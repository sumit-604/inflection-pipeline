#!/usr/bin/env python3
"""Compute the facts sheet the nightly brief is written from.

Reads the 34 Chartink table CSVs for the latest trade date under
data/chartink/csv/<date>/ and writes one dense markdown sheet of numbers:
regime readings with history percentiles, index and sector tables, every
screener's size, sector mix and leading names, institutional-flow shifts, and
the names that appear on several lists at once.

It is arithmetic only. It ranks, counts, and intersects. It draws no conclusion.
The brief writer reads this sheet, not the 34 raw files.

A file that is missing is reported as missing. A number that cannot be computed
is written as NOT FOUND. Nothing is estimated.

Output:
    data/chartink/analysis/facts/<date>.md
    data/chartink/analysis/facts/latest.md

Usage:
    python tools/chartink/facts.py            # latest date folder
    python tools/chartink/facts.py 2026-09-04
"""

from __future__ import annotations

import re
import shutil
import sys
import warnings
from collections import Counter
from pathlib import Path

import pandas as pd

# A few return columns hold values in the tens of thousands of percent (new
# listings). numpy warns on the sum. The numbers themselves are fine.
warnings.filterwarnings("ignore", category=RuntimeWarning)

REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_ROOT = REPO_ROOT / "data" / "chartink" / "csv"
OUT_DIR = REPO_ROOT / "data" / "chartink" / "analysis" / "facts"

# The 34 table tiles, by their export filename stem. Missing ones are reported.
EXPECTED = [
    "MBM 2.0 (magnitude)", "MBM 2.0 (velocity) - basic",
    "MBM 2.0 (velocity) - advanced",
    "Market Breadth_ Number above 500 indicates trend reversal",
    "Index Level Changes", "Weekly Percentage Change in Indices",
    "Quarterly Percentage Change in Indices", "Indices _ %Age Away from 30 WMA",
    "Sectors Above Key Weekly EMA",
    "Minervini Screener", "Darvas Screener", "Breakouts v2",
    "Potential Breakouts", "Modified Relative Strength", "Momentum Investing",
    "Stocks at 52 week high", "Top Gainers Today",
    "CCI Daily crossing 100 (Short to medium term breakout scanner)",
    "CCI Daily crossing above -100 (Trendline reversal scanner)",
    "CCI Weekly crossing 100 (Long term breakout scanner)",
    "CCI Weekly crossing above -100 (Trendline reversal scanner)",
    "Large Cap Stocks Above VWAP", "Mid Cap Stocks Above VWAP",
    "Small Cap Stocks Above VWAP",
    "Return 1Week", "Return 2Week", "Return 1Month", "Return 3Month",
    "Return 6Month", "Return Yearly",
    "Stocks Where FIIs are Increasing Shareholding",
    "DII increased shareholding in terms of %",
    "Stocks Where Promoters are Increasing Shareholding",
    "Stocks Where Retail is Increasing Shareholding",
]

MIN_HISTORY = 20


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def norm(col):
    """Lower-case, single-spaced column name.

    Chartink's own export writes '4.5%' as '4-5%' in headers. Fold that so a
    file from either source reads the same.
    """
    c = re.sub(r"\s+", " ", str(col).strip().lower())
    return c.replace("4-5%", "4.5%")


def is_text(series):
    return not pd.api.types.is_numeric_dtype(series)


def load_folder(date):
    folder = CSV_ROOT / date
    tables = {}
    missing = []
    for name in EXPECTED:
        p = folder / (name + ".csv")
        if not p.exists():
            missing.append(name)
            continue
        df = pd.read_csv(p, encoding="utf-8-sig")
        df.columns = [norm(c) for c in df.columns]
        # Chartink emits a ~1.7e308 sentinel where its own arithmetic divided
        # by zero. No market number has that size. Treat it as missing.
        num = df.select_dtypes(include="number").columns
        for c in num:
            df.loc[df[c].abs() > 1e12, c] = float("nan")
        # A grouped tile with size > 1 carries several dates per symbol.
        # Counting names must see each symbol once: keep its latest date.
        if "symbol" in df.columns and "date" in df.columns:
            df = (df.sort_values("date", ascending=False)
                    .drop_duplicates("symbol", keep="first")
                    .reset_index(drop=True))
        tables[name] = df
    return tables, missing


