# STAGE 1: GATE 0 SCORECARD — Rappid Valves (India) Ltd (RAPPID)
Run date: 2026-09-19 | Model: claude-sonnet-5 | CORRECTION RUN (round 2)

Data available: 5 years (FY22 to FY26). Scoring adapted to 5-year history.
Source hierarchy used: screener-Data_Sheet.csv for the continuous 5-year
P&L/BS/CF series (INR Cr); FY26 Annual Report (INR Lakhs, converted to Cr)
for line items screener does not carry (contingent liabilities, trade
payables, capex, promoter holding, disclosed ratios); RHP Sep-2024 (INR
Lakhs, restated, converted to Cr) for the pre-listing years FY22-FY24 where
the AR does not go back that far (current liabilities, capex, pre-IPO
promoter holding). Every number below is followed by its source.

This is the round-2 corrected report. Verifier C (12c) audited round 1 and
raised six B01 findings: G3, G22, G6, G30, G34, G37. All six are addressed
below; see the CORRECTIONS (round 2) section for disposition of each. Two
(G3, G22) change block scores. Four (G6, G30, G34, G37) correct methodology,
stated reasoning, or YAML completeness without changing a score.

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

## CORRECTIONS (round 2)

Each finding re-checked against the cited rule in prompts/01-gate-0-pipeline.md
and against the source (AR p.69 Note 36; RHP p.95; screener-Data_Sheet.csv).

**G3 (MAJOR) — ROCE source precedence.** Rule: "If the data source provides
its own ROCE ... use the source's figure and anchor it; compute only when
absent." Re-read AR p.69, Note 36 ("Significant Changes in key financial
ratios ... Return on capital employed, % = (M+O) ÷ average of K"): discloses
FY26 = 14%, FY25 = 17% (AR p.69, Note 36, row 10). This is the source's own
ROCE, audited and statutory, for the two years it covers. Round 1 used a
self-computed EBIT ÷ (TA − CL) figure for all five years (FY26 18.7%, FY25
20.2%) and only cross-checked RHP's disclosed ROCE (a different denominator,
Net worth + Total Debt) without reconciling AR's. **DISPOSITION: APPLIED.**
FY25 and FY26 ROCE now use the AR Note 36 disclosed figures (17%, 14%). AR
does not go back to FY22-FY24; no RHP KPI-note ROCE is substituted there
because RHP's own disclosed ROCE uses a different denominator (Net worth +
Total Debt, RHP p.150-151/237), not (Total Assets − Current Liabilities); the
two bases are not interchangeable, so FY22-FY24 stay on the fixed computed
formula, stated as "computed" per the rule. This mixes formula bases within
one 5-year series (computed for 3 years, source-disclosed for 2); flagged as
a data note, not smoothed away, because Rule 2 forbids qualitative
adjustment.

**G22 (MAJOR) — E2 promoter holding change over 3 years.** Rule: "Promoter
holding change over 3 years: increased ≥1% = 5 | ±1% = 3 | decreased 1-3% =
1 | decreased >3% = 0." No exception is written for IPO dilution versus
promoter selling (Rule 2: no qualitative judgment, only numbers and scoring
rules). Re-read RHP p.95 (Capital Structure, Pre-Issue and Post-Issue
Shareholding of Promoter and Promoter Group table): Total (A+B) Pre-Issue
69.46%, Post-Issue 51.13% (RHP p.95, confirmed at the page-95 marker in the
source text; the same table also appears without a page marker earlier in
the Objects-of-the-Issue summary). Round 1 substituted a post-listing-only
window (Sep-2024 51.13% to Mar-2026 51.58%, AR p.60) on the reasoning that
pre-IPO dilution is not a valid comparator, scoring +0.45pp → 3. **DISPOSITION:
APPLIED.** The rule gives no basis to discard the pre-issue reading; the only
change actually available across a window approximating 3 years (and the
only one the round-1 report itself sourced) is 69.46% (RHP p.95, pre-issue)
to 51.58% (AR p.60, Mar-2026) = -17.88pp → decreased >3% → **0** (was 3).
Noted, not judged: this fall is IPO-mechanical dilution, not promoter
selling; the number stands per Rule 2, and the distinction is carried as a
data note for downstream reading, not as a score override.

