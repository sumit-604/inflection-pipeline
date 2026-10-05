#!/usr/bin/env python3
"""Macro regime model, 6 to 12 month horizon.

Reads the monthly series under data/, builds four dials (GROWTH, INFLATION,
LIQUIDITY, STRESS) plus an India stress dial, names the regime, and sets an
exposure band per asset. No learned parameters. Every rule is one line and
is printed by rules().

Horizon: the dials are built from 6- and 12-month changes and 5-year
z-scores; nothing here is meant to say anything about next month.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
ZWIN = 60            # months in the trailing z-score window
ZMIN = 36            # minimum months before a z-score is used
START = "1995-01"    # panel start; evaluation starts 2004-01


# --------------------------------------------------------------- loading
def _s(name: str, col: str = "value") -> pd.Series | None:
    p = DATA / f"{name}.csv"
    if not p.exists():
        return None
    df = pd.read_csv(p, dtype={"month": str}).set_index("month")
    s = pd.to_numeric(df[col], errors="coerce")
    s.index = pd.PeriodIndex(s.index, freq="M")
    return s


def load_panel() -> pd.DataFrame:
    """One row per month: raw inputs and asset prices, as of month-end."""
    c = {}
    # prices (month-end unless noted)
    c["gold"] = _s("gold_usd")
    c["silver"] = _s("silver_usd")
    c["copper"] = _s("copper_usd")
    pink = pd.read_csv(DATA / "pinksheet_monthly_avg.csv",
                       dtype={"month": str}).set_index("month")
    pink.index = pd.PeriodIndex(pink.index, freq="M")
    c["aluminium_avg"] = pink["aluminium"]          # monthly average
    c["zinc_avg"] = pink["zinc"]                    # monthly average
    c["copper_avg"] = pink["copper"]
    c["gold_avg"] = pink["gold"]
    c["brent"] = _s("brent_spot_eia")
    c["nifty"] = _s("nifty_long")
    c["usdinr"] = _s("usdinr")
    c["dxy"] = _s("dxy")
    c["usd_broad"] = _s("usd_broad")
    c["shanghai"] = _s("shanghai")
    # macro
    for k in ["us_real_yield_10y", "us_breakeven_10y", "us_curve_10y2y",
              "us_nominal_10y", "us_fedfunds", "us_cpi", "us_core_cpi",
              "us_m2", "us_fed_assets", "us_nfci", "us_baa_spread",
              "us_stlfsi", "us_vix", "us_indpro", "us_recession_prob",
              "epu_us", "epu_india", "epu_global", "in_call_rate",
              "in_gsec_10y", "in_cpi_yoy", "in_m3", "in_cli", "india_vix",
              "us_crude_stocks_ex_spr", "in_iip_yoy", "in_cpi_yoy_mospi"]:
        c[k] = _s(k)
    # quarterly series, placed when they become known: GVA two months after
    # the quarter ends (release lag), bank credit one month after; each then
    # holds for the quarter (ffill 3 months).
    gva = _s("in_gva_yoy_q")
    if gva is not None:
        gva.index = gva.index + 2
        c["in_services_gva_yoy"] = gva
        mf = _s("in_gva_yoy_q", "manufacturing_yoy"); mf.index = mf.index + 2
        c["in_mfg_gva_yoy"] = mf
    cr = _s("in_bank_credit_yoy_q")
    if cr is not None:
        cr.index = cr.index + 1
        c["in_bank_credit_yoy"] = cr
    # India CPI YoY: MoSPI (issuing body) from 2014-01, FRED OECD before.
    # The two differ by up to 5.6 points on the overlap; MoSPI wins there.
    if c.get("in_cpi_yoy_mospi") is not None and c.get("in_cpi_yoy") is not None:
        fred_pre = c["in_cpi_yoy"][c["in_cpi_yoy"].index < pd.Period("2014-01", "M")]
        c["in_cpi"] = c["in_cpi_yoy_mospi"].combine_first(fred_pre)
    fpi = pd.read_csv(DATA / "in_fpi_flows.csv", dtype={"month": str}) \
        .set_index("month")
    fpi.index = pd.PeriodIndex(fpi.index, freq="M")
    c["fpi_equity"] = fpi["value"]
    c["fpi_total"] = fpi["fpi_total_net_inr_cr"]
    for k in ["gold", "silver", "wti", "copper"]:
        c[f"cot_{k}"] = _s(f"cot_{k}_net_pct_oi")
    panel = pd.DataFrame({k: v for k, v in c.items() if v is not None})
    panel = panel.sort_index()
    panel = panel[panel.index >= pd.Period(START, "M")]
    for k in ["in_services_gva_yoy", "in_mfg_gva_yoy", "in_bank_credit_yoy"]:
        if k in panel:
            panel[k] = panel[k].ffill(limit=3)
    # the dollar: broad index from 2006, DXY before (spliced on log change)
    d = np.log(panel["usd_broad"]).diff()
    d = d.fillna(np.log(panel["dxy"]).diff())
    panel["dollar"] = d.cumsum()
    panel["cu_au"] = panel["copper_avg"] / panel["gold_avg"]
    return panel


# ------------------------------------------------------------ transforms
def chg(s: pd.Series, n: int) -> pd.Series:
    return s - s.shift(n)


def logchg(s: pd.Series, n: int) -> pd.Series:
    return np.log(s) - np.log(s.shift(n))


def yoy(s: pd.Series) -> pd.Series:
    return 100 * (s / s.shift(12) - 1)


def z(s: pd.Series) -> pd.Series:
    """Trailing 5-year z-score, so 'high' means high against recent history."""
    m = s.rolling(ZWIN, min_periods=ZMIN).mean()
    sd = s.rolling(ZWIN, min_periods=ZMIN).std()
    out = (s - m) / sd
    return out.clip(-3, 3)


# ------------------------------------------------------------------ dials
DIAL_INPUTS = {
    "GROWTH": [
        ("cu_au 6m log change", lambda p: logchg(p["cu_au"], 6), +1),
        ("copper 6m log change", lambda p: logchg(p["copper_avg"], 6), +1),
        ("US industrial production YoY", lambda p: yoy(p["us_indpro"]), +1),
        ("US recession probability (inverted)",
         lambda p: p["us_recession_prob"], -1),
        ("US 10y-2y curve level", lambda p: p["us_curve_10y2y"], +1),
        ("Shanghai 6m log change", lambda p: logchg(p["shanghai"], 6), +1),
    ],
    "INFLATION": [
        ("US breakeven level", lambda p: p["us_breakeven_10y"], +1),
        ("US breakeven 6m change", lambda p: chg(p["us_breakeven_10y"], 6), +1),
        ("US CPI YoY", lambda p: yoy(p["us_cpi"]), +1),
        ("US core CPI YoY 6m change",
         lambda p: chg(yoy(p["us_core_cpi"]), 6), +1),
    ],
    "LIQUIDITY": [   # positive = easing
        ("US M2 YoY", lambda p: yoy(p["us_m2"]), +1),
        ("Fed assets 6m log change", lambda p: logchg(p["us_fed_assets"], 6), +1),
        ("Fed funds 6m change (inverted)", lambda p: chg(p["us_fedfunds"], 6), -1),
        ("NFCI level (inverted)", lambda p: p["us_nfci"], -1),
        ("dollar 6m change (inverted)", lambda p: chg(p["dollar"], 6), -1),
        ("real yield 6m change (inverted)",
         lambda p: chg(p["us_real_yield_10y"], 6), -1),
    ],
    "STRESS": [
        ("VIX level", lambda p: p["us_vix"], +1),
        ("Baa spread level", lambda p: p["us_baa_spread"], +1),
        ("St Louis stress index", lambda p: p["us_stlfsi"], +1),
        ("EPU US level", lambda p: p["epu_us"], +1),
        ("EPU global level", lambda p: p["epu_global"], +1),
    ],
    "IN_STRESS": [   # India-only modifier for Nifty
        ("India VIX level", lambda p: p["india_vix"], +1),
        ("EPU India level", lambda p: p["epu_india"], +1),
        ("USD/INR 6m log change", lambda p: logchg(p["usdinr"], 6), +1),
        ("FPI equity 3m sum (inverted)",
         lambda p: p["fpi_equity"].rolling(3).sum(), -1),
        ("India call rate 6m change", lambda p: chg(p["in_call_rate"], 6), +1),
        ("India CPI YoY (MoSPI from 2014, OECD before)", lambda p: p["in_cpi"], +1),
    ],
    "IN_GROWTH": [   # India growth dial; sets the India regime with in_cpi
        ("India IIP YoY (MoSPI)", lambda p: p["in_iip_yoy"], +1),
        ("India OECD CLI 6m change (partial, ends 2024-01)",
         lambda p: chg(p["in_cli"], 6), +1),
        ("Nifty 6m log change", lambda p: logchg(p["nifty"], 6), +1),
    ],
}
DIALS = ["GROWTH", "INFLATION", "LIQUIDITY", "STRESS", "IN_STRESS", "IN_GROWTH"]


def build_dials(panel: pd.DataFrame) -> pd.DataFrame:
    """Each dial = mean of its inputs' z-scores (inputs present that month)."""
    out = {}
    for dial, items in DIAL_INPUTS.items():
        cols = []
        for label, fn, sign in items:
            try:
                raw = fn(panel)
            except KeyError:
                continue
            # a monthly release lags the read month by one or two months;
            # the last published value is carried forward up to 2 months
            cols.append(sign * z(raw).ffill(limit=2))
        out[dial] = pd.concat(cols, axis=1).mean(axis=1, skipna=True)
        out[dial + "_n"] = pd.concat(cols, axis=1).notna().sum(axis=1)
    d = pd.DataFrame(out)
    for dial in DIALS:
        d[dial + "_6m"] = d[dial] - d[dial].shift(6)
        d[dial + "_sm"] = d[dial].rolling(3).mean()   # 3-month smoothing
    return d


