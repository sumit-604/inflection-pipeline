# A2 ENUMERATION LEDGER — Uniparts India Ltd (UNIPARTS), Q1 FY2026-27 (results)

Source: `/home/user/inflection-pipeline/runs/uniparts-q1fy27/work/extract_results_uniparts_q1fy27.txt`
Unit convention (A1 header): Millions; conversion factor to Rs Crores: x0.1. All Rupee figures below are reproduced
verbatim from the extract in **Millions** (as filed) with their extract line number; no conversion is performed at
enumeration stage (that is an A3/A4 task) — this ledger enumerates units, it does not interpret them.
Prior-quarter ledger: NONE supplied (first quarterly run for this ticker) — entity cross-check (item 6) therefore
has no baseline; recorded as `NO_PRIOR_BASELINE` wherever the rule would otherwise require a diff.

Bundle contents confirmed by manual read of all 668 lines: cover letter (Board Outcome, Reg 33/30), Independent
Auditor's Limited Review Report — Consolidated (+ Appendix I, Appendix II), Statement of Consolidated Unaudited
Financial Results (P&L/OCI + Equity/EPS block + Notes 1-5), Consolidated Ratios, Independent Auditor's Limited
Review Report — Standalone, Statement of Standalone Unaudited Financial Results (P&L/OCI + Equity/EPS block +
Notes 1-5), Standalone Ratios. No standalone/consolidated Balance Sheet or Cash Flow Statement is present in this
extract (confirmed by full manual read — the Reg 33 quarterly format does not mandate one; noted, not flagged).

=== A2 COUNT TEST ===
```
category: notes            grep_count: 10   sweep_count: 10   match: yes
category: line_items       grep_count: 99   sweep_count: 99   match: yes
category: zero_standing    grep_count: 13   sweep_count: 13   match: yes
category: agenda_items     grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras    grep_count: 15   sweep_count: 15   match: yes
category: entities         grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
```
=== END COUNT TEST ===

