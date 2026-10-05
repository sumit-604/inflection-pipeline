#!/usr/bin/env python3
"""Build the monthly series for the macro regime model from raw source files.

Raw files live in data/raw/ and were fetched on 2026-10-05 through the
operator's laptop browser (the cloud shell cannot reach FRED, Yahoo, EIA,
NSDL or CFTC). This script turns them into one CSV per series under data/,
each with columns month, value (plus month_avg and last_obs_date where the
source is daily or weekly), and writes data/sources.md from what it built.
Nothing here types a number: every value comes from a raw file.

Run: python build_data.py
"""
from __future__ import annotations

import datetime as dt
import io
import json
import zipfile
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
RAW = DATA / "raw"
V1 = HERE.parent / "macro-direction" / "data"      # v1 cache, reused
CFTC_DIR = Path("/tmp/claude-0/cftc")               # zips kept out of the repo
TODAY = "2026-10-05"
LOG: list[dict] = []


def _monthly(s: pd.Series, how: str = "last") -> pd.DataFrame:
    """Daily/weekly/monthly series -> month-end value, monthly mean, last date.

    A final month whose last observation is before the 15th is dropped
    (same rule as macro-direction/fetch.py).
    """
    s = pd.to_numeric(s, errors="coerce").dropna().sort_index()
    m = s.index.to_period("M")
    out = pd.DataFrame({"value": s.groupby(m).last() if how == "last"
                        else s.groupby(m).mean(),
                        "month_avg": s.groupby(m).mean(),
                        "last_obs_date": pd.Series(s.index, index=s.index)
                        .groupby(m).last().dt.date.astype(str)})
    per_month = s.groupby(m).size().median()
    if per_month > 1.5 and len(out) and \
            pd.Timestamp(out["last_obs_date"].iloc[-1]).day < 15:
        out = out.iloc[:-1]
    out.index = out.index.astype(str)
    out.index.name = "month"
    return out


def _save(df: pd.DataFrame, name: str, code: str, url: str, status: str,
          note: str = ""):
    df.to_csv(DATA / f"{name}.csv")
    LOG.append(dict(name=name, code=code, url=url, status=status,
                    first=df.index[0], last=df.index[-1], rows=len(df),
                    fetched=TODAY, note=note))


