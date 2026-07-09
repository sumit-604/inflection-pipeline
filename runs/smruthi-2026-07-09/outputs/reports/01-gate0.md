# STAGE 1: GATE 0 SCORECARD — Smruthi Organics Ltd (SMRUTHI)
Run date: 2026-07-09 | Data source: screener.in CSV export (FY17-FY26) + results PDFs
Sector: Pharma / CDMO (bulk drugs / API + drug intermediates; Formulations Marketing Division discontinued FY26)

Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year history.

Anchor key: (screener-data) = screener-Data_Sheet.csv (identical content replicated across
main-/financials-/screener- prefixed exports). (results Q4 FY26) = board outcome + audited
standalone financials, filed 13 May 2026, PDF 3264e39f-8d92-4465-b63f-038a79f3d69a.pdf.
(results Q3 FY26) = unaudited nine-month results, filed 13 Feb 2026, PDF
50e16328-5cf0-44b1-aadf-2b810122bfe1.pdf.

DATA GAP NOTE (governs several blocks below): The screener 10-year summary sheet
(screener-/main-/financials-Balance_Sheet.csv) ships with template rows for Working
Capital, Debtor Days, Inventory Turnover, ROE and ROCE — all of these rows are BLANK in
this export. Trade Payables are not itemized at all in the 10-year summary (only
Receivables, Inventory, Cash & Bank are broken out on the asset side). No shareholding
pattern (promoter holding/pledge) or contingent liabilities data is present anywhere in
the provided inputs. No peer/sector financial data is provided. These gaps are called out
per-metric below as "N/A (not in provided data)" / "PEER DATA NEEDED" and scored 0 per
rule 5.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE is NOT provided by the source (template row blank) — computed. Formula used:
EBIT = PBT + Interest (screener-data); Capital Employed = Equity Share Capital + Reserves
+ Borrowings (screener-data), i.e. Total Assets − Other Liabilities, because the 10-year
summary does not split current vs non-current liabilities and therefore "Total Assets −
Current Liabilities" cannot be computed literally from this source. Stated as "computed,
proxy basis."

| FY | EBIT (PBT+Int, Cr) | Cap. Employed (Cr) | ROCE % |
|----|---|---|---|
| FY17 | 6.96 | 64.95 | 10.72% |
| FY18 | -0.60 | 60.49 | -0.99% |
| FY19 | 13.33 | 64.05 | 20.81% |
| FY20 | 15.27 | 58.13 | 26.27% |
| FY21 | 25.14 | 70.40 | 35.71% |
| FY22 | 14.75 | 70.00 | 21.07% |
| FY23 | 5.32 | 73.86 | 7.20% |
| FY24 | 6.38 | 81.32 | 7.85% |
| FY25 | 6.77 | 88.43 | 7.66% |
| FY26 | 6.34 | 81.88 | 7.74% |
(all inputs: screener-data, PROFIT & LOSS / BALANCE SHEET rows)

**A1 Median ROCE = 9.29%** (computed; sorted median of the 10 values above) → <10% → **A1 = 0**
**A2 Minimum single-year ROCE = -0.99% (FY18)** (computed) → <8% → **A2 = 0**

ROE (computed; not provided — template row blank). Net worth = Equity Share Capital +
Reserves (screener-data). FY17 uses closing net worth (no FY16 opening figure available).

| FY | PAT (Cr) | Avg Net Worth (Cr) | ROE % |
|----|---|---|---|
| FY17 | 1.58 | 32.28 (closing, no opening) | 4.90% |
| FY18 | -3.21 | 30.68 | -10.46% |
| FY19 | 6.86 | 32.73 | 20.96% |
| FY20 | 8.45 | 39.43 | 21.44% |
| FY21 | 17.11 | 51.49 | 33.24% |
| FY22 | 10.38 | 63.84 | 16.26% |
| FY23 | 4.13 | 67.67 | 6.10% |
| FY24 | 3.59 | 68.89 | 5.21% |
| FY25 | 3.56 | 70.63 | 5.04% |
| FY26 | 3.43 | 72.58 | 4.73% |
(all inputs: screener-data)

