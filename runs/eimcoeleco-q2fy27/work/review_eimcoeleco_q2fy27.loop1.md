# A4 REVIEW: Eimco Elecon (India) Limited (EIMCOELECO) | Q2 FY27 | Role 4 (Quarterly Results Review Protocol v1.4)

Run: /run-quarterly A4 analyst | Model: claude-opus-5-5 | Date: 2026-10-17 | Revision: Loop 1 (A5 audit items A5-F01, A5-F02, A5-M01, A5-M02 applied; log at end)
Docs merged: results filing (Reg 33 statement, BS, CF, limited review report, board outcome, embedded press release, Annexures B and C), investor presentation (39 slides), press release (4 pages). No concall in this run, so Role 5 is not run.
Framing: PRE-THESIS READ. No Notion COMPANIES MASTER page, no companies/EIMCOELECO.md, no spear on record. Decision Status: ND (no page). This review is not a thesis check.

Anchor key: `res Lnnn` = line in extracted/eimcoeleco-results-q2fy27-fulltext.md; `pres Lnnn` = line in extracted/eimcoeleco-presentation-q2fy27-fulltext.md; `pr Lnnn` = line in extracted/eimcoeleco-pressrelease-q2fy27-fulltext.md. `[d]` = arithmetic on the anchored filed numbers, not a filed number. A3 finding IDs: results `FN##`, presentation `A3-##`, press release `PR/F#-#`.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 7 notes / 0 turns / 43 slides (presentation 39 slides + press release 4 pages). All 7 notes, all 43 slides and every structured row are reviewed: results R001-R470 plus M001 (financing total, res L322); presentation R001-R946; press release R001-R092. Orphan IDs: none in any ledger. Gate A2: pass on all three. A3 ledger reconciliation: 100% on all three.

Findings incorporated (44): results FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN19, FN20; presentation A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16; press release PR/F6-1, PR/F6-2, PR/F6-3, PR/F12-1, PR/F14-1, PR/F14-2, PR/F16-1, PR/F16-2.

Data corrections carried from A2/A3 (applied in every table below):
- R150 Other non-current assets 4,824.68 lakhs belongs to 31.03.26, not 30.09.26 (A2 Z5, A3 FN01; NCA sums tie only that way, res L211-212). The Sep-26 cell is blank.
- Text-layer glitches resolved by tie-out (A3): R014 Q1 FY27 total income = 8,528.25; R153 Sep-26 inventories = 11,547.54; R242 = (308.64). R267 FY26 PPE sale proceeds verbatim value NOT FOUND.
- The H1 FY26 investing-cash-flow comparatives are row-misaligned against their labels (res L303-308; A2 layout flag, A3 FN20). The column total (364.39) ties; the line labels do not. H1 FY26 capex is therefore ND in this review.
- The financing total (C) is M001: (0.93) H1 FY27, (128.42) FY26, (327.09) H1 FY26 (res L322).

---

## STEP 0: PRE-FLIGHT

### 0A. Notion fetch
| Item | Value |
|---|---|
| One-line thesis | ND (no Notion page) |
| Four-pillar destination PE | ND |
| Bear/Base/Bull projections | ND |
| Thesis-broken conditions | ND |
| Quarterly monitoring checklist | ND |
| Position size / cost basis | ND |
| Decision Status | ND (no page). Verified against orchestrator copy work/notion-thesis.md, live fetch 2026-10-17. Notion "Eimco" hits on the KCPSUGIND page refer to a different entity and are ignored. |
| Devil's Advocate split | ND |
| Prior-quarter Questions for Management | ND (not passed). Answer-status tracking is not possible this quarter. |
| Downstream Signal Tracker rows | Not supplied |

Under /run-quarterly the protocol's "stop and ask" becomes this PRE-THESIS READ framing. No HOLD/ADD/TRIM/EXIT framing appears anywhere in this review.

### 0B. Units
Financial statements (res pp4-6): Rs lakhs (res L149, R443). Conversion: Rs crore = Rs lakhs x 0.01. Press release, presentation: Rs crore, rounded to whole crore (res L353, pres L385, L410, L437). All analysis below is in Rs crore, converted from the lakhs statement. Deck figures are used only where the filing is silent, and are marked `pres`.

### 0C. Share count
Paid-up equity 576.84 lakhs at face value Rs 10 (res L181, L229) = 57.684 lakh shares, unchanged in all six P&L columns and at both balance-sheet dates. Basic EPS = diluted EPS in every period (res L185-186). No split, bonus, rights, ESOP, QIP or buyback in the review or comparison period. Reported EPS = share-adjusted EPS.

### 0D. Notes extraction
| Note # | Subject | What it says (1 sentence) | Rs cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 (res L188-190) | Approval and review | Audit Committee reviewed and Board approved on 13 Oct 2026; statutory auditors gave an unmodified limited-review conclusion. | 0 | Q2 / H1 FY27 | None. Confirms reviewed (not audited) status. |
| 2 (res L191) | Segment | Only one reportable segment, Machinery and Spares. | 0 | All | No filed product vs spares split. The only split is the unmapped chart in the press release and deck (FN12, A3-14, PR/F12-1). |
| 3 (res L192) | Group structure | No subsidiary, associate or JV as on 30 Sep 2026. | 0 | 30 Sep 2026 | Standalone = whole company. Standalone vs consolidated gap is N.A. |
| 4 (res L193) | Regrouping | Prior-period figures "have been regrouped /rearranged wherever necessary, to make them comparable". | ND (lines not named) | Prior periods | MEDIUM. The regrouped comparatives still show Compensation to Distributors at 11.2% of revenue (Q1 FY27) and 11.9% (Q2 FY26). A Q2 reclassification between that line and Other Expenses would normally show in regrouped comparatives, so the filed text leans against the reclass reading (FN11; A5-F02). |
| 5 (res L194) | Balance sheet | Statement of assets and liabilities at 30 Sep 2026 attached. | 0 | 30 Sep 2026 | Enables Step 5. |
| 6 (res L266, R452) | Cash flow | Statement of cash flows for H1 attached. | 0 | H1 FY27 | Enables H1 CFO/PAT. |
| Unnumbered (res L328, R453) | Cash-flow method | Indirect method under Ind AS 7. | 0 | H1 | H1 FY26 investing comparatives are row-misaligned (FN20). H1 FY26 capex not usable. |
| Line item (res L171, R091) | Prior-period tax | Adjustment of tax for earlier periods (0.11) credit in FY26 only. | (0.11) | FY26 | Low (FN06). |
| Line items (res L177-179) | OCI | Remeasurement of defined benefit plan booked annually only: FY26 net (0.26). | (0.26) | FY26 | Interim columns blank; FY27 remeasurement will land in Q4 FY27. |

Exceptional items: none, and no exceptional line exists in the filed template (A3 F1). Deck carries an "Exceptional Income / (Expense)" line at 0 in all five periods (pres L401, A3-03).

Auditor opinion check: Unmodified conclusion on a limited review under SRE 2410 (res L108-123, L188-190). No Emphasis of Matter, no Other Matter, no Going Concern paragraph (A2 section 6, A3 F4/F5 PASS). Prior-quarter report is ND, so removal of an earlier EoM cannot be ruled out from these files.

Board outcome beyond results (res L41-58, L465-522): CFO and KMP Mr. Vishal C. Begwani resigns with effect from close of business on 30 Oct 2026. No successor or interim CFO is named (NOT FOUND). His letter is dated 5 Sep 2026 (res L486) and addressed to the Executive Director (res L489); the board noted it on 13 Oct 2026 (res L32, L41), 38 days later (FN16, FN17).

### 0E. Business type
Standard operating business (not a lender). Archetype fit: order-book business (capital goods: underground mining and construction equipment) with an aftermarket spares line and a large, mostly non-current treasury book. Steps 1 and 5 (standard) apply.

Checkpoint: Notion fetched (no page, Decision Status ND), units identified, no share-count change, all notes extracted, auditor opinion unmodified, business type standard.

---

## STEP 1: DATA EXTRACTION TABLE (Rs crore; standalone only, Note 3)

Columns: Q2 FY26 = quarter to 30.09.25; Q1 FY27 = quarter to 30.06.26; Q2 FY27 = quarter to 30.09.26; FY26 = year to 31.03.26 (audited); FY27 = ND (year not complete). H1 columns added because Q2 carries the half-year cash flow.

| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | 33.24 | 77.52 | 56.80 | 230.75 | ND | 100.81 | 134.32 | res L154 |
| Other Income | 4.27 | 7.76 | 1.89 | 17.00 | ND | 12.36 | 9.65 | res L155 |
| Total Income | 37.51 | 85.28 | 58.69 | 247.75 | ND | 113.17 | 143.97 | res L156 (Q1 glitch resolved, A3) |
| Cost of Materials Consumed | 20.37 | 21.59 | 31.88 | 88.18 | ND | 35.02 | 53.47 | res L158 |
| Purchase of stock-in-trade | 2.74 | 2.84 | 2.41 | 13.60 | ND | 5.54 | 5.24 | res L159 |
| Change in Inventories (FG, WIP) | (13.72) | 11.13 | (11.50) | (2.87) | ND | (2.96) | (0.37) | res L160 |
| Manufacturing expense | 2.16 | 1.83 | 1.90 | 8.05 | ND | 4.37 | 3.73 | res L161 |
| Employee Benefits Expense | 5.95 | 5.79 | 5.54 | 22.01 | ND | 11.55 | 11.34 | res L162 |
| Finance Costs | 0.16 | 0.28 | 0.12 | 0.85 | ND | 0.28 | 0.40 | res L163 |
| Depreciation, impairment, amortisation | 2.44 | 2.11 | 2.07 | 8.77 | ND | 4.31 | 4.18 | res L164 |
| Compensation to Distributors | 3.94 | 8.71 | 3.17 | 26.49 | ND | 11.72 | 11.87 | res L165 |
| Other Expenses | 6.58 | 11.39 | 12.66 | 32.32 | ND | 18.04 | 24.05 | res L166 |
| Total Expenses | 30.62 | 65.66 | 48.25 | 197.39 | ND | 87.86 | 113.91 | res L167 |
| Profit Before Tax | 6.89 | 19.62 | 10.44 | 50.36 | ND | 25.31 | 30.06 | res L168 |
| Tax Expense (total) | 1.54 | 4.24 | 2.61 | 11.64 | ND | 5.47 | 6.85 | res L173 |
| of which current tax | 1.47 | 5.18 | 2.61 | 11.53 | ND | 4.85 | 7.79 | res L170 |
| of which earlier-period adjustment | ND (blank) | ND (blank) | ND (blank) | (0.11) | ND | ND (blank) | ND (blank) | res L171 |
| of which deferred tax | 0.07 | (0.94) | (0.00) | 0.22 | ND | 0.62 | (0.94) | res L172 |
| Exceptional items | ND (no line) | ND (no line) | ND (no line) | ND (no line) | ND | ND (no line) | ND (no line) | res L154-174 |
| PAT | 5.35 | 15.38 | 7.83 | 38.71 | ND | 19.83 | 23.21 | res L174 |
| EPS reported (Rs, basic = diluted) | 9.28 | 26.66 | 13.58 | 67.11 | ND | 34.38 | 40.24 | res L185-186 |
| EPS share-adjusted (Rs) | 9.28 | 26.66 | 13.58 | 67.11 | ND | 34.38 | 40.24 | res L185-186 (no share change, 0C) |

