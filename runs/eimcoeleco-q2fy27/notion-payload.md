# Notion payload: EIMCOELECO Q2 FY27 (PENDING, NOT WRITTEN)

STATUS: READY FOR OPERATOR APPROVAL, CLOSED WITH OPEN ITEMS. A5 is INCOMPLETE after correction
loop 2 (open: A5-F04, A5-M05, A5-M06; see work/audit_eimcoeleco_q2fy27.md). By operator ruling
2026-10-17 there is no third loop; the run closes with these items flagged in the review
("OPEN ITEMS AT CLOSE"). Under the write gate, every write needs the operator's explicit
approval. Decision Status is never written.

TARGET: no COMPANIES MASTER page exists (live search 2026-10-17: "Eimco Elecon" and
"EIMCOELECO"; the "Eimco" hits on KCPSUGIND refer to Eimco-KCP, another entity). The save
therefore needs a NEW page.
- Data source: COMPANIES MASTER, collection://345bb2b9-d3ab-8032-9b46-000ba16ab827
- Call 1: notion-create-pages with properties:
  - Name: "Eimco Elecon (India) Ltd"
  - Ticker: "EIMCOELECO"
  - Sector: "Capital Goods / Mining Equipment"
  - date:Analysis Date 1:start: "2026-10-17"
  - Key Notes (new page, so no prior trail to preserve; escape | as \|):
    "2026-10-17 \| Q2 FY27 pre-thesis read (/run-quarterly; results + deck + press release, all 13-Oct-2026): revenue 56.80 cr (+70.9% YoY off a trough base, -26.7% QoQ); core PBT 2.62 to 8.55 cr (+226% YoY, but trough-free Q1 YoY +14.9%, TTM EPS 14.4% below FY25); operating EBITDA margin 18.9% vs 15.7%, whole gain on the unexplained distributor plus other line; H1 CFO 1.84 cr vs PAT 23.21 cr, (5.30) cr without a 7.14 cr other-liabilities inflow, cash conversion INDETERMINATE-WITH-DIRECTION; liquid net cash 11.86 to (1.53) cr; unnamed 47.44 cr PPE addition; CFO exits 30-Oct-2026, no successor named; Rs 133 cr order book vs open order pipeline label unresolved \| Protocol verdict PROCEED WITH FLAGS \| A5 INCOMPLETE after loop 2, 3 items open (operator ruling: no third loop) \| no trigger fired (no thesis)"
  - Decision Status: NOT WRITTEN (operator-only)
- Call 2..n: insert_content, position end, in sequential chunks: the full A4 review below
  (complete tables, includes the PLAIN-LANGUAGE BRIEF and OPEN ITEMS AT CLOSE), then the three
  A3 forensics tables, then the A5 audit verdict block.

=====================================================================
## CONTENT PART 1: A4 MERGED REVIEW (work/review_eimcoeleco_q2fy27.md, verbatim)
=====================================================================
# A4 REVIEW: Eimco Elecon (India) Limited (EIMCOELECO) | Q2 FY27 | Role 4 (Quarterly Results Review Protocol v1.4)

Run: /run-quarterly A4 analyst | Model: claude-opus-5-5 | Date: 2026-10-17 | Revision: Loop 2 (Loop 1: A5-F01, A5-F02, A5-M01, A5-M02; Loop 2: A5-F03, A5-M03, A5-M04, A5-C01; logs at end)
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
| Core Operating PBT (PBT - OI) | 2.62 | 8.55 | +226.4% | Off a trough base. H1 +57.7% and TTM +22.4% carry the same Rs 7.47 cr gain, 79% of it from Q2; trough-free Q1 YoY +14.9%; Q2 FY27 level is below the H2 FY26 quarterly average (10.21) | [d] |
| Reported PBT | 6.89 | 10.44 | +51.5% | Understates YoY core growth | res L168 |
| PAT | 5.35 | 7.83 | +46.4% | Understates YoY core growth | res L174 |
| EPS (share-adjusted, Rs) | 9.28 | 13.58 | +46.3% | Same as PAT | res L185 |

H1 YoY (H1 FY27 vs H1 FY26) for context: revenue +33.2% (100.81 to 134.32); operating EBITDA +42.6% (17.53 to 24.99); margin +122 bps (17.39% to 18.61%); OI -22.0% (12.36 to 9.65); core PBT +57.7% (12.94 to 20.41); PBT +18.8% (25.31 to 30.06); PAT +17.0% (19.83 to 23.21); EPS +17.0% (34.38 to 40.24). TTM core PBT Rs 40.82 cr vs FY26 Rs 33.35 cr = +22.4%. TTM less FY26 equals H1 FY27 less H1 FY26, so the TTM gain (Rs 7.47 cr) is the H1 gain, and Rs 5.93 cr of it (79%) is the Q2 recovery. Trough-free Q1 FY27 vs Q1 FY26 core PBT: +14.9% (10.32 to 11.86). All [d] from res L154-L185.

Mandatory diagnostic answers:
1. Did revenue grow YoY? Yes. Q2 FY27 revenue of Rs 56.80 cr vs Q2 FY26 Rs 33.24 cr = +70.9% YoY. There is no company annual guidance in the filings and no Notion base case, so the comparison to guidance and to base is ND.
2. Margin YoY? Expanded. Q2 FY27 operating EBITDA margin 18.92% vs Q2 FY26 15.71% = +321 bps. The gain does not come from fixed-cost leverage. Filing-basis gross margin fell 1,187 bps (71.75% to 59.88%). Employee cost fell from 17.90% to 9.76% of revenue (+814 bps to margin) and manufacturing expense from 6.49% to 3.34% (+314 bps). Those fixed-cost lines only offset the gross-margin fall: net -59 bps. Without the distributor plus other line, Q2 FY27 operating EBITDA margin would be about 15.11%, below Q2 FY26's 15.71% [d]. The whole +321 bps rests on distributor comp plus other expenses falling from 31.66% to 27.86% of revenue (+380 bps). Inside that line, Other Expenses rose 92.3% in rupees (6.58 to 12.66) against revenue +70.9%, and Compensation to Distributors fell 19.6% in rupees (3.94 to 3.17) [d, res L154, L158-166]. The line is unexplained (FN11). Note 4 (res L193) leans against a reclassification reading (Step 0D). The YoY gross-margin fall is measured from the Q2 FY26 outlier; the sequential series is in Step 3.
3. Core operating PBT YoY? Grew. Rs 2.62 cr to Rs 8.55 cr = +226.4%. This is off a trough base: Q2 FY26 revenue had fallen 50.8% QoQ. In level terms Q2 FY27 core PBT sits below Q1 FY26 (Rs 10.32 cr), the H2 FY26 quarterly average (Rs 10.21 cr) and Q1 FY27 (Rs 11.86 cr). H1 (+57.7%) and TTM (+22.4%) are not trough-free bases (A5-M03). The TTM core-PBT gain of Rs 7.47 cr equals the H1 gain, and Rs 5.93 cr of it (79%) is the Q2 recovery off the Q2 FY26 trough [d]. The trough-free comparison, Q1 FY27 vs Q1 FY26, is +14.9% (10.32 to 11.86) [d]. TTM EPS of Rs 72.97 is 14.4% below FY25's Rs 85.25 [MGMT, pres L715]. TTM core PBT of Rs 40.82 cr is below FY25's about Rs 48 cr (PBT 66 less OI 18, deck rounded) [MGMT, pres L705, L710]. Profit has not yet recovered the FY25 level. The distributor-rate drop alone is worth Rs 3.57 cr: at the Q2 FY26 rate of 11.85%, Q2 FY27 distributor comp would be Rs 6.73 cr, not the filed Rs 3.17 cr. That is 60% of the Rs 5.93 cr YoY core-PBT gain [d, res L154, L165]. Headline PAT growth (+46.4%) understates YoY core growth, but the core gain itself rests heavily on one unexplained line.
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

Sequential gross margin and spares share (A5-C01) [d, res L154, L158-160; spares share under the A3-14 chart reading, spares = upper segment, res L364-367]:
| Period | Gross margin (filing basis) | Spares share of revenue (chart, A3-14 reading) | Anchor |
|---|---|---|---|
| Q1 FY26 [d: H1 FY26 - Q2 FY26] | 58.25% | 21% | [d] res L154, L158-160, L364-367 |
| Q2 FY26 | 71.75% | 48% | [d] res L154, L158-160, L364-366 |
| H2 FY26 [d: FY26 - H1 FY26] | 52.81% | ND (no H2 chart) | [d] res L154, L158-160 |
| FY26 | 57.13% | ND (no FY chart) | [d] res L154, L158-160 |
| Q1 FY27 [d: H1 FY27 - Q2 FY27] | 54.14% | 18% | [d] res L154, L158-160, L364-367 |
| Q2 FY27 | 59.88% | 35% | [d] res L154, L158-160, L364-366 |

Q2 FY27 gross margin is above every period on file except the Q2 FY26 outlier. In the four quarters with a chart split, gross margin ranks in the same order as the spares share (Q2 FY26 > Q2 FY27 > Q1 FY26 > Q1 FY27). The filed series shows a mix effect. It shows no price erosion. The chart segment labels are unmapped (A3-14), so Q10 and Q11 confirm or break this reading.

Diagnostics:
- Trajectory: Recovering YoY, dipping QoQ. Q2 was below Q1 in both years on file (33.24 < 67.57; 56.80 < 77.52), and H2 was 56.3% of FY26 revenue (one H2 observed; FN15). Read as seasonal and dispatch-lumpy, not as a step-up.
- One-off distortion: Q2 FY26 is the distorted base (weak quarter, gross margin 71.75%, outlier vs every other period; FN12). Sequentially Q2 FY27 gross margin rose to 59.88% from 54.14% in Q1 FY27 (table above). Q1 FY27 PAT carries a Rs 0.94 cr deferred-tax credit. No exceptional items anywhere.
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
| CFO (H1) | 6.04 (H1 FY26); 22.11 (FY26) | 1.84 (H1 FY27) | -69.6% vs H1 FY26 | Weak; positive only because of a Rs 7.14 cr other-financial-liabilities inflow (next row but one) | res L300 |
| CFO / PAT | 0.30x (H1 FY26); 0.57x (FY26) | 0.08x (H1 FY27) | -0.23x vs H1 FY26 | Below every Pillar 2 band (floor 0.65x) | [d] res L174, L300 |
| CFO excluding the other-financial-liabilities inflow (A5-M04) | 6.04 (H1 FY26; line 0.01); 22.02 (FY26; line 0.09) | (5.30) (H1 FY27; line 7.14) | ND | Negative. Reported H1 CFO rests on one line; (0.23)x of H1 PAT on this basis | [d] res L174, L294, L300 |
| Capex (PPE + CWIP payments) | ND (H1 FY26 column row-misaligned, FN20); 60.55 (FY26) | 2.11 (H1 FY27) | ND | Low cash capex in H1; the FY26 advance was capitalised (FN09) | res L303 |
| FCF (CFO - capex) | ND (H1 FY26); (38.44) (FY26) | (0.28) (H1 FY27) | ND | Negative; Rs (7.42) cr without the other-financial-liabilities inflow [d] | [d] res L294, L300, L303 |
| Working capital change (CF) | (6.08) (H1 FY26); (11.31) (FY26) | (15.76) (H1 FY27) | -9.68 vs H1 FY26 | Absorbing, even after Rs 8.61 cr from trade payables and Rs 7.14 cr from other financial liabilities | [d] res L288-294 |
| Receivable days (period-end receivables / annualised revenue x 365) | 114.7 (Mar-26, on FY26 revenue) | 123.9 (Sep-26, on H1 x 2) | +9.2 days | Stretching | [d] res L154, L217 |
| Inventory days (on COGS: materials + purchases + inventory change) | 400.4 (Mar-26) | 361.2 (Sep-26, H1 x 2) | -39.2 days | High; improves on a larger H1 COGS base | [d] res L158-160, L214 |
| Payable days (on same COGS) | 65.1 (Mar-26) | 81.2 (Sep-26) | +16.1 days | Lengthening; trade payables added Rs 8.61 cr to H1 CFO (res L292), so this props up reported cash | [d] res L252-257 |
| Cash Conversion Cycle | 450.0 (Mar-26) | 403.9 (Sep-26) | -46.1 days | Very long; H1-annualised basis is seasonal, read direction with care | [d] |
| PPE | 64.11 (Mar-26) | 111.55 (Sep-26) | +47.44 (+74.0%) | Large unexplained addition | res L204 |
| CWIP | 1.57 (Mar-26) | 0.45 (Sep-26) | -1.12 | Capitalised | res L205 |
| Other non-current assets | 48.25 (Mar-26; A2 Z5 correction) | ND (blank, Sep-26) | -48.25 | Emptied into PPE (FN01, FN09, A3-01) | res L211 |
| Net debt / (net cash) excluding investments | 3.55 net debt (Mar-26) | 5.75 net debt (Sep-26) | +2.20 | Small, rising | [d] res L218-219, L235, L243-244 |
| Liquid net cash / (net debt): current investments + cash + bank - borrowings | 11.86 net cash (Mar-26) | (1.53) net debt (Sep-26) | -13.39 | Liquid treasury turned to net borrowing in H1 (A5-M02). Excludes lease liabilities (Rs 1.56 cr Mar-26; Rs 1.41 cr Sep-26), which the two net-debt rows include; with leases Sep-26 is Rs (2.93) cr [d] | [d] res L216, L218, L219, L235, L243, L244 |
| Net debt / (net cash) including all investments | (200.98) net cash (Mar-26) | (207.03) net cash (Sep-26) | +6.05 net cash | Book is 98.7% non-current, composition undisclosed; the +6.05 rise is below the 7.21 FV and sale gains, so ex-MTM net cash fell about 1.17 | [d] res L209, L216, L218-219, L235, L243-244, L278 |
| Promoter pledge | ND | ND | ND | Not in filings | ND |

Supporting stock items (Rs cr): trade receivables 72.49 (Mar-26) to 91.18 (Sep-26), +18.70 (+25.8%) (res L217); inventories 108.52 to 115.48, +6.96 (+6.4%) (res L214); borrowings 2.79 to 5.75 (res L243); current investments 13.86 to 2.81 (-79.7%) (res L216); non-current investments 190.68 to 209.96 (res L209); total investments 204.54 to 212.78 (37.95% of total assets of 560.61; 98.7% non-current) (res L209, L216, L224); trade payables 17.63 to 25.95 (res L252-257); other current financial liabilities 5.27 to 11.10 (+110%) (res L260); other non-current financial liabilities nil to 0.28 (res L236); other current liabilities 14.21 to 11.69 (-17.7%) (res L261); total equity 467.51 to 488.41 (res L231).

H1 cash funding [d]: CFO Rs 1.84 cr did not cover capex of Rs 2.11 cr (res L300, L303). The Rs 2.32 cr dividend paid (res L319) was in effect funded by Rs 2.87 cr of new borrowing (res L315), not by drawing the treasury.

CFO dependency (A5-M04) [d]: H1 CFO of Rs 1.84 cr includes a Rs 7.14 cr operating inflow from other financial liabilities (res L294). The same line gave Rs 0.09 cr in all of FY26 and Rs 0.01 cr in H1 FY26 (res L294). Without that line H1 CFO is Rs (5.30) cr and H1 FCF is Rs (7.42) cr. Trade payables added a further Rs 8.61 cr (res L292). The balance-sheet rise in other financial liabilities is Rs 6.11 cr: current 5.27 to 11.10 (res L260) plus non-current nil to 0.28 (res L236). The filing does not reconcile that rise to the Rs 7.14 cr cash-flow line. If capital creditors for the H1 asset sit inside this operating line, reported CFO is overstated and cash capex understated by up to that amount [INFERENCE]. Q18 asks for the split.

Deck working-capital days (TTM basis, formula undisclosed): 232 (FY26) to 219 (H1 FY27) (pres L376-377, L382). In rupees working capital absorbed Rs 15.76 cr in H1, and receivable days stretched. The deck's improvement comes from a larger TTM revenue denominator (A3-11). The deck key ratios do not tie to its own balance sheet (current ratio 3.8 shown vs 3.53 period-end; NFAT 2.8 vs 2.22; A3-12). This review uses period-end balance-sheet values, never the slide 17 ratios.

Multi-year conversion (deck, rounded): FY23-FY26 cumulative OCF Rs 74 cr vs PAT Rs 149 cr = 0.50x (pres L762, L713).

