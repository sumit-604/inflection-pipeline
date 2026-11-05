# liquidity-smallcap

Does money tightness lead Indian small caps? This tool tests three money
measures against the Nifty Smallcap 250, January 2023 to today:

- RBI net LAF (Liquidity Adjustment Facility), Rs crore. Surplus +, deficit -.
- FBIL 3-month CD (certificate of deposit) rate, %.
- MTF (Margin Trading Facility) book, NSE + BSE, Rs crore.

## Status, 2026-11-05

Code is built and tested end to end on a synthetic fixture (kept out of the
repo). **No real data is in data/ yet.** The cloud shell got a policy 403 on
every source host (RBI, FBIL, NSE, BSE, niftyindices.com, indiamtf.com).
Firecrawl reached indiamtf.com and FBIL pages, but the session's auto-mode
classifier denied the bulk-download calls. So the fetch runs on the laptop,
the same route as tools/macro-regime. data/gaps.md lists every series as
NOT FOUND until then.

## Files

| File | Does |
|---|---|
| fetch_laptop.py | Laptop only. Downloads MTF and index history; registers browser downloads in data/raw/manifest.json |
| build_data.py | data/raw/ to one CSV per series (each row carries source_url and downloaded_on), panel_daily.csv, sources.md, gaps.md |
| chart.py | out/liquidity_smallcap.png and .html: four panels, one date axis, deficit days shaded |
| lag_test.py | Monthly correlation table, lags 0 to 3; rolling 12-month check for failure periods |
| summary_draft.py | Fills the numbers into out/SUMMARY_DRAFT.md; a person then writes SUMMARY.md |

## Laptop runbook

```
pip install -r requirements.txt
python fetch_laptop.py mtf
python fetch_laptop.py indices --start 2023-01-01
```

Two series need a browser download. Save each file in data/raw/, then
register it with the page URL you used:

1. **Net LAF.** RBI DBIE (https://data.rbi.org.in), search "Liquidity
   Adjustment Facility", daily frequency, 01-Jan-2023 to today, export.
   Backup: the daily RBI "Money Market Operations" press releases.
   ```
   python fetch_laptop.py register data/raw/<file> --series laf --url "<DBIE page URL>"
   ```
2. **3M CD rate.** https://www.fbil.org.in, Money Market, CD CURVE tab,
   Choose Date From 01-Jan-2023 To today, Fetch, then csv. If the site caps
   the range, download year by year and register each file.
   ```
   python fetch_laptop.py register data/raw/<file> --series cd3m --url "https://www.fbil.org.in/#/home (CD CURVE)"
   ```

Then build and push:

```
python build_data.py
python chart.py
python lag_test.py
python summary_draft.py
```

build_data.py stops with a message if it cannot tell which LAF column is the
net figure, or which sign it uses. Pass `--laf-col "<name>"` and
`--laf-sign injection_positive` (RBI's convention: injection +, so a deficit
system shows +) or `surplus_positive`. It never guesses a sign.

## Rules

- No estimates. A day a source does not publish stays blank. Nothing is
  filled forward or interpolated. data/gaps.md lists every blank trading day.
- Trading calendar = Nifty 50 dates from niftyindices.com.
- Monthly: LAF and CD use the monthly mean (daily LAF jumps on tax and
  month-end dates); MTF and indices use month-end. A month needs 10 daily
  LAF or CD values. The running month is dropped.
- MTF break: BSE disclosures start about 2025-10-15 (indiamtf openapi.json).
  Before that, "combined" is NSE only. The test uses the NSE book for the
  whole window; the combined book is tested with the break month blanked.
- Lag k pairs the money change in month t with the Smallcap 250 return in
  month t+k. Lag 0 is coincident. Only lags 1 to 3 count as a lead.
- Expected sign if money leads: LAF +, CD rate -, MTF +.
- About 45 monthly points: the rough 95% bar is |r| > 0.30. Treat anything
  below it as noise.
