# GATE 0 SCORECARD — Virtuoso Optoelectronics Ltd (VOEPL)
Run date: 2026-07-18 | Model: Sonnet 5 | Stage: B01-gate0

Data available: 3 years (FY2024 to FY2026). Scoring adapted to 3-year
history. This is the entirety of the P&L/BS/CF history populated in the
screener export (screener-Data_Sheet.csv); the company listed on BSE SME
c.2022 and pre-IPO/DRHP restated financials were not collected into this
workbook (prospectus gap, per orchestrator context — noted, not
independently verified in this stage).

## MECHANICAL / ENVIRONMENT FAILURE — READ FIRST
The three PDF inputs (two results PDFs and the FY24-25 Annual Report)
could **not** be extracted in this run. `pdftoppm` (poppler-utils) is not
installed in the execution environment: page-limited reads
(`pages="1-3"`, `pages="1"`, `pages="1-2"`) all failed with
`pdftoppm is not installed`. Whole-file reads (no page range) completed
without error but returned no extractable text or tabular content for any
of the three files (3c69ed09-...pdf, 7fc85d5c-...pdf,
6ff4905d-...pdf). This was retried twice per file. This is a tool/
environment failure, not a company-quality issue, and is recorded under
`input_gaps` below, not as a scoring penalty.

Consequently every number in this scorecard is drawn from
**screener-Data_Sheet.csv only** — the sole populated screener file.
screener-Profit_Loss.csv, screener-Balance_Sheet.csv,
screener-Cash_Flow.csv, screener-Quarters.csv (ratio section) and
screener-Customization.csv were opened and confirmed to be **empty
templates** (headers only, no data rows) — checked directly, not
assumed. All figures that would normally come from the Annual Report or
results PDFs (shareholding pattern, contingent liabilities, trade
payables, capex/PPE breakup, R&D, peer detail) are therefore
"N/A (not in provided data)" and scored 0 per the grounding rule, not
estimated.

Per orchestrator instruction, the contextually supplied promoter holding
figure (49.74%) and FII trend are **not** used as a scored Gate 0 number
in this stage — they arrive without a page/document anchor verifiable
against the sources listed for this stage, and the rules require every
number to be anchored. Block E is scored on grounds of unavailability,
not on the (unanchored) context figures.

## EXTRACTED BASE DATA (screener-Data_Sheet.csv, PROFIT & LOSS / BALANCE
SHEET / CASH FLOW sections, rows 9-63)

| Item (Rs Cr) | FY24 | FY25 | FY26 |
|---|---|---|---|
| Sales | 531.06 | 697.32 | 823.6 | (screener-data)
| Raw Material Cost | 440.16 | 579.04 | 690.65 | (screener-data)
| Employee Cost | 12.95 | 20.55 | 29.85 | (screener-data)
| Other Income | 1.22 | 5.04 | 2.39 | (screener-data)
| Depreciation | 18.3 | 10.27 | 27.91 | (screener-data)
| Interest | 20.11 | 25.38 | 33.47 | (screener-data)
| PBT | 14.36 | 25.15 | 24.51 | (screener-data)
| Tax | 4.2 | 11.06 | 9.49 | (screener-data)
| Net Profit (PAT) | 10.17 | 14.09 | 15.03 | (screener-data)
| Equity Share Capital | 26.34 | 29.49 | 31.83 | (screener-data)
| Reserves | 183.24 | 252.32 | 380.39 | (screener-data)
| Borrowings | 134.97 | 171.5 | 344.56 | (screener-data)
| Other Liabilities | 111.25 | 158.71 | 212.38 | (screener-data)
| Net Block | 130.55 | 208.55 | 452.0 | (screener-data)
| CWIP | 6.89 | 48.07 | 38.21 | (screener-data)
| Investments | 100.22 | 41.77 | 102.13 | (screener-data)
| Receivables | 21.31 | 30.58 | 72.22 | (screener-data)
| Inventory | 164.76 | 213.08 | 227.39 | (screener-data)
| Cash & Bank | 0.09 | 2.36 | 1.01 | (screener-data)
| Cash from Operating Activity | 13.75 | 30.6 | 3.33 | (screener-data)
| Cash from Investing Activity | -150.08 | -99.75 | -185.58 | (screener-data)
| Cash from Financing Activity | 136.07 | 71.42 | 180.9 | (screener-data)

