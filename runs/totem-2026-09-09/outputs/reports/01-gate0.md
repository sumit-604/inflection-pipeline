# GATE 0 QUANTITATIVE SCORECARD — Forbes Precision Tools & Machine Parts Ltd (TOTEM)

Run: runs/totem-2026-09-09/ | Stage 1 (B01-gate0) | Model: claude-sonnet-5 | 2026-09-09 | **RUN 2**

## WHY THIS IS RUN 2

Run 1 scored every peer-dependent moat test 0 / "PEER DATA NEEDED" on the
finding that the peer screening CSVs were empty templates. That finding was
based on reading the wrong files. The screener export splits into six CSVs
per company; five (Profit_Loss.csv, Balance_Sheet.csv, Cash_Flow.csv,
Quarters.csv, Customization.csv) are empty formula shells in every export —
this holds for the subject too, and is a known collector defect, now logged
in B00. All data for all four companies (subject + 3 peers) lives in
`<TICKER>-Data_Sheet.csv`, fully populated. This run reads those four files
directly:
- `inputs/screening/screener-Data_Sheet.csv` (subject)
- `inputs/screening/KENNAMET-Data_Sheet.csv` (Kennametal India)
- `inputs/screening/BIRLAPREC-Data_Sheet.csv` (Birla Precision Technologies)
- `inputs/screening/WENDT-Data_Sheet.csv` (Wendt India)

Every conclusion from run 1 that did not depend on peer data is carried
unchanged: the load-bearing-fact verifications, the three-year history
reality, Blocks A through E, and the pledge deal-breaker. Only Block F
(the moat block) and the totals/classification arithmetic that flow from it
are re-done.

Data available: 3 years (FY2023-24 to FY2025-26). Scoring adapted to
3-year history. The company was incorporated in 2022; the Scheme of
Arrangement demerging it out of Forbes & Company Ltd took effect
01-Mar-2024; shares listed on BSE 11-Jun-2024. FY23 is a pre-demerger shell
stub (Total assets Rs 0.05 cr, PBT Rs -0.01 lakh per screener-Data_Sheet.csv)
and is NOT used as a data year. Longer restated history exists only inside
the Information Memorandum (pre-demerger, different entity structure) and
is not used here per the basis-hierarchy rule. FY2023-24, FY2024-25 and
FY2025-26 are the three audited standalone years used throughout.

---

## LOAD-BEARING FACTS — VERIFICATION FIRST (unchanged from run 1; not peer-dependent)

**LBF-1, Q1 FY27 margin bridge — CONFIRMED, all four legs exact.**
Source: inputs/results/FY27-Q1_Unaudited_Results_30Jun2026.pdf, Statement
of P&L, rendered page-03.png (Q1 FY27 results, p.3), cross-checked against
screener-Data_Sheet.csv Quarters block.
- Revenue: Q1 FY27 Rs 67.55 cr vs Q1 FY26 Rs 52.41 cr, +28.9%.
- OPM (Revenue minus materials, purchases, inventory change, employee cost,
  other expenses; excludes finance cost and D&A): Q1 FY27 = (6755-2348-0-92
  -1245-1522)/6755 = 22.9%. Q1 FY26 = (5241-1782-0-(-116)-1131-1603)/5241 =
  16.05% ≈ 16.1%. Both match the claim exactly.
- Combined material cost (net of inventory absorption): Q1 FY27 =
  2440/6755 = 36.12% of revenue. Q1 FY26 = 1666/5241 = 31.79%. Delta =
  +4.33pp, matching the claimed "+4.3pp worsening" exactly. [INFERENCE:
  the margin gain is not a raw-material story; it is an employee-cost and
  other-expense compression story riding on volume, with material cost
  (net of inventory absorption) actually a modest drag.]
- Employee cost: Q1 FY27 = 1245/6755 = 18.43% ≈ 18.4%. Q1 FY26 = 1131/5241
  = 21.58% ≈ 21.6%. Matches exactly.
