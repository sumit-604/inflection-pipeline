# GATE 0 SCORECARD — Virtuoso Optoelectronics Ltd (VOEPL)
Run date: 2026-07-18 | Stage: B01-gate0 | Model: claude-sonnet-5

Data available: 3 years (FY24 to FY26). Scoring adapted to 3-year history.

RE-RUN NOTE: the prior run of this stage could not read the PDFs because
the Read tool's PDF renderer (pdftoppm/poppler) was broken in that
environment — a mechanical/environment failure, not a data gap. This run
uses deterministic, page-marked TEXT EXTRACTS of every PDF, which are
authoritative for this run. All figures below are drawn from those
extracts plus the screener CSV and the operator-supplied shareholding
series. Nothing here is estimated; genuine gaps are marked NOT FOUND.

Sources used (anchor labels used below in parentheses):
- (screener-data) = `runs/voepl-2026-07-18/inputs/screening/screener-Data_Sheet.csv`
  (populated P&L/BS/CF FY24-FY26 + FY25-FY26 quarters). PRIMARY for
  revenue, PAT, receivables, inventory, CFO, borrowings, equity, cash. The
  other five screener CSVs in that folder are empty templates and were not
  used.
- (results Q4 FY26, p.N) = `runs/voepl-2026-07-18/extracted/results/3c69ed09-3088-45bf-bbae-01362ea7aea7.txt`
  (board outcome + audited standalone cash flow statement, FY26 vs FY25
  columns, filed 29-May-2026, 24 pages). Balance sheet pages (5-10,
  12-24) did not extract as text in the source PDF (image-only) — content
  genuinely unavailable, not read.
- (results Q3 FY26, p.N) = `runs/voepl-2026-07-18/extracted/results/7fc85d5c-6e2d-4706-b7c7-7b38871dea7a.txt`
  (limited review report only, Dec-2025 quarter, 12 pages; no P&L/BS
  figures extracted — pages 4-6, 10-12 image-only in source).
- (AR p.N) = `runs/voepl-2026-07-18/extracted/annual-report/6ff4905d-7e49-4d3d-a6ee-39f6acb8886a.txt`
  (Annual Report 2025, standalone + consolidated financials for FY24 and
  FY25, 92 pages; balance sheet, P&L, cash flow, Notes, CARO, MD&A ratios).
- (operator SHP) = `runs/voepl-2026-07-18/inputs/shareholding/OPERATOR-SUPPLIED-shareholding-screener-screenshot.md`
  (screener.in Shareholding Pattern screenshot, quarterly, Sep-2022 to
  Jul-2026; treated as ANCHORED-equivalent per orchestrator instruction).

DATA GAP CARRIED FORWARD: the Q4 FY26 results filing's balance sheet
section did not extract as text (image-only pages in that PDF). FY26 Total
Assets split, Total Current Liabilities and Trade Payables are therefore
NOT FOUND in any provided source (the AR only covers FY24-FY25; no FY26
Annual Report exists yet). This blocks FY26 ROCE (computed formula), FY26
Current Ratio, and FY26 Payable Days / full WC Days. Marked NOT FOUND
throughout, never estimated; metrics computed on the best complete pair
(FY24-FY25) are flagged as such below.

FY26 capex was reconstructed from the results PDF's OCR-garbled cash flow
table (numbers and labels partially decoupled by the extractor) by
column-order alignment: the standard Ind AS cash flow statement item order
(23 CFO line items, 6 CFI line items, 9 CFF line items, 3 cash-reconciliation
lines) was matched against the raw numeric sequence for the FY26 column,
then cross-validated against the FY25 comparative column in the same
table. That FY25 reconstruction reproduces the AR's audited FY25 cash flow
line items exactly: Trade Receivables change -923.15, Inventories -4,770.37,
Trade Payables +3,313.90, Capex -12,230.88, Proceeds from Share Warrants
+6,026.74, ICD to subsidiary -880.46, closing cash 209.33 (all Lakhs, all
match AR p.55-56 to two decimals). This validates the ordering method used
for the FY26 column.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 9/20

