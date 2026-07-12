# GATE 0 SCORECARD — Azad Engineering Ltd (AZAD)
Run date: 2026-07-12 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 7 years (FY2020 to FY2026). Scoring adapted to 7-year history.
All P&L/Balance Sheet/Cash Flow annual figures sourced from screener-Data_Sheet.csv
(standalone basis, Rs Cr) unless otherwise anchored. Cross-checked against and
supplemented by the two results PDFs (Rs Mn, standalone), which reconcile exactly
to the Data Sheet for FY2025/FY2026 (e.g. FY26 Sales 590.38 Cr = Rs 5,903.75 Mn;
FY26 PAT 132.16 Cr = Rs 1,321.61 Mn). screener-Balance_Sheet.csv, -Cash_Flow.csv,
-Profit_Loss.csv, -Quarters.csv and -Customization.csv contained no populated data
rows (headers only) — all figures below are pulled from screener-Data_Sheet.csv and
the two results PDFs.

Note on capital history: FY24 (Dec 2023 IPO) and FY25 (~Rs 700 Cr QIP, March 2025
quarter) both saw large equity infusions ahead of a capex ramp (CWIP Rs 79.78 Cr →
Rs 256.68 Cr, FY25→FY26). This mechanically depresses ROCE/ROE and near-term cash
conversion in FY25-FY26 even as the underlying P&L continues to compound. Flagged
below, not adjusted for.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (screener.in ROCE/ROE
rows were blank in screener-Balance_Sheet.csv, so computed per formula).
- FY2020-FY2024: Capital Employed approximated as Net Worth + Borrowings (Total −
  "Other Liabilities" per Data Sheet structure), because screener-Data_Sheet.csv
  does not split current vs non-current liabilities for these years. Basis note:
  "Other Liabilities" treated as proxy for Current Liabilities.
- FY2025-FY2026: Capital Employed computed as actual Total Assets − Total Current
  Liabilities from the audited Standalone Balance Sheet (results FY26 p.4, columns
  "As at March 31, 2026" and "As at March 31, 2025").
- EBIT = PBT − Other Income + Interest (computed each year from screener-Data_Sheet.csv
  PROFIT & LOSS rows; cross-checked to results FY26 p.3 for FY25/FY26).

| FY | PBT | OI | Interest | EBIT | Capital Employed | ROCE | Basis |
|---|---|---|---|---|---|---|---|
|2020|29.81|1.45|6.10|34.46|148.24|23.24%|NW+Borrowings (screener-data)|
|2021|19.10|4.16|4.89|19.83|179.74|11.03%|NW+Borrowings (screener-data)|
|2022|38.68|3.35|13.62|48.95|316.99|15.44%|NW+Borrowings (screener-data)|
|2023|13.20|9.85|52.38|55.73|504.43|11.05%|NW+Borrowings (screener-data)|
|2024|80.79|31.99|47.27|96.07|684.54|14.03%|NW+Borrowings (screener-data)|
|2025|126.02|11.55|17.94|132.41 (audited: 132.40)|1,629.90|8.12%|Actual TA−CL (results FY26 p.4)|
|2026|185.48|47.53|29.71|167.66|1,896.61|8.84%|Actual TA−CL (results FY26 p.4)|

(All figures screener-data unless marked; EBIT FY25/26 cross-checked to results FY26 p.3)

**A1 Median ROCE** = 11.05% (sorted: 8.12, 8.84, 11.03, 11.05, 14.03, 15.44, 23.24) → band 10-14.9% → **Score 1**
**A2 Minimum single-year ROCE** = 8.12% (FY2025, results FY26 p.4) → band 8-11.9% → **Score 1**
**A3 Median ROE** = 13.80% (see table below) → band 12-14.9% → **Score 2**
**A4 ROCE trend, latest (FY26=8.84%) vs earliest (FY20=23.24%)**: decline of 14.4pp → >5pp decline → **Score 0**

ROE = PAT ÷ average Net Worth (opening+closing÷2). FY2020 uses closing Net Worth only
(no FY2019 opening balance in provided data, stated per formula rule).
Net Worth = Equity Share Capital + Reserves (screener-data); FY25/FY26 cross-checked
to audited "Total equity" (results FY26 p.4: Rs 14,176.03 Mn / Rs 15,519.78 Mn).