# ----------------------------------------------------------------- regime
QUAD = {(True, True): "REFLATION", (True, False): "GOLDILOCKS",
        (False, True): "STAGFLATION", (False, False): "DEFLATION"}


# Regime definition (operator ruling 2026-10-05): LEVEL against benchmarks.
# Inflation is HIGH when US CPI YoY is above CPI_BENCH or the 10y breakeven is
# above BE_BENCH. Growth is HIGH when the smoothed GROWTH dial is above its
# five-year norm (z > 0). "direction" (sign of the 6-month change in each
# dial) is kept as an option; it was the v2 definition and is what
# EVALUATION_2026-10.md tested.
REGIME_MODE = "level"      # "level" or "direction"
CPI_BENCH = 3.0            # % YoY
BE_BENCH = 2.5             # % 10y breakeven
# India regime (operator request 2026-10-05): the same quadrant logic on
# India's own growth and inflation, read beside the global one. India
# inflation is HIGH when MoSPI CPI YoY is above IN_CPI_BENCH: the RBI 4%
# target plus one point, the same margin the US benchmark gives the Fed's
# 2%, and the midpoint of the 4-6% upper half of the tolerance band. India
# growth is HIGH when the smoothed IN_GROWTH dial (IIP YoY, OECD CLI change,
# Nifty 6m change) is above its five-year norm. The India regime governs
# Nifty and Indian rates; the global regime governs gold, silver, the base
# metals and Brent. When the two differ the read is flagged DIVERGENCE.
IN_CPI_BENCH = 5.0         # % YoY, MoSPI CPI combined
# India growth test (operator ruling 2026-10-05, "Design A"): fixed
# benchmarks, majority vote, no price input. Growth HIGH when a strict
# majority of the available tests pass: IIP YoY above IN_IIP_BENCH
# (industry), services GVA YoY above IN_GVA_BENCH (the 55% of GVA that IIP
# misses; quarterly, known two months after quarter end), bank credit YoY
# above IN_CREDIT_BENCH (financing of both). With three tests available two
# must pass; with two (before the quarterly GVA series starts in 2012) both
# must. The z-score dial ("zscore") stays as an option.
IN_GROWTH_MODE = "vote"    # "vote" or "zscore"
IN_IIP_BENCH = 4.0         # % YoY
IN_GVA_BENCH = 7.0         # % YoY, services GVA, constant prices
IN_CREDIT_BENCH = 12.0     # % YoY, bank credit to the private sector


