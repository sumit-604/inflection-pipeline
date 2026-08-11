# A2 ENUMERATION LEDGER — EXICOM Q1 FY27 Results Filing

Source: `results_board_outcome.pdf` (10 pages) via
`/home/user/inflection-pipeline/runs/exicom-q1fy27/work/extract_results_exicom_q1fy27.txt`
Units: Rs Lakhs unless stated (x0.01 = Rs Cr). Two numeric renderings of pages 8-10 exist in
the extract: PRIMARY pdftotext-layout (lines 347-443, comma/decimal separators collapsed) and
OCR NUMERIC SUPPLEMENT (lines 495-663, clean formatting). Per task instruction, OCR values are
used as the numeric spine; PRIMARY is the cross-check. Every numeric cell below that required a
correction beyond straight OCR transcription is logged in the RECONCILIATION LOG (Section 5) and
flagged `NUMERIC_RECONCILED` in its row.

```
=== A2 COUNT TEST ===
category: notes_top_level        grep_count: 6    sweep_count: 6    match: yes
category: note_subitems_footnotes grep_count: 8   sweep_count: 8    match: yes
category: note_table_line_items  grep_count: 10   sweep_count: 10   match: yes
category: pl_line_items          grep_count: 34   sweep_count: 34   match: yes
category: segment_line_items     grep_count: 17   sweep_count: 17   match: yes
category: zero_standing          grep_count: 12   sweep_count: 12   match: yes
category: agenda_items           grep_count: 3    sweep_count: 3    match: yes
category: auditor_paras          grep_count: 13   sweep_count: 13   match: yes  (see note*)
category: entities                grep_count: 9   sweep_count: 9    match: yes
category: signature_blocks       grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```
*auditor_paras note: first mechanical pass with pattern `^\s*[0-9]+\.?\s` + `^\s*\([a-c]\)\s`
found only 12 (missed consolidated-report Other Matters sub-para (c) at line 325 because the
source text itself renders it as "()" — the letter "c" is dropped by the extraction, i.e. a
genuine source-OCR corruption, not a sweep miss). Re-swept with a broadened pattern
`^\s*\(([a-c]|)\)\s` that also catches the bare "()" token; this raised the mechanical count to
match the manual sweep of 13. Logged as flag `OCR_CORRUPTION` on that row. This is the GATE A2
re-sweep-and-reconcile process working as designed — see row 6(c) in Section 6.

---
## 1. NOTES (numbered notes 1-6 on page 10)

| # | Note | Line (primary / OCR) | First ~15 words | Flags |
|---|------|----------------------|------------------|-------|
| 1 | Results reviewed by Audit Committee, approved by Board 10-Aug-2026; auditors issued unmodified report | 445 / 610 | "The above Un-Audited Standalone And Consolidated Financial Results for the first quarter..." | — |
| 2 | Compliance with Ind AS under Companies Act 2013 s.133 | 447 / 612 | "The above Financial Results are in compliance with the Indian Accounting Standards..." | — |
| 3 | IPO / Pre-IPO Placement disclosure, 5 sub-parts (a)-(e), 2 embedded tables | 448-467 / 613-637 | "The Parent Company has completed an Initial Public Offer ('IPO') and equity shares..." | see 1a below for sub-items |
| 4 | Consolidation entity list (9 entities) + ENTITY_CHANGE footnote on entity iv | 474-484 / 638-648 | "The Un-audited Consolidated Financial Results for the first quarter ended June 30, 2026 includes..." | ENTITY_CHANGE — see Section 8 |
| 5 | Q4 FY26 figures are balancing figures (audited FY − limited-reviewed 9M) | 485-486 / 649-650 | "The Figures of the quarter ended March 31, 2026 were balancing figures between audited..." | — |
| 6 | Prior-period regrouping/reclassification statement | 487 / 651 | "Previous period figures have been re-grouped/ re-classified wherever considered necessary..." | GENERIC_REGROUPING_NOTE — no specifics named, flag for A3 (regrouping notes with no detail are a known evasion pattern) |

### 1a. Note-3 sub-items and other footnotes (8 units — "note_subitems_footnotes" category)

