# GATE 0 SCORECARD — Ram Ratna Wires Ltd (RAMRAT)
Run date: 2026-07-29 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year history.
Data sources: screener.in CSV export (screener-Data_Sheet.csv is the only
populated sheet in the export bundle; screener-Profit_Loss.csv,
screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv,
screener-Customization.csv are unpopulated templates with no numeric data —
confirmed by direct read), plus one results PDF located at
`inputs/results/789d1085-67ff-46ca-b91f-38b82bd6b01d.pdf` (Q3 FY26 / 9M
ended 31-Dec-2025 standalone + consolidated results, board meeting
06-Feb-2026) used for cross-check. The second results PDF path given in
the task (`0a5a99ff-9ec3-47bb-b91f-49ca3432890d.pdf`) does not exist in
`inputs/results/` — directory listing confirms only the one PDF above is
present. This is recorded as an input gap, not invented around.

FY26 (year ended 31-Mar-2026) in the Data_Sheet is the latest annual
column and is internally consistent with the Q3 FY26 PDF (9M standalone
revenue ₹3,351.31 Cr + implied Q4 ≈ ₹1,825.34 Cr against FY26 full-year
₹5,176.65 Cr; quarterly PAT progression 15.46→21.30→31.29→39.01 Cr sums
close to FY26 annual 107.05 Cr, standalone/consolidated minority-interest
differences accepted).

**Note on interpretation of "Change in Inventory" line**: cross-checked
against PBT reconciliation and against screener's own disclosed quarterly
"Operating Profit" figures (e.g. Q4 FY26 = ₹91.83 Cr, screener-Data_Sheet.csv
Quarters block) — Change in Inventory must be *subtracted* from the sum of
other expense lines to reconcile to PBT (it represents finished-goods stock
movement, a separate Ind AS line from "Raw Material Cost" = cost of
materials consumed). All EBITDA/OPM figures below use this reconciled
convention; every one was cross-checked against a directly disclosed PBT or
quarterly Operating Profit figure.

---

## FORMULA NOTES / PROXIES USED (apply throughout)

