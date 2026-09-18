# STAGE 1: GATE 0 SCORECARD — TruAlt Bioenergy Ltd (TRUALT)
Run date: 2026-09-18 | Model: claude-sonnet-5 | Mode: pipeline

Data available: 4 years (FY23 to FY26). Scoring adapted to 4-year history.
Company incorporated March 2021 (AR CIN note); FY23 is the first full
reporting year. Listed 03-Oct-2025. Audited annual statements exist only
for FY23-FY26 (prospectus restated FY23-FY25 + AR FY26 audited). This is
below the 5-year floor for "moderate" confidence; per the CLASSIFICATION
rules this run is LIMITED confidence (3-4 yrs), one-tier downgrade, and
also trips deal-breaker checks that are evaluated below (history <3 years
does NOT fire; 4 years clears that specific floor).

Units: all figures below are ₹ Cr unless marked otherwise. Source unit on
face of document: screener Data_Sheet = ₹ Cr; AR and prospectus = ₹ lakh
(converted ÷100 for display, original lakh cited in parens where it aids
verification).

Sources used:
1. inputs/screening/screener-Data_Sheet.csv ("screener Data_Sheet")
2. inputs/annual-report/Annual_Report_2026.txt ("AR p.N", consolidated
   unless marked "standalone")
3. inputs/prospectus/TRUALT-Prospectus-01OCT2025.txt ("prospectus p.N",
   restated consolidated FY24-FY25 / restated standalone FY23)
4. inputs/shareholding/TRUALT-SHP-June-2026.txt and -March-2026.txt
   ("SHP Jun-2026" / "SHP Mar-2026")
5. inputs/screening/GULPOLY-Data_Sheet.csv, BALRAMCHIN-Data_Sheet.csv,
   TRIVENI-Data_Sheet.csv ("GULPOLY screener", "BALRAMCHIN screener",
   "TRIVENI screener") — peer screener exports, ₹ Cr, added to
   DATA_SOURCES by orchestrator correction after the initial pass; used
   below for the three peer-comparison moat tests (M2, M5, M9).

---
## CROSS-CHECK: screener vs AR vs prospectus

Screener FY23-FY26 P&L and FY25/FY26 balance sheet figures were checked
against the AR (FY26 audited, consolidated) and the prospectus (FY23-FY25
restated). All of Sales, PBT, Interest, Depreciation, Other Income, PAT,
Total Assets and No. of Equity Shares tie out exactly year by year
(screener Data_Sheet; AR p.244-246; prospectus p.91-92). Screener is
confirmed to be reporting on a CONSOLIDATED basis throughout, including
FY23 (which the prospectus itself restates as standalone, since the
subsidiary/group structure only appears from FY24). This scorecard treats
the FY23 standalone-restated figures as the FY23 data point (no separate
consolidated FY23 exists).

One discrepancy found and resolved: the prospectus's restated FY25 CFO
(₹329.23cr, prospectus p.93) differs from the FY26 AR's FY25 comparative
CFO (₹342.03cr, AR p.247), because the AR's FY26 consolidation scope
(one more subsidiary, JV effects) differs slightly from the prospectus's
Aug/Sep-2025 restatement scope. Screener's FY25 CFO (342.03) matches the
AR figure. This scorecard uses the AR figure for FY25 wherever FY25 sits
alongside FY26 in the same calculation, to keep the comparison on one
consolidation basis; noted in data_notes.

---
## SPEAR LOAD-BEARING FACT 2 CHECK (cash conversion and IPO money)

Filed numbers confirm the fact as stated in companies/TRUALT.md:
- FY26 CFO: -₹295.63cr (screener Data_Sheet; AR p.247 states
  -29,562.92 lakh, consolidated).
- Inventory: ₹210.21cr (FY25) to ₹528.43cr (FY26) (screener Data_Sheet;
  AR p.244 consolidated balance sheet, Inventories 21,021.04 lakh to
  52,843.00 lakh).
