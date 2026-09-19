# STAGE 1: GATE 0 SCORECARD — Rappid Valves (India) Ltd (RAPPID)
Run date: 2026-09-19 | Model: claude-sonnet-5

Data available: 5 years (FY22 to FY26). Scoring adapted to 5-year history.
Source hierarchy used: screener-Data_Sheet.csv for the continuous 5-year
P&L/BS/CF series (INR Cr); FY26 Annual Report (INR Lakhs, converted to Cr)
for line items screener does not carry (contingent liabilities, trade
payables, capex, promoter holding, disclosed ratios); RHP Sep-2024 (INR
Lakhs, restated, converted to Cr) for the pre-listing years FY22-FY24 where
the AR does not go back that far (current liabilities, capex, pre-IPO
promoter holding). Every number below is followed by its source.

## LOAD-BEARING FACT CHECK (company memory, verified against this run's filings)

Per CLAUDE.md this is memory to weigh, never evidence; checked against the
provided filings before scoring:

1. CFO negative FY23-FY26: CONFIRMED. FY23 -0.43, FY24 -2.48, FY25 -12.82,
   FY26 -10.83 Cr (screener-Data_Sheet.csv); cumulative -26.56 Cr, matches
   memory's "-26.6 Cr" claim.
2. Debtor days ~170 (FY26): CONFIRMED closely. This stage computes 170.24
   days (Receivables 24.83 Cr ÷ Revenue 53.23 Cr × 365; screener-Data_Sheet.csv).
3. Inventory days ~258 (FY26): NOT RECONCILED. This stage's prescribed
   formula (Inventory ÷ Revenue × 365, revenue basis, no COGS line
   explicitly available) gives 182.9 days, not 258. Basis difference not
   resolved from provided documents; memory figure not used as evidence,
   own computed figure used for scoring.
4. Borrowings Rs 8.4 Cr to Rs 17.9 Cr in FY26: CONFIRMED. FY25 8.41 Cr, FY26
   17.85 Cr (screener-Data_Sheet.csv); AR confirms this is entirely
   short-term borrowings, Rs 1,784.3 Lakh (AR p.55, Balance Sheet Note 9),
   up from Rs 841.4 Lakh FY25.
5. Rs 7.65 Cr IPO proceeds moved to working capital: CONFIRMED. AR MD&A
   states Rs 764.51 Lakh reallocated to working capital after the 17-Apr-2026
   EGM (AR p.27).
6. Investments Rs 0.57 Cr to Rs 4.76 Cr in FY26: CONFIRMED (screener-Data_Sheet.csv,
   BALANCE SHEET, Investments row).
7. Auditor Kava & Associates: CONFIRMED (AR p.41 and p.60-61 area, consent
   and signature references).

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score 15

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed
(source does not provide its own ROCE on this exact basis; screener's Data
Sheet export carries no ratio rows). EBIT = PBT + Finance Costs − Other
Income (basis confirmed as the standard definition by RHP's own KPI note,
RHP p.151, "(6) Return on Capital Employed... Profit before tax + Finance
Costs – Other Income (EBIT)"). Capital Employed = Total Assets (screener-Data_Sheet.csv)
− Current Liabilities (RHP p.215 restated BS for FY22-24; AR p.55 audited
BS for FY25-26).

| Year | PBT | Interest | Other Inc | EBIT | Total Assets | Current Liab | Cap Employed | ROCE |
|---|---|---|---|---|---|---|---|---|
| FY22 | 0.29 | 1.46 | 0.01 | 1.74 | 12.17 | 10.13 (RHP p.215) | 2.04 | 85.4% |
| FY23 | 0.63 | 1.44 | 0.04 | 2.03 | 16.57 | 11.44 (RHP p.215) | 5.13 | 39.5% |
| FY24 | 5.53 | 1.40 | 0.09 | 6.84 | 29.96 | 15.62 (RHP p.215) | 14.34 | 47.7% |
| FY25 | 8.24 | 1.12 | 0.21 | 9.15 | 60.26 | 14.89 (AR p.55) | 45.37 | 20.2% |
| FY26 | 8.66 | 1.33 | 0.32 | 9.67 | 75.32 | 23.52 (AR p.55) | 51.80 | 18.7% |

(PBT, Interest, Other Income, Total Assets: screener-Data_Sheet.csv, all
figures Rs Cr.)

DATA NOTE: FY22 ROCE of 85.4% is a small-base distortion — capital
employed was only Rs 2.04 Cr against reserves that were still negative
(-Rs 0.8 Cr, screener-Data_Sheet.csv) at that balance-sheet date. It
pulls the median upward relative to the FY23-FY26 run rate (18.7%-47.7%).
Reported per the fixed formula with no adjustment (Rule 2, no qualitative
judgment).

Cross-check: RHP's own disclosed ROCE (different denominator, Net
worth + Total Debt, RHP p.150-151/p.237) reads FY24 29.88%, FY23 15.85%,
FY22 18.38% — directionally consistent (rising then normalising) but not
numerically comparable to this stage's fixed formula.

