# STAGE 1: GATE 0 QUANTITATIVE SCORECARD — Orchid Pharma Ltd (ORCHPHARMA)
Run date: 2026-09-06 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history,
per screener-Data_Sheet.csv (the sole populated screener export; screener-Profit_Loss,
Balance_Sheet, Cash_Flow and Quarters CSVs are empty templates, a known
collect_to_repo v3 defect, per orchestrator instruction).

FY2026 has no primary filing in this corpus (no FY2026 annual report, no FY2026
audited results). FY2026 Data_Sheet figures are screener aggregates, marked
unverified throughout. The FY2026 cost-line split (Power and Fuel, Other Mfr.
Exp, Selling and admin) is blank in the export; treated as NOT FOUND. FY2026
PBT/Interest/Depreciation figures are intact (they are direct P&L subtotals,
not built from the blank cost lines), so EBIT/EBITDA could still be derived,
but every FY2026 number below carries the "unverified, screener-sourced" tag.

A material internal inconsistency was found and is flagged, not smoothed: the
FY2026 annual PBT (Data_Sheet) is 10.43cr, but the sum of the four quarters
that make up FY2026 (Jun-25, Sep-25, Dec-25, Mar-26 in the Quarters block) is
-6.89-3.33-12.15+24.85 = 2.48cr, a gap of ~7.95cr with no reconciling note in
corpus (screener-data, Data_Sheet Quarters block). Not resolved here.

Capital Employed methodology note: Data_Sheet's balance sheet does not split
current vs non-current liabilities; "Other Liabilities" is the plug for
everything beyond Equity Share Capital + Reserves + Borrowings. ROCE below is
computed as EBIT ÷ (Equity Share Capital + Reserves + Borrowings), i.e.
Capital Employed = Total Assets − Other Liabilities, the standard proxy when
no current/non-current split exists, and is marked "computed" throughout.
EBIT = PBT + Interest (screener-data), robust to the FY2026 cost-line gaps
since PBT and Interest are direct subtotals.

Equity/net-worth reconciliation note: AR2025 standalone Total Equity (Equity
Share Capital + Other Equity) is 1,324.05cr for FY2025 (Annual_Report_2025.pdf,
p.177) and 1,218.32cr for FY2024 (Annual_Report_2024.pdf, p.157), while
Data_Sheet's Equity Share Capital + Reserves gives 1,267.29cr (FY2025) and
1,169.47cr (FY2024) — gaps of 56.76cr and 48.85cr respectively. Both figures
are anchored; ROE/D-E below use the Data_Sheet figure for consistency across
the 10-year series, with the AR figure cited as a cross-check. The gap does
not change any banding.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Capital Employed (Equity Share Capital + Reserves + Borrowings, screener-data,
computed) and ROCE (= EBIT ÷ Capital Employed, computed) by year:

| FY | EBIT (cr) | Cap. Employed (cr) | ROCE % |
|----|-----------|--------------------|--------|
| 17 | -197.00 | 2,639.41 | -7.46 |
| 18 | -88.70 | 2,410.19 | -3.68 |
| 19 | 76.10 | 2,525.92 | 3.01 |
| 20 | -124.84 | 1,332.38 | -9.37 |
| 21 | -64.32 | 1,105.65 | -5.82 |
| 22 | 35.04 | 915.34 | 3.83 |
| 23 | 81.37 | 1,019.99 | 7.98 |
| 24 | 108.68 | 1,304.65 | 8.33 |
| 25 | 110.49 | 1,441.90 | 7.66 |
| 26 | 19.41 | 1,650.38 | 1.18 (unverified) |

(all inputs: screener-data, Data_Sheet.csv P&L and Balance Sheet blocks)

**A1 Median ROCE (10yr) = 2.10%** (midpoint of 3.01 and 1.18, sorted series)
→ <10% → **score 0**
Context (not scored, stated per orchestrator instruction 4): restricting to
post-restructuring FY2022-FY2026, median ROCE = 7.66% — still under the 10%
band. The low score is NOT purely a pre-restructuring artifact: even the best
clean year (FY2024, 8.33%) never cleared 10%.

