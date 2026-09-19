# STAGE 1: GATE 0 SCORECARD — Goodluck India Ltd (GOODLUCK)
Run date: 2026-09-19 | Model: claude-sonnet-5

Data available: 10 years (FY17 to FY26) for revenue, PAT and cash-flow
lines (screener Data_Sheet, consolidated, cross-checked against
Annual_Report_2026.txt and Annual_Report_2025.txt consolidated
statements — Total Assets, Borrowings, CFO, PBT, Interest, Depreciation
and Other Income all tie to the rupee-crore across both sources).
Balance-sheet-dependent metrics that need the current/non-current split
or Trade Payables (ROCE, D1/D2 latest-year inputs, and the WC-days trend
in B4) are computable for FY24-FY26 only (3 years): the provided corpus
holds two Annual Reports, each giving only a 2-year comparative Balance
Sheet, and FY17-FY23 Balance Sheets are not in the corpus. Scoring is
adapted per metric; each metric below states its own window.

All figures consolidated (Group) unless marked STANDALONE. Rs Cr unless
stated. AR figures in the source are Rs Lakh; converted to Cr (÷100) and
shown to 2dp.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — FY24-FY26 window only

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (not
source-provided; screener Data_Sheet carries no ROCE row).
EBIT = PBT + Finance Cost (Other Income stays inside PBT, not stripped
out — stated assumption).

| FY | PBT | Interest | EBIT | Total Assets | Current Liab. | Cap. Employed | ROCE |
|----|-----|----------|------|--------------|----------------|---------------|------|
| FY24 | 182.42 | 77.48 | 259.90 | 2,032.40 | 736.41 | 1,295.99 | 20.06% |
| FY25 | 220.87 | 80.33 | 301.20 | 2,529.32 | 970.57 | 1,558.75 | 19.32% |
| FY26 | 245.63 | 105.84 | 351.47 | 3,046.18 | 1,231.40 | 1,814.78 | 19.37% |

Sources: PBT/Interest — screener-data (Data_Sheet P&L rows), cross-checked
to AR consolidated P&L: FY26/FY25 (AR p.189), FY24 (AR2025 p.202).
Total Assets — screener-data, ties to AR consolidated BS: FY26/FY25
(AR p.188), FY24 (AR2025 p.201). Current Liabilities — AR consolidated BS
only (not in screener Data_Sheet): FY26 Rs1,231.40 Cr / FY25 Rs970.57 Cr
(AR p.188), FY24 Rs736.41 Cr (AR2025 p.201).

- **A1 Median ROCE (3yr)** = 19.37% → band 15-19.9% = **3**
- **A2 Minimum single-year ROCE** = 19.32% (FY25) → band ≥15% = **5**
- **A3 Median ROE (3yr)** — source-provided (AR consolidated Key Ratios,
  Note 41): FY24 14.94% (AR2025 p.232), FY25 13.26%, FY26 12.70%
  (AR p.223). Median = 13.26% → band 12-14.9% = **2**
- **A4 ROCE trend, latest (FY26 19.37%) vs earliest (FY24 20.06%)** =
  decline of 0.69pp. This falls below the defined "decline 1-3pp" band's
  own floor (no band covers a sub-1pp decline); scored against the
  nearest defined band (1-3pp) as the closest fit, flagged as an edge
  case rather than forced into "latest ≥ earliest." → **3**

**Block A raw = 3+5+2+3 = 13/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

B1 uses the full 10-year CFO/PAT series (screener-data, verified: FY26
CFO Rs200.24 Cr and FY24 CFO -Rs45.93 Cr both tie to AR consolidated cash
flow statements, AR p.190 and AR2025 p.203 respectively). B2/B3 need
Capex (PP&E purchase), available only for FY24-FY26 from the two ARs'
cash flow statements; screener's "Cash from Investing Activity" is not
pure capex (includes investments, interest received, disposals) so is
not substituted, per the formula's own exclusion rule.

| FY | CFO | PAT |
|----|-----|-----|
| FY17 | 22.78 | 19.75 |
| FY18 | 73.18 | 15.99 |
| FY19 | 56.89 | 31.46 |
| FY20 | 58.05 | 33.87 |
| FY21 | 43.11 | 30.05 |
| FY22 | 77.75 | 75.01 |
| FY23 | 64.89 | 87.80 |
| FY24 | -45.93 | 132.27 |
| FY25 | 158.26 | 165.63 |
| FY26 | 200.24 | 180.71 |
| **Cum.** | **709.22** | **772.54** |

(screener-data, Data_Sheet CASH FLOW and PROFIT & LOSS rows)

- **B1 Cumulative CFO ÷ Cumulative PAT (10yr)** = 709.22 / 772.54 =
  0.918 → band 0.85-0.99 = **4**

