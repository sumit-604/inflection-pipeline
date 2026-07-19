# STAGE 1: GATE 0 SCORECARD — Shyam Metalics & Energy Ltd (SHYAMMETL)
Run date: 2026-07-19 | Model: claude-sonnet-5 | Mode: PIPELINE (no human in loop)

Data available: 9 years (FY18 to FY26). Scoring adapted to 9-year history.

**Sources used**
- screener-Profit_Loss.csv / screener-Balance_Sheet.csv / screener-Cash_Flow.csv / screener-Quarters.csv — all EMPTY (narration headers only, no row data). Not usable.
- screener-Data_Sheet.csv — populated, FY2018-FY2026 annual P&L, Balance Sheet, Cash Flow. Primary source for the 9-year series. Values confirmed consolidated (FY26 Sales 18,552.21 matches audited consolidated revenue exactly).
- screener-Customization.csv — instructional sheet, no data.
- results 518b5092...pdf ("results Q4 FY26") — audited consolidated financial results, balance sheet, cash flow statement for FY26 (year ended 31-Mar-2026) with FY25 audited comparative. Page map used for anchors: p.10 = consolidated P&L, p.11 = consolidated balance sheet, p.12 = consolidated cash flow statement.
- results c8a0eab2...pdf ("results Q3 FY26") — unaudited consolidated/standalone results for 9M ended 31-Dec-2025. No balance sheet or cash flow statement in this filing; used only to corroborate quarter run-rate, not relied on for scorecard anchors.

**Known data source conflict (flagged, not resolved by estimation):** screener-Data_Sheet.csv shows FY25 CFO = ₹1,964.15cr, while the audited FY26 filing's FY25 comparative cash flow statement (results Q4 FY26 p.12) shows FY25 CFO = ₹1,713.43cr. Note (x) to that filing states prior-year figures were "regrouped/reclassified." B1 (cumulative CFO/PAT) uses the Data_Sheet series for full 9-year consistency; FCF calc for FY25-26 (B2/B3) uses the audited CF-statement figures throughout (CFO and Capex from the same statement) for internal consistency.

---

## FORMULA NOTES (methodology declared up front)

- **EBIT** = PBT + Interest (Finance Cost), all years — validated against audited FY25/FY26 actuals (this equals the reported EBITDA line minus Depreciation).
- **EBITDA** = PBT + Interest + Depreciation. Validated: FY26 computed 2,536.75 vs audited reported 2,536.65 (results Q4 FY26 p.10, "Earnings before Interest, Depreciation... and Tax"); FY25 computed 2,096.28 vs audited 2,096.16. Both within rounding.
- **Capital Employed (CE)** for ROCE: formula requires Total Assets − Current Liabilities. Current Liabilities is broken out only for FY26/FY25 in the audited balance sheet (results Q4 FY26 p.11). For FY18-24, screener-Data_Sheet has no current/non-current liability split (only aggregate "Other Liabilities"), so CE is **computed as a proxy: Equity Share Capital + Reserves + Borrowings**, applied consistently across all 9 years for comparability. Cross-check: proxy CE FY26 = ₹12,527.88cr vs actual audited (TA−CL) = ₹12,781.21cr (1.9% variance); proxy FY25 = ₹11,342.76cr vs actual ₹11,711.18cr (3.1% variance). Proxy accepted as reasonable approximation; flagged as data_notes item, not an estimate of the underlying missing figures themselves (the underlying split is NOT FOUND for FY18-24).
- **Receivable/Inventory/Payable Days**: Revenue basis (COGS not separately disclosed as a clean line in Data_Sheet). Trade Payables are NOT FOUND for FY18-24 (no separate line in Data_Sheet Balance Sheet section, and not disclosed in the results PDFs for those years) — only available for FY25/FY26 from the audited balance sheet. This blocks WC Days trend (B4) and the negative-WC test (M12) for the required "latest vs earliest" / "majority of years" comparisons.
- **Capex** (purchase of PPE + intangibles from CF statement) is NOT FOUND in screener-Data_Sheet (only aggregate "Cash from Investing Activity" is given, which bundles capex with financial investment purchases/sales — not separable). Capex is only available for FY26 (₹2,637.24cr) and FY25 (₹2,148.32cr) from the audited consolidated cash flow statement (results Q4 FY26 p.12). FCF-based metrics (B2, B3) are therefore assessed on 2 of 9 years only; flagged.