# ------------------------------------------------------------------- FRED
def fred():
    series = {}
    for f in ["fred_bundle_2026-10-05.json", "fred_bundle2_2026-10-05.json"]:
        j = json.load(open(RAW / f))
        for code, text in j["series"].items():
            if not text.startswith("ERROR"):
                series[code] = text
    keep = {
        # code: (file name, note)
        "DFII10": ("us_real_yield_10y", "US 10y TIPS yield, %, daily"),
        "T10YIE": ("us_breakeven_10y", "US 10y breakeven inflation, %, daily"),
        "T10Y2Y": ("us_curve_10y2y", "US 10y minus 2y, pp, daily"),
        "DGS10": ("us_nominal_10y", "US 10y Treasury yield, %, daily"),
        "FEDFUNDS": ("us_fedfunds", "Effective Fed funds, %, monthly"),
        "CPIAUCSL": ("us_cpi", "US CPI-U index, SA, monthly"),
        "CPILFESL": ("us_core_cpi", "US core CPI index, SA, monthly"),
        "M2SL": ("us_m2", "US M2, $bn, SA, monthly"),
        "WALCL": ("us_fed_assets", "Fed total assets, $mn, weekly (Wed)"),
        "BOGMBASE": ("us_monetary_base", "US monetary base, $mn, monthly"),
        "NFCI": ("us_nfci", "Chicago Fed National Financial Conditions "
                            "Index, weekly; positive = tighter than average"),
        "BAA10Y": ("us_baa_spread", "Moody's Baa yield minus 10y Treasury, "
                                    "pp, daily; the credit-stress series "
                                    "(ICE HY OAS on FRED starts 2023-10 only)"),
        "BAMLH0A0HYM2": ("us_hy_oas", "ICE BofA US HY OAS, pp, daily; "
                                      "FRED serves 2023-10 on only"),
        "STLFSI4": ("us_stlfsi", "St Louis Fed Financial Stress Index, "
                                 "weekly"),
        "VIXCLS": ("us_vix", "CBOE VIX close, daily"),
        "DTWEXBGS": ("usd_broad", "Fed broad dollar index, daily"),
        "DEXINUS": ("usdinr", "USD/INR, daily"),
        "DEXCHUS": ("usdcny", "USD/CNY, daily"),
        "INDPRO": ("us_indpro", "US industrial production index, monthly"),
        "RECPROUSM156N": ("us_recession_prob", "Smoothed US recession "
                                               "probability, %, monthly"),
        "USEPUINDXM": ("epu_us", "Economic Policy Uncertainty index, US, "
                                 "monthly (Baker-Bloom-Davis via FRED)"),
        "INDEPUINDXM": ("epu_india", "Economic Policy Uncertainty index, "
                                     "India, monthly"),
        "GEPUCURRENT": ("epu_global", "Global EPU, current-price GDP "
                                      "weights, monthly"),
        "IRSTCI01INM156N": ("in_call_rate", "India call money rate, %, "
                                            "monthly (OECD MEI)"),
        "INDIRLTLT01STM": ("in_gsec_10y", "India 10y government bond yield, "
                                          "%, monthly (OECD MEI), 2011-12 on"),
        "INTDSRINM193N": ("in_policy_rate_imf", "India central bank "
                                                "discount/policy rate, %, "
                                                "monthly (IMF IFS), ends "
                                                "2022-07"),
        "CPALTT01INM659N": ("in_cpi_yoy", "India CPI all items, % change "
                                          "YoY, monthly (OECD MEI), ends "
                                          "2025-03: PARTIAL"),
        "MABMM301INM189N": ("in_m3", "India broad money M3, INR, monthly "
                                     "(OECD MEI), ends 2023-09: PARTIAL"),
        "INDLOLITONOSTSAM": ("in_cli", "India OECD composite leading "
                                       "indicator, ends 2024-01: PARTIAL"),
        "PCOPPUSDM": ("imf_copper", "IMF copper price, $/t, monthly avg"),
        "PALUMUSDM": ("imf_aluminium", "IMF aluminium price, $/t, monthly "
                                       "avg; cross-check for Pink Sheet"),
        "PZINCUSDM": ("imf_zinc", "IMF zinc price, $/t, monthly avg; "
                                  "cross-check for Pink Sheet"),
        "DCOILBRENTEU": ("brent_spot_fred", "EIA Brent spot via FRED, "
                                            "$/bbl, daily"),
    }
    for code, (name, note) in keep.items():
        if code not in series:
            LOG.append(dict(name=name, code=code, url="", status="FAILED",
                            first="", last="", rows="", fetched=TODAY,
                            note="not served by FRED"))
            continue
        df = pd.read_csv(io.StringIO(series[code]), na_values=".")
        s = pd.Series(df.iloc[:, 1].values, index=pd.to_datetime(df.iloc[:, 0]))
        out = _monthly(s)
        _save(out, name, code,
              f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={code}",
              "PRIMARY", note)


# ------------------------------------------------------------------ Yahoo
def yahoo():
    j = json.load(open(RAW / "yahoo_bundle_2026-10-05.json"))
    keep = {
        "GC=F": ("gold_usd", "COMEX gold front future, $/oz"),
        "SI=F": ("silver_usd", "COMEX silver front future, $/oz"),
        "HG=F": ("copper_usd", "COMEX copper front future, $/lb"),
        "ALI=F": ("aluminium_fut", "COMEX aluminium future, $/t, 2014-05 on"),
        "BZ=F": ("brent_fut", "ICE Brent front future, $/bbl, 2007-07 on"),
        "CL=F": ("wti_fut", "NYMEX WTI front future, $/bbl"),
        "^NSEI": ("nifty", "NIFTY 50 close, INR, 2007-09 on"),
        "^NSEBANK": ("banknifty", "NIFTY Bank close, INR"),
        "^INDIAVIX": ("india_vix", "India VIX close, 2008-03 on"),
        "^VIX": ("vix_yahoo", "CBOE VIX close (Yahoo copy)"),
        "DX-Y.NYB": ("dxy", "ICE US Dollar Index, 1971 on"),
        "^GSPC": ("spx", "S&P 500 close"),
        "000001.SS": ("shanghai", "Shanghai Composite close, 1997-07 on"),
        "TLT": ("tlt", "iShares 20y+ Treasury ETF, 2002-07 on"),
    }
    for sym, (name, note) in keep.items():
        if sym not in j["series"]:
            LOG.append(dict(name=name, code=sym, url="", status="FAILED",
                            first="", last="", rows="", fetched=TODAY,
                            note="not served by Yahoo"))
            continue
        rows = j["series"][sym]["rows"]
        s = pd.Series([r[1] for r in rows],
                      index=pd.to_datetime([r[0] for r in rows]))
        out = _monthly(s)
        _save(out, name, sym,
              f"https://query1.finance.yahoo.com/v8/finance/chart/{sym} "
              "(interval=1d, period1=0)", "PRIMARY",
              f"{note}; {len(rows)} daily closes")