| FY | PAT | Net Worth (closing) | Avg NW used | ROE |
|---|---|---|---|---|
|2020|21.10|86.80|86.80 (closing only, no opening)|24.31%|
|2021|13.51|92.36|89.58|15.08%|
|2022|28.00|120.01|106.19|26.37%|
|2023|8.51|204.03|162.02|5.25%|
|2024|58.58|645.10|424.57|13.80%|
|2025|88.53|1,417.61|1,031.36|8.59%|
|2026|132.16|1,551.98|1,484.80|8.90%|

**BLOCK A TOTAL = 1+1+2+0 = 4/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO and PAT (screener-Data_Sheet.csv; FY25/FY26 CFO cross-checked exactly to
results FY26 p.5 standalone cash flow: FY26 CFO = Rs (1,232.63) Mn = Rs (123.26) Cr;
FY25 CFO = Rs 628.85 Mn = Rs 62.89 Cr).

| FY | CFO | PAT |
|---|---|---|
|2020|36.60|21.10|
|2021|33.91|13.51|
|2022|20.94|28.00|
|2023|-10.21|8.51|
|2024|-6.95|58.58|
|2025|62.89|88.53|
|2026|-123.26|132.16|

Cumulative CFO (FY20-26) = 13.92 Cr | Cumulative PAT = 350.39 Cr

**B1 Cumulative CFO ÷ Cumulative PAT = 13.92 ÷ 350.39 = 0.04** → <0.50 → **Score 0**

FCF = CFO − Capex (purchase of PPE+intangibles from cash flow statement, excl.
acquisitions). Capex breakdown is NOT available in screener-Data_Sheet.csv for
FY2020-FY2024 (only aggregate "Cash from Investing Activity" is given, which
for FY2025 in particular is dominated by ~Rs 622 Cr of QIP-proceeds bank deposits,
not capex — using it as a capex proxy would misstate FCF badly). Capex is
available only for FY2025 and FY2026 from the audited cash flow statement
(results FY26 p.5: "Purchase of property, plant and equipment (including capital
work in progress and capital advances)"). FY2020-FY2024 capex marked N/A (not in
provided data); B2/B3 computed on the FY2025-FY2026 subset only — PARTIAL DATA.

| FY | CFO | Capex | FCF |
|---|---|---|---|
|2025|62.89|275.13 (results FY26 p.5)|-212.24|
|2026|-123.26|570.71 (results FY26 p.5)|-693.97|

**B2 FCF-positive years as proportion** (of the 2 years with capex data) = 0/2 = 0% → <50% → **Score 0**
**B3 Cumulative FCF ÷ Cumulative PAT** (FY25+FY26 subset) = -906.21 ÷ 220.69 = -4.11 → negative → **Score 0**

Working Capital Days = Receivable Days + Inventory Days − Payable Days, Revenue
basis (COGS not used as a single explicit line is not clearly isolable; stated).
Payable Days require Trade Payables, only available in the audited balance sheet
for FY2025/FY2026 (results FY26 p.4); not present in screener-Data_Sheet.csv for
FY2020-FY2024, so full WC Days is only computable for FY2025 and FY2026.

| FY | Receivable Days | Inventory Days | Payable Days | WC Days |
|---|---|---|---|---|
|2020|121.8|49.3|N/A|N/A (R+I only = 171.1)|
|2021|159.2|103.8|N/A|N/A (R+I only = 263.0)|
|2022|140.1|107.7|N/A|N/A (R+I only = 247.8)|
|2023|172.1|124.8|N/A|N/A (R+I only = 296.9)|
|2024|182.0|142.4|N/A|N/A (R+I only = 324.4)|
|2025|178.6|151.9|63.6 (results FY26 p.4)|266.9|
|2026|191.2|201.9|53.4 (results FY26 p.4)|339.7|

**B4 Change in WC Days**: true "latest vs earliest" (FY26 vs FY20) is not
computable (no FY20 payables). Using the closest fully-computable comparator,
FY26 (339.7) vs FY25 (266.9) = +72.8 days increase — well past the >15-day
threshold, and consistent with the R+I-only proxy for FY20-24 which already
shows a rising trend (171.1 → 324.4) before any payables offset. → increased
>15 days → **Score 0**

**BLOCK B TOTAL = 0+0+0+0 = 0/20**

block_b_trend: **deteriorating** — cumulative CFO/PAT of 0.04 across FY20-26,
driven by FY23 (-10.21 Cr), FY24 (-6.95 Cr) and especially FY26 (-123.26 Cr)
operating cash outflows against a receivables+inventory build (WC days
171→340) that has outpaced the payables offset in the two years it can be
measured.

---

## BLOCK C: GROWTH (Max 20)

Revenue and PAT (screener-Data_Sheet.csv).