| # | Item | Line (primary / OCR) | Content | Flags |
|---|------|----------------------|---------|-------|
| 3(a) | IPO completion + listing detail (NSE/BSE, 05-Mar-2024) + issue-structure table (Fresh Issue / Offer for Sale / Total — 3 rows, see Section 2 note-tables) | 448-453 / 613-618 | Listing date, share counts, face value, issue price, premium | — |
| 3(b) | Pre-IPO Placement: 52,59,257 equity shares @ Rs135.00 (incl. Rs125 premium), cash consideration Rs7,100.00 lakh | 454 / 619 | — | — |
| 3(c) | Total offer expenses (incl. Pre-IPO) Rs3,595.89 lakh incl. GST; proportionate recovery from selling shareholders | 455 / 620 | — | — |
| 3(d) | Board circular resolution 26-Mar-2026 extended IPO-proceeds utilisation timeline to 30-Sep-2026 | 457 / 621 | — | — |
| 3(e) | As at 30-Jun-2026, entire net proceeds Rs40,000.00 lakh fully utilised + utilisation table (7 rows, see Section 2) | 458-473 / 622-637 | — | CHANGE_FROM_PRIOR — prior-quarter (Q4 FY26) COMPANY MEMORY records Rs8.83 Cr (R&D) unutilised; this quarter states full utilisation. Flag for A3 verbatim-diff (what closed the R&D gap this quarter) |
| Note-4 asterisk footnote | "*Exicom Power Solutions B.V. ceased to be a wholly-owned subsidiary of the Company w.e.f. April 22, 2026" | 484 / 648 | Sub-footnote to entity iv in the Note-4 list | ENTITY_CHANGE |
| EPS asterisk footnote | "* Basic and Diluted Earnings Per Share (EPS) is not annualised for the quarter ended June 30, 2026, quarter ended March 31, 2026 and quarter ended June 30, 2025" | 406 / 566 | Table footnote qualifying the EPS line | — |
| "See Accompanying note to financial results" cross-reference marker | 405 (OCR equivalent implicit at table foot, no separate OCR line) | Generic footnote pointer beneath the P&L table, directing reader to Notes 1-6 | — |

---
## 2. NOTE-3 EMBEDDED TABLES (10 rows — "note_table_line_items" category)

### 2a. IPO issue structure (3 rows), lines 450-453 / 615-618
| Row | No. of Shares | Face Value | Issue Price | Premium | Amount (Rs Lakh) | Flags |
|---|---|---|---|---|---|---|
| Fresh Issue | 23,169,000 | Rs10/- | Rs142/- | Rs132/- | 32,899.98 | — |
| Offer for Sale | 7,042,200 | Rs10/- | Rs142/- | Rs132/- | 9,999.97 | — |
| Total | 30,211,200 | Rs10/- | Rs142/- | Rs132/- | 42,899.90 | rounding: 32,899.98+9,999.97=42,899.95 vs stated total 42,899.90 — Rs0.05 lakh immaterial rounding gap, flag NUMERIC_QA (immaterial) |

### 2b. IPO proceeds utilisation (Sr. 1-6 + Total = 7 rows), lines 461-473 / 622-637
Columns: Amount proposed in Offer Document | Surplus transferred to Gen. Corp. Purposes | Revised amount after transfer | Utilised as at 30-Jun-2026 | Unutilised as at 30-Jun-2026

| Sr | Item head | Proposed | Transfer | Revised | Utilised | Unutilised | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Part-financing cost of setting up production/assembly lines, planned manufacturing facility, Telangana | ILLEGIBLE (raw fragment "s097)" unreadable) | — | — | — | "-" (nil, per note text "fully utilised") | NOT_FOUND — figure not reliably extractable from either primary or OCR; flag for source-PDF verification |
| 2 | ILLEGIBLE label (raw fragments "come...sue...sunan\|sand" / "jour Company" — possibly a repayment-of-borrowings object per standard IPO-object conventions, NOT confirmed) | NOT FOUND | — | — | — | "-" (nil, per note text) | NOT_FOUND — both label and amount unreadable; flag for source-PDF verification |
| 3 | Part-funding incremental working capital requirements | 6,900.00 | — | 6,900.00 | 6,900.00 | "-" | — |
| 4 | Investment in R&D and product development | 4,000.00 | — | 4,000.00 | 4,000.00 | "-" | CHANGE_FROM_PRIOR — prior quarter (Q4 FY26 memory) shows Rs8.83 Cr (883 lakh) unutilised here; now fully utilised. Flag for A3 |
| 5 | General Corporate Purpose | CONFLICT: primary reads 6,036.00; OCR reads 6,936.00 | (inflow, exact figure illegible) | 6,100.40 | 6,100.40 | "-" | NUMERIC_QA — primary vs OCR conflict on proposed amount, ~Rs900 lakh gap; not independently resolvable from extract; flag for source verification |
| 6 | Offer-related expenses | 2,887.13 | (64.40) | 2,822.73 | 2,822.73 | "-" | — |
| Total | — | 40,000.00 | — | 40,000.00 | 40,000.00 | "-" | Ties to Note 3(e) "entire net proceeds of Rs.40,000.00 lakhs stand fully utilised" |

---
## 3. P&L LINE ITEMS — Statement of Un-Audited Standalone AND Consolidated Financial Results
(34 rows; single combined table, 4 periods each side: Q1 FY27 unaudited | Q4 FY26 audited-balancing | Q1 FY26 unaudited | FY26 audited. Primary lines 360-406, OCR lines 520-566. All values reconciled per Section 5 log; `NUMERIC_RECONCILED` flag = value differs from a straight raw-OCR read.)

