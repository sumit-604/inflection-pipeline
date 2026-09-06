# STAGE 1: GATE 0 SCORECARD — CEIGALL INDIA LTD (CEIGALL)
Run date: 2026-09-06 | Model: claude-sonnet-5

Data available: 6 years (FY2021 to FY2026). Scoring adapted to 6-year history.

Source note: screener-Profit_Loss.csv, -Balance_Sheet.csv, -Cash_Flow.csv and
-Quarters.csv are header-only (collector defect, confirmed empty, not
re-reported as data gaps below beyond the input_gaps list). All P&L,
balance sheet and cash flow figures below come from
screener-Data_Sheet.csv (the populated file). inputs/results/,
inputs/rating/, inputs/prospectus/ and inputs/shareholding/ are empty. Per
run instruction, this stage runs from screener data alone; the annual
report PDF was not opened.

Two computed bases used consistently across the scorecard (screener-data
does not supply EBIT/EBITDA/ROCE/ROE rows directly in this cut-down sheet,
so they are computed, per the instruction file's "compute when absent"
rule):
- EBIT = PBT + Interest (screener-data)
- EBITDA = PBT + Depreciation + Interest − Other Income (screener-data,
  algebraically implied by the P&L structure; verified against PBT each
  year)
- Capital Employed = Equity Share Capital + Reserves + Borrowings =
  Total Assets − Other Liabilities (screener-data; "Other Liabilities" is
  the only current-liabilities-equivalent line the sheet provides, so it
  is used as the current-liabilities proxy, consistent with how
  screener.in itself derives Capital Employed in the absence of a
  separate current/non-current split)

---

## BLOCK A: RETURN ON CAPITAL (max 20)

| Year | PBT | Interest | EBIT (computed) | Capital Employed (computed) | ROCE |
|---|---|---|---|---|---|
| FY21 | 151.26 | 6.54 | 157.80 | 334.99 | 47.10% |
| FY22 | 169.47 | 10.55 | 180.02 | 747.56 | 24.08% |
| FY23 | 225.19 | 51.71 | 276.90 | 1295.99 | 21.36% |
| FY24 | 405.35 | 94.15 | 499.50 | 1953.97 | 25.56% |
| FY25 | 384.59 | 134.36 | 518.95 | 3229.63 | 16.07% |
| FY26 | 417.62 | 160.37 | 577.99 | 3449.28 | 16.76% |

(all figures screener-data, computed as stated above)

Median ROCE = 22.72% (median of the 6 values above, screener-data computed)
Min single-year ROCE = 16.07% (FY25, screener-data computed)

Net Worth (Equity Share Capital + Reserves, screener-data):
FY21 305.29 | FY22 431.25 | FY23 593.06 | FY24 887.73 | FY25 1832.59 | FY26 2138.14

ROE (PAT ÷ average Net Worth; FY21 uses closing Net Worth only, no prior
year available, stated per rule):
FY21 36.85% | FY22 34.17% | FY23 32.66% | FY24 41.35% | FY25 21.62% | FY26 15.71%
Median ROE = 33.42% (screener-data computed)

- A1 Median ROCE 22.72% → band 20-24.9% = **4**
- A2 Min single-year ROCE 16.07% → ≥15% = **5**
- A3 Median ROE 33.42% → ≥20% = **5**
- A4 ROCE trend, latest (16.76%, FY26) vs earliest (47.10%, FY21): decline
  30.34pp → decline >5pp = **0**. Data note: FY21 sits on a pre-scale
  capital base (982,100 shares, face value Rs10, Net Worth Rs305cr, before
  the FY22 stock split, FY24 bonus issue and Aug-2024 IPO); the 47.10%
  figure is arithmetically correct on the provided data but is not
  comparable to the post-IPO capital structure. Scored per rule as
  written; not softened.

**Block A total = 4+5+5+0 = 14/20**

---

## BLOCK B: CASH GENERATION QUALITY (max 20)

