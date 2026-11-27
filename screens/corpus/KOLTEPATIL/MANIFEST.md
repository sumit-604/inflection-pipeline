# KOLTEPATIL corpus manifest

Kolte-Patil Developers Ltd. NSE KOLTEPATIL, BSE 532924.
Ledger written 2026-10-26 for the sixth screen run. Card: `screens/cards/KOLTEPATIL.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM = housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).

## How it was built

- screener/: `screener_collect.py https://www.screener.in/company/KOLTEPATIL/consolidated/ --output-dir ... --no-drive` under `py -3.14`.
- filings/: NSE corporate-announcements API, 1-Apr-2025 to 26-Oct-2026, filtered by subject (results, decks, press releases, operational updates, ratings, post-results notices, takeover and SAST filings, Reg 30 notices). 75 NSE files plus one BSE-only file (the 26-Oct-2026 volume-query reply, from BSE `AttachLive/`). Six NSE zips were unpacked, each into its own `<zip name>_unzipped/` folder.
- credit-ratings/: screener-linked CARE PDFs and CRISIL HTML rationales, saved as fetched; `.txt` beside each. CRISIL HTML text carries no page markers; cite by file.
- market-data-2026-10-26.md: screener.in company page, a service record.
- Text: PyMuPDF, with Tesseract OCR on near-empty pages, tagged `[OCR]`.

## Integrity check (2026-10-26)

All 91 PDFs (screener, filings, unzipped and ratings) opened with PyMuPDF, every page's text extracted, page markers in each `.txt` match the PDF page count, and every PDF ends with `%%EOF` in its last 2 KB. All six zips test clean (`unzip -t`). Downloads used `curl -C -` with three retries. **No broken file.** No file name carries a byte count to check against.

## screener/

| Path | Type | Period | Pages | Status | Notes |
|---|---|---|---|---|---|
| screener/Annual_Report_2026.pdf | Annual report | FY26 | 350 | PART | Read: p.4 (highlights), pp.8-9 (rating, history), pp.22-23 (MD letter), pp.58-61 (Directors' report: results, Blackstone deal, NCDs, board changes), p.75 (pay), pp.140-141 (auditor's report, EoM, KAM), p.148 (CARO disputed dues, idle funds), p.181 (loans to related parties). 1 page [OCR]. |
| screener/Annual_Report_2025.pdf | Annual report | FY25 | 345 | SKIM | Not needed beyond FY26 AR comparatives. |
| screener/Concall_Aug_2025_Transcript.pdf | Transcript | Q1 FY26, call 30-Jul-2025 | 14 | PART, DUP | Last call held. Margin lines pp.5-6, 10-11. = filings/KOLTEPATIL_06082025225243. |
| screener/Concall_May_2025_Transcript.pdf | Transcript | Q4 FY25 | 19 | SKIM, DUP | = filings/KOLTEPATIL_31052025162215. |
| screener/Concall_Feb_2025_Transcript.pdf | Transcript | Q3 FY25 | 21 | SKIM | Older than six quarters. |
| screener/Concall_Nov_2024_Transcript.pdf | Transcript | Q2 FY25 | 18 | SKIM | Older than six quarters. |
| screener/Investor_Presentation_1.pdf | Deck | Q1 FY27 | 27 | DUP | = filings/KOLTEPATIL_10082026213359. |
| screener/Financials.xlsx | screener.in export | n/a | n/a | not used | Service export. |

## credit-ratings/

| File | Agency | Date | Action | Status |
|---|---|---|---|---|
| 01-CARE.pdf | CARE | 07-Oct-2026 | NCDs Rs 250 crore, AA-/Stable reaffirmed | FULL |
| 02-CRISIL.html | CRISIL | 25-Mar-2026 | AA-/Stable/A1+ reaffirmed | PART (rationale, drivers) |
| 03-CARE.pdf | CARE | Oct-2025 | Prior CARE release | SKIM |
| 04-CRISIL.html | CRISIL | 29-Sep-2025 | Credit bulletin, bank-facility update only | SKIM |
| 05-CRISIL.html | CRISIL | 25-Mar-2025 | Prior rationale | SKIM |
| 06-CRISIL.html | CRISIL | 16-Aug-2024 | Prior rationale | SKIM |

