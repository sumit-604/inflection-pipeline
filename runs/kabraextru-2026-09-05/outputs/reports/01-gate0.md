# STAGE 1 — GATE 0 SCORECARD (PIPELINE MODE)
Company: Kabra Extrusion Technik Ltd (KABRAEXTRU) | Run date: 2026-09-05 | Model: claude-sonnet-5

Data sources: runs/kabraextru-2026-09-05/inputs/screening/screener-Data_Sheet.csv (only populated
screener sheet — consolidated P&L FY17-FY26, 10 quarters Mar-24 to Jun-26, balance sheet FY17-FY26,
cash flow FY17-FY26, price); Annual_Report_2026.txt (FY26 audited, FY25 comparative, standalone +
consolidated); Annual_Report_2025.txt (FY25 audited, FY24 comparative); peer Data_Sheets
RAJOOENG / WINDMACHIN / HBLENGINE. No results PDFs, no shareholding-pattern filing, no CRISIL
rationale document in this run (input gaps, see YAML).

Data available: 10 years (FY2017 to FY2026), annual P&L/balance sheet/cash flow (screener
Data_Sheet); 10 quarters Mar-2024 to Jun-2026. Scoring adapted to 10-year history. Two sub-metrics
(FCF/capex breakdown, trade-payables-based WC days) are constrained to a 3-year window (FY24-FY26)
because the AR text corpus only covers FY2025 and FY2026 annual reports — flagged inline and in
data_notes.

---
## PRIORITY VERIFICATION (Company Memory / Spear override load-bearing facts, checked first)

**1. "~40% market share in plastic extrusion machinery" claim.**
Found in AR FY2024-25 (Annual_Report_2025.txt, p.37), Directors' Report "Key Strengths" section:
"KET enjoys market leadership status in the extrusion market with ~40% market share in its product
category as on FY25" (AR FY25, p.37). This is a **self-reported, unsourced** claim: no independent
study or market-research house is cited, "product category" is not defined (unclear if it means
pipe-extrusion lines specifically, all plastic extrusion machinery, domestic-only or global), and
the base (units, revenue, or installations) is not stated. The FY2025-26 Annual Report
(Annual_Report_2026.txt) **does not repeat the ~40% figure**; its equivalent "Key Strengths"
section (AR FY26, p.35-36) only says the company "enjoys a strong leadership position in the
domestic plastic extrusion machinery market" with no percentage (AR FY26, p.35). The only
quantified reach figures repeated in both years are "15,000+ installations" and "100+ countries"
(AR FY26, p.69/p.123, Corporate Overview note). Conclusion: the 40% figure is a prior-year,
unverified management assertion, not corroborated by this run's corpus and not restated in FY26.

**2. Battrixx / Geon Energy li-ion battery packs — does the FY26 consolidated loss sit there?**
Yes, confirmed by the Segment Information note (standalone: AR FY26 p.105-106, Note 38;
consolidated: AR FY26 p.160, same note; three-year trend visible via AR FY25 p.104/p.158
comparative):

| Rs Cr | FY24 | FY25 | FY26 |
|---|---|---|---|
| Extrusion Machinery segment revenue | 348.49 | 362.85 | 314.89 |
| Extrusion Machinery segment result | 45.49 | 70.14 | 50.75 |
| Battery (Geon) segment revenue | 266.16 | 126.98 | 136.11 |
| Battery (Geon) segment result | +6.52 | **-25.53** | **-43.35** |
| Total segment result (pre-interest) | 52.02 | 44.61 | 7.40 |

(AR FY26 p.105-106 Note 38 for FY26/FY25 standalone; AR FY26 p.160 for FY26/FY25 consolidated —
figures identical to standalone at the revenue/result line; AR FY25 p.104 Note (segment info) for
FY24 comparative, AR FY25 p.158 consolidated.) Battery division revenue nearly halved FY24→FY25
(266→127 Cr) and the segment swung from a small profit (+6.5 Cr FY24) to a widening loss (-25.5 Cr
FY25, -43.4 Cr FY26), even as it partially recovered revenue FY25→FY26. The Extrusion Machinery
core stayed profitable throughout but its own segment result also declined FY25→FY26 (70.1→50.8
Cr). Consolidated PBT of -7.78 Cr (screener Data_Sheet; matches AR FY26 Consolidated P&L line
"Profit before tax (VIII-IX)" -778.04 lakh, p.122) is the net of a still-profitable core machinery
business and a battery-division loss that more than offsets it, plus unallocated
interest/corporate costs (segment result 7.40 Cr pre-interest, less 11.39 Cr finance cost, less
other unallocated items, plus an exceptional item, nets to -7.78 Cr). **The FY26 consolidated loss
sits in Geon/Battrixx, not in the legacy extrusion business.**

