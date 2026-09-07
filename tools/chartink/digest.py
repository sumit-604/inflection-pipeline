#!/usr/bin/env python3
"""Write a dated market-breadth digest from the consolidated CSVs.

This is arithmetic, not judgement. It says where each breadth metric sits
against its own history, what moved, and what crossed a level. It draws no
conclusion about direction and recommends nothing.

A metric with no reading for the latest date is reported as NOT FOUND. Nothing
is carried forward and nothing is estimated.

Output:
    data/chartink/analysis/digest/<date>.md
    data/chartink/analysis/digest/latest.md   (copy of the newest)

Run it after consolidate.py:

    python tools/chartink/digest.py
"""

from __future__ import annotations

import csv
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ANALYSIS = REPO_ROOT / "data" / "chartink" / "analysis"
MASTER = ANALYSIS / "market_breadth_daily.csv"
OUT_DIR = ANALYSIS / "digest"

# The metrics reported at the top, in this order. Anything not listed still
# appears in the full table lower down.
CORE = [
    ("mbm_2_0_magnitude__abv_10ma", "% above 10 EMA"),
    ("mbm_2_0_magnitude__abv_20ma", "% above 20 EMA"),
    ("mbm_2_0_magnitude__abv_50ma", "% above 50 EMA"),
    ("mbm_2_0_magnitude__abv_200ma", "% above 200 EMA"),
    ("mbm_2_0_velocity_basic__net_breadth", "Net breadth (4% adv minus dec)"),
    ("mbm_2_0_velocity_basic__4_advance", "4% advancers"),
    ("mbm_2_0_velocity_basic__4_decline", "4% decliners"),
    ("mbm_2_0_velocity_advanced__net_nh_nl", "Net new highs minus lows"),
    ("mbm_2_0_velocity_advanced__net_15_h_l", "Net within 15% of 52wk H/L"),
    ("mbm_2_0_velocity_basic__volume", "Volume expansion ratio"),
    ("oversold_overbought_rsi__overbought", "Overbought count (weekly RSI>70)"),
    ("oversold_overbought_rsi__oversold", "Oversold count (weekly RSI<30)"),
]

# Everything below this line is written by hand or by the nightly market-read
# task. digest.py regenerates only what sits above it.
MARKER = "\n<!-- market-read -->\n"

# A percentile against two readings says nothing. Below this much history a
# metric still shows its value and changes, but no rank and no extreme flag.
MIN_HISTORY = 20


