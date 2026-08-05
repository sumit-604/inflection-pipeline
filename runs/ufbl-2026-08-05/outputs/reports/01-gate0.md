# GATE 0 SCORECARD — United Foodbrands Ltd (erstwhile Barbeque Nation Hospitality Ltd), UFBL
Run date: 2026-08-05 | Stage: B01-gate0 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history
for P&L-level metrics (revenue, PAT, CFO). Balance-sheet-granular metrics
(exact-formula ROCE, Working Capital Days, FCF) are constrained to 2 computable
years (FY2025, FY2026) because the screener export does not split Current
Liabilities from Non-current, does not disclose Trade Payables, and does not
give a clean Capex line — see DATA NOTES. Every number below carries a source
anchor; where a formula could not be computed from provided data it is marked
N/A (not in provided data), never estimated.

Basis note (critical, read first): screener figures are consolidated, in Rs
crore (cross-verified: screener FY26 Sales 1,338.70cr = results filing
consolidated Revenue from Operations Rs 13,387.02 million ÷ 10). Screener's
"Borrowings" line is confirmed to bundle Ind AS 116 lease liabilities with
financial debt (FY26: Rs 885.27cr = Rs 134.43cr financial borrowings + Rs
750.84cr lease liabilities, per Q4 FY26 results consolidated balance sheet;
ICRA corroborates FY25: total debt Rs 757.5cr of which lease liabilities Rs
688.0cr, external borrowings only Rs 69.5cr — ICRA rating p.2). This is a
restaurant/lease-heavy business; leverage and coverage ratios below are
lease-inclusive per the fixed formula, with the lease-accounting distortion
flagged where material.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Exact-formula ROCE = EBIT ÷ (Total Assets − Current Liabilities) requires a
Current Liabilities split. The screener Data_Sheet does not provide one (only
aggregate "Borrowings" and "Other Liabilities"). Current Liabilities are only
available, at exact balance-sheet granularity, for FY2025 and FY2026, from the
Q4 FY26 results filing (audited, board 19-May-2026). FY2017-FY2024 ROCE is
therefore N/A (not in provided data).

| Year | EBIT (PBT+Interest, screener) | Capital Employed (Total Assets − Current Liab., results filing) | ROCE |
|---|---|---|---|
| FY2025 | Rs 50.70cr (-27.16+77.86) (screener-data) | Rs 1,314.06cr − Rs 268.47cr = Rs 1,045.59cr (results Q4FY26 filing, consol BS, p.16, "as at Mar 31 2025" column) | 4.85% |
| FY2026 | Rs 17.78cr (-68.26+86.04) (screener-data) | Rs 1,437.34cr − Rs 353.22cr = Rs 1,084.12cr (results Q4FY26 filing, consol BS, p.16, "as at Mar 31 2026" column) | 1.64% |

- **A1 Median ROCE** (n=2 computable years): median(4.85%, 1.64%) = 3.25% → <10% → **Score 0**
- **A2 Minimum single-year ROCE**: 1.64% (FY2026) → <8% → **Score 0**
- **A3 Median ROE** (PAT ÷ average Net Worth, opening+closing÷2; FY17 uses closing only, no FY16 opening available): computed for all 10 years (screener-data, PAT and Net Worth = Equity Share Capital+Reserves).

| Year | PAT (cr) | Avg Net Worth (cr) | ROE |
|---|---|---|---|
| FY17 | 9.03 | 146.99 (closing only, no opening) | 6.14% |
| FY18 | -5.80 | 145.99 | -3.97% |
| FY19 | -38.39 | 138.31 | -27.76% |
| FY20 | -32.39 | 68.78 | -47.09% |
| FY21 | -90.46 | 124.91 | -72.42% |
| FY22 | -25.60 | 314.95 | -8.13% |
| FY23 | 17.02 | 393.57 | 4.33% |
| FY24 | -13.41 | 397.06 | -3.38% |
| FY25 | -27.79 | 377.83 | -7.36% |
| FY26 | -59.13 | 336.49 | -17.57% |

Median (avg of 5th/6th of 10 sorted values) = (-8.13 + -7.36)/2 = **-7.75%** → <12% → **Score 0**

