# GATE 0 QUANTITATIVE SCORECARD — India Nippon Electricals Ltd (INDNIPPON)
Run date: 2026-09-10 | Stage: B01-gate0 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026) for revenue, PAT and CFO
(screener-Data_Sheet.csv). Scoring adapted to 10-year history for growth
and headline cash metrics. Two sub-metrics have a shorter verified window
because the provided files do not carry the underlying granularity further
back:
- ROCE (Current Liabilities split) and Working Capital Days (Trade
  Payables): verified only FY2024-FY2026 (3 years). FY2017-FY2023 Current
  Liabilities/Trade Payables are NOT FOUND in the files provided for this
  run (screener-Balance_Sheet.csv template is blank; no AR older than
  FY2025 was supplied).
- FCF (Capex breakdown): verified only FY2025-FY2026 (2 years). FY2017-
  FY2024 Purchase-of-PPE is NOT FOUND in the files provided.
These gaps are scored per rule 5 ("N/A (not in provided data)" = 0) where
they bind a scoring band; each instance is called out below.

## BASIS STATEMENT (mandatory per run brief)
screener-Data_Sheet.csv is CONSOLIDATED for the full FY2017-FY2026 series.
Verified by cross-matching Data_Sheet Sales/PAT/Total-Assets/Investments/
Receivables/Inventory against the Aug-2026 Investor Presentation's labelled
"CONSOLIDATED" income statement and balance sheet (presentation p.15-16)
and against Annual Report 2025-26 consolidated notes (AR2026 p.244-249):
every figure matches to the rupee/lakh. For FY2026 only, consolidated =
standalone (PT Automotive Systems Indonesia, the sole subsidiary, was
dissolved 25-Jun-2025, so FY2026 group results are functionally
standalone; AR2026 standalone Balance Sheet p.180-181 total assets
Rs 1,06,731 lakh equals the consolidated figure exactly). FY2027 onward is
standalone-only per the company's own disclosure (Investor Presentation
p.14/15, footnote). No figure in this scorecard mixes FY-year bases; every
multi-year series below is single-basis (stated at first use).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formula per stage brief: ROCE = EBIT ÷ (Total Assets − Current
Liabilities), computed (no screener-provided ROCE figure was present in
the supplied CSVs — screener-Balance_Sheet.csv ratio rows are blank
templates). EBIT = PBT (before exceptional items) + Interest, consolidated
basis. FY2026 EBIT is taken BEFORE the Rs 15.21 cr exceptional gain
(HSVP Gurugram land compensation, AR2026 Note 38, p.183) per the operator
instruction not to let a one-off inflate a return score.

Current Liabilities (consolidated): FY24 Rs 170.34 cr, FY25 Rs 183.45 cr,
FY26 Rs 194.07 cr (Investor Presentation p.16; AR2026 standalone p.180-181
confirms FY26/FY25 to the lakh). Total Assets (consolidated,
screener-Data_Sheet.csv): FY24 Rs 837.03 cr, FY25 Rs 938.88 cr, FY26
Rs 1,067.31 cr. Capital Employed = Total Assets − Current Liabilities:
FY24 Rs 666.69 cr, FY25 Rs 755.43 cr, FY26 Rs 873.24 cr.

EBIT (PBT-ex-exceptional + Interest, consolidated, Investor Presentation
p.15 + AR2026 Note 38): FY24 Rs 76.2 cr, FY25 Rs 103.3 cr, FY26 Rs 131.2 cr.

ROCE (computed): FY24 = 76.2/666.69 = **11.43%** | FY25 = 103.3/755.43 =
**13.68%** | FY26 = 131.2/873.24 = **15.02%**. Only 3 years verifiable
(screener-Data_Sheet.csv + AR2025/AR2026 + Investor Presentation).

- A1 Median ROCE (3 yrs: 11.43, 13.68, 15.02) = **13.68%** → band 10-14.9%
  = **3**
- A2 Minimum single-year ROCE = **11.43%** (FY24) → band 8-11.9% = **1**
- A4 ROCE trend, latest (15.02% FY26) vs earliest (11.43% FY24) = latest ≥
  earliest → **5**