def latest_date():
    if not CSV_ROOT.exists():
        return None
    dates = sorted(p.name for p in CSV_ROOT.iterdir()
                   if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name))
    return dates[-1] if dates else None


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def f(v, nd=2):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return "NOT FOUND"
    try:
        return f"{float(v):,.{nd}f}"
    except (TypeError, ValueError):
        return str(v)


def fs(v, nd=2):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return "NOT FOUND"
    return f"{float(v):+,.{nd}f}"


def table(headers, rows, align=None):
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(align) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def num_align(n_text, n_num):
    return ["---"] * n_text + ["---:"] * n_num


# ---------------------------------------------------------------------------
# Regime: the time-series tables
# ---------------------------------------------------------------------------

def series_stats(df, col):
    """Latest, changes, percentile and 20-day range for one column.

    Export files are newest first. Reverse to oldest first for arithmetic.
    """
    if col not in df.columns:
        return None
    s = pd.to_numeric(df[col], errors="coerce").dropna().iloc[::-1].reset_index(drop=True)
    if s.empty:
        return None
    latest = s.iloc[-1]
    n = len(s)

    def chg(k):
        return latest - s.iloc[-1 - k] if n > k else None

    pct = 100.0 * (s <= latest).sum() / n if n >= MIN_HISTORY else None
    last20 = s.iloc[-20:] if n >= 20 else s
    return {
        "latest": latest, "d1": chg(1), "d5": chg(5), "d20": chg(20),
        "pct": pct, "n": n, "lo20": last20.min(), "hi20": last20.max(),
        "lo": s.min(), "hi": s.max(),
        "last5": list(s.iloc[-5:]),
    }


