# Corpus manifest: PURPLEWAVE

Collected 2026-11-04.

Identity: Purple Wave Infocom Ltd. NSE symbol: not confirmed. BSE code 544627. ISIN INE0VDK01019. screener.in: https://www.screener.in/company/544627/ . Board (SME vs main board) unresolved: operator says SME, Bull AI says main-board BSE.

| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---:|---|
| inputs/annual-report/Annual_Report_2026.pdf | Annual report (from screener.in) | FY26 | not recorded | 125 | OK (.txt present) |
| inputs/screening/Financials.xlsx | screener.in export | n/a | 2026-11-04 | n/a | spreadsheet |

## Known gaps
- Last two quarterly/half-yearly results: NOT HELD. screener.in supplied none. BSE announcements API (AnnSubCategoryGetData/w, strCat=Result) returned Akamai "Access Denied" from this environment; not retried.
- Concall transcript: none on screener.in (collector warning "No concall transcripts found").
- Investor presentation: none on screener.in (collector warning).
- Credit rating: fetch_ratings.py found no credit-rating links on screener.in page. Not looked for elsewhere.
- Shareholding pattern: not held; not on screener.in download set.
- Annual-report .txt has no "===== PAGE n =====" markers (grep count 0) although extractor reported 125 pages.
