# GATE 0 SCORECARD — Diffusion Engineers Ltd (DIFFNKG)
Run date: 2026-09-05 | Stage: B01-gate0

Data available: 8 years (FY2019 to FY2026). Scoring adapted to 8-year history.
Source: Screener Data_Sheet (screener-Data_Sheet.csv) is the sole reliable
consolidated time series; the peer Balance Sheet / Cash Flow / Quarters /
Customization screener CSVs are blank dashboard templates with no populated
rows and contribute nothing. AR2025/AR2026 text used only where a figure
(contingent liabilities, R&D description, distributor count) is not carried
in the Data Sheet. Where AR standalone cash-flow-statement and financial-
instrument-note figures conflict with the Data Sheet by a non-round factor
(~9-10x, not the clean 100x a Lakh->Crore conversion would give), those AR
lines are treated as unit-ambiguous and NOT used (see data_notes).

Post-IPO rebase (per injected input and AR2026 narrative): Reserves jumped
84.02cr FY24 -> 331.45cr FY25 (screener-data) on IPO primary proceeds
(Financing activity +128.72cr FY25, screener-data). This enlarges the FY25
capital-employed and net-worth denominators, mechanically depressing FY25
ROCE/ROE versus FY24 and FY26. Treated as a historical depressor, not
operating deterioration; history_downgrade = true, flagged below.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE computed (screener does not supply its own ROCE row in this file;
EBIT = PBT + Interest; Capital Employed = Equity Capital + Reserves +
Borrowings, i.e. Total minus Other Liabilities, per screener convention),
all figures (screener-data, Data_Sheet rows: Sales/PBT/Interest/Equity
Share Capital/Reserves/Borrowings):

| FY | EBIT (cr) | Cap. Employed (cr) | ROCE % |
|---|---|---|---|
| FY19 | 15.21 | 102.84 | 14.79 |
| FY20 | 16.33 | 127.38 | 12.82 |
| FY21 | 18.80 | 124.82 | 15.06 |
| FY22 | 23.35 | 145.25 | 16.08 |
| FY23 | 30.96 | 190.09 | 16.29 |
| FY24 | 42.84 | 225.14 | 19.02 |
| FY25 | 49.17 | 392.09 | 12.54 |
| FY26 | 67.18 | 433.68 | 15.49 |

A1 Median ROCE = 15.28% (median of the 8 values above, computed) → band
15-19.9% = **3**
A2 Minimum single-year ROCE = 12.54% (FY25, computed; post-IPO base
effect per above) → band 12-14.9% = **3**
A3 Median ROE = 12.92% (computed; PAT ÷ avg Net Worth, avg = opening+
closing/2 except FY19 which uses closing only, no FY18 opening) → band
12-14.9% = **2**

| FY | Avg Net Worth (cr) | PAT (cr) | ROE % |
|---|---|---|---|
| FY19 | 87.53 (closing only, no FY18) | 9.49 | 10.84 |
| FY20 | 91.35 | 11.14 | 12.20 |
| FY21 | 100.15 | 11.72 | 11.70 |
| FY22 | 112.89 | 17.02 | 15.08 |
| FY23 | 131.33 | 22.16 | 16.87 |
| FY24 | 166.35 | 30.66 | 18.43 |
| FY25 | 279.79 | 35.91 | 12.84 |
| FY26 | 386.97 | 50.32 | 13.00 |

A4 ROCE trend, latest (FY26=15.49%) vs earliest (FY19=14.79%): latest ≥
earliest → **5**

**Block A = 3+3+2+5 = 13/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY19-FY26) = 109.56cr (screener-data, Cash from Operating
Activity row, sum of 8 years). Cumulative PAT (same window) = 188.42cr
(screener-data, Net profit row).

B1 CFO ÷ PAT cumulative = 109.56 ÷ 188.42 = 0.5815 → band 0.50-0.69 = **1**

Capex: the screener Data Sheet cash-flow section carries only CFO/CFI/CFF/
Net (no capex line). AR2026 standalone cash-flow-statement "Purchase/Sale
of property, plant and equipment" line is unit-inconsistent against the
Data Sheet balance sheet (see data_notes) and is NOT used. Capex is
instead computed as a proxy: ΔNet Block + ΔCWIP + Depreciation (all
screener-data, Balance Sheet rows), stated as proxy basis per instruction
6/data_notes.

