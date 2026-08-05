# LEDGER — Vaibhav Global Limited (VAIBHAVGBL) — Q1 FY27 — Results Filing (Reg 33)
Source: extract_results_vaibhavgbl_q1fy27.txt | 654 lines | 14 pages | Lakhs (x0.01 -> Cr)
Prior-quarter ledger: NONE (first-time coverage; no diff/ENTITY_CHANGE baseline exists yet)

```
=== A2 COUNT TEST ===
category: notes             grep_count: 15   sweep_count: 15   match: yes
category: line_items        grep_count: 81   sweep_count: 81   match: yes
category: zero_standing     grep_count: 4    sweep_count: 4    match: yes
category: agenda_items      grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras     grep_count: 13   sweep_count: 13   match: yes
category: entities          grep_count: 14   sweep_count: 14   match: yes
category: annexure_rows     grep_count: 11   sweep_count: 11   match: yes
category: signature_blocks  grep_count: 7    sweep_count: 7    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methods used (all run against the extract file with Bash, cross-checked by manual read of every line 15-654):
- notes: `grep -n -E "^\s*[0-9]+\)\s"` (notes use "N)" numbering, distinct from statement-line "N." numbering)
- line_items: per-table `grep -c -E "[0-9]{2,}\.[0-9]{2}|[[:space:]]-[[:space:]]|[[:space:]]-$"` over each table's line range, summed across 4 tables
- zero_standing: `grep -n -E "[[:space:]]-[[:space:]]+-[[:space:]]+-[[:space:]]+-[[:space:]]*$"` inside consolidated P&L range (all-dash rows across all 4 reporting periods)
- agenda_items: `grep -n -E "^\s*[0-9]+\.\s"` restricted to Board Outcome letter (page 1)
- auditor_paras: `grep -n -E "^\s*[0-9]+\.\s"` restricted to both Limited Review Report ranges
- entities: `grep -c -E "subsidiary|Parent Company|Controlled Trust"` in Annexure I (BSR&Co entity list), cross-checked against lettered/roman-numeral entity list in Note 3
- annexure_rows: `grep -n -E "^\s*[a-f]\)\s"` restricted to pages 13-14 (ESOP/RSU grant table + EY appointment table)
- signature_blocks: `grep -n -E "Digitally signed|^\s*Partner|Managing Director"`

---

## 1. BOARD OUTCOME — AGENDA ITEMS (Regulation 30 letter, page 1, lines 25-63)
Board meeting: commenced 15:30 IST, concluded 20:00 IST — **4.5 hour meeting** (long relative to a routine quarterly-results-only meeting; consistent with a meeting that also cleared an ESOP grant and an internal auditor appointment, not a flag on its own but recorded as required).

| # | Line | Agenda Item | First 15 words | Flags |
|---|------|-------------|-----------------|-------|
| 1 | 30-31 | Approval of unaudited Financial Results (Consolidated and Standalone) under Ind AS, Q1 FY27 | "The unaudited Financial Results (Consolidated and Standalone) under Ind AS for the quarter ended 30th June, 2026." | — |
| 2 | 33-37 | Declared Interim Dividend Rs. 1.50/share (FV Rs. 2/-), record date 12 Aug 2026, FY26-27 | "Declared an Interim Dividend of Rs. 1.50/- per Equity Share (on the face value of Rs. 2/-...)" | — |
| 3 | 39-40 | Grant of Stock Options and Restricted Stock Units (MSOP/RSU/ESOP plans) | "The Grant of Stock Options and Restricted Stock Units convertible into equal number of Equity Shares..." | see Section 7 (annexure detail) |
| 4 | 42-43 | Appointment of Ernst & Young LLP (EY) as Internal Auditors, FY27+FY28 (2 years) | "Based on the recommendation of audit committee, the appointment of Ernst & Young LLP ('EY'), as..." | see Section 7 (annexure detail) |

No AR/AGM approval, no record date beyond dividend, no director appointment/resignation, no statutory auditor change, no scrutinizer, no capital-raising enabling resolution present in this Board Outcome — confirmed absent by full read, not merely un-grepped.

---

## 2. NOTES — CONSOLIDATED (page 4-5, lines 155-231; numbering style "N)")

| Note # | Line | First 15 words | Flags |
|--------|------|-----------------|-------|
| 1 | 157-159 | "The above statement of unaudited consolidated financial results for the quarter ended 30 June 2026..." (Audit Committee/Board approval, statutory auditor review) | — |
| 2 | 161-163 | "These statement of unaudited consolidated financial results have been prepared in accordance with Indian Accounting..." (Ind AS / Reg 33 basis) | — |
| 3 | 165-180 | "The unaudited consolidated financial results include the financial results of the Parent Company and the..." — full entity list (see Section 6) | — |
| 4 | 182-184 | "The Parent Company has allotted 276,874 equity shares having face value of Rs. 2/- each..." (ESOP allotments, exercise price range Rs.2.00-188.95) | — |
| 5 | 186-190 | "Item exceeding 10% of total expenditure (included in other expenses):" — Content and broadcasting expenses line item | see Section 3 (line item) |
| 6 | 194-196 | "The Board of Directors of the Parent Company has declared interim dividend of Rs. 1.5/- per..." (duplicate of agenda item 2, dividend mechanics) | — |
| 7 | 198-200 | "The figures for the preceding quarter ended 31 March 2026 are the balancing figures between the..." (Q4 balancing-figure caveat, not separately audited) | — |
| 8 | 202-229 | "During the year ended 31 March 2026, certain subsidiaries of the Group operating in the United..." — IEEPA/Section 122 tariff refund saga | MULTI_PARA (spans pages 4-5, 4 sub-paragraphs: original contingent asset recognition, refund receipt Rs.3,839.90L + interest Rs.148.04L, Rs.1,425.73L further Section 122 tariffs paid, and CIT/Federal Circuit appeal status as of 24 July 2026 — not yet probable, not recognized) |
| 9 | 231 | "Segment information as per Ind AS – 108, 'Operating Segment' is disclosed in Annexure – I." | — |

## 3. NOTES — STANDALONE (page 7, lines 289-313; numbering style "N)")

| Note # | Line | First 15 words | Flags |
|--------|------|-----------------|-------|
| 1 | 291-294 | "The above statement of unaudited standalone financial results for the quarter ended 30 June 2026..." | — |
| 2 | 296-298 | "These statement of unaudited standalone financial results have been prepared in accordance with Indian Accounting..." | — |
| 3 | 300-302 | "The Company has allotted 276,874 equity shares having face value of Rs. 2/- each, under..." (same ESOP allotment as consol Note 4) | — |
| 4 | 304-306 | "The Board of Directors of the Company has declared interim dividend of Rs. 1.5/- per fully..." | — |
| 5 | 308-310 | "The figures for the preceding quarter ended 31 March 2026 are the balancing figures between the..." | — |
| 6 | 312-313 | "As per Ind AS 108, 'Operating Segments', the Company has disclosed the segment information only..." (standalone segment data intentionally absent, cross-refers to consol) | — |

Notes subtotal: 9 + 6 = **15**.

---

## 4. LINE ITEMS — CONSOLIDATED P&L (page 2, lines 78-121) — 34 rows

| # | Line | Particulars | Q1FY27 (30-Jun-26) | Q4FY26 (31-Mar-26) | Q1FY26 (30-Jun-25) | FY26 (audited) | Flags |
|---|------|-------------|----|----|----|----|-------|
| 1 | 79 | Revenue from operations | 91,707.34 | 93,470.74 | 81,373.71 | 3,69,178.57 | — |
| 2 | 80 | Other income | 531.34 | 1,254.46 | 1,307.41 | 4,126.99 | — |
| 3 | 81 | Total income | 92,238.68 | 94,725.20 | 82,681.12 | 3,73,305.56 | — |
| 4 | 83 | Cost of materials consumed | 9,863.73 | 15,857.31 | 8,044.46 | 39,906.35 | — |
| 5 | 84 | Purchases of stock-in-trade | 21,692.69 | 14,138.13 | 21,864.58 | 87,921.41 | — |
| 6 | 85 | Change in inventories of FG/stock-in-trade/WIP | (4,127.88) | 1,992.59 | (2,207.88) | (375.11) | — |
| 7 | 86 | Employee benefits expense | 15,287.61 | 15,511.50 | 14,900.56 | 61,681.79 | — |
| 8 | 87 | Finance costs | 454.29 | 430.55 | 350.27 | 1,493.76 | — |
| 9 | 88 | Depreciation and amortisation expenses | 2,662.96 | 2,792.36 | 2,529.44 | 10,288.50 | — |
| 10 | 89 | Other expenses (Refer note 5) | 39,317.99 | 37,629.18 | 32,617.90 | 1,44,221.15 | — |
| 11 | 90 | Total expenses | 85,151.39 | 88,351.62 | 78,099.33 | 3,45,137.85 | — |
| 12 | 91 | Profit before exceptional items and tax (1-2) | 7,087.29 | 6,373.58 | 4,581.79 | 28,167.71 | — |
| 13 | 92 | Exceptional items | - | 17.53 | - | 17.53 | dash in Q1FY27 & Q1FY26 but not ALL periods (nonzero in FY26/Q4FY26) — not ZERO_STANDING |
| 14 | 93 | Profit after exceptional items (3+4) | 7,087.29 | 6,391.11 | 4,581.79 | 28,185.24 | — |
| 15 | 95 | Current tax | 2,296.95 | 1,753.34 | 1,737.19 | 8,088.27 | — |
| 16 | 96 | Deferred tax credit | (847.92) | (4,476.21) | (918.59) | (6,515.94) | — |
| 17 | 97 | Total tax expense / (credit) | 1,449.03 | (2,722.87) | 818.60 | 1,572.33 | — |
| 18 | 98 | Profit for the period / year (5-6) | 5,638.26 | 9,113.98 | 3,763.19 | 26,612.91 | — |
| 19 | 101 | Remeasurement of defined benefit plans | 47.97 | 3.65 | (39.00) | 191.90 | — |
| 20 | 102 | Tax relating to remeasurement of defined benefit plans | (12.08) | (0.16) | 13.63 | (65.94) | — |
| 21 | 104 | Exchange difference on translation of foreign operations | (80.27) | 4,931.10 | 2,190.77 | 10,959.16 | — |
| 22 | 105 | Tax relating to exchange difference on translation of foreign operations | - | - | - | - | **ZERO_STANDING** (dash in all 4 periods — template line for a tax event that has never occurred on FX translation) |
| 23 | 106 | Total comprehensive income / (loss) [OCI subtotal] | (44.38) | 4,934.59 | 2,165.40 | 11,085.12 | — |
| 24 | 107 | Total comprehensive income for the period / year (7+8) | 5,593.88 | 14,048.57 | 5,928.59 | 37,698.03 | — |
| 25 | 109 | Profit/(loss) attributable to: Owners of VGL | 5,638.26 | 9,113.98 | 3,763.19 | 26,612.91 | — |
| 26 | 110 | Profit/(loss) attributable to: Non-controlling interests | - | - | - | - | **ZERO_STANDING** (all wholly-owned subs; NCI template line never populated) |
| 27 | 112 | OCI attributable to: Owners of VGL | (44.38) | 4,934.59 | 2,165.40 | 11,085.12 | — |
| 28 | 113 | OCI attributable to: Non-controlling interests | - | - | - | - | **ZERO_STANDING** |
| 29 | 115 | Total comprehensive income attributable to: Owners of VGL | 5,593.88 | 14,048.57 | 5,928.59 | 37,698.03 | — |
| 30 | 116 | Total comprehensive income attributable to: Non-controlling interests | - | - | - | - | **ZERO_STANDING** |
| 31 | 117 | Paid-up equity share capital (FV Rs.2/-) | 3,346.01 | 3,340.48 | 3,328.68 | 3,340.48 | — |
| 32 | 118 | Other equity | (blank) | (blank) | (blank) | 1,61,452.89 | Quarterly columns not disclosed — standard interim-statement convention (Other Equity shown only for audited FY column), not a ZERO_STANDING per se |
| 33 | 120 | EPS Basic (Rs.) | 3.37 | 5.47 | 2.26 | 15.97 | — |
| 34 | 121 | EPS Diluted (Rs.) | 3.33 | 5.40 | 2.24 | 15.75 | — |

## 5. LINE ITEMS — CONSOLIDATED SEGMENT (Annexure I, page 3, lines 130-152) — 20 rows

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | 131 | Segment revenue — USA | 59,800.88 | 59,578.22 | 49,467.98 | 2,28,821.40 | — |
| 2 | 132 | Segment revenue — UK | 25,007.87 | 25,287.63 | 22,821.88 | 1,03,467.88 | — |
| 3 | 133 | Segment revenue — India | 16,293.43 | 14,092.64 | 14,737.74 | 58,513.32 | — |
| 4 | 134 | Segment revenue — Europe (ex-UK) | 10,602.20 | 10,713.12 | 8,704.00 | 40,757.49 | — |
| 5 | 135 | Segment revenue — Rest of world | 11,737.69 | 9,586.15 | 9,492.12 | 40,552.15 | — |
| 6 | 136 | Less: Intersegment eliminations (revenue) | (31,734.73) | (25,787.02) | (23,850.01) | (1,02,933.67) | — |
| 7 | 137 | Revenue from operations (total, ties to P&L line 1) | 91,707.34 | 93,470.74 | 81,373.71 | 3,69,178.57 | — |
| 8 | 139 | Segment results (PBIT) — USA | 5,831.98 | 3,283.40 | 3,374.70 | 16,430.61 | — |
| 9 | 140 | Segment results (PBIT) — UK | (47.48) | (2,256.16) | 978.27 | 9,848.02 | — |
| 10 | 141 | Segment results (PBIT) — India | 2,123.69 | 4,529.21 | 1,406.91 | 17,698.92 | — |
| 11 | 142 | Segment results (PBIT) — Europe (ex-UK) | (288.50) | (313.60) | 1,287.87 | 1,144.53 | — |
| 12 | 143 | Segment results (PBIT) — Rest of world | 857.10 | 2,115.06 | 1,141.38 | 12,607.46 | — |
| 13 | 144 | Less: Intersegment eliminations (results) | (935.21) | (553.78) | (3,257.07) | (28,068.07) | — |
| 14 | 145 | Subtotal (segment results) | 7,541.58 | 6,804.13 | 4,932.06 | 29,661.47 | — |
| 15 | 147 | Exceptional items — USA | - | 2,969.08 | - | 2,969.08 | dash Q1FY27/Q1FY26 only, not all periods |
| 16 | 148 | Exceptional items — UK | - | (2,501.55) | - | (2,501.55) | dash Q1FY27/Q1FY26 only, not all periods |
| 17 | 149 | Exceptional items — India | - | (450.00) | - | (450.00) | dash Q1FY27/Q1FY26 only, not all periods |
| 18 | 150 | Subtotal (after exceptional items) | 7,541.58 | 6,821.66 | 4,932.06 | 29,679.00 | — |
| 19 | 151 | Less: Finance cost | (454.29) | (430.55) | (350.27) | (1,493.76) | — |
| 20 | 152 | Total profit before tax (ties to P&L line 12) | 7,087.29 | 6,391.11 | 4,581.79 | 28,185.24 | — |

## 6a. LINE ITEM — CONSOLIDATED NOTE 5 SUB-TABLE (page 4, lines 186-190) — 1 row

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | 190 | Content and broadcasting expenses (>10% of total expenditure, within Other expenses) | 19,654.98 | 18,910.53 | 16,502.55 | 72,443.02 | — |

## 6. LINE ITEMS — STANDALONE P&L (page 6, lines 256-286) — 26 rows

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | 256 | Revenue from operations | 15,752.12 | 13,584.69 | 14,215.46 | 56,327.61 | — |
| 2 | 257 | Other income | 495.87 | 4,418.80 | 998.00 | 15,004.63 | — |
| 3 | 258 | Total income | 16,247.99 | 18,003.49 | 15,213.46 | 71,332.24 | — |
| 4 | 260 | Cost of materials consumed | 5,034.53 | 7,711.60 | 9,734.39 | 33,450.57 | — |
| 5 | 261 | Purchases of stock-in-trade | 3,929.24 | 897.56 | 1,984.73 | 4,553.28 | — |
| 6 | 262 | Change in inventories of FG/stock-in-trade/WIP | 712.59 | 548.74 | (1,953.40) | (700.64) | — |
| 7 | 263 | Employee benefits expense | 1,768.73 | 1,520.76 | 1,582.24 | 6,089.28 | — |
| 8 | 264 | Finance costs | 168.70 | 216.14 | 244.60 | 968.53 | — |
| 9 | 265 | Depreciation and amortization expenses | 200.86 | 200.43 | 187.38 | 765.45 | — |
| 10 | 266 | Other expenses | 2,637.58 | 2,725.89 | 2,371.96 | 10,103.23 | — |
| 11 | 267 | Total expenses | 14,452.23 | 13,821.12 | 14,151.90 | 55,229.70 | — |
| 12 | 268 | Profit before exceptional items and tax (1-2) | 1,795.76 | 4,182.37 | 1,061.56 | 16,102.54 | — |
| 13 | 269 | Exceptional items | - | 5,842.88 | - | 5,842.88 | dash Q1FY27/Q1FY26 only, not all periods |
| 14 | 270 | Profit after exceptional items (3+4) | 1,795.76 | 10,025.25 | 1,061.56 | 21,945.42 | — |
| 15 | 272 | Current tax | 358.11 | 467.67 | 178.66 | 1,228.92 | — |
| 16 | 273 | Deferred tax | 109.62 | (4,753.16) | (19.08) | (4,938.98) | — |
| 17 | 274 | Total tax expense | 467.73 | (4,285.49) | 159.58 | (3,710.06) | — |
| 18 | 275 | Profit for the period / year (5-6) | 1,328.03 | 14,310.74 | 901.98 | 25,655.48 | — |
| 19 | 278 | Remeasurement of defined benefit plans | 45.12 | (7.78) | (39.00) | 180.47 | — |
| 20 | 279 | Tax relating to remeasurement of defined benefit plans | (11.36) | 2.72 | 13.63 | (63.06) | — |
| 21 | 280 | Total other comprehensive income / (loss) | 33.76 | (5.06) | (25.37) | 117.41 | — |
| 22 | 281 | Total comprehensive income for the period / year (7+8) | 1,361.79 | 14,305.68 | 876.61 | 25,772.89 | — |
| 23 | 282 | Paid-up equity share capital (FV Rs.2/-) | 3,346.01 | 3,340.48 | 3,328.68 | 3,340.48 | — |
| 24 | 283 | Other equity | (blank) | (blank) | (blank) | 84,162.83 | Quarterly columns not disclosed — standard interim convention |
| 25 | 285 | EPS Basic (Rs.) | 0.79 | 8.58 | 0.54 | 15.40 | — |
| 26 | 286 | EPS Diluted (Rs.) | 0.78 | 8.48 | 0.54 | 15.19 | — |

No Balance Sheet and no Cash Flow Statement are present anywhere in this extract (confirmed by full manual read of all 654 lines) — this Reg 33 quarterly filing contains only the P&L statements, the segment annexure, notes, and the two Limited Review Reports. Nothing to enumerate for those two statement types this quarter; recorded here so the absence is a documented finding, not a silent gap.

Line items subtotal: 34 + 20 + 1 + 26 = **81**. Of these, **4** carry ZERO_STANDING (rows 22, 26, 28, 30 in Section 4, all consolidated, all NCI-related or FX-translation-tax related — consistent with a wholly-owned-subsidiary group structure with no minority interests, confirmed against Section 6 entity list where every subsidiary is "wholly owned").

---

## 7. ANNEXURE DETAIL TABLES (page 13-14) — 11 rows

### 7a. ESOP/RSU Grant Details (Reg 30 / Para A Schedule III disclosure, page 13, lines 553-587) — 6 rows x 3 plans

| Row | Line | Particulars | VGL MSOP Plan-2021 | VGL RSU Plan-2019 | VGL ESOP Plan-2021 | Flags |
|-----|------|-------------|---------------------|---------------------|----------------------|-------|
| a | 556-560 | Brief details of options granted | 93,170 Stock Options (MSOPs) | 11,858 RSUs | 14,970 Stock Options (ESOPs) | — |
| b | 561-571 | Scheme in terms of SEBI (SBEB & SE) Regulations 2021 | Yes | Yes | Yes | — |
| c | 572-576 | Total shares covered | 93,170 shares (FV Rs.2/-) | 11,858 shares (FV Rs.2/-) | 14,970 shares (FV Rs.2/-) | — |
| d | 577 | Exercise price | Rs. 2/- | Rs. 2/- | Rs. 2/- | — |
| e | 578-580 | Vesting schedule | 100% on completion of 2 years | 20%/30%/50% over yrs 1/2/3 | (same tranche schedule as RSU column per source layout) | — |
| f | 581-584 | Exercise window | 7 years from vesting | 3 months from respective vesting | 3 months from respective vesting | — |
| — | 586-587 | Footnote (unnumbered): "requirements prescribed under Clause 10(g) to (n) of Para B of Annexure 18 ... not applicable" | — | — | — | unnumbered footnote, manual-sweep catch |

### 7b. Appointment of Internal Auditors — Ernst & Young LLP (Reg 30, page 14, lines 607-639) — 5 rows

| Row | Line | Particulars | Detail | Flags |
|-----|------|-------------|--------|-------|
| a | 611-615 | Reason for change | Appointment of EY as Internal Auditors | — |
| b | 617 | Date of appointment | 4 August 2026 | — |
| c | 619 | Term of appointment | 2 years — FY 2026-27 and FY 2027-28 | — |
| d | 626-633 | Brief profile | Global assurance/tax/transaction/advisory firm; IA services scope: risk assessment, process improvement, technology integration, regulatory compliance, stakeholder engagement | — |
| e | 636-638 | Disclosure of director relationships | Not applicable (not a director appointment) | — |

Annexure rows subtotal: 6 + 5 = **11**.

---

## 8. AUDITOR REPORTS — LIMITED REVIEW, CONSOLIDATED (pages 8-10, BSR & Co. LLP, lines 328-460, OCR'd)

| Para | Line | Type | First 15 words | Flags |
|------|------|------|-----------------|-------|
| Title/addressee | 335-343 | Header | "Limited Review Report on unaudited consolidated financial results of Vaibhav Global Limited..." — addressed to Board of Directors | — |
| 1 | 345-350 | Scope statement | "We have reviewed the accompanying Statement of unaudited consolidated financial results of Vaibhav Global..." | — |
| 2 | 352-357 | Responsibility statement | "This Statement, which is the responsibility of the Parent's management and approved by the Parent's..." Ind AS 34 basis | — |
| 3 | 359-368 | Review standard (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." — explicit "we do not express an audit opinion" | — |
| (unnumbered) | 369-370 | Continuation of scope | "We also performed procedures in accordance with the circular issued by the Securities and Exchange..." Reg 33(8) circular procedures | UNNUMBERED_PARA (not separately numbered in source; caught by manual sweep, excluded from the numbered-paragraph gate count) |
| 4 | 372 | Entity list cross-reference | "The Statement includes the results of the entities mentioned in Annexure I to the Statement." | — |
| 5 | 374-378 | Other Matters (Q4 balancing-figure caveat) | "Attention is drawn to the fact that the figures for the three months ended 31 March..." | — |
| 6 | 380-386 | Conclusion (unmodified) | "Based on our review conducted and procedures performed as stated in paragraph 3 above and..." — "nothing has come to our attention" | opinion type: UNMODIFIED / no qualification |
| 7 | 400-418 | Other auditors reliance (Other Matters) | "We did not review the interim financial information of four subsidiaries included in the Statement..." — 4 subsidiaries, revenue Rs.10,560.67L, PAT Rs.414.01L, TCI Rs.414.01L, reviewed by other auditors, furnished by Parent's management | 4 subsidiaries **not named** in the extract text (INDETERMINATE — names not disclosed in this filing); also notes foreign subsidiaries' local-GAAP conversion reviewed by BSR |
| (unnumbered) | 419 | Closing sentence to para 7 | "Our conclusion is not modified in respect of this matter." | UNNUMBERED_PARA |
| Signature block | 420-427 | Attestation | ForBSR&Co.LLP, Gaurav Mahajan, Partner, Firm Reg. 101248W/W-100022, Chandigarh, Membership 507857, dated 04 Aug 2026, UDIN:26507857CFMFLQ7321 | see Section 9 |

Numbered paragraphs (gate count): 7 (paras 1-7). No Going Concern paragraph present; no Emphasis of Matter heading used explicitly (para 5 functions as an Other-Matters-style balancing-figure note); opinion is unmodified/clean review conclusion in both paragraph 6 and the standalone equivalent below.

## 9. AUDITOR REPORT — LIMITED REVIEW, STANDALONE (pages 11-12, BSR & Co. LLP, lines 463-546, OCR'd)

| Para | Line | Type | First 15 words | Flags |
|------|------|------|-----------------|-------|
| Title/addressee | 470-478 | Header | "Limited Review Report on unaudited standalone financial results of Vaibhav Global Limited..." | — |
| 1 | 480-484 | Scope statement | "We have reviewed the accompanying Statement of unaudited standalone financial results of Vaibhav Global..." — includes VGL Employee Stock Option Welfare Trust results | — |
| 2 | 485-491 | Responsibility statement | "This Statement, which is the responsibility of the Company's management and approved by its Board..." Ind AS 34 basis | — |
| 3 | 493-500 | Review standard (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." — "we do not express an audit opinion" | — |
| 4 | 502-506 | Other Matters (Q4 balancing-figure caveat) | "Attention is drawn to the fact that the figures for the three months ended 31 March..." | — |
| 5 | 508-514 | Conclusion (unmodified) | "Based on our review conducted as above and based on the consideration of the review..." | opinion type: UNMODIFIED / no qualification |
| 6 | 516-522 | Other auditor reliance (Trust) | "We did not review the interim financial results of the Trust included in the Statement of..." — Trust revenue Rs. Nil, net loss Rs.0.49L, reviewed by other auditor | Trust financials management-furnished/other-auditor-reviewed, not reviewed by BSR directly |
| (unnumbered) | 532 | Closing sentence to para 6 | "Our conclusion is not modified in respect of this matter." | UNNUMBERED_PARA |
| Signature block | 533-543 | Attestation | ForBSR&Co.LLP, Gaurav Mahajan, Partner, Firm Reg. 101248W/W-100022, Chandigarh, Membership 507857, dated 04 Aug 2026, UDIN:26507857XCEAGI3776 | see Section 9 (distinct UDIN from consolidated report) |

Numbered paragraphs (gate count): 6 (paras 1-6). No Going Concern paragraph. Same auditor, same partner, same signing date as the consolidated report; two distinct UDINs (one per statement, correct practice).

Auditor paragraphs subtotal (numbered only, gate count): 7 + 6 = **13**. Three additional unnumbered paragraphs identified by manual sweep (lines 369-370, 419, 532) — recorded above, excluded from the strict numbered-paragraph gate since the source itself does not number them, but not dropped from the ledger.

---

## 10. CONSOLIDATION ENTITY LIST (cross-checked: Note 3 body list [lines 165-180] vs. Auditor Annexure I [lines 435-459]) — 14 entities

No prior-quarter ledger exists for this ticker, so ENTITY_CHANGE cannot be evaluated this quarter — this list is the baseline for all future diffs.

| # | Entity | Jurisdiction | Relationship | Source lines |
|---|--------|-------------|--------------|---------------|
| 1 | Vaibhav Global Limited | India | Parent Company | 438 (Annexure I); implicit head of Note 3 list |
| 2 | VGL Retail Ventures Limited | Mauritius | Wholly owned subsidiary | 168, 439-440 |
| 3 | Shop TJC Limited | UK | Step-down subsidiary (wholly owned), under VGL Retail Ventures | 169, 441-442 |
| 4 | Shop LC Global Inc. | USA | Step-down subsidiary (wholly owned), under Shop TJC | 170, 443-444 |
| 5 | Mindful Souls BV | Netherlands | Step-down subsidiary (wholly owned), under Shop TJC | 171, 445-446 |
| 6 | STS Global Supply Limited | Hong Kong | Wholly owned subsidiary | 172, 447-448 |
| 7 | Pt. STS Bali | Indonesia | Step-down subsidiary (wholly owned), under STS Global Supply | 173, 449-450 |
| 8 | STS (Guangzhou) Trading Limited | China | Step-down subsidiary (wholly owned), under STS Global Supply | 174, 451-452 |
| 9 | STS Jewels Inc. | USA | Wholly owned subsidiary | 175, 453 |
| 10 | STS Global Limited | Thailand | Wholly owned subsidiary | 176, 454 |
| 11 | STS Global Limited | Japan | Wholly owned subsidiary | 177, 455 |
| 12 | Vaibhav Lifestyle Limited | India | Wholly owned subsidiary | 178, 456 |
| 13 | Shop LC GmbH | Germany | Wholly owned subsidiary | 179, 457 |
| 14 | Vaibhav Global Employee Stock Option Welfare Trust | India | Controlled Trust (also consolidated separately into the Standalone statement per LRR para 1) | 180, 458-459 |

Cross-check: Note 3 (13 entities excluding parent) + implied parent = 14; Auditor Annexure I lists all 14 explicitly including parent. Counts reconcile.

Note: 4 of these subsidiaries are the ones referenced, but not individually named, in Consolidated LRR para 7 as not directly reviewed by BSR & Co. (reviewed by other auditors, furnished by management) — which 4 of the 14 cannot be determined from this extract (flag below).

---

## 11. DIGITAL SIGNATURE / SIGN-OFF BLOCKS — 7 total

| # | Line | Signatory | Designation | Document | Timestamp | Flags |
|---|------|-----------|-------------|----------|-----------|-------|
| 1 | 53-61 | Yashasvi Pareek | Company Secretary & Compliance Officer (M.No. A39220) | Board Outcome letter (Reg 30), page 1 | 2026.08.04 21:58:52 +05'30' | Board meeting concluded 20:00 IST; signature 21:58:52 IST is AFTER conclusion — no SIGNATURE_BEFORE_MEETING flag |
| 2 | 236-243 | Sunil Agrawal | Managing Director (DIN: 00061142) | Consolidated results statement sign-off, page 5 | typed, not digitally timestamped; Place: Dusseldorf, Germany; Date: 04 August 2026 | — |
| 3 | 318-325 | Sunil Agrawal | Managing Director (DIN: 00061142) | Standalone results statement sign-off, page 7 | typed, not digitally timestamped; Place: Dusseldorf, Germany; Date: 04 August 2026 | — |
| 4 | 420-427 | Gaurav Mahajan | Partner, BSR & Co. LLP, Firm Reg. 101248W/W-100022, Chandigarh, Membership 507857 | Consolidated LRR signature block, page 9 | 04 August 2026; UDIN:26507857CFMFLQ7321 | — |
| 5 | 533-543 | Gaurav Mahajan | Partner, BSR & Co. LLP (same registration/membership as above) | Standalone LRR signature block, page 12 | 04 August 2026; UDIN:26507857XCEAGI3776 | distinct UDIN from consolidated (correct — one UDIN per report) |
| 6 | 591-596 | Yashasvi Pareek | Company Secretary & Compliance Officer | ESOP/RSU grant annexure (Reg 30), page 13 | 2026.08.04 21:59:52 +05'30' | after meeting conclusion — no flag |
| 7 | 644-649 | Yashasvi Pareek | Company Secretary & Compliance Officer | EY internal auditor appointment annexure (Reg 30), page 14 | 2026.08.04 22:00:16 +05'30' | after meeting conclusion — no flag |

---

## FLAG SUMMARY

- **ZERO_STANDING** x4 — Section 4, rows 22/26/28/30 (all consolidated: tax on FX-translation OCI, and 3x non-controlling-interest attribution lines — consistent template signal that this Group carries zero NCI, i.e., every subsidiary is wholly owned, per Section 10).
- **UNNUMBERED_PARA** x3 — Section 8/9, source-formatted but un-numbered continuations/closing sentences in both Limited Review Reports (lines 369-370, 419, 532); caught only by manual sweep, not by the numbered-paragraph grep.
- **UNNAMED_SUBSIDIARIES_IN_LRR** — Section 8, consolidated LRR para 7 references "four subsidiaries" not reviewed directly by BSR & Co. without naming them; cannot be mapped to specific rows in Section 10 from this extract alone (flag for A3/A4 to chase in disclosure or prior correspondence if material).
- **NO_PRIOR_LEDGER** — first-time coverage of VAIBHAVGBL; Section 10 entity list is the new baseline, ENTITY_CHANGE not evaluable this quarter.
- No Balance Sheet / Cash Flow Statement present in this filing (confirmed absent, not a miss).
- No SIGNATURE_BEFORE_MEETING — all 3 digital CS signature timestamps post-date the 20:00 IST board meeting conclusion.