**A2 Minimum single-year ROCE = -9.37% (FY2020)** → <8% → **score 0**
Context: minimum of the post-restructuring years alone is 1.18% (FY2026,
unverified) or 3.83% (FY2022, audited) — both still <8%.

**A3 Median ROE.** Net Worth = Equity Share Capital + Reserves (screener-data).
FY2017-FY2020 ROE marked N/M: net worth is negative (FY17-19) or transits
through the FY2020 CDR restructuring (equity capital 88.96→40.82cr, reserves
-793.00→+725.17cr in one step), making the ratio uninterpretable. Median taken
over the 6 valid years (FY21-FY26): -16.43, -0.30, 0.78, 6.93, 8.18, 0.78/6.93
midpoint → **median = 3.86%** → <12% → **score 0**

**A4 ROCE trend, latest (FY26 = 1.18%, unverified) vs earliest (FY17 = -7.46%):**
latest ≥ earliest → **score 5**
Flagged: this passes only because the earliest year was catastrophically
negative; it is not evidence of a strong current trend (FY24 and FY25, both
audited, were higher than FY26 at 8.33% and 7.66%).

**BLOCK A TOTAL = 0+0+0+5 = 5 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

**B1 Cumulative CFO ÷ Cumulative PAT, FY17-FY26** (screener-data): Cumulative
CFO = 883.76cr. Cumulative PAT = -780.23cr (negative — FY17-21 losses
dominate). Ratio is not meaningful with a negative denominator; literal value
-1.13 <0.50 → **score 0**
Context: FY2022-FY2026 subset (screener-data): Cumulative CFO = 357.22cr,
Cumulative PAT = 246.16cr, ratio = 1.45 (would score 5 on that window alone).
The low score on the scored (full) window is a legacy-loss effect, stated per
orchestrator instruction 4.

**B2 FCF-positive years as proportion.** Capex (purchase of PPE incl. CWIP
changes) is absent from Data_Sheet for all 10 years; sourced from AR cash
flow statements, available for FY2023-FY2025 only (no earlier AR, no FY2026
filing):
- FY2023: CFO 13.39cr (Annual_Report_2024.pdf, p.161) − Capex 84.55cr
  (Annual_Report_2024.pdf, p.158) = **FCF -71.16cr**
- FY2024: CFO 130.73cr (Annual_Report_2024.pdf, p.161) − Capex 55.15cr
  (Annual_Report_2024.pdf, p.158) = **FCF +75.58cr**
- FY2025: CFO 27.48cr (Annual_Report_2025.pdf, p.180) − Capex 68.54cr
  (Annual_Report_2025.pdf, p.180) = **FCF -41.06cr**
1 of 3 years positive = 33% → <50% → **score 0**
(FY17-22 and FY26 capex: NOT FOUND, no primary source in corpus.)

**B3 Cumulative FCF ÷ Cumulative PAT** (same 3-year window, the only window
with primary capex data): Cumulative FCF = -36.64cr. Cumulative PAT (FY23-25,
screener-data) = 238.15cr. Ratio = -0.15 → negative → **score 0**

**B4 Change in WC Days, latest vs earliest available.** Trade Payables are
absent from Data_Sheet for all years; sourced from AR standalone balance
sheets, available FY2023-FY2025 only:
- FY2023: Receivables 215.19cr, Inventory 228.74cr, Sales 665.90cr (all
  screener-data), Payables 129.11cr (=12,910.61 lakh, Annual_Report_2024.pdf,
  p.158, note 27, MSME + other creditors). Receivable Days 117.97, Inventory
  Days 125.36, Payable Days 70.75 (Revenue basis throughout; Raw Material Cost
  alone is not equivalent to full COGS, so COGS basis not used, stated per
  formula rule). **WC Days = 172.58**
