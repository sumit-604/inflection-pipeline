# STAGE 1: GATE 0 QUANTITATIVE SCORECARD
Company: Finolex Cables Ltd (FINCABLES) | Run date: 2026-08-12 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.
Source files: screener-Data_Sheet.csv (populated; the five other screener exports —
Profit_Loss, Balance_Sheet, Cash_Flow, Quarters, Customization — contain only header
rows with no data cells, so Data_Sheet.csv is the sole quantitative screener source
used below), and Annual_Report.pdf (FY2019-20 vintage — this is the only AR provided;
it is 5+ years stale relative to the FY2026 screener data and is used only where it
adds genuine evidence: capex actuals FY2019/FY2020, and the distribution-network
narrative). No results PDFs, rating notes, announcements, shareholding filings, or
research notes were provided for this run (input gaps, see below).

---

## FORMULA NOTES (stated once, applied throughout)

- ROCE = EBIT ÷ (Total Assets − Current Liabilities). Screener's own ROCE/ROE rows
  (screener-Balance_Sheet.csv, L18-19) are blank in this export, so both are
  **computed**. EBIT = PBT + Interest (Other Income retained inside PBT, since the
  capital-employed base below includes Investments, the asset generating that Other
  Income — this keeps numerator and denominator consistent). Verified against the
  Quarters block: Q4 FY26 Operating Profit given directly as 180.45
  (screener-Data_Sheet.csv L36) reproduces exactly from PBT − OtherIncome + Depreciation
  + Interest = 303.38 − 140.04 + 16.67 + 0.44 = 180.45 (L33-36), confirming the formula.
- Capital Employed: the balance sheet in screener-Data_Sheet.csv (L38-54) does not
  split Current vs Non-current liabilities — "Other Liabilities" (L42) is a combined
  residual. **Data limitation**: Capital Employed is therefore computed as Equity
  Share Capital + Reserves + Borrowings (= Total Assets − Other Liabilities), a
  standard proxy for capital employed when current-liability granularity is absent.
  Stated as "computed, proxy" throughout Block A.
- ROE = PAT ÷ average Net Worth (Equity Share Capital + Reserves). FY2017 uses
  closing Net Worth only (no FY2016 opening balance in the data), stated per rule.
- Capex for FCF: no capex/PPE-purchase line exists in the screener cash-flow export
  (screener-Data_Sheet.csv L55-60 gives only CFO/CFI/CFF/Net Cash Flow totals — CFI
  is an aggregate that includes large investment-portfolio purchases/sales, not just
  capex). The AR (FY2019-20 vintage) gives actual "Purchase of PPE" for two years:
  FY2020 = 32.33, FY2019 = 44.32 (AR p.103, Standalone Cash Flows — Investing
  Activities). For all other years (FY2018, FY2021-FY2026), capex is **computed as a
  proxy** = Δ(Net Block + CWIP) + Depreciation for the year. Cross-check: proxy gives
  FY2020 = 38.16 and FY2019 = 40.93 vs AR actuals of 32.33 and 44.32 — reasonably
  close, proxy used with this caveat stated. FY2017 capex is not computable (no
  FY2016 opening balance).
- CFO reconciliation note: AR Standalone Cash Flow Statement shows FY2020 CFO =
  259.02 (AR p.102) vs screener-Data_Sheet.csv's 308.80 for the same year (L57) —
  likely differing operating/investing classification of interest/tax items between
  sources. FY2019 CFO matches exactly across both sources (154.06). The screener
  figure is used throughout for cross-year consistency; this discrepancy is noted,
  not resolved.
- Trade Payables do not appear anywhere in the provided data (absent from the
  screener export; the AR balance sheet, AR p.100, only covers FY2019/FY2020, not
  the required "latest" FY2026 year). Working Capital Days (Receivable + Inventory −
  Payable) cannot be computed. Receivable Days and Inventory Days alone are shown for
  moat tests that need them (M4, M10); the full WC-days metric (B4, M12) is marked
  N/A per Rule 5, scored 0, not estimated.
- Current Ratio (D4): screener-Data_Sheet.csv has no current-asset/current-liability
  split for FY2026 (or any year); the AR split (FY2019/FY2020 only) is the wrong
  year. Marked N/A, scored 0.
- Shareholding/promoter data (E1-E4 inputs) is entirely absent from this run's
  inputs (confirmed input gap). Block E scored 0/20 on data-absence grounds, not as
  a confirmed weakness. This is flagged prominently below and in the YAML block.
- No PAT loss-to-profit swing in the window: PAT is positive in all 10 years
  (FY2017-FY2026), so no synthetic-CAGR issue arises for C2.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Per-year EBIT, Capital Employed (proxy), ROCE — all computed from
