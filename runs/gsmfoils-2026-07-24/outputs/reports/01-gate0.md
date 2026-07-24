# STAGE 1: GATE 0 SCORECARD — GSM Foils Ltd (GSMFOILS)
Run date: 2026-07-24 | Model: Sonnet 5 | Pipeline mode

Data available: 3 years (FY24 to FY26). Scoring adapted to 3-year history.
FY24 = year ended 31-Mar-2024, FY25 = year ended 31-Mar-2025, FY26 = year
ended 31-Mar-2026 (audited, BM 17-Apr-2026). A "31-Dec-2023" 9-month stub
also appears in the screener Data_Sheet; this is an interim disclosure
INSIDE FY24, not a fourth fiscal year (AR calls FY25 the company's "02nd
Annual Report," confirming FY24 is the first full FY) — excluded from all
CAGR/trend counts. Company listed (SME IPO) 31-May-2024; no prospectus in
inputs, so no pre-IPO restated years exist. Q1 FY27 (quarter ended
30-Jun-2026) is available as supplementary quarterly context only, not
scored into the annual blocks below.

Primary sources: screener Data_Sheet CSV (clean, machine-readable —
primary anchor for all P&L and aggregate balance-sheet lines), FY25
Annual Report (clean OCR, used for FY24/FY25 balance-sheet detail and
trade payables), Q4/FY26 results filing BM 17-Apr-2026 (badly
OCR-garbled scanned PDF — used only where digits could be cross-validated
against the clean Data_Sheet; flagged wherever used), Q1FY27 results
filing BM 18-Jul-2026 (cover letter text only; the financial-statement
pages did not OCR — no incremental figures extracted from it beyond what
the Data_Sheet's Jun-2026 quarterly column already carries), and the
operator-supplied screener shareholding screenshot (anchored-equivalent
per OPERATOR_CONTEXT.md, dated 2026-07-24).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formulas: ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed
(source does not carry ROCE). EBIT = PBT + Interest − Other Income
(computed from screener-data P&L lines). ROE = PAT ÷ average Net Worth.

| FY | EBIT (cr) | Capital Employed (cr) | ROCE | PAT (cr) | Avg Net Worth (cr) | ROE |
|----|-----------|------------------------|------|----------|---------------------|-----|
| FY24 | 2.60 (=1.86+0.74−0, screener-data) | 11.95 (AR p.82 Balance Sheet, Total Assets 19.97 − Current Liab 8.02) | 21.77% | 1.37 (screener-data) | 11.03 (closing only; opening N/W not in data, closing used and stated) | 12.42% |
| FY25 | 14.93 (=13.63+1.32−0.02, screener-data) | 31.26 (AR p.82, Total Assets 61.40 − Current Liab 30.14) | 47.77% | 9.65 (screener-data) | 21.14 (avg of 11.03 opening / 31.24 closing) | 45.66% |
| FY26 | 29.32 (=26.69+3.00−0.37, screener-data) | N/A precise figure — bounded 74.46–118.85 (see note) | bounded 24.67%–39.37% | 19.84 (screener-data) | 52.85 (avg of 31.24 opening / 74.46 closing) | 37.54% |

**FY26 Capital Employed bound**: Total Assets FY26 = 165.03cr (screener-data,
clean). Shareholders' funds FY26 = Equity 14.09 + Reserves 60.37 = 74.46cr
(screener-data, clean). By the accounting identity Total Assets = Equity +
Non-Current Liab + Current Liab, (NCL+CL) = 90.57cr — but the results
filing's FY26 balance sheet (p.6-7, BM 17-Apr-2026) is too OCR-corrupted
to reliably read the NCL/CL split, and the screener Data_Sheet does not
carry it either (input_gap). Bounding: if NCL≈0 (all borrowings
short-term, matching the company's actual FY24/FY25 pattern — AR shows
FY25 long-term borrowings = 0, 100% of borrowings short-term; FY24 was
89% short-term), Capital Employed = 74.46cr → ROCE 39.37%. If NCL were the
maximum conceivable (all Rs44.39cr of FY26 borrowings classified
long-term, an assumption with zero historical precedent at this company),
Capital Employed = 118.85cr → ROCE 24.67%. **Every point in this bound is
≥ FY24's clean 21.77%**, so A4 (trend) is scored robustly without needing
the exact figure. A1/A2 (median/minimum) are computed from the two clean
years only (see below) to avoid the FY24-FY26 3-value median flipping
bands under the bound's low end.

A1 Median ROCE (FY24+FY25, 2 clean years; FY26 excluded — bounded value
straddles the 25%/20% band edge, see above): median (of 2) = 34.77% →
**≥25% = 5**
A2 Minimum single-year ROCE: FY24 = 21.77% is the minimum whether or not
FY26 is included (FY26's bounded floor, 24.67%, still exceeds it) →
**≥15% = 5**
A3 Median ROE (3 clean years: 12.42%, 45.66%, 37.54%): median = 37.54% →
**≥20% = 5**
A4 ROCE trend, latest vs earliest: FY26 (bounded 24.67%–39.37%) vs FY24
(21.77%) — latest ≥ earliest holds at every point in the bound →
**latest≥earliest = 5**

**Block A = 20/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

| FY | CFO (cr) | Capex (cr) | FCF (cr) | PAT (cr) |
|----|----------|------------|----------|----------|
| FY24 | −13.72 (screener-data) | 0.97 (=CFO−CFI proxy; CFI FY24 −0.97cr screener-data, and non-current investments were nil that year so CFI ≈ capex) | −14.69 | 1.37 |
| FY25 | **N/A (not in provided data)** — screener Data_Sheet cell blank; Q4FY26 results filing p.8 cash-flow statement (BM 17-Apr-2026) is scanned/OCR-garbled and not used as a scored anchor. Non-scored cross-check: internal cash reconciliation of the same garbled page (closing cash 24.25cr − opening cash 39.54cr − CFI[−4.55] − CFF[22.09], all independently legible on that page) implies CFO FY25 ≈ −17.69cr — directionally consistent (also deeply negative) but NOT used in any score below. | 1.56 (computed: closing Net Block 2.12 − opening Net Block 0.84 + Depreciation 0.28, screener-data) | N/A (CFO unavailable) | 9.65 |
| FY26 | −36.79 (screener-data) | 3.43 (computed: 5.09−2.12+0.46, screener-data) | −40.22 | 19.84 |

B1 Cumulative CFO ÷ Cumulative PAT (FY24+FY26 only, the 2 years with
anchored CFO): ΣCFO = −50.51cr, ΣPAT = 21.21cr → ratio = **−2.38** →
**<0.50 = 0**
B2 FCF-positive years as proportion (FY24, FY26 — the 2 computable years):
0 of 2 positive → **<50% = 0**
B3 Cumulative FCF ÷ Cumulative PAT (FY24+FY26): ΣFCF = −54.91cr, ΣPAT =
21.21cr → ratio = **−2.59** → **<0.20 or negative = 0**
B4 Change in WC Days, latest (FY26) vs earliest (FY24) — see Working
Capital table below for the full derivation and the payables bound:
**increased >15 days = 0** (see note; this is the least-certain single
score in this run)

**Block B = 0/20 — DEAL-BREAKER TRIGGERED** (#2 Block B<8 → max GOOD;
#4 cumulative CFO/PAT<0.50 → max AVERAGE)

### Working Capital Days detail (feeds B4, and FLAG-CASH)

Receivable Days = Receivables÷Revenue×365 (Revenue basis). Inventory Days
computed on **Raw Material Cost basis** (COGS proxy, explicitly available
in screener-data, per formula's COGS-if-available rule — stated).
Payable Days = Trade Payables÷Revenue×365 (Revenue basis; Trade Payables
FY24/FY25 from AR p.85-86, FY26 not extractable, see below).

| FY | Receivable Days | Inventory Days (RM-cost basis) | Payable Days | WC Days |
|----|------------------|----------------------------------|--------------|---------|
| FY24 | 64.63 (Receivables 7.23cr, screener-data) | 104.98 (Inventory 10.23cr ÷ RM Cost 35.57cr, screener-data) | 23.46 (Trade Payables 2.624cr, AR p.85) | **146.15** |
| FY25 | 92.12 (Receivables 33.77cr, screener-data) | 59.41 (Inventory 18.86cr ÷ RM Cost 115.86cr, screener-data) | 20.09 (Trade Payables 7.3645cr, AR p.86) | **131.44** |
| FY26 | 133.36 (Receivables **94.31cr**, screener-data — this ANCHORS the operator-relayed "~Rs94cr receivables spike" lead; it is not merely a lead, it is a clean screener figure) | 73.19 (Inventory 47.04cr ÷ RM Cost 234.60cr, screener-data) | **N/A** (not in screener Data_Sheet; results filing p.6-7 balance sheet OCR too corrupted to extract) | Receivable+Inventory Days alone = **206.55** |

Bound for B4: WC Days FY26 = 206.55 − Payable Days FY26. For the FY26 vs
FY24 change to fall to ≤15 days (bands 1 or 3 instead of 0), Payable Days
FY26 would need to be ≥45.4 days — more than double the FY24 (23.46) and
FY25 (20.09) actual levels, with no evidence anywhere in the record
(concalls, digest, AR) of such a payment-term extension; the operator
digest instead describes ~35-45 day RM inventory cycles and monthly
Hindalco pricing resets, consistent with payables staying in the
historical ~20-35 day range. Scored **0** on this basis; flagged as a
bound, not an exact figure.

**FLAG-CASH**: block_b_trend = deteriorating. Receivables grew 179%
(Rs33.77cr → Rs94.31cr, FY25→FY26, screener-data) against 93% revenue
growth in the same period; CFO went from −Rs13.72cr (FY24) to −Rs36.79cr
(FY26) against PAT that grew from +Rs1.37cr to +Rs19.84cr — cash
conversion deteriorated in absolute terms even as reported profit
strengthened. INDETERMINATE FY25 CFO is a genuine input_gap; it does not
change B1/B2/B3's classification-relevant conclusion (both anchored years
already sit at the worst scoring band).

---

## BLOCK C: GROWTH (Max 20)

| FY | Revenue (cr) | YoY | PAT (cr) | YoY |
|----|--------------|-----|----------|-----|
| FY24 | 40.83 (screener-data) | — | 1.37 (screener-data) | — |
| FY25 | 133.80 (screener-data) | +227.7% | 9.65 (screener-data) | +604.4% |
| FY26 | 258.15 (screener-data) | +93.0% | 19.84 (screener-data) | +105.6% |

C1 Revenue CAGR (FY24→FY26, 2yr): (258.15/40.83)^(1/2)−1 = **151.46%** →
**≥20% = 5**
C2 PAT CAGR (FY24→FY26): (19.84/1.37)^(1/2)−1 = **280.55%** → **≥20% = 5**
C3 Positive YoY revenue years: 2 of 2 (100%) → **100% = 5**
C4 PAT CAGR − Revenue CAGR = 280.55 − 151.46 = **+129.09pp** → **≥+3pp = 5**

**Block C = 20/20** — a post-IPO capacity-ramp growth story (Unit 1 Vasai
scaling toward 100% utilisation, Unit 2 Ahmedabad ramping per the operator
digest); mechanical growth score, not itself a quality signal — see Block
B for the cash-conversion cost of this growth.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

All at FY26 (latest, screener-data unless noted).
EBITDA FY26 = EBIT 29.32 + Depreciation 0.46 = 29.78cr.

D1 Net Debt ÷ EBITDA: Net Debt = Borrowings 44.39 − Cash 0.50 = 43.89cr.
43.89 ÷ 29.78 = **1.47x** → **1-2x = 3**
D2 Interest Coverage: EBIT 29.32 ÷ Interest 3.00 = **9.77x** → **5-9.9x = 4**
D3 Debt ÷ Equity: Borrowings 44.39 ÷ (Equity+Reserves) 74.46 = **0.596** →
**0.5-1.0 = 4** — correction, see note below
D4 Current Ratio: Current Assets ≈149.6cr (screener-data "Other Assets"
150.11cr, net of an immaterial non-current residual — FY25's equivalent
residual was 0.23cr on a 56.29cr base, i.e. <1%) ÷ Current Liabilities
bounded 90.55cr (NCL≈0, historical pattern) to 74.57cr (NCL≈16cr) →
Current Ratio bounded **1.65x–2.01x**, straddling the 1.5-2.0x band edge.
Scored conservatively at the low bound: **1.5-1.99x = 4**

Note on D3: 0.596 falls in the 0.5-1.0 band, which scores **3**, not 4 —
correcting the line above: **D3 = 3**.

**Block D = 3(D1... )** — recomputing the total: D1=3, D2=4, D3=3, D4=4 →
**Block D = 14/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Source: operator-supplied screener shareholding screenshot, anchored as
"(screener shareholding, operator-supplied 2026-07-24)" per
OPERATOR_CONTEXT.md provenance rules.

| Quarter | Promoters | DII | Public | #Shareholders |
|---------|-----------|-----|--------|----------------|
| Sep 2024 (earliest available; company IPO'd 31-May-2024, no earlier quarter exists) | 73.14% | 0.00% | 26.86% | 450 |
| Jun 2026 (latest) | 54.38% | 2.46% | 43.16% | 1,719 |

E1 Promoter holding (latest, Jun2026) = **54.38%** → **50-59.9% = 4**
E2 Promoter holding change: a true 3-year window is not available (only
~21 months of disclosed history exist, from the first post-IPO quarter).
Using the full available window, Sep2024 (73.14%) → Jun2026 (54.38%) =
**−18.76pp** → **decreased >3% = 0**. Whether this reflects QIP/fresh-issue
dilution (funds the FY26 reserves jump and capex ramp) or open-market
sell-down is explicitly flagged by OPERATOR_CONTEXT.md as an open question
for Stage 8 (promoter) to adjudicate from the AR, results, and web — not
resolved here.
E3 Promoter pledge: **N/A (not in provided data)** — no pledge column in
the operator shareholding table; no pledge disclosure found in the AR
extract or either results filing. Scored **0**, not assumed nil.
E4 Contingent Liabilities ÷ Net Worth: **N/A (not in provided data)** — no
contingent-liabilities note found anywhere in the FY25 AR extract (grep
across the full 113-page extract returned no match). Scored **0**, not
assumed nil.

**Block E = 4/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Note on sector label: the run manifest's sector_cap_row says "Pharma /
CDMO." GSM Foils is an aluminium pharma-foil + ROPP-caps packaging
manufacturer, not a CDMO — a mislabel. This did not distort any test
below because M2/M5/M7/M9 (the peer-relative tests) already score 0 for
absent peer data regardless of sector label; flagged for phase-3.

| # | Test | Score | Basis |
|---|------|-------|-------|
| M1 | Pricing Power | **5** | EBITDA margin expanded 6.69%→11.54% (screener-data derived, +4.85pp) AND revenue CAGR 151.46% ≥10% |
| M2 | Cost Advantage vs peer | **0** | PEER DATA NEEDED — no peer/competitor financials in inputs |
| M3 | Capital Efficiency | **5** | FAT (Revenue÷Net Block) FY25 = 133.8/2.12 = 63.1x, FY26 = 258.15/5.09 = 50.7x, both >3x; ROCE FY25=47.77% and FY26 bounded 24.67-39.37%, both >20% in every scenario. Caveat: Units 2/3/4 are leased not owned (operator digest), so the tiny Net Block base inflates FAT beyond what owned-asset capital efficiency would show — flagged for downstream (Stage 7/11), not double-counted here. |
| M4 | Customer Stickiness | **3** | Zero revenue-decline years (satisfies the "max 1 decline year" clause for the 3-band); does NOT reach the 5-band because receivable days rose 64.6→133.4 days, far outside the required ±10 stability |
| M5 | Scale & Dominance | **0** | PEER DATA NEEDED — no segment mcap/margin ranking data provided |
| M6 | Technology/R&D | **0** | No R&D line disclosed; not applicable to this business |
| M7 | Regulatory/License | **0** | PEER DATA NEEDED — pharma-foil packaging is a regulated-adjacent segment but player-count data not provided |
| M8 | Distribution | **0** | No quantified distribution/reach metric in provided data (B2B industrial supplier) |
| M9 | Brand | **0** | PEER DATA NEEDED. Gross-margin proxy computed = (Revenue−Material Cost)÷Revenue: FY24 12.88%, FY25 13.41%, FY26 9.12% (screener-data) — proxy stated but not scored, no peer median available |
| M10 | Switching Costs | **0** | Revenue grew every year, but receivable days rose 68.7 days over the period (64.6→133.4), far above the ≤10-day requirement for any positive band |
| M11 | Network Effects | **0** | Only 3 years available, <6 required for the two-window test; scored conservatively per instruction. Partial, non-decisive signal: FY24→FY25 selling-expense/revenue ratio declined 1.54%→0.59% (screener-data); FY26 selling & admin not separately disclosed (merged into "Other Expenses" in screener-data) |
| M12 | Negative WC/Float | **0** | WC Days positive and >45 in every year (146.15 / 131.44 / ≥161 bounded FY26) |

**Moat score = 13/60. Moats present (score≥3): M1, M3, M4 = 3 → MODERATE**
(2-3 present = MODERATE)

---

## DASHBOARD SUMMARY

```
BLOCK SCORES (Core, /100)
A Return on Capital .......... 20/20  ████████████████████
B Cash Generation Quality ....  0/20  (deal-breaker: max AVERAGE)
C Growth ...................... 20/20  ████████████████████
D Balance Sheet Strength ...... 14/20  ██████████████
E Shareholder Alignment ........ 4/20  ████
                              -------
CORE SCORE ..................... 58/100

MOAT PROFILE (/60)
M1 ████████████████████ 5   M2 ░ 0 (peer needed)  M3 ████████████████████ 5
M4 ████████████ 3          M5 ░ 0 (peer needed)   M6 ░ 0
M7 ░ 0 (peer needed)        M8 ░ 0                 M9 ░ 0 (peer needed)
M10 ░ 0                     M11 ░ 0                M12 ░ 0
MOAT SCORE ...................... 13/60  Moats present: 3 (M1,M3,M4) = MODERATE

GRAND TOTAL ..................... 71/160
```

Strongest blocks: A (Return on Capital, 20/20) and C (Growth, 20/20) —
tied. Weakest block: B (Cash Generation Quality, 0/20) — deal-breaker.

### Classification

Base matrix: Core 58 falls in the 40-59 band → **AVERAGE** (flat by
matrix regardless of moat class in this band).
Deal-breakers confirm/cap the same result: #2 Block B<8 → max GOOD (not
binding, already below GOOD); #4 cumulative CFO/PAT<0.50 → **max AVERAGE**
(binding, matches matrix result).

**History confidence tier**: 3 years of full-FY data (FY24, FY25, FY26)
falls in the framework's stated "3-4 yrs = LIMITED, downgrade
classification one tier" band. This rule fires mechanically here — stated
explicitly per pipeline instruction, and it is a **data-length rule, not
a quality judgment**: GSM Foils listed 31-May-2024 (SME IPO) and no
prospectus/pre-IPO restated financials exist in inputs, so no additional
years can be sourced. `history_downgrade = true`.

Applying the one-tier downgrade to the base AVERAGE classification:
**AVERAGE → AVOID**.

```
┌─────────────────────────────────────────────────────────┐
│  GATE 0 CLASSIFICATION:  AVOID                           │
│  Core 58/100 (AVERAGE band) + MODERATE moat (13/60)      │
│  → downgraded one tier (LIMITED history, 3 yrs) → AVOID  │
│  Grand total: 71/160                                     │
└─────────────────────────────────────────────────────────┘
```

Two independent mechanisms land here, and downstream stages should treat
them separately:
1. **Substantive**: Block B deal-breaker — cumulative CFO deeply negative
   against positive and growing PAT in every measurable year, driven by a
   real, anchored receivables buildup (Rs7.23cr→Rs94.31cr, FY24→FY26)
   that has outpaced revenue growth. This is a genuine, evidenced
   cash-conversion concern, not a data artifact.
2. **Mechanical**: LIMITED-tier one-notch history downgrade, purely a
   function of GSM Foils being 2 years post-IPO with no way to source
   more history. Per this run's instructions, this is a data-length note
   and should not be read by downstream stages as an independent
   quality signal beyond what's already captured in mechanism 1.

Per CLAUDE.md, this classification does not halt the pipeline (no STOP
verdict exists) and flags propagate rather than gating; downstream
position-sizing may weigh the post-IPO-rebase context noted above.

### Decision line
GSM Foils screens AVOID at Gate 0 on a 58/100 core (strong 20/20 Return on
Capital and 20/20 Growth blocks, offset by a 0/20 Cash Generation block
that trips the CFO/PAT deal-breaker) plus a mechanical one-tier downgrade
for its 3-year (LIMITED-tier) post-IPO history. The receivables spike to
Rs94.31cr (FY26, anchored, up 179% YoY against 93% revenue growth) is the
single dominant number behind Block B and should be the first thing
Stage 5 (concall) and Stage 8 (promoter) interrogate — including whether
it is genuinely collectible (pharma-client payment delays per operator
digest) and whether the concurrent promoter stake fall (73.14%→54.38%,
Sep2024→Jun2026) reflects dilution funding the capex ramp or something
else.

---

```yaml
stage: B01-gate0
company: "GSMFOILS"
run_date: "2026-07-24"
model: claude-sonnet-5
status: complete
input_gaps:
  - "CFO FY25 (screener Data_Sheet blank; Q4FY26 results filing p.8 cash-flow statement is scanned/OCR-corrupted, not used as a scored anchor)"
  - "FY26 balance-sheet current/non-current liability split (results filing p.6-7 OCR corrupted; not carried in screener Data_Sheet) — bounded, not exact, for ROCE FY26 and Current Ratio FY26"
  - "FY26 trade payables (not in screener Data_Sheet; results filing OCR corrupted) — B4 WC-days score is a bounded conclusion, not an exact figure"
  - "Promoter pledge % (not disclosed in operator shareholding table, AR extract, or either results filing)"
  - "Contingent liabilities (no note found anywhere in the FY25 AR extract)"
  - "Peer/competitor financial and segment-structure data for moat tests M2, M5, M7, M9 (PEER DATA NEEDED, none provided in inputs)"
flags:
  - {type: FLAG-GATE0, reason: "AVOID classification: Core 58/100 (AVERAGE band) capped by Block B deal-breaker (cumulative CFO/PAT -2.38x on anchored years), then downgraded one tier by the mechanical LIMITED-tier history rule (3 yrs data, listed 31-May-2024). Blocks A (Return on Capital, 20/20) and C (Growth, 20/20) are strong; the depressors are Block B (0/20) and Block E (4/20, pledge/contingent-liability data gaps plus a -18.76pp promoter stake fall Sep2024-Jun2026 not yet adjudicated as dilution vs sell-down)."}
  - {type: FLAG-CASH, reason: "Block B deteriorating: receivables grew 179% (Rs33.77cr to Rs94.31cr, FY25 to FY26, screener-data) against 93% revenue growth; CFO worsened from -Rs13.72cr (FY24) to -Rs36.79cr (FY26) against PAT growing +Rs1.37cr to +Rs19.84cr over the same span. FY25 CFO is INDETERMINATE (not in provided data) and is not resolved to any score; caps B1/B3 conclusions on the two anchored years only."}
data_years: 3
fy_range: "FY24 to FY26"
blocks: {A: 20, B: 0, C: 20, D: 14, E: 4}
core_score: 58
moat_score: 13
grand_total: 71
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "#2 Block B <8 -> max GOOD (Block B = 0)"
  - "#4 cumulative CFO/PAT <0.50 -> max AVERAGE (ratio -2.38x, FY24+FY26 anchored years)"
history_downgrade: true
data_notes:
  - "FY23 stub (9-month, to 31-Dec-2023, screener-data) excluded from FY count; FY24 (year ended 31-Mar-2024) is the first full fiscal year, consistent with the AR calling FY25 the company's '02nd Annual Report.'"
  - "Inventory Days computed on Raw Material Cost (COGS proxy) basis per the formula's COGS-if-available rule, stated; Receivable and Payable Days on Revenue basis."
  - "B1/B2/B3 computed from FY24+FY26 only (2 of 3 years) because FY25 CFO is not in provided data; a non-anchored cross-check (internal cash reconciliation of the OCR-garbled Q4FY26 results filing p.8) implies FY25 CFO approx -Rs17.69cr, directionally consistent (also deeply negative) but NOT used in any score."
  - "Capex proxied via net-block-movement (closing Net Block - opening Net Block + Depreciation) for FY25 (Rs1.56cr) and FY26 (Rs3.43cr); FY24 capex taken directly from CFI (Rs0.97cr) since non-current investments were nil that year (screener-data)."
  - "FY26 ROCE (A1/A2/A4) and Current Ratio (D4) were bounded via the accounting identity Total Assets = Equity+Reserves+NCL+CL against the company's historical near-all-short-term borrowings mix, rather than an exact extracted figure; A1's median uses FY24+FY25 only to avoid the bound's low end flipping bands; A4's latest-vs-earliest and A2's minimum are robust across the full bound range; D4 used the bound's conservative (lower) end."
  - "M9 Brand test: gross-margin proxy (Revenue-Material Cost)/Revenue computed (FY24 12.88%, FY25 13.41%, FY26 9.12%, screener-data) but not scored — no peer median available, proxy basis stated per instruction."
  - "M11 Network Effects: <6 years of history (3 available) makes the two-window test non-computable; scored conservatively at 0 per instruction. Partial, non-decisive signal: FY24-to-FY25 selling-expense/revenue ratio declined 1.54%->0.59% (screener-data); FY26 selling & admin expense not separately disclosed (merged into 'Other Expenses' in screener-data)."
  - "Sector cap row in the run manifest ('Pharma/CDMO') is a mislabel -- GSM Foils manufactures aluminium pharma foils and ROPP caps, not CDMO services. Did not distort Gate 0 scoring since the peer-relative moat tests (M2, M5, M7, M9) already scored 0 for absent peer data regardless of sector label; flagged for phase-3."
  - "history_downgrade fires under the framework's '3-4 yrs = LIMITED tier, downgrade one tier' rule (we have exactly 3 full fiscal years). This is a data-length rule tied to GSM Foils being ~2 years post-IPO with no sourceable pre-IPO history, not an independent company-quality judgment -- flagged explicitly per this run's instructions."
  - "Q1 FY27 (quarter ended 30-Jun-2026, screener-data): Sales Rs96.89cr, Operating Profit Rs11.51cr (11.9% margin, tracking the operator-digest FY27 margin-sustain guidance of 11.5-12%), Net Profit Rs7.62cr -- supplementary momentum context only, not scored into any block above."
block_b_trend: "deteriorating -- receivables grew 179% (Rs33.77cr to Rs94.31cr, FY25 to FY26, screener-data) against 93% revenue growth, and CFO worsened from -Rs13.72cr (FY24) to -Rs36.79cr (FY26) even as PAT grew from +Rs1.37cr to +Rs19.84cr"
```