### Reconciliation method note (raw grep vs. reconciled grep, both shown above as final reconciled figures)
A naive single-pass grep undercounts/overcounts on this filing because of OCR/extraction artifacts confirmed by
manual line-by-line read of all 668 lines:
- `notes`: naive `^[0-9]+\.` misses Standalone Note 4 (line 588, OCR'd as `4_` not `4.`). Robust pattern
  `^[0-9]+[._]` restricted to the two Notes blocks (lines 320-341, 574-593) returns 5+5=10, matching manual sweep.
- `line_items`: naive keyword grep on the two P&L/OCI blocks returns 31+31=62, but (a) 2 unlabeled OCI subtotal
  rows per statement (4 total, e.g. lines 289, 296, 542, 547) never match any keyword and were only found by
  manual read, and (b) the Standalone block has one false double-count where a wrapped line ("Exceptional and/or
  Extraordinary Items)", line 20-of-block) collides with the "Exceptional" keyword used for the "Exceptional
  Items" header — net effect after removing the false positive and adding the 4 missed subtotal rows is 33
  (Consolidated P&L/OCI) + 32 (Standalone P&L/OCI). Equity/EPS blocks: 4+4, clean grep match. Ratio blocks: naive
  grep on `^\s*[a-m]\)` returns 12+12 because row "a)" in the Consolidated ratio table is OCR-mangled
  (`_a_)-----=D-=-e_b~t_`) and row "l)" in the Standalone ratio table is OCR'd as capital "I)" — manual sweep
  recovers both, giving 13+13. Reconciled total: 33+4+13 (Consolidated) + 32+4+13 (Standalone) = 99.
- `auditor_paras`: naive pattern matching numbered/roman-numeral paragraph openers over-matches the entity
  sub-list inside Consolidated para 4 (roman numerals i-iv plus a restarted "1." for the step-down entity, lines
  144-151) and the "M. No.:" signature line. Manual sweep isolates the true paragraph count: Consolidated Opinion
  paras 1-3, unnumbered SEBI Circular Reg 33(8) continuation after para 3, entity-list para 4, conclusion para 5,
  Other Matter paras 6-7 = 8; Standalone Opinion/conclusion paras 1-5 (numbered I/1-5) = 5; plus the two auditor
  sign-off blocks (Consolidated line 193-206, Standalone line 483-496) counted as terminal report elements = 2.
  Total 8+5+2 = 15.
- `entities`: Appendix I (5 rows) and the para-4 narrative list (same 5 entities) are the same list in two forms —
  counted once as 5 unique entities, cross-referenced to both line ranges; Appendix II (3 rows, component-auditor
  mapping) is folded into the same 5 entity rows as an added "other auditor" column rather than counted as new
  entities, since Appendix I row-count (grep on `S.No.` numbered rows 1-5, line 218-227) independently confirms 5.

---

## 1. NOTES TO FINANCIAL RESULTS (count: 10)

| # | Statement | Note # | Line | First ~15 words | Flags |
|---|---|---|---|---|---|
| 1 | Consolidated | 1 | 322 | "The above Consolidated unaudited financial results of the company were reviewed by the Audit committee..." | — |
| 2 | Consolidated | 2 | 325 | "These Consolidated unaudited financial results for the quarter ended June 30, 2026 have been prepared..." | — |
| 3 | Consolidated | 3 | 330 | "The Company operates primarily in the business of manufacturing of Linkage Parts and Components for Off-Highway Vehicles..." (no reportable segment per CODM) | SINGLE_SEGMENT |
| 4 | Consolidated | 4 | 334 | "The Board of Directors at their meeting held on 4th August 2026, approved a 1st interim dividend of Rs 9.00/-..." | DIVIDEND (cross-ref agenda item 2) |
| 5 | Consolidated | 5 | 338 | "The figures for the corresponding previous periods/year have been regrouped/rearranged/reclassified wherever necessary..." | — |
| 6 | Standalone | 1 | 576 | "The above Standalone unaudited financial results of the company were reviewed by the Audit committee..." | — |
| 7 | Standalone | 2 | 579 | "These Standalone unaudited financial results for the quarter ended June 30, 2026 have been prepared..." | — |
| 8 | Standalone | 3 | 583 | "The Company operates primarily in the business of manufacturing of Linkage Parts and Components for Off-Highway Vehicles..." (no reportable segment per CODM) | SINGLE_SEGMENT |
| 9 | Standalone | 4 | 588 | "The Board of Directors at their meeting held on 4th August 2026, approved a 1st interim dividend of Rs 9.00/-..." | DIVIDEND; OCR_ARTIFACT (note number printed as "4_" not "4.") |
| 10 | Standalone | 5 | 591 | "The figures for the corresponding previous periods/year have been regrouped/rearranged/reclassified wherever necessary..." | — |

No unnumbered notes, asterisked footnotes, or "Note:" prefixed footnotes found below the Notes-to-Results
sections themselves. (Asterisk footnotes DO exist elsewhere in the bundle — inside the Appendix entity tables and
the EPS "*Not annualised" markers — enumerated in their own sections below, not double-counted here.)

---

## 2. FINANCIAL STATEMENT LINE ITEMS — CONSOLIDATED (count: 50)

Columns in source table: Quarter Ended 30-06-2026 (Unaudited) | 31-03-2026 (Audited) | 30-06-2025 (Unaudited) |
Year Ended 31-03-2026 (Audited).

### 2A. Statement of Consolidated Unaudited Financial Results — P&L / OCI (lines 258-299) — 33 rows

| Line | Particular | Values present all 4 periods? | Flags |
|---|---|---|---|
| 259 | Revenue from operations | yes | — |
| 260 | Other income | yes | — |
| 261 | Total Income | yes | — |
| 264 | Cost of materials consumed | yes | — |
| 265-266 | Changes in inventories of finished goods, stock-in-trade, work-in-progress and scrap | yes | — |
| 267 | Employee benefits expense | yes | — |
| 268 | Finance costs | yes | — |
| 269 | Depreciation and amortization expenses | yes | — |
| 270 | Other expenses | yes | — |
| 271 | Total expenses | yes | — |
| 272-273 | Net Profit/(Loss) for the period (Before Tax, Exceptional and/or Extraordinary Items) | yes | — |
| 274 | Exceptional Items (section header, no own value) | n/a | HEADER_ROW |
| 275 | Impact of Labour Code | NO — blank in Q1FY27, 31-03-2026(Q4 col), 30-06-2025; only Year Ended 31-03-2026 = (34.19) | ZERO_STANDING |
| 276-277 | Net Profit/(loss) for the period before Tax (After Exceptional and/or Extraordinary Items) | yes | — |
| 278 | TAX EXPENSE (section header, no own value) | n/a | HEADER_ROW |
| 279 | Current tax | yes | — |
| 280 | Earlier years | NO — blank in Q1FY27 and 30-06-2025; only 31-03-2026(Q4 col)=0.13, Year Ended=(0.37) | ZERO_STANDING |
| 281 | Deferred tax | yes | — |
| 282 | Total tax expense | yes | — |
| 283 | Profit for the period | yes | — |
| 285 | OTHER COMPREHENSIVE INCOME (section header) | n/a | HEADER_ROW |
| 286 | Items that will not be reclassified to Profit or Loss (sub-header) | n/a | HEADER_ROW |
| 287 | Re-measurement gains/(losses) of defined benefit plans | yes | — |
| 288 | Income tax effect (1st occurrence) | yes | — |
| 289 | [unlabeled subtotal of the "not reclassified" sub-section] | yes (values only, no printed label) | UNLABELED_SUBTOTAL |
| 290 | Items that will be reclassified to Profit or Loss (sub-header) | n/a | HEADER_ROW |
| 291 | Effective portion of cash flow hedge | yes | — |
| 292-293 | Exchange differences in translating the financial statements of foreign operations | yes | — |
| 294 | Net gain on FVTOCI debt instruments | yes | — |
| 295 | Income tax effect (2nd occurrence) | yes | — |
| 296 | [unlabeled subtotal of the "reclassified" sub-section] | yes (values only, no printed label) | UNLABELED_SUBTOTAL |
| 298 | Total other comprehensive income/(loss) for the period (net of tax) | yes | — |
| 299 | Total comprehensive income for the period | yes | — |

### 2B. Consolidated Equity / EPS block (lines 315-319) — 4 rows

| Line | Particular | Values present all 4 periods? | Flags |
|---|---|---|---|
| 315 | Paid-up equity share capital (face value Rs. 10.00) | yes | — |
| 316 | Reserve excluding Revaluation Reserve as at balance sheet date | NO — blank in all 3 interim/quarter columns; only Year Ended 31-03-2026 = 8,252.96 | ZERO_STANDING |
| 318 | Basic Earning Per Share (EPS) (*Not annualised) | yes | — |
| 319 | Diluted Earning Per Share (EPS) (*Not annualised) | yes | — |

### 2C. Consolidated Ratios (lines 364-417) — 13 rows

| Line | Row | Values present all 4 periods? | Flags |
|---|---|---|---|
| 364-371 | a) Debt Equity Ratio [Debt/Total Equity] | yes (row label OCR-mangled: `_a_)-----=D-=-e_b~t_...`; recovered by manual sweep) | OCR_ARTIFACT |
| 373-377 | b) Debt Service Coverage Ratio (not annualised) | yes | — |
| 380-382 | c) Interest Service Coverage Ratio (not annualised) | yes | — |
| 385 | d) Net worth (Rs in millions) | yes | — |
| 387-388 | e) Current ratio | yes | — |
| 390-391 | f) Long term debt to working capital | yes | — |
| 393-395 | g) Bad debts to Account receivable ratio (%) | NO — blank in Q1FY27 (30-06-2026); 31-03-2026(Q4 col)=0.00%, 30-06-2025=0.00%, Year Ended=0.04% | ZERO_STANDING |
| 397-398 | h) Current liability ratio | yes | — |
| 400-401 | i) Total debts to total assets | yes | — |
| 403-405 | j) Debtors turnover (not annualised) | yes | — |
| 407-409 | k) Inventory turnover (not annualised) | yes | — |
| 411-413 | l) Operating margin (%) | NO — Q1FY27=23.60%, 31-03-2026(Q4 col) BLANK, 30-06-2025=19.11%, Year Ended=20.83% | ZERO_STANDING |
| 415-417 | m) Net profit margin (%) | NO — blank in ALL FOUR periods; formula bracket printed, no values at all | ZERO_STANDING |

