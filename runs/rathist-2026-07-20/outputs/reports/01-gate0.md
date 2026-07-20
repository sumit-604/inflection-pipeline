# STAGE 1: GATE 0 SCORECARD — Rathi Steel & Power Ltd (RATHIST, BSE 504903)
Run date: 2026-07-20 | Model: Sonnet 5 | Data source(s): screener.in CSV exports + BSE results filings (Q3 FY26 unaudited, Q4/FY26 audited)

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

**LABELING NOTE**: The file prefixed `513456-*` in the peer folder is KANISHK STEEL
INDUSTRIES (a peer), not Rathi. Rathi's own data is drawn exclusively from
`screener-Data_Sheet.csv` (Rathi's real BSE scrip is 504903; the `513456` prefix in
the manifest is a collection error, corroborated by the BSE results PDFs which both
show "Scrip Code: 504903"). The four separate screener export files
(`screener-Profit_Loss.csv`, `screener-Balance_Sheet.csv`, `screener-Cash_Flow.csv`,
`screener-Quarters.csv`) contain only column headers with no populated data rows —
all Rathi figures below are sourced from `screener-Data_Sheet.csv`, cross-checked
against the two BSE results PDFs where the periods overlap (FY2025, FY2026), and
they reconcile exactly (see cross-check note below).

**Cross-check**: screener-Data_Sheet.csv FY26 figures (Sales 716.05cr, Net profit
12.86cr, Total assets 327.19cr, Receivables 56.54cr, Inventory 55.93cr, Cash
2.26cr, Borrowings 44.80cr, Equity 149.89cr, CFO -1.32cr, CFI -22.15cr) all
reconcile to the paisa with the audited Q4/FY26 results PDF (Revenue 716.05cr,
PAT 12.8649cr, Total Assets 327.19cr, Trade receivables 56.5449cr, Inventories
55.9332cr, Cash 2.2636cr, Borrowings 44.80cr, Total Equity 149.8896cr, CFO
-1.3216cr, CFI -22.1506cr). Screener Data_Sheet is treated as reliable for Rathi.

---

## KEY DATA-AVAILABILITY LIMITATION (read before scores below)

`screener-Data_Sheet.csv`'s simplified Balance Sheet bundles all non-equity,
non-borrowing items into a single "Other Liabilities" line and all borrowings
(current + non-current) into a single "Borrowings" line, for every year FY2017–
FY2025. It does **not** split Current Liabilities from Non-Current Liabilities,
and does not itemize Trade Payables separately, for those years. The two BSE
results PDFs only carry a full Statement of Assets & Liabilities (with the
current/non-current split and Trade Payables) for FY2025 and FY2026 (comparative
columns in the Q4/FY26 audited PDF). Similarly, the Cash Flow section of
Data_Sheet.csv gives only aggregate "Cash from Investing Activity" for FY2017–
FY2024 (no isolated Purchase of Fixed Assets / capex line); the audited PDF's
Cash Flow Statement gives capex only for FY2025 and FY2026.

**Consequence**: ROCE (Block A), FCF, and Working-Capital-Days (Block B, B2–B4)
are computable, per the formula definitions in this stage's rules, only for
FY2025 and FY2026. FY2017–FY2024 are marked NOT FOUND for those specific
line items and excluded from those calculations. This is stated explicitly at
each metric below and carried into `data_notes`. It does not affect Revenue/PAT
based metrics (Blocks C, D1–D3 latest-year, which use figures available for
all 10 years or from the audited latest-year balance sheet).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE = EBIT ÷ (Total Assets − Current Liabilities); EBIT computed as PBT +
Interest (screener convention, includes Other Income), "computed" as no
source-provided ROCE series exists in the empty screener Balance_Sheet.csv.
Only FY2025 and FY2026 have a Current Liabilities figure available (see
limitation above).

FY2025: EBIT = PBT 13.95 + Interest 5.50 = 19.45cr (screener Data_Sheet, FY25
col). Capital Employed = Total Assets 265.42cr − Current Liabilities 121.23cr
(Q4 FY26 audited results PDF, Statement of Assets & Liabilities, FY25
comparative col, p.7) = 144.19cr. **ROCE FY25 = 13.49%** (computed).

