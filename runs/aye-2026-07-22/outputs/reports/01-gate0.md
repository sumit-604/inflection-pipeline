# GATE 0 QUANTITATIVE SCORECARD — Aye Finance Limited (AYE)
Run date: 2026-07-22 | Stage: B01-gate0 | Model: claude-sonnet-5

Data available: 4 fiscal years (FY23 to FY26), plus one interim quarter
(Q1 FY27, quarter ended 30-Jun-2026). Scoring adapted to a 4-year history
— this lands in the framework's "3-4 yrs = LIMITED" confidence band, which
triggers a one-tier classification downgrade (applied at the end of this
report).

## NBFC METRIC ADAPTATION (read first)

Aye Finance is an NBFC-ML lender (MSME/micro-enterprise loans), not a
manufacturer. Per the CLAUDE.md NBFC adaptation instruction, the following
substitutions are used and named at each line:
- ROCE (A1/A2) → ROA (PAT ÷ average Total Assets); ROE (A3) is already
  framework-native and is additionally used as the primary capital-return
  read for a lender.
- EV/EBITDA, inventory/WC days → not applicable; GNPA/NNPA, credit cost,
  CRAR and gearing carry the balance-sheet-strength read (Block D).
- CFO/PAT (Block B) is structurally negative for any growing balance-sheet
  lender (loan disbursements are an operating cash outflow under Ind AS 7).
  This is marked INDETERMINATE, not scored as a going-concern signal — see
  Block B note. Per CLAUDE.md this must cap any downstream verdict at
  PROCEED WITH CAVEATS minimum; it is not on its own an AVOID driver.
- D1 uses CRAR, D2 uses PCR (both framework-specified NBFC substitutes).
  D4 (current ratio) is substituted with Liquidity Coverage Ratio (LCR),
  named explicitly as it is not a framework-specified substitute.
- Six of twelve moat tests (M2,M3,M5,M6,M7,M9) require peer financial/
  market-cap data not present in the four anchored sources for this run
  and are scored 0, marked PEER DATA NEEDED per the moat-scoring rule.

## SOURCES USED (with anchor page counters)
- Prospectus (IPO), Restated Financial Statements: Annexure I (Statement
  of Assets & Liabilities) = extract PAGE 313/614; Annexure II (P&L) =
  PAGE 314/614; Annexure III (Cash Flows) = PAGE 315-316/614. Covers FY23,
  FY24, FY25 (year ended 31-Mar) plus H1 FY26/H1 FY25 stubs to 30-Sep.
  File: annual-report__1770879625663.txt
- FY26 Audited Results (year ended 31-Mar-2026), board 27-Apr-2026:
  Balance sheet = PAGE 5/26; P&L = PAGE 6/26; Cash flow = PAGE 7-8/26;
  Annexure I (Reg 52(4) ratios) = PAGE 11/26. File: results__edbf1e94-
  d388-49a5-9842-9b8955a19b59.txt
- Q1 FY27 Results (quarter ended 30-Jun-2026), board 22-Jul-2026:
  Annexure-1 (Reg 52(4) ratios) = PAGE 5/19. This filing is heavily OCR-
  garbled (character-per-line extraction); only the Annexure-1 ratio block
  was reliably digit-by-digit reconstructed and cross-checked (arithmetic
  ties back to itself: e.g. Net worth 2,528.01 and PAT 74.50 are the raw
  tokens recovered). Full P&L/B&S line items for Q1 FY27 are NOT FOUND
  (unreconstructable from this extract). File: results__2246e44a-59ad-
  423a-ae43-c3e537e8c140.txt
- ICRA rating rationale, 12-Nov-2025, [ICRA]A Stable: PAGE 1/7 (rationale,
  credit strengths), PAGE 2/7 (credit challenges, sensitivities), PAGE 3/7
  (Key financial indicators table). File: rating__138929.txt
- Shareholding (operator-supplied, screener-class, mid-run fill):
  runs/aye-2026-07-22/inputs/shareholding/screener_shareholding_Mar-
  Jun2026.md