def regime_section(tables):
    out = ["## 1. Breadth regime (market-wide, with history)", ""]
    out.append("Percentile is the rank of the latest reading against that "
               "series' own history (share of readings at or below it). "
               "n is the history length. 20d range is the last 20 readings.")
    out.append("")

    spec = [
        ("MBM 2.0 (magnitude)", [
            ("abv 10ma", "% above 10 EMA"), ("abv 20ma", "% above 20 EMA"),
            ("abv 50ma", "% above 50 EMA"), ("abv 200ma", "% above 200 EMA")]),
        ("MBM 2.0 (velocity) - basic", [
            ("4% advance", "4% advancers (% of mkt)"),
            ("4% decline", "4% decliners (% of mkt)"),
            ("net breadth", "Net breadth (adv minus dec)"),
            ("3% range", "Stocks in <3% daily range (%)"),
            ("5d range", "Stocks in <4% 5-day range (%)"),
            ("volume", "Volume expansion ratio (hi-vol / lo-vol)"),
            ("+15% in 5d", "+15% in 5 days (%)"),
            ("-10% in 5d", "-10% in 5 days (%)"),
            ("10% + 10ema", ">10% above 10 EMA (%)"),
            ("10% - 10ema", ">10% below 10 EMA (%)")]),
        ("MBM 2.0 (velocity) - advanced", [
            ("breakouts", "Breakouts (high >= +4% vs prev close, %)"),
            ("breakdowns", "Breakdowns (low <= -4%, %)"),
            ("up close %", "Up-close share of breakouts (%)"),
            ("down close %", "Down-close share of breakdowns (%)"),
            ("new 52-wk high", "New 52wk highs (%)"),
            ("new 52-wk low", "New 52wk lows (%)"),
            ("net nh-nl", "Net new highs minus lows"),
            ("15% 52wh", "Within 15% of 52wk high (%)"),
            ("15% 52wl", "Within 15% of 52wk low (%)"),
            ("net 15% h-l", "Net 15% H minus L"),
            ("30% 52wh", "Within 30% of 52wk high (%)"),
            ("30% 52 wl", "Within 30% of 52wk low (%)"),
            ("net 30% h-l", "Net 30% H minus L")]),
        ("Market Breadth_ Number above 500 indicates trend reversal", [
            ("up 4.5%+ today", "Count up 4.5%+ today"),
            ("down 4.5%+ today", "Count down 4.5%+ today"),
            ("up 20%+ in 5d", "Count up 20%+ in 5d"),
            ("down 20%+ in 5d", "Count down 20%+ in 5d"),
            ("above 20dma", "Count above 20 DMA"),
            ("below 20dma", "Count below 20 DMA"),
            ("above 50dma", "Count above 50 DMA"),
            ("below 50dma", "Count below 50 DMA"),
            ("above 200dma", "Count above 200 DMA"),
            ("below 200dma", "Count below 200 DMA")]),
    ]

    for fname, cols in spec:
        df = tables.get(fname)
        out.append("### " + fname)
        out.append("")
        if df is None:
            out.append("FILE MISSING")
            out.append("")
            continue
        rows = []
        for col, label in cols:
            s = series_stats(df, col)
            if not s:
                rows.append([label] + ["NOT FOUND"] * 7)
                continue
            rows.append([
                label, f(s["latest"]), fs(s["d1"]), fs(s["d5"]), fs(s["d20"]),
                f(s["pct"], 0) if s["pct"] is not None else "n=" + str(s["n"]),
                f(s["lo20"]) + " to " + f(s["hi20"]),
                " / ".join(f(v) for v in s["last5"]),
            ])
        out.append(table(
            ["Metric", "Latest", "1d", "5d", "20d", "Pctile", "20d range",
             "Last 5 (oldest to newest)"],
            rows, num_align(1, 7)))
        out.append("")

    # Derived ratios from the count table.
    cnt = tables.get("Market Breadth_ Number above 500 indicates trend reversal")
    if cnt is not None:
        top = cnt.iloc[0]
        def g(c):
            try:
                return float(top[c])
            except (KeyError, ValueError, TypeError):
                return None
        a20, b20 = g("above 20dma"), g("below 20dma")
        a50, b50 = g("above 50dma"), g("below 50dma")
        a200, b200 = g("above 200dma"), g("below 200dma")
        out.append("### Derived from the count table (latest day)")
        out.append("")
        rows = []
        for lbl, a, b in (("20 DMA", a20, b20), ("50 DMA", a50, b50),
                          ("200 DMA", a200, b200)):
            if a is None or b is None:
                rows.append([lbl, "NOT FOUND", "NOT FOUND", "NOT FOUND"])
            else:
                tot = a + b
                rows.append([lbl, f(a, 0) + " / " + f(b, 0),
                             f(100 * a / tot if tot else None, 1) + "%",
                             f(a / b if b else None, 2)])
        out.append(table(["Line", "Above / below", "Share above", "Ratio"],
                         rows, num_align(1, 3)))
        u, d = g("up 4.5%+ today"), g("down 4.5%+ today")
        u5, d5 = g("up 20%+ in 5d"), g("down 20%+ in 5d")
        out.append("")
        out.append("- Up 4.5%+ vs down 4.5%+ today: " + f(u, 0) + " vs " + f(d, 0)
                   + (" (ratio " + f(u / d, 2) + ")" if u is not None and d else ""))
        out.append("- Up 20%+ vs down 20%+ in 5d: " + f(u5, 0) + " vs " + f(d5, 0))
        out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Indices and sectors
# ---------------------------------------------------------------------------