**A3 Median ROE = 5.66%** (computed) → <12% → **A3 = 0**
**A4 ROCE trend latest (FY26 7.74%) vs earliest (FY17 10.72%): decline of 2.98pp** → band
1-3pp decline → **A4 = 3**

**BLOCK A TOTAL = 0+0+0+3 = 3 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY17-26) = 9.17+5.14+12.07+21.43+22.82+2.17+12.11+4.40+9.98+22.26 =
**121.55 Cr** (screener-data, CASH FLOW section)
Cumulative PAT (FY17-26) = 1.58-3.21+6.86+8.45+17.11+10.38+4.13+3.59+3.56+3.43 =
**55.88 Cr** (screener-data, PROFIT & LOSS section)

**B1 Cumulative CFO ÷ Cumulative PAT = 121.55 / 55.88 = 2.18** → ≥1.00 → **B1 = 5**

FCF = CFO − Capex. Capex proxied as the full Cash from Investing Activity outflow (i.e.
FCF = CFO + CFI), since the 10-year summary does not itemize capex separately and
Investments held are immaterial (Rs 0.05-0.20 Cr per screener-data, BALANCE SHEET
section) across the whole period. Cross-check: results PDFs give explicit capex
("Purchases of Fixed Assets, including intangible assets, CWIP & Capital advances") of
Rs 11.52 Cr FY25 and Rs 8.47 Cr FY26 (results Q4 FY26, Statement of Cash Flows, p.9),
close to the CFI figures of -11.42 and -8.92 Cr respectively (screener-data) — proxy
validated for the two years checkable against source documents.

| FY | CFO | CFI (≈ −Capex) | FCF |
|----|---|---|---|
| FY17 | 9.17 | -0.48 | 8.69 |
| FY18 | 5.14 | -3.21 | 1.93 |
| FY19 | 12.07 | -4.50 | 7.57 |
| FY20 | 21.43 | -4.52 | 16.91 |
| FY21 | 22.82 | -3.40 | 19.42 |
| FY22 | 2.17 | +7.15 | 9.32 |
| FY23 | 12.11 | -10.25 | 1.86 |
| FY24 | 4.40 | -7.16 | -2.76 |
| FY25 | 9.98 | -11.42 | -1.44 |
| FY26 | 22.26 | -8.92 | 13.34 |
(all inputs: screener-data, CASH FLOW section)

**B2 FCF-positive years = 8 of 10 = 80%** → band 75-99% → **B2 = 4**
Cumulative FCF = 8.69+1.93+7.57+16.91+19.42+9.32+1.86-2.76-1.44+13.34 = **74.84 Cr**
**B3 Cumulative FCF ÷ Cumulative PAT = 74.84 / 55.88 = 1.34** → ≥0.60 → **B3 = 5**

**B4 Change in WC Days, latest vs earliest = N/A (not in provided data), score 0.**
Trade Payables (needed for Payable Days, and therefore WC Days) are not itemized in the
10-year screener summary for FY17-FY24; only available from results PDFs for FY25
(Rs 15.99 Cr = MSME 1.85 + non-MSME 14.14, results Q4 FY26 p.8) and FY26 (Rs 13.77 Cr,
results Q4 FY26 p.8). The earliest-year figure (FY17) required for the "latest vs
earliest" comparison is genuinely absent — not estimated. For reference only (not
scored), WC Days FY25 = 129.8 days, FY26 = 121.3 days (both Revenue basis: Receivable
Days + Inventory Days − Payable Days; screener-data + results PDFs).

**BLOCK B TOTAL = 5+4+5+0 = 14 / 20**

block_b_trend: **improving.** FY26 CFO of Rs 22.26 Cr (screener-data) is the highest
since FY21 (Rs 22.82 Cr) despite revenue falling 19% YoY, driven by working-capital
release — trade receivables dropped from Rs 32.47 Cr (FY25) to Rs 19.30 Cr (FY26)
(screener-data, BALANCE SHEET section) — reversing two weak FCF years (FY24: -Rs 2.76 Cr,
FY25: -Rs 1.44 Cr).