## filings/ (76 files, plus unzipped folders)

Substantive, read:
- KOLTEPATIL_13102026075428_SubmissionoperationalQ2 (4 pp): Q2 FY27 operational update. FULL.
- KOLTEPATIL_10082026213359_submission_presentation_q1Fy27 (27 pp): Q1 FY27 deck. PART (pp.6-24).
- KOLTEPATIL_10082026171630_Results_Equity (13 pp): Q1 FY27 results; notes p.4; review EoM p.5. 6 pages [OCR]. PART.
- KOLTEPATIL_22052026190102_Result_Presentation_upload (28 pp): Q4 FY26 deck; p.15 financial highlights, p.24 outlook. PART. DUP of KOLTEPATIL_22052026190825.
- KOLTEPATIL_17072026205525, KOLTEPATIL_16042026220436, KOLTEPATIL_14012026190413: Q1 FY27, Q4 FY26, Q3 FY26 operational updates. PART (summary tables).
- Four "Update on the Post-Results Conference Call" notices (KOLTEPATIL_11112025213259, _05022026184319, _22052026214739, _10082026222326): no call held. FULL.
- KOLTEPATIL_06042026211227, _04062026170851, _20062026133318: GST demand order, intimations, show-cause notice. FULL p.2 each.
- KOLTEPATIL_19082026164527 (CEO appointment), KOLTEPATIL_11112025195450 (board and leadership changes), KOLTEPATIL_05022026194749 (MD pay to Re 1), KOLTEPATIL_24082026163822 (ESOP grant). FULL.
- BSE_26102026_Response_to_volume_movement (1 p). FULL.
- team_sandeshc_16092025124413_KOLTE_unzipped/KOLTE.pdf and KOLTE1.pdf: post-offer advertisement and report, offer at Rs 329, 614 shares tendered. [OCR]. FULL.

Held, SKIM: Q2 FY26 results, deck and release (11-Nov-2025); Q3 FY26 results (two DUP copies, 05-Feb-2026), deck and release; Q4 FY26 results and release (22-May-2026); Q1 FY27 board outcome and release; Q4 FY25 and Q1 FY26 decks, releases, results and transcripts; rating letters (01-Oct-2026, 25-Mar-2026, 04-Oct-2025, 30-Sep-2025); Bhugaon press releases; NCD allotment (05-Dec-2025); KPIT merger order (07-Oct-2025); CCI approval (10-Jun-2025); preferential allotment outcome (23-Jun-2025); letter of offer, detailed public statement and public notice zips; BREP and founder SAST disclosures; AMC exit intimation; shareholder communication (07-Jul-2026); ASCR FY26; press releases of 06-Aug and 10-Sep-2026.

DUP pairs (md5): KOLTEPATIL_31052025162215 = screener/Concall_May_2025_Transcript; KOLTEPATIL_06082025225243 = screener/Concall_Aug_2025_Transcript; KOLTEPATIL_05022026172515 = KOLTEPATIL_05022026195335; KOLTEPATIL_10082026213359 = screener/Investor_Presentation_1; KOLTEPATIL_22052026190102 = KOLTEPATIL_22052026190825.

## Gaps (NOT FOUND, with where it was looked for)

- **Transcripts after Q1 FY26.** None exist: the company held no call for Q2 FY26, Q3 FY26, Q4 FY26 or Q1 FY27 (the four notices above). Weakens steps 3, 7, 8.
- **Q2 FY27 financial results.** Not filed on NSE by 26-Oct-2026; only the operational update. Weakens steps 5, 8, 13.
- **Project-level margins.** Not in any FY26 or FY27 deck. Weakens steps 3, 6.
- **FY27 profit guidance.** Not in any deck, release or rationale. Step 13 is Tier D.
- **The "strategic arrangements" behind the MD's Re 1 pay** and the shareholders' agreement of 13-Mar-2025. Referenced (filings/KOLTEPATIL_05022026194749; AR26 p.59), not held.
- **Pledge figure for the founder group.** Not stated in the SAST filings read.
