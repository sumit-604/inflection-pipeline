# STAGE 1: GATE 0 SCORECARD — IOL Chemicals & Pharmaceuticals Ltd (IOLCP)
Run date: 2026-09-19 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026, standalone). Scoring adapted
to 10-year history. Primary source: screener-standalone-{Profit_Loss,
Balance_Sheet,Cash_Flow,Data_Sheet}.csv. Consolidated screener CSVs
(FY22-FY26+TTM) cross-checked and are near-identical to standalone (one
subsidiary, total assets Rs 0.12 Cr per run brief); standalone used
throughout as primary per task instructions. Cash flow statement capex
breakdown, trade payables, contingent liabilities and R&D spend pulled
from AR FY26 (comparative FY26/FY25 only) and Q4 FY26 audited results
(same comparative window) — these fields are NOT available for FY17-FY24
in the provided corpus; gaps are marked N/A below, never estimated.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Source for ROCE and ROE-base figures: screener-standalone-Balance_Sheet.csv
(screener's own ROCE column used per formula rule; ROE computed per stage
formula, average net worth, not screener's own closing-equity ROE column).

| Year | ROCE (screener) | Net Worth (Cap+Res) | PAT | ROE (avg NW, computed) |
|---|---|---|---|---|
| FY17 | N/A (screener blank) | 188.70 | 4.67 | 2.48% (closing NW used, opening N/A) |
| FY18 | 15.03% | 215.74 | 27.70 | 13.70% |
| FY19 | 55.53% | 474.34 | 236.70 | 68.60% |
| FY20 | 67.94% | 813.54 | 361.29 | 56.11% |
| FY21 | 54.04% | 1260.43 | 444.56 | 42.87% |
| FY22 | 17.14% | 1390.27 | 165.66 | 12.50% |
| FY23 | 13.64% | 1506.55 | 139.98 | 9.67% |
| FY24 | 12.30% | 1611.33 | 135.42 | 8.69% |
| FY25 | 8.85% | 1687.41 | 101.00 | 6.12% |
| FY26 | 10.65% | 1798.38 | 137.72 | 7.90% |

(screener-standalone-Balance_Sheet.csv rows "Return on Capital Emp" and
"Reserves"/"Equity Share Capital"; PAT from screener-standalone-Profit_Loss.csv)

**A1 Median ROCE** (FY18-FY26, 9 values; FY17 blank in source): sorted
8.85, 10.65, 12.30, 13.64, **15.03**, 17.14, 54.04, 55.53, 67.94 → median
15.03% → band 15-19.9% → **A1 = 3**

**A2 Minimum single-year ROCE**: FY25 = 8.85% (screener-standalone-Balance_Sheet.csv)
→ band 8-11.9% → **A2 = 1**

**A3 Median ROE** (computed, avg net worth, FY17-FY26): sorted 2.48, 6.12,
7.90, 8.69, 9.67, 12.50, 13.70, 42.87, 56.11, 68.60 → median = avg(9.67,
12.50) = 11.08% → band <12% → **A3 = 0**

**A4 ROCE trend, latest vs earliest available** (FY18 15.03% → FY26
10.65%, FY17 blank in source so FY18 is earliest usable): decline of
4.38pp → band decline 3-5pp → **A4 = 1**

**BLOCK A TOTAL = 3+1+0+1 = 5 / 20**
Deal-breaker 1 triggered: Block A < 8 → caps classification at max GOOD.
Driver years: the FY19-FY21 window (ROCE 55-68%, an Ibuprofen API pricing
supercycle, per FY26 AR narrative on non-Ibuprofen diversification, AR
p.24) is not the base problem; the deal-breaker is driven by the FY22-FY26
normalization (ROCE 17.1% → 8.85% → 10.65%) sitting below the 15%+ minimum
threshold in 4 of the last 5 years.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

**B1 Cumulative CFO ÷ Cumulative PAT** (FY17-FY26, full 10-year window):
Cumulative CFO = 83.34+119.72+273.17+470.80+379.78+91.04+123.14+290.46+
178.68+214.42 = **2224.55** (screener-standalone-Cash_Flow.csv)
Cumulative PAT = 4.67+27.70+236.70+361.29+444.56+165.66+139.98+135.42+
101.00+137.72 = **1754.70** (screener-standalone-Profit_Loss.csv)
Ratio = 2224.55 / 1754.70 = 1.268 → ≥1.00 → **B1 = 5**

**Capex basis note (applies to B2, B3):** the stage formula requires
"purchase of PPE + intangibles from cash flow statement." The provided
screener-standalone-Cash_Flow.csv gives only CFO/CFI/CFF totals, no capex
line. Capex breakdown by the CFS definition is available only for FY26
(Rs 172.99 Cr) and FY25 (Rs 213.55 Cr), both anchored to the Standalone
Cash Flow Statement, "Purchase of property, plant and equipment including
intangible assets and Capital work in progress" (Annual_Report_2026.txt
p.136-137; cross-checked against 20260520-Q4FY26-audited-results.txt p.9,
identical figures). For FY22-FY24, no CFS capex breakdown is in the
provided corpus (only FY26/FY25 comparatives were extracted); the only
capex figure available for those years is the AR's own ESG/capex-utilisation
chart, "Capex (Rs in Cr)": FY22 = 153, FY23 = 224, FY24 = 257
(Annual_Report_2026.txt p.24). This is company-disclosed but is not
confirmed to be on the identical cash-paid CFS basis (it may include
accrual/committed capex or exclude proceeds from asset sales); flagged as
a basis approximation, not an estimate. FY17-FY21 capex is N/A (not in
provided data) — FCF is not computed for those 5 years.