Arithmetic tie (Q2 FY27, lakhs): 3,187.99 + 240.67 - 1,149.94 + 189.93 + 554.28 + 12.21 + 206.96 + 316.53 + 1,265.91 = 4,824.54 = Total Expenses (res L167). Ties.

### Derived metrics (Rs crore; [d] from the Step 1 rows)
| Derived metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + Fin - OI | 5.22 | 14.25 | 10.74 | 42.97 | ND | 17.53 | 24.99 | [d] res L155, L163, L164, L168 |
| Operating EBITDA margin | Op EBITDA / Revenue | 15.71% | 18.38% | 18.92% | 18.62% | ND | 17.39% | 18.61% | [d] + res L154 |
| Reported EBITDA | PBT + D + Fin | 9.49 | 22.01 | 12.63 | 59.98 | ND | 29.89 | 34.64 | [d] res L163, L164, L168 |
| Core PBT (ex-OI) | PBT - OI | 2.62 | 11.86 | 8.55 | 33.35 | ND | 12.94 | 20.41 | [d] res L155, L168 |
| Other Income / PBT | OI / PBT | 62.0% | 39.6% | 18.1% | 33.8% | ND | 48.9% | 32.1% | [d] res L155, L168 |
| Effective tax rate | Tax / PBT | 22.36% | 21.61% | 24.99% | 23.12% | ND | 21.62% | 22.79% | [d] res L168, L173 |
| PAT margin | PAT / Revenue | 16.10% | 19.84% | 13.79% | 16.78% | ND | 19.68% | 17.28% | [d] res L154, L174 |
| Gross margin (filing basis) | (Rev - materials - purchases - inventory change) / Rev | 71.75% | 54.14% | 59.88% | 57.13% | ND | 62.70% | 56.57% | [d] res L154, L158-160 |
| Distributor compensation / revenue | L165 / L154 | 11.85% | 11.23% | 5.57% | 11.48% | ND | 11.62% | 8.84% | [d] res L154, L165 |
| Other Expenses / revenue | L166 / L154 | 19.81% | 14.69% | 22.29% | 14.01% | ND | 17.89% | 17.91% | [d] res L154, L166 |
| Distributor comp + Other Expenses / revenue | (L165 + L166) / L154 | 31.66% | 25.92% | 27.86% | 25.48% | ND | 29.51% | 26.75% | [d] res L154, L165-166 |
| Employee cost / revenue | L162 / L154 | 17.90% | 7.47% | 9.76% | 9.54% | ND | 11.46% | 8.44% | [d] res L154, L162 |

Press release and deck EBITDA cross-check (FN20, PR/F14-1): the release states Q2 FY27 EBITDA margin 18.8% (res L404) and YoY growth 108.8% (res L403). Computed operating EBITDA gives 18.92% and +105.8%. Deck margins run 0.1-0.3 pp below the computed series in every period (Q2 FY26 15.4% vs 15.71%; Q1 FY27 18.3% vs 18.38%; H1 FY27 18.5% vs 18.61%; FY26 18.3% vs 18.62%; pres L393, L704). The EBITDA definition is not stated (R464). Use the computed operating EBITDA. The deck "Other Expenses" line combines Compensation to Distributors and Other Expenses (pres L391: Q2 FY27 16 = 3.17 + 12.66; Q1 FY27 20 = 8.71 + 11.39).

Checkpoint: every cell is a filed number, a [d] derivation of filed numbers, or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26, Rs crore)

| Metric | Q2 FY26 | Q2 FY27 | YoY % change | Verdict | Anchor |
|---|---|---|---|---|---|
| Revenue from Operations | 33.24 | 56.80 | +70.9% | Strong, off a weak base (Q2 FY26 was -50.8% QoQ) | res L154 |
| Operating EBITDA | 5.22 | 10.74 | +105.8% | Strong; all of the margin gain rests on the unexplained distributor plus other line (FN11) | [d] |
| Operating EBITDA margin (pp) | 15.71% | 18.92% | +321 bps | Expanded YoY; fixed-cost lines net -59 bps against the gross-margin fall | [d] |
| Depreciation | 2.44 | 2.07 | -15.1% | Falling despite Rs 47.44 cr PPE addition (FN09) | res L164 |
| Finance Costs | 0.16 | 0.12 | -25.5% | Immaterial | res L163 |
| EBIT (operating, ex-OI) | 2.78 | 8.67 | +211.6% | Strong YoY, off a trough base | [d] Op EBITDA - D |
| Other Income | 4.27 | 1.89 | -55.7% | Treasury drag on headline | res L155 |
| Core Operating PBT (PBT - OI) | 2.62 | 8.55 | +226.4% | Off a trough base: TTM +22.4%, H1 +57.7%; Q2 FY27 level is below the H2 FY26 quarterly average (10.21) | [d] |
| Reported PBT | 6.89 | 10.44 | +51.5% | Understates YoY core growth | res L168 |
| PAT | 5.35 | 7.83 | +46.4% | Understates YoY core growth | res L174 |
| EPS (share-adjusted, Rs) | 9.28 | 13.58 | +46.3% | Same as PAT | res L185 |

H1 YoY (H1 FY27 vs H1 FY26) for context: revenue +33.2% (100.81 to 134.32); operating EBITDA +42.6% (17.53 to 24.99); margin +122 bps (17.39% to 18.61%); OI -22.0% (12.36 to 9.65); core PBT +57.7% (12.94 to 20.41); PBT +18.8% (25.31 to 30.06); PAT +17.0% (19.83 to 23.21); EPS +17.0% (34.38 to 40.24). TTM core PBT Rs 40.82 cr vs FY26 Rs 33.35 cr = +22.4%. All [d] from res L154-L185.

Mandatory diagnostic answers:
1. Did revenue grow YoY? Yes. Q2 FY27 revenue of Rs 56.80 cr vs Q2 FY26 Rs 33.24 cr = +70.9% YoY. There is no company annual guidance in the filings and no Notion base case, so the comparison to guidance and to base is ND.
2. Margin YoY? Expanded. Q2 FY27 operating EBITDA margin 18.92% vs Q2 FY26 15.71% = +321 bps. The gain does not come from fixed-cost leverage. Filing-basis gross margin fell 1,187 bps (71.75% to 59.88%). Employee cost fell from 17.90% to 9.76% of revenue (+814 bps to margin) and manufacturing expense from 6.49% to 3.34% (+314 bps). Those fixed-cost lines only offset the gross-margin fall: net -59 bps. Without the distributor plus other line, Q2 FY27 operating EBITDA margin would be about 15.11%, below Q2 FY26's 15.71% [d]. The whole +321 bps rests on distributor comp plus other expenses falling from 31.66% to 27.86% of revenue (+380 bps). Inside that line, Other Expenses rose 92.3% in rupees (6.58 to 12.66) against revenue +70.9%, and Compensation to Distributors fell 19.6% in rupees (3.94 to 3.17) [d, res L154, L158-166]. The line is unexplained (FN11). Note 4 (res L193) leans against a reclassification reading (Step 0D).
3. Core operating PBT YoY? Grew. Rs 2.62 cr to Rs 8.55 cr = +226.4%. This is off a trough base: Q2 FY26 revenue had fallen 50.8% QoQ. In level terms Q2 FY27 core PBT sits below Q1 FY26 (Rs 10.32 cr), the H2 FY26 quarterly average (Rs 10.21 cr) and Q1 FY27 (Rs 11.86 cr). On less distorted bases core PBT grew 57.7% in H1 and 22.4% on TTM. The distributor-rate drop alone is worth Rs 3.57 cr: at the Q2 FY26 rate of 11.85%, Q2 FY27 distributor comp would be Rs 6.73 cr, not the filed Rs 3.17 cr. That is 60% of the Rs 5.93 cr YoY core-PBT gain [d, res L154, L165]. Headline PAT growth (+46.4%) understates YoY core growth, but the core gain itself rests heavily on one unexplained line.
4. Gap between core PBT growth and PAT growth: Other Income fell Rs 2.38 cr (4.27 to 1.89). ETR rose 263 bps (22.36% to 24.99%), costing Rs 0.28 cr. Finance cost fell Rs 0.04 cr. No exceptional items. Bridge in Step 4.
5. D&A and finance costs scaling faster than revenue? No. Both fell YoY while revenue rose 70.9%. Watch item: PPE rose Rs 47.44 cr in H1 (64.11 to 111.55, res L204) with no D&A step-up yet (Q1 2.11, Q2 2.07). Either the asset is non-depreciable (land) or capitalisation came late in the half and a Q3 step-up follows (FN09, A3-01). No absorption deficit is visible yet.
6. Other Income concentration changing? Yes, falling. OI was 62.0% of PBT in Q2 FY26 and 18.1% in Q2 FY27. H1 OI fell 22.0% YoY. 74.7% of H1 FY27 OI is fair-value and sale gains on investments (7.21 of 9.65; res L278), which are non-cash MTM in large part (investments rose 8.24 = 1.03 purchases + 7.21 FV gain; A3 tie-out). OI is volatile within the half: Q1 7.76, Q2 1.89 (res L155). Stripping OI gives the cleaner read.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY

| Quarter | Revenue (Rs cr) | Op EBITDA margin | Core PBT ex-OI (Rs cr) | One-offs flagged | QoQ run-rate | Anchor |
|---|---|---|---|---|---|---|
| Q1 FY26 [d: H1 FY26 - Q2 FY26] | 67.57 | 18.22% | 10.32 | None disclosed | ND (Q4 FY25 not in files) | [d] res L154-168 |
| Q2 FY26 | 33.24 | 15.71% | 2.62 | None disclosed | -50.8% vs Q1 FY26 | res L154-168 |
| H2 FY26 [d: FY26 - H1 FY26; Q3/Q4 split ND] | 129.94 (64.97 per quarter average) | 19.58% | 20.41 (10.21 per quarter average) | FY26 earlier-period tax credit 0.11; annual OCI (0.26) | ND per quarter | [d] res L154-171 |
| Q1 FY27 | 77.52 | 18.38% | 11.86 | Deferred tax credit 0.94 (res L172) | +19.3% vs H2 FY26 quarterly average; +14.7% YoY vs Q1 FY26 | res L154-172 |
| Q2 FY27 | 56.80 | 18.92% | 8.55 | No exceptional; distributor comp at 5.57% of revenue vs 11.2-11.9% (FN11) | -26.7% QoQ; +70.9% YoY | res L154-168 |

QoQ (Q2 FY27 vs Q1 FY27): revenue -26.7%; operating EBITDA -24.6% (14.25 to 10.74); core PBT -27.9% (11.86 to 8.55); OI -75.6% (7.76 to 1.89); PBT -46.8%; PAT -49.1% (15.38 to 7.83). [d]

Diagnostics:
- Trajectory: Recovering YoY, dipping QoQ. Q2 was below Q1 in both years on file (33.24 < 67.57; 56.80 < 77.52), and H2 was 56.3% of FY26 revenue (one H2 observed; FN15). Read as seasonal and dispatch-lumpy, not as a step-up.
- One-off distortion: Q2 FY26 is the distorted base (weak quarter, gross margin 71.75%, outlier vs every other period; FN12). Q1 FY27 PAT carries a Rs 0.94 cr deferred-tax credit. No exceptional items anywhere.
- Latest quarter vs H1 average: Q2 FY27 revenue Rs 56.80 cr is below the H1 FY27 quarterly average of Rs 67.16 cr. Capex-commissioning test: PPE rose Rs 47.44 cr in H1 while the latest quarter fell below the H1 average. If the asset is productive capacity, this is the protocol's red-flag pattern. If it is land, the test does not apply. The filings do not say which (FN09, A3-01).
- Implied next base: Q3 FY26 standalone is ND, so a Q3 YoY comparator is ND. The H2 FY26 per-quarter average is Rs 64.97 cr revenue and Rs 10.21 cr core PBT. To hold H1's +33.2% YoY into H2, H2 FY27 revenue must reach at least Rs 173.1 cr (129.94 x 1.3325) [d, arithmetic threshold, not a forecast]. The Rs 133 cr order book (res L374, L413) covers 77% of that threshold, before spares and before definition is confirmed.

---

## STEP 4: OPERATIONAL DECOMPOSITION (PAT bridge)

### Q2 FY27 vs Q2 FY26 (Rs crore; [d])
| Component | YoY change (Rs cr) | Share of reported PAT change | Recurring? |
|---|---|---|---|
| Revenue contribution (volume at Q2 FY26 op EBITDA margin 15.71%) | +3.70 | +149.2% | Recurring |
| Margin change contribution (+321 bps on Q2 FY27 revenue) | +1.82 | +73.4% | UNRESOLVED: rests wholly on the distributor plus other line (FN11); fixed-cost lines net -59 bps |
| D&A change (2.44 to 2.07) | +0.37 | +14.8% | Recurring (post-capex: at risk of reversal if FN09 asset depreciates) |
| Finance cost change (0.16 to 0.12) | +0.04 | +1.7% | Recurring |
| Other Income change (4.27 to 1.89) | -2.38 | -96.0% | NON-RECURRING (treasury, largely MTM) |
| Tax on PBT increase at Q2 FY26 ETR (22.36%) | -0.79 | -32.0% | Mixed |
| Effective tax rate change (+263 bps) | -0.28 | -11.1% | Mixed |
| Exceptional items | 0.00 | 0.0% | NON-RECURRING (none) |
| **Reported PAT YoY change** | **+2.48 (5.35 to 7.83)** | **100.0%** | |

Check: 3.70 + 1.82 + 0.37 + 0.04 - 2.38 - 0.79 - 0.28 = 2.48. Ties (lakhs: 370.07 + 182.24 + 36.68 + 4.19 - 238.16 - 79.38 - 27.52 = 248.12).

### H1 FY27 vs H1 FY26 (Rs crore; [d])
| Component | YoY change (Rs cr) | Share of reported PAT change | Recurring? |
|---|---|---|---|
| Revenue contribution (at H1 FY26 margin 17.39%) | +5.83 | +172.6% | Recurring |
| Margin change (+122 bps) | +1.63 | +48.3% | UNRESOLVED (distributor plus other line, FN11) |
| D&A change (4.31 to 4.18) | +0.13 | +3.8% | Recurring |
| Finance cost change (0.28 to 0.40) | -0.12 | -3.5% | Recurring |
| Other Income change (12.36 to 9.65) | -2.71 | -80.4% | NON-RECURRING |
| Tax on PBT increase at H1 FY26 ETR (21.62%) | -1.03 | -30.4% | Mixed |
| ETR change (+117 bps) | -0.35 | -10.4% | Mixed |
| Exceptional items | 0.00 | 0.0% | NON-RECURRING |
| **Reported PAT YoY change** | **+3.38 (19.83 to 23.21)** | **100.0%** | |

Mandatory answers:
- Recurring vs non-recurring: in Q2, operations added Rs 5.93 cr pre-tax, 2.4x the reported PAT gain of Rs 2.48 cr. Falling Other Income removed Rs 2.38 cr. The PAT growth is operating, but Rs 3.57 cr of the Rs 5.93 cr (60%) equals the distributor-rate drop, which is unexplained (FN11). Its durability is not established.
- If Other Income reverts to the prior-year level (Rs 4.27 cr in Q2): PBT would be Rs 12.82 cr and PAT Rs 9.62 cr at the Q2 FY27 ETR of 24.99% [d]. At zero Other Income, core PAT is Rs 6.41 cr (8.55 x (1 - 24.99%)) vs Rs 2.03 cr in Q2 FY26 (+215%) [d, reported ETR applied].
- D&A and finance costs: not at steady state. A Rs 47.44 cr net PPE increase in H1 (FN09) has not yet shown in D&A. The new steady-state D&A is ND until the asset class and capitalisation date are disclosed. Finance cost is small (Rs 0.40 cr H1) but borrowing doubled to Rs 5.75 cr (FN02).
- Tax adjustments: Q1 FY27 carries a deferred-tax credit of Rs 0.94 cr (res L172). H1 ETR is 22.79%; ex-deferred it is 25.91% (7.79 / 30.06) vs 25.17% statutory [statute, not in filing; tax-regime election NOT FOUND]. DTL fell 0.94 (7.70 to 6.76, res L239) in a half with Rs 7.21 cr FV gains and a Rs 47 cr capitalisation, both of which normally raise DTL (FN07, A3-08). If the credit does not recur, ETR steps up toward 25-26%. Reported H1 PAT is inflated by the credit; Q2 is clean (deferred 0.00).

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 cash flow available under Reg 33)

Prior period: H1 FY26 for flows; 31 Mar 2026 for stock items (no Sep-25 balance sheet in the filing).

| Metric | Prior period | Current period | Change | Verdict | Anchor |
|---|---|---|---|---|---|
| CFO (H1) | 6.04 (H1 FY26); 22.11 (FY26) | 1.84 (H1 FY27) | -69.6% vs H1 FY26 | Weak | res L300 |
| CFO / PAT | 0.30x (H1 FY26); 0.57x (FY26) | 0.08x (H1 FY27) | -22.6 pp vs H1 FY26 | Below every Pillar 2 band (floor 0.65x) | [d] res L174, L300 |
| Capex (PPE + CWIP payments) | ND (H1 FY26 column row-misaligned, FN20); 60.55 (FY26) | 2.11 (H1 FY27) | ND | Low cash capex in H1; the FY26 advance was capitalised (FN09) | res L303 |
| FCF (CFO - capex) | ND (H1 FY26); (38.44) (FY26) | (0.28) (H1 FY27) | ND | Negative | [d] res L300, L303 |
| Working capital change (CF) | (6.08) (H1 FY26); (11.31) (FY26) | (15.76) (H1 FY27) | -9.68 vs H1 FY26 | Absorbing | [d] res L288-294 |
| Receivable days (period-end receivables / annualised revenue x 365) | 114.7 (Mar-26, on FY26 revenue) | 123.9 (Sep-26, on H1 x 2) | +9.2 days | Stretching | [d] res L154, L217 |
| Inventory days (on COGS: materials + purchases + inventory change) | 400.4 (Mar-26) | 361.2 (Sep-26, H1 x 2) | -39.2 days | High; improves on a larger H1 COGS base | [d] res L158-160, L214 |
| Payable days (on same COGS) | 65.1 (Mar-26) | 81.2 (Sep-26) | +16.1 days | Lengthening (supports cash) | [d] res L252-257 |
| Cash Conversion Cycle | 450.0 (Mar-26) | 403.9 (Sep-26) | -46.1 days | Very long; H1-annualised basis is seasonal, read direction with care | [d] |
| PPE | 64.11 (Mar-26) | 111.55 (Sep-26) | +47.44 (+74.0%) | Large unexplained addition | res L204 |
| CWIP | 1.57 (Mar-26) | 0.45 (Sep-26) | -1.12 | Capitalised | res L205 |
| Other non-current assets | 48.25 (Mar-26; A2 Z5 correction) | ND (blank, Sep-26) | -48.25 | Emptied into PPE (FN01, FN09, A3-01) | res L211 |
| Net debt / (net cash) excluding investments | 3.55 net debt (Mar-26) | 5.75 net debt (Sep-26) | +2.20 | Small, rising | [d] res L218-219, L235, L243-244 |
| Liquid net cash / (net debt): current investments + cash + bank - borrowings | 11.86 net cash (Mar-26) | (1.53) net debt (Sep-26) | -13.39 | Liquid treasury turned to net borrowing in H1 (A5-M02) | [d] res L216, L218, L219, L243 |
| Net debt / (net cash) including all investments | (200.98) net cash (Mar-26) | (207.03) net cash (Sep-26) | +6.05 net cash | Book is 98.7% non-current, composition undisclosed; the +6.05 rise is below the 7.21 FV and sale gains, so ex-MTM net cash fell about 1.17 | [d] res L209, L216, L218-219, L235, L243-244, L278 |
| Promoter pledge | ND | ND | ND | Not in filings | ND |

