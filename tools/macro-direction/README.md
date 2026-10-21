# Macro direction model (tools/macro-direction)

Monthly cross-asset DIRECTION model for gold, silver, aluminium, zinc,
Brent, Nifty 50, plus gold and silver in INR. A research tool. It changes
no analytical rule in the pipeline.

    pip install -q -r requirements.txt
    python fetch.py        # cache every series in data/, write data/sources.md
    python run.py          # latest.md: this month's calls, as a macro-sheet section
    python backtest.py     # BACKTEST_<yyyy-mm>.md

Files: `model.py` (panel, three vote layers, logistic comparison),
`backtest.py` (metrics), `report.py` (report tables), `verdicts.md`
(reviewer prose that report.py inserts; rewrite it when the tables move).

Data status 2026-10-04: the cloud shell could not reach FRED, Yahoo, the
World Bank or NSDL. Every cached series came from a public GitHub copy
(status MIRROR in data/sources.md). DFII10 and the Yahoo futures were not
found at all. Operator: run `python fetch.py --primary` on the laptop,
commit data/, then re-run backtest.py and run.py.
FPI flows: if NSDL blocks the script too, save the monthly table as
data/raw/fpi_equity_monthly.csv (see data/raw/README.md) and commit it.