| Year | CFO | Capex | Capex source/basis | FCF |
|---|---|---|---|---|
| FY22 | 91.04 | 153.00 | AR capex chart (p.24), non-CFS-confirmed basis | -61.96 |
| FY23 | 123.14 | 224.00 | AR capex chart (p.24), non-CFS-confirmed basis | -100.86 |
| FY24 | 290.46 | 257.00 | AR capex chart (p.24), non-CFS-confirmed basis | +33.46 |
| FY25 | 178.68 | 213.55 | Standalone CFS (AR p.136-137) | -34.87 |
| FY26 | 214.42 | 172.99 | Standalone CFS (AR p.136-137) | +41.43 |

**B2 FCF-positive years as proportion** (5 years available, FY22-FY26):
2 of 5 positive (FY24, FY26) = 40% → band <50% → **B2 = 0**

**B3 Cumulative FCF ÷ Cumulative PAT** (same 5-year window):
Cumulative FCF = -61.96-100.86+33.46-34.87+41.43 = **-122.80**
Cumulative PAT (FY22-FY26) = 165.66+139.98+135.42+101.00+137.72 = **679.78**
Ratio = -122.80 / 679.78 = -0.181 → negative → **B3 = 0**

**B4 Change in WC Days, latest vs earliest available**: Working Capital
Days = Receivable Days + Inventory Days − Payable Days, all on Revenue
basis (no standalone COGS line isolated in provided data; Receivable Days
basis matches screener's own published Debtor Days column exactly, e.g.
FY26 603.13/2319.06×365 = 94.93, confirming Revenue basis is screener's
convention — used consistently here). Trade Payables (needed for Payable
Days) is available in the provided corpus only for FY26 (Rs 482.56 Cr =
7.29+475.27) and FY25 (Rs 427.56 Cr = 6.74+420.82)
(20260520-Q4FY26-audited-results.txt p.8). No payables breakdown for
FY17-FY24 is in the provided data, so full WC Days is computable only for
FY25 and FY26.

| | Receivable Days | Inventory Days | Payable Days | WC Days |
|---|---|---|---|---|
| FY25 | 90.18 (screener-standalone-Balance_Sheet.csv) | 63.30 (360.62/2079.21×365) | 75.06 (427.56/2079.21×365) | 78.42 |
| FY26 | 94.93 (screener-standalone-Balance_Sheet.csv) | 58.40 (371.07/2319.06×365) | 75.95 (482.56/2319.06×365) | 77.38 |

Change (FY26 vs FY25) = 77.38 − 78.42 = -1.04 days (decreased) → within
±5 days → **B4 = 3**

**BLOCK B TOTAL = 5+0+0+3 = 8 / 20** (exactly at, not below, the deal-
breaker-2 threshold of <8; deal-breaker 2 NOT triggered)

