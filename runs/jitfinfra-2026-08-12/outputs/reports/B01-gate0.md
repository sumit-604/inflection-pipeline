# GATE 0 SCORECARD — JITF Infra Logistics Ltd (JITFINFRA)
Run date: 2026-08-12 | Model: claude-sonnet-5 | Stage: B01-gate0

Sector correction carried forward: JITF Infralogistics is a water /
wastewater / waste-to-energy / rail-and-urban infrastructure holding
company (Jindal ITF group), not a cables company. True comparables used
below: AWHCL (Antony Waste Handling Cell), EIEL (Enviro Infra Engineers),
EMSLIMITED (EMS Ltd), WABAG (VA Tech Wabag). This is a first / full run;
no prior run exists for refresh comparison.

Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year
history. Primary source: screener.in Data_Sheet.csv (the only populated
screener export — Profit_Loss.csv, Balance_Sheet.csv, Cash_Flow.csv and
Quarters.csv exports were blank templates with no data rows). Cross-checked
against two exchange filings: Q3 FY26 (9M ended 31.12.2025, filed
06.02.2026) and FY26 full-year audited results (year ended 31.03.2026,
filed 12.05.2026). Both filings' consolidated figures reconcile almost
exactly to the screener export (Sales, CFO, investing/financing cash flow,
Receivables, Inventory all match FY25/FY26 to the rupee), confirming
screener's series is consolidated and PAT is profit attributable to owners
of the parent (post minority interest) — confirmed directly: FY26
consolidated PAT total = -₹9.93 Cr, of which owners' share = -₹48.13 Cr
(results FY26, Consolidated P&L), matching screener's Net Profit FY26 of
-48.13 exactly.

## KEY DATA-AVAILABILITY GAPS (apply throughout)
- No shareholding-pattern filing, no rating, no prospectus, no
  announcements, no research, no presentation, no concalls
  (concalls_available:false) in provided inputs. Block E is therefore
  unscored on evidence (all NOT FOUND), not zero-because-bad.
- screener's simplified balance sheet has no current/non-current split
  and no Trade Payables line for any year. ROCE capital employed is
  therefore computed as a stated proxy (Equity + Reserves + Borrowings);
  Working Capital Days (B4, M12) cannot be computed per the specified
  formula for FY17-FY24 because Trade Payables are not disclosed.
- screener's Cash Flow export has no capex (Purchase of PPE) breakout;
  only the FY26 results filing's audited cash flow statement discloses
  capex, for FY26 and FY25 (comparative) only. FCF (B2, B3) is therefore
  scored on 2 of 10 years.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 5

ROCE = EBIT ÷ (Equity Share Capital + Reserves + Borrowings), **computed**
— capital employed proxied because screener's Balance_Sheet/Data_Sheet
exports do not split current vs non-current liabilities (Other
Liabilities is a single aggregate bucket). EBIT = PBT + Interest.

| FY | Sales | PBT | Interest | EBIT | Capital Employed | ROCE |
|----|------:|----:|---------:|-----:|------------------:|-----:|
| 17 | 542.95 | -142.95 | 118.70 | -24.25 | 1,048.18 | -2.31% |
| 18 | 399.91 | -188.53 | 133.60 | -54.93 | 1,081.22 | -5.08% |
| 19 | 580.88 | -118.17 | 165.10 | 46.93 | 1,443.71 | 3.25% |
| 20 | 844.14 | -125.94 | 200.48 | 74.54 | 1,538.57 | 4.85% |
| 21 | 927.97 | -141.28 | 216.41 | 75.13 | 1,800.36 | 4.17% |
| 22 | 1,233.92 | -127.04 | 253.04 | 126.00 | 2,165.20 | 5.82% |
| 23 | 1,589.14 | -97.18 | 312.55 | 215.37 | 2,410.39 | 8.94% |
| 24 | 2,535.18 | 135.98 | 298.24 | 434.22 | 3,216.63 | 13.50% |
| 25 | 2,264.81 | 189.69 | 352.19 | 541.88 | 2,992.75 | 18.11% |
| 26 | 2,808.02 | 55.39 | 401.29 | 456.68 | 3,432.76 | 13.31% |
(all rows: screener-data, computed)

