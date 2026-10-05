#!/usr/bin/env python3
"""Write latest.md: the current regime read, formatted to drop into
macro-sheet.md as a section. Does not edit macro-sheet.md.

Run: python run.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from model import (ASSETS, BAND, BASE, BASE_REASON, DIAL_INPUTS, LIQ_SHADE,
                   QIDX, STRESS_SHADE, run_all, z)

HERE = Path(__file__).resolve().parent
DIALS = ["GROWTH", "INFLATION", "LIQUIDITY", "STRESS", "IN_STRESS"]


def _band_reason(a, row):
    q, liq, st, ist = row["quadrant"], row["liquidity"], row["stress"], row["in_stress"]
    parts = [f"{q.lower()} base {BASE[a][QIDX[q]]:+d}"]
    if liq == "EASING" and LIQ_SHADE[a]:
        parts.append("+1 easing")
    if liq == "TIGHT" and LIQ_SHADE[a]:
        parts.append("-1 tight")
    if st == "HIGH":
        parts.append(f"{STRESS_SHADE[a]:+d} stress")
    if a == "nifty" and ist == "HIGH":
        parts.append("-1 India stress")
    return ", ".join(parts)


def main():
    p, d, r, b = run_all()
    m = r.index[-1]
    row = r.loc[m]
    L = [f"## Macro regime read, {m} (tools/macro-regime, 6-12 month horizon)",
         "",
         f"**Regime: {row['quadrant']}** (growth "
         f"{'rising' if d.loc[m, 'GROWTH_sm'] - d.loc[m - 6, 'GROWTH_sm'] > 0 else 'falling'}, "
         f"inflation {'rising' if d.loc[m, 'INFLATION_sm'] - d.loc[m - 6, 'INFLATION_sm'] > 0 else 'falling'}). "
         f"Liquidity {row['liquidity']}. Global stress {row['stress']}. India stress {row['in_stress']}.",
         "",
         "| Dial | Level (z) | 6m change | Inputs voting | Reading |",
         "|---|---|---|---|---|"]
    for k in DIALS:
        lvl, ch, n = d.loc[m, k + "_sm"], d.loc[m, k + "_sm"] - d.loc[m - 6, k + "_sm"], int(d.loc[m, k + "_n"])
        tag = ("high" if lvl > 0.5 else "low" if lvl < -0.5 else "mid") + \
              (", rising" if ch > 0.1 else ", falling" if ch < -0.1 else ", flat")
        L.append(f"| {k} | {lvl:+.2f} | {ch:+.2f} | {n} of {len(DIAL_INPUTS[k])} | {tag} |")
    L += ["", "| Asset | Band | How the band was set |", "|---|---|---|"]
    for a in ASSETS:
        L.append(f"| {a} | {BAND[int(b.loc[m, a])]} | {_band_reason(a, row)} |")
    # inputs behind each dial, latest z
    L += ["", "Inputs, latest z-score (sign already applied):", ""]
    for k in DIALS:
        bits = []
        for lab, fn, sgn in DIAL_INPUTS[k]:
            try:
                v = (sgn * z(fn(p))).loc[m]
            except KeyError:
                v = float("nan")
            bits.append(f"{lab} {v:+.2f}" if pd.notna(v) else f"{lab} n/a")
        L.append(f"- {k}: " + "; ".join(bits))
    # staleness
    L += ["", "Series ending before the read month:", ""]
    src = (HERE / "data" / "sources.md").read_text().splitlines()
    for line in src:
        if line.startswith("| ") and not line.startswith("| File"):
            c = [x.strip() for x in line.strip("|").split("|")]
            if c[5] and c[5] < str(m) and c[2] != "V1 CACHE":
                L.append(f"- {c[0]} ends {c[5]}")
    L += ["", "No direction call is made for any horizon under 6 months. "
          "Bands are exposure tilts conditional on the regime, not forecasts. "
          "Evaluation: EVALUATION_2026-10.md; bar: PASS_BAR.md."]
    text = "\n".join(L) + "\n"
    (HERE / "latest.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