- Other expenses: Q1 FY27 = 1522/6755 = 22.53% ≈ 22.5%. Q1 FY26 = 1603/5241
  = 30.59% ≈ 30.6%. Matches exactly.
- Exceptional items (Net) = NIL in both quarters.

**LBF-2, FY26 inventory build — CONFIRMED on absolute rupee figures;
inventory-days and CCC figures NOT reproducible from the prescribed
formula on this run's own data.**
Source: annual-report__Annual_Report_2026.txt, Note 8 Inventories (AR FY26,
p.92): Total inventory Rs 5,642.15 lakh (Rs 56.42 cr) at 31-Mar-2026 vs
Rs 3,193.07 lakh (Rs 31.93 cr) at 31-Mar-2025 — matches the claim exactly.
CFO: Rs 2,755.29 lakh (Rs 27.55 cr) FY26 vs Rs 5,131.62 lakh (Rs 51.32 cr)
FY25 (AR FY26, Cash Flow Statement, p.71) — matches the claim exactly.
Using this stage's fixed formula (Inventory Days = Inventory ÷ Revenue ×
365, revenue basis; COGS is not a single explicit P&L line so revenue
basis is used and stated), inventory days computed here are FY24 61.5,
FY25 50.1, FY26 82.0 — real deterioration but far below the claimed
146 → 255 days. The AR-disclosed inventory turnover ratio (AR FY26, p.118)
is 1.83x FY26 vs 2.27x FY25, days-equivalent ~199.5 vs ~160.8 — also
directionally consistent but still not matching 146/255. [DATA NOTE: the
LBF-2 "146 to 255 days" and "91 to 152 day CCC" figures cannot be
reconstructed from this run's own filed data on any basis tried. Direction
confirmed; specific magnitude unverified, not used in scoring.] This
stage's own formula-compliant WC Days: FY24 73.8, FY25 65.2, FY26 78.9.

**LBF-3, promoter pledge — CONFIRMED exactly, all three quarters checked.**
Source: shareholding__SHP_30Jun2026.txt (p.4-5), shareholding__SHP_31Mar2026.txt
(p.4-5), shareholding__SHP_30Jun2025.txt (p.4-5). Promoter and promoter
group hold 38,102,764 shares = 73.85% of 51,594,464 total shares, unchanged
across all three filings. Shares pledged = 35,967,172, all held by
Shapoorji Pallonji And Company Private Limited (100% of ITS holding
pledged). Pledged shares as % of total promoter group holding =
35,967,172 / 38,102,764 = 94.4%, identical at Jun-2025, Mar-2026 and
Jun-2026. No corporate guarantees given (AR FY26 contingent-liabilities
note, p.124: only Rs 16.81 lakh labour-matter claims). Promoter
(Shapoorji Pallonji & Co.) financing-structure pledge, not evidence of an
operating-company guarantee, but a stable, near-total pledge of the
controlling stake and a governance deal-breaker per the scoring rules.

**LBF-4, FY26 revenue basis and exceptional item — RESOLVED: screener
figure is the audited figure; the alleged exceptional item is not found.**
Source: results__FY26_Audited_Results_31Mar2026.txt (FY26 Audited Results,
p.5): Revenue from operations Rs 25,101 lakh = Rs 251.01 cr, FY25
Rs 23,266 lakh = Rs 232.66 cr, matching screener-Data_Sheet.csv exactly.
Growth = 7.9%. "Exceptional items (Net)" is NIL for both FY26 and FY25. A
corpus-wide search for "Labour Code" language returns only standard
boilerplate in every year, no rupee figure. [DATA NOTE: the claimed
"Rs 5.9 cr pre-tax Labour Codes charge inside FY26 profit" is NOT found in
this run's filed sources and is treated as unverified / likely erroneous.]

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — unchanged from run 1, not peer-dependent

Source: AR FY25 ratio note (AR FY25, p.100) for FY24/FY25; AR FY26 ratio
note (AR FY26, p.118) for FY26.

| Year | ROCE (AR-disclosed) | ROE (AR-disclosed) |
|---|---|---|
| FY24 | 28% | 43% |
| FY25 | 22% | 19% |
| FY26 | 22% | 17% |

FY24's 43% ROE is a base-effect artifact of the demerger (average equity
blends a near-zero FY23 pre-demerger base with the post-demerger closing
equity). Flagged, not excluded — the AR discloses it as the actual ratio.