Cross-check FY26 with audited precision: Total Assets ₹5,032.96 Cr −
Current Liabilities ₹1,703.27 Cr = Capital Employed ₹3,329.69 Cr (results
FY26, Consolidated Statement of Assets and Liabilities, 12.05.2026); EBIT
₹456.67 Cr ÷ ₹3,329.69 Cr = 13.72% — within 0.4pp of the proxy figure
(13.31%), confirming the proxy does not distort the conclusion.

- **A1 Median ROCE**: sorted, median of 10 years = avg(4.85%, 5.82%) =
  **5.34%**. Band <10% = 0. **A1 = 0**
- **A2 Minimum single-year ROCE**: **-5.08% (FY18)**. Band <8% = 0.
  **A2 = 0**
- **A3 Median ROE**: Net Worth (Equity Share Capital + Reserves) is
  **negative in all 10 fiscal years** (FY17: -₹96.17 Cr through FY26:
  -₹513.28 Cr — screener-data), i.e. accumulated losses exceed paid-up
  capital throughout. ROE = PAT ÷ average Net Worth is not economically
  meaningful with a negative denominator across the whole window; marked
  N/M rather than computed. **A3 = 0**
- **A4 ROCE trend, latest vs earliest**: latest (FY26, 13.31%) ≥ earliest
  (FY17, -2.31%). **A4 = 5**

**Block A total = 0+0+0+5 = 5 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0

| FY | CFO | PAT |
|----|----:|----:|
| 17 | -162.88 | -110.87 |
| 18 | 4.37 | -156.78 |
| 19 | -52.10 | -110.55 |
| 20 | 72.92 | -135.95 |
| 21 | 21.22 | -150.72 |
| 22 | 84.18 | -143.85 |
| 23 | 190.20 | -127.66 |
| 24 | 185.34 | 35.41 |
| 25 | 185.02 | 52.39 |
| 26 | 198.76 | -48.13 |
(screener-data)

Cumulative CFO (FY17-26) = **₹727.03 Cr**. Cumulative PAT = **-₹896.71 Cr**
(10 years of accumulated net loss on an owners'-PAT basis, despite
cumulative positive CFO — a genuine divergence worth flagging: cash
generation has been more resilient than reported earnings, largely via
depreciation add-back and working-capital timing, but the formula below is
scored mechanically).

- **B1 Cumulative CFO ÷ Cumulative PAT** = 727.03 ÷ (-896.71) = **-0.81**.
  A negative ratio falls below the 0.50 floor. **B1 = 0** (data_note:
  ratio is negative because cumulative PAT is negative, not because CFO
  is weak; flagged, not silently passed)
- **B2 FCF-positive years proportion**: FCF = CFO − Capex. Capex
  (Purchase of PPE, consolidated audited cash flow) is only disclosed for
  FY25 (₹280.55 Cr) and FY26 (₹244.48 Cr) — results FY26 filing,
  Consolidated Cash Flow Statement, 12.05.2026. FY17-FY24 capex is N/A
  (not in provided data; screener's Cash Flow export gives only the
  investing-activity aggregate, not a capex line).
  - FY25: FCF = 185.02 − 280.55 = **-₹95.53 Cr**
  - FY26: FCF = 198.76 − 244.48 = **-₹45.72 Cr**
  Both of the 2 years with data are negative → 0% positive, <50% band.
  **B2 = 0** (scored on 2 of 10 years; limitation stated)
- **B3 Cumulative FCF ÷ Cumulative PAT** (same 2-year window): Cumulative
  FCF (FY25+26) = -₹141.25 Cr; Cumulative PAT (FY25+26) = ₹4.26 Cr.
  Ratio = -33.16, "<0.20 or negative" band. **B3 = 0**
