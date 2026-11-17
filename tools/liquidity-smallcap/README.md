# liquidity-smallcap

Does money tightness lead Indian small caps? This tool tests three money
measures against the Nifty Smallcap 250, January 2023 to today:

- RBI net LAF (Liquidity Adjustment Facility), Rs crore. Surplus +, deficit -.
- FBIL 3-month CD (certificate of deposit) rate, %.
- MTF (Margin Trading Facility) book, NSE + BSE, Rs crore.

## Status, 2026-11-17

Done. Data Jan 2023 to Nov 2026 is in data/; results are in SUMMARY.md and
out/. Headline: no measure leads the Smallcap 250 by 1 to 3 months. The
3M CD rate moves with it in the same month (r -0.43); the MTF book follows
it (r +0.64 same month, +0.44 one month later).

Data routes used (the session environment allows these hosts):

| Series | Route |
|---|---|
| Net LAF | RBI daily Money Market Operations releases, row F "net liquidity injected (outstanding including today's operations)" = Repo+MSF+SLF-Reverse Repo-SDF. DBIE encrypts its API calls, so it is not scripted. |
| 3M CD | FBIL public endpoint www.fbil.org.in/wasdm/cd/fetchfiltered (the call the FBIL site makes) |
| MTF book | indiamtf.com /history/snapshots.json (NSE, BSE, combined) |
| Indices | NSE ind_close_all daily files on nsearchives.nseindia.com. NSE Indices publishes niftyindices.com; its own history API needs a further host. |

## Files

| File | Does |
|---|---|
| fetch_laptop.py | Downloads every series (subcommands mtf, indices-nse, cd3m, laf-mmo); `register` records a manual download in data/raw/manifest.json |
| build_data.py | data/raw/ to one CSV per series (each row carries source_url and downloaded_on), panel_daily.csv, sources.md, gaps.md |
| chart.py | out/liquidity_smallcap.png and .html: four panels, one date axis, deficit days shaded |
| lag_test.py | Monthly correlation table, lags 0 to 3; rolling 12-month check for failure periods |
| summary_draft.py | Fills the numbers into out/SUMMARY_DRAFT.md; a person then writes SUMMARY.md |

## Refresh

```
pip install -r requirements.txt
python fetch_laptop.py mtf
python fetch_laptop.py indices-nse
python fetch_laptop.py cd3m
python fetch_laptop.py laf-mmo
python build_data.py
python chart.py
python lag_test.py
python summary_draft.py
```

laf-mmo pulls about 1,400 RBI pages and indices-nse about 1,000 NSE files;
each takes 15 to 30 minutes. Older raw files with the same series stay in the
manifest; delete a superseded file and its manifest line before a rebuild.
SUMMARY.md is written by a person from out/SUMMARY_DRAFT.md.

## Rules

- No estimates. A day a source does not publish stays blank. Nothing is
  filled forward or interpolated. data/gaps.md lists every blank trading day.
- Trading calendar = Nifty 50 dates from the NSE daily index files.
- Monthly: LAF and CD use the monthly mean (daily LAF jumps on tax and
  month-end dates); MTF and indices use month-end. A month needs 10 daily
  LAF or CD values. The running month is dropped.
- MTF: indiamtf's openapi.json says BSE starts about 2025-10-15, but its
  file has daily BSE values from 2017-07-03 with no 2025 jump. The test uses
  NSE + BSE; NSE alone is a cross-check.
- NSE index files: some write Index Date month-first (6 to 11 Apr 2023), so
  the date comes from the file name requested, not that column.
- Lag k pairs the money change in month t with the Smallcap 250 return in
  month t+k. Lag 0 is coincident. Only lags 1 to 3 count as a lead.
- Expected sign if money leads: LAF +, CD rate -, MTF +.
- About 45 monthly points: the rough 95% bar is |r| > 0.30. Treat anything
  below it as noise.
