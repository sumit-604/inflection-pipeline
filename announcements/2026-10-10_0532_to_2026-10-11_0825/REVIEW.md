# REVIEW.md: filing evidence file for the window 10 Oct 2026 05:32 to 11 Oct 2026 08:25 IST

Job: brief-2026-10-11. Written on 11 Oct 2026 (Sunday). This is the technical evidence file behind BRIEF.md. One entry per distinct filing event. Every figure carries its source and the source's date.

Provenance tiers used in every entry:

- [FILED] stated in the exchange filing itself. Page numbers refer to the PDF page.
- [MGMT] a statement by the company or its management (press release quote, concall answer, MD letter).
- [AGENCY] a credit rating agency document.
- [RECORD] your Notion export (COMPANIES MASTER and sub-pages), the single source of truth about your view. Quoted with the date of the entry.
- [SECONDARY] an aggregator (screener.in) or trade press.
- [INFERENCE] my own arithmetic or reading. Never filed. Labelled each time.
- NOT FOUND means the fact is not in any document I could read. The entry says where it would be found.

## 0. Counts and what was read

| Item | Count |
|---|---|
| Feed items listed in INDEX.md for the window | 37 |
| Files in the window folder | 34 PDFs plus 1 NSE zip (.bin) |
| PDFs read | 35 (34 PDFs, plus the 1 PDF inside the Yaap zip). The zip also holds 1 NSE XBRL file, read |
| Pages read | 156 (155 in the 34 PDFs plus 1 in the zip) |
| Pages with no text layer | 37 pages, in 6 PDFs (Aequs 2, Fedbank CHRO letter 1, Hexaware 17, Karnika 13, TIPCO 2 plus 2 in the byte-identical copy). All 37 were OCR'd with tesseract at 300 dpi |
| PDFs with no text at all | 0 (page 1 of every PDF has text) |
| Items with no PDF | 2: item 2 Aarti Pharma (rating update) and item 24 Poonawalla Fin (rating update). Both documents were found on the web (CRISIL, 9 Oct) and read. See E03 and E30 |
| Duplicate postings collapsed | 7 (see section 5). 37 feed items become 30 distinct events |
| Companies in the window | 28 |
| Companies on your list (found in the Notion export) | 14 |
| Companies not on your list (not found in the export) | 14 |
| Companies in held.txt that appear in the window | 0 |
| Prices refreshed from screener.in | 28 of 28 (14 on your list, 14 not) |
| Prices not refreshed | 0 |

Outside the window, read to fill gaps (section 6): 5 PDFs from the previous window's folder in the same zip (Bajel order filing naming the customer, Hexaware vote report of 20 pages, India Glycols price clarification, Aequs Ajna JV filing, Aarti board notice), 3 documents fetched from the exchange and company sites (Yaap 8-Oct board outcome, Aequs 8-Oct Amansa disclosure, Quality Power website corrigendum) and 2 CRISIL web pages. All are labelled wherever used. They are not counted in the 35 PDFs.

### 0.1 Things in the zip that were not part of the window

The zip also carried a second folder (2026-10-09_0500_to_2026-10-10_0532, 60 files) and, inside the window folder, files I did not write: INDEX.md, REVIEW.md, companies.json, text/, deep/ and page_images/. I did not use them as evidence. I extracted and read every PDF myself. I used INDEX.md only for the feed item numbers and the two items that have no PDF. After finishing, I compared my findings with the older REVIEW.md. The comparison is in section 7.

## 1. Method and limits

1. pdftotext -layout on every page. A page with fewer than 15 words was rendered at 300 dpi and OCR'd. Where a number mattered (Karnika results, Premier results, Aequs table, TIPCO letter, Hexaware execution date), I opened the page image and read the number by eye.
2. Notion export: 265 rows in COMPANIES MASTER (CSV) and 406 pages. A company is "on your list" only if it has a row or a page of its own. A name that appears only inside another company's page (Deep Industries inside the South West Pinnacle page, Aurionpro inside eMudhra) is "not on your list". I note the mention where it helps.
3. Each filing was tested for: a warning line (what the record calls a tripwire), a thesis-broken condition, a promised date, the entry zone or margin of safety price, and a monitoring item. The result is the line "touches a rule: yes/no, which".
4. Prices: screener.in company page, Current Price field. The page does not print a trade date. The pages were read on Sunday 11 Oct 2026 between 11:02 and 11:05 IST. Markets are closed at weekends, so the figures are the last close, expected to be Friday 9 Oct [INFERENCE]. The filings in this window were made on Friday evening and Saturday, so none of the prices has reacted to them.
5. Screener code used: the export ticker first. Three needed a different code. Aarti PharmaLabs: export says AARTIPHARMA, which does not load; AARTIPHARM does. Oswal Pumps: export says OSWAL; OSWALPUMPS loads. TIPCO: export says TIPCO; the BSE code 544740 (the link on your own page) loads.
6. No cloud BullAI. Where a document was missing I tried to fetch it. Seven facts sit in documents I could not fetch (section 7). Each has a screener.ai prompt in BRIEF.md where it matters.

## 2. Prices

### 2.1 Companies on your list

| Company (on your list) | Status on file | Price now (₹) | 52w high / low (₹) | Mcap (₹ Cr) | Read at (IST) | Price on file (₹) and its date | Change | Buy level on file | Price vs top of buy zone |
|---|---|---|---|---|---|---|---|---|---|
| TIPCO Engineering | WATCHLIST / AVOID | 304 | 337 / 76.5 | 631 | 11-Oct 11:03:22 | 296; 22-Sep-26 close (Screener, per Key Notes 23-Sep); properties show 296 | +2.7% | Entry Price Max 111; MoS 99 | 2.74x |
| Oswal Pumps | WATCHLIST | 254 | 779 / 251 | 2,900 | 11-Oct 11:03:16 | 274; 22-Sep-26 close (Screener, per Key Notes); properties 274 | -7.3% | body ₹350-435 (April); Key Notes 23-Sep: no entry price set; properties blank; MoS 406 | 0.58x |
| Yaap Digital | AVOID | 116 | 214 / 113 | 244 | 11-Oct 11:03:25 | 198; Jul-26 (record says stale) | -41.4% | none on file; MoS none | n/a |
| Aequs | not set | 274 | 295 / 113 | 18,343 | 11-Oct 11:02:55 | 242.87; 22-Sep-26 close (Bajaj Finserv, secondary, per Key Notes) | +12.8% | none (model unsigned); MoS none | n/a |
| ADF Foods | WATCHLIST / AVOID | 290 | 347 / 153 | 3,183 | 11-Oct 11:02:48 | 273.1; 01-Oct-26 (Trendlyne, per Key Notes) | +6.2% | Entry Price Max 204 (body 205); AVOID above 268; MoS 181 | 1.42x |
| Cyient DLM | not set | 952 | 1,015 / 265 | 7,560 | 11-Oct 11:03:02 | 923; 10-Sep-26 close (Screener, per Key Notes) | +3.1% | none (no valuation run); MoS none | n/a |
| Fedbank Financial | WATCHLIST / AVOID | 146 | 178 / 119 | 5,492 | 11-Oct 11:03:04 | 164; Jul-26 run (record also logs ~157 on 23-Aug) | -11.0% | Entry Price Max 77 (zone 68-77); MoS 61 | 1.90x |
| Quality Power | WATCHLIST | 1,547 | 1,681 / 581 | 11,984 | 11-Oct 11:03:18 | 1513.4; 24-Sep-26 11:18 NSE (secondary, per Key Notes) | +2.2% | Entry zone 456-570; MoS 456 | 2.71x |
| Fractal Analytics | AVOID | 708 | 1,120 / 698 | 12,285 | 11-Oct 11:03:06 | 861; Aug-26 (Key Notes 31-Aug: CMP ~861) | -17.8% | Entry 275, watchlist trigger 400; MoS 220 | 2.57x |
| Airfloa Rail | WATCHLIST / AVOID | 566 | 594 / 246 | 1,356 | 11-Oct 11:02:57 | 315; Jul-26 run (still quoted 29-Sep) | +79.7% | Entry Price Max 193 (zone 146-193); MoS 155 | 2.93x |
| Bajel Projects | WATCHLIST / AVOID | 157 | 216 / 135 | 1,820 | 11-Oct 11:02:59 | 177; May-26 analysis (still on properties) | -11.3% | Entry Price Max 92 (zone 74-92); MoS 74 | 1.71x |
| Garware Hi-Tech | WATCHLIST | 6,998 | 7,990 / 2,691 | 16,257 | 11-Oct 11:03:09 | 7015.5; 01-Oct-26 last trade (Trendlyne, per Key Notes) | -0.2% | Entry Price Max 3,437 (refresh to 4,500-5,700 pending); MoS 2750 | 2.04x |
| India Glycols (residual) | WATCHLIST / AVOID | 330 | 400 / 168 | 2,209 | 11-Oct 11:03:11 | 307.4; 01-Oct-26 (Trendlyne, per Key Notes) | +7.4% | properties 429 (pre-demerger); body: residual ~91-105; MoS 222 | 3.14x |
| Aarti PharmaLabs | WATCHLIST | 856 | 1,002 / 584 | 7,758 | 11-Oct 11:02:52 | 901; 22-Sep-26 (analysis date) | -5.0% | none on file; MoS none | n/a |

Notes. (a) "Price vs top of buy zone" divides today's price by the top of the entry zone on file. (b) For Oswal Pumps the entry zone on the page body (₹350 to ₹435) conflicts with the 23 Sep Key Notes ("no entry price is on file; set one after H1 FY27") and with the blank Entry Price Max property. (c) For India Glycols the Entry Price Max property (₹429) and MoS property (₹222) are pre-demerger numbers; the body gives a residual zone of about ₹91 to ₹105 from the 25 Aug value study. (d) For ADF Foods the properties say ₹204 and ₹181, the body says ₹205 and ₹182; the page already lists this as a ruling pending.

### 2.2 Companies not on your list (for context only)

| Company (not on your list) | Price now (₹) | 52w high / low (₹) | Mcap (₹ Cr) | Screener page used | Read at (IST) |
|---|---|---|---|---|---|
| Aurionpro | 602 | 1,247 / 593 | 3,325 | /company/AURIONPRO/ | 11-Oct 11:03:27 |
| Chemplast Sanmar | 215 | 413 / 161 | 3,394 | /company/CHEMPLASTS/ | 11-Oct 11:03:29 |
| Deep Industries | 746 | 827 / 327 | 4,777 | /company/DEEPINDS/ | 11-Oct 11:03:31 |
| Fairchem | 749 | 847 / 428 | 943 | /company/FAIRCHEMOR/ | 11-Oct 11:03:34 |
| Heritage Foods | 390 | 504 / 292 | 3,620 | /company/HERITGFOOD/ | 11-Oct 11:03:36 |
| Hexaware | 538 | 808 / 400 | 32,903 | /company/HEXT/ | 11-Oct 11:03:38 |
| Karnika | 125 | 182 / 90.2 | 777 | /company/KARNIKA/ | 11-Oct 11:03:41 |
| Poonawalla | 447 | 545 / 361 | 39,389 | /company/POONAWALLA/ | 11-Oct 11:03:43 |
| Premier Polyfilm | 103 | 107 / 38.0 | 1,077 | /company/PREMIERPOL/ | 11-Oct 11:03:45 |
| Rathi Steel | 19.8 | 29.0 / 13.5 | 171 | /company/504903/ | 11-Oct 11:03:47 |
| Shilpa Medicare | 1,022 | 1,096 / 260 | 19,983 | /company/SHILPAMED/ | 11-Oct 11:03:49 |
| Steamhouse | 128 | 133 / 91.5 | 3,535 | /company/STEAMHOUSE/ | 11-Oct 11:03:51 |
| Tanfac | 3,146 | 3,648 / 1,633 | 6,807 | /company/TANFACIND/ | 11-Oct 11:03:53 |
| Tinna Rubber | 886 | 1,322 / 527 | 1,596 | /company/TINNARUBR/ | 11-Oct 11:03:56 |

## 3. File accounting: every PDF, its feed item and its entry

