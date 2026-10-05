# STAGE 1: GATE 0 SCORECARD — Steel Strips Wheels Ltd (SSWL)
Run date: 2026-09-19 | Model: claude-sonnet-5

Data available: 5 years (FY22 to FY26), annual. Quarterly: 10 quarters (Q4
FY24 to Q1 FY27). Scoring adapted to 5-year history.

Basis: figures below are CONSOLIDATED unless marked standalone. The
screener Data_Sheet (inputs/screening/SSWL-Data_Sheet.csv) reports
consolidated figures in INR Cr; cross-checked exactly against the AR FY26
consolidated statements (inputs/annual-report/SSWL-AR-FY26-Reg34-2026-09-03.txt,
INR lakh, converted at 100 lakh = 1 Cr) for FY25-FY26, where every
cross-checked line (Total Assets, CFO, Cash & Bank, Total Equity) matched
the screener figure exactly. All figures ₹ Cr unless stated.

## LOAD-BEARING FACTS CHECKED IN THIS STAGE'S SCOPE

- **LBF2 (margin trend)**: CONFIRMED. Computed EBITDA margin (operating,
  excl. Other Income; formula validated below) fell from 12.72% (FY22) to
  9.84% (FY26), matching the company-memory range "~12.7% (FY22) to ~9.8%
  (FY26)" almost exactly. Per-wheel EBITDA (Rs 314 vs Rs 262) and the 35%
  alloy-mix claim need volume/segment data not present in the Data_Sheet;
  deferred to a later stage.
- **LBF3 (cash conversion)**: CONFIRMED on the numbers named, with one
  basis mismatch flagged. FY26 CFO = Rs 331.65 Cr (screener-data; AR FY26
  p.193 consolidated cash flow statement, 33,164.60 lakh) vs computed
  EBITDA Rs 510.23 Cr = 65.0% conversion. Year-end cash "~Rs 6.5 Cr" is the
  STANDALONE figure (AR p.141, 652.14 lakh = Rs 6.52 Cr); consolidated
  year-end cash is Rs 11.40 Cr (AR p.193, 1,140.01 lakh). The factoring /
  bill-discounting note itself was not located in the reviewed AR pages;
  flagged for a later stage.
- **LBF4 (AMW exceptional gain)**: PARTIALLY CONFIRMED. Screener FY24
  Other Income (consolidated) = Rs 486.76 Cr against Rs 3-13 Cr in every
  adjacent year (screener-data) — consistent with a large one-off tied to
  the AACL/AMW NCLT resolution-plan gain. The exact gain break-up and the
  "~Rs 138 Cr consideration" figure could NOT be verified from the FY26 AR
  (it carries only FY25-FY26 comparatives; the FY24 AR is not in the
  corpus per B00). AMW Autocomponent Ltd (AACL) status CONFIRMED: "Wholly
  Owned Subsidiary Company" (AR p.77, line 4567; also p.85 note on related
  parties). The FY24 spike inflated FY24 PAT and, via retained earnings,
  the FY25/FY26 equity base — this is why FY24 ROE (52.4%) is an outlier
  and why FY25-FY26 ROCE/ROE run on a larger equity denominator than they
  would have absent the gain. EBIT (used for ROCE here) excludes Other
  Income, so ROCE is NOT directly contaminated by the gain; the equity
  (ROE, and the ROCE denominator via retained reserves) is.

## FORMULA NOTE (screener Data_Sheet reconciliation)

Data_Sheet gives no EBITDA/EBIT/ROCE/ROE line. Computed EBITDA as Sales −
Raw Material Cost − Power & Fuel − Other Mfr. Exp − Employee Cost −
Selling & Admin − Other Expenses + Change in Inventory (screener's
"Change in Inventory" is a credit to profit, i.e. inventory build). This
reconciles EXACTLY to reported PBT in all 5 years once Depreciation,
Interest and Other Income are applied (e.g. FY26: EBITDA 510.23 −
Depreciation 136.05 − Interest 123.22 + Other Income 3.18 = PBT 254.14,
matching the reported 254.14 exactly). Stated "computed" throughout,
screener-data source.

