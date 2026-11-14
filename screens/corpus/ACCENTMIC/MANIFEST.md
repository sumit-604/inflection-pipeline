# ACCENTMIC corpus manifest

Accent Microcell Ltd. NSE SME (Emerge) ACCENTMIC; no BSE listing. ISIN INE0Q5D01013.
Ledger written 2026-10-27 for a shallow screen. Card: `screens/cards/ACCENTMIC.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM = housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).

## How it was built

- screener/: `screener_collect.py https://www.screener.in/company/ACCENTMIC/ --output-dir ... --no-drive` under `py -3.14`. Identity confirmed on the screener.in page: "NSE - SME: ACCENTMIC".
- filings/: NSE corporate-announcements API (`index=sme`, symbol ACCENTMIC), 1-Jan-2024 to 27-Oct-2026, filtered by subject. 36 files from `nsearchives.nseindia.com/corporate/`.
- credit-ratings/: screener-linked CARE PDFs and CRISIL HTML rationales, saved as fetched; `.txt` beside each. CRISIL HTML text carries no page markers; cite by file.
- market-data-2026-10-27.md: screener.in company page, a service record.
- Text: PyMuPDF, with Tesseract OCR on near-empty pages, tagged `[OCR]`. Pages with a garbled native text layer carry no marker (see defects).

## Integrity check (2026-10-27)

All 44 PDFs opened with PyMuPDF. Every page's text extracted. Page markers in each `.txt` match the PDF page count. Every PDF ends with `%%EOF` in its last 2 KB. Downloads used `curl -C -` with three retries. Both annual-report file names carry a byte count (NSE `_A_<bytes>_`): 4,996,042 and 5,826,821 bytes, both matched exactly on disk. **No broken file.**

## screener/

| Path | Type | Period | Pages | Status | Notes |
|---|---|---|---|---|---|
| screener/Annual_Report_2026.pdf | Annual report | FY26 | 132 | PART | Read: p.9 (letter), pp.11, 17-19, 23, 28 (capacity, mix, Unit III), pp.39-41 (MD&A, SWOT, ROCE), p.73 (s.186, RPT policy), pp.85-86 (auditor, KAMs), pp.94-96 (balance sheet, P&L, cash flow), p.111 (receivables), pp.117-118 (related parties), p.124 (rights utilisation, contingent liabilities, segments). 6 pages [OCR]. |
| screener/Annual_Report_2025.pdf | Annual report | FY25 | 108 | SKIM | FY25 figures taken from FY26 AR comparatives. |
| screener/Concall_May_2026_Transcript.pdf | Transcript | FY26 call, 16-May-2026 | 27 | FULL to p.19, PART after | Unit III timeline, trading share, margins, realisations. DUP of filings/ACCENT_21052026164310. |
| screener/Concall_Aug_2025_Transcript.pdf | Transcript | Q1 FY26 investor meet, Aug-2025 | 42 | PART | Unit III Oct/Nov-2025 target, RPT land purchase. DUP of filings/ACCENT_13082025174352. |
| screener/Concall_May_2025_Transcript.pdf | Transcript | FY25 call, 17-May-2025 | 36 | SKIM | DUP of filings/ACCENT_20052025173721. |
| screener/Investor_Presentation_1.pdf | Deck | H1 FY27 | 28 | DUP | = filings/ACCENT_15102026155931. |
| screener/Financials.xlsx | screener.in export | n/a | n/a | not used | Service export. |

## credit-ratings/

| File | Agency | Date | Action | Status |
|---|---|---|---|---|
| 01-CRISIL-2026-10-22.html | CRISIL | 22-Oct-2026 | BB-/Stable/A4+, Issuer Not Cooperating (revised; Rs 20.92 crore legacy facilities) | FULL |
| 02-CARE-2026-03.pdf | CARE | 25-Mar-2026 | Upgraded to A-/Stable/A2+ from BBB+/Stable/A2 | FULL |
| 03-CRISIL-2026-02-27.html | CRISIL | 27-Feb-2026 | Prior INC rationale | SKIM |
| 04-CARE-2025-03.pdf | CARE | Mar-2025 | Prior CARE release, BBB+/A2 | SKIM |
| 05-CRISIL-2024-12-27.html | CRISIL | 27-Dec-2024 | Prior INC rationale | SKIM |

## filings/ (36 files)

