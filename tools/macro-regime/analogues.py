#!/usr/bin/env python3
"""Historical analogues for the current month.

Two views, both from the data, none from memory:
1. Transitions: every spell of the current regime since 1998, how long it
   ran, and what came next.
2. Nearest neighbours: the past months whose dials and key inputs look most
   like now (Euclidean distance on 16 standardised features), what regime
   followed 6 and 12 months later, and what the six assets did.

Used by run.py to append an "Analogues" section to latest.md.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from model import ASSETS, z

PRICE_COL = {"gold": "gold", "silver": "silver", "aluminium": "aluminium_avg",
             "zinc": "zinc_avg", "brent": "brent", "nifty": "nifty"}


def features(p: pd.DataFrame, d: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "G": d["GROWTH_sm"], "I": d["INFLATION_sm"], "L": d["LIQUIDITY_sm"],
        "S": d["STRESS_sm"], "IN": d["IN_STRESS_sm"],
        "G6": d["GROWTH_sm"].diff(6), "I6": d["INFLATION_sm"].diff(6),
        "L6": d["LIQUIDITY_sm"].diff(6),
        "real yield": z(p["us_real_yield_10y"]),
        "curve": z(p["us_curve_10y2y"]),
        "cu/au 6m": z(np.log(p["cu_au"]).diff(6)),
        "fed funds 6m": z(p["us_fedfunds"].diff(6)),
        "Baa spread": z(p["us_baa_spread"]),
        "USD/INR 6m": z(np.log(p["usdinr"]).diff(6)),
        "Brent 12m": z(np.log(p["brent"]).diff(12)),
        "gold 6m": z(np.log(p["gold_avg"]).diff(6)),
    }).dropna()


def spells(r: pd.DataFrame, regime: str, since: str = "1998-01"):
    q = r["quadrant"].dropna()
    out, start, prev = [], None, None
    for m, v in q.items():
        if v == regime and start is None:
            start = m
        if v != regime and start is not None:
            out.append((start, prev, (prev - start).n + 1, v))
            start = None
        prev = m
    if start is not None:
        out.append((start, prev, (prev - start).n + 1, "ongoing"))
    return [s for s in out if s[1] >= pd.Period(since, "M")]


def nearest(p, d, r, n: int = 8, min_gap: int = 6):
    f = features(p, d)
    now = f.index[-1]
    x = f.loc[now]
    cand = f[f.index <= now - 12]
    dist = np.sqrt(((cand - x) ** 2).mean(axis=1)).sort_values()
    f12 = {a: 100 * (p[PRICE_COL[a]].shift(-12) / p[PRICE_COL[a]] - 1) for a in ASSETS}
    rows, shown = [], []
    for m, dv in dist.items():
        if any(abs((m - s).n) < min_gap for s in shown):
            continue
        shown.append(m)
        rows.append(dict(month=str(m), distance=round(float(dv), 2),
                         regime=r.loc[m, "quadrant"], india=r.loc[m, "in_quadrant"],
                         liquidity=r.loc[m, "liquidity"],
                         stress=r.loc[m, "stress"],
                         plus6=r["quadrant"].get(m + 6, "?"),
                         plus12=r["quadrant"].get(m + 12, "?"),
                         **{a: f12[a].get(m, np.nan) for a in ASSETS}))
        if len(rows) >= n:
            break
    return now, x, rows


def india_section(p, d, r) -> list[str]:
    """India regime spells, and what Nifty did for each global x India pair."""
    now = r.index[-1]
    cur, icur = r.loc[now, "quadrant"], r.loc[now, "in_quadrant"]
    rr = r.rename(columns={"quadrant": "global", "in_quadrant": "quadrant"})
    sp = spells(rr, icur)
    nxt = pd.Series([s[3] for s in sp if s[3] != "ongoing"]).value_counts()
    L = ["", "### India regime analogues", "",
         f"**India {icur} spells since 1998** ({len(sp)}, median length "
         f"{int(np.median([s[2] for s in sp]))} months). What came next: "
         + ", ".join(f"{k} {v}" for k, v in nxt.items()) + ".", "",
         "| Start | End | Months | Next India regime | Global regime at end |",
         "|---|---|---|---|---|"]
    for s in sp:
        L.append(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {r.loc[s[1], 'quadrant']} |")
    f12 = 100 * (p["nifty"].shift(-12) / p["nifty"] - 1)
    x = r[r["in_quadrant"].notna() & r["quadrant"].notna()].copy()
    x["n12"] = f12.reindex(x.index)
    tab = x.groupby(["quadrant", "in_quadrant"])["n12"].agg(["count", "median"])
    L += ["", f"**Nifty 12 months on, by global x India pair** (months since "
          f"{x.index[0]}; the pair now is global {cur} / India {icur}). "
          f"Regimes differ in {100 * x['divergence'].mean():.0f}% of months.", "",
          "| Global | India | Months | Nifty 12m median |", "|---|---|---|---|"]
    for (g, i), w in tab.iterrows():
        mark = " **<- now**" if (g == cur and i == icur) else ""
        med = f"{w['median']:+.1f}%" if pd.notna(w["median"]) else ""
        L.append(f"| {g} | {i} | {int(w['count'])} | {med}{mark} |")
    return L


def section(p, d, r) -> list[str]:
    now = r.index[-1]
    cur = r.loc[now, "quadrant"]
    sp = spells(r, cur)
    nxt = pd.Series([s[3] for s in sp if s[3] != "ongoing"]).value_counts()
    L = ["", f"### Analogues", "",
         f"**{cur} spells since 1998** ({len(sp)}, median length "
         f"{int(np.median([s[2] for s in sp]))} months). What came next: "
         + ", ".join(f"{k} {v}" for k, v in nxt.items()) + ".", "",
         "| Start | End | Months | Next regime |", "|---|---|---|---|"]
    for s in sp:
        L.append(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} |")
    _, x, rows = nearest(p, d, r)
    L += ["", f"**Nearest past months to {now}** on the five dials, their "
          "6-month changes, and eight inputs (real yield, curve, copper/gold, "
          "Fed funds change, Baa spread, USD/INR, Brent 12m, gold 6m). "
          "Distance is root-mean-square in z units; below 1.0 is close.", "",
          "| Month | Dist | Regime then | India then | Liq | Stress | +6m | +12m | "
          + " | ".join(f"{a} 12m" for a in ASSETS) + " |",
          "|---|---|---|---|---|---|---|---|" + "---|" * len(ASSETS)]
    for w in rows:
        L.append(f"| {w['month']} | {w['distance']} | {w['regime']} | {w['india']} | {w['liquidity']} | "
                 f"{w['stress']} | {w['plus6']} | {w['plus12']} | "
                 + " | ".join(f"{w[a]:+.0f}%" if pd.notna(w[a]) else "" for a in ASSETS) + " |")
    L += ["", "Now, same features (z): " + ", ".join(f"{k} {v:+.2f}" for k, v in x.items())]
    L += india_section(p, d, r)
    return L


if __name__ == "__main__":
    from model import run_all
    p, d, r, b = run_all()
    print("\n".join(section(p, d, r)))
