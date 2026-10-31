# Corpus manifest: DHANBANK (Dhanlaxmi Bank Ltd)

NSE DHANBANK | BSE 532180. Ledger written 2026-10-18 for the shallow card `screens/cards/DHANBANK.md`.
Every PDF has a `.txt` beside it with `===== PAGE n =====` markers. Page numbers in the card are PDF pages (AR printed page = PDF page minus 11).
Status key: READ = read in full; READ (pages) = named sections read in full; SKIMMED = scanned for substance; NOT USED.

## Market data
| Path | Type | Status |
|---|---|---|
| market-data-2026-10-18.md | screener.in service record, fetched 2026-10-18: market cap Rs 1,413 cr, price Rs 35.8, book value Rs 38.3, PE 12.2, ROE 7.15%, shareholding Dec-2023 to Sep-2026. NOT a filed document. | READ |

## screener/
| Path | Type | Period | Pages | Status |
|---|---|---|---|---|
| Annual_Report_2026.pdf | Annual report (99th) | FY26 | 173 | READ (pages): cover letter p.1, board p.5, dashboard p.7-8 (read visually), chairman p.9, MD and CEO p.10, directors' report p.12-24, MD&A p.25-38, corporate governance p.39-68, auditor's report and IFC p.72-78, balance sheet, P&L, cash flow p.78-80, NPA movement p.114-117, divergence p.119, gold loans and concentration p.123-124, RBI penalties p.127, business ratios p.131. Other schedules and Basel III Pillar 3 (p.132-163) SKIMMED. Marketing pages p.164-173 NOT USED. |
| Annual_Report_2025.pdf | Annual report (98th) | FY25 | 173 | READ (pages): chairman and MD letters p.9-10 (OCR, quotes only), directors' report p.12-15, rights issue p.13 and p.57-58, board table p.38. Rest SKIMMED by grep. |
| Financials.xlsx / Financials.txt | screener.in export (service record) | FY17-FY26, quarters Mar-2024 to Jun-2026 | n/a | SKIMMED; used only for FY24 PBT and to cross-check filed numbers. Template sheets are empty; only the Data Sheet carries numbers. |

No transcript and no investor presentation are held in screener/.

## filings/ (exchange announcements; prefix DHANBANK_ omitted)
| Path | Type | Date | Pages | Status |
|---|---|---|---|---|
| 02072025131637_Rating | Reg 30: CARE withdraws Tier II rating after redemption | 02-Jul-2025 | 1 | READ |
| 21072025190722_ResultJune | Results Q1 FY26 | 21-Jul-2025 | 8 | SKIMMED (Q1 FY26 figures taken from the Q1 FY27 comparative column) |
| 29092025181256_Outcome | 98th AGM outcome | 29-Sep-2025 | 1 | READ |
| 29102025151514_result | Results Q2 FY26, scanned; pages 2-11 OCR, text unusable | 29-Oct-2025 | 11 | NOT USED (duplicate content) |
| 10122025170724_Results | Results Q2 FY26, a second scan of the same 29-Oct-2025 filing, re-uploaded 10-Dec-2025; text layer garbled | 29-Oct-2025 | 11 | READ visually p.4-5; figures used come from the page images |
| 21012026142634_Decresult | Results Q3 FY26 | 21-Jan-2026 | 10 | READ (p.6-10 notes and segments; P&L via Q4 comparative) |
| 24032026180226_Creditrating | Reg 30: ICRA reaffirms Tier II BBB- (Stable) | 24-Mar-2026 | 1 | READ |
| 28042026141930_Resultmarch2026 | Audited results Q4 and FY26 | 28-Apr-2026 | 14 | READ; p.8 read visually to confirm digits |
| 29072026130743_ResultsJune2026 | Results Q1 FY27 | 29-Jul-2026 | 7 | READ; p.4 read visually to confirm digits |
| 19082026154827_BM | Board outcome: ESOP 2025, up to 2,76,28,919 options | 19-Aug-2026 | 3 | READ |
| 19082026163308_Creditrating | Reg 30: ICRA reaffirms Tier II BBB- (Stable) | 19-Aug-2026 | 1 | READ |
| 23092026192755_Outcome | 99th AGM outcome: accounts, auditors, two independent directors, ESOP 2025 approved | 23-Sep-2026 | 1 | READ |

No investor presentation, analyst-meet material or transcript exists in filings/.

## credit-ratings/
| Path | Agency, action | Date | Pages | Status |
|---|---|---|---|---|
| 01-ICRA.pdf | ICRA: BBB- (Stable) Tier II reaffirmed; FD BBB- and CD A3 assigned | 19-Aug-2026 | 7 | READ |
| 02-ICRA.pdf | ICRA: Tier II BBB- (Stable) reaffirmed | 24-Mar-2026 | 7 | READ (p.1-3) |
| 03-Brickwork.pdf | Brickwork: BB, Issuer Not Cooperating, withdrawn on redemption | 08-Jul-2025 | 5 | READ |
| 04-CARE.pdf | CARE: Tier II rating withdrawn on redemption | 01-Jul-2025 | 3 | READ |
| 05-ICRA.pdf | ICRA: Tier II BBB- (Stable) assigned | 25-Mar-2025 | 7 | SKIMMED (superseded by 01 and 02) |
| 06-CARE.pdf | CARE: BB+ (Stable) reaffirmed | 19-Dec-2024 | 5 | READ |
| manifest.json | Collector log of rating sources | n/a | n/a | READ |

## OCR notes
- AR26: OCR on p.2 and p.172 only (cover art). No numbers used from them.
- AR25: OCR on p.2-5, 7-11 and 162-173. The chairman and MD letters (p.9-10) are OCR; the card takes only a text quote from p.10, no digits.
- Q2 FY26 results: both copies are image scans. The 29102025 copy is tagged OCR on p.2-11. The 10122025 copy is not tagged but its text layer is garbled. Figures were read from the page image (p.4-5).
- Q4 FY26 and Q1 FY27 results are not tagged OCR, but the text layer drops or garbles some digits (for example "3,47" for 3,547 in the tax line). Key pages read visually.

## Documents that exist but are not held
- Earnings call transcripts: none found. The corpus gives no sign the bank holds calls.
- Investor presentations: none held.
- Q2 FY27 results (September 2026 quarter): not yet filed by 2026-10-18 in this corpus.
- Shareholding-pattern filings and any SAST disclosures: not held (screener summary only).
- AGM notice for 23-Sep-2026 with ESOP terms and voting results: not held.
- Pillar 3 disclosures for June 2026 (website only).
- Pre-FY25 annual reports: not held, so governance history before 2024 is NOT FOUND.

## Defects found
1. AR26 performance dashboard (p.8) shows FY26 net NPA as Rs 118 crore (0.51%). The NPA schedule (p.115) and the Q4 FY26 results show Rs 75.40 crore. The dashboard also shows FY24 net NPA as 1.05%, where AR25 p.12 shows 1.25%. Confirmed against the page image.
2. Two files hold the same Q2 FY26 results (29102025151514_result and 10122025170724_Results). The second file name carries the 10-Dec-2025 upload date, but its cover letter is dated 29-Oct-2025.
3. Text layers of the result PDFs garble digits even where not tagged OCR. Treat every result-table number as unverified until read from the image.
4. Return on assets for FY25 appears as 0.41% in AR25 p.12 and 0.40% in AR26 p.12 and the results. Minor.