screener-Data_Sheet.csv L22 (PBT), L21 (Interest), L39-41 (Equity Capital, Reserves,
Borrowings):

| FY | PBT | Interest | EBIT=PBT+Int | Cap.Employed (proxy) | ROCE |
|---|---|---|---|---|---|
| 2017 | 503.68 | 4.29 | 507.97 | 2,142.12 | 23.71% |
| 2018 | 549.14 | 1.44 | 550.58 | 2,429.80 | 22.66% |
| 2019 | 610.22 | 0.92 | 611.14 | 2,737.63 | 22.33% |
| 2020 | 512.05 | 1.55 | 513.60 | 3,011.65 | 17.06% |
| 2021 | 630.87 | 0.76 | 631.63 | 3,421.21 | 18.46% |
| 2022 | 786.63 | 1.52 | 788.15 | 3,930.85 | 20.05% |
| 2023 | 649.45 | 1.24 | 650.69 | 4,383.97 | 14.84% |
| 2024 | 863.79 | 2.03 | 865.82 | 4,963.92 | 17.44% |
| 2025 | 922.45 | 1.67 | 924.12 | 5,515.24 | 16.76% |
| 2026 | 928.52 | 1.75 | 930.27 | 6,105.02 | 15.24% |

(screener-Data_Sheet.csv L21-22, L39-41, all years; ROCE computed, proxy capital
employed per note above)

- **A1 Median ROCE**: sorted {14.84, 15.24, 16.76, 17.06, 17.44, 18.46, 20.05, 22.33,
  22.66, 23.71}, median = (17.44+18.46)/2 = **17.95%** → band 15-19.9% → **Score 3**
- **A2 Minimum single-year ROCE**: **14.84%** (FY2023) → band 12-14.9% → **Score 3**
- **A3 Median ROE**: PAT (L24) ÷ average Net Worth (L39+L40). FY2017 closing-only:
  400.24/2,140.88=18.70%. FY2018-26 (avg NW): 14.45%,15.77%,13.62%,14.38%,16.33%,
  12.16%,13.99%,13.42%,12.33%. Sorted: {12.16,12.33,13.42,13.62,13.99,14.38,14.45,
  15.77,16.33,18.70}, median=(13.99+14.38)/2=**14.19%** → band 12-14.9% → **Score 2**
- **A4 ROCE trend, latest vs earliest**: FY2026 15.24% vs FY2017 23.71% = decline of
  **8.47pp** → band >5pp decline → **Score 0**

**Block A total = 3+3+2+0 = 8/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

| FY | CFO | PAT | Capex | FCF |
|---|---|---|---|---|
| 2017 | 212.76 | 400.24 | N/A (no FY16 base) | N/A |
| 2018 | 235.68 | 330.11 | 34.97 (proxy) | 200.71 |
| 2019 | 154.06 | 407.47 | 44.32 (AR p.103, actual) | 109.74 |
| 2020 | 308.80 | 391.00 | 32.33 (AR p.103, actual) | 276.47 |
| 2021 | 114.37 | 461.46 | 45.28 (proxy) | 69.09 |
| 2022 | 473.05 | 599.14 | 85.66 (proxy) | 387.39 |
| 2023 | 356.31 | 504.28 | 35.44 (proxy) | 320.87 |
| 2024 | 576.90 | 651.69 | 199.87 (proxy) | 377.03 |
| 2025 | 207.25 | 700.77 | 228.50 (proxy) | -21.25 |
| 2026 | 49.08 | 713.72 | 220.48 (proxy) | -171.40 |

(CFO: screener-Data_Sheet.csv L57; PAT: L24; capex per note above)

- **B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO(10yr)=2,688.26, ΣPAT(10yr)=5,159.88,
  ratio=**0.521** → band 0.50-0.69 → **Score 1**
- **B2 FCF-positive years**: 7 of 9 computable years positive (FY2018-24 positive;
  FY2025, FY2026 negative; FY2017 excluded, no capex base) = **77.8%** → band
  75-99% → **Score 4**
- **B3 Cumulative FCF ÷ Cumulative PAT** (matched FY2018-2026 window): ΣFCF=1,548.65,
  ΣPAT=4,759.64, ratio=**0.325** → band 0.20-0.39 → **Score 1**
- **B4 Change in WC Days, latest vs earliest**: **N/A (not in provided data)** —
  Trade Payables absent (see formula note) → **Score 0**

**Block B total = 1+4+1+0 = 6/20**

