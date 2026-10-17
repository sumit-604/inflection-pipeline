# A4 MERGED REVIEW: Tata Communications Limited (TATACOMM), Q2 FY27

Quarter and half-year ended 30-Sep-2026. Run type: FULL QUARTER (results filing plus earnings presentation; no concall transcript in --docs).
Protocol: Role 4, Quarterly Results Review Protocol v1.4. Role 5 not run (no concall passed).
Framing: **PRE-THESIS READ.** No Notion company page exists (live search 2026-10-17). No companies/TATACOMM.md. No spear on record. Decision Status: NONE ON RECORD.
Model: claude-opus-5-5. Reviewed 2026-10-17. Revised in correction loop 1 (A5 audit, same date); change log at the end.

Anchor convention. "L###" = line in runs/tatacomm-q2fy27/extracted/tatacomm-results-q2fy27-fulltext.md. "P-L###" = line in tatacomm-presentation-q2fy27-fulltext.md. "R####" = A1 structured row (results file unless prefixed "P-"). A3 findings carry a doc prefix: "R-A3-xx" = results forensics, "P-A3-xx" = presentation forensics (both A3 files number from A3-01). [DERIVED] = arithmetic on filed numbers, shown inline. It is never an estimate of a missing number. ND = not disclosed.

---

## LEDGER RECONCILIATION PREAMBLE

**Ledger contains 18 notes / 0 turns / 9 slides. All 18 notes, 0 turns and 9 slides reviewed.**
- Results ledger: 18 notes, 28 footnotes (+3 unresolved), 356 line-item rows, 1,260 line-item cells, 87 ZERO_STANDING cells, 3 agenda items, 11 auditor paragraphs, 132 entities, 71 dates, 32 forward rows. 1,778 of 1,778 structured IDs (R001-R1778) referenced, orphan_ids [], gate_a2 pass. Every R### row read in the structured file.
- Presentation ledger: 9 slides, 74 of 74 structured IDs (P-R001-P-R074), orphan_ids [], gate_a2 pass.
- Turns: 0 (no concall in this run).
- Unreviewed ledger rows: none.

**Findings incorporated:** R-A3-01, R-A3-02, R-A3-04, R-A3-05, R-A3-06, R-A3-07, R-A3-08, R-A3-09, R-A3-10, R-A3-11, R-A3-12, R-A3-13, R-A3-14, R-A3-15, R-A3-16, R-A3-17, R-A3-18, R-A3-19, R-A3-20, R-A3-21, R-A3-22, R-A3-23, R-A3-24, R-A3-25, R-A3-26, R-A3-27, R-A3-28, R-A3-29, R-A3-30 (R-A3-03 not used by A3); P-A3-01 to P-A3-11.

A2 flags with no finding (reviewed, no finding): SIGNATURE_BEFORE_MEETING_END (CEO 12:58:01 L1028, auditor 13:05:38 L1159 and 13:04:44 L1335, meeting close 13:45 L33; approval of item (i) before items (ii)-(iii) is a coherent order, per R-A3 reconciliation); ENTITY_CHANGE R1482, R1495, R1514, R1518 (all dated in FY26, context only); ANONYMISED_CLIENT P-R055, P-R056 (carried into Q30); slides 2, 3 and 9 (title, safe harbour, closing; no data).

A1 QA carried from P-A3 reconciliation: P-R026 value is wrong (5 plan levers at P-L122-128, not 6). Nine presentation rows carry 1-9 line cite offsets. None is load-bearing.

---

## STEP 0: PRE-FLIGHT

### 0A. Notion page

| Item | Value |
|---|---|
| One-line thesis | ND (no page) |
| Four-pillar destination PE | ND (no page) |
| Bear/Base/Bull projections | ND (no page) |
| Thesis-broken conditions | ND (no page) |
| Quarterly monitoring checklist | ND (no page) |
| Position size, cost basis | ND (no page) |
| **Decision Status** | **NONE ON RECORD. Verified against the orchestrator's live fetch (work/notion-thesis.md, 2026-10-17).** |
| Devil's Advocate split | ND (no page) |
| Spear line | NONE. companies/TATACOMM.md does not exist. |
| Prior-quarter Questions for Management | ND (not passed). Answer-status tracking (ANSWERED / EVADED) cannot run this quarter. This review's questions become the baseline. |

Consequence: no HOLD/ADD/TRIM/EXIT framing anywhere below. Step 8 runs the 8A-W branch in pre-thesis form.

### 0B. Units

All figures in **Rs Crores** as filed ("₹ in Crores", L508; press release "INR Crore", L1380; deck "INR Cr", P-L138). Conversion factor 1. No conversion needed.

### 0C. Share count changes

| Date | Paid-up capital (Rs Cr) | Anchor |
|---|---|---|
| 31-Mar-2026 | 285.00 | L200, L361 |
| 30-Jun-2026 | 285.02 | L200 |
| 30-Sep-2026 | 285.09 | L200, L361 |

ESOP exercise proceeds 0.09 in H1 FY27 (L481), at par. About 90,000 shares; dilution 0.03% (R-A3-17). No split, bonus, rights, QIP or buyback. **EPS share-adjusted = EPS reported.** Basic-diluted spread 0.02 in Q2 FY27 (11.96 / 11.94, L213-214).

### 0D. Notes extraction (every numbered note, consolidated and standalone)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| C-1 | Review and approval | Results limited-reviewed, approved by Board 15-Oct-2026 (L503-506). | Nil | All | None |
| C-2 table | Exceptional items | Total (36.54) Q2 FY27, (106.36) Q1 FY27, (21.00) Q2 FY26, (142.90) H1 FY27, (41.44) H1 FY26, (97.96) FY26 (L526). | As stated | All | All growth below uses pre-exceptional PBT as "core"; reported PBT shown separately |
| C-2a | Staff cost optimisation | Phased organisational changes make positions redundant; labelled a "one-time charge" (L528-531). | (36.54) Q2 FY27; (44.78) Q1 FY27; (98.26) Q2 FY26; (81.32) H1 FY27; (118.70) H1 FY26; (114.64) FY26 (L515) | Recurs in 3 of 3 quarters shown | "One-time" label conflicts with recurrence (R-A3-11). Sensitivity row in Step 1 treats it as recurring cost |
| C-2b | Gain on sale of held-for-sale assets | FY26 sale of a few properties; gain under exceptional (L532-533). | +77.26 Q2 FY26 (L517) | Q2 FY26 | Flatters Q2 FY26 reported PBT; stripped in core PBT. A 7.40 held-for-sale asset remains, with a 4.00 advance in H1 FY27 (L344, L460; R-A3-01) |
| C-2c | Labour Codes | FY26 provision 60.58; Q1 FY27 reversal 18.52 on revised actuarial estimate (L534-540). | +18.52 Q1 FY27; (60.58) FY26 (L520) | Q1 FY27; H2 FY26 | Q1 FY27 reported PBT flattered by 18.52; stripped in core PBT |
| C-2d | Fire at co-located third-party data centre | Provision for losses "basis the available information/estimate" (L541-542). | (30.10) Q1 FY27 (L522); the cash-flow line "Includes impairment" of PPE, 25.67 (L417, L495) | Q1 FY27 | One-off; true-up either way open (R-A3-12) |
| C-2e | Provision, contractual obligation | Provision on management's recoverability assessment (L543-544). | (50.00) Q1 FY27 (L524) | Q1 FY27 | One-off; counterparty unnamed; reads with credit write-offs (R-A3-13, R-A3-06) |
| C-3 | DoT demand notices | Aggregate 7,844.57 for FY2005-06 to FY2024-25, "revised over a period of time"; 7,513.71 contingent liability net of 54.18 provision; 276.68 remote (L545-562). | No P&L; contingent liability 7,513.71 | Ongoing | No growth impact; balance-sheet risk = 2.21x consolidated parent equity 3,401.18 (R-A3-09). Emphasis of matter |
| C-4 | Foreign subsidiary VAT | VAT 168.77 plus penalty 197.03 = 365.80 contingent; National Court judgment scheduled 13-Oct-2026; "the Group awaits the National Court's decision" (L563-574). | No P&L; contingent 365.80 | Ongoing; binary | Outcome not stated though the date passed 2 days before sign-off (R-A3-08). Emphasis of matter |
| C-5 | Discontinued operations | Subsidiary deconsolidated 22-Apr-2025 (stake to 11.49%); remaining stake sold in FY26 (L575-581). | Loss on sale (42.19) H1 FY26 and FY26 (L593), FCTR recycle (L597) | H1 FY26, FY26 | Total PAT H1 FY26 depressed 42.19; continuing PAT used for like-for-like. Entity = NetFoundry by date match [INFERENCE, R-A3-02] |
| C-6 | FY26 OCI gain and DTA | OCI gain 335.24 (net of DTL 73.25) from disposal of listed investments via a fund; DTA 73.25 booked in FY26 P&L against accumulated losses (L598-601). | +73.25 deferred tax credit FY26 | FY26 | FY26 ETR 30.02% flattered by 73.25 [DERIVED: ex-credit tax 504.87 = 35.11% of 1,437.89] |
| S-1 | Standalone review and approval | Same as C-1 (R1733). | Nil | All | None |
| S-a | Staff cost optimisation (standalone) | Same wording (L990-993). | (5.03) Q2 FY27; (7.62) Q1 FY27; (2.35) Q2 FY26; (11.15) FY26 (L972) | Recurs | Most of the programme sits in subsidiaries: Q2 FY27 consolidated 36.54 vs standalone 5.03 |
| S-b | Gain on held-for-sale (standalone) | Same (L994). | +77.26 Q2 FY26 (L974) | Q2 FY26 | Standalone Q2 FY26 PBT flattered by 77.26 |
| S-c | Labour Codes (standalone) | Provision 36.82 FY26; reversal 11.93 Q1 FY27 (L996-1002). | +11.93 Q1 FY27 | Q1 FY27 | Stripped in core PBT |
| S-d | Fire (standalone) | Same (L1003-1004). | (2.65) Q1 FY27 (L979) | Q1 FY27 | One-off |
| S-e | Contractual obligation (standalone) | Same (L1005-1006). | (50.00) Q1 FY27 (L981) | Q1 FY27 | The full 50.00 sits at the parent |
| S-3 | DoT demand notices (standalone) | Same as C-3 (L1008-1020). | Contingent 7,513.71 = 72.9% of standalone net worth 10,306.04 | Ongoing | Emphasis of matter |
| Reg 52(4) footnotes | Ratio movements | Asset cover up "mainly due to repayment of unsecured debentures" (L956); current ratio down "mainly due to loan repaid by subsidiary" (L957). | Standalone debt repaid 1,760.48 (L878); subsidiary loans repaid to parent 2,641.16 (L855) | H1 FY27 | Standalone leverage ratios improve while consolidated debt rises (R-A3-05). Bad-debts ratio and current ratio worsen (see 5B) |

Answers to the four note questions. (1) Notes C-2a to C-2e change every comparison; growth below runs on pre-exceptional PBT. (2) Q2 FY26 is normalised for the 77.26 gain; Q1 FY27 for the 18.52 reversal and the 80.10 of fire and contractual provisions. (3) C-2a is labelled one-time but recurs; it is treated as non-recurring in the base table and as recurring in a sensitivity row. (4) C-3, C-4 and C-6 move thesis inputs: balance-sheet risk, a binary cash event, and the tax-rate run-rate.

**Auditor opinion check.** Limited review (SRE 2410), not an audit (L1076-1082). Conclusion **unmodified**, with **two Emphasis of Matter paragraphs in the consolidated report** (para 6: DoT, 7,513.71, L1101-1105; para 7: VAT, 365.80, L1107-1109) and **one in the standalone report** (para 5: DoT, L1319-1323). Other matters: one subsidiary relied on another auditor (para 8, L1113-1123); two subsidiaries and three associates management-furnished and unreviewed (para 9, L1125-1140). Going-concern language: none. Board letter calls the review an "unmodified opinion" (L41); the auditor gives a "conclusion" (R-A3-26, drafting only). **Per protocol 0D this is an AMBER flag.**

### 0E. Business type

**Standard operating business** (global communications and digital platforms). Not a lender. Steps 1 and 5 apply. The filing has no Cost of Materials or Change in Inventories line; its principal direct cost is "Network and transmission expense" (L139), added as its own row.

Checkpoint. Notion verified (no page, no Decision Status). Units Rs Cr. Share count change 0.03%. All 18 notes extracted. Auditor: unmodified with EoM. Business type standard.

---

## STEP 1: DATA EXTRACTION

### 1A. Consolidated P&L (Rs Cr)

