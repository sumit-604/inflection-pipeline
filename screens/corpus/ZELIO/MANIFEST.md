# Corpus manifest: ZELIO

Collected 2026-11-04.

## Identity
- Company: Zelio E-Mobility Ltd.
- BSE code: 544563 (NSE symbol: Zelio per H1/H2 results cover letters; listing board not verified, operator said SME, Bull AI says main-board)
- ISIN: INE1B3501014
- Screener: https://www.screener.in/company/544563/
- Reporting cadence: half-yearly (BSE Result category shows only H1 and H2 filings)

NOTE: the .txt files carry `[page n]` markers, not `===== PAGE n =====` as README states (extract_pdfs.py behaviour).

| File | Document | Period | Filed | Pages | Text |
|---|---|---|---|---:|---|
| annual-report/Annual_Report_2026.pdf | Annual report | FY26 | screener | 105 | clean |
| concalls/Concall_Jun_2026_Transcript.pdf | Concall transcript | Jun 2026 | screener | 15 | ok |
| concalls/Concall_Nov_2025_Transcript.pdf | Concall transcript | Nov 2025 | screener | 21 | ok |
| presentations/Investor_Presentation_1.pdf | Investor presentation | undated (not read) | screener | 32 | ok |
| results/ZELIO-H2FY26-audited-results-2026-05-28.pdf | Audited standalone+consolidated results | H2/FY26 (Mar 2026) | 2026-05-28 | 22 | ok |
| results/ZELIO-H1FY26-results-2025-11-14.pdf | Unaudited standalone+consolidated results | H1 FY26 (Sep 2025) | 2025-11-14 | 14 | ok |
| screening/Financials.xlsx | Screener financials export | n/a | screener | n/a | n/a |

## Known gaps
- Credit rating: NOT FOUND. screener.in Credit ratings block has no links (fetch_ratings.py: "no credit-rating links found"). BSE announcements (last 12 months, all categories) show no rating filing.
- Quarterly results: none exist; company reports half-yearly. H1 FY26 and H2 FY26 held.
- Annual report: only FY26 held (screener offered one).
- Shareholding pattern: not collected (no filing fetched; not in screener download).
- Presentation date not identified from first page; only one presentation supplied.
- BSE API limit: date range cannot exceed 12 months, so filings older than Nov 2025 were not searched.
