# JYOTISTRUC corpus manifest

Jyoti Structures Ltd. NSE JYOTISTRUC, BSE 513250, ISIN INE197A01024, face value Rs 2.
Power transmission line and substation EPC contractor, Mumbai; out of insolvency under an
NCLT-approved resolution plan implemented 9-Nov-2021; no identifiable promoter.
Ledger written 2026-10-29. Card: `screens/cards/JYOTISTRUC.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked);
IMG = scanned page read as a page image with the Read tool because the OCR text was unusable or
the page carried only a signature block and was not OCR'd. Page numbers are PDF page numbers.
In AR26 the printed page number is three lower than the PDF page (AR26 PDF p.16 = printed p.13).

## How it was built

- screener/: `tools/collector/screener_collect.py https://www.screener.in/company/JYOTISTRUC/ --output-dir screens/corpus/JYOTISTRUC/screener --no-drive`
  under `py -3.14`, 2026-10-29. Two annual reports (FY25, FY26) and Financials.xlsx. No transcripts
  or decks exist on screener.in. Financials.xlsx is a service export and is never cited.
- filings/: BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a
  bseindia.com page in the in-app browser because scripted calls to both NSE and BSE returned
  Access Denied on 2026-10-29. Windows of 12 months or less; the ledger runs from 04-Nov-2024 to
  28-Oct-2026 and lists 105 announcements (a first pull of 91 rows missed the 15-Oct-2025 to
  04-Mar-2026 window through a pagination error; the orchestrator re-pulled it on 29-Oct-2026
  and added 14 files). Housekeeping categories dropped (board-meeting intimations, newspaper
  publications, trading-window closures, Reg 74(5), investor complaints, shareholding patterns,
  Reg 7(3), Reg 40, ESOP allotments filed as such, record dates, large-corporate forms,
  secretarial compliance). 103 attachments downloaded from `xml-data/corpfiling/AttachLive/`,
  falling back to `AttachHis/`, with `curl -C -` and three retries; two ledger rows (28-May-2025
  Financial Results and 26-Aug-2025 Outcome) share the date and byte size of a held file and were
  not downloaded separately. File name = filing date + BSE attachment name.
- credit-ratings/: `tools/collector/fetch_ratings.py` found no agency link on the screener.in
  page; no folder was created.
- market-data-2026-10-29.md: screener.in company page, a service record (prices are the
  28-Oct-2026 close).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (2026-10-29, run by the orchestrator)

All 91 PDFs of the first pull (2 screener, 89 filings) opened with PyMuPDF. Every page's text
was extracted, page markers in each `.txt` match the PDF page count, and every file ends with
`%%EOF`. 276 filing pages and 10 screener pages carry `[OCR]`. 3 md5 duplicate sets, listed in
`dup-sets-2026-10-29.json`. **No broken file.** The 14 filings added later on 29-Oct-2026 carry
`.txt` with OCR where native text was under 40 characters; they were read for the card but were
not part of the integrity run.

