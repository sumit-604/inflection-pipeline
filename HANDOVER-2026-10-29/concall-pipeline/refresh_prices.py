"""
refresh_prices.py — current price, 52-week high / low and market cap for every
company in a run, read from its screener.in company page.

Replaces the Trendlyne price call in the daily filing review. Same read as
collect_to_repo.py (plain GET of the screener page, regex on the top ratios,
consolidated -> standalone fallback when the consolidated page has no price).

Order per company:
  1. screener.in company page (URL from the run's companies.json, else
     review_spec/screener_map.json, else screener's search API)
  2. NSE quote API (backup)
  3. BSE quote API (backup for BSE-only names, and when NSE refuses)
  4. none worked: "PRICE NOT REFRESHED" with the reason for each source

Every reading carries the time it was read (IST) and its source. Readings are
appended to review_spec/price_history.json so the next run can tell whether a
price crossed a stop, trim or exit line in between.

Outputs:
  <run>/deep/prices.json   one record per company
  <run>/deep/prices.md     the same as a table
  review_spec/screener_map.json   name -> screener URL / NSE symbol / BSE code
  review_spec/price_history.json  every reading, keyed by company name

Usage:
  python refresh_prices.py "<run folder>"
  python refresh_prices.py --names "Paushak,Gargi,Pace Digitek,Tata Power" [test folder]
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(ROOT, "review_spec")
MAP_FILE = os.path.join(SPEC, "screener_map.json")
HISTORY_FILE = os.path.join(SPEC, "price_history.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
DELAY = 1.5          # seconds between screener requests
NOT_REFRESHED = "PRICE NOT REFRESHED"


def now_ist():
    # Always IST, even when the machine's timezone is changed (travel, 28-Oct-2026).
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")


def num(s):
    return float(s.replace(",", "")) if s else None


def load(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        return default


def save(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


# ---------------- screener ----------------
def screener_search(name):
    """First company hit from screener's search box, or None."""
    r = requests.get("https://www.screener.in/api/company/search/",
                     params={"q": name, "v": 3, "fts": 1},
                     headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    for hit in r.json():
        if hit.get("id") and "/company/" in hit.get("url", ""):
            return "https://www.screener.in" + hit["url"], hit.get("name", "")
    return None, ""


def screener_page(url):
    """Price facts from one screener page. Raises on HTTP failure."""
    for attempt in (1, 2):
        r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
        if r.status_code == 429 and attempt == 1:
            time.sleep(10)
            continue
        r.raise_for_status()
        break
    html = r.text
    m = re.search(r'<ul id="top-ratios">(.*?)</ul>', html, re.S)
    flat = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1) if m else html))
    g = lambda pat: (re.search(pat, flat) or [None, None])[1]
    hl = re.search(r"High / Low\s*₹?\s*([\d,]+(?:\.\d+)?)\s*/\s*([\d,]+(?:\.\d+)?)", flat)
    h1 = re.search(r"<title>\s*(.*?) share price", html, re.S)
    nse = re.search(r"nseindia\.com/get-quotes/equity\?symbol=([A-Za-z0-9&%._-]+)", html)
    bse = re.search(r"bseindia\.com/stock-share-price/[^\"'\s]*?/(\d{6})/?", html)
    return {
        "price": num(g(r"Current Price\s*₹?\s*([\d,]+(?:\.\d+)?)")),
        "high_52w": num(hl.group(1)) if hl else None,
        "low_52w": num(hl.group(2)) if hl else None,
        "mcap_cr": num(g(r"Market Cap\s*₹?\s*([\d,]+(?:\.\d+)?)\s*Cr")),
        "page_name": re.sub(r"\s+", " ", h1.group(1)).strip() if h1 else "",
        "nse_symbol": requests.utils.unquote(nse.group(1)) if nse else "",
        "bse_code": bse.group(1) if bse else "",
    }


def from_screener(url):
    """Screener read with the consolidated -> standalone fallback."""
    facts, note = screener_page(url), ""
    if not facts["price"] and "/consolidated/" in url:
        alt = url.replace("/consolidated/", "/")
        time.sleep(DELAY)
        alt_facts = screener_page(alt)
        if alt_facts["price"]:
            facts, url = alt_facts, alt
            note = "consolidated page had no price; standalone page used"
    return facts, url, note


