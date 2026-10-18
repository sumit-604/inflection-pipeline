# A4 MERGED REVIEW: Cyient DLM Ltd (CYIENTDLM) | Q2 FY27 (quarter and half year ended 30-Sep-2026)

Agent: A4 analyst | Model: claude-opus-5-5 | Run date: 2026-10-17
Protocol loaded: Quarterly Results Review Protocol v1.4 (Role 4) only. Role 5 not run: the 15-Oct-2026 call transcript is not in this run. (Role 5 addendum, 2026-10-18: Quarterly Concall Analysis Protocol v1.1 (Role 5) now run on the 15-Oct-2026 machine transcript; see the ROLE 5 section. Role 4 tables and numbers are unchanged.)
Inputs: A1 structured and fulltext (results, presentation, press release), A2 ledgers (3), A3 forensics (3), Notion context (orchestrator copy, live fetch 2026-10-17). No source PDF and nothing under inputs/ was opened.
Anchor convention: "res L###" = results fulltext line; "pres L###" = presentation fulltext line; "pr L###" = press release fulltext line; R### = A1 structured row of that document. Page 2 P&L values come only from the image-verified transcription (res L533-L565, rows R678-R993). The corrupted text layer at res L74-L118 is superseded and not used.
Units: filing in Rs Millions (res L79, R636). Conversion: Rs Cr = Rs Mn x 0.1. Tables show Rs Cr to 2 dp. All arithmetic runs on the Rs Mn source values, so a Rs Cr total can differ from the sum of its rounded parts by 0.01.
Correction loop 1 (A5 verdict INCOMPLETE, 2026-10-17): C1, C2, M1-M4 and S1-S5 applied in place. Every grafted figure was re-verified against the A1 fulltexts at the cited lines. The protocol was not re-run.
Correction loop 2 (A5 loop-1 re-audit INCOMPLETE, 2026-10-17): LC1, LF1, N1, N2, N3 and style notes LS1, LS2 applied in place (Step 2A, 2C, 4, 5B, 5C, 6B, 6.5, 8C, 8.5, monitorables, brief, flags). Every grafted figure was re-verified against res L170-L177, L212, L243-L248, L286, L538-L552 and pres L255-L257, L334-L362, L381-L382. No table number changed. The protocol was not re-run.

---

## LEDGER RECONCILIATION PREAMBLE (contractual)

Ledger contains 8 notes / 0 turns / 21 slides. All 8 notes, all 21 slides and every ledger row reviewed. Findings incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18, A3-19, A3-20, A3-21, FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN-01, FN-02, FN-03, FN-04, FN-05, FN-06, FN-07, FN-08].

| Ledger | Rows in structured | Rows referenced by A2 | Orphans | A2 gate | A3 reconciled | Reviewed by A4 |
|---|---|---|---|---|---|---|
| Results (ledger_results) | 993 (R001-R993) | 993 | 0 | pass | 100% | all; 8 numbered notes (Notes 1, 1 cont, 2, 3, 3(ii), 4, 5, cash-flow note (i)) |
| Presentation (ledger_presentation) | 372 (R001-R372) | 372 | 0 | pass | 100% | all; 18 slides; 30 qualifier/footnote rows |
| Press release (ledger_pressrelease) | 60 (R001-R060) | 60 | 0 | pass | 100% | all; 3 pages; 0 notes; 5 qualifiers |

Slides count = 18 deck pages + 3 press release pages = 21. Turns = 0 (no concall document in the run). No unreviewed row exists, so the review proceeds.

Pipeline notes carried into this review (none blocks the run):
1. A2 press release ledger R036 has the rename direction reversed. The fulltext governs (pr L103-104): Altek Electronics was renamed Cyient DLM Electronics Inc.
2. Results R451 (Loan repaid by subsidiary 19.33) belongs to standalone HY Sep-25, not HY Sep-26. Footing proves it (A3 errata; res L232-L239).
3. Consolidated Q2 FY26 employee cost prints 329.42 (res L543, R740) and fails footing by exactly 200.00 (res L547). The deck prints Q2 FY26 employee cost 529 (pres L377, R156). This review uses 529.42 for cost ratios only, labelled each time. No growth rate is computed from 329.42 (A3-14).
4. Standalone HY Sep-26 basic EPS reads 4.35{F} (res L562, R975), below diluted 4.54 (res L563). Ind AS 33 does not allow that. Computed: 360.78 / about 79.37 Mn shares = 4.55. This review uses 4.55 (A3-15).
5. Standalone HY Sep-25 clipped cells: other expenses read "?18.47{P}" (res L546); footing to the printed total 4,157.85 requires 718.47. PBT reads "?35.10{P}" (res L548); the cash flow prints 335.10 (res L206). Both repaired values are used.
6. A3 presentation FN04 states FY26 deck EBITDA margin as 1,303 / 14,614 = 8.9%. The four tied quarters of revenue sum to 2,784 + 3,106 + 3,033 + 3,691 = 12,614 (pres L247-L250), not 14,614. Correct value: 1,303 / 12,614 = 10.3%, inside the deck's own 9-11% "today" band. This is the deck-normalized basis: the 1,303 includes the 34 Mn Q3 FY26 one-off bar (pres L253), which the filing excludes (see Step 3 cross-check). The filed FY26 operating EBITDA margin is 10.05% (Step 1A). The trailing-four-quarter figure in FN04 (10.2%) is correct. The FN04 conclusion for Q2 (8.7%, below band) stands.
7. A3 presentation "positive data points" says implied book-to-bill 1.55x "ties to the stated 1.6x". It does not: 6,078.90 / 3,930.90 = 1.546, which rounds to 1.5. A3 press release FN-05 is correct and governs.

---

## STEP 0: PRE-FLIGHT

### 0A. Notion page (orchestrator copy, work/notion-thesis.md)

| Item | Reading |
|---|---|
| Decision Status | NOT SET (operator-only). Verified before any framing. |
| Framing | PRE-THESIS READ. Halt 1 pending. Mental model UNSIGNED. No spear on record. Prior run runs/cyientdlm-2026-09-06 (Phase 1, gate REWORK, confidence 54). |
| One-line thesis | ND (none signed) |
| Four-pillar destination PE | ND (no valuation run) |
| Bear/Base/Bull projections | ND |
| Thesis-broken conditions | ND (none signed) |
| Monitoring checklist | No formal checklist. The six named Q2 tests serve as the reading list. |
| Position size, cost basis | None (no position) |
| Devil's Advocate split | ND |
| Prior-quarter Questions for Management | ND (not on page). The answer-status tracking rule cannot run this quarter. |
| Properties (memory, not filed) | CMP 979 (13-Oct-2026), mkt cap about Rs 7,772 Cr; Gate 0 47/160 AVOID as scored (F-G01 open); EM 21; Promoter Verdict TRUSTWORTHY-with-flags; parent Cyient Ltd 52.11%, zero pledge |

### 0B. Units
All figures in the results filing are in Rs Millions (res L79, L127, L199, L281). The deck is in INR Mn (pres L371, L427). The press release is in Rs crore (pr L69). Conversion used: Rs Cr = Rs Mn x 0.1.

### 0C. Share count changes
| Item | Reading | Anchor |
|---|---|---|
| Paid-up capital | 793.64 Mn (31-Mar-26) to 793.83 Mn (30-Sep-26): +0.19 Mn = +19,000 shares at Rs 10 face value | res L163, R309-R310 |
| Source | ESOP exercise proceeds 0.19 Mn in H1 FY27 | res L242, R475 |
| New grants (15-Oct-26, after period end) | 10,000 RSUs + 2,63,400 options = 273,400 units = 0.34% of about 79.38 Mn shares; exercise price, vesting, recipients NOT FOUND | res L42-43, R551-R552, R615 |
| Split, bonus, rights, QIP, buyback | None disclosed | res L36-43 |
| EPS adjustment | Not needed. Basic vs diluted spread is at most 0.01 on every consolidated period. Share-adjusted EPS = reported EPS. | res L562-563 |

### 0D. Notes extraction (mandatory, before any growth figure)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 | Basis, approval, review | Ind AS results, reviewed by the Audit Committee and approved by the Board on 15-Oct-2026; auditors issued unmodified limited-review reports (res L268-273, R655-R656). | nil | all | none |
| 2 | Segment | Single reportable segment, EMS, under Ind AS 108 (res L277-278, R657). | nil | all | No segment walk. The standalone vs consolidated split is the only geographic proxy. |
| 3(i) | Net FX in other income | Consolidated FX: Q2 FY27 +1.90; Q1 FY27 (2.06); Q2 FY26 (1.95); H1 FY27 (0.15); H1 FY26 (4.10); FY26 (3.22). Standalone: +1.89; (2.06); (1.95); (0.17); (4.10); (3.26) (res L285-286, R534-R545). | Q2 FY27 +1.90; YoY swing +3.86; QoQ swing +3.96 | Q2 FY27 vs Q2 FY26 and Q1 FY27 | Strip from core. Standalone PBT ex-FX is flat QoQ: 24.27 vs 24.35 (A3-01). |
| 3(ii) | Earnout fair-value gain | Gain on fair valuation of earnout liability 18.20 (181.95 Mn) in consolidated Q2 and H1 FY27; sentence has a text gap and names no entity or cause (res L288, R546, R659). | +18.20 to PBT and PAT (untaxed, A3-11/FN06) | Q2 FY27. Same line was 19.58 (195.75 Mn) in H1 FY26 (res L213, R400), placed in Q2 FY26 by the deck (pres L385). | Normalise both Q2s. 53.5% of Q2 FY27 consolidated PAT. |
| 4 | FVOCI investee | OCI fair-value decline on an IP communications investee, blamed on long order lead time; management expects recovery as products launch "over the next few years" (res L290-291, R660, R612). | P&L nil. OCI nil in Q1 and Q2 FY27; (3.84) in Q2 FY26; (20.72) in FY26 (res L555). | OCI only | No P&L effect. Carrying value 10.23 cons is unchanged (res L141) [INFERENCE: this is the investee]. |
| 5 | Annexures | Balance sheet (Annexure 1) and cash flow (Annexure 2) attached (res L294, R661). | nil | H1 | Enables Step 5. |
| CF note (i) | Cash components | Cash 82.71 cons = bank current accounts 82.68 + cash on hand 0.03; no sub-3-month deposits at 30-Sep-26 (38.12 at 30-Sep-25) (res L257-262). | nil | H1 | Deposits moved to other bank balances 71.89 (res L154). |
| EPS footnote | EPS not annualised | Quarterly and half-year EPS are not annualised (res L564, R644). | nil | Q, HY | none |
| Board item 2 | CHRO appointment | Sandip Mishra appointed Senior VP and CHRO (senior management, not a director), effective 15-Oct-2026, term "as per the employment contract" (res L39-40, L486-487). | nil | post period | Governance data point (A3-13). |
| Board item 3 | Equity grants | 10,000 RSUs and 2,63,400 options granted to "associates" (res L42-43). | future SBP expense ND | post period | SBP was 2.20 this H1 vs a (3.96) credit last H1 (res L214): a 6.16 YoY headwind inside employee cost (A3-12). |
| Data defect | Cons Q2 FY26 employee | Prints 32.94 (329.42 Mn); footing and deck both require 52.94 (A3-14; pres L377). | 20.00 misprint | Q2 FY26 | Ratios use 52.94; no growth from 32.94. |
| Data defect | Standalone HY basic EPS | 4.35 read is a defect; 4.55 computed (A3-15). | nil | H1 FY27 | Use 4.55. |

Per-note questions answered:
- Note 3(ii) changes every YoY and QoQ read. Both Q2 FY26 and Q2 FY27 carry an earnout write-back, so YoY reported PAT (+5.81%) compares two inflated quarters. QoQ reported PAT (+108.87%) is meaningless without stripping it.
- Note 3(i) moves Q2 PBT by +3.86 YoY. FX is non-recurring by nature and is stripped from core.
- Note 4 does not touch the P&L. It flags a forward OCI risk on 10.23 of carrying value [INFERENCE].
- The template has no exceptional-items line. A gain worth 46.3% of consolidated Q2 PBT therefore sits inside "Other income" (A3-06).

Auditor opinion check: Standalone and consolidated reports are both unmodified limited-review conclusions (res L346-352, L450-456). No Emphasis of Matter, Other Matter, Going Concern or component-auditor paragraph in either report (A2 L5; A3 F4/F5 PASS). Auditor: S.R. Batliboi & Associates LLP, partner Harish Khemnani (res L355-363, L460-467). Status: CLEAN. Wording note: the reports call the period "six month period"; the statement header says "Half Year" (A3-17, wording only).

### 0E. Business type
Standard operating business (EMS manufacturer). Steps 1 and 5 apply. Lender variant not used.

Checkpoint: Notion fetched with Decision Status NOT SET, units Rs Mn, share change +19,000, notes tabled, auditor clean, business type standard.

---

## STEP 1: DATA EXTRACTION TABLES (Rs Cr)

Column note: the protocol's "FY[YY]" column cannot exist at Q2. The table carries H1 FY26, H1 FY27 and FY26 instead. FY27 = ND.

### 1A. CONSOLIDATED (res L538-L563, rows R678-R683, R690-R695 ... R978-R983)

| Line Item (anchor) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from Operations (res L538) | 310.63 | 373.80 | 393.09 | 589.06 | 766.89 | 1,261.49 | ND |
| Other Income (res L539) | 22.66 | 0.27 | 22.62 | 26.84 | 22.88 | 36.26 | ND |
| Total Income (res L540) | 333.30 | 374.07 | 415.71 | 615.90 | 789.77 | 1,297.75 | ND |
| Cost of Materials Consumed (res L541) | 196.12 | 216.87 | 255.87 | 357.81 | 472.74 | 784.79 | ND |
| Change in Inventories (res L542) | (13.52) | 15.09 | (9.84) | (8.73) | 5.26 | (32.58) | ND |
| Employee Benefits Expense (res L543) | 32.94 [printed; misprint, 52.94 by footing and pres L377] | 64.43 | 67.89 | 110.72 | 132.32 | 226.78 | ND |
| Finance Costs (res L544) | 6.81 | 6.12 | 6.10 | 15.43 | 12.22 | 27.17 | ND |
| Depreciation (res L545) | 10.57 | 11.10 | 11.37 | 21.08 | 22.47 | 42.75 | ND |
| Other Expenses (res L546) | 43.90 | 38.24 | 45.00 | 73.01 | 83.24 | 155.68 | ND |
| Total Expenses (res L547) | 296.82 | 351.86 | 376.39 | 569.32 | 728.25 | 1,204.59 | ND |
| Profit Before Tax (res L548) | 36.48 | 22.21 | 39.31 | 46.58 | 61.52 | 93.16 | ND |
| Tax Expense (res L551) | 4.33 | 5.93 | 5.30 | 6.97 | 11.22 | 19.88 | ND |
| of which current tax (res L549) | 4.59 | 4.90 | 6.91 | 8.05 | 11.81 | 19.29 | ND |
| of which deferred tax (res L550) | (0.26) | 1.02 | (1.61) | (1.08) | (0.59) | 0.59 | ND |
| PAT (res L552) | 32.15 | 16.29 | 34.01 | 39.61 | 50.30 | 73.28 | ND |
| EPS reported, basic Rs (res L562) | 4.05 | 2.05 | 4.28 | 4.99 | 6.34 | 9.23 | ND |
| EPS reported, diluted Rs (res L563) | 4.05 | 2.05 | 4.28 | 4.99 | 6.33 | 9.23 | ND |
| EPS share-adjusted Rs | 4.05 | 2.05 | 4.28 | 4.99 | 6.34 | 9.23 | ND |
| Memo: earnout gain inside Other Income (res L288, L213; pres L385) | 19.58 | 0.00 | 18.20 | 19.58 | 18.20 | 19.6 (pres L448 "INR 196M ... FY26") | ND |
| Memo: net FX inside Other Income (res L286) | (1.95) | (2.06) | 1.90 | (4.10) | (0.15) | (3.22) | ND |

Footing check: all six total-expense columns foot except Q2 FY26 (gap 20.00, the employee misprint). PBT = Total income minus Total expenses in all six columns.

Derived metrics, consolidated (Rs Cr; computed from the rows above):

| Derived Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 31.19 | 39.16 | 34.17 | 56.25 | 73.33 | 126.82 | ND |
| Operating EBITDA Margin | Op EBITDA / Rev | 10.04% | 10.48% | 8.69% | 9.55% | 9.56% | 10.05% | ND |
| Reported EBITDA | PBT + D + FC | 53.85 | 39.43 | 56.79 | 83.09 | 96.21 | 163.08 | ND |
| Core PBT (ex-OI) | PBT - OI | 13.82 | 21.95 | 16.70 | 19.74 | 38.64 | 56.90 | ND |
| Other Income / PBT | OI / PBT | 62.12% | 1.19% | 57.53% | 57.62% | 37.19% | 38.93% | ND |
| Effective Tax Rate | Tax / PBT | 11.88% | 26.68% | 13.48% | 14.96% | 18.24% | 21.34% | ND |
| PAT Margin | PAT / Rev | 10.35% | 4.36% | 8.65% | 6.72% | 6.56% | 5.81% | ND |
| Gross margin | (Rev - materials - inv change) / Rev | 41.22% | 37.94% | 37.41% | 40.74% | 37.67% | 40.37% | ND |
| PAT ex-earnout | PAT - earnout gain (untaxed) | 12.57 | 16.29 | 15.82 | 20.03 | 32.10 | ND (FY26 total earnout per deck 19.6; filing FY26 figure NOT FOUND) | ND |
| ETR ex-earnout | Tax / (PBT - earnout) | 25.63% | 26.68% | 25.09% | 25.81% | 25.90% | ND | ND |

Derived earlier quarters from the filing: Q1 FY26 = H1 FY26 minus Q2 FY26: revenue 278.43, op EBITDA 25.06 (9.00%), core PBT 5.93, gross margin 40.21%. H2 FY26 = FY26 minus H1 FY26: revenue 672.42, op EBITDA 70.57 (10.49%), core PBT 37.16, gross margin 40.05%.

### 1B. STANDALONE (res L538-L563, rows R684-R689 ... R984-R989)

| Line Item (anchor) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Revenue from Operations (res L538) | 235.64 | 282.89 | 294.79 | 441.97 {P} | 577.68 {F} | 942.65 | ND |
| Other Income (res L539) | 3.06 | 0.32 | 4.66 | 7.32 | 4.98 {F} | 16.80 | ND |
| Total Income (res L540) | 238.71 | 283.21 | 299.45 | 449.30 | 582.65 | 959.46 | ND |
| Cost of Materials Consumed (res L541) | 146.03 | 167.69 | 188.04 | 269.40 {P} | 355.73 | 604.50 | ND |
| Change in Inventories (res L542) | (7.66) | 16.45 | (2.12) | (4.10) | 14.33 | (29.99) | ND |
| Employee Benefits Expense (res L543) | 25.61 | 27.59 | 30.25 | 52.38 {P} | 57.84 | 105.16 | ND |
| Finance Costs (res L544) | 4.93 | 4.14 | 3.99 | 11.91 | 8.12 | 20.02 | ND |
| Depreciation (res L545) | 7.22 | 7.31 | 7.53 | 14.35 | 14.84 | 29.12 | ND |
| Other Expenses (res L546) | 44.31 | 37.74 | 45.60 | 71.85 [clipped; 718.47 Mn by footing] | 83.34 | 154.82 | ND |
| Total Expenses (res L547) | 220.45 | 260.91 | 273.29 | 415.79 | 534.20 | 883.63 | ND |
| Profit Before Tax (res L548; HY Sep-25 from res L206) | 18.26 | 22.29 | 26.16 | 33.51 | 48.45 | 75.83 | ND |
| Tax Expense (res L551) | 4.73 | 5.59 | 6.78 | 8.70 | 12.37 | 19.51 | ND |
| PAT (res L552) | 13.54 | 16.70 | 19.38 | 24.81 {P} | 36.08 | 56.32 | ND |
| EPS reported, basic Rs (res L562) | 1.71 | 2.10 | 2.44 | 3.13 | 4.35 [read defect; 4.55 computed] | 7.10 | ND |
| EPS reported, diluted Rs (res L563) | 1.70 | 2.10 | 2.44 | 3.12 | 4.54 | 7.09 | ND |
| EPS share-adjusted Rs (basic) | 1.71 | 2.10 | 2.44 | 3.13 | 4.55 | 7.10 | ND |
| Memo: net FX inside Other Income (res L285) | (1.95) | (2.06) | 1.89 | (4.10) | (0.17) | (3.26) | ND |

Derived metrics, standalone (Rs Cr):

| Derived Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 27.35 | 33.42 | 33.02 | 52.45 | 66.44 | 108.17 | ND |
| Operating EBITDA Margin | Op EBITDA / Rev | 11.61% | 11.81% | 11.20% | 11.87% | 11.50% | 11.48% | ND |
| Reported EBITDA | PBT + D + FC | 30.41 | 33.74 | 37.68 | 59.77 | 71.41 | 124.97 | ND |
| Core PBT (ex-OI) | PBT - OI | 15.20 | 21.98 | 21.50 | 26.19 | 43.48 | 59.03 | ND |
| Other Income / PBT | OI / PBT | 16.77% | 1.43% | 17.80% | 21.85% | 10.27% | 22.16% | ND |
| Effective Tax Rate | Tax / PBT | 25.88% | 25.09% | 25.92% | 25.97% | 25.54% | 25.72% | ND |
| PAT Margin | PAT / Rev | 5.74% | 5.90% | 6.57% | 5.61% | 6.25% | 5.98% | ND |
| Gross margin | (Rev - materials - inv change) / Rev | 41.28% | 34.91% | 36.93% | 39.97% | 35.94% | 39.05% | ND |

### 1C. SUBSIDIARY CONTRIBUTION (consolidated minus standalone; two US subsidiaries, net of intercompany eliminations; entity split NOT FOUND)

| Metric (Rs Cr) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 |
|---|---|---|---|---|---|---|
| Revenue | 74.99 | 90.91 | 98.30 | 147.09 | 189.21 | 318.83 |
| Operating EBITDA | 3.84 | 5.74 | 1.15 | 3.81 | 6.89 | 18.65 |
| Op EBITDA margin | 5.13% | 6.32% | 1.17% | 2.59% | 3.64% | 5.85% |
| Gross margin | 41.02% | 47.39% | 38.85% | ND | ND | ND |
| PBT reported | 18.22 | (0.08) | 13.15 | 13.07 | 13.07 | 17.33 |
| PBT ex-earnout | (1.36) | (0.08) | (5.04) | (6.51) | (5.12) | ND |
| PAT reported | 18.61 | (0.41) | 14.64 | 14.80 | 14.22 | 16.96 |
| PAT ex-earnout | (0.97) | (0.41) | (3.56) | (4.77) | (3.97) | ND |

Note: consolidated other expenses sit below standalone in Q2 FY27 (45.00 vs 45.60) and Q2 FY26 (43.90 vs 44.31). That is an elimination signature. Subsidiary figures are net, and the intercompany flow is NOT FOUND (A3-05).

---

## STEP 1D: STANDALONE vs CONSOLIDATED GAP (first-class metric, A3 F2)

| Period | Cons PAT (Rs Cr) | Standalone PAT (Rs Cr) | Gap (Rs Cr) | Gap % of standalone PAT | Gap ex-earnout % of standalone PAT |
|---|---|---|---|---|---|
| Q2 FY26 | 32.15 | 13.54 | 18.61 | 137.5% | (7.1%) |
| Q1 FY27 | 16.29 | 16.70 | (0.41) | (2.5%) | (2.5%) |
| Q2 FY27 | 34.01 | 19.38 | 14.64 | 75.5% | (18.4%) |
| H1 FY26 | 39.61 | 24.81 | 14.80 | 59.7% | (19.2%) |
| H1 FY27 | 50.30 | 36.08 | 14.22 | 39.4% | (11.0%) |
| FY26 | 73.28 | 56.32 | 16.96 | 30.1% | ND |

Reading: the reported gap is positive only because of the earnout gains. Ex-earnout, the US subsidiaries subtract from group PAT in every period shown. The Q2 FY27 ex-earnout drag (3.56) is the largest single-quarter drag in the table. Standalone revenue is 75.0% of consolidated in Q2 FY27 (294.79 / 393.09), yet the deck puts India geography at 7% of revenue (pres L359). So the standalone entity is mainly an exporter (A3 FN18).

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

### 2A. Consolidated

| Metric | Q2 FY26 | Q2 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 310.63 | 393.09 | +26.54% | Strong |
| Operating EBITDA | 31.19 | 34.17 | +9.54% | Weak vs revenue |
| Operating EBITDA Margin | 10.04% | 8.69% | -135 bps | Contraction |
| Depreciation | 10.57 | 11.37 | +7.62% | Leverage |
| Finance Costs | 6.81 | 6.10 | -10.42% | Lower |
| EBIT (operating) = Op EBITDA - D | 20.63 | 22.80 | +10.53% | Modest |
| Other Income | 22.66 | 22.62 | -0.20% | Flat; both quarters carry an earnout |
| Core Operating PBT (PBT - OI) | 13.82 | 16.70 | +20.86% | Positive |
| Reported PBT | 36.48 | 39.31 | +7.77% | Inflated base and current |
| PAT | 32.15 | 34.01 | +5.81% | Inflated base and current |
| PAT ex-earnout | 12.57 | 15.82 | +25.85% | Positive headline, FX-driven: the 3.86 FX swing is about 2.88 after tax at 25.17%, about 89% of the 3.25 gain (ties to deck 25.8%, pres L391) |
| PBT ex-earnout ex-FX (res L548, L213, L288, L286) | 18.86 | 19.22 | +1.91% | Flat; the FX gain and lower interest income offset |
| EPS (share-adjusted) Rs | 4.05 | 4.28 | +5.68% | Inflated |

Bear counter (A5 P3, loop 1): the consolidated FX line swung from a 19.54 Mn loss to a 19.01 Mn gain (res L286). The 38.55 Mn swing is about 28.85 Mn after tax at 25.17%. That is about 89% of the 32.49 Mn normalized PAT gain (125.70 to 158.19 Mn; res L552, L213, L288). Ex-earnout and ex-FX, consolidated PBT rose 1.91% (188.56 to 192.17 Mn; res L548, L213, L288, L286) on revenue +26.54%. Other other-income fell 25.21 Mn, mostly interest [INFERENCE from H1: res L212 gives H1 interest income only, 23.27 vs 100.83 Mn; the Q2 split is NOT FOUND], and offsets the FX gain. Core PBT (+20.86%) strips FX and interest alike, so the core figure stands. The +25.85% normalized PAT headline is FX-driven and does not stand unqualified. A 14.48 Mn US deferred-tax credit also lifts it (Step 4 tax bullet).

### 2B. Standalone

| Metric | Q2 FY26 | Q2 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 235.64 | 294.79 | +25.10% | Strong; no India-entity shrink this quarter |
| Operating EBITDA | 27.35 | 33.02 | +20.73% | Good |
| Operating EBITDA Margin | 11.61% | 11.20% | -41 bps | Mild contraction |
| Gross margin (res L538, L541, L542) | 41.28% | 36.93% | -435 bps | Contraction; larger than consolidated -381 bps |
| Depreciation | 7.22 | 7.53 | +4.35% | Leverage |
| Finance Costs | 4.93 | 3.99 | -19.23% | Lower |
| EBIT (operating) | 20.13 | 25.49 | +26.61% | Good |
| Other Income | 3.06 | 4.66 | +52.04% | FX swing +3.84 |
| Core Operating PBT | 15.20 | 21.50 | +41.49% | Strong (strips all other income, FX and interest alike) |
| PBT ex-FX (PBT - net FX; res L285, L548) | 20.21 | 24.27 | +20.07% | Good; below revenue +25.10% |
| Reported PBT | 18.26 | 26.16 | +43.26% | Strong headline; the 3.84 FX swing is 48.7% of the 7.90 gain |
| PAT | 13.54 | 19.38 | +43.18% | Strong headline; FX-assisted |
| EPS (share-adjusted) Rs | 1.71 | 2.44 | +42.69% | Strong headline; FX-assisted |

Bear counter (A5 P1, loop 1): the standalone FX line swung from a 19.54 Mn loss to an 18.89 Mn gain (res L285). The 38.43 Mn swing is 48.7% of the 78.99 Mn standalone PBT gain (182.60 to 261.59 Mn; res L548). Ex-FX, standalone PBT grew 20.1% (202.14 to 242.70 Mn), below standalone revenue growth of 25.1% (res L538). Standalone gross margin fell 435 bps (41.28% to 36.93%; res L538, L541, L542). H1 standalone CFO was 25.31 Mn against 360.78 Mn PAT, 0.07x (res L229, L552). H1 standalone op EBITDA also carries a 30.53 Mn ECL write-back against a 10.08 Mn charge a year earlier (res L216); the quarter split is NOT FOUND (Q22). The PAT +43.18% headline does not stand unqualified.

