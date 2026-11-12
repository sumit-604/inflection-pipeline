#!/usr/bin/env python3
"""Fetch raw files for the liquidity vs small-cap study. RUN ON THE LAPTOP.

The cloud shell cannot reach RBI, FBIL, NSE, niftyindices.com or
indiamtf.com (policy 403 on every host, 2026-11-05). Run this on the
operator's laptop, then push data/raw/ to the repo.

Two series download automatically:
  mtf      indiamtf.com /history/snapshots.json (NSE, BSE, combined book)
  indices  niftyindices.com historical close API (Smallcap 250,
           Microcap 250, Nifty 50), in 360-day windows

Two series need a browser download, because both sites serve their history
through a JavaScript app with no documented file URL:
  laf      RBI DBIE, net LAF daily (Rs crore)
  cd3m     FBIL CD curve, 3-month tenor

For a browser download, save the file in data/raw/ and record where it came
from:
  python fetch_laptop.py register data/raw/<file> --series laf --url "<page URL>"

Every raw file gets a line in data/raw/manifest.json: series, source URL,
download date. build_data.py refuses a raw file with no manifest line.

Usage:
  python fetch_laptop.py mtf
  python fetch_laptop.py indices [--start 2023-01-01] [--end YYYY-MM-DD]
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


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("mtf")
    pi = sub.add_parser("indices")
    pi.add_argument("--start", default="2023-01-01")
    pi.add_argument("--end", default=_today())
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
    else:
        p = Path(a.file).resolve()
        if p.parent != RAW:
            sys.exit(f"put the file in {RAW} first")
        record(p, a.series, a.url, a.note)


if __name__ == "__main__":
    main()
