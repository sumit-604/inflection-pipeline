# GATE 0 SCORECARD — Aarti Surfactants Ltd (AARTISURF)
Run date: 2026-08-04 | Stage: 1 of pipeline | Model: claude-sonnet-5

Data available: 7 years (FY20 to FY26). Scoring adapted to 7-year history.

**DATA QUALITY ALERT (read before the numbers):**
1. The only populated quantitative source is `screener-Data_Sheet.csv`. The four
   companion CSVs (`screener-Balance_Sheet.csv`, `screener-Cash_Flow.csv`,
   `screener-Quarters.csv`, `screener-Customization.csv`) are all empty Screener.in
   export templates — headers only, zero data rows. Confirmed by direct read.
2. The "annual report" provided is dated and titled **Annual Report 2020-21** (cover
   page, contents page, MD sign-off, auditor's report all say FY 2020-21; 3rd AGM
   held 10-Aug-2021). It is **not** FY2022 as the task brief described — it is one
   year older than briefed, i.e. ~5 years stale relative to this FY26 run, not ~4.
   All AR anchors below are labeled "AR FY2020-21" accordingly.
3. Screener Data_Sheet.csv carries no Trade Payables line, no Current Liabilities
   split, and no itemized capex (only a lump "Cash from Investing Activity"). This
   blocks exact computation of Working Capital Days, Current Ratio, and FCF — each
   is marked NOT FOUND below rather than estimated, per rule 5.
4. No shareholding pattern, promoter pledge, credit rating, or announcements data
   exists anywhere in the provided inputs at a "latest" (FY26 or current-quarter)
   date. The only shareholding snapshot in the entire input set is in the AR
   FY2020-21 (as of 31-Mar-2021) — cited for context only, not scored as "latest."

---

## SOURCE DATA EXTRACTED (screener Data_Sheet.csv, Rs Cr, report-date columns FY20–FY26)

| Line item | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| Sales | 325.86 | 465.77 | 575.52 | 601.29 | 589.86 | 659.09 | 859.13 |
| Raw Material Cost | 248.38 | 356.15 | 462.87 | 468.10 | 445.83 | 542.61 | 720.94 |
| Change in Inventory | 1.07 | 4.77 | 7.33 | -6.24 | -0.72 | 8.30 | -2.16 |
| Power & Fuel | 12.32 | 13.88 | 13.18 | 15.24 | 15.97 | 16.53 | N/A (folded into Other Exp, FY26) |
| Other Mfr. Exp | 21.16 | 23.82 | 22.24 | 21.27 | 24.05 | 21.37 | N/A (folded into Other Exp, FY26) |
| Employee Cost | 14.30 | 15.71 | 18.01 | 16.86 | 17.91 | 20.19 | 23.57 |
| Selling & Admin | 7.16 | 15.27 | 34.25 | 25.62 | 22.90 | 24.33 | N/A (folded into Other Exp, FY26) |
| Other Expenses | 0.02 | 0.21 | 0.16 | 0.21 | 0.35 | 0.44 | 65.57 |
| Other Income | 0.21 | 0.06 | 0.29 | 0.33 | 0.13 | 7.68 | 0.33 |
| Depreciation | 10.58 | 12.21 | 12.45 | 15.49 | 16.04 | 17.35 | 17.69 |
| Interest | 10.28 | 10.44 | 10.67 | 14.79 | 14.03 | 11.55 | 12.31 |
| PBT | 2.94 | 22.91 | 9.31 | 17.80 | 32.19 | 20.70 | 17.22 |
| Net Profit (PAT) | 2.09 | 21.63 | 5.49 | 12.70 | 21.33 | 14.54 | 12.34 |

(screener Data_Sheet.csv, PROFIT & LOSS block, rows 11-24)

