# Corpus manifest: TASTYBITE

Collected 2026-11-04. Each PDF has a .txt beside it with '[page n]' markers (not '===== PAGE n =====').

## Identity
- Company: Tasty Bite Eatables Ltd. (screener page: https://www.screener.in/company/TASTYBITE/consolidated/)
- NSE: TASTYBITE; BSE: 519091; ISIN: not recorded (screener collector returned empty company name)

| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---:|---|
| annual-report/Annual_Report_2026.pdf | Annual report | FY26 | n/a | 236 | ok |
| annual-report/Annual_Report_2025.pdf | Annual report | FY25 | n/a | 217 | ok |
| results/TASTYBITE-Q1FY27-2026-08-12.pdf | Quarterly results (BSE API) | Q1 FY27 (Jun 2026) | 2026-08-12 | 4 | ok per check_extraction, but text only 1.5 KB (cover letter; results pages may be image-only) |
| results/TASTYBITE-Q4FY26-2026-05-29.pdf | Results (BSE API) | Q4 FY26 / year ended Mar 2026 | 2026-05-29 | 11 | ok |
| concalls/Concall_Feb_2023_Transcript.pdf | Concall transcript | Feb 2023 | n/a | 13 | ok |
| concalls/Concall_Aug_2021_Transcript.pdf | Concall transcript | Aug 2021 | n/a | 26 | ok |
| presentations/Investor_Presentation_1.pdf | Investor presentation (undated) | not identified | n/a | 27 | ok |
| credit-ratings/01-ICRA ... 06-ICRA (.html/.txt) | ICRA rating pages, screener updates 6 Jun 2023, 25 Jan 2023, 5 May 2022, 30 Mar 2021, 11 Mar 2020, 28 Dec 2018 | 2018-2023 | n/a | 0 | SHELL: all six .txt are byte-identical (ICRA page navigation, 5,560 B); no rationale text |

## Known gaps
- Financials.xlsx: NOT collected. Collector warned "Export to Excel button not found"; company name printed empty. Looked for: screener.in consolidated page.
- Credit rating: only ICRA page shells, newest screener entry 6 Jun 2023; rationale content NOT FETCHED (needs browser render). No rating letters on BSE fetched.
- Transcripts: only Feb 2023 and Aug 2021 held; no transcript for FY26/FY27 quarters on screener.
- Presentation: one undated presentation; no Q4FY26 / Q1FY27 deck.
- Annual report: FY26 and FY25 held, filed dates unknown.
- Quarterly results: screener supplied none; fetched from BSE API (strCat=Result). Q1FY27 text thin (see above).
- Shareholding pattern: not collected; looked for on screener only via collector (no such class).
- Filings: none held.
