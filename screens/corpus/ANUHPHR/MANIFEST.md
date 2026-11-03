# Corpus manifest: ANUHPHR

Collected 2026-11-04. PDFs have a .txt beside them with '[page n]' markers.

Identity: Anuh Pharma Ltd. | NSE ANUHPHR | BSE 506260 | ISIN INE489G01022 | screener.in /company/ANUHPHR/ (standalone page; see defects)

| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---:|---|
| annual-report/Annual_Report_2025.pdf | Annual report | FY25 | n/a | 149 | OK |
| annual-report/Annual_Report_2026.pdf | Annual report | FY26 | n/a | 151 | OK |
| concalls/Concall_Aug_2021_Transcript.pdf | Concall transcript | Aug 2021 | - | 9 | OK |
| concalls/Concall_Nov_2021_Transcript.pdf | Concall transcript | Nov 2021 | - | 10 | OK |
| concalls/Concall_Feb_2022_Transcript.pdf | Concall transcript | Feb 2022 | - | 20 | OK |
| concalls/Concall_May_2022_Transcript.pdf | Concall transcript | May 2022 | - | 5 | OK |
| presentations/Investor_Presentation_1.pdf | Investor presentation | undated (screener) | - | 31 | OK |
| results/ANUHPHR-result-2026-08-07-cf454222-....pdf | Unaudited results | Q1 FY27 (30 Jun 2026) | 2026-08-07 | 3 | OK (poor text quality, first line shows OCR-like noise) |
| results/ANUHPHR-result-2026-10-30-0ace46ce-....pdf | Unaudited results | Q2/H1 FY27 (30 Sep 2026) | 2026-10-30 | 5 | OK |
| results/ANUHPHR-result-2026-11-01-e531eec8-....pdf | Newspaper publication of Q2 results | Q2 FY27 | 2026-11-01 | 3 | OK |
| credit-ratings/01..06-ICRA.html/.txt | ICRA rating-update pages (15 Sep 2025, 3 Jan 2025, 28 Dec 2023, 20 Oct 2022, 19 Aug 2021, 29 Oct 2020) | various | - | 0 | UNREADABLE as rationale: all six .txt are the identical ICRA JS page shell (5,560 B), no rationale text |
| screening/Financials.xlsx | Screener export | - | - | - | xlsx |
| screening/Financials.txt | Tab-separated dump, sheets marked '===== SHEET name =====' | - | - | - | OK |

## Known gaps
- Credit rating: ICRA rationale text NOT FETCHED (6 links held as shell pages only; needs browser render). Rating letters on BSE not searched.
- Transcripts: none newer than May 2022 on screener; Q1/Q2 FY27 transcripts not found.
- Presentation: one undated presentation only; no FY26/FY27 decks.
- Filings: none collected.
- Shareholding: no separate document; only in annual report and Financials sheets.
- Collector defect: the URL given (/consolidated/) has no Export to Excel button for this company (standalone only), so Financials.xlsx was NOT downloaded and "Company:" printed blank; rerun on /company/ANUHPHR/ succeeded. First-run log: collect.log; second: collect2.log.
- Reader defect: extract_pdfs writes '[page n]' markers, not '===== PAGE n ====='.
- BSE: strCat=Result returned 0 rows; strCat=-1 with filtering on headline worked.