- Operator digest (non-anchored cross-check only, digest-only where noted):
  runs/aye-2026-07-22/inputs/announcements/operator_digest_6m_to_2026-07-22.md

Company does NOT have an identifiable promoter (Prospectus, PE/VC-backed:
Elevation, CapitalG/Google, Temasek IMP2, A91, BII, Alpha Wave and others).
Listed BSE 544699 / NSE AYE, Feb-2026.

---

## BLOCK A: RETURN ON CAPITAL (adapted: ROA in place of ROCE) — Max 20

Total Assets and Total Equity (₹ crore): FY23 3,126.00 / FY24 4,869.59 /
FY25(restated) 6,338.63 / FY26(audited) 7,772.94 (annual report PAGE
313/614; results p.5/26). Equity: FY23 754.49 / FY24 1,232.65 / FY25
1,658.87 (restated, annual report PAGE313/614; audited comparative in
results p.5/26 is 1,658.35, consistent) / FY26 2,532.71 (results p.5/26).

PAT (₹ crore, restated FY23-25 / audited FY26): FY23 39.87 / FY24 171.68 /
FY25 175.25 (annual report PAGE 314/614) / FY26 193.63 (results p.6/26,
p.11/26 Annexure I).

ROA = PAT ÷ average Total Assets (computed; FY23 opening total assets not
available in the 3-year restated window, FY23 uses closing only, stated):
- FY23: 39.87 ÷ 3,126.00 (closing only) = 1.28%
- FY24: 171.68 ÷ avg(3,126.00, 4,869.59) = 4.29%
- FY25: 175.25 ÷ avg(4,869.59, 6,338.63) = 3.13%
- FY26: 193.63 ÷ avg(6,338.11, 7,772.94) = 2.74%
Median ROA = 2.94% (avg of 2.74%, 3.13%). Min single-year ROA = 1.28%
(FY23, closing-only distorted) / 2.74% ex-FY23.

ROE = PAT ÷ average Net Worth (computed, FY23 closing-only, stated):
- FY23: 39.87 ÷ 754.49 (closing only) = 5.28%
- FY24: 171.68 ÷ avg(754.49, 1,232.65) = 17.28%
- FY25: 175.25 ÷ avg(1,232.65, 1,658.87) = 12.12%
- FY26: 193.63 ÷ avg(1,658.35, 2,532.71) = 9.24% (post-IPO equity dilution
  — FY26 net worth was inflated mid-year by the Feb-2026 ₹710cr primary
  raise, results p.11/26)
Median ROE = 10.68%. Cross-check, ICRA-reported average-net-worth ROE
(originally-audited basis, not restated): FY24 16.1%, FY25 11.8% (rating
PAGE 1/7).

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| A1 | Median ROA (ROCE substitute) | 2.94% | <10% manufacturing band | **0** |
| A2 | Min single-year ROA | 1.28% (FY23 closing-only) | <8% | **0** |
| A3 | Median ROE | 10.68% | <12% | **0** |
| A4 | ROA/ROE trend, latest vs earliest | ROA +1.47pp, ROE +3.96pp (FY26 vs FY23) | latest ≥ earliest | **5** |

**Block A = 5/20.** A1/A2 mechanically floor at 0 because ROA for any NBFC
sits in low single digits while the manufacturing ROCE bands are
calibrated to double-digit capital returns — this is a scale mismatch, not
evidence of weak capital return (ICRA-anchored ROE of 16.1% in FY24 was
solid). A3 also floors at 0 largely on the FY23 closing-only distortion
and FY26 post-IPO dilution; FY24's 17.28%/16.1% ROE (both bases) was the
strongest year before asset-quality-driven compression.

---

## BLOCK B: CASH GENERATION QUALITY — Max 20 — **INDETERMINATE**

Net cash used in operating activities (₹ crore): FY23 (720.39) / FY24
(1,322.83) / FY25 (811.78, restated, ties exactly to the FY26 filing's
audited FY25 comparator of (811.79), results p.7/26) / FY26 (1,354.64)
(annual report PAGE 315/614; results p.7/26).

