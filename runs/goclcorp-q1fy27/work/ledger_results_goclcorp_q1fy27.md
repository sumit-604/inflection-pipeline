A2 COMPLETENESS LEDGER — GOCL Corporation Limited, Q1 FY27 (quarter ended June 30, 2026)
Doctype: results | Standalone AND Consolidated | Units: Rs Lakhs in filing (x0.01 = Rs Crores)
Source: /home/user/inflection-pipeline/runs/goclcorp-q1fy27/work/extract_results_goclcorp_q1fy27.txt

NUMERIC-EVIDENCE RULE APPLIED THROUGHOUT: for pages 4, 5, 6, 7, 8, 10, 11, 12 all numeric anchors below cite
the `[OCR SUPPLEMENT page N]` block line numbers, per A1's fidelity note (primary pdftotext numeric content on
these pages is corrupted). Where the OCR block itself dropped a row or a row label, this ledger cites the
corrupted primary block instead and flags `OCR_ROW_MISSING` / `ROW_LABEL_GAP` — never inferred, position-anchored
only. Pages 1, 2, 3, 9 are clean prose; cited directly.

=== A2 COUNT TEST ===
category: notes_consolidated      grep_count: 8   sweep_count: 9   match: no (see reconciliation below) -> reconciled: yes
category: notes_standalone        grep_count: 9   sweep_count: 9   match: yes
category: line_items_all_tables   grep_count: 88  sweep_count: 94  match: no (see reconciliation below) -> reconciled: yes
category: segment_rows            grep_count: 23  sweep_count: 26  match: no (see reconciliation below) -> reconciled: yes
category: agenda_items            grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras           grep_count: 12  sweep_count: 12  match: yes
category: entities                grep_count: 2   sweep_count: 2   match: yes
category: signature_blocks        grep_count: 5   sweep_count: 5   match: yes
gate_a2: pass
reconciliation_note: |
  Raw digit-anchored grep undercounts three series relative to manual sweep. Each gap is fully explained by
  a specific, individually-flagged extraction defect (not a sweep omission) and is anchored below:
  (1) notes_consolidated grep=8 vs sweep=9: Consolidated Note 1's leading numeral is dropped in BOTH the
      primary pdftotext block (line 426, no digit at all before "The above...") AND the OCR block (line 469,
      renders as "{" not "1"). Manual sweep identifies it as Note 1 by position (first paragraph after the
      "Notes:" header, immediately preceding the explicitly-numbered "2 On 1 March 2022..." at OCR line 475).
      Flag: NUMERAL_OCR_LOSS.
  (2) line_items_all_tables grep=88 vs sweep=94 (delta 6) and segment_rows grep=23 vs sweep=26 (delta 3, a
      subset of the 6): the grep pass used a decimal-value-row pattern ([0-9]+\.[0-9]{2}) as a proxy for
      "this row carries data." Six rows in the manual sweep do not match that pattern because the row itself
      is absent from, or dash-valued in, the OCR supplement:
        - Consolidated Segment Information "Total Assets" row: absent from OCR supplement page 5 (block ends
          at "d. Discontinued Operations #" liabilities, line 414); present only in corrupted primary line 371.
        - Consolidated Segment Information "Total Liabilities" row: same gap, corrupted primary line 377.
        - Consolidated Segment Information "Less: Inter segment revenue": dash ("-") in all four periods, OCR
          line 391 — no decimal digits to match, correctly a ZERO_STANDING row not a missed row.
        - Standalone P&L "Total tax expense" row: label AND row absent from OCR supplement entirely (OCR jumps
          from "b) Deferred tax Credit" at line 875 straight to "5. Profit from continuing operations" at line
          876); present only in corrupted primary line 825.
        - Standalone P&L "8. Net profit after tax (5+7)" row: label AND values absent from OCR supplement
          entirely (OCR jumps from row 7 at line 880 straight to "Other comprehensive income" at line 881);
          present only in corrupted primary line 831 (itself mislabelled "3." by the same corruption).
        - Standalone P&L "10. Total comprehensive income (8+9)" row: label AND values absent from OCR
          supplement entirely (OCR jumps from "Other comprehensive income, net of tax" at line 885 straight to
          "11. Paid up equity share capital" at line 886); present only in corrupted primary line 837.
      These three standalone-P&L omissions are IN ADDITION TO the two row-label gaps A1 already flagged
      ("Total expenses" and "3. Profit before tax (1-2)" — labels lost but values retained in OCR at lines
      871-872). Flags: OCR_ROW_MISSING (5 instances), ROW_LABEL_GAP (2 instances, A1-flagged), ZERO_STANDING
      (1 instance, correctly excluded from the numeric grep by design).
=== END COUNT TEST ===

--------------------------------------------------------------------------------
## A. BOARD OUTCOME LETTER (page 1, Reg 30/33) — lines 54-103
--------------------------------------------------------------------------------
| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| A1 | Board meeting agenda item | 76-78 | "Board of Directors...approved and taken on record the un-audited financial results (Standalone and Consolidated) for the quarter ended June 30, 2026" — single combined resolution, standalone + consolidated results | — |
| A2 | Board meeting start time | 81 | "commenced at 03:15 p.m." | — |
| A3 | Board meeting end time | 81 | "concluded at about 05:20 p.m." — total duration ~2h05m | — |
| A4 | Auditor named | 79 | "Haribhakti & Co LLP, the Auditors of the Company" | — |
| A5 | Digital signature block (Company Secretary) | 87-93 | A.Satyanarayana, Company Secretary; digitally signed; timestamp "2026.08.13 17:46:34 +05'30'" | signature 17:46:34 is AFTER meeting conclusion (~17:20) — compliant, checked, no flag |
No other agenda items found (no AR/AGM notice, no record date, no dividend, no director appointment, no auditor change, no scrutinizer, no ESOP grant, no capital-raising resolution) — manual sweep of full page 1 text confirms single-item letter.

