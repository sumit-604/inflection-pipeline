# STAGE 1: GATE 0 SCORECARD — Fabtech Technologies Ltd (FABTECH)

Run date: 2026-09-26. Basis: CONSOLIDATED (subsidiaries ~35% of FY26 revenue).

Data available: 7 years (FY20 to FY26, plus TTM). Scoring adapted to 7-year
history (screener consolidated annual P&L/BS/CF, cross-checked against
audited FY26 results and Data_Sheet.csv). ROCE% source series starts FY21
(FY20 ROCE not disclosed by screener), so A4 trend uses FY21 as earliest.

## LOAD-BEARING FACT CHECKS (LBF2, LBF4) — done first, per task instructions

**LBF2 cash conversion.** Confirmed: consolidated CFO FY25 = Rs -36.14 Cr,
FY26 = Rs +0.48 Cr (screener rounds to 0) (screening/FABTECH-screener-
consolidated-2026-09-26.txt, Cash Flows block; cross-checked against
audited consolidated cash flow statement, "Net cash generated/(used) from
operating activities," FY26 = Cash generated from operations 1,255.97 lakh
less taxes paid 1,208.23 lakh = ~47.74 lakh = Rs 0.48 Cr; FY25 = -2,646.84
less 967.65 = -3,614.49 lakh = Rs -36.14 Cr) (inputs/results/20260427-
Results_FY26_audited.txt p.9). PAT the same years: Rs 46.45 Cr (FY25),
Rs 38.36 Cr (FY26) (screening/screener-Data_Sheet.csv row "Net profit").
Debtor days 182 FY26 confirmed (screener Ratios block).

