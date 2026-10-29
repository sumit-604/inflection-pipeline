"""
download_feed.py — Screener.in personal feed downloader (watchlist-driven)

Scrapes https://www.screener.in/ — the root page after login, which renders
the Core Watchlist activity stream (the page Sumit screenshotted). It is
already filtered to companies he follows on Screener, so every announcement
PDF found here is in-scope.

NOTE: there is NO /feed/ endpoint — that path returns 404. The feed lives
at the authenticated root.

Each scheduled-task run writes PDFs into:
    results_downloads_feed/<YYYY-MM-DD>/<HHMM>/<safe_company>_<title>_<hash>.pdf

Persistent dedup: results_downloads_feed/.downloaded_feed_urls.txt accumulates
URL hashes across runs forever. Items already downloaded are skipped silently.

Usage:
    python download_feed.py                 # visible browser, interactive
    python download_feed.py --auto          # headless, for scheduled task

Stdout finishes with a single SUMMARY line that the scheduled task parses:
    SUMMARY: slot=<YYYY-MM-DD>/<HHMM> downloaded=<N> skipped=<N> failed=<N>
"""

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from datetime import datetime
import argparse
import hashlib
import os
import re
import sys
import time

load_dotenv()
EMAIL = os.getenv("SCREENER_EMAIL")
PASSWORD = os.getenv("SCREENER_PASSWORD")

parser = argparse.ArgumentParser()
parser.add_argument("--auto", action="store_true",
                    help="Headless mode for scheduled runs")
parser.add_argument("--max-scrolls", type=int, default=12,
                    help="How many infinite-scroll steps to attempt (default 12)")
args, _ = parser.parse_known_args()

AUTOMATED = args.auto
MAX_SCROLLS = args.max_scrolls
REQUEST_DELAY = 2.5

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "results_downloads_feed")
DEDUP_FILE = os.path.join(DOWNLOAD_ROOT, ".downloaded_feed_urls.txt")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
DOWNLOAD_HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": "https://www.screener.in/",
    "Accept": "application/pdf,application/octet-stream,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def safe_filename(s: str) -> str:
    """Collapse whitespace first, then strip special chars — guards against
    multi-line announcement titles that would otherwise produce Errno 22."""
    s = re.sub(r"\s+", " ", s or "").strip()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.replace(" ", "_")[:80]


def load_dedup_set() -> set:
    os.makedirs(DOWNLOAD_ROOT, exist_ok=True)
    if not os.path.exists(DEDUP_FILE):
        return set()
    with open(DEDUP_FILE, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}


def append_dedup(url: str) -> None:
    with open(DEDUP_FILE, "a", encoding="utf-8") as f:
        f.write(url + "\n")


def now_slot():
    n = datetime.now()
    return n.strftime("%Y-%m-%d"), n.strftime("%H%M")


def is_pdf_or_filing_url(href: str) -> bool:
    if not href:
        return False
    h = href.lower()
    if ".pdf" in h:
        return True
    if "bseindia.com" in h or "nseindia.com" in h:
        return True
    # Screener's own document redirect endpoints
    if "/api/" in h and ("document" in h or "attachment" in h):
        return True
    return False