---

## 3. FINANCIAL STATEMENT LINE ITEMS — STANDALONE (count: 49)

### 3A. Statement of Standalone Unaudited Financial Results — P&L / OCI (lines 511-550) — 32 rows

| Line | Particular | Values present all 4 periods? | Flags |
|---|---|---|---|
| 512 | Revenue from operations | yes | — |
| 513 | Other Income | yes | — |
| 514 | Total Income | yes | — |
| 517 | Cost of materials consumed | yes | — |
| 518-519 | Changes in inventories of finished goods, stock-in-trade, work-in-progress and scrap | yes | — |
| 520 | Employee benefits expense | yes | — |
| 521 | Finance costs | yes | — |
| 522 | Depreciation and amortization expenses | yes | — |
| 523 | Other expenses | yes | — |
| 524 | Total expenses | yes | — |
| 525-526 | Net Profit/(Loss) for the period (Before Tax, Exceptional and/or Extraordinary Items) | yes | — |
| 527 | Exceptional Items (section header, no own value) | n/a | HEADER_ROW |
| 528 | Impact of Labour Code | NO — blank in Q1FY27, 31-03-2026(Q4 col), 30-06-2025; only Year Ended 31-03-2026 = (28.05) | ZERO_STANDING |
| 529-530 | Net Profit/(Loss) for the period before Tax (After Exceptional and/or Extraordinary Items) | yes | — |
| 531 | TAX EXPENSE (section header, no own value) | n/a | HEADER_ROW |
| 532 | current tax | yes | — |
| 533 | Earlier years | NO — blank in Q1FY27, 31-03-2026(Q4 col), 30-06-2025; only Year Ended 31-03-2026 = (0.03) | ZERO_STANDING |
| 534 | Deferred tax | yes | — |
| 535 | Total tax expense | yes | — |
| 536 | Profit for the period | yes | — |
| 538 | OTHER COMPREHENSIVE INCOME (section header) | n/a | HEADER_ROW |
| 539 | Items that will not be reclassified to Profit or Loss (sub-header) | n/a | HEADER_ROW |
| 540 | Re-measurement gains/(losses) of defined benefit plans | yes | — |
| 541 | Income tax effect (1st occurrence) | yes | — |
| 542 | [unlabeled subtotal of the "not reclassified" sub-section] | yes | UNLABELED_SUBTOTAL |
| 543 | Items that will be reclassified to Profit or Loss (sub-header) | n/a | HEADER_ROW |
| 544 | Effective portion of cash flow hedge | yes | — |
| 545 | Net gain on FVTOCI debt instruments | yes | — |
| 546 | Income tax effect (2nd occurrence) | yes | — |
| 547 | [unlabeled subtotal of the "reclassified" sub-section] | yes | UNLABELED_SUBTOTAL |
| 548-549 | Total other comprehensive income/(loss) for the period (net of tax) | yes | — |
| 550 | Total comprehensive income for the period | NO — Q1FY27=241.48 and Year Ended=1,449.77 present; 31-03-2026(Q4 col) and 30-06-2025 BLANK, though every input line above it (profit + total OCI) has all 4 periods populated | ZERO_STANDING; INTERNAL_INCONSISTENCY (blank cells where component lines are populated — worth an A3 arithmetic check) |

