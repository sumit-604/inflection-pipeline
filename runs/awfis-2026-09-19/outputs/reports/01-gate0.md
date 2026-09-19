# STAGE 1 — GATE 0 SCORECARD: AWFIS SPACE SOLUTIONS LTD (AWFIS)
Run date: 2026-09-19 | Model: claude-sonnet-5 | Mode: PIPELINE (mechanical, no qualitative judgment)

Data available: 8 years (FY19 to FY26) for revenue, PAT, CFO and PAT-linked
metrics (screener-data, `screener-Data_Sheet.csv`, PROFIT & LOSS / CASH FLOW
sections). Balance-sheet metrics that need a current-liabilities /
trade-payables split are available for only 5 of those 8 years: FY21, FY22,
FY23 (Prospectus restated financials, p.76-79) and FY25, FY26 (FY26 AR,
standalone p.89 / consolidated p.130-131). FY19, FY20 and FY24 lack that
breakdown in the provided corpus and are marked NOT FOUND for those
sub-metrics. Scoring adapted to this mixed 8-year / 5-year history; every
line states which window it used.

ACCOUNTING BASIS NOTE (binds every number below): AWFIS is an Ind AS 116
lessee. Screener's "Borrowings" line bundles real financial debt with lease
liabilities (verified: FY26 screener Borrowings Rs1,501.18 Cr vs AR FY26
financial borrowings Rs509.03m + lease liabilities Rs14,502.69m =
Rs1,501.17 Cr non-current+current, AR p.155 adjusted-net-debt note). All
Block D ratios below are on this REPORTED (Ind AS 116, lease-inclusive)
basis unless stated otherwise. The AR's own "adjusted net debt" (financial
debt only, ex-lease) is NEGATIVE (net cash) in both FY25 (-Rs583.12 Cr) and
FY26 (-Rs386.84 Cr) (AR p.155, Note 33(ii)). Both readings are shown; only
the reported basis is scored, per the fixed formula rule.

## LOAD-BEARING FACTS CHECKED AGAINST THIS SCORECARD (companies/AWFIS.md SPEAR)
- LBF1 (cash EBITDA): touches Block D's EBITDA base. FY26 core EBITDA
  (Sales - Expenses, ex-other-income) = Rs549.76-549.78 Cr (screener quarterly
  sum FY26 Q1-Q4 Operating Profit, cross-checked against AR PBT+Dep+Interest-
  OtherIncome, both consolidated) = 36.8% margin. This is the REPORTED
  (pre-rent) EBITDA the company itself distinguishes from cash EBITDA
  (~10% of revenue per company memory); Gate 0 cannot compute cash EBITDA
  from the Data_Sheet (no lease-rent-paid cash-flow line isolated here) and
  marks it NOT FOUND for this scorecard. Downstream stages must not read
  Block D's "reported EBITDA" figure as cash economics.
- LBF2 (lease book/ALM): confirmed structurally — screener "Borrowings" is
  ~97% lease liability at FY26 (Rs1,450.27 Cr of Rs1,501.18 Cr). Full ALM
  detail (maturity ladder) is outside Gate 0's quantitative scope.
- LBF3 (governance/control): touches Block E directly. Promoter holding
  17.00% (BSE Jun-2026 summary), no pledge. The FY25-to-FY26 promoter
  decline of 3.40pp (20.40% to 17.00%, AR p.104) is PARTLY a 10-Jul-2025
  reclassification of Peak XV Partners' 3.24pp stake from Promoter to
  Public (AR p.104), not entirely an open-market sale. Flagged under E2.
- LBF4 (occupancy/churn): not a Gate 0 quantitative-block input (no seat-
  level occupancy line in the Data_Sheet or AR financial statements used
  here); carried forward unscored.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 7/20

Capital employed = Total Assets - Total Current Liabilities (fixed formula).
EBIT = PBT + Interest. Computed for the 5 years with a current-liabilities
breakdown; FY19, FY20, FY24 NOT FOUND (screener Data_Sheet gives no current/
non-current split).