## GATE 0 SCORECARD

### BLOCK A: RETURN ON CAPITAL (11 / 20)

Capital Employed = Total Assets − Total Current Liabilities.
FY25-FY26: EXACT, from AR FY26 consolidated balance sheet (Total Assets
FY26 3,83,137.93 lakh / FY25 3,39,891.28 lakh, matching screener's Total
exactly; Total Current Liabilities FY26 1,62,646.16 lakh / FY25
1,37,061.24 lakh — AR p.191). FY22-FY24: Data_Sheet does NOT split Current
Liabilities from other liabilities, so Capital Employed is PROXIED as
Equity + Total Borrowings (screener-data) — a superset that also includes
current borrowings, so it UNDERSTATES true ROCE for FY22-FY24. This is a
methodology break; flagged (see data_notes). Treat FY22-24 ROCE as a soft
floor.

| Year | EBIT (computed) | Capital Employed | Basis | ROCE |
|---|---|---|---|---|
| FY22 | 375.91 | 1,729.74 | proxy (Equity+Borrowings) | 21.73% |
| FY23 | 362.41 | 1,773.64 | proxy | 20.43% |
| FY24 | 359.34 | 2,490.61 | proxy | 14.43% |
| FY25 | 373.21 | 2,028.30 | exact (AR p.191) | 18.40% |
| FY26 | 374.18 | 2,204.92 | exact (AR p.191/192) | 16.97% |
(all: screener-data for EBIT inputs and FY22-24 CE; AR FY26 p.191-192 for
FY25-26 CE)

- **A1 Median ROCE = 18.40%** (band 15-19.9%) → **3**
- **A2 Minimum single-year ROCE = 14.43%** (FY24, band 12-14.9%) → **3**
- **A3 Median ROE = 18.57%** (band 15-19.9%) → **4**
  ROE = PAT ÷ average Net Worth; FY22 uses closing Net Worth only
  (opening unavailable, stated per rule). Net Worth = Equity Share
  Capital + Reserves (screener-data).
  | Year | PAT | Avg Net Worth | ROE |
  |---|---|---|---|
  | FY22 | 205.46 | 951.84 (closing only) | 21.58% |
  | FY23 | 193.79 | 1,043.28 | 18.57% |
  | FY24 | 674.68 | 1,288.47 | 52.36% (AMW-gain outlier, see LBF4) |
  | FY25 | 195.28 | 1,533.96 | 12.73% |
  | FY26 | 190.22 | 1,715.25 | 11.09% |
- **A4 ROCE trend, latest (FY26 16.97%) vs earliest (FY22 21.73%)**:
  decline 4.76pp (band 3-5pp decline) → **1**

### BLOCK B: CASH GENERATION QUALITY (18 / 20)

- **B1 Cumulative CFO ÷ Cumulative PAT (5yr) = 1,795.41 ÷ 1,459.43 = 1.230**
  (band ≥1.00) → **5** (screener-data, CFO and PAT rows, all 5 years)
- **B2 FCF-positive years proportion**: FCF computable for FY25-FY26 only
  (Capex not broken out of Data_Sheet's aggregate Investing Activities for
  FY22-24; N/A those years). FY25 FCF = CFO 516.64 − Capex 212.35 =
  304.29 (positive). FY26 FCF = CFO 331.65 − Capex 192.81 = 138.84
  (positive). 2 of 2 computable years positive = 100% → **5** (flagged:
  only 2 of 5 years computable; capex from AR FY26 p.193 consolidated cash
  flow, "Purchase of fixed assets")
- **B3 Cumulative FCF ÷ Cumulative PAT** (same 2-year window, flagged):
  443.13 ÷ 385.50 = 1.150 (band ≥0.60) → **5**