| FY | ΔNet Block | ΔCWIP | Depreciation | Capex proxy (cr) | CFO (cr) | FCF (cr) |
|---|---|---|---|---|---|---|
| FY20 | 19.68 | -0.28 | 3.19 | 22.59 | 10.18 | -12.41 |
| FY21 | -4.63 | 0.00 | 3.90 | -0.73 | 11.88 | 12.61 |
| FY22 | 3.37 | 0.00 | 4.17 | 7.54 | 11.05 | 3.51 |
| FY23 | 3.25 | 1.83 | 3.84 | 8.92 | -4.74 | -13.66 |
| FY24 | 27.47 | -0.72 | 4.55 | 31.30 | 36.38 | 5.08 |
| FY25 | 6.88 | 2.03 | 5.28 | 14.19 | 8.62 | -5.57 |
| FY26 | 12.46 | 19.84 | 6.85 | 39.15 | 22.79 | -16.36 |

(FY19 capex not computable, no FY18 opening Net Block/CWIP.)

B2 FCF-positive years / total (FY20-FY26, 7 years) = 2/7 = 28.6% → band
<50% = **0**
B3 Cumulative FCF (-26.80cr) ÷ Cumulative PAT (178.93cr, FY20-FY26 window
matching FCF window) = -0.150 → band <0.20 or negative = **0**
B4 WC Days change: NOT computable. Screener Data Sheet does not isolate
Trade Payables (only combined "Other Liabilities"); the WC Days formula
(Receivable + Inventory − Payable) cannot be completed. Marked N/A (not
in provided data) → **0**. Partial context only (not scored): Receivable
Days + Inventory Days (sales basis) rose from 161.5 days (FY19: 79.6+81.9)
to 181.2 days (FY26: 115.1+66.1), a +19.7 day increase, driven mostly by
FY26 receivables (128.18cr, screener-data) growing faster than sales.

**Block B = 1+0+0+0 = 1/20**

Block B trend: **deteriorating**. FY26 FCF proxy = -16.36cr despite record
PAT of 50.32cr (screener-data), driven by a capex proxy of 39.15cr
(CWIP alone rose 19.84cr) and receivables consuming cash faster than
revenue grew. This is IPO-proceeds-funded capacity build, not distress,
but it is the one number that shows the cash-conversion strain.

---

## BLOCK C: GROWTH (Max 20)

C1 Revenue CAGR FY19 (153.92cr) → FY26 (406.63cr), 7 years (screener-data)
= (406.63/153.92)^(1/7)-1 = 14.89% → band 10-14.9% = **3**
C2 PAT CAGR FY19 (9.49cr) → FY26 (50.32cr), 7 years (screener-data) =
(50.32/9.49)^(1/7)-1 = 26.9% → band ≥20% = **5**
C3 Positive YoY revenue years: 7/7 transitions FY19-FY26 all positive
(screener-data, Sales row) = 100% → **5**
C4 PAT CAGR (26.9%) − Revenue CAGR (14.89%) = +12.0pp → band ≥+3pp = **5**

**Block C = 3+5+5+5 = 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

D1 Net Debt ÷ EBITDA: Borrowings FY26 = 28.62cr, Cash & Bank FY26 =
97.56cr (both screener-data) → Net Debt = -68.94cr (net cash) → **5**
D2 Interest Coverage: EBIT (excl. other income) = PBT+Interest-OtherIncome
= 65.03+2.15-16.81 = 50.37cr (screener-data); Interest = 2.15cr →
23.4x → band ≥10x = **5**
D3 Debt ÷ Equity: Borrowings 28.62cr ÷ (Equity Capital 37.43cr + Reserves
367.63cr = 405.06cr) = 0.071 → band <0.1 = **5**
D4 Current Ratio: computed as proxy Other Assets (334.12cr) ÷ Other
Liabilities (76.75cr) = 4.35 (screener-data; screener's "Other Assets"/
"Other Liabilities" convention approximates current assets/current
liabilities since Net Block, CWIP, Investments and Borrowings are broken
out separately — no literal current/non-current schedule was in the
provided data, so this is a proxy, stated as such) → band ≥2.0 = **5**

**Block D = 5+5+5+5 = 20/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

E1 Promoter holding: N/A (not in provided data — shareholding pattern
ABSENT per input gaps) → **0**
E2 Promoter holding change: N/A (same gap) → **0**
E3 Promoter pledge: N/A (same gap) → **0**
E4 Contingent Liabilities ÷ Net Worth: Contingent liabilities FY26 = 7.21
(AR2026 p.168, Note 37, GST demand under appeal) ÷ Net Worth 405.06cr =
well under 5% under either plausible unit reading of the AR figure →
band <5% = **5**

**Block E = 0+0+0+5 = 5/20**

**Core Score (A+B+C+D+E) = 13+1+18+20+5 = 57/100**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

