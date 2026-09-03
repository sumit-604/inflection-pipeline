# STAGE 1: GATE 0 SCORECARD — MPS Ltd (MPSLTD)
Run date: 2026-09-03 | Data sources: screener.in CSV set (screener-Data_Sheet.csv is the only
populated CSV; Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/Customization CSVs were exported
as blank templates with no numeric rows) + audited FY26/Q4 results PDF + unaudited Q1 FY27
results PDF.

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

**Sector note:** Financials show a content/platform/education services business (Research
solutions, Education solutions, Corporate learning segments per results PDFs), not pharma.
No raw material cost line, no inventory, asset-light. Scored as a general (non-bank,
non-financial) company.

---

## DATA SOURCE CAVEAT (read before scores)

The screener CSV export for this ticker has all numeric data consolidated into
`screener-Data_Sheet.csv`; the separate `Profit_Loss.csv`, `Balance_Sheet.csv`,
`Cash_Flow.csv`, and `Quarters.csv` files contain only column headers with zero data rows.
All screener-sourced figures below are anchored to `screener-Data_Sheet.csv` by fiscal year
(rows are P&L, Balance Sheet, Cash Flow, and Quarters blocks within that single file).
Cross-checked against the FY26 and Q1 FY27 results PDFs where both exist (figures reconcile:
consolidated FY26 Sales 768.36 cr = INR 76,837 lacs and PAT 173.22 cr = INR 17,322 lacs per
Results Q1 FY27 PDF, consolidated P&L, p.9, "Previous year ended" column). The screener
export figures are CONSOLIDATED, confirmed by this reconciliation.

Three data items required by the fixed formulas are **absent from every provided source**:
- Trade Payables (all 10 years) — blocks Payable Days, so full Working Capital Days (B4, M12)
  cannot be computed per the fixed formula.
- Itemized Capex / purchase of PP&E+intangibles (all 10 years in the screener export) —
  screener-Cash_Flow.csv gives only the blank template; screener-Data_Sheet.csv gives the
  aggregate "Cash from Investing Activity" line, which is not a valid capex proxy (it nets
  investment purchases/sales, loans to subsidiaries, and dividend income). Blocks FCF (B2, B3).
- Shareholding pattern (promoter holding, pledge) and contingent liabilities — not present in
  any screener CSV or in either results PDF (these filings were not supplied to this stage).
  Blocks all of Block E.

These are named per-metric below as "N/A (not in provided data)" and scored 0, per rule 5.
They are NOT estimated.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE is not populated in the provided screener export (screener-Balance_Sheet.csv template
is blank; screener-Data_Sheet.csv has no ROCE/ROE row). Computed per formula, methodology
noted: Capital Employed = Net Worth (Equity Share Capital + Reserves) + Borrowings, since
the compressed "Other Liabilities" bucket in screener-Data_Sheet.csv aggregates current and
non-current items and cannot be split into a true Current Liabilities figure. State: "computed."

| FY | EBIT (PBT+Interest, cr) | Capital Employed (cr) | ROCE % | Net Worth avg (cr) | PAT (cr) | ROE % |
|---|---|---|---|---|---|---|
| 2017 | 102.72 | 347.90 | 29.53 | 347.90 (closing only, no FY16 opening) | 70.42 | 20.24 |
| 2018 | 101.99 | 418.68 | 24.36 | 383.29 | 70.21 | 18.32 |
| 2019 | 107.54 | 471.16 | 22.83 | 444.92 | 76.04 | 17.09 |
| 2020 | 83.57 | 385.75 | 21.67 | 419.04 | 59.86 | 14.29 |
| 2021 | 95.43 | 399.47 | 23.89 | 374.02 | 58.56 | 15.66 |
| 2022 | 119.49 | 378.86 | 31.55 | 374.00 | 87.12 | 23.30 |
| 2023 | 148.04 | 431.28 | 34.32 | 395.30 | 109.19 | 27.62 |
| 2024 | 162.12 | 464.36 | 34.91 | 441.77 | 118.77 | 26.89 |
| 2025 | 201.91 | 482.13 | 41.88 | 469.13 | 148.91 | 31.74 |
| 2026 | 231.30 | 656.96 | 35.21 | 537.39 | 173.22 | 32.23 |

(all inputs: screener-Data_Sheet.csv, P&L rows PBT/Interest/Net profit and Balance Sheet rows
Equity Share Capital/Reserves/Borrowings, by fiscal year column)

