# STAGE 1: GATE 0 SCORECARD — CAPILLARY (Capillary Technologies India Ltd)
Run date: 2026-09-19 | Model: claude-sonnet-5 | Mode: pipeline

Data available: 6 years (FY21 to FY26) for revenue/PAT (screener-data,
consolidated). Balance-sheet current/non-current split needed for
Capital Employed and Working-Capital-Days is available only FY23 to FY26
(4 years): screener's Data_Sheet does not split current vs non-current
liabilities, and the UDRHP-I restated financials start at FY23. Scoring
adapted: Blocks C (growth) and most of E use the full 6-year window;
Block A (ROCE/ROE median/min/trend) and B4 (WC days) use the 4-year
FY23-FY26 window, noted at each line. Block D uses latest year (FY26)
only, per formula definition.

Units: all figures below in Rs Cr unless stated. Source filings are in
Rs million; conversions are shown at first use per line (10 INR
million = 1 Cr).

## LOAD-BEARING FACT CHECK (company memory, first verification priority)

LBF4 (cash conversion): CFO went from Rs -46.20 Cr (FY25) to Rs +149.91
Cr (FY26) (screener-data; cross-checked against AR Consolidated
Statement of Cash Flows, "Net cash generated/(used in) by operating
activities" Rs -461.99m / Rs 1,499.07m, AR p.193). Confirmed as stated
in company memory. Debtor days: computed at 98.3 (FY25) and 89.8 (FY26)
using Receivables/Revenue x 365 (screener-data), close to the "90" cited
in memory; AR's own Trade Receivable Turnover Ratio of 4.30x (FY26)
implies ~84.9 days on a different (average-receivables) base (AR p.82).
Net block (fixed assets) grew Rs 300.95 Cr (FY25) to Rs 460.17 Cr (FY26)
(screener-data), matching memory's "301 to 460". Capitalised development:
AR note 4 states Rs nil (FY26) / Rs 208.69m = Rs 20.87 Cr (FY25) was
capitalised from Intangible Assets Under Development (AR p.145 area,
note 4). Filed evidence: cash conversion improved sharply in the latest
year on an absolute basis, but Working Capital Days worsened over
FY23-FY26 (see B4 below), and the FY26 CFO improvement is helped by a
large payables build and a one-off Rs 24.96 Cr exceptional item sitting
in the same year's P&L (see below) — this is not a clean read of
recurring operating cash conversion.

LBF2(b) (other income): screener's annual "Other Income" FY26 = Rs 38.69
Cr (screener-data), of which Q4 FY26 alone was Rs 31.67 Cr
(screener-data quarterly row) — matches memory exactly. Filed evidence
(AR) shows this bundles two things: a true recurring "Other income" of
Rs 137.34m = Rs 13.73 Cr (AR consolidated P&L note 23, p.190) and a
separate Rs 249.60m = Rs 24.96 Cr one-off exceptional item, the Kognitiv
acquisition's churn-indemnity compensation (AR p.190, note IX / note 28).
13.73 + 24.96 = 38.69 Cr, reconciling exactly to screener's combined
figure. Q1 FY27 other income of Rs -27.68 Cr (screener quarterly row)
is confirmed by the Q1 FY27 results filing, which separately shows a Rs
333.86m = Rs 33.39 Cr exceptional expense from the Czech step-down
subsidiary cyber fraud (Results-Q1FY27-20260804.txt, exceptional items
note 9/10), consistent with memory's Rs 33.4 Cr figure. Both LBF4 and
LBF2 check out against the filings as described in company memory; the
detail added here is that the FY26 "clean" numbers (CFO, EBITDA margin)
need the one-off Kognitiv gain stripped out to read the recurring trend,
which this scorecard does for the moat block (M1).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Capital Employed = Total Assets - Total Current Liabilities, Rs Cr,
consolidated:
- FY23: 466.41 - 224.06 = 242.35 (UDRHP-I p.100: assets 4,664.13m,
  current liabilities 2,240.61m)
- FY24: 871.07 - 309.18 = 561.89 (UDRHP-I p.100: assets 8,710.68m,
  current liabilities 3,091.83m)
- FY25: 838.65 - 250.70 = 587.96 (UDRHP-I p.100 / AR p.189 cross-check:
  assets 8,386.54m, current liabilities 2,506.96m)
- FY26: 1,300.24 - 257.42 = 1,042.82 (AR p.189: assets 13,002.42m,
  current liabilities 2,574.21m)

ROCE = EBIT / Capital Employed. FY25 and FY26 use the AR's own published
ROCE (AR p.83, MD&A Key Financial Ratios) per the fixed-formula rule
allowing the source's own figure; FY23/FY24 are computed (EBIT = PBT +
Interest, screener-data):
- FY23: EBIT -81.49 (PBT -92.73 + Interest 11.24) / CE 242.35 = -33.63%
  (computed)