Mandatory answers:
- Is CFO/PAT meeting the Pillar 2 cash multiplier assumption? No Notion assumption exists (ND). On the filed numbers, H1 FY27 0.08x, FY26 0.57x and FY23-FY26 0.50x all sit below the lowest band of 0.65x. Reported H1 CFO itself rests on the Rs 7.14 cr other-financial-liabilities inflow; without it H1 CFO is Rs (5.30) cr. Pillar-relevant fact flagged for /fttcp and Role 1.
- Is the WC drag structural or growth-induced? Test: "If the company stopped growing tomorrow, would WC days still be high?" FY26 revenue fell 6.6% (247 to 231, pres L697) and CFO/PAT was still 0.57x. Inventory sits at about a year of COGS at both dates. That leans structural. H1 is seasonally the weak cash half, and no rating-agency commentary is in the files. Classification: INDETERMINATE-WITH-DIRECTION (lean structural). Missing evidence that would resolve it: receivable ageing and state-owned vs private customer payment terms; the capital-creditor share of the Rs 7.14 cr other-financial-liabilities inflow; FY27 full-year CFO (Q4 FY27 filing); any CARE/ICRA/CRISIL WC assessment (none in files). Per house rule this caps the verdict at PROCEED WITH CAVEATS or below.
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
| CIL subsidiary payment behaviour (ECL, MCL, SECL, WCL in customer roster; 8 of 16 roster names are state-owned) | Customer liquidity | Quarterly | pres L515-532 | Receivable days (FN10, A3-11) |

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
- TTM to Sep-26 [d, FY26 - H1 FY26 + H1 FY27]: revenue Rs 264.26 cr; operating EBITDA Rs 50.43 cr (19.08%); Other Income Rs 14.29 cr; core PBT Rs 40.82 cr (+22.4% vs FY26); PAT Rs 42.09 cr; EPS Rs 72.97. Base qualifier (A5-M03): TTM is not a trough-free base. The TTM core-PBT gain of Rs 7.47 cr equals the H1 gain, and Rs 5.93 cr of it (79%) is the Q2 recovery off the Q2 FY26 trough [d]. The trough-free comparison, Q1 FY27 vs Q1 FY26, is +14.9% [d]. Against FY25 (deck, rounded): TTM EPS Rs 72.97 is 14.4% below Rs 85.25 (pres L715); TTM core PBT Rs 40.82 cr is below about Rs 48 cr (PBT 66 less OI 18, pres L705, L710); TTM operating EBITDA margin 19.08% is below 22.7% (pres L704); TTM revenue is 7.0% above Rs 247 cr (pres L697) [d]. Profit has not yet recovered the FY25 level.
- Known one-offs to adjust: Q1 FY27 deferred-tax credit Rs 0.94 cr; H1 FV gains Rs 7.21 cr on investments (non-operating, largely MTM); FY26 earlier-period tax credit Rs 0.11 cr. The Q2 margin rests on the unexplained distributor plus other line (FN11); do not fold it into the base until answered.
- Treasury: investments Rs 212.78 cr; net cash including investments Rs 207.03 cr = Rs 358.9 per share [d, 57.684 lakh shares]. LIQUIDITY QUALIFIER (A5-M02): this per-share figure is not a liquid figure. 98.7% of the book (Rs 209.96 cr) is non-current with undisclosed composition. Liquid net cash is Rs (1.53) cr at Sep-26, down from Rs 11.86 cr at Mar-26. The H1 rise in net cash (Rs 6.05 cr) is less than the H1 FV gains (Rs 7.21 cr). Any treasury credit at /fttcp or Role 1 must first establish the book's liquidity and composition (Q14, Q16). Book value per share Rs 846.7 [d, res L231].

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

Deferred to /fttcp and Role 1 (operator ruling OR-30). No Section 1B or FTTCP authority is loaded in this stage. Pillar-relevant facts, each flagged:

| Pillar / Input | Original Assumption | Current Reading (pillar-relevant fact) | Action |
|---|---|---|---|
| ROCE base (Pillar 1) | ND | Deck ROCE 11.7% H1 FY27 TTM, 10.7% FY26; ROE 9.0% / 8.3% (pres L361-366); formula undisclosed and slide 17 ratios do not tie (A3-12). Investments are 37.95% of total assets, which depresses reported ROCE. | Deferred to /fttcp (FTTCP verdict sole authority). Compute operating ROCE ex-treasury there. |
| Cash multiplier (Pillar 2) | ND | CFO/PAT 0.08x H1 FY27, 0.57x FY26, 0.50x FY23-FY26 (res L300; pres L762, L713). Below the 0.65x floor band. Without the Rs 7.14 cr other-financial-liabilities inflow, H1 CFO is Rs (5.30) cr (res L294) [d]. | Deferred to Role 1. FLAG. |
| Growth visibility premium | ND | Order book Rs 133 cr = 0.50x TTM revenue (res L374; [d]); definition unresolved (order book vs "open order pipeline", FN19, PR/F16-2). | Deferred. Do not credit until the definition is answered. |
| Strategic premium | ND | No moat evidence in filings; product launches carry no orders or revenue (A3-05). | Deferred. |
| UA multiplier | ND | Shareholding and institutional ownership not in the filings. | Deferred (ND). |
| Sector cap | ND | Capital goods / mining equipment; single segment Machinery and Spares (res L191). | Deferred. |
| Hurdle ratio recheck | ND | No CMP and no EPS CAGR baseline in inputs. TTM EPS Rs 72.97 [d], 14.4% below FY25 EPS Rs 85.25 (pres L715). | Deferred (ND). |

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
- New information on execution quality for any future thesis: fixed-cost leverage only offset the gross-margin fall (net -59 bps); the whole +321 bps margin gain rests on the unexplained distributor plus other line. Cash conversion is the binding weakness, and reported H1 CFO rests on one Rs 7.14 cr liability inflow. The liquid treasury turned to net debt. The Rs 47 cr asset is undisclosed.

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
| 2 | D | What share of the Rs 91.18 cr receivables, and of H1 revenue, is due from state-owned customers (Coal India subsidiaries, Singareni, MOIL, Hutti Gold, UCIL) vs private customers, and what are the contracted payment days for each group? | The customer slide lists 8 state-owned and 8 private names with no revenue or receivable share (pres L515-532). Tests whether WC is structural (state-payer terms) or timing. | Short contracted days with a dated collection plan. | Long state-payer terms on a dominant receivable share, which make the drag structural. | FN10, A3-11 |
| 3 | A | Compensation to Distributors fell to Rs 3.17 cr (5.6% of revenue) in Q2 from Rs 8.71 cr (11.2%) in Q1, while Other Expenses rose to Rs 12.66 cr (22.3%) from Rs 11.39 cr. Was any amount reclassified between these two lines in Q2: yes or no, and how many Rs cr? | The whole +321 bps YoY margin gain rests on this line group; at the Q1 distributor rate, Q2 EBITDA margin would be 13.3%, not 18.9%. Note 4 (res L193) says comparatives were regrouped to be comparable, yet Q1 FY27 and Q2 FY26 still show 11.2% and 11.9%, which leans against a Q2 reclass. | A dated shift to direct (non-distributor) sales, with the Rs cr named; or a stated reclass with restated comparatives. | No reclassification and no channel change: the Q2 margin rests on a line that reverts. | FN11, FN04, A3-04, PR/F6-1 |
| 4 | F | PPE rose from Rs 64.11 cr to Rs 111.55 cr in H1 while other non-current assets of Rs 48.25 cr went to nil and H1 cash capex was Rs 2.11 cr. What asset was capitalised (land, building or plant), for how many Rs cr, and on what date? | A Rs 47 cr asset is 74% of the prior PPE base, with no note. | Land, or plant with a named capacity and a dated revenue ramp. | Plant capitalised late in Q2 with no capacity disclosure. | FN09, A3-01, PR/F6-3 |
| 5 | F | What annual depreciation charge does the asset capitalised in H1 FY27 add, in Rs cr? | Q2 D&A fell to Rs 2.07 cr; a step-up hits core PBT from Q3. | Nil (land) or small. | A step-up that offsets the H2 order-book margin. | FN09, A3-01 |
| 6 | E | Of the Rs 133 cr reported as order book at 30 Sep 2026, how many Rs cr are signed purchase orders not yet executed, net of GST? | The release calls the same Rs 133 cr an "open order pipeline"; a pipeline can include bids. | All Rs 133 cr firm, net of GST. | A part is bids or enquiries, or the figure is gross of GST. | FN19, FN05, A3-15, PR/F16-2, PR/F6-2 |
| 7 | E | What was the order book at 31 Mar 2026 and at 30 Jun 2026, in Rs cr, on the same definition? | Only Sep-25 (Rs 44 cr) is given; H1 inflow and book-to-bill cannot be computed. | A rising sequential book with H1 inflow above H1 revenue of Rs 134 cr. | A flat or falling sequential book. | FN05, A3-15, PR/F6-2 |
| 8 | G | Who is the successor or interim CFO, and on what date will that person take office? | The CFO leaves on 30 Oct 2026; Q3 FY27 close and limited review will be the first without him. | A named appointee before 30 Oct 2026. | No appointee by the Q3 board meeting. | FN16 |
| 9 | G | On what date did the company receive Mr. Begwani's letter dated 5 Sep 2026, and was an earlier Reg 30 intimation filed: yes or no? | The exchange disclosure came 38 days after the letter date. | Received close to 13 Oct, or an earlier intimation exists. | Received early September with no earlier disclosure. | FN17 |
| 10 | C | What were product revenue and spares revenue in Rs cr for Q2 FY26, Q1 FY27 and Q2 FY27, and which chart segment is spares? | Gross margin tracks the unlabelled chart segment in every period; mix drives margin. | Spares share stable or rising. | Equipment-heavy growth with spares share falling (35% Q2 FY27 vs 48% Q2 FY26 under one reading). | FN12, A3-14, PR/F12-1 |
| 11 | C | Filing-basis gross margin fell from 71.75% in Q2 FY26 to 59.88% in Q2 FY27. How many bps of that fall is product mix, and how many is price? | The gross-margin fall (-1,187 bps) was larger than the fixed-cost recovery (+1,128 bps). Sequentially Q2 FY27 gross margin is above Q1 FY27 (54.14%), and margin ranks with the spares share, which points to mix (Step 3). This question tests that reading. | Mostly mix, with stable equipment pricing. | Price erosion on equipment orders. | A3-13, FN12 |
| 12 | A | Q2 built Rs 11.50 cr of finished goods and WIP while revenue fell 26.7% QoQ. What share of the Sep-26 inventory of Rs 115.48 cr is against orders scheduled to ship in Q3 FY27? | Inventory sits at about a year of COGS. | Most of the build ships in Q3. | Slow-moving stock with no dispatch date. | FN12 |
| 13 | A | Q2 FY27 revenue of Rs 56.80 cr was 26.7% below Q1 FY27 (Rs 77.52 cr). Did any order planned for Q2 slip to H2: yes or no, and for how many Rs cr? | The release says "sustained momentum" but shows YoY only. | No slippage; seasonal dispatch pattern. | A named slippage. | PR/F16-1, A3-13, FN18 |
| 14 | F | Borrowings rose from Rs 2.79 cr to Rs 5.75 cr while investments stood at Rs 212.78 cr and current investments fell to Rs 2.81 cr. What is the facility type and interest rate? | Liquid net cash moved from Rs 11.86 cr to Rs (1.53) cr; the H1 dividend was in effect funded by borrowing. | A cheap working-capital line kept for banking relations. | A liquidity need the treasury book cannot meet (illiquid or locked investments). | FN02, A3-02 |
| 15 | C | Q1 FY27 carried a deferred-tax credit of Rs 0.94 cr and DTL fell from Rs 7.70 cr to Rs 6.76 cr. Which temporary difference reversed? | Ex-deferred H1 ETR is 25.91%; the credit may not recur. | A named one-time item, with FY27 ETR guided near 25%. | No explanation. | FN07, A3-08 |
| 16 | D | Of H1 Other Income of Rs 9.65 cr, Rs 7.21 cr is fair-value and sale gains. What share of the Rs 209.96 cr non-current investment book is equity or equity funds? | OI is 32.1% of H1 PBT and mostly MTM; the book is 98.7% non-current. | Mostly debt instruments with stable accrual and short redemption terms. | Mostly equity or locked instruments, so PBT carries market risk and the book is not liquid. | A3-16 |
| 17 | F | The reserve roll implies an FY26 dividend of Rs 4.00 per share vs Rs 5.00 for FY25. Confirm the FY26 DPS, and was the cut made to fund the Rs 60.55 cr FY26 capex: yes or no? | Capital allocation signal. | Yes, a one-time capex funding decision. | A cut with no stated reason. | FN08 |
| 18 | D | Other current financial liabilities rose from Rs 5.27 cr to Rs 11.10 cr, and the H1 cash-flow statement books a Rs 7.14 cr operating inflow from other financial liabilities (Rs 0.09 cr in all of FY26). How many Rs cr of that inflow are capital creditors, and on what date will the balance be settled? | H1 CFO is Rs 1.84 cr with the line and Rs (5.30) cr without it. Capital creditors carried inside operating cash flow would overstate CFO and understate cash capex. | Operating accruals with a dated settlement, and H1 CFO stated without them. | Capital creditors carried inside operating cash flow, or dues that unwind in H2. | FN14 |
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
| M8 | Q4 FY27 / FY27 audited results with H2 cash flow: full-year CFO/PAT | by 2027-05-30 (LODR Reg 33, 60 days after 31 Mar 2027) | res L294, L300 (FN10, A3-11) | Bull at or above 0.80x; bear below 0.57x; CFO with and without the other-financial-liabilities line |
| M9 | FY27 annual report: tax note (DTL reversal), PPE schedule (asset class of the Rs 47 cr addition), actuarial OCI, related parties, investment composition | AGM date ND | FN06, FN07, FN09, A3-16, Z2-Z4 | Verify each at the Role 6 deep dive |
| M10 | Borrowings, liquid net cash and new non-current liability lines (Rs 0.28 cr and Rs 0.09 cr) | Mar-27 balance sheet | res L216-219, L236-237, L243 (FN02, FN03) | Size and nature; liquid net cash back above zero or not |
| M11 | Exceptional line in the deck template | Each quarter | pres L401 (A3-03) | Any non-zero entry |
| M12 | New products CM-3500, MUV, MCAR-E commercial data | Next deck (with Q3 FY27 results, by 2027-02-14) | pres L487, L182-186 (A3-05) | Orders or units disclosed |
| M13 | Piling-rig leads after Bauma ConExpo India (15-18 Sep 2026, held) | Next deck | pres L539-544 (A3-07) | Orders disclosed |
| M14 | FY27 dividend per share vs implied FY26 Rs 4.00 | FY27 board outcome (with Q4 results) | res L319, L230 (FN08) | DPS and reason |

---

## VERDICT

Protocol verdict: **PROCEED WITH FLAGS**. The filed numbers are clean: unmodified limited review, all column totals tie (two cell positions need the data corrections listed under the preamble), no exceptional items, standalone-only filer. Core PBT grew 226% YoY, but off a trough base. H1 and TTM carry the same Rs 7.47 cr gain, 79% of it the Q2 recovery; the trough-free Q1 YoY is +14.9%. TTM EPS of Rs 72.97 is 14.4% below FY25's Rs 85.25 (pres L715), so profit has not recovered the FY25 level. Q2's Rs 8.55 cr sits below the H2 FY26 quarterly average of Rs 10.21 cr. 60% of the YoY gain equals the unexplained distributor-rate drop. Four items need to be surfaced, and cash conversion caps the verdict below PROCEED in any case:
1. Cash conversion INDETERMINATE-WITH-DIRECTION (lean structural): H1 CFO/PAT 0.08x; FY23-FY26 0.50x. H1 CFO is Rs (5.30) cr without a Rs 7.14 cr other-financial-liabilities inflow (res L294). Missing evidence named in Step 5.
2. Governance: CFO exits 30 Oct 2026 with no successor named, after a 38-day letter-to-disclosure gap. Mitigant: ED Kamlesh Shah signs the statements (res L337-339) and is an ICAI fellow with about 27 years in financial operations and treasury (pres L212-217). That gives continuity. It does not address the 38-day gap or the missing successor.
3. Disclosure gaps that move the margin read: an unnamed Rs 47.44 cr capitalisation, and the distributor plus other line, which carries the whole +321 bps margin gain. Note 4's regrouped comparatives lean against the reclass reading.
4. Treasury liquidity: liquid net cash moved from Rs 11.86 cr to Rs (1.53) cr in H1; the Rs 212.78 cr book is 98.7% non-current with undisclosed composition.

The Loop 1 and Loop 2 fixes strengthen the flags. They raise no mechanical failure and no REWORK trigger, so the verdict stands.

Standalone vs consolidated gap (A3 F2): N.A. in every period. Note 3 (res L192) states no subsidiary, associate or JV. No consolidated statement exists.

---

## PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (results filing), MGMT (company deck or release statements), SECONDARY (third-party data the deck cites), INFERENCE (this review's reading). Every figure below comes from this quarter's filings or deck. No prior Notion or peer work exists for this name.