--------------------------------------------------------------------------------
## B. CONSOLIDATED AUDITOR'S REVIEW REPORT (Haribhakti & Co LLP) — pages 2-3, lines 104-217
--------------------------------------------------------------------------------
| # | Para | Line | First ~15 words | Flags |
|---|------|------|-----------------|-------|
| B1 | Para 1 — scope of review | 117-122 | "We have reviewed the accompanying Statement of Unaudited Consolidated Financial Results of GOCL..." | — |
| B2 | Para 2 — management responsibility / Ind AS 34 basis | 124-129 | "This Statement, which is the responsibility of the Holding Company's Management..." | — |
| B3 | Para 3 — review standard SRE 2410 + SEBI Reg 33(8) circular procedures | 131-140 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| B4 | Para 4 — entities included (table) | 142-146 | "The Statement includes the results of the following entities:" | see Entity List below |
| B5 | Para 5 — conclusion (unmodified) | 148-155 | "Based on our review conducted and procedures performed...nothing has come to our attention..." | — |
| B6 | Para 6 — Emphasis of Matter | 169-181 | "We draw attention to Note 4 to the Statement, which describes that the corporate guarantees aggregating Rs. 131,610 lakhs, were not processed as Related Party Transactions..." | RPT_NONCOMPLIANCE (governance flag for A3/A4) |
| B7 | Para 7 — Other Matter | 183-202 | "We did not review the interim financial information of one subsidiary included in the Statement, whose interim financial information reflect total revenue of Rs. Nil, total net profit after tax of Rs. 829.11 lakhs..." | UNAUDITED_ENTITY — subsidiary (HGHL Holdings Limited, UK, per entity table) reviewed by other auditor, financials furnished by management, foreign-GAAP-to-Ind-AS conversion performed and reviewed by Holding Co management |
| B8 | Signature block | 205-217 | Snehal Shah, Partner, Membership No. 048539, UDIN 26048539IDHXAK5820, Place Mumbai, Date August 13, 2026 | — |

### Entity List (consolidated review report, para 4, lines 144-146)
| # | Sr.No. | Entity | Relationship | Flags |
|---|--------|--------|--------------|-------|
| E1 | 1 | GOCL Corporation Limited | Holding Company | — |
| E2 | 2 | HGHL Holdings Limited, UK | Wholly Owned subsidiary | UNAUDITED_ENTITY (per Para 7 Other Matter — reviewed by other auditor, mgmt-furnished) |
No prior-quarter ledger path was supplied to this run, so ENTITY_CHANGE (added/removed/renamed vs prior quarter) cannot be assessed — flag as `PRIOR_LEDGER_UNAVAILABLE`.

