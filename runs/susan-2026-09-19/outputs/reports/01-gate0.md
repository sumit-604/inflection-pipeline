# STAGE 1 — GATE 0 QUANTITATIVE SCORECARD
Susan Electricals India Ltd (SUSAN) | BSE SME 544793 | Run date 2026-09-19

Data available: 6 years for revenue and balance sheet raw figures (FY21 to
FY26, screener-data). 3 years for audited/restated ratios (FY24 to FY26,
RHP Annexure 33, cross-verified against AR FY26 standalone balance sheet).
4 years for cash flow (FY23 to FY26, screener-data for FY23; RHP Annexure 3
for FY24-FY26). Scoring adapted per metric to the years each source
actually carries; the company listed 18-Jun-2026, so no pre-restatement
statutory financials beyond screener's own scrape exist for FY21-FY23.

UNIT NOTE: RHP and AR figures are in INR Lakhs; screener and CRISIL are in
INR Cr. Conversions are shown explicitly at each figure (100 Lakhs = 1 Cr).

## LOAD-BEARING FACTS CHECK (first priority, per orchestrator brief)

- LBF1 (margin reconciliation 1.7% FY23 to ~12% FY26): CONFIRMED IN FILINGS.
  RHP Annexure 33 (p.234) gives EBITDA margin 3.51% FY24, 8.84% FY25, 11.91%
  FY26 (screener/RHP definition: EBITDA = PAT + tax + depreciation + finance
  cost − other income). Q1 FY27 result (results p.2) computes to ~11.9%
  (EBITDA 1,137.34 Lakhs / Revenue 9,535.68 Lakhs), so the ~12% run-rate has
  continued one quarter post-listing. The orchestrator's cited "1.7% FY23"
  figure is NOT independently in the corpus (RHP restates only FY24-26); the
  earliest margin this run can anchor is FY24's 3.51%. Gate 0 cannot verify
  a segment-EBITDA (6.5% LT / 7% HT) breakdown against the ~12% company
  figure: no segment P&L is in the Data_Sheet, RHP, AR or Q1 FY27 result.
  This reconciliation needs stage 2+ (RHP business section / concall) to
  separate manufacturing margin from the 38.8% trading-revenue line, which
  by definition carries much thinner unit margin. Flagged forward, not
  resolved here.
- LBF2 (cash conversion, FY26 CFO ~-Rs10 Cr on PAT Rs18.25 Cr; borrowings
  Rs24.8 Cr FY24 to Rs66.7 Cr FY26): CONFIRMED IN FILINGS, exactly.
  RHP Annexure 3 (p.55): FY26 CFO = -971.42 Lakhs = -Rs9.71 Cr (screener-data
  matches: -9.71). FY26 PAT = 1,824.64 Lakhs = Rs18.25 Cr (screener-data:
  18.25). Borrowings: screener-data FY24 = Rs24.79 Cr, FY26 = Rs66.72 Cr
  (RHP capitalisation statement p.233: total debt 6,671.70 Lakhs = Rs66.72
  Cr). CRISIL rationale (p.1) separately names "high working capital cycle"
  as a rated weakness, corroborating from a third source. See Block B below
  for the WC-days math behind this.
- LBF3 (revenue quality: trading ~38.8% of 9M FY26; government 90.6% FY24
  to 35.8% FY26; RPTs): PARTIALLY IN CORPUS. RHP (p.[near line 1704])
  gives "Total Revenue from Traded Products" as 38.38% of FY26 revenue
  (10,337.16 / 26,935.66 Lakhs) — this is the FULL FY26 figure, not the 9M
  figure the brief cites, but it lands at the same ~38-39%, so directionally
  CONFIRMED. The government-share glide path (90.6% to 35.8%) and named RPT
  counterparties (Vishal Jain, Mahak Jain, Subhash Jain, SMV Enterprises
  appear in RHP related-party annexures, e.g. p.[near line 14700]) are
  present in the RHP but a government-vs-private revenue SPLIT BY YEAR is
  not in the Data_Sheet, AR or Q1 result read for this stage; it needs a
  targeted RHP customer-concentration section read at stage 2/3. Not
  scored in Gate 0 (no numeric field maps to it).