### 1. Summary narrative
Eimco Elecon sold Rs 56.80 cr in Q2 FY27, up 70.9% from Rs 33.24 cr a year ago [FILED].
The base was weak. Q2 FY26 revenue had fallen 50.8% from the quarter before it [FILED, derived].
Against Q1 FY27, revenue fell 26.7% [FILED]. Q2 was below Q1 in both years, and H2 was 56.3% of FY26 revenue [FILED, derived]. Only one H2 is on file.
Core profit before tax, after taking out other income, rose from Rs 2.62 cr to Rs 8.55 cr [FILED, derived]. That growth is off a trough base.
The twelve-month gain of Rs 7.47 cr equals the first-half gain, and 79% of it is the Q2 rebound [FILED, derived].
Q1 against Q1, free of the trough, core profit grew 14.9% [FILED, derived]. Twelve-month EPS of Rs 72.97 is still 14.4% below FY25's Rs 85.25 [MGMT, pres L715].
Q2's Rs 8.55 cr is below last year's H2 quarterly average of Rs 10.21 cr [FILED, derived].
Reported profit after tax rose 46.4% to Rs 7.83 cr, because treasury income fell [FILED].
Operating margin rose to 18.9% from 15.7% [FILED, derived]. Gross margin fell from 71.8% to 59.9% [FILED, derived]. Against Q1 FY27, gross margin rose from 54.1% [FILED, derived].
Lower staff and factory costs per rupee of sales only made up for the lower gross margin [FILED, derived]. The whole margin rise came from one cost group, distributor payments plus other expenses [FILED, derived].
Inside that group, distributor payments fell while sales rose 71%, and other expenses rose 92% [FILED]. Until the company explains this, the 18.9% margin is not proven [INFERENCE].
Cash is the weak point. The first half produced Rs 1.84 cr of operating cash against Rs 23.21 cr of profit [FILED]. Without a Rs 7.14 cr rise in other financial liabilities, operating cash was Rs 5.30 cr negative [FILED, derived].
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
Payer mix: the customer slide shows 16 names, 8 state-owned (four Coal India subsidiaries, Singareni, MOIL, Hutti Gold, UCIL) and 8 private (mining contractors and Tata Steel) [MGMT, pres L515-532]. The deck cites demand from both public and private customers [MGMT, pres L356]. A logo count gives no revenue or receivable share; Q2 asks for it. If state payers dominate receivables, slow payment would fit the cash picture [INFERENCE].

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
Where it looks weaker: small scale (TTM revenue Rs 264.26 cr) [FILED, derived], an undisclosed customer mix, and slow cash collection [FILED].
Competitive risk to watch: gross margin on new equipment orders. YoY gross margin fell from 71.8% to 59.9%, but Q2 FY26 is the outlier base [FILED, derived]. Sequentially, Q2 FY27's 59.88% is above Q1 FY27 (54.14%), Q1 FY26 (58.25%), H2 FY26 (52.81%) and FY26 (57.13%) [FILED, derived]. In four quarters, gross margin ranks in the same order as the spares share (48%, 35%, 21%, 18%) under the A3-14 chart reading [INFERENCE]. The filed series shows mix, not price erosion. Tender pricing would show as a margin fall at a stable spares share. Question 11 is the test.

### 5. Forward map (next ~10-11 months)
Make-or-break reading: Q3 FY27 core profit before tax, in the Q3 results due by 14 Feb 2027. Bull at or above Rs 10.21 cr. Bear below Rs 8.55 cr.
- 30 Oct 2026, CFO exit. Bull: a named successor before the date. Bear: no appointee by the Q3 board meeting.
- By 14 Feb 2027, Q3 FY27 results. Bull: core PBT at or above Rs 10.21 cr with D&A and distributor comp explained. Bear: core PBT below Rs 8.55 cr, or a D&A step-up that eats the margin.
- Every quarter, margin band 18-20%. Bull: operating EBITDA margin holds inside the band with the distributor line explained. Bear: the distributor line reverts and margin falls toward 13%.
- H2 FY27, Rs 133 cr order book. Bull: a firm, net-of-GST book that grows sequentially. Bear: the figure turns out to include bids, or the sequential book falls.
- Next deck (with Q3 results), new products and piling rigs. Bull: named orders for CM-3500, MUV, MCAR-E or piling rigs. Bear: no commercial data again.
- By 30 Apr 2027, statutory CFO window [statute, not in filing; PENDING LIVE VERIFICATION; a shorter listing-regulation timeline may apply]. Bull: a permanent CFO in office. Bear: the vacancy is still open.
- By 30 May 2027, FY27 results with full-year cash flow. Bull: CFO/PAT at or above 0.80x and liquid net cash back above zero. Bear: CFO/PAT below 0.57x, or CFO that again rests on the other-financial-liabilities line, which confirms the structural reading.

---

## LOOP 1 CHANGES (A5 audit, work/audit_eimcoeleco_q2fy27.md)

All figures were rechecked against the A1 results fulltext (res L154-174, L193, L209-243, L278, L300-319) before writing.
- A5-F01 (FACTUAL): the summary line "Q1-high, Q2-low, H2-heavy pattern in both years [FILED]" is replaced with "Q2 was below Q1 in both years, and H2 was 56.3% of FY26 revenue [FILED, derived]. Only one H2 is on file." The same fix is applied to the Step 3 trajectory diagnostic and the Step 6.5 seasonality bullet.
- A5-F02 (FACTUAL): the "fixed-cost leverage" attribution is removed from Step 2 (table and diagnostic 2), the Step 4 margin rows (now UNRESOLVED), 8B, Q11, the summary and analyst_note. New reading: gross margin -1,187 bps, employee +814, manufacturing +314, net -59 bps. The whole +321 bps rests on the distributor plus other line (+380 bps). Other Expenses +92.3% and distributor comp -19.6% in rupees. Without that line, the margin would be about 15.11%. The Note 4 regrouping point (res L193) is added to Step 0D, Q3 (why, bull answer), the verdict and flag 5. The Q3 bull answer no longer treats a reclass as the likely good outcome.
- A5-M01 (MISSING): the base-effect qualifier is added to the verdict, the Step 2 table and diagnostic 3, the Step 4 recurring answer, 8C and the summary. It covers: TTM core PBT +22.4% (40.82 vs 33.35), H1 +57.7%, the Q2 level Rs 8.55 cr below the H2 FY26 quarterly average of Rs 10.21 cr and Q1 FY26 Rs 10.32 cr, and the distributor-rate drop of Rs 3.57 cr = 60% of the Rs 5.93 cr YoY gain.
- A5-M02 (MISSING): treasury liquidity is added to Step 5, both in a new liquid net cash row (11.86 to (1.53)) and in the qualified all-investments row (98.7% non-current; the +6.05 rise is below the 7.21 FV gains). Step 5 also gains the H1 cash funding line (CFO 1.84 < capex 2.11; dividend 2.32 in effect funded by 2.87 of new borrowing) and a rewritten net-debt answer. The qualifier is attached to the Rs 358.9 per share figure in Step 6.5. Q14, Q16, M10, the business-model brief, the summary and a new verdict item 4 are updated.
- Style applied at no extra cost: S01 (sector anchor pres L428-434 corrected to res L428-434); S04 (25.17% marked [statute, not in filing; tax-regime election NOT FOUND]); S05 (Q2 FY26 -50.8% tagged [FILED, derived]).
- Verdict unchanged: PROCEED WITH FLAGS. Flags were added and sharpened; no REWORK or INSUFFICIENT EVIDENCE trigger arises.

## LOOP 2 CHANGES (A5 re-audit, work/audit_eimcoeleco_q2fy27.md)

Every new figure was checked against the A1 fulltexts before writing: res L154-174 (P&L, lakhs), L236, L260, L292-300 (BS and CF), L337-339 (ED signature), L364-367 (chart split); pres L212-217 (ED profile), L356, L515-532 (customer slide), L697-715 (FY25 history). Lakh-level arithmetic: Q1 FY26 gross margin 3,935.87 / 6,756.99 = 58.25%; H2 FY26 6,862.36 / 12,994.02 = 52.81%; Q1 FY27 core PBT 1,185.91 vs Q1 FY26 1,032.14 = +14.9%; CFO 183.78 - 713.83 = (530.05); FCF (530.05) - 211.48 = (741.53); liquid net cash with leases (152.54) - 140.53 = (293.07).
- A5-F03 (FACTUAL): the sector-brief payer-mix line now states the roster as 16 names, 8 state-owned and 8 private (pres L515-532), cites the deck's "both public-sector and private-sector customers" (pres L356), and makes the slow-payer reading conditional on a receivable share that Q2 now asks for. The competition brief replaces "dependence on state-owned buyers" with "an undisclosed customer mix". Q2 (question, why, bear), the Step 5 missing-evidence list and the 5.5C candidate-signal anchor (pres L513 to L515-532) are aligned.
- A5-M03 (MISSING): every place that called H1 or TTM a less distorted base now carries the qualifier: Step 2 table and H1 context line, diagnostic 3, Step 6.5 TTM bullet, Step 7 hurdle row, the verdict, the summary, flag 6 and analyst_note. The qualifier: the TTM core-PBT gain of Rs 7.47 cr equals the H1 gain, and Rs 5.93 cr (79%) is the Q2 recovery; trough-free Q1 YoY +14.9%; TTM EPS Rs 72.97 is 14.4% below FY25 Rs 85.25 (pres L715); TTM core PBT Rs 40.82 cr is below FY25 about Rs 48 cr (pres L705, L710); TTM margin 19.08% vs FY25 22.7% (pres L704); TTM revenue +7.0% vs FY25 Rs 247 cr (pres L697). The Loop 1 log above is left as a record.
- A5-M04 (MISSING): Step 5 gains a "CFO excluding the other-financial-liabilities inflow" row ((5.30) H1 FY27; 6.04 H1 FY26; 22.02 FY26), an FCF note ((7.42)), revised CFO, WC and payable-days verdicts, and a CFO dependency paragraph. That paragraph also states that the Rs 7.14 cr cash-flow line exceeds the Rs 6.11 cr balance-sheet rise in other financial liabilities (res L236, L260), with no reconciliation in the filing. Q18 is re-forked: bull = operating accruals with a dated settlement and CFO stated without them; bear = capital creditors inside operating cash flow, or dues that unwind in H2. The cash answer, Pillar 2 row, 8B, M8, verdict item 1, summary, forward map and flag 2 are aligned.
- A5-C01 (CONTRADICTION): Step 3 gains a sequential gross-margin and spares-share table (Q1 FY26 58.25% / 21%; Q2 FY26 71.75% / 48%; H2 FY26 52.81%; FY26 57.13%; Q1 FY27 54.14% / 18%; Q2 FY27 59.88% / 35%). Gross margin ranks with the spares share in all four quarters with a split. The competition brief now states the series and the ranking before any pricing reading; the tender-pricing reading is conditional, and Q11 stays the test. Step 2 diagnostic 2, the Step 3 one-off line, Q11 (why), the summary and a new flag are aligned.
- Style applied at no extra cost: S10 ("all column totals tie", with the data-correction pointer); S11 (derived summary figures tagged [FILED, derived]); S14 (CFO/PAT change written -0.23x); S15 (PENDING LIVE VERIFICATION on the 30 Apr 2027 forward-map date); S16 (ED Kamlesh Shah as the continuity mitigant in verdict item 2 and the CFO flag); S17 (liquid net cash row states it excludes leases; Rs (2.93) cr with leases). S12, S13 and S18 were not requested and are left as logged.
- Verdict unchanged: PROCEED WITH FLAGS. Cash conversion stays INDETERMINATE-WITH-DIRECTION (lean structural); A5-M04 strengthens the structural lean but the missing evidence (ageing, capital-creditor split, FY27 full-year CFO) is still missing. No REWORK or INSUFFICIENT EVIDENCE trigger arises.

## OPEN ITEMS AT CLOSE (orchestrator flag; loop cap reached, operator ruling 2026-10-17: no third loop)

The loop 2 A5 re-audit (work/audit_eimcoeleco_q2fy27.md) returned INCOMPLETE. These three items are NOT fixed in the text above. Read the review with them:
- A5-F04 (FACTUAL): "the filed series shows mix, not price erosion" (rev L178, L508, L614, L625) is not supported. The Q1 FY27 vs Q1 FY26 pair shows gross margin -411 bps with spares share +2.7 pp. Even at a 100% spares gross margin, mix explains at most about 285 of the 613 bps H1 fall. At least about 330 bps (H1, Q2) and about 120 bps (Q1) is an intra-segment fall: price, input cost or equipment mix, not separable from the filing. Q11 stays the test.
- A5-M05 (MISSING): the ED continuity mitigant (rev L451, L610) needs a qualifier. The CFO letter is addressed to an unnamed "Executive Director" (res L489), and the board has two EDs (pres L201-213). Q9 should also ask which ED received the letter, and on what date.
- A5-M06 (MISSING): the liquid-treasury flag needs its cause. Rs 11.05 cr (82%) of the Rs 13.39 cr fall is current investments moving to non-current inside the book. The total book rose Rs 8.24 cr (1.03 net purchases + 7.21 gains), and the company net-bought Rs 1.03 cr while borrowing Rs 2.87 cr. Two readings: a liquidity need, or a choice to borrow short rather than sell. Q14 and Q16 separate them.
None of the three challenges the PROCEED WITH FLAGS verdict (A5). Style notes S19-S28 are logged in the audit only.


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
  - {q: "Share of receivables and H1 revenue due from state-owned customers (CIL subsidiaries, Singareni, MOIL, Hutti Gold, UCIL) vs private customers, and contracted payment days for each? (slide lists 8 state-owned, 8 private names)", from_finding_id: "FN10, A3-11"}
  - {q: "Was any amount reclassified between Compensation to Distributors (3.17 cr, 5.6%) and Other Expenses (12.66 cr, 22.3%) in Q2: yes/no, Rs cr? (Note 4 regrouped comparatives still show 11.2% / 11.9%)", from_finding_id: "FN11, FN04, A3-04, PR/F6-1"}
  - {q: "What asset was capitalised into PPE (64.11 to 111.55 cr), Rs cr, date?", from_finding_id: "FN09, A3-01, PR/F6-3"}
  - {q: "Annual depreciation added by the H1 capitalisation, Rs cr?", from_finding_id: "FN09, A3-01"}
  - {q: "Rs cr of the Rs 133 cr that are signed POs not yet executed, net of GST?", from_finding_id: "FN19, FN05, A3-15, PR/F16-2, PR/F6-2"}
  - {q: "Order book at 31 Mar 2026 and 30 Jun 2026 on the same definition?", from_finding_id: "FN05, A3-15, PR/F6-2"}
  - {q: "Name and start date of successor or interim CFO?", from_finding_id: "FN16"}
  - {q: "Date the 5 Sep 2026 CFO letter was received; earlier Reg 30 intimation yes/no?", from_finding_id: "FN17"}
  - {q: "Product vs spares revenue Rs cr for Q2 FY26, Q1 FY27, Q2 FY27; which chart segment is spares?", from_finding_id: "FN12, A3-14, PR/F12-1"}
  - {q: "Bps split of the 1,187 bps YoY gross-margin fall between mix and price? (sequential GM 59.88% vs 54.14% Q1 FY27 ranks with spares share)", from_finding_id: "A3-13, FN12"}
  - {q: "Share of Rs 115.48 cr inventory against orders shipping in Q3 FY27?", from_finding_id: "FN12"}
  - {q: "Did any Q2 order slip to H2: yes/no, Rs cr?", from_finding_id: "PR/F16-1, A3-13, FN18"}
  - {q: "Facility type and rate of the Rs 5.75 cr borrowing, given liquid net cash moved to Rs (1.53) cr?", from_finding_id: "FN02, A3-02"}
  - {q: "Which temporary difference reversed in the Rs 0.94 cr Q1 deferred-tax credit?", from_finding_id: "FN07, A3-08"}
  - {q: "Share of the Rs 209.96 cr non-current investment book in equity or equity funds?", from_finding_id: "A3-16"}
  - {q: "Confirm FY26 DPS Rs 4.00 vs Rs 5.00; cut to fund FY26 capex yes/no?", from_finding_id: "FN08"}
  - {q: "Rs cr of the Rs 7.14 cr H1 other-financial-liabilities CFO inflow (Rs 0.09 cr in FY26) that are capital creditors, and settlement date? (H1 CFO Rs (5.30) cr without it)", from_finding_id: "FN14"}
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
  - {item: "FY27 full-year CFO/PAT, with and without the other-financial-liabilities line", implied_date: "by 2027-05-30", source_ref: "res L294, L300 (FN10, A3-11)"}
  - {item: "FY27 AR: tax note, PPE schedule, OCI, investment composition", implied_date: "AGM date ND", source_ref: "FN06, FN07, FN09, A3-16"}
  - {item: "Borrowings, liquid net cash and new NC liability lines", implied_date: "Mar-27 balance sheet", source_ref: "res L216-219, L236-237, L243 (FN02, FN03)"}
  - {item: "Deck Exceptional line non-zero", implied_date: "each quarter", source_ref: "pres L401 (A3-03)"}
  - {item: "New products commercial data", implied_date: "next deck, by 2027-02-14", source_ref: "pres L487 (A3-05)"}
  - {item: "Piling-rig orders after Bauma ConExpo", implied_date: "next deck", source_ref: "pres L539-544 (A3-07)"}
  - {item: "FY27 DPS vs implied FY26 Rs 4.00", implied_date: "Q4 FY27 board outcome", source_ref: "res L319, L230 (FN08)"}