- **B4 Change in WC Days, latest vs earliest**: N/A (not in provided
  data) — Trade Payables are not disclosed anywhere in the screener
  export for FY17-FY24; the specified formula (Receivable + Inventory −
  Payable Days) cannot be computed at the FY17 (earliest) end-point.
  **B4 = 0**, scored as data gap, not as a measured decline.
  Supplementary (not scored): using the 2 years where full WC Days data
  exists — FY25 = 135.07 + 5.87 − 84.91 = 56.03 days; FY26 = 165.22 +
  8.29 − 108.46 = 65.05 days (all four inputs: results FY26 filing,
  Consolidated Balance Sheet/P&L, reconciled exactly to screener
  Receivables/Inventory) — a 9-day increase FY25→FY26, i.e. the one
  confirmed year-over-year data point points to a mild WC Days
  deterioration, not the improvement a partial (payables-excluded) view
  would suggest.

**Block B total = 0+0+0+0 = 0 / 20**

block_b_trend: **deteriorating** — FY26 FCF -₹45.72 Cr vs FY25 FCF
-₹95.53 Cr (both negative; results FY26 filing), while Borrowings rose
+12.6% YoY to ₹3,946.04 Cr (screener-data) — capex continues to outrun
operating cash generation and is being funded by fresh debt, not the
balance sheet.

---

## BLOCK C: GROWTH (Max 20) — Score: 8

Revenue FY17→FY26: ₹542.95 Cr → ₹2,808.02 Cr (screener-data).

- **C1 Revenue CAGR** (9-year, FY17-26) = (2808.02/542.95)^(1/9) − 1 =
  **20.03%**. Band ≥20% = 5. **C1 = 5**
- **C2 PAT CAGR**: endpoint FY17 PAT = -₹110.87 Cr (negative), endpoint
  FY26 PAT = -₹48.13 Cr (negative). Both endpoints negative → **N/M
  (negative endpoint)**. **C2 = 0**. data_notes: loss-to-profit swing
  FY23 (-127.66) → FY24 (+35.41); profit-to-loss swing FY25 (+52.39) →
  FY26 (-48.13) — two swings inside the window, no synthetic CAGR
  attempted.
- **C3 Positive YoY revenue years proportion**: 7 of 9 YoY periods
  positive (declines in FY18 vs FY17, and FY25 vs FY24) = **77.8%**.
  Band 75-99% = 3. **C3 = 3**
- **C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → per rule, **C4 =
  0** and noted.

**Block C total = 5+0+3+0 = 8 / 20**

Deal-breaker #7 check (revenue declined in majority of years): 2 of 9 =
22%, not a majority — **not triggered**.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 2

Latest-year figures sourced primarily from the FY26 audited results
filing (Consolidated Statement of Assets and Liabilities and Consolidated
Cash Flow Statement, 12.05.2026), cross-checked against screener-data
where the two overlap (Borrowings ₹3,946.04 Cr audited-computed
₹3,945.48 Cr — match to rounding).

- **D1 Net Debt ÷ EBITDA (latest, FY26)**: Total borrowings (current +
  non-current) = ₹3,945.48 Cr; Cash & cash equivalents = ₹200.42 Cr
  (results FY26 filing, Consolidated Balance Sheet). Net Debt = **₹3,745.06
  Cr**. EBITDA FY26 = Revenue ₹2,808.02 Cr − (Total expenses ₹2,753.40 Cr
  − Finance costs ₹401.29 Cr − Depreciation ₹102.54 Cr) = **₹558.46 Cr**
  (results FY26 filing, Consolidated P&L, computed). Net Debt/EBITDA =
  **6.71x**. Band >3x = 0. **D1 = 0**
- **D2 Interest Coverage (EBIT ÷ Interest, latest FY26)**: EBIT = PBT
  ₹55.38 Cr + Finance costs ₹401.29 Cr = ₹456.67 Cr; Interest ₹401.29 Cr
  (results FY26 filing, Consolidated P&L). Coverage = **1.14x**. Band
  <1.5x = 0. **D2 = 0**
