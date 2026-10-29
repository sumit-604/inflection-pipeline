"""
fetch_announcements.py — download every Screener watchlist announcement
since a cutoff time into ONE folder.

Replaces the 4-hourly download_feed.py. Screener's feed (screener.in root
after login) shows 25 items per page and a "Show More" button whose
data-last-timestamp holds the time of the page's oldest item. Scrolling does
not load more, so this script requests the next pages directly (the same
GET the button sends) until that timestamp is older than the cutoff.

Output:
    announcements/<since>_to_<now>/<Company>_<Title>_<hash>.pdf
    announcements/<since>_to_<now>/INDEX.md   (count + one row per item)
    announcements/<since>_to_<now>/companies.json   (company -> screener page)

Cutoff:
    --since "YYYY-MM-DD HH:MM"   explicit
    otherwise the end time of the last successful run (last_run.txt)

Day filter: Screener groups items under day headings (Today, Yesterday,
"1 Oct" ...). Items are kept when their day is on or after the cutoff day,
so the first day can include a few items from before the cutoff hour.

Usage:
    python fetch_announcements.py --since "2026-10-01 07:00"
    python fetch_announcements.py          # daily 05:00 run
"""

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from datetime import date, datetime, timedelta
import argparse
import hashlib
import json
import os
import re
import requests
import sys
import time

load_dotenv()
EMAIL = os.getenv("SCREENER_EMAIL")
PASSWORD = os.getenv("SCREENER_PASSWORD")

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.join(PROJECT_ROOT, "announcements")
STATE_FILE = os.path.join(OUT_ROOT, "last_run.txt")
MAX_PAGES = 200
REQUEST_DELAY = 1.5

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

def extract_items(html: str) -> list:
    """Every feed item, with the day heading that precedes it."""
    out, day = [], None
    for li in BeautifulSoup(html, "html.parser").find_all("li"):
        cls = li.get("class") or []
        if "news-item-section-title" in cls:
            day = li.get_text(strip=True)
            continue
        if "news-item" not in cls:
            continue
        co = li.find("a", href=re.compile(r"/company/"))
        doc = next((a for a in li.find_all("a", href=True)
                    if "/company/" not in a["href"]), None)
        summ = li.find("div", class_="ink-600")
        href = doc["href"] if doc else ""
        if href.startswith("/"):
            href = "https://www.screener.in" + href
        co_url = co["href"] if co else ""
        if co_url.startswith("/"):
            co_url = "https://www.screener.in" + co_url
        out.append({
            "day": day,
            "company": co.get_text(" ", strip=True) if co else "Unknown",
            "company_url": co_url,
            "title": doc.get_text(" ", strip=True) if doc else "untitled",
            "href": href,
            "summary": summ.get_text(" ", strip=True) if summ else "",
        })
    return out


def safe_filename(s: str) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.replace(" ", "_")[:80]


def parse_day(label: str, today: date):
    """'Today' / 'Yesterday' / '1 Oct' / '1 Oct 2026' -> date (None if unknown)."""
    if not label:
        return None
    l = label.strip()
    if l.lower() == "today":
        return today
    if l.lower() == "yesterday":
        return today - timedelta(days=1)
    for fmt in ("%d %b %Y", "%d %B %Y"):
        try:
            return datetime.strptime(l, fmt).date()
        except ValueError:
            pass
    for fmt in ("%d %b", "%d %B"):
        try:
            d = datetime.strptime(l, fmt).date().replace(year=today.year)
            return d if d <= today else d.replace(year=today.year - 1)
        except ValueError:
            pass
    return None


# Big documents the operator wants called out on their own, checked in order.
KEY_DOC_KINDS = [
    ("Annual reports", r"annual report|reg\.? ?34"),
    ("Concall transcripts", r"transcript"),
    ("Investor presentations", r"presentation|investor deck|earnings deck"),
    ("Concall audio / video links", r"audio|video recording|recording of"),
    ("Investor meet / concall notices (upcoming)",
     r"analyst|investor meet|institutional investor|con\.? ?call|earnings call"),
]


def key_documents(rows, out_dir) -> list:
    """Markdown section listing annual reports, transcripts, presentations
    and meeting notices, with page counts, ahead of the full table."""
    try:
        import pymupdf
    except ImportError:
        pymupdf = None
    groups = {k: [] for k, _ in KEY_DOC_KINDS}
    for r in rows:
        text = f"{r['title']} {r['summary']}".lower()
        for kind, pat in KEY_DOC_KINDS:
            if re.search(pat, text):
                groups[kind].append(r)
                break
    out = ["## Key documents", ""]
    for kind, items in groups.items():
        out.append(f"**{kind}: {len(items)}**")
        for r in sorted(items, key=lambda r: r["company"]):
            pages = ""
            path = os.path.join(out_dir, r["file"])
            if pymupdf and r["file"].endswith(".pdf") and os.path.exists(path):
                try:
                    pages = f", {pymupdf.open(path).page_count} pages"
                except Exception:
                    pass
            out.append(f"- {r['company']}: {r['title']} ({r['date']:%d %b}{pages}) "
                       f"{r['summary']}".rstrip())
        out.append("")
    return out


