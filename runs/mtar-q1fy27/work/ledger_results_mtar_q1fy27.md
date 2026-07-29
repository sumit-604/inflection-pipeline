# A2 COMPLETENESS LEDGER — MTAR Technologies Limited (MTAR), Q1 FY27, RESULTS filing

Source: /home/user/inflection-pipeline/runs/mtar-q1fy27/work/extract_results_mtar_q1fy27.txt (585 lines, 9 pages)
Prior-quarter ledger: NONE AVAILABLE (first quarterly pipeline run for this ticker) — all
cross-quarter checks (ENTITY_CHANGE, DROPPED_SLIDE-equivalent) are marked N/A below, not
"no change."

```
=== A2 COUNT TEST ===
category: notes             grep_count: 11   sweep_count: 11   match: yes
category: line_items        grep_count: 68   sweep_count: 68   match: yes
category: zero_standing     grep_count: 8    sweep_count: 8    match: yes
category: agenda_items      grep_count: 7    sweep_count: 7    match: yes
category: auditor_paras     grep_count: 26   sweep_count: 26   match: yes
category: entities           grep_count: 3    sweep_count: 3    match: yes
category: annexure_profiles grep_count: 2    sweep_count: 2    match: yes
category: signature_blocks  grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Count-test method notes (per category)
- **notes**: `grep -n -E "^\s*[0-9]+\s+[A-Z]"` restricted to consolidated Notes block
  (lines 428-441) returns 6. The standalone Notes block (lines 358-369) has its leading
  digit glyphs dropped by the pdftotext -layout renderer (same artifact class as A1's
  decimal-glyph note, confirmed by cross-reference to the "(refer note 2)" / "Refer note
  5" table anchors at lines 320 and 338, and by 1:1 structural match to the consolidated
  block's paragraph content) — grep re-run with content-anchored sentence-start patterns
  on that range returns 5. Combined grep 6+5=11 = manual sweep 11. Match.
- **line_items**: `awk 'NR>=321&&NR<=355 && NF>0'` → 35 raw lines (standalone table),
  minus 1 for the single item whose header text wraps across two extract lines (352-353,
  "Earnings per share..." caption) = 34. `awk 'NR>=392&&NR<=425 && NF>0'` → 34 raw lines
  (consolidated table, no wraps). Combined 34+34=68 = manual sweep 68. Match.
- **zero_standing**: `grep -n -E "(Statutory impact|Adjustment of tax|Items that will not|Total
  other comprehensive)"` restricted to each table range → 4 standalone + 4 consolidated = 8
  = manual sweep 8. Match.
- **agenda_items**: `grep -n -E "^\s*[0-9]+\."` on Board Outcome letter body (lines 104-121)
  → 7 = manual sweep 7. Match.
- **auditor_paras**: blank-line-delimited block count (awk paragraph mode) on standalone
  report range (459-547) → 10; on consolidated report range (557-692) → 16. Combined 26 =
  manual sweep 26 (sweep aligned to the same block boundaries, including two non-substantive
  structural blocks — a page-break marker and a repeated letterhead — both enumerated and
  flagged as such, not silently dropped). Match.
- **entities**: `grep -oE "MTAR Technologies Limited|Gee Pee Aerospace and Defence Private
  Limited|Magnatar Aero Systems Private Limited"` restricted to the Group-definition sentence
  (consolidated note 1, lines 429-430) → 3 unique names = manual sweep 3. Match.
- **annexure_profiles**: count of distinct director names in Annexure A column headers
  (page 3, line 210: "Mr. Rohith Loka Reddy", "Mr. Anushman Reddy") = 2 = manual sweep 2
  (cross-checked against Board Outcome agenda items 3 and 4, lines 109-112). Match.
- **signature_blocks**: `grep -n "Digitally signed by"` → 2 (Priyanka Agarwal, lines 150,
  279) + count of "For S.R. Batliboi" / "For S.R. BATLIBOI" firm sign-offs → 2 (lines 527,
  679) = 4 = manual sweep 4. Match.
