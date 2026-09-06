# STAGE 1: GATE 0 QUANTITATIVE SCORECARD
Company: Ceigall India Ltd (CEIGALL) | Run date: 2026-09-06 | Model: claude-sonnet-5

Data available: 6 years (FY2021 to FY2026) for the revenue/PAT/cash-flow
series (screener Data_Sheet). Balance-sheet granularity needed for
capital-employed and payables (current liabilities, trade payables) is
available for only 3 years (FY2024 to FY2026), sourced from the Investor
Presentation, because the Annual Report text extraction is unusable (see
DATA QUALITY NOTE below) and the screener CSV lumps "Other Liabilities"
without a current/non-current split. Scoring is adapted: 6-year history
used wherever the screener P&L/BS/CF series alone suffices (Blocks B1,
C, receivable-day trend); a 3-year FY2024-FY2026 sub-window is used for
every metric that needs capital employed or trade payables (A1, A2, A4,
D1-D4, the payables leg of B4).

## DATA QUALITY NOTE (read before the scorecard)
The provided Annual Report file (`annual-report__Annual_Report_2026.txt`,
source PDF `Annual_Report_2026.pdf`) is unusable: of its 151 pages, page 1
is a garbled/mojibake extraction (unreadable, likely a cover letter using a
custom font with no ToUnicode map) and pages 2-151 are blank. No figure in
this scorecard is drawn from the Annual Report. Of the six screener CSVs
supplied, only `screener-Data_Sheet.csv` is populated; `Profit_Loss`,
`Balance_Sheet`, `Cash_Flow`, `Quarters`, and `Customization` are empty
templates. Where the screener Data_Sheet lacks a needed breakdown
(current liabilities, trade payables, EBIT, current assets), this stage
uses the Investor Presentation's audited-figure tables (pp.34, 36-41),
which were cross-checked against the screener Data_Sheet and reconcile
almost exactly on Total Assets, Net Worth, Borrowings, and EBIT (see
inline notes). This is a genuine input gap, not a preference; it is
carried to input_gaps below.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 13/20

**A1. Median ROCE = 19.21% → Score 3** (band 15-19.9%)
ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed per the fixed
formula (screener Data_Sheet does not populate its own ROCE field; the
Balance_Sheet.csv "Return on Capital Emp" row is blank). Computable only
for FY2024-FY2026, the only years with a Total Current Liabilities figure
(Investor Presentation, consolidated balance sheet, p.39).
- FY2024: EBIT 499.50 Cr (PBT 405.35 + Interest 94.15, screener-data) ÷
  CE 1,561.8 Cr (Total Assets 2,592.2 screener-data − Current Liabilities
  1,030.4 Cr [Investor Presentation p.39]) = **31.98%**
- FY2025: EBIT 518.95 Cr (PBT 384.59 + Interest 134.36, screener-data) ÷
  CE 2,701.93 Cr (TA 4,247.83 screener-data − CL 1,545.9 Cr [Investor
  Presentation p.39]) = **19.21%**
- FY2026: EBIT 577.99 Cr (PBT 417.62 + Interest 160.37, screener-data) ÷
  CE 3,264.76 Cr (TA 5,523.36 screener-data − CL 2,258.6 Cr [Investor
  Presentation p.39]) = **17.71%**
Median of the 3 available years = 19.21%.
Cross-check: Investor Presentation's own ROCE chart (p.36) shows 32.0% /
19.0% / 20.0% for FY24/FY25/FY26 — matches our computed figures closely
for FY24-25 but diverges 2.3pp for FY26 (computed 17.71% vs disclosed
20.0%), plausibly because FY2026 consolidated assets/liabilities include
an INR 5,431mn "held for sale" HAM asset and its matching INR 3,303mn
liability (Investor Presentation p.39) that the company may exclude from
its own capital-employed base. Scored on the fixed-formula computed
figure per the rule ("compute only when absent"), not the company chart.