def india_growth_votes(panel: pd.DataFrame) -> pd.DataFrame:
    """Per-month pass/fail of the three India growth tests and the verdict."""
    t = pd.DataFrame(index=panel.index)
    # IIP is noisy month to month (single prints of -0.9% and +8.8% sit
    # weeks apart in 2025-26); the test reads its 3-month mean
    iip = panel["in_iip_yoy"].ffill(limit=2).rolling(3, min_periods=2).mean()
    t["iip"] = (iip > IN_IIP_BENCH).where(iip.notna())
    t["gva"] = (panel["in_services_gva_yoy"] > IN_GVA_BENCH).where(panel["in_services_gva_yoy"].notna())
    t["credit"] = (panel["in_bank_credit_yoy"] > IN_CREDIT_BENCH).where(panel["in_bank_credit_yoy"].notna())
    t["available"] = t[["iip", "gva", "credit"]].notna().sum(axis=1)
    t["votes"] = t[["iip", "gva", "credit"]].fillna(False).astype(bool).sum(axis=1)
    t["high"] = (t["votes"] * 2 > t["available"]).where(t["available"] >= 2)
    return t


def regime(d: pd.DataFrame, panel: pd.DataFrame | None = None,
           mode: str | None = None) -> pd.DataFrame:
    """Quadrant of GROWTH x INFLATION, by level (default) or by direction."""
    mode = mode or REGIME_MODE
    r = pd.DataFrame(index=d.index)
    if mode == "level":
        if panel is None:
            raise ValueError("level mode needs the panel for CPI and breakeven")
        cpi = yoy(panel["us_cpi"]).ffill(limit=2).reindex(d.index)
        be = panel["us_breakeven_10y"].reindex(d.index)
        i_hi = (cpi > CPI_BENCH) | (be > BE_BENCH)
        g_hi = d["GROWTH_sm"] > 0
        r["quadrant"] = [QUAD[(a, b)] for a, b in zip(g_hi, i_hi)]
        r.loc[d["GROWTH_sm"].isna() | (cpi.isna() & be.isna()), "quadrant"] = None
    else:
        g_up = d["GROWTH_sm"].diff(6) > 0
        i_up = d["INFLATION_sm"].diff(6) > 0
        r["quadrant"] = [QUAD[(a, b)] for a, b in zip(g_up, i_up)]
        r.loc[d["GROWTH_sm"].diff(6).isna() | d["INFLATION_sm"].diff(6).isna(),
              "quadrant"] = None
    # India quadrant
    if mode == "level":
        icpi = panel["in_cpi"].ffill(limit=2).reindex(d.index)
        ii_hi = icpi > IN_CPI_BENCH
        if IN_GROWTH_MODE == "vote":
            v = india_growth_votes(panel).reindex(d.index)
            ig_hi = v["high"].fillna(False).astype(bool)
            g_missing = v["high"].isna()
            r["in_votes"] = v["votes"].where(v["available"] >= 2)
        else:
            ig_hi = d["IN_GROWTH_sm"] > 0
            g_missing = d["IN_GROWTH_sm"].isna()
        r["in_quadrant"] = [QUAD[(a, b)] for a, b in zip(ig_hi, ii_hi)]
        r.loc[g_missing | icpi.isna(), "in_quadrant"] = None
    else:
        icpi = panel["in_cpi"].ffill(limit=2).reindex(d.index) if panel is not None else None
        ig_up = d["IN_GROWTH_sm"].diff(6) > 0
        ii_up = icpi.diff(6) > 0 if icpi is not None else pd.Series(False, index=d.index)
        r["in_quadrant"] = [QUAD[(a, b)] for a, b in zip(ig_up, ii_up)]
        bad = d["IN_GROWTH_sm"].diff(6).isna()
        if icpi is not None:
            bad = bad | icpi.diff(6).isna()
        r.loc[bad, "in_quadrant"] = None
    r["divergence"] = (r["quadrant"].notna() & r["in_quadrant"].notna()
                       & (r["quadrant"] != r["in_quadrant"]))
    r["liquidity"] = np.where(d["LIQUIDITY_sm"] > 0.25, "EASING",
                              np.where(d["LIQUIDITY_sm"] < -0.25, "TIGHT",
                                       "NEUTRAL"))
    r["stress"] = np.where(d["STRESS_sm"] > 1.0, "HIGH",
                           np.where(d["STRESS_sm"] < -0.5, "LOW", "NORMAL"))
    r["in_stress"] = np.where(d["IN_STRESS_sm"] > 1.0, "HIGH",
                              np.where(d["IN_STRESS_sm"] < -0.5, "LOW",
                                       "NORMAL"))
    return r