- Independent scan of pages 5-6 for decimal-glyph artifacts beyond A1's six flagged cells
  (`grep -nE '[0-9]{1,3},[0-9]{2}([^0-9,]|$)'` and `grep -nE '[0-9]:[0-9]{2}'` on lines
  310-425) returns exactly the same six cells A1 already flagged — no additional cells found.

---

## 1. BOARD OUTCOME LETTER — administrative / meta (page 1-2, informational, not counted
   toward agenda_items)

| Item | Line | Content |
|---|---|---|
| Addressees | 85-88 | BSE Limited (Scrip Code 543270) and National Stock Exchange of India Limited (Symbol MTARTECH) |
| Date of letter | 83 | "Date: 29th July, 2026" (superscript rendered as `"`) |
| Unit / ISIN | 93-94 | MTAR Technologies Limited; ISIN INE864101014 |
| Subject line | 97 | "Outcome of the Board Meeting" |
| Meeting date/venue | 100-102 | Wednesday, 29th July 2026, at registered office of the Company |
| **Meeting START time** | 101 | **3:00 p.m.** |
| **Meeting END (concluded) time** | 139 | **3:35 p.m.** — duration 35 minutes |
| Closing / valediction | 142-149 | "This is for the information and records... Yours sincerely, For MTAR Technologies Limited" |

