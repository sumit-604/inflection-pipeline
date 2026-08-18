# A2 COMPLETENESS LEDGER — UFBL Q1 FY27 Results (Reg-33)

Source: `extract_results_ufbl_q1fy27.txt` (12 pages, 715 lines, unit ₹ Millions, x0.1 to Cr)

```
=== A2 COUNT TEST ===
category: notes_standalone          grep_count: 14   sweep_count: 14   match: yes
category: notes_consolidated        grep_count: 13   sweep_count: 13   match: yes
category: notes_total               grep_count: 27   sweep_count: 27   match: yes
category: line_items_standalone     grep_count: 23   sweep_count: 23   match: yes  (raw grep 24, 1 wrapped-text false positive at line 161 "and amortisation expense (EBITDA)(1-2)" excluded on re-sweep)
category: line_items_consolidated   grep_count: 30   sweep_count: 30   match: yes  (raw grep 31, 1 wrapped-text false positive at line 488 "amortisation expense (EBITDA)(1-2)" excluded on re-sweep)
category: agenda_items              grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras_standalone  grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras_consolidated grep_count: 8   sweep_count: 8    match: yes
category: auditor_paras_total       grep_count: 12   sweep_count: 12   match: yes
category: zero_standing             grep_count: 2    sweep_count: 2    match: yes  (standalone only; consolidated = 0, confirmed both ways)
category: entities                  grep_count: 13   sweep_count: 13   match: yes  (subsidiaries a-m; +1 Holding Co = 14 total consolidation-scope entities; list identical in auditor report para 4 and note 3)
category: signature_blocks          grep_count: 5    sweep_count: 5    match: yes  (raw narrow-pattern grep "Digitally signed by" returned 3; re-swept with broader pattern "Digitally" and found 2 additional blocks split across a line-wrap — see Section 8 note)
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1, lines 14-64)

| # | Agenda item | Line | Detail | Flags |
|---|---|---|---|---|
| 1 | Approval of un-audited Standalone and Consolidated Financial Results, Q1 FY27 | 34-36 | Board Meeting commenced 12:00 Noon (IST), concluded 12:30 PM (IST) — 30 minutes total. This is the sole agenda item disclosed in the letter. | SINGLE_AGENDA_ITEM (informational — no AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising resolution present in this letter) |

No other agenda items found in a full keyword sweep (approv*, consider*, record date, dividend, AGM, scrutinizer, ESOP, director) across lines 14-64.

---

## 2. STANDALONE AUDITOR REVIEW REPORT — PARAGRAPHS (page 2, lines 66-135)

Auditor: S.R. Batliboi & Associates LLP. Signatory: Sunil Gaggar, Partner, Membership No. 104315. UDIN: 26104315DGARWI5810. Opinion type: Limited Review (SRE 2410), unmodified conclusion — "nothing has come to our attention."

| Para | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 82 | "We have reviewed the accompanying statement of unaudited standalone financial results of United..." — scope | |
| 2 | 88 | "The Company's Management is responsible for the preparation of the Statement in accordance with..." — mgmt responsibility | |
| 3 | 96 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." — SRE 2410 basis | |
| 4 | 107 | "Based on our review conducted as above, nothing has come to our attention that causes..." — unmodified conclusion | |
| — | 129-130 | Place: Bengaluru; Date: August 04, 2026 | |
| — | 119-127 | Signature block: Sunil Gaggar, Partner, signed 2026.08.04 12:27:17 +05'30' | SIGNATURE_TIMING (signed 3 min before board meeting concluded at 12:30 PM) |

No Emphasis of Matter, Other Matters, or Going Concern paragraphs present in the standalone report. Single entity (Company only, no subsidiaries in standalone scope).

---

## 3. STANDALONE P&L STATEMENT — LINE ITEMS (page 3, lines 143-186)

Columns: Q1FY27 (Jun 30 2026, Unaudited) | Q4FY26 (Mar 31 2026, refer note 2) | Q1FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited)

| Row | Sl.No | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | [header] Income | 151 | — | — | — | — | HEADER_ROW |
| 2 | | Revenue from operations | 152 | 3,283.85 | 2,782.35 | 2,289.36 | 10,254.04 | |
| 3 | | Other income | 153 | 17.39 | 2.94 | 22.88 | 120.68 | |
| 4 | | Total income | 154 | 3,301.24 | 2,785.29 | 2,312.24 | 10,374.72 | |
| 5 | 2 | [header] Expenses | 155 | — | — | — | — | HEADER_ROW |
| 6 | | (a) Cost of food and beverages consumed | 156 | 1,179.88 | 1,035.14 | 775.96 | 3,663.56 | |
| 7 | | (b) Employee benefits expense (refer note 9) | 157 | 612.46 | 548.28 | 536.20 | 2,360.02 | |
| 8 | | (c) Other expenses | 158 | 959.11 | 810.33 | 657.22 | 2,942.49 | |
| 9 | | Total expenses | 159 | 2,751.45 | 2,393.75 | 1,969.38 | 8,966.07 | |
| 10 | 3 | EBITDA (1-2) | 160-161 | 549.79 | 391.54 | 342.86 | 1,408.65 | |
| 11 | 4 | Finance costs | 162 | 175.45 | 170.53 | 163.58 | 668.64 | |
| 12 | 5 | Depreciation and amortisation expense | 163 | 313.02 | 334.55 | 348.84 | 1,387.07 | |
| 13 | 6 | Profit/(Loss) before tax (3-4-5) | 164 | 61.32 | (113.54) | (169.56) | (647.06) | |
| 14 | 7 | [header] Tax expense/(credit) | 165 | — | — | — | — | HEADER_ROW |
| 15 | (a) | Current tax expense | 166 | - | - | - | - | ZERO_STANDING |
| 16 | (b) | Adjustment of tax relating to earlier years (refer note 10) | 167-168 | - | - | - | (61.42) | |
| 17 | (c) | Deferred tax | 169 | - | - | - | - | ZERO_STANDING |
| 18 | | Net tax expense/(credit) | 170 | - | - | - | (61.42) | |
| 19 | 8 | Profit/(Loss) after tax (6-7) | 171 | 61.32 | (113.54) | (169.56) | (585.64) | STANDALONE_CONSOLIDATED_PAT_GAP (see Section 9) |
| 20 | 9 | [header] Other comprehensive income/(loss) | 172 | — | — | — | — | HEADER_ROW |
| 21 | | [subheader] Items not reclassified to P&L | 173-174 | — | — | — | — | HEADER_ROW |
| 22 | (a) | Remeasurement gains/(losses) on defined benefit plan | 175-176 | (1.38) | (2.26) | (0.28) | (5.50) | |
| 23 | | Income tax effect on above | 177 | 0.35 | 0.56 | 0.07 | 1.38 | |
| 24 | 10 | Total comprehensive income/(loss) (8+9) | 178 | 60.29 | (115.24) | (169.77) | (589.76) | |
| 25 | 11 | Paid-up equity share capital (FV Rs.5) | 179-180 | 195.43 | 195.43 | 195.41 | 195.43 | |
| 26 | 12 | Other equity | 181 | [blank] | [blank] | [blank] | 3,220.92 | quarterly cols not disclosed (standard practice, not zero-standing) |
| 27 | 13 | [header] EPS (FV Rs.5, not annualised) | 182-184 | — | — | — | — | HEADER_ROW |
| 28 | | Basic (Rs.) | 185 | 1.57 | (2.91) | (4.34) | (14.98) | |
| 29 | | Diluted (Rs.) | 186 | 1.55 | (2.91) | (4.34) | (14.98) | |

Value-bearing line items: 23. Header/subheader rows: 6. Total table rows: 29.

---

## 4. STANDALONE NOTES TO ACCOUNTS (pages 4-5, lines 189-292)

| Note | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 191 | "The above unaudited standalone financial results have been reviewed by the Audit Committee and approved by the [Board]..." | |
| 2 | 196 | "The figures for the quarter ended March 31, 2026 are the balancing figures between..." | |
| 3 | 201 | "The unaudited standalone financial results have been prepared in accordance with the recognition and measurement..." | |
| 4 | 207 | "The name of the Company has changed from 'Barbeque-Nation Hospitality Limited' to 'United Foodbrands Limited'..." | entity rename, effective Sept 18, 2025 |
| 5 | 211 | "On February 03, 2025, the Company executed a Share Subscription Agreement...to acquire upto 51%..." — WGPL became subsidiary June 30, 2025 | |
| 6 | 220 | "The Board of Directors of Red Apple Kitchen Consultancy...and Blue Planet Foods...approved the Scheme of Amalgamation..." — NCLT approved May 29, 2026, appointed date April 1, 2024 | ENTITY_CHANGE |
| 7 | 232 | "On December 16, 2025, Barbeque Nation MENA Holding Limited...purchased the shares of United Foodbrands Thai Holding..." — 2 step-down subsidiaries added | ENTITY_CHANGE |
| 8 | 239 | "On February 24, 2026, Barbeque Nation MENA Holding Limited...incorporated a Limited Liability Company...Barbeque-Qatar..." — 1 step-down subsidiary added | ENTITY_CHANGE |
| 9 | 246 | "On November 21, 2025, the Government of India notified the four Labour Codes...consolidating 29 existing labour laws." — Ԓ46.68mn gratuity + Ԓ14.20mn compensated absences recognised FY26 | |
| 10 | 264 | "During the year ended March 31, 2026, pursuant to favourable Appellate Orders...reversed Ԓ61.42 million..." | |
| 11 | 269 | "During the year ended March 31, 2026, the Company had granted an unsecured loan to its subsidiary Red Apple..." — Ԓ100mn sanctioned, Ԓ14mn disbursed, 4-yr tenor | |
| 12 | 279 | "The Company had impaired the loan advanced to Barbeque Nation MENA Holding Limited...RBI approved write-off Ԓ273.72 million..." | |
| 13 | 286 | "The Company operates in only one segment, viz., operating restaurant business." | |
| 14 | 289 | "Previous periods figures have been regrouped/ reclassified, wherever necessary." | |

14 notes total.

---

## 5. CONSOLIDATED AUDITOR REVIEW REPORT — PARAGRAPHS, ENTITY LIST, RELIANCE (pages 6-8, lines 309-461)

Auditor: S.R. Batliboi & Associates LLP. Signatory: Sunil Gaggar, Partner, Membership No. 104315. UDIN: 26104315AWOZQJ2204. Opinion type: Limited Review (SRE 2410), unmodified conclusion, reliance placed on other auditors and on Management-furnished results for unreviewed entities.

### 5a. Paragraphs

| Para | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 326 | "We have reviewed the accompanying statement of unaudited consolidated financial results of United..." — scope, Holding Co + Group | |
| 2 | 333 | "The Holding Company's Management is responsible for the preparation of the Statement..." | |
| 3 | 341 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." SRE 2410 basis, plus unnumbered continuation (line 352-353) on SEBI Master Circular Reg 33(8) procedures | |
| 4 | 355 | "The Statement includes the results of the following entities:" — entity list (see 5b) | |
| 5 | 387 | "Based on our review conducted and procedures performed as stated in paragraph 3 above..." — unmodified conclusion | |
| 6 | 397 | "The unaudited interim financial results, in respect of 8 subsidiaries...reviewed by their respective independent auditors" — revenue Rs.968.86mn, net loss Rs.25.50mn, TCI loss Rs.26.41mn for Q1FY27; plus 2 unnumbered continuation paragraphs (lines 402-405, 407-416) on furnished-report reliance and foreign GAAP conversion | OTHER_AUDITOR_RELIANCE |
| 7 | 418 | "The accompanying Statement includes unaudited interim financial results in respect of: 3 subsidiaries...not audited/reviewed" — revenue Rs.49.39mn, net loss Rs.11.43mn, TCI loss Rs.11.43mn, deemed immaterial by Management; plus continuation paragraph (lines 424-435) | UNAUDITED_SUBSIDIARY_RELIANCE (management-furnished, not independently reviewed) |
| 8 | 441 | "Our conclusion on the Statement in respect of matters stated in paragraphs 6 and 7 above is not modified..." | |
| — | 459-460 | Place: Bengaluru; Date: August 04, 2026 | |
| — | 449-457 | Signature block: Sunil Gaggar, Partner, signed 2026.08.04 12:26:20 +05'30' | SIGNATURE_TIMING (signed 4 min before board meeting concluded at 12:30 PM) |

Reliance reconciliation for A3: 13 subsidiaries total; 8 reviewed by other auditors (para 6) + 3 unaudited/management-furnished (para 7) = 11; remaining 2 subsidiaries (of the 13) reviewed directly by S.R. Batliboi & Associates LLP as principal auditor (not separately itemised — arithmetic gap, worth an A3 check).

### 5b. Entity List — Auditor Report Para 4 (lines 355-385)

| # | Entity | Relationship | Line | Flags |
|---|---|---|---|---|
| 1 | United Foodbrands Limited (fka Barbeque-Nation Hospitality Limited) | Holding Company | 358 | |
| 2 | Barbeque Nation Mena Holding Limited | Subsidiary (a) | 361 | |
| 3 | Barbeque Nation Restaurants LLC | Subsidiary (b) | 362 | |
| 4 | Barbeque Nation (Malaysia) SDN. BHD. | Subsidiary (c) | 363 | |
| 5 | Barbeque Nation International LLC | Subsidiary (d) | 364 | |
| 6 | Barbeque Nation Bahrain W.L.L. | Subsidiary (e) | 365 | |
| 7 | Barbeque Nation Lanka (Pvt) Ltd | Subsidiary (f) | 366 | |
| 8 | Barbeque Nation Saudi Arabia Limited | Subsidiary (g) | 367 | |
| 9 | United Foodbrands Thai Holding Co., Ltd. * | Subsidiary (h), step-down, ops not commenced | 368 | |
| 10 | United Foodbrands Thai Co., Ltd. | Subsidiary (i), step-down | 369 | |
| 11 | Barbeque Nation Restaurant W.L.L. (Qatar) * | Subsidiary (j), step-down, ops not commenced | 370 | |
| 12 | Red Apple Kitchen Consultancy Private Limited | Subsidiary (k) | 371 | |
| 13 | Blue Planet Foods Private Limited (amalgamated with Red Apple w.e.f. May 29, 2026) | Subsidiary (l), merged into (k) | 381-382 | ENTITY_CHANGE |
| 14 | Willow Gourmet Private Limited | Subsidiary (m) | 383 | |

13 subsidiaries + 1 Holding Company = 14 entities. List cross-checked against Note 3 (Section 7 below) — identical, no discrepancy within this filing. No prior-quarter ledger supplied to this run, so a cross-quarter ENTITY_CHANGE diff could not be performed; the amalgamation of entity 13 into entity 12 (effective retroactively from April 1, 2024, court-approved May 29, 2026) is itself flagged as a substantive entity-structure change for A3.

---

## 6. CONSOLIDATED P&L STATEMENT — LINE ITEMS (page 9, lines 462-528)

Columns: Q1FY27 (Jun 30 2026, Unaudited) | Q4FY26 (Mar 31 2026, refer note 2) | Q1FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited)

| Row | Sl.No | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | [header] Income | 477 | — | — | — | — | HEADER_ROW |
| 2 | | Revenue from operations | 478 | 4,258.99 | 3,603.96 | 2,969.81 | 13,387.02 | |
| 3 | | Other income | 479 | 12.38 | 30.64 | 19.33 | 147.88 | |
| 4 | | Total income | 480 | 4,271.37 | 3,634.60 | 2,989.14 | 13,534.90 | |
| 5 | 2 | [header] Expenses | 481 | — | — | — | — | HEADER_ROW |
| 6 | | (a) Cost of food and beverages consumed | 482 | 1,456.69 | 1,242.80 | 959.69 | 4,498.34 | |
| 7 | | (b) Employee benefits expense (refer note 11) | 483 | 870.14 | 790.33 | 729.08 | 3,229.86 | |
| 8 | | (c) Other expenses | 484 | 1,233.59 | 1,026.84 | 820.92 | 3,729.28 | |
| 9 | | Total expenses | 485 | 3,560.42 | 3,059.97 | 2,509.69 | 11,457.48 | |
| 10 | 3 | EBITDA, before share of associate (1-2) | 486-488 | 710.95 | 574.63 | 479.45 | 2,077.42 | |
| 11 | 4 | Share of profit of associate (net of tax) | 489 | - | - | 0.28 | 0.28 | |
| 12 | 5 | EBITDA, after share of associate (3+4) | 490-491 | 710.95 | 574.63 | 479.73 | 2,077.70 | |
| 13 | 6 | Finance costs | 492 | 229.47 | 226.49 | 200.36 | 860.40 | |
| 14 | 7 | Depreciation and amortisation expense | 493 | 457.14 | 485.66 | 449.24 | 1,899.92 | |
| 15 | 8 | Profit/(Loss) before tax (5-6-7) | 494 | 24.34 | (137.52) | (169.87) | (682.62) | |
| 16 | 9 | [header] Tax expense/(credit) | 495 | — | — | — | — | HEADER_ROW |
| 17 | (a) | Current tax expense | 496 | 1.18 | 3.83 | - | 6.17 | |
| 18 | (b) | Adjustment of tax relating to earlier years (refer note 12) | 497-498 | - | (1.17) | - | (62.59) | |
| 19 | (c) | Deferred tax | 499 | 0.08 | 10.52 | (3.12) | (7.09) | |
| 20 | | Net tax expense/(credit) | 500 | 1.26 | 13.18 | (3.12) | (63.51) | |
| 21 | 10 | Profit/(Loss) after tax (8-9) | 501 | 23.08 | (150.70) | (166.75) | (619.11) | STANDALONE_CONSOLIDATED_PAT_GAP (see Section 9) |
| 22 | 11 | [header] Profit/(Loss) attributable to | 502 | — | — | — | — | HEADER_ROW |
| 23 | | Owners of the Company | 503 | 30.93 | (134.08) | (164.09) | (591.31) | |
| 24 | | Non-controlling interest | 504 | (7.85) | (16.62) | (2.66) | (27.80) | |
| 25 | 12 | [header] Other comprehensive income/(loss) | 505 | — | — | — | — | HEADER_ROW |
| 26 | | [subheader] Items not reclassified to P&L | 506-507 | — | — | — | — | HEADER_ROW |
| 27 | (a) | Remeasurement gains/(losses) on defined benefit plan | 508-509 | (2.61) | 8.63 | (0.19) | 2.49 | |
| 28 | | Income tax effect on above | 510 | 0.66 | (2.17) | 0.05 | (0.63) | |
| 29 | | [subheader] Items to be reclassified to P&L | 511-512 | — | — | — | — | HEADER_ROW |
| 30 | (a) | Exchange differences on translating foreign operations | 513-514 | 1.78 | (5.72) | 7.25 | (16.24) | |
| 31 | 13 | Total comprehensive income/(loss) (10+12) | 515 | 22.91 | (149.96) | (159.64) | (633.49) | |
| 32 | 14 | [header] Total comprehensive income/(loss) attributable to | 516-517 | — | — | — | — | HEADER_ROW |
| 33 | | Owners of the Company | 518 | 30.93 | (134.45) | (156.98) | (606.80) | |
| 34 | | Non-controlling interest | 519 | (8.02) | (15.51) | (2.66) | (26.69) | |
| 35 | 15 | Paid-up equity share capital (FV Rs.5) | 520-521 | 195.43 | 195.43 | 195.41 | 195.43 | |
| 36 | 16 | Other equity | 522 | [blank] | [blank] | [blank] | 2,907.64 | quarterly cols not disclosed (standard practice, not zero-standing) |
| 37 | 17 | [header] EPS (FV Rs.5, not annualised) | 523-525 | — | — | — | — | HEADER_ROW |
| 38 | | Basic (Rs.) | 526 | 0.79 | (3.43) | (4.20) | (15.13) | |
| 39 | | Diluted (Rs.) | 527 | 0.78 | (3.43) | (4.20) | (15.13) | |

Value-bearing line items: 30. Header/subheader rows: 9. Total table rows: 39.

---

## 7. CONSOLIDATED NOTES TO ACCOUNTS (pages 10-12, lines 530-702)

| Note | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 532 | "The above unaudited consolidated financial results of United Foodbrands Limited...have been reviewed by the Audit Committee..." | |
| 2 | 538 | "The figures for the quarter ended March 31, 2026 are the balancing figures between audited..." | |
| 3 | 542 | "As at June 30, 2026, the Holding Company has the following subsidiaries:" — repeats 13-entity list a-m, see 7a | matches auditor-report para 4 list, no ENTITY_CHANGE within filing |
| 4 | 561 | "The Group operates in only one segment, viz., operating restaurant business...single segment" + Geographical segment sub-table, see 7b | |
| 5 | 577 | "The unaudited consolidated financial results have been prepared in accordance with the recognition and measurement..." | |
| 6 | 582 | "The name of the Holding Company has changed from 'Barbeque-Nation Hospitality Limited' to 'United Foodbrands Limited'..." | entity rename, effective Sept 18, 2025 |
| 7 | 585 | "On February 03, 2025, the Holding Company executed a Share Subscription Agreement...to acquire upto 51%..." — WGPL | |
| 8 | 592 | "The Board of Directors of Red Apple Kitchen Consultancy...and Blue Planet Foods...approved the Scheme of Amalgamation..." + NCI restatement tables, see 7c | ENTITY_CHANGE |
| 9 | 664 | "On December 16, 2025, Barbeque Nation MENA Holding Limited...purchased the shares of United Foodbrands Thai Holding..." | ENTITY_CHANGE |
| 10 | 671 | "On February 24, 2026, Barbeque Nation MENA Holding Limited...incorporated a Limited Liability Company...Barbeque-Qatar..." | ENTITY_CHANGE |
| 11 | 678 | "On November 21, 2025, the Government of India notified the four Labour Codes...consolidating 29 existing labour laws." — Ԓ55.13mn gratuity + Ԓ19.58mn compensated absences, Group level FY26 | |
| 12 | 695 | "During the year ended March 31, 2026, pursuant to favourable Appellate Orders...reversed Ԓ61.42 million..." | |
| 13 | 699 | "Previous periods figures have been regrouped/ reclassified, wherever necessary." | |

13 notes total.

### 7a. Note 3 Entity List (lines 542-560)

Identical to Section 5b list (13 subsidiaries a-m, Blue Planet amalgamated into Red Apple w.e.f. May 29, 2026, cross-referenced "Refer note 8"). Cross-checked line by line against auditor report para 4: MATCH, no discrepancy.

### 7b. Note 4 Geographical Segment Table (lines 568-574)

| Country | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 |
|---|---|---|---|---|---|
| India | 573 | 3,873.57 | 3,267.58 | 2,706.90 | 12,139.90 |
| Others (Overseas) | 574 | 385.42 | 336.38 | 262.91 | 1,247.12 |

### 7c. Note 8 NCI Restatement Tables (lines 613-662) — impact of Blue Planet/Red Apple amalgamation on attribution

Three period sub-tables, each with 6 rows (Owners/NCI x PAT/OCI/TCI), showing Previously Reported -> Adjustment -> Restated:

**Table 1 — Year ended March 31, 2026 (lines 615-628):**
| Line item | Line | Previously reported | Adjustment | Restated |
|---|---|---|---|---|
| Owners — Profit/(Loss) | 619 | (591.31) | 1.81 | (589.50) |
| NCI — Profit/(Loss) | 620 | (27.80) | (1.81) | (29.61) |
| Owners — OCI | 623 | (15.49) | (0.02) | (15.51) |
| NCI — OCI | 624 | 1.11 | 0.02 | 1.13 |
| Owners — TCI | 627 | (606.80) | 1.79 | (605.01) |
| NCI — TCI | 628 | (26.69) | (1.79) | (28.48) |

**Table 2 — Quarter ended March 31, 2026 (lines 631-645):**
| Line item | Line | Previously reported | Adjustment | Restated |
|---|---|---|---|---|
| Owners — Profit/(Loss) | 636 | (134.08) | 0.10 | (133.98) |
| NCI — Profit/(Loss) | 637 | (16.62) | (0.10) | (16.72) |
| Owners — OCI | 640 | (0.37) | (0.07) | (0.44) |
| NCI — OCI | 641 | 1.11 | 0.07 | 1.18 |
| Owners — TCI | 644 | (134.45) | 0.03 | (134.42) |
| NCI — TCI | 645 | (15.51) | (0.03) | (15.54) |

**Table 3 — Quarter ended June 30, 2025 (lines 648-662):**
| Line item | Line | Previously reported | Adjustment | Restated |
|---|---|---|---|---|
| Owners — Profit/(Loss) | 653 | (164.09) | 0.71 | (163.38) |
| NCI — Profit/(Loss) | 654 | (2.66) | (0.71) | (3.37) |
| Owners — OCI | 657 | 7.11 | - | 7.11 |
| NCI — OCI | 658 | - | - | - | ZERO_STANDING (this row only, all 3 columns nil) |
| Owners — TCI | 661 | (156.98) | 0.71 | (156.27) |
| NCI — TCI | 662 | (2.66) | (0.71) | (3.37) |

18 restated data rows total across the three tables. This restatement means every prior-period NCI/owner attribution figure quoted anywhere else in this filing (and any prior-quarter filing referencing the pre-restatement numbers) is now superseded — a reconciliation point for A3.

---

## 8. DIGITAL SIGNATURE BLOCKS (all pages)

Board Meeting window: commenced 12:00 Noon (IST), concluded 12:30 PM (IST) on August 4, 2026 (line 34).

| # | Signatory | Designation | Document | Line | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 1 | Nagamani C Y | Company Secretary & Compliance Officer | Board Outcome letter | 53-62 | 2026.08.04 12:42:05 +05'30' | (after meeting concluded — expected) |
| 2 | Rahul Agrawal | CEO & Whole-time Director (DIN-07194134) | Standalone Financial Results | 298-304 | 2026.08.04 12:09:04 +05'30' | SIGNATURE_TIMING — signed 21 min before meeting concluded |
| 3 | Sunil Gaggar | Partner, S.R. Batliboi & Associates LLP (Membership 104315) | Standalone Review Report (UDIN 26104315DGARWI5810) | 119-127 | 2026.08.04 12:27:17 +05'30' | SIGNATURE_TIMING — signed 3 min before meeting concluded |
| 4 | Sunil Gaggar | Partner, S.R. Batliboi & Associates LLP (Membership 104315) | Consolidated Review Report (UDIN 26104315AWOZQJ2204) | 449-457 | 2026.08.04 12:26:20 +05'30' | SIGNATURE_TIMING — signed 4 min before meeting concluded |
| 5 | Rahul Agrawal | CEO & Whole-time Director (DIN-07194134) | Consolidated Financial Results | 705-712 | 2026.08.04 12:10:59 +05'30' | SIGNATURE_TIMING — signed 19 min before meeting concluded |

Reconciliation note: initial grep with the narrow literal pattern `"Digitally signed by"` returned 3 hits (missed rows 2 and 5, where the phrase wraps across a line break as "Digitally  signed" / "by ..."). Re-swept with the broader pattern `"Digitally"` and located all 5 blocks — GATE A2 re-sweep working as designed.

All 4 of the financial-document signatures (rows 2-5: both CEO signatures and both auditor signatures) are timestamped BEFORE the 12:30 PM board meeting conclusion — the substantive documents were signed while the 30-minute meeting was still nominally in progress. Only the Company Secretary's outward-facing cover letter (row 1) was signed after the meeting concluded, which is the expected sequence. This is flagged as SIGNATURE_TIMING for A3.

---

## 9. CROSS-CUTTING FLAGS FOR A3 (first-class items)

| Flag | Description | Evidence lines |
|---|---|---|
| STANDALONE_CONSOLIDATED_PAT_GAP | Standalone PAT Q1FY27 = Rs.61.32mn vs Consolidated PAT (total) Q1FY27 = Rs.23.08mn (Consolidated PAT attributable to Owners = Rs.30.93mn). The standalone entity alone reports nearly double the group's total post-tax profit, and the group figure is further split with NCI absorbing a Rs.(7.85)mn loss. The gap (~Rs.38mn between standalone PAT and consolidated PAT) implies the consolidated subsidiaries as a group were loss-making in Q1FY27, dragging down an otherwise profitable standalone quarter. | Standalone: line 171 (61.32); Consolidated: line 501 (23.08), line 503 (30.93 owners), line 504 (-7.85 NCI) |
| SIGNATURE_TIMING | 4 of 5 signature blocks (both CEO signatures, both auditor review-report signatures) are timestamped before the 30-minute board meeting concluded at 12:30 PM. | Lines 298-304, 449-457, 705-712 vs meeting end time line 34 |
| ENTITY_CHANGE | Blue Planet Foods Private Limited amalgamated into Red Apple Kitchen Consultancy Private Limited, NCLT-approved May 29, 2026, retroactively effective April 1, 2024; triggers a 3-period NCI/owner attribution restatement (18 data rows, Section 7c). Also: 2 Thai step-down subsidiaries added (note 7/9), 1 Qatar step-down subsidiary added (note 8/10), all since prior FY. | Standalone notes 6,7,8 (lines 220,232,239); Consolidated notes 8,9,10 (lines 592,664,671) |
| ZERO_STANDING | Standalone: Current tax expense and Deferred tax are nil across all 4 periods (template rows, no current-year current-tax or deferred-tax charge/credit at the standalone level). Consolidated Note 8 Table 3: NCI — OCI row is nil across all 3 restatement columns for the June 30 2025 quarter only. | Lines 166, 169; line 658 |
| OTHER_AUDITOR_RELIANCE / UNAUDITED_SUBSIDIARY_RELIANCE | 8 of 13 subsidiaries reviewed by other (non-principal) auditors; 3 of 13 unaudited/management-furnished and deemed immaterial by Management; principal auditor directly covers the remaining 2 (arithmetic gap not itemised in the report — worth an A3 check). | Lines 397-436 |

---

## SUMMARY COUNTS

- Notes: 27 (14 standalone + 13 consolidated)
- Line items (value-bearing, core P&L): 53 (23 standalone + 30 consolidated); header/subheader rows enumerated separately: 15 (6 standalone + 9 consolidated); supplementary embedded-table rows (geographical segment + NCI restatement): 20 (2 + 18)
- Zero-standing line items: 2 (standalone: current tax expense, deferred tax) + 1 restatement-table row (consolidated Note 8, NCI OCI, Q1FY26 column)
- Agenda items: 1
- Auditor review-report paragraphs: 12 (4 standalone + 8 consolidated)
- Auditor review reports: 2 (1 standalone, 1 consolidated)
- Entities in consolidation scope: 14 (1 Holding Co + 13 subsidiaries)
- Digital signature blocks: 5
