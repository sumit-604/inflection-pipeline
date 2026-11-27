# RATNAVEER corpus manifest

Company: Ratnaveer Precision Engineering Ltd (formerly Ratnaveer Metals Ltd)
NSE: RATNAVEER | BSE: 543978 | ISIN: INE05CZ01011
Screened: 2026-10-18. Card: `screens/cards/RATNAVEER.md`.
Page counts from pdfinfo. Page numbers in the card are PDF pages (the `===== PAGE n =====` markers), not printed folios.
"Read" means read in full. "Skimmed" means navigated by grep and the relevant pages read. Duplicates were identified by md5.

## Documents held

### screener/ (new this run)

| Path | Type | Period / date | Pages | Use |
|---|---|---|---|---|
| screener/Annual_Report_2026.pdf | Annual report | FY26, cover letter 03-Sep-2026, Board's Report dated 20-Aug-2026 | 199 | Read: corporate pages p.3-17, MD letter p.7, MD&A p.33-43, Board's Report p.44-53, annexures A-D p.54-58, secretarial remarks p.51-52, general meetings p.76-77, shareholder info p.82-84, auditor report, KAM, Other Matter, CARO p.89-96, notes p.114-143 (PPE, receivables, other current assets, RPT, geography, note 61A). Consolidated statements skimmed; subsidiary is dormant, figures identical to standalone |
| screener/Annual_Report_2025.pdf | Annual report | FY25 | 141 | Skimmed: Other Matter p.85, PPE note p.110, note 61A p.138, RPT p.133, employees p.51, forex p.56. DUPLICATE of annual-report/Ratnaveer-AR-FY2025.pdf (md5 03f9389c3e) |
| screener/Concall_Nov_2025_Transcript.pdf | Q2 FY26 earnings call, 10-Nov-2025 | First call since listing | 27 | Read. DUPLICATE of concalls/...Q2FY26 and filings/..._13112025140838 (md5 6c1f7eb384) |
| screener/Concall_May_2026_Transcript.pdf | Q4 FY26 earnings call, 14-May-2026 | | 25 | Read. DUPLICATE of concalls/...Q4FY26 and filings/..._21052026175649 (md5 4883e0892e) |
| screener/Investor_Presentation_1.pdf | Q1 FY27 investor deck | July 2026 | 13 | Read. Same text as filings/..._27072026091847 (2.7 MB here, 37.6 MB there; different binaries, identical text layer) |
| screener/Financials.xlsx and .txt | screener.in export | FY20 to FY26, quarters to Jun-2026 | n/a | Data Sheet used for cross-check and FY24 PBT only. Service record, not a filed document. Formula sheets are empty shells |

### filings/ (new this run)