**Signature-timing check** (per instruction #7): digital signature timestamp on this letter
is 2026.07.29 16:34:40 (line 169) — after the 3:35 p.m. (15:35) meeting conclusion. No
`SIGNATURE_BEFORE_MEETING` flag warranted; check performed and PASSED.

## 2. BOARD OUTCOME — AGENDA ITEMS (7 of 7 enumerated, page 1, lines 104-121)

| # | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 105-106 | "Un-audited Financial Results (Standalone and Consolidated) for the quarter ended 30.06.2026. (Attached)" | — |
| 2 | 107-108 | "Limited Review Reports (Standalone and Consolidated) for the quarter ended 30.06.2026. (Attached)" | — |
| 3 | 109-110 | "Re-appointment of Mr. Rohith Loka Reddy (DIN: 06464331) as Director of the Company, Retiring by rotation." | — |
| 4 | 111-112 | "Re-appointment of Mr. Anushman Reddy (DIN: 08104131) as Director of the Company, Retiring by rotation." | — |
| 5 | 113-116 | "Notice of the Annual General Meeting (AGM), the Directors' Report along with the Annexures thereto, the BRSR, the MD&A, and the Corporate Governance Report for FY ended 31.03.2026." | — |
| 6 | 117-118 | "Annual General Meeting for the FY 2025-26 is scheduled to be held on Monday, 28th September 2026 through video conference..." | — |
| 7 | 119-120 | "Appointment of M/s. S.S. Reddy & Associates, Practicing Company Secretaries, as scrutinizers for conducting E-voting in the ensuing AGM." | — |

## 3. ANNEXURE A — DIRECTOR PROFILES (page 3-4)

### 3a. Director profile summary (2 rows, one per director)

| Director | Line (start) | DIN | Role | Term | Background (first clause) | Relationships disclosed |
|---|---|---|---|---|---|---|
| Mr. Rohith Loka Reddy | 210 (col start), profile detail 228-234 | 06464331 (from agenda item 3, line 109) | Director, retiring by rotation, re-appointment subject to shareholder approval at ensuing AGM | w.e.f. ensuing AGM (line 216-219) | MBA, Indian School of Business; Bachelors in Science in Economics-Finance from Bentley University, Boston, USA; expertise in Finance and Investment (228-234) | Related to Mr. P. Srinivas Reddy, Managing Director of the Company (259-263); not related to any other Director/KMP; not debarred by SEBI/BSE/NSE order per BSE Circular ref (264-269) |
| Mr. Anushman Reddy | 210 (col start), profile detail 228-241 | 08104131 (from agenda item 4, line 111) | Director, retiring by rotation, re-appointment subject to shareholder approval at ensuing AGM | w.e.f. ensuing AGM (line 216-219) | Bachelor's in Mechanical Engineering, JNTU; MS global supply chain management, Marshall School of Business (USC); Executive PG diploma, Narsee Monjee Institute of Management; expertise in export operations, supply chain, cost reduction, greenfield lean manufacturing setup (228-241) | Related to Mr. Praveen Kumar Reddy, Whole Time Director of the Company (259-263); not related to any other Director/KMP; not debarred by SEBI/BSE/NSE order per BSE Circular ref (264-269) |

### 3b. Annexure A field-level table (5 field rows, both director columns per row)

| Field | Line | Rohith Loka Reddy content | Anushman Reddy content |
|---|---|---|---|
| Reason for change (appointment/resignation/removal/death/otherwise) | 211-214 | Re-appointment, Director, Retiring by rotation | Re-appointment, Director, Retiring by rotation |
| Date of Appointment and Terms of Appointment | 216-227 | w.e.f. ensuing AGM, subject to shareholder approval; reappointment retiring by rotation | w.e.f. ensuing AGM, subject to shareholder approval; reappointment retiring by rotation |
| Brief Profile | 228-241 | MBA (ISB), BSc Economics-Finance (Bentley Univ., Boston); Finance & Investment expertise | BE Mechanical (JNTU), MS supply chain (Marshall/USC), Exec PGDM (NMIMS); export ops/supply chain/cost reduction/greenfield lean mfg expertise |
| Disclosure of relationships between directors (Regulation 30, SEBI Master Circular dated Jan 30, 2026) | 259-263 | Related to Mr. P. Srinivas Reddy, Managing Director | Related to Mr. Praveen Kumar Reddy, Whole Time Director |
| Information re: BSE Circular LIST/COMP/14/2018-19 & NSE ref NSE/CML/2018/24 (debarment) | 264-274 | Not debarred by SEBI/other statutory authority | Not debarred by SEBI/other statutory authority |

## 4. FINANCIAL RESULTS — STANDALONE TABLE (page 5, lines 321-355; 34 line items, INR millions)
Columns: 30-Jun-26 (Unaudited) | 31-Mar-26 (Audited, refer note 2) | 30-Jun-25 (Unaudited) | 31-Mar-26 Year ended (Audited)

| Line | Item | 30-Jun-26 | 31-Mar-26 (Q) | 30-Jun-25 | FY26 (year) | Flags |
|---|---|---|---|---|---|---|
| 321 | 1. Income (header) | — | — | — | — | header |
| 322 | (a) Revenue from operations (subheader) | — | — | — | — | header |
| 323 | (i) Sale of Products | 3,558.92 | 3,028.37 | 1,544.10 | 8,653.19 | — |
| 324 | (ii) Other operating revenue | 48.29 | 31.93 | 21.74 | 107.89 | — |
| 325 | Total Revenue from Operations | 3,607.21 | 3,060.30 | 1,565.84 | 8,761.08 | — |
| 326 | (b) Other income | 80.36 | 165.41 | 7.59 | 236.88 | — |
| 327 | Total income | 3,687.57 | 3,225.71 | 1,573.43 | 8,997.96 | — |
| 328 | 2. Expenses (header) | — | — | — | — | header |
| 329 | (a) Cost of materials consumed | 2,042.72 | 1,649.49 | 927.74 | 5,034.25 | — |
| 330 | (b) Changes in inventory of work in progress | (80.61) | 59.70 | (210.92) | (447.64) | — |
| 331 | (c) Employee benefit expenses | 457.71 | 424.39 | 339.12 | 1,488.34 | — |
| 332 | (d) Finance costs | 158.47 | 96.07 | 58.16 | 293.44 | — |
| 333 | (e) Depreciation and amortisation expenses | 94.76 | 88.80 | 81.94 | 343.63 | — |
| 334 | (f) Other expenses | 338.12 | 311.16 | 225.42 | 975.58 | — |
| 335 | Total expenses | 3,011.17 | 2,629.61 | 1,421.46 | 7,687.60 | — |
| 336 | 3. Profit before exceptional items and tax (1-2) | 676.40 | 596.10 | 151.97 | 1,310.36 | — |
| 337 | 4. Exceptional Items (header) | — | — | — | — | header |
| 338 | Statutory impact of new Labour Codes (Refer note 5) | "~" (nil-glyph) | "-" | "-" | 37.67 | ZERO_STANDING; note also a non-A1-flagged dash-glyph rendered as "~" in the 30-Jun-26 cell — unambiguous nil, no arithmetic disambiguation needed |
| 339 | 5. Profit before tax (3-4) | 676.40 | 596.10 | 151.97 | 1,272.69 | — |
| 340 | 6. Tax expense (header) | — | — | — | — | header |
| 341 | (a) Current tax | 151.39 | 157.33 | 8.87 | 302.48 | — |
| 342 | (b) Adjustment of tax relating to earlier periods | "-" | (8.26) | "-" | (8.26) | ZERO_STANDING (nil in Jun-26 and Jun-25 cols) |
| 343 | (c) Deferred tax charge | 19.97 | 3.66 | 30.81 | 25.23 | — |
| 344 | Total tax expense | **171.36 (VERIFIED, A1 note line 30; raw "171,36")** | 152.73 | 39.68 | 319.45 | see A1 verification note |
| 345 | 7. Net profit for the period (5-6) | 505.04 | 443.37 | 112.29 | 953.24 | — |
| 346 | 8. Items of other comprehensive loss (net of tax) (header) | — | — | — | — | header |
| 347 | Items that will not be reclassified to statement of profit and loss | "-" | (3.61) | "-" | (3.61) | ZERO_STANDING |
| 348 | Total other comprehensive loss (net of tax) | "-" | (3.61) | "-" | (3.61) | ZERO_STANDING |
| 349 | 9. Total comprehensive income (7+8) | 505.04 | 439.76 | 112.29 | 949.63 | — |
| 350 | 10. Paid-up equity share capital (face value INR 10/share) | 307.59 | 307.59 | 307.59 | 307.59 | — |
| 351 | 11. Other equity | (blank) | (blank) | (blank) | 7,949.23 | Only year-end column populated — blank not dash; standard treatment for this balance-sheet line in a quarterly statement, not asserted as ZERO_STANDING |
| 352-353 | 12. Earnings per share (of INR 10 each) (not annualised) (amount in INR) (header, wraps 2 lines) | — | — | — | — | header |
| 354 | - Basic earnings per share | 16.42 | 14.41 | 3.65 | 30.99 | — |
| 355 | - Diluted earnings per share | 16.42 | 14.41 | 3.65 | 30.99 | — |

## 5. FINANCIAL RESULTS — CONSOLIDATED TABLE (page 6, lines 392-425; 34 line items, INR millions)
Columns: 30-Jun-26 (Unaudited) | 31-Mar-26 (Audited, refer note 3) | 30-Jun-25 (Unaudited) | 31-Mar-26 Year ended (Audited)

| Line | Item | 30-Jun-26 | 31-Mar-26 (Q) | 30-Jun-25 | FY26 (year) | Flags |
|---|---|---|---|---|---|---|
| 392 | 1. Income (header) | — | — | — | — | header |
| 393 | (a) Revenue from operations (subheader) | — | — | — | — | header |
| 394 | (i) Sale of Products | 3,558.92 | 3,028.77 | 1,544.10 | 8,654.01 | — |
| 395 | (ii) Other operating revenue | **48.29 (VERIFIED, A1 note line 35; raw "48,29")** | 31.92 | 21.74 | 108.05 | see A1 verification note |
| 396 | Total Revenue from Operations | 3,607.21 | 3,060.69 | 1,565.84 | 8,762.06 | — |
| 397 | (b) Other income | 78.87 | 163.95 | 6.10 | 230.90 | — |
| 398 | Total income | 3,686.08 | 3,224.64 | 1,571.94 | 8,992.96 | — |
| 399 | 2. Expenses (header) | — | — | — | — | header |
| 400 | (a) Cost of materials consumed | 2,043.19 | 1,650.01 | 927.74 | 5,034.80 | — |
| 401 | (b) Changes in inventory of work in progress | (78.16) | 56.60 | (210.92) | (450.74) | — |
| 402 | (c) Employee benefit expenses | 465.20 | 430.49 | 343.20 | 1,509.13 | — |
| 403 | (d) Finance costs | 158.47 | 96.21 | 58.15 | 293.58 | — |
| 404 | (e) Depreciation and amortisation expenses | 96.92 | 90.38 | 83.66 | 350.25 | — |
| 405 | (f) Other expenses | 326.44 | 305.53 | 221.98 | 956.81 | — |
| 406 | Total expenses | 3,012.06 | 2,629.22 | 1,423.81 | 7,693.83 | — |
| 407 | 3. Profit before exceptional items and tax (1-2) | 674.02 | 595.42 | 148.13 | 1,299.13 | — |
| 408 | 4. Exceptional Items (header) | — | — | — | — | header |
| 409 | Statutory impact of new Labour Code (Refer note 6) | "-" | "-" | "i" (nil-glyph) | 37.67 | ZERO_STANDING; non-A1-flagged glyph anomaly in Jun-25 cell ("i" instead of "-") — unambiguous nil in structural context, no arithmetic disambiguation needed |
| 410 | 5. Profit before tax (3-4) | 674.02 | 595.42 | 148.13 | 1,261.46 | — |
| 411 | 6. Tax expense (header) | — | — | — | — | header |
| 412 | (a) Current tax | 151.39 | 157.33 | 8.87 | 302.48 | — |
| 413 | (b) Adjustment of tax relating to earlier periods | "-" | (8.26) | "-" | (8.26) | ZERO_STANDING |
| 414 | (c) Deferred tax charge | 20.36 | **3.52 (VERIFIED, A1 note line 41; raw "3:52")** | 31.13 | **26.94 (VERIFIED, A1 note line 46; raw "26,94")** | see A1 verification note (two cells this row) |
| 415 | Total tax expense | 171.75 | 152.59 | 40.00 | 321.16 | — |
| 416 | 7. Net profit for the period (5-6) | 502.27 | 442.83 | 108.13 | 940.30 | — |
| 417 | 8. Items of other comprehensive loss (net of tax) (header) | — | — | — | — | header |
| 418 | Items that will not be reclassified to statement of profit and loss | "-" | (3.61) | "-" | (3.61) | ZERO_STANDING |
| 419 | Total other comprehensive loss (net of tax) | "-" | (3.61) | "-" | (3.61) | ZERO_STANDING |
| 420 | 9. Total comprehensive income (7+8) | 502.27 | 439.22 | 108.13 | 936.69 | — |
| 421 | 10. Paid-up equity share capital (face value INR 10/share) | 307.59 | 307.59 | 307.59 | 307.59 | — |
| 422 | 11. Other equity | (blank) | (blank) | (blank) | 7,918.28 | Only year-end column populated — blank not dash |
| 423 | 12. Earnings per share (of INR 10 each) (not annualised) (amount in INR) (header) | — | — | — | — | header |
| 424 | - Basic earnings per share | **16.33 (VERIFIED, A1 note line 52; raw "16,33")** | 14.40 | 3.52 | 30.57 | see A1 verification note |
| 425 | - Diluted earnings per share | 16.33 | 14.40 | **3.52 (VERIFIED, A1 note line 58; raw "352", no decimal)** | 30.57 | see A1 verification note |

**Cross-table note**: standalone Net profit (505.04, Jun-26, line 345) exceeds consolidated
Net profit (502.27, Jun-26, line 416) by 2.77, consistent with the two subsidiaries (Gee Pee
Aerospace, Magnatar Aero Systems) contributing a net loss at consolidation — enumerated for
downstream reconciliation, not interpreted here.

## 6. STANDALONE NOTES (page 5, lines 358-369; 5 notes — leading digit glyphs dropped by
   pdftotext -layout, positional numbering inferred from parallel structure with consolidated
   notes 1-2-4-5-6 minus the Group-composition note, and cross-checked against in-table
   references "(refer note 2)" line 320 and "Refer note 5" line 338)

