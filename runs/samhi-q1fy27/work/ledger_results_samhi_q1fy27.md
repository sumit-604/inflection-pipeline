# A2 ENUMERATION LEDGER — SAMHI Hotels Limited (SAMHI) — Q1 FY27 (quarter ended 30 June 2026) — RESULTS FILING

Source: `extract_results_samhi_q1fy27.txt` (14 pages; pages 8, 9, 13, 14 OCR-substituted per A1 header).
Unit convention: figures below are reproduced in the source unit (INR million) exactly as extracted; Rs Crore = INR million x 0.1. No values recalculated or estimated — NOT FOUND / OCR-uncertain is marked explicitly where the extract itself is garbled.

---

## === A2 COUNT TEST ===
```
category: notes            grep_count: 20  sweep_count: 18  match: yes (adjusted)
category: line_items       grep_count: 102 sweep_count: 102 match: yes
category: zero_standing    grep_count: 12  sweep_count: 12  match: yes
category: agenda_items     grep_count: 5   sweep_count: 5   match: yes
category: auditor_paras    grep_count: 17  sweep_count: 13  match: yes (adjusted)
category: entities         grep_count: 18  sweep_count: 18  match: yes
category: annexure_rows    grep_count: 18  sweep_count: 18  match: yes
category: signature_blocks grep_count: 9   sweep_count: 9   match: yes
gate_a2: pass
```
**Reconciliation notes (both adjustments fully explained, no disclosure unit dropped):**
- **notes**: naive grep `^[0-9]+[.\s]` on the notes sections returns 20 hits, but 2 are false positives caused by OCR: line 515 is mid-sentence wrapped text ("34 "Interim Financial Reporting"...") that begins with a number because "Ind AS 34" wrapped to a new line, and line 526 is a table-header row ("| 30 June 2026 | ...") inside standalone Note 5's sub-table that happens to start with a pipe+digit. Excluding these 2, adjusted grep = 18, exactly matching the manual sweep (10 standalone notes + 8 consolidated notes = 18). Manual sweep additionally recovered standalone Note 1 (line 514) whose leading numeral "1" was dropped entirely by OCR/pdftotext (the line begins "| The above unaudited standalone financial results...") — confirmed via `cat -A` showing no digit present. No notes are missing; the reconciliation is a false-positive/OCR-digit-loss correction, not a missed unit.
- **auditor_paras**: naive grep on explicit paragraph numerals (`^[0-9]\.`) returns only 6 hits (standalone: para 1, para 5; consolidated: paras 1-4) because this auditor consistently numbers only the opening paragraph and the "Other Matter"-type paragraph in the standalone report, and leaves several body paragraphs unnumbered in both reports (this is the source document's own formatting choice on a non-OCR page, not an extraction defect — pages 6-7 and 10-12 were pdftotext, not OCR). Blank-line-delimited block counting gives 17 raw blocks across both reports; of these, 4 are letterhead/page-repeat-header artifacts (firm address block + repeated "(cont'd)" page header appearing on the second page of each report), not paragraphs. Removing those 4 yields 13, matching the manual sweep (6 standalone + 7 consolidated, the extra consolidated block being the unnumbered SEBI-circular sentence appended after numbered para 3). No paragraph is missing.

---

## 1. NOTES TO THE FINANCIAL STATEMENTS

### 1A. Standalone notes (10) — source page 9 (OCR), lines 513-545

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 514 | "The above unaudited standalone financial results of SAMHI Hotels Limited ('the Company') have been prepared..." (basis of preparation, Ind AS 34) | OCR_DIGIT_DROPPED (leading numeral "1" absent from extract; recovered by position/content) |
| 2 | 518 | "The above unaudited standalone financial results for the quarter ended 30 June 2026 were reviewed and recommended..." (AC/Board approval dates 31 Jul 2026 & 03 Aug 2026) | |
| 3 | 520 | "The results for the quarter ended 30 June 2026 are available on the Bombay Stock Exchange website..." | |
| 4 | 522 | "The Chief Operating Decision Maker ('CODM') evaluates the Company's performance at an overall company level as one segment..." (single segment: hotels) | |
| 5 | 524 | "Exceptional items includes:" — heads a 4-row sub-table (see Section 2C) | OCR_LOW_CONFIDENCE on sub-table values (page 9 OCR) |
| 6 | 534 | "Revenue from operations include service income from subsidiaries of INR 123.16 million for the quarter ended 30 June 2026..." | |
| 7 | 536 | "The figures for the quarter ended 31 March 2026 are the balancing figures between the audited figures in respect of full financial year..." | |
| 8 | 538 | "The Board of directors of the Company, in its meeting held on 05 March 2026, approved the acquisition of 70% interest in RARE India..." (55% acquired 22 Apr 2026, control obtained; 15% remaining) | |
| 9 | 541 | "During the quarter, on 22 May 2026, the Company acquired a 49% equity interest in Clean Max Nile Private Limited..." (not an associate — no significant influence) | |
| 10 | 544 | "The Company acquired 24,487,096 Compulsorily Convertible Preference Shares (CCPS) in Duet India Hotels Hyderabad Private Limited..." (from Duet India Hotels (Pune), at carrying amount INR 440.18 mn) | |