| # | Line item | SA Q1FY27 | SA Q4FY26 | SA Q1FY26 | SA FY26 | C Q1FY27 | C Q4FY26 | C Q1FY26 | C FY26 | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Revenue from operations | 23,682.91 | 28,207.43 | 15,065.97 | 89,479.94 | 33,106.97 | 38,794.95 | 20,531.72 | 115,172.53 | — |
| 2 | Other Income | 726.84 | 626.82 | 1,202.93 | 2,990.50 | 492.86 | 189.87 | 822.19 | 2,275.74 | — |
| 3 | Total Income (subtotal) | 24,409.75 | 28,834.25 | 16,268.90 | 92,470.44 | 33,599.83 | 38,984.82 | 21,353.91 | 117,448.27 | — |
| 4 | Cost of Material Consumed | 16,465.95 | 20,380.95 | 9,484.18 | 69,030.30 | 21,021.12 | 23,864.01 | 11,619.39 | 79,427.00 | — |
| 5 | Purchase of Stock-in-Trade | 3.47 | 7.73 | 0.66 | 14.09 | 3.46 | 7.73 | 133.15 | 146.59 | — |
| 6 | Changes in Inventories of FG/WIP/Stock-in-Trade | (89.22) | (396.57) | 395.17 | (4,814.78) | 1,189.37 | 1,823.01 | 423.63 | (3,167.63) | — |
| 7 | Employee Benefits Expenses | 2,560.55 | 2,351.01 | 1,813.71 | 8,089.55 | 5,009.35 | 5,635.98 | 5,308.45 | 21,867.56 | — |
| 8 | Manufacturing Expenses | 399.19 | 596.90 | 257.42 | 1,517.03 | 401.72 | 598.82 | 259.19 | 1,524.58 | — |
| 9 | Finance Costs | 1,140.83 | 1,098.05 | 1,328.54 | 4,396.82 | 1,620.89 | 1,549.94 | 1,563.69 | 5,584.88 | — |
| 10 | Depreciation and amortization expenses | 1,033.03 | 913.52 | 616.98 | 2,904.88 | 3,895.88 | 3,499.36 | 2,483.62 | 11,630.29 | — |
| 11 | Other Expenses | 2,255.17 | 2,277.24 | 2,235.03 | 8,643.45 | 7,671.57 | 6,838.75 | 6,646.20 | 25,706.91 | — |
| 12 | Total Expenses (subtotal) | 23,768.97 | 27,228.83 | 16,131.69 | 89,781.34 | 40,803.36 | 43,817.60 | 28,437.32 | 142,720.18 | NUMERIC_RECONCILED (SA-FY26: raw OCR/primary reads "9,701.34"/"89,701.34", corrupted; reconciled = 92,470.44 − 2,689.10 = 89,781.34, exact tie to row 13) |
| 13 | Profit/(Loss) before exceptional items and tax (I−II) | 640.78 | 1,605.42 | 137.21 | 2,689.10 | (7,203.53) | (4,832.78) | (7,083.41) | (25,271.91) | NUMERIC_RECONCILED (SA-Q1FY27: raw primary reads 610.78; reconciled 640.78 = Total Income 24,409.75 − Total Expenses 23,768.97, independently confirmed by row15 tie-out and Segment Note "Total Profit before Tax" = 640.78) |
| 14 | Exceptional Items | "-" (nil) | "-" (nil) | 886.99 | 973.25 | "-" (nil) | 55.38 | 1,204.93 | 1,653.04 | NUMERIC_RECONCILED / ZERO_STANDING (SA Q1FY27, SA Q4FY26, C Q1FY27 all nil this row; values sourced from Segment Note "ii. Un-allocable expense/(income)" row, which reconciles exactly to row13−row15 in every column — raw P&L row itself is badly OCR-corrupted in both primary and OCR-supplement passes). **Note: this CONTRADICTS the task-injected assumption that "the consolidated column carries exceptional items while standalone shows nil this quarter" — reconciliation shows BOTH standalone AND consolidated are nil for Q1 FY27 specifically; consolidated exceptional items appear only in Q4FY26/Q1FY26/FY26. Flag SOURCE_VERIFY_NEEDED for A3/A4.** |
| 15 | Profit/(Loss) before tax (III−IV) | 640.78 | 1,605.42 | (749.78) | 1,715.85 | (7,203.53) | (4,888.16) | (8,288.34) | (26,924.95) | Cross-verified against Segment Note "Total Profit before Tax" row (exact match all 8 columns) |
| 16 | Current Tax | 125.25 | 433.02 | "-" (nil) | 493.01 | 130.16 | 499.82 | "-" (nil) | 500.50 | NUMERIC_RECONCILED (SA-Q4FY26 raw fragment "193.01" does not tie; reconciled via V−VII−DT. SA-FY26 raw "93,01" truncated, reconciled 493.01. C-Q4FY26 raw "199.82" does not tie, reconciled 499.82. SA/C-Q1FY26 raw glyphs "E"/":" read as dash) |
| 17 | Deferred Tax | 23.72 | (17.99) | 25.42 | (134.05) | 21.62 | 43.28 | 25.23 | (12.79) | NUMERIC_RECONCILED (SA-Q1FY27 raw fragment "2.72" truncated, reconciled 23.72 via V−CT−VII tie-out). C-Q1FY27: ~Rs2.00 lakh immaterial residual gap vs full tie-out (23.62 implied) — flag NUMERIC_QA minor |
| 18 | Profit/(Loss) for the period/year (V−VI) | 491.81 | 1,190.39 | (775.20) | 1,356.89 | (7,357.31) | (5,431.26) | (8,313.57) | (27,412.66) | Cross-verified via row24 (Total Comprehensive Income) minus row23 (OCI after tax), exact tie all 8 columns |
| 19 | Equity Instruments measured at Fair value (OCI, not reclassified) | "-" | "-" | "-" | "-" | "-" | (2.90) | 18.42 | (5.55) | ZERO_STANDING (SA, all 4 periods) |
| 20 | Re-measurement gains/(loss) on defined benefit plans (OCI, not reclassified) | (47.32) | 49.51 | 31.61 | 42.48 | (47.32) | 49.51 | 31.61 | 42.48 | NUMERIC_RECONCILED (Q4FY26 and C-Q1FY27 raw OCR fragments drop a leading digit — "9.51"→49.51, "7.32"→47.32 — reconciled via OCI-after-tax subtotal tie-out, exact match all columns). Note SA = Consol in every period (defined-benefit plan appears to be parent-only, flows through unadjusted) |
| 21 | Tax on above item | 11.91 | 8.92 | 7.96 | 10.69 | 11.91 | 8.92 | 7.96 | 10.69 | SA = Consol every period (same driver as row 20) |
| 22 | Exchange gain/(loss) on translation of foreign operations (OCI, reclassifiable) | "-" | "-" | "-" | "-" | (1,830.18) | 2,351.12 | 1,095.22 | 5,232.63 | ZERO_STANDING (SA, all 4 periods — standalone entity has no foreign operations to translate) |
| 23 | Other Comprehensive Income (OCI) (After Tax) — subtotal | (35.41) | 58.43 | 39.57 | 53.17 | (1,865.59) | 2,406.65 | 1,153.21 | 5,280.25 | Sum of rows 19+20+21+22 ties exactly in all 8 columns (full reconciliation) |
| 24 | Total Comprehensive Income for the period/year (VII+VIII) | 456.40 | 1,248.82 | (735.63) | 1,410.06 | (9,222.90) | (3,024.61) | (7,160.36) | (22,132.41) | = row18+row23, exact tie all columns |
| 25 | Profit attributable to: Owners of the Parent | "-" | "-" | "-" | "-" | (6,925.57) | (5,431.26) | (8,313.57) | (27,412.66) | ZERO_STANDING (SA, all 4 periods — structural, standalone has no NCI concept) |
| 26 | Profit attributable to: Non-Controlling Interests | "-" | "-" | "-" | "-" | (431.74) | "-" | "-" | "-" | ZERO_STANDING (SA, all 4 periods). Consol: nonzero ONLY in Q1 FY27 — first quarter NCI appears, ties to ENTITY_CHANGE (Exicom Power Solutions B.V. ceased WOS 22-Apr-2026, now 7.8% minority). row25+row26 = row18 (Consol), exact tie |
| 27 | OCI attributable to: Owners of the Parent | "-" | "-" | "-" | "-" | (1,775.33) | 2,406.65 | 1,153.21 | 5,280.25 | ZERO_STANDING (SA, all 4 periods) |
| 28 | OCI attributable to: Non-Controlling Interests | "-" | "-" | "-" | "-" | (90.26) | "-" | "-" | "-" | ZERO_STANDING (SA, all 4 periods). Consol nonzero only Q1 FY27, same ENTITY_CHANGE driver as row26 |
| 29 | Total Comprehensive Income attributable to: Owners of the Parent | "-" | "-" | "-" | "-" | (8,700.90) | (3,024.61) | (7,160.36) | (22,132.41) | ZERO_STANDING (SA, all 4 periods). = row25+row27 exact tie |
| 30 | Total Comprehensive Income attributable to: Non-Controlling Interests | "-" | "-" | "-" | "-" | (522.00) | "-" | "-" | "-" | ZERO_STANDING (SA, all 4 periods). = row26+row28 exact tie; Consol nonzero only Q1 FY27 |
| 31 | Paid-up equity share capital (Face Value Rs10/- each) | 13,907.98 | 13,907.98 | 12,093.89 | 13,907.98 | 13,907.98 | 13,907.98 | 12,093.89 | 13,907.98 | Identical SA/Consol every period (entity-level capital, expected) |
| 32 | Other Equity | (blank, not disclosed) | (blank) | (blank) | 79,213.80 | (blank) | (blank) | (blank) | 51,221.39 | STRUCTURAL_NA — Other Equity is a balance-sheet item disclosed only for the year-end (FY26) column per standard Ind-AS 34 quarterly format; the 6 interim-period cells are genuinely blank in source, not zero-standing transactions |
| 33 | Earnings per equity share — Basic (Rs) | 0.35 | 0.88 | (0.64) | 1.01 | (4.98) | (4.03) | (6.87) | (20.36) | See EPS asterisk footnote (Section 1a) — not annualised |
| 34 | Earnings per equity share — Diluted (Rs) | 0.35 | 0.88 | (0.64) | 1.01 | (4.98) | (4.03) | (6.87) | (20.36) | Diluted = Basic in every period/statement — no dilutive instruments outstanding; see EPS footnote |