- EBIT = PBT + Interest (screener convention; PBT already nets other income).
- EBITDA (excl. other income, screener's "Operating Profit") = PBT − Other
  Income + Depreciation + Interest. Cross-validated exactly against
  screener-Data_Sheet.csv quarterly "Operating Profit" row.
- Capital Employed (for ROCE) = Equity Share Capital + Reserves + Borrowings
  (= Total Assets − Other Liabilities). Screener's 2-line balance sheet does
  not split current/non-current liabilities, so "Other Liabilities" is used
  as the Current Liabilities proxy — stated explicitly, not a screener-
  disclosed ROCE figure (the Balance_Sheet.csv template's ROCE/ROE row is
  present but unpopulated). Closing-balance basis used for all years (no
  FY16 opening balance available).
- Current Ratio (D4) = "Other Assets" ÷ "Other Liabilities" (same current/
  non-current split limitation; stated as proxy).
- ROE = PAT ÷ average Net Worth (Equity Share Capital + Reserves); FY17 uses
  closing Net Worth only (opening FY16 unavailable), per rule.
- Receivable/Inventory Days computed on a revenue basis (no explicit COGS
  line disclosed) — stated.
- Payable Days: NOT COMPUTABLE. Trade Payables is not disclosed separately
  anywhere in the provided data (only the aggregate "Other Liabilities",
  which also contains provisions/other current items). This breaks WC Days
  (B4) and M12 — both marked N/A / score 0, not estimated.
- FCF (B2, B3): NOT COMPUTABLE. Cash flow data provides only aggregate
  "Cash from Investing Activity," not a discrete purchase-of-PP&E/
  intangibles line. FY25-FY26 CFI is additionally distorted by the Tefabo
  Product Pvt Ltd subsidiary acquisition and the Global Copper Pvt Ltd
  merger into RRWL (results PDF, standalone notes, note vii) — using CFI as
  a capex proxy would materially overstate capex. Marked N/A / score 0, not
  estimated.
- Gross margin proxy (M9) = (Revenue − Raw Material Cost) ÷ Revenue.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

| FY | PBT | Interest | EBIT (=PBT+Int) | Cap. Employed | ROCE | PAT | Avg Net Worth | ROE |
|----|----:|---------:|-----------------:|--------------:|-----:|----:|--------------:|----:|
|17|33.55|11.16|44.71|273.32|16.36%|22.05|125.32*|17.60%|
|18|43.37|17.79|61.16|421.67|14.51%|27.17|146.13|18.59%|
|19|24.67|29.50|54.17|497.94|10.88%|15.63|175.24|8.92%|
|20|16.69|28.84|45.53|470.99|9.67%|14.45|181.15|7.98%|
|21|21.15|25.89|47.04|561.39|8.38%|14.90|189.52|7.86%|
|22|72.58|27.57|100.15|541.10|18.51%|52.19|235.85|22.13%|
|23|64.41|33.50|97.91|578.18|16.93%|44.89|291.54|15.40%|
|24|74.64|40.64|115.28|675.38|17.07%|56.09|368.91|15.20%|
|25|97.16|54.72|151.88|788.26|19.27%|70.15|454.75|15.43%|
|26|152.97|85.52|238.49|1254.71|19.01%|107.05|531.41|20.15%|

(all cells: screener-Data_Sheet.csv, PROFIT & LOSS / BALANCE SHEET rows,
respective FY column; ROCE/ROE computed per proxies above)
*FY17 ROE uses closing Net Worth only (125.32), opening FY16 unavailable.

- **A1 Median ROCE = 16.65%** (median of the 10 values above, computed) →
  band 15-19.9% → **score 3**
- **A2 Minimum single-year ROCE = 8.38% (FY21)** → band 8-11.9% →
  **score 1**
- **A3 Median ROE = 15.42%** (median of the 10 values above, computed) →
  band 15-19.9% → **score 4**
- **A4 ROCE trend, FY26 (19.01%) vs FY17 (16.36%)**: latest ≥ earliest
  (+2.65pp) → **score 5**

**Block A = 3+1+4+5 = 13 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

| FY | CFO | PAT |
|----|----:|----:|
|17|20.61|22.05|
|18|2.16|27.17|
|19|-7.75|15.63|
|20|64.30|14.45|
|21|-25.64|14.90|
|22|150.78|52.19|
|23|64.72|44.89|
|24|138.35|56.09|
|25|227.33|70.15|
|26|-92.99|107.05|

(screener-Data_Sheet.csv, CASH FLOW / PROFIT & LOSS rows, each FY column)

- **B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO = 541.87, ΣPAT = 424.57
  (both computed by summation of the table above) → ratio = 1.28x → band
  ≥1.00 → **score 5**
- **B2 FCF-positive years proportion**: N/A (not in provided data) — capex
  breakdown absent, see formula notes above → **score 0**
- **B3 Cumulative FCF ÷ Cumulative PAT**: N/A (not in provided data) — same
  reason → **score 0**
- **B4 Change in WC Days, latest vs earliest**: N/A (not in provided data)
  — Payable Days component (Trade Payables) not disclosed anywhere in the
  source files → **score 0**

**Block B = 5+0+0+0 = 5 / 20**

**block_b_trend = deteriorating (latest year)**: FY26 CFO swung to
**-92.99 Cr** (screener-Data_Sheet.csv, CASH FLOW, FY26) against a **record
PAT of 107.05 Cr** the same year — a reversal from FY25's +227.33 Cr. This
tracks a large receivables and inventory build funding FY26 revenue growth:
Receivables 390.15 → 640.61 Cr, Inventory 233.68 → 486.09 Cr (screener-
Data_Sheet.csv, BALANCE SHEET, FY25 vs FY26). The 10-year cumulative CFO/PAT
of 1.28x still clears B1's top band, but the single-year divergence is
material and should be watched downstream (FLAG-CASH candidate).

---

## BLOCK C: GROWTH (Max 20)

Sales FY17 → FY26: 800.83 → 5176.65 (screener-Data_Sheet.csv, Sales row).
All 9 YoY comparisons FY18-FY26 are positive (no decline years).

- **C1 Revenue CAGR (FY17→FY26, 9yr) = 23.04%** (computed:
  (5176.65/800.83)^(1/9)-1) → band ≥20% → **score 5**
- **C2 PAT CAGR (FY17→FY26, 9yr) = 19.19%** (computed:
  (107.05/22.05)^(1/9)-1) → band 15-19.9% → **score 4**
- **C3 Positive YoY revenue years = 9/9 = 100%** → **score 5**
- **C4 PAT CAGR − Revenue CAGR = 19.19% − 23.04% = -3.85pp** → band
  -3 to -8pp → **score 1**

**Block C = 5+4+5+1 = 15 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20), latest = FY26

