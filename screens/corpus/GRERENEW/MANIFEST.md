# GRERENEW corpus manifest

GRE Renew Enertech Ltd (formerly GRE Renew Enertech Pvt Ltd, before that GRE Electronics Pvt Ltd).
BSE SME 544682, scrip ID GRERENEW, no NSE listing, ISIN INE0U8P01015. Listed 21-Jan-2026 at Rs 105
(AR26 p.3). Half-yearly reporter. Promoters Kamleshkumar D Patel, Kirtikumar K Suthar, Mukeshkumar P
Trivedi; promoter group 68.59% at Sep-2026 (market-data-2026-10-30.md).
Ledger written 2026-10-30. Card: `screens/cards/GRERENEW.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM =
housekeeping, checked for substance; DUP = byte-identical to another held file (md5 checked).
Page numbers are PDF page numbers. In AR26 one PDF page carries two printed pages (PDF p.13 =
printed pp.20-21).

## How it was built

- screener/: screener.in public page links (https://www.screener.in/company/544682/consolidated/),
  resolved to BSE `AttachHis/` PDFs, 2026-10-30. `Annual_Report_2026.pdf` is BSE attachment
  6bc7169c (Reg 34(1) annual report FY26, filed 03-Sep-2026). `Investor_Presentation_Jun_2026.pdf`
  is BSE attachment b1df4168 (filed 29-Jun-2026). No transcripts exist on screener.in.
- results/: screener.in quarter links. `q-2026-03.pdf` resolved to BSE attachment 2dc84559 and is
  md5-identical to filings/20260523_6661ec78 (DUP). `q-2025-09` and `q-2025-03` failed (link
  returned the BSE announcements HTML page, 16,901 bytes, not a PDF).
- filings/: BSE announcements listed through the bseindia.com form in the in-app browser, windows
  30/10/2025-30/10/2026 (54 rows, page 1 of 2 read to 21-02-2026) and 30/10/2025-20/02/2026 (4 rows),
  per `work/bse/GRERENEW.txt`. Housekeeping dropped. 38 attachments downloaded from
  `xml-data/corpfiling/AttachHis/`. File name = filing date + first 8 characters of the attachment.
  First filing in the list is 04-Feb-2026 (listing period).
- credit-ratings/: `tools/collector/fetch_ratings.py` over the one link on the screener.in page:
  CRISIL rationale of 31-Jul-2026 (HTML plus text). No ICRA file.
- prospectus/: `PROSPECTUS_GRERENEW_DRHP_20240928.pdf`, from
  https://www.bseindia.com/corporates/download/360109/GRE_Final%20DRHP_28.09_QR_Final_20240928201217.pdf.
  The September 2025 draft (bsesme.com `GRE_DRHP_29.09.2025_6PM_QR_20250929185545.pdf`) failed three
  times: two ConnectTimeouts on www.bsesme.com and one non-PDF on the bseindia.com mirror. The final
  prospectus of 16-Jan-2026 was not fetched.
- market-data-2026-10-30.md: screener.in company page, a service record, about 09:00 IST.
- Financials.xlsx: absent this run (collector browser could not start).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check (from fetch-ledger-2026-10-30.jsonl)

Every downloaded file has status OK and a byte size equal to the exchange-declared size. 42 PDFs
held: 38 filings, 2 screener, 1 results, 1 prospectus. OCR pages: deck 8 of 34, 20260801_4d03d570
6 of 7, 20260626_2e5a383e 3 of 5, DRHP 1 of 469; all others 0. DUP sets (md5): 20260204_15d754dc =
20260204_74ed10eb; filings/20260523_6661ec78 = results/q-2026-03.

Defects found by the analyst:
- **Scanned pages without an `[OCR]` tag.** FY26 res pp.3-19 and the auditor letters (AudRes1
  pp.3-5, AudRes2 pp.3-7) carry a text layer with misread digits and no tag (the ledger shows 0 OCR
  pages). Examples in FY26 res: p.18 "41,310.35" for 1,310.35; p.6 "3175" for 3.75; p.8 cash flow
  "936.27" for an arithmetic 836.37. The card reads FY26 res p.15 and AudRes1 p.3 from the page image.
- **Sign inconsistency in the standalone cash flow (FY26 res p.8).** "Decrease/(Increase) in Short Term
  Loans & Advances" prints +1,254.32 lakh while the balance sheet shows an increase; the subtotal
  (-824.37) uses the negative sign. Not used in the card; the consolidated statement (p.17) is used.
- **Two copies of the auditor resignation.** AudRes2 repeats AudRes1 pp.1-5 and adds the SEBI
  information form (pp.6-7). Different md5, same substance.

## Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| FY26 res | filings/20260523_6661ec78 | H2 and FY26 audited, filed 23-May-2026, Rs lakh | 21 | FULL | 1-2 (outcome, IPO variation), 3-10 (standalone report, P&L, BS, CF, segments, notes), 11-19 (consolidated), 15 from page image, 20-21 (Reg 33 declarations). Period on p.1 and p.15 confirmed |
| AR26 | screener/Annual_Report_2026.pdf | FY26, AGM 25-Sep-2026 | 69 | PART | 3-10 (highlights, order book, KPIs, MD letter, strategy), 11-17 (board, directors' report, CFO history, subsidiaries, auditors, ICD, subsequent events), 21-24 (MD&A, ratios), 27 (AOC-1, pay), 28-30 (auditor report, CARO, keyword pass), 39-42 (standalone notes 15-37, RPT), 55 (consolidated note 20, loans to Hasmukh Patel), 57 (consolidated RPT) |
| Deck | screener/Investor_Presentation_Jun_2026.pdf | June 2026 | 34 [8 OCR] | FULL | 1-34; OCR pages are title and logo slides |
| DRHP | prospectus/PROSPECTUS_GRERENEW_DRHP_20240928.pdf | Draft red herring prospectus, 28-Sep-2024, STALE | 469 [1 OCR] | PART | 4 (contents), 25-34 (summary: objects, shareholding, litigation, RPT, cost of acquisition, bonus), 53 (top ten 61.46%), 167 (top ten customers), 186-187 (DK USA, GRE Green), 214-215 (group company), 369 (DK USA licences) |
| AudRes1 | filings/20260815_9bb575c5 | Statutory auditor resignation, 14-Aug-2026 | 5 | FULL | 1-5; p.3 from page image |
| AudRes2 | filings/20260817_447fd021 | Resignation resubmitted with SEBI information form | 7 | FULL | 1-7 |
| CFO | filings/20260827_29f8adde | CFO resignation 27-Aug-2026, effective 05-Sep-2026 | 3 | FULL | 1-3 |
| Board-Sep | filings/20260902_1630bdc9 | Board outcome 02-Sep-2026 | 9 | FULL | 1-9 (CFO noted, new auditor, internal auditor, Rs 2,000 crore RPT limits, WTD) |
| AudApp | filings/20260903_a76869cd | Manubhai & Shah LLP appointed to casual vacancy | 2 | FULL | 1-2 |
| IA | filings/20260903_a39e936c | Internal auditor Ashvin K. Yagnik & Co., FY27 | 2 | FULL | 1-2 |
| AGM-N | filings/20260903_20a4ac29 | AGM notice (AR extract) | 17 | PART | 2-4 (resolutions), 10-14 (RPT and auditor explanatory statements), 16 |
| AGM | filings/20260925_fd5075d9 | AGM proceedings 25-Sep-2026 | 3 | FULL | 1-3 |
| Subs | filings/20260831_d796bdec | Solarsource and Solarcatch incorporated | 2 | FULL | 1-2 |
| Solarium | filings/20260630_12bea780; 20260701_65e208b1 | Rs 175 crore LOA and EPC agreement | 2 / 2 | FULL | 1-2 each |
| PR | filings/20260716_f5cd7ed5 | Press release, order book Rs 224 crore | 3 | FULL | 1-3 |
| OB-Jul | filings/20260716_905fad63 | Orders 1-15 Jul, order book Rs 248 crore | 2 | FULL | 1-2 |
| Orders | filings/20260226_f98c60a0, 20260325_767efe4f, 20260504_5274374a, 20260520_d2f70ee6, 20260702_7de360ed, 20260818_de42d9bb, 20260905_02f183e0, 20260917_8620460a, 20261003_9e41e14f, 20261017_2ee016b8 | Order intimations Feb to Oct 2026 | 2-3 each | FULL | all |
| Reg32 | filings/20260523_4aaaf518 | IPO use statement and auditor certificate, Mar-2026 | 7 | FULL | 1-7 |
| Mehsana | filings/20260221_7fcd5ef7 | Mehsana Dairy project transfer, Rs 4.06 crore | 2 | FULL | 1-2 |
| Comm | filings/20260603_caecf7be; 20260603_1c3c1641 | 7.20 MW AC and 1.5 MW AC plants commissioned | 1 / 1 | FULL | 1 each |
| CR | filings/20260801_4d03d570 | CRISIL rating intimation | 7 [6 OCR] | SKIM | 1; rationale read from CRISIL |
| CRISIL | credit-ratings/01-CRISIL.txt | BBB-/Stable, A3, 31-Jul-2026 | - | FULL | all |
| PB | filings/20260525_f197fa61; 20260626_2e5a383e | Postal ballot on IPO variation, result | 17 / 5 [3 OCR] | SKIM | resolution text; scrutiniser pp.1-3 |
| MD | market-data-2026-10-30.md | screener.in, 30-Oct-2026 | - | FULL | market cap, price, shareholding |

Housekeeping, SKIM: 20260204_15d754dc and _74ed10eb (Reg 30(5) KMP list, DUP), 20260221_1dfacf8d
(internal auditor FY26), 20260221_ae52d307 (secretarial auditor), 20260401_e0eaf359 (IR agency),
20260625_6523b64d (GRE Foundation), 20260708_7b7d59c3 (interview link).

## Gaps (NOT FOUND, with where it was looked for)

- **Final prospectus (16-Jan-2026) and September 2025 revised draft.** bsesme.com timed out; would come
  from bsesme.com or the lead manager's site. Promoter, group-company and restated FY25 claims rest on
  the stale 2024 draft.
- **H1 FY27 results.** Not filed to 30-Oct-2026; BSE announcements.
- **H1 FY26 standalone filing** (screener link failed); H1 figures taken from FY26 res comparatives.
- **AGM 25-Sep-2026 voting results and scrutiniser report**, including the vote on the new auditor; BSE.
- **New CFO appointment.** None in the BSE list to 30-Oct-2026.
- **Fee of the new auditor.** Not in AudApp or AGM-N p.14.
- **Shareholding pattern, Reg 29, insider-trading disclosures** (dropped as housekeeping). The promoter
  fall from 69.99% to 68.59% has no filing in the corpus. Pledge NOT FOUND.
- **Terms and security of the Rs 6.96 crore loans to Hasmukh Patel and Laxmi Vishnu Corporation.**
  AR26 p.55 gives balances only.
- **Solarium order execution period and margin.** Solarium p.2 says "as per the terms" only.
- **FY26 customer concentration.** Not in AR26 pp.13-24, 39-42; FY24 figures from DRHP only.
- **Order filings for 16-31 May, 1-15 Jun and 16-31 Jul 2026.** Not in the BSE list; nil orders or not filed.
- **Concall transcripts.** None exist.
- **Financials.xlsx.** Absent this run.