Note (data_note): for FY26, Power/Fuel, Other Mfr. Exp, and Selling & Admin are
blank — screener has folded them into "Other Expenses" (65.57), verified by
reconciling: Sales − PBT − Dep − Interest + Other Income = 812.24, and
RM(720.94) + Employee(23.57) + Other Exp(65.57) + Chg.Inv(2.16, sign-adjusted)
= 812.24. Exact match confirms the fold-in; no fabricated split is used anywhere
below — EBITDA is derived from the aggregate, not from a guessed breakdown.

**EBITDA derivation** (Expenses = RM + Power + OtherMfr + Employee + Selling +
OtherExp − Chg.Inv; EBITDA = Sales − Expenses). Cross-checked against
EBITDA = PBT + Dep + Interest − Other Income for every year; all seven years
reconcile exactly (screener Data_Sheet.csv, computed).

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| EBITDA (Cr) | 23.59 | 45.50 | 32.14 | 47.75 | 62.13 | 41.92 | 46.89 |
| EBITDA margin | 7.24% | 9.77% | 5.58% | 7.94% | 10.53% | 6.36% | 5.46% |
| EBIT (=EBITDA−Dep) | 13.01 | 33.29 | 19.69 | 32.26 | 46.09 | 24.57 | 29.20 |

**Balance sheet** (screener Data_Sheet.csv, BALANCE SHEET block, rows 39-51):

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| Net Worth (Equity Cap+Reserves) | 110.95 | 132.65 | 135.91 | 168.03 | 218.11 | 232.63 | 244.92 |
| Borrowings | 108.96 | 151.94 | 161.51 | 149.13 | 99.21 | 110.40 | 104.19 |
| Other Liabilities | 42.38 | 101.94 | 105.01 | 86.50 | 104.99 | 134.15 | 167.55 |
| Total Assets | 262.29 | 386.53 | 402.43 | 403.66 | 422.31 | 477.18 | 516.66 |
| Receivables | 17.92 | 54.43 | 54.47 | 65.36 | 70.11 | 76.26 | 104.65 |
| Inventory | 56.49 | 73.19 | 74.82 | 77.33 | 99.21 | 134.33 | 118.64 |
| Cash & Bank | 0.10 | 6.73 | 1.43 | 7.69 | 6.31 | 1.21 | 13.43 |

**Cash flow** (screener Data_Sheet.csv, CASH FLOW block, rows 57-60):

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| CFO | 18.11 | 35.51 | 23.32 | 24.52 | 51.96 | 11.14 | 76.65 |
| Cash from Investing (aggregate, not itemized capex) | -2.15 | -60.47 | -22.54 | -10.65 | -16.22 | -16.16 | -45.65 |

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Capital Employed proxy used throughout: Net Worth + Total Borrowings (screener-
standard convention). Formula rule calls for Total Assets − Current Liabilities;
screener-Balance_Sheet.csv (the sheet meant to carry Working Capital/Current
Liabilities) is an empty template, so this proxy is used and stated as
"computed" per the rules. This may understate/overstate true capital employed
to the extent Other Liabilities (42.38–167.55 Cr across the years) contains
material non-current items (e.g. deferred tax, ~Rs8-9 Cr per AR FY2020-21 p.73).

| Year | EBIT | Cap. Employed | ROCE (computed) |
|---|---|---|---|
| FY20 | 13.01 | 219.91 | 5.92% |
| FY21 | 33.29 | 284.59 | 11.70% |
| FY22 | 19.69 | 297.42 | 6.62% |
| FY23 | 32.26 | 317.16 | 10.17% |
| FY24 | 46.09 | 317.32 | 14.53% |
| FY25 | 24.57 | 343.03 | 7.16% |
| FY26 | 29.20 | 349.11 | 8.36% |

Median ROCE = 8.36% (screener Data_Sheet.csv, computed). Min single-year ROCE = 5.92% (FY20).

ROE = PAT ÷ average Net Worth; FY20 uses closing Net Worth only (no FY19 opening figure in data).