- FY2024 (context): Payables 179.39cr (Annual_Report_2024.pdf, p.158). WC Days
  = 124.91 (non-monotonic dip, noted, not scored)
- FY2025: Payables 170.48cr (=17,047.89 lakh, Annual_Report_2025.pdf, p.234,
  note 28). Receivable Days 95.75, Inventory Days 129.20, Payable Days 67.51.
  **WC Days = 157.44**
Change FY2025 vs FY2023 = -15.14 days (decrease >5 days) → **score 5**

**BLOCK B TOTAL = 0+0+0+5 = 5 / 20**

block_b_trend: **deteriorating** — FCF swung from +75.58cr (FY24) to -41.06cr
(FY25) as capex (68.54cr) outran CFO (27.48cr); the only 3-year window with
primary capex evidence shows a negative cumulative FCF/PAT ratio (-0.15).

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-data): FY17 796.51cr → FY26 1,232.78cr (9-year span).
YoY: FY18 decline, FY19 decline, FY20 decline, FY21 decline, FY22 increase,
FY23 increase, FY24 increase, FY25 increase, FY26 increase (4 declines / 9
periods).

**C1 Revenue CAGR (FY17→FY26, 9yr)** = (1232.78/796.51)^(1/9)-1 = **4.97%**
→ <5% (sits just under the cutoff) → **score 0**
Context: FY2021 trough (450.06cr) → FY2026 (1,232.78cr), 5yr CAGR = 22.33% —
would score 5. The scored figure is dragged below the 5% line entirely by the
FY18-21 decline years; stated per orchestrator instruction 4.

**C2 PAT CAGR (FY17→FY26)**: FY17 PAT = -495.43cr, a negative endpoint →
**N/M, score 0**. data_notes: PAT swung loss→profit→loss→profit across the
window — loss FY17-18, marginal profit FY19 (69.41cr), loss FY20-22, profit
FY23-26 (46.32 → 92.17 → 99.66 → 9.96cr, the last unverified).

**C3 Positive YoY revenue years proportion** = 5/9 = 55.6% → 50-74% band
→ **score 1**

**C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → **score 0**, per CAGR
edge rule for C4.

**BLOCK C TOTAL = 0+0+1+0 = 1 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Latest = FY2026 (screener aggregate, unverified, no primary filing).
FY2025 (last audited year) shown alongside for every line as context.

**D1 Net Debt ÷ EBITDA (latest).**
FY2026: Net Debt = Borrowings 362.59cr − Cash & Bank 83.21cr = 279.38cr.
EBITDA = EBIT 19.41cr + Depreciation 43.25cr = 62.66cr (screener-data,
computed). ND/EBITDA = **4.46x** → >3x → **score 0**
FY2025 context: Net Debt = 174.61 − 179.63 = **-5.02cr (net cash)** → would
score 5. EBITDA = 110.49+34.55 = 145.04cr.

**D2 Interest Coverage (EBIT ÷ Interest, latest).**
FY2026: 19.41 ÷ 8.98 = **2.16x** → 1.5-2.9 band → **score 1**
FY2025 context: 110.49 ÷ 14.93 = **7.40x** → would score 4.

**D3 Debt ÷ Equity (latest).**
FY2026: Borrowings 362.59cr ÷ Equity (Data_Sheet, 1,287.79cr) = **0.28** →
0.1-0.5 band → **score 4**

**D4 Current Ratio (latest).**
FY2026: **NOT FOUND** — no FY2026 primary filing exists, and Data_Sheet does
not split current assets/liabilities → **score 0** (data-availability zero,
not a fundamentals finding).
Context, both from primary filings: FY2025 Total current assets 786.39cr ÷
Total current liabilities 237.47cr = **3.31x** (Annual_Report_2025.pdf,
p.233-234, standalone balance sheet, Data_Sheet cross-check: Trade
receivables 24,183.21 lakh matches Data_Sheet Receivables FY25 241.83cr
exactly). FY2024: 782.29cr ÷ 209.67cr = 3.73x (Annual_Report_2024.pdf,
p.157). FY2023: 493.79cr ÷ 326.63cr = 1.51x (Annual_Report_2024.pdf, p.157).
All three audited years would score 4-5.

