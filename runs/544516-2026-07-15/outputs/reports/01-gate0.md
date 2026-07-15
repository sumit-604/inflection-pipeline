# STAGE 1 — GATE 0 SCORECARD
## Airfloa Rail Technology Ltd (BSE 544516, SME platform, symbol AIRFLOA)
Run date: 2026-07-15 | Model: claude-sonnet-5 | Mode: pipeline

Data available: 2 years (FY25 to FY26). Scoring adapted to 2-year history.

---

## SOURCE MAP AND A CRITICAL CORRECTION TO THE INPUT GAPS NOTE

The file `inputs/annual-report/1758608206692.pdf` supplied to this stage as "annual report"
is in fact the **IPO Prospectus dated 16 September 2025** (100% Book Built Offer, BSE SME
platform), not a post-listing statutory Annual Report. It was used extensively below for
promoter shareholding, capital structure, the FY25 restated financial statements, and
contingent liabilities. This corrects the task brief's assumption that "prospectus ABSENT" —
the prospectus is present, just filed under the annual-report path. A genuine FY26 Annual
Report (Directors' Report, MGT-7 full shareholding pattern, FY26 contingent liabilities note)
was NOT supplied and remains absent. See `input_gaps` in the YAML block.

Financial statements used:
- FY25 and FY26 **standalone** audited figures: `inputs/results/c6f8b4e6-...pdf` (Board
  outcome 30-May-2026, audited standalone + consolidated results for year ended 31-Mar-2026,
  with FY25 comparatives), pages 1, 6-9 of extraction ("results FY26 p.6" P&L, "p.7" Balance
  Sheet, "p.8" Cash Flow).
- H1 FY26 (interim, Sept-2025) standalone/consolidated: `inputs/results/f51ba69b-...pdf`
  ("results H1 FY26 p.5-7") — used for context only, not scored (interim, not full year).
- FY25 restated consolidated financials, contingent liabilities, promoter shareholding,
  capital structure: prospectus, `inputs/annual-report/1758608206692.pdf` ("prospectus
  p.69-79" capital structure/shareholding, "prospectus CFS5-7" restated B/S, P&L, cash flow,
  "prospectus CFS35" contingent liabilities Annexure XXXIX).
- Screener export `inputs/screening/screener-Data_Sheet.csv` ("screener-data") — cross-checked
  against the above; matches to the rupee on all overlapping line items (see reconciliation
  note below). The other screener CSVs (Profit_Loss, Balance_Sheet, Cash_Flow, Quarters) are
  EMPTY (headers only, no populated cells) — not usable.
- FRONTSP-*.csv and TEXRAIL-*.csv (peer companies) were NOT used per explicit instruction.

**Anchor reconciliation note:** the Data_Sheet FY25 net profit (₹25.55 Cr) matches the
prospectus's **restated consolidated** FY25 PAT (₹2,554.76 lakh = ₹25.5476 Cr) almost exactly,
not the FY26-results-filing's **standalone** FY25 comparative PAT (₹2,578.27 lakh = ₹25.78 Cr).
This stage uses the standalone FY25 vs FY26 figures throughout for like-for-like comparability
(both drawn from the same FY26 results filing's comparative columns); the ~0.9% gap to the
restated consolidated FY25 number is disclosed, not hidden, and is immaterial to every score
band below.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 15/20

Formulas: ROCE = EBIT ÷ (Total Assets − Current Liabilities); EBIT = PBT + Finance Costs.
Screener.in does not populate a ROCE/ROE figure for Airfloa (Balance_Sheet.csv and
Data_Sheet.csv both have the ROCE/ROE rows present but empty) — both computed here, marked
"computed."

| Year | PBT | Finance Cost | EBIT | Total Assets | Current Liab. | Capital Employed | ROCE |
|---|---|---|---|---|---|---|---|
| FY25 | ₹3,499.21L | ₹1,107.03L | ₹4,606.24L | ₹25,575.84L | ₹14,420.35L | ₹11,155.49L | **41.30%** |
| FY26 | ₹5,267.69L | ₹857.94L | ₹6,125.63L | ₹40,100.25L | ₹15,806.27L | ₹24,293.98L | **25.22%** |

(all figures: results FY26 p.6-7, standalone, computed)

- **A1 Median ROCE** (n=2, median = average) = (41.30+25.22)/2 = **33.26%** → ≥25% band → **Score 5**
- **A2 Minimum single-year ROCE** = min(41.30, 25.22) = **25.22%** → ≥15% band → **Score 5**
- **A3 Median ROE**: Net Worth FY25 closing = ₹10,875.38L (Share Cap ₹1,746.30L + Reserves
  ₹9,129.08L); FY26 closing = ₹23,677.80L (₹2,397.00L + ₹21,280.80L). Opening net worth for
  FY25 unavailable (no FY24 balance sheet supplied) — **closing NW used for FY25, stated per
  formula rule**. ROE FY25 = 2,578.27/10,875.38 = **23.71%**. ROE FY26 uses average NW
  (10,875.38+23,677.80)/2=17,276.59: 3,915.22/17,276.59 = **22.66%**. Median (avg of 2) =
  **23.19%** → ≥20% band → **Score 5** (results FY26 p.6-7, computed)
- **A4 ROCE trend, latest vs earliest**: 25.22% (FY26) vs 41.30% (FY25) = **−16.08pp decline**
  → >5pp decline band → **Score 0**. Driver: equity capital base near-doubled (₹174.63L →
  ₹239.70L share capital; net worth ₹108.75 Cr → ₹236.78 Cr) from the September 2025 IPO
  (fresh issue ₹91.10 Cr) diluting the capital-employed denominator faster than EBIT grew.
  This is a mechanical consequence of capital raised for growth, not an operating decline —
  noted here, scored per the fixed rule regardless.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20 — WEAKEST BLOCK

| Year | CFO (standalone) | Capex (PPE+intangibles) | FCF |
|---|---|---|---|
| FY25 | ₹(286.99)L | ₹(567.32)L | ₹(854.31)L |
| FY26 | ₹(5,745.24)L | ₹(1,715.42)L | ₹(7,460.66)L |

(results FY26 p.8, standalone cash flow, computed)

- **B1 Cumulative CFO ÷ Cumulative PAT** = (−286.99 + −5,745.24) ÷ (2,578.27 + 3,915.22) =
  −6,032.23 ÷ 6,493.49 = **−0.93x** → negative → **Score 0**
- **B2 FCF-positive years** = 0 of 2 years (0%) → <50% → **Score 0**
- **B3 Cumulative FCF ÷ Cumulative PAT** = (−854.31 + −7,460.66) ÷ 6,493.49 = −8,314.97 ÷
  6,493.49 = **−1.28x** → negative → **Score 0**
- **B4 Change in WC Days, latest vs earliest**: Receivable Days on revenue basis (formula
  fixed); Inventory and Payable Days on **COGS basis** (Cost of Material Consumed), used
  because COGS is explicitly disclosed, per the formula's basis rule — stated here.
  - FY25: Receivable Days = 12,760.05/19,238.70×365 = 242.11d; Inventory Days =
    6,243.89/13,343.47×365 = 170.83d; Payable Days = 6,392.70/13,343.47×365 = 174.87d.
    WC Days = 242.11+170.83−174.87 = **238.07 days**
  - FY26: Receivable Days = 21,401.59/31,959.76×365 = 244.40d; Inventory Days =
    7,240.00/20,362.20×365 = 129.75d; Payable Days = 6,091.53/20,362.20×365 = 109.16d.
    WC Days = 244.40+129.75−109.16 = **264.99 days**
  - Change = +26.92 days (increase) → >15 days increase → **Score 0**

**block_b_trend: deteriorating** — every one of the four cash sub-metrics scored zero.
Cumulative CFO of −₹60.32 Cr against cumulative PAT of +₹64.93 Cr over the same two years is
the single number that shows it. Both years' free cash flow is negative and getting more
negative in absolute terms as revenue scales (FCF −₹8.54 Cr FY25 → −₹74.61 Cr FY26). Working
capital (receivables specifically — up ₹86.42 Cr YoY vs revenue up only ₹127.21 Cr) is
consuming cash faster than profit is generating it. This is the block that should anchor any
downstream FLAG-CASH.

---

## BLOCK C: GROWTH (Max 20) — Score: 15/20

Only one YoY comparison is available (FY25→FY26); the CAGR formula with n=1 year reduces to
simple one-year growth, not a multi-year compounded trend — **stated as a limited-history
caveat, not hidden**.

| Metric | FY25 | FY26 | Growth |
|---|---|---|---|
| Revenue | ₹19,238.70L | ₹31,959.76L | **+66.12%** |
| PAT | ₹2,578.27L | ₹3,915.22L | **+51.85%** |

(results FY26 p.6, standalone, computed; formula reduces to 1-yr growth given n=1)

- **C1 Revenue CAGR** = 66.12% → ≥20% band → **Score 5**
- **C2 PAT CAGR** = 51.85% → ≥20% band → **Score 5**
- **C3 Positive YoY revenue years** = 1 of 1 available comparison positive (100%) → **Score 5**
- **C4 PAT CAGR minus Revenue CAGR** = 51.85 − 66.12 = **−14.27pp** → <−8pp band → **Score 0**
  (PAT is growing fast in absolute terms but growing slower than revenue — margin dilution,
  consistent with the EBITDA margin compression noted under Block F, M1.)

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 17/20 — STRONGEST BLOCK

All figures latest year (FY26), standalone (results FY26 p.7).

- **D1 Net Debt ÷ EBITDA**: Total Borrowings = LT ₹411.85L + ST ₹6,419.13L = ₹6,830.98L
  (₹68.31 Cr — matches screener-data Borrowings 68.31 exactly). Cash & Bank = ₹1,307.55L.
  Net Debt = ₹5,523.43L. EBITDA = EBIT ₹6,125.63L + Depreciation ₹346.94L = ₹6,472.57L.
  ND/EBITDA = **0.85x** → 0-1.0x band → **Score 4**
- **D2 Interest Coverage** = EBIT ÷ Interest = 6,125.63 ÷ 857.94 = **7.14x** → 5-9.9x band →
  **Score 4**
- **D3 Debt ÷ Equity** = 6,830.98 ÷ 23,677.80 = **0.29x** → 0.1-0.5x band → **Score 4**
- **D4 Current Ratio** = Current Assets (₹7,240.00+21,401.59+1,307.55+3,493.76=₹33,442.90L) ÷
  Current Liabilities (₹15,806.27L) = **2.12x** → ≥2.0x band → **Score 5**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 14/20

- **E1 Promoter holding (latest available)**: **54.20% post-issue** (prospectus, "Our
  Promoters" table, page 169 — Manikandan Dakshna moorthy 27.10% + Venkatesan
  Dakshinamoorthy 27.10%; Nandhini Manikandan and Sathishkumar Venkatesan hold Nil). This is
  the post-IPO figure as of listing (18-Sep-2025, ~10 months before this run date); **no
  quarterly shareholding pattern filing dated closer to Jul-2026 was supplied** — flagged as
  the best available, not confirmed current. → 50-59.9% band → **Score 4**
- **E2 Promoter holding change**: pre-issue 74.40% → post-issue 54.20% (prospectus p.69,
  p.76-77), a −20.2pp move, entirely from **primary dilution** (fresh-issue preferential
  allotments to unrelated investors in Aug/Dec 2024 at ₹290-300/share premium, then the IPO
  fresh issue in Sept 2025 at ₹140/share) — not any promoter secondary sale-down. Going back
  further, promoters + immediate family held 100% of the pre-Aug-2024 share count
  (49,95,000 shares, prospectus p.69-73), so the multi-year decline is larger still and is
  the capital-raising history of a company scaling from private to listed, not an exit
  signal. A clean 3-year, quarter-by-quarter promoter-holding series (the form this metric is
  normally computed on) is **N/A (not in provided data)** for a company listed under 12
  months. Scored **0** per the mechanical rule (decrease >3pp) — **the qualitative
  distinction from a sale-down is carried here, not silently dropped.**
- **E3 Promoter pledge**: **0%** — prospectus shareholding-pattern table explicitly answers
  "Whether any shares held by Promoters are pledge or otherwise encumbered? No" (prospectus
  p.75), and the promoter build-up table shows "No. of Shares Pledged" = NA/nil for both
  promoters (prospectus p.79) → 0% band → **Score 5**
- **E4 Contingent Liabilities ÷ Net Worth**: Contingent liabilities (claims against the
  company not acknowledged as debt — two GST demands under appeal, ₹20.01L + ₹19.88L) =
  ₹39.89L as at 31-Mar-2025 (prospectus, Restated Financials Annexure XXXIX, "prospectus
  CFS35"). Net Worth (restated, consolidated, same date) = ₹11,080.17L. Ratio = 39.89 ÷
  11,080.17 = **0.36%**. **This is the most recent contingent-liability disclosure available
  — FY26 results filings do not carry a contingent-liabilities note** (interim/annual board
  outcomes are P&L/B/S/CF only) — flagged as a FY25-dated figure used as best available. →
  <5% band → **Score 5**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 15/60

Peer data was explicitly withheld from this run (FRONTSP-*.csv, TEXRAIL-*.csv excluded per
instruction) — every test requiring a peer comparison is scored 0 and marked "PEER DATA
NEEDED," not guessed.

| # | Test | Result | Score |
|---|---|---|---|
| M1 | Pricing Power | EBITDA margin 25.26% (FY25) → 20.25% (FY26), **−5.01pp**, outside the "declined 2-5pp" qualifying band despite ≥10% revenue growth | **0** |
| M2 | Cost Advantage vs peer | PEER DATA NEEDED | **0** |
| M3 | Capital Efficiency | FAT = Revenue÷Net Fixed Assets = 31,959.76÷5,041.04 = **6.34x**; ROCE = 25.22% → FAT>3x AND ROCE>20% | **5** |
| M4 | Customer Stickiness | 0 revenue-decline years (only 1 YoY window, positive); Receivable Days FY25→FY26 +2.29d (within ±10) — **based on 1-year window only, limited-history caveat stated** | **5** |
| M5 | Scale & Dominance | PEER DATA NEEDED | **0** |
| M6 | Technology / R&D | No R&D expense line disclosed for Airfloa standalone in any supplied statement — N/A (not in provided data) | **0** |
| M7 | Regulatory / License | PEER DATA NEEDED (count of listed segment players) | **0** |
| M8 | Distribution | No distribution-network metric disclosed (B2B rail-component manufacturer selling direct to Indian Railways/OEMs — not a distribution-network business model) | **0** |
| M9 | Brand | PEER DATA NEEDED (peer gross margin) | **0** |
| M10 | Switching Costs | Revenue grew in the only available year; Receivable Days rose +2.29d (≤10d) | **5** |
| M11 | Network Effects | Needs ≥6 years for the two-window test; only 2 years available. Scored conservatively per instruction — selling-expense % trend cannot be verified from supplied data (FY26 P&L does not break out selling expense separately) | **0** |
| M12 | Negative WC / Float | WC Days 238.07 (FY25), 264.99 (FY26) — both far above the 45-day ceiling | **0** |

**Moats present (score ≥3): 3** (M3 Capital Efficiency, M4 Customer Stickiness, M10 Switching
Costs) → **Moat class: MODERATE** (2-3 present band)

---

## ADDITIONAL FINDING — NOT SCORED, FLAGGED FOR DOWNSTREAM ATTENTION

The prospectus's restated-financials Annexure XLV(vii) ("prospectus CFS38") discloses that
Airfloa's **book-debt statements filed with its working-capital lenders** (Axis Bank, Union
Bank of India) **materially diverge from the books of account** for FY25, e.g. Q1 FY25: book
debts per books ₹118.73 Cr vs reported to Axis Bank ₹47.76 Cr (difference −₹70.97 Cr) and vs
Union Bank ₹98.65 Cr (difference −₹20.08 Cr). The company's stated reason is "netting-off
advances" / stock-statement scoping to project-specific facility allocation, but the
magnitude (roughly 40-60% of book debts in Q1) is large enough to be a lender-reporting /
data-integrity item worth downstream diligence, separate from and additional to the Block B
cash-conversion weakness. Carried as a second FLAG-GATE0 entry below.

---

## SCORECARD SUMMARY

```
BLOCK A  Return on Capital          ███████████████░░░░░  15/20
BLOCK B  Cash Generation Quality    ░░░░░░░░░░░░░░░░░░░░░   0/20  <- weakest
BLOCK C  Growth                     ███████████████░░░░░  15/20
BLOCK D  Balance Sheet Strength     █████████████████░░░  17/20  <- strongest
BLOCK E  Shareholder Alignment      ██████████████░░░░░░  14/20
                                    ─────────────────────
CORE SCORE (A+B+C+D)                                       47/80

BLOCK F  Quantitative Moat          ███████░░░░░░░░░░░░░  15/60
Moats present: 3 (Capital Efficiency, Customer Stickiness, Switching Costs)
Moat class: MODERATE

GRAND TOTAL (Core + E + Moat)                               76/160
```

## DATA CONFIDENCE

2 years of financial statements (FY25, FY26) → **<3 years band → data confidence AVERAGE,
auto** (per the fixed confidence table). This is a direct, documented consequence of the
company's recent listing (18-Sep-2025; formerly Airflow Equipments India Pvt Ltd, converted
to public limited Nov-2024) — not a data gap invented by this stage.

## DEAL-BREAKER OVERRIDES TRIGGERED

1. **Block B < 8** (Block B = 0/20) → caps classification at max **GOOD**
2. **Cumulative CFO ÷ PAT < 0.50** (ratio = −0.93x) → caps classification at max **AVERAGE**
3. **History < 3 years** (2 years supplied: FY25-FY26) → caps classification at **AVERAGE**

Not triggered: Block A <8 (A=15); median ROCE <10% (33.26%); pledge >15% (0%); ND/EBITDA>3x
AND IC<3x (0.85x / 7.14x); revenue declined in majority of years (grew); PAT negative in any
of the last 3 years (both available years positive — only 2 years exist to test).

## CLASSIFICATION

Core score 47 falls in the 40-59 band → **AVERAGE** on the classification matrix alone,
independent of and consistent with the deal-breaker caps above. Moat class (MODERATE) does
not change the outcome at this Core band.

**CLASSIFICATION: AVERAGE**

## STRONGEST / WEAKEST BLOCK

- **Strongest: Block D, Balance Sheet Strength (17/20).** The company is comfortably
  capitalised post-IPO (D/E 0.29x, current ratio 2.12x, net debt/EBITDA 0.85x), which is the
  direct fruit of the September 2025 fresh-issue proceeds (₹91.10 Cr gross) — most of it used
  for working capital and loan repayment per the IPO utilisation table.
- **Weakest: Block B, Cash Generation Quality (0/20).** Every sub-metric failed. The
  business is profitable on paper (PAT up 52% YoY) but is burning cash at an accelerating
  rate (FCF −₹8.5 Cr FY25 → −₹74.6 Cr FY26) because receivables and inventory are growing
  faster than revenue. This is the single most important number in this scorecard for the
  next stage to carry forward.

## DECISION LINE

AVERAGE, capped there independently by Core score (47/80), by Block B < 8, and by
cumulative CFO/PAT < 0.50 — three separate mechanisms landing on the same tier. The company's
growth (revenue +66% YoY) and balance-sheet strength (post-IPO, low leverage) are real and
anchored, but they sit on top of a cash-conversion profile that is deteriorating in absolute
terms and a financial history too short (2 years) to confirm the growth or the moat tests are
durable. Per pipeline rules this classification does not halt the run — it flags forward with
the depressors named above so downstream stages weigh them explicitly. No STOP verdict exists
in this pipeline; company-quality findings propagate as flags only.

---

```yaml
stage: B01-gate0
company: "544516"
run_date: "2026-07-15"
model: claude-sonnet-5
status: complete
input_gaps:
  - "prospectus: PRESENT — supplied under inputs/annual-report/1758608206692.pdf (IPO Prospectus dated 16-Sep-2025, not a post-listing Annual Report); used for promoter shareholding, capital structure, FY25 restated financials, contingent liabilities. This corrects the task brief's 'prospectus ABSENT' note."
  - "annual report (true post-listing FY26 statutory AR with Directors' Report, MGT-7 full shareholding pattern, FY26 contingent liabilities note): ABSENT"
  - "rating: ABSENT — no credit rating agency report supplied or found"
  - "research: ABSENT — no third-party equity research supplied or found"
  - "promoter shareholding more recent than 18-Sep-2025 (IPO listing date, post-issue disclosure): ABSENT — no quarterly shareholding pattern filing closer to run date supplied"
  - "peer data (screener CSVs for FRONTSP, TEXRAIL): EXCLUDED per explicit instruction, not used for Airfloa's Gate 0 — drives PEER DATA NEEDED zero-scores on Moat tests M2, M5, M7, M9"
  - "3-year restated financial history (FY23-FY25): NOT FOUND in prospectus despite a summary-page reference to FY2023/2024/2025 — the actual restated financial statement annexures (CFS/SFS) supplied cover FY2025 only, single year"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE with historical depressors identified: only 2 years of financial history (recently listed Sep-2025); cumulative CFO/PAT -0.93x with both years' FCF negative and worsening in absolute terms (-Rs8.5 Cr FY25 to -Rs74.6 Cr FY26), driven by working capital days rising +26.9 (COGS basis) as receivables outgrew revenue; ROCE declined 16.08pp YoY (41.30% to 25.22%) mechanically from IPO equity-base dilution, not operating deterioration; promoter holding fell from 100% (pre-Aug-2024) to 54.20% (post-IPO) entirely via primary capital raises, not secondary sale-down."
  - type: FLAG-GATE0
    reason: "Prospectus Annexure XLV(vii) discloses FY25 book-debt statements filed with working-capital lenders (Axis Bank, Union Bank) materially diverge from books of account, e.g. Q1 FY25 book debts per books Rs118.73 Cr vs Rs47.76 Cr reported to Axis Bank (Rs70.97 Cr gap); stated reason is stock-statement/netting scoping, not restated financial misstatement, but the magnitude warrants downstream lender-reporting diligence."
data_years: 2
fy_range: "FY25 to FY26"
blocks: {A: 15, B: 0, C: 15, D: 17, E: 14}
core_score: 47
moat_score: 15
grand_total: 76
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "Block B < 8 (Block B = 0/20) -> max GOOD"
  - "Cumulative CFO / PAT < 0.50 (ratio -0.93x) -> max AVERAGE"
  - "History < 3 years (2 years: FY25-FY26, listed 18-Sep-2025) -> AVERAGE"
history_downgrade: true
data_notes:
  - "CAGR metrics (C1-C4) computed with n=1 year (only FY25-FY26 comparison available); formula reduces to simple one-year growth, not a multi-year compounded trend -- stated, not hidden"
  - "A3 ROE FY25 uses closing net worth only (opening/FY24 net worth not supplied), per formula fallback rule -- stated"
  - "B4/M4/M10/M12 WC Days use Receivable Days on revenue basis (formula-fixed) and Inventory/Payable Days on COGS basis (Cost of Material Consumed explicitly disclosed) -- basis stated"
  - "Data_Sheet.csv (screener) FY25 net profit Rs25.55 Cr reconciles to the prospectus's RESTATED CONSOLIDATED FY25 PAT (Rs25.5476 Cr), not the FY26-results-filing's STANDALONE FY25 comparative PAT (Rs25.78 Cr) used throughout this scorecard for like-for-like standalone comparability; ~0.9% gap disclosed, immaterial to all score bands"
  - "M6 Technology/R&D scored 0: no R&D expense line disclosed for Airfloa standalone in any supplied statement -- N/A (not in provided data), not estimated"
  - "M11 Network Effects scored 0 conservatively per instruction: only 2 years available vs the 6-year two-window test requirement; selling-expense % trend not verifiable from supplied P&L breakdowns"
  - "Screener CSVs screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv are empty (headers only) -- not used; screener-Data_Sheet.csv was the only populated screener source and was cross-checked against, not substituted for, the primary results/prospectus filings"
block_b_trend: "deteriorating -- cumulative CFO/PAT -0.93x across both available years; WC days rose from 238.07 to 264.99 (+26.92 days, COGS basis) as receivables (+Rs86.42 Cr YoY) outgrew revenue (+Rs127.21 Cr YoY); FCF went from -Rs8.5 Cr (FY25) to -Rs74.6 Cr (FY26), worsening in absolute terms even as PAT grew 52%"
```
