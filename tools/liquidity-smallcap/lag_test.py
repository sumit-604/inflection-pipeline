#!/usr/bin/env python3
"""Lead-lag test: monthly change in each money measure vs Smallcap 250 return.

Monthly rules (fixed before any result was seen):
  net LAF   monthly MEAN of daily values (Rs crore); change = difference of means.
            Daily LAF swings with tax dates and month-end flows, so the mean
            is the level. A month with fewer than 10 daily values is blank.
  3M CD     monthly MEAN (%); change = difference in percentage points.
  MTF book  month-end level, NSE + BSE; change = % change. NSE alone is a
            cross-check. indiamtf's API note says BSE starts about
            2025-10-15, but its own file has daily BSE values from
            2017-07-03 with no jump in 2025, so no break is applied.
  SC250     month-end close; return = % change.
  A month counts only if its last observation falls on or after the 20th
  (drops the running month).

Correlation at lag k pairs the money change in month t with the Smallcap 250
return in month t+k, k = 0..3. Lag 0 is coincident, not a lead.
Expected sign if money leads: LAF +, CD rate -, MTF +.
Also reported: Spearman rank correlation, n, and the rough 95% bar 2/sqrt(n).

Failure periods: a rolling 12-month correlation at each measure's best lag.
Months where it runs against the expected sign are the periods the link failed.

Run: python lag_test.py   (reads data/panel_daily.csv; writes out/)
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = Path(os.environ.get("LSC_DATA", HERE / "data"))
OUT = Path(os.environ.get("LSC_OUT", HERE / "out"))
LAGS = [0, 1, 2, 3]
MEASURES = {   # name: (column, expected sign, label)
    "net_laf": ("d_laf", +1, "Net LAF, change in monthly mean (Rs cr)"),
    "cd_3m": ("d_cd", -1, "3M CD rate, change in monthly mean (pp)"),
    "mtf_combined": ("d_mtf_comb", +1, "MTF book NSE+BSE, month-end % change"),
    "mtf_nse": ("d_mtf_nse", +1, "MTF book NSE only (cross-check), % change"),
}


def monthly(p: pd.DataFrame) -> pd.DataFrame:
    p = p.apply(pd.to_numeric, errors="coerce")
    g = p.groupby(p.index.to_period("M"))
    last_day = pd.Series(p.index, index=p.index).groupby(p.index.to_period("M")).max()
    m = pd.DataFrame(index=g.size().index)
    laf_n = g["net_laf_cr"].count()
    m["laf_mean"] = g["net_laf_cr"].mean().where(laf_n >= 10)
    m["cd_mean"] = g["cd_3m_pct"].mean().where(g["cd_3m_pct"].count() >= 10)
    m["mtf_nse"] = g["mtf_nse_cr"].last()
    m["mtf_comb"] = g["mtf_combined_cr"].last()
    m["sc250"] = g["nifty_smallcap_250"].last()
    m = m[last_day.dt.day >= 20]
    # full month grid first, so a change never spans a missing month
    m = m.reindex(pd.period_range(m.index.min(), m.index.max(), freq="M"))
    m["d_laf"] = m["laf_mean"].diff()
    m["d_cd"] = m["cd_mean"].diff()
    m["d_mtf_nse"] = m["mtf_nse"].pct_change(fill_method=None) * 100
    m["d_mtf_comb"] = m["mtf_comb"].pct_change(fill_method=None) * 100
    m["ret_sc250"] = m["sc250"].pct_change(fill_method=None) * 100
    return m


def corr_table(m: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for name, (col, sign, label) in MEASURES.items():
        for k in LAGS:
            x, y = m[col], m["ret_sc250"].shift(-k)
            ok = x.notna() & y.notna()
            n = int(ok.sum())
            r = x[ok].corr(y[ok]) if n >= 6 else np.nan
            rho = x[ok].rank().corr(y[ok].rank()) if n >= 6 else np.nan   # Spearman
            bar = 2 / np.sqrt(n) if n else np.nan
            rows.append(dict(measure=name, label=label, lag=k, n=n,
                             pearson=r, spearman=rho, bar95=bar,
                             expected=sign,
                             right_sign=bool(np.sign(r) == sign) if pd.notna(r) else None,
                             clears_bar=bool(abs(r) > bar) if pd.notna(r) else None))
    return pd.DataFrame(rows)


def best_leads(t: pd.DataFrame) -> pd.DataFrame:
    lead = t[(t["lag"] >= 1) & t["pearson"].notna()].copy()
    lead["signed"] = lead["pearson"] * lead["expected"]
    return lead.sort_values("signed", ascending=False).groupby("measure").head(1)


def failures(m: pd.DataFrame, best: pd.DataFrame, window: int = 12) -> dict:
    out = {}
    for _, b in best.iterrows():
        col, sign, _ = MEASURES[b["measure"]]
        x, y = m[col], m["ret_sc250"].shift(-int(b["lag"]))
        rc = x.rolling(window, min_periods=window - 2).corr(y)
        bad = (rc * sign) < 0
        runs, start, prev = [], None, None
        for per, v in bad.items():
            if v and start is None:
                start = per
            if not v and start is not None:
                runs.append((start, prev))
                start = None
            prev = per
        if start is not None:
            runs.append((start, prev))
        out[b["measure"]] = dict(
            lag=int(b["lag"]), window=window,
            runs=[f"{a} to {z}" if a != z else str(a) for a, z in runs],
            rolling={str(k): (None if pd.isna(v) else round(float(v), 3))
                     for k, v in rc.items()})
    return out


def extras(m: pd.DataFrame) -> dict:
    """Checks added after the first run (2026-11-17), stated as such:
    reverse lags (does the index move first?), lag-0 rolling 12-month
    correlation (the only lag with a link), and SC250 returns by LAF regime."""
    y = m["ret_sc250"]
    rev = {name: {k: round(float(m[col].corr(y.shift(k))), 3) for k in (1, 2, 3)}
           for name, (col, _, _) in MEASURES.items()}
    roll = {}
    for name, (col, sign, _) in MEASURES.items():
        rc = m[col].rolling(12, min_periods=10).corr(y)
        roll[name] = {"min": round(float(rc.min()), 3), "min_window_end": str(rc.idxmin()),
                      "max": round(float(rc.max()), 3), "max_window_end": str(rc.idxmax()),
                      "wrong_sign_window_ends": [str(p) for p in rc.index[(rc * sign) < 0]]}
    reg = m.assign(regime=np.where(m["laf_mean"] < 0, "deficit", "surplus"))
    reg = reg.dropna(subset=["ret_sc250", "laf_mean"])
    by = reg.groupby("regime")["ret_sc250"].agg(["count", "mean", "median"]).round(2)
    months = {str(p): round(float(r), 2) for p, r in
              reg.loc[reg["regime"] == "deficit", "ret_sc250"].items()}
    return {"reverse_lag_r": rev, "rolling12_lag0": roll,
            "sc250_by_laf_regime": by.to_dict("index"), "deficit_month_returns": months}


def fmt(t: pd.DataFrame) -> str:
    L = ["| Measure | Lag 0 | Lag 1 | Lag 2 | Lag 3 | n (lag 0) | 95% bar | Expected sign |",
         "|---|---|---|---|---|---|---|---|"]
    for name, g in t.groupby("measure", sort=False):
        g = g.set_index("lag")
        cells = []
        for k in LAGS:
            r = g.loc[k, "pearson"]
            if pd.isna(r):
                cells.append("n/a")
                continue
            mark = "*" if g.loc[k, "clears_bar"] else ""
            cells.append(f"{r:+.2f}{mark} (rho {g.loc[k, 'spearman']:+.2f})")
        sign = "+" if g.loc[0, "expected"] > 0 else "-"
        L.append(f"| {g.loc[0, 'label']} | " + " | ".join(cells) +
                 f" | {g.loc[0, 'n']} | {g.loc[0, 'bar95']:.2f} | {sign} |")
    L += ["", "Pearson r, Spearman rho in brackets. * = |r| above 2/sqrt(n), a rough "
          "95% bar. Lag k pairs the money change in month t with the Smallcap 250 "
          "return in month t+k."]
    return "\n".join(L)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    p = pd.read_csv(DATA / "panel_daily.csv", parse_dates=["date"]).set_index("date")
    m = monthly(p)
    m.to_csv(OUT / "monthly.csv")
    t = corr_table(m)
    t.to_csv(OUT / "lag_table.csv", index=False, float_format="%.4f")
    md = fmt(t)
    (OUT / "lag_table.md").write_text(md + "\n")
    best = best_leads(t)
    fail = failures(m, best)
    span = m.dropna(subset=["ret_sc250"]).index
    res = dict(months=f"{span.min()} to {span.max()}" if len(span) else "none",
               table=t.replace({np.nan: None}).to_dict("records"),
               best=best.replace({np.nan: None}).to_dict("records"),
               failures=fail, extras=extras(m))
    (OUT / "results.json").write_text(json.dumps(res, indent=2, default=str) + "\n")
    print(md)
    print()
    ex = res["extras"]
    print("Reverse lags (SC250 return month t-k vs money change month t):")
    for k, v in ex["reverse_lag_r"].items():
        print(f"  {k}: " + ", ".join(f"k={a} {b:+.2f}" for a, b in v.items()))
    print("Lag-0 rolling 12m r:")
    for k, v in ex["rolling12_lag0"].items():
        print(f"  {k}: {v['min']:+.2f} (window to {v['min_window_end']}) .. "
              f"{v['max']:+.2f} (to {v['max_window_end']}); wrong sign: "
              f"{', '.join(v['wrong_sign_window_ends']) or 'none'}")
    print("SC250 monthly return by net LAF regime:", ex["sc250_by_laf_regime"])
    print()
    for _, b in best.iterrows():
        f = fail[b["measure"]]
        print(f"{b['measure']}: best lead lag {int(b['lag'])}, r {b['pearson']:+.2f}; "
              f"link failed: {', '.join(f['runs']) or 'no run'}")


if __name__ == "__main__":
    main()