**A2. Minimum single-year ROCE = 17.71% (FY2026) → Score 5** (band ≥15%)

**A3. Median ROE = 33.42% → Score 5** (band ≥20%)
ROE = PAT ÷ average Net Worth (opening + closing ÷ 2); FY2021 uses
closing only (no FY2020 opening net worth in the data).
Net Worth (screener-data, Equity Share Capital + Reserves): FY21 305.29,
FY22 431.25, FY23 593.06, FY24 887.73, FY25 1,832.59, FY26 2,138.14 (Cr).
- FY21: 112.5 ÷ 305.29 (closing only) = 36.85%
- FY22: 125.86 ÷ 368.27 (avg) = 34.17%
- FY23: 167.27 ÷ 512.16 (avg) = 32.66%
- FY24: 306.14 ÷ 740.40 (avg) = 41.35%
- FY25: 294.02 ÷ 1,360.16 (avg) = 21.62%
- FY26: 311.89 ÷ 1,985.37 (avg) = 15.71%
Median of 6 years = (32.66+34.17)/2 = 33.42%.
Note the steep fall to 15.71% in FY26 as the post-IPO equity base
(net worth roughly 7x FY21) dilutes returns — flagged in analyst_note.

**A4. ROCE trend, latest vs earliest (available window FY24→FY26) → Score 0**
(decline >5pp)
17.71% (FY26) vs 31.98% (FY24) = decline of 14.27pp. This is the sharpest
depressor in Block A: post-listing capital deployed (HAM equity, working
capital) has not yet earned its keep at FY2024's rate.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 5/20

**B1. Cumulative CFO ÷ Cumulative PAT = −0.70 → Score 0** (band <0.50)
CFO by year (screener-data, Cash Flow section): FY21 103.18, FY22
−134.59, FY23 −72.66, FY24 −210.83, FY25 −519.56, FY26 −91.28. Cumulative
CFO (FY21-FY26) = **−925.74 Cr**.
PAT by year (screener-data): 112.5, 125.86, 167.27, 306.14, 294.02,
311.89. Cumulative PAT = **1,317.68 Cr**.
Ratio = −925.74 ÷ 1,317.68 = **−0.7026**. Five of six years show CFO
negative despite PAT positive every year — the central finding of this
scorecard (deal-breaker #4 triggers, see below).

**B2. FCF-positive years as proportion → N/A, Score 0**
FCF requires Capex = purchase of PPE + intangibles from the cash flow
statement (fixed formula, excl. acquisitions). No provided source breaks
this out: screener Data_Sheet gives only aggregate "Cash from Investing
Activity" (−19.62, −163.59, −133.85, −38.16, −129.89, −43.92 Cr,
FY21-FY26); the Investor Presentation cash flow statement (p.40) likewise
gives only the aggregate investing-activity total, not a capex sub-line.
Concall guidance (Concall Feb 2026 Transcript p.11: "close to 25 to 30
crores"; Concall Aug 2026 Transcript p.8: "close to INR30 crores-INR35
crores" full-year FY26 guidance) is qualitative guidance, not an audited
cash-flow-statement line, and is not substituted per rule 5. Marked N/A
(not in provided data); scored 0.

**B3. Cumulative FCF ÷ Cumulative PAT → N/A, Score 0**
Same capex-breakdown gap as B2. Marked N/A; scored 0.

**B4. Change in WC Days, latest vs earliest available window → Score 5**
(decrease >5 days)
WC Days = Receivable Days + Inventory Days − Payable Days, Revenue basis
(COGS not explicitly available as a single line in any source, so Revenue
basis used throughout, as the fixed rule requires when COGS is absent).
Trade Payables are available only FY2024-FY2026 (Investor Presentation
consolidated balance sheet, p.39: micro/small + other creditors); no
payables figure exists for FY2021-FY2023 in any provided source.
- FY2024: Receivable Days 51.79 (Receivables 429.79 ÷ Sales 3,029.35 ×
  365, screener-data) + Inventory Days 14.25 (118.25 ÷ 3,029.35 × 365,
  screener-data) − Payable Days 41.41 (Trade Payables 343.6 Cr [743+2,693
  mn, Investor Presentation p.39] ÷ 3,029.35 × 365) = **24.63 days**
- FY2025: 71.79 + 11.01 − 80.06 (Payables 753.7 Cr [410+7,127mn]) =
  **2.74 days**
- FY2026: 57.72 + 9.00 − 133.53 (Payables 1,471.3 Cr [1,040+13,673mn]) =
  **−66.81 days**
Change, FY2026 vs FY2024 = −66.81 − 24.63 = −91.44 days → decreased
>5 days → Score 5.
**IMPORTANT ARCHETYPE CAVEAT**: this formula-defined WC-days figure is
favourable only because it excludes Contract Assets / WIP (unbilled
revenue), which is not part of the fixed Receivable+Inventory−Payable
formula but is the dominant working-capital item for an EPC/HAM
contractor. Contract Assets (consolidated, Investor Presentation p.39)
grew from 402.8 Cr (FY24) to 873.3 Cr (FY25) to 1,413.2 Cr (FY26) — a
3.5x increase, the real driver of the deeply negative CFO in B1. The
company's own "Net Working Capital Days" chart (Investor Presentation
p.41, which does include WIP: Inventory+Debtor+WIP−Creditor) shows
45 / 67 / 49 days for FY24/25/26 — worse and non-improving versus this
scorecard's formula-mandated 24.6 / 2.7 / −66.8. **The B4 score of 5 is
mechanically correct per the fixed formula but is not representative of
the true cash-conversion picture for this archetype; B1's −0.70 ratio is
the reliable signal.**

