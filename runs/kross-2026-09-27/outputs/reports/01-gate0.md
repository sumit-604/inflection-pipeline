# STAGE 1: GATE 0 SCORECARD — KROSS Ltd (KROSS)
Run date: 2026-09-27 | Model: claude-sonnet-5

**PEER RESCORE NOTE (2026-09-27, same run):** the orchestrator's original
task omitted the peer Data_Sheet CSVs in error. They have now been supplied
(AUTOAXLES-Data_Sheet.csv, HAPPYFORGE-Data_Sheet.csv, RKFORGE-Data_Sheet.csv
as the run's peers; JAMNAAUTO-Data_Sheet.csv as a numbers-only reference
comp) and the peer-relative moat tests M2, M5, M9 have been re-scored below.
What changed from the first pass: M2 moved 0 → 1, M5 moved 0 → 1, M9 stays
0 (now on an actual peer comparison instead of "PEER DATA NEEDED"). Moat
score moved 11 → 13/60. Grand total moved 79 → 81. Moats confirmed stays at
3 (M1, M3, M4; M2 and M5 score 1, below the "present" threshold of ≥3).
Moat class stays MODERATE. Core score, deal-breakers, and final
classification (GOOD) are unchanged. Everything else in this report is
identical to the first pass.

Data available: 7 years (FY20 to FY26), annual figures. Scoring adapted to
7-year history. One sub-metric (Working Capital Days, Block B4, M4, M10,
M12) is computable only for FY22-FY26 (5 years) because Trade Payables is
not broken out in the screener Data_Sheet for FY20-FY21 and no restated
FY20/FY21 balance sheet exists in the corpus (prospectus restates only
FY22-FY24, plus Q1 FY25). This is stated wherever it binds.

Units: screener Data_Sheet is INR Cr. Annual Report and prospectus figures
are INR million; converted to INR Cr (÷10) and flagged "(converted)" at
first use per line. Peer Data_Sheet CSVs are INR Cr, same as KROSS's.

## DATA SOURCE NOTE (screener defect)
The screener export's own P&L / Balance Sheet / Cash Flow / Quarters CSV
sheets came back EMPTY (formulas with no cached values); no screener-native
ROCE/ROE figures exist. Only Data_Sheet (raw annual + 10 quarters) is
populated, for KROSS and for the peers. Per Formula Definitions rule, all
ratios below are COMPUTED, not sourced-and-anchored to a screener ratio
field, and are labelled "computed" throughout.

