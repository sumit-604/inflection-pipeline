# STAGE 1: GATE 0 SCORECARD — Asian Energy Services Limited (ASIANENE)
Run date: 2026-07-13 | Model: claude-sonnet-5 | Pipeline mode

Data sources: screener.in Data_Sheet.csv (10-year annual + quarterly block; the
Profit_Loss.csv, Balance_Sheet.csv, Cash_Flow.csv, Quarters.csv exports were blank
templates and contributed nothing), plus two BSE/NSE filing PDFs: (1) Q3 FY26
results (standalone + consolidated, quarter/9M ended 31-Dec-2025, filed
13-Feb-2026) and (2) FY26 annual audited results (standalone + consolidated,
year ended 31-Mar-2026, filed 19-May-2026, with full balance sheet and cash flow
statement). Consolidated figures used throughout as primary (verified to tie to
Data_Sheet.csv line for line on FY25/FY26 — see cross-checks below). No prior
run, no company memory (first Gate 0 for this ticker).

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history
for revenue/PAT-based metrics. IMPORTANT LIMITATION: the screener Data_Sheet.csv
does not split Balance Sheet liabilities into current vs non-current, and does
not carry a separate Trade Payables line or a Capex line in the Cash Flow
section for FY17–FY24. Full breakdowns (current liabilities, trade payables,
capex) exist only for FY25 and FY26, sourced from the audited balance sheets and
cash flow statements in the two results PDFs. This means ROCE, FCF, and WC-Days
(with payables) are computable for only 2 of 10 years; those years are marked
explicitly below and are NOT extrapolated. No shareholding pattern, promoter
holding, pledge, or contingent-liability data was present in any provided file
— Block E is entirely NOT FOUND.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (source does not
provide it in this export). EBIT = PBT + Interest (screener/standard
convention, includes other income).

Current-liability breakdown available only for FY25 and FY26 (audited
consolidated balance sheets):
- FY26: Total Assets 918.41 Cr (screener-data, Data Sheet FY26; cross-checked
  91,841.18 lakh, results FY26 annual p.10) − Current Liabilities 338.81 Cr
  (33,881.35 lakh, results FY26 annual p.10) = Capital Employed 579.60 Cr
- FY25: Total Assets 592.46 Cr (screener-data, Data Sheet FY25; cross-checked
  59,245.67 lakh, results FY26 annual p.10) − Current Liabilities 178.95 Cr
  (17,895.42 lakh, results FY26 annual p.10) = Capital Employed 413.50 Cr

EBIT: FY26 = PBT 68.84 Cr (screener-data, Data Sheet) + Interest 10.65 Cr
(screener-data, Data Sheet) = 79.49 Cr (cross-checked 6,883.66 + 1,065.12 lakh,
results FY26 annual p.9). FY25 = PBT 56.17 + Interest 3.83 = 60.00 Cr
(cross-checked 5,617.69 + 382.55 lakh, results FY26 annual p.9).

- ROCE FY26 = 79.49 ÷ 579.60 = 13.71% (computed)
- ROCE FY25 = 60.00 ÷ 413.50 = 14.51% (computed)
- ROCE FY17–FY24 = N/A (not in provided data) — current-liability split absent

**A1 Median ROCE**: median of the two available years = (13.71+14.51)/2 = 14.11%
→ 10-14.9% band → **score 1** (data note: based on only 2 of 10 years; other
years NOT FOUND, not estimated)

**A2 Minimum single-year ROCE**: min(13.71%, 14.51%) = 13.71% → 12-14.9% band →
**score 3**