Capex and FCF, FY24-FY26 (Capex = PP&E purchase from consolidated CF
statement; AR p.190 for FY26/FY25, AR2025 p.203 for FY24):

| FY | CFO | Capex | FCF |
|----|-----|-------|-----|
| FY24 | -45.93 | 196.39 | -242.32 |
| FY25 | 158.26 | 490.96 | -332.70 |
| FY26 | 200.24 | 347.63 | -147.39 |
| **Cum.** | **312.57** | **1,034.98** | **-722.41** |

- **B2 FCF-positive years, proportion (3yr window)** = 0 of 3 = 0% →
  band <50% = **0**
- **B3 Cumulative FCF ÷ Cumulative PAT (same 3yr window; cumulative PAT
  FY24-26 = 478.61)** = -722.41 / 478.61 = -1.51 → band <0.20 or
  negative = **0**

Working Capital Days, FY24 vs FY26 (Receivable Days = Receivables ÷
Revenue × 365; Inventory Days = Inventory ÷ Revenue × 365; Payable Days
= Payables ÷ Revenue × 365; revenue basis used throughout, stated).
Trade Payables only in AR consolidated BS (screener Data_Sheet has no
payables row): FY24 Rs137.20 Cr (AR2025 p.201), FY26 Rs158.11 Cr
(AR p.188). Receivables/Inventory/Revenue from screener-data.

| FY | Recv. Days | Inv. Days | Pay. Days | WC Days |
|----|-----------|-----------|-----------|---------|
| FY24 | 36.37 | 63.09 | 14.20 | 85.26 |
| FY26 | 42.60 | 76.21 | 14.08 | 104.73 |

- **B4 Change in WC Days, FY26 vs FY24 (3yr window, per the same
  Current-Liabilities/Payables limitation as Block A)** = +19.47 days →
  band increased >15 = **0**