- **A1 Median ROCE** = median(28, 22, 22) = 22% → 20-24.9% band → **4**
- **A2 Minimum single-year ROCE** = 22% → ≥15% → **5**
- **A3 Median ROE** = median(43, 19, 17) = 19% → 15-19.9% band → **4**
- **A4 ROCE trend, latest (22%) vs earliest (28%)** = decline of 6pp →
  decline >5pp → **0**

**Block A total = 13/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — unchanged from run 1, not peer-dependent

Source: Cash Flow Statements, AR FY25 (p.58) for FY24/FY25, AR FY26 (p.71)
for FY26.

| Year | CFO (cr) | Capex (cr) | FCF (cr) | PAT (cr) |
|---|---|---|---|---|
| FY24 | 9.46 | 97.26 | -87.80 | 29.71 |
| FY25 | 51.32 | 28.26 | 23.06 | 28.75 |
| FY26 | 27.55 | 18.39 | 9.16 | 28.77 |

FY24's huge capex is the post-demerger capacity build.

- **B1 Cumulative CFO ÷ Cumulative PAT** = 88.33 / 87.23 = 1.013 → **5**
- **B2 FCF-positive years** = 2 of 3 = 66.7% → 50-74% band → **2**
- **B3 Cumulative FCF ÷ Cumulative PAT** = -55.58 / 87.23 = -0.637 → **0**
- **B4 Change in WC Days, latest vs earliest** = 78.9 - 73.8 = +5.0 days →
  increased 5-15 → **1**

**Block B total = 8/20**

block_b_trend: **deteriorating** — CFO fell from Rs 51.32 cr (FY25) to
Rs 27.55 cr (FY26), a 46% decline, on the inventory build (LBF-2); WC days
rose from 65.2 (FY25) to 78.9 (FY26), +13.7 days within the year even
though the 3-year trend is a smaller +5.0 day net change because FY24's
WC days (73.8) were already elevated by the pre-listing capex ramp.

---

## BLOCK C: GROWTH (Max 20) — unchanged from run 1, not peer-dependent

| Year | Revenue (cr) | PAT (cr) |
|---|---|---|
| FY24 | 228.50 | 29.71 |
| FY25 | 232.66 | 28.75 |
| FY26 | 251.01 | 28.77 |

- **C1 Revenue CAGR** (FY24→FY26, 2 years) = (251.01/228.50)^(1/2) - 1 =
  4.81% → <5% → **0**
- **C2 PAT CAGR** = (28.77/29.71)^(1/2) - 1 = -1.60% → negative → **0**
- **C3 Positive YoY revenue years** = 2 of 2 = 100% → **5**
- **C4 PAT CAGR minus Revenue CAGR** = -1.60 - 4.81 = -6.41pp → -3 to -8pp
  band → **1**

**Block C total = 6/20**

Three years of flat revenue (4.8% CAGR) and flat-to-declining PAT
(-1.6% CAGR) sit directly underneath the Q1 FY27 print (+28.9% revenue,
OPM 16.1%→22.9%, PAT +137% per LBF-1). This scorecard's fixed 3-year
annual window cannot capture Q1 FY27 (single quarter, not a scoring year).

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — unchanged from run 1, not peer-dependent