---

## [BLOCK A: RETURN ON CAPITAL] — Score: 4 / 20

| Year | EBIT (PBT+Interest) | CE (proxy: Equity+Reserves+Borrow) | ROCE | PAT | Avg Net Worth | ROE |
|---|---|---|---|---|---|---|
| FY18 | 566.24 | 2,421.51 | 23.38% | 424.37 | 1,853.99 (closing only, no FY17 opening) | 22.89% |
| FY19 | 828.32 | 3,218.30 | 25.74% | 604.13 | 2,171.83 | 27.82% |
| FY20 | 381.26 | 3,940.79 | 9.67% | 340.24 | 2,658.06 | 12.80% |
| FY21 | 1,117.40 | 4,430.01 | 25.22% | 843.34 | 3,230.24 | 26.11% |
| FY22 | 2,387.49 | 6,377.71 | 37.44% | 1,724.54 | 4,734.35 | 36.43% |
| FY23 | 1,130.08 | 8,447.66 | 13.38% | 852.68 | 6,555.32 | 13.01% |
| FY24 | 1,073.08 | 10,243.58 | 10.48% | 1,034.79 | 8,461.32 | 12.23% |
| FY25 | 1,385.11 | 11,342.76 | 12.21% | 908.10 | 10,100.00 | 8.99% |
| FY26 | 1,654.60 | 12,527.88 | 13.21% | 1,070.24 | 11,038.07 | 9.70% |

(all raw inputs: screener-Data_Sheet.csv rows: Sales, PBT, Tax, Interest, Net profit, Equity Share Capital, Reserves, Borrowings; FY26 EBIT/PBT/Interest also cross-checked to results Q4 FY26 p.10)

- **A1 Median ROCE** = 13.38% (sorted: 9.67, 10.48, 12.21, 13.21, 13.38, 23.38, 25.22, 25.74, 37.44 → median = 13.38%). Band 10-14.9% = **1**
- **A2 Minimum single-year ROCE** = 9.67% (FY20). Band 8-11.9% = **1**
- **A3 Median ROE** = 13.01% (sorted: 8.99, 9.70, 12.23, 12.80, 13.01, 22.89, 26.11, 27.82, 36.43 → median = 13.01%). Band 12-14.9% = **2**
- **A4 ROCE trend, latest vs earliest** = FY26 13.21% vs FY18 23.38% = decline of 10.17pp. Decline >5pp = **0**

**Block A = 1+1+2+0 = 4/20.** Deal-breaker #1 triggered (Block A <8 → max GOOD).

---

## [BLOCK B: CASH GENERATION QUALITY] — Score: 5 / 20

CFO by year (screener-Data_Sheet.csv, Cash from Operating Activity row): FY18 246.95, FY19 456.56, FY20 −91.00, FY21 1,056.17, FY22 1,561.20, FY23 1,518.33, FY24 1,794.38, FY25 1,964.15, FY26 2,023.56. Cumulative CFO = ₹10,530.30cr.
Cumulative PAT (same source, Net profit row) = ₹7,802.43cr.