Supplementary observation (not separately scored, flagged for downstream):
Receivable Days on the full 10-year window (screener-standalone-Balance_Sheet.csv)
rose from 78.51 (FY22) to 94.93 (FY26), +16.4 days over 4 years, while
revenue over the same window was roughly flat (2184.02 → 2319.06). Annual
CFO/PAT cash-conversion ratio fell from 2.15x (FY24: 290.46/135.42) to
1.56x (FY26: 214.42/137.72). This matches LBF3 in company memory
(debtor days 79 to 95) and is the single number behind the trend call
below.

---

## BLOCK C: GROWTH (Max 20)

Source: screener-standalone-Profit_Loss.csv, Sales and Net profit rows,
FY17-FY26 (9-year CAGR window).

**C1 Revenue CAGR**: (2319.06 / 710.65)^(1/9) − 1 = 14.04% → band
10-14.9% → **C1 = 3**

**C2 PAT CAGR**: (137.72 / 4.67)^(1/9) − 1 = 45.65% → band ≥20% →
**C2 = 5**
Base-effect flag: FY17 PAT of Rs 4.67 Cr is a near-breakeven year (PBT
Rs 5.93 Cr, screener-standalone-Profit_Loss.csv) on Interest expense of
Rs 67.68 Cr against an operating profit of Rs 102.40 Cr — a depressed,
debt-heavy base, not a loss year (so the CAGR edge rule for loss-to-profit
swings does not apply), but the resulting 45.65% PAT CAGR is a base-year
artifact, not organic acceleration; it is mechanically much higher than
the 10-year revenue CAGR because the denominator is thin.

**C3 Positive YoY revenue years**: FY18-FY26 = 9 year-over-year
comparisons. Declines: FY24 (2132.79 < FY23 2217.11), FY25 (2079.21 <
FY24 2132.79). 7 of 9 positive = 77.8% → band 75-99% → **C3 = 3**

**C4 PAT CAGR minus Revenue CAGR**: 45.65% − 14.04% = +31.61pp → band
≥+3pp → **C4 = 5** (same FY17 base-effect caveat as C2 applies directly
to this score)

**BLOCK C TOTAL = 3+5+3+5 = 16 / 20**
Deal-breaker 7 (revenue declined in majority of years) NOT triggered:
2 of 9 years declined, not a majority.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Source: screener-standalone-Balance_Sheet.csv (FY26) and
20260520-Q4FY26-audited-results.txt p.8 (Standalone Balance Sheet,
31-Mar-2026 audited column) for current asset/liability split not itemised
in the screener CSV.

**D1 Net Debt ÷ EBITDA (latest, FY26)**: Borrowings 135.42 − Cash & Bank
198.25 (screener-standalone-Data_Sheet.csv; = Cash and cash equivalents
65.29 + Bank balances other than above 132.96, results p.8) = **-62.83**
(net cash position) → **D1 = 5**

**D2 Interest Coverage EBIT ÷ Interest (latest, FY26)**: EBIT = Operating
Profit − Depreciation = 269.86 − 80.17 = 189.69 (screener-standalone-Profit_Loss.csv);
Interest = 14.55 → 189.69 / 14.55 = 13.04x → ≥10x → **D2 = 5**

**D3 Debt ÷ Equity (latest, FY26)**: Borrowings 135.42 / Total Equity
1798.38 (58.71 + 1739.67, screener-standalone-Balance_Sheet.csv) = 0.075
→ <0.1 → **D3 = 5**

**D4 Current Ratio (latest, FY26)**: Total current assets 1227.51 / Total
current liabilities 690.12 (20260520-Q4FY26-audited-results.txt p.8) =
1.779 → band 1.5-1.99 → **D4 = 4**

**BLOCK D TOTAL = 5+5+5+4 = 19 / 20**
Deal-breaker 6 (ND/EBITDA >3x AND IC <3x → AVOID) NOT triggered: company
sits in net cash with 13x coverage.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Source: inputs/shareholding/SHP-June-2026.txt and SHP-September-2024.txt
(earliest shareholding filing in the provided corpus); contingent
liabilities from Annual_Report_2026.txt p.161.

**E1 Promoter holding (latest quarter, Jun-2026)**: 62.28%
(SHP-June-2026.txt, Table I, category A) → ≥60% → **E1 = 5**