- LBF4 (guidance vs delivery, HT/MVCC to ~50% of revenue by end FY27;
  12,000 km by Feb 2027): NOT A GATE-0 METRIC. This is a forward guidance
  item, not a scoreable historical financial. Deferred to stage 5/9
  (promise-to-delivery testing). Q1 FY27 result carries no product-mix
  breakdown to check against it here.

## BLOCK A: RETURN ON CAPITAL (max 20) — score 14

RHP Annexure 33 (Restated Statement of Accounting & Other Ratios, p.234)
gives the company's own ROCE and ROE; per the formula rule this is used
directly rather than recomputed. FY21-FY23 ROCE/ROE are marked N/A: screener
Data_Sheet's Balance Sheet section does not split Current Liabilities from
Borrowings/Other Liabilities for those years, so EBIT/(Total Assets − CL)
cannot be computed without estimating a missing split (not done, per rule).

| Year | ROCE (RHP) | ROE (RHP, "Return On Equity") |
|---|---|---|
| FY24 | 9.47% (RHP p.234) | 15.92% (RHP p.234) |
| FY25 | 17.46% (RHP p.234) | 46.72% (RHP p.234) |
| FY26 | 29.05% (RHP p.234) | 64.64% (RHP p.234) |

- A1 Median ROCE (3 yrs) = 17.46% (RHP p.234) → band 15-19.9% → **score 3**
- A2 Minimum single-year ROCE = 9.47% FY24 (RHP p.234) → band 8-11.9% →
  **score 1**
- A3 Median ROE = 46.72% (RHP p.234) → band ≥20% → **score 5**
- A4 ROCE trend, latest (29.05% FY26) vs earliest (9.47% FY24) (RHP p.234):
  latest ≥ earliest → **score 5**

Block A = 3+1+5+5 = **14/20**

## BLOCK B: CASH GENERATION QUALITY (max 20) — score 0

CFO (RHP Annexure 3 p.55, cross-verified screener-data): FY23 = Rs4.44 Cr
(screener-data only, RHP restatement does not cover FY23); FY24 = -549.22
Lakhs = -Rs5.49 Cr; FY25 = -1,839.33 Lakhs = -Rs18.39 Cr; FY26 = -971.42
Lakhs = -Rs9.71 Cr. PAT (same sources): FY23 = Rs0.72 Cr; FY24 = 75.58
Lakhs = Rs0.7558 Cr; FY25 = 565.10 Lakhs = Rs5.651 Cr; FY26 = 1,824.64
Lakhs = Rs18.2464 Cr.

- B1 Cumulative CFO ÷ Cumulative PAT (FY23-FY26) = (444 − 549.22 − 1,839.33
  − 971.42) ÷ (72 + 75.58 + 565.10 + 1,824.64) Lakhs = -2,915.97 ÷ 2,537.32
  = **-1.15** → band <0.50 → **score 0**
- B2 FCF-positive years as proportion: FCF = CFO − Capex (purchase of fixed
  assets, RHP Annexure 3 line "Purchase of Fixed Assets including capital
  advance" for FY24-26; screener-data total investing-activity outflow used
  as a capex PROXY for FY23 only, since screener does not break out capex
  separately that year — flagged as a proxy, not a strict capex figure).
  FY23: CFO 444 − capex-proxy 309 = **+135 Lakhs (positive)**.
  FY24: -549.22 − 424.06 = **-973.28 Lakhs (negative)**.
  FY25: -1,839.33 − 159.47 = **-1,998.80 Lakhs (negative)**.
  FY26: -971.42 − 427.30 = **-1,398.72 Lakhs (negative)**.
  1 of 4 years positive = 25% → band <50% → **score 0**
- B3 Cumulative FCF ÷ Cumulative PAT = (135 − 973.28 − 1,998.80 − 1,398.72)
  ÷ 2,537.32 = -4,235.80 ÷ 2,537.32 = **-1.67** → band <0.20 or negative →
  **score 0**
- B4 Change in WC Days, latest (FY26) vs earliest with a full breakdown
  (FY24). Basis: revenue (Trade Payables not separately reported in
  screener; used RHP Annexure 1, p.51, for FY24-26).
  Receivable Days = TR/Revenue×365; Inventory Days = Inventory/Revenue×365;
  Payable Days = Payables/Revenue×365 (all Lakhs, RHP p.51 and p.53).
  | Year | Receivable days | Inventory days | Payable days | WC days |
  |---|---|---|---|---|
  | FY24 | 45.96 | 36.84 | 22.16 | 60.64 |
  | FY25 | 67.37 | 77.07 | 20.86 | 123.58 |
  | FY26 | 62.74 | 68.65 | 25.43 | 105.96 |
  Change FY26 vs FY24 = +45.32 days (worse) → band increased >15 days →
  **score 0**