FY26 headline cross-check: consol revenue Rs823.6 Cr, PAT Rs15.03 Cr — both
confirmed directly in screener-Data_Sheet.csv row 11 and row 24
(screener-data). Matches orchestrator's supplied cross-check.

Note (data_notes): FY26 Power & Fuel, Other Mfr. Exp. and Selling & admin
rows are blank in the Data_Sheet (screener-data); Operating Profit for
FY26 was therefore **computed** as PBT + Depreciation + Interest − Other
Income = 24.51 + 27.91 + 33.47 − 2.39 = 83.50 Cr, and cross-validated
against the Quarters section: Q1+Q2+Q3+Q4 FY26 Operating Profit
(20.07+10.1+24.27+29.05) = 83.49 Cr (screener-data, Quarters section) —
reconciled to within rounding. Same OP formula applied to FY24 and FY25
for consistency (both years reconcile exactly against Sales−Expenses in
the underlying line items where fully populated).

Computed Operating Profit (EBITDA proxy, excl. other income): FY24 =
51.55 Cr (OPM 9.71%), FY25 = 55.76 Cr (OPM 8.00%), FY26 = 83.50 Cr (OPM
10.14%) — computed (screener-data, PBT+Dep+Interest−OI formula).

Computed EBIT (= PBT + Interest, standard for ROCE): FY24 = 34.47, FY25 =
50.53, FY26 = 57.98 — computed (screener-data).

Computed Capital Employed (Net Worth + Borrowings; Balance Sheet does not
split Other Liabilities into current/non-current, so the standard
screener proxy — Total Assets − Current Liabilities ≈ Equity + Total Debt
— is used and stated): FY24 = 344.55, FY25 = 453.31, FY26 = 756.78 —
computed, proxy basis (screener-data).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE (computed, EBIT ÷ Capital Employed, proxy basis stated above):
FY24 = 34.47 ÷ 344.55 = 10.00% | FY25 = 50.53 ÷ 453.31 = 11.15% |
FY26 = 57.98 ÷ 756.78 = 7.66% — computed (screener-data)

ROE (PAT ÷ average Net Worth; FY24 uses closing Net Worth only, no FY23
opening figure available — stated per formula rule):
FY24 = 10.17 ÷ 209.58 (closing) = 4.85% | FY25 = 14.09 ÷ avg(209.58,
281.81) = 5.74% | FY26 = 15.03 ÷ avg(281.81, 412.22) = 4.33% — computed
(screener-data)

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| A1 | Median ROCE | 10.00% (FY24, 11.15% FY25, 7.66% FY26) | 10-14.9% | 1 |
| A2 | Minimum single-year ROCE | 7.66% (FY26) | <8% | 0 |
| A3 | Median ROE | 4.85% | <12% | 0 |
| A4 | ROCE trend, FY26 vs FY24 | 7.66% vs 10.00% = decline 2.34pp | decline 1-3pp | 3 |

**Block A = 4 / 20**

data_note: median ROCE 10.00% sits essentially at the 10% deal-breaker-3
threshold; precise computed value is 10.0015% (>10%), so deal-breaker 3
(median ROCE <10% → max AVERAGE) narrowly does NOT trigger.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY24-26) = 13.75+30.6+3.33 = 47.68 Cr (screener-data)
Cumulative PAT (FY24-26) = 10.17+14.09+15.03 = 39.29 Cr (screener-data)