- Borrowings: ₹1,556.54cr (FY25, screener) to ₹1,651.51cr (FY26,
  screener); AR p.244 splits this as non-current borrowings 98,868.12
  lakh + current borrowings 65,707.12 lakh + lease liabilities 575.88
  lakh = 1,65,151.12 lakh = ₹1,651.51cr, tying exactly.
- Fresh issue: AR note 60 (p.358) states gross fresh-issue proceeds of
  ₹75,000 lakh = ₹750cr (company memory's "₹751cr" is a close estimate,
  not the filed figure; filed figure is ₹750cr). Unutilised IPO proceeds
  at 31-Mar-2026 were ₹2,979 lakh (AR p.358).
All four data points are as filed. The fact holds: a year of heavy
inventory build and borrowing increase alongside negative CFO, in the
same year as the fresh issue.

---
## BLOCK A: RETURN ON CAPITAL (max 20)

ROCE = EBIT ÷ (Total Assets − Total Current Liabilities), year-end basis
(no average; opening capital-employed not usable because FY23 is the
first restated year and no FY22 balance sheet exists). EBIT = PBT +
Finance costs (interest), consistent across all four years and cross-
checked to tie (see cross-check section).

| FY | Total Assets | Current Liab | Capital Employed | EBIT | ROCE |
|----|---|---|---|---|---|
| FY23 | 1,855.98 (prospectus p.91, standalone restated) | 442.53 (prospectus p.91) | 1,413.45 | 84.30 (48.99+35.31, prospectus p.92) | 5.96% |
| FY24 | 2,419.08 (prospectus p.91, consol restated) | 1,061.48 (prospectus p.91) | 1,357.60 | 187.95 (44.87+143.08, prospectus p.92) | 13.85% |
| FY25 | 3,029.73 (prospectus p.91 / AR p.244) | 1,047.50 (prospectus p.91) | 1,982.23 | 303.05 (159.44+143.61, prospectus p.92) | 15.29% |
| FY26 | 3,778.34 (AR p.244) | 1,084.73 (AR p.244) | 2,693.61 | 289.97 (129.95+160.02, AR p.246) | 10.76% |

A1 Median ROCE = 12.30% (avg of 10.76 and 13.85, sorted series
5.96/10.76/13.85/15.29) → band 10-14.9% → **score 1**
A2 Minimum single-year ROCE = 5.96% (FY23) → <8% → **score 0**
A3 Median ROE = 13.67% (see below) → band 12-14.9% → **score 2**
A4 ROCE trend, latest (10.76%) vs earliest (5.96%): latest higher by
4.80pp → latest ≥ earliest → **score 5**

ROE = PAT ÷ average Net Worth (opening+closing÷2); FY23 uses closing
only (no FY22 opening figure available), stated per formula rule.

| FY | Opening NW | Closing NW | Avg NW | PAT | ROE |
|----|---|---|---|---|---|
| FY23 | n/a (use closing) | 240.49 (prospectus p.91) | 240.49 | 35.46 | 14.75% |
| FY24 | 240.49 | 264.61 (prospectus p.91) | 252.55 | 31.81 | 12.60% |
| FY25 | 264.61 | 769.00 (prospectus p.91 / AR p.244, parent equity) | 516.80 | 146.64 | 28.38% |
| FY26 | 769.00 | 1,520.33 (AR p.244, equity attributable to parent) | 1,144.67 | 95.95 | 8.38% |

**BLOCK A TOTAL = 8/20** (1+0+2+5)

---
## BLOCK B: CASH GENERATION QUALITY (max 20)

CFO (screener Data_Sheet, AR p.247 for FY26/FY25): FY23 233.49, FY24
35.48, FY25 342.03, FY26 -295.63. Cumulative CFO = 315.37.
PAT: FY23 35.46, FY24 31.81, FY25 146.64, FY26 95.95. Cumulative PAT =
309.86.