**G6 (MINOR) — A3 ROE, FY22 exclusion.** Rule: "if opening net worth
unavailable for the earliest year, use closing and state so." It instructs
a substitution (closing for opening), not an exclusion. Round 1 computed
FY22 ROE (0.29/-0.25 = -116%) and then dropped it from the median because a
negative-net-worth denominator is not a meaningful percentage. **DISPOSITION:
APPLIED (methodology only, score unchanged).** FY22 is now included per the
literal rule: sorted ROE [-116%, 13.4%, 22.9%, 32.1%, 78.6%], median = 22.9%
(was 27.5% with FY22 excluded). Still ≥20% → **5** (unchanged). The
distortion is kept visible as a data note rather than papered over by
exclusion.

**G30 (MINOR) — M10 stated reasoning.** Rule tiers: "revenue grew every year
AND receivable days rose ≤10 days = 5 | growth all but 1 year AND stable = 3
| overall growth, 2+ decline years = 1 | else 0." Round 1's write-up said the
score of 0 followed because "the ≤10-day threshold [is] required even at the
loosest scoring tier" — that is wrong; the loosest tier (score 1) carries no
receivable-day test at all, only a decline-year test ("2+ decline years"),
which this business does not have (0 decline years, so it does not fit that
tier's growth description either). **DISPOSITION: APPLIED (reasoning
corrected, score unchanged).** Correct reasoning: revenue grew every year
(0 decline years) but receivable days rose from 79.1 to 170.2 (+91.1 days,
FY22 to FY26), so the top tier fails on the receivable-day test; the two
lower tiers each specify a decline-year count (1, or 2+) that this
zero-decline record does not match either, so no tier condition is
literally satisfied → **0** stands, on corrected grounds.

**G34 (MINOR) — data-confidence flag not carried to YAML.** Rule: "5-6 yrs
lower, flag 'may not have seen full cycle'." Round 1 stated this in the
report prose only; it was missing from the B01 YAML `flags`/`data_notes`
fields that downstream stages actually read. **DISPOSITION: APPLIED.** Added
to `data_notes` in the YAML block below.

