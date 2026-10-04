#!/usr/bin/env python3
"""Data loaders for the macro direction model.

Run:  python fetch.py            # try every primary source once, then the mirror
      python fetch.py --primary  # primary sources only (operator laptop)

Every series lands in data/<name>.csv at monthly frequency, and data/sources.md
records the URL actually used, the series code, the first and last month, the
fetch date, and whether the primary source or a public mirror served it.
Nothing is typed by hand. A series that no source serves is listed as FAILED
and the model runs without it (its vote is 0).

Each source is tried once. No retries: a refused host is a policy refusal,
not a transient fault.
"""
from __future__ import annotations

import datetime as dt
import io
import json
import sys
from pathlib import Path

import pandas as pd
import requests

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
RAW = DATA / "raw"          # manual drops (FPI flows) live here
TIMEOUT = 60
UA = {"User-Agent": "Mozilla/5.0 (macro-direction fetch.py)"}
TODAY = dt.date.today().isoformat()

FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={code}"
PINK_PRIMARY = ("https://thedocs.worldbank.org/en/doc/"
                "74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/"
                "CMO-Historical-Data-Monthly.xlsx")
YAHOO = ("https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
         "?period1=0&period2={now}&interval=1d&includeAdjustedClose=true")
NSDL_FPI = "https://www.fpi.nsdl.co.in/web/Reports/Yearwise.aspx?RptType=6"

# Public GitHub mirrors, used only when the primary host refuses. Each mirror
# names the upstream it copies; sources.md carries both URLs.
RAW_GH = "https://raw.githubusercontent.com/{repo}/{ref}/{path}"
MIRRORS: dict[str, dict] = {
    "pinksheet": dict(repo="datasets/gold-prices", ref="main",
                      path="cache/monthly.xls",
                      note="datahub mirror; byte copy of the World Bank "
                           "CMO-Historical-Data-Monthly.xlsx, sheet "
                           "'Monthly Prices' read as published"),
    "DEXINUS": dict(repo="datasets/exchange-rates", ref="main",
                    path="data/daily.csv", filter_col="Country",
                    filter_val="India", date_col="Date",
                    value_col="Exchange rate",
                    note="datahub mirror of FRED H.10 daily rates "
                         "(DEXINUS for India)"),
    "BRENT_EIA": dict(repo="datasets/oil-prices", ref="main",
                      path="data/brent-daily.csv", date_col="Date",
                      value_col="Price",
                      note="datahub mirror of EIA RBRTE (Europe Brent spot "
                           "FOB, daily)"),
}

# Pink Sheet columns we keep: header text in row 5 of 'Monthly Prices'.
PINK_COLS = {
    "brent": "Crude oil, Brent",
    "aluminium": "Aluminum",
    "copper": "Copper",
    "zinc": "Zinc",
    "gold": "Gold",
    "silver": "Silver",
}
FRED_SERIES = ["DFII10", "DTWEXBGS", "T10YIE", "FEDFUNDS", "DEXINUS"]
YAHOO_SYMS = {"GC=F": "yahoo_gold_fut", "SI=F": "yahoo_silver_fut",
              "BZ=F": "yahoo_brent_fut", "^NSEI": "yahoo_nifty"}

LOG: list[dict] = []


def _get(url: str) -> bytes:
    r = requests.get(url, headers=UA, timeout=TIMEOUT)
    r.raise_for_status()
    return r.content


def _record(name, code, url, status, df=None, note=""):
    first = last = rows = ""
    if df is not None and len(df):
        first, last, rows = df.index.min(), df.index.max(), len(df)
    LOG.append(dict(name=name, code=code, url=url, status=status,
                    first=str(first), last=str(last), rows=rows,
                    fetched=TODAY, note=note))


def _monthly_from_daily(s: pd.Series) -> pd.DataFrame:
    """Daily series -> month-end (last valid obs) and monthly mean."""
    s = pd.to_numeric(s, errors="coerce").dropna().sort_index()
    m = s.index.to_period("M")
    out = pd.DataFrame({"month_end": s.groupby(m).last(),
                        "month_avg": s.groupby(m).mean(),
                        "last_obs_date": pd.Series(s.index, index=s.index)
                        .groupby(m).last().dt.date.astype(str)})
    out.index = out.index.astype(str)
    out.index.name = "month"
    return out


def _save(df: pd.DataFrame, name: str):
    df.to_csv(DATA / f"{name}.csv")