FY2026: EBIT = PBT 12.87 + Interest 7.42 = 20.29cr (screener Data_Sheet, FY26
col). Capital Employed = Total Assets 327.19cr − Current Liabilities 139.33cr
(Q4 FY26 audited results PDF, Statement of Assets & Liabilities, p.7) =
187.86cr. **ROCE FY26 = 10.80%** (computed).

FY2017–FY2024 ROCE: NOT FOUND (not in provided data — Current Liabilities not
separately reported for these years in screener Data_Sheet.csv).

- **A1 Median ROCE**: median of {13.49%, 10.80%} = 12.15% (only 2 usable
  years) → band 10-14.9% → **Score: 1**
- **A2 Minimum single-year ROCE**: 10.80% (FY26) → band 8-11.9% →
  **Score: 1**
- **A3 Median ROE**: ROE = PAT ÷ average Net Worth. Net Worth (Equity Share
  Capital + Reserves, screener Data_Sheet) was **negative from FY2017 through
  FY2023** (e.g. FY23 Net Worth = 31.31 + (-100.41) = -69.10cr), turning
  positive only in FY2024 (112.67cr) after Equity Share Capital jumped from
  31.31cr to 85.06cr (screener Data_Sheet, FY24 col; shares outstanding rose
  3.13cr → 8.51cr) — consistent with a legacy debt-restructuring/
  recapitalization event. ROE is not meaningful with a negative denominator
  for FY17-FY23 (excluded). FY24 ROE (PAT 23.53 ÷ avg NW 21.79 = 108%) is a
  restructuring artifact (average net worth near zero, crossing from negative
  to positive) and is excluded as N/M.
  Usable years: FY25 ROE = 13.95 ÷ avg(112.67, 128.13)=120.40 = **11.59%**
  (screener Data_Sheet); FY26 ROE = 12.86 ÷ avg(128.13, 149.89)=139.01 =
  **9.25%** (screener Data_Sheet). Median = 10.42% → band <12% →
  **Score: 0**
- **A4 ROCE trend, latest (FY26) vs earliest (FY25, the only two usable
  years)**: 10.80% vs 13.49% = decline of 2.69pp → band decline 1-3pp →
  **Score: 3**

**BLOCK A TOTAL: 5 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO (screener Data_Sheet): FY17 4.81, FY18 NOT FOUND (blank cell), FY19 NOT
FOUND (blank cell), FY20 2.88, FY21 196.32, FY22 -11.75, FY23 105.33, FY24
24.15, FY25 -11.06, FY26 -1.32 (all cr).
PAT (screener Data_Sheet): FY17 -63.31, FY20 -25.63, FY21 190.14, FY22
-36.49, FY23 87.22, FY24 23.53, FY25 13.95, FY26 12.86 (all cr, excluding
FY18/FY19 to match CFO availability).

- **B1 Cumulative CFO ÷ Cumulative PAT** (8 years with both CFO and PAT
  available; FY18/FY19 excluded, NOT FOUND): Cumulative CFO = 309.36cr.
  Cumulative PAT = 202.27cr. Ratio = **1.53x** → band ≥1.00 →
  **Score: 5**
  (Note: FY21 carries an outsized Other Income of 200.67cr and CFO of
  196.32cr, screener Data_Sheet FY21 col — likely a one-off debt-
  restructuring/settlement item that materially inflates this cumulative
  ratio; not adjusted per formula rules, flagged in data_notes.)