FCF = CFO − Capex. Capex (purchase of PPE + intangibles) is **not**
separately disclosed in screener-Data_Sheet.csv — only the aggregate
"Cash from Investing Activity" is given, which also includes
investment purchases/sales (Investments balance-sheet line moves
100.22→41.77→102.13, confirming non-capex flows are material within
Investing Activity). Per the grounding rule this is marked N/A, not
estimated from Net Block movement.

Trade Payables are **not** disclosed anywhere in the provided sources
(no Payables line in Balance Sheet section of Data_Sheet; Annual Report
unreadable). Payable Days, hence full WC Days, is N/A.

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| B1 | Cumulative CFO ÷ Cumulative PAT | 47.68 ÷ 39.29 = 1.21x | ≥1.00 | 5 |
| B2 | FCF-positive years proportion | N/A (not in provided data — capex not isolable) | — | 0 |
| B3 | Cumulative FCF ÷ Cumulative PAT | N/A (not in provided data) | — | 0 |
| B4 | Change in WC Days, latest vs earliest | N/A (Payable Days not in provided data) | — | 0 |

**Block B = 5 / 20**

Partial WC context (Receivable Days + Inventory Days only, Payable Days
excluded — NOT the scored metric, shown for record): Receivable Days
(Trade Receivables ÷ Revenue × 365, revenue basis since COGS not
explicitly separable): FY24 = 14.65, FY25 = 16.01, FY26 = 32.01 —
computed (screener-data). Inventory Days (revenue basis, stated):
FY24 = 113.24, FY25 = 111.55, FY26 = 100.79 — computed (screener-data).

block_b_trend: **deteriorating**. CFO/PAT ratio by year: FY24 = 1.35x,
FY25 = 2.17x, FY26 = 0.22x — computed (screener-data, CFO and PAT rows).
Cash conversion collapsed in FY26 even as PAT kept growing; receivable
days nearly doubled over the same year (16.01 → 32.01). Feeds
FLAG-CASH downstream.

---

## BLOCK C: GROWTH (Max 20)

Revenue CAGR (FY24→FY26, 2yr): (823.6÷531.06)^(1/2) − 1 = 24.54% —
computed (screener-data)
PAT CAGR (FY24→FY26, 2yr): (15.03÷10.17)^(1/2) − 1 = 21.59% — computed
(screener-data)

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| C1 | Revenue CAGR | 24.54% | ≥20% | 5 |
| C2 | PAT CAGR | 21.59% | ≥20% | 5 |
| C3 | Positive YoY revenue years | 2/2 (100%) — only 2 YoY comparisons exist given 3-yr history | 100% | 5 |
| C4 | PAT CAGR − Revenue CAGR | 21.59 − 24.54 = −2.95pp | ±3pp | 3 |

**Block C = 18 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Net Debt FY26 = Borrowings − Cash & Bank = 344.56 − 1.01 = 343.55 —
computed (screener-data)
EBITDA FY26 (Operating Profit, computed above) = 83.50

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| D1 | Net Debt ÷ EBITDA (FY26) | 343.55 ÷ 83.50 = 4.11x | >3x | 0 |
| D2 | Interest Coverage, EBIT ÷ Interest (FY26) | 57.98 ÷ 33.47 = 1.73x | 1.5-2.9x | 1 |
| D3 | Debt ÷ Equity (FY26) | 344.56 ÷ 412.22 = 0.84x | 0.5-1.0 | 3 |
| D4 | Current Ratio (FY26) | N/A (Current Assets/Current Liabilities split not in provided data) | — | 0 |

**Block D = 4 / 20**

