# A2 ENUMERATION LEDGER — TRUALT Q1FY27 Results Filing

Source: `extract_results_trualt_q1fy27.txt` (10 pages, Reg 33 Board Outcome letter +
Audited/Reviewed Standalone & Consolidated Financial Results + Limited Review Report by
N.M. Raiji & Co.). Units: Rs Lakhs (x0.01 to Cr per A1 header).

```
=== A2 COUNT TEST ===
category: notes                grep_count: 12  sweep_count: 12  match: yes
category: line_items           grep_count: 67  sweep_count: 67  match: yes
category: zero_standing        grep_count: 3   sweep_count: 3   match: yes
category: agenda_items         grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras        grep_count: 11  sweep_count: 11  match: yes
category: entities             grep_count: 3   sweep_count: 3   match: yes
category: segment_tables       grep_count: 4   sweep_count: 4   match: yes  (supplementary, not in fixed YAML schema)
category: signature_blocks     grep_count: 5   sweep_count: 5   match: yes  (supplementary, not in fixed YAML schema)
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology note: naive first-pass regex on the two P&L tables returned 35/30 due to
two OCR artifacts — `(bl Other Income` (consolidated line 213, "(b)" OCR'd as "(bl") and
the unlabeled OCI subtotal row "Other Comprehensive Income for the period/ year" (starts
with "Other", not a digit/letter/dash/"Total" token). Regex was widened to
`^\s*(\(?[a-g][\)l]|[0-9]{1,2}\s|-\s|Total|Other Comprehensive Income for)` and re-run;
manual sweep independently confirmed both rows and the widened grep count. Reconciled
before emission per GATE A2.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (Reg 30(6) intimation, pp.1)

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | 50-53 | Financial results approval | Board approved Audited (Standalone and Consolidated) Financial Results for Q ended June 30, 2026 + Limited Review Report by N.M. Raiji & Co., filed as Annexure I | — |

**Board meeting timing** (line 59): commenced 2:30 p.m. IST, concluded 6:15 p.m. IST — 3h45m duration.

**Flag — AGENDA_INCOMPLETE / LETTER_SCOPE**: line 48 reads "has **inter-alia** approved" but
only ONE item is then enumerated (the results). "Inter-alia" ("among other things") signals
additional board business was transacted at the same meeting that is not detailed in this
letter. Per task context, a separate chairman-appointment intimation exists from the same
July 28, 2026 board meeting; this results letter does **not** itself enumerate it or any
other agenda item (no AR approval, AGM notice, record date, dividend, director appointment,
auditor change, scrutinizer, ESOP grant, or capital-raising resolution appears anywhere in
this extract). This is a genuine gap in this document's scope, not a missed row — the
chairman-appointment item lives in a separate filing outside this extract's page coverage.

**Flag — LABEL_INCONSISTENCY**: the Board letter (line 50-51) calls these the "**Audited**
(Standalone and Consolidated) Financial Results," while both auditor reports (lines 98,
420) and both financial-result table headers title them "**Unaudited** Consolidated /
Standalone Financial Results," reviewed (not audited) via a Limited Review under SRE 2410 —
consistent with a quarterly (non-year-end) filing. The letter's "Audited" is very likely a
misnomer/boilerplate carry-over; results are limited-review, not audited.

**Signature block** (lines 68-75): Monu Kumar, Company Secretary and Compliance Officer,
M. No. 38853; digitally signed by "MONU KUMAR KUMAR" (name field OCR-duplicated), Date:
2026.07.28 18:59:07 +05'30'. Signed 18:59, meeting concluded 18:15 — signature is AFTER
conclusion, no `SIGNATURE_TIMING` flag warranted.

---

## 2. NUMBERED NOTES

### 2A. Consolidated Financial Results — Notes (p.5-6, "Notes:" header line 307)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 308 | "The Unaudited Consolidated Financial Results have been prepared in accordance with the recognition..." | — |
| 2 | 312 | "The above Unaudited Consolidated Financial Results for the quarter ended June 30, 2026, have been reviewed..." | — |
| 3 | 314 | "The Limited Review, as required under Regulation of the SEBI... has been carried out by the Statutory Auditors..." | — |
| 4 | 316-385 | "The Group is primarily engaged in the business of manufacturing, selling of ethanol and compressed biogas..." — segment note; includes 2 reportable segments (Ethanol and other products; Compressed Biogas), 4 segment sub-tables (see Section 5 below), inter-segment pricing at arm's length | Contains embedded tables — see Section 5 |
| 5 | 386-387 | "Other Expenses for the quarter and year ended March 31, 2026, has been adjusted for an amount of Rs. 1,054.34 Lakhs representing prior period adjustments..." | Prior-period restatement disclosure |
| 6 | 388 | "Figures for the previous periods/ year have been regrouped and reclassified, wherever necessary." | Boilerplate regroup note |

Subtotal: 6 notes.

### 2B. Standalone Financial Results — Notes (p.10, "Notes:" header line 573)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 574 | "The Unaudited Standalone Financial Results have been prepared in accordance with the recognition and measurement principles..." | — |
| 2 | 578 | "The above Unaudited Standalone Financial Results for the quarter ended June 30, 2026, have been reviewed..." | — |
| 3 | 580 | "The Limited Review, as required under Regulation of the SEBI... has been carried out by the Statutory Auditors..." | — |
| 4 | 583 | "The Company's business activity falls within a single operating segment, as per the Indian Accounting Standard ('Ind AS') 108..." | Single-segment — no segment table required (contrast with consolidated Note 4, which has two segments) |
| 5 | 585-586 | "Other Expenses for the quarter and year ended March 31, 2026, has been adjusted for an amount of Rs. 1,054.34 Lakhs..." | Same Rs.1,054.34L restatement as consolidated Note 5 — cross-check consistency, appears consistent |
| 6 | 587 | "Figures for the previous periods/ year have been regrouped and reclassified, wherever necessary." | Boilerplate |

Subtotal: 6 notes.

**Manual sweep for unnumbered/footnote-style notes** (asterisks, daggers, "Note:" prefixes
below tables): none found. The single "*" hit at extract line 285 ("i * M BAI !)") is OCR
noise from a stamp/seal image on the consolidated results signature page, not a footnote
marker — confirmed by visual context (surrounded by garbled "!rd Office:" / address
fragment, i.e., part of a company-seal graphic, not text).

**TOTAL NOTES: 12** (6 consolidated + 6 standalone).

---

## 3. FINANCIAL-TABLE LINE ITEMS

### 3A. Consolidated Financial Results table (p.4, lines 210-281) — 4 periods: Q1FY27 (Jun 30 2026, Unaudited), Q4FY26 (Mar 31 2026, Audited), Q1FY26 (Jun 30 2025, Unaudited), FY26 (Mar 31 2026, Audited)

| Row | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|-----|------|------|--------|--------|--------|------|-------|
| 1 | 210 | Income (header) | — | — | — | — | — |
| 1a | 211 | Revenue from Operations | 62,688.31 | 59,551.97 | 30,389.17 | 1,72,750.66 | — |
| 1b | 213 | Other Income (OCR: "(bl Other Income") | 1,452.48 | 3,138.70 | 2,274.15 | 8,645.25 | OCR_ARTIFACT |
| — | 215 | Total Income | 64,140.79 | 62,690.67 | 32,663.32 | 1,81,395.91 | subtotal |
| 2 | 217 | Expenses (header) | — | — | — | — | — |
| 2a | 218 | Cost of Materials Consumed | 33,352.25 | 49,857.80 | 7,349.06 | 1,08,470.95 | — |
| 2b | 220 | Purchases of Stock-in-Trade | 1,058.68 | 5,368.75 | 2,253.69 | 19,967.15 | — |
| 2c | 222 | Changes in Inventories of Finished Goods | 4,768.81 | (24,352.36) | 12,372.19 | (16,992.44) | — |
| 2d | 224 | Employee Benefits Expense | 1,205.63 | 1,350.45 | 1,119.73 | 4,781.69 | — |
| 2e | 226 | Finance Costs | 4,403.46 | 4,350.25 | 3,778.88 | 16,002.41 | — |
| 2f | 228 | Depreciation and Amortisation Expense | 2,480.34 | 2,294.65 | 2,069.02 | 8,622.76 | — |
| 2g | 230 | Other Expenses | 9,027.06 | 14,396.54 | 3,140.80 | 26,493.58 | Note 5 restatement applies to Q4FY26/FY26 cols |
| — | 232 | Total Expenses | 56,296.23 | 53,266.08 | 32,083.37 | 1,67,346.10 | subtotal |
| 3 | 234 | Profit before Exceptional Items and Tax (1-2) | 7,844.56 | 9,424.59 | 579.95 | 14,049.81 | — |
| 4 | 236 | Exceptional Items | — | — | — | — | **ZERO_STANDING** — blank all 4 periods |
| 5 | 237 | Profit before Tax (3-4) | 7,844.56 | 9,424.59 | 579.95 | 14,049.81 | — |
| 6 | 239 | Tax Expense (header w/ total) | (1,917.42) | (2,540.64) | (107.43) | (3,573.85) | — |
| 6-CT | 241 | - Current Tax | (87.01) | (53.19) | — (blank) | (244.64) | blank in Q1FY26 only, not all-period zero |
| 6-DT | 243 | - Deferred Tax | (1,830.41) | (2,487.45) | (107.43) | (3,329.21) | — |
| 7 | 245 | Profit for the period/year (5-6) | 5,927.14 | 6,883.95 | 472.52 | 10,475.96 | — |
| 8 | 247 | Other Comprehensive Income (header) | — | — | — | — | — |
| 8a | 249 | - Remeasurement gain/(loss) on defined benefit plans | 1.52 | 13.23 | 0.56 | 31.01 | — |
| 8b | 251 | - Income tax effect on the above | (0.22) | (3.40) | (0.14) | (7.81) | — |
| — | 253 | Other Comprehensive Income for the period/year | 1.30 | 9.83 | 0.42 | 23.20 | subtotal (missed by naive grep — see methodology note) |
| 9 | 255 | Total Comprehensive Income for the period/year (7+8) | 5,928.44 | 6,893.78 | 472.94 | 10,499.16 | — |
| 10 | 257 | Profit for the year attributable to (header) | — | — | — | — | — |
| 10a | 259 | - Equity holders of the parent | 5,715.46 | 6,787.29 | 472.52 | 10,406.94 | — |
| 10b | 261 | - Non-controlling interests | 211.68 | 106.49 | — (blank) | 92.22 | blank Q1FY26 only |
| 11 | 263 | Other Comprehensive Income attributable to (header) | — | — | — | — | — |
| 11a | 265 | - Equity holders of the parent | 0.45 | 9.83 | 0.42 | 23.20 | — |
| 11b | 267 | - Non-controlling interests | 0.85 | — | — | — | value present ONLY in Q1FY27 col; blank other 3 — not all-period zero, flag for A3 attention as thin disclosure |
| 12 | 269 | Total Comprehensive Income for the period/year attributable to (header) | — | — | — | — | — |
| 12a | 271 | - Equity holders of the parent | 5,715.91 | 6,797.12 | 472.94 | 10,430.14 | — |
| 12b | 273 | - Non-controlling interests | 212.53 | 106.49 | — (blank) | 92.22 | blank Q1FY26 only |
| 13 | 275 | Paid up Equity Share Capital (Face Value ₹10 each) | 8,575.26 | 8,575.26 | 7,063.16 | 8,575.26 | — |
| 14 | 277 | Other Equity excluding Revaluation Reserves | — | — | — | 1,43,457.92 | value only in FY26 (annual) col — standard for interim filings, not all-period zero |
| 15 | 279-281 | Earnings Per Equity Share (₹10 FV, not annualised) — single undifferentiated row (no Basic/Diluted split, unlike standalone table) | 6.67 | 7.93 | 0.67 | 13.34 | structural inconsistency vs standalone table (see below) |

Consolidated subtotal: **37 line items** (15 numbered + 22 sub-rows/subtotals).

### 3B. Standalone Financial Results table (p.9, lines 517-547) — same 4 periods

| Row | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|-----|------|------|--------|--------|--------|------|-------|
| 1 | 517 | Income (header) | — | — | — | — | — |
| 1a | 518 | Revenue from Operations | 61,592.17 | 60,322.11 | 29,393.47 | 1,70,465.34 | — |
| 1b | 519 | Other Income | 1,445.31 | 1,339.56 | 2,255.88 | 6,828.35 | — |
| — | 520 | Total Income | 63,037.48 | 61,661.67 | 31,649.35 | 1,77,293.69 | subtotal |
| 2 | 521 | Expenses (header) | — | — | — | — | — |
| 2a | 522 | Cost of Materials Consumed | 33,222.92 | 49,810.84 | 7,235.42 | 1,08,031.39 | — |
| 2b | 523 | Purchases of Stock-in-Trade (OCR: "{b)") | 1,058.68 | 5,368.75 | 2,253.69 | 19,967.15 | OCR_ARTIFACT |
| 2c | 524 | Changes in Inventories of Finished Goods | 4,701.68 | (24,586.69) | 12,405.36 | (17,089.29) | — |
| 2d | 525 | Employee Benefits Expense | 1,133.87 | 1,274.59 | 1,054.90 | 4,494.32 | — |
| 2e | 526 | Finance Costs | 4,351.71 | 4,294.38 | 3,725.40 | 15,785.20 | — |
| 2f | 527 | Depreciation and Amortisation Expense | 2,423.09 | 2,243.27 | 2,006.47 | 8,409.08 | — |
| 2g | 528 | Other Expenses | 8,814.44 | 14,301.92 | 2,954.92 | 25,694.02 | Note 5 restatement applies to Q4FY26/FY26 cols |
| — | 529 | Total Expenses | 55,706.39 | 52,707.06 | 31,636.16 | 1,65,291.87 | subtotal |
| 3 | 530 | Profit before Exceptional Items and Tax (1-2) | 7,331.09 | 8,954.61 | 13.19 | 12,001.82 | — |
| 4 | 531 | Exceptional Items | — | — | — | — | **ZERO_STANDING** — blank all 4 periods |
| 5 | 532 | Profit before Tax (3-4) | 7,331.09 | 8,954.61 | 13.19 | 12,001.82 | — |
| 6 | 533 | Tax Expense (header w/ total) | (1,830.45) | (2,492.48) | (10.62) | (3,209.84) | — |
| 6-CT | 534 | - Current Tax | — | — | — | — | **ZERO_STANDING** — blank all 4 periods (differs from consolidated, which had partial Current Tax values — company-level tax fully deferred at standalone level this period) |
| 6-DT | 535 | - Deferred Tax | (1,830.45) | (2,492.48) | (10.62) | (3,209.84) | — |
| 7 | 536 | Profit for the period/year (5-6) | 5,500.64 | 6,462.13 | 2.57 | 8,791.98 | — |
| 8 | 537 | Other Comprehensive Income/(Expense) (header) | — | — | — | — | — |
| 8a | 539 | - Remeasurement gain/(loss) on defined benefit plans | (0.57) | 13.52 | 0.56 | 31.01 | sign flip vs consolidated (1.52 positive) — standalone vs consol basis difference, not an error per se |
| 8b | 540 | - Income tax effect on the above | 0.14 | (3.41) | (0.14) | (7.81) | — |
| — | 541 | Total Other Comprehensive Income/(Expense) | (0.43) | 10.11 | 0.42 | 23.20 | subtotal |
| 9 | 542 | Total Comprehensive Income for the period/year (7+8) | 5,500.21 | 6,472.24 | 2.99 | 8,815.18 | — |
| 10 | 543 | Paid up Equity Share Capital (Face Value ₹10 each) | 8,575.26 | 8,575.26 | 7,063.16 | 8,575.26 | — |
| 11 | 544 | Other Equity excluding Revaluation Reserves | — | — | — | 1,42,774.81 | value only FY26 col — standard, not all-period zero. Differs from consolidated Other Equity (1,43,457.92) by the NCI/consolidation adjustment — expected |
| 12 | 545 | Earnings Per Equity Share (₹10 FV, not annualised) (header) | — | — | — | — | — |
| 12a | 546 | - Basic (₹) | 6.41 | 7.54 | 0.00 | 11.24 | Q1FY26 basic EPS prints as 0.00 (rounds from 2.57L profit / large share base) |
| 12b | 547 | - Diluted (₹) | 6.41 | 7.54 | 0.00 | 11.24 | — |

Standalone subtotal: **30 line items** (12 numbered + 18 sub-rows/subtotals).

**TOTAL FINANCIAL-TABLE LINE ITEMS: 67** (37 consolidated + 30 standalone).
**TOTAL ZERO_STANDING ROWS: 3** — Consolidated "Exceptional Items" (line 236); Standalone
"Exceptional Items" (line 531); Standalone "Current Tax" (line 534).

**Structural flag — EPS_FORMAT_INCONSISTENCY**: consolidated table item 15 shows a single
undifferentiated EPS row (line 279-281, no Basic/Diluted split), while the standalone table
item 12 splits into Basic (line 546) and Diluted (line 547), both printing identical values
(6.41 / 7.54 / 0.00 / 11.24) — i.e., no dilution effect at standalone level. The consolidated
table's single EPS figure (6.67 / 7.93 / 0.67 / 13.34) is presumably also basic=diluted but
the filing does not label it as such — a presentation inconsistency between the two
statements in the same filing, worth flagging for A3/A4 rather than assuming.

---

## 4. SEGMENT SUB-TABLES (embedded in Consolidated Note 4, p.5-6, lines 322-359)

Consolidated only — standalone is single-segment (Note 4, standalone) with no segment table.

### 4A. Segment P&L — Quarter ended June 30, 2026 (lines 326-333)

| Line | Item | Ethanol & other products | Compressed Biogas | Total | Flags |
|------|------|---------------------------|--------------------|-------|-------|
| 328 | Revenue from operations | 61,567.71 | 1,120.60 | 62,688.31 | ties to line 211 |
| 329 | Segment Result | 22,584.42 | 924.15 | 23,508.57 | — |
| 330 | Other income | 1,438.42 | 14.06 | 1,452.48 | ties to line 213 |
| 331 | Profit before tax | 7,331.04 | 513.52 | 7,844.56 | ties to line 234/237 |
| 332 | Tax expense | 1,830.45 | 86.97 | 1,917.42 | ties to line 239 |
| 333 | Profit for the Period | 5,500.59 | 426.55 | 5,927.14 | ties to line 245 |

### 4B. Other Information — Quarter ended June 30, 2026 (lines 337-340)

| Line | Item | Ethanol & other products | Compressed Biogas | Total |
|------|------|---------------------------|--------------------|-------|
| 339 | Segment Assets | 3,52,683.84 | 22,763.65 | 3,75,447.49 |
| 340 | Segment Liabilities | 1,94,230.13 | 13,169.19 | 2,07,399.32 |

### 4C. Segment P&L — Quarter ended June 30, 2025 (lines 345-352)

| Line | Item | Ethanol & other products | Compressed Biogas | Total |
|------|------|---------------------------|--------------------|-------|
| 347 | Revenue from operations | 29,393.47 | 995.70 | 30,389.17 |
| 348 | Segment Result | 7,485.04 | 929.19 | 8,414.23 |
| 349 | Other income | 2,250.45 | 23.70 | 2,274.15 |
| 350 | Profit before tax | 413.93 | 166.02 | 579.95 |
| 351 | Tax expense | 78.92 | 28.51 | 107.43 |
| 352 | Profit for the Period | 335.01 | 137.51 | 472.52 |

### 4D. Other Information — Quarter ended June 30, 2025 (lines 356-359)

| Line | Item | Ethanol & other products | Compressed Biogas | Total |
|------|------|---------------------------|--------------------|-------|
| 358 | Segment Assets | 2,54,532.35 | 6,013.63 | 2,60,545.98 |
| 359 | Segment Liabilities | 1,77,158.99 | 4,578.51 | 1,81,737.50 |

TOTAL SEGMENT TABLES: 4 (16 data rows across them). No prior-year comparatives given for
Segment Assets/Liabilities beyond the two quarter-end snapshots shown (no Mar-31-2026
segment balance sheet shown) — a coverage gap worth noting, not necessarily a flag (segment
balance-sheet data is only SEBI-mandated at year-end typically).

---

## 5. AUDITOR REPORT PARAGRAPHS

### 5A. Consolidated — Independent Auditor's Review Report (p.2-3, lines 96-185)

| Para | Line | Section heading | Content | Flags |
|------|------|------------------|---------|-------|
| 1 | 106-113 | (intro) | Scope of engagement: reviewed unaudited consolidated results of TruAlt Bioenergy Ltd (Holding Co.) + subsidiaries Leafiniti Bioenergy Pvt Ltd and TruAlt Gas Pvt Ltd ("the Group"), Q ended June 30 2026 | — |
| 2 | 115-122 | (intro) | Statement is management's responsibility, approved by Board; prepared per Ind AS 34; auditor's responsibility is to express a conclusion | — |
| — | 124 | "Scope of the Review" (heading) | — | structural, not numbered |
| 3 | 126-146 | Scope of Review | Review per SRE 2410; moderate assurance, not an audit, no audit opinion expressed; also performed SEBI Circular CIR/CFD/CMD1/44/2019 procedures | — |
| 4 | 148-150 | Scope of Review | Confirms entity list: Holding Company + Leafiniti Bioenergy Pvt Ltd + TruAlt Gas Pvt Ltd | ties to consolidation entity list (Section 6) |
| — | 152 | "Conclusion" (heading) | — | structural |
| 5 | 154-161 | Conclusion | Unmodified conclusion — "nothing has come to our attention" that Statement is not prepared per Ind AS / not in compliance with Reg 33 disclosure requirements, or contains material misstatement | opinion type: unmodified review conclusion (not an "opinion" — this is a review, not an audit) |
| — | 163 | "Emphasis of Matter" (heading) | — | structural |
| 6 | 165-170 | Emphasis of Matter | Componentization exercise for Unit 4 (capitalized Feb 2026, mono-to-dual feed conversion) per Ind AS 16 is in progress; fixed assets register update pending. Conclusion NOT modified for this matter | EoM present — no Other Matters para, no Going Concern language anywhere in this report |
| — | 173-184 | Signature block | For N.M. Raiji & Co., Chartered Accountants, FRN 108296W; Partner (name OCR-garbled "Vii Baise"), Membership No. 039434; UDIN OCR-garbled ("2.S039484LHS VFF5I 4 t"); Place: Bengaluru; Date: July 28, 2026 | **OCR_ILLEGIBLE** — UDIN and partner name both corrupted in extraction; cannot be verified against ICAI UDIN portal as extracted |

Consolidated subtotal: 6 numbered paragraphs.

### 5B. Standalone — Independent Auditor's Review Report (p.7-8, lines 418-492)

| Para | Line | Section heading | Content | Flags |
|------|------|------------------|---------|-------|
| 1 | 428-432 | (intro) | Scope of engagement: reviewed unaudited standalone results of TruAlt Bioenergy Ltd ("the Company"), Q ended June 30 2026 | — |
| 2 | 434-440 | (intro) | Statement is management's responsibility, approved by Board; prepared per Ind AS 34; auditor's responsibility is to express a conclusion | — |
| — | 442 | "Scope of the Review" (heading) | — | structural |
| 3 | 444-454 | Scope of Review | Review per SRE 2410; moderate assurance, not an audit, no audit opinion expressed | note: standalone report omits the SEBI Circular CIR/CFD/CMD1/44/2019 sentence present in the consolidated report para 3 — minor asymmetry, not necessarily a flag (circular is consol-specific in some templates) |
| — | 461 | "Conclusion" (heading) | — | structural |
| 4 | 463-469 | Conclusion | Unmodified conclusion — same "nothing has come to our attention" language as consolidated | — |
| — | 471 | "Emphasis of Matter" (heading) | — | structural |
| 5 | 473-478 | Emphasis of Matter | Identical Unit 4 componentization EoM as consolidated report (Ind AS 16, fixed assets register update pending). Conclusion NOT modified | EoM present, mirrors consolidated — no Other Matters, no Going Concern |
| — | 481-492 | Signature block | For N.M. Raiji & Co., Chartered Accountants, FRN 108296W; Partner name field blank/not printed; Membership No. 039434 (same as consolidated — same signing partner); UDIN OCR-garbled ("~e,03q43i, 5 El K$ z_l-tlf O g"); Place: Bengaluru; Date: July 28, 2026 | **OCR_ILLEGIBLE** — UDIN corrupted; partner name not printed at all in this block (vs garbled-but-present in consolidated) |

Standalone subtotal: 5 numbered paragraphs.

**TOTAL AUDITOR-REPORT PARAGRAPHS: 11** (6 consolidated + 5 standalone).
**Opinion type (both reports): unmodified review conclusion** (SRE 2410 limited review, not an audit — no audit opinion expressed, consistent with both reports' own text and inconsistent with the Board letter's "Audited" label, see Section 1 LABEL_INCONSISTENCY flag).
**Entities unaudited/management-furnished**: none singled out — both subsidiaries (Leafiniti Bioenergy Pvt Ltd, TruAlt Gas Pvt Ltd) are covered within the single consolidated review scope per para 1/4; no language carves out any entity as unreviewed or management-certified-only.
**UDIN**: both present but OCR-illegible in this extract — flag for A1/source-PDF re-check if UDIN verification is required.

---

## 6. CONSOLIDATION ENTITY LIST

| # | Entity | Relationship | First cited line | Flags |
|---|--------|--------------|-------------------|-------|
| 1 | TruAlt Bioenergy Limited | Holding Company (the "Company" / reporting entity) | 104 | — |
| 2 | Leafiniti Bioenergy Private Limited | Subsidiary | 108 | — |
| 3 | TruAlt Gas Private Limited | Subsidiary | 108 | — |

TOTAL ENTITIES: 3. Entity list is internally consistent across auditor report para 1, para
4, and consolidated Note 4 (segment note references "the Group" / "its subsidiaries" without
naming a third or different subsidiary set anywhere). No internal inconsistency found.

**Prior-quarter comparison**: none available — task context confirms this is fresh TRUALT
coverage with no prior /run-quarterly ledger for this ticker. `ENTITY_CHANGE` NOT raised
(no prior list to diff against, and no internal inconsistency found within this filing).

---

## 7. SIGNATURE / DIGITAL-SIGNATURE BLOCKS

| # | Line | Document | Signatory | Designation | Timestamp | Flags |
|---|------|----------|-----------|-------------|-----------|-------|
| 1 | 68-75 | Board Outcome letter | Monu Kumar (digitally signed, name field OCR-duplicated as "MONU KUMAR KUMAR") | Company Secretary and Compliance Officer, M.No. 38853 | 2026.07.28 18:59:07 +05'30' | Signed AFTER meeting concluded (18:15) — no timing flag |
| 2 | 173-184 | Consolidated Auditor's Review Report | Partner (name OCR-garbled) | Partner, N.M. Raiji & Co., Membership No. 039434, FRN 108296W | Date only: July 28, 2026 (no time) | OCR_ILLEGIBLE (partner name, UDIN) |
| 3 | 392-400 | Consolidated Financial Results — Board sign-off | Name OCR-garbled ("rugesh Nir...") | Managing Director, DIN partially legible ("...77") | Place: Bengaluru; Date: 28 July 2026 | OCR_ILLEGIBLE (name, DIN truncated) |
| 4 | 481-492 | Standalone Auditor's Review Report | Partner (name not printed) | Partner, N.M. Raiji & Co., Membership No. 039434, FRN 108296W | Date only: July 28, 2026 (no time) | OCR_ILLEGIBLE (UDIN); same Membership No. as consolidated report — same signing partner across both reports, consistent |
| 5 | 589-602 | Standalone Financial Results — Board sign-off | Name OCR-garbled/not legible | Managing Director, DIN: 07413777 | Place: Bengaluru; Date: 28 July 2026 | DIN 07413777 is fully legible here and consistent with the truncated "...77" in signature block #3 — same Managing Director signed both statements |

TOTAL SIGNATURE BLOCKS: 5.

---

## 8. ANNEXURES

| # | Line | Annexure | Contents |
|---|------|----------|----------|
| 1 | 53, 96 | Annexure I | Financial Results (Consolidated + Standalone) together with Limited Review Report issued by N.M. Raiji & Co. — encompasses Sections 3, 4, 5 of this ledger in full |

Only one annexure is named in the filing (the letter's "Encl.: As above" at line 79 refers
back to this single Annexure I). No further annexures (no separate director-profile
annexure, no separate press-release annexure) appear in this extract.

---

## 9. HEADER / LETTERHEAD BOILERPLATE (not separately enumerated as disclosure units)

Company letterhead (name, CIN L15400KA2021PLC145978, GSTIN 29AAICT5347A1ZB, phone, email,
website, "FORMERLY KNOWN AS TRUALT ENERGY LIMITED") repeats on every page (1, 4-6, 9-10);
Registered/Corporate Office address block repeats on pages 1, 6, 9, 10 — identical each time,
no discrepancy found. Not treated as discrete disclosure line items per instruction scope
(static branding, not a transaction/agenda/financial disclosure), but flagged here for
completeness of sweep documentation. The "(FORMERLY KNOWN AS TRUALT ENERGY LIMITED)" tag is
itself informative (recent name change) but is not a Q1FY27-specific disclosure event.

---

## SUMMARY COUNTS

| Category | Count |
|----------|-------|
| Notes (numbered) | 12 |
| Financial-table line items (standalone + consolidated, all periods) | 67 |
| — of which ZERO_STANDING | 3 |
| Segment sub-tables (supplementary) | 4 (16 rows) |
| Board Outcome agenda items | 1 |
| Auditor-report numbered paragraphs | 11 |
| Consolidation entities | 3 |
| Signature blocks | 5 |
| Annexures | 1 |

## FLAGS RAISED (full list)
- `ZERO_STANDING` x3 — Consolidated Exceptional Items (line 236); Standalone Exceptional Items (line 531); Standalone Current Tax (line 534)
- `AGENDA_INCOMPLETE` — Board letter says "inter-alia approved" but enumerates only 1 item; separate chairman-appointment intimation from same meeting exists outside this extract
- `LABEL_INCONSISTENCY` — Board letter calls results "Audited"; both auditor reports and table headers call them "Unaudited...Financial Results" under Limited Review (not audit)
- `OCR_ILLEGIBLE` x2 — both UDINs (consolidated line 183, standalone line 490) and both partner-name fields are OCR-corrupted in this extract; cannot be verified as-is
- `EPS_FORMAT_INCONSISTENCY` — consolidated EPS shown as single undifferentiated row (line 279-281); standalone EPS split into Basic/Diluted (lines 546-547)
- `ENTITY_CHANGE` — NOT raised (no prior-quarter ledger available for comparison; no internal inconsistency found)
- `SIGNATURE_TIMING` — NOT raised (board letter digital signature at 18:59 is after 18:15 meeting conclusion)