# ---------------------------------------------------------------- Pink Sheet
def _parse_pink(content: bytes) -> pd.DataFrame:
    raw = pd.read_excel(io.BytesIO(content), sheet_name="Monthly Prices",
                        header=None)
    hdr = [str(h) for h in raw.iloc[4].tolist()]
    body = raw.iloc[6:].copy()
    body = body[body[0].map(str).str.match(r"^\d{4}M\d{2}$")]
    out = pd.DataFrame(index=[f"{p[:4]}-{p[5:]}" for p in body[0]])
    for key, label in PINK_COLS.items():
        idx = [i for i, h in enumerate(hdr) if h.startswith(label)]
        if len(idx) != 1:
            raise ValueError(f"Pink Sheet column '{label}' matched {idx}")
        out[key] = pd.to_numeric(body[idx[0]].values, errors="coerce")
    out.index.name = "month"
    return out.dropna(how="all")


def fetch_pinksheet(primary_only: bool):
    try:
        df = _parse_pink(_get(PINK_PRIMARY))
        _save(df, "pinksheet_monthly_avg")
        _record("pinksheet_monthly_avg", "CMO Monthly Prices", PINK_PRIMARY,
                "PRIMARY", df)
        return
    except Exception as e:                              # noqa: BLE001
        err = repr(e)[:120]
    if primary_only:
        _record("pinksheet_monthly_avg", "CMO Monthly Prices", PINK_PRIMARY,
                "FAILED", note=err)
        return
    m = MIRRORS["pinksheet"]
    url = RAW_GH.format(**m)
    try:
        df = _parse_pink(_get(url))
        _save(df, "pinksheet_monthly_avg")
        _record("pinksheet_monthly_avg", "CMO Monthly Prices", url, "MIRROR",
                df, note=f"primary refused ({err}); {m['note']}")
    except Exception as e2:                             # noqa: BLE001
        _record("pinksheet_monthly_avg", "CMO Monthly Prices", url, "FAILED",
                note=f"primary {err}; mirror {repr(e2)[:120]}")


# --------------------------------------------------------------------- FRED
def _mirror_daily(key: str) -> tuple[pd.Series, str, str]:
    m = MIRRORS[key]
    url = RAW_GH.format(**m)
    df = pd.read_csv(io.BytesIO(_get(url)))
    if "filter_col" in m:
        df = df[df[m["filter_col"]] == m["filter_val"]]
    s = pd.Series(df[m["value_col"]].values,
                  index=pd.to_datetime(df[m["date_col"]]))
    return s, url, m["note"]


def fetch_fred(code: str, primary_only: bool):
    url = FRED_CSV.format(code=code)
    name = f"fred_{code}"
    try:
        df = pd.read_csv(io.BytesIO(_get(url)), na_values=".")
        s = pd.Series(df.iloc[:, 1].values,
                      index=pd.to_datetime(df.iloc[:, 0]))
        out = _monthly_from_daily(s)
        _save(out, name)
        _record(name, code, url, "PRIMARY", out)
        return
    except Exception as e:                              # noqa: BLE001
        err = repr(e)[:120]
    if not primary_only and code in MIRRORS:
        try:
            s, murl, note = _mirror_daily(code)
            out = _monthly_from_daily(s)
            _save(out, name)
            _record(name, code, murl, "MIRROR", out,
                    note=f"primary refused ({err}); {note}")
            return
        except Exception as e2:                         # noqa: BLE001
            err += f"; mirror {repr(e2)[:120]}"
    _record(name, code, url, "FAILED", note=err)


def fetch_brent_eia(primary_only: bool):
    name, code = "eia_brent_spot", "RBRTE"
    url = "https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls"
    try:
        df = pd.read_excel(io.BytesIO(_get(url)), sheet_name="Data 1",
                           skiprows=2)
        out = _monthly_from_daily(pd.Series(df.iloc[:, 1].values,
                                            index=pd.to_datetime(df.iloc[:, 0])))
        _save(out, name)
        _record(name, code, url, "PRIMARY", out)
        return
    except Exception as e:                              # noqa: BLE001
        err = repr(e)[:120]
    if not primary_only:
        try:
            s, murl, note = _mirror_daily("BRENT_EIA")
            out = _monthly_from_daily(s)
            _save(out, name)
            _record(name, code, murl, "MIRROR", out,
                    note=f"primary refused ({err}); {note}")
            return
        except Exception as e2:                         # noqa: BLE001
            err += f"; mirror {repr(e2)[:120]}"
    _record(name, code, url, "FAILED", note=err)