**3. FY26 consolidated loss vs the CRISIL downgrade path.**
AR FY26 Corporate Governance Report (p.51) discloses the rating history directly:

| | Upto 5-Apr-2025 | W.e.f. 13-May-2026 | Stated reason |
|---|---|---|---|
| Long-term | CRISIL A/Negative (downgraded from A+/Negative) | CRISIL A-/Stable (downgraded from A/Negative) | "Basis performance reported for Quarter 3" |
| Short-term | CRISIL A1 (reaffirmed) | CRISIL A2+ (downgraded from A1) | "Basis performance reported for Quarter 3" |

(AR FY26, p.51.) This confirms the full path named in Company Memory: A+/Neg → A/Neg → A-/Stable,
A1 → A2+. The stated "rationale" in the corpus is a single terse line ("basis performance reported
for Quarter 3") for both legs; no separate CRISIL rationale report is in this run's corpus (input
gap "rating" stands — the *fact* of the downgrade and its trigger quarter are anchored, but the
underlying CRISIL analytical rationale is NOT FOUND). The downgrade lines up with the timeline of
the widening Battery segment loss and the FY26 full-year swing to a consolidated net loss.

**4. Sales FY23 670 → FY26 451 Cr; borrowings 74 → 145 Cr; FY26 CFO 8.96 Cr; cash 3.08 Cr.**
Confirmed against screener Data_Sheet and cross-checked in the AR:
- Revenue: 670.01 (FY23) → 607.77 (FY24) → 476.85 (FY25) → 451.05 (FY26) Cr (screener Data_Sheet).
  Extrusion segment note (AR FY26 p.105) shows the FY26 slowdown tied to "slower execution and
  fund disbursement under Jal Jeevan Mission (JJM), delays in infrastructure spending by state
  governments, and weakness in export markets" (AR FY26, p.36, MD&A).
- Borrowings: screener shows 73.98 Cr (FY23) → 145.06 Cr (FY26). AR FY26 Note 17 (p.148-149,
  consolidated) shows FY26 borrowings are almost entirely **short-term secured working-capital
  loans** (Rs 141.09 Cr financial borrowings + Rs 3.97 Cr lease liabilities = Rs 145.06 Cr,
  reconciling exactly to the screener figure), secured by hypothecation of "all present and future
  movable assets and book debts" (AR FY26, p.148, Note 17(i)) — i.e., the borrowing increase is a
  working-capital funding line, not fresh capex-linked term debt.
- CFO FY26 = Rs 8.96 Cr (screener; matches AR FY26 Consolidated Cash Flow Statement, p.123, "Net
  cash flow from operating activities" Rs 896.49 lakh) versus Rs 43.45 Cr FY25 (AR FY26 p.123
  comparative column, Rs 4,345.20 lakh) — a 79% collapse.
- Cash FY26 = Rs 3.08 Cr (screener Data_Sheet); AR FY26 Consolidated Cash Flow Statement shows
  narrower "cash and cash equivalents" at year-end of Rs 2.04 Cr (Rs 204.02 lakh, p.123) — the
  screener figure likely also nets in other bank balances; difference is immaterial to the
  direction of the finding.
- **Direction and cause**: working-capital days (receivable + inventory − payable, computed from
  screener Data_Sheet Sales/Receivables/Inventory and AR Note 18/34.1 trade payables — see Block B4
  below) rose from ~154 days (FY24) to ~244 days (FY26), a deterioration of ~90 days in two years,
  driven mostly by inventory days (143→232 days) rather than receivables. Cash conversion is
  **deteriorating**, not improving, and the extra borrowing is funding that working-capital stretch.

---
## FORMULA NOTES (apply once, used throughout)

- **EBIT (ROCE/interest-coverage basis)** = PBT + Interest (includes Other Income, matching the
  Company's own Schedule III ratio disclosure — see cross-validation below). **EBITDA (same basis)**
  = EBIT + Depreciation.
- **Operating EBITDA (moat-block margin tests M1/M2/M9 only)** = PBT + Interest + Depreciation −
  Other Income, i.e. excludes Other Income (dividend/interest income, fair-value/investment gains)
  to isolate core operating profitability for pricing-power/cost-advantage tests. Verified
  line-by-line against the P&L cost lines for every year (see Block C/Moat detail) — matches to the
  rupee.
- **Capital Employed** (denominator for ROCE) = Equity Share Capital + Reserves + Borrowings
  (year-end). The screener Data_Sheet does not split current vs non-current liabilities, so the
  literal "Total Assets − Current Liabilities" cannot be computed from it. This NW+Borrowings proxy
  is cross-validated against the Company's own AR-disclosed consolidated ROCE (Note 43, Schedule
  III ratios): computed FY26 0.62% vs AR-disclosed 0.61%; computed FY25 8.63% vs AR-disclosed
  8.67% — both within 0.05pp, confirming the proxy matches the Company's own capital-employed
  basis. **Marked "computed", cross-validated against source for FY25-FY26** (AR FY26, p.112
  standalone / p.167 consolidated, Note 43).
