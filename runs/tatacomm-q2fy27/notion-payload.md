# NOTION PAYLOAD: TATACOMM Q2 FY27 quarterly review (NOT WRITTEN; awaiting operator batch approval)

Saved per orchestrator WRITE GATE (operator instruction for this batch: do not wait at the gate; the operator approves all writes later in one batch). Nothing below has been written to Notion. Decision Status is NEVER written.

## Target
- Live search 2026-10-17 found NO Tata Communications page in COMPANIES MASTER (data source collection://345bb2b9-d3ab-8032-9b46-000ba16ab827).
- Proposed operation: CREATE one new page in COMPANIES MASTER (parent data source collection://345bb2b9-d3ab-8032-9b46-000ba16ab827). Operator decides whether a pre-thesis name gets a page. If the operator declines, store this file only.

## Properties (create-page call)
| Property | Value |
|---|---|
| Name | Tata Communications Limited |
| Ticker | TATACOMM |
| Sector | Telecom |
| SECTOR | Telecom |
| Analysis Date | Oct-26 |
| date:Analysis Date 1:start | 2026-10-17 |
| Key Notes | (line below, verbatim) |
| Decision Status | NOT WRITTEN (operator-only) |

Key Notes line (first entry; no prior entries exist; pipes inside the line escaped as \| when written):

17-Oct-2026 Q2 FY27 QUARTERLY REVIEW (/run-quarterly, results + deck, no concall; PRE-THESIS READ, no spear on record): verdict PROCEED WITH FLAGS; cash conversion INDETERMINATE-WITH-DIRECTION; A5 COMPLETE after 1 correction loop. Consol revenue Rs 6,687.89 Cr (+9.64% YoY); Op EBITDA Rs 1,421.88 Cr (+21.15%), margin 21.26% (+202 bps) but half the gain is cost-out and network spread -305 bps. Parent PAT Rs 341.03 Cr (+86%); subsidiaries plus eliminations supplied 192.08 (92.9%) of the 206.80 QoQ rise (all non-parent sources 185.39, 89.6%), cause undisclosed. Net debt +Rs 1,606.60 Cr (+16.8%) to 11,197.04 in H1; FCF after lease and interest -584.30; dividend above H1 PAT; debt migrated to subsidiaries. DoT contingent Rs 7,513.71 Cr (2.21x consol parent equity) and Rs 365.80 Cr VAT judgment (due 13-Oct-2026, outcome not disclosed) both under emphasis of matter. Next test: Q3 FY27 Op EBITDA margin >=21.0% real / <=19.5% one-off. /step1 gates any pipeline run. Decision Status not set (operator-only).

## Page content (insert_content, position: end; split across sequential calls at the section breaks below)

### Part 1 of 4: A4 merged review (full, including the PLAIN-LANGUAGE BRIEF and the correction loop log)

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


### Part 2 of 4: A3 forensics, results

# A3 FORENSIC NOTES - Tata Communications Limited (TATACOMM) - results - q2fy27

Inputs read: A1 structured extraction (R001-R1778, all 1,778 rows read), A1 fulltext (L1-L1569, all pages 1-33 read), A2 ledger (all sections, 1,778 IDs referenced, gate_a2 pass). Source PDF and inputs/ not opened.
Prior-quarter fulltext: NOT AVAILABLE (ND). F5 and F15 cannot be verbatim-diffed against Q1 FY27; they rest on in-document dates and qualifiers only.
Notion monitoring checklist: NONE (pre-thesis read).
Units: Rs crore unless stated. "L" = fulltext line number. "Consol" = consolidated. "Parent PAT" = profit attributable to equity holders of the parent.

## RECONCILIATION STATEMENT
- Ledger IDs in structured file: 1,778. IDs read at their structured row and checked against the fulltext line: 1,778. ledger_reconciled_pct: 100.
- Arithmetic re-checks that tie (no finding): consol EBITDA, standalone Reg 52(4) ratios (D/E 0.34, asset cover 1.60, current ratio 0.36, DSCR 0.35, bad-debt ratio 8.57%, debtors turnover 2.71, operating margin 10.49%, net margin 6.79%), consol equity roll-forward (exact), NCI roll-forward (exact), DoT contingent-liability arithmetic (7,844.57 - 276.68 - 54.18 = 7,513.71), Attachment D share-swap value (3,17,632 x USD 291.6 = USD 92.62m).
- A2 flags resolved here:
  - FOOTNOTE_UNRESOLVED R1767 (EBITDA): RESOLVED by computation. Press-release EBITDA 1,422 = Income from operations 6,687.89 less network 3,181.47, employee 1,178.75 and other expenses 905.79 = 1,421.88 (L135, L139-143). Margin 21.26%, Q2 FY26 1,173.62 / 19.24%, growth 21.2%, +202 bps: all tie.
  - FOOTNOTE_UNRESOLVED R1766 (data revenue): NOT resolved. See A3-25.
  - FOOTNOTE_UNRESOLVED R1768 (digital margin -3.6%): NOT reconcilable. No digital P&L in the filing.
  - SIGNATURE_BEFORE_MEETING_END (R1323, R1628, R1641): judged NOT a defect. Sequence is coherent: CEO 12:58:01 (L1028), auditor standalone 13:04:44 (L1335), auditor consol 13:05:38 (L1159), meeting close 13:45 (L33), CS letter 13:52:19 (L97). The auditor signs after management, results item (i) is approved before the other agenda items.
  - OUTCOME_NOT_DISCLOSED (R1558, R1608): carried to A3-08.
  - NAME_NOT_DISCLOSED R1442: the discontinued subsidiary is identifiable by date match. Note 5 loss of control "On April 22, 2025" (L576) equals "Netfoundry Inc. (upto April 22, 2025)" (L1233). [INFERENCE, date match only.] R1439 (VAT jurisdiction) and R1433 (Campaign Registry operator) stay NOT FOUND in the note text; the entity list carries "Campaign Registry Inc (US)" (L1244).

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R590-R592, R593, R446-R447, R673-R676 | L460, L461, L344 | "Advance received towards assets held for sale  4.00" / "Proceeds from disposal of asset held for sale (refer note 2b)  -" | FORWARD-SIGNAL | An asset carried at 7.40 (unchanged since Mar) has a fresh Rs 4.00cr advance in H1 FY27, but no proceeds and no gain yet. The zero "Gain on sale of asset held for sale" exceptional line (L517) is set to reactivate on completion. Ask: asset, buyer, price, expected completion date. |
| A3-02 | F1 | R126-R137, R215-R226, R499, R526, R718-R737 | L162-163, L210-211, L589-597 | "12 Loss on sale of subsidiary (refer note 5)  -  -  -  -  (42.19)  (42.19)" | NEUTRAL-FACT | Template carry of the FY26 NetFoundry loss of control (FCTR recycle, L597). Zero in all FY27 columns; lines drop out as comparatives roll. Note 5 table shows PAT "-" in H1 FY26 against revenue 3.27 (L589-591), and the H1 FY27 cell is blank, not "-" (L589). Immaterial. |
| A3-04 | F2 | R144-R149, R150-R155, R113-R118, R826-R831, R073-R075, R796-R798 | L166, L637, L146, L631 | "Equity holders of the parent  341.03  134.23  183.06" vs standalone "Profit for the period/ year (7 - 8)  125.86  104.45  210.94" | AMBIGUOUS | S-vs-C PAT gap (parent PAT less standalone PAT) as % of standalone PAT: Q2 FY26 -13.2%, Q1 FY27 +28.5%, Q2 FY27 +171.0%. Swing far above the 5pp test. Decomposed: subsidiaries + eliminations 213.00 (Q1 20.92), associates (3.25) (Q1 4.35), NCI absorbs 5.42 of losses. Parent PAT rose 206.80 QoQ; subsidiaries/eliminations supplied 192.08 (93%). Subsidiary pre-exceptional PBT rose 195.34 (130.47 to 325.81); standalone fell 7.3% (187.27 to 173.63). Subsidiary EBITDA (consol less standalone) rose 195.09 (756.07 to 951.16) on only 89.54 more revenue. Revenue gap is stable (70.4%, 72.1%, 72.3% of consol), so the profit jump is a cost or one-off event inside subsidiaries. Ask: which entities, and does any Q2 credit (provision release, FX, SBP reversal) sit in the 63.07 QoQ fall in consol other expenses or the 60.98 fall in employee cost. |
| A3-05 | F2 | R1174-R1179, R1205-R1210, R633-R638, R998-R999, R1020-R1021, R463-R464, R477-R478, R1041-R1042, R1053-R1054, R1256-R1263, R1731-R1732 | L854-855, L877-878, L476-477, L751, L957, L956 | "Loan repaid by subsidiaries  2,641.16" / "Proceeds from Long-term borrowings  2,628.15" (consol) / "Proceeds from long-term borrowings (net off arrangement fees)  -" (standalone) / "# Decreased mainly due to loan repaid by subsidiary as per repayment terms." | FORWARD-SIGNAL | Debt moved down the group in H1. All new long-term debt (2,628.15) was raised outside the parent; a subsidiary repaid 2,641.16 to the parent; the parent repaid 1,760.48 of debentures (L878, L956). Standalone gross debt fell 1,209.34 (4,751.10 to 3,541.76); subsidiary gross debt (consol less standalone) rose 2,482.20 (5,830.58 to 8,312.78, +42.6%). Standalone Reg 52(4) ratios improved (D/E 0.45 to 0.34, asset cover 1.14 to 1.60) while consol gross debt rose 1,272.86. Standalone loans to subsidiaries fell 1,919.53 (2,787.45 to 867.92), so standalone interest income (86.58 in H1, L817) will fall; consol is unaffected by that elimination but bears the subsidiary interest cost. Ask: borrower entity, currency, tenor, rate, parent guarantee. |
| A3-06 | F2 | R529-R534, R1104-R1106, R1116-R1120, R1264-R1265, R434-R435, R556-R558 | L419-420, L825, L829, L940, L338 | "Bad debts written off  161.23  28.67  57.79" / "Allowance/(Reversal) for trade receivables  (91.33)  (69.56)  (120.12)" | AMBIGUOUS | Consol net credit cost H1 FY27 = +69.90 (161.23 - 91.33) vs a net release of (40.89) in H1 FY26: a 110.79 swing. Standalone nets to 4.92 (116.73 - 111.81), so subsidiaries carry about 64.98. Standalone bad-debt ratio 8.57% for half a year vs 1.90% for all of FY26 (L940). Consol receivables +433.03 (+10.4%) since Mar; WC outflow (454.20) (L432). Q1 also booked a 50.00 "recoverability" provision (A3-13). Ask: customer or contract behind the write-offs, quarter split, and whether more provisions remain. |
| A3-07 | F4 | R1343-R1356, R1335-R1342, R1750-R1752, R416-R417, R596-R598, R113 | L1125-1140, L1113-1123, L326, L462, L158 | "these interim financial results are not material to the Group." | AMBIGUOUS | PAT test passes: unreviewed absolute contribution Q2 = two subsidiaries' loss 14.83 + associates' share loss 3.26 = 18.09, 5.4% of consol PAT 335.61 (H1 6.1%); other-auditor subsidiary adds 2.50 (0.7%). Below 10%. Trend vs prior: ND. But the balance-sheet exposure is not small: investments in associates 2,331.73 (+348.86 in H1, driven by 356.10 new investment, L462) equals 68.6% of parent equity 3,401.18, and it rests on management-furnished, unreviewed associate numbers. The associate share turned to a loss in Q2: (3.25) vs 4.35 in Q1 and 10.70 in Q2 FY26. The "not material" statement is the Management's, relayed by the auditor. The two unreviewed subsidiaries lose 4.8x their revenue (14.83 loss on 3.11 revenue). Ask: which associate took the 356.10, what further capital calls are committed, and which two subsidiaries are unreviewed. |
| A3-08 | F5 | R1558, R1559, R1604-R1608, R714-R716, R1334, R1748, R1691 | L571-574, L1107-1109 | "The National Court scheduled the deliberation and judgment of the appeal for 13 October 2026, and the Group awaits the National Court's decision." | FORWARD-SIGNAL | Binary outcome on Rs 365.80cr (EUR 33.6m), 10.8% of parent equity. The judgment date (13-Oct-2026) fell two days before the board and auditor sign-off (15-Oct-2026), and the note gives no post-period update. Payment is suspended pending appeal (L570-571), so an adverse ruling is a cash and P&L event, not only a disclosure. Prior-quarter note text ND, so no verbatim diff of the emphasis paragraph. Ask: was the decision delivered, and what was it. |
| A3-09 | F5 | R706-R713, R1316-R1322, R1332-R1333, R1360-R1361, R1689-R1690, R1747, R1765 | L545-547, L560-562, L1101-1105, L1319-1323 | "aggregating to ₹ 7,844.57 crores for financial years (FY) ranging from FY 2005-06 to FY 2024-25, which have been revised over a period of time" | AMBIGUOUS | DoT contingent liability 7,513.71 is 2.21x consol parent equity 3,401.18 and 72.9% of standalone net worth 10,306.04. Emphasis of matter in both reports, conclusion not modified. "Revised over a period of time" means the aggregate moves; without the Q1 text the change in aggregate, year range and provision (54.18) cannot be diffed. Ask: aggregate at 30-Jun-2026 and 31-Mar-2026, any new notice in Q2, and hearing dates at SC/TDSAT. |
| A3-10 | F6 | R1550-R1552, R1574-R1579, R1402-R1410, R1425-R1426, R1546-R1547, R1775-R1778 | L45-53, L1493-1524 | "The Board of Directors has approved the transfer of the entire shareholding held by the Company in Kaleyra, Inc., to Tata Communications (Netherlands) B.V." / "not expected to have any material impact on the consolidated financial position" | FORWARD-SIGNAL | Kaleyra, Inc. (100 shares, FMV USD 92.625m) moves from the parent to the Netherlands holdco for 3,17,632 TCNL shares at USD 291.6. Completion date not stated (ND). Only the consolidated impact is addressed; the standalone carrying value of the Kaleyra investment vs the USD 92.625m FMV is not disclosed, so a standalone gain or loss on transfer is open. [INFERENCE] Housing Kaleyra under an overseas holdco creates room for overseas financing or a later stake event; the document states only simplification. Ask: standalone book value of Kaleyra, INR value of the FMV, expected completion, and purpose beyond simplification. |
| A3-11 | F6 | R1555-R1556, R1560, R667-R672, R1276-R1281, R1684, R1739 | L528-531, L515, L990-993, L972 | "the Group is undertaking organisational changes to align its current and prospective business requirements in a phased manner" ... "has incurred a one-time charge with respect to staff cost optimization." | AMBIGUOUS | A charge labelled "one-time" recurs in three of the last five quarters shown: (98.26) Q2 FY26, (44.78) Q1 FY27, (36.54) Q2 FY27. H1 FY26 (118.70) vs FY26 (114.64) implies a net credit of 4.06 in H2 FY26. The program is ongoing ("phased manner") with no end date or total cost stated. Employee cost fell 60.98 QoQ and 90.82 YoY (L140). If the program continues, part of this cost belongs in run-rate earnings. Ask: total program cost, remaining charge, end date, annualised saving. |
| A3-12 | F7 | R1687, R1742, R685-R690, R1294-R1299, R523-R525, R1086-R1088, R1672, R1677, R1700, R1707 | L541-542, L1003-1004, L522, L417, L495 | "recognized a provision for losses arising from a fire incident at a co-located third party data centre premise basis the available information/estimate." | AMBIGUOUS | Q1 provision 30.10 consol (2.65 standalone), of which 25.67 is PPE impairment (L417, L495). The note hedges the amount as an estimate. True-up can run either way: insurance or landlord recovery (gain) or further loss. Q2 line is zero. Ask: insurance claim status, customer service credits, any further impact. |
| A3-13 | F7 | R1688, R1743, R691-R696, R1300-R1305 | L543-544, L1005-1006, L524, L981 | "made provision towards certain amounts based on management's assessment of their recoverability under the contractual obligations." | AMBIGUOUS | Rs 50.00cr booked in Q1 at the parent (same 50.00 in both tables), counterparty and contract not named. Reads with A3-06 (credit write-offs). Ask: counterparty, nature (receivable, advance, guarantee), and whether recovery action is under way. Strict hedge-lexicon hits in notes: zero; the hedges here are estimate language. |
| A3-14 | F8 | R094-R105, R814-R825, R422-R423, R1002-R1003, R739-R740, R1696 | L153-154, L635-636, L329, L740, L600-601 | "b. Deferred tax  (43.27)  (30.05)  (41.29)  (73.32)  (96.26)  (180.62)" | FORWARD-SIGNAL | Deferred tax is a credit in every period shown, consol and standalone. Consol ETR: Q2 26.8%, Q1 40.7%, Q2 FY26 32.3%, H1 FY27 31.2%, FY26 30.0%. Current tax alone runs 36.1% of PBT in Q2 (42.0% in H1). The deferred credit shields 935 bps of Q2 PBT (1,087 bps in H1). Consol DTA rose 67.02 (901.22 to 968.24). FY26 includes a 73.25 DTA recognised in P&L against accumulated losses (L600-601). Standalone ETR is near statutory (Q2 25.3%) but also carries a deferred credit of 881 bps. Risk: if DTA recognition stops, reported ETR steps up toward the 36% current rate. No "tax relating to earlier years" line exists in the template. |
| A3-15 | F8 | R577-R582, R424-R425, R1004-R1005, R1148-R1153, R487-R488 | L440-441, L330, L741, L842 | "Income tax (paid)/refund (net)  (97.79)  (413.21)  (720.37)" | FORWARD-SIGNAL | Consol OCF rose 609.06 YoY (953.64 to 1,562.70); 315.42 of that is lower net tax paid. Non-current tax assets fell 241.04 (consol) and 185.95 (standalone): refunds received. Standalone shows a net refund of 9.60 vs payment of 186.50. This OCF support is non-recurring. Ask: refund amount received, years, and remaining refundable balance. |
| A3-16 | F9 | R832-R837, R157-R175, R738-R740, R1696 | L639, L188, L598-599 | Standalone "Other Comprehensive Income / (Loss) (net of tax)  3.08  (9.37)  3.49  (6.29)  4.98  0.97" | AMBIGUOUS | Standalone Q1 FY27 OCI (9.37) exceeds the full FY26 OCI of 0.97 by 9.7x: the single-quarter swing test fires. It coincides with the Q1 Labour Codes actuarial re-estimate (reversal 11.93 in P&L, L1000-1002), so a changed actuarial basis or discount rate is the likely driver [INFERENCE]. Verify assumptions at the FY27 Annual Report. Consol OCI has no breakdown; FY26 OCI 102.24 includes a 335.24 fund gain (L598), so underlying FY26 OCI was (233.00). |
| A3-17 | F10 | R194-R199, R845-R850, R453-R454, R1035-R1036, R648-R650, R1222-R1224, R203-R214, R856-R867 | L200, L481, L883, L207-208 | "Proceeds from exercise of share options  0.09  -  -" | NEUTRAL-FACT | Paid-up capital 285.00 (Mar) to 285.02 (Jun) to 285.09 (Sep): about 90,000 new shares, consideration 0.09 = face value, so exercise at par. Dilution 0.03%. Basic-diluted EPS spread: Q2 FY27 0.02 (11.96 / 11.94), Q2 FY26 0.01, FY26 0.06. Not widening. |
| A3-18 | F10 | R538-R540, R1089-R1091, R043-R048, R766-R771 | L422, L820, L140 | "Accrual for share-based payments  2.02  24.01  45.01" | AMBIGUOUS | Consol SBP accrual fell 91.6% YoY in H1 (24.01 to 2.02); standalone 20.89 to 0.83. A collapse this size suggests forfeiture reversals on departing staff (ties to A3-11) or no new grants [INFERENCE]. It lowers H1 employee cost by about 22 vs H1 FY26, roughly 11 per quarter, inside EBITDA. Ask: reversal amount, grants in FY27, plan status. |
| A3-19 | F11 | R453-R462, R1035-R1040, R1274-R1275, R852-R853, R642-R644, R1216-R1218 | L361-368, L774-776, L954, L647-648, L479 | "Equity attributable to equity holders of the parent  3,401.18" vs "10. Net worth (₹ in crores)  10,306.04" | NEUTRAL-FACT | Tie-outs pass: consol 285.09 + 3,116.09 = 3,401.18, and the roll-forward is exact (3,447.04 + TCI 450.81 - dividend 498.78 + capital 0.09 + SBP 2.02). Standalone roll-forward leaves 1.19 unexplained. Gap above 5%: consol parent equity is 33.0% of standalone net worth, gap 6,904.86. Candidate reconciling items: accumulated losses of overseas subsidiaries, goodwill and investment eliminations, FCTR, NCI (shown separately at 197.97). Consequence: consol gross borrowings are 3.49x parent equity (3.07x in Mar) while the standalone D/E shown to debenture holders is 0.34. Dividend 498.78 (Rs 17.50 per share vs Rs 25.00 a year earlier, -30%) exceeded H1 parent PAT 475.26, so parent equity fell 45.86. Standalone "Reserves excluding Revaluation reserve" 10,087.63 vs Other equity 10,293.69: 206.06 (2.0%) unexplained, below the 5% test (candidate: revaluation or other reserve). |
| A3-20 | F12 | R264-R269, R306-R311, R353-R356, R385-R388, R1507-R1508, R1668 | L238, L246, L273, L282, L1244-1245 | "Campaign Registry  162.03  147.14  75.58" | FORWARD-SIGNAL | One US messaging-registry business now earns 23.8% of Q2 segment result on 4.2% of revenue (15.3% of result in Q2 FY26; 21.2% in FY26). Result +114.4% YoY, revenue +37.1% YoY, margin 58.3%. Net segment assets 843.59. Group profit growth is concentrating in a single regulated niche. Campaign Registry Inc (Canada) left the group on 14-Jan-2026. Ask: drivers, contract and regulatory durability, Canada exit reason. |
| A3-21 | F12 | R252-R257, R270-R275, R294-R299, R345-R348, R377-R380 | L236, L239, L271, L280 | "Transformation Services  190.11  194.59  286.74" | AMBIGUOUS | Revenue -33.7% YoY (96.63); inter-segment revenue fell 38.96 (51.81 to 12.85), so 57.67 of the fall is external or unexplained. Segment liabilities -35.7% YoY (263.40 to 169.26); assets -16.2%. Result held (47.89 vs 45.08). Falling liabilities read as either WC unwinding or a shrinking book. Ask: client loss or in-sourcing by the group, and outlook. |
| A3-22 | F12 | R246-R251, R288-R293, R037-R044, R061-R062, R341-R344, R373-R376 | L235, L243, L139-143, L270, L279 | "Data Services  425.74  250.56  313.59" | AMBIGUOUS | Data Services result +175.18 QoQ on revenue +107.41: incremental margin 163%. Segment margin 7.3% vs 4.4% Q1 and 6.0% Q2 FY26. Segment assets +708.86 since Mar while segment liabilities fell 354.91, so the build is funded through unallocated borrowings. Ask: Q2 one-offs in Data Services cost (provision releases, SBP reversal, FX), and the sustainable margin. |
| A3-23 | F12 | R393-R396, R404-R405, R414-R415, R584-R586, R580-R582, R463-R464, R477-R478, R432-R439, R639-R647 | L284, L318, L323, L458, L441, L373, L382, L337-340 | "Unallocated Liabilities  13,555.00 ... 12,428.62" / "(b) Capital work-in-progress  1,120.81  761.50" | FORWARD-SIGNAL | Net debt (borrowings less cash, bank and current investments) rose 1,606.60 (+16.8%) in H1, from 9,590.44 to 11,197.04. Capex 1,500.69 (+31.7% YoY) used 96% of OCF 1,562.70; after lease 292.51 and interest 353.80 the pre-dividend cash gap is 584.30, before the 356.10 associate investment and 498.78 dividend. CWIP +359.31 (+47.2%), intangibles under development +28.42. D&A steps up when CWIP capitalises. The build is debt-funded. Ask: capex guidance, CWIP commissioning dates, net-debt ceiling. |
| A3-30 | F12 | R240-R245, R282-R287, R337-R340, R369-R372, R869-R874, R893-R898 | L234, L242, L269, L278, L675 | "Voice Solutions  18.13  20.61  34.93" | CONFIRMATORY-NEGATIVE | Voice result fell in each period shown: 34.93 (Q2 FY26), 20.61 (Q1), 18.13 (Q2), -48.1% YoY on revenue -8.8%. Standalone Voice loses (27.02) a quarter. Voice segment liabilities (314.25) exceed assets (275.08). Structural decline, no reversal signal in the filing. |
| A3-24 | F13 | R1411-R1417, R1428-R1430, R1553-R1554, R1580-R1581, R1585, R1652 | L67-72, L99-100, L1540-1542 | "Reason for change | Appointment of Ms. Ridhi Sood as the Company Secretary and Compliance Officer" | AMBIGUOUS | The incumbent, Zubin Adil Patel, signs this letter as Company Secretary (L99-100). The filing discloses the successor from 1-Nov-2026 but not the incumbent's cessation, date, or reason. Ask: does he leave, move within the group, or retire. Board outcome otherwise carries no AR, AGM, record date, dividend, director, auditor, ESOP or capital-raising item (A2 absence row A5). |
| A3-25 | F14 | R1365-R1367, R1372-R1380, R1766, R246, R248, R1523 | L1363-1364, L1382-1384, L235 | "Data Revenue  5,810  5,179  12.2%" / "digital platform revenue grew by 18.6% YoY" vs table "Digital Portfolio Revenue" | AMBIGUOUS | The press release's Q2 FY26 data revenue base (5,179) is 25.47 below the filed Data Services segment revenue (5,204.47). On filed numbers data growth is 11.7%, not 12.2%. Q2 FY27 5,810 also does not round from 5,810.99. The headline says "digital platform", the table says "Digital Portfolio"; neither figure, nor the -3.6% digital margin, ties to any filed line. Ask: definition of press-release data revenue and digital portfolio, and the reconciliation to segment revenue. |
| A3-26 | F14 | R1653, R1745-R1746, R1282-R1287, R1734-R1736, R718-R722, R1387-R1389 | L41, L1082, L1111, L973-976, L202, L589, L1387 | "have issued a Limited Review Report with an unmodified opinion" vs auditor "Accordingly, we do not express an audit opinion." | NEUTRAL-FACT | Cumulative drafting set, each immaterial: (1) board letter calls the review an "opinion"; a review gives a "conclusion" (L1111). (2) Standalone exceptional table numbering is broken: "2. Gain on sale..." / "3. (refer note b)" / "4. Statutory Impact..." (L973-976), so it runs 1-6 against the consolidated 1-5. (3) Consol line 18 "Reserves excluding Revaluation reserve" is blank for the audited FY26 column (L202); standalone fills it (L647). (4) Note 5 table H1 FY27 cell blank (L589). (5) Press release PAT growth "86.2%" vs 86.3% computed from 341.03 / 183.06 (L1387). (6) "one-time" label on a recurring charge (A3-11). Governance data point only. |
| A3-27 | F15 | R1509, R1634, R1757 | L1246 | "Kaleyra Africa (pty) Limited (upto September 04, 2026)" | AMBIGUOUS | Exit inside Q2 FY27. No note states the mode (sale, liquidation, strike-off), consideration, or gain/loss, and no discontinued-ops or disposal line moved (L461, L465 zero for H1 FY27). Read with the Kaleyra, Inc. move to TCNL (A3-10). Ask: mode of exit, consideration, P&L impact. |
| A3-28 | F15 | R1519, R1639, R1762, R599-R601 | L1256, L463 | "TComm Turkey Dijital Çözümler Limited Şirketi (wef May 21, 2026)" | FORWARD-SIGNAL | New subsidiary in H1 FY27 with no acquisition outflow (L463 zero), so incorporated, not bought [INFERENCE]. New geography entry; purpose undisclosed. Whether it already sat in the Q1 FY27 list cannot be checked (prior list ND). Ask: purpose, capital committed. |
| A3-29 | F15 | R1502, R1464, R1578-R1579 | L1519-1521, L1239, L1197 | "Kaleyra, Inc. will cease to be a direct subsidiary of the Company and will become a direct subsidiary of TCNL" | FORWARD-SIGNAL | Approved relationship change (direct to step-down subsidiary). Expect it in the next consolidation list or a later one; group perimeter unchanged. Tracks A3-10. |

(Ids A3-03 not used: folded into A3-11 during drafting; numbering kept stable for downstream reference.)

## CHECKLIST SCORECARD

| check | status | basis (one line) |
|---|---|---|
| F1 | FINDING | 36 zero-standing lines read. Template carries for FY26 NetFoundry discontinued ops (A3-02); a pending held-for-sale disposal with fresh advance (A3-01). Other zeros (Q1 one-offs, dividend from subs, acquisition of subsidiary, sublease) are period-specific. |
| F2 | FINDING | S-vs-C PAT gap moved -13.2% to +28.5% to +171.0% of standalone PAT; Q2 jump is a subsidiary event (A3-04); debt migrated to subsidiaries (A3-05); subsidiaries carry the net credit charge (A3-06). |
| F3 | PASS | Standalone and consol cost lines differ widely (network 669.97 vs 3,181.47; employee 396.50 vs 1,178.75); no shell pattern; no going concern paragraph. Individual entity cost lines not disclosed. |
| F4 | FINDING | Unreviewed PAT 5.4% of consol PAT (below 10%), but unreviewed associate carrying value is 68.6% of parent equity and its share turned to a loss (A3-07). Prior trend ND. |
| F5 | FINDING | No going concern language. Two emphasis matters: VAT ruling date passed without update (A3-08); DoT aggregate "revised over a period of time", no prior text to diff (A3-09). |
| F6 | FINDING | Strict-lexicon hits only in the board letter and Attachment D ("has approved", "shall", "will", "proposed", "not expected to"). Commitments register below; Kaleyra transfer (A3-10), phased staff program (A3-11). No status transitions detectable without prior text. |
| F7 | FINDING | Zero strict-lexicon hedge hits in notes; estimate-language hedges on the fire provision (A3-12) and the recoverability provision (A3-13). |
| F8 | FINDING | Persistent deferred tax credits shield 935 bps of Q2 PBT; current tax 36.1% (A3-14). OCF lifted by tax refunds (A3-15). No earlier-years tax line exists. |
| F9 | FINDING | Standalone Q1 OCI (9.37) exceeds FY26 full-year 0.97 (A3-16). |
| F10 | FINDING | First share-option allotment, 0.03% dilution, EPS spread stable (A3-17); SBP accrual down 91.6% (A3-18). |
| F11 | FINDING | Net worth tie-outs pass; consol parent equity is 33.0% of standalone net worth, 6,904.86 gap (A3-19). |
| F12 | FINDING | Campaign Registry profit concentration (A3-20); Transformation Services liabilities -35.7% (A3-21); Data Services incremental margin 163% (A3-22); debt-funded CWIP build (A3-23); Voice decline (A3-30). |
| F13 | FINDING | CS successor named without incumbent cessation disclosure (A3-24); Kaleyra restructuring (A3-10). No AR, AGM, dividend or capital-raising item. |
| F14 | FINDING | Press-release data base differs from filing (A3-25); cumulative drafting set (A3-26). Signature timestamps judged coherent. |
| F15 | FINDING | Prior list ND. In-document: Kaleyra Africa exit in Q2 (A3-27), TComm Turkey added in Q1 (A3-28), Kaleyra, Inc. relationship change pending (A3-29). Eight other wef/upto dates fall in FY26 and are carried as context, not QoQ changes. |
| F16 | N.A. | Results filing, not a presentation. Press-release metric gaps handled under F14. |
| F17 | N.A. | Results filing, not a concall; no Notion checklist (pre-thesis). |

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Transfer 100% of Kaleyra, Inc. (FMV USD 92.625m) to TCNL for 3,17,632 TCNL shares at USD 291.6 under a Share Contribution Agreement | ND (not stated) | Board letter item (ii) L45-53; Attachment D L1493-1524 | initiated (board approved 15-Oct-2026) |
| Kaleyra, Inc. becomes a direct subsidiary of TCNL; no change in ultimate ownership | on completion, ND | Attachment D item 4 L1519-1524 | initiated |
| "not expected to have any material impact on the consolidated financial position" | on completion, ND | Attachment D item 2 L1512-1513 | initiated |
| Ms. Ridhi Sood as Company Secretary and Compliance Officer | 01-Nov-2026 | Board letter item (iii) L67-72; Attachment E L1540-1542 | initiated (appointed, effective date ahead) |
| Organisational changes "in a phased manner" (staff cost optimisation) | ND, ongoing | Consol note 2a L528-531; standalone note a L990-993 | underway |
| Defend DoT AGR demand position; appeals pending at SC and TDSAT | ND | Consol note 3 L552-559; standalone note 3 L1013-1018 | underway |
| National Court VAT appeal judgment | 13-Oct-2026 (scheduled; passed before filing) | Consol note 4 L569-574 | underway (outcome not disclosed) |
| Disposal of asset held for sale (7.40 carrying, 4.00 advance received in H1) | ND | BS L344; CF L460 | initiated (advance received) [inferred from cash flow, not a note statement] |
| Fire incident loss provision on estimate | true-up ND | Consol note 2d L541-542; standalone note d L1003-1004 | initiated (provisional) |
| Labour Codes provision re-estimated | Q1 FY27 | Consol note 2c L534-540; standalone note c L996-1002 | completed |
| "We enter the second half of the year with momentum and confidence" (CEO, soft outlook) | H2 FY27 | Press release L1375-1376 | n.a. (outlook statement) |
| DC-to-DC connectivity "$1 billion opportunity", "ongoing investments" | ND | Press release L1374-1375, L1398-1402 | n.a. (outlook statement) |
| Investor data pack uploaded | 15-Oct-2026 | Press release L1433-1434 | completed |

## QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
A3-01, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-18, A3-20, A3-21, A3-22, A3-23, A3-24, A3-25, A3-27, A3-28, A3-29. Each row's "Ask:" clause is the seed question.

```yaml
stage: A3-forensics
company: "TATACOMM"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tatacomm-q2fy27/work/forensics_results_tatacomm_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L460, L461, L344", classification: "FORWARD-SIGNAL", implication: "Held-for-sale asset (7.40) got a 4.00 advance in H1 with no proceeds or gain yet; exceptional gain line set to reactivate on completion."}
  - {id: "A3-02", check: "F1", line: "L162-163, L210-211, L589-597", classification: "NEUTRAL-FACT", implication: "Discontinued-ops and loss-on-sale lines are a template carry of the FY26 NetFoundry event; zero in all FY27 columns."}
  - {id: "A3-04", check: "F2", line: "L166, L637, L146, L631", classification: "AMBIGUOUS", implication: "S-vs-C PAT gap -13.2% to +28.5% to +171.0% of standalone PAT; 93% of the 206.80 QoQ parent PAT rise came from subsidiaries; subsidiary EBITDA +195.09 on +89.54 revenue, so cost-out or a one-off."}
  - {id: "A3-05", check: "F2", line: "L854-855, L877-878, L476-477, L751, L956-957", classification: "FORWARD-SIGNAL", implication: "Debt migrated to subsidiaries: standalone gross debt -1,209.34, subsidiary gross debt +2,482.20; standalone Reg 52(4) ratios flatter; standalone interest income from subsidiary loans will fall."}
  - {id: "A3-06", check: "F2", line: "L419-420, L825, L829, L940, L338", classification: "AMBIGUOUS", implication: "Consol net credit cost H1 +69.90 vs net release (40.89) a year ago; standalone bad-debt ratio 8.57% in H1 vs 1.90% in FY26."}
  - {id: "A3-07", check: "F4", line: "L1125-1140, L326, L462, L158", classification: "AMBIGUOUS", implication: "Unreviewed PAT 5.4% (passes), but unreviewed associate carrying value 2,331.73 = 68.6% of parent equity and associate share turned to a loss (3.25)."}
  - {id: "A3-08", check: "F5", line: "L571-574, L1107-1109", classification: "FORWARD-SIGNAL", implication: "VAT judgment on 365.80 (10.8% of parent equity) was due 13-Oct-2026, before sign-off; no update; payment suspended so an adverse ruling is a cash event."}
  - {id: "A3-09", check: "F5", line: "L545-547, L560-562, L1101-1105, L1319-1323", classification: "AMBIGUOUS", implication: "DoT contingent liability 7,513.71 = 2.21x consol parent equity; aggregate 'revised over a period of time'; no prior text to diff."}
  - {id: "A3-10", check: "F6", line: "L45-53, L1493-1524", classification: "FORWARD-SIGNAL", implication: "Kaleyra, Inc. (FMV USD 92.625m) moves under the Netherlands holdco; standalone carrying value vs FMV undisclosed; completion date ND."}
  - {id: "A3-11", check: "F6", line: "L528-531, L515, L990-993, L972", classification: "AMBIGUOUS", implication: "'One-time' staff cost charge recurs (98.26, 44.78, 36.54) under a phased program with no end date or total cost."}
  - {id: "A3-12", check: "F7", line: "L541-542, L1003-1004, L522, L417, L495", classification: "AMBIGUOUS", implication: "Fire provision 30.10 (25.67 impairment) stated on estimate; true-up either way pending."}
  - {id: "A3-13", check: "F7", line: "L543-544, L1005-1006, L524, L981", classification: "AMBIGUOUS", implication: "50.00 recoverability provision at the parent, counterparty unnamed; reads with credit write-offs."}
  - {id: "A3-14", check: "F8", line: "L153-154, L635-636, L329, L740, L600-601", classification: "FORWARD-SIGNAL", implication: "Deferred tax credit every period; shields 935 bps of Q2 PBT; current tax 36.1%; ETR step-up risk if DTA recognition stops."}
  - {id: "A3-15", check: "F8", line: "L440-441, L330, L741, L842", classification: "FORWARD-SIGNAL", implication: "315.42 of the 609.06 YoY OCF rise is lower tax paid from refunds; non-recurring."}
  - {id: "A3-16", check: "F9", line: "L639, L188, L598-599", classification: "AMBIGUOUS", implication: "Standalone Q1 OCI (9.37) exceeds FY26 full-year 0.97; verify actuarial assumptions at the Annual Report."}
  - {id: "A3-17", check: "F10", line: "L200, L481, L883, L207-208", classification: "NEUTRAL-FACT", implication: "About 90,000 shares allotted at par; dilution 0.03%; basic-diluted spread stable."}
  - {id: "A3-18", check: "F10", line: "L422, L820, L140", classification: "AMBIGUOUS", implication: "SBP accrual -91.6% YoY (24.01 to 2.02) lowers employee cost about 11 a quarter; possible forfeiture reversals."}
  - {id: "A3-19", check: "F11", line: "L361-368, L774-776, L954, L647-648, L479", classification: "NEUTRAL-FACT", implication: "Consol parent equity 33.0% of standalone net worth (gap 6,904.86); consol gross debt 3.49x parent equity vs standalone D/E 0.34; dividend exceeded H1 PAT."}
  - {id: "A3-20", check: "F12", line: "L238, L246, L273, L282, L1244-1245", classification: "FORWARD-SIGNAL", implication: "Campaign Registry earns 23.8% of segment result on 4.2% of revenue, up from 15.3%; profit concentrating in one regulated niche."}
  - {id: "A3-21", check: "F12", line: "L236, L239, L271, L280", classification: "AMBIGUOUS", implication: "Transformation Services revenue -33.7% YoY, liabilities -35.7%; 57.67 of the fall not explained by inter-segment."}
  - {id: "A3-22", check: "F12", line: "L235, L243, L139-143, L270, L279", classification: "AMBIGUOUS", implication: "Data Services result +175.18 QoQ on revenue +107.41 (163% incremental margin); one-offs unknown."}
  - {id: "A3-23", check: "F12", line: "L284, L318, L323, L458, L441, L373, L382", classification: "FORWARD-SIGNAL", implication: "Net debt +1,606.60 (+16.8%) in H1; CWIP +47.2%; capex 96% of OCF; debt-funded build and later D&A step-up."}
  - {id: "A3-30", check: "F12", line: "L234, L242, L269, L278, L675", classification: "CONFIRMATORY-NEGATIVE", implication: "Voice result down each period (34.93, 20.61, 18.13); liabilities exceed assets; structural decline."}
  - {id: "A3-24", check: "F13", line: "L67-72, L99-100, L1540-1542", classification: "AMBIGUOUS", implication: "CS successor named from 01-Nov-2026; incumbent cessation, date and reason not disclosed."}
  - {id: "A3-25", check: "F14", line: "L1363-1364, L1382-1384, L235", classification: "AMBIGUOUS", implication: "Press-release Q2 FY26 data base 5,179 vs filed 5,204.47; filed growth 11.7% not 12.2%; digital metrics untied to filing."}
  - {id: "A3-26", check: "F14", line: "L41, L1082, L1111, L973-976, L202, L589, L1387", classification: "NEUTRAL-FACT", implication: "Cumulative drafting slips (opinion vs conclusion, broken table numbering, blank reserves line, PAT growth rounding)."}
  - {id: "A3-27", check: "F15", line: "L1246", classification: "AMBIGUOUS", implication: "Kaleyra Africa left the group 04-Sep-2026 with no disclosed mode, consideration or P&L impact."}
  - {id: "A3-28", check: "F15", line: "L1256, L463", classification: "FORWARD-SIGNAL", implication: "TComm Turkey added 21-May-2026 with no acquisition outflow; new geography, purpose undisclosed."}
  - {id: "A3-29", check: "F15", line: "L1519-1521, L1239, L1197", classification: "FORWARD-SIGNAL", implication: "Kaleyra, Inc. to become a step-down subsidiary of TCNL; next consolidation list should reflect it."}
forward_signals: ["A3-01", "A3-05", "A3-08", "A3-10", "A3-14", "A3-15", "A3-20", "A3-23", "A3-28", "A3-29"]
ambiguous: ["A3-04", "A3-06", "A3-07", "A3-09", "A3-11", "A3-12", "A3-13", "A3-16", "A3-18", "A3-21", "A3-22", "A3-24", "A3-25", "A3-27"]
commitments:
  - {commitment: "Transfer 100% of Kaleyra, Inc. (FMV USD 92.625m) to TCNL for 3,17,632 TCNL shares at USD 291.6", implied_date: "ND", ref: "Board letter (ii) L45-53; Attachment D L1493-1524", status_word: "initiated"}
  - {commitment: "Kaleyra, Inc. becomes direct subsidiary of TCNL; ultimate ownership unchanged", implied_date: "on completion, ND", ref: "Attachment D item 4 L1519-1524", status_word: "initiated"}
  - {commitment: "Transfer not expected to have material impact on consolidated financial position", implied_date: "on completion, ND", ref: "Attachment D item 2 L1512-1513", status_word: "initiated"}
  - {commitment: "Ridhi Sood appointed Company Secretary and Compliance Officer", implied_date: "2026-11-01", ref: "Board letter (iii) L67-72; Attachment E L1540-1542", status_word: "initiated"}
  - {commitment: "Organisational changes in a phased manner (staff cost optimisation)", implied_date: "ND, ongoing", ref: "Consol note 2a L528-531; standalone note a L990-993", status_word: "underway"}
  - {commitment: "Defend DoT AGR demand position; appeals pending at SC and TDSAT", implied_date: "ND", ref: "Consol note 3 L552-559; standalone note 3 L1013-1018", status_word: "underway"}
  - {commitment: "National Court VAT appeal judgment", implied_date: "2026-10-13 (scheduled, passed)", ref: "Consol note 4 L569-574", status_word: "underway"}
  - {commitment: "Disposal of asset held for sale (7.40 carrying, 4.00 advance received)", implied_date: "ND", ref: "BS L344; CF L460 (inferred)", status_word: "initiated"}
  - {commitment: "Fire incident provision on estimate, true-up pending", implied_date: "ND", ref: "Consol note 2d L541-542; standalone note d L1003-1004", status_word: "initiated"}
  - {commitment: "Labour Codes provision re-estimated (reversal 18.52 consol)", implied_date: "Q1 FY27", ref: "Consol note 2c L534-540; standalone note c L996-1002", status_word: "completed"}
  - {commitment: "Enter H2 FY27 with momentum and confidence (CEO outlook)", implied_date: "H2 FY27", ref: "Press release L1375-1376", status_word: "n.a."}
  - {commitment: "DC-to-DC connectivity USD 1bn opportunity; ongoing investments", implied_date: "ND", ref: "Press release L1374-1375, L1398-1402", status_word: "n.a."}
  - {commitment: "Investor data pack uploaded", implied_date: "2026-10-15", ref: "Press release L1433-1434", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The Q2 profit jump is a subsidiary event. Parent PAT rose 206.80 QoQ and subsidiaries plus eliminations supplied 192.08 (93%). Standalone pre-exceptional PBT fell 7.3%. Subsidiary EBITDA rose 195.09 on 89.54 more revenue, so cost-out or a one-off credit drove it; A4 must ask which, with the SBP accrual collapse and recurring 'one-time' staff charges in view. Debt moved down the group: subsidiaries raised 2,628.15 long-term and repaid 2,641.16 to the parent, so standalone Reg 52(4) ratios improved while consolidated net debt rose 1,606.60. Consolidated parent equity is 33% of standalone net worth and gross debt is 3.49x it. OCF strength is partly tax refunds (315.42 less tax paid YoY). Reported ETR stays near 27% only because deferred credits recur; current tax runs 36%. The VAT ruling (365.80) was due 13-Oct, two days before sign-off, and the note is silent. Read the Kaleyra move to the Netherlands holdco together with the Kaleyra Africa exit on 04-Sep. With no prior-quarter text, F5 and F15 rest on in-document dates only."
```


### Part 3 of 4: A3 forensics, presentation

# A3 FORENSIC NOTES: TATACOMM q2fy27 (doctype: presentation)

Company: Tata Communications Limited (TATACOMM)
Quarter: Q2 FY27 | Doctype: presentation (9 slides, earnings call deck, filed 15 Oct 2026)
Inputs read: A1 structured (runs/tatacomm-q2fy27/extracted/tatacomm-presentation-q2fy27-structured.md), A1 fulltext (runs/tatacomm-q2fy27/extracted/tatacomm-presentation-q2fy27-fulltext.md), A2 ledger (runs/tatacomm-q2fy27/work/ledger_presentation_tatacomm_q2fy27.md). Prior-quarter fulltext: ND. Notion checklist: NONE (pre-thesis read). Source PDF and inputs/ not opened.
Model: claude-opus-5-5

Scope note. This deck carries no consolidated financial table. It has no revenue, EBITDA, PAT, net debt, capex, share count or segment figures. The only financial numbers are the six Digital Margin labels on slide 6 (fulltext lines 137-151). Most results-filing checks are therefore N.A. by doctype. [DERIVED] marks arithmetic on two disclosed numbers. It is not an estimate of a missing number.

## 1. LEDGER RECONCILIATION (74 of 74 rows read at cited line = 100%)

All 74 structured IDs (R001-R074) were read in the structured file and at their cited fulltext line. Every ledger row is accounted for. A2 count test (74/74, orphan_ids []) confirmed.

Reconciliation exceptions (A1 extraction defects; pipeline QA, not company findings):

| ID | A1 cite | Actual fulltext location | Issue | Load-bearing? |
|---|---|---|---|---|
| R026 | line 122, value "6" levers | lines 122-128 name 5 levers ("Accelerated Network Growth", "Drive Profitability- Digital Portfolio", "Increase Mix - Platforms", "Sales Contribution", "Agility in Operations") | VALUE ERROR. Count is 5, not 6. A2 already flagged COUNT_DISCREPANCY. Fulltext supports 5. | No (deck structure count) |
| R005, R006 | line 21 | "400 051" / "400 001" sit on line 23 | line offset (2) | No |
| R010 | line 48 | "14:14:50 +05'30'" is line 49 (line 48 carries the date) | line offset (1) | No |
| R020 | line 146 | "-INR 886Cr" is line 147 | line offset (1); value correct | Yes (value verified) |
| R025 | line 185 | "with a single contract and a unified SLA" is line 187 | line offset (2) | No |
| R029 | line 20 | "2015" is on lines 29 and 32 (line 20 blank) | line offset (9) | No |
| R059 | line 111 | "Driving absolute EBITDA growth, NPS and ESAT" is line 112 (111 is title) | line offset (1) | No |
| R063 | line 32 | "October 14, 2026" is line 33 | line offset (1) | No |
| R069 | line 71 | "Such statements involve known and unknown risks, uncertainties and other factors" is line 74 | line offset (3) | No |
| R070 | line 78 | Not verbatim. Fulltext lines 77-78 read "These risks may cause actual results and performance of Tata Communications, or industry results, to differ materially from those expressed or implied by the forward-looking statements" | paraphrase in structured file | No |
| R032, R033 | lines 153, 176 (slide titles) | content at lines 158 and 181 | cite points to title | No |

R018 (CHART_LABEL_UNPAIRED). Confirmed. The text layer carries "-6.9%" (line 142) for Q1FY27 and no rupee label for that bar. Slide 6 was not rendered (A1 header, line 11). Absence of a Q1 rupee label is confirmed in the text layer only. Caption pairing: text-layer column positions put "Digital Margins / Q2FY27" (lines 142-143) under the -3.6% / -INR 107 Cr labels, "Digital Margins / Q1FY27" (lines 146-147) under -6.9%, and "Digital Margin in FY25" (line 151) under -9.7% / -INR 886Cr. This matches the A1 pairing.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | R017, R020, R067, R072 | L138, L147, L151 / slide 6 | "-INR 107 Cr" (Q2FY27) vs "-INR 886Cr" ... "Digital Margin in FY25" | AMBIGUOUS | One chart sets a single-quarter rupee loss beside a full-year rupee loss. The bar heights suggest an 88% cut. Q2 annualised = INR 428 Cr [DERIVED, 107 x 4], which is 48% of FY25. The real improvement is about a halving. A4: ask for the quarterly rupee series on a like-for-like basis. |
| A3-02 | F16 | R018 | L142 / slide 6 | "-6.9%" (Q1FY27, no rupee label in text layer) | AMBIGUOUS | The Q1 bar gives a percent only. The absolute Q1 to Q2 loss change cannot be read. The 330 bps QoQ margin gain [DERIVED] can come from revenue growth or from cost cuts, and the deck does not show which. A4: ask for the Q1FY27 rupee loss and the revenue vs cost split of the gain. |
| A3-03 | F16 | R019, R067, R072 | L151 / slide 6 | "Digital Margin in FY25" | AMBIGUOUS | The base period is two fiscal years back. FY26 and Q2FY26 are absent, so the deck gives no YoY comparator. Lean bear: a skipped year can hide a FY26 setback. A4: ask for FY26 and Q2FY26 Digital margin in percent and rupees. |
| A3-04 | F6 | R061, R016-R020 | L132 / slide 6 | "DIGITAL PORFOLIO ON THE PATH TO BREAKEVEN" | FORWARD-SIGNAL | Management states a breakeven path with no date, no margin definition (EBITDA, EBIT or contribution) and no definition of the portfolio. The trajectory is -9.7% (FY25) to -6.9% (Q1FY27) to -3.6% (Q2FY27), +610 bps in total [DERIVED]. At the last-quarter pace breakeven falls within about 1-2 quarters [DERIVED, linear; not a company statement]. This is a catalyst candidate for the Role 5 tracker. A4: ask for the breakeven quarter, the margin definition and the portfolio perimeter. |
| A3-05 | F16 | R016, R017, R019, R020 | L137-L138, L145-L147 / slide 6 | "-3.6%" "-INR 107 Cr" ; "-9.7%" "-INR 886Cr" | AMBIGUOUS | Implied Digital revenue (if margin = loss / Digital revenue): Q2FY27 about INR 2,930-3,010 Cr. FY25 about INR 9,080-9,190 Cr, or INR 2,270-2,300 Cr a quarter [DERIVED, rounding bands]. That puts Q2 about 30% above the FY25 quarterly average. Two readings fit: real growth, or a change in portfolio perimeter or definition. The observation that separates them is a restated FY25 on the current perimeter. A4 question. |
| A3-06 | F16 | R059, R027, R053 | L112, L115-L117 / slide 5 | "Driving absolute EBITDA growth, NPS and ESAT" | AMBIGUOUS | The plan goal is absolute EBITDA growth. It has no margin target, number or date. The earnings deck carries no consolidated revenue, EBITDA, PAT or net debt. Prior deck ND, so a dropped earlier target cannot be tested. Lean bear: a growth goal stated in absolute terms can sit beside margin dilution. A4: ask whether any earlier quantified target (margin, revenue) stands, changed or was withdrawn. |
| A3-07 | F16 | R042-R052, R058, R059, R060 | L85, L111 / slides 4-5 | "THE TEAM IS IN PLACE" ; "PLAN ON PAGE" | FORWARD-SIGNAL | The deck frames a reset: a new org structure (Network, Infra, Interaction and Services Towers, a Transformation Group, line 98-104) under "MD AND CEO Ganesh Lakshminarayanan" (L107-L109), plus a new one-page plan with 5 levers. A reset deck sets a new baseline for promise-vs-delivery. Prior-quarter tenure and structure ND. A4: ask when the structure took effect, which heads are new, and the timeline for each lever. |
| A3-08 | F16 | R021-R025, R033, R055, R056 | L184-L193 / slide 8 | "700+ agents live" ; "600K+ voice AI mins / month" ; "A leading insurer serving 37 million customers" | AMBIGUOUS | Both AI case studies name no client and attach no revenue, contract value or margin. The counts carry "+" floors and no period base. AI monetisation is unquantified. A4: ask for AI-platform revenue, the number of paying customers, and the contract term of the "single contract" (L187). |
| A3-09 | F6 | R054 | L162-L163 / slide 7 | "We've invested in GPU infrastructure in India" | AMBIGUOUS | This GPU capex is stated as complete, with no amount, capacity, utilisation or funding source. It brings forward depreciation and return-on-capital questions for the Digital portfolio. A4: ask for the GPU capex amount, capacity in use, and whether it sits inside the Digital margin on slide 6. |
| A3-10 | F16 | R011-R015, R040, R041 | L88-L90 / slide 4 | "70% of India's live Financial Services data traffic" ; "300 of Fortune 500 Customers" | NEUTRAL-FACT | The reach claims carry no source, measurement date or revenue share. They need verification before use as evidence. No forward direction. |
| A3-11 | F14 | R061 | L132, L70 / slides 6, 3 | "PORFOLIO" ; "in this presentations" | NEUTRAL-FACT | There are drafting errors on the deck's only quantitative slide title and in the safe harbour. This is immaterial alone. It is logged as a cumulative governance data point. |

## 3. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Presentation has no line-item template. Ledger zero_standing count = 0. |
| F2 Standalone vs consolidated | N.A. | No standalone or consolidated figures in deck. |
| F3 Shell-entity detection | N.A. | No cost lines in deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor report in a presentation. |
| F5 Going concern / EoM tracking | N.A. | No EoM paragraph. Prior fulltext ND. |
| F6 Forward-commitment mining | FINDING | Lexicon hits: only "expected" at L71 inside safe-harbour boilerplate ("expected financial position"), not a commitment. Non-lexicon commitments at L85, L112, L122-L128, L132, L162-L163 were logged (A3-04, A3-09, register below). |
| F7 Hedge phrase mining | PASS | No lexicon hit ("may sometimes", "no assurance", "subject to", "evaluating", "exploring", "in discussions", "endeavour" absent). Safe harbour L70-L83 is standard boilerplate. No hedge is attached to the breakeven claim. |
| F8 Tax forensics | N.A. | No tax figures in deck. |
| F9 OCI forensics | N.A. | No OCI figures in deck. |
| F10 Share count and dilution | N.A. | Deck carries no paid-up capital, share count or EPS (ledger R001-R033 hold none). |
| F11 Reserves and net worth tie-out | N.A. | Deck carries no net worth or other-equity figure. |
| F12 Segment forensics | N.A. | No segment assets or liabilities. The Digital portfolio margin is covered under F16. |
| F13 Board outcome beyond results | N.A. | No board outcome in deck. The cover letter (L28-L34) is a Reg 30 deck filing only. |
| F14 Note drafting inconsistencies | FINDING | A3-11: "PORFOLIO" L132, "this presentations" L70. The cover letter is internally consistent (dated 15 Oct 2026 at L19, signed 2026.10.15 14:14:50 at L48-L49, before the 4:00 pm call at L33). |
| F15 Entity list diffs | N.A. | No consolidation list. Prior ND. |
| F16 Dropped and reframed disclosures | FINDING | A3-01, 02, 03, 05, 06, 07, 08, 10. Quarter vs year rupee mix, Q1 rupee label absent, FY26 skipped, no headline financials, reset framing. A dropped-metric test against the prior deck is not possible (prior ND). |
| F17 Silence audit | N.A. | Concall-specific check. Doctype is presentation. No Notion checklist exists (pre-thesis read). |

## 4. COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Digital portfolio to reach breakeven | ND (no date stated) | slide 6, L132 | underway |
| Drive absolute EBITDA growth, NPS and ESAT | ND (no number or date) | slide 5, L112 | underway |
| Five plan levers: Accelerated Network Growth; Drive Profitability-Digital Portfolio; Increase Mix-Platforms; Sales Contribution; Agility in Operations | ND | slide 5, L122-L128 | initiated |
| GPU infrastructure in India (sovereign AI) | ND (stated in past tense, amount ND) | slide 7, L162-L163 | completed |
| Leadership team and Tower structure in place | ND | slide 4, L85 | completed |

## 5. QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)

- A3-04: In which quarter does management expect Digital breakeven? Which margin does "Digital Margin" measure, and which businesses form the Digital portfolio?
- A3-01 / A3-02 / A3-03: What is the quarterly rupee Digital loss for each quarter of FY26, Q1FY27 and Q2FY27, on one perimeter?
- A3-05: Was FY25 Digital restated to the current perimeter? What is Digital revenue in Q2FY27?
- A3-06: Does any earlier quantified margin or revenue target still stand?
- A3-07: When did the Tower structure take effect, and which leaders are new in the last 12 months?
- A3-08: What are AI-platform revenue and the paying-customer count? What is the term of the insurer's single contract?
- A3-09: What is the GPU capex amount and utilisation, and is it inside the Digital margin?

```yaml
stage: A3-forensics
company: "TATACOMM"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tatacomm-q2fy27/work/forensics_presentation_tatacomm_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F16", line: "138,147,151 (slide 6)", classification: "AMBIGUOUS", implication: "Quarter rupee loss (-INR 107 Cr) charted beside full-year loss (-INR 886Cr); Q2 annualised INR 428 Cr [DERIVED] = 48% of FY25, a halving not an 88% cut"}
  - {id: "A3-02", check: "F16", line: "142 (slide 6)", classification: "AMBIGUOUS", implication: "Q1FY27 bar shows -6.9% with no rupee label in text layer; absolute Q1-to-Q2 change and revenue-vs-cost source of 330 bps gain not readable"}
  - {id: "A3-03", check: "F16", line: "151 (slide 6)", classification: "AMBIGUOUS", implication: "Baseline set at FY25; FY26 and Q2FY26 absent, no YoY comparator; lean bear, may mask an FY26 setback"}
  - {id: "A3-04", check: "F6", line: "132 (slide 6)", classification: "FORWARD-SIGNAL", implication: "Undated Digital breakeven claim; -9.7% to -6.9% to -3.6%; linear pace implies 1-2 quarters [DERIVED, not company statement]; catalyst candidate, margin and perimeter undefined"}
  - {id: "A3-05", check: "F16", line: "137-138,145-147 (slide 6)", classification: "AMBIGUOUS", implication: "Implied Digital revenue Q2FY27 ~INR 2,930-3,010 Cr vs FY25 ~INR 2,270-2,300 Cr per quarter [DERIVED], about +30%; growth or perimeter change"}
  - {id: "A3-06", check: "F16", line: "112,115-117 (slide 5)", classification: "AMBIGUOUS", implication: "Goal is absolute EBITDA growth, no margin target or number; deck has no consolidated financials; prior targets untestable (prior ND)"}
  - {id: "A3-07", check: "F16", line: "85,98-109,111 (slides 4-5)", classification: "FORWARD-SIGNAL", implication: "Reset framing: new Tower org and one-page plan with 5 levers; new promise-vs-delivery baseline"}
  - {id: "A3-08", check: "F16", line: "184-193 (slide 8)", classification: "AMBIGUOUS", implication: "AI case studies anonymised, '700+ agents live', '600K+ voice AI mins / month'; no revenue or contract value; AI monetisation unquantified"}
  - {id: "A3-09", check: "F6", line: "162-163 (slide 7)", classification: "AMBIGUOUS", implication: "GPU capex in India stated complete with no amount, capacity or utilisation; depreciation and return drag on Digital unknown"}
  - {id: "A3-10", check: "F16", line: "88-90 (slide 4)", classification: "NEUTRAL-FACT", implication: "Reach claims (70% of India FS live data traffic; 300 of Fortune 500) unsourced and undated; verify before use"}
  - {id: "A3-11", check: "F14", line: "132,70 (slides 6,3)", classification: "NEUTRAL-FACT", implication: "Drafting errors 'PORFOLIO' and 'this presentations'; cumulative governance data point only"}
forward_signals: ["A3-04", "A3-07"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-05", "A3-06", "A3-08", "A3-09"]
commitments:
  - {commitment: "Digital portfolio to reach breakeven", implied_date: "ND", ref: "slide 6 L132", status_word: "underway"}
  - {commitment: "Drive absolute EBITDA growth, NPS and ESAT", implied_date: "ND", ref: "slide 5 L112", status_word: "underway"}
  - {commitment: "Five plan levers (Network Growth; Digital Profitability; Platforms Mix; Sales Contribution; Agility in Operations)", implied_date: "ND", ref: "slide 5 L122-128", status_word: "initiated"}
  - {commitment: "GPU infrastructure in India for sovereign AI", implied_date: "ND (past tense, amount ND)", ref: "slide 7 L162-163", status_word: "completed"}
  - {commitment: "Leadership team and Tower structure in place", implied_date: "ND", ref: "slide 4 L85", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck's only financial content is the slide 6 Digital margin chart, and its framing flatters. It sets a single-quarter rupee loss (-INR 107 Cr) beside a full-year one (-INR 886Cr), skips FY26, and drops the Q1 rupee label. On a like-for-like annualised basis the loss halved; it did not fall 88%. The percent path (-9.7, -6.9, -3.6) is real and steep, so the undated breakeven claim is the deck's main catalyst candidate. Implied Digital revenue runs about 30% above the FY25 quarterly average [DERIVED]. A perimeter change would produce the same chart, so ask for a restated FY25. 'THE TEAM IS IN PLACE' plus 'PLAN ON PAGE' reads as a reset deck, with absolute EBITDA growth as the goal and no margin number; test against the results filing and the concall. A1 QA: R026 value is wrong (5 levers, not 6); nine rows carry cite offsets of 1 to 9 lines; R070 is a paraphrase. None is load-bearing; R020 value verified at L147."
```


### Part 4 of 4: A5 audit verdicts (completeness proof)

- Loop 0 audit (runs/tatacomm-q2fy27/work/audit_tatacomm_q2fy27.md): INCOMPLETE; FACTUAL 3, MISSING 4, CONTRADICTION 0, STYLE 13; loop back to A4.
- Loop 1 re-audit (runs/tatacomm-q2fy27/work/audit_tatacomm_q2fy27_loop1.md): COMPLETE; FACTUAL 0, MISSING 0, CONTRADICTION 0, STYLE 6. A5 withdrew its loop-0 F2 numeric claim.

stage: A5-adversary
company: "TATACOMM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "L1-S1 Step 4 rev L343 'absorbed most of the credit swing': ex-credit other expenses fell 53.55 of 110.79 (about half, 48%); credit-cost P&L line not disclosed (wording from A5 loop-0 text)"
    - "L1-S2 Brief rev L725 labels 'about 90%' as subsidiaries with eliminations; 5C gives 92.9% subsidiaries plus eliminations, 89.6% all non-parent sources"
    - "L1-S3 Diagnostic 1 rev L261 named components sum to 588.15; add Real Estate -0.01 (L237)"
    - "L1-S4 Brief rev L741 '114% quarterly jump' reads as QoQ; say 'on the year-ago quarter'"
    - "L1-S5 Preamble rev L22 lists R1514 (Mgage) as context only while rev L316 and Q27 use it as a Digital perimeter fact"
    - "L1-S6 Loop-0 A1/A2 style items S6, S7, S8, S10, S11 remain open (not A4)"
loop_back_to: ""
gap: ""
style_notes:
  - "L1-S1 'most' should read 'about half' (53.55 of 110.79)"
  - "L1-S2 align brief attribution label with 5C"
  - "L1-S3 add Real Estate -0.01 to the revenue decomposition"
  - "L1-S4 '114% quarterly jump' to 'rise on the year-ago quarter'"
  - "L1-S5 drop R1514 from the no-finding disposition list"
  - "L1-S6 A1/A2 items S6, S7, S8, S10, S11 carried, no loop"
analyst_note: "Loop 1 re-audit is COMPLETE. Every loop-0 FACTUAL and MISSING item is resolved in the revised review, checked against the A1 fulltext lines. One loop-0 finding was an A5 error: F2. My 185.39 (89.6%) was consolidated parent PAT less standalone PAT, which also holds the associate swing (-7.60) and NCI (+0.91). A4's original 192.08 (92.9%) was correct for its label, subsidiaries plus eliminations. The revised 5C shows both bases, the parts sum to the 206.80 rise, and the conclusion is unchanged. The Step 4 phrase 'absorbed most of the credit swing' also traces to my loop-0 wording; on H1 numbers it is about half, logged as STYLE. Coverage is unchanged and clean. Every new derived number ties; one 0.01 Real Estate omission is rounding-level. Re-reading the three most positive remaining claims (operating gain, cash direction, Digital breakeven path) finds counters that survive but are already in the review. The acquisition probe is satisfied. A1/A2 style notes S6, S7, S8, S10, S11 carry with no loop."