--------------------------------------------------------------------------------
## C. STATEMENT OF UNAUDITED CONSOLIDATED FINANCIAL RESULTS (page 4) — OCR lines 288-329
--------------------------------------------------------------------------------
All values Rs Lakhs, four columns: Q1FY27 (Jun 30 2026, unaudited) | Q4FY26 (Mar 31 2026, Refer Note 6) | Q1FY26 (Jun 30 2025, unaudited) | FY26 (Mar 31 2026, audited).
| # | Row | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----|------|--------|--------|--------|------|-------|
| C1 | 1. Income [header] | 288 | — | — | — | — | SECTION_HEADER |
| C2 | (a) Revenue from operations | 289 | 428.51 | 233.29 | 339.18 | 976.31 | — |
| C3 | (b) Other income (Refer note 3 and 4) | 290 | 5,884.36 | 7,626.70 | 8,310.45 | 41,581.03 | — |
| C4 | Total income | 291 | 6,312.87 | 7,859.99 | 6,845.63 | 42,557.34 | — |
| C5 | 2. Expenses [header] | 292 | — | — | — | — | SECTION_HEADER |
| C6 | a) Cost of materials consumed | 293 | 95.19 | 47.54 | 54.26 | 193.90 | — |
| C7 | b) Changes in inventories of finished goods, WIP and stock-in-trade | 294 | 32.00 | (9.03) | 3.00 | (58.84) | — |
| C8 | c) Employee benefits expense | 295 | 283.19 | 219.94 | 160.71 | 777.40 | — |
| C9 | d) Finance cost | 296 | 0.36 | 384.67 | 2,578.84 | 4,853.77 | — |
| C10 | e) Depreciation and amortisation expense | 297 | 86.39 | 70.75 | 53.10 | 237.70 | — |
| C11 | f) Other expense | 298 | 543.08 | 786.82 | 689.71 | 3,202.71 | — |
| C12 | Total expenses | 299 | 1,040.21 | 1,500.69 | 3,571.62 (OCR shows "3,571.62"; primary line 243 shows "1,500.69" for Q1FY26 col — cross-check needed) | 9,206.64 | NUMBER_DISCREPANCY — flagged for A3/A4 (see note below table) |
| C13 | 3. Profit before exceptional items and tax (1-2) | 300 | 5,272.66 | 6,359.30 | 5,078.01 | 33,350.70 | — |
| C14 | 4. Exceptional items (net) (Refer note 2) | 301 | 351.65 | (209.83) | 1,220.09 | 1,300.43 | NUMBER_DISCREPANCY (resolved loop 1): Q1FY26 primary/OCR read 4,220.09 breaks the C13+C14=C15 identity (5,078.01+4,220.09=9,298.10 != 6,298.10) and conflicts with Note 2 (1,220.09); render-adjudicated to 1,220.09 (Rs 12.20 Cr) in A1-ADDENDUM CORRECTION. A2-missed on first pass, A5-caught. |
| C15 | 5. Profit before tax (3+4) | 302 | 5,624.31 | 6,149.47 | 6,298.10 | 34,651.13 | — |
| C16 | 6. Tax expense: [header] | 303 | — | — | — | — | SECTION_HEADER |
| C17 | a) Current tax | 304 | 1,314.74 | 2,334.87 | 1,144.32 | 6,979.29 | — |
| C18 | b) Deferred tax Credit | 305 | (75.63) | (178.00) | (218.70) | (286.95) | — |
| C19 | Total tax expense | 306 | 1,239.11 | 2,156.87 | 925.62 | 6,692.34 | — |
| C20 | 7. Profit from continuing operations (5-6) | 307 | 4,385.20 | 3,992.60 | 5,372.48 | 27,958.79 | — |
| C21 | 8. Discontinued Operations (Refer note 3) [header] | 308 | — | — | — | — | SECTION_HEADER |
| C22 | a) (Loss)/Profit before tax from discontinued operations | 309 | (337.33) | 5,722.07 | 4,36,241.16 (sic, likely 1,36,241.16 — OCR digit-repeat artifact) | 1,48,051.39 | NUMBER_DISCREPANCY — flag for A3/A4 |
| C23 | b) Tax expense of discontinued operations | 310 | 8.00 | 2,200.00 | 19,359.05 | 23,815.48 | — |
| C24 | 9. (Loss)/Profit after tax from discontinued operations [(8a)-(8b)] | 311 | (345.33) | 3,522.07 | 1,16,882.05 | 1,24,235.91 | — |
| C25 | 10. Net profit after tax (7+9) | 312 | 4,039.87 | 7,514.67 | 1,22,254.53 | 1,52,194.70 | — |
| C26 | 11. Other Comprehensive Income [header] | 313 | — | — | — | — | SECTION_HEADER |
| C27 | (i) Items not reclassified to P&L [subheader] | 314 | — | — | — | — | SECTION_HEADER |
| C28 | - Remeasurement (loss)/gain on defined benefit plans | 315 | (2.13) | (29.02) | (6.51) | (8.50) | — |
| C29 | - Income tax relating to remeasurement of defined benefit plans | 316 | 0.54 | 7.30 | 1.64 | 2.14 | — |
| C30 | (ii) Items reclassified to P&L [subheader] | 317 | — | — | — | — | SECTION_HEADER |
| C31 | - Exchange differences on translation of foreign operations | 318 | (175.20) | 5,090.15 | 287.16 | 9,505.74 | row label present only in primary (line 262); OCR line 318 dropped the label, values retained — ROW_LABEL_GAP |
| C32 | Other comprehensive income, net of tax | 319 | (176.73) | 5,068.43 | 282.29 | 9,499.38 | — |
| C33 | 12. Total comprehensive income (10+11) | 320 | 3,863.08 | 12,583.10 | 1,22,536.82 | 1,61,694.08 | — |
| C34 | 13. Paid up equity share capital (Face value Rs 2 each) | 321 | 991.45 | 981.45 (sic, likely 991.45 — OCR digit-transposition, cf. col.1/3/4 all 991.45) | 991.45 | 991.45 | NUMBER_DISCREPANCY — flag for A3/A4 |
| C35 | 14. Reserves i.e. other equity | 322 | — | — | — | 3,13,302.40 | ZERO_STANDING — blank in all three interim-quarter columns, populated only in FY-end audited column (standard practice, template row) |
| C36 | 15. Earnings per share for continuing operations (Basic and Diluted, Rs.) | 323-324 | 8.85 | 8.05 | 10.84 | 56.40 | — |
| C37 | 16. Earnings per share for discontinued operations (Basic and Diluted, Rs.) | 325-326 | (0.70) | 7.10 | 235.78 | 250.61 | — |
| C38 | 17. Earnings per share for continuing and discontinued operations (Basic and Diluted, Rs.) | 327-328 | 8.15 (OCR line 328 shows "8.45"; primary line 272 shows "8.15" — digit conflict) | 15.15 | 246.62 | 307.01 | NUMBER_DISCREPANCY — flag for A3/A4; also "(not annualised)/(Annualised)" qualifier row at line 329 |
NOTE on NUMBER_DISCREPANCY rows above (C12, C22, C34, C38): these are internal conflicts between the corrupted
primary block and the OCR block (or within the OCR block itself) that A1's extraction could not resolve; A2 is
surfacing each explicitly with both readings rather than silently picking one, per "never estimate a missing
number." These are candidates for A3 forensic reconciliation against the PDF image directly.

