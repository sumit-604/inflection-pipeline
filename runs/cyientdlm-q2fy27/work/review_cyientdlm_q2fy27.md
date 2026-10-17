# A4 MERGED REVIEW: Cyient DLM Ltd (CYIENTDLM) | Q2 FY27 (quarter and half year ended 30-Sep-2026)

Agent: A4 analyst | Model: claude-opus-5-5 | Run date: 2026-10-17
Protocol loaded: Quarterly Results Review Protocol v1.4 (Role 4) only. Role 5 not run: the 15-Oct-2026 call transcript is not in this run.
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
- Bull threshold: Q3 FY27 gross margin at or above 40.05% (the H2 FY26 average). That proves the Q2 mix effect was one-off, as management says (pres L374).
- Bear threshold: Q3 FY27 gross margin at or below 37.41% (the Q2 FY27 level) with Box Build share at or above 37%. That proves material intensity rises with the strategy itself (FN02 reading b). The 11-13% EXPAND target would then need a lever the deck does not name.
- Co-reading (A5 loop-1 N1): the consolidated combined opex ratio against the H2 FY26 average of 29.55% (Q1 FY27 27.47%, Q2 FY27 28.72%; res L538, L543, L546). Below 29.55% supports Step 4 reading (a): seasonal Q2 opex, so the YoY leverage recurs. At or above 29.55% supports reading (b): the YoY leverage was a Q2 FY26 base spike and is reversing. Gross margin alone cannot carry the Q3 test, because opex gave 125 of the 178 bps QoQ margin fall.
Why this metric: the margin leg of the proof gate, Notion test 2, and the EXPAND target all run through it. Cash (test 1) waits on a basis ruling; the order book (test 3) is already green.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to at least one question below (coverage list after the table). Ordered by thesis materiality. Q1-Q8 are the protocol's core 5-8 set.