| # | File (as downloaded) | Feed item | Entry | Pages | Pages with no text layer (OCR) | MD5 (first 8) |
|---|---|---|---|---|---|---|
| 1 | ADF_Foods_Announcement_Under_Regulation_30_LODR_-__1b2db7.pdf | 1 | E21 | 2 | none | 567c020e |
| 2 | Aequs_Disclosures_under_Reg_311_and_312_of_SEB_7a01a5.pdf | 3 | E15 | 3 | 2,3 | 3f78859b |
| 3 | Airfloa_Rail_Announcement_under_Regulation_30_LODR-Pr_43f7a8.pdf | 4 | E02 | 3 | none | c1f6c3cd |
| 4 | Airfloa_Rail_Signing_Of_MOU_With_KTK_Group_Co_Ltd_a3a6bd.pdf | 5 | E02 | 2 | none | c08a5fd0 |
| 5 | Aurionpro_Sol_Announcement_under_Regulation_30_LODR-An_ff9842.pdf | 6 | E28 | 2 | none | 83efb8b0 |
| 6 | Bajel_Projects_Announcement_under_Regulation_30_LODR-Pr_392ab9.pdf | 7 | E01 | 2 | none | 88fa795f |
| 7 | Chemplast_Sanmar_Announcement_under_Regulation_30_LODR-Ac_45c719.pdf | 8 | E09 | 4 | none | c195680a |
| 8 | Cyient_DLM_Announcement_under_Regulation_30_LODR-An_4c79b7.pdf | 9 | E25 | 2 | none | d408c394 |
| 9 | Deep_Industries_Rating_update_fd5228.pdf | 10 | E07 | 7 | none | 0212819e |
| 10 | Fairchem_Organic_Board_Meeting_Intimation_for_Unaudited_F_8f10d3.pdf | 11 | E29 | 1 | none | 60ca5d2b |
| 11 | Fedbank_Financi_Announcement_under_Regulation_30_LODR-An_54b43b.pdf | 13 | E26 | 1 | none | ea25fc6f |
| 12 | Fedbank_Financi_Announcement_under_Regulation_30_LODR-An_99c20a.pdf | 12 | E26 | 2 | none | a3364ba1 |
| 13 | Fedbank_Financi_Announcement_under_Regulation_30_LODR-Ch_7c5877.pdf | 14 | E19 | 3 | 3 | d05c6d9c |
| 14 | Fedbank_Financi_Board_Meeting_Intimation_for_Considerati_f63622.pdf | 15 | E27 | 1 | none | 5f3ddd3e |
| 15 | Fractal_Analyt_Change_In_Chairman_Of_The_Board_Of_The_C_e7a20d.pdf | 16 | E20 | 2 | none | 8b0036c5 |
| 16 | Garware_Hi_Tech_Announcement_under_Regulation_30_LODR-Co_fc5d83.pdf | 17 | E16 | 4 | none | c5c2efa9 |
| 17 | Heritage_Foods_Update_On_Acquisition_Of_560_Equity_Shar_67af73.pdf | 18 | E10 | 1 | none | b60804bc |
| 18 | Hexaware_Tech_Restated_And_Amended_Trust_Deed_8d58bf.pdf | 19 | E13 | 18 | 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18 | 80a2540d |
| 19 | India_Glycols_Intimation_Of_GST_Order_b94904.pdf | 20 | E22 | 2 | none | 9bd5c5e2 |
| 20 | Karnika_Industri_Outcome_of_Board_Meeting_4f1a1d.pdf | 21 | E04 | 14 | 2,3,4,5,6,7,8,9,10,11,12,13,14 | 2b783498 |
| 21 | Oswal_Pumps_Adoption_Of_New_Line_Of_Business_And_Var_243c45.pdf | 23 | E11 | 7 | none | 01db4a4e |
| 22 | Oswal_Pumps_Announcement_under_Regulation_30_LODR-Pr_80d914.pdf | 22 | E11 | 4 | none | 96feed56 |
| 23 | Premier_Polyfilm_Board_Meeting_Outcome_for_Board_Meeting__f1151a.pdf | 26 | E05 | 8 | none | 947b44a2 |
| 24 | Premier_Polyfilm_UNAUDITED_FINANCIAL_RESULTS_FOR_THE_QUAR_636eac.pdf | 25 | E05 | 8 | none | 44a70c19 |
| 25 | Quality_Power_El_Corrigendum_To_The_Notice_Of_The_Extra-O_6ecded.pdf | 27 | E12 | 2 | none | 1d16e7fb |
| 26 | Rathi_Steel_Disclosure_Under_Regulation_30_Of_Listin_3ed8b0.pdf | 28 | E23 | 2 | none | 7b489247 |
| 27 | Shilpa_Medicare_Europe_GMP_Approval_Of_Shilpa_Medicare_L_e066ce.pdf | 29 | E24 | 1 | none | ce998439 |
| 28 | Steamhouse_India_Announcement_under_Regulation_30_LODR-Ea_5ff94e.pdf | 30 | E06 | 24 | none | 7a4d9fef |
| 29 | TIPCO_Engineering_Announcement_under_Regulation_30_LODR-Ch_22f920.pdf | 31 | E17 | 4 | 3,4 | 69ee5491 |
| 30 | TIPCO_Engineering_Intimation_Under_Regulation_30_Of_The_SE_db8123.pdf | 32 | E17 | 4 | 3,4 | 69ee5491 |
| 31 | Tanfac_Inds_Intimation_Of_Receipt_Of_Trading_Approva_a876b4.pdf | 33 | E14 | 2 | none | 5c48bcad |
| 32 | Tinna_Rubber_Rating_update_c4c6ed.pdf | 34 | E08 | 7 | none | db8d74f2 |
| 33 | Yaap_Digital_Change_in_Management_9d64e6.pdf | 36 | E18 | 3 | none | a4710c28 |
| 34 | Yaap_Digital_Resignation_96d888.pdf | 37 | E18 | 3 | none | a4710c28 |
| 35 | Yaap_Digital_Resignation_of_DirectorKMPSMP_ed230a.bin (NSE zip) holds Resignation_Raj_new_2.pdf (1 page, text) and ROID_26827_WebXMLFile_20261010_144933976_1.xml | 35 | E18 | 1 | none | pdf: f7677f64 |

Feed items 2 and 24 have no file. They are covered in E03 and E30 from CRISIL web pages.

## 4. Entries

Order follows the seven headings of the manual. Inside a heading: companies on your list that touch a rule first, then the rest of your list, then companies not on your list. No stock in the window is in held.txt, so there is no "held" group.

### HEADING 1. OPERATIONAL UPDATES

#### E01. Bajel Projects: order of "INR 200 Cr+" for two 220kV substations in Mumbai (feed item 7)

- Status: on your list. Notion: WATCHLIST / AVOID, not held. Position: none at the current price; Small (2-3%) only below ₹92.
- File: Bajel_Projects_Announcement_under_Regulation_30_LODR-Pr_392ab9.pdf, 2 pages, text layer.
- Event. Press release filing, letter dated 9 Oct, digitally signed 9 Oct 20:38 [FILED p.1]. Bajel "secures a Major Order worth INR 200 Cr+ for 220kV GIS Substations in Mumbai" [FILED p.1].
- Key facts.
  - Scope: Package A, 220kV GIS at the Salsette receiving station. Package B, 220kV outdoor GIS substation at the Powai receiving station. Supply and installation, EPC [FILED p.2].
  - "Major" is Bajel's own band, inclusive of GST: Significant ₹50 to 100 Cr, Large ₹100 to 200 Cr, Major ₹200 to 300 Cr, Mega ₹300 to 400 Cr, Ultra-mega ₹400 Cr and above [FILED p.2 footnote].
  - Quote from MD and CEO Rajesh Ganesh on strengthening Mumbai's grid [MGMT p.2].
  - This file does not name the customer. NOT FOUND in this file.
