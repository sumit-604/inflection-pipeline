# A2 COMPLETENESS LEDGER — KRN Heat Exchanger and Refrigeration Limited — Q1 FY27 (results filing)

Source: `runs/krn-q1fy27/work/extract_results_krn_q1fy27.txt` (13 pages, unit = Lakhs, no OCR pages,
line-numbered extract). NOTE: A1 header states `line_count: 708`; the extract as read actually
runs to line 735 (page 13 content ends at line 735, trailing header line 736). This is a header/body
line-count mismatch in the A1 artifact — flagged `HEADER_MISCOUNT` for A3 to carry forward; it does not
affect line-number citations below, which are taken directly off the file as delivered.

Prior-quarter ledger: not supplied — `ENTITY_CHANGE` and `DROPPED_SLIDE`-style diffs cannot be run this
cycle; noted as `NO_PRIOR_LEDGER` where relevant.

=== A2 COUNT TEST ===
```
category: notes                 grep_count: 18   sweep_count: 18   match: yes
category: agenda_items          grep_count: 3    sweep_count: 3    match: yes
category: line_items            grep_count: 63   sweep_count: 63   match: yes
category: zero_standing         grep_count: 51   sweep_count: 51   match: yes
category: segment_rows          grep_count: 36   sweep_count: 36   match: yes
category: export_countries      grep_count: 22   sweep_count: 22   match: yes
category: auditor_paras         grep_count: 16   sweep_count: 16   match: yes
category: entities              grep_count: 2    sweep_count: 2    match: yes
category: annexure_items        grep_count: 8    sweep_count: 8    match: yes
category: signature_blocks      grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Reconciliation notes (method, per category)
- **notes**: first grep pass `^\s*[0-9]+\.\s` and a naive `^\s*\[[0-9]+\]` pass both undercounted
  (7/9 consolidated notes matched) because OCR mangled three closing brackets to non-bracket
  characters — `[SJ` for `[5]` at line 193, `[71` for `[7]` at line 198, and `(2]`/`(9]` using a
  paren instead of a bracket at lines 184/238. A widened regex
  `^\s*[\[\(][0-9A-Za-z]{1,2}[])1lJ]` plus manual visual sweep of both notes blocks (pages 4 and 9)
  converged on 18/18 (9 consolidated + 9 standalone). GATE A2 pass only after this re-sweep — logged
  per operating rule 4.
- **line_items**: P&L tables (lines 116-165 consolidated, 419-456 standalone) were read twice
  independently (raw sequential read, then `sed -n | nl` re-verification) and produced identical
  35 + 28 = 63 row counts both passes. A literal single-line grep is unreliable here because several
  rows span 2-3 physical lines (e.g. "Changes in Inventories..." at lines 123-125) and OCR splits
  decimals across whitespace; the two independent manual passes serve as the reconciliation.
- **zero_standing**: tallied per table below on a first pass, then independently re-tallied by
  grepping the literal string `ZERO_STANDING` inside each of tables C, D, F2, F3, F5, F6, H1, I1, M1,
  M2 in isolation. First pass under-tallied at 45 (missed the "Purchase of Stock-in-trade" nil-in-one-
  quarter row in tables C and D, and undercounted the QIP unutilized-balance Total rows in F2/F5) —
  re-swept per operating rule 4 and converged on 51/51: C=9, D=6, H1=9, I1=9, F2=4, F3=4, F5=4, F6=4,
  M1=1, M2=1.
- **segment_rows**: 18 non-country rows per segment note x 2 statements (9 consolidated line items
  across Segment Revenue/Results/Capital Employed + 9 standalone) = 36 total, verified against manual
  sweep of lines 265-291 and 552-577.
- **export_countries**: grep `^[A-Za-z].*[0-9]\.[0-9]{2}$` inside lines 295-308 (14 rows) and 582-589
  (8 rows) = 22, matches manual country-by-country sweep.
- **auditor_paras**: table J (consolidated LRR) enumerates 10 discrete elements (title, addressee,
  scope, management-responsibility, review-standard/basis, entity list, conclusion, other-matters/
  subsidiary-reliance, modification statement, signature); table K (standalone LRR) enumerates 6
  (title, addressee, scope+responsibility, review-standard/basis, conclusion, signature — no entity
  list or Other Matters paragraph, confirmed absent by sweep since standalone has no subsidiaries).
  10 + 6 = 16, matching a second independent count of the row totals in tables J and K.
- **entities**: 2 subsidiaries listed at lines 367-368, cross-checked against the "2 subsidiaries"
  figure quoted in the LRR other-matters paragraph (line 382) — internally consistent.
- **annexure_items**: 2 Reg 30 appointment blocks x 4 sub-rows (S.No. 1-4) = 8.
- **signature_blocks**: CS digital signature (1), two auditor signatures (2), two unnamed "For and on
  behalf of Board of Directors" placeholder blocks on the P&L statements (2) = 5.

---

## A. Board Outcome — Agenda Items (letter, pages 1-2, lines 15-101)

| # | Line(s) | Agenda item | First 15 words | Flags |
|---|---------|-------------|-----------------|-------|
| 1 | 39-51 | Unaudited Financial Results (Consol + Standalone) for Q1 FY27 approved | "Approved the Unaudited Financial Results (both Consolidated and Standalone) of the Company for the quarter" | — |
| 2 | 53-57 | Appointment of Cost Auditor FY26-27 — M/s. R S Chauhan & Associates (FRN 003517) | "Pursuant to the recommendation of Audit Committee, the Board of Directors approved the appointment" | — |
| 3 | 59-64 | Appointment of Internal Auditor FY26-27 — M/s. Sharma Shankar & Co. (FRN 019317C) | "Pursuant to the recommendation of Audit Committee, the Board of Directors approved the appointment" | — |

No AR approval, AGM notice, record date, dividend, director appointment/resignation, statutory-auditor
change, scrutinizer, ESOP, or capital-raising enabling resolution appears as a fourth agenda item —
confirmed absent by sweep of lines 15-101, not merely unlisted.

**Board meeting timing** (line 79-80): commenced 15:30, concluded 15:59 — a 29-minute meeting for three
agenda items including full quarterly results approval. Recorded as a data point, not interpreted here.

## B. Digital / Named Signature Blocks

| # | Line(s) | Signatory | Role | Timestamp / Date | Flags |
|---|---------|-----------|------|-------------------|-------|
| 1 | 88-94 | Jitendra Kumar Sharma | Company Secretary (Board Outcome letter) | Digitally signed 2026.08.12 17:26:24 +05'30' | Signed ~1h27m after board meeting concluded (15:59) — normal sequence, no `SIGNATURE_TIMING` flag |
| 2 | 393-403 | Keyur Shah | Proprietor, Keyur Shah & Co., FRN 141173W (consolidated LRR) | Date 12th Aug 2026, UDIN 26153774EUACWV7849 | — |
| 3 | 637-647 | Keyur Shah | Proprietor, Keyur Shah & Co., FRN 141173W (standalone LRR) | Date 12th Aug 2026, UDIN 26153774LHTHBS5726 | — |
| 4 | 458-459 | (unnamed) | "For and on the behalf of Board of Directors ... [Heat] Exchanger and Refrigeration Limited" on consolidated/standalone P&L | no name/designation legible | `INCOMPLETE_SIGNATURE` (OCR-garbled or stamp-only, no extractable signatory name) |
| 5 | 533-534 | (unnamed) | Same placeholder, standalone P&L page | no name/designation legible | `INCOMPLETE_SIGNATURE` |

## C. Consolidated P&L — Line Items (pages 3, lines 116-165)

| # | Line(s) | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---------|------|--------|--------|--------|------|-------|
| 1 | 117 | Revenue from operations | 25,231.70 | 17,947.98 | 11,528.21 | 60,005.77 | — |
| 2 | 118 | Other Income | 277.76 | 191.55 | 357.53 | 974.82 | — |
| 3 | 119 | Total Income (I+II) | 25,509.46 | 18,139.53 | 11,885.74 | 60,980.59 | — |
| 4 | 121 | Cost of materials consumed | 16,441.22 | 5,700.12 | 9,067.18 | 24,311.80 | — |
| 5 | 122 | Purchase of Stock-in-trade | 921.46 | 8,048.00 | (blank) | 21,165.88 | `ZERO_STANDING` (Q1FY26 blank) |
| 6 | 123-125 | Changes in Inventories of Finished Goods, WIP and Stock-in-Trade | (260.14) | (1,655.63) | (495.19) | (4,298.62) | — |
| 7 | 126 | Employee benefit expenses | 1,819.26 | 1,349.62 | 665.37 | 4,156.36 | — |
| 8 | 127 | Finance costs | 304.12 | 264.03 | 69.55 | 590.08 | — |
| 9 | 128 | Depreciation and amortisation expense | 646.76 | 597.44 | 218.50 | 1,876.49 | — |
| 10 | 129 | Other expenses | 1,403.70 | 1,151.02 | 531.43 | 3,422.74 | — |
| 11 | 130 | Total expenses (IV) | 21,276.38 | 15,454.60 | 10,056.84 | 51,224.73 | — |
| 12 | 131 | Profit Before Prior Period and Exceptional Item (III-IV) | 4,233.08 | 2,684.93 | 1,828.90 | 9,755.86 | — |
| 13 | 132 | Prior Period Item/Exceptional Item | blank | blank | blank | 39.71 | `ZERO_STANDING` (all quarters) |
| 14 | 133 | Profit before tax (V-VI) | 4,233.08 | 2,684.93 | 1,828.90 | 9,795.57 | — |
| 15 | 135 | Current tax | 763.74 | 498.18 | 537.61 | 2,382.39 | — |
| 16 | 136 | Deferred tax Liability/(Assets) | 179.78 | 153.25 | 49.21 | 69.09 | — |
| 17 | 137 | Income Tax (Short/Excess provision) | blank | 302.65 | blank | 302.65 | `ZERO_STANDING` (current & prior-year quarter) |
| 18 | 138 | Total Tax expenses (VIII) | 943.52 | 346.76 | 566.82 | 2,148.63 | — |
| 19 | 139 | Profit for the period (VII-VIII) | 3,269.56 | 2,336.15 | 1,242.08 | 7,646.74 | — |
| 20 | 142 | Remeasurements of defined benefit plans (OCI) | 19.18 | (3.67) | (2.38) | (14.26) | — |
| 21 | 143 | Income Tax relating to above (OCI) | (4.51) | 0.79 | 1.35 | 3.98 | — |
| 22 | 144-145 | [Duplicate heading] "Items that will not be reclassified..." — Remeasurements of defined benefit plans | blank | blank | blank | blank | `ZERO_STANDING` + template artifact (duplicate row, fully blank all periods) |
| 23 | 146 | [Duplicate] Income Tax relating to above | blank | blank | blank | blank | `ZERO_STANDING` + template artifact |
| 24 | 147 | Total Other Comprehensive Income (X) | 14.67 | (2.88) | (1.03) | (10.28) | — |
| 25 | 148 | Total Comprehensive Income for the year (IX-X) | 3,274.89 | 2,339.03 | 1,243.11 | 7,657.02 | — |
| 26 | 150 | Net Profit attributable to: a) Owner of the company | 3,289.56 | 2,336.15 | 1,242.08 | 7,646.74 | Note: figure (3,289.56) differs from line-19 "Profit for the period" (3,269.56) — possible transcription/typo in source; flagged for A3 (`FIGURE_MISMATCH`), not resolved here |
| 27 | 151 | Net Profit attributable to: b) Non Controlling Interest | blank | blank | blank | blank | `ZERO_STANDING` (all periods — no NCI; both subsidiaries wholly owned) |
| 28 | 153 | OCI attributable to: a) Owner of the company | 14.67 | (2.88) | (1.03) | (10.28) | — |
| 29 | 154 | OCI attributable to: b) Non Controlling Interest | blank | blank | blank | blank | `ZERO_STANDING` |
| 30 | 157 | Total Comprehensive Income attributable to: a) Owner of the company | 3,274.89 | 2,339.03 | 1,243.11 | 7,657.02 | — |
| 31 | 158 | Total Comprehensive Income attributable to: b) Non Controlling Interest | blank | blank | blank | blank | `ZERO_STANDING` |
| 32 | 160 | Net Profit after Tax and Non Controlling Interest | 3,289.56 | 2,336.15 | 1,242.08 | 7,646.74 | Same figure as row 26; see `FIGURE_MISMATCH` note |
| 33 | 161 | Paidup Equity Share Capital (FV Rs 10) | 6,545.85 | 6,215.66 | 6,215.66 | 6,215.66 | — |
| 34 | 162 | Other Equity | blank | blank | blank | 51,183.82 | `ZERO_STANDING` (quarterly columns not disclosed, standard practice) |
| 35 | 165 | EPS Basic/Diluted | 5.20 | 3.75 | 2.00 | 12.30 | — |

## D. Standalone P&L — Line Items (page 8, lines 419-456)

| # | Line(s) | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---------|------|--------|--------|--------|------|-------|
| 1 | 420 | Revenue from operations | 18,197.15 | 20,206.18 | 11,439.90 | 67,623.01 | — |
| 2 | 421 | Other Income | 242.17 | 286.71 | 274.03 | 1,372.29 | — |
| 3 | 422 | Total Income (I+II) | 18,439.32 | 20,492.89 | 11,713.93 | 68,995.30 | — |
| 4 | 424 | Cost of materials consumed | 11,162.31 | 9,136.47 | 8,908.22 | 34,979.78 | — |
| 5 | 425 | Purchase of Stock-in-trade | 3,375.03 | 8,048.00 | blank | 21,165.88 | `ZERO_STANDING` (Q1FY26 blank) |
| 6 | 426-428 | Changes in Inventories of Finished Goods, WIP and Stock-in-Trade | 187.80 | 414.21 | (420.06) | (723.79) | — |
| 7 | 429 | Employee benefit expenses | 446.26 | 376.92 | 532.64 | 1,844.16 | — |
| 8 | 430 | Finance costs | 132.99 | 141.81 | 63.14 | 398.12 | — |
| 9 | 431 | Depreciation and amortisation expense | 71.84 | 73.42 | 93.54 | 341.42 | — |
| 10 | 432 | Other expenses | 558.73 | 431.09 | 440.26 | 1,878.07 | — |
| 11 | 433 | Total expenses (IV) | 15,934.96 | 18,621.92 | 9,617.74 | 59,883.64 | — |
| 12 | 434 | Profit Before Prior Period and Exceptional Item (III-IV) | 2,504.36 | 1,870.97 | 2,096.19 | 9,111.66 | — |
| 13 | 435 | Prior Period Item/Exceptional Item | blank | blank | blank | (39.71) | `ZERO_STANDING`; sign is negative on FY line, opposite sign to consolidated FY (+39.71) — flag `FIGURE_MISMATCH` for A3 |
| 14 | 436 | Profit before tax (V-VI) | 2,504.36 | 1,870.97 | 2,096.19 | 9,151.37 | — |
| 15 | 438 | Current tax | 641.75 | 498.20 | 537.61 | 2,382.39 | — |
| 16 | 439 | Deferred tax Liability/(Assets) | (4.23) | (11.57) | (9.98) | (58.90) | — |
| 17 | 440 | Income Tax (Short/Excess provision) | blank | (302.65) | blank | (302.65) | `ZERO_STANDING`; sign negative vs consolidated positive 302.65 — `FIGURE_MISMATCH` |
| 18 | 441 | Total Tax expenses (VIII) | 637.52 | 183.98 | 527.63 | 2,020.84 | — |
| 19 | 442 | Profit for the period (VII-VIII) | 1,866.84 | 1,686.99 | 1,568.56 | 7,130.53 | — |
| 20 | 445 | Remeasurements of defined benefit plans (OCI) | 15.16 | (1.97) | (11.71) | (19.08) | — |
| 21 | 446 | Income Tax relating to above (OCI) | (3.82) | 0.50 | 2.95 | 4.80 | — |
| 22 | 447-448 | [Duplicate heading] "Items that will be reclassified..." — Remeasurements of defined benefit plans | blank | blank | blank | blank | `ZERO_STANDING` + template artifact |
| 23 | 449 | [Duplicate] Income Tax relating to above | blank | blank | blank | blank | `ZERO_STANDING` + template artifact |
| 24 | 450 | Total Other Comprehensive Income (X) | 11.34 | (1.47) | (8.76) | (14.28) | — |
| 25 | 451 | Total Comprehensive Income for the year (IX-X) | 1,855.50 | 1,688.46 | 1,577.32 | 7,144.81 | — |
| 26 | 452 | Paidup Equity Share Capital (FV Rs 10) | 6,545.85 | 6,215.66 | 6,215.66 | 6,215.66 | — |
| 27 | 453 | Other Equity | blank | blank | blank | 50,452.30 | `ZERO_STANDING` |
| 28 | 456 | EPS Basic/Diluted | 2.95 | 2.71 | 2.52 | 11.47 | — |

No "Net Profit attributable to" / NCI breakdown in standalone (expected — no subsidiaries in a
standalone statement); confirmed absent by sweep, not merely unlisted.

## E. Numbered Notes — Consolidated Financial Statement (page 4, lines 180-243)

| Note | Line(s) | First 15 words | Flags |
|------|---------|-----------------|-------|
| [1] | 180-183 | "The above Unaudited Consolidated financial results for the quarter ended 30th June, 2026 have been prepared" | — |
| [2] | 184 | "Previous Year's / period's figures have been regrouped/rearranged/ restated/adjusted/rectified wherever considered necessary." | — |
| [3] | 186-187 | "Basis of Preparation of the Statement and Adoption of Indian Accounting Standards. The Company has adopted" | — |
| [4] | 189-191 | "The Company manufactures fin and tube type heat exchangers for the Heat Ventilation Air Conditioning" | — |
| [5] | 193-194 | "The Figure for the Quarter ended 31st March, 2026 are balancing figures between the un-audited" | OCR-garbled marker `[SJ` — required widened grep to catch |
| [6] | 196 | "Segment Reporting is attached herewith." | cross-ref to section G below |
| [7] | 198-236 | "The Proceeds From IPO Net Off Issue Expense Is Rs 31,111.66 Lakhs And Utilisation of the same is as follows" | OCR-garbled marker `[71`; contains 2 sub-tables (IPO utilization, QIP utilization) — see section F |
| [8] | 213-236 | "During the quarter, the Company completed a Qualified Institutions Placement (\"QIP\") in accordance with Chapter" | shares line range with note 7's QIP sub-table; note text begins 213, table at 221-236 |
| [9] | 238-243 | "The Status of investor's complaints during the Period ended on 30th June, 2026 as under" | contains 4-row nil table — see section F |

## F. Note Sub-Tables — Consolidated

### F1. Note [7] — IPO proceeds utilization (lines 198-211)
| Line(s) | Particular | Planned/Prospectus | Utilised | Balance | Flags |
|---------|-----------|---------------------|----------|---------|-------|
| 202-206 | Investment in wholly owned subsidiary KRN HVAC Products Pvt Ltd (Proposed Project) | 23,575.66 | 23,575.66 | fully utilised, no unutilised balance (line 210) | — |
| 207 | General corporate purposes | 7,536.00 | 7,536.00 | — | — |
| 208 | Total | 31,111.66 | 31,111.66 | — | — |

### F2. Note [8] — QIP proceeds utilization (lines 221-236)
| Line(s) | Particular | Offer document amount | Utilised during quarter | Total unutilized | Flags |
|---------|-----------|------------------------|---------------------------|--------------------|-------|
| 226-228 | Repayment/pre-payment of outstanding borrowings | 3,000.00 | 3,000.00 | Nil | `ZERO_STANDING` |
| 229-231 | Investment in material subsidiary KRN HVAC Products Pvt Ltd (working capital) | 23,525.75 | 23,525.75 | Nil | `ZERO_STANDING` |
| 232 | General Corporate purposes | 7,653.73 | 7,653.73 | Nil | `ZERO_STANDING` |
| 233 | Total | 34,179.48 | 34,179.48 | Nil | `ZERO_STANDING` |
| 234-236 | Footnote: subsidiary utilised Rs 9,207.98 Lakhs of the Rs 23,525.75 Lakhs invested; Rs 14,317.77 Lakhs unutilized, parked in FDs/Bonds | — | — | — | reported at subsidiary level, not company level |

### F3. Note [9] — Investor complaints (lines 240-243)
| Line | Item | Value | Flags |
|------|------|-------|-------|
| 240 | Complaints pending at beginning of period | Nil | `ZERO_STANDING` |
| 241 | Complaints received during the period | Nil | `ZERO_STANDING` |
| 242 | Complaints disposed during the period | Nil | `ZERO_STANDING` |
| 243 | Complaints unresolved at the end of the period | Nil | `ZERO_STANDING` |

## G. Numbered Notes — Standalone Financial Statement (page 9, lines 472-532)

| Note | Line(s) | First 15 words | Flags |
|------|---------|-----------------|-------|
| [1] | 472-475 | "The above Unaudited standalone financial results for the Quarter ended 30th June, 2026 have been prepared" | closing bracket OCR'd as `)` not `]` |
| [2] | 477 | "Previous Year's /period's figures have been regrouped/rearranged/ restated/adjusted/rectified wherever considered necessary." | — |
| [3] | 479-480 | "Basis of Preparation of the Statement and Adoption of Indian Accounting Standards . The Company has" | — |
| [4] | 482-484 | "The Company manufactures fin and tube type heat exchangers for the Heat Ventilation Air Conditioning" | — |
| [5] | 486-487 | "The Figure for the Quarter ended 31st March, 2026 are balancing figures between the un-audited" | — |
| [6] | 489 | "Segment Reporting is attached herewith." | cross-ref section H |
| [7] | 491-522 | "The Proceeds From IPO Net Off Issue Expense Is Rs 31,111.66 Lakhs And Utilisation of the same" | contains sub-table, see F4 |
| [8] | 504-526 | "During the quarter, the Company completed a Qualified Institutions Placement (\"QIP\") in accordance w ith Chapter" | contains sub-table, see F5 |
| [9] | 528-532 | "The Status of investor's complaints during the Period ended on 30th June, 2026 as under" | contains 4-row nil table, see F6 |

## F (cont). Note Sub-Tables — Standalone

### F4. Note [7] — IPO proceeds utilization (lines 491-502)
| Line(s) | Particular | Planned/Prospectus | Utilised | Balance | Flags |
|---------|-----------|---------------------|----------|---------|-------|
| 495-497 | Investment in wholly owned subsidiary KRN HVAC Products Pvt Ltd | 23,575.66 | 23,575.66 | fully utilised (line 501) | — |
| 498 | General corporate purposes | 7,536.00 | 7,536.00 | — | — |
| 499 | Total | 31,111.66 | 31,111.66 | — | — |

### F5. Note [8] — QIP proceeds utilization (lines 510-526)
| Line(s) | Particular | Offer document amount | Utilised during quarter | Total unutilized | Flags |
|---------|-----------|------------------------|---------------------------|--------------------|-------|
| 515-516 | Repayment/pre-payment of outstanding borrowings | 3,000.00 | 3,000.00 | Nil | `ZERO_STANDING` |
| 518-520 | Investment in material subsidiary KRN HVAC Products Pvt Ltd | 23,525.75 | 23,525.75 | Nil | `ZERO_STANDING` |
| 521 | General Corporate purposes | 7,653.73 | 7,653.73 | Nil | `ZERO_STANDING` |
| 522 | Total | 34,179.48 | 34,179.48 | Nil | `ZERO_STANDING` |
| 524-526 | Footnote: identical subsidiary utilization detail as consolidated F2 | — | — | — | — |

### F6. Note [9] — Investor complaints (lines 529-532)
| Line | Item | Value | Flags |
|------|------|-------|-------|
| 529 | Complaints pending at beginning of period | Nil | `ZERO_STANDING` |
| 530 | Complaints received during the period | Nil | `ZERO_STANDING` |
| 531 | Complaints disposed during the period | Nil | `ZERO_STANDING` |
| 532 | Complaints unresolved at the end of the period | Nil | `ZERO_STANDING` |

## H. Consolidated Segment Reporting (page 5, lines 257-309)

### H1. Segment line items (lines 265-291)
| # | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| 1 | 266 | Segment Revenue — India | 19,994.00 | 15,164.47 | 9,639.41 | 50,060.10 | — |
| 2 | 267 | Segment Revenue — Overseas | 5,237.70 | 2,783.51 | 1,888.80 | 9,945.67 | — |
| 3 | 268 | Total Segment Revenue | 25,231.70 | 17,947.98 | 11,528.21 | 60,005.77 | — |
| 4 | 269 | Inter Segment Sales | blank | blank | blank | blank | `ZERO_STANDING` |
| 5 | 270 | Income From Operations | 25,231.70 | 17,947.98 | 11,528.21 | 60,005.77 | — |
| 6 | 274 | Segment Results — India | 4,537.20 | 2,948.96 | 1,898.45 | 10,345.94 | — |
| 7 | 275 | Segment Results — Overseas | blank | blank | blank | blank | `ZERO_STANDING` (overseas segment result not separately disclosed in any period) |
| 8 | 276 | Segment Results — Total | 4,537.20 | 2,948.96 | 1,898.45 | 10,345.94 | — |
| 9 | 277 | Less: Finance Cost | 304.12 | 264.03 | 69.55 | 590.08 | — |
| 10 | 278 | Profit/(loss) Before Exceptional Items & Tax | 4,233.08 | 2,684.93 | 1,828.90 | 9,755.86 | — |
| 11 | 279 | Exceptional Items | blank | blank | blank | 39.71 | `ZERO_STANDING` (quarters) |
| 12 | 280 | Profit Before Tax | 4,233.08 | 2,684.93 | 1,828.90 | 9,795.57 | — |
| 13 | 284 | Segment Asset — India | blank | blank | blank | 9,486.24 | `ZERO_STANDING` (quarterly not disclosed) |
| 14 | 285 | Segment Asset — Overseas | blank | blank | blank | 8,102.18 | `ZERO_STANDING` |
| 15 | 286 | Total Segment Asset | blank | blank | blank | 17,588.42 | `ZERO_STANDING` |
| 16 | 289 | Segment Liabilities — India | blank | blank | blank | 4,972.02 | `ZERO_STANDING` |
| 17 | 290 | Segment Liabilities — Overseas | blank | blank | blank | 10,851.33 | `ZERO_STANDING` |
| 18 | 291 | Total Segment Liabilities | blank | blank | blank | 15,823.35 | `ZERO_STANDING` |

Footnote line 292: "figures disclosed in segment asset above are gross amount i.e. before ECL provision" — qualifier on rows 13-15.

### H2. Country-wise export revenue, consolidated, upto 30th June 2026 (lines 294-309)
| # | Line | Country | Value (Rs Lakhs) |
|---|------|---------|-------------------|
| 1 | 295 | Brazil | 95.35 |
| 2 | 296 | Canada | 295.29 |
| 3 | 297 | France | 1,037.75 |
| 4 | 298 | Italy | 564.72 |
| 5 | 299 | Nepal | 8.50 |
| 6 | 300 | Netherlands | 8.42 |
| 7 | 301 | Norway | 1.30 |
| 8 | 302 | Sri Lanka | 282.05 |
| 9 | 303 | United Arab Emirates | 594.09 |
| 10 | 304 | United Kingdom | 3.17 |
| 11 | 305 | USA | 1,706.88 |
| 12 | 306 | Vietnam | 639.14 |
| 13 | 307 | Croatia | 1.01 |
| 14 | 308 | Austria | 0.03 |
| — | 309 | Total (= Segment Revenue Overseas, ties to row H1-2) | 5,237.70 |

## I. Standalone Segment Reporting (page 10, lines 542-590)

### I1. Segment line items (lines 551-577)
| # | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| 1 | 552 | Segment Revenue — India | 15,463.64 | 17,614.21 | 9,551.10 | 58,393.61 | — |
| 2 | 553 | Segment Revenue — Overseas | 2,733.51 | 2,591.97 | 1,888.80 | 9,229.40 | — |
| 3 | 554 | Total Segment Revenue | 18,197.15 | 20,206.18 | 11,439.90 | 67,623.01 | — |
| 4 | 555 | Inter Segment Sales | blank | blank | blank | blank | `ZERO_STANDING` |
| 5 | 556 | Income From Operations | 18,197.15 | 20,206.18 | 11,439.90 | 67,623.01 | — |
| 6 | 560 | Segment Results — India | 2,637.35 | 2,012.78 | 2,159.33 | 9,589.20 | — |
| 7 | 561 | Segment Results — Overseas | blank | blank | blank | blank | `ZERO_STANDING` |
| 8 | 562 | Segment Results — Total | 2,637.35 | 2,012.78 | 2,159.33 | 9,589.20 | — |
| 9 | 563 | Less: Finance Cost | 132.99 | 141.81 | 63.14 | 398.12 | — |
| 10 | 564 | Profit/(loss) Before Exceptional Items & Tax | 2,504.36 | 1,870.97 | 2,096.19 | 9,191.08 | — |
| 11 | 565 | Prior Period/Exceptional Item | blank | blank | blank | (39.71) | `ZERO_STANDING`; ties to row D-13 (opposite sign vs consolidated) |
| 12 | 566 | Profit Before Tax | 2,504.36 | 1,870.97 | 2,096.19 | 9,151.37 | — |
| 13 | 570 | Segment Asset — India | blank | blank | blank | 14,155.15 | `ZERO_STANDING` |
| 14 | 571 | Segment Asset — Overseas | blank | blank | blank | 4,839.22 | `ZERO_STANDING` |
| 15 | 572 | Total Segment Asset | blank | blank | blank | 18,994.37 | `ZERO_STANDING` |
| 16 | 575 | Segment Liabilities — India | blank | blank | blank | 1,014.58 | `ZERO_STANDING` |
| 17 | 576 | Segment Liabilities — Overseas | blank | blank | blank | 4,919.50 | `ZERO_STANDING` |
| 18 | 577 | Total Segment Liabilities | blank | blank | blank | 5,934.08 | `ZERO_STANDING` |

Footnote line 578: same "gross amount before ECL provision" qualifier as H1.

Note: row 10 above (Profit/(loss) Before Exceptional Items & Tax = 9,191.08 for FY26) does not equal
row 6 P&L "Profit Before Prior Period and Exceptional Item" FY26 figure (9,111.66, line 434). Flagged
`FIGURE_MISMATCH` for A3/A4 reconciliation — not resolved by A2.

### I2. Country-wise export revenue, standalone, period ended 30th June 2026 (lines 581-590)
| # | Line | Country | Value (Rs Lakhs) |
|---|------|---------|-------------------|
| 1 | 582 | Austria | 0.03 |
| 2 | 583 | Canada | 138.96 |
| 3 | 584 | Croatia | 1.01 |
| 4 | 585 | France | 1,031.23 |
| 5 | 586 | Italy | 340.22 |
| 6 | 587 | Vietnam | 367.98 |
| 7 | 588 | United Arab Emirates | 189.41 |
| 8 | 589 | USA | 664.67 |
| — | 590 | Total (= Segment Revenue Overseas, ties to row I1-2) | 2,733.51 |

Standalone export list (8 countries) is a strict subset of the consolidated list (14 countries) minus
Brazil, Nepal, Netherlands, Norway, Sri Lanka, United Kingdom — i.e. those five/six markets are served
only via the consolidated entity (subsidiary-level exports). Recorded as a data point for A3/A4, not
interpreted further here.

## J. Auditor's Limited Review Report — Consolidated (pages 6-7, lines 311-403)

| # | Line(s) | Paragraph / element | Content summary | Flags |
|---|---------|----------------------|------------------|-------|
| 1 | 320-323 | Report title | "Independent Auditor's Limited Review Report on the Quarterly Unaudited Consolidated Financial Results..." Reg 33 SEBI LODR | — |
| 2 | 326-328 | Addressee | To the Board of Directors of KRN Heat Exchanger and Refrigeration Limited | — |
| 3 | 331-335 | Scope paragraph | Reviewed accompanying Statement of Unaudited Consolidated Financial Results, Parent + subsidiaries ("the Group"), for quarter ended 30 June 2026 | — |
| 4 | 337-342 | Management responsibility statement | Statement is Parent management's responsibility, approved by Board, prepared per Ind AS 34 | — |
| 5 | 344-354 | Review standard / basis paragraph | SRE 2410 review, less in scope than audit, no audit opinion expressed; SEBI Reg 33(8) circular procedures applied | No Emphasis of Matter paragraph present; no Going Concern paragraph present — confirmed absent by sweep |
| 6 | 363-369 | Entity list reviewed | 2 subsidiaries: (1) KRN HVAC Products Private Limited (2) Thermotech Research Laboratory Private Limited | see section K |
| 7 | 370-377 | Conclusion paragraph | "Nothing has come to our attention that causes us to believe..." — unmodified/clean review conclusion | — |
| 8 | 379-388 | Other Matters — reliance on unaudited subsidiary financials | 2 subsidiaries unaudited, furnished by management: total income Rs 16,718.73 Lakhs, PAT Rs 1,422.72 Lakhs, TCI Rs 1,419.39 Lakhs for the quarter, approved/furnished by Management, not independently reviewed by principal auditor | `UNAUDITED_SUBSIDIARY_RELIANCE` — both subsidiaries management-furnished, not auditor-reviewed |
| 9 | 390 | Modification statement | "Our conclusion on the statement is not modified in respect of these matters" | — |
| 10 | 393-403 | Signature block | Keyur Shah & Co., FRN 141173W; Keyur Shah, Proprietor, M.No. 153774, UDIN 26153774EUACWV7849, dated 12 Aug 2026, Ahmedabad | see section B row 2 |

## K. Auditor's Limited Review Report — Standalone (page 11, lines 591-651)

| # | Line(s) | Paragraph / element | Content summary | Flags |
|---|---------|----------------------|------------------|-------|
| 1 | 599-601 | Report title | "Limited Review Report on unaudited standalone financial results..." Reg 33 SEBI LODR | — |
| 2 | 604-606 | Addressee | To the Board of Directors of KRN Heat Exchanger and Refrigeration Limited | — |
| 3 | 608-615 | Scope + responsibility paragraph | Reviewed Standalone financial results, Company management's responsibility, approved by Board, prepared per Section 133 CA 2013 and Reg 33 | — |
| 4 | 617-625 | Review standard / basis paragraph | SRE 2410, moderate assurance, less scope than audit, no audit opinion expressed | No Emphasis of Matter, no Going Concern, no Other Matters paragraph present — confirmed absent by sweep (expected: standalone has no subsidiaries to disclaim reliance on) |
| 5 | 627-633 | Conclusion paragraph | "Nothing has come to our attention..." — unmodified/clean review conclusion | — |
| 6 | 637-647 | Signature block | Keyur Shah & Co., FRN 141173W; Keyur Shah, Proprietor, M.No. 153774, UDIN 26153774LHTHBS5726, dated 12 Aug 2026, Ahmedabad | see section B row 3; same audit firm/partner as consolidated report, different UDIN (correct — distinct engagements) |

Both LRRs: same auditor (Keyur Shah & Co.), same date (12 Aug 2026), same place (Ahmedabad), two
distinct UDINs — no UDIN reuse detected.

## L. Entities in Consolidation (lines 363-369, 382-388)

| # | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| 1 | 367 | KRN HVAC Products Private Limited | Wholly owned subsidiary (per Note 7, line 202-206) | Unaudited, management-furnished (line 379-388) |
| 2 | 368 | Thermotech Research Laboratory Private Limited | Subsidiary | Unaudited, management-furnished (line 379-388) |

`NO_PRIOR_LEDGER` — no prior-quarter ledger supplied; `ENTITY_CHANGE` diff cannot be run this cycle.

## M. Annexure-II — Regulation 30 Disclosures (page 12-13, lines 657-730)

### M1. Appointment of Cost Auditor FY 2026-27 (lines 663-693)
| S.No. | Line(s) | Particular | Disclosure |
|-------|---------|------------|------------|
| 1 | 667-670 | Reason for change | Appointment of M/s. R S Chauhan & Associates, Cost Accountants (FRN: 003517), as Cost Auditor |
| 2 | 671-674 | Date of appointment & term | Appointed 12th August 2026 for FY 2026-27 |
| 3 | 675-687 | Brief profile | Firm in practice 7+ years; industries incl. auto, dairy, textiles, garments, steel/copper/aluminium; services incl. audit & assurance, business advisory, cost records compilation, taxation |
| 4 | 688-691 | Disclosure of relationships between directors | NA (`ZERO_STANDING` — not-applicable standing field, correctly nil since not a director appointment) |

### M2. Appointment of Internal Auditor FY 2026-27 (lines 694-730)
| S.No. | Line(s) | Particular | Disclosure |
|-------|---------|------------|------------|
| 1 | 699-702 | Reason for change | Appointment of M/s. Sharma Shankar & Co., Chartered Accountants (FRN: 019317C), as Internal Auditor |
| 2 | 703-706/716 | Date of appointment & term | Appointed 12th August 2026 for FY 2026-27 (row split across page break, lines 703-706 then continuation at 716) |
| 3 | 717-726 | Brief profile | Firm in practice 12+ years; wide advisory range: Accounting & Assurance, Taxation; best practices/technology adoption |
| 4 | 727-730 | Disclosure of relationships between directors | NA (`ZERO_STANDING`) |

Cross-check: Annexure-II items M1/M2 correspond 1:1 to Board Outcome agenda items A-2 and A-3 —
consistent, no discrepancy in appointee names, FRNs, or effective dates between the letter and the
annexure.

---

## Flags raised (roll-up)

- `ZERO_STANDING` — 51 instances: P&L (consolidated 9, standalone 6), segment reporting
  (consolidated 9, standalone 9), note sub-tables (investor complaints 4+4, QIP unutilized-balance
  rows incl. Total 4+4), Annexure-II "disclosure of relationships" NA fields (1+1).
- `FIGURE_MISMATCH` — 4 instances flagged for A3/A4, not resolved by A2: (i) consolidated Net Profit
  attributable to Owner (3,289.56, line 150) vs Profit for the period (3,269.56, line 139); (ii)
  standalone Prior Period Item sign flip vs consolidated FY figure; (iii) standalone Income Tax
  Short/Excess provision sign flip vs consolidated; (iv) standalone segment "Profit Before Exceptional
  Items & Tax" FY26 figure (9,191.08) vs standalone P&L FY26 figure for the equivalent line (9,111.66).
- `UNAUDITED_SUBSIDIARY_RELIANCE` — both consolidated subsidiaries' quarterly financials are
  unaudited/management-furnished per the LRR Other Matters paragraph.
- `INCOMPLETE_SIGNATURE` — 2 unnamed "For and on behalf of Board of Directors" blocks on the P&L
  statement pages (no extractable signatory name).
- `HEADER_MISCOUNT` — A1 header states 708 lines; file as delivered runs to line 735.
- `NO_PRIOR_LEDGER` — entity-change and dropped-disclosure diffs against the prior quarter could not
  be run this cycle; A1 was not supplied a prior-quarter ledger path.

No `DROPPED_SLIDE`, `MGMT_ABSENCE`, `REPEAT_QUESTION` — not applicable to this doctype (results
filing, not a transcript or presentation).

```yaml
stage: A2-enumerator
company: "KRN"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "runs/krn-q1fy27/work/ledger_results_krn_q1fy27.md"
counts:
  notes: 18
  line_items: 63
  zero_standing: 51
  agenda_items: 3
  auditor_paras: 16
  entities: 2
flags_raised: [ZERO_STANDING, FIGURE_MISMATCH, UNAUDITED_SUBSIDIARY_RELIANCE, INCOMPLETE_SIGNATURE, HEADER_MISCOUNT, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