Block B = 0+0+0+0 = **0/20**. This is the weakest block by a wide margin and
is the numeric backbone of LBF2: three years of restated cash flow show CFO
below PAT in every year (FY24-26), and FCF negative in three of four years
including the two largest (FY25, FY26), against borrowings that nearly
tripled (Rs24.8 Cr to Rs66.7 Cr) over the same window.

block_b_trend: **deteriorating**. The one number that shows it: WC days
rose from 60.64 (FY24) to 123.58 (FY25) before easing to 105.96 (FY26),
net +45.32 days over the two-year restated window, while CFO stayed
negative all three years.

## BLOCK C: GROWTH (max 20) — score 20

Revenue (screener-data, Cr): FY21 48.59, FY22 54.77, FY23 78.38, FY24
102.73, FY25 135.44, FY26 268.91. PAT (screener-data, Cr): FY21 0.08, FY22
0.32, FY23 0.72, FY24 0.76, FY25 5.65, FY26 18.25.

- C1 Revenue CAGR (FY21→FY26, 5 yrs) = (268.91/48.59)^(1/5)-1 = **40.8%**
  (screener-data) → band ≥20% → **score 5**
- C2 PAT CAGR (FY21→FY26, 5 yrs) = (18.25/0.08)^(1/5)-1 = **~196%**
  (screener-data) → mechanically ≥20% → **score 5**. FLAGGED: the FY21
  base (Rs0.08 Cr = Rs8 Lakhs PAT) is a near-zero starting point for what
  was then a small private company; this CAGR is a base-effect artifact,
  not a read on sustainable earnings growth. See data_notes.
- C3 Positive YoY revenue years = 5 of 5 transitions (FY22 through FY26 all
  grew over the prior year, screener-data) = 100% → **score 5**
- C4 PAT CAGR minus Revenue CAGR = 196% − 40.8% = **+155pp** → band ≥+3pp →
  **score 5**. Same base-effect caveat as C2 applies with more force here:
  this delta is arithmetically correct but not an operating-leverage
  signal at this magnitude.

Block C = 5+5+5+5 = **20/20**, entirely driven by a five-year span that
starts at a near-shell-scale FY21 base. See analyst_note.

## BLOCK D: BALANCE SHEET STRENGTH (max 20) — score 5

Latest = FY26. Borrowings Rs66.72 Cr, Cash Rs0.85 Cr (screener-data) → Net
Debt = Rs65.87 Cr. EBITDA FY26 = 3,208.22 Lakhs = Rs32.08 Cr (RHP "Other
Financial Information", p.239). Interest FY26 = Rs6.55 Cr (screener-data,
matches RHP Finance Cost 654.76 Lakhs). EBIT FY26 = EBITDA − Depreciation =
3,208.22 − 152.00 = 3,056.22 Lakhs = Rs30.56 Cr.

- D1 Net Debt ÷ EBITDA = 65.87 / 32.08 = **2.05x** → band 2-3x → **score 1**
- D2 Interest Coverage = EBIT ÷ Interest = 30.56 / 6.55 = **4.67x** → band
  3-4.9x → **score 2**
- D3 Debt ÷ Equity FY26 = **1.73x** (RHP Annexure 33 p.234, source's own
  figure) → band >1.5x → **score 0**
- D4 Current Ratio FY26 = **1.22** (RHP Annexure 33 p.234, source's own
  figure) → band 1.2-1.49 → **score 2**

Block D = 1+2+0+2 = **5/20**. Deal-breaker #6 (ND/EBITDA>3x AND IC<3x →
AVOID) does NOT trigger: ND/EBITDA is 2.05x, under the 3x threshold, even
though D/E and current ratio are both weak.

## BLOCK E: SHAREHOLDER ALIGNMENT (max 20) — score 13

Source: BSE shareholding pattern as on 17-Jun-2026 (pre-listing snapshot,
filed the day before the 18-Jun-2026 listing; this is the ONLY shareholding
filing in the corpus — no post-listing SHP exists yet, per input_gaps).