| Note # (inferred) | Line | First 15 words |
|---|---|---|
| [1] | 359-362 | "The unaudited Financial results of the Company have been prepared in accordance with the Indian Accounting Standards..." |
| [2] | 363-364 | "The figures for the quarters ended March 31, 2026 are the balancing numbers between audited figures..." |
| [3] | 365-366 | "The Company has filed the scheme for the merger of its wholly owned subsidiaries, Gee Pee Aerospace..." |
| [4] | 367 | "The Company's business activity falls within a single line of business segment in terms of Ind AS 108..." |
| [5] | 368-369 | "Exceptional item for the year ended March 31, 2026 represents one-time increase in provision of INR 37.67 million..." |

## 7. CONSOLIDATED NOTES (page 6, lines 429-441; 6 notes, explicitly numbered in source)

| Note # | Line | First 15 words |
|---|---|---|
| 1 | 429-430 | "The unaudited Financial results include the financial results of MTAR Technologies Limited ('the Company') and the financial results of its subsidiaries, Gee Pee..." |
| 2 | 431-434 | "The unaudited Financial results of the Group have been prepared in accordance with the Indian Accounting Standards..." |
| 3 | 435-436 | "The figures for the quarters ended March 31, 2026 are the balancing numbers between audited figures..." |
| 4 | 437-438 | "The Company has filed the scheme for the merger of its wholly owned subsidiaries, Gee Pee Aerospace..." |
| 5 | 439 | "The Group's business activity falls within a single line of business segment in terms of Ind AS 108..." |
| 6 | 440-441 | "Exceptional item for the year ended March 31, 2026 represents one-time increase in provision of INR 37.67 million..." |

