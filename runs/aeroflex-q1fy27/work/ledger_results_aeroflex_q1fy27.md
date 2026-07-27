# LEDGER — AEROFLEX Q1 FY27 Results Filing (+ Reg 32 Deviation Statement)
Source: `extract_results_aeroflex_q1fy27.txt` (2 source documents: main results filing [page 1]-[page 10]; Reg 32 Statement of Deviation [REG32 page 1]-[REG32 page 3])
Prior-quarter ledger: NOT PROVIDED — no diff possible for `ENTITY_CHANGE` / `DROPPED_SLIDE`-type comparisons this run.

```
=== A2 COUNT TEST ===
category: notes          grep_count: 15   sweep_count: 15   match: yes
category: line_items     grep_count: 81   sweep_count: 81   match: yes
category: zero_standing  grep_count: 20   sweep_count: 20   match: yes
category: agenda_items   grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras  grep_count: 10   sweep_count: 10   match: yes
category: entities       grep_count: 2    sweep_count: 2    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Count-test method notes (for A3/A4 audit trail)
- **notes**: naive `grep -nE "^Note [0-9]+\."` returns only 7 (consolidated notes, page 6, each on its own line). This UNDER-counts. Manual sweep found: 6 more standalone notes inline in one paragraph (line 146, "STANDALONE NOTES (same page): 1. ... 6. ..." — never on their own line, a genuine grep trap) + 2 unnumbered footnotes (line 87 "Note #:" balancing-figure footnote on the consolidated P&L table; line 197 "Deviation or variation could mean: (a)...(c)..." unnumbered definitional footnote below the Reg 32 objects table). Refined multi-pattern grep (7 + 6 + 1 + 1) reconciles to 15, matching the sweep.
- **agenda_items**: naive `grep -n "BOARD OUTCOME ITEM"` returns 3 lines (26, 27, 150) — 150 is a cross-reference back to Item 2 inside the Annexure-B heading, not a third resolution. Anchored grep `^BOARD OUTCOME ITEM [0-9]+\.` returns 2, matching the sweep (2 genuine board resolutions).
- **line_items**: swept across six distinct tabular disclosure sets (A-F below); grep = count of pipe-delimited data rows per line range, summed.
- **zero_standing**: swept via three sub-patterns — dash-only rows across all 4 periods (7), "Nil" cells in the Reg 32 objects table (4), "Not Applicable" / "No Comments" / "No Deviation/Variation" narrative fields in the Reg 32 header (8), plus one "None" (Annexure-B, line 156) — sum 20.

---

## TABLE 1 — NOTES (15 total: 7 consolidated numbered + 6 standalone numbered-inline + 2 unnumbered footnotes)

| # | Line | Statement | Note # | First ~15 words | Flags |
|---|------|-----------|--------|------------------|-------|
| 1 | 91 | Consolidated | Note 1 | "The above results have been reviewed by the audit committee and approved by..." | — |
| 2 | 92 | Consolidated | Note 2 | "Exceptional items:- There is no exceptional items during this quarter." | ZERO_STANDING (ties to line 70) |
| 3 | 93 | Consolidated | Note 3 | "The Company has increased the production capacity of its liquid cooling SFN skid..." | capacity 6,000->9,000 pcs/annum |
| 4 | 94-99 | Consolidated | Note 4 | "The standalone financial results for the quarter ended 30th June, 2026 are summarised..." | embeds a 5-row standalone summary table (Table 2, set B); cross-checked against full standalone statement (Table 2, set C) — all 5 figures match exactly, no discrepancy |
| 5 | 100 | Consolidated | Note 5 | "Company operates in a single segment (manufacturing of product); segment-wise reporting not..." | — |
| 6 | 101 | Consolidated | Note 6 | "Figures for previous periods re-grouped / re-classified to conform to current periods." | — |
| 7 | 102 | Consolidated | Note 7 | "This statement is as per Regulation 33 of SEBI (LODR) Regulations, 2015." | — |
| 8 | 146 | Standalone | Note 1 | "Reviewed by audit committee, approved by board 27 July 2026; limited review;..." | inline, never on own line (grep trap) |
| 9 | 146 | Standalone | Note 2 | "No exceptional items during the quarter." | ZERO_STANDING (ties to line 133); inline |
| 10 | 146 | Standalone | Note 3 | "The Company has increased the production capacity of its liquid cooling SFN skid..." | identical wording to consolidated Note 3; inline |
| 11 | 146 | Standalone | Note 4 | "Single segment; no segment reporting." | inline |
| 12 | 146 | Standalone | Note 5 | "Previous periods re-grouped/re-classified." | inline |
| 13 | 146 | Standalone | Note 6 | "As per Regulation 33." | inline |
| 14 | 87 | Consolidated (P&L table footnote) | unnumbered ("Note #:") | "figures for 3 months ended 31.03.2026 are balancing figures between audited full..." | qualifies the Q4FY26 column on both consolidated (line 58) and standalone (line 121) table headers; not restated after the standalone table |
| 15 | 197 | Reg 32 Annexure A | unnumbered | "Deviation or variation could mean: (a) deviation in objects/purposes; (b) deviation in..." | boilerplate definition below the objects table |

---

## TABLE 2 — LINE ITEMS (81 total across 6 disclosure sets)

### Set A — Consolidated detailed P&L, page 5, INR Lakhs (28 rows), lines 59-86
Columns are Q1FY27 (30.06.2026, unaudited) | Q4FY26 (31.03.2026, balancing #) | Q1FY26 (30.06.2025, unaudited) | FY26 (31.03.2026, audited)

| Line | Item (note #) | Q1FY27 | Q4FY26# | Q1FY26 | FY26 | Flags |
|------|----------------|--------|---------|--------|------|-------|
| 59 | Revenue from operations (1) | 14,537.63 | 12,583.79 | 8,433.34 | 44,193.51 | — |
| 60 | Other income (2) | 59.74 | 61.99 | 33.23 | 135.91 | — |
| 61 | Total Income 1+2 (3) | 14,597.38 | 12,645.77 | 8,466.56 | 44,329.42 | — |
| 62 | Cost of Materials consumed | 8,422.70 | 7,214.85 | 5,337.63 | 25,959.80 | — |
| 63 | Changes in inventories of FG/WIP/stock-in-trade | (353.22) | (25.83) | (393.75) | (867.23) | — |
| 64 | Employee benefits expense | 1,394.23 | 1,011.03 | 906.47 | 4,131.33 | — |
| 65 | Finance costs | 35.26 | 28.23 | 17.77 | 93.65 | — |
| 66 | Depreciation and amortization expense | 784.41 | 778.94 | 592.79 | 2,607.74 | — |
| 67 | Other expenses | 1,724.62 | 1,380.94 | 1,035.08 | 4,995.76 | — |
| 68 | Total expenses (4) | 12,007.99 | 10,388.15 | 7,495.98 | 36,921.04 | — |
| 69 | Profit before exceptional items and tax 3-4 (5) | 2,589.39 | 2,257.62 | 970.58 | 7,408.38 | — |
| 70 | Exceptional items (6) | - | - | - | - | ZERO_STANDING |
| 71 | Profit/(loss) before tax 5+6 (7) | 2,589.39 | 2,257.62 | 970.58 | 7,408.38 | — |
| 72 | Tax expense: Current Tax (8) | 715.68 | 500.00 | 282.00 | 1,897.00 | — |
| 73 | Tax expense: Deferred Tax (8) | (5.59) | (5.88) | (28.11) | (66.70) | — |
| 74 | Taxation of Earlier Year (8) | - | - | - | 25.38 | mixed: dash in all quarterly cols, populated only in FY26 annual col — not all-period-zero, not ZERO_STANDING, but note the pattern |
| 75 | Profit/(loss) for the period, continuing ops, 7-8 (9) | 1,879.31 | 1,763.50 | 716.69 | 5,552.70 | — |
| 76 | Profit/(loss) from discontinued operations (10) | - | - | - | - | ZERO_STANDING |
| 77 | Profit/(loss) for the period, 9+12 (13) | 1,879.31 | 1,763.50 | 716.69 | 5,552.70 | NUMBERING_GAP: note jumps 10->13, skipping 11-12 (standard slots for tax/PAT of discontinued ops, not applicable here since line 76/10 is already nil) |
| 78 | Net profit after tax and share in associates (15) | 1,879.31 | 1,763.50 | 716.69 | 5,552.70 | NUMBERING_GAP: note jumps 13->15, skipping 14 (standard slot for share of profit/loss of associates/JV — company has none) |
| 79 | Attributable to (a) Owners of the company | 1,879.31 | 1,763.50 | 716.69 | 5,552.70 | — |
| 80 | Attributable to (b) Non-controlling interest | - | - | - | - | ZERO_STANDING |
| 81 | Other Comprehensive Income (16) | - | - | - | - | ZERO_STANDING |
| 82 | Total Comprehensive Income for the period, 15+16 (17) | 1,879.31 | 1,763.50 | 716.69 | 5,552.70 | — |
| 83 | Paid up Equity Share Capital (FV Rs 2/-) | 2,646.62 | 2,646.62 | 2,586.41 | 2,646.62 | — |
| 84 | Other Equity | - | - | - | 42,080.73 | mixed: dash in all quarterly cols, populated only in FY26 annual col (standard disclosure convention, not ZERO_STANDING) |
| 85 | EPS continuing (not annualised) — Basic | 1.42 | 1.36 | 0.55 | 4.28 | — |
| 86 | EPS continuing (not annualised) — Diluted | 1.42 | 1.36 | 0.55 | 4.28 | — |

### Set B — Note 4 embedded standalone summary table, page 6 (within consolidated notes), INR Lakhs (5 rows), lines 95-99

| Line | Item | Q1FY27 | Q4FY26# | Q1FY26 | FY26 | Flags |
|------|------|--------|---------|--------|------|-------|
| 95 | Revenue from operations | 13,901.13 | 11,881.72 | 7,918.63 | 41,247.20 | matches Set C line 122 exactly |
| 96 | Profit/(loss) before tax | 2,615.97 | 2,252.21 | 1,020.56 | 7,397.67 | matches Set C line 134 exactly |
| 97 | Profit/(loss) for the period | 1,905.89 | 1,768.66 | 762.28 | 5,528.22 | matches Set C line 139 exactly |
| 98 | Other comprehensive income | - | - | - | - | ZERO_STANDING; matches Set C line 140 exactly |
| 99 | Total comprehensive income for the period | 1,905.89 | 1,768.66 | 762.28 | 5,528.22 | matches Set C line 141 exactly |

### Set C — Standalone detailed P&L, page 9, INR Lakhs (24 rows), lines 122-145

| Line | Item (note #) | Q1FY27 | Q4FY26# | Q1FY26 | FY26 | Flags |
|------|----------------|--------|---------|--------|------|-------|
| 122 | Revenue from operations (1) | 13,901.13 | 11,881.72 | 7,918.63 | 41,247.20 | — |
| 123 | Other income (2) | 76.45 | 72.07 | 33.23 | 155.14 | — |
| 124 | Total Income 1+2 (3) | 13,977.58 | 11,953.79 | 7,951.86 | 41,402.34 | — |
| 125 | Cost of materials consumed | 8,015.44 | 7,068.39 | 5,095.22 | 24,254.82 | — |
| 126 | Changes in inventories of FG/WIP/stock-in-trade | (323.52) | (421.23) | (521.29) | (1,241.78) | — |
| 127 | Employee benefits expense | 1,330.42 | 963.76 | 831.72 | 3,802.27 | — |
| 128 | Finance costs | 35.15 | 28.23 | 17.77 | 93.60 | — |
| 129 | Depreciation and amortization expense | 727.93 | 721.50 | 548.35 | 2,412.67 | — |
| 130 | Other expenses | 1,576.20 | 1,340.93 | 959.54 | 4,683.08 | — |
| 131 | Total expenses (4) | 11,361.61 | 9,701.58 | 6,931.31 | 34,004.67 | — |
| 132 | Profit before exceptional items and tax 3-4 (5) | 2,615.97 | 2,252.21 | 1,020.56 | 7,397.67 | — |
| 133 | Exceptional items / Diminution in value of Investment (6) | - | - | - | - | ZERO_STANDING |
| 134 | Profit/(loss) before tax 5+6 (7) | 2,615.97 | 2,252.21 | 1,020.56 | 7,397.67 | — |
| 135 | Tax expense: Current Tax (8) | 715.68 | 500.00 | 282.00 | 1,897.00 | — |
| 136 | Tax expense: Deferred Tax (8) | (5.59) | (16.45) | (23.73) | (63.93) | — |
| 137 | Taxation of Earlier year (8) | - | - | - | 36.38 | mixed, same pattern as line 74; not ZERO_STANDING |
| 138 | Profit/(loss) for the period, continuing ops, 7-8 (9) | 1,905.89 | 1,768.66 | 762.28 | 5,528.22 | — |
| 139 | Profit/(loss) for the period, 9+12 (13) | 1,905.89 | 1,768.66 | 762.28 | 5,528.22 | NUMBERING_GAP: jumps 9->13, skipping 10-12; standalone has no discontinued-ops line at all (unlike consolidated line 76 which shows it explicitly as nil) — a real structural difference between the two statements, not just a numbering artifact |
| 140 | Other Comprehensive Income (14) | - | - | - | - | ZERO_STANDING |
| 141 | Total Comprehensive Income for the period, 13+14 (15) | 1,905.89 | 1,768.66 | 762.28 | 5,528.22 | — |
| 142 | Paid up Equity Share Capital (FV Rs 2/-) | 2,646.62 | 2,646.62 | 2,586.41 | 2,646.62 | — |
| 143 | Other Equity | - | - | - | 42,006.99 | mixed, same pattern as line 84 (Other Equity differs standalone 42,006.99 vs consolidated 42,080.73 — expected, consolidation adjustment) |
| 144 | EPS continuing (not annualised) — Basic | 1.44 | 1.36 | 0.59 | 4.26 | — |
| 145 | EPS continuing (not annualised) — Diluted | 1.44 | 1.36 | 0.59 | 4.26 | — |

### Set D — Annexure-B Reg 30 disclosure fields (Tax Auditor appointment, Board Outcome Item 2 detail), page 10 (6 rows), lines 151-156

| Line | Field | Value | Flags |
|------|-------|-------|-------|
| 151 | Name of the Tax Auditor | M/s. Kailash Chand Jain & Co., Chartered Accountants | — |
| 152 | FRN | 112318W | — |
| 153 | Reason of Change | Appointment of Tax Auditor | — |
| 154 | Date of appointment / Term | July 27, 2026; FY 2026-27 | — |
| 155 | Brief Profile | est. 14 Aug 1990, ICAI-registered, empaneled RBI/C&AG/IBA/IRDAI/IT Dept/GST Dept/CBI/SFIO/NIA | — |
| 156 | Relationships between Directors inter-se | None | ZERO_STANDING |

### Set E — Reg 32 statement header fields, [REG32 page 2] (13 rows), lines 173-185

| Line | Field | Value | Flags |
|------|-------|-------|-------|
| 173 | Name of listed entity | Aeroflex Industries Limited | — |
| 174 | Mode of Fund Raising | Issue And Allotment of Equity shares on Preferential Basis | — |
| 175 | Date of Raising Funds | 03rd February, 2026 (date of allotment) | — |
| 176 | Amount Raised | Rs. 54,99,99,714.60 (~Rs 55.00 Cr) | — |
| 177 | Report filed for Quarter ended | June 30, 2026 | — |
| 178 | Monitoring Agency | Not Applicable | ZERO_STANDING |
| 179 | Monitoring Agency Name, if applicable | Not Applicable | ZERO_STANDING |
| 180 | Is there a Deviation/Variation in use of funds raised | No Deviation/Variation | ZERO_STANDING |
| 181 | Whether pursuant to change in terms of contract/objects approved by shareholders | Not Applicable | ZERO_STANDING |
| 182 | Date of shareholder Approval | Not Applicable | ZERO_STANDING |
| 183 | Explanation for the Deviation/Variation | Not Applicable | ZERO_STANDING |
| 184 | Comments of the Audit Committee after review | No Comments | ZERO_STANDING |
| 185 | Comments of the auditors, if any | No Comments | ZERO_STANDING |

### Set F — Reg 32 objects/utilisation table, [REG32 page 2]-[REG32 page 3], absolute Rupees (5 rows), lines 187-188, 193-195

| Line | Item | Original Allocation | Modified Allocation | Funds Utilised (qtr) | Deviation/Variation | Flags |
|------|------|---------------------|----------------------|------------------------|------------------------|-------|
| 187 | Long-term working capital | 41,52,49,783.60 | Nil | 40,76,86,751.00 | Nil | ZERO_STANDING (Modified Alloc + Deviation cols) |
| 188 | General Corporate Purpose | 12,02,49,931.00 | Nil | 1,64,00,806.00 | Nil | ZERO_STANDING (Modified Alloc + Deviation cols); only 13.6% of allocated GCP utilised this quarter — arithmetic observation only, not interpreted here |
| 193 | a. Advisory Fees | 1,41,60,000.00 | Nil | 1,41,60,000.00 | Nil | ZERO_STANDING (Modified Alloc + Deviation cols); fully utilised |
| 194 | b. Board Meetings, EGMs and Miscellaneous expenses | 3,40,000.00 | Nil | 3,40,000.00 | Nil | ZERO_STANDING (Modified Alloc + Deviation cols); fully utilised |
| 195 | TOTAL | 54,99,99,714.60 | (blank) | 43,85,87,557.00 | (blank) | subtotal row; derived unutilised = 11,14,12,157.60 (~Rs 11.14 Cr, ~20.3% of total raised) per line 196 annotation — arithmetic only, not interpreted here |

---

## TABLE 3 — BOARD OUTCOME AGENDA ITEMS (2 total)

| # | Line | Item | Description | Flags |
|---|------|------|-------------|-------|
| 1 | 26 | Item 1 | Un-audited Standalone and Consolidated Financial Results for Q1 FY27 + Limited Review Reports from Statutory Auditors | — |
| 2 | 27 | Item 2 | Appointment of M/s. Kailash Chand Jain & Co. as Tax Auditor for FY 2026-27 (detail in Annexure-B, Set D above) | — |

Board meeting timing (line 32): commenced 03:30 p.m., concluded 04:16 p.m. — **46 minutes** for a meeting covering quarterly results (both standalone + consolidated), 2 Limited Review Reports, and a tax-auditor appointment.

No other agenda items present in this filing (no AR approval, no AGM notice, no dividend, no director appointment/resignation, no scrutinizer, no ESOP grant, no capital-raising enabling resolution) — confirmed absent by full-text sweep of pages 1-10, not merely unlisted.

---

## TABLE 4 — AUDITOR REPORT PARAGRAPHS (10 total: 6 consolidated + 4 standalone)

### 4a. Consolidated LRR (pages 3-4), Shweta Jain & Co LLP, UDIN 26125740CDLRZN4282

| Line | Para | Content | Flags |
|------|------|---------|-------|
| 40 | Para 1 | Scope: reviewed Statement of Consolidated Unaudited Financial Results, Parent + subsidiaries ("Group"), Q1 FY27 + YTD, per Reg 33 | — |
| 41 | Para 2 | Basis of preparation: Ind AS 34, s.133 Companies Act 2013 | — |
| 42 | Para 3 | Review standard: SRE 2410; explicitly states review provides less assurance than audit, no audit opinion expressed | — |
| 43 | Para 4 | Additional procedures per SEBI circular under Reg 33(8) | — |
| 48 | Para 5 | Conclusion premised on own review + reliance on other auditors' reports referenced in Para 6; no material misstatement noted | — |
| 49 | Para 6 | Reliance/Other Matters para: subsidiary Hyd-Air Engineering Pvt Ltd NOT reviewed by this firm; its interim financials (total assets Rs 3,825.35 lakhs; total revenue Rs 765.66 lakhs; PAT Rs (26.58) lakhs; TCI Rs (26.58) lakhs for the quarter) were reviewed by other auditors whose reports were furnished by Management; conclusion relies solely on those reports | subsidiary loss-making this quarter (PAT -26.58 lakhs) |

Opinion type: UNMODIFIED / CLEAN (line 52). No Emphasis of Matter paragraph present. Other Matters = Para 6 (subsidiary reliance). No Going Concern language. Entity list reviewed directly: Parent only. Entity reviewed by other auditors (unaudited by this firm, management-furnished report): Hyd-Air Engineering Pvt Ltd. UDIN: 26125740CDLRZN4282. Signatory: CA Ravi Jain, Partner, Membership No. 125740, FRN 127673W/W101149, dated 27 July 2026, Mumbai (line 53).

### 4b. Standalone LRR (pages 7-8), Shweta Jain & Co LLP, UDIN 26125740ZGJEJV5319

| Line | Para | Content | Flags |
|------|------|---------|-------|
| 109 | Para 1 | Scope: reviewed Standalone unaudited financial results, Q1 FY27 + YTD, per Reg 33 | — |
| 110 | Para 2 | Responsibility statement (Management) + basis Ind AS 34, s.133 Companies Act 2013 | — |
| 111 | Para 3 | Review standard SRE 2410; moderate assurance; less than audit scope; no audit opinion | — |
| 115 | Para 4 | Conclusion: nothing came to attention indicating non-disclosure or material misstatement | — |

Opinion type: UNMODIFIED / CLEAN, explicitly annotated "no emphasis of matter, no qualification" (line 116). No Other Matters paragraph (standalone has no subsidiaries to reference). No Going Concern language. Entity reviewed: Parent (standalone) only. UDIN: 26125740ZGJEJV5319. Signatory: CA Ravi Jain, Partner, Membership No. 125740, FRN 127673W/W101149, dated 27 July 2026, Mumbai (line 117). Same partner signs both reports, same date, two different UDINs (correct practice, one UDIN per report).

---

## TABLE 5 — CONSOLIDATION ENTITIES (2 total)

| # | Line(s) | Entity | Relationship | Flags |
|---|---------|--------|--------------|-------|
| 1 | 39, 57 | Aeroflex Industries Limited (CIN L27509MH1993PLC074576) | Parent / listed entity | — |
| 2 | 44, 50 | Hyd-Air Engineering Pvt Ltd | Subsidiary (only one consolidated) | reviewed by OTHER auditors, report furnished by Management, not reviewed by Shweta Jain & Co LLP directly; loss-making this quarter (PAT -26.58 lakhs, line 50); PRIOR_LEDGER_UNAVAILABLE — no prior-quarter entity list supplied to this run, so ENTITY_CHANGE cannot be determined either way; A3/A4 should check company memory / prior filings independently |

---

## TABLE 6 — DIGITAL SIGNATURE BLOCKS (9 total; supplementary, not a fixed YAML count category for this doctype)

| # | Line | Document | Signatory | Designation | Timestamp | Flags |
|---|------|----------|-----------|-------------|-----------|-------|
| 1 | 33 | Main filing, Board Outcome letter | Ruthu Parampogi | Company Secretary & Compliance Officer, Mem No. A60982 | 2026.07.27 18:30:43 +05'30' | signed ~4h14m after board meeting concluded (04:16 p.m.) — normal lag, no flag |
| 2 | 53 | Main filing, Consolidated LRR | CA Ravi Jain | Partner, Shweta Jain & Co LLP, Mem 125740 | dated 27 July 2026 (no time given) | — |
| 3 | 103 | Main filing, Consolidated notes sign-off | Asad Daud | Chairman & Managing Director, DIN 02491539 | dated 27 July 2026 (no time given) | — |
| 4 | 117 | Main filing, Standalone LRR | CA Ravi Jain | Partner, Shweta Jain & Co LLP, Mem 125740 | dated 27 July 2026 (no time given) | — |
| 5 | 147 | Main filing, Standalone notes sign-off | Asad Daud | Chairman & Managing Director, DIN 02491539 | dated 27 July 2026 (no time given) | — |
| 6 | 158 | Main filing, Annexure-B | Ruthu John Parampogi | Company Secretary | 2026.07.27 18:31:10 +05'30' | NAME_VARIANT: "Ruthu John Parampogi" here vs "Ruthu Parampogi" at lines 33, 169, 189, 198 — same Mem No. context (A60982 given at line 33 only), likely same person, worth a one-line confirmation |
| 7 | 169 | Reg32 page 1 | Ruthu Parampogi | Company Secretary & Compliance Officer, M. No. A60982 | 2026.07.27 19:11:19 | — |
| 8 | 189 | Reg32 page 2 | Ruthu Parampogi | Company Secretary | 2026.07.27 19:11:35 | — |
| 9 | 198 | Reg32 page 3 | Ruthu Parampogi | Company Secretary | 2026.07.27 19:11:51 | — |

No signature timestamp precedes the board meeting conclusion (04:16 p.m.) — earliest is 18:30:43 the same day. No SIGNATURE_BEFORE_MEETING flag.

---

## OBSERVATIONS LOG (non-counted, carried forward for A3/A4; enumeration only, no interpretation)
- NUMBERING_GAP x3: consolidated P&L note numbering skips 11-12 (line 77) and 14 (line 78); standalone P&L note numbering skips 10-12 (line 139). Consistent with "no discontinued operations, no associates/JV" — structural, not an error, but A3 should confirm against the full Ind AS 34 format the company is entitled to abbreviate.
- Consolidated vs standalone structural difference: consolidated statement explicitly shows a nil "Profit/(loss) from discontinued operations" row (line 76) and an "Attributable to owners / NCI" split (lines 79-80); standalone shows neither (no such rows exist to enumerate, they are structurally absent, not zero-valued).
- Note 4 embedded standalone summary (Set B, page 6) cross-checked line-for-line against full standalone statement (Set C, page 9): all 5 values match exactly. No discrepancy.
- Reg 32 fund utilisation: General Corporate Purpose object shows only Rs 1,64,00,806 utilised of Rs 12,02,49,931 allocated (13.6%) despite the form's own declaration of "No Deviation/Variation" (line 180) and "No Comments" from Audit Committee/auditors (lines 184-185); Long-term working capital object nearly fully utilised (98.2%). Total unutilised ~Rs 11.14 Cr (~20.3% of the Rs 55 Cr raised, allotted 3 Feb 2026). Arithmetic only; A4 should assess whether "No Deviation/Variation" is the correct characterization given the GCP underspend.
- NAME_VARIANT: signatory named "Ruthu John Parampogi" at line 158 vs "Ruthu Parampogi" elsewhere (lines 33, 169, 189, 198). Likely the same Company Secretary; flagged for confirmation, not treated as a discrepancy.
- Two auditor reports, same partner (CA Ravi Jain), same firm, same date, different UDINs for consolidated vs standalone — correct practice.
- entities/ENTITY_CHANGE: cannot be assessed this run; no prior-quarter ledger was supplied as input.

---
```yaml
stage: A2-enumerator
company: "AEROFLEX"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "runs/aeroflex-q1fy27/work/ledger_results_aeroflex_q1fy27.md"
counts:
  notes: 15
  line_items: 81
  zero_standing: 20
  agenda_items: 2
  auditor_paras: 10
  entities: 2
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, NUMBERING_GAP, NAME_VARIANT]
gate_a2: pass
mismatch_note: ""
```