- **B2 FCF-positive years as proportion**: FCF = CFO − Capex (Purchase of
  Fixed Assets, from CF statement). Capex is available only for FY25 (22.60cr,
  Q4 FY26 audited PDF Cash Flow Statement, FY25 col, p.8) and FY26 (23.65cr,
  same source, p.8); FY17-FY24 capex NOT FOUND (only aggregate "Cash from
  Investing Activity" available, which the formula excludes).
  FY25 FCF = -11.06 - 22.60 = **-33.66cr**. FY26 FCF = -1.32 - 23.65 =
  **-24.97cr**. 0 of 2 usable years positive (0%) → band <50% →
  **Score: 0**

- **B3 Cumulative FCF ÷ Cumulative PAT** (same 2 usable years): Cumulative
  FCF = -58.63cr. Cumulative PAT (FY25+FY26) = 26.81cr. Ratio = **-2.19**
  → negative → **Score: 0**

- **B4 Change in WC Days, latest (FY26) vs earliest usable (FY25)**: Trade
  Payables only available FY25 (82.43cr) and FY26 (91.35cr) from the Q4 FY26
  audited PDF Statement of Assets & Liabilities (p.7); FY17-FY24 NOT FOUND
  (no Trade Payables line in screener Data_Sheet). Basis: Revenue (COGS not
  separately itemized in provided sources).
  FY25: Receivable Days = 24.77/503.15×365 = 17.97; Inventory Days =
  50.09/503.15×365 = 36.33; Payable Days = 82.43/503.15×365 = 59.79. **WC
  Days FY25 = -5.49**.
  FY26: Receivable Days = 56.54/716.05×365 = 28.83; Inventory Days =
  55.93/716.05×365 = 28.51; Payable Days = 91.35/716.05×365 = 46.57. **WC
  Days FY26 = 10.77**.
  Change = 10.77 − (−5.49) = +16.26 days (increase) → band increase >15 →
  **Score: 0**

**BLOCK B TOTAL: 5 / 20**

**block_b_trend**: improving (but still negative) — CFO improved from
-₹11.06cr (FY25) to -₹1.32cr (FY26); FCF improved from -₹33.66cr (FY25) to
-₹24.97cr (FY26), though both years remain cash-negative on both metrics.

---

## BLOCK C: GROWTH (Max 20)

Sales (screener Data_Sheet, cr): FY17 381.75, FY18 350.01, FY19 350.27, FY20
37.53, FY21 427.30, FY22 542.52, FY23 726.55, FY24 493.19, FY25 503.15, FY26
716.05.
PAT (screener Data_Sheet, cr): FY17 -63.31 … FY26 12.86 (full series above).

**Data quality note on FY2020**: Sales collapsed to 37.53cr against 350.27cr
(FY19) and 427.30cr (FY21) — a >90% single-year anomaly (screener Data_Sheet,
FY20 col), most likely a plant-shutdown/restructuring year. This distorts any
CAGR window that uses FY20 as an endpoint or base; flagged where relevant.

- **C1 Revenue CAGR** (FY17→FY26, 9 years, full available history):
  (716.05/381.75)^(1/9) − 1 = **7.25%** → band 5-9.9% → **Score: 1**
- **C2 PAT CAGR** (FY17→FY26): FY17 PAT = -63.31cr (negative endpoint) →
  **N/M (negative endpoint)** → **Score: 0**.
  data_notes: PAT swung loss-to-profit multiple times across the window:
  losses FY2017-FY2020, profit FY2021, loss FY2022, profit FY2023-FY2026
  (screener Data_Sheet) — no synthetic CAGR attempted.
- **C3 Positive YoY revenue years proportion** (9 YoY comparisons FY18-FY26,
  screener Data_Sheet): declines in FY18 (350.01<381.75), FY20
  (37.53<350.27), FY24 (493.19<726.55) = 3 decline years; 6 of 9 positive =
  66.7% → band 50-74% → **Score: 1** (revenue declined in 3 of 9 years,
  a minority — deal-breaker #7 "revenue declined in majority of years" NOT
  triggered)
- **C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → per rule, **Score: 0**

**BLOCK C TOTAL: 2 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY2026)

Operating EBITDA FY26 (excludes Other Income) = PBT 12.87 + Interest 7.42 +
Depreciation 8.61 − Other Income 0.44 = **28.46cr** (screener Data_Sheet,
FY26 col; cross-checked against Quarters sum: Q1 6.12 + Q2 6.23 + Q3 6.34 +
Q4 9.77 = 28.46, screener Data_Sheet Quarters section).

- **D1 Net Debt ÷ EBITDA (latest)**: Net Debt = Borrowings 44.80cr − Cash
  2.26cr = 42.54cr (screener Data_Sheet, FY26 col, cross-checked against Q4
  FY26 audited PDF p.7: non-current borrowings 12.12cr + current borrowings
  32.68cr = 44.80cr). Net Debt/EBITDA = 42.54/28.46 = **1.50x** → band
  1-2x → **Score: 3**