---

## BLOCK C: GROWTH (Max 20)

Revenue: FY17 Rs 79.35 Cr → FY26 Rs 101.97 Cr (screener-data, PROFIT & LOSS, Sales row).
**C1 Revenue CAGR (9 years) = (101.97/79.35)^(1/9) − 1 = 2.83%** → <5% → **C1 = 0**

PAT: FY17 Rs 1.58 Cr → FY26 Rs 3.43 Cr, both positive endpoints (screener-data, Net
profit row).
**C2 PAT CAGR (9 years) = (3.43/1.58)^(1/9) − 1 = 9.00%** → band 5-9.9% → **C2 = 1**

YoY revenue (screener-data, Sales row), 9 comparisons FY18 vs FY17 through FY26 vs FY25:
FY18 +, FY19 +, FY20 −, FY21 −, FY22 +, FY23 +, FY24 −, FY25 −, FY26 −.
**C3 Positive YoY years = 4 of 9 = 44.4%** → <50% → **C3 = 0**
(Revenue declined in 5 of 9 periods — majority — this trips deal-breaker 7 below.)

**C4 PAT CAGR − Revenue CAGR = 9.00% − 2.83% = +6.17pp** → ≥+3pp → **C4 = 5**

**BLOCK C TOTAL = 0+1+0+5 = 6 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

Net Debt = Borrowings (8.36) − Cash & Bank (2.27) = **Rs 6.09 Cr** (screener-data,
BALANCE SHEET section). EBITDA = EBIT (6.34, = PBT 4.66 + Interest 1.68) + Depreciation
(6.35) = **Rs 12.69 Cr** (screener-data, PROFIT & LOSS section).
**D1 Net Debt ÷ EBITDA = 6.09/12.69 = 0.48x** → band 0-1.0x → **D1 = 4**

**D2 Interest Coverage = EBIT ÷ Interest = 6.34/1.68 = 3.77x** (screener-data) → band
3-4.9x → **D2 = 2**

Net worth FY26 = Equity Share Capital (11.45) + Reserves (62.07) = Rs 73.52 Cr; Debt =
Borrowings Rs 8.36 Cr (screener-data).
**D3 Debt ÷ Equity = 8.36/73.52 = 0.11** → band 0.1-0.5 → **D3 = 4**

Current Ratio uses the FY26 audited Balance Sheet (results Q4 FY26 p.8, Statement of
Assets and Liabilities, standalone): Total Current Assets Rs 5,268.33 lakh ÷ Total
Current Liabilities Rs 2,656.44 lakh.
**D4 Current Ratio = 5268.33/2656.44 = 1.98x** → band 1.5-1.99 → **D4 = 4**

**BLOCK D TOTAL = 4+2+4+4 = 14 / 20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding pattern data (promoter holding, promoter holding change, pledge) and no
contingent liabilities data are present in any provided input (screening CSVs contain no
shareholding sheet; results PDFs cover financial results/board outcomes only, not
shareholding disclosures or notes to accounts).

**E1 Promoter holding (latest quarter) = N/A (not in provided data) → E1 = 0**
**E2 Promoter holding change, 3yr = N/A (not in provided data) → E2 = 0**
**E3 Promoter pledge (latest) = N/A (not in provided data) → E3 = 0**
**E4 Contingent liabilities ÷ Net worth (latest) = N/A (not in provided data) → E4 = 0**

**BLOCK E TOTAL = 0 / 20** (entirely a data-availability gap, not a demonstrated
governance failure — flagged, not to be read as a governance red flag without evidence)

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

**M1 Pricing Power** — EBITDA margin FY17 = (EBIT 6.96+Dep 3.97)/79.35 = 13.77%; FY26 =
12.69/101.97 = 12.44% (screener-data). Margin change = -1.33pp (stable band, ±2pp) but
Revenue CAGR 2.83% < 10%, so top two conditions fail; decline is also not in the 2-5pp
"declined despite growth" band. **M1 = 0**