**C1 Revenue CAGR** (FY20→FY26, 6 yrs): (590.38/122.17)^(1/6)−1 = **30.04%** → ≥20% → **Score 5**
**C2 PAT CAGR** (FY20→FY26, 6 yrs): (132.16/21.10)^(1/6)−1 = **35.78%** → ≥20% → **Score 5** (no loss-to-profit swing; PAT positive every year FY20-26, low point FY23 at 8.51 Cr)
**C3 Positive YoY revenue years**: 5 of 6 YoY periods positive (FY21 declined -1.4% vs FY20; FY22-FY26 all grew) = 83.3% → 75-99% → **Score 3**
**C4 PAT CAGR − Revenue CAGR** = 35.78% − 30.04% = **+5.74pp** → ≥+3pp → **Score 5**

**BLOCK C TOTAL = 5+5+3+5 = 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY2026)

Net Debt = Total Borrowings (incl. lease liabilities, per Data Sheet convention;
reconciles exactly: standalone borrowings Rs 4,515.80 Mn + lease Rs 124.46 Mn =
Rs 4,640.26 Mn ≈ Data Sheet Rs 464.02 Cr) − Cash & Bank.

**D1 Net Debt ÷ EBITDA (latest, FY26)**: Net Debt = 464.02 − 183.58 = 280.44 Cr
(screener-data). EBITDA = PBT−OI+Dep+Interest = 217.75 Cr (computed, screener-data).
280.44 ÷ 217.75 = **1.29x** → 1-2x → **Score 3**

**D2 Interest Coverage EBIT ÷ Interest (latest, FY26)**: 167.66 ÷ 29.71 = **5.65x**
(screener-data, computed) → 5-9.9x → **Score 4**

**D3 Debt ÷ Equity (latest, FY26)**: 464.02 ÷ 1,551.98 = **0.30x** (screener-data)
→ 0.1-0.5 → **Score 4**

**D4 Current Ratio (latest, FY26)**: Total current assets Rs 9,836.28 Mn ÷ Total
current liabilities Rs 2,985.27 Mn (results FY26 p.4, audited) = **3.30x** → ≥2.0
→ **Score 5**

**BLOCK D TOTAL = 3+4+4+5 = 16/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding pattern (promoter holding, pledge) and no contingent liabilities
data were present in any provided file — screener-Data_Sheet.csv has no
shareholding-pattern section, screener-Customization.csv/-Balance_Sheet.csv are
unpopulated, and neither results PDF (quarterly financial results filings)
discloses shareholding pattern or contingent liabilities notes (these are
disclosed separately under SEBI Reg. 31 filings / Annual Report notes, not
provided here).

**E1 Promoter holding (latest quarter)**: N/A (not in provided data) → **Score 0**
**E2 Promoter holding change over 3 years**: N/A (not in provided data) → **Score 0**
**E3 Promoter pledge (latest)**: N/A (not in provided data) → **Score 0**
**E4 Contingent liabilities ÷ Net Worth (latest)**: N/A (not in provided data) → **Score 0**

**BLOCK E TOTAL = 0+0+0+0 = 0/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer data (FY2026, standalone, screener-Data_Sheet.csv) for MTAR Technologies,
Dynamatic Technologies, PTC Industries, Unimech Aerospace, computed on the same
EBIT/EBITDA basis (PBT−OI+Interest[+Dep]) as AZAD:

| Company | FY26 Sales | FY26 EBITDA | EBITDA Margin | GM proxy (Rev−RM)/Rev | Mkt Cap (Cr) |
|---|---|---|---|---|---|
|AZAD|590.38|217.75|36.88%|78.28%|16,013.04|
|MTAR Technologies|876.11|171.05|19.52%|42.54%|21,842.39|
|Dynamatic Tech.|1,621.34|182.68|11.27%|48.06%|7,258.69|
|PTC Industries|602.78|131.77|21.86%|43.16%|26,389.88|
|Unimech Aerospace|240.49|75.12|31.24%|74.55%|6,026.54|

Peer median EBITDA margin = 20.69% | Peer median GM proxy = 45.61%
(all peer figures: peer *-Data_Sheet.csv, PROFIT & LOSS rows, FY2026 column)

**M1 Pricing Power**: AZAD EBITDA margin 33.9% (FY20) → 36.9% (FY26), +2.99pp
expansion, AND revenue CAGR 30.0% ≥10% → **Score 5**

**M2 Cost Advantage vs peer median EBITDA margin**: 36.88% vs 20.69% = +16.19pp
above → ≥5pp above → **Score 5**