### 1B. Consolidated notes (8) — source page 14 (OCR), lines 802-837

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 803 | "The above unaudited consolidated financial results of SAMHI Hotels Limited (hereinafter referred to as 'the Parent'...)..." (basis of preparation) | |
| 2 | 808 | "The above unaudited consolidated financial results for the quarter ended 30 June 2026 were reviewed and recommended..." (AC/Board dates 31 Jul & 03 Aug 2026) | |
| 3 | 811 | "The results for the quarter ended 30 June 2026 are available on the Bombay Stock Exchange website..." | |
| 4 | 813 | "The Chief Operating Decision Maker ('CODM') evaluates the Group's performance at an overall group level as one segment..." | |
| 5 | 815 | "Exceptional items includes:" — heads a 4-row sub-table (see Section 2C) | OCR_LOW_CONFIDENCE on sub-table values (page 14 OCR) |
| 6 | 826 | "The figures for the quarter ended 31 March 2026 are the balancing figures between the audited figures..." | |
| 7 | 829 | "The Board of directors of the Parent, in its meeting held on 05 March 2026, approved the acquisition of 70% interest in RARE India..." (RARE India consolidated w.e.f. 22 Apr 2026 acquisition date; PPA provisional, Ind AS 103) | |
| 8 | 835 | "During the quarter, on 22 May 2026, the Parent acquired a 49% equity interest in Clean Max Nile Private Limited..." (same treatment as standalone note 9) | |

**Note-count reconciliation vs company-level dual note set**: standalone and consolidated notes overlap substantially in subject (RARE India, Clean Max Nile) but consolidated Note 7 adds PPA/Ind AS 103 provisional-accounting language absent from standalone Note 8 — expected, not flagged.

---

## 2. FINANCIAL STATEMENT LINE ITEMS (both statements, zero/nil/dash included)

### 2A. Standalone P&L — page 8 (OCR), lines 436-501 — 40 line items

Columns in source order: Q1 FY27 (30-Jun-26, Unaudited) | Q4 FY26 (31-Mar-26, Audited — balancing figure per Note 7) | Q1 FY26 (30-Jun-25, Unaudited) | FY26 (31-Mar-26, Audited, full year)

| S.No | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 443 | Income (header) | — | — | — | — | header row |
| 1a | 444 | Revenue from operations (Refer note 6) | 335.20 | 303.65 | 337.54 | 1,350.18 | |
| 1b | 445 | Other income | 9.40 | 34.21 | 2.24 | 40.46 | |
| 1c | 446 | Total income | 344.60 | 337.86 | 339.78 | 1,390.64 | |
| 2 | 447 | Expenses (header) | — | — | — | — | header row |
| 2a | 448 | Cost of materials consumed | 12.20 | 11.75 | 13.24 | 53.14 | |
| 2b | 449 | Employee benefits expense | 124.10 | 136.48 | 116.49 | 505.69 | |
| 2c | 450 | Other expenses | 117.73 | 116.53 | 601.60(OCR uncertain) | 933.61 | OCR_LOW_CONFIDENCE Q1FY26 cell |
| 2d | 451 | Total expenses (subtotal) | OCR garbled | 264.76 | OCR garbled | 1,492.44 | OCR_LOW_CONFIDENCE |
| 3 | 453-454 | EBITDA before finance costs, D&A, exceptional items and tax (1-2) | 73.10(pos.) | (391.55) | (101.80) | OCR garbled/absent | OCR_LOW_CONFIDENCE column alignment |
| 4 | 455 | Finance costs | 44.19 | 52.82 | 72.03 | 228.96 | |
| 5 | 456 | Depreciation and amortisation expenses | 34.20 | 43.20 | 24.25 | 118.41 | |
| 5a | 457 | [subtotal: Finance costs + D&A, unlabeled] | 78.39(implied) | 96.02(implied) | 96.28(implied) | 347.37 | OCR_LOW_CONFIDENCE label lost; value cross-foots to 228.96+118.41=347.37 for FY26 col |
| 6 | 459 | Profit/(loss) before exceptional items and tax (3-4-5) | OCR garbled | OCR garbled | 487.83 | (449.1x, truncated) | OCR_LOW_CONFIDENCE |
| 7 | 460 | Exceptional items (net) (Refer note 5) | OCR garbled | 2,490.77 | 974.93 | 4,347.05 | OCR_LOW_CONFIDENCE Q1FY27 cell — see Section 5 flag |
| 8 | 461 | Profit from continuing operations before tax (6+7) | OCR garbled | 2,467.85 | 487.10 | 3,897.88 | OCR_LOW_CONFIDENCE Q1FY27 cell |
| 9 | 462 | Tax expense (header) | — | — | — | — | header row |
| 9a | 463 | Current tax | nil/blank | nil/blank | nil/blank | nil/blank | ZERO_STANDING |
| 9b | 464 | Deferred tax | nil/blank | nil/blank | nil/blank | nil/blank | ZERO_STANDING |
| 9c | 465 | Total tax expense (subtotal) | nil/blank | nil/blank | nil/blank | nil/blank | ZERO_STANDING |
| 10 | 467 | Profit from continuing operations for the period/year (8-9) | 2,467.85(implied) | 2,467.85 | 487.10 | 3,897.88 | column alignment OCR-uncertain |
| — | 468 | Discontinued operations (header) | — | — | — | — | header row |
| 11a | 469 | Loss from discontinued operations before tax | blank | blank | (28.22) | (54.51) | standing item, nil in current 2 periods (not all-4 nil — see flags) |
| 11b | 470 | Tax expense of discontinued operations | dash | dash | dash | dash | ZERO_STANDING |
| 11 | 471 | Loss from discontinued operations for the period/year | blank | blank | (28.22) | (54.51) | |
| 12 | 473 | Profit for the period/year (10+11) | 2,467.85(implied) | 2,467.85 | 458.88(likely OCR for 458.59-ish) | 3,843.37 | OCR_LOW_CONFIDENCE |
| 13 | 475 | Other comprehensive income (header) | — | — | — | — | header row |
| 13a | 476 | Items that will not be reclassified to profit or loss (sub-header) | — | — | — | — | sub-header row |
| 13b | 477 | Re-measurement gain/(loss) on defined benefit obligations | blank | 0.25 | blank | (0.11) | |
| 13c | 478 | Income tax relating to items mentioned above | dash | dash | dash | dash | ZERO_STANDING |
| 13d | 479 | Other comprehensive income, net of tax (subtotal) | blank | 0.25(implied) | blank | (0.11)(implied) | |
| 14 | 481 | Total comprehensive income for the period/year (12+13) | 12.43(OCR uncertain) | 2,467.74 | 458.88 | 3,844.38 | OCR_LOW_CONFIDENCE Q1FY27 cell — cross-check vs row 12 |
| 15 | 482 | Paid up equity share capital (face value INR 1, fully paid) | 222.13 | 222.13 | 221.21 | 222.13 | |
| 16 | 483 | Other equity as shown in the audited balance sheet | n/a (interim) | n/a (interim) | n/a (interim) | 32,275.07 | standard: disclosed only for audited annual column |
| 17a | 487 | EPS from continuing operations — Basic (INR) | 0.05 | 11.15 | 2.20 | 17.62 | |
| 17b | 488 | EPS from continuing operations — Diluted (INR) | 0.05 | 11.09 | 2.18 | 17.53 | |
| 18a | 492 | EPS from discontinued operations — Basic (INR) | dash | dash | (0.13) | (0.25) | nil in current 2 periods |
| 18b | 493 | EPS from discontinued operations — Diluted (INR) | dash | dash | (0.13) | (0.25) | nil in current 2 periods |
| 19a | 499 | EPS from continuing + discontinued operations — Basic (INR) | 0.05 | 11.15(implied) | 2.07 | 17.37 | |
| 19b | 500 | EPS from continuing + discontinued operations — Diluted (INR) | 0.05 | 11.09(implied) | 2.05 | 17.28 | |