| Metric | FY24 | FY25 | FY26 |
|---|---|---|---|
| ROCE (%) | 25.66 (AR p.36, MD&A "Key Financial Ratios" table, company-disclosed, standalone) | 17.19 (AR p.36, same table) | NOT FOUND — requires FY26 Current Liabilities, unavailable (balance sheet pages did not extract in the FY26 results filing) |
| ROE (%) | 4.85 (computed: PAT 10.17 (screener-data) ÷ closing Net Worth 209.58 (screener-data, ShareCap 26.34+Reserves 183.24); opening FY24 net worth unavailable, closing used and so stated) | 5.74 (computed: PAT 14.09 (screener-data) ÷ avg NW [209.58, 281.81] (screener-data)) | 4.33 (computed: PAT 15.03 (screener-data) ÷ avg NW [281.81, 412.22] (screener-data)) |

A1 Median ROCE: only 2 of 3 years computable (FY26 NOT FOUND). Median of
(25.66%, 17.19%) = 21.43% → 20-24.9% band → **Score 4**. Flagged: this is
a 2-of-3-year sample, not the full 3-year median the framework specifies.

A2 Minimum single-year ROCE (of the available years): 17.19% (FY25) →
≥15% → **Score 5**. Caveat: FY26 — the year with the highest leverage and
weakest cash conversion (see Blocks B and D) — is excluded because it is
NOT FOUND; the true 3-year minimum could be materially lower.

A4 ROCE trend, latest vs earliest: using the best available window (FY25
vs FY24, since FY26 is NOT FOUND): 17.19% − 25.66% = −8.47pp → decline
>5pp → **Score 0**. Flagged: "latest" here is FY25, not the true FY26,
due to the data gap.

A3 Median ROE: all 3 years computable (equity is available for all years;
this metric does not need the current-liabilities split). Values sorted:
4.33%, 4.85%, 5.74% → median 4.85% → <12% → **Score 0**.

**Block A = 4+5+0+0 = 9 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 8/20

| Metric | FY24 | FY25 | FY26 |
|---|---|---|---|
| CFO (Cr) | 13.75 (screener-data) | 30.60 (screener-data) | 3.33 (screener-data) |
| PAT (Cr) | 10.17 (screener-data) | 14.09 (screener-data) | 15.03 (screener-data) |
| CFO/PAT | 1.35x | 2.17x | 0.22x |
| Capex (Cr) | 60.84 (AR p.55-56, standalone Cash Flow Statement, "Investments in Property, Plant & Equipment" 6,083.84 Lakhs) | 122.31 (AR p.55-56, standalone CF, "Investments in Property, Plant & Equipment" 12,230.88 Lakhs) | 143.24 (results Q4 FY26 p.11, standalone CF, "Investments in Property, Plant & Equipments" 14,324.11 Lakhs — column-order reconstruction, cross-validated per method note above) |
| FCF = CFO − Capex (Cr) | −47.09 | −91.71 | −139.91 |

B1 Cumulative CFO ÷ Cumulative PAT: (13.75+30.60+3.33) ÷ (10.17+14.09+
15.03) = 47.68 ÷ 39.29 = **1.21x** → ≥1.00 → **Score 5**. This cumulative
figure masks a real within-period collapse — see block_b_trend below.

B2 FCF-positive years: 0 of 3 (every year negative — heavy capex
expansion) → **Score 0**.

B3 Cumulative FCF ÷ Cumulative PAT: (−47.09−91.71−139.91) ÷ 39.29 =
−278.71 ÷ 39.29 = **−7.09x** → negative → **Score 0**.

B4 Change in WC Days, latest vs earliest: FY26 Trade Payables is NOT
FOUND, so full FY26 WC Days cannot be computed. Scored on the best
complete pair, FY25 vs FY24:
- Receivable Days = Trade Receivables ÷ Revenue × 365 (revenue basis used
  — no explicit COGS line in screener-data, so stated). FY24: 21.31
  (screener-data) ÷ 531.06 (screener-data) × 365 = 14.65 days. FY25: 30.58
  ÷ 697.32 × 365 = 16.01 days. FY26 (receivables-only, for color): 72.22
  (screener-data) ÷ 823.6 (screener-data) × 365 = 32.01 days.
- Inventory Days (revenue basis, stated): FY24: 164.76 (screener-data) ÷
  531.06 × 365 = 113.24 days. FY25: 213.08 ÷ 697.32 × 365 = 111.55 days.
  FY26: 227.39 ÷ 823.6 × 365 = 100.79 days.
