# STAGE 1 — GATE 0 SCORECARD: K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND)
Run date: 2026-07-21 | Model: claude-sonnet-5 | Mode: NO-CONCALL, full pipeline restart

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

## MECHANICAL DATA-ACCESS NOTICE (read first)

Of the five listed data sources, only the **screener Data_Sheet CSV** was
actually extractable in this environment. All three result/rating PDFs and
the Annual Report PDF failed for a tooling reason, not a data-availability
reason:

- `pdftoppm` (poppler-utils) is **not installed** in this environment. Every
  `pages`-scoped PDF read (needed for any PDF >10 pages) errors with
  "pdftoppm is not installed."
- Whole-file reads of the three smaller PDFs (FY26 audited results PDF,
  Q3 FY26 unaudited results PDF, CARE rating PR) returned only a file-size
  confirmation with no extractable text/content — no usable data was
  delivered by the tool for any of them.
- The FY24-25 Annual Report PDF additionally exceeds the 20MB whole-file
  read ceiling (first pages are scanned/OCR per the task brief), so it
  could not be read by any method.

Net effect: **all figures in this scorecard are anchored to the screener
Data_Sheet CSV only.** Every field that would have required the PDFs
(promoter holding/pledge, contingent liabilities, current ratio granularity,
exact capex, segment detail, CARE's own gearing/coverage figures) is marked
**NOT FOUND** below and is not estimated. This is flagged as FLAG-DATA-GAP
in the YAML block and should drive a re-run of this stage once PDF
extraction is fixed, before Blocks D4 and E are treated as final.

One partial mitigation: the screener CSV's own FY26 quarterly columns
(Q1-Q4 FY26) sum to the FY26 annual column (Sales 259.95cr vs
59.37+67.20+64.58+68.80=259.95; PAT 11.13cr vs 19.15+0.42+6.75-15.20=11.12,
rounding) — screener Data_Sheet CSV, cross-checked internally. This gives
some confidence in the FY26 annual P&L line even without the audited PDF.

`screener-Balance_Sheet.csv` and `screener-Cash_Flow.csv` were supplied as
empty header-only templates (no data rows) — superseded entirely by
`screener-Data_Sheet.csv`, which carries the equivalent figures.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formula notes (stated per prompt rule, since screener Data_Sheet CSV in
this export carries no ROCE/ROE rows): EBIT = PBT + Interest (screener
Data_Sheet CSV, computed); this necessarily includes Other Income since no
clean operating-only EBIT split is available (FY26 additionally has three
blank expense sub-lines — Power & Fuel, Other Mfr. Exp., Selling & admin —
in the CSV). Capital Employed = Net Worth + Borrowings (i.e. Total Assets
minus the "Other Liabilities" aggregate, since the CSV does not split
Other Liabilities into current/non-current) — computed proxy, stated.

| FY | PBT | Interest | EBIT=PBT+Int | Net Worth (Cap+Res) | Borrowings | Cap. Employed | ROCE |
|---|---|---|---|---|---|---|---|
|17|73.67|11.53|85.20|281.96|139.87|421.83|20.20%|
|18|-3.00|14.79|11.79|281.79|208.65|490.44|2.40%|
|19|33.93|19.76|53.69|297.10|220.50|517.60|10.37%|
|20|-10.76|21.86|11.10|289.22|265.24|554.46|2.00%|
|21|17.12|24.36|41.48|313.30|270.35|583.65|7.11%|
|22|5.16|19.70|24.86|315.28|189.56|504.84|4.92%|
|23|70.21|14.29|84.50|372.85|183.60|556.45|15.19%|
|24|78.87|11.19|90.06|438.68|146.67|585.35|15.39%|
|25|28.02|9.11|37.13|450.28|99.33|549.61|6.75%|
|26|15.73|7.75|23.48|459.51|127.71|587.22|4.00%|

(all inputs: screener Data_Sheet CSV, P&L / Balance Sheet rows, FY17-FY26)

**A1 Median ROCE = 6.93%** (sorted series median, 5th/6th of 10 = avg of
6.75% and 7.11%) → <10% band → **score 0**

**A2 Minimum single-year ROCE = 2.00% (FY20)** → <8% band → **score 0**

**A3 Median ROE = 4.86%** (see ROE table below) → <12% band → **score 0**

**A4 ROCE trend, FY26 (4.00%) vs FY17 (20.20%): decline of 16.20pp** →
decline >5pp → **score 0**

ROE table (PAT ÷ average Net Worth; FY17 uses closing Net Worth only, no
FY16 opening figure in the provided window, per formula rule):

| FY | PAT | Avg Net Worth | ROE |
|---|---|---|---|
|17|57.17|281.96 (closing only)|20.28%|
|18|11.50|281.88|4.08%|
|19|16.31|289.45|5.63%|
|20|-6.26|293.16|-2.14%|
|21|23.30|301.26|7.73%|
|22|3.58|314.29|1.14%|
|23|58.17|344.07|16.91%|
|24|66.16|405.77|16.30%|
|25|14.39|444.48|3.24%|
|26|11.13|454.90|2.45%|

(PAT: screener Data_Sheet CSV, "Net profit" row, FY17-FY26)

**Block A total = 0 + 0 + 0 + 0 = 0 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY17-FY26) = 152.63cr (screener Data_Sheet CSV, "Cash from
Operating Activity" row, sum of FY17-FY26).
Cumulative PAT (FY17-FY26) = 255.45cr (screener Data_Sheet CSV, "Net
profit" row, sum of FY17-FY26).

**B1 Cumulative CFO ÷ Cumulative PAT = 152.63 / 255.45 = 0.598** →
0.50-0.69 band → **score 1**

**B2 FCF-positive years / B3 Cumulative FCF ÷ Cumulative PAT: NOT FOUND.**
Formula requires capex = "purchase of PPE + intangibles from cash flow
statement." The screener Data_Sheet CSV provides only an aggregate "Cash
from Investing Activity" line (which also nets off the company's large
Investments book, ~147-293cr across the decade) with no PPE-purchase
sub-line, and the CF-statement PDFs that would carry this are unreadable
(see notice above). Per the "formulas fixed, do not substitute
alternatives" rule, no proxy (e.g. Δ Net Fixed Assets + Depreciation) was
substituted. **B2 = 0, B3 = 0, both N/A (not in provided data).**

**B4 Change in WC Days: NOT FOUND (partial).** Receivable Days and
Inventory Days are computable (table below, Revenue basis stated — Raw
Material Cost is only a partial COGS component in this CSV, not full
COGS, so Revenue basis is used per the formula's fallback rule) but
**Payable Days is NOT FOUND**: Trade Payables is not separately disclosed
in the screener Data_Sheet CSV (embedded inside the aggregate "Other
Liabilities" line). WC Days needs all three components per the fixed
formula, so **B4 = 0, N/A**.

| FY | Receivables | Receivable Days | Inventory | Inventory Days | Recv+Inv Days |
|---|---|---|---|---|---|
|17|32.96|27.20|225.15|185.86|213.06|
|18|28.75|29.86|219.84|228.28|258.14|
|19|28.43|28.87|378.69|384.58|413.45|
|20|37.12|34.51|344.67|320.42|354.93|
|21|46.30|51.45|261.58|290.55|342.00|
|22|29.31|33.50|215.48|246.28|279.78|
|23|22.11|27.87|230.29|290.36|318.23|
|24|29.20|30.83|204.75|216.24|247.07|
|25|48.62|57.16|133.38|156.79|213.95|
|26|57.40|80.60|155.78|218.75|299.35|

(screener Data_Sheet CSV, Receivables / Inventory / Sales rows, FY17-FY26)

**Block B total = 1 + 0 + 0 + 0 = 1 / 20**

**block_b_trend: deteriorating.** The one number: CFO fell from **+47.79cr
(FY25) to -30.89cr (FY26)** (screener Data_Sheet CSV, "Cash from Operating
Activity" row) — the first negative annual CFO print since FY19.

---

## BLOCK C: GROWTH (Max 20)

Revenue: FY17 442.17cr → FY26 259.95cr (screener Data_Sheet CSV, "Sales"
row). Both endpoints positive, 9-year window.

**C1 Revenue CAGR = (259.95/442.17)^(1/9) - 1 = -5.73%** → <5% band →
**score 0**

PAT: FY17 57.17cr → FY26 11.13cr (screener Data_Sheet CSV, "Net profit"
row). Both endpoints positive (not a loss-to-profit swing at the
endpoints, though FY20 PAT was -6.26cr mid-window — noted, not scored as
a swing per the CAGR edge rule).

**C2 PAT CAGR = (11.13/57.17)^(1/9) - 1 = -16.62%** → negative → **score 0**

**C3 Positive YoY revenue years: 3 of 9 (FY19, FY20, FY24) = 33.3%** → <50%
band → **score 0**

YoY revenue direction: FY18 down, FY19 up, FY20 up, FY21 down, FY22 down,
FY23 down, FY24 up, FY25 down, FY26 down (screener Data_Sheet CSV, Sales
row, FY17-FY26).

**C4 PAT CAGR − Revenue CAGR = -16.62% − (-5.73%) = -10.89pp** → <-8pp →
**score 0**

**Block C total = 0 + 0 + 0 + 0 = 0 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

All figures latest = FY26 (screener Data_Sheet CSV).

**D1 Net Debt ÷ EBITDA.** Net Debt = Borrowings − Cash & Bank = 127.71 −
39.35 = 88.36cr. EBITDA = EBIT + Depreciation = 23.48 + 5.95 = 29.43cr
(EBIT as defined in Block A; includes Other Income, see caveat above).
Net Debt/EBITDA = 88.36 / 29.43 = **3.00x** (precisely 3.002x) → >3x band
→ **score 0**. Borderline note: the company also carries a 292.76cr
Investments book (screener Data_Sheet CSV, "Investments" row, FY26) not
netted here — the strict Debt-minus-Cash definition is used because the
CSV does not disclose whether these investments are liquid/current or
strategic/illiquid; if fully netted the company would show net cash. This
distinction cannot be resolved without the unreadable Annual Report notes.

**D2 Interest Coverage = EBIT ÷ Interest = 23.48 / 7.75 = 3.03x** → 3-4.9x
band → **score 2**

**D3 Debt ÷ Equity = 127.71 / 459.51 = 0.28x** → 0.1-0.5x band → **score 4**

**D4 Current Ratio: NOT FOUND.** The screener Data_Sheet CSV does not
split Current Assets / Current Liabilities (Receivables, Inventory, Cash
& Bank plus an aggregate, unspecified "Other Assets" line; "Other
Liabilities" is likewise an unsplit aggregate). The CARE rating PR, which
would normally state this, was unreadable (mechanical failure, see
notice). **D4 = 0, N/A.**

**Block D total = 0 + 2 + 4 + 0 = 6 / 20**

Deal-breaker 6 near-miss: ND/EBITDA (3.00x, just over the >3x trigger) AND
IC (3.03x, just over the <3x trigger, so this leg does NOT fire) — both
metrics sit right at the boundary. Deal-breaker 6 is **not** triggered
(IC is not <3x), but this is a razor-thin non-trigger, flagged separately.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**All four sub-metrics: NOT FOUND (not in provided data).** No
shareholding-pattern export was supplied among the input files (per the
B00 restart inventory: "no shareholding" is a named gap), and the Annual
Report / CARE PR that would carry pledge and contingent-liability detail
are unreadable in this environment (mechanical failure, see notice).

- E1 Promoter holding: NOT FOUND → **score 0**
- E2 Promoter holding change (3yr): NOT FOUND → **score 0**
- E3 Promoter pledge: NOT FOUND → **score 0**
- E4 Contingent liabilities ÷ Net Worth: NOT FOUND → **score 0**

**Block E total = 0 / 20**

Deal-breaker 5 (pledge >15% → max AVERAGE) **cannot be evaluated** —
pledge % NOT FOUND. Flagged, not scored as triggered or clear.

---

## CORE SCORE

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 0 | 20 |
| B — Cash Generation Quality | 1 | 20 |
| C — Growth | 0 | 20 |
| D — Balance Sheet Strength | 6 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **Core Score** | **7** | **100** |

Strongest block: D (6/20) — carried entirely by D3 (Debt/Equity 0.28x,
score 4) and D2 (Interest Coverage 3.03x, score 2); D1 and D4 both zero.
Weakest blocks (fundamentals): A and C, both 0/20 — flat-zero on every
sub-metric, driven by sub-10% median ROCE/ROE and a shrinking top line.
Block E is also 0/20 but purely a data-availability gap, not a
fundamentals signal — excluded from the "weakest fundamentals" framing.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

No peer/sector data was supplied in any input source (no comparable-company
financials, no market-cap ranking, no listed-player counts) — every test
requiring peer comparison is marked **PEER DATA NEEDED** and scored 0 per
rule.

**M1 Pricing Power = 0.** Revenue CAGR -5.73% (<10% threshold for any
positive band); EBITDA margin swung from 21.46% (FY17) to 11.32% (FY26)
but through a highly volatile, Other-Income-distorted series (4.87%-31.08%
across the decade) — condition set requires growth, which is absent.
(EBITDA margin computed as (PBT+Interest+Depreciation)/Sales, screener
Data_Sheet CSV; includes Other Income, no clean operating-only split
available — data note.)

**M2 Cost Advantage vs peers = 0. PEER DATA NEEDED.**

**M3 Capital Efficiency = 0.** FAT (FY26) = Sales/Net Fixed Assets =
259.95/99.22 = 2.62x (CWIP FY26 blank in CSV; Net Block only used).
ROCE FY26 = 4.00%. FAT>2x is true but ROCE is nowhere near the required
>15%/>12% thresholds → else band → 0.

**M4 Customer Stickiness = 0.** 6 of 9 YoY revenue-decline years (see
Block C) → "3+ decline years" band → 0.

**M5 Scale & Dominance = 0. PEER DATA NEEDED** (requires market-cap /
segment-share comparison, not provided).

**M6 Technology / R&D = 0.** No R&D line disclosed anywhere in the
provided data → 0 (not in provided data).

**M7 Regulatory / License = 0. PEER DATA NEEDED** (sugar is a
government-regulated commodity but the count of listed players in the
segment is not provided data — no industry-knowledge substitution used).

**M8 Distribution = 0.** No distribution-reach data (outlets, network
growth) disclosed in any provided source.

**M9 Brand = 0. PEER DATA NEEDED.** Gross-margin proxy used per the
prompt's stated option: GM = (Revenue − Raw Material Cost)/Revenue =
45.08% (FY17) declining to 25.96% (FY26) (screener Data_Sheet CSV) — no
peer median available to benchmark against, so unscoreable beyond 0.

**M10 Switching Costs = 0.** Revenue did not grow every year and there is
no overall growth over the window (CAGR negative) → else band → 0.

**M11 Network Effects = 0.** Two-window test (10 years available, ≥6yr
requirement met): latest-3yr CAGR (FY23→FY26) = -3.53% vs prior-3yr CAGR
(FY20→FY23) = -9.65%. Latest is numerically greater (less negative) than
prior, but both are contractions, not growth — the top band (score 5)
also requires confirming "selling exp % declining," which cannot be
verified because FY26 "Selling and admin" is blank in the screener
Data_Sheet CSV (data gap). Scored 0: this is a shrinking business with a
slower rate of shrinkage, not network-effect growth, and the required
supporting data point is missing regardless.

**M12 Negative WC / Float = 0.** Payable Days is NOT FOUND (see Block B),
so exact WC Days cannot be computed, but Receivable Days + Inventory Days
alone range 213-413 days every single year in the decade (table in Block
B) — directionally conclusive that WC Days is far above the 45-day
ceiling even before any payables offset. Scored 0 on this partial-but-
conclusive basis.

**Moat score = 0 / 60. Moats confirmed (score ≥3): 0.**

Moat profile:
```
M1  Pricing Power       [          ] 0/5
M2  Cost Advantage      [          ] 0/5  PEER DATA NEEDED
M3  Capital Efficiency  [          ] 0/5
M4  Customer Stickiness [          ] 0/5
M5  Scale & Dominance   [          ] 0/5  PEER DATA NEEDED
M6  Technology / R&D    [          ] 0/5
M7  Regulatory/License  [          ] 0/5  PEER DATA NEEDED
M8  Distribution        [          ] 0/5
M9  Brand               [          ] 0/5  PEER DATA NEEDED
M10 Switching Costs     [          ] 0/5
M11 Network Effects     [          ] 0/5
M12 Negative WC / Float [          ] 0/5
```

**Moat classification: 0 present → NONE**

---

## CLASSIFICATION

Data confidence: 10 years (FY17-FY26) → **10+ yrs, full confidence.** No
history-based downgrade.

Grand total = Core (7) + Moat (0) = **7 / 160**

Classification matrix: Core <40 → **AVOID** (automatic, independent of
moat classification).

Deal-breaker overrides confirmed and consistent with (but individually
weaker than) the Core<40 floor:
- DB1: Block A (0) < 8 → max GOOD
- DB2: Block B (1) < 8 → max GOOD
- DB3: median ROCE 6.93% < 10% → max AVERAGE
- DB7: revenue declined in 6 of 9 years (majority) → max AVERAGE
- DB4 (cumul CFO/PAT <0.50): **not triggered** (0.598 ≥ 0.50)
- DB8 (PAT negative in any of last 3 years): **not triggered** (FY24
  66.16cr, FY25 14.39cr, FY26 11.13cr all positive)
- DB9 (history <3 years): **not triggered** (10 years available)
- DB5 (pledge >15%): **cannot be evaluated**, pledge % NOT FOUND
- DB6 (ND/EBITDA>3x AND IC<3x → AVOID): **not triggered**, but a
  razor-thin near-miss — ND/EBITDA 3.00x clears its trigger, IC 3.03x
  narrowly does not clear its <3x trigger.

Since the Core<40 rule already forces AVOID, the deal-breaker caps (which
would separately have capped at AVERAGE) are superseded — but they are
recorded because they corroborate the same underlying weakness (return
profile, cash quality, and revenue trajectory) from a different angle,
and DB6 is close enough to an explicit trigger to be operationally
relevant.

**CLASSIFICATION: AVOID**

---

## DECISION LINE

KCPSUGIND scores 7/100 on Core and 0/60 on Moat (grand total 7/160,
classification AVOID) on a full 10-year window (FY17-FY26, screener
Data_Sheet CSV). The company is a cyclical sugar / distillery / engineering
agri-processor whose revenue has contracted from 442.17cr (FY17) to
259.95cr (FY26), a -5.73% CAGR, with declines in 6 of the last 9 years;
PAT CAGR is -16.62% over the same window; median ROCE (6.93%) and median
ROE (4.86%) both sit well under cost-of-capital-adequate thresholds; and
FY26 cash flow from operations turned negative (-30.89cr) for the first
time since FY19, reversing three prior years of positive CFO. Leverage
itself is not extreme (D/E 0.28x) but coverage is thin and borderline on
two separate deal-breaker legs simultaneously (ND/EBITDA 3.00x, Interest
Coverage 3.03x). No moat evidence was confirmed on any of the 12
quantitative tests, though four of the twelve (M2, M5, M7, M9) could not
be properly tested at all for lack of any peer data in the input set.
Blocks D4 and E are materially incomplete due to a mechanical PDF-reading
failure in this environment (not a company-quality finding) and this
scorecard should be revisited once that tooling gap is fixed; the
Core<40 AVOID classification is unlikely to be reversed by that missing
data (Blocks A, B, C are complete and are what drive the score), but
Block E in particular is currently an unscored blank rather than a
verified negative.

---

```yaml
stage: B01-gate0
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-sonnet-5
status: complete
input_gaps:
  - "AR FY24-25 PDF (275pp) unreadable: exceeds 20MB single-file read limit and pdftoppm/poppler-utils not installed for page-range rendering (mechanical tool failure) — promoter holding, pledge %, contingent liabilities, notes-level balance-sheet detail all NOT FOUND"
  - "FY26 audited results PDF unreadable: pdftoppm/poppler-utils not installed, page-range rendering errors, full-file read returns no extractable content — segment data, standalone/consolidated split beyond CSV, balance-sheet notes NOT FOUND"
  - "Q3 FY26 unaudited results PDF unreadable: same mechanical failure"
  - "CARE rating PR PDF unreadable: same mechanical failure — rating agency's own gearing/current-ratio/coverage figures and rating rationale NOT FOUND"
  - "screener-Balance_Sheet.csv and screener-Cash_Flow.csv are empty header-only templates (no data rows); superseded by screener-Data_Sheet.csv"
  - "Trade Payables not separately disclosed in screener Data_Sheet CSV (aggregated within 'Other Liabilities') — Payable Days and full WC Days (B4) NOT FOUND"
  - "Exact capex (purchase of PPE + intangibles per CF statement) not separately disclosed in screener Data_Sheet CSV (only aggregate 'Cash from Investing Activity', which also nets the Investments book) — FCF (B2, B3) NOT FOUND"
  - "Current Ratio components (Current Assets / Current Liabilities split) not disclosed in screener Data_Sheet CSV — D4 NOT FOUND"
  - "No shareholding-pattern export supplied (named gap in B00 restart inventory) — all of Block E NOT FOUND"
  - "No peer/sector comparison data supplied for any company — M2, M5, M7, M9 scored 0, marked PEER DATA NEEDED"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID; Core score 7/100 driven by median ROCE 6.93% (<10%), median ROE 4.86% (<12%), revenue CAGR -5.73% FY17-FY26, revenue declined in 6 of 9 YoY comparisons, PAT CAGR -16.62%. Historical depressor: cyclical sugar/agri-commodity pricing under government-regulated cane costs; FY26 revenue (259.95cr) is the lowest print in the 10-year window, ~41% below the FY17 peak (442.17cr)."}
  - {type: FLAG-CASH, reason: "block_b_trend deteriorating: CFO swung from +47.79cr (FY25) to -30.89cr (FY26), the first negative annual CFO since FY19 (screener Data_Sheet CSV); cumulative CFO/PAT of 0.598 sits just above the 0.50 deal-breaker floor, i.e. one weak year from tripping it."}
  - {type: FLAG-DATA-GAP, reason: "All four PDF source documents (FY26 audited results, Q3 FY26 unaudited results, CARE rating PR, FY24-25 Annual Report) were mechanically unreadable in this environment: pdftoppm/poppler-utils is not installed so page-range PDF rendering errors on every file, and the Annual Report additionally exceeds the 20MB whole-file read ceiling. Block E is entirely NOT FOUND, D4 is NOT FOUND, B2/B3/B4 are partially NOT FOUND. This is a tooling failure, not a company-quality signal — flag for re-run with working PDF extraction before Blocks D-E are treated as final."}
  - {type: FLAG-DEALBREAKER-NEARMISS, reason: "Deal-breaker 6 (ND/EBITDA>3x AND IC<3x -> AVOID) narrowly not triggered: FY26 Net Debt/EBITDA = 3.00x (clears the >3x leg) while Interest Coverage = 3.03x (just above the <3x trigger, so this leg does not fire). Both metrics sit at the boundary; a small negative revision to FY26 EBITDA or interest would flip this to an explicit deal-breaker AVOID."}
data_years: 10
fy_range: "FY17 to FY26"
blocks: {A: 0, B: 1, C: 0, D: 6, E: 0}
core_score: 7
moat_score: 0
grand_total: 7
moats_confirmed: 0
moat_class: "NONE"
classification: "AVOID"
deal_breakers:
  - "DB1: Block A score 0 < 8 -> max GOOD (superseded by Core<40 floor)"
  - "DB2: Block B score 1 < 8 -> max GOOD (superseded by Core<40 floor)"
  - "DB3: median ROCE 6.93% < 10% -> max AVERAGE (superseded by Core<40 floor)"
  - "DB7: revenue declined in 6 of 9 years (majority) -> max AVERAGE (superseded by Core<40 floor)"
  - "DB5: promoter pledge >15% could not be evaluated -> pledge % NOT FOUND, not scored as triggered"
history_downgrade: false
data_notes:
  - "EBIT computed as PBT + Interest (screener Data_Sheet CSV carries no ROCE/ROE rows in this export); includes Other Income since no clean operating-only EBIT breakup is available, especially for FY26 where three expense sub-lines (Power & Fuel, Other Mfr. Exp., Selling and admin) are blank in the CSV."
  - "Capital Employed computed as Net Worth + Borrowings (Total Assets minus the unsplit 'Other Liabilities' aggregate) since the CSV provides no current/non-current liability split — stated as computed proxy per the fixed-formula rule."
  - "ROE FY17 uses closing Net Worth only (no FY16 opening figure in the provided 10-year window), per formula rule."
  - "Inventory Days computed on Revenue basis, not COGS — Raw Material Cost in the CSV is only a partial COGS component, not full COGS."
  - "PAT dipped negative in FY20 (-6.26cr) inside the FY17-FY26 CAGR window; both window endpoints (FY17 +57.17cr, FY26 +11.13cr) are positive, so this is not scored as a loss-to-profit swing per the CAGR edge rule, but is noted for context."
  - "M9 Brand test used Gross Margin proxy = (Revenue - Raw Material Cost)/Revenue per the prompt's stated proxy option; declined from 45.08% (FY17) to 25.96% (FY26); unscoreable beyond 0 with no peer median available."
  - "M2, M5, M7, M9 scored 0 and marked PEER DATA NEEDED — no peer/sector comparison data was provided in any input source."
  - "M12 scored using Receivable Days + Inventory Days only (213-413 days every year in the window) since Payable Days is NOT FOUND; directionally conclusive (far above the 45-day ceiling) even without a payables offset."
  - "FY26 annual P&L cross-validated internally: the four FY26 quarterly columns in the screener Data_Sheet CSV sum to the FY26 annual column (Sales 259.95cr both ways; PAT 11.12 vs 11.13cr, rounding), partially offsetting the inability to read the FY26 audited results PDF directly."
block_b_trend: "deteriorating — CFO fell from +47.79cr (FY25) to -30.89cr (FY26), first negative annual CFO print since FY19 (screener Data_Sheet CSV, Cash from Operating Activity row)"
```