- **A4 ROCE trend, latest vs earliest** (only 2 computable years, FY2025→FY2026): 4.85% → 1.64%, decline of 3.21pp → band "decline 3-5pp" → **Score 1**

**Block A total = 0+0+0+1 = 1/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

- **B1 Cumulative CFO ÷ Cumulative PAT** (10-yr, screener-data CFO and PAT):
  Cumulative CFO (FY17-26) = 54.20+127.55+122.25+181.05+67.93+59.81+227.59+220.51+193.35+222.96 = **Rs 1,477.20cr**
  Cumulative PAT (FY17-26) = 9.03-5.80-38.39-32.39-90.46-25.60+17.02-13.41-27.79-59.13 = **Rs -266.92cr**
  Ratio is negative (CFO strongly positive, cumulative PAT negative) → falls in "<0.50" band → **Score 0**
  This is the single most important number in this scorecard: CFO has been positive in every one of the 10 years while cumulative PAT is negative, i.e. cash generation is intact but Ind AS 116 depreciation+lease-interest (below-EBITDA, non-cash-heavy lines) plus the FY21 COVID trough have kept accounting PAT negative most years. See block_b_trend and FLAG-GATE0 below.

- **B2 FCF-positive years as proportion** (computable years only — capex, i.e. purchase of PP&E+intangibles excl. acquisitions, is disclosed cleanly only for FY25/FY26 in the results filings; screener's aggregate "Cash from Investing Activity" bundles acquisitions for all years and cannot be used per the formula):
  FY25: CFO Rs 193.35cr (screener-data) − Capex Rs 83.15cr (results Q4FY26 filing, consol CF stmt, "Purchase of PP&E... capital advances", FY25 column) = **FCF Rs 110.20cr**
  FY26: CFO Rs 222.96cr (screener-data) − Capex Rs 128.83cr (results Q4FY26 filing, consol CF stmt, FY26 column) = **FCF Rs 94.13cr**
  2 of 2 computable years positive = 100% → **Score 5** (sample limited to 2 of 10 years; see DATA NOTES)

- **B3 Cumulative FCF ÷ Cumulative PAT** (same 2-year computable window):
  Cumulative FCF (FY25+FY26) = Rs 204.33cr; Cumulative PAT (FY25+FY26) = Rs -86.92cr (screener-data)
  Ratio negative → **Score 0**

- **B4 Change in WC Days, latest vs earliest** (computable years only; Trade Payables not in screener export, so exact WC Days needs the results-filing balance sheets, available for FY25/FY26 only. Revenue basis used throughout, not COGS basis, per rule — COGS not explicitly broken out.):
  FY25 (consol, results filing): Receivable days = 23.28mn÷12,330.49mn×365 = 0.69; Inventory days = 470.90÷12,330.49×365 = 13.94; Payable days = (89.73+334.99)÷12,330.49×365 = 12.57 → **WC Days = +2.06**
  FY26 (consol, results filing): Receivable days = 30.67÷13,387.02×365 = 0.84; Inventory days = 436.79÷13,387.02×365 = 11.91; Payable days = (292.01+1,099.52)÷13,387.02×365 = 37.94 → **WC Days = -25.19**
  Change = -25.19 − (+2.06) = -27.25 days, i.e. decreased by 27.25 days → "decreased >5 days" → **Score 5**

**Block B total = 0+5+0+5 = 10/20**

**block_b_trend: improving** — CFO rose FY25→FY26 (Rs 193.35cr → Rs 222.96cr, screener-data) and consolidated PAT attributable to owners turned positive in Q1 FY27 (+Rs 3.09cr, results 04-Aug-2026 p.9, un-audited) after the FY26 full-year consolidated net loss of Rs -59.13cr (screener-data / results 19-May-2026).

---

## BLOCK C: GROWTH (Max 20)

Revenue by year (screener-data, cr): FY17 503.48, FY18 586.34, FY19 739.02,
FY20 846.97, FY21 507.08, FY22 860.55, FY23 1233.76, FY24 1254.51, FY25
1233.05, FY26 1338.70.

- **C1 Revenue CAGR** (FY17→FY26, 9 years): (1338.70/503.48)^(1/9)-1 = **11.47%** → 10-14.9% band → **Score 3**
- **C2 PAT CAGR**: FY17 PAT +9.03cr (positive) → FY26 PAT -59.13cr (negative) → endpoint sign change → **N/M (negative endpoint) → Score 0**.
  data_note: PAT swung profit→loss FY17→FY18 (+9.03cr→-5.80cr), loss→profit FY22→FY23 (-25.60cr→+17.02cr), and profit→loss FY23→FY24 (+17.02cr→-13.41cr) — three swings across the window (all screener-data).
- **C3 Positive YoY revenue years proportion**: 9 YoY comparisons FY18-FY26; declines in FY21 (COVID, 846.97→507.08) and FY25 (1254.51→1233.05); 7 of 9 positive = 77.8% → 75-99% band → **Score 3**
- **C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → **Score 0** (per rule)

**Block C total = 3+0+3+0 = 6/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20), latest = FY2026