M1 Pricing Power: EBITDA margin (PBT+Dep+Interest-OtherIncome ÷ Sales,
computed) FY19 = 10.81%, FY26 = 14.07%, +3.26pp expansion AND revenue
CAGR 14.89% ≥10% → **5**
M2 Cost Advantage vs peer median: PEER DATA NEEDED (GEE Ltd, Esab India,
Ador Welding margins not in provided corpus) → **0**
M3 Capital Efficiency: FAT (FY26) = Sales 406.63 ÷ Net Block 110.34 =
3.69x >3x, but ROCE FY26 = 15.49% is not >20% → falls to FAT>2x AND
ROCE>15% tier → **3**
M4 Customer Stickiness: 0 revenue-decline years (screener-data) but
receivable days rose 35.5 days FY19->FY26 (not stable ±10) → fails top
tier; 0 decline years satisfies "max 1 decline year" tier → **3**
M5 Scale & Dominance: PEER DATA NEEDED (mcap/margin rank vs GEE/Esab/
Ador not in provided corpus) → **0**
M6 Technology/R&D: AR2026 p.99-100 describes an R&D team, a doctoral
candidate, DSIR recognition (valid to 31-Mar-2027), and NABL lab
accreditation, but R&D spend is NOT quantified as %-of-revenue anywhere
in the provided corpus → **0**, noted "qualitative only, not estimated"
M7 Regulatory/License: welding consumables, wear-plate and
reconditioning services are unregulated/unlicensed businesses → **0**
M8 Distribution: AR2026 p.~ (Corporate Overview pages) states 95+
domestic distributors, 9 international partners, 50+ new dealer MoUs
signed in FY26 — reach IS quantified, but revenue-per-outlet
stable/growing is not tracked in provided data, and revenue CAGR
(14.89%) sits just under the ≥15% needed for the middle tier → **1**
M9 Brand: gross-margin proxy (Revenue − Raw Material Cost) ÷ Revenue =
42.1% FY19 vs 42.5% FY26 (screener-data, proxy stated), but no peer
median available → PEER DATA NEEDED → **0**
M10 Switching Costs: revenue grew every year, but receivable days rose
35.5 days (>10 day tolerance) → fails top two tiers; does not have 2+
decline years for the third tier either → **0**
M11 Network Effects (8yr history, ≥6yr test valid): latest 3yr revenue
CAGR (FY23->FY26) = 16.86% vs prior 3yr (FY20->FY23) = 18.28% — latest is
LOWER than prior, fails top tier; latest 3yr CAGR ≥20%? No (16.86%);
falls to "growth >15% but selling % rising" tier — Selling & admin ÷
Sales rose from 5.31% (FY23) to 6.49% (FY26), confirming rising →
**1**
M12 Negative WC/Float: WC days (receivable+inventory only, payables
unavailable — partial basis, caveat noted) run 150-181 days across the
period, consistently >45 days and never negative → **0**

**Moats present (score ≥3): M1, M3, M4 = 3 present → Moat Classification
= MODERATE (2-3 present)**

**Moat Score = 5+0+3+3+0+0+0+1+0+0+1+0 = 13/60**

---

## CLASSIFICATION

Data confidence: 8 years = moderate (7-9yr band). No automatic tier
downgrade triggered by history length.

Deal-breaker check:
1. Block A (13) <8? No.
2. Block B (1) <8? **YES → caps classification at max GOOD.**
3. Median ROCE (15.28%) <10%? No.
4. Cumulative CFO/PAT (0.5815) <0.50? No (close, but above).
5. Pledge >15%? No data to trigger (E1-E3 N/A, not evidenced).
6. ND/EBITDA >3x AND IC <3x? No (net cash, IC 23.4x).
7. Revenue declined majority of years? No (0 of 7).
8. PAT negative in any of last 3 years (FY24/25/26: 30.66/35.91/50.32)?
   No.
9. History <3 years? No (8 years).

Classification matrix: Core score 57 falls in the 40-59 band → **AVERAGE**
regardless of moat class. The Block-B deal-breaker cap ("max GOOD") does
not bite further since AVERAGE already sits below GOOD.

**GRAND TOTAL = Core 57 + Moat 13 = 70/160**

### Strongest block: D (Balance Sheet Strength), 20/20 — net cash, high
interest cover, negligible leverage, strong proxy current ratio.
### Weakest block: B (Cash Generation Quality), 1/20 — cumulative cash
conversion barely above 50%, FCF proxy negative in 5 of 7 computable
years, receivables growing faster than revenue, payables data gap
prevents a complete WC Days read.