**M2 Cost Advantage vs peer median EBITDA margin** — PEER DATA NEEDED, no peer financial
data provided this run. **M2 = 0**

**M3 Capital Efficiency** — FAT = Revenue/Net Block = 101.97/46.89 = 2.17x (screener-data);
latest ROCE = 7.74% (computed above). FAT>2x but ROCE not >15%; FAT>1x but ROCE not >12%
either. **M3 = 0**

**M4 Customer Stickiness** — 5 of 9 YoY periods were revenue-decline years (FY20, FY21,
FY24, FY25, FY26) → 3+ decline years band. **M4 = 0**

**M5 Scale & Dominance** — PEER DATA NEEDED (no peer mcap/margin ranking data provided).
**M5 = 0**

**M6 Technology / R&D** — No R&D expense line is reported in the P&L (screener-data); N/A
(not in provided data). Revenue CAGR (2.83%) also below the lowest qualifying band
regardless. **M6 = 0**

**M7 Regulatory / License** — Count of listed peers in the regulated bulk-drug/API segment
not provided. PEER DATA NEEDED. **M7 = 0**

**M8 Distribution** — No quantified distribution/reach data in provided inputs (bulk
drug manufacturer selling to institutional/pharma customers; no network metrics
disclosed). **M8 = 0**

**M9 Brand** — PEER DATA NEEDED for gross margin vs peer median comparison; not scored
without peer data even though a GM proxy (Revenue − Material Cost)/Revenue could be
computed for SMRUTHI alone. **M9 = 0**

**M10 Switching Costs** — Overall revenue growth across the period (FY17 Rs 79.35 Cr →
FY26 Rs 101.97 Cr) with 2+ decline years (5 of 9) → matches "overall growth, 2+ decline
years" band. **M10 = 1**

**M11 Network Effects** — 10 years of history, ≥6yr test applies. Latest 3yr window
(FY23→FY26) CAGR = (101.97/141.04)^(1/3)−1 = -10.24%; prior 3yr window (FY20→FY23) CAGR =
(141.04/131.07)^(1/3)−1 = +2.47% (screener-data). Latest window is NOT greater than prior
window, and growth is negative (fails ≥20% and >15% bands too). **M11 = 0**

**M12 Negative WC / Float** — Cannot be scored reliably: Trade Payables (required for WC
Days) are absent for 8 of the 10 years (see Block B4 note). For the 2 years checkable
(FY25, FY26 from results PDFs), WC Days were 129.8 and 121.3 respectively — both firmly
positive and well above the >45-day band, so even on the available sample this would not
score above 0. Scored conservatively. **M12 = 0**

**BLOCK F TOTAL (moat score) = 1 / 60**

### Moat Profile
```
M1  Pricing Power       [          ] 0/5
M2  Cost Advantage      [          ] 0/5  PEER DATA NEEDED
M3  Capital Efficiency  [          ] 0/5
M4  Customer Sticky     [          ] 0/5
M5  Scale & Dominance   [          ] 0/5  PEER DATA NEEDED
M6  Tech / R&D          [          ] 0/5
M7  Regulatory/License  [          ] 0/5  PEER DATA NEEDED
M8  Distribution        [          ] 0/5
M9  Brand               [          ] 0/5  PEER DATA NEEDED
M10 Switching Costs     [##        ] 1/5
M11 Network Effects     [          ] 0/5
M12 Negative WC/Float    [          ] 0/5
```
Moats present (score ≥3): **0**. Moat classification: 0 present → **NONE**

---

## CLASSIFICATION AND OVERRIDES

**Core score = A(3) + B(14) + C(6) + D(14) + E(0) = 37 / 100**
**Moat score = 1 / 60**
**Grand total = 38**

Data confidence: 10 years (FY17-FY26) → **10+ yrs full** confidence tier. No history
downgrade applies (history_downgrade = false).

Classification matrix lookup: Core score 37 is <40 → **AVOID** (independent of moat
class).

### Deal-breaker overrides (recorded; do not raise a classification, only cap it — base
matrix result of AVOID is already the floor, so none of these caps binds above it, but
all are recorded per instructions with the years driving them):