## 8. AUDITOR'S REVIEW REPORT — STANDALONE (S.R. Batliboi & Associates LLP; page 7, lines
   452-547; 10 structural blocks)

| Block | Line | Content type | Detail |
|---|---|---|---|
| 1 | 459-464 | Title | "Independent Auditor's Review Report on the Quarterly Unaudited Standalone Financial Results of the Company Pursuant to Regulation 33 of the SEBI (LODR) Regulations, 2015, as amended" |
| 2 | 465-467 | Addressee | "Review Report to / The Board of Directors / MTAR Technologies Limited" |
| 3 | 469-478 | Body para 1 | "We have reviewed the accompanying Statement of unaudited standalone financial results of MTAR Technologies Limited... for the quarter ended June 30, 2026..." — scope statement |
| 4 | 479-491 | Body para 2 | "The Company's Management is responsible for the preparation of the Statement in accordance with... Ind AS 34..." — management responsibility |
| 5 | 493-510 | Body para 3 | "We conducted our review of the Statement in accordance with SRE 2410... Accordingly, we do not express an audit opinion." — review scope/basis (no audit opinion) |
| 6 | 512-524 | Body para 4 — Conclusion | "Based on our review conducted as above, nothing has come to our attention that causes us to believe that the accompanying Statement... has not disclosed the information required... or that it contains any material misstatement." — **UNMODIFIED conclusion; no EoM, no Other Matters, no Going Concern paragraph present anywhere in this report** |
| 7 | 527-529 | Signature — firm attribution | "For S.R. BATLIBOI & ASSOCIATES LLP, Chartered Accountants, ICAI Firm registration number: 101049W/E300004" |
| 8 | 532-535 | Signature — partner | Partner name rendered illegibly in text layer ("BE, Bhargang_" / "per Atin sacra 7"), Partner, Membership No.: 504777 |
| 9 | 537-539 | Signature — UDIN/place/date | "UDIN: 2650477 1 DMUF RT 3484" (raw, spacing artifact), Place: Hyderabad, Date: July 29, 2026 |
| 10 | 544-547 | Footer boilerplate | "S.R. Batliboi & Associates LLP, a Limited Liability Partnership with LLP Identity No. AAB-4295, Regd. Office: 22, Camac Street, Block 'B', 3rd Floor, Kolkata-700 016" |