**E2 Promoter holding change**: 48.19% (Sep-2024, SHP-September-2024.txt)
→ 62.28% (Jun-2026) = +14.09pp increase. Note: the provided shareholding
corpus starts at Sep-2024, ~21 months before the latest filing, not the
full 3-year window the rule specifies (no SHP filing older than Sep-2024
was provided); scored on the available window. Share capital held flat
in Rs terms across the period (Equity Share Capital = 58.71 Cr both FY25
and FY26, screener-standalone-Balance_Sheet.csv; share count moved from
58.7 Cr shares at face value Rs 10 to 293.5 Cr shares at face value Rs 2,
a 5:1 split, not a capital raise), so the promoter % rise reflects
market purchases, not share-count dilution mechanics. +14.09pp ≥ +1% →
**E2 = 5**

**E3 Promoter pledge (latest)**: SHP-June-2026.txt Declaration item 7,
"Whether any shares held by promoters are encumbered under 'Pledge'?" =
No → 0% → **E3 = 5**

**E4 Contingent liabilities ÷ Net Worth (latest, FY26)**: Contingent
liabilities (Claims not acknowledged as debts 0.26 + Bank Guarantees
issued in favour of others 3.34 + Others 2.06) = Rs 5.66 Cr
(Annual_Report_2026.txt p.161, Note 35A); Net Worth = 1798.38 → 5.66 /
1798.38 = 0.31% → <5% → **E4 = 5**

**BLOCK E TOTAL = 5+5+5+5 = 20 / 20**
Deal-breaker 5 (pledge >15% → max AVERAGE) NOT triggered.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

No peer dataset was provided in this run's inputs. Every test requiring a
peer median, peer count, or peer mcap ranking (M2, M5, M6's top tier, M7,
M9) is scored 0 and marked PEER DATA NEEDED per the stage rule — this
reflects missing evidence, not a finding of no moat on those dimensions.

**M1 Pricing Power**: OPM (screener-standalone-Profit_Loss.csv) FY17
14.41% → FY26 11.64%, decline of 2.77pp; revenue CAGR 14.04% (≥10%) →
"margin declined 2-5pp despite growth" → **M1 = 1**

**M2 Cost Advantage vs peer median EBITDA margin**: no peer data provided
→ **M2 = 0, PEER DATA NEEDED**

**M3 Capital Efficiency**: FY26 Fixed Asset Turnover = Sales 2319.06 /
Net Block 1181.26 = 1.96x; FY26 ROCE = 10.65% (screener). FAT >1x but
ROCE not >12% → fails the FAT>1x/ROCE>12% tier and all higher tiers →
**M3 = 0**

**M4 Customer Stickiness**: 2 revenue-decline years (FY24, FY25) with
overall positive 10-year revenue CAGR (14.04%) → "2 decline years, CAGR
positive" → **M4 = 1**

**M5 Scale & Dominance**: no peer mcap/margin ranking data provided →
**M5 = 0, PEER DATA NEEDED**

**M6 Technology / R&D**: R&D revenue expense Rs 24.32 Cr + capital
expense Rs 1.69 Cr = Rs 26.01 Cr on FY26 Sales 2319.06 = 1.12% of revenue
(Annual_Report_2026.txt p.161, Note 33/34); FY26 EBITDA margin 11.64%
(well below the 15% and 20% tiers), so only the "≥1% AND margin above
peer median" tier is reachable, and that requires a peer median which is
not provided → **M6 = 0, PEER DATA NEEDED**

**M7 Regulatory / License**: no count of listed peers in the regulated
API/CDMO segment provided → **M7 = 0, PEER DATA NEEDED**

**M8 Distribution**: IOLCP is a B2B bulk-drug/API manufacturer selling to
formulators; no distribution-network/reach metric is disclosed in the
provided corpus → **M8 = 0**

**M9 Brand**: gross-margin-vs-peer-median comparison needs peer data, not
provided → **M9 = 0, PEER DATA NEEDED**

**M10 Switching Costs**: overall revenue growth (CAGR 14.04%) with 2
decline years (FY24, FY25) → "overall growth, 2+ decline years" →
**M10 = 1**