def as_float(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load():
    if not MASTER.exists():
        print("No market_breadth_daily.csv. Run consolidate.py first.",
              file=sys.stderr)
        sys.exit(2)
    with MASTER.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        cols = list(reader.fieldnames or [])
        rows = [dict(r) for r in reader]
    rows.sort(key=lambda r: r.get("date", ""))
    return cols, rows


def series(rows, col):
    """Dated, non-empty readings for one column, oldest first."""
    return [(r["date"], as_float(r.get(col)))
            for r in rows if as_float(r.get(col)) is not None]


def percentile(values, current):
    """Share of history at or below the current reading, 0 to 100."""
    if not values:
        return None
    below = sum(1 for v in values if v <= current)
    return 100.0 * below / len(values)


def change(hist, back):
    """Change over `back` readings, or None if history is too short."""
    if len(hist) <= back:
        return None
    return hist[-1][1] - hist[-1 - back][1]


def fmt(v, nd=2):
    return "NOT FOUND" if v is None else f"{v:,.{nd}f}"


def fmt_signed(v, nd=2):
    if v is None:
        return "NOT FOUND"
    return f"{v:+,.{nd}f}"


def fmt_pct(s):
    """Percentile cell. 'too short' is a different thing from a missing value."""
    if not s.get("ranked"):
        return f"n={s['n']}"
    return f"{s['pct']:,.0f}"


def describe(rows, col):
    """Everything the digest knows about one column."""
    hist = series(rows, col)
    if not hist:
        return None
    latest_date, latest = hist[-1]
    values = [v for _, v in hist]
    lo, hi = min(values), max(values)
    ranked = len(values) >= MIN_HISTORY and hi > lo
    return {
        "col": col,
        "date": latest_date,
        "value": latest,
        "d1": change(hist, 1),
        "d5": change(hist, 5),
        "d20": change(hist, 20),
        # Rank only where it means something: enough history, and a series that
        # actually varies. A constant column is a chart guide line, not data.
        "pct": percentile(values, latest) if ranked else None,
        "ranked": ranked,
        "constant": hi == lo,
        "n": len(values),
        "min": lo,
        "max": hi,
    }


def main():
    cols, rows = load()
    if not rows:
        print("master file is empty", file=sys.stderr)
        return 2

    as_of = rows[-1]["date"]
    metric_cols = [c for c in cols if c != "date"]

    stats = {}
    guide_lines = []
    for c in metric_cols:
        s = describe(rows, c)
        if not s:
            continue
        if s["constant"] and s["n"] >= MIN_HISTORY:
            # A column that never moves is a reference line drawn on a chart,
            # such as the 50/50 marker. It is not a market metric.
            guide_lines.append(c)
            continue
        stats[c] = s

    # Only metrics that actually reported on the latest date are "today".
    fresh = {c: s for c, s in stats.items() if s["date"] == as_of}
    stale = {c: s for c, s in stats.items() if s["date"] != as_of}

    out = []
    out.append("# Market breadth digest: " + as_of)
    out.append("")
    out.append("Computed from `market_breadth_daily.csv`. Arithmetic only. "
               "No view is expressed and nothing is recommended.")
    out.append("")
    out.append(f"- Metrics reporting on {as_of}: **{len(fresh)}** of {len(metric_cols)}")
    out.append(f"- History available: {rows[0]['date']} to {as_of}, "
               f"{len(rows)} dated rows")
    if stale:
        out.append(f"- Metrics with no reading for {as_of}: {len(stale)} "
                   "(weekly series and slower tiles; see the end)")
    if guide_lines:
        out.append(f"- Chart guide lines excluded: {len(guide_lines)} "
                   "(constant columns such as the 50/50 marker)")
    out.append("")
    out.append("A percentile needs history. Metrics with fewer than "
               f"{MIN_HISTORY} readings show `n=<count>` instead of a rank, "
               "and are never flagged as extreme.")
    out.append("")

    # --- Core table -------------------------------------------------------
    out.append("## Core breadth")
    out.append("")
    out.append("Percentile is this reading's rank against that metric's own "
               "history. 50 means mid-range, 95 means near the top of its range.")
    out.append("")
    out.append("| Metric | Value | 1d | 5d | 20d | Percentile | History |")
    out.append("|---|---:|---:|---:|---:|---:|---:|")
    for col, label in CORE:
        s = fresh.get(col) or stats.get(col)
        if not s:
            out.append(f"| {label} | NOT FOUND | | | | | |")
            continue
        note = "" if s["date"] == as_of else f" (as of {s['date']})"
        out.append(
            f"| {label}{note} | {fmt(s['value'])} | {fmt_signed(s['d1'])} | "
            f"{fmt_signed(s['d5'])} | {fmt_signed(s['d20'])} | "
            f"{fmt_pct(s)} | {s['n']} |"
        )
    out.append("")

    # --- Biggest moves ----------------------------------------------------
    movers = [s for s in fresh.values() if s["d1"] is not None]
    movers.sort(key=lambda s: abs(s["d1"]), reverse=True)
    if movers:
        out.append("## Largest one-day moves")
        out.append("")
        out.append("| Metric | Value | 1d change | Percentile |")
        out.append("|---|---:|---:|---:|")
        for s in movers[:10]:
            out.append(f"| `{s['col']}` | {fmt(s['value'])} | "
                       f"{fmt_signed(s['d1'])} | {fmt_pct(s)} |")
        out.append("")

    # --- Extremes ---------------------------------------------------------
    rankable = [s for s in fresh.values() if s["ranked"] and s["pct"] is not None]
    hot = [s for s in rankable if s["pct"] >= 90]
    cold = [s for s in rankable if s["pct"] <= 10]
    if hot or cold:
        out.append("## At the edge of their own range")
        out.append("")
        if hot:
            out.append("Top decile of history:")
            out.append("")
            for s in sorted(hot, key=lambda x: -x["pct"]):
                out.append(f"- `{s['col']}` at {fmt(s['value'])} "
                           f"(percentile {fmt_pct(s)}, "
                           f"range {fmt(s['min'])} to {fmt(s['max'])})")
            out.append("")
        if cold:
            out.append("Bottom decile of history:")
            out.append("")
            for s in sorted(cold, key=lambda x: x["pct"]):
                out.append(f"- `{s['col']}` at {fmt(s['value'])} "
                           f"(percentile {fmt_pct(s)}, "
                           f"range {fmt(s['min'])} to {fmt(s['max'])})")
            out.append("")

    # --- 50 line crossings ------------------------------------------------
    crossings = []
    for col, s in fresh.items():
        if "abv_" not in col and "above_" not in col and not col.endswith("__pct"):
            continue
        if s["d1"] is None:
            continue
        prev = s["value"] - s["d1"]
        if (prev < 50 <= s["value"]) or (prev >= 50 > s["value"]):
            direction = "up through" if s["value"] >= 50 else "down through"
            crossings.append(f"- `{col}` crossed {direction} 50: "
                             f"{fmt(prev)} to {fmt(s['value'])}")
    if crossings:
        out.append("## Crossed the 50 line today")
        out.append("")
        out.extend(crossings)
        out.append("")

    # --- Full table -------------------------------------------------------
    out.append("## All metrics reporting today")
    out.append("")
    out.append("| Metric | Value | 1d | 5d | 20d | Percentile |")
    out.append("|---|---:|---:|---:|---:|---:|")
    for col in sorted(fresh):
        s = fresh[col]
        out.append(f"| `{col}` | {fmt(s['value'])} | {fmt_signed(s['d1'])} | "
                   f"{fmt_signed(s['d5'])} | {fmt_signed(s['d20'])} | "
                   f"{fmt_pct(s)} |")
    out.append("")

    if stale:
        out.append("## No reading for " + as_of)
        out.append("")
        out.append("These are weekly or slower series. The date shown is their "
                   "last reading.")
        out.append("")
        for col in sorted(stale):
            out.append(f"- `{col}`: last {stale[col]['date']}, "
                       f"{fmt(stale[col]['value'])}")
        out.append("")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / (as_of + ".md")

    # A written market read lives below the marker. Regenerating the computed
    # part must never delete it, so carry any existing read across.
    carried = ""
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if MARKER in old:
            carried = old.split(MARKER, 1)[1]

    text = "\n".join(out) + "\n" + MARKER + carried
    path.write_text(text, encoding="utf-8")
    shutil.copyfile(path, OUT_DIR / "latest.md")

    print("digest for " + as_of + ": " + str(len(fresh)) + " metrics reporting")
    if carried.strip():
        print("carried the existing market read across")
    print("wrote " + str(path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