- E1 Promoter holding (latest available) = **66.97%** (Vishal Jain, sole
  promoter; SHP Table I, row A) → band ≥60% → **score 5**
- E2 Promoter holding change over 3 years: **N/A (not in provided data)** —
  the company was private before this IPO; no prior filed shareholding
  pattern exists to compare against, and the RHP does not carry a
  quantified pre-offer-vs-3-years-ago promoter percentage in the sections
  read for this stage. **score 0**
- E3 Promoter pledge (latest) = **0%** (SHP declaration Q7: "Whether any
  shares held by promoters are encumbered under 'Pledge'? No") → **score 5**
- E4 Contingent liabilities ÷ Net Worth (FY26) = 480.49 Lakhs ÷ 3,847.74
  Lakhs (RHP Annexure 36, p.236; Net Worth per RHP Annexure 1, p.51) =
  **12.49%** → band 5-15% → **score 3**

Block E = 5+0+5+3 = **13/20**

## BLOCK F: QUANTITATIVE MOAT SCORING (max 60) — score 21

Peer data is thin: the only peer screener file that downloaded is DIACABS
(Diamond Power Infrastructure), a post-CIRP name carrying negative reserves
(-Rs656.9 Cr FY26) and revenue an order of magnitude smaller than SUSAN
(Rs19.1 Cr FY26 vs Rs268.9 Cr) — not a usable margin/scale peer. DYCL and
VIDYAWIRES screener sheets did not download (input_gaps). Every test that
needs a peer median is therefore marked PEER DATA NEEDED and scored 0.

- M1 Pricing Power: EBITDA margin FY24→FY26 +8.4pp (3.51%→11.91%, RHP
  p.234) AND revenue CAGR FY24→FY26 61.3% (screener-data) → both conditions
  met at the top band → **score 5**. Caveat: LBF1 flags this expansion may
  partly reflect trading/other-income mix, not pure manufacturing pricing
  power; unresolved at Gate 0 (see LBF1 note above).
- M2 Cost Advantage vs peer median EBITDA margin: **PEER DATA NEEDED** →
  **score 0**
- M3 Capital Efficiency: FAT = Revenue/Net Block = 26,935.66/1,282.82 =
  **21.0x** (RHP, both in Lakhs) AND ROCE 29.05% > 20% → top band → **score
  5**. Caveat: FAT this high is unusual for a cable manufacturer and is
  inflated by the 38.8% trading-revenue line, which needs almost no fixed
  assets; this is not solely manufacturing capital efficiency.
- M4 Customer Stickiness: zero revenue-decline years (screener-data, all
  6 years) is met, but receivable days are NOT stable within ±10 (45.96→
  67.37→62.74 days, RHP p.51/53, a 21.4-day swing). The rubric's lower
  bands are defined by decline-year counts (1, 2, 3+), none of which apply
  here (we have zero declines). Judgment call, recorded as a rubric-fit
  gap, not a shaded input: **score 3** (best-fit, not a clean 5).
- M5 Scale & Dominance: **PEER DATA NEEDED** (no peer market-cap data) →
  **score 0**
- M6 Technology/R&D: no R&D expense line is disclosed anywhere in the
  corpus for SUSAN → **N/A (not in provided data)**, **score 0**
- M7 Regulatory/License: wires/cables/conductors manufacturing has well
  over 10 listed players (Polycab, KEI, Havells, Finolex, RR Kabel,
  Universal Cables, Apar, Dynamic Cables, Diamond Power, Vidya Wires and
  more; general industry knowledge, not a scored input) → unregulated-
  scarcity band → **score 0**
- M8 Distribution: no company-specific dealer/distributor count or reach
  is disclosed in the RHP business section read for this stage; the RHP
  describes the trading segment as populated by manufacturers, stockists,
  dealers and traders generally, not SUSAN's own network → **score 0**
- M9 Brand: **PEER DATA NEEDED** (no peer gross-margin median) → **score 0**
- M10 Switching Costs: revenue grew every year (screener-data, 0 decline
  years) but receivable days rose 45.96→62.74 = +16.78 days over FY24-26
  (RHP p.51/53), above the ≤10-day top-band threshold. Same rubric-fit gap
  as M4: **score 3** (best-fit judgment call, flagged).
- M11 Network Effects (6-year window available, meets the ≥6yr test
  threshold): latest-3yr window CAGR (FY24→FY26, 2 yrs) = 61.8% vs
  prior-3yr window CAGR (FY21→FY23, 2 yrs) = 27.0% (screener-data), latest >
  prior; selling & admin expense as % of revenue fell FY24 (2.76%) → FY26
  (1.91%) (screener-data) → top band met → **score 5**. Caveat: "network
  effects" as a construct does not fit a cable/wire manufacturing-and-
  trading archetype; this is a mechanical pass on a test built for
  platform businesses. Flagged for downstream discount.
- M12 Negative WC/Float: WC days were 60.64/123.58/105.96 (FY24-26,
  computed above), all >45 days → **score 0**

moats_confirmed (score ≥3): M1, M3, M4, M10, M11 = **5**
Block F = 5+0+5+3+0+0+0+0+0+3+5+0 = **21/60**
moat_class band: 4-5 present → **STRONG** — but see analyst_note: two of
the five confirmed tests (M4, M10) are rubric-fit judgment calls at the
minimum "present" threshold (3), not clean top-band passes, and a third
(M11) tests a construct that does not fit the archetype. Read STRONG with
real caution; three PEER DATA NEEDED gaps (M2, M5, M9) mean the moat
picture is unverified on cost position, competitive scale and brand.

## CLASSIFICATION

Core score = A(14) + B(0) + C(20) + D(5) + E(13) = **52/100**
Moat score = **21/60**, moats_confirmed = **5** → moat_class **STRONG**

Data confidence: the raw P&L/balance-sheet span is 6 years (FY21-FY26),
placing this in the "5-6 years, lower confidence, flag may not have seen
full cycle" band. The audited/restated RATIOS that drive Block A and half
of Block D exist for only 3 years (FY24-FY26); FY21-FY23 come only from
screener's own scrape with no ratio detail and predate the RHP restatement.
**history_downgrade: true** — flagged for this reason, not because the
overall span triggers the "3-4yr, downgrade one tier" rule (it does not,
at 6 years of raw data). Treat Block A and D as thinner-evidenced than
Blocks C's 6-year span suggests.

Classification matrix: Core 52 falls in the 40-59 bracket → **AVERAGE**,
independent of moat class at this bracket.

Deal-breaker overrides triggered (recorded per rule; both cap at or below
the already-computed AVERAGE, so neither changes the outcome, but both are
real and are named as instructed):
- #2 Block B < 8 (actual: 0) → caps at max GOOD. No effect (already below).
- #4 Cumulative CFO/PAT < 0.50 (actual: -1.15) → caps at max AVERAGE.
  Reinforces the Core-score-driven AVERAGE.

Deal-breakers NOT triggered: #1 (Block A=14, not <8), #3 (median ROCE
17.46%, not <10%), #5 (pledge 0%, not >15%), #6 (ND/EBITDA 2.05x, not
>3x — IC/ND combination test does not fire), #7 (revenue never declined),
#8 (PAT positive all of last 3 years), #9 (history is 6 years, not <3).

**FINAL CLASSIFICATION: AVERAGE**

## STRONGEST / WEAKEST BLOCK

- Strongest: Block C (Growth), 20/20 — but flagged as base-effect inflated
  (FY21 PAT of Rs8 Lakhs makes the 5-year PAT CAGR arithmetically ~196%,
  not operationally meaningful).
- Weakest: Block B (Cash Generation Quality), 0/20 — CFO has trailed PAT
  in every one of the last three restated years, FCF was negative in three
  of the last four years, and borrowings nearly tripled (Rs24.8 Cr to
  Rs66.7 Cr, FY24-FY26) over the same window. This is the numeric core of
  LBF2 and is corroborated by CRISIL's own rated weakness, "high working
  capital cycle" (CRISIL rationale p.1).

## DECISION LINE

Gate 0 mechanical score: AVERAGE. The company posts genuine and fast top-
line and margin growth (Block C, and the LBF1-consistent margin path) off
a very small base, funded so far by a near-tripling of borrowings against
consistently negative operating cash flow (Block B, LBF2). Nothing here
halts the pipeline — Gate 0 does not carry a STOP verdict — but Block B and
the base-effect caveat on Block C are the two facts stage 2 onward should
carry forward without dilution.