**M11 Network Effects** (10-year history qualifies for the two-window
test): latest 3yr CAGR (FY23→FY26) = (2319.06/2217.11)^(1/3)-1 = 1.51%;
prior 3yr CAGR (FY20→FY23) = (2217.11/1894.47)^(1/3)-1 = 5.38%. Latest <
prior, and overall CAGR (14.04%) is below the 20%/15% alternate-tier
thresholds → **M11 = 0**

**M12 Negative WC / Float**: full WC Days available only for FY25 (78.42)
and FY26 (77.38), both >45 days → **M12 = 0**

**BLOCK F TOTAL = 1+0+0+1+0+0+0+0+0+1+0+0 = 3 / 60**

Moat profile:
```
M1  [#----] 1/5  Pricing Power
M2  [------] 0/5  Cost Advantage        PEER DATA NEEDED
M3  [------] 0/5  Capital Efficiency
M4  [#----] 1/5  Customer Stickiness
M5  [------] 0/5  Scale & Dominance     PEER DATA NEEDED
M6  [------] 0/5  Technology / R&D      PEER DATA NEEDED
M7  [------] 0/5  Regulatory / License  PEER DATA NEEDED
M8  [------] 0/5  Distribution
M9  [------] 0/5  Brand                 PEER DATA NEEDED
M10 [#----] 1/5  Switching Costs
M11 [------] 0/5  Network Effects
M12 [------] 0/5  Negative WC / Float
```
Moats present (score ≥3): 0 → **Moat classification = NONE**

---

## DATA CONFIDENCE

10 years of standalone history (FY17-FY26) → **10+ yrs, FULL confidence**.
No history-based downgrade. `history_downgrade: false`

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation Quality | 8 | 20 |
| C — Growth | 16 | 20 |
| D — Balance Sheet Strength | 19 | 20 |
| E — Shareholder Alignment | 20 | 20 |
| **Core total** | **68** | **100** |
| F — Moat (informational) | 3 | 60 |
| **Grand total** | **71** | **160** |

Matrix: Core 60-79 + moat class NONE → base classification **GOOD**.
Deal-breaker 1 (Block A < 8) independently also caps at max GOOD — same
result, no further downgrade.

Deal-breakers evaluated:
1. Block A (5) < 8 → **TRIGGERED**, caps at GOOD. Driver years: FY22-FY26
   ROCE normalization (17.1% → 8.85% → 10.65%) below 15% threshold in 4 of
   5 years, following the FY19-FY21 Ibuprofen-pricing-supercycle peak
   (54-68% ROCE) that is not repeated in the recent window.
2. Block B (8) < 8 → not triggered (exactly at threshold).
3. Median ROCE (15.03%) < 10% → not triggered.
4. Cumulative CFO/PAT (1.27x) < 0.50 → not triggered.
5. Pledge (0%) > 15% → not triggered.
6. ND/EBITDA >3x AND IC <3x → not triggered (net cash, 13x coverage).
7. Revenue declined in majority of years → not triggered (2 of 9).
8. PAT negative in any of last 3 years → not triggered (FY24/25/26 all
   positive).
9. History < 3 years → not triggered (10 years).

**CLASSIFICATION = GOOD**

---

## STRONGEST / WEAKEST BLOCK

Strongest: **Block E, Shareholder Alignment (20/20)** — promoter holding
62.28%, rising, unpledged, contingent liabilities negligible relative to
net worth.

Weakest: **Block A, Return on Capital (5/20)** — post-supercycle ROCE
sits below the 15% band in 4 of the last 5 years, and is the sole
deal-breaker triggered in this scorecard.

---

## DECISION LINE

Gate 0 mechanical scorecard: **GOOD** (Core 68/100, Moat class NONE,
grand total 71/160). This is a mechanical screen only; it does not
constitute a valuation or investment recommendation and carries no
qualitative read on the FY19-FY21 vs FY22-FY26 mix shift, the debtor-days
trend, or the capex-financing question already logged as load-bearing
facts (LBF1-LBF4) in company memory. Those are carried forward for later
stages.

---

## ANALYST NOTE (flagged for downstream, not separately scored)