**block_b_trend: deteriorating** — CFO/PAT cash conversion fell from 88.6% in
FY2024 (CFO 576.90 ÷ PAT 651.69) to 6.9% in FY2026 (CFO 49.08 ÷ PAT 713.72), and FCF
turned negative in FY2025 (-21.25) and FY2026 (-171.40) after 7 consecutive positive
years (screener-Data_Sheet.csv L11-24, L57).

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-Data_Sheet.csv L11): FY2017=2,444.84 → FY2026=6,321.01.
PAT (L24): FY2017=400.24 → FY2026=713.72.

- **C1 Revenue CAGR** (9-year, FY2017-FY2026): (6,321.01/2,444.84)^(1/9)-1 =
  **11.13%** → band 10-14.9% → **Score 3**
- **C2 PAT CAGR** (9-year): (713.72/400.24)^(1/9)-1 = **6.64%** → band 5-9.9% →
  **Score 1**
- **C3 Positive YoY revenue years**: of 9 YoY transitions, 2 declines (FY2020:
  2,877.30 < FY2019's 3,077.79; FY2021: 2,768.11 < FY2020's 2,877.30 — pandemic-era
  years), 7 positive = **77.8%** → band 75-99% → **Score 3**
- **C4 PAT CAGR minus Revenue CAGR**: 6.64% − 11.13% = **-4.49pp** → band -3 to
  -8pp → **Score 1**

**Block C total = 3+1+3+1 = 8/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Latest year FY2026 (screener-Data_Sheet.csv L39-51):
Borrowings=19.14, Cash&Bank=168.12, Reserves=6,055.29, Equity Share Cap=30.59,
EBIT (per Block A)=930.27, Interest=1.75.

- **D1 Net Debt ÷ EBITDA**: Net Debt = 19.14 − 168.12 = **-148.98 (net cash)** →
  **Score 5**
- **D2 Interest Coverage** (EBIT ÷ Interest): 930.27 ÷ 1.75 = **531.6x** → band
  ≥10x → **Score 5**
- **D3 Debt ÷ Equity**: 19.14 ÷ (6,055.29+30.59=6,085.88) = **0.003x** → band
  <0.1 → **Score 5**
- **D4 Current Ratio (latest)**: **N/A (not in provided data)** — no current
  asset/liability split for FY2026 in any provided file → **Score 0**

**Block D total = 5+5+5+0 = 15/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

- **E1 Promoter holding (latest quarter)**: **N/A (not in provided data)** —
  shareholding filing absent (confirmed input gap) → **Score 0**
- **E2 Promoter holding change, 3yr**: **N/A** → **Score 0**
- **E3 Promoter pledge (latest)**: **N/A** → **Score 0**
- **E4 Contingent Liabilities ÷ Net Worth (latest)**: **N/A** — the only
  contingent-liabilities disclosure in the provided data is in the FY2019-20 AR
  notes, the wrong (stale) year for "latest" → **Score 0**

**Block E total = 0/20 — entirely a data-absence outcome, not a scored weakness.**
No promoter/shareholding filing of any kind was provided for this run.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 0 | EBITDA margin (computed = PBT−OI+Dep+Int, ÷Sales) fell from 16.20% (FY2017) to 9.80% (FY2026), a **6.4pp decline** despite revenue CAGR 11.1% — exceeds the -2 to -5pp band, so "else 0" (screener-Data_Sheet.csv L11,19-22) |
| M2 | Cost Advantage vs peer | 0 | **PEER DATA NEEDED** — no peer EBITDA margin data provided |
| M3 | Capital Efficiency | 3 | FAT (Sales÷Net Block, FY2026) = 6,321.01÷849.78 = **7.44x** (>2x) AND ROCE 15.24% (>15%) → band 3 (L11, L44) |
| M4 | Customer Stickiness | 1 | 2 revenue-decline years (FY2020, FY2021), overall CAGR positive (11.1%) → band "2 decline years, CAGR positive" = 1 (L11) |
| M5 | Scale & Dominance | 0 | **PEER DATA NEEDED** — no peer mcap/margin ranking provided |
| M6 | Technology/R&D | 0 | N/A (not in provided data) — no R&D line disclosed |
| M7 | Regulatory/License | 0 | Wires & cables manufacturing is an unregulated segment (no licensing-scarcity dynamic); scored 0, not a peer-data gap |
| M8 | Distribution | 1 | AR (FY2019-20, p.10-11, stale) states "5,000+ distributors" and retailer count growing 30,000→50,000 (+67% YoY) — quantified and growing, but revenue-per-outlet trend not verifiable and overall revenue CAGR (11.1%) is below the 15% threshold for band 3; scored conservatively at 1 |
| M9 | Brand | 0 | **PEER DATA NEEDED** — no peer gross-margin data. (Informational only, not scored: GM proxy = (Revenue−RM Cost−ΔInventory)÷Revenue = 19.69% FY2017 vs 10.94% FY2026, declining) |
| M10 | Switching Costs | 1 | Overall revenue growth with 2 decline years (FY2020, FY2021) → band "overall growth, 2+ decline years" = 1 |
| M11 | Network Effects | 0 | 10-year history sufficient for two-window test. Latest 3yr revenue CAGR (FY2023→FY2026) = 12.14% vs prior 3yr (FY2020→FY2023) = 15.93% — latest is **not** greater than prior, and neither meets the ≥20% band → 0 |
| M12 | Negative WC/Float | 0 | N/A (not in provided data) — Trade Payables absent, full WC-days formula not computable |

