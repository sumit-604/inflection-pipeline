#!/usr/bin/env python3
"""Build one clean CSV per series from data/raw/, plus sources.md and gaps.md.

Every value comes from a raw file listed in data/raw/manifest.json. Nothing
is typed, filled forward or interpolated. A date a source does not publish
stays blank, and data/gaps.md lists it.

Outputs (data/):
  net_laf.csv          date, net_laf_cr (surplus +, deficit -), raw value, sign rule
  cd_3m.csv            date, cd_3m_pct (FBIL CD curve, 3-month tenor)
  mtf_book.csv         date, mtf_combined_cr, mtf_nse_cr, mtf_bse_cr
  nifty_smallcap_250.csv, nifty_microcap_250.csv, nifty_50.csv   date, close
  panel_daily.csv      all series on the trading-day calendar, blanks kept
  sources.md, gaps.md

Each series CSV carries source_url and downloaded_on on every row.

Run: python build_data.py [--laf-col NAME] [--laf-sign surplus_positive|injection_positive]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = Path(os.environ.get("LSC_DATA", HERE / "data"))
RAW = DATA / "raw"
START = pd.Timestamp("2023-01-01")
INDEX_KEYS = ["nifty_smallcap_250", "nifty_microcap_250", "nifty_50"]
LOG: list[dict] = []


def manifest() -> dict:
    p = RAW / "manifest.json"
    if not p.exists():
        sys.exit(f"missing {p}; run fetch_laptop.py on the laptop first")
    return json.loads(p.read_text())


def files_for(series: str, m: dict) -> list[tuple[Path, dict]]:
    out = []
    for name, meta in sorted(m.items()):
        if meta["series"] == series:
            p = RAW / name
            if not p.exists():
                sys.exit(f"manifest lists {name} but the file is not in {RAW}")
            out.append((p, meta))
    return out


def _read_table(p: Path) -> pd.DataFrame:
    if p.suffix.lower() in (".xlsx", ".xls"):
        return pd.read_excel(p)
    if p.suffix.lower() == ".json":
        return pd.DataFrame(json.loads(p.read_text()))
    return pd.read_csv(p)


def _to_dt(col: pd.Series) -> pd.Series:
    """ISO strings parse as ISO; anything else day-first (Indian sources)."""
    s = col.astype(str).str.strip()
    iso = s.str.match(r"^\d{4}-\d{2}-\d{2}")
    out = pd.Series(pd.NaT, index=s.index, dtype="datetime64[ns]")
    out[iso] = pd.to_datetime(s[iso].str[:10], format="%Y-%m-%d", errors="coerce")
    out[~iso] = pd.to_datetime(s[~iso], dayfirst=True, format="mixed", errors="coerce")
    return out


def _date_col(df: pd.DataFrame) -> str:
    for c in df.columns:
        if "date" in str(c).lower():
            return c
    for c in df.columns:
        if _to_dt(df[c]).notna().mean() > 0.9:
            return c
    sys.exit(f"no date column in {list(df.columns)}")


def _stamp(df: pd.DataFrame, meta: dict) -> pd.DataFrame:
    df["source_url"] = meta["source_url"]
    df["downloaded_on"] = meta["downloaded_on"]
    return df


def _save(df: pd.DataFrame, name: str, value_col: str, metas: list[dict],
          note: str) -> None:
    df = df[df["date"] >= START].sort_values("date").drop_duplicates("date", keep="last")
    df.to_csv(DATA / f"{name}.csv", index=False, date_format="%Y-%m-%d")
    LOG.append(dict(file=f"{name}.csv", value=value_col,
                    urls=sorted({m["source_url"] for m in metas}),
                    downloaded=sorted({m["downloaded_on"] for m in metas}),
                    first=df["date"].min(), last=df["date"].max(),
                    rows=int(df[value_col].notna().sum()), note=note))


# ---------------------------------------------------------------- series
def build_mtf(m: dict) -> pd.DataFrame | None:
    fs = files_for("mtf", m)
    if not fs:
        return None
    p, meta = fs[-1]                       # latest snapshot supersedes
    js = json.loads(p.read_text())

    def side(key):
        pts = [x for x in js.get(key, []) if x.get("kind", "day") == "day"]
        s = pd.Series({pd.Timestamp(x["date"]): x["net"] for x in pts}, dtype=float)
        return s
    df = pd.DataFrame({"mtf_combined_cr": side("combined"),
                       "mtf_nse_cr": side("nse"), "mtf_bse_cr": side("bse")})
    df.index.name = "date"
    df = _stamp(df.reset_index(), meta)
    _save(df, "mtf_book", "mtf_combined_cr", [meta],
          "INR crore. BSE disclosures begin about 2025-10-15 (indiamtf "
          "openapi.json); before that the combined book is NSE only. "
          "This is a level break, not market growth.")
    return df


def build_indices(m: dict) -> dict[str, pd.DataFrame]:
    out = {}
    metas_by_key: dict[str, list[dict]] = {}
    nse_names = {"Nifty 50": "nifty_50", "Nifty Smallcap 250": "nifty_smallcap_250",
                 "Nifty Microcap 250": "nifty_microcap_250"}
    for p, meta in files_for("indices", m):
        if p.name.startswith("nse_ind_close_all") and p.suffix == ".csv":
            raw = pd.read_csv(p)
            for nm, key in nse_names.items():
                r = raw[raw["index_name"] == nm]
                df = pd.DataFrame({"date": _to_dt(r["index_date"]),
                                   "close": pd.to_numeric(r["close"], errors="coerce"),
                                   "source_url": r["source_url"].values,
                                   "downloaded_on": meta["downloaded_on"]})
                prev = out.get(key)
                out[key] = df if prev is None else pd.concat([prev, df])
                metas_by_key.setdefault(key, []).append(meta)
            continue
        key = next((k for k in INDEX_KEYS if k in p.name), None)
        if key is None:
            continue
        rows = json.loads(p.read_text())
        df = pd.DataFrame(rows)
        dc = _date_col(df)
        cc = next(c for c in df.columns if str(c).upper() == "CLOSE")
        df = pd.DataFrame({"date": _to_dt(df[dc]),
                           "close": pd.to_numeric(df[cc].astype(str).str.replace(",", ""),
                                                  errors="coerce")})
        df = _stamp(df, meta)
        metas_by_key.setdefault(key, []).append(meta)
        prev = out.get(key)
        out[key] = df if prev is None else pd.concat([prev, df])
    for key, df in out.items():
        _save(df, key, "close", metas_by_key[key],
              "Index close, price return. NSE ind_close_all daily files (NSE Indices "
              "publishes niftyindices.com); per-day file URL in the source_url column")
    return out


def build_cd(m: dict) -> pd.DataFrame | None:
    parts, metas = [], []
    for p, meta in files_for("cd3m", m):
        df = _read_table(p)
        dc = _date_col(df)
        tc = next((c for c in df.columns if "tenor" in str(c).lower()), None)
        rc = next((c for c in df.columns if "rate" in str(c).lower()), None)
        if rc is None:
            sys.exit(f"{p.name}: no rate column in {list(df.columns)}")
        if tc is not None:
            t = df[tc].astype(str).str.strip().str.lower()
            df = df[t.str.fullmatch(r"3\s*(months?|m)|91\s*days?")]
        parts.append(_stamp(pd.DataFrame({
            "date": _to_dt(df[dc]),
            "cd_3m_pct": pd.to_numeric(df[rc], errors="coerce")}), meta))
        metas.append(meta)
    if not parts:
        return None
    df = pd.concat(parts)
    _save(df, "cd_3m", "cd_3m_pct", metas, "FBIL CD curve, 3-month tenor, % p.a.")
    return df


def build_laf(m: dict, col: str | None, sign: str | None) -> pd.DataFrame | None:
    parts, metas = [], []
    for p, meta in files_for("laf", m):
        df = _read_table(p)
        dc = _date_col(df)
        if col:
            vc = col
        else:
            hits = [c for c in df.columns
                    if re.search(r"net", str(c), re.I)
                    and re.search(r"laf|liquidity|inject|absorb", str(c), re.I)]
            if len(hits) != 1:
                sys.exit(f"{p.name}: cannot pick the net LAF column from "
                         f"{list(df.columns)}; pass --laf-col")
            vc = hits[0]
        rule = sign
        if rule is None:
            if re.search(r"inject", str(vc), re.I):
                rule = "injection_positive"
            else:
                sys.exit(f"{p.name}: sign of '{vc}' is not stated in its name; "
                         "pass --laf-sign surplus_positive or injection_positive")
        raw = pd.to_numeric(df[vc].astype(str).str.replace(",", ""), errors="coerce")
        val = -raw if rule == "injection_positive" else raw
        part = _stamp(pd.DataFrame({
            "date": _to_dt(df[dc]),
            "net_laf_cr": val, "raw_value": raw, "raw_column": str(vc),
            "sign_rule": rule}), meta)
        if "release_url" in df.columns:          # per-release URL beats the listing URL
            part["source_url"] = df["release_url"].values
        parts.append(part)
        metas.append(meta)
    if not parts:
        return None
    df = pd.concat(parts)
    _save(df, "net_laf", "net_laf_cr", metas,
          "Rs crore. Stored as surplus positive, deficit negative. RBI reports "
          "net injection as positive; that sign is flipped here (sign_rule column).")
    return df


# ---------------------------------------------------------------- panel, gaps
def _ranges(dates: list[pd.Timestamp], cal: pd.DatetimeIndex) -> list[str]:
    if not dates:
        return []
    pos = {d: i for i, d in enumerate(cal)}
    out, a, b = [], dates[0], dates[0]
    for d in dates[1:]:
        if pos[d] == pos[b] + 1:
            b = d
        else:
            out.append((a, b))
            a = b = d
    out.append((a, b))
    return [f"{x:%Y-%m-%d}" if x == y else
            f"{x:%Y-%m-%d} to {y:%Y-%m-%d} ({pos[y] - pos[x] + 1} days)"
            for x, y in out]


def panel_and_gaps(series: dict[str, pd.Series], end: pd.Timestamp) -> None:
    idx = [s for k, s in series.items() if k.startswith("nifty")]
    cal = (series["nifty_50"].index if "nifty_50" in series
           else pd.DatetimeIndex(sorted(set().union(*[s.index for s in idx])))
           if idx else None)
    lines = ["# Data gaps, liquidity vs small caps", "",
             f"Built {pd.Timestamp.today():%Y-%m-%d}. Window {START:%Y-%m-%d} "
             f"to {end:%Y-%m-%d}.",
             "Calendar = Nifty 50 trading days from niftyindices.com. A gap is "
             "a trading day the source did not publish. Gaps stay blank; "
             "nothing is filled.", ""]
    if cal is None:
        lines += ["No index file yet, so no trading calendar. Every series is "
                  "NOT FOUND until the index fetch runs.", ""]
        cal = pd.DatetimeIndex([])
    cal = cal[(cal >= START) & (cal <= end)]
    want = ["net_laf_cr", "cd_3m_pct", "mtf_combined_cr", "mtf_nse_cr",
            "nifty_smallcap_250", "nifty_microcap_250", "nifty_50"]
    panel = pd.DataFrame(index=cal)
    panel.index.name = "date"
    for k in want:
        s = series.get(k)
        if s is None:
            lines += [f"## {k}", "", "NOT FOUND. No raw file in the manifest.", ""]
            panel[k] = pd.NA
            continue
        panel[k] = s.reindex(cal)
        miss = list(panel.index[panel[k].isna()])
        extra = len(s.index.difference(cal))
        lines += [f"## {k}", "",
                  f"{len(cal) - len(miss)} of {len(cal)} trading days filled; "
                  f"{len(miss)} blank. {extra} source dates fall outside the "
                  "trading calendar (kept in the series CSV, dropped from the panel)."]
        rs = _ranges(miss, cal)
        lines += [""] + [f"- {r}" for r in rs] + [""] if rs else [""]
    panel.to_csv(DATA / "panel_daily.csv", date_format="%Y-%m-%d")
    (DATA / "gaps.md").write_text("\n".join(lines) + "\n")


def write_sources() -> None:
    L = ["# Data sources, liquidity vs small caps", "",
         "Written by build_data.py. Raw files are in data/raw/; "
         "data/raw/manifest.json records each file's URL and download date.", "",
         "| File | Value | First | Last | Rows | Source URL | Downloaded | Note |",
         "|---|---|---|---|---|---|---|---|"]
    for r in LOG:
        L.append(f"| {r['file']} | {r['value']} | {r['first']:%Y-%m-%d} | "
                 f"{r['last']:%Y-%m-%d} | {r['rows']} | {'<br>'.join(r['urls'])} | "
                 f"{', '.join(r['downloaded'])} | {r['note']} |")
    (DATA / "sources.md").write_text("\n".join(L) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--laf-col")
    ap.add_argument("--laf-sign", choices=["surplus_positive", "injection_positive"])
    ap.add_argument("--end", default=pd.Timestamp.today().strftime("%Y-%m-%d"))
    a = ap.parse_args()
    m = manifest()
    series: dict[str, pd.Series] = {}
    laf = build_laf(m, a.laf_col, a.laf_sign)
    if laf is not None:
        series["net_laf_cr"] = laf.set_index("date")["net_laf_cr"].groupby(level=0).last()
    cd = build_cd(m)
    if cd is not None:
        series["cd_3m_pct"] = cd.set_index("date")["cd_3m_pct"].groupby(level=0).last()
    mtf = build_mtf(m)
    if mtf is not None:
        series["mtf_combined_cr"] = mtf.set_index("date")["mtf_combined_cr"]
        series["mtf_nse_cr"] = mtf.set_index("date")["mtf_nse_cr"]
    for k, df in build_indices(m).items():
        series[k] = df.set_index("date")["close"].groupby(level=0).last()
    for k in series:
        series[k] = series[k][series[k].index >= START].sort_index()
    panel_and_gaps(series, pd.Timestamp(a.end))
    write_sources()
    for r in LOG:
        print(f"{r['file']:28s} {r['rows']:5d} rows  {r['first']:%Y-%m-%d} .. {r['last']:%Y-%m-%d}")
    print("wrote panel_daily.csv, sources.md, gaps.md")


if __name__ == "__main__":
    main()