Capex (purchase of PPE excl. ROU, ₹ crore): FY23 (4.43) / FY24 (11.61) /
FY25 (16.89) (annual report PAGE 315/614) / FY26 (11.66) (results p.7/26).

FCF = CFO − Capex: FY23 (724.82) / FY24 (1,334.44) / FY25 (828.67) / FY26
(1,366.30). All four years negative.

CFO is structurally negative every year because loan disbursements to
customers are classified as an operating cash outflow under Ind AS 7 for
a balance-sheet lender funding its own loan book — this is normal for any
scaling NBFC and is NOT a going-concern or earnings-quality signal in the
way it would be for a manufacturer. Literal formula application:

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| B1 | Cumulative CFO ÷ Cumulative PAT | (4,209.64) ÷ 580.43 = **-7.25x** | <0.50 | **0** |
| B2 | FCF-positive years | 0 / 4 = 0% | <50% | **0** |
| B3 | Cumulative FCF ÷ Cumulative PAT | (4,254.23) ÷ 580.43 = **-7.33x** | <0.20 / negative | **0** |
| B4 | Change in WC Days | NOT APPLICABLE — no trade receivables/inventory/payables for a balance-sheet lender | — | **0 (N/A)** |

**Block B = 0/20 — INDETERMINATE.** Per CLAUDE.md, an INDETERMINATE cash-
conversion read must not silently resolve to PROCEED downstream; it caps
the eventual verdict at PROCEED WITH CAVEATS minimum, with this note named
explicitly. `block_b_trend`: CFO/PAT ratio improved from -18.1x (FY23) to
-4.6/-4.7x (FY25) then worsened to -7.0x (FY26), tracking accelerated loan
disbursement growth after the IPO capital infusion (AUM +26-27% YoY FY26
per ICRA/digest) — a scale-of-growth signal, not a profitability-quality
deterioration signal.

---

## BLOCK C: GROWTH — Max 20

Total revenue from operations (₹ crore): FY23 623.43 / FY24 1,040.22 /
FY25 1,459.73 (restated, annual report PAGE 314/614, ties exactly to the
FY26 filing's FY25 comparator) / FY26 1,814.73 (results p.6/26).

PAT (₹ crore, same basis as Block A): FY23 39.87 / FY24 171.68 / FY25
175.25 / FY26 193.63.

Revenue CAGR (FY23→FY26, 3yr) = (1,814.73 ÷ 623.43)^(1/3) − 1 = **42.8%**
PAT CAGR (FY23→FY26, 3yr) = (193.63 ÷ 39.87)^(1/3) − 1 = **69.4%** (basis
note: mixes restated FY23 with audited FY26 — see data_notes on the FY24/
FY25 restatement uplift; both endpoints used here are on their respective
native bases and each is independently anchored)

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| C1 | Revenue CAGR | 42.8% | ≥20% | **5** |
| C2 | PAT CAGR | 69.4% | ≥20% | **5** |
| C3 | Positive YoY revenue years | 3/3 = 100% (FY24,FY25,FY26 all up) | 100% | **5** |
| C4 | PAT CAGR − Revenue CAGR | +26.6pp | ≥+3pp | **5** |

**Block C = 20/20.** Revenue growth is broad-based across all four years
(no decline year in either revenue or PAT on either restatement basis) and
is corroborated by ICRA's independently-stated AUM CAGR of 25% FY2020-
FY2025 (rating PAGE 1/7). This is the strongest block and is genuine, not
an artifact of a low base alone — see Block A/D for where growth is being
purchased at a cost (asset-quality softening, thin core ROA).

---

## BLOCK D: BALANCE SHEET STRENGTH (adapted: CRAR/PCR/LCR) — Max 20

CRAR: FY24 32.8%, FY25 34.9%, Q1FY26 34.8% (rating PAGE 3/7) → FY26
(audited) 42.24% (results p.11/26) → Q1FY27 42.38% (results p.5/19). Rise
in FY26 driven by the Feb-2026 IPO primary raise.

PCR (Provision Coverage Ratio, ECL on Gross Stage III ÷ Gross Stage III):
FY26 63.66% (results p.11/26) → Q1FY27 63.80% (results p.5/19).

Debt/Equity (company-disclosed): FY26 2.06x (results p.11/26) → Q1FY27
2.22x (results p.5/19). Context: ICRA's managed gearing (on-book debt +
off-book portfolio ÷ net worth) was 3.0x (FY25) / 3.1x (Q1FY26, rating
PAGE 1/7) — well inside ICRA's own negative-sensitivity trigger of >4.5x
(rating PAGE 2/7).