- **D3 Debt ÷ Equity (latest, FY26)**: Net Worth (owners' equity) =
  **-₹513.28 Cr** (screener-data / results FY26 Consolidated Balance
  Sheet, "Net Worth" line = -51,327.81 lakhs). Equity is negative
  (deficit); Debt/Equity is undefined in the conventional sense. Scored
  as the worst-case band given the equity deficit. **D3 = 0**
- **D4 Current Ratio (latest, FY26)**: Current assets ₹2,503.09 Cr ÷
  Current liabilities ₹1,703.27 Cr (results FY26 filing, Consolidated
  Balance Sheet, summed line-by-line) = **1.47x**. Band 1.2-1.49x = 2.
  **D4 = 2**

**Block D total = 0+0+0+2 = 2 / 20**

**Deal-breaker #6 TRIGGERED**: Net Debt/EBITDA 6.71x (>3x) AND Interest
Coverage 1.14x (<3x), both FY26 audited → **classification capped at
AVOID**, independent of the core-score outcome below.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 0

No shareholding-pattern filing, no annual report, and no promoter-pledge
disclosure exist in the provided inputs (screening CSVs contain no
shareholding rows; the two results filings are Reg. 33 financial-results
filings only and carry no shareholding schedule).

- **E1 Promoter holding**: N/A (not in provided data). **E1 = 0**
- **E2 Promoter holding change, 3 years**: N/A (not in provided data).
  **E2 = 0**
- **E3 Promoter pledge**: N/A (not in provided data). **E3 = 0**
- **E4 Contingent liabilities ÷ Net Worth**: N/A (not in provided data —
  no annual-report notes to accounts in inputs). **E4 = 0**

**Block E total = 0 / 20**

Note (unanchored, weighed not scored): COMPANY MEMORY reports Jun-2026
promoter holding 63.03% (flat since Sep-2023), FIIs 1.94%, DIIs 0.04%,
~33,028 shareholders, no promoter-holding change in 3 years. This is
operator memory, not an input-source anchor, and per Gate 0 rules cannot
be scored. If accurate it would likely score E1=5 (≥60%) and E2=3 (±1%),
but Block E stands at 0 pending an anchored shareholding filing.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 12

Peer set (true water/environmental-infra comparables): AWHCL, EIEL,
EMSLIMITED, WABAG (peer screening CSVs).

Peer EBITDA margin FY26 (Operating Profit ÷ Sales, using screener's own
quarterly Operating Profit line where the annual P&L breakdown had
blanks/gaps — AWHCL-Data_Sheet, EIEL-Data_Sheet, EMSLIMITED-Data_Sheet,
WABAG-Data_Sheet):
- AWHCL: (36.15+... quarterly OP FY26: 55.06+50.69+42.73+56.95=205.43) ÷
  1,053.19 = **19.5%**
- EIEL: quarterly OP FY26 (64.22+64.94+67.76+79.91=276.83) ÷ 1,145.60 =
  **24.2%**
- EMSLIMITED: quarterly OP FY26 (54.11+37.17+30.75+18.31=140.34) ÷
  732.75 = **19.1%**
- WABAG: quarterly OP FY26 (95.6+89.3+121.5+156.1=462.5) ÷ 3,944.2 =
  **11.7%**
- Peer median = avg(19.1%, 19.5%) = **19.3%**
- JITF FY26 (quarterly OP sum 558.40 ÷ Sales 2,808.02) = **19.9%**, i.e.
  +0.6pp above peer median.

**M1 Pricing Power**: OPM expanded FY17 (8.15%, screener-data, computed)
→ FY26 (19.14%, screener-data, computed) — expansion of ~11pp, far
exceeding 2pp — AND Revenue CAGR 20.03% (≥10%). **M1 = 5**

**M2 Cost Advantage vs peer median**: JITF 19.9% vs peer median 19.3% =
+0.6pp, within ±2pp band. **M2 = 1**

**M3 Capital Efficiency**: FAT = Sales ÷ Net Block = 2,808.02 ÷ 1,838.97
= **1.53x** (screener-data). ROCE FY26 = 13.31% (Block A). FAT >1x AND
ROCE >12% band. **M3 = 1**

**M4 Customer Stickiness**: 2 revenue-decline years (FY18, FY25), overall
CAGR positive. Band "2 decline years, CAGR positive". **M4 = 1**

**M5 Scale & Dominance**: Market cap (screener-data): JITF ₹892.83 Cr is
the **smallest** of the 5 named comparables — AWHCL ₹1,117.6 Cr,
EMSLIMITED ₹2,121.28 Cr, EIEL ₹3,577.58 Cr, WABAG ₹11,884.84 Cr. Not
largest, not top-3. (Treating "top 5 of a 5-name sample" as trivially
true would not be a meaningful scale signal, so not credited.) **M5 = 0**

**M6 Technology / R&D**: No R&D disclosure in any provided input for
JITF. N/A. **M6 = 0**

**M7 Regulatory / License**: JITF operates under municipal
waste/water concession agreements (regulated), but the total count of
listed players in the segment is not established by the provided
inputs — only 5 comparables are named and completeness of that universe
is not confirmed. **PEER DATA NEEDED. M7 = 0**

**M8 Distribution**: No quantified distribution/reach data in provided
inputs. **M8 = 0**

**M9 Brand** (GM proxy = (Revenue − Material Cost) ÷ Revenue, stated
proxy): JITF FY26 = (2,808.02 − 1,065.75) ÷ 2,808.02 = **62.05%**
(screener-data, computed). Peer comparison is compromised: EMSLIMITED and
WABAG disclose no Raw Material Cost line at all in any year (**PEER DATA
NEEDED**); AWHCL's Raw Material Cost is near-zero (₹12.21 Cr FY26 on
₹1,053.19 Cr sales — a waste-collection service model with minimal
"material" cost by nature), giving a GM proxy of 98.8% that is not
economically comparable to an EPC/infrastructure cost structure; only
EIEL has a usable figure (34.7%). With the peer set this degraded, no
reliable brand-premium claim can be substantiated. **M9 = 0**