EBITDA FY26 = PBT+Interest+Dep = -68.26+86.04+189.99 = **Rs 207.77cr**
(screener-data; cross-checked to results filing consol EBITDA Rs 2,077.70
million ÷ 10 = Rs 207.77cr — exact match, results 19-May-2026 p.15).

- **D1 Net Debt ÷ EBITDA**: Net Debt = Borrowings Rs 885.27cr − Cash & Bank Rs 27.66cr (screener-data) = Rs 857.61cr. ND/EBITDA = 857.61/207.77 = **4.13x** → >3x → **Score 0**
  Context (not separately scored): of the Rs 885.27cr, Rs 750.84cr is Ind AS 116 lease liabilities (results Q4FY26 filing consol BS: non-current lease liab Rs 666.52cr + current Rs 84.32cr) and only ~Rs 134.43cr is financial borrowings. ICRA (Oct-2025, p.2) states FY25 external borrowings were just Rs 69.5cr of Rs 757.5cr total debt, "adequate" liquidity, no debt-funded capex plans. Ex-lease Net Debt/EBITDA would be materially lower (~0.5x), but the fixed formula as defined uses the screener's all-in Borrowings figure.
- **D2 Interest Coverage (EBIT ÷ Interest)**: EBIT Rs 17.78cr ÷ Interest Rs 86.04cr (screener-data, = results filing consol Finance costs Rs 860.40 million ÷ 10, exact match) = **0.21x** → <1.5x → **Score 0**. The weak coverage is driven primarily by depressed EBIT (trough year), not by an unusually high interest bill: even isolating only the borrowings-interest component (Rs 8.74cr, results filing consol CF stmt "Interest expense on borrowings", excluding lease interest) gives EBIT/borrowings-interest ≈ 2.0x, still below the 3x threshold.
- **D3 Debt ÷ Equity**: Debt Rs 885.27cr ÷ Equity (Net Worth) Rs 310.30cr (screener-data) = **2.85x** → >1.5x → **Score 0**
- **D4 Current Ratio**: Current Assets Rs 1,468.22 million ÷ Current Liabilities Rs 3,532.18 million (results Q4FY26 filing, consol BS, Mar-2026) = **0.42x** → <1.0x → **Score 0**

**Block D total = 0/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

- **E1 Promoter holding (latest quarter)**: 32.7% as on June 30, 2025 (ICRA rating, 28-Oct-2025, p.3: "promoters and promoter group holding 32.7% stakes... as on June 30, 2025"). Cross-check: 33.72% as of Mar-31-2025 (AR FY2024-25 extract, Corporate Governance shareholding table, line 4567: "Total Promoter & Promoter Group Shareholding (A) 15 1,31,78,544 33.72"). Using the more recent anchored figure (32.7%) → 30-39.9% band → **Score 1**
- **E2 Promoter holding change over 3 years**: N/A (not in provided data) — no anchored shareholding-pattern filing was collected (inputs/shareholding/ empty, an input_gap carried from B00); the AR extract gives only the Mar-2025 snapshot, ICRA gives only Jun-2025. No anchored 3-years-prior comparator exists in the provided sources → **Score 0**
- **E3 Promoter pledge (latest)**: N/A (not in provided data) — neither the AR extract nor the ICRA rating discloses a promoter share-pledge percentage → **Score 0**
- **E4 Contingent liabilities ÷ Net Worth (latest available)**: Contingent liabilities as at Mar-31-2025 (AR extract, consolidated Note 35, p.232-233): indirect tax Rs 206.90mn + direct tax Rs 744.41mn + other Rs 18.92mn = **Rs 970.23mn (Rs 97.02cr)**. Net Worth (total equity incl. NCI) as at Mar-31-2025 = Rs 3,708.55mn (Rs 370.86cr) (results Q4FY26 filing, consol BS, comparative column). Ratio = 97.02/370.86 = **26.17%** → 15-30% band → **Score 3**
  (No FY26 contingent-liability note was in the provided results filings; Mar-2025 is the latest anchored figure available.)

