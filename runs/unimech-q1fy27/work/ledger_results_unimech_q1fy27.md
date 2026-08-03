# A2 ENUMERATION LEDGER — UNIMECH Q1 FY27 (Results, Reg 33 filing)
Source: `extract_results_unimech_q1fy27.txt` (655 lines, 11 pages, no OCR pages, 100% page coverage)
Prior-quarter ledger: not provided (ENTITY_CHANGE assessed from in-document "w.e.f." qualifiers and note text only)

```
=== A2 COUNT TEST ===
category: notes            grep_count: 21   sweep_count: 21   match: yes
category: line_items       grep_count: 75   sweep_count: 75   match: yes
category: zero_standing    grep_count: 3    sweep_count: 3    match: yes
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 11   sweep_count: 11   match: yes
category: entities         grep_count: 6    sweep_count: 6    match: yes
category: annexure_items   grep_count: 3    sweep_count: 3    match: yes
category: signature_blocks grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation note on `notes` category (methodology, shows why grep needed refinement)
First-pass grep `^\s*[0-9]+\.\s` / `^\s*[0-9]+\s` restricted to the two "Explanatory notes" sections
returned 9 explicit-numbered hits in the standalone block (notes 2-10; note 1 has no leading numeral
in the extracted text) and 7 explicit-numbered hits in the consolidated block (notes 4, 6-11; notes
1, 2, 3, 5 have no leading numeral in the extracted text) = 16 total. Manual line-by-line sweep of
both "Explanatory notes to..." sections found 21 discrete notes (10 standalone + 11 consolidated),
i.e. 5 notes whose leading numeral did not survive text extraction (standalone note 1; consolidated
notes 1, 2, 3, 5 — the last cross-confirmed against the "Refer note 5" pointer in the consolidated
table's column header at line 485, matching table header note 4 at line 205/line 279 in standalone).
This is flagged `NOTE_NUMBER_NOT_EXTRACTED` below rather than silently absorbed. Refined grep
(numeric-prefix regex OR paragraph boundary immediately after the "Explanatory notes to..." header /
before the next explicit numeral, cross-checked against the "Refer note N" pointers) reproduces 21.
Re-swept once; final counts match. GATE A2 = pass for this category.

---

## 1. STANDALONE — EXPLANATORY NOTES (10 notes)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 268 | "The standalone unaudited statement of financial results of Unimech Aerospace and Manufacturing Limited..." (basis of preparation) | NOTE_NUMBER_NOT_EXTRACTED |
| 2 | 273 | "The Company's operating segments are established in a manner consistent with the products..." (single segment, Ind AS 108) | |
| 3 | 277 | "The standalone unaudited financial results are available on the website of the Company..." | |
| 4 | 279 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited..." | |
| 5 | 281 | "The Company had received net proceeds of INR 23,091.10 lakhs from the fresh issue of equity shares..." (IPO proceeds utilisation) | |
| 6 | 284 | "During the quarter ended June 30, 2026, Uniflux Renewable Energy Private Limited was incorporated on April 27, 2026..." | ENTITY_CHANGE |
| 7 | 287 | "During the quarter ended June 30, 2026, the Company entered into definitive agreements to acquire Hobel Bellows Private Limited and Hobel Bellows Co..." (Rs 45,000 lakh total investment) | ENTITY_CHANGE |
| 8 | 293 | "The Company Secretary and Compliance Officer of the Company, Mr. Akash Shetty, tendered his resignation with effect from March 03, 2026..." | |
| 9 | 296 | "The Board of Directors, at its meeting held on August 03, 2026, approved the proposal to raise funds aggregating up to INR 75,000 lakhs..." (QIP) | |
| 10 | 300 | "The Board of Directors, at its meeting held on August 03, 2026, approved the further investment in Dheya Engineering Technologies..." (Rs 500 lakh, Associate) | |

## 2. CONSOLIDATED — EXPLANATORY NOTES (11 notes)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 558 | "The consolidated unaudited statement of financial results of Unimech Aerospace and Manufacturing Limited ('the Holding Company')..." (basis of preparation) | NOTE_NUMBER_NOT_EXTRACTED |
| 2 | 565 | "This statement includes the results of the Holding Company and the following entities" — entity table (see section 8) | NOTE_NUMBER_NOT_EXTRACTED, ENTITY_CHANGE |
| 3 | 575 | "The Group's operating segments are established in a manner consistent with the products of the Group..." (single segment, Ind AS 108) | NOTE_NUMBER_NOT_EXTRACTED |
| 4 | 580 | "The consolidated unaudited financial results are available on the website of the Company..." | |
| 5 | 582 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited..." | NOTE_NUMBER_NOT_EXTRACTED |
| 6 | 584 | "The Company had received net proceeds of INR 23,091.10 lakhs from the fresh issue of equity shares..." (IPO proceeds utilisation) | |
| 7 | 587 | "During the quarter ended June 30, 2026, Uniflux Renewable Energy Private Limited was incorporated on April 27, 2026..." | ENTITY_CHANGE |
| 8 | 590 | "During the quarter ended June 30, 2026, the Group entered into definitive agreements to acquire Hobel Bellows Private Limited and Hobel Bellows Co..." (Rs 45,000 lakh total investment) | ENTITY_CHANGE |
| 9 | 596 | "The Company Secretary and Compliance Officer of the Company, Mr. Akash Shetty, tendered his resignation with effect from March 03, 2026..." | |
| 10 | 598 | "The Board of Directors, at its meeting held on August 03, 2026, approved the proposal to raise funds aggregating up to INR 75,000 lakhs..." (QIP) | |
| 11 | 603 | "The Board of Directors, at its meeting held on August 03, 2026, approved the further investment in Dheya Engineering Technologies..." (Rs 500 lakh, Associate) | |

---

## 3. STANDALONE FINANCIAL RESULTS TABLE — line items (32 rows: 25 value rows + 7 header rows)
Columns: Q ended 30-Jun-26 (Unaudited) | Q ended 31-Mar-26 (Audited, refer note 4) | Q ended 30-Jun-25 (Unaudited) | Year ended 31-Mar-26 (Audited)

| Line | Row label | Type | Flags |
|------|-----------|------|-------|
| 206 | 1 Income | header | |
| 207 | (a) Revenue from operations — 459.06 / 756.97 / 1,170.55 / 4,391.59 | value | |
| 208 | (b) Other income — 978.32 / 924.66 / 1,116.51 / 4,087.13 | value | |
| 209 | Total income — 1,437.38 / 1,681.63 / 2,287.06 / 8,478.72 | value | |
| 212 | 2 Expenses | header | |
| 213 | (a) Cost of materials consumed — 108.08 / 154.65 / 230.10 / 731.70 | value | |
| 214 | (b) Changes in inventories of finished goods and WIP — (9.50) / 81.66 / (0.23) / 630.59 | value | |
| 216 | (c) Subcontracting charges — 101.83 / 135.85 / 205.07 / 503.99 | value | |
| 217 | (d) Employee benefit expenses — 377.71 / 432.62 / 245.47 / 1,381.50 | value | |
| 218 | (e) Finance costs — 40.96 / 36.98 / 33.79 / 150.69 | value | |
| 219 | (f) Depreciation and amortization expenses — 237.18 / 261.20 / 192.12 / 922.89 | value | |
| 220 | (g) Other expenses — 281.09 / 374.93 / 200.16 / 1,128.36 | value | |
| 221 | Total expenses — 1,137.35 / 1,477.89 / 1,106.48 / 5,449.72 | value | |
| 224 | 3 Profit before tax for the period/year — 300.03 / 203.74 / 1,180.58 / 3,029.00 | value | |
| 226 | 4 Income tax (credit)/expense | header | |
| 227 | a Current tax | header (sub) | |
| 228 | Tax expense for the period/year — 373.41 / 115.46 / 242.81 / 843.90 | value | |
| 229 | Adjustments for current tax of prior period — blank / (4.49) / "-" / 43.42 | value | PARTIAL_BLANK (nil in 2 of 4 periods; current-quarter cell blank) |
| 230 | b Deferred tax (credit)/charge — (293.53) / (97.04) / 51.57 / (79.98) | value | |
| 231 | Total income tax expense — 79.88 / 13.93 / 294.38 / 807.34 | value | |
| 233 | 5 Profit after tax for the period/year — 220.15 / 189.81 / 886.20 / 2,221.66 | value | |
| 235 | 6 Other comprehensive income/(loss) | header | |
| 236-237 | Items that will not be reclassified subsequently to profit or loss | header (sub) | |
| 238 | a Remeasurement gain/(loss) on defined benefit plan — 3.57 / (1.24) / (5.43) / 6.05 | value | |
| 239 | b Income tax effect on above item — (0.90) / 0.31 / 1.37 / (1.52) | value | |
| 241 | Total other comprehensive income/(loss) for the period/year — 2.67 / (0.93) / (4.06) / 4.53 | value | |
| 245 | 7 Total comprehensive income for the period/year — 222.82 / 188.88 / 882.14 / 2,226.19 | value | |
| 248 | 8 Paid-up equity share capital (FV Rs 5) — 2,542.84 / 2,542.84 / 2,542.84 / 2,542.84 | value | |
| 252 | 9 Other equity — blank / blank / blank / 52,565.56 | value | ANNUAL_ONLY_LINE (nil in all 3 quarter columns; SEBI-format convention, populated only at FY-end) |
| 254-255 | 10 Earnings per share (FV Rs 5, not annualised except FY) | header | |
| 256 | (a) Basic (INR) — 0.43 / 0.37 / 1.74 / 4.37 | value | |
| 257 | (b) Diluted (INR) — 0.43 / 0.37 / 1.74 / 4.36 | value | |

## 4. CONSOLIDATED FINANCIAL RESULTS TABLE — line items (43 rows: 33 value rows + 10 header rows)
Columns: Q ended 30-Jun-26 (Unaudited) | Q ended 31-Mar-26 (Audited, refer note 5) | Q ended 30-Jun-25 (Unaudited) | Year ended 31-Mar-26 (Audited)

| Line | Row label | Type | Flags |
|------|-----------|------|-------|
| 486 | 1 Income | header | |
| 487 | (a) Revenue from operations — 10,762.04 / 8,180.21 / 6,298.85 / 24,049.04 | value | |
| 488 | (b) Other income — 732.85 / 1,476.14 / 1,143.81 / 4,696.93 | value | |
| 489 | Total income — 11,494.89 / 9,656.35 / 7,442.66 / 28,745.97 | value | |
| 491 | 2 Expenses | header | |
| 492 | (a) Cost of materials consumed — 2,694.74 / 1,683.48 / 1,509.48 / 6,117.60 | value | |
| 493 | (b) Changes in inventories of finished goods and WIP — 756.98 / 120.05 / 189.70 / (237.45) | value | |
| 495 | (c) Subcontracting charges — 351.15 / 372.42 / 433.74 / 1,406.14 | value | |
| 496 | (d) Employee benefits expense — 1,624.65 / 1,558.03 / 1,266.78 / 5,342.37 | value | |
| 497 | (e) Finance costs — 193.76 / 1,125.23 / 114.61 / 1,538.81 | value | |
| 498 | (f) Depreciation and amortization expenses — 795.70 / 715.71 / 588.51 / 2,626.11 | value | |
| 499 | (g) Other expenses — 1,409.07 / 922.49 / 919.84 / 3,908.86 | value | |
| 500 | Total expenses — 7,826.05 / 6,497.41 / 5,022.66 / 20,702.44 | value | |
| 502 | 3 Profit before tax for the period/year — 3,668.84 / 3,158.94 / 2,420.00 / 8,043.53 | value | |
| 504 | 4 Income tax (credit)/expense | header | |
| 505 | a Current tax | header (sub) | |
| 506 | Tax expense for the period/year — 1,168.66 / 633.56 / 452.02 / 1,718.82 | value | |
| 507 | Adjustments for current tax of prior period — blank / (4.49) / blank / 35.52 | value | PARTIAL_BLANK (nil in 2 of 4 periods) |
| 508 | b Deferred tax (credit)/charge — (299.98) / (97.04) / 51.57 / (79.98) | value | |
| 509 | Total income tax expense — 868.68 / 532.03 / 503.59 / 1,674.36 | value | |
| 511 | 5 Profit before share of loss of associate entity for the period/year — 2,800.16 / 2,626.91 / 1,916.41 / 6,369.17 | value | |
| 513 | 6 Share of loss from associate entity — (13.80) / (16.72) / (3.98) / (40.87) | value | |
| 514 | 7 Profit after tax for the period/year — 2,786.36 / 2,610.19 / 1,912.43 / 6,328.30 | value | |
| 516 | 8 Other comprehensive loss | header | |
| 517 | Items that will not be reclassified subsequently to profit or loss | header (sub) | |
| 520 | a Remeasurement gain/(loss) on defined benefit plan — (8.36) / (37.10) / (24.47) / (41.60) | value | |
| 521 | b Income tax effect on above item — (0.90) / 0.31 / 1.37 / (1.52) | value | |
| 522 | c Share of other comprehensive loss from associate entity — blank / 0.37 / blank / (0.28) | value | PARTIAL_BLANK (nil in 2 of 4 periods) |
| 524 | Total other comprehensive loss for the period/year — (9.26) / (36.42) / (23.10) / (43.40) | value | |
| 526 | 9 Total comprehensive income for the period/year — 2,777.10 / 2,573.77 / 1,889.33 / 6,284.90 | value | |
| 528 | 10 Net profit attributable to: | header | |
| 529 | Equity shareholders of the Company — 2,786.41 / 2,610.19 / 1,912.43 / 6,328.30 | value | |
| 530 | Non-controlling interest — (0.05) / "-" / "-" / "-" | value | PARTIAL_BLANK; nil in 3 of 4 periods — NCI arose this quarter only, ties to Uniflux Renewable Energy subsidiary formation and Hobel Bellows acquisitions (see ENTITY_CHANGE, notes 6/7 consolidated) |
| 531 | 11 Other comprehensive loss for the period/year attributable to: | header | NUMBERING_ANOMALY (note/line index "11" reused — see line 534) |
| 532 | Equity shareholders of the Company — (9.26) / (36.42) / (23.10) / (43.40) | value | |
| 534 | 11 Total comprehensive income attributable to: | header | NUMBERING_ANOMALY (duplicate index "11"; should logically be "12" — source document numbering defect, not an extraction artifact, since both instances show explicit "11") |
| 535 | Equity shareholders of the Company — 2,777.15 / 2,573.77 / 1,889.33 / 6,284.90 | value | |
| 536 | Non-controlling interest — (0.05) / [no further columns printed] | value | PARTIAL_BLANK; only current-quarter cell populated |
| 538 | 12 Paid-up equity share capital (FV Rs 5) — 2,542.84 / 2,542.84 / 2,542.84 / 2,542.84 | value | |
| 542 | 13 Other equity — blank / blank / blank / 71,196.17 | value | ANNUAL_ONLY_LINE (nil in all 3 quarter columns) |
| 544 | 14 Earnings per share (FV Rs 5, not annualised except FY) | header | |
| 546 | (a) Basic (INR) — 5.48 / 5.13 / 3.76 / 12.44 | value | |
| 547 | (b) Diluted (INR) — 5.47 / 5.12 / 3.76 / 12.42 | value | |

---

## 5. ZERO_STANDING items (3) — auditor report explicit "Nil" disclosure
Consolidated auditor report, paragraph 7 (lines 439-445): the results of a consolidated subsidiary
not subject to review are stated as Nil on all three headline metrics for the quarter — this is the
company's own unaudited/management-furnished subsidiary line, structurally identical to the
SOUTHWEST canonical example (a template line standing at zero because the entity, freshly added
to consolidation, has not yet traded).

| # | Line | Metric | Value | Flags |
|---|------|--------|-------|-------|
| 1 | 440 | Total revenue (unreviewed subsidiary) | Rs. Nil | ZERO_STANDING |
| 2 | 440 | Total net profit/(loss) after tax (unreviewed subsidiary) | Rs. Nil | ZERO_STANDING |
| 3 | 441 | Total comprehensive income/(loss) (unreviewed subsidiary) | Rs. Nil | ZERO_STANDING |

(Entity is management-identified only as "subsidiary...not subject to review" — cross-reference to
entity list in section 8 strongly implicates Uniflux Renewable Energy Private Limited, incorporated
April 27, 2026 and therefore pre-revenue at quarter-end, but the auditor report itself does not name
it — that inference is left to A3/A4, not asserted here.)

---

## 6. BOARD OUTCOME LETTER — agenda items (4)

| # | Line | Item | Details | Flags |
|---|------|------|---------|-------|
| 1 | 36 | Un-audited Financial Results | Approved standalone + consolidated Q1 FY27 results; noted Limited Review Report from MSKA & Associates LLP | |
| 2 | 50 | Issuance of Equity Shares / QIP | Board approved raising up to Rs 750,00,00,000 (Rs 750 Cr) via QIP, subject to shareholder approval at ensuing AGM; Reg 30 additional info in Annexure-II | |
| 3 | 64 | Further investment in Dheya Engineering Technologies Pvt Ltd (Associate) | Up to Rs 5 crore via subscription/secondary sale; Reg 30 additional info to follow post-completion | |
| 4 | 80 | Annual General Meeting | 10th AGM on Friday, August 28, 2026, 11:00 A.M. IST, via VC/OAVM; AR for FY 2025-26 to follow separately | |

### Board meeting timing
| Line | Detail |
|------|--------|
| 93 | Meeting commenced 11:30 A.M., concluded 05:30 P.M. — a 6-hour meeting |

No other agenda items present in this letter: no dividend, no director appointment/resignation
(that item is disclosed only in the results notes, not as a separate Board Outcome agenda item — see
standalone note 8 / consolidated note 9), no auditor change, no scrutinizer appointment, no ESOP
grant beyond what is captured above.

---

## 7. ANNEXURE-II — Reg 30 QIP details table (3 rows, line 634-655)

| # | Line | Particular | Information of event |
|---|------|-----------|------------------------|
| 1 | 643 | Type of securities proposed to be issued | Equity Shares and/or convertible securities or any combination thereof |
| 2 | 646 | Type of issuance | Qualified Institutions Placement |
| 3 | 651 | Total number of securities / total amount | Aggregate consideration not exceeding Rs 750,00,00,000 (Rs 750 Cr), in one or more tranches |

No other annexures present beyond Annexure-I (financial statements + auditor reports, enumerated
in sections 1-5 above) and Annexure-II (this table). No director-profile annexure in this filing.

---

## 8. AUDITOR REPORT PARAGRAPHS (11 total: 4 standalone + 7 consolidated)

### 8a. Standalone Limited Review Report (MSKA & Associates LLP) — 4 paragraphs

| # | Line | Paragraph type | First ~12 words |
|---|------|-----------------|------------------|
| 1 | 142 | Scope of engagement | "We have reviewed the accompanying statement of standalone unaudited financial results..." |
| 2 | 148 | Management responsibility / basis of preparation (Ind AS 34) | "This Statement, which is the responsibility of the Company's Management..." |
| 3 | 155 | Review standard applied (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard..." |
| 4 | 165 | Conclusion (unmodified) | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." |

Opinion type: unmodified (clean) review conclusion. No Emphasis of Matter, no Other Matters
paragraph, no going-concern language in the standalone report. Entities reviewed: standalone
Company only. UDIN: 26233552PBZRGS2214 (line 180). Partner: Pankaj S Bhauwala, Membership No.
233552. Place: Bengaluru. Date: August 03, 2026.

### 8b. Consolidated Limited Review Report (MSKA & Associates LLP) — 7 paragraphs

| # | Line | Paragraph type | First ~12 words |
|---|------|-----------------|------------------|
| 1 | 335 | Scope of engagement | "We have reviewed the accompanying Statement of consolidated unaudited financial results..." |
| 2 | 344 | Management responsibility / basis of preparation (Ind AS 34) | "This Statement, which is the responsibility of the Holding Company's Management..." |
| 3 | 352 | Review standard applied (SRE 2410) + Reg 33(8) circular procedures | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." |
| 4 | 376 | Entity list (Other Matters-adjacent: identifies Group composition) | "This Statement includes the results of the Holding Company and the following entities" — 6-entity table, see section 9 | ENTITY_CHANGE |
| 5 | 408 | Conclusion (unmodified) | "Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing has come to our attention..." |
| 6 | 416 | Other Matters — associate not reviewed by principal auditor | "The Statement also includes the Group's share of net loss after tax of Rs. 13.80 lakhs..." — relies on other auditor's report for Dheya Engineering Technologies Pvt Ltd (Associate); conclusion not modified | OTHER_MATTERS |
| 7 | 439 | Other Matters — unreviewed subsidiary, management-furnished figures | "The Statement includes the financial results of subsidiary which are not subject to review..." — revenue/PAT/TCI all Nil, management-certified, conclusion not modified | OTHER_MATTERS, ZERO_STANDING (see section 5) |

Opinion type: unmodified (clean) review conclusion on the consolidated Statement, with two Other
Matters paragraphs (associate reliance on other auditor; one subsidiary's unaudited/management-
furnished Nil results) — neither modifies the conclusion. No Emphasis of Matter paragraph, no
going-concern language. UDIN: 26233552USOXJO8804 (line 461). Partner: Pankaj S Bhauwala,
Membership No. 233552 (same partner signs both standalone and consolidated reports). Place:
Bengaluru. Date: August 03, 2026.

---

## 9. CONSOLIDATION ENTITY LIST (6 entities, appears twice: auditor report table lines 376-405 and
## notes narrative list lines 566-573 — identical composition in both places)

| Sr | Entity | Relationship to Holding Co | Effective date | Flags |
|----|--------|------------------------------|-----------------|-------|
| 1 | Innomech Aerospace Toolings Private Limited | Wholly Owned Subsidiary | pre-existing | |
| 2 | Unimech Global Manufacturing Solutions Inc. | Wholly Owned Subsidiary | pre-existing | |
| 3 | Uniflux Renewable Energy Private Limited | Subsidiary of Holding Company | w.e.f. April 27, 2026 (incorporated during quarter) | ENTITY_CHANGE (new) |
| 4 | Hobel Bellows Private Limited | Subsidiary of Innomech Aerospace Toolings Private Limited | w.e.f. April 27, 2026 (acquired during quarter) | ENTITY_CHANGE (new) |
| 5 | Hobel Bellows Co. | Subsidiary of Hobel Bellows Private Limited | w.e.f. April 27, 2026 (acquired during quarter) | ENTITY_CHANGE (new) |
| 6 | Dheya Engineering Technologies Private Limited | Associate | pre-existing | |

3 of 6 entities are new to the consolidation this quarter (all effective April 27, 2026). No
prior-quarter ledger was supplied to this run, so this ENTITY_CHANGE determination rests solely on
the "*w.e.f. April 27, 2026" qualifiers and explanatory notes 6/7 (standalone) and 7/8 (consolidated)
describing the Uniflux incorporation and the Hobel Bellows acquisitions within the quarter — not on
an external diff against a prior filing.

---

## 10. SIGNATORY / SIGNATURE BLOCKS (3)

| # | Line | Signatory | Designation | Type | Timestamp | Flags |
|---|------|-----------|-------------|------|-----------|-------|
| 1 | 104-115 | Rashmi Gupta | Company Secretary & Compliance Officer (M. No. A25382) | Digital signature (with certificate timestamp) | 2026.08.03 17:52:07 +05'30' | Signed 22 minutes after board meeting concluded (05:30 P.M. / 17:30) — timing is AFTER conclusion, no red flag |
| 2 | 176-183 | Pankaj S Bhauwala | Partner, MSKA & Associates LLP (Membership No. 233552) | Physical/scanned signature representation, no digital-certificate timestamp | none captured | Standalone auditor report; UDIN 26233552PBZRGS2214; Place Bengaluru; Date August 03, 2026 (date only, no time) |
| 3 | 457-464 | Pankaj S Bhauwala | Partner, MSKA & Associates LLP (Membership No. 233552) | Physical/scanned signature representation, no digital-certificate timestamp | none captured | Consolidated auditor report; UDIN 26233552USOXJO8804; Place Bengaluru; Date August 03, 2026 (date only, no time) |

---

## FLAGS SUMMARY
- ZERO_STANDING (3): auditor report para 7 — revenue/PAT/TCI all Nil for unreviewed subsidiary
- ENTITY_CHANGE (3 entities + 2 cross-referencing notes rows): Uniflux Renewable Energy Pvt Ltd,
  Hobel Bellows Pvt Ltd, Hobel Bellows Co. — all added to consolidation w.e.f. April 27, 2026
- NOTE_NUMBER_NOT_EXTRACTED (5 notes): standalone note 1; consolidated notes 1, 2, 3, 5 — leading
  numeral not present in extracted text (formatting/extraction artifact, confirmed via "Refer note N"
  cross-references and sequential-content logic, not an assumption)
- NUMBERING_ANOMALY (1): consolidated statement reuses index "11" for two distinct line items
  (line 531 "Other comprehensive loss...attributable to" and line 534 "Total comprehensive income
  attributable to") — appears to be a source-document numbering defect, not an extraction fault
- PARTIAL_BLANK (5 rows): standalone line 229; consolidated lines 507, 522, 530, 536 — nil/dash in
  some but not all periods; noted but NOT counted toward the strict ZERO_STANDING flag (which is
  reserved for items nil in ALL reported periods per the operating rules)
- ANNUAL_ONLY_LINE (2 rows): standalone "Other equity" (line 252), consolidated "Other equity"
  (line 542) — nil in all 3 quarterly columns, populated only in the FY column; standard SEBI-format
  convention, not treated as ZERO_STANDING
- OTHER_MATTERS (2 paragraphs): consolidated auditor report paras 6 and 7