# -------------------------------------------------------------------- Yahoo
def fetch_yahoo(sym: str, name: str, primary_only: bool):
    now = int(dt.datetime.now().timestamp())
    url = YAHOO.format(sym=requests.utils.quote(sym), now=now)
    try:
        j = json.loads(_get(url))["chart"]["result"][0]
        ts = pd.to_datetime(j["timestamp"], unit="s").normalize()
        close = j["indicators"]["quote"][0]["close"]
        out = _monthly_from_daily(pd.Series(close, index=ts))
        _save(out, name)
        _record(name, sym, url.split("?")[0], "PRIMARY", out)
        return
    except Exception as e:                              # noqa: BLE001
        err = repr(e)[:120]
    if not primary_only and name in MIRRORS:
        try:
            s, murl, note = _mirror_daily(name)
            out = _monthly_from_daily(s)
            _save(out, name)
            _record(name, sym, murl, "MIRROR", out,
                    note=f"primary refused ({err}); {note}")
            return
        except Exception as e2:                         # noqa: BLE001
            err += f"; mirror {repr(e2)[:120]}"
    _record(name, sym, url.split("?")[0], "FAILED", note=err)


# ------------------------------------------------------- India FPI (NSDL)
def fetch_fpi(primary_only: bool):
    """Monthly net FPI equity flow, INR crore.

    NSDL serves an HTML table per year. If the shell cannot reach it, the
    operator saves the yearly tables from NSDL as one CSV with columns
    month (YYYY-MM), fpi_equity_net_inr_cr at data/raw/fpi_equity_monthly.csv
    and commits it; this loader then picks it up.
    """
    name = "nsdl_fpi_equity_monthly"
    manual = RAW / "fpi_equity_monthly.csv"
    try:
        tables = pd.read_html(io.BytesIO(_get(NSDL_FPI)))
        t = max(tables, key=len)
        _save(t, name + "_raw_table")
        _record(name + "_raw_table", "NSDL FPI monthly", NSDL_FPI, "PRIMARY",
                note="raw HTML table saved; map columns to month,"
                     "fpi_equity_net_inr_cr into data/raw/"
                     "fpi_equity_monthly.csv")
    except Exception as e:                              # noqa: BLE001
        _record(name, "NSDL FPI monthly", NSDL_FPI, "FAILED",
                note=repr(e)[:120])
    if manual.exists():
        df = pd.read_csv(manual, dtype={"month": str}).set_index("month")
        _save(df, name)
        _record(name, "NSDL FPI monthly (operator file)", str(manual),
                "MANUAL", df)


def write_sources():
    lines = ["# Data sources", "",
             f"Written by fetch.py on {TODAY}. One row per cached series. "
             "Status PRIMARY = the named source served it; MIRROR = the "
             "primary host refused this shell and a public GitHub copy of "
             "the same upstream served it (re-run `python fetch.py "
             "--primary` on the operator laptop to replace it); FAILED = no "
             "data, the model runs without it.", "",
             "| File | Series code | Status | Source URL used | First | Last "
             "| Rows | Fetched | Note |", "|---|---|---|---|---|---|---|---|---|"]
    for r in LOG:
        lines.append(f"| {r['name']}.csv | {r['code']} | {r['status']} | "
                     f"{r['url']} | {r['first']} | {r['last']} | {r['rows']} "
                     f"| {r['fetched']} | {r['note']} |")
    (DATA / "sources.md").write_text("\n".join(lines) + "\n")


def main():
    primary_only = "--primary" in sys.argv
    DATA.mkdir(exist_ok=True)
    RAW.mkdir(exist_ok=True)
    fetch_pinksheet(primary_only)
    for code in FRED_SERIES:
        fetch_fred(code, primary_only)
    fetch_brent_eia(primary_only)
    for sym, name in YAHOO_SYMS.items():
        fetch_yahoo(sym, name, primary_only)
    fetch_fpi(primary_only)
    write_sources()
    for r in LOG:
        print(f"{r['status']:8} {r['name']:28} {r['first']:>8} -> "
              f"{r['last']:8}  {r['url'][:70]}")


if __name__ == "__main__":
    main()