- A1 Median ROCE = 39.5% (sorted: 18.7, 20.2, 39.5, 47.7, 85.4) → ≥25% → **5**
- A2 Minimum single-year ROCE = 18.7% (FY26) → ≥15% → **5**
- A3 Median ROE = 27.5% (see below) → ≥20% → **5**
- A4 ROCE trend, latest (18.7%) vs earliest (85.4%) = decline 66.7pp → >5pp decline → **0**

ROE = PAT ÷ average Net Worth. Net Worth (Equity Capital + Reserves,
screener-Data_Sheet.csv, Rs Cr): FY22 -0.25, FY23 3.12, FY24 7.39, FY25
45.25, FY26 51.71.

| Year | PAT | Avg NW | ROE |
|---|---|---|---|
| FY22 | 0.29 | -0.25 (opening unavailable, closing used, stated) | N/M (negative net worth denominator) |
| FY23 | 0.46 | 1.44 | 32.1% |
| FY24 | 4.13 | 5.26 | 78.6% |
| FY25 | 6.04 | 26.32 | 22.9% |
| FY26 | 6.48 | 48.48 | 13.4% |

FY22 excluded from the median (negative-denominator division is not a
meaningful percentage even with positive PAT). Median over FY23-FY26 =
(22.9+32.1)/2 = 27.5%. Cross-check: AR's own disclosed Return on Net
Worth (AR p.27, Note 36 basis) reads FY26 13.4% (exact match to this
stage's figure) and FY25 21.0% (this stage: 22.9%, small basis
difference, not reconciled).

Block A = 5+5+5+0 = **15/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score 0

CFO (screener-Data_Sheet.csv, Rs Cr): FY22 1.14, FY23 -0.43, FY24 -2.48,
FY25 -12.82, FY26 -10.83. Cumulative FY22-FY26 CFO = -25.42 Cr.
Cumulative PAT = 17.40 Cr.

Capex (purchase of PPE, excl. acquisitions; RHP p.217 for FY22-24, AR
p.57 for FY25-26, Rs Cr): FY22 0.05, FY23 1.01, FY24 2.72, FY25 3.38,
FY26 1.79. FCF = CFO - Capex:

| Year | CFO | Capex | FCF |
|---|---|---|---|
| FY22 | 1.14 | 0.05 | 1.09 |
| FY23 | -0.43 | 1.01 | -1.44 |
| FY24 | -2.48 | 2.72 | -5.20 |
| FY25 | -12.82 | 3.38 | -16.20 |
| FY26 | -10.83 | 1.79 | -12.62 |

Cumulative FCF = -34.37 Cr.

DATA NOTE: RHP's restated FY24 CFO is -Rs 1.07 Cr (RHP p.217 area,
line-item reconciliation), against -Rs 2.48 Cr in screener-Data_Sheet.csv
for the same year. Screener's continuous series used for all 5 years for
internal consistency; the discrepancy is not reconciled from the provided
documents.