| Year | CFO | PAT |
|---|---|---|
| FY21 | 103.18 | 112.50 |
| FY22 | -134.59 | 125.86 |
| FY23 | -72.66 | 167.27 |
| FY24 | -210.83 | 306.14 |
| FY25 | -519.56 | 294.02 |
| FY26 | -91.28 | 311.89 |

(screener-data)

Cumulative CFO = -925.74 (screener-data, summed)
Cumulative PAT = 1317.68 (screener-data, summed)
Cumulative CFO ÷ Cumulative PAT = **-0.70x**

- B1 Cumulative CFO/PAT -0.70x → <0.50 = **0**
- B2 FCF-positive years: **N/A (not in provided data), scored 0.**
  screener-Data_Sheet's cash flow section carries only three aggregate
  lines (Cash from Operating/Investing/Financing Activity); it does not
  carry the purchase-of-PPE/intangibles line the FCF formula requires,
  and the aggregate "Cash from Investing Activity" also nets in
  investment purchases/sales, so it cannot stand in as capex without
  estimating. Per CLAUDE.md ("never estimate a missing number"), capex
  and FCF are marked N/A rather than derived from balance-sheet asset
  movement.
- B3 Cumulative FCF/PAT: **N/A, same reason, scored 0.**
- B4 Change in WC Days, latest vs earliest: **N/A, scored 0.** Payables
  are not itemized in screener-data (only a lumped "Other Liabilities"
  line that mixes current and non-current items), so Payable Days cannot
  be isolated and the WC Days formula (Receivable + Inventory − Payable)
  is incomplete. Informational only, NOT the scored metric: Receivable
  Days + Inventory Days alone (ex-payables) rose from 26.97 days (FY21)
  to 66.71 days (FY26), screener-data computed.

**Block B total = 0+0+0+0 = 0/20**

Block B trend: **deteriorating**. Cumulative CFO ÷ cumulative PAT =
-0.70x; CFO was negative in 5 of the 6 years (FY22-FY26) while PAT rose
from Rs112.5cr (FY21) to Rs311.89cr (FY26) (screener-data). FY26 CFO
(-91.28) is less negative than FY25 (-519.56), a partial within-year
improvement, but the 6-year structural picture is negative CFO against
rising reported profit.

---

## BLOCK C: GROWTH (max 20)

Revenue: FY21 873.20 | FY22 1133.79 | FY23 2068.17 | FY24 3029.35 |
FY25 3436.73 | FY26 4022.40 (screener-data)
PAT: FY21 112.50 | FY22 125.86 | FY23 167.27 | FY24 306.14 | FY25 294.02 |
FY26 311.89 (screener-data)

Revenue CAGR (FY21→FY26, 5 years) = (4022.40/873.20)^(1/5)-1 = **35.73%**
PAT CAGR (FY21→FY26, 5 years) = (311.89/112.50)^(1/5)-1 = **22.63%**
(both screener-data computed; both endpoints positive, CAGR valid)

- C1 Revenue CAGR 35.73% → ≥20% = **5**
- C2 PAT CAGR 22.63% → ≥20% = **5**
- C3 Positive YoY revenue years: all 5 year-over-year comparisons
  positive (FY22 through FY26) = 100% → **5**
- C4 PAT CAGR minus Revenue CAGR = 22.63 - 35.73 = -13.10pp → <-3pp
  (below -8pp band) = **0**

**Block C total = 5+5+5+0 = 15/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (max 20)

EBITDA (computed as PBT+Depreciation+Interest-Other Income, screener-data):
FY21 159.74 | FY22 185.91 | FY23 295.63 | FY24 517.65 | FY25 518.38 |
FY26 585.43

Latest year (FY26) figures (screener-data):
Borrowings 1311.14 | Cash & Bank 378.68 | Net Worth 2138.14 |
Interest 160.37 | EBIT 577.99 | EBITDA 585.43

Net Debt = 1311.14 - 378.68 = 932.46 (screener-data computed)