--------------------------------------------------------------------------------
## D. SEGMENT INFORMATION — CONSOLIDATED (page 5) — OCR lines 386-414, primary lines 345-378 (Total Assets/Liabilities rows only)
--------------------------------------------------------------------------------
| # | Row | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----|------|--------|--------|--------|------|-------|
| D1 | 1. Segment income [header] | 386 | — | — | — | — | SECTION_HEADER |
| D2 | a. Electronics Manufacturing Services | 387 | 262.33 | 68.96 | 174.76 | 326.37 | — |
| D3 | b. Realty | 388 | 164.35 | 2,017.70 | 2,123.55 | 4,417.88 | — |
| D4 | c. Unallocable income | 389 | 5,886.19 | 5,773.33 | 6,351.32 | 37,813.09 | — |
| D5 | Total (segment income) | 390 | 6,312.87 | 7,859.99 | 6,649.63 | 42,557.34 | — |
| D6 | Less: Inter segment revenue | 391 | - | - | - | - | ZERO_STANDING — dash in all four periods, standing template row |
| D7 | Total Segment Revenue | 392 | 6,312.87 | 7,859.99 | 6,649.63 | 42,557.34 | — |
| D8 | Discontinued Operations # | 393 | 34.21 | 6,079.79 | 1,48,851.05 | 1,75,394.44 | — |
| D9 | Total income | 394 | 6,347.08 | 13,939.78 | 1,57,500.68 | 2,17,951.78 | — |
| D10 | 2. Segment results (Profit before tax and finance costs) [header] | 395 | — | — | — | — | SECTION_HEADER |
| D11 | a. Electronics Manufacturing Services | 396 | (110.94) | (146.16) | 3.82 | (280.62) | — |
| D12 | b. Realty | 397 | (4.58) | 1,782.62 | 1,847.59 | 3,295.17 | — |
| D13 | Total (segment results) | 398 | (115.52) | 1,636.46 | 1,851.41 | 3,014.55 | — |
| D14 | (i) Finance costs | 400 | 0.36 | 384.67 | 2,578.84 | 4,853.77 | — |
| D15 | (ii) Other Unallocable expenditure net off (un-allocable income) | 401 | (5,740.19) | value illegible in OCR ("Penna papel sh") | value illegible in OCR | (36,490.35) | OCR_ROW_MISSING — Q4FY26 and Q1FY26 cells unreadable in OCR block; not present cleanly in either block for these two columns |
| D16 | [unlabeled subtotal — Profit before tax, continuing] | 402 | 5,624.31 | 6,149.47 | 6,298.10 | 34,651.13 | ROW_LABEL_GAP — no row label in primary or OCR; anchored by position (matches Statement of Results line "5. Profit before tax" C15) and by value cross-check |
| D17 | Discontinued Operations # | 403 | (337.33) | 5,722.07 | 1,36,241.10 | 1,48,051.39 | — |
| D18 | Total profit before tax | 404 | 5,286.98 | 11,871.54 | 1,42,539.20 | 1,82,702.52 | — |
| D19 | 3. Segment assets [header] | 405 | — | — | — | — | SECTION_HEADER |
| D20 | a. Electronics Manufacturing Services | 406 | 1,583.72 | 1,817.66 | 1,955.67 | 1,817.66 | — |
| D21 | b. Realty | 407 | 12,879.46 | 14,897.62 | 16,133.81 | 14,897.62 | — |
| D22 | c. Unallocable assets | 408 | 3,37,109.48 | 3,32,942.12 | 3,48,271.57 | 3,32,942.12 | — |
| D23 | d. Discontinued Operations # | 409 | 7,838.55 | 5,854.22 | 30,879.54 | 5,854.22 | — |
| D24 | Total Assets | primary 371 (OCR-absent) | 3,59,411.21 (from corrupted primary; digits as "359411.21") | 3,55,511.62 | 3,97,240.50 | 3,56,511.62 | OCR_ROW_MISSING — row entirely absent from OCR supplement (block ends before this row); anchored to corrupted primary block only, digits not independently confirmed |
| D25 | 4. Segment liabilities [header] | 410 | — | — | — | — | SECTION_HEADER |
| D26 | a. Electronics Manufacturing Services | 411 | 530.21 | 832.50 | 944.17 | 832.50 | — |
| D27 | b. Realty | 412 | 1,746.63 | 1,719.07 | 1,834.26 | 1,719.07 | — |
| D28 | c. Unallocable liabilities | 413 | 38,877.36 | 38,566.20 | 97,607.13 | 38,566.20 | — |
| D29 | d. Discontinued Operations # | 414 | 100.00 | 100.00 | 16,639.33 | 100.00 | — |
| D30 | Total Liabilities | primary 377 (OCR-absent) | 41,254.30 (from corrupted primary; digits as "41254.30") | 41,217.77 | 1,17,024.89 | 41,217.77 | OCR_ROW_MISSING — row entirely absent from OCR supplement; anchored to corrupted primary block only, digits not independently confirmed |
| D31 | Footnote on Discontinued Operations # | line 378 (primary) / 415-422 (OCR, garbled) | "#Pertaining to Energetics Division and IDL Explosives Limited, both being classified as Discontinued Operations" | — | — | — | — |
Segment-row leaf count (D2-D30, excluding headers D1/D10/D19/D25): 26 rows. Two named reportable segments
recur across all four metrics (Electronics Manufacturing Services, Realty), reconciled through Unallocable and
Discontinued Operations lines to entity totals.