**BLOCK D TOTAL = 0+1+4+0 = 5 / 20**

Deal breaker 6 (ND/EBITDA >3x AND IC <3x → AVOID) is TRIGGERED on FY2026
figures alone. This is flagged prominently: it rests entirely on unverified,
screener-sourced FY2026 numbers with a known broken cost-line split and an
unreconciled ~7.95cr quarterly-vs-annual PBT gap (see header). On FY2025 (the
latest AUDITED year), neither leg of deal breaker 6 fires (net cash, IC
7.40x).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding-pattern filing and no results PDF exist in this corpus, so
promoter holding, pledge, and contingent liabilities were sought first in
Annual_Report_2025.pdf, then Annual_Report_2024.pdf, per orchestrator
instruction 2.

**E1 Promoter holding (latest).** 69.84% as on 31-Mar-2025 (Annual_Report_
2025.pdf, p.93-94, Corporate Governance Report, Shareholding Pattern table:
3,54,19,957 of 5,07,19,105 shares) → ≥60% → **score 5**

**E2 Promoter holding change.** Only two data points exist in corpus: 69.84%
as on 31-Mar-2024 (Annual_Report_2024.pdf, p.75, same 3,54,19,957 shares) and
69.84% as on 31-Mar-2025 (as above) — unchanged, a 1-year proxy, NOT a true
3-year trend (no earlier AR in corpus to establish FY2022 or FY2023 holding).
Change = 0.00% → ±1% band → **score 3**, noted as a 1-year proxy.

**E3 Promoter pledge (latest).** NOT FOUND. Checked Annual_Report_2025.pdf
(Corporate Governance Report shareholding table, p.93-94: no encumbrance/
pledge column) and Annual_Report_2024.pdf (p.75: same table format, no
pledge column) — neither AR discloses a pledge/encumbrance figure. → **score
0**, a data-availability zero, not an evidenced pledge finding.

**E4 Contingent liabilities ÷ Net Worth (latest).** Contingent liabilities
(Consolidated Financial Statements, note 45, FY2025): GST dispute 144.22 lakh
+ Electricity Department claim 112.44 lakh + Other claims 379.78 lakh +
Unexpired LC/BG 773.20 lakh = 1,409.64 lakh = **14.10cr** (Annual_Report_
2025.pdf, p.264-265, note 45; consolidated basis used, no separate standalone
note 45 was located in the extracted text — flagged, subsidiaries are
described elsewhere in the AR as largely dormant, so the consolidated figure
is treated as a close proxy). Excludes capital commitments (296.43cr,
estimated contracts on capital account not provided for — a separate,
forward capex item, not a contingent liability). Net Worth (Data_Sheet,
FY2025) = 1,267.29cr. Ratio = 14.10 ÷ 1,267.29 = **1.11%** → <5% → **score 5**

**BLOCK E TOTAL = 5+3+0+5 = 13 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer EBITDA and gross margins computed from the three peer Data_Sheet.csv
files (context-only, per orchestrator instruction), FY2025, using the
verified sign convention Change in Inventory is SUBTRACTED from Raw Material
Cost (cross-checked: this reconciles Orchid, Neuland, Kopran and Granules
FY2025 stated PBT exactly in every case).

| | Sales FY25 (cr) | EBITDA excl. other income (cr) | EBITDA margin | GM proxy (Sales-RM)/Sales |
|---|---|---|---|---|
| Orchid | 921.93 | 117.89 | 12.79% | 36.21% |
| Neuland Labs | 1,476.84 | 330.58 | 22.39% | 60.83% |
| Kopran | 629.60 | 72.90 | 11.58% | 34.77% |
| Granules India | 4,481.61 | 947.72 | 21.15% | 61.51% |
| **Peer median (3)** | | | **21.15%** | **60.83%** |