# ---------------- backups ----------------
def from_nse(symbol):
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
                      "Accept": "application/json,text/html,*/*"})
    page = f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}"
    s.get(page, timeout=20)
    r = s.get("https://www.nseindia.com/api/quote-equity", params={"symbol": symbol},
              headers={"Referer": page}, timeout=20)
    r.raise_for_status()
    d = r.json()
    p = d.get("priceInfo") or {}
    wk = p.get("weekHighLow") or {}
    if not p.get("lastPrice"):
        raise ValueError("no lastPrice in NSE reply")
    return {"price": float(p["lastPrice"]), "high_52w": wk.get("max"),
            "low_52w": wk.get("min"), "mcap_cr": None,
            "exchange_time": (d.get("metadata") or {}).get("lastUpdateTime", "")}


BSE_API = "https://api.bseindia.com/BseIndiaAPI/api/"
# BSE's API refuses a full browser user-agent string (403) and answers a plain one.
BSE_HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.bseindia.com/"}


def from_bse(code):
    r = requests.get(BSE_API + "getScripHeaderData/w", headers=BSE_HEADERS, timeout=20,
                     params={"Debtflag": "", "scripcode": code, "seriesid": ""})
    r.raise_for_status()
    d = r.json()
    ltp = (d.get("CurrRate") or {}).get("LTP")
    if not ltp:
        raise ValueError("no LTP in BSE reply")
    out = {"price": float(ltp), "high_52w": None, "low_52w": None, "mcap_cr": None,
           "exchange_time": (d.get("Header") or {}).get("Ason", "")}
    try:  # 52-week band and market cap come from two more BSE calls
        hl = requests.get(BSE_API + "HighLow/w", headers=BSE_HEADERS, timeout=20,
                          params={"Type": "EQ", "flag": "C", "scripcode": code}).json()
        out["high_52w"] = num(hl.get("Fifty2WkHigh_adj") or "")
        out["low_52w"] = num(hl.get("Fifty2WkLow_adj") or "")
        st = requests.get(BSE_API + "StockTrading/w", headers=BSE_HEADERS, timeout=20,
                          params={"flag": "", "quotetype": "EQ", "scripcode": code}).json()
        out["mcap_cr"] = num(st.get("MktCapFull") or "")
    except Exception:
        pass
    return out


# ---------------- one company ----------------
def refresh_one(name, url_hint, smap):
    rec = {"company": name, "page_name": "", "price": None, "high_52w": None, "low_52w": None,
           "mcap_cr": None, "read_at": None, "source": None, "url": "",
           "status": NOT_REFRESHED, "notes": [], "errors": []}
    known = smap.get(name, {})
    url = url_hint or known.get("url", "")
    if not url:
        try:
            url, hit = screener_search(name)
            if url:
                rec["notes"].append(f"screener URL found by search: '{hit}'")
            time.sleep(DELAY)
        except Exception as e:
            rec["errors"].append(f"screener search: {str(e)[:80]}")
    nse_sym, bse_code = known.get("nse_symbol", ""), known.get("bse_code", "")
    if url:
        rec["url"] = url
        try:
            facts, url, note = from_screener(url)
            nse_sym = facts["nse_symbol"] or nse_sym
            bse_code = facts["bse_code"] or bse_code
            smap[name] = {"url": url, "page_name": facts["page_name"],
                          "nse_symbol": nse_sym, "bse_code": bse_code}
            if note:
                rec["notes"].append(note)
            rec["page_name"] = facts["page_name"]
            if facts["price"]:
                rec.update({k: facts[k] for k in ("price", "high_52w", "low_52w", "mcap_cr")})
                rec.update(read_at=now_ist(), source="screener.in", url=url, status="OK")
                return rec
            rec["errors"].append("screener: page had no Current Price")
        except Exception as e:
            rec["errors"].append(f"screener: {str(e)[:80]}")
    else:
        rec["errors"].append("screener: no URL on file and search found none")

    # The screener slug is the NSE symbol (letters) or the BSE code (digits).
    slug = (re.search(r"/company/([^/]+)/", url or "") or [None, ""])[1]
    nse_sym = nse_sym or ("" if slug.isdigit() else slug)
    bse_code = bse_code or (slug if slug.isdigit() else "")
    for label, key, fn in (("NSE", nse_sym, from_nse), ("BSE", bse_code, from_bse)):
        if not key:
            rec["errors"].append(f"{label}: no {'symbol' if label == 'NSE' else 'scrip code'} known")
            continue
        try:
            got = fn(key)
            ex_time = got.pop("exchange_time", "")
            rec.update(got)
            rec.update(read_at=now_ist(), source=f"{label} quote ({key})", status="OK")
            if ex_time:
                rec["notes"].append(f"{label} quote time: {ex_time}")
            rec["notes"].append("screener failed; backup used")
            return rec
        except Exception as e:
            rec["errors"].append(f"{label}: {str(e)[:80]}")
    rec["read_at"] = now_ist()   # time of the failed attempt
    return rec