**A3 Median ROE**: ROE = PAT ÷ average Net Worth (opening+closing)/2; FY17 uses
closing only (opening not available), stated. Net Worth = Equity Share Capital
+ Reserves (screener-data, Data Sheet, all years).
| FY | Net Worth (Cr) | PAT (Cr) | ROE |
|---|---|---|---|
|17|81.79 (closing only)|-18.20|-22.25%|
|18|avg 111.16|10.30|9.27%|
|19|avg 146.27|9.10|6.22%|
|20|avg 166.73|29.24|17.54%|
|21|avg 192.44|22.57|11.73%|
|22|avg 222.60|38.81|17.44%|
|23|avg 220.61|-44.36|-20.11%|
|24|avg 238.67|25.47|10.67%|
|25|avg 338.28|42.12|12.45%|
|26|avg 446.41|51.16|11.46%|
(all inputs screener-data, Data Sheet)
Median (10 values, avg of 5th/6th sorted) = (10.67+11.46)/2 = 11.07% → <12% →
**score 0**

**A4 ROCE trend, latest vs earliest**: only FY25 and FY26 are comparable
(earliest available = FY25, 14.51%; latest = FY26, 13.71%) — decline of 0.80pp.
This falls below the rule's explicit "decline 1-3pp" floor (i.e., it is a
sub-1pp edge case not literally enumerated); scored conservatively into the
nearest applicable declining band → **score 3** (flagged as a banding edge
case, not a data gap — both endpoints are anchored)

**Block A total = 1+3+0+3 = 7/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO (screener-data, Data Sheet, Cash Flow section) FY17–FY26 (Cr): -18.22,
27.33, 26.93, 89.06, -6.81, 48.11, -2.64, -44.10, -33.08, 52.99. FY26 and FY25
cross-checked to 5,298.52 and -3,307.65 lakh respectively (results FY26 annual
p.11) — exact match confirms Data_Sheet CFO is consolidated audited CFO.

PAT (screener-data, Data Sheet) FY17–FY26 (Cr): -18.20, 10.30, 9.10, 29.24,
22.57, 38.81, -44.36, 25.47, 42.12, 51.16. FY26 cross-checked to 5,115.71 lakh
(net profit attributable to owners of Holding Company, results FY26 annual p.9)
— confirms Data_Sheet PAT is consolidated-attributable-to-owners, not
whole-group PAT.

**B1 Cumulative CFO ÷ Cumulative PAT**: Cumulative CFO = 139.57 Cr; Cumulative
PAT = 166.21 Cr → ratio = 0.8397 → 0.70-0.84 band → **score 2** (0.01 short of
the 0.85 threshold for score 4)

**B2 FCF-positive years as proportion**: FCF = CFO − Capex (purchase of PPE +
intangibles, excl. acquisitions). Capex is a distinct cash-flow line only in
the two results PDFs (FY25, FY26); for FY17–FY24 the Data_Sheet.csv only
carries aggregate "Cash from Investing Activity" which conflates capex with
acquisitions/investments/ICDs and cannot be safely disaggregated (e.g., FY26
CFI of -159.49 Cr includes the ~122.80 Cr Kuiper Group acquisition and mutual
fund churn, vs actual capex of 60.64 Cr) — FCF is therefore NOT FOUND for
FY17–FY24, never estimated.
- FY26: CFO 52.99 − Capex 60.64 Cr (6,064.15 lakh, "Purchase of PPE and CWIP",
  results FY26 annual p.11) = **-7.66 Cr** (negative)
- FY25: CFO -33.08 − Capex 19.02 Cr (1,901.52 lakh, results FY26 annual p.11)
  = **-52.09 Cr** (negative)
Of the 2 years with data, 0 are FCF-positive → 0% → <50% band → **score 0**
(data note: based on 2 of 10 years only)

**B3 Cumulative FCF ÷ Cumulative PAT** (same 2 years only): Cumulative FCF =
-59.75 Cr; Cumulative PAT (FY25+FY26) = 93.28 Cr → ratio = -0.64 → negative →
**score 0**