Three items a downstream stage cannot reconstruct from the fields above.
One, the PAT CAGR (45.65%) and C4 gap (+31.6pp) are a base-year artifact:
FY17 PAT (Rs 4.67 Cr) was suppressed by Rs 67.68 Cr of interest expense on
a leveraged balance sheet since since deleveraged; revenue CAGR (14.04%)
is the more representative growth read. Two, Block A's deal-breaker is a
normalization story, not a straight decline: ROCE ran 54-68% in FY19-FY21
(Ibuprofen API pricing supercycle per the FY26 AR's own diversification
narrative, AR p.24-25) then reset to a 8.85-17.14% band FY22-FY26; A1-A4
all score off the post-reset band, which is the right read for a forward
screen but means the raw "decline" framing understates how episodic the
high-ROCE years were. Three, cash-quality signals are directionally mixed
inside a net-CFO-positive picture: cumulative CFO/PAT is a strong 1.27x
over 10 years (B1=5), but FCF turned negative in 3 of the last 5 years on
rising capex, and receivable days climbed from 78.5 (FY22) to 94.9 (FY26)
even as revenue was flat — the single number behind block_b_trend below.
Five of twelve moat tests (M2, M5, M6, M7, M9) scored 0 purely for
missing peer data, not weak evidence; moat_score (3/60) should not be
read as a finding of no moat until peer data resolves those tests.

---

```yaml
stage: B01-gate0
company: "IOLCP"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
input_gaps:
  - "CFS purchase-of-PPE capex breakdown not in provided data for FY17-FY24; FY22-FY24 FCF uses AR capex-utilisation chart (p.24) as a non-CFS-confirmed proxy, FY17-FY21 FCF not computed"
  - "Trade payables breakdown (for Payable Days / WC Days) available only for FY25 and FY26 in provided corpus; FY17-FY24 WC Days not computed"
  - "Shareholding data provided only from Sep-2024 onward; E2 promoter-change scored on ~21-month window (Sep-2024 to Jun-2026), not the full 3-year window the rule specifies"
  - "No peer dataset provided; M2, M5, M6 (top tier), M7, M9 scored 0, PEER DATA NEEDED"
flags: []
data_years: 10
fy_range: "FY17 to FY26"
blocks: {A: 5, B: 8, C: 16, D: 19, E: 20}
core_score: 68
moat_score: 3
grand_total: 71
moats_confirmed: 0
moat_class: "NONE"
classification: "GOOD"
deal_breakers:
  - "Block A total (5) < 8 -> caps classification at max GOOD; driven by FY22-FY26 ROCE normalization (17.1% -> 8.85% -> 10.65%) below 15% in 4 of last 5 years, following the FY19-FY21 pricing-supercycle peak"
history_downgrade: false
data_notes:
  - "PAT CAGR (45.65%) and C4 (+31.6pp) driven by a depressed FY17 base (PAT Rs 4.67 Cr, near-breakeven on Rs 67.68 Cr interest expense), not a loss year so the loss-to-profit swing rule does not apply, but flagged as a base-effect distortion; revenue CAGR (14.04%) is the more representative growth read"
  - "Inventory Days and Payable Days computed on Revenue basis (no standalone COGS line isolated in provided data), consistent with screener's own Receivable Days convention"
  - "FY22-FY24 capex (153/224/257) sourced from AR FY26 capex-utilisation chart (p.24), a different presentation than the Standalone Cash Flow Statement 'purchase of PP&E' line used for FY25/FY26 (213.55/172.99); basis switch noted, not an estimate"
  - "5 of 12 moat tests (M2, M5, M6, M7, M9) scored 0 solely for missing peer data (PEER DATA NEEDED), not weak evidence; moat_score should not be read as a finding of no moat until peer data resolves those tests"
block_b_trend: "deteriorating"
analyst_note: "PAT CAGR (45.65%) is a base-effect artifact off a depressed FY17 (Rs 4.67 Cr PAT on Rs 67.68 Cr interest expense); revenue CAGR 14.04% is more representative. Block A's deal-breaker is a normalization off an episodic FY19-FY21 Ibuprofen pricing supercycle (ROCE 54-68%), not a straight decline; FY22-FY26 sits in an 8.85-17.14% band. Cash quality is mixed inside a strong headline: cumulative CFO/PAT is 1.27x over 10 years (B1=5), but FCF was negative in 3 of the last 5 years and receivable days rose from 78.5 (FY22) to 94.9 (FY26) on flat revenue (matches company-memory LBF3). Five of twelve moat tests scored 0 purely for missing peer data; treat moat_score (3/60) as unresolved, not a finding of no moat."
```