FY26 figures. Total borrowings Rs 16.64 cr = non-current Rs 10.72 cr +
current Rs 4.15 cr + lease liabilities Rs 1.77 cr (AR FY26 Balance Sheet,
p.69). Cash & bank Rs 6.28 cr. Net worth FY26 = Rs 51.59 cr + Rs 116.99 cr
= Rs 168.58 cr.

- **D1 Net Debt ÷ EBITDA** = (16.64 - 6.28) / 52.62 = 0.197x → **4**.
  [Excludes Rs 23.23 cr mutual-fund investments; including them as
  quasi-cash flips the company to net cash. EBITDA (Operating Profit,
  ex other income) FY26 = Rs 52.62 cr, computed from FY26 Audited Results
  p.5.]
- **D2 Interest Coverage** = (39.50 + 1.66) / 1.66 = 24.8x → **5**
- **D3 Debt ÷ Equity** = 16.64 / 168.58 = 0.099 → <0.1 → **5** [AR's own
  narrower "total debt" D/E is 10% (AR FY26, p.118), exactly at the
  threshold; this stage's screener-total-borrowings-incl-lease basis is
  9.9%, used for scoring]
- **D4 Current Ratio** = 1.84 (AR-disclosed, AR FY26 p.118) → **4**

**Block D total = 18/20** — strongest block. Near net cash, ample
interest cover, minimal leverage.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — unchanged from run 1, not peer-dependent

Source: shareholding__SHP_30Jun2026.txt, shareholding__SHP_31Mar2026.txt,
shareholding__SHP_30Jun2025.txt (all p.4-5). No earlier SHP filing was
provided; the company listed 11-Jun-2024, so a true 3-year
promoter-holding-change window does not yet exist in this run's inputs.

- **E1 Promoter holding (latest, Jun-2026)** = 73.85% → **5**
- **E2 Promoter holding change** — unchanged at 73.85% across all three
  filings (~12 months, not 3 years) → within ±1% → **3** [data_note: window
  is provisional]
- **E3 Promoter pledge (latest, Jun-2026)** = 94.4% of the 73.85% promoter
  holding → >15% → **0**
- **E4 Contingent liabilities ÷ Net Worth** = Rs 0.1681 cr / Rs 168.58 cr =
  0.0997% → <5% → **5**

**Block E total = 13/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — RE-SCORED THIS RUN

### Peer year-end alignment (stated honestly)

Kennametal India (KENNAMET) reports to a **June** year end: its "FY24",
"FY25", "FY26" columns in KENNAMET-Data_Sheet.csv end 2024-06-30,
2025-06-30, 2026-06-30. The subject and Birla Precision Technologies
(BIRLAPREC) both report to **March**: FY24/FY25/FY26 end 2024-03-31,
2025-03-31, 2026-03-31. Wendt India (WENDT) also reports to March, same
calendar as the subject.