flags:
  - "PRE-THESIS READ: no Notion page, no companies file, no spear; Decision Status ND"
  - "Cash conversion INDETERMINATE-WITH-DIRECTION (lean structural): H1 FY27 CFO/PAT 0.08x, FY26 0.57x, FY23-FY26 0.50x; receivables +25.8% in H1; H1 CFO Rs (5.30) cr without the Rs 7.14 cr other-financial-liabilities inflow (res L294); capital-creditor share unknown (Q18)"
  - "CFO exits 2026-10-30 with no successor named; letter dated 2026-09-05 disclosed 2026-10-13 (38 days); mitigant only: ED Kamlesh Shah (ICAI fellow, about 27 years in finance and treasury) signs the statements"
  - "Rs 47.44 cr net PPE addition in H1 with no note; D&A not yet stepped up; Q3 D&A is the tell"
  - "Whole +321 bps YoY margin gain rests on the distributor plus other line (fixed-cost lines net -59 bps vs GM fall); distributor comp 5.6% of Q2 revenue vs 11.2-11.9%; Note 4 regrouped comparatives lean against a reclass; Q2 margin 18.9% not creditable until answered"
  - "Core PBT +226% YoY is off a trough base: H1 (+57.7%) and TTM (+22.4%) carry the same Rs 7.47 cr gain, 79% from the Q2 recovery; trough-free Q1 YoY +14.9%; TTM EPS Rs 72.97 is 14.4% below FY25 Rs 85.25; TTM core PBT Rs 40.82 cr below FY25 about Rs 48 cr; Q2 Rs 8.55 cr below H2 FY26 quarterly average Rs 10.21 cr; 60% of YoY gain equals the distributor-rate drop"
  - "YoY gross-margin fall (71.75% to 59.88%) is off the Q2 FY26 outlier; sequential GM 59.88% vs Q1 FY27 54.14% and ranks with the spares share (A3-14 reading); no filed evidence of price erosion; Q11 tests"
  - "Treasury liquidity: liquid net cash Rs 11.86 cr to Rs (1.53) cr in H1 (Rs (2.93) cr with leases); current investments -79.7%; book 98.7% non-current, composition undisclosed; Rs 358.9/share net cash is not a liquid figure; H1 dividend in effect funded by borrowing"
  - "Rs 133 cr labelled both order book and open order pipeline; definition unresolved"
  - "Customer slide: 8 state-owned, 8 private of 16 names; no revenue or receivable share disclosed (Q2)"
  - "Other income 32.1% of H1 PBT; 74.7% of H1 OI is FV gains (largely MTM)"
  - "Q1 FY27 deferred-tax credit Rs 0.94 cr; ex-deferred H1 ETR 25.91%"
  - "Implied FY26 DPS cut Rs 5.00 to Rs 4.00 (derived from reserve roll)"
  - "Data corrections applied: R150 belongs to 31.03.26; H1 FY26 investing comparatives row-misaligned (H1 FY26 capex ND); text glitches R014/R153/R242 resolved"
  - "Downstream tracker rows not supplied; zero signals; reopen Role 5.5 at initial workup"
  - "Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); pillar facts flagged in review"
plain_language_brief_included: true
analyst_note: "Loop 2 applied (A5-F03, M03, M04, C01). Core PBT rose from Rs 2.62 cr to 8.55 cr YoY, off a trough base. H1 and TTM carry the same Rs 7.47 cr gain, 79% of it the Q2 recovery. The trough-free Q1 YoY is +14.9%, and TTM EPS is still 14.4% below FY25. The +321 bps margin gain rests wholly on the distributor plus other line; fixed-cost lines net -59 bps. The YoY gross-margin fall is off an outlier base. Sequential gross margin ranks with the spares share, so the filed series shows mix, not price. Cash conversion is the binding weakness. H1 CFO of Rs 1.84 cr is positive only because of a Rs 7.14 cr other-financial-liabilities inflow; without it CFO is Rs (5.30) cr. If that line holds capital creditors, CFO is overstated. The lean stays structural, but ageing and the creditor split are missing, so INDETERMINATE-WITH-DIRECTION holds. Liquid net cash moved from Rs 11.86 cr to Rs (1.53) cr. The customer slide is 8 state-owned and 8 private names, so the slow-payer reading is conditional. PROCEED WITH FLAGS stands. 8A-W applies because the name is not held."
review_path: "runs/eimcoeleco-q2fy27/work/review_eimcoeleco_q2fy27.md"
```

=====================================================================
## CONTENT PART: A3 FORENSICS, results (work/forensics_results_eimcoeleco_q2fy27.md, verbatim)
=====================================================================
# A3 FORENSIC NOTES: results | Eimco Elecon (India) Ltd (EIMCOELECO) | q2fy27

Inputs read: A1 structured (R001-R470), A1 fulltext (lines 1-523, all), A2 ledger (LI001-LI099, Z1-Z11, AG1-AG2d, P1-P4, S1-S4, M001). Prior-quarter fulltext: ND. Notion checklist: ND (pre-thesis read, no spear on record). Source PDF and inputs/ not opened.
Units: Rs lakhs unless stated (x0.01 = Rs crore). Quotes are verbatim from the fulltext with runs of whitespace collapsed. Ratios marked [derived] are arithmetic on filed numbers, not filed numbers.

## LEDGER RECONCILIATION
- Structured IDs in ledger: 470 of 470, plus M001 (fulltext line 322). Every row read at its fulltext line. Reconciled: 100%.
- Arithmetic tie-outs run (all tie unless noted): P&L totals Q/H1/FY; BS NCA, CA, NCL, CL, total (both dates); CF operating, investing, financing and net change (all three columns); taxes paid vs current tax plus current tax liability movement (779.00 + 5.32 = 784.32); investments movement vs CF (102.75 purchase + 721.17 FV gain = 823.92 = change in total investments); DTL movement vs P&L deferred tax (770.36 - 676.36 = 94.00).
- A2 Z5 confirmed: R150 Other non-current assets 4,824.68 belongs to 31.03.26. Line 211 places it in the right-hand column, and NCA sums tie only that way (31,717.32 with it; 33,502.99 without it at 30.09.26).
- A2 layout flag confirmed (H1 FY26 investing column, lines 303-308): the column sums to the printed (364.39), but 241.20 and 10.15 equal the H1 FY26 interest and dividend add-backs (lines 280-281) one row higher. The comparative labels are misaligned. See FN20.
- Text-layer glitches resolved by tie: R014 = 8,528.25; R153 = 11,547.54; R242 = (308.64); R267 FY26 PPE sale proceeds = 121.03 [derived from investing total; verbatim value NOT FOUND].
- ASSIGNMENT_BY_LAYOUT (R307-R310) confirmed: current liabilities tie at both dates with 791.17 + 1,803.87 (Sep-26) and 770.37 + 992.58 (Mar-26).

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN01 | F1 | Z5 / R150, R151, R152 | 211, 212 | "(f) Other non-current assets 4,824.68" (right-hand, 31.03.26 column) | NEUTRAL-FACT | Data correction for A1/A4: the Mar-26 cell is 4,824.68 and the Sep-26 cell is blank. The line did not stand at zero. It emptied in H1. Substance carried to FN09. |
| FN02 | F1 | Z8 / R287, R288; LI054 R187, R188 | 315, 243 | "Borrowing 286.58 270.39" ; "(i) Borrowing 574.91 278.93" | AMBIGUOUS | Borrowing line is blank for H1 FY26, so borrowing started in H2 FY26. It then doubled to 574.91 by Sep-26 while the company held 21,277.57 of investments (lines 209, 216). Question: nature of the facility, and why borrow instead of drawing the treasury book. |
| FN03 | F1 | Z6, Z7 / R179, R180 | 236, 237 | "(Ii) Other Financial Liabilities 28.37" ; "(b) Other non-current liabilities 8.89" | NEUTRAL-FACT | Two NC liability classes nil at Mar-26 now carry balances (37.26 total, 0.07% of total equity and liabilities). Template lines for deposits or deferred income. Track size in Q3. |
| FN04 | F6 | R355, R412 | 408 | "Margins are in line with our targeted range of 18-20%." | FORWARD-SIGNAL | Undated margin target. Computed EBITDA margin [derived]: Q2 18.9%, Q1 18.4%, H1 18.6%, FY26 18.6%. Feeds Role 5 promise tracker. The Q2 figure depends on FN11. |
| FN05 | F6 | R356, R415, R336, R341, R435, R436 | 374, 377, 381, 386, 413-414 | "Order Book as on September 30th, 2026 (₹ crore)" ; "133" ; "44" ; "Sep-25 Sep-26" | FORWARD-SIGNAL | Rs 133 cr at Sep-26 against a Sep-25 bar of 44 [chart mapping unresolved, CHART_UNMAPPED], about 3x. Order book = 0.50x TTM revenue of Rs 264.26 cr [derived: 23,074.65 - 10,080.63 + 13,432.03]. No inflow figure or basis (GST, executed vs pending) given. |
| FN06 | F8 | Z1 / R091 | 171 | "Adjustment of tax relating to earlier periods ... (10.54)" | NEUTRAL-FACT | Non-zero in FY26 only (a credit of 10.54, 0.2% of FY26 PBT). Blank in all Q/H1 columns. Rule-triggered finding, low weight. Check the FY26 AR tax note at the Role 6 deep dive. |
| FN07 | F8 | R092-R097, R098-R103, R183, R184 | 172, 173, 239 | "Deferred Tax (0.41) (93.59) 7.30 (94.00) 62.15 22.35" ; "(d) Deferred tax liabilities (net) 676.36 770.36" | AMBIGUOUS | ETR [derived]: Q2 25.0%, Q1 21.6%, Q2 FY26 22.4%, H1 22.8%, H1 FY26 21.6%, FY26 23.1%, against 25.17% statutory. The H1 gap below statutory (238 bps) comes from the Q1 deferred credit of 93.59. Ex-deferred, H1 ETR is 25.9%. The DTL fell 94.00 in a half with 721.17 of fair-value gains (line 278) and about Rs 47 cr capitalised (FN09), and both would normally raise a DTL. Question: what reversed. If it does not recur, ETR steps up about 300 bps. |
| FN08 | F11 | R173, R174, R116, R295, R297, R278, R280 | 230, 180, 319, 308 | "Dividend Paid (232.11) (288.21) (286.34)" ; "Bank balance not considered as cash and cash equivalent (Net) 1.37 (0.21) (2.08)" | AMBIGUOUS | Reserve roll [derived]: 46,173.87 + 2,321.09 - 48,264.22 = 230.74 charged to equity = Rs 4.00 x 57.684 lakh shares. The H1 FY26 payout ties to 286.34 + 2.08 = 288.42 = Rs 5.00 per share. Implied FY26 dividend is Rs 4.00 per share, against Rs 5.00 for FY25 (-20%). No dividend note is in this filing. Question: confirm the DPS and the reason (capex funding vs caution). |
| FN09 | F12 | R138, R139, R140, R141, R150, R263, R264, R055, R056; R412-R416 | 204, 205, 211, 303, 164, 405 | "(a) Property, plant and equipment 11,154.88 6,410.76" ; "Depreciation, Impairment and amortisation expense 206.96 210.75" ; "better capacity utilisation" | FORWARD-SIGNAL | PPE +4,744.12 (+74%). Other NCA (capital advance pattern) -4,824.68, CWIP -111.66, but H1 cash capex only 211.48. FY26 cash capex was 6,054.91, so about Rs 47-48 cr was advanced in FY26 and capitalised in H1 FY27, with no note. Q2 D&A fell QoQ (206.96 vs 210.75). So the asset is non-depreciable (land), or it was capitalised late in the half. If late, a Q3 D&A step-up follows. Adding Rs 47 cr of block also sits awkwardly with "better capacity utilisation". Questions: what asset, what capacity, commissioning date. |
| FN10 | F12 | R157, R158, R153, R154, R233, R236, R260, R262, R261, R107 | 217, 214, 288, 289, 300 | "(ii) Trade receivables 9,118.35 7,248.77" ; "NET CASH GENERATED FROM OPERATING ACTIVITIES (A) 183.78 2,210.89 604.44" | AMBIGUOUS | H1 OCF/PAT [derived] = 7.9% (H1 FY26 30.5%; FY26 57.1%). OCF/EBITDA = 7.4%. Receivables +1,869.58 (+25.8%) and equal 68% of H1 billing. DSO on annualised H1 revenue is about 124 days, against about 115 at Mar-26. Last year H1 released 3,039.33 from receivables. This year H1 absorbed 1,870.64. Lean bear: the collection stretch is unexplained. Question: customer mix and overdue ageing. Per CLAUDE.md, cash conversion stays INDETERMINATE until H2. |
| FN11 | F12 | R061-R066, R067-R072, R001-R006 | 165, 166 | "(h) Compensation to Distributors 316.53 870.66 393.91" ; "(i) Other Expenses 1,265.91 1,139.11 658.44" | AMBIGUOUS | Distributor compensation as % of revenue [derived]: Q2 5.6%, Q1 11.2%, Q2 FY26 11.9%, H1 FY26 11.6%, FY26 11.5%. At the Q1 rate, Q2 EBITDA would be 753 (13.3%), not 1,074 (18.9%). Other Expenses rose to 22.3% of revenue (FY26 14.0%). The two lines combined moved less: 27.9% vs 25.5% FY26. So a reclassification is possible (Note 4, line 193, "regrouped /rearranged"), or the channel mix changed (direct vs distributor-routed). The press release credits operating leverage and cost discipline (lines 404-405) and does not name this line. The 18-20% target (FN04) is not creditable until this is answered. |
| FN12 | F12 | R019-R036, R001-R006, R462 | 158-160, 154, 369 | "Changes in inventories of finished goods and work-in-progress (1,149.94) 1,113.13 (1,372.14)" ; "Product Spares" | FORWARD-SIGNAL | Q2 materials consumed 3,187.99 (+47.7% QoQ) and FG/WIP build of 1,149.94, while revenue fell 26.7% QoQ. That points to H2 dispatch loading (a Q3 revenue signal) or to slow-moving stock. Inventory is 11,547.54, about 361 days of H1 COGS annualised [derived]. Gross margin [derived]: Q2 59.9%, Q1 54.1%, Q2 FY26 71.8%, H1 56.6%, H1 FY26 62.7%, FY26 57.1%. Q2 FY26 is the outlier base. The chart stacks (33 = 16 + 17; 57 = 20 + 37; 101 = 30 + 71) hint at mix, but the series are unmapped. Question: the product vs spares revenue split by quarter. |
| FN13 | F12 | R007-R012, R212-R214, R218, R221, R146, R147, R155, R156 | 155, 278, 209, 216 | "Other Income 189.06 775.94 427 .22 965.00" ; "Gain on sale/ fair valuation of Investment (Net) (721.17)" | NEUTRAL-FACT | Investments total 21,277.57 (38.0% of total assets) [derived]. H1 fair-value and sale gains of 721.17 are 74.7% of H1 other income and 24.0% of H1 PBT. The QoQ other-income swing (-586.88) explains 64% of the Q1-to-Q2 PBT fall (-917.61). PBT ex-OI [derived]: Q2 855.18 vs Q2 FY26 262.00 (+226%); H1 2,041.09 vs 1,294.14 (+57.7%). Reported PAT growth (+46.5% Q2) understates core growth because of the treasury line. |
| FN14 | F12 | R191, R192, R193, R194, R195, R196, R251 | 260, 261, 262, 294 | "(iv) Other financial liabilities 1,110.30 527.46" ; "(b) Other current liabilities 1,169.14 1,421 .33" | AMBIGUOUS | Current other financial liabilities +582.84 (+110%). The CF line shows +713.83, and the BS movement explains only 611.21 including FN03, leaving a gap of about 103. Other current liabilities (customer advances usually sit here) fell 252.19 (-17.7%) while the order book rose (FN05). Provisions +174.59 (+29%). Per F12, a falling liability is either a WC unwind or a mix change. Question: what the 1,110.30 holds (capital creditors, deposits, employee dues), and the customer-advance trend. |
| FN15 | F12 | R001-R005 | 154, 393 | "Revenue from Operations 5,679.72 7,752.31 3,323 .64 13,432.03 10,080.63" ; "reflects the sustained momentum in our business" | NEUTRAL-FACT | Q2 revenue -26.7% QoQ. The same pattern ran in FY26: Q1 FY26 6,756.99 [derived] to Q2 FY26 3,323.64 (-50.8%). H2 FY26 was 12,994.02 (56.3% of FY26). Seasonal and lumpy. The press release shows YoY only. Q1 FY27 vs Q1 FY26 [derived] = +14.7%, and Q2 = +70.9%. |
| FN16 | F13 | AG2, R381, R404-R408, R423, R440 | 41-44, 46-50, 474-475 | "has noted the resignation of Mr. Vishal C. Begwani as Chief Financial Officer (CFO) and Key Managerial Personnel (KMP)" | FORWARD-SIGNAL | CFO, materiality KMP and Risk Committee member exits at close of business on 30 Oct 2026. No successor or interim CFO is named (NOT FOUND). The Q3 FY27 close and limited review will be the first without him. His letter names "audit closures" in the handover (line 509). Statutory deadlines for filling the vacancy (Companies Act s.203(4), six months; any LODR timeline) are for A4 to verify. They are not stated here. |
| FN17 | F13 | AG2 TIMING_GAP, R441, R419, R402 | 486, 18, 489 | "Date: September 5, 2026" ; "To: The Executive Director" | AMBIGUOUS | The letter is dated 5 Sep 2026. The exchange disclosure is dated 13 Oct 2026, 38 days later. This filing states no receipt date and references no earlier intimation. The letter is addressed to the Executive Director, not the Board or Chair. Question: when it was received, whether an earlier Reg 30 intimation exists, and why the board noted it only at the results meeting. |
| FN18 | F14 | R353, R354, R340, R343, R345, R346 | 406-407, 380-384 | "PAT stood at ₹8 crore, registering a 46.5% year-on-year increase. Margins improved year-on- year" ; "16.1% 13.8%" | AMBIGUOUS | The deck's own PAT margin chart shows 16.1% to 13.8% (Q2) and 19.7% to 17.3% (H1); the filed numbers confirm 16.1% and 13.8% [derived]. "Margins improved" holds for EBITDA only. The sentence sits next to PAT. Low materiality, but it is a framing tell. |
| FN19 | F14 | R356, R415, R463 | 374, 413-414 | "Order Book as on September 30th, 2026" ; "healthy open order pipeline of ₹133 crore" | AMBIGUOUS | One number, two terms. A "pipeline" can include unconfirmed or bid-stage orders. A "book" means firm orders. Question: are the Rs 133 cr firm executable orders, and what is the GST, spares and executed treatment. Do not use it as a book-to-bill input until answered. |
| FN20 | F14 | R350-R352, R464, R329, R330, R333; LI082-LI087 | 403-404, 363-366, 303-307 | "EBITDA for the quarter increased by 108.8% year-on-year to ₹11 crore, with the EBITDA margin improving to 18.8%" ; "Payments for purchase of property plant and equipment and CWIP (211.48) (6,054.91) 0.40" | AMBIGUOUS | The press-release EBITDA does not reproduce from the statement. Computed ex-OI [derived]: Q2 1,074.35 (18.9%) vs stated 18.8%; Q2 FY26 522.04 (15.7%) vs chart 15.4%; YoY +105.8% vs stated +108.8%; H1 18.6% vs chart 18.5%. The definition is not stated (R464). Separately, the filed H1 FY26 investing comparatives are row-misaligned (the column total ties, the labels do not). Two drafting defects in one filing. Question: the EBITDA definition. |

## F1 ZERO_STANDING EXPLANATION (all 11 rows)
| Z | row | line | why the line exists / transaction class anticipated | outcome |
|---|---|---|---|---|
| Z1 | R091 | 171 | Assessment true-ups for prior years | Non-zero FY26 only; FN06 |
| Z2-Z4 | R110-R112 | 177-179 | Actuarial remeasurement of the gratuity plan | Booked annually only (FY26 gross (35.22)). Interim columns blank, so all of FY27's remeasurement lands in Q4 FY27 |
| Z5 | R150 | 211 | Capital advances / prepaid non-current | Not a standing zero; 4,824.68 emptied in H1; FN01, FN09 |
| Z6-Z7 | R179, R180 | 236-237 | NC deposits, deferred income | Newly populated; FN03 |
| Z8 | R287 | 315 | Borrowing drawdown | Borrowing began H2 FY26; FN02 |
| Z9 | R393 | 192 | Group structure | No subsidiary, associate or JV at 30 Sep 2026 |
| Z10-Z11 | R468, R469 | 476-477 | Reg 30 appointment template | Not applicable (a cessation, not an appointment). It confirms no successor was appointed in this filing |
| Absent lines | - | - | No exceptional-items or discontinued-operations line is in the template at all | Nothing to anticipate from the template |

## CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | FINDING | All 11 ZERO_STANDING rows explained. R150 is a mislabel and an emptied line (FN01). Borrowing started H2 FY26 (FN02). New NC liability lines (FN03). |
| F2 | N.A. | Standalone-only filer. Note 3 (line 192): "The Company has no Subsidiary, Associate or Joint Venture Company(ies) as on September 30, 2026." No consolidated statement exists to decompose. |
| F3 | N.A. | No subsidiaries (line 192), so no shell entities to detect. No Going Concern EoM to reconcile. |
| F4 | PASS | Auditor paras 1-4 (lines 94-123) cover the Company only, with no Other Matter and no component auditors. 0 Rs and 0% of PAT rest on unreviewed numbers. |
| F5 | PASS | No EoM, Going Concern or Other Matter paragraph in the current review report (lines 94-123). Prior-quarter fulltext is ND, so a verbatim diff was not possible. A removal of an earlier EoM cannot be ruled out from this file. |
| F6 | FINDING | Lexicon hits: "shall ... cease" (46, 49), "will relinquish" (470), "I will work closely" (510). Commitments are registered below. Margin target FN04, order book FN05, CFO exit FN16. No "expected to be", "underway" or "completed" status language in the notes. |
| F7 | PASS | Hedge lexicon swept across the notes and full document. The only hit is "future endeavours" (line 516), the valediction of the resignation letter, which is not a hedge. No "subject to", "evaluating", "exploring" or "no assurance" anywhere. |
| F8 | FINDING | ETR 21.6-25.0% across periods vs 25.17%. FY26 earlier-period adjustment is non-zero (FN06). The H1 deferred credit drives the ETR gap, against the expected DTL direction (FN07). |
| F9 | PASS | No OCI in any Q/H1 column (lines 177-179). FY26 net OCI was (26.36), 0.7% of FY26 PBT. There is no interim swing to test. The annual-only booking is noted in F1. Verify the actuarial assumptions at the FY27 AR. |
| F10 | PASS | Paid-up capital 576.84 in all six columns (line 181) and at both BS dates (line 229). Basic = diluted in every period (lines 185-186). Spread is zero, so no dilutive instruments are visible. |
| F11 | FINDING | Net worth ties: 576.84 + 48,264.22 = 48,841.06; 576.84 + 46,173.87 = 46,750.71. The P&L Other Equity of 46,173.87 (line 182) equals the BS. No third-party number is in context. The reserve roll ties to within 1.37, and that 1.37 equals the earmarked-bank release (line 308). The roll exposes the implied DPS cut (FN08). |
| F12 | FINDING | Single segment (line 191), so the whole BS is the segment. Findings: capitalisation (FN09), WC and cash conversion (FN10), cost-line mix (FN11), inventory build and gross margin (FN12), treasury weight (FN13), liability moves (FN14), revenue seasonality (FN15). |
| F13 | FINDING | Board items: results, plus the CFO resignation noted. No AR, AGM, record date, dividend, fund raise or director appointment items. CFO exit with no successor (FN16). 38-day letter-to-disclosure gap (FN17). |
| F14 | FINDING | Note 1 (line 189) "reviewed by Statutory Auditors ... Unmodified conclusion" is consistent with the limited-review letter (lines 86, 117), so there is no audit/review mismatch. Press-release framing and definition defects: FN18, FN19, FN20. Minor: the circular cited at line 56 carries a "SEBI/" prefix that line 462 drops. The board letter (line 43) and Annexure B (line 469) say "outside the Organization", but the resignation letter (line 501) does not. |
| F15 | PASS | The consolidation list is nil at 30 Sep 2026 (line 192). No entity exists to add, delete or rename. Prior-quarter list is ND, so the check is current-period only. |
| F16 | N.A. | Results doctype (instruction rule). The embedded press release has no prior deck to diff against. Its in-document framing issues are carried under F14. |
| F17 | N.A. | Results doctype, no transcript. The Notion checklist is ND (pre-thesis). |

## COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| Vishal C. Begwani ceases as CFO and KMP | close of business 30 Oct 2026 | lines 41-43, 474-475 (R404, R407, R408, R423, R440) | initiated |
| Ceases as materiality KMP (Reg 30) and Risk Committee member | 30 Oct 2026 | lines 46-50 (R405, R406) | initiated |
| "seamless, structured handover of all financial operations, statutory reporting, audit closures" | by 30 Oct 2026 | lines 508-511 (R410, R411) | initiated |
| Successor CFO appointment | NOT STATED. Statutory window is for A4 to verify | implied by lines 41-44, 476 | not started (NOT FOUND) |
| EBITDA margin "targeted range of 18-20%" | undated, ongoing | line 408 (R355, R412) | in line (Q2 18.8% stated) |
| Execute Rs 133 cr "open order pipeline" / order book | undated, as at 30 Sep 2026 | lines 374, 413-414 (R356, R415) | underway |
| "continuing to invest in capabilities" | undated | line 409 (R416) | underway (see FN09 capitalisation) |

## QUESTIONS SEEDED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
FN02 borrowing nature; FN04/FN11 distributor-compensation drop vs Other Expenses rise (reclass or channel mix?); FN05/FN19 order book definition and inflow; FN07 DTL reversal source; FN08 FY26 DPS; FN09 asset capitalised, capacity, commissioning, Q3 D&A; FN10 receivable ageing and collection; FN12 inventory build purpose and product/spares split; FN14 content of other financial liabilities, customer advances; FN16/FN17 CFO successor and disclosure timing; FN18/FN20 EBITDA definition.

```yaml
stage: A3-forensics
company: "EIMCOELECO"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/eimcoeleco-q2fy27/work/forensics_results_eimcoeleco_q2fy27.md"
ledger_reconciled_pct: 100        # 470/470 structured IDs + M001
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN01", check: "F1", line: "211", classification: "NEUTRAL-FACT", implication: "Other NCA 4,824.68 belongs to 31.03.26; Sep-26 blank; line emptied in H1 (see FN09)"}
  - {id: "FN02", check: "F1", line: "315, 243", classification: "AMBIGUOUS", implication: "Borrowing began H2 FY26, doubled to 574.91 while holding 21,277.57 investments; ask facility nature"}
  - {id: "FN03", check: "F1", line: "236, 237", classification: "NEUTRAL-FACT", implication: "New NC liability classes 28.37 and 8.89; track size"}
  - {id: "FN04", check: "F6", line: "408", classification: "FORWARD-SIGNAL", implication: "18-20% margin target, undated; Q2 18.9% computed depends on FN11"}
  - {id: "FN05", check: "F6", line: "374, 377, 381, 386, 413-414", classification: "FORWARD-SIGNAL", implication: "Order book Rs 133 cr vs 44 Sep-25 (chart unmapped), 0.50x TTM revenue; basis and inflow not given"}
  - {id: "FN06", check: "F8", line: "171", classification: "NEUTRAL-FACT", implication: "FY26 prior-period tax credit (10.54); rule-triggered, low weight"}
  - {id: "FN07", check: "F8", line: "172, 173, 239", classification: "AMBIGUOUS", implication: "H1 ETR 22.8% vs 25.17% from Q1 deferred credit 93.59; DTL fell despite FV gains and capitalisation; ~300 bps step-up risk"}
  - {id: "FN08", check: "F11", line: "230, 319, 308", classification: "AMBIGUOUS", implication: "Reserve roll implies FY26 DPS Rs 4.00 vs Rs 5.00 FY25 (derived); confirm and ask why"}
  - {id: "FN09", check: "F12", line: "204, 205, 211, 303, 164, 405", classification: "FORWARD-SIGNAL", implication: "~Rs 47 cr advance capitalised into PPE in H1, no note, no D&A step-up; land or late capitalisation; Q3 D&A is the tell"}
  - {id: "FN10", check: "F12", line: "217, 214, 288, 289, 300", classification: "AMBIGUOUS", implication: "H1 OCF/PAT 7.9%; receivables +25.8%, DSO ~124d; cash conversion INDETERMINATE until H2"}
  - {id: "FN11", check: "F12", line: "165, 166", classification: "AMBIGUOUS", implication: "Distributor comp 5.6% of revenue vs 11.2-11.9%; at Q1 rate Q2 EBITDA margin is 13.3%; Other Expenses rose to 22.3%; possible reclass"}
  - {id: "FN12", check: "F12", line: "158-160, 154, 369", classification: "FORWARD-SIGNAL", implication: "Q2 FG/WIP build 1,149.94 with revenue -26.7% QoQ; H2 dispatch loading or slow stock; product/spares split unmapped"}
  - {id: "FN13", check: "F12", line: "155, 278, 209, 216", classification: "NEUTRAL-FACT", implication: "FV gains 74.7% of H1 OI; OI swing explains 64% of QoQ PBT fall; core PBT ex-OI +226% YoY Q2"}
  - {id: "FN14", check: "F12", line: "260, 261, 262, 294", classification: "AMBIGUOUS", implication: "Other financial liabilities +110%, other current liabilities -17.7% while order book rose; ask contents and customer advances"}
  - {id: "FN15", check: "F12", line: "154, 393", classification: "NEUTRAL-FACT", implication: "Q2 -26.7% QoQ mirrors FY26 seasonality (-50.8%); H2-heavy year; press release shows YoY only"}
  - {id: "FN16", check: "F13", line: "41-44, 46-50, 474-475", classification: "FORWARD-SIGNAL", implication: "CFO exits 30 Oct 2026, no successor named; Q3 close is the first without him"}
  - {id: "FN17", check: "F13", line: "486, 18, 489", classification: "AMBIGUOUS", implication: "Letter 5 Sep 2026, disclosed 13 Oct 2026 (38 days); addressed to ED; ask receipt date and earlier intimation"}
  - {id: "FN18", check: "F14", line: "406-407, 380-384", classification: "AMBIGUOUS", implication: "Margins improved claim next to PAT while PAT margin fell 16.1% to 13.8%"}
  - {id: "FN19", check: "F14", line: "374, 413-414", classification: "AMBIGUOUS", implication: "Rs 133 cr called both order book and open order pipeline; firm vs pipeline unresolved"}
  - {id: "FN20", check: "F14", line: "403-404, 363-366, 303-307", classification: "AMBIGUOUS", implication: "Press-release EBITDA not reproducible (18.9% vs 18.8%, +105.8% vs +108.8%); H1 FY26 investing comparatives row-misaligned"}