- Payable Days (revenue basis): FY24: Trade Payables 98.25 Cr (AR p.~65,
  Note 10: MSME dues 245.00 + Other creditor dues 9,579.69 = 9,824.69
  Lakhs) ÷ 531.06 × 365 = 67.55 days. FY25: Trade Payables 131.39 Cr (AR
  Note 10: MSME 772.60 + Others 12,366.00 = 13,138.60 Lakhs) ÷ 697.32 ×
  365 = 68.78 days. FY26: **NOT FOUND** — no Trade Payables figure in any
  provided FY26 source.
- WC Days FY24 = 14.65+113.24−67.55 = 60.34 days. WC Days FY25 =
  16.01+111.55−68.78 = 58.78 days. Change FY25 vs FY24 = −1.57 days →
  within ±5 days → **Score 3**.
- Color only, not scored: FY26 Receivable Days alone more than doubled
  (14.65→32.01 days, FY24→FY26) while Inventory Days improved slightly.
  If Payable Days held roughly flat at ~68 days, full WC Days would rise
  materially in FY26 — directionally consistent with the FY26
  cash-conversion collapse below, but Payable Days FY26 is NOT FOUND so
  this is not scored.

**Block B = 5+0+0+3 = 8 / 20**

**block_b_trend: deteriorating** — CFO/PAT fell from ~2.17x (FY25) to
~0.22x (FY26) (screener-data, CFO and PAT rows), even as PAT kept growing.
This is the genuine FY26 cash-conversion collapse; it is not masked by the
cumulative B1 score of 5, which is a 3-year aggregate.

---

## BLOCK C: GROWTH (Max 20) — Score: 18/20

Revenue CAGR (FY24→FY26, 2yr): (823.6÷531.06)^(1/2)−1 = **24.54%** —
computed (screener-data).
PAT CAGR (FY24→FY26, 2yr): (15.03÷10.17)^(1/2)−1 = **21.57%** — computed
(screener-data).

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| C1 | Revenue CAGR | 24.54% | ≥20% | 5 |
| C2 | PAT CAGR | 21.57% | ≥20% | 5 |
| C3 | Positive YoY revenue years | 2/2 (100%) — FY25>FY24, FY26>FY25 (screener-data) | 100% | 5 |
| C4 | PAT CAGR − Revenue CAGR | 21.57−24.54 = −2.97pp | ±3pp | 3 |

**Block C = 18 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 4/20

| Metric | FY24 | FY25 | FY26 |
|---|---|---|---|
| EBIT = PBT+Interest (Cr) | 34.47 | 50.53 | 57.98 |
| EBITDA = EBIT+Depn (Cr) | 52.77 | 60.80 | 85.89 |
| Net Debt = Borrowings−Cash (Cr) | 134.88 | 169.14 | 343.55 |
| Net Debt/EBITDA | 2.56x | 2.78x | **4.00x** |
| Interest Coverage EBIT/Interest | 1.71x | 1.99x | **1.73x** |
| Debt/Equity = Borrowings/(ShareCap+Reserves) | 0.64 | 0.61 | **0.84** |
| Current Ratio | 1.23 (AR p.36, MD&A, company-disclosed) | 1.31 (AR p.36) | NOT FOUND |

All P&L/BS inputs (screener-data). All ratios "computed" per formula
definitions (this screener export has no native ROCE/ratio block).

D1 Net Debt/EBITDA (latest, FY26) = 4.00x → >3x → **Score 0**.
D2 Interest Coverage (latest, FY26) = 1.73x → 1.5-2.9x band → **Score 1**.
D3 Debt/Equity (latest, FY26) = 0.84 → 0.5-1.0 band → **Score 3**. Note:
AR's own MD&A-disclosed Debt-Equity Ratio is 0.61 (FY25) / 0.94 (FY24) —
differs from the figure computed here (0.61 FY25 matches; 0.64 vs 0.94 FY24
does not), likely because AR nets or classifies debt/equity differently
(e.g. share-warrant treatment); AR does not show its own formula so this
is not reconciled, only noted as a data_note.
D4 Current Ratio (latest, FY26) = **NOT FOUND** (no FY26 balance sheet
split available) → **Score 0** per "N/A → score 0" rule.