For latest-year peer comparisons (M2, M5, M9 below) I compared subject
FY26 (year ended 31-Mar-2026) against BIRLAPREC FY26 and WENDT FY26 (same
31-Mar-2026 year end, exact match) and against KENNAMETAL's FY26 column
(year ended 30-Jun-2026, a 3-month lag — Kennametal's period overlaps
9 of the subject's 12 FY26 months and extends 3 months into what is the
subject's FY27 Q1). This is the closest available match; the alternative
(Kennametal FY25, ended 30-Jun-2025, which overlaps the subject's FY25
more than FY26) was also computed as a sensitivity check for every
peer-dependent test below — in all three cases the peer median or peer
ranking used for scoring did not change between the two alignment choices,
because Birla's and Wendt's own FY26 (exact-match) figures already
determine the tier. This is stated at each test.

Every EBITDA-margin and gross-margin figure below is computed from the
Data_Sheet.csv P&L component rows using one formula, applied identically
to all four companies (screener's own sign convention: "Change in
Inventory" is additive back):

`EBITDA = Sales − Raw Material Cost − Power & Fuel − Other Mfr. Exp −
Employee Cost − Selling & Admin − Other Expenses + Change in Inventory`

This formula was verified against each company's own Quarters-block
"Operating Profit" line (Sales − Expenses, given directly) by summing the
four quarters making up each fiscal year and cross-checking against the
annual computation. All four companies' FY25 and FY26 figures below
reconciled to within rounding; only FY24 could not be cross-checked
(quarterly data in this export starts at the quarter ending 2024-03-31,
before FY24 begins for a March filer and mid-FY24 for a June filer).

**EBITDA margin (Data_Sheet-consistent basis):**

| Company | Basis | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Subject (TOTEM) | Mar FYE | 22.49% | 22.01% | 21.09% |
| Kennametal India | Jun FYE (offset +3mo) | 15.58% | 14.71% | 20.09% |
| Birla Precision | Mar FYE | 11.11% | 8.57% | 6.95% |
| Wendt India | Mar FYE | 24.71% | 22.73% | 13.72% |

(Anchors: KENNAMET-Data_Sheet.csv PROFIT & LOSS rows 11-18, columns
2024-06-30/2025-06-30/2026-06-30; BIRLAPREC-Data_Sheet.csv PROFIT & LOSS
rows 11-18, columns 2024-03-31/2025-03-31/2026-03-31; WENDT-Data_Sheet.csv
PROFIT & LOSS rows 11-18, columns 2024-03-31/2025-03-31/2026-03-31;
screener-Data_Sheet.csv PROFIT & LOSS rows 11-18. Quarterly cross-check:
each file's Quarters block rows 27-36, "Operating Profit" row, summed over
the four quarters composing the relevant fiscal year.)

- **M1 Pricing Power** (not peer-dependent, unchanged): OPM FY24 22.5% →
  FY26 21.0% (AR-sourced basis), change -1.5pp (not expansion); revenue
  CAGR 4.8% (<10%). Fits no scoring tier. **0**
- **M2 Cost Advantage vs peer median EBITDA margin**: subject FY26
  21.09%. Peer FY26 figures: Kennametal (Jun-26) 20.09%, Birla (Mar-26)
  6.95%, Wendt (Mar-26) 13.72%. Peer median = 13.72%. Subject − peer
  median = **+7.37pp**, ≥5pp above → **5**. [Sensitivity: substituting
  Kennametal FY25 (14.71%) for FY26 gives the same peer median, 13.72%
  (order 6.95/13.72/14.71) — score unchanged.]
- **M3 Capital Efficiency** (not peer-dependent, unchanged): FAT (Revenue
  ÷ [Net Block + CWIP]) FY26 = 251.01 / 113.40 = 2.21x; ROCE FY26 = 22%.
  FAT>2x AND ROCE>15% → **3**
- **M4 Customer Stickiness** (not peer-dependent, unchanged): zero
  revenue-decline years; receivable days FY24 47.0 → FY26 43.9, within
  ±10 days → **5**
- **M5 Scale & Dominance**: market capitalisation (as captured in each
  Data_Sheet.csv header, live snapshot as of export, not FY26-end mcap):
  Kennametal Rs 10,356.69 cr, Wendt Rs 1,640.07 cr, subject Rs 856.27 cr,
  Birla Precision Rs 385.64 cr. Subject ranks 3rd of the 4 companies in
  this comparison set. On the same FY26-basis EBITDA-margin table above,
  subject's 21.09% is the HIGHEST of the four (Kennametal 20.09%, Wendt
  13.72%, Birla 6.95%) — margin rank 1 of 4. Test band "top 3 mcap AND
  margin top 2" is met (top 3 of 4, and margin rank 1 clears top 2) → **3**.
  [Caveat: this comparison set is limited to the 3 named peers this run's
  inputs contain, not the full listed precision-tooling/cutting-tool
  segment; treat "top 3" / "largest" language as relative to this
  4-company set, not a verified full-segment ranking. Scored on available
  comparator data, flagged as directional.]
- **M6 Technology/R&D**: no R&D line exists in any of the four
  Data_Sheet.csv exports (no R&D row in the P&L section for subject or any
  peer) and none is disclosed as a separate line in the subject's filed
  ARs. NOT FOUND across the board, not a peer-data gap. **0**
- **M7 Regulatory/License** (not peer-dependent, unchanged): unregulated,
  no licence/quota regime governs this business (cutting tools / precision
  machine parts is not a licensed segment). **0**
- **M8 Distribution** (not peer-dependent, unchanged): not disclosed in
  any filed source read this run. **0**
- **M9 Brand**: gross margin proxy = (Revenue − Raw Material Cost) ÷
  Revenue, stated basis (raw material cost only, not netted for inventory
  change, applied identically to subject and all three peers). Subject
  FY26 GM = (251.01−93.32)/251.01 = 62.83%. Peer FY26 GM: Kennametal
  (1510.7−1018.0)/1510.7 = 32.61%; Birla (247.13−96.87)/247.13 = 60.81%;
  Wendt (236.32−103.38)/236.32 = 56.25%. Peer median = 56.25%. Subject −
  peer median = **+6.58pp** (≥5pp above tier) but revenue CAGR is 4.81%
  (<8% required for the ≥5pp/≥8% tier). Falls to "above peers but growth
  below" → **1**. [Sensitivity: substituting Kennametal FY25 GM (44.61%)
  for FY26 gives the same peer median, 56.25% — score unchanged.]