Substantive, read:
- ACCENT_14102026172349_Unaudited_Financial_Statment (13 pp): H1 FY27 results, balance sheet, cash flow, segments, IPO and rights utilisation. FULL pp.1-8. DUP of ACCENT_14102026110004.
- ACCENT_15102026155931_Investors_Presentation (28 pp): H1 FY27 deck. FULL. 3 image pages [OCR].
- ACCENT_13052026192658_Intimation_For_Unit-III (1 p): Unit III delay and pending approvals. FULL.
- ACCENT_13082026105256_Intimation_for_Wind_turbine (2 pp): 4.45 MW WTG order on Inox Wind. FULL.
- ACCENT_06072026113750_Outcome_of_BM (19 pp): pay-limit increases, new independent director. PART pp.1-2.
- ACCENT_08072026111456_Notice_of_14th_AGM (19 pp): pay ceilings Rs 15 lakh to Rs 25 lakh a month per director. PART pp.2-4, 12-18.
- ACCENT_31072026142306_14th_AGM_Proceedings (3 pp): resolutions passed. FULL.
- ACCENT_30062026104951_Resignation_Chintan_bhatt (3 pp): independent director and NRC chair resigned 29-Jun-2026. FULL.
- ACCENT_21022025202621_Intimation_to_cautionary_letter (2 pp): NSE caution, late board-outcome disclosure. FULL.
- ACCENT_03042026161625_Regulation_31_4_ (2 pp, [OCR]): promoter annual encumbrance declaration. SKIM.
- ACCENT_09062025192505_Letter_of_offer__Right_issue (212 pp, 42 pages [OCR]): rights issue, 7:50 at Rs 135. PART (risk factors pp.25-33 by keyword).

Held, SKIM: FY26 audited results (12-May-2026, 21 pp all [OCR]); H1 FY26 results (14-Oct-2025, 14 of 15 pp [OCR]); FY25 results outcome (12-May-2025); May-2026 deck (21 pp); May-2025 deck (25 pp, 24 [OCR]); statements of deviation (12-May-2026, 16-Oct-2025); RPT filings (04-Oct-2025 NA, 20-May-2025); rating disclosures (18-Mar-2026, 26-Mar-2026 press release, 13-Mar-2025); rights issue outcome, closing and allotment (29-May, 27-Jun, 02-Jul-2025); rights committee and board outcomes (29-Oct-2024, 24-Dec-2024); dividend and re-appointment outcomes (12-May-2026); FY26 call invite (13-May-2026); auditor change outcome (03-Aug-2024).

DUP pairs (md5): ACCENT_14102026110004 = ACCENT_14102026172349; ACCENT_15102026155931 = screener/Investor_Presentation_1; ACCENT_21052026164310 = screener/Concall_May_2026_Transcript; ACCENT_13082025174352 = screener/Concall_Aug_2025_Transcript; ACCENT_20052025173721 = screener/Concall_May_2025_Transcript.

## Reader defects

- H1 FY27 results p.6 (segment PBIT) has a garbled native text layer with no `[OCR]` tag. Unit III PBIT reads "J44.06". The segment total (4,147.77) less Dahej (3,508.15) and Pirana (683.68) gives (44.06), a loss. The card uses the derived figure.
- FY26 audited results and H1 FY26 results are scans read by OCR. The card takes FY26 and FY25 figures from the annual report and the H1 FY27 filing (both native text) instead.

## Gaps (NOT FOUND, with where it was looked for)

- **IPO prospectus (Dec-2023).** Not linked on screener.in (only a SEBI page for a Jun-2024 rights draft). NSE `ipo-detail` and `public-past-issues` APIs return no document link. Three guessed NSE Emerge archive paths returned 404. IPO objects and utilisation are taken from the H1 FY27 filing (p.7) and the deck (p.24). The rights Letter of Offer (Jun-2025) stands in for the business description.
- **H1 FY27 earnings call.** No schedule, recording or transcript in NSE announcements to 27-Oct-2026. Screener's "Oct 2026" concall entry links only the deck. Weakens steps 3, 7, 8.
- **Counterparty of the Rs 17 crore inter-corporate deposit** given in H1 FY27 (results p.5). Not named in any held filing.
- **Promoter selling, Mar to Sep-2026.** Screener shows promoters at 51.40% against 55.47%. No SAST or insider-trading disclosure appears in the NSE corporate-announcements list for 2026. The NSE SAST database was not queried.
- **Unit III approval status after 13-May-2026.** No later Reg 30 update filed. The H1 FY27 deck says approvals are still pending.
- **Wind turbine order value.** Not stated in the 13-Aug-2026 intimation.
- **Revenue split by product and end industry.** Management declined on the May-2026 call (p.12).