**M10 Switching Costs**: 2 revenue-decline years within overall growth
(same as M4 evidence). Band "overall growth, 2+ decline years". **M10 =
1**

**M11 Network Effects** (10 years available, ≥6-year test applies):
Latest 3yr revenue CAGR (FY23→FY26) = (2,808.02/1,589.14)^(1/3) − 1 =
**20.90%**. Prior 3yr CAGR (FY20→FY23) = (1,589.14/844.14)^(1/3) − 1 =
**23.49%**. Latest is *not* greater than prior, so the top band fails.
Next band: latest 3yr CAGR ≥20% AND selling-expense % of sales
declining — Selling & admin % of sales: FY23 3.24% → FY26 2.77%,
declining (screener-data, computed). Band qualifies. **M11 = 3**

**M12 Negative WC / Float**: Cannot compute WC Days per formula for
FY17-FY24 (Trade Payables not disclosed — see Block B4). The 2 years
where full data exists (FY25: 56.03 days, FY26: 65.05 days — see B4
supplementary calc) both exceed 45 days, i.e. both confirmed data points
fall in the ">45 days" (score 0) band, not negative or low. Scored
conservatively on the available evidence rather than guessed for the
missing years. **M12 = 0**

| Test | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|------|---:|---:|---:|---:|---:|---:|---:|---:|---:|----:|----:|----:|
| Score| 5 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 |

**Block F (Moat) total = 12 / 60**

Moats "present" (score ≥3): M1 (Pricing Power, 5), M11 (Network Effects,
3) → **2 moats present → MODERATE** classification (band: 2-3 present).

Moat profile:
```
M1  Pricing Power      [#####] 5  PRESENT
M2  Cost Advantage     [#....] 1
M3  Capital Efficiency [#....] 1
M4  Cust. Stickiness   [#....] 1
M5  Scale & Dominance  [.....] 0
M6  Tech / R&D         [.....] 0
M7  Regulatory/License [.....] 0  PEER DATA NEEDED
M8  Distribution       [.....] 0
M9  Brand              [.....] 0  PEER DATA NEEDED
M10 Switching Costs    [#....] 1
M11 Network Effects    [###..] 3  PRESENT
M12 Negative WC/Float  [.....] 0
```