Supporting stock items (Rs cr): trade receivables 72.49 (Mar-26) to 91.18 (Sep-26), +18.70 (+25.8%) (res L217); inventories 108.52 to 115.48, +6.96 (+6.4%) (res L214); borrowings 2.79 to 5.75 (res L243); current investments 13.86 to 2.81 (-79.7%) (res L216); non-current investments 190.68 to 209.96 (res L209); total investments 204.54 to 212.78 (37.95% of total assets of 560.61; 98.7% non-current) (res L209, L216, L224); trade payables 17.63 to 25.95 (res L252-257); other current financial liabilities 5.27 to 11.10 (+110%) (res L260); other current liabilities 14.21 to 11.69 (-17.7%) (res L261); total equity 467.51 to 488.41 (res L231).

H1 cash funding [d]: CFO Rs 1.84 cr did not cover capex of Rs 2.11 cr (res L300, L303). The Rs 2.32 cr dividend paid (res L319) was in effect funded by Rs 2.87 cr of new borrowing (res L315), not by drawing the treasury.

Deck working-capital days (TTM basis, formula undisclosed): 232 (FY26) to 219 (H1 FY27) (pres L376-377, L382). In rupees working capital absorbed Rs 15.76 cr in H1, and receivable days stretched. The deck's improvement comes from a larger TTM revenue denominator (A3-11). The deck key ratios do not tie to its own balance sheet (current ratio 3.8 shown vs 3.53 period-end; NFAT 2.8 vs 2.22; A3-12). This review uses period-end balance-sheet values, never the slide 17 ratios.

Multi-year conversion (deck, rounded): FY23-FY26 cumulative OCF Rs 74 cr vs PAT Rs 149 cr = 0.50x (pres L762, L713).

Mandatory answers:
- Is CFO/PAT meeting the Pillar 2 cash multiplier assumption? No Notion assumption exists (ND). On the filed numbers, H1 FY27 0.08x, FY26 0.57x and FY23-FY26 0.50x all sit below the lowest band of 0.65x. Pillar-relevant fact flagged for /fttcp and Role 1.
- Is the WC drag structural or growth-induced? Test: "If the company stopped growing tomorrow, would WC days still be high?" FY26 revenue fell 6.6% (247 to 231, pres L697) and CFO/PAT was still 0.57x. Inventory sits at about a year of COGS at both dates. That leans structural. H1 is seasonally the weak cash half, and no rating-agency commentary is in the files. Classification: INDETERMINATE-WITH-DIRECTION (lean structural). Missing evidence that would resolve it: receivable ageing and CIL-subsidiary payment terms; FY27 full-year CFO (Q4 FY27 filing); any CARE/ICRA/CRISIL WC assessment (none in files). Per house rule this caps the verdict at PROCEED WITH CAVEATS or below.
- Did CWIP capitalise as expected? No expectation exists (ND). Rs 47.44 cr net PPE addition came from the Rs 48.25 cr Mar-26 other non-current assets balance (a capital-advance pattern paid in FY26: FY26 capex payments Rs 60.55 cr, res L303) plus Rs 1.12 cr CWIP. No note names the asset (FN09, A3-01, PR/F6-3).
- Net debt within projected range? No projection (ND). Gross borrowing doubled to Rs 5.75 cr. On a liquid basis the company moved from Rs 11.86 cr net cash to Rs 1.53 cr net debt, because current investments fell 79.7% (13.86 to 2.81) while borrowing rose. The Rs 212.78 cr headline book is 98.7% non-current, and its composition and liquidity are undisclosed (FN02, A3-02, A3-16). The borrowing is a liquid funding need at the operating level. Whether the non-current book can be drawn is ND (Q14, Q16).

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
| Signal Name | Type | Cadence | Latest Observation Date and Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| ND (tracker rows not supplied by the orchestrator; no Role 5.5 workup exists for this name) | ND | ND | ND | ND | ND | ND |

Flag: fewer than three signals (zero). Role 5.5 has never run for this company. Reopen Role 5.5 at initial workup if the operator takes the name forward.

### 5.5B. Reconciliation
Target reported: strong YoY (revenue +70.9%, core PBT +226% off a trough base), weak QoQ (revenue -26.7%), weak cash (CFO/PAT 0.08x). Signals said: ND. Interpretation: not assessable. No cell of the four-outcome matrix can be filled.

### 5.5C. New signal actions
No signal written. Under /run-quarterly any write goes through the operator-approval gate, and no company page exists to relate a signal to. The deck surfaces these dependencies as candidate payload rows for Role 5.5 at initial workup (MGMT slides citing SECONDARY sources):
| Candidate signal | Type | Cadence | Source in deck | Thesis element it would test |
|---|---|---|---|---|
| CIL underground coal: continuous-miner fleet and reopened UG mines (47 CMs at 27 mines; 23 discontinued UG mines awarded June 2024; 100 Mt UG target by 2030) | Customer capex / regulatory | Quarterly / event | pres L561-575 | Coal equipment order inflow |
| Hindustan Copper ore capacity (about 4 to 12.2 MTPA by FY2029-30) | Customer capex | Event | pres L589-597 | Metal-mine LHD demand |
| ICEMA domestic construction-equipment sales forecast FY27 (9-12%, raised from about 7%) | Industry volume | Annual / revision | pres L641-642 | Piling-rig demand |
| CIL subsidiary payment behaviour (ECL, MCL, SECL, WCL in customer roster) | Customer liquidity | Quarterly | pres L513 | Receivable days (FN10, A3-11) |

### 5.5D. Feed to Step 6
No signal-reconciled forward view is possible. Step 6 rests on the single-quarter filing alone, which raises the weight of conservative interpretation.

---

## STEP 6: RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections
| Metric | Bear Proj | Base Proj | Bull Proj | Actual (Q2 FY27 / H1 FY27) | Lands In |
|---|---|---|---|---|---|
| Revenue | ND | ND | ND | 56.80 / 134.32 (res L154) | ND (no projections) |
| EBITDA margin (operating) | ND | ND | ND | 18.92% / 18.61% [d] | ND |
| PAT | ND | ND | ND | 7.83 / 23.21 (res L174) | ND |
| EPS (Rs) | ND | ND | ND | 13.58 / 40.24 (res L185) | ND |
| Net debt (ex-investments) | ND | ND | ND | 5.75 at Sep-26 [d] | ND |
| ROCE | ND | ND | ND | 11.7% H1 FY27 TTM, deck formula undisclosed (pres L361) | ND |

Probability re-weighting state: not applicable (no Role 1 scenario weights exist).

### 6B. Watchlist item status
| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| ND | ND (no Notion monitoring checklist) | ND | ND | ND | UNKNOWN |

### 6C. Thesis-broken trigger check
| Thesis-Broken Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| ND (no Notion thesis-broken conditions) | ND | ND | ND |

No condition can fire. No exit or AVOID recommendation arises.

### 6D. Growth trigger status
| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| ND (no Notion growth triggers) | ND | ND | ND | ND |

Candidate growth triggers the filings make observable (for a future thesis, not credited here): order-book execution (Rs 133 cr, res L374, L413); EBITDA margin band 18-20% (res L408); new products CM-3500, MUV, MCAR-E with no commercial data (pres L487, A3-05).

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

Deferred to /fttcp and Role 1 (operator ruling OR-30). No expectation ledger exists for this name (ND). Pillar-relevant facts flagged for the A21 base:
- Seasonality: Q2 < Q1 in both years on file and H2 = 56.3% of FY26 (one H2 observed; FN15). A trailing-four-quarter base is the declared basis, not single-quarter annualisation.
- TTM to Sep-26 [d, FY26 - H1 FY26 + H1 FY27]: revenue Rs 264.26 cr; operating EBITDA Rs 50.43 cr (19.08%); Other Income Rs 14.29 cr; core PBT Rs 40.82 cr (+22.4% vs FY26); PAT Rs 42.09 cr; EPS Rs 72.97.
- Known one-offs to adjust: Q1 FY27 deferred-tax credit Rs 0.94 cr; H1 FV gains Rs 7.21 cr on investments (non-operating, largely MTM); FY26 earlier-period tax credit Rs 0.11 cr. The Q2 margin rests on the unexplained distributor plus other line (FN11); do not fold it into the base until answered.
- Treasury: investments Rs 212.78 cr; net cash including investments Rs 207.03 cr = Rs 358.9 per share [d, 57.684 lakh shares]. LIQUIDITY QUALIFIER (A5-M02): this per-share figure is not a liquid figure. 98.7% of the book (Rs 209.96 cr) is non-current with undisclosed composition. Liquid net cash is Rs (1.53) cr at Sep-26, down from Rs 11.86 cr at Mar-26. The H1 rise in net cash (Rs 6.05 cr) is less than the H1 FV gains (Rs 7.21 cr). Any treasury credit at /fttcp or Role 1 must first establish the book's liquidity and composition (Q14, Q16). Book value per share Rs 846.7 [d, res L231].

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

Deferred to /fttcp and Role 1 (operator ruling OR-30). No Section 1B or FTTCP authority is loaded in this stage. Pillar-relevant facts, each flagged:

| Pillar / Input | Original Assumption | Current Reading (pillar-relevant fact) | Action |
|---|---|---|---|
| ROCE base (Pillar 1) | ND | Deck ROCE 11.7% H1 FY27 TTM, 10.7% FY26; ROE 9.0% / 8.3% (pres L361-366); formula undisclosed and slide 17 ratios do not tie (A3-12). Investments are 37.95% of total assets, which depresses reported ROCE. | Deferred to /fttcp (FTTCP verdict sole authority). Compute operating ROCE ex-treasury there. |
| Cash multiplier (Pillar 2) | ND | CFO/PAT 0.08x H1 FY27, 0.57x FY26, 0.50x FY23-FY26 (res L300; pres L762, L713). Below the 0.65x floor band. | Deferred to Role 1. FLAG. |
| Growth visibility premium | ND | Order book Rs 133 cr = 0.50x TTM revenue (res L374; [d]); definition unresolved (order book vs "open order pipeline", FN19, PR/F16-2). | Deferred. Do not credit until the definition is answered. |
| Strategic premium | ND | No moat evidence in filings; product launches carry no orders or revenue (A3-05). | Deferred. |
| UA multiplier | ND | Shareholding and institutional ownership not in the filings. | Deferred (ND). |
| Sector cap | ND | Capital goods / mining equipment; single segment Machinery and Spares (res L191). | Deferred. |
| Hurdle ratio recheck | ND | No CMP and no EPS CAGR baseline in inputs. TTM EPS Rs 72.97 [d]. | Deferred (ND). |

No destination PE or fair value is computed or revised here.

---

## STEP 8: POSITION DECISION

Decision Status verified: ND (no Notion page). The name is not held in any record passed to this stage. Branch: 8A-W (non-held).

8A-W evaluation: every arm needs a thesis baseline. Thesis-broken conditions: ND, none can fire. Bear/Base/Bull projections: ND, so "below bear / between / at or above base" cannot evaluate. Output of the branch:
- Updated entry zone: ND (none exists; no Role 1 valuation).
- Updated gate: none exists. The pipeline gate for a new name is a Spear line or Step-1 intake (CLAUDE.md SPEAR GATE). Neither exists.
- Proposed Decision Status: none proposed. The operator decides whether to open /step1 intake.

### 8B. Add-back / trim trigger refinement
- Original add-back trigger: ND. Revised: ND.
- Original trim ladder: ND. Revised: ND.
- New information on execution quality for any future thesis: fixed-cost leverage only offset the gross-margin fall (net -59 bps); the whole +321 bps margin gain rests on the unexplained distributor plus other line. Cash conversion is the binding weakness. The liquid treasury turned to net debt. The Rs 47 cr asset is undisclosed.

### 8C. Single cleanest metric for next quarter
Metric: **Q3 FY27 core operating PBT (PBT - Other Income)**, from the Q3 FY27 results (LODR Reg 33 timeline: within 45 days of 31 Dec 2026, so by 14 Feb 2027).
- Why: Other Income swings Rs 1.9-7.8 cr a quarter and is mostly MTM. Core PBT captures order-book execution, the distributor-comp question (FN11) and any D&A step-up from the Rs 47 cr asset (FN09) in one number.
- Bull threshold: at or above Rs 10.21 cr (H2 FY26 per-quarter average core PBT, [d]), with D&A disclosed and distributor comp explained.
- Bear threshold: below Rs 8.55 cr (Q2 FY27 core PBT) despite a Rs 133 cr book. That would mean the order book is not converting in H2, or that the Q2 margin rested on a cost line that reverts. Q2 FY27 itself sits at the bear bar and below the bull bar.
- Second-order (cash) test, not available at Q3: FY27 full-year CFO/PAT at the Q4 FY27 filing (by 30 May 2027). Bull at or above 0.80x; bear below 0.57x (the FY26 level).

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

Ordered by materiality. Each question references a filed number and asks for a number, date or yes/no. Every FORWARD-SIGNAL and AMBIGUOUS A3 finding maps to at least one row (coverage map below the table).

| # | Cat | Question | Why it matters | Bull answer | Bear answer | From finding |
|---|---|---|---|---|---|---|
| 1 | D | H1 FY27 CFO was Rs 1.84 cr against PAT of Rs 23.21 cr, and trade receivables rose from Rs 72.49 cr to Rs 91.18 cr. How much of the Rs 91.18 cr was overdue more than 180 days at 30 Sep 2026? | Cash conversion is the binding weakness (0.08x H1, 0.50x FY23-FY26). | Under Rs 5 cr overdue; the build is Q2 dispatches billed late in September. | A material overdue share, or a refusal to give ageing. | FN10, A3-11 |
| 2 | D | What share of the Rs 91.18 cr receivables is due from Coal India subsidiaries, and what are the contracted payment days? | Tests whether WC is structural (PSU terms) or timing. | Short contracted days with a dated collection plan. | Long PSU terms that make the drag structural. | FN10, A3-11 |
| 3 | A | Compensation to Distributors fell to Rs 3.17 cr (5.6% of revenue) in Q2 from Rs 8.71 cr (11.2%) in Q1, while Other Expenses rose to Rs 12.66 cr (22.3%) from Rs 11.39 cr. Was any amount reclassified between these two lines in Q2: yes or no, and how many Rs cr? | The whole +321 bps YoY margin gain rests on this line group; at the Q1 distributor rate, Q2 EBITDA margin would be 13.3%, not 18.9%. Note 4 (res L193) says comparatives were regrouped to be comparable, yet Q1 FY27 and Q2 FY26 still show 11.2% and 11.9%, which leans against a Q2 reclass. | A dated shift to direct (non-distributor) sales, with the Rs cr named; or a stated reclass with restated comparatives. | No reclassification and no channel change: the Q2 margin rests on a line that reverts. | FN11, FN04, A3-04, PR/F6-1 |
| 4 | F | PPE rose from Rs 64.11 cr to Rs 111.55 cr in H1 while other non-current assets of Rs 48.25 cr went to nil and H1 cash capex was Rs 2.11 cr. What asset was capitalised (land, building or plant), for how many Rs cr, and on what date? | A Rs 47 cr asset is 74% of the prior PPE base, with no note. | Land, or plant with a named capacity and a dated revenue ramp. | Plant capitalised late in Q2 with no capacity disclosure. | FN09, A3-01, PR/F6-3 |
| 5 | F | What annual depreciation charge does the asset capitalised in H1 FY27 add, in Rs cr? | Q2 D&A fell to Rs 2.07 cr; a step-up hits core PBT from Q3. | Nil (land) or small. | A step-up that offsets the H2 order-book margin. | FN09, A3-01 |
| 6 | E | Of the Rs 133 cr reported as order book at 30 Sep 2026, how many Rs cr are signed purchase orders not yet executed, net of GST? | The release calls the same Rs 133 cr an "open order pipeline"; a pipeline can include bids. | All Rs 133 cr firm, net of GST. | A part is bids or enquiries, or the figure is gross of GST. | FN19, FN05, A3-15, PR/F16-2, PR/F6-2 |
| 7 | E | What was the order book at 31 Mar 2026 and at 30 Jun 2026, in Rs cr, on the same definition? | Only Sep-25 (Rs 44 cr) is given; H1 inflow and book-to-bill cannot be computed. | A rising sequential book with H1 inflow above H1 revenue of Rs 134 cr. | A flat or falling sequential book. | FN05, A3-15, PR/F6-2 |
| 8 | G | Who is the successor or interim CFO, and on what date will that person take office? | The CFO leaves on 30 Oct 2026; Q3 FY27 close and limited review will be the first without him. | A named appointee before 30 Oct 2026. | No appointee by the Q3 board meeting. | FN16 |
| 9 | G | On what date did the company receive Mr. Begwani's letter dated 5 Sep 2026, and was an earlier Reg 30 intimation filed: yes or no? | The exchange disclosure came 38 days after the letter date. | Received close to 13 Oct, or an earlier intimation exists. | Received early September with no earlier disclosure. | FN17 |
| 10 | C | What were product revenue and spares revenue in Rs cr for Q2 FY26, Q1 FY27 and Q2 FY27, and which chart segment is spares? | Gross margin tracks the unlabelled chart segment in every period; mix drives margin. | Spares share stable or rising. | Equipment-heavy growth with spares share falling (35% Q2 FY27 vs 48% Q2 FY26 under one reading). | FN12, A3-14, PR/F12-1 |
| 11 | C | Filing-basis gross margin fell from 71.75% in Q2 FY26 to 59.88% in Q2 FY27. How many bps of that fall is product mix, and how many is price? | The gross-margin fall (-1,187 bps) was larger than the fixed-cost recovery (+1,128 bps). | Mostly mix, with stable equipment pricing. | Price erosion on equipment orders. | A3-13, FN12 |
| 12 | A | Q2 built Rs 11.50 cr of finished goods and WIP while revenue fell 26.7% QoQ. What share of the Sep-26 inventory of Rs 115.48 cr is against orders scheduled to ship in Q3 FY27? | Inventory sits at about a year of COGS. | Most of the build ships in Q3. | Slow-moving stock with no dispatch date. | FN12 |
| 13 | A | Q2 FY27 revenue of Rs 56.80 cr was 26.7% below Q1 FY27 (Rs 77.52 cr). Did any order planned for Q2 slip to H2: yes or no, and for how many Rs cr? | The release says "sustained momentum" but shows YoY only. | No slippage; seasonal dispatch pattern. | A named slippage. | PR/F16-1, A3-13, FN18 |
| 14 | F | Borrowings rose from Rs 2.79 cr to Rs 5.75 cr while investments stood at Rs 212.78 cr and current investments fell to Rs 2.81 cr. What is the facility type and interest rate? | Liquid net cash moved from Rs 11.86 cr to Rs (1.53) cr; the H1 dividend was in effect funded by borrowing. | A cheap working-capital line kept for banking relations. | A liquidity need the treasury book cannot meet (illiquid or locked investments). | FN02, A3-02 |
| 15 | C | Q1 FY27 carried a deferred-tax credit of Rs 0.94 cr and DTL fell from Rs 7.70 cr to Rs 6.76 cr. Which temporary difference reversed? | Ex-deferred H1 ETR is 25.91%; the credit may not recur. | A named one-time item, with FY27 ETR guided near 25%. | No explanation. | FN07, A3-08 |
| 16 | D | Of H1 Other Income of Rs 9.65 cr, Rs 7.21 cr is fair-value and sale gains. What share of the Rs 209.96 cr non-current investment book is equity or equity funds? | OI is 32.1% of H1 PBT and mostly MTM; the book is 98.7% non-current. | Mostly debt instruments with stable accrual and short redemption terms. | Mostly equity or locked instruments, so PBT carries market risk and the book is not liquid. | A3-16 |
| 17 | F | The reserve roll implies an FY26 dividend of Rs 4.00 per share vs Rs 5.00 for FY25. Confirm the FY26 DPS, and was the cut made to fund the Rs 60.55 cr FY26 capex: yes or no? | Capital allocation signal. | Yes, a one-time capex funding decision. | A cut with no stated reason. | FN08 |
| 18 | D | Other current financial liabilities rose from Rs 5.27 cr to Rs 11.10 cr. How many Rs cr of the Rs 11.10 cr are capital creditors? | It may hold unpaid capex for the Rs 47 cr asset. | Capital creditors tied to the H1 asset. | Unexplained. | FN14 |
| 19 | D | Other current liabilities fell from Rs 14.21 cr to Rs 11.69 cr while the order book rose. What were customer advances in Rs cr at 31 Mar 2026 and 30 Sep 2026? | Falling advances with a rising book means weaker customer funding of WC. | Advances stable or up. | Advances down. | FN14 |
| 20 | C | The release states Q2 EBITDA margin 18.8% and growth 108.8%; the filed statement gives 18.9% and 105.8% on PBT plus D&A plus finance cost less Other Income. What is the company's EBITDA definition? | Undefined headline metric. | A stated definition that reconciles. | No definition. | FN20, PR/F14-1 |
| 21 | C | The 18-20% targeted range: is it EBITDA excluding Other Income, and is 20% a ceiling given FY25 EBITDA margin of 22.7%? | The band sits below the FY25 peak; it may cap a margin reset. | EBITDA ex-OI; 20% is a floor for FY28. | 20% is the ceiling. | FN04, A3-04, PR/F6-1 |
| 22 | C | The release says "Margins improved year-on-year" next to PAT, but PAT margin fell from 16.1% to 13.8%. Which margin does the sentence refer to? | Framing tell. | EBITDA margin, with a correction in the next release. | No answer. | FN18, A3-13 |
| 23 | B | How many units of CM-3500, MUV and MCAR-E were delivered in H1 FY27, and how many Rs cr of the Rs 133 cr order book are these products? | Launches carry no commercial data. | Named orders. | Nil orders. | A3-05 |
| 24 | B | What Rs cr of the order book is for CIL reopened underground mines, and what Rs cr for metal mines (HCL, HZL, UCIL, MOIL, HGML)? | The outlook slides are third-party sector data, self-hedged. | A material Eimco-specific CIL or metals share. | Sector context with no orders behind it. | A3-06 |
| 25 | B | How many piling-rig orders (units) were booked after Bauma ConExpo India, 15-18 Sep 2026? | The deck pre-empts flat construction demand. | Named orders. | None. | A3-07 |
| 26 | C | What formulas give the slide 17 ratios (ROCE 11.7%, current ratio 3.8, NFAT 2.8): period-end or average balances? | The ratios do not tie to the deck's own balance sheet. | A stated, consistent formula. | Undisclosed or inconsistent. | A3-12 |