# -------------------------------------------------------------------- EIA
def eia():
    for fname, name, code, note in [
        ("eia_WCESTUS1w.xls", "us_crude_stocks_ex_spr", "WCESTUS1",
         "US ending stocks of crude oil excl. SPR, kbbl, weekly"),
        ("eia_WCRSTUS1w.xls", "us_crude_stocks_total", "WCRSTUS1",
         "US ending stocks of crude oil incl. SPR, kbbl, weekly"),
        ("eia_WCRFPUS2w.xls", "us_crude_production", "WCRFPUS2",
         "US field production of crude oil, kb/d, weekly"),
        ("eia_RBRTEd.xls", "brent_spot_eia", "RBRTE",
         "Europe Brent spot FOB, $/bbl, daily (primary EIA file)"),
    ]:
        df = pd.read_excel(RAW / fname, sheet_name="Data 1", skiprows=2)
        s = pd.Series(df.iloc[:, 1].values, index=pd.to_datetime(df.iloc[:, 0]))
        out = _monthly(s)
        _save(out, name, code,
              f"https://www.eia.gov/dnav/pet/hist_xls/{fname[4:]}",
              "PRIMARY", note)


# ------------------------------------------------------------------- NSDL
def nsdl():
    j = json.load(open(RAW / "nsdl_fpi_yearwise_2026-10-05.json"))
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    eq, debt, total = {}, {}, {}
    for y, blk in j["years"].items():
        hdr = blk["header_rows"][0] if blk["header_rows"] else \
            ["Equity", "Debt", "Total"]
        # the second header row (2024+) splits debt into sub-limits; the
        # first header row's column count still maps the data row
        for r in blk["rows"]:
            mon = months.index(next(m for m in months if r[0].startswith(m))) + 1
            key = f"{y}-{mon:02d}"
            if r[0].strip().endswith("**"):          # partial month
                continue
            vals = [float(x.replace(",", "")) if x.replace(",", "")
                    .replace("-", "").replace(".", "").strip() else 0.0
                    for x in r[1:]]
            if len(hdr) == 3:                        # Equity|Debt|Total
                e, d, t = vals[0], vals[1], vals[-1]
            elif hdr[:4] == ["Equity", "Debt", "Hybrid", "Total"]:
                e, d, t = vals[0], vals[1], vals[-1]
            elif "Debt-VRR" in hdr and len(hdr) == 5:
                e, d, t = vals[0], vals[1] + vals[2], vals[-1]
            else:   # 2024+: Equity|Debt-GL|Debt-VRR|Debt-FAR|Hybrid|MF x5|AIF|Total
                e, d, t = vals[0], vals[1] + vals[2] + vals[3], vals[-1]
            eq[key], debt[key], total[key] = e, d, t
    df = pd.DataFrame({"value": pd.Series(eq), "fpi_debt_net_inr_cr":
                       pd.Series(debt), "fpi_total_net_inr_cr":
                       pd.Series(total)}).sort_index()
    df.index.name = "month"
    _save(df, "in_fpi_flows", "NSDL FPI net investment, calendar-year tables",
          "https://www.fpi.nsdl.co.in/web/Reports/Yearwise.aspx?RptType=6",
          "PRIMARY", "value = equity net, INR crore; debt = general + VRR + "
          "FAR where split; total as published. Partial current month "
          "excluded. Each year's table read from NSDL on 2026-10-05.")