- **B1 Cumulative CFO ÷ Cumulative PAT** = 10,530.30 / 7,802.43 = **1.35**. ≥1.00 = **5**
- **B2 FCF-positive years as proportion**: Capex NOT FOUND for FY18-24 (screener-Data_Sheet has no separate capex line; only bundled CFI). Assessable only for FY25 and FY26 using audited CF statement (results Q4 FY26 p.12): FY26 FCF = CFO 2,023.56 − Capex 2,637.24 = **−613.68**; FY25 FCF = CFO 1,713.43 (audited) − Capex 2,148.32 = **−434.89**. 0 of 2 assessable years FCF-positive (0%). <50% = **0**. *Flagged: only 2 of 9 years assessable; FY18-24 Capex NOT FOUND (not in provided data).*
- **B3 Cumulative FCF ÷ Cumulative PAT**: only computable for the same 2 years (not a true 9-year cumulative). FY25+FY26 FCF = −1,048.57; FY25+FY26 PAT = 1,978.34. Ratio = **−0.53** (partial-period, not the intended full-history metric). Negative → **0**. *Flagged: not a valid full-period cumulative given the Capex data gap; presented for transparency only.*
- **B4 Change in WC Days, latest vs earliest**: Trade Payables NOT FOUND for FY18 (screener-Data_Sheet Balance Sheet section has no Trade Payables line; only available for FY25/FY26 from the audited balance sheet). Cannot compute Payable Days for the earliest year, so latest-vs-earliest WC Days change cannot be calculated. **N/A (not in provided data) = 0**.

**Block B = 5+0+0+0 = 5/20.** Deal-breaker #2 triggered (Block B <8 → max GOOD).

**block_b_trend: deteriorating** — the one number: FCF swung from −₹434.89cr (FY25) to −₹613.68cr (FY26); Capex (₹2,637.24cr, +22.8% YoY) is outrunning CFO (₹2,023.56cr, +18.1% YoY) (results Q4 FY26 p.12). Company approved fresh capex programs of ₹6,660cr (Jan-2026 board meeting) and a further ₹2,700cr (May-2026 board meeting) during/just after this window, so the capex-heavy phase is ongoing, not a one-off.

---

## [BLOCK C: GROWTH] — Score: 11 / 20

Revenue (screener-Data_Sheet.csv, Sales row): FY18 3,747.16 → FY26 18,552.21 (8-year span).
PAT (Net profit row): FY18 424.37 → FY26 1,070.24.

