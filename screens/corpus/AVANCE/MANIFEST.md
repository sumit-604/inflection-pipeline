# Corpus manifest: AVANCE

Collected 2026-11-04. Text files sit beside each PDF (page markers '[page n]' or '===== PAGE n =====').

## Identity
- Company: Avance Technologies Ltd.
- NSE: AVANCE; BSE: 512149; ISIN: INE758A01072
- Screener: https://www.screener.in/company/AVANCE/

## Documents held
| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---:|---|
| inputs/annual-report/Annual_Report_2025.pdf | Annual report | FY25 | screener | 139 | OK |
| inputs/annual-report/Annual_Report_2026.pdf | Annual report | FY26 | 2026-09-07 | 140 | OK |
| inputs/results/AVANCE-Q1FY27-results-2026-08-11.pdf | Unaudited results | Q1 FY27 (Jun 2026) | 2026-08-11 | 10 | OK |
| inputs/results/AVANCE-Q2FY27-results-2026-11-02.pdf | Unaudited results | Q2 FY27 (Sep 2026) | 2026-11-02 | 18 | UNREADABLE: scanned; only cover letter (page 1) extracted. OCR attempt via tools/ocr_repair.py failed on 17 pages (FileNotFoundError, OCR binary missing on this machine) |
| inputs/screening/Financials.xlsx | Screener export | - | 2026-11-04 | - | n/a |
| inputs/screening/Financials.txt | Tab-separated dump of Financials.xlsx, sheets marked '===== SHEET name =====' | - | - | - | OK |

Results source: BSE AnnSubCategoryGetData (strCat=Result), AttachLive.

## Known gaps
- Concall transcripts: none. screener.in reported none; none on screener.
- Investor presentations: none. screener.in reported none.
- Credit rating: none. fetch_ratings.py found no credit-rating links on screener.in.
- Q2 FY27 results text: scanned PDF, UNREADABLE until OCR tooling (tesseract/pdf rasteriser) is installed; ocr_repair.py failed with FileNotFoundError.
- Shareholding: no shareholding sheet in Financials.xlsx; not collected.
- Filings: none collected (not requested beyond results).
