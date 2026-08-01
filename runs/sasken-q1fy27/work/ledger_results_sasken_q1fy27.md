# COMPLETENESS LEDGER — SASKEN Q1FY27 (Results, Reg 33 filing)
Source extract: `/home/user/inflection-pipeline/runs/sasken-q1fy27/work/extract_results_sasken_q1fy27.txt` (57 pages, line-numbered spine, 2092 lines incl. header/coverage proof)
Enumerator: A2 | Prior-quarter ledger: NOT PROVIDED (no path given in task inputs) — entity/slide diffs vs prior quarter cannot be computed; flagged `NO_PRIOR_LEDGER`.

```
=== A2 COUNT TEST ===
category: notes_consolidated    grep_count: 3    sweep_count: 3    match: yes
category: notes_standalone      grep_count: 3    sweep_count: 3    match: yes
category: notes_total (primary) grep_count: 6    sweep_count: 6    match: yes
category: footnotes_unnumbered  grep_count: 10   sweep_count: 10   match: yes   (2 OCR-artifact "*" fragments at lines 251, 296 excluded — verified as seal/stamp OCR noise, not footnotes, see NOTE below)
category: auditor_paras         grep_count: 3    sweep_count: 3    match: yes   (2 consol "Other Matters" + 1 standalone "Other Matter"; 0 KAM, 0 EOM — confirmed absent by grep)
category: line_items_consol_PL  grep_count: 36   sweep_count: 36   match: yes
category: line_items_stand_PL   grep_count: 27   sweep_count: 27   match: yes
category: segment_lines_consol  grep_count: 17   sweep_count: 17   match: yes   (initial naive regex returned 16 — missed the all-dash "Inter segment revenue" row because dashes sit mid-row, not alone on a line; corrected pattern + manual re-sweep both converge on 17, re-swept before emission per GATE A2 rule)
category: newspaper_extract_lines grep_count: 19  sweep_count: 19  match: yes
category: line_items_TOTAL      grep_count: 99   sweep_count: 99   match: yes  (36+27+17+19)
category: agenda_items          grep_count: 1    sweep_count: 1    match: yes  (keyword sweep for approv/resolved/record date/dividend/appointment/AGM/auditor/ESOP/scrutinizer on cover letter returns only "taken on record" — single-item board meeting)
category: group_entities        grep_count: 13   sweep_count: 13   match: yes  (matches A1 header's explicit "13 entities" cross-check)
category: slides                grep_count: 32   sweep_count: 32   match: yes  ([page N] markers N=26..57)
category: digital_signatures    grep_count: 10   sweep_count: 10   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

NOTE on footnote exclusions: lines 251 and 296 in the extract (`* i,` / `* ,`) are OCR debris from the auditor-report seal/signature block on OCR pages 4 and 5 (see A1 header ocr_reason), not real footnotes. Included in the raw regex hit list, excluded from the reconciled count of 10 after manual verification against page context.

---

## SECTION 1 — NOTES TO FINANCIAL RESULTS: CONSOLIDATED (page 9)
| # | Line(s) | Subject (first ~15 words) | Flags |
|---|---------|---------------------------|-------|
| 1 | 454-458 | Basis of preparation: Ind AS per Sec 133 Companies Act 2013 + Companies (Ind AS) Rules 2015 | |
| 2 | 460-463 | Board approval July 31, 2026; statutory auditors expressed unmodified opinion on consolidated results | |
| 3 | 465-474 | Segment Reporting basis: CEO identified as CODM per Ind AS 108; two segments — Software Services & Product Solutions | |

## SECTION 2 — NOTES TO FINANCIAL RESULTS: STANDALONE (page 14)
| # | Line(s) | Subject (first ~15 words) | Flags |
|---|---------|---------------------------|-------|
| 1 | 689-692 | Basis of preparation: Ind AS per Sec 133 Companies Act 2013 + Companies (Ind AS) Rules 2015 | |
| 2 | 694-696 | Board approval July 31, 2026; statutory auditors expressed unmodified opinion on standalone results | |
| 3 | 698-700 | Segment info per Ind AS 108 provided on consolidated basis only; NOT separately given in standalone | **NOTE_ABSENT_ONE_SIDE** — standalone explicitly declines to disclose segment data (structural difference, see Flags Summary) |

**Reconciliation, Notes population:** grep `^\s*[0-9]+\.\s` restricted to notes sections (lines 452-476, 686-702) = 6; manual sweep of both Notes blocks = 6. MATCH. (A raw whole-file run of the same regex returns 10 hits total — the extra 4 are 2 consolidated "Other Matters" auditor-report paragraphs [lines 285, 305, ledgered separately in Section 3] and 2 EPS sub-item rows inside the newspaper-extract table item 8 [lines 750-751, ledgered in Section 7]. These are correctly excluded from the Notes population — documented, not silently dropped.)

## SECTION 3 — AUDITOR REPORT PARAGRAPHS: KAM / EMPHASIS OF MATTER / OTHER MATTER
| # | Report | Type | Line(s) | Subject | Flags |
|---|--------|------|---------|---------|-------|
| 1 | Consolidated (MSKA & Associates LLP) | Other Matters, para 1 | 285-293 | Step-down subsidiary (unnamed here — see Section 9 entity list) audited by other auditor: revenue Rs 6,543.83 lakhs, PAT Rs 64.71 lakhs, TCI Rs 103.46 lakhs for Q1FY27; opinion relies on other auditor's report, unmodified | OTHER_AUDITOR_RELIANCE |
| 2 | Consolidated | Other Matters, para 2 | 305-310 | Q4FY26 comparative is a balancing figure (audited FY26 less audited 9M-FY26 per Ind AS 34); opinion not modified | BALANCING_FIGURE_COMPARATIVE |
| 3 | Standalone (MSKA & Associates LLP) | Other Matter (singular) | 611-617 | Same balancing-figure explanation for standalone Q4FY26 comparative; opinion not modified | BALANCING_FIGURE_COMPARATIVE |
| — | Consolidated | Key Audit Matter | n/a | NOT PRESENT — confirmed absent by grep (`key audit matter` zero hits) | ZERO_STANDING (structural — Reg 33 quarterly review format carries no KAM section) |
| — | Consolidated | Emphasis of Matter | n/a | NOT PRESENT — confirmed absent by grep | ZERO_STANDING |
| — | Standalone | KAM / EOM | n/a | NOT PRESENT — confirmed absent by grep | ZERO_STANDING |
| — | Both | Going Concern material uncertainty | n/a | NOT PRESENT — only boilerplate going-concern responsibility language (lines 208-212, 550-553), no material uncertainty flagged | ZERO_STANDING |

Opinion type both reports: unmodified/unqualified (stated explicitly in Note 2 of each Notes block, Section 1/2 above, and implicit in the Opinion paragraphs, lines 127-168 consol / 499-512 standalone).
UDIN consolidated: 26130795ZCEBGP2244 (line 322). UDIN standalone: 26130795LMTNII2250 (line 628). Partner both reports: Deepak Khatri, Membership No. 130795 (lines 318-321, 625-627).
Entities reviewed by other auditor: 1 step-down subsidiary (unnamed in Other Matter text; cross-check against Section 9 entity list — total revenue Rs 6,543.83 lakhs points to Borqs China per scale, but the extract does not itself name the entity in the Other Matter paragraph — **NOT FOUND** by name in this paragraph, flag **ENTITY_NAME_NOT_IN_OTHER_MATTER_PARA**).

## SECTION 4 — STATEMENT OF FINANCIAL RESULTS LINE ITEMS: CONSOLIDATED (page 7, lines 338-383) — Rs. in lakhs
Columns: Q1FY27 | Q4FY26 | Q1FY26 | FY26
| Sl | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|----|------|-----------|--------|--------|--------|------|-------|
| I | 338 | Revenue from operations | 33,923.85 | 33,402.41 | 27,353.07 | 111,316.84 | |
| II | 339 | Other income | 967.18 | 1,533.20 | 760.42 | 3,870.42 | |
| III | 340 | Total income (I+II) | 34,891.03 | 34,935.61 | 28,113.49 | 115,187.26 | |
| IV | 341 | EXPENSES (header) | — | — | — | — | header row, no own value |
| | 342 | Cost of materials consumed | 8,982.53 | 8,493.28 | 7,557.08 | 23,734.49 | |
| | 343 | Changes in inventories of finished goods and WIP | 151.17 | 63.62 | (515.66) | (232.57) | |
| | 344 | Employee benefits expense | 17,497.91 | 17,039.49 | 14,878.79 | 63,117.87 | |
| | 345 | Finance costs | 144.43 | 75.11 | 106.71 | 400.42 | |
| | 346 | Depreciation and amortization expense | 1,077.65 | 1,031.82 | 916.72 | 3,900.24 | |
| | 347 | Other expenses | 4,080.25 | 4,489.54 | 3,968.60 | 15,853.73 | |
| | 348 | Total expenses (IV) | 31,933.94 | 31,192.86 | 26,912.24 | 106,774.18 | |
| V | 349 | Profit before exceptional items and tax (III-IV) | 2,957.09 | 3,742.75 | 1,201.25 | 8,413.08 | |
| VI | 350-351 | Exceptional items — Impact of labour code | - | - | - | 830.80 | **ZERO_STANDING** in all three quarter columns; only FY26 populated |
| VII | 352 | Profit before tax (V-VI) | 2,957.09 | 3,742.75 | 1,201.25 | 7,582.28 | |
| VIII | 353 | Tax expense: | 604.94 | 842.56 | 200.68 | 1,717.71 | |
| | 354 | (1) Current tax | 965.18 | 753.62 | 697.26 | 2,590.02 | |
| | 355 | (2) Deferred tax | (360.24) | 88.94 | (496.58) | (872.31) | |
| IX | 356 | Profit after tax (VII-VIII) | 2,352.15 | 2,900.19 | 1,000.57 | 5,864.57 | |
| X | 357 | Other comprehensive income (OCI) | (182.29) | 2,233.51 | (152.70) | 4,681.61 | |
| | 358 | (A) Items not reclassified to P&L (header) | — | — | — | — | header |
| | 359 | (i) Remeasurement of defined benefit plans | (25.66) | (657.36) | (63.66) | (617.11) | |
| | 360 | (ii) Equity instruments through OCI | 15.45 | (36.46) | 22.58 | 161.00 | |
| | 361-362 | (iii) Income tax relating to (A) items | (3.76) | 195.80 | 2.85 | 115.85 | |
| | 363 | (B) Items subsequently reclassified to P&L (header) | — | — | — | — | header |
| | 364 | (i) Effective portion gain/(loss) on hedging instruments, cash flow hedges | 626.37 | (600.74) | (24.53) | (740.20) | |
| | 365 | (ii) Debt instruments through OCI | (33.15) | (47.76) | 120.99 | (8.18) | |
| | 366-367 | (iii) Exchange differences translating foreign operations | (610.63) | 3,223.55 | (186.52) | 5,585.70 | present in consol only — see Section 5 structural diff |
| | 368 | (iv) Income tax relating to (B) items | (150.91) | 156.48 | (24.41) | 184.55 | |
| XI | 369-370 | Total comprehensive income (IX+X) | 2,169.86 | 5,133.70 | 847.87 | 10,546.18 | |
| | 371-372 | Profit attributable to: Owners of the company | 2,485.99 | 2,698.90 | 944.00 | 5,392.97 | |
| | 373 | Profit attributable to: Non-controlling interests | (133.84) | 201.29 | 56.57 | 471.60 | |
| | 374 | (subtotal, = IX) | 2,352.15 | 2,900.19 | 1,000.57 | 5,864.57 | |
| | 375-376 | Total comprehensive income attributable to: Owners of the company | 2,297.19 | 4,927.11 | 791.42 | 10,067.39 | |
| | 377 | Total comprehensive income attributable to: Non-controlling interests | (127.33) | 206.59 | 56.45 | 478.79 | |
| | 378 | (subtotal, = XI) | 2,169.86 | 5,133.70 | 847.87 | 10,546.18 | |
| XII | 379 | Paid up equity share capital (FV Rs 10) | 1,518.65 | 1,518.65 | 1,512.16 | 1,518.65 | |
| XIII | 380 | Other equity* | (blank) | (blank) | (blank) | 83,956.37 | **ZERO_STANDING** — blank in all quarter columns, populated only in FY26 (annual balance-sheet-date figure; footnote: excl. NCI) |
| XIV | 381 | Earnings per equity share** (header) | — | — | — | — | header |
| | 382 | (1) Basic | 16.37 | 17.79 | 6.24 | 35.61 | |
| | 383 | (2) Diluted | 16.32 | 17.72 | 6.21 | 35.43 | |

36 numeric-bearing rows (count-test population). Signed by Rajiv C Mody, Chairman MD & CEO, digitally 2026-07-31 17:58:59 (line 388-394).

## SECTION 5 — STATEMENT OF FINANCIAL RESULTS LINE ITEMS: STANDALONE (page 13, lines 643-684) — Rs. in lakhs
| Sl | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|----|------|-----------|--------|--------|--------|------|-------|
| I | 643 | Revenue from operations | 15,548.08 | 14,467.62 | 11,834.38 | 53,252.20 | |
| II | 644 | Other income | 1,392.10 | 807.75 | 1,101.60 | 3,727.89 | |
| III | 645 | Total income (I+II) | 16,940.18 | 15,275.37 | 12,935.98 | 56,980.09 | |
| IV | 646 | EXPENSES (header) | — | — | — | — | header; **no "Cost of materials consumed" / "Changes in inventories" lines** — structural diff, see Flags Summary |
| | 647 | Employee benefits expense | 10,676.54 | 10,698.16 | 9,843.86 | 40,823.52 | |
| | 648 | Finance costs | 60.65 | 47.16 | 47.16 | 181.16 | |
| | 649 | Depreciation and amortization expense | 309.45 | 277.76 | 283.56 | 1,091.82 | |
| | 650 | Other expenses | 2,249.31 | 1,757.06 | 1,690.72 | 6,293.53 | |
| | 651 | Total expenses (IV) | 13,295.95 | 12,780.14 | 11,865.30 | 48,390.03 | |
| V | 652 | Profit before exceptional items and tax (III-IV) | 3,644.23 | 2,495.23 | 1,070.68 | 8,590.06 | |
| VI | 653-654 | Exceptional items — Impact of labour code | - | - | - | 457.30 | **ZERO_STANDING** in quarter columns |
| VII | 655 | Profit before tax (V-VI) | 3,644.23 | 2,495.23 | 1,070.68 | 8,132.76 | |
| VIII | 656 | Tax expense: | 758.65 | 521.43 | 153.52 | 1,665.89 | |
| | 657 | (1) Current tax | 749.60 | 518.73 | 458.28 | 2,004.07 | |
| | 658 | (2) Deferred tax | 9.05 | 2.70 | (304.76) | (338.18) | |
| IX | 659 | Profit after tax (VII-VIII) | 2,885.58 | 1,973.80 | 917.16 | 6,466.87 | |
| X | 660 | Other comprehensive income (OCI) | 444.49 | (1,030.93) | 84.50 | (908.96) | |
| | 661 | A) Items not reclassified (header) | — | — | — | — | header |
| | 662 | (i) Remeasurement of defined benefit plans | (0.51) | (704.93) | (13.00) | (629.77) | |
| | 663 | (ii) Equity instruments through OCI | 15.45 | (36.46) | 22.58 | 161.00 | |
| | 664-665 | (iii) Income tax relating to (A) items | (3.76) | 202.48 | 2.87 | 123.64 | |
| | 666 | B) Items reclassified subsequently (header) | — | — | — | — | header |
| | 667 | (i) Effective portion gain/(loss) hedging instruments, cash flow hedges | 617.37 | (600.74) | (24.53) | (740.20) | |
| | 668 | (ii) Debt instruments through OCI | (33.15) | (47.76) | 120.99 | (8.18) | |
| | 669-670 | (iii) Income tax relating to (B) items | (150.91) | 156.48 | (24.41) | 184.55 | **no "exchange differences" sub-line** — standalone has only 3 items under (B) vs 4 in consolidated (no foreign-operations translation line; single-entity, no subsidiaries to translate) — structural diff |
| XI | 671-672 | Total comprehensive income (IX+X) | 3,330.07 | 942.87 | 1,001.66 | 5,557.91 | **no owners/NCI attribution breakdown** — standalone is a single legal entity, no NCI possible — structural diff |
| XII | 673 | Paid up equity share capital (FV Rs 10) | 1,518.65 | 1,518.65 | 1,512.16 | 1,518.65 | |
| XIII | 674 | Other equity | (blank) | (blank) | (blank) | 79,631.02 | **ZERO_STANDING** — blank in quarter columns |
| XIV | 675 | Earnings per equity share* (header) | — | — | — | — | header |
| | 676 | (1) Basic | 19.00 | 13.01 | 6.07 | 42.71 | |
| | 677 | (2) Diluted | 18.94 | 12.96 | 6.03 | 42.48 | |

27 numeric-bearing rows (count-test population). Signed by Rajiv C Mody, digitally 2026-07-31 17:59:49 (line 680-684).

## SECTION 6 — SEGMENT NOTE: CONSOLIDATED (page 8, lines 407-433) — Rs. in lakhs
| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 407-408 | Segment Revenue: a) Software services | 21,955.88 | 20,947.66 | 17,670.10 | 77,246.46 | |
| | 409 | b) Product solutions | 11,967.97 | 12,454.75 | 9,682.97 | 34,070.38 | |
| | 410 | Total | 33,923.85 | 33,402.41 | 27,353.07 | 111,316.84 | |
| 2 | 411 | Less: Inter segment revenue | - | - | - | - | **ZERO_STANDING** — dash in every period, all four columns |
| 3 | 413 | Net Sales/Income from Operations | 33,923.85 | 33,402.41 | 27,353.07 | 111,316.84 | |
| 4 | 415-417 | Segment Results: a) Software Services | 6,729.24 | 5,909.60 | 4,141.13 | 21,027.22 | |
| | 418 | b) Product solutions | 708.12 | 1,599.76 | 872.58 | 2,748.63 | |
| | 419 | Total | 7,437.36 | 7,509.36 | 5,013.71 | 23,775.85 | |
| 5 | 421 | Less: Finance costs | 144.43 | 75.11 | 106.71 | 400.42 | |
| | 422 | Less: Other unallocable expenditure* | 5,303.02 | 5,224.70 | 4,466.17 | 19,663.57 | |
| | 423 | Add: Unallocable other income | 967.18 | 1,533.20 | 760.42 | 3,870.42 | |
| 6 | 424 | Total Profit before tax | 2,957.09 | 3,742.75 | 1,201.25 | 7,582.28 | |
| 7 | 426-429 | Segment assets: Software services | 25,679.53 (as at Jun 30, 2026) | 24,928.16 (as at Mar 31, 2026) | n/a | n/a | only 2 date columns (no Q1FY26/FY26 comparatives for assets — standard, balance-sheet items compared to two dates only) |
| | 430 | Product solutions | 12,831.64 | 5,489.90 | n/a | n/a | |
| | 431 | Total allocable segments assets | 38,511.17 | 30,418.06 | n/a | n/a | |
| | 432 | Unallocable assets | 87,669.68 | 86,191.64 | n/a | n/a | |
| | 433 | Total assets | 126,180.85 | 116,609.70 | n/a | n/a | |

17 numeric-bearing rows (count-test population, reconciled per note above). Segment capital employed: text note (lines 438-442) states asset/liability segregation NOT presented — segments share assets/liabilities interchangeably, allocation deemed impractical. This is itself a disclosure unit: **SEGMENT_CAPITAL_EMPLOYED_NOT_DISCLOSED** (line 440-442).
Standalone segment note: **NOT PRESENT** — standalone Note 3 (Section 2, row 3 above) explicitly states segment info is on consolidated basis only. **NOTE_ABSENT_ONE_SIDE / STRUCTURAL_DIFFERENCE.**

## SECTION 7 — EXTRACT FOR NEWSPAPER PUBLICATION (page 15, lines 722-760, Reg 47(1)(b)) — Rs. in lakhs, CONSOLIDATED basis (items 1-8) + STANDALONE basis (items 9-11, marked **)
| Sl | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|----|------|-----------|--------|--------|--------|------|-------|
| 1 | 727 | Total income from operations | 34,891.03 | 34,935.61 | 28,113.49 | 115,187.26 | |
| 2 | 729-730 | Net Profit/(Loss) before Tax, Exceptional and/or Extraordinary items | 2,957.09 | 3,742.75 | 1,201.25 | 8,413.08 | |
| 3 | 731-732 | Net Profit/(Loss) before tax (after Exceptional and/or Extraordinary items) | 2,957.09 | 3,742.75 | 1,201.25 | 7,582.28 | |
| 4 | 733-734 | Net Profit/(Loss) after tax (after Exceptional and/or Extraordinary items) | 2,352.15 | 2,900.19 | 1,000.57 | 5,864.57 | |
| 5 | 735-736 | Total comprehensive income for the period | 2,169.86 | 5,133.70 | 847.87 | 10,546.18 | |
| | 738-739 | Profit attributable to: Owners of the company | 2,485.99 | 2,698.90 | 944.00 | 5,392.97 | |
| | 740 | Non-controlling interests | (133.84) | 201.29 | 56.57 | 471.60 | |
| | 741 | (subtotal) | 2,352.15 | 2,900.19 | 1,000.57 | 5,864.57 | |
| | 742-743 | TCI attributable to: Owners of the company | 2,297.19 | 4,927.11 | 791.42 | 10,067.39 | |
| | 744 | Non-controlling interests | (127.33) | 206.59 | 56.45 | 478.79 | |
| | 745 | (subtotal) | 2,169.86 | 5,133.70 | 847.87 | 10,546.18 | |
| 6 | 746 | Paid up equity share capital | 1,518.65 | 1,518.65 | 1,512.16 | 1,518.65 | |
| 7 | 747-748 | Reserves (excl. Revaluation Reserve) per audited FY26 balance sheet | - | - | - | 83,956.37 | **ZERO_STANDING** — dash in all quarter columns |
| 8 | 749 | EPS (Rs 10 each) header | — | — | — | — | header |
| | 750 | 1. Basic | 16.37 | 17.79 | 6.24 | 35.61 | |
| | 751 | 2. Diluted | 16.32 | 17.72 | 6.21 | 35.43 | |
| 9 | 752 | Total income ** (standalone) | 16,940.18 | 15,275.37 | 12,935.98 | 56,980.09 | |
| 10 | 753 | Profit before tax ** (standalone) | 3,644.23 | 2,495.23 | 1,070.68 | 8,132.76 | |
| 11 | 754 | Profit after tax ** (standalone) | 2,885.58 | 1,973.80 | 917.16 | 6,466.87 | |
| — | 758-760 | Note: extract is a summary; full format on Stock Exchange/Company websites (Reg 33) | — | — | — | — | standard boilerplate note |

19 numeric-bearing rows (count-test population). Signed Rajiv C Mody, digitally 2026-07-31 18:00:24 (line 763-767).

## SECTION 8 — BOARD OUTCOME AGENDA ITEMS (cover letter, page 1, lines 62-119)
| # | Line(s) | Agenda item | Flags |
|---|---------|-------------|-------|
| 1 | 75, 78-79 | Approval / taking on record of Standalone and Consolidated audited financial results for quarter ended June 30, 2026 | Sole substantive board resolution in this letter |

Board meeting timing: **11:30 am to 4:15 pm** (line 75) = 4 hours 45 minutes.
Confirmed ABSENT from this letter (checked by keyword sweep, zero hits): AR/Annual Report approval, AGM notice, record date fixing, dividend declaration, director appointment/resignation, auditor appointment/change, scrutinizer appointment, ESOP grant, capital-raising enabling resolution. **SINGLE_ITEM_AGENDA** — this is a results-only board outcome letter; no other corporate actions bundled into this filing.
Enclosures listed (documents, not separate agenda items): Auditor's Report (standalone + consolidated) [line 83-85], Media release [line 86], Communication to Analysts [line 87]. Also referenced: Reg 47(1)(b) newspaper-extract publication commitment [lines 89-93] (a disclosure consequence, not a board resolution).
Signatory: Paawan Bhargava, Company Secretary, digitally signed 2026-07-31 18:01:07 (lines 102-108) — signed AFTER all financial-statement and auditor signatures (see Section 10), consistent sequencing, no flag.

## SECTION 9 — CONSOLIDATED GROUP ENTITY LIST (page 2, OCR, lines 136-153)
| # | Line | Entity name (as OCR'd) | Relationship | Flags |
|---|------|------------------------|--------------|-------|
| 1 | 139 | Sasken Communication Technologies Mexico S.A. de C.V ('Sasken Mexico') | Subsidiary | trailing "*" marker in OCR text — possible footnote reference not resolved elsewhere in extract; **OCR_UNCERTAIN_MARKER** |
| 2 | 140 | Sasken Finland Oy. ('Sasken Finland') | Subsidiary | |
| 3 | 141 | Sasken Silicon Technologies Private Limited | Subsidiary | |
| 4 | 142 | Sasken Inc. ('Sasken USA') | Subsidiary | |
| 5 | 143 | Sasken Silicon Inc. | Step-down Subsidiary | |
| 6 | 144 | Sasken Technologies Japan Corporation ('Sasken Japan') | Subsidiary | |
| 7 | 145 | Sasken Design Solutions Pte. Ltd ('Sasken Singapore') | Subsidiary | |
| 8 | 146 | Borqs International Holding Corp (Cayman Island) [OCR: "Borgs"] | Step-down Subsidiary | OCR renders "Borqs" as "Borgs" throughout this block — cross-checked against clean-text-layer pages (e.g. line 866, 891, 1060 "Borqs") confirming correct spelling is Borqs; **OCR_SPELLING_VARIANT**, not a distinct entity |
| 9 | 147 | New Borqs Technologies (Beijing) Company, Ltd. (China) [OCR: "New Borgs"] | Step-down Subsidiary | same OCR spelling note |
| 10 | 148 | BORQS Technologies (HK) Limited (Hong Kong) | Step-down Subsidiary | |
| 11 | 149 | Borqs Technologies India Private Limited [OCR: "Borgs"] | Step-down Subsidiary | same OCR spelling note |
| 12 | 150 | Sasken Employees Welfare Trust | Controlled Trust | |
| 13 | 151 | Sasken Foundation | Controlled Trust | |

13 entities total (matches A1 header's explicit cross-check statement "13 entities" and the Other Matters para's single-entity reliance disclosure in Section 3). Additional OCR fragment at line 152 ("pec Under liquidation process") could not be resolved to a specific entity in this extract — **OCR_UNCERTAIN_FRAGMENT**, flagged for A3 to check against the source PDF image if material (possibly a status qualifier on one of rows 8-11, given Borqs group restructuring context elsewhere in the document, but NOT FOUND as attributable to a named row in this text).
No prior-quarter entity list available for diff — **NO_PRIOR_LEDGER**, `ENTITY_CHANGE` cannot be assessed this cycle.

## SECTION 10 — DIGITAL SIGNATURE BLOCKS (all documents)
| # | Line(s) | Signatory | Designation | Timestamp (2026-07-31) | Document | Flags |
|---|---------|-----------|-------------|------------------------|----------|-------|
| 1 | 312-324 | Deepak Khatri (MSKA & Associates LLP) | Partner, Membership 130795 | 16:23:35 IST | Consolidated Auditor's Report | UDIN 26130795ZCEBGP2244; signed after board meeting end (16:15) — consistent |
| 2 | 618-630 | Deepak Khatri (MSKA & Associates LLP) | Partner, Membership 130795 | 16:20:54 IST | Standalone Auditor's Report | UDIN 26130795LMTNII2250; signed after board meeting end — consistent |
| 3 | 388-394 | Rajiv C Mody | Chairman, MD & CEO | 17:58:59 IST | Consolidated Financial Results (P&L page) | |
| 4 | 446-450 | Rajiv C Mody | Chairman, MD & CEO | 17:59:16 IST | Consolidated Segment Note | |
| 5 | 480-490 | Rajiv C Mody | Chairman, MD & CEO | 17:59:32 IST (date only shown; time inferred from block sequence) | Consolidated Notes page | DIN 00092037 |
| 6 | 680-684 | Rajiv C Mody | Chairman, MD & CEO | 17:59:49 IST | Standalone Financial Results (P&L page) | |
| 7 | 706-716 | Rajiv C Mody | Chairman, MD & CEO | 18:00:06 IST | Standalone Notes page | DIN 00092037 |
| 8 | 763-767 | Rajiv C Mody | Chairman, MD & CEO | 18:00:24 IST | Newspaper Extract | |
| 9 | 1258-1265 | Rajiv C Mody (Rajiv C. Mody) | Chairman, MD & CEO | 18:00:43 IST | Communication to Analysts sign-off | |
| 10 | 102-108 | Paawan Bhargava | Company Secretary | 18:01:07 IST | Cover letter to BSE/NSE | Last signature in sequence |

All 10 signature timestamps fall AFTER the stated board meeting end time (4:15 pm / 16:15), in a coherent sequence: auditors (~16:20-16:24) → CEO across all financial documents (~17:59-18:00) → Company Secretary cover letter (18:01). No `PREMATURE_SIGNATURE` flag warranted.

## SECTION 11 — INVESTOR PRESENTATION SLIDES (pages 26-57, lines 1272-2006)
| Page | Line | Title/Subject | Content type | Quant data? | Flags |
|------|------|----------------|--------------|-------------|-------|
| 26 | 1272 | Cover: "SASKEN TECHNOLOGIES LTD. INVESTOR PRESENTATION Q1 FY2026-27" | title/divider | No | sparse by design (A1 header) |
| 27 | 1284 | Safe Harbor Clause (forward-looking statements disclaimer) | text/legal | No | |
| 28 | 1306 | Section divider: "PERFORMANCE HIGHLIGHTS Q1 FY2026-27" | divider | No | sparse by design |
| 29 | 1316 | Message from Management — Rajiv C Mody (Chairperson, MD & CEO) quote | text/quote | No | |
| 30 | 1339 | Message from Management — Priyaranjan (CFO) quote | text/quote | **Yes** | inline: revenue ₹3,392M +24.0% YoY, EBITDA margin 9.5% (+411bps YoY), PAT +135.1% YoY to ₹235M |
| 31 | 1361 | Message from Management — Hareesh Ramanna (President, Borqs India) quote | text/quote | No | |
| 32 | 1384 | Business Highlights summary tiles (5 tiles) | tiles/text | **Yes** | revenue ₹3,392M, EBITDA ₹321M/9.5% margin, 60x4x3 (93 accounts, 6 $4M+, top-5 56%), utilization 85%, headcount 2,658, attrition 9.8%, order book $47.1M |
| 33 | 1417 | Quarter at a Glance — KPI tiles | tiles/chart | **Yes** | Revenue ₹3,392M, EBITDA ₹321M, EBIT ₹213M, PAT ₹235M, orders $47.1M, EBITDA margin 9.5%, LTM attrition 9.8%, utilization 85.1% |
| 34 | 1438 | Financial Performance Snapshot — Revenue/EBIT/PBT/PAT quarterly trend charts (₹M) | chart | **Yes** | 3-quarter trend, QoQ/YoY % growth annotated |
| 35 | 1468 | Key Revenue Breakdowns — by delivery, project type, geography (%) | chart | **Yes** | Onsite/Offshore, T&M/Fixed Price/Product, NA/EMEA/India/APAC % |
| 36 | 1497 | Segmental Results — revenue/gross profit split by segment (₹Mn), growth, gross margin % | chart/table | **Yes** | duplicate-basis figures to Section 4/6 statutory segment note, but in ₹M presentation-basis, unaudited |
| 37 | 1520 | Order Book Summary — TCV, TCV-new, ACV, order book mix ($M) | chart | **Yes** | |
| 38 | 1551 | Major Order Wins (8 bullet descriptions) | text list | No | qualitative only, no $ figures on this slide |
| 39 | 1584 | People and Process Updates (bullets: headcount, awards, learning, offices, ISO, DEI) | text list | **Yes** | headcount 2,658, gross adds 340, attrition 9.8%, 72 employees trained |
| 40 | 1614 | Section divider: "60x4x3 STRATEGY & THE ROADMAP" | divider | No | sparse by design |
| 41 | 1624 | Our Strategy to Accelerate Growth — 60x4x3 framework explainer | text/diagram | No | framework description, no period figures |
| 42 | 1663 | Tracking 60x4x3 Progress — customer break-up by LTM sales, client concentration % | chart | **Yes** | active base 93 (69 <$1M, 18 $1-4M, 6 $4M+), top-5 56%, top-10 69% |
| 43 | 1686 | Section divider: "FINANCIALS Q1 FY 2026-27" | divider | No | sparse by design |
| 44 | 1695 | Income Statement Summary — Consolidated (function-wise), ₹M | table | **Yes** | full P&L in ₹M with % of revenue and QoQ/YoY growth columns |
| 45 | 1721 | Income Statement Summary — Consolidated Nature-wise, ₹M | table | **Yes** | full P&L, nature-of-expense basis |
| 46 | 1748 | Balance Sheet Summary — Consolidated, ₹M, Jun 30 2026 vs Mar 31 2026 | table | **Yes** | Assets and Liabilities/Equity, two-date comparison only |
| 47 | 1773 | Key Metrics — employee/hiring/attrition/utilization table | table | **Yes** | 3-quarter comparison |
| 48 | 1803 | Section divider: "PEOPLE, ESG & AWARDS Q1 FY 2026-27" | divider | No | sparse by design |
| 49 | 1813 | Participation in Industry Events (5 logos/events) | text/logos | No | |
| 50 | 1833 | Awards Q1 (5 awards listed) | text list | No | |
| 51 | 1858 | Our Commitment to Society (ESG) — E/S/G topic headers | text list | No | topic headers only, no metrics on this slide |
| 52 | 1884 | Snapshot of ESG Achievements — metric tiles (9 tiles) | tiles | **Yes** | 86% GHG reduction, 100% power/lighting, 9,560 KL wastewater, 8,000 KL rainwater, 0 wage disputes, 13,089 students, 1,081 students in skill program, 0% data/cyber breach, 0 disasters, 99% patch compliance |
| 53 | 1916 | Section divider: "ABOUT SASKEN" | divider | No | sparse by design |
| 54 | 1922 | Sasken at a Glance — company facts tiles (8 tiles) | tiles | **Yes** | 37+ years, 90+ clients, 200+ patents, 32M+ devices, 2,658 headcount, 4.5 CSAT |
| 55 | 1945 | Key Offerings — service line / vertical tiles | tiles | No | category list only |
| 56 | 1962 | Global Presence & Compliance — locations map, certifications | map/list | **Yes** (minor) | "5 Continents (23 Countries)" |
| 57 | 2001 | Closing "THANK YOU" slide | divider | No | sparse by design |

32 slides total. 7 section-divider slides (26, 28, 40, 43, 48, 53, 57 — matches A1 header's explicit sparse-page list). 16 slides carry quantitative data; 16 do not.
No prior-quarter deck available for diff — `DROPPED_SLIDE` cannot be assessed this cycle (**NO_PRIOR_LEDGER**).

## SECTION 12 — FOOTNOTES / UNNUMBERED NOTES (all documents, manual + grep sweep)
| # | Line | Document/Table | Footnote text | Flags |
|---|------|----------------|----------------|-------|
| 1 | 384 | Consolidated P&L | "*excluding non-controlling interests" (qualifies Other Equity row XIII) | |
| 2 | 389 | Consolidated P&L | "**EPS is not annualized for the quarter June 30, 2026, March 31, 2026 and June 30, 2025." | |
| 3 | 435 | Consolidated Segment Note | "* All expenses which are not attributable or allocable to segments or non-recurring in nature have been disclosed as unallocable expenses." | |
| 4 | 678 | Standalone P&L | "* EPS is not annualized for the quarter ended June 30, 2026, March 31, 2026 and June 30, 2025." | |
| 5 | 755 | Newspaper Extract | "* EPS is not annualized for the quarter ended June 30, 2026, March 31, 2026 and June 30, 2025." | |
| 6 | 756 | Newspaper Extract | "** information pertains to Sasken Technologies Limited on a standalone basis." (qualifies items 9-11) | |
| 7 | 758-760 | Newspaper Extract | "Note: The above is an extract... full format... available on the website of the Stock Exchange(s) and the Company." | Reg 33/47 boilerplate |
| 8 | 1479 | Investor Presentation, p.35 | "*Onsite includes US, Europe, Japan, Finland, China" | |
| 9 | 1546 | Investor Presentation, p.37 | "1 Includes new and renewal bookings" (qualifies Total Contract Value chart) | |
| 10 | 1984 | Investor Presentation, p.56 | "* Both development center & hardware capabilities" (India map annotation) | |

10 footnotes (reconciled, see count-test block). Excludes 2 OCR-artifact fragments (lines 251, 296) verified as seal/stamp noise, not disclosure content.

---

## FLAGS SUMMARY (list only, not interpreted)

**ZERO_STANDING rows (6):**
1. Consolidated P&L — "Impact of labour code" (Exceptional items), line 351 — zero in Q1FY27/Q4FY26/Q1FY26, populated only FY26 (830.80)
2. Consolidated P&L — "Other equity*", line 380 — blank in all quarter columns, populated only FY26 (83,956.37)
3. Consolidated Segment Note — "Less: Inter segment revenue", line 411 — dash in all four columns
4. Standalone P&L — "Impact of labour code" (Exceptional items), line 654 — zero in quarter columns, populated only FY26 (457.30)
5. Standalone P&L — "Other equity", line 674 — blank in all quarter columns, populated only FY26 (79,631.02)
6. Newspaper Extract — "Reserves (excluding Revaluation Reserve)", line 747 — dash in all quarter columns, populated only FY26 (83,956.37)

**Notes/line items present in one of standalone/consolidated but not the other:**
- Consolidated Note 3 (segment reporting, full detail) vs Standalone Note 3 (explicitly states segment info is NOT separately provided, consolidated basis only) — lines 465-474 vs 698-700
- Consolidated P&L carries "Cost of materials consumed" and "Changes in inventories of finished goods and WIP" (lines 342-343) — standalone P&L has neither (standalone is services-only; product/materials activity sits in subsidiaries)
- Consolidated OCI section (B) has 4 sub-items including "(iii) Exchange differences in translating financial statements of foreign operations" (lines 366-367) — standalone OCI section (B) has only 3 sub-items, no translation line (single entity, no foreign subsidiaries to translate)
- Consolidated P&L carries Owners/NCI attribution breakdown for both Profit and TCI (lines 371-378) — standalone P&L has no such breakdown (single entity, no NCI)
- Consolidated Segment Note (full table, page 8) — standalone has no equivalent statutory segment note at all (see Section 6)

**Line items present this quarter but absent (blank/dash) in a comparative column:** all 6 ZERO_STANDING rows above are simultaneously "absent in comparative column" cases — see that list; no additional rows found with this pattern beyond the six.

**Structural differences, standalone vs consolidated (rollup):**
- Segment reporting: full note (consolidated) vs none (standalone, by explicit note)
- P&L expense structure: materials/inventory lines (consolidated only)
- OCI structure: foreign-currency translation sub-line (consolidated only)
- NCI: attribution rows present (consolidated) vs absent (standalone, no subsidiaries)
- Reserves/Other equity FY26 balances differ in absolute value (83,956.37 consolidated vs 79,631.02 standalone) as expected given consolidation of subsidiary equity

**Other flags raised:**
- `OTHER_AUDITOR_RELIANCE` — one step-down subsidiary audited by another auditor, consolidated opinion relies on their report (Section 3, item 1); entity not named in the Other Matter paragraph itself (**ENTITY_NAME_NOT_IN_OTHER_MATTER_PARA**, NOT FOUND by name in this text)
- `BALANCING_FIGURE_COMPARATIVE` — Q4FY26 comparative in both consolidated and standalone is an unaudited-in-isolation balancing figure per Ind AS 34 (Section 3, items 2-3)
- `OCR_SPELLING_VARIANT` — "Borqs" rendered "Borgs" throughout the OCR'd entity list (page 2); confirmed correct spelling via clean text-layer pages elsewhere
- `OCR_UNCERTAIN_MARKER` / `OCR_UNCERTAIN_FRAGMENT` — trailing "*" on Sasken Mexico row (line 139) and unresolved fragment "pec Under liquidation process" (line 152) in the OCR'd entity table; not resolved to a specific entity within this extract
- `SINGLE_ITEM_AGENDA` — Board Outcome letter carries exactly one substantive resolution (results approval), no other corporate actions this quarter
- `NO_PRIOR_LEDGER` — no prior-quarter ledger path was supplied to this run; `ENTITY_CHANGE` and `DROPPED_SLIDE` comparisons could not be performed

---

```yaml
stage: A2-enumerator
company: "SASKEN"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/sasken-q1fy27/work/ledger_results_sasken_q1fy27.md"
counts:
  notes: 6
  line_items: 99
  zero_standing: 6
  agenda_items: 1
  auditor_paras: 3
  entities: 13
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 32
  slide_numbers: 32
flags_raised: [ZERO_STANDING, STRUCTURAL_DIFFERENCE, OTHER_AUDITOR_RELIANCE, ENTITY_NAME_NOT_IN_OTHER_MATTER_PARA, BALANCING_FIGURE_COMPARATIVE, OCR_SPELLING_VARIANT, OCR_UNCERTAIN_MARKER, OCR_UNCERTAIN_FRAGMENT, SINGLE_ITEM_AGENDA, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