- **M10 Switching Costs** (not peer-dependent, unchanged): revenue grew
  every year; receivable days fell (43.9 vs 47.0) → **5**
- **M11 Network Effects** (not peer-dependent, unchanged): only 3 years
  available, below the 6-year two-window test threshold; scored
  conservatively. 2-year CAGR 4.8%, well under thresholds; no structural
  network-effect mechanism in this business model. **0**
- **M12 Negative WC/Float** (not peer-dependent, unchanged): WC days
  positive and >45 in all three years (73.8, 65.2, 78.9). **0**

**Moats present (score ≥3): M2, M3, M4, M5, M10 = 5 moats**
**Moat score = 0+5+3+5+3+0+0+0+1+5+0+0 = 22/60**
**Moat classification: 4-5 present = STRONG**

This is a material re-read from run 1's MODERATE (3 moats, 13/60): with
the correct peer data, the subject shows a genuine, well-evidenced margin
and gross-margin edge over the three named peers (Cost Advantage +7.37pp
EBITDA margin, Brand/GM proxy +6.58pp), on top of the peer-independent
capital-efficiency, stickiness and switching-cost tests that already
scored ≥3 in run 1. The moat count and score both roughly double.

---

## SCORECARD DASHBOARD

```
BLOCK A  Return on Capital        [======......] 13/20
BLOCK B  Cash Generation Quality  [========......] 8/20
BLOCK C  Growth                   [======........] 6/20
BLOCK D  Balance Sheet Strength   [==================] 18/20
BLOCK E  Shareholder Alignment    [=============.] 13/20
--------------------------------------------------------
CORE SCORE (A+B+C+D+E)                              58/100

BLOCK F  Quantitative Moat (12 tests, max 60)        22/60
Moats present: M2 Cost Advantage, M3 Capital Efficiency,
               M4 Customer Stickiness, M5 Scale & Dominance,
               M10 Switching Costs
Moat classification: STRONG (5 of 12 present)

GRAND TOTAL (core + moat)                            80/160
```

**Strongest block: D (Balance Sheet Strength), 18/20.** Near net cash,
24.8x interest coverage, D/E 0.10x, current ratio 1.84x.

**Weakest block: C (Growth), 6/20.** Flat revenue (4.8% 3-year CAGR),
flat-to-declining PAT (-1.6% CAGR) across the three audited years — a
structurally quiet base sitting directly beneath the Q1 FY27 inflection
claim, which this scorecard's fixed 3-year annual window cannot capture.

