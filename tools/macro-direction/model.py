"""Macro direction model: data panel, three rule layers, logistic comparison.

Timing convention (the one rule that keeps the backtest honest)
---------------------------------------------------------------
Every forecast is made at a DECISION point for month t and predicts the
direction of the asset's price from month t to month t+h (h = 1 or 3).

* Basis "avg" (Pink Sheet assets: monthly AVERAGE prices). The decision is
  made when the Pink Sheet for month t is published (first days of t+1).
  Inputs: Pink Sheet through month t, daily series at the end of month t.
  Target: sign(avg(t+h) / avg(t) - 1).
* Basis "end" (Nifty, Brent EIA spot, futures: month-END prices). The
  decision is made at the close of month t. Monthly-published inputs (the
  Pink Sheet copper/gold ratio, FEDFUNDS) enter with a one-month lag, because
  they are not public on that date. Target: sign(end(t+h) / end(t) - 1).

No input ever uses a value dated after the decision point.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

DATA = Path(__file__).resolve().parent / "data"


# ------------------------------------------------------------------ loading
def _read(name: str, col: str | None = None) -> pd.Series | pd.DataFrame | None:
    p = DATA / f"{name}.csv"
    if not p.exists():
        return None
    df = pd.read_csv(p, dtype={"month": str}).set_index("month")
    df.index = pd.PeriodIndex(df.index, freq="M")
    return df[col] if col else df


def load_panel() -> pd.DataFrame:
    """One row per calendar month, raw values as of that month."""
    cols = {}
    pink = _read("pinksheet_monthly_avg")
    for c in pink.columns:
        cols[f"{c}_avg"] = pink[c]
    for code, key in [("DFII10", "real_yield"), ("DTWEXBGS", "dollar"),
                      ("T10YIE", "breakeven"), ("FEDFUNDS", "fedfunds"),
                      ("DEXINUS", "usdinr")]:
        s = _read(f"fred_{code}", "month_end")
        if s is not None:
            cols[key] = s
    s = _read("fred_DEXINUS", "month_avg")
    if s is not None:
        cols["usdinr_avg"] = s
    for name, key in [("eia_brent_spot", "brent_eia_avg"),
                      ("nifty_monthly", "nifty_avg")]:
        s = _read(name, "month_avg")
        if s is not None:
            cols[key] = s
    for name, key in [("eia_brent_spot", "brent_end"),
                      ("nifty_monthly", "nifty_end"),
                      ("yahoo_gold_fut", "gold_fut_end"),
                      ("yahoo_silver_fut", "silver_fut_end"),
                      ("yahoo_brent_fut", "brent_fut_end")]:
        s = _read(name, "month_end")
        if s is not None:
            cols[key] = s
    fpi = _read("nsdl_fpi_equity_monthly")
    if fpi is not None:
        cols["fpi"] = fpi.iloc[:, 0]
    panel = pd.DataFrame(cols).sort_index()
    panel = panel[panel.index >= pd.Period("1990-01", "M")]
    if "usdinr_avg" in panel:
        panel["gold_inr_avg"] = panel["gold_avg"] * panel["usdinr_avg"]
        panel["silver_inr_avg"] = panel["silver_avg"] * panel["usdinr_avg"]
    panel["cu_au"] = panel["copper_avg"] / panel["gold_avg"]
    return panel


# ------------------------------------------------------------------- assets
@dataclass(frozen=True)
class Asset:
    key: str          # short name used in tables
    label: str
    price: str        # panel column
    basis: str        # "avg" or "end"
    regime: str       # row of REGIME_TABLE
    driver: str | None
    core: bool        # one of the six portfolio assets


ASSETS = [
    Asset("gold", "Gold (USD)", "gold_avg", "avg", "gold", "real_yield", True),
    Asset("silver", "Silver (USD)", "silver_avg", "avg", "silver",
          "real_yield", True),
    Asset("aluminium", "Aluminium (USD, LME)", "aluminium_avg", "avg",
          "metal", "metal", True),
    Asset("zinc", "Zinc (USD, LME)", "zinc_avg", "avg", "metal", "metal",
          True),
    Asset("brent", "Brent (USD)", "brent_avg", "avg", "crude", None, True),
    Asset("nifty", "Nifty 50 (INR)", "nifty_end", "end", "equity", "nifty",
          True),
    Asset("gold_inr", "Gold (INR)", "gold_inr_avg", "avg", "gold",
          "real_yield", False),
    Asset("silver_inr", "Silver (INR)", "silver_inr_avg", "avg", "silver",
          "real_yield", False),
]
# Month-end cross-check assets: same rules, tradeable month-end prices.
CHECK_ASSETS = [
    Asset("brent_end", "Brent EIA spot, month-end", "brent_end", "end",
          "crude", None, False),
    Asset("brent_eia_avg", "Brent EIA spot, month-average", "brent_eia_avg",
          "avg", "crude", None, False),
    Asset("nifty_avg", "Nifty 50, month-average", "nifty_avg", "avg",
          "equity", "nifty", False),
    Asset("nifty_nofpi", "Nifty 50, FPI vote off", "nifty_end", "end",
          "equity", "nifty_nofpi", False),
    Asset("gold_end", "Gold futures GC=F, month-end", "gold_fut_end", "end",
          "gold", "real_yield", False),
    Asset("silver_end", "Silver futures SI=F, month-end", "silver_fut_end",
          "end", "silver", "real_yield", False),
]

# Quadrant keys: (growth_rising, inflation_rising)
QUADRANTS = {(True, True): "REFLATION (growth up, inflation up)",
             (True, False): "GOLDILOCKS (growth up, inflation down)",
             (False, True): "STAGFLATION (growth down, inflation up)",
             (False, False): "DEFLATION (growth down, inflation down)"}
QSHORT = {(True, True): "REFL", (True, False): "GOLD", (False, True): "STAG",
          (False, False): "DEFL"}
# Expected direction per quadrant. Order: REFL, GOLDILOCKS, STAG, DEFL.
REGIME_TABLE = {
    # Gold wants rising inflation and falling growth: +1 when both, -1 when
    # neither, 0 when they conflict.
    "gold":   {(True, True): 0, (True, False): -1, (False, True): 1,
               (False, False): 0},
    # Industrial metals follow growth alone.
    "metal":  {(True, True): 1, (True, False): 1, (False, True): -1,
               (False, False): -1},
    # Equities want rising growth and falling inflation.
    "equity": {(True, True): 0, (True, False): 1, (False, True): -1,
               (False, False): 0},
    # Crude follows inflation alone.
    "crude":  {(True, True): 1, (True, False): -1, (False, True): 1,
               (False, False): -1},
    # Silver = sign(gold entry + metal entry): up in reflation, down in
    # deflation, flat where gold and metals disagree.
    "silver": {(True, True): 1, (True, False): 0, (False, True): 0,
               (False, False): -1},
}
REGIME_REASON = {
    "gold": "gold is the hedge for inflation and for weak growth",
    "metal": "industrial metals are priced off factory demand",
    "equity": "equities want growth with falling inflation",
    "crude": "crude prices move with the inflation impulse",
    "silver": "silver is half monetary metal, half industrial metal",
}


def _sgn(x):
    return np.sign(x).fillna(0).astype(int) if isinstance(x, pd.Series) \
        else int(np.sign(x)) if pd.notna(x) else 0


# ----------------------------------------------------------------- features
def inputs(panel: pd.DataFrame, basis: str) -> pd.DataFrame:
    """Macro inputs as known at the decision point for each month t."""
    p = panel
    lag = 1 if basis == "end" else 0          # monthly-published inputs
    f = pd.DataFrame(index=p.index)
    cu_au = p["cu_au"].shift(lag)
    f["cu_au_3m"] = cu_au / cu_au.shift(3) - 1
    f["breakeven_3m"] = p["breakeven"] - p["breakeven"].shift(3) \
        if "breakeven" in p else np.nan
    f["real_yield"] = p.get("real_yield")
    f["real_yield_3m"] = p["real_yield"] - p["real_yield"].shift(3) \
        if "real_yield" in p else np.nan
    f["dollar_3m"] = p["dollar"] / p["dollar"].shift(3) - 1 \
        if "dollar" in p else np.nan
    ff = p["fedfunds"].shift(lag) if "fedfunds" in p else None
    f["fedfunds_6m"] = ff - ff.shift(6) if ff is not None else np.nan
    f["usdinr_3m"] = p["usdinr"] / p["usdinr"].shift(3) - 1
    f["brent_3m"] = p["brent_end"] / p["brent_end"].shift(3) - 1
    f["fpi"] = p["fpi"] if "fpi" in p else np.nan
    # Regime: 3-month change against its own trailing 12-month average.
    g, i = f["cu_au_3m"], f["breakeven_3m"]
    f["growth_up"] = (g > g.rolling(12).mean()).where(
        g.rolling(12).count() == 12)
    f["infl_up"] = (i > i.rolling(12).mean()).where(
        i.rolling(12).count() == 12)
    return f


def votes(panel: pd.DataFrame, asset: Asset,
          feats: pd.DataFrame | None = None) -> pd.DataFrame:
    """Three layer votes, score, call and confidence for one asset."""
    f = inputs(panel, asset.basis) if feats is None else feats
    px = panel[asset.price]
    out = pd.DataFrame(index=panel.index)
    out["px"] = px
    r1 = px / px.shift(1) - 1
    r12 = px / px.shift(12) - 1
    out["r1"], out["r12"] = r1, r12
    # Layer 1, trend: sign(12m) and sign(12m - 1m); both agree -> vote.
    l1 = _sgn(_sgn(r12) + _sgn(r12 - r1))
    out["L1"] = l1.where(r12.notna(), 0)
    out["trend12"] = _sgn(r12)
    # Layer 2, regime.
    ok = f["growth_up"].notna() & f["infl_up"].notna()
    tbl = REGIME_TABLE[asset.regime]
    out["quad"] = [QSHORT[(bool(g), bool(i))] if k else None
                   for g, i, k in zip(f["growth_up"], f["infl_up"], ok)]
    out["L2"] = [tbl[(bool(g), bool(i))] if k else 0
                 for g, i, k in zip(f["growth_up"], f["infl_up"], ok)]
    # Layer 3, driver.
    d = asset.driver
    if d == "real_yield":
        l3 = -_sgn(f["real_yield_3m"])
    elif d == "metal":
        l3 = _sgn(-_sgn(f["dollar_3m"]) + _sgn(f["cu_au_3m"]))
    elif d == "nifty":
        l3 = _sgn(_sgn(f["fpi"]) - _sgn(f["brent_3m"]))
    elif d == "nifty_nofpi":
        l3 = -_sgn(f["brent_3m"])
    else:
        l3 = pd.Series(0, index=panel.index)
    out["L3"] = l3
    out["score"] = out["L1"] + out["L2"] + out["L3"]
    out["call"] = _sgn(out["score"])
    out["conf"] = out["score"].abs()
    for h in (1, 3):
        out[f"fwd{h}"] = px.shift(-h) / px - 1
    return out


# ------------------------------------------------------------ logistic model
LOGIT_FEATURES = ["r12", "r12_minus_r1", "cu_au_3m", "breakeven_3m",
                  "real_yield", "real_yield_3m", "dollar_3m", "fedfunds_6m",
                  "usdinr_3m", "brent_3m", "fpi"]
WINDOW = 120


def logit_walk_forward(v: pd.DataFrame, feats: pd.DataFrame, h: int,
                       exclude_brent: bool = False) -> pd.Series:
    """Out-of-sample P(up) from a 120-month window refit every January.

    A training row (decision month m) is used only when its target is fully
    realised at the refit decision point F, i.e. m + h <= F.
    """
    X = feats.copy()
    X["r12"] = v["r12"]
    X["r12_minus_r1"] = v["r12"] - v["r1"]
    cols = [c for c in LOGIT_FEATURES if not (exclude_brent and c == "brent_3m")]
    X = X[cols].astype(float)
    y = (v[f"fwd{h}"] > 0).astype(float).where(v[f"fwd{h}"].notna())
    prob = pd.Series(np.nan, index=v.index)
    months = v.index
    for F in [m for m in months if m.month == 1]:
        lo = F - WINDOW
        tr = (months >= lo) & (months <= F - h)
        Xt, yt = X[tr], y[tr]
        keep = yt.notna() & v["r12"][tr].notna()
        Xt, yt = Xt[keep], yt[keep]
        if len(yt) < WINDOW - h - 1 or yt.nunique() < 2:
            continue
        use = [c for c in cols if Xt[c].notna().mean() >= 0.5]
        mu, sd = Xt[use].mean(), Xt[use].std().replace(0, 1)
        Z = ((Xt[use] - mu) / sd).fillna(0)
        m = LogisticRegression(max_iter=1000).fit(Z, yt)
        te = (months >= F) & (months < F + 12) & v["r12"].notna().values
        if not te.any():
            continue
        Zte = ((X.loc[te, use] - mu) / sd).fillna(0)
        prob[te] = m.predict_proba(Zte)[:, 1]
    return prob
