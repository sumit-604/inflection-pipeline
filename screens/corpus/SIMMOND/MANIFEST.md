# SIMMOND corpus manifest

- Company: Simmonds Marshall Ltd.
- NSE symbol: none (BSE only). BSE code: 507998. ISIN: INE657D01021
- Screener: https://www.screener.in/company/507998/
- Built: 2026-11-04

## Documents held

| File (under inputs/) | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---|---|
| annual-report/Annual_Report_2026.pdf | Annual report | FY26 | screener.in | 173 | extracted |
| annual-report/Annual_Report_2025.pdf | Annual report | FY25 | screener.in | 177 | extracted |
| results/Q1FY27_Jun2026.pdf | Financial results (standalone and consolidated) | Quarter ended 30 Jun 2026 | 2026-08-07 (BSE, AttachHis) | 11 | UNREADABLE: scanned; only page 2 has text (cover note). Financial tables pages 3-11 not extracted. OCR attempted, failed (see gaps) |
| results/Q4FY26_Mar2026.pdf | Results for year ended 31 Mar 2026 (Q4) | Quarter/year ended 31 Mar 2026 | 2026-05-14 (BSE, AttachHis) | 16 | extracted |
| credit-ratings/01-CRISIL.html/.txt | CRISIL rating rationale | 3 Jul 2026 | - | - | extracted |
| credit-ratings/02-CARE.pdf/.txt | CARE rating press release | 2 Mar 2026 (URL dated 202603) | - | 6 | extracted |
| credit-ratings/03-CRISIL.html/.txt | CRISIL rationale | 5 Sep 2025 | - | - | extracted |
| credit-ratings/04-CRISIL.html/.txt | CRISIL rationale | 30 Aug 2024 | - | - | extracted |
| credit-ratings/05-CRISIL.html/.txt | CRISIL rationale | 20 Jun 2023 | - | - | extracted |
| credit-ratings/06-CRISIL.html/.txt | CRISIL rationale | 4 Jul 2022 | - | - | extracted |
| screening/Financials.xlsx | screener.in export | - | - | - | extracted (Financials.txt) |

## Known gaps

- Q1FY27 results PDF is scanned. tools/ocr_repair.py ran (with PYTHONUTF8=1) but every page failed with FileNotFoundError (OCR binary, likely tesseract or poppler, not found); text file holds pages tagged OCR:embedded-CORRUPT. Needs OCR tooling installed, then re-run.
- Concall transcripts: none (screener.in reported none found).
- Investor presentations: none (screener.in reported none found).
- Shareholding: not collected as a separate document; only what is in Financials.xlsx and the annual reports.
- Filings (inputs/filings): empty; none sought.
- Annual report filed dates not recorded.
- Collector defect: log shows "Company:" blank for this URL.
- ocr_repair.py crashes with UnicodeEncodeError (cp1252) unless PYTHONUTF8=1 is set.
- BSE announcements API rejects date ranges over 12 months.