Flags: `SIGNATURE_ILLEGIBLE` (block 8 — partner name not cleanly machine-readable in the
text layer, consistent with a handwritten/image signature overlaid on printed text).

## 9. AUDITOR'S REVIEW REPORT — CONSOLIDATED (S.R. Batliboi & Associates LLP; pages 8-9,
   lines 552-693; 16 structural blocks, 2 of which are pagination/letterhead artifacts and
   still enumerated below, not silently dropped)

| Block | Line | Content type | Detail |
|---|---|---|---|
| 1 | 557-561 | Title | "Independent Auditor's Review Report on the Quarterly Unaudited Consolidated Financial Results of the Company Pursuant to Regulation 33 of the SEBI (LODR) Regulations, 2015, as amended" |
| 2 | 563-565 | Addressee | "Review Report to / The Board of Directors / MTAR Technologies Limited" |
| 3 | 567-577 | Body para | "We have reviewed the accompanying Statement of Unaudited Consolidated Financial Results of MTAR Technologies Limited (the 'Holding Company') and its subsidiaries (together 'the Group') for the quarter ended June 30, 2026..." — scope statement |
| 4 | 579-591 | Body para | "The Holding Company's Management is responsible for the preparation of the Statement in accordance with... Ind AS 34..." — management responsibility |
| 5 | 593-609 | Body para | "We conducted our review of the Statement in accordance with SRE 2410... Accordingly, we do not express an audit opinion." — review scope/basis |
| 6 | 611-614 | Body para | "We also performed procedures in accordance with the Master Circular issued by SEBI under Regulation 33(8) of the Listing Regulations, to the extent applicable." — referenced later in the report as "paragraph 3 above" (line 621, 673) |
| 7 | 616-619 | Entity list | "The Statement includes the results of the following entities: a. Gee Pee Aerospace and Defence Private Limited; b. Magnatar Aero Systems Private Limited" |
| 8 | 620-634 | Conclusion (part 1) | "Based on our review conducted and procedures performed as stated in paragraph 3 above and based on the consideration of the review/audit reports of other auditors referred to in paragraph 6 below, nothing has come to our attention... has not disclosed the information required... or that it contains any material misstatement." — **UNMODIFIED conclusion; no EoM, no explicitly headed "Other Matters," no Going Concern paragraph — but see block 9 below for the entities-reviewed-by-other-auditors disclosure, which is Other-Matters-type content without the formal heading** |
| 9 | 637-646 | Other-Matters-type disclosure | "The accompanying Statement includes the unaudited interim financial results... in respect of: two subsidiaries, whose unaudited interim financial results include total revenues of Rs 16.79 million, total net loss after tax of Rs. 7.22 million, and total comprehensive loss of Rs. 7.22 million, for the quarter ended June 30, 2026... which have been reviewed by their respective independent auditors." |
| 10 | 651-654 | Footer boilerplate | "S.R. Batliboi & Associates LLP, a Limited Liability Partnership with LLP Identity No. AAB-4295, Regd. Office: 22, Camac Street, Block 'B', 3rd Floor, Kolkata-700 016" |
| 11 | 657 | **Pagination marker (extraction artifact, not source report content)** | "[page 9]" |
| 12 | 659-663 | **Letterhead recurrence (page-9 header, not a report paragraph)** | "S.R. BATLIBOI & ASSOCIATES LLP / Chartered Accountants" (badly OCR/text-layer garbled: "S.R. BATL & IB / ASSOCI / OI ATES LLP") |
| 13 | 666-673 | Other-Matters-type disclosure (continued) | "The independent auditor's reports on unaudited interim financial results and other financial information of these entities have been furnished to us by the Management and our conclusion on the Statement, in so far as it relates to the amounts and disclosures in respect of these subsidiaries, is based solely on the report of such auditors and procedures performed by us as stated in paragraph 3 above." — **explicit disclosure that the two subsidiaries' review reports were management-furnished, not independently obtained** |
| 14 | 675-681 | Conclusion (part 2) + firm sign-off attribution (no blank-line break between them in source) | "Our conclusion on the Statement in respect of matters stated in para above is not modified with respect to our reliance on the work done and the reports of the other auditors." followed immediately by "For S.R. Batliboi & Associates LLP, Chartered Accountants, ICAI Firm registration number: 101049W/E300004" |
| 15 | 684-687 | Signature — partner | Partner name rendered illegibly ("Min Rharponr" / "per Atin Bhargay,"), Partner, Membership No.: **4777** (vs. "504777" on the standalone report — see flag) |
| 16 | 691-692 | Signature — place/date | Place: Hyderabad, Date: July 29, 2026 |