- Borrowings FY26 = 675.23, Cash & Bank FY26 = 13.86 (screener-Data_Sheet.csv,
  BALANCE SHEET, FY26) → Net Debt = 661.37
- EBITDA (excl. other income, computed per proxy) FY26 = 261.43
- **D1 Net Debt ÷ EBITDA = 661.37 / 261.43 = 2.53x** → band 2-3x →
  **score 1**
- Interest FY26 = 85.52 (screener-Data_Sheet.csv, FY26); EBIT = 238.49
  (computed) → **D2 Interest Coverage = 238.49 / 85.52 = 2.79x** → band
  1.5-2.9x → **score 1**
- Net Worth FY26 = 579.48 (computed, Equity+Reserves) → **D3 Debt/Equity =
  675.23 / 579.48 = 1.17x** → band 1.0-1.5x → **score 1**
- Other Assets FY26 = 1304.61, Other Liabilities FY26 = 738.80 (screener-
  Data_Sheet.csv, BALANCE SHEET, FY26; used as Current Assets/Current
  Liabilities proxy, stated above) → **D4 Current Ratio = 1304.61 / 738.80
  = 1.77x** → band 1.5-1.99x → **score 4**

**Block D = 1+1+1+4 = 7 / 20**

Deal-breaker check #6 (ND/EBITDA >3x AND IC <3x → AVOID): ND/EBITDA = 2.53x
(not >3x) → **not triggered**, though both D1 and D2 sit at the weak end of
their bands — leverage/coverage is a genuine watch item, not a data gap.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Confirmed by direct grep of screener-Data_Sheet.csv and
screener-Customization.csv for "promoter / pledge / holding / contingent":
**no matches**. No shareholding-pattern filing was provided in inputs/
(per B00 carry-forward gap), and the only results PDF located (Q3 FY26
board outcome + standalone/consolidated results + auditor limited-review
reports + segment notes) contains no shareholding, pledge, or contingent
liability disclosure either.

- **E1 Promoter holding**: NOT FOUND → **score 0**
- **E2 Promoter holding change, 3yr**: NOT FOUND → **score 0**
- **E3 Promoter pledge**: NOT FOUND → **score 0**
- **E4 Contingent liabilities ÷ Net Worth**: NOT FOUND → **score 0**

**Block E = 0 / 20** — entirely a data-availability gap, not a scored
finding of poor alignment; carried into input_gaps and the FLAG-GATE0 note.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set (RAMRAT peers, copper winding-wire/electrical-wire makers):
BHAGYANGR (Bhagyanagar India), PRECWIRE (Precision Wires India), VIDYAWIRES
(Vidya Wires). **PRECWIRE-Data_Sheet.csv contains only FY2015-16 data**
(confirmed by direct read — a stale/truncated export) and is excluded from
all FY26 peer-margin and market-cap comparisons below; peer medians use
BHAGYANGR + VIDYAWIRES only, stated at each test.