**Block D = 0+1+3+0 = 4 / 20**

**Deal-breaker #6 triggered: Net Debt/EBITDA >3x (4.00x) AND Interest
Coverage <3x (1.73x), both FY26 → AVOID.** Driving year: FY26 only. FY24
(2.56x / 1.71x) and FY25 (2.78x / 1.99x) do not independently trigger this
rule. The deterioration is concentrated in the FY26 expansion year, which
saw capex of Rs143.24 Cr (see Block B) funded substantially by fresh
borrowings (Borrowings 171.5→344.56 Cr, screener-data) alongside fresh
equity/warrant proceeds (results Q4 FY26 CF, FY26 column: Proceeds from
share capital 10,666.67 Lakhs, Proceeds from Share Warrants 833.33 Lakhs).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 6/20

Source: operator-supplied screener.in Shareholding Pattern screenshot
(operator SHP), quarterly series Sep-2022 to Jul-2026, treated as
ANCHORED-equivalent per orchestrator instruction.

E1 Promoter holding (latest, Jul-2026) = 49.74% (operator SHP) → 40-49.9%
band → **Score 3**.

E2 Promoter holding change over ~3 years: latest 49.74% (Jul-2026,
operator SHP) vs. ~3-years-prior 65.60% (Mar-2023 and Sep-2023, both
65.60%, operator SHP — closest available quarters to the Jul-2023 3-year
mark) = −15.86pp → decreased >3% → **Score 0**. Per orchestrator context
(not pre-judged here): whether this decline is a promoter sell-down or
dilution via fresh primary issuance is left for stage 8 to adjudicate
against filings; scored mechanically here on the raw percentage change
only.

E3 Promoter pledge (latest): **NOT FOUND** — the operator SHP source
carries no pledge row; not present in any other provided source →
**Score 0** per "N/A → 0" rule. Deal-breaker #5 (pledge >15% → max
AVERAGE) is NOT invoked since pledge level is unconfirmed, not assumed.

