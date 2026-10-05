#!/usr/bin/env python3
"""Episode evaluation against PASS_BAR.md. Writes EVALUATION_2026-10.md.

Run: python evaluate.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from model import ASSETS, BAND, run_all

HERE = Path(__file__).resolve().parent
EVAL_START = pd.Period("2004-01", "M")
EPISODES = ["2007-06", "2008-06", "2009-03", "2011-04", "2013-05", "2014-06",
            "2016-02", "2018-09", "2020-02", "2020-04", "2021-06", "2022-03",
            "2022-10", "2024-09"]
PRICE_COL = {"gold": "gold", "silver": "silver", "aluminium": "aluminium_avg",
             "zinc": "zinc_avg", "brent": "brent", "nifty": "nifty"}


def fwd(p: pd.DataFrame, a: str, n: int) -> pd.Series:
    s = p[PRICE_COL[a]]
    return 100 * (s.shift(-n) / s - 1)


def trend_band(p: pd.DataFrame, a: str) -> pd.Series:
    s = p[PRICE_COL[a]]
    return np.sign(s / s.shift(12) - 1).replace(0, 1)


def agree(band: float, ret: float) -> float:
    """1 if the band points with the return, 0 against, 0.5 for NEUTRAL."""
    if pd.isna(band) or pd.isna(ret):
        return np.nan
    if band == 0:
        return 0.5
    return 1.0 if np.sign(ret) == band else 0.0


def main():
    p, d, r, b = run_all()
    f6 = {a: fwd(p, a, 6) for a in ASSETS}
    f12 = {a: fwd(p, a, 12) for a in ASSETS}
    tb = {a: trend_band(p, a) for a in ASSETS}
    L = ["# Evaluation, macro regime model v2 (2026-10)", "",
         "Judged against PASS_BAR.md, committed before this file existed "
         "(0ca0acc). Data: data/sources.md. Rules: `python -c \"import model; "
         "print(*model.rules(), sep=chr(10))\"`.", ""]

    # ------------------------------------------------------- episodes
    L += ["## 1. Episodes", "",
          "Regime read as of the month-end, bands, and what each asset did "
          "over the next 6 and 12 months (%). Trend = 12-month sign at the "
          "same date, the baseline for condition (c).", ""]
    hdr = "| Month | Regime | Liq | Stress | IN | " + " | ".join(
        f"{a} band / 6m / 12m / trend" for a in ASSETS) + " |"
    L += [hdr, "|" + "---|" * (5 + len(ASSETS))]
    score_model = {a: [] for a in ASSETS}
    score_trend = {a: [] for a in ASSETS}
    for m in EPISODES + [str(r.index[-1])]:
        pm = pd.Period(m, "M")
        row = r.loc[pm]
        cells = []
        for a in ASSETS:
            bd, r6, r12, t = b.loc[pm, a], f6[a].get(pm), f12[a].get(pm), tb[a].get(pm)
            cells.append(f"{BAND.get(bd, '-')[:2]} / "
                         f"{'' if pd.isna(r6) else f'{r6:+.0f}'} / "
                         f"{'' if pd.isna(r12) else f'{r12:+.0f}'} / "
                         f"{'' if pd.isna(t) else ('up' if t > 0 else 'dn')}")
            if m in EPISODES:
                score_model[a].append(agree(bd, r12))
                score_trend[a].append(agree(t, r12))
        L.append(f"| {m} | {row['quadrant']} | {row['liquidity']} | "
                 f"{row['stress']} | {row['in_stress']} | " + " | ".join(cells) + " |")
    L += ["", "OV = OVERWEIGHT, NE = NEUTRAL, UN = UNDERWEIGHT. The last row is "
          "the current read and is not scored.", ""]

    # condition (a)
    ga, na = np.nansum(score_model["gold"]), np.nansum(score_model["nifty"])
    gt, nt = np.nansum(score_trend["gold"]), np.nansum(score_trend["nifty"])
    n_ep = len(EPISODES)
    L += ["### Condition (a): gold and Nifty bands vs the next 12 months", "",
          "| | Gold agrees | Nifty agrees | Both needed: 10 of 14 |", "|---|---|---|---|",
          f"| Model bands | {ga:.1f} / {n_ep} | {na:.1f} / {n_ep} | "
          f"{'PASS' if ga >= 10 and na >= 10 else 'FAIL'} |",
          f"| Trend (12m sign) | {gt:.1f} / {n_ep} | {nt:.1f} / {n_ep} | "
          f"{'PASS' if gt >= 10 and nt >= 10 else 'FAIL'} |", ""]
    per_asset = ["| Asset | Model agrees / 14 | Trend agrees / 14 |", "|---|---|---|"]
    for a in ASSETS:
        per_asset.append(f"| {a} | {np.nansum(score_model[a]):.1f} | "
                         f"{np.nansum(score_trend[a]):.1f} |")
    L += ["All six assets, same scoring:", ""] + per_asset + [""]
    a_pass = ga >= 10 and na >= 10

    # ------------------------------------------------------- buckets (b)
    L += ["## 2. Buckets, all months 2004-01 onward", "",
          "Median forward return by band, with the number of months in each "
          "bucket. Overlapping windows: the effective sample is about n/12 "
          "for 12-month returns.", ""]
    mask = (b.index >= EVAL_START)
    L += ["| Asset | Horizon | OVERWEIGHT median (n) | NEUTRAL median (n) | "
          "UNDERWEIGHT median (n) | OW minus UW | Trend up median (n) | "
          "Trend down median (n) | Trend spread |", "|---|---|---|---|---|---|---|---|---|"]
    b_wins, t_wins = 0, 0
    for a in ASSETS:
        for h, fr in [(6, f6[a]), (12, f12[a])]:
            fr = fr[mask & fr.notna()]
            bd = b.loc[fr.index, a]
            med = {k: (fr[bd == k].median(), int((bd == k).sum())) for k in [1, 0, -1]}
            t = tb[a].loc[fr.index]
            tm = {k: (fr[t == k].median(), int((t == k).sum())) for k in [1, -1]}
            spread = med[1][0] - med[-1][0]
            tspread = tm[1][0] - tm[-1][0]
            if h == 12:
                b_wins += int(spread > 0)
                t_wins += int(tspread > 0)
            L.append(f"| {a} | {h}m | {med[1][0]:+.1f} ({med[1][1]}) | "
                     f"{med[0][0]:+.1f} ({med[0][1]}) | {med[-1][0]:+.1f} ({med[-1][1]}) | "
                     f"{spread:+.1f} | {tm[1][0]:+.1f} ({tm[1][1]}) | "
                     f"{tm[-1][0]:+.1f} ({tm[-1][1]}) | {tspread:+.1f} |")
    b_pass = b_wins >= 4
    L += ["", f"### Condition (b): OVERWEIGHT median beats UNDERWEIGHT at 12 "
          f"months on {b_wins} of 6 assets: {'PASS' if b_pass else 'FAIL'}. "
          f"Trend does so on {t_wins} of 6.", ""]

    # ------------------------------------------------------- (c)
    c_pass = (ga + na > gt + nt) or (b_wins > t_wins)
    c_pass = c_pass and not ((ga + na < gt + nt) and (b_wins < t_wins))
    L += ["### Condition (c): does the model beat the trend sign?", "",
          f"Episodes, gold + Nifty agreement: model {ga + na:.1f}, trend {gt + nt:.1f}. "
          f"Buckets, assets with positive 12m spread: model {b_wins}, trend {t_wins}. "
          f"{'PASS' if c_pass else 'FAIL'}: the model "
          f"{'does' if c_pass else 'does not'} beat the trend sign on at least one "
          "of the two counts without losing on the other.", ""]

    # ------------------------------------------------------- lead times
    L += ["## 3. Lead time of the stress and liquidity dials", "",
          "First month in the 12 before the episode in which STRESS read HIGH "
          "or LIQUIDITY read TIGHT.", "",
          "| Episode | First STRESS HIGH | First LIQUIDITY TIGHT | Read at the episode |",
          "|---|---|---|---|"]
    for m in ["2008-06", "2020-02", "2022-03"]:
        pm = pd.Period(m, "M")
        win = r.loc[pm - 12:pm]
        fs = win.index[win["stress"] == "HIGH"]
        fl = win.index[win["liquidity"] == "TIGHT"]
        L.append(f"| {m} | {fs[0] if len(fs) else 'none'} | "
                 f"{fl[0] if len(fl) else 'none'} | "
                 f"{r.loc[pm, 'quadrant']}, {r.loc[pm, 'liquidity']}, {r.loc[pm, 'stress']} |")
    L += [""]

    # ------------------------------------------------------- regime table
    L += ["## 4. Regime history, months per quadrant and forward returns", ""]
    rr = r[mask].copy()
    L += ["| Quadrant | Months | " + " | ".join(f"{a} 12m median" for a in ASSETS) + " |",
          "|---|---|" + "---|" * len(ASSETS)]
    for q in ["REFLATION", "GOLDILOCKS", "STAGFLATION", "DEFLATION"]:
        idx = rr.index[rr["quadrant"] == q]
        L.append(f"| {q} | {len(idx)} | " + " | ".join(
            f"{f12[a].reindex(idx).median():+.1f}" for a in ASSETS) + " |")
    L += ["", "By liquidity tag:", "",
          "| Liquidity | Months | " + " | ".join(f"{a} 12m median" for a in ASSETS) + " |",
          "|---|---|" + "---|" * len(ASSETS)]
    for q in ["EASING", "NEUTRAL", "TIGHT"]:
        idx = rr.index[rr["liquidity"] == q]
        L.append(f"| {q} | {len(idx)} | " + " | ".join(
            f"{f12[a].reindex(idx).median():+.1f}" for a in ASSETS) + " |")
    L += ["", "By stress tag:", "",
          "| Stress | Months | " + " | ".join(f"{a} 12m median" for a in ASSETS) + " |",
          "|---|---|" + "---|" * len(ASSETS)]
    for q in ["LOW", "NORMAL", "HIGH"]:
        idx = rr.index[rr["stress"] == q]
        L.append(f"| {q} | {len(idx)} | " + " | ".join(
            f"{f12[a].reindex(idx).median():+.1f}" for a in ASSETS) + " |")

    # ------------------------------------------------------- verdict
    L += ["", "## 5. Verdict against PASS_BAR.md", "",
          f"- (a) episodes: {'PASS' if a_pass else 'FAIL'} (gold {ga:.1f}, Nifty {na:.1f}; need 10 each)",
          f"- (b) buckets: {'PASS' if b_pass else 'FAIL'} ({b_wins} of 6; need 4)",
          f"- (c) vs trend: {'PASS' if c_pass else 'FAIL'}", ""]
    if a_pass and b_pass and c_pass:
        L.append("**All three pass. Keep the bands; latest.md becomes a monthly "
                 "section in macro-sheet.md.**")
    elif a_pass and b_pass:
        L.append("**(a) and (b) pass, (c) fails: keep the dashboard, drop the "
                 "bands; the 12-month trend sign is enough.**")
    else:
        L.append("**(a) or (b) fails: the tool is a dashboard. latest.md shows "
                 "dials and regime, no exposure bands.**")
    (HERE / "EVALUATION_2026-10.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