B1 Cumulative CFO ÷ Cumulative PAT = 315.37 / 309.86 = 1.018 → ≥1.00 →
**score 5**

Capex (Purchase of PPE incl. CWIP, net of capital advances where stated;
excludes the FY23 acquisition-of-distillery-business outflow of
₹873.04cr and the FY24 acquisition-of-subsidiary-shares outflow of
₹16.86cr, per the CAGR EDGE / FCF rule that excludes acquisitions):
FY23 275.54 (prospectus p.93), FY24 356.80 (prospectus p.93), FY25 259.60
(AR p.247, consistent with prospectus p.93's 259.60), FY26 510.68 (AR
p.247, "net of capital advances").

FCF = CFO − Capex:
FY23: 233.49 − 275.54 = **-42.05**
FY24: 35.48 − 356.80 = **-321.32**
FY25: 342.03 − 259.60 = **+82.43**
FY26: -295.63 − 510.68 = **-806.31**

B2 FCF-positive years = 1 of 4 (25%) → <50% → **score 0**
B3 Cumulative FCF ÷ Cumulative PAT = -1,087.25 / 309.86 = -3.51 →
negative → **score 0**

Working Capital Days = Receivable Days + Inventory Days − Payable Days,
all on a revenue basis (COGS not separately itemised as a single line in
any source, so the revenue-basis rule applies; stated per formula rule).
Trade payables from prospectus p.91 (FY23-FY25) and AR p.245 (FY26).

| FY | Recv Days | Inv Days | Pay Days | WC Days |
|----|---|---|---|---|
| FY23 | 41.4 (86.54/762.38) | 73.5 (153.49/762.38) | 147.8 (308.72/762.38) | **-32.9** |
| FY24 | 89.0 (298.21/1223.40) | 47.6 (159.48/1223.40) | 45.8 (153.62/1223.40) | **90.7** |
| FY25 | 64.9 (339.27/1907.72) | 40.2 (210.21/1907.72) | 92.9 (485.71/1907.72) | **12.2** |
| FY26 | 85.8 (406.11/1727.51) | 111.6 (528.43/1727.51) | 57.5 (272.11/1727.51) | **140.0** |

B4 Change latest (FY26, +140.0) vs earliest (FY23, -32.9) = +172.8 days
increase → increased >15 → **score 0**

**BLOCK B TOTAL = 5/20** (5+0+0+0)

block_b_trend: DETERIORATING. FY26 CFO -₹295.63cr against FY25 +₹342.03cr
(screener/AR) is the single number that shows it; WC days swung from
-32.9 to +140.0 over the same four years, entirely on an inventory build
(₹210.21cr → ₹528.43cr, screener/AR p.244).

Deal-breaker 2 (Block B <8) fires: caps at max GOOD. Deal-breaker 4
(cumulative CFO/PAT <0.50) does NOT fire (ratio is 1.018).

---
## BLOCK C: GROWTH (max 20)

Revenue: FY23 762.38, FY24 1,223.40, FY25 1,907.72, FY26 1,727.51
(screener Data_Sheet, all tie to AR/prospectus).
PAT: FY23 35.46, FY24 31.81, FY25 146.64, FY26 95.95.

C1 Revenue CAGR (FY23→FY26, 3yr) = (1,727.51/762.38)^(1/3)-1 = **31.4%**
→ ≥20% → **score 5**
C2 PAT CAGR (FY23→FY26, 3yr) = (95.95/35.46)^(1/3)-1 = **39.4%** → ≥20%
→ **score 5** (both endpoints positive, no N/M condition)
C3 Positive YoY revenue years: FY24 (+60.5%), FY25 (+56.0%), FY26
(-9.4%) → 2 of 3 positive = 66.7% → band 50-74% → **score 1**
C4 PAT CAGR − Revenue CAGR = 39.4 − 31.4 = **+8.0pp** → ≥+3pp →
**score 5**