---

## BLOCK C: GROWTH (Max 20) — Score: 15/20

**C1. Revenue CAGR (FY2021→FY2026, 5yr) = 35.73% → Score 5** (band ≥20%)
(4,022.4 ÷ 873.2)^(1/5) − 1, screener-data.

**C2. PAT CAGR (FY2021→FY2026, 5yr) = 22.62% → Score 5** (band ≥20%)
(311.89 ÷ 112.5)^(1/5) − 1, screener-data.

**C3. Positive YoY revenue years = 5/5 (100%) → Score 5**
Revenue rose every year FY22-FY26 versus the prior year (screener-data).

**C4. PAT CAGR minus Revenue CAGR = 22.62 − 35.73 = −13.11pp → Score 0**
(band <−8pp)
Growth is genuine and broad-based, but profit has not kept pace with
revenue — consistent with the OPM compression noted under M1 below
(margin fell from 18.30% FY21 to 14.43% FY26, screener-data-derived).

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY2026) — Score: 12/20

**D1. Net Debt ÷ EBITDA = 1.59x → Score 3** (band 1-2x)
Net Debt = Borrowings 1,311.14 Cr (screener-data) − Cash & Bank 378.68 Cr
(screener-data) = 932.46 Cr.
Operating EBITDA (excl. other income) = EBIT 577.99 − Other Income 54.26
+ Depreciation 61.7 = 585.43 Cr (screener-data-derived; matches Investor
Presentation's own consolidated EBITDA of 585.4 Cr, p.37, exactly).
932.46 ÷ 585.43 = 1.593x.

**D2. Interest Coverage (EBIT ÷ Interest) = 3.61x → Score 2** (band 3-4.9x)
577.99 ÷ 160.37 (screener-data).

**D3. Debt ÷ Equity = 0.61x → Score 3** (band 0.5-1.0x)
Borrowings 1,311.14 ÷ Net Worth 2,138.14 (screener-data) = 0.6133.
Cross-check: Investor Presentation's own consolidated D/E chart (p.34)
shows 0.6x for FY26 — matches.

**D4. Current Ratio = 1.61x → Score 4** (band 1.5-1.99x)
Total Current Assets 36,255mn ÷ Total Current Liabilities 22,586mn
(Investor Presentation consolidated balance sheet, p.39) = 1.605.
Screener Data_Sheet has no current-asset/current-liability split; this
metric is Investor-Presentation-sourced only, no screener cross-check
possible.

Deal-breaker #6 check (ND/EBITDA>3x AND IC<3x): 1.59x and 3.61x — neither
leg trips; deal-breaker #6 NOT triggered.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 0/20

**E1-E4: all N/A (not in provided data) → Score 0 each**
No shareholding pattern file is in this corpus (confirmed absent per
stage-0 input_gaps; confirmed by search — no promoter/pledge/FII/DII
mention anywhere in the screener CSVs, Investor Presentation, or the
three concall transcripts). Contingent liabilities (E4) are disclosed
only in Annual Report notes, which are unreadable (see DATA QUALITY
NOTE). This entire block is a hard data gap, not a demonstrated
weakness — carried to input_gaps, not to be read as a governance
red flag.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 12/60

Peer set used (screener Data_Sheet, FY2026 unless noted): H.G. Infra
Engineering (HGINFRA), KNR Constructions (KNRCON), PNC Infratech
(PNCINFRA). This is a limited, named 3-peer set, not an exhaustive listed
universe (larger players such as KEC, IRB, Dilip Buildcon, GR
Infraprojects, Ashoka Buildcon are not in the corpus) — noted wherever
this limits a test.

**M1 Pricing Power → Score 1** (margin declined 2-5pp despite growth)
OPM FY21 18.30% → FY26 14.43% (screener-data-derived, Sales less all
operating expense lines each year), decline of 3.87pp, while Revenue
CAGR is 35.73% (≥10%).

**M2 Cost Advantage vs peer median EBITDA margin → Score 0** (below peers)
FY26 OPM: CEIGALL 14.43%; HGINFRA 19.37% (screener-data); KNRCON 26.37%
(screener-data); PNCINFRA 21.17% (screener-data). Peer median = 21.17%.
CEIGALL sits 6.74pp below the peer median, and is the lowest margin of
the four. Peer OPM cross-checked against each peer's own quarterly
Operating Profit sum (screener-data, Quarters row) and matches exactly
for all three, so the ranking is reliable despite a categorization
artifact in the FY26 sub-line items (see data_notes).

**M3 Capital Efficiency → Score 3** (FAT >2x AND ROCE >15%)
Fixed Asset Turnover = Sales 4,022.4 ÷ Net Block 341.15 (screener-data)
= 11.79x. ROCE (computed, A1) = 17.71% FY26. Both clear the FAT>2x/
ROCE>15% tier; the FAT>3x/ROCE>20% top tier is not clearly met (ROCE
17.71-20.0% depending on basis, see A1 cross-check note), so scored
conservatively at the middle tier.

**M4 Customer Stickiness → Score 3** (zero decline years, but receivable
days not stable — scored at the "max 1 decline year" tier since zero
decline years is at least as good)
Zero revenue-decline years (C3). Receivable Days (screener-data,
Revenue basis): FY21 15.12, FY22 30.90, FY23 55.83, FY24 51.79, FY25
71.79, FY26 57.72 — a 56.7-day swing, not stable within ±10 days, so
the top tier (5) is not met.

**M5 Scale & Dominance → Score 1** (top-5 mcap only, within the limited
peer set)
Market cap (screener-data): CEIGALL 6,198.21 Cr — largest of the four —
but CEIGALL's FY26 OPM (14.43%) is the LOWEST of the four, so the
"top margin among top 3" condition for the 5-tier and the "margin top 2"
condition for the 3-tier both fail. Scored at the "top 5 mcap" tier only.
Peer set limited to 3 names (see Block F header); a fuller segment
comparison could change this score — noted, not scored as PEER DATA
NEEDED since the 3-name comparison was performed.

**M6 Technology/R&D → Score 0** (not applicable to archetype; no R&D
line in any provided source for a road-EPC/HAM contractor)

**M7 Regulatory/License → Score 1** (regulated — NHAI/MoRTH contracts
and HAM concessions — but far more than 10 listed players compete in
Indian road EPC/HAM; the named peer set alone is 3 of dozens)

**M8 Distribution → Score 0** (not applicable; EPC/HAM contractor has
no retail distribution network)

**M9 Brand (GM proxy) → Score 1** (above peers, gap below the scored
thresholds)
GM proxy = (Revenue − Material Cost) ÷ Revenue. FY2026 screener Raw
Material Cost lines are unusable for this cross-company test (see
data_notes: CEIGALL's FY26 "Raw Material Cost" row of 3,279.96 Cr
absorbs several normally-separate cost lines, and KNRCON/PNCINFRA show
a similar FY26 categorization shift). FY2025 used instead, the last year
with cleanly split cost lines for all four companies:
CEIGALL 70.41% ((3,436.73−1,016.86)/3,436.73); HGINFRA 53.08%; KNRCON
69.15%; PNCINFRA 69.85% (all screener-data). Peer median = 69.15%.
CEIGALL is 1.26pp above the peer median — above, but well short of the
5pp threshold for score 3 — while revenue growth is strong (not below).
Scored at the lower "above peers but growth below" tier as the closest
described state, since neither explicit condition (≥5pp above, or
"at/below peers") fits; flagged as a judgment call.

**M10 Switching Costs → Score 0**
Revenue grew every year (best case for the growth leg), but Receivable
Days rose from 15.12 (FY21) to 57.72 (FY26), a 42.6-day increase, far
above the ≤10-day threshold for the top two tiers. No listed tier
matches this combination (uniform growth + large receivable-day
deterioration) cleanly; scored 0 as the closest fit given the receivable
deterioration is the dominant signal.

**M11 Network Effects → Score 1** (two-window test; exactly 6 years,
the minimum for this test)
Prior 3yr window (FY21→FY23, 2 intervals): Revenue CAGR = (2,068.17 ÷
873.2)^(1/2) − 1 = 53.90% (screener-data). Latest 3yr window (FY24→FY26,
2 intervals): (4,022.4 ÷ 3,029.35)^(1/2) − 1 = 15.23% (screener-data).
Latest window is LOWER than prior (decelerating), so the top tier fails.
Latest-window CAGR of 15.23% is just above the 15% "growth >15% but
selling% rising" tier threshold; Selling & Admin as % of Sales rose from
1.68% (FY24) to 1.84% (FY25) (screener-data) — FY26 not separately
available (same lumping issue as M2/M9). Scored 1, conservatively, given
the incomplete FY26 selling-expense split.

**M12 Negative WC/Float → Score 1**
Only 3 years of WC-days-with-payables exist (B4): FY24 +24.63, FY25
+2.74, FY26 −66.81. Only 1 of 3 years is negative (not "majority"); no
band describes a consistent pattern across this volatile 3-year run.
Scored 1 as the closest fit to the mixed evidence; the caveat under B4
(this excludes ballooning Contract Assets/WIP, the true working-capital
driver) applies here too — the true float position is materially worse
than this narrow metric shows.

**Moat tally: M1=1, M2=0, M3=3, M4=3, M5=1, M6=0, M7=1, M8=0, M9=1,
M10=0, M11=1, M12=1. Sum = 12/60.**
Moats "present" (score ≥3): M3 (Capital Efficiency), M4 (Customer
Stickiness) = **2 moats confirmed**.
Moat classification (2 present) = **MODERATE**.

---

## MOAT PROFILE

```
M1  Pricing Power        [#----] 1/5
M2  Cost Advantage       [-----] 0/5
M3  Capital Efficiency   [###--] 3/5  MOAT PRESENT
M4  Customer Stickiness  [###--] 3/5  MOAT PRESENT
M5  Scale & Dominance    [#----] 1/5
M6  Technology/R&D       [-----] 0/5
M7  Regulatory/License   [#----] 1/5
M8  Distribution         [-----] 0/5
M9  Brand                [#----] 1/5
M10 Switching Costs      [-----] 0/5
M11 Network Effects      [#----] 1/5
M12 Negative WC/Float     [#----] 1/5
```

---

## SCORE SUMMARY

| Block | Score | Max | % |
|---|---|---|---|
| A — Return on Capital | 13 | 20 | 65% |
| B — Cash Generation Quality | 5 | 20 | 25% |
| C — Growth | 15 | 20 | 75% |
| D — Balance Sheet Strength | 12 | 20 | 60% |
| E — Shareholder Alignment | 0 | 20 | 0% (data absent) |
| **Core Score (A+B+C+D+E)** | **45** | **100** | **45%** |
| F — Quantitative Moat | 12 | 60 | 20% |
| **Grand Total** | **57** | **160** | — |

Strongest evidenced block: **C — Growth (75%)**, driven by uniform,
sharp revenue and PAT expansion.
Weakest evidenced block: **B — Cash Generation Quality (25%)**, a
genuine negative finding (cumulative CFO/PAT of −0.70). Block E (0%) is
lower in raw score but reflects total data absence, not a demonstrated
governance weakness — do not read it as worse than Block B.

---

## DATA CONFIDENCE

6 years of core P&L/CF history (FY2021-FY2026) → **"5-6 lower, flag: may
not have seen full cycle"** per the confidence table. This is a flag,
not a full tier downgrade (that threshold is 3-4 years). Note further
that capital-employed-dependent metrics (A1, A2, A4, D1-D4, the payables
leg of B4) rest on only 3 years (FY2024-FY2026) of underlying balance-
sheet detail, coinciding with the company's August 2024 listing —
history_downgrade is NOT applied (>=5 years overall), but the narrower
3-year sub-window for these specific metrics is flagged.

---

## CLASSIFICATION

Core Score = 45 → **Core 40-59 band → AVERAGE** (this band is flat
regardless of moat class per the classification matrix).

**Deal-breaker overrides triggered (recorded per rule; neither worsens
the already-AVERAGE outcome):**
- **#2** Block B < 8 (actual 5) → caps at max GOOD (non-binding here,
  since matrix already yields AVERAGE, which is below GOOD)
