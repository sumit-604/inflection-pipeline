# STAGE 1: GATE 0 SCORECARD — Vilas Transcore Ltd (VILAS)
Run: vilas-2026-09-03 | Model: Sonnet 5 | Mode: pipeline (no human in loop)
Classification context (from B00, not a source): CONVERTER (Section 1B v3.7
Amendment 17), CRGO electrical-steel lamination converter. Manifest sector
row "Pharma/CDMO" is a collector error, ignored.

Data available: 7 years (FY2020 to FY2026), screener-data only. Scoring
adapted to a 7-year history for revenue, PAT, receivables, inventory,
cash & bank, borrowings and equity (all present in screener-Data_Sheet.csv
for all 7 years). ROCE, Current Ratio, FCF/Capex, Working-Capital-Days and
Block E (shareholder alignment) are N/A for EVERY year — see CRITICAL DATA
GAP below — because the two results PDFs supplied for this run could not be
extracted in this session.

## CRITICAL DATA GAP — BOTH RESULTS PDFs UNREADABLE THIS SESSION
`VILAS_11052026191340_NSE_Outcome31326_VILAS_final.pdf` (FY26 audited) and
`VILAS_13112025192806_FinancialResults.pdf` (H1 FY26) were provided as
inputs but could not be read in this tool session:
- Grep for balance-sheet keywords ("Total Assets", "Current Liabilities",
  "Trade Receivables", "Trade Payables", "Current Ratio") returned zero
  matches in the FY26 audited PDF — confirms it is scanned/image-based with
  no embedded text layer.
- Page-range rendering ("pages" parameter) failed with a hard tool error:
  `pdftoppm is not installed` (poppler-utils missing in this environment).
- Whole-file reads of both PDFs returned `[media removed: request limit]`
  with zero page content on every attempt (4 attempts across both files).

Net effect: NONE of the balance-sheet detail behind these two filings
(Trade Payables, Current Liabilities split, Capex/PPE purchases,
shareholding pattern, pledge, contingent liabilities) reached this stage.
Every number in this report is sourced from `screener-Data_Sheet.csv`
alone (anchored "screener-data"); `screener-Profit_Loss.csv`,
`screener-Balance_Sheet.csv`, `screener-Cash_Flow.csv` and
`screener-Quarters.csv` are empty templates (headers only, no data rows) —
confirmed by direct read, not assumed.

Operator cross-check anchors (FY26 revenue Rs 460.7 Cr, EBITDA Rs 51.5 Cr,
PAT Rs 39.6 Cr, EPS Rs 16.16, book value Rs 134) were NOT used as sourced
anchors (per task instruction, cross-check only) but line up closely with
this stage's independent screener-derived figures: Sales Rs 460.67 Cr
(screener-data), Net profit Rs 39.56 Cr (screener-data), computed EBITDA
Rs 51.46 Cr = 11.17% margin (computed: PBT+Dep+Interest−Other Income,
screener-data), computed book value Rs 134.09/share (computed: Equity Rs
328.53 Cr ÷ 2.45 Cr adjusted shares, screener-data). Operator ROCE ~16%
and 55% utilisation could not be independently verified this session
(capital-employed and volume data absent from readable inputs).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 4/20

| # | Metric | Value | Score |
|---|---|---|---|
| A1 | Median ROCE | N/A (not in provided data) — formula needs Current Liabilities, absent for all 7 years; screener's own ROCE field is blank (screener-Balance_Sheet.csv) | 0 |
| A2 | Minimum single-year ROCE | N/A (not in provided data), same reason | 0 |
| A3 | Median ROE | 15.27% (computed: PAT ÷ avg Net Worth, screener-data — series below) | 4 |
| A4 | ROCE trend, latest vs earliest | N/A (not in provided data), same reason | 0 |

ROE series (PAT ÷ average Net Worth; FY20 uses closing equity only, no
FY19 opening available, stated per rule):
- FY20: 3.60 ÷ 95.76 (screener-data) = 3.76%
- FY21: 5.23 ÷ avg(95.76, 100.29) (screener-data) = 5.34%
- FY22: 17.91 ÷ avg(100.29, 117.51) (screener-data) = 16.45%
- FY23: 20.21 ÷ avg(117.51, 136.98) (screener-data) = 15.88%
- FY24: 23.08 ÷ avg(136.98, 159.36) (screener-data) = 15.58%
- FY25: 34.17 ÷ avg(159.36, 288.09) (screener-data) = 15.27% ← median
- FY26: 39.56 ÷ avg(288.09, 328.53) (screener-data) = 12.83%