# ------------------------------------------------------------------- CFTC
def cftc():
    """Legacy futures-only COT, 1986-2026: non-commercial net as % of OI."""
    want = {"088691": "gold", "084691": "silver", "067651": "wti",
            "085692": "copper"}
    frames = []
    for z in sorted(CFTC_DIR.glob("cftc_deacot*.zip")):
        with zipfile.ZipFile(z) as zf:
            name = [n for n in zf.namelist() if n.lower().endswith(".txt")][0]
            df = pd.read_csv(zf.open(name), dtype=str, low_memory=False)
        df.columns = [c.strip() for c in df.columns]
        code_col = "CFTC Contract Market Code"
        df = df[df[code_col].str.strip().isin(want)]
        frames.append(df)
    all_ = pd.concat(frames)
    all_["date"] = pd.to_datetime(all_["As of Date in Form YYYY-MM-DD"])
    num = lambda c: pd.to_numeric(all_[c].str.replace(",", ""), errors="coerce")
    all_["net_pct_oi"] = (num("Noncommercial Positions-Long (All)")
                          - num("Noncommercial Positions-Short (All)")) \
        / num("Open Interest (All)") * 100
    all_["oi"] = num("Open Interest (All)")
    out_all = []
    for code, label in want.items():
        d = all_[all_[code_col].str.strip() == code].sort_values("date")
        d = d.drop_duplicates("date", keep="last")
        s = pd.Series(d["net_pct_oi"].values, index=d["date"])
        out = _monthly(s)
        _save(out, f"cot_{label}_net_pct_oi", f"CFTC legacy COT {code}",
              "https://www.cftc.gov/MarketReports/CommitmentsofTraders/"
              "HistoricalCompressed/index.htm (deacot1986_2016.zip + "
              "deacot2017..2026.zip)", "PRIMARY",
              f"{d['Market and Exchange Names'].iloc[-1].strip()}; "
              "non-commercial (long minus short) as % of open interest, "
              "futures only, last report of the month")
        slim = d[["date", "oi", "net_pct_oi"]].assign(contract=label)
        out_all.append(slim)
    pd.concat(out_all).to_csv(RAW / "cftc_legacy_weekly_slim.csv", index=False)


# ------------------------------------------------------------------ MoSPI
MOSPI_API = "https://api.mospi.gov.in"
_MON = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def _mospi_series(fname: str, col: str) -> pd.Series:
    rows = json.loads((RAW / fname).read_text())
    s = {pd.Period(f"{int(r['year'])}-{_MON[r['month']]:02d}", "M"):
         pd.to_numeric(r[col], errors="coerce") for r in rows}
    return pd.Series(s).sort_index()


def mospi():
    """India IIP YoY and CPI YoY from the MoSPI API (fetched 2026-10-05
    through Firecrawl; raw JSON kept under data/raw/mospi_*.json).

    IIP: four base years spliced. The first twelve months of a new base
    compare against the base-year average, not a real prior month (base
    2004-05 prints +26.7% for 2006-03; base 2022-23 prints +19.0% for
    2024-03), so each base is used only from its second year, and the
    older base covers the join. Base 1993-94 is null for 2004-04 to
    2005-03 at source and base 2004-05 is invalid there: that year is
    NOT FOUND.
    CPI: base 2012 from 2014-01 (2013 inflation is null at source) to
    2025-12, base 2024 from 2026-01. Earlier months come from the FRED
    OECD series in_cpi_yoy.csv, which the model uses only before 2014-01:
    on the 2014-2025 overlap it differs from MoSPI by up to 5.6 points.
    """
    b93 = _mospi_series("mospi_iip_1993-94_monthly.json", "growth_rate")
    b04 = _mospi_series("mospi_iip_2004-05_monthly.json", "growth_rate")
    b11 = _mospi_series("mospi_iip_2011-12_monthly.json", "growth_rate")
    b22 = _mospi_series("mospi_iip_2022-23_monthly.json", "growth_rate")
    P = lambda s: pd.Period(s, "M")
    iip = pd.concat([
        b93[(b93.index >= P("1995-04")) & (b93.index <= P("2006-03"))],
        b04[(b04.index >= P("2006-04")) & (b04.index <= P("2012-12"))],
        b11[(b11.index >= P("2013-01")) & (b11.index <= P("2024-12"))],
        b22[b22.index >= P("2025-01")],
    ]).sort_index()
    iip = iip.reindex(pd.period_range(iip.index[0], iip.index[-1], freq="M"))
    df = pd.DataFrame({"value": iip.values}, index=iip.index.astype(str))
    df.index.name = "month"
    _save(df, "in_iip_yoy", "MoSPI IIP General index, growth rate % YoY",
          f"{MOSPI_API}/api/iip/getIipData?base_year=<1993-94|2004-05|"
          "2011-12|2022-23>&frequency=Monthly&type=General&year=...&Format=JSON",
          "PRIMARY", "spliced: base 1993-94 to 2006-03, 2004-05 from 2006-04, "
          "2011-12 from 2013-01, 2022-23 from 2025-01 (first year of each "
          "base dropped: it compares to the base-year average); 2004-04 to "
          "2005-03 null at source")
    c12 = _mospi_series("mospi_cpi_2012_monthly.json", "inflation")
    c24 = _mospi_series("mospi_cpi_2024_monthly.json", "inflation")
    cpi = pd.concat([c12[(c12.index >= P("2014-01")) & (c12.index <= P("2025-12"))],
                     c24[c24.index >= P("2026-01")]]).sort_index()
    df = pd.DataFrame({"value": cpi.values}, index=cpi.index.astype(str))
    df.index.name = "month"
    _save(df, "in_cpi_yoy_mospi", "MoSPI CPI Combined All India General, "
          "inflation % YoY",
          f"{MOSPI_API}/api/cpi/getCPIIndex?base_year=2012&series=Current&"
          "state_code=99&group_code=0&sector_code=3 ; /api/cpi/getCPIData?"
          "base_year=2024&series=Current&state_code=1&sector_code=3&"
          "division_code=0", "PRIMARY",
          "base 2012 to 2025-12, base 2024 from 2026-01; 2020-04 and "
          "2020-05 null at source (status F*); the model uses this from "
          "2014-01 and the FRED OECD series before")