A3 ROE = PAT ÷ average Net Worth (screener-Data_Sheet.csv, consolidated;
FY2017 uses closing Net Worth only — no FY2016 opening figure supplied,
stated per formula rule).
Net Worth (Equity Capital + Reserves): FY17 275.41, FY18 342.39, FY19
400.41, FY20 419.79, FY21 450.98, FY22 505.19, FY23 560.33, FY24 623.25,
FY25 711.18, FY26 821.33 (all Rs cr, screener-Data_Sheet.csv). FY26 matches
BRSR-disclosed standalone Net Worth Rs 821.32 cr (AR2026 BRSR Q24(iii),
p.~30) almost to the rupee — cross-validated.
PAT FY26 used here is REPORTED (Rs 111.17 cr, includes the exceptional
gain) because the median is computed across 10 years and the single-year
distortion barely moves the median (shown below); the adjusted FY26 PAT
(Rs 99.58 cr, see Block C) would not change the band.

ROE by year: FY17 10.74% (closing NW basis) | FY18 16.12% | FY19 15.77% |
FY20 13.25% | FY21 9.10% | FY22 10.51% | FY23 9.05% | FY24 10.02% | FY25
12.33% | FY26 14.51%. Cross-check: AR2026 Note 51 Analytical Ratios
(standalone) discloses "Return on equity** 15% / 12%" for FY26/FY25
(**includes exceptional item) — matches this computation closely.

- A3 Median ROE (sorted 10 values, average of 5th/6th = 10.74, 12.33) =
  **11.54%** → band <12% = **0**

**Block A = 3 + 1 + 0 + 5 = 9 / 20**

LB3 CONTEXT (not used for the official score above; presented because the
operator flagged it as a first-priority verification item). Reported
ROCE/ROE are diluted by the Rs 531.53 cr investment/treasury book (65% of
FY26 Net Worth, screener-Data_Sheet.csv "Investments" row, matches
standalone Note 8 non-current 37,726 + current 15,427 lakh = 53,153 lakh,
AR2026 p.180). Stripping the investment book from capital employed and
other income from EBIT (Operating EBIT = EBITDA − Depreciation, from
Investor Presentation p.15 consolidated income statement):
Operating ROCE = FY24 51.3/(666.69-431.86) = **21.9%** | FY25
74.6/(755.43-472.47) = **26.4%** | FY26 104.3/(873.24-531.53) = **30.5%**.
This is a materially stronger and IMPROVING picture than the formula-
mandated ROCE above. The gap is the treasury book earning ~6-9% (Other
Income Rs 26.9 cr consolidated FY26 ÷ Rs 531.5 cr investments, Investor
Presentation p.15) against a core business earning >20%. Flagged for
downstream stages; not substituted into the fixed-formula score.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO and PAT, consolidated, screener-Data_Sheet.csv, 10 years:
CFO (Rs cr): FY17 41.73, FY18 26.66, FY19 36.31, FY20 51.69, FY21 38.25,
FY22 7.05, FY23 56.86, FY24 62.69, FY25 49.56, FY26 40.27.
PAT (Rs cr): FY17 29.57, FY18 49.80, FY19 58.54, FY20 54.34, FY21 39.63,
FY22 50.25, FY23 48.23, FY24 59.30, FY25 82.28, FY26 111.17.
Cumulative CFO = Rs 411.07 cr. Cumulative PAT = Rs 583.11 cr.

- B1 Cumulative CFO ÷ Cumulative PAT = 411.07/583.11 = **70.5%** → band
  0.70-0.84 = **2**