**Block E total = 1+0+0+3 = 4/20**

---

## CORE SCORE

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 1 | 20 |
| B — Cash Generation Quality | 10 | 20 |
| C — Growth | 6 | 20 |
| D — Balance Sheet Strength | 0 | 20 |
| E — Shareholder Alignment | 4 | 20 |
| **Core Score** | **21** | **100** |

Strongest block: **B — Cash Generation Quality (10/20)**. Weakest block: **D — Balance Sheet Strength (0/20)**.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Accounting-comparability note (applies to M1, M3, M9 and any margin-trend
test): FY17-FY19 EBITDA/margins are on a pre-Ind AS 116 basis (lease rentals
expensed in opex); FY20 onward reflects Ind AS 116 (lease rentals reclassified
into depreciation + lease interest, below EBITDA), which mechanically inflates
reported EBITDA/EBITDA-margin post-transition versus pre-transition without a
real economic improvement. Margin-trend tests below use the FY20-FY26
like-for-like window, not the full FY17-FY26 span, where the distinction
matters.

EBITDA margin by year (screener-data, EBITDA = PBT+Interest+Dep):
FY17 12.72%, FY18 22.24%, FY19 16.50%, FY20 21.77%, FY21 18.64%, FY22 18.65%,
FY23 19.65%, FY24 18.31%, FY25 18.43%, FY26 15.52%.