def run_companies(run):
    index = open(os.path.join(run, "INDEX.md"), encoding="utf-8").read()
    names = []
    for m in re.finditer(r"(?m)^\| \d+ \| [^|]+ \| ([^|]+?) \|", index):
        if m.group(1) not in names:
            names.append(m.group(1))
    urls = load(os.path.join(run, "companies.json"), {})
    return names, urls


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("run", nargs="?")
    ap.add_argument("--names", help="comma-separated company names (test mode: never "
                    "written to price_history; with a run folder, writes its prices files)")
    a = ap.parse_args()
    test = bool(a.names)
    if a.names:
        names, urls = [n.strip() for n in a.names.split(",") if n.strip()], {}
        run = os.path.abspath(a.run) if a.run else None
    elif a.run:
        run = os.path.abspath(a.run)
        names, urls = run_companies(run)
    else:
        sys.exit("give a run folder or --names")

    smap, hist = load(MAP_FILE, {}), load(HISTORY_FILE, {})
    out = []
    for i, name in enumerate(names, 1):
        rec = refresh_one(name, urls.get(name, ""), smap)
        out.append(rec)
        # Test runs stay out of the history: it is the "last run" baseline.
        if rec["status"] == "OK" and run and not test:
            hist.setdefault(name, []).append(
                {"price": rec["price"], "read_at": rec["read_at"], "source": rec["source"],
                 "run": os.path.basename(run)})
        shown = f"{rec['price']:,.2f}" if rec["price"] else NOT_REFRESHED
        print(f"  [{i}/{len(names)}] {name[:28]:28} {shown:>12}  {rec['source'] or ''}  "
              f"{rec['read_at']}  {'; '.join(rec['errors']) if rec['status'] != 'OK' else ''}",
              flush=True)
        time.sleep(DELAY)
    save(MAP_FILE, smap)
    save(HISTORY_FILE, hist)

    if run:
        deep = os.path.join(run, "deep")
        os.makedirs(deep, exist_ok=True)
        save(os.path.join(deep, "prices.json"), out)
        f = lambda v: "" if v is None else f"{v:,.2f}"
        rows = ["| Company | Price (₹) | 52w high | 52w low | Mcap (₹ Cr) | Read at | Source | Notes |",
                "|---|---|---|---|---|---|---|---|"]
        for r in out:
            price = f(r["price"]) if r["status"] == "OK" else f"**{NOT_REFRESHED}**"
            note = "; ".join(r["notes"] + (r["errors"] if r["status"] != "OK" else []))
            rows.append(f"| {r['company']} | {price} | {f(r['high_52w'])} | {f(r['low_52w'])} | "
                        f"{f(r['mcap_cr'])} | {r['read_at']} | {r['source'] or ''} | {note} |")
        open(os.path.join(deep, "prices.md"), "w", encoding="utf-8").write(
            "# Prices for this run\n\n" + "\n".join(rows) + "\n")
    ok = sum(r["status"] == "OK" for r in out)
    print(f"PRICES: companies={len(out)} refreshed={ok} not_refreshed={len(out) - ok} "
          f"screener={sum(r['source'] == 'screener.in' for r in out)}")


if __name__ == "__main__":
    main()
