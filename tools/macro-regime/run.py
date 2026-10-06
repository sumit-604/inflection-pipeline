#!/usr/bin/env python3
"""Write latest.md: the current regime read, formatted to drop into
macro-sheet.md as a section. Does not edit macro-sheet.md.

Run: python run.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from analogues import section as analogue_section
from model import (ASSETS, BAND, BASE, BASE_REASON, BE_BENCH, CPI_BENCH,
                   DIAL_INPUTS, DIALS, IN_CPI_BENCH, IN_CREDIT_BENCH,
                   IN_GVA_BENCH, IN_IIP_BENCH, LIQ_SHADE, QIDX, STRESS_SHADE,
                   india_growth_votes, run_all, yoy, z)

HERE = Path(__file__).resolve().parent
# EVALUATION_2026-10.md: condition (a) of PASS_BAR.md failed, so latest.md
# shows dials and regime only. Set True only after a new bar is written and
# passed. The band code stays in model.py for the next evaluation.
BANDS_ENABLED = False


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


def _vs_norm(v: float) -> str:
    if abs(v) < 0.1:
        return f"on its 5-year norm at z {v:+.2f} (on the line: the call can flip next month)"
    return f"{'above' if v > 0 else 'below'} its 5-year norm at z {v:+.2f}"


def _fmt(x) -> str:
    return "NOT FOUND" if pd.isna(x) else f"{x:.1f}%"


def main():
    p, d, r, b = run_all()
    v = india_growth_votes(p)
    m = r.index[-1]
    row = r.loc[m]
    L = [f"## Macro regime read, {m} (tools/macro-regime, 6-12 month horizon)",
         "",
         f"**Regime: {row['quadrant']}** (growth "
         f"{_vs_norm(d.loc[m, 'GROWTH_sm'])}; "
         f"inflation {'HIGH' if row['quadrant'] in ('REFLATION', 'STAGFLATION') else 'LOW'} against the benchmarks "
         f"CPI {CPI_BENCH}% / breakeven {BE_BENCH}%, US CPI YoY {yoy(p['us_cpi']).ffill(limit=2).loc[m]:.1f}%, "
         f"breakeven {p['us_breakeven_10y'].loc[m]:.2f}%). "
         f"Liquidity {row['liquidity']}. Global stress {row['stress']}. India stress {row['in_stress']}.",
         "",
         f"**India regime: {row['in_quadrant']}** (India growth "
         f"{'HIGH' if row['in_quadrant'] in ('REFLATION', 'GOLDILOCKS') else 'LOW'}: "
         f"{int(v.loc[m, 'votes'])} of {int(v.loc[m, 'available'])} tests pass, "
         f"IIP YoY 3m mean {p['in_iip_yoy'].ffill(limit=2).rolling(3, min_periods=2).mean().loc[m]:.1f}% vs {IN_IIP_BENCH}%, "
         f"services GVA YoY {_fmt(p['in_services_gva_yoy'].loc[m])} vs {IN_GVA_BENCH}%, "
         f"bank credit YoY {_fmt(p['in_bank_credit_yoy'].loc[m])} vs {IN_CREDIT_BENCH}%; "
         f"India CPI YoY {p['in_cpi'].ffill(limit=2).loc[m]:.2f}% against the {IN_CPI_BENCH}% benchmark). "
         + ("**DIVERGENCE**: the India regime differs from the global one. "
            if row["divergence"] else "India and global regimes agree. ")
         + "The India regime governs Nifty and Indian rates; the global regime "
         "governs gold, silver, base metals and Brent.",
         "",
         "| Dial | Level (z) | 6m change | Inputs voting | Reading |",
         "|---|---|---|---|---|"]
    for k in DIALS:
        lvl, ch, n = d.loc[m, k + "_sm"], d.loc[m, k + "_sm"] - d.loc[m - 6, k + "_sm"], int(d.loc[m, k + "_n"])
        tag = ("high" if lvl > 0.5 else "low" if lvl < -0.5 else "mid") + \
              (", rising" if ch > 0.1 else ", falling" if ch < -0.1 else ", flat")
        L.append(f"| {k} | {lvl:+.2f} | {ch:+.2f} | {n} of {len(DIAL_INPUTS[k])} | {tag} |")
    if BANDS_ENABLED:
        L += ["", "| Asset | Band | How the band was set |", "|---|---|---|"]
        for a in ASSETS:
            L.append(f"| {a} | {BAND[int(b.loc[m, a])]} | {_band_reason(a, row)} |")
    else:
        L += ["", "Exposure bands are switched off: the band table failed "
              "condition (a) of PASS_BAR.md (EVALUATION_2026-10.md, section 5). "
              "What each quadrant, liquidity and stress tag has meant for the "
              "six assets over the following 12 months is in that file, "
              "section 4."]
    # inputs behind each dial, latest z
    L += ["", "Inputs, latest z-score (sign already applied; \"carried\" = last published value carried forward, up to 2 months):", ""]
    for k in DIALS:
        bits = []
        for lab, fn, sgn in DIAL_INPUTS[k]:
            try:
                zz = sgn * z(fn(p))
                v, raw = zz.ffill(limit=2).loc[m], zz.loc[m]
            except KeyError:
                v = raw = float("nan")
            carried = " (carried)" if pd.notna(v) and pd.isna(raw) else ""
            bits.append(f"{lab} {v:+.2f}{carried}" if pd.notna(v) else f"{lab} n/a")
        L.append(f"- {k}: " + "; ".join(bits))
    L += analogue_section(p, d, r)
    # staleness
    L += ["", "Series ending before the read month:", ""]
    src = (HERE / "data" / "sources.md").read_text().splitlines()
    for line in src:
        if line.startswith("| ") and not line.startswith("| File"):
            c = [x.strip() for x in line.strip("|").split("|")]
            if c[5] and c[5] < str(m) and c[2] != "V1 CACHE":
                L.append(f"- {c[0]} ends {c[5]}")
    L += ["", "No direction call is made for any horizon. This is a regime "
          "read, not a forecast. Evaluation: EVALUATION_2026-10.md; bar: "
          "PASS_BAR.md; reading: VERDICT_2026-10.md."]
    text = "\n".join(L) + "\n"
    (HERE / "latest.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