E4 Contingent Liabilities ÷ Net Worth (latest available: FY25 — no FY26
Annual Report exists yet): Contingent liabilities = Custom Duty Payable
under EPCG Scheme 624.41 Lakhs = 6.24 Cr (AR p.68-69, Note 30: "Other
Disclosures"; TDS Outstanding Demand NIL, Corporate Guarantees NIL) PLUS
GST dispute 14.38 Cr (AR p.51, CARO Annexure A, disputed statutory dues
table: statute "Goods and Service Tax Act, 2017", forum "Goods and
Service Tax Commissioner of Appeals", period 2017-18, amount Rs.14.38 Cr —
this is disclosed in the CARO annexure, not in Note 30, and both are
captured here per orchestrator instruction). Total = 6.24+14.38 = 20.62
Cr. Net Worth FY25 = 281.81 Cr (screener-data, ShareCap 29.49+Reserves
252.32). Ratio = 20.62÷281.81 = **7.32%** → 5-15% band → **Score 3**.

**Block E = 3+0+0+3 = 6 / 20**

---

## CORE SCORE

A (9) + B (8) + C (18) + D (4) + E (6) = **45 / 100**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 10/60

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 3 | EBITDA margin FY24 9.94% → FY26 10.43% (computed, screener-data), +0.49pp (stable ±2pp) AND revenue CAGR 24.54% ≥10% → "margin stable and growth" tier |
| M2 | Cost Advantage vs peer median | 0 | PEER DATA NEEDED — no peer (AMBER/ELIN/EPACK/PGEL) EBITDA margin data provided this run |
| M3 | Capital Efficiency | 3 | FAT (Fixed Asset Turnover = Revenue÷Net Block, screener-data) FY25 = 697.32÷208.55 = 3.34x >2x, AND ROCE FY25 17.19% (AR p.36) >15% → tested on FY25 (latest complete year) since FY26 ROCE is NOT FOUND; flagged |
| M4 | Customer Stickiness | 3 | Zero revenue-decline years (screener-data) but Receivable Days rose 14.65→32.01 days (FY24→FY26), so the top tier's "stable ±10" clause fails; scored on the "max 1 decline year, fully recovered" tier (0 decline years trivially satisfies ≤1). Caveat: the underlying stickiness signal is undermined by the receivables deterioration, noted not scored twice |
| M5 | Scale & Dominance | 0 | PEER DATA NEEDED — no peer mcap/margin ranking data provided |
| M6 | Technology / R&D | 0 | R&D spend Rs8.34 Cr disclosed (AR p.31, Directors' Report, single year only) ÷ FY25 Revenue 697.32 = 1.20% ≥1%, but that tier also requires "margin above peer median" — PEER DATA NEEDED, unconfirmable; scored 0 |
| M7 | Regulatory / License | 0 | EMS/ODM consumer-electronics contract manufacturing (room-AC ODM, PCBA, compressors) is not a licensed/limited-player regulated segment per the test definition; unregulated → 0 |
| M8 | Distribution | 0 | VOEPL is a B2B OEM/ODM contract manufacturer (AR p.29-32 MD&A) selling to other brands, not a consumer-distribution business; no reach/network figures disclosed in any provided source |
| M9 | Brand | 0 | PEER DATA NEEDED — GM proxy [(Revenue−Material Cost)÷Revenue] is computable but no peer GM figure is available to compare against |
| M10 | Switching Costs | 0 | Revenue grew every year (screener-data), but Receivable Days rose 17.36 days FY24→FY26 (>10-day threshold) — top tier fails; no decline years exist to qualify for the middle/bottom tiers as worded → scored 0 (else) |
| M11 | Network Effects | 1 | Only 3 years available (<6 needed for the two-window test) — scored conservatively per instruction, and so stated. Revenue CAGR 24.54%>15%, but Selling & Admin expense as % of sales rose FY24 1.65%→FY25 2.31% (screener-data; FY26 not separately disclosed in screener-data, bundled into "Other Expenses") — rising, not declining → "growth>15% but selling% rising" tier |
| M12 | Negative WC / Float | 0 | WC Days FY24 60.34, FY25 58.78 (both >45 days); FY26 Receivable+Inventory Days alone already total 132.80 days (Payable Days NOT FOUND but immaterial to the >45 conclusion) → 0 |

Moats "present" (score ≥3): M1, M3, M4 = **3 moats present**.

Moat profile:
```
M1  [███░░] 3/5  present
M2  [░░░░░] 0/5
M3  [███░░] 3/5  present
M4  [███░░] 3/5  present
M5  [░░░░░] 0/5
M6  [░░░░░] 0/5
M7  [░░░░░] 0/5
M8  [░░░░░] 0/5
M9  [░░░░░] 0/5
M10 [░░░░░] 0/5
M11 [█░░░░] 1/5
M12 [░░░░░] 0/5
```

**Moat score = 3+0+3+3+0+0+0+0+0+0+1+0 = 10 / 60. Classification: 3
present → MODERATE.**

---

## GRAND TOTAL

Core Score (45) + Moat Score (10) = **55 / 160**

---

## DEAL-BREAKER OVERRIDES

| # | Rule | Triggered? | Detail |
|---|---|---|---|
| 1 | Block A <8 → max GOOD | NO | Block A = 9 |
| 2 | Block B <8 → max GOOD | NO | Block B = 8, exactly at the boundary — noted, not breached |
| 3 | Median ROCE <10% → max AVERAGE | NO | Median 21.43% (2-year sample, FY26 excluded — NOT FOUND) |
| 4 | Cumulative CFO/PAT <0.50 → max AVERAGE | NO | 1.21x |
| 5 | Pledge >15% → max AVERAGE | NO | Pledge NOT FOUND; not assumed, not triggered |
| 6 | ND/EBITDA >3x AND IC <3x → AVOID | **YES** | 4.00x AND 1.73x, both FY26 |
| 7 | Revenue declined majority of years → max AVERAGE | NO | 0 of 2 YoY periods declined |
| 8 | PAT negative in any of last 3 years → max AVERAGE | NO | PAT positive all 3 years |
| 9 | History <3 years → AVERAGE | NO | Exactly 3 years available (see Data Confidence below for the separate LIMITED-tier downgrade) |

---

## DATA CONFIDENCE / HISTORY

3 years of data (FY24-FY26) falls in the **3-4 LIMITED** tier per the
data-confidence rule → classification downgrade one tier applies
mechanically. History is short because VOEPL SME-listed c.2022 and the
DRHP-restated pre-FY24 financials were not collected into this run's
screener export (screener-data carries only FY24-FY26). This is a
legitimate mechanical downgrade (`history_downgrade: true`), kept
separate from the SME→mainboard ramp/recovery narrative, which is
qualitative color only and is not conflated with this boolean.

---

## CLASSIFICATION

Classification matrix: Core 45 falls in the 40-59 band → **AVERAGE**
(pre-downgrade, pre-deal-breaker; this band is not further conditioned on
moat class per the matrix).

Applying the LIMITED history downgrade (one tier down): AVERAGE → **AVOID**.

Applying deal-breaker #6 independently (ND/EBITDA 4.00x AND Interest
Coverage 1.73x, both FY26) → **AVOID**.

Both mechanisms converge on the same result.

**FINAL CLASSIFICATION: AVOID**

---

## STRONGEST / WEAKEST BLOCK

Strongest: **Block C, Growth (18/20)** — revenue CAGR 24.54%, PAT CAGR
21.57%, 100% positive YoY revenue years, all screener-data anchored.

Weakest: **Block D, Balance Sheet Strength (4/20)** — FY26 Net
Debt/EBITDA 4.00x, Interest Coverage 1.73x, Current Ratio NOT FOUND. This
is also the block carrying the outright deal-breaker.

---

## DECISION LINE

Gate 0 classification: **AVOID** (Core 45/100 = AVERAGE band, downgraded
one tier by the LIMITED 3-year history tier; independently confirmed by
deal-breaker #6, Net Debt/EBITDA 4.00x AND Interest Coverage 1.73x, both
FY26). Per pipeline rules this does not halt the run — there is no STOP
verdict in this pipeline and company quality never halts. It is recorded
here as a mechanical scorecard output that propagates forward as evidence
(FLAG-GATE0) for stage 8 and downstream synthesis to weigh alongside the
genuine FY26 cash-conversion collapse (CFO/PAT ~2.17x FY25 → ~0.22x FY26)
and the capex-driven capacity expansion (Rs143.24 Cr in FY26 alone, likely
the compressor-plant and EMS/PCBA buildout referenced in company
disclosures) that is driving both the leverage spike and the negative FCF
across all 3 years. The growth profile (Block C, 18/20) and the moat
signal (3 present, MODERATE class) are genuinely strong; the deal-breaker
and the history-length downgrade are both concentrated in FY26 and in the
short listing history, not in a structural growth or demand problem. Low
institutional ownership is explicitly not treated as a risk factor here
(FII+DII combined ~12.1% per operator SHP, entering not absent — FII rose
0.00%→11.29% over the series, most of the step-up recent) — this did not
affect any Block E score, which was driven by promoter percentage bands
and the pledge data gap only, consistent with CLAUDE.md Amendment 3.

---

## INPUT GAPS (for downstream stages)

1. FY26 balance sheet (Total Assets split, Current Liabilities, Trade
   Payables) — NOT FOUND. The results filing's balance sheet pages did
   not extract as text (image-only in the source PDF). Blocks FY26 ROCE,
   FY26 Current Ratio, FY26 Payable Days / full WC Days.
2. Promoter pledge % — NOT FOUND in the operator SHP source (no pledge
   row) or any other provided source.
3. Peer financial data (AMBER/ELIN/EPACK/PGEL) — not provided this run.
   Blocks M2, M5, M9, and the higher tiers of M6.
4. Pre-FY24 (pre-restatement / DRHP) financials — not collected this run;
   history capped at 3 years (FY24-FY26).
5. FY26 contingent liabilities / updated Note 30 — no FY26 Annual Report
   exists yet; E4 uses the latest available disclosure (FY25 AR + CARO),
   explicitly noted as such.

---

```yaml
stage: B01-gate0
company: "VOEPL"
run_date: "2026-07-18"
model: claude-sonnet-5
status: complete
input_gaps:
  - "FY26 balance sheet (Total Assets split, Current Liabilities, Trade Payables) NOT FOUND - Q4 FY26 results filing balance sheet pages did not extract as text (image-only); blocks FY26 ROCE, FY26 Current Ratio, FY26 Payable Days / full WC Days"
  - "Promoter pledge % NOT FOUND - operator SHP source carries no pledge row; not present in any other provided source"
  - "Peer financials (AMBER/ELIN/EPACK/PGEL) not provided this run - blocks M2, M5, M9, and higher tiers of M6"
  - "Pre-FY24 (pre-restatement/DRHP) financials not collected this run - history capped at 3 years (FY24-FY26)"
  - "FY26 contingent liabilities / updated Note 30 not available - no FY26 Annual Report exists yet; E4 uses latest available (FY25 AR + CARO)"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID (core 45/100 = AVERAGE band, downgraded one tier by LIMITED 3-year history; independently confirmed by deal-breaker 6: ND/EBITDA 4.00x AND Interest Coverage 1.73x, both FY26). Driving year is FY26 only - FY24 (2.56x/1.71x) and FY25 (2.78x/1.99x) do not independently trigger the leverage/coverage deal-breaker; deterioration concentrated in FY26's Rs143.24 Cr capex year funded by fresh borrowings and equity/warrant proceeds. Concurrent FY26 cash-conversion collapse: CFO/PAT 2.17x (FY25) -> 0.22x (FY26), screener-data. Growth strong (Rev CAGR 24.54%, PAT CAGR 21.57%, both FY24-FY26) and 3 moat tests present (Pricing Power, Capital Efficiency, Customer Stickiness - MODERATE class). Flags propagate; no STOP verdict, decision stays human per pipeline rules."}
data_years: 3
fy_range: "FY24 to FY26"
blocks: {A: 9, B: 8, C: 18, D: 4, E: 6}
core_score: 45
moat_score: 10
grand_total: 55
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers: ["6: ND/EBITDA 4.00x AND Interest Coverage 1.73x (both FY26) -> AVOID"]
history_downgrade: true
data_notes:
  - "FY26 capex (Rs143.24 Cr) reconstructed from OCR-garbled results-PDF cash flow table via column-order alignment; cross-validated against AR audited FY25 cash flow line items in the same table's comparative column (Trade Receivables -923.15, Inventories -4,770.37, Trade Payables +3,313.90, Capex -12,230.88, Share Warrants +6,026.74, ICD to subsidiary -880.46, closing cash 209.33, all Lakhs - all match AR p.55-56 exactly)"
  - "A1/A2/A4 (ROCE median/min/trend) computed on FY24-FY25 only (2 of 3 years) - FY26 ROCE NOT FOUND due to missing Current Liabilities; true 3-year figures may differ, especially the minimum and the trend"
  - "B4 (WC Days change) scored on FY25-vs-FY24, not FY26-vs-FY24, because FY26 Payable Days is NOT FOUND; FY26 Receivable Days alone more than doubled (14.65->32.01 days) - directional color only, not scored"
  - "D3 (Debt/Equity) computed as Borrowings/(ShareCap+Reserves) from screener-data; differs from AR's own MD&A-disclosed Debt-Equity Ratio (0.61 FY25 matches; 0.94 FY24 does not match computed 0.64) - AR formula not disclosed, not reconciled"
  - "M3 tested on FY25 (latest complete year), not FY26, since FY26 ROCE is NOT FOUND"
  - "ROE FY24 uses closing Net Worth only (no FY23 opening figure available), per formula rule, and so stated"
  - "E4 contingent liabilities combines AR Note 30 (Custom Duty EPCG 6.24 Cr) with the CARO Annexure A disputed-dues table (GST dispute 14.38 Cr, FY2017-18, at GST Commissioner of Appeals) - the CARO figure is not in Note 30 and both are captured per orchestrator instruction"
  - "M6 R&D/Revenue ~1.20% is a single-year figure (FY25 only, AR Directors' Report) - 'consistently' higher tiers not assessable"
  - "M11 scored conservatively per instruction: only 3 years available vs 6 required for the two-window test"
  - "Deal-breaker 5 (pledge) not invoked - pledge % is NOT FOUND, not assumed >15%"
block_b_trend: "deteriorating - CFO/PAT fell from ~2.17x (FY25) to ~0.22x (FY26), screener-data CFO and PAT rows"
```
