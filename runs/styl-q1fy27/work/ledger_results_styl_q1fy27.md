# A2 Completeness Ledger — STYL Q1FY27 Results Filing (Reg 33)

Source: `extract_results_styl_q1fy27.txt` (results_styl_q1fy27.pdf, 12 pages, Adobe Paper
Capture scan + OCR text layer; pages 7, 8, 11, 12 carry an independent tesseract
cross-check block per A1). Unit: INR Million (x0.1 = Rs Cr).

Doctype contents actually present: covering letter / Board Outcome (p1), Press
Release (p2-4), Consolidated Limited Review report (p5-6), Statement of
Consolidated Unaudited Financial Results + Notes (p7-8), Standalone Limited
Review report (p9-10), Statement of Standalone Unaudited Financial Results +
Notes (p11-12).

**No Balance Sheet and no Cash Flow Statement are present in this filing** —
confirmed by full-text sweep (no "Balance Sheet", "Assets", "Liabilities",
"Cash Flow" headers anywhere in the 1088-line extract). This is expected for a
non-annual (Q1) Reg 33 filing, which requires only the results statement, not
balance sheet/cash flow (those are Q4/annual obligations). Recorded here as a
confirmed absence, not a miss.

```
=== A2 COUNT TEST ===
category: notes             grep_count: 12   sweep_count: 12   match: yes
category: note_2_subrows    grep_count: 20   sweep_count: 20   match: yes
category: agenda_items      grep_count: 5    sweep_count: 5    match: yes
category: auditor_paras     grep_count: 10   sweep_count: 10   match: yes
category: entities          grep_count: 2    sweep_count: 2    match: yes
category: line_items        grep_count: 60   sweep_count: 60   match: yes
category: zero_standing     grep_count: 3    sweep_count: 3    match: yes
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes on method:
- `notes`: `grep -n -E "^\s*[0-9]+\.\s"` restricted to the Notes sections only
  (page 8 lines 569-649, page 12 lines 964-1039, primary text, excluding the
  OCR cross-check duplicate blocks) returns 6 + 6 = 12; manual sweep of the
  same ranges confirms 6 numbered notes per column, no unnumbered footnotes
  found below either Notes block. Match.
- `note_2_subrows`: Note 2 (IPO proceeds utilisation) contains two 5-row
  sub-tables (allocation table + utilisation table) per column. Grep on the
  five `Objects` row labels (`Funding capital expenditure`, `Repayment and/or
  prepayment`, `Issue Exoenses`/`Issue Expenses`, `General coroorate
  ourooses`/`General corporate purposes`, `Total`) returns 5 rows x 2
  sub-tables x 2 columns = 20; manual sweep of lines 582-609 (Consolidated)
  and 977-1003 (Standalone) confirms 20. Match.
- `agenda_items`: grep on the covering letter (lines 37-95) for
  `Board Meeting|approved the same|Press Release|Limited Review|website`
  returns 5 distinct disclosure lines; manual sweep confirms the same 5 items
  and finds no additional agenda items (no AGM notice, dividend, director
  appointment/resignation, auditor change, scrutinizer, ESOP grant, or
  capital-raising resolution anywhere in the extract). Match — this is a
  single-substantive-item board meeting (results only).
- `auditor_paras`: grep on `^\s*[0-9]+\.` restricted to each auditor report
  body (Consolidated lines 261-367, Standalone lines 708-793) returns 6 and 4
  numbered paragraphs respectively = 10; manual sweep confirms the same
  numbering. **Not** included in this count: an unlabeled block of text in
  the Consolidated report (lines 343-349) that Para 5 explicitly cross-refers
  to as "paragraph 7 below" (line 323) but which carries no "7." marker in
  the extract — flagged separately below (`MISSING_PARA_NUMBER`) rather than
  folded into the reconciled count, to keep the grep/sweep definitions
  identical (both count only explicitly numbered paragraphs).
- `entities`: grep for subsidiary names (line 304-305) returns 2; manual
  sweep of auditor para 6(a)/(b) (reviewed subsidiary + subsidiary reviewed by
  other auditor) also totals 2. Match.
- `line_items`: manual full-text sweep (Read tool, full 385-500 and 813-905
  ranges) counts 32 Consolidated + 28 Standalone = 60 data-bearing Statement
  of Results rows (excluding section headers "1. Income:", "2. Expenses:",
  "6. Tax expenses", "8. OCI", "(A)/(B)" sub-headers, which are structural,
  not data rows). A first grep pass on data-row keywords under-counted
  Consolidated at 30/32 because the OCR text layer renders "Non Controlling"
  as "Non Controlhng" (h/i substitution) on both NCI rows — the keyword regex
  had to be corrected to match the OCR variant before grep and sweep
  reconciled. This mismatch-then-correction is itself evidence for why the
  manual sweep is mandatory on these OCR'd pages; final grep_count of 60 above
  uses the corrected keyword set. Standalone matched at 28 on the first pass
  (OCR is cleaner on that column).
- `zero_standing`: identified by comparing the row's own value against the
  arithmetic identity of adjacent totals across all 4 periods. 3 rows are nil
  in all 4 periods (see zero_standing flag column below).
- `signature_blocks`: grep for `DIN:|UDIN|Digitally signed|Partner` plus
  manual sweep of the 5 sign-off points in the document (1 covering-letter CS
  signature, 2 MD sign-offs on results — Consolidated and Standalone, 2
  auditor sign-offs — Consolidated and Standalone reports). Match.

---

## 1. Notes to Results — Consolidated (page 8)

| # | Line(s) | First ~15 words | Flags |
|---|---|---|---|
| 1 | 571 | "The unaudited consolidated financial results of the Group for the Quarter ended June 30, 2026 have been reviewed..." — Audit Committee review + Board approval July 23, 2026 + Limited Review confirmation | |
| 2 | 577-609 | "The utilisation of the IPO proceeds in relation to fresh issue is summarised below" — two sub-tables (allocation + utilisation), see section 1a below | NUMBER_FIDELITY (table values, see 1a) |
| 3 | 611-612 | "The Company only has a single business segment i.e. business of Security & variable data Printing..." — single reportable segment, Ind AS 108 | |
| 4 | 616-618 | "The financial results have been prepared in accordance with the Companies (Indian Accounting Standards) Rules, 2015..." — basis of preparation, Reg 33, SEBI circular July 5 2016 | |
| 5 | 620-621 | "The figures of Quarter ended 31st March 2026 are balancing figures between the audited figures..." — Q4 derived as balancing figure vs 9M published | |
| 6 | 625 | "The figures for the corresponding previous period have been regrouped/rearranged/recasted/wherever necessary for the purpose of comparison." | |

### 1a. Note 2 — IPO Proceeds Utilisation, Consolidated — sub-table rows

Table A (Objects x Pre-IPO Proceeds / IPO Proceeds / Amount per offer doc), lines 582-595:
| Line(s) | Object | Pre-IPO (Rs Mn) | IPO Proceeds (Rs Mn) | Offer doc total (Rs Mn) | Flags |
|---|---|---|---|---|---|
| 587-589 | Funding capex — expansion of existing manufacturing units | - | 1,979.13 | 1,979.13 | |
| 590-592 | Repayment/prepayment of outstanding borrowings | 700.02 | 2,299.98 | 3,000.00 | |
| 593 | Issue Expenses | 41.34 | 309.28 | 350.62 | |
| 594 | General corporate purposes | 458.61 | 211.64 | 670.25 | |
| 595 | Total | 1,199.97 | 4,800.03 | 6,000.00 | |

Table B (Objects x Offer doc / As-at-beginning / During quarter / As-at-end / Unutilised), lines 597-609:
| Line(s) | Object | Offer doc (A) | Begin qtr (B) | During qtr (C) | End qtr (B+C) | Unutilised (A-B-C) | Flags |
|---|---|---|---|---|---|---|---|
| 602-603 | Funding capex — expansion | 1,979.13 | 550.56 | 67.65 | 618.21 | 1,360.92 | |
| 604-606 | Repayment/prepayment of borrowings | 3,000.00 | 3,000.00 | - | 3,000.00 | - | ZERO_STANDING (nil "during quarter" and "unutilised" — fully utilised in a prior period) |
| 607 | Issue Expenses | 350.62 | 293.03 | 39.05 | 332.08 | 18.54 | |
| 608 | General corporate purposes | 670.25 | 211.61 | 137.30 | 348.91 | 321.34 | |
| 609 | Total | 6,000.00 | 4,055.20 | 244.00 | 4,299.20 | 1,700.80 | |

OCR cross-check for both tables: lines 654-678. No material numeric divergence found vs primary on visual comparison, but cross-check text is fragmentary (garbled cell alignment); flag NUMBER_FIDELITY as a caution for A3/A4 to re-verify the Table B "During qtr" / "Unutilised" columns against the primary reading above.

## 2. Notes to Results — Standalone (page 12)

| # | Line(s) | First ~15 words | Flags |
|---|---|---|---|
| 1 | 967-968 | "The unaudited standalone financial results of the Company for the Quarter ended June 30, 2026 have been reviewed..." — Audit Committee + Board approval, Limited Review confirmed | |
| 2 | 973-1003 | "The utilisation of the IPO proceeds in relation to fresh issue is summarised below" — two sub-tables, see section 2a | NUMBER_FIDELITY |
| 3 | 1005-1006 | "The Company only has a single business segment i.e. business of Security & variable data Printing..." | |
| 4 | 1010-1012 | "The financial results have been prepared in accordance with the Companies (Indian Accounting Standards) Rules, 2015..." | |
| 5 | 1015-1016 | "The figures of Quarter ended 31st March 2026 are balancing figures between the audited figures..." | |
| 6 | 1020 | "The figures for the corresponding previous period have been regrouped/rearranged/recasted/wherever necessary for the purpose of comparison." | |

### 2a. Note 2 — IPO Proceeds Utilisation, Standalone — sub-table rows

Table A, lines 977-991: identical Rs figures to Consolidated Table A (983-991) — Funding capex (1,979.13 offer doc), Repayment (700.02/2,299.98/3,000.00), Issue Expenses (41.34/309.28/350.62), General corporate purposes (458.61/211.64/670.25), Total (1,199.97/4,800.03/6,000.00). Standalone-vs-Consolidated IPO utilisation figures are identical because the IPO was raised at the Company (standalone) level and the Consolidated statement simply carries the same disclosure — no gap.

Table B, lines 993-1003: Funding capex (1,979.13/550.56/67.65/618.21/1,360.92), Repayment (3,000.00/3,000.00/-/3,000.00/- → ZERO_STANDING on "during qtr"/"unutilised", same as Consolidated), Issue Expenses (350.62/293.03/39.05/332.08/18.54), General corporate purposes (670.25/211.61/137.30/348.91/321.34), Total (6,000.00/4,055.20/244.00/4,299.20/1,700.80). Standalone-vs-Consolidated gap: **none** on Note 2 — figures match exactly between columns, as expected for an IPO-proceeds note that applies to the listed entity, not the Group.

OCR cross-check: lines 1041-1088. Same NUMBER_FIDELITY caution as Consolidated Note 2.

## 3. Board Outcome / Covering Letter — Agenda & Disclosure Items (page 1)

| # | Line(s) | Item | Flags |
|---|---|---|---|
| 1 | 52-54, 68 | Board approved Unaudited Financial Results (Standalone AND Consolidated) for quarter ended June 30, 2026 — single combined resolution, one board meeting | |
| 2 | 55-57 | Press Release on the Consolidated Financial Results enclosed (per Reg 33) | |
| 3 | 57-58 | Statutory Auditors (Vatsaraj & Co.) conducted Limited Review of the Financial Results; both reports (Consolidated + Standalone) enclosed | |
| 4 | 60-61 | Information to also be made available on Company website (URL given) | |
| 5 | 63 | Board Meeting timing: commenced 05:45 p.m., concluded 07:00 p.m. — 1 hr 15 min meeting | |

No other agenda items found anywhere in the extract: no AR/AGM approval, no AGM notice, no record date, no dividend declaration, no director appointment/resignation, no auditor (re)appointment, no scrutinizer appointment, no ESOP grant, no capital-raising enabling resolution. This reads as a single-item (results-only) board meeting.

## 4. Auditor Report Paragraphs — Consolidated Limited Review (Vatsaraj & Co., pages 5-6)

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 270-276 | Introduction — reviewed Statement of Consolidated Unaudited Financial Results of the Parent + 2 Subsidiaries ("the Group"), quarter ended June 30 2026 | |
| 2 | 278-284 | Management's responsibility statement — prepared per Ind AS 34, Companies Act s.133, Reg 33 | |
| 3 | 286-300 | Basis of review — SRE 2410, moderate assurance (not audit-level assurance, no audit opinion expressed); also SEBI circular procedures under Reg 33(8) performed | |
| 4 | 302-306 | Entity list — Statement includes results of 2 Subsidiaries: Rite Infotech Private Limited, Atoll Solutions Private Limited | |
| 5 | 322-328 | Opinion / conclusion — unmodified (nothing came to attention that Statement not prepared per Ind AS 34 / not disclosed per Reg 33) — this paragraph explicitly cross-refers to "paragraph 7 below" (line 323) | NUMBER_FIDELITY — forward reference to a "paragraph 7" that carries no numeric marker anywhere later in the text |
| 6 | 330-349 | Other Matters — sub-item (a) 1 subsidiary reviewed by this auditor (revenue Rs 2.65 Mn, net loss Rs(2.15) Mn, TCI Rs(2.11) Mn); sub-item (b) 1 subsidiary NOT reviewed by this auditor, reviewed by other auditor instead (revenue Rs 18.10 Mn, PAT Rs 0.77 Mn, TCI Rs 0.74 Mn) — reliance on other auditor's report per SA 600 equivalent; conclusion not modified in respect of this matter | ENTITY unaudited-by-primary-auditor disclosure |
| (unnumbered) | 343-349 | "The interim financial information of this entity has been reviewed by other auditor... conclusion... based solely on the report of such other auditor... Our conclusion on the Statement is not modified in respect of this matter." — this block is the substantive content that Para 5 calls "paragraph 7," but carries no "7." label in the extracted text | MISSING_PARA_NUMBER — flagged for A3/A4; either a source-document drafting/numbering gap or an OCR-dropped numeral; does not change the substantive conclusion but is a documentation-quality flag on the auditor's own report |
| sig | 351-362 | Signature block: For Vatsaraj & Co., CA Jwalant S Buch, Partner, M.No. 039033, UDIN illegible in OCR ("1GC:!>30°5"5L'f'KQ)(Z. °TLtOC)"), Mumbai, 23 July 2026 | UDIN_ILLEGIBLE — not one of A1's flagged OCR pages (5/6 were not re-OCR'd since they are auditor-report text pages, not financial-statement table pages), so no cross-check reading exists for this UDIN; A3/A4 should treat the UDIN as NOT FOUND / illegible rather than transcribe the garbled string |

Opinion type: unmodified/unqualified conclusion (Limited Review, not audit). No Emphasis of Matter paragraph. No Going Concern language present anywhere in either auditor report.

## 5. Auditor Report Paragraphs — Standalone Limited Review (Vatsaraj & Co., pages 9-10)

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 718-724 | Introduction — reviewed Statement of Unaudited Standalone Financial Results of the Company, quarter ended June 30 2026 | |
| 2 | 726-733 | Management's responsibility statement — Ind AS 34, Companies Act s.133, Reg 33 | |
| 3 | 735-747 | Basis of review — SRE 2410, moderate assurance, no audit opinion expressed | |
| 4 | 766-774 | Opinion/conclusion — unmodified (nothing came to attention that Statement not prepared per Ind AS / not disclosed per Listing Regulations) | |
| sig | 777-788 | Signature block: For Vatsaraj & Co., CA Jwalant S Buch, Partner, M.No. 039033, UDIN illegible in OCR ("2b0°!>9033 TLKVWV'-155'-i"), Mumbai, 23 July 2026 | UDIN_ILLEGIBLE — same caveat as Consolidated (page 10 not in A1's re-OCR set) |

Standalone report has no Other Matters paragraph and no entity list (no subsidiaries at standalone level) — 4 paragraphs is structurally complete for a single-entity SRE 2410 review, not a miss. No Emphasis of Matter, no Going Concern language.

## 6. Consolidation Entity List

| # | Line | Entity | Relationship | Reviewed by primary auditor? | Flags |
|---|---|---|---|---|---|
| 1 | 304 | Rite Infotech Private Limited | Subsidiary of Parent | One of the two subsidiaries — per para 6(a)/(b) allocation, cannot be determined from the extract WHICH named subsidiary is the reviewed one vs the other-auditor one; names are not individually tied to the (a)/(b) split in the text | NUMBER_FIDELITY / ENTITY — name-to-review-status mapping not explicit in source text, A3/A4 should not assume an order |
| 2 | 305 | Atoll Solutions Private Limited | Subsidiary of Parent | Same caveat as above | same |

No prior-quarter ledger was supplied for this run (prior-quarter ledger path not provided), so ENTITY_CHANGE cannot be evaluated this cycle — flagged as a gap for A3/A4 to source Q4FY26 or Q1FY26 entity list for comparison. Total entities in Group per para 1 (line 273): "two Subsidiaries" — consistent with the 2 names given.

## 7. Statement of Results Line Items — Consolidated (page 7, lines 385-500)

All 4 columns are: Q1FY27 (Jun 30 2026, Unaudited) | Q4FY26 (Mar 31 2026, Audited) | Q1FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited, full year). Primary-text line cited; OCR cross-check block is lines 501-567 for every row below — NUMBER_FIDELITY is flagged wherever the primary text shows OCR corruption (missing decimals/separators) severe enough that a reader could misstate the value without the cross-check.

| # | Line(s) | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 387 | Revenue from Operations | 3,764.70 | 4,041.76 | 3,108.73 | 14,41 1 35 (primary) / **14,411.35** (OCR xcheck, line 511) | NUMBER_FIDELITY — primary FY26 figure corrupted, use OCR reading |
| 2 | 389 | Other Income | 70.97 | 60 65 (primary) / **60.65** (OCR, 513) | 23.42 | 145.78 | NUMBER_FIDELITY |
| 3 | 392 | Total Income | 3,835.67 | 4,102.41 | 3,132.15 | 14,557.13 | |
| 4 | 397-398 | Cost of Materials Consumed | 2,283.14 | 2,255 20 (primary) / **2,255.20** (OCR, 517) | 1,818.58 | 8,03316 (primary) / **8,033.16** (OCR, 517) | NUMBER_FIDELITY |
| 5 | 399-400 | Purchases of Stock-in-trade | 8.32 | 14 57 / **14.57** | 11.50 | 54.53 | NUMBER_FIDELITY |
| 6 | 401-402 | Change in inventories of Finished goods, WIP, Stock-in-trade | -95.05 | -124 53 / **-124.53** | -105.36 | -272 26 / **-272.26** | NUMBER_FIDELITY |
| 7 | 405-406 | Employee Benefit Expenses | 175 35 / **175.35** | 193 44 / **193.44** | 149 75 / **149.75** | 69584 / **695.84** | NUMBER_FIDELITY |
| 8 | 407-408 | Finance Cost | 18 44 / **18.44** | 2909 / **29.09** | 7764 / **77.64** | 208 79 / **208.79** | NUMBER_FIDELITY |
| 9 | 409-410 | Depreciation and amortization (OCR of header: "Oeprecaatton") | 107 80 / **107.80** | 97 46 / **97.46** | 11020 / **110.20** | 44215 / **442.15** | NUMBER_FIDELITY |
| 10 | 411-412 | Other Expenses | 519.80 | 518 78 / **518.78** | 520.10 | 2,104.97 | NUMBER_FIDELITY |
| 11 | 415 | Total Expenses | 3,017.80 | 2,984.01 | 2,582.41 | 11,267.18 | |
| 12 | 418-419 | Profit before exceptional items and tax (1-2) | 817.87 | 1,118.40 | 549.74 | 3,289 95 / **3,289.95** | NUMBER_FIDELITY |
| 13 | 421-422 | Exceptional items | - (nil) | 0.23 | - (nil) | -2.51 | NUMBER_FIDELITY (partial-nil: nil in both June columns, populated only in Mar'26 and FY26 — not a full ZERO_STANDING since 2 of 4 periods are non-zero) |
| 14 | 424-425 | Profit before tax for the period/year (3-4) | 817.87 | 1,118.63 | 549.74 | 3,287.44 | |
| 15 | 429-430 | Current year (tax) | 21387 / **213.87** | 272 40 / **272.40** | 163.27 | 834 49 / **834.49** | NUMBER_FIDELITY |
| 16 | 431-432 | Deferred tax | 1.16 | 5.90 | 18.08 | 28.98 | |
| 17 | 433-434 | Tax Adjustments of Earlier Years | - (nil) | 21 57 / **21.57** | 0.00 | 25.84 | |
| 18 | 436 | Total Tax Expenses | 215.03 | 299.87 | 181.35 | 889.31 | |
| 19 | 439-440 | Profit for the period/year (5-6) [pre-NCI, first "7."] | 602.84 | 818.76 | 368.39 | 2,398.13 | DUPLICATE_LINE_NUMBER — labeled "7." same as row 21 below; this is a source-document numbering repeat (both instances literally printed "7."), not an extraction artifact |
| 20 | 441-442 | Add/(Less) Share of Non Controlling Interest [PAT] (OCR: "Non Controlhng") | 0.52 | -0 89 / **-0.89** | - (nil) | 1 97 / **1.97** | NUMBER_FIDELITY |
| 21 | 443-444 | Profit for the period/year (5-6) [post-NCI, second "7." — this is the reported Consolidated PAT figure quoted in the Press Release, 603.4 Mn] | 603.36 | 817.87 | 368.39 | 2,400.10 | DUPLICATE_LINE_NUMBER (see row 19) |
| 22 | 450-451 | Remeasurements of defined benefit plan | 7.82 | 14.00 | -3.89 | 366 (primary) / **3.66** (OCR, 543) | NUMBER_FIDELITY |
| 23 | 453-454 | Equity instrument through Other Comprehensive Income (OCR: "thrQUllh") | 0.00 (only value visible; other 3 periods show no digits at all) | — | — | — | ZERO_STANDING — line reads nil/0.00 across all 4 periods; template line retained for when equity-instrument fair-value movements occur |
| 24 | 455-456 | Income tax relating to items no (i & ii) above | -1.95 | -3.52 | 0.98 | -0 92 / **-0.92** | NUMBER_FIDELITY |
| 25 | 458-461 | Fair Value change on Cashflow hedge | 0.00 | 0.00 | -1.02 (primary garbled as "_,02" at line 458-459; OCR xcheck line 550 reads "-1.02") | 1.02 (primary garbled; OCR reads "1,02"/"1.02") | NUMBER_FIDELITY — primary text materially illegible on this cell, OCR cross-check is the only legible reading, record both per A1 instruction |
| 26 | 462-464 | Income tax relating to items that will be reclassified to P&L (OCR: "De reclassified") | 0.00 | 0.00 | 0.26 | 026 (primary) / **0.26** (OCR, 552) | NUMBER_FIDELITY |
| 27 | 466-467 | Total Other Comprehensive Income (OCI), net off tax [pre-NCI] (OCR of label: "Othor") | 5.87 | 10.48 | ·3.67 (primary, likely -3.67) / **-3.67** (OCR consistent) | 1.98 | NUMBER_FIDELITY |
| 28 | 469-470 | Add/(Less) Share of Non Controlling Interest [OCI] | -0.01 | -0.01 (duplicated across lines 469 and 471 in primary layout) | - (nil) | -002 (primary) / **-0.02** (OCR) | NUMBER_FIDELITY |
| 29 | 472-473 | Total Other Comprehensive Income (OCI), net off tax [post-NCI] | 5.86 | 10.47 | -3.67 | 1.96 | |
| 30 | 476-477 | Total Comprehensive Income for the period/year (7+8) | 609.22 | 828.34 | 364.72 | 2,402.06 | |
| 31 | 485, 490, 499 | EPS — (a) Basic (Face value Rs 10, not annualised) | 3.73 | 5.06 | 2.50 | 15.45 | |
| 32 | 500 | EPS — (b) Diluted | 3.73 | 5.06 | 2.50 | 15.45 | |

Note: Basic = Diluted EPS in every period (no dilutive instruments outstanding) — consistent, not a flag.

## 8. Statement of Results Line Items — Standalone (page 11, lines 813-905)

Same 4-column structure. OCR cross-check block: lines 910-961. Standalone text is materially cleaner than Consolidated (fewer garbled cells) but the same page-level flag applies per A1.

| # | Line(s) | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 815 | Revenue from Operations | 3,762.15 | 4,041.01 | 3,108.73 | 14,405.58 | |
| 2 | 817 | Other Income | 70.86 | 60.33 | 23.04 | 144.56 | |
| 3 | 820 | Total Income (primary shows "3,833,01" — comma where decimal expected) | 3,833.01 | 4,101.34 | 3,131.77 | 14,550.1 4 (primary, likely 14,550.14) | NUMBER_FIDELITY — both the Q1FY27 and FY26 cells show punctuation corruption; cross-check block (line 921 area) does not repeat the Total Income row explicitly, so this total should be independently re-footed by A3/A4 from Revenue + Other Income (3,762.15+70.86=3,833.01, confirms Q1FY27 reading) |
| 4 | 825 | Cost of Materials Consumed (OCR of label: "Cosl") | 2,280.48 | 2,256.37 | 1,818.58 | 8,029.63 | |
| 5 | 827 | Purchases of Stock-in-trade | 8.32 | 14.57 | 11.50 | 54.53 | |
| 6 | 828-829 | Change in inventories of Finished goods, WIP, Stock-in-trade | -94.94 | -124.63 | -105,36 (primary, comma) / **-105.36** | -272.15 | NUMBER_FIDELITY |
| 7 | 832 | Employee Benefit Expenses | 166.09 | 184.62 | 142.27 | 653.49 | |
| 8 | 834 | Finance Cost | 18.42 | 32.52 | 77.64 | 208.77 | |
| 9 | 836 | Depreciation and amortization (OCR: "amort,zation") | 107.21 | 96.80 | 110.11 (primary) vs **110.14** (OCR xcheck line 928) | 440.14 | NUMBER_FIDELITY — primary and OCR disagree on Q1FY26 (110.11 vs 110.14), record both, do not resolve |
| 10 | 838 | Other Expenses | 514.57 | 511 70 / **511.70** | 529.36 | 2,105 96 / **2,105.96** | NUMBER_FIDELITY |
| 11 | 841 | Total Expenses | 3,000.15 | 2,971.95 | 2,584.10 | 11,220.37 | |
| 12 | 844 | Profit before exceptional items and tax (1-2) | 832.86 | 1,129.39 | 547.67 | 3,329 77 / **3,329.77** | NUMBER_FIDELITY |
| 13 | 847 | Exceptional Items | - (nil) | - (nil) | - (nil) | - (nil) | ZERO_STANDING — confirmed nil across all 4 periods; Profit before tax (row 14) equals Profit before exceptional items and tax (row 12) exactly in every column, arithmetically confirming nil exceptional items throughout |
| 14 | 850 | Profit before tax for the period/year (3-4) | 832.86 | 1,129.39 | 547.67 | 3,329.77 | |
| 15 | 855 | Current year (tax) | 213.50 | 271 .30 / **271.30** | 162.80 | 831 .80 / **831.80** | NUMBER_FIDELITY |
| 16 | 857 | Deferred tax | 1.91 | 11 .28 / **11.28** | 18.11 | 35.16 | NUMBER_FIDELITY |
| 17 | 859 | Tax Adjustments of Earlier Years | 0.00 | 21.19 | 0.00 | 25.46 | note: 0.00 in Q1FY27 and Q1FY26 only, non-zero in Q4FY26/FY26 — partial-nil, not full ZERO_STANDING |
| 18 | 861-862 | Total Tax Expenses | 215.41 | 303.77 | 180.91 | 892.42 | |
| 19 | 865 | Profit for the period/year (5-6) — this is the reported Standalone PAT | 617.45 | 825.62 | 366.76 | 2,437.35 | |
| 20 | 872-873 | Remeasurements of defined benefit plan | 7.84 | 14.08 | -3.93 | 3.79 | |
| 21 | 875-876 | Equity Instrument through Other Comprehensive Income | 0.00 (only value visible; other 3 periods show no digits) | — | — | — | ZERO_STANDING — same pattern as Consolidated row 23 |
| 22 | 878 | Income tax relating to items no (i & ii) above | -1 .97 / **-1.97** | -3 .54 / **-3.54** | 0.99 | -0.95 | NUMBER_FIDELITY |
| 23 | 882 | Fair Value change on Cashflow hedge | 0.00 | 0.00 | -1 .02 / **-1.02** | -1 .02 / **-1.02** | NUMBER_FIDELITY (minor — value legible in primary here, unlike the Consolidated equivalent) |
| 24 | 884-885 | Income tax relating to items that will be reclassified to P&L | 0.00 | 0.00 | 0.26 | 0.26 | |
| 25 | 887 | Total Other Comprehensive Income (OCI), net off tax | 5.87 | 10.54 | -3.70 | 2.08 | |
| 26 | 890-891 | Total Comprehensive Income for the period/year (7-8) | 623.32 | 836.16 | 363.06 | 2,439.43 | |
| 27 | 902-903 | EPS — (a) Basic (Face value Rs 10, not annualised) | 3.82 | 5.10 | 2.48 | 15.70 | |
| 28 | 904-905 | EPS — (b) Diluted | 3.82 | 5.10 | 2.48 | 15.70 | |

Standalone-vs-Consolidated gap on the Statement of Results (first-class metric per protocol): Consolidated has 4 extra rows that Standalone structurally lacks — the two "Share of Non Controlling Interest" rows (PAT-level and OCI-level) and the resulting duplicate "7." / dual-total presentation (pre-NCI and post-NCI). This is the expected structural difference for a Group with non-wholly-owned subsidiaries and is not itself a flag. Revenue gap: Consolidated Revenue from Operations (3,764.70) exceeds Standalone (3,762.15) by 2.55 Mn in Q1FY27 — consistent with the 2 subsidiaries' combined revenue of Rs 2.65 Mn + Rs 18.10 Mn = Rs 20.75 Mn contributed at Group level, net of intercompany eliminations (2.55 Mn net addition implies ~18.2 Mn of intercompany elimination against the 20.75 Mn gross subsidiary revenue — a computation for A3/A4 to verify, not resolved here).

## 9. Signature / Sign-off Blocks

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | 68-78 | Manali Siddharth Shah | Company Secretary and Compliance Officer | Digitally signed 2026.07.23, 19:21:19 +05'30' | Board Meeting concluded 07:00 p.m. (19:00) per line 63 — signature at 19:21:19 is 21 minutes AFTER meeting conclusion; normal sequencing, not a red flag |
| 2 | 629-649 | Pragnyat Lalwani | Managing Director, DIN 01870792 | Date: 23rd July 2026, Place: Mumbai (no time stamp given on the results-statement signature block itself) | |
| 3 | 351-362 | CA Jwalant S Buch | Partner, Vatsaraj & Co., M.No. 039033, Firm Regn 111327W | Mumbai, 23rd July 2026 | UDIN_ILLEGIBLE (see section 4) |
| 4 | 1024-1039 | Pragnyat Lalwani | Managing Director, DIN 01870792 | Date: 23rd July 2026, Place: Mumbai | DIN consistent with row 2 (same signatory both statements) |
| 5 | 777-788 | CA Jwalant S Buch | Partner, Vatsaraj & Co., M.No. 039033, Firm Regn 111327W | Mumbai, 23rd July 2026 | UDIN_ILLEGIBLE (see section 5); same partner signs both Consolidated and Standalone reports |

---

## Flags raised — summary

- **ZERO_STANDING** (3 standing-nil line items across all 4 periods): Consolidated OCI "Equity instrument through OCI" (item 23); Standalone Exceptional Items (item 13); Standalone OCI "Equity Instrument through OCI" (item 21). Plus 1 Note-2 sub-row: Consolidated/Standalone Note 2 Table B "Repayment of borrowings" — nil during-quarter movement and nil unutilised balance (fully utilised in a prior quarter).
- **NUMBER_FIDELITY** (pervasive on pages 7/8/11/12 per A1's instruction; individually flagged above at ~25 cells): primary pdftotext layer vs tesseract OCR cross-check readings differ or primary is illegible; both readings recorded, none resolved by A2.
- **DUPLICATE_LINE_NUMBER**: Consolidated Statement of Results labels two distinct rows "7." (pre-NCI and post-NCI Profit for the period) — source-document numbering, not an extraction error.
- **MISSING_PARA_NUMBER**: Consolidated auditor report Para 5 cross-refers to "paragraph 7 below" but no paragraph in the extracted text carries a "7." marker; the substantive content (lines 343-349) appears to be the referenced material but is unlabeled.
- **UDIN_ILLEGIBLE**: both auditor UDIN numbers (Consolidated report line 361, Standalone report line 787) are OCR-garbled on pages (6, 10) that were NOT in A1's re-OCR set (only 7/8/11/12 were cross-checked) — no independent reading exists; treat as NOT FOUND, do not attempt to reconstruct.
- **ENTITY** (mapping gap): the 2 named subsidiaries (Rite Infotech Private Limited, Atoll Solutions Private Limited) are not individually tied to the "(a) reviewed by us" / "(b) not reviewed by us" split in auditor para 6 — cannot determine which entity is which without further source (management letter, prior filings).
- No **ENTITY_CHANGE** evaluable — no prior-quarter ledger was provided to this run.
- No Emphasis of Matter, Other Matters (beyond the one subsidiary-reliance clause), or Going Concern language in either auditor report.
- No Balance Sheet, no Cash Flow Statement in this filing (expected for Q1, not Q4/annual).