**Block F (moat) total = 0+0+3+1+0+0+0+1+0+1+0+0 = 6/60**

Moat profile bars (score/5):
```
M1  Pricing Power        [          ] 0
M2  Cost Advantage       [PEER DATA NEEDED]
M3  Capital Efficiency   [===       ] 3  <- CONFIRMED
M4  Customer Stickiness  [=         ] 1
M5  Scale & Dominance    [PEER DATA NEEDED]
M6  Technology/R&D       [          ] 0 (N/A)
M7  Regulatory/License   [          ] 0 (unregulated)
M8  Distribution         [=         ] 1
M9  Brand                [PEER DATA NEEDED]
M10 Switching Costs      [=         ] 1
M11 Network Effects      [          ] 0
M12 Negative WC/Float    [          ] 0 (N/A)
```

**Moats confirmed (score ≥3): 1 (Capital Efficiency only)**
**Moat classification: 1 present = THIN**

---

## CLASSIFICATION BOX

```
Core score        = A(8) + B(6) + C(8) + D(15) + E(0) = 37 / 100
Moat score         = 6 / 60
Moat classification = THIN (1 of 12 tests confirmed)
Data confidence     = 10 years (FY2017-FY2026) = "10+ yrs full" — no downgrade
Classification matrix: Core <40 -> AVOID (moat class does not change this tier)

CLASSIFICATION: AVOID
Grand total (core + moat) = 37 + 6 = 43 / 160
```

**Deal-breaker check** (all 9 rules tested; caps are ceilings, non-binding once
classification is already at AVOID, recorded for the audit trail):
1. Block A <8 → Block A=8, not triggered (exactly at threshold)
2. Block B <8 → **Block B=6, TRIGGERED** (cap: max GOOD — non-binding, already below GOOD)
3. Median ROCE <10% → 17.95%, not triggered
4. Cumulative CFO/PAT <0.50 → 0.521, not triggered (near-miss, 2pp above threshold)
5. Pledge >15% → data absent, cannot confirm, not triggered
6. ND/EBITDA >3x AND IC <3x → net cash position, not triggered
7. Revenue declined majority of years → 2 of 9 years, not majority, not triggered
8. PAT negative in any of last 3 years → PAT positive FY2024-2026, not triggered
9. History <3 years → 10 years available, not triggered

---

## STRONGEST / WEAKEST BLOCK

- **Strongest block: D (Balance Sheet Strength), 15/20 (75%)** — the company is
  net-cash with negligible debt (D/E 0.003x) and interest coverage of 531x; only D4
  (Current Ratio) is unscored, for data reasons, not weakness.
- **Weakest scored block: B (Cash Generation Quality), 6/20 (30%)** — cumulative
  cash conversion of 52% and a sharp FY2026 collapse to 7% CFO/PAT conversion are
  genuine, evidenced depressors, not data artifacts.
- **Lowest raw block: E (Shareholder Alignment), 0/20** — this is a pure
  data-absence outcome (no shareholding filing provided for this run), not a
  confirmed governance weakness, and should not be read as one.

---

## DATA-COMPLETENESS CAVEAT (read before treating AVOID as final)

Of the 100-point core score, **20 points (all of Block E) and 10 further points
(B4 + D4) are unscored purely because the required data was absent from this run's
inputs** — no shareholding/promoter filing, no Trade Payables line anywhere in the
screener export, and no current AR/results covering FY2021-FY2026 (only a FY2019-20
AR was provided). That is 30 of 100 core points (and part of Block F: M2, M5, M9 =
15 of 60 moat points) resting on data gaps rather than measured company performance.
Excluding Block E from the denominator, core score is 37/80 (46.3%), which would sit
in the Core 40-59 (AVERAGE) tier rather than AVOID. **The genuine, fully-evidenced
depressors independent of these gaps are real**: ROCE decline (23.71%→15.24%,
A4=0), EBITDA margin compression (16.2%→9.8%, M1=0), and the FY2026 cash-conversion
collapse (CFO/PAT 6.9%, B1/B3 weak). These would likely keep the classification
below GOOD even with full data, but AVOID specifically should not be treated as
final without shareholding pattern history and a current annual report/results
filing to fill Block E, B4, D4, M2, M5, and M9.