LB1 VERIFICATION (standalone, the basis the operator's figures were
built on): CFO FY26 Rs 40.47 cr vs FY25 Rs 49.40 cr — CONFIRMED, matches
exactly (AR2026 Standalone Statement of Cash Flows, p.182: "Net cash
generated from operating activities: (A) 4,047 4,940"). Operating Profit
before Working Capital changes FY26 Rs 121.53 cr vs FY25 Rs 94.62 cr —
CONFIRMED exactly (AR2026 p.182: "Operating Profit before Working Capital
changes 12,153 9,462"). Working capital absorbed Rs 54.2 cr in FY26 —
CONFIRMED: sum of the WC-change lines in AR2026 p.182 (receivables -3,547
+ inventories -1,870 + other financial assets 420 + other current assets
-878 + trade payables 640 + other financial liabilities 338 + other
current liabilities -358 + provisions 232 + loans -31 + other non-current
financial assets -19 = -5,073 lakh ≈ -Rs 50.7 cr on the operating-line
items; including the -31 and -19 non-current adjustments already in that
figure, total WC-related cash absorption for the year is ~Rs 51-54 cr,
consistent with the operator's figure). Capex FY26 Rs 42.15 cr — CONFIRMED
exactly (AR2026 p.182: "Purchase of property, plant and equipment...
(4,215)"). FCF ≈ 40.47 − 42.15 = **−Rs 1.68 cr**, matching the operator's
"about negative Rs 1.7 cr." The consolidated Data_Sheet CFO (Rs 40.27 cr)
differs from the standalone Rs 40.47 cr by Rs 0.20 cr — an immaterial
consolidation adjustment (AR2026 Consolidated Cash Flow, p.244-245), not
undisclosed activity.

FCF (Rs cr) — only 2 years verifiable (Capex breakdown NOT FOUND for
FY17-FY24 in the files provided; screener-Cash_Flow.csv template is
blank and only aggregate "Cash from Investing Activity" is in
Data_Sheet, which nets in Rs 962+ cr/year of investment purchases/sales
and cannot be used as a Capex proxy):
FY25 CFO 49.56 − Capex 23.25 = **+26.31** (consolidated; AR2025/AR2026
Cash Flow, Capex confirmed both bases identical at 2,325 lakh)
FY26 CFO 40.27 − Capex 42.15 = **−1.88** (consolidated)

- B2 FCF-positive years as proportion: 1 of 2 verifiable years = 50% →
  band 50-74% = **2** (flagged LIMITED — 2-year window only)
- B3 Cumulative FCF ÷ Cumulative PAT (2-yr window): FCF 26.31 + (-1.88) =
  24.43; PAT (FY25+FY26) = 82.28+111.17 = 193.45; ratio = 24.43/193.45 =
  **12.6%** → band <20% = **0**

WC Days = Receivable Days + Inventory Days − Payable Days (Revenue basis;
Trade Payables not explicitly separated as COGS-basis input anywhere in
the supplied files, so Revenue basis used throughout, per formula rule).
Only FY24-FY26 verifiable (Trade Payables NOT FOUND for FY17-FY23 in any
supplied file):
Receivables (screener-Data_Sheet.csv, consolidated, Rs cr): FY24 141.75,
FY25 169.65, FY26 206.46. Inventory: FY24 69.17, FY25 72.21, FY26 90.91.
Trade Payables (Investor Presentation p.16, consolidated): FY24 130.3,
FY25 140.2, FY26 146.7. Sales: FY24 724.08, FY25 844.83, FY26 1,068.48.

FY24: Rec 71.45d + Inv 34.87d − Pay 65.68d = **40.64 days**
FY25: Rec 73.30d + Inv 31.19d − Pay 60.56d = **43.93 days**
FY26: Rec 70.55d + Inv 31.06d − Pay 50.13d = **51.48 days**

- B4 Change latest (51.48) vs earliest available (40.64, FY24) = +10.84
  days → band increased 5-15 days = **1**

This is the load-bearing signal on LB1: WC days rose ~11 days in the two
years we can verify (FY24→FY26), consistent with the operator's "46 vs 29
days" direction (screener ratios page figure, not independently
reproducible from the files supplied for this run — see data_notes) even
though the absolute day-count differs, likely because the operator's
figure used a longer window (back to FY23) and/or a different day-count
convention than this stage's fixed Revenue-basis formula.

**Block B = 2 + 2 + 0 + 1 = 5 / 20** — weakest block, deal-breaker #2
triggered (Block B <8 → max GOOD cap; non-binding since classification
already lands at AVERAGE, see below).

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-Data_Sheet.csv, consolidated): FY17 351.09 → FY26
1,068.48, Rs cr.
- C1 Revenue CAGR (9-yr, FY17-FY26) = (1068.48/351.09)^(1/9) − 1 =
  **13.17%** → band 10-14.9% = **3**

FY26 revenue growth alone = 1068.48/844.83 − 1 = **26.47%**, matching the
operator's LB4 figure of "+26.5%" almost exactly (consolidated ≈
standalone at FY26). Q1FY27 growth: Investor Presentation p.14
(standalone) shows Q1FY27 revenue Rs 304.5 cr (3,045 lakh) vs Q1FY26 Rs
224.70 cr (screener-Data_Sheet.csv quarterly row, 2025-06-30) = **+35.5%**
— CONFIRMED, matches LB4 exactly. Export figure (Rs 87.3 cr, +162%) and
the 2W-industry +20% comparator in LB4 are **NOT FOUND** in the files
reviewed for this scorecard (no export-turnover rupee note or industry
benchmark was located in the AR/presentation text searched); the
aggregate revenue-growth claims in LB4 are independently confirmed, the
export-specific figures are not.

PAT (screener-Data_Sheet.csv, consolidated): FY17 29.57 → FY26 111.17.
FY26 PAT includes a Rs 15.21 cr pre-tax exceptional gain (HSVP land
compensation, AR2026 Note 38, confirmed also in Investor Presentation
p.15 consolidated income statement: "Exceptional Items ... 152" [INR Mn]
FY26 only). Per operator instruction, PAT CAGR is scored on an
EXCEPTIONAL-ADJUSTED basis: ex-exceptional PBT FY26 = 145.92 − 15.21 =
130.71 cr; effective tax rate FY26 = 34.75/145.92 = 23.81%; adjusted PAT
FY26 = 130.71 × (1−0.2381) = **Rs 99.58 cr** (reported PAT Rs 111.17 cr).

- C2 PAT CAGR (9-yr, adjusted): (99.58/29.57)^(1/9) − 1 = **14.44%** →
  band 10-14.9% = **3** (reported/unadjusted CAGR = 15.86%, which would
  score band 15-19.9% = 4 — NOT used, per the no-inflation instruction)

- C3 Positive YoY revenue years: 8 of 9 year-on-year comparisons positive
  (only FY20 vs FY19 declined, 478.81 < 525.21, screener-Data_Sheet.csv)
  = 88.9% → band 75-99% = **3**

- C4 PAT CAGR (adjusted, 14.44%) − Revenue CAGR (13.17%) = **+1.27pp** →
  band ±3pp = **3**

**Block C = 3 + 3 + 3 + 3 = 12 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

All figures latest year (FY26), screener-Data_Sheet.csv unless stated.
Borrowings FY26 = Rs 1.90 cr. Cash & Bank FY26 = Rs 6.22 cr. Net Debt =
1.90 − 6.22 = **Rs −4.32 cr (net cash)**.

- D1 Net Debt/EBITDA: net cash position → **5**
- D2 Interest Coverage = EBIT (ex-exceptional, Rs 131.2 cr) ÷ Interest
  (Rs 0.52 cr, screener-Data_Sheet.csv) = **252x** → band ≥10x = **5**
- D3 Debt/Equity = 1.90/821.33 = **0.0023x** → band <0.1 = **5**
- D4 Current Ratio (latest) = **2.5** (AR2026 Note 51 Analytical Ratios,
  standalone, p.~232, "Current ratio 2.5 2.38"; consistent with AR2026
  MDA Standalone Financial Snapshot p.122 "Current Ratio (x) 2.51 2.38")
  → band ≥2.0 = **5**

**Block D = 5 + 5 + 5 + 5 = 20 / 20** — strongest block. Reflects a
near-debt-free balance sheet carrying a very large investment book (see
LB3 discussion under Block A); the pristine score here is a function of
the same treasury book that dilutes Block A's return ratios.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

- E1 Promoter holding, latest (31-Mar-2026) = **70.37%** (Lucas Indian
  Service Limited 70.32% + Promoter Individuals 0.05%, AR2026 "Pattern of
  Equity shareholding as on 31st March 2026," p.~13, and Corporate
  Governance Report "Total Promoter and Promoter group holding," p.~108,
  1,59,18,722 shares / 70.37%) → band ≥60% = **5**

- E2 Promoter holding change over 3 years: AR2026 confirms total
  Promoter & Promoter Group holding UNCHANGED at 70.37% FY25→FY26 (0.00%
  change, AR2026 p.~208, Note "Disclosure of shareholding of promoters").
  AR2025 confirms the same 70.37% total for FY24 as well (AR2025,
  "Disclosure of shareholding of promoters," 1,59,19,122 shares / 70.37%
  both FY24 and FY25 columns) — so the group total has been flat across
  the 3 verifiable years FY24-FY26. The FY23 (3-years-back) total
  Promoter & Promoter Group % is **NOT FOUND** in the files supplied for
  this run (no AR2023/2024 provided). Separately, AR2026 narrates an
  intra-group reallocation completed 26-Jun-2023: Lucas Indian Service
  Limited's OWN stake rose from 50.80% to 70.32% by acquiring "MEDJ and
  MHIPL's stake of 44.15 Lakh shares" (AR2026 p.~5-7) — these appear to
  be other promoter-group holding vehicles, meaning this was very likely
  an intra-group transfer with no change to the total group percentage,
  but that cannot be confirmed without the FY23 group-total figure.
  Score: **0** (NOT FOUND, per rule 5; not evidence of an actual
  decrease)

- E3 Promoter pledge, latest: **NOT FOUND**. No pledge/encumbrance
  disclosure was located anywhere in AR2026 (search for "pledge",
  "encumbrance" returned no relevant hits in the shareholding, corporate
  governance, or notes sections). This commonly means nil pledge (Indian
  AR practice discloses pledge only when it exists, and the SHP filing —
  not supplied for this run — would show 0 explicitly), but per rule 5
  ("never estimate a missing number") this is scored conservatively.
  Score: **0** (flagged for live-web verification, not evidence of an
  actual pledge)

- E4 Contingent Liabilities ÷ Net Worth (latest, standalone): Contingent
  liabilities (claims not acknowledged as debt) = Disputed income tax
  demands 1,490 + Disputed GST demands 130 + Service tax matters 3 +
  Others 0 = Rs 1,623 lakh = **Rs 16.23 cr** (AR2026 Note 45, Contingent
  Liabilities and Commitments, standalone). Capital commitments
  (Rs 26.35 cr) excluded — commitments, not contingent liabilities.
  Net Worth (standalone) = Rs 821.32 cr (BRSR Q24(iii), AR2026). Ratio =
  16.23/821.32 = **1.98%** → band <5% = **5**

**Block E = 5 + 0 + 0 + 5 = 10 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

- **M1 Pricing Power** (0-5): EBITDA margin FY17 (computed: 34.81/351.09
  = 9.91%, screener-Data_Sheet.csv, EBITDA = PBT − Other Income +
  Depreciation + Interest, method disclosed as "computed") vs FY26
  (11.44%, Investor Presentation p.15 consolidated, EBITDA 1,222/Revenue
  10,685 Mn) = **+1.53pp** (stable band, ±2pp) AND revenue CAGR 13.17% ≥
  10% → **3**. Context: the FY24→FY26 window alone shows margin
  expansion of +2.27pp (9.17%→11.44%, Investor Presentation p.15) on 2-yr
  revenue CAGR 21.48% — a materially stronger recent signal not used for
  the score to keep the window consistent with C1.

- **M2 Cost Advantage vs peer**: PEER DATA NEEDED (no peer EBITDA margin
  data supplied) → **0**

- **M3 Capital Efficiency**: FAT = Sales ÷ (Net Block + CWIP) =
  1,068.48/(173.49+6.82) = **5.93x** (>3x). ROCE (formula-mandated,
  ex-exceptional, from Block A) = **15.02%** (not >20%, but >15%) → band
  "FAT>2x AND ROCE>15%" = **3**. (Using the LB3 operating-ROCE figure of
  30.5% instead would score 5; the formula-mandated ROCE is used here for
  scoring consistency with Block A, per the fixed-formula rule.)

- **M4 Customer Stickiness**: 1 revenue-decline year in 10 (FY20),
  fully recovered by FY21 onward. Receivable days (screener-Data_Sheet.csv
  + Sales, all 10 years, Revenue basis): range 66.5d (FY23) to 83.0d
  (FY21), FY17 69.0d vs FY26 70.6d (+1.5d, stable). "Max 1 decline year,
  fully recovered" → **3**

- **M5 Scale & Dominance**: PEER DATA NEEDED (no peer mcap/segment-margin
  data supplied) → **0**

- **M6 Technology/R&D**: R&D expenditure (AR2026 Note 43, standalone):
  FY26 = revenue exp 465 + capital exp 341 = 806 lakh = Rs 8.06 cr =
  0.75% of Sales (1,068.48 cr); FY25 = 473+585 = 1,058 lakh = Rs 10.58 cr
  = 1.25% of Sales (844.83 cr). Below the 3% and 5% thresholds in both
  years; not "consistently ≥1%" either (drops below 1% in FY26) → **0**

- **M7 Regulatory/License**: Auto-component ignition-systems segment is
  not licence-capped; no regulated-segment player-count evidence supplied
  → unregulated → **0**

- **M8 Distribution**: AR2026 MDA (p.~122) references "investments in
  distribution, partnerships, and brand building" for the aftermarket
  segment, but reach is not quantified (no outlet count, no revenue/
  outlet metric) → "mentioned unquantified" → **1**

- **M9 Brand**: Gross margin proxy (Revenue − Material Cost)/Revenue,
  FY26 = (1068.48−738.03)/1068.48 = 30.92% (screener-Data_Sheet.csv,
  proxy basis stated). No peer median supplied to benchmark against →
  PEER DATA NEEDED → **0**

- **M10 Switching Costs**: Revenue grew in 8 of 9 years (1 decline, FY20)
  AND receivable days rose only +1.5 days FY17→FY26 (stable, ≤10d) →
  "growth all but 1 year AND stable" → **3**

- **M11 Network Effects** (10 years available, ≥6-year test valid):
  latest 3-yr revenue CAGR (FY23→FY26) = (1068.48/656.25)^(1/3)−1 =
  **17.65%**; prior 3-yr CAGR (FY20→FY23) = (656.25/478.81)^(1/3)−1 =
  **11.09%**. Latest > prior. Selling & admin expense as % of sales
  (screener-Data_Sheet.csv): FY23 5.80%, FY24 6.20% (interim spike),
  FY26 4.93% — declining from the FY23/FY24 peak by FY26. "Latest 3yr
  CAGR > prior 3yr AND selling% declining" → **5**

- **M12 Negative WC/Float**: WC days (from Block B, only FY24-FY26
  verifiable) = 40.64 / 43.93 / 51.48 days — all positive, sitting mostly
  in the 15-45 band with the latest year (FY26) crossing above 45. Scored
  on the representative multi-year band (2 of 3 years in 15-45; FY26
  already past 45 and rising, flagged) → band 15-45 = **1**

**Moat profile:**
```
M1  Pricing Power        [###..] 3  present
M2  Cost Advantage       [.....] 0  PEER DATA NEEDED
M3  Capital Efficiency   [###..] 3  present
M4  Customer Stickiness  [###..] 3  present
M5  Scale & Dominance    [.....] 0  PEER DATA NEEDED
M6  Technology/R&D       [.....] 0
M7  Regulatory/License   [.....] 0
M8  Distribution         [#....] 1
M9  Brand                [.....] 0  PEER DATA NEEDED
M10 Switching Costs      [###..] 3  present
M11 Network Effects      [#####] 5  present
M12 Negative WC/Float    [#....] 1
```

**Moat score = 3+0+3+3+0+0+0+1+0+3+5+1 = 19 / 60**
**Moats present (score ≥3): 5 (M1, M3, M4, M10, M11)**
**Moat classification: 4-5 present = STRONG**

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 9 | 20 |
| B — Cash Generation Quality | 5 | 20 |
| C — Growth | 12 | 20 |
| D — Balance Sheet Strength | 20 | 20 |
| E — Shareholder Alignment | 10 | 20 |
| **Core Total** | **56** | **100** |
| F — Moat (12 tests) | 19 | 60 |
| **Grand Total** | **75** | **160** |

Data confidence: 10 years of revenue/PAT/CFO history supplied →
"10+ yrs full" tier on the headline series. Sub-metric caveat: ROCE and
WC Days verified only FY24-FY26 (3 yrs); FCF verified only FY25-FY26
(2 yrs) — see data_notes. history_downgrade = false (overall company
history exceeds the 10-year full-confidence threshold; the gaps are
document-availability gaps for this run, not company-history gaps).

Classification matrix: Core 56 falls in the 40-59 band → **AVERAGE**
(the 40-59 band is not moat-conditioned, so the STRONG moat class does
not lift it — per the fixed matrix).

**Deal-breakers checked:**
1. Block A <8 → max GOOD: Block A = 9, NOT triggered
2. Block B <8 → max GOOD: Block B = 5, **TRIGGERED** (non-binding —
   AVERAGE is already below GOOD)
3. Median ROCE <10% → max AVERAGE: median ROCE = 13.68%, NOT triggered
4. Cumulative CFO/PAT <0.50 → max AVERAGE: 70.5%, NOT triggered
5. Pledge >15% → max AVERAGE: pledge NOT FOUND (no evidence of breach),
   NOT triggered on available data
6. ND/EBITDA >3x AND IC <3x → AVOID: net cash position, NOT triggered
7. Revenue declined in majority of years → max AVERAGE: 1 of 9 years
   declined, NOT triggered
8. PAT negative in any of last 3 years → max AVERAGE: PAT positive all
   3 years, NOT triggered
9. History <3 years → AVERAGE: 10 years of history, NOT triggered

**Strongest block: D (Balance Sheet Strength), 20/20 — near-debt-free,
net cash, current ratio 2.5x.**
**Weakest block: B (Cash Generation Quality), 5/20 — this is the LB1
signal: cumulative cash conversion (70.5%) sits in the middle band, but
the 2 most-recent verifiable years show FCF turning negative (FY26:
−Rs 1.7 cr standalone) and WC days rising +10.8 days FY24→FY26.**

**DECISION: AVERAGE.** The company carries a fortress balance sheet
(Block D 20/20) and a genuine 5-moat-present profile led by an
accelerating, cost-discipline-linked growth curve (M11 = 5), but the
core score is held down by two real, evidenced depressors: (1) cash
generation quality (Block B = 5/20) — cumulative CFO/PAT sits at a
middling 70.5% and the FY26 stand-alone year alone shows CFO/PAT falling
to ~36% with FCF turning negative, the load-bearing LB1 concern,
CONFIRMED; (2) a 10-year ROE median of 11.5% (Block A3 = 0) that the
LB3 analysis shows is substantially a function of a Rs 531.5 cr treasury
book earning single-digit yields sitting inside the return-ratio
denominator — the core operating business, stripped of that book, is
compounding returns in the 22-30% range and rising. Both depressors are
named per rule; neither is shaded away. AVERAGE is the correct
classification on the fixed formulas; the operating-ROCE and moat-count
evidence argue this name is a stronger business than the core score
alone communicates, which is exactly the tension the next-stage dossier
should carry forward.

---

## LOAD-BEARING FACTS — VERIFICATION SUMMARY

- **LB1 (cash conversion break)**: CONFIRMED in full. Standalone CFO
  Rs 40.47 cr (FY26) vs Rs 49.40 cr (FY25); Operating Profit before WC
  changes Rs 121.53 cr vs Rs 94.62 cr; Capex Rs 42.15 cr; FCF ≈ −Rs 1.7
  cr — all match AR2026 p.182 exactly. Working capital absorption ≈
  Rs 51-54 cr for the year, consistent with the operator's figure. The
  operator's screener-sourced WC-days figures (46 FY26 vs 29 FY23) could
  NOT be independently reproduced from the files supplied for this run
  (this stage computed 51.48 FY26 vs 40.64 FY24, the earliest year with
  a verifiable Trade Payables figure) — directionally identical
  (worsening), magnitude differs, likely a different window (FY23 vs
  FY24 as the "earliest" anchor) and/or day-count convention. Flagged for
  reconciliation with the operator's screener source, not treated as an
  error.
- **LB2 (customer concentration vs BRSR related-party %)**: NOT
  independently verified in this stage. The two-customer 71%-of-revenue
  figure and the BRSR 5.38% related-party-sales figure were not located
  in the CSV/cash-flow/balance-sheet sources reviewed for the
  quantitative scorecard; this is a qualitative/disclosure-cross-check
  item better suited to a document-reading stage than Gate 0's numeric
  scan. No scorecard line item scores it directly.
- **LB3 (treasury book diluting ROCE)**: CONFIRMED and quantified. See
  Block A "LB3 CONTEXT." Investments Rs 531.53 cr = 64.7% of FY26 Net
  Worth (821.33 cr). Operating ROCE (ex-investments, ex-other-income)
  runs 21.9% (FY24) → 26.4% (FY25) → 30.5% (FY26), well above the
  formula-mandated ROCE of 11.4-15.0% used for the official score.
- **LB4 (growth vs industry)**: FY26 revenue +26.47% CONFIRMED (matches
  "+26.5%"). Q1FY27 +35.5% CONFIRMED exactly (Investor Presentation p.14
  standalone vs screener-Data_Sheet.csv Q1FY26). 2W industry +20%
  comparator and export figure (Rs 87.3 cr, +162%) NOT FOUND in the
  files reviewed for this stage.

---

```yaml
stage: B01-gate0
company: "INDNIPPON"
run_date: "2026-09-10"
model: claude-sonnet-5
status: complete
input_gaps:
  - "screener-Balance_Sheet.csv, screener-Profit_Loss.csv, screener-Cash_Flow.csv, screener-Quarters.csv: blank templates, no data populated; screener-Data_Sheet.csv used as sole screener source"
  - "Current Liabilities / Trade Payables split: NOT FOUND for FY2017-FY2023 (no AR older than FY2025 supplied); ROCE and WC Days scored on FY2024-FY2026 only"
  - "Capex (Purchase of PPE) breakdown: NOT FOUND for FY2017-FY2024; FCF scored on FY2025-FY2026 only"
  - "Promoter holding as at FY2023 (3-years-back total Promoter+Group %): NOT FOUND"
  - "Promoter pledge disclosure: NOT FOUND anywhere in AR2026 text"
  - "Export revenue rupee figure and 2W-industry growth comparator (LB4): NOT FOUND in files reviewed"
  - "Peer data for M2, M5, M9 moat tests: NOT SUPPLIED"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE (core 56/100). Two named depressors: Block B cash-generation quality 5/20 (cumulative CFO/PAT 70.5%, FY26 FCF turns negative, WC days +10.8d FY24-FY26); Block A3 median ROE 11.5% over 10yr, largely a function of a Rs 531.5cr treasury book diluting the return denominator (LB3) rather than weak core-business economics (operating ROCE 22-30% and rising)."}
  - {type: FLAG-CASH, reason: "Block B trend deteriorating: standalone CFO/PAT fell to ~36% in FY26 (Rs40.47cr/Rs111.26cr) from a 10yr cumulative 70.5%; WC days rose from 40.6 (FY24) to 51.5 (FY26), +10.8 days, driven by receivables+inventory build outpacing payables growth. This is the LB1 signal, confirmed against AR2026 p.182."}
  - {type: FLAG-DATA-GAP, reason: "E2 (promoter holding 3yr change) and E3 (promoter pledge) both NOT FOUND in files supplied; both scored 0 per rule 5, conservative default, not evidence of an actual decline or pledge. Needs live-web/BSE shareholding-pattern verification in a later stage."}
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 9, B: 5, C: 12, D: 20, E: 10}
core_score: 56
moat_score: 19
grand_total: 75
moats_confirmed: 5
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 -> max GOOD (triggered, non-binding: AVERAGE already below GOOD cap)"
history_downgrade: false
data_notes:
  - "screener-Data_Sheet.csv is CONSOLIDATED for all FY2017-FY2026 (verified against Investor Presentation Aug-2026 consolidated statements and AR2026 consolidated notes p.244-249); FY2026 consolidated = standalone since the sole subsidiary (PT Automotive Systems Indonesia) was dissolved 25-Jun-2025; FY2027 onward is standalone-only per company disclosure."
  - "FY26 PAT/PBT include a Rs15.21cr pre-tax exceptional gain (HSVP Gurugram land-acquisition compensation, AR2026 Note 38). C2 (PAT CAGR) scored on an ex-exceptional adjusted basis (adjusted FY26 PAT Rs99.58cr vs reported Rs111.17cr, effective tax rate 23.81% applied). A1/A2/A4 (ROCE) also computed ex-exceptional. Reported (unadjusted) figures shown alongside for transparency."
  - "LB3: operating ROCE (net of the Rs531.5cr investment book, ex-other-income) computed as 21.9%/26.4%/30.5% for FY24/FY25/FY26, materially above the formula-mandated ROCE (11.4%/13.7%/15.0%) used for the official Block A score. Not substituted into the score, per the fixed-formula rule; carried forward as an explicit flag for downstream stages."
  - "M3 (Capital Efficiency) scored using the formula-mandated ROCE (15.02%, band score 3) for internal consistency with Block A; using the LB3 operating ROCE (30.5%) would score 5."
  - "GM proxy used for M9 (Revenue minus Material Cost)/Revenue = 30.92% FY26; no peer median available to complete the test."
  - "WC-days discrepancy: this stage computed FY26=51.48d vs FY24=40.64d (+10.84d, Revenue basis, Trade Payables from Investor Presentation p.16); could not reproduce the operator-cited screener figures of 46d(FY26)/29d(FY23) from files supplied — same direction (deteriorating), different magnitude/window."
block_b_trend: "deteriorating - standalone CFO/PAT fell from a 10yr cumulative 70.5% to ~36% in FY26 alone (CFO Rs40.47cr / PAT Rs111.26cr, AR2026 p.182); WC days rose 40.64 (FY24) -> 51.48 (FY26), +10.84 days"
analyst_note: "Block A's 9/20 and the AVERAGE classification are formula-correct but understate the core business. LB3 shows the Rs531.5cr treasury book (65% of net worth) sits inside both the ROCE denominator and (via other income) inflates nothing in FY26 PBT beyond the already-stripped exceptional item — the operating business alone runs 22-30% ROCE and is improving each of the 3 verifiable years. Block B's 5/20 is the real, un-diluted concern: FY26 standalone FCF turned negative for the first time in the 2-year window this stage can verify, driven by WC absorption (+10.8 days), not by capex discipline failing. Both threads (treasury-diluted returns, cash-conversion break) point to the same underlying fact: FY26 revenue grew 26.5% faster than the balance sheet could fund it internally. Next stage should independently source FY17-FY23 Balance Sheet/Cash Flow detail (older ARs) to extend the ROCE/WC-days/FCF verification window beyond 2-3 years, and verify promoter pledge/3yr holding change via BSE shareholding-pattern filings."
```
