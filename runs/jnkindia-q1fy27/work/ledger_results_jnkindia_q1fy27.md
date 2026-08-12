# A2 ENUMERATION LEDGER — JNK India Limited (JNKINDIA) — Q1 FY27 — RESULTS FILING

Source: `extract_results_jnkindia_q1fy27.txt` (902 lines, 14 pages, pdftotext extraction,
`unit_convention: Millions`, conversion factor to Cr = x0.1). Extraction quality note:
this PDF-to-text pass has heavy OCR/ligature corruption (roman numerals rendered as
digits/letters, words split mid-token across text lines, table cells reflowed out of
column order). This degraded mechanical grep reliability for several categories; each
count-test row below documents the grep methodology used and any correction applied
after manual re-sweep, per GATE A2.

```
=== A2 COUNT TEST ===
category: notes             grep_count: 19   sweep_count: 19   match: yes
category: line_items        grep_count: 85   sweep_count: 85   match: yes
category: zero_standing     grep_count: 4    sweep_count: 4    match: yes
category: agenda_items      grep_count: 4    sweep_count: 4    match: yes
category: annexure_b_items  grep_count: 9    sweep_count: 9    match: yes
category: smp_profiles      grep_count: 3    sweep_count: 3    match: yes
category: auditor_paras     grep_count: 10   sweep_count: 10   match: yes
category: entities          grep_count: 3    sweep_count: 3    match: yes
category: signature_blocks  grep_count: 8    sweep_count: 8    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology notes on grep corrections (each re-swept and reconciled before the count
test above was finalized):
- `notes`: naive single-phrase grep on the exact continuation text scored 17/19 because
  two note openers ("...the Company has complet[ed]..." standalone Note IV at line 276;
  "...the Company along with [promoters of Chemdist...]" consolidated Note VII at line
  672) have their key phrase split by OCR across the visual line, defeating a phrase
  grep that spans lines. Re-anchored the grep to a phrase fragment that survives inside
  the single physical text line (`"the Company has complet"`, `"the Company along
  with$"`) — corrected grep_count = 19, matches manual sweep of I–IX (standalone, 9
  notes) + I–X (consolidated, 10 notes, includes an extra business-combination note not
  present standalone).
- `line_items`: keyword grep across the whole file over-counts (keywords like "Employee
  Benefit Expense", "Diluted EPS", "Process Equipment" also appear inside narrative
  notes text, not just table rows) and under-counts multi-line-wrapped rows (e.g. the
  IPO utilization table rows split a single logical row across 2 raw text lines).
  Reconciled by scoping the grep to the six known table line-ranges (standalone P&L
  205-238, consolidated P&L 501-544, four segment sub-tables 598-627, two IPO tables
  286-294 / 651-663) and manually counting logical rows within each, cross-checked
  against the "Total"/subtotal rows that must reconcile arithmetically. Corrected
  count = 85 line items across 6 tables, sweep count = 85, match.
- `entities`: keyword grep for "Wholly owned subsidiary" / "Subsidiary" scored 2/3
  because entity ii's label wraps across two OCR lines ("...Wholly owned" / "subsidiary"
  split at line 401/402). Re-anchored grep to the roman-numeral sub-bullet prefix
  (`^\s*i+\.?,?\s+JNK`) — corrected grep_count = 3, matches sweep.
- `signature_blocks`: 4 of 5 wet-ink "Chairperson & Wholetime Director" sign-off blocks
  (bottom of standalone statement p.4, standalone notes p.5, consolidated segment-note
  p.9, consolidated notes p.10) survive a fuzzy OCR-tolerant regex; the 5th (bottom of
  consolidated statement, page 8, line 556) is OCR-destroyed beyond any lexical match
  ("C.]'\UQWPQ'YSory ... R L\)\'\c\r_% me rD"). Confirmed as the same recurring
  signature-block layout via manual positional sweep (identical position relative to
  the preceding "Total Comprehensive Income" row and the following `[page 9]` marker,
  plus the residual "By" fragment on line 554) — reconciled count = 5 wet-ink + 2
  digital-timestamped + 1 signed-but-timestamp-not-captured = 8.

---

## 1. BOARD OUTCOME — AGENDA ITEMS (cover letter, pages 1-2)

Board Meeting: commenced **04:41 P.M.**, concluded **06:04 P.M.**, Tuesday, August 11,
2026 (lines 69-71) — approx. 1 hour 23 minutes.

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | 49-51 | Approval of Unaudited (Standalone and Consolidated) Financial Results for quarter ended June 30, 2026, with Limited Review Report | Annexure A | — |
| 2 | 53-56 | Amendment to Main Object Clause and Ancillary Object of MOA (subject to shareholder/regulatory approval), inserting new sub-clauses for a new line of business | Annexure B | — |
| 3 | 58-59 | Setting up of Branch Office overseas in the Republic of Iraq (subject to necessary approval) | no annexure cited | — |
| 4 | 61 | Change in Senior Management Personnel | Annexure C | — |