| # | Cat | Question | Why It Matters | Bull Answer | Bear Answer | From finding(s) |
|---|---|---|---|---|---|---|
| 1 | E | What is the remaining earnout (contingent consideration) liability at 30-Sep-2026, in Rs Mn, after the Rs 181.95 Mn gain in Note 3(ii)? | The gain is 53.5% of Q2 PAT and recurs each Q2; a residual sets the next write-back or payout | Nil or small; the earnout window is closed | A residual large enough to allow another write-back in Q2 FY28 | A3-06, A3-16, FN05, FN-03 |
| 2 | A | By what % did the acquired US business miss the earnout metric that triggered the Rs 181.95 Mn write-back? | A miss is an Ind AS 36 impairment indicator for 117.89 Cr of goodwill and intangibles | Small miss on a timing metric | Large miss on revenue or EBITDA | A3-04, A3-06, FN05, FN-03 |
| 3 | A | What was Cyient DLM Electronics Inc. (ex-Altek) EBITDA in Q2 FY27, in Rs Mn? Consolidated minus standalone EBITDA fell to Rs 11.51 Mn (1.17%) from Rs 57.43 Mn in Q1. | Separates the acquired unit from the other US subsidiary and from eliminations | Positive and near the Q1 level; the drop is an elimination effect | Negative; the acquired unit is loss-making | A3-05, A3-04, FN14 |
| 4 | C | Of the 381 bps YoY drop in consolidated gross margin (41.22% to 37.41%), how many bps came from component price inflation, and how many from Box Build mix? | Notion test 2 asks for a component-cost answer; the deck gives mix and product development, and its p11 opex cause conflicts with a 245 bps YoY opex ratio fall (QoQ it fits: opex gave 125 of the 178 bps fall) | Mostly one-off purchases; component cost flat | Mostly Box Build mix: structural to the strategy | FN01, FN02, FN03, A3-07, FN-01 |
| 5 | B | The deck sets ~11-13% margins for FY27-29 (p7). Is that EBITDA margin, and in which fiscal year does management expect to enter the band, given H1 FY27 at 9.6%? | The only dated margin target; Role 5 promise-vs-delivery anchor | EBITDA; entry in FY28 with named levers | Undefined metric, or entry pushed to FY29 | FN04, FN17, FN-08 |
| 6 | D | What formula produces the deck's NWC of 153 days for Q2 FY27, and what does that formula give for FY26? | The cash falsifier (test 1) cannot score until the basis is fixed; Notion's 169 matches neither basis | A formula that reproduces 169 for FY26 | Notion's 169 is on a third basis; the test must be rebuilt | FN08, A3-08 |
| 7 | F | Standalone took Rs 287.91 Mn of new short-term borrowings in H1 to fund a Rs 434.34 Mn inventory build. What peak balance of standalone short-term borrowings does the company plan by 31-Mar-2027? | Tests whether India growth now needs debt funding | Repaid by Q4 from collections | Rising further through H2 | A3-03, FN09 |
| 8 | D | What share of the Rs 28,137 Mn order book carries customer advance terms today, against a year ago? Customer advance days fell from 33 to 13. | Separates growth-induced from structural WC | Advances return as new programmes mobilise | New orders carry no advances; WC per rupee of revenue rises | FN07, A3-10 |
| 9 | F | About Rs 278 Mn of US term debt moved to current in H1. Is the US facility due within 12 months, and will it be refinanced or repaid from India cash? | 12-month refinancing need on a loss-making unit | Refinanced on existing terms | Repaid from India cash; group net cash falls further | A3-08 |
| 10 | F | Finance cost fell 10.4% YoY, which the deck credits to "lower working capital borrowings". What were consolidated borrowings at 30-Sep-2025, and which source funded the H1 FY27 working-capital increase of Rs 506.41 Mn while borrowings rose to Rs 1,319.60 Mn from Rs 1,061.25 Mn? | The deck's YoY cause cannot be tested: the 30-Sep-2025 balance is NOT FOUND. H1 FY26 repayments (992.96, 746.72 Mn) and a 33% fall in interest paid (143.09 to 95.86 Mn) fit it; the H1 FY27 build (gross borrowings +24.3%) points to higher finance cost from Q3 [INFERENCE] | Internal cash; borrowings are US refinancing only | Debt; finance cost rises from Q3 | FN09, A3-03 |
| 11 | D | Will the FY27 impairment test of the US cash-generating unit (goodwill Rs 730.94 Mn plus intangibles Rs 447.97 Mn) use the reduced earnout forecasts, and what headroom did the FY26 test show? | Two earnout write-backs vs rising goodwill (FX) | Large headroom on the reduced forecast | Thin headroom; impairment risk at Q4 FY27 | A3-06, FN05, FN-03 |
| 12 | D | Define "operation free cash flow" of Rs 172 Mn (p12): is it CFO minus capex, before or after lease payments? | H1 consolidated CFO minus capex is only Rs 4.11 Mn; Q1 would then be about Rs (168) Mn on the same basis [INFERENCE] | CFO minus capex after leases | Excludes working capital or leases | FN10, FN-06 |
| 13 | D | What was Q2 FY27 consolidated CFO alone, in Rs Mn? | Only H1 CFO (Rs 147.51 Mn) is filed; the "improvement" claim has no comparator | Q2 CFO above Rs 150 Mn | Q2 CFO near zero or negative | A3-08, FN-06 |
| 14 | A | What share of the Rs 28,137 Mn order book is executable within 12 months? | "Strong revenue visibility" (pr L81) depends on it; the book is 1.95 years of TTM revenue | Above 60% | Below 40%, or framework/LTA values included | FN-05 |
| 15 | A | The book walk implies Q2 FY27 intake of Rs 6,079 Mn (1.55x) vs a stated 1.6x, and Q2 FY26 intake of Rs 4,699 Mn, so YoY intake growth of +29.4% vs the stated +15.4% (pr L94). What were the Q2 FY26 and Q2 FY27 cancellations, FX revaluation and re-scoping, in Rs Mn? | Neither the stated ratio nor the stated YoY intake growth ties to the book; +15.4% needs Rs 568-751 Mn of undisclosed Q2 FY26 book reductions | Small FX revaluation only, or stated intake is on a different (gross) basis | Cancellations or de-scoping in the Q2 FY26 book | FN-05 |
| 16 | E | What % of Q2 FY27 revenue came from B2S (design-led) work? | Proof gate share leg; the deck hides B2S inside "Others" | 10% or more | Low single digits | FN12, FN-08 |
| 17 | B | How much of the Rs 28,137 Mn order book comes from semicap, robotics and AI data center combined? | The "+3 new" industries carry no revenue or order line; semicap is carved from "Industrial/Semicon" | A named, material order value | Nil or immaterial | FN13, FN-08 |
| 18 | C | What is the Rs Mn value of "purchases towards product development" inside Q2 FY27 material cost? | Splits one-off cost from mix | A large one-off amount | A small amount; the drop is mix | FN02, FN-08 |
| 19 | B | Does any numeric FY27 revenue growth guidance stand? | "Positive on the outlook for the year" names no figure or year | A reaffirmed figure | No figure; earlier guidance withdrawn | FN-07 |
| 20 | D | What % of USD receivables was hedged at 30-Sep-2026? Net FX swung from Rs (20.55) Mn in Q1 to Rs 18.89 Mn in Q2 (standalone), and the cash-flow-hedge line is nil in FY27. | Undesignated FX flows into PBT; standalone PBT ex-FX is flat QoQ | A policy hedge ratio is in place | Unhedged; PBT carries FX volatility | A3-01, FN-02 |
| 21 | D | The subsidiaries booked a Rs 14.48 Mn deferred-tax credit in Q2 on losses. What is the US unused tax-loss balance and its expiry? | DTA on a loss-making unit can reverse, as it did in H2 FY26 | Long-dated losses with a profit plan | Short-dated; reversal risk | A3-11 |
| 22 | D | Which receivables produced the H1 standalone ECL write-back of Rs 30.53 Mn, and how much of it was booked in Q2? | 4.6% of standalone H1 EBITDA; line and quarter NOT FOUND | Specific recoveries, booked in Q1 | Model release booked in Q2 | A3-09 |
| 23 | D | What share of contract assets (Rs 581.44 Mn, +32.7%) is unbilled for more than 90 days? | Over-time recognition vs slow billing | Under 10% | Over 25% | A3-10 |
| 24 | A | Was the IP-communications investee re-valued at 30-Sep-2026, and on what product launch date does Note 4's recovery view rest? | FVOCI line nil in FY27 after Rs (207.16) Mn in FY26; the commitment is undated | Re-valued; launch dated | Not re-valued; launch undated | A3-02, A3-20, A3-21 |
| 25 | G | Do any of the 2,63,400 options granted on 15-Oct-2026 go to KMP or the new CHRO, and at what exercise price? | Grant terms are unstated | None to KMP; market price | KMP grants at face value | A3-13 |
| 26 | G | Consolidated Q2 FY26 employee cost prints Rs 329.42 Mn but the expense lines foot only at Rs 529.42 Mn. Will the company file a corrected statement? | Filing data integrity | Acknowledged misprint, corrected | No response | A3-14 |
| 27 | G | What was the Rs 83.78 Mn inflow under "Payment towards acquisition of business" in H1 FY26? | An inflow under an acquisition line suggests a purchase-price refund [INFERENCE] | Working-capital true-up | Seller refund on missed performance | A3-18 |
| 28 | G | What was the date of the Altek rename, and were the earnout terms amended at the same time? | The rename coincides with the second write-back | Rename after earnout close; terms unchanged | Terms amended with the rename | A3-19, FN14 |
| 29 | A | Was the Rs 34 Mn one-off in Q3 FY26 EBITDA (p11) a charge inside filed operating costs that the deck adds back, or a gain booked outside operating EBITDA? Which filed line holds it? | Deck H2 FY26 PAT 362 Mn exceeds filed 336.74 Mn by 25.26 Mn, about the one-off after tax (25.44 Mn); the answer sets the TTM ex-earnout base at about 68.3 or 63.2 Cr | A one-off charge in filed costs; normalized base about 68.3 Cr | A gain in filed other income; normalized base about 63.2 Cr | FN11 |
| 30 | A | What was Q2 FY27 revenue from Auto & Others, in Rs Mn, and its YoY change? By the p12 shares and growth rates, Aerospace and Industrial gave Rs 881.7-981.0 Mn of growth against a Rs 824.56 Mn total increase. | Revenue breadth: the other 22% of revenue shrank 6-15% in aggregate while Defence grew 13% and Med Tech 14%, so Auto & Others fell sharply [INFERENCE] | A small slice; one programme ended | A lost customer, or a structural exit from Auto | A5 loop-1 N2 (pres L334-L362; res L538) |