forward_signals: ["FN04", "FN05", "FN09", "FN12", "FN16"]
ambiguous: ["FN02", "FN07", "FN08", "FN10", "FN11", "FN14", "FN17", "FN18", "FN19", "FN20"]
commitments:
  - {commitment: "Begwani ceases as CFO and KMP", implied_date: "2026-10-30", ref: "lines 41-43, 474-475", status_word: "initiated"}
  - {commitment: "Ceases as materiality KMP and Risk Committee member", implied_date: "2026-10-30", ref: "lines 46-50", status_word: "initiated"}
  - {commitment: "Structured handover incl. statutory reporting and audit closures", implied_date: "2026-10-30", ref: "lines 508-511", status_word: "initiated"}
  - {commitment: "Successor CFO appointment (not stated)", implied_date: "NOT FOUND; statutory window for A4 to verify", ref: "lines 41-44, 476", status_word: "not started"}
  - {commitment: "EBITDA margin targeted range 18-20%", implied_date: "undated", ref: "line 408", status_word: "in line"}
  - {commitment: "Execute Rs 133 cr open order pipeline / order book", implied_date: "undated, as at 2026-09-30", ref: "lines 374, 413-414", status_word: "underway"}
  - {commitment: "Continue to invest in capabilities", implied_date: "undated", ref: "line 409", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read, standalone-only filer, no EoM. Three things matter for A4. (1) The Q2 EBITDA margin of 18.9% (computed) rests on Compensation to Distributors falling to 5.6% of revenue from 11.2-11.9%. Other Expenses rose to 22.3% from 14.0% (FY26). Combined, the two lines moved little (27.9% vs 25.5%), so a Note 4 reclassification is possible. Do not credit the 18-20% target until this is answered. (2) Cash conversion is weak. H1 OCF is 183.78 lakhs against PAT of 2,321.09 (7.9%). Receivables hold 68% of H1 billing. Q2 built 1,149.94 of FG/WIP while revenue fell 26.7% QoQ. Either H2 dispatch loading or slow collection explains it; Q3 separates the two. (3) About Rs 47 cr moved from Other NCA (a Mar-26 capital advance) into PPE in H1, with no note and no D&A step-up. The asset is land or was capitalised late; Q3 D&A is the observation. The CFO exits 30 Oct 2026 with no successor, after a 38-day letter-to-disclosure gap. Derived, not filed: FY26 DPS Rs 4.00 vs Rs 5.00. Fair-value gains make up 74.7% of other income; core PBT ex-OI rose 226% YoY."
```

=====================================================================
## CONTENT PART: A3 FORENSICS, presentation (work/forensics_presentation_eimcoeleco_q2fy27.md, verbatim)
=====================================================================
# A3 FORENSIC NOTES: Eimco Elecon (India) Limited (EIMCOELECO) | Q2 FY27 | doctype: presentation

Inputs read: A1 structured `extracted/eimcoeleco-presentation-q2fy27-structured.md` (R001-R946), A1 fulltext `extracted/eimcoeleco-presentation-q2fy27-fulltext.md` (787 lines, 39 pages), A2 ledger `work/ledger_presentation_eimcoeleco_q2fy27.md`. Prior-quarter fulltext: ND. Notion monitoring checklist: ND (PRE-THESIS READ, no spear on record). Source PDF and `inputs/` not opened.
Line numbers below are A1 fulltext line numbers; slide = page. Units Rs crore unless stated. Deck values are rounded to whole crore; where a ratio needs precision, I derive it from the deck's own margin percentages (shown to 0.1pp) and state the method.

## 0. LEDGER RECONCILIATION

| ledger section | ID range | rows in ledger | rows read at cited line | result |
|---|---|---|---|---|
| Slides | 39 slides (38 with rows; slide 32 divider, none) | 39 | 39 | all slide titles confirmed in fulltext |
| Slide numbers | R001-R748 | 748 | 748 | values match fulltext lines |
| of which ZERO_STANDING | 93 IDs | 93 | 93 | all 0 / "-" / "Nil" confirmed |
| Line items | 130 table x metric | 130 | 130 | slides 18, 19, 20, 36, 37, 38 |
| RESTATED pairs | slide 19~37, 20~38 | 145 | 145 | all equal; R360 "-" (line 431) vs R670 "0" (line 742) is the one difference |
| Chart vs text vs table (A2 left pairing to A3) | slides 15, 16, 18 | 27 pairs | 27 | 25 tie; 2 differ (A3-09) |
| Entities | R749-R821 | 73 | 73 | |
| Forward | R822-R839 | 18 | 18 | |
| Dates | R840-R911 | 72 | 72 | |
| Qualifiers | R912-R946 | 35 | 35 | |
| TOTAL | R001-R946 | 946 | 946 | ledger_reconciled_pct 100 |

Arithmetic tie-outs run on the deck tables (all within crore rounding unless noted): Sep-26 balance sheet assets 335 + 226 = 561 (line 434); equity and liabilities 488 + 8 + 64 = 560 vs 561 (rounding); Mar-26 to Mar-23 balance sheets tie; P&L Q1 + Q2 = H1 within 1 crore on every line; cash flow H1 FY27 does not roll (beginning 1 + increase 1 = 2 vs closing 1, lines 457-461, A3-10).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line / slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R287, R288 (ZERO_STANDING Other Non-Current Assets); R243, R244 (PPE); R251 (CWIP 0); R417 (investing CF); R154-R156 (depreciation) | lines 413, 414, 420, 453, 395; slide 19, 20, 18 | "Other Non-Current Assets  -  48  -  -" and "Property, Plant and Equipment  112  64" | FORWARD-SIGNAL | A Rs 48 cr asset (equal to 75% of the Mar-26 PPE base of 64) moved from Other Non-Current Assets (48 at Mar-26, nil at Sep-26) into PPE (64 to 112) in H1 FY27, with CWIP at 0 and H1 investing cash flow only -1. The cash left in FY26 (FY26 investing -22, line 453) as an advance. Quarterly depreciation stayed at 2 in both Q1 and Q2 (line 395), so either the asset is non-depreciable (land) or it was capitalised late and a depreciation step-up is coming. The deck names no capex, capacity or land purchase anywhere. Net fixed asset turnover falls as a result (3.1 to 2.8, lines 376-377). Question for A4: what is the asset, what capacity does it add, and what is the H2 depreciation run-rate. |
| A3-02 | F1 | R275-R278 (ZERO_STANDING non-current borrowings); R323, R324 (current borrowings); R175-R179 (ZERO_STANDING finance cost); R325 (cash); R271, R315 (investments) | lines 418, 426, 398, 427; slide 19, 18 | "(i) Borrowings  6  3" (current) against "(i) Borrowings  -  -  -  -" (non-current) and "Finance Cost  0  0  0  0  0" | AMBIGUOUS | The line stays at zero for term debt, but short-term borrowings appear for the first time in four year-ends: 3 at Mar-26, 6 at Sep-26. Operating cash is 1 cr (line 427), while investments total 213 (210 + 3, lines 418, 425). The company borrows against operations while it holds 38% of total assets in investments. Finance cost rounds to 0 in all periods. The EBIT YoY of 50.7% vs PBT YoY of 51.8% (lines 396, 399) shows a sub-crore finance cost in Q2 FY26 that the "0" hides. Question for A4: the nature of the 6 cr facility (overdraft, bill discounting, packing credit), and why it is not funded from the current investment book (14 to 3 in H1). |
| A3-03 | F1 | R196-R200 (Exceptional, all zero); R303 (Other non-current liabilities 0 vs "-"); R283, R284, R329, R330 (lease liability) | lines 401, 422, 419, 427, 709-710; slide 18, 19, 36 | "Exceptional Income / (Expense)  0  0  0  0  0" | NEUTRAL-FACT | The quarterly P&L template carries an Exceptional line (and "Profit before Tax & Exceptional Items", line 399) that the historical P&L (lines 709-710) does not carry. The line anticipates one-off items; none in the five periods shown. A lease liability appears from Mar-26 (1 cr non-current, 0 current). Other non-current liabilities change from "-" to "0" at Sep-26 (a sub-0.5 cr balance appears). No action beyond watching the Exceptional line in H2. |
| A3-04 | F6 | R822, R064 (target); R146, R505, R506 (actuals) | line 327 (slide 15); lines 393, 704 | "Margins are in line with our targeted range of 18-20%." | FORWARD-SIGNAL | The only quantified management target in the deck. It is undated and standing. H1 FY27 EBITDA margin 18.5% (line 393) and FY26 18.3% (line 704) sit inside it; FY25 was 22.7% (line 704), above the band. The band therefore sets the bar below the FY25 peak. It caps a bull margin-reset reading unless management raises it. Tracker item: EBITDA margin vs 18-20% each quarter; question for A4 on the basis of the band and on whether FY25 22.7% was mix or one-off. |
| A3-05 | F6 | R438, R873, R768, R853, R788-R790, R767, R849 | lines 487, 182-186, 173-177 (slides 23, 9) | "Three New Products Released in 2025-26" and "Entered the Battery-Operated space with the MUV & MCAR-E" | AMBIGUOUS | Launch status is "completed" for MCAR-E, MUV and CM-3500. The deck gives no units sold, orders or revenue share for any of them. The installed base is 1,065 machines (683 coal, 382 non-coal, lines 504-511); no prior count is available to diff. Question for A4: orders and deliveries of each new product, and their share of the 133 cr order book. |
| A3-06 | F7 | R927, R938, R830, R829, R834 | lines 579, 627, 595-598, 590, 616 (slides 28-30) | "Production goal and fleet ambition are separate disclosures." / "(in-principle pipeline, not current committed capex)" / "Fleet use may support ... subject to maintenance cycles." | AMBIGUOUS | The outlook slides rest on third-party sector data (PIB, CIL, HCL, HZL, MOIL, DAE, HGML), and the deck hedges each demand route itself. It separates the 100 Mt UG coal goal from fleet demand (only 47 continuous miners across 27 CIL mines, line 568). It calls uranium a non-committed pipeline. It makes metals demand conditional ("potential", "may", "subject to"). No Eimco-specific pipeline, tender win or customer order figure appears. Lean bear: the sector case is context, not evidence of Eimco orders. Question for A4: how much of the order book is continuous miner packages and LHDs for CIL reopened mines vs metals. |
| A3-07 | F7 | R838, R942, R470, R468, R941 | lines 646-649, 641-644, 326 (slides 31, 15) | "Six-month outlook signals stabilisation rather than a broad upturn." / "resilience in an unstable market" | FORWARD-SIGNAL | Management chose to show a neutral (50) real-estate sentiment survey on its piling-rig slide. It also notes that the 9-12% ICEMA forecast "Covers all construction equipment, beyond piling rigs" (line 643). The revenue text uses "unstable market" (line 326). Together these pre-empt flat construction (piling rig) demand for H2 FY27. Question for A4: piling-rig orders and leads after Bauma ConExpo (15-18 Sep 2026, line 539). |
| A3-08 | F8 | R188, R191, R193, R194, R230, R233, R235, R236, R217-R221, R534-R550, R299, R300 | lines 400, 404, 406, 711-714, 421 (slides 18, 36, 19) | "Tax  3  2  4  7  5"; "Deferred Tax Liabilities  7  8" | AMBIGUOUS | ETR from the deck's own margins (1 minus PAT margin / PBT margin): Q2 FY27 25.0%, Q1 FY27 21.3%, Q2 FY26 22.7%, H1 FY27 22.8%, H1 FY26 21.5%, FY26 22.9%, FY25 25.5%, FY24 19.1%, FY23 20.9%. Six of nine periods sit below the 25.17% statutory rate. H1 FY27 is about 240 bps below. The low-ETR quarter (Q1 FY27, 21.3%) is the high other-income quarter (8 cr, line 394). Q2 FY27 has other income of 2 and ETR of 25.0%. The pattern fits other income that is taxed at concessional capital-gains rates. DTL fell from 8 to 7 in H1 (line 421), a small deferred tax credit. If treasury income falls, ETR moves toward 25.17%. The deck carries no prior-year tax adjustment line (NOT FOUND). Verify at the results filing and the AR. |
| A3-09 | F14 | R224 vs R069, R077; R231 vs R076 | lines 405 vs 341, 351; line 406 vs 346 (slides 18, 16) | "PAT ... 46.7%" (table) vs "increasing 46.5% YoY" (text); "PAT Margin (%) ... 16.0%" (table) vs "16.1%" (chart) | NEUTRAL-FACT | Two figures differ between chart and table on the same metric and period. Each gap is immaterial. They show that the deck draws its numbers from two separate calculations. Use table values (slide 18) as the deck's base. |
| A3-10 | F14 | R002 vs R437; R360 vs R670; R425, R429, R433 | lines 148 vs 472; 321; 428-429, 739-740; 431 vs 742; 457-461 | "52 YEARS" vs "50 Years of Engineering Excellence"; "Q2 F27 EBITDA" | NEUTRAL-FACT | Drafting slips. Company age is 52 years on slide 8 and 50 years on slide 22. "F27" is a typo for FY27 (line 321). Two balance-sheet lines carry the same number "(iii)" (Trade Payables and Other Financial Liabilities). Mar-24 Current Tax Assets is "-" on slide 19 and "0" on slide 37. The H1 cash roll does not foot (beginning 1 + increase 1 vs closing 1). Each slip is immaterial. Together they are a governance data point on deck preparation. |
| A3-11 | F16 | R091, R093, R916 (WC days, TTM note); R401, R413 (WC change, OCF); R222-R229 (PAT); R319, R320 (receivables); R724-R727, R542-R545 (history) | lines 376-377, 382, 445, 451, 405, 426, 762, 713 (slides 17, 20, 18, 19, 38, 36) | "Working Capital (Days)  232  219" and "Note: All the Key Ratios are calculated on TTM basis" vs "Net Cash from Operating Activities  2" | FORWARD-SIGNAL | The ratio slide shows working-capital days improving from 232 to 219. In rupees, working capital rose by 16 cr in H1 (line 445). Receivables rose from 72 to 91 (line 426). On TTM revenue of 264 (231 - 101 + 134), receivable days moved from about 114 to about 126. H1 OCF is 2 cr against PAT of 23 (9% conversion). The days figure improves only because the TTM revenue denominator rose. Multi-year conversion is weak as well: FY23-FY26 OCF 74 vs PAT 149, about 50% (lines 762, 713). Cash conversion is a first-order flag for the thesis. H2 collections on the 91 cr receivables are the test. Question for A4: receivable ageing, PSU (CIL subsidiary) payment terms, and whether the 6 cr borrowing (A3-02) funds this gap. |
| A3-12 | F16 | R086, R088 (current ratio); R090, R092 (NFAT); R373, R374, R377, R378 (current assets and liabilities); R243, R267 | lines 363, 365, 376-377, 433, 413, 416 (slides 17, 19) | "Current Ratio ... 4.5 ... 3.8"; "Net Fixed Asset Turnover Ratio  3.1  2.8" | AMBIGUOUS | The key-ratio slide does not tie to the balance sheet on the same slide set. The period-end current ratio is 207/47 = 4.40 at Mar-26 (shown 4.5) and 226/64 = 3.53 at Sep-26 (shown 3.8, a 7.6% gap). NFAT ties at FY26 (231/(64+9+2) = 3.08, shown 3.1). It does not tie at H1 FY27 (264/(112+7) = 2.22, shown 2.8), which points to an average fixed-asset base used only for H1. The only stated basis is "TTM", which does not define a balance-sheet ratio. The definition differs across periods, or is undisclosed, and the H1 ratios flatter the period-end position. Question for A4: the ratio formulas. Use period-end balance-sheet values downstream, never the slide 17 ratios. |
| A3-13 | F16 | R098, R111, R163, R226 (QoQ); R115-R117 (gross margin); R167-R169, R230-R232 (EBIT and PAT margins); R055, R822 area text | lines 321, 325, 386, 388-389, 396-397, 405-406 (slides 15, 18) | "We delivered a strong Q2 FY27 performance" / "Margins improved year-on-year" vs "-26.7%" QoQ revenue and "Gross Margin (%) 56.5% 65.2% -870 bps" | AMBIGUOUS | The narrative frames Q2 on YoY growth against a low Q2 FY26 base (revenue 33). Sequentially Q2 fell: revenue -26.7%, EBIT -46.9%, PAT -49.2% QoQ (lines 386, 396, 405). The text never mentions these falls. "Margins improved" holds only at EBITDA (+340 bps). Gross margin fell 870 bps YoY. EBIT margin fell 250 bps, PBT margin 230 bps and PAT margin 230 bps YoY (lines 389, 397, 400, 406). The EBITDA gain comes from flat employee cost (6 vs 6, line 390) on 71% higher revenue, not from gross margin. Question for A4: Q2 vs Q1 execution phasing, and whether the gross margin fall is mix or price. |
| A3-14 | F16 | R913 (legend), R035, R038, R044, R045, R049, R050, R052, R054 (bar segments); R115, R116, R118, R120, R121 | lines 302-320, 389 (slides 15, 18) | "Product    Spares" (legend, segments not labelled on bars) | AMBIGUOUS | The revenue chart splits each bar into two segments but does not label which segment is Product and which is Spares. Upper-segment share and gross margin move together in every period: Q2 FY26 48% upper share with GM 65.2%; Q2 FY27 35% with 56.5%; implied Q1 FY27 18% (14 of 78) with 51.8%; H1 FY26 30% with 58.3%; H1 FY27 25% with 53.8%. [INFERENCE] The upper segment is likely spares, the higher-margin aftermarket. On that reading, spares grew 16 to 20 (+25%) YoY in Q2 while product grew 17 to 37 (+118%). Gross margin then falls as equipment share rises. A 133 cr order book that is mostly equipment would carry the same gross-margin pressure into H2. Confirm the legend mapping before anyone uses the split. |
| A3-15 | F16 | R066, R072, R081-R083, R914, R857, R858, R823 | lines 331, 334, 343, 349, 354-356 (slide 16) | "Order Book as on 30th September, 2026 (₹ crore)"; "rising 202% year-on-year to ₹133 crore ... compared with ₹44 crore" | FORWARD-SIGNAL | The order book tripled to 133, which is 0.50x TTM revenue of 264, about six months of sales. That supports H2 revenue. The disclosure is YoY only, from a low Sep-25 base. It gives no Mar-26 or Jun-26 point, no inflow figure, no executable period, no GST basis, and does not say whether spares sit inside the book. If the book covers all revenue, implied TTM inflow is 133 - 44 + 264 = 353. That figure is invalid if spares are booked outside the order book. Definition change vs the prior deck: not assessable (prior ND). Question for A4: sequential order book, Q2 inflow, the order book definition, and concentration by customer. |
| A3-16 | F16 | R149-R153 (other income); R180-R187, R201-R208 (PBT); R509-R512, R529-R532; R271-R274, R315-R318 (investments); R915; R255, R256 (other equity) | lines 394, 402, 705, 710, 418, 425, 352, 414 (slides 18, 36, 19, 16) | "Profitability remained stable despite margin moderation primarily due to lower other income" | AMBIGUOUS | Other income is a structural part of PBT: H1 FY27 9 of 30 (30%), H1 FY26 12 of 25 (48%), FY26 17 of 50 (34%), FY23 to FY25 27-38%. It also swings hard within the half: Q1 8, Q2 2. Investments (213) are 38% of total assets (561). Total investments rose 8 in H1 (205 to 213) while investing cash flow was -1 (line 453). That gap suggests a non-cash fair-value element. Whether it sits in P&L other income or in OCI cannot be closed from the deck: the deck shows no OCI and no dividend (NOT FOUND). Other Equity rose 21 against PAT of 23 (line 414). Headline PAT growth therefore carries treasury noise. Operating PBT (EBIT less other income) is the clean series. Question for A4: the other income split into interest, dividend, realised and MTM gains, and the composition of the 210 cr non-current investment book. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing line items | FINDING | 93 ZERO_STANDING cells read. The Other Non-Current Assets 48-to-nil transition carries a Rs 48 cr capitalisation (A3-01). Nil term debt sits beside new short-term borrowings (A3-02). The Exceptional line and minor template lines are NEUTRAL (A3-03). |
| F2 Standalone vs consolidated | N.A. | The deck presents unaudited standalone results only ("unaudited standalone financial results", line 33). There are no consolidated columns to decompose. |
| F3 Shell-entity detection | N.A. | No standalone vs consolidated cost lines in the deck. |
| F4 Unaudited contribution ratio | N.A. | No auditor's report or Other Matters paragraph in a presentation. |
| F5 Going concern / EoM scope | N.A. | No emphasis-of-matter text in the deck; prior-quarter fulltext ND. |
| F6 Forward-commitment phrase mining | FINDING | Lexicon sweep returns no management hit. The only hit is safe-harbour boilerplate: "No offering of securities of the Company will be made" (line 63). Non-lexicon management commitments go to the register: the 18-20% EBITDA band (A3-04), order book visibility, and completed product launches (A3-05). |
| F7 Hedge phrase mining | FINDING | The outlook slides self-hedge each demand route ("subject to", "may", "potential", "not current committed capex", "separate disclosures"; A3-06). The construction slide pre-empts flat piling-rig demand (A3-07). Safe-harbour "subject to known and unknown risks" (line 72) is boilerplate and is not scored. |
| F8 Tax forensics | FINDING | ETR is derived from the deck's margins in nine periods. Six of nine sit below 25.17%. Low ETR coincides with high other income. DTL fell 8 to 7 (A3-08). Prior-year tax line NOT FOUND in the deck. |
| F9 OCI forensics | N.A. | The deck shows no OCI or actuarial line. The equity roll-forward gap is noted in A3-16. |
| F10 Share count and dilution | PASS | Equity Share Capital is 6 in all five balance sheets (lines 413, 722). EPS ties to PAT with no change in share count (FY26 PAT 39 / EPS 67.11 = about 58 lakh shares; H1 FY27 23 / 40). The deck shows only one EPS line; no diluted EPS is shown, so no spread is visible. |
| F11 Reserves and net worth tie-out | PASS | Paid-up plus Other Equity equals Shareholders Funds in every period: Sep-26 6 + 483 = 489 vs 488 (rounding); Mar-26 468; Mar-25 432; Mar-24 386; Mar-23 349 (lines 413-415, 722-724). The Other Equity roll-forward runs within 3 cr of PAT in every year (FY24 +37 vs PAT 40; FY25 +46 vs 49; FY26 +36 vs 39; H1 +21 vs 23). There is no gap above 5%, and no third-party net worth figure appears in the deck. |
| F12 Segment forensics | N.A. | No segment revenue, assets or liabilities in the deck. The product/spares revenue split is treated under F16 (A3-14). |
| F13 Board outcome beyond results | N.A. | The deck carries no board outcome. Slide 10 lists eight directors (four independent) with no term dates. The cover letter (lines 26-34) is a Reg 30 transmittal of the presentation only. |
| F14 Note drafting inconsistencies | FINDING | Chart vs table mismatches on PAT growth and PAT margin (A3-09). Age 52 vs 50 years, the "F27" typo, duplicate "(iii)" numbering, a dash vs 0 restatement, and an H1 cash roll that does not foot (A3-10). |
| F15 Entity list diffs | N.A. | Standalone deck, no consolidation list; prior-quarter ledger ND (A2: ENTITY_CHANGE not assessable). |
| F16 Dropped and reframed disclosures | FINDING | The cross-deck diff is not assessable (prior deck ND). The within-deck reframes are recorded: WC days improve while rupee WC and OCF deteriorate (A3-11); key ratios do not tie to the balance sheet (A3-12); YoY framing on a low base leaves the QoQ fall and the 870 bps gross-margin fall unnarrated (A3-13); the product/spares legend is unresolved (A3-14); the order book is shown YoY only, without a definition (A3-15); other income reliance (A3-16). |
| F17 Silence audit | N.A. | Concall-specific; this is a presentation. No Notion monitoring checklist exists (PRE-THESIS READ). Items for A4 to carry into the concall silence audit: A3-01 asset, A3-02 borrowings, A3-11 cash conversion, A3-15 order book definition. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note / slide ref | status word |
|---|---|---|---|
| EBITDA margin "targeted range of 18-20%" (management) | undated, standing | slide 15, line 327 (R822) | underway (H1 FY27 18.5%, inside band) |
| Order book "provides strong visibility going forward" (management) | undated; implies H2 FY27 execution | slide 16, line 355 (R823) | underway (book 133 at 30 Sep 2026) |
| Battery-operated MUV and MCAR-E entry | 2026 | slide 9, lines 182-186 (R853); slide 23, line 487 | completed (launched; no commercial data) |
| CM-3500 continuous miner launch | 2025 | slide 9, lines 173-177 (R849); slide 23 | completed (launched; no commercial data) |
| EC216 "India manufacturing, local spares and pan-India service" | undated, stated as in place | slide 31, line 643 | completed (claimed; not evidenced) |
| Bauma ConExpo India showcase of EC125 / EC216 / EC267 | 15-18 Sep 2026 | slide 26, lines 539-544 (R874, R824) | completed (event held; leads not disclosed) |

Third-party targets cited as context (not management commitments; do not track as Eimco promises): government UG coal of 100 Mt by 2030 (line 561); HCL ore capacity of 12.2 MTPA by FY2029-30 (line 597); 13 uranium projects with in-principle approval (line 616); CIL award of 23 discontinued UG mines, June 2024 (line 573).

## 4. FLAGGED FOR A4 (management questions)
FORWARD-SIGNAL: A3-01, A3-04, A3-07, A3-11, A3-15.
AMBIGUOUS: A3-02, A3-05, A3-06, A3-08, A3-12, A3-13, A3-14, A3-16.

```yaml
stage: A3-forensics
company: "EIMCOELECO"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/eimcoeleco-q2fy27/work/forensics_presentation_eimcoeleco_q2fy27.md"
ledger_reconciled_pct: 100        # 946 of 946 structured IDs read at fulltext line
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: PASS
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "413, 414, 420, 453, 395 (slides 19, 20, 18)", classification: "FORWARD-SIGNAL", implication: "Rs 48 cr Other Non-Current Assets (Mar-26) capitalised into PPE (64 to 112) in H1 with CWIP 0, investing CF -1, depreciation flat at 2/qtr; asset unnamed in deck; land or a coming depreciation step-up"}
  - {id: "A3-02", check: "F1", line: "418, 426, 398, 427 (slide 19, 18)", classification: "AMBIGUOUS", implication: "First short-term borrowings (3 at Mar-26, 6 at Sep-26) beside cash 1 and investments 213; finance cost rounds to 0; nature of facility unknown"}
  - {id: "A3-03", check: "F1", line: "401, 399, 709-710, 419, 422", classification: "NEUTRAL-FACT", implication: "Exceptional line zero in all quarterly periods and absent from historical template; small lease and other NCL balances appear"}
  - {id: "A3-04", check: "F6", line: "327 (slide 15); 393, 704", classification: "FORWARD-SIGNAL", implication: "Only quantified target: EBITDA margin 18-20%, undated; sits below FY25 actual 22.7%; caps a margin-reset bull unless raised"}
  - {id: "A3-05", check: "F6", line: "487, 182-186, 173-177 (slides 23, 9)", classification: "AMBIGUOUS", implication: "MCAR-E, MUV, CM-3500 launched; no orders, units or revenue disclosed"}
  - {id: "A3-06", check: "F7", line: "579, 627, 595-598, 590, 616 (slides 28-30)", classification: "AMBIGUOUS", implication: "Outlook built on third-party sector data, self-hedged ('separate disclosures', 'not current committed capex', 'subject to'); no Eimco-specific pipeline"}
  - {id: "A3-07", check: "F7", line: "646-649, 641-644, 326 (slides 31, 15)", classification: "FORWARD-SIGNAL", implication: "Neutral construction sentiment chosen for piling-rig slide plus 'unstable market' pre-empts flat piling-rig demand in H2"}
  - {id: "A3-08", check: "F8", line: "400, 404, 406, 711-714, 421", classification: "AMBIGUOUS", implication: "Margin-derived ETR below 25.17% in 6 of 9 periods (H1 FY27 22.8%, Q1 21.3% with OI 8; Q2 25.0% with OI 2); ETR rises toward statutory if treasury income fades"}
  - {id: "A3-09", check: "F14", line: "405 vs 341, 351; 406 vs 346", classification: "NEUTRAL-FACT", implication: "PAT YoY 46.7% table vs 46.5% text/chart; Q2 FY26 PAT margin 16.0% vs 16.1%; use slide 18 table"}
  - {id: "A3-10", check: "F14", line: "148 vs 472; 321; 428-429; 431 vs 742; 457-461", classification: "NEUTRAL-FACT", implication: "Drafting slips (52 vs 50 years, F27 typo, duplicate (iii), dash vs 0, H1 cash roll not footing); cumulative governance data point"}
  - {id: "A3-11", check: "F16", line: "376-377, 382, 445, 451, 405, 426, 762, 713", classification: "FORWARD-SIGNAL", implication: "WC days framed as improving (232 to 219) while rupee WC +16, receivables 72 to 91, H1 OCF 2 vs PAT 23; FY23-FY26 OCF/PAT about 50%; H2 collections are the test"}
  - {id: "A3-12", check: "F16", line: "363, 365, 376-377, 433, 413, 416", classification: "AMBIGUOUS", implication: "Key ratios do not tie to balance sheet (current ratio 3.8 shown vs 3.53 period-end; NFAT 2.8 vs 2.22); formula undisclosed; use balance-sheet values downstream"}
  - {id: "A3-13", check: "F16", line: "321, 325, 386, 388-389, 396-397, 400, 405-406", classification: "AMBIGUOUS", implication: "YoY framing on low base hides QoQ falls (revenue -26.7%, EBIT -46.9%, PAT -49.2%) and GM -870 bps; EBIT/PBT/PAT margins fell YoY; EBITDA gain from flat employee cost"}
  - {id: "A3-14", check: "F16", line: "302-320, 389", classification: "AMBIGUOUS", implication: "Product/Spares legend unmapped; upper-segment share tracks gross margin in all periods ([INFERENCE] upper = spares); equipment-heavy mix and order book imply H2 GM pressure"}
  - {id: "A3-15", check: "F16", line: "331, 334, 343, 349, 354-356", classification: "FORWARD-SIGNAL", implication: "Order book 133 (+202% YoY, 0.50x TTM revenue 264) supports H2; YoY-only, no sequential point, inflow, GST basis, spares scope or execution period"}
  - {id: "A3-16", check: "F16", line: "394, 402, 705, 710, 418, 425, 352, 414, 453", classification: "AMBIGUOUS", implication: "Other income 30-48% of PBT, Q1 8 vs Q2 2; investments 38% of assets rose 8 with investing CF -1 (non-cash fair value element); OCI and dividend NOT FOUND; track operating PBT"}