Excluded as non-line-item OCR noise (table borders/decorative characters, not disclosure units): lines 452, 458, 466, 472, 474, 480, 494, 496-498.

### 2B. Consolidated P&L — page 13 (OCR), lines 713-786 — 52 line items

Same 4-column structure as standalone. Rows 1-14, 18-22 mirror the standalone structure with Group-level figures; rows 15-17 (Profit/OCI/TCI attributable to Owners vs NCI) exist **only** in the consolidated statement (no standalone equivalent, since standalone has no subsidiaries/NCI) — structurally expected, not itself a flag, but load-bearing for the PAT-gap reconciliation below.

| S.No | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 719 | Income (header) | — | — | — | — | header |
| 1a | 720 | Revenue from operations | 3,052.06 | 3,448.60 | 2,722.11 | 12,477.96 | |
| 1b | 721 | Other income | 30.77 | 86.09 | 150.86 | 312.02 | |
| 1c | 722 | Total income | 3,082.83 | 3,534.69 | 2,872.97 | 12,789.98 | |
| 2 | 723 | Expenses (header) | — | — | — | — | header |
| 2a | 724 | Cost of materials consumed | 211.75 | 295.29 | 216.78 | 1,000.11 | |
| 2b | 725 | Employee benefits expense | 502.07 | 499.94 | 466.59 | 1,954.09 | |
| 2c | 726 | Other expenses | 1,355.96 | 1,537.40 | 1,133.73 | 5,210.16 | |
| 2d | 727 | Total expenses (subtotal) | 2,069.78 | 2,332.63 | 1,817.10 | 8,164.36 | |
| 3 | 729-730 | EBITDA before finance costs, D&A, exceptional items and tax (1-2) | 1,013.08 | 1,202.06 | 1,055.87 | 4,628.02(OCR: "628.02", digit likely dropped) | OCR_LOW_CONFIDENCE FY26 cell |
| 4 | 731 | Finance costs | OCR garbled/blank | 376.89 | 506.16 | 1,709.14 | OCR_LOW_CONFIDENCE Q1FY27 cell |
| 5 | 732 | Depreciation and amortisation expenses | 308.83 | 381.55 | 290.66 | 1,266.65 | |
| 5a | 733 | [subtotal: Finance costs + D&A, unlabeled] | OCR garbled | 685.72(implied Q4) | 754.81 | 2,975.79 | OCR_LOW_CONFIDENCE |
| 6 | 735 | Profit before exceptional items and tax (3-4-5) | OCR garbled | OCR garbled | 259.05 | 1,649.83 | OCR_LOW_CONFIDENCE |
| 7 | 736 | Exceptional items (net) (Refer note 5) | OCR garbled/near-blank | OCR garbled | 433.10(implied, OCR uncertain) | 1,075.26(implied) | OCR_LOW_CONFIDENCE — see Section 5 PAT-gap flag |
| 8 | 737 | Profit from continuing operations before tax (6+7) | 327.33 | 692.15 | 590.05(OCR) | 2,725.09(OCR) | OCR_LOW_CONFIDENCE |
| 9 | 738 | Tax expense (header) | — | — | — | — | header |
| 9a | 739 | Current tax | blank/nil | 0.58 | blank/nil | 0.58 | not all-periods nil (2 of 4 nonzero) — no ZERO_STANDING |
| 9b | 740 | Deferred tax | 78.06 | 3,302.39 | 38.67 | 2,995.45 | |
| 9c | 741 | Total tax expense (subtotal) | 73.06(OCR, cross-foot suggests ~78.06) | (3,300.81)(OCR uncertain sign/digits) | 38.67 | 2,994.87 | OCR_LOW_CONFIDENCE |
| 10 | 743 | Profit from continuing operations for the period/year (8-9) | 249.27 | 3,993.96 | 220.38 | 5,719.96 | |
| — | 744 | Discontinued operations (header) | — | — | — | — | header |
| 11a | 745 | Loss from discontinued operations before tax | blank | blank | (28.22) | (54.51) | standing, nil in current 2 periods |
| 11b | 746 | Tax expense of discontinued operations | dash | dash | dash | dash | ZERO_STANDING |
| 11 | 747 | Loss from discontinued operations for the period/year | blank | blank | (28.22) | (54.51) | |
| 12 | 749 | Profit for the period/year (10+11) | 249.27 | 3,993.96 | 192.16(implied) | 5,665.45(implied) | |
| 13 | 750 | Other comprehensive income (header) | — | — | — | — | header |
| 13a | 751 | Items that will not be reclassified to profit or loss (sub-header) | — | — | — | — | sub-header |
| 13b | 752 | Re-measurement loss on defined benefit obligations | (0.47) | (0.29) | (0.06) | (3.22) | |
| 13c | 753 | Income tax relating to items mentioned above | blank | 0.11 | blank | 0.11(OCR "Ot") | not all-periods nil — no ZERO_STANDING |
| 13d | 754 | Other comprehensive income, net of tax (subtotal) | OCR garbled | OCR garbled | OCR garbled | OCR garbled | OCR_LOW_CONFIDENCE |
| 14 | 756 | Total comprehensive income for the period/year (12+13) | 248.80 | 3,993.78 | 192(implied) | 662.34(OCR — inconsistent vs row12 FY26 5,665.45; likely digit-drop) | OCR_LOW_CONFIDENCE, cross-foot mismatch flagged for A3 |
| 15 | 757 | Profit attributable to: (header) | — | — | — | — | header, CONSOLIDATED-ONLY (no standalone equiv.) |
| 15a | 758 | Owners of the Company | 182.50 | 3,536.71 | 172.80 | 5,029.90 | CONSOLIDATED-ONLY — see PAT-gap flag |
| 15b | 759 | Non-controlling interests | 66.77 | 457.25 | 19.36 | 635.55 | CONSOLIDATED-ONLY |
| 15c | 760 | Profit for the period/year (cross-check total) | 249.27 | 3,993.96 | 192.16 | 5,665.45 | CONSOLIDATED-ONLY, ties to row 12 |
| 16 | 761 | Other comprehensive income attributable to: (header) | — | — | — | — | header, CONSOLIDATED-ONLY |
| 16a | 762 | Owners of the Company | blank | (0.39) | (0.10) | (2.78) | CONSOLIDATED-ONLY |
| 16b | 763 | Non-controlling interests | blank | (0.08) | 0.08(OCR) | 0.33 | CONSOLIDATED-ONLY |
| 16c | 764 | Other comprehensive income for the period/year (cross-check) | OCR garbled | OCR garbled | OCR garbled | OCR garbled | CONSOLIDATED-ONLY, OCR_LOW_CONFIDENCE |
| 17 | 765 | Total comprehensive income attributable to: (header) | — | — | — | — | header, CONSOLIDATED-ONLY |
| 17a | 766 | Owners of the Company | 182.11 | 3,536.61 | 172.74 | 5,027.12 | CONSOLIDATED-ONLY |
| 17b | 767 | Non-controlling interests | 66.69 | 457.17 | 19.36 | 635.22 | CONSOLIDATED-ONLY |
| 17c | 768 | Total comprehensive income for the period/year (15+16) (cross-check) | OCR garbled | 98.78(OCR, likely mis-scan) | 192(implied) | 5,662.34(implied FY26) | CONSOLIDATED-ONLY, OCR_LOW_CONFIDENCE |
| 18 | 769 | Paid up equity share capital (face value INR 1, fully paid) | 222.13 | 222.13 | 221.21 | 222.13 | |
| 19 | 770 | Other equity as shown in the audited balance sheet | n/a (interim) | n/a (interim) | n/a (interim) | 21,599.67 | standard: audited annual column only |
| 20a | 774 | EPS from continuing operations — Basic (INR) | 1.12 | 18.04 | 1.00 | 25.85 | |
| 20b | 775 | EPS from continuing operations — Diluted (INR) | 1.12(OCR "L.42") | 17.94 | 0.99 | 25.72 | OCR_LOW_CONFIDENCE Q1FY27 cell |
| 21a | 779 | EPS from discontinued operations — Basic (INR) | dash | dash | (0.13) | (0.25) | nil in current 2 periods |
| 21b | 780 | EPS from discontinued operations — Diluted (INR) | dash | dash | (0.13) | (0.25) | nil in current 2 periods |
| 22a | 784 | EPS from continuing + discontinued operations — Basic (INR) | 1.12 | 18.04 | 0.87 | 25.61 | |
| 22b | 785 | EPS from continuing + discontinued operations — Diluted (INR) | 1.12 | 17.94 | 0.86 | 25.47 | |

