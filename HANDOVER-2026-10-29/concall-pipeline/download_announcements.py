"""
Multi-category announcement downloader for Screener.in

Usage:
  python download_announcements.py                              # manual, no batch
  python download_announcements.py --auto --batch=morning
  python download_announcements.py --auto --batch=evening

Includes:
- Browser fingerprint spoofing (User-Agent + Referer) to avoid BSE/NSE
  bot-detection 403 errors when running headless.
- safe_filename() normalizes ALL whitespace (newlines, tabs) BEFORE
  stripping special characters - prevents [Errno 22] Invalid argument
  errors from multi-line title text.
- 10 curated categories matching Screener filter pill text exactly,
  including quoted variants like '"Credit Rating"' which are saved
  custom searches with literal quotes in the pill display text.
"""

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from datetime import datetime
import argparse
import os
import re
import time
import hashlib

load_dotenv()
EMAIL = os.getenv("SCREENER_EMAIL")
PASSWORD = os.getenv("SCREENER_PASSWORD")

parser = argparse.ArgumentParser()
parser.add_argument('--auto', action='store_true')
parser.add_argument('--batch', choices=['morning', 'evening'])
args, _ = parser.parse_known_args()

AUTOMATED = args.auto
BATCH = args.batch
REQUEST_DELAY = 3
DOWNLOAD_FOLDER = "results_downloads"
DOWNLOADED_URLS_FILE = os.path.join(DOWNLOAD_FOLDER, ".downloaded_urls.txt")

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
)
DOWNLOAD_HEADERS = {
    'User-Agent': USER_AGENT,
    'Referer': 'https://www.screener.in/',
    'Accept': 'application/pdf,application/octet-stream,*/*',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Filter pill names matching exact Screener display text.
# Quoted entries (e.g. '"Credit Rating"') are saved custom searches
# where the quotes are part of the pill's displayed text.
# Excludes: "Concall" and "Earnings Call Transcript" (covered by
# download_today.py via the /concalls/ page).
CATEGORIES = [
    "Important",
    "Results",
    "Capacity Increase",
    "Scheme Of Arrangement",
    "Order Win",
    '"Scheme Of Arrangement"',
    '"Capacity Expansion"',
    "Qip",
    '"Credit Rating"',
    '"Operational Update"',
]


def safe_filename(s):
    """Build a filename-safe string from arbitrary text.
    Normalizes ALL whitespace (incl. newlines, tabs) FIRST so multi-line
    title text from Screener doesn't break paths."""
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'[^\w\s-]', '', s)
    return s.replace(' ', '_')[:80]


def safe_folder_name(s):
    """Build a folder-safe lowercase string. Strips quotes so saved-search
    pills like '"Credit Rating"' produce clean folder names like
    'credit_rating' instead of '_credit_rating_'."""
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.replace('"', '').replace("'", '')
    return re.sub(r'[^\w\s-]', '', s).replace(' ', '_').lower()


os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
today_str = datetime.now().date().isoformat()

if os.path.exists(DOWNLOADED_URLS_FILE):
    with open(DOWNLOADED_URLS_FILE, encoding='utf-8') as f:
        downloaded_urls = set(line.strip() for line in f if line.strip())
else:
    downloaded_urls = set()
print(f"Mode: {'AUTOMATED (headless)' if AUTOMATED else 'MANUAL (visible)'}")
print(f"Batch: {BATCH if BATCH else 'NONE (flat folder)'}")
print(f"Categories: {len(CATEGORIES)} configured")
print(f"Tracking {len(downloaded_urls)} previously downloaded URLs (dedup memory)")


def get_target_folder(category_name):
    if BATCH:
        return os.path.join(
            DOWNLOAD_FOLDER, today_str, BATCH, safe_folder_name(category_name)
        )
    return os.path.join(
        DOWNLOAD_FOLDER, today_str, safe_folder_name(category_name)
    )


def download_for_current_filter(page, category_name):
    folder = get_target_folder(category_name)
    os.makedirs(folder, exist_ok=True)

    pdf_links = page.locator('a[href*=".pdf"]').all()
    if len(pdf_links) == 0:
        pdf_links = page.locator(
            'a[href*="bseindia.com"], a[href*="nseindia.com"]'
        ).all()

    print(f"  Found {len(pdf_links)} PDF links in '{category_name}'")

    cat_dl, cat_skip, cat_fail = 0, 0, 0

    for i, link in enumerate(pdf_links):
        try:
            pdf_url = link.get_attribute("href")
            title = link.inner_text().strip()

            if not pdf_url:
                continue
            if pdf_url.startswith("/"):
                pdf_url = "https://www.screener.in" + pdf_url

            if pdf_url in downloaded_urls:
                cat_skip += 1
                continue

            company = "Unknown"
            try:
                container = link.locator(
                    'xpath=ancestor::*[descendant::a[contains(@href, "/company/")]][1]'
                )
                if container.count() > 0:
                    company_link = container.locator('a[href*="/company/"]').first
                    company = company_link.inner_text().strip()
            except Exception:
                pass

            url_hash = hashlib.md5(pdf_url.encode()).hexdigest()[:6]
            filename = os.path.join(
                folder,
                f"{safe_filename(company)}_{safe_filename(title)[:40]}_{url_hash}.pdf"
            )

            time.sleep(REQUEST_DELAY)

            title_log = re.sub(r'\s+', ' ', title)[:60]
            print(f"    [{i+1}] {company[:25]:<25} | {title_log}")
            response = page.context.request.get(pdf_url, headers=DOWNLOAD_HEADERS)

            if response.ok:
                with open(filename, "wb") as f:
                    f.write(response.body())
                size_kb = len(response.body()) / 1024
                print(f"        Saved ({size_kb:.0f} KB)")
                cat_dl += 1
                downloaded_urls.add(pdf_url)
                with open(DOWNLOADED_URLS_FILE, "a", encoding='utf-8') as f:
                    f.write(pdf_url + "\n")
            else:
                print(f"        Failed: HTTP {response.status}")
                cat_fail += 1

        except Exception as e:
            print(f"    Error on link {i+1}: {str(e)[:80]}")
            cat_fail += 1

    return cat_dl, cat_skip, cat_fail, len(pdf_links)