Coverage check (every FORWARD-SIGNAL / AMBIGUOUS finding has a question): results A3-01 (Q20), A3-02 (Q24), A3-03 (Q7, Q10), A3-04 (Q2, Q3), A3-05 (Q3), A3-06 (Q1, Q2, Q11), A3-07 (Q4), A3-08 (Q6, Q9, Q13), A3-09 (Q22), A3-10 (Q8, Q23), A3-11 (Q21), A3-13 (Q25), A3-14 (Q26), A3-16 (Q1), A3-18 (Q27), A3-19 (Q28), A3-20 (Q24), A3-21 (Q24). Presentation FN01 (Q4), FN02 (Q4, Q18), FN03 (Q4), FN04 (Q5), FN05 (Q1, Q2, Q11), FN07 (Q8), FN08 (Q6), FN09 (Q7, Q10), FN10 (Q12), FN11 (Q29), FN12 (Q16), FN13 (Q17), FN14 (Q3, Q28), FN17 (Q5). Press release FN-01 (Q4), FN-02 (Q20; partly answered from the filing in Step 4), FN-03 (Q1, Q2, Q11), FN-05 (Q14, Q15), FN-06 (Q12, Q13), FN-07 (Q19), FN-08 (Q5, Q16, Q17, Q18). NEUTRAL-FACT findings (A3-12, A3-15, A3-17, FN06, FN15, FN16, FN18, FN-04) are incorporated in the tables above; they need no question. Q30 comes from the A5 loop-1 counter N2, not from an A3 finding.