**B4 Change in WC Days, latest vs earliest** (available years only, FY25 vs
FY26): Receivable Days = Receivables÷Revenue×365; Inventory Days =
Inventory÷Revenue×365 (revenue basis used — COGS not separately itemized in
provided P&L, Raw Material Cost row is blank in all years, stated); Payable
Days = Trade Payables÷Revenue×365 (revenue basis, same reason). Trade
Payables only available FY25/FY26 (results FY26 annual p.10).
- FY25: Receivables 224.42 Cr (screener-data) → 176.12 days; Inventory 0.18 Cr
  → 0.14 days; Payables 142.44 Cr (14,244.48 lakh, results FY26 annual p.10) →
  111.79 days → WC Days = 176.12+0.14-111.79 = **64.47 days**
- FY26: Receivables 347.73 Cr → 160.44 days; Inventory 0.29 Cr → 0.13 days;
  Payables 229.58 Cr (22,957.65 lakh, results FY26 annual p.10) → 105.93 days
  → WC Days = 160.44+0.13-105.93 = **54.64 days**
Change = 54.64 − 64.47 = -9.83 days (decreased) → decreased >5 days → **score 5**
(data note: only 2 of 10 years comparable; FY17–FY24 payables NOT FOUND)

**Block B total = 2+0+0+5 = 7/20**

block_b_trend: CFO (screener-data, Data Sheet) moved -44.10 Cr (FY24) →
-33.08 Cr (FY25) → +52.99 Cr (FY26) — **improving**, driven by working-capital
release and revenue scale-up in FY26.

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-data, Data Sheet) FY17–FY26 (Cr): 124.32, 222.22, 193.86,
273.15, 228.79, 260.47, 109.95, 305.06, 465.04, 791.05.

**C1 Revenue CAGR** (FY17→FY26, 9 years): (791.05÷124.32)^(1/9)-1 = 22.84% →
≥20% → **score 5**

**C2 PAT CAGR**: start-year PAT (FY17) = -18.20 Cr (negative endpoint) →
**"N/M (negative endpoint)" → score 0**. Additional note: PAT swung
loss-to-profit twice in the window — FY17 (-18.20 Cr) to FY18 (+10.30 Cr), and
FY23 (-44.36 Cr) to FY24 (+25.47 Cr) — no synthetic CAGR attempted.

**C3 Positive YoY revenue years proportion**: 9 YoY comparisons (FY18–FY26);
positive: FY18, FY20, FY22, FY24, FY25, FY26 (6); negative: FY19, FY21, FY23
(3) → 6/9 = 66.7% → 50-74% band → **score 1**

**C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → per rule, **score 0**
(operating-leverage test invalid when PAT CAGR is N/M)

**Block C total = 5+0+1+0 = 6/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

**D1 Net Debt ÷ EBITDA**: Borrowings (incl. lease liabilities) FY26 = 158.64 Cr
(screener-data, Data Sheet; cross-checked 7,224.26+8,587.55+52.49 lakh,
results FY26 annual p.10). Cash & Bank FY26 = 146.85 Cr (screener-data, Data
Sheet; cross-checked 10,874.81+3,809.73 lakh, results FY26 annual p.10). Net
Debt = 158.64-146.85 = 11.79 Cr. EBITDA = EBIT 79.49 + Depreciation 18.86 Cr
(screener-data, Data Sheet) = 98.35 Cr. Ratio = 11.79÷98.35 = 0.12x → 0-1.0x
band → **score 4**

**D2 Interest Coverage (EBIT ÷ Interest)**: 79.49 ÷ 10.65 (screener-data, Data
Sheet) = 7.46x → 5-9.9x band → **score 4**

**D3 Debt ÷ Equity**: Debt 158.64 Cr ÷ Equity 494.15 Cr (screener-data, Data
Sheet; equity attributable to owners, cross-checked 49,415.30 lakh, results
FY26 annual p.10) = 0.32x → 0.1-0.5x band → **score 4**

**D4 Current Ratio**: Current Assets 715.10 Cr ÷ Current Liabilities 338.81 Cr
(71,510.05 ÷ 33,881.35 lakh, results FY26 annual p.10) = 2.11x → ≥2.0x →
**score 5**