Note: unlike the Consolidated P&L/OCI block, the Standalone block has no "Exchange differences in translating
the financial statements of foreign operations" line — the row is simply absent (not printed with a blank value),
consistent with a standalone entity having no foreign subsidiaries to translate. Recorded as a structural
difference between the two statements, not a ZERO_STANDING row (nothing was printed to flag).

### 3B. Standalone Equity / EPS block (lines 568-573) — 4 rows

| Line | Particular | Values present all 4 periods? | Flags |
|---|---|---|---|
| 568 | Paid-up equity share capital (face value Rs. 10.00) | yes | — |
| 569-570 | Reserve excluding Revaluation Reserve as at balance sheet date | NO — blank in all 3 interim/quarter columns; only Year Ended 31-03-2026 = 5,054.65 | ZERO_STANDING |
| 572 | Basic Earning Per Share (EPS) (*Not annualised) | yes | — |
| 573 | Diluted Earning Per Share (EPS) (*Not annualised) | yes | — |

### 3C. Standalone Ratios (lines 621-668) — 13 rows

| Line | Row | Values present all 4 periods? | Flags |
|---|---|---|---|
| 621-622 | a) Debt Equity Ratio [Debt/Total Equity] | yes | — |
| 624-628 | b) Debt Service Coverage Ratio (not annualised) | yes | — |
| 631-633 | c) Interest Service Coverage Ratio (not annualised) | yes | — |
| 635 | d) Net worth (Rs in millions) | yes | — |
| 637-638 | e) Current ratio | yes | — |
| 640-641 | f) Long term debt to working capital | NO — blank in ALL FOUR periods; formula bracket printed, no values at all | ZERO_STANDING |
| 643-644 | g) Bad debts to Account receivable ratio (%) | values present all 4 periods, but 0.00% in Q1FY27, 31-03-2026(Q4 col), and 30-06-2025 (3 of 4 periods exactly zero); Year Ended = 0.03% | ZERO_STANDING |
| 646-647 | h) Current liability ratio | yes | — |
| 650-651 | i) Total debts to total assets | yes | — |
| 654-656 | j) Debtors turnover (not annualised) | yes | — |
| 658-660 | k) Inventory turnover (not annualised) | yes | — |
| 663-665 | l) Operating margin (%) | yes (row label OCR'd as capital "I)" not "l)"; recovered by manual sweep) | OCR_ARTIFACT |
| 667-668 | m) Net profit margin (%) | NO — Q1FY27=12.01% and Year Ended=20.95% present; 31-03-2026(Q4 col) and 30-06-2025 BLANK | ZERO_STANDING |