# ----------------------------------------------------------------- bands
ASSETS = ["gold", "silver", "aluminium", "zinc", "brent", "nifty"]
# Base band by quadrant: +1 OVERWEIGHT, 0 NEUTRAL, -1 UNDERWEIGHT.
BASE = {
    #            REFL  GOLD  STAG  DEFL
    "gold":      (0,   -1,   +1,   0),
    "silver":    (+1,   0,    0,  -1),
    "aluminium": (+1,  +1,   -1,  -1),
    "zinc":      (+1,  +1,   -1,  -1),
    "brent":     (+1,  -1,   +1,  -1),
    "nifty":     (0,   +1,   -1,   0),
}
BASE_REASON = {
    "gold": "gold wants rising inflation with falling growth; it is the hedge",
    "silver": "half monetary, half industrial: best when both growth and "
              "inflation rise, worst when both fall",
    "aluminium": "priced off factory demand: growth up is what matters",
    "zinc": "as aluminium",
    "brent": "an inflation asset: rises with the inflation impulse, falls "
             "without it",
    "nifty": "equities want growth with falling inflation; stagflation is "
             "the one quadrant that hurts",
}
# Liquidity shade: easing adds one step to these, tightening removes one.
LIQ_SHADE = {"gold": +1, "silver": +1, "aluminium": +1, "zinc": +1,
             "brent": 0, "nifty": +1}