with sync_playwright() as p:
    launch_args = ['--disable-blink-features=AutomationControlled'] if AUTOMATED else []
    browser = p.chromium.launch(headless=AUTOMATED, args=launch_args)

    context = browser.new_context(
        user_agent=USER_AGENT,
        viewport={'width': 1920, 'height': 1080},
    )
    page = context.new_page()

    print("\nLogging in...")
    # Don't wait for the full "load" event (slow third-party resources on the
    # login page were timing out and crashing the whole run); domcontentloaded
    # is enough to interact with the form. Retry once on a transient timeout.
    # Back-ported from download_today.py (2026-07-27 login-timeout fix).
    for _attempt in range(2):
        try:
            page.goto(
                "https://www.screener.in/login/",
                wait_until="domcontentloaded",
                timeout=60000,
            )
            break
        except Exception as e:
            if _attempt == 1:
                raise
            print(f"  Login page load failed ({e}); retrying...")
            page.wait_for_timeout(3000)
    page.fill('input[name="username"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state("domcontentloaded")
    print("Logged in")

    print("\nGoing to announcements page...")
    # Same domcontentloaded + timeout hardening as the login goto above, so a
    # slow-loading announcements page can't hang the whole evening run.
    page.goto(
        "https://www.screener.in/announcements/",
        wait_until="domcontentloaded",
        timeout=60000,
    )
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)

    total_dl, total_skip, total_fail = 0, 0, 0
    total_links_found = 0
    completed_cats = []
    skipped_cats = []

    for category in CATEGORIES:
        print(f"\n{'='*55}")
        print(f"CATEGORY: {category}")
        print(f"{'='*55}")

        try:
            filter_button = page.get_by_text(category, exact=True).first
            filter_button.click(timeout=10000)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(2500)
            print(f"  Filter '{category}' applied")
        except Exception as e:
            print(f"  Could not click filter '{category}': {str(e)[:80]}")
            print(f"  Skipping category")
            skipped_cats.append(category)
            continue

        d, s, f, links = download_for_current_filter(page, category)
        total_dl += d
        total_skip += s
        total_fail += f
        total_links_found += links
        completed_cats.append(category)

    print(f"\n{'='*55}")
    print(f"OVERALL RUN SUMMARY")
    print(f"{'='*55}")
    print(f"  Batch:                {BATCH if BATCH else 'flat'}")
    print(f"  Categories completed: {len(completed_cats)} of {len(CATEGORIES)}")
    if skipped_cats:
        print(f"  Categories skipped:   {', '.join(skipped_cats)}")
    print(f"  Total links found:    {total_links_found}")
    print(f"  Total downloaded:     {total_dl}")
    print(f"  Total skipped (dup):  {total_skip}")
    print(f"  Total failed:         {total_fail}")
    print(f"{'='*55}")

    # ---- Guardrail: detect silent failures ----------------------------------
    # Mirrors the greppable WARNING guardrail added to download_today.py on
    # 2026-07-27. This downloader has NO date parsing (it pulls by category
    # filter pill, not by row date), so the "cannot parse date" failure mode
    # does not apply here. The equivalent silent-failure signatures are:
    #   1. Every category filter click failed -> not logged in, OR the
    #      announcements page / filter-pill layout changed.
    #   2. Filters applied but zero PDF links were found anywhere AND nothing
    #      was downloaded/skipped/failed -> the PDF-link selector likely broke
    #      (could be a legitimate quiet batch, but flag if it repeats).
    # Grep the log for "WARNING:" to alert on either.
    if len(completed_cats) == 0:
        print("WARNING: ALL categories were skipped - every filter pill click "
              "failed. Login likely failed OR the announcements page / filter "
              "layout changed. Announcement downloads are BROKEN until fixed.")
    elif (total_links_found == 0 and total_dl == 0
          and total_skip == 0 and total_fail == 0):
        print("WARNING: filters applied but NO PDF links were found in any "
              "category and nothing was downloaded. May be a legitimate empty "
              "batch, but if it repeats verify the a[href*=\".pdf\"] selector "
              "and the announcements page layout.")
    elif skipped_cats:
        print(f"WARNING: {len(skipped_cats)} of {len(CATEGORIES)} category "
              f"filters could not be applied ({', '.join(skipped_cats)}) - "
              "partial layout issue; review the filter-pill names/selectors.")
    # -------------------------------------------------------------------------

    if not AUTOMATED:
        input("\nPress Enter to close browser...")
    browser.close()