| Year | PAT | Avg Net Worth | ROE |
|---|---|---|---|
| FY20 | 2.09 | 110.95 (closing only) | 1.88% |
| FY21 | 21.63 | 121.80 | 17.76% |
| FY22 | 5.49 | 134.28 | 4.09% |
| FY23 | 12.70 | 151.97 | 8.36% |
| FY24 | 21.33 | 193.07 | 11.05% |
| FY25 | 14.54 | 225.37 | 6.45% |
| FY26 | 12.34 | 238.78 | 5.17% |

Median ROE = 6.45% (computed).

| Metric | Value | Band | Score |
|---|---|---|---|
| A1 Median ROCE | 8.36% | <10% | **0** |
| A2 Min single-yr ROCE | 5.92% (FY20) | <8% | **0** |
| A3 Median ROE | 6.45% | <12% | **0** |
| A4 ROCE trend latest(FY26 8.36%) vs earliest(FY20 5.92%) | +2.44pp | latest ≥ earliest | **5** |

**Block A subtotal: 5 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY20-26) = 18.11+35.51+23.32+24.52+51.96+11.14+76.65 = **241.21 Cr**
Cumulative PAT (FY20-26) = 2.09+21.63+5.49+12.7+21.33+14.54+12.34 = **90.12 Cr**
(both screener Data_Sheet.csv, computed sums)

| Metric | Value | Band | Score |
|---|---|---|---|
| B1 Cumulative CFO ÷ Cumulative PAT | 241.21/90.12 = 2.68x | ≥1.00 | **5** |
| B2 FCF-positive years proportion | N/A (not in provided data) | — | **0** |
| B3 Cumulative FCF ÷ Cumulative PAT | N/A (not in provided data) | — | **0** |
| B4 Change in WC Days, latest vs earliest | N/A (not in provided data) | — | **0** |

B2/B3 reasoning: FCF = CFO − Capex per the formula rule, where capex must be
"purchase of PPE + intangibles from cash flow statement." screener-Cash_Flow.csv
is an empty template and Data_Sheet.csv gives only the aggregate "Cash from
Investing Activity" (e.g. FY26: -45.65 Cr), which is not decomposed and may
include non-capex items (subsidiary investments, deposits, disposals). Per rule
5 ("never fill gaps with... estimates"), capex is marked NOT FOUND and FCF is
not computed. The raw investing-activity outflows are reported above for
reference only, not used for scoring.

B4 reasoning: WC Days = Receivable Days + Inventory Days − Payable Days. Trade
Payables is not itemized anywhere in the provided screener data (only a
combined "Other Liabilities" balance-sheet line exists, which bundles payables
with non-current items). Receivable Days and Inventory Days are computable
(see Block F below) but Payable Days is NOT FOUND, so the composite WC Days
metric cannot be built and is scored 0/N/A rather than computed on two of
three legs.

**Block B subtotal: 5 / 20**

**block_b_trend detail (feeds FLAG-CASH):** CFO is highly volatile year to
year despite a strong 7-year cumulative CFO/PAT ratio. CFO fell from Rs51.96
Cr (FY24) to Rs11.14 Cr (FY25) — a ratio of just 0.77x that year's PAT of
Rs14.54 Cr, the weakest single-year CFO/PAT conversion in the whole series —
then rebounded sharply to Rs76.65 Cr in FY26 (6.21x FY26 PAT of Rs12.34 Cr).
Net assessment: **improving** in the most recent year, off a working-capital-
driven trough the year before (screener Data_Sheet.csv, CASH FLOW block,
computed).

---

## BLOCK C: GROWTH (Max 20)

Revenue CAGR (FY20→FY26, 6-year window): (859.13/325.86)^(1/6)−1 = **17.53%**
PAT CAGR (FY20→FY26): (12.34/2.09)^(1/6)−1 = **34.44%**

Both endpoints positive (no loss-to-profit swing to note; PAT stayed positive
in all 7 years, screener Data_Sheet.csv).

