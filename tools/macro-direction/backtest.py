#!/usr/bin/env python3
"""Walk-forward backtest of the macro direction model.

Run:  python backtest.py            # writes BACKTEST_<yyyy-mm>.md
      python backtest.py --out X.md

Rule layers have no fitted parameters, so every month from START is out of
sample in the mechanical sense. They were written with knowledge of how
these markets behaved in general, which no backtest can remove; the report
says so. The logistic model is strictly walk-forward (model.py).
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import numpy as np
import pandas as pd

import model as M

HERE = Path(__file__).resolve().parent
START = pd.Period("2004-01", "M")


# ------------------------------------------------------------------ metrics
def hit(call: pd.Series, fwd: pd.Series) -> tuple[float, int]:
    """Hit rate over months with a call (call != 0) and a known outcome."""
    m = (call != 0) & fwd.notna()
    if m.sum() == 0:
        return np.nan, 0
    return float(((call[m] > 0) == (fwd[m] > 0)).mean()), int(m.sum())


def perf(r: pd.Series) -> dict:
    r = r.dropna()
    if len(r) == 0:
        return dict(ann=np.nan, vol=np.nan, mdd=np.nan, n=0)
    eq = (1 + r).cumprod()
    ann = eq.iloc[-1] ** (12 / len(r)) - 1
    vol = r.std() * np.sqrt(12)
    mdd = (eq / eq.cummax().clip(lower=1) - 1).min()
    return dict(ann=ann, vol=vol, mdd=mdd, n=len(r))


def pct(x, d=1):
    return "n/a" if x is None or pd.isna(x) else f"{100 * x:.{d}f}%"


def fmt_hit(hr, n):
    return "n/a" if pd.isna(hr) else f"{100 * hr:.1f}% ({n})"


# ------------------------------------------------------------- evaluation
def evaluate(panel, asset: M.Asset, with_logit=True) -> dict:
    feats = M.inputs(panel, asset.basis)
    v = M.votes(panel, asset, feats)
    v = v[(v.index >= START) & v["r12"].notna()]
    res = dict(asset=asset, v=v)
    if with_logit:
        vf = M.votes(panel, asset, feats)
        for h in (1, 3):
            p = M.logit_walk_forward(vf, feats, h,
                                     exclude_brent=asset.regime == "crude")
            res[f"logit{h}"] = p.reindex(v.index)
    return res


def hit_table(res: dict, h: int) -> dict:
    v = res["v"]
    fwd = v[f"fwd{h}"]
    row = {}
    row["model"] = hit(v["call"], fwd)
    for c in (1, 2, 3):
        row[f"conf{c}"] = hit(v["call"].where(v["conf"] == c, 0), fwd)
    row["trend"] = hit(v["L1"], fwd)
    row["trend12"] = hit(v["trend12"], fwd)
    row["up"] = hit(pd.Series(1, index=v.index), fwd)
    row["coverage"] = float((v["call"] != 0).mean())
    lp = res.get(f"logit{h}")
    if lp is not None:
        lc = np.sign(lp - 0.5).fillna(0)
        row["logit"] = hit(lc, fwd)
        win = lp.notna()
        row["model_lw"] = hit(v["call"][win], fwd[win])
        row["trend_lw"] = hit(v["L1"][win], fwd[win])
        row["up_lw"] = hit(pd.Series(1, index=v.index)[win], fwd[win])
        row["logit_start"] = str(lp.dropna().index.min()) if win.any() else "n/a"
    return row


def strategies(res: dict) -> dict:
    v = res["v"]
    r = v["fwd1"]
    out = {"Buy and hold": perf(r),
           "Rules long/flat": perf(r * (v["call"] > 0)),
           "Rules long/short": perf(r * v["call"]),
           "Trend (L1) long/flat": perf(r * (v["L1"] > 0)),
           "Trend (L1) long/short": perf(r * v["L1"])}
    for h in (1, 3):
        lp = res.get(f"logit{h}")
        if lp is not None and lp.notna().any():
            lc = np.sign(lp - 0.5)
            w = lp.notna()
            out[f"Logit {h}m long/flat"] = perf((r * (lc > 0))[w])
            out[f"Logit {h}m long/short"] = perf((r * lc)[w])
            out[f"Buy and hold (logit window)"] = perf(r[w])
    return out


def worst_stretches(res: dict, k=3) -> list[dict]:
    v = res["v"]
    ls = (v["fwd1"] * v["call"]).dropna()
    roll = (1 + ls).rolling(12).apply(np.prod, raw=True) - 1
    roll = roll.dropna().sort_values()
    picked = []
    for end, val in roll.items():
        if all(abs((end - p["end"]).n) >= 12 for p in picked):
            win = v.loc[end - 11:end]
            hr, n = hit(win["call"], win["fwd1"])
            q = win["quad"].value_counts()
            mix = ", ".join(f"{a} {b}" for a, b in q.items())
            bh = (1 + win["fwd1"]).prod() - 1
            picked.append(dict(end=end, start=end - 11, ret=val, bh=bh,
                               hit=hr, quads=mix))
        if len(picked) == k:
            break
    return picked


# NB on dates: row t holds the call made at decision t and its realised
# return over month t+1, so a stretch labelled start..end covers returns
# realised from start+1 to end+1.


def portfolio(results: dict) -> dict:
    core = [a.key for a in M.ASSETS if a.core and a.key in results]
    idx = results[core[0]]["v"].index
    for k in core[1:]:
        idx = idx.intersection(results[k]["v"].index)
    score = pd.DataFrame({k: results[k]["v"]["score"] for k in core}).loc[idx]
    r12 = pd.DataFrame({k: results[k]["v"]["r12"] for k in core}).loc[idx]
    fwd = pd.DataFrame({k: results[k]["v"]["fwd1"] for k in core}).loc[idx]
    rank_key = score + r12.rank(axis=1, pct=True) * 0.5   # tiebreak: momentum
    top2 = rank_key.apply(lambda s: list(s.nlargest(2).index), axis=1)
    r_top = pd.Series([fwd.loc[t, top2[t]].mean() for t in idx], index=idx)
    pos = (score > 0)
    r_top_pos = pd.Series([
        fwd.loc[t, [a for a in top2[t] if pos.loc[t, a]]].sum() / 2
        for t in idx], index=idx)
    r_ew = fwd.mean(axis=1)
    r_bot = pd.Series([fwd.loc[t, list(rank_key.loc[t].nsmallest(2).index)]
                       .mean() for t in idx], index=idx)
    valid = fwd.notna().all(axis=1)
    picks = pd.Series([a for t in idx[valid] for a in top2[t]]).value_counts()
    return dict(core=core, top=perf(r_top[valid]), top_pos=perf(r_top_pos[valid]),
                ew=perf(r_ew[valid]), bottom=perf(r_bot[valid]),
                start=str(idx[valid].min()), end=str(idx[valid].max()),
                picks=picks, months=int(valid.sum()),
                hit_vs_ew=float((r_top[valid] > r_ew[valid]).mean()))


def averaging_check(panel) -> list[tuple]:
    """Same rules on monthly-average vs month-end prices of one asset."""
    rows = []
    pairs = [("brent", "brent_end"), ("gold", "gold_end"),
             ("silver", "silver_end")]
    all_assets = {a.key: a for a in M.ASSETS + M.CHECK_ASSETS}
    for a_avg, a_end in pairs:
        if all_assets[a_end].price not in panel:
            rows.append((a_avg, None, None))
            continue
        ra = evaluate(panel, all_assets[a_avg], with_logit=False)
        re_ = evaluate(panel, all_assets[a_end], with_logit=False)
        common = ra["v"].index.intersection(re_["v"]["px"].dropna().index)
        ra["v"] = ra["v"].loc[common]
        re_["v"] = re_["v"].loc[common]
        rows.append((a_avg, ra, re_))
    return rows


# ------------------------------------------------------------------- report
def build(out_path: Path):
    panel = M.load_panel()
    results = {}
    for a in M.ASSETS:
        if a.price in panel and panel[a.price].notna().sum() > 24:
            results[a.key] = evaluate(panel, a)
    return panel, results


def main():
    out = HERE / f"BACKTEST_{dt.date.today():%Y-%m}.md"
    if "--out" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--out") + 1])
    panel, results = build(out)
    import report
    report.write(out, panel, results)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