- **B4 Change in WC Days, latest vs earliest** (computable window FY25 →
  FY26 only; Trade Payables not in Data_Sheet for FY22-24, so full WC Days
  needs AR payables, available FY25-26 only, AR p.191/pp.218-219): WC Days
  FY25 = 39.26 (Receivable 40.08 + Inventory 61.24 − Payable 62.06); WC
  Days FY26 = 39.37 (Receivable 42.88 + Inventory 67.05 − Payable 70.56).
  Change = +0.11 days (band ±5 days) → **3**

### BLOCK C: GROWTH (6 / 20)

- **C1 Revenue CAGR FY22→FY26 (4yr)** = (5,182.80 ÷ 3,559.95)^(1/4) − 1 =
  **9.85%** (band 5-9.9%) → **1** (screener-data)
- **C2 PAT CAGR FY22→FY26** = (190.22 ÷ 205.46)^(1/4) − 1 = **−1.91%**
  (negative, both endpoints positive so not N/M, but negative band) → **0**
- **C3 Positive YoY revenue years** = 4 of 4 (FY22→23, 23→24, 24→25,
  25→26 all positive) = 100% → **5**
- **C4 PAT CAGR − Revenue CAGR** = −1.91 − 9.85 = **−11.76pp** (band
  <−8pp) → **0**

### BLOCK D: BALANCE SHEET STRENGTH (10 / 20)

- **D1 Net Debt ÷ EBITDA (FY26)** = (Borrowings 828.37 − Cash & Bank
  11.40) ÷ EBITDA 510.23 = 816.97 ÷ 510.23 = **1.60x** (band 1-2x) → **3**
  (screener-data; AR consol borrowings cross-check current+non-current =
  825.90, close, minor diff from lease liability inclusion)
- **D2 Interest Coverage (FY26)** = EBIT 374.18 ÷ Interest 123.22 =
  **3.04x** (band 3-4.9x) → **2**
- **D3 Debt ÷ Equity (FY26)** = Borrowings 828.37 ÷ Net Worth 1,804.82 =
  **0.459x** (band 0.1-0.5x) → **4**
- **D4 Current Ratio (FY26)** = Total Current Assets 1,635.79 ÷ Total
  Current Liabilities 1,626.46 (AR FY26 p.191, consolidated) = **1.006x**
  (band 1.0-1.19x) → **1**

### BLOCK E: SHAREHOLDER ALIGNMENT (18 / 20)

- **E1 Promoter holding (latest quarter, Jun-2026)** = **61.14%**
  (inputs/shareholding/SSWL-SHP-Jun2026-BSE.txt, Table I; 17 promoter
  holders, no partly-paid/DR complications) (band ≥60%) → **5**