- **M1 Pricing Power**: using the Ind AS116-consistent FY20→FY26 window: margin 21.77%→15.52%, a decline of 6.25pp (outside the "2-5pp despite growth" band), and revenue CAGR FY20-26 = (1338.70/846.97)^(1/6)-1 = 7.93% (<10% growth threshold in any band) → **Score 0**
- **M2 Cost Advantage vs peer median EBITDA margin**: no peer data provided in injected inputs → **PEER DATA NEEDED → Score 0**
- **M3 Capital Efficiency**: FAT = Revenue ÷ Net Block = 1338.70/1160.78 = 1.15x (screener-data; Net Block confirmed = PP&E+ROU assets+Goodwill+Intangibles per results filing consol BS cross-check). ROCE FY26 = 1.64% (Block A). FAT>1x but ROCE far below 12% → **Score 0**
- **M4 Customer Stickiness**: 2 revenue-decline years (FY21, FY25) with overall positive CAGR (11.47%) → "2 decline years, CAGR positive" band → **Score 1**
- **M5 Scale & Dominance**: ICRA (p.1, p.3) describes UFBL qualitatively as "among the largest single-brand chains of barbeque-themed restaurants and a leading player in the casual dining segment," but no quantified peer mcap/margin ranking was provided → **PEER DATA NEEDED → Score 0**
- **M6 Technology/R&D**: restaurant business, no R&D disclosed → **Score 0**
- **M7 Regulatory/License**: unregulated, highly fragmented casual-dining segment; ICRA (p.2) explicitly notes "high competition... numerous regional and national players across both organised and unorganised segments" → **Score 0**
- **M8 Distribution**: single anchored snapshot only — ICRA (p.1, p.3): 236 outlets as on June 30, 2025 (incl. 32 Toscano/SALT, 11 international); ICRA states expansion "has been gradual over the past few years" (qualitative, no anchored multi-year outlet count series or revenue-per-outlet trend available in the provided sources — the operator digest's FY25/FY26/Q1FY27 store-count series is explicitly NON-ANCHORED and is not used for scoring here). Reach is quantified at one point but growth/stability cannot be verified on an anchored basis → **Score 1**
- **M9 Brand**: gross-margin-vs-peer-median test needs peer data, not provided → **PEER DATA NEEDED → Score 0**
- **M10 Switching Costs**: overall revenue growth positive (CAGR 11.47%) with 2 decline years (FY21, FY25) → "overall growth, 2+ decline years" band → **Score 1**
- **M11 Network Effects** (10 years available, ≥6yr test applicable): latest ~3yr CAGR (FY24→FY26, 2 periods) = 3.30%; "prior 3yr" (FY21→FY24) = 35.24%, which is COVID-recovery-distorted off the depressed FY21 base (507.08cr) and not a meaningful comparator. Neither leg clears the 15-20%+ growth thresholds; selling-expense-% for FY26 is blank in the screener export (cannot verify that leg) → **Score 0** (scored conservatively per the instruction for insufficient-window cases)
- **M12 Negative WC/Float**: only 2 years of exact WC Days computable (FY25 +2.06, FY26 -25.19, from Block B4) — a 1-of-2 split, not a clear majority-negative; average = -11.57 days (within the "0-15 days" magnitude band) → **Score 3** (data limited to 2 of 10 years; see DATA NOTES)

**Moat score = 0+0+0+1+0+0+0+1+0+1+0+3 = 6/60**

Moats "present" (score ≥3): M12 only → **1 moat present**

**Moat classification: 1 present = THIN**

---

## CLASSIFICATION

Data confidence: 10 years of P&L/CFO-level history (FY17-FY26) → "10+ yrs full"
tier, no downgrade on data-length grounds. (Note: this is distinct from the
metric-level gaps — ROCE/WC-Days/FCF exact-formula computability is limited to
2 years each, FY25-FY26, as documented in DATA NOTES; per the operator's
instruction this routes to the flag below, not to history_downgrade, which is
reserved for the 3-4yr LIMITED tier.)

Classification matrix: Core Score = 21 → **Core <40 = AVOID**

**Deal-breaker overrides triggered:**
1. Block A (1) < 8 → max GOOD — driven by FY25/FY26 (only ROCE-computable
   years), both in single digits (4.85%, 1.64%), and a negative median ROE
   (-7.75%) across FY18-22 and FY24-26.
3. Median ROCE (3.25%) < 10% → max AVERAGE — same FY25/FY26 driver as above;
   Ind AS 116 inflates the capital-employed base (large ROU assets) against a
   trough EBIT.
4. Cumulative CFO/PAT (negative) < 0.50 → max AVERAGE — driven by cumulative
   PAT -Rs 266.92cr over FY17-26 despite cumulative CFO +Rs 1,477.20cr; this is
   the Ind AS 116 depreciation/lease-interest effect described in block_b_trend,
   not a cash-generation failure.
6. ND/EBITDA (4.13x) > 3x AND Interest Coverage (0.21x) < 3x → **AVOID** —
   driven by FY26 lease-inclusive Borrowings (Rs 885.27cr, of which ~Rs 750.84cr
   is Ind AS 116 lease liabilities, not conventional financial debt — see D1
   context note) against a trough FY26 EBIT of Rs 17.78cr.
8. PAT negative in FY24 (-13.41cr), FY25 (-27.79cr) and FY26 (-59.13cr), i.e.
   all of the last 3 years → max AVERAGE.

Not triggered: #2 (Block B=10, not <8), #5 (pledge data N/A, not confirmed
>15%), #7 (2 of 9 YoY periods declined = 22%, not a majority), #9 (10 years of
history, not <3).

The most restrictive trigger is #6 (AVOID), which is also consistent with the
Core Score <40 AVOID band independently.

**FINAL CLASSIFICATION: AVOID**

This is a Gate-0 quantitative classification against fixed thresholds feeding
downstream stages — per pipeline rules it does not halt the run; there is no
STOP verdict and the low classification is expected and explained by the
trough/recovery and Ind AS 116 lease-accounting drivers below. Flags
propagate; the human decision stays downstream at synthesis.

---

## DATA NOTES