def incomplete(body: bytes, declared) -> str:
    """Why a downloaded file looks cut short, or "" if it looks whole.
    A PDF must end with %%EOF; a body shorter than Content-Length is cut.
    (Zota 15-Oct-2026: NSE's archive copy itself is 262,144 bytes, no %%EOF.)"""
    if declared and declared.isdigit() and len(body) < int(declared):
        return f"got {len(body):,} of {int(declared):,} bytes"
    if body.startswith(b"%PDF") and b"%%EOF" not in body[-2048:]:
        return f"no PDF end marker at {len(body):,} bytes"
    return ""


def fetch_pdf(context, url: str):
    """Returns (body, partial_reason). Playwright first; requests as fallback
    (NSE archives sometimes send a header Playwright's strict parser rejects).
    A cut-short body is retried once with requests before it is accepted."""
    best = None
    try:
        resp = context.request.get(url, headers=DOWNLOAD_HEADERS,
                                   max_redirects=5, timeout=60000)
        body = resp.body() if resp.ok else b""
        if len(body) >= 1024:
            why = incomplete(body, resp.headers.get("content-length"))
            if not why:
                return body, ""
            best = (body, why)
        err = f"HTTP {resp.status}, {len(body)} B"
    except Exception as e:
        err = str(e)[:80]
    r = requests.get(url, headers=DOWNLOAD_HEADERS, timeout=120)
    if r.ok and len(r.content) >= 1024:
        why = incomplete(r.content, r.headers.get("Content-Length"))
        if not why or best is None or len(r.content) > len(best[0]):
            return r.content, why
    if best:
        return best
    raise RuntimeError(f"{err}; fallback HTTP {r.status_code}, {len(r.content)} B")