**M1 Pricing Power.** EBITDA margin (excl. other income), audited years:
FY23 12.68%, FY24 13.58%, FY25 12.79% — stable within ±2pp. Revenue CAGR
FY23→FY25 = 17.67% ≥10%. → **score 3**
Flagged: FY2026 (unverified) shows margin collapsing to ~2.7% (excl. other
income) or ~5.1% (incl.) — not used for scoring since the FY26 cost split is
broken, but a material caveat on the direction implied.

**M2 Cost Advantage vs peer median EBITDA margin.** Orchid 12.79% vs peer
median 21.15% → 8.36pp BELOW → **score 0**

**M3 Capital Efficiency.** FAT (FY25) = Sales 921.93 ÷ Net Block 632.71 =
1.46x (>1x) but ROCE FY25 = 7.66% (<12%) → fails the ROCE leg → **score 0**

**M4 Customer Stickiness.** 4 revenue-decline years (FY18-21) in the 10-year
window → 3+ decline years → **score 0**
Context: zero decline years FY2022-FY2026.

**M5 Scale & Dominance.** Market cap (screener-data, meta): Orchid 5,716.94cr,
Neuland 29,072.53cr, Granules 21,020.61cr, Kopran 1,122.83cr. Orchid ranks
3rd of 4 (top-3 mcap). EBITDA margin rank: Orchid also 3rd of 4 (not top-2).
"top3 mcap AND margin top2" fails → falls to "top5 mcap" → **score 1**.
Flagged PARTIAL: only 3 named peers were supplied; true segment ranking
(all listed Cephalosporin API/FDF players) is PEER DATA NEEDED beyond this
set.