- **D2 Interest Coverage EBIT ÷ Interest (latest)**: EBIT (excl. Other
  Income) = EBITDA 28.46 − Depreciation 8.61 = 19.85cr. Interest = 7.42cr
  (screener Data_Sheet FY26; matches Q4 FY26 audited PDF Finance cost
  742.06 Lacs). Coverage = 19.85/7.42 = **2.68x** → band 1.5-2.9x →
  **Score: 1**
- **D3 Debt ÷ Equity (latest)**: Debt = 44.80cr (as above). Equity = Equity
  Share Capital 95.26cr + Reserves 54.63cr = 149.89cr (screener Data_Sheet
  FY26; matches Q4 FY26 audited PDF Total Equity 149.8896cr, p.7). D/E =
  44.80/149.89 = **0.30x** → band 0.1-0.5x → **Score: 4**
  (Note: Redeemable Preference Shares of 8.89cr appear in the paid-up
  capital footnote of both results PDFs but are not included in this Equity
  figure or in the audited "Total Equity" line — flagged for downstream
  review as a possible debt-like instrument not captured in D3.)
- **D4 Current Ratio (latest)**: Current Assets 144.61cr ÷ Current
  Liabilities 139.33cr (Q4 FY26 audited PDF, Statement of Assets &
  Liabilities, p.7) = **1.04x** → band 1.0-1.19x → **Score: 1**

**BLOCK D TOTAL: 9 / 20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

The exchange shareholding filing is ABSENT from provided data. E1 and E2 use
the operator-provided screener.in shareholding snapshot
(`inputs/shareholding/screener-shareholding-operator-provided-2026-07-20.md`),
explicitly marked NON-ANCHORED per the run instructions.

- **E1 Promoter holding (latest quarter)**: 41.30% as of Mar 2026 (screener
  SHP snapshot, operator-provided, NON-ANCHORED) → band 40-49.9% →
  **Score: 3**
- **E2 Promoter holding change over 3 years**: Earliest data point in the
  snapshot is Jun 2023 (51.47%) — no Mar 2023 data point exists in the
  provided snapshot, so this uses the nearest available quarter, ~2.75 years
  prior (screener SHP snapshot, operator-provided, NON-ANCHORED). Change =
  41.30% − 51.47% = **-10.17pp** (decreased). The snapshot notes a step-down
  from 51.47% to 40.32% between Dec 2023 and Mar 2024, i.e. within the
  window, not a data artifact. Band: decreased >3% → **Score: 0**
- **E3 Promoter pledge (latest)**: NOT FOUND (not in provided data — no
  pledge column in the operator-provided snapshot, no exchange filing
  provided) → **Score: 0**. Deal-breaker #5 (pledge >15%) cannot be
  confirmed either way and is not applied.
- **E4 Contingent liabilities ÷ Net Worth (latest)**: NOT FOUND (not in
  provided data — no notes-to-accounts or contingent liability disclosure in
  the two results PDFs, which are stock-exchange result summaries, not full
  annual reports) → **Score: 0**

**BLOCK E TOTAL: 3 / 20**

---

## CORE SCORE SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation Quality | 5 | 20 |
| C — Growth | 2 | 20 |
| D — Balance Sheet Strength | 9 | 20 |
| E — Shareholder Alignment | 3 | 20 |
| **CORE TOTAL** | **24** | **100** |

Strongest block: **D — Balance Sheet Strength** (9/20, 45%) — moderate
leverage and coverage, weakest on liquidity (Current Ratio 1.04x).
Weakest block: **C — Growth** (2/20, 10%) — sub-double-digit revenue CAGR,
N/M PAT CAGR off a loss-making base year, and 3 of 9 years with revenue
declines.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set: Kanishk Steel Industries (screener export prefixed `513456-*`,
BSE peer), Scan Steels (`SCANSTL-*`), Vraj Iron & Steel (`VRAJ-*`). Where a
test needed an operating-margin or gross-margin figure, Power & Fuel / Other
Mfr. Exp / Selling & admin lines were blank for FY2026 across **all four**
companies in the screener export (an XBRL-tagging artifact for the latest
period), so operating margin was computed uniformly as (PBT + Interest +
Depreciation − Other Income) ÷ Sales for Rathi and all three peers (state:
proxy used, consistent methodology across companies).