Leverage trend context (not separately scored, all years computed from
screener-data): ND/EBITDA FY24 = 2.62x, FY25 = 3.03x, FY26 = 4.11x —
rising every year. Interest Coverage FY24 = 1.71x, FY25 = 1.99x, FY26 =
1.73x — persistently weak across all three years, not a one-off. This
coincides with heavy capex (Net Block + CWIP nearly quadrupled FY24→FY26:
137.44 → 256.62 → 490.21) and large financing inflows (136.07, 71.42,
180.9 Cr) — consistent with the orchestrator's noted compressor-line
capacity build (from Jan-2026), but that qualitative context is not
independently verified in this stage (source documents unreadable).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding-pattern, pledge, or contingent-liability data exists in
any source available to this stage: screener-Data_Sheet.csv has no
shareholding section; the other screener CSVs are empty templates; the
results PDFs and Annual Report could not be read (see mechanical-failure
note above). Per rule, all four items are marked N/A and scored 0 — this
is NOT a judgment that alignment is poor, simply that no anchored figure
exists in this stage's inputs.

| # | Metric | Value | Score |
|---|---|---|---|
| E1 | Promoter holding (latest quarter) | N/A (not in provided data) | 0 |
| E2 | Promoter holding change, 3yr | N/A (not in provided data) | 0 |
| E3 | Promoter pledge (latest) | N/A (not in provided data) | 0 |
| E4 | Contingent Liabilities ÷ Net Worth | N/A (not in provided data — AR unreadable) | 0 |

**Block E = 0 / 20**

---

## CORE SCORE

A (4) + B (5) + C (18) + D (4) + E (0) = **31 / 100**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

| # | Test | Basis | Score |
|---|---|---|---|
| M1 | Pricing Power | OPM 9.71%→10.14%, Δ +0.43pp (stable ±2pp); Rev CAGR 24.54% (≥10%) — computed (screener-data) | 3 |
| M2 | Cost Advantage vs peer median | PEER DATA NEEDED (AMBER/ELIN/EPACK/PGEL financials not in provided sources) | 0 |
| M3 | Capital Efficiency | FAT (Rev÷Net Block, FY26) = 823.6÷452.0 = 1.82x; ROCE FY26 = 7.66% — neither threshold tier met (needs FAT>1x AND ROCE>12% minimum) — computed | 0 |
| M4 | Customer Stickiness | 0 revenue-decline years (≤"max 1 decline" tier satisfied vacuously); receivable days rose 17.4 days so top tier (stable ±10) not met | 3 |
| M5 | Scale & Dominance | PEER DATA NEEDED (mcap/margin ranking vs AMBER/ELIN/EPACK/PGEL not provided) | 0 |
| M6 | Technology / R&D | R&D not disclosed in provided data | 0 |
| M7 | Regulatory / License | EMS/contract manufacturing — unregulated segment per test definition | 0 |
| M8 | Distribution | Reach/outlet metrics not disclosed in provided data | 0 |
| M9 | Brand | GM proxy computed (17.12%→16.14%, declining) but PEER DATA NEEDED for the comparison the test requires | 0 |
| M10 | Switching Costs | Revenue grew every year, but receivable days rose 17.4 days (>10) — fails the "stable" clause in both top tiers; literal conditions for tiers 3/1 not met either | 0 |
| M11 | Network Effects | Only 3 years available (<6 required) — scored conservatively per rule. Rev CAGR 24.54% (≥20%) but selling & admin % rose FY24→FY25 (1.65%→2.31%, screener-data); FY26 selling expense not separately disclosed | 1 |
| M12 | Negative WC / Float | Payable Days not in provided data — true WC Days indeterminate (partial Receivable+Inventory days alone run 100-133 days across all years, but this excludes payables and cannot be scored per formula) | 0 |

**Moat score = 3+0+0+3+0+0+0+0+0+0+1+0 = 7 / 60**

Moats present (score ≥3): M1 (Pricing Power), M4 (Customer Stickiness) = **2 moats confirmed**

Moat classification: 2 present → **MODERATE**

data_notes (moat block): M2, M5, M9 marked "PEER DATA NEEDED" (peer set
per orchestrator: AMBER, ELIN, EPACK, PGEL — no peer financials supplied
to this stage). M6, M8 marked N/A (not in provided data). M7 is a
genuine 0 (unregulated segment), not a data gap.

---

## GRAND TOTAL