| Path | Type | Date | Pages | Use |
|---|---|---|---|---|
| ..._28072025164633_OBM | Q1 FY26 results, limited review | 28-Jul-2025 | 5 | Skimmed; Emphasis of Matter on tax p.3. Table header misprints "June 30, 2026" |
| ..._03112025161628_OBM-_Signed | Q2 FY26 results | 03-Nov-2025 | 11 | Skimmed; Emphasis of Matter on tax |
| ..._04112025153449_DRAFT_INTIMATION | Newspaper ad, Q2 FY26 | 04-Nov-2025 | 3 | Skimmed (housekeeping) |
| ..._13112025140838_Transcript_Final_signed | Q2 FY26 transcript | 13-Nov-2025 | 27 | DUPLICATE (see screener/) |
| ..._01122025211619_outcome_Final_OCR | QIP opening, floor price Rs 152.46 | 01-Dec-2025 | 2 | Read |
| ..._04122025193942_Intimation_on_Issue_Closing | QIP closing, issue price Rs 145 | 04-Dec-2025 | 1 | Read |
| ..._04122025234225_Intimation_on_Allotment | QIP allotment Rs 185.50 crore, allottees above 5% | 04-Dec-2025 | 3 | Read |
| ..._12122025164940_BM_Outcome | Warrant conversion 20.28 lakh at Rs 143; new warrants proposed | 12-Dec-2025 | 5 | Read p.1-4. p.5 is a garbled image table |
| ..._31012026174241_Out_come_of_BM_Final_Signed | Q3 FY26 results | 31-Jan-2026 | 5 | Skimmed. DUPLICATE of results/Ratnaveer-result-20260131 (md5 f009d9cb26) |
| ..._02022026170801_News_Paper_Publication | Newspaper ad, Q3 FY26 | 02-Feb-2026 | 3 | Skimmed (housekeeping) |
| ..._12032026165806_OBM_S | CCPS conversion; 72.33 lakh warrants at Rs 159.25 to promoter group | 12-Mar-2026 | 4 | Read |
| ..._24042026170611_INTIMATION-CREDIT_RATINGS | Infomerics rating letter, upgrade | 24-Apr-2026 | 9 | Skimmed. p.2-9 are [OCR] scans; content matches credit-ratings/01 |
| ..._28042026165655_BM_Outcome | Rs 330 crore fundraise approval; Seema Sanghavi as ED | 28-Apr-2026 | 4 | Read |
| ..._12052026192208_OBM_OCR_Signed | FY26 audited results, BS, cash flow, warrant conversion | 12-May-2026 | 19 | Read; p.9-10 read visually. DUPLICATE of results/Ratnaveer-result-20260512 |
| ..._12052026193607_OBM_OCR_Signed | Same filing submitted twice | 12-May-2026 | 19 | DEFECT: byte-identical to ..._192208 (md5 a079a81143) |
| ..._12052026201211_Covering_Letter_s | Reg 33(3)(d) unmodified opinion declaration | 12-May-2026 | 1 | Read |
| ..._12052026235258_Presentation_Signed | FY26 results deck (short) | 12-May-2026 | 16 | Read. Chart pages carry no readable numbers. DUPLICATE of presentations/...-b (md5 09cd87950b) |
| ..._14052026144651_Investor_Presentation_Q4FY2026 | Q4 FY26 investor deck | 14-May-2026 | 28 | Read. DUPLICATE of presentations/...-a (md5 5248885375). p.15-16 client logos are [OCR] |
| ..._14052026180859_Intimation_News_Paper_Advertisement | Newspaper ad, FY26 | 14-May-2026 | 3 | Skimmed (housekeeping) |
| team_sandeshc_18052026131418_29 | Reg 31(4) no-encumbrance declaration FY26 | 06-Apr-2026 | 1 | Read |
| ..._21052026175649_Ratnaveer_Transcript_Merged | Q4 FY26 transcript | 21-May-2026 | 25 | DUPLICATE (see screener/) |
| ..._11062026170326_Final_Covering_letter | Board approves Rs 330 crore rights issue | 11-Jun-2026 | 2 | Read |
| ..._20062026180521_Intimation_signed | Analyst plant visit outcome | 20-Jun-2026 | 1 | Read (housekeeping) |
| ..._24062026183715_Outcome_signed | Investor meeting outcome | 24-Jun-2026 | 1 | Read (housekeeping) |
| ..._09072026173308_Intimation_for_Postal_Ballot | Postal ballot: independent director Kashyap Shah | 09-Jul-2026 | 14 | Skimmed |
| ..._10072026171705_Intimation-Signed | Newspaper ad, postal ballot | 10-Jul-2026 | 3 | Skimmed; p.2 [OCR] Gujarati |
| ..._24072026165544_FInalFiles | Q1 FY27 results | 24-Jul-2026 | 9 | DUPLICATE of results/Ratnaveer-result-20260724 (md5 b93c3ed4c2) |
| ..._25072026130056_INTIMATION_News_paper | Newspaper ad, Q1 FY27 | 25-Jul-2026 | 3 | Skimmed (housekeeping) |
| ..._27072026091847_New__FY_26_27_Ratnaveer | Q1 FY27 investor deck | 27-Jul-2026 | 13 | Read. 37.6 MB file |
| ..._27072026092410_Press_release | Q1 FY27 press release | 25-Jul-2026 | 2 | Read |
| ..._29072026160522_OBM_Final_Signed | Q1 FY27 results re-filed with a scanned copy | Letter dated 24-Jul-2026, filed 29-Jul-2026 | 9 | Skimmed; p.2-9 [OCR]; same figures as the 24-Jul filing |
| ..._10092026220128_OBM_10092026 | Rights issue allotment 1.25 crore shares at Rs 264 | 10-Sep-2026 | 2 | Read |
| ..._13092026075550_97c96770-... | Rights issue basis of allotment ad | 12-Sep-2026 | 4 | p.2 read visually (text layer is glyph garbage); p.3 [OCR] Gujarati |

### Older collection folders