data_note: FY20 is an unusually depressed base year — PAT of Rs2.09 Cr on
Sales of Rs325.86 Cr is a 0.64% net margin, the weakest year in the series by
a wide margin (next-weakest is FY22 at 0.95%). This inflates the PAT CAGR
computed off that base; treat the 34.44% PAT CAGR as base-effect-driven, not
representative of a steady compounding trend (screener Data_Sheet.csv, computed).

YoY revenue: FY21↑, FY22↑, FY23↑, FY24↓ (589.86 vs 601.29, a 1.9% decline),
FY25↑, FY26↑ → 5 of 6 YoY periods positive = 83.3% (screener Data_Sheet.csv, computed).

| Metric | Value | Band | Score |
|---|---|---|---|
| C1 Revenue CAGR | 17.53% | 15-19.9% | **4** |
| C2 PAT CAGR | 34.44% | ≥20% | **5** |
| C3 Positive YoY revenue years | 5/6 = 83.3% | 75-99% | **3** |
| C4 PAT CAGR − Revenue CAGR | 34.44−17.53=+16.91pp | ≥+3pp | **5** |

**Block C subtotal: 17 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20), latest = FY26

Net Debt (FY26) = Borrowings 104.19 − Cash & Bank 13.43 = 90.76 Cr
Net Debt ÷ EBITDA = 90.76/46.89 = **1.94x** (screener Data_Sheet.csv, computed)

Interest Coverage (FY26) = EBIT 29.20 ÷ Interest 12.31 = **2.37x** (computed)

Debt ÷ Equity (FY26) = Borrowings 104.19 ÷ Net Worth 244.92 = **0.43x** (computed)

Current Ratio (FY26): N/A (not in provided data) — screener Data_Sheet.csv has
no Current Liabilities line and no split of "Other Assets" into current vs
non-current; Current Ratio cannot be built without fabricating a split.

| Metric | Value | Band | Score |
|---|---|---|---|
| D1 Net Debt ÷ EBITDA | 1.94x | 1-2x | **3** |
| D2 Interest Coverage | 2.37x | 1.5-2.9x | **1** |
| D3 Debt ÷ Equity | 0.43x | 0.1-0.5x | **4** |
| D4 Current Ratio | N/A (not in provided data) | — | **0** |

**Block D subtotal: 8 / 20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

All four metrics require "latest quarter" / "latest" data. None exists in the
provided inputs. The only shareholding figure anywhere in the input set is a
5-year-stale AR snapshot, cited below for context only — **not scored** as
"latest," per the input_gaps this run carries (no shareholding CSV, no
announcements, no current rating).

Context only (not scored): Promoter & Promoter Group held 48.68% of equity
shares as on 31-Mar-2021 (AR FY2020-21 p.35, Shareholding Pattern table).
Contingent Liabilities ÷ Net Worth as on 31-Mar-2021 was Rs1,464.41 lakhs ÷
Rs13,266.20 lakhs = 11.04% (AR FY2020-21 p.79 Note 27, p.82 Note 32.1) — again
five years stale relative to this FY26 run, not usable as "latest."

| Metric | Value | Band | Score |
|---|---|---|---|
| E1 Promoter holding (latest quarter) | N/A (not in provided data) | — | **0** |
| E2 Promoter holding change, 3yr | N/A (not in provided data) | — | **0** |
| E3 Promoter pledge (latest) | N/A (not in provided data) | — | **0** |
| E4 Contingent Liab. ÷ Net Worth (latest) | N/A (not in provided data) | — | **0** |

**Block E subtotal: 0 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

