# STAGE 1: GATE 0 SCORECARD — Akums Drugs & Pharmaceuticals Ltd (AKUMS)

Run date: 2026-07-10 | Model: claude-sonnet-5 | Data source: screener.in CSV exports only (no annual report, no results PDFs, no rating note)

Data available: 9 years (FY15, FY16, FY20, FY21, FY22, FY23, FY24, FY25, FY26). Scoring adapted to this 9-data-point / 11-fiscal-year-span history. **Gap: FY17-FY19 not provided in the export** (screener Data_Sheet). Trend/CAGR metrics use FY15 as earliest and FY26 as latest available endpoints; single-year comparisons across the gap (FY16→FY20) are excluded from YoY counts.

No shareholding-pattern file, no results extracts, no annual report, no rating note were provided for this run — this depresses Block E and several moat tests to zero, not because of company quality but because of input scope. Flagged, not halted.

---

## FORMULA BASIS NOTES (read before the blocks)

- **ROCE/ROE**: screener-Balance_Sheet.csv and screener-Customization.csv ratio rows were exported blank (no populated ROCE/ROE column). Both are therefore **computed**, not sourced. ROCE = EBIT ÷ Capital Employed, where EBIT = PBT + Interest, and Capital Employed = Equity Share Capital + Reserves + Borrowings (= Total Assets − Other Liabilities, screener's standard bucket convention, used as the current-liabilities proxy since no current/non-current split is exported).
- **Payable Days / full WC Days**: Trade Payables is not a separate line in screener-Data_Sheet (only "Other Liabilities," a combined bucket). Payable Days is therefore **not computable**. B4 and M12 use Receivable Days + Inventory Days only, stated as a partial proxy.
- **Current Ratio (D4)**: Current Assets/Current Liabilities are not split out anywhere in the export (Other Assets and Other Liabilities are combined buckets). D4 is scored 0 / N/A.
- **Capex/FCF**: screener-Data_Sheet gives only aggregate "Cash from Investing Activity," not a discrete capex line. Capex is proxied as Δ(Net Block + CWIP) + Depreciation for the year (an accounting-identity derivation, not an estimate), computable only for consecutive-year pairs. This excludes FY15 (no prior year) and FY20 (prior data point is FY16, a 4-year gap, so the identity would blend 4 years of capex into 1 year of depreciation and is invalid). B2/B3 therefore run over 7 valid pairs: FY16, FY21, FY22, FY23, FY24, FY25, FY26.
- **Shareholding (Block E)**: no shareholding-pattern file was supplied for Akums in any input. Promoter holding, promoter holding change, pledge, and contingent liabilities are all N/A (not in provided data). Despite the operator note that Akums is a professionally-run promoter (Jain family) company, no FII+DII percentage was supplied either, so the "professionally managed: 3 if FII+DII>50%" branch of E1 cannot be applied — E1 is scored 0/N/A, not 3.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Per-year EBIT, Capital Employed, and ROCE (computed; screener Data_Sheet for underlying PBT/Interest/Equity/Reserves/Borrowings):

| FY | PBT | Interest | EBIT | Cap. Employed | ROCE |
|---|---|---|---|---|---|
| 15 | 76.74 | 23.12 | 99.86 | 748.80 | 13.34% |
| 16 | 88.78 | 22.14 | 110.92 | 842.81 | 13.16% |
| 20 | 113.82 | 19.93 | 133.75 | 897.25 | 14.91% |
| 21 | 172.26 | 6.74 | 179.00 | 1014.82 | 17.64% |
| 22 | -193.20 | 16.66 | -176.54 | 1016.96 | -17.36% |
| 23 | 150.30 | 46.25 | 196.55 | 1336.28 | 14.71% |
| 24 | -45.28 | 50.61 | 5.33 | 1274.72 | 0.42% |
| 25 | 345.25 | 34.60 | 379.85 | 3135.23 | 12.12% |
| 26 | 382.10 | 94.07 | 476.17 | 3470.78 | 13.72% |

(all inputs: screener Data_Sheet)

- **A1 Median ROCE = 13.34%** (5th of 9 sorted values) → band 10-14.9% = **3**
- **A2 Minimum single-year ROCE = -17.36% (FY22)** → <8% = **0**
- **A3 Median ROE = 8.72%** (computed: PAT ÷ average Net Worth; FY15 uses closing NW only, opening unavailable due to gap; FY20 likewise uses closing NW as opening is the missing FY19; see table below) → <12% = **0**
- **A4 ROCE trend, FY26 (13.72%) vs FY15 (13.34%)**: latest ≥ earliest → **5**

ROE detail:
| FY | PAT | Avg/Closing NW | ROE |
|---|---|---|---|
|15|43.07|494.02 (closing only, opening N/A)|8.72%|
|16|61.48|561.70|10.95%|
|20|43.65|722.40 (closing only, opening N/A — FY19 gap)|6.04%|
|21|122.71|803.63|15.27%|
|22|-252.54|753.42|-33.52%|
|23|94.86|669.59|14.17%|
|24|-4.04|713.35|-0.57%|
|25|338.18|1878.26|18.01%|
|26|255.19|3180.18|8.02%|
(all inputs: screener Data_Sheet)

**Block A = 3 + 0 + 0 + 5 = 8 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (9 yrs) = 2672.78 (screener Data_Sheet, sum FY15-FY26); Cumulative PAT (9 yrs) = 702.56 (screener Data_Sheet).

- **B1 Cumulative CFO ÷ Cumulative PAT = 2672.78 ÷ 702.56 = 3.80x** → ≥1.00 = **5**

FCF (computed, capex proxy — see Formula Basis Notes), 7 valid years:
| FY | CFO | Capex (proxy) | FCF |
|---|---|---|---|
|16|89.14|105.14|-16.00|
|21|130.61|289.30|-158.69|
|22|31.85|225.29|-193.44|
|23|176.63|261.67|-85.04|
|24|498.26|311.35|+186.91|
|25|465.20|327.43|+137.77|
|26|1181.20|227.58|+953.62|
(CFO, Net Block, CWIP, Depreciation: screener Data_Sheet)

- **B2 FCF-positive years = 3 of 7 (42.9%)** → <50% = **0**
- **B3 Cumulative FCF (825.13) ÷ Cumulative PAT over same 7 years (615.84) = 1.34x** → ≥0.60 = **5**
- **B4 WC Days change, FY26 vs FY15** (partial: Receivable Days + Inventory Days only, payables unavailable — see Formula Basis Notes):
  - FY15: RD = 272.76/1464.27×365 = 67.98d; ID = 260.85/1464.27×365 = 65.02d → 133.00d (screener Data_Sheet)
  - FY26: RD = 796.56/4359.02×365 = 66.69d; ID = 755.71/4359.02×365 = 63.25d → 129.94d (screener Data_Sheet)
  - Change = -3.06 days → within ±5 days = **3**

**Block B = 5 + 0 + 5 + 3 = 13 / 20**

**block_b_trend = improving.** CFO jumped from 465.2 cr (FY25) to 1181.2 cr (FY26), +154% YoY (screener Data_Sheet); FCF (computed) also flipped decisively positive in FY24-FY26 (+186.91, +137.77, +953.62) after four straight negative-FCF years (FY16, FY21, FY22, FY23).

---

## BLOCK C: GROWTH (Max 20)

Revenue: FY15 = 1464.27, FY26 = 4359.02 (screener Data_Sheet, both endpoints positive, 11-year span).
- Revenue CAGR = (4359.02/1464.27)^(1/11) - 1 = **10.43%**
PAT: FY15 = 43.07, FY26 = 255.19 (screener Data_Sheet, both endpoints positive).
- PAT CAGR = (255.19/43.07)^(1/11) - 1 = **17.56%**

- **C1 Revenue CAGR = 10.43%** → band 10-14.9% = **3**
- **C2 PAT CAGR = 17.56%** → band 15-19.9% = **4**
- **C3 Positive YoY revenue years**: valid consecutive pairs only (FY16→20 excluded as a 4-year gap, not a true YoY): FY15-16 (+), FY20-21 (+), FY21-22 (+), FY22-23 (-, 3654.82 < 3671.89), FY23-24 (+), FY24-25 (-, 4118.16 < 4178.18), FY25-26 (+) — 5 of 7 positive = 71.4% (screener Data_Sheet) → band 50-74% = **1**
- **C4 PAT CAGR − Revenue CAGR = 17.56% − 10.43% = +7.13pp** → ≥+3pp = **5**

**Block C = 3 + 4 + 1 + 5 = 13 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

- **D1 Net Debt ÷ EBITDA**: Borrowings 157.43 − Cash & Bank 1680.60 = **-1523.17 (net cash)** (screener Data_Sheet). EBITDA FY26 = Sales 4359.02 − (RM 2499.68 + ΔInv -13.84 + Power 184.29 + OtherMfr 110.90 + Employee 753.82 + SellAdmin 178.25 + OtherExp 96.02) = **549.90** (computed, screener Data_Sheet line items). Net cash position → **5**
- **D2 Interest Coverage = EBIT ÷ Interest = 476.17 ÷ 94.07 = 5.06x** (screener Data_Sheet) → band 5-9.9x = **4**
- **D3 Debt ÷ Equity = 157.43 ÷ 3313.35 = 0.048x** (screener Data_Sheet) → <0.1 = **5**
- **D4 Current Ratio**: not computable — screener export has no current/non-current split for assets or liabilities → N/A = **0**

**Block D = 5 + 4 + 5 + 0 = 14 / 20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding-pattern data was provided in any input file for this run (no promoter holding %, no pledge %, no FII/DII %, no contingent-liability disclosure).

- **E1 Promoter holding**: N/A (not in provided data) → **0**
- **E2 Promoter holding change**: N/A → **0**
- **E3 Promoter pledge**: N/A → **0**
- **E4 Contingent liabilities ÷ Net Worth**: N/A → **0**

**Block E = 0 / 20** — entirely a data-availability artifact, not a scored deficiency in the company.

---

## CORE SCORE

Blocks A(8) + B(13) + C(13) + D(14) + E(0) = **48 / 100**

Block scores as %: A 40% | B 65% | C 65% | D 70% | E 0%.
**Strongest block: D (Balance Sheet Strength) at 70%. Weakest block: E (Shareholder Alignment) at 0%, driven entirely by absent shareholding data, not a scored quality failure.**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin by year (computed, screener Data_Sheet — Sales minus RM, ΔInventory, Power, Other Mfr Exp, Employee, Selling/Admin, Other Expenses; excludes Other Income):

| FY | EBITDA | Margin |
|---|---|---|
|15|64.26|4.39%|
|16|90.30|5.47%|
|20|116.54|4.83%|
|21|143.11|5.26%|
|22|-264.10|-7.19% (one-off: Other Expenses spiked to 565.07 vs ~75-100 cr normal run-rate)|
|23|342.03|9.36%|
|24|147.99|3.54% (one-off: Other Expenses 434.05, IPO-period exceptional items)|
|25|461.34|11.20%|
|26|549.90|12.61% (annual-summed); cross-check via quarters-summed Operating Profit = 522.03/4359.02 = **11.98%** (screener Data_Sheet Quarters section) — quarters figure used for peer comparison in M2/M5 below since it is a directly reported field rather than a re-summed one|

**M1 Pricing Power**: margin expanded FY15 (4.39%) → FY26 (12.61%), +8.2pp, well past ≥2pp, AND revenue CAGR 10.43% ≥10% → **5**

**M2 Cost Advantage vs peer median EBITDA margin (FY26, quarters-summed Operating Profit ÷ Sales)**:
- COHANCE: 426.99/2268.55 = 18.82% (COHANCE Data_Sheet, Quarters)
- INNOVACAP: 238.46/1630.02 = 14.63% (INNOVACAP Data_Sheet, Quarters)
- PPLPHARMA: 921.63/8869.07 = 10.39% (PPLPHARMA Data_Sheet, Quarters)
- WINDLAS: 104.76/904.09 = 11.59% (WINDLAS Data_Sheet, Quarters)
- Peer median = (11.59+14.63)/2 = **13.11%**
- Akums (quarters basis) = 11.98%, which is 1.13pp *below* peer median, within ±2pp → **1**

**M3 Capital Efficiency**: FAT = Sales ÷ Net Block = 4359.02/1455.80 = 2.99x (screener Data_Sheet); ROCE FY26 = 13.72%. FAT>3x AND ROCE>20% fails; FAT>2x AND ROCE>15% fails (ROCE short); FAT>1x AND ROCE>12% holds → **1**

**M4 Customer Stickiness**: 2 revenue-decline years (FY22-23, FY24-25) identified in Block C3, overall CAGR positive → **1**

**M5 Scale & Dominance** (peer set limited to the 4 supplied comparators; broader listed universe not enumerable from provided data — noted as a limitation): Market cap ranking — PPLPHARMA 23598.52 > COHANCE 17270.55 > **AKUMS 11051.63** > INNOVACAP 5668.41 > WINDLAS 1713.64 (screener/COHANCE/INNOVACAP/PPLPHARMA/WINDLAS Data_Sheet, "Market Capitalization" field). Akums is 3rd of 5 by mcap. Margin ranking (FY26, computed above): COHANCE 18.82% > INNOVACAP 14.63% > AKUMS 11.98% > WINDLAS 11.59% > PPLPHARMA 10.39%. Akums is 3rd of 5 by margin (not top 2). Top-3 mcap holds, but margin-top-2 fails → falls to "top 5 mcap" band → **1**

**M6 Technology/R&D**: R&D expense is not a separate disclosed line anywhere in the screener export → N/A (not in provided data) → **0**

**M7 Regulatory/License**: cannot verify the true count of listed players in the regulated pharma-CDMO/formulations segment from provided data — only 4 comparators were supplied, not a full segment enumeration → PEER DATA NEEDED, scored **0**

**M8 Distribution**: no outlet count, distributor count, or geographic-reach metric disclosed in any input → N/A → **0**

**M9 Brand** (GM proxy = (Revenue − Material Cost) ÷ Revenue, Material Cost = Raw Material Cost + Change in Inventory, FY26, stated proxy):
- Akums: (4359.02 − 2485.84)/4359.02 = **42.97%** (screener Data_Sheet)
- COHANCE: (2268.55 − 748.15)/2268.55 = 67.02% (COHANCE Data_Sheet)
- INNOVACAP: (1630.02 − 849.16)/1630.02 = 47.90% (INNOVACAP Data_Sheet)
- PPLPHARMA: (8869.08 − 3614.22)/8869.08 = 59.26% (PPLPHARMA Data_Sheet)
- WINDLAS: (904.09 − 543.03)/904.09 = 39.94% (WINDLAS Data_Sheet)
- Peer median = (47.90+59.26)/2 = 53.58%. Akums 42.97% is 10.61pp *below* peer median → at/below → **0**

**M10 Switching Costs**: overall revenue growth (CAGR +10.43%) with 2 decline years identified (C3) → "overall growth, 2+ decline years" → **1**

**M11 Network Effects** (7 continuous years FY20-FY26 available, ≥6-year threshold met, two-window test applied): Latest 3yr (FY23→FY26) revenue CAGR = (4359.02/3654.82)^(1/3)-1 = **6.05%**; Prior 3yr (FY20→FY23) CAGR = (3654.82/2414.16)^(1/3)-1 = **14.83%** (screener Data_Sheet). Latest 3yr CAGR is *lower* than prior (deceleration), and latest 3yr CAGR is well below the 20% threshold for the middle band → **0**

**M12 Negative WC/Float**: cannot be scored — payable days is not computable (Trade Payables not disclosed), so true (negative) WC days cannot be assessed; partial RD+ID figures (129-133 days) cannot demonstrate a negative-WC/float position without the payables offset → N/A → **0**

**Moat score = 5+1+1+1+1+0+0+0+0+1+0+0 = 10 / 60**

Moats "present" (score ≥3): M1 only. **moats_confirmed = 1 → THIN**

---

## CLASSIFICATION

- Data confidence: 9 data points → band "7-9 = moderate" (no formal downgrade tier triggered; the FY17-FY19 gap is noted but the count itself sits in the moderate band, not the 3-4 LIMITED band).
- Core score = 48/100 → **Core 40-59 = AVERAGE** (moat class does not branch the outcome at this tier per the classification matrix).

**Deal-breaker check:**
1. Block A (8) <8? No (exactly 8, not below) — no trigger.
2. Block B (13) <8? No — no trigger.
3. Median ROCE (13.34%) <10%? No — no trigger.
4. Cumulative CFO/PAT (3.80x) <0.50? No — no trigger.
5. Pledge >15%? Not in provided data — cannot confirm, not triggered on absence of evidence.
6. ND/EBITDA >3x AND IC <3x? Net cash position — no trigger.
7. Revenue declined in majority of years? 2 of 7 valid YoY pairs (28.6%) — not majority, no trigger.
8. **PAT negative in any of last 3 years? YES — FY24 PAT = -4.04 cr (screener Data_Sheet). Triggers → max AVERAGE.**
9. History <3 years? No, 9 data points — no trigger.

**Deal-breaker #8 triggers, driven by FY24** (and note FY22 also carried a much larger loss, -252.54 cr, though it falls outside the strict "last 3 years" window). Both FY22 and FY24 losses coincide with abnormal "Other Expenses" spikes (FY22: 565.07 cr; FY24: 434.05 cr, vs a ~75-100 cr normal run-rate) and major equity-structure changes (bonus share issuances, face-value/capital-base changes) around the company's IPO period — consistent with a **documented post-IPO rebase / legacy cleanup pattern**. Per pipeline rules, this is recorded for downstream position-sizing consideration; it does not lift the Gate 0 cap here.

Since the matrix-derived base classification (AVERAGE) and the deal-breaker cap (max AVERAGE) coincide, the deal-breaker does not further depress the outcome — final classification is already AVERAGE on core-score grounds alone.

**FINAL CLASSIFICATION: AVERAGE**

---

## DASHBOARD SUMMARY

```
BLOCK A (Return on Capital).........  8/20  [####------] 40%
BLOCK B (Cash Generation Quality)... 13/20  [######----] 65%
BLOCK C (Growth).................... 13/20  [######----] 65%
BLOCK D (Balance Sheet Strength).... 14/20  [#######---] 70%
BLOCK E (Shareholder Alignment).....  0/20  [----------]  0%  (no shareholding data supplied)
                                     -----
CORE SCORE...........................48/100

MOAT PROFILE (12 tests, present = score >=3):
M1 Pricing Power.........  5  [FORTRESS-GRADE]  PRESENT
M2 Cost Advantage......... 1
M3 Capital Efficiency..... 1
M4 Customer Stickiness.... 1
M5 Scale & Dominance...... 1
M6 Technology/R&D......... 0  (N/A - not disclosed)
M7 Regulatory/License..... 0  (PEER DATA NEEDED)
M8 Distribution............ 0  (N/A - not disclosed)
M9 Brand................... 0
M10 Switching Costs....... 1
M11 Network Effects....... 0
M12 Negative WC/Float..... 0  (N/A - payables not disclosed)
                          ---
MOAT SCORE................10/60   MOATS PRESENT: 1 -> THIN

GRAND TOTAL: 48 + 10 = 58/160

+----------------------------------------------------+
| CLASSIFICATION: AVERAGE                             |
| Deal-breaker #8 (PAT negative, FY24) - capped at AVG |
| Data confidence: MODERATE (9 data points, FY17-19    |
| gap noted)                                           |
+----------------------------------------------------+

Strongest block: D (Balance Sheet Strength), 70%
Weakest block: E (Shareholder Alignment), 0% - data gap, not
a scored quality failure
```

**Decision line**: Gate 0 does not halt (no STOP verdict exists). AKUMS clears with an AVERAGE classification driven by weak return-on-capital consistency (FY22 ROCE -17.36%, FY24 near-zero) and a FY24 PAT loss deal-breaker, both traceable to one-off IPO-period expense items rather than sustained operating deterioration; cash generation is improving sharply (FY26 CFO +154% YoY) and the balance sheet is net-cash. Block E and four of twelve moat tests are zero purely because promoter/shareholding data and qualitative disclosures (R&D, distribution, contingent liabilities, full segment peer count) were not supplied in this run's input set — these should be revisited if richer inputs (annual report, shareholding pattern, results extracts) become available in a later run. Proceeds to Stage 2 with flags carried forward.

---