Reader note: in the results filings the P&L pages are scans that carry a digital-signature text
block of more than 40 characters, so OCR did not run on them and the `.txt` shows only the
signature. Those pages were read as images (status IMG below).

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| AR26 | screener/Annual_Report_2026.pdf | FY26, Directors' report dated 20-Jul-2026 | 193 | PART | 3-4 (highlights, board), 6, 8-10 (WTD letter, Plant 2), 12, 15-30 (Directors' report: results, order book, orders, capacity, board, KMP, CSR, risk, auditors, remuneration), 32-33 (secretarial audit), 40, 42, 47-48 (board holdings, remuneration, price data, shareholding), 53-55 (MD&A, BRSR), 78-79, 84-86 (auditor's report, EoM, KAM, CARO), 89-90 (BS, P&L), 98-101 (notes 9-26), 105, 115, 125, 128-131 (ratios, notes 27-41, AOC-1). DUP = filings/20260722_c9a0f8e0 |
| AR25 | screener/Annual_Report_2025.pdf | FY25 | 177 | PART | 3, 5-6 (CEO and WTD letters), 14 (orders in hand, plant). DUP = filings/20250820_9cbcbf55 |
| FY26 res | filings/20260430_274c1ede-... | Q4 and FY26 audited, filed 30-Apr-2026 | 20 | FULL | 2 (standalone P&L, IMG), 3-4 (cash flow, BS, OCR), 6-7 (consol), 8-19 (audit reports) |
| FY26 PR | filings/20260430_02e7c200-... | FY26 press release | 3 | FULL | 1-3 |
| Q1 res | filings/20260804_7581090e-... | Q1 FY27 unaudited, filed 04-Aug-2026 | 12 | FULL | 2 (standalone P&L, OCR and IMG), 3 (consol), 4-11 (review reports) |
| Q1 PR | filings/20260804_becbb9ab-... | Q1 FY27 press release | 3 | FULL | 1-3 |
| Q2 res | filings/20251112_494c5ade-... | Q2 and H1 FY26 unaudited, filed 12-Nov-2025 | 16 | PART | 2 (standalone P&L, IMG), 3 (H1 balance sheet, IMG), 4 (H1 cash flow, IMG), 6, 13 (review-report other matters, OCR). Outcome 20251112_4df23f32 SKIM |
| Q2 PR | filings/20251113_6f34709f-... | Q2 FY26 press release | 3 | FULL | 1-3 |
| Q3 res | filings/20260123_5e3e2a98-... | Q3 and 9M FY26 unaudited, filed 23-Jan-2026 | 12 | PART | 2 (standalone P&L, IMG); pages 3-12 are scans carrying only signature blocks in `.txt`, not read. Outcome 20260123_afeb4e61 SKIM |
| Q3 PR | filings/20260123_a4c61441-... | Q3 FY26 press release | 3 | FULL | 1-3 |
| Q3 FY25 res | filings/20250203_5f3ac75b-... | Q3 and 9M FY25 | 8 | PART | 2 (standalone P&L, OCR). DUP of the board outcome under 20250203_f0c2c47c and 20250210_603523e0 |
| FY25 PR | filings/20250528_7f42b0e5-... | FY25 press release, order book | 3 | FULL | 1-3 |
| LOF | filings/20250211_19a22f3a-... | Rights issue Letter of Offer, Feb-2025 | 391 | PART | 2, 5, 24, 28, 34-35 (risk factors, concentration), 70-79 (resolution plan, investors, objects), 83-84 (NFB need), 167, 173-176 (business, capacity, subsidiaries, projects) |
| MAR | filings/20260804_5c90f20e-... | Monitoring agency report, Rights Issue II, Q1 FY27 | 10 | PART | 3-9 (objects, utilisation, delay) |
| MAR-D | filings/20260123_a604426f-... | Monitoring agency report, Rights Issue II, Dec-2025 quarter | 10 | PART | 7-9 (utilisation: LC/BG margins, salaries and vendors) |
| MAR-S, MAR-I | filings/20251112_bb5c5680-...; 20251112_de4c3596-... | Monitoring agency reports, Sep-2025 quarter, Rights Issue II and Rights Issue I | 10; 11 | PART | 6-8; 4-9 (cost of objects, delay note, share price note) |
| NCLT-3, Appeal | filings/20260218_328f2065-...; 20260227_c76f2593-... | NCLT contempt order of 16-Feb-2026 directing release of NFB limits; lenders' NCLAT appeal | 1 each | FULL | all |
| LILO | filings/20260223_f34a4e3d-... | 400 kV Pirana LILO completed and charged | 1 | FULL | 1 |
| COO | filings/20260205_20bb894c-...; 20260205_23a82d36-... | COO appointment and press release | 2; 3 | FULL / SKIM | all; 1 |
| Nasik | filings/20250221_b3a49d29-... | Plant 2 restart, orders in hand | 1 | FULL | 1 |
| Rights, Rights PR | filings/20250318_76c10c55-...; 20250319_7ed37ded-... | Basis of allotment; subscription press release | 1; 2 | FULL | all |
| Orders 2025 | filings/20250123_b52561a3; 20250225_e1617527; 20250811_7eea023b; 20251015_bf978123 | PGCIL Khavda; Adani Boisar; Rs 639 crore PR; AESL Bhadla | 1-2 each | FULL | all |
| Orders 2026 | filings/20260330_4ae7dcb3; 20260513_e199eacf; 20260514_8773d2db; 20261023_d76bd1aa; 20261023_b5848248; 20261026_f165510c; 20261026_fab0099c; 20261028_9cdd5b1b; 20261028_909b4c65 | AEML; Sri Lanka JV and PR; GETCO and PR; PGCIL TL01/TL02 and PR; PGCIL TL05 and PR | 1-3 each | FULL | all |
| Commissioning | filings/20260304_5479cd05-... | 400 kV Gadag-II completed | 1 | FULL | 1 |
| NCLT-1, NCLT-2, NCLAT | filings/20250707_c69e039e; 20251013_a4179d43; 20260527_0b19e6b2 | Applications against WBSEDCL and NFB lenders; NCLAT order of 26-May-2026 allowing the lenders' appeal | 1 each | FULL | all |
| OTS, NCD-OTS | filings/20250218_0ed164ea; 20250618_4b4fb00f | OTS authorisation; settlement of 1,149 NCDs | 1; 2 | FULL | all |
| Warrants | filings/20250528_ec07ce58; 20250618_34006ee3 | Conversions at Rs 13.20 | 3 each | FULL | all |
| ESOS | filings/20250425_b0fce4a5; 20250930_ab79e225 | Allotments; cancellation of 5,02,333 shares | 3; 5 | FULL | all |
| Management | filings/20250826_176be840; 20260529_6308ec08; 20260717_ac6226ba; 20261015_a3b7cd35; 20261015_fa867403; 20260804_fc089588 | CEO extension; CEO resignation; chairman's demise; CFO change and new director; internal auditor removal | 1-4 each | FULL | all |
| Board outcomes | filings/20241122_9a95ad59; 20241125_39743950; 20260430_8c21f505; 20260720_4fa6f621; 20260721_3675780a | Rights approval; FY26 outcome; authorised capital | 1-26 | PART | 1-7 of 20260430 (auditor appointments); rest full |
| SAST | filings/20241104_5B7A77B1...; 20241104_1E056811... | Aion Jyoti and Apollo Jyoti sales, Oct-2024 | 2 each | PART | 1 |
| Clarification | filings/20250710_803aae0c-... | Reply to BSE price-movement query | 1 | FULL | 1 |
| Corrigendum | filings/20260727_d3b70c62-... | AR26 CSR committee correction | 2 | FULL | 1-2 |
| AGM 2026 | filings/20260722_131d9815-... | 51st AGM notice | 11 | SKIM | 2, 8-9 (authorised capital item) |

Held, SKIM or not opened beyond page 1: Q2 FY25 and Q1 FY26 results and board outcomes (figures
taken from later comparatives), Q2 and Q3 FY26 board outcomes, FY25 integrated filing and
outcome, monitoring agency reports for Q2 FY25 to Jun-2025 and Mar-2026, EGM and AGM voting
results, BRSR FY25 and FY26, auditor appointments
(tax, cost, secretarial, internal), related-party disclosure, record date, rights-issue
committee outcomes and corrigendum, rights-issue closing extension.

DUP sets (md5): 20250203_f0c2c47c = 20250210_603523e0 (Q3 FY25 outcome and integrated filing);
20250820_9cbcbf55 = screener/Annual_Report_2025.pdf; 20260722_c9a0f8e0 =
screener/Annual_Report_2026.pdf.

## Gaps (NOT FOUND, with where it was looked for)

- **Q2 FY27 result.** Not filed by 29-Oct-2026.
- **Q3 FY26 review report and balance sheet detail.** Pages 3-12 of filings/20260123_5e3e2a98
  are scans whose `.txt` holds only signature blocks; only the P&L page was read as an image.
  The Dec-2025 expected-credit-loss provision is therefore NOT FOUND (Sep-2025 Rs 13.00 crore and
  Jun-2026 Rs 15.25 crore are held).
- **Credit rating.** None. No agency named in AR26, AR25 or the 91 ledger entries; screener.in
  lists no rating link; CARE Ratings appears only as monitoring agency for the rights issues
  (LOF, p.79). Step 10 is NOT FOUND.
- **Concall transcripts and investor presentations.** None on screener.in or in the ledger.
- **The NCLT-approved resolution plan and the current instalment schedule** after the
  exclusions sought from the NCLT. Only the LOF extract (pp.71-72) and AR26 notes 27-29 are held.
- **Status of the non-fund limits** after the 26-May-2026 NCLAT order. No later filing.
- **Completion of the Adani Boisar-Pune line** (18 months from Feb-2025). No filing.
- **Quarterly cash flow and order-book figures.** The company files neither; the order book is
  disclosed once a year and in press releases.
- **Life of the tax shield.** No note in AR26 states the unabsorbed losses or their expiry.