| Test | Reasoning | Score |
|---|---|---|
| M1 Pricing Power | EBITDA margin FY20 7.24% → FY26 5.46% = −1.78pp (within ±2pp, "stable" band); Revenue CAGR 17.53% ≥10% (screener Data_Sheet.csv, computed) | **3** |
| M2 Cost Advantage vs peer | PEER DATA NEEDED — no peer margin data provided | **0** |
| M3 Capital Efficiency | FAT (Sales/Net Block, FY26) = 859.13/204.13 = 4.21x (>3x) BUT ROCE FY26 = 8.36% (not >12%, >15%, or >20% on any threshold) — fails the paired ROCE condition at every tier | **0** |
| M4 Customer Stickiness | 1 revenue-decline year (FY24), fully recovered by FY25/FY26 (both > FY23 pre-decline level) → "max 1 decline year, fully recovered" band | **3** |
| M5 Scale & Dominance | PEER DATA NEEDED — no mcap/market-share data provided | **0** |
| M6 Technology/R&D | "Expenditure Incurred on Research and Development: Nil" (AR FY2020-21 p.24, Annexure C) — R&D/Rev = 0% | **0** |
| M7 Regulatory/License | Surfactants manufacturing is not a licensed-oligopoly segment; AR itself notes "the industry is witnessing intensified competition as new players continue to enter the market" (AR FY2020-21 p.11) — unregulated | **0** |
| M8 Distribution | AR references a "well-established and strong distribution network" (AR FY2020-21 p.4) but gives no outlet count, distributor count, or reach metric — mentioned, unquantified | **1** |
| M9 Brand | PEER DATA NEEDED — no peer gross-margin data provided | **0** |
| M10 Switching Costs | Revenue grew in 5 of 6 years (1 decline, FY24) but Receivable Days rose from 20.1 days (FY20) to 44.5 days (FY26, +24.4 days) — fails the "stable" qualifier that the middle tier requires, and doesn't meet the ≤10-day tier either; does not cleanly fit any scored tier | **0** |
| M11 Network Effects | 7 years available (≥6 required). Latest 3yr revenue CAGR (FY23→FY26) = 12.63% vs prior 3yr (FY20→FY23) = 22.65% — deceleration, not acceleration, so top tier fails. Overall Revenue CAGR 17.53% >15% but Selling & Admin % of sales rose from 2.20% (FY20) to 3.69% (FY25, latest isolable year — FY26 not separable, folded into Other Expenses) — net rising over the period despite an intervening peak at 5.95% (FY22) and decline since. Scored conservatively per the "fewer years" fallback instruction given the FY26 selling-expense gap | **1** |
| M12 Negative WC / Float | N/A (not in provided data) — Trade Payables not itemized, so WC Days cannot be computed | **0** |

Revenue CAGR figures used for M11: (601.29/325.86)^(1/3)−1 = 22.65% (prior 3yr);
(859.13/601.29)^(1/3)−1 = 12.63% (latest 3yr) (screener Data_Sheet.csv, computed).

Receivable Days (= Receivables ÷ Sales × 365, Sales basis — COGS not
explicitly separated in the source, so Sales basis stated per rule):

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| Receivable Days | 20.1 | 42.6 | 34.6 | 39.7 | 43.4 | 42.2 | 44.5 |

Inventory Days (Sales basis, same reasoning):

| | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|
| Inventory Days | 63.3 | 57.4 | 47.5 | 46.9 | 61.4 | 74.4 | 50.4 |

(both rows: screener Data_Sheet.csv, computed; Payable Days N/A for both WC
Days and M12, Trade Payables not in provided data)

Moats "present" (score ≥3): M1, M4 → **2 moats present**

**Moat Profile:**
```
M1  Pricing Power        [***      ] 3/5  PRESENT
M2  Cost Advantage       [         ] 0/5  PEER DATA NEEDED
M3  Capital Efficiency   [         ] 0/5
M4  Customer Stickiness  [***      ] 3/5  PRESENT
M5  Scale & Dominance    [         ] 0/5  PEER DATA NEEDED
M6  Technology/R&D       [         ] 0/5
M7  Regulatory/License   [         ] 0/5
M8  Distribution         [*        ] 1/5
M9  Brand                [         ] 0/5  PEER DATA NEEDED
M10 Switching Costs      [         ] 0/5
M11 Network Effects      [*        ] 1/5
M12 Negative WC / Float  [         ] 0/5  N/A (no Trade Payables)
```