- **E2 Promoter holding change**: only a 1-year change is in the corpus —
  FY25 61.24% → FY26 61.14% = **−0.10pp** (AR p.164/p.219, "TOTAL
  SHAREHOLDING (A+B)" note). The formula's 3-year window cannot be filled
  (FY23 shareholding data not in corpus); scored on the 1-year change as
  the best available evidence, flagged. Band ±1% → **3**
- **E3 Promoter pledge (latest)** = **0%** (SHP Jun-2026, declaration
  items 7-9 all "No"; AR p.164 shows no encumbrance column populated)
  (band 0%) → **5**
- **E4 Contingent Liabilities ÷ Net Worth (FY26)** = LC/BG outstanding
  60.22 (AR p.225, consolidated Note 40, 6,022.11 lakh) ÷ Net Worth
  1,804.82 = **3.34%** (band <5%) → **5**. Note: this excludes disputed
  statutory dues under CARO annexure (~Rs 24.9 Cr across GST/excise/customs
  disputes, AR p.135-136), which are a separate disclosure from the formal
  Note 40 Contingent Liabilities line; not included in this ratio.

### BLOCK F: QUANTITATIVE MOAT SCORING (17 / 60) — 3 moats present, MODERATE

Peer set used for M2/M5/M9 (3-company peer set, not a full segment/industry
set): ALICON Castalloy, Uno Minda, Wheels India
(inputs/screening/ALICON-Data_Sheet.csv, UNOMINDA-Data_Sheet.csv,
WHEELS-Data_Sheet.csv), same EBITDA/GM formula as SSWL, FY26.

| Peer | EBITDA margin FY26 | GM proxy (Rev−RM)/Rev FY26 | Mcap (Cr) |
|---|---|---|---|
| SSWL | 9.84% | 33.18% | 5,856.55 |
| ALICON | 11.29% | 45.34% | 1,197.0 |
| UNOMINDA | 11.45% | 34.76% | 74,146.79 |
| WHEELS | 7.55% | 31.57% | 5,315.89 |
| Peer median (excl SSWL) | 11.29% | 34.76% | — |

- **M1 Pricing Power**: margin declined 2.88pp (12.72%→9.84%) despite
  revenue growth → **1**
- **M2 Cost Advantage vs peer median EBITDA margin**: SSWL 9.84% vs
  median 11.29% = −1.45pp (band ±2pp) → **1**
- **M3 Capital Efficiency**: FAT (Sales÷Net Block, FY26) = 5,182.80 ÷
  1,970.95 = 2.63x; ROCE (exact) 16.97%. Band FAT>2x AND ROCE>15% → **3**
- **M4 Customer Stickiness**: zero revenue-decline years; receivable days
  FY22 40.23 → FY26 42.87, +2.64 days (within ±10) → **5**
- **M5 Scale & Dominance**: SSWL mcap rank 2nd of 4 in peer set (top3);
  margin rank 3rd of 4 (not top2) → fails the top3-mcap/top2-margin band,
  qualifies only "top5 mcap" → **1** (flagged: peer-set only, not a full
  segment ranking)
- **M6 Technology/R&D**: R&D operating expense (R&D/Revenue) not
  separately disclosed in the reviewed AR pages; only R&D CAPITAL
  expenditure by site is disclosed (AR p.212-213, Note on PPE). N/A (not
  in provided data) → **0**
- **M7 Regulatory/License**: unregulated, OEM-spec auto component
  manufacturing, no licence/quota gate → **0**
- **M8 Distribution**: B2B OEM supply, no outlet/distribution-reach
  metric applicable → **0**
- **M9 Brand**: GM proxy 33.18% vs peer median 34.76% = below peer median
  → **0**
- **M10 Switching Costs**: revenue grew every year; receivable days rose
  2.64 days over the period (≤10 days) → **5**
- **M11 Network Effects**: only 5 years available (<6 needed for the
  two-window test); scored conservatively on overall trend. Revenue CAGR
  9.85% <20% and <15% → **0**
- **M12 Negative WC / Float**: WC Days computable for FY25 (39.26) and
  FY26 (39.37) only (payables not in Data_Sheet pre-FY25); both fall in
  15-45 band, flagged as a 2-of-5-year sample → **1**

Moat sum = 1+1+3+5+1+0+0+0+0+5+0+1 = **17**. Moats "present" (score ≥3):
M3, M4, M10 = **3 moats confirmed** → **MODERATE**.

## SCOREBOARD

| Block | Score | Max |
|---|---|---|
| A Return on Capital | 11 | 20 |
| B Cash Generation Quality | 18 | 20 |
| C Growth | 6 | 20 |
| D Balance Sheet Strength | 10 | 20 |
| E Shareholder Alignment | 18 | 20 |
| **Core Score** | **63** | **100** |
| F Quantitative Moat | 17 | 60 |
| **Grand Total** | **80** | **160** |

Moat profile: FORTRESS(0) STRONG(0) MODERATE(●, 3 present) THIN(0) NONE(0)

**Strongest blocks**: B (Cash Generation, 18/20 = 90%) and E (Shareholder
Alignment, 18/20 = 90%), tied.
**Weakest block**: C (Growth, 6/20 = 30%) — revenue CAGR just under the
10% band and a negative PAT CAGR drag the block down; note C1/C2/C4 all
reflect a business growing top line modestly while margin compression
(Block A/M1) erodes bottom line faster than revenue grows.

## DATA CONFIDENCE

5 years (FY22-FY26) → "lower, may not have seen full cycle" tier (per
scale: 5-6 yrs). No classification downgrade at this tier (downgrade
applies only at 3-4 years). `history_downgrade: false`.

## DEAL-BREAKER CHECK (none triggered)

1. Block A <8 → Block A=11, not triggered.
2. Block B <8 → Block B=18, not triggered.
3. Median ROCE <10% → 18.40%, not triggered.
4. Cumulative CFO/PAT <0.50 → 1.230, not triggered.
5. Pledge >15% → 0%, not triggered.
6. ND/EBITDA >3x AND IC <3x → ND/EBITDA 1.60x, not triggered.
7. Revenue declined in majority of years → 0 decline years, not
   triggered.
8. PAT negative in any of last 3 years → FY24/25/26 PAT all positive
   (674.68 / 195.28 / 190.22), not triggered.
9. History <3 years → 5 years, not triggered.

## CLASSIFICATION

Core Score 63 (60-79 band) + Moat MODERATE (else, not STRONG/FORTRESS) →
**GOOD**

No deal-breaker override applies. Classification stands at **GOOD**.

## DECISION LINE

SSWL scores GOOD (80/160 grand total; Core 63/100, MODERATE moat 17/60,
3 moats confirmed: Capital Efficiency, Customer Stickiness, Switching
Costs). Cash generation and shareholder alignment are the strongest
blocks; growth and the return-on-capital trend are the weakest, with a
4.76pp ROCE decline over 5 years and a negative PAT CAGR despite steady
revenue growth — consistent with the margin-compression thesis question
in company memory (LBF2, CONFIRMED this stage). The FY26 cash-conversion
ratio (CFO/EBITDA 65.0%) sits well below FY25's 106.7%, a one-year swing
worth carrying forward as a tripwire. The FY24 AMW/AACL gain (LBF4,
PARTIALLY CONFIRMED) inflates the FY24 ROE reading and lifts the equity
base the FY25-26 ROE/ROCE denominators sit on; this is a data-quality
flag, not a deal-breaker, since EBIT (used for ROCE here) already
excludes Other Income.

## DATA GAPS AND METHODOLOGY FLAGS CARRIED FORWARD FROM B00

From outputs/blocks/B00-inputs.yaml input_gaps (relevant to this stage):
- Screener export sheets (P&L/BS/CF/Quarters) came out empty; Data_Sheet
  read instead (used throughout this stage).
- FY25 AR not in corpus; only FY26 AR (with FY25-26 comparatives) — this
  is why FY22-24 Capital Employed, Capex and Payables could not be
  sourced exactly (see Block A/B/moat notes above).
- Shareholding: only Jun-2026 SHP in corpus — this is why E2 (3-year
  promoter change) could only be scored on a 1-year window.

New gaps found in this stage's own work:
- Capital Employed methodology break FY22-24 (proxy, Equity+Borrowings)
  vs FY25-26 (exact, AR Total Assets − Current Liabilities). Proxy
  understates true ROCE for FY22-24.
- Capex and Trade Payables not in Data_Sheet for FY22-24 (aggregate cash
  flow lines only); FCF, B2, B3, B4 and full WC Days scored on a 2-of-5
  year window (FY25-26) for those metrics, flagged in each line item.
- R&D operating expense (as % of revenue) not located in the reviewed AR
  pages; M6 scored 0, N/A not in provided data.
- Factoring / bill-discounting note referenced in LBF3 not located in the
  reviewed AR pages; flagged for a later stage's document read.