| Path | Type | Pages | Use |
|---|---|---|---|
| annual-report/Ratnaveer-AR-FY2025.pdf | FY25 annual report | 141 | DUPLICATE of screener/Annual_Report_2025.pdf |
| concalls/Ratnaveer-Concall-Q2FY26-2025-11-10.pdf | Q2 FY26 transcript | 27 | DUPLICATE |
| concalls/Ratnaveer-Concall-Q4FY26-2026-05-14.pdf | Q4 FY26 transcript | 25 | DUPLICATE |
| presentations/Ratnaveer-InvestorPresentation-Q4FY26-a.pdf | Q4 FY26 deck | 28 | DUPLICATE of filings/..._14052026144651 |
| presentations/Ratnaveer-InvestorPresentation-Q4FY26-b.pdf | FY26 short deck | 16 | DUPLICATE of filings/..._12052026235258 |
| results/Ratnaveer-result-20260131.pdf | Q3 FY26 results (Dec-2025 quarter) | 5 | Skimmed. File name is the filing date, not the quarter end |
| results/Ratnaveer-result-20260512.pdf | FY26 audited results (Mar-2026 quarter) | 19 | Read; p.9-10 read visually. Name is the filing date |
| results/Ratnaveer-result-20260724.pdf | Q1 FY27 results (Jun-2026 quarter) | 9 | Read; p.4-5 read visually. Name is the filing date |
| credit-ratings/01-Infomerics.pdf | Rationale, IVR A-/Stable, A2+ | 28-Apr-2026, 11 pages | Read |
| credit-ratings/02-Infomerics.pdf | Rationale, IVR BBB+/Positive, A2 | 17-Mar-2025, 9 pages | Read p.1-5, rest skimmed |
| credit-ratings/03-Infomerics.pdf | Rationale, IVR BBB+/Stable, A2 | 18-Jan-2024, 9 pages | Read p.1-5, rest skimmed |
| credit-ratings/04-Infomerics.pdf | Rationale, IVR BBB/Positive, A3 (initial) | 15-Jun-2023, 10 pages | Read p.1-5, rest skimmed |
| credit-ratings/manifest.json | Collector log | n/a | All four fetches status 200 |
| market-data-2026-10-18.md | screener.in page | 18-Oct-2026 | Market cap, price, PE, book, shareholding pattern. Service record |

Distinct documents after removing duplicates: about 38 of the 51 PDFs.

## OCR notes

- Pages marked [OCR]: AR FY26 p.2, 88, 144, 198, 199 (covers and dividers); AR FY25 4 pages (covers); Q4 FY26 deck p.15-16 (client logos); short deck p.8, 14, 15 (charts); rating letter 24-Apr-2026 p.2-9; newspaper ads; Q1 FY27 re-filing p.2-9.
- The results PDFs are not marked [OCR] but their text layer is a scan transcript with column order scrambled. Every results figure in the card was read from the page image: results/Ratnaveer-result-20260724.pdf p.4 and p.5; results/Ratnaveer-result-20260512.pdf p.9 and p.10. The Q4 FY26 and Q1 FY27 decks carry the same figures in clean text and agree.
- filings/..._13092026075550 p.2 has a glyph-garbage text layer. The rights basis-of-allotment table was read visually from a rendered crop.

## Documents that exist but are not held

- Q2 FY27 results (Sep-2026 quarter). Not yet filed at the screen date.
- Rights issue Letter of Offer (20-Aug-2026, corrigenda) and any monitoring agency report. Use of the Rs 330 crore is therefore from call commentary only.
- QIP placement document (04-Dec-2025) and preliminary placement document (01-Dec-2025).
- IPO prospectus (September 2023).
- ECMS approval letter (30-Mar-2026) and the Gujarat Electronics Policy in-principle approval (29-Jun-2026).
- Infomerics Annexure 2 lender list (linked from 01-Infomerics.pdf p.9).
- Any shareholding pattern filing under Reg 31; promoter holding after September 2026 rests on the screener.in service record.
- Any Q3 FY26 or Q1 FY27 earnings call transcript. The corpus suggests only two calls were held.
- Financial statements of Ratnaveer Ventures Pvt Ltd and Ratnaveer Industries (promoter entities).

## Defects found

1. filings/..._12052026192208 and ..._12052026193607 are byte-identical (FY26 results filed twice).
2. results/ file names are filing dates (20260131, 20260512, 20260724), not quarter ends as the brief convention states. Contents are Q3 FY26, Q4 FY26 and Q1 FY27.
3. Q1 FY27 results (results/Ratnaveer-result-20260724.pdf p.4) print EPS Rs 10.36 for the quarter. PAT of Rs 182.37 million on 71.62 million shares gives about Rs 2.55. The press release repeats Rs 10.36. Company-side error.
4. Q1 FY27 standalone segment table (p.5) shows Q1 FY26 revenue Rs 2,643.23 million and exports Rs 154.39 million; the P&L shows Rs 2,646.23 million. The consolidated segment table (p.9 text) shows Rs 157.39 million. Rs 3.00 million mismatch, company-side.
5. Q1 FY26 results (filings/..._28072025164633 p.4) head the table "quarter and year ended June 30, 2026". Company-side misprint.
6. AR FY26 p.83 lists "Ratnaveer Precision Engineering Limited" as a promoter group warrant allottee; the March 2026 filing names Ratnaveer Ventures Pvt Ltd. Company-side error.
7. Company-side inconsistencies recorded in the card, step 9: employee count (211, 380, 800+, 1,200, 2,000); foreign exchange earned Rs 2.68 crore against Rs 55.46 crore export sales; founding year 2000 (Q1 FY27 deck) against 2002 (AR).
8. screener/Financials.xlsx formula sheets are empty; only the Data Sheet carries numbers.
