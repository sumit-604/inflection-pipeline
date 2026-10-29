"""
Download today's concall transcripts from Screener.

Usage:
  python download_today.py                              # manual, no batch
  python download_today.py --auto --batch=morning       # automated, save to <date>/morning/
  python download_today.py --auto --batch=evening       # automated, save to <date>/evening/

Includes browser fingerprint spoofing (User-Agent + Referer) to avoid
BSE/NSE bot-detection 403 errors when running headless.
"""

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from datetime import datetime
import argparse
import os
import re
import time

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
CUTOFF_DATE = datetime.now().date()
DOWNLOAD_FOLDER = "downloads"

# Browser fingerprint to avoid BSE/NSE 403 in headless mode
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


def safe_filename(s):
    return re.sub(r'[^\w\s-]', '', s).replace(' ', '_')[:80]


# Locale-independent month lookup (full names + common abbreviations).
# Avoids strptime %b/%B, which is locale-sensitive and was silently failing
# on the production Windows box for every month except May.
_MONTHS = {}
for _i, _full in enumerate(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'], 1):
    _MONTHS[_full.lower()] = _i
    _MONTHS[_full[:3].lower()] = _i
_MONTHS['sept'] = 9  # screener sometimes renders "Sept"


def parse_pub_date(date_str):
    """Parse Screener publish dates like '24 July 2026' / '24 Jul 2026'.

    Normalizes non-breaking / narrow spaces (which .strip() does NOT remove
    and which break strptime's literal-space formats), then maps the month
    name explicitly so parsing does not depend on the OS locale.
    Raises ValueError if the string cannot be parsed.
    """
    s = (date_str or '').replace('\xa0', ' ').replace(' ', ' ').replace(' ', ' ')
    s = ' '.join(s.split())
    m = re.match(r'^(\d{1,2})\s+([A-Za-z]+)\.?\s+(\d{4})$', s)
    if not m:
        raise ValueError(f"unrecognized date format: {date_str!r}")
    day, mon, year = m.groups()
    mon_num = _MONTHS.get(mon.lower())
    if not mon_num:
        raise ValueError(f"unknown month {mon!r} in {date_str!r}")
    return datetime(int(year), mon_num, int(day)).date()


def transcript_already_downloaded(company, date_str):
    date_dir = os.path.join(DOWNLOAD_FOLDER, date_str)
    if not os.path.exists(date_dir):
        return False
    target_name = f"{safe_filename(company)}.pdf"
    if os.path.exists(os.path.join(date_dir, target_name)):
        return True
    for entry in os.listdir(date_dir):
        entry_path = os.path.join(date_dir, entry)
        if os.path.isdir(entry_path):
            if os.path.exists(os.path.join(entry_path, target_name)):
                return True
    return False


with sync_playwright() as p:
    launch_args = ['--disable-blink-features=AutomationControlled'] if AUTOMATED else []
    browser = p.chromium.launch(headless=AUTOMATED, args=launch_args)

    context = browser.new_context(
        user_agent=USER_AGENT,
        viewport={'width': 1920, 'height': 1080},
    )
    page = context.new_page()

    print(f"Mode: {'AUTOMATED (headless)' if AUTOMATED else 'MANUAL (visible)'}")
    print(f"Batch: {BATCH if BATCH else 'NONE (flat folder)'}")
    print("Logging in...")
    # Don't wait for the full "load" event (slow third-party resources on the
    # login page were timing out and crashing the whole run); domcontentloaded
    # is enough to interact with the form. Retry once on a transient timeout.
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

    print("\nGoing to concalls page...")
    page.goto("https://www.screener.in/concalls/")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)

    print("Applying Transcript filter...")
    page.get_by_text("Transcript", exact=True).click()
    page.wait_for_timeout(2000)
    print("Transcript filter applied")

    rows = page.locator('table tbody tr').all()
    print(f"\nFound {len(rows)} rows. Looking for transcripts from {CUTOFF_DATE} onwards.\n")

    downloaded = 0
    skipped_dup = 0
    failed = 0
    parse_failures = 0
    rows_found = len(rows)

    for i, row in enumerate(rows):
        try:
            cells = row.locator('th, td').all()
            if len(cells) < 3:
                continue

            company = cells[0].inner_text().strip()
            date_str = cells[1].inner_text().strip()

            try:
                pub_date = parse_pub_date(date_str)
            except ValueError:
                print(f"  Skip {company}: cannot parse date '{date_str}'")
                parse_failures += 1
                continue

            if pub_date < CUTOFF_DATE:
                print(f"\nReached older date ({pub_date}) - stopping.")
                break

            link_loc = row.locator('a:has-text("View Transcript")')
            if link_loc.count() == 0:
                continue

            url = link_loc.first.get_attribute("href")
            if url.startswith("/"):
                url = "https://www.screener.in" + url

            pub_date_str = pub_date.isoformat()

            if transcript_already_downloaded(company, pub_date_str):
                print(f"  Skip (already downloaded): {company}")
                skipped_dup += 1
                continue

            if BATCH:
                target_folder = os.path.join(
                    DOWNLOAD_FOLDER, pub_date_str, BATCH
                )
            else:
                target_folder = os.path.join(DOWNLOAD_FOLDER, pub_date_str)

            os.makedirs(target_folder, exist_ok=True)
            filename = os.path.join(target_folder, f"{safe_filename(company)}.pdf")

            time.sleep(REQUEST_DELAY)

            print(f"  Downloading: {company} ({pub_date}) -> {target_folder}")
            response = page.context.request.get(url, headers=DOWNLOAD_HEADERS)

            if response.ok:
                with open(filename, "wb") as f:
                    f.write(response.body())
                size_kb = len(response.body()) / 1024
                print(f"    Saved ({size_kb:.0f} KB)")
                downloaded += 1
            else:
                print(f"    Failed: HTTP {response.status}")
                failed += 1

        except Exception as e:
            print(f"  Error on row {i+1}: {e}")
            failed += 1

    print(f"\n{'='*45}")
    print(f"Run summary for {CUTOFF_DATE}:")
    print(f"  Mode:              {BATCH if BATCH else 'flat'}")
    print(f"  Rows found:        {rows_found}")
    print(f"  Downloaded:        {downloaded}")
    print(f"  Skipped (already): {skipped_dup}")
    print(f"  Skipped (parse):   {parse_failures}")
    print(f"  Failed:            {failed}")
    print(f"{'='*45}")

    # ---- Guardrail: detect silent failures ----------------------------------
    # A run that finds rows but can neither parse nor download anything is the
    # exact signature of the May-Jul 2026 date-format outage. Emit a loud,
    # greppable WARNING so it never passes unnoticed again. Grep the log for
    # "WARNING:" to alert on it.
    if rows_found > 0 and parse_failures == rows_found:
        print("WARNING: ALL rows failed date parsing - Screener date format "
              "likely changed. Concall downloads are BROKEN until fixed. "
              "Check parse_pub_date() against the current page.")
    elif rows_found > 0 and downloaded == 0 and skipped_dup == 0 and failed == 0:
        print("WARNING: rows were found but nothing was downloaded, skipped as "
              "duplicate, or failed. This may be a legitimate zero-day, but if "
              "it repeats, verify the concalls page layout and date parsing.")
    elif parse_failures > 0:
        print(f"WARNING: {parse_failures} of {rows_found} rows failed date "
              "parsing - partial format issue; review parse_pub_date().")
    # -------------------------------------------------------------------------

    if not AUTOMATED:
        input("\nPress Enter to close browser...")
    browser.close()