FY27 full year is not complete: FY27 column = ND. H1 columns added because Q2 is a half-year filing.

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | 6,099.75 | 6,582.82 | 6,687.89 | 12,059.60 | 13,270.71 | 24,802.72 | ND | L135 |
| Other Income | (17.24) | 12.94 | 16.41 | (0.14) | 29.35 | 301.73 | ND | L136 |
| Total Income | 6,082.51 | 6,595.76 | 6,704.30 | 12,059.46 | 13,300.06 | 25,104.45 | ND | L137 |
| Cost of Materials Consumed | ND | ND | ND | ND | ND | ND | ND | not a line item |
| Network and transmission expense | 2,715.35 | 3,144.09 | 3,181.47 | 5,444.42 | 6,325.56 | 11,361.83 | ND | L139 |
| Change in Inventories | ND | ND | ND | ND | ND | ND | ND | not a line item |
| Employee Benefits Expense | 1,269.57 | 1,239.73 | 1,178.75 | 2,487.34 | 2,418.48 | 4,938.93 | ND | L140 |
| Finance Costs | 201.96 | 185.90 | 197.91 | 378.49 | 383.81 | 761.60 | ND | L141 |
| Depreciation and amortisation | 678.78 | 739.44 | 740.94 | 1,344.47 | 1,480.38 | 2,826.74 | ND | L142 |
| Other Expenses | 941.21 | 968.86 | 905.79 | 1,817.41 | 1,874.65 | 3,679.50 | ND | L143 |
| Total Expenses | 5,806.87 | 6,278.02 | 6,204.86 | 11,472.13 | 12,482.88 | 23,568.60 | ND | L144 |
| PBT before exceptional items | 275.64 | 317.74 | 499.44 | 587.33 | 817.18 | 1,535.85 | ND | L146 |
| Exceptional items | (21.00) | (106.36) | (36.54) | (41.44) | (142.90) | (97.96) | ND | L148 |
| Profit Before Tax (reported, pre-associates) | 254.64 | 211.38 | 462.90 | 545.89 | 674.28 | 1,437.89 | ND | L150 |
| Current tax | 123.42 | 116.06 | 167.31 | 243.82 | 283.37 | 612.24 | ND | L153 |
| Deferred tax | (41.29) | (30.05) | (43.27) | (96.26) | (73.32) | (180.62) | ND | L154 |
| Tax Expense (total) [DERIVED, L153+L154] | 82.13 | 86.01 | 124.04 | 147.56 | 210.05 | 431.62 | ND | L153-154 |
| Share of associates | 10.70 | 4.35 | (3.25) | 17.21 | 1.10 | 32.77 | ND | L158 |
| PAT, continuing operations | 183.21 | 129.72 | 335.61 | 415.54 | 465.33 | 1,039.04 | ND | L160 |
| Discontinued operations | 0 (dash) | 0 (dash) | 0 (dash) | (42.19) | 0 (dash) | (42.19) | ND | L163 |
| PAT (total) | 183.21 | 129.72 | 335.61 | 373.35 | 465.33 | 996.85 | ND | L164 |
| PAT, equity holders of parent | 183.06 | 134.23 | 341.03 | 373.04 | 475.26 | 1,001.57 | ND | L166 |
| Non-controlling interest | 0.15 | (4.51) | (5.42) | 0.31 | (9.93) | (4.72) | ND | L167 |
| EPS basic, total (Rs) | 6.42 | 4.71 | 11.96 | 13.09 | 16.67 | 35.14 | ND | L213 |
| EPS basic, continuing (Rs) | 6.42 | 4.71 | 11.96 | 14.57 | 16.67 | 36.62 | ND | L207 |
| EPS diluted, total (Rs) | 6.41 | 4.70 | 11.94 | 13.06 | 16.64 | 35.08 | ND | L214 |
| EPS (share-adjusted) | 6.42 | 4.71 | 11.96 | 13.09 | 16.67 | 35.14 | ND | = reported (0C) |

Tie-check: PBT less total tax equals L156 in all six columns (e.g. 462.90 - 124.04 = 338.86, L156).

### 1B. Consolidated derived metrics

"Core" uses pre-exceptional PBT (L146) so that the C-2 one-offs do not distort growth. Reported-PBT versions are shown too.

| Derived Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | Pre-exc PBT + D + FC - OI | 1,173.62 | 1,230.14 | 1,421.88 | 2,310.43 | 2,652.02 | 4,822.46 | ND |
| Operating EBITDA Margin | Op EBITDA / Revenue | 19.24% | 18.69% | 21.26% | 19.16% | 19.98% | 19.44% | ND |
| Reported EBITDA | Reported PBT + D + FC | 1,135.38 | 1,136.72 | 1,401.75 | 2,268.85 | 2,538.47 | 5,026.23 | ND |
| Operating EBIT | Op EBITDA - D | 494.84 | 490.70 | 680.94 | 965.96 | 1,171.64 | 1,995.72 | ND |
| Core PBT (ex-OI, pre-exceptional) | Pre-exc PBT - OI | 292.88 | 304.80 | 483.03 | 587.47 | 787.83 | 1,234.12 | ND |
| Reported PBT ex-OI | Reported PBT - OI | 271.88 | 198.44 | 446.49 | 546.03 | 644.93 | 1,136.16 | ND |
| Other Income / PBT | OI / reported PBT | -6.77% | 6.12% | 3.55% | -0.03% | 4.35% | 20.98% | ND |
| Effective Tax Rate | Total tax / reported PBT | 32.25% | 40.69% | 26.80% | 27.03% | 31.15% | 30.02% | ND |
| Current-tax rate | Current tax / reported PBT | 48.47% | 54.91% | 36.14% | 44.66% | 42.03% | 42.58% | ND |
| PAT Margin (total PAT) | PAT / Revenue | 3.00% | 1.97% | 5.02% | 3.10% | 3.51% | 4.02% | ND |
| PAT Margin (parent PAT) | Parent PAT / Revenue | 3.00% | 2.04% | 5.10% | 3.09% | 3.58% | 4.04% | ND |
| Network cost / Revenue | L139 / L135 | 44.52% | 47.76% | 47.57% | 45.15% | 47.67% | 45.81% | ND |
| Employee cost / Revenue | L140 / L135 | 20.81% | 18.83% | 17.63% | 20.63% | 18.22% | 19.91% | ND |
| Other expenses / Revenue | L143 / L135 | 15.43% | 14.72% | 13.54% | 15.07% | 14.13% | 14.84% | ND |
| Sensitivity: Op EBITDA less staff-optimisation charge (if recurring, R-A3-11) | Op EBITDA + C-2a | 1,075.36 (17.63%) | 1,185.36 (18.01%) | 1,385.34 (20.71%) | 2,191.73 (18.17%) | 2,570.70 (19.37%) | 4,707.82 (18.98%) | ND |

Ties: Op EBITDA Q2 FY27 1,421.88 = press-release EBITDA 1,422 (L1385) and = revenue less L139, L140, L143. Operating EBIT equals total segment result in every column (680.94, 490.70, 494.84, 1,171.64, 965.96, 1,995.72; L247). OI Q2 FY26 is negative, so Op EBITDA there adds back 17.24.

### 1C. Standalone P&L (Rs Cr)

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | 1,802.60 | 1,838.59 | 1,854.12 | 3,625.62 | 3,692.71 | 7,375.71 | ND | L621 |
| Other Income | 67.30 | 76.00 | 73.41 | 192.02 | 149.41 | 617.74 | ND | L622 |
| Total Income | 1,869.90 | 1,914.59 | 1,927.53 | 3,817.64 | 3,842.12 | 7,993.45 | ND | L623 |
| Cost of Materials / Change in Inventories | ND | ND | ND | ND | ND | ND | ND | not line items |
| Network and transmission expense | 606.76 | 642.64 | 669.97 | 1,329.31 | 1,312.61 | 2,640.72 | ND | L625 |
| Employee Benefits Expense | 402.08 | 414.20 | 396.50 | 806.58 | 810.70 | 1,627.46 | ND | L626 |
| Finance Costs | 89.76 | 92.00 | 94.32 | 155.33 | 186.32 | 336.72 | ND | L627 |
| Depreciation | 263.90 | 270.80 | 276.18 | 512.28 | 546.98 | 1,044.26 | ND | L628 |
| Other Expenses | 343.13 | 307.68 | 316.93 | 681.79 | 624.61 | 1,359.46 | ND | L629 |
| Total Expenses | 1,705.63 | 1,727.32 | 1,753.90 | 3,485.29 | 3,481.22 | 7,008.62 | ND | L630 |
| PBT before exceptional | 164.27 | 187.27 | 173.63 | 332.35 | 360.90 | 984.83 | ND | L631 |
| Exceptional items | 74.91 | (48.34) | (5.03) | 74.90 | (53.37) | 29.29 | ND | L632 |
| Profit Before Tax | 239.18 | 138.93 | 168.60 | 407.25 | 307.53 | 1,014.12 | ND | L633 |
| Current tax | 60.16 | 37.64 | 57.59 | 123.36 | 95.23 | 315.05 | ND | L635 |
| Deferred tax | (31.92) | (3.16) | (14.85) | (63.34) | (18.01) | (94.80) | ND | L636 |
| Tax Expense [DERIVED] | 28.24 | 34.48 | 42.74 | 60.02 | 77.22 | 220.25 | ND | L635-636 |
| PAT | 210.94 | 104.45 | 125.86 | 347.23 | 230.31 | 793.87 | ND | L637 |
| EPS basic (Rs) | 7.40 | 3.66 | 4.42 | 12.18 | 8.08 | 27.86 | ND | L652 |
| EPS diluted (Rs) | 7.39 | 3.66 | 4.41 | 12.16 | 8.07 | 27.80 | ND | L653 |
| EPS (share-adjusted) | 7.40 | 3.66 | 4.42 | 12.18 | 8.08 | 27.86 | ND | = reported |

### 1D. Standalone derived metrics

| Derived Metric | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Operating EBITDA | 450.63 | 474.07 | 470.72 | 807.94 | 944.79 | 1,748.07 | ND |
| Operating EBITDA Margin | 25.00% | 25.78% | 25.39% | 22.28% | 25.59% | 23.70% | ND |
| Reported EBITDA | 592.84 | 501.73 | 539.10 | 1,074.86 | 1,040.83 | 2,395.10 | ND |
| Core PBT (ex-OI, pre-exceptional) | 96.97 | 111.27 | 100.22 | 140.33 | 211.49 | 367.09 | ND |
| Other Income / PBT | 28.14% | 54.70% | 43.54% | 47.15% | 48.58% | 60.91% | ND |
| Effective Tax Rate | 11.81% | 24.82% | 25.35% | 14.74% | 25.11% | 21.72% | ND |
| PAT Margin | 11.70% | 5.68% | 6.79% | 9.58% | 6.24% | 10.76% | ND |

Ties: PAT margins equal the Reg 52(4) net-margin line (11.70%, 5.68%, 6.79%, 9.58%, 6.24%, 10.76%; L909). Standalone Other Income is 43.54% of Q2 PBT: the parent's profit leans on treasury and intra-group interest (interest income on financial assets 86.58 in H1, L817).

### 1E. Consolidated segment table (Rs Cr)

| Segment | Rev Q2 FY26 | Rev Q1 FY27 | Rev Q2 FY27 | Rev YoY | Result Q2 FY26 | Result Q1 FY27 | Result Q2 FY27 | Result YoY | Margin Q2 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|---|---|
| Voice Solutions | 405.96 | 381.95 | 370.04 | -8.85% | 34.93 | 20.61 | 18.13 | -48.10% | 4.90% | L234, L242 |
| Data Services | 5,204.47 | 5,703.58 | 5,810.99 | +11.65% | 313.59 | 250.56 | 425.74 | +35.76% | 7.33% | L235, L243 |
| Transformation Services | 286.74 | 194.59 | 190.11 | -33.70% | 45.08 | 44.38 | 47.89 | +6.23% | 25.19% | L236, L244 |
| Real Estate | 51.85 | 51.99 | 51.84 | -0.02% | 25.66 | 28.01 | 27.15 | +5.81% | 52.37% | L237, L245 |
| Campaign Registry | 202.54 | 258.70 | 277.76 | +37.14% | 75.58 | 147.14 | 162.03 | +114.38% (depressed base; see note) | 58.33% | L238, L246 |
| Inter-segment | (51.81) | (7.99) | (12.85) | n.m. | ND | ND | ND | ND | ND | L239 |
| Total | 6,099.75 | 6,582.82 | 6,687.89 | +9.64% | 494.84 | 490.70 | 680.94 | +37.61% | 10.18% | L240, L247 |

Data Services margin: 6.03% Q2 FY26, 4.39% Q1 FY27, 7.33% Q2 FY27. Campaign Registry share of segment result: 15.27% Q2 FY26, 29.99% Q1 FY27, 23.80% Q2 FY27, on 4.15% of Q2 revenue (R-A3-20). Standalone segments: Voice result (27.02) Q2 FY27 (L675); Data Services result 182.87 (L676).