---

## DATA CONFIDENCE

10 years of history (FY17-FY26) → **"10+ yrs full"** confidence tier.
No history-based downgrade applies. **history_downgrade: false**

---

## CLASSIFICATION

| Block | Score | Max |
|-------|------:|----:|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation Quality | 0 | 20 |
| C — Growth | 8 | 20 |
| D — Balance Sheet Strength | 2 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **Core score** | **15** | **100** |
| F — Moat (12 tests) | 12 | 60 |
| **Grand total** | **27** | **160** |

Moat classification: MODERATE (2 of 12 tests present)

Classification matrix: Core score 15 (<40) → **AVOID** on the core-score
rule alone.

**Deal-breakers triggered:**
1. Block A (5) < 8 → max GOOD — triggered, superseded by stricter rules below
2. Block B (0) < 8 → max GOOD — triggered, superseded by stricter rules below
3. Median ROCE (5.34%) < 10% → max AVERAGE — triggered
4. Cumulative CFO/PAT (-0.81) < 0.50 → max AVERAGE — triggered
6. **Net Debt/EBITDA (6.71x) >3x AND Interest Coverage (1.14x) <3x →
   AVOID — TRIGGERED (FY26, audited results filing)**
8. PAT negative in FY26 (one of the last 3 years, FY24-FY26) → max
   AVERAGE — triggered

Deal-breakers not triggered: #5 (pledge, unanchored — no evidence
either way), #7 (revenue declined 2 of 9 years, not a majority), #9
(history = 10 years, well above the 3-year floor).

```
╔══════════════════════════════════════════╗
║  CLASSIFICATION: AVOID                    ║
║  Core score: 15/100  |  Moat: MODERATE    ║
║  Grand total: 27/160                      ║
║  Deal-breaker #6 (ND/EBITDA 6.71x + IC     ║
║  1.14x) independently forces AVOID         ║
╚══════════════════════════════════════════╝
```

**Strongest block**: C — Growth (8/20), driven by a clean 20% revenue
CAGR (C1=5) on the back of the water/urban-infra segment build-out.

**Weakest blocks**: B — Cash Generation Quality and E — Shareholder
Alignment, tied at 0/20. B is a genuine mechanical result (negative
cumulative CFO/PAT ratio, both years of measurable FCF negative); E is an
evidence gap (no shareholding filing provided), not a demonstrated
governance failure — flagged separately as FLAG-SHAREHOLDING.

**Decision line**: Gate 0 does not halt on company quality — flags
propagate to downstream stages per pipeline rules. This scorecard records
AVOID with two independent triggers (core score <40, and the
Deal-breaker #6 leverage/coverage combination), plus a live data gap in
Block E that the operator should weigh against COMPANY MEMORY (unanchored
63.03% promoter holding) before treating the AVOID as final. FCF has been
negative in both years capex is actually disclosed (FY25, FY26), and
Net Debt/EBITDA of 6.71x against Interest Coverage of 1.14x describes a
company financing continued capex through debt at a pace its EBIT does
not yet cover comfortably.

---

## INPUT GAPS

- prospectus: absent
- rating: absent
- announcements: absent
- shareholding: absent (no shareholding-pattern filing in inputs)
- research: absent
- presentation: absent
- concalls: absent (concalls_available: false)
- Trade Payables: not disclosed in screener CSV for FY17-FY24 (only
  derivable for FY25/FY26 from the results filings) — blocks B4 and M12
  from being computed per the specified formula for the full window
- Capex (Purchase of PPE): not disclosed in screener CSV for any year;
  only available for FY25/FY26 from the FY26 results filing's audited
  cash flow statement — blocks B2/B3 from being computed for FY17-FY24
- Contingent liabilities: not in provided data (no annual report / notes
  to accounts) — blocks E4
- Peer Raw Material Cost: EMSLIMITED and WABAG disclose no Raw Material
  Cost line in any year of their screener exports — degrades M9
- Peer segment universe count: not established beyond the 4 named
  comparables — degrades M7