- **C1 Revenue CAGR** = (18,552.21/3,747.16)^(1/8) − 1 = **22.12%**. ≥20% = **5**
- **C2 PAT CAGR** = (1,070.24/424.37)^(1/8) − 1 = **12.26%** (both endpoints positive, no N/M). Band 10-14.9% = **3**
- **C3 Positive YoY revenue years**: 8 YoY comparisons (FY19-FY26 vs prior year). Only FY20 declined (4,376.35 vs FY19's 4,606.40); all other 7 years grew. 7/8 = 87.5%. Band 75-99% = **3**
- **C4 PAT CAGR − Revenue CAGR** = 12.26% − 22.12% = **−9.86pp**. <−8pp = **0**

**Block C = 5+3+3+0 = 11/20.**

---

## [BLOCK D: BALANCE SHEET STRENGTH] — Score: 14 / 20 (latest = FY26, audited, results Q4 FY26 p.11-12)

- **D1 Net Debt ÷ EBITDA**: Total Borrowings (non-current 97.04 + current 884.28) = ₹981.32cr; Cash & cash equivalents 904.59 + other bank balances 97.12 = ₹1,001.71cr. Net Debt = 981.32 − 1,001.71 = **−₹20.39cr (net cash)**. Net cash = **5**
- **D2 Interest Coverage** = EBIT (PBT 1,462.37 + Interest 192.23 = 1,654.60) ÷ Interest 192.23 = **8.61x**. Band 5-9.9x = **4**
- **D3 Debt ÷ Equity** = Total Borrowings 981.32 ÷ Total Equity (owners) 11,522.81 = **0.085x**. <0.1 = **5**
- **D4 Current Ratio** = Total Current Assets 7,255.90 ÷ Total Current Liabilities 7,279.63 = **0.997x**. <1.0 = **0**

**Block D = 5+4+5+0 = 14/20.**

---

## [BLOCK E: SHAREHOLDER ALIGNMENT] — Score: 0 / 20 — DATA GAP, not a quality signal

- **E1 Promoter holding (latest quarter)**: NOT FOUND — shareholding pattern data ABSENT from provided inputs (carried B00 input gap). Score **0**
- **E2 Promoter holding change, 3yr**: NOT FOUND, same gap. Score **0**
- **E3 Promoter pledge (latest)**: NOT FOUND, same gap. Score **0**
- **E4 Contingent liabilities ÷ Net Worth**: NOT FOUND — no contingent liability note visible in the two results PDFs provided (this disclosure typically sits in the Annual Report notes, not in quarterly/annual results filings). Score **0**

**Block E = 0/20. This is entirely a data-availability gap** (shareholding ABSENT was already flagged at B00), **not evidence of poor alignment**. It mechanically drags Core Score down by 20 points per the scoring rules ("never estimate a missing number"), and materially affects the classification outcome below — flagged prominently.

---

## [BLOCK F: QUANTITATIVE MOAT SCORING] — Total: 7 / 60

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | 0 | EBITDA margin FY18 20.85% → FY26 13.67% (screener-Data_Sheet, PBT+Interest+Dep/Sales), decline of 7.18pp despite revenue CAGR 22.12% ≥10%. Decline >5pp falls outside all scoring bands ("else") = 0 |
| M2 Cost Advantage vs peer | 0 | PEER DATA NEEDED — peer CSVs explicitly excluded from Gate 0 scope per task instructions |
| M3 Capital Efficiency | 1 | FAT = Sales 18,552.21 / PPE 7,968.68 (audited BS, results Q4 FY26 p.11) = 2.33x (>2x); ROCE FY26 = 13.21%/12.95% (proxy/audited CE), not >15%. Falls to "FAT>1x AND ROCE>12%" = 1 |
| M4 Customer Stickiness | 3 | 1 revenue-decline year (FY20); FY21 revenue (6,297.07) recovered well above prior peak FY19 (4,606.40) — fully recovered. "Max 1 decline year, fully recovered" = 3 |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED (mcap/margin ranking vs segment peers not in scope) |
| M6 Technology/R&D | 0 | R&D/Revenue NOT FOUND (not disclosed in provided data; steel/ferro-alloys manufacturer, no R&D line in screener export) |
| M7 Regulatory/License | 0 | Steel/ferro-alloys/stainless manufacturing — unregulated entry (many listed players), not a licensed-scarcity segment = 0 |
| M8 Distribution | 0 | Distribution reach data NOT FOUND in provided data |
| M9 Brand | 0 | PEER DATA NEEDED for peer gross-margin comparison (GM proxy = (Revenue−Material Cost)/Revenue computable for the company itself but scoring requires peer median, unavailable) |
| M10 Switching Costs | 3 | Revenue grew all years but 1 (FY20); Receivable Days improved from 35.91 (FY18: 368.72/3,747.16×365) to 17.80 (FY26: 904.59/18,552.21×365) — stable/declining. "Growth all but 1 year AND stable" = 3 |
| M11 Network Effects | 0 | 9-year history supports the two-window test. Latest 3yr revenue CAGR (FY23→FY26) = (18,552.21/12,658.07)^(1/3)−1 = 13.59%; prior 3yr CAGR (FY20→FY23) = (12,658.07/4,376.35)^(1/3)−1 = 42.49%. Latest CAGR is lower, not higher, and does not clear the ≥20% alternate band either = 0 |
| M12 Negative WC/Float | 0 | Trade Payables NOT FOUND for FY18-24 (7 of 9 years); WC Days computable only for FY25 (20.86 days: Receivable 19.11 + Inventory 72.09 − Payable 70.34) and FY26 (10.62 days: 17.80 + 88.57 − 95.75), both from partial data. "Consistently" cannot be established across the required majority of years = 0 |

**Moat score = 0+0+1+3+0+0+0+0+0+3+0+0 = 7/60**
**Moats "present" (score ≥3): M4, M10 → moats_confirmed = 2**
**Moat classification: 2-3 present = MODERATE**

---

## DASHBOARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 4 | 20 |
| B — Cash Generation Quality | 5 | 20 |
| C — Growth | 11 | 20 |
| D — Balance Sheet Strength | 14 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **Core Score** | **34** | **100** |
| F — Quantitative Moat | 7 | 60 |
| **Grand Total** | **41** | **160** |

Moat profile: [M1□ M2□ M3▪ M4■ M5□ M6□ M7□ M8□ M9□ M10■ M11□ M12□] — 2 of 12 present (■), MODERATE

**Strongest block: D (Balance Sheet Strength, 14/20)** — net cash, negligible leverage, strong interest cover; only the current ratio (0.997x) is sub-1.0, a working-capital funding-mix point worth watching given the concurrent heavy capex program.

**Weakest block: E (Shareholder Alignment, 0/20)** — entirely a data-availability gap (shareholding pattern and contingent liabilities not in provided inputs), not a demonstrated alignment problem. Block A (4/20) is the weakest block on genuine evidence: ROCE has compounded down from 23.4% (FY18) to 13.2% (FY26), median ROCE of 13.4% sits in the bottom third of bands, and EBITDA margin has compressed 7.2pp over the period despite strong top-line growth — consistent with a capital-intensive, cyclically-diluted return profile as the asset base has scaled ~5x (Capital Employed proxy ₹2,422cr → ₹12,528cr, FY18→FY26).

---

## DATA CONFIDENCE

9 years of annual history (FY18-FY26) → band "7-9 = moderate." No history-based downgrade applies (downgrade only triggers at 3-4 years; "may not have seen full cycle" flag only at 5-6 years). The 9-year window does span both a trough (FY20, COVID) and a peak (FY22), so cycle coverage is reasonable within the moderate-confidence band. **history_downgrade = false.**

---

## DEAL-BREAKER CHECK

| # | Rule | Result | Triggered? |
|---|---|---|---|
| 1 | Block A <8 → max GOOD | Block A = 4 | **Yes** |
| 2 | Block B <8 → max GOOD | Block B = 5 | **Yes** |
| 3 | Median ROCE <10% → max AVERAGE | 13.38% | No |
| 4 | Cumul CFO/PAT <0.50 → max AVERAGE | 1.35 | No |
| 5 | Pledge >15% → max AVERAGE | NOT FOUND (shareholding absent) — cannot evaluate | Cannot evaluate |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | Net cash position; IC 8.61x | No |
| 7 | Revenue declined majority of years → max AVERAGE | 1 of 8 YoY comparisons declined (12.5%) | No |
| 8 | PAT negative in any of last 3 years → max AVERAGE | FY24 1,034.79 / FY25 908.10 / FY26 1,070.24, all positive | No |
| 9 | History <3 years → AVERAGE | 9 years | No |

Deal-breakers #1 and #2 cap the classification at max GOOD. This is superseded by a lower outcome from the classification matrix itself (below).

---

## CLASSIFICATION

Classification matrix: Core Score = 34 → **Core <40 = AVOID** (this band applies irrespective of moat class per the matrix as written).

**Classification: AVOID**

**Material caveat for the downstream synthesis stage:** this AVOID is driven in material part by Block E scoring 0/20 purely because shareholding-pattern and contingent-liability data were not in the provided inputs (input_gaps carried from B00: shareholding ABSENT). Had Block E been assessable and scored even moderately (e.g., a typical "professionally managed, FII+DII >50%" score of 3/20 on E1 alone plus average scores elsewhere), Core Score would sit materially higher, plausibly clearing the 40 threshold into AVERAGE territory. Genuine, non-data-gap depressors independently identified: declining ROCE trend (23.4%→13.2%, FY18-26), EBITDA margin compression (20.85%→13.67%), sub-1.0x current ratio, and negative/worsening FCF against an active heavy-capex program (₹6,660cr + ₹2,700cr newly approved). These are real mechanical findings and would likely have capped classification at GOOD even with full data (deal-breakers #1/#2), but AVOID specifically should be re-tested once shareholding data is available in a later stage.

**Decision line:** SHYAMMETL screens AVOID on Gate 0 mechanics, driven jointly by weak Block A/B scores (genuine: capital-intensive returns compounding down, cash conversion adequate on a cumulative multi-year basis but FCF negative in both audited years assessable) and a complete Block E data gap (shareholding/contingent liabilities not in provided inputs — mechanical, not qualitative). Flag propagates; verdict decision remains with the operator per pipeline rules — no STOP, no company-quality halt.

---