LCR (D4 substitute for current ratio, named explicitly — no NBFC
substitute is specified by the framework for D4): FY26 205.16%, Q1FY27
269.61% (results p.11/26, p.5/19) — both far above the ~85-100% regulatory
floor for NBFC-ML.

| # | Metric | Value (latest = Q1FY27, FY26 in parens) | Band | Score |
|---|---|---|---|---|
| D1 | CRAR (ND/EBITDA substitute) | 42.38% (42.24%) | ≥18% | **5** |
| D2 | PCR (Interest coverage substitute) | 63.80% (63.66%) | 60-70% | **3** |
| D3 | Debt/Equity | 2.22x (2.06x); "Financials: default 3" applied literally | default | **3** |
| D4 | LCR (Current ratio substitute) | 269.61% (205.16%) | ≥2.0x-equivalent | **5** |

**Block D = 16/20.** Capitalisation is genuinely strong and improving
(IPO-boosted CRAR, low managed gearing vs. rating sensitivity, very
comfortable liquidity). PCR at 63.66-63.80% sits just under the 70%
top-band threshold — asset-quality provisioning is adequate, not
generous, consistent with the GNPA trend flagged below.

Asset quality trend (context for D-block, not separately scored — avoids
double-counting into moat tests M4/M10, see Block F): Gross Stage
III/GNPA 3.2% (Mar-24) → 4.2% (Mar-25) → 4.6% (Sep-25, rating PAGE 2/7,
"marginally breaching the ICRA-stipulated rating sensitivity of 5%" at
90+dpd 5.1%) → 4.77% (Mar-26, results p.11/26) → 4.49% (Jun-26, results
p.5/19). Deteriorated through FY25/H1FY26, improving in the most recent
two data points but not yet a demonstrated full cycle.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (adapted: no promoter) — Max 20

No identifiable promoter (Prospectus). Institutional stake used as the
alignment proxy in place of promoter holding: FII+DII 37.05% (Mar-2026,
debut post-listing quarter) → 35.45% (Jun-2026) (operator-supplied
screener shareholding, screener-class/anchored-equivalent). This is below
the framework's ">50% FII+DII = professionally managed, score 3" carve-
out threshold, so it is scored via literal analogy to the promoter-holding
band (30-39.9% = 1).

| # | Metric | Value | Band | Score |
|---|---|---|---|---|
| E1 | Institutional stake (promoter-holding proxy) | 35.45% (Jun-26) | 30-39.9% band, by analogy | **1** |
| E2 | 3-year change | NOT APPLICABLE — listed Feb-2026, no 3-year window exists | — | **0 (N/A)** |
| E3 | Pledge | 0% by definition — no promoter entity exists to pledge | 0% | **5** |
| E4 | Contingent liabilities ÷ Net Worth | ₹158.92mn ÷ ₹17,273.72mn = 0.92% (as at 30-Sep-2025, restated stub — most recent breakout in the anchored sources; annual report PAGE 31/614, Note 33 reference) | <5% | **5** |

**Block E = 11/20.** Per CLAUDE.md, this must NOT be read as an
"institutional-absence risk" flag — ~35-37% FII+DII is a substantial
institutional base for a small-cap NBFC, not a thin one, and the UA
(institutional-absence) multiplier is explicitly not triggered for this
name. E1's low mechanical score reflects the framework's promoter-centric
band structure not cleanly covering a "no promoter, 30-50% institutional"
case, not a genuine alignment concern.

---

## BLOCK F: QUANTITATIVE MOAT SCORING — Max 60