def indices_section(tables):
    out = ["## 2. Indices", ""]
    lvl = tables.get("Index Level Changes")
    wk = tables.get("Weekly Percentage Change in Indices")
    qt = tables.get("Quarterly Percentage Change in Indices")
    ema = tables.get("Indices _ %Age Away from 30 WMA")

    if lvl is None:
        out.append("Index Level Changes: FILE MISSING")
        return "\n".join(out)

    m = lvl[["symbol", "% change", "ltp"]].rename(
        columns={"% change": "1d %", "ltp": "LTP"})
    if wk is not None:
        m = m.merge(wk[["symbol", "% change"]].rename(columns={"% change": "1w %"}),
                    on="symbol", how="left")
    if qt is not None:
        m = m.merge(qt[["symbol", "% change"]].rename(columns={"% change": "3m %"}),
                    on="symbol", how="left")
    if ema is not None:
        m = m.merge(ema[["symbol", "% from 30w ema"]].rename(
            columns={"% from 30w ema": "vs 30W EMA %"}), on="symbol", how="left")
    for c in ("1d %", "1w %", "3m %", "vs 30W EMA %", "LTP"):
        if c in m.columns:
            m[c] = pd.to_numeric(m[c], errors="coerce")
    m = m.sort_values("1d %", ascending=False)

    rows = []
    for _, r in m.iterrows():
        rows.append([r["symbol"], f(r.get("LTP")), fs(r.get("1d %")),
                     fs(r.get("1w %")) if "1w %" in m else "NOT FOUND",
                     fs(r.get("3m %")) if "3m %" in m else "NOT FOUND",
                     fs(r.get("vs 30W EMA %")) if "vs 30W EMA %" in m else "NOT FOUND"])
    out.append(str(len(m)) + " indices, sorted by 1-day change.")
    out.append("")
    out.append(table(["Index", "LTP", "1d %", "1w %", "3m %", "vs 30W EMA %"],
                     rows, num_align(1, 5)))
    out.append("")

    def sub(col, k, asc):
        if col not in m.columns:
            return "NOT FOUND"
        s = m.dropna(subset=[col]).sort_values(col, ascending=asc).head(k)
        return ", ".join(f"{r['symbol']} {fs(r[col])}" for _, r in s.iterrows())

    out.append("- Top 5 by 1d: " + sub("1d %", 5, False))
    out.append("- Bottom 5 by 1d: " + sub("1d %", 5, True))
    out.append("- Top 5 by 1w: " + sub("1w %", 5, False))
    out.append("- Bottom 5 by 1w: " + sub("1w %", 5, True))
    out.append("- Top 5 by 3m: " + sub("3m %", 5, False))
    out.append("- Bottom 5 by 3m: " + sub("3m %", 5, True))
    out.append("- Furthest above 30W EMA: " + sub("vs 30W EMA %", 5, False))
    out.append("- Furthest below 30W EMA: " + sub("vs 30W EMA %", 5, True))
    if "vs 30W EMA %" in m.columns:
        below = m[m["vs 30W EMA %"] < 0]
        out.append("- Indices below their 30W EMA: " + str(len(below)) + " of "
                   + str(m["vs 30W EMA %"].notna().sum())
                   + (" (" + ", ".join(below["symbol"]) + ")" if len(below) else ""))
    if "1d %" in m.columns and "1w %" in m.columns:
        up_d = int((m["1d %"] > 0).sum())
        up_w = int((m["1w %"] > 0).sum())
        out.append(f"- Indices up on the day: {up_d} of {len(m)}; up on the week: "
                   f"{up_w} of {m['1w %'].notna().sum()}")
    out.append("")
    return "\n".join(out)


def sectors_section(tables):
    out = ["## 3. Sectors above key weekly EMAs (% of sector members)", ""]
    df = tables.get("Sectors Above Key Weekly EMA")
    if df is None:
        out.append("FILE MISSING")
        return "\n".join(out)
    cols = ["4w ema", "20w ema", "30w ema", "40w ema", "52w ema"]
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.sort_values("40w ema", ascending=False)
    rows = []
    for _, r in df.iterrows():
        flag = ""
        if r["4w ema"] < 50 and r["40w ema"] >= 60:
            flag = "short-term weak, long-term strong"
        elif r["4w ema"] >= 60 and r["40w ema"] < 50:
            flag = "short-term strong, long-term weak"
        elif r["4w ema"] >= 60 and r["40w ema"] >= 60:
            flag = "strong on all"
        elif r["4w ema"] < 40 and r["40w ema"] < 40:
            flag = "weak on all"
        rows.append([r["sector"]] + [f(r[c], 1) for c in cols] + [flag])
    out.append(str(len(df)) + " sectors, sorted by % above 40W EMA.")
    out.append("")
    out.append(table(["Sector", "4W", "20W", "30W", "40W", "52W", "Pattern"],
                     rows, num_align(1, 5) + ["---"]))
    out.append("")
    out.append("- Mean % above 40W EMA across sectors: " + f(df["40w ema"].mean(), 1))
    out.append("- Mean % above 4W EMA across sectors: " + f(df["4w ema"].mean(), 1))
    out.append("- Sectors with 4W below 20W (short-term losing the medium term): "
               + str(int((df["4w ema"] < df["20w ema"]).sum())) + " of " + str(len(df)))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Screeners