# ------------------------------------------------------- v1 cache reuse
def v1_reuse():
    if not V1.exists():
        for new in ["pinksheet_monthly_avg", "nifty_long"]:
            if (DATA / f"{new}.csv").exists():
                df = pd.read_csv(DATA / f"{new}.csv", dtype={"month": str}).set_index("month")
                LOG.append(dict(name=new, code=new, url="tools/macro-direction/data (PR #202)", status="V1 CACHE", first=df.index[0], last=df.index[-1], rows=len(df), fetched="2026-10-04", note="kept from the earlier build; v1 folder not present in this checkout"))
        return
    for name, new, note in [
        ("pinksheet_monthly_avg", "pinksheet_monthly_avg",
         "World Bank Pink Sheet monthly averages; copied from "
         "tools/macro-direction/data (datahub mirror, not checked against "
         "the World Bank file: the browser cannot reach thedocs.worldbank.org)"),
        ("nifty_monthly", "nifty_long",
         "NIFTY 50 month-end from NSE files 1990-07 on, patched 2026-09 "
         "from Yahoo; copied from tools/macro-direction/data"),
    ]:
        df = pd.read_csv(V1 / f"{name}.csv", dtype={"month": str}).set_index("month")
        if "month_end" in df:
            df = df.rename(columns={"month_end": "value"})
        df.to_csv(DATA / f"{new}.csv")
        LOG.append(dict(name=new, code=name, url="tools/macro-direction/data/"
                        f"{name}.csv", status="V1 CACHE", first=df.index[0],
                        last=df.index[-1], rows=len(df), fetched="2026-10-04",
                        note=note))


def write_sources():
    L = ["# Data sources, macro regime model",
         "",
         f"Written by build_data.py on {TODAY}. One row per series under "
         "data/. PRIMARY = the issuing body's own file, fetched through the "
         "operator's laptop browser on 2026-10-05 and kept under data/raw/ "
         "(CFTC zips reduced to data/raw/cftc_legacy_weekly_slim.csv). "
         "V1 CACHE = copied from tools/macro-direction/data with that "
         "folder's provenance. FAILED = not served; the model runs without "
         "it. PARTIAL in a note = the series ends before 2026-09.",
         "",
         "Monthly rule: last observation of the month is the month value; "
         "month_avg is the mean; a final month whose last observation is "
         "before the 15th is dropped.",
         "",
         "| File | Series code | Status | Source URL | First | Last | Rows | "
         "Fetched | Note |", "|---|---|---|---|---|---|---|---|---|"]
    for r in LOG:
        L.append(f"| {r['name']}.csv | {r['code']} | {r['status']} | {r['url']} "
                 f"| {r['first']} | {r['last']} | {r['rows']} | {r['fetched']} "
                 f"| {r['note']} |")
    (DATA / "sources.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    fred(); yahoo(); eia(); nsdl(); cftc(); mospi(); v1_reuse()
    write_sources()
    for r in LOG:
        print(f"{r['status']:9} {r['name']:28} {str(r['first']):>8} -> "
              f"{str(r['last']):8} {r['rows']}")