### 2C. Six diagnostic answers

1. Did revenue grow YoY? Yes. Consolidated +26.54% (310.63 to 393.09). Standalone +25.10%. Subsidiaries +31.08% (74.99 to 98.30). No company numeric guidance exists to compare against (A3 FN-07: "positive on the outlook for the year", no figure, pr L107). Base case: ND. Breadth (A5 loop-1 N2) [INFERENCE from MGMT shares and growth rates; the p12 slice-to-label mapping is unassigned in A1 pres R131-R135, so both mappings are tested]: Aerospace (+62%) and Industrial (+29%) gave increments of 881.7-981.0 Mn (pres L334-L355; res L538). That is 107-119% of the 824.56 Mn YoY increase. The other 22% of revenue (Defence, Med Tech, Auto & Others) shrank 6-15% in aggregate (921.9-1,021.3 Mn to 864.8 Mn). Defence grew 13% and Med Tech 14% (pres L358-L362), so Auto & Others fell sharply; its value is NOT DISCLOSED. Aerospace alone gave 57-86% of the increase (Q30).
2. Did operating EBITDA margin expand? No. Consolidated Q2 FY27 margin 8.69% vs Q2 FY26 10.04% = -135 bps. Standalone 11.20% vs 11.61% = -41 bps. Subsidiaries 1.17% vs 5.13% = -396 bps. YoY, the cause is gross margin: consolidated 37.41% vs 41.22% = -381 bps. Opex fell as a share of revenue (A3 FN01): employee ratio 17.27% vs 17.04% (on the corrected 52.94 base) = +23 bps; other expense ratio 11.45% vs 14.13% = -268 bps. QoQ the read reverses (A5 loop-1 N1): op EBITDA margin fell 178 bps (10.48% to 8.69%) = gross margin -53 bps (37.94% to 37.41%), employee ratio +3 bps (17.24% to 17.27%) and other-expense ratio +122 bps (10.23% to 11.45%). Other expenses rose 17.7% (382.41 to 450.02 Mn) on revenue +5.2% (res L538-L548). So opex gave 125 of the 178 bps QoQ fall. The YoY opex leverage has two readings (Step 4).
3. Did core operating PBT grow YoY? Yes. Consolidated core PBT +20.86% (13.82 to 16.70). It grew faster than reported PBT (+7.77%), because the earnout gain shrank (19.58 to 18.20) and finance cost and D&A grew slower than revenue. Headline growth is not inflated YoY. The level is inflated: the earnout is 46.3% of Q2 FY27 PBT (18.20 / 39.31).
4. What drove the gap between core PBT growth and reported PAT growth? Core PBT +2.88; other income (0.05) (earnout (1.38), FX +3.86, other other-income (2.52)); PBT +2.84; tax (0.97); PAT +1.87. The tax charge rose 22.3% (43.32 to 52.99 Mn, res L551) while PBT rose 7.77%, because Q2 FY27 has a smaller untaxed gain share. Exceptional items: none (no line in template).
5. Are D&A and finance costs scaling faster than revenue? No. D&A +7.62% and finance cost -10.42% vs revenue +26.54%. No capex absorption deficit. Warning: gross borrowings rose to 131.96 from 106.13 in H1 (res L170, L177), so finance cost may rise from Q3 [INFERENCE].
6. Is Other Income concentration changing? H1 FY27 other income 22.88 of which the earnout is 18.20 (79.5%). Q1 FY27 other income was 0.27. Ex-earnout and ex-FX, Q2 other income fell to 2.52 from 5.04 (interest income H1 2.33 vs 10.08, res L212). Treasury yield is falling as cash moved into working capital.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY (consolidated, six quarters)

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT ex-OI (Rs Cr) | One-offs Flagged | QoQ Run-Rate (revenue) |
|---|---|---|---|---|---|
| Q1 FY26 | 278.43 (filing: H1 FY26 minus Q2 FY26) | 9.00% (filing-derived) | 5.93 | none known | ND (Q4 FY25 not in run) |
| Q2 FY26 | 310.63 (res L538) | 10.04% | 13.82 | Earnout 19.58 in OI (pres L385; res L213) | +11.57% |
| Q3 FY26 | 303.3 (deck, pres L249) | 9.07% filing basis (deck base bar 275 / 3,033; ties to filed H2 FY26 op EBITDA 705.68 Mn less deck Q4 431 Mn); 10.2% deck-normalized under reading (a), with the 34 Mn added back (pres L253, L256, L267) | ND (H2 FY26 combined 37.16) | 3.4 one-off on the deck EBITDA chart; direction and filed line NOT FOUND; the PAT tie-out favours a charge the deck adds back (FN11; cross-check below) | -2.36% |
| Q4 FY26 | 369.1 (deck, pres L247) | 11.7% (deck, pres L265) | ND (H2 FY26 combined 37.16) | none disclosed | +21.69% |
| Q1 FY27 | 373.80 (res L538) | 10.48% | 21.95 | FX loss (2.06) in OI | +1.27% |
| Q2 FY27 | 393.09 (res L538) | 8.69% | 16.70 | Earnout 18.20 and FX gain 1.90 in OI | +5.16% |

Cross-check (rewritten in loop 1): deck Q3 + Q4 FY26 revenue 3,033 + 3,691 = 6,724 Mn = filed H2 FY26 6,724.24 Mn (pres L247-L250; res L538). Deck Q3 + Q4 EBITDA 309 + 431 = 740 Mn; minus the 34 Mn one-off = 706 Mn = filed H2 FY26 op EBITDA 705.68 Mn (pres L247-L256; res L539-L548). So the filed operating EBITDA excludes the 34 Mn, and the deck's 309 bar includes it.
PAT tie-out: the deck PAT chart gives Q3 FY26 138 and Q4 FY26 224 (pres L269, L271, positional read). Deck H2 FY26 PAT = 362 Mn. Filed H2 FY26 PAT = 732.82 - 396.08 = 336.74 Mn (res L552). The gap is 25.26 Mn. The 34 Mn one-off after tax at 25.17% is 25.44 Mn. The other four deck quarters tie to filed PAT within 0.5 Mn: Q1 FY26 75 vs 74.63; Q2 FY26 321 vs 321.45; Q1 FY27 163 vs 162.85; Q2 FY27 340 vs 340.14 (pres L265-L273; res L552).
Two readings:
- (a) A charge inside filed operating costs that the deck adds back. This fits the PAT tie-out: deck PAT sits above filed PAT by the after-tax one-off. Under (a), 9.07% is the filing-basis Q3 FY26 margin and 10.2% is the deck-normalized margin.
- (b) A gain booked outside operating EBITDA (in filed other income), stacked on the deck bar like the earnout segments on the PAT chart. This fits the chart layout. It does not fit the PAT tie-out: with the gain inside filed PAT, deck PAT would equal filed PAT.
The PAT tie-out favours reading (a) [INFERENCE]. The separating observation is the filed Q3 FY26 quarterly P&L, or the answer to Q29. The direction matters for the TTM ex-earnout base (Step 6A): about 68.3 Cr under (a), about 63.2 Cr under (b).

Diagnostics:
- Trajectory: revenue STEPPING UP (three consecutive QoQ rises after the Q3 FY26 dip; TTM revenue 1,439.31). Margin DIPPING: 11.7% (Q4 FY26), 10.48% (Q1 FY27), 8.69% (Q2 FY27). Q2 FY27 is the lowest operating margin of the six quarters.
- One-off distortion: Q2 FY26 and Q2 FY27 both carry earnout gains in OI. The core PBT and operating margin columns exclude them. Q3 FY26 carries a 3.4 deck one-off.
- Latest quarter vs H1 average: H1 FY27 average revenue 383.45 per quarter; Q2 393.09 is above it. H1 FY27 operating margin 9.56%; Q2 8.69% is below it. Core PBT H1 average 19.32; Q2 16.70 is below it. No capex commissioning thesis applies (CWIP 3.96, H1 capex 14.34).
- Implied Q3 FY27 base to hold trajectory: revenue at or above 393.09 and operating margin back at or above the H1 average 9.56%. A third quarter below 9.56% confirms the dip as a trend.

---

## STEP 4: OPERATIONAL DECOMPOSITION (consolidated PAT bridge, Q2 FY27 vs Q2 FY26)

Base: reported PAT Q2 FY26 32.15. All values Rs Cr. Employee cost for Q2 FY26 uses the corrected 52.94 (A3-14).

| Component | YoY Change (Rs Cr) | YoY Change (% of Q2 FY26 PAT) | Recurring? |
|---|---|---|---|
| Revenue contribution to gross profit (at prior op EBITDA margin 10.04%) | +8.28 | +25.76% | Recurring |
| Margin change contribution (8.69% vs 10.04% on 393.09) | (5.30) | (16.50%) | Recurring |
|   of which gross margin -381 bps | (14.96) | (46.55%) | Recurring unless mix is one-off (FN02 two readings) |
|   of which employee ratio +23 bps | (0.89) | (2.77%) | Recurring |
|   of which other expense ratio -268 bps | +10.55 | +32.83% | Contested: recurring under reading (a); under reading (b) about 7.23 of it is a Q2 FY26 base spike (two readings below) |
| D&A change | (0.81) | (2.50%) | Recurring |
| Finance cost change | +0.71 | +2.21% | Recurring (debt rose in H1, may reverse) |
| Other Income change | (0.05) | (0.14%) | NON-RECURRING |
|   of which earnout gain 18.20 vs 19.58 | (1.38) | (4.29%) | NON-RECURRING |
|   of which FX +1.90 vs (1.95) | +3.86 | +11.99% | NON-RECURRING |
|   of which other other-income 2.52 vs 5.04 | (2.52) | (7.84%) | Mixed (interest on falling cash) |
| Effective tax rate change | (0.97) | (3.01%) | Mixed |
|   of which tax on higher PBT at prior ETR 11.88% | (0.34) | (1.05%) | Mixed |
|   of which ETR change (13.48% vs 11.88%) | (0.63) | (1.96%) | Mixed (falls as untaxed share falls) |
| Exceptional items | 0.00 | 0.00% | NON-RECURRING (no line; earnout is the de facto exceptional) |
| **Reported PAT YoY change** | **+1.87** | **+5.81%** | |

Mandatory questions:
- Recurring vs non-recurring share of the YoY change: pre-tax, recurring operations gave +2.88 (op EBITDA +2.98, D&A (0.81), finance cost +0.71) and other income gave (0.05). Almost all of the PBT change is operating. The level is the problem: the 18.20 earnout is 53.5% of Q2 PAT (A3-04, FN05, FN-03).
  - The operating +2.88 rests wholly on opex leverage: other expenses +10.55 and employee (0.89) against gross margin (14.96) (A5 loop-1 N1). QoQ the opex leg reversed: op EBITDA margin -178 bps = gross margin -53 bps, employee +3 bps, other expenses +122 bps; other expenses rose 17.7% (382.41 to 450.02 Mn) on revenue +5.2% (res L538-L548). Core PBT fell 23.9% QoQ (21.95 to 16.70; res L539, L548).
  - Other-expense ratio by period: Q1 FY26 10.45%, Q2 FY26 14.13%, H2 FY26 12.29%, Q1 FY27 10.23%, Q2 FY27 11.45%. Combined employee plus other-expense ratio: 31.21%, 31.18%, 29.55%, 27.47%, 28.72% (Q2 FY26 employee on the corrected 529.42 Mn; res L538, L543, L546).
  - Reading (a): Q2 carries seasonally high other expenses. The ratio rose from Q1 to Q2 in both years (+368 bps in FY26, +122 bps in FY27). Then the YoY leverage is like-for-like and recurring.
  - Reading (b): Q2 FY26 was a spike. About 7.23 of the 10.55 leg is the gap between the Q2 FY26 ratio (14.13%) and the H2 FY26 average (12.29%) on Q2 FY27 revenue. The leverage peaked in Q1 FY27 (27.47% combined). Q2 FY27 then gave part of it back on the "investment into sales, strategy and strengthening capabilities" the deck names (pres L255-L257, L378-L379).
  - Separating observation: the Q3 FY27 combined opex ratio against the H2 FY26 average of 29.55%. Below it supports (a); at or above it supports (b) [INFERENCE]. Step 8C carries it as a co-reading.
- If Other Income reverts: if Q2 other income fell to the Q1 FY27 level (0.27), PBT = 39.31 - 22.62 + 0.27 = 16.96; at the 25.17% statutory rate, PAT = 12.69 per quarter, 50.77 annualised. Ex-earnout only: PAT 15.82 per quarter, 63.28 annualised.
- D&A and finance cost state: D&A 11.37 vs 11.10 QoQ (+2.5%), near steady. Finance cost flat QoQ at 6.10 vs 6.12, but gross borrowings rose 25.83 in H1 and lease liabilities rose 5.50 (res L170-178). Steady state is likely higher from Q3 [INFERENCE].
- Tax adjustments: yes. The subsidiaries booked a deferred-tax credit of 1.45 (14.48 Mn) in Q2 (cons (16.12) minus standalone (1.64) Mn, res L550), 368 bps of consolidated PBT. Subsidiary DTA rose to 6.35 from 4.90 (res L143) on US losses. Ex-earnout consolidated ETR is 25.09% only because the US loss is tax-effected (A5 loop-1 N3). Before the credit, Q2 ex-earnout tax is 67.47 Mn on 211.18 Mn of PBT, a 31.95% rate (res L548, L551, L288). The credit is 9.2% of Q2 normalized PAT (158.19 Mn). It grew from 3.93 Mn in Q2 FY26 (cons (2.57), standalone 1.36 Mn). Without the credit in both quarters, normalized PAT rose 18.0% (121.77 to 143.71 Mn), not 25.85%. Ex the credit and ex FX after tax at 25.17%, it fell about 5.1% (136.39 to 129.48 Mn) [derived; res L286, L550-L552]. The pattern reversed once already: the subsidiary deferred tax was a 17.33 Mn credit in H1 FY26 and a 24.35 Mn charge in H2 FY26 (res L550; A3-11). Standalone ETR 25.09-25.97% is normal (FN06).

Below-EBITDA offset that holds normalized PAT margin flat (answers A3 FN-02): normalized PAT margin 4.02% vs 4.05% (-2 bps; pres L392) while operating EBITDA margin fell 135 bps. The offset by line, as a share of revenue: D&A +51 bps, finance cost +64 bps, other income ex-earnout +13 bps, tax +5 bps. Total +133 bps. So 115 of the 133 bps is leverage on D&A and finance cost. 13 bps is FX-inclusive other income. About half the offset (64 bps) rests on finance cost, which fell 10.42% YoY (61.01 vs 68.11 Mn; res L544) while gross borrowings rose 24.3% in H1 (1,061.25 to 1,319.60 Mn; res L170, L177) and lease liabilities rose 8.3% (661.49 to 716.46 Mn; res L171, L178). The deck credits the YoY fall to "lower working capital borrowings" (pres L381-L382). That YoY cause cannot be tested: the 30-Sep-2025 borrowing balance is NOT FOUND. H1 FY26 repayments of current and non-current borrowings (992.96 and 746.72 Mn; res L244-L245) and a 33.0% fall in H1 interest paid (143.09 to 95.86 Mn; res L248) fit it. The whole YoY fall sits in standalone (49.34 to 39.85 Mn); subsidiary finance cost rose (18.77 to 21.16 Mn; res L544). The H1 FY27 build (gross borrowings +24.3%) points to higher finance cost from Q3 [INFERENCE]. The normalized PAT gain itself is about 89% FX (Step 2A). The bear lean in FN-02 is partly resolved: the D&A leg (51 bps) is recurring, but the finance-cost leg (64 bps) is at risk from Q3 on the H1 debt build [INFERENCE].

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 FY27 actuals; Reg 33 half-year statements)

Basis: flows are H1 FY27 vs H1 FY26 (res L206-L254). Balances are 30-Sep-26 vs 31-Mar-26 (res L135-L190). Days (filing basis) = balance / trailing-12-month revenue x 365: Sep-26 on TTM revenue 1,439.31 (cons) and 1,078.36 (standalone); Mar-26 on FY26 revenue. Deck days are on an undefined basis (pres L284; FN08) and shown separately.

### 5A. Consolidated

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (res L229) | 139.67 (H1 FY26) | 14.75 (H1 FY27) | (124.92) | Weak; H1 FY26 was lifted by a 109.71 receivable release (res L220) |
| CFO/PAT ratio | 3.53x | 0.29x (0.46x on ex-earnout PAT 32.10) | -3.24x | Below the lowest Pillar 2 band (0.65x) |
| CFO / Op EBITDA | 248.3% | 20.1% | | Weak |
| Capex, PPE and intangibles (res L234) | 32.54 | 14.34 | (18.20) | Low |
| FCF (CFO - Capex) | 107.14 | 0.41 | (106.73) | Near zero |
| FCF after lease payments (res L246-247) | 98.90 | (7.88) | | Negative |
| Working capital change (res L220-226) | +100.60 | (50.64) | (151.24) | Absorbing; inventory (51.79), payables +47.87 |
| Receivable days (filing basis) | 88.9 | 77.6 | -11.3 | Improving |
| Inventory days (filing basis, on revenue) | 187.3 | 177.8 | -9.5 | Improving, still very high |
| Payable days (filing basis, on revenue) | 79.1 | 81.1 | +2.0 | Stable |
| Cash Conversion Cycle (inv + rec - pay) | 197.1 | 174.3 | -22.9 | Improving on filing basis |
| NWC days incl. contract assets (A3-08 basis) | 209.8 | 189.0 | -20.8 | Above 161 on this basis |
| Deck DIO / DSO / DPO / advances / NWC (pres L286-L315) | Q4 FY26: 153 / 74 / 64 / 18 / 145 | Q2 FY27: 162 / 73 / 68 / 13 / 153 | NWC +8 vs Q4 FY26; +14 vs Q2 FY26 (139) | Advances falling four quarters (FN07) |
| PPE (res L135) | 176.39 | 176.87 | +0.48 | Flat |
| CWIP (res L136) | 2.12 | 3.96 | +1.84 | No large project |
| Gross borrowings (res L170, L177) | 106.13 | 131.96 | +25.83 | Rising |
| Cash + other bank balances + current investments (res L151-154) | 145.80 | 154.60 | +8.80 | |
| Net Debt / (Net Cash), ex-leases | (39.68) net cash | (22.64) net cash | net cash -17.04 | Weaker |
| Net debt incl. lease liabilities (res L171, L178) | 26.47 | 49.01 | +22.54 | Weaker |
| Promoter Pledge | ND (not in filing; Notion memory: zero) | ND (not in filing) | ND | ND |

### 5B. Standalone

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (res L229) | 138.81 | 2.53 | (136.28) | Very weak |
| CFO/PAT ratio | 5.60x | 0.07x | -5.53x | Far below band |
| Capex (res L234) | 31.65 | 14.20 | (17.45) | Low |
| FCF (CFO - Capex) | 107.16 | (11.67) | (118.83) | Negative |
| Working capital change (res L220-226) | +103.20 | (56.42) | (159.62) | Inventory build (43.43) |
| Receivable days (filing basis) | 100.4 | 86.6 | -13.8 | Improving |
| Inventory days (filing basis) | 209.7 | 198.0 | -11.7 | Very high |
| Payable days (filing basis) | 100.2 | 97.6 | -2.6 | Stable |
| Cash Conversion Cycle | 209.9 | 187.0 | -22.9 | Improving, high |
| PPE (res L135) | 151.89 | 152.90 | +1.01 | Flat |
| CWIP (res L136) | 2.12 | 3.96 | +1.84 | |
| Borrowings (res L565, R992-R993) | nil | 28.79 current | +28.79 | New short-term debt (A3-03) |
| Net Debt / (Net Cash) | (140.78) | (118.82) | net cash -21.96 | Weaker |
| Promoter Pledge | ND | ND | ND | ND |

Subsidiary balance sheet (consolidated minus standalone): borrowings 103.17 (Mar 106.13), of which current 67.18 (Mar 28.30); cash 6.99 (Mar 5.02); net debt about 96.18 (Mar 101.11). Trade payables 31.52 vs 14.62 (+115.6%). Other current financial liabilities 4.76 vs 22.31 [INFERENCE: holds the earnout residual]. Goodwill 73.09 and acquired intangibles 44.80, together 117.89 = 11.0% of consolidated equity 1,068.20 (A3-06, A3-08).

Acquisition-economics probe (A5 P4, loop 1; subsidiary figures are consolidated minus standalone, net of intercompany eliminations, entity split NOT FOUND):
- Consideration: NOT FOUND in the three extracts. The acquired carrying value stands in as the price proxy.
- Carrying value: goodwill 730.94 Mn + acquired intangibles 447.97 Mn = 1,178.91 Mn (res L137-L138).
- Earnings base: subsidiary TTM op EBITDA 217.37 Mn = H2 FY26 148.43 + H1 FY27 68.94 (res L538-L548). Carrying value / TTM op EBITDA = about 5.4x. On Q2 FY27 annualised (11.51 x 4 = 46.04 Mn) it is about 25.6x.
- Profit: subsidiary TTM PAT ex-earnout (18.17) Mn = H2 FY26 21.57 + H1 FY27 (39.74) (res L552, L213, L288). There is no positive earnings multiple.
- Seller performance: earnout fair-value write-backs 195.75 Mn (H1 FY26) + 181.95 Mn (Q2 FY27) = 377.70 Mn = 32.0% of the carrying value (res L213, L288).
- Leverage: subsidiary net debt 961.79 Mn (borrowings 1,031.69 less cash 69.90; res L153, L170, L177) = about 4.4x TTM op EBITDA, of which 671.80 Mn is current.
- Reading: the 5.4x looks cheap only because TTM includes H2 FY26; subsidiary op EBITDA fell from 148.43 Mn in H2 FY26 to 68.94 Mn in H1 FY27 and to 11.51 Mn in Q2 FY27. This is a leveraged, low-margin asset that loses money ex-earnout. The bear reading survives.

### 5C. Mandatory questions

- Is CFO/PAT meeting the Pillar 2 cash band? No band is set in Notion (no valuation). H1 FY27 consolidated CFO/PAT 0.29x (0.46x ex-earnout) sits below the lowest band, 0.65x. Standalone 0.07x. One H1 reading is noisy: H1 FY26 was 3.53x on a receivable release. Notion memory records four-year CFO of about Rs (25) Cr against Rs 234 Cr reported profit (SECONDARY, prior Notion). Pillar 2 flag raised; the band decision is deferred to /fttcp and Role 1 (OR-30).
- Is the WC drag structural or growth-induced? Test: if growth stopped tomorrow, would WC days stay high? Inventory is 177.8 days of TTM revenue (filing basis) and 162 days on the deck basis. It is the dominant item and does not fall with slower growth. Customer advances fell from 33 to 13 days over four quarters (pres L305-L315) while the book hit a record, so new orders carry fewer advances (FN07). Agency evidence (Notion memory, AGENCY): CRISIL gross current asset days net of cash 311 at 31-Mar-2026 vs 236 earlier; that rating was withdrawn at company request on 02-Jul-2026. Bull side: filing-basis CCC improved 22.9 days in H1, receivable days fell 11.3, and deck NWC improved QoQ 161 to 153. Classification: INDETERMINATE-WITH-DIRECTION, direction STRUCTURAL. Missing evidence: (a) the operator ruling on which NWC basis and which print (H1 or Q4 FY27) the falsifier uses; (b) the deck NWC formula; (c) Q2 FY27 standalone CFO; (d) customer-advance terms on the new book.
- Did CWIP capitalise as expected? No commissioning was projected. CWIP rose 1.84; PPE +0.48. Right-of-use assets rose 6.15 consolidated and 7.49 standalone (res L139) [INFERENCE: a new India lease].
- Did net debt move within the projected range? No projection exists. Group net cash fell to 22.64 from 39.68. Standalone added 28.79 of new current borrowings to fund a 43.43 inventory build against standalone CFO of 2.53 (A3-03). About 27.8 of US term debt moved to current [INFERENCE, before FX] and subsidiary current borrowings rose to 67.18 from 28.30. A 12-month US refinancing need exists (A3-08). The deck says finance cost fell YoY "driven by lower working capital borrowings" (pres L381-L382). That YoY cause cannot be tested: the 30-Sep-2025 balance is NOT FOUND. H1 FY26 repayments (992.96, 746.72 Mn; res L244-L245) and a 33% fall in interest paid (143.09 to 95.86 Mn; res L248) fit it. The H1 FY27 build (gross borrowings +24.3%) points to higher finance cost from Q3 [INFERENCE] (FN09).

Checkpoint: cash conversion = INDETERMINATE-WITH-DIRECTION (structural). This caps the protocol verdict at PROCEED WITH CAVEATS or below, with the missing evidence named above.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
Tracker rows were not supplied (Notion Downstream Signals property empty). This agent has no Notion access.

| Signal Name | Type | Cadence | Latest Observation Date and Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| ND (no rows on file) | ND | ND | ND | ND | ND | ND |

FLAG: zero signals on file, below the three-signal floor. Role 5.5 must reopen for this company (OR-17 floor applies to /fttcp).

### 5.5B. Target vs signal reconciliation
Not possible. Target reported: revenue strong (+26.54% YoY), margin weak (-135 bps). Signals: ND. Outcome cell: ND.