**Block F subtotal: 8 / 60**

**Moat classification: 2 present → MODERATE** (band: 2-3 present = MODERATE)

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A Return on Capital | 5 | 20 |
| B Cash Generation | 5 | 20 |
| C Growth | 17 | 20 |
| D Balance Sheet | 8 | 20 |
| E Shareholder Alignment | 0 | 20 |
| **Core score (A-E)** | **35** | **100** |
| F Moat (quantitative) | 8 | 60 |
| **Grand total** | **43** | **160** |

Data confidence: 7 years of history (FY20-FY26) → **7-9 years = moderate**
confidence band. No downgrade tier triggered (not 5-6, not 3-4, not <3).

**Classification matrix application: Core 35 < 40 → AVOID**, independent of
the MODERATE moat class (the Core<40 rule is the binding constraint; the
matrix's Core-based bands take precedence over the moat-adjusted GOOD/GOOD+
outcomes at higher Core scores).

**Deal-breaker overrides checked (all recorded; superseded here by the
harsher Core<40 rule since AVOID is already the floor classification):**
1. Block A < 8 (A=5) → would cap at max GOOD — **triggered**, moot (AVOID is below GOOD)
2. Block B < 8 (B=5) → would cap at max GOOD — **triggered**, moot
3. Median ROCE < 10% (8.36%) → would cap at max AVERAGE — **triggered**, moot
4. Cumulative CFO/PAT < 0.50 → not triggered (2.68x)
5. Pledge > 15% → cannot evaluate, pledge data NOT FOUND
6. ND/EBITDA >3x AND IC <3x → not triggered (ND/EBITDA 1.94x, condition requires both legs)
7. Revenue declined in majority of years → not triggered (1 of 6 YoY periods)
8. PAT negative in any of last 3 years → not triggered (FY24/25/26 all positive)
9. History < 3 years → not triggered (7 years)

**Strongest block: C (Growth), 17/20** — driven by a 17.53% revenue CAGR and
positive operating leverage (PAT CAGR exceeds revenue CAGR by 16.9pp, though
flagged above as partly a low-base effect from FY20).

**Weakest block: E (Shareholder Alignment), 0/20** — entirely a data
availability failure (no shareholding, pledge, or contingent-liability data at
a current date), not necessarily a governance red flag; Block A (Return on
Capital, 5/20) is the weakest block on genuine quantitative substance — median
ROCE of 8.36% and median ROE of 6.45% sit well below GARP-quality thresholds.

**Decision line:** Gate 0 classification is **AVOID** on Core score alone
(35/100, driven by sub-10% median ROCE and ROE across a full 7-year window)
with a MODERATE quantitative moat (2 of 12 tests present: pricing power and
customer stickiness). Historical depressors are name-able: FY20 was a
post-listing/demerger startup year with margins compressed to 0.64% net
margin, and ROCE has never cleared 15% in any of the 7 years on record (peak
14.53% in FY24). This is not a mechanical-failure halt — flags propagate per
project rules; the AVOID classification and its drivers pass to downstream
stages for human weighing, alongside the significant data gaps (no current
shareholding/rating/announcements, no Trade Payables, no capex breakdown)
that should be closed before this classification is treated as final.