# Stress shade when STRESS is HIGH.
STRESS_SHADE = {"gold": +1, "silver": -1, "aluminium": -1, "zinc": -1,
                "brent": -1, "nifty": -1}
QIDX = {"REFLATION": 0, "GOLDILOCKS": 1, "STAGFLATION": 2, "DEFLATION": 3}
BAND = {1: "OVERWEIGHT", 0: "NEUTRAL", -1: "UNDERWEIGHT"}


def bands(r: pd.DataFrame) -> pd.DataFrame:
    """Band per asset per month from the regime row. Clipped to one step."""
    out = {}
    for a in ASSETS:
        score = pd.Series(np.nan, index=r.index)
        for i, (q, liq, st, ist) in enumerate(zip(r["quadrant"], r["liquidity"],
                                                  r["stress"], r["in_stress"])):
            if q is None or (isinstance(q, float) and np.isnan(q)):
                continue
            s = BASE[a][QIDX[q]]
            if liq == "EASING":
                s += LIQ_SHADE[a]
            elif liq == "TIGHT":
                s -= LIQ_SHADE[a]
            if st == "HIGH":
                s += STRESS_SHADE[a]
            if a == "nifty" and ist == "HIGH":
                s -= 1
            score.iloc[i] = max(-1, min(1, s))
        out[a] = score
    return pd.DataFrame(out)


def rules() -> list[str]:
    L = ["Each input is a trailing 5-year z-score (60 months, minimum 36); "
         "a dial is the mean of its inputs' z-scores, smoothed 3 months. "
         "A series that lags the read month is carried forward up to 2 months.",
         f"Regime ({REGIME_MODE}): inflation HIGH when US CPI YoY > {CPI_BENCH}% "
         f"or 10y breakeven > {BE_BENCH}%; growth HIGH when the smoothed GROWTH "
         "dial is above its 5-year norm (z > 0). Direction mode (sign of the "
         "6-month change in each dial) is available as an option.",
         f"India regime: inflation HIGH when MoSPI CPI YoY > {IN_CPI_BENCH}% "
         "(RBI 4% target plus one point); growth HIGH when a strict majority "
         f"of the available tests pass: IIP YoY (3-month mean) > {IN_IIP_BENCH}%, services GVA "
         f"YoY > {IN_GVA_BENCH}% (quarterly, known two months after quarter "
         f"end), bank credit YoY > {IN_CREDIT_BENCH}% (IN_GROWTH_MODE = vote; "
         "the z-score dial is the other option). India regime governs Nifty "
         "and Indian rates; the global regime governs gold, silver, base "
         "metals and Brent. DIVERGENCE is flagged when the two differ.",
         "LIQUIDITY tag: EASING above +0.25, TIGHT below -0.25. STRESS tag: "
         "HIGH above +1.0, LOW below -0.5. IN_STRESS the same, Nifty only.",
         "Band = base band for the quadrant, +1 step if EASING, -1 if TIGHT "
         "(brent unshaded), stress HIGH adds +1 to gold and -1 to the rest, "
         "Nifty takes -1 more if IN_STRESS is HIGH; clipped to one step."]
    for dial, items in DIAL_INPUTS.items():
        L.append(f"{dial}: " + "; ".join(
            f"{lab}{' (-)' if sgn < 0 else ''}" for lab, _, sgn in items))
    for a in ASSETS:
        L.append(f"{a}: REFL {BASE[a][0]:+d}, GOLDILOCKS {BASE[a][1]:+d}, "
                 f"STAG {BASE[a][2]:+d}, DEFL {BASE[a][3]:+d}; "
                 f"{BASE_REASON[a]}")
    return L


def run_all():
    p = load_panel()
    d = build_dials(p)
    r = regime(d, p)
    b = bands(r)
    return p, d, r, b


if __name__ == "__main__":
    p, d, r, b = run_all()
    last = r.index[-1]
    print(last, r.loc[last].to_dict())
    print(d.loc[last, DIALS].round(2).to_dict())
    print(b.loc[last].map(BAND).to_dict())