**Block D total = 4+4+4+5 = 17/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding pattern, promoter-holding history, promoter-pledge disclosure,
or contingent-liability note was present in any provided input file (screener
CSVs contain no shareholding export; the two results PDFs are P&L/balance
sheet/cash-flow filings only, with no shareholding or contingent-liability
annexure).

**E1 Promoter holding (latest quarter)**: N/A (not in provided data) → **score 0**
**E2 Promoter holding change, 3yr**: N/A (not in provided data) → **score 0**
**E3 Promoter pledge (latest)**: N/A (not in provided data) → **score 0**
**E4 Contingent liabilities ÷ Net Worth**: N/A (not in provided data) →
**score 0**

**Block E total = 0/20** (entirely a data-availability gap, not a company-quality
finding — flagged below)

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin (screener-data, computed as (PBT+Interest+Depreciation)÷Sales)
by year: FY17 3.87%, FY18 15.24%, FY19 17.71%, FY20 23.12%, FY21 21.22%, FY22
26.56%, FY23 -18.31%, FY24 15.65%, FY25 16.71%, FY26 12.43%.

**M1 Pricing Power**: margin FY26 (12.43%) vs FY17 (3.87%) = +8.56pp expansion;
revenue CAGR 22.84% (≥10%) → margin expanded ≥2pp AND revenue CAGR≥10% →
**score 5** (note: margin path is volatile — peaked 26.56% FY22, crashed to
-18.31% FY23 — the test as literally specified is latest-vs-earliest only)

**M2 Cost Advantage vs peer median EBITDA margin**: peer data excluded per
task scope (DOLPHIN/DEEPINDS/JINDRILL are peers, not to be scored) → **score 0,
"PEER DATA NEEDED"**

**M3 Capital Efficiency**: FAT (FY26) = Sales 791.05 ÷ Net Block 114.56 Cr
(screener-data, Data Sheet) = 6.91x (>3x); ROCE FY26 = 13.71% (not >20%, not
>15%, but >12%) → falls to "FAT>1x AND ROCE>12%" band → **score 1**

**M4 Customer Stickiness**: 3 revenue-decline years in the period (FY19, FY21,
FY23) → 3+ decline years → **score 0**

**M5 Scale & Dominance**: requires peer mcap/margin ranking — peer data
excluded per task scope → **score 0, "PEER DATA NEEDED"**

**M6 Technology/R&D**: no R&D expenditure line in any provided filing (oilfield
services business; not disclosed) → **score 0, N/A (not in provided data)**

**M7 Regulatory/License**: no evidence of a licensed/limited-entrant segment;
oilfield/energy services is a competitively bid project services business →
unregulated → **score 0**

**M8 Distribution**: no distribution-network/outlet metric applies to a
B2B project-services business; none disclosed → **score 0**

**M9 Brand**: Gross-margin proxy (Revenue − Material Cost)÷Revenue could not
be computed — the "Raw Material Cost" row is blank for all 10 years in the
Data_Sheet.csv — and peer median is unavailable regardless (peer data
excluded) → **score 0, N/A (not in provided data) / PEER DATA NEEDED**

**M10 Switching Costs**: overall revenue growth over the period (FY17→FY26 up)
with 3 decline years (FY19, FY21, FY23) ≥2 → "overall growth, 2+ decline years"
band → **score 1**

**M11 Network Effects** (10 years available, ≥6yr test valid): latest-3yr
window (FY24→FY26) revenue CAGR = (791.05÷305.06)^(1/2)-1 = 61.03%; prior-3yr
window (FY21→FY23) revenue CAGR = (109.95÷228.79)^(1/2)-1 = -30.68%. Latest >
prior. Selling & admin expense as % of sales (screener-data, Data Sheet):
FY24 4.48%, FY25 3.28% — declining — but FY26 Selling and admin figure is
blank/NOT FOUND in Data_Sheet.csv, so the full-window trend cannot be
confirmed through the latest year → scored conservatively at the
"rev CAGR≥20% AND selling% stable/declining" band rather than the top band →
**score 3** (data note: FY26 selling-expense figure NOT FOUND)