**A1 Median ROCE:** sorted values give median = avg(29.53, 31.55) = **30.54%** → ≥25% → **Score 5**
**A2 Minimum single-year ROCE:** FY2020 = **21.67%** → ≥15% → **Score 5**
**A3 Median ROE:** sorted values give median = avg(20.24, 23.30) = **21.77%** → ≥20% → **Score 5**
**A4 ROCE trend, latest vs earliest:** FY2026 35.21% ≥ FY2017 29.53% → **Score 5**

**BLOCK A TOTAL: 20/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (screener-Data_Sheet.csv, Cash Flow rows FY17-26) = 971.43 cr
Cumulative PAT (screener-Data_Sheet.csv, P&L Net profit rows FY17-26) = 972.30 cr

**B1 Cumulative CFO ÷ Cumulative PAT** = 971.43 / 972.30 = **0.999** → 0.85-0.99 band → **Score 4**

**B2 FCF-positive years proportion:** N/A (not in provided data) — capex not itemized in any
provided source across the 10-year window (see Data Source Caveat). **Score 0.**

**B3 Cumulative FCF ÷ Cumulative PAT:** N/A (not in provided data), same capex gap. **Score 0.**

**B4 Change in WC Days, latest vs earliest:** N/A (not in provided data) — Trade Payables
absent from every provided source, so Payable Days (and therefore full WC Days per the fixed
formula) cannot be computed. Inventory = 0 in all 10 years (screener-Data_Sheet.csv,
Inventory row genuinely blank — a services business with no inventory, not a data gap).
Receivable Days alone (for context, not scored): 75.98(FY17), 63.08, 69.19, 68.53, 78.21,
69.68, 63.09, 68.88, 58.54, 63.42(FY26) — relatively stable 58-78 day band across the period
(screener-Data_Sheet.csv, Receivables ÷ Sales × 365). **Score 0.**

**BLOCK B TOTAL: 4/20**

---

## BLOCK C: GROWTH (Max 20)

Revenue (cr): 288.70(FY17) → 768.36(FY26). PAT (cr): 70.42(FY17) → 173.22(FY26).
(screener-Data_Sheet.csv, Sales and Net profit rows)

**C1 Revenue CAGR (9-yr):** (768.36/288.70)^(1/9)-1 = **11.49%** → 10-14.9% band → **Score 3**

**C2 PAT CAGR (9-yr):** (173.22/70.42)^(1/9)-1 = **10.52%** → 10-14.9% band → **Score 3**

**C3 Positive YoY revenue years:** 9 YoY comparisons FY18-FY26; declines in FY18 (267.03 vs
288.70) and FY20 (331.65 vs 362.54); 7 of 9 positive = **77.8%** → 75-99% band → **Score 3**

**C4 PAT CAGR minus Revenue CAGR:** 10.52% − 11.49% = **−0.97pp** → within ±3pp → **Score 3**

**BLOCK C TOTAL: 12/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Latest year FY2026, consolidated (screener-Data_Sheet.csv) unless noted:
Borrowings 60.63 cr, Cash & Bank 94.55 cr, Net Worth 596.33 cr, EBITDA (Operating Profit,
Sales−Expenses excl. D&A/interest/other income) 235.84 cr, EBIT 231.30 cr, Interest 2.01 cr.

**D1 Net Debt ÷ EBITDA:** Net Debt = 60.63 − 94.55 = **−33.92 cr (net cash)** → **Score 5**

**D2 Interest Coverage (EBIT ÷ Interest):** 231.30 / 2.01 = **115.1x** → ≥10x → **Score 5**

**D3 Debt ÷ Equity:** 60.63 / 596.33 = **0.102** → 0.1-0.5 band → **Score 4**

**D4 Current Ratio:** Consolidated current asset/liability split is not in the screener
export. Computed on STANDALONE FY26 balance sheet instead (Results Q4 FY26 PDF, Annexure A,
p.2): Total current assets 19,305 lacs ÷ Total current liabilities 7,645 lacs = **2.525x**
→ ≥2.0 → **Score 5**. Basis note: this one line item is standalone while D1-D3 are
consolidated; flagged as a limitation, not treated as a data gap since a real number exists.

**BLOCK D TOTAL: 19/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding (latest quarter):** N/A (not in provided data) — no shareholding
pattern file supplied. **Score 0.**
**E2 Promoter holding change over 3 years:** N/A (not in provided data). **Score 0.**
**E3 Promoter pledge (latest):** N/A (not in provided data). **Score 0.**
**E4 Contingent liabilities ÷ Net Worth (latest):** N/A (not in provided data) — no AR/notes
with contingent liability disclosure supplied to this stage. **Score 0.**