- **ROE** computed as PAT ÷ average Net Worth (opening+closing)/2; FY17 uses closing net worth only
  (no FY16 opening data available), stated. Cross-validated exactly against AR Note 43: computed
  FY26 -1.19% = AR-disclosed -1.19%; computed FY25 7.04% = AR-disclosed 7.04% (AR FY26, p.167,
  Consolidated Note 43). Exact match.

---
## BLOCK A: RETURN ON CAPITAL (Max 20)

| FY | EBIT (PBT+Int) | Capital Employed | ROCE | Net Worth (avg) | PAT | ROE |
|---|---|---|---|---|---|---|
|17|24.76|234.70|10.55%|226.33 (closing only)|20.42|9.02%|
|18|22.70|237.34|9.57%|229.80|20.00|8.70%|
|19|33.26|255.55|13.02%|239.70|24.37|10.17%|
|20|7.69|258.87|2.97%|239.14|7.41|3.10%|
|21|34.33|302.10|11.36%|255.14|24.56|9.63%|
|22|46.18|387.37|11.92%|303.53|30.27|9.97%|
|23|63.32|457.48|13.84%|356.21|37.50|10.53%|
|24|54.13|537.45|10.07%|417.69|33.82|8.10%|
|25|50.98|590.61|8.63% (AR: 8.67%)|457.14|32.20|7.04% (AR: 7.04%)|
|26|3.61|586.55|0.62% (AR: 0.61%)|451.94|-5.37|-1.19% (AR: -1.19%)|

All figures: screener Data_Sheet (Sales/PBT/Interest/Equity Share Capital/Reserves/Borrowings
columns), computed per formula notes above; AR cross-checks as cited.

- **A1 Median ROCE** = 10.31% (avg of 5th/6th sorted values 10.07%, 10.55%) → band 10-14.9% = **1**
  (computed, screener Data_Sheet + AR cross-check)
- **A2 Minimum single-year ROCE** = 0.62% (FY26) → band <8% = **0** (computed)
- **A3 Median ROE** = 8.86% (avg of 8.70%, 9.02%) → band <12% = **0** (computed)
- **A4 ROCE trend, latest vs earliest** = 0.62% (FY26) vs 10.55% (FY17) = decline of 9.93pp →
  band >5pp decline = **0** (computed)

**Block A = 1 / 20**

---
## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY17-FY26) = 18.41+12.00+5.98+28.45+38.10-62.20-3.73+32.84+43.45+8.96 = **122.26 Cr**
(screener Data_Sheet, Cash from Operating Activity row, all 10 years).
Cumulative PAT (FY17-FY26) = 20.42+20.00+24.37+7.41+24.56+30.27+37.50+33.82+32.20-5.37 = **225.18 Cr**
(screener Data_Sheet, Net profit row).

- **B1 Cumulative CFO ÷ Cumulative PAT** = 122.26 / 225.18 = **0.543** → band 0.50-0.69 = **1**
  (screener Data_Sheet). Note: this sits just above the 0.50 deal-breaker-4 threshold.

**FCF (B2/B3): computable only for FY24-FY26.** Screener's "Cash from Investing Activity" for
FY17-FY23 conflates capex with investment purchases/sales and cannot be decomposed without the
underlying AR cash-flow statements, which are not in this run's corpus for those years (only
Annual_Report_2025.txt and Annual_Report_2026.txt are provided, covering FY24-FY26). Capex (PP&E +
intangibles, ex-acquisitions) taken from AR consolidated Cash Flow Statements:
- FY26: PP&E 2,938.85 + intangibles 799.13 = 3,737.98 lakh = 37.38 Cr (AR FY26, p.124)
- FY25: PP&E 6,249.56 + intangibles 565.63 = 6,815.19 lakh = 68.15 Cr (AR FY26, p.124, comparative
  column)
- FY24: PP&E 5,042.49 lakh outflow, intangibles line shown as +357.21 lakh (net inflow, unusual —
  noted as a data quirk) = net capex 4,685.28 lakh = 46.85 Cr (AR FY25, p.125, comparative column)

