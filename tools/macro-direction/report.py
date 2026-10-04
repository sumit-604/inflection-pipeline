"""Tables for BACKTEST_<yyyy-mm>.md. Prose verdicts live in verdicts.md.

The tables are generated; the per-asset paragraphs are written by a person
(or session) after reading the tables, and kept in verdicts.md so a re-run
of backtest.py refreshes the numbers without silently keeping stale prose.
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import pandas as pd

import backtest as B
import model as M

HERE = Path(__file__).resolve().parent


def _sources_table() -> list[str]:
    p = HERE / "data" / "sources.md"
    rows = [l for l in p.read_text().splitlines() if l.startswith("| ")][1:]
    out = ["| Series | Status | First | Last |", "|---|---|---|---|"]
    for r in rows:
        c = [x.strip() for x in r.strip("|").split("|")]
        out.append(f"| {c[0]} ({c[1]}) | {c[2]} | {c[4]} | {c[5]} |")
    return out


def _verdict(key: str) -> list[str]:
    p = HERE / "verdicts.md"
    if not p.exists():
        return ["_Verdict paragraph not written yet (verdicts.md)._"]
    text, out, on = p.read_text().splitlines(), [], False
    for line in text:
        if line.startswith("## "):
            on = line[3:].strip() == key
            continue
        if on:
            out.append(line)
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out or ["_No verdict for this asset._"]


def _crosscheck(panel) -> str:
    x = panel[["brent_avg", "brent_eia_avg"]].dropna()
    x = x[x.index >= pd.Period("2004-01", "M")]
    d = (x["brent_avg"] / x["brent_eia_avg"] - 1).abs()
    ra = x.pct_change().dropna()
    agree = (ra.iloc[:, 0] > 0) == (ra.iloc[:, 1] > 0)
    return (f"{len(x)} months from 2004, median level gap {100 * d.median():.2f}%, "
            f"max {100 * d.max():.2f}% ({d.idxmax()}), monthly direction "
            f"agrees in {100 * agree.mean():.1f}% of months.")


def write(path: Path, panel: pd.DataFrame, results: dict):
    L: list[str] = []
    a = L.append
    first = min(r["v"].index.min() for r in results.values())
    last = max(r["v"]["fwd1"].dropna().index.max() for r in results.values())
    a("# Macro direction model: backtest, October 2026")
    a("")
    a(f"Generated {dt.date.today()} by `python backtest.py`. Decision months "
      f"{first} to {last} (the last month with a known 1-month outcome). "
      "Tables are machine output; the paragraphs under each asset are the "
      "reviewer's reading of them (verdicts.md).")
    a("")
    for l in _verdict("HEADLINE"):
        a(l)
    a("")
    a("## 1. Data")
    a("")
    a("Full detail, URLs and fetch dates: `data/sources.md`. MIRROR means the "
      "primary host refused this cloud shell and a public GitHub copy of the "
      "same upstream file served it. FAILED series vote 0.")
    a("")
    L.extend(_sources_table())
    a("")
    a("## 2. The rules (one line each)")
    a("")
    a("- **Layer 1, trend.** Vote +1 when the 12-month return and the "
      "12-month return minus the 1-month return are both positive, -1 when "
      "both are negative, 0 when they disagree. Layer 1 alone is the "
      "baseline.")
    a("- **Layer 2, regime.** Growth is rising when the 3-month change of "
      "copper/gold is above its own trailing 12-month average; inflation is "
      "rising when the 3-month change of the 10-year breakeven (T10YIE) is "
      "above its trailing 12-month average. The asset votes the table entry "
      "for the quadrant.")
    a("- **Layer 3, driver.** Gold and silver: minus the sign of the 3-month "
      "change in the 10-year real yield. Aluminium and zinc: sign of "
      "(minus sign of the 3-month dollar change, plus sign of the 3-month "
      "copper/gold change). Nifty: sign of (sign of last month's net FPI "
      "equity flow, minus sign of the 3-month Brent change). Brent: none.")
    a("- **Combine.** Score = L1 + L2 + L3. Call = sign of score. "
      "Confidence LOW / MEDIUM / HIGH = |score| 1 / 2 / 3. Score 0 = NO "
      "CALL.")
    a("- **Timing.** Pink Sheet assets are monthly AVERAGE prices: the call "
      "is made when month t is published and predicts avg(t+h) vs avg(t). "
      "Nifty uses month-end closes; monthly-published inputs enter it one "
      "month late. Nothing uses a value dated after the decision.")
    a("")
    a("Regime table (+1 up, -1 down, 0 no view):")
    a("")
    a("| Asset group | Reflation (G up, I up) | Goldilocks (G up, I down) "
      "| Stagflation (G down, I up) | Deflation (G down, I down) | Why |")
    a("|---|---|---|---|---|---|")
    order = [(True, True), (True, False), (False, True), (False, False)]
    for g, tbl in M.REGIME_TABLE.items():
        a(f"| {g} | " + " | ".join(f"{tbl[q]:+d}" for q in order)
          + f" | {M.REGIME_REASON[g]} |")
    a("")
    a("Logistic comparison: L2-regularised logistic regression (scikit-learn "
      "default C=1) on the same inputs (12-month return, 12m minus 1m, "
      "copper/gold 3m, breakeven 3m, real yield level and 3m change, dollar "
      "3m, Fed funds 6m, USD/INR 3m, Brent 3m except for Brent, FPI flow). "
      "Inputs standardised on the training window. 120-month rolling window, "
      "refit each January, training rows only where the target was already "
      "realised at the refit date. One model per asset and horizon.")
    a("")

    a("## 3. Hit rates")
    a("")
    a("Hit rate = share of months with a call where the call matched the sign "
      "of the forward return; (n) = months with a call. Coverage = share of "
      "months the model made any call. Noise band: with 200 calls, one "
      "standard error of a hit rate near 55% is 3.5 points, so a gap under "
      "about 7 points between two rules is not distinguishable from luck. "
      "3-month outcomes overlap month to month, so their effective sample is "
      "about a third of n.")
    for h in (1, 3):
        a("")
        a(f"### {h}-month horizon, full window")
        a("")
        a("| Asset | Model | Coverage | LOW | MEDIUM | HIGH | Trend L1 "
          "(baseline) | 12m sign only | Always up | Model minus trend |")
        a("|---|---|---|---|---|---|---|---|---|---|")
        for k, r in results.items():
            t = B.hit_table(r, h)
            d = t["model"][0] - t["trend"][0]
            a(f"| {r['asset'].label} | {B.fmt_hit(*t['model'])} | "
              f"{B.pct(t['coverage'], 0)} | {B.fmt_hit(*t['conf1'])} | "
              f"{B.fmt_hit(*t['conf2'])} | {B.fmt_hit(*t['conf3'])} | "
              f"{B.fmt_hit(*t['trend'])} | {B.fmt_hit(*t['trend12'])} | "
              f"{B.fmt_hit(*t['up'])} | {100 * d:+.1f} pts |")
        a("")
        a(f"### {h}-month horizon, logistic window (rules vs logistic on the "
          "same months)")
        a("")
        a("| Asset | Logistic starts | Logistic | Rules | Trend L1 | Always up |")
        a("|---|---|---|---|---|---|")
        for k, r in results.items():
            t = B.hit_table(r, h)
            if "logit" not in t:
                continue
            a(f"| {r['asset'].label} | {t['logit_start']} | "
              f"{B.fmt_hit(*t['logit'])} | {B.fmt_hit(*t['model_lw'])} | "
              f"{B.fmt_hit(*t['trend_lw'])} | {B.fmt_hit(*t['up_lw'])} |")
    a("")
    a("### Where all three layers could vote (breakeven data ends 2019-10)")
    a("")
    a("Same tables restricted to months with a regime reading. After "
      "2019-10 the regime layer votes 0 for every asset (input missing), "
      "so this is the only fair test of the full rule set.")
    for h in (1, 3):
        a("")
        a(f"| Asset ({h}m) | Model | LOW | MEDIUM | HIGH | Trend L1 | Always "
          "up | Logistic | Model minus trend |")
        a("|---|---|---|---|---|---|---|---|---|")
        for k, r in results.items():
            t = B.hit_table(r, h, regime_only=True)
            d = t["model"][0] - t["trend"][0]
            a(f"| {r['asset'].label} | {B.fmt_hit(*t['model'])} | "
              f"{B.fmt_hit(*t['conf1'])} | {B.fmt_hit(*t['conf2'])} | "
              f"{B.fmt_hit(*t['conf3'])} | {B.fmt_hit(*t['trend'])} | "
              f"{B.fmt_hit(*t['up'])} | {B.fmt_hit(*t.get('logit', (None, 0)))} "
              f"| {100 * d:+.1f} pts |")
    a("")
    nf = B.evaluate(panel, M.CHECK_ASSETS[3], with_logit=False)
    t1, t3 = B.hit_table(nf, 1), B.hit_table(nf, 3)
    a(f"Nifty with the FPI vote switched off (FPI history before 2020 is "
      f"unverified, see data): 1m {B.fmt_hit(*t1['model'])}, 3m "
      f"{B.fmt_hit(*t3['model'])}.")
    a("")
    a("Calibration reads off the LOW / MEDIUM / HIGH columns: a calibrated "
      "model shows hit rate rising with confidence.")
    a("")

    a("Cross-check, Pink Sheet Brent vs EIA Brent spot (monthly average): "
      + _crosscheck(panel) + " Gold and silver could not be cross-checked: "
      "Yahoo futures (GC=F, SI=F) were refused and no copy was found.")
    a("")
    a("## 4. Averaging check: monthly-average vs month-end prices")
    a("")
    a("Pink Sheet prices are monthly averages. Averaging a random walk "
      "creates positive autocorrelation in its monthly changes, so a trend "
      "rule looks better on averages than on prices anyone can trade. This "
      "table runs the same rules, same months, on both series where a "
      "month-end series exists.")
    a("")
    a("| Asset | Months | Rules on averages | Trend on averages | Rules on "
      "month-end | Trend on month-end |")
    a("|---|---|---|---|---|---|")
    for key, ra, re_ in B.averaging_check(panel):
        if ra is None:
            a(f"| {key} | no month-end series fetched | | | | |")
            continue
        ta, te = B.hit_table(ra, 1), B.hit_table(re_, 1)
        a(f"| {key} | {len(ra['v'])} | {B.fmt_hit(*ta['model'])} | "
          f"{B.fmt_hit(*ta['trend'])} | {B.fmt_hit(*te['model'])} | "
          f"{B.fmt_hit(*te['trend'])} |")
    a("")

    a("## 5. Strategies (monthly rebalance, 1-month returns, no costs)")
    a("")
    a("Long/flat: long when the call is up, flat otherwise. Long/short: long "
      "on up, short on down, flat on NO CALL. Rule calls are the same for "
      "both horizons, so one row covers both; the logistic rows use the "
      "1-month and the 3-month model's call for the next month. Returns on "
      "Pink Sheet assets are average-to-average and NOT tradeable as shown "
      "(see section 4).")
    for k, r in results.items():
        a("")
        a(f"### {r['asset'].label}")
        a("")
        a("| Strategy | Ann. return | Volatility | Max drawdown | Months |")
        a("|---|---|---|---|---|")
        for name, p in B.strategies(r).items():
            a(f"| {name} | {B.pct(p['ann'])} | {B.pct(p['vol'])} | "
              f"{B.pct(p['mdd'])} | {p['n']} |")
        a("")
        a("Worst three 12-month stretches (rules long/short, non-overlapping; "
          "decision months shown; regime mix = months per quadrant):")
        a("")
        a("| Decision months | Long/short | Buy and hold | Hit rate | "
          "Regime mix |")
        a("|---|---|---|---|---|")
        for w in B.worst_stretches(r):
            a(f"| {w['start']} to {w['end']} | {B.pct(w['ret'])} | "
              f"{B.pct(w['bh'])} | {B.pct(w['hit'], 0)} | {w['quads']} |")
        a("")
        for l in _verdict(k):
            a(l)

    a("")
    a("## 6. Cross-asset: top-2 of 6 by score")
    a("")
    pf = B.portfolio(results)
    a(f"Assets: {', '.join(pf['core'])}. Each month, hold the two highest "
      "scores in equal weight (ties broken by 12-month momentum rank); "
      f"compare with equal weight in all six. Months {pf['start']} to "
      f"{pf['end']} ({pf['months']}). Mixed currency (Nifty in INR, the rest "
      "USD) and Pink Sheet average returns: read as a ranking test, not a "
      "tradeable portfolio.")
    a("")
    a("| Portfolio | Ann. return | Volatility | Max drawdown |")
    a("|---|---|---|---|")
    for name, key in [("Top-2 by score", "top"),
                      ("Top-2, only scores > 0 (else cash)", "top_pos"),
                      ("Top-2 by trend L1 alone (baseline ranking)", "trend"),
                      ("Bottom-2 by score (sanity check)", "bottom"),
                      ("Equal weight, all six", "ew")]:
        p = pf[key]
        a(f"| {name} | {B.pct(p['ann'])} | {B.pct(p['vol'])} | "
          f"{B.pct(p['mdd'])} |")
    a("")
    a(f"Top-2 beat equal weight in {B.pct(pf['hit_vs_ew'], 0)} of months. "
      "Times each asset was picked: "
      + ", ".join(f"{k} {v}" for k, v in pf["picks"].items()) + ".")
    a("")
    for l in _verdict("PORTFOLIO"):
        a(l)
    a("")
    a("## 7. What this backtest cannot tell you")
    a("")
    for l in _verdict("LIMITS"):
        a(l)
    path.write_text("\n".join(L) + "\n")