# ---------------------------------------------------------------------------

def mix(df, col, k=4):
    if col not in df.columns:
        return "NOT FOUND"
    c = Counter(df[col].dropna().astype(str))
    tot = sum(c.values())
    return ", ".join(f"{name} {n} ({100 * n / tot:.0f}%)" for name, n in c.most_common(k))


def top_names(df, sort_col, k=10, extra=None, asc=False):
    if sort_col not in df.columns:
        return ", ".join(df["symbol"].head(k)) if "symbol" in df.columns else "NOT FOUND"
    d = df.copy()
    d[sort_col] = pd.to_numeric(d[sort_col], errors="coerce")
    d = d.dropna(subset=[sort_col]).sort_values(sort_col, ascending=asc).head(k)
    parts = []
    for _, r in d.iterrows():
        s = f"{r['symbol']} {f(r[sort_col], 1)}"
        if extra and extra in d.columns:
            s += f" ({r[extra]})"
        parts.append(s)
    return ", ".join(parts)


def screener_block(name, df, sort_col, extra=None, describe_col=None):
    out = ["### " + name, ""]
    if df is None:
        out.append("FILE MISSING")
        out.append("")
        return "\n".join(out)
    n = len(df)
    out.append(f"- Names: {n}")
    if "sector" in df.columns:
        out.append("- Sector mix: " + mix(df, "sector"))
    for capcol in ("market cap", "category", "market cap category"):
        if capcol in df.columns and is_text(df[capcol]):
            out.append("- Cap mix: " + mix(df, capcol))
            break
    if describe_col and describe_col in df.columns:
        s = pd.to_numeric(df[describe_col], errors="coerce").dropna()
        if len(s):
            out.append(f"- {describe_col}: median {f(s.median(), 1)}, "
                       f"mean {f(s.mean(), 1)}, max {f(s.max(), 1)}, min {f(s.min(), 1)}")
    out.append("- Top by " + sort_col + ": " + top_names(df, sort_col, 12, extra))
    out.append("")
    return "\n".join(out)