**Trade receivables discrepancy found (flag for downstream stages).**
companies/FABTECH.md / B00 LBF2 states FY26 consolidated trade receivables
of Rs 24,151.90 lakh, sourced to the AR (an OCR'd image scan per B00
tooling note). The audited FY26 results filing (text layer, not OCR) shows
consolidated trade receivables at 31-Mar-2026 = **Rs 20,433.51 lakh**
(inputs/results/20260427-Results_FY26_audited.txt p.8, "AUDITED CONSOLIDATED
STATEMENT OF ASSETS AND LIABILITIES," current asset "Trade receivables").
This matches screener's Receivables FY26 = Rs 204.34 Cr exactly
(screening/screener-Data_Sheet.csv row "Receivables"). The FY25 comparative
in both sources agrees at Rs 15,073.61 lakh. Conclusion: the AR OCR figure
(Rs 24,151.90 lakh) is a probable digit misread; the results-filing / screener
figure (Rs 20,433.51 lakh = Rs 204.34 Cr) is the one this scorecard and
downstream stages should carry forward. Flagged below as FLAG-DATA-OCR.

**LBF4 earnings quality.** Other income Rs 22.74 Cr of PBT Rs 48.28 Cr FY26
= 47.1% of PBT (screening/screener-Data_Sheet.csv rows "Other Income" and
"Profit before tax," FY26 column), consistent with the ~Rs 23 Cr / ~Rs 48 Cr
figures named in B00 LBF4. OPM trend confirmed: 15% FY24, 12% FY25, 9% FY26
(screening/FABTECH-screener-consolidated-2026-09-26.txt, annual P&L "OPM %"
row). Both LBF4 figures check out against the filed/screener data available
to this stage.

## BLOCK A: RETURN ON CAPITAL (Max 20)

Source for ROCE%: screener.in's own computed figure, used per formula rule
(screening/FABTECH-screener-consolidated-2026-09-26.txt, Ratios block,
"ROCE %" row: FY21 26%, FY22 48%, FY23 31%, FY24 28%, FY25 22%, FY26 14%).

- **A1 Median ROCE = 27%** (median of 14, 22, 26, 28, 31, 48; screener
  Ratios block) → ≥25% → **Score 5**
- **A2 Minimum single-year ROCE = 14% (FY26)** (screener Ratios block) →
  12-14.9% band → **Score 3**
- **A3 Median ROE = 26.2%**, computed per formula (PAT ÷ average net worth,
  opening+closing/2) using Equity Capital+Reserves and Net Profit from
  screening/screener-Data_Sheet.csv (BALANCE SHEET and PROFIT & LOSS
  blocks): FY21 19.0%, FY22 41.3%, FY23 27.8%, FY24 24.65%, FY25 30.46%,
  FY26 12.94% (median of these six). Note FY26 ROE is depressed by the
  Rs ~207 Cr IPO equity infusion (Oct-2025) diluting average net worth; the
  formula is applied mechanically as specified, no adjustment made.
  ≥20% → **Score 5**
- **A4 ROCE trend, latest (FY26=14%) vs earliest available (FY21=26%)**
  (screener Ratios block) → decline of 12pp, >5pp band → **Score 0**

**Block A total = 13/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Source: screening/FABTECH-screener-consolidated-2026-09-26.txt, Cash Flows
block (CFO, FCF) and Profit & Loss block (Net Profit), FY20-FY26.
CFO by year: 64, -9, -3, -14, 60, -36, 0 (Rs Cr). PAT by year: 12, 8, 23,
22, 27, 46, 38 (Rs Cr). FCF by year: 64, -9, -4, -14, 59, -61, 5 (Rs Cr).

- **B1 Cumulative CFO ÷ Cumulative PAT** = 62 ÷ 176 = **0.35** → <0.50 →
  **Score 0**
- **B2 FCF-positive years** = 3 of 7 (FY20, FY24, FY26) = **43%** → <50% →
  **Score 0**
- **B3 Cumulative FCF ÷ Cumulative PAT** = 40 ÷ 176 = **0.23** → 0.20-0.39
  band → **Score 1**
- **B4 Change in WC days, latest (FY26=90) vs earliest (FY20=-19)**
  (screener Ratios block, "Working Capital Days" row) → increase of 109
  days → >15 days increase → **Score 0**

**Block B total = 1/20.** This is the block that carries the LBF2 concern:
strong reported profit growth has not converted to cash. FY24 CFO (Rs 60
Cr, a good year) collapsed to Rs -36 Cr in FY25 and only partially
recovered to ~Rs 0 Cr in FY26, a year when PAT was Rs 38 Cr and WC days hit
their 7-year high of 90.

## BLOCK C: GROWTH (Max 20)

Source: screening/screener-Data_Sheet.csv, PROFIT & LOSS block, Sales and
Net profit rows, FY20-FY26.

- **C1 Revenue CAGR (FY20 Rs 133.42 Cr to FY26 Rs 410.77 Cr, 6 years)** =
  (410.77/133.42)^(1/6)-1 = **20.7%** → ≥20% → **Score 5**
- **C2 PAT CAGR (FY20 Rs 12.39 Cr to FY26 Rs 38.36 Cr, 6 years)** =
  (38.36/12.39)^(1/6)-1 = **20.7%** → ≥20% → **Score 5**
- **C3 Positive YoY revenue years**: of 6 YoY comparisons FY21-FY26, 4 are
  positive (FY22, FY24, FY25, FY26) and 2 are declines (FY21, FY23) =
  **67%** → 50-74% band → **Score 1**
- **C4 PAT CAGR minus Revenue CAGR** = 20.7% - 20.7% = **~0pp** → within
  ±3pp → **Score 3**

**Block C total = 14/20**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

Source: audited consolidated balance sheet
(inputs/results/20260427-Results_FY26_audited.txt p.8) and screener
Ratios/Balance Sheet blocks.

- **D1 Net Debt ÷ EBITDA**: Total borrowings (non-current Rs 53.02 lakh +
  current Rs 4,220.24 lakh = Rs 42.73 Cr) less Cash & cash equivalents (Rs
  86.88 Cr) and other bank balances (Rs 121.69 Cr) = **net cash position**
  (results filing p.8; screener Balance Sheet "Cash & Bank" FY26 = Rs
  208.57 Cr, matching) → net cash → **Score 5**
- **D2 Interest Coverage, EBIT ÷ Interest**: EBIT = Operating Profit Rs 35
  Cr less Depreciation Rs 5.30 Cr = Rs 29.7 Cr (screener P&L block, FY26
  "Operating Profit" and "Depreciation" rows); Interest Rs 4.16 Cr (screener
  P&L block, FY26 "Interest" row) → 29.7/4.16 = **7.1x** → 5-9.9x band →
  **Score 4**
- **D3 Debt ÷ Equity**: Borrowings Rs 69.64 Cr (screener Balance Sheet
  block, FY26 "Borrowings" row, includes lease liabilities per Ind AS 116)
  ÷ Equity (Capital Rs 44.45 Cr + Reserves Rs 375.32 Cr = Rs 419.77 Cr) =
  **0.17x** → 0.1-0.5 band → **Score 4**
- **D4 Current Ratio**: Total current assets Rs 516.42 Cr ÷ Total current
  liabilities Rs 206.85 Cr (audited consolidated balance sheet, FY26) =
  **2.50x** → ≥2.0 → **Score 5**

**Block D total = 18/20.** The IPO (Oct-2025, Rs ~207 Cr fresh proceeds
after expenses) rebased the balance sheet: FY25 current ratio was only
1.37x (Rs 308.24 Cr / Rs 225.47 Cr); post-IPO cash swamps borrowings.

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

- **E1 Promoter holding (latest, Jun-2026) = 68.94%** (screener
  Shareholding Pattern block; NSE XBRL shareholding pattern
  inputs/shareholding/NSE_SHP_30JUN2026.xml, Promoter and promoter group
  tag, confirms 68.94% at both 31-Mar-2026 and 30-Jun-2026) → ≥60% →
  **Score 5**
- **E2 Promoter holding change over 3 years**: N/A (not in provided data).
  Fabtech listed 07-Oct-2025; only three post-listing quarters exist
  (Dec-2025, Mar-2026, Jun-2026), all flat at 68.94% (screener Shareholding
  Pattern block). No pre-listing/pre-IPO promoter percentage was checked
  in this stage's data sources (RHP shareholding section not extracted
  here). Scored 0 per the "missing data = N/A = 0" rule, not as a
  penalty for dilution; flagged as a post-IPO data limitation, not a
  deal-breaker history trigger (history <3 years applies to financial
  history, not shareholding-pattern history).