**G37 (MINOR) — FLAG-GATE0 reason window mismatch.** The round-1 flag
reason paired FY23-26 cumulative CFO (-26.56 Cr, a 4-year figure) against
FY22-26 cumulative PAT (+17.40 Cr, a 5-year figure) — a window mismatch. The
`block_b_trend` field already used the correctly matched FY23-26 PAT
(+17.11 Cr, = 0.46+4.13+6.04+6.48, screener-Data_Sheet.csv). **DISPOSITION:
APPLIED.** The FLAG-GATE0 reason below now states both matched windows
explicitly: FY22-26 cumulative CFO -25.42 Cr vs cumulative PAT +17.40 Cr
(the deal-breaker's own 5-year basis), and separately FY23-26 cumulative CFO
-26.56 Cr vs cumulative PAT +17.11 Cr (the 4-year window during which CFO
was continuously negative).

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score 13 (was 15)

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed where
no source-disclosed ROCE exists. EBIT = PBT + Finance Costs − Other Income
(basis confirmed as the standard definition by RHP's own KPI note, RHP
p.151, "(6) Return on Capital Employed... Profit before tax + Finance Costs
– Other Income (EBIT)"). Capital Employed = Total Assets (screener-Data_Sheet.csv)
− Current Liabilities (RHP p.215 restated BS for FY22-24; AR p.55 audited BS
for FY25-26). Per G3 (round-2 correction), FY25 and FY26 use the AR's own
disclosed Note 36 ROCE instead of this computed figure; FY22-FY24 have no
AR/screener-disclosed ROCE and stay on the computed formula.

| Year | PBT | Interest | Other Inc | EBIT | Total Assets | Current Liab | Cap Employed | ROCE (computed) | ROCE used for scoring |
|---|---|---|---|---|---|---|---|---|---|
| FY22 | 0.29 | 1.46 | 0.01 | 1.74 | 12.17 | 10.13 (RHP p.215) | 2.04 | 85.4% | 85.4% (computed, no source disclosure) |
| FY23 | 0.63 | 1.44 | 0.04 | 2.03 | 16.57 | 11.44 (RHP p.215) | 5.13 | 39.5% | 39.5% (computed, no source disclosure) |
| FY24 | 5.53 | 1.40 | 0.09 | 6.84 | 29.96 | 15.62 (RHP p.215) | 14.34 | 47.7% | 47.7% (computed, no source disclosure) |
| FY25 | 8.24 | 1.12 | 0.21 | 9.15 | 60.26 | 14.89 (AR p.55) | 45.37 | 20.2% | **17%** (AR p.69, Note 36, disclosed) |
| FY26 | 8.66 | 1.33 | 0.32 | 9.67 | 75.32 | 23.52 (AR p.55) | 51.80 | 18.7% | **14%** (AR p.69, Note 36, disclosed) |

(PBT, Interest, Other Income, Total Assets: screener-Data_Sheet.csv, all
figures Rs Cr. AR Note 36 formula: "Return on capital employed, % = (M+O) ÷
average of K", AR p.69.)

DATA NOTE: FY22 ROCE of 85.4% is a small-base distortion — capital
employed was only Rs 2.04 Cr against reserves that were still negative
(-Rs 0.8 Cr, screener-Data_Sheet.csv) at that balance-sheet date. It pulls
the median upward relative to the FY23-FY26 run rate. Reported per the
fixed formula with no adjustment (Rule 2, no qualitative judgment).

DATA NOTE (round 2): FY25/FY26 now use AR-disclosed ROCE (Note 36) at 17%
and 14%, materially below this stage's own computed 20.2%/18.7% for the same
years. The AR's formula denominator ("average of K") is not shown in the
extracted text; treated as authoritative per the source-precedence rule
regardless of the basis difference, consistent with how D2-D4 already use
AR-disclosed ratios in this same scorecard. This produces a 5-year ROCE
series that mixes two formula bases (computed FY22-24, AR-disclosed FY25-26);
flagged, not smoothed.

Cross-check: RHP's own disclosed ROCE (different denominator, Net
worth + Total Debt, RHP p.150-151/p.237) reads FY24 29.88%, FY23 15.85%,
FY22 18.38% — directionally consistent (rising then normalising) but not
numerically comparable to this stage's fixed formula, and not substituted
in for FY22-24 for that reason.

- A1 Median ROCE (scoring basis: 14, 17, 39.5, 47.7, 85.4) = 39.5% → ≥25% → **5** (unchanged)
- A2 Minimum single-year ROCE = **14%** (FY26, AR-disclosed) → 12-14.9% → **3** (was 5)
- A3 Median ROE = 22.9% (see below, round-2 corrected) → ≥20% → **5** (unchanged)
- A4 ROCE trend, latest (14%, AR-disclosed) vs earliest (85.4%, computed) = decline 71.4pp → >5pp decline → **0** (unchanged)

ROE = PAT ÷ average Net Worth. Net Worth (Equity Capital + Reserves,
screener-Data_Sheet.csv, Rs Cr): FY22 -0.25, FY23 3.12, FY24 7.39, FY25
45.25, FY26 51.71.

| Year | PAT | Avg NW | ROE |
|---|---|---|---|
| FY22 | 0.29 | -0.25 (opening unavailable, closing used per rule) | -116.0% |
| FY23 | 0.46 | 1.44 | 32.1% |
| FY24 | 4.13 | 5.26 | 78.6% |
| FY25 | 6.04 | 26.32 | 22.9% |
| FY26 | 6.48 | 48.48 | 13.4% |

Round-2 correction (G6): the rule directs "use closing and state so" for
FY22, not exclusion. FY22 ROE is now included in the median. Sorted:
[-116.0, 13.4, 22.9, 32.1, 78.6]. Median = 22.9% (was 27.5% under round 1's
FY22-excluded calculation). Still ≥20% → score unchanged at 5. The negative
figure is a small-base/negative-net-worth artefact, kept visible rather than
dropped, per Rule 2. Cross-check: AR's own disclosed Return on Net Worth
(AR p.27/p.69, Note 36 basis) reads FY26 13.4% (exact match to this stage's
figure) and FY25 21.0% (this stage: 22.9%, small basis difference, not
reconciled) / AR p.69 Note 36 shows FY26 13%, FY25 13% on its own
"Return on equity ratio" row (P ÷ average of H), a third close-but-not-
identical reading; not reconciled from the provided documents.

Block A = 5+3+5+0 = **13/20** (was 15/20)

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score 0

Unchanged from round 1; no B-block finding was raised.

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

Block B = 0+0+0+0 = **0/20** — the weakest block and the principal
deal-breaker driver, unchanged.

## BLOCK C: GROWTH (Max 20) — Score 20

Unchanged from round 1; no C-block finding was raised.

Revenue (screener-Data_Sheet.csv, Rs Cr): FY22 12.14, FY23 16.40, FY24
36.51, FY25 52.13, FY26 53.23. PAT: FY22 0.29, FY23 0.46, FY24 4.13, FY25
6.04, FY26 6.48.

- C1 Revenue CAGR FY22-FY26 (4yr) = (53.23/12.14)^(1/4)-1 = 44.7% → ≥20% → **5**
- C2 PAT CAGR FY22-FY26 (4yr) = (6.48/0.29)^(1/4)-1 = 117.4% (both endpoints
  positive, no N/M) → ≥20% → **5**
- C3 Positive YoY revenue years: FY23 +35.1%, FY24 +122.6%, FY25 +42.8%,
  FY26 +2.1% — all 4 of 4 periods positive = 100% → **5**
- C4 PAT CAGR − Revenue CAGR = 117.4% − 44.7% = +72.7pp → ≥+3pp → **5**

Block C = 5+5+5+5 = **20/20** — the strongest block, unchanged.

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score 16

Unchanged from round 1; no D-block finding was raised.

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

Block D = 3+4+4+5 = **16/20**, unchanged.

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score 14 (was 17)

- E1 Promoter holding, latest available (Mar-2026) = 51.58% (AR p.60,
  Note 3.7: Gaurav Dalal 47.97% + Vijay Dalal 3.61%). No shareholding
  pattern later than Mar-2026 in the provided documents. → 50-59.9% → **4**
  (Company memory cites 51.69% from screener/deck; AR Note 3.7, the
  audited primary source, used instead.) Unchanged.
- E2 Promoter holding change over 3 years, round-2 corrected (G22): rule
  carries no exception for IPO dilution (Rule 2, no qualitative judgment).
  Pre-Issue 69.46% (RHP p.95, Capital Structure, Total A+B) to Mar-2026
  51.58% (AR p.60) = -17.88pp → decreased >3% → **0** (was 3). Data note:
  this decline is IPO-mechanical dilution (new shares issued at listing),
  not promoter selling; the AR's own Note 3.7 shows 0.00pp change within
  the post-listing window (Sep-2024 to Mar-2026) alone. The number is
  scored as filed; the distinction is carried as context, not as a score
  adjustment, per Rule 2.
- E3 Promoter pledge, latest = 0%. RHP p.94: "our Promoter have not
  pledged any of the Equity Shares that they hold." No later pledge
  disclosure found in the provided documents to contradict this; AR
  Note 3.7 shows 0.00% holding change FY25-FY26 with no pledge column
  flagged. → 0% → **5**. Unchanged.
- E4 Contingent Liabilities ÷ Net Worth = Rs 14.6 Lakh ÷ Rs 5,171.4 Lakh
  (AR p.68 Note, Performance Bank Guarantee, IDBI Bank; AR p.55,
  Shareholders' Funds) = 0.28% → <5% → **5**. Unchanged.

Block E = 4+0+5+5 = **14/20** (was 17/20)

Core score (A+B+C+D+E) = 13+0+20+16+14 = **63/100** (was 68/100)

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score 13 (was 15)

- M1 Pricing Power: EBITDA margin FY23 13.0% to FY26 19.4% (AR p.20,
  4-year snapshot), +6.3pp expansion, ≥2pp; revenue CAGR FY23-FY26
  (3yr) = 48.1%, ≥10% → **5**. Unchanged.
- M2 Cost Advantage vs peer median EBITDA margin: no peer EBITDA-margin
  dataset provided to this stage → **0, PEER DATA NEEDED**. Unchanged.
- M3 Capital Efficiency, round-2 corrected (G3 flows through): FAT =
  Revenue/Net Block = 53.23/10.28 = 5.18x (screener-Data_Sheet.csv) >3x,
  but ROCE (FY26, now AR Note 36 disclosed = **14%**, not this stage's own
  computed 18.7%) is not >20% and not >15%; the FAT>1x AND ROCE>12% tier
  holds (14%>12%) → **1** (was 3, when the computed 18.7% put it in the
  FAT>2x AND ROCE>15% tier).
- M4 Customer Stickiness: zero revenue-decline years (confirmed at C3),
  but receivable days rose 79.1 (FY22) to 170.2 (FY26), far outside ±10
  days stable band, so the top tier (zero decline AND stable receivables)
  is disqualified. No decline year exists to test the "1 decline,
  recovered" tier literally; scored at that tier as the closest fit given
  zero declines is at least as strong as ≤1 decline → **3** (flagged: the
  receivable-days deterioration is the same signal as Load-Bearing Fact 2).
  Unchanged.
- M5 Scale & Dominance: no peer market-cap/margin ranking dataset provided
  → **0, PEER DATA NEEDED**. Unchanged.
- M6 Technology/R&D: no R&D expenditure line disclosed in screener, AR, or
  RHP → **0, N/A (not in provided data)**. Unchanged.
- M7 Regulatory/License: no formal government licence or quota regime
  identified in the filings; shipyard vendor "type-approval" is a
  qualification barrier, not a licence in the sense this test intends;
  insufficient evidence to classify as a regulated-licence business →
  **0** (scored for lack of evidence, not confirmed "unregulated").
  Unchanged.
- M8 Distribution: reach is partially quantified — "customers across 19
  States" plus exports to USA, UAE, Qatar, Sri Lanka (AR p.18) — but no
  prior-year comparison or revenue-per-outlet given → mentioned,
  unquantified trend → **1**. Unchanged.
- M9 Brand: no peer gross-margin dataset provided → **0, PEER DATA NEEDED**.
  Unchanged.
- M10 Switching Costs, round-2 reasoning corrected (G30, score unchanged):
  revenue grew every year (0 decline years) but receivable days rose 91.1
  days (FY22 to FY26). The top tier (5) requires receivable days to rise
  ≤10 days — fails. The two lower tiers (3, 1) each specify a decline-year
  count (a single decline year, or "2+" decline years respectively) that
  this zero-decline record does not literally match either. Round 1's
  stated reason ("≤10-day threshold required even at the loosest scoring
  tier") was wrong — the loosest tier (1) has no receivable-day test at
  all, only the decline-year test, which is also not met → **0** stands.
- M11 Network Effects: only 5 years of data available, fewer than the
  6 years the two-window test needs; scored conservatively on the overall
  trend as instructed. Revenue CAGR (44.7%, FY22-26) ≥20%; Selling &
  Admin as % of Sales fell from 5.4% (FY22) to 3.9% (FY26) after a FY23
  spike of 9.3% (screener-Data_Sheet.csv) — stable-to-declining → **3**.
  Unchanged.
- M12 Negative WC / Float: WC days were positive and rising in every year
  (150.3 to 334.2, see Block B table), never negative and never in the
  0-15 band → **0**. Unchanged.

Block F = 5+0+1+3+0+0+0+1+0+0+3+0 = **13/60** (was 15/60)

Moats present (score ≥3): M1, M4, M11 = **3 moats confirmed** (was 4;
M3 dropped from 3 to 1 and no longer counts) → 2-3 → **MODERATE**
(was STRONG).

PEER DATA NEEDED flagged on M2, M5, M9 (3 of 12 tests) — no peer
financial dataset was provided to this stage; peers named in company
memory (KSB, QUESTFLOW, ATAM) but their figures are not in this run's
input set.

## GRAND TOTAL

Core score 63 + Moat score 13 = **Grand total 76** (was 83)

## DATA CONFIDENCE

5 years of annual data (FY22-FY26) → 5-6 year band → LOWER confidence,
flag "may not have seen full cycle" (per G34, round-2, now also carried in
the YAML `data_notes` field below, not only in this report prose). No
downgrade tier applies (that is reserved for 3-4 years).

## CLASSIFICATION AND OVERRIDES

Raw classification (before deal-breakers): Core 63 (60-79 band) + Moat
MODERATE → **GOOD** (was GOOD+ at Core 68 + STRONG).

Deal-breaker check:
1. Block A <8 → max GOOD: Block A = 13, not triggered.
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

**Final classification: AVERAGE** (unchanged from round 1; capped from
raw GOOD by deal-breaker #4, cumulative CFO/PAT = -1.46, itself the same
signal as Block B's 0/20 and Load-Bearing Fact 2). The round-2 corrections
lower the raw pre-deal-breaker classification from GOOD+ to GOOD, but the
Block B deal-breaker caps the outcome at AVERAGE either way, so the
decision does not move.

## STRONGEST / WEAKEST BLOCK

Strongest: Block C, Growth, 20/20 — revenue and PAT both compounded
fast off a small base with zero decline years. Unchanged.

Weakest: Block B, Cash Generation Quality, 0/20 — every sub-metric
scored zero; CFO has been negative every year since FY23 while PAT stayed
positive and grew. Unchanged.

## DECISION LINE

Gate 0 mechanical scorecard: AVERAGE, capped by the cash-conversion
deal-breaker. Fast, real revenue and profit growth (Block C 20/20) sits
against a balance sheet that has not converted that growth into cash for
four straight years (Block B 0/20), and against a moat count that the
round-2 source-ROCE correction pulls from 4 (STRONG) to 3 (MODERATE). The
classification outcome (AVERAGE) is unchanged by every round-2 correction;
the deal-breaker was already, and remains, the binding constraint. No STOP
verdict applies at this mechanical stage; the flag propagates to Halt 1 for
the operator.

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
    reason: "Classification capped at AVERAGE by deal-breaker 4 (cumulative CFO/PAT = -1.46x, FY22-26: cumulative CFO -25.42 Cr vs cumulative PAT +17.40 Cr; on the FY23-26 window during which CFO was continuously negative, cumulative CFO -26.56 Cr vs cumulative PAT +17.11 Cr) despite raw GOOD (round-2 corrected; Core 63, Moat MODERATE). Block B scored 0/20 on all four sub-metrics: CFO negative every year FY23-FY26 against positive, growing PAT; FCF positive in only 1 of 5 years; WC days rose from 150.3 to 334.2 (FY22 to FY26), driven mainly by receivable days (79.1 to 170.2) and inventory days (138.3 to 182.9). Round-2 correction (verifier 12c, G3): FY25/FY26 ROCE now use the AR's own Note 36 disclosed figures (17%, 14%) instead of this stage's higher computed figures (20.2%, 18.7%), which drops A2 from 5 to 3 and M3 from 3 to 1, taking the moat count from 4 (STRONG) to 3 (MODERATE). Round-2 correction (G22): E2 promoter-holding-change now uses the pre-issue-to-latest window (69.46% to 51.58%, -17.88pp) per the rule's own literal 3-year-change test, dropping E2 from 3 to 0. Neither correction changes the final classification; deal-breaker 4 already capped it at AVERAGE."
data_years: 5
fy_range: "FY22 to FY26"
blocks: {A: 13, B: 0, C: 20, D: 16, E: 14}
core_score: 63
moat_score: 13
grand_total: 76
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 -> max GOOD (Block B = 0)"
  - "Cumulative CFO/PAT <0.50 -> max AVERAGE (ratio = -1.46, FY22-26)"
history_downgrade: false
data_notes:
  - "5-6 years of data (FY22-FY26): LOWER confidence band, flag 'may not have seen full cycle' (round 2 addition, G34: this was stated in the report prose in round 1 but omitted from this YAML field)."
  - "FY22 ROCE (85.4%) is a small-capital-employed-base distortion (Cap Employed only Rs 2.04 Cr, reserves still negative at that date); reported per fixed formula with no adjustment."
  - "Round 2 (G3): FY25/FY26 ROCE scoring basis changed from this stage's computed EBIT/(TA-CL) figures (20.2%, 18.7%) to the AR's own Note 36 disclosed ROCE (17%, 14%, AR p.69), per the rule's source-precedence instruction. FY22-FY24 stay on the computed formula; no AR/screener ROCE disclosure exists for those years, and RHP's disclosed ROCE uses a different denominator (Net worth + Total Debt) not treated as substitutable. This produces a 5-year ROCE series on two different bases; flagged, not smoothed."
  - "Round 2 (G6): A3 median ROE now includes FY22 (closing-NW basis, -116%, rule-directed substitution not exclusion), giving median 22.9% (was 27.5% with FY22 excluded in round 1). Score unchanged at 5."
  - "Round 2 (G22): E2 promoter-holding-change now measured pre-issue (69.46%, RHP p.95) to latest (51.58%, AR p.60) = -17.88pp, per the rule's literal 3-year-change test with no dilution exception (Rule 2). Score changed from 3 to 0. The post-listing-only window (Sep-2024 to Mar-2026, +0.45pp) is kept as context: it isolates post-IPO promoter behaviour from the one-time IPO dilution event, but is not the scoring basis."
  - "RHP restated FY24 CFO (-Rs 1.07 Cr, RHP p.217 area) differs from screener-Data_Sheet.csv FY24 CFO (-Rs 2.48 Cr); screener series used across all 5 years for internal consistency, discrepancy not reconciled."
  - "Company memory (step1 brief) cites FY26 inventory days ~258; this stage's prescribed formula (Inventory/Revenue x 365) gives 182.9 for FY26. Basis difference not reconciled; own computed figure used for scoring."
  - "No loss-to-profit swing: PAT positive in all 5 years (FY22 smallest at Rs 0.29 Cr)."
  - "PEER DATA NEEDED: M2 (cost advantage), M5 (scale and dominance), M9 (brand) all require peer financial data not present in this run's input set."
block_b_trend: "deteriorating - CFO swung from +Rs1.14 Cr (FY22) to -Rs10.83 Cr (FY26); cumulative FY23-26 CFO -Rs26.56 Cr against cumulative PAT +Rs17.11 Cr over the same 4 years"
analyst_note: "Round-2 correction lowers the classification's raw pre-deal-breaker footing (GOOD+ -> GOOD, moat STRONG -> MODERATE) but does not move the final AVERAGE call: deal-breaker 4 (cumulative CFO/PAT -1.46x) was already the binding constraint and stays binding. The two MAJOR fixes both point the same direction, toward a more conservative read of return quality and promoter alignment: the AR's own Note 36 ROCE (14-17%) is lower than this stage's computed figure (18.7-20.2%), and the only rule-compliant 3-year promoter-holding window is IPO-dilution-inclusive and shows a large drop, not the small post-listing rise round 1 reported. Growth (Block C, 20/20) is untouched by any correction and remains the strongest signal in the scorecard. Downstream stages should treat the cash-conversion pattern (Block B, 0/20) as the single most load-bearing fact of this run, and should now read the moat count as 3 (MODERATE), not 4 (STRONG), when B07's 6C table cites this block."
```