Net Worth (Equity Share Capital + Reserves, screener-data): FY20 95.76,
FY21 100.29, FY22 117.51, FY23 136.98, FY24 159.36, FY25 288.09, FY26
328.53 (Cr).

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 1/20

| # | Metric | Value | Score |
|---|---|---|---|
| B1 | Cumulative CFO ÷ Cumulative PAT | 79.55 ÷ 143.76 = 0.5534x (computed, screener-data) | 1 |
| B2 | FCF-positive years proportion | N/A (not in provided data) — Capex isolated from cash flow statement not available in any input; screener only gives aggregate "Cash from Investing Activity" (not equivalent to capex) | 0 |
| B3 | Cumulative FCF ÷ Cumulative PAT | N/A (not in provided data), same reason | 0 |
| B4 | Change in WC Days, latest vs earliest | N/A (not in provided data) — Payable Days needs Trade Payables, absent from every provided sheet | 0 |

CFO series (Cr, screener-data): FY20 21.69, FY21 19.76, FY22 12.91, FY23
13.19, FY24 49.16, FY25 −35.46, FY26 −1.70. Cumulative = 79.55.
PAT series (Cr, screener-data): FY20 3.60, FY21 5.23, FY22 17.91, FY23
20.21, FY24 23.08, FY25 34.17, FY26 39.56. Cumulative = 143.76.