Coverage map (35 FORWARD-SIGNAL / AMBIGUOUS findings, all covered):
- Results: FN02 (Q14), FN04 (Q3, Q21), FN05 (Q6, Q7), FN07 (Q15), FN08 (Q17), FN09 (Q4, Q5), FN10 (Q1, Q2), FN11 (Q3), FN12 (Q10, Q11, Q12), FN14 (Q18, Q19), FN16 (Q8), FN17 (Q9), FN18 (Q13, Q22), FN19 (Q6), FN20 (Q20).
- Presentation: A3-01 (Q4, Q5), A3-02 (Q14), A3-04 (Q3, Q21), A3-05 (Q23), A3-06 (Q24), A3-07 (Q25), A3-08 (Q15), A3-11 (Q1, Q2), A3-12 (Q26), A3-13 (Q11, Q13, Q22), A3-14 (Q10), A3-15 (Q6, Q7), A3-16 (Q16).
- Press release: PR/F6-1 (Q3, Q21), PR/F6-2 (Q6, Q7), PR/F6-3 (Q4), PR/F12-1 (Q10), PR/F14-1 (Q20), PR/F16-1 (Q13), PR/F16-2 (Q6).
- NEUTRAL-FACT findings (FN01, FN03, FN06, FN13, FN15, A3-03, A3-09, A3-10, PR/F14-2) need no question; FN03, FN06 and A3-03 go to monitorables.

Top 3 by likelihood of thesis-changing information:
- Q3 (distributor comp vs Other Expenses): a "no reclassification, no channel change" answer would move the Q2 margin from 18.9% toward 13.3% and remove the whole YoY margin gain. Note 4 already leans this way. Changes bull probability most.
- Q1 (receivable ageing): a material overdue share confirms the structural cash-conversion bear case.
- Q8 (successor CFO): tests management transparency and continuity during the Q3 close.

Channel recommendation: IR email. No concall is in this run and none is scheduled in the inputs (ND). Send all 26 questions verbatim to the investor contact named in the release, Ms. Vrushali Thakkar, vsthakkar1@eimcoelecon.in (res L451-452). If a Q2 FY27 concall is announced, put Q3, Q1 and Q8 live and submit the rest in writing. AGM Q&A is the fallback for any question left unanswered by the Q3 FY27 results.

---

## MONITORABLES AND CATALYST LIST (seeded by A3 F6 commitment registers and F13 board items)

| # | Item | Implied date | Source ref | What to check |
|---|---|---|---|---|
| M1 | CFO Vishal C. Begwani ceases as CFO, KMP, materiality KMP and Risk Committee member | 2026-10-30 (close of business) | res L41-50, L474-475 (FN16) | Exchange filing of cessation; interim arrangement |
| M2 | CFO handover "of all financial operations, statutory reporting, audit closures" | by 2026-10-30 | res L508-511 | Any qualification or delay at Q3 close |
| M3 | Successor CFO appointment | NOT STATED. Companies Act 2013 s.203(4) six-month window from vacancy implies 2027-04-30 [statute, not in filing; PENDING LIVE VERIFICATION]. Any LODR timeline: PENDING LIVE VERIFICATION. | res L41-44, L476 (FN16) | Reg 30 appointment filing |
| M4 | Q3 FY27 results: core PBT (8C metric), D&A run-rate after the Rs 47 cr capitalisation, distributor comp line, revenue vs order book | by 2027-02-14 (LODR Reg 33, 45 days after 31 Dec 2026) | res L154-168; FN09, FN11 | Bull at or above Rs 10.21 cr core PBT; bear below Rs 8.55 cr |
| M5 | EBITDA margin vs "targeted range of 18-20%" | Undated, every quarter | res L408; pres L327 (FN04, A3-04, PR/F6-1) | Operating EBITDA margin each quarter |
| M6 | Execution of Rs 133 cr order book / "open order pipeline" | Undated; about six months at the TTM run-rate, so H2 FY27 [d] | res L374, L413-415; pres L354-356 (FN05, A3-15, PR/F6-2) | Sequential order book and inflow in the Q3 deck |
| M7 | "continuing to invest in capabilities" | Undated | res L409 (PR/F6-3) | Capex note; asset named |
| M8 | Q4 FY27 / FY27 audited results with H2 cash flow: full-year CFO/PAT | by 2027-05-30 (LODR Reg 33, 60 days after 31 Mar 2027) | res L300 (FN10, A3-11) | Bull at or above 0.80x; bear below 0.57x |
| M9 | FY27 annual report: tax note (DTL reversal), PPE schedule (asset class of the Rs 47 cr addition), actuarial OCI, related parties, investment composition | AGM date ND | FN06, FN07, FN09, A3-16, Z2-Z4 | Verify each at the Role 6 deep dive |
| M10 | Borrowings, liquid net cash and new non-current liability lines (Rs 0.28 cr and Rs 0.09 cr) | Mar-27 balance sheet | res L216-219, L236-237, L243 (FN02, FN03) | Size and nature; liquid net cash back above zero or not |
| M11 | Exceptional line in the deck template | Each quarter | pres L401 (A3-03) | Any non-zero entry |
| M12 | New products CM-3500, MUV, MCAR-E commercial data | Next deck (with Q3 FY27 results, by 2027-02-14) | pres L487, L182-186 (A3-05) | Orders or units disclosed |
| M13 | Piling-rig leads after Bauma ConExpo India (15-18 Sep 2026, held) | Next deck | pres L539-544 (A3-07) | Orders disclosed |
| M14 | FY27 dividend per share vs implied FY26 Rs 4.00 | FY27 board outcome (with Q4 results) | res L319, L230 (FN08) | DPS and reason |

---

## VERDICT

Protocol verdict: **PROCEED WITH FLAGS**. The filed numbers are clean: unmodified limited review, all statements tie, no exceptional items, standalone-only filer. Core PBT grew 226% YoY, but off a trough base: TTM core PBT grew 22.4%, and Q2's Rs 8.55 cr sits below the H2 FY26 quarterly average of Rs 10.21 cr. 60% of the YoY gain equals the unexplained distributor-rate drop. Four items need to be surfaced, and cash conversion caps the verdict below PROCEED in any case:
1. Cash conversion INDETERMINATE-WITH-DIRECTION (lean structural): H1 CFO/PAT 0.08x; FY23-FY26 0.50x. Missing evidence named in Step 5.
2. Governance: CFO exits 30 Oct 2026 with no successor named, after a 38-day letter-to-disclosure gap.
3. Disclosure gaps that move the margin read: an unnamed Rs 47.44 cr capitalisation, and the distributor plus other line, which carries the whole +321 bps margin gain. Note 4's regrouped comparatives lean against the reclass reading.
4. Treasury liquidity: liquid net cash moved from Rs 11.86 cr to Rs (1.53) cr in H1; the Rs 212.78 cr book is 98.7% non-current with undisclosed composition.

The Loop 1 fixes strengthen the flags. They raise no mechanical failure and no REWORK trigger, so the verdict stands.

Standalone vs consolidated gap (A3 F2): N.A. in every period. Note 3 (res L192) states no subsidiary, associate or JV. No consolidated statement exists.

---

## PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (results filing), MGMT (company deck or release statements), SECONDARY (third-party data the deck cites), INFERENCE (this review's reading). Every figure below comes from this quarter's filings or deck. No prior Notion or peer work exists for this name.

### 1. Summary narrative
Eimco Elecon sold Rs 56.80 cr in Q2 FY27, up 70.9% from Rs 33.24 cr a year ago [FILED].
The base was weak. Q2 FY26 revenue had fallen 50.8% from the quarter before it [FILED, derived].
Against Q1 FY27, revenue fell 26.7% [FILED]. Q2 was below Q1 in both years, and H2 was 56.3% of FY26 revenue [FILED, derived]. Only one H2 is on file.
Core profit before tax, after taking out other income, rose from Rs 2.62 cr to Rs 8.55 cr [FILED]. That growth is off a trough base. Over twelve months core profit grew 22.4% [FILED, derived].
Q2's Rs 8.55 cr is below last year's H2 quarterly average of Rs 10.21 cr [FILED, derived].
Reported profit after tax rose 46.4% to Rs 7.83 cr, because treasury income fell [FILED].
Operating margin rose to 18.9% from 15.7% [FILED]. Gross margin fell from 71.8% to 59.9% [FILED].
Lower staff and factory costs per rupee of sales only made up for the lower gross margin [FILED, derived]. The whole margin rise came from one cost group, distributor payments plus other expenses [FILED, derived].
Inside that group, distributor payments fell while sales rose 71%, and other expenses rose 92% [FILED]. Until the company explains this, the 18.9% margin is not proven [INFERENCE].
Cash is the weak point. The first half produced Rs 1.84 cr of operating cash against Rs 23.21 cr of profit [FILED].
Receivables grew 25.8% in six months to Rs 91.18 cr [FILED].
The liquid part of the treasury moved from Rs 11.86 cr net cash to Rs 1.53 cr net borrowing [FILED, derived].
Plant and equipment jumped by Rs 47.44 cr with no note to say what was bought [FILED].
The CFO leaves on 30 Oct 2026, and the filing names no successor [FILED].
There is no thesis, no Notion page and no Decision Status for this name. This is a pre-thesis read.
The decision for the operator is whether to open a Step-1 intake. Nothing in this quarter forces either answer.

### 2. Sector intelligence
Demand comes from underground coal and metal mines, plus construction piling [MGMT, res L428-434].
Coal: the government targets 100 Mt of underground coal by 2030 [SECONDARY, PIB, pres L561]. Coal India runs only 47 continuous miners across 27 mines [SECONDARY, CIL, pres L568]. Coal India has awarded 23 discontinued underground mines for reopening [SECONDARY, pres L573]. The deck itself says the production goal and the fleet plan are separate [MGMT, pres L579].
Metals: Hindustan Copper plans ore capacity of 12.2 MTPA by FY2029-30, from about 4 [SECONDARY, pres L589-597]. The deck calls uranium projects an in-principle pipeline, not committed capex [MGMT, pres L627].
Construction: real construction GVA grew 7.7% in Apr-Jun 2026 [SECONDARY, MoSPI, pres L636]. ICEMA expects 9-12% FY27 equipment sales across all construction equipment, not piling rigs alone [SECONDARY, pres L641-643]. A real-estate survey reads neutral at 50 [SECONDARY, pres L646].
Read: the coal and metals tailwinds are real at sector level. The deck gives no Eimco order figure tied to any of them [INFERENCE, A3-06].
Payer mix: the customer roster is mostly state-owned miners (Coal India subsidiaries, Singareni, MOIL, Hutti Gold, UCIL) [MGMT, pres L513]. State payers usually pay slowly [INFERENCE]. That fits the cash picture.

### 3. Business-model intelligence
The company makes underground loaders (LHDs and side-dump loaders), continuous-miner packages, man-riding chair lifts, piling rigs and new battery vehicles [MGMT, pres L476, L487].
It reports one segment, Machinery and Spares [FILED, res L191].
It has 1,065 machines in the field: 683 in coal, 382 in other mining [MGMT, pres L504-511]. That base feeds spares sales.
It pays distributors a commission that ran at 11.5% of FY26 sales [FILED, res L165].
It holds Rs 212.78 cr of investments, 38% of total assets [FILED, res L209, L216, L224]. 98.7% of the book is non-current, and its composition is not disclosed [FILED, derived]. Other income was 32.1% of first-half profit before tax [FILED].
Model drift this quarter: growth came from equipment, not spares, if the unlabelled chart reads the likely way [INFERENCE, A3-14]. Equipment carries a lower gross margin than spares [INFERENCE].
A Rs 133 cr order book that is mostly equipment would lift H2 sales and press H2 gross margin [INFERENCE].
The company did not disclose: product vs spares revenue, order inflow, order-book definition, receivable ageing, the new asset, investment composition, or its EBITDA definition.

### 4. Competition intelligence
The filings name no competitor, and Notion passed no peer set.
From general industry knowledge, not from these filings [INFERENCE, PENDING LIVE VERIFICATION]: global loader and continuous-miner makers such as Sandvik, Epiroc and Komatsu Mining compete for Coal India and metal-mine tenders. BEML is a domestic state-owned mining-equipment maker.
Where Eimco looks strong: a long-installed fleet that needs spares, a domestic plant and service network (1 plant, 10 sales offices) [MGMT, pres L262-273], and an early position in semi-mechanised underground coal [MGMT, pres L155].
Where it looks weaker: small scale (TTM revenue Rs 264.26 cr) [FILED, derived], dependence on state-owned buyers, and slow cash collection [FILED].
Competitive risk to watch: gross margin on new equipment orders. A fall from 71.8% to 59.9% YoY may reflect tender pricing, not only mix [INFERENCE]. Question 11 separates the two.

### 5. Forward map (next ~10-11 months)
Make-or-break reading: Q3 FY27 core profit before tax, in the Q3 results due by 14 Feb 2027. Bull at or above Rs 10.21 cr. Bear below Rs 8.55 cr.
- 30 Oct 2026, CFO exit. Bull: a named successor before the date. Bear: no appointee by the Q3 board meeting.
- By 14 Feb 2027, Q3 FY27 results. Bull: core PBT at or above Rs 10.21 cr with D&A and distributor comp explained. Bear: core PBT below Rs 8.55 cr, or a D&A step-up that eats the margin.
- Every quarter, margin band 18-20%. Bull: operating EBITDA margin holds inside the band with the distributor line explained. Bear: the distributor line reverts and margin falls toward 13%.
- H2 FY27, Rs 133 cr order book. Bull: a firm, net-of-GST book that grows sequentially. Bear: the figure turns out to include bids, or the sequential book falls.
- Next deck (with Q3 results), new products and piling rigs. Bull: named orders for CM-3500, MUV, MCAR-E or piling rigs. Bear: no commercial data again.
- By 30 Apr 2027, statutory CFO window. Bull: a permanent CFO in office. Bear: the vacancy is still open.
- By 30 May 2027, FY27 results with full-year cash flow. Bull: CFO/PAT at or above 0.80x and liquid net cash back above zero. Bear: CFO/PAT below 0.57x, which confirms the structural reading.

---

## LOOP 1 CHANGES (A5 audit, work/audit_eimcoeleco_q2fy27.md)

All figures were rechecked against the A1 results fulltext (res L154-174, L193, L209-243, L278, L300-319) before writing.
- A5-F01 (FACTUAL): the summary line "Q1-high, Q2-low, H2-heavy pattern in both years [FILED]" is replaced with "Q2 was below Q1 in both years, and H2 was 56.3% of FY26 revenue [FILED, derived]. Only one H2 is on file." The same fix is applied to the Step 3 trajectory diagnostic and the Step 6.5 seasonality bullet.
- A5-F02 (FACTUAL): the "fixed-cost leverage" attribution is removed from Step 2 (table and diagnostic 2), the Step 4 margin rows (now UNRESOLVED), 8B, Q11, the summary and analyst_note. New reading: gross margin -1,187 bps, employee +814, manufacturing +314, net -59 bps. The whole +321 bps rests on the distributor plus other line (+380 bps). Other Expenses +92.3% and distributor comp -19.6% in rupees. Without that line, the margin would be about 15.11%. The Note 4 regrouping point (res L193) is added to Step 0D, Q3 (why, bull answer), the verdict and flag 5. The Q3 bull answer no longer treats a reclass as the likely good outcome.
- A5-M01 (MISSING): the base-effect qualifier is added to the verdict, the Step 2 table and diagnostic 3, the Step 4 recurring answer, 8C and the summary. It covers: TTM core PBT +22.4% (40.82 vs 33.35), H1 +57.7%, the Q2 level Rs 8.55 cr below the H2 FY26 quarterly average of Rs 10.21 cr and Q1 FY26 Rs 10.32 cr, and the distributor-rate drop of Rs 3.57 cr = 60% of the Rs 5.93 cr YoY gain.
- A5-M02 (MISSING): treasury liquidity is added to Step 5, both in a new liquid net cash row (11.86 to (1.53)) and in the qualified all-investments row (98.7% non-current; the +6.05 rise is below the 7.21 FV gains). Step 5 also gains the H1 cash funding line (CFO 1.84 < capex 2.11; dividend 2.32 in effect funded by 2.87 of new borrowing) and a rewritten net-debt answer. The qualifier is attached to the Rs 358.9 per share figure in Step 6.5. Q14, Q16, M10, the business-model brief, the summary and a new verdict item 4 are updated.
- Style applied at no extra cost: S01 (sector anchor pres L428-434 corrected to res L428-434); S04 (25.17% marked [statute, not in filing; tax-regime election NOT FOUND]); S05 (Q2 FY26 -50.8% tagged [FILED, derived]).
- Verdict unchanged: PROCEED WITH FLAGS. Flags were added and sharpened; no REWORK or INSUFFICIENT EVIDENCE trigger arises.

