# Corpus manifest: CREDENT (two collections, merged 2026-11-04)

Two runs collected documents for this company. Both ledgers are kept below. Files from the 2026-10-30 run sit in the top-level category folders; files from the 2026-11-04 run sit under inputs/.

## Collection of 2026-11-04

### Corpus manifest: CREDENT

Collected 2026-11-04.

#### Identity
- Company: Credent Connect N Care Ltd (screener.in /company/CREDENT/, standalone and /consolidated/ both resolve)
- NSE symbol: CREDENT (NSE SME only). BSE code: none. ISIN: INE1KPX01025 (from operator)
- Screener URL: https://www.screener.in/company/CREDENT/

#### Documents held
| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---:|---|
| inputs/screening/Financials.xlsx | Screener export | FY23-FY26 annual, quarters sheet | 2026-11-04 | n/a | binary |
| inputs/screening/Financials.txt | Tab-separated dump of every sheet of Financials.xlsx (written by this run) | same | 2026-11-04 | n/a | text; values are on the "Data Sheet" tab, other tabs are formula shells with no cached values |

No PDFs held.

#### Known gaps
- Annual report FY26: NOT HELD. Screener link: https://archives.nseindia.com/annual_reports/SME_AR_31744_CREDENT_2025_2026_A_4289822_07092026182348.pdf (NSE returns HTTP 403 to curl and python requests; browser-based bypass was declined by the permission classifier).
- Last two results: NOT HELD (H1 FY27 filed 28-Oct-2026, H2 FY26 ~May 2026). H1 FY27 NSE links: https://nsearchives.nseindia.com/corporate/CREDENT_28102026190226_FinalOutcomeBM.pdf and .../CREDENT_28102026191521_PressFinal.pdf (403). Company is NSE-only, so the BSE announcements API does not apply. H2 FY26 link not on the screener page.
- Transcript: NOT HELD. Screener lists only intimation/audio-recording PDFs on nsearchives (CREDENT_24102026114001_Earning_call.pdf, CREDENT_29102026185245_Audio_Recording_Of_Earnings.pdf, both 403) and an mp3 link (https://ccreservations.com/recordings/data/10047705.mp3, not fetched, audio).
- Presentation: NOT HELD. https://nsearchives.nseindia.com/corporate/CREDENT_28102026210652_Investor_presentation.pdf (403).
- Credit rating: NOT FOUND. Screener page has no rating documents (looked on the screener page only).
- Shareholding: not in corpus as a document; only whatever the Financials.xlsx holds.
- Defect: screener_collect.py downloads AR/concall/presentation links with a plain requests session; links on this company point to nseindia.com, which returns 403, so the collector prints "Could not download annual reports" and "No concall transcripts found" (the latter is a misleading message: links exist, only the download fails). It also prints an empty "Company:" because get_company_name_from_html reads the first <h1>, which on this page has the name in a nested element (page <title> does hold it).
- Possible fix: operator downloads the six NSE PDFs in a normal browser and drops them in the matching inputs/ folders; then run extract_pdfs.py.

## Collection of 2026-10-30

### CREDENT corpus manifest

Credent Connect N Care Ltd (formerly Credent Connect N Care Pvt Ltd, formerly Credent Cold Chain Logistics Pvt Ltd).
NSE Emerge (SME) symbol CREDENT, no BSE listing, ISIN INE1KPX01025 (Pros p.6). Listed 20-Aug-2026 after a Rs 93.90 crore
fresh issue at Rs 189 (Pros p.2). Half-yearly reporter. Promoters: Ashok Kumar Sharma, Karan Sharma, Tarun Sharma, Dimple
Sharma, Tanveen; 87.52% pre-issue (Pros p.167), 63.75% at Sep-2026 (market-data, service record).
Ledger written 2026-10-30. Card: `screens/cards/CREDENT.md`.

Status key: FULL = read in full; PART = key sections read, rest navigated by keyword; SKIM = checked for
substance. Page numbers are PDF page numbers. In the prospectus, PDF page = printed page + 4.

#### How it was built

- **Exchange route refused.** NSE refused scripted downloads (HTTP 403) and the in-app browser (Access Denied) on
  30-Oct-2026. The ledger records four 403 failures: the FY26 annual report on `archives.nseindia.com`, the
  28-Oct-2026 investor presentation on `nsearchives.nseindia.com`, and the two screener.in quarter links (Sep-2026 and
  Sep-2025) that resolve to NSE. No exchange announcement list exists for this corpus. No BSE listing exists, so the
  BSE announcements route used in earlier runs does not apply.
- screener/: the FY26 annual report linked from the public screener.in page was taken from the company's investor page,
  `https://c3logistics.co.in/Downloads/Annual%20Reports/Annual%20Report%20C3%20Final.pdf`, 2026-10-30. Its size,
  4,289,822 bytes, equals the size encoded in the refused NSE archive file name (`..._A_4289822_...`). No transcripts
  or decks are held.
- prospectus/: `https://c3logistics.co.in/Downloads/Offer%20Document/Prospectus.pdf` (Prospectus dated 18-Aug-2026,
  314 pages).
- filings/: from the company's investor page, not the exchange:
  `.../Downloads/Financial%20Results/Financial%20Results%20H1%202026-27.pdf` (curl single pass, no resume);
  `.../Downloads/Material%20Documents/17%20SPA_CMC_Team_Alltrak.pdf`;
  `.../Downloads/Material%20Documents/9.%20Report%20Medical%20Diagnostics%2031%20July%202026.pdf` (IPO material
  documents list). File names are the operator's, not exchange attachment names.
- credit-ratings/: none. No rating is linked on screener.in, and Pros p.66 states no credit rating exists.
- market-data-2026-10-30.md: screener.in consolidated company page, a service record.
- Financials.xlsx: absent (the screener collector's browser could not start in this environment).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

#### Integrity check (from the fetch ledger, 2026-10-30)

All five downloaded PDFs have status OK, and each byte count matches the declared size where one was declared. Page
counts: AR26 121, Pros 314, SPA 90, D&B 63, H1-27 27. OCR pages: 76 of 90 in the SPA; none elsewhere.
`dup-sets-2026-10-30.json` is empty: no md5 duplicates.

Defects found by the analyst:
- **H1-27 is a scan with a garbled native text layer and no `[OCR]` tags** (pp.4-7, 10-12 and 26-27 carry numbers).
  Every figure the card uses was read from the page image: pp.10, 11, 12, 13, 25, 26, 27. Example: the text layer reads
  consolidated cash "741972 / 22102"; the image reads 7,419.72 and 221.02 (Rs lakh).
- **H1-27 p.7 (standalone notes)** says "half year ended 30th September, 2025" for the current period. A typo; the
  consolidated notes on p.13 read 2026.
- **H1-27 p.26 utilisation table** totals Rs 21.65 crore in "during the period" and Rs 21.13 crore in "end of the
  period". The rows sum to Rs 21.65 crore.
- **Pros p.149** gives 100,000 CHPL shares bought; the SPA (pp.4-5, 16-17) sells 4,999 shares per seller at
  Rs 5,72,50,000 each. The rupee total, Rs 11.45 crore, agrees.
- **AR26 pp.13-14** compare FY26 with unrestated audited FY25 (revenue Rs 8,182.32 lakh, PAT Rs 553.23 lakh), while Pros
  p.55 shows restated FY25 (Rs 7,794.26 lakh, Rs 224.67 lakh). The reconciliation is in Pros p.189.
- **SPA OCR** is noisy; the consideration on p.5 was read from the page image.

#### Substantive files, read

| Short name | Path | Period / date | Pages | Status | Pages read |
|---|---|---|---|---|---|
| H1-27 | filings/20261028_Financial-Results-H1-FY27.pdf | H1 FY27, board 28-Oct-2026; H2 FY26, H1 FY26, FY26 comparatives | 27 | FULL | 1-3 (outcome, CEO, internal auditor), 4-7 (standalone balance sheet, P&L, cash flow, notes), 8-9 (standalone review), 10-13 (consolidated balance sheet, P&L, cash flow, notes incl. 80JJAA credit; images), 14-16 (consolidated review, Alltrak other auditor), 17-23 (NFRA policy, SKIM), 24-27 (IPO utilisation certificate and annexures; images). Period on p.1 and p.11 confirmed |
| Pros | prospectus/PROSPECTUS_CREDENT_Prospectus_2026.pdf | Prospectus, 18-Aug-2026 | 314 | PART | 2-4 (cover, issue, contents), 6 (ISIN), 24-37 (risk factors 1-24: concentration, receivables, subsidiary losses, seasonality, ROC discrepancies, cash flow, disqualification, emphasis of matter, guarantees), 55-62 (restated P&L, cash flow, contingent, RPT summary), 66 (no credit rating), 71-78 (capital structure, allotments, holders, promoter build-up), 87-93 (objects, working-capital projections, loans, issue expenses), 119-133 (business), 145-151 (history, SPAs, subsidiaries), 155-162 (management, pay; keyword), 167-172 (promoters, promoter group, dividend), 189-190 (restatement reconciliation), 198 (bank stock statement), 227-236 (MD&A, capitalisation), 237-240 (litigation), 250 (no group company) |
| AR26 | screener/Annual_Report_2026.pdf | FY26 | 121 | PART | 3-14 (about, chairman, MD&A, KPIs), 35 (loans, RPT policy), 40-43 (board and committee meetings), 50-51 (AOC-2), 61-62 and 94-95 (auditor reports, KAM unbilled revenue), 66 and 100 (audit trail), 85 (standalone receivables ageing, revenue and cost notes; image), 91 and 118 (contingent liability) |
| SPA | filings/2026_SPA_CMC_Team_Alltrak.pdf | SPAs for CMC (now CHPL) 02-Apr-2025, Credent Team, Alltrak | 90 [76 OCR] | PART | 1-5 and 14-18 (CMC SPAs, consideration; p.5 image), 32-37 and 45-50 (Team and Alltrak terms, keyword) |
| D&B | filings/20260731_Report-Medical-Diagnostics.pdf | Commissioned industry report, 31-Jul-2026 | 63 | SKIM | 1-3 (title, disclaimer, contents), company profile around the "Company Profiling" section. Not used for any card number |
| MD | market-data-2026-10-30.md | screener.in, fetched 30-Oct-2026 | - | FULL | Market cap Rs 692 crore, price Rs 380, PE 27.1, Sep-2026 shareholding |

Housekeeping files: `fetch-ledger-2026-10-30.jsonl` (FULL), `dup-sets-2026-10-30.json` (empty), the `.txt` beside each PDF.

#### Gaps (NOT FOUND, with where it would come from)

- **Exchange announcement list.** NSE refused the API and the in-app browser on 30-Oct-2026. Missing with it: Reg 30
  filings (the CFO change from Karan Sharma to Sachin Sharma, listing and allotment notices, lock-in details), the
  Sep-2026 Reg 31 shareholding pattern (only the screener.in service record is held), and the H1 FY27 Reg 23(9)
  related-party disclosure. Source: NSE Emerge corporate announcements for CREDENT.
- **Earnings-call transcript.** None in the corpus. Source: NSE announcements or the company's investor page.
- **Investor presentation, 28-Oct-2026.** Linked on screener.in; NSE returned HTTP 403
  (`CREDENT_28102026210652_Investor_presentation.pdf`). Source: NSE archive or the company's investor page.
- **Standalone H1 FY26 results document.** The screener.in Sep-2025 link resolved to NSE and returned 403. H1 FY26
  figures come from the H1-27 comparatives.
- **Credit rating.** None exists (Pros p.66). CARE Ratings is the IPO monitoring agency only (H1-27 p.25); its
  monitoring report is not held.
- **Customer names and per-client revenue.** Not disclosed (Pros pp.24-25, 120, 235; AR26 p.14).
- **Price per sample, volumes, organic split of H1 FY27 growth.** Not in any held document.
- **Unbilled revenue amount inside consolidated receivables at 30-Sep-2026.** Not in H1-27; AR26 p.85 gives the
  standalone March figure only (Rs 396.15 lakh).
- **Subsidiary annual reports (CHPL, Alltrak, Credent Team).** Not held; the prospectus gives KPI summaries only
  (Pros pp.27, 121).