**BLOCK C TOTAL = 16/20** (5+5+1+5)

Deal-breaker 7 (revenue declined in majority of years) does NOT fire (1
of 3 transitions declined, not a majority). Deal-breaker 8 (PAT negative
in any of last 3 years) does NOT fire at the annual level: FY24, FY25,
FY26 PAT are all positive.

data_note: annual PAT never swings negative, but FY26 carried two weak
quarters inside it — Q1FY26 (Jun-2025) PAT ₹4.73cr and Q2FY26 (Sep-2025)
PAT **-₹37.94cr** (screener quarters) — before recovering to ₹69.33cr
(Q3FY26) and ₹67.87cr (Q4FY26). The annual CAGR calculation is unaffected
(FY-level PAT stayed positive throughout), but this intra-year swing is
the concall-era volatility SPEAR fact 1 asks about; carried forward as
context, not as an annual data quality issue.

---
## BLOCK D: BALANCE SHEET STRENGTH (max 20, latest = FY26)

EBITDA (operating, excl. other income) FY26: summed from screener
quarterly Operating Profit (Sales − Expenses, ties exactly to quarterly
PBT identity: Q1 41.54 + Q2 -4.55 + Q3 134.00 + Q4 129.30 = **300.29**cr;
cross-check via annual PBT+Interest+Depreciation-OtherIncome =
129.95+160.02+86.23-86.45 = 289.75cr, consistent).

D1 Net Debt ÷ EBITDA: Net Debt = Borrowings 1,651.51 − Cash&Bank 89.77 =
1,561.74cr. ND/EBITDA = 1,561.74/300.29 = **5.20x** → >3x → **score 0**
D2 Interest Coverage = EBIT ÷ Interest = 289.97/160.02 = **1.81x** →
band 1.5-2.9x → **score 1**
D3 Debt ÷ Equity = 1,651.51 (screener, incl. lease liabilities) /
1,520.33 (AR p.244, equity attributable to parent) = **1.09x** → band
1.0-1.5x → **score 1**
D4 Current Ratio = Total Current Assets 1,478.75 (AR p.244) / Total
Current Liabilities 1,084.73 (AR p.244) = **1.36x** → band 1.2-1.49x →
**score 2**

**BLOCK D TOTAL = 4/20** (0+1+1+2)

**Deal-breaker 6 fires: Net Debt/EBITDA >3x (5.20x) AND Interest
Coverage <3x (1.81x), both true simultaneously → caps classification at
AVOID.** This is the binding constraint on this scorecard; see
CLASSIFICATION below.

---
## BLOCK E: SHAREHOLDER ALIGNMENT (max 20, latest = Jun-2026 quarter)

E1 Promoter holding (latest quarter) = 70.55% (SHP Jun-2026, category A
total) → ≥60% → **score 5**

E2 Promoter holding change over 3 years: NOT A CLEAN 3-YEAR SERIES. The
company listed 03-Oct-2025 (under one year of public float as of this
run). Pre-Offer promoter+group holding was 88.20% (prospectus p.24); the
prospectus's illustrative post-Offer table shows 52.75% at the upper
price band (prospectus p.24) — but that is a pre-listing projection, not
the actual outcome. The first REAL post-listing SHP on file (Mar-2026)
already shows 70.55%, unchanged through Jun-2026 (SHP Mar-2026, SHP
Jun-2026). Scored on the only comparable actual window available
(Mar-2026 to Jun-2026, both 70.55%, 0.00pp change) → ±1% → **score 3**.
The pre/post-IPO mechanical swing (88.20% → ~53-71%) is NOT a promoter
selling signal in the ordinary sense; it is IPO dilution and OFS. Flagged
in data_notes rather than scored as a decrease.