- Customer found in another document. The separate Reg 30 order filing of 9 Oct (signed 17:19) names The Tata Power Company Limited as the awarding entity, 18 months from the purchase order, ordinary course, not a related party transaction, no promoter interest [FILED, file Bajel_Projects_Announcement_under_Regulation_30_LODR-Aw_4e736f.pdf, p.1 to 2, from the previous window's folder in the same zip]. That filing gives no rupee value beyond "Major Order".
- Record test.
  - Order book ₹3,442 Cr at FY26 end, up 15% [RECORD, AR review 17-Jul-26]. ₹200 Cr is 5.8% of it, ₹300 Cr is 8.7% [INFERENCE]. The Q1 FY27 order book is not in the record (the 06-Oct entry says the Q1 FY27 master gate is unlogged), so growth since March cannot be stated.
  - Monitoring row 3 (unexecuted order book above ₹3,000 Cr and rising) and row 4 (EHV and GIS above 40% of the book) are helped. Row 5 asks for three or more wins above ₹400 Cr per year and calls "zero major wins in 2 consecutive quarters" red. A ₹200 to 300 Cr order is below the ₹400 Cr bar, so it does not count there [RECORD, Section 8 checklist].
  - Thesis-broken condition 3 (order book below ₹2,500 Cr) is not touched. The direction is away from it.
- Touches a rule: YES. Monitoring rows 3, 4 and 5 (order book, GIS share, size of wins). No thesis-broken condition fires.
- Not said: value before GST, purchase order date, payment terms, margin.
- Price: ₹157 (screener.in, 11-Oct-26 11:02 IST), record ₹177 (May-26). Entry zone ₹74 to ₹92, MoS ₹74. Price is 1.71x the top of the zone.
- Record note: the 06-Oct entry also lists the Saudi JVCo "not incorporated by September 2026" as a red line and the Q1 FY27 master gate as unlogged. Neither is answered by this filing.

#### E02. Airfloa Rail Technology: MOU with KTK Group (China) to bid together for platform screen door projects (feed items 4 and 5)

- Status: on your list. Notion: WATCHLIST / AVOID, not held. Position: none.
- Files: Airfloa_Rail_Signing_Of_MOU_With_KTK_Group_Co_Ltd_a3a6bd.pdf (2 pages, letter signed 10-Oct 13:09) and Airfloa_Rail_Announcement_under_Regulation_30_LODR-Pr_43f7a8.pdf (3 pages, press release letter signed 10-Oct 20:31). Both text layer. Same event, two different documents.
- Key facts.
  - MOU with KTK Group Co. Ltd, "incorporated under the laws of China", with an India office at Coimbatore, to bid jointly for "eligible" platform screen door (PSD) projects in India through tender specific joint ventures, consortiums or other permitted structures [FILED, MOU letter p.1 to 2].
  - It "does not, by itself, require either Party to acquire equity". Consideration is "dependable on the value of each tender which is unpredictable in advance". Before any bid the parties must confirm in writing that conditions in the MOU are done or can lawfully be done within the tender timetable. Not a related party transaction. Promoter group has no interest in KTK [FILED p.2, items 3, 4, 8, 9, 10].
  - Airfloa would lead an Indian manufacturing programme for selected parts of full-height PSD systems. Mechanical: fixed door panels, emergency exit doors, fixed screens, columns, base supports, platform escape doors. Electrical: cables and power supply systems. KTK would supply system design, engineering, proprietary technology, documents and technical oversight. Airfloa would lead local manufacturing, project management, installation, testing, commissioning and customer coordination [MGMT, press release p.2].
  - No tender, customer, value, volume or date is named.
- Drafting error [FILED, press release p.3]: the safe harbour paragraph says "Prime Cable Industries Limited will not be in any way responsible". Prime Cable Industries is not Airfloa. The legal disclaimer was copied from another company's release.
- Record test.
  - Thesis-broken conditions: PRIMARY (share of receivables older than 6 months above 23.4% and rising, with zero provisioning) and SECONDARY (standalone operating cash flow negative into FY27 on a full half basis) are not touched [RECORD, page body].
  - Monitoring row 7 (14-acre facility and BBBS JV) and row 8 (no new guarantees or related party deals) are not touched.
  - The page says the aero and defence story is "diluting not building" because railway share of revenue rose from 65% to 72% in FY26 [RECORD, 08-Sep-26]. PSD systems are metro and railway equipment, so this adds to railway exposure rather than diversifying away [INFERENCE].
  - The 14-Sep MoU to buy KIN Railway Equipment (₹48 Cr, ₹180 Cr order book) is still at MoU stage on file; no definitive agreement appears in this window.
- General rule worth checking [INFERENCE from general knowledge, not in any file]: since 2020 Indian public tenders have required bidders from countries sharing a land border with India to register with a government authority. Whether a tender allows a China based technical partner must be checked in the tender document.
- Touches a rule: NO (no thesis-broken condition or monitoring row is touched). It touches the diversification narrative on file.
- Price: ₹566 (screener.in, 11-Oct-26 11:02 IST) against ₹315 on file. Up 79.7%. 52-week high ₹594. No filing in this window explains the rise. Entry zone ₹146 to ₹193, MoS ₹155. Price is 2.93x the top of the zone.
- Not found: any reason for the 80% rise since the July price on file; where it would be found: BSE and NSE announcements for 29-Sep to 9-Oct and the price chart. Screener's list shows only the 28-Sep AGM papers and a 9-Oct newspaper notice before the MOU.

#### E03. Aarti PharmaLabs: CRISIL reaffirms AA- Stable and raises bank limits to ₹1,000 Cr (feed item 2, no PDF)

- Status: on your list. Notion: WATCHLIST, not held. No entry zone, no thesis-broken conditions (page is a stub).
- File: none in the zip. The feed item has no summary. I found the CRISIL rating rationale dated 9 Oct 2026 (link on the Screener page: crisil.com RatingDocs AartiPharmalabsLtd_October 09_ 2026_RR_405037.html), read in full [AGENCY]. It is a web document, not one of the 35 PDFs.
- Key facts [AGENCY, CRISIL, 9-Oct-26].
  - Rating reaffirmed at Crisil AA-/Stable. Rated bank loan facilities enhanced to ₹1,000 Cr from ₹700 Cr. Table of facilities: cash credit lines ₹735 Cr, proposed fund-based limits ₹36 Cr, term loans ₹115 Cr, ₹15 Cr and ₹99 Cr. They add to ₹1,000 Cr [INFERENCE sum].
  - Rating history: A+/Positive until 2024, AA-/Stable since 17-Jul-25, reaffirmed 13-Mar-26.
  - Consolidated operating income ₹1,819 Cr in FY26 against ₹2,115 Cr in FY25, down 14.0% [INFERENCE on the percentage]. CRISIL gives two reasons: a change in accounting for the Ganesh Polychem joint venture and weaker API intermediates. FY27 revenue is expected at ₹2,100 to ₹2,200 Cr.
  - Operating margin 20.29% in FY26, 22.04% in FY25, 25% in Q1 FY27. Expected 22% to 25% over the medium term as the Atali site ramps.
  - Reported profit after tax ₹174.71 Cr against ₹272.40 Cr. Forex loss ₹33.2 Cr on a foreign currency term loan.
  - Gearing 0.38x against 0.22x. Total outside liabilities to net worth 0.68x. Interest cover 8.25x against 18.16x. Net worth above ₹2,000 Cr.
  - Gross current assets 278 days against 219 days. Customers get 90 to 120 days. Inventory 140 to 160 days. Bank limit use 70% over the 12 months to July 2026. Cash and bank ₹7.85 Cr at 31-Mar-26. Expected cash accruals ₹300 to 330 Cr against term debt repayments of ₹50 to 55 Cr.
  - Upgrade factors: net cash accrual above ₹500 Cr and a better working capital cycle. Downgrade factors: revenue decline or operating margin below 18%, or larger debt funded capex or higher working capital need.
- Record test.
  - The FY26 numbers match the record: "CONSOLIDATED revenue -14% mostly mechanical: Ganesh Polychem JV moved to equity-method accounting" [RECORD, Key Notes 22-Sep-26].
  - The record says the catalyst is "NOW CLOSER": Atali Phase 1 commissioned, Tarapur xanthine live, Atali Block-2 groundbreaking targeted Q3 FY27 [RECORD]. CRISIL's 25% Q1 FY27 margin and Atali ramp support the first two.
  - The promoter group sold about 17.9 lakh shares (about 2%, about ₹145 Cr) between June and September [RECORD]. Not touched.
- Touches a rule: NO. The page has no rule on file. The filing supports the record's "catalyst closer" reading and adds a working capital and gearing fact.
- Next date: board meeting on Wednesday 28 Oct 2026 for Q2 results; trading window closed 1 Oct to 30 Oct [FILED, Aarti_Pharma_Board_Meeting_Intimation_..._d0c932.pdf p.1, from the previous window's folder].
- Price: ₹856 (screener.in, 11-Oct-26 11:02 IST). Record ₹901 (22-Sep-26). No buy level on file.
- Record fix: Ticker AARTIPHARMA does not load on screener.in; AARTIPHARM does and is the NSE symbol on the company's own letter [FILED, the 9-Oct board notice: "SYMBOL: AARTIPHARM"].
- Missing document: none for this fact. The full CRISIL document is the source.

#### E04. Karnika Industries: Q2 and H1 FY27 results (feed item 21)

- Status: NOT on your list. No rules on file.
- File: Karnika_Industri_Outcome_of_Board_Meeting_4f1a1d.pdf, 14 pages. Page 1 text. Pages 2 to 14 are scanned images (OCR'd). Page 4 (standalone results) is a rotated scan. I read the results pages by eye (pp.4 and 10).
- Event. Board meeting on Saturday 10 Oct 2026, 19:00 to 20:30, approved unaudited standalone and consolidated results for the quarter and half year ended 30 Sep 2026 [FILED p.1]. Letter signed 22:12. Limited review reports by AAAJ & Associates, Kolkata, dated 10 Oct, no qualification [FILED p.2, p.8].
- Key numbers (₹ lakh in the filing).
  - Standalone: revenue Q2 8,182.82, Q1 5,977.78, Q2 FY26 6,972.71. H1 14,160.60 against 10,301.30. Profit after tax Q2 1,081.68 against 938.88; H1 1,816.87 against 1,246.44 [FILED p.4]. In rupees crore: Q2 revenue ₹81.83 Cr (+17.4% on a year ago), profit ₹10.82 Cr (+15.2%); H1 revenue ₹141.61 Cr (+37.5%), profit ₹18.17 Cr (+45.8%) [INFERENCE on percentages].
  - Consolidated: revenue Q2 10,619.84, Q1 7,377.20, H1 17,997.04; profit after tax and associate share Q2 1,418.01, H1 2,331.76 [FILED p.10]. That is ₹106.20 Cr, ₹179.97 Cr and ₹23.32 Cr for H1 profit. No year-ago comparison is given for the consolidated numbers because the 75% subsidiary Kidcity Solutions was bought on 4-Oct-25 [FILED p.6, note 6; p.13].
  - Balance sheet, standalone: trade receivables ₹109.91 Cr at 30-Sep-26 against ₹67.41 Cr at 31-Mar-26, up 63% [FILED p.3; INFERENCE on percentage]. Short-term borrowings ₹67.68 Cr, long-term ₹11.25 Cr.
  - Cash flow H1, standalone: operating cash flow minus ₹4.88 Cr after a ₹42.50 Cr receivables rise [FILED p.5]. Consolidated minus ₹4.41 Cr [FILED p.11].
  - Warrants: 39,66,860 warrants at ₹121, each convertible within 18 months, 25% paid on issue, ₹11,99,97,521 received [FILED p.6, note 4]. The unpaid 75% is about ₹36 Cr [INFERENCE: 39,66,860 x 121 = ₹48.0 Cr in total].
  - Other: ₹2 Cr for 40% of Elementa Lifespaces Pvt Ltd (associate from 24-Jul-26; share of loss ₹15.53 lakh); agreed to buy 26% of RDB Elementa Sports Academy for ₹5.2 lakh, not yet allotted [FILED p.7, notes 11 to 12]. Net loans and advances to others ₹15.93 Cr in H1 [FILED p.5].
- Oddity [INFERENCE]: standalone EPS for Q2 FY26 is printed ₹3.29 and for H1 FY26 ₹6.07 [FILED p.4], but profit of ₹938.88 lakh over the same 6,199.75 lakh of equity capital (face value ₹10, so 619.975 lakh shares) is ₹1.51, and H1 is ₹2.01. The filing shows one share capital figure for every period. The year-ago EPS looks based on an older share count.
- Touches a rule: NO (not on your list).
- Dated event outside the window: the Screener list shows an earnings call on 13 Oct 2026 for Q2 and H1 FY27 [SECONDARY, NSE intimation of 7-Oct-26, not read].
- Price: ₹125 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹90.2 to ₹182, market cap ₹777 Cr. Warrant price ₹121.

#### E05. Premier Polyfilm: Q2 and H1 FY27 results (feed items 25 and 26)

- Status: NOT on your list.
- Files: Premier_Polyfilm_UNAUDITED_FINANCIAL_RESULTS_FOR_THE_QUAR_636eac.pdf (8 pages, cover letter under the title "unaudited financial results") and Premier_Polyfilm_Board_Meeting_Outcome_for_Board_Meeting__f1151a.pdf (8 pages, cover letter under the title "board meeting outcome"). The two files differ only in the cover letter. The results pages carry an OCR text layer that is garbled in places, so I read the numbers from the page images (pp.2, 3, 7).
- Event. Board met 10 Oct 2026, 13:30 to 14:30 and approved standalone unaudited results for the quarter and half year to 30 Sep 2026; limited review report by ADV and Co LLP attached [FILED p.1 of each; report p.8].
- Key numbers (₹ lakh) [FILED p.2 to 3].
  - Revenue from operations including GST: Q2 11,506; Q1 10,006; Q2 FY26 8,317. H1 21,512 against 15,761. Total income Q2 11,618; H1 21,683.
  - GST is shown again as an expense: Q2 1,363, H1 2,636 (H1 FY26 2,041).
  - Profit before tax Q2 1,311, H1 2,525. Profit after tax Q2 981 (Q1 908, Q2 FY26 801), H1 1,889 (H1 FY26 1,401). EPS Q2 ₹0.94, H1 ₹1.80, on 1,059 lakh shares of ₹1.
  - In crore: Q2 revenue incl. GST ₹115.06 Cr (+38.3% on ₹83.17 Cr), profit ₹9.81 Cr (+22.5%); H1 profit ₹18.89 Cr (+34.8%) [INFERENCE on percentages]. Taking GST out, Q2 revenue is ₹101.43 Cr against ₹72.64 Cr (+39.6%) and H1 ₹188.76 Cr against ₹137.20 Cr (+37.6%) [INFERENCE: revenue minus the GST expense line].
  - Balance sheet 30-Sep-26: total equity ₹167.75 Cr; trade receivables ₹39.64 Cr (₹41.26 Cr in March); no borrowings line (both borrowing lines show a dash) [FILED p.6 to 7]. Debt equity ratio printed 0.11 (p.3). The ratio and the balance sheet disagree and the filing gives no explanation [INFERENCE: other financial liabilities of ₹23.63 Cr may carry it].
  - Cash: H1 net cash from operations ₹13.22 Cr; capex ₹5.81 Cr [FILED p.4]. Cash and equivalents ₹6.90 Cr (₹5.04 Cr in March) [FILED p.5].
- Feed summary error: the exchange summary says "H1 revenue Rs 216.83 crore". That is total income including other income, and revenue is stated including GST.
- Touches a rule: NO (not on your list).
- Price: ₹103 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹38 to ₹107, market cap ₹1,077 Cr. Trades near the 52-week high.

#### E06. Steamhouse India: Q1 FY27 earnings call transcript (feed item 30)

- Status: NOT on your list.
- File: Steamhouse_India_Announcement_under_Regulation_30_LODR-Ea_5ff94e.pdf, 24 pages, text layer. Read in full (cover letter p.1, call pp.2 to 24).
- Event. Transcript of the maiden investor call held Tuesday 6 Oct 2026 on Q1 FY27 (quarter ended 30 Jun 2026) filed on 10 Oct [FILED p.1]. The host said the company is "in the silent period" for the quarter ended 30 Sep, so the call "would not discuss any unpublished financial or operational information" [FILED p.3].
- Key numbers [MGMT, CMD Vishal Budhia and CFO Vaibhav Gattani]. Page numbers are PDF pages.
  - Q1 FY27: steam sold 3,05,816 tons (+16.7% a year ago, +11.52% on Q4) [p.6 to 7]; revenue ₹128.62 Cr (+13.35%); EBITDA ₹30.93 Cr (+60.08%), margin 24.05% against 17.03%; profit before tax ₹21.90 Cr; profit after tax ₹18.34 Cr (+80.25%) [p.7]. Revenue from steam ₹123.37 Cr (+46.07%), because coal trading was stopped [p.7, p.9].
  - FY26: revenue ₹491.51 Cr (+24.4%), EBITDA ₹83.49 Cr (16.99% margin), profit ₹38.64 Cr, return on equity 22.36%, return on capital employed 16.06% [p.8].
  - Capacity 345 tons per hour, about 70% tied to customers [p.10]; use 41.40% in Q1 against 36.06% a year ago [p.7]; target 60% to 65% [p.16]. Plan for about 705 tons per hour [p.5, p.8]. Four projects under way should go live in FY27; Tarapur in Q4 FY28; Dahej, Ankleshwar and Panoli in Q1 FY29 [p.12]. Capex: about ₹60 Cr to finish the four [p.11], about ₹170 Cr more over the next 15 to 18 months [p.12].
  - Una (Himachal) bulk drug park: EPC mandate of about ₹311 Cr including GST, 300 tons per hour, paid for by the park company [p.5]; 9% revenue share [p.11]; EBITDA per ton about 8% to 10%, "not finalized" [p.17].
  - Gross debt ₹359.48 Cr at Q1 against ₹281.62 Cr at FY26 end [p.8]. Working capital cycle guided at 35 to 40 days; coal bought for cash since May 2026 [p.21].
  - Related party: steam is still bought from Sanjoo Dyeing & Printing Mills for Sachin "at least for next few quarters" [p.16 to 17]. Q2 is usually weaker because of the monsoon [p.18]. On annual growth: "we will try" to match Q1; an analyst referred to guidance of 30% to 35% EBITDA growth a year [p.22].
- Inconsistency to note: own generated steam 73.7% and traded steam 22.2% add to 95.9% [p.22]. The remainder is not explained [INFERENCE: probably nitrogen and other].
- Touches a rule: NO (not on your list).
- Price: ₹128 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹91.5 to ₹133, market cap ₹3,535 Cr.

#### E07. Deep Industries: CARE reaffirms A+ Stable (feed item 10)

- Status: NOT on your list. The name appears once on another page: as the best peer in the comparison on the South West Pinnacle Exploration page (a stock in held.txt) [RECORD].
- File: Deep_Industries_Rating_update_fd5228.pdf, 7 pages, text layer. Byte-identical to the file of the same name in the previous window's folder (same MD5). The rating press release is dated 9 Oct 2026 [FILED p.1].
- Key numbers [AGENCY, CARE Ratings, 9-Oct-26].
  - Bank facilities: long and short term ₹179.50 Cr (cut from ₹189.50 Cr), CARE A+; Stable / CARE A1; long term ₹288.69 Cr (raised from ₹269.69 Cr), CARE A+; Stable. Both reaffirmed [p.1]. Together ₹468.19 Cr against ₹459.19 Cr [INFERENCE].
  - Order book ₹3,047 Cr at 30-Jun-26 (3.29x FY26 income of ₹926.31 Cr); ONGC about 65% of it. Fifteen year production enhancement contract worth ₹1,395 Cr [p.2 to 3].
  - Consolidated total operating income ₹926.31 Cr in FY26 (+60%), ₹278.92 Cr in Q1 FY27 (+40%). Operating profit before interest, lease rentals, depreciation and tax margin about 40% in FY26 and 38.8% in Q1 [p.2, p.4; margin INFERENCE: 108.14 / 278.92].
  - Profit after tax FY26 ₹197.06 Cr reported, ₹405.34 Cr adjusted for a write-off of about ₹208 Cr of receivables inherited in the Kandla Energy merger [p.2, p.4].
  - Loans and advances to Prabha Energy (promoter group company) ₹134.75 Cr at March; ₹88.93 Cr received by 30-Jun-26 [p.3]. The unpaid balance is about ₹45.8 Cr [INFERENCE].
  - Overall gearing 0.13x. Planned FY27 capex about ₹350 Cr with about ₹100 Cr new term debt [p.3].
  - Weakness: since Feb 2026 ONGC has provisionally barred Deep from new workover rig tenders after a rig was sabotaged in Bokaro; the bar "continues" [p.3]. ONGC is about 67% of standalone FY26 sales [p.3].
- Source inconsistency: page 2 says integrated project management was 39% of FY26 income "(FY25: 62%)" and natural gas services 61% "(FY25: 62%)". Two 62% figures cannot both be right [INFERENCE: FY25 project share is probably 38%].
- Touches a rule: NO (not on your list). Indirect: the comparison peer for a stock in held.txt. Nothing in the filing changes that comparison.
- Price: ₹746 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹327 to ₹827.

#### E08. Tinna Rubber and Infrastructure: CARE upgrades to BBB Stable (feed item 34)

- Status: NOT on your list (mentioned once on the E2E Networks page [RECORD]).
- File: Tinna_Rubber_Rating_update_c4c6ed.pdf, 7 pages, text layer. Byte-identical to the previous window's copy (same MD5). Press release dated 9 Oct 2026 [FILED p.1].
- Key numbers [AGENCY, CARE, 9-Oct-26].
  - Upgrade from CARE BBB- to CARE BBB, Stable, on long term bank facilities of ₹220.76 Cr (raised from ₹137.86 Cr) and ₹17.00 Cr long and short term (upgraded to BBB; A3+) [p.1]. Total ₹237.76 Cr [INFERENCE; annexure p.5 adds the same].
  - FY26 income ₹545.81 Cr (+7.83%); operating margin 17.25% (15.36% in FY25); profit after tax ₹52.85 Cr; Q1 FY27 income ₹156.18 Cr, margin 21.8% [p.2, p.4; Q1 margin INFERENCE 34.07 / 156.18].
  - Planned capex about ₹255 Cr over FY27 to FY29, largely funded by about ₹100 Cr of equity in FY28 "subject to approvals", ₹30 Cr term loan, and accruals [p.1, p.3]. New plant at Sullurpeta about ₹200 Cr; first phase by Q4 FY28.
  - Gearing 0.43x; interest cover 8.23x; operating cycle 53 days; collection period 38 days against 27 days a year ago [p.2, p.4].
  - Risks named: raw material prices, currency (imports are 54% of raw material), cyclical road and tyre demand, execution of the capex [p.3].
- Touches a rule: NO (not on your list).
- Price: ₹886 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹527 to ₹1,322.

### HEADING 2. CORPORATE ACTIONS

#### E09. Chemplast Sanmar: agrees to buy 27% of a solar power producer for ₹45 lakh (feed item 8)

- Status: NOT on your list.
- File: Chemplast_Sanmar_Announcement_under_Regulation_30_LODR-Ac_45c719.pdf, 4 pages, text layer. Letter dated 10 Oct, signed 13:07; event time 10-Oct 11:30 IST [FILED p.1 to 2].
- Event. Chemplast is entering a power purchase agreement with Yesaryes Energy Pvt Ltd and a share purchase agreement with the seller, Veebee Yarnntex Pvt Ltd. It will buy 27% of Yesaryes's paid up share capital, in cash, in one or more tranches, for ₹45 lakh [FILED p.4 items 7 to 9]. Yesaryes runs a 37.5 MW solar plant in Tamil Nadu that started commercial operations in April 2026; the company was incorporated on 20-Jan-25 [FILED p.3 items 1 and 10]. The purpose is to buy green power under the group captive scheme and cut energy cost [FILED p.1, p.3 to 4].
- Other facts [FILED p.3 to 4]: not a related party transaction; promoter group has no interest in Yesaryes; no regulatory approvals needed; completion "within the statutory time limits". Turnover is not given because the plant is new.
- Reading [INFERENCE from general knowledge, not in the file]: group captive power rules normally require the buyer to hold at least 26% of the generator. 27% sits just above that.
- Size: ₹45 lakh is about 0.013% of the ₹3,394 Cr market cap [INFERENCE]. The cost saving, tariff and volume (units a year) are not disclosed. NOT FOUND; they would be in the power purchase agreement, not filed.
- Touches a rule: NO (not on your list).
- Price: ₹215 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹161 to ₹413.

#### E10. Heritage Foods: pays for another 5.60% of Heritage Novandie Foods (feed item 18)

- Status: NOT on your list.
- File: Heritage_Foods_Update_On_Acquisition_Of_560_Equity_Shar_67af73.pdf, 1 page, text layer. Letter dated 10 Oct, signed 12:57 [FILED p.1].
- Event. Heritage "has paid the purchase consideration on October 9, 2026" for the further 5.60% of its subsidiary Heritage Novandie Foods Ltd. "The transfer of the aforesaid equity shares is currently under process". It follows earlier intimations of 16-Jul-26 and 29-Aug-26 [FILED p.1].
- NOT FOUND in this file: the amount paid, the seller and the resulting holding. They would be in the 16-Jul and 29-Aug intimations on the BSE and NSE announcement pages. Those two documents are not in this window.
- Touches a rule: NO (not on your list).
- Price: ₹390 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹292 to ₹504.

### HEADING 3. FUNDRAISING AND CAPITAL

#### E11. Oswal Pumps: ₹456 Cr solar cell plant, ₹296 Cr from debt, and a change in how IPO money is used (feed items 22 and 23)

- Status: on your list. Notion: WATCHLIST, not held. Position: Small (2-3% max). Promoter verdict: CONCERN.
- Files: Oswal_Pumps_Announcement_under_Regulation_30_LODR-Pr_80d914.pdf (press release, 4 pages, signed 10-Oct 17:38) and Oswal_Pumps_Adoption_Of_New_Line_Of_Business_And_Var_243c45.pdf (Reg 30 disclosure, 7 pages, signed 10-Oct 17:39). Both text layer. One event, two documents. Placed under this heading because the central items are the change in use of IPO money and the debt. The plant itself is pointed to under Heading 1.
- What was approved [FILED, disclosure p.1; MGMT, press release p.2].
  - The board of the 100% subsidiary Oswal Solar Energy Pvt Ltd (OSEPL) approved a greenfield 1.2 GW TOPCon solar cell plant at Karnal, Haryana. Commercial production "expected by April 2028". All output for OSEPL's own module lines. It would meet about 75% of OSEPL's cell need; the rest is still bought in [press release p.2 to 3; disclosure Annexure B p.6].
  - The company board, meeting 16:45 to 17:30, approved a change in the objects of the IPO and a longer time limit, "subject to ... approval of the Shareholders". Details "shall form part of the postal ballot notice to be issued ... in due course" [disclosure p.1].
- Numbers [FILED].
  - Project cost ₹4,558.50 million, that is ₹455.85 Cr [disclosure p.7 item 3]. About ₹296 Cr by debt. ₹159.85 Cr from unused IPO money out of ₹163.04 Cr [press release p.2]. 455.85 minus 159.85 is 296.00, so the two documents agree [INFERENCE check].
  - IPO net proceeds ₹8,415.14 million. Used ₹6,312.78 million (75.02%). Unused ₹2,102.36 million, that is ₹210.24 Cr, as at 8-Oct-26 [disclosure p.4].
  - Object 2 (equity into Oswal Solar for new Karnal units): ₹2,727.58 million, used ₹1,097.14 million (40.22%), unused ₹1,630.44 million. Of the unused, ₹1,598.50 million (₹159.85 Cr) moves to the cell plant "in place of" the aluminium frame unit, the remaining 300 MW of EVA encapsulant and the remaining 500 MW of module capacity. ₹31.94 million (₹3.19 Cr) stays on the original object. Deployment by FY2028 [disclosure p.3 to 4].
  - Object 1 (capex of the company itself): ₹898.60 million, used ₹455.46 million (50.69%); no change in amount; deployment date moved to FY2027 [disclosure p.3].
  - Module unit is now 1,000 MW and EVA 1,200 MW "as per the Prospectus" [disclosure p.5 footnote ^^]; the original plan in the same document was 1,500 MW of each [p.3]. So the module plan is cut by 500 MW and EVA by 300 MW [INFERENCE from the two pages].
  - This is the second variation. The first (postal ballot of 17-Dec-25) moved the site to a larger Karnal parcel [disclosure p.5 footnote ^].
  - Reasons given [MGMT]: ALMM List II needs domestic cells; long term cell contracts were offered "only at elevated prices even though cell prices are reasonably likely to soften" and with large deposits; frames are low value and the technology "is in flux" [disclosure p.6 to 7; press release p.3].
  - The press release still calls the 1 GW module line "now being set up" [p.3]. The Q1 FY27 concall had it starting commercial production in the first or second week of September 2026 [RECORD, Q1 concall guidance table]. That is a possible slip [INFERENCE].
  - Quirk: the press release says "Commenting on the order" for a capex decision [p.3]. Template wording.
- Record test [RECORD].
  - Thesis-broken price condition: "CMP below ₹280" (Valuation Verdict "STOP: Below ₹280 (price) OR CFO/PAT stays negative through FY27"; Q4 FY26 review table "CMP below ₹280: not assessable from filing"). Price today ₹254, that is 9.3% below ₹280 [INFERENCE]. The record's own last prices were also below it: ₹274 on 22-Sep and ₹255 on 8-Oct. No entry since 22-Sep flags this. ₹280 was set in April against a ₹390 price. Whether it is a stop for a position you never held is for you to rule.
  - ICRA, 22-Sep: [ICRA]A+ outlook revised to Negative on receivables and margin. Negative sensitivity includes "failure to improve working capital cycle, or large debt-funded capex". This filing announces the second while the first is open. Receivables ₹1,128 Cr at March; company said payments should come from Q2 FY27 [RECORD, 23-Sep].
  - Gate 1: H1 FY27 operating cash flow over profit of at least +0.10x, due with the H1 filing in November. Dated test inside it: receivables at 30-Sep-26 should be below ₹1,128 Cr. Hard entry stop: 3 of 4 legs met or adverse; leg (d), segment return not disclosed, is still met. Not changed by this filing.
  - Capex plan on file: about ₹250 Cr in FY27 funded from IPO deposits plus accruals (ICRA, 23-Sep). Debt of ₹296 Cr is not in it.
  - Debt context: total debt ₹225.34 Cr at 31-Mar-26 [RECORD, Q4 FY26 review]. ₹296 Cr new debt is 1.31x that [INFERENCE]. Net worth ₹1,683 Cr, gearing about 0.1x [RECORD, ICRA 22-Sep]. ₹296 Cr is 17.6% of net worth [INFERENCE].
  - Unused IPO money was ₹271.34 Cr at 31-Mar-26 [RECORD, AR Note 45] and is ₹210.24 Cr at 8-Oct-26. About ₹61 Cr used in about six months [INFERENCE].
  - ₹455.85 Cr is 15.7% of the ₹2,900 Cr market cap and 3.3x FY26 consolidated capex of ₹136.73 Cr [INFERENCE; RECORD].
- Record conflict and arithmetic problem [INFERENCE, needs your ruling]:
  - The page body (April) gives an entry zone of ₹350 to ₹435 and MoS ₹406. The 23-Sep Key Notes say "Entry price still NOT SET; set after H1 FY27 filing". The Entry Price Max property is blank. These cannot all stand.
  - The ₹406 MoS comes from a base fair value of ₹990 = FY28E EPS ₹59.0 x 16 to 20x, with FY28E PAT ₹361 Cr. ₹361 Cr over ₹59 means about 6.1 Cr shares. The April page itself shows market cap about ₹2,400 Cr at ₹390, which is 6.15 Cr shares. The record elsewhere says about 114.0 million (11.4 Cr) shares [Key Notes 28-Sep] and ₹3,119 Cr market cap at ₹274 (about 11.4 Cr). FY26 diluted EPS was ₹34.73 on PAT ₹376.28 Cr, about 10.8 Cr shares [Q4 FY26 table]. On about 11.4 Cr shares, FY28E PAT of ₹361 Cr is EPS of about ₹32, not ₹59. At the same 18x that is about ₹570 instead of ₹990. The same method then gives about ₹292 entry and about ₹234 MoS instead of ₹507 and ₹406 [INFERENCE: ₹570 / 1.953 and then 20% lower]. The April thesis line also says "EPS ₹47 (FY25) to ₹150 (FY28E)", a third set of numbers.
- Touches a rule: YES. (1) The ₹280 price condition. (2) ICRA's "large debt-funded capex" sensitivity. (3) Gate 1 and its dated receivables test. (4) The entry zone, which conflicts with the Key Notes.
- Not said: technology partner, equipment supplier, cell efficiency, land, debt terms and lenders, IRR or payback, margin uplift, whether subsidies apply, and the postal ballot date. Whether dissenting shareholders get an exit offer is not stated [INFERENCE: SEBI rules have such an exit route for changes to IPO objects; check the notice].
- Missing document: the postal ballot notice with the explanatory statement. It does not exist yet ("in due course"). It will be on BSE and NSE. Prompt for screener.ai is in BRIEF.md.
- Price: ₹254 (screener.in, 11-Oct-26 11:02 IST), 52-week ₹251 to ₹779. It is 1.2% above its 52-week low. Record price ₹274 (22-Sep).

#### E12. Quality Power Electrical Equipments: corrigendum to the 19 Oct EGM notice on the Winwin share swap (feed item 27)

- Status: on your list. Notion: WATCHLIST, not held. Entry zone ₹456 to ₹570, MoS ₹456.
- File: Quality_Power_El_Corrigendum_To_The_Notice_Of_The_Extra-O_6ecded.pdf, 2 pages, text layer. Cover letter dated 9 Oct, signed 20:58 [FILED p.1]. I also read the company's own website copy of the corrigendum (one page, same four points; fetched from qualitypower.com).
- Event [FILED p.1 to 2]. The company applied to NSE and BSE for in-principle approval of the preferential issue. NSE gave "certain observations" in a letter of 7-Oct-26, so a corrigendum is issued. It corrects four things.
  1. Date of the notice: read as 26-Sep-26 (the dispatch date), not the 23-Sep-26 board date. The in-principle applications were filed the same day, citing ICDR Reg 160(f).
  2. The 90 trading day VWAP printed as ₹1,456.40 should read ₹1,238.49. "No change in the floor price of Rs 1,456.40 or the issue price of Rs 1,460".
  3. Share count "10,19,635" should read "10,17,123", the number in the resolution.
  4. Footnotes: the shares go to the selling shareholders of Winwin Speciality Insulators against transfer of their shares under the SPA of 23-Sep-26. Allotment within 15 days of the special resolution, or within 15 days of the last approval if one is pending (ICDR Reg 170).
- Arithmetic [INFERENCE]. 10,17,123 x ₹1,460 = ₹148.50 Cr, the swap leg on file. ₹148.50 Cr divided by the ₹1,456.40 floor gives 10,19,637 shares, which is the wrong number the notice printed. So the first draft sized the swap at the floor price instead of the issue price. The gap is 2,512 shares, about ₹0.37 Cr. The floor of ₹1,456.40 is 17.6% above the corrected 90-day VWAP, so the floor must come from the 10 day average [INFERENCE: the rule uses the higher of the two]. The issue price is 0.25% above the floor.
- Record test [RECORD].
  - Numbers match the 25-Sep entry exactly: 10,17,123 swap shares, ₹1,460, floor ₹1,456.40, ₹148.50 Cr, 1.30% post-issue for the sellers. Nothing on file needs correcting. The ₹1,238.49 VWAP is new.
  - Five thesis-broken conditions (Sangli delayed beyond March 2027, return on capital below 20% for 2 years, CFO/PAT below 30% for 4 quarters and two others): none touched.
  - Open items on file: use of about ₹575 Cr of the ₹700 Cr QIP beyond the ₹123.84 Cr cash leg; Winwin profit and net debt (not disclosed). The corrigendum covers only the swap (it refers to "Item No. 1"). It does not say what other items are on the 19-Oct agenda. The record calls it the "QIP EGM". Whether the QIP is on this agenda is NOT FOUND in anything I could read: trade press summaries disagree (one lists only the swap resolution, one lists both). The EGM notice itself (26-Sep-26) is not in the record and I could not fetch it.
  - Next event on file: EGM Monday 19-Oct-26, 4:00 PM, by video [FILED p.1].
- Touches a rule: NO thesis-broken condition. It touches an open item (QIP use of funds) and the 19-Oct EGM date. It confirms two numbers on file.
- The in-principle approval from NSE and BSE is not yet in hand. NOT FOUND as received. It would appear as a Reg 30 filing.
- Price: ₹1,547 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹581 to ₹1,681. Swap shares are priced 5.6% below it (₹1,460 against ₹1,547) [INFERENCE]. Record ₹1,513.40 (24-Sep). The price is 2.71x the top of the zone.

#### E13. Hexaware Technologies: restated trust deed for the RSU plan 2026 (feed item 19)

- Status: NOT on your list.
- File: Hexaware_Tech_Restated_And_Amended_Trust_Deed_8d58bf.pdf, 18 pages. Page 1 text (cover letter, 9 Oct, signed 21:14). Pages 2 to 18 are scanned images, OCR'd. I checked page 2 by eye: "executed at Mumbai on this October 9th 2026" on stamp paper dated 8 Oct 2026.
- Event. Under the SEBI share based employee benefits rules, the company files the restated and amended deed of the Hexaware Employees Benefit Trust (earlier "Hexaware Employees Stock Option Trust 2024") [FILED p.1, p.6 clause 3.1].
- What the deed says [FILED]. The company is the settlor; trustees are Uma Thomas (Chief Risk Officer), Riten Gosar (VP Finance) and Jacob P U (Sr VP HR) [p.3]. Initial contribution ₹5 lakh [p.3 recital D]. The trust may take money and loans from the company [p.8 to 9 clause 9.1], buy shares including on the stock exchange [p.9 clause 10, p.11 clause 20.1], fund cashless exercise [p.6 to 7 clause 5.1(b)]. Trustees cannot vote the shares [p.12 clause 23.1]. The company can amend the deed if not harmful to employees [p.14 clause 28.1]. Between 2 and 4 individual trustees [p.9 clause 12.1]. There is no limit on the number of shares in the deed itself. NOT FOUND in this file; the limit would be in the RSU Plan 2026 and the shareholder resolution.
- Related vote, from another document. Shareholders approved the RSU Plan 2026 by postal ballot on 9-Oct-26 (scrutinizer's report, 20 pages, previous window's folder, file Hexaware_Tech_Scrutinizers_Report_On_Postal_Ballot_1b0f2b.pdf; the same file is on the BSE page). Item 1 passed with 84.59% for. The promoter group (45.40 Cr shares, 74.3% of shares) voted 100% for. Public institutions voted 77.5% against (8.83 Cr votes against, 2.56 Cr for, of 11.40 Cr votes polled; 95.9% turnout). Public non-institutions voted 99.75% for [FILED, report pp.2 to 3]. Items 4 and 5 (the trust buying shares from the market and the company lending it money) passed with the same split (84.58% for; institutions 77.5% against). Item 8, an amended incentive payment agreement with R. Srikrishna (promoter group interested, so promoters did not vote), passed with 59.88% for; public institutions voted 58.05% for and 41.95% against [FILED, report p.9]. I did not read the notice itself. NOT FOUND: the notice (dated 2-Sep-26) with the plan size and cost. It is on the Hexaware site and the exchange pages.
- Touches a rule: NO (not on your list).
- Price: ₹538 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹400 to ₹808.

#### E14. Tanfac Industries: BSE grants trading approval for 4,24,647 preferential shares (feed item 33)

- Status: NOT on your list (mentioned once on the Kronox Lab Sciences page [RECORD]).
- File: Tanfac_Inds_Intimation_Of_Receipt_Of_Trading_Approva_a876b4.pdf, 2 pages, text layer. Letter dated 10 Oct, signed 10:03 [FILED p.1].
- Event. BSE letter LOD/PREF/DD/107/2026-2027 of 9-Oct-26: 4,24,647 equity shares of ₹5 face value, issued "to Promoter and Non Promoter investors on a preferential basis" at ₹2,341 (premium ₹2,336), are listed and tradable from Monday 12-Oct-26. Distinctive numbers 21208919 to 21633565 [FILED p.1 to 2]. The difference of those numbers plus one is 4,24,647 [INFERENCE check].
- Size [INFERENCE]: 4,24,647 x ₹2,341 = ₹99.4 Cr. Today's price is 34% above the issue price.
- NOT FOUND in this file: the split between promoters and others, lock-in terms, and use of money. They are in the allotment filing and the preferential issue notice.
- Touches a rule: NO (not on your list).
- Price: ₹3,146 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹1,633 to ₹3,648.

### HEADING 4. PROMOTER AND INSIDER TRANSACTIONS

#### E15. Aequs: promoter foundation releases the pledge on all its shares (feed item 3)

- Status: on your list. Notion: Decision Status NOT set; Phase 1 verdict REWORK; mental model unsigned; no entry zone or MoS. Promoter verdict CAUTION, with an open ruling on the Hasbro statement.
- File: Aequs_Disclosures_under_Reg_311_and_312_of_SEB_7a01a5.pdf, 3 pages. Page 1 text (cover letter 9 Oct 18:04). Pages 2 and 3 are scanned (OCR'd; page 2 read by eye).
- Event [FILED].
  - Melligeri Private Family Foundation (trustee Mellwood Trustee Services) released the pledge on 10,05,13,070 shares (14.99% of capital) on 8-Oct-26, reported 9-Oct-26 [p.2].
  - After the event all 10,05,13,070 shares (14.99%) show as unencumbered [p.2].
  - Cover letter: "the release of pledge is for a temporary short period to enable Company to complete certain regulatory requirements" [p.1]. The requirement is not named.
  - Footnote: 10,04,38,070 of the 10,05,13,070 shares were locked in for 12 months at the IPO [p.3].
  - Form problems [INFERENCE]: the column "promoter holding already encumbered" reads Nil, though the 21-Sep filing on your page shows the whole holding pledged. The columns "reasons" and "entity in whose favour" are blank. Only one promoter is listed.
- Record test [RECORD, 23-Sep and 28-Sep entries].
  - On 21-Sep the same foundation pledged 100% of these shares to 360 One Prime Ltd for a ₹200 Cr facility "and such extended amount from time to time", for "making investments".
  - On 25-Sep the board approved up to 2,80,71,690 warrants at ₹231.55 (about ₹650 Cr) to the same foundation, ₹325 Cr upfront, EGM on 22-Oct-26.
  - Proposed warning line, not yet adopted by you: fires on any of (a) the pledge being invoked, (b) the facility shown above ₹200 Cr, (c) an "investment" being an Aequs related party. This filing is a release, so (a) does not apply, (b) is not answered, (c) is not answered. The record says the line "fires in substance on its third limb if the Rs325 Cr is funded from the pledge facility". Nothing here settles that.
  - Open: whether pledging IPO locked-in shares was allowed under the ICDR conditions (not verified in the record).
  - Reading [INFERENCE]: the release sits between the 25-Sep warrant approval and the 22-Oct EGM, which fits an ICDR rule that an allottee's existing shares must be locked in from the relevant date. That rule is not named in the filing. The second possible reading is the open ICDR question about pledging locked-in shares. The filing cannot separate the two.
- Other filings found outside the window [FILED, from the Screener list; documents fetched]:
  - 8-Oct, Reg 29(2): Amansa Investments Ltd (a large early investor) held 35,866,000 shares, 5.35%, down 2.13 points from 7.48% after a secondary market sale on 1-Oct-26 (filed 7 to 8 Oct) [file 40B8F842_9F8D_4CC6_8C9B_1D8F3CE8604D_092101.pdf, scanned, read by eye]. The sale price is not in the filing. NOT FOUND.
  - 9-Oct: Aequs put ₹15.75 Cr into its joint venture Ajna Aerospace & Defence (45,00,000 partly paid shares at ₹100, ₹35 paid) by rights issue; the JV is a related party; MD Rajeev Kaul is nominee director; Ajna's FY26 turnover ₹0.02 Cr, loss ₹0.99 Cr [FILED p.1 to 2; file Aequs_Aequs_Limited_Company_Has_informed_About_bbc900.pdf in the previous window's folder].
- Touches a rule: YES, the proposed (not adopted) pledge warning line, and the open Hasbro ruling by weight.
- Dates ahead: EGM 22-Oct-26 [RECORD]; lock-in lapses about Dec-2026 [RECORD].
- Price: ₹274 (screener.in, 11-Oct-26 11:02 IST), 52-week ₹113 to ₹295, market cap ₹18,343 Cr. Record ₹242.87 (22-Sep). Up 12.8%. The foundation's block is worth about ₹2,754 Cr at ₹274 [INFERENCE]. No buy level on file.

#### E16. Garware Hi-Tech Films: employee fined ₹5,000 for a trade within six months of his last buy (feed item 17)

- Status: on your list. Notion: WATCHLIST, not held. Entry Price Max ₹3,437, MoS ₹2,750. Promoter verdict: CONCERN (preliminary).
- File: Garware_Hi_Tech_Announcement_under_Regulation_30_LODR-Co_fc5d83.pdf, 4 pages, text layer. Letter dated 10 Oct, signed 13:57 [FILED p.1].
- Event [FILED p.2 to 4]. Report under the insider trading code. The person is Ashok Narayan Dane, General Manager, Production, not a promoter or promoter group member. Between 5-Dec-25 and 15-May-26 he bought 16 shares for ₹54,704.10 and sold 26 shares for ₹1,14,796.85 (values on weekly closing prices). The contra trade was "for 16 shares" within six months of the previous buy. The Audit Committee on 6-Aug-26 imposed a ₹5,000 penalty and warned him. He paid ₹5,000 to the SEBI investor protection fund on 21-Aug-26 (UTR 260821283031107). No earlier violations since last financial year. He confirmed in writing it was inadvertent and not based on unpublished price sensitive information.
- Timing [INFERENCE]: the filing is 50 days after the payment and 65 days after the committee decision. Whether that is within the deadline is NOT CHECKED.
- Record test [RECORD]. Governance record already has a SEBI insider trading fine of ₹76 lakh in 2021 (covering 2011 to 2014, Garware Polyester entity). No thesis-broken condition relates to this (ROCE, the 34% customer, margin below 18%, promoter verdict resolving to Avoid). Not touched.
- Touches a rule: NO. Hygiene item. The preliminary promoter verdict of CONCERN is not changed by a ₹5,000 employee fine.
- Price: ₹6,998 (screener.in, 11-Oct-26 11:03 IST), record ₹7,015.50 (1-Oct). 2.04x the ₹3,437 entry. Two rulings already pending on the page (price zone table against status; entry zone refresh to about ₹4,500 to ₹5,700).

### HEADING 5. GOVERNANCE AND MANAGEMENT

#### E17. TIPCO Engineering: CFO Ramesh Goel resigns on health grounds (feed items 31 and 32)

- Status: on your list. Notion: WATCHLIST / AVOID, never held. Entry Price Max ₹111, MoS ₹99. Promoter verdict CONCERN. Listed on BSE SME on 1-Apr-26.
- Files: TIPCO_Engineering_Announcement_under_Regulation_30_LODR-Ch_22f920.pdf and TIPCO_Engineering_Intimation_Under_Regulation_30_Of_The_SE_db8123.pdf. Byte-identical (same MD5, same size). 4 pages each: pages 1 to 2 text; pages 3 to 4 are the resignation letter as a scan (OCR'd, page 3 read by eye). Filed with BSE only.
- Event [FILED].
  - Letter dated 10-Oct-26, signed by CMD Ritesh Sharma at 12:33 (not by the Company Secretary). Mr Ramesh Goel resigned as Chief Financial Officer (KMP). His letter of 10-Oct-26 was received by e-mail that day. Effective close of business 10-Oct-26 [p.1].
  - Reason: "personal health grounds". "He has confirmed that there is no other material reason" [p.2 Annexure A].
  - Letter [p.3 to 4]: he joined on 10-Feb-26 in Finance and Accounts and was appointed CFO and KMP from 27-Apr-26. "I have been on medical leave since 11th September 2026". After "discussions with the Management" he asked to be relieved from 10-Oct-26 and "the Management has agreed", "subject to acceptance by the Board". He will hand over books, digital signature certificates and portal credentials.
  - No successor and no interim CFO is named. NOT FOUND. It would be on the next BSE filing.
- Arithmetic [INFERENCE]. CFO for 166 days (27-Apr to 10-Oct). On leave for the last 29 of them (11-Sep to 10-Oct).
- Record test [RECORD].
  - "Hard Thesis-Break Triggers (any one fires, permanent AVOID)", number 3: "Any further KMP or Independent Director resignation in FY27". A CFO is a KMP. 10-Oct-26 is in FY27. The filing fires it as written. The wording has no carve-out for health.
  - Monitoring trigger 9 (same wording) fires: "AVOID strengthens; no re-engagement for 12+ months".
  - History on the page: pre-IPO auditor Mittal Vaish resigned Jun-25; first CFO Neha Sharma resigned within weeks of listing; independent director Jeewan Chandra resigned 6 days after listing; the Company Secretary resigned in 2024; second statutory auditor Vinay I Aggarwal resigned effective 18-Aug-26. Goel is the CFO whose concall remark "we are realizing our payments on the time" was logged as contradicting 169 debtor days.
  - Timeline [RECORD dates, INFERENCE on overlap]: his leave began 11-Sep. In the next 11 days the company set up a 51% defence subsidiary with an unnamed partner (16-Sep), passed ₹117.33 Cr of preferential shares and warrants at the EGM (17-Sep) and doubled executive pay ceilings at the AGM (22-Sep). The CFO was on leave for all three. The leave was not disclosed in the record at the time.
  - The real gate: H1 FY27 filing by mid-November 2026 (SME half-yearly reporting; record correction of 23-Sep). That filing needs a CFO who can certify accounts.
- General rules to verify [INFERENCE from general knowledge, not in any file]: the Companies Act gives six months to fill a whole time KMP vacancy. SEBI's three month rule for listed companies probably does not apply on the SME board.
- Touches a rule: YES. Hard thesis-break trigger 3 and monitoring trigger 9.
- Price: ₹304 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹76.5 to ₹337, market cap ₹631 Cr. Record ₹296 (22-Sep). Price is 2.74x the ₹111 entry max and 3.07x the ₹99 MoS. The ₹180 preferential shares and warrants are about 69% in the money [INFERENCE]. The 9-Oct broker note on the page puts the price at ₹309 on 8-Oct [RECORD, Arihant, secondary].

#### E18. Yaap Digital: Chairman and Managing Director resigns ten days after shareholders re-approved him (feed items 35, 36, 37)

- Status: on your list. Notion: AVOID. Position: none (Do Not Initiate). Promoter verdict AVOID.
- Files. Three postings of one event. Items 36 and 37 are byte-identical PDFs (Yaap_Digital_Change_in_Management_9d64e6.pdf and Yaap_Digital_Resignation_96d888.pdf, 3 pages each, text). Item 35 is an NSE zip (Yaap_Digital_Resignation_of_DirectorKMPSMP_ed230a.bin) holding an XBRL form and Resignation_Raj_new_2.pdf (the email, 1 page). The email is the same text as page 3 of the others. Letters are addressed to NSE only (SME board).
- Event [FILED].
  - Laxmiraj Seetharam Nayak (DIN 01828278), Chairman and Managing Director, "has tendered his resignation from the positions of Chairman and Managing Director ... vide his resignation letter dated October 10, 2026, with effect from October 09, 2026, on account of his personal reasons and other pre-occupations". He confirms no other material reasons [p.1 to 2]. Signed by the CS 10-Oct 14:10.
  - The attached "letter" is an Outlook email from "Raj Nayak" to Sudhir Menon sent 09 Oct 2026 22:20, copied to Subodh Menon, B. Jagadesh Babu, Vandana Maithani, Vijay Malpani, Jigesh Shah, the CS and one other. It says the "demands and intensity of a full-time operating role are more than I would like to take on at this stage", he wants "to focus on my own venture" and give "greater attention to my health and personal priorities", and he is "positive about YAAP and its future" [p.3].
  - XBRL: event time 9-Oct 22:39; resignation letter received 10-Oct; effective 9-Oct; acknowledgement 2026/Oct/497836/6522; designation entered as "Others: Chairman & Managing Director" [item 35 xml].
  - No successor, interim chair or interim MD is named. NOT FOUND. It does not say whether he stays on the board.
- Related filing found outside the window [FILED]. Board meeting of Thursday 8-Oct-26, 12:30 to 12:50 PM (NSE file YAAPDIGITAL_08102026130353_Outcome_BM_08-10-2026.pdf, 4 pages, fetched; also on the Screener list). The board: approved a working capital loan or overdraft from HSBC up to ₹25 Cr and borrowing up to ₹25 Cr; "took note of the resignation of M/s. Shweta Jain & Co. LLP" as statutory auditors "with effect from September 23, 2026", reason "pre-occupation with other professional commitments"; appointed NGPC & Co (FRN 145474W, set up 2017 by CA Navnit S. Gajja and CA Pushpa U. Chandwani) to fill the casual vacancy, subject to members' approval; approved paying cash to the selling shareholders for the Tranche 2 purchase of Gozoop Online shares and an amendment agreement, whose details "shall be disclosed upon execution" [pp.1 to 4]. The amount of the Tranche 2 cash is NOT FOUND.
  - Dates [INFERENCE]: the auditor's exit took effect 15 days before the board noted it, and 6 days before the 29-Sep AGM that adopted the accounts. When the company received the auditor's letter is NOT FOUND.
  - The new firm's co-founder shares a surname with the earlier auditor S.S. Gajja & Co that quit in July 2024. No link is stated. I make no claim.
- Record test [RECORD].
  - Key Notes 01-Oct: the 11th AGM on 29-Sep approved Nayak as CMD for three years, approved a material related party deal with Gozoop (promoter votes excluded) and adopted FY26 accounts. He resigned 10 days later [INFERENCE: 9-Oct minus 29-Sep].
  - The record's governance stack has 8 items plus the NSE Reg 33 query (9th). Item 1 is the mid-term auditor resignation of S.S. Gajja & Co on 1-Jul-24, called "an institutional deal-breaker on its own". A second auditor exit (23-Sep-26) is 26.7 months later [INFERENCE]. Neither the auditor exit nor the Tranche 2 payment is in the record (last entry 01-Oct).
  - None of the 12 monitoring triggers covers leadership or auditor change.
  - Conflict on the page: the snapshot (Jul-26) names "Chairman & MD: Atul Hegde" and a June concall MD credibility grade C for him; the 01-Oct entry and today's filings name Nayak as CMD. The record never logs who Nayak is relative to Hegde. NOT FOUND: Hegde's current role.
  - Gozoop: 60.2% owned since 30-Mar-26. Tranche 2 buys 20% more. The record's inference: if later tranches price off Gozoop profit, related party flows that lift it raise the price YAAP pays [RECORD, INFERENCE].
- Touches a rule: PARTLY. No numbered trigger is touched. It adds to the governance stack and, with the 8-Oct auditor exit, repeats the record's flag 1.
- Dates ahead: H1 FY27 results for a BSE/NSE SME company are normally due within 45 days of 30-Sep, about 14-Nov-26 [INFERENCE from general rule; verify]. Record triggers for Q2 FY27 (Nov 2026): debtor days below 130, CFO/PAT above 0.2x, factoring facility.
- Price: ₹116 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹113 to ₹214, market cap ₹244 Cr. Record ₹198 (Jul-26, marked stale). Down 41.4%. Market cap over FY26 profit: 11.0x on total profit ₹22.2 Cr, 13.2x on shareholders' profit ₹18.46 Cr [INFERENCE]. The record's destination multiple is about 14x. No buy level on file.

#### E19. Fedbank Financial Services: CHRO leaves after notice, disclosed on her last day (feed item 14)

- Status: on your list. Notion: WATCHLIST / AVOID, not held. Entry Price Max ₹77 (zone ₹68 to ₹77), MoS ₹61.
- File: Fedbank_Financi_Announcement_under_Regulation_30_LODR-Ch_7c5877.pdf, 3 pages. Pages 1 to 2 text; page 3 the resignation letter, scanned (OCR'd).
- Event [FILED]. Letter dated 9-Oct-26, signed 21:39. Ms Anila Rajneesh, Chief Human Resources Officer, "had tendered her resignation on July 10, 2026, to pursue a new opportunity" and "ceased to be the CHRO ... with effect from the close of business hours on October 09, 2026" [p.1, p.2 Annexure I, p.3 letter dated 10-Jul-26]. She is a senior management person (SMP), not KMP.
- Arithmetic [INFERENCE]: the exchange filing came 91 days after the resignation and on her last day. Whether the rules required earlier disclosure is NOT CHECKED.
- Record test [RECORD]. In July the devil's advocate marked management trust WEAKENED on "near-total exec turnover in 18 months". The 9-Sep AR review softened this to a watch item as "mostly benign PE unwind plus a CS change". The CHRO's resignation (10-Jul) pre-dates the Q1 concall (15-Jul), the AR (4-Sep) and the AGM (29-Sep). The record of those three events does not mention it. Tripwires (credit cost above 1.1%, ROE below 14% by FY28, coverage ratio below 32%) are not touched by an HR exit.
- Touches a rule: YES, the "executive turnover" watch item. No tripwire.
- Price: see E26.

#### E20. Fractal Analytics: board chair moves between two non-executive directors (feed item 16)

- Status: on your list. Notion: AVOID, not held. Entry ₹275, MoS ₹220, watchlist trigger ₹400.
- File: Fractal_Analyt_Change_In_Chairman_Of_The_Board_Of_The_C_e7a20d.pdf, 2 pages, text. Letter dated 9-Oct-26, signed 21:26 [FILED p.1].
- Event [FILED p.1 to 2]. By circular resolution on 9-Oct-26 the board "noted" that Mr Rohan Haldea (DIN 08335883) ceased as Chairman and will continue as non-executive, non-independent director. It approved Mr Vivek Mohan (DIN 08306394), non-executive, non-independent director, as Chairman from 9-Oct-26. No profile (already a director). No reason given.
- Not said: why, who nominated Vivek Mohan, and the independent directors' view. NOT FOUND in the file and the record.
- Record test [RECORD]. Chairman and CEO roles are separate, "via Rohan Haldea". Vivek Mohan was re-appointed by rotation at the AGM [AR Notice item 2]. Board of 9 with 3 independent (33%). The six thesis-broken conditions include "Pranay Agrawal departs OR Srikanth steps back from CEO role". Neither founder is affected. Not touched.
- Dates on the record: new CFO Shilpa Kedia starts 19-Oct-26. Q2 FY27 conference call on 4-Nov-26, 8:00 AM (notice of 25-Sep in the Screener list, not read). The record's cleanest Q2 test is Fractal's share of the Qure loss: under ₹10 Cr bull, over ₹15 Cr bear.
- Touches a rule: NO.
- Price: ₹708 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹698 to ₹1,120, market cap ₹12,285 Cr. Record ₹861. Down 17.8%. 1.4% above its low. 2.57x the ₹275 entry and 1.77x the ₹400 watchlist trigger.

### HEADING 6. REGULATORY, LEGAL AND TAX

#### E21. ADF Foods: US subsidiary settles with Ascot for US$1.75 million (feed item 1)

- Status: on your list. Notion: WATCHLIST / AVOID, not held. Entry Price Max ₹204 (body ₹205), MoS ₹181 (body ₹182). The ladder on the page: above ₹268 is AVOID.
- File: ADF_Foods_Announcement_Under_Regulation_30_LODR_-__1b2db7.pdf, 2 pages, text. Letter dated 10-Oct-26, signed 14:56 [FILED p.1].
- Event [FILED p.1 to 2]. ADF Foods (USA) Ltd, a step-down wholly owned subsidiary, signed a Forbearance Agreement dated 9-Oct-26 with Ascot Valley Foods and its affiliates in the US District Court case (Southern District of New York).
  - Judgments for the subsidiary total about US$2.31 million plus interest. It "conditionally agreed to accept" US$1.75 million plus interest.
  - US$450,000 was received on 9-Oct-26. The balance of US$1.30 million plus interest is payable in monthly instalments of at least US$25,000 over a maximum of 52 months from Nov-26.
  - Ascot must withdraw its appeal. The permanent injunction protecting the recipes and trade secrets "remains fully effective". If Ascot defaults the subsidiary can enforce the original judgments after crediting payments. Satisfaction is conditional on full payment.
  - The letter follows earlier intimations of 28-Jun-26 and 14-Aug-26.
- Arithmetic [INFERENCE]. US$1.75M over US$2.31M is 75.8%, a cut of US$0.56M (24%). 52 x US$25,000 is exactly US$1.30M, so the minimum payment path runs the full term, last instalment Feb 2031. In rupees at ₹94.7 per US$ (implied by the Q1 FY27 note: US$2.08M = ₹19.69 Cr [RECORD, 30-Jul review]): first receipt ₹4.3 Cr, full US$1.75M about ₹16.6 Cr, original US$2.31M about ₹21.9 Cr. The record also holds ₹85.4 per US$ in its Ascot section (28-Jun) [RECORD]. At that rate the amounts are about 10% lower. Minimum cash before 31-Mar-27: US$575,000 (US$450,000 plus five instalments), about ₹5.4 Cr.
- Record test [RECORD].
  - Thesis-broken condition 8, "Ascot final judgment reversed on appeal", and the downgrade trigger "Ascot appeal reversal": with the appeal to be withdrawn, they are effectively retired. They return only if Ascot defaults and reopens the case. The filing does not say that route exists.
  - One-time cash stack FY27 to FY29 (28-Jun): PLI ₹16 Cr, tariff refund about ₹12 Cr, Ascot ₹18 to 22 Cr, total about ₹46 to 50 Cr, with Ascot collected "FY28-29" at 60 to 70% probability. Now the minimum for Ascot inside FY27 to FY29 is about US$1.175M (₹11.1 Cr at ₹94.7) [INFERENCE: US$450,000 plus 29 instalments to Mar-29]. Cash arrives sooner and smaller. The US$575,000 balance falls in FY30 and FY31.
  - Strategic premium: court-validated trade secrets. The injunction stands. Not raised.
  - Tripwire 6 (operating margin under 16% two quarters, tested on Q2, September quarter) is not touched: receipts fall in Q3. The FY27 cash conversion test (0.70x kill line) could be helped by about ₹5.4 Cr of non-operating receipts [INFERENCE].
  - The August Q1 FY27 concall (master gate) is still not logged on the page (03-Oct entry).
- Touches a rule: YES. Thesis-broken condition 8 and the one-time cash stack. No tripwire fires.
- Not said: interest rate, security or guarantee for the instalments, accounting treatment, whether the US$100,706.96 that ADF owed Ascot under the June ruling is netted. NOT FOUND. The 14-Aug-26 intimation is not on file or in the window.
- Price: ₹290 (screener.in, 11-Oct-26 11:02 IST), 52-week ₹153 to ₹347, market cap ₹3,183 Cr. Record ₹273.10 (1-Oct). Up 6.2%. Above the ₹268 AVOID line by ₹22; 1.42x the ₹204 entry max and 1.60x the ₹181 MoS [INFERENCE].

#### E22. India Glycols: GST penalty of ₹6.22 lakh for an e-way bill gap (feed item 20)

- Status: on your list. Notion: WATCHLIST / AVOID, not held. Page title says "pre-demerger shell, splits 2 Sep 2026".
- File: India_Glycols_Intimation_Of_GST_Order_b94904.pdf, 2 pages, text. Letter dated 10-Oct-26, signed 21:55 [FILED p.1].
- Event [FILED p.2 Annexure A]. State Tax Officer, SGST Department, Uttarakhand, passed an order dated 10-Oct-26 levying a penalty of ₹6,22,080 under the GST Act. A vehicle carrying goods under 3 invoices was inspected at Singhniwala, Uttarakhand. "Due to oversight of the transporter" the Part-B details were not updated in the e-way bill for 1 of the 3 invoices. The e-invoice was with the goods and there was no difference in quantity or description. The penalty was deposited to release the vehicle. The company will appeal and is "confident of successfully challenging".
- Record test [RECORD]. The three thesis-broken conditions (opening net debt above about ₹1,050 Cr for one entity and ₹813 Cr for another; bio-glycol realisation falling while the Asia index is flat; Clariant JV profit falling toward ₹30 Cr or its dividend stopping) are not touched.
- Context found outside the window [FILED, file India_Glycols_Clarification_On_Movement_In_Price_f0be20.pdf, previous window's folder, 1 page]: on 8-Oct BSE and NSE asked about the price move; on 9-Oct (signed 15:48) the company replied there is no undisclosed material information and the move "appears to be market-driven".
- Not said: which of the three post-demerger businesses the goods belonged to. NOT FOUND.
- Touches a rule: NO.
- Price: ₹330 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹168 to ₹400, market cap ₹2,209 Cr. Record ₹307.40 (1-Oct, residual company). Up 7.4%. The record put the residual's fair value at about ₹178 and its entry at about ₹91 to ₹105. At ₹330 the price is 85% above that value [INFERENCE].

#### E23. Rathi Steel and Power: GST demand of ₹59.45 lakh (feed item 28)

- Status: NOT on your list.
- File: Rathi_Steel_Disclosure_Under_Regulation_30_Of_Listin_3ed8b0.pdf, 2 pages, text. Letter dated 10-Oct-26, signed 16:36 by the Whole Time Director [FILED p.1].
- Event [FILED p.1 to 2]. Demand order by the Additional Commissioner, GST and Central Excise, Rourkela, dated 8-Oct-26, received 9-Oct-26, under section 74 of the CGST Act, for ₹59,44,859. The demand is "interest on delayed payments of GST liability for the month of January 2021". The company thinks it is "not maintainable" and will "explore appropriate legal remedies". "No material impact" foreseen.
- Reading [INFERENCE from general knowledge]: section 74 is the section used for cases of fraud, wilful misstatement or suppression. The filing says the demand is interest on a late payment and does not say fraud is alleged.
- Size: ₹59.45 lakh is 0.35% of the ₹171 Cr market cap [INFERENCE].
- Touches a rule: NO (not on your list).
- Price: ₹19.80 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹13.5 to ₹29.

#### E24. Shilpa Medicare: European GMP certificate for Unit 4, Jadcherla (feed item 29)

- Status: NOT on your list. (The word "Shilpa" elsewhere in your export is a person, a CFO named Shilpa Kedia, not this company.)
- File: Shilpa_Medicare_Europe_GMP_Approval_Of_Shilpa_Medicare_L_e066ce.pdf, 1 page, text. Letter dated 10-Oct-26, signed 12:31 [FILED p.1].
- Event [FILED p.1]. AGES (Austria) inspected Unit 4, Jadcherla, Telangana from 27 to 30 July 2026. "Following a successful inspection, the Unit has been issued GMP Certification from AGES, Austria". The unit makes sterile injections and non-sterile tablets and capsules (finished dosage forms) for Europe and the rest of the world.
- NOT FOUND in the file: certificate number, issue date, validity, and any observations. They would be on the EU EudraGMP database or the company's regulatory page.
- Touches a rule: NO (not on your list).
- Price: ₹1,022 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹260 to ₹1,096.

### HEADING 7. CALENDAR AND ROUTINE

#### E25. Cyient DLM: earnings call booked for 15 Oct at 5:30 PM (feed item 9)

- Status: on your list. Notion: Decision Status NOT set; Halt 1 pending; model unsigned; no entry or MoS.
- File: Cyient_DLM_Announcement_under_Regulation_30_LODR-An_4c79b7.pdf, 2 pages, text. Letter dated 9-Oct-26, digitally signed 10-Oct 10:50 [FILED p.1].
- Event [FILED p.1 to 2]. The company announces its Ind AS results for the quarter ended 30-Sep-26 on Thursday 15-Oct-26. An earnings call follows at 5:30 PM IST for 60 minutes, with Krishna Bodanapu (non-executive chairman), Rajendra Velagapudi (MD and CEO) and Subramanian RM (CFO). The CIN on page 2 drops its last digit (L31909TG1993PLC14134 against L31909TG1993PLC141346 on page 1).
- Record test [RECORD, 06-Oct entry and 11-Sep stress test].
  - The 06-Oct entry says the board-meeting notice "does not mention an earnings call". This closes that gap: a call is booked for the same day (the board date of 15-Oct is on file).
  - Open ruling: does an H1 FY27 net working capital print above 161 days confirm STRUCTURAL now, or does only the Q4 FY27 print count? The falsifier: net working capital days at or below 120 by Q4 FY27 with positive operating cash flow; "any print above 161 days confirms it". Logged FY26 working capital days 169.
  - Also on the list: a third quarter of gross margin compression without a component cost answer; order book against ₹2,600 Cr and 1.5x book-to-bill at Q1; at least 100 basis points of reported margin gain.
  - The call has the parent's chairman on it. The record has an open question on parent related party flows (₹53.76 Cr of subcontracting charges from nil, payables to the parent up 257%).
- Touches a rule: YES. The cash falsifier date and the open ruling. An intimation fires nothing.
- Price: ₹952 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹265 to ₹1,015, market cap ₹7,560 Cr. Record ₹923 (10-Sep). Up 3.1%. The 52-week high of ₹1,015 is above the ₹1,009.90 all-time high on the record, so a new high was made after 10-Sep [SECONDARY]. No buy level on file.

#### E26. Fedbank Financial Services: Q2 FY27 earnings call on 15 Oct at 4:00 PM (feed items 12 and 13)

- Status: on your list. See E19 for status and buy levels.
- Files: Fedbank_Financi_Announcement_under_Regulation_30_LODR-An_54b43b.pdf (1 page, dated 9-Oct, signed 21:50) and Fedbank_Financi_Announcement_under_Regulation_30_LODR-An_99c20a.pdf (2 pages, dated 10-Oct, signed 23:03). Text. One event.
- Event [FILED]. Earnings call with analysts on Thursday 15-Oct-26 at 4:00 pm IST on Q2 FY27 results. The 10-Oct letter is a "revised intimation" because "the enclosure to the said intimation was inadvertently missed". Page 2 of it is the invitation from Equirus Securities: MD and CEO Parvez Mulla, CFO C. V. Ganesh and senior management.
- Touches a rule: YES, through E27 (the results the call explains).

#### E27. Fedbank Financial Services: board meets 15 Oct to approve Q2 FY27 results (feed item 15)

- File: Fedbank_Financi_Board_Meeting_Intimation_for_Considerati_f63622.pdf, 1 page, text. Letter dated 9-Oct-26, signed 21:25 [FILED p.1].
- Event [FILED p.1]. Board meeting Thursday 15-Oct-26 to consider unaudited results for the quarter and half year ended 30-Sep-26. Trading window closed 1-Oct to 17-Oct, until 48 hours after results. Earlier intimation of 29-Sep-26. The feed summary says "FY26"; the filing means the September 2026 quarter, which is Q2 FY27.
- Record test [RECORD]. The three tripwires: credit cost above 1.1% of average assets (Q1 FY27: 0.8%; guide sub 1%), ROE below 14% by FY28 (Q1: 15.4%), coverage ratio (PCR) below 32% (Q1: 38.36%, guided down; "the tripwire most at risk"; 32.29% at March). The record's single cleanest Q2 test: credit cost against sub 1%; bull at or below 0.9% with PCR at or above 32%, bear above 1.1% or PCR below 32%. Also: CRAR 20.71% at Q1, branch openings (none in Q1 against 200 planned for FY27), gold tonnage.
- Touches a rule: YES. The 15-Oct results are the test for all three tripwires.
- Price: ₹146 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹119 to ₹178, market cap ₹5,492 Cr. Record ₹164 (Jul-26 run). Down 11.0%. On FY26 diluted EPS of ₹9.12 that is 16.0x [INFERENCE]. 1.90x the ₹77 entry max, 2.39x the ₹61 MoS.

#### E28. Aurionpro Solutions: Q2 FY27 earnings call on 2 Nov at 9:30 AM (feed item 6)

- Status: NOT on your list (the name appears once as a peer on the eMudhra page [RECORD]).
- File: Aurionpro_Sol_Announcement_under_Regulation_30_LODR-An_ff9842.pdf, 2 pages, text. Letter dated 9-Oct-26, signed 23:08 [FILED p.1].
- Event [FILED p.1 to 2]. Q2 FY27 earnings call on Monday 2-Nov-26 at 9:30 AM IST, by Zoom. Management: Ashish Rai (Group CEO and Vice Chairman), Vipul Parmar (CFO), Ninad Kelkar (Company Secretary). The date of the results board meeting is NOT FOUND in this file.
- Touches a rule: NO.
- Price: ₹602 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹593 to ₹1,247. 1.5% above the low.

#### E29. Fairchem Organics: board meets 22 Oct for Q2 FY27 results (feed item 11)

- Status: NOT on your list.
- File: Fairchem_Organic_Board_Meeting_Intimation_for_Unaudited_F_8f10d3.pdf, 1 page, text. Letter dated 10-Oct-26, signed 10:10 [FILED p.1].
- Event [FILED p.1]. Board meeting Thursday 22-Oct-26 by audio visual means to approve unaudited results for the quarter and half year ended 30-Sep-26. The trading window "shall continue to remain closed" from 1-Oct-26 to 26-Oct-26. The feed summary says "FY26"; the quarter is September 2026.
- Touches a rule: NO.
- Price: ₹749 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹428 to ₹847.

#### E30. Poonawalla Fincorp: CRISIL credit bulletin of 9 Oct, no rating change (feed item 24, no PDF)

- Status: NOT on your list (mentioned once on the EMBDL page [RECORD]).
- File: none in the zip. I found the CRISIL document on the web (link on the Screener page): "Credit Bulletin, October 09, 2026" (PoonawallaFincorpLimited_October 09_ 2026_RR_407420.html), read in full [AGENCY].
- Content. "This Credit Bulletin is published solely to update the bank-wise facility details in line with RBI requirement." For all other sections it refers to the rating rationale of 9-Sep-26. It lists lenders and amounts, all rated Crisil AAA/Stable, for example Punjab National Bank ₹1,800 Cr, SIDBI ₹1,462 Cr, ₹1,500 Cr and ₹1,000 Cr, Union Bank of India ₹1,000 Cr, State Bank of India ₹969.17 Cr, and a proposed long term facility of ₹5,936.29 Cr. No operating numbers.
- Placement: a bare rating with no operating detail goes under Calendar and routine.
- Touches a rule: NO (not on your list).
- Price: ₹447 (screener.in, 11-Oct-26 11:03 IST), 52-week ₹361 to ₹545.

## 5. Duplicates and feed problems

| Case | Detail |
|---|---|
| TIPCO items 31 and 32 | Same file byte for byte. Listed once (E17). |
| Yaap items 36 and 37 | Same file byte for byte. Item 35 is the NSE zip with the XBRL form and the same email. One event (E18). |
| Premier items 25 and 26 | Two different files. Same results under two cover letters ("results" and "board outcome"). One event (E05). |
| Fedbank items 12 and 13 | Two different files. The 9-Oct notice lacked its enclosure; the 10-Oct revised notice carries it. One event (E26). |
| Airfloa items 4 and 5 | Two different documents (press release and Reg 30 disclosure), same MOU. One event (E02). |
| Oswal items 22 and 23 | Two different documents (press release and Reg 30 disclosure), same board decisions. One event (E11). |
| Deep Industries item 10 and Tinna Rubber item 34 | Byte-identical to files of the same name in the previous window's folder. The rating press releases are dated 9 Oct. They were fed again in this window. Listed once, here. |
| Items with no PDF | Items 2 (Aarti Pharma) and 24 (Poonawalla): the morning download found no document. |
| Wrong documents behind a link | None. Every PDF is the filing of the company named. |
| Wrong or weak exchange summaries | Fedbank board notice and Fairchem say "FY26" where the filings mean the September 2026 quarter (Q2 FY27). Premier "H1 revenue Rs 216.83 crore" is total income. Item 35 (Yaap) has a generic summary. |
| Drafting errors inside filings | Airfloa press release names "Prime Cable Industries Limited" in its disclaimer. Cyient DLM CIN on page 2 drops a digit. Oswal press release says "Commenting on the order" for a capex decision. Quality Power's EGM notice carried three errors (E12). |

## 6. Documents used from outside the 35 PDFs

| Document | Where from | Used in |
|---|---|---|
| Bajel_Projects_Announcement_under_Regulation_30_LODR-Aw_4e736f.pdf (order filing naming Tata Power) | Previous window's folder, same zip | E01 |
| Hexaware_Tech_Scrutinizers_Report_On_Postal_Ballot_1b0f2b.pdf (20 pages) | Previous window's folder; same MD5 as the BSE file | E13 |
| India_Glycols_Clarification_On_Movement_In_Price_f0be20.pdf | Previous window's folder; same MD5 as the BSE file | E22 |
| Aequs_Aequs_Limited_Company_Has_informed_About_bbc900.pdf (Ajna JV) | Previous window's folder; same MD5 as the BSE file | E15 |
| Aarti_Pharma_Board_Meeting_Intimation_for_Approval_Of_d0c932.pdf | Previous window's folder | E03 |
| Yaap board outcome of 8-Oct-26 (4 pages) | NSE archives, fetched 11-Oct | E18 |
| Aequs Reg 29(2) disclosure of 8-Oct-26, Amansa Investments (3 scanned pages) | BSE, fetched 11-Oct, OCR and read by eye | E15 |
| Quality Power corrigendum, website copy (1 page) | qualitypower.com, fetched 11-Oct | E12 |
| CRISIL rating rationale for Aarti Pharmalabs, 9-Oct-26 | crisil.com, fetched 11-Oct | E03 |
| CRISIL credit bulletin for Poonawalla Fincorp, 9-Oct-26 | crisil.com, fetched 11-Oct | E30 |
| screener.in company pages (28) | fetched 11-Oct, 11:02 to 11:05 IST | prices; announcement lists used to find the documents above |

Everything else in the other folder (about 55 other PDFs of the previous window) was not read.

## 7. Documents that could not be fetched (NOT FOUND) and where they sit

| Missing document | Why it matters | Where it would be found |
|---|---|---|
| Oswal Pumps postal ballot notice and explanatory statement on the IPO objects change | Cost split, lender terms, return expectations, exit offer for dissenters | BSE and NSE announcements once issued ("in due course") |
| Quality Power EGM notice explanatory statement for the Rs 700 Cr QIP | Use of about Rs 575 Cr beyond the Rs 123.84 Cr cash leg | BSE, NSE and qualitypower.com, EGM notice of 26-Sep-26 |
| Heritage Foods intimations of 16-Jul-26 and 29-Aug-26 | Amount paid for the 5.60% stake | BSE and NSE announcement pages |
| Hexaware postal ballot notice dated 2-Sep-26 | Size and cost of the RSU plan | hexaware.com investor page, BSE and NSE |
| Yaap Tranche 2 amendment agreement filing | Cash paid for the next 20% of Gozoop | NSE announcements after execution |
| Aequs filing that states why the pledge was released | The "regulatory requirement" | The next Aequs Reg 31 or Reg 30 filing; the 22-Oct EGM notice |
| Shilpa Medicare EU GMP certificate | Number, date and validity | EudraGMP database; company regulatory page |

## 8. Record conflicts and fixes

Fixes (two conflicting figures, stale values, typos). Each appears again in the Notion save list in BRIEF.md.

| Company | Field | Old value | New value | Why |
|---|---|---|---|---|
| Aarti PharmaLabs | Ticker | AARTIPHARMA | AARTIPHARM | The old code does not load on screener.in. The new code is the NSE symbol on the company's own letter of 9-Oct-26 |
| Oswal Pumps | Ticker | OSWAL | OSWALPUMPS | Exchange letters of 10-Oct-26 say "Name of Scrip: OSWALPUMPS"; OSWAL does not load on screener.in |
| Yaap Digital | Snapshot: Chairman & MD | Atul Hegde | Laxmiraj Seetharam Nayak (CMD; resigned effective 9-Oct-26) | The 01-Oct Key Notes and the filings name Nayak. Hegde's present role is NOT FOUND |
| ADF Foods | Exchange rate used for the Ascot amounts | ₹85.4 per US$ (28-Jun entry) | ₹94.7 per US$ (implied by Q1 FY27 Note 6) | Two rates sit on one page |
| ADF Foods | Entry Price Max, MoS (properties) | ₹204 and ₹181 | ₹205 and ₹182 | The page body says ₹205 and ₹182; already listed on the page as awaiting your confirmation |
| India Glycols | Entry Price Max (property) | ₹429 (pre-demerger) | about ₹105 (top of the residual zone ₹91 to ₹105, 25-Aug value study) | Properties are pre-demerger. The MoS for the residual is NOT FOUND; ₹222 is pre-demerger |
| Prices (14 names) | Current Market Price | see section 2.1 | see section 2.1 | Stale. Refreshed from screener.in on 11-Oct-26 |

Conflicts that need a ruling, not a fix:

- Oswal Pumps: the entry zone of ₹350 to ₹435 on the page body against "entry price NOT SET" in the Key Notes, and the EPS built on about 6.1 Cr shares against about 11.4 Cr actual (E11).
- Oswal Pumps: whether the ₹280 price condition applies to a name you never held (E11).
- Garware: price zone table says AVOID above ₹5,000 while Decision Status is WATCHLIST (already pending on the page).
- Aequs: the proposed pledge warning line is not yet adopted.

## 9. Cross-check against the REVIEW.md that came inside the zip

I did not use it. I wrote every entry from the PDFs. After finishing I read it and compared. Where we agree: the 14 and 14 split of companies, the 37 image pages, the Oswal and TIPCO findings, the Aequs, ADF, Cyient DLM, Fedbank and Quality Power readings, and all 28 prices (identical to the rupee, read at 08:28 IST by the morning script and again by me at about 11:03 IST).

Where I went further or differ:

1. Yaap: the 8-Oct board outcome (auditor Shweta Jain & Co resigned effective 23-Sep, new firm appointed, Gozoop Tranche 2 cash approved) is not in the older file, which says a second auditor exit "would settle" the bear reading. It had already happened.
2. Bajel: the customer is Tata Power, from the 9-Oct order filing in the previous window's folder. The older file says the client is undisclosed.
3. Aarti Pharma and Poonawalla: I found and read the CRISIL documents. The older file says "agency, rating and direction unknown".
4. Hexaware: the RSU plan vote of 9-Oct (public institutions 77.5% against) is new.
5. Aequs: the Amansa sale (7.48% to 5.35%) and the Ajna JV investment are new.
6. Oswal: I confirm the share count problem independently from the record's own numbers (E11).
7. Deep Industries and Tinna Rubber PDFs are duplicates of the previous window's files. The older file treats them as new.
8. Rupee conversion for ADF: the older file used ₹94.7 per US$. I show both rates the record holds and flag the conflict.
9. Item counts: the older file counts 155 pages in 34 PDFs plus the zip. I count 156 because I counted the one-page PDF inside the Yaap zip.
