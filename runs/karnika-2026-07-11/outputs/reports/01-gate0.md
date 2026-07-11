# STAGE 1: GATE 0 SCORECARD — Karnika Industries Ltd (KARNIKA)
Run date: 2026-07-11 | Model: claude-sonnet-5 | Mode: pipeline (full run, no prior run/company memory)

Data available: **2 years (FY25 to FY26)**. Scoring adapted to 2-year history.

## DATA AVAILABILITY NOTE (read before the numbers)

The dedicated screener multi-year exports for the subject company —
`screener-Profit_Loss.csv`, `screener-Balance_Sheet.csv`,
`screener-Cash_Flow.csv`, `screener-Quarters.csv` — contain **no populated
data cells**, only row labels (verified by direct read and grep). This is
a data gap, not a zero. All annual figures below are instead sourced from:
1. `screener-Data_Sheet.csv` — CONSOLIDATED, FY26 only (single year) + 3
   quarters (Dec-25, Mar-26, Jun-26), in ₹ Crores. Cross-checked line by
   line against the audited PDFs below; reconciles exactly (e.g. Sales
   248.48 Cr = Consolidated Revenue from Operations + Other Income FY26).
2. `KARNIKA_16052026231140_..._MARCH_-26.pdf` (16 pages, audited) —
   **Standalone** P&L, Balance Sheet and Cash Flow for FY26 **with FY25
   comparatives**, and Consolidated statements for FY26 only (first
   consolidation year, no FY25 consolidated comparative — company note:
   "Comparative consolidated information for the year 2024-25 has not
   been presented, as the requirement for consolidation was not
   applicable in the previous period").
3. `KARNIKA_04072026203308_..._June_2026.pdf` (11 pages, unaudited) — Q1
   FY27 standalone + consolidated P&L only (no balance sheet/cash flow
   in a quarterly filing); used for context, not for annual scoring.

Because only STANDALONE has a genuine 2-year comparative (FY25 vs FY26),
**this scorecard runs on standalone financials** throughout Blocks A-D
and the moat tests, not the screener's consolidated Data_Sheet, so that
every ratio is computed on a like-for-like 2-point series. This is
flagged explicitly wherever it matters.

**No shareholding pattern, promoter holding, pledge, or contingent
liability data appears anywhere in the provided inputs.** Block E is
scored 0/20 throughout on that basis (N/A, not estimated).

Formula basis used consistently across all blocks (stated once, applied
everywhere): **EBIT = PBT + Interest − Other Income**; **EBITDA = EBIT +
Depreciation**. Other Income is excluded as non-operating — the
standalone cash flow statement's indirect-method adjustments show it is
composed of profit on sale of shares/mutual funds, interest received and
dividend income, i.e. investment income, not operating income (results
Mar-26 PDF, Standalone CF p.7).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

| Item | FY25 | FY26 | Source |
|---|---|---|---|
| PBT | 2,417.11 | 3,659.15 | results Mar-26 PDF, Standalone P&L p.6, Year Ended columns |
| Interest | 446.38 | 538.16 | results Mar-26 PDF, Standalone P&L p.6 |
| Other Income | 373.12 | 868.12 | results Mar-26 PDF, Standalone P&L p.6 |
| Depreciation | 112.87 | 163.49 | results Mar-26 PDF, Standalone P&L p.6 |
| EBIT (computed) | 2,490.37 | 3,329.19 | computed: PBT+Interest−OtherIncome |
| Total Assets | 15,436.31 | 18,901.85 | results Mar-26 PDF, Standalone BS p.5 |
| Current Liabilities | 8,209.02 | 9,290.78 | results Mar-26 PDF, Standalone BS p.5 |
| Capital Employed (TA−CL) | 7,227.29 | 9,611.07 | computed |
| **ROCE (computed)** | **34.46%** | **34.64%** | computed |
| PAT | 1,803.05 | 2,667.73 | results Mar-26 PDF, Standalone P&L p.6 |
| Closing Net Worth | 7,078.30 | 9,513.56 | results Mar-26 PDF, Standalone BS p.5 |
| Avg Net Worth | 7,078.30 (closing only, FY24 opening N/A) | 8,295.93 | computed |
| **ROE (computed)** | **25.47%** | **32.16%** | computed |

(All ₹ Lakhs unless noted.)

- **A1 Median ROCE**: median(34.46%, 34.64%) = 34.55% → ≥25% → **Score 5**
- **A2 Minimum single-year ROCE**: min = 34.46% → ≥15% → **Score 5**
- **A3 Median ROE**: median(25.47%, 32.16%) = 28.82% → ≥20% → **Score 5**
  (FY25 ROE uses closing net worth only — FY24 opening net worth not in
  provided data, per formula fallback rule)
- **A4 ROCE trend, latest vs earliest**: 34.64% (FY26) ≥ 34.46% (FY25) →
  **Score 5**

**Block A total: 20/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

| Item | FY25 | FY26 | Source |
|---|---|---|---|
| CFO | 329.60 | 2,115.91 | results Mar-26 PDF, Standalone CF p.7, "Net Cash Generated from/(used in) Operating Activities" |
| Capex (net PPE line) | 347.60 (outflow) | 32.53 (outflow) | results Mar-26 PDF, Standalone CF p.7, "Sales/(Purchase) of Property, Plant & Equipments" — single net line, no gross purchase/intangibles/acquisition split disclosed |
| FCF (CFO−Capex, computed) | −18.00 | 2,083.38 | computed |
| PAT | 1,803.05 | 2,667.73 | results Mar-26 PDF, Standalone P&L p.6 |

- **B1 Cumulative CFO ÷ Cumulative PAT**: (329.60+2,115.91) / (1,803.05+2,667.73)
  = 2,445.51 / 4,470.78 = **0.547** → 0.50-0.69 band → **Score 1**
  (note: just above the 0.50 deal-breaker-#4 threshold — a watch item)
- **B2 FCF-positive years as proportion**: 1 of 2 years (FY26 only) = 50%
  → 50-74 band → **Score 2**
- **B3 Cumulative FCF ÷ Cumulative PAT**: (−18.00+2,083.38)/4,470.78 =
  2,065.38/4,470.78 = **0.462** → 0.40-0.59 band → **Score 3**
- **B4 Change in WC Days, latest vs earliest**: see WC days table below
  — 165.48 (FY26) vs 219.17 (FY25) = decreased 53.69 days → decreased
  >5 days → **Score 5**

**Block B total: 11/20**

Working Capital Days detail (Revenue basis for all three components; a
COGS-basis figure is not explicitly disclosed as a standalone line, so
Revenue basis is used throughout and stated here):

| | FY25 | FY26 |
|---|---|---|
| Trade Receivables | 7,456.85 | 6,740.70 |
| Revenue | 17,254.85 | 22,428.14 |
| Receivable Days | 157.72 | 109.70 |
| Inventory | 5,000.99 | 5,064.76 |
| Inventory Days | 105.79 | 82.44 |
| Trade Payables (MSE + other) | 217.55+1,878.44=2,095.99 | 232.14+1,406.05=1,638.19 |
| Payable Days | 44.34 | 26.66 |
| **WC Days (R+I−P)** | **219.17** | **165.48** |

(Source: results Mar-26 PDF, Standalone BS p.5)

---

## BLOCK C: GROWTH (Max 20)

CAUTION: with only 2 annual data points, every "CAGR" below is a
**single-period (n=1) YoY growth rate**, not a verified multi-year CAGR.
Flagged in data_notes; treat with caution downstream.

- **C1 Revenue CAGR**: Revenue FY25 17,254.85 → FY26 22,428.14 (results
  Mar-26 PDF, Standalone P&L p.6) = (22,428.14/17,254.85)^(1/1)−1 =
  **+29.98%** → ≥20% → **Score 5**
- **C2 PAT CAGR**: PAT FY25 1,803.05 → FY26 2,667.73 =
  (2,667.73/1,803.05)^(1/1)−1 = **+47.96%** → ≥20% → **Score 5**
- **C3 Positive YoY revenue years proportion**: 1 of 1 measurable YoY
  period is positive = 100% → **Score 5**
- **C4 PAT CAGR minus Revenue CAGR**: 47.96% − 29.98% = **+17.98pp** →
  ≥+3pp → **Score 5**

**Block C total: 20/20** (caveated — see data confidence override below)

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

| Item | FY26 | Source |
|---|---|---|
| Non-current Borrowings | 77.89 | results Mar-26 PDF, Standalone BS p.5 |
| Current Borrowings | 6,970.88 | results Mar-26 PDF, Standalone BS p.5 |
| Total Borrowings | 7,048.77 | computed |
| Cash & Cash Equivalents | 9.13 | results Mar-26 PDF, Standalone BS p.5 |
| Net Debt (computed) | 7,039.64 | computed |
| EBITDA (computed, FY26) | 3,492.68 | computed (EBIT 3,329.19 + Depreciation 163.49) |
| Total Equity | 9,513.56 | results Mar-26 PDF, Standalone BS p.5 |
| Total Current Assets | 15,710.76 | results Mar-26 PDF, Standalone BS p.5 |
| Total Current Liabilities | 9,290.78 | results Mar-26 PDF, Standalone BS p.5 |

- **D1 Net Debt ÷ EBITDA**: 7,039.64/3,492.68 = **2.02x** → 2-3x band →
  **Score 1**
- **D2 Interest Coverage (EBIT ÷ Interest)**: 3,329.19/538.16 = **6.19x**
  → 5-9.9x band → **Score 4**
- **D3 Debt ÷ Equity**: 7,048.77/9,513.56 = **0.74x** → 0.5-1.0x band →
  **Score 3**
- **D4 Current Ratio**: 15,710.76/9,290.78 = **1.69x** → 1.5-1.99x band
  → **Score 4**

**Block D total: 12/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding pattern, promoter holding, promoter pledge, or
contingent-liability note appears in any provided input (screener CSVs
or either results PDF, all pages read). All four items are "N/A (not in
provided data)".

- **E1 Promoter holding (latest quarter)**: N/A (not in provided data)
  → **Score 0**
- **E2 Promoter holding change over 3 years**: N/A (not in provided
  data) → **Score 0**
- **E3 Promoter pledge (latest)**: N/A (not in provided data) →
  **Score 0**
- **E4 Contingent liabilities ÷ Net Worth**: N/A — no contingent
  liability note in either results PDF (not in provided data) →
  **Score 0**

**Block E total: 0/20**

---

## CORE SCORE

A(20) + B(11) + C(20) + D(12) + E(0) = **Core Score: 63/100**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

| Test | Score | Bar | Rationale (anchored) |
|---|---|---|---|
| M1 Pricing Power | 3 | ███░░ | EBITDA margin 15.09% (FY25) → 15.58% (FY26) = +0.49pp (stable ±2pp), revenue CAGR 29.98% (≥10%) → stable-margin + growth band (computed from standalone P&L, results Mar-26 PDF p.6) |
| M2 Cost Advantage vs peers | 3 | ███░░ | Karnika EBITDA margin 15.58% (FY26) vs peer median 13.40% (KITEX 4.26%, MONTECARLO 17.81%, SPAL 13.40% — peer screener-Data_Sheet.csv FY26 col) = +2.18pp → 2-5pp above band |
| M3 Capital Efficiency | 5 | █████ | FAT = Revenue 22,428.14 / Net Block+CWIP 602.40 = 37.23x (>3x); ROCE 34.64% FY26 (>20%) → top band (results Mar-26 PDF, Standalone BS/P&L) |
| M4 Customer Stickiness | 3 | ███░░ | Zero revenue-decline years (only YoY period measured is positive) but receivable days moved −48.02 days (not stable ±10) → does not meet the top-band stability condition, scored at the "max 1 decline year" tier |
| M5 Scale & Dominance | 0 | ░░░░░ | PEER DATA NEEDED — only 3 named peers provided (KITEX, MONTECARLO, SPAL), not a full segment universe; among those 3 + subject, Karnika mcap ₹742.42 Cr is smallest (KITEX ₹3,059.33 Cr, SPAL ₹2,915.36 Cr, MONTECARLO ₹1,122.95 Cr — screener-Data_Sheet.csv each), but full-segment ranking cannot be confirmed |
| M6 Technology / R&D | 0 | ░░░░░ | No R&D data in provided inputs → N/A |
| M7 Regulatory / License | 0 | ░░░░░ | Apparel/textile is an unregulated segment (no license gate, many listed players) → 0 |
| M8 Distribution | 0 | ░░░░░ | No reach/outlet data in provided inputs → N/A |
| M9 Brand | 0 | ░░░░░ | GM proxy (Revenue−Material Cost)/Revenue: Karnika 33.72% vs peer median 55.20% (KITEX) — Karnika 21.48pp BELOW peer median → at/below band. Basis caveat: Karnika's Material Cost includes Purchase of Stock-in-Trade; peer sheets show no equivalent trading-purchase line, so this is not fully like-for-like |
| M10 Switching Costs | 5 | █████ | Revenue grew in the one measurable YoY period AND receivable days declined 48.02 days (well within "rose ≤10 days") → top band on the literal test, though based on a single YoY period (flagged as thin evidence) |
| M11 Network Effects | 0 | ░░░░░ | Only 2 years available vs 6 required for the two-window test; selling expense is not separately disclosed (bundled into "Other Expenses") so the selling-% condition cannot be verified → scored conservatively at 0, per rule |
| M12 Negative WC / Float | 0 | ░░░░░ | WC days 219.17 (FY25) and 165.48 (FY26), both >45 days in every year → 0 |

**Moat Score: 3+3+5+3+0+0+0+0+0+5+0+0 = 19/60**

Moats "present" (score ≥3): M1, M2, M3, M4, M10 = **5 moats present**

**Moat Classification: 4-5 present → STRONG**

---

## GRAND TOTAL

Core Score (63) + Moat Score (19) = **Grand Total: 82/160**

---

## DATA CONFIDENCE AND CLASSIFICATION

Data confidence rule: "<3 [years] auto AVERAGE." Only 2 years of
standalone annual data are available (FY25, FY26) — consolidated FY25
does not exist as a comparative (subsidiary Kidcity Solutions Pvt Ltd
first consolidated FY26, per company disclosure).

Raw classification matrix result (before the history override): Core
63 (60-79 band) + moat class STRONG → **GOOD+**.

Deal-breaker #9 — "history <3 years → AVERAGE" — is triggered by the
2-year data window and overrides the matrix result.

**Final Classification: AVERAGE** (capped down from a computed GOOD+ by
the <3-year history override; the underlying scores are the strongest
part of the picture the data can currently support, not a judgment that
the business is average)

Deal-breakers checked and their status:
1. Block A <8 → not triggered (20)
2. Block B <8 → not triggered (11)
3. Median ROCE <10% → not triggered (34.55%)
4. Cumulative CFO/PAT <0.50 → not triggered, but close (0.547) — watch item
5. Pledge >15% → cannot be evaluated, no pledge data provided
6. ND/EBITDA >3x AND IC <3x → not triggered (2.02x / 6.19x)
7. Revenue declined in majority of years → not triggered on available
   data (1 of 1 measurable years grew); cannot confirm a longer window
8. PAT negative in any of last 3 years → not triggered on available
   data (both of 2 available years positive); cannot confirm FY24
9. **History <3 years → TRIGGERED. Classification capped at AVERAGE.**

---

## STRONGEST / WEAKEST BLOCK

- **Strongest**: Block A (Return on Capital), 20/20 — every metric maxes
  out on both available years; Block C also scored 20/20 but is
  single-period (n=1) and therefore not treated as equally robust.
- **Weakest**: Block E (Shareholder Alignment), 0/20 — entirely a data
  gap (no shareholding, pledge, or contingent liability disclosure
  provided), not a scored weakness in the business itself.

## CASH TREND (feeds FLAG-CASH downstream)

Block B trend: **improving** — standalone CFO/PAT conversion rose from
18.3% in FY25 (CFO ₹329.60L / PAT ₹1,803.05L) to 79.3% in FY26 (CFO
₹2,115.91L / PAT ₹2,667.73L), though the cumulative two-year CFO/PAT of
0.55x remains below the 1.00x full-conversion bar (results Mar-26 PDF,
Standalone CF p.7 and P&L p.6).

---

## DECISION LINE

Karnika Industries scores GOOD+ on the raw matrix (Core 63, moat STRONG,
Grand Total 82) but is mechanically capped at **AVERAGE** because only
2 years of standalone financial history exist in the provided inputs —
this is a data-window constraint, not a company-quality verdict. Returns
on capital are exceptionally high and improving (ROCE ~34-35% both
years), growth is strong (+30% revenue, +48% PAT YoY), and cash
conversion improved sharply in FY26, but Block E is a total blank (no
shareholding data) and the growth/CAGR figures rest on a single YoY
observation. Downstream stages should treat this as an early-stage
verified track record, not yet a full-cycle one.

---

```yaml
stage: B01-gate0
company: "KARNIKA"
run_date: "2026-07-11"
model: claude-sonnet-5
status: complete
input_gaps:
  - "rating: absent (no rating PDF provided)"
  - "presentation: absent (no investor presentation provided)"
  - "concalls: 2 FY26 concalls present in run inputs; not used in Gate 0 (quantitative-only stage), noted for continuity"
  - "sector_cap_row 'Pharma / CDMO' in manifest appears misclassified for Karnika/peers (apparel/textile); flagged for phase 3, no Gate 0 impact"
  - "screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv contain no populated historical data cells (headers/labels only); all annual figures sourced instead from results PDFs (FY25 & FY26 standalone) and screener-Data_Sheet.csv (FY26 consolidated single-year + quarterly)"
  - "no shareholding pattern / promoter holding / pledge data in provided inputs; Block E scored 0/20 as N/A throughout"
  - "no contingent liabilities note in either results PDF; E4 scored 0/N/A"
  - "only 2 years of standalone annual financials available (FY25, FY26); consolidated FY25 comparative does not exist (subsidiary Kidcity Solutions Pvt Ltd first consolidated in FY26 per company note); history <3yr deal-breaker caps classification at AVERAGE"
  - "peer data limited to 3 named peers (KITEX, MONTECARLO, SPAL) via screener Data_Sheet exports; not a full segment/industry universe, so M5 scale-and-dominance scored 0/PEER DATA NEEDED"
flags:
  - type: FLAG-GATE0
    reason: "Classification capped at AVERAGE by the <3-year history deal-breaker (#9). Underlying computed matrix score (Core 63/100, moat STRONG, grand total 82/160) would map to GOOD+ absent that override. Only 2 years of standalone annual financials are available (FY25, FY26) because the screener's dedicated multi-year CSV exports were empty and no consolidated FY25 comparative exists (first-year consolidation of subsidiary Kidcity Solutions Pvt Ltd in FY26). All Block C growth metrics and moat tests M1/M10/M11 are single-period (n=1) YoY observations, not verified multi-year trends."
data_years: 2
fy_range: "FY25 to FY26"
blocks: {A: 20, B: 11, C: 20, D: 12, E: 0}
core_score: 63
moat_score: 19
grand_total: 82
moats_confirmed: 5
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers:
  - "#9 history <3 years -> AVERAGE (2 years of standalone annual data available: FY25, FY26; consolidated FY25 comparative does not exist per company disclosure); overrides raw matrix result of GOOD+"
history_downgrade: true
data_notes:
  - "no loss-to-profit swing identified (both FY25 and FY26 standalone PAT positive)"
  - "GM proxy used for M9: (Revenue - Material Cost)/Revenue; Karnika's Material Cost includes Purchase of Stock-in-Trade, peer sheets show no equivalent trading-purchase line item, so the comparison basis is not fully like-for-like"
  - "M5 PEER DATA NEEDED: only 3 named peers available (KITEX, MONTECARLO, SPAL), not a full segment universe; scored 0"
  - "M11 scored conservatively at 0: only 2 years available vs 6 required for the two-window test; selling expense not separately disclosed (bundled into Other Expenses)"
  - "C1/C2/C4 CAGR figures are single-period YoY growth rates (n=1 year), not verified multi-year CAGRs, due to 2-year data availability"
  - "FY25 ROE computed using closing net worth only (FY24 opening net worth not available in provided data), per formula fallback rule"
  - "EBIT/EBITDA computed basis used throughout: PBT + Interest [+ Depreciation for EBITDA] minus Other Income; Other Income excluded as non-operating per standalone cash-flow-statement indirect-method adjustments (profit on sale of investments, interest income, dividend income)"
  - "FCF capex figure uses standalone CF statement's single net line 'Sale/(Purchase) of Property, Plant & Equipments' (no separate gross purchase, intangibles, or acquisition breakdown disclosed)"
  - "WC days computed on Revenue basis for all three components (Receivable/Inventory/Payable Days); COGS not explicitly disclosed as a standalone line"
  - "cumulative CFO/PAT (B1) = 0.547, just above the 0.50 deal-breaker #4 threshold -- a watch item even though not formally triggered"
  - "Karnika equity share capital rose from Rs1,239.95L (FY25) to Rs6,199.75L (FY26), a ~5x increase, sharply diluting EPS (FY25 14.54 vs FY26 6.41) despite higher PAT; noted for downstream context, does not affect Gate 0 scoring since no promoter-specific data was available regardless"
block_b_trend: "improving - standalone CFO/PAT conversion rose from 18.3% in FY25 (CFO Rs329.60L / PAT Rs1,803.05L) to 79.3% in FY26 (CFO Rs2,115.91L / PAT Rs2,667.73L), though the cumulative two-year CFO/PAT of 0.55x remains below the 1.00x full-conversion bar"
```