| FY | PBT (Cr) | Interest (Cr) | EBIT (Cr) | Total Assets (Cr) | Curr Liab (Cr) | Capital Employed (Cr) | ROCE |
|----|---------|---------------|-----------|--------------------|-----------------|-------------------------|------|
| FY21 | -42.64 | 46.56 | 3.91 | 508.58 | 108.95 | 399.64 | 0.98% |
| FY22 | -57.15 | 48.72 | -8.44 | 559.69 | 213.05 | 346.64 | -2.43% |
| FY23 | -46.64 | 72.72 | 26.08 | 930.61 | 280.46 | 650.15 | 4.01% |
| FY25 | 68.76 (consol 68.76 differs from AR consol 68.76 — see note) | — | — | 2,506.98 (screener) | — | — | see AR-based row below |
| FY25 (AR consol) | 68.76 | 136.08 | 20.48 → **use AR PBT 68.76 / consol** | 2,506.98 | 726.72 | 1,780.26 | 11.51% |
| FY26 (AR consol) | 72.25 | 186.26 | 25.85 → **see AR figures below** | 2,910.19 | 990.37 | 1,919.82 | 13.47% |

(Prospectus figures FY21-23 are in Rs million, converted /10 to Cr; source:
Prospectus restated Balance Sheet p.76-77 and restated P&L p.78-79. AR
figures FY25/FY26 are consolidated, Rs million converted /10 to Cr; source:
FY26 AR Consolidated Balance Sheet p.130, Consolidated P&L p.131. EBIT FY25
= PBT 687.60m + Finance costs 1,360.83m = 2,048.43m = 204.84 Cr; EBIT FY26 =
PBT 722.51m + Finance costs 1,862.63m = 2,585.14m = 258.51 Cr — the table
row above understates these; corrected values used in scoring: **FY25 EBIT
Rs204.84 Cr, ROCE 11.51%; FY26 EBIT Rs258.51 Cr, ROCE 13.47%.**)