**M6 Technology / R&D.** R&D cost (Consolidated FS, note 43, "Research and
Development"): FY2025 = 139.31+663.14+31.55+1.18+0.80+0.70 = 836.68 lakh =
8.37cr, R&D/Revenue = 0.91% (Annual_Report_2025.pdf, p.264). FY2024 = 148.35+
483.69+24.65+6.15+0.77+6.75 = 670.36 lakh = 6.70cr, R&D/Revenue = 0.82%.
Below the 1% floor in both years, and margin is below peer median (M2) →
**score 0**

**M7 Regulatory / License.** Orchid discloses regulatory-filing counts (48
cumulative US DMFs, 15 EU COS, 8 Japan JDMFs, Annual_Report_2025.pdf, p.29-30)
but no count of competing LISTED players in the Cephalosporin API/FDF segment
is disclosed anywhere in corpus → **PEER DATA NEEDED, score 0**

**M8 Distribution.** "exports spanning over 40 countries" is disclosed
(Annual_Report_2025.pdf, p.240, note 1 Corporate Information) — reach IS
quantified, but no prior-year baseline exists to show it growing, and
"revenue per outlet" does not map to a B2B bulk-API/FDF exporter (no retail
outlet concept). Scored conservatively at the "mentioned" tier given the
absence of a growth data point → **score 1**, flagged as a business-model
mismatch with the test's FMCG-distribution framing.

**M9 Brand.** GM proxy: Orchid 36.21% vs peer median 60.83% → 24.6pp BELOW
→ at/below → **score 0**

**M10 Switching Costs.** Overall growth FY17→FY26 (up) with 4 decline years
(≥2) → **score 1**

**M11 Network Effects.** Latest 3yr revenue CAGR (FY23→FY26) = (1232.78/
665.90)^(1/3)-1 = 22.80%. Prior 3yr CAGR (FY20→FY23) = (665.90/483.80)^(1/3)-1
= 11.23%. Latest > prior. Selling and admin % of sales: FY20 13.17%, FY23
4.81%, FY24 5.54%, FY25 5.03% — declining (FY26 selling% NOT FOUND, broken
cost split). Latest3yr CAGR > prior3yr AND selling% declining → **score 5**

**M12 Negative WC / Float.** WC Days (the only 3 years with primary payables
data): FY23 172.58, FY24 124.91, FY25 157.44 — all far above 45 → **score 0**

**BLOCK F (MOAT) TOTAL = 3+0+0+0+1+0+0+1+0+1+5+0 = 11 / 60**

Moat profile bars:
```
M1  [###......] 3   M2  [..........] 0   M3  [..........] 0
M4  [..........] 0   M5  [#.........] 1   M6  [..........] 0
M7  [..........] 0   M8  [#.........] 1   M9  [..........] 0
M10 [#.........] 1   M11 [#####.....] 5   M12 [..........] 0
```
Moats present (score ≥3): M1 (Pricing Power), M11 (Network Effects proxy) = 2
**Moat classification: 2 present → MODERATE**

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation Quality | 5 | 20 |
| C — Growth | 1 | 20 |
| D — Balance Sheet Strength | 5 | 20 |
| E — Shareholder Alignment | 13 | 20 |
| **Core score** | **29** | **100** |
| F — Moat (MODERATE) | 11 | 60 |
| **Grand total** | **40** | **160** |

Data confidence: 10 years available → "full" tier, no data-confidence
downgrade. (Block B's capex/payables sub-metrics rest on only 3 years of
primary AR data — flagged throughout, not treated as a confidence downgrade
of the whole scorecard.)

Base matrix: Core 29 <40 → **AVOID**

Deal-breaker overrides triggered:
1. Block A (5) <8 → max GOOD
2. Block B (5) <8 → max GOOD
3. Median ROCE (2.10%) <10% → max AVERAGE
4. Cumulative CFO/PAT <0.50 (literal, negative-PAT-driven) → max AVERAGE
6. ND/EBITDA (4.46x, FY2026 unverified) >3x AND IC (2.16x, FY2026 unverified)
   <3x → **AVOID**

Not triggered: 5 (pledge — no evidence either way, data unavailable), 7
(revenue declined in a majority of years — false, 5 of 9 YoY periods
increased), 8 (PAT negative in any of last 3 years — false, FY24/25/26 all
positive), 9 (history <3yrs — false, 10 years available).

**CLASSIFICATION: AVOID**

This holds on the base Core-score matrix alone (29 <40) independent of deal
breaker 6. Deal breaker 6 is an additional, separately-flagged trigger that
rests entirely on unverified FY2026 data; even fully discounting FY2026, the
AVOID classification stands on Blocks A, B and C as scored on audited years.

**Strongest block: E (Shareholder Alignment), 13/20** — high, stable
promoter holding (69.84%, unchanged across the only two years evidenced) and
low contingent-liability exposure, though pledge is a genuine data gap, not
a clean pass.

**Weakest block: C (Growth), 1/20** — revenue CAGR sits just under the 5%
floor over the full 10-year window and PAT CAGR is not computable (loss
endpoints); the recent-window picture (post-restructuring) is materially
better on revenue (22.33% 5yr CAGR from the FY21 trough) but PAT growth
remains negative even on the clean FY23→FY26 window (-40.1%), which is
consistent with the FY26 margin-collapse concern, not solely a legacy-loss
artifact.

**Decision line:** AVOID, on quantitative scorecard grounds. Both a genuine,
across-the-cycle sub-10% ROCE ceiling (never exceeded 8.33% even in the best
audited year, FY2024) and an unverified but sharp FY2026 profitability
collapse drive the result. Per CLAUDE.md, this is a mechanical Gate 0 output,
not a halt: it carries forward as a flag, not a stop, and the operator
reviews it at Halt 1 alongside the dossier.

---

## DATA NOTES

- Capital Employed proxy: Equity Share Capital + Reserves + Borrowings, used
  throughout Block A and D3/D1, since Data_Sheet does not split current vs
  non-current liabilities (screener-data).
- Equity/net-worth reconciliation gap: Data_Sheet net worth is 48.85-56.76cr
  lower than AR standalone Total Equity for FY2024/FY2025 (both anchored
  above); does not change any band.
- Loss-to-profit swings: FY17-18 loss, FY19 marginal profit, FY20-22 loss,
  FY23-26 profit (FY26 sharply lower, unverified). No synthetic CAGR
  attempted per CAGR edge rules.
- FY2026 cost-line split (Power & Fuel, Other Mfr. Exp, Selling and admin)
  is blank in Data_Sheet; treated as NOT FOUND. Other Expenses reads 237.10cr
  FY26 vs 11.40cr FY25 — a broken split, not a real cost explosion, per
  orchestrator instruction.
- FY2026 quarterly PBT sum (2.48cr) does not reconcile with FY2026 annual
  PBT (10.43cr), a ~7.95cr unexplained gap in the Data_Sheet Quarters block;
  unresolved in this corpus.
- Trade Payables and capex are absent from Data_Sheet for all 10 years;
  sourced from AR standalone statements, available FY2023-FY2025 only (no
  earlier AR, no FY2026 filing in corpus). B2, B3 and B4 are scored on this
  3-year (or 2-year change) window; a genuine evidence limitation, stated
  throughout rather than smoothed.
- Contingent liabilities (E4) sourced from the Consolidated FS note 45; no
  separate standalone note 45 was located in the extracted text. Subsidiaries
  are described elsewhere in the AR as largely dormant/closed, so this is
  treated as a close proxy, flagged.
- M2, M5, M9 peer comparisons use only the three named peer Data_Sheets
  (Neuland, Kopran, Granules), context-only per orchestrator instruction; a
  fuller segment peer set is PEER DATA NEEDED for M5 and M7 specifically.
- M7 (Regulatory/License): PEER DATA NEEDED — no count of competing listed
  Cephalosporin API/FDF players found in corpus.
- M8 (Distribution): business-model mismatch flagged — the test is framed
  for FMCG-style distribution networks; Orchid is a B2B bulk-API/FDF
  exporter, scored conservatively.

## ANALYST NOTE

AVOID rests on two independent legs. First, the base Core score (29/100) is
weak even ignoring FY2026: ROCE never cleared 8.33% in any audited year
(FY2017-FY2025), so the low score is not solely a pre-2020 CDR-restructuring
artifact, though the restructuring years (FY17-21, huge losses) do pull the
10-year medians down further. Second, deal breaker 6 (ND/EBITDA >3x and IC
<3x) fires only on unverified FY2026 screener figures, alongside a broken
FY2026 cost-line split and an unreconciled quarterly-vs-annual PBT gap. FY2025
audited figures show net cash and 7.4x interest coverage — the opposite
picture. The moat scan finds 2 of 12 tests present (MODERATE): margin
stability with growth (M1) and a network-effects proxy (M11), but the company
sits below the three named peers on both EBITDA margin and gross-margin
proxy. Shareholder alignment (Block E) is the one clean area: 69.84% promoter
holding, unchanged, low contingent liabilities. Pledge could not be evidenced
either way.

```yaml
stage: B01-gate0
company: "ORCHPHARMA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results: no quarterly or annual results filing in corpus"
  - "rating: no credit rating bulletin or rationale in corpus"
  - "announcements: no exchange / Reg 30 filings in corpus"
  - "shareholding: no quarterly shareholding pattern in corpus"
  - "research: no broker notes in corpus (non-anchored; no evidence effect)"
  - "screening: Profit_Loss, Balance_Sheet, Cash_Flow, Quarters CSVs are empty templates (collect_to_repo v3 defect); Data_Sheet used in their place"
  - "presentation: image-based, 3124 chars over 14 pages; treated as near-absent"
  - "FY2026 primary filings absent: no FY2026 annual report and no FY2026 audited annual results filing; FY2026 figures are screener aggregates only"
  - "FY2026 cost breakdown blank in Data_Sheet; FY2026 cost split is NOT FOUND"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID (Core 29/100) with historical depressors identified: full 10yr window includes FY17-21 CDR-restructuring losses that suppress medians, but even audited FY22-25 years never clear 8.33% ROCE, so the low score is not purely a history artifact"}
  - {type: FLAG-DEALBREAKER-6, reason: "AVOID trigger (ND/EBITDA 4.46x, IC 2.16x) rests solely on unverified FY2026 screener-aggregate figures with a broken cost-line split and an unreconciled ~7.95cr quarterly-vs-annual PBT gap; FY2025 audited figures show net cash and 7.40x interest coverage instead"}
  - {type: FLAG-CASH, reason: "block_b_trend deteriorating: FCF swung from +75.58cr (FY24) to -41.06cr (FY25) as capex outran CFO; only 3 years (FY23-25) carry primary capex/payables evidence"}
  - {type: FLAG-DATA-GAP, reason: "Promoter pledge (E3) and true 3-year promoter-holding trend (E2) not found in either AR; scored 0 and 3 respectively as data-availability findings, not evidenced negatives"}
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 5, B: 5, C: 1, D: 5, E: 13}
core_score: 29
moat_score: 11
grand_total: 40
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers: [1, 2, 3, 4, 6]
history_downgrade: true
data_notes:
  - "Capital Employed = Equity Share Capital + Reserves + Borrowings (proxy, Data_Sheet has no current/non-current liability split)"
  - "Data_Sheet net worth is 48.85-56.76cr lower than AR standalone Total Equity for FY24/FY25 (both anchored); no band change"
  - "PAT loss-to-profit-loss-profit swings across FY17-FY26; no synthetic CAGR attempted"
  - "FY2026 cost-line split blank in Data_Sheet (Power&Fuel, Other Mfr Exp, Selling and admin); Other Expenses 237.10cr FY26 vs 11.40cr FY25 is a broken split, not a real cost spike"
  - "FY2026 quarterly PBT sum (2.48cr) vs FY2026 annual PBT (10.43cr): ~7.95cr unreconciled gap, unresolved in corpus"
  - "Trade Payables and capex absent from Data_Sheet for all 10 years; sourced from AR, available FY2023-FY2025 only; B2/B3/B4 scored on this 3yr window"
  - "Contingent liabilities (E4) sourced from Consolidated FS note 45 only; no standalone note 45 located; subsidiaries described as largely dormant"
  - "M2/M5/M9 peer comparisons limited to 3 named peers (Neuland, Kopran, Granules), context-only; PEER DATA NEEDED for a fuller segment set"
  - "M7 PEER DATA NEEDED: no count of competing listed Cephalosporin API/FDF players in corpus"
  - "M8 business-model mismatch flagged: test framed for FMCG distribution, Orchid is a B2B bulk-API/FDF exporter"
block_b_trend: "deteriorating — FCF +75.58cr (FY24) to -41.06cr (FY25); cumulative FCF/PAT FY23-25 = -0.15x"
analyst_note: "AVOID rests on two legs. Core score (29/100) is weak even ignoring FY2026: ROCE never cleared 8.33% in any audited year, so this is not solely a pre-2020 CDR-restructuring artifact, though FY17-21 losses pull the 10yr medians down further. Deal breaker 6 (ND/EBITDA>3x, IC<3x) fires only on unverified FY2026 figures alongside a broken cost-line split and an unreconciled quarterly-vs-annual PBT gap; FY2025 audited figures show net cash and 7.4x coverage instead. Moat scan: 2/12 present (MODERATE) - margin stability with growth (M1), network-effects proxy (M11) - but Orchid sits below all 3 named peers on EBITDA margin and gross-margin proxy. Block E (shareholder alignment) is the clean area: 69.84% promoter holding, unchanged, low contingent liabilities; pledge could not be evidenced either way."
```