def main() -> int:
    try:
        sys.stdout.reconfigure(line_buffering=True, encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(line_buffering=True, encoding="utf-8", errors="replace")
    except Exception:
        pass

    parser = argparse.ArgumentParser()
    parser.add_argument("--since", help='"YYYY-MM-DD HH:MM" (default: last_run.txt)')
    args = parser.parse_args()

    os.makedirs(OUT_ROOT, exist_ok=True)
    if args.since:
        since = datetime.strptime(args.since, "%Y-%m-%d %H:%M")
    elif os.path.exists(STATE_FILE):
        since = datetime.strptime(open(STATE_FILE).read().strip(), "%Y-%m-%d %H:%M")
    else:
        print("ERROR: no --since and no last_run.txt", flush=True)
        return 2
    if not EMAIL or not PASSWORD:
        print("ERROR: SCREENER_EMAIL / SCREENER_PASSWORD not set in .env", flush=True)
        return 2

    started = datetime.now()
    label = f"{since:%Y-%m-%d_%H%M}_to_{started:%Y-%m-%d_%H%M}"
    out_dir = os.path.join(OUT_ROOT, label)
    os.makedirs(out_dir, exist_ok=True)
    print(f"[{started:%Y-%m-%d %H:%M:%S}] since {since:%Y-%m-%d %H:%M} -> {out_dir}")

    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(user_agent=USER_AGENT,
                                      viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        page.goto("https://www.screener.in/login/")
        page.fill('input[name="username"]', EMAIL)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("domcontentloaded")
        if "login" in page.url:
            print("ERROR: login failed", flush=True)
            browser.close()
            return 3

        page.goto("https://www.screener.in/")
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(2000)

        # "Show More" runs Dash.loadNextPage: GET <data-load-more>?timestamp=<ts>
        # returns the next 25 items as an HTML fragment ending in a new button.
        load_more = page.locator("#page-info").get_attribute("data-load-more")
        first = page.locator("ul.list-style-none").filter(
            has=page.locator("li.news-item")).first.inner_html()
        chunks = [first]
        ts_raw = re.findall(r'data-last-timestamp="([^"]+)"', first)
        pages = 1
        while ts_raw and pages < MAX_PAGES:
            ts = datetime.strptime(ts_raw[-1][:19], "%Y-%m-%d-%H-%M-%S")
            if ts < since:
                break
            # Without X-Requested-With the server ignores timestamp and
            # returns the first page again.
            resp = context.request.get(
                f"https://www.screener.in{load_more}?timestamp={ts_raw[-1]}",
                headers={"X-Requested-With": "XMLHttpRequest",
                         "Referer": "https://www.screener.in/"})
            if not resp.ok:
                print(f"  page {pages + 1}: HTTP {resp.status}; stopping", flush=True)
                break
            frag = resp.text()
            chunks.append(frag)
            ts_raw = re.findall(r'data-last-timestamp="([^"]+)"', frag)
            pages += 1
            print(f"  page {pages}: oldest={ts_raw[-1][:16] if ts_raw else 'end of feed'}",
                  flush=True)
            time.sleep(1)

        items = extract_items("".join(chunks))
        today = started.date()
        seen = set()
        for it in items:
            d = parse_day(it["day"], today)
            if d is None or d < since.date() or not it["href"] or it["href"] in seen:
                continue
            seen.add(it["href"])
            it["date"] = d
            rows.append(it)
        print(f"Feed items loaded: {len(items)}  in window: {len(rows)}", flush=True)

        ok = failed = nopdf = partial = 0
        for n, it in enumerate(rows, 1):
            h = hashlib.md5(it["href"].encode()).hexdigest()[:6]
            fname = f"{safe_filename(it['company'])}_{safe_filename(it['title'])[:40]}_{h}.pdf"
            try:
                time.sleep(REQUEST_DELAY)
                body, why = fetch_pdf(context, it["href"])
                if b"<html" in body[:2000].lower():
                    # Insider trades and rating updates link to a BSE web
                    # page, not a filing. The title already holds the detail.
                    it["file"] = "no PDF (detail in Type)"
                    nopdf += 1
                    continue
                if not body.startswith(b"%PDF"):
                    fname = fname[:-4] + ".bin"
                with open(os.path.join(out_dir, fname), "wb") as f:
                    f.write(body)
                it["file"] = fname
                ok += 1
                if why:
                    # Keep the part we have; flag it where the reader sees it.
                    partial += 1
                    it["summary"] = f"PARTIAL FILE ({why}). {it['summary']}"
                    print(f"  [{n}/{len(rows)}] PART {it['company'][:25]} | {why}",
                          flush=True)
                else:
                    print(f"  [{n}/{len(rows)}] OK   {it['company'][:25]} | {it['title'][:50]}",
                          flush=True)
            except Exception as e:
                it["file"] = f"FAILED ({str(e)[:80]})"
                failed += 1
                print(f"  [{n}/{len(rows)}] FAIL {it['company'][:25]} | {str(e)[:80]}",
                      flush=True)
        browser.close()

    companies = len({r["company"] for r in rows})
    lines = [
        f"# Watchlist announcements: {since:%d %b %Y %H:%M} to {started:%d %b %Y %H:%M}",
        "",
        f"**Announcements: {len(rows)}**  |  downloaded {ok}  |  partial {partial}  |  "
        f"no PDF {nopdf}  |  failed {failed}  |  "
        f"companies {companies}",
        "",
    ]
    lines += key_documents(rows, out_dir)
    lines += [
        "## All announcements",
        "",
        "| # | Day | Company | Type | Summary | File |",
        "|---|---|---|---|---|---|",
    ]
    for n, r in enumerate(sorted(rows, key=lambda r: (r["company"], r["date"])), 1):
        cells = [str(n), r["date"].strftime("%d %b"), r["company"], r["title"],
                 r["summary"], r["file"]]
        lines.append("| " + " | ".join(c.replace("|", "/").replace("\n", " ")
                                       for c in cells) + " |")
    with open(os.path.join(out_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    # Company -> screener page link, as the feed gives it (consolidated or
    # standalone). refresh_prices.py reads prices from these pages.
    with open(os.path.join(out_dir, "companies.json"), "w", encoding="utf-8") as f:
        json.dump({r["company"]: r.get("company_url", "") for r in rows}, f,
                  indent=1, ensure_ascii=False)
    # Source link per saved file, so a bad download can be fetched again.
    with open(os.path.join(out_dir, "urls.json"), "w", encoding="utf-8") as f:
        json.dump({r["file"]: r["href"] for r in rows if r["file"].endswith((".pdf", ".bin"))},
                  f, indent=1, ensure_ascii=False)

    if failed == 0 or ok > 0:
        with open(STATE_FILE, "w") as f:
            f.write(started.strftime("%Y-%m-%d %H:%M"))

    print(f"SUMMARY: since={since:%Y-%m-%d %H:%M} items={len(rows)} downloaded={ok} "
          f"failed={failed} partial={partial} companies={companies} -> {out_dir}", flush=True)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