**Which entities are unaudited/management-furnished (per instruction #5)**: Gee Pee Aerospace
and Defence Private Limited and Magnatar Aero Systems Private Limited — both reviewed by
their own respective independent auditors (not S.R. Batliboi), whose review reports were
furnished to S.R. Batliboi by Management (block 13); S.R. Batliboi's consolidated conclusion
relies on those other auditors' work without modification (block 14).

Flags:
- `SIGNATURE_ILLEGIBLE` (block 15 — partner name not cleanly machine-readable, same class as
  standalone report block 8).
- `UDIN_MISSING` — **no UDIN line appears anywhere in the consolidated report's signature
  block (blocks 14-16), unlike the standalone report which carries "UDIN: 2650477 1 DMUF RT
  3484" at line 537.** Enumerated as an absence, not interpreted.
- `MEMBERSHIP_NO_MISMATCH` — consolidated report shows Membership No. "4777" (line 687)
  vs. "504777" on the standalone report (line 535) for the same named partner/firm signing
  the same day. Enumerated as a raw text discrepancy; could be a text-layer truncation of the
  leading "50" or a genuine printing difference — not resolved here, flagged for A3/A4.

## 10. CONSOLIDATION ENTITY LIST (3 entities; source: consolidated note 1 lines 429-430,
    auditor report entity list lines 616-619)