- **A1 Median ROCE**: values {0.98%, -2.43%, 4.01%, 11.51%, 13.47%} (5 years
  with data) → median = **4.01%** (FY23, computed) → <10% → **Score 0**
  (deal-breaker #3 trigger).
- **A2 Minimum single-year ROCE**: **-2.43%** (FY22, computed) → <8% →
  **Score 0**.
- **A3 Median ROE**: see below → **Score 2** (single valid year, 14.01%,
  band 12-14.9%).
- **A4 ROCE trend, latest vs earliest**: latest (FY26, 13.47%) ≥ earliest
  (FY21, 0.98%) → **Score 5**.

**ROE detail (PAT / average Net Worth):**
Net Worth = Equity Share Capital + Reserves (screener-data, BALANCE SHEET
section), per year:
FY19 -37.21 | FY20 -82.37 | FY21 11.36 | FY22 -44.67 | FY23 -23.60 |
FY24 -93.81 | FY25 459.22 | FY26 552.45 (all Rs Cr, screener-data)

PAT (screener-data): FY19 -62.47 | FY20 -67.98 | FY21 -42.64 | FY22 -57.16 |
FY23 -46.64 | FY24 -17.57 | FY25 67.87 | FY26 70.85 (Rs Cr)

Net worth is negative in FY19, FY20, FY22, FY23, FY24, and the FY25 average
crosses from a negative FY24 opening (-93.81) to a positive FY25 closing
(459.22, IPO primary proceeds) — every one of these years produces a
mathematically meaningless ROE (sign-crossing or negative denominator) and
is marked **N/M (negative/crossing net worth)**, excluded from the median,
consistent with the CAGR negative-endpoint convention applied by analogy.
Only **FY26** has both opening (FY25 closing, positive) and closing net
worth positive: ROE FY26 = 70.85 / [(459.22+552.45)/2] = 70.85/505.84 =
**14.01%** (computed, screener-data). With one clean year, median = 14.01%
→ band 12-14.9% → **Score 2**. FLAG: this is a single-data-point median; do
not treat as a stable ROE read.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 10/20

Cumulative figures across the full 8-year window (screener-data, CASH FLOW
and P&L sections) unless stated:
Cumulative CFO (FY19-26) = -11.48-7.79+57.44+82.69+195.19+228.96+362.56+616.24
= **Rs1,523.81 Cr**
Cumulative PAT (FY19-26) = **-Rs155.74 Cr** (net cumulative loss; the
company has not yet earned back its pre-listing losses on a PAT basis)

- **B1 Cumulative CFO / Cumulative PAT**: 1,523.81 / -155.74 = **negative,
  N/M** (cumulative PAT is negative; the ratio falls outside every positive
  band). Scored per the catch-all "<0.50 = 0" → **Score 0**. FLAG: this is
  a scoring-mechanics artifact, not a cash-quality warning — cumulative CFO
  is strongly positive and PAT is near-breakeven only because of heavy
  Ind AS 116 depreciation/interest in the FY19-24 loss years; see
  block_b_trend below.

- **B2 FCF-positive years as proportion**: FCF = CFO - Capex (PPE +
  intangibles from cash flow statement). Capex breakdown available for
  FY21, FY22, FY23 (Prospectus p.79-80) and FY25, FY26 (FY26 AR
  Consolidated Cash Flow p.131-132); FY19, FY20, FY24 NOT FOUND.
  | FY | CFO (Cr) | Capex (Cr) | FCF (Cr) |
  |----|---------|-----------|---------|
  | FY21 | 57.44 | 38.09 | 19.36 |
  | FY22 | 82.69 | 64.03 | 18.67 |
  | FY23 | 195.19 | 145.72 | 49.47 |
  | FY25 | 362.56 | 199.44 | 163.12 |
  | FY26 | 616.24 | 210.47 | 405.77 |
  5 of 5 years with data are FCF-positive = 100% → **Score 5**.

- **B3 Cumulative FCF / Cumulative PAT**: cumulative FCF (5 years with
  data) = 19.36+18.67+49.47+163.12+405.77 = **Rs656.39 Cr**. Matched-year
  cumulative PAT (FY21,22,23,25,26 only, for an apples-to-apples base) =
  -42.64-57.16-46.64+67.87+70.85 = **-Rs7.72 Cr**. Ratio negative/N/M →
  **Score 0** (same mechanical-artifact flag as B1: FCF strongly positive
  against a near-zero PAT base).

- **B4 Change in WC Days, latest vs earliest** (of years with a payables
  breakdown, FY21 to FY26): WC Days = Receivable Days + Inventory Days -
  Payable Days, revenue basis (no COGS line disclosed).
  FY21: Recv 31.50d + Inv 0.43d - Pay 56.81d = **-24.88 days**
  FY26: Recv 33.66d + Inv 0.18d - Pay 75.18d = **-41.34 days**
  (Receivables, Inventory: screener-data; Payables FY21: Prospectus p.77
  Rs277.65m=27.77Cr; Payables FY26: FY26 AR Consolidated BS p.130
  Rs3,077.03m=307.70Cr)
  Change = -41.34 - (-24.88) = **-16.46 days** (WC days deepened negative,
  i.e. improved float) → decreased >5 days → **Score 5**.

**block_b_trend: improving.** FCF turned from Rs19.4 Cr (FY21) to Rs405.8 Cr
(FY26); WC days deepened from -24.9 (FY21) to -41.3 (FY26). The B1/B3 zero
scores are a denominator artifact (near-zero/negative cumulative PAT), not a
deterioration signal.

---

## BLOCK C: GROWTH (Max 20) — Score: 8/20

Revenue (screener-data, Rs Cr): FY19 154.05 | FY20 226.39 | FY21 178.36 |
FY22 257.05 | FY23 545.28 | FY24 848.82 | FY25 1,207.54 | FY26 1,493.48

- **C1 Revenue CAGR** (FY19 to FY26, 7 years): (1,493.48/154.05)^(1/7)-1 =
  **38.3%** → ≥20% → **Score 5**.
- **C2 PAT CAGR**: FY19 PAT -Rs62.47 Cr (negative endpoint) → **N/M
  (negative endpoint)** per CAGR edge rule → **Score 0**. data_notes:
  loss-to-profit swing, FY19 to FY26 (through FY24 last loss year).
- **C3 Positive YoY revenue years**: FY20 +47.0%, FY21 -21.2% (decline),
  FY22 +44.1%, FY23 +112.1%, FY24 +55.6%, FY25 +42.3%, FY26 +23.7%. 6 of 7
  YoY comparisons positive = 85.7% → band 75-99% → **Score 3**.
- **C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → **Score 0** per
  the fixed C4 rule.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 1/20 (REPORTED basis)

Latest = FY26. All figures reported (Ind AS 116) basis, lease liabilities
included in "Borrowings" per screener convention (confirmed above).

- **D1 Net Debt / EBITDA**: Net Debt = Borrowings 1,501.18 - Cash 89.59 =
  **Rs1,411.59 Cr** (screener-data). EBITDA (core, ex-other-income) =
  Rs549.78 Cr (screener quarterly Operating Profit sum, Q1-Q4 FY26: 126.53
  +132.31+139.22+151.72; cross-checked via AR PBT+Dep+Interest-OtherIncome
  = Rs549.76 Cr, FY26 AR Consolidated P&L p.131). ND/EBITDA = 1,411.59 /
  549.78 = **2.57x** → 2-3x band → **Score 1**.
  ALTERNATE (ex-lease, company's own "adjusted net debt", AR p.155): net
  cash of -Rs386.84 Cr FY26. Not scored; formula rule fixes the reported
  basis.
- **D2 Interest Coverage (EBIT/Interest)**: EBIT FY26 = Rs258.51 Cr;
  Interest FY26 = Rs186.26 Cr (screener-data, matches AR Finance costs
  Rs1,862.63m). Coverage = **1.39x** → <1.5x → **Score 0**. FLAG: of the
  Rs186.26 Cr interest, only Rs3.39 Cr is term-loan interest (AR
  Consolidated Cash Flow p.131, "Interest paid on term loan"); Rs161.65 Cr
  is lease interest. This is a reported-basis (Ind AS 116) artifact, not a
  distress signal on actual financial debt.
- **D3 Debt / Equity**: Debt (incl. lease) = Rs1,501.18 Cr; Equity =
  Rs552.45 Cr (screener-data). D/E = **2.72x** → >1.5x → **Score 0**.
  ALTERNATE (financial debt only, AR p.155): Rs509.03m / Rs5,524.46m =
  0.09x, would score 5. Not scored; formula rule fixes the reported basis.
- **D4 Current Ratio**: Total Current Assets Rs6,776.03m / Total Current
  Liabilities Rs9,903.73m (FY26 AR Consolidated BS, p.130) = **0.68x** →
  <1.0 → **Score 0**. Current liabilities include Rs3,950.44m of current
  lease liabilities; excluding those gives 6,776.03/5,953.29 = 1.14x
  (1.0-1.19 band, would score 1). Not scored; formula rule fixes the
  reported basis.

Deal-breaker #6 (ND/EBITDA >3x AND IC <3x → AVOID) does NOT trigger:
ND/EBITDA is 2.57x, not >3x, even though IC is 1.39x <3x. Both legs are
required.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 5/20

- **E1 Promoter holding (latest quarter)**: 17.00% (BSE shareholding
  summary, quarter ended Jun-2026, `inputs/shareholding/BSE-SHP-summary-
  Jun2026.txt`). <30% → **Score 0**. The "professionally managed, 3 if
  FII+DII >50%" alternate cannot be applied: the FII/DII split is NOT in
  the provided shareholding summary (B00 input_gaps, carried forward as an
  open qualifier).
- **E2 Promoter holding change**: a true 3-year window does not exist
  (AWFIS listed 30-May-2024, `B00.recently_listed: true`). Available
  points: post-Offer expected 28.25% (Prospectus p.[IPO section], forward
  estimate, not an actual filed shareholding point) → FY25 actual 20.40%
  (AR p.104) → FY26 actual 17.00% (AR p.104, matches BSE Jun-2026 17.00%).
  FY25-to-FY26 change = **-3.40pp**, decreased >3% → **Score 0**. FLAG:
  3.24pp of that 3.40pp decline is a 10-Jul-2025 reclassification of Peak
  XV Partners Investments V from Promoter & Promoter Group to Public
  category (AR p.104 footnote), not an open-market sale; the residual
  open-market/other decline is ~0.16pp for the year. Company memory
  separately notes a Rs583 Cr block sale by Peak XV/Bisque/Link Investment
  Trust (unanchored, web-sourced per step1 brief, not independently
  re-verified in this scorecard's document set).
- **E3 Promoter pledge (latest)**: "Whether any shares held by promoters
  are pledge or otherwise encumbered? No" (BSE shareholding summary,
  Jun-2026). 0% → **Score 5**.
- **E4 Contingent liabilities / Net Worth**: AR states legal proceedings
  exist (direct/indirect taxation, vendors, customers, erstwhile
  shareholders) but "do not meet the recognition or disclosure criteria of
  a contingent liability under Ind AS 37" — **no quantified amount is
  disclosed** (FY26 AR Standalone Notes p.113 / Consolidated Notes p.155).
  Marked **N/A (not quantified in provided data)** → **Score 0** per rule
  5, not treated as zero-contingent-liability. FLAG: the GST show-cause
  notices filed May-Jun 2026 (Commercial Tax Officer, Tamil Nadu and
  others, per B00) are not quantified as a contingent liability in this
  25-May-2026-dated AR; check the SCN documents directly downstream (LBF3).

---

## CORE SCORE: 31/100 (A7 + B10 + C8 + D1 + E5)

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 24/60, 5 present → STRONG

Peer set: SMARTWORKS (Smartworks Coworking Spaces), INDIQUBE (IndiQube
Spaces), DEVX (Dev Accelerator) — all screener-Data_Sheet.csv, same
EMPTY-CSV defect as AWFIS (raw Data_Sheet only, no ratios sheet).

| # | Test | Score | Evidence |
|---|------|-------|----------|
| M1 | Pricing Power | **5** | Core EBITDA margin FY19 -21.6% → FY26 36.8% (computed, screener-data, PBT+Dep+Interest-OtherIncome basis), expansion far >2pp; revenue CAGR 38.3% ≥10%. PRESENT |
| M2 | Cost Advantage vs peer median | **0** | AWFIS FY26 core EBITDA margin 36.8% vs peer median 60.7% (Smartworks 64.3%, Indiqube 60.7%, DevX 48.4%; all computed PBT+Dep+Interest-OI / Sales, screener-data). AWFIS is 23.9pp BELOW peer median. FLAG below. |
| M3 | Capital Efficiency (FAT>x AND ROCE>y) | **0** | FAT = Sales/Net Block = 1,493.48/1,701.34 = 0.88x (<1x, screener-data) — fails even the lowest band regardless of ROCE. |
| M4 | Customer Stickiness | **3** | 1 revenue-decline year (FY21, COVID), fully recovered by FY22 (257.05 > FY20's 226.39). PRESENT |
| M5 | Scale & Dominance | **1** | Mcap: Smartworks Rs6,260.65 Cr > Indiqube Rs4,088.37 Cr > AWFIS Rs1,973.35 Cr > DevX Rs304.81 Cr (screener-data "Market Capitalization"). AWFIS is top-3 of 4 by mcap but margin rank is LAST (4th of 4) → fails "top3 mcap AND margin top2" → falls to "top5 mcap" band. Narrow 4-name peer universe, flag caveat. |
| M6 | Technology/R&D | **0** | No R&D line disclosed; not a tech/R&D-driven model. |
| M7 | Regulatory/License | **0** | Flexible-workspace leasing is an unregulated activity; no licence/quota gate found in the corpus. |
| M8 | Distribution | **5** | 41 new centres and ~30K seats added in FY26, taking signed supply to 250+ centres / 175K+ seats across 18 cities (FY26 AR p.8); revenue/centre roughly stable-to-growing (FY26 ~Rs5.97 Cr/centre vs FY25 ~Rs5.78 Cr/centre, implied). PRESENT |
| M9 | Brand (GM proxy) | **0** | GM proxy = (Revenue-Material Cost)/Revenue: AWFIS 97.83% (screener-data) vs 2-peer median (Smartworks 99.56%, Indiqube 93.36%; DevX material cost NOT FOUND) 96.46% — only +1.37pp above, below the 5pp band. FLAG: test not business-model-fit for a lease-sublease operator (no real "raw material" cost line); not a brand read. |
| M10 | Switching Costs | **0** | Revenue grew all but 1 year, BUT receivable days rose from 8.91 (FY19) to 33.66 (FY26), +24.75 days — fails the "stable" leg required alongside "growth all but 1 year," so drops out of the middle band. |
| M11 | Network Effects | **5** | Latest 3yr revenue CAGR (FY23-26) 39.9% > prior 3yr CAGR (FY20-23) 34.0% (computed, screener-data); selling expense % declined 19.8% (FY23) → 19.6% (FY25, nearest available; FY26 value blank/NOT FOUND in screener Data_Sheet — collector gap). PRESENT, with data-gap caveat on the FY26 point. |
| M12 | Negative WC / Float | **5** | WC days negative in all 5 years with a payables breakdown (FY21 -24.9, FY22 -19.7, FY23 -1.3, FY25 -24.3, FY26 -41.3) — majority (in fact all) negative. PRESENT |

**Moat profile:**
```
M1  Pricing Power        [#####] 5/5  PRESENT
M2  Cost Advantage       [.....] 0/5
M3  Capital Efficiency   [.....] 0/5
M4  Customer Stickiness  [###..] 3/5  PRESENT
M5  Scale & Dominance    [#....] 1/5
M6  Technology/R&D       [.....] 0/5
M7  Regulatory/License   [.....] 0/5
M8  Distribution         [#####] 5/5  PRESENT
M9  Brand                [.....] 0/5
M10 Switching Costs      [.....] 0/5
M11 Network Effects      [#####] 5/5  PRESENT
M12 Negative WC/Float    [#####] 5/5  PRESENT
```
Total 24/60. 5 tests ≥3 (present): M1, M4, M8, M11, M12. → 4-5 present =
**STRONG**.

---

## GRAND TOTAL: 55/160 (Core 31 + Moat 24)

## CLASSIFICATION

Base matrix: Core 31 <40 → **AVOID** (this tier applies regardless of moat
class).

Deal-breaker overrides checked (all recorded; none can raise a classifi-
cation above what the base matrix already gives, since AVOID is the floor):
1. Block A = 7 <8 → max GOOD. TRIGGERED. Driven by FY22's negative ROCE
   (-2.43%) and a 5-of-8-year data window for capital-employed detail.
2. Block B = 10, not <8 → not triggered.
3. Median ROCE 4.01% <10% → max AVERAGE. TRIGGERED.
4. Cumulative CFO/PAT negative (<0.50) → max AVERAGE. TRIGGERED. Years
   driving this: the FY19-24 pre-scale loss years (cumulative PAT -Rs155.74
   Cr) against strongly positive cumulative CFO (Rs1,523.81 Cr).
5. Pledge 0%, not >15% → not triggered.
6. ND/EBITDA (2.57x) not >3x → not triggered (needs both legs).
7. Revenue declined in 1 of 7 years, not a majority → not triggered.
8. PAT negative in FY24 (-Rs17.57 Cr), within the last 3 years (FY24-26)
   → max AVERAGE. TRIGGERED. FY25 and FY26 PAT are both positive.
9. History = 8 years, not <3 → not triggered.

**FINAL CLASSIFICATION: AVOID** (mechanical). Data confidence: 8 years =
moderate tier (7-9 band); no automatic downgrade, but sub-metric coverage
is genuinely patchy (5 of 8 years for balance-sheet detail) — flagged, not
downgraded, per the rules.

---

## STRONGEST / WEAKEST BLOCK

**Strongest**: Block B, Cash Generation Quality (10/20) — driven by 100%
FCF-positive years (of years with data) and deeply negative, deepening
working-capital days; depressed only by the B1/B3 mechanical denominator
artifact (near-zero/negative cumulative PAT).

**Weakest**: Block D, Balance Sheet Strength (1/20) — near-total function
of Ind AS 116 lease-liability accounting. The company's own "adjusted"
(ex-lease) net debt is negative (net cash) in both FY25 and FY26.

---

## DECISION LINE

AVOID (mechanical, Core 31/100 <40, three deal-breakers confirm the
AVERAGE-or-below ceiling independently). This is not a going-concern or
fraud signal: revenue compounds at 38.3% CAGR, FCF is positive in every
year with data (100%), and working-capital days run deeply negative and
deepening. The mechanical failure is concentrated in two places the fixed
formulas cannot see through cleanly: (1) Ind AS 116 lease-liability
accounting inflates Block D's debt and depresses Block D's coverage ratios
for a company the AR itself shows as net-cash on financial debt; (2) only
two years (FY25, FY26) carry a full balance-sheet breakdown in the provided
corpus, so Blocks A and E are scored on a genuinely short, still-scaling
post-IPO window. Route to Halt 1 for the qualitative read; do not treat
this AVOID as a standalone kill signal per the "never halt on company
quality" rule — flags propagate, the operator decides.

---

## KEY FLAGS FOR DOWNSTREAM STAGES

1. **FLAG-LEASE-ACCOUNTING**: Screener's "Borrowings" (Rs1,501.18 Cr FY26)
   is ~97% lease liability. Every Block D ratio scored here is on the
   reported (lease-inclusive) basis; the AR's own adjusted net debt is
   negative (net cash) both FY25 and FY26 (AR p.155). Section 1B / FTTCP
   must decide which basis governs valuation and ROCE for this Ind AS 116
   lessee.
2. **FLAG-ROCE-DEFINITION-GAP**: FY26 AR business review (p.9) claims
   "60%+ RoCE... across 250+ centres, 175K+ seats" against this
   scorecard's fixed-formula ROCE of 13.47% FY26. The gap is almost
   certainly the capital-employed definition (company likely excludes
   lease liabilities); unreconciled here, must be resolved before any
   ROCE-based valuation input is used.
3. **FLAG-MARGIN-VS-PEERS**: AWFIS's reported EBITDA margin (36.8% FY26)
   is 23.9pp below the 3-peer median (60.7%), despite AWFIS being the
   largest of the four by revenue. Check segment mix (Transform,
   third-party D&B growing to 59% of that segment per AR p.9) and peer
   accounting comparability before reading this as a genuine cost
   disadvantage.
4. **FLAG-SHAREHOLDING-GAP**: FII/DII split not in the provided
   shareholding summary; E1's professionally-managed alternate could not
   be tested. Peak XV's 3.24pp reclassification (not a sale) drives most
   of the apparent E2 promoter decline.
5. **FLAG-CASH-MECHANICS**: B1 and B3 both score 0 on a denominator
   artifact (near-zero/negative cumulative PAT against strongly positive
   cumulative CFO/FCF), not a cash-quality problem.
6. **FLAG-GST-SCN**: GST show-cause notices (May-Jun 2026, per B00) are
   not reflected as a quantified contingent liability in the 25-May-2026
   AR (dated before some of the notices); E4 could not be scored on them.