- **#4** Cumulative CFO ÷ PAT < 0.50 (actual −0.70) → caps at max
  AVERAGE (binding; confirms AVERAGE, does not lower it further since
  there is no tier below AVERAGE for this override)

Deal-breakers NOT triggered: #1 (Block A =13, not <8), #3 (median ROCE
19.21%, not <10%), #5 (pledge data absent, no evidence to trigger), #6
(ND/EBITDA 1.59x, not >3x), #7 (no revenue decline years), #8 (PAT
positive all years), #9 (6 years of history, not <3).

## FINAL CLASSIFICATION: AVERAGE

---

## DECISION LINE

Ceigall scores AVERAGE (45/100 core, MODERATE moat, 2 confirmed moats).
Growth is real and broad (35.7% revenue CAGR, zero decline years,
55% ROCE at FY24) but two deal-breakers fire: cash conversion is
negative across five of six years (cumulative CFO/PAT −0.70), and ROCE
has fallen 14.3pp from FY24 to FY26 as post-IPO capital (HAM equity,
ballooning contract assets) has not yet earned a return. Block E
(shareholder alignment) is entirely unscored for lack of a shareholding
pattern — a hard corpus gap, not a governance finding, that must be
closed before Halt 1. The B4/M12 working-capital-days metrics score
favourably only because the fixed formula excludes Contract
Assets/WIP, the archetype's real working-capital driver; B1's −0.70
ratio is the trustworthy signal on cash quality.