- D1 Net Debt/EBITDA = 932.46/585.43 = 1.59x → 1-2x = **3**
- D2 Interest Coverage = EBIT/Interest = 577.99/160.37 = 3.60x → 3-4.9x = **2**
- D3 Debt/Equity = Borrowings/Net Worth = 1311.14/2138.14 = 0.61x →
  0.5-1.0 = **3**
- D4 Current Ratio: **N/A (not in provided data), scored 0.**
  screener-Data_Sheet does not split Total Assets into current/non-current
  or Other Liabilities into current/non-current; only Net Block, CWIP,
  Investments and a lumped "Other Assets" are given on the asset side, and
  a lumped "Other Liabilities" on the liability side. No current ratio is
  computable without estimating the split.

**Block D total = 3+2+3+0 = 8/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (max 20)

inputs/shareholding/ is empty (confirmed at stage 0). screener-Data_Sheet
carries no shareholding-pattern section. No promoter holding, pledge or
change-over-time figures are available in any provided source for this
stage.

- E1 Promoter holding (latest quarter): **N/A (not in provided data), scored 0**
- E2 Promoter holding change over 3 years: **N/A (not in provided data), scored 0**
- E3 Promoter pledge (latest): **N/A (not in provided data), scored 0**
- E4 Contingent liabilities ÷ Net Worth (latest): **N/A (not in provided
  data), scored 0.** This figure sits in the AR financial-statement notes
  (Standalone/Consolidated notes, sheets 74-132); per run instruction this
  stage runs from screener data alone and the AR was not opened.

**Block E total = 0/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (max 60)

EBITDA margin (EBITDA/Sales, screener-data computed):
FY21 18.30% | FY22 16.40% | FY23 14.30% | FY24 17.09% | FY25 15.08% |
FY26 14.56%

Receivable Days (Receivables÷Revenue×365, screener-data, revenue basis):
FY21 15.12 | FY22 30.89 | FY23 55.83 | FY24 51.79 | FY25 71.79 | FY26 57.71

Inventory Days (Inventory÷Revenue×365, screener-data, revenue basis):
FY21 11.85 | FY22 12.43 | FY23 18.87 | FY24 14.25 | FY25 11.01 | FY26 9.00

Gross margin proxy (Revenue−Raw Material Cost)÷Revenue, screener-data,
stated as proxy: FY21 60.87% | FY26 18.46% (informational; no peer
benchmark available)

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 1 | EBITDA margin declined 3.74pp (18.30%→14.56%) despite revenue CAGR 35.73% (≥10%) → "declined 2-5pp despite growth" band (screener-data computed) |
| M2 | Cost Advantage vs peer | 0 | PEER DATA NEEDED, no sector-comp source provided |
| M3 | Capital Efficiency | 3 | FAT (FY26) = Revenue/Net Block = 4022.40/341.15 = 11.79x (>2x); ROCE FY26 16.76% (>15%) → "FAT>2x AND ROCE>15%" band (screener-data computed) |
| M4 | Customer Stickiness | 3 | Zero revenue-decline years (all 5 YoY comparisons positive) satisfies the "max 1 decline year" tier; receivable days rose from 15.12 to 57.71 (not stable ±10, so the top 5-band condition is not met) (screener-data computed) |
| M5 | Scale & Dominance | 0 | PEER DATA NEEDED, no mcap/margin ranking source provided |
| M6 | Technology/R&D | 0 | Not applicable / N/A (not in provided data) — no R&D line item in screener-data; road EPC business model |
| M7 | Regulatory/License | 0 | PEER DATA NEEDED, listed-player count in the road EPC segment not available in provided sources |
| M8 | Distribution | 0 | Not applicable — EPC contractor, no outlet/distribution-reach concept in the business model |
| M9 | Brand | 0 | PEER DATA NEEDED for gross-margin peer median; own GM proxy computed above for reference only |
| M10 | Switching Costs | 0 | Revenue grew every year but receivable days rose 42.59 days (15.12→57.71), failing the stability leg of every tier that requires it; no tier's AND-conditions are satisfied (screener-data computed) |
| M11 | Network Effects | 1 | Latest 2-year window (FY24→FY26) revenue CAGR 15.23% is NOT greater than the prior window (FY21→FY23) 53.91%, so the top band fails; overall FY21-FY26 revenue CAGR 35.73% (>15%) with Selling & Admin expense as % of sales rising (0.80%→1.84%, FY21→FY25; FY26 not reported) → "growth>15% but selling% rising" band (screener-data computed) |
| M12 | Negative WC/Float | 0 | N/A (not in provided data) — Payable Days not computable (payables not itemized; see Block B4), so true WC Days cannot be determined |