**Campaign Registry base effect (A5 M1).** The +114.38% YoY rests on a depressed base quarter. Q1 FY26 result was 122.93 on revenue 189.38 [DERIVED: H1 FY26 198.51 - 75.58, L246; 391.92 - 202.54, L238], a 64.91% margin. Q2 FY26 result fell 38.5% QoQ to 75.58 (37.32% margin) while revenue rose. Against Q1 FY26, Q2 FY27 result is +31.8%, and its 58.33% margin is still below Q1 FY26's 64.91%. Trend figures: H1 FY27 vs H1 FY26 result +55.75% (198.51 to 309.17, L246); QoQ +10.1% (147.14 to 162.03). Campaign Registry share of segment result was already 26.09% in Q1 FY26 [DERIVED: 122.93 / 471.12]. Perimeter: Campaign Registry Inc (Canada) left consolidation on 14-Jan-2026 (L1245, R1508), so YoY is not like-for-like; its effect is ND. **H1/H1 +55.75% is the trend figure used below.**

Checkpoint. Every cell filled or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

### 2A. Consolidated

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 6,099.75 | 6,687.89 | +588.14 / +9.64% | Positive |
| Operating EBITDA | 1,173.62 | 1,421.88 | +248.26 / +21.15% | Positive; about half is cost-out (see diagnostic 2) |
| Operating EBITDA Margin | 19.24% | 21.26% | +202 bps | Positive; gross spread fell 305 bps |
| Depreciation | 678.78 | 740.94 | +62.16 / +9.16% | In line with revenue |
| Finance Costs | 201.96 | 197.91 | -4.05 / -2.01% | Flat; lags the debt rise |
| EBIT (operating) | 494.84 | 680.94 | +186.10 / +37.61% | Positive |
| Other Income | (17.24) | 16.41 | +33.65 / n.m. | Swing helps reported PBT |
| **Core Operating PBT (pre-exc, ex-OI)** | 292.88 | 483.03 | **+190.15 / +64.92%** | Positive at group level; subsidiary-driven |
| Reported PBT | 254.64 | 462.90 | +208.26 / +81.79% | Positive |
| PAT (total) | 183.21 | 335.61 | +152.40 / +83.18% | Positive |
| PAT (parent) | 183.06 | 341.03 | +157.97 / +86.29% | Positive |
| EPS (share-adjusted, basic) | 6.42 | 11.96 | +5.54 / +86.29% | Positive |

### 2B. Standalone

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue | 1,802.60 | 1,854.12 | +51.52 / +2.86% | Slow |
| Operating EBITDA | 450.63 | 470.72 | +20.09 / +4.46% | Slow |
| Op EBITDA margin | 25.00% | 25.39% | +39 bps | Flat |
| Core PBT (pre-exc, ex-OI) | 96.97 | 100.22 | +3.25 / +3.35% | Flat |
| Reported PBT | 239.18 | 168.60 | -70.58 / -29.51% | Base flattered by +77.26 gain |
| PAT | 210.94 | 125.86 | -85.08 / -40.33% | Base flattered by gain and an 11.81% ETR |
| EPS basic | 7.40 | 4.42 | -40.27% | Negative |

### 2C. Half-year cross-check (H1 FY27 vs H1 FY26, consolidated)

| Metric | H1 FY26 | H1 FY27 | YoY |
|---|---|---|---|
| Revenue | 12,059.60 | 13,270.71 | +10.04% |
| Op EBITDA | 2,310.43 | 2,652.02 | +14.78% |
| Op EBITDA margin | 19.16% | 19.98% | +83 bps (unrounded 19.158% to 19.984%) |
| Core PBT | 587.47 | 787.83 | +34.11% |
| Parent PAT | 373.04 | 475.26 | +27.40% |

### 2D. Six diagnostic answers

1. **Revenue growth.** Yes. +9.64% YoY (6,099.75 to 6,687.89, L135). No company guidance is filed. Base-case comparison: ND (no thesis). Growth came from Data Services (+606.52) and Campaign Registry (+75.22), offset by Transformation Services (-96.63) and Voice (-35.92), plus a smaller inter-segment elimination (+38.96, from (51.81) to (12.85)) (L234-239). Components sum to 588.14.
2. **Operating EBITDA margin.** Q2 FY27 21.26% vs Q2 FY26 19.24% = **+202 bps YoY**. Sequential Q1 to Q2: 18.69% to 21.26% = +257 bps. The expansion is cost-led. Revenue less network cost rose only 122.02 (+3.61%, 3,384.40 to 3,506.42); network cost rose 17.17%, almost twice revenue, so the gross spread fell from 55.48% to 52.43% (-305 bps). Employee plus other expenses fell 126.24 (2,210.78 to 2,084.54). So 126.24 of the 248.26 EBITDA gain (50.9%) is cost reduction, and part of that cost reduction is not explained (R-A3-04, R-A3-18).
3. **Core operating PBT.** Yes. +64.92% YoY (292.88 to 483.03). At group level the growth is real in the filed numbers. It is not real at the parent: standalone core PBT +3.35% (96.97 to 100.22). Subsidiaries plus eliminations supplied 228.17 of the 248.26 consolidated EBITDA gain [DERIVED: subsidiary EBITDA 722.99 to 951.16].
4. **Gap between core PBT growth (+64.92%) and reported PAT growth (+83.18%).** Other Income +33.65 (from a loss of 17.24 to income of 16.41). Finance cost +4.05 helps. Exceptional items -15.54 worse ((21.00) to (36.54); Q2 FY26 netted a 77.26 gain against a 98.26 charge). Associates -13.95 worse (10.70 to (3.25)). Tax: ETR fell from 32.25% to 26.80%, worth +25.26; higher PBT added 67.17 of tax; net tax change -41.91. See Step 4.
5. **D&A and finance cost vs revenue.** D&A +9.16% vs revenue +9.64%: no absorption deficit this quarter. Finance cost -2.01%. Watch item: CWIP rose 359.31 (+47.2%, 761.50 to 1,120.81, L318) and net debt rose 1,606.60 in H1 (R-A3-23). D&A and interest step up when CWIP capitalises and the new debt runs a full quarter.
6. **Other Income concentration.** Q2 OI is small (16.41 = 3.55% of PBT). The FY26 total of 301.73 sat almost wholly in H2 FY26 (301.87 [DERIVED] = 301.73 - (0.14)). Q2 is not treasury-flattered. A trailing-twelve-month base is: it carries the H2 FY26 OI. Flag for the A21 base in Step 6.5.

Checkpoint. YoY table and six answers shown.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY (consolidated)

The filing gives three quarters directly. Q1 FY26 and the H2 FY26 block are [DERIVED] by subtraction of filed columns (H1 FY26 - Q2 FY26; FY26 - H1 FY26). Q3 FY26 and Q4 FY26 separately: ND.

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT (ex-OI, pre-exc) | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|
| Q1 FY26 [DERIVED] | 5,959.85 | 19.07% (1,136.81) | 294.59 | Staff charge (20.44); NetFoundry loss on sale (42.19) below PAT | Base |
| Q2 FY26 | 6,099.75 | 19.24% (1,173.62) | 292.88 | Staff (98.26); property gain +77.26 | +2.35% revenue |
| H2 FY26, 2 quarters [DERIVED] | 12,743.12 (avg 6,371.56) | 19.71% (2,512.03) | 646.65 (avg 323.33) | Labour Codes (60.58); staff net +4.06; OI 301.87 | avg +4.46% vs Q2 FY26 |
| Q1 FY27 | 6,582.82 | 18.69% (1,230.14) | 304.80 | Staff (44.78); Labour Codes reversal +18.52; fire (30.10); contractual (50.00) | +3.32% vs H2 avg |
| Q2 FY27 | 6,687.89 | 21.26% (1,421.88) | 483.03 | Staff (36.54) | +1.60% revenue; +58.47% core PBT |

Diagnostics.
- **Trajectory.** Revenue: stepping up, slowly (+1.60% QoQ). Margin and core PBT: a step-up in Q2 after a plateau of 18.7% to 19.7% across five quarters. One quarter does not make a new run-rate. Conservative read: the step is unproven until Q3 confirms it.
- **One-off distortion.** Q1 FY27 carries 106.36 of net exceptional charges, but they sit below core PBT. Core PBT is clean of the C-2 items in every row. It is not clean of unexplained operating credits inside employee and other expenses (R-A3-04, R-A3-18).
- **Q2 vs H1 average.** H1 FY27 average: revenue 6,635.36, Op EBITDA 1,326.01, core PBT 393.92. Q2 exceeds all three.
- **Implied Q3 FY27 base.** To hold trajectory Q3 needs revenue at or above 6,687.89 and Op EBITDA margin at or above 21.26% (EBITDA at or above 1,421.88). Q3 FY26 comparator: ND.
- **Capex commissioning test (H1 vs Q4 rule).** CWIP is building, not commissioning: 761.50 to 1,120.81 (L318). No commissioning in H1; PPE fell 234.03 (8,132.92 to 7,898.89, L317). The test applies when CWIP converts.

---

## PRESENTATION CROSS-READ (feeds Steps 2, 6 and 8.5)

The deck carries no consolidated revenue, EBITDA, PAT, net debt, capex or segment table (P-A3 scope note). Its only financial figures are on slide 6.

| Item | Deck reading | Filing / press release cross-check | Read |
|---|---|---|---|
| Digital margin Q2 FY27 | -3.6%, -INR 107 Cr (P-L137-138) | Press release: "digital margins at -3.6%" (L1366); Digital Portfolio Revenue 3,016 (L1384). 107 / 3,016 = 3.55% [DERIVED] | Denominator is consistent with Digital Portfolio Revenue [INFERENCE]. Margin type (EBITDA, EBIT, contribution) ND |
| Digital margin Q1 FY27 | -6.9%, no rupee label (P-L142) | Press release: "Digital losses halved from last quarter" (L1366) | Q1 rupee loss ND (P-A3-02) |
| Digital margin FY25 | -9.7%, -INR 886 Cr full year (P-L145-151) | Not in filing | Quarter vs full-year rupee framing; Q2 annualised loss 428 [DERIVED, 107 x 4] = 48% of FY25: a halving, not an 88% cut (P-A3-01). FY26 skipped (P-A3-03) |
| Digital revenue YoY | ND in deck | 3,016 vs 2,542 = +18.6% (L1384), MGMT, does not tie to any filed line (R-A3-25) | Perimeter moves both ways (see bound below) |
| Core connectivity (Data revenue less Digital Portfolio) | ND | 5,810 - 3,016 = 2,794 vs 5,179 - 2,542 = 2,637, +5.95% [DERIVED from MGMT figures; INFERENCE that Digital sits inside Data revenue, per segment definition L292] | Core connectivity grows near mid-single digits; Digital drives Data growth |
| Plan goal | "Driving absolute EBITDA growth, NPS and ESAT" (P-L112); 5 levers (P-L122-128) | Op EBITDA +21.15% YoY (Step 2) | Goal met this quarter on absolute EBITDA; no margin target stated (P-A3-06) |
| Reset framing | "THE TEAM IS IN PLACE" (P-L85), Tower structure (P-L98-104) | Staff cost optimisation "phased" (L528-531) | New baseline for promise-vs-delivery (P-A3-07) |
| GPU infrastructure in India | "We've invested in GPU infrastructure in India" (P-L162-163) | No amount in filing; capex 1,500.69 H1 (L458) | GPU spend amount and place in Digital margin ND (P-A3-09) |
| AI case studies | "700+ agents live", "600K+ voice AI mins / month" (P-L193) | No revenue in filing | AI monetisation ND (P-A3-08) |
| Reach claims | 70% of India FS live data traffic; 300 of Fortune 500; 380 of ET 500 (P-L88-89) | Press release repeats 300 of Fortune 500 (L1451) | Unsourced, undated (P-A3-10). Not used as evidence |

**Digital as an explanation of the subsidiary jump: bounded (A5 M2).** The Digital portfolio sits mostly in subsidiaries (Kaleyra, Commotion and others in the entity list, L1239-1254). Subsidiary Op EBITDA rose 195.09 QoQ [DERIVED, 5C] and the Data Services result rose 175.18 QoQ (L243).
- If Q1 FY27 Digital revenue did not exceed Q2's 3,016 (L1384), the Q1 loss was at most 208.10 (6.9% x 3,016) and the QoQ cut was at most 101.10 [DERIVED bound].
- That is at most 51.8% of the 195.09 subsidiary EBITDA rise and 57.7% of the 175.18 Data result rise. At least about 94 of the subsidiary rise sits outside Digital or in one-off credits.
- The press-release word "halved" (L1366) gives a cut of about 107 on a Q2 loss of 107: still about 55% of 195.09 [DERIVED, MGMT basis].
- For Digital to explain all 195.09, Q1 Digital revenue would need to be about 4,378 [DERIVED: (195.09 + 107) / 0.069], 45% above Q2's 3,016.
- "Digital margin" has no definition (L1366; A2 FOOTNOTE_UNRESOLVED R1768), so it may not match EBITDA or segment result.
- The perimeter moves both ways. In: Commotion wef 01-Dec-2025 (L1253-1254); FY26 "Acquisition of Subsidiary" cash 136.96 (L463; its link to Commotion is INFERENCE by date). Out: Mgage SA de CV upto 01-Oct-2025 (L1251); Kaleyra Africa upto 04-Sep-2026 (L1246).