1. **Block A < 8 (actual 3) → cap max GOOD.** Driven by FY23-FY26 ROCE compression to
   7.2-7.9% (vs FY19-FY21 peak of 20.8-35.7%) and FY18's -0.99% trough.
2. Block B < 8: not triggered (actual 14).
3. **Median ROCE < 10% (actual 9.29%) → cap max AVERAGE.** Driven by FY23, FY24, FY25,
   FY26 all sitting at 7.2-7.9%, dragging the 10-year median below the FY19-FY22 boom
   years (20.8-35.7%).
4. Cumulative CFO/PAT < 0.50: not triggered (actual 2.18).
5. Pledge > 15%: cannot be evaluated — N/A (not in provided data); not triggered for lack
   of evidence, not asserted clean.
6. ND/EBITDA > 3x AND IC < 3x: not triggered (0.48x / 3.77x).
7. **Revenue declined in majority of years (5 of 9 YoY periods) → cap max AVERAGE.**
   Driven by FY20, FY21 (COVID-period demand/pricing normalization after a strong FY19),
   and the consecutive FY24, FY25, FY26 declines, the latter compounded by the FY26
   discontinuation of the Formulations Marketing Division (results Q4 FY26, Note 1, p.7).
8. PAT negative in any of last 3 years: not triggered (FY24 3.59, FY25 3.56, FY26 3.43,
   all positive).
9. History < 3 years: not triggered (10 years available).

Net effect: deal-breakers 1, 3 and 7 fire, capping at GOOD and AVERAGE respectively — both
less restrictive than the base matrix result of AVOID, so the binding classification
remains **AVOID**.

### Strongest / weakest block
- Strongest (of the scored, data-available blocks): **Block B (Cash Generation Quality)
  and Block D (Balance Sheet Strength), tied at 14/20 (70%)**. Cash conversion is
  genuinely strong (cumulative CFO/PAT 2.18x, cumulative FCF/PAT 1.34x) and the balance
  sheet is lightly levered (Net Debt/EBITDA 0.48x, D/E 0.11x).
- Weakest by score: **Block E (Shareholder Alignment), 0/20** — but this reflects a
  complete data gap (no shareholding/pledge/contingent liability data provided), not a
  demonstrated governance failure.
- Weakest by demonstrated company performance: **Block A (Return on Capital), 3/20
  (15%)** — median ROCE 9.29% and median ROE 5.66% both sit well below GARP screening
  thresholds, and the trend is a structural step-down from FY19-FY22 boom-era returns to
  a sub-8% ROCE plateau across FY23-FY26.

---

## CLASSIFICATION BOX

```
┌─────────────────────────────────────────────┐
│ SMRUTHI ORGANICS LTD — GATE 0 SCORECARD      │
│                                               │
│ Core Score:        37 / 100                  │
│ Moat Score:          1 / 60  (NONE)          │
│ Grand Total:        38                       │
│                                               │
│ Data Confidence:   10+ yrs FULL              │
│ Classification:    AVOID                     │
│ Deal-breakers hit: DB1, DB3, DB7             │
└─────────────────────────────────────────────┘
```

### Decision line
Gate 0 mechanical screen classifies SMRUTHI as **AVOID** on a Core score of 37/100 (Block
A 3, Block B 14, Block C 6, Block D 14, Block E 0) plus a moat score of 1/60 (NONE — 0 of
12 tests present, 4 blocked on PEER DATA NEEDED). The cash-generation and balance-sheet
metrics are genuinely solid (CFO/PAT 2.18x, Net Debt/EBITDA 0.48x), but returns on capital
have structurally reset from a FY19-FY21 boom (ROCE up to 35.7%) to a sub-8% plateau
across FY23-FY26, and revenue has declined in 5 of the last 9 years including three
straight years into FY26 (compounded by the FY26 discontinuation of the Formulations
Marketing Division). Per pipeline rules this is a mechanical, non-halting classification —
flags propagate downstream; the run continues through subsequent stages with this
scorecard as an anchor data point, not a stop signal.

---