---

```yaml
stage: B01-gate0
company: "CEIGALL"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Annual Report FY2026 text extraction unusable: 150 of 151 pages blank, page 1 garbled/mojibake; no AR-sourced figure used in this stage"
  - "screener CSVs: only Data_Sheet populated; Profit_Loss, Balance_Sheet, Cash_Flow, Quarters, Customization tabs are empty templates"
  - "Shareholding pattern absent from corpus; Block E (E1-E4) fully N/A, scored 0"
  - "Trade payables and current-liabilities split unavailable for FY2021-FY2023 (screener lumps into 'Other Liabilities'); ROCE (A1/A2/A4), Current Ratio (D4), and the payables leg of WC Days (B4) computed only for FY2024-FY2026 using Investor Presentation balance sheet"
  - "Capex (purchase of PPE + intangibles) not broken out in any provided source; only aggregate Investing Cash Flow given; FCF metrics B2/B3 marked N/A"
  - "Contingent liabilities not disclosed in any provided source; E4 N/A"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE. Deal-breaker #4 (cumulative CFO/PAT -0.70) and #2 (Block B 5/20) both triggered despite strong Block A (65%) and Block C (75%) scores. Revenue CAGR 35.73% vs PAT CAGR 22.62% (-13.1pp, C4=0) and ROCE fell 14.27pp FY24->FY26 (A4=0): growth is real but not yet self-funding or capital-efficient at the margin."}
data_years: 6
fy_range: "FY2021 to FY2026"
blocks: {A: 13, B: 5, C: 15, D: 12, E: 0}
core_score: 45
moat_score: 12
grand_total: 57
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "#2 Block B <8 (actual 5) -> max GOOD (non-binding, matrix already AVERAGE)"
  - "#4 cumulative CFO/PAT <0.50 (actual -0.70) -> max AVERAGE (binding)"
history_downgrade: false
data_notes:
  - "No loss-to-profit swing: PAT positive all 6 years (FY21-FY26)."
  - "WC Days computed on Revenue basis throughout (no explicit standalone COGS line in any source)."
  - "M9 Brand GM proxy = (Revenue-Material Cost)/Revenue; FY2026 Raw Material Cost lines are not comparable across CEIGALL/KNRCON/PNCINFRA due to a categorization shift in the FY2026 screener export (cost buckets appear lumped into fewer lines); FY2025 used instead for the peer GM comparison, the last year with cleanly split cost lines for all four companies."
  - "M2/M5/M9/M11 peer comparisons use a 3-name named peer set (HGINFRA, KNRCON, PNCINFRA) only, not an exhaustive listed road-EPC/HAM universe; PEER DATA NEEDED for a fuller segment ranking on M5 in particular."
  - "A1 computed ROCE (FY26 17.71%) diverges 2.3pp from the Investor Presentation's own disclosed ROCE (20.0%, p.36); plausibly explained by an INR 5,431mn 'held for sale' asset/INR 3,303mn matching liability in the FY26 consolidated balance sheet (p.39) that the company may net out of its own capital-employed base. Scored on the fixed-formula computed figure, not the company chart, per rule."
block_b_trend: "improving"        # CFO narrowed from -519.56 Cr (FY25) to -91.28 Cr (FY26), though cumulative 6-year CFO of -925.74 Cr against cumulative PAT of +1,317.68 Cr remains deeply negative (B1 = 0)
analyst_note: "Two distinct stories coexist. Blocks A and C say this is a fast, profitable grower (35.7% revenue CAGR, 33.4% median ROE, zero revenue-decline years). Block B says the growth has not yet turned to cash: CFO was negative in 5 of 6 years and cumulative CFO trails cumulative PAT by 925.74 Cr, driven by Contract Assets/WIP nearly quadrupling FY24-FY26 (402.8 to 1,413.2 Cr), an item the fixed WC-Days formula does not capture, so B4 and M12 score well despite this. ROCE nearly halved FY24 (31.98%) to FY26 (17.71%) as post-IPO HAM equity and working capital have not yet earned a return. Block E is a pure data gap (no shareholding file), not a governance finding; treat classification AVERAGE as growth-outrunning-cash-conversion, not as a quality problem, pending Block E and the missing capex breakdown."
```