---
## 4. SEGMENT TABLE LINE ITEMS
(17 rows; single combined table, same 8-column structure. Primary lines 417-442, OCR lines 577-598. This block OCR'd cleanly — no reconciliation required, and it is the anchor used to reconcile several P&L rows above.)

| # | Line item | SA Q1FY27 | SA Q4FY26 | SA Q1FY26 | SA FY26 | C Q1FY27 | C Q4FY26 | C Q1FY26 | C FY26 | Flags |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Segment Revenue — a. Critical Power | 17,601.95 | 19,414.88 | 9,781.96 | 61,766.18 | 17,721.21 | 19,889.20 | 10,248.84 | 64,181.80 | — |
| 2 | Segment Revenue — b. EV Charger | 6,080.96 | 8,792.55 | 5,284.01 | 27,713.76 | 15,385.76 | 18,905.75 | 10,282.88 | 50,990.73 | — |
| 3 | Revenue from Operations (segment total) | 23,682.91 | 28,207.43 | 15,065.97 | 89,479.94 | 33,106.97 | 38,794.95 | 20,531.72 | 115,172.53 | Ties exactly to P&L row1 |
| 4 | Segment Results — a. Critical Power | 1,537.71 | 1,761.11 | 778.34 | 3,845.36 | 1,277.25 | 2,138.41 | 548.67 | 3,827.64 | — |
| 5 | Segment Results — b. EV Charger | 243.90 | 942.36 | 687.41 | 3,240.56 | (6,859.89) | (5,421.25) | (6,068.39) | (23,514.67) | EV Charger segment result deeply negative every consol period — thesis-relevant, not an extraction flag |
| 6 | Segment Results — Total | 1,781.61 | 2,703.47 | 1,465.75 | 7,085.92 | (5,582.64) | (3,282.84) | (5,519.72) | (19,687.03) | = row4+row5, exact tie |
| 7 | Less: i. Interest | 1,140.83 | 1,098.05 | 1,328.54 | 4,396.82 | 1,620.89 | 1,549.94 | 1,563.69 | 5,584.88 | Ties exactly to P&L Finance Costs (row9) |
| 8 | Less: ii. Un-allocable expense/(income) | "-" | "-" | 886.99 | 973.25 | "-" | 55.38 | 1,204.93 | 1,653.04 | Used as authoritative source for P&L row14 (Exceptional Items) reconciliation |
| 9 | Total Profit before Tax | 640.78 | 1,605.42 | (749.78) | 1,715.85 | (7,203.53) | (4,888.16) | (8,288.34) | (26,924.95) | Ties exactly to P&L row15 |
| 10 | Segment Assets — a. Critical Power | 69,385.42 | 74,389.13 | 60,373.36 | 74,389.13 | 78,141.68 | 84,416.79 | 68,656.62 | 84,416.79 | Note SA Q1FY27 (69,385.42) < SA Q4FY26/FY26 (74,389.13, same figure repeated for both — expected since Q4FY26=FY26-end) |
| 11 | Segment Assets — b. EV Charger | 102,223.49 | 103,854.99 | 83,332.24 | 103,854.99 | 111,023.87 | 114,470.82 | 99,256.91 | 114,470.82 | — |
| 12 | Segment Assets — c. Unallocated | "-" | "-" | "-" | "-" | "-" | "-" | "-" | "-" | ZERO_STANDING (both SA and Consol, all 4 periods) |
| 13 | Segment Assets — Total | 171,608.91 | 178,244.12 | 143,705.60 | 178,244.12 | 189,165.55 | 198,887.61 | 167,913.53 | 198,887.61 | = row10+row11+row12 |
| 14 | Segment Liabilities — a. Critical Power | 44,925.92 | 56,483.26 | 47,088.21 | 56,483.26 | 46,031.01 | 58,528.96 | 47,765.24 | 58,528.96 | — |
| 15 | Segment Liabilities — b. EV Charger | 33,044.82 | 28,639.08 | 31,543.71 | 28,639.08 | 80,250.20 | 75,229.28 | 65,922.37 | 75,229.28 | — |
| 16 | Segment Liabilities — c. Unallocated | "-" | "-" | "-" | "-" | "-" | "-" | "-" | "-" | ZERO_STANDING (both SA and Consol, all 4 periods) |
| 17 | Segment Liabilities — Total | 77,970.74 | 85,122.34 | 78,631.92 | 85,122.34 | 126,281.21 | 133,758.24 | 113,687.61 | 133,758.24 | = row14+row15+row16 |

No balance-sheet-level statement (full B/S) is present in this filing — Segment Assets/Liabilities are the only balance-sheet-type disclosures. No standalone entity ever shows Segment Assets/Liabilities Unallocated > 0, consistent with a fully allocated two-segment structure (Critical Power, EV Charger).

---
## 5. RECONCILIATION LOG (numeric extraction corrections applied above)

| Row(s) | Raw reading (primary and/or OCR) | Reconciled value | Method | Confidence |
|---|---|---|---|---|
| P&L row13, SA-Q1FY27 | 610.78 | 640.78 | Total Income − Total Expenses; independently confirmed by Segment Note row9 | High |
| P&L row12, SA-FY26 | "9,701.34" / "89,701.34" | 89,781.34 | Total Income − row13 | High |
| P&L row14 (all 8 columns) | garbled tokens "-","5","699","57325","5","5530","120093","165300" | "-","-",886.99,973.25,"-",55.38,1,204.93,1,653.04 | = row13 − row15 per column; exact match to Segment Note row8 in every column | High |
| P&L row16 (Current Tax), SA-Q4FY26 / SA-FY26 / C-Q4FY26 | "193.01" / "93,01" / "199.82" | 433.02 / 493.01 / 499.82 | V − VII − Deferred Tax, cross-checked against VII derived independently via row24−row23 | High |
| P&L row17 (Deferred Tax), SA-Q1FY27 | "2.72" | 23.72 | V − Current Tax − VII | High |
| P&L row17, C-Q1FY27 | 21.62 (raw, retained) | — (residual ~Rs2.00 lakh gap vs full tie-out) | Immaterial, flagged not corrected | Low-materiality flag only |
| P&L row20 (Re-measurement), SA/C-Q4FY26 and C-Q1FY27 | "9.51" / "7.32" | 49.51 / 47.32 | OCI-after-tax subtotal (row23) minus other 3 components; exact match all affected columns | High |
| Note 2b row1, row2 (IPO utilisation) | illegible fragments | NOT FOUND | No independent equation available (2 unknowns, 1 equation from Total row) | Not resolved — flag for source PDF |
| Note 2b row5 (General Corporate Purpose, proposed amount) | 6,036.00 (primary) vs 6,936.00 (OCR) | Not resolved | Same underdetermination as above | Not resolved — flag for source PDF |
| Auditor consol report para 6(c) | "()" | "(c)" | Contextual (follows "(b)"; three Other Matters sub-points is the standard SRE 2410 structure) | High |

---
## 6. BOARD OUTCOME — AGENDA ITEMS (3 rows)

Board meeting: commenced 11:30 a.m., concluded 1:40 p.m. (13:40) on 10-Aug-2026 — line 51. Duration ~2h10m.

| # | Agenda item | Line | Detail | Flags |
|---|---|---|---|---|
| 1 | Approval of Unaudited Financial Results (SA + Consol) for Q1 FY27, together with Limited Review Reports from Khandelwal Jain & Co. | 54-67 | Reviewed/recommended by Audit Committee same day; QR-code newspaper publication compliance (Reg. 47) noted as a consequence, not a separate agenda item | — |
| 2a | Approval of Material Related Party Transactions between the Company's subsidiary(ies) and step-down subsidiary(ies) (Company not a direct party) | 80-93 | Exceeds Reg. 23 materiality threshold; reviewed/approved by Audit Committee same day; subject to shareholder approval at ensuing AGM; arm's-length, ordinary course | RPT is between subsidiaries only (Company not a party) — worth A3 attention on which subsidiaries and value |
| 2b | Approval of draft Notice convening the ensuing Annual General Meeting (seeking shareholder approval for the above RPT, "along with other business items") | 95-98 | Notice to be dispatched "in due course"; no date, no record date, and no other business items specified in this filing | NOT_FOUND — no AGM date, no record date, "other business items" unspecified; flag for A3 (silence on AGM calendar) |

No dividend, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant, and no capital-raising enabling resolution appear anywhere in this filing — checked and absent, not merely unenumerated.

---
## 7. AUDITOR REVIEW REPORTS — every paragraph (13 rows)

### 7a. Standalone report (Annexure I, pages 3-4, lines 134-211) — Khandelwal Jain & Co.

| Para | Line | Content | Flags |
|---|---|---|---|
| 1 | 145 | Scope: reviewed Unaudited Standalone Financial Results for quarter ended 30-Jun-2026 per Reg. 33 | — |
| 2 | 151 | Responsibility statement: Statement is Management's/Board's responsibility, prepared per Ind AS 34 | — |
| 3 | 159 | Review standard: SRE 2410, moderate assurance, explicitly "we do not express an audit opinion" | — |
| 4 | 171 | Conclusion: unmodified — "nothing has come to our attention" that indicates material misstatement | — |
| 5 | 187 | "Other Matter": Q4 FY26 figures in the comparative column are balancing figures (audited FY less limited-reviewed 9M); conclusion not modified in respect of this matter | No Emphasis of Matter paragraph present; no Going Concern language present — both checked, absent |
| Signature block | 197-211 | Ravi Dakliya, Partner, Membership No. 304534, UDIN 26304534YGRZKC8103, Place Gurugram, Dated 10-Aug-2026 | See Section 9 (signature blocks) |

### 7b. Consolidated report (Annexure I, pages 5-7, lines 221-346) — Khandelwal Jain & Co.

| Para | Line | Content | Flags |
|---|---|---|---|
| 1 | 231 | Scope: reviewed Unaudited Consolidated Financial Results of the Parent and Subsidiaries (the "Group") for quarter ended 30-Jun-2026 | — |
| 2 | 238 | Responsibility statement: Parent's Management/Board, prepared per Ind AS 34 | — |
| 3 | 246 | Review standard: SRE 2410, moderate assurance, "we do not express an audit opinion" | — |
| 4 | 270-278 | Entity list: results of 8 entities included (subsidiaries only — parent not listed here, see Section 8 for full 9-entity Note-4 list) | Cross-checked against Note 4 — the 8 entities match Note-4 items ii-ix exactly (parent excluded, consistent, since para 4 lists only the subsidiaries whose results are consolidated INTO the parent) |
| 5 | 280-289 | Conclusion: unmodified, "based on the consideration of review reports of other auditors referred to in paragraph 6" | Explicitly conditions the unmodified conclusion on other-auditor reliance — feeds directly into para 6(a) |
| 6(a) | 293-304 | Other Matters (a): auditor did NOT review interim results of 8 subsidiaries (all 8 foreign entities); their unreviewed-by-KJCo figures reflect total revenue Rs10,111.23 lakh, net loss Rs(7,458.13) lakh, TCI Rs(8,896.19) lakh for Q1 FY27; reviewed instead by other (foreign) auditors under local regulations, reports furnished to KJCo by management | Material — 0 of 8 consolidated foreign subsidiaries were reviewed directly by the Statutory Auditor; conclusion relies entirely on other auditors' reports furnished by management. Flag SOURCE_VERIFY_NEEDED / AUDIT_SCOPE for A3-A5 |
| 6(b) | 306-323 | Other Matters (b): foreign subsidiaries' results prepared under local GAAP, reviewed by other auditors under local standards; Parent's management converted to Indian GAAP; KJCo reviewed the CONVERSION ADJUSTMENTS only (not the underlying foreign-GAAP figures) | Two-layer reliance: other-auditor review of local-GAAP figures + KJCo review of conversion only |
| 6(c) | 325-328 | Other Matters (c) [source renders as "()" — see Section 5/reconciliation]: consolidated Q4 FY26 comparative figures are balancing figures (audited FY less limited-reviewed 9M), same structure as standalone para 5 | OCR_CORRUPTION on the "(c)" label itself — content unambiguous from context |
| — | 330 | Closing line: "Our conclusion on the Statement is not modified in respect of above matters" | No Emphasis of Matter paragraph present; no Going Concern language present — both checked, absent |
| Signature block | 332-346 | Ravi Dakliya, Partner, Membership No. 304534, UDIN 26304534DKBRDD2636, Place Gurugram, Dated 10-Aug-2026 | Same partner, same date, DIFFERENT UDIN from standalone report (expected — one UDIN per report) — see Section 9 |

---
## 8. NOTE-4 CONSOLIDATION ENTITY LIST (9 entities)
Lines 474-484 (primary) / 638-648 (OCR). Cross-checked against auditor consolidated-report para 4 (lines 270-278), which lists the same 8 subsidiaries (excludes the parent, item i).

| # | Entity | Relationship | Line | Flags |
|---|---|---|---|---|
| i | Exicom Tele-Systems Limited | Holding Company (the Parent) | 475/639 | — |
| ii | Exicom Tele-Systems (Singapore) Pte. Ltd. | Wholly owned subsidiary | 476/640 | — |
| iii | Horizon Tele-Systems SDN BHD | Wholly owned subsidiary of (ii) | 477/641 | — |
| iv | Exicom Power Solutions B.V., Netherlands | Subsidiary (no longer wholly owned) | 478/642 | **ENTITY_CHANGE** — "ceased to be a wholly-owned subsidiary of the Company w.e.f. April 22, 2026" (footnote, line 484/648). Now carries a 7.8% minority per COMPANY MEMORY context (not itself stated as a percentage in this filing — the filing only states "Subsidiary" without quantifying the retained stake or naming the new minority holder). Direct consequence: P&L rows 26/28/30 (NCI attribution) newly populate this quarter. Flag SOURCE_VERIFY_NEEDED — 7.8% figure and counterparty name are NOT stated anywhere in this filing itself; they come only from prior-quarter memory, not this quarter's anchored evidence |
| v | Tritium NexGen Solutions B.V., Netherlands | Wholly owned subsidiary of (iv) | 479/643 | Held via Exicom Power Solutions B.V., which is itself no longer wholly owned — downstream WOS status of (v)-(viii) is therefore indirectly diluted by the same 22-Apr-2026 event, though each is separately labelled "wholly owned subsidiary of Exicom Power Solutions B.V." in the filing text |
| vi | Tritium Power Solutions, USA | Wholly owned subsidiary of (iv) | 480/644 | Same indirect-dilution note as (v) |
| vii | Tritium Power Solutions, UK | Wholly owned subsidiary of (iv) | 481/645 | Same indirect-dilution note as (v) |
| viii | Tritium Power Solutions Pty, Australia | Wholly owned subsidiary of (iv) | 482/646 | Same indirect-dilution note as (v) |
| ix | Horizon Power Solution L.L.C-FZ, Dubai | (relationship not specified beyond consolidation — no "wholly owned" or parent-chain qualifier given, unlike items ii-viii) | 483/647 | NOT_FOUND — relationship type to Group unstated in filing text; flag for A3 |

Auditor para 6(a) (Section 7b) states 8 of these 9 entities' interim figures were NOT reviewed by KJCo (reviewed instead by other/foreign auditors) — i.e., every entity in this list except item i (the Parent itself) falls under the unreviewed-by-primary-auditor disclosure.

No prior-quarter ledger exists for this ticker (first quarterly-pipeline run) so no entity add/remove/rename diff is possible against a prior ENUMERATED ledger; the ENTITY_CHANGE flag above is corroborated only by the Notion COMPANY MEMORY (prior_context.md), which is weighed, not anchored.

---
## 9. SIGNATURE BLOCKS (4 rows)

| # | Signatory | Designation | Line | Timestamp / Date | Flags |
|---|---|---|---|---|---|
| 1 | Sangeeta Karnatak | Company Secretary & Compliance Officer | 106-115 | Digitally signed 2026.08.10, 13:59:46 +05'30' | Board meeting concluded 13:40 (1:40 p.m.); CS signature at 13:59:46 is ~19 minutes AFTER conclusion — consistent/expected, no red flag. Recorded per task instruction for explicit comparison |
| 2 | Ravi Dakliya | Partner, Khandelwal Jain & Co. (standalone review report) | 197-211 | Place: Gurugram, Dated: August 10, 2026 (no intraday timestamp — typed signature block, not a digital-signature timestamp) | UDIN 26304534YGRZKC8103 |
| 3 | Ravi Dakliya | Partner, Khandelwal Jain & Co. (consolidated review report) | 332-346 | Place: Gurugram, Dated: August 10, 2026 (no intraday timestamp) | UDIN 26304534DKBRDD2636 — different UDIN from row 2 as expected (one per report), same partner same date |
| 4 | Anant Nahata | Managing Director Cum CEO, DIN 02216037 | 488-494/652-660 | "By the order of the Board", Place: Gurugram, Dated: August 10, 2026 (no intraday timestamp; sign-off block at foot of the financial-results statement itself, page 10) | Not marked as a digital signature in the extract (no "digitally signed by" wrapper unlike row 1) — flag NOT_FOUND for signature-method detail if material |

---
## SUMMARY OF FLAGS RAISED (for A3/A4 reconciliation)
ZERO_STANDING (12 occurrences: P&L rows 19,22,25,26,27,28,29,30 on SA side [8] + Segment rows 12,16 on both SA and Consol sides [2+2]) ·
ENTITY_CHANGE (Note 4, entity iv, Exicom Power Solutions B.V.) ·
NUMERIC_RECONCILED (P&L rows 12,13,14,16,17,20 — see Section 5 log) ·
NUMERIC_QA (Note 2b rows 1,2,5; P&L row17 C-Q1FY27 minor residual) ·
SOURCE_VERIFY_NEEDED (P&L row14 Exceptional Items Q1FY27 nil-vs-nonzero conflict with task-injected assumption; auditor para 6(a) full audit-scope reliance on other auditors; Note-4 entity iv 7.8%/counterparty not stated in-filing) ·
OCR_CORRUPTION (auditor consol report para 6(c) label rendered "()") ·
NOT_FOUND (Note 2b rows 1-2 figures/labels; Board Outcome item 2b AGM date/record date/other business items; Note-4 entity ix relationship type; signature-4 digital-signature method) ·
CHANGE_FROM_PRIOR (Note 3(e)/2b row4 — R&D IPO-proceeds fully utilised this quarter vs Rs8.83 Cr unutilised per prior-quarter memory) ·
GENERIC_REGROUPING_NOTE (Note 6, no specifics named)

No prior-quarter ENUMERATED ledger exists for EXICOM (first run) — no DROPPED_SLIDE/DROPPED_LINE-ITEM diff possible against a prior A2 ledger; all "change from prior" flags above are sourced from the Notion COMPANY MEMORY only (weighed, not anchored).