**BLOCK E TOTAL: 0/20** (entirely a data-availability gap, not a scored finding of misalignment)

---

## CORE SCORE

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 20 | 20 |
| B — Cash Generation Quality | 4 | 20 |
| C — Growth | 12 | 20 |
| D — Balance Sheet Strength | 19 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **CORE TOTAL** | **55** | **100** |

Strongest block: A (Return on Capital), 20/20.
Weakest block: E (Shareholder Alignment), 0/20 — entirely unscored for lack of data, not a
finding of weak alignment.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin by year (Operating Profit = Sales − Power&Fuel − Other Mfr Exp − Employee Cost
− Selling&admin − Other Expenses, ÷ Sales; screener-Data_Sheet.csv P&L rows):
FY17 32.35%, FY18 32.60%, FY19 25.80%, FY20 23.85%, FY21 25.31%, FY22 28.13%, FY23 31.29%,
FY24 31.15%, FY25 29.01%, FY26 30.69%.

**M1 Pricing Power:** margin change FY17→FY26 = 30.69−32.35 = −1.66pp (stable, within ±2pp)
AND revenue CAGR 11.49% ≥10% → **Score 3**

**M2 Cost Advantage vs peer:** PEER DATA NEEDED (no peer EBITDA margin provided). **Score 0.**

**M3 Capital Efficiency:** FAT (FY26) = Sales 768.36 / Net Block 539.65 = 1.42x; ROCE FY26
35.21%. FAT>1x AND ROCE>12% → **Score 1** (does not clear FAT>2x or FAT>3x tiers; note Net
Block jumped FY25→FY26, 342.85→539.65, on the Unbound Medicine acquisition, screener-Data_Sheet.csv
and Results Q1 FY27 PDF Annexure 1 subsidiary list, p.7)

**M4 Customer Stickiness:** 2 revenue-decline years (FY18, FY20) against an overall positive
revenue CAGR → **Score 1**

**M5 Scale & Dominance:** PEER DATA NEEDED (no peer mcap/margin ranking provided). **Score 0.**

**M6 Technology/R&D:** N/A (not in provided data) — no R&D expense line item in the P&L.
**Score 0.**

**M7 Regulatory/License:** Business is unregulated content/platform/education services, no
license-cap evidence in provided data → **Score 0.**

**M8 Distribution:** N/A (not in provided data) — no reach/outlet metric disclosed; business
is platform/digital-delivery per segment description. **Score 0.**

**M9 Brand:** N/A — no Raw Material Cost line (screener-Data_Sheet.csv row blank, consistent
with a services business), so the gross-margin proxy cannot be built, and no peer gross
margin is provided regardless. **Score 0.**

**M10 Switching Costs:** overall revenue growth with 2 decline years (FY18, FY20) → **Score 1**

**M11 Network Effects (10 years available, two-window test valid):** latest 3yr revenue CAGR
(FY23→FY26) = (768.36/501.05)^(1/3)-1 = 15.31%; prior 3yr CAGR (FY20→FY23) =
(501.05/331.65)^(1/3)-1 = 14.74%. Latest > prior, but Selling & admin expense as % of sales
rose in the latest year: FY23 6.81%, FY24 6.19%, FY25 6.15%, FY26 7.71% (screener-Data_Sheet.csv,
Selling and admin row ÷ Sales). Latest-3yr CAGR 15.31% >15% but selling % rising in FY26 →
**Score 1**

**M12 Negative WC/Float:** N/A (not in provided data) — Trade Payables absent from every
provided source, WC Days cannot be computed (same gap as B4). **Score 0.**

| Moat test | Score |
|---|---|
| M1 Pricing Power | 3 |
| M2 Cost Advantage | 0 (PEER DATA NEEDED) |
| M3 Capital Efficiency | 1 |
| M4 Customer Stickiness | 1 |
| M5 Scale & Dominance | 0 (PEER DATA NEEDED) |
| M6 Technology/R&D | 0 (N/A) |
| M7 Regulatory/License | 0 |
| M8 Distribution | 0 (N/A) |
| M9 Brand | 0 (N/A) |
| M10 Switching Costs | 1 |
| M11 Network Effects | 1 |
| M12 Negative WC/Float | 0 (N/A) |
| **TOTAL** | **7/60** |

Moats present (score ≥3): **M1 only → 1 moat confirmed**
**Moat classification: 1 present → THIN**