Top 3 by likelihood of thesis-changing information:
- Q4 (gross margin split): a "mostly Box Build mix" answer moves weight to the bear case; it says the strategy itself compresses margin.
- Q2 (earnout miss size): a large miss confirms the bear case on the US arm and points to a Q4 FY27 impairment.
- Q6 (NWC formula): tests transparency. A precise formula that reproduces FY26 is a good sign. A vague answer is itself diagnostic.

Channel recommendation: the 15-Oct-2026 concall has already occurred. Its transcript is not in this run. First run Role 5 on the transcript and mark each question ANSWERED / PARTIALLY / EVADED / NOT ADDRESSED. Send the remainder by IR email with the questions verbatim.

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
| 1 | Role 5 on the Q2 FY27 earnings call transcript (questions answer-status) | now (call held 15-Oct-2026; transcript not in run) | Orchestrator note; Step 8.5 |
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

---

## PROTOCOL VERDICT

PROCEED WITH FLAGS.
Reasons: the filing is clean (unmodified limited review) and every table is filled or ND, so the review is complete. Cash conversion is INDETERMINATE-WITH-DIRECTION (structural), which caps the verdict below PROCEED; the missing evidence is named in Step 5C. Material flags surface for the operator: earnings quality (earnout 53.5% of PAT), the US arm loss ex-earnout, a third gross-margin compression on Notion's count, the proof-gate margin leg moving the wrong way, new debt at both entities, and four filing or pipeline data defects. None is a mechanical failure, so REWORK does not apply.

---

## PLAIN-LANGUAGE BRIEF

Provenance key: FILED = this quarter's results filing; MGMT = this quarter's deck or press release; AGENCY = rating agency (via prior Notion); SECONDARY = prior Notion or peer work; INFERENCE = our reasoning. "Prior Notion" marks memory from the Notion page, not this quarter's filings.

### 1. Summary narrative
- Sales grew fast. Q2 FY27 revenue was Rs 393.09 Cr, up 26.54% on a year ago (FILED).
- Growth was narrow. Aerospace and Industrial gave more than all of the rise. The rest of the mix shrank 6-15% (INFERENCE from MGMT shares).
- Profit per rupee of sales fell. Operating EBITDA margin was 8.69%, down from 10.04% (FILED).
- Year on year, the cause is materials, not overheads. Gross margin fell to 37.41% from 41.22% (FILED). Opex fell as a share of sales (MGMT deck table).
- Quarter on quarter, overheads caused most of the fall: 125 of the 178 bps. Other expenses rose 17.7% on sales up 5.2% (FILED, derived).
- Management calls the material jump a one-off from mix and product development buys (MGMT). The same deck calls the mix shift the strategy (MGMT).
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
- Verdict: PROCEED WITH FLAGS. The operator decides at Halt 1.

### 2. Sector intelligence
- Demand is strong at the top of the market. The deck puts global EMS at $649 Bn in 2025 and $853 Bn by 2030 (MGMT, citing MarketsandMarkets).
- The company names three growth pools: AI data centres, chip-making equipment and robotics (MGMT). SEMI expects record 2026 equipment sales of $165.9 Bn (MGMT, citing SEMI).
- Aerospace is the engine this quarter: it grew 62% (MGMT). Defence grew 13%, half the company rate (MGMT).
- Aerospace and Industrial gave Rs 881.7-981.0 Mn of growth against a total rise of Rs 824.56 Mn. The other 22% of revenue shrank 6-15%, so Auto & Others fell sharply. Its value is NOT DISCLOSED (INFERENCE from MGMT shares and growth rates; FILED total).
- Component and PCB costs rose in the same window at Indian peers Kaynes and Syrma (SECONDARY, prior Notion). This quarter's material ratio rise fits that pattern, but management did not name component cost (INFERENCE).
- India's semiconductor mission incentives support local equipment work (MGMT). No filed revenue line shows this yet.
- Not disclosed: segment revenue in rupees, the chip-equipment share, and component price effects.