- B1 Cumulative CFO ÷ Cumulative PAT = -25.42/17.40 = -1.46 → <0.50 → **0**
- B2 FCF-positive years = 1 of 5 (FY22 only) = 20% → <50% → **0**
- B3 Cumulative FCF ÷ Cumulative PAT = -34.37/17.40 = -1.98 → <0.20 (negative) → **0**
- B4 WC Days change, latest vs earliest (see table below) = +183.9 days → >15 increase → **0**

Working Capital Days = Receivable Days + Inventory Days − Payable Days,
revenue basis (no explicit standalone COGS line in the provided data).
Trade Payables: RHP p.215 for FY22-24, AR p.55 for FY25-26 (Rs Cr).

| Year | Receivables | Inventory | Payables | Revenue | Rec Days | Inv Days | Pay Days | WC Days |
|---|---|---|---|---|---|---|---|---|
| FY22 | 2.63 | 4.60 | 2.23 | 12.14 | 79.1 | 138.3 | 67.1 | 150.3 |
| FY23 | 3.27 | 6.99 | 2.45 | 16.4 | 72.8 | 155.5 | 54.4 | 173.9 |
| FY24 | 8.32 | 11.58 | 3.71 | 36.51 | 83.2 | 115.8 | 37.1 | 161.9 |
| FY25 | 19.23 | 16.17 | 4.12 | 52.13 | 134.7 | 113.2 | 28.8 | 219.1 |
| FY26 | 24.83 | 26.68 | 2.77 | 53.23 | 170.2 | 182.9 | 19.0 | 334.2 |

(Receivables, Inventory, Revenue: screener-Data_Sheet.csv.)

Block B = 0+0+0+0 = **0/20** — this is the weakest block and the
principal deal-breaker driver.

## BLOCK C: GROWTH (Max 20) — Score 20

Revenue (screener-Data_Sheet.csv, Rs Cr): FY22 12.14, FY23 16.40, FY24
36.51, FY25 52.13, FY26 53.23. PAT: FY22 0.29, FY23 0.46, FY24 4.13, FY25
6.04, FY26 6.48.

- C1 Revenue CAGR FY22-FY26 (4yr) = (53.23/12.14)^(1/4)-1 = 44.7% → ≥20% → **5**
- C2 PAT CAGR FY22-FY26 (4yr) = (6.48/0.29)^(1/4)-1 = 117.4% (both endpoints
  positive, no N/M) → ≥20% → **5**
- C3 Positive YoY revenue years: FY23 +35.1%, FY24 +122.6%, FY25 +42.8%,
  FY26 +2.1% — all 4 of 4 periods positive = 100% → **5**
- C4 PAT CAGR − Revenue CAGR = 117.4% − 44.7% = +72.7pp → ≥+3pp → **5**

Block C = 5+5+5+5 = **20/20** — the strongest block.

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score 16

Latest = FY26. EBITDA FY26 = Rs 10.31 Cr (AR p.20, "EBITDA 1,030.9" Lakh,
FY2026 Highlights). Borrowings FY26 = Rs 17.85 Cr, all short-term (AR
p.55, Note 9: Short-Term Borrowings Rs 1,784.3 Lakh, Long-Term Borrowings
Rs 0). Cash & Bank FY26 = Rs 2.51 Cr (screener-Data_Sheet.csv). Net Debt =
17.85 - 2.51 = Rs 15.34 Cr.

- D1 Net Debt ÷ EBITDA = 15.34/10.31 = 1.49x → 1-2x → **3**
- D2 Interest Coverage = 7.52x (AR p.27, Note 36 Key Financial Ratios,
  disclosed). Cross-check: this stage's EBIT/Interest = 9.67/1.33 = 7.27x,
  consistent. → 5-9.9x → **4**
- D3 Debt ÷ Equity = 0.35x (AR p.27, disclosed) → 0.1-0.5 → **4**
- D4 Current Ratio = 2.55x (AR p.27, disclosed; also AR p.69 Note 36) →
  ≥2.0 → **5**