---
```yaml
stage: B01-gate0
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results_pdfs: NOT FOUND - no quarterly or annual results PDFs provided for this run"
  - "shareholding_pattern_latest: NOT FOUND - screener CSVs carry no shareholding data; only a single AR FY2020-21 snapshot (Mar 31 2021, Promoter+Promoter Group 48.68%) exists, 5 years stale, used for context only, not scored"
  - "credit_rating_latest: NOT FOUND - only a historical CARE rating action dated Oct 2020 appears in AR FY2020-21 (p.36), no current rating available"
  - "announcements: NOT FOUND - no corporate announcements data provided"
  - "screener_balance_sheet_cash_flow_quarters_customization_csvs: empty Screener.in export templates, header rows only, zero populated data rows (screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv, screener-Customization.csv)"
  - "trade_payables: NOT FOUND - not itemized anywhere in screener-Data_Sheet.csv; blocks WC Days, Current Ratio, and M12 computation"
  - "capex_breakdown: NOT FOUND - screener-Data_Sheet.csv gives only aggregate Cash from Investing Activity, not itemized purchase of PPE/intangibles; blocks FCF computation (B2, B3)"
  - "annual_report_vintage_mismatch: the AR provided is titled and dated Annual Report 2020-21 (FY ended 31-Mar-2021), not FY2022 as briefed in the task; all AR anchors in this report are labeled AR FY2020-21 accordingly, and are 5 years stale relative to this FY26 run, not the ~4 years implied by the brief"
flags:
  - type: FLAG-GATE0
    reason: "Classification is AVOID (Core 35/100, below the <40 AVOID threshold), driven by median ROCE 8.36% and median ROE 6.45% across the full 7-year history (FY20-FY26), neither of which ever clears 12% median. Historical depressor identified: FY20 was a post-listing/demerger startup year (net margin 0.64%, the weakest of all 7 years), and ROCE has not exceeded 15% in any single year on record (peak 14.53%, FY24). Block E (Shareholder Alignment, 0/20) is a data-availability gap, not a scored governance failure - no current shareholding, pledge, or contingent-liability data exists in the provided inputs."
data_years: 7
fy_range: "FY20 to FY26"
blocks: {A: 5, B: 5, C: 17, D: 8, E: 0}
core_score: 35
moat_score: 8
grand_total: 43
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "1: Block A <8 (A=5/20) -> would cap max GOOD; moot, Core<40 rule already yields AVOID"
  - "2: Block B <8 (B=5/20) -> would cap max GOOD; moot, Core<40 rule already yields AVOID"
  - "3: median ROCE <10% (8.36%) -> would cap max AVERAGE; moot, Core<40 rule already yields AVOID"
history_downgrade: false
data_notes:
  - "No loss-to-profit swings across FY20-FY26; PAT positive in all 7 years"
  - "FY20 is an anomalously depressed base year (0.64% net margin, weakest in series) which inflates the FY20->FY26 PAT CAGR (34.44%) computed off that base; treat as base-effect-driven, not steady-state compounding"
  - "Inventory Days and Receivable Days computed on Sales basis, not COGS basis, since COGS is not explicitly a separate line in screener-Data_Sheet.csv (only Raw Material Cost, which is a component, not full COGS); basis stated per rule"
  - "ROCE Capital Employed computed as Net Worth + Total Borrowings (screener-standard proxy), not strict Total Assets - Current Liabilities, because screener-Balance_Sheet.csv (which would carry Current Liabilities) is an empty template; proxy may differ from the strict formula to the extent Other Liabilities contains material non-current items"
  - "PEER DATA NEEDED for M2 (Cost Advantage), M5 (Scale & Dominance), M9 (Brand) - no peer/industry comparison data provided in any input"
  - "FY26 P&L: Power & Fuel, Other Mfr. Exp, and Selling & Admin are blank in screener-Data_Sheet.csv and appear folded into 'Other Expenses' (65.57 Cr); verified by exact reconciliation against Sales-PBT-Dep-Interest+OtherIncome (812.24 Cr matches to the cent); this blocks isolating the FY26 selling-expense ratio used in M11"
  - "Annual report provided is Annual Report 2020-21 (FY ended 31-Mar-2021), not FY2022 as briefed; all AR-sourced figures are dated accordingly and are ~5 years stale relative to this FY26 run"
block_b_trend: "improving - CFO recovered from Rs11.14cr in FY25 (0.77x that year's PAT of Rs14.54cr, the weakest CFO/PAT conversion in the 7-year series) to Rs76.65cr in FY26 (6.21x FY26 PAT of Rs12.34cr), against a 7-year cumulative CFO/Cumulative PAT ratio of 2.68x"
```
