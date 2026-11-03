# Corpus manifest: TCPLPACK

Collected 2026-11-04.

## Identity
- Company: TCPL Packaging Ltd (screener name field came back empty in collect.log)
- NSE: TCPLPACK; BSE: 523301; ISIN: not recorded (collector does not capture it)
- Screener: https://www.screener.in/company/TCPLPACK/consolidated/
- Q2 FY27 results due 5-Nov-2026; not yet filed.

## Documents held
Page markers in .txt are `[page n]` (not `===== PAGE n =====`).

| File | Document | Period | Filed | Pages | Text |
|---|---|---|---|---:|---|
| annual-report/Annual_Report_2026.pdf | Annual report | FY26 | - | 309 | OK |
| annual-report/Annual_Report_2025.pdf | Annual report | FY25 | - | 306 | OK |
| results/TCPLPACK-result-Q1FY27-2026-08-11.pdf | Results (BSE) | Q1 FY27 | 2026-08-11 | 7 | OK |
| results/TCPLPACK-result-Q4FY26-2026-05-28.pdf | Results (BSE, AttachHis) | Q4 FY26 | 2026-05-28 | 19 | OK |
| concalls/Concall_Aug_2026_Transcript.pdf | Transcript | Q1 FY27 | Aug 2026 | 18 | OK |
| concalls/Concall_Jun_2026_Transcript.pdf | Transcript | Q4 FY26 | Jun 2026 | 13 | OK |
| concalls/Concall_Feb_2026_Transcript.pdf | Transcript | Q3 FY26 | Feb 2026 | 13 | OK |
| concalls/Concall_Nov_2025_Transcript.pdf | Transcript | Q2 FY26 | Nov 2025 | 13 | OK |
| presentations/Investor_Presentation_1.pdf | Investor presentation (period not checked) | - | - | 18 | OK |
| credit-ratings/01-CRISIL.html/.txt | CRISIL rationale | 21 May 2026 | - | - | text OK (A+/Stable reaffirmed) |
| credit-ratings/02-CRISIL | CRISIL | 11 Sep 2025 | - | - | OK |
| credit-ratings/03-ICRA | ICRA | 27 Aug 2025 | - | - | OK |
| credit-ratings/04-CRISIL | CRISIL | 10 Jul 2025 | - | - | OK |
| credit-ratings/05-CRISIL | CRISIL | 1 Aug 2024 | - | - | OK |
| credit-ratings/06-CRISIL | CRISIL | 9 Jul 2024 | - | - | OK |
| screening/Financials.xlsx | Screener export | - | - | - | n/a |

## Known gaps
- Shareholding pattern: not collected (screener Financials.xlsx only).
- Q2 FY27 results: not yet filed (due 5-Nov-2026).
- Earlier ICRA rating: only Aug 2025 held; no ICRA 2026 link on screener.
- Defects: collector printed empty Company name; fetch_ratings.py BSE-style header needs Origin+Accept (curl with only Referer got Access Denied from api.bseindia.com, python requests with Origin worked); extractor marker is `[page n]`.