Core Score (31) + Moat Score (7) = **38 / 160**

---

## DEAL-BREAKER OVERRIDES (recorded, mechanical check against original
rules)

| # | Rule | Triggered? | Detail |
|---|---|---|---|
| 1 | Block A <8 → max GOOD | YES | Block A = 4 |
| 2 | Block B <8 → max GOOD | YES | Block B = 5 |
| 3 | Median ROCE <10% → max AVERAGE | NO | Median ROCE = 10.00% (10.0015% precise), not <10% |
| 4 | Cumulative CFO/PAT <0.50 → max AVERAGE | NO | 1.21x |
| 5 | Pledge >15% → max AVERAGE | NO | No evidence (N/A, not scored as triggered) |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | **YES** | ND/EBITDA 4.11x AND IC 1.73x (both FY26) |
| 7 | Revenue declined majority of years → max AVERAGE | NO | Revenue grew both YoY periods |
| 8 | PAT negative in any of last 3 years → max AVERAGE | NO | PAT positive all 3 years |
| 9 | History <3 years → AVERAGE | NO | Exactly 3 years available |

Deal-breaker 6 is a hard AVOID override, independently confirming the
core-score-band result below.

---

## DATA CONFIDENCE / HISTORY

3 years of data (FY2024-FY2026) falls in the **3-4 LIMITED** tier per the
data-confidence rule → classification downgrade one tier applies
mechanically. Per orchestrator context this is a genuine short-history
name (BSE SME listing c.2022, pre-IPO restated financials not collected
into the screener workbook) — legitimately LIMITED, not a proxy for
company quality. Since the mechanical classification already resolves to
the floor (AVOID, see below), the one-tier downgrade has no further
effect on the output but `history_downgrade: true` is set per rule.

---

## CLASSIFICATION

Core Score = 31 (<40 band) → **AVOID** per classification matrix, Core
<40 row (independent of moat class). Confirmed independently by
deal-breaker 6 (ND/EBITDA >3x AND IC <3x → AVOID).

**Classification: AVOID**

---

## STRONGEST / WEAKEST BLOCK

Strongest: **Block C — Growth (18/20)**. Revenue and PAT both compounding
above 20% over the 2-year window with no decline years.

Weakest: **Block E — Shareholder Alignment (0/20)**, tied with the
combination of Block A (Return on Capital, 4/20) and Block D (Balance
Sheet Strength, 4/20) as scored deficiencies. Block E's 0 is a data
coverage gap (mechanical PDF failure), not a demonstrated governance
weakness — this distinction is material for downstream stages and should
not be read as an alignment red flag. Blocks A and D are genuine
extracted-number weaknesses: sub-10% returns on capital and leverage
(ND/EBITDA 4.11x, Interest Coverage persistently under 2x across all
three years) that are NOT data gaps.

---

## DECISION LINE

Gate 0 mechanical classification is **AVOID**, driven by weak returns on
capital (median ROCE 10.00%, min 7.66%), a hard deal-breaker on leverage
plus coverage (ND/EBITDA 4.11x AND Interest Coverage 1.73x, FY26), and a
FY26 cash-conversion collapse (CFO/PAT fell from 2.17x to 0.22x
year-on-year) layered on top of a genuinely LIMITED 3-year data history.
Growth is strong (Block C = 18/20, Revenue and PAT CAGR both >20%) and
two moat tests register (Pricing Power, Customer Stickiness — MODERATE
moat class, 2 confirmed), but per pipeline rules company quality never
halts a run — this classification and its drivers propagate to
downstream stages as flags, not a stop. Block E (0/20) reflects a data
coverage gap this stage could not close (PDF extraction tool failure),
not an alignment finding, and should be re-attempted with a working PDF
pipeline before being weighed as evidence. Block D's leverage and
coverage numbers, and Block B's FY26 cash-conversion deterioration, are
both extracted-number findings (not gaps) and should be read together
with the orchestrator-noted capacity expansion (compressor line from
Jan-2026) at later valuation and cash-conversion stages.