- **E3 Promoter pledge (latest, 30-Jun-2026) = 0%**. NSE XBRL shareholding
  pattern (inputs/shareholding/NSE_SHP_30JUN2026.xml,
  "WhetherAnySharesHeldByPromotersAreEncumberedUnderNonDisposalUndertaking"
  tag) = **false** at the MainI (30-Jun-2026) context → 0% → **Score 5**
- **E4 Contingent liabilities ÷ Net Worth**: N/A (not in provided data).
  The annual report (which would carry the contingent-liabilities note) is
  not among this stage's designated data sources (screener, results, RHP,
  peer screeners only). Scored 0 per the grounded-claims rule.

**Block E total = 10/20**

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer EBITDA margin (OPM%) comparison uses the three named peers' screener
consolidated annual P&L, latest FY column: SETL 15%
(screening/SETL-screener-consolidated-2026-09-26.txt, OPM% row), HLEGLAS
15% (screening/HLEGLAS-screener-consolidated-2026-09-26.txt, OPM% row),
PRAJIND 7% (screening/PRAJIND-screener-consolidated-2026-09-26.txt, OPM%
row) → peer median 15%. Fabtech FY26 OPM = 9% (screener P&L block).

- **M1 Pricing Power**: EBITDA margin ran 11% (FY20) to a peak 15% (FY24)
  then fell to 9% (FY26), a ~6pp decline from peak despite revenue CAGR
  20.7% (screener OPM% row) → decline exceeds the 2-5pp "1" band → **Score
  0**
