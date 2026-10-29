#!/usr/bin/env python3
"""Download a company's credit-rating documents from its screener.in page.

screener.in lists each company's rating updates under "Documents > Credit
ratings", and those links are visible without a login. The links point at the
agencies: CRISIL and Acuite serve PDFs, ICRA and India Ratings serve web pages.
PDFs are saved as-is; pages are saved as HTML and also as extracted text.

The main collector (screener_collect.py) fetches annual reports, concalls and
presentations. It never fetched ratings. This fills that gap.

Usage:
    python fetch_ratings.py <screener company URL> --output-dir <folder>
    python fetch_ratings.py https://www.screener.in/company/526433/ --output-dir ../../screens/corpus/ASMTEC/credit-ratings
"""

from __future__ import annotations

import argparse
import html as htmlmod
import json
import re
import sys
import time
from pathlib import Path

import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")


def agency_of(url):
    u = url.lower()
    for key, name in (("crisil", "CRISIL"), ("icra", "ICRA"), ("indiaratings", "IndiaRatings"),
                      ("acuite", "Acuite"), ("careratings", "CARE"), ("brickwork", "Brickwork"),
                      ("infomerics", "Infomerics"), ("bseindia", "BSE-announcement")):
        if key in u:
            return name
    return "other"


def rating_links(page_html):
    """Links from two places on the screener page.

    1. The Documents > Credit ratings block, which screener marks with
       class="documents credit-ratings". Agency rationale links live here.
    2. Exchange announcements whose title carries "Credit Rating". These are
       the company's own filing of the rating letter, served as a PDF by the
       BSE, and they exist even when the agency page is a script shell.
    """
    out = []
    m = re.search(r'(?is)class="documents credit-ratings[^"]*".*?<ul[^>]*>(.*?)</ul>', page_html)
    block = m.group(1) if m else ""
    for href, text in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.S):
        text = re.sub(r"<[^>]+>", " ", text)
        text = htmlmod.unescape(re.sub(r"\s+", " ", text)).strip()
        if href.startswith("http"):
            out.append((href, text))
    for href, text in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', page_html, re.S):
        plain = htmlmod.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))).strip()
        if re.search(r"(?i)credit\s+rating", plain) and href.startswith("http") \
                and "AnnPdfOpen" in href:
            out.append((href, plain))
    # De-duplicate, keep order.
    seen, uniq = set(), []
    for h, t in out:
        if h not in seen:
            seen.add(h)
            uniq.append((h, t))
    return uniq


def html_to_text(doc):
    doc = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", doc)
    doc = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</li>|</h\d>", "\n", doc)
    doc = re.sub(r"<[^>]+>", " ", doc)
    doc = htmlmod.unescape(doc)
    doc = re.sub(r"[ \t]+", " ", doc)
    doc = re.sub(r"\n\s*\n+", "\n\n", doc)
    return doc.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--max", type=int, default=8, help="most recent N links to fetch")
    a = ap.parse_args()

    out = Path(a.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "en-IN,en;q=0.9"})

    r = s.get(a.url, timeout=60)
    r.raise_for_status()
    links = rating_links(r.text)
    if not links:
        print("no credit-rating links found on", a.url)
        return 1
    print(f"{len(links)} rating links on page; fetching up to {a.max}")

    manifest = []
    for i, (href, text) in enumerate(links[: a.max], 1):
        agency = agency_of(href)
        base = f"{i:02d}-{agency}"
        try:
            rr = s.get(href, timeout=90, allow_redirects=True)
            ctype = rr.headers.get("content-type", "").lower()
            is_pdf = "pdf" in ctype or rr.content[:5] == b"%PDF-"
            if is_pdf:
                path = out / (base + ".pdf")
                path.write_bytes(rr.content)
                kind = "pdf"
            else:
                text_body = html_to_text(rr.text)
                # A page that is only a loading shell (India Ratings, Acuite
                # connect) has no rationale in it. Say so instead of saving junk.
                if len(text_body) < 400:
                    print(f"  [{i}] {agency:15s} SHELL    page needs a browser to render; skipped")
                    manifest.append({"index": i, "agency": agency, "url": href, "link_text": text,
                                     "kind": "shell", "status": rr.status_code})
                    time.sleep(1.0)
                    continue
                path = out / (base + ".html")
                path.write_text(rr.text, encoding="utf-8", errors="ignore")
                (out / (base + ".txt")).write_text(text_body, encoding="utf-8")
                kind = "html+txt"
            print(f"  [{i}] {agency:15s} {kind:8s} {len(rr.content):>9,d} B  {text[:40]!r}")
            manifest.append({"index": i, "agency": agency, "kind": kind, "link_text": text,
                             "url": href, "file": path.name, "status": rr.status_code,
                             "bytes": len(rr.content)})
        except Exception as exc:  # noqa: BLE001
            print(f"  [{i}] {agency:15s} FAILED {str(exc)[:80]}")
            manifest.append({"index": i, "agency": agency, "url": href, "link_text": text,
                             "error": str(exc)[:200]})
        time.sleep(1.5)

    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("manifest ->", out / "manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