---

## DECISION LINE

Classification: **AVOID** on available core financial data (37/100, THIN moat, 1 of
12 moat tests confirmed). Mechanical run complete; per pipeline rules this flags but
does not halt — flags propagate downstream. Given the scale of the data-completeness
caveat above (30 of 100 core points and 15 of 60 moat points resting on absent
shareholding, trade-payables, and current-AR data rather than measured weakness),
the next data-gathering pass should prioritize a shareholding pattern history and a
current (FY2025-26) annual report or results filing before this AVOID is treated as
decisive.

```yaml
stage: B01-gate0
company: "FINCABLES"
run_date: "2026-08-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results: ABSENT — no dedicated quarterly results PDFs; Gate 0 run from screening CSVs + AR financial statements per degradation map"
  - "rating: ABSENT"
  - "announcements: ABSENT"
  - "shareholding: ABSENT (filing) — caused Block E (E1-E4) to score 0/20 entirely"
  - "research: ABSENT"
  - "prospectus: ABSENT — expected, company long-listed since the 1990s, not a gap"
  - "annual report provided is FY2019-20 vintage, 5+ years stale vs FY2026 screener data; no current AR/results PDF"
  - "Trade Payables absent from all provided files — caused B4 and M12 to score 0/N-A"
  - "current asset/liability split absent for FY2026 (any recent year) — caused D4 to score 0/N-A"
  - "peer/industry comparator data absent — caused M2, M5, M9 to score 0/PEER DATA NEEDED"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID (core 37/100, moat THIN). Genuine depressors: ROCE decline 23.71%->15.24% FY17-FY26 (A4=0), EBITDA margin compression 16.2%->9.8% (M1=0), cash conversion deteriorating to 6.9% CFO/PAT in FY26 (B1/B3 weak), PAT CAGR trailing revenue CAGR by 4.5pp (C4=1). Separately, 30 of 100 core points (all Block E, plus B4, D4) and 15 of 60 moat points (M2, M5, M9) are unscored purely for data-absence reasons (no shareholding filing, no trade payables line, no current AR/results, no peer data), not confirmed weakness -- ex-Block E core score is 37/80 (46.3%, AVERAGE tier). Do not treat AVOID as final without shareholding history and a current annual report/results filing.
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 8, B: 6, C: 8, D: 15, E: 0}
core_score: 37
moat_score: 6
grand_total: 43
moats_confirmed: 1
moat_class: "THIN"
classification: "AVOID"
deal_breakers:
  - "Block B <8 (scored 6/20) -> cap max GOOD (non-binding, classification already AVOID via Core<40 rule)"
history_downgrade: false
data_notes:
  - "No PAT loss-to-profit swing FY2017-FY2026; PAT positive all 10 years"
  - "ROCE and ROE computed (screener's own ROCE/ROE rows blank in this export); EBIT = PBT + Interest; Capital Employed = Equity Share Capital + Reserves + Borrowings (proxy, current-liability split absent)"
  - "FY2017 ROE uses closing Net Worth only, no FY2016 opening balance available"
  - "Capex: actuals from AR p.103 for FY2019 (44.32) and FY2020 (32.33) only; all other years computed proxy = Delta(Net Block+CWIP)+Depreciation, cross-checked reasonably close to the two AR actuals; FY2017 capex not computable"
  - "CFO discrepancy: AR p.102 shows FY2020 CFO=259.02 vs screener Data_Sheet's 308.80 for same year; screener figure used throughout for consistency, discrepancy unresolved"
  - "M8 Distribution scored from stale FY2019-20 AR narrative (5,000+ distributors; retailers 30,000->50,000), not FY2026 reality"
  - "M9 Brand: informational GM proxy computed (19.69% FY2017 vs 10.94% FY2026, declining) but not scored -- no peer data"
  - "PEER DATA NEEDED: M2, M5, M9"
block_b_trend: "deteriorating - CFO/PAT cash conversion fell from 88.6% in FY2024 (CFO 576.90/PAT 651.69) to 6.9% in FY2026 (CFO 49.08/PAT 713.72); FCF turned negative in FY2025 (-21.25) and FY2026 (-171.40) after 7 consecutive positive years"
```