def screeners_section(tables):
    out = ["## 4. Screener lists (each is a list of stocks meeting a rule)", ""]
    out.append("Each block: how many names qualify, what sectors and caps "
               "dominate, and the leading names by the tile's sort column.")
    out.append("")

    out.append(screener_block("Minervini Screener (trend template, 8 conditions)",
                              tables.get("Minervini Screener"), "vol > yr avg",
                              "sector", "1 week %"))
    out.append(screener_block("Darvas Screener (2x off 52wk low, near high, above 30W SMA)",
                              tables.get("Darvas Screener"), "vol > yr avg",
                              "sector", "1 week %"))
    out.append(screener_block("Breakouts v2 (EMA stack 10>21>50, within 25% of 10yr high)",
                              tables.get("Breakouts v2"), "1 week %", "sector",
                              "1 week %"))
    out.append(screener_block("Potential Breakouts (within 5% of 200d high, vol > 40d avg)",
                              tables.get("Potential Breakouts"), "vol > yr avg",
                              "sector", "1 week %"))
    out.append(screener_block("Modified Relative Strength (weekly CCI cross + 75% off low)",
                              tables.get("Modified Relative Strength"), "vol > yr avg",
                              "sector", "1 week %"))
    out.append(screener_block("Momentum Investing (32wk momentum / volatility)",
                              tables.get("Momentum Investing"), "column1", None, "roc"))
    out.append(screener_block("Stocks at 52 week high (close within Rs 1 of 52wk high)",
                              tables.get("Stocks at 52 week high"),
                              "current vol multiple of yearly avg", "sector",
                              "weekly return"))

    tg = tables.get("Top Gainers Today")
    out.append("### Top Gainers Today (whole market, sorted by % change)")
    out.append("")
    if tg is None:
        out.append("FILE MISSING")
    else:
        s = pd.to_numeric(tg["changeinpercentage"], errors="coerce").dropna()
        out.append(f"- Rows returned: {len(s)}")
        for th in (20, 10, 5, 3):
            out.append(f"- Count up >= {th}%: {int((s >= th).sum())}")
        out.append("- Top 15: " + top_names(tg, "changeinpercentage", 15))
    out.append("")

    for key, label in (
        ("CCI Daily crossing 100 (Short to medium term breakout scanner)",
         "CCI daily crossed above +100 (fresh daily momentum)"),
        ("CCI Daily crossing above -100 (Trendline reversal scanner)",
         "CCI daily crossed above -100 (daily reversal from oversold)"),
        ("CCI Weekly crossing 100 (Long term breakout scanner)",
         "CCI weekly crossed above +100 (fresh weekly momentum)"),
        ("CCI Weekly crossing above -100 (Trendline reversal scanner)",
         "CCI weekly crossed above -100 (weekly reversal from oversold)"),
    ):
        df = tables.get(key)
        out.append("### " + label)
        out.append("")
        if df is None:
            out.append("FILE MISSING")
        else:
            out.append(f"- Names: {len(df)}")
            out.append("- Sector mix: " + mix(df, "sector"))
            out.append("- Cap mix: " + mix(df, "category"))
            out.append("- Largest by market cap: "
                       + top_names(df, "market cap", 10, "sector"))
            out.append("- Biggest movers on the day: "
                       + top_names(df, "% change", 8, "sector"))
        out.append("")

    out.append("### Stocks above VWAP with 50 EMA > 200 EMA, by cap")
    out.append("")
    for key, label in (("Large Cap Stocks Above VWAP", "Large cap (>25,000 cr)"),
                       ("Mid Cap Stocks Above VWAP", "Mid cap (5,000 to 25,000 cr)"),
                       ("Small Cap Stocks Above VWAP", "Small cap (500 to 5,000 cr)")):
        df = tables.get(key)
        if df is None:
            out.append(f"- {label}: FILE MISSING")
        else:
            names = ", ".join(df["symbol"].head(15))
            out.append(f"- {label}: {len(df)} names. {names}"
                       + (" ..." if len(df) > 15 else ""))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Returns: leadership persistence across horizons
# ---------------------------------------------------------------------------

def returns_section(tables):
    out = ["## 5. Return leaders by horizon (close > 20, mcap > 500 cr)", ""]
    keys = [("Return 1Week", "1W"), ("Return 2Week", "2W"), ("Return 1Month", "1M"),
            ("Return 3Month", "3M"), ("Return 6Month", "6M"), ("Return Yearly", "1Y")]
    sets = {}
    for key, lbl in keys:
        df = tables.get(key)
        if df is None:
            out.append(f"- {lbl}: FILE MISSING")
            continue
        df = df.copy()
        df["% change"] = pd.to_numeric(df["% change"], errors="coerce")
        df = df.dropna(subset=["% change"]).sort_values("% change", ascending=False)
        sets[lbl] = list(df["symbol"])
        s = df["% change"]
        out.append(f"- {lbl}: {len(df)} names; #1 {df.iloc[0]['symbol']} "
                   f"{fs(s.iloc[0], 1)}; #10 {fs(s.iloc[min(9, len(s) - 1)], 1)}; "
                   f"median of list {fs(s.median(), 1)}")
        out.append("  - Top 10: " + top_names(df, "% change", 10))
    out.append("")
    if sets:
        cnt = Counter()
        for lbl, names in sets.items():
            for nme in names[:30]:
                cnt[nme] += 1
        multi = [(nme, k) for nme, k in cnt.most_common() if k >= 3]
        out.append("- Names in the top 30 of 3 or more horizons (persistent leaders): "
                   + (", ".join(f"{nme} ({k})" for nme, k in multi[:25]) if multi else "none"))
        if "1W" in sets and "1Y" in sets:
            fresh = [nme for nme in sets["1W"][:30] if nme not in set(sets["1Y"])]
            out.append("- In 1W top 30 but absent from the 1Y list (new leadership): "
                       + (", ".join(fresh[:20]) if fresh else "none"))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Institutional and promoter flow