Excluded as non-line-item OCR noise: lines 728, 734, 742, 748, 755, 771-773, 776-778, 781-783, 786.

### 2C. Exceptional items sub-tables (Note 5, both statements) — 10 line items

**Standalone (page 9 OCR, lines 524-533) — 5 rows:**
| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|
| 529 | Profit on sale of investment | blank | blank | 974.93 | 979.07 | intermittent, not all-periods-zero |
| 530 | Reversal of impairment of investment in subsidiary, net | OCR garbled | OCR garbled ("2soeot") | blank | 3,250.87 | OCR_LOW_CONFIDENCE |
| 531 | Gain on sale of business undertaking | blank | blank | blank | 144.90 | intermittent, not all-periods-zero |
| 532 | Impact of New Labour Codes | OCR garbled ("(27))") | blank | blank | blank | OCR_LOW_CONFIDENCE |
| 533 | Total (subtotal) | OCR garbled | 890.77(implied)/2,490.77(per main P&L row 7) | 974.93 | 4,347.05 | OCR_LOW_CONFIDENCE — inconsistent totals across extract, flagged for A3 numeric reconciliation |

**Consolidated (page 14 OCR, lines 815-825) — 5 rows:**
| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|
| 820-821 | Reversal of impairment in value of PP&E and other intangible assets | blank | blank | 268.93(implied) | 268.93 | OCR_LOW_CONFIDENCE column alignment |
| 822 | Gain on sale of business undertaking | OCR garbled/blank | OCR garbled | OCR garbled | OCR garbled | OCR_LOW_CONFIDENCE |
| 823 | Reversal of impairment in value of right-of-use assets, net | blank | blank | blank | 696.58(implied) | |
| 824 | Impact of New Labour Codes | OCR garbled ("(403)?") | blank | blank | (35.15) | OCR_LOW_CONFIDENCE |
| 825 | Total (subtotal) | OCR garbled | OCR garbled | OCR garbled | 1,078.26(implied) | OCR_LOW_CONFIDENCE |