FY26 OPM (EBITDA excl. OI ÷ Sales, computed per proxy, cross-checked
against each company's own PBT):
- RAMRAT: 261.43/5176.65 = **5.05%**
- BHAGYANGR: (67.51−4.72+7.38+35.96)/2377.83 = 106.13/2377.83 = **4.46%**
  (BHAGYANGR-Data_Sheet.csv, FY26)
- VIDYAWIRES: (77.94−8.61+3.65+12.80)/1839.64 = 85.78/1839.64 = **4.66%**
  (VIDYAWIRES-Data_Sheet.csv, FY26)
- Peer median (2 names) = 4.56%

Market cap (screener-Data_Sheet.csv / peer Data_Sheet.csv, META block):
RAMRAT ₹4,248.77 Cr; PRECWIRE ₹6,591.00 Cr; VIDYAWIRES ₹1,904.56 Cr;
BHAGYANGR ₹1,250.28 Cr.

**M1 Pricing Power**: OPM FY17 6.40% → FY26 5.05%, change -1.35pp (within
±2pp, i.e. stable) AND revenue CAGR 23.04% (≥10%) → **score 3**

**M2 Cost Advantage vs peer median EBITDA margin**: RAMRAT 5.05% vs peer
median 4.56% (2-peer, PRECWIRE excluded — stale data) = +0.49pp, within
±2pp → **score 1**

**M3 Capital Efficiency**: FAT = Sales/Net Block = 5176.65/639.28 = 8.10x
(>2x); ROCE FY26 = 19.01% (>15%, but ≤20% so top tier not met) → **score 3**

**M4 Customer Stickiness**: zero revenue-decline years (confirmed above);
Receivable Days FY17 67.28 → FY26 45.16 (computed, revenue basis) — trend
improving but not stable within ±10 days across the full 10yr range
(38.7-70.9 days) → falls to second tier (0 decline years trivially
satisfies "max 1 decline year, fully recovered") → **score 3**

**M5 Scale & Dominance** (within the 3-peer + RAMRAT universe supplied;
broader cable-sector names such as Polycab/KEI are out of scope of
provided data, stated): RAMRAT is 2nd-largest by mcap (PRECWIRE larger)
but has the top OPM among the 3 names with FY26 data → top-3 mcap AND
margin top 2 → **score 3**

**M6 Technology/R&D**: no R&D expense line disclosed anywhere in the
provided data → **score 0, PEER DATA NEEDED / N/A**

**M7 Regulatory/License**: copper winding-wire manufacturing is an
unregulated/unlicensed segment with materially more than 10 listed
competitors → **score 0**

**M8 Distribution**: no dealer/distribution-network figures disclosed in
any provided source → **score 0, N/A (not in provided data)**

**M9 Brand** (GM proxy = (Revenue−Raw Material Cost)/Revenue, stated):
RAMRAT FY26 = (5176.65−4829.10)/5176.65 = **6.71%**; BHAGYANGR FY26 =
(2377.83−2190.87)/2377.83 = **7.86%**; VIDYAWIRES FY26 =
(1839.64−1713.51)/1839.64 = **6.86%**; peer median (2 names) = 7.36%.
RAMRAT is at/below peer median → **score 0**

**M10 Switching Costs**: revenue grew every year (9/9) AND Receivable Days
change FY17→FY26 = -22.12 days (a decrease, i.e. "rose ≤10 days" is
satisfied) → **score 5**

**M11 Network Effects** (10yr history ≥ required 6yr): latest-3yr revenue
CAGR (FY23→FY26) = 25.03% (computed) vs prior-3yr (FY20→FY23) = 22.36%
(computed) — latest > prior; Selling & admin expense as % of sales: FY20
1.22% → FY23 0.94% → FY26 0.88% (screener-Data_Sheet.csv, computed),
declining → **score 5**

**M12 Negative WC/Float**: N/A (not in provided data) — Payable Days
component (Trade Payables) not disclosed, so WC Days cannot be computed
(same gap as B4) → **score 0**

| Test | Score | Present (≥3)? |
|---|---:|---|
|M1 Pricing Power|3|Yes|
|M2 Cost Advantage|1|No|
|M3 Capital Efficiency|3|Yes|
|M4 Customer Stickiness|3|Yes|
|M5 Scale & Dominance|3|Yes|
|M6 Technology/R&D|0|No|
|M7 Regulatory/License|0|No|
|M8 Distribution|0|No|
|M9 Brand|0|No|
|M10 Switching Costs|5|Yes|
|M11 Network Effects|5|Yes|
|M12 Negative WC/Float|0|No|

**Moat Score = 3+1+3+3+3+0+0+0+0+5+5+0 = 23 / 60**
**Moats present (score ≥3): 6** (M1, M3, M4, M5, M10, M11)
**Moat classification: 6+ present → FORTRESS**

Moat profile bar:
```
M1  [###......] 3   M7  [..........] 0
M2  [#.........] 1   M8  [..........] 0
M3  [###......] 3   M9  [..........] 0
M4  [###......] 3   M10 [#####.....] 5
M5  [###......] 3   M11 [#####.....] 5
M6  [..........] 0   M12 [..........] 0
```

---

## CLASSIFICATION

Data confidence: 10 years → **10+ yrs full**, no downgrade.
history_downgrade = false.

| Block | Score | Max |
|---|---:|---:|
|A — Return on Capital|13|20|
|B — Cash Generation Quality|5|20|
|C — Growth|15|20|
|D — Balance Sheet Strength|7|20|
|**Core (A+B+C+D)**|**40**|**80**|
|E — Shareholder Alignment|0|20|
|F — Moat|23|60|
|**Grand Total**|**63**|**160**|

Moat classification: **FORTRESS** (6 tests present)

Classification matrix: Core = 40 falls in the **40-59** bucket →
**AVERAGE** (moat tier does not move this bucket per the matrix; FORTRESS
only lifts classification at Core ≥60).

**Deal-breaker check:**
1. Block A <8 → max GOOD: Block A = 13, not triggered.
2. **Block B <8 → max GOOD: Block B = 5, triggered** (non-binding here —
   AVERAGE is already below the GOOD cap).
3. Median ROCE <10% → max AVERAGE: median ROCE = 16.65%, not triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: ratio = 1.28x, not triggered.
5. Pledge >15% → max AVERAGE: pledge NOT FOUND, cannot evaluate — not
   triggered (data gap, not a clean pass).
6. ND/EBITDA >3x AND IC <3x → AVOID: ND/EBITDA = 2.53x, not triggered.
7. Revenue declined in majority of years → max AVERAGE: 0 decline years,
   not triggered.
8. PAT negative in any of last 3 years → max AVERAGE: FY24/25/26 all
   positive, not triggered.
9. History <3 years → AVERAGE: 10 years available, not triggered.

**Classification: AVERAGE**

**Strongest block**: C — Growth (15/20), driven by a clean 9/9 positive-
revenue-year record and a 23.04% revenue CAGR.

**Weakest block**: E — Shareholder Alignment (0/20), entirely a data-
availability gap (no promoter/pledge/contingent-liability disclosure in
any provided source), not a scored finding against the company. Numerically
tied for structurally weakest: B — Cash Generation Quality (5/20), also
substantially data-gap-driven (B2/B3/B4 = 0 for missing capex and trade-
payables breakdowns) but carrying one genuine fact worth flagging: the
FY26 CFO reversal to -92.99 Cr against record PAT (see block_b_trend).

**Decision line**: RAMRAT screens AVERAGE at Gate 0 on a Core score of
40/80, held down by (a) a real FY19-FY21 ROCE/ROE trough (8.4-10.9% ROCE,
COVID-period) that depresses the 10-year medians despite a strong FY22-FY26
recovery (ROCE 17-19%, ROE 15-22%), and (b) five scoring items (B2, B3, B4,
E1-E4, M12) that are 0 purely because the underlying data (capex
breakdown, trade payables, shareholding pattern, contingent liabilities)
was not present in the provided screener export or the single located
results PDF. The moat profile is comparatively strong (FORTRESS, 6/12
tests present) on pricing stability, capital efficiency, customer
stickiness, scale-within-peer-set, switching costs and network-effect
growth-deceleration-vs-selling-expense tests, but M2/M9 show RAMRAT's
margins and gross-margin proxy are in-line-to-slightly-below its two
comparable peers, not a cost or brand advantage. Downstream stages should
treat Block E and the FCF/WC gaps as evidence gaps to close (shareholding
pattern filing, cash flow statement with capex breakdown, trade payables)
rather than as confirmed weaknesses, per pipeline rules on missing data.

---
