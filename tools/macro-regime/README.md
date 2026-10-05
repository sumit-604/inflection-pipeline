# macro-regime

Monthly macro regime read for six assets (gold, silver, aluminium, zinc,
Brent, Nifty 50) at a 6 to 12 month horizon. Four dials (GROWTH, INFLATION,
LIQUIDITY, STRESS) plus an India stress dial, a regime quadrant, and an
exposure band per asset. No learned parameters, no monthly direction call.

- `build_data.py` rebuilds `data/*.csv` from `data/raw/` and writes
  `data/sources.md`.
- `model.py` builds the dials, the regime and the bands; `python model.py`
  prints the latest read.
- `run.py` writes `latest.md`, formatted to drop into macro-sheet.md.
- `evaluate.py` runs the episode test in `PASS_BAR.md` and writes
  `EVALUATION_2026-10.md`.

Data is fetched through the operator's laptop browser (the cloud shell
cannot reach the source hosts); see data/sources.md for the route and the
checks. Supersedes tools/macro-direction (PR #202), which was a 1-month
direction model and failed its own bar.