**Block B raw = 4+0+0+0 = 4/20** (triggers deal-breaker #2, Block B<8)

**block_b_trend: deteriorating** — WC days +19.5 (FY24→FY26); FCF
negative in all 3 measurable years; cumulative FY24-26 CFO (Rs312.57 Cr)
covers only 65% of cumulative FY24-26 PAT (Rs478.61 Cr), against a
10-year cumulative CFO/PAT of 92% — the deterioration is recent and
capex-driven, not visible in the 10-year headline ratio.

---

## BLOCK C: GROWTH (Max 20) — full 10-year window (FY17-FY26)

Revenue: FY17 Rs1,093.01 Cr → FY26 Rs4,100.28 Cr (screener-data).
PAT: FY17 Rs19.75 Cr → FY26 Rs180.71 Cr (screener-data). No loss-to-profit
swing anywhere in the window (PAT positive every year FY17-FY26).

- **C1 Revenue CAGR (9yr)** = (4,100.28/1,093.01)^(1/9)-1 = **15.81%** →
  band 15-19.9% = **4**
- **C2 PAT CAGR (9yr)** = (180.71/19.75)^(1/9)-1 = **27.85%** → band
  ≥20% = **5**
- **C3 Positive YoY revenue years** = 7 of 9 (declines FY20 vs FY19,
  FY21 vs FY20; all other 7 years positive) = 77.8% → band 75-99% = **3**
- **C4 PAT CAGR minus Revenue CAGR** = 27.85 - 15.81 = +12.04pp → band
  ≥+3pp = **5**

**Block C raw = 4+5+3+5 = 17/20**

Deal-breaker #7 check: revenue declined in 2 of 9 years, not a majority
— not triggered.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — latest year FY26 only

- **D1 Net Debt ÷ EBITDA**: Net Debt = Borrowings 1,119.46 − Cash & Bank
  49.33 = Rs1,070.13 Cr (screener-data, FY26; Borrowings and Cash&Bank
  both tie to AR consolidated BS p.188 — Borrowings 22,390.57+89,554.85
  lakh, Cash+other bank balances 84.00+4,848.69 lakh). EBITDA = PBT
  245.63 + Interest 105.84 + Depreciation 67.03 − Other Income 20.24 =
  **Rs398.26 Cr** (derived; cross-checked against screener's quarterly
  Operating Profit sum for FY26 of Rs398.25 Cr — consistent to Rs0.01
  Cr). Net Debt/EBITDA = 1,070.13/398.26 = **2.69x** → band 2-3x = **1**
  (0.31x from the >3x deal-breaker-6 threshold — flagged as a near-miss,
  not triggered).
- **D2 Interest Coverage** = EBIT 351.47 ÷ Interest 105.84 = **3.32x** →
  band 3-4.9x = **2** (also close to the deal-breaker-6 IC<3x line, from
  the other side).
- **D3 Debt ÷ Equity (latest)** = **0.73x**, source-provided (AR
  consolidated Key Ratios Note 41, p.223: "Total Debts / Total Equity")
  → band 0.5-1.0x = **3**
- **D4 Current Ratio (latest)** = **1.38x**, source-provided (AR
  consolidated Key Ratios Note 41, p.223) → band 1.2-1.49x = **2**

**Block D raw = 1+2+3+2 = 8/20**

Deal-breaker #6 check (ND/EBITDA>3x AND IC<3x → AVOID): ND/EBITDA 2.69x
(not >3x) and IC 3.32x (not <3x) — neither condition met, **not
triggered**, but both readings sit inside 0.3x-0.4x of the trigger line.
Flagged for the operator as a leverage watch item, not a mechanical
breaker.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

- **E1 Promoter holding (latest quarter, Aug 2026)** = **54.00%**
  (screener-shareholding-quarterly CSV, aggregator table, row "Promoters"
  Aug 2026 column) → band 50-59.9% = **4**
- **E2 Promoter holding change over ~3 years**: latest Aug 2026 (54.00%)
  vs nearest available prior data point, Dec 2023 (56.45%) — the
  quarterly series in the provided CSV starts Dec 2023, so the lookback
  is ~32 months, not a clean 36 (closest available anchor; stated as an
  approximation). Change = 54.00 - 56.45 = -2.45pp → band decreased
  1-3% = **1**
- **E3 Promoter pledge (latest)**: not disclosed anywhere in the provided
  corpus — checked AR2026 (both standalone and consolidated notes; only
  "Company/Group has pledged its trade receivables..." as collateral
  for its own borrowings, not a promoter share pledge) and both rating
  rationales (IndRa, CRISIL — no pledge mention). **N/A (not in provided
  data)** → scored **0** per the no-estimate rule (not assumed 0%).
- **E4 Contingent Liabilities ÷ Net Worth (latest)**: Contingent
  Liabilities FY26 (consolidated, AR p.220) = bank guarantees 119.52 +
  bills discounted 219.28 + disputed excise/commercial tax 13.43 +
  disputed income tax 0.99 = **Rs353.23 Cr** (capital-account
  commitments of Rs363.06 Cr excluded — a commitment, not a contingent
  liability, per the AR's own heading split). Net Worth = Total Equity
  (incl. non-controlling interest, matching the AR's own D3 convention)
  FY26 = **Rs1,528.61 Cr** (AR p.188). Ratio = 353.23/1,528.61 = 23.11%
  → band 15-30% = **1**

**Block E raw = 4+1+0+1 = 6/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

No peer/competitor dataset, no research, and no R&D-spend or
distribution-network disclosure was in the provided corpus (see input
gaps). Every test that needs peer data is marked PEER DATA NEEDED and
scored 0, per the rule — never guessed.

- **M1 Pricing Power**: EBITDA margin proxy (PBT+Interest+Dep-Other
  Income)÷Revenue: FY17 = 87.03/1,093.01 = 7.96%; FY26 =
  398.26/4,100.28 = 9.71%. Change = +1.75pp (within ±2pp "stable" band).
  Revenue CAGR 15.81% (≥10%). → band margin stable ±2pp AND rev CAGR
  ≥10% = **3**
- **M2 Cost Advantage vs peer**: PEER DATA NEEDED → **0**
- **M3 Capital Efficiency**: FAT = Revenue 4,100.28 ÷ Net Block 1,202.68
  (screener-data, FY26) = 3.41x (>3x). ROCE FY26 = 19.37% (not >20%, but
  >15%). → band FAT>2x AND ROCE>15% = **3**
- **M4 Customer Stickiness**: 2 revenue-decline years (FY20, FY21) in
  the 9-year window, overall revenue CAGR positive. → band 2 decline
  years, CAGR positive = **1**
- **M5 Scale & Dominance**: PEER DATA NEEDED (no mcap/market-share
  ranking data provided) → **0**
- **M6 Technology/R&D**: no R&D-spend disclosure in the provided corpus
  → **0** (PEER DATA / DISCLOSURE NEEDED)
- **M7 Regulatory/License**: Group is "in the business of manufacturing
  and sale of Iron & steel products" (AR p.220, Segment note) — an
  unregulated manufacturing business, no licence/quota gate evidenced.
  → band unregulated = **0**
- **M8 Distribution**: no distribution-reach data (outlets, dealers) in
  the corpus → band none/unquantified = **0**
- **M9 Brand**: PEER DATA NEEDED (no peer gross-margin benchmark
  provided to apply the proxy against) → **0**
- **M10 Switching Costs**: overall revenue growth with 2 decline years
  (FY20, FY21) → band overall growth, 2+ decline years = **1**
- **M11 Network Effects** (10yr history, ≥6yr test applies): latest 3yr
  revenue CAGR (FY23→FY26) = (4,100.28/3,072.01)^(1/3)-1 = 10.09%; prior
  3yr CAGR (FY20→FY23) = (3,072.01/1,635.86)^(1/3)-1 = 23.39%. Latest is
  NOT greater than prior, and latest growth (10.09%) is below the 15%
  floor of the lower tiers too. Selling-expense % trend not assessable
  (screener's "Selling and admin" row is blank for FY26). → **0**
- **M12 Negative WC/Float**: WC days 85.3 (FY24) and 104.7 (FY26), both
  >45 in the only years computable → band >45 = **0**

**Moat score = 3+0+3+1+0+0+0+0+0+1+0+0 = 8/60**

Moats present (score ≥3): M1 (Pricing Power), M3 (Capital Efficiency) =
**2 present → MODERATE**

---

## SCORECARD SUMMARY

| Block | Raw | Max |
|-------|-----|-----|
| A — Return on Capital | 13 | 20 |
| B — Cash Generation Quality | 4 | 20 |
| C — Growth | 17 | 20 |
| D — Balance Sheet Strength | 8 | 20 |
| E — Shareholder Alignment | 6 | 20 |
| **Core total** | **48** | **100** |
| F — Moat Scoring | 8 | 60 |
| **Grand total** | **56** | **160** |

**Strongest block: C — Growth (17/20)**, driven by PAT CAGR outrunning
revenue CAGR by 12pp and near-zero decline years.
**Weakest block: B — Cash Generation Quality (4/20)**, driven by 3
straight years of negative FCF under a heavy capex programme and WC
days lengthening 19.5 days.

## MOAT PROFILE
```
M1 Pricing Power        [###--] 3/5  present
M2 Cost Advantage       [-----] 0/5  PEER DATA NEEDED
M3 Capital Efficiency   [###--] 3/5  present
M4 Customer Stickiness  [#----] 1/5
M5 Scale & Dominance    [-----] 0/5  PEER DATA NEEDED
M6 Technology/R&D       [-----] 0/5  DISCLOSURE NEEDED
M7 Regulatory/License   [-----] 0/5
M8 Distribution         [-----] 0/5
M9 Brand                [-----] 0/5  PEER DATA NEEDED
M10 Switching Costs     [#----] 1/5
M11 Network Effects     [-----] 0/5
M12 Negative WC/Float   [-----] 0/5
```
Moat classification: **MODERATE** (2 of 12 present)

## CLASSIFICATION

Core score 48 falls in the 40-59 band → matrix classification =
**AVERAGE** (this band is flat AVERAGE regardless of moat tier).

Deal-breaker check:
1. Block A (13) <8? No.
2. **Block B (4) <8? Yes → caps classification at max GOOD.** Already
   below the cap (AVERAGE < GOOD), so non-binding on the final result,
   but recorded per the rule.
3. Median ROCE (19.37%) <10%? No.
4. Cumulative CFO/PAT (0.918, 10yr) <0.50? No.
5. Pledge (N/A, not disclosed) >15%? No evidence found; not triggered.
6. ND/EBITDA (2.69x) >3x AND IC (3.32x) <3x? No — near-miss, flagged,
   not triggered.
7. Revenue declined in majority of years? No (2 of 9).
8. PAT negative in any of last 3 years? No (FY24/25/26 all positive).
9. History <3 years? No.

Data confidence caveat: the metrics that most shape Blocks A and D
(ROCE, the WC-days trend, Net Debt/EBITDA, Interest Coverage) run on a
3-year window (FY24-FY26) because the corpus holds only two Annual
Reports, each with a 2-year Balance Sheet comparative. The 10-year
window (Blocks B1, C) is unaffected. This is not mechanically applied
as a tier downgrade because the shortfall is metric-specific, not a
whole-corpus shortfall — flagged instead (FLAG-DATA-LIMITED below).

## DECISION LINE

**Classification: AVERAGE.** Growth is genuinely strong (Block C
17/20, PAT compounding faster than revenue) but the balance sheet has
been funding a large capex programme with debt, not operating cash:
Borrowings consolidated rose from Rs612.04 Cr (FY24) to Rs1,119.46 Cr
(FY26) while FCF stayed negative all 3 measurable years and WC days
lengthened. Leverage (Net Debt/EBITDA 2.69x, IC 3.32x) sits close to
(not past) the AVOID-tier deal-breaker. Gate 0 is mechanical: this
carries forward as flags, not a halt.

---