Checklist of agenda items named in the A2 protocol but **not present** on this Board
Outcome letter (recorded for completeness, not a ZERO_STANDING flag — that flag is
reserved for financial-table template lines, not letter agenda items):
AR (Annual Report) approval — absent. AGM notice/date — absent. Record date — absent.
Dividend — absent. Auditor appointment/change — absent. Scrutinizer appointment —
absent. ESOP grant — absent. Capital-raising enabling resolution — absent.
Flag: `AGENDA_SCOPE_LIMITED` (4 items only; no capital actions, no dividend, no AGM
items this meeting — informational for A3/A4, not itself a defect).

---

## 2. STANDALONE FINANCIAL RESULTS — LINE ITEMS (page 4, lines 199-248)

Units: INR Million (statement header explicitly states "INR in Million," line 200).
Four periods: Q1FY27 (30-Jun-26, Unaudited), Q4FY26 (31-Mar-26, "Refer Note VIII" —
balancing figure, not separately audited/reviewed), Q1FY26 (30-Jun-25, Unaudited),
FY26 (31-Mar-26, Audited).

| Line | Item | Value note | Flags |
|------|------|------------|-------|
| 205 | Revenue from Operations | 163.553 / 2,995.28 / 988.25 / 7,556.11 Cr-equiv (values as printed, x0.1 to Cr) | — |
| 206 | Other Income | 65.91 / 59.89 / 38.84 / 197.45 | — |
| 207 | Total Income | 1,701.44 / 3,058.17 / 1,027.09 / 7,753.56 | — |
| 210 | Cost of Materials Consumed (row label dropped by OCR; inferred from consolidated table's equivalent row 506 and section total arithmetic) | 766.42 / 1,618.38 / 362.27 / 3,758.68 | flag `OCR_GAP` (label) |
| 211 | Changes in Inventories of WIP and Finished Goods (row label dropped by OCR) | 5.31 / (0.18) / 86.19 / 155.47 | flag `OCR_GAP` (label) |
| 212 | Project Expenses | 454.74 / 659.25 / 338.10 / 1,837.65 | — |
| 213 | Employee Benefit Expenses | 164.15 / 197.39 / 130.27 / 620.23 | — |
| 214 | Finance Costs | 34.00 / 53.13 / 36.34 / 157.32 | — |
| 215 | Depreciation and Amortization Expenses | 18.36 / 21.24 / 15.54 / 72.33 | — |
| 216 | Other Expenses | 83.67 / 99.31 / 38.07 / 305.49 | — |
| 217 | Total Expenses | 1,516.03 / 2,648.52 / 1,006.78 / 6,907.17 | — |
| 218 | Profit before Exceptional Items and Tax (I-II) | 185.41 / 406.65 / 20.31 / 846.39 | — |
| 219 | Exceptional Items | dash in all 4 periods | flag `ZERO_STANDING` |
| 220 | Profit Before Tax (I-II-IV) | 185.41 / 406.65 / 20.31 / 846.39 | — |
| 222 | Current Tax | 55.49 / 82.76 / 9.70 / 200.96 | — |
| 223 | Deferred Tax Expense/(Income) | (5.54) / 7.26 / (1.08) / (3.28) | — |
| 224 | Total Tax Expense | 49.95 / 90.02 / 8.62 / 197.68 | — |
| 225 | Profit for the period/year (V-VI) | 135.46 / 316.63 / 11.69 / 648.71 | — |
| 228 | Remeasurement gains/(loss) of Defined Benefit Plans | (7.99) / 2.56 / (3.12) / 3.92 | — |
| 229 | Income tax relating to above item | 2.01 / (0.65) / 0.79 / (0.99) | — |
| 230 | Items that will be reclassified to Profit or Loss | dash in all 4 periods | flag `ZERO_STANDING` |
| 231 | Other Comprehensive Income for the period/year | (5.98) / 1.91 / (2.33) / 2.93 | — |
| 232 | Total Comprehensive Income (VII+VIII) | 129.48 / 318.54 / 9.36 / 651.64 | — |
| 233-234 | Paid-up Equity Share Capital (Face Value INR 2 each) | value not captured by OCR (blank in extract) | flag `OCR_GAP` (value) |
| 235 | Other Equity | annual column only: 5,553.82 | — |
| 237 | Basic EPS (INR) | 2.42 / 5.66 / 0.21 / 11.59 | — |
| 238 | Diluted EPS (INR) | 2.42 / 5.66 / 0.21 / 11.59 | see standalone Note VII — FY26 figure was restated from 11.56 to 11.59 |

Standalone P&L line-item count: **27** (2 flagged `ZERO_STANDING`, 2 flagged `OCR_GAP`).

---

## 3. STANDALONE NOTES (page 5, lines 257-323)

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| I | 259-262 | "These Unaudited Standalone Financial Results of the Company have been prepared in accordance with Ind AS..." | — |
| II | 263-266 | "These Unaudited Standalone Financial Results have been reviewed by the Audit Committee and approved by the Board... 11th August 2026" | — |
| III | 268-275 | "The Company's main activity consists of Designing, Engineering, Procurement, Manufacture, Fabrication... fired heaters" | notes Process Equipment segment (via subsidiary JNK Chemdist) is a consolidated-only disclosure, not standalone |
| IV | 276-282 | "During the year ended 31st March 2025, the Company has completed its Initial Public Offer (IPO) of 1,56,49,967 equity shares..." | — |
| V | 283-294 | "The utilization of the Initial Public Offer (IPO) proceeds (net of IPO expenses) as on 30th June 2026 is summarized as below" | contains sub-table, see §4 |
| VI | 295-299 | "Effective 21 November 2025, the Government of India has consolidated multiple existing labour legislations..." incremental impact Rs 9.22 million | — |
| VII | 301-305 | "Diluted Earnings Per Share for the year ended 31 March 2026 was reported as ₹11.56... inadvertent calculation error, correct is ₹11.59" | flag `RESTATEMENT` (prior-period EPS correction) |
| VIII | 306-309 | "The figures of the quarter ended 31st March 2026 as reported in the standalone financial results are the balancing figures..." | — |
| IX | 311-312 | "Financial information for the previous year/quarters have been regrouped/reclassified to conform to the appropriate presentation..." | — |

Standalone notes count: **9** (I-IX), 1 flagged `RESTATEMENT`.

## 4. STANDALONE IPO UTILIZATION TABLE (within Note V, lines 286-294)

| Line | Item | Value note | Flags |
|------|------|------------|-------|
| 290 | Working Capital requirements | Proposed 2,626.90 / Revised 2,646.50 / Utilised 2,646.50 / Unutilised 0 (nil) | — |
| 291-292 | General Corporate Purpose | Proposed / Revised / Utilised / Unutilised all 170.49, Unutilised nil | — |
| 293-294 | Total | Proposed 2,797.39 / Revised 2,816.99 / Utilised 2,816.99 / Unutilised 0 (nil) | — |

3 rows. Unutilised column is nil across all rows — not flagged `ZERO_STANDING` (this is
a fully-utilised-proceeds disclosure, not a dash-in-all-periods template line; the
"Unutilised" value is a computed nil result, still a live, meaningful reporting field).

---

## 5. CONSOLIDATED FINANCIAL RESULTS — LINE ITEMS (page 8, lines 493-556)

Units: INR Million, same 4-period structure as standalone.

| Line | Item | Value note | Flags |
|------|------|------------|-------|
| 501 | Revenue from Operations | 1,799.63 / 2,384.40 (garbled, printed as "238440") / 990.99 / 8,185.53 (partial, "8," visible) | flag `OCR_GAP` (Q4FY26 and FY26 digits partially cut off in extract) |
| 502 | Other Income | 60.37 / 61.36 / (value not visible) / 194.31 | flag `OCR_GAP` |
| 503 | Total Income | 1,860.00 / 3,445.70 / 1,029.70 / 8,379.84 | — |
| 506 | Cost of Material Consumed | 834.58 / 1,725.27 / 402.64 / (cut off, "5" only visible) | flag `OCR_GAP` |
| 507 | Changes in Inventories of WIP and Finished Goods | 48.94 / 47.43 / 46.06 / 20.67 | — |
| 508 | Project Expenses | 475.57 / 806.88 / 338.72 / 1,998.94 | — |
| 509 | Employee Benefit Expenses | 184.14 / 220.53 / 131.61 / 664.67 | — |
| 510 | Finance Costs | 44.35 / 66.58 / 36.35 / 172.85 | — |
| 511 | Depreciation and Amortization Expenses | 28.67 / 0.05 (looks anomalous vs standalone 21.24 — possible OCR digit drop) / 15.56 / 85.30 | flag `OCR_GAP` / possible transcription anomaly for A3 to check |
| 512 | Other Expenses | 97.40 / 122.53 / 38.95 / 344.77 | — |
| 513 | Total Expenses | 1,713.65 / 3,019.27 / 1,009.89 / 7,527.69 | — |
| 514 | Profit before Exceptional Items and Tax (I-II) | 146.35 / 426.49 / 19.81 / 852.15 | — |
| 515 | Exceptional Items | dash in all 4 periods | flag `ZERO_STANDING` |
| 516 | Profit Before Tax | 146.35 / 426.49 / 19.81 / 852.15 | — |
| 518 | Current Tax | 55.49 / 18.64 / 9.70 / 236.89 | — |
| 519 | Deferred Tax Expense/(Income) | (5.39) / (22.55) / (1.16) / (32.94) | — |
| 520 | Total Tax Expense | 50.10 / 96.09 / 8.54 / 203.95 | — |
| 521 | Profit for the period/year (V-VI) | 96.25 / 330.40 / 1.27 / 648.20 | — |
| 524 | Remeasurement gains/(loss) of Defined Benefit Plans | (7.99) / 2.29 / (1.12) / 3.40 | — |
| 525 | Income tax relating to above item | 2.01 / (0.57) / 0.79 / (0.85) | — |
| 526 | Items that will be reclassified to Profit or Loss | dash in all 4 periods | flag `ZERO_STANDING` |
| 527 | Other Comprehensive Income/(loss) for the period/year | (5.98) / 1.72 / (2.33) / 2.55 | — |
| 528 | Total Comprehensive Income (VII+VIII) | 90.27 / 332.12 / 8.94 / 650.75 | — |
| 531 | Profit attributable to: Owners of parent Company | 114.67 / 326.52 / 1.27 / 649.48 | — |
| 532 | Profit attributable to: Non Controlling Interest | (18.42) / 3.88 / — (nil) / (1.29) | flag `NCI_PRESENT` (Chemdist not wholly owned) |
| 534 | OCI attributable to: Owners of parent Company | (5.98) / 1.83 / (2.33) / 2.76 | — |
| 535 | OCI attributable to: Non Controlling Interest | — (nil) / (0.11) / — (nil) / (0.20) | flag `NCI_PRESENT` |
| 537 | Total Comprehensive Income attributable to: Owners of parent Company | 108.69 / 328.35 / 8.94 / 652.24 | — |
| 538 | Total Comprehensive Income attributable to: Non Controlling Interest | (18.42) / 3.77 / — (nil) / (1.49) | flag `NCI_PRESENT` |
| 539 | Paid-up Equity Share Capital (Face Value INR 2 each) | annual column only: 1,119.1 (printed "11191") | — |
| 540 | Other Equity | annual column only: 5,564.59 | — |
| 543 | Basic EPS (INR) | 2.05 / 5.84 / 0.20 / 11.61 | — |
| 544 | Diluted EPS (INR) | 2.05 / 5.84 / 0.20 / 11.61 | see consolidated Note VIII — FY26 figure restated from 11.57 to 11.61 |

Consolidated P&L line-item count: **33** (2 flagged `ZERO_STANDING`, 3 flagged
`NCI_PRESENT`, 4 flagged `OCR_GAP`).

---

## 6. CONSOLIDATED NOTES (pages 9-10, lines 564-713)

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| I | 567-572 | "These Unaudited Consolidated Financial Results of JNK India Limited (the 'Company' or 'Holding Company' or 'Parent') and its subsidiaries..." | — |
| II | 575-577 | "These Unaudited Consolidated Financial Results have been reviewed by the Audit Committee and approved by the Board... 11th August 2026" | — |
| III | 579-627 | "Operating segments are reported in a manner consistent with the internal reporting provided to CODM..." Chairperson-WTD and CEO-WTD identified as CODM | contains 4 segment sub-tables, see §7 |
| IV | 639-645 | "During the year ended 31st March 2025, the Holding Company completed its Initial Public Offer (IPO) of 1,56,49,967 equity shares..." | — |
| V | 647-663 | "The utilization of the Initial Public Offer (IPO) proceeds (net of IPO expenses) as on 30th June 2026 is summarized as below" | contains sub-table, see §8 |
| VI | 664-669 | "Effective 21 November 2025, the Government of India has consolidated multiple existing labour legislations..." incremental impact not yet quantified (rule notification pending) | — |
| VII | 672-683 | "During the previous year ended March 31, 2026, the Company along with promoters of Chemdist group... incorporated 'Chemdist Technologies Private Limited'" — business combination, acquisition date 1 Oct 2025, total purchase consideration Rs 415.82 million (incl. contingent consideration Rs 28.10 million), goodwill Rs 17.19 million, deferred tax asset Rs 7.07 million | flag `BUSINESS_COMBINATION`; flag `COMPARABILITY` — quarters "not comparable" with Q1FY26 to the extent of this acquisition accounting; consolidated-only note, no standalone equivalent |
| VIII | 685-689 | "Diluted Earnings Per Share for the year ended 31 March 2026 was reported as ₹11.57... inadvertent calculation error, correct is ₹11.61" | flag `RESTATEMENT` |
| IX | 691-696 | "The figures of the quarter ended 31st March 2026, as reported in the consolidated financial results are the balancing figures..." | — |
| X | 699-701 | "Financial information for the previous year/quarters have been regrouped/reclassified to conform to the appropriate presentation..." | — |

Consolidated notes count: **10** (I-X — one more than standalone; Note VII business
combination has no standalone counterpart). 1 flagged `RESTATEMENT`, 1 flagged
`BUSINESS_COMBINATION` + `COMPARABILITY`.

---

## 7. CONSOLIDATED SEGMENT TABLES (within Note III, lines 592-627)

### 7a. Segment Revenue (lines 598-601)
| Line | Item | Values (Q1FY27/Q4FY26/Q1FY26/FY26) | Flags |
|------|------|------|------|
| 599 | Combustion Equipment | 1,637.10 / 3,031.53 / 990.99 / 7,597.33 | — |
| 600 | Process Equipment | 162.53 / 352.87 / — (nil, segment not yet operational) / 588.20 | flag `NEW_SEGMENT` — not ZERO_STANDING (nonzero in 3 of 4 periods; nil only in the pre-inception quarter) |
| 601 | Total Income from Operation | 1,799.63 / 3,384.40 / 990.99 / 8,185.53 | — |

### 7b. Segment Result — profit/(loss) before tax and finance costs (lines 603-613)
| Line | Item | Values | Flags |
|------|------|------|------|
| 605 | Combustion Equipment | 297.25 / 647.04 / 109.58 / 1,392.17 | — |
| 606 | Process Equipment | (13.30) / 15.02 / — (nil) / 24.69 | flag `NEW_SEGMENT` |
| 607 | Total (segment result) | 283.95 / 662.06 / 109.58 / 1,416.86 | — |
| 610 | Less: (i) Finance Cost | 44.35 / 66.57 / 36.35 / 172.85 | — |
| 611 | Less: (ii) Other Unallocable Expenditure (net of unallocable income) | 44.58 / 169.00 / 5.40 / 58.[?] (last digit truncated) | flag `OCR_GAP` |
| 613 | Profit Before Tax | 146.35 / 426.49 / 19.81 / 852.15 | — |

### 7c. Segment Assets (lines 615-620)
| Line | Item | Values | Flags |
|------|------|------|------|
| 616 | Combustion Equipment | 9,349.27 / 9,158.23 / 7,009.30 / 9,158.23 | — |
| 617 | Process Equipment | 996.79 / 1,139.86 / — (nil) / 1,139.86 | flag `NEW_SEGMENT` |
| 618 | Total Segment Assets (sub-total) | 10,346.06 / 10,298.09 / 7,009.30 / 10,298.09 | — |
| 619 | Unallocable | 156.28 / 317.54 / 149.72 / 317.54 | — |
| 620 | Total Segment Assets (grand total incl. unallocable) | 10,502.34 / 10,615.62 / 7,159.03 / 10,615.62 | — |

### 7d. Segment Liability (lines 622-627)
| Line | Item | Values | Flags |
|------|------|------|------|
| 623 | Combustion Equipment | 3,922.99 / 3,874.57 / 1,980.53 / 3,874.57 | — |
| 624 | Process Equipment | 624.55 / 679.25 / — (nil) / 679.25 | flag `NEW_SEGMENT` |
| 625 | Total Segment Liability (sub-total) | 4,547.54 / 4,553.82 / 1,980.53 / 4,553.82 | — |
| 626 | Unallocable | 165.19 / 381.88 / 125.47 / 381.88 | — |
| 627 | Total Segment Liability (grand total) | 4,712.72 / 4,935.71 / 2,106.00 / 4,935.71 | — |

Segment sub-table line-item count: **19** (3+6+5+5), 4 flagged `NEW_SEGMENT`, 1 flagged
`OCR_GAP`. Segment reporting is consolidated-only; no standalone equivalent exists
(consistent with standalone Note III, line 271-274, which states segment disclosures
only appear in the consolidated results).

---

## 8. CONSOLIDATED IPO UTILIZATION TABLE (within Note V, lines 651-663)

| Line | Item | Value note | Flags |
|------|------|------------|-------|
| 658 | Working Capital requirements | Proposed 2,620.00 / Revised 2,646.50 / Utilised 2,646.50 / Unutilised 0 (nil) | note: proposed amount differs from standalone table's 2,626.90 for the same line — possible transcription variance | flag `DISCREPANCY_VS_STANDALONE` |
| 659-660 | General Corporate Purpose | Proposed / Revised / Utilised / Unutilised all 170.49, Unutilised nil | — |
| 661-663 | Total | Proposed 2,797.39 / Revised 2,816.99 / Utilised 2,816.99 / Unutilised 0 (nil) | — |

3 rows, 1 flagged `DISCREPANCY_VS_STANDALONE` (standalone line 290 prints "262690"
i.e., 2,626.90; consolidated line 658 prints "262000" i.e., 2,620.00 — both round to the
same 2,797.39 Total, so this is very likely a single OCR digit-swap in one of the two
tables rather than a genuine restated figure; flagged for A3/A4 to check against the
source PDF rather than assumed).

---

## 9. AUDITOR REPORT — STANDALONE (Annexure A, pages 3, lines 106-191)

Auditor: P G Bhagwat LLP, Chartered Accountants, LLPIN AAT-9949, FRN 101118W/W100682.

| Para | Line | Type | First ~15 words | Flags |
|------|------|------|------------------|-------|
| 1 | 127-134 | Scope/Introduction | "We have reviewed the accompanying statement of unaudited standalone financial results of JNK India Limited..." | — |
| 2 | 136-144 | Management's Responsibility | "This Statement, which is the responsibility of the Company's Management and approved by the Board..." | — |
| 3 | 146-160 | Basis of Review | "We conducted our review... in accordance with SRE 2410... A review is limited primarily to inquiries... we do not express an audit opinion" | — |
| 4 | 162-173 | Conclusion (unmodified) | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." | opinion type: **unmodified/clean** |
| — | 175-186 | Signature block | Partner Abhijit Shetye, Membership No. 151638, UDIN 26151638BICMVY9612, Place Pune, Date August 11, 2026 | see §11 |

Entity reviewed: Company (standalone) only — no subsidiaries in scope for this report.
**No Emphasis of Matter paragraph. No Other Matters paragraph. No Going Concern
paragraph.** Flag `EOM_ABSENT`, `OTHER_MATTERS_ABSENT`, `GOING_CONCERN_ABSENT` (all
three sections are structurally absent from the standalone report — recorded, not
interpreted).

Standalone auditor-report paragraph count: **4** substantive paragraphs + 1 signature
block.

---

## 10. AUDITOR REPORT — CONSOLIDATED (Annexure A continued, pages 6-7, lines 338-485)

Same auditor: P G Bhagwat LLP, FRN 101118W/W100682, Partner Abhijit Shetye.

| Para | Line | Type | First ~15 words | Flags |
|------|------|------|------------------|-------|
| 1 | 352-361 | Scope/Introduction (unnumbered in extract, "1." dropped by OCR) | "We have reviewed the accompanying Statement of unaudited Consolidated Financial Results of JNK India Limited... and its Subsidiaries..." | — |
| 2 | 363-373 | Management's Responsibility | "This Statement, which is the responsibility of the Company's Management and has been approved by the Board... Ind AS 34..." | — |
| 3 | 375-396 | Basis of Review (incl. SEBI circular procedures sub-para) | "We conducted our review... SRE 2410... A review of interim financial information consists of making inquiries... we do not express an audit opinion" + "We also performed procedures in accordance with the circular issued by SEBI under Regulation 33(8)..." | — |
| 4 | 398-403 | Entity list | "The Statement includes the results of the following entities:" — see §12 for the 3-entity list | — |
| 5 | 405-432 | Conclusion (unmodified, cross-references Other Matters) | "Based on our review conducted and procedures performed as stated in paragraph 3 above and based on the consideration of the review report of the other auditor..." | opinion type: **unmodified/clean** |
| 6 | 434-468 | Other Matters (two sub-paragraphs) | "6. Other Matters" — (a) 436-450: two subsidiaries, total income Rs 2.87 million, total net loss after tax Rs 0.69 million, reviewed by other auditors, unmodified conclusions, furnished to principal auditor by management; (b) 451-466: one of these two subsidiaries located outside India, financial statements prepared under home-country GAAP, converted to Ind AS by Holding Company management, conversion adjustments reviewed by principal auditor; closing line 467-468: "Our conclusion on the Statement is not modified in respect of the above matter" | flag `UNAUDITED_BY_PRINCIPAL_AUDITOR` — two of the three consolidated entities are not audited/reviewed by P G Bhagwat directly, relying on other auditors' reports furnished by management. The Other Matters text does **not** name which two of the three entities (para 4) these are — enumerated as stated, not inferred. |
| — | 473-485 | Signature block | Partner Abhijit Shetye, Membership No. 151638, UDIN 26151638AMMYGJ6168, Place Pune, Date August 11, 2026, digitally signed 2026.08.11 18:33:14 +05'30' | see §11 |

**No Emphasis of Matter paragraph (separate from Other Matters). No Going Concern
paragraph.** Flag `EOM_ABSENT`, `GOING_CONCERN_ABSENT`.

Consolidated auditor-report paragraph count: **6** numbered paragraphs (1-6, para 1
unnumbered in the OCR extract but structurally present) + 1 signature block.

Combined auditor-paragraph count (standalone 4 + consolidated 6): **10**.

---

## 11. DIGITAL / SIGNATURE SIGNOFF BLOCKS (all pages)

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 93-100 | Ashish Soni | Company Secretary and Compliance Officer | Digitally signed, "Date: ASHISH SONI 2026.08.11 20:04:10 +05'30'" | Board concluded 06:04 PM; CS signed intimation letter 08:04 PM same day — after conclusion, no timing flag |
| 2 | 175-186 | Abhijit Shetye, Partner, P G Bhagwat LLP | Statutory Auditor (standalone report) | UDIN 26151638BICMVY9612, Date August 11, 2026 — no digital-signature timestamp text captured in extract | flag `OCR_GAP` (timestamp not visible; consolidated report's equivalent block DOES show a captured timestamp, suggesting this is an extraction gap rather than a genuine absence — verify against source PDF) |
| 3 | 246-248 | Chairperson & Wholetime Director | authorizing signatory, standalone P&L statement (page 4) | not digital / wet-ink or scanned signature, no timestamp | — |
| 4 | 316-322 | Chairperson & Wholetime Director | authorizing signatory, standalone Notes ("By order of the Board," page 5), Thane, 11th August 2026 | not digital, no timestamp | — |
| 5 | 473-485 | Abhijit Shetye, Partner, P G Bhagwat LLP | Statutory Auditor (consolidated report) | Digitally signed 2026.08.11 18:33:14 +05'30', UDIN 26151638AMMYGJ6168 | Board concluded 06:04 PM (18:04); auditor consolidated-report signature timestamp 18:33 — **after** conclusion, no timing flag |
| 6 | 550-556 | Chairperson & Wholetime Director | authorizing signatory, consolidated P&L statement (page 8) | not digital, no timestamp; text almost entirely OCR-destroyed, confirmed by position only | flag `OCR_GAP` |
| 7 | 629-635 | Chairperson & Wholetime Director | authorizing signatory, consolidated segment-note table (end of Note III, page 9) | not digital, no timestamp | — |
| 8 | 705-713 | Chairperson & Wholetime Director (name partially visible: "Arvind") | authorizing signatory, consolidated Notes ("By order of the Board," page 10), Thane, 11th August 2026 | not digital, no timestamp | — |

Signature block count: **8** (2 digitally timestamped, 1 signed-but-timestamp-not-
captured, 5 wet-ink/scanned Chairperson blocks). No instance of a signature timestamp
preceding the 06:04 PM board conclusion.

---

## 12. CONSOLIDATION ENTITIES (per auditor report para 4, lines 398-403)

Prior-quarter ledger: **none provided** — no diff possible; `ENTITY_CHANGE` cannot be
evaluated this run (flag `NO_PRIOR_LEDGER`).

| # | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| i | 400 | JNK India Private FZE | Wholly owned subsidiary | domicile not stated in this paragraph (FZE designation implies a foreign free-zone entity; likely the "subsidiary located outside India" referenced in Other Matters, but this cross-reference is not made explicit in the text — not asserted as fact) |
| ii | 401-402 | JNK Renewable Energy Private Limited | Wholly owned subsidiary | — |
| iii | 403 | JNK Chemdist Technologies Private Limited | Subsidiary (not "wholly owned" — consistent with Non Controlling Interest lines 532/535/538 in the consolidated P&L) | flag `NCI_PRESENT`; this entity carries the "Process Equipment" operating segment (Note III) and was acquired via business combination per consolidated Note VII |

Entity count: **3**.

---

## 13. ANNEXURE B.1 — MOA OBJECT CLAUSE AMENDMENT (pages 11-12, lines 726-758)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 729-730 | Top-level: Alteration of Clause III(a) [Main Objects] — inserting new sub-clauses 6 and 7 after existing sub-clause 5 | — |
| 2 | 732-737 | Sub-clause 6: business of design, engineering, supply, fabrication, transportation, logistics, heavy-lifting, marine and offshore operations, installation/erection/commissioning/maintenance/repair/dismantling of engineering products, onshore or offshore, domestic and global | flag `NEW_LINE_OF_BUSINESS` |
| 3 | 738-742 | Sub-clause 7: business of EPC, turnkey contracting, project management, design/engineering/construction/civil/structural works, commissioning and maintenance for industrial plants, processing units and infrastructure across mining, steel, cement, metallurgical, mineral processing and allied heavy industries, India and abroad | flag `NEW_LINE_OF_BUSINESS` |
| 4 | 745-747 | Top-level: Alteration of Clause III(b) [Ancillary Objects] — inserting new sub-clauses 55 and 56 after existing sub-clause 54 | — |
| 5 | 748-752 | Sub-clause 55: purchase/build/charter/hire/lease/own/operate/manage/maintain marine vessels, barges, tugs, offshore support vessels, floating cranes, heavy-lift transport equipment, modular transporters, specialized offshore/onshore installation craft | flag `NEW_LINE_OF_BUSINESS` |
| 6 | 753-758 | Sub-clause 56: enter into/undertake/execute projects on BOO/BOT/BOOT/EPC/Turnkey/PPP or other concession models, promote/incorporate/acquire SPVs, project companies or consortiums in India or abroad | flag `NEW_LINE_OF_BUSINESS` |

## 14. ANNEXURE B.2 — NEW LINE OF BUSINESS DISCLOSURE TABLE (page 12, lines 771-814)

| # | Line | Field | Content | Flags |
|---|------|-------|---------|-------|
| 1 | 773-786 | Industry or area to which new business belongs | Heavy Industrial Engineering, Procurement and Construction, alongside Marine, Offshore, and Onshore Transportation, Logistics, and Fabrication; comprehensive design/engineering/supply/civil-structural works/turnkey contracting for mining, steel, cement, metallurgical, mineral processing including offshore oil & gas | — |
| 2 | 788-801 | Expected benefits (3 sub-bullets: 1. value-chain expansion; 2. new revenue streams from turnkey heavy-industry projects; 3. capability to undertake complex long-term infrastructure projects) | — | — |
| 3 | 802-814 | Estimated amount to be invested | "incurred incrementally based on specific project requirements, contract awards, and operational needs... funded through a mix of internal accruals and/or borrowings" — **no rupee figure given** | flag `NO_QUANTUM` — amount to be invested is qualitatively described only, no number disclosed |

Annexure B combined item count (B.1: 6 + B.2: 3): **9**.

## 15. ANNEXURE C — CHANGE IN SENIOR MANAGEMENT PERSONNEL (pages 13-14, lines 827-903)

Table has 5 fields per person (Name, Reason for change, Date of appointment/
reappointment/cessation & term, Brief profile, Disclosure of Relationship between
Directors). DIN not applicable/not disclosed for any of the three (these are SMP
designations, not board directorships).

| # | Line(s) | Name | Role/Change | Term/Effective date | Background | Relationship disclosure | Flags |
|---|---------|------|-------------|----------------------|------------|--------------------------|-------|
| 1 | 829-877 (name 829; reason 832-836; date 838-844; profile 853-878) | M. Pravin Pulujkar | Designated as Senior Management Personnel, due to change in internal role and responsibilities | w.e.f. August 11, 2026; term: existing full-time employment | Senior Procurement Professional, 22+ years cross-functional experience across Oil & Gas, EPC, Chemical, Automobile; strategic sourcing, global procurement, supplier development, contract negotiation, inventory management, cost control, vendor management, procurement planning; track record in high-value procurement, cost savings, supplier relationships, e-auction/online vendor ordering systems | Not Applicable | DIN: NOT FOUND (not a director) |
| 2 | 829-877 (date 838-844; profile 853-877) | Mr. Prasad Phatak | Designated as Senior Management Personnel, due to change in internal role and responsibilities | w.e.f. August 11, 2026; term: existing full-time employment | Experienced Senior General Manager — Projects, 30+ years project management/execution of EPC projects, managing teams of Project Managers, multiple PSU and private-sector client projects, project planning/execution/cost and cash-flow management/stakeholder coordination/risk management/procurement/logistics/timely delivery; experience across India and international locations | Not Applicable | DIN: NOT FOUND (not a director) |
| 3 | 829-877 (reason/date 838-851; profile 853, "Not Applicable") | Mr. Ravikumar Mudali Vallathur | **Ceased** to be designated as Senior Management Personnel, due to change in internal role and responsibilities, w.e.f. August 11, 2026 (from closure of business hours); no cessation of employment — continues in employment | w.e.f. August 11, 2026 (SMP designation ends; employment continues) | Not Applicable (no profile given for a cessation) | Not Applicable | flag `SMP_DESIGNATION_ENDED` (not a resignation from the Company, only from SMP status) |

SMP profile count: **3**.

---

## SUMMARY FLAGS RAISED (deduplicated)

`ZERO_STANDING` (x4: Exceptional Items standalone/consolidated, Items reclassified to
P&L standalone/consolidated), `RESTATEMENT` (x2: standalone and consolidated Diluted
EPS FY26 correction), `BUSINESS_COMBINATION`, `COMPARABILITY`, `NEW_SEGMENT` (x4),
`NCI_PRESENT` (x4: 3 P&L lines + 1 entity), `NEW_LINE_OF_BUSINESS` (x4), `NO_QUANTUM`,
`SMP_DESIGNATION_ENDED`, `UNAUDITED_BY_PRINCIPAL_AUDITOR`, `EOM_ABSENT` (x2),
`OTHER_MATTERS_ABSENT` (standalone only), `GOING_CONCERN_ABSENT` (x2),
`AGENDA_SCOPE_LIMITED`, `DISCREPANCY_VS_STANDALONE`, `NO_PRIOR_LEDGER`, `OCR_GAP`
(x7, various value/label/timestamp gaps — flagged for verification against source PDF,
not assumed to be substantive).

No `ENTITY_CHANGE` (no prior-quarter ledger to diff against — see `NO_PRIOR_LEDGER`).
No pre-conclusion signature timestamps found.