**M12 Negative WC/Float**: WC Days computable only for FY25 (64.47) and FY26
(54.64), both >45 days in the only years available → **score 0** (data note:
based on 2 of 10 years; FY17–FY24 NOT FOUND, same limitation as B4)

**Block F total = 5+0+1+0+0+0+0+0+0+1+3+0 = 10/60**

Moat profile:
```
M1  Pricing Power        [#####] 5  PRESENT
M2  Cost Advantage       [     ] 0  PEER DATA NEEDED
M3  Capital Efficiency   [#    ] 1
M4  Customer Stickiness  [     ] 0
M5  Scale & Dominance    [     ] 0  PEER DATA NEEDED
M6  Technology/R&D       [     ] 0  N/A
M7  Regulatory/License   [     ] 0
M8  Distribution         [     ] 0  N/A
M9  Brand                [     ] 0  N/A / PEER DATA NEEDED
M10 Switching Costs      [#    ] 1
M11 Network Effects      [###  ] 3  PRESENT
M12 Negative WC/Float    [     ] 0
```
Moats confirmed (score ≥3): M1, M11 = **2**
Moat classification (2-3 present): **MODERATE**

---

## CLASSIFICATION

Data confidence: overall revenue/PAT history = 10 years → **"10+ yrs full"**
tier by the letter of the rule. However, this masks a material sub-metric gap:
ROCE, FCF, and payables-based WC Days are anchored for only 2 of those 10
years (FY25, FY26); Block E is 0/20 entirely because no shareholding data was
provided. This does not trigger the formal history-length downgrade (which is
based on total fiscal years available, satisfied here), but materially caps
confidence in Blocks A, B, and E specifically — flagged below.

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 7 | 20 |
| B — Cash Generation Quality | 7 | 20 |
| C — Growth | 6 | 20 |
| D — Balance Sheet Strength | 17 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **Core Score** | **37** | **100** |
| F — Quantitative Moat | 10 | 60 |
| **Grand Total** | **47** | **160** |

Classification matrix: Core 37 → **Core <40 → AVOID**

Deal-breaker check:
1. Block A (7) <8 → caps at max GOOD — no effect (base AVOID already below GOOD)
2. Block B (7) <8 → caps at max GOOD — no effect (base AVOID already below GOOD)
3. Median ROCE 14.11% (≥10%) — not triggered
4. Cumulative CFO/PAT 0.84 (not <0.50) — not triggered
5. Pledge — unknown (NOT FOUND), cannot confirm trigger, treated as not
   triggered on available evidence
6. ND/EBITDA 0.12x (not >3x) — not triggered
7. Revenue declined in 3 of 9 years (not majority) — not triggered
8. PAT last 3 years (FY24 25.47, FY25 42.12, FY26 51.16) all positive — not
   triggered
9. History = 10 years (≥3) — not triggered

**Final classification: AVOID**

**Strongest block: D — Balance Sheet Strength (17/20)** — net cash-light
balance sheet, current ratio 2.11x, low leverage.
**Weakest block: E — Shareholder Alignment (0/20)** — entirely a data gap
(no shareholding pattern in inputs), not a demonstrated company-quality
finding.

**Decision line**: Gate 0 mechanically classifies ASIANENE as AVOID on a
core score of 37/100, driven by Block E being wholly unscored for lack of
shareholding data, by Block A/B metrics anchored for only FY25-FY26, by a
below-12% median 10-year ROE, and by three revenue-decline years including
the FY23 collapse (Sales fell to Rs110cr from Rs260cr FY22, alongside a
Rs44.36cr loss). FY24-FY26 show a strong, fully anchored recovery (Sales
Rs305cr → Rs465cr → Rs791cr, PAT positive and rising all three years, plus
the Kuiper Group acquisition concluded Aug-2025 and the pending OEPL merger
via NCLT). Flags propagate per protocol; this Gate 0 does not halt the run.

---