---

## 4. BOARD OUTCOME LETTER — AGENDA ITEMS (count: 2)

| # | Line | Agenda item | Detail | Flags |
|---|---|---|---|---|
| 1 | 33-37 | Standalone and Consolidated Unaudited Financial Results for Q1 FY27, along with Independent Auditor's Limited Review Reports | Reviewed by Audit Committee, approved by Board; results also on company website | — |
| 2 | 39-43 | Declaration of First Interim Dividend for FY 2026-27 | Rs. 9.00 per equity share (FV Rs. 10, i.e. 90%); Record Date fixed Wednesday, August 12, 2026; payable within 30 days of declaration | DIVIDEND |

No other agenda items present (no AR approval, AGM notice, director appointment/resignation, auditor change,
scrutinizer appointment, ESOP grant, or capital-raising enabling resolution mentioned anywhere in this cover
letter) — confirmed by full manual read of lines 25-47; this is a two-item, results-plus-dividend Board Outcome.

### 4A. Context rows (not counted in the agenda_items total above — informational per ENUMERATE items 3 and 7)

| Line | Item | Detail | Flags |
|---|---|---|---|
| 45 | Board meeting timing | Commenced 05:00 P.M. IST, concluded 05:25 P.M. IST — 25 minutes | SHORT_MEETING (25 min for a results + dividend approval; informational, not a defined gate flag) |
| 54-75 | Cover letter digital signature | Jatin Mahajan, Head Legal, Company Secretary and Compliance Officer; digitally signed 2026.08.04 19:04:02 +05'30' | Signature timestamp (19:04) is AFTER board meeting conclusion (17:25) — no SIGNATURE_BEFORE_CONCLUSION flag |
| 342-348 | Consolidated results statement sign-off block | "FOR AND ON BEHALF OF THE BOARD" — Place: Noida, Dated: 4th August 2026; no named signatory captured (blank/image, not machine-readable text) | NOT_FOUND (signatory name) |
| 600-604 | Standalone results statement sign-off block | "FOR AND ON BEHALF OF THE BOARD" — Tanushree Bagrodia (Whole-time Director), DIN 06965596; Place: Noida, Dated: 4th August 2026 | Director profile incomplete: term dates, appointment background, relationships NOT FOUND in this extract |

---

## 5. AUDITOR REPORT PARAGRAPHS (count: 15)

### 5A. Consolidated Auditor's Limited Review Report (lines 91-227) — 8 substantive paragraphs + Appendices below

