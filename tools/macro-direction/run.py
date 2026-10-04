#!/usr/bin/env python3
"""Monthly call. Prints and writes latest.md, formatted as a macro-sheet.md
section (the operator pastes it; this script never edits macro-sheet.md).

Run after `python fetch.py`:   python run.py
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import numpy as np
import pandas as pd

import model as M

HERE = Path(__file__).resolve().parent
CALL = {1: "UP", -1: "DOWN", 0: "NO CALL"}
CONF = {0: "-", 1: "LOW", 2: "MEDIUM", 3: "HIGH"}


def _f(x, d=2, pctg=False):
    if x is None or pd.isna(x):
        return "NOT FOUND"
    return f"{100 * x:+.{d}f}%" if pctg else f"{x:.{d}f}"


def _dir(x):
    return "NOT AVAILABLE" if pd.isna(x) else "RISING" if x else "FALLING"


def _last(s: pd.Series, t):
    s = s.loc[:t].dropna()
    return (s.index[-1], s.iloc[-1]) if len(s) else (None, np.nan)


def reason(a: M.Asset, row, f) -> str:
    bits = []
    bits.append({1: "trend up", -1: "trend down", 0: "trend mixed"}[row.L1])
    q = row.quad or "regime n/a"
    bits.append(f"{q} {'favours' if row.L2 > 0 else 'opposes' if row.L2 < 0 else 'neutral for'} it")
    if a.driver == "real_yield":
        bits.append(f"real yield {_f(f.real_yield_3m)} pts 3m")
    elif a.driver == "metal":
        bits.append(f"dollar {_f(f.dollar_3m, 1, True)} 3m, Cu/Au "
                    f"{_f(f.cu_au_3m, 1, True)} 3m")
    elif a.driver == "nifty":
        fpi = "FPI NOT FOUND" if pd.isna(f.fpi) else f"FPI {f.fpi:+,.0f} cr"
        bits.append(f"{fpi}, Brent {_f(f.brent_3m, 1, True)} 3m")
    else:
        bits.append("no driver vote (v1)")
    return "; ".join(bits)


def flips(a: M.Asset, v: pd.DataFrame, f: pd.DataFrame, panel, t) -> str:
    """What would move the call next month: per-layer triggers."""
    row = v.loc[t]
    px = panel[a.price]
    base12 = px.loc[:t].iloc[-12] if len(px.loc[:t]) >= 12 else np.nan
    trig = []
    # Layer 1: next month's 12m return uses the price 11 months before t.
    if row.L1 != 0:
        side = "below" if row.L1 > 0 else "above"
        what = "month-average price" if a.basis == "avg" else "month-end close"
        trig.append(f"L1 leaves {row.L1:+d} if next month's {what} is "
                    f"{side} {base12:,.1f} (or the 12m-minus-1m sign turns)")
    else:
        trig.append("L1 is 0; it votes when the 12m and 12m-minus-1m signs "
                    "agree")
    # Layer 2: votes available in other quadrants.
    tbl = M.REGIME_TABLE[a.regime]
    alt = sorted({f"{M.QSHORT[q]} {tbl[q]:+d}" for q in tbl
                  if tbl[q] != row.L2})
    trig.append(f"L2 changes in {', '.join(alt)}")
    # Layer 3.
    if a.driver == "real_yield":
        ry = M.inputs(panel, a.basis)["real_yield"]
        ref = ry.loc[:t].iloc[-3] if len(ry.loc[:t].dropna()) >= 3 else np.nan
        trig.append(f"L3 flips if the 10y real yield ends next month on the "
                    f"other side of {_f(ref)}%")
    elif a.driver == "metal":
        trig.append("L3 moves if the dollar or the Cu/Au 3m change reverses")
    elif a.driver == "nifty":
        trig.append("L3 moves on the sign of next month's FPI flow or a "
                    "reversal in the Brent 3m change")
    sc = int(row.score)
    head = (f"score {sc:+d}; a {abs(sc)}-point move toward zero gives NO "
            f"CALL, {abs(sc) + 1} points flips it" if sc else
            "score 0; any one-point move makes a call")
    return head + ". " + "; ".join(trig) + "."


def main():
    panel = M.load_panel()
    t_avg = panel["gold_avg"].dropna().index.max()
    rows, flip_lines = [], []
    regime_f = M.inputs(panel, "avg")
    for a in M.ASSETS:
        if a.price not in panel or panel[a.price].dropna().empty:
            rows.append(f"| {a.label} | NOT FOUND | - | - | - | - | price "
                        "series not fetched |")
            continue
        f = M.inputs(panel, a.basis)
        v = M.votes(panel, a, f)
        t = v["px"].dropna().index.max() if a.basis == "end" else t_avg
        t = min(t, t_avg) if a.basis == "avg" else t
        r = v.loc[t]
        rows.append(f"| {a.label} | {CALL[int(r.call)]} | "
                    f"{CONF[int(r.conf)]} | {int(r.L1):+d} | {int(r.L2):+d} | "
                    f"{int(r.L3):+d} | {reason(a, r, f.loc[t])} |")
        flip_lines.append(f"- **{a.label}** ({t}): {flips(a, v, f, panel, t)}")
    rf = regime_f.loc[t_avg]
    g, i = rf.growth_up, rf.infl_up
    quad = (M.QUADRANTS[(bool(g), bool(i))]
            if pd.notna(g) and pd.notna(i) else "NOT AVAILABLE (input missing)")
    g12 = regime_f["cu_au_3m"].rolling(12).mean().loc[t_avg]
    i12 = regime_f["breakeven_3m"].rolling(12).mean().loc[t_avg]
    L = [f"## CROSS-ASSET DIRECTION ({t_avg.strftime('%B %Y')} data, "
         f"call for {(t_avg + 1).strftime('%B %Y')})", "",
         f"Generated {dt.date.today()} by tools/macro-direction/run.py. "
         "Direction only, not price. Rule model v1; backtest in "
         "tools/macro-direction/BACKTEST_2026-10.md.", "",
         f"**Regime:** {quad}", "",
         "| Input | Value | Reading |", "|---|---|---|",
         f"| Copper/gold 3m change | {_f(rf.cu_au_3m, 1, True)} | vs its 12m "
         f"average {_f(g12, 1, True)}: growth {_dir(g)} |",
         f"| 10y breakeven 3m change | {_f(rf.breakeven_3m)} pts | vs its 12m "
         f"average {_f(i12)} pts: inflation {_dir(i)} |",
         f"| 10y real yield (level, 3m change) | {_f(rf.real_yield)}%, "
         f"{_f(rf.real_yield_3m)} pts | gold/silver driver |",
         f"| Broad dollar 3m change | {_f(rf.dollar_3m, 1, True)} | metals "
         "driver |",
         f"| Fed funds 6m change | {_f(rf.fedfunds_6m)} pts | context only |",
         f"| USD/INR 3m change | {_f(rf.usdinr_3m, 1, True)} | context only |",
         f"| Brent 3m change | {_f(rf.brent_3m, 1, True)} | Nifty driver |",
         f"| Net FPI equity flow (month) | "
         f"{'NOT FOUND' if pd.isna(rf.fpi) else f'{rf.fpi:+,.0f} cr'} | "
         "Nifty driver |", "",
         "| Asset | Call | Confidence | L1 trend | L2 regime | L3 driver | "
         "Reason |", "|---|---|---|---|---|---|---|", *rows, "",
         "**What would flip each call next month**", "", *flip_lines, ""]
    text = "\n".join(L)
    (HERE / "latest.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