| Rs Cr | FY24 | FY25 | FY26 |
|---|---|---|---|
| CFO (screener, = AR) | 32.84 | 43.45 | 8.96 |
| Capex (AR) | 46.85 | 68.15 | 37.38 |
| FCF | -14.01 | -24.70 | -28.42 |

- **B2 FCF-positive years as proportion** = 0 of 3 computable years = 0% → band <50% = **0**
  (computed from AR cash flow statements; scored on the 3-year window available, noted as a data
  constraint, not the full 10-year period)
- **B3 Cumulative FCF ÷ Cumulative PAT** (3-yr window) = (-14.01-24.70-28.42) / (33.82+32.20-5.37) =
  -67.13 / 60.65 = **-1.107** → band <0.20 or negative = **0** (computed)

**B4 WC Days, computable only for FY24-FY26** (trade payables not disclosed anywhere in the
provided corpus for FY17-FY23; screener Data_Sheet balance sheet aggregates payables inside "Other
Liabilities"). Receivables/Inventory from screener Data_Sheet; Trade Payables from AR Note 18/34.1
(consolidated): FY26 Rs 64.96 Cr (AR FY26 p.150, Note 34.1), FY25 Rs 74.70 Cr (AR FY26 p.150-153),
FY24 Rs 81.13 Cr (AR FY25 p.148-151, Note 34.1).

| Rs Cr / days | FY24 | FY25 | FY26 |
|---|---|---|---|
| Sales | 607.77 | 476.85 | 451.05 |
| Receivables | 99.15 | 90.91 | 79.99 |
| Inventory | 238.67 | 290.91 | 286.16 |
| Trade Payables | 81.13 | 74.70 | 64.96 |
| Receivable days | 59.5 | 69.6 | 64.7 |
| Inventory days | 143.3 | 222.7 | 231.6 |
| Payable days | 48.7 | 57.2 | 52.6 |
| **WC days** | **154.1** | **235.1** | **243.7** |

- **B4 Change in WC Days, latest vs earliest available (FY26 vs FY24, not FY26 vs FY17 — FY17
  trade payables NOT FOUND in corpus)** = 243.7 − 154.1 = **+89.6 days increase** → band >15 days
  increase = **0** (computed)

**Block B = 1 / 20**

**block_b_trend: deteriorating** — working capital days rose from ~154 (FY24) to ~244 (FY26), +90
days in two years (screener Data_Sheet Receivables/Inventory/Sales; AR FY26 Note 34.1 / AR FY25
Note 34.1 for Trade Payables). This is the single number that should feed FLAG-CASH downstream.

---
## BLOCK C: GROWTH (Max 20)

Revenue by year (screener Data_Sheet): FY17 276.08 → FY18 268.38 → FY19 245.14 → FY20 220.19 →
FY21 276.23 → FY22 405.90 → FY23 670.01 → FY24 607.77 → FY25 476.85 → FY26 451.05 (Rs Cr).

- **C1 Revenue CAGR** (FY17→FY26, 9 years) = (451.05/276.08)^(1/9) − 1 = **5.61%** → band 5-9.9% =
  **1** (computed)
- **C2 PAT CAGR**: FY26 PAT = -5.37 Cr (negative endpoint) → **N/M (negative endpoint)**, score **0**
  (per CAGR edge rule). Note: **profit-to-loss swing, FY25 (+32.20 Cr) to FY26 (-5.37 Cr)** — logged
  under data_notes.
- **C3 Positive YoY revenue years** = FY21, FY22, FY23 positive; FY18, FY19, FY20, FY24, FY25, FY26
  negative = 3 of 9 years = 33.3% → band <50% = **0** (computed)
- **C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → **score 0 per rule** (computed)

**Block C = 1 / 20**

(Revenue declining in 6 of 9 YoY years is majority-decline → triggers deal-breaker #7, see below.)

---
## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

- **D1 Net Debt ÷ EBITDA (latest)**: Net Debt = Borrowings 145.06 − Cash 3.08 = 141.98 Cr (screener
  Data_Sheet). EBITDA (EBIT+Dep basis) = 3.61 + 30.25 = 33.86 Cr. Ratio = 141.98/33.86 = **4.19x**
  → band >3x = **0** (computed). (Using the narrower operating-EBITDA basis of 10.43 Cr, the ratio
  is 13.6x — even worse; either basis clears the >3x threshold.)
- **D2 Interest Coverage EBIT ÷ Interest (latest)** = 3.61 / 11.39 = **0.317x** → band <1.5x = **0**
  (computed)
- **D3 Debt ÷ Equity (latest)** = 145.06 / 441.49 = **0.329x** → band 0.1-0.5 = **4** (computed;
  cross-checked against AR FY26 Note 43 Consolidated, p.167: Debt-Equity Ratio 0.32x — matches)
- **D4 Current Ratio (latest)** = **1.55x** (AR FY26, p.167, Note 43 Consolidated — source's own
  figure, used directly since screener Data_Sheet does not split current assets/liabilities) →
  band 1.5-1.99 = **4**

**Block D = 8 / 20**

(D1+D2 jointly trigger deal-breaker #6: ND/EBITDA >3x AND IC <3x → AVOID, see below.)

---
## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20, latest = FY26)

- **E1 Promoter holding (latest)** = **60.49%** (AR FY26, p.90, Note 14.4 "Shares held by
  promoters", Total row) → band ≥60% = **5**. Note: the separate Corporate Governance Report
  shareholder-category table (AR FY26, p.50) splits the same promoter population differently
  ("Promoters" 40.51% + "Corporate Bodies (Promoter Co)" 19.47% + "Relatives of promoters" 2.70%
  — an RTA/demat-category split, not the standard SEBI promoter aggregate); Note 14.4's clean
  "Total" row is used as the authoritative figure.
- **E2 Promoter holding change over 3 years**: FY26 = 60.49% (AR FY26, p.90); FY24 = 60.24% with a
  stated "change during the year" of +0.01% (AR FY25, p.89, Note 14.4) → FY23 ≈ 60.23% (derived,
  not a directly-stated point value). Change FY23→FY26 ≈ **+0.26pp** → band ±1% = **3**
- **E3 Promoter pledge (latest)**: **NOT FOUND in provided corpus.** No promoter-pledge disclosure
  located in either Annual Report text (SEBI shareholding-pattern filings, which carry this
  disclosure, are not part of this run's inputs — consistent with the "shareholding" input gap
  carried from B00). Marked N/A, scored **0** per grounding rule (absence of evidence is not
  evidence of 0% pledge).
- **E4 Contingent liabilities ÷ Net Worth (latest)**: Contingent liabilities FY26 = Bank
  guarantees/LCs 2,188.87 + disputed income tax 127.76 + service tax/excise 12.11 + GST disputes
  174.96 + customs 1.43 = 2,505.13 lakh = **25.05 Cr** (AR FY26, p.165, Note 41, Consolidated).
  Net Worth FY26 = 441.49 Cr (screener Data_Sheet). Ratio = 25.05/441.49 = **5.68%** → band 5-15% =
  **3**

**Block E = 11 / 20**

Additional context (not scored): the Board recommended **Rs 0.00 dividend for FY26** versus Rs 2.50
FY25 (AR FY26, p.110, Note 44) — a full dividend cut, consistent with the FY26 loss.

---
## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin series (operating basis, excludes Other Income — see Formula Notes; verified against
P&L cost lines for every year, screener Data_Sheet):

| FY | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|
| EBITDA margin | 10.82% | 10.46% | 8.38% | 5.66% | 14.76% | 13.53% | 11.01% | 9.97% | 10.42% | 2.31% |

Peer data (screener Data_Sheets, RAJOOENG / WINDMACHIN / HBLENGINE — only 3 comparators provided;
HBLENGINE is a diversified defence-electronics/lead-acid-and-lithium-battery major, not a close
segment comparator for the extrusion-machinery business, noted as a limited-comparability peer):

| FY26 | Kabra | Rajoo Engineers | Windsor Machines | HBL Engineering |
|---|---|---|---|---|
| EBITDA margin (operating) | 2.31% | 18.40% | 5.27% | 33.89% |
| Gross margin proxy (Rev−RM Cost)/Rev | 35.72% | 37.02% | 29.67% | 58.02% |
| Market cap (Rs Cr) | 2,025 | 922 | 3,148 | 19,286 |

Peer FY26 EBITDA margins computed as PBT+Interest+Depreciation−Other Income (robust formula, used
because RAJOOENG/WINDMACHIN FY26 cost-line detail (Power/Fuel, Other Mfr Exp, Selling&admin) is
blank in their screener Data_Sheets — a collector gap on the peer sheets, reconciled via the PBT
identity instead). Peer EBITDA median FY26 = 18.40%; Kabra sits 16.09pp below.

- **M1 Pricing Power**: margin FY26 (2.31%) vs FY17 (10.82%) = declined 8.51pp (>5pp decline);
  revenue CAGR 5.61% (<10%) → neither the "expand≥2pp" nor "decline 2-5pp despite growth" band
  fits → **0**
- **M2 Cost Advantage vs peer median EBITDA margin**: Kabra 2.31% vs peer median 18.40% = 16.09pp
  below (also true using FY25: Kabra 10.42% vs peer median 18.37%, 7.95pp below) → band "below" =
  **0**
- **M3 Capital Efficiency**: FAT (Sales/Net Block, FY26) = 451.05/246.46 = 1.83x; ROCE (median
  10.31% or latest 0.62%) both <12% → **0**
- **M4 Customer Stickiness**: 6 of 9 YoY years show revenue decline (≥3+ decline years) → **0**
- **M5 Scale & Dominance**: market cap rank among the 4 companies compared: HBL (19,286) >
  Windsor (3,148) > Kabra (2,025) > Rajoo (922) — Kabra ranks 3rd of 4 (within top 5) but its
  EBITDA margin (2.31%) is the LOWEST of the four, not top-2 → fails tiers 1-2, fits "top 5 mcap" =
  **1**
- **M6 Technology/R&D**: R&D expenditure disclosed for FY26 only — Extrusion Division Rs 367 lakh
  (AR FY26, p.28, Annexure-4) + Geon Division Rs 185.18 lakh (AR FY26, p.29, Annexure-4) = Rs 552.18
  lakh = 5.52 Cr; R&D/Revenue = 5.52/451.05 = **1.22%**. The ≥1% tier also requires "margin above
  peer median", which fails (2.31% vs 18.40%) → **0**
- **M7 Regulatory/License**: unregulated industrial capital-goods manufacturing (no licence/quota
  constraint identified in filings) → **0**
- **M8 Distribution**: reach is quantified (100+ countries, 15,000+ installations — AR FY26, p.69)
  but repeated identically across FY25 and FY26 reports with no stated growth trend or
  revenue-per-outlet metric → scored conservatively at "mentioned/quantified but no growth
  evidence" = **1**
- **M9 Brand**: gross margin proxy FY26 35.72% vs peer median 37.02% = 1.3pp BELOW (also below on
  FY25 basis: 32.78% vs 35.14%) → band "at/below" = **0**
- **M10 Switching Costs**: overall revenue growth FY17→FY26 (276→451 Cr) positive, but with 6
  (≥2) decline years → band "overall growth, 2+ decline years" = **1**
- **M11 Network Effects** (10 years available, two-window test applied): latest 3-yr revenue CAGR
  (FY23→FY26) = (451.05/670.01)^(1/3)−1 = **-12.4%**; prior 3-yr CAGR (FY20→FY23) =
  (670.01/220.19)^(1/3)−1 = **+44.9%**. Latest is NOT greater than prior, and latest CAGR is
  negative (<20%, <15%) → **0**
- **M12 Negative WC/Float**: WC days FY24-26 all deeply positive (154-244 days, >45 days band) →
  **0**

**Moat tests scoring ≥3 ("present") = 0 of 12.**

**Block F (moat) = 3 / 60. Moat classification: 0 present → NONE**

---
## CLASSIFICATION

**Core score = A(1) + B(1) + C(1) + D(8) + E(11) = 22 / 100**
**Moat score = 3 / 60**
**Grand total = 25 / 160**

Data confidence: 10 years of full P&L/balance sheet/cash flow (FY17-FY26) = "10+ yrs full" tier —
no history downgrade to the headline classification. (Sub-metrics B2/B3/B4 are constrained to a
3-year window as noted; this is a corpus-coverage limitation on those specific tests, not on the
overall 10-year data depth.)

**Deal-breaker check:**
1. Block A < 8 (=1) → caps at GOOD → **triggered**
2. Block B < 8 (=1) → caps at GOOD → **triggered**
3. Median ROCE < 10% → caps at AVERAGE → median is 10.31%, **not triggered** (borderline — 0.31pp
   above the line)
4. Cumulative CFO/PAT < 0.50 → caps at AVERAGE → ratio is 0.543, **not triggered** (borderline —
   0.04 above the line)
5. Pledge > 15% → caps at AVERAGE → pledge data NOT FOUND, **cannot confirm, not counted as
   triggered**
6. ND/EBITDA > 3x (4.19x) AND IC < 3x (0.317x) → **AVOID → triggered**
7. Revenue declined in majority of years (6 of 9) → caps at AVERAGE → **triggered**
8. PAT negative in any of last 3 years (FY26: -5.37 Cr, of FY24-FY26) → caps at AVERAGE →
   **triggered**
9. History < 3 years → AVERAGE → 10 years available, **not triggered**

**Classification matrix**: Core score 22 is <40 → **AVOID** on the base matrix alone, independently
confirmed by deal-breaker #6's direct AVOID override. No downstream-position-sizing override
applies (this is not a documented post-IPO rebase or legacy-cleanup case; the FY26 loss is a
live, segment-identifiable operating deterioration in the Battery/Geon division, not an accounting
one-off).

**FINAL CLASSIFICATION: AVOID**

---
## MOAT PROFILE

```
M1  Pricing Power        [          ] 0
M2  Cost Advantage       [          ] 0
M3  Capital Efficiency   [          ] 0
M4  Customer Stickiness  [          ] 0
M5  Scale & Dominance    [##        ] 1
M6  Technology/R&D       [          ] 0
M7  Regulatory/License   [          ] 0
M8  Distribution         [##        ] 1
M9  Brand                [          ] 0
M10 Switching Costs      [##        ] 1
M11 Network Effects      [          ] 0
M12 Negative WC/Float    [          ] 0
```
Moat class: **NONE** (0 of 12 tests ≥3/5; highest individual score is 1/5)

---
## STRONGEST / WEAKEST BLOCK

**Strongest: Block E, Shareholder Alignment (11/20)** — promoter holding is high (60.49%) and
essentially flat over 3 years (+0.26pp), and contingent liabilities are moderate (5.68% of net
worth). The promoter-pledge gap (E3, NOT FOUND) and the FY26 dividend cut to zero temper this.

**Weakest: Blocks A, B, C, tied at 1/20 each** — return on capital, cash generation, and growth all
collapsed in the same year (FY26) for the same underlying reason: the Battery/Geon segment loss
overwhelmed a still-profitable but shrinking Extrusion Machinery core, while working capital
(inventory in particular) built up sharply over FY24-FY26.

---
## DECISION LINE

**AVOID.** Core score 22/100 is well below the 40-point floor, and deal-breaker #6 (Net
Debt/EBITDA 4.19x with Interest Coverage 0.317x) independently forces AVOID. Zero of 12
quantitative moat tests clear the "present" bar. The FY26 swing to a consolidated loss (PBT -7.78
Cr, PAT -5.37 Cr) traces specifically to the Battery/Geon division (segment loss -43.35 Cr,
widening for the second straight year) rather than to the legacy Extrusion Machinery business
(segment profit +50.75 Cr, declining but still positive). Revenue has declined in 6 of the last 9
years, working capital days rose ~90 days in two years (154→244, FY24→FY26), and CRISIL has
downgraded both the long-term and short-term rating twice since FY24-25. The ~40% market-share
claim central to the bull case is a self-reported, unsourced, single-year assertion not repeated
in the current annual report. Company quality flags propagate; this scorecard does not itself halt
the pipeline (no STOP verdict exists) — but the numbers argue for a REWORK / INSUFFICIENT EVIDENCE
posture pending resolution of the promoter-pledge gap, the CRISIL rationale gap, and clarity on
whether the Battery division loss is a temporary scale-up cost or a structural drag.

---
```yaml
stage: B01-gate0
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results: HIGH - no results filings in corpus; Q1 FY27 (Jun-2026) exists only as screener quarterly numbers"
  - "rating: HIGH - CRISIL detailed rationale report absent; AR FY26 CG report (p.51) discloses the downgrade dates and a one-line trigger ('basis performance reported for Quarter 3') only"
  - "announcements: not in corpus"
  - "shareholding: SEBI shareholding-pattern filing not in corpus; promoter pledge (E3) NOT FOUND as a result"
  - "research: not in corpus"
  - "prospectus: not expected, long-listed company"
  - "presentation-stale: only a Dec-2023 investor deck available"
  - "peer-concall-windsor: not in corpus"
  - "screener-csv-defect: sibling screener-Profit_Loss/Balance_Sheet/Cash_Flow/Quarters CSVs are empty formula shells; only Data_Sheet populated"
  - "sector_cap_row: manifest sector 'Cables / Industrial products' flagged for phase-3 confirmation"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID (Core 22/100, well below 40 floor; deal-breaker 6 also independently forces AVOID: Net Debt/EBITDA 4.19x with Interest Coverage 0.317x). Historical depressor is FY26-specific and segment-identifiable: Battery/Geon division segment loss widened to -43.35 Cr (AR FY26 Note 38, p.105-106/p.160), overwhelming a still-profitable but declining Extrusion Machinery core (+50.75 Cr). Revenue declined in 6 of 9 years; PAT negative in FY26 (of last 3 years); WC days rose 154->244 (FY24->FY26)."
data_years: 10
fy_range: "FY17 to FY26"
blocks: {A: 1, B: 1, C: 1, D: 8, E: 11}
core_score: 22
moat_score: 3
grand_total: 25
moats_confirmed: 0
moat_class: "NONE"
classification: "AVOID"
deal_breakers:
  - "1: Block A score 1/20 (<8) -> caps at GOOD"
  - "2: Block B score 1/20 (<8) -> caps at GOOD"
  - "6: FY26 Net Debt/EBITDA 4.19x (>3x) AND Interest Coverage 0.317x (<3x) -> AVOID"
  - "7: revenue declined in 6 of 9 YoY years (FY18,19,20,24,25,26) -> caps at AVERAGE"
  - "8: PAT negative in FY26 (of last 3 years FY24-26) -> caps at AVERAGE"
history_downgrade: false
data_notes:
  - "profit-to-loss swing, FY25 (PAT +32.20 Cr) to FY26 (PAT -5.37 Cr); no synthetic PAT CAGR attempted (C2/C4 scored 0 per rule)"
  - "ROCE computed as EBIT(PBT+Interest)/(Net Worth+Borrowings), a proxy for Total Assets-Current Liabilities since the screener Data_Sheet does not split current/non-current liabilities; cross-validated against AR FY26 Note 43 disclosed consolidated ROCE (FY26 0.61% vs 0.62% computed; FY25 8.67% vs 8.63% computed)"
  - "ROE computed as PAT/average Net Worth; matches AR FY26 Note 43 consolidated ROE exactly for FY26 (-1.19%) and FY25 (7.04%)"
  - "FCF (B2/B3) computable only for FY24-FY26 because capex breakdown requires AR cash-flow statements, and only Annual_Report_2025.txt and Annual_Report_2026.txt are in this run's corpus; FY17-FY23 capex NOT FOUND (screener's aggregate Investing Activity line conflates capex with investment purchases/sales)"
  - "WC days (B4) computable only for FY24-FY26 because trade payables are NOT FOUND in the corpus for FY17-FY23 (screener balance sheet aggregates payables inside 'Other Liabilities'); latest-vs-earliest comparison is FY26 vs FY24, not FY26 vs FY17"
  - "FY24 AR cash-flow statement shows the 'Expenditure on intangibles' line as a positive (net inflow) figure of Rs 357.21 lakh, unusual versus the outflow convention used every other year; treated at face value, noted as a data quirk"
  - "promoter holding (E1/E2) taken from AR Note 14.4 'Shares held by promoters' Total row (60.49% FY26), not from the Corporate Governance Report's shareholder-category table which splits the same population differently (Promoters 40.51% + Corporate Bodies (Promoter Co) 19.47% + Relatives of promoters 2.70%)"
  - "E2 FY23 promoter % (~60.23%) is derived (FY24 total 60.24% minus FY24 stated change +0.01%, AR FY25 p.89 Note 14.4), not a directly-stated point value"
  - "E3 promoter pledge: NOT FOUND in provided corpus; scored 0, not assumed 0% pledge"
  - "M2/M5/M9 used peer Data_Sheets for RAJOOENG, WINDMACHIN, HBLENGINE (3 comparators); HBLENGINE is a diversified defence-electronics/battery major and a weak segment comparator, noted not excluded"
  - "M6 R&D/Revenue (1.22% FY26) sourced from AR FY26 Annexure-4 (p.28-29), Extrusion Rs 367 lakh + Geon Rs 185.18 lakh; only one year of R&D disclosure available in corpus"
  - "~40% market-share claim (Company Memory priority 1) is self-reported in AR FY25 (p.37) only, unsourced, product-category undefined, and not repeated in AR FY26"
  - "Board recommended Rs 0.00 dividend for FY26 vs Rs 2.50 FY25 (AR FY26 p.110, Note 44), a full dividend cut, not separately scored but relevant context"
block_b_trend: "deteriorating - working capital days rose from ~154 (FY24) to ~244 (FY26), +90 days in two years (screener Data_Sheet Receivables/Inventory/Sales; AR FY26/FY25 Note 34.1 Trade Payables)"
analyst_note: "AVOID is doubly confirmed: Core score (22) sits far below the 40 floor, and deal-breaker 6 (ND/EBITDA 4.19x with IC 0.317x) fires independently. The cause is narrow and traceable, not a broad quality collapse: Segment Note 38 shows the Extrusion Machinery core stayed solidly profitable (+50.75 Cr FY26, down from +70.14 Cr FY25), while the Battery/Geon division's loss widened for a second straight year (-25.53 Cr FY25 to -43.35 Cr FY26) and swamped it. Two scoring lines sat just barrier-side of a deal-breaker: median ROCE 10.31% (0.31pp above the <10% AVERAGE-cap line) and cumulative CFO/PAT 0.543 (0.04 above the <0.50 line) - both would read materially worse if FY26 repeats. The ~40% market-share claim underpinning any bull case is unsourced and was dropped from the current-year report. CRISIL's stated downgrade trigger ('Q3 performance') is thin; no independent rating rationale is in corpus. Promoter pledge is an unresolved data gap, not evidence of cleanliness."
```