FY2026 operating margin (computed, screener Data_Sheet each company): Rathi
3.97%, Kanishk 3.39%, Scan Steels 5.86%, Vraj Iron & Steel 9.65%. Peer median
(Kanishk, Scan, Vraj) = **5.86%**.

FY2026 gross-margin proxy (Revenue − Material Cost) ÷ Revenue, Material Cost
= Raw Material Cost + Change in Inventory (state: proxy used): Rathi 16.77%,
Kanishk 27.87%, Scan Steels 22.58%, Vraj Iron & Steel 19.51%. Peer median =
**22.58%**.

Market Capitalization (screener Data_Sheet META, cr): Rathi 205.98, Kanishk
149.54, Scan Steels 293.41, Vraj Iron & Steel 445.79.

- **M1 Pricing Power**: Rathi revenue CAGR (FY17-26) = 7.25% (<10% in both
  top bands); FY22-26 operating margin held fairly stable (5.15% → 3.97%,
  computed above) but growth stayed below the 10% CAGR gate required for
  bands 5/3, and margin did not decline (rules out band 1, which requires
  decline) → **else = 0**
- **M2 Cost Advantage vs peer median EBITDA margin**: Rathi 3.97% vs peer
  median 5.86% = **below** → **Score: 0**
- **M3 Capital Efficiency**: FAT = Sales 716.05 ÷ Net Block 98.42 = 7.28x
  (screener Data_Sheet FY26; Net Block is small because the plant is largely
  depreciated, not because of high productivity). ROCE FY26 = 10.80%. FAT>1x
  AND ROCE>12% gate not met (ROCE 10.80% < 12%) → **Score: 0**
- **M4 Customer Stickiness**: 3 revenue-decline years (FY18, FY20, FY24, per
  C3 above) → band "3+ decline years" → **Score: 0**
- **M5 Scale & Dominance**: By market cap, Rathi (205.98cr) ranks 3rd of 4
  in the available peer set (Vraj 445.79 > Scan 293.41 > Rathi 205.98 >
  Kanishk 149.54); by FY26 operating margin Rathi also ranks 3rd of 4. Not
  largest/top-margin, not top-3-mcap-with-top-2-margin. **PEER DATA NEEDED**
  for the full listed segment (only 3 peers provided, real segment likely
  larger) — scored conservatively at **1** ("top 5 mcap" band, unconfirmed
  beyond the 3-peer set)
- **M6 Technology/R&D**: No R&D disclosure in provided data (commodity steel
  reroller) → **N/A (not in provided data)** → **Score: 0**
- **M7 Regulatory/License**: Steel re-rolling is not a licensed/regulated
  segment in the sense of this test → unregulated → **Score: 0**
- **M8 Distribution**: No distribution-network/reach data in provided
  sources → **N/A (not in provided data)** → **Score: 0**
- **M9 Brand**: Rathi gross-margin proxy 16.77% is **below** peer median
  22.58% by 5.81pp → "at/below" → **Score: 0**
- **M10 Switching Costs**: overall revenue growth (FY17→FY26 CAGR positive)
  with 3 decline years (2+) → **Score: 1**
- **M11 Network Effects** (10 years available, ≥6yr test applies): Latest
  3yr CAGR (FY23→FY26) = (716.05/726.55)^(1/3)−1 = **-0.49%**. Prior 3yr
  CAGR (FY20→FY23) = (726.55/37.53)^(1/3)−1 = **+168.6%**, but this is
  computed off the FY2020 anomaly base (37.53cr, see Block C note) and is
  not a meaningful comparator. Given the corrupted base and no selling-
  expense data available for recent years (Selling and admin blank FY26,
  screener Data_Sheet) to test the selling% leg, scored conservatively →
  **Score: 0** (data quality issue noted, not a clean "else" case)
- **M12 Negative WC/Float**: Only 2 years of WC Days computable (see Block
  B4): FY25 -5.49 days, FY26 +10.77 days — both within the 0-15 day band
  (one negative, one modestly positive) → **Score: 3** (2-year sample only,
  flagged)