## PEER SET
Peers (this run): AUTOMOTIVE AXLES LTD (AUTOAXLES), HAPPY FORGINGS LTD
(HAPPYFORGE), RAMKRISHNA FORGINGS LTD (RKFORGE) — all
inputs/screening/*-Data_Sheet.csv. Reference comp only (not counted in
"peer median" below, per orchestrator instruction): JAMNA AUTO INDUSTRIES
LTD (JAMNAAUTO), CV suspension. Market Capitalization (screener Data_Sheet
META, run date pricing): KROSS 1,728.01 Cr | AUTOAXLES 2,583.51 Cr |
HAPPYFORGE 19,479.68 Cr | RKFORGE 13,073.41 Cr | JAMNAAUTO 5,527.79 Cr.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

EBIT = PBT + Interest (computed; screener does not carry a separate EBIT
line). Capital Employed = Total Assets − Current Liabilities. For FY22-FY26,
Total Assets and Total Current Liabilities are taken from the classified
balance sheet in the Prospectus (FY22-FY24 restated) and the FY26 Annual
Report (FY25-FY26), which is more precise than the Data_Sheet's lumped
"Other Liabilities" line. For FY20-FY21, no classified current-liabilities
figure exists in the corpus; Capital Employed is approximated as
Total Assets − "Other Liabilities" (Data_Sheet), flagged.

| FY | EBIT (Cr) | Capital Employed (Cr) | ROCE |
|----|-----------|------------------------|------|
| FY20 | 12.56 (screener-Data_Sheet: PBT 2.83 + Interest 9.73) | 123.24 (screener-Data_Sheet Total 158.39 − Other Liab. 35.15; APPROX, no CL split available) | 10.19% |
| FY21 | 14.85 (2.83→5.83+9.02) | 143.39 (174.07−30.68; APPROX) | 10.36% |
| FY22 | 24.47 (16.31+8.16) | 105.688 (2024-09_Kross_Prospectus.txt p.279 area, offset ~6968: Total Assets 1,978.24 mn − Total current liabilities 921.36 mn = 1,056.88 mn = 105.688 Cr, converted) | 23.15% |
| FY23 | 53.93 (41.71+12.22) | 139.412 (prospectus: TA 2,505.72 mn − TCL 1,111.60 mn = 1,394.12 mn, converted) | 38.68% |
| FY24 | 76.19 (61.29+14.90) | 180.682 (prospectus: TA 3,520.04 mn − TCL 1,713.22 mn = 1,806.82 mn, converted) | 42.17% |
| FY25 | 79.68 (67.39+12.29) | 453.398 (Annual_Report_2026.txt p.~57: TA 5,732.84 mn − TCL 1,198.86 mn = 4,533.98 mn, converted) | 17.57% |
| FY26 | 83.12 (75.05+8.07) | 534.639 (Annual_Report_2026.txt p.~57: TA 6,383.89 mn − TCL 1,037.50 mn = 5,346.39 mn, converted) | 15.55% |

(All P&L inputs: screener-Data_Sheet.csv, PROFIT & LOSS block, rows "Profit
before tax" and "Interest".)

**A1 Median ROCE**: sorted {10.19, 10.36, 15.55, 17.57, 23.15, 38.68, 42.17},
median = **17.57%** → band 15-19.9% → **Score 3**

**A2 Minimum single-year ROCE**: **10.19% (FY20)** → band 8-11.9% → **Score 1**

**A3 Median ROE**: ROE = PAT ÷ avg Net Worth (opening+closing÷2); FY20 uses
closing only (no FY19 opening in corpus), stated.
Net Worth (Equity Share Capital + Reserves, screener-Data_Sheet): FY20=58.26,
FY21=59.91, FY22=72.40, FY23=102.10, FY24=146.81, FY25=434.51, FY26=489.77 (Cr).
PAT (screener-Data_Sheet "Net profit"): FY20=1.95, FY21=4.77, FY22=12.17,
FY23=30.93, FY24=44.88, FY25=48.03, FY26=55.21.
ROE: FY20=3.35% (closing NW only) | FY21=8.07% | FY22=18.40% | FY23=35.45% |
FY24=36.06% | FY25=16.53% | FY26=11.95%.
Median = sorted{3.35,8.07,11.95,16.53,18.40,35.45,36.06} = **16.53%** → band
15-19.9% → **Score 4**

**A4 ROCE trend, latest (FY26=15.55%) vs earliest (FY20=10.19%)**: latest ≥
earliest → **Score 5**. FLAG: this mechanical score masks a severe two-year
decline — ROCE peaked at 42.17% (FY24) and fell to 15.55% (FY26) as the
IPO more than tripled the equity/capital base (Net Worth 146.81 Cr FY24 →
489.77 Cr FY26, screener-Data_Sheet) while EBIT grew only 9% over the same
two years. The latest-vs-earliest test is blind to this because FY20 (the
earliest point) was itself a low-capital, low-ROCE year. See analyst_note.

**BLOCK A TOTAL: 3+1+4+5 = 13 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO (screener-Data_Sheet, "Cash from Operating Activity"): FY20=16.27,
FY21=1.31, FY22=17.54, FY23=41.75, FY24=8.25, FY25=8.64, FY26=27.75 (Cr).
Cross-checked against Annual_Report_2026.txt cash flow statement (offset
~10367): "Net cash flow from operating activities" FY26=277.52 mn (27.752
Cr, matches) and FY25=86.35 mn (8.635 Cr, matches).

Capex = Purchase of PP&E (incl. CWIP) + Purchase of Intangible assets, from
the cash flow statement:
- FY26: 995.35 + 6.42 = 1,001.77 mn = **100.177 Cr** (Annual_Report_2026.txt,
  offset ~10372-10378)
- FY25: 272.68 + 10.88 = 283.56 mn = **28.356 Cr** (same page)
- FY24: 216.23 + 0.77 = 217.00 mn = **21.70 Cr** (2024-09_Kross_Prospectus.txt,
  offset ~7353-7359, restated)
- FY23: 185.85 + 0.10 = 185.95 mn = **18.595 Cr** (prospectus, same table)
- FY22: 123.18 + 0 = 123.18 mn = **12.318 Cr** (prospectus, same table)
- FY20, FY21: NOT FOUND (not in provided data; prospectus restates only
  FY22-FY24). PROXY used: total "Cash from Investing Activity" outflow
  (screener-Data_Sheet) as a capex stand-in for these two years only —
  13.03 Cr (FY20), 10.48 Cr (FY21). Flagged: this proxy also captures
  investment purchases and overstates true capex slightly.

FCF = CFO − Capex:
FY20 = 16.27−13.03(proxy) = **3.24** | FY21 = 1.31−10.48(proxy) = **−9.17** |
FY22 = 17.54−12.318 = **5.222** | FY23 = 41.75−18.595 = **23.155** |
FY24 = 8.25−21.70 = **−13.45** | FY25 = 8.635−28.356 = **−19.72** |
FY26 = 27.752−100.177 = **−72.43**

**B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO = 121.51 Cr; ΣPAT = 197.94 Cr
(both screener-Data_Sheet, 7-year sums). Ratio = **0.614x** → band 0.50-0.69
→ **Score 1**

**B2 FCF-positive years as proportion**: 3 of 7 years positive (FY20, FY22,
FY23) = **42.9%** → band <50% → **Score 0**

**B3 Cumulative FCF ÷ Cumulative PAT**: ΣFCF = 3.24−9.17+5.222+23.155−13.45
−19.72−72.43 = **−83.14 Cr**; ÷ ΣPAT (197.94) = **−0.42x** → negative →
**Score 0**

**B4 Change in WC Days, latest vs earliest available (FY26 vs FY22)**:
WC Days = Receivable Days + Inventory Days − Payable Days, Sales basis
(no single COGS line in the data; Sales basis used throughout, stated).
Trade Payables sourced from Annual Report / Prospectus Note 20 (FY20-FY21
not available, so B4 uses FY22 as the earliest year, not FY20 — stated):
- Trade Payables (Cr, converted): FY22=19.162 (prospectus, offset ~28625-28630),
  FY23=34.043, FY24=48.751 (same table), FY25=67.361, FY26=59.799
  (Annual_Report_2026.txt Note 20, offset ~13755-13769).
- Receivables / Inventory (Cr): screener-Data_Sheet.

| FY | Rec Days | Inv Days | Pay Days | WC Days |
|----|----------|----------|----------|---------|
| FY22 | 61.77 | 50.75 | 23.51 | **89.01** |
| FY23 | 38.68 | 46.44 | 25.42 | 59.70 |
| FY24 | 64.65 | 49.15 | 28.69 | 85.11 |
| FY25 | 107.02 | 57.98 | 39.64 | 125.36 |
| FY26 | 106.92 | 57.24 | 32.43 | **131.73** |

Change FY26 vs FY22 = 131.73 − 89.01 = **+42.72 days (increase)** → band
increased >15 days → **Score 0**

**BLOCK B TOTAL: 1+0+0+0 = 1 / 20** — the weakest block by a wide margin.

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-Data_Sheet "Sales"): FY20=159.91 → FY26=673.2 Cr.
PAT (screener-Data_Sheet "Net profit"): FY20=1.95 → FY26=55.21 Cr.

**C1 Revenue CAGR (6 years, FY20→FY26)**: (673.2/159.91)^(1/6)−1 = **27.08%**
→ band ≥20% → **Score 5**

**C2 PAT CAGR (6 years, FY20→FY26)**: (55.21/1.95)^(1/6)−1 = **74.57%** →
band ≥20% → **Score 5**. FLAG: this figure is a base-effect artefact — FY20
PAT (1.95 Cr) was near break-even on a much smaller balance sheet; the CAGR
is real arithmetic but not representative of a repeatable growth rate. Noted
in data_notes, not suppressed.

**C3 Positive YoY revenue years proportion**: Revenue rose every year,
FY21 through FY26 (6 of 6 YoY comparisons positive, screener-Data_Sheet) =
**100%** → **Score 5**

**C4 PAT CAGR minus Revenue CAGR**: 74.57% − 27.08% = **+47.49pp** → band
≥+3pp → **Score 5**. Driven by the same base-effect noted at C2, plus real
operating leverage (EBITDA margin 10.37%→13.08%, see M1).

**BLOCK C TOTAL: 5+5+5+5 = 20 / 20 (max)**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

EBITDA FY26 = Operating Profit = PBT − Other Income + Depreciation + Interest
(computed; formula cross-checked against screener-Data_Sheet Quarters block,
where "Operating Profit" is given directly — e.g. Q4 FY26: PBT 30.06 − Other
Income 0.84 + Depreciation 2.47 + Interest 1.89 = 33.58, which matches the
stated Operating Profit 33.58 exactly). FY26 EBITDA = 75.05 − 4.17 + 9.08 +
8.07 = **88.03 Cr** (screener-Data_Sheet, PROFIT & LOSS block, FY26 column).

**D1 Net Debt ÷ EBITDA**: Net Debt = Borrowings 53.73 − Cash & Bank 23.74
(screener-Data_Sheet, FY26) = **29.99 Cr**. ÷ EBITDA 88.03 = **0.341x** →
band 0-1.0x → **Score 4**

**D2 Interest Coverage**: EBIT 83.12 ÷ Interest 8.07 (screener-Data_Sheet,
FY26) = **10.30x** → band ≥10x → **Score 5**

**D3 Debt ÷ Equity**: Borrowings 53.73 ÷ (Equity Share Capital 32.26 +
Reserves 457.51 = 489.77) = **0.110x** (screener-Data_Sheet, FY26) → band
0.1-0.5 → **Score 4**

**D4 Current Ratio**: Total current assets 3,587.25 mn ÷ Total current
liabilities 1,037.50 mn (Annual_Report_2026.txt, offset ~9984-9989 and
~10088-10090, FY26 column) = 358.725 ÷ 103.75 = **3.458x** → band ≥2.0 →
**Score 5**

**BLOCK D TOTAL: 4+5+4+5 = 18 / 20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20, latest = Jun-2026)

**E1 Promoter holding (latest quarter)**: **68.57%**
(SHP_30-JUN-2026_KROSS_NSE_xbrl.txt, "ShareholdingAsAPercentageOfTotalNumberOfShares
| ShareholdingOfPromoterAndPromoterGroup_ContextI") → band ≥60% → **Score 5**

**E2 Promoter holding change**: company listed 16-Sep-2024 (2.0 years before
run date); a true 3-year window does not exist. Available window used
instead (post-Offer at listing → Jun-2026), stated as a limitation:
- Post-Offer promoter+group holding at listing: **67.70%**
  (2024-09_Kross_Prospectus.txt, offset ~2020-2025, "Total holding of
  Promoters and Promoter Group (A+B)", post-Offer column)
- Latest (Jun-2026): 68.57% (as above)
- Change = **+0.87pp** over ~2 years → band ±1% → **Score 3**

**E3 Promoter pledge (latest)**: **0%** — XBRL field
"WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged" = false
(SHP_30-JUN-2026_KROSS_NSE_xbrl.txt) → band 0% → **Score 5**

**E4 Contingent liabilities ÷ Net Worth (latest)**: Total Contingent
Liabilities FY26 = 397.13 mn = **39.713 Cr** (Annual_Report_2026.txt, Note
34(A), offset ~14309-14330 — excise/service tax, sales tax/GST, income tax
disputes, and bills discounted with recourse). Net Worth FY26 = 489.77 Cr
(screener-Data_Sheet). Ratio = 39.713/489.77 = **8.11%** → band 5-15% →
**Score 3**

**BLOCK E TOTAL: 5+3+5+3 = 16 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — PEER RESCORE APPLIED

Peer Data_Sheet CSVs for AUTOAXLES, HAPPYFORGE, RKFORGE are now available
(inputs/screening/*-Data_Sheet.csv, INR Cr, same convention as KROSS).
JAMNAAUTO is a numbers-only reference comp and is shown for context but not
folded into "peer median" per the orchestrator's framing of the peer set.

**Peer EBITDA margin, FY26** (Operating Profit = PBT − Other Income +
Depreciation + Interest, same formula as KROSS, ÷ Sales; all figures from
each peer's Data_Sheet.csv, PROFIT & LOSS block, FY26 column):
- AUTOAXLES: OP = 219.8−20.19+35.89+1.57 = 237.07 ÷ 2,177.73 = **10.89%**
- HAPPYFORGE: OP = 401.99−30.81+89.04+10.47 = 470.69 ÷ 1,546.34 = **30.44%**
- RKFORGE: OP = 84.01−2.40+332.89+212.50 = 627.00 ÷ 4,238.08 = **14.79%**
- (reference) JAMNAAUTO: OP = 319.76+1.99+60.61+13.74 = 396.10 ÷ 2,611.59 =
  **15.17%**
- Peer median (3 peers) = sorted{10.89, 14.79, 30.44} = **14.79%**
- KROSS FY26 EBITDA margin (from Block D/M1) = **13.08%**

**Peer gross-margin proxy, FY26** ((Revenue − Raw Material Cost) ÷ Revenue,
same peer Data_Sheet source):
- AUTOAXLES: (2,177.73−1,453.82)/2,177.73 = **33.24%**
- HAPPYFORGE: (1,546.34−606.77)/1,546.34 = **60.75%**
- RKFORGE: (4,238.08−2,055.55)/4,238.08 = **51.51%**
- (reference) JAMNAAUTO: (2,611.59−1,602.86)/2,611.59 = **38.63%**
- Peer median (3 peers) = sorted{33.24, 51.51, 60.75} = **51.51%**
- KROSS FY26 GM proxy = **45.86%** (Block F, M9 basis)

**M1 Pricing Power**: EBITDA margin (OP÷Sales, computed, formula validated
against Quarters "Operating Profit"): FY20=10.37%, FY26=13.08% (expansion
+2.71pp, ≥2pp) AND Revenue CAGR 27.08% (≥10%) → **Score 5 (present)**

**M2 Cost Advantage vs peer median EBITDA margin** [RESCORED]: KROSS FY26
margin 13.08% vs peer median 14.79% = **1.71pp BELOW** peer median. Bands:
≥5pp above=5 | 2-5pp above=3 | ±2pp=1 | below=0. −1.71pp sits inside the
±2pp near-parity band → **Score 1** (was 0, PEER DATA NEEDED, in the first
pass).

**M3 Capital Efficiency**: FAT (Fixed Asset Turnover) FY26 = Sales 673.2 ÷
Net Block 207.44 (screener-Data_Sheet) = **3.246x** (>3x) but ROCE FY26 =
15.55% (not >20%, fails the top band). FAT >2x AND ROCE >15% → **Score 3
(present)**

**M4 Customer Stickiness**: zero revenue-decline years (see C3) but
receivable days ranged 38.68-107.02 over FY22-FY26 (not stable ±10) →
top band fails. Falls to "max 1 decline year, fully recovered" (0 decline
years satisfies "max 1" trivially) → **Score 3 (present)**

**M5 Scale & Dominance** [RESCORED]: Market Capitalization (screener
Data_Sheet META, run date pricing): KROSS 1,728.01 Cr is the SMALLEST of
the five names compared (AUTOAXLES 2,583.51 | JAMNAAUTO 5,527.79 | RKFORGE
13,073.41 | HAPPYFORGE 19,479.68 Cr). KROSS is not largest, not top 3.
Literally "top 5 mcap" is satisfied only because the comparison set itself
has exactly 5 names — this is a trivial pass, not evidence of scale, and is
flagged as such. → **Score 1** (was 0, PEER DATA NEEDED, in the first
pass), with the caveat that this is the weakest possible support for the
band and should not be read as a scale finding.

**M6 Technology / R&D**: R&D/Revenue is NOT FOUND (not in provided data;
no R&D line in any Data_Sheet, KROSS or peer, nor in the reviewed sections
of the Annual Report) → **Score 0** (peer data would not have resolved this
test; it needs an R&D disclosure that none of the four Data_Sheets carry)

**M7 Regulatory / License**: Kross is an unregulated discrete-manufacturing
business (trailer axles, suspension, forged/cast/machined components for
M&HCV/tractor OEMs — sector_cap_row_evidence, B00-inputs.yaml); no licence
or quota gate identified in the provided data → **Score 0**

**M8 Distribution**: reach/outlet data NOT FOUND in the provided
quantitative data (no Data_Sheet, KROSS or peer, carries a distribution
metric) → **Score 0**

**M9 Brand** [RESCORED]: Gross margin proxy (Revenue − Material Cost) ÷
Revenue: KROSS 45.86% vs peer median 51.51% = KROSS is **5.65pp BELOW**
peer median, not above. Bands all require KROSS to be AT OR ABOVE peer
median to score >0 ("above peers but growth below"=1, "at/below"=0). KROSS
is below → **Score 0** (unchanged from the first pass, but now backed by
an actual peer number instead of PEER DATA NEEDED).

**M10 Switching Costs**: revenue grew every year (top-band condition met)
but receivable days rose from 78.87 (FY20, screener-Data_Sheet: Receivables
34.56÷Sales159.91×365) to 106.92 (FY26) = **+28.05 days**, exceeding both
the ≤10-day (top band) and "stable" (middle band) thresholds, and there are
0 (not 2+) decline years for the next band down → no band fits → **Score 0**

**M11 Network Effects** (7 years available, ≥6-year test applies): latest
3yr revenue CAGR (FY23→FY26, 488.63→673.2) = **11.28%**; prior 3yr CAGR
(FY20→FY23, 159.91→488.63) = **45.12%**. Latest is NOT greater than prior —
growth is decelerating sharply, not accelerating → **Score 0**. FLAG: this
deceleration (45% CAGR in the first 3-year window to 11% in the most recent)
is a growth-quality signal worth carrying forward, distinct from the C1/C2
6-year CAGR which averages the two windows together.

**M12 Negative WC / Float**: WC Days (FY22-FY26, per B4) = 89.01, 59.70,
85.11, 125.36, 131.73 — all >45 days in every available year → **Score 0**

**Moats present (score ≥3): M1, M3, M4 = 3 of 12** (unchanged — M2 and M5
moved from 0 to 1, still below the ≥3 "present" threshold)

**BLOCK F TOTAL: 5+1+3+3+1+0+0+0+0+0+0+0 = 13 / 60** (was 11/60 before the
peer rescore)

**Moat classification: 3 present → MODERATE** (unchanged)

---

## SCORECARD SUMMARY

| Block | Score | Max |
|-------|-------|-----|
| A — Return on Capital | 13 | 20 |
| B — Cash Generation Quality | 1 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 18 | 20 |
| E — Shareholder Alignment | 16 | 20 |
| **Core Score** | **68** | **100** |
| F — Moat Score | 13 | 60 |
| **Grand Total** | **81** | **160** |

Moat class: **MODERATE** (3 of 12 tests present: M1 Pricing Power, M3
Capital Efficiency, M4 Customer Stickiness)

**Strongest block: C (Growth), 20/20.**
**Weakest block: B (Cash Generation Quality), 1/20 — by a wide margin.**

Peer read in one line: on FY26 EBITDA margin (13.08% vs peer median 14.79%)
and gross-margin proxy (45.86% vs peer median 51.51%), Kross sits BELOW
both peer medians — HAPPYFORGE and RKFORGE both carry materially higher
margins on the same FY26 base. This is consistent with, not contradictory
to, Block C's strong growth and Block D's strong balance sheet: Kross is
growing faster than at least AUTOAXLES and JAMNAAUTO off a smaller base,
but is not yet the margin leader in its peer set.

## DATA CONFIDENCE

7 years of annual data (FY20-FY26) → band 7-9 years → **moderate
confidence**, no downgrade tier triggered. One sub-metric family (WC Days
and everything derived from it: B4, M4, M10, M12) is backed by only 5 years
(FY22-FY26) because Trade Payables is unavailable for FY20-FY21 in the
corpus; this does not change the overall data-years count but is a named
limitation on those four tests specifically.

## DEAL-BREAKER OVERRIDES

Checked all nine:
1. Block A <8 → NOT TRIGGERED (Block A = 13)
2. **Block B <8 → TRIGGERED (Block B = 1). Caps classification at max GOOD.**
3. Median ROCE <10% → NOT TRIGGERED (median = 17.57%)
4. Cumulative CFO/PAT <0.50 → NOT TRIGGERED (0.614x), but close; the FY24-FY26
   trend alone (see below) is well under this line
5. Pledge >15% → NOT TRIGGERED (0%)
6. ND/EBITDA >3x AND IC <3x → NOT TRIGGERED (0.34x and 10.30x)
7. Revenue declined in majority of years → NOT TRIGGERED (0 decline years)
8. PAT negative in any of last 3 years → NOT TRIGGERED (FY24=44.88,
   FY25=48.03, FY26=55.21, all positive)
9. History <3 years → NOT TRIGGERED (7 years)

Only deal-breaker #2 fires. The base classification matrix (Core 68 [60-79
bracket] + MODERATE moat → GOOD) already lands at GOOD, so the deal-breaker
cap does not move the outcome further, but it is the reason GOOD (not GOOD+)
is the ceiling here regardless of the moat count. The peer rescore moved
the moat score (11→13/60) but not the moat class (still MODERATE, 3
present) and therefore not the classification.

## CLASSIFICATION

**Core 68 (60-79 bracket) + MODERATE moat → GOOD (base matrix)**
**Deal-breaker #2 (Block B <8) confirms cap at GOOD.**

**FINAL CLASSIFICATION: GOOD** (unchanged by the peer rescore)

## DECISION LINE

GOOD on the quant scorecard, driven almost entirely by growth (20/20) and a
strong post-IPO balance sheet (18/20, near-zero net debt, 3.46x current
ratio). The Core Score is dragged down by the weakest cash-generation block
in the whole scorecard (1/20): cumulative CFO covers only 61% of cumulative
PAT over 7 years, free cash flow was negative in 4 of the last 5 years and
turned sharply more negative as capex ramped (FY23 FCF +23.16 Cr → FY26 FCF
−72.43 Cr), and working-capital days rose 42.7 days FY22→FY26. Two further
mechanical-score artefacts do not show up in the totals: (a) ROCE peaked at
42.17% in FY24 and fell to 15.55% by FY26 purely because the IPO more than
tripled the capital base while EBIT grew only 9% over the same two years —
the A4 "latest≥earliest" test scores this a 5 because FY20 was itself a low
base; (b) the 6-year revenue/PAT CAGRs (27%/75%) blend a first 3-year window
running at ~45% CAGR with a second running at ~11% CAGR — real deceleration
that C1/C2 do not surface on their own. Now backed by peer data, the moat
picture (13/60, MODERATE, 3 of 12 present) adds one more finding: Kross's
FY26 EBITDA margin and gross-margin proxy both sit below the three-peer
median (AUTOAXLES, HAPPYFORGE, RKFORGE), so its growth is not yet
accompanied by margin leadership in its own peer set. This scorecard is
quantitative and mechanical only; it does not override any Section 1B,
mental-model, or FTTCP finding downstream, and it does not itself set a
verdict on the company beyond GOOD/quant-screen terms.

---
```yaml
stage: B01-gate0
company: "KROSS"
run_date: "2026-09-27"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Trade Payables not in provided data for FY20-FY21 (prospectus restates only FY22-FY24); WC Days, B4, M4, M10, M12 use FY22 as the earliest year instead of FY20."
  - "Capex (PP&E + intangibles) not in provided data for FY20-FY21; proxied with total investing-activity cash outflow for those two years only, flagged in the report."
  - "R&D/Revenue (M6) and distribution reach (M8) NOT FOUND in provided quantitative data (KROSS or peers)."
  - "Screener's own P&L/Balance Sheet/Cash Flow/Quarters CSV sheets came out empty; no screener-native ROCE/ROE anchor exists. All ratios are computed."
flags:
  - {type: FLAG-CASH, reason: "Block B cash-generation score is 1/20 and triggers deal-breaker #2 (Block B<8, caps classification at GOOD). Cumulative CFO/PAT 0.614x over 7 years; FCF negative in 4 of last 5 years, worsening from +Rs23.16 Cr (FY23) to -Rs72.43 Cr (FY26) as capex ramped; WC days rose 42.7 days FY22-FY26 (89.01 to 131.73). Consistent with company memory LBF2."}
  - {type: FLAG-ROCE-BASE-EFFECT, reason: "A4 scores 5 (latest ROCE 15.55% >= earliest 10.19%) but masks a real decline: ROCE peaked 42.17% in FY24 and fell to 15.55% by FY26 as the IPO more than tripled the capital base (Net Worth Rs146.81 Cr FY24 to Rs489.77 Cr FY26) while EBIT grew only ~9% over the same two years. Consistent with the post-IPO-rebase caution flagged in COMPANY MEMORY / B00-inputs.yaml."}
  - {type: FLAG-GROWTH-DECELERATION, reason: "M11 (Network Effects) shows latest 3yr revenue CAGR (FY23-FY26) of 11.28% versus prior 3yr CAGR (FY20-FY23) of 45.12%, a sharp deceleration the 6-year C1/C2 CAGRs (27.08%/74.57%) do not surface on their own."}
  - {type: FLAG-MARGIN-BELOW-PEER, reason: "Peer rescore (M2, M9): KROSS FY26 EBITDA margin 13.08% is 1.71pp below the 3-peer median (14.79%, AUTOAXLES/HAPPYFORGE/RKFORGE); KROSS FY26 gross-margin proxy 45.86% is 5.65pp below the 3-peer median (51.51%). Kross's growth is not yet accompanied by margin leadership in its own peer set."}
data_years: 7
fy_range: "FY20 to FY26"
blocks: {A: 13, B: 1, C: 20, D: 18, E: 16}
core_score: 68
moat_score: 13
grand_total: 81
moats_confirmed: 3
moat_class: "MODERATE"
classification: "GOOD"
deal_breakers: [2]
history_downgrade: false
data_notes:
  - "PAT CAGR (C2, 74.57%) and PAT-minus-Revenue CAGR (C4, +47.49pp) are inflated by a near-zero FY20 PAT base (Rs1.95 Cr); real but not a repeatable growth rate. No loss-to-profit swing occurred (PAT positive every year FY20-FY26)."
  - "Peer rescore applied (same run, correction from orchestrator): M2 moved 0->1 (KROSS FY26 EBITDA margin 13.08% vs 3-peer median 14.79%, -1.71pp, inside the +-2pp band); M5 moved 0->1 (KROSS is smallest of 5 names by market cap; 'top 5 mcap' band is trivially satisfied only because the comparison set has exactly 5 names, flagged as a weak pass); M9 stays 0 but is now backed by an actual number (GM proxy 45.86% vs 3-peer median 51.51%, -5.65pp, below peer median). JAMNAAUTO used as reference comp only, not folded into peer median. Moat score moved 11->13/60; grand total 79->81; moat class (MODERATE, 3 present) and final classification (GOOD) unchanged."
  - "Gross margin proxy used for M9: (Revenue - Raw Material Cost) / Revenue, screener-Data_Sheet, applied identically to KROSS and all three peers."
  - "EBITDA/Operating Profit formula (PBT - Other Income + Depreciation + Interest) validated against screener-Data_Sheet Quarters block, where Operating Profit is given directly and matches exactly (e.g. Q4 FY26: 33.58 computed = 33.58 stated); same formula applied to peer Data_Sheets for M2/M5."
  - "E2 (promoter holding change) uses a ~2-year window (listing Sep-2024 to Jun-2026), not 3 years, because Kross listed 16-Sep-2024. Promoter+group holding rose 67.70% (post-Offer, prospectus) to 68.57% (Jun-2026 XBRL), +0.87pp."
  - "Capital Employed for FY20-FY21 (Block A) is an approximation (Total Assets minus Data_Sheet 'Other Liabilities', which is not confirmed to be current-liabilities-only); FY22-FY26 use the classified balance sheet's actual Total Current Liabilities from the Prospectus and FY26 Annual Report, which is more precise."
block_b_trend: "deteriorating: FCF swung from +Rs23.16 Cr (FY23) to -Rs72.43 Cr (FY26) as capex ramped past CFO; WC days rose from 89.01 (FY22) to 131.73 (FY26)"
analyst_note: "GOOD is driven by growth (20/20) and balance-sheet strength (18/20, near-zero net debt), not by returns, cash quality, or margin leadership. Block B (1/20) is the scorecard's clearest signal and matches company memory LBF2 (cash conversion). Two mechanical scores understate real trends: A4 (ROCE trend) scores 5 on a latest-vs-earliest test but ROCE actually fell from a 42% FY24 peak to 15.55% FY26 as the IPO tripled capital employed while EBIT grew ~9%; M11 shows revenue CAGR decelerating from ~45% (FY20-23) to ~11% (FY23-26), which the smoothed 6-year C1 figure (27%) does not show. The peer rescore adds one more finding: KROSS's FY26 EBITDA margin and gross-margin proxy both sit below the 3-peer median (AUTOAXLES, HAPPYFORGE, RKFORGE) by 1.71pp and 5.65pp respectively, so growth is not yet paired with margin leadership. All are quant-screen findings only; downstream stages (mental model, Section 1B, FTTCP) should treat the post-IPO ROCE base, growth deceleration, and sub-peer margin as verification priorities, consistent with LBF1 (guidance vs delivery) already flagged in COMPANY MEMORY."
```
