#!/usr/bin/env python3
"""Fetch raw files for the liquidity vs small-cap study.

Runs in a cloud session whose environment allows the source hosts
(the "inflection-pipeline" environment, 2026-11-16), or on the laptop.

  mtf          indiamtf.com /history/snapshots.json (NSE, BSE, combined book)
  indices-nse  NSE ind_close_all daily files (Nifty 50, Smallcap 250, Microcap 250)
  cd3m         FBIL CD curve public endpoint, all tenors
  laf-mmo      RBI Money Market Operations releases, net liquidity row
  indices      niftyindices.com history API (needs liveindexsa.niftyindices.com;
               superseded by indices-nse)
  register     record a file saved by hand (for example a DBIE export)

Every raw file gets a line in data/raw/manifest.json: series, source URL,
download date. build_data.py refuses a raw file with no manifest line.

Usage:
  python fetch_laptop.py {mtf|indices-nse|cd3m|laf-mmo} [--start 2023-01-01] [--end YYYY-MM-DD]
  python fetch_laptop.py register FILE --series {laf,cd3m,mtf,indices} --url URL
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "data" / "raw"
MANIFEST = RAW / "manifest.json"
UA = "Mozilla/5.0 (inflection-pipeline liquidity-smallcap research fetch)"

MTF_URL = "https://indiamtf.com/history/snapshots.json"
NI_HOME = "https://www.niftyindices.com/reports/historical-data"
NI_API = "https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString"
INDICES = {
    "nifty_smallcap_250": "NIFTY SMALLCAP 250",
    "nifty_microcap_250": "NIFTY MICROCAP 250",
    "nifty_50": "NIFTY 50",
}


def _today() -> str:
    return dt.date.today().isoformat()


def _load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {}


def record(path: Path, series: str, url: str, note: str = "") -> None:
    m = _load_manifest()
    m[path.name] = {"series": series, "source_url": url,
                    "downloaded_on": _today(), "note": note}
    RAW.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(m, indent=2, sort_keys=True) + "\n")
    print(f"manifest: {path.name} -> {series} | {url} | {_today()}")


def fetch_mtf() -> None:
    import requests
    r = requests.get(MTF_URL, headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    payload = r.json()
    if not {"nse", "combined"} <= set(payload):
        sys.exit(f"unexpected snapshots.json keys: {sorted(payload)}")
    out = RAW / f"indiamtf_snapshots_{_today()}.json"
    out.write_text(json.dumps(payload))
    record(out, "mtf", MTF_URL, "whole-book daily net, INR crore; "
           "BSE disclosures start about 2025-10-15 (indiamtf openapi.json)")


def _windows(start: dt.date, end: dt.date, days: int = 360):
    a = start
    while a <= end:
        b = min(a + dt.timedelta(days=days), end)
        yield a, b
        a = b + dt.timedelta(days=1)


def fetch_indices(start: str, end: str) -> None:
    import requests
    s = requests.Session()
    s.headers.update({"User-Agent": UA,
                      "Content-Type": "application/json; charset=UTF-8",
                      "Origin": "https://www.niftyindices.com",
                      "Referer": NI_HOME,
                      "X-Requested-With": "XMLHttpRequest"})
    s.get(NI_HOME, timeout=60)            # session cookie
    d0, d1 = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    for key, name in INDICES.items():
        rows = []
        for a, b in _windows(d0, d1):
            cinfo = ("{'name':'%s','startDate':'%s','endDate':'%s',"
                     "'indexName':'%s'}" % (name, a.strftime("%d-%b-%Y"),
                                            b.strftime("%d-%b-%Y"), name))
            r = s.post(NI_API, json={"cinfo": cinfo}, timeout=60)
            r.raise_for_status()
            chunk = json.loads(r.json()["d"])
            print(f"{name} {a}..{b}: {len(chunk)} rows")
            rows.extend(chunk)
            time.sleep(1.0)
        out = RAW / f"niftyindices_{key}_{_today()}.json"
        out.write_text(json.dumps(rows))
        record(out, "indices", NI_API + f" (cinfo name='{name}')",
               f"{name} daily close, {start} to {end}")


# ------------------------------------------------------------ added 2026-11-16
NSE_IDX = "https://nsearchives.nseindia.com/content/indices/ind_close_all_{d:%d%m%Y}.csv"
NSE_NAMES = {"Nifty 50": "nifty_50", "Nifty Smallcap 250": "nifty_smallcap_250",
             "Nifty Microcap 250": "nifty_microcap_250"}
NSE_UA = "Mozilla/5.0"   # nsearchives drops connections with a longer custom UA
FBIL_CD = "https://www.fbil.org.in/wasdm/cd/fetchfiltered"
RBI_PR = "https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx"
MMO_ROW = r"Net liquidity injected \(outstanding including today'?s\s*\|?\s*operations\)"


def fetch_indices_nse(start: str, end: str) -> None:
    """NSE daily all-index close files (NSE Indices, publisher of niftyindices.com).
    A 404 is a non-trading day; it is logged, never filled."""
    import csv
    import io
    import requests
    s = requests.Session()
    s.headers["User-Agent"] = NSE_UA
    rows, missing = [], []
    d, d1 = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    while d <= d1:
        if d.weekday() < 5:
            url = NSE_IDX.format(d=d)
            r = None
            for attempt in range(4):              # NSE drops idle/bursty connections
                try:
                    r = s.get(url, timeout=60)
                    break
                except requests.exceptions.ConnectionError:
                    time.sleep(2 ** (attempt + 1))
                    s = requests.Session()
                    s.headers["User-Agent"] = NSE_UA
            if r is None:
                missing.append(f"{d.isoformat()} connection failed after 4 tries")
                d += dt.timedelta(days=1)
                continue
            if r.status_code == 200:
                for rec in csv.DictReader(io.StringIO(r.text)):
                    if rec.get("Index Name", "").strip() in NSE_NAMES:
                        rows.append({"file_date": d.isoformat(),
                                     "index_name": rec["Index Name"].strip(),
                                     "index_date": rec["Index Date"],
                                     "close": rec["Closing Index Value"],
                                     "source_url": url})
            else:
                missing.append(f"{d.isoformat()} HTTP {r.status_code}")
            time.sleep(0.3)
        d += dt.timedelta(days=1)
    out = RAW / f"nse_ind_close_all_{_today()}.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (RAW / f"nse_ind_close_all_{_today()}_missing.txt").write_text("\n".join(missing) + "\n")
    print(f"{len(rows)} index rows; {len(missing)} weekdays with no file")
    record(out, "indices", NSE_IDX.replace("{d:%d%m%Y}", "DDMMYYYY"),
           "NSE ind_close_all daily files; weekday 404s listed in *_missing.txt")


def fetch_cd(start: str, end: str) -> None:
    """FBIL CD curve, public endpoint the fbil.org.in app calls (authenticated=false)."""
    import requests
    s = requests.Session()
    s.headers["User-Agent"] = UA
    allrows = []
    for a, b in _windows(dt.date.fromisoformat(start), dt.date.fromisoformat(end), 30):
        r = s.get(FBIL_CD, params={"fromDate": a.isoformat(), "toDate": b.isoformat(),
                                   "authenticated": "false"}, timeout=60)
        r.raise_for_status()
        chunk = r.json()
        print(f"CD {a}..{b}: {len(chunk)} rows")
        allrows.extend(chunk)
        time.sleep(0.5)
    out = RAW / f"fbil_cd_curve_{_today()}.json"
    out.write_text(json.dumps(allrows))
    record(out, "cd3m", FBIL_CD + "?fromDate=YYYY-MM-DD&toDate=YYYY-MM-DD&authenticated=false",
           "FBIL CD curve, all tenors; build keeps 3 Months")


def fetch_laf_mmo(start: str, end: str) -> None:
    """RBI daily Money Market Operations press releases, row F:
    net liquidity injected (outstanding including today's operations),
    injection (+) / absorption (-), Rs crore. RBI: Repo+MSF+SLF-Reverse Repo-SDF."""
    import csv
    import html
    import re
    import requests
    s = requests.Session()
    s.headers["User-Agent"] = UA
    d0, d1 = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    links = {}
    y, m = d0.year, d0.month
    while (y, m) <= (d1.year, d1.month):
        page = s.get(RBI_PR, timeout=60).text
        form = dict(re.findall(r'name="(__[A-Z]+)"[^>]*value="([^"]*)"', page))
        form.update({"hdnYear": str(y), "hdnMonth": str(m)})
        lst = s.post(RBI_PR, data=form, timeout=60).text
        for prid, title in re.findall(
                r"BS_PressReleaseDisplay\.aspx\?prid=(\d+)[^>]*>([^<]*Money Market Operations[^<]*)", lst):
            links[prid] = html.unescape(title).strip()
        print(f"{y}-{m:02d}: {len(links)} MMO links so far")
        m += 1
        if m == 13:
            y, m = y + 1, 1
        time.sleep(0.5)
    rows = []
    for prid, title in sorted(links.items(), key=lambda kv: int(kv[0])):
        mt = re.search(r"as on (\w+ \d{1,2}, \d{4})", title)
        url = f"{RBI_PR}?prid={prid}"
        val, note = "", ""
        try:
            t = s.get(url, timeout=60).text
            txt = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " | ", t)))
            txt = re.sub(r"(\s*\|\s*)+", " | ", txt)
            hit = re.search(MMO_ROW + r".{0,80}?\| (-?[\d,]+\.\d+) \|", txt)
            if hit:
                val = hit.group(1).replace(",", "")
            else:
                note = "row F not found"
        except Exception as e:                                  # noqa: BLE001
            note = f"fetch error {type(e).__name__}"
        as_on = (dt.datetime.strptime(mt.group(1), "%B %d, %Y").date().isoformat()
                 if mt else "")
        rows.append({"date": as_on, "net_liquidity_injected_cr": val,
                     "release_title": title, "release_url": url, "note": note})
        time.sleep(0.4)
    out = RAW / f"rbi_mmo_net_liquidity_{_today()}.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} MMO releases; {sum(1 for r in rows if not r['net_liquidity_injected_cr'])} without a value")
    record(out, "laf", RBI_PR + " (Money Market Operations releases; per-row URL in release_url)",
           "Row F, net liquidity injected incl. today's operations, injection +")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("mtf")
    pi = sub.add_parser("indices")
    pi.add_argument("--start", default="2023-01-01")
    pi.add_argument("--end", default=_today())
    for name in ("indices-nse", "cd3m", "laf-mmo"):
        q = sub.add_parser(name)
        q.add_argument("--start", default="2023-01-01")
        q.add_argument("--end", default=_today())
    pr = sub.add_parser("register")
    pr.add_argument("file")
    pr.add_argument("--series", required=True,
                    choices=["laf", "cd3m", "mtf", "indices"])
    pr.add_argument("--url", required=True)
    pr.add_argument("--note", default="")
    a = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    if a.cmd == "mtf":
        fetch_mtf()
    elif a.cmd == "indices":
        fetch_indices(a.start, a.end)
    elif a.cmd == "indices-nse":
        fetch_indices_nse(a.start, a.end)
    elif a.cmd == "cd3m":
        fetch_cd(a.start, a.end)
    elif a.cmd == "laf-mmo":
        fetch_laf_mmo(a.start, a.end)
    else:
        p = Path(a.file).resolve()
        if p.parent != RAW:
            sys.exit(f"put the file in {RAW} first")
        record(p, a.series, a.url, a.note)


if __name__ == "__main__":
    main()