Note: cumulative CFO/PAT of 0.5534 sits just above the 0.50 deal-breaker
threshold (#4, cumul CFO/PAT <0.50 → max AVERAGE) — a near miss, flagged
for downstream attention.

## BLOCK C: GROWTH (Max 20) — Score: 17/20

| # | Metric | Value | Score |
|---|---|---|---|
| C1 | Revenue CAGR (FY20→FY26) | (460.67÷161.91)^(1/6)−1 = 19.04% (computed, screener-data) | 4 |
| C2 | PAT CAGR (FY20→FY26) | (39.56÷3.60)^(1/6)−1 = 49.10% (computed, screener-data) | 5 |
| C3 | Positive YoY revenue years | 5 of 6 transitions positive (FY21 declined vs FY20; FY22-FY26 all grew) = 83.3% (screener-data) | 3 |
| C4 | PAT CAGR − Revenue CAGR | 49.10% − 19.04% = +30.06pp (computed) | 5 |

Revenue series (Cr, screener-data): FY20 161.91, FY21 132.65 (decline,
COVID-affected year), FY22 233.03, FY23 282.61, FY24 309.74, FY25 353.05,
FY26 460.67.

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 14/20

| # | Metric | Value | Score |
|---|---|---|---|
| D1 | Net Debt ÷ EBITDA (FY26) | Borrowings 38.96 Cr − Cash&Bank 94.36 Cr (screener-data) = net cash of −55.40 Cr | 5 |
| D2 | Interest Coverage EBIT÷Interest (FY26) | EBIT 53.77 Cr (PBT 51.65 + Interest 2.12, screener-data) ÷ Interest 2.12 Cr = 25.36x | 5 |
| D3 | Debt ÷ Equity (FY26) | 38.96 ÷ 328.53 (screener-data) = 0.1186x | 4 |
| D4 | Current Ratio (FY26) | N/A (not in provided data) — screener-Data_Sheet.csv does not split current vs non-current assets/liabilities; the split was to come from the unreadable FY26 audited PDF | 0 |

FY26 EBITDA computed = PBT 51.65 + Dep 4.29 + Interest 2.12 − Other Income
6.60 (all screener-data) = 51.46 Cr = 11.17% margin.

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 0/20

| # | Metric | Value | Score |
|---|---|---|---|
| E1 | Promoter holding (latest quarter) | N/A (not in provided data) — no shareholding pattern supplied in any input | 0 |
| E2 | Promoter holding change, 3yr | N/A (not in provided data), same reason | 0 |
| E3 | Promoter pledge (latest) | N/A (not in provided data), same reason | 0 |
| E4 | Contingent liabilities ÷ Net Worth | N/A (not in provided data) — no AR/notes-to-accounts supplied this run | 0 |

This is a pure data gap, not evidence of poor alignment. No shareholding
file of any kind (aggregator or primary) was part of this run's inputs.

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 10/60

| # | Test | Finding | Score |
|---|---|---|---|
| M1 | Pricing Power | EBITDA margin expanded from 4.42% (FY20) to 11.17% (FY26), +6.75pp (computed, screener-data); revenue CAGR 19.04% ≥10% → top tier | 5 |
| M2 | Cost Advantage vs peers | PEER DATA NEEDED — no peer/sector data provided | 0 |
| M3 | Capital Efficiency | FAT = 460.67÷81.79 (screener-data) = 5.63x >3x, but ROCE component N/A (Block A) — tier cannot be verified | 0 |
| M4 | Customer Stickiness | 1 revenue-decline year (FY21), fully recovered thereafter (screener-data) — matches "max 1 decline year, fully recovered" tier | 3 |
| M5 | Scale & Dominance | PEER DATA NEEDED — no mcap/segment ranking data provided | 0 |
| M6 | Technology/R&D | No R&D line item in any provided data | 0 |
| M7 | Regulatory/License | CRGO lamination conversion is an unregulated, unlicensed segment | 0 |
| M8 | Distribution | No distribution-network data; B2B converter, not applicable | 0 |
| M9 | Brand | PEER DATA NEEDED — GM proxy computed (Revenue−Raw Material)/Revenue = 15.38% FY26 vs 18.06% FY20 (screener-data), but no peer median to compare against | 0 |
| M10 | Switching Costs | Revenue grew all but 1 year (5/6), but receivable days swung from 106.7 (FY20) to 34.7 (FY22) to 61.4 (FY26) (computed, screener-data) — too volatile to call "stable"; scored conservatively between tiers | 1 |
| M11 | Network Effects | Latest 3yr rev CAGR (FY23→FY26) 17.69% < prior 3yr CAGR (FY20→FY23) 20.41% (computed, screener-data) — decelerating, not accelerating; selling expense % rose from 0.88% (FY24) to 1.35% (FY25, screener-data; FY26 blank) while growth >15% → matches "growth >15% but selling% rising" tier | 1 |
| M12 | Negative WC/Float | N/A (not in provided data) — WC Days formula needs Trade Payables, absent from every input | 0 |

Moats present (score ≥3): M1 (5), M4 (3) = 2 present → MODERATE
(2-3 present band).

Moat profile:
```
M1  #####  5/5  PRESENT
M2  -      0/5  PEER DATA NEEDED
M3  -      0/5  N/A (ROCE absent)
M4  ###    3/5  PRESENT
M5  -      0/5  PEER DATA NEEDED
M6  -      0/5
M7  -      0/5
M8  -      0/5
M9  -      0/5  PEER DATA NEEDED
M10 #      1/5
M11 #      1/5
M12 -      0/5  N/A (payables absent)
```

---

## SCORING SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 4 | 20 |
| B — Cash Generation Quality | 1 | 20 |
| C — Growth | 17 | 20 |
| D — Balance Sheet Strength | 14 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **Core Score** | **36** | **100** |
| F — Moat Score | 10 | 60 |
| **Grand Total** | **46** | **160** |

Strongest block: C — Growth (17/20). Weakest block: E — Shareholder
Alignment (0/20, entirely a data gap) and B — Cash Generation Quality
(1/20, partly data gap, partly a real cumulative CFO/PAT weakness of
0.55x).

Data confidence: 7 years of screener P&L/partial-BS data → "7-9 moderate"
band, no automatic downgrade. (Note: this masks that ROCE, Current
Ratio, FCF and WC Days have ZERO usable years, not 7 — a data-completeness
gap distinct from the years-of-history dimension.)

Deal-breaker overrides evaluated:
1. Block A <8 (=4/20) → max GOOD. Triggered, non-binding (base
   classification below GOOD already).
2. Block B <8 (=1/20) → max GOOD. Triggered, non-binding, same reason.
3. Median ROCE <10% → max AVERAGE. NOT EVALUABLE — ROCE data entirely
   absent this session.
4. Cumulative CFO/PAT <0.50 → max AVERAGE. NOT triggered (0.5534, a near
   miss above the line).
5. Pledge >15% → max AVERAGE. NOT EVALUABLE — no pledge data supplied.
6. ND/EBITDA >3x AND IC <3x → AVOID. NOT triggered (net cash, IC 25.4x).
7. Revenue declined majority of years → max AVERAGE. NOT triggered
   (1 of 6 years).
8. PAT negative in any of last 3 years → max AVERAGE. NOT triggered
   (FY24-26 all positive).
9. History <3 years → AVERAGE. NOT triggered (7 years of screener P&L
   history).

## CLASSIFICATION

```
Core Score:   36/100   (band: Core <40)
Moat Class:   MODERATE (2 of 12 tests present)
Matrix:       Core <40 = AVOID
──────────────────────────────
CLASSIFICATION: AVOID
```

## DECISION LINE

Mechanically, Core <40 maps to AVOID under the fixed matrix. This
classification is DATA-GAP DRIVEN, not fundamentals-driven: both source
results PDFs for this run were unreadable in this session (scanned
images, no text layer; no PDF-page renderer available), which zeroed
ROCE (A1/A2/A4), Current Ratio (D4), FCF and WC Days (B2/B3/B4), two moat
tests (M3, M12), and all of Block E (no shareholding data was supplied at
all, not even an aggregator extract). The screener-only numbers that DID
extract describe a business growing fast with expanding margins and a net
cash balance sheet (revenue CAGR 19.0%, PAT CAGR 49.1%, EBITDA margin
4.4%→11.2%, D/E 0.12x, interest cover 25.4x, median ROE 15.3%). The one
real, screener-visible weak spot is cash conversion: cumulative CFO/PAT
of 0.55x, with CFO negative in both FY25 (−Rs 35.46 Cr) and FY26
(−Rs 1.70 Cr) despite rising PAT — plausibly tied to a post-IPO
capex/working-capital ramp (equity base roughly tripled from Rs 159.36 Cr
FY24 to Rs 328.53 Cr FY26, screener-data), but this cannot be confirmed
without the unreadable balance-sheet detail. Before this AVOID is used
for any downstream decision, re-supply the two results PDFs in
extractable form (or OCR'd) plus the shareholding pattern; Core is
expected to move well above 40 once ROCE, Current Ratio and Block E can
be scored on real data.

---

```yaml
stage: B01-gate0
company: "VILAS"
run_date: "2026-09-03"
model: claude-sonnet-5
status: complete
input_gaps:
  - "prospectus ABSENT (HIGH) - restated FY20-FY22 pre-listing financials not in corpus"
  - "FY26 annual report NOT FILED (HIGH, freshness) - FY26 figures sourced from audited results filing + screener only"
  - "results PDFs (FY26 audited, H1 FY26) UNREADABLE this session (HIGH, NEW) - scanned/image-based, no text layer, PDF page-rendering unavailable (poppler missing); whole-file reads hit a media/request limit with zero content returned on 4 attempts; all figures in this report sourced from screener-Data_Sheet.csv only"
  - "shareholding pattern NOT PROVIDED in any input (HIGH) - Block E entirely N/A"
  - "trade payables / current-liabilities split NOT PROVIDED in any readable input (HIGH) - ROCE (A1/A2/A4), Current Ratio (D4), WC Days (B4, M12) entirely N/A"
  - "capex breakdown NOT PROVIDED in any readable input (HIGH) - FCF (B2, B3) entirely N/A"
  - "announcements primary PDFs (partial)"
  - "peer/sector data NOT PROVIDED - M2, M5, M9 scored 0, PEER DATA NEEDED"
flags:
  - type: FLAG-GATE0
    reason: "Classification computed as AVOID (Core 36/100, Core<40 band) but this is DATA-GAP DRIVEN, not fundamentals-driven: both source results PDFs (FY26 audited, H1 FY26) were unreadable in this session (scanned, no text layer; PDF page-rendering unavailable), zeroing ROCE (A1/A2/A4), Current Ratio (D4), FCF and WC-Days (B2/B3/B4), two moat tests (M3, M12), and all of Block E (no shareholding/pledge/contingent-liability data was available in any provided input). Visible screener-only fundamentals are strong: revenue CAGR 19.0%, PAT CAGR 49.1%, EBITDA margin expanded from 4.4% to 11.2%, Debt/Equity 0.12x, interest coverage 25.4x, net cash balance sheet, median ROE 15.3%. Re-run Gate 0 once the two results PDFs are re-supplied in text-extractable form (or OCR'd) and the shareholding pattern / FY25 AR notes are added as inputs, before treating AVOID as a real signal."
data_years: 7
fy_range: "FY2020 to FY2026"
blocks: {A: 4, B: 1, C: 17, D: 14, E: 0}
core_score: 36
moat_score: 10
grand_total: 46
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "Block A <8 (=4/20) -> max GOOD (triggered, non-binding)"
  - "Block B <8 (=1/20) -> max GOOD (triggered, non-binding)"
  - "median ROCE <10% -> max AVERAGE (NOT EVALUABLE, ROCE data absent)"
  - "cumulative CFO/PAT <0.50 -> max AVERAGE (NOT triggered, 0.5534 near miss)"
  - "pledge >15% -> max AVERAGE (NOT EVALUABLE, no pledge data)"
history_downgrade: false
data_notes:
  - "Both results PDFs unreadable this session: no embedded text layer (confirmed via keyword search) and PDF page-rendering unavailable (poppler/pdftoppm not installed); whole-file conversion hit a media/request limit with zero content returned. All figures sourced from screener-Data_Sheet.csv only."
  - "screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv are empty templates (headers only, no data rows), confirmed by direct read."
  - "ROCE (A1,A2,A4) and Current Ratio (D4) N/A for all years: formula needs Current Liabilities, not split from Total Liabilities in screener-Data_Sheet.csv; screener's own ROCE field is also blank."
  - "WC Days (B4, M12) N/A for all years: Payable Days needs Trade Receivables/Payables, and Trade Payables is not present in any provided sheet for any year."
  - "FCF (B2, B3) N/A for all years: Capex (purchase of PPE+intangibles) not isolated from the aggregate 'Cash from Investing Activity' line in screener-Data_Sheet.csv; no substitution attempted."
  - "Operator cross-check anchors (FY26 revenue Rs460.7 Cr, EBITDA Rs51.5 Cr, PAT Rs39.6 Cr, book value Rs134) are consistent with this stage's independently derived screener figures (Sales Rs460.67 Cr, Net profit Rs39.56 Cr, computed EBITDA Rs51.46 Cr = 11.17% margin, computed book value Rs134.09/share) but were not used as sourced anchors, per task instruction."
  - "FY21 is the sole revenue-decline year in the 7-year window (Rs132.65 Cr vs Rs161.91 Cr FY20, screener-data), consistent with a COVID-affected year; revenue grew every year after."
  - "Equity share capital rose Rs3.0 Cr (FY20-23) -> Rs18.0 Cr (FY24) -> Rs24.48 Cr (FY25-26), and Reserves jumped at FY25 (Rs141.36 Cr to Rs263.61 Cr), consistent with a bonus issue and IPO/listing event around FY24-FY25 (screener-data). This is a likely driver of the ROE decline in later years and should be read as a capital-base/dilution effect, not an operating deterioration, when read downstream."
block_b_trend: "deteriorating - cumulative CFO/PAT = 0.55x (screener-data); CFO turned negative in FY25 (Rs-35.46 Cr) and stayed negative in FY26 (Rs-1.70 Cr) despite PAT of Rs34.17 Cr and Rs39.56 Cr respectively, a widening cash-earnings gap"
analyst_note: "AVOID (Core 36/100) is driven almost entirely by unreadable source PDFs, not weak fundamentals. Both results filings are scanned image PDFs with no text layer; this session's PDF renderer also lacks poppler, so page-range extraction failed too. That zeroed ROCE, current ratio, FCF, WC days, two moat tests, and all of Block E (no shareholding data was supplied at all). The screener-only numbers that DID extract look like a genuine post-IPO small-cap converter: revenue CAGR 19%, PAT CAGR 49%, EBITDA margin nearly tripled (4.4% to 11.2%), net cash balance sheet, D/E 0.12x, 25x interest cover, median ROE 15.3%. Cash conversion is the one real screener-visible weak spot: cumulative CFO/PAT is 0.55x, and CFO turned negative in FY25 and FY26 despite rising PAT, likely tied to an IPO-era capex/working-capital ramp (equity base roughly tripled FY24 to FY26). Before this AVOID is used for any decision, re-supply the two results PDFs in extractable form (or OCR them) plus the shareholding pattern; expect Core to move well above 40 once ROCE, current ratio and Block E can be scored on real data."
```