- FY24: EBIT -46.19 (PBT -63.90 + Interest 17.71) / CE 561.89 = -8.22%
  (computed)
- FY25: 4.56% (AR p.83, published)
- FY26: 8.82% (AR p.83, published)

A1 Median ROCE (4 values, FY23-FY26): sorted -33.63, -8.22, 4.56, 8.82;
median = -1.83%. <10% => **A1 = 0**
A2 Minimum single-year ROCE: -33.63% (FY23). <8% => **A2 = 0**
A3 Median ROE: Net Worth (screener-data, Equity + Reserves), Rs Cr: FY21
12.60, FY22 116.14, FY23 166.44, FY24 538.96, FY25 568.25, FY26 1,023.49.
ROE = PAT / average NW (opening FY21 unavailable, closing used per rule):
FY21 -22.83/12.60 = -181.19% (closing basis); FY22 -100.84/64.37 =
-156.63%; FY23 -87.72/141.29 = -62.09%; FY24 -56.99/352.70 = -16.16%;
FY25 = 2.40% (AR p.83, published); FY26 = 6.58% (AR p.83, published).
Median of 6 = -39.13%. <12% => **A3 = 0**
A4 ROCE trend, latest (FY26 8.82%) vs earliest (FY23 -33.63%): latest >
earliest => **A4 = 5**

**Block A total = 5 / 20**

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO (Rs Cr, screener-data, cross-checked to AR consolidated cash flow
p.193): FY21 1.18, FY22 7.16, FY23 -20.05, FY24 97.14, FY25 -46.20,
FY26 149.91. Cumulative CFO (FY21-FY26) = 189.14.
PAT (Rs Cr, screener-data): FY21 -22.83, FY22 -100.84, FY23 -87.72, FY24
-56.99, FY25 13.28, FY26 52.39. Cumulative PAT = -202.71 (net loss over
the window).

B1 Cumulative CFO / Cumulative PAT = 189.14 / -202.71: cumulative PAT is
negative, so the ratio is not meaningful as a coverage measure (a
positive cumulative CFO against a negative cumulative PAT signals
reported losses funded by non-cash charges, not "cash exceeding
earnings"). Scored at the floor per the <0.50 band. **B1 = 0** (data
note: denominator-sign anomaly, not a clean ratio)

Capex (purchase of PP&E + intangibles, Rs Cr, excl. acquisitions):
available FY23-FY26 only (UDRHP-I p.102 for FY23-FY25, AR p.193 for
FY26): FY23 28.20, FY24 36.93, FY25 47.46, FY26 39.37. FY21/FY22 capex
not in provided data (UDRHP restated cash flows start FY23) — marked
N/A, not estimated.

FCF = CFO - Capex, Rs Cr (FY23-FY26 only, the only years with capex
data):
- FY23: -20.05 - 28.20 = -48.25 (negative)
- FY24: 97.14 - 36.93 = 60.21 (positive)
- FY25: -46.20 - 47.46 = -93.66 (negative)
- FY26: 149.91 - 39.37 = 110.54 (positive)

B2 FCF-positive years as proportion (of the 4 years with data): 2 of 4 =
50%. 50-74% band => **B2 = 2**
B3 Cumulative FCF / Cumulative PAT (same FY23-FY26 window): Cumulative
FCF = -48.25+60.21-93.66+110.54 = 28.84. Cumulative PAT (FY23-FY26) =
-87.72-56.99+13.28+52.39 = -79.04 (negative). Ratio not meaningful for
the same reason as B1 (negative denominator); scored at the floor.
**B3 = 0** (data note: denominator-sign anomaly)