Two readings fit, and neither covers the whole jump alone. Reading A: a real Digital loss cut (cost-out plus revenue growth), which recurs and can explain about half at most. Reading B: one-off credits inside subsidiary costs, which do not recur and must cover the remainder unless Q1 Digital revenue was far higher than Q2. The observation that separates them: the Q2 non-recurring credit amount (Q1 in Step 8.5) together with the Q1 and Q3 Digital rupee losses on one perimeter (Q2 in Step 8.5).

---

## STEP 4: OPERATIONAL DECOMPOSITION (PAT bridge, Q2 FY27 vs Q2 FY26, consolidated total PAT)

| Component | YoY change (Rs Cr) | Share of PAT change | Recurring? |
|---|---|---|---|
| Revenue contribution (588.14 x prior margin 19.24%) | +113.16 | 74.3% | Recurring |
| Margin change contribution (248.26 - 113.16) | +135.10 | 88.6% | Recurring in part: 126.24 of opex reduction, cause partly undisclosed |
| D&A change | -62.16 | -40.8% | Recurring (post-capex) |
| Finance cost change | +4.05 | 2.7% | Recurring; will reverse as H1 debt rise flows through |
| **Subtotal: core operating PBT change** | **+190.15** | **124.8%** | |
| Other Income change ((17.24) to 16.41) | +33.65 | 22.1% | Non-recurring typically |
| Exceptional items ((21.00) to (36.54)) | -15.54 | -10.2% | Non-recurring by label; recurring in fact (R-A3-11) |
| Tax: volume effect (PBT growth at 32.25%) | -67.17 | -44.1% | Mixed |
| Tax: ETR change (32.25% to 26.80%) | +25.26 | 16.6% | Mixed; deferred credits (R-A3-14) |
| Share of associates (10.70 to (3.25)) | -13.95 | -9.2% | Mixed |
| Discontinued operations | 0 | 0% | n.a. |
| **Reported PAT YoY change (183.21 to 335.61)** | **+152.40** | **100%** | |
| NCI swing (0.15 to (5.42)) | +5.57 | | Parent PAT change +157.97 |

Arithmetic: 113.16 + 135.10 - 62.16 + 4.05 + 33.65 - 15.54 - 67.17 + 25.26 - 13.95 = 152.40.

Mandatory answers.
- **Recurring vs non-recurring.** Core operating items delivered +190.15, more than the whole +152.40 PAT gain. Non-recurring and mixed items net to -37.75. On the face of the filing, the gain is operating. Conservative caveat: the "recurring" margin line holds 126.24 of employee and other-expense reductions in Q2. The filing does not say how much of that is one-off. SBP accrual alone fell about 11 a quarter (R-A3-18). Consolidated net credit cost swung adversely by 110.79 in H1 (R-A3-06); H1 other expenses still rose only 57.24 (1,817.41 to 1,874.65, L143, +3.15% against revenue +10.04%), and in Q2 alone they fell 35.42 YoY and 63.07 QoQ. So other cost lines absorbed most of the credit swing.
- **If Other Income reverts to Q2 FY26 (-17.24).** PBT falls 33.65; PAT falls 24.63 at the 26.80% ETR [DERIVED]. Run-rate Q2 PAT 310.98 [DERIVED]: still +69.7% YoY.
- **D&A and finance cost steady state.** Not steady. CWIP 1,120.81 and intangibles under development 117.25 (L318, L323) await capitalisation. Gross debt rose 1,272.86 in H1 (10,581.68 to 11,854.54, L373+L382), while Q2 finance cost is only 12.01 above Q1. Implied steady state: ND (rates, tenor and commissioning dates not disclosed).
- **Tax adjustments.** Yes. Deferred tax credit 43.27 in Q2 (L154). On current tax alone Q2 PAT would be 292.34 [DERIVED, 335.61 - 43.27]. Current tax runs 36.14% of PBT. FY26 also holds a one-off 73.25 DTA credit (C-6).

Checkpoint. Bridge ties.

---

## STEP 5: CASH QUALITY AND BALANCE SHEET

Half-year cash flow and balance sheet are filed (Reg 33). Flows compare H1 FY27 with H1 FY26. Balance-sheet stocks compare 30-Sep-2026 with 31-Mar-2026 (the filing gives no 30-Sep-2025 balance sheet).

### 5A. Consolidated

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | 953.64 (H1 FY26, L441) | 1,562.70 (H1 FY27) | +609.06 / +63.87% | Improved; 315.42 of it is lower tax paid (L440) |
| Cash generated before tax | 1,366.85 | 1,660.49 (L439) | +293.64 / +21.48% | Underlying improvement |
| CFO / PAT (total PAT) | 2.55x (953.64 / 373.35) | 3.36x (1,562.70 / 465.33) | +0.81x | D&A-heavy business; ratio is not a quality test alone |
| CFO / Op EBITDA | 41.28% | 58.92% | +17.64 pp | Improved; FY26 full year 92.88% (4,479.10 / 4,822.46) shows H1 seasonality |
| Capex (PPE + intangibles paid) | 1,139.43 (L458) | 1,500.69 | +361.26 / +31.71% | Rising |
| FCF (CFO - Capex) | (185.79) | 62.01 | +247.80 | Thin; capex = 96.0% of CFO |
| FCF after lease (L478) and interest paid (L480) | (713.47) | (584.30) | +129.17 | Negative; dividend 498.78 and associate investment 356.10 on top (R-A3-23) |
| Working capital change (L431-438) | (813.20) | (963.35) | -150.15 | More drag |
| Receivable days (on annualised H1 revenue) | 61.38 (31-Mar-2026, 4,171.10 / 24,802.72 x 365) | 63.32 (4,604.13 / 26,541.42 x 365) | +1.94 days | Slightly worse; receivables +433.03 (+10.4%) |
| Inventory days (on network cost) | 3.22 (100.36) | 3.87 (134.17) | +0.65 days | Not a business driver |
| Payable days (on network cost) | 138.69 (4,317.31) | 123.02 (4,263.89) | -15.67 days | Supplier credit shrinking; capex-payables split ND |
| Cash Conversion Cycle | -74.09 days | -55.83 days (63.32 + 3.87 - 123.02) | +18.26 days | Negative cycle, less negative |
| PPE | 8,132.92 (L317) | 7,898.89 | -234.03 | No commissioning in H1 |
| CWIP | 761.50 (L318) | 1,120.81 | +359.31 / +47.2% | Building |
| Gross borrowings (NC + current) | 10,581.68 | 11,854.54 (L373, L382) | +1,272.86 | Rising |
| Cash + other bank + current investments | 991.24 | 657.50 (L337, L339, L340) | -333.74 | Falling |
| **Net Debt (ex-lease)** | **9,590.44** | **11,197.04** | **+1,606.60 / +16.8%** | **Rising; RED-AMBER** |
| Lease liabilities (NC + current) | 1,667.22 | 1,514.79 (L374, L383) | -152.43 | |
| Net debt / Op EBITDA (FY26; H1 x 2) | 1.99x | 2.11x | +0.12x | Leverage up |
| Net debt / parent equity | 2.78x (3,447.04) | 3.29x (3,401.18) | +0.51x | Low consolidated book (R-A3-19) |
| Promoter Pledge | ND | ND | ND | Not in filing |

### 5B. Standalone

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | 149.59 (H1 FY26, L843) | 740.93 | +591.34 | Improved; tax refund 9.60 vs paid 186.50 (L842) |
| CFO / PAT | 0.43x (149.59 / 347.23) | 3.22x (740.93 / 230.31) | +2.79x | Improved |
| Capex | 458.04 (L845) | 807.18 | +349.14 / +76.2% | Rising |
| FCF (CFO - Capex) | (308.45) | (66.25) | +242.20 | Negative |
| Working capital change (L834-840) | (567.87) | (199.93) | +367.94 | Less drag |
| Receivable days (on annualised H1 revenue) | 67.67 (31-Mar-2026, 1,367.42 / 7,375.71 x 365) | 67.06 (1,356.97 / 7,385.42 x 365) | -0.61 days | Flat |
| Inventory days | n.m. (7.26) | n.m. (18.91) | | Not a driver |
| Payable days (on network cost, trade payables L791+L793) | 187.67 (1,357.78 / 2,640.72 x 365) | 178.55 (1,284.21 / 2,625.22 x 365) | -9.12 days | |
| Cash Conversion Cycle | ND (inventory n.m.) | ND | ND | |
| PPE | 3,928.79 (L730) | 3,906.79 | -22.00 | |
| CWIP | 414.08 (L731) | 589.87 | +175.79 / +42.5% | Building |
| Gross borrowings | 4,751.10 (L780+L788) | 3,541.76 | -1,209.34 | Falling, funded by subsidiary loan repayment 2,641.16 (L855) |
| Net Debt (ex-lease) | 4,259.99 | 3,432.23 | -827.76 | Falling |
| Standalone D/E (Reg 52(4)) | 0.45 (L932) | 0.34 | -0.11 | Improved, but see 5C |
| Bad debts to receivables (Reg 52(4)) | 1.90% (FY26, L940) | 8.57% (H1, not annualised, L940) | +6.67 pp | Worse |
| Current ratio (Reg 52(4)) | 0.57 (L938) | 0.36 | -0.21 | Worse ("loan repaid by subsidiary", L957) |
| Promoter Pledge | ND | ND | ND | |

Reg 52(4) read (A5 M4). Only the leverage ratios improved: D/E 0.45 to 0.34, asset cover 1.14 to 1.60, debt to assets 0.22 to 0.18 (L928-946). The bad-debts ratio rose from 1.90% for all of FY26 to 8.57% for H1 alone, and the current ratio fell from 0.57 to 0.36 (L938, L940). The parent wrote off 116.73 (L829) of the 161.23 consolidated H1 bad debts (L419), 72%, against a 111.81 allowance reversal (L825). The defaulted receivable sits mainly at the parent and was largely provided in earlier periods.

### 5C. Standalone vs consolidated gap (first-class metric, from R-A3-04, R-A3-05, R-A3-19)

| Metric | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 |
|---|---|---|---|---|---|---|
| Parent PAT (consol) | 183.06 | 134.23 | 341.03 | 373.04 | 475.26 | 1,001.57 |
| Standalone PAT | 210.94 | 104.45 | 125.86 | 347.23 | 230.31 | 793.87 |
| **S-vs-C PAT gap % ((consol parent - standalone) / standalone)** | **-13.2%** | **+28.5%** | **+171.0%** | **+7.4%** | **+106.4%** | **+26.2%** |
| Subsidiary revenue share [DERIVED, consol less standalone] | 70.4% | 72.1% | 72.3% | 69.9% | 72.2% | 70.3% |
| Subsidiary Op EBITDA [DERIVED] | 722.99 | 756.07 | 951.16 | 1,502.49 | 1,707.23 | 3,074.39 |
| Subsidiary Op EBITDA margin [DERIVED] | 16.82% | 15.94% | 19.68% | 17.81% | 17.82% | 17.64% |

| Balance sheet | 31-Mar-2026 | 30-Sep-2026 | Change |
|---|---|---|---|
| Consol parent equity (L363) | 3,447.04 | 3,401.18 | -45.86 |
| Standalone net worth (L954) | 10,578.69 | 10,306.04 | -272.65 |
| Consol parent equity / standalone net worth | 32.6% | 33.0% | |
| Consol gross debt / consol parent equity | 3.07x | 3.49x | +0.42x |
| Standalone gross debt | 4,751.10 | 3,541.76 | -1,209.34 |
| Subsidiary gross debt [DERIVED] | 5,830.58 | 8,312.78 | +2,482.20 (+42.6%) |

**Attribution of the 206.80 QoQ rise in parent PAT (134.23 to 341.03, L166):**

| Component | Q1 FY27 | Q2 FY27 | QoQ change | Anchor |
|---|---|---|---|---|
| Standalone PAT | 104.45 | 125.86 | +21.41 | L637 |
| All non-parent sources (consol parent PAT less standalone PAT) | 29.78 | 215.17 | **+185.39 (89.6%)** | L166, L637 |
| of which subsidiaries plus eliminations, before associates and NCI | 20.92 | 213.00 | +192.08 (92.9%) | R-A3-04 |
| of which share of associates | 4.35 | (3.25) | -7.60 | L158 |
| of which NCI absorbing subsidiary losses | 4.51 | 5.42 | +0.91 | L167 |