| Entity | Relationship | First referenced (line) | Flag |
|---|---|---|---|
| MTAR Technologies Limited | Holding Company / filer (implicit — "the Company," parent of the Group) | 429 | ENTITY_CHANGE check: N/A, no prior-quarter ledger available |
| Gee Pee Aerospace and Defence Private Limited | Wholly owned subsidiary (per standalone note 3 / consolidated note 4, line 365/437); merger into Holding company filed with NCLT, pending | 429, 617 | ENTITY_CHANGE check: N/A |
| Magnatar Aero Systems Private Limited | Wholly owned subsidiary; merger into Holding company filed with NCLT, pending (same NCLT scheme as above) | 430, 618 | ENTITY_CHANGE check: N/A |

Note: both subsidiaries are subject to a pending NCLT merger scheme into the Holding company
(standalone note 3, consolidated note 4) — this is a prospective entity-count change, not yet
effective this quarter. Enumerated, not interpreted.

## 11. SIGNATURE BLOCKS (4 total: 2 digital, 2 wet-ink/printed auditor)

| # | Line | Signatory | Designation | Timestamp | Type |
|---|---|---|---|---|---|
| 1 | 150-169 | Priyanka Agarwal | Company Secretary and Compliance Officer | 2026.07.29 16:34:40 +05'30' | Digital (DSC), Board Outcome letter — after 3:35 p.m. meeting conclusion, no timing flag |
| 2 | 279-299 | Priyanka Agarwal | Company Secretary and Compliance Officer | 2026.07.29 16:35:00 +05'30' | Digital (DSC), Annexure A — after 3:35 p.m. meeting conclusion, no timing flag |
| 3 | 527-539 | [partner name illegible in text layer, firm-attributed to S.R. Batliboi & Associates LLP] | Partner, Membership No. 504777 | Date: July 29, 2026 (no intraday timestamp) | Printed/wet-ink, standalone review report — UDIN present (line 537) |
| 4 | 679-692 | [partner name illegible in text layer, firm-attributed to S.R. Batliboi & Associates LLP] | Partner, Membership No. 4777 (see MEMBERSHIP_NO_MISMATCH flag) | Date: July 29, 2026 (no intraday timestamp) | Printed/wet-ink, consolidated review report — **UDIN absent (see UDIN_MISSING flag)** |

---
END OF LEDGER