--------------------------------------------------------------------------------
## E. CONSOLIDATED NOTES (pages 6-7) — Notes 1-9
--------------------------------------------------------------------------------
| # | Note | Line (OCR) | First ~15 words | Flags |
|---|------|------------|-----------------|-------|
| E-N1 | Note 1 | primary 426-430 / OCR 469-473 (leading numeral lost in both blocks) | "The above unaudited consolidated financial results have been prepared in accordance with Indian Accounting Standards..." | NUMERAL_OCR_LOSS — identified by position, not inferred content |
| E-N2 | Note 2 | OCR 475-480 | "On 1 March 2022, HGHL Holdings Limited (wholly owned subsidiary) has entered into Addendum to share purchase agreement with ACHT..." | referenced by C14 (Exceptional items) |
| E-N3 | Note 3 | OCR 482-496 | "The Company had entered into a Memorandum of Understanding on March 27, 2024 with Squarespace Builders Private Limited, Hyderabad...for sale...Kukatpally...also covers detonator/blasting-devices operations cessation (Nov 28, 2024 board decision), Discontinued Operation / assets-held-for-sale classification (Ind AS 105), and IDL reclassification to Discontinued Operations till Nov 15, 2025" | referenced by C3 (Other income) and C21 (Discontinued Operations); multi-paragraph single numbered note |
| E-N3-sub | Discontinued Operations results sub-table (embedded in Note 3) | OCR 497-506 | "The results of discontinued operations are presented below" — 5 rows: Income (502), Expenses (503), (Loss)/Profit before tax (504), Tax expense (505), (Loss)/Profit after tax (506) | see table below |
| E-N4 | Note 4 | OCR 583-591 | "The Audit committee and Board of Directors at their respective meetings held on May 29, 2026, had ratified Corporate Guarantees extended by the Company to Hinduja National Power Corporation Limited (HNPCL) Rs. 109,610 Lakhs...and Hinduja Energy India Limited Rs. 22,000 Lakhs..." | RPT_NONCOMPLIANCE — cross-references EOM para B6 (aggregate Rs. 1,31,610 lakhs = 1,09,610 + 22,000) |
| E-N5 | Note 5 | OCR 592-597 | "The Board of Directors of the Company at their meeting held on December 15, 2025, inter alia had approved a 'Scheme of Merger by Absorption' (scheme) of Hinduja National Power Corporation Limited (HNPCL) with and into the Company..." | MATERIAL_SUBSEQUENT_EVENT — NCLT declined to accede approval on July 20, 2026 (per note text, "not acceding approval"; note text on this page later also says "July 30, 2026" at OCR line 594-596 — internal date conflict, see NUMBER_DISCREPANCY below), Company appealing to NCLAT, no scheme effect given in results |
| E-N6 | Note 6 | OCR 598-599 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited consolidated financial results for the year ended March 31, 2026 and the published unaudited...results for the period ended December 31, 2025..." | — |
| E-N7 | Note 7 | OCR 600-605 | "Pursuant to the approval of the Board of Directors at its meeting held on March 23, 2026, the Company entered into an Agreement to Sell on March 27, 2026 with the SPVs of Tata Realty and Infrastructure Limited for the sale of the Company's property...'Ecopolis'..." | advance received "Rs. 400 lakhs" per OCR line 603 vs "Rs. 100 lakhs" per primary line 559 and per Standalone Note 7 (both standalone renderings say 100) — NUMBER_DISCREPANCY, majority reading is 100, single OCR outlier flagged |
| E-N8 | Note 8 | OCR 606 | "The figures for the previous quarter/ year have been regrouped/rearranged wherever necessary to conform to the current quarter classification." | — |
| E-N9 | Note 9 | OCR 607-608 | "The above unaudited consolidated financial results are also available on the Stock Exchanges website i.e. www.bseindia.com, www.nseindia.com and the Company's website" | — |
| E-Sig | Signature block | OCR 609-619 | "By Order of the Board For GOCL Corporation Limited...Ravi Jain, Whole Time Director and Chief Financial Officer, DIN: 09184688" | Mumbai, August 13, 2026 |

Note 3 embedded Discontinued Operations sub-table (line items):
| # | Row | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----|------|--------|--------|--------|------|-------|
| E-D1 | 1. Income (Refer note 3) | 502 | 34.21 | 6,079.79 | 1,48,851.05 | 1,75,394.44 | — |
| E-D2 | 2. Expenses | 503 | 371.54 | 357.72 | 12,609.95 | 27,343.05 | — |
| E-D3 | 3. (Loss)/Profit before tax (1-2) | 504 | (337.33) | 5,722.07 | 1,36,241.10 | 1,48,051.39 | — |
| E-D4 | 4. Tax expense | 505 | 8.00 | 2,200.00 | 19,359.05 | 23,815.48 | — |
| E-D5 | 5. (Loss)/Profit after tax (3-4) | 506 | (345.33) | 3,522.07 | 1,16,882.05 | 1,24,235.91 | — |