B4 Change in WC Days, latest (FY26) vs earliest available (FY23):
Receivable Days = Receivables/Revenue x 365 (screener-data): FY23 90.6,
FY24 101.2, FY25 98.3, FY26 89.8. Inventory Days = 0 (SaaS business, no
inventory line in any year; AR p.82 states Inventory Turnover "NA").
Payable Days = Trade Payables/Revenue x 365: trade payables Rs Cr FY23
58.86 (UDRHP-I p.394, note 20), FY24 72.83 (UDRHP-I p.394), FY25 50.58
(UDRHP-I p.394 / AR p.230 cross-check), FY26 74.38 (AR p.230, note 18).
Payable Days: FY23 66.6, FY24 50.6, FY25 30.9, FY26 37.0.
WC Days = Receivable Days + 0 - Payable Days: FY23 = 24.0, FY24 = 50.6,
FY25 = 67.4, FY26 = 52.8.
Change, latest (52.8) vs earliest (24.0) = +28.8 days, increased >15 =>
**B4 = 0**

**Block B total = 2 / 20**

block_b_trend: the latest-year absolute swing is an improvement (CFO
Rs -46.2 Cr FY25 to Rs +149.9 Cr FY26), but the underlying conversion
quality is deteriorating: WC Days rose from 24.0 (FY23) to 52.8 (FY26),
driven mostly by payable days compressing (66.6 to 37.0) rather than
receivable discipline improving, and cumulative FY21-FY26 CFO (Rs 189.1
Cr) sits against a cumulative PAT that is still net negative (Rs -202.7
Cr).

## BLOCK C: GROWTH (Max 20)

Revenue (Rs Cr, screener-data): FY21 170.91, FY22 223.07, FY23 322.68,
FY24 525.10, FY25 598.26, FY26 734.60.
PAT (Rs Cr): FY21 -22.83 ... FY26 52.39 (as above).

C1 Revenue CAGR, FY21-FY26 (n=5): (734.60/170.91)^(1/5)-1 = 33.88%.
≥20% => **C1 = 5**
C2 PAT CAGR: FY21 endpoint is negative (loss-to-profit swing, FY24 to
FY25: PAT was negative FY21-FY24, turned positive FY25 onward). Per
CAGR edge rule, marked N/M. **C2 = 0** (data note: loss-to-profit swing,
FY24 to FY25)
C3 Positive YoY revenue years: all 5 YoY periods (FY22 through FY26)
were positive = 100% => **C3 = 5**
C4 PAT CAGR minus Revenue CAGR: PAT CAGR is N/M => **C4 = 0** (per rule)

**Block C total = 10 / 20**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest year FY26 only)

D1 Net Debt / EBITDA: Borrowings Rs 44.7 Cr (AR p.81, MD&A narrative:
"total borrowings reduced to Rs447 million"), Cash & Bank Rs 359.05 Cr
(screener-data; AR MD&A also separately notes Rs 3,232.4m = Rs 323.24 Cr
placed in demand deposits during FY26, so liquid resources are wider
still). Net debt = 44.7 - 359.05 = -314.4 Cr => net cash. **D1 = 5**
D2 Interest Coverage = EBIT / Interest = 56.57 / 5.46 = 10.36x
(screener-data: EBIT = PBT 51.11 + Interest 5.46; matches AR consol
finance costs of Rs 54.64m = Rs 5.46 Cr). ≥10x => **D2 = 5** (note: AR's
own published "Interest Service Coverage Ratio" is 7.01x FY26 / 2.58x
FY25, AR p.83 — a different EBIT/finance-cost base; the fixed pipeline
formula, not the source's own ratio, governs this line per the formula
rules)
D3 Debt/Equity = 0.04 (AR p.82, MD&A Key Financial Ratios, published;
cross-check: 44.7/1,023.49 = 0.044, computed). <0.1 => **D3 = 5**
D4 Current Ratio = 2.80 (AR p.82, published; cross-check: 7,209.86m /
2,574.21m = 2.80, computed from AR p.189 balance sheet). ≥2.0 =>
**D4 = 5**

**Block D total = 20 / 20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

E1 Promoter holding, latest quarter (Jun 2026) = 51.45% (BSE-SHP-summary-
Jun2026.txt). 50-59.9% => **E1 = 4**
E2 Promoter holding change over 3 years: not computable. Capillary
listed 21-Nov-2025; BSE shareholding-pattern data provided covers only
Dec-2025 (52.28%), Mar-2026 (52.23%) and Jun-2026 (51.45%) — three
quarters, not three years, and the pre-listing entity was privately
held with a different cap-table structure (CTIPL holding company, per
company memory). Marked N/A (not in provided data). **E2 = 0**
E3 Promoter pledge, latest (Jun 2026): BSE-SHP-summary-Jun2026.txt
states "Whether any shares held by promoters are pledge or otherwise
encumbered? No." 0% => **E3 = 5**
E4 Contingent Liabilities / Net Worth, latest (FY26): AR note 34 (p.244)
discloses only a bank guarantee of Rs 3.91m = Rs 0.391 Cr as a
quantified contingent item; the note's narrative states claims and
assertions exist in the ordinary course but are assessed as not
material and are not separately quantified. Net Worth FY26 = Rs 1,023.49
Cr (screener-data). Ratio = 0.391/1,023.49 = 0.04%. <5% => **E4 = 5**
(data note: only the bank-guarantee line is quantified; unquantified
litigation-type contingencies are disclosed narratively only, not
estimated here)