Moat profile bar (present tests marked X):
```
M1 [XXX..]  M2 [.....]  M3 [X....]  M4 [X....]  M5 [.....]  M6 [.....]
M7 [.....]  M8 [.....]  M9 [.....]  M10 [X....]  M11 [X....]  M12 [.....]
```

---

## CLASSIFICATION

Data confidence: 10 years available → **full confidence**, no history-based downgrade.

Grand Total = Core (55) + Moat (7) = **62 / 160**

Classification matrix: Core 55 falls in the 40-59 band → **AVERAGE** (independent of moat
class, which was THIN anyway).

**Deal-breaker overrides checked:**
1. Block A <8 → max GOOD: Block A = 20, not triggered.
2. Block B <8 → max GOOD: **Block B = 4, TRIGGERED.** Cap has no net effect since matrix
   result (AVERAGE) already sits below the GOOD cap.
3. Median ROCE <10% → max AVERAGE: median ROCE 30.54%, not triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: 0.999, not triggered.
5. Pledge >15% → max AVERAGE: pledge data N/A, cannot assess (not triggered, not clearable
   either — flagged as an open item for Halt 1).
6. ND/EBITDA >3x AND IC <3x → AVOID: net cash position, not triggered.
7. Revenue declined in majority of years → max AVERAGE: 2 of 9 years declined (22%), not a
   majority, not triggered.
8. PAT negative in any of last 3 years → max AVERAGE: FY24/25/26 PAT all positive
   (118.77/148.91/173.22 cr), not triggered.
9. History <3 years → AVERAGE: 10 years available, not triggered.

**Which years drive the deal-breaker:** Deal-breaker #2 (Block B<8) is driven by 3 of 4
sub-metrics (B2, B3, B4) scoring 0 for missing capex/payables data across the full FY17-26
window, not by a poor B1 cash-conversion ratio (B1 = 0.999, essentially 1:1 cash conversion,
scored 4/5). This is a data-completeness artifact, not a demonstrated cash-quality weakness.

**FINAL CLASSIFICATION: AVERAGE**

---

## FACTUAL NOTES TIED TO SPEAR PRIORITIES (not scored, per pipeline rule against
qualitative judgment — reported as line-item facts only)

- **AJE (American Journal Experts) restructuring:** Consolidated FY26 results disclose
  exceptional items: "Restructuring of American Journal Experts (AJE) business amounting to
  INR 63 lacs [Q1 FY26], INR 66 lacs [FY26] and INR 209 lacs [FY25]" and a separate
  write-back of "INR 1,395 lacs...advances from customer in AJE Business to align policy with
  market conditions/competition and pursuant to change in commercial terms with customers"
  (Results Q1 FY27 PDF, consolidated notes 5(a) and 5(d), p.10). This is consistent with the
  SPEAR flag on AJE revenue pruning; the screener export does not break out AJE revenue by
  currency (USD 18M→12M is not a figure present in any provided source here — NOT FOUND in
  screener/results data, would need transcript-level ferry).
- **Platform vs content segment margins:** Consolidated FY26 segment margins (Results Q1
  FY27 PDF, consolidated segment note, p.9): Research solutions revenue 46,351 lacs / result
  17,024 lacs = 36.7% margin; Education solutions revenue 20,890 lacs / result 7,721 lacs =
  37.0% margin; Corporate learning revenue 9,596 lacs / result 1,131 lacs = 11.8% margin.
  Q1 FY27 (quarter ended 30-Jun-2026): Research 41.5%, Education 31.0%, Corporate learning
  18.5% (same PDF, p.9). Corporate learning is the newest and lowest-margin segment
  (added via the Liberate Group acquisition completed in the quarter per note 5(c), p.10) and
  is a drag on group blended margin relative to the two legacy content segments.

---

## input_gaps summary (for downstream stages / Halt 1 dossier)

1. Shareholding pattern (promoter %, pledge %) — not supplied to this stage, blocks all of
   Block E.
2. Contingent liabilities (Net Worth ratio) — not supplied, blocks E4.
3. Trade Payables, all 10 years — blocks B4 and M12 (WC Days).
4. Itemized Capex (PP&E + intangibles purchases), all 10 years — blocks B2 and B3 (FCF).
5. Peer EBITDA margin, peer market-cap ranking, peer gross margin — blocks M2, M5, M9.
6. R&D expense line item, distribution-reach metric — blocks M6, M8.
7. AJE segment USD revenue figures (18M→12M pruning cited in SPEAR) — not present in
   screener/results data; NOT FOUND, needs transcript-level verification.

---