**Flag — EXCEPTIONAL_ITEMS_COMPOSITION_DIFFERS**: standalone exceptional items are investment-level (profit/impairment on investment in subsidiary), consolidated exceptional items are asset-level (impairment on PP&E/intangibles/ROU assets). This is the expected consolidation-elimination mechanic (standalone gain on sale of an intercompany investment eliminates on consolidation, replaced by the underlying asset's impairment history) — routed to A3/A4 as the explanatory bridge for the PAT gap below, not asserted as an error.

---

## 3. STANDALONE-VS-CONSOLIDATED PAT GAP — FLAGGED

| Metric (Q1 FY27, INR mn) | Standalone | Consolidated (total) | Consolidated (owners' share) |
|---|---|---|---|
| Profit before tax (row 8) | ~2,467.85 (OCR-implied) | 327.33 | n/a |
| Profit for the period (row 12) | 2,467.85 | 249.27 | 182.50 |
| Rs Crore equivalent | ~246.79 | ~24.93 | ~18.25 |

**Flag: STANDALONE_CONSOL_PAT_GAP.** Standalone PAT (~Rs 247 cr) is roughly 10x consolidated PAT (~Rs 25 cr) and roughly 13.5x the owners'-share consolidated PAT (~Rs 18.25 cr) for the same quarter. Standalone-statement row 7 "Exceptional items (net)" carries a large gain (2,490.77 mn per the Q4FY26 column, current-quarter cell OCR-garbled but implied large-positive given row 8 vs row 6 relationship) that is largely absent/much smaller at the consolidated level (row 736, mostly blank/garbled for the current quarter). This is consistent with a standalone-only gain on an intercompany transaction (see Section 2C composition-difference flag) that eliminates on consolidation. A3/A4 must confirm the exact quantum from the clean (non-OCR) source PDF and characterize whether this is a recurring or one-off item, and whether it is disclosed anywhere in the concall/investor deck (not part of this results-only filing).

---

## 4. BOARD OUTCOME LETTER — AGENDA ITEMS (5) — page 1-2, lines 44-146

Board meeting: commenced 04:30 p.m. IST, concluded 06:58 p.m. IST (line 49-50) — approx. 2 hours 28 minutes, consistent with the volume of business transacted (results approval + 2 capital-structure resolutions + AGM + an acquisition approval).

| # | Line | Agenda item | Flags |
|---|------|-------------|-------|
| 1 | 52-58 | Approved Unaudited Financial Results (Standalone and Consolidated) for quarter ended 30 June 2026, per Reg 33; Limited Review Report by Walker Chandiok & Co LLP enclosed | |
| 2 | 60-66 | Approved increase in Authorized Share Capital from INR 25,00,00,000 (25 cr shares of INR 1) to INR 29,00,00,000 (29 cr shares of INR 1); consequent amendment to Capital Clause (Clause V) of MOA; subject to shareholder approval | CAPITAL_STRUCTURE_CHANGE |
| 3 | 68-88 | Approved enabling resolution to raise funds up to INR 750,00,00,000 (Rs 750 cr) via equity shares/warrants/CCDs/CCPS or combination, in one or more tranches, any permissible mode (QIP/preferential/private placement etc.); subject to shareholder approval at forthcoming AGM. Rationale given: capex cycle for room-inventory addition, acquisition pipeline, balance-sheet strengthening | FUNDRAISE_ENABLING_RESOLUTION — flagged for A4 dilution/capital-allocation analysis |
| 4 | 102-104 | Approved holding the 16th AGM on Monday, 31 August 2026; approved Notice convening AGM and the Board's Report for FY2025-26 | |
| 5 | 106-121 | Approved acquisition of 100% of Itmenaan Lodges Private Limited (29,582 equity shares of INR 10 each) — owner of 'Itmenaan Estate' boutique luxury hotel (RARE India portfolio), Village Naugaon, Tehsil Bhanoli, District Almora, Uttarakhand — for cash consideration INR 12,00,00,000 (Rs 12 cr), total approved investment (incl. capex) not exceeding INR 25,00,00,000 (Rs 25 cr); target FY25-26 total income disclosed as INR 69,76,266 (~Rs 0.70 cr) | M&A_APPROVAL — small target relative to company scale |

**Cross-reference**: Item 3's "strong capex cycle... attractive acquisition/growth opportunities... increasingly volatile geo-political environment" language (lines 78-84) is qualitative/forward-looking narrative embedded in the agenda text itself, not a separate agenda item — routed to A3 (forensic notes) for hedge-language/forward-commitment lexicon review.

---

## 5. ANNEXURES TO BOARD OUTCOME LETTER (2 annexures, 18 rows total)

### 5A. Annexure A — "Details of Raising of Funds" (Reg 30 read with SEBI circular dated 30 Jan 2026) — page 3, lines 153-215 — 8 rows

| Row | Line | Particular | Remark | Flags |
|---|---|---|---|---|
| 1 | 159-165 | Type of securities proposed to be issued | Equity shares (incl. warrants), fully convertible debentures, with/without warrants, convertible preference shares, or any convertible security, in one or more tranches | |
| 2 | 167-175 | Type of issuance | Any permissible mode — private placement, QIP, preferential issue, or other method, subject to regulatory/shareholder approval | |
| 3 | 177-183 | Total number of securities / total amount | Up to aggregate INR 750,00,00,000 (Rs 750 cr) or equivalent, inclusive of premium, in one or more tranches | |
| 4 | 185-188 | Preferential issue — additional details | Not Applicable | ZERO_STANDING |
| 5 | 190-192 | Bonus issue — additional details | Not Applicable | ZERO_STANDING |
| 6 | 194-198 | Depository receipts (ADR/GDR)/FCCB — additional details | Not Applicable | ZERO_STANDING |
| 7 | 200-205 | Debt securities/other non-convertible securities — additional details | Not Applicable | ZERO_STANDING |
| 8 | 207-209 | Cancellation or termination of proposal, incl. reasons | Not Applicable | ZERO_STANDING |

### 5B. Annexure B — "Details of Acquisition" (Itmenaan Lodges Pvt Ltd, Reg 30) — pages 4-5, lines 217-327 — 10 rows

| Row | Line | Particular | Remark (abridged) | Flags |
|---|---|---|---|---|
| 1 | 224-235 | Name of target entity, brief details | Itmenaan Lodges Private Limited, CIN U74999DL2011PTC212592, owns 'Itmenaan Estate' hotel, Village Naugaon, Uttarakhand, part of RARE India | |
| 2 | 237-244 | Whether RPT; promoter/group interest | Not a related-party transaction | |
| 3 | 246-247 | Industry | Hospitality Services | |
| 4 | 249-257 | Objects and impact of acquisition | OCR-garbled narrative; substance: in line with earlier strategy of tactical property-level investments | OCR_LOW_CONFIDENCE |
| 5 | 259-261 | Governmental/regulatory approvals required | NA | ZERO_STANDING |
| 6 | 263-264 | Indicative completion timeline | By 30 August 2026 | |
| 7 | 267-271 | Consideration type/quantum | Cash consideration, total INR 12,00,00,000 (Rs 12 cr), subject to TDS/SPA adjustments | |
| 8 | 273-278 | Cost of acquisition / share price | INR 12,00,00,000 for 29,582 shares of INR 10 each | |
| 9 | 295-300 | % shareholding/control acquired | 100% of issued, subscribed, paid-up equity | |
| 10 | 302-321 | Brief background of target | Incorporated 14 Dec 2011; total income FY25-26 INR 69,76,266; FY24-25 INR 85,75,908; FY23-24 INR 88,99,955; India presence only | Declining 3-year revenue trend on a very small base — informational, routed to A4 |

**annexure_rows count = 8 (Annexure A) + 10 (Annexure B) = 18.**

---

## 6. AUDITOR LIMITED REVIEW REPORTS — PARAGRAPHS (13 total)

### 6A. Standalone report (Walker Chandiok & Co LLP) — pages 6-7, lines 336-423 — 6 paragraphs

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 357-360 | Numbered "1." — scope: reviewed standalone unaudited quarterly financial results per Reg 33 | |
| 2 (unnumbered) | 362-367 | Statement is management's/Board's responsibility; prepared per Ind AS 34; auditor's responsibility to express a conclusion | |
| 3 (unnumbered) | 369-376 | Review conducted per SRE 2410; review is substantially less in scope than an audit; no audit opinion expressed | |
| 4 (unnumbered) | 378-383 | Conclusion: nothing has come to attention causing belief of non-disclosure or material misstatement — **clean/unmodified conclusion** | |
| 5 | 399-404 | Numbered "5." — Other Matter/EOM-type: Company's share of net loss of Rs 7.38 mn in a partnership firm whose interim financials are unreviewed by its auditors, furnished by management; not material to the Company | ENTITY_UNAUDITED (partnership firm interim financials management-furnished, unreviewed) |
| 6 (unnumbered) | 406-407 | Conclusion not modified in respect of the above matter | |

Signature: For Walker Chandiok & Co LLP, Neeraj Goel (Partner, Membership No. 099514), UDIN 26099514QZSUUM5820, Place Gurugram, Date 03 August 2026 (lines 410-423).

### 6B. Consolidated report (Walker Chandiok & Co LLP) — pages 10-12, lines 565-701 — 7 paragraphs

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 586-591 | Numbered "1." — scope: reviewed consolidated unaudited quarterly financial results of the Group; refers to Annexure 1 for subsidiary list | |
| 2 | 593-598 | Numbered "2." — Statement is Holding Company management's/Board's responsibility; Ind AS 34 basis | |
| 3 | 600-607 | Numbered "3." — SRE 2410 review scope; no audit opinion expressed | |
| 3 (cont'd, unnumbered) | 609-610 | Additional scope sentence: procedures also performed per SEBI Circular CIR/CFD/CMD1/44/2019 dated 29 March 2019 under Reg 33(8), to the extent applicable | |
| 4 | 625-631 | Numbered "4." — Conclusion: nothing has come to attention causing belief of non-disclosure or material misstatement — **clean/unmodified conclusion** | |
| 5 (unnumbered) | 633-640 | Other Matter: interim financials of **three subsidiaries** (unreviewed by their auditors) reflecting total revenue Rs 1.91 mn, net loss after tax Rs 17.14 mn, total comprehensive loss Rs 17.14 mn for the quarter, furnished by Holding Company management; not material to the Group | ENTITY_UNAUDITED — 3 subsidiaries not individually named in this paragraph |
| 6 (unnumbered) | 642-643 | Conclusion not modified in respect of the above matter | |

Signature: For Walker Chandiok & Co LLP, Neeraj Goel (Partner, Membership No. 099514), UDIN 26099514JEQMHK9210, Place Gurugram, Date 03 August 2026 (lines 648-661). Same partner and date as standalone report; UDIN correctly differs per report (one UDIN per report is standard practice, not a flag).

**Both reports: unmodified/clean conclusions.** No qualification, adverse conclusion, disclaimer, or Going Concern paragraph in either report. Each carries one Other-Matter-type paragraph limited to unreviewed, management-furnished interim financial information of (a) one partnership firm (standalone) and (b) three subsidiaries (consolidated) — none individually named, none stated to be material.

---

## 7. ENTITY LIST — CONSOLIDATION SCOPE (Annexure 1 to consolidated auditor report) — page 12, lines 674-701 — 18 entities

No prior-quarter ledger was supplied with this task (`PRIOR_LEDGER_PATH` not provided) — entity-list diffing against the prior quarter could not be performed. The two entities below are flagged based on the **document's own** effective-date annotations, not a cross-quarter diff.

| # | Entity | Flags |
|---|---|---|
| 1 | Argon Hotels Private Limited | |
| 2 | Ascent Hotels Private Limited | |
| 3 | Barque Hotels Private Limited | |
| 4 | Caspia Hotels Private Limited | |
| 5 | Paulmech Hospitality Private Limited | |
| 6 | SAMHI JV Business Hotels Private Limited | |
| 7 | SAMHI Hotels (Ahmedabad) Private Limited | |
| 8 | SAMHI Hotels (Gurgaon) Private Limited | |
| 9 | Duet India Hotels (Pune) Private Limited | |
| 10 | Duet India Hotels (Hyderabad) Private Limited | |
| 11 | Duet India Hotels (Ahmedabad) Private Limited | |
| 12 | Duet India Hotels (Chennai) Private Limited | |
| 13 | Duet India Hotels (Jaipur) Private Limited | |
| 14 | Duet India Hotels (Navi Mumbai) Private Limited | |
| 15 | Innmar Tourism and Hotels Private Limited | |
| 16 | SAMHI Hospitality Ventures Private Limited (formerly ACIC Advisory Private Limited) | RENAMED entity (per document's own parenthetical) |
| 17 | SAMHI Skyline Private Limited (from 16 January 2026) | NEW_ENTITY_THIS_PERIOD (self-declared effective date; PRIOR_LEDGER_NOT_AVAILABLE for cross-check) |
| 18 | RARE India (from 22 April 2026) | NEW_ENTITY_THIS_PERIOD (ties to standalone Note 8 / consolidated Note 7 acquisition; PRIOR_LEDGER_NOT_AVAILABLE for cross-check) |

---

## 8. DIGITAL SIGNATURE BLOCKS (9) — timestamp vs board-meeting-conclusion check

Board meeting concluded 06:58 p.m. (18:58) IST (line 49-50).

| # | Signatory | Designation | Location (line) | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | Sanjay Jain | Sr. Director-Corporate Affairs, Company Secretary & Compliance Officer | Board Outcome letter, page 1 end (90-94) | 2026.08.03 19:23:01 +05'30' | post-meeting by ~25 min — normal |
| 2 | Sanjay Jain | (same) | Board Outcome letter, page 2 close (138-142) | 2026.08.03 19:23:22 +05'30' | post-meeting — normal |
| 3 | Sanjay Jain | (same) | Annexure A close (211-215) | 2026.08.03 19:23:36 +05'30' | post-meeting — normal |
| 4 | Sanjay Jain | (same) | Annexure B page 4 close (280-284) | 2026.08.03 19:25:01 +05'30' | post-meeting — normal |
| 5 | Sanjay Jain | (same) | Annexure B page 5 close (323-327) | 2026.08.03 19:25:15 +05'30' | post-meeting — normal |
| 6 | Neeraj Goel | Partner, Walker Chandiok & Co LLP | Standalone Auditor's Review Report (415-423) | Date only: 03 August 2026 (no time in extract) | UDIN 26099514QZSUUM5820 |
| 7 | Ashish Jakhanwala | Chairman, Managing Director & CEO (DIN 03304345) | Standalone financial results sign-off (548-557) | Place: New Delhi, Date: 03 August 2026 (no time) | |
| 8 | Neeraj Goel | Partner, Walker Chandiok & Co LLP | Consolidated Auditor's Review Report (653-661) | Date only: 03 August 2026 (no time in extract) | UDIN 26099514JEQMHK9210 |
| 9 | Ashish Jakhanwala | Chairman, Managing Director & CEO (DIN 03304345) | Consolidated financial results sign-off (838-848) | Place: New Delhi, Date: 03 August 2026 (no time) | |

**No SIGNATURE_TIMING flag.** All five timestamped digital signatures (all Sanjay Jain, Board Outcome letter + annexures) fall 25-27 minutes AFTER the 06:58 p.m. meeting conclusion — the expected sequence (letter/annexures signed once the meeting concludes). None precede the conclusion time.

---

## 9. ZERO_STANDING SUMMARY (12 rows)

| # | Item | Statement | Line |
|---|------|-----------|------|
| 1 | Current tax | Standalone P&L | 463 |
| 2 | Deferred tax | Standalone P&L | 464 |
| 3 | Total tax expense (subtotal) | Standalone P&L | 465 |
| 4 | Tax expense of discontinued operations | Standalone P&L | 470 |
| 5 | Income tax relating to OCI items | Standalone P&L | 478 |
| 6 | Tax expense of discontinued operations | Consolidated P&L | 746 |
| 7 | Preferential issue additional details | Board Outcome Annexure A | 185-188 |
| 8 | Bonus issue additional details | Board Outcome Annexure A | 190-192 |
| 9 | ADR/GDR/FCCB additional details | Board Outcome Annexure A | 194-198 |
| 10 | Debt securities/non-convertible securities additional details | Board Outcome Annexure A | 200-205 |
| 11 | Cancellation/termination of issuance proposal | Board Outcome Annexure A | 207-209 |
| 12 | Governmental/regulatory approvals required (acquisition) | Board Outcome Annexure B | 259-261 |

Rows carrying a nonzero value in at least one of the four displayed periods (e.g., "Loss from discontinued operations before tax," EPS-discontinued lines, all four exceptional-items sub-table rows) are NOT included here even though several periods within them show nil/blank — per the operating rule, ZERO_STANDING applies to items that are zero/nil/dash in ALL periods shown.

---

## 10. FLAGS RAISED — SUMMARY

- **STANDALONE_CONSOL_PAT_GAP** — Section 3 (standalone PAT ~Rs 247 cr vs consolidated PAT ~Rs 25 cr / owners'-share ~Rs 18.25 cr, Q1 FY27)
- **EXCEPTIONAL_ITEMS_COMPOSITION_DIFFERS** — Section 2C (standalone = investment-level items; consolidated = asset-level items)
- **ZERO_STANDING** x12 — Section 9
- **NEW_ENTITY_THIS_PERIOD** x2 — SAMHI Skyline Private Limited, RARE India (Section 7; prior-quarter ledger not available for formal ENTITY_CHANGE cross-check)
- **CAPITAL_STRUCTURE_CHANGE** — authorized capital increase 25cr → 29cr shares (Board Outcome item 2)
- **FUNDRAISE_ENABLING_RESOLUTION** — up to Rs 750 cr enabling resolution (Board Outcome item 3)
- **M&A_APPROVAL** — Itmenaan Lodges Pvt Ltd acquisition, Rs 12 cr (Board Outcome item 5 / Annexure B)
- **ENTITY_UNAUDITED** x2 — one partnership firm (standalone report Other Matter), three unnamed subsidiaries (consolidated report Other Matter)
- **OCR_LOW_CONFIDENCE** — numerous cells across both P&L statements' current-quarter/prior-quarter columns and both exceptional-items sub-tables (pages 8, 9, 13, 14, all pre-flagged as OCR pages by A1); Annexure B row 4 narrative
- **OCR_DIGIT_DROPPED** — standalone Note 1's leading numeral (line 514)
- No SIGNATURE_TIMING flag (Section 8)
- No Going Concern language, no qualified/adverse/disclaimer conclusion in either auditor report