# ---------------------------------------------------------------------------

def flow_section(tables):
    out = ["## 6. Shareholding shifts (quarterly filings, % of equity)", ""]
    out.append("Each list: stocks where that holder class rose. 'Change' is the "
               "3-quarter change in percentage points. Zero prior values usually "
               "mean a new listing or missing history, so the largest changes "
               "need that caveat.")
    out.append("")
    spec = [
        ("Stocks Where FIIs are Increasing Shareholding", "FII", "change in 3 qtr",
         "% current qtr"),
        ("DII increased shareholding in terms of %", "DII (4 straight quarters up)",
         "change in % in 3 qtrs", "% current quarter"),
        ("Stocks Where Promoters are Increasing Shareholding", "Promoter",
         "change in 3 qtrs", "% current qtr"),
        ("Stocks Where Retail is Increasing Shareholding", "Retail", "change in 3 qtrs",
         "% current qtr"),
    ]
    names = {}
    for key, lbl, chg, cur in spec:
        df = tables.get(key)
        out.append("### " + lbl)
        out.append("")
        if df is None:
            out.append("FILE MISSING")
            out.append("")
            continue
        df = df.copy()
        df[chg] = pd.to_numeric(df[chg], errors="coerce")
        df[cur] = pd.to_numeric(df[cur], errors="coerce")
        # Exclude rows whose 3-quarters-ago value is 0: no real history.
        prior_col = [c for c in df.columns if c.startswith("% 3 q")]
        real = df
        if prior_col:
            p = pd.to_numeric(df[prior_col[0]], errors="coerce")
            real = df[p > 0]
        names[lbl] = set(df["symbol"])
        out.append(f"- Rows: {len(df)}; with real 3-quarter history: {len(real)}")
        pos = real[real[chg] > 0]
        out.append(f"- Of those, rose over 3 quarters: {len(pos)}; "
                   f"median rise {fs(pos[chg].median(), 2)} pp")
        out.append("- Largest 3-quarter rises (real history): "
                   + top_names(real, chg, 15, None))
        if lbl.startswith("DII"):
            one = [c for c in df.columns if "1 qtr" in c and "change" in c]
            if one:
                df[one[0]] = pd.to_numeric(df[one[0]], errors="coerce")
                out.append("- Largest 1-quarter rises: " + top_names(df, one[0], 12))
        out.append("")

    if "FII" in names and "DII (4 straight quarters up)" in names:
        both = sorted(names["FII"] & names["DII (4 straight quarters up)"])
        out.append("- Names on BOTH the FII and DII lists: " + str(len(both))
                   + (". " + ", ".join(both[:40]) if both else ""))
    if "Promoter" in names and "FII" in names:
        both = sorted(names["Promoter"] & names["FII"])
        out.append("- Names on BOTH the Promoter and FII lists: " + str(len(both))
                   + (". " + ", ".join(both[:30]) if both else ""))
    out.append("")
    return "\n".join(out), names


# ---------------------------------------------------------------------------
# Confluence across lists
# ---------------------------------------------------------------------------