### Decision line
DIFFNKG scores AVERAGE (57 core / 70 grand total) on a 8-year screener
history. Growth (18/20) and balance sheet strength (20/20) are the
strongest legs; cash generation (1/20) and shareholder alignment (5/20,
mostly a data gap on promoter holding) are the weakest. Moat profile is
MODERATE (3 of 12 tests present: pricing power, capital efficiency,
customer stickiness), with 4 of 12 tests unscored for "PEER DATA NEEDED"
(GEE Ltd, Esab India, Ador Welding not in this run's corpus). The FY25
ROCE/ROE dip is an IPO equity-base effect per AR2026, not operating
deterioration, and the FY26 negative FCF proxy is IPO-funded capacity
capex (CWIP +19.84cr), not distress — both are flagged as historical
depressors for downstream weighing, not scored away.

---

```yaml
stage: B01-gate0
company: "DIFFNKG"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps: [prospectus ABSENT, results ABSENT, rating ABSENT, announcements ABSENT, shareholding ABSENT, research ABSENT]
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE (core 57/100). Two depressors identified as historical/mechanical rather than operating: FY25 ROCE 12.54% and ROE dip reflect IPO equity-base enlargement (Reserves 162.68cr->331.45cr FY24->FY25), and FY26 negative FCF proxy (-16.36cr) reflects IPO-funded capacity capex (CWIP +19.84cr), not distress. Block B deal-breaker (cumulative CFO/PAT 0.58, FCF proxy negative in 5/7 years) caps classification at max GOOD but core score already sits in AVERAGE band. Trade Payables not isolated in provided data, so WC Days (B4) and true Current Ratio (D4, proxy used) are incomplete; promoter shareholding entirely absent."
data_years: 8
fy_range: "FY2019 to FY2026"
blocks: {A: 13, B: 1, C: 18, D: 20, E: 5}
core_score: 57
moat_score: 13
grand_total: 70
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers: ["Block B <8 (score 1) -> caps at max GOOD (non-binding, core score already below GOOD in AVERAGE band)"]
history_downgrade: true
data_notes:
  - "Capex computed as proxy (delta Net Block + delta CWIP + Depreciation, screener-data) since AR2026 standalone cash-flow-statement PPE purchase line is unit-inconsistent against the screener Balance Sheet by a non-round factor (~9-10x, not a clean 100x Lakh->Crore conversion) and was excluded as unreliable."
  - "Trade Payables not isolated in screener Data Sheet (combined into Other Liabilities); B4 (WC Days) marked N/A, scored 0. Partial context: Receivable+Inventory days (sales basis) rose 161.5 -> 181.2 days FY19->FY26."
  - "D4 Current Ratio computed via screener-convention proxy (Other Assets / Other Liabilities = 4.35), not a literal current-asset/current-liability schedule."
  - "M2, M5, M9 scored 0 as PEER DATA NEEDED (GEE Ltd, Esab India, Ador Welding not in provided corpus)."
  - "M6 R&D described qualitatively in AR2026 p.99-100 (DSIR recognition, NABL lab, doctoral candidate) but never quantified as %-of-revenue; scored 0, not estimated."
  - "FY25 ROCE (12.54%) and ROE dip are AR-stated consequence of IPO equity-base enlargement (Reserves 162.68cr FY24 -> 331.45cr FY25 on IPO proceeds), not operating deterioration."
  - "Revenue CAGR FY19-FY26 = 14.89%, just under the 15% threshold used in M8/M11 middle tiers; both scored at the lower tier as a result."
data_notes_source: "runs/diffnkg-2026-09-05/inputs/screening/screener-Data_Sheet.csv; runs/diffnkg-2026-09-05/work/txt/annual-report/Annual_Report_2026.txt pp.99-100,142,145,168"
block_b_trend: "deteriorating - FY26 FCF proxy -16.36cr despite record PAT 50.32cr (screener-data), driven by capex proxy 39.15cr (CWIP alone +19.84cr) and receivables (128.18cr) outgrowing sales"
analyst_note: "Two of the three worst-looking numbers (FY25 ROCE/ROE dip, FY26 negative FCF) are IPO-linked base and capex effects per AR2026, not operating decay; downstream stages should weigh Block A/B scores with this in mind rather than reading them as raw deterioration. The genuine gap is shareholder-alignment data (promoter holding wholly absent) and the payables data gap blocking a complete WC Days read. Moat base is thin (3/12) but 4 tests are blocked purely by missing peer data, not by evidenced weakness, so MODERATE may understate once GEE/Esab/Ador figures are available downstream."
```