Block D = 3+4+4+5 = **16/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score 17

- E1 Promoter holding, latest available (Mar-2026) = 51.58% (AR p.60,
  Note 3.7: Gaurav Dalal 47.97% + Vijay Dalal 3.61%). No shareholding
  pattern later than Mar-2026 in the provided documents. → 50-59.9% → **4**
  (Company memory cites 51.69% from screener/deck; AR Note 3.7, the
  audited primary source, used instead.)
- E2 Promoter holding change over 3 years: company listed only ~2 years
  (30-Sep-2024). Pre-IPO capital structure (69.46% pre-issue, RHP p.95) is
  not a valid comparator — the drop to 51.13% post-issue (RHP p.95) is IPO
  dilution, not promoter selling. Used the full available listed-history
  window instead: post-issue Sep-2024 51.13% (RHP p.95) to Mar-2026 51.58%
  (AR p.60) = +0.45pp → within ±1% → **3**
- E3 Promoter pledge, latest = 0%. RHP p.94: "our Promoter have not
  pledged any of the Equity Shares that they hold." No later pledge
  disclosure found in the provided documents to contradict this; AR
  Note 3.7 shows 0.00% holding change FY25-FY26 with no pledge column
  flagged. → 0% → **5**
- E4 Contingent Liabilities ÷ Net Worth = Rs 14.6 Lakh ÷ Rs 5,171.4 Lakh
  (AR p.68 Note, Performance Bank Guarantee, IDBI Bank; AR p.55,
  Shareholders' Funds) = 0.28% → <5% → **5**

Block E = 4+3+5+5 = **17/20**

Core score (A+B+C+D+E) = 15+0+20+16+17 = **68/100**

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score 15

- M1 Pricing Power: EBITDA margin FY23 13.0% to FY26 19.4% (AR p.20,
  4-year snapshot), +6.3pp expansion, ≥2pp; revenue CAGR FY23-FY26
  (3yr) = 48.1%, ≥10% → **5**
- M2 Cost Advantage vs peer median EBITDA margin: no peer EBITDA-margin
  dataset provided to this stage → **0, PEER DATA NEEDED**
- M3 Capital Efficiency: FAT = Revenue/Net Block = 53.23/10.28 = 5.18x
  (screener-Data_Sheet.csv) >3x, but ROCE (FY26, this stage) 18.7% is not
  >20%; next tier FAT>2x AND ROCE>15% both hold → **3**
- M4 Customer Stickiness: zero revenue-decline years (confirmed at C3),
  but receivable days rose 79.1 (FY22) to 170.2 (FY26), far outside ±10
  days stable band, so the top tier (zero decline AND stable receivables)
  is disqualified. No decline year exists to test the "1 decline,
  recovered" tier literally; scored at that tier as the closest fit given
  zero declines is at least as strong as ≤1 decline → **3** (flagged: the
  receivable-days deterioration is the same signal as Load-Bearing Fact 2)
- M5 Scale & Dominance: no peer market-cap/margin ranking dataset provided
  → **0, PEER DATA NEEDED**
- M6 Technology/R&D: no R&D expenditure line disclosed in screener, AR, or
  RHP → **0, N/A (not in provided data)**
- M7 Regulatory/License: no formal government licence or quota regime
  identified in the filings; shipyard vendor "type-approval" is a
  qualification barrier, not a licence in the sense this test intends;
  insufficient evidence to classify as a regulated-licence business →
  **0** (scored for lack of evidence, not confirmed "unregulated")
- M8 Distribution: reach is partially quantified — "customers across 19
  States" plus exports to USA, UAE, Qatar, Sri Lanka (AR p.18) — but no
  prior-year comparison or revenue-per-outlet given → mentioned,
  unquantified trend → **1**
- M9 Brand: no peer gross-margin dataset provided → **0, PEER DATA NEEDED**
- M10 Switching Costs: revenue grew every year (0 decline years) but
  receivable days rose 91.1 days (FY22 to FY26), far above the ≤10-day
  threshold required even at the loosest scoring tier → **0**
- M11 Network Effects: only 5 years of data available, fewer than the
  6 years the two-window test needs; scored conservatively on the overall
  trend as instructed. Revenue CAGR (44.7%, FY22-26) ≥20%; Selling &
  Admin as % of Sales fell from 5.4% (FY22) to 3.9% (FY26) after a FY23
  spike of 9.3% (screener-Data_Sheet.csv) — stable-to-declining → **3**
- M12 Negative WC / Float: WC days were positive and rising in every year
  (150.3 to 334.2, see Block B table), never negative and never in the
  0-15 band → **0**

Block F = 5+0+3+3+0+0+0+1+0+0+3+0 = **15/60**

Moats present (score ≥3): M1, M3, M4, M11 = **4 moats confirmed** →
4-5 → **STRONG**

PEER DATA NEEDED flagged on M2, M5, M9 (3 of 12 tests) — no peer
financial dataset was provided to this stage; peers named in company
memory (KSB, QUESTFLOW, ATAM) but their figures are not in this run's
input set.

## GRAND TOTAL

Core score 68 + Moat score 15 = **Grand total 83**

## DATA CONFIDENCE

5 years of annual data (FY22-FY26) → 5-6 year band → LOWER confidence,
flag "may not have seen full cycle." No downgrade tier applies (that is
reserved for 3-4 years).

## CLASSIFICATION AND OVERRIDES

Raw classification (before deal-breakers): Core 68 (60-79 band) + Moat
STRONG → **GOOD+**.

Deal-breaker check:
1. Block A <8 → max GOOD: Block A = 15, not triggered.
2. Block B <8 → max GOOD: Block B = 0, **TRIGGERED**.
3. Median ROCE <10% → max AVERAGE: median 39.5%, not triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: -1.46, **TRIGGERED**.
5. Pledge >15% → max AVERAGE: 0%, not triggered.
6. ND/EBITDA >3x AND IC <3x → AVOID: 1.49x, not triggered.
7. Revenue declined in majority of years → max AVERAGE: 0 decline years,
   not triggered.
8. PAT negative in any of last 3 years → max AVERAGE: FY24-FY26 all
   positive, not triggered.
9. History <3 years → AVERAGE: 5 years of financial data available (FY22
   FY26), not triggered on this test (note: listed trading history is
   only ~2 years, a separate fact, carried above under E2 and in
   input_gaps, not this deal-breaker).

Two deal-breakers triggered (#2 max GOOD, #4 max AVERAGE). The more
restrictive cap governs.

**Final classification: AVERAGE** (capped from raw GOOD+ by deal-breaker
#4, cumulative CFO/PAT = -1.46, itself the same signal as Block B's 0/20
and Load-Bearing Fact 2).

## STRONGEST / WEAKEST BLOCK

Strongest: Block C, Growth, 20/20 — revenue and PAT both compounded
fast off a small base with zero decline years.

Weakest: Block B, Cash Generation Quality, 0/20 — every sub-metric
scored zero; CFO has been negative every year since FY23 while PAT stayed
positive and grew.

## DECISION LINE

Gate 0 mechanical scorecard: AVERAGE, capped by the cash-conversion
deal-breaker. Fast, real revenue and profit growth (Block C 20/20, 4
quantitative moats, STRONG) sits against a balance sheet that has not
converted that growth into cash for four straight years (Block B 0/20).
No STOP verdict applies at this mechanical stage; the flag propagates to
Halt 1 for the operator.

```yaml
stage: B01-gate0
company: "RAPPID"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
input_gaps:
  - "rating/ folder empty, no credit rating exists"
  - "research/ folder empty"
  - "one earnings call only (NO-CONCALL MODE)"
  - "peer transcripts 8 of 12 available"
  - "screener P&L/BS/CF/Quarters tabs were empty exports; Data_Sheet tab populated and used"
  - "SME half-yearly filer; Q1 FY27 figures exist only as an unaudited business update, not used in this annual scorecard"
  - "no peer margin/mcap dataset provided for M2/M5/M9 moat tests, PEER DATA NEEDED"
  - "no R&D expenditure disclosure in provided documents (M6)"
  - "no shareholding pattern later than Mar-2026 (AR) available for E1/E3 latest-quarter checks"
flags:
  - type: FLAG-GATE0
    reason: "Classification capped at AVERAGE by deal-breaker 4 (cumulative CFO/PAT = -1.46x, FY22-26) despite raw GOOD+ (Core 68, Moat STRONG). Block B scored 0/20 on all four sub-metrics: CFO negative every year FY23-FY26 (-26.56 Cr cumulative) against cumulative PAT +17.40 Cr; FCF positive in only 1 of 5 years; WC days rose from 150.3 to 334.2 (FY22 to FY26), driven mainly by receivable days (79.1 to 170.2) and inventory days (138.3 to 182.9). Block A also carries an ROCE-trend penalty (A4=0) driven by a small-base FY22 ROCE of 85.4% that is not representative of run-rate returns."
data_years: 5
fy_range: "FY22 to FY26"
blocks: {A: 15, B: 0, C: 20, D: 16, E: 17}
core_score: 68
moat_score: 15
grand_total: 83
moats_confirmed: 4
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 -> max GOOD (Block B = 0)"
  - "Cumulative CFO/PAT <0.50 -> max AVERAGE (ratio = -1.46, FY22-26)"
history_downgrade: false
data_notes:
  - "FY22 ROCE (85.4%) is a small-capital-employed-base distortion (Cap Employed only Rs 2.04 Cr, reserves still negative at that date); reported per fixed formula with no adjustment."
  - "FY22 ROE excluded from median: negative average net worth (-Rs 0.25 Cr) makes PAT/NW a non-meaningful negative ratio despite positive PAT; opening NW unavailable for FY22 so closing NW used per rule, as stated."
  - "RHP restated FY24 CFO (-Rs 1.07 Cr, RHP p.217 area) differs from screener-Data_Sheet.csv FY24 CFO (-Rs 2.48 Cr); screener series used across all 5 years for internal consistency, discrepancy not reconciled."
  - "Company memory (step1 brief) cites FY26 inventory days ~258; this stage's prescribed formula (Inventory/Revenue x 365) gives 182.9 for FY26. Basis difference not reconciled; own computed figure used for scoring."
  - "E2 measured over the ~2-year listed history (post-issue Sep-2024 to Mar-2026), not a full 3 years, since pre-IPO holding is a dilution event, not a valid same-basis comparator; stated explicitly, not estimated."
  - "No loss-to-profit swing: PAT positive in all 5 years (FY22 smallest at Rs 0.29 Cr)."
  - "PEER DATA NEEDED: M2 (cost advantage), M5 (scale and dominance), M9 (brand) all require peer financial data not present in this run's input set."
block_b_trend: "deteriorating - CFO swung from +Rs1.14 Cr (FY22) to -Rs10.83 Cr (FY26); cumulative FY23-26 CFO -Rs26.56 Cr against cumulative PAT +Rs17.11 Cr over the same 4 years"
analyst_note: "The classification hinges entirely on Block B. Growth (20/20) and moat count (4, STRONG) would put this at GOOD+ on a Core/Moat basis alone. Block B's zero score is not one weak metric outvoted by three strong ones; all four cash metrics failed together, and the same underlying driver (receivable and inventory days both roughly doubling FY22 to FY26) shows up again in moat test M4 and M10, where it blocks credit that revenue growth would otherwise earn. This is one root cause counted honestly across multiple tests, not four independent problems. The FY22 ROCE outlier (85.4%) inflates the Block A median; A2 (minimum-year ROCE, 18.7%) and A4 (trend, -66.7pp) better reflect the current run rate. Downstream stages should treat the cash-conversion pattern as the single most load-bearing fact of this run, consistent with company memory's own framing."
```