def confluence_section(tables, flow_names):
    out = ["## 7. Confluence: names on several lists at once", ""]
    out.append("A name on many independent lists is a stronger fact than a name "
               "on one. Counts below say how many of the listed screens each "
               "name sits on. Flow lists are shown separately.")
    out.append("")
    screens = {
        "Minervini": "Minervini Screener",
        "Darvas": "Darvas Screener",
        "BreakoutV2": "Breakouts v2",
        "PotBreakout": "Potential Breakouts",
        "ModRS": "Modified Relative Strength",
        "52wkHigh": "Stocks at 52 week high",
        "CCI-D100": "CCI Daily crossing 100 (Short to medium term breakout scanner)",
        "CCI-W100": "CCI Weekly crossing 100 (Long term breakout scanner)",
        "Momentum": "Momentum Investing",
        "Ret1M-top30": "Return 1Month",
        "Ret3M-top30": "Return 3Month",
    }
    membership = {}
    for tag, key in screens.items():
        df = tables.get(key)
        if df is None or "symbol" not in df.columns:
            continue
        syms = list(df["symbol"].astype(str))
        if tag.startswith("Ret"):
            d = df.copy()
            d["% change"] = pd.to_numeric(d["% change"], errors="coerce")
            syms = list(d.sort_values("% change", ascending=False)["symbol"].head(30))
        for s in syms:
            membership.setdefault(s, set()).add(tag)

    sector_of = {}
    for key in ("Minervini Screener", "Darvas Screener", "Breakouts v2",
                "Potential Breakouts", "Stocks at 52 week high",
                "CCI Daily crossing 100 (Short to medium term breakout scanner)"):
        df = tables.get(key)
        if df is not None and "sector" in df.columns:
            for _, r in df.iterrows():
                sector_of.setdefault(str(r["symbol"]), str(r["sector"]))

    ranked = sorted(membership.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    rows = []
    for sym, tags in ranked:
        if len(tags) < 3:
            break
        fl = []
        for lbl, short in (("FII", "FII+"), ("DII (4 straight quarters up)", "DII+"),
                           ("Promoter", "Prom+"), ("Retail", "Ret+")):
            if lbl in flow_names and sym in flow_names[lbl]:
                fl.append(short)
        rows.append([sym, sector_of.get(sym, ""), str(len(tags)),
                     ", ".join(sorted(tags)), ", ".join(fl)])
    out.append(f"- Names on 3+ screens: {len(rows)}")
    out.append("")
    if rows:
        out.append(table(["Symbol", "Sector", "Screens", "Which", "Flow"],
                         rows[:40], ["---", "---", "---:", "---", "---"]))
    out.append("")

    # Sector concentration across all momentum screens combined.
    sc = Counter(sector_of[s] for s in membership if s in sector_of)
    tot = sum(sc.values())
    if tot:
        out.append("- Sector share of all names across the momentum screens: "
                   + ", ".join(f"{k} {v} ({100 * v / tot:.0f}%)" for k, v in sc.most_common(8)))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Data quality
# ---------------------------------------------------------------------------

def quality_section(date, tables, missing):
    out = ["## 0. Data check", ""]
    out.append(f"- Trade date folder: {date}")
    out.append(f"- Files present: {len(tables)} of {len(EXPECTED)}")
    if missing:
        out.append("- MISSING: " + "; ".join(missing))
    stamps = set()
    for df in tables.values():
        if "date" in df.columns and len(df):
            stamps.add(str(df["date"].iloc[0])[:10])
    out.append("- Latest date stamps seen across files: " + ", ".join(sorted(stamps)))
    small = [n for n, df in tables.items() if len(df) == 0]
    if small:
        out.append("- Empty files: " + "; ".join(small))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    date = sys.argv[1] if len(sys.argv) > 1 else latest_date()
    if not date:
        print("No csv/<date> folders. Run fetch_chartink.py first.", file=sys.stderr)
        return 2
    tables, missing = load_folder(date)
    if not tables:
        print("No files in csv/" + date, file=sys.stderr)
        return 2

    parts = [
        "# Breadth facts sheet: " + date,
        "",
        "Computed from the 34 Chartink table exports for this trade date. "
        "Numbers only. No conclusion is drawn here.",
        "",
        quality_section(date, tables, missing),
        regime_section(tables),
        indices_section(tables),
        sectors_section(tables),
        screeners_section(tables),
        returns_section(tables),
    ]
    flow_text, flow_names = flow_section(tables)
    parts.append(flow_text)
    parts.append(confluence_section(tables, flow_names))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / (date + ".md")
    text = "\n".join(parts) + "\n"
    path.write_text(text, encoding="utf-8")
    shutil.copyfile(path, OUT_DIR / "latest.md")
    print(f"facts for {date}: {len(tables)} of {len(EXPECTED)} files, "
          f"{len(text.split())} words")
    if missing:
        print("missing: " + "; ".join(missing))
    print("wrote " + str(path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