**Block E total = 14 / 20**

---

## CORE SCORE = A(5) + B(2) + C(10) + D(20) + E(14) = 51 / 100

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin used below excludes screener's raw "Other Income" line,
which for FY26 bundles a one-off Rs 24.96 Cr Kognitiv churn-indemnity
exceptional gain (AR p.190, note IX/28) inside a Rs 38.69 Cr total
(screener-data). EBITDA = PBT + Interest + Depreciation - Other Income,
Rs Cr: FY21 -12.60 (-7.37% margin), FY22 -51.04 (-22.88%), FY23 -64.18
(-19.89%), FY24 -11.83 (-2.25%), FY25 64.97 (10.86%), FY26 92.85
(12.64%). Cross-check: this reconciles to AR's own disclosed EBITDA
(Rs 106.59 Cr FY26, Rs 78.57 Cr FY25, AR p.190) once AR's Rs 13.73 Cr
true recurring other income is removed (106.59 - 13.73 = 92.86 ~= 92.85).

M1 Pricing Power: EBITDA margin expanded from -7.37% (FY21) to 12.64%
(FY26), >>2pp, AND revenue CAGR 33.88% (≥10%). **M1 = 5**
M2 Cost Advantage vs peer median EBITDA margin: no peer (NEWGEN,
UNIECOM, INTELLECT) financial data was provided in this run's input
set. **M2 = 0, PEER DATA NEEDED**
M3 Capital Efficiency: FAT (Revenue/Net Block, FY26) = 734.60/460.17 =
1.60x; ROCE (FY26) = 8.82%. FAT >1x but ROCE not >12% => **M3 = 0**
M4 Customer Stickiness: zero revenue-decline years (all 5 YoY periods
positive), but Receivable Days moved from 117.1 (FY21) to 89.8 (FY26),
a 27-day change, outside a strict "stable +/-10" band for the top tier.
Decline-year count is 0 (<=1), satisfying the next tier. **M4 = 3**
M5 Scale & Dominance: requires peer mcap/margin ranking; no peer data
provided. **M5 = 0, PEER DATA NEEDED**
M6 Technology/R&D: no R&D or product-development spend ratio disclosed
in the AR or screener data (searched; no "Research and development"
line found). **M6 = 0, N/A (not in provided data)**
M7 Regulatory/License: SaaS business, unregulated/no licence regime.
**M7 = 0**
M8 Distribution: purely digital SaaS distribution, no physical network.
**M8 = 0**
M9 Brand: requires peer gross-margin comparison; no peer data provided.
**M9 = 0, PEER DATA NEEDED**
M10 Switching Costs: revenue grew every year, and Receivable Days moved
by -27.3 days (FY21 to FY26) which is <= the +10 day ceiling on the top
tier (a decrease also satisfies "rose <=10 days" literally). **M10 = 5**
M11 Network Effects (6 years available, two-window test used): latest
3yr revenue CAGR (FY23->FY26) = (734.60/322.68)^(1/3)-1 = 31.57%; prior
3yr CAGR (FY21->FY24) = (525.10/170.91)^(1/3)-1 = 45.39%. Latest is
lower than prior, so the top tier fails. Latest 3yr CAGR (31.57%) >=20%;
selling-expense trend used as a proxy (Selling & Admin + Other Expenses
combined, % of revenue) because the raw screener "Selling and admin"
line breaks in FY24 (Rs 2.49 Cr vs Rs 98.52 Cr FY23 and Rs 220.98 Cr
FY25, a categorization anomaly): combined series is 53.9% (FY21), 39.0%
(FY22), 32.5% (FY23), 50.5% (FY24), 39.7% (FY25), 39.2% (FY26) —
declining over the last two years and below the FY21 starting level, so
treated as "stable/declining". **M11 = 3**
M12 Negative WC/Float: WC Days (FY23-FY26) were 24.0, 50.6, 67.4, 52.8 —
none negative, and 3 of 4 years exceed 45 days. **M12 = 0**