--------------------------------------------------------------------------------
## F. STANDALONE AUDITOR'S REVIEW REPORT (Haribhakti & Co LLP) — pages 8-9, lines 624-790
--------------------------------------------------------------------------------
| # | Para | Line | First ~15 words | Flags |
|---|------|------|-----------------|-------|
| F1 | Para 1 — scope of review | 716-720 | "We have reviewed the accompanying Statement of Unaudited Standalone Financial Results of GOCL Corporation Limited..." | — |
| F2 | Para 2 — management responsibility / Ind AS 34 basis | 722-728 | "This Statement, which is the responsibility of the Company's Management and approved by the Company's Board of Directors..." | — |
| F3 | Para 3 — review standard SRE 2410 | 730-737 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | — |
| F4 | Para 4 — conclusion (unmodified) | 739-745 | "Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing has come to our attention..." | — |
| F5 | Para 5 — Emphasis of Matter | 761-773 | "We draw attention to Note 5 to the Statement, which describes that the corporate guarantees aggregating Rs. 131,610 lakhs, were not processed as Related Party Transactions..." | RPT_NONCOMPLIANCE — same underlying matter as consolidated EOM (B6) / Note 5 standalone; no standalone Other Matter paragraph (single-entity statement, no subsidiary to carve out) |
| F6 | Signature block | 785-790 | Snehal Shah, Partner, Membership No. 048539, UDIN 26048539VYZQPQ5315 (distinct from consolidated report's UDIN 26048539IDHXAK5820 — correct, each report requires its own UDIN), Place Mumbai, Date August 13, 2026 | — |
No entity table in standalone report (single-entity statement) — entities category applies to consolidated report only.

--------------------------------------------------------------------------------
## G. STATEMENT OF UNAUDITED STANDALONE FINANCIAL RESULTS (page 10) — OCR lines 860-893, primary lines 810-845 (for OCR-missing rows)
--------------------------------------------------------------------------------
Four columns: Q1FY27 (Jun 30 2026, unaudited) | Q4FY26 (Mar 31 2026, audited, Refer Note 3) | Q1FY26 (Jun 30 2025, unaudited) | FY26 (Mar 31 2026 — column header literally reads "March 31, 2025 (Audited)" in primary line 805 vs "March 31, 2026" in OCR line 856; column-header date conflict flagged below).
| # | Row | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----|------|--------|--------|--------|------|-------|
| G0 | Column header date conflict | primary 805 vs OCR 856 | primary reads "March 31, 2025 (Audited)" for last column; OCR reads "March 31, 2026" | — | — | — | NUMBER_DISCREPANCY — flag for A3/A4; FY26 values in this table (28,376.04 total income primary / 28,375.04 OCR — also conflicting, see G1) are internally consistent with a FY26 year-end, so the "2025" in primary is treated as the likely OCR/pdftotext misread, not the OCR block's "2026" |
| G1 | 1. Income [header] | 860 | — | — | — | — | SECTION_HEADER |
| G2 | a) Revenue from operations | 861 | 428.51 | 233.29 | 339.18 | 976.31 | — |
| G3 | b) Other income (Refer note 5 and 8) | 862 | 5,254.59 | 7,026.99 | 4,745.76 | 27,398.73 | — |
| G4 | Total income | 863 | 5,683.10 | 7,260.28 | 5,084.94 | 28,375.04 (OCR) vs 28,376.04 (primary line 812) | NUMBER_DISCREPANCY — flag for A3/A4 |
| G5 | 2. Expenses [header] | 864 | — | — | — | — | SECTION_HEADER |
| G6 | a) Cost of materials consumed | 865 | 95.19 | 47.54 | 54.26 | 193.90 | — |
| G7 | b) Changes in inventories of finished goods, WIP and stock-in-trade | 866 | 32.00 | (9.03) | 35.00 | (58.84) | — |
| G8 | c) Employee benefits expense | 867 | 283.19 | 219.94 | 160.71 | 777.40 | — |
| G9 | d) Finance cost | 868 | 0.36 | 0.73 | 27.29 | 31.71 | — |
| G10 | e) Depreciation and amortisation expense | 869 | 86.39 | 70.75 | 53.10 | 237.79 (OCR) vs 231.70 (primary line 818) | NUMBER_DISCREPANCY — flag for A3/A4 |
| G11 | f) Other expense | 870 | 535.50 | 710.82 | 621.81 | 2,796.98 | — |
| G12 | Total expenses | ROW_LABEL_GAP: label absent OCR line 871 (values "952.17 / 3,978.85" only); full row incl. label present primary line 820 | 1,032.63 (primary only) | 1,040.75 (primary only) | 952.17 | 3,978.85 | ROW_LABEL_GAP (A1-flagged) — anchored to primary for label and Q1FY27/Q4FY26 columns since OCR line 871 only carries the last two columns |
| G13 | 3. Profit before tax (1-2) | ROW_LABEL_GAP: label absent OCR line 872; full row incl. label present primary line 821 | 4,650.47 (primary only) | 6,219.53 | 4,132.77 | 24,396.19 | ROW_LABEL_GAP (A1-flagged) — anchored to primary for label and Q1FY27 column |
| G14 | 4. Tax expense: [header] | 873 | — | — | — | — | SECTION_HEADER |
| G15 | a) Current tax | 874 | 1,170.00 | 2,300.00 | 1,044.01 | 6,712.33 | — |
| G16 | b) Deferred tax Credit | 875 | (75.63) | (178.00) | (218.70) | (286.95) | — |
| G17 | Total tax expense | OCR_ROW_MISSING — row entirely absent from OCR (jumps from G16 straight to G18); anchored primary line 825 | 1,094.37 | 2,122.00 | 825.31 | 6,425.38 | OCR_ROW_MISSING — anchored to corrupted primary block only |
| G18 | 5. Profit from continuing operations (3-4) | 876 (OCR columns 3-4 dropped, values 5,372.46/17,870.81 missing from OCR) | 3,556.10 | 4,097.53 | 3,307.46 (primary 826 only) | 17,870.81 (primary 826 only) | OCR_ROW_MISSING (partial — OCR retains first two columns only) |
| G19 | 6. Discontinued Operations (Refer note 8) [header] | 877 | — | — | — | — | SECTION_HEADER |
| G20 | a) (Loss)/Profit before tax from discontinued operations | 878 | (337.33) | 5,722.07 | 1,36,748.16 | 1,49,737.05 | — |
| G21 | b) Tax expense of discontinued operations | 879 (mislabelled "c)" in OCR, should be "b)") | 8.00 | 2,200.00 | 19,355.99 | 23,123.32 | OCR_LABEL_ERROR — OCR renders "c)" for what is row (b) per primary line 829 "o) Tax 2cpanse..." (also corrupted, but position confirms it is item b) |
| G22 | 7. (Loss)/Profit after tax from discontinued operations [6(a)-6(b)] | 880 (OCR retains only first column value, "(345.33"; remaining 3 columns cut off) | (345.33) | 3,522.07 (primary 830 only) | 1,17,392.7 (primary 830 only, digit-truncated) | 1,26,613.73 (primary 830 only) | OCR_ROW_MISSING (partial) |
| G23 | 8. Net profit after tax (5+7) | OCR_ROW_MISSING — entire row (label + all 4 values) absent from OCR supplement; anchored primary line 831 (there mislabelled "3." by the same corruption, should be "8." per statement structure) | 3,210.77 | 7,619.60 | 1,20,699.63 | 1,44,584.54 | OCR_ROW_MISSING — HIGH PRIORITY, sole numeric anchor is the corrupted primary block; digits not independently confirmed by OCR for any column |
| G24 | 9. Other comprehensive income [header] | 881 | — | — | — | — | SECTION_HEADER |
| G25 | Items not reclassified to P&L [subheader] | 882 | — | — | — | — | SECTION_HEADER |
| G26 | - Remeasurement (loss)/gain on defined benefit plans | 883 | (2.13) | (29.02) | (0.43) (primary 834 only, OCR line 883 truncated before this column) | (8.50) (primary 834 only) | OCR_ROW_MISSING (partial) |
| G27 | - Income tax relating to remeasurement of defined benefit plans | 884 | 0.54 | 7.30 | 0.03 | 2.14 | — |
| G28 | Other comprehensive income, net of tax | 885 | (1.59) | (21.72) | 0.10 | (6.36) | — |
| G29 | 10. Total comprehensive income (8+9) | OCR_ROW_MISSING — entire row (label + all 4 values) absent from OCR supplement; anchored primary line 837 | 3,209.18 | 7,597.88 | 1,20,699.53 | 1,44,578.18 | OCR_ROW_MISSING — HIGH PRIORITY, sole numeric anchor is the corrupted primary block |
| G30 | 11. Paid up equity share capital (face value Rs 2 each) | 886 | 991.45 | 991.45 | 991.45 | 991.45 | — |
| G31 | 12. Reserves i.e. other equity | 887 | — | — | — | 2,16,389.43 | ZERO_STANDING — blank in all three interim-quarter columns, populated only in FY-end column (same template pattern as consolidated C35) |
| G32 | 13. Earnings per share for continuing operations (Basic and Diluted, Rs.) | 888-889 | 7.17 | 8.27 | 6.67 | 36.25 | — |
| G33 | 14. Earnings per share for discontinued operations (Basic and Diluted, Rs.) | 890-891 | (0.70) | 7.10 | 236.81 | 255.41 | — |
| G34 | 15. Earnings per share for continuing and discontinued operations (Basic and Diluted, Rs.) | 892-893 | 6.47 | 15.37 | 243.48 | 291.66 (OCR); primary line 845 shows "29168" (=291.68) — NUMBER_DISCREPANCY | — | NUMBER_DISCREPANCY — flag for A3/A4 |

