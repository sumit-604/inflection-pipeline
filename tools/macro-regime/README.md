# macro-regime

Monthly macro regime read for six assets (gold, silver, aluminium, zinc,
Brent, Nifty 50) at a 6 to 12 month horizon. Four dials (GROWTH, INFLATION,
LIQUIDITY, STRESS) plus India stress and India growth dials, a global
regime quadrant and an India regime quadrant (both by LEVEL against
benchmarks: US CPI 3% or breakeven 2.5%; India CPI 5%), and an exposure
band per asset (off: failed its bar). No learned parameters, no monthly
direction call. The India regime governs Nifty and Indian rates; the global
regime governs the metals and Brent; DIVERGENCE is flagged when they differ.

- `build_data.py` rebuilds `data/*.csv` from `data/raw/` and writes
  `data/sources.md`.
- `model.py` builds the dials, the regime and the bands; `python model.py`
  prints the latest read.
- `run.py` writes `latest.md`, formatted to drop into macro-sheet.md.
- `evaluate.py` runs the episode test in `PASS_BAR.md` and writes
  `EVALUATION_2026-10.md`.

- `analogues.py` adds regime spells, nearest past months and the India
  cross-table to `latest.md`.
- `pine/` holds the TradingView indicator and backtest strategy.

Data is fetched through the operator's laptop browser (the cloud shell
cannot reach the source hosts), and India CPI and IIP from the MoSPI API
through Firecrawl; see data/sources.md for the route and the checks. Supersedes tools/macro-direction (PR #202), which was a 1-month
direction model and failed its own bar.