### 5.5C. New signals surfaced
No tracker write this run. Candidate signals are emitted as payload rows for the operator-approval write gate (Role 5.5 Step 4 in claude.ai):
| Candidate signal | Why (this quarter's evidence) | Thesis element |
|---|---|---|
| Global semiconductor equipment sales / billings (SEMI) | Deck names semicap as a new vertical; cites SEMI record 2026 sales of $165.9 Bn (pres L127-128) | EXPAND stage new industries (FN13, FN17) |
| Commercial aerospace OEM build rates (anchor customer end market) | Aerospace grew 62% YoY and leads revenue share (pres L353-356) | Revenue momentum, order book |
| Electronic component and PCB price index | Gross margin -381 bps YoY with material ratio +379 bps (pres L376; FN01) | Notion test 2, gross margin |
| AI data-center capex | Deck names AI/data center as a new vertical (pres L127, L192) | EXPAND stage |
Statement: "No new signal written this quarter. Four candidates emitted for the Role 5.5 gate."

### 5.5D. Forward-view weighting
No signal trajectory exists, so Step 6 rests on the single-quarter filing print alone. Single-quarter weight is therefore high, and conservative interpretation binds.

---

## STEP 6: RECONCILIATION vs THESIS (PRE-THESIS READ)

### 6A. Variance vs Notion projections

| Metric | Bear Proj | Base Proj | Bull Proj | Actual | Lands In |
|---|---|---|---|---|---|
| Revenue (Q2 FY27 / H1 FY27, Rs Cr) | ND | ND | ND | 393.09 / 766.89 (res L538) | ND (no projections) |
| EBITDA Margin (operating) | ND | ND | ND | 8.69% Q2 / 9.56% H1 | ND |
| PAT (Rs Cr) | ND | ND | ND | 34.01 reported, 15.82 ex-earnout (Q2); 50.30 / 32.10 (H1) | ND |
| EPS (Rs) | ND | ND | ND | 4.28 reported, 1.99 ex-earnout (Q2); TTM 10.58 reported, 8.29 ex-earnout (filed basis; 7.97-8.61 across the two Q3 FY26 one-off readings) | ND |
| Net Debt (Rs Cr) | ND | ND | ND | (22.64) net cash ex-leases; 49.01 net debt incl. leases | ND |
| ROCE | ND | ND | ND | H1 annualised operating EBIT 101.73 / (equity + borrowings) 1,200.16 = 8.48%; net of cash and bank 9.73% (basis stated; Notion's 11.4% FY26 / 9.9% basis not reproduced) | ND |

TTM EPS basis: reported 9.23 - 4.99 + 6.34 = 10.58. Ex-earnout TTM PAT on the filed basis = H2 FY26 33.67 + H1 FY27 32.10 = 65.78; / 79.38 Mn shares = 8.29. H2 FY26 carries no earnout per pres L448. The Q3 FY26 34 Mn one-off makes this base two-sided (Step 3 cross-check). Under reading (a), a charge in filed costs that the deck adds back, the normalized TTM ex-earnout PAT is 65.78 + 2.54 = 68.32 (EPS 8.61). Under reading (b), a gain in filed other income, it is 65.78 - 2.54 = 63.23 (EPS 7.97). The 2.54 is the 34 Mn one-off after tax at 25.17% (25.44 Mn). Range: about 63.2-68.3. The PAT tie-out favours the upper end [INFERENCE].
Probability re-weighting state: not applicable (no projections; first tracked quarter).

### 6B. Watchlist item status (the six named Notion tests)

| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| 1 | Cash falsifier (consolidated NWC days and CFO) | NWC <=120 days by Q4 FY27 with positive CFO falsifies STRUCTURAL | Any print above 161 days confirms STRUCTURAL | H1 CFO +14.75 (positive). NWC: filing basis 189.0 days TTM (incl. contract assets), CCC 174.3; deck basis 153 (Q1 FY27 161). FY26 logged 169 is not reproducible on either basis (filing 209.8; deck Q4 FY26 145). | AMBER. Reading A (H1 print counts): on the filing basis 189.0 > 161, so STRUCTURAL is confirmed; on the deck basis 153 sits between 120 and 161, so neither fires. Reading B (only Q4 FY27 counts): the H1 print is directional only; the test stays open until the Q4 FY27 disclosure. Both readings need the basis ruling first. |
| 2 | Gross margin | Compression stops, or a component-cost answer is given | A third quarter of compression without a component-cost answer | Consolidated gross margin 41.22% (Q2 FY26), H2 FY26 average 40.05%, 37.94% (Q1 FY27), 37.41% (Q2 FY27). YoY: Q1 -226 bps, Q2 -381 bps. QoQ -53 bps. Management cause: "one-off Revenue mix impact and purchases towards product development" (pres L374-375). YoY, the p11 commentary's opex cause (pres L255-257) does not fit: opex fell 245 bps as a share of revenue (FN01). QoQ it fits: the combined opex ratio rose 125 bps (27.47% to 28.72%) and gave 125 of the 178 bps margin fall (Step 4). | RED (provisional). On Notion's own log (Q4 FY26 and Q1 FY27 compressed), Q2 FY27 is the third quarter. The answer given is mix and product development, not component cost. The filing alone confirms two YoY compressions; the third count rests on the Notion Q4 FY26 entry. |
| 3 | Order book momentum | Book rising, book-to-bill >=1x | Falling book | 28,137 Mn (Rs 2,813.7 Cr), +2,148 Mn QoQ (+8.27%) and +5,226 Mn YoY (+22.8%) (pres L229-230, L414). Stated book-to-bill 1.6x (pres L179); walk-implied 1.55x. Stated intake +15.4% YoY (pr L94) does not tie to the book walk (closing book - opening book + revenue): Q2 FY26 = 22,911 - 21,318 + 3,106.34 = 4,699 Mn; Q2 FY27 = 28,137 - 25,989 + 3,930.90 = 6,079 Mn; walk-implied YoY intake +29.4% (pres L289-L294; res L538). For +15.4% to hold, the Q2 FY26 book must have lost 568-751 Mn to cancellations, FX revaluation or re-scoping. None is disclosed. | GREEN (with two tie-out caveats: 1.55x vs 1.6x, FN-05; intake YoY +29.4% by walk vs +15.4% stated) |
| 4 | Proof gate | Design-led share double digits on the standalone services-over-time proxy for two quarters, plus >=100 bps reported consolidated EBITDA margin uplift | Margin flat or down; share below 10% | Margin leg: -135 bps YoY (Q2); +1 bp (H1, pres L414). Design-led share: NOT DISCLOSED. "Others share includes B2S" with no figure (pres L361). Services-over-time revenue proxy: NOT FOUND in the results; contract assets +32.7% is indirect only. | RED on the margin leg; UNKNOWN on the share leg. Gate NOT FIRED. |
| 5 | Related-party flow to parent Cyient Ltd | Flow stable or falling | Subcontracting or payables to parent rising | No RPT disclosure at H1. Standalone other current financial liabilities +9.55 and trade payables +29.62, unattributed (res L181, L183). | UNKNOWN (NOT FOUND) |
| 6 | Standalone vs consolidated divergence | Both legs grow profitably | One leg loss-making or shrinking | Standalone revenue +25.10% YoY, op EBITDA margin 11.20%. Subsidiaries op EBITDA 1.15 (1.17%), PAT ex-earnout (3.56). Second Q2 earnout write-back. | RED for the US leg. The divergence has reversed: in FY26 the India entity shrank; now the US arm is the weak leg. |

### 6C. Thesis-broken trigger check

| Thesis-Broken Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| None signed (Notion: ND) | ND | ND | NO (no condition exists) |

Candidate tripwires for the operator to sign at Halt 1 (not conditions yet, so none can fire): (a) US subsidiary ex-earnout PBT negative for a third consecutive quarter (Q2 FY26 (1.36), Q1 FY27 (0.08), Q2 FY27 (5.04)); (b) a goodwill or intangible impairment on the US CGU at the FY27 test; (c) consolidated gross margin below 37.41% in Q3 FY27; (d) standalone short-term borrowings above 28.79 at 31-Mar-27 with standalone CFO negative; (e) related-party subcontracting to the parent rising in the FY27 AR.

### 6D. Growth trigger status

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| Order book momentum (Notion test 3) | ND (not signed) | Record book 28,137 Mn, +22.8% YoY; 1.6x stated; three new logos (pr L94-95) | Walk-implied 1.55x does not tie to 1.6x; stated intake +11% QoQ does not tie to the walk (+9.3%) (FN-05); stated intake +15.4% YoY does not tie to the walk (+29.4%, 4,699 to 6,079 Mn), which needs 568-751 Mn of undisclosed Q2 FY26 book reductions (pr L94; pres L289-L294; res L538) | ON TRACK (two tie-out caveats) |
| Box Build mix shift to higher-value integration | ND | Box Build +86% YoY, 37% share (pres L186, L357-358) | Material ratio +379 bps YoY in the same quarter; mix may be structurally material-heavy (FN02) | ON TRACK for revenue; WEAKENED for margin |
| Margin path to 11-13% in FY27-29 (EXPAND) | ND (company target, pres L165) | Q4 FY26 11.7% touched the band (pres L265) | Q2 FY27 8.69%, H1 9.56%, below the deck's own 9-11% "today" band in Q2 (FN04, FN17) | DELAYED |
| Design-led / B2S share to double digits (proof gate) | ND | B2S investment named (pr L97) | Share not disclosed; FY27 double-digit target dropped (Notion memory) | DELAYED (unmeasurable) |
| US arm (ex-Altek) turnaround | ND | Integration completed and renamed (pres L192; pr L103-104); subsidiary revenue +31.08% YoY | Subsidiary op EBITDA 1.17%; second earnout write-back implies missed targets [INFERENCE] (A3-06, FN05); acquisition probe (Step 5B): carrying value 5.4x a falling TTM op EBITDA, TTM PAT ex-earnout negative, net debt 4.4x | WEAKENED |
| New verticals (semicap, robotics, AI data center) | ND | Named on p7-p8 (pres L153-161, L192) | No revenue line or order figure for any of them (FN13) | DELAYED (unmeasurable) |

Checkpoint: 6A to 6D complete. No condition can fire. Three of six named tests read RED or RED-provisional (2, 4 margin leg, 6 US leg).

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

DEFERRED TO /fttcp AND ROLE 1 (operator ruling OR-30). No Expectation Ledger exists for this company (ND). Pillar-relevant facts flagged for the A21 base:
- FLAG A21-1: Q2 FY27 ex-earnout PAT 15.82, annualised 63.28. H1 FY27 ex-earnout PAT 32.10, annualised 64.21. TTM ex-earnout PAT 65.78 on the filed basis; about 63.2-68.3 across the two readings of the Q3 FY26 34 Mn one-off (Step 6A). The uncertainty runs both ways; the PAT tie-out leans to the upper end [INFERENCE]. Reported TTM PAT 83.97 includes the 18.20 earnout. Any run-rate base built on reported PAT overstates it by the earnout. The Q2-annualised base (63.28) carries 5.79 of annualised US deferred-tax credit (4 x 14.48 Mn); the H1-annualised base (64.21) carries 2.71 (2 x 13.54 Mn; res L550). The TTM base nets the 24.35 Mn H2 FY26 charge against the 13.54 Mn H1 FY27 credit (net 10.81 Mn charge), so TTM is the cleaner base.
- FLAG A21-2: The evidence shows no clear revenue seasonality: revenue rose in four of the five measured QoQ moves; Q3 FY26 dipped 2.36%; Q1 FY26 QoQ is ND (pres L249; Step 3). Six quarters cannot confirm or reject a seasonal pattern. The earnout does recur in Q2, and other expenses ran higher in Q2 than Q1 in both years (Step 4 reading a). Declare a trailing-four-quarter base ex-earnout (preferred, A21-1 and A21-3), or a single quarter ex-earnout only with the US deferred-tax credit stripped; never reported Q2 annualised (that would give 136.06).
- FLAG A21-3: Ex-earnout ETR is 25.09-25.90%, but Q2 ex-earnout ETR is 31.95% before the 14.48 Mn US deferred-tax credit (res L548-L551, L288). The credit is 9.2% of Q2 normalized PAT; without it, normalized PAT rose 18.0% YoY, not 25.85% (Step 4). The 17.33 Mn H1 FY26 subsidiary credit reversed as a 24.35 Mn H2 FY26 charge (res L550). A Q2-annualised A21 base carries 5.79 Cr of the credit; TTM nets it and is the cleaner base.

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

DEFERRED TO /fttcp AND ROLE 1 (operator ruling OR-30). No pillar values exist on file (ND). Pillar-relevant facts flagged:

| Pillar / Input | Original Assumption | Current Reading (flagged fact) | Action |
|---|---|---|---|
| ROCE Base | ND | H1 annualised operating ROCE 8.48% on closing equity + borrowings; 9.73% net of cash and bank (Step 6A). Operating EBIT margin H1 6.63%. | Deferred: FTTCP ROCE forward verdict |
| Cash Multiplier | ND | H1 CFO/PAT 0.29x cons (0.46x ex-earnout), 0.07x standalone; cash INDETERMINATE-WITH-DIRECTION (structural) | Deferred; flag below-band reading |
| Growth Visibility Premium | ND | Order book 2,813.7 Cr = 1.95 years of TTM revenue (1.79 years of Q2 run rate); book-to-bill 1.55-1.6x | Deferred |
| Strategic Premium | ND | Design-led / B2S share not disclosed; margin 8.69% vs the deck's 13-18% "B2S platform moat" stage (pres L165). Single-credit rule: no ROCE recovery credited here. | Deferred |
| UA Multiplier | ND | Not in filing. Notion memory: FII 0.24%, DII 29.19% (SECONDARY) | Deferred; qualifiers need evidence |
| Sector Cap | ND | Open operator ruling (no EMS row; Cables/Industrial 25x vs Defence 38x set by hand) | Deferred |
| Hurdle Ratio recheck | ND | TTM EPS 10.58 reported, 8.29 ex-earnout (7.97-8.61 across the Q3 FY26 one-off readings). At the Notion CMP of 979 (memory, 13-Oct-2026), trailing PE = 92.5x reported and 118.1x ex-earnout (113.7x-122.9x across the range) [arithmetic on a memory price] | Deferred to Role 1 |

---

## STEP 8: POSITION DECISION

Decision Status verified: NOT SET. No position. Branch: 8A-W (watchlist / non-held).

### 8A-W logic applied
- Any thesis-broken condition FIRED? No condition is signed. Nothing fires.
- Below bear / between bear and base / at or above base? Not assessable: projections ND.
- Output: there is no entry zone to update (none exists). Gate: Halt 1 remains the master gate; it is pending. This review adds three RED readings on the six named tests (2, 4 margin leg, 6 US leg) and one AMBER (1). Proposed Decision Status: none proposed. The operator sets it at Halt 1.
- Transition Decision Matrix inputs for the signed model (informational): proof gate NOT FIRED this quarter. The ugliness classification and the recognition gap are not signed. Note for Halt 1: the earnout-inflated reported PAT makes the trailing multiple look 22% lower than it is on operating earnings (92.5x vs 118.1x), so the recognition-gap test must run on ex-earnout EPS.

### 8B. Add-back / trim trigger refinement
- Original add-back trigger: ND (none on file).
- Revised add-back trigger (proposed for Halt 1): consolidated gross margin back at or above 40.05% (H2 FY26 average) for two consecutive quarters, AND US subsidiary ex-earnout PBT positive.
- Original trim ladder: ND (no position).
- Revised trim ladder: not applicable (no position).

### 8C. Single cleanest metric for Q3 FY27
Consolidated gross margin (revenue minus materials minus inventory change), read with the Box Build share and, as a co-reading, the combined employee plus other-expense ratio.
- Bull threshold: Q3 FY27 gross margin at or above 40.05% (the H2 FY26 average). That proves the Q2 mix effect was one-off, as management says (pres L374). (Role 5 addendum, loop 2: revised. "As management says" rests on the deck and the CEO's "some of these one-offs" (cc L231). On mix the chairman agrees (cc L283-L284): he called it a "this quarter thing". On PD purchases he undercuts the deck: product development "has been going on for a while" (cc L286), so repeat purchases are likely [INFERENCE]. His "it's not a one-off thing" (cc L291) refers to the S&M and PD investment drag on EBITDA margin, not to the material cost. See Role 5 Step 7A row 24.)
- Bear threshold: Q3 FY27 gross margin at or below 37.41% (the Q2 FY27 level) with Box Build share at or above 37%. That proves material intensity rises with the strategy itself (FN02 reading b). The 11-13% EXPAND target would then need a lever the deck does not name.
- Co-reading (A5 loop-1 N1): the consolidated combined opex ratio against the H2 FY26 average of 29.55% (Q1 FY27 27.47%, Q2 FY27 28.72%; res L538, L543, L546). Below 29.55% supports Step 4 reading (a): seasonal Q2 opex, so the YoY leverage recurs. At or above 29.55% supports reading (b): the YoY leverage was a Q2 FY26 base spike and is reversing. Gross margin alone cannot carry the Q3 test, because opex gave 125 of the 178 bps QoQ margin fall.
Why this metric: the margin leg of the proof gate, Notion test 2, and the EXPAND target all run through it. Cash (test 1) waits on a basis ruling; the order book (test 3) is already green.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to at least one question below (coverage list after the table). Ordered by thesis materiality. Q1-Q8 are the protocol's core 5-8 set.

| # | Cat | Question | Why It Matters | Bull Answer | Bear Answer | From finding(s) | ANSWER STATUS (Role 5 addendum; cc = concall fulltext line; machine transcript, speakers inferred) |
|---|---|---|---|---|---|---|---|
| 1 | E | What is the remaining earnout (contingent consideration) liability at 30-Sep-2026, in Rs Mn, after the Rs 181.95 Mn gain in Note 3(ii)? | The gain is 53.5% of Q2 PAT and recurs each Q2; a residual sets the next write-back or payout | Nil or small; the earnout window is closed | A residual large enough to allow another write-back in Q2 FY28 | A3-06, A3-16, FN05, FN-03 | NOT ADDRESSED. Reversal amount only (cc L133, L163, L173). A related recurrence question was ASKED (cc L462-L463); the answer omitted the earnout (cc L464-L465). See Q39 |
| 2 | A | By what % did the acquired US business miss the earnout metric that triggered the Rs 181.95 Mn write-back? | A miss is an Ind AS 36 impairment indicator for 117.89 Cr of goodwill and intangibles | Small miss on a timing metric | Large miss on revenue or EBITDA | A3-04, A3-06, FN05, FN-03 | NOT ADDRESSED |
| 3 | A | What was Cyient DLM Electronics Inc. (ex-Altek) EBITDA in Q2 FY27, in Rs Mn? Consolidated minus standalone EBITDA fell to Rs 11.51 Mn (1.17%) from Rs 57.43 Mn in Q1. | Separates the acquired unit from the other US subsidiary and from eliminations | Positive and near the Q1 level; the drop is an elimination effect | Negative; the acquired unit is loss-making | A3-05, A3-04, FN14 | EVADED. US revenue and margin outlook ASKED (cc L433-L436); reply "currently doing as per our plans", no figure (cc L437-L439); conflicts with the filing. A3 graded PARTIAL |
| 4 | C | Of the 381 bps YoY drop in consolidated gross margin (41.22% to 37.41%), how many bps came from component price inflation, and how many from Box Build mix? | Notion test 2 asks for a component-cost answer; the deck gives mix and product development, and its p11 opex cause conflicts with a 245 bps YoY opex ratio fall (QoQ it fits: opex gave 125 of the 178 bps fall) | Mostly one-off purchases; component cost flat | Mostly Box Build mix: structural to the strategy | FN01, FN02, FN03, A3-07, FN-01 | PARTIALLY (Role 5 addendum, loop 1: cell revised). The split was asked (cc L222-L223) and deflected: "a mix of various factors" (cc L225-L228; 4A grade D). The CFO gives the Q2 cause as "revenue mix and certain product development related costs" (cc L158). The CEO and the chairman scope the mix effect to this quarter and give sales and marketing as the full-year cause (cc L279-L285). PARTIALLY holds only because T039 gave a direction. No bps split; no component cost (CF03). (Role 5 addendum, loop 2: revised) The chairman also says product development "has been going on for a while" (cc L286), so repeat PD purchases are likely [INFERENCE], against the deck's "one-off" label on the PD-purchase leg (pres L374-L375). On mix he agrees with the deck: a "this quarter thing" (cc L283-L284). His "it's not a one-off thing" (cc L291) refers to the S&M and PD investment drag. The PD leg of the bull answer rests on the deck and cc L231 only; see Step 7A row 24 |
| 5 | B | The deck sets ~11-13% margins for FY27-29 (p7). Is that EBITDA margin, and in which fiscal year does management expect to enter the band, given H1 FY27 at 9.6%? | The only dated margin target; Role 5 promise-vs-delivery anchor | EBITDA; entry in FY28 with named levers | Undefined metric, or entry pushed to FY29 | FN04, FN17, FN-08 | PARTIALLY. Band restated as "margin framework", metric unnamed (cc L78, L86, L96). No entry year given. FY27 is guided at 9-10% (cc L244), below the band. FY28 is guided at a floor, "double digits" (cc L266) and "10 plus percent ... without even doing any further additional effort" (cc L476-L477), which neither puts FY28 in the band nor rules it out. FY28 is the earliest entry year (CF02). (Role 5 addendum, loop 1: corrects "entry not before FY29", which the call does not support) |
| 6 | D | What formula produces the deck's NWC of 153 days for Q2 FY27, and what does that formula give for FY26? | The cash falsifier (test 1) cannot score until the basis is fixed; Notion's 169 matches neither basis | A formula that reproduces 169 for FY26 | Notion's 169 is on a third basis; the test must be rebuilt | FN08, A3-08 | NOT ADDRESSED. 153 stated, no formula (cc L148) |
| 7 | F | Standalone took Rs 287.91 Mn of new short-term borrowings in H1 to fund a Rs 434.34 Mn inventory build. What peak balance of standalone short-term borrowings does the company plan by 31-Mar-2027? | Tests whether India growth now needs debt funding | Repaid by Q4 from collections | Rising further through H2 | A3-03, FN09 | NOT ADDRESSED |
| 8 | D | What share of the Rs 28,137 Mn order book carries customer advance terms today, against a year ago? Customer advance days fell from 33 to 13. | Separates growth-induced from structural WC | Advances return as new programmes mobilise | New orders carry no advances; WC per rupee of revenue rises | FN07, A3-10 | NOT ADDRESSED. QoQ advance days only, 15 to 13 (cc L149) |
| 9 | F | About Rs 278 Mn of US term debt moved to current in H1. Is the US facility due within 12 months, and will it be refinanced or repaid from India cash? | 12-month refinancing need on a loss-making unit | Refinanced on existing terms | Repaid from India cash; group net cash falls further | A3-08 | NOT ADDRESSED |
| 10 | F | Finance cost fell 10.4% YoY, which the deck credits to "lower working capital borrowings". What were consolidated borrowings at 30-Sep-2025, and which source funded the H1 FY27 working-capital increase of Rs 506.41 Mn while borrowings rose to Rs 1,319.60 Mn from Rs 1,061.25 Mn? | The deck's YoY cause cannot be tested: the 30-Sep-2025 balance is NOT FOUND. H1 FY26 repayments (992.96, 746.72 Mn) and a 33% fall in interest paid (143.09 to 95.86 Mn) fit it; the H1 FY27 build (gross borrowings +24.3%) points to higher finance cost from Q3 [INFERENCE] | Internal cash plus the standalone short-term line drawn in H1 (Rs 287.91 Mn), repaid from H2 collections; finance cost holds near Rs 61 Mn a quarter (Role 5 addendum: OI-1 corrected; the prior text "borrowings are US refinancing only" contradicted the filed standalone draw, res L565) | Debt; finance cost rises from Q3 | FN09, A3-03 | NOT ADDRESSED (Role 5 addendum, loop 1: regraded from PARTIALLY). The cited lines are CFO prepared remarks that restate the deck's YoY cause, "lower working capital borrowings" (cc L160, L179), which is the claim Q10 tests. No balance, no funding source, no new fact; the H1 build not mentioned (CF14) |
| 11 | D | Will the FY27 impairment test of the US cash-generating unit (goodwill Rs 730.94 Mn plus intangibles Rs 447.97 Mn) use the reduced earnout forecasts, and what headroom did the FY26 test show? | Two earnout write-backs vs rising goodwill (FX) | Large headroom on the reduced forecast | Thin headroom; impairment risk at Q4 FY27 | A3-06, FN05, FN-03 | NOT ADDRESSED |
| 12 | D | Define "operation free cash flow" of Rs 172 Mn (p12): is it CFO minus capex, before or after lease payments? | H1 consolidated CFO minus capex is only Rs 4.11 Mn; Q1 would then be about Rs (168) Mn on the same basis [INFERENCE] | CFO minus capex after leases | Excludes working capital or leases | FN10, FN-06 | NOT ADDRESSED. Figure restated, no definition (cc L149) |
| 13 | D | What was Q2 FY27 consolidated CFO alone, in Rs Mn? | Only H1 CFO (Rs 147.51 Mn) is filed; the "improvement" claim has no comparator | Q2 CFO above Rs 150 Mn | Q2 CFO near zero or negative | A3-08, FN-06 | NOT ADDRESSED |
| 14 | A | What share of the Rs 28,137 Mn order book is executable within 12 months? | "Strong revenue visibility" (pr L81) depends on it; the book is 1.95 years of TTM revenue | Above 60% | Below 40%, or framework/LTA values included | FN-05 | EVADED. ASKED (cc L451); refused: "we don't publish the numbers of what is for each year"; average 18-24 months (cc L452-L455) |
| 15 | A | The book walk implies Q2 FY27 intake of Rs 6,079 Mn (1.55x) vs a stated 1.6x, and Q2 FY26 intake of Rs 4,699 Mn, so YoY intake growth of +29.4% vs the stated +15.4% (pr L94). What were the Q2 FY26 and Q2 FY27 cancellations, FX revaluation and re-scoping, in Rs Mn? | Neither the stated ratio nor the stated YoY intake growth ties to the book; +15.4% needs Rs 568-751 Mn of undisclosed Q2 FY26 book reductions | Small FX revaluation only, or stated intake is on a different (gross) basis | Cancellations or de-scoping in the Q2 FY26 book | FN-05 | PARTIALLY. "600 crores plus" intake (cc L256) fits the walk; "over 1.6 times" restated (cc L36); no cancellations or FX (CF10) |
| 16 | E | What % of Q2 FY27 revenue came from B2S (design-led) work? | Proof gate share leg; the deck hides B2S inside "Others" | 10% or more | Low single digits | FN12, FN-08 | EVADED. ASKED with the prior FY27 double-digit target (cc L375-L376); reply gives no share (cc L382-L394) (CF07). See Q35 |
| 17 | B | How much of the Rs 28,137 Mn order book comes from semicap, robotics and AI data center combined? | The "+3 new" industries carry no revenue or order line; semicap is carved from "Industrial/Semicon" | A named, material order value | Nil or immaterial | FN13, FN-08 | PARTIALLY. Semicap revenue "in the last two quarters", unquantified (cc L238); AI DC and robotics "just started exploring" (cc L215, L460) (CF18). See Q40 |
| 18 | C | What is the Rs Mn value of "purchases towards product development" inside Q2 FY27 material cost? | Splits one-off cost from mix | A large one-off amount | A small amount; the drop is mix | FN02, FN-08 | EVADED. ASKED (cc L194-L195); refused: "we do not want to be putting a number" (cc L205, L208). (Role 5 addendum, loop 1) The chairman says product development "has been going on for a while" (cc L286), which undercuts the bull answer "a large one-off amount" [INFERENCE: repeat PD purchases are likely]. His "it's not a one-off thing" (cc L291) refers to the S&M and PD investment drag, not to the material cost (Role 5 addendum, loop 2); see Step 7A row 24 |
| 19 | B | Does any numeric FY27 revenue growth guidance stand? | "Positive on the outlook for the year" names no figure or year | A reaffirmed figure | No figure; earlier guidance withdrawn | FN-07 | ANSWERED. FY27 30-35% (analyst-offered, accepted, cc L353-L354); H2 above 30% (cc L361) (CF23) |
| 20 | D | What % of USD receivables was hedged at 30-Sep-2026? Net FX swung from Rs (20.55) Mn in Q1 to Rs 18.89 Mn in Q2 (standalone), and the cash-flow-hedge line is nil in FY27. | Undesignated FX flows into PBT; standalone PBT ex-FX is flat QoQ | A policy hedge ratio is in place | Unhedged; PBT carries FX volatility | A3-01, FN-02 | NOT ADDRESSED. Forex named only as an other-income item (cc L464) |
| 21 | D | The subsidiaries booked a Rs 14.48 Mn deferred-tax credit in Q2 on losses. What is the US unused tax-loss balance and its expiry? | DTA on a loss-making unit can reverse, as it did in H2 FY26 | Long-dated losses with a profit plan | Short-dated; reversal risk | A3-11 | NOT ADDRESSED |
| 22 | D | Which receivables produced the H1 standalone ECL write-back of Rs 30.53 Mn, and how much of it was booked in Q2? | 4.6% of standalone H1 EBITDA; line and quarter NOT FOUND | Specific recoveries, booked in Q1 | Model release booked in Q2 | A3-09 | NOT ADDRESSED |
| 23 | D | What share of contract assets (Rs 581.44 Mn, +32.7%) is unbilled for more than 90 days? | Over-time recognition vs slow billing | Under 10% | Over 25% | A3-10 | NOT ADDRESSED |
| 24 | A | Was the IP-communications investee re-valued at 30-Sep-2026, and on what product launch date does Note 4's recovery view rest? | FVOCI line nil in FY27 after Rs (207.16) Mn in FY26; the commitment is undated | Re-valued; launch dated | Not re-valued; launch undated | A3-02, A3-20, A3-21 | NOT ADDRESSED |
| 25 | G | Do any of the 2,63,400 options granted on 15-Oct-2026 go to KMP or the new CHRO, and at what exercise price? | Grant terms are unstated | None to KMP; market price | KMP grants at face value | A3-13 | NOT ADDRESSED |
| 26 | G | Consolidated Q2 FY26 employee cost prints Rs 329.42 Mn but the expense lines foot only at Rs 529.42 Mn. Will the company file a corrected statement? | Filing data integrity | Acknowledged misprint, corrected | No response | A3-14 | NOT ADDRESSED |
| 27 | G | What was the Rs 83.78 Mn inflow under "Payment towards acquisition of business" in H1 FY26? | An inflow under an acquisition line suggests a purchase-price refund [INFERENCE] | Working-capital true-up | Seller refund on missed performance | A3-18 | NOT ADDRESSED |
| 28 | G | What was the date of the Altek rename, and were the earnout terms amended at the same time? | The rename coincides with the second write-back | Rename after earnout close; terms unchanged | Terms amended with the rename | A3-19, FN14 | NOT ADDRESSED (Role 5 addendum, loop 1: regraded from PARTIALLY). The call restates the rename already in the deck and press release (cc L114, L437; pres L192; pr L103-L104). No date, no earnout terms (CF22) |
| 29 | A | Was the Rs 34 Mn one-off in Q3 FY26 EBITDA (p11) a charge inside filed operating costs that the deck adds back, or a gain booked outside operating EBITDA? Which filed line holds it? | Deck H2 FY26 PAT 362 Mn exceeds filed 336.74 Mn by 25.26 Mn, about the one-off after tax (25.44 Mn); the answer sets the TTM ex-earnout base at about 68.3 or 63.2 Cr | A one-off charge in filed costs; normalized base about 68.3 Cr | A gain in filed other income; normalized base about 63.2 Cr | FN11 | NOT ADDRESSED |
| 30 | A | What was Q2 FY27 revenue from Auto & Others, in Rs Mn, and its YoY change? By the p12 shares and growth rates, Aerospace and Industrial gave Rs 881.7-981.0 Mn of growth against a Rs 824.56 Mn total increase. | Revenue breadth: the other 22% of revenue shrank 6-15% in aggregate while Defence grew 13% and Med Tech 14%, so Auto & Others fell sharply [INFERENCE] | A small slice; one programme ended | A lost customer, or a structural exit from Auto | A5 loop-1 N2 (pres L334-L362; res L538) | NOT ADDRESSED. The CFO's mix omits Auto (cc L151-L152); "positive growth across all key segments" (cc L41) (CF17) |
| 31 | B | (Role 5 addendum) FY27 EBITDA margin guidance was "close to around 9%" and then "9% to 10%" (cc L230, L244). On 30-35% FY27 growth, 9% needs an H2 margin of about 8.5%, below Q2's 8.69%; 10% needs about 10.4%. Which end applies, and what holds H2 below Q2 if investment intensity falls from Q3 (cc L295)? | The first numeric margin guide; sets the margin-leg baseline | Top end; H2 above 10% as S&M absorbs | ~9%; H2 margin below Q2 | CF01 | NEW (Role 5 addendum; for the Q3 FY27 call) |
| 32 | C | (Role 5 addendum) Define "contribution margin" (cc L282-L283). What were the Q2 FY27 and Q2 FY26 values on that basis, and how do they reconcile with the filed 381 bps fall in gross margin? | The chairman's cause runs opposite to the filing and the deck | A defined measure that excludes pass-through material and rose YoY | Undefined, or the reconciliation shows material cost drove the fall | CF03 | NEW (Role 5 addendum) |
| 33 | C | (Role 5 addendum) What were sales and marketing costs (Rs Mn) in Q2 FY27 and Q2 FY26, and the product development cost expensed in Q2 FY27? The call sized the drag at 100-150 bps (cc L199), ~100 bps (cc L287) and 150-200 bps (cc L290). | Fixes the base for the S&M freeze (no net new S&M until quarterly revenue reaches about Rs 7,862 Mn) and for the FY28 recovery claim | A stated Rs base that stays flat QoQ | No base given; S&M rises QoQ | CF04, CF05 | NEW (Role 5 addendum) |
| 34 | B | (Role 5 addendum) The "around 200 basis points" margin expansion (cc L294) followed an audio gap: on what base, by which year? Does "from the Q1 onwards ... double-digit EBITDA margin" (cc L231) mean Q1 FY28? | Dates the first double-digit quarter | 200 bps on FY27 by FY28; Q1 FY28 double digit | Undated; Q1 FY28 below 10% | CF06, CF24 | NEW (Role 5 addendum) |
| 35 | E | (Role 5 addendum) Per an analyst, the Q3 and Q4 FY26 calls set B2S at a double-digit share of FY27 revenue (cc L375-L376). Is that target withdrawn? What was the B2S share of H1 FY27 revenue? | Proof-gate share leg; DROPPED-candidate status | Target restated with a date | Withdrawn; share low single digits | CF07 | NEW (Role 5 addendum) |
| 36 | E | (Role 5 addendum) Of the "close to $1 billion" across four B2S programmes (cc L309), what value is under signed contract today, and with which customers? | "the contracts have been signed" (cc L409) vs "few will be contract signed" (cc L427) | Majority signed; named customers | Minority signed; no names | CF08 | NEW (Role 5 addendum) |
| 37 | A | (Role 5 addendum, loop 1: revised) On what date was the $1.4 bn unweighted pipeline measured ("some time back", cc L331), and what is the weighted value of the ~$1.5 bn? The chairman put both figures on one unweighted basis, "1.5 which has increased" (cc L338-L339; T053, low confidence). The CEO said "we are also seeing some of the things going up" (cc L330); his "more than a billion" (cc L331) restates the opening floor (cc L33). | The chairman names the pipeline as the feeder to watch (cc L348) | 1.4 dated to the prior quarter; weighted value disclosed and rising | 1.4 older than one quarter, or the weighted value far below $1.5 bn; no date given | CF09 | NEW (Role 5 addendum) |
| 38 | D | (Role 5 addendum) Which component categories limit order book conversion, and what inventory-days and NWC-days targets, with dates, does management hold? | Material availability limits the H2 >30% pledge (cc L248-L251, L356); the cash falsifier has no management target | Named shortage clearing by Q4 FY27; a dated NWC target | No target; inventory at or above 162 days | CF11 | NEW (Role 5 addendum) |
| 39 | E | (Role 5 addendum) Asked whether Q2 other income recurs, the CFO named forex and export incentives (cc L464-L465). The deck states an earnout reversal in both Q2 FY26 and Q2 FY27 (pres L384-L385). Is a residual earnout open for Q2 FY28, and what was the export-incentive amount in Q2 FY27 (Rs Mn)? | The earnout is 80.5% of Q2 other income (181.95 / 226.15 Mn; loop 1 rounding fix); the "one-time" label conflicts with the deck | Earnout closed; no Q2 FY28 write-back | Residual open; a third Q2 write-back possible | CF12 | NEW (Role 5 addendum) |
| 40 | B | (Role 5 addendum) What semicap revenue (Rs Mn) was booked in Q1 and Q2 FY27 (cc L238), and what order book does semicap hold? | The only EXPAND leg with revenue; AI DC and robotics are "just started exploring" | A named, rising Rs figure | Immaterial; unquantified again | CF18 | NEW (Role 5 addendum) |
| 41 | D | (Role 5 addendum) Will product development stay fully expensed through FY28, and would any switch to capitalisation be disclosed with its EBITDA effect (cc L389-L391)? | The proof-gate margin leg uses reported EBITDA; the option to capitalise is retained | Policy fixed; any change disclosed with effect | A policy switch lifts reported EBITDA | CF20 | NEW (Role 5 addendum) |
| 42 | A | (Role 5 addendum) When does the Honeywell build-to-print programme return to serial production after the engineering changes (cc L404-L407)? | Anchor-customer revenue timing | Dated restart within FY27 | Undated; slips into FY28 | CF21 | NEW (Role 5 addendum) |

Coverage check (every FORWARD-SIGNAL / AMBIGUOUS finding has a question): results A3-01 (Q20), A3-02 (Q24), A3-03 (Q7, Q10), A3-04 (Q2, Q3), A3-05 (Q3), A3-06 (Q1, Q2, Q11), A3-07 (Q4), A3-08 (Q6, Q9, Q13), A3-09 (Q22), A3-10 (Q8, Q23), A3-11 (Q21), A3-13 (Q25), A3-14 (Q26), A3-16 (Q1), A3-18 (Q27), A3-19 (Q28), A3-20 (Q24), A3-21 (Q24). Presentation FN01 (Q4), FN02 (Q4, Q18), FN03 (Q4), FN04 (Q5), FN05 (Q1, Q2, Q11), FN07 (Q8), FN08 (Q6), FN09 (Q7, Q10), FN10 (Q12), FN11 (Q29), FN12 (Q16), FN13 (Q17), FN14 (Q3, Q28), FN17 (Q5). Press release FN-01 (Q4), FN-02 (Q20; partly answered from the filing in Step 4), FN-03 (Q1, Q2, Q11), FN-05 (Q14, Q15), FN-06 (Q12, Q13), FN-07 (Q19), FN-08 (Q5, Q16, Q17, Q18). NEUTRAL-FACT findings (A3-12, A3-15, A3-17, FN06, FN15, FN16, FN18, FN-04) are incorporated in the tables above; they need no question. Q30 comes from the A5 loop-1 counter N2, not from an A3 finding.

Coverage check, concall findings (Role 5 addendum): CF01 (Q31), CF02 (Q5), CF03 (Q32, Q4), CF04 (Q33, Q18), CF05 (Q33), CF06 (Q34), CF07 (Q35, Q16), CF08 (Q36), CF09 (Q37), CF10 (Q15), CF11 (Q38), CF12 (Q39, Q1), CF13 (Q2, Q3, Q11), CF14 (Q10), CF15 (Q8), CF16 (Q12, Q13), CF17 (Q30), CF18 (Q40, Q17), CF20 (Q41), CF21 (Q42), CF24 (Q34), CF25 (Q6). NEUTRAL-FACT CF19, CF22 and CF23 are incorporated in the Role 5 tables; CF23 also closes Q19. Answer-status tally on the 30 Role 4 questions (Role 5 addendum, loop 1: Q10 and Q28 regraded from PARTIALLY, because a restated fact with no new information grades NOT ADDRESSED, as at Q6, Q8 and Q12): ANSWERED 1 (Q19); PARTIALLY 4 (Q4, Q5, Q15, Q17); EVADED 4 (Q3, Q14, Q16, Q18); NOT ADDRESSED 21 (Q1, Q2, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30). Differences from the A3 silence audit: A3 graded Q3 PARTIAL; this review grades it EVADED, because the US question was asked (cc L433-L436) and got no figure. A3 "DECLINED" (Q14, Q18) maps to EVADED. Caveat: the Role 4 questions were drafted after the call and were never put to management, so NOT ADDRESSED on an unasked question is weak evidence. OI-1 corrected (Role 5 addendum): the Q10 bull answer "Internal cash; borrowings are US refinancing only" contradicted the filed standalone short-term draw of Rs 287.91 Mn (res L565); the corrected text is in the Q10 row.

Top 3 by likelihood of thesis-changing information:
- Q4 (gross margin split): a "mostly Box Build mix" answer moves weight to the bear case; it says the strategy itself compresses margin.
- Q2 (earnout miss size): a large miss confirms the bear case on the US arm and points to a Q4 FY27 impairment.
- Q6 (NWC formula): tests transparency. A precise formula that reproduces FY26 is a good sign. A vague answer is itself diagnostic.

Channel recommendation: the 15-Oct-2026 concall has already occurred. Its transcript is not in this run. First run Role 5 on the transcript and mark each question ANSWERED / PARTIALLY / EVADED / NOT ADDRESSED. Send the remainder by IR email with the questions verbatim. (Role 5 addendum: Role 5 has now run; answer status is in the last column. Send the 21 NOT ADDRESSED (Role 5 addendum, loop 1 count) and 4 EVADED questions, plus Q31-Q42, by IR email before the Q3 FY27 call.)

---

## STEP 9: NOTION PAYLOAD (for the run's operator-approval write gate; Decision Status never written)

- Decision Status: NOT written. No change proposed (NOT SET; Halt 1 pending).
- Row properties to update: none proposed.
- Key Notes prepend (proposed): "2026-10-17 | Q2 FY27 pre-thesis read: revenue +26.5% YoY; op EBITDA margin 8.69% (-135 bps); gross margin 37.41% (-381 bps, third compression on Notion count); 53.5% of PAT is an earnout write-back; US arm loss-making ex-earnout; cash INDETERMINATE (structural lean); verdict PROCEED WITH FLAGS"
- Page append: this full review (complete tables) under "## Q2 FY27 Results Review - 2026-10-17". Catalyst status: DELAYED. Thesis status: not applicable (pre-thesis). Source: BSE/NSE filings 15-Oct-2026 (results, investor presentation, press release). Auditor opinion: Unmodified (limited review). Business type: Standard.
- Tracker payload: four candidate signals in 5.5C (not written).

---

## MONITORABLES / CATALYST LIST (seeded by A3 F6 registers and F13 board items)

| # | Item | Implied date | Source ref |
|---|---|---|---|
| 1 | Role 5 on the Q2 FY27 earnings call transcript (questions answer-status) (Role 5 addendum: DONE 2026-10-18; see the ROLE 5 section) | now (call held 15-Oct-2026; transcript not in run) | Orchestrator note; Step 8.5 |
| 2 | Operator ruling: NWC basis and whether the H1 print counts for the cash falsifier | Halt 1 (date ND) | Notion open rulings; FN08, A3-08 |
| 3 | Q3 FY27 results: consolidated gross margin vs 40.05% / 37.41% thresholds; combined opex ratio vs H2 FY26 29.55%; subsidiary EBITDA; standalone borrowings | about mid-Jan 2027 [INFERENCE from the Jul and Oct board cadence] | Step 8C; Step 4; A3-03, A3-05, A3-07 |
| 4 | EXPAND stage margins ~11-13% | FY27-FY29 | pres L150, L165 (FN17 register) |
| 5 | Go from 4 to 7 industries (semicap, robotics, AI data center) | FY27-FY29 | pres L153-161 (FN17 register) |
| 6 | TRANSFORM stage margins ~13-18% (B2S platform moat) | FY30+ (outside window) | pres L165 (FN17 register) |
| 7 | "Positive on the outlook for the year" (no figure) | FY27, 31-Mar-2027 | pr L107 (FN-07 register) |
| 8 | ICRA AA- Stable annual surveillance | about Mar 2027 [INFERENCE: one year after 16-Mar-2026, Notion memory] | Notion properties (AGENCY) |
| 9 | Q4 FY27 / FY27 audited results: formal cash-falsifier print; US CGU goodwill impairment test; standalone short-term debt at 31-Mar-27 | about late Apr to May 2027 [INFERENCE] | A3-06, FN05, Notion test 1 |
| 10 | FY27 Annual Report: related-party flow to Cyient Ltd; US entity financials (AOC-1); earnout residual; DTA on US losses | about Jun to Jul 2027 [INFERENCE] | Notion test 5; A3-06, A3-11 |
| 11 | US subsidiary current borrowings 671.80 Mn: refinance or repay | within 12 months of 30-Sep-2026 (by Sep 2027) | res L177, L170 (A3-08) |
| 12 | Q1 FY28 results: entry into the 11-13% band; new-vertical revenue | about late Jul 2027 [INFERENCE] | FN17, FN13 |
| 13 | IP-communications investee value to improve as products launch | "over the next few years" (undated) | res L291 (A3-20 register) |
| 14 | ESOP/RSU grants (273,400 units): vesting and exercise price disclosure | granted 15-Oct-2026; vesting NOT FOUND | res L42-43 (A3-13 register) |
| 15 | CHRO Sandip Mishra appointment | effective 15-Oct-2026; term NOT FOUND | res L39-40, L486-487 (A3 register) |
| 16 | Altek integration and rename | completed by Q2 FY27 (done) | pres L192; pr L103-104 |
| 17 | Q2 FY28 base effect: Q2 FY27 reported PAT carries an 18.20 earnout | about Oct 2027 (just outside window) | FN05 |
| 18 | (Role 5 addendum, loop 1: revised) H2 FY27 revenue >= 874.15 Cr (30% on H2 FY26 672.42 Cr), about 437 Cr a quarter. Q3 FY26 (303.3 Cr, pres L249) holds the only QoQ decline in Step 3 (-2.36%) and is the weaker of the two H2 bases, so the Q3 30% bar of 394.29 Cr is only +0.3% QoQ on Q2's 393.09 Cr. A Q3 at the bar leaves Q4 needing 479.86 Cr (+21.7% QoQ, the same QoQ step Q4 FY26 made, Step 3; +30.0% YoY on Q4 FY26 369.1 Cr, pres L247) (Role 5 addendum, loop 2). Restate the Q4 requirement after Q3 prints | Q3: about mid-Jan 2027; Q4: about Apr-May 2027 [INFERENCE] | cc L361; res L538; pres L247-L249 (P09, CF23) |
| 19 | (Role 5 addendum) Order intake "600 crores plus" in Q3 and in Q4 FY27 (book walk >= Rs 6,000 Mn each). (Role 5 addendum, loop 2) Hedged: "probably you will be expecting it" (cc L256); walk intake reached 600 Cr once in five quarters; the guide needs H2 intake about 50% above H2 FY26 797.9 Cr [INFERENCE] (P10) | Q3 FY27 (mid-Jan 2027); Q4 FY27 (Apr-May 2027) [INFERENCE] | cc L256 (P10, CF10) |
| 20 | (Role 5 addendum) Investment intensity lower: combined employee plus other-expense ratio below Q2's 28.72%. (Role 5 addendum, loop 2) Absolute co-reading: combined employee plus other expenses vs Q2 FY27 1,128.89 Mn (res L543, L546). At about 437 Cr a quarter the ratio stays below 28.72% with expenses up to about 1,255 Mn (+11.2% QoQ) [INFERENCE], so a ratio pass alone re-credits P09 and does not test "There will not be any future investment in that area" (cc L297) | Q3 or Q4 FY27 | cc L295 (P07, CF04) |
| 21 | (Role 5 addendum) No net new S&M cost until quarterly revenue reaches about Rs 7,862 Mn (2x Q2) | every quarter, open-ended | cc L288, L297 (P06, CF05) |
| 22 | (Role 5 addendum) FY27 EBITDA margin 9-10% ("close to around 9%"); at 9% H2 runs about 8.5% [INFERENCE] | Q4 FY27 / FY27 results, about Apr-May 2027 [INFERENCE] | cc L230, L244 (P01, CF01) |
| 23 | (Role 5 addendum) AI data centre and robotics update: position, opportunities, pipeline | Q4 FY27 call, about Apr-May 2027 [INFERENCE] | cc L217, L460-L461 (P15, CF18) |
| 24 | (Role 5 addendum) Semicap growth "every quarter" (amount not disclosed) | from Q3 FY27 | cc L238, L459 (P16, CF18) |
| 25 | (Role 5 addendum) Double-digit EBITDA margin "from the Q1 onwards" (read Q1 FY28) | about late Jul 2027 [INFERENCE] | cc L231 (P03, CF24) |
| 26 | (Role 5 addendum) FY28 EBITDA margin double digits / "10 plus" from backlog alone | FY28 (outside window; Q1 FY28 first read) | cc L266, L476 (P02, CF02) |
| 27 | (Role 5 addendum) B2S: four programmes ~$1 bn enter the order book after design and prototype testing; production FY29, full ramp FY30 | undated / FY29-FY30 (outside window) | cc L309-L310, L409-L411, L428-L429 (P13, P14, CF07, CF08) |
| 28 | (Role 5 addendum) Honeywell build-to-print programme back to serial production | undated | cc L405-L407 (P21, CF21) |
| 29 | (Role 5 addendum) Product development stays fully expensed; any capitalisation is a tripwire | ongoing | cc L199, L389-L391, L473 (P22, CF20) |
| 30 | (Role 5 addendum) Pipeline $1.5 bn unweighted; win ratio ~40%; $400-500 Mn order impact | undated | cc L262, L332, L338 (P12, CF09) |
| 31 | (Role 5 addendum) More US revenue traction; large orders from the new sales team | undated | cc L439, L478-L479 (P18, P20, CF13) |
| 32 | (Role 5 addendum) Growth sustains into FY28 | FY28 | cc L56, L298-L299 (P24) |

---

## PROTOCOL VERDICT

PROCEED WITH FLAGS.
Reasons: the filing is clean (unmodified limited review) and every table is filled or ND, so the review is complete. Cash conversion is INDETERMINATE-WITH-DIRECTION (structural), which caps the verdict below PROCEED; the missing evidence is named in Step 5C. Material flags surface for the operator: earnings quality (earnout 53.5% of PAT), the US arm loss ex-earnout, a third gross-margin compression on Notion's count, the proof-gate margin leg moving the wrong way, new debt at both entities, and four filing or pipeline data defects. None is a mechanical failure, so REWORK does not apply.

(Role 5 addendum, 2026-10-18) Role 5 does not change the verdict. It stays PROCEED WITH FLAGS. The call adds no mechanical failure: all 97 turns and 303 rows reconcile, and every Role 5 table cell is anchored or ND. Cash conversion stays INDETERMINATE-WITH-DIRECTION (structural). The call gave no CFO figure, no NWC formula and no target, so the cap holds. The protocol override "concall narrative contradicts filing numbers materially" fires on three points: the margin cause, the earnout recurrence and the US arm. The filing is trusted, the credibility issue is noted for Halt 1, and the next-quarter watchlist is tightened (Monitorables 18-32). The credibility ratio and the archetype are ND because this call opens the promise log. Source caveat: machine transcript, inferred speakers; the filing wins on any number conflict.

---

## ROLE 5: CONCALL ANALYSIS (Q2 FY27 call, 15-Oct-2026; machine transcript)

(Role 5 addendum, 2026-10-18.) Protocol loaded: Quarterly Concall Analysis Protocol v1.1 (Role 5). Role 4 above is final; its tables and numbers are unchanged except passages marked "(Role 5 addendum)". Correction loop 1 (A5 Role 5 audit INCOMPLETE, 2026-10-18): run-1 findings F1-F4, C1-C3, M1, M2, M3a, M3b applied in place, marked "loop 1". Correction loop 2 (A5 loop-1 re-audit INCOMPLETE, 2026-10-18): L1-C1, L1-C2, L1-M1, L1-M2, L1-M3 and style LS1-LS6 applied in place, marked "loop 2". Figures re-verified against cc L199, L256-L257, L283-L297, res L538-L546 and pres L247-L249, L289-L294. No Role 4 number changed. Run-1 S2 (brief length) not applied.
Inputs: A1 concall structured (R001-R303, T001-T097) and fulltext (488 lines); A2 concall ledger; A3 concall forensics (CF01-CF25); filing extracts for Step 7 (res, pres, pr); Notion orchestrator copy (work/notion-thesis.md). No source PDF, audio file or inputs/ file was opened.
Anchor convention: "cc L###" = concall fulltext line; T### = A1 concall turn; R### in this section = A1 concall structured row. Filing anchors (res, pres, pr) and Step references point to the Role 4 sections above.
SOURCE CAVEAT (binds every concall-derived statement in this section and in every "(Role 5 addendum)" passage): the source is a faster-whisper MACHINE transcript, not an official transcript (cc L4, L20). Speakers are INFERRED by A1 from T009 onward, except T096. Numbers and names may be misheard. On any number conflict the filing wins.

### LEDGER RECONCILIATION PREAMBLE (concall, contractual)

Ledger contains 0 notes / 97 turns / 0 slides. All 97 turns reviewed, and all 303 ledger rows (R001-R303). Findings incorporated: [CF01, CF02, CF03, CF04, CF05, CF06, CF07, CF08, CF09, CF10, CF11, CF12, CF13, CF14, CF15, CF16, CF17, CF18, CF19, CF20, CF21, CF22, CF23, CF24, CF25].

| Ledger | Rows in structured | Rows referenced by A2 | Orphans | A2 gate | A3 reconciled | Reviewed by A4 |
|---|---|---|---|---|---|---|
| Concall (ledger_concall) | 303 (R001-R303) | 303 | 0 | pass | 100% (301 of 303 verbatim at cited line; 2 anchor defects, no value change) | all 97 turns (T001-T097), 10 question slots, 26 question turns, 303 rows |

Pipeline notes carried (none blocks the run):
1. R294 anchor defect: "we don't publish the numbers of what is for each year" is at cc L454 (T088), not L450 (T086). This section cites L454.
2. R177 cross-reference: "BLM Electronics Inc" is at cc L437 (R196), not L413.
3. A1 turn-table cue column uses source-file line numbers; the turn line ranges are correct (hygiene only).
4. Spoken variances kept verbatim: earnout reversal 182 (cc L133, L142, L163) vs 183 (cc L173); Box Build growth 86% (cc L111) vs 85% (cc L153). The filing governs: 181.95 Mn (res L288); the deck gives 86% (pres L359).
5. Audio gap 00:40:00-00:40:30 (cc L293-L294): the "200 basis points" statement has lost its base and year (CF06).
6. "Modila Loswal" (cc L364) and "EBITOL" (cc L399) are machine text; firm and customer names are unverified.
No unreviewed row exists, so Role 5 proceeds.

### STEP 0: PRE-FLIGHT

#### 0A. Notion page

| Item | Reading |
|---|---|
| Decision Status | NOT SET (verified before any framing). PRE-THESIS READ; Halt 1 pending; mental model unsigned. |
| Growth triggers | None signed. The Role 4 Step 6D trigger list is used. |
| Thesis-broken conditions | ND (none signed) |
| Monitoring checklist | The six named Q2 tests (Role 4 Step 6B) |
| Promoter Verdict / Management Grade | TRUSTWORTHY-with-flags / ND (no grade on page) |
| Devil's Advocate findings | ND |
| Previous concall log | ND ("Prior concall promise log: ND"; prior transcript not passed). First concall under the protocol for this company: the promise log starts with this call. |
| Prior-call phrases in Notion memory (SECONDARY) | April call: gross margin fall "a couple of basis points"; July call: "investments made into the organisation" (an opex cause); FY27 double-digit design-led target "silently dropped" (Phase 2, 11-Sep-2026); Q1 FY27 book about Rs 2,600 Cr, book-to-bill 1.5x |

#### 0B. Participants

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | ND (moderator addressed as "Darwin", cc L28; no broker named) | Independence not assessable |
| CMD / Chairman | Krishna Bodanapu, non-executive chairman (cc L28) | Present. Promoter is the listed parent Cyient Ltd, 52.11% (Notion). His parent-side role is NOT FOUND in the run's documents. |
| Managing Director and CEO | Rajendra Velagapudi (cc L29) | Present |
| CEO (if different) | same as MD | n/a |
| CFO | R.M. Subramanian (cc L29) | Present |
| COO / Other senior | None on the call. A new Chief Growth Officer is named only on the call (cc L289, name machine text "in Rama"); sales leadership "strengthened" (cc L42) | New senior hire not in the filing board items (the filing names only the CHRO, res L39-L40) |
| IR Advisor | ND | |

Yellow flags: no promoter-absence flag. Notes: (a) the non-executive chairman answered the central margin question (T039, inferred) and the pipeline question (T053, low confidence). His full-year cause (sales and marketing) differs in weight from the CFO's Q2 cause (mix and product development); he and the CEO scope the mix effect to Q2 (cc L279-L284), so this is not a contradiction (Role 5 addendum, loop 1). His claim that gross margin is higher YoY does contradict the filing (Step 7A row 4) (CF03); (b) the CFO answered order-book execution (T088, inferred), a mild yellow flag; (c) a new senior hire (CGO) appears without a filing disclosure.

#### 0C. Structure and date

| Item | Reading |
|---|---|
| Call date | 15-Oct-2026 (cc L19), same day as board approval of results (res L268-L273): same day = canned |
| Quarter | Q2 FY27 (cc L24) |
| Duration | 61:14 (cc L488) |
| Prepared remarks | 00:00-26:20 (cc L24-L185): 1,580 s = 43.0% |
| Q&A | 26:20-59:27 (cc L186-L470): 1,987 s = 54.1%; by turns T005-T097 = 93 of 97 (A2) |
| Close | 59:27-61:14 (cc L470-L488): 107 s = 2.9% |
| Analyst slots / analysts who asked | 10 / 8 (Meeth Jain no response, cc L268-L270; Suman Kumar dropped, cc L364-L369); 26 question turns (A2) |
| Queue control | Two-question limit imposed at cc L320 |

#### 0D. Safe harbour
cc L30-L31: generic "risks and uncertainties", with a pointer to the website disclaimer. Narrow. Prior caveats: ND. The chairman names supply chain shortages, longer lead times, geopolitical uncertainty and the memory market (cc L39) as context, not as a caveat.

#### 0E. Business type
Standard operating business (EMS). Step 2 metric set applies; Step 2L not used.

Checkpoint: Notion verified (NOT SET), participants listed, structure noted, caveats logged, business type standard.

---

### STEP 1: OPENING REMARKS CLAIMS INVENTORY (T002-T004, cc L28-L184)

| # | Claim | Type | Quantified? | Source Line |
|---|---|---|---|---|
| 1 | Order backlog Rs 2,813 Cr | Customer/Order | YES | cc L33 |
| 2 | Pipeline "in excess of a billion dollars" | Customer/Order | YES | cc L33 |
| 3 | Positive order book momentum six continuous quarters | Backward | YES | cc L35 |
| 4 | Q2 book-to-bill "over 1.6 times" | Customer/Order | YES | cc L36 |
| 5 | Previous record order book surpassed | Customer/Order | YES | cc L37 |
| 6 | Execution despite supply chain shortages, memory market | Macro/Tailwind | NO | cc L39 |
| 7 | Revenue growth "more than 26%", "broadly in line with our expectations" | Backward | YES | cc L40 |
| 8 | "positive growth across all key segments" | Backward | NO | cc L41 |
| 9 | Sales leadership team strengthened | Operational | NO | cc L42 |
| 10 | Deliberate investments in sales and B2S; near-term margin impact | Strategic | NO | cc L45-L47 |
| 11 | B2S: engineering upfront, IP owned with customers, long manufacturing responsibility | Strategic | NO | cc L49 |
| 12 | Investments "starting to show some very good results" | Forward Soft | NO | cc L50 |
| 13 | Profitable growth, sustainable margin improvement medium to long term | Forward Soft | NO | cc L51 |
| 14 | "very strong and favourable demand environment" | Macro/Tailwind | NO | cc L52 |
| 15 | Design-led model "unique" to Cyient DLM | Strategic | NO | cc L53 |
| 16 | H1 FY27 revenue growth "more than 30%" | Backward | YES | cc L54 |
| 17 | Growth sustains "through the rest of the year and into next year" | Forward Soft | NO | cc L56 |
| 18 | Global EMS ~650 bn to ~1.1 tn | Macro/Tailwind | YES | cc L62 |
| 19 | High-reliability EMS ~$230 bn | Macro/Tailwind | YES | cc L63 |
| 20 | AI and data centre addressable EMS ~$58 bn | Macro/Tailwind | YES | cc L69 |
| 21 | Four core industries incl. automotive (EV) | Strategic | NO | cc L76 |
| 22 | STRENGTHEN margin framework ~9-11% | Forward Guidance | YES | cc L78 |
| 23 | EXPAND FY27-FY29: four to seven industries | Forward Guidance | YES | cc L82-L84 |
| 24 | EXPAND margin framework ~11-13% | Forward Guidance | YES | cc L86 |
| 25 | TRANSFORM from FY30: product and platform moat | Strategic | YES | cc L88-L89 |
| 26 | B2S renamed "Electronic Products" | Strategic | YES | cc L91 |
| 27 | "several multi-million dollar opportunities" | Customer/Order | NO | cc L93 |
| 28 | B2S "significant sustained growth from FY30 onward" | Forward Guidance | YES | cc L94 |
| 29 | TRANSFORM margin framework ~13-18% | Forward Guidance | YES | cc L96 |
| 30 | FY27 margins "at the higher end of the single-digit range" | Forward Guidance | YES | cc L103 |
| 31 | Order book all-time high; book-to-bill 1.6x | Customer/Order | YES | cc L106 |
| 32 | Q2 revenue +26.5% YoY | Backward | YES | cc L108 |
| 33 | H1 revenue +30% YoY | Backward | YES | cc L109 |
| 34 | Box Build revenue +86% YoY | Backward | YES | cc L111 |
| 35 | Three new logos | Customer/Order | YES | cc L113 |
| 36 | Altec integration completed; renamed | Operational | YES | cc L114 |
| 37 | Investing in AI DC, robotics, semicap | Strategic | NO | cc L116-L117 |
| 38 | Revenue Rs 3,931 Mn, +26.5% | Backward | YES | cc L126, L137 |
| 39 | Order book Rs 28.1 bn, +Rs 2.1 bn QoQ | Customer/Order | YES | cc L127, L148 |
| 40 | EBITDA Rs 342 Mn, +9.5%, margin 8.7%, -135 bps | Backward | YES | cc L129-L130, L157 |
| 41 | Normalized PAT Rs 158 Mn, +25.8%, "broadly keeping pace with our revenue growth", margin stable 4% | Backward | YES | cc L131, L141, L164 |
| 42 | Reported PAT Rs 340 Mn; "one-time reversal" of earnout Rs 182 Mn | Backward | YES | cc L132-L133, L142, L163 |
| 43 | Margin moderation from investment in sales, strategy, new growth areas | Backward | NO | cc L130, L139 |
| 44 | "underlying profitability remained healthy" | Backward | NO | cc L140, L165 |
| 45 | NWC 153 days from 161; inventory 162 stable; DSO 77 to 73 | Backward | YES | cc L148 |
| 46 | Customer advances 13 days vs 15 | Backward | YES | cc L149 |
| 47 | Operating free cash flow Rs 172 Mn in Q2 | Backward | YES | cc L149 |
| 48 | Focus on inventory optimisation and collections | Forward Soft | NO | cc L150 |
| 49 | Industry mix: aerospace 47% (+62%), industrial 31% (+29%), defence 7% (+13%), Med Tech 14% (+14%). (Role 5 addendum, loop 1) These shares assign the deck's p12 slices and fix the Role 4 Step 2C range at its upper end: Aerospace plus Industrial gave 981.0 Mn, 119.0% of the 824.56 Mn rise; Aerospace alone 707.1 Mn, 85.8%; the other 22% fell 15.3% (1,021.3 to 864.8 Mn). With +/-0.5 pp share rounding: 969-993 Mn (118-120%) and -14% to -17% [INFERENCE; res L538]. Role 4 numbers unchanged | Backward | YES | cc L151-L152 |
| 50 | Product mix: PCBA 48% (+19%); Box Build 37% (+85%) | Backward | YES | cc L153 |
| 51 | RoW 93%, India 7% | Backward | YES | cc L154 |
| 52 | Margin causes: "revenue mix and certain product development related costs"; employee cost for sales | Backward | NO | cc L158-L159 |
| 53 | Finance cost -10.4% to Rs 61 Mn on "lower working capital borrowings" | Backward | YES | cc L160 |
| 54 | PBT Rs 393 Mn; PAT Rs 340 Mn | Backward | YES | cc L161 |
| 55 | H1 revenue Rs 7,669 Mn, +30.2% | Backward | YES | cc L168 |
| 56 | H1 EBITDA Rs 733 Mn, +30.4%; margin "stable at 9.6%" | Backward | YES | cc L169-L170 |
| 57 | H1 normalized PAT Rs 321 Mn, +60.4%; margin +79 bps to 4.2% | Backward | YES | cc L171 |
| 58 | H1 reported PAT Rs 503 Mn, +27% | Backward | YES | cc L172 |
| 59 | Order book +Rs 5.2 bn YoY | Customer/Order | YES | cc L174 |
| 60 | H1 finance cost -21% YoY | Backward | YES | cc L179 |
| 61 | H2 priorities: intake, execution, margin, WC efficiency | Forward Soft | NO | cc L182 |

Type count: Backward 27, Customer/Order 9, Strategic 7, Forward Guidance 6, Forward Soft 5, Macro/Tailwind 5, Operational 2. Total 61.

Diagnostics:
- Quantified share: 43 of 61 (70.5%). Forward claims (Guidance + Soft): 11, of which 6 quantified (54.5%). Five of the six quantified forward claims are multi-year "margin framework" bands or phase dates (cc L78-L96); the "margin framework" metric is never named as EBITDA. One is the FY27 margin guide (cc L103).
- New vs reaffirmed: prior transcript ND. Against Notion memory, the order book and book-to-bill are reaffirmed and raised (Q1: about Rs 2,600 Cr, 1.5x). The FY27 margin guide is new against this quarter's deck and press release, which gave no figure (FN-07). The three-phase framework repeats the deck (pres L150-L165).
- Quietly dropped: the FY27 double-digit B2S (design-led) share target. It is absent from the opening; the opening dates B2S growth "from FY30 onward" (cc L94). An analyst raised the target in Q&A (cc L375-L376) and got no answer (CF07). Notion memory already logs it as silently dropped. Status: DROPPED candidate, unverified (prior log not passed); not scored.
- Internal contradictions: (a) "positive growth across all key segments" (cc L41) vs automotive named a core industry (cc L76) but missing from the CFO's mix (cc L151-L152); the deck shows a 1% slice (pres L334) and Role 4 Step 2C infers Auto & Others fell sharply; (b) "one-time reversal" (cc L133, L163) vs the company's own deck: "one-off Earnout reversal in both Q2 FY26 and Q2 FY27 (INR 196M and INR 182M respectively)" (pres L384-L385); (c) "very strong and favourable demand environment" (cc L52) vs "continued supply chain shortages" (cc L39); (d) withdrawn (Role 5 addendum, loop 1): the CFO's Q2 cause, "revenue mix and certain product development related costs" (cc L158), and the chairman's "it's not the revenue mix" (cc L284) differ in scope, not in fact. The CEO and the chairman both tie the mix effect to this quarter (cc L279, L283-L284). The chairman's gross-margin claim against the filing stays in Step 7A row 4.

---

### STEP 2: FORWARD GUIDANCE

"Last Quarter" and "Two Quarters Ago" are ND (prior log not passed) in every row; Notion memory is noted where it exists.

| Metric | This Quarter's Guidance | Last Quarter's Guidance | Two Quarters Ago | Trajectory | Confidence Level |
|---|---|---|---|---|---|
| Revenue growth (FY27) | 30-35%, analyst-offered and accepted: "probably yes ... 30-35% growth" (cc L353-L354); H2 FY27 "definitely" above 30% (cc L361); material-dependent (cc L356) | ND (prior log not passed); Notion: no numeric guide | ND | New | MEDIUM |
| Revenue growth (FY28) | "growth will continue in FY28" (cc L298-L299); "sustaining ... into next year" (cc L56); no figure | ND | ND | New | LOW |
| EBITDA margin band (FY27) | "higher end of the single-digit range" (cc L103); "close to around 9% EBITDA margin" (cc L230); "9% to 10% range" (cc L244, L266) | ND; deck "today" band ~9-11% (pres L165) | ND | New; widened within the call (~9% to 9-10%) | MEDIUM |
| EBITDA margin band (FY28) | "double digits" (cc L266); "10 plus percent" from backlog execution "without even doing any further additional effort" (cc L476-L477) | ND | ND | New | MEDIUM |
| EBITDA margin (quarter) | "from the Q1 onwards ... double-digit EBITDA margin" (cc L231). Q1 FY27 already printed 10.48% (Step 1A), so read as Q1 FY28 [INFERENCE] | ND | ND | New | LOW (period unclear, CF24) |
| Margin framework bands | STRENGTHEN ~9-11% (cc L78); EXPAND FY27-FY29 ~11-13% (cc L86); TRANSFORM FY30+ ~13-18% (cc L96); metric unnamed | ND; deck same bands (pres L165) | ND | Maintained vs deck | LOW |
| Margin expansion | "around 200 basis points" (cc L294); base and year lost in a 30-second audio gap (cc L293) | ND | ND | New | LOW (CF06) |
| Order book / pipeline | Book Rs 2,813 Cr (cc L33) / Rs 28.1 bn (cc L127). Pipeline "in excess of a billion dollars" (cc L33); "1.5 billion dollars roughly ... unweighted", with the 1.4 "previously" also unweighted, "1.5 which has increased" (cc L338-L339; T053, low confidence). The CEO: "we are also seeing some of the things going up" (cc L330); "close here on 1.4 ... Now ... more than a billion" (cc L331) restates the opening floor (Role 5 addendum, loop 1). Win ratio ~40% (cc L262-L264). "$400 to 500 million" order impact from the existing pipeline (cc L332-L333). Intake: "this quarter is close to 600 crores plus, that's where probably you will be expecting it for the next two quarters too" (cc L256). Hedged ("probably"), and the first reply to a win-ratio question that the analyst rejected (cc L257) (Role 5 addendum, loop 2) | ND; Notion Q1: book about Rs 2,600 Cr, 1.5x | ND | Raised (book); pipeline rose to ~$1.5 bn from $1.4 bn unweighted, date of the 1.4 figure ND (CF09; Role 5 addendum, loop 1) | MEDIUM |
| Capex envelope | ND (not discussed) | ND | ND | ND | ND |
| Utilization target / timeline | ND (not discussed) | ND | ND | ND | ND |
| Strategic order execution timeline | Book executes in 18-24 months on average; "very few" beyond two years (cc L236-L237, L452-L455); year split "we don't publish" (cc L454). B2S: four programmes, "close to $1 billion", outside the order book, 7-9 years (cc L309, L431); production "FY29 probably", full ramp "FY30 onwards" (cc L428-L429); earlier in the same call "By FY30" (cc L308), "from FY30 onwards" (cc L317), "from FY 29" (cc L411) | ND; analyst recall: B2S double-digit share in FY27 (cc L376, unverified) | ND | New; later than the analyst-recalled target | LOW-MEDIUM |
| Working capital / CCC band | No target. "inventory optimization and collections will remain an important area of focus" (cc L150) | ND | ND | ND | LOW |
| Net debt trajectory | Not guided. Finance cost fall credited to "lower working capital borrowings" (cc L160, L179), a backward claim | ND | ND | ND | ND |
| Export / segment guidance | Semicap: revenue "in the last two quarters" (cc L238); "growth every quarter" from now (cc L459). Exports continue; "a little growth in that India market" (cc L445). US division: "some more traction on the revenue" (cc L439) | ND | ND | New | LOW |
| New product / contract milestones | AI DC and robotics "just started exploring"; update "by the end of this financial year" (cc L215-L217, L460-L461). Honeywell build-to-print programme back to serial production, no date (cc L404-L407). B2S: "the contracts have been signed" (cc L409) vs "few ... contract signed and few will be contract signed" (cc L427) | ND | ND | New | LOW |
| Opex / cost (added row) | "We will not add any more sales and marketing costs till we at least hit about, or at least net new, we won't add any more sales and marketing costs till we hit at least double our revenue on a quarterly basis" (cc L288; speaker INFERRED chairman). The pledge covers net new cost; wage growth on the "fully loaded" team (cc L289) sits outside it [INFERENCE: a reading of "net new"] (Role 5 addendum, loop 1; loop 2: tagged, "bonus" dropped); "There will not be any future investment in that area" (cc L297); "intensity of investments will get kind of lower from Q3 or Q4 onwards" (cc L295). On Q2 revenue Rs 3,931 Mn (cc L126) the freeze runs to about Rs 7,862 Mn a quarter [INFERENCE: 2x] | ND | ND | New | MEDIUM (Role 5 addendum, loop 1: was MEDIUM-HIGH; specific threshold, but self-qualified to net new, no S&M base disclosed or filed (Q33), speaker inferred) |
| Accounting policy (added row) | Product development fully expensed, "as a policy, today" (Role 5 addendum, loop 2) (cc L199, L389-L391, L473); option to capitalise retained (cc L389) | ND | ND | New | HIGH (policy statement) |
| Dividend / payout policy | ND (not discussed) | ND | ND | ND | ND |

Diagnostics:
- Widened or tightened: no prior to compare. Within the call the FY27 guide widened from "close to around 9%" (cc L230) to "9% to 10%" (cc L244). The FY27 guide sits at or below the bottom of the deck's own ~9-11% STRENGTHEN band (pres L165).
- Dropped without acknowledgment: the FY27 double-digit B2S share (CF07). DROPPED candidate, unverified, not scored.
- Internal consistency [INFERENCE, filed bases]: FY26 revenue 1,261.49 Cr (Step 1A). FY27 at +30-35% = 1,639.94-1,703.01 Cr. Less H1 FY27 766.89 gives H2 873.05-936.12 Cr, +29.8% to +39.2% on H2 FY26 672.42. FY27 EBITDA at 9.0% = 147.59-153.27 Cr; less H1 op EBITDA 73.33 gives H2 74.26-79.94 Cr, an H2 margin of 8.51-8.54%, below Q2's 8.69%. At 10.0%, H2 must run at 10.36-10.38%. The point guide implies no H2 recovery, while the same call says investment intensity falls from Q3 or Q4 (cc L295) and no new S&M is added (cc L288). The statements reconcile only near the 10% top end (CF01).
- The H2 revenue range needs about 436.5-468.1 Cr a quarter, 11-19% above Q2's 393.09 [INFERENCE]. Management names material availability as the limiter (cc L248-L251, L356).
- EXPAND band timing (Role 5 addendum, loop 1: corrected): FY27 at 9-10% sits below the 11-13% band, so the phase's first year misses. FY28 is guided at a floor, not a band: "double digits" (cc L266) and "10 plus percent ... without even doing any further additional effort" (cc L476-L477). "Around 200 basis points" (cc L294, base lost) on a 9-10% base would reach 11-12% [INFERENCE]. Band entry is unguided; FY28 is the earliest year (CF02).
- Versus Four-Pillar projections: ND (no projections on file).
- Guidance refused when pressed: annual product development budget (cc L205, L208); order book by year (cc L454); AI DC and robotics numbers (cc L216); B2S revenue share (cc L382-L394, no answer); the split of the margin drop between mix and product development (cc L225-L228).

---

### STEP 3: PROMISE vs DELIVERY AUDIT

#### 3A. Last quarter's commitments
| Commitment From Q1 FY27 Concall | This Quarter's Actual | Status | Points |
|---|---|---|---|
| ND (prior log not passed) | ND | ND | ND |
| Analyst-recalled, unverified: B2S double-digit share of FY27 revenue (cc L375-L376) | Q2 share NOT DISCLOSED (pres L361 "Others share includes B2S"); B2S revenue now FY29-FY30 (cc L411, L428-L429) | Not scored (prior commitment unverified); DROPPED candidate | excluded |

#### 3A-bis. Baseline promise log opened by this call (Q2 FY27 call, 15-Oct-2026)
Seeded by the A3 commitment register. Every row is OPEN. Scoring starts at the Q3 FY27 call.

| # | Commitment | Test threshold | Due / test date | Test source | Ref |
|---|---|---|---|---|---|
| P01 | FY27 EBITDA margin ~9% / 9-10% | FY27 consolidated op EBITDA margin in 9.0-10.0% | Q4 FY27 results, about Apr-May 2027 [INFERENCE] | filing | cc L103, L230, L244, L266 |
| P02 | FY28 EBITDA margin double digits / "10 plus" | FY28 op EBITDA margin >= 10.0% | FY28 results | filing | cc L266, L476 |
| P03 | Double-digit EBITDA margin "from the Q1 onwards" (read Q1 FY28) | Q1 FY28 op EBITDA margin >= 10.0% | about late Jul 2027 [INFERENCE] | filing | cc L231 |
| P04 | EXPAND: four to seven industries; ~11-13% framework | Robotics and AI DC revenue named; margin in band | FY27-FY29 | filing / deck | cc L82-L86 |
| P05 | TRANSFORM: ~13-18% framework | Margin in band | FY30+ (outside window) | filing | cc L88, L96 |
| P06 | No net new S&M cost until quarterly revenue at least doubles | No net new S&M cost (new sales, bid or marketing roles or cost lines) until revenue about Rs 7,862 Mn a quarter; testable only once the S&M base is disclosed (Q33); wage growth on the existing team sits outside the pledge as given [INFERENCE: a reading of "net new"] (Role 5 addendum, loop 1; tag loop 2) | every quarter | call / deck | cc L288, L297 |
| P07 | Investment intensity lower from Q3 or Q4 FY27 | Combined employee plus other-expense ratio below Q2's 28.72%. (Role 5 addendum, loop 2) Absolute co-reading: combined employee plus other expenses vs Q2 FY27 1,128.89 Mn (678.87 + 450.02; res L543, L546). At about 437 Cr a quarter the ratio stays below 28.72% with expenses up to about 1,255 Mn (+11.2% QoQ) [INFERENCE: 0.28718 x 4,370.8], so a ratio pass alone re-credits the P09 revenue growth and does not test "There will not be any future investment in that area" (cc L297). Q1 FY27 already printed 27.47% (Step 8C) | Q3 / Q4 FY27 | filing | cc L295 |
| P08 | Margin expansion ~200 bps (base lost) | UNCLEAR until base stated (Q34) | undated | call | cc L294 |
| P09 | FY27 revenue growth 30-35%; H2 above 30% | FY27 revenue 1,639.94-1,703.01 Cr; H2 >= 874.15 Cr (30% on 672.42); Q3 FY27 >= 394.29 Cr (30% on the deck Q3 FY26 303.3, pres L249) [INFERENCE]. (Role 5 addendum, loop 1) H2 governs: Q3 + Q4 >= 874.15 Cr. The Q3 bar is only +0.3% QoQ on 393.09 (Q3 FY26 is the weaker H2 base and the only QoQ decline in Step 3, -2.36%), so it is an early warning, not a pass; at the bar Q4 needs 479.86 Cr (+21.7% QoQ; +30.0% YoY; the same QoQ step Q4 FY26 made, Step 3) (Role 5 addendum, loop 2). Restate the Q4 requirement after Q3 | Q3 FY27 (about mid-Jan 2027) and Q4 FY27 | filing | cc L354, L361 |
| P10 | Order intake "600 crores plus" in each of Q3 and Q4 FY27 (hedged: "probably you will be expecting it", cc L256) | Book-walk intake >= Rs 6,000 Mn each quarter (closing book - opening book + revenue). (Role 5 addendum, loop 2) Walk intake Q2 FY26 469.9, Q3 FY26 361.6, Q4 FY26 436.3, Q1 FY27 556.1, Q2 FY27 607.9 Cr (pres L247-L249, L289-L294; res L538): 600 Cr reached once in five quarters; the guide needs H2 intake about 50% above H2 FY26 797.9 Cr [INFERENCE: 1,200 / 797.9] | Q3, Q4 FY27 | deck book + filed revenue | cc L256 |
| P11 | Book executes in 18-24 months on average | UNCLEAR (year split not published) | rolling | call | cc L236, L452-L455 |
| P12 | Win ratio ~40%; $400-500 Mn order impact from the existing pipeline | UNCLEAR (undated) | undated | call | cc L262-L264, L332-L333 |
| P13 | Four B2S programmes (~$1 bn) enter the order book after design and prototype testing | Order book step-up named as B2S | undated | deck / call | cc L309-L310, L409-L410 |
| P14 | B2S production start FY29; full ramp FY30 | B2S revenue line from FY29 | FY29 / FY30 (outside window) | filing / deck | cc L411, L428-L429 |
| P15 | AI DC and robotics update: position, opportunities, pipeline | Named pipeline or orders at the Q4 FY27 call | Q4 FY27 call | call | cc L217, L460-L461 |
| P16 | Semicap growth "every quarter" | Semicap revenue disclosed and rising QoQ (needs Q40) | from Q3 FY27 | call / deck | cc L238, L459 |
| P17 | Altec integration completed; renamed | Completion statement, confirmed (pres L192; pr L103-L104); recorded, not scored | done (date NOT FOUND) | deck | cc L114, L437 |
| P18 | More US revenue traction | Subsidiary revenue (consolidated minus standalone) up QoQ | undated | filing | cc L439 |
| P19 | Inventory optimisation and collections focus (no target) | Inventory days below 162 (deck) / 177.8 (filing) | undated | deck / filing | cc L150, L182 |
| P20 | "ready to convert some large orders from the new sales team" | Named large order | undated | call / deck | cc L478-L479 |
| P21 | Honeywell build-to-print programme back to serial production | Restart dated or confirmed | undated | call | cc L405-L407 |
| P22 | Product development fully expensed; "no surprises in the future" | No capitalisation policy change; no new intangibles under development | ongoing | filing | cc L199, L389-L391, L473 |
| P23 | Exports continue; "a little growth in that India market" | India share above 7% (deck) | undated | deck | cc L444-L445 |
| P24 | Growth sustains through FY27 and into FY28 | FY28 revenue growth positive | FY28 | filing | cc L56, L298-L299 |

#### 3B. Cumulative track record (trailing 4 concalls)
| Concall Date | Total Commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| 15-Oct-2026 (baseline) | 23 forward (P17 recorded, not scored) | 0 | 0 | 0 | 0 | 0 (1 candidate, unverified) | 23 (none measurable yet) | 0 |
| Prior three concalls | ND (prior log not passed) | ND | ND | ND | ND | ND | ND | ND |

Credibility Ratio = 0 / (23 - 23): undefined. ND. Grade ND. Role 1 track-record input ND. The protocol's single-source rule cannot run until the Q3 FY27 call scores the first commitments; Role 1 must carry ND, not a substituted judgment. DROPPED governance rule: 0 verified DROPPED; not fired.

#### 3C. Pattern recognition
No scored history. One cross-call pattern sits in Notion memory (SECONDARY): the stated gross-margin cause has changed in each of three calls. April: "a couple of basis points". July: "investments made into the organisation". October: Q2 cause revenue mix and product development (CFO, cc L158); full-year cause sales and marketing, with mix scoped to this quarter (CEO and chairman, cc L279-L287) (Role 5 addendum, loop 1: scope, not conflict). No call names component cost. Logged for tracking; not scored.

#### 3D. Promoter Verdict / Management Grade
No change. Promoter Verdict TRUSTWORTHY-with-flags stands (Notion); no Management Grade on file; credibility ratio ND. Flag for Halt 1: eight call claims contradict the filing or the deck (Step 7A); that is a credibility input, not a grade change.

#### 3E. Last quarter's questions
Prior-quarter Questions for Management: ND (not on page). This quarter's Role 4 Step 8.5 questions now carry an ANSWER STATUS column (Step 8.5, Role 5 addendum): ANSWERED 1, PARTIALLY 4, EVADED 4, NOT ADDRESSED 21, of 30 (Role 5 addendum, loop 1: Q10 and Q28 regraded). Repeated evasion across calls cannot be counted yet (first logged call).

Checkpoint: 3A-3E shown. Credibility ND; the unanswered pattern is the main input.

---

### STEP 4: Q&A DECOMPOSITION

#### 4A. Q&A inventory
Speaker for every management reply is INFERRED (A1) unless stated.

| # | Analyst & Firm (turns) | Question (1-line) | Category | Response Quality | Substance (cc lines) |
|---|---|---|---|---|---|
| 1 | Bala Subramanian, Arihant Capital (T006; reply T007 CFO) | Q2 margin impact of product development spend; annual PD budget; capitalise or expense? | Financial | C | Drag "in the range of 100 to 150 basis points" for all investment, not PD alone (L199); all expensed (L199, L202); budget refused: "we do not want to be putting a number" (L205, L208) |
| 2 | Bala Subramanian (T008; T009 CEO) | Work on AI DC, semicap, robotics over 3-5 years | Strategic | B | Semicap "already working" (L214); AI DC and robotics "just started exploring"; update "probably by the end of this financial year" (L215-L217) |
| 3 | Santosh Seshadri, Avendus Park (T012; T013 CFO) | Quantify one-off PD vs revenue mix; mix driver; recurrence | Financial | D | "a mix of various factors"; confident of return to "targeted levels"; no number, no driver (L225-L228) |
| 4 | Santosh Seshadri (T014; T015 CEO) | FY27 margin guidance | Forward Guidance | B | "close to around 9% EBITDA margin" (L230); "from the Q1 onwards ... double-digit" (L231), period unclear |
| 5 | Santosh Seshadri (T016; T017 CEO) | Order book conversion time; semicap revenue timing and run rate | Customer/Order | B | 18-24 months, "very few" beyond two years (L236-L237); semicap revenue in the last two quarters, ramp ahead; no run rate (L238-L239) |
| 6 | Shashank Jha, SP Capital (T020; T021) | Confirm FY27 margin ~9% | Forward Guidance | A | "9% to 10% range. So, that is what we have currently in the guidance" (L244) |
| 7 | Shashank Jha (T022; T023 CEO) | Why the book grows faster than revenue | Operational | B | Material availability; purchase-order release; 18-24 months (L248-L252) |
| 8 | Shashank Jha (T024-T028; T025, T029) | Win ratio on the >$1 bn bid pipeline | Customer/Order | B (first reply C) | First reply gave book-to-bill and "600 crores plus" intake (L254-L256); analyst pushed back: "No, sir. I asked about something else" (L257); then "close to around 40%" on past history (L262-L264) |
| 9 | Shashank Jha (T030; T031) | FY28 margin in double digits? | Forward Guidance | A | "For FY28, double digits, and for this year I said it will be 9 to 10" (L266) |
| 10 | Meeth Jain, Systematics Asset Management (T033) | none | n/a | n/a | No response; moderator moved on (L268-L270) |
| 11 | Umang Gadda, Avener Investment Management (T037; T038 CEO, T039 chairman, T040 CEO) | ~1% FY27 margin squeeze: services mix or industry mix? | Financial | B (conflicts with filing) | FY cause is S&M (L280); chairman: gross and contribution margin higher, "it's not the revenue mix" (L282-L284); drag "about 100 bps" (L287) and "150-200 basis point" (L290); freeze on net new S&M until quarterly revenue doubles (L288; Role 5 addendum, loop 1: "net new" restored); "it's not a one-off thing" (L291); "around 200 basis points" after the audio gap (L294); intensity lower from Q3 or Q4 (L295) |
| 12 | Umang Gadda (T041-T045; T042, T044, T046) | The "$1 billion design-led order book" from a press interview | Customer/Order | B | Four B2S programmes, some contracts signed, "close to $1 billion", "not there currently in our order book" (L305-L310); production "from FY30 onwards" (L317) |
| 13 | Nishita, Sapphire Capital (T050; T051 CEO) | Timeline for orders from the pipeline; is the $1 bn B2S in it? | Customer/Order | C | Only "a part" of B2S in the pipeline (L327-L328); "close here on 1.4 billion ... Now ... more than a billion" (L331); "400 to 500 million dollars" order impact; no timeline (L332-L333) |
| 14 | Nishita (T052; T053 chairman, low confidence) | When does the $400-500 Mn reach the order book? | Clarification | C | Pipeline is "a point in time"; "1.5 billion dollars roughly ... unweighted", up from 1.4 (L336-L339); closes "60-70 million dollars" a quarter, adds "x 100 million dollars" (L340-L341); no timing |
| 15 | Nishita (T054; T055 CEO) | Q1 35% vs Q2 26%; FY27 30-35%? | Forward Guidance | B | "probably yes ... 30-35% growth" (L354); material and customer-site delays (L356-L357); H2 "definitely ... above 30%" (L361) |
| 16 | Suman Kumar, "Modila Loswal" (machine text) (T057) | none | n/a | n/a | Dropped from the queue (L364-L369) |
| 17 | Aditya Pal, MSA Capital Partners (T061; T062 CFO) | Prior FY27 double-digit B2S share target; should higher B2S margin offset the investment drag? | Forward Guidance | D | Rename to Electronic Products; lifecycle lag; expensing by choice (L382-L394). No share; target neither confirmed nor withdrawn |
| 18 | Aditya Pal (T063; T064 CEO) | Large customer launching 2027-28 on a nine-year contract; Honeywell's Indigo avionics award | Customer/Order | B | Honeywell work is build-to-print; serial production delayed by engineering changes, no date (L404-L407); other contracts signed, not in the book; revenue "from FY 29" (L409-L411) |
| 19 | Aditya Pal (T065; T066 CEO) | Honeywell micro VCS / liquid loops: margin and lateral capability | Strategic | B | Box build, "completely a build-to-print program", "not for the liquid cooling" (L418-L420); corrects the analyst's premise |
| 20 | Karan Sanwal, Niveshye (T070; T071 CEO) | B2S projects, clients and size by FY28-FY30 | Customer/Order | C | Four programmes "close to a billion dollar"; some signed, some to be signed (L426-L427); "FY29 probably it may start", full ramp FY30 (L428-L429); no client named |
| 21 | Karan Sanwal (T072; T073 CEO) | Years covered by the $1 bn | Clarification | A | "Over a period of some 7 to 9 years" (L431) |
| 22 | Karan Sanwal (T074-T076; T075, T077 CEO) | Altec / US division: revenue and margin outlook | Strategic | D | Renamed; "currently doing as per our plans"; "some more traction on the revenue" (L437-L439); no figure |
| 23 | Karan Sanwal (T078-T080; T079, T081 CEO) | Will the revenue mix shift to domestic? | Strategic | B | Exports continue; "a little growth in that India market" (L444-L445) |
| 24 | Gaurav Shukla, PitVestor (T087; T088 CFO) | Order book split, FY27 vs FY28 execution | Forward Guidance | E | "we don't publish the numbers of what is for each year"; average 18-24 months (L452-L455) |
| 25 | Gaurav Shukla (T089; T090 CEO) | AI DC, semicap, robotics engagement; when material | Strategic | C | Semicap "growth every quarter" (L458-L459); AI DC and robotics "just started exploring"; update at year end (L460-L461) |
| 26 | Gaurav Shukla (T091; T092 CFO) | Q2 other income ~23 Cr in both years: recurring or one-off? | Financial | D | "forex variations ... some export incentives ... every quarter it keeps varying" (L464-L465); omits the earnout reversal the CFO himself placed in other income at L163 |

Grade tally (24 graded exchanges; 2 slots without a question): A 3, B 11, C 5, D 4, E 1. C/D/E = 10 of 24 (41.7%).

#### 4B. Question pattern analysis
- Most repeated: margin and investment drag, asked by 5 of 8 analysts (Q1 T006, Q2 T012/T014, Q3 T020/T030, Q5 T037, Q8 T061; A2). Order book, pipeline and B2S, asked by 7 of 8 (Role 5 addendum, loop 2: label widened; on the narrow pipeline / B2S label the count is 5 of 8) (Q2 T016, Q3 T022-T026, Q5 T041, Q6 T050-T052, Q8 T061-T063, Q9 T070-T072, Q10 T087; Role 5 addendum, loop 1: Q8 added). The market did not accept the first answer on either topic.
- Topics graded C, D or E: the margin split (D, C), the B2S share (D), the US arm (D), other income recurrence (D), the order book by year (E), pipeline timing (C, C), B2S clients (C), new verticals (C). These map onto Role 4's open filing questions: earnout, US arm, gross margin, B2S share.
- Buy-side vs sell-side: classification by firm name only. "Asset Management" / "Investment Management" firms: Systematics (no response), Avener (asked). Other firms: ND. The one large-broker slot (machine text "Modila Loswal") dropped. No hosting broker named. No identifiable large sell-side house asked a question.
- Hosting broker lead: ND. The first question (Arihant Capital) was substantive (margin, PD budget, capitalisation), not a softball.
- Pushback: Shashank Jha (cc L257, "I asked about something else"); Aditya Pal set the old B2S target against the margin drag (cc L375-L381); Umang Gadda "Sorry to harp on the margin spot again" (cc L274).
- Not asked by any analyst: cash flow and CFO, the H1 debt build, the US subsidiary loss directly, the earnout residual, a gross margin figure, related-party flow to the parent, customer concentration.
- Participant note: the non-executive chairman answered the most material margin question. He set the full-year cause at sales and marketing and scoped the CFO's mix comment to Q2 (cc L283-L284); his gross-margin claim contradicts the filing (Role 5 addendum, loop 1); the CFO answered an order-book execution question (T088).

#### 4C. The three most important exchanges

**Exchange A: margin cause (Q5 Umang Gadda, T037-T040)**
- Question (cc L275-L278): "We are expecting kind of a squeeze in margin of around 1% this year compared to 26. And you mentioned that it's due to the product development costs and revenue mix. So, can you ... clarify ... is it because of some nature of services mix changing, like PCB box build or some industry mix changing in revenue?"
- Response (cc L282-L290, T039, chairman INFERRED): "if you look at our gross margin or contribution margin ... they are higher, actually they are significantly higher in FA27 by a year to date than they are in FA26 ... even this quarter if you compare it to the same quarter last year, our contribution margin is still higher. So, it's not the revenue mix ... the reason for the drop in margins by about 100 bps or so is because all these sales and marketing costs have been accounted for. We will not add any more sales and marketing costs till we at least hit about, or at least net new, we won't add any more sales and marketing costs till we hit at least double our revenue on a quarterly basis ... which is almost a 150-200 basis point." (Role 5 addendum, loop 1: "net new" restored from cc L288)
- Said: S&M cost is the full-year cause, with mix scoped to Q2 (cc L279-L284); gross and contribution margin are higher YoY; no net new S&M until quarterly revenue doubles (Role 5 addendum, loop 1).
- Not said: a gross margin figure; a definition of contribution margin; the rupee size of S&M; component cost.
- Thesis implication: the filing contradicts the cause. Consolidated gross margin fell 381 bps YoY (41.22% to 37.41%) and 307 bps in H1 (40.74% to 37.67%) (Step 1A). The combined employee plus other-expense ratio fell 245 bps YoY (Step 4). The deck names revenue mix (pres L374-L375). If "gross margin" means the filed measure, the claim is wrong; "contribution margin" is undefined and untestable. The filing wins. The QoQ read fits the S&M story: opex gave 125 of the 178 bps QoQ fall (Step 4). Defensible reading [INFERENCE]: YoY, materials; QoQ, opex. (Role 5 addendum, loop 1) The S&M pledge covers net new cost only (cc L288). It is testable only once the S&M base is disclosed (Q33). The filing proxy P07 also carries product development, which management says continues (cc L207, L286, L386). The speaker is inferred (T039).
- Follow-up we would have asked: Q32 (define contribution margin and reconcile it to -381 bps) and Q33 (Q2 S&M cost in Rs Mn).

**Exchange B: other income recurrence (Q10 Gaurav Shukla, T091-T092)**
- Question (cc L462-L463): "In last Q2 there is other income of 23 crore and in this Q2 also there is other income 23 crore. So then we should understand that in during Q2 there will be other income or this is one of?"
- Response (cc L464-L465, CFO INFERRED): "Other income this time obviously is a mix of couple of things. There are forex variations which also contributes other income and few other one of items in terms of some export incentives is also part of it. So every quarter it keeps varying."
- Said: forex, export incentives, quarterly variation.
- Not said: the Rs 181.95 Mn earnout reversal, which is 80.5% of Q2 FY27 other income (181.95 of 226.15 Mn; res L288, L539; Role 5 addendum, loop 1 rounding fix) and which the CFO placed in other income in his own remarks (cc L163). Nor that Q2 FY26 carried one too (195.75 Mn, res L213; deck pres L384-L385).
- Thesis implication: the analyst asked the right question and got an answer that omits the dominant item. The company's deck answers it: both Q2s carry an earnout reversal. "One-time" (cc L133) is the label on a second annual write-back. Net FX was +19.0 Mn (res L286). Export incentives are not named in the filing notes; they can sit only in the 25.2 Mn residual [INFERENCE]. Reported Q2 PAT is not a base; the Role 4 A21-1 TTM ex-earnout base stands.
- Follow-up: Q39 (residual for Q2 FY28; export incentive amount).

**Exchange C: B2S share target (Q8 Aditya Pal, T061-T062)**
- Question (cc L375-L381): "over the last couple of quarters, F526, Q3 and Q4, we had mentioned that B2S sales contribution should be in double digit in F527 ... there are higher ... margin for [B2S] ... if we are investing, say for example, 150, 200 basis points, this higher ... margin product should actually neutralize it. So, I am not able to connect".
- Response (cc L382-L391, CFO INFERRED): "Built Respect Division is where we are now renamed as a Product Division, Electronic Product Division ... it's a slightly longer lifecycle. Cost happens in one particular quarter and then obviously you will see the results getting out in the later quarter ... what we have the option is to calculate some of the costs, which we have chosen not to do it because from a pure conservatism principle, we would like to expense it."
- Said: the rename; a lifecycle lag; expensing by choice, with the option to capitalise kept.
- Not said: the B2S share; whether the FY27 double-digit target stands. Later answers put B2S production at "FY29 probably" and full ramp "FY30 onwards" (cc L428-L429).
- Thesis implication: the proof-gate share leg (double-digit design-led share for two quarters) cannot fire before FY29-FY30 on management's own timeline [INFERENCE]. The target is a DROPPED candidate. The retained option to capitalise means a later policy switch could lift reported EBITDA with no operating change (CF20), which matters because the proof-gate margin leg uses reported EBITDA.
- Follow-up: Q35 (is the target withdrawn; H1 B2S share) and Q41 (expensing policy through FY28).

Checkpoint: 4A-4C complete.

---

### STEP 5: NEW INFORMATION AUDIT

#### 5A. New disclosures

| Disclosure | Type | Material? | Thesis Impact |
|---|---|---|---|
| FY27 EBITDA margin ~9% / 9-10%; FY28 double digits / "10 plus" (cc L230, L244, L266, L476) | Forward catalyst pre-announced (guidance) | YES | First numeric margin guide in the run (deck and press release gave none, FN-07). Sets the margin-leg baseline. Internally inconsistent at 9% (Step 2) |
| FY27 revenue growth 30-35%; H2 above 30% (cc L354, L361) | Forward catalyst pre-announced (guidance) | YES | Answers Role 4 Q19. First dated test at Q3 FY27 |
| No net new S&M until quarterly revenue doubles (cc L288, L297) | Forward catalyst pre-announced (cost pledge) | YES | Operating-leverage pledge on net new S&M only (cc L288). Testable only once the S&M base is disclosed (Q33); the filing proxy P07 also carries product development, which continues (cc L207, L286, L386); speaker inferred (Role 5 addendum, loop 1) |
| Chief Growth Officer and sales leadership hires (cc L42, L289) | New senior management | NO | Not in the filing board items (CHRO only, res L39-L40); name is machine text |
| Four B2S programmes, ~$1 bn, outside the order book, 7-9 years, partly signed (cc L305-L317, L409, L427, L431) | New customer / contract win (unnamed) | YES | Pillar 3 candidate. Only "a part" sits in the pipeline (cc L327-L328). (Role 5 addendum, loop 1) The value rests on expected volumes (cc L313); a press "order book" label (analyst-reported, cc L301-L302) was walked back to "not there currently in our order book" (cc L309). At full run-rate about $111-143 Mn a year [INFERENCE: $1 bn over 9 to 7 years], from FY30 |
| B2S revenue from FY29-FY30 (cc L411, L428-L429) | Negative surprise | YES | Proof-gate share leg moves beyond FY27-FY28 |
| Pipeline "1.5 billion dollars roughly ... unweighted", up from 1.4 on the same basis (cc L338-L339; T053, low confidence); CEO "some of the things going up" (cc L330); closures $60-70 Mn a quarter; "another x 100 million dollars" added (cc L340-L341, an illustration) | New disclosure (pipeline) | YES | Feeder metric; rose $1.4 bn to ~$1.5 bn unweighted; date of the 1.4 figure and weighted value ND (CF09; Role 5 addendum, loop 1) |
| Win ratio ~40% (cc L262-L264); $400-500 Mn order impact (cc L332-L333) | Customer / order | NO (undated) | 40% x $1.5 bn = $600 Mn vs stated $400-500 Mn [INFERENCE] |
| Intake "600 crores plus" in Q3 and Q4 FY27, hedged: "probably you will be expecting it" (cc L256) | Forward catalyst pre-announced (hedged, not pledged; Role 5 addendum, loop 2) | YES | Testable by the book walk (P10); walk intake reached 600 Cr once in five quarters (P10) |
| Honeywell programme is build-to-print; serial production slipped on engineering changes (cc L404-L407, L420) | Negative surprise | YES (moderate) | The analyst's high-margin B2S framing was wrong; anchor-customer timing undated |
| Semicap revenue booked in the last two quarters, unquantified (cc L238, L459) | New product / segment | NO (unquantified) | First EXPAND leg with revenue |
| AI DC and robotics "just started exploring" (cc L215, L460) | Negative surprise (vs deck narrative) | YES | Two of three EXPAND legs are narrative only; update due at the Q4 FY27 call |
| Product development fully expensed; option to capitalise retained (cc L199, L389-L391, L473) | Accounting policy | YES | Tripwire on the proof-gate margin leg (CF20) |
| Book executes in 18-24 months on average; year split not published (cc L236, L452-L455) | Customer / order | NO | Role 4 Q14 refused |
| Other income includes "export incentives" (cc L464) | New disclosure | NO | Not named in the filing notes; can sit only in the 25.2 Mn residual [INFERENCE] |
| Contribution margin "still higher" YoY (cc L283) | Negative surprise (conflict) | YES | Undefined non-GAAP claim against the filed -381 bps gross margin |

#### 5B. What was NOT discussed

| Expected Topic | Why It Should Have Been Discussed | Significance of Silence |
|---|---|---|
| Component cost inside gross margin (Notion test 2) | Filed gross margin -381 bps YoY; peers Kaynes and Syrma disclosed a component and PCB cost shock (Notion memory, SECONDARY) | RED. Third call without a component-cost answer on Notion's count; peer topic. The chairman named memory-market supply, not cost (cc L39) |
| CFO and cash conversion | H1 CFO Rs 14.75 Cr vs PAT 50.30 (Step 5A); the cash falsifier is a named test | AMBER to RED. Only an undefined Q2 "operating free cash flow" was given (cc L149) |
| H1 debt build | Gross borrowings +24.3% in H1; standalone new Rs 28.79 Cr (Step 5) | AMBER. The call claimed "lower working capital borrowings" (cc L160) |
| US subsidiary P&L, earnout residual, impairment headroom | Subsidiary loss ex-earnout (Step 1C); goodwill plus intangibles Rs 117.89 Cr | RED (thesis-relevant) |
| Earnout recurrence in both Q2s | Asked indirectly (cc L462-L463) | RED (omitted from the answer, cc L464-L465) |
| Related-party flow to parent Cyient Ltd (Notion test 5) | FY26 subcontracting Rs 53.756 Cr from nil (Notion memory) | AMBER |
| Automotive / EV, a named core industry (cc L76) | Deck 1% slice (pres L334); Auto & Others fell sharply [INFERENCE, Step 2C] | AMBER |
| Customer advances YoY (33 to 13 days, pres L305-L315) | Only the QoQ move was given (cc L149) | AMBER |
| Customer concentration (top customers 56% consolidated, Notion) | Concentration risk on a single-segment EMS | AMBER (no analyst asked either) |
| CRISIL withdrawal (02-Jul-2026) and GCA days 311 (Notion, AGENCY) | Agency WC read | AMBER |
| FX hedging (FX swing +3.86 Cr YoY inside PBT) | Role 4 Q20 | AMBER |
| Capex and capacity utilisation | CWIP small; no capacity guide | Neutral (routine) |
| Dividend / capital allocation | Routine | Neutral |
| ESOP grants and CHRO appointment of 15-Oct-2026 (res L39-L43) | Same-day board items | Neutral (routine) |

Consecutive-call counts: 1 for every row (prior transcripts not passed), except component cost, where Notion memory gives 3 calls (SECONDARY).

Checkpoint: 5A and 5B complete.

---

### STEP 6: TONE AND SPECIFICITY

#### 6A. Tone comparison
| Topic | Prior Concall Phrase | This Concall Phrase | Direction |
|---|---|---|---|
| Gross margin cause | April: "a couple of basis points"; July: "investments made into the organisation" (Notion memory, SECONDARY) | CFO, for Q2: "revenue mix and certain product development related costs" (cc L158); chairman, for the year: "it's not the revenue mix ... sales and marketing" (cc L284-L287), with mix "just mentioned as it was this quarter thing" (cc L284) | DOWNGRADED (cause shifts again across calls; within the call the speakers differ in scope, not in fact; Role 5 addendum, loop 1) |
| B2S / design-led share | FY27 double-digit (analyst recall of Q3 and Q4 FY26 calls, cc L376; unverified) | Revenue "from FY 29", full ramp "FY30 onwards" (cc L411, L428-L429); no share | DROPPED (candidate) |
| Order book | Q1: about Rs 2,600 Cr, 1.5x (Notion memory) | "all-time high" Rs 2,813 Cr; "over 1.6 times" (cc L33, L36) | UPGRADED (book-walk 1.55x caveat) |
| Supply chain | ND | "continued supply chain shortages ... memory market" (cc L39); "challenges in getting the materials" (cc L248); close: "we're over all the challenges that we had last year" (cc L481) | ND (no prior); conflicts within the call |
| Within call: FY27 margin | n/a | "higher end of the single-digit range" (cc L103) to "close to around 9%" (cc L230) to "9% to 10% range" (cc L244) | WIDENED within the call |
| Within call: product development cost | n/a | "some of these one-offs" (cc L231) to "it's not a one-off thing" (cc L291) | Contradicted within the call |
| Within call: B2S timing | n/a | "By FY30" (cc L308) to "from FY30 onwards" (cc L317) to "from FY 29" (cc L411) to "FY29 probably it may start" (cc L428) | Unstable within the call |
| Within call: investment drag | n/a | "100 to 150 basis points" (cc L199) to "about 100 bps" (cc L287) to "150-200 basis point" (cc L290) | Unstable within the call |
| US arm | ND | "currently doing as per our plans" (cc L438) | ND |

#### 6B. Specificity score
Base: the 53 A2 forward rows (R198-R250).
- Quantified (number, date or binary milestone): 29 (R203-R208, R210, R211, R215, R218, R219, R221-R228, R230, R231, R233-R236, R239, R241, R246, R248).
- Unquantified: 24 (R198-R202, R209, R212-R214, R216, R217, R220, R229, R232, R237, R238, R240, R242-R245, R247, R249, R250).
- Specificity ratio: 29 / 53 = 0.547 (highly specific band, >0.5).
- De-duplicated (restatements of the same pledge collapsed: FY27 margin R211/R218/R221; FY28 margin R225/R248; B2S timing R230/R233/R241; disclosure timing R215/R246; S&M freeze R226/R228): 22 / 46 = 0.478 (moderate band). One quantified row (R235, 30-35%) was offered by an analyst and accepted.
- Reading: the ratio straddles the 0.5 boundary.

#### 6C. Defensive language count (management turns only)
| Pattern | Count | Lines |
|---|---|---|
| Refusal ("would not like to get into", "do not want to be putting a number", "don't publish") | 3 | cc L205, L208, L454 |
| Deferral ("we will come back") | 2 | cc L217, L461 |
| "we believe" | 3 | cc L46, L53, L104 |
| "we expect" | 3 | cc L89, L94, L103 |
| "we hope" | 0 | n/a |
| Protocol-listed total | 11 | |
| Memo: "probably" | 12 | cc L217, L239, L256, L264, L332, L354, L411, L428, L439, L458, L460, L461 |

11 > 5: a hedge-heavy call. Prior count ND. Analyst-turn "we expect" (cc L253, L325, L335, L353, L433, L436) is excluded.

#### 6D. Confidence indicators
- Specific dated pledges: H2 growth above 30% (cc L361); FY28 double-digit margin (cc L266, L476); AI DC and robotics update at year end (cc L217). (Role 5 addendum, loop 2) Moved out: intake 600 Cr plus for Q3 and Q4 is hedged ("probably", cc L256; counted in 6C), a dated expectation, not a pledge. The 6B specificity score runs on A2 rows and does not change.
- A cost pledge with a numeric threshold: no net new S&M until quarterly revenue doubles (cc L288). No S&M base is disclosed (Q33), so it is not yet testable (Role 5 addendum, loop 1).
- An honest slip: the Honeywell programme's serial production delay (cc L406-L407), without a recovery date.
- An acknowledged miss: "a little bit of a hiccup with margin" (cc L473), recovery dated only to FY28.
- Promoter-side chairman on the call answering operational questions directly (T039, T053).
- Absent: named customer wins with deal size (three new logos unnamed, cc L113).

#### 6E. Management archetype
Credibility ratio ND (Step 3B). Archetype: UNCLASSIFIED. Specificity sits at the boundary (0.55 raw, 0.48 de-duplicated). Watch item: if the Q3 and Q4 FY27 scoring puts credibility below 60% and specificity stays above 0.5, management lands in the OVERPROMISER quadrant. The 8 contradicted claims in Step 7A are the early warning.

Checkpoint: 6A-6E complete.

---

### STEP 7: CROSS-REFERENCE vs FILING AND PEERS

#### 7A. Concall narrative vs filing numbers
| # | Concall Claim | Filing Evidence | Reconciliation |
|---|---|---|---|
| 1 | Revenue Rs 3,931 Mn, +26.5% (cc L126) | 393.09 Cr, +26.54% (res L538) | CONFIRMED |
| 2 | EBITDA Rs 342 Mn, 8.7%, -135 bps (cc L129-L130) | Op EBITDA 34.17 Cr, 8.69%, -135 bps (Step 1A, 2A) | CONFIRMED |
| 3 | Margin drop is investment in sales and growth areas (cc L130, L139); chairman: "about 100 bps ... sales and marketing costs" (cc L287), "150-200 basis point" (cc L290) | YoY combined employee plus other-expense ratio fell 245 bps (31.18% to 28.72%); employee ratio +23 bps; gross margin -381 bps (Step 2C, Step 4). QoQ opex gave 125 of the 178 bps fall | CONTRADICTED YoY; PARTIALLY CONFIRMED QoQ |
| 4 | Gross and contribution margin higher YoY and YTD; "it's not the revenue mix" (cc L282-L284) | Gross margin 37.41% vs 41.22% (Q2); 37.67% vs 40.74% (H1) (Step 1A). Deck: "one-off Revenue mix impact and purchases towards product development" (pres L374-L375) | CONTRADICTED (gross margin); contribution margin UNVERIFIABLE (undefined) |
| 5 | Normalized PAT Rs 158 Mn, +25.8%, "broadly keeping pace with our revenue growth" (cc L131) | 15.82 Cr, +25.85% (Step 2A); about 89% of the gain is the FX swing; ex-earnout ex-FX PBT +1.91% | PARTIALLY CONFIRMED (arithmetic true; quality claim misleading) |
| 6 | "our underlying profitability remained healthy" (cc L140) | As row 5; a 14.48 Mn US deferred-tax credit also lifts it (Step 4) | PARTIALLY CONFIRMED (misleading) |
| 7 | "one-time reversal" of earnout Rs 182 Mn (cc L133, L163) | 181.95 Mn in Q2 FY27 (res L288); 195.75 Mn in H1 FY26 (res L213), placed in Q2 FY26 by the deck (pres L384-L385) | CONTRADICTED (second consecutive Q2) |
| 8 | Q2 other income is forex plus export incentives, varies each quarter (cc L464-L465) | Q2 other income 226.15 Mn (res L539): earnout 181.95 (80.5%; Role 5 addendum, loop 1 rounding fix); FX +19.0 (res L286); residual 25.2 [derived] | CONTRADICTED by omission |
| 9 | Finance cost -10.4% YoY to Rs 61 Mn; H1 -21% (cc L160, L179) | 61.01 vs 68.11 Mn (res L544); H1 12.22 vs 15.43 Cr = -20.8% | CONFIRMED |
| 10 | "supported by lower working capital borrowings" (cc L160, L179) | 30-Sep-2025 balance NOT FOUND; H1 FY27 gross borrowings +24.3% (1,061.25 to 1,319.60 Mn; res L170, L177); standalone new 287.91 Mn (res L565) | UNVERIFIABLE YoY; the current direction runs against it |
| 11 | Order book Rs 28.1 bn; +2.1 bn QoQ; +5.2 bn YoY (cc L127, L174) | Deck 28,137 / 25,989 / 22,911 Mn (pres L289-L294) | CONFIRMED (deck; not a filed figure) |
| 12 | Book-to-bill "over 1.6 times" (cc L36) | Book walk 6,079 / 3,930.90 = 1.55x (Step 6B) | CONTRADICTED (marginal; the walk governs) |
| 13 | NWC 153 days from 161; inventory 162; DSO 77 to 73 (cc L148) | Deck same (pres L286-L315); filing basis NWC 189.0 days TTM, inventory 177.8 (Step 5A) | PARTIALLY CONFIRMED (deck basis only) |
| 14 | Customer advances 13 days vs 15 (cc L149) | Deck 15 to 13; Q2 FY26 33 (pres L305-L315) | CONFIRMED QoQ; YoY fall omitted |
| 15 | Operating free cash flow Rs 172 Mn (cc L149) | Deck footnote only (pres L325); H1 CFO minus capex 4.11 Mn [derived, res L229, L234]; Q2 CFO not filed | UNVERIFIABLE |
| 16 | H1 revenue Rs 7,669 Mn, +30.2%; EBITDA Rs 733 Mn, +30.4%, 9.6% (cc L168-L170) | 766.89 Cr, +30.19%; 73.33 Cr vs 56.25 (+30.4%), 9.56% (Step 1A) | CONFIRMED |
| 17 | H1 normalized PAT Rs 321 Mn, +60.4%; reported Rs 503 Mn, +27% (cc L171-L172) | 32.10 vs 20.03 Cr (+60.3%); 50.30 vs 39.61 Cr (+27.0%) (Step 1A) | CONFIRMED |
| 18 | "positive growth across all key segments" (cc L41) | Auto & Others 1% slice (pres L334); the other 22% of revenue shrank 6-15% in aggregate (Step 2C) [INFERENCE]. (Role 5 addendum, loop 1) The CFO's mix (cc L151-L152) assigns the slices and fixes the upper end: the other 22% fell about 15.3% (1,021.3 to 864.8 Mn; -14% to -17% across share rounding) [INFERENCE] | CONTRADICTED [INFERENCE] |
| 19 | US business "currently doing as per our plans" (cc L438) | Subsidiary op EBITDA 1.15 Cr (1.17%); PAT ex-earnout (3.56) Cr in Q2 (Step 1C); an earnout write-back implies missed targets [INFERENCE] | CONTRADICTED [INFERENCE] |
| 20 | RoW 93%, India 7% (cc L154) | Deck 93% / 7% (pres L334-L350); standalone is 75.0% of consolidated revenue (Step 1D) | CONFIRMED (deck) |
| 21 | Box Build +86% / +85%, 37% share (cc L111, L153) | Deck 86%, 37% (pres L346, L359) | CONFIRMED (85% is a misspeak or mishearing) |
| 22 | Normalized PAT margin "stable at 4%" (cc L131) | 4.02% vs 4.05% (pres L392; Step 4) | CONFIRMED |
| 23 | "we're over all the challenges that we had last year" (cc L481) | Filing leg withdrawn (Role 5 addendum, loop 1): inventory days improved to 177.8 from 187.3 at Mar-26 on the filing basis (Step 5A), which does not contradict the claim. Within the call: "continued supply chain shortages" (cc L39); "challenges in getting the materials" (cc L248); material and customer-site delays (cc L356) | CONTRADICTED WITHIN THE CALL (not by the filing) |
| 24 | (Role 5 addendum, loop 1; revised loop 2) Chairman: product development "has been going on for a while, it's not that it is something that we only started this quarter" (cc L286). His "it's not a one-off thing" (cc L291) refers to the S&M and PD investment drag on EBITDA margin (cc L285-L293), not to the deck's material-cost item; the sentence breaks off ("it's not a con, yes there is, there was a...", cc L291) at a page break and an audio gap (cc L292-L294). On mix he agrees with the deck: "this quarter thing" (cc L283-L284) | Deck: "one-off Revenue mix impact and purchases towards product development" (pres L374-L375); CEO in the same call: "some of these one-offs" (cc L231) | CONTRADICTED [INFERENCE] (call vs deck; PD-purchase leg only: PD going on for a while, cc L286, so repeat purchases are likely). The mix leg has the chairman's support (this quarter thing, cc L283-L284); the PD-purchase leg of the Q4 and Q18 bull answers is weakened (Role 5 addendum, loop 2) |

Tally (Role 5 addendum, loop 1: row 23 re-tagged, row 24 added): CONFIRMED 10, PARTIALLY CONFIRMED 3, CONTRADICTED by the filing or the deck 8 (rows 3, 4, 7, 8, 12, 18, 19, 24), CONTRADICTED within the call 1 (row 23), UNVERIFIABLE 2; 24 rows. Reading: the reported arithmetic ties. The interpretive claims (cause, quality, recurrence, US arm, breadth) fail. This is the "specificity without reconciliation" pattern the protocol warns against. The filing wins on every row.

#### 7B. Peer concall cross-check
Peer concalls were not supplied to this run. UNVERIFIABLE this run.

| Topic | This Company Said | Peer 1 Said | Peer 2 Said | Most Credible Narrative |
|---|---|---|---|---|
| Component / PCB input cost | Supply shortage in the memory market (cc L39); no cost effect named | ND (not supplied). Notion memory: Kaynes disclosed a component and PCB cost shock in the July window (SECONDARY) | ND (not supplied). Notion memory: Syrma, same (SECONDARY) | UNVERIFIABLE this run; the material ratio rise (+380.7 bps YoY on the filed basis; 379 bps on the deck's rounded figures, pres L376; Role 5 addendum, loop 1) fits the peer narrative [INFERENCE] |
| Demand environment | "very strong and favourable" (cc L52) | ND | ND | UNVERIFIABLE |
| Margin trajectory | FY27 9-10%, FY28 double digits (cc L244, L266) | ND | ND | UNVERIFIABLE |

#### 7C. Concall vs external sources
| Concall Claim | External Source | External Says | Alignment |
|---|---|---|---|
| Working capital improving; "over all the challenges" (cc L148, L481) | CRISIL (Notion memory, AGENCY) | GCA days net of cash 311 at 31-Mar-2026 vs 236; rating withdrawn at company request 02-Jul-2026 | MISALIGNED (agency data predates Q2) |
| Credit standing (not discussed) | ICRA (Notion memory, AGENCY) | AA- Stable, 16-Mar-2026 | ND |
| Semicap growth "every quarter" (cc L459) | SEMI, cited in the deck (pres L127-L128) | Record 2026 equipment sales $165.9 Bn | ALIGNED directionally (company-cited source) |
| Supply shortage, memory market (cc L39) | Kaynes, Syrma (Notion memory, SECONDARY) | Component and PCB cost shock | PARTIALLY ALIGNED (supply named, cost not) |

Checkpoint: 7A-7C complete.

---

### STEP 8: UPDATE THESIS AND POSITION DECISION

#### 8A. Growth trigger status
| Trigger | Status Pre-Concall (Role 4 6D) | Concall Evidence | Status Post-Concall |
|---|---|---|---|
| Order book momentum | ON TRACK (two tie-out caveats) | Intake "600 crores plus" expected for Q3 and Q4, hedged: "probably" (cc L256; reached once in five walk quarters, P10; Role 5 addendum, loop 2); win ratio ~40% (cc L262); pipeline rose to ~$1.5 bn from $1.4 bn unweighted (cc L330, L338-L339; T053, low confidence; Role 5 addendum, loop 1) | ON TRACK (caveats stand; pipeline rise added, date of the 1.4 figure ND) |
| Box Build mix shift | ON TRACK revenue; WEAKENED margin | Box Build "strategically important" (cc L112); chairman claims contribution margin higher (cc L283), filing contradicts | ON TRACK revenue; WEAKENED margin |
| Margin path to 11-13% (EXPAND) | DELAYED | FY27 9-10%, FY28 "10 plus" (cc L244, L266, L476); FY28 guided at a floor; band entry unguided (Role 5 addendum, loop 1) | DELAYED (FY27, the phase's first year, misses the band; FY28 the earliest entry year) |
| B2S share to double digits (proof gate) | DELAYED (unmeasurable) | B2S production "FY29 probably", full ramp FY30 (cc L428-L429); FY27 target unanswered (cc L376, L382-L394) | WEAKENED |
| US arm (ex-Altek) turnaround | WEAKENED | "doing as per our plans" (cc L438), contradicted by the filing (Step 7A row 19) | WEAKENED |
| New verticals (semicap, robotics, AI DC) | DELAYED (unmeasurable) | Semicap revenue for two quarters, unquantified (cc L238); AI DC and robotics "just started exploring" (cc L215, L460) | DELAYED (update due Q4 FY27) |
| FY27 growth 30-35%, H2 above 30% | n/a | cc L354, L361 | NEW (first test Q3 FY27) |
| Operating leverage from the S&M freeze (net new cost only) | n/a | cc L288, L295, L297 | NEW (testable once the S&M base is disclosed, Q33; Role 5 addendum, loop 1) |

#### 8B. Watchlist items (six Notion tests)
| # | Watchlist Item | This Concall Reading | Status |
|---|---|---|---|
| 1 | Cash falsifier | Deck-basis NWC 153 days stated; no formula, no target, no CFO; Q2 "operating free cash flow" Rs 172 Mn undefined (cc L148-L150) | AMBER (unchanged; basis ruling still pending) |
| 2 | Gross margin | No component-cost answer. Q2 cause: mix and product development (CFO, cc L158); full-year cause: sales and marketing, with mix scoped to Q2 (cc L279-L285) (Role 5 addendum, loop 1). Chairman claims gross margin higher YoY against the filed -381 bps | RED (provisional). The call confirms the "no component-cost answer" leg; the third-quarter count still rests on Notion's Q4 FY26 entry |
| 3 | Order book | Rs 2,813 Cr, "over 1.6 times" (cc L33, L36); intake 600 Cr plus expected, hedged: "probably" (cc L256; reached once in five walk quarters, P10; Role 5 addendum, loop 2) | GREEN (caveats: walk 1.55x; YoY intake tie-out) |
| 4 | Proof gate | Margin leg: FY27 9-10%, FY28 10 plus. Share leg: not given when asked (cc L376, L382-L394); B2S revenue FY29-FY30 | RED on the margin leg; share leg cannot fire before FY29-FY30 on management's timeline [INFERENCE]. NOT FIRED |
| 5 | Related-party flow to parent | Silent | UNKNOWN (SILENT, 1 call) |
| 6 | Standalone vs consolidated | US "as per our plans" (cc L438); no subsidiary figures; earnout called one-time | RED for the US leg (call conflicts with the filing) |

#### 8C. Thesis-broken trigger check
| Thesis-Broken Condition | Threshold | Concall-Relevant Evidence | FIRED? |
|---|---|---|---|
| None signed (Notion: ND) | ND | ND | NO (no condition exists) |

Candidate tripwires added for the operator to sign at Halt 1 (Role 4 list (a)-(e) stands): (f) (Role 5 addendum, loop 1: aligned to the pledge as given) any net new S&M cost (new sales, bid or marketing roles or cost lines) before quarterly revenue reaches about Rs 7,862 Mn (P06); testable only once the S&M base is disclosed (Q33); (g) (loop 1: revised) H2 FY27 revenue below 874.15 Cr (P09). A Q3 below 394.29 Cr is an early warning only, because that bar is +0.3% QoQ on the weaker H2 base (Q3 FY26 303.3 Cr, the only QoQ decline in Step 3); a Q3 at the bar leaves Q4 needing 479.86 Cr (+21.7% QoQ; +30.0% YoY; the same QoQ step Q4 FY26 made, Step 3; Role 5 addendum, loop 2); restate the Q4 requirement after Q3; (h) any switch to capitalising product development before FY28 (P22); (i) FY27 op EBITDA margin below 9.0% (P01); (j) FY28 op EBITDA margin below 10.0% (P02). None can fire; none is signed.

#### 8D. Four-Pillar inputs
DEFERRED TO /fttcp AND ROLE 1 (operator ruling OR-30). No pillar values exist (ND). Pillar-relevant concall facts flagged:

| Pillar / Input | Pre-Concall | Concall Evidence (flagged fact) | Post-Concall Adjustment |
|---|---|---|---|
| Pillar 1 ROCE (FTTCP ROCE forward verdict) | ND | No ROCE commentary. FY27 margin 9-10%, FY28 "10 plus" from backlog alone (cc L266, L476); operating leverage from the S&M freeze (cc L288); no capex guide | Deferred |
| Pillar 2 Cash | ND | No CFO figure; deck NWC 153 with no formula or target (cc L148, L150); advances falling; conversion limited by materials (cc L248, L356) | Deferred; cash stays INDETERMINATE-WITH-DIRECTION |
| Pillar 3 Emerging Moat | ND | Four B2S programmes ~$1 bn, outside the book, 7-9 years, partly signed, revenue FY29-FY30 (cc L309, L427-L431); semicap revenue started, unquantified (cc L238); AI DC and robotics exploratory (cc L215, L460) | Deferred; signed value NOT DISCLOSED (Q36) |
| Strategic Premium | ND | EXPAND ~11-13% and TRANSFORM ~13-18% bands (cc L86, L96); "Electronic Products" rename (cc L91). Single-credit rule: credit margin recovery once only | Deferred |
| Growth visibility | ND | Book executes in 18-24 months (cc L236, L452); year split refused (cc L454); FY27 30-35%, H2 above 30% (cc L354, L361); intake 600 Cr plus a quarter, hedged "probably" (cc L256; reached once in five walk quarters, P10; Role 5 addendum, loop 2) | Deferred |
| Earnings base (A21) | ND | "One-time" earnout label vs the deck's two-Q2 disclosure (Step 7A row 7) | Deferred; Role 4 A21-1 TTM ex-earnout base stands |
| Role 1 track-record input | ND | No Role 5 history; baseline log of 24 rows opened | ND until scored |

No pillar is recomputed here; no destination PE, Hurdle or fair value is revised.

#### 8E. Position decision
Decision Status verified: NOT SET. Branch 8A-W (non-held). Concall-specific overrides:
- Credibility ratio below 60%: not testable (ND). Not fired.
- Two or more DROPPED in trailing 4 calls: 0 verified (1 candidate). Not fired.
- Undisclosed material risk: none new beyond the filing. Trim rule applies to held names only. n/a.
- Undisclosed material positive (the ~$1 bn B2S outside the book): hold pending verification; no entry-zone action on concall noise.
- Evasion pattern across 3+ quarters: not countable on a verified basis (component-cost silence is 3 calls on Notion memory only). Logged.
- Concall narrative contradicts filing numbers materially: FIRES (margin cause, earnout recurrence, US arm; Step 7A rows 3, 4, 7, 8, 19). Action: trust the filing; note the credibility issue for Halt 1; tighten the next-quarter watchlist (Monitorables 18-32).
Output: no entry zone exists to update. No Decision Status proposed. Halt 1 remains the gate.

#### 8F. Updated questions for the next quarter
| # | Question | Why It Matters | What to Watch in Next Concall |
|---|---|---|---|
| 1 | Q31: which end of the FY27 9-10% band, and why H2 below Q2 at 9% | Margin-leg baseline | A single number and an H2 bridge |
| 2 | Q32: define contribution margin; reconcile to -381 bps gross margin | Call vs filing conflict | A defined measure with values |
| 3 | Q33: Q2 S&M and PD cost in Rs Mn | Base for the S&M freeze | A Rs base, flat in Q3 |
| 4 | Q39 with Q1: earnout residual; Q2 FY28 write-back risk | 80.5% of Q2 other income (loop 1 rounding fix) | Residual stated, or the earnout closed |
| 5 | Q35 with Q16: B2S FY27 target and H1 share | Proof-gate share leg; DROPPED candidate | An explicit withdrawal or a share figure |
| 6 | Q36: signed vs unsigned value of the ~$1 bn | Pillar 3 evidence | A signed value and named customers |
| 7 | Q37: date of the $1.4 bn unweighted figure; weighted value of the ~$1.5 bn (Role 5 addendum, loop 2) | Feeder metric | A dated 1.4 and a weighted value |
| 8 | Q3, Q2, Q11: US subsidiary EBITDA, earnout miss, impairment headroom | US arm "as per plans" vs filing | Subsidiary figures |
| 9 | Q38 with Q6: NWC formula and a dated target | Cash falsifier | A formula and a target date |
| 10 | Q40, Q41, Q42, Q34: semicap revenue; expensing policy; Honeywell restart; 200 bps base | Dated pledges | Numbers and dates |
All other open Role 4 questions (21 NOT ADDRESSED, 4 EVADED, 4 PARTIALLY; Role 5 addendum, loop 1 count) carry forward to Role 4 Step 8.5 of the Q3 FY27 review.

Checkpoint: 8A-8F complete.

---

### STEP 9: NOTION PAYLOAD (Role 5; operator-approval write gate; Decision Status never written)

- Decision Status: NOT written. No change proposed.
- Row properties: none proposed (no Management Grade on file; credibility ND; DROPPED rule not fired).
- Key Notes prepend (proposed): "2026-10-18 | Q2 FY27 concall (machine transcript, speakers inferred): FY27 EBITDA margin guided ~9% / 9-10%, FY28 double digits; FY27 growth 30-35%, H2 >30%; no net new S&M until quarterly revenue doubles (loop 1); B2S revenue FY29-FY30, FY27 double-digit B2S target unanswered; margin cause, 'one-time' earnout and US 'as per plans' contradict filing/deck; credibility ND (baseline log, 24 rows); verdict PROCEED WITH FLAGS unchanged"
- Page append: this Role 5 section under "## Q2 FY27 Concall Analysis - 15-Oct-2026", below the results review.

**Concall Verdict:**
- Call participants: Krishna Bodanapu (non-executive chairman), Rajendra Velagapudi (MD and CEO), R.M. Subramanian (CFO); moderator only.
- Hosting broker: ND.
- Call duration / Q&A duration: 61:14 / 33:07 (54.1%).
- Number of analyst questions: 26 question turns from 8 analysts (10 slots).
- Business type: Standard.
- Management Credibility (this quarter): ND (baseline quarter; no scored commitments). Call vs filing: 8 of 24 checked claims CONTRADICTED by the filing or the deck; 1 more conflicts within the call (Role 5 addendum, loop 1).
- Trailing 4-Quarter Credibility Ratio: ND (0 points / (23 - 23 UNCLEAR)).
- Management Archetype (6E): UNCLASSIFIED (credibility ND; specificity 0.55 raw, 0.48 de-duplicated).
- Role 1 Track Record Input: ND.
- Net concall impact on the pre-thesis read: WEAKENED.
- Position decision: none (8A-W; Decision Status NOT SET; no entry zone).
*Concall reviewed 2026-10-18 | Source: CyientDLM_Q2FY27_Concall_Transcript.txt (machine transcript, via A1 fulltext)*

Save: NOT executed by A4 (no Notion access; payload only).

### ROLE 5 CONCALL FLAGS (Role 5 addendum)
1. CALL vs FILING, MARGIN CAUSE: chairman (T039, inferred) says gross and contribution margin higher YoY and "it's not the revenue mix" (cc L282-L284); he scopes the mix effect to Q2 (cc L283-L284), so no CFO-chairman conflict is counted (Role 5 addendum, loop 1). Filing: gross margin -381 bps YoY; combined opex ratio -245 bps; the deck names revenue mix (pres L374-L375). Filing wins.
2. EARNOUT LABEL: "one-time reversal" Rs 182 Mn (cc L133, L163) vs the deck's "both Q2 FY26 and Q2 FY27" (pres L384-L385). Asked whether Q2 other income recurs, the CFO named forex and export incentives and omitted the earnout (cc L464-L465), which is 80.5% of Q2 other income (res L288, L539; loop 1 rounding fix).
3. GUIDANCE ARITHMETIC: FY27 margin ~9% / 9-10% (cc L230, L244) on 30-35% growth (cc L354) needs H2 at 8.51-8.54% at 9% (below Q2 8.69%) and 10.36-10.38% at 10% [INFERENCE]; it conflicts with "intensity ... lower from Q3 or Q4" (cc L295).
4. PROOF GATE TIMELINE: B2S production "FY29 probably", full ramp FY30 (cc L428-L429). The FY27 double-digit B2S target put by an analyst (cc L376) got no answer: DROPPED candidate, unverified. The share leg cannot fire before FY29-FY30 [INFERENCE]. The EXPAND 11-13% band is missed in FY27; entry is unguided, FY28 at the earliest (Role 5 addendum, loop 1).
5. US ARM: "currently doing as per our plans" (cc L438) vs subsidiary op EBITDA 1.17% and a second earnout write-back (Step 1C); no subsidiary figure when asked (cc L433-L436).
6. NOTION TEST 2: no component-cost answer on the call; the stated cause has changed across three calls (April and July per Notion memory; October: Q2 mix and product development, full-year sales and marketing; Role 5 addendum, loop 1).
7. HEDGE-HEAVY CALL: 11 protocol-listed defensive phrases plus 12 "probably"; specificity 0.55 raw / 0.48 de-duplicated; archetype UNCLASSIFIED.
8. ANALYST COVERAGE: 8 of 10 slots asked; the one large-broker slot (machine text "Modila Loswal") dropped; no question on CFO, the debt build, a gross margin figure or parent related-party flow.
9. PIPELINE DIRECTION (Role 5 addendum, loop 1: corrected): the pipeline rose from $1.4 bn to about $1.5 bn, both unweighted (chairman, cc L338-L339; T053, low confidence). The CEO said "some of the things going up" (cc L330); his "more than a billion" (cc L331) restates the opening floor (cc L33). Open: the date of the 1.4 figure and the weighted value (Q37).
10. ACCOUNTING OPTION: product development fully expensed; option to capitalise retained (cc L389-L391). A later switch would lift reported EBITDA and could meet the proof-gate margin leg through accounting alone (tripwire candidate h).
11. SOURCE: machine transcript, inferred speakers. The S&M freeze pledge and the contribution-margin claim rest on an inferred chairman attribution (T039).
12. TRACK RECORD: no prior concall log; credibility ratio and Role 1 track-record input ND until the Q3 FY27 call scores the baseline log.

---

---

## PLAIN-LANGUAGE BRIEF

Provenance key: FILED = this quarter's results filing; MGMT = this quarter's deck or press release; AGENCY = rating agency (via prior Notion); SECONDARY = prior Notion or peer work; INFERENCE = our reasoning. "Prior Notion" marks memory from the Notion page, not this quarter's filings. (Role 5 addendum) CALL = the 15-Oct-2026 earnings call, from a machine transcript with inferred speakers; where CALL and FILED differ, FILED wins.

### 1. Summary narrative
- Sales grew fast. Q2 FY27 revenue was Rs 393.09 Cr, up 26.54% on a year ago (FILED).
- Growth was narrow. Aerospace and Industrial gave more than all of the rise: about 119% on the call's mix. The rest of the mix shrank about 15% (deck alone: 6-15%) (INFERENCE from CALL and MGMT shares; FILED total; Role 5 addendum, loop 1; deck range restored, loop 2).
- Profit per rupee of sales fell. Operating EBITDA margin was 8.69%, down from 10.04% (FILED).
- Year on year, the cause is materials, not overheads. Gross margin fell to 37.41% from 41.22% (FILED). Opex fell as a share of sales (MGMT deck table).
- Quarter on quarter, overheads caused most of the fall: 125 of the 178 bps. Other expenses rose 17.7% on sales up 5.2% (FILED, derived).
- Management calls the material jump a one-off from mix and product development buys (MGMT). The same deck calls the mix shift the strategy (MGMT). On the call the chairman called the mix a "this quarter thing" and said product development "has been going on for a while" (CALL), so repeat PD purchases are likely (INFERENCE; Role 5 addendum, loop 2).
- Reported profit was Rs 34.01 Cr. Rs 18.20 Cr of that is an earnout write-back (FILED). Without it, profit was Rs 15.82 Cr, up 25.85% (FILED + MGMT: the Q2 FY26 earnout placement comes from the deck).
- About 89% of that gain is a currency swing. Without the earnout and the currency effect, profit before tax rose 1.9% (FILED, derived).
- A US deferred-tax credit of Rs 1.45 Cr also lifts it. Without the credit, profit ex-earnout grew 18.0%, and the tax rate was 31.95%, not 25.09% (FILED, derived).
- This is the second Q2 in a row with such a gain (FILED, MGMT). A shrinking earnout usually means the bought US business missed its targets (INFERENCE).
- The India entity grew revenue 25.10% and profit 43.18% (FILED).
- About half of India's pre-tax profit gain (48.7%) is a currency swing. Without it, India pre-tax profit rose 20.1%, slower than sales. India gross margin fell 435 bps (FILED, derived).
- The US arm is the weak leg. Measured as consolidated minus standalone, net of intercompany eliminations, its EBITDA was Rs 1.15 Cr on Rs 98.30 Cr of sales. It lost money before the earnout gain (FILED, derived; the split by US entity is NOT FOUND).
- Cash was weak. H1 operating cash flow was Rs 14.75 Cr against Rs 50.30 Cr of profit (FILED). The India entity took Rs 28.79 Cr of new short-term debt (FILED).
- The order book hit a record Rs 2,813.7 Cr, up 22.8% in a year (MGMT). The stated order intake growth does not tie to the book (INFERENCE from MGMT figures).
- There is no thesis to test yet. Decision Status is NOT SET and the mental model is unsigned (prior Notion).
- Three of the six named tests read red: gross margin, the proof-gate margin leg, and the US leg. The order-book test is green. Cash and related-party tests are open.
- (Role 5 addendum) On the 15-Oct call, management guided FY27 EBITDA margin to "close to around 9%", then "9% to 10%" (CALL). It guided FY28 to "double digits" (CALL).
- (Role 5 addendum) It accepted an analyst's 30-35% FY27 revenue growth figure. It said H2 growth will "definitely" exceed 30% (CALL).
- (Role 5 addendum) At 9%, the H2 margin must fall to about 8.5%, below Q2. Only the 10% end fits the claim that investment costs ease "from Q3 or Q4" (INFERENCE; loop 1 wording fix).
- (Role 5 addendum, loop 1) The chairman pledged no net new sales and marketing cost until quarterly revenue doubles (CALL; speaker inferred). No cost base was given, so the pledge cannot be tested yet.
- (Role 5 addendum) Design-led (B2S) revenue now starts in FY29 to FY30 (CALL). An analyst asked about the FY27 double-digit target. Management did not answer.
- (Role 5 addendum, loop 1) Of 30 filing questions, the call answered 1, partly answered 4, evaded 4 and did not address 21.
- (Role 5 addendum, loop 1) Eight of 24 checked call claims contradict the filing or the deck. One more conflicts with the call itself. The table below lists the main ones.
- Verdict: PROCEED WITH FLAGS. The operator decides at Halt 1. (Role 5 addendum: unchanged after the call.)

#### Management said vs filing shows (Role 5 addendum)
| Management said (CALL) | Filing shows |
|---|---|
| Gross and contribution margin higher YoY and year to date (chairman, inferred); mix was a Q2-only effect | Gross margin 37.41% vs 41.22% in Q2 and 37.67% vs 40.74% in H1 (FILED) (Role 5 addendum, loop 1) |
| The margin drop is sales and marketing cost, 100-200 bps | Employee plus other-expense ratio fell 245 bps YoY (FILED) |
| The earnout reversal is "one-time" | Q2 FY26 and Q2 FY27 both carry one (FILED; MGMT deck) |
| Q2 other income is forex and export incentives | The earnout is 80.5% of Q2 other income (FILED; loop 1 rounding fix) |
| The US business is "doing as per our plans" | US arm EBITDA 1.17%; a loss before the earnout (FILED, derived) |
| Finance cost fell on "lower working capital borrowings" | YoY cause untestable: the 30-Sep-2025 balance is NOT FOUND, and H1 FY26 repayments fit it. The H1 FY27 build (gross borrowings +24.3%) is a Q3 finance-cost risk (FILED) (Role 5 addendum, loop 1) |
| "positive growth across all key segments" | Auto & Others fell sharply (INFERENCE from MGMT shares) |
| Book-to-bill "over 1.6 times" | The book walk gives 1.55x (INFERENCE from the MGMT book and FILED revenue) |

### 2. Sector intelligence
- Demand is strong at the top of the market. The deck puts global EMS at $649 Bn in 2025 and $853 Bn by 2030 (MGMT, citing MarketsandMarkets).
- The company names three growth pools: AI data centres, chip-making equipment and robotics (MGMT). SEMI expects record 2026 equipment sales of $165.9 Bn (MGMT, citing SEMI).
- Aerospace is the engine this quarter: it grew 62% (MGMT). Defence grew 13%, half the company rate (MGMT).
- Aerospace and Industrial gave Rs 881.7-981.0 Mn of growth against a total rise of Rs 824.56 Mn. The other 22% of revenue shrank 6-15%, so Auto & Others fell sharply. Its value is NOT DISCLOSED (INFERENCE from MGMT shares and growth rates; FILED total). (Role 5 addendum, loop 1) The call assigns the slices (cc L151-L152), which fixes the upper end: Rs 981.0 Mn, about 119% of the rise, and the other 22% down about 15% (INFERENCE from CALL shares).
- Component and PCB costs rose in the same window at Indian peers Kaynes and Syrma (SECONDARY, prior Notion). This quarter's material ratio rise fits that pattern, but management did not name component cost (INFERENCE).
- India's semiconductor mission incentives support local equipment work (MGMT). No filed revenue line shows this yet.
- (Role 5 addendum) On the call, AI data centres and robotics are at the "just started exploring" stage. Chip-equipment work has booked revenue for two quarters; the amount was not given (CALL).
- (Role 5 addendum) Management named memory-market supply shortages. It did not name component cost (CALL).
- Not disclosed: segment revenue in rupees, the chip-equipment share, and component price effects.

### 3. Business-model intelligence
- The company builds electronics to customer drawings. Build-to-print was 94% of FY26 revenue (SECONDARY, prior Notion).
- It earns a conversion margin on bought-in parts. Contracts pass input costs through (SECONDARY, prior Notion). So material cost drives margin.
- Box Build (full assemblies) grew 86% and is now 37% of revenue (MGMT). Box Build carries more bought-in material (INFERENCE). If that holds, faster Box Build growth lowers gross margin even as sales rise.
- The model needs a lot of stock. Inventory equals 177.8 days of sales on our basis, 162 days on the deck basis (FILED; MGMT).
- Customer advances fell from 33 to 13 days in four quarters (MGMT). New orders now fund less of their own stock (INFERENCE).
- The US arm (ex-Altek) adds sales but not profit so far (FILED). Goodwill and acquired intangibles of Rs 117.89 Cr ride on it (FILED).
- Model drift this quarter: margin moved away from the 11-13% target band, not toward it (FILED; MGMT target).
- (Role 5 addendum) Four B2S programmes worth "close to $1 billion" over 7-9 years sit outside the order book. Only part is signed (CALL).
- (Role 5 addendum) Product development is fully expensed. Management keeps the option to capitalise it (CALL).
- Not disclosed: design-led (B2S) revenue share, US entity split, customer advance terms.

### 4. Competition intelligence
- Where it wins: certified, safety-critical work for aerospace, defence and medical customers. Anchor customers include Honeywell Aerospace and Thales (SECONDARY, prior Notion). Aerospace growth of 62% shows this lane works (MGMT). The lane is also narrow: Aerospace alone gave 57-86% of the YoY increase (INFERENCE). On the call's mapping it is about 86% (INFERENCE from CALL shares; Role 5 addendum, loop 1).
- Where it is weaker: scale and cash. Top customers were 56% of consolidated revenue (SECONDARY, prior Notion). Peers Kaynes and Syrma are larger EMS players in India (SECONDARY, prior Notion).
- Design-led share is small (6% in FY26, SECONDARY, prior Notion) and is not disclosed now (FILED/MGMT silence). A design moat is not visible in the numbers.
- The US arm was bought to reach customers abroad (MGMT). Its 1.17% EBITDA margin says it does not yet compete on cost (FILED).
- (Role 5 addendum) The Honeywell programme is build-to-print, not design-led. Serial production slipped on engineering changes, with no new date (CALL).
- Risk to watch: if peers pass on component costs faster, Cyient DLM's gross margin gap widens (INFERENCE).

### 5. Forward map (next ~10-11 months)
Make-or-break reading: Q3 FY27 consolidated gross margin, results about mid-Jan 2027 (INFERENCE date). Bull at or above 40.05%. Bear at or below 37.41% with Box Build at or above 37%. Co-reading: the combined opex ratio against the H2 FY26 average of 29.55%. (Role 5 addendum, loop 1: revised) The same results open the H2 growth test: H2 revenue at or above 874.15 Cr, about 437 Cr a quarter. Q3 FY26 (303.3 Cr) holds the only QoQ decline in Step 3 (-2.36%) and is the weaker of the two H2 bases, so a Q3 at the 30% bar (394.29 Cr) is only +0.3% QoQ and leaves Q4 needing 479.86 Cr (+21.7% QoQ; +30.0% YoY; the same QoQ step Q4 FY26 made, Step 3) (Role 5 addendum, loop 2). They also test intake of 600 Cr plus. Rows that share a period test different claims: the Q4 FY27 call row tests the company guide and the 31-Mar-2027 row the H1 run rate; the two late-Jul 2027 rows test the "double-digit from Q1" pledge and the 11-13% band.

| Date | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| Now (Role 5 addendum: done 2026-10-18) | Role 5 on the 15-Oct-2026 call | Management gives a component-cost split and an earnout residual | Questions on the earnout and margin are evaded (outcome: bear fork; no component split, earnout omitted) |
| About mid-Jan 2027 (Role 5 addendum) | Q3 FY27 call: first score of the baseline promise log | Q3 revenue at or above about 437 Cr (even split of the 874.15 Cr H2 floor; Q4 then needs no QoQ growth); intake 600 Cr plus by the book walk; S&M base disclosed and no net new S&M cost. Neutral band (Role 5 addendum, loop 2): a Q3 of 394.29-437 Cr does not decide H2. H2 then rests on Q4 at up to +21.7% QoQ, the step Q4 FY26 made (Step 3), and at the bar both H2 quarters grow the pledged 30% YoY | Q3 below 394.29 Cr, so Q4 must beat the FY26 Q4 step (+21.7% QoQ) to reach 874.15 Cr; intake below 600 Cr; S&M base still undisclosed, or net new S&M added. Two readings [INFERENCE, one year of data]: even split (437 Cr a quarter) vs the FY26 shape (Q3 45.1% of H2, so 394.3 / 479.9 Cr). The separating observation: whether the Q3 FY26 -2.36% QoQ dip was seasonal (Q3 FY25 not in the run) (Role 5 addendum, loop 2) |
| About Apr to May 2027 (Role 5 addendum) | Q4 FY27 call: AI data centre and robotics update; FY27 margin vs 9-10% | Named pipeline and orders; FY27 margin near 10% | Still "exploring"; FY27 margin at or below 9% |
| About late Jul 2027 (Role 5 addendum) | Q1 FY28: the "double-digit from Q1" pledge | Q1 FY28 margin at or above 10% | Below 10% |
| Halt 1 (date ND) | Operator ruling on NWC basis and the H1 print | A basis that reproduces 169 days; H1 deck 153 reads as improving | Filing basis governs; 189.0 days confirms STRUCTURAL |
| About mid-Jan 2027 | Q3 FY27 results | Gross margin back to 40.05%; combined opex ratio below 29.55%; US EBITDA positive; standalone debt repaid | Gross margin at or below 37.41%; combined opex ratio at or above 29.55%; US loss widens; debt rises above 28.79 |
| About Mar 2027 | ICRA AA- surveillance | Rating and outlook held | Outlook cut on working capital or US debt |
| 31-Mar-2027 | FY27 outlook "positive for the year" | Revenue growth near the H1 rate of 30.19% | Growth slows and margin stays below 9.56% |
| About Apr to May 2027 | Q4 FY27 and FY27 audited results | Positive CFO and NWC on a path to 120 days; no impairment | CFO weak; NWC above 161; US goodwill impaired |
| About Jun to Jul 2027 | FY27 Annual Report | Related-party flow to the parent stable; US loss small | Parent subcontracting rises; US loss and DTA grow |
| By Sep 2027 | US current borrowings of 67.18 Cr fall due | Refinanced on its own terms | India cash repays it; group net cash falls below 22.64 |
| About late Jul 2027 | Q1 FY28 results | Margin enters 11-13%; a new-vertical order is named | Margin still below 9.56%; new verticals unquantified |

---

```yaml
stage: A4-analyst
company: "CYIENTDLM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2   # Role 4 correction loops; Role 5 addendum correction loops: 2 (loop 1 and loop 2, 2026-10-18)
docs_merged: [results, presentation, pressrelease, concall]   # Role 5 addendum 2026-10-18: concall added; loop 1: pressrelease restored
ledger_reconciliation:
  notes: 8
  turns: 97   # Role 5 addendum: concall ledger (Role 4 ledgers carry 0 turns)
  slides: 21
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18, A3-19, A3-20, A3-21, FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN-01, FN-02, FN-03, FN-04, FN-05, FN-06, FN-07, FN-08, CF01, CF02, CF03, CF04, CF05, CF06, CF07, CF08, CF09, CF10, CF11, CF12, CF13, CF14, CF15, CF16, CF17, CF18, CF19, CF20, CF21, CF22, CF23, CF24, CF25]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "NOT SET (Halt 1 pending; mental model unsigned; pre-thesis read)"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY26", reported_pct: 137.5, ex_earnout_pct: -7.1}
  - {period: "Q1 FY27", reported_pct: -2.5, ex_earnout_pct: -2.5}
  - {period: "Q2 FY27", reported_pct: 75.5, ex_earnout_pct: -18.4}
  - {period: "H1 FY26", reported_pct: 59.7, ex_earnout_pct: -19.2}
  - {period: "H1 FY27", reported_pct: 39.4, ex_earnout_pct: -11.0}
  - {period: "FY26", reported_pct: 30.1, ex_earnout_pct: "ND"}
questions_for_management:
  - {q: "Remaining earnout liability at 30-Sep-2026 after the Rs 181.95 Mn gain (Rs Mn)?", from_finding_id: [A3-06, A3-16, FN05, FN-03]}
  - {q: "By what % did the acquired US business miss the earnout metric behind the Rs 181.95 Mn write-back?", from_finding_id: [A3-04, A3-06, FN05, FN-03]}
  - {q: "Cyient DLM Electronics Inc. (ex-Altek) Q2 FY27 EBITDA in Rs Mn (subs EBITDA fell to 11.51 Mn from 57.43 Mn)?", from_finding_id: [A3-05, A3-04, FN14]}
  - {q: "Of the 381 bps YoY gross-margin drop, how many bps from component price inflation vs Box Build mix?", from_finding_id: [FN01, FN02, FN03, A3-07, FN-01]}
  - {q: "Is the deck's 11-13% FY27-29 margin an EBITDA margin, and in which FY does the company expect to enter the band?", from_finding_id: [FN04, FN17, FN-08]}
  - {q: "What formula gives the deck NWC of 153 days, and what does it give for FY26?", from_finding_id: [FN08, A3-08]}
  - {q: "Planned peak standalone short-term borrowings by 31-Mar-2027 (Rs 287.91 Mn drawn in H1)?", from_finding_id: [A3-03, FN09]}
  - {q: "Share of the Rs 28,137 Mn order book with customer advance terms now vs a year ago?", from_finding_id: [FN07, A3-10]}
  - {q: "Is the US facility (about Rs 278 Mn moved to current) due within 12 months; refinance or repay from India cash?", from_finding_id: [A3-08]}
  - {q: "Consolidated borrowings at 30-Sep-2025 (the deck's YoY 'lower working capital borrowings' cause is untestable without it), and which source funded the H1 FY27 working-capital increase of Rs 506.41 Mn while borrowings rose to Rs 1,319.60 Mn?", from_finding_id: [FN09, A3-03]}
  - {q: "Will the FY27 US CGU impairment test use the reduced earnout forecasts; FY26 headroom?", from_finding_id: [A3-06, FN05, FN-03]}
  - {q: "Define 'operation free cash flow' Rs 172 Mn: CFO minus capex, before or after leases?", from_finding_id: [FN10, FN-06]}
  - {q: "Q2 FY27 consolidated CFO alone, Rs Mn?", from_finding_id: [A3-08, FN-06]}
  - {q: "Share of the order book executable within 12 months?", from_finding_id: [FN-05]}
  - {q: "Q2 FY26 and Q2 FY27 cancellations, FX revaluation and re-scoping (Rs Mn) reconciling walk-implied 1.55x to stated 1.6x and walk-implied YoY intake +29.4% (4,699 to 6,079 Mn) to stated +15.4%?", from_finding_id: [FN-05]}
  - {q: "B2S / design-led share of Q2 FY27 revenue?", from_finding_id: [FN12, FN-08]}
  - {q: "Order book value from semicap, robotics and AI data center combined?", from_finding_id: [FN13, FN-08]}
  - {q: "Rs Mn value of 'purchases towards product development' in Q2 material cost?", from_finding_id: [FN02, FN-08]}
  - {q: "Does any numeric FY27 revenue growth guidance stand?", from_finding_id: [FN-07]}
  - {q: "% of USD receivables hedged at 30-Sep-2026 (FX swing (20.55) to 18.89 Mn; hedge line nil)?", from_finding_id: [A3-01, FN-02]}
  - {q: "US unused tax-loss balance and expiry behind the Rs 14.48 Mn Q2 DT credit?", from_finding_id: [A3-11]}
  - {q: "Which receivables produced the Rs 30.53 Mn standalone ECL write-back, and how much in Q2?", from_finding_id: [A3-09]}
  - {q: "Share of contract assets (Rs 581.44 Mn) unbilled over 90 days?", from_finding_id: [A3-10]}
  - {q: "Was the IP-communications investee re-valued at 30-Sep-2026; what launch date supports Note 4?", from_finding_id: [A3-02, A3-20, A3-21]}
  - {q: "Do any of the 2,63,400 options go to KMP or the new CHRO; exercise price?", from_finding_id: [A3-13]}
  - {q: "Will the company correct the Q2 FY26 consolidated employee cost (329.42 printed vs 529.42 by footing)?", from_finding_id: [A3-14]}
  - {q: "What was the Rs 83.78 Mn inflow under 'Payment towards acquisition of business' in H1 FY26?", from_finding_id: [A3-18]}
  - {q: "Date of the Altek rename; were earnout terms amended with it?", from_finding_id: [A3-19, FN14]}
  - {q: "Was the Rs 34 Mn Q3 FY26 one-off a charge in filed operating costs that the deck adds back, or a gain outside operating EBITDA; which filed line holds it (deck H2 FY26 PAT 362 vs filed 336.74 Mn)?", from_finding_id: [FN11]}
  - {q: "Q2 FY27 Auto & Others revenue (Rs Mn) and its YoY change, given Aerospace + Industrial increments of 881.7-981.0 Mn exceed the 824.56 Mn total increase?", from_finding_id: [A5-L1-N2]}
  - {q: "Q31 Which end of the FY27 9-10% EBITDA band applies; at 9% H2 runs ~8.5%, below Q2 8.69%: what holds H2 below Q2 if investment intensity falls from Q3?", from_finding_id: [CF01]}
  - {q: "Q32 Define 'contribution margin'; Q2 FY27 vs Q2 FY26 values; reconcile with the filed -381 bps gross margin", from_finding_id: [CF03]}
  - {q: "Q33 S&M cost (Rs Mn) Q2 FY27 vs Q2 FY26 and PD cost expensed in Q2 FY27 (drag sized 100-150, ~100 and 150-200 bps)", from_finding_id: [CF04, CF05]}
  - {q: "Q34 Base and year of the 'around 200 bps' expansion (audio gap); does 'from Q1 onwards double-digit' mean Q1 FY28?", from_finding_id: [CF06, CF24]}
  - {q: "Q35 Is the FY27 double-digit B2S share target withdrawn; H1 FY27 B2S share?", from_finding_id: [CF07]}
  - {q: "Q36 Signed vs unsigned value of the ~$1 bn across four B2S programmes; which customers?", from_finding_id: [CF08]}
  - {q: "Q37 Date of the $1.4 bn unweighted pipeline figure and weighted value of the ~$1.5 bn (rise stated cc L338-L339; loop 1 revised)", from_finding_id: [CF09]}
  - {q: "Q38 Component categories limiting conversion; dated inventory-days and NWC-days targets", from_finding_id: [CF11]}
  - {q: "Q39 Residual earnout open for Q2 FY28 (deck: reversal in both Q2s); Q2 FY27 export-incentive amount (Rs Mn)", from_finding_id: [CF12]}
  - {q: "Q40 Semicap revenue (Rs Mn) in Q1 and Q2 FY27; semicap order book", from_finding_id: [CF18]}
  - {q: "Q41 Will PD stay fully expensed through FY28; would a switch be disclosed with its EBITDA effect?", from_finding_id: [CF20]}
  - {q: "Q42 Date for the Honeywell build-to-print programme's return to serial production", from_finding_id: [CF21]}
monitorables:
  - {item: "Role 5 on the 15-Oct-2026 call transcript; mark question answer status (Role 5 addendum: DONE 2026-10-18)", implied_date: "now", source_ref: "orchestrator note; Step 8.5"}
  - {item: "Operator ruling on NWC basis and H1 cash-falsifier print", implied_date: "Halt 1 (ND)", source_ref: "Notion open rulings; FN08; A3-08"}
  - {item: "Q3 FY27 cons gross margin vs 40.05% bull / 37.41% bear; combined opex ratio vs H2 FY26 29.55%; subs EBITDA; standalone borrowings", implied_date: "about mid-Jan 2027 [INFERENCE]", source_ref: "Step 8C; Step 4; A3-03; A3-05; A3-07"}
  - {item: "EXPAND margins ~11-13%", implied_date: "FY27-FY29", source_ref: "pres L150, L165 (FN17)"}
  - {item: "4 to 7 industries: semicap, robotics, AI data center", implied_date: "FY27-FY29", source_ref: "pres L153-161 (FN17)"}
  - {item: "TRANSFORM margins ~13-18% (B2S)", implied_date: "FY30+", source_ref: "pres L165 (FN17)"}
  - {item: "Outlook 'positive for the year' (no figure)", implied_date: "31-Mar-2027", source_ref: "pr L107 (FN-07)"}
  - {item: "ICRA AA- Stable surveillance", implied_date: "about Mar 2027 [INFERENCE]", source_ref: "Notion properties (AGENCY)"}
  - {item: "Q4 FY27 audited: formal cash-falsifier print; US CGU impairment test; standalone debt at 31-Mar-27", implied_date: "about Apr-May 2027 [INFERENCE]", source_ref: "A3-06; FN05; Notion test 1"}
  - {item: "FY27 AR: RPT to Cyient Ltd; US AOC-1; earnout residual; US DTA", implied_date: "about Jun-Jul 2027 [INFERENCE]", source_ref: "Notion test 5; A3-06; A3-11"}
  - {item: "US subsidiary current borrowings Rs 671.80 Mn refinance or repay", implied_date: "by Sep 2027", source_ref: "res L170, L177 (A3-08)"}
  - {item: "Q1 FY28: entry to 11-13% band; new-vertical revenue", implied_date: "about late Jul 2027 [INFERENCE]", source_ref: "FN17; FN13"}
  - {item: "IP-communications investee value recovery as products launch", implied_date: "over the next few years (undated)", source_ref: "res L291 (A3-20)"}
  - {item: "ESOP/RSU grant terms (273,400 units)", implied_date: "granted 2026-10-15; vesting NOT FOUND", source_ref: "res L42-43 (A3-13)"}
  - {item: "CHRO Sandip Mishra appointment", implied_date: "effective 2026-10-15; term NOT FOUND", source_ref: "res L39-40, L486-487"}
  - {item: "Altek integration and rename", implied_date: "completed Q2 FY27", source_ref: "pres L192; pr L103-104"}
  - {item: "Q2 FY28 base effect of Rs 18.20 Cr earnout in Q2 FY27 PAT", implied_date: "about Oct 2027", source_ref: "FN05"}
  - {item: "H2 FY27 revenue >= 874.15 Cr (H2 pledge), ~437 Cr a quarter; Q3 30% bar 394.29 Cr is +0.3% QoQ on the weaker H2 base, so a Q3 at the bar leaves Q4 needing 479.86 Cr (+21.7% QoQ; +30.0% YoY; the same QoQ step Q4 FY26 made, Step 3); restate Q4 after Q3 (loop 1 revised; loop 2)", implied_date: "Q3 about mid-Jan 2027; Q4 about Apr-May 2027 [INFERENCE]", source_ref: "cc L361; res L538; pres L247-L249 (P09)"}
  - {item: "Order intake 600 Cr plus in Q3 and Q4 FY27 (book walk >= Rs 6,000 Mn each; hedged probably, cc L256; reached once in five walk quarters, H2 needs about 50% above H2 FY26 797.9 Cr [INFERENCE], P10; loop 2)", implied_date: "Q3 and Q4 FY27", source_ref: "cc L256 (P10)"}
  - {item: "Investment intensity lower: combined opex ratio below Q2 28.72%; absolute co-reading vs Q2 FY27 combined 1,128.89 Mn: at ~437 Cr a quarter the ratio passes with expenses up to ~1,255 Mn (+11.2% QoQ) [INFERENCE], so a ratio pass alone re-credits P09 and does not test no future investment in that area (cc L297) (loop 2)", implied_date: "Q3 or Q4 FY27", source_ref: "cc L295, L297; res L543, L546 (P07)"}
  - {item: "No net new S&M until quarterly revenue ~Rs 7,862 Mn", implied_date: "every quarter, open-ended", source_ref: "cc L288, L297 (P06)"}
  - {item: "FY27 EBITDA margin 9-10% (at 9% H2 ~8.5% [INFERENCE])", implied_date: "about Apr-May 2027 [INFERENCE]", source_ref: "cc L230, L244 (P01)"}
  - {item: "AI DC and robotics update: position, opportunities, pipeline", implied_date: "Q4 FY27 call, about Apr-May 2027 [INFERENCE]", source_ref: "cc L217, L460-L461 (P15)"}
  - {item: "Semicap growth every quarter (amount not disclosed)", implied_date: "from Q3 FY27", source_ref: "cc L238, L459 (P16)"}
  - {item: "Double-digit EBITDA margin from Q1 (read Q1 FY28)", implied_date: "about late Jul 2027 [INFERENCE]", source_ref: "cc L231 (P03)"}
  - {item: "FY28 EBITDA margin double digits / 10 plus", implied_date: "FY28", source_ref: "cc L266, L476 (P02)"}
  - {item: "B2S ~$1 bn into order book after design/prototype; production FY29, full ramp FY30", implied_date: "undated / FY29-FY30", source_ref: "cc L309-L310, L409-L411, L428-L429 (P13, P14)"}
  - {item: "Honeywell build-to-print programme back to serial production", implied_date: "undated", source_ref: "cc L405-L407 (P21)"}
  - {item: "PD fully expensed; any capitalisation is a tripwire", implied_date: "ongoing", source_ref: "cc L199, L389-L391, L473 (P22)"}
  - {item: "Pipeline $1.5 bn unweighted; win ratio ~40%; $400-500 Mn order impact", implied_date: "undated", source_ref: "cc L262, L332, L338 (P12)"}
  - {item: "More US revenue traction; large orders from the new sales team", implied_date: "undated", source_ref: "cc L439, L478-L479 (P18, P20)"}
  - {item: "Growth sustains into FY28", implied_date: "FY28", source_ref: "cc L56, L298-L299 (P24)"}
flags:
  - "EARNINGS QUALITY: earnout write-back Rs 181.95 Mn = 53.5% of cons Q2 PAT and 46.3% of PBT; second Q2 in a row (Rs 195.75 Mn in Q2 FY26); normalized PAT +25.85% is about 89% FX (38.55 Mn swing, about 28.85 Mn after tax, of the 32.49 Mn gain); ex-earnout ex-FX PBT +1.9% (188.56 to 192.17 Mn); Q2 ex-earnout ETR 31.95% before a 14.48 Mn US deferred-tax credit (9.2% of normalized PAT; normalized PAT +18.0% YoY without it, about -5.1% ex FX and ex the credit); the 17.33 Mn H1 FY26 subsidiary credit reversed as a 24.35 Mn H2 FY26 charge; a Q2-annualised A21 base carries 5.79 Cr of the credit, so TTM is the cleaner base"
  - "US ARM: subsidiary op EBITDA Rs 11.51 Mn (1.17%) in Q2 vs 57.43 Mn in Q1; PBT ex-earnout (50.41) Mn; goodwill + intangibles Rs 1,178.91 Mn (11.0% of equity) face an FY27 impairment indicator; acquisition probe: consideration NOT FOUND, carrying value about 5.4x subs TTM op EBITDA 217.37 Mn (about 25.6x on Q2 annualised), TTM PAT ex-earnout (18.17) Mn, earnout write-backs 377.70 Mn = 32.0% of carrying value, subs net debt 961.79 Mn = 4.4x"
  - "INDIA ENTITY: standalone PAT +43.18% is FX-assisted; FX swing 38.43 Mn = 48.7% of the 78.99 Mn PBT gain; ex-FX PBT +20.1% vs revenue +25.1%; standalone gross margin -435 bps; H1 standalone CFO 0.07x PAT"
  - "GROSS MARGIN: cons 37.41% vs 41.22% YoY (-381 bps); third compression on Notion's count; cause given is mix and product development, not component cost; deck opex attribution contradicted by YoY cost ratios; QoQ opex gave 125 of the 178 bps op EBITDA margin fall (other expenses +17.7% on revenue +5.2%), so the YoY opex leverage has two readings (Q2-seasonal opex vs a Q2 FY26 spike partly reversing), separated by the Q3 FY27 combined opex ratio vs H2 FY26 29.55%"
  - "REVENUE BREADTH: Aerospace + Industrial increments 881.7-981.0 Mn exceed the 824.56 Mn YoY increase; the other 22% of revenue shrank 6-15%; Auto & Others fell sharply, value NOT DISCLOSED [INFERENCE]"
  - "PROOF GATE NOT FIRED: margin leg -135 bps YoY (H1 +1 bp); design-led share NOT DISCLOSED"
  - "CASH INDETERMINATE-WITH-DIRECTION (structural): H1 cons CFO/PAT 0.29x, standalone 0.07x; NWC basis unresolved (filing 189.0 d TTM, deck 153, Notion 169); H1-falsifier ruling pending"
  - "DEBT: standalone new current borrowings Rs 287.91 Mn; subs current borrowings Rs 671.80 Mn from 283.00; group net cash Rs 226.38 Mn from 396.75; gross borrowings +24.3% in H1 put the 64 bps finance-cost leg of the below-EBITDA offset at risk; the deck's YoY 'lower working capital borrowings' cause is untestable (30-Sep-2025 balance NOT FOUND) and H1 FY26 repayments fit it"
  - "ORDER BOOK: walk-implied book-to-bill 1.55x does not tie to stated 1.6x; residual Rs 14-407 Mn across rounding; stated intake +15.4% YoY vs walk-implied +29.4% (4,699 to 6,079 Mn); the stated rate needs 568-751 Mn of undisclosed Q2 FY26 book reductions"
  - "A21 BASE: TTM ex-earnout PAT 65.78 Cr on the filed basis is two-sided, about 63.2-68.3 Cr, on the Q3 FY26 34 Mn one-off; deck H2 FY26 PAT 362 vs filed 336.74 Mn favours a charge the deck adds back; TTM preferred over a single quarter, which annualises the US deferred-tax credit"
  - "DATA DEFECTS: cons Q2 FY26 employee 329.42 misprint (529.42 by footing and deck L377); standalone HY basic EPS 4.35 read defect (4.55); R451 belongs to HY Sep-25; A2 press R036 rename reversed"
  - "PIPELINE: A3 presentation FN04 FY26 margin denominator typo (12,614 not 14,614; deck FY26 margin 10.3%); A3 presentation 1.55x-ties-1.6x claim wrong (FN-05 governs)"
  - "TRACKER: zero downstream signals on file, below the three-signal floor; four candidates emitted"
  - "Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); pillar facts flagged; trailing PE 92.5x reported vs 118.1x ex-earnout at memory CMP 979"
  - "Role 5 addendum complete 2026-10-18 (machine transcript, speakers inferred); verdict unchanged"
  - "CALL vs FILING, MARGIN CAUSE: chairman (T039, inferred) says gross/contribution margin higher YoY, 'not the revenue mix' (cc L282-L284); filing GM -381 bps, combined opex ratio -245 bps; deck names revenue mix (pres L374-L375)"
  - "EARNOUT LABEL: 'one-time' Rs 182 Mn (cc L133, L163) vs deck 'both Q2 FY26 and Q2 FY27' (pres L384-L385); CFO omitted it when asked if Q2 other income recurs (cc L464-L465); 80.5% of Q2 other income (res L288, L539; loop 1 rounding fix)"
  - "GUIDANCE ARITHMETIC: FY27 ~9% / 9-10% on 30-35% growth needs H2 8.51-8.54% at 9% (below Q2 8.69%), 10.36-10.38% at 10% [INFERENCE]; conflicts with 'intensity lower from Q3 or Q4' (cc L295)"
  - "PROOF GATE TIMELINE: B2S production FY29 'probably', full ramp FY30 (cc L428-L429); FY27 double-digit B2S target unanswered (cc L376): DROPPED candidate; share leg cannot fire before FY29-FY30 [INFERENCE]; EXPAND band missed in FY27, entry unguided, FY28 earliest (loop 1)"
  - "US ARM: 'doing as per our plans' (cc L438) vs subsidiary op EBITDA 1.17% and second earnout write-back"
  - "NOTION TEST 2: no component-cost answer; stated cause changed across three calls (April, July per Notion memory; October: Q2 mix and product development, full-year S&M; loop 1: scope, not a CFO-chairman conflict)"
  - "HEDGE-HEAVY: 11 protocol-listed defensive phrases plus 12 'probably'; specificity 0.55 raw / 0.48 de-dup; archetype UNCLASSIFIED"
  - "ANALYST COVERAGE: 8 of 10 slots asked; large-broker slot dropped; no question on CFO, debt build, gross margin figure or parent RPT"
  - "PIPELINE DIRECTION (loop 1 corrected): rose $1.4 bn to ~$1.5 bn unweighted (chairman, cc L338-L339; T053 low confidence); CEO 'going up' (cc L330), 'more than a billion' restates the floor (cc L331, L33); date of 1.4 and weighted value open (Q37)"
  - "ACCOUNTING OPTION: PD fully expensed, option to capitalise retained (cc L389-L391); a switch could meet the proof-gate margin leg through accounting (tripwire candidate)"
  - "SOURCE: machine transcript, inferred speakers; S&M freeze pledge and contribution-margin claim rest on inferred chairman attribution (T039)"
  - "TRACK RECORD: no prior concall log; credibility ratio and Role 1 track-record input ND until the Q3 FY27 call scores the 24-row baseline log"
plain_language_brief_included: true
role5_verdict: "PROCEED WITH FLAGS (unchanged); concall impact WEAKENED; credibility ND (baseline log); archetype UNCLASSIFIED"   # Role 5 addendum
answer_status_counts: {ANSWERED: 1, PARTIALLY: 4, EVADED: 4, NOT_ADDRESSED: 21}   # Role 5 addendum, loop 1: Q10 and Q28 regraded
new_question_ids: [Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40, Q41, Q42]   # Role 5 addendum
oi_1_corrected: true   # Role 5 addendum
analyst_note: "Pre-thesis read, so no condition can fire and 8A-W yields no entry-zone change. India grew revenue 25.1% at an 11.2% margin, but half its PBT gain is FX. The US arm earned 1.17% EBITDA and lost money before a second Q2 earnout write-back, 53.5% of reported PAT. Normalized PAT +25.85% is about 89% FX, and a 14.48 Mn US deferred-tax credit also lifts it; ex both it fell about 5.1%. YoY the margin drop is materials (gross margin -381 bps); QoQ opex gave 125 of 178 bps. So Q3 FY27 reads gross margin with the combined opex ratio against 29.55%, which separates seasonal Q2 opex from a reversing Q2 FY26 spike. Aerospace and Industrial gave more than all of the revenue increase; Auto & Others fell, value NOT DISCLOSED. TTM ex-earnout PAT (63.2-68.3 Cr) is the cleaner A21 base; a Q2-annualised base carries 5.79 Cr of a tax credit type that reversed last H2. Loop 2 dropped the deck-vs-balance-sheet conflict: the YoY finance-cost cause is untestable without the 30-Sep-2025 balance, but the H1 debt build puts the finance-cost leg at risk. Cash is directionally structural; the NWC basis is unresolved."
role5_analyst_note: "Machine transcript, inferred speakers; the filing wins. The chairman says gross and contribution margin rose YoY; the filing shows gross margin down 381 bps in Q2 and 307 bps in H1. He scopes the mix to Q2, as the deck does; his 'not a one-off' is the S&M and PD drag, and PD 'going on for a while' makes repeat PD purchases likely, against the deck on that leg [INFERENCE]. The earnout is called one-time; the deck shows one in both Q2s, and the CFO omitted it when asked if Q2 other income recurs. The US business is called on plan at 1.17% subsidiary EBITDA. The FY27 guide reconciles only near 10%. FY28 is guided at a 10% floor, so EXPAND entry is unguided. The pipeline rose to about $1.5 bn unweighted (low confidence). B2S revenue moves to FY29-FY30. Positives to test: H2 revenue of 874.15 Cr or more (at the Q3 bar, Q4 needs the +21.7% step Q4 FY26 made), 600 Cr intake a quarter (hedged 'probably'; met once in five walk quarters, P10), and full PD expensing. The S&M pledge covers net new cost only and has no base. Credibility stays ND until Q3 FY27."   # Role 5 addendum, loop 1; loop 2 (196 words)
review_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\cyientdlm-q2fy27\\work\\review_cyientdlm_q2fy27.md"
```