Read. The swing in the PAT gap from -13.2% to +171.0% is far above the 5 pp test. The Q2 profit jump is a subsidiary event: non-parent sources supplied 185.39 (89.6%) of the 206.80 QoQ rise; within that, subsidiaries plus eliminations supplied 192.08 before a 7.60 associate swing and a 0.91 NCI offset. In short, about 90%. Debt moved the other way: down the group. The standalone Reg 52(4) leverage ratios shown to debenture holders improved while consolidated leverage rose. Eliminations sit inside the derived subsidiary rows, so they are directional, not entity-level. The subsidiaries include Indian entities (e.g. L1211, L1221, L1241, L1254), so the jump is not shown to be overseas.

Dispute note (A5 F2). A5 recomputes 185.39 (89.6%) and calls A3's 192.08 (93%) wrong. Both figures are correct on their own basis. 185.39 = (341.03 - 125.86) - (134.23 - 104.45), all non-parent sources. 192.08 = 213.00 - 20.92, subsidiaries plus eliminations before the associate share (L158) and NCI (L167), per R-A3-04: 215.17 = 213.00 - 3.25 + 5.42 and 29.78 = 20.92 + 4.35 + 4.51. The earlier text applied the 92.9% figure to the "subsidiaries plus eliminations" label correctly but did not state the basis. The review now uses 185.39 (89.6%) as the headline "about 90%" and shows 192.08 as the subsidiary component. The conclusion is unchanged.

### 5D. Mandatory questions

- **CFO/PAT vs Pillar 2 band.** Assumed band: ND (no valuation). H1 CFO/PAT 3.36x consolidated sits above the top 1.30x band, but D&A is 1,480.38 against PAT 465.33, so CFO/PAT overstates cash quality for this business. FCF after lease and interest is negative (584.30). Flag for /fttcp: the Pillar 2 input should run on FCF, not CFO/PAT [pillar-relevant].
- **WC drag structural or growth-induced?** Test: if growth stopped, would WC days stay high? The cycle is negative (-55.83 days), so WC funds the business. The drag in H1 is receivables (+433.03) and lower payables (-53.42 on the balance sheet). Receivable days moved only +1.94; the cycle lost 18.26 days, mostly from shorter payable days. The H1 FY26 pattern was similar (WC (813.20)) and full-year FY26 WC turned positive (+247.64 [DERIVED, 4,951.83 to 5,199.47 before tax]). Rating-agency commentary: not supplied (ND). Classification: neither structural nor growth-induced is proven. Direction: H1 seasonal drag, improving YoY on CFO.
- **CWIP capitalisation.** None in H1. CWIP +359.31; PPE -234.03. Capitalised amount: ND.
- **Net debt vs projected range.** Projection: ND. Net debt rose 1,606.60 (+16.8%) in six months. New debt sits in subsidiaries (2,628.15 long-term raised outside the parent, R-A3-05). Finance cost will rise in H2 FY27.

**Associate stake buy: acquisition economics (A5 M3).** H1 FY27 "Purchase of investments in associates" 356.10 (L462), paid by the parent (standalone 356.11, L850). Target not named; the three associates are STT Global Data Centres India, Smart ICT Services and United Telecom (L1260-1262). Target PAT, ROCE, debt and cash: ND. The only earnings proxy is the group share of all three associates: TTM 16.66 [DERIVED: 32.77 - 17.21 + 1.10, L158]. The H1 cash call is about 21.4x that TTM share. The carrying value 2,331.73 (L326) is about 140x it (139.96x), an earnings yield on book of 0.71%. The associate numbers are management-furnished and unreviewed (L1131-1137), and the Q2 share is a loss of 3.25. The cash call equals 5.7x H1 FCF of 62.01 and went out in the half when net debt rose 1,606.60. On filed evidence this is a capital-hungry stake earning under 1% on book, not an accretive buy.

**Cash conversion classification: INDETERMINATE-WITH-DIRECTION.** Direction: improving (CFO +63.87% YoY; pre-tax cash generated +21.48%). Missing evidence: (1) the tax-refund share of OCF and the remaining refundable balance (non-current tax assets fell 241.04, L330; R-A3-15); (2) the counterparty and recurrence of 161.23 of H1 bad-debt write-offs (L419; R-A3-06); (3) full-year cash flow, because H1 is seasonally weak in FY26 (41.28% vs 92.88% CFO/EBITDA); (4) rating-agency WC commentary. Per house rule this cannot resolve to PROCEED. It caps at PROCEED WITH CAVEATS; the flags below set PROCEED WITH FLAGS.

Checkpoint. Cash and balance-sheet tables shown, both bases.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull

**Tracker rows not supplied.** No tracker rows were passed to A4, and no Notion company page exists to link Affected Companies.

| Signal Name | Type | Cadence | Latest Observation Date and Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| ND (not supplied) | ND | ND | ND | ND | ND | ND |

Fewer than three signals: **FLAG.** Role 5.5 has not run for this company (no initial workup). The tracker floor (OR-17, three external signals) would block /fttcp until Role 5.5 runs in claude.ai.

### 5.5B. Reconciliation

Target reported: Strong at group level (Op EBITDA +21.15% YoY), Weak at the parent (standalone core PBT +3.35%). Signals said: ND. Outcome cell: cannot be assigned. The review does not weight any signal trajectory.

### 5.5C. New signal candidates (payload rows only; written only through the run's operator-approval gate; Decision Status never written)

No signal is written by A4. Candidate dependencies surfaced by this filing, for Role 5.5 to source and verify (sources PENDING LIVE VERIFICATION):

| Candidate signal | Case | Why (filed anchor) |
|---|---|---|
| US messaging-campaign registry volumes and fees (Campaign Registry segment) | B (new) | 23.80% of Q2 segment result on 4.15% of revenue; result H1/H1 +55.75% (YoY +114.38% on a depressed base) (L238, L246; R-A3-20). Segment definition: campaign data shared "with mobile operators to reduce spam" (L297) |
| India data-centre capacity additions and DC-to-DC connectivity demand | B (new) | CEO: "strong demand for DC-to-DC connectivity" (L1374); "$1 billion opportunity" (L1400, MGMT); associate STT Global Data Centres India (L1260) |
| DoT AGR litigation docket (SC, TDSAT) | B (new, event-driven) | Contingent liability 7,513.71 (L560) |
| Foreign-subsidiary VAT appeal outcome (National Court) | B (new, event-driven) | 365.80; judgment scheduled 13-Oct-2026 (L572). Jurisdiction not named in the note (A2 NAME_NOT_DISCLOSED, R1439) |
| Enterprise AI voice and agent adoption (Commotion platform) | B (new) | "700+ agents live", "600K+ voice AI mins / month" (P-L193) |

State: "No new signal written this quarter. Five candidates listed for Role 5.5."

### 5.5D. Forward-view weighting

No signals, so Step 6 runs on the single-quarter print alone. A single quarter is one data point. Conservative weighting applies to the Q2 step-up.

Section checkpoint passed (no wait under /run-quarterly).

---

## STEP 6: RECONCILIATION VS THESIS (PRE-THESIS FORM)

### 6A. Variance vs Notion projections

| Metric | Bear Proj | Base Proj | Bull Proj | Actual | Lands In |
|---|---|---|---|---|---|
| Revenue (Q2 FY27) | ND | ND | ND | 6,687.89 (L135) | ND (no projection) |
| Op EBITDA Margin | ND | ND | ND | 21.26% | ND |
| PAT (parent) | ND | ND | ND | 341.03 (L166) | ND |
| EPS (basic) | ND | ND | ND | 11.96 (L213) | ND |
| Net Debt (ex-lease) | ND | ND | ND | 11,197.04 | ND |
| ROCE (pre-tax, H1 annualised on closing capital) | ND | ND | ND | 15.84% [DERIVED: 2,343.28 / 14,796.19]; FY26 15.07% (1,995.72 / 13,241.54) | ND |

Probability re-weighting rule: not applicable (no projections; no consecutive-quarter history).

### 6B. Watchlist items

| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| ND | No monitoring checklist exists | ND | ND | ND | UNKNOWN |

### 6C. Thesis-broken trigger check

| Thesis-Broken Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| None on record | ND | ND | NOT APPLICABLE (no conditions) |

No condition can fire. No exit or AVOID recommendation arises from 6C.

### 6D. Growth trigger status

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| None on record | ND | ND | ND | ND |

Candidate triggers observed in this quarter's documents, for a future thesis to adopt or reject (not statuses):
- Digital portfolio breakeven: -9.7% FY25, -6.9% Q1 FY27, -3.6% Q2 FY27 (P-L137-151); undated (P-A3-04).
- Campaign Registry profit growth: result H1/H1 +55.75% (L246); the YoY +114.38% rests on a depressed Q2 FY26 base and a perimeter change (1E note).
- DC-to-DC connectivity: MGMT claim only (L1374, L1400).
- Cost programme: employee cost -7.15% YoY (1,269.57 to 1,178.75, L140) under a "phased" programme (L528-529).

Checkpoint. 6A-6D shown in pre-thesis form.

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

**Deferred to /fttcp and Role 1 (operator ruling OR-30).** No expectation ledger exists for this name. Pillar-relevant facts flagged for that step:

| Fact | Value and anchor | Why it matters for 6.5A |
|---|---|---|
| Q2 FY27 parent PAT annualised | 1,364.12 [DERIVED, 341.03 x 4] | Single-quarter base |
| TTM parent PAT | 1,103.79 [DERIVED: 1,001.57 - 373.04 + 475.26] | Trailing base; divergence from Q2 annualised = 23.6% (under the 25% test) |
| TTM basic EPS | 38.72 [DERIVED: 35.14 - 13.09 + 16.67] | |
| H2 FY26 Other Income inside TTM | 301.87 [DERIVED] | Inflates the TTM base with non-operating income |
| Q2 FY27 one-offs to adjust | Staff charge (36.54); deferred tax credit 43.27; possible unexplained cost credits (R-A3-04) | Declare before annualising |
| Seasonality | H1 CFO/EBITDA 41-59% vs FY 93% | Use a trailing-4-quarter base for cash items |

---

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

**Deferred to /fttcp and Role 1 (operator ruling OR-30).** No Section 1B value is computed here. Pillar-relevant facts:

| Pillar / Input | Original Assumption | Current Reading (this quarter) | Action |
|---|---|---|---|
| ROCE Base (Pillar 1) | ND | Pre-tax ROCE 15.84% H1 annualised; 15.07% FY26 [DERIVED, closing capital, ex-lease]. Consolidated book is low (parent equity 3,401.18 vs standalone net worth 10,306.04), so RoE-type ratios flatter | Deferred; FTTCP ROCE verdict governs |
| Cash Multiplier (Pillar 2) | ND | CFO/PAT 3.36x H1 (D&A-heavy); FCF after lease and interest (584.30) H1; FY26 FCF 2,045.92 [DERIVED, 4,479.10 - 2,433.18] | Deferred; use FCF-based evidence |
| Growth Visibility Premium | ND | Digital margin path (explains about half of the subsidiary jump at most); Campaign Registry result H1/H1 +55.75%; capex +31.71% | Deferred |
| Strategic Premium | ND | Campaign Registry niche (58.33% margin, below Q1 FY26's 64.91%); network assets; single-credit rule state: ND | Deferred |
| UA Multiplier | ND | Institutional ownership and three qualifiers: ND (not in filing) | Deferred |
| Sector Cap | ND | Business mix: Data Services 86.9% of Q2 revenue (5,810.99 / 6,687.89) | Deferred |
| Hurdle Ratio recheck | ND | Current PE ND (no price in documents); EPS CAGR ND | Deferred |

Balance-sheet overlays for the pillar session: DoT contingent liability 7,513.71 (2.21x parent equity); VAT 365.80 binary; net debt 11,197.04 rising; associates carried at about 140x TTM share of profit.

Section checkpoint passed.

---

## STEP 8: POSITION DECISION

**Decision Status verified: NONE ON RECORD.** The name is not held and not on a recorded watchlist. **Branch: 8A-W**, run in pre-thesis form.

### 8A-W logic applied

- Thesis-broken condition FIRED? None exist. Not applicable.
- Actual vs Bear/Base/Bull? No projections. Lands In: ND on every metric.
- Output required by 8A-W: updated entry zone (ND, none exists and none can be set without Role 1); updated gate (ND); proposed Decision Status: **none proposed.** The operator sets status.
- Gate note for the operator: CLAUDE.md SPEAR GATE. No Spear line exists. /run-pipeline or /fttcp on TATACOMM needs /step1 (or a web spear) first. This review supplies its load-bearing-fact candidates: (1) Q2 margin step-up cause (R-A3-04); (2) Digital breakeven date and definition (P-A3-04); (3) net-debt path (R-A3-23); (4) DoT and VAT contingent outcomes (R-A3-08, R-A3-09).

### 8B. Trigger refinement

- Original add-back trigger: ND (no page).
- Revised add-back trigger: ND. Proposed watch conditions for a future thesis, for operator decision only: (a) Q3 FY27 Op EBITDA margin at or above 21.0% with disclosed non-recurring credits under 20 Cr; (b) net debt / annualised Op EBITDA at or below 2.11x at 31-Mar-2027; (c) VAT judgment disclosed and favourable.
- Original trim ladder: ND. Revised trim ladder: not applicable (not held).

### 8C. Single cleanest metric for Q3 FY27

**Consolidated operating EBITDA margin, ex Other Income and pre-exceptional (Op EBITDA / Revenue from operations).**
- Bull threshold: **at or above 21.0%** in Q3 FY27 (holds most of Q2's 21.26%). This says the Q2 step was structural cost-out and Digital loss reduction.
- Bear threshold: **at or below 19.5%** (back to the FY26 level of 19.44% and H1 FY26 19.16%). This says Q2 held one-off credits.
- Between the two: inconclusive; read with the Q3 Digital rupee loss.

Section checkpoint passed.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

Every R-A3 and P-A3 finding classified FORWARD-SIGNAL or AMBIGUOUS maps to at least one question below (coverage shown in the "From" column).

### 8.5A. Primary table (ordered by materiality)

| # | Cat | Question | Why it matters | Bull answer | Bear answer | From |
|---|---|---|---|---|---|---|
| 1 | C | Consolidated employee cost fell 60.98 and other expenses fell 63.07 QoQ in Q2 while revenue rose 105.07 (L140, L143). What rupee amount of Q2 cost was non-recurring (provision releases, SBP reversals, FX, credits)? | Non-parent sources supplied about 90% (185.39) of the 206.80 QoQ parent PAT rise; Digital can explain about half at most; the cause decides whether 21.26% margin is a run-rate | Under 20 Cr non-recurring; savings named and permanent | Over 75 Cr non-recurring, or no number given | R-A3-04, R-A3-22 |
| 2 | C | What was the Digital portfolio rupee loss in Q1 FY27, Q2 FY26 and FY26, on the Q2 FY27 perimeter and margin definition? | The deck sets a quarter (-107 Cr) beside a full year (-886 Cr) and skips FY26; the Q1 figure sets how much of the jump Digital explains | A consistent quarterly series showing the cut | Perimeter or definition changed; series not given | P-A3-01, P-A3-02, P-A3-03 |
| 3 | B | In which fiscal quarter do you expect Digital portfolio margin to reach zero, and is "Digital Margin" EBITDA, EBIT or contribution? | Breakeven is the deck's main catalyst and it has no date | A named quarter within FY28, EBITDA-level definition | No date, or contribution-level only | P-A3-04 |
| 4 | A | Did the National Court deliver its 13-Oct-2026 judgment on the 365.80 Cr VAT and penalty appeal, and was it for or against the Group? | Payment is suspended pending appeal, so a loss is a cash and P&L event (10.8% of parent equity) | Delivered, in the Group's favour | Delivered against, or deferred with no date | R-A3-08 |
| 5 | F | Net debt rose 1,606.60 to 11,197.04 in H1 and capex used 96% of CFO. What is FY27 capex guidance, and what net debt / EBITDA ceiling does the Board hold? | The build is debt-funded; leverage rose from 1.99x to 2.11x | Capex guided, ceiling at or below 2.5x, FCF positive in H2 | No ceiling; capex rising again in FY28 | R-A3-23, R-A3-05 |
| 6 | G | What is the total cost of the staff cost optimisation programme, how much remains, and in which quarter does it end? | A "one-time" charge recurred in Q2 FY26, Q1 FY27 and Q2 FY27 (98.26, 44.78, 36.54) | Total and end date stated, under 50 Cr left | Open-ended, no total | R-A3-11 |
| 7 | D | What FY27 effective tax rate do you expect, and how much DTA on accumulated losses remains to recognise? | Deferred credits shield 935 bps of Q2 PBT; current tax runs 36.14% | ETR guided near 27% with a stated DTA pool | ETR steps toward 36% | R-A3-14 |
| 8 | E | Campaign Registry result fell from 122.93 (Q1 FY26) to 75.58 (Q2 FY26) and is 162.03 now. What caused the Q2 FY26 dip, what did Campaign Registry Inc (Canada) contribute before its 14-Jan-2026 exit, and does any operator contract or regulatory term renew in the next 12 months? | One niche earns 23.80% of segment result on 4.15% of revenue; the YoY +114.38% rests on that dip | Dip was a one-off; Canada immaterial; no renewal inside 12 months | Recurring volatility, material Canada loss, or a renewal or rule change due | R-A3-20 |

### 8.5B. Coverage table (each remaining FORWARD-SIGNAL / AMBIGUOUS finding)

| # | Cat | Question | Bull answer | Bear answer | From |
|---|---|---|---|---|---|
| 9 | F | Which entity raised the 2,628.15 Cr of H1 long-term borrowings (L476), and does the parent guarantee it (yes/no)? | Named entity, INR or hedged, no guarantee needed | Guaranteed USD debt at a high rate | R-A3-05 |
| 10 | D | The parent wrote off 116.73 Cr of the 161.23 Cr H1 bad debts (L829, L419) and the standalone bad-debts ratio rose to 8.57% from 1.90% (L940). Which customer or contract is it, and is any further amount at risk (Rs)? | One legacy account, fully provided earlier | Several accounts, more at risk | R-A3-06 |
| 11 | D | Is the 50.00 Cr Q1 contractual-obligation provision (L524) a receivable, an advance or a guarantee, and is it the same counterparty as the write-offs (yes/no)? | Receivable, recovery action filed | Guarantee, more exposure | R-A3-13 |
| 12 | F | Which associate received the 356.10 Cr H1 investment (L462), what return do you expect on it, and what further capital is committed for FY27-FY28 (Rs)? The group's TTM share of all associates' profit is 16.66 Cr against a 2,331.73 Cr carrying value. | Named, committed amount stated, earnings ramp dated | Open-ended capital calls, no return date | R-A3-07 |
| 13 | G | Which two subsidiaries are management-furnished and unreviewed (loss 14.83 on revenue 3.11 in Q2, L1127-1128)? | Named, wind-down planned | Unnamed, losses growing | R-A3-07 |
| 14 | A | What was the DoT demand aggregate at 31-Mar-2026 and 30-Jun-2026 against 7,844.57 now, and was any new notice received in Q2 (yes/no)? | Flat aggregate, no new notice | Aggregate rising | R-A3-09 |
| 15 | F | What is the standalone carrying value of the Kaleyra, Inc. investment against the FMV of USD 92.625m (L1506), and what standalone gain or loss do you expect on transfer (Rs)? | Carrying value near FMV, no loss | Large standalone loss | R-A3-10 |
| 16 | F | On what date do you expect the Kaleyra, Inc. transfer to TCNL to complete, and is any external financing or stake sale planned at TCNL (yes/no)? | Date given; simplification only | Overseas raise or stake sale planned | R-A3-10, R-A3-29 |
| 17 | G | How did Kaleyra Africa (Pty) Limited leave the group on 04-Sep-2026 (sale, liquidation or strike-off), and what was the consideration and P&L impact (Rs)? | Small sale, no loss | Write-off, unstated loss | R-A3-27 |
| 18 | F | What is the purpose of TComm Turkey (wef 21-May-2026, L1256), and how much capital is committed (Rs)? | Small sales entity, capital stated | Large undisclosed commitment | R-A3-28 |
| 19 | D | For the Q1 fire provision of 30.10 Cr, has an insurance claim been filed, for what amount, and by when do you expect recovery? | Claim filed, recovery dated | No insurance, more losses | R-A3-12 |
| 20 | D | What tax refund amount did the Group receive in H1 FY27, and what refundable balance remains in the 1,498.33 Cr non-current tax assets (L330)? | Amount and years stated, balance large | Refund one-off, balance small | R-A3-15 |
| 21 | D | What discount-rate or actuarial change drove the standalone Q1 FY27 OCI loss of 9.37 Cr (L639)? | Single assumption change stated | No explanation | R-A3-16 |
| 22 | C | What forfeiture reversal sits in the H1 SBP accrual of 2.02 Cr against 24.01 Cr a year ago (L422), and were new grants made in FY27 (yes/no)? | Small reversal, grants continue | Large reversal inside EBITDA | R-A3-18 |
| 23 | E | Transformation Services revenue fell 33.70% YoY (286.74 to 190.11, L236). Was this a client loss (how many clients) or group in-sourcing? | In-sourcing, margin held | Client loss | R-A3-21 |
| 24 | G | Does Zubin Adil Patel leave the company, move within the group, or retire when Ridhi Sood takes over on 01-Nov-2026? | Planned internal move | Unexplained exit | R-A3-24 |
| 25 | A | Please reconcile press-release Data revenue of 5,179 Cr for Q2 FY26 (L1383) to filed Data Services revenue of 5,204.47 Cr (L235), and define "Digital Portfolio". | Definitional, reconciliation given | No reconciliation | R-A3-25 |
| 26 | F | What is the 7.40 Cr asset held for sale (L344), who is the buyer, at what price, and by what date does it complete? | Named, price above book, dated | No date | R-A3-01 |
| 27 | A | Was FY25 Digital restated to the current perimeter (yes/no)? What Digital revenue came from entities added after FY25 (Commotion wef 01-Dec-2025; FY26 acquisition cash 136.96 Cr, L463), and what left (Mgage SA de CV 01-Oct-2025, Kaleyra Africa 04-Sep-2026)? | Restated; net perimeter effect small | Not restated; growth is perimeter | P-A3-05 |
| 28 | B | Does any earlier quantified margin or revenue target still stand (yes/no), and if withdrawn, when? | Target stands and is on track | Withdrawn without notice | P-A3-06 |
| 29 | G | When did the Tower structure take effect, and which of the 11 named heads joined in the last 12 months? | Stable team, few new heads | Many new heads mid-reset | P-A3-07 |
| 30 | E | What was AI-platform revenue in Q2 FY27 (Rs), and how many paying customers does it have (the deck's two case studies are unnamed)? | Disclosed, growing | Not disclosed | P-A3-08 |
| 31 | F | What did the India GPU infrastructure cost (Rs), what share is in use, and is its depreciation inside the Digital margin (yes/no)? | Amount stated, high use, included | Large, idle, excluded | P-A3-09 |

### 8.5C. Top 3 by likelihood of thesis-changing information

1. **Q1 (cost credits in Q2).** A non-recurring amount above 75 Cr would show the Q2 margin step is mostly one-off. That changes any Bull case probability.
2. **Q5 (capex and net-debt ceiling).** No ceiling with capex rising would confirm the Bear case: a debt-funded build with thin FCF.
3. **Q4 (VAT judgment).** A binary, dated fact. A non-answer two weeks after the hearing date tests management transparency.

### 8.5D. Channel

The earnings call took place on 15-Oct-2026 at 4:00 pm IST (P-R064, P-L33), but its transcript was not in --docs. Channel: **wait for the concall transcript, run Role 5 on it, then send an IR email** with every question the call did not answer, verbatim. IR contact named in the press release: Rajiv Sharma (L1439). Q4 (VAT) is material and dated: if the transcript is silent, email it at once.

---

## MONITORABLES AND CATALYST LIST (seeded by the A3 commitment registers and the Board Outcome forward items)

| # | Item | Implied date | Source | Status |
|---|---|---|---|---|
| 1 | National Court VAT judgment outcome (365.80 Cr) | Judgment scheduled 13-Oct-2026; disclosure due at the next filing at the latest (Q3 FY27 results) | L572; R1558; R-A3-08 | Outcome ND |
| 2 | Q2 FY27 concall transcript (Role 5 input) | Call held 15-Oct-2026; transcript expected within days [INFERENCE, exchange practice] | P-L33 | Pending |
| 3 | Ridhi Sood takes office as Company Secretary | 01-Nov-2026 | L72; L1542; R1585 | Initiated |
| 4 | Kaleyra, Inc. transfer to TCNL completes | ND (not stated); check the Q3 FY27 consolidation list | L45-53; L1519-1524; R-A3-10, R-A3-29 | Initiated |
| 5 | Q3 FY27 results (quarter ending 31-Dec-2026): Op EBITDA margin vs 21.0% / 19.5% thresholds | Quarter end 31-Dec-2026; filing date ND | Step 8C | Pending |
| 6 | Digital portfolio breakeven | ND (no date) | P-L132; P-A3-04 | Underway |
| 7 | Staff cost optimisation programme end | ND, ongoing | L528-531; R-A3-11 | Underway |
| 8 | Asset held for sale (7.40) disposal, gain to exceptional line | ND | L344, L460; R-A3-01 | Initiated (4.00 advance) |
| 9 | CWIP 1,120.81 capitalises; D&A step-up | ND | L318; R-A3-23 | Building |
| 10 | Fire provision true-up (insurance or further loss) | ND | L541-542; R-A3-12 | Provisional |
| 11 | DoT AGR appeals at SC and TDSAT | ND | L552-559; R-A3-09 | Underway |
| 12 | CEO outlook: "enter the second half ... with momentum and confidence" | H2 FY27 (Q3 and Q4 FY27 results) | L1375-1376 | Outlook |
| 13 | DC-to-DC connectivity "$1 billion opportunity" | ND | L1400 | Outlook (MGMT) |
| 14 | FY27 full-year results with full-year cash flow (FCF, CFO/EBITDA vs FY26 92.88%) | Year end 31-Mar-2027; filing date ND | Step 5 | Pending |
| 15 | FY27 Annual Report: actuarial assumptions behind Q1 OCI (9.37); entity-level subsidiary results | ND (after FY27 close) | L639; R-A3-16 | Pending |
| 16 | Plan levers (5) and "THE TEAM IS IN PLACE" reset baseline | ND | P-L85, P-L122-128; P-A3-07 | Initiated |
| 17 | GPU infrastructure in India (amount ND) | Stated complete | P-L162-163; P-A3-09 | Completed (per deck) |

---

## STEP 9: NOTION UPDATE

Not executed by A4. No Notion company page exists, so there is no page to append to. Payload status: this review is the payload body if the operator creates a page. Decision Status: never written by /run-quarterly; no change proposed. Row properties: none. Page ID: ND.

---

## VERDICT AND FLAGS

**Protocol verdict: PROCEED WITH FLAGS.** Cash conversion is INDETERMINATE-WITH-DIRECTION, which caps the verdict at PROCEED WITH CAVEATS; the flags below are material enough to set PROCEED WITH FLAGS. No mechanical failure. No REWORK trigger. Correction loop 1 changes no verdict.

Flags (surfaced; decisions stay with the operator):
1. PRE-THESIS: no Notion page, no Decision Status, no Spear line. /step1 is the gate before any pipeline run.
2. Q2 profit jump is a subsidiary event. Non-parent sources supplied 185.39 (89.6%) of the 206.80 QoQ parent PAT rise. Cause undisclosed; Digital can explain about half at most (R-A3-04, R-A3-22).
3. Half of the 248.26 YoY EBITDA gain is cost reduction; the gross spread fell 305 bps (Step 2).
4. Net debt +1,606.60 (+16.8%) to 11,197.04 in H1. FCF after lease and interest (584.30). Dividend 498.78 exceeded H1 parent PAT 475.26 (R-A3-23, R-A3-19).
5. Debt migrated to subsidiaries (+2,482.20). Standalone Reg 52(4) leverage ratios improved while consolidated leverage rose (R-A3-05).
6. DoT contingent liability 7,513.71 = 2.21x consolidated parent equity; emphasis of matter in both reports (R-A3-09).
7. VAT judgment on 365.80 was due 13-Oct-2026; the note says only "the Group awaits the National Court's decision" (L572; R-A3-08).
8. Reported ETR 26.80% rests on recurring deferred credits; current tax 36.14% (R-A3-14).
9. OCF lifted by 315.42 lower tax paid, from refunds (R-A3-15).
10. Credit costs: 161.23 H1 write-offs, 116.73 at the parent; standalone bad-debts ratio 8.57% vs 1.90%; current ratio 0.36 vs 0.57; 50.00 recoverability provision; counterparties unnamed (R-A3-06, R-A3-13).
11. "One-time" staff charge recurs in every quarter shown (R-A3-11).
12. Campaign Registry concentration: 23.80% of segment result on 4.15% of revenue; YoY +114.38% rests on a depressed base, H1/H1 +55.75% (R-A3-20).
13. Associates carried at 2,331.73 (68.6% of parent equity, about 140x TTM share of profit 16.66) on unreviewed numbers; 356.10 added in H1; associate share turned to a loss (R-A3-07).
14. Press-release and deck metrics do not tie to filed lines; Digital chart framing flatters (R-A3-25, P-A3-01 to P-A3-05).
15. Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30). Tracker rows not supplied; Role 5.5 not run.
16. Concall held 15-Oct-2026; transcript not in this run; Role 5 pending.

---

## PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (this quarter's results filing), MGMT (press release, deck, CEO quote), SECONDARY (none used), AGENCY (none supplied), INFERENCE (analyst reasoning, labelled). No prior Notion or peer work exists for this company. Every figure below is from this quarter's documents unless marked INFERENCE.

### 1. Summary narrative

Revenue grew 9.6% from a year ago, to Rs 6,688 Cr (FILED).
Operating EBITDA grew 21.2%, to Rs 1,422 Cr (FILED).
The margin rose 2 points, to 21.3% (FILED).
Profit for shareholders rose 86%, to Rs 341 Cr (FILED).
The margin gain came from lower staff and other costs (FILED); better pricing is not shown (INFERENCE from the 305 bps fall in the network spread).
Network costs grew almost twice as fast as revenue (FILED).
The parent company itself barely grew; its core profit rose 3% (FILED).
Subsidiaries, with eliminations, supplied about 90% of the profit rise from last quarter (FILED, Step 5C).
The filing does not say why, and the Digital loss cut can explain about half at most (INFERENCE, bounded in the cross-read).
Net debt grew Rs 1,607 Cr in six months, to Rs 11,197 Cr (FILED).
Capex took 96% of operating cash, and cash flow after lease and interest payments was negative (FILED).
A dispute with the telecom department carries Rs 7,514 Cr of contingent liability (FILED).
A foreign VAT case of Rs 366 Cr had a court date on 13 October; the filing says the group awaits the decision (FILED).
This is a first read, with no thesis, no entry zone and no Decision Status.
The verdict is PROCEED WITH FLAGS.
The next quarter's margin decides whether Q2 was a new level or a one-off.

### 2. Sector intelligence

Demand for data links between data centres in India is rising; the CEO calls it a "$1 billion opportunity" (MGMT, L1400). The company also holds a stake in a data-centre associate, STT Global Data Centres India (FILED, L1260). AI workloads add demand for GPU capacity, which the company says it has built in India (MGMT, P-L162). Voice is in structural decline: revenue fell 8.9% and profit fell 48% (FILED). Regulation is a live risk. The telecom department's demands date back to FY2005-06 and are "revised over a period of time" (FILED, L545-547). New Labour Codes moved staff costs in FY26 and Q1 FY27 (FILED). Growth in AI and data-centre traffic as a tailwind for the whole sector is INFERENCE; no sector data was supplied.

### 3. Business-model intelligence

The company earns 87% of revenue from Data Services: network connectivity plus digital platforms (FILED, L235). Its biggest cost is the network it rents and runs, at 48% of revenue (FILED). The digital platforms (messaging, customer engagement, AI tools) still lose money, at -3.6% margin, though the loss is shrinking (MGMT). A small US business, Campaign Registry, checks text-message campaigns for mobile operators. It earns 58% margins and now makes 24% of segment profit on 4% of revenue (FILED). Its profit rose 56% half-year on half-year; the 114% quarterly jump flatters because the year-ago quarter was weak (FILED). Model drift this quarter: profit leans on cost cuts and on one niche, while the core network spread narrows. Core connectivity appears to grow about 6% a year (INFERENCE, derived from MGMT revenue lines that do not tie to the filing). Most profit and most new debt now sit in subsidiaries, not the parent (FILED). The group keeps putting money into associates that earn under 1% on their book value so far (FILED, Step 5D).

### 4. Competition intelligence

The filings name no competitor. The company claims 300 of the Fortune 500 as customers and 70% of India's live financial-services data traffic (MGMT, unsourced). Its likely strength is a global subsea and enterprise network that new entrants cannot copy quickly (INFERENCE). Its likely weak spots are messaging and engagement platforms, where global software firms compete on price, and voice, which is shrinking (INFERENCE; the filed voice decline supports the second point). In Indian enterprise connectivity the large mobile operators compete for the same customers (INFERENCE). Peer market shares and peer margins: ND. Notion holds pages for E2E Networks, iValue and Tejas that cite Tata Communications as a peer, but no peer figures were passed to this review. Risk to watch: price pressure on Campaign Registry or a rule change by US carriers, since one niche carries a quarter of segment profit (INFERENCE from FILED concentration).

### 5. Forward map (next about 10-11 months)

Make-or-break reading: **Q3 FY27 consolidated operating EBITDA margin (quarter ending 31-Dec-2026).** At or above 21.0%, the Q2 step looks real. At or below 19.5%, Q2 held one-off credits.
- **VAT judgment (court date 13-Oct-2026; disclosure by Q3 FY27 results).** Bull: ruling for the group, the Rs 365.80 Cr contingent falls away. Bear: ruling against, a cash payment and a P&L charge.
- **Concall transcript (call held 15-Oct-2026).** Bull: management names the Q2 cost credits and they are small. Bear: no number, or a large one-off.
- **New Company Secretary (01-Nov-2026).** Bull: planned handover explained. Bear: unexplained exit of the incumbent.
- **Kaleyra, Inc. transfer to TCNL (date ND).** Bull: simple re-housing, no standalone loss. Bear: a standalone write-down or an overseas debt raise.
- **Digital breakeven (date ND).** Bull: margin moves from -3.6% toward zero in Q3. Bear: the loss widens again.
- **CWIP of Rs 1,120.81 Cr capitalises (date ND).** Bull: revenue rises with it. Bear: D&A rises before revenue.
- **Net debt at 31-Mar-2027 (FY27 results).** Bull: at or below 2.11x operating EBITDA with positive H2 free cash flow. Bear: above it, with capex still rising.
- **Staff cost programme (end date ND).** Bull: an end date and total cost are given. Bear: another charge each quarter.
- **Asset held for sale, Rs 7.40 Cr (date ND).** Bull: sale completes with a gain. Bear: it stays unsold.

---

## CORRECTION LOOP 1 LOG (A5 audit, 2026-10-17)

Each item was checked against the A1 fulltext at the cited lines before it was written.

| A5 item | Change | Verified at |
|---|---|---|
| F1 | CCC at 30-Sep-2026 corrected from -61.83 to -55.83 days; change from +12.26 to +18.26 days (5A table, 5D) | L335, L338, L384, L135, L139 |
| F2 | Attribution now headlined as 185.39 (89.6%) from all non-parent sources, with 192.08 shown as the subsidiaries-plus-eliminations component before associates (-7.60) and NCI (+0.91). Updated in 5C, 8.5A Q1, flag 2, brief, analyst note, YAML flag. "Overseas" dropped from the brief. Dispute note on basis added under 5C | L158, L166, L167, L637; Indian subsidiaries L1211, L1221, L1241, L1254 |
| F3 | Step 4 sentence corrected: H1 other expenses rose 57.24 (+3.15%); they fell only in Q2 (-35.42 YoY, -63.07 QoQ) | L143 |
| M1 | Campaign Registry base-effect note added under 1E (Q1 FY26 122.93 at 64.91%; Q2 FY26 dip to 75.58; +31.8% vs Q1 FY26; H1/H1 +55.75%; QoQ +10.1%; Canada exit 14-Jan-2026). Qualifier added in 5.5C, 6D, Step 7, Q8, flag 12, brief | L238, L246, L1245 |
| M2 | Digital bound added to the cross-read (101.10 ceiling, 51.8% of 195.09, 57.7% of 175.18, 4,378 requirement, two-way perimeter with 136.96 acquisition cash and Mgage exit). "Likeliest" removed from the analyst note. Q27 extended | P-L138, P-L142, L1366, L1384, L243, L463, L1246, L1251, L1253-1254 |
| M3 | Associate stake-buy economics added to 5D (356.10 = 21.4x and 2,331.73 = 139.96x TTM share 16.66; 0.71% yield; 5.7x H1 FCF). Q12, flag 13, Step 7 overlay updated | L158, L326, L441, L458, L462, L850, L1131-1137 |
| M4 | Reg 52(4) bad-debts ratio (1.90% to 8.57%) and current ratio (0.57 to 0.36) added to 5B with read; "ratios improved" narrowed to leverage ratios; parent share of write-offs (116.73 of 161.23, 72%) and 111.81 reversal added to flag 10 and Q10 | L419, L825, L829, L938, L940, L928-946 |
| Style S1 | 2C H1 Op EBITDA growth 14.78%; margin +83 bps unrounded | L135-146 |
| Style S2 | C-2d: "Includes impairment" restored | L417, L495 |
| Style S3 | VAT note quoted ("the Group awaits the National Court's decision") in C-4, flag 7, brief | L572 |
| Style S4 | Brief: "rose 86%" | L166 |
| Style S5 | Brief: pricing statement tagged INFERENCE | L135, L139 |
| Style S9 | One-line dispositions added for un-dispositioned A2 flags and slides 2, 3, 9 | L33, L1028, L1159, L1335 |
| Style S12 | Summary narrative set one sentence per line (16 lines) | n.a. |
| Style S13 | Diagnostic 1 now includes inter-segment +38.96; components sum to 588.14 | L239 |
| Style S6, S7, S8, S10, S11 | Not A4 items (A1/A2 bases, labels and row emission); no change here | n.a. |

Verdict, cash classification and position branch unchanged.

---

```yaml
stage: A4-analyst
company: "TATACOMM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, presentation]
ledger_reconciliation:
  notes: 18
  turns: 0
  slides: 9
  all_reviewed: true
  a3_findings_incorporated: ["R-A3-01", "R-A3-02", "R-A3-04", "R-A3-05", "R-A3-06", "R-A3-07", "R-A3-08", "R-A3-09", "R-A3-10", "R-A3-11", "R-A3-12", "R-A3-13", "R-A3-14", "R-A3-15", "R-A3-16", "R-A3-17", "R-A3-18", "R-A3-19", "R-A3-20", "R-A3-21", "R-A3-22", "R-A3-23", "R-A3-24", "R-A3-25", "R-A3-26", "R-A3-27", "R-A3-28", "R-A3-29", "R-A3-30", "P-A3-01", "P-A3-02", "P-A3-03", "P-A3-04", "P-A3-05", "P-A3-06", "P-A3-07", "P-A3-08", "P-A3-09", "P-A3-10", "P-A3-11"]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "NONE ON RECORD (no Notion page; live search 2026-10-17); framed as PRE-THESIS READ"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY26", gap_pct: -13.2}
  - {period: "Q1 FY27", gap_pct: 28.5}
  - {period: "Q2 FY27", gap_pct: 171.0}
  - {period: "H1 FY26", gap_pct: 7.4}
  - {period: "H1 FY27", gap_pct: 106.4}
  - {period: "FY26", gap_pct: 26.2}
questions_for_management:
  - {q: "What rupee amount of Q2 consolidated employee (-60.98 QoQ) and other-expense (-63.07 QoQ) reduction was non-recurring?", from_finding_id: "R-A3-04"}
  - {q: "Same question for Data Services: what one-offs sit in the +175.18 QoQ segment result on +107.41 revenue?", from_finding_id: "R-A3-22"}
  - {q: "What was the Digital rupee loss in Q1 FY27, Q2 FY26 and FY26 on the Q2 FY27 perimeter?", from_finding_id: "P-A3-01"}
  - {q: "What was the Q1 FY27 Digital rupee loss and revenue, and how much of the 330 bps QoQ gain came from revenue vs cost?", from_finding_id: "P-A3-02"}
  - {q: "What were FY26 and Q2 FY26 Digital margin in % and Rs?", from_finding_id: "P-A3-03"}
  - {q: "In which fiscal quarter will Digital margin reach zero, and is it EBITDA, EBIT or contribution?", from_finding_id: "P-A3-04"}
  - {q: "Did the National Court deliver its 13-Oct-2026 VAT judgment on 365.80 Cr, and for or against the Group?", from_finding_id: "R-A3-08"}
  - {q: "What is FY27 capex guidance and the Board's net debt / EBITDA ceiling?", from_finding_id: "R-A3-23"}
  - {q: "Which entity raised the 2,628.15 Cr H1 long-term debt, and is it parent-guaranteed (yes/no)?", from_finding_id: "R-A3-05"}
  - {q: "Total staff cost optimisation programme cost, amount remaining, end quarter?", from_finding_id: "R-A3-11"}
  - {q: "Expected FY27 ETR, and remaining unrecognised DTA on accumulated losses?", from_finding_id: "R-A3-14"}
  - {q: "Campaign Registry: cause of the Q2 FY26 result dip (122.93 to 75.58), Canada entity contribution before its 14-Jan-2026 exit, and any contract or rule renewal within 12 months?", from_finding_id: "R-A3-20"}
  - {q: "Parent wrote off 116.73 of 161.23 Cr H1 bad debts (standalone ratio 8.57% vs 1.90%): which customer or contract, and what further amount is at risk?", from_finding_id: "R-A3-06"}
  - {q: "Is the 50.00 Cr contractual-obligation provision a receivable, advance or guarantee, and same counterparty as the write-offs?", from_finding_id: "R-A3-13"}
  - {q: "Which associate received 356.10 Cr in H1, what return is expected (TTM associate share 16.66 vs carrying 2,331.73), and what capital is committed for FY27-FY28?", from_finding_id: "R-A3-07"}
  - {q: "Name the two management-furnished unreviewed subsidiaries (Q2 loss 14.83 on revenue 3.11).", from_finding_id: "R-A3-07"}
  - {q: "DoT demand aggregate at 31-Mar-2026 and 30-Jun-2026 vs 7,844.57; any new notice in Q2?", from_finding_id: "R-A3-09"}
  - {q: "Standalone carrying value of Kaleyra, Inc. vs FMV USD 92.625m; expected standalone gain or loss?", from_finding_id: "R-A3-10"}
  - {q: "Expected Kaleyra transfer completion date; any TCNL external financing or stake sale planned?", from_finding_id: "R-A3-29"}
  - {q: "Kaleyra Africa exit on 04-Sep-2026: mode, consideration, P&L impact?", from_finding_id: "R-A3-27"}
  - {q: "TComm Turkey (wef 21-May-2026): purpose and capital committed?", from_finding_id: "R-A3-28"}
  - {q: "Fire provision 30.10 Cr: insurance claim filed, amount, expected recovery date?", from_finding_id: "R-A3-12"}
  - {q: "H1 FY27 tax refund received and remaining refundable balance in 1,498.33 Cr non-current tax assets?", from_finding_id: "R-A3-15"}
  - {q: "Which actuarial assumption drove the standalone Q1 FY27 OCI loss of 9.37 Cr?", from_finding_id: "R-A3-16"}
  - {q: "Forfeiture reversal inside H1 SBP accrual 2.02 Cr vs 24.01 Cr; new FY27 grants (yes/no)?", from_finding_id: "R-A3-18"}
  - {q: "Transformation Services revenue -33.70% YoY: client loss (how many) or group in-sourcing?", from_finding_id: "R-A3-21"}
  - {q: "Does Zubin Adil Patel leave, move within the group, or retire on 01-Nov-2026?", from_finding_id: "R-A3-24"}
  - {q: "Reconcile press-release Q2 FY26 Data revenue 5,179 to filed 5,204.47; define Digital Portfolio.", from_finding_id: "R-A3-25"}
  - {q: "Asset held for sale 7.40 Cr: identity, buyer, price, completion date?", from_finding_id: "R-A3-01"}
  - {q: "Was FY25 Digital restated to the current perimeter; what revenue came in (Commotion, FY26 acquisition cash 136.96) and went out (Mgage, Kaleyra Africa)?", from_finding_id: "P-A3-05"}
  - {q: "Does any earlier quantified margin or revenue target still stand (yes/no)?", from_finding_id: "P-A3-06"}
  - {q: "When did the Tower structure take effect, and which of the 11 named heads joined in the last 12 months?", from_finding_id: "P-A3-07"}
  - {q: "Q2 FY27 AI-platform revenue and paying-customer count?", from_finding_id: "P-A3-08"}
  - {q: "India GPU capex amount, utilisation, and is its depreciation inside the Digital margin?", from_finding_id: "P-A3-09"}
monitorables:
  - {item: "National Court VAT judgment outcome (365.80 Cr)", implied_date: "scheduled 2026-10-13; disclosure by Q3 FY27 results", source_ref: "L572; R1558; R-A3-08"}
  - {item: "Q2 FY27 concall transcript for Role 5", implied_date: "call held 2026-10-15; transcript pending", source_ref: "P-L33"}
  - {item: "Ridhi Sood takes office as Company Secretary", implied_date: "2026-11-01", source_ref: "L72; L1542; R1585"}
  - {item: "Kaleyra, Inc. transfer to TCNL completes", implied_date: "ND; check Q3 FY27 consolidation list", source_ref: "L45-53; L1519-1524; R-A3-10"}
  - {item: "Q3 FY27 consolidated Op EBITDA margin vs 21.0% bull / 19.5% bear", implied_date: "quarter end 2026-12-31; filing date ND", source_ref: "Step 8C"}
  - {item: "Digital portfolio breakeven", implied_date: "ND", source_ref: "P-L132; P-A3-04"}
  - {item: "Staff cost optimisation programme end", implied_date: "ND, ongoing", source_ref: "L528-531; R-A3-11"}
  - {item: "Asset held for sale (7.40) disposal", implied_date: "ND", source_ref: "L344; L460; R-A3-01"}
  - {item: "CWIP 1,120.81 capitalisation and D&A step-up", implied_date: "ND", source_ref: "L318; R-A3-23"}
  - {item: "Fire provision true-up", implied_date: "ND", source_ref: "L541-542; R-A3-12"}
  - {item: "DoT AGR appeals at SC and TDSAT", implied_date: "ND", source_ref: "L552-559; R-A3-09"}
  - {item: "CEO H2 FY27 momentum claim tested", implied_date: "Q3 and Q4 FY27 results", source_ref: "L1375-1376"}
  - {item: "DC-to-DC connectivity USD 1bn opportunity", implied_date: "ND", source_ref: "L1400"}
  - {item: "FY27 full-year cash flow (FCF; CFO/EBITDA vs FY26 92.88%)", implied_date: "year end 2027-03-31; filing date ND", source_ref: "Step 5"}
  - {item: "FY27 Annual Report: actuarial basis of Q1 OCI; entity-level subsidiary results", implied_date: "ND, after FY27 close", source_ref: "L639; R-A3-16"}
  - {item: "Five plan levers and reset baseline", implied_date: "ND", source_ref: "P-L85; P-L122-128; P-A3-07"}
flags:
  - "PRE-THESIS: no Notion page, no Decision Status, no Spear line; /step1 gates any pipeline run"
  - "Q2 profit jump is a subsidiary event: non-parent sources supplied 185.39 (89.6%) of the 206.80 QoQ parent PAT rise (subsidiaries plus eliminations 192.08 before associates and NCI); cause undisclosed; Digital explains about half at most (R-A3-04)"
  - "Half of the 248.26 YoY EBITDA gain is cost-out; gross spread -305 bps"
  - "Net debt +1,606.60 (+16.8%) to 11,197.04 in H1; FCF after lease and interest (584.30); dividend 498.78 > H1 parent PAT 475.26"
  - "Debt migrated to subsidiaries (+2,482.20); standalone Reg 52(4) leverage ratios flatter the consolidated position (R-A3-05)"
  - "DoT contingent liability 7,513.71 = 2.21x consolidated parent equity; emphasis of matter (R-A3-09)"
  - "VAT judgment on 365.80 due 13-Oct-2026; note says the Group 'awaits the National Court's decision' (R-A3-08)"
  - "ETR 26.80% rests on recurring deferred credits; current tax 36.14% (R-A3-14)"
  - "OCF supported by 315.42 lower tax paid (R-A3-15)"
  - "Credit costs: 161.23 H1 write-offs (116.73 at parent); standalone bad-debts ratio 8.57% vs 1.90%; current ratio 0.36 vs 0.57; 50.00 recoverability provision; counterparties unnamed (R-A3-06, R-A3-13)"
  - "'One-time' staff charge recurs every quarter shown (R-A3-11)"
  - "Campaign Registry: 23.80% of segment result on 4.15% of revenue; YoY +114.38% on a depressed base, H1/H1 +55.75%; Canada entity deconsolidated 14-Jan-2026 (R-A3-20)"
  - "Associates 2,331.73 (68.6% of parent equity, ~140x TTM share of profit 16.66) on unreviewed numbers; 356.10 added in H1 (R-A3-07)"
  - "Press-release and deck metrics do not tie to filed lines; Digital chart framing flatters (R-A3-25, P-A3-01..05)"
  - "Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); tracker rows not supplied; Role 5.5 not run"
  - "Concall held 15-Oct-2026; transcript not in run; Role 5 pending"
plain_language_brief_included: true
analyst_note: "Group numbers look strong: revenue +9.6%, Op EBITDA +21.2%, margin 21.26%. Two facts temper them. First, half the EBITDA gain is opex reduction while the network spread fell 305 bps, and non-parent sources supplied about 90% (185.39) of the QoQ parent PAT rise with no cause stated. The Digital loss cut can explain at most about 101 of the 195 QoQ subsidiary EBITDA rise unless Q1 Digital revenue exceeded Q2's, so one-off cost credits or other subsidiaries must carry the rest. Q3 margin against 21.0%/19.5% separates the readings. Second, the balance sheet weakened: net debt +16.8% in six months, debt moved into subsidiaries, FCF after lease and interest negative, dividend above H1 PAT, and 356 more into associates carried at ~140x their TTM profit share. Campaign Registry's +114% YoY rests on a weak base; H1/H1 is +56%. Cash is INDETERMINATE-WITH-DIRECTION. No thesis exists; the spear gate applies before any pipeline run."
review_path: "runs/tatacomm-q2fy27/work/review_tatacomm_q2fy27.md"
correction_loop: 1
```