| Test | Score | Note |
|---|---|---|
| M1 Pricing Power | 0 | |
| M2 Cost Advantage | 0 | below peer median |
| M3 Capital Efficiency | 0 | ROCE gate not met |
| M4 Customer Stickiness | 0 | 3 decline years |
| M5 Scale & Dominance | 1 | PEER DATA NEEDED, 3-peer set only |
| M6 Technology/R&D | 0 | N/A, not in data |
| M7 Regulatory/License | 0 | unregulated |
| M8 Distribution | 0 | N/A, not in data |
| M9 Brand | 0 | below peer median |
| M10 Switching Costs | 1 | growth w/ 2+ decline yrs |
| M11 Network Effects | 0 | FY20 base anomaly, data quality |
| M12 Negative WC/Float | 3 | 2-year sample only |
| **TOTAL** | **5 / 60** | |

Moat profile:
```
M1  [          ] 0
M2  [          ] 0
M3  [          ] 0
M4  [          ] 0
M5  [==        ] 1  (PEER DATA NEEDED)
M6  [          ] 0  (N/A)
M7  [          ] 0
M8  [          ] 0  (N/A)
M9  [          ] 0
M10 [==        ] 1
M11 [          ] 0  (data quality)
M12 [======    ] 3  (present, 2-yr sample)
```

Moats present (score ≥3): 1 (M12 only) → **Moat classification: THIN**

---

## CLASSIFICATION

Data confidence: 10 years of P&L/PAT history (FY2017-FY2026) → "10+ yrs
full" tier per the rules — **no automatic history downgrade**. However,
Blocks A and B are materially constrained: ROCE, FCF and WC Days are
computable for only 2 of those 10 years (FY2025, FY2026) because the
screener export lacks a current/non-current liability split and a capex
line for FY2017-FY2024. This is a data-availability caveat on Block A/B
reliability, separate from the 10-year "full" tier for revenue/PAT history.

Core score: 24/100 (Core < 40)
Moat class: THIN (1 moat present)

**Classification matrix**: Core <40 → **AVOID** (this band overrides moat
tier).

**Deal-breaker overrides** (recorded; classification already at the lowest
tier so these caps are superseded, but noted per pipeline rule to state
which years drive them):
1. Block A <8 (scored 5) → cap max GOOD [superseded by Core<40 AVOID].
   Driven by the only two computable years, FY2025 ROCE 13.49%/ROE 11.59%
   and FY2026 ROCE 10.80%/ROE 9.25%.
2. Block B <8 (scored 5) → cap max GOOD [superseded by Core<40 AVOID].
   Driven by negative FCF in the only two computable years: FY2025
   -33.66cr, FY2026 -24.97cr.
3. Median ROCE <10% → NOT triggered (12.15%, above threshold, but on a
   2-year sample).
4. Cumulative CFO/PAT <0.50 → NOT triggered (1.53x, but built on an
   8-year sum that includes an anomalous FY2021, see data_notes).
5. Pledge >15% → cannot be confirmed (E3 NOT FOUND); not applied.
6. ND/EBITDA >3x AND IC <3x → NOT triggered (ND/EBITDA 1.50x).
7. Revenue declined in majority of years → NOT triggered (3 of 9 years).
8. PAT negative in any of last 3 years (FY24-FY26) → NOT triggered (all
   three positive: 23.53, 13.95, 12.86cr).
9. History <3 years → NOT triggered (10 years available).

**GRAND TOTAL: 24 (core) + 5 (moat) = 29 / 160**

---

## DECISION LINE

**Classification: AVOID.** Core score 24/100 reflects a company that spent
FY2017-FY2023 with negative net worth (legacy debt-restructuring/
recapitalization signature), a FY2020 revenue collapse to 37.53cr, thin and
volatile operating margins throughout, and — even in its recent,
recapitalized state (FY2025-FY2026, the only years with computable balance-
sheet detail) — negative free cash flow and sub-12% ROCE. Only 1 of 12
quantitative moat tests scores as "present" (M12, negative-WC-days, on a
2-year sample). Per pipeline rules there is no STOP verdict and no halt on
company quality; this scorecard and its flags propagate to the next stage
for the decision to be made by the operator, not this stage.

Flag: classification ≤ AVERAGE with historical depressors identified (see
FLAG-GATE0 in the YAML block below).