### 3. Business-model intelligence
- The company builds electronics to customer drawings. Build-to-print was 94% of FY26 revenue (SECONDARY, prior Notion).
- It earns a conversion margin on bought-in parts. Contracts pass input costs through (SECONDARY, prior Notion). So material cost drives margin.
- Box Build (full assemblies) grew 86% and is now 37% of revenue (MGMT). Box Build carries more bought-in material (INFERENCE). If that holds, faster Box Build growth lowers gross margin even as sales rise.
- The model needs a lot of stock. Inventory equals 177.8 days of sales on our basis, 162 days on the deck basis (FILED; MGMT).
- Customer advances fell from 33 to 13 days in four quarters (MGMT). New orders now fund less of their own stock (INFERENCE).
- The US arm (ex-Altek) adds sales but not profit so far (FILED). Goodwill and acquired intangibles of Rs 117.89 Cr ride on it (FILED).
- Model drift this quarter: margin moved away from the 11-13% target band, not toward it (FILED; MGMT target).
- Not disclosed: design-led (B2S) revenue share, US entity split, customer advance terms.

### 4. Competition intelligence
- Where it wins: certified, safety-critical work for aerospace, defence and medical customers. Anchor customers include Honeywell Aerospace and Thales (SECONDARY, prior Notion). Aerospace growth of 62% shows this lane works (MGMT). The lane is also narrow: Aerospace alone gave 57-86% of the YoY increase (INFERENCE).
- Where it is weaker: scale and cash. Top customers were 56% of consolidated revenue (SECONDARY, prior Notion). Peers Kaynes and Syrma are larger EMS players in India (SECONDARY, prior Notion).
- Design-led share is small (6% in FY26, SECONDARY, prior Notion) and is not disclosed now (FILED/MGMT silence). A design moat is not visible in the numbers.
- The US arm was bought to reach customers abroad (MGMT). Its 1.17% EBITDA margin says it does not yet compete on cost (FILED).
- Risk to watch: if peers pass on component costs faster, Cyient DLM's gross margin gap widens (INFERENCE).

### 5. Forward map (next ~10-11 months)
Make-or-break reading: Q3 FY27 consolidated gross margin, results about mid-Jan 2027 (INFERENCE date). Bull at or above 40.05%. Bear at or below 37.41% with Box Build at or above 37%. Co-reading: the combined opex ratio against the H2 FY26 average of 29.55%.

| Date | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| Now | Role 5 on the 15-Oct-2026 call | Management gives a component-cost split and an earnout residual | Questions on the earnout and margin are evaded |
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
loop_iteration: 2
docs_merged: [results, presentation]   # presentation = investor deck + press release; no concall in run
ledger_reconciliation:
  notes: 8
  turns: 0
  slides: 21
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18, A3-19, A3-20, A3-21, FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN-01, FN-02, FN-03, FN-04, FN-05, FN-06, FN-07, FN-08]
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
monitorables:
  - {item: "Role 5 on the 15-Oct-2026 call transcript; mark question answer status", implied_date: "now", source_ref: "orchestrator note; Step 8.5"}
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
  - "Role 5 pending: 15-Oct-2026 call transcript not in this run"
plain_language_brief_included: true
analyst_note: "Pre-thesis read, so no condition can fire and 8A-W yields no entry-zone change. India grew revenue 25.1% at an 11.2% margin, but half its PBT gain is FX. The US arm earned 1.17% EBITDA and lost money before a second Q2 earnout write-back, 53.5% of reported PAT. Normalized PAT +25.85% is about 89% FX, and a 14.48 Mn US deferred-tax credit also lifts it; ex both it fell about 5.1%. YoY the margin drop is materials (gross margin -381 bps); QoQ opex gave 125 of 178 bps. So Q3 FY27 reads gross margin with the combined opex ratio against 29.55%, which separates seasonal Q2 opex from a reversing Q2 FY26 spike. Aerospace and Industrial gave more than all of the revenue increase; Auto & Others fell, value NOT DISCLOSED. TTM ex-earnout PAT (63.2-68.3 Cr) is the cleaner A21 base; a Q2-annualised base carries 5.79 Cr of a tax credit type that reversed last H2. Loop 2 dropped the deck-vs-balance-sheet conflict: the YoY finance-cost cause is untestable without the 30-Sep-2025 balance, but the H1 debt build puts the finance-cost leg at risk. Cash is directionally structural; the NWC basis is unresolved."
review_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\cyientdlm-q2fy27\\work\\review_cyientdlm_q2fy27.md"
```