| # | Test | Read | Score |
|---|---|---|---|
| M1 | Pricing Power | Net profit margin (PAT/Total income substitute for EBITDA margin) expanded from 6.20% (FY23) to 11.38% (FY26, results p.11/26), +5.18pp, with revenue CAGR 42.8% ≥10% | **5** |
| M2 | Cost Advantage vs peer | PEER DATA NEEDED | **0** |
| M3 | Capital Efficiency (FAT×ROCE) | NOT APPLICABLE — no fixed-asset-turnover concept for a lender; ROA substitute is inherently low-single-digit (see Block A) | **0** |
| M4 | Customer Stickiness | Receivable-days concept N/A for a lender; revenue grew every year but the stability leg cannot be assessed without reusing the GNPA trend already scored in Block D (avoiding double-count per CLAUDE.md) | **0** |
| M5 | Scale & Dominance | PEER DATA NEEDED (mcap/margin ranking not provided) | **0** |
| M6 | Technology / R&D | PEER DATA NEEDED — no anchored R&D/Revenue % disclosed (digest mentions AI/ML underwriting, non-anchored, unquantified) | **0** |
| M7 | Regulatory / License | Regulated NBFC-ML segment, but exact count of comparable listed players is PEER DATA NEEDED (not anchored in provided sources) | **0** |
| M8 | Distribution | Reach quantified at one point (527 branches, 21 states/UTs, rating PAGE 3/7) but no anchored branch-count trend or revenue-per-branch series to confirm growth | **1** |
| M9 | Brand / spread vs peers | PEER DATA NEEDED | **0** |
| M10 | Switching Costs | Revenue grew every year, but the stability leg (receivable days) is N/A for a lender and not double-counted with Block D's GNPA read | **0** |
| M11 | Network Effects | Only 4 years of data (<6yr two-window test); revenue CAGR 42.8% >20% but "selling expense %" is not separately broken out in the anchored P&L (bundled in Other Expenses) — scored conservatively per the rule, and stated so | **1** |
| M12 | Negative WC / Float | NOT APPLICABLE — no inventory/payables float concept for a balance-sheet lender | **0** |

**Moat score = 7/60.** Moats present (score ≥3): M1 only → **moats_confirmed = 1 → THIN**.
Profile: [█░░░░░░░░░░░] M1 present; ten of eleven remaining tests are 0,
eight of which are explicitly PEER DATA NEEDED or NOT APPLICABLE rather
than demonstrated moat absence.

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation | 0 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 16 | 20 |
| E — Shareholder Alignment | 11 | 20 |
| **Core Score** | **52** | **100** |
| Moat Score | 7 | 60 |
| **Grand Total** | **59** | **160** |

Moat class: THIN (1 moat confirmed).

Classification matrix: Core 52 falls in the 40-59 band → **AVERAGE**
(flat at this tier regardless of moat class).

Deal-breaker check:
1. Block A (5) < 8 → cap GOOD — non-binding (already below GOOD)
2. Block B (0) < 8 → cap GOOD — non-binding
3. Median return < 10% (ROA substitute 2.94%) → cap AVERAGE — binding but
   non-differentiating (already at AVERAGE); using the framework-native
   ROE instead (median 10.68%) this deal-breaker would NOT trigger
4. Cumulative CFO/PAT (-7.25x) < 0.50 → cap AVERAGE — binding, tied to
   the Block B INDETERMINATE read above
5-9: pledge, ND/EBITDA+IC, revenue decline, PAT negative, history<3yrs —
   none triggered

History-length downgrade: data_years = 4 → LIMITED confidence band (3-4
years) → **classification downgraded one tier: AVERAGE → AVOID**

## FINAL CLASSIFICATION: AVOID

Strongest block: **C — Growth (20/20)**, genuine and broad-based.
Weakest block: **B — Cash Generation (0/20, INDETERMINATE)**, structural
to a scaling balance-sheet lender, not an earnings-quality failure.