**Block F total = 1+0+3+3+0+0+0+0+0+0+1+0 = 8/60**

Moats "present" (score ≥3): M3, M4 = **2 confirmed**
Moat classification: 2-3 present = **MODERATE**

---

## SCORECARD SUMMARY

```
BLOCK A (Return on Capital)        14 / 20  ||||||||||||||......
BLOCK B (Cash Generation Quality)   0 / 20  ....................
BLOCK C (Growth)                   15 / 20  |||||||||||||||.....
BLOCK D (Balance Sheet Strength)    8 / 20  ||||||||............
BLOCK E (Shareholder Alignment)     0 / 20  ....................
-----------------------------------------------------------------
CORE SCORE                         37 / 100

BLOCK F (Quantitative Moat)         8 / 60
Moat bars: M1|. M2.. M3||| M4||| M5.. M6.. M7.. M8.. M9.. M10.. M11| M12..
Moats confirmed (≥3): 2 (M3 Capital Efficiency, M4 Customer Stickiness)
Moat classification: MODERATE

GRAND TOTAL (Core + Moat)          45 / 160
```

Strongest block: Block C (Growth), 15/20 — revenue and PAT CAGR both
strong, revenue grew every year.
Weakest block: Block B (Cash Generation Quality) and Block E (Shareholder
Alignment), both 0/20. Block B is a scored, evidenced weakness
(structurally negative operating cash flow). Block E is an evidence gap,
not a scored weakness (shareholding corpus absent) — flagged separately
from Block B in the classification reasoning.

## DATA CONFIDENCE

6 years of data (FY2021-FY2026) → "5-6 lower" band: flagged "may not have
seen full cycle". This does not trigger the automatic one-tier
classification downgrade (that applies only to the 3-4 year band).
history_downgrade = false.

## DEAL-BREAKER OVERRIDES TRIGGERED

1. Rule 2: Block B (0) < 8 → caps classification at max GOOD.
2. Rule 4: Cumulative CFO/PAT (-0.70x) < 0.50 → caps classification at
   max AVERAGE.
Neither rule 3, 5, 6, 7, 8 or 9 triggers (median ROCE 22.72% is not <10%;
no pledge evidence exists to confirm or deny rule 5; Net Debt/EBITDA
1.59x is not >3x; revenue never declined; PAT positive in FY24, FY25,
FY26; 6 years of history clears the 3-year floor).

## CLASSIFICATION

Core score 37/100 → Core <40 = **AVOID** (matrix rule fires independent
of moat class; the AVOID outcome already sits below both deal-breaker
caps (max GOOD, max AVERAGE), so no conflict between the matrix result
and the override caps).

**FINAL CLASSIFICATION: AVOID**

## DECISION LINE

CEIGALL scores AVOID on Gate 0 at a Core score of 37/100 (Grand total
45/160), driven by a 0/20 cash-generation block (cumulative CFO/PAT
-0.70x, CFO negative in 5 of 6 years against rising PAT) and a 0/20
shareholder-alignment block that is an evidence gap rather than a scored
finding (no shareholding corpus provided). Growth (15/20) and returns on
capital (14/20) are the strongest parts of the profile. Moat evidence is
thin (MODERATE, 2 of 12 tests confirmed) but five of the twelve moat
tests scored 0 purely for missing peer data, not for absence of moat
evidence; the moat read is unconfirmed rather than negative. This is a
mechanical scorecard result; it does not halt the pipeline (no STOP
verdict exists) and the flags below propagate to later stages.