---

## CLASSIFICATION

**Data confidence**: 3 years (FY24-FY26) → 3-4 band → **LIMITED,
downgrade classification one tier**.

**Classification matrix**: Core score 58 falls in the 40-59 band → this
band is flat in the matrix (does not branch on moat tier) → baseline
**AVERAGE**. (Block F strengthening from MODERATE to STRONG this run does
not change the baseline, because the Core 40-59 band does not read Block
F; it would matter at Core 60-79 or Core ≥80.)

**Deal-breaker overrides checked** (unchanged from run 1; none are
peer-dependent):
1. Block A <8? No (13). Not triggered.
2. Block B <8? No (8, at the line). Not triggered.
3. Median ROCE <10%? No (22%). Not triggered.
4. Cumulative CFO/PAT <0.50? No (1.01). Not triggered.
5. **Pledge >15%? YES (94.4% of the 73.85% promoter stake pledged,
   Shapoorji Pallonji & Co., stable across three consecutive quarters
   Jun-2025 to Jun-2026) → caps classification at max AVERAGE.**
6. ND/EBITDA >3x AND IC <3x? No. Not triggered.
7. Revenue declined in majority of years? No. Not triggered.
8. PAT negative in any of last 3 years? No. Not triggered.
9. History <3 years? No (exactly 3 audited years). Not triggered (distinct
   from the data-confidence downgrade below).

**Sequencing**: baseline AVERAGE (Core 40-59) → apply the 3-year LIMITED
history-confidence downgrade, one tier: AVERAGE → **AVOID**. The pledge
deal-breaker independently confirms the classification cannot rise above
AVERAGE even before the history downgrade.

**FINAL CLASSIFICATION: AVOID** (mechanical, per the fixed scoring rules —
unchanged from run 1's outcome, but for a materially different Block F
picture underneath it)

This is a compounding-mechanism outcome, not a company-quality verdict on
its own terms. CLAUDE.md is explicit that quality does not halt a run and
that "downstream position sizing may override AVERAGE for documented
post-IPO rebase / legacy cleanup cases." Three distinct things should be
weighed on their own facts by the operator, not collapsed into one:
- The pledge (94.4% of promoter stake, stable, no operating-company
  guarantee found) is a real governance flag on its own facts.
- The 3-year LIMITED-history downgrade is a structural artifact of the
  Mar-2024 demerger and Jun-2024 listing, not a company-quality signal.
  Absent that downgrade, the mechanical floor here is AVERAGE (from the
  pledge deal-breaker alone), not AVOID.
- With the corrected peer data, the moat picture underneath this AVOID is
  STRONG, not MODERATE: a genuine, evidenced margin edge over all three
  named peers (Kennametal, Birla Precision, Wendt), on top of capital
  efficiency, customer stickiness and switching-cost tests that already
  cleared the bar. Underlying fundamentals in the three audited years are
  solid: near-net-cash balance sheet, 22% ROCE, positive cumulative
  CFO/PAT, and now a demonstrated cost/margin advantage versus the closest
  listed comparators — sitting under flat growth and a FY26 cash-conversion
  wobble that LBF-1's Q1 FY27 print (if it holds up) would be the first
  data point against.

---

## DECISION LINE

Gate 0 mechanical classification: **AVOID** (pledge deal-breaker caps at
AVERAGE; 3-year LIMITED-history downgrade pulls one tier further to
AVOID). Flags propagate; this does not halt the run. Historical
depressors are named above (flat 3-year growth, FY26 cash-conversion
deterioration, near-total promoter pledge, short listed history) for the
operator to weigh against a moat block that, once correctly peer-scored,
reads STRONG (5 of 12 tests, 22/60) rather than MODERATE — and against the
Q1 FY27 inflection claim this run exists to test.