---

```yaml
stage: B01-gate0
company: "VOEPL"
run_date: "2026-07-18"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Results PDFs (3c69ed09-...pdf, 7fc85d5c-...pdf) and Annual Report PDF (6ff4905d-...pdf) could not be read: pdftoppm/poppler-utils not installed in execution environment; page-limited reads errored (pdftoppm is not installed), whole-file reads returned no extractable content, retried twice per file"
  - "screener-Profit_Loss.csv, screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv (ratio rows), screener-Customization.csv are empty templates, no populated data rows"
  - "Trade Payables not disclosed anywhere in provided sources - Payable Days, WC Days trend (B4), M12 not computable"
  - "Capex/PPE purchase breakdown not disclosed (only aggregate Investing Activity given) - FCF (B2, B3) not computable"
  - "Current Assets/Current Liabilities split not disclosed - Current Ratio (D4) not computable"
  - "Shareholding pattern (promoter %, pledge, FII/DII) not present in any readable source for this stage - Block E (E1-E4) not computable"
  - "Contingent liabilities note not accessible (Annual Report unreadable) - E4 not computable"
  - "R&D spend, distribution/outlet metrics, peer (AMBER/ELIN/EPACK/PGEL) financials not present in provided sources - M2, M5, M6, M8, M9 not fully computable"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID (core 31/100, deal-breaker 6 triggered: ND/EBITDA 4.11x AND Interest Coverage 1.73x FY26). Historical depressors: sub-10% returns on capital in a LIMITED 3-year (FY24-FY26) history, rising leverage every year (ND/EBITDA 2.62x->3.03x->4.11x), persistently weak interest coverage (1.71x-1.99x range all 3 years), and a FY26 cash-conversion collapse (CFO/PAT 2.17x FY25 -> 0.22x FY26) concurrent with heavy capex (Net Block+CWIP roughly quadrupled FY24-FY26). Growth strong (Rev/PAT CAGR both >20%) and 2 moat tests present (Pricing Power, Customer Stickiness). Flags propagate; verdict decision remains human per pipeline rules."}
data_years: 3
fy_range: "FY24 to FY26"
blocks: {A: 4, B: 5, C: 18, D: 4, E: 0}
core_score: 31
moat_score: 7
grand_total: 38
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers: ["1: Block A <8 (=4) -> max GOOD", "2: Block B <8 (=5) -> max GOOD", "6: ND/EBITDA 4.11x AND Interest Coverage 1.73x (FY26) -> AVOID"]
history_downgrade: true
data_notes:
  - "FY26 Power & Fuel, Other Mfr. Exp., Selling & admin rows blank in screener-Data_Sheet.csv; Operating Profit computed via PBT+Depreciation+Interest-Other Income and cross-validated against Quarters section (83.50 computed vs 83.49 from quarterly sum, reconciled)"
  - "Capital Employed computed as Equity+Reserves+Borrowings (proxy for Total Assets-Current Liabilities) since Balance Sheet does not split Other Liabilities into current/non-current"
  - "ROE FY24 uses closing Net Worth only, no FY23 opening figure available, per formula rule"
  - "Median ROCE 10.00% (precise 10.0015%) sits at deal-breaker-3 threshold (<10% -> max AVERAGE); narrowly does not trigger"
  - "M9 gross-margin proxy computed (Revenue-Material Cost)/Revenue = 17.12% FY24 -> 16.14% FY26, declining, but not scored (PEER DATA NEEDED for the comparison the test requires)"
  - "M11 scored conservatively: only 3 years available vs 6 required for two-window test"
  - "Orchestrator-supplied promoter holding (49.74%) and FII trend not used as scored figures in this stage - no verifiable source anchor within this stage's provided inputs"
block_b_trend: "deteriorating - CFO/PAT ratio fell from 2.17x (FY25) to 0.22x (FY26), screener-Data_Sheet CFO and PAT rows"
```