--------------------------------------------------------------------------------
## H. STANDALONE NOTES (pages 11-12) — Notes 1-9
--------------------------------------------------------------------------------
| # | Note | Line (OCR) | First ~15 words | Flags |
|---|------|------------|-----------------|-------|
| H-N1 | Note 1 | OCR 961-965 (also present cleanly in primary 903-906) | "The above unaudited standalone financial results have been prepared in accordance with Indian Accounting Standards..." | — |
| H-N2 | Note 2 | OCR 967 | "As per Ind AS 108 'Operating segments', the Company has disclosed the segment information only as part of the unaudited consolidated financial results." | confirms segment table (Section D) is consolidated-only, standalone has no segment disclosure — expected, not a gap |
| H-N3 | Note 3 | OCR 969-970 | "The figures for the Quarter ended March 31, 2026 are the balancing figures between the audited standalone financial results for the year ended March 31, 2026 and the published..." | — |
| H-N4 | Note 4 | OCR 972 | "The figures for the previous quarter/ year have been regrouped/rearranged wherever necessary to conform to the current quarter classification." | — |
| H-N5 | Note 5 | OCR 974-982 | "The Audit committee and Board of Directors at their respective meetings held on May 29, 2026, had ratified Corporate Guarantees extended by the Company to Hinduja National Power Corporation Limited (HNPCL) Rs. 109,610 Lakhs..." | RPT_NONCOMPLIANCE — same matter as Consolidated Note 4 / EOM paras B6 and F5 |
| H-N6 | Note 6 | OCR 984-988 | "The Board of Directors of the Company at their meeting held on December 15, 2025, inter alia had approved a 'Scheme of Merger by Absorption' ('scheme') of Hinduja National Power Corporation Limited..." | MATERIAL_SUBSEQUENT_EVENT — same NCLT/NCLAT matter as Consolidated Note 5 |
| H-N7 | Note 7 | OCR 990-995 | "Pursuant to the approval of the Board of Directors at their meeting held on March 23, 2026, the Company entered into an Agreement to Sell on March 27, 2026 with the SPVs of Tata Realty and Infrastructure Limited...Ecopolis..." | advance received "Rs. 100 lakhs" (consistent with consolidated primary reading; consolidated OCR's "400" at line 603 is the outlier) |
| H-N8 | Note 8 | OCR 1053-1058 (page 12) | "The Company had entered into a Memorandum of Understanding on March 27, 2024 with Squarespace Builders Private Limited, Hyderabad for sale of the Company's Scheduled Property...also covers detonator/blasting-devices cessation and Ind AS 105 classification" | referenced by G3 (Other income) and G19 (Discontinued Operations); multi-paragraph single numbered note, mirrors Consolidated Note 3 minus the IDL/HNPCL-specific consolidation language |
| H-N8-sub | Discontinued Operations results sub-table (embedded in Note 8) | OCR 1069-1073 | "The results of discontinued operations are presented below" — 5 rows | see table below |
| H-N9 | Note 9 | OCR 1074-1075 | "The above unaudited standalone financials results are also available on the Stock Exchanges website i.e. www.bseindia.com, www.nseindia.com and the Company's website" | — |
| H-Sig | Signature block | OCR 1076-1082 | "For GOCL Corporation Limited...Ravi Jain, Whole Time Director and Chief Financial Officer, DIN: 09184688" | Mumbai, August 13, 2026 |

Note 8 embedded Discontinued Operations sub-table (line items):
| # | Row | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----|------|--------|--------|--------|------|-------|
| H-D1 | 1. Income (Refer note 8) | 1069 | 34.21 | 6,079.79 | 1,37,325.35 | 1,51,081.22 | — |
| H-D2 | 2. Expenses | 1070 | 371.54 | 357.72 | 877.19 | 1,344.17 | — |
| H-D3 | 3. (Loss)/Profit before tax (1-2) | 1071 (mislabelled "5." in OCR, should be "3.") | (337.33) | 5,722.07 | 1,36,748.16 | 1,49,737.05 | OCR_LABEL_ERROR |
| H-D4 | 4. Tax expense | 1072 | 8.00 | 2,200.00 | 19,355.99 | 23,123.32 | — |
| H-D5 | 5. (Loss)/Profit after tax (3-4) | 1073 | (345.33) | 3,522.07 | 1,17,392.17 | 1,26,613.73 | — |
Note: standalone discontinued-operations Income figures differ from consolidated discontinued-operations Income
figures for Q1FY26/FY26 columns (H-D1: 1,37,325.35/1,51,081.22 vs E-D1: 1,48,851.05/1,75,394.44) — expected,
since standalone Discontinued Operations (detonators business only) is a subset of consolidated Discontinued
Operations (detonators + Energetics Division + IDL Explosives Limited per footnote D31); not a discrepancy.

--------------------------------------------------------------------------------
## SUMMARY FLAG REGISTER (all flags raised, cross-referenced to ledger IDs)
--------------------------------------------------------------------------------
- ZERO_STANDING (3): D6, C35, G31
- SECTION_HEADER (structural, not counted in leaf line_items): C1,C5,C16,C21,C26,C27,C30,D1,D10,D19,D25,G1,G5,G14,G19,G24,G25 (17 rows)
- ROW_LABEL_GAP (3): C31, D16, G12, G13 (A1-flagged: G12, G13; A2-additional: C31, D16) — 4 instances total
- OCR_ROW_MISSING (7): D15, D24, D30, G17, G18(partial), G22(partial), G23, G26(partial), G29 — 9 instances total (G23 and G29 are full-row losses, highest priority for A3/A4)
- NUMERAL_OCR_LOSS (1): E-N1
- OCR_LABEL_ERROR (2): G21, H-D3
- NUMBER_DISCREPANCY (7): C12, C22, C34, C38, E-N7, G0, G4, G10, G34 (9 instances total — internal conflicts between primary/OCR or within OCR itself, none silently resolved)
- RPT_NONCOMPLIANCE (governance, non-mechanical, surfaced not evaluated): B6, E-N4, F5, H-N5
- UNAUDITED_ENTITY: B7, E2
- MATERIAL_SUBSEQUENT_EVENT: E-N5, H-N6 (HNPCL merger scheme — NCLT declined to accede approval)
- PRIOR_LEDGER_UNAVAILABLE: entity list (Section B) — no prior-quarter ledger supplied to this run, ENTITY_CHANGE not assessable

--------------------------------------------------------------------------------
## CATEGORY COUNTS (for YAML)
--------------------------------------------------------------------------------
notes: 18 (9 consolidated + 9 standalone)
line_items: 94 leaf value-bearing rows (30 consolidated P&L + 26 consolidated segment + 5 consolidated discontinued-ops sub-table + 28 standalone P&L + 5 standalone discontinued-ops sub-table); +17 SECTION_HEADER structural rows enumerated separately, not double-counted
zero_standing: 3
agenda_items: 1
auditor_paras: 12 (7 consolidated + 5 standalone)
entities: 2
turns/questions/mgmt_numbers/slides/slide_numbers: not applicable (results filing, no transcript/deck)

```yaml
stage: A2-enumerator
company: "goclcorp"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/goclcorp-q1fy27/work/ledger_results_goclcorp_q1fy27.md"
counts:
  notes: 18
  line_items: 94
  zero_standing: 3
  agenda_items: 1
  auditor_paras: 12
  entities: 2
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, SECTION_HEADER, ROW_LABEL_GAP, OCR_ROW_MISSING, NUMERAL_OCR_LOSS, OCR_LABEL_ERROR, NUMBER_DISCREPANCY, RPT_NONCOMPLIANCE, UNAUDITED_ENTITY, MATERIAL_SUBSEQUENT_EVENT, PRIOR_LEDGER_UNAVAILABLE]
gate_a2: pass
mismatch_note: "Raw grep undercounted notes_consolidated (8 vs 9) and line_items_all_tables (88 vs 94) relative to manual sweep. Both gaps are fully explained and reconciled: consolidated Note 1's leading numeral is lost in both primary and OCR blocks alike (identified by position, flag NUMERAL_OCR_LOSS); the 6-row line-item gap is explained by 2 OCR-missing rows in Consolidated Segment Info (Total Assets, Total Liabilities), 3 OCR-missing rows in Standalone P&L (Total tax expense, Net profit after tax, Total comprehensive income), and 1 correctly-excluded dash-valued ZERO_STANDING row (Less: Inter segment revenue). See full reconciliation_note in the COUNT TEST header of the ledger file. No disclosure unit was dropped; every gap row is individually anchored and flagged in the ledger body."
```

--------------------------------------------------------------------------------
## A5 ADVISORY FIDELITY NOTES (loop-1, non-blocking; zero derived-metric impact)
--------------------------------------------------------------------------------
Two additional cmap-corrupt display cells surfaced by A5 re-audit, resolvable from the extract, immaterial (A4 anchored all totals to render-verified values so nothing downstream changed):
1. Consolidated Q1FY26 "Changes in inventories of finished goods, WIP, stock-in-trade" (C7): reads 0.03 Cr but must be 0.35 Cr (35.00 lakh) — render-adjudicated Total expenses 3,571.62 lakh foots only with 35.00 lakh (delta exactly 32.00), and the standalone twin (G7) is 35.00. Review Step 1.1 cell corrected to 0.35.
2. Consolidated Segment "Total income" Q1FY26 (D5/D7): reads 6,649.63 lakh but its own components and the P&L both give 8,649.63 (8->6 misread). A4 derives nothing from it; no correction needed to any analytical line.
