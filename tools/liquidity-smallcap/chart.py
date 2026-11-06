#!/usr/bin/env python3
"""Four stacked panels on one date axis, PNG and HTML.

1 net LAF, bars (surplus green, deficit red)
2 FBIL 3-month CD rate
3 MTF book, NSE + BSE (dotted line at the BSE coverage start)
4 Nifty Smallcap 250 / Nifty 50, rebased to 100

Shading on all panels marks trading days with net LAF below zero.
Blank days stay blank: lines break, bars are absent.

Run: python chart.py   (reads data/panel_daily.csv; writes out/)
"""
from __future__ import annotations

import os
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = Path(os.environ.get("LSC_DATA", HERE / "data"))
OUT = Path(os.environ.get("LSC_OUT", HERE / "out"))
BSE_START = pd.Timestamp("2025-10-15")   # indiamtf openapi.json
GREEN, RED, SHADE = "#2e7d32", "#c62828", "#c6282822"
LINE, LINE2 = "#1f4e79", "#6a3d9a"


def load() -> pd.DataFrame:
    p = pd.read_csv(DATA / "panel_daily.csv", parse_dates=["date"]).set_index("date")
    both = p[["nifty_smallcap_250", "nifty_50"]].dropna()
    p["rel_sc250_n50"] = pd.NA
    if len(both):
        base = both.iloc[0]
        p["rel_sc250_n50"] = (p["nifty_smallcap_250"] / p["nifty_50"]) / \
            (base["nifty_smallcap_250"] / base["nifty_50"]) * 100
    return p


def deficit_spans(laf: pd.Series) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    """Contiguous runs of trading days with net LAF < 0. A blank day ends a run."""
    spans, start, prev = [], None, None
    for d, v in laf.items():
        neg = pd.notna(v) and v < 0
        if neg and start is None:
            start = d
        if not neg and start is not None:
            spans.append((start, prev))
            start = None
        prev = d
    if start is not None:
        spans.append((start, prev))
    # widen each span by half a day so single days are visible
    return [(a - pd.Timedelta(hours=12), b + pd.Timedelta(hours=12)) for a, b in spans]


def png(p: pd.DataFrame, spans) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    fig, ax = plt.subplots(4, 1, sharex=True, figsize=(13, 11),
                           gridspec_kw={"height_ratios": [1.2, 1, 1, 1.2]})
    laf = pd.to_numeric(p["net_laf_cr"], errors="coerce") / 1e5   # Rs lakh crore
    ax[0].bar(laf.index, laf.where(laf >= 0), color=GREEN, width=1.0, label="surplus")
    ax[0].bar(laf.index, laf.where(laf < 0), color=RED, width=1.0, label="deficit")
    ax[0].axhline(0, color="#444", lw=0.6)
    ax[0].set_ylabel("Net LAF\nRs lakh crore")
    ax[0].legend(loc="upper left", fontsize=8, frameon=False)
    ax[1].plot(p.index, pd.to_numeric(p["cd_3m_pct"], errors="coerce"), color=LINE, lw=1.2)
    ax[1].set_ylabel("3M CD rate\n% (FBIL)")
    mtf = pd.to_numeric(p["mtf_combined_cr"], errors="coerce") / 1e3
    ax[2].plot(p.index, mtf, color=LINE2, lw=1.2)
    ax[2].axvline(BSE_START, color="#555", ls=":", lw=1)
    ax[2].text(BSE_START, 0.95, " BSE added", transform=ax[2].get_xaxis_transform(),
               fontsize=8, va="top", color="#555")
    ax[2].set_ylabel("MTF book\nRs '000 crore")
    ax[3].plot(p.index, pd.to_numeric(p["rel_sc250_n50"], errors="coerce"), color=LINE, lw=1.2)
    ax[3].axhline(100, color="#444", lw=0.6)
    ax[3].set_ylabel("Smallcap 250 /\nNifty 50 (=100)")
    for a in ax:
        for s, e in spans:
            a.axvspan(s, e, color=RED, alpha=0.10, lw=0)
        a.grid(axis="y", color="#ddd", lw=0.5)
        for side in ("top", "right"):
            a.spines[side].set_visible(False)
    ax[3].xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax[3].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    first = p.index.min()
    last = p.index.max()
    fig.suptitle(f"Money conditions and small caps, {first:%b %Y} to {last:%b %Y}. "
                 "Red shade = net LAF in deficit", fontsize=12, x=0.01, ha="left")
    fig.text(0.01, 0.005, "Sources: RBI DBIE (net LAF), FBIL (CD curve), indiamtf.com "
             "(NSE+BSE MTF disclosures), niftyindices.com. Blank = not published.",
             fontsize=7, color="#555")
    fig.tight_layout(rect=(0, 0.015, 1, 0.97))
    out = OUT / "liquidity_smallcap.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def html(p: pd.DataFrame, spans) -> Path:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.03,
                        row_heights=[0.3, 0.22, 0.22, 0.26],
                        subplot_titles=("Net LAF, Rs crore (surplus +, deficit -)",
                                        "FBIL 3-month CD rate, %",
                                        "MTF book, NSE + BSE, Rs crore",
                                        "Nifty Smallcap 250 / Nifty 50, rebased to 100"))
    laf = pd.to_numeric(p["net_laf_cr"], errors="coerce")
    fig.add_bar(x=p.index, y=laf, marker_color=[GREEN if v >= 0 else RED for v in laf.fillna(0)],
                name="Net LAF", row=1, col=1)
    fig.add_scatter(x=p.index, y=pd.to_numeric(p["cd_3m_pct"], errors="coerce"),
                    line=dict(color=LINE, width=1.4), name="3M CD", row=2, col=1)
    fig.add_scatter(x=p.index, y=pd.to_numeric(p["mtf_combined_cr"], errors="coerce"),
                    line=dict(color=LINE2, width=1.4), name="MTF book", row=3, col=1)
    fig.add_scatter(x=p.index, y=pd.to_numeric(p["rel_sc250_n50"], errors="coerce"),
                    line=dict(color=LINE, width=1.4), name="SC250 / N50", row=4, col=1)
    for s, e in spans:
        fig.add_vrect(x0=s, x1=e, fillcolor=RED, opacity=0.10, line_width=0,
                      row="all", col=1)
    fig.add_vline(x=BSE_START, line_dash="dot", line_color="#555", row=3, col=1)
    fig.update_layout(height=1000, showlegend=False, bargap=0, hovermode="x unified",
                      plot_bgcolor="white", paper_bgcolor="white",
                      margin=dict(l=60, r=20, t=60, b=40),
                      title="Money conditions and small caps. Red shade = net LAF in deficit")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#e5e5e5")
    out = OUT / "liquidity_smallcap.html"
    fig.write_html(out, include_plotlyjs="cdn", full_html=True)
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    p = load()
    spans = deficit_spans(pd.to_numeric(p["net_laf_cr"], errors="coerce"))
    print(png(p, spans))
    print(html(p, spans))
    print(f"{len(spans)} deficit spans shaded")


if __name__ == "__main__":
    main()