1. Screener export (Data_Sheet.csv) provides no ROCE row and no Current
   Liabilities / Trade Payables / clean-Capex breakdown; exact-formula ROCE,
   Working Capital Days, and FCF are therefore computable only for FY2025 and
   FY2026 (from the Q4 FY26 results filing balance sheets/cash-flow
   statements). FY2017-FY2024 marked N/A (not in provided data) for these
   three metrics.
2. Pre-FY20 vs FY20-onward EBITDA/margin figures are not like-for-like due to
   Ind AS 116 adoption (lease rentals move from opex to below-EBITDA
   depreciation+interest). M1 and other margin-trend tests use the FY20-FY26
   window only, documented explicitly in Block F.
3. Screener's "Borrowings" line bundles Ind AS 116 lease liabilities with
   financial debt (FY26: Rs 885.27cr = Rs 134.43cr financial + Rs 750.84cr
   lease, results filing; FY25 cross-check via ICRA: Rs 757.5cr total debt =
   Rs 69.5cr external borrowings + Rs 688.0cr lease liabilities, ICRA p.2).
   Block D's deal-breaker #6 (AVOID) is therefore substantially a lease-
   accounting effect, not conventional financial distress — ICRA separately
   assesses liquidity as "adequate" with no debt-funded capex planned (ICRA
   p.2-3).
4. PAT swings (screener-data): profit→loss FY17→FY18 (+9.03cr→-5.80cr);
   loss→profit FY22→FY23 (-25.60cr→+17.02cr); profit→loss FY23→FY24
   (+17.02cr→-13.41cr). C2 (PAT CAGR) is N/M because FY17 (positive) to FY26
   (negative) is a sign change across the full window.
5. Q1 FY27 (quarter ended Jun-30-2026, un-audited, results filed 04-Aug-2026):
   consolidated PAT attributable to owners turned positive at +Rs 3.09cr
   (results 04-Aug-2026 p.9), the first positive quarter visible in the
   screener quarterly series (which runs Mar-2024 to Jun-2026); standalone
   entity-only PAT for the same quarter was +Rs 6.13cr (results 04-Aug-2026
   p.3). This post-dates the FY26 full-year loss of Rs -59.13cr scored above.
6. E2 (promoter holding change, 3yr) and E3 (promoter pledge): no anchored
   shareholding-pattern filing was collected (inputs/shareholding/ is an
   empty input_gap carried from B00). AR extract gives only Mar-2025 (33.72%);
   ICRA gives only Jun-2025 (32.7%). Neither a 3-year-prior comparator nor a
   pledge percentage is in the provided anchored sources. The operator's
   non-anchored screener screenshot (OPERATOR_CONTEXT.md) shows promoter
   holding drifting 33.77%→34.62% (Sep-2023→Jun-2026) and FII+DII combined
   ~27.8% (Jun-2026) — directional only, not used for scoring per the
   provenance rule.
7. E4 uses Mar-31-2025 contingent liabilities (latest anchored figure in the
   provided AR extract); no FY26 contingent-liability note was in the
   provided results filings.
8. M2, M5, M9 marked PEER DATA NEEDED: no peer-company financials were
   provided in the injected inputs.
9. M11: FY21→FY24 "prior 3yr" window is COVID-recovery-distorted (35.24%
   CAGR off the depressed FY21 base of Rs 507.08cr) and not a meaningful
   comparator; FY26 "Selling and admin" expense is blank in the screener
   export, so the selling-expense-% leg of the test could not be fully
   verified for the latest year.
10. M12: only 2 of 10 years have exact-formula WC Days (FY25 +2.06, FY26
    -25.19); scored conservatively (3, not 5) given the 1-of-2 split rather
    than a clear majority-negative history.