forward_signals: ["A3-01", "A3-04", "A3-07", "A3-11", "A3-15"]
ambiguous: ["A3-02", "A3-05", "A3-06", "A3-08", "A3-12", "A3-13", "A3-14", "A3-16"]
commitments:
  - {commitment: "EBITDA margin targeted range 18-20%", implied_date: "undated, standing", ref: "slide 15 line 327 (R822)", status_word: "underway"}
  - {commitment: "Order book provides strong visibility going forward", implied_date: "H2 FY27 (implied)", ref: "slide 16 line 355 (R823)", status_word: "underway"}
  - {commitment: "Battery-operated MUV and MCAR-E entry", implied_date: "2026", ref: "slide 9 lines 182-186 (R853); slide 23 line 487", status_word: "completed"}
  - {commitment: "CM-3500 launch", implied_date: "2025", ref: "slide 9 lines 173-177 (R849)", status_word: "completed"}
  - {commitment: "EC216 India manufacturing, local spares and service", implied_date: "undated, stated as in place", ref: "slide 31 line 643", status_word: "completed"}
  - {commitment: "Bauma ConExpo India showcase EC125/EC216/EC267", implied_date: "15-18 Sep 2026", ref: "slide 26 lines 539-544 (R874)", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Two items carry the most weight. First, cash conversion: H1 OCF is 2 cr against PAT of 23, with receivables up 19. The slide 17 working-capital days improve only because the TTM revenue denominator rose. FY23-FY26 conversion is about 50%. Second, an unnamed Rs 48 cr asset (75% of the prior PPE base) was capitalised in H1 out of an FY26 advance, with depreciation unchanged so far. The first short-term borrowings appear while the company holds 213 cr of investments. This points to tight operating liquidity, not a funding need. Gross margin follows the product/spares mix in every period shown. A tripled, likely equipment-heavy order book therefore lifts revenue but should pressure H2 gross margin. Other income is about a third of PBT, partly non-cash, and it drives the ETR swing. Use operating PBT as the earnings series. The 18-20% EBITDA band sits below FY25's 22.7%. Treat it as management's own bar. The outlook slides are third-party sector data that the deck itself hedges; they are not order evidence."
```

=====================================================================
## CONTENT PART: A3 FORENSICS, pressrelease (work/forensics_pressrelease_eimcoeleco_q2fy27.md, verbatim)
=====================================================================
# A3 FORENSIC NOTES: EIMCOELECO q2fy27, doctype presentation (file tag pressrelease: media release on results)

Inputs read: A1 structured (extracted/eimcoeleco-pressrelease-q2fy27-structured.md), A1 fulltext (extracted/eimcoeleco-pressrelease-q2fy27-fulltext.md), A2 ledger (work/ledger_pressrelease_eimcoeleco_q2fy27.md). Prior-quarter fulltext: ND. Notion monitoring checklist: ND (pre-thesis read, no spear on record). Source PDF and inputs/ not opened.

## LEDGER RECONCILIATION
- Ledger rows: 92 (R001-R092). Rows read at cited fulltext line: 92. Reconciled: 100%.
- Pipeline cite defect (A1, carried into A2): R061 (Ms. Vrushali Thakkar, investor contact) is cited at page 4 line 140. Line 140 is blank. The name sits at fulltext line 160: "For further queries, please contact: Ms. Vrushali Thakkar". Value correct, line wrong. No forensic impact.
- Rounding note: H1 FY27 revenue stack 101 + 34 = 135 (lines 66, 68, 73) vs total 134 (R010). Chart values are rounded Rs crore integers. Growth % values (R013, R014, R023, R024, R033, R034) are consistent with unrounded bases, not with the rounded integers (e.g. 11/5 = +120% vs stated +108.8%). All derived figures below use margin % x revenue where possible and are marked DERIVED, accurate to about Rs 0.5 cr.
- All other line cites verified verbatim.

## DERIVED QUARTER SPLIT (H1 minus Q2; DERIVED from R004-R032)
| Metric (Rs cr) | Q1 FY26 | Q2 FY26 | Q1 FY27 | Q2 FY27 | Q1 YoY | Q2 YoY |
|---|---|---|---|---|---|---|
| Revenue | 68 | 33 | 77 | 57 | +13% | +70.9% (stated) |
| EBITDA (margin x rev) | 12.3 | 5.1 | 14.1 | 10.7 | +15% | +108.8% (stated) |
| PAT (margin x rev) | 14.6 | 5.3 | 15.3 | 7.9 | +5% | +46.5% (stated) |
| PAT minus EBITDA | +2.3 | +0.2 | +1.2 | -2.8 | | |
H1 PAT minus EBITDA: H1 FY26 +2.5 (19.9 vs 17.4); H1 FY27 -1.6 (23.2 vs 24.8). Swing about Rs 4.1 cr.

## FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-1 | F6 | R065, R045, R016, R018, R020, R022 | 117 | "Margins are in line with our targeted range of 18-20%" | FORWARD-SIGNAL | A trackable margin band. Q2 FY27 EBITDA 18.8% and H1 18.5% sit inside it; Q2 FY26 15.4% and H1 FY26 17.2% sat below it. The band is newly reached, not a run-rate. The sentence follows the PAT sentence (line 115); PAT margin 13.8% (R028) is outside it, so which margin is targeted is not stated. Role 5 tracker item: EBITDA margin vs 18-20% each quarter. |
| F6-2 | F6 | R035, R036, R067, R087 | 86, 90, 122-124 | "With a healthy open order pipeline of ₹133 crore ... we are well positioned to sustain our growth momentum" | FORWARD-SIGNAL | Order book Rs 133 cr Sep-26 vs Rs 44 cr Sep-25 = 3.0x. At the H1 FY27 run-rate (Rs 268 cr annualised, DERIVED) it covers about 6 months of revenue. Order inflow is called "healthy" (line 106) but not quantified; opening order book (Mar-26) ND, so H1 inflow and book-to-bill cannot be computed. Execution timeline of the 133 ND. |
| F6-3 | F6 | R069, R070 | 114, 118 | "continuing to invest in capabilities that strengthen our competitive position" | AMBIGUOUS | Investment intent with no amount, asset or date. Line 114 credits "better capacity utilisation". Undisclosed capex is a candidate reading for the D&A side of F14-1. |
| F12-1 | F12 | R002, R003, R005, R006, R008, R009, R011, R012, R059, R089 | 68-78 | "Product    Spares" (legend, line 78; values unlabelled in stacks) | AMBIGUOUS | Revenue split is assigned by chart position only. Reading A (first legend series at stack base = Product): Product 17 -> 37 (+118%), Spares 16 -> 20 (+25%) in Q2; Spares share 48% -> 35% (Q2), 30% -> 25% (H1); Q1 Spares flat at 14 both years (DERIVED). Reading B (reverse): Spares 37 of 57 (65%) in Q2 FY27, up from 52%. Under A, growth is equipment-led and margin rose despite a lower Spares share; under B, the margin rise is mix-led. Separating observation: a labelled split in the results filing or deck. No segment assets or liabilities in document. |
| F14-1 | F14 | R091, R016, R020, R026, R030, R018, R022, R028, R032 | 112-117 | "Our EBITDA for the quarter increased by 108.8% year-on-year to ₹11 crore" | AMBIGUOUS | EBITDA is defined nowhere. PAT margin exceeded EBITDA margin in Q2 FY26 (16.1% vs 15.4%) and H1 FY26 (19.7% vs 17.2%), then fell below it in Q2 FY27 (13.8% vs 18.8%) and H1 FY27 (17.3% vs 18.5%). PAT > EBITDA implies EBITDA excludes Other Income [INFERENCE] and that non-operating income was material in FY26. The PAT-minus-EBITDA cushion swung about Rs 4.1 cr in H1 (DERIVED). Three readings: lower Other Income (treasury drawn down), higher D&A (capacity investment, F6-3), higher tax rate. This is why PAT growth (+17.1% H1) lags EBITDA growth (+43.4% H1). Lean bear: PAT quality now rests more on operations, but the release headlines EBITDA and does not explain the gap. |
| F14-2 | F14 | R086, R073, R077 | 57 | "announced its unaudited financial results for the quarter & half-year ended 30th September 2026" | NEUTRAL-FACT | The release does not state whether figures are standalone or consolidated, and does not mention a limited review. The results filing governs; A4 matches these figures to the filed basis. |
| F16-1 | F16 | R004, R007, R010, R013, R014, R082, R084 | 102-105 | "Our performance in the second quarter of FY27 reflects the sustained momentum in our business" | AMBIGUOUS | The release shows YoY only. DERIVED Q1 FY27 revenue is Rs 77 cr, so Q2 FY27 (Rs 57 cr) is down about 26% QoQ. Q2 FY26 (Rs 33 cr) was itself down about 51% from Q1 FY26 (Rs 68 cr), so the +70.9% headline grows off a weak base. Q1 FY27 grew only +13% YoY revenue and about +5% PAT. Two readings: Q1-heavy seasonality (both years show Q2 < Q1) or lumpy delivery-timed revenue. "Sustained momentum" is not shown quarter on quarter. Separating observation: Q3 FY27 revenue vs Q2 FY27 against the 133 order book. |
| F16-2 | F16 | R092, R046, R036, R087 | 83, 122-123 | "Order Book as on September 30th, 2026 (₹ crore)" vs "healthy open order pipeline of ₹133 crore" | AMBIGUOUS | One number, two labels. "Pipeline" can mean enquiries or bids, not firm orders. Conservative reading: 133 is not confirmed as firm, executable, net-of-GST backlog until defined. The definition (firm vs pipeline, gross vs net of GST, includes spares/service contracts or not) decides whether F6-2 coverage holds. |

## CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | N.A. | Press release has no financial template; A2 zero_standing = 0. |
| F2 | N.A. | One unlabelled set of figures; no standalone vs consolidated pair (basis gap logged at F14-2). |
| F3 | N.A. | No cost lines in document. |
| F4 | N.A. | No auditor report or Other Matters paragraph. |
| F5 | N.A. | No EoM or Going Concern text; prior-quarter fulltext ND. |
| F6 | FINDING | Strict lexicon: zero hits (no "will be", "expected", "commenc", "underway", etc.). Seven undated forward rows (R065-R071) read; three findings F6-1, F6-2, F6-3. |
| F7 | PASS | Hedge lexicon: zero hits ("subject to", "no assurance", "exploring", "evaluating", "endeavour" all absent). No safe-harbour disclaimer either. Nothing to flag. |
| F8 | N.A. | No tax, PBT or deferred-tax line; ETR not computable. Tax is one of the readings named in F14-1. |
| F9 | N.A. | No OCI line. |
| F10 | N.A. | Deck carries no share count or EPS. |
| F11 | N.A. | Deck carries no net worth or reserves. |
| F12 | FINDING | No segment assets or liabilities; the deck carries a Product/Spares revenue stack, assigned by position only (F12-1). |
| F13 | N.A. | No board outcome, AGM, dividend or director text; Reg 30 cover letter only (line 30-32). |
| F14 | FINDING | EBITDA undefined and PAT/EBITDA ordering flips (F14-1); figure basis and review status not stated (F14-2). |
| F15 | N.A. | No consolidation or entity list; prior ND. |
| F16 | FINDING | Dropped disclosures vs prior deck: not assessable (prior ND). Within-deck reframing: YoY-only framing hides QoQ decline (F16-1); order book vs pipeline label (F16-2). |
| F17 | N.A. | Not a concall; Notion checklist ND (pre-thesis read). |

## COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| EBITDA (assumed) margin in the 18-20% targeted range | ongoing, undated | R065, line 117 | none stated (claimed met in Q2/H1 FY27) |
| Sustain growth momentum off Rs 133 cr open order pipeline | undated (order book executes over roughly the next 6 months at H1 run-rate, DERIVED) | R067, lines 122-124 | none stated |
| Continue to invest in capabilities | undated, no amount | R069, lines 117-119 | none stated |
| Strengthen portfolio, broaden capabilities across mining and construction | undated, boilerplate | R071, lines 149-153 | none stated |
| Demand optimism on infrastructure and mining activity | undated | R066, lines 121-122 | none stated |

## QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
- F6-1: Which margin is the 18-20% target, and over what horizon? Is 20% a ceiling?
- F6-2 / F16-2: Is Rs 133 cr firm order book or pipeline? Gross or net of GST? Spares/service included? Execution schedule? H1 order inflow and opening Mar-26 book?
- F6-3: Capex amount and assets behind "invest in capabilities"; capacity added in FY26-FY27?
- F12-1: Product vs Spares values per quarter, labelled.
- F14-1: EBITDA definition; Other Income, D&A, finance cost and tax for Q2 FY26 / Q2 FY27 / H1 both years (match to results filing).
- F16-1: Q1 vs Q2 seasonality pattern; why Q2 FY27 revenue fell from Q1 FY27.

```yaml
stage: A3-forensics
company: "EIMCOELECO"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/eimcoeleco-q2fy27/work/forensics_pressrelease_eimcoeleco_q2fy27.md"
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
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F6-1", check: "F6", line: "117", classification: "FORWARD-SIGNAL", implication: "18-20% margin band newly reached (Q2 FY27 EBITDA 18.8%, H1 18.5% vs FY26 15.4%/17.2%); which margin is targeted not stated; PAT 13.8% is outside it"}
  - {id: "F6-2", check: "F6", line: "86, 90, 122-124", classification: "FORWARD-SIGNAL", implication: "Order book Rs 133 cr vs Rs 44 cr a year ago (3.0x), about 6 months of H1-run-rate revenue; inflow and execution timeline ND"}
  - {id: "F6-3", check: "F6", line: "114, 118", classification: "AMBIGUOUS", implication: "Investment in capabilities unquantified; candidate D&A driver behind F14-1"}
  - {id: "F12-1", check: "F12", line: "68-78", classification: "AMBIGUOUS", implication: "Product/Spares split by chart position only; reading A equipment-led growth with Spares share 48% to 35% in Q2, reading B mix-led margin gain; labelled split separates them"}
  - {id: "F14-1", check: "F14", line: "112-117", classification: "AMBIGUOUS", implication: "EBITDA undefined; PAT exceeded EBITDA in FY26 periods and fell below it in FY27 periods, about Rs 4.1 cr H1 swing; other income down, D&A up or tax up; explains PAT growth lagging EBITDA growth"}
  - {id: "F14-2", check: "F14", line: "57", classification: "NEUTRAL-FACT", implication: "Standalone/consolidated basis and limited-review status not stated; results filing governs"}
  - {id: "F16-1", check: "F16", line: "102-105", classification: "AMBIGUOUS", implication: "YoY-only framing; derived Q1 FY27 revenue Rs 77 cr so Q2 Rs 57 cr is about 26% lower QoQ; +70.9% grows off weak Q2 FY26 base; Q1 FY27 PAT about +5% YoY"}
  - {id: "F16-2", check: "F16", line: "83, 122-123", classification: "AMBIGUOUS", implication: "133 labelled Order Book in chart and open order pipeline in remarks; firm vs pipeline and GST basis undefined; decides whether F6-2 coverage holds"}
forward_signals: ["F6-1", "F6-2"]
ambiguous: ["F6-3", "F12-1", "F14-1", "F16-1", "F16-2"]
commitments:
  - {commitment: "Margin in 18-20% targeted range", implied_date: "ongoing, undated", ref: "R065 line 117", status_word: "none stated"}
  - {commitment: "Sustain growth momentum off Rs 133 cr open order pipeline", implied_date: "undated (about 6 months of revenue cover, derived)", ref: "R067 lines 122-124", status_word: "none stated"}
  - {commitment: "Continue to invest in capabilities", implied_date: "undated, no amount", ref: "R069 lines 117-119", status_word: "none stated"}
  - {commitment: "Strengthen portfolio and broaden capabilities", implied_date: "undated", ref: "R071 lines 149-153", status_word: "none stated"}
  - {commitment: "Demand optimism on infrastructure and mining", implied_date: "undated", ref: "R066 lines 121-122", status_word: "none stated"}
gate_a3: pass
blank_checks: []
analyst_note: "The release headlines YoY growth off a weak Q2 FY26 base (Rs 33 cr, itself about 51% below Q1 FY26). H1 minus Q2 puts Q1 FY27 revenue at about Rs 77 cr, so Q2 fell about 26% QoQ and Q1 FY27 PAT grew only about 5%. The PAT/EBITDA flip matters most: in FY26 PAT exceeded EBITDA, so EBITDA likely excludes a material other-income line. That cushion shrank about Rs 4.1 cr in H1. PAT therefore grew far slower than EBITDA. A4 should match every figure to the results filing's Other Income, D&A and tax lines. The 3.0x order book is the main forward signal. Its label switch (Order Book vs open order pipeline) must be resolved before it counts as backlog. Pipeline defect: A1 cites R061 at line 140; the name is at line 160."
```

=====================================================================
## CONTENT PART: A5 AUDIT VERDICT (work/blocks/a5-audit.yaml, loop 2 re-audit, verbatim)
=====================================================================
stage: A5-adversary
company: "EIMCOELECO"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
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
surviving_bear_counters:
  - {claim: "The filed series shows a mix effect; it shows no price erosion (rev L178, L508, L614, L625; rev L148 frames the YoY GM fall as an outlier-base effect)", counter: "Under A4's own A3-14 chart reading, mix cannot carry the YoY GM fall. Trough-free Q1 FY27 vs Q1 FY26: spares share 20.7% to 18.1%, GM -411 bps, which meets A4's own tender-pricing test (rev L508). Even at a 100% spares gross margin and the most favourable chart rounding, mix explains at most about 285 of the 613 bps H1 fall and about 860 of the 1,187 bps Q2 fall; at least about 330 bps (H1, Q2) and 120 bps (Q1) is within-segment. H1 and Q1 pairs are nearly free of FG/WIP build timing. The residual may be price, input cost or mix inside equipment; the filing cannot split them. Under the opposite chart reading GM ranks inversely with spares share.", source_line: "res L154, L158-160, L357-367; pr L66-76", type: FACTUAL}
  - {claim: "ED Kamlesh Shah signs the statements and gives continuity (rev L451, L610)", counter: "The CFO letter is addressed to an unnamed 'The Executive Director' (res L488-490) and offers to 'work closely with you' on the finance handover (res L510). The board has two EDs, Prayasvin B. Patel and Kamlesh Shah (pres L201-202, L212-213). If the addressee is Kamlesh Shah [INFERENCE], the continuity mitigant is also the officer who held the letter through the 38 days before the board noted it (res L486, L32, L41). Q9 should name the addressee and the receipt date.", source_line: "res L32, L41, L337-339, L486-490, L510; pres L201-217", type: MISSING}
findings_by_type:
  factual:
    - "A5-F04: 'mix, not price erosion' (rev L178, L508, L614, L625) unsupported; at least ~330 bps (H1, Q2) and ~120 bps (trough-free Q1) of the YoY GM fall is within-segment under A4's own chart reading; Q1 meets A4's own tender-pricing test. Loop A4."
  missing:
    - "A5-M05: ED continuity mitigant (rev L451, L610) lacks the qualifier that the CFO letter is addressed to an unnamed ED, one of two (res L489; pres L201-213); the mitigant may be the addressee who held it 38 days. Loop A4."
    - "A5-M06: liquid-treasury flag (rev L246, L264, L453, L615, L479) lacks the attribution: Rs 11.05 cr (82%) of the Rs 13.39 cr fall is current investments moving inside the book (total book +8.24 on 1.03 net purchases + 7.21 gains), not cash spent; Rs 1.03 cr net purchases during Rs 2.87 cr new borrowing; name both readings and Q14/Q16 as separator. Loop A4."
  contradiction: []
  style: [A5-S19, A5-S20, A5-S21, A5-S22, A5-S23, A5-S24, A5-S25, A5-S26, A5-S27, A5-S28]
loop_back_to: "A4"
gap: "A5-F04 (FACTUAL): replace 'shows no price erosion / mix, not price' at rev L178, L508, L614, L625 with the bounded reading (H1 GM -613 bps on a 4.5 pp spares fall; mix at most ~285 bps even at a 100% spares margin; >= ~330 bps within-segment; trough-free Q1 -411 bps on 2.7 pp; residual = price, input cost or inside-equipment mix, unsplit; Q11 tests); align rev L148, L182, L394, L499-500. A5-M05 (MISSING): add to verdict item 2, flag and Step 0D that the CFO letter's addressee is an unnamed ED, one of two (res L489; pres L201-213), so the mitigant may sit inside the 38-day gap; Q9 asks which ED and the receipt date. A5-M06 (MISSING): add to the Step 5 liquid row, net-debt answer, verdict item 4, flag and summary that 82% (Rs 11.05 cr) of the Rs 13.39 cr liquid-net-cash fall is an inside-book shift from current to non-current investments, not cash spent, and that the company net-bought Rs 1.03 cr of investments while borrowing Rs 2.87 cr; name the liquidity-need and allocation-choice readings with Q14/Q16 as separator. Keep the summary within 20 lines."
style_notes:
  - "A5-S19: rounding drift from rounded inputs: H1 margin +122 vs +121.5 bps; Q2 ETR +263 vs +263.6 bps; net debt +2.20 vs +2.19; H1 FY27 dist+other 26.75 vs 26.74%. Compute from lakhs."
  - "A5-S20: FN20 cited for both the H1 FY26 investing misalignment (rev L20, L58, L235) and the EBITDA definition (rev L122, L403, L412); confirm the ID."
  - "A5-S21: rev L449 'two cell positions' understates the preamble's data corrections; reword."
  - "A5-S22: Reg 33 deadlines (rev L370, L433, L437, L511, L518) are statute, not filing; tag as rev L432 does."
  - "A5-S23: Q1 spares-share anchors should add res L359 and L362 (H1 segment labels)."
  - "A5-S24: rev L262 -6.6% uses filed 230.75 (res L154); the anchored deck figures give -6.5%; cite both."
  - "A5-S25: NFAT 2.22 basis unstated; ties to TTM revenue / (PPE + CWIP + intangibles); same basis gives FY26 3.11 vs deck 3.1."
  - "A5-S26: bull symmetry: Sep-25 book Rs 44 cr was 0.34x of H2 FY26 revenue; Sep-26 book is 0.77x of the H2 FY27 threshold."
  - "A5-S27: deck GM (pres L389) deducts manufacturing expense; filing basis does not (Q2 FY27 56.54% vs 59.88%); add one reconciling line."
  - "A5-S28: current provisions +29% (Rs 5.98 to 7.72 cr, res L262) absent from supporting stock items; candidate Q3 sub-question on warranty provisions."
analyst_note: "Loop 2 revision audited fresh. Gate, coverage and arithmetic pass: every derived figure was recomputed from lakhs, with no mismatch above rounding. Three findings loop to A4. F04: the 'mix, not price erosion' reading fails A4's own test. Under the A3-14 chart reading, Q1 FY27 vs Q1 FY26 gross margin fell 411 bps on a 2.7 pp spares shift. Even at a 100% spares margin, mix explains at most about half of the 613 bps H1 fall; at least about 330 bps is within-segment. The H1 and Q1 pairs are nearly free of inventory-build timing. The residual may be price, input cost or mix inside equipment, and the filing cannot split them. M05: the CFO letter is addressed to an unnamed Executive Director, and the board has two; the continuity mitigant may be the addressee. M06: 82% of the liquid-treasury fall is current investments moving inside the book, not cash spent, so the bear and allocation-choice readings both fit. The verdict class PROCEED WITH FLAGS is not challenged. The acquisition probe was not triggered: no deal is described."