E3 Promoter pledge (latest) = 22,295,674 of 60,498,650 promoter shares =
**36.85%** of promoter holding pledged (SHP Jun-2026, category A row;
same figure at SHP Mar-2026) → >15% → **score 0**. (The SHP also reports
a second pledge ratio, 26.00%, which is pledged shares as a % of TOTAL
company shares outstanding, not promoter holding — used 36.85%, the
promoter-holding-denominator figure, as the standard convention and per
SPEAR fact 3's own framing.) AR p.357 (standalone related-party/security
note) confirms 2,22,95,674 shares were pledged on 06/11/19-Nov-2025 in
favour of lenders, replacing an earlier pledge released at IPO.

E4 Contingent liabilities ÷ Net Worth (latest): AR p.293 (consolidated,
note 57) and AR p.357 (standalone, note 57) both state: "does not have
any contingent liabilities and contingent assets as at 31 March 2026
(31 March 2025: Nil)." Ratio = 0% → <5% → **score 5**

**BLOCK E TOTAL = 13/20** (5+3+0+5)

Deal-breaker 5 (pledge >15%) fires: caps at max AVERAGE (superseded by
deal-breaker 6's AVOID, which is more restrictive).

---
## BLOCK F: QUANTITATIVE MOAT SCORING (max 60)

Peer screener data (GULPOLY, BALRAMCHIN, TRIVENI Data_Sheet.csv, ₹ Cr)
was added to DATA_SOURCES by orchestrator correction after the initial
pass and is used below for the three peer-comparison moat tests (M2, M5,
M9). All other tests use TRUALT's own filed data only, as before.

Peer comparison set (latest available annual FY per each peer's screener
export; GULPOLY's screener stops at FY25, BALRAMCHIN and TRIVENI carry
FY26): market cap (screener Data_Sheet, current price basis) TRUALT
₹3,635.48cr, BALRAMCHIN ₹14,297.64cr (FY26), TRIVENI ₹5,122.34cr (FY26),
GULPOLY ₹1,066.85cr (FY25).

EBITDA margin (operating, excl. other income; PBT+Interest+Depreciation
-Other Income, ÷ Sales, same method as TRUALT's Block D calc, latest FY
per peer):
- TRUALT FY26: (129.95+160.02+86.23-86.45)/1,727.51 = **16.77%**
- BALRAMCHIN FY26: (560.16+77.22+177.17-68.04)/6,271.15 = **11.90%**
- TRIVENI FY26: (364.14+100.20+144.16-59.86)/6,290.49 = **8.72%**
- GULPOLY FY25: (34.43+28.41+37.38-3.28)/2,019.67 = **4.80%**
Peer median (n=3, excl. TRUALT) = **8.72%** (BALRAMCHIN/TRIVENI/GULPOLY
sorted, TRIVENI is the median).

Gross margin proxy (Revenue − Raw Material Cost) ÷ Revenue, screener's
"Raw Material Cost" row used literally as Material Cost, consistently
across all four companies (proxy stated per the M9 instruction; Change
in Inventory excluded from the proxy since screener's sign convention for
that line is not comparable to a direct-materials cost across the four
sheets):
- TRUALT FY26: (1,727.51-1,257.11)/1,727.51 = **27.23%**
- GULPOLY FY25: (2,019.67-1,459.96)/2,019.67 = **27.71%**
- BALRAMCHIN FY26: (6,271.15-4,641.50)/6,271.15 = **25.99%**
- TRIVENI FY26: (6,290.49-4,712.49)/6,290.49 = **25.08%**
Peer median (n=3) = **25.99%** (BALRAMCHIN is the median).

M1 Pricing Power: EBITDA margin (operating, excl. other income) FY23
13.78% (105.05/762.38) → FY26 16.77% (289.75/1727.51), a **+2.99pp**
expansion, AND revenue CAGR 31.4% ≥10% → **score 5**
M2 Cost Advantage vs peer median EBITDA margin: TRUALT 16.77% vs peer
median 8.72% = **+8.05pp above** → ≥5pp above → **score 5**
M3 Capital Efficiency: FAT = Revenue/Net Block = 1,727.51/2,185.38
(screener FY26 Net Block) = **0.79x**, below the >1x floor → **score 0**
M4 Customer Stickiness: 1 revenue-decline year (FY26); no FY27 annual
data exists yet to confirm "fully recovered," and receivable days are
not stable (41→89→65→86, a >10-day swing in 3 of 3 transitions) →
neither the 5, 3 nor 1 bucket is cleanly met → **score 0**
M5 Scale & Dominance: by market cap among the four-company set, TRUALT
ranks 3rd of 4 (BALRAMCHIN > TRIVENI > TRUALT > GULPOLY) → within top 3
mcap; by EBITDA margin, TRUALT ranks 1st of 4 (16.77% > BALRAMCHIN
11.90% > TRIVENI 8.72% > GULPOLY 4.80%) → within margin top 2. TRUALT is
NOT the largest mcap (BALRAMCHIN is), so the top band does not apply;
"top 3 mcap AND margin top 2" is met → **score 3**
M6 Technology/R&D: no R&D line disclosed in the P&L; ethanol/distillery
manufacturing, not an R&D-intensive model → **score 0**
M7 Regulatory/License: ethanol pricing is OMC-administered, but the
listed peer set in this space (Balrampur Chini, Triveni, EID Parry,
Dalmia Bharat Sugar, Dhampur, Bajaj Hindusthan, Gulshan Polyols, and
others) is well over 10 listed players → regulated but >10 players →
**score 1**
M8 Distribution: company sells B2B direct to OMCs, no retail/distribution
network → **score 0**
M9 Brand: gross margin proxy 27.23% vs peer median 25.99% = **+1.24pp
above**. Positive but below the 5pp floor for the middle band; revenue
CAGR (31.4%) is well above the 8-10% thresholds in the higher bands, but
those bands require the margin gap itself to clear 5pp or 10pp first,
which it does not → falls to "above peers but growth below" catch-all →
**score 1**
M10 Switching Costs: revenue grew in 2 of 3 years (growth "all but 1
year") but receivable days rose 44.4 days FY23→FY26, not stable → does
not meet the "stable" condition for score 3, and does not have 2+ decline
years for score 1 → **score 0**
M11 Network Effects: only 4 years of data, below the 6-year minimum for
the two-window test; scored conservatively on overall trend — no network-
effect characteristics in a B2B commodity-fuel model → **score 0**
M12 Negative WC / Float: WC days negative in only 1 of 4 years (FY23);
not majority-negative, not consistently 0-15 or 15-45 either; the latest
year (FY26, 140.0 days) is firmly >45 → **score 0**

**BLOCK F TOTAL = 15/60** (M1=5, M2=5, M5=3, M7=1, M9=1, all others 0)

Moats "present" (score ≥3): M1, M2, M5. **moats_confirmed = 3** →
classification band "2-3 = MODERATE"

---
## SCORECARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 8 | 20 |
| B — Cash Generation Quality | 5 | 20 |
| C — Growth | 16 | 20 |
| D — Balance Sheet Strength | 4 | 20 |
| E — Shareholder Alignment | 13 | 20 |
| **Core (A-E)** | **46** | **100** |
| F — Quantitative Moat | 15 | 60 |
| **Grand Total** | **61** | **160** |

Moat profile: [M1=5][M2=5][M3=0][M4=0][M5=3][M6=0][M7=1][M8=0][M9=1]
[M10=0][M11=0][M12=0]
Moat classification: MODERATE (3 of 12 moats present, ≥3 threshold: M1
pricing power, M2 cost advantage vs peers, M5 scale/dominance)

Strongest block: C — Growth (16/20). Revenue and PAT both compounded at
over 30% over FY23-FY26, and PAT CAGR ran ahead of revenue CAGR.
Weakest block: D — Balance Sheet Strength (4/20). Net Debt/EBITDA of
5.20x and interest coverage of 1.81x are the two numbers that drive the
AVOID floor below.

---
## CLASSIFICATION AND OVERRIDES

Data confidence: 4 years (FY23-FY26) → band "3-4 LIMITED, downgrade
classification one tier."

Base classification from Core score: Core = 46 → band "Core 40-59 =
AVERAGE" (this band does not branch on moat class; moat class only
differentiates EXCELLENT/GOOD+/GOOD at Core ≥80 or Core 60-79). The
moat-score update (MODERATE, up from THIN) does not change the Core-band
outcome.

Deal-breaker overrides evaluated:
1. Block A <8? Block A = 8, exactly at the floor, NOT <8 → does not fire.
2. Block B <8? Block B = 5 <8 → **fires, caps at max GOOD.**
3. Median ROCE <10%? Median = 12.30%, NOT <10% → does not fire.
4. Cumulative CFO/PAT <0.50? Ratio = 1.018 → does not fire.
5. Pledge >15%? Pledge = 36.85% → **fires, caps at max AVERAGE.**
6. ND/EBITDA >3x (5.20x, true) AND Interest Coverage <3x (1.81x, true)?
   Both conditions true → **fires, AVOID.**
7. Revenue declined in majority of years? 1 of 3 transitions declined,
   not a majority → does not fire.
8. PAT negative in any of last 3 years? FY24/25/26 all positive → does
   not fire.
9. History <3 years? 4 years of audited history → does not fire.

The most restrictive deal-breaker (6) governs: **AVOID**. This is
unaffected by the peer-data correction: deal-breaker 6 is a Block D
(balance sheet) test, and Block D did not change. The LIMITED-confidence
one-tier downgrade has no further room to apply below AVOID (already the
floor above the withheld/no-score state), so it is recorded but does not
change the final letter.

**FINAL CLASSIFICATION: AVOID** (unchanged by the peer-data correction)

This is a mechanical scorecard output, not a company-quality halt (per
CLAUDE.md NEVER rules, no stage halts a run on company quality; flags
propagate and the decision stays with the operator). It is a factual
statement that FY26's balance sheet, on the two ratios the framework
tests, sits outside the framework's own AVOID threshold: net debt has
run to 5.2x a shrunk EBITDA base, and interest is covered only 1.8x, in
the same year working capital consumed ₹296cr of cash and the IPO
proceeds were largely absorbed. Growth (Block C, 16/20), shareholder
alignment ex-pledge (Block E, 13/20 driven by 70.55% promoter holding and
zero contingent liabilities), and now a MODERATE peer-verified moat
profile (Block F, 15/60: TRUALT runs the highest EBITDA margin and the
highest gross-margin proxy of the four-company comparison set, though
market cap ranks 3rd of 4) are the constructive counterweights the
operator should weigh against this floor at Halt 1.

---
## DECISION LINE

Gate 0 mechanical classification: **AVOID** (deal-breaker 6: ND/EBITDA
5.20x >3x AND Interest Coverage 1.81x <3x, FY26, both from filed
consolidated statements). Deal-breakers 2 (Block B <8, cash quality) and
5 (pledge 36.85% >15%) independently would have capped this at GOOD and
AVERAGE respectively; deal-breaker 6 is more restrictive and governs.
Core score 46/100 sits in the AVERAGE band pre-deal-breaker. Moat
classification MODERATE (3 of 12 present: pricing power, cost advantage
vs the peer set, and scale/dominance by margin rank), now peer-verified
against GULPOLY, BALRAMCHIN and TRIVENI screener data. History is 4
audited years, post-IPO (listed 03-Oct-2025), LIMITED confidence.
This is a flag for the operator's Halt 1 read, not a run-ending verdict;
CLAUDE.md's verdict set (PROCEED / PROCEED WITH CAVEATS / PROCEED WITH
FLAGS / REWORK / INSUFFICIENT EVIDENCE) is decided downstream, never by
Gate 0 alone.