11. Minor cross-source PAT discrepancy (not scoring-material): ICRA's own key
    financial indicators table (p.4) shows consolidated PAT of Rs -11.2cr
    (FY24) and Rs -27.1cr (FY25) versus screener-data Rs -13.41cr (FY24) and
    Rs -27.79cr (FY25) — both anchored to their respective sources, close but
    not identical, likely differing PAT scope (owners' share vs total) or
    ICRA's own restatement; screener-data used as the primary scored figure
    throughout for consistency with the rest of the P&L series.

---

```yaml
stage: B01-gate0
company: "UFBL"
run_date: "2026-08-05"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID (Core 21/100, deal-breakers #1/#3/#4/#6/#8 triggered) is driven by Ind AS 116 lease accounting (screener 'Borrowings' bundles ~Rs751cr of lease liabilities into FY26's Rs885cr total, per results filing/ICRA cross-check) plus the FY21 COVID trough and FY25/H1-FY26 SSSG contraction (ICRA: -3.8% FY25, -3.4% Q1 FY26), not a cash-generation failure: cumulative CFO FY17-26 is +Rs1,477cr against cumulative PAT of -Rs267cr. Q1 FY27 (un-audited, 04-Aug-2026) turned consolidated PAT positive (+Rs3.09cr owners' share) after the FY26 full-year loss of -Rs59.13cr. Deal-breaker #6 (ND/EBITDA 4.13x AND IC 0.21x -> AVOID) is the binding constraint and is itself substantially lease-accounting driven; ICRA separately rates liquidity 'adequate' with no debt-funded capex planned."
data_years: 10
fy_range: "FY17 to FY26"
blocks: {A: 1, B: 10, C: 6, D: 0, E: 4}
core_score: 21
moat_score: 6
grand_total: 27
moats_confirmed: 1
moat_class: "THIN"
classification: "AVOID"
deal_breakers: ["1: Block A <8 (FY25-26 ROCE 4.85%/1.64%)", "3: median ROCE 3.25% <10%", "4: cumulative CFO/PAT negative (CFO +Rs1,477cr vs PAT -Rs267cr, FY17-26)", "6: ND/EBITDA 4.13x AND IC 0.21x -> AVOID (FY26, lease-inclusive debt)", "8: PAT negative FY24/FY25/FY26"]
history_downgrade: false
data_notes:
  - "Screener export lacks Current Liabilities/Trade Payables/clean-Capex splits; exact ROCE, WC Days, FCF computable only FY25-FY26 (results filing balance sheets); FY17-FY24 marked N/A."
  - "Pre-FY20 vs FY20+ EBITDA margins not like-for-like (Ind AS 116 adoption reclassifies lease rentals below EBITDA); M1 scored on FY20-FY26 window only."
  - "Screener 'Borrowings' bundles Ind AS 116 lease liabilities with financial debt (FY26: Rs885.27cr = Rs134.43cr financial + Rs750.84cr lease); Block D deal-breakers are substantially lease-accounting driven, not conventional distress (ICRA: FY25 external borrowings only Rs69.5cr of Rs757.5cr total debt, liquidity 'adequate')."
  - "PAT swings: profit-to-loss FY17-FY18; loss-to-profit FY22-FY23; profit-to-loss FY23-FY24 (screener-data). C2 PAT CAGR N/M, negative endpoint FY26."
  - "Q1 FY27 (un-audited, 04-Aug-2026): consolidated PAT owners' share turned positive +Rs3.09cr; standalone +Rs6.13cr; first positive quarter in the screener quarterly series."
  - "E2/E3 (promoter 3yr change, pledge) N/A: no anchored shareholding-pattern filing collected (input_gap); AR gives only Mar-2025 (33.72%), ICRA only Jun-2025 (32.7%)."
  - "E4 uses latest anchored contingent-liability figure, Mar-31-2025 (AR extract); no FY26 figure in provided filings."
  - "M2/M5/M9 marked PEER DATA NEEDED, no peer financials provided."
  - "M11 prior-3yr window COVID-recovery-distorted (FY21 base); FY26 selling-expense % blank in screener, that leg unverifiable."
  - "M12 only 2 of 10 years computable (FY25 +2.06 days, FY26 -25.19 days); scored conservatively at 3."
  - "Minor non-material PAT discrepancy: ICRA's own table shows FY24 -11.2cr/FY25 -27.1cr vs screener-data -13.41cr/-27.79cr; screener-data used as primary throughout."
block_b_trend: "improving — CFO rose FY25 Rs193.35cr to FY26 Rs222.96cr (screener-data), and consolidated PAT (owners' share) turned positive in Q1 FY27 at +Rs3.09cr (results 04-Aug-2026) after the FY26 full-year consolidated loss of -Rs59.13cr."
```
