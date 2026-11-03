# Corpus manifest: GRCL

Attempted 2026-11-04 (headless collector run). 1 document held.

Identity: Gayatri Rubbers and Chemicals Ltd; NSE GRCL; no BSE code; ISIN not recorded (collector log shows "Company:" blank, page content not parsed).

| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---|---|
| inputs/screening/Financials.xlsx | screener.in Financials export | n/a | 2026-11-04 | n/a | spreadsheet |

## Known gaps
- Annual report: NOT FOUND. Collector logged "Could not download annual reports" (screener.in, collect.log).
- Concall transcripts: none downloaded (screener.in).
- Presentations: none downloaded (screener.in).
- Last two quarterly results: NOT FETCHED (no BSE code; BSE API step not attempted).
- Credit rating: NOT FETCHED (earlier fetch_ratings.py found no links; collector did not parse the page).
- Shareholding: NOT COLLECTED.
- Stopped per stuck rule: collector ran but returned only Financials.xlsx and a blank company name.