**Moat score = 5+0+0+3+0+0+0+0+0+5+3+0 = 16 / 60**
Moats "present" (score >=3): M1, M4, M10, M11 = **4 confirmed**
Moat classification: 4-5 present = STRONG => **Moat class = STRONG**

---

## GRAND TOTAL = Core (51) + Moat (16) = 67 / 160

## DATA CONFIDENCE

6 years of P&L history (FY21-FY26) => "5-6 lower" band: flag "may not
have seen full cycle" — the company only turned PBT/CFO positive in
FY25/FY26 and has one post-IPO year of consolidated reporting; the
window has not seen a full demand or funding cycle. Separately, the
balance-sheet-dependent lines (Capital Employed for ROCE, WC Days) rely
on only 4 years (FY23-FY26) because screener-data does not split
current/non-current liabilities and UDRHP-I's restated financials start
at FY23; this narrower window is disclosed at each affected line rather
than applied as a blanket one-tier downgrade, since the overall P&L
window (6 years) does not itself fall in the 3-4 year LIMITED band.
**history_downgrade = false**

## DEAL-BREAKER OVERRIDES

1. Block A < 8 (score 5) -> cap GOOD. Non-binding (actual class already
   below GOOD).
2. Block B < 8 (score 2) -> cap GOOD. Non-binding.
3. Median ROCE < 10% (-1.83%, FY23-FY26 basis) -> cap AVERAGE. Binding.
4. Cumulative CFO/PAT < 0.50 (cumulative PAT FY21-FY26 is net negative,
   Rs -202.71 Cr, against cumulative CFO of Rs +189.14 Cr) -> cap
   AVERAGE. Binding.
8. PAT negative in FY24 (Rs -56.99 Cr), one of the last three fiscal
   years FY24-FY26 -> cap AVERAGE. Binding. Years driving this: FY24.

Not triggered: #5 pledge (0%), #6 ND/EBITDA + IC (net cash, 10.36x
coverage), #7 revenue decline (none), #9 history <3 years (6 years of
P&L exist).

## CLASSIFICATION

Core score 51 falls in the 40-59 band => **AVERAGE**, independently
confirmed by deal-breakers #3, #4 and #8 above (each also caps at
AVERAGE). The STRONG moat class (4/12 confirmed) does not lift the
classification, since the matrix only applies moat class as a modifier
at Core >=60.

**Classification: AVERAGE**

Strongest block: **D (Balance Sheet Strength), 20/20** — but this
reflects one-time IPO cash and near-zero debt post-listing (Nov-2025),
not operating deleveraging built over time.
Weakest block: **B (Cash Generation Quality), 2/20** — driven by the
FY21-FY24 loss years dragging cumulative cash-to-earnings ratios
negative, and by worsening Working Capital Days even in the profitable
FY25-FY26 years.

## FLAGS

- FLAG-GATE0: classification is AVERAGE (Core 51/100) with historical
  depressors clearly identified: four consecutive loss years FY21-FY24
  (deal-breaker #8, PAT negative FY24), median ROCE still below 10% on
  the only balance-sheet years available (deal-breaker #3), and a
  cumulative cash-to-earnings ratio distorted by the same loss years
  (deal-breaker #4). The FY25-FY26 inflection is real (PBT, CFO, ROCE,
  EBITDA margin all turned positive/expanded) but is only two years
  deep and the latest year (FY26) carries a one-off Rs 24.96 Cr
  exceptional gain that inflates headline PAT and other income.
- FLAG-CASH: Working Capital Days worsened from 24.0 (FY23) to 52.8
  (FY26) even as absolute CFO improved sharply; the FY26 CFO
  improvement leans on payable-days compression (66.6 to 37.0 days)
  rather than receivable discipline, and cumulative FY21-FY26 CFO
  (Rs 189.1 Cr) still sits against a net cumulative loss (Rs -202.7 Cr
  PAT).

## DECISION LINE

Gate 0 mechanical score: AVERAGE (67/160, Core 51/100, moat STRONG
4/12). Three deal-breakers bind, all rooted in the FY21-FY24 loss
history; the FY25-FY26 turn is evidenced but short and carries a
one-off item. Flags propagate; this is not a halt. Per pipeline rule,
company quality never halts a run — the classification and flags above
carry forward to Halt 1 for the operator's read.

---