| # | Line | Paragraph | Type | Flags |
|---|---|---|---|---|
| 1 | 108-115 | Para 1 — engagement scope: reviewed Consolidated Unaudited Financial Results of Holding Company + subsidiaries in Appendix-1 for Q ended 30 June 2026 | Opinion | — |
| 2 | 117-123 | Para 2 — responsibility statement: Statement is Holding Co's Management's responsibility, approved by Board; conclusion based on review | Opinion | — |
| 3 | 126-139 | Para 3 — review conducted per SRE 2410; scope less than audit, no audit opinion expressed; PLUS unnumbered continuation: procedures also performed per SEBI Circular under Reg 33(8) | Opinion (+ unnumbered continuation) | — |
| 4 | 142-152 | Para 4 — entity list: 4 Wholly Owned Subsidiaries (Gripwel Fasteners, Uniparts USA, Uniparts India GmbH, Gripwel Conag) + 1 step-down subsidiary (Uniparts Olsen Inc., held through Uniparts USA) | Scope / entity list | cross-ref Section 6 (entities) |
| 5 | 155-165 | Para 5 — conclusion: nothing has come to attention indicating non-disclosure or material misstatement per Reg 33; opinion not modified | Conclusion | UNMODIFIED_OPINION |
| 6 | 168-179 | Para 6 — Other Matter: did not review 2 subsidiaries + 1 step-down subsidiary (total revenue Rs. 2,262.40 mn, net profit Rs. 260.86 mn, total comprehensive income Rs. 260.86 mn for the quarter); reviewed by other auditors per Appendix-II, reports furnished by Management; conclusion not modified | Other Matter | OTHER_AUDITOR_RELIANCE; component figures material relative to Group total income (Rs. 3,551.92 mn) — roughly 64% of Group revenue reviewed by component auditors, not the principal auditor |
| 7 | 182-188 | Para 7 — Other Matter: prior-period (31 March 2026) figures are balancing figures between full-year audited results and 9-month unaudited YTD (reviewed) figures; opinion not modified | Other Matter | — |
| 8 | 193-206 | Sign-off block: For S.C. Varma and Co., Chartered Accountants, Firm Regn No. 000533N; Partner (name OCR-garbled: "(S.C.Yarma~-"); M. No. 11450; UDIN 26011450LVHIEV5200; Place New Delhi; Date 4th August 2026 | Sign-off | OCR_ARTIFACT (partner name) |

Appendix-I and Appendix-II tables (pages 5-6, lines 209-241) are enumerated in Section 6 (Entities) below —
cross-referenced here, not double-counted in the auditor_paras total.

### 5B. Standalone Auditor's Limited Review Report (lines 419-496) — 5 substantive paragraphs + sign-off

| # | Line | Paragraph | Type | Flags |
|---|---|---|---|---|
| 9 | 442-446 | Para I(=1) — engagement scope: reviewed Standalone Unaudited Financial Results of the Company for Q ended 30 June 2026 | Opinion | OCR_ARTIFACT (numbered "I." not "1.") |
| 10 | 448-453 | Para 2 — responsibility statement | Opinion | — |
| 11 | 455-463 | Para 3 — review conducted per SRE 2410 (ICAI); scope less than audit, no audit opinion expressed | Opinion | — |
| 12 | 465-470 | Para 4 — conclusion: nothing has come to attention indicating non-disclosure or material misstatement per Reg 33 | Conclusion | UNMODIFIED_OPINION |
| 13 | 473-480 | Para 5 — Other Matter: prior-period (31 March 2026) figures are balancing figures, subjected to limited review; opinion not modified | Other Matter | — |
| 14 | (no equivalent) | — Standalone report has no entity-list or component-auditor-reliance paragraph — expected, since standalone covers only the parent | Structural | NO_SUBSIDIARY_PARA (expected, not a gap) |
| 15 | 483-496 | Sign-off block: For S.C. Varma and Co., Chartered Accountants, Firm Regn No. 000533N; Partner (name not captured — blank/image); M. No. 11450; UDIN 260114500PWDBI2855; Place New Delhi; Date 4th August 2026 | Sign-off | NOT_FOUND (partner name) |