```yaml
stage: A4-analyst
company: "EIMCOELECO"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, presentation, pressrelease]
ledger_reconciliation:
  notes: 7
  turns: 0
  slides: 43
  all_reviewed: true
  a3_findings_incorporated: [FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN19, FN20, A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, PR/F6-1, PR/F6-2, PR/F6-3, PR/F12-1, PR/F14-1, PR/F14-2, PR/F16-1, PR/F16-2]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "ND (no Notion COMPANIES MASTER page; PRE-THESIS READ; orchestrator live fetch 2026-10-17)"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY27", gap: "N.A. (standalone-only filer; Note 3, res L192)"}
  - {period: "Q1 FY27", gap: "N.A."}
  - {period: "Q2 FY26", gap: "N.A."}
  - {period: "H1 FY27", gap: "N.A."}
  - {period: "FY26", gap: "N.A."}
questions_for_management:
  - {q: "Rs cr of the Rs 91.18 cr receivables overdue >180 days at 30 Sep 2026?", from_finding_id: "FN10, A3-11"}
  - {q: "Share of receivables due from CIL subsidiaries and contracted payment days?", from_finding_id: "FN10, A3-11"}
  - {q: "Was any amount reclassified between Compensation to Distributors (3.17 cr, 5.6%) and Other Expenses (12.66 cr, 22.3%) in Q2: yes/no, Rs cr? (Note 4 regrouped comparatives still show 11.2% / 11.9%)", from_finding_id: "FN11, FN04, A3-04, PR/F6-1"}
  - {q: "What asset was capitalised into PPE (64.11 to 111.55 cr), Rs cr, date?", from_finding_id: "FN09, A3-01, PR/F6-3"}
  - {q: "Annual depreciation added by the H1 capitalisation, Rs cr?", from_finding_id: "FN09, A3-01"}
  - {q: "Rs cr of the Rs 133 cr that are signed POs not yet executed, net of GST?", from_finding_id: "FN19, FN05, A3-15, PR/F16-2, PR/F6-2"}
  - {q: "Order book at 31 Mar 2026 and 30 Jun 2026 on the same definition?", from_finding_id: "FN05, A3-15, PR/F6-2"}
  - {q: "Name and start date of successor or interim CFO?", from_finding_id: "FN16"}
  - {q: "Date the 5 Sep 2026 CFO letter was received; earlier Reg 30 intimation yes/no?", from_finding_id: "FN17"}
  - {q: "Product vs spares revenue Rs cr for Q2 FY26, Q1 FY27, Q2 FY27; which chart segment is spares?", from_finding_id: "FN12, A3-14, PR/F12-1"}
  - {q: "Bps split of the 1,187 bps YoY gross-margin fall between mix and price?", from_finding_id: "A3-13, FN12"}
  - {q: "Share of Rs 115.48 cr inventory against orders shipping in Q3 FY27?", from_finding_id: "FN12"}
  - {q: "Did any Q2 order slip to H2: yes/no, Rs cr?", from_finding_id: "PR/F16-1, A3-13, FN18"}
  - {q: "Facility type and rate of the Rs 5.75 cr borrowing, given liquid net cash moved to Rs (1.53) cr?", from_finding_id: "FN02, A3-02"}
  - {q: "Which temporary difference reversed in the Rs 0.94 cr Q1 deferred-tax credit?", from_finding_id: "FN07, A3-08"}
  - {q: "Share of the Rs 209.96 cr non-current investment book in equity or equity funds?", from_finding_id: "A3-16"}
  - {q: "Confirm FY26 DPS Rs 4.00 vs Rs 5.00; cut to fund FY26 capex yes/no?", from_finding_id: "FN08"}
  - {q: "Rs cr of the Rs 11.10 cr other current financial liabilities that are capital creditors?", from_finding_id: "FN14"}
  - {q: "Customer advances at 31 Mar 2026 and 30 Sep 2026, Rs cr?", from_finding_id: "FN14"}
  - {q: "Company EBITDA definition (18.8% stated vs 18.9% computed; 108.8% vs 105.8%)?", from_finding_id: "FN20, PR/F14-1"}
  - {q: "Is the 18-20% band EBITDA ex-OI, and is 20% a ceiling given FY25 22.7%?", from_finding_id: "FN04, A3-04, PR/F6-1"}
  - {q: "Which margin does 'Margins improved year-on-year' refer to, given PAT margin fell 16.1% to 13.8%?", from_finding_id: "FN18, A3-13"}
  - {q: "Units delivered and Rs cr in order book for CM-3500, MUV, MCAR-E?", from_finding_id: "A3-05"}
  - {q: "Rs cr of the order book for CIL reopened UG mines vs metal mines?", from_finding_id: "A3-06"}
  - {q: "Piling-rig orders (units) booked after Bauma ConExpo India 15-18 Sep 2026?", from_finding_id: "A3-07"}
  - {q: "Formulas for slide 17 ROCE 11.7%, current ratio 3.8, NFAT 2.8?", from_finding_id: "A3-12"}
monitorables:
  - {item: "CFO Begwani ceases as CFO/KMP/Risk Committee member", implied_date: "2026-10-30", source_ref: "res L41-50, L474-475 (FN16)"}
  - {item: "CFO handover incl. statutory reporting and audit closures", implied_date: "2026-10-30", source_ref: "res L508-511"}
  - {item: "Successor CFO appointment", implied_date: "NOT STATED; s.203(4) six months implies 2027-04-30 (PENDING LIVE VERIFICATION)", source_ref: "res L41-44, L476 (FN16)"}
  - {item: "Q3 FY27 results: core PBT, D&A after Rs 47 cr capitalisation, distributor comp", implied_date: "by 2027-02-14", source_ref: "res L154-168 (FN09, FN11)"}
  - {item: "EBITDA margin vs 18-20% band", implied_date: "undated, every quarter", source_ref: "res L408; pres L327"}
  - {item: "Execution of Rs 133 cr order book", implied_date: "H2 FY27 (about six months at TTM run-rate, derived)", source_ref: "res L374, L413-415; pres L354-356"}
  - {item: "Invest in capabilities: asset named", implied_date: "undated", source_ref: "res L409 (PR/F6-3)"}
  - {item: "FY27 full-year CFO/PAT", implied_date: "by 2027-05-30", source_ref: "res L300 (FN10, A3-11)"}
  - {item: "FY27 AR: tax note, PPE schedule, OCI, investment composition", implied_date: "AGM date ND", source_ref: "FN06, FN07, FN09, A3-16"}
  - {item: "Borrowings, liquid net cash and new NC liability lines", implied_date: "Mar-27 balance sheet", source_ref: "res L216-219, L236-237, L243 (FN02, FN03)"}
  - {item: "Deck Exceptional line non-zero", implied_date: "each quarter", source_ref: "pres L401 (A3-03)"}
  - {item: "New products commercial data", implied_date: "next deck, by 2027-02-14", source_ref: "pres L487 (A3-05)"}
  - {item: "Piling-rig orders after Bauma ConExpo", implied_date: "next deck", source_ref: "pres L539-544 (A3-07)"}
  - {item: "FY27 DPS vs implied FY26 Rs 4.00", implied_date: "Q4 FY27 board outcome", source_ref: "res L319, L230 (FN08)"}
flags:
  - "PRE-THESIS READ: no Notion page, no companies file, no spear; Decision Status ND"
  - "Cash conversion INDETERMINATE-WITH-DIRECTION (lean structural): H1 FY27 CFO/PAT 0.08x, FY26 0.57x, FY23-FY26 0.50x; receivables +25.8% in H1"
  - "CFO exits 2026-10-30 with no successor named; letter dated 2026-09-05 disclosed 2026-10-13 (38 days)"
  - "Rs 47.44 cr net PPE addition in H1 with no note; D&A not yet stepped up; Q3 D&A is the tell"
  - "Whole +321 bps YoY margin gain rests on the distributor plus other line (fixed-cost lines net -59 bps vs GM fall); distributor comp 5.6% of Q2 revenue vs 11.2-11.9%; Note 4 regrouped comparatives lean against a reclass; Q2 margin 18.9% not creditable until answered"
  - "Core PBT +226% YoY is off a trough base: TTM +22.4%, H1 +57.7%; Q2 Rs 8.55 cr below H2 FY26 quarterly average Rs 10.21 cr; 60% of YoY gain equals the distributor-rate drop"
  - "Treasury liquidity: liquid net cash Rs 11.86 cr to Rs (1.53) cr in H1; current investments -79.7%; book 98.7% non-current, composition undisclosed; Rs 358.9/share net cash is not a liquid figure; H1 dividend in effect funded by borrowing"
  - "Rs 133 cr labelled both order book and open order pipeline; definition unresolved"
  - "Other income 32.1% of H1 PBT; 74.7% of H1 OI is FV gains (largely MTM)"
  - "Q1 FY27 deferred-tax credit Rs 0.94 cr; ex-deferred H1 ETR 25.91%"
  - "Implied FY26 DPS cut Rs 5.00 to Rs 4.00 (derived from reserve roll)"
  - "Data corrections applied: R150 belongs to 31.03.26; H1 FY26 investing comparatives row-misaligned (H1 FY26 capex ND); text glitches R014/R153/R242 resolved"
  - "Downstream tracker rows not supplied; zero signals; reopen Role 5.5 at initial workup"
  - "Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); pillar facts flagged in review"
plain_language_brief_included: true
analyst_note: "Loop 1 applied (A5-F01, F02, M01, M02). Core PBT rose from Rs 2.62 cr to 8.55 cr YoY, but off a trough base: TTM +22.4%, H1 +57.7%. Q2 sits below the H2 FY26 quarterly average of Rs 10.21 cr. The +321 bps margin gain is not fixed-cost leverage. Gross margin -1,187 bps, employee +814 and manufacturing +314 net to -59 bps. The whole gain rests on the distributor plus other line (+380 bps). The distributor-rate drop alone equals 60% of the YoY core-PBT gain. Note 4's regrouped comparatives still show 11.2% and 11.9%, which leans against a Q2 reclass. Cash conversion is the binding weakness. FY26 (revenue down, CFO/PAT 0.57x) leans structural, hence INDETERMINATE-WITH-DIRECTION. Liquid net cash moved from Rs 11.86 cr to Rs (1.53) cr. 98.7% of the treasury is non-current and undisclosed, so the Rs 358.9 per share figure is not liquid. PROCEED WITH FLAGS stands: the fixes sharpen the flags but trigger no REWORK. 8A-W applies because the name is not held. Statutory dates are marked for live verification."
review_path: "runs/eimcoeleco-q2fy27/work/review_eimcoeleco_q2fy27.md"
```