- **M2 Cost Advantage vs peer median (15%)**: Fabtech FY26 OPM 9% is 6pp
  *below* peer median → **Score 0**
- **M3 Capital Efficiency**: Fixed Asset Turnover = Sales Rs 410.77 Cr ÷
  Net Block Rs 78.11 Cr (screening/screener-Data_Sheet.csv) = **5.3x**;
  ROCE (FY26) = 14%. FAT>3x but ROCE not >20% or >15%; FAT>1x AND ROCE>12%
  holds → **Score 1**
- **M4 Customer Stickiness**: 2 revenue-decline years (FY21, FY23) with
  overall positive CAGR (20.7%) → matches the "2 decline years, CAGR
  positive" band → **Score 1**
- **M5 Scale & Dominance**: PEER DATA NEEDED. Only 3 named peers read at
  this stage (SETL mcap Rs 8,031 Cr, HLEGLAS Rs 3,064 Cr, PRAJIND Rs 5,807
  Cr vs Fabtech Rs 648 Cr, screener Market Cap fields) — insufficient for
  a full segment ranking → **Score 0**
- **M6 Technology/R&D**: N/A (not in provided data). No R&D/Revenue line
  disclosed in the screener P&L → **Score 0**
- **M7 Regulatory/License**: Turnkey pharma-plant EPC is not a
  licence/quota-capped business (B00 sector-cap note: "EPC / Civil
  construction" or "Consulting / Engineering services" candidate rows,
  neither licence-gated) → unregulated → **Score 0**
- **M8 Distribution**: No reach/outlet network disclosed for this
  project/order-book business → **Score 0**
- **M9 Brand**: Gross margin proxy (Revenue − Material Cost) ÷ Revenue,
  FY26 = (Rs 410.77 Cr − (Rs 216.35 Cr Raw Material Cost + Rs -26.22 Cr
  Change in Inventory = Rs 190.13 Cr net material cost)) ÷ Rs 410.77 Cr =
  **53.7%** (screening/screener-Data_Sheet.csv, PROFIT & LOSS block, proxy
  stated). Peer gross-margin proxy: PEER DATA NEEDED (peer raw-material-cost
  lines not extracted at this stage) → **Score 0**
- **M10 Switching Costs**: revenue did not grow every year (2 declines);
  "overall growth, 2+ decline years" band applies → **Score 1**
- **M11 Network Effects**: 7 years available, sufficient for the two-window
  test. Latest 3yr revenue CAGR (FY24 Rs 226 Cr to FY26 Rs 411 Cr) = 34.9%
  vs prior 3yr (FY21 Rs 121 Cr to FY23 Rs 194 Cr) = 26.6% → latest > prior.
  Selling expense % of sales: FY24 14.9% (Rs 33.65 Cr / Rs 226 Cr), FY25
  14.35% (Rs 46.94 Cr / Rs 327 Cr), both from screening/screener-Data_Sheet.csv
  "Selling and admin" row — mildly declining. FY26 "Selling and admin" is
  blank in the data sheet (re-bucketed into a lump "Other Expenses" line of
  Rs 89.87 Cr, likely including IPO-related and one-off items), so the
  selling-% test cannot be cleanly confirmed for FY26. Scored conservatively
  at the "rev CAGR ≥20% AND selling % stable/declining" tier rather than the
  top tier, given the FY26 data-bucketing gap → **Score 3**
- **M12 Negative WC/Float**: WC days negative in only 1 of 7 years (FY20 =
  -19); the 4 most recent years (FY23-FY26: 65, 63, 53, 90) are all >45
  days → **Score 0**

**Block F (moat) total = 0+0+1+1+0+0+0+0+0+1+3+0 = 6/60**

