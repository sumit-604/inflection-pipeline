"""
One-off backfill downloader for concall transcripts.

Same logic as download_today.py, but accepts --since YYYY-MM-DD so you can
pull transcripts newer than any date you choose (e.g. anything from Oct 6
onwards after a weekend of pipeline outages).

Usage (from the pipeline folder):
    python download_backfill_win.py --since 2026-10-06 --batch morning

Writes PDFs into downloads\<pub_date>\<batch>\<Company>.pdf, same layout as
download_today.py so the normal analysis task picks them up.
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
parser.add_argument('--since', required=True, help='Earliest pub date YYYY-MM-DD (inclusive)')
parser.add_argument('--batch', default='morning', choices=['morning', 'evening'])
parser.add_argument('--download-folder', default='downloads')
args = parser.parse_args()

CUTOFF_DATE = datetime.strptime(args.since, '%Y-%m-%d').date()
BATCH = args.batch
DOWNLOAD_FOLDER = args.download_folder
REQUEST_DELAY = 3

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


_MONTHS = {}
for _i, _full in enumerate(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'], 1):
    _MONTHS[_full.lower()] = _i
    _MONTHS[_full[:3].lower()] = _i
_MONTHS['sept'] = 9


def parse_pub_date(date_str):
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


def already_downloaded(company, pub_date_str):
    """Match download_today.py's dedup logic: look under <date>/, <date>/<batch>/"""
    date_dir = os.path.join(DOWNLOAD_FOLDER, pub_date_str)
    target = f"{safe_filename(company)}.pdf"
    if os.path.exists(os.path.join(date_dir, target)):
        return True
    if os.path.isdir(date_dir):
        for entry in os.listdir(date_dir):
            p = os.path.join(date_dir, entry)
            if os.path.isdir(p) and os.path.exists(os.path.join(p, target)):
                return True
    return False


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=['--disable-blink-features=AutomationControlled'],
    )
    context = browser.new_context(
        user_agent=USER_AGENT,
        viewport={'width': 1920, 'height': 1080},
    )
    page = context.new_page()

    print(f"BACKFILL: downloading transcripts dated {CUTOFF_DATE} or newer, batch={BATCH}")
    print("Logging in...")
    for attempt in range(2):
        try:
            page.goto("https://www.screener.in/login/", wait_until="domcontentloaded", timeout=60000)
            break
        except Exception as e:
            if attempt == 1:
                raise
            print(f"  retry login page: {e}")
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
    print(f"\nFound {len(rows)} rows visible. Downloading those on/after {CUTOFF_DATE}.\n")

    downloaded = 0
    skipped_dup = 0
    failed = 0
    stopped_at = None

    for i, row in enumerate(rows):
        try:
            cells = row.locator('th, td').all()
            if len(cells) < 3:
                continue
            company = cells[0].inner_text().strip()
            date_str = cells[1].inner_text().strip()

            try:
                pub_date = parse_pub_date(date_str)
            except ValueError as e:
                print(f"  Skip {company}: {e}")
                continue

            if pub_date < CUTOFF_DATE:
                print(f"\nRow {i+1} ({company}) is {pub_date}, older than cutoff. Stopping.")
                stopped_at = pub_date
                break

            link_loc = row.locator('a:has-text("View Transcript")')
            if link_loc.count() == 0:
                continue
            url = link_loc.first.get_attribute("href")
            if url.startswith("/"):
                url = "https://www.screener.in" + url

            pub_date_str = pub_date.isoformat()
            if already_downloaded(company, pub_date_str):
                print(f"  Skip (already have): {company} ({pub_date})")
                skipped_dup += 1
                continue

            target_folder = os.path.join(DOWNLOAD_FOLDER, pub_date_str, BATCH)
            os.makedirs(target_folder, exist_ok=True)
            filename = os.path.join(target_folder, f"{safe_filename(company)}.pdf")

            time.sleep(REQUEST_DELAY)
            print(f"  Downloading: {company} ({pub_date})")
            response = page.context.request.get(url, headers=DOWNLOAD_HEADERS)
            if response.ok:
                with open(filename, "wb") as f:
                    f.write(response.body())
                size_kb = len(response.body()) / 1024
                print(f"    Saved ({size_kb:.0f} KB) -> {filename}")
                downloaded += 1
            else:
                print(f"    Failed: HTTP {response.status}")
                failed += 1
        except Exception as e:
            print(f"  Error on row {i+1}: {e}")
            failed += 1

    print(f"\n{'='*45}")
    print(f"BACKFILL summary (--since {CUTOFF_DATE}):")
    print(f"  Rows visible:      {len(rows)}")
    print(f"  Downloaded:        {downloaded}")
    print(f"  Skipped (already): {skipped_dup}")
    print(f"  Failed:            {failed}")
    if stopped_at:
        print(f"  Stopped at row older than cutoff ({stopped_at})")
    print(f"{'='*45}")

    browser.close()
