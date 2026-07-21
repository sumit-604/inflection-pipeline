```
=== A2 COUNT TEST ===
category: notes           grep_count: 13  sweep_count: 13  match: yes
category: line_items      grep_count: 65  sweep_count: 65  match: yes
category: zero_standing   grep_count: 6   sweep_count: 6   match: yes
category: agenda_items    grep_count: 6   sweep_count: 6   match: yes
category: annexure_rows   grep_count: 12  sweep_count: 12  match: yes
category: auditor_paras   grep_count: 10  sweep_count: 10  match: yes
category: entities        grep_count: 3   sweep_count: 3   match: yes
category: signature_blocks grep_count: 5  sweep_count: 5   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Reconciliation notes (how grep and manual sweep were made to converge)
- `notes`: naive `grep -n -E "^\s*[0-9]+\s"` on the Consolidated notes block (lines 356-391) returns only 6 (misses note 5) because OCR dropped the leading numeral "5" — the note begins directly with the heading "Key numbers of Standalone Statement of Financial Results...". Refined grep adds an anchor on that heading text; refined count = 7, matching the manual sweep (which reads the note in context and recognizes it as note 5 by position between note 4 and note 6). Standalone notes block (lines 534-561) grepped cleanly at 6/6. Total 7+6=13.
- `line_items`: naive digit-anchored grep on the Consolidated statement (lines 280-345) misses two labels: (a) "Income ta\ relating to items that will not be reclassified..." (line 310) — OCR rendered "tax" as "ta\", breaking a literal-text grep; (b) the Basic EPS row label is dropped entirely by OCR (line 338 shows only the value 6.83, no "Basic" text) and Sr no. "15" itself renders as "IS". Refined patterns (OCR-tolerant regex for "ta.? relating", and a positional rule: unlabeled value row immediately preceding an identical-value "Diluted" row = Basic EPS) bring grep to parity with the manual sweep. Standalone statement (lines 479-522) grepped cleanly. Consolidated 17 Sr-rows + 21 sub-rows = 38; Standalone 14 Sr-rows (incl. unnumbered "Other equity..." row, OCR-mangled to "Mler equity...") + 13 sub-rows = 27. Total 65.
- `zero_standing`: grep on exact labels ("Non controlling interests" x3, "Purchases of stock-in-trade" blank row in Standalone x1, "equity excluding revaluation reserve" x2) = 6, matches manual sweep.
- All other categories (agenda_items, annexure_rows, auditor_paras, entities, signature_blocks) matched grep to sweep on first pass, no OCR-driven refinement needed.

---

## 1. Board Outcome Letter — Agenda Items (Reg 30/33 intimation, dated 17 July 2026)

Board meeting: commenced 11:30 A.M., concluded 03:40 P.M. (line 83) — a 4-hour-10-minute meeting, consistent with a substantive agenda (results + 3 director re-appointments + capacity expansion + borrowing-limit increase), not a rubber-stamp session.

| # | Line(s) | Agenda item | First 15 words | Flags |
|---|---|---|---|---|
| 1 | 36-45 | Unaudited Financial Results (Standalone & Consolidated), Q1FY27, plus Limited Review Reports by NDJ & Co. | "Unaudited Financial Results (Standalone and Consolidated) of the Company for the quarter ended 30 June 2026" | — |
| 2 | 46-51 | Re-appointment of Mr. Chintan Nitinkumar Shah (DIN 00183618) as Managing Director, 3 years from 01-Feb-2027 to 31-Jan-2030, subject to member approval at AGM | "The Board, based on the recommendation of Nomination and Remuneration Committee, has approved the re-appointment of" | AGENDA_SUBJECT_TO_AGM |
| 3 | 52-56 | Re-appointment of Mr. Ajaykumar Mansukhlal Patel (DIN 00183745) as Whole-time Director, 3 years from 01-Feb-2027 to 31-Jan-2030, subject to member approval at AGM | "The Board, based on the recommendation of Nomination and Remuneration Committee, has approved the re-appointment of" | AGENDA_SUBJECT_TO_AGM |
| 4 | 58-62 | Re-appointment of Mr. Shekhar Rasiklal Somani (DIN 00183665) as Whole-time Director, 3 years from 01-Feb-2027 to 31-Jan-2030, subject to member approval at AGM | "The Board, based on the recommendation of Nomination and Remuneration Committee, has approved the re-appointment of" | AGENDA_SUBJECT_TO_AGM |
| 5 | 64-68 | Approval of proposed capacity expansion (new greenfield unit) at Dahej-III, Dahej Industrial Estate, Bharuch, Gujarat | "The Board has approved the proposed capacity expansion (addition) of manufacturing capacities of various" | — |
| 6 | 71-74 | Approval to increase borrowing limits under Sec. 180(1)(c), Companies Act 2013, from Rs 300 cr to Rs 1,000 cr, subject to member approval at AGM | "The Board has approved the proposal for increase in the borrowing limits of the Company" | AGENDA_SUBJECT_TO_AGM, BORROWING_LIMIT_3X |

Note (line 76-78): Items 2, 3, 4, and 5 are cross-referenced to "Annexure A" for detailed Reg 30 disclosure — see Section 5 below. No AGM date, record date, dividend, auditor-change, scrutinizer, or ESOP-grant agenda item is present anywhere in this filing (checked and confirmed absent — not merely unlisted).

---

## 2. Numbered Notes

### 2A. Notes forming part of the Consolidated Statement of Financial Results (lines 356-391)

| Note # | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 359-363 | "in terms of Regulation 33 of the SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015" | — |
| 2 | 365-367 | "The Consolidated Financial Results of the Company for the quarter ended 30 June 2026 has" | — |
| 3 | 368-372 | "The Consolidated Financial Results of the Company have been prepared in accordance with the recognition" | — |
| 4 | 373-375 | "The Company has only one reportable business segment i.e. specialty chemicals, accordingly segment disclosure" | — |
| 5 | 376-385 | "Key numbers of Standalone Statement of Financial Results for the quarter ended 30 June 2026" (embeds a full 5-row standalone key-figures sub-table: Total income from operations, PBT before exceptional items, PBT after exceptional items, PAT, Total comprehensive income) | OCR_NUMBER_MISSING (note number "5" itself dropped by OCR — recovered by manual sweep from sequence position) |
| 6 | 386-388 | "The Consolidated Financial Results of the Company shall be available on the website of BSE" | — |
| 7 | 389-390 | "Figures for the previous periods/year have been reclassified/rearranged/regrouped to conform to classification of current" | — |

### 2B. Notes forming part of the Standalone Statement of Financial Results (lines 534-561)

| Note # | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 538-541 | "in terms of Regulation 33 of the SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015" | — |
| 2 | 543-544 | "The Standalone Financial Results of the Company for the quarter ended 30 June 2026, have" | — |
| 3 | 546-549 | "The Standalone Financial Results of the Company have been prepared in accordance with the recognition" | — |
| 4 | 552-553 | "The Company has only one reportable business segment i.e. specialty chemicals, accordingly segment disclosure" | — |
| 5 | 556-557 | "The Standalone Financial Results of the Company shall be available on the website of BSE" | — |
| 6 | 559-560 | "Figures for the previous periods/year have been reclassified/rearranged/regrouped to conform to classification of current" | — |

No asterisks, daggers, or "Note:" prefixed footnotes were found anywhere else in the filing (swept full-file, none found).

---

## 3. Financial Table Line Items — Consolidated Statement (lines 280-345)

Columns are: Q1FY27 (30.06.2026, Unaudited) | Q4FY26 (31.03.2026, Unaudited) | Q1FY26 (30.06.2025, Unaudited) | FY26 (Audited, year ended).

| Sr | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 286 | Revenue from operations | 1,670.55 | 1,341.44 | 1,168.64 | 5,058.58 | — |
| 2 | 287 | Other income | 27.80 | (3.48) | 11.55 | 35.49 | — |
| 3 | 288 | Total income (1+2) | 1,698.35 | 1,337.96 | 1,180.19 | 5,094.07 | — |
| — | 290 | Cost of materials consumed | 1,054.07 | 672.61 | 638.89 | 2,627.50 | — |
| — | 291 | Purchases of stock-in-trade | 14.03 | 22.43 | 12.89 | 64.94 | — |
| — | 292-293 | Changes in inventories of finished goods, WIP and stock-in-trade | (315.19) | (133.18) | (68.32) | (447.05) | — |
| — | 294 | Employee benefits expense | 167.36 | 170.74 | 140.86 | 629.32 | — |
| — | 295 | Finance costs | 20.81 | 14.38 | 4.13 | 28.51 | — |
| — | 296 | Depreciation and amortisation expenses | 105.66 | 97.55 | 89.71 | 368.47 | — |
| — | 297 | Other expenses | 427.32 | 327.56 | 271.02 | 1,252.29 | — |
| 4 | 299 | Total expenses | 1,474.06 | 1,172.09 | 1,089.18 | 4,523.98 | — |
| 5 | 300 | Profit/(loss) before exceptional items and tax (3-4) | 224.29 | 165.87 | 91.01 | 570.09 | — |
| 6 | 301 | Exceptional items | 13.18 | (blank) | (blank) | (blank) | ONE_TIME_ITEM (present only in current quarter; not zero in all periods so not ZERO_STANDING, but a new line this quarter warranting A3/A4 review of nature) |
| 7 | 302 | Profit/(loss) before tax (5-6) | 211.11 | 165.87 | 91.01 | 570.09 | — |
| — | 304 | Current tax | 10.10 | 30.14 | 18.62 | 119.68 | — |
| — | 305 | Deferred tax | 41.20 | 32.52 | 5.88 | 29.87 | — |
| 8 | 306 | Total tax expenses/(benefits) | 51.30 | 62.66 | 24.50 | 149.55 | — |
| 9 | 307 | Profit for the period/year (7-8) | 159.81 | 103.21 | 66.51 | 420.54 | — |
| — | 309 | Items that will not be reclassified to profit or loss | 0.61 | 2.01 | (0.98) | 2.45 | — |
| — | 310-311 | Income tax relating to items that will not be reclassified to profit or loss | (0.15) | (0.58) | 0.28 | (0.71) | OCR_GARBLED (source text: "Income ta\ relating...") |
| — | 312 | Items that will be reclassified to profit or loss | (3.65) | 12.59 | 6.80 | 30.46 | — |
| — | 313-314 | Income tax relating to items that will be reclassified to profit or loss | not reliably legible | not reliably legible | not reliably legible | not reliably legible | OCR_GARBLED (values appear merged into line 315-316's OCI totals; A3 must request clean source page) |
| 10 | 315-317 | Other comprehensive income/(expense) for the period/year, net of tax | not reliably legible | 14.02 | not reliably legible | 32.20 | OCR_GARBLED |
| 11 | 318 | Total comprehensive income for the period/year (9+10) | 156.62 | 117.23 | 72.61 | 452.74 | — |
| 12 | 321 | Profit for the period/year attributable to: (header) | — | — | — | — | — |
| — | 322 | — Owners of the parent | 159.81 | 103.21 | 66.51 | 420.54 | — |
| — | 323 | — Non controlling interests | nil/dash | nil/dash | nil/dash | nil/dash | ZERO_STANDING (Group's only subsidiaries, per auditor's entity list, are wholly owned — NCI line exists structurally but is nil in all periods) |
| 13 | 325-326 | Other comprehensive income/(expense) for the period/year attributable to: (header) | — | — | — | — | — |
| — | 327 | — Owners of the parent | (3.19) | 14.02 | 6.10 | 32.20 | — |
| — | 328 | — Non controlling interests | nil/dash | nil/dash | nil/dash | nil/dash | ZERO_STANDING |
| 14 | 331-332 | Total comprehensive income for the period/year attributable to: (header) | — | — | — | — | — |
| — | 333 | — Owners of the parent | 156.62 | 117.23 | 72.61 | 452.74 | — |
| — | 334 | — Non controlling interests | nil/dash | nil/dash | nil/dash | nil/dash | ZERO_STANDING |
| 15 | 336-339 | Earnings per share (Face value Rs 10/- each) (not annualised) (header) | — | — | — | — | — |
| — | 338 | — Basic | 6.83 | 4.41 | 2.84 | 17.98 | OCR_LABEL_MISSING (the word "Basic" is entirely absent from OCR text; row identity inferred structurally from position immediately above an identical-value "Diluted" row) |
| — | 339 | — Diluted | 6.83 | 4.41 | 2.84 | 17.98 | — |
| 16 | 341 | Paid-up equity share capital (Face value Rs 10/- each) | 233.92 | 233.92 | 233.92 | 233.92 | — |
| 17 | 344 | Other equity excluding revaluation reserve | (blank) | (blank) | (blank) | 7,583.67 | ZERO_STANDING (balance-sheet-style line, reported only in the annual/audited column — nil by convention in all three quarterly columns) |

Consolidated line-item count: 17 Sr-numbered rows + 21 unnumbered sub-rows = **38**.

---

## 4. Financial Table Line Items — Standalone Statement (lines 479-522)

Columns: Q1FY27 (30.06.2026, Unaudited) | Q4FY26 (31.03.2026, Unaudited) | Q1FY26 (30.06.2025, Unaudited) | FY26 (Audited, year ended).

| Sr | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 484 | Revenue from operations | 1,467.02 | 1,326.65 | 1,091.80 | 4,962.96 | — |
| 2 | 485 | Other income | 40.33 | (3.69) | 13.69 | 35.28 | — |
| 3 | 486 | Total income (1+2) | 1,507.35 | 1,322.96 | 1,105.49 | 4,998.24 | — |
| — | 489 | Cost of materials consumed | 1,054.06 | 672.60 | 638.89 | 2,627.49 | — |
| — | 490 | Purchases of stock-in-trade | nil/dash | nil/dash | nil/dash | nil/dash | ZERO_STANDING (line exists — Consolidated equivalent line carries live values in every period, e.g. 14.03/22.43/12.89/64.94 — so the transaction type occurs at Group level via a subsidiary but never at the standalone/parent entity; a template signal for future related-party stock-in-trade flow into the parent) |
| — | 492 | Changes in inventories of finished goods and work-in-progress | (389.35) | (70.82) | (89.20) | (317.91) | — |
| — | 493 | Employee benefits expense | 167.36 | 170.75 | 140.86 | 629.31 | — |
| — | 494 | Finance costs | 20.81 | 14.38 | 4.13 | 28.51 | — |
| — | 495 | Depreciation and amortisation expense | 105.65 | 97.53 | 89.69 | 368.42 | — |
| — | 496 | Other expenses | 394.70 | 288.77 | 250.58 | 1,130.77 | — |
| 4 | 497 | Total expenses | 1,353.23 | 1,173.21 | 1,034.95 | 4,466.59 | — |
| 5 | 498 | Profit before exceptional items and tax (3-4) | 154.12 | 149.75 | 70.54 | 531.65 | — |
| 6 | 499 | Exceptional items | 13.18 | (blank) | (blank) | (blank) | ONE_TIME_ITEM (mirrors Consolidated Sr 6; same 13.18 amount, so exceptional item originates at standalone/parent level, not from a subsidiary) |
| 7 | 500 | Profit before tax (5-6) | 140.94 | 149.75 | 70.54 | 531.65 | — |
| — | 502 | Current tax | nil (blank) | 25.70 | 12.12 | 100.67 | CURRENT_PERIOD_ZERO (nil only in Q1FY27; not zero in all periods so does not qualify as ZERO_STANDING — flagged for A3/A4 to confirm whether tax-credit / MAT position explains a nil current-tax quarter alongside a live deferred-tax charge) |
| — | 503 | Deferred tax | 36.48 | 33.82 | 7.09 | 40.16 | — |
| 8 | 504 | Total tax expenses | 36.48 | 59.52 | 19.21 | 140.83 | — |
| 9 | 505 | Profit for the period/year (7-8) | 104.46 | 90.23 | 51.33 | 390.82 | — |
| — | 507 | Items that will not be reclassified to profit or loss | 0.61 | 2.01 | (0.98) | 2.45 | — |
| — | 508-509 | Income tax relating to items that will not be reclassified to profit or loss | (0.15) | (0.58) | 0.28 | (0.71) | — |
| 10 | 510-512 | Other comprehensive income/(expenses) for the period/year, net of tax | 0.46 | 1.43 | not reliably legible | 1.74 | OCR_GARBLED; STRUCTURE_DIFF (Standalone has no "items that will be reclassified to profit or loss" sub-lines that Consolidated carries — consistent with no FX-translation reserve at standalone level, since that arises only on consolidating the two foreign subsidiaries) |
| 11 | 513 | Total comprehensive income for the period/year (9+10) | 104.92 | 91.66 | 50.63 | 392.56 | — |
| 12 | 516-517 | Earnings per share (Face value Rs 10/- each) (not annualised) (header) | — | — | — | — | — |
| — | 518 | — Basic | 4.47 | 3.86 | 2.19 | 16.71 | — |
| — | 519 | — Diluted | 4.47 | 3.86 | 2.19 | 16.71 | — |
| 13 | 520-521 | Paid-up equity share capital (Face value Rs 10/- each) | 233.92 | 233.92 | 233.92 | 233.92 | — |
| 14 | 522 | Other equity excluding revaluation reserve | (blank) | (blank) | (blank) | 7,348.37 | ZERO_STANDING (annual-only balance-sheet line, mirrors Consolidated Sr 17; OCR renders label as "Mler ... equity excluding revaluation reserve" and drops the Sr no.) |

Standalone line-item count: 14 Sr-numbered rows (including the unnumbered Sr-14 recovered by manual sweep) + 13 unnumbered sub-rows = **27**.

**Combined financial-table line items: 38 + 27 = 65.**

**ZERO_STANDING total: 6** — Consolidated Sr12/13/14 Non-controlling-interest rows (3), Consolidated Sr17 Other equity (1), Standalone Purchases of stock-in-trade (1), Standalone Sr14 Other equity (1).

---

## 5. Annexures

### 5A. Annexure A — Reg 30 Director Disclosure (page 3, lines 108-166) — covers Board Outcome items 2, 3, 4

One row per director per instruction #4; each row aggregates the 5 Sr-numbered disclosure criteria in the source table (1. Reason for change, 2. Date/term of (re-)appointment, 3. Brief profile, 4. Relationship with other Directors, 5. Debarment status per BSE/NSE circular).

| Row | Line(s) | Name | DIN | Role | Term | Background / relationships | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 112-165 (col 1) | Mr. Chintan Nitinkumar Shah | 00183618 | Managing Director | Re-appointed for 3 years, 01-Feb-2027 to 31-Jan-2030 (current tenure ends 31-Jan-2027), subject to member approval | Age 53, B.E. (Computer Science), founding member/promoter, joined 1996, 30 years' experience; President & Director of Tatva Chintan USA Inc., Board Member of Tatva Chintan Europe B.V.; not related to any other Director; not debarred by SEBI/any authority | — |
| 2 | 112-165 (col 2) | Mr. Ajaykumar Mansukhlal Patel | 00183745 | Whole-time Director | Re-appointed for 3 years, 01-Feb-2027 to 31-Jan-2030 (current tenure ends 31-Jan-2027), subject to member approval | Age 54, B.E. (Chemical), founding member/promoter, joined 1996, 31 years' experience (note: 1 year more than Shah despite same join year — worth a consistency check); Director & Treasurer of Tatva Chintan USA Inc., Board Member of Tatva Chintan Europe B.V.; not related to any other Director; not debarred | EXPERIENCE_YEARS_INCONSISTENCY (31 yrs vs Shah's/Somani's 30 yrs, same 1996 joining year stated for all three) |
| 3 | 112-165 (col 3) | Mr. Shekhar Rasiklal Somani | 00183665 | Whole-time Director | Re-appointed for 3 years, 01-Feb-2027 to 31-Jan-2030 (current tenure ends 31-Jan-2027), subject to member approval | Age 52, Bachelor's in Pharmacy, founding member/promoter, joined 1996, 30 years' experience; Director & Secretary of Tatva Chintan USA Inc., Board Member of Tatva Chintan Europe B.V.; not related to any other Director; not debarred | — |

### 5B. Annexure A — Reg 30 Capacity Expansion Disclosure (page 4, lines 168-186) — covers Board Outcome item 5

| Sr | Line | Particular | Detail | Flags |
|---|---|---|---|---|
| 1 | 175-177 | Existing Capacity | Not applicable — new greenfield unit, no expansion/modification of an existing facility | — |
| 2 | 178 | Existing Capacity Utilization | Not applicable | — |
| 3 | 179 | Proposed Capacity Addition | Installation of aggregate reactor capacity of 344 kilolitres (KL) | — |
| 4 | 180 | Period to add proposed capacity | 21 months (approximately) | — |
| 5 | 181 | Investment Required | Rs 200 crores (approximately) | — |
| 6 | 182 | Mode of Financing | Combination of Internal Accruals and Debt | — |
| 7 | 183-186 | Rationale | Projected growth of chemical industry and anticipated demand increase for specialty chemicals | — |

**Note on labeling:** both 5A (line 110) and 5B (line 171) are headed "Annexure A" — the covering letter (line 78) also refers to a single "Annexure A" for items 2, 3, 4, and 5 collectively. Two physically distinct tables sharing one annexure letter is either intended as one combined annexure split across pages, or a labeling oversight (second part should arguably be "Annexure A (contd.)" or "Annexure B"). Flag: **ANNEXURE_LABEL_DUPLICATE**.

Annexure row count: 5 (5A Sr items) + 7 (5B Sr items) = **12** Sr-numbered rows (presented above as 3 director-summary rows + 7 capacity rows for readability).

---

## 6. Auditor's Review Reports (NDJ & Co., Chartered Accountants, FRN 136345W)

### 6A. Independent Auditor's Review Report on the CONSOLIDATED Statement (pages 5-6, lines 189-267)

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 199-204 | Scope statement: reviewed Consolidated Statement of Tatva Chintan Pharma Chem Ltd (Holding Co.) and subsidiaries ("the Group") for quarter ended 30 June 2026, per Reg 33 | — |
| 2 | 206-211 | Management responsibility; prepared per Ind AS 34; auditor's responsibility is to express a conclusion based on review | — |
| 3 | 213-221 | Review conducted per SRE 2410 (ICAI); review is substantially less in scope than an audit; no audit opinion expressed | — |
| 4 | 223-224 | Additional procedures performed per SEBI Reg 33(8) circular, to the extent applicable | — |
| 5 | 226-231 | Entity list reviewed (see Section 7 below): (a) Tatva Chintan Pharma Chem Ltd — Holding Co.; (b) Tatva Chintan USA Inc. — WOS; (c) Tatva Chintan Europe B.V. — WOS | — |
| 6 | 246-251 | Conclusion: unmodified — "nothing has come to our attention" that the Statement is not in accordance with Ind AS / Reg 33 or contains material misstatement | — |

**Opinion type:** Unmodified (review conclusion, not an audit opinion). **Emphasis of Matter:** none found. **Other Matters paragraph:** none found. **Going Concern language:** none found. **Entities unaudited/management-furnished:** none — both subsidiaries are stated as reviewed within the Group figures (no carve-out language distinguishing which subsidiary financials were reviewed vs furnished by management, which is itself worth noting for A3 — a "based solely on unaudited financial information/ certified by management" caveat is common in such reports and is absent here). **UDIN:** 26434585YAYOYC1333 (line 265). **Signatory:** CA Basant Chandak, Partner, Membership No. 434585, dated 17 July 2026, Place Vadodara (lines 262-267).

### 6B. Independent Auditor's Review Report on the STANDALONE Statement (pages 9-10, lines 405-466)

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 413-417 | Scope statement: reviewed Standalone Statement of Tatva Chintan Pharma Chem Ltd for quarter ended 30 June 2026, per Reg 33 | — |
| 2 | 419-425 | Management responsibility; prepared per Ind AS 34; auditor's responsibility is to express a conclusion based on review | — |
| 3 | 427-436 | Review conducted per SRE 2410 (ICAI); review is substantially less in scope than an audit; no audit opinion expressed | — |
| 4 | 438-444 | Conclusion: unmodified — "nothing has come to our attention" that the Statement is not in accordance with Ind AS / Reg 33 or contains material misstatement | — |

**Opinion type:** Unmodified. **Emphasis of Matter:** none found. **Other Matters:** none found. **Going Concern language:** none found. **UDIN:** 26434585FHXVRU5246 (line 459). **Signatory:** CA Basant Chandak, Partner, Membership No. 434585, dated 17 July 2026, Place Vadodara (lines 455-461). Note: Standalone report has no equivalent to Consolidated para 4 (SEBI Reg 33(8) circular procedures) — 4 paragraphs vs 6, consistent with the absence of a subsidiary entity-list requirement at standalone level.

**Auditor paragraph total: 6 (Consolidated) + 4 (Standalone) = 10.**

---

## 7. Consolidation Entity List (from Consolidated Auditor's Report, para 5, lines 226-231)

No prior-quarter ledger was supplied for this first pipeline run, so no ENTITY_CHANGE diff is possible — noted as a gap, not a finding.

| # | Line | Entity | Relationship | Flags |
|---|---|---|---|---|
| 1 | 228 | Tatva Chintan Pharma Chem Limited | Holding Company | — |
| 2 | 229 | Tatva Chintan USA Inc. | Wholly Owned Subsidiary | — |
| 3 | 230 | Tatva Chintan Europe B.V. | Wholly Owned Subsidiary | — |

Cross-check: both director-profile rows (Section 5A) name these same two subsidiaries as directorship affiliations for Mr. Patel and Mr. Somani — internally consistent, no unlisted entity found in either document.

---

## 8. Digital Signature / Signing Blocks

| # | Line(s) | Document | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 1 | 91-103 | Reg 30/33 intimation letter | Ishwar Ramanbhai Nayi | Company Secretary and Compliance Officer (M. No. A37444) | Digitally signed 2026.07.17 15:42:26 +05'30" | — (meeting concluded 15:40; signature is ~2 min 26 sec AFTER conclusion, not before — checked, no SIGNATURE_BEFORE_CONCLUSION flag warranted) |
| 2 | 397-402 | Consolidated Statement of Financial Results | Chintan N. Shah | Chairman and Managing Director (DIN 00183618) | Date 17 July 2026, Place Vadodara (no intraday timestamp — physical/typed signature block, not a digital-signature-certificate block) | NO_DIGITAL_TIMESTAMP |
| 3 | 569-575 | Standalone Statement of Financial Results | Chintan N. Shah | Chairman and Managing Director (DIN 00183618) | Date 17 July 2026, Place Vadodara (no intraday timestamp) | NO_DIGITAL_TIMESTAMP |
| 4 | 255-267 | Consolidated Auditor's Review Report | CA Basant Chandak | Partner, NDJ & Co. (Membership No. 434585) | Date 17 July 2026, Place Vadodara; UDIN 26434585YAYOYC1333 (no intraday timestamp) | NO_DIGITAL_TIMESTAMP |
| 5 | 449-461 | Standalone Auditor's Review Report | CA Basant Chandak | Partner, NDJ & Co. (Membership No. 434585) | Date 17 July 2026, Place Vadodara; UDIN 26434585FHXVRU5246 (no intraday timestamp) | NO_DIGITAL_TIMESTAMP |

Only signature block #1 carries an actual digital-signature-certificate timestamp; blocks #2-5 are conventional signed/dated blocks without intraday timestamps, so the "signature before meeting concluded" check (instruction #7) can only be performed on block #1, where it does not trigger.

---

## Summary counts

| Category | Count |
|---|---|
| Notes (numbered) | 13 (7 Consolidated + 6 Standalone) |
| Financial-table line items | 65 (38 Consolidated + 27 Standalone) |
| ZERO_STANDING line items | 6 |
| Board Outcome agenda items | 6 |
| Annexure Sr-numbered rows | 12 (5 director-disclosure + 7 capacity-disclosure) |
| Auditor report paragraphs | 10 (6 Consolidated + 4 Standalone) |
| Consolidation entities | 3 |
| Signature/signing blocks | 5 |

Flags raised across the ledger: ZERO_STANDING (x6), ONE_TIME_ITEM (x2 — Exceptional items, Consolidated & Standalone), CURRENT_PERIOD_ZERO (x1 — Standalone current tax), OCR_GARBLED (x3), OCR_LABEL_MISSING (x1), OCR_NUMBER_MISSING (x1), STRUCTURE_DIFF (x1), ANNEXURE_LABEL_DUPLICATE (x1), AGENDA_SUBJECT_TO_AGM (x3), BORROWING_LIMIT_3X (x1), EXPERIENCE_YEARS_INCONSISTENCY (x1), NO_DIGITAL_TIMESTAMP (x4).