def main() -> int:
    # Force line-buffered stdout/stderr — under `>> log.txt 2>&1` redirection,
    # default Python buffers progress prints for tens of seconds, making the
    # script look hung. Belt-and-braces with `python -u` in the .bat.
    # UTF-8 with replace: under redirection Windows defaults to cp1252, and a
    # single non-ASCII char in an error message (e.g. Playwright's "→") used
    # to raise inside the except block and kill the whole run.
    try:
        sys.stdout.reconfigure(line_buffering=True, encoding="utf-8",
                               errors="replace")
        sys.stderr.reconfigure(line_buffering=True, encoding="utf-8",
                               errors="replace")
    except Exception:
        pass

    print(
        f"[{datetime.now().isoformat(timespec='seconds')}] Starting "
        f"download_feed.py (this takes ~60-120s — do NOT close the window)",
        flush=True,
    )

    if not EMAIL or not PASSWORD:
        print("ERROR: SCREENER_EMAIL / SCREENER_PASSWORD not set in .env",
              flush=True)
        return 2

    today_str, slot_str = now_slot()
    target_folder = os.path.join(DOWNLOAD_ROOT, today_str, slot_str)
    os.makedirs(target_folder, exist_ok=True)

    dedup = load_dedup_set()
    print(f"Mode: {'AUTOMATED (headless)' if AUTOMATED else 'MANUAL (visible)'}",
          flush=True)
    print(f"Slot: {today_str}/{slot_str}", flush=True)
    print(f"Target folder: {target_folder}", flush=True)
    print(f"Dedup memory: {len(dedup)} prior URLs", flush=True)

    downloaded = skipped = failed = seen_items = 0

    with sync_playwright() as p:
        launch_args = (
            ["--disable-blink-features=AutomationControlled"] if AUTOMATED else []
        )
        browser = p.chromium.launch(headless=AUTOMATED, args=launch_args)
        context = browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1920, "height": 1080},
        )
        page = context.new_page()

        print("\nLogging in...", flush=True)
        page.goto("https://www.screener.in/login/")
        page.fill('input[name="username"]', EMAIL)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("domcontentloaded")
        if "login" in page.url:
            print("ERROR: login failed", flush=True)
            browser.close()
            return 3
        print("Logged in", flush=True)

        # The feed lives at the root after login — `/feed/` returns a 404.
        # Once authenticated, https://www.screener.in/ renders the Core
        # Watchlist activity stream (the page Sumit screenshotted).
        print("\nGoing to feed (screener.in root, post-login)...", flush=True)
        page.goto("https://www.screener.in/")
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(3000)

        # Trigger infinite scroll a few times to load enough history that we
        # don't miss anything posted between scheduled runs.
        for i in range(MAX_SCROLLS):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1500)

        # Find every anchor that looks like an attachment/filing PDF. Screener
        # renders feed cards as <a> with the announcement title as link text;
        # the href can be a direct PDF, a BSE/NSE deep link, or a Screener
        # /api/.../document/ redirect.
        all_links = page.locator("a").all()
        print(f"\nScanned {len(all_links)} anchors on the loaded feed.",
              flush=True)

        for i, link in enumerate(all_links):
            try:
                href = link.get_attribute("href") or ""
                if not is_pdf_or_filing_url(href):
                    continue

                seen_items += 1
                if href.startswith("/"):
                    href = "https://www.screener.in" + href

                if href in dedup:
                    skipped += 1
                    continue

                title = link.inner_text().strip() or "untitled"
                # Walk up the DOM to find the owning company card (Screener
                # places a company link in the same card container).
                company = "Unknown"
                try:
                    container = link.locator(
                        'xpath=ancestor::*[descendant::a[contains(@href, "/company/")]][1]'
                    )
                    if container.count() > 0:
                        company_link = container.locator(
                            'a[href*="/company/"]'
                        ).first
                        company = company_link.inner_text().strip()
                except Exception:
                    pass

                url_hash = hashlib.md5(href.encode()).hexdigest()[:6]
                fname = (
                    f"{safe_filename(company)}_"
                    f"{safe_filename(title)[:40]}_{url_hash}.pdf"
                )
                fpath = os.path.join(target_folder, fname)

                time.sleep(REQUEST_DELAY)
                title_log = re.sub(r"\s+", " ", title)[:60]
                print(f"  [{seen_items}] {company[:25]:<25} | {title_log}",
                      flush=True)

                resp = page.context.request.get(
                    href, headers=DOWNLOAD_HEADERS, max_redirects=5
                )

                if not resp.ok:
                    print(f"      Failed: HTTP {resp.status}", flush=True)
                    failed += 1
                    continue

                body = resp.body()
                if len(body) < 1024:
                    print(f"      Skipped: too small ({len(body)} B)",
                          flush=True)
                    failed += 1
                    continue
                # Quick magic-byte sniff: real PDF starts with %PDF-
                if not body.startswith(b"%PDF"):
                    # Some BSE attachments are zipped — keep them anyway but
                    # mark in filename so the analyzer can ignore.
                    fpath = fpath[:-4] + ".bin"

                with open(fpath, "wb") as f:
                    f.write(body)
                size_kb = len(body) / 1024
                print(f"      Saved ({size_kb:.0f} KB)", flush=True)
                downloaded += 1
                dedup.add(href)
                append_dedup(href)

            except Exception as e:
                print(f"  Error on anchor {i+1}: {str(e)[:120]}", flush=True)
                failed += 1

        browser.close()

    # If the slot folder ended up empty, remove it so the analyzer's "no PDFs"
    # check fires cleanly.
    try:
        if os.path.isdir(target_folder) and not os.listdir(target_folder):
            os.rmdir(target_folder)
    except OSError:
        pass

    print("\n" + "=" * 55, flush=True)
    print(f"Slot:        {today_str}/{slot_str}", flush=True)
    print(f"Items seen:  {seen_items}", flush=True)
    print(f"Downloaded:  {downloaded}", flush=True)
    print(f"Skipped:     {skipped}", flush=True)
    print(f"Failed:      {failed}", flush=True)
    print("=" * 55, flush=True)
    print(
        f"SUMMARY: slot={today_str}/{slot_str} "
        f"downloaded={downloaded} skipped={skipped} failed={failed}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