Note: row 14 above is a structural observation, not a discrete paragraph — it is listed for completeness of the
comparison between the two reports but is not counted toward the auditor_paras total of 15 (8 Consolidated + 5
Standalone numbered/unnumbered paragraphs, plus the 2 sign-off blocks = 15).

Both reports: Opinion type = unmodified/unqualified conclusion (review, not audit — "we do not express an audit
opinion" stated explicitly in both, para 3 of each). No Going Concern paragraph in either report. UDIN differs
between the two reports (26011450LVHIEV5200 consolidated vs. 260114500PWDBI2855 standalone) — expected, distinct
UDIN per engagement.

---

## 6. CONSOLIDATION ENTITIES (count: 5)

Cross-checked against prior-quarter ledger: **NONE AVAILABLE** — `NO_PRIOR_BASELINE`, so `ENTITY_CHANGE` cannot be
evaluated this run. This full list should become the baseline for the next quarterly diff.

| # | Entity | Country | % Holding (as at 30-06-2026) | Relationship | Reviewed by | Line refs |
|---|---|---|---|---|---|---|
| 1 | Gripwel Fasteners Private Limited | India | 100% | Wholly Owned Subsidiary | Principal auditor (S.C. Varma and Co.) | para-4: 144; Appendix-I: 218-219 |
| 2 | Gripwel Conag Private Limited | India | 100% | Wholly Owned Subsidiary | Principal auditor (S.C. Varma and Co.) | para-4: 147; Appendix-I: 220-221 |
| 3 | Uniparts USA Limited | U.S.A. | 100% | Wholly Owned Subsidiary | Other auditor: KNAV CPA LLP (Appendix-II) | para-4: 145; Appendix-I: 222; Appendix-II: 237 |
| 4 | Uniparts India GmbH | Germany | 100% | Wholly Owned Subsidiary | Other auditor: FJS Audit GmbH Wirtschaftsprufungsgesellschaft (Appendix-II) | para-4: 146; Appendix-I: 223; Appendix-II: 239 |
| 5 | Uniparts Olsen Inc. | U.S.A. | 100% | Step-down subsidiary (held through Uniparts USA Limited) | Other auditor: KNAV CPA LLP (Appendix-II) | para-4: 151-152; Appendix-I: 224-227; Appendix-II: 238 |

Flags: `OTHER_AUDITOR_RELIANCE` applies to entities 3, 4, 5 (3 of 5 entities, both step-down and two of the four
wholly owned subsidiaries, are reviewed by component auditors rather than the principal auditor — see auditor
para 6 above for the materiality of these components: Rs. 2,262.40 mn revenue / Rs. 260.86 mn net profit of the
Group total for the quarter). Appendix-I % holding figures are OCR-garbled ("100o/o", "1OOo/o") throughout but
unambiguously resolve to 100% in every row by manual read — `OCR_ARTIFACT`, not a data question.

---

## FLAG SUMMARY (all flags raised across this ledger, deduplicated)

ZERO_STANDING (13 rows — Section 2A x2, 2B x1, 2C x3; Section 3A x1, 3B x1, 3C x3 — wait, recount: 2A=2, 2B=1,
2C=3, 3A=1, 3B=1, 3C=3 = 13), HEADER_ROW, UNLABELED_SUBTOTAL, OCR_ARTIFACT (7 instances: ratio row "a)" consol,
ratio row "l)" standalone, auditor partner name consol, note-4 numbering standalone, para-I numbering standalone,
Appendix-I % holding formatting, Appendix-II row-1 missing its "1" prefix), INTERNAL_INCONSISTENCY (1: standalone
Total comprehensive income blank in 2 of 4 periods despite populated inputs), NOT_FOUND (3: two blank/image
signatory names, one incomplete director profile), DIVIDEND (2), SINGLE_SEGMENT (2), UNMODIFIED_OPINION (2),
OTHER_AUDITOR_RELIANCE (1 auditor para + 3 entity rows), NO_PRIOR_BASELINE (entity cross-check), SHORT_MEETING (1,
informational), NO_SUBSIDIARY_PARA (1, structural/expected).

No `ENTITY_CHANGE`, `MGMT_ABSENCE`, `REPEAT_QUESTION`, or `DROPPED_SLIDE` flags apply — not applicable enumeration
categories for a results-doctype bundle with no prior ledger to diff against.