**M3 Capital Efficiency**: FAT = Revenue ÷ Net Block = 590.38 ÷ 756.08 = 0.78x
(screener-data); ROCE FY26 = 8.84% (computed above). FAT <1x AND ROCE <12% →
**Score 0**

**M4 Customer Stickiness**: 1 revenue-decline year (FY21, -1.4%), fully
recovered by FY22 (194.47 Cr, above FY20's 122.17 Cr) → max 1 decline year,
fully recovered → **Score 3**

**M5 Scale & Dominance**: AZAD mcap Rs 16,013 Cr ranks 3rd of 5 (PTC 26,390 >
MTAR 21,842 > AZAD 16,013 > Dynamatic 7,259 > Unimech 6,027) — top-3 mcap.
Margin: AZAD 36.88% is #1 of 5, i.e. top margin within the top-3 mcap group
(PTC 21.86%, MTAR 19.52%, AZAD 36.88%) → top-3 mcap AND margin top-2 → **Score 3**
(not eligible for 5: AZAD is not the largest mcap in the segment)

**M6 Technology/R&D**: R&D/Revenue not disclosed anywhere in provided data
(no R&D line item in screener-Data_Sheet.csv or the results PDFs) → N/A (not in
provided data) → **Score 0**

**M7 Regulatory/License**: Context notes describe AZAD as a manufacturer of
"mission/life-critical" aerospace/defence/energy components, but no evidence of
licensing regime or a verified total count of listed players in the regulated
segment is present in the provided data (the 4-peer comparator set was supplied
by the orchestrator, not confirmed as an exhaustive industry census). Per the
no-estimate rule → N/A (not in provided data) → **Score 0**

**M8 Distribution**: AZAD is a B2B precision-component supplier to OEMs; no
distribution-network reach/outlet data is provided or applicable → **Score 0**

**M9 Brand**: Gross margin proxy = (Revenue − Raw Material Cost) ÷ Revenue
(screener-data "Raw Material Cost" row used as Material Cost; matches "Cost of
materials consumed" in results FY26 p.3 exactly). AZAD 78.28% vs peer median
45.61% = +32.67pp above, AND revenue CAGR 30.0% ≥10% → ≥10pp above AND ≥10%
growth → **Score 5**

**M10 Switching Costs**: Revenue grew in all but 1 year (FY21 decline), but
receivable days rose from 121.8 (FY20) to 191.2 (FY26), +69.4 days — well
past the ≤10-day "stable" threshold required for the "growth all but 1 year"
tier, and there are not 2+ decline years to qualify for the next tier down →
**Score 0**

**M11 Network Effects** (7-yr history, ≥6 yr test applies in full): Latest
3yr revenue CAGR (FY23→FY26) = (590.38/251.68)^(1/3)−1 = 32.88%; prior 3yr
CAGR (FY20→FY23) = (251.68/122.17)^(1/3)−1 = 27.24%. Latest > prior. Selling
and admin expense as % of revenue (screener-data; FY26 not separately broken
out, folded into "Other Expenses"): 7.55% (FY20) → 6.07% → 4.13% → 5.32% →
4.31% → 3.92% (FY25), a declining trend over the 6 years it can be measured →
latest 3yr CAGR > prior 3yr AND selling % declining → **Score 5**

**M12 Negative WC/Float**: WC Days computable only for FY25 (266.9) and FY26
(339.7), both far above 45 days; the R+I-only proxy for FY20-24 (171-324) is
already above 45 before any payables offset, so WC days are >45 in effectively
every year measurable → **Score 0**

| Test | Score | Present (≥3)? |
|---|---|---|
|M1 Pricing Power|5|Yes|
|M2 Cost Advantage|5|Yes|
|M3 Capital Efficiency|0|No|
|M4 Customer Stickiness|3|Yes|
|M5 Scale & Dominance|3|Yes|
|M6 Technology/R&D|0|No (N/A)|
|M7 Regulatory/License|0|No (N/A)|
|M8 Distribution|0|No|
|M9 Brand|5|Yes|
|M10 Switching Costs|0|No|
|M11 Network Effects|5|Yes|
|M12 Negative WC/Float|0|No|

**BLOCK F TOTAL = 5+5+0+3+3+0+0+0+5+0+5+0 = 26/60**
**Moats present (≥3) = 6 → Moat Classification: FORTRESS** (6+ threshold)

---

## MOAT PROFILE (bars, /5)

```
M1  Pricing Power       █████ 5
M2  Cost Advantage      █████ 5
M3  Capital Efficiency  ▒▒▒▒▒ 0
M4  Customer Stickiness ███▒▒ 3
M5  Scale & Dominance   ███▒▒ 3
M6  Technology/R&D      ▒▒▒▒▒ 0 (N/A - no data)
M7  Regulatory/License  ▒▒▒▒▒ 0 (N/A - no data)
M8  Distribution        ▒▒▒▒▒ 0 (N/A - B2B OEM model)
M9  Brand               █████ 5
M10 Switching Costs     ▒▒▒▒▒ 0
M11 Network Effects     █████ 5
M12 Negative WC/Float   ▒▒▒▒▒ 0
```

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
|A: Return on Capital|4|20|
|B: Cash Generation Quality|0|20|
|C: Growth|18|20|
|D: Balance Sheet Strength|16|20|
|E: Shareholder Alignment|0|20|
|**Core Total**|**38**|**100**|
|F: Moat Score|26|60|
|**Grand Total**|**64**|**160**|

Data confidence: 7 years of history → 7-9 band → **moderate confidence**, no
history-based downgrade tier triggered (LIMITED downgrade applies only at 3-4
years; auto-AVERAGE only applies at <3 years).

**Classification matrix**: Core = 38 → Core <40 = **AVOID** (base classification;
moat class does not enter the matrix at Core <40).

**Deal-breaker overrides** (recorded per rule; caps are non-binding here since
the base classification, AVOID, is already at or below every cap listed):
1. Block A = 4 <8 → max GOOD. Driven by FY2025 (ROCE 8.12%) and FY2026
   (ROCE 8.84%) — the two years immediately following the ~Rs 700 Cr QIP
   (March 2025 quarter), where the equity/capital base expanded well ahead of
   incremental EBIT.
2. Block B = 0 <8 → max GOOD. Driven by FY2023 (-10.21 Cr), FY2024 (-6.95 Cr)
   and FY2026 (-123.26 Cr) operating cash outflows against a rising working
   capital base.
4. Cumulative CFO/PAT = 0.04 <0.50 → max AVERAGE. Same years as above, most
   acutely FY2026, where CFO of -123.26 Cr sits against PAT of +132.16 Cr —
   a receivables (+87.66 Cr YoY) and inventory (+138.15 Cr YoY) build funded
   by the QIP cash rather than operations.

Deal-breakers 3, 5, 6, 7, 8, 9 not triggered (median ROCE 11.05% ≥10%; pledge
data not available so not assessed; ND/EBITDA 1.29x with IC 5.65x; only 1 of 6
YoY revenue periods declined; PAT positive in all of the last 3 years; 7 years
of history ≥3).

**CLASSIFICATION: AVOID**

Strongest block: **C (Growth), 18/20**. Weakest blocks: **B (Cash Generation
Quality) and E (Shareholder Alignment), 0/20 each** — B on hard evidence
(cumulative CFO/PAT of 0.04), E on absent data (no shareholding-pattern or
contingent-liabilities disclosure in the provided files).

**Decision line**: Gate 0 mechanics classify AZAD as AVOID on trailing
return-on-capital and cash-conversion metrics that are mechanically depressed
by the FY2024 IPO and FY2025 QIP raises funding an active capex ramp (CWIP
Rs 79.78 Cr → Rs 256.68 Cr) — a documented post-capital-raise rebase pattern,
not an operating-quality deterioration; revenue and PAT CAGRs (30.0%/35.8%),
EBITDA margin expansion, balance sheet leverage (D/E 0.30x, current ratio
3.30x) and 6 of 12 moat tests present (FORTRESS class) are all strong. Per
pipeline rules this does not halt the run; it flags forward with the
historical depressors named above for downstream stages and the operator to
weigh.

---

## INPUT GAPS

- Promoter shareholding pattern (holding %, 3-yr change, pledge) — not present
  in any provided file (E1, E2, E3)
- Contingent liabilities — not present in any provided file (E4)
- R&D spend / R&D-to-revenue — not disclosed anywhere in provided data (M6)
- Total listed-player count / licensing-regime evidence for the regulated
  segment — not evidenced in provided data (M7)
- Capex breakdown for FY2020-FY2024 — screener-Data_Sheet.csv gives only
  aggregate "Cash from Investing Activity"; capex only isolable for FY2025 and
  FY2026 from the results PDFs (affects B2, B3)
- Trade payables for FY2020-FY2024 — not present in screener-Data_Sheet.csv;
  only available for FY2025/FY2026 from the audited balance sheet (affects B4,
  M12)