**Moats present (score ≥3): 1 (M11 only, score 3).**

**Moat classification: 1 present → THIN**

## SCORECARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A. Return on Capital | 13 | 20 |
| B. Cash Generation Quality | 1 | 20 |
| C. Growth | 14 | 20 |
| D. Balance Sheet Strength | 18 | 20 |
| E. Shareholder Alignment | 10 | 20 |
| **Core total** | **56** | **100** |
| F. Moat (12 tests) | 6 | 60 |
| **Grand total** | **62** | **160** |

Strongest block: **D (Balance Sheet Strength, 18/20)** — IPO proceeds left
the company net cash with a 2.50x current ratio.
Weakest block: **B (Cash Generation Quality, 1/20)** — cumulative CFO is
35% of cumulative PAT over FY20-26, WC days rose 109 days peak-to-latest,
and only 3 of 7 years were FCF-positive.

## DATA CONFIDENCE

7 years of annual data (FY20-FY26) → **7-9 band = moderate confidence**.
No downgrade tier triggered (downgrade only applies at 5-6 years [flag] or
3-4 years [downgrade one tier] or <3 years [auto AVERAGE]). Company itself
listed only 07-Oct-2025; the pre-listing years are the same operating
entity's audited/restated financials, not a different business, so no
history-truncation issue applies to the numeric scorecard, only to
market-facing metrics (E2 shareholding history, which is separately N/A'd
above).

## DEAL-BREAKER OVERRIDES

- **#2 Block B <8 → caps classification at max GOOD.** Block B = 1/20.
  TRIGGERED.
- **#4 Cumulative CFO ÷ Cumulative PAT <0.50 → caps classification at max
  AVERAGE.** Ratio = 0.35. TRIGGERED.
- #1 (Block A<8, actual 13), #3 (median ROCE<10%, actual 27%), #5 (pledge
  >15%, actual 0%), #6 (ND/EBITDA>3x AND IC<3x — net cash, not triggered),
  #7 (revenue declined majority of years — 2 of 6 = 33%, not majority),
  #8 (PAT negative in any of last 3 years FY24-26 — all positive), #9
  (history <3 years — 7 years available): none triggered.

The two triggered deal-breakers name FY25 (CFO -36 Cr) and FY26 (CFO ~0 Cr
against PAT Rs 38 Cr) as the specific years driving the cap; these sit
inside the post-IPO/recently-listed window and coincide with WC days
climbing to their 7-year high, consistent with the growth-induced working
capital drag named in companies/FABTECH.md LBF2 rather than a pre-existing
structural cash problem. That classification (GROWTH-INDUCED vs
STRUCTURAL) is not resolved by this Gate 0 arithmetic pass; it is a stage
2/3 qualitative call.

## CLASSIFICATION

Classification matrix input: Core score 56 (falls in the 40-59 band) →
**Core 40-59 = AVERAGE**, independent of the moat tier. The deal-breaker
caps (max GOOD from #2, max AVERAGE from #4) both resolve to the same or a
looser bound than the matrix already gives, so **AVERAGE** is the final
classification, with **history_downgrade = false** (7-year data confidence
is "moderate," not below the downgrade threshold).

## DECISION LINE

**AVERAGE.** Fabtech shows genuine top-line and bottom-line growth (20.7%
revenue CAGR, 20.7% PAT CAGR, ROCE historically strong at 22-48% in
FY22-25) sitting on a now-clean, net-cash balance sheet post-IPO. But the
scorecard is dragged down by two mechanical facts: cash conversion (Block
B, 1/20, cumulative CFO only 35% of cumulative PAT) and a moat profile that
scores THIN (1 of 12 tests present, all quantitative peer-margin and
scale tests fail or lack peer data). This is a company whose reported
profit growth has not yet proven it can turn into cash, verified directly
against LBF2's cash-conversion concern. No STOP is issued; this scorecard
flags for the operator and the pipeline carries forward.