**Decision line:** Mechanical Gate 0 output is AVOID, but this is driven
predominantly by (a) NBFC metric-scale mismatches under manufacturing-
calibrated bands in Blocks A and B, (b) the LIMITED-history one-tier
downgrade from a company that IPO'd Feb-2026 and therefore has only four
FY periods of disclosed financials by construction, and (c) heavy PEER
DATA NEEDED gaps across six of twelve moat tests — not by demonstrated
fundamental deterioration. ICRA-anchored fundamentals (comfortable 42%
CRAR, historically double-digit ROE, 25% AUM CAGR) and the Mar-26→Jun-26
GNPA improvement (4.77%→4.49%) cut against a simple AVOID read. Per
CLAUDE.md, Gate 0 does not halt the pipeline on company quality; this
finding propagates as a flag for stage 13 synthesis and the operator,
not as a stop.

```yaml
# report: runs/aye-2026-07-22/outputs/reports/01-gate0.md
stage: B01-gate0
company: "Aye Finance Limited (AYE)"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps:
  - "NIM/spread-yield not anchored in the four provided sources (digest-only: 15.94% Q1FY27, non-anchored)"
  - "Peer NBFC financial/market-cap data not provided; 6 of 12 moat tests (M2,M3,M5,M6,M7,M9) scored 0 as PEER DATA NEEDED"
  - "Q1FY27 (2246e44a) full P&L/balance-sheet line items NOT FOUND — OCR extract is character-per-line garbled; only the Annexure-1 summary ratio block was reconstructable"
  - "FY23 opening Total Assets / Net Worth (FY22 closing) not in the 3-year restated window; FY23 ROA/ROE computed on closing-only basis, stated"
  - "Contingent liabilities / Net Worth latest available only as at 30-Sep-2025 (restated IPO stub); no later breakout in the FY26 or Q1FY27 filings extracts provided"
  - "Selling-expense % not separately broken out in the anchored P&L (bundled in Other Expenses); M11 scored conservatively per the rule"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID is driven primarily by NBFC metric-scale mismatch in Blocks A/B under manufacturing-calibrated bands and by the LIMITED-history one-tier downgrade (4 FY periods, IPO Feb-2026), not by demonstrated fundamental deterioration. ICRA-anchored CRAR 42%, historically double-digit ROE (16.1% FY24), and 25% AUM CAGR (rating p.1) cut against a simple AVOID read; flagged for stage 13 human synthesis, not a stop."
  - type: FLAG-CASH
    reason: "Block B (cash generation) is INDETERMINATE, not a genuine failure — CFO is structurally negative every year for a balance-sheet lender funding loan-book growth via borrowings (Ind AS 7 classification). Per CLAUDE.md this caps any downstream verdict at PROCEED WITH CAVEATS minimum and must be named explicitly, not silently resolved to PROCEED."
  - type: FLAG-ASSET-QUALITY
    reason: "Gross Stage III/GNPA rose from 3.2% (Mar-24) to 4.77% (Mar-26 audited); 90+dpd breached ICRA's 5% rating sensitivity at 5.1% (Sep-25, rating p.2). Improved to 4.49% (Jun-26, results p.5/19) in the most recent two data points but this is not yet a demonstrated full asset-quality cycle."
  - type: FLAG-DATA
    reason: "Prospectus RESTATED FY24/FY25 PAT (Rs171.68cr/Rs175.25cr, annual report p.314) exceeds ICRA's originally-audited FY24/FY25 PAT (Rs161cr/Rs171cr, rating p.1) by ~6.6%/~2.3% - a restatement uplift. Both figures are independently anchored; the delta itself is not estimated. Flagged for operator awareness before relying on restated-basis growth CAGRs."
data_years: 4
fy_range: "FY23 to FY26"
blocks: {A: 5, B: 0, C: 20, D: 16, E: 11}
core_score: 52
moat_score: 7
grand_total: 59
moats_confirmed: 1
moat_class: "THIN"
classification: "AVOID"
deal_breakers:
  - "1: Block A=5 <8 -> cap GOOD (non-binding, already below)"
  - "2: Block B=0 <8 -> cap GOOD (non-binding)"
  - "3: median ROA=2.94% <10% (ROCE substitute) -> cap AVERAGE (binding but non-differentiating; median ROE=10.68% would NOT trigger this test)"
  - "4: cumulative CFO/PAT=-7.25x <0.50 -> cap AVERAGE (binding, tied to Block B INDETERMINATE read)"
history_downgrade: true
data_notes:
  - "PAT basis mismatch: Prospectus RESTATED PAT for FY24 (Rs171.68cr, annual report p.314) and FY25 (Rs175.25cr) exceeds ICRA's originally-audited PAT for FY24 (Rs161cr, rating p.1) and the FY26 filing's audited FY25 comparator (Rs171.27cr, results p.6/26) by ~Rs10.7cr (+6.6%) and ~Rs4cr (+2.3%) respectively - restatement uplift, both bases anchored."
  - "ROA/ROE FY23 computed on closing-only Total Assets/Net Worth (no FY22 opening balance in the 3-year restated window); likely understates true FY23 return - stated explicitly per formula rule."
  - "Block A (A1/A2): ROCE->ROA substitution structurally scores near-zero for any NBFC under manufacturing bands (ROA is inherently low single-digit vs. bands calibrated to double-digit manufacturing returns); ROE (A3, framework-native) used instead of ROA for the deal-breaker #3 median-return test."
  - "Block B is INDETERMINATE for a balance-sheet lender: CFO is structurally negative every year (loan disbursements = operating outflow under Ind AS 7). Literal formula scores B1-B3 at 0; this is not an earnings-quality or going-concern signal for an NBFC."
  - "B4, M4, M10, M12 marked NOT APPLICABLE - no trade receivables/inventory/payables concept for a balance-sheet lender. GNPA/dpd trend (Block D) is the correct lender analog and is deliberately not reused here to avoid crediting/debiting one quality signal through two mechanisms (CLAUDE.md)."
  - "M2,M3,M5,M6,M7,M9 = PEER DATA NEEDED - no peer NBFC financial or market-cap data was supplied in this run's four anchored sources; never guessed."
  - "D4 (current ratio) substituted with Liquidity Coverage Ratio (LCR): 205.16% FY26 (results p.11/26), 269.61% Q1FY27 (results p.5/19) - both far above the ~85-100% regulatory floor for NBFC-ML. Substitution named explicitly as it is not framework-specified (unlike D1/D2)."
  - "history_downgrade: 4 fiscal years (FY23-FY26 restated+audited) = LIMITED confidence band (3-4 yrs); classification downgraded one tier from the Core-score-implied AVERAGE to AVOID. Company IPO'd Feb-2026, so this reflects listing recency by construction, not disclosed-history quality problems - flagged for operator override consideration per CLAUDE.md's post-IPO rebase note (state which years drive the deal-breaker: all four, FY23-FY26, are the entirety of the company's disclosed financial history to date)."
  - "E1: no identifiable promoter (Prospectus, PE/VC-backed). FII+DII institutional stake (37.05% Mar-26 -> 35.45% Jun-26, operator-supplied screener shareholding) used as the alignment proxy in place of promoter holding, below the framework's >50% 'professionally managed' carve-out, scored via literal analogy to the 30-39.9% band. Per CLAUDE.md this must NOT be read as an institutional-absence risk signal - ~35-37% is a substantial institutional base for a small-cap NBFC."
  - "Q1FY27 (2246e44a) figures: only the Annexure-1 summary ratio block (Debt/equity 2.22x, net worth Rs2,528.01cr, PAT Rs74.50cr, total debt/assets 66.77%, net profit margin 15.22%, EPS 3.02/3.00, Gross Stage III 4.49%, Net Stage III 1.67%, PCR 63.80%, CRAR 42.38%, LCR 269.61%) was reconstructable from this heavily OCR-garbled filing; these figures are internally self-consistent (arithmetic ties) and directionally corroborated by the operator digest. Full Q1FY27 P&L/balance-sheet line items are NOT FOUND (anchored) - digest-only for AUM (Rs7,324cr)/NIM(15.94%) context."
block_b_trend: "deteriorating - CFO/PAT ratio improved from -18.1x (FY23) to -4.6x/-4.7x (FY25) then worsened to -7.0x (FY26), tracking accelerated loan-disbursement growth post-IPO capital infusion (AUM +26-27% YoY FY26), a growth-scale signal rather than a profitability-quality deterioration signal."
```
