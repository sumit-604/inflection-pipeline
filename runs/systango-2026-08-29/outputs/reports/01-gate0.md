# STAGE 1: GATE 0 SCORECARD — Systango Technologies Ltd (SYSTANGO)
Run date: 2026-08-29 | Model: claude-sonnet-5 | Mode: pipeline

Data available: 4 years of full, audited, granular detail (FY2023 to FY2026,
post-SME-listing consolidated statements: results filing + June-2026 investor
deck). A wider 7-year revenue/PAT trend also exists (FY2020 to FY2026,
screener-data), but FY2020-FY2022 predate the March-2023 NSE Emerge listing
and come from pre-IPO/RHP-era disclosure, not exchange-filed results, and
lack the balance-sheet granularity (current liabilities, trade payables,
capex) needed for ROCE, WC-days and FCF. Scoring below uses the 4-year
FY2023-FY2026 window for Blocks A, D, E and most of Block B (source: results
filing SYSTANGO_14052026200758_Intimation.pdf, June-2026 Investor
Presentation, and the FY2024-25 Annual Report). The 7-year window is used
only for Block B1 (CFO/PAT, both windows shown) and as supplementary
context for the C-block CAGR calculation. Scoring adapted to 4-year history
per the confidence table (3-4 years = LIMITED, one-tier downgrade applied
— see Classification).

**Source-file note**: the input filed as `Annual_Report_2023.pdf` is in fact
the 21st Annual Report, FY2024-25 (year ended 31-Mar-2025) — its own cover
page and auditor's report date (26-May-2025) confirm this. All AR anchors
below are cited as "AR FY24-25" regardless of the input filename.

**Basis note**: standalone (parent-only) and consolidated (parent +
Isystango UK, Systango INC USA) figures reconcile almost exactly at every
checkpoint tested (revenue, PBT, PAT, tax, receivables all match within
rounding). Consolidated is used as primary basis below; standalone is cited
where it is the only source (e.g. contingent liabilities, related-party
loan detail).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Source's own figures used (deck reports ROCE/ROE FY23-FY26 directly;
Investor_Presentation_1.pdf p.30 "Consolidated Financial Performance" —
ROCE/ROE chart). Not independently recomputed; deck's underlying
capital-employed base not disclosed.

| FY | ROCE (deck) | ROE (deck) |
|----|------------|------------|
| FY23 | 26.85% | 22.73% |
| FY24 | 26.88% | 21.56% |
| FY25 | 28.54% | 23.17% |
| FY26 | 33.00% | 27.00% |

(Investor_Presentation_1.pdf, p.30, "ROCE & ROE" chart)

Cross-check: AR FY24-25 Note 22(xiv)(d), standalone basis, gives ROE
(PAT ÷ average total equity) = 23.44% FY24, 26.10% FY25 (AR FY24-25 p.93) —
same order of magnitude as the deck's consolidated figures; standalone vs
consolidated basis difference noted, not reconciled further.

- **A1 Median ROCE**: sorted [26.85, 26.88, 28.54, 33.00] → median = 27.71%
  → ≥25% → **Score 5**
- **A2 Minimum single-year ROCE**: 26.85% (FY23) → ≥15% → **Score 5**
- **A3 Median ROE**: sorted [21.56, 22.73, 23.17, 27.00] → median = 22.95%
  → ≥20% → **Score 5**
- **A4 ROCE trend, latest (33.00%) vs earliest (26.85%)**: latest ≥ earliest
  → **Score 5**

**Block A = 20/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

- **B1 Cumulative CFO ÷ Cumulative PAT**

  Two windows computed; primary uses maximal anchored data (7-year,
  screener-data CFO and PAT, both fully available all 7 years):

  | FY | CFO (Rs cr) | PAT (Rs cr) |
  |----|------------|-------------|
  | FY20 | 3.75 | 2.52 |
  | FY21 | 7.26 | 5.68 |
  | FY22 | 3.38 | 6.84 |
  | FY23 | 5.13 | 13.99 |
  | FY24 | 8.69 | 16.93 |
  | FY25 | 12.38 | 23.73 |
  | FY26 | 33.77 | 31.88 |

  (screener-Data_Sheet.csv, "CASH FLOW" and "Sales/Net profit" rows)

  Cumulative FY20-26: CFO = 74.36 cr, PAT = 101.57 cr → ratio = **0.732**
  → 0.70-0.84 band → **Score 2** (primary)

  Post-listing alternate (FY23-26 only): CFO = 59.97 cr, PAT = 86.53 cr →
  ratio = **0.693** → 0.50-0.69 band → would score 1. Flagged in
  `block_b_trend` below — cash conversion is *improving* within this
  window, the cumulative ratio is dragged down by a weak FY23.

- **B2 FCF-positive years as proportion** (FY23-FY26, only window with a
  capex breakout available)

  Free Cash Flow (Rs mn, deck-reported, Investor_Presentation_1.pdf p.30
  "Free Cash Flow" chart): FY23 = 7, FY24 = 70, FY25 = 116, FY26 = 333.
  Cross-checked against results-filing cash flow statements: FY26 CFO
  337.66 mn − capex (PPE 4.52 mn + CWIP 0.90 mn) = 332.24 mn ≈ deck's 333
  (SYSTANGO_14052026200758_Intimation.pdf, consolidated cash flow); FY25
  CFO 123.84 mn − capex (PPE 3.14 + intangibles 1.22 + intangibles-under-dev
  3.91 mn) = 115.57 mn ≈ deck's 116 (same filing, comparative column).
  FY23/FY24 capex not independently verifiable from provided documents
  (no full FY23/FY24 cash flow statement in corpus); deck's own reported
  FCF used and anchored as the source's own figure.

  4/4 years positive → 100% → **Score 5**

- **B3 Cumulative FCF ÷ Cumulative PAT** (FY23-FY26)

  Cumulative FCF = 7+70+116+333 = 526 mn. Cumulative PAT (consolidated,
  same window) = 140+169+237+319 = 865 mn (SYSTANGO_14052026200758_
  Intimation.pdf and AR FY24-25 P&L). Ratio = 526/865 = **0.608** → ≥0.60
  → **Score 5**

- **B4 Change in WC Days, latest (FY26) vs earliest (FY23)**

  Inventory = 0 throughout (IT services, no inventory — confirmed CARO
  AR FY24-25 Annexure-A (ii)(a), p.64: "does not hold any physical
  inventories").

  | FY | Trade Rec. (mn) | Revenue (mn) | Rec. Days | Trade Pay. (mn) | Pay. Days | WC Days |
  |----|-----------------|--------------|-----------|-----------------|-----------|---------|
  | FY23 | 65 | 523 | 45.35 | 2 | 1.40 | 43.95 |
  | FY24 | 107 | 566 | 69.00 | 1 | 0.64 | 68.35 |
  | FY25 | 155 | 671 | 84.30 | 4 | 2.18 | 82.13 |
  | FY26 | 118 | 904 | 47.63 | 10 | 4.04 | 43.59 |

  (Investor_Presentation_1.pdf p.21-32, consolidated balance sheet detail;
  cross-checked against screener-Data_Sheet.csv receivables row, which
  matches to within rounding for all 4 years)

  Change = 43.59 − 43.95 = **−0.36 days** → within ±5 days → **Score 3**.
  Note: the net change masks a large intra-period swing (45→69→84→48
  days) — receivable days more than doubled into FY24-25 before
  normalising in FY26. Plausibly tied to the ~46-48% top-3 client
  concentration reported for H1FY26 (per SPEAR priority items).

**Block B = 2+5+5+3 = 15/20**

`block_b_trend`: **improving** — quarterly-year CFO/PAT ratio rose from
0.37x (FY23) to 1.06x (FY26); FY26 is the first year CFO exceeded PAT.

---

## BLOCK C: GROWTH (Max 20)

Primary window: FY2023-FY2026 (post-listing, 3-year CAGR), matching the
deck's own stated "3 Year Revenue CAGR 20%" / "3 Year PAT CAGR 32%"
(Investor_Presentation_1.pdf, snapshot page). Independently recomputed
from screener-Data_Sheet.csv:

- Revenue: FY23 = 52.34 cr → FY26 = 90.38 cr, 3 years → CAGR = (90.38 /
  52.34)^(1/3) − 1 = **19.97%** ≈ deck's stated 20%.
- PAT: FY23 = 13.99 cr → FY26 = 31.88 cr, 3 years → CAGR = (31.88 /
  13.99)^(1/3) − 1 = **31.6%** ≈ deck's stated 32%.

Supplementary 7-year context (FY2020-FY2026, screener-data): revenue CAGR
= (90.38/14.28)^(1/6)−1 = **36.0%** — materially higher, but distorted by
a tiny FY20 base (Rs 14.28 cr) from the pre-listing era; not used for
scoring.

- **C1 Revenue CAGR**: 19.97% (rounds to deck's stated 20%) → ≥20% band
  → **Score 5**
- **C2 PAT CAGR**: 31.6% → ≥20% → **Score 5**
- **C3 Positive YoY revenue years**: all 6 YoY comparisons FY21-FY26
  positive (FY20-26 screener data) = 100% → **Score 5**
- **C4 PAT CAGR − Revenue CAGR**: 31.6% − 19.97% = **+11.6pp** → ≥+3pp →
  **Score 5**

No CAGR edge cases triggered — no negative/zero endpoints, no loss-to-
profit swing (PAT positive every year FY2020-FY2026).

**Block C = 20/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Latest = FY2026 (audited consolidated, SYSTANGO_14052026200758_
Intimation.pdf, consolidated balance sheet, year ended 31-Mar-2026, Rs
lakh): Shareholders' funds 13,546.65; Long-term borrowings 6.26; no
short-term borrowings line; Trade payables 103.65 + Other current
liabilities 97.33 + Short-term provisions 1,295.92 = Total current
liabilities 1,496.90; Total assets 15,049.81; Current assets 10,768.90;
Cash & cash equivalents 1,573.43.

- **D1 Net Debt ÷ EBITDA**: Total debt 6.26 lakh vs Cash 1,573.43 lakh →
  net cash position → **Score 5**
- **D2 Interest Coverage (EBIT ÷ Interest)**: EBIT = PBT 3,917.78 +
  Finance cost 6.0 − Other income 594.12 = 3,329.66 lakh; Interest
  (screener-Data_Sheet.csv, FY26) = 6 lakh → coverage ≈ 555x → ≥10x →
  **Score 5**
- **D3 Debt ÷ Equity**: 6.26 / 13,546.65 = 0.0005 → <0.1 → **Score 5**
- **D4 Current Ratio**: 10,768.90 / 1,496.90 = 7.19x → ≥2.0 → **Score 5**

Cross-check (standalone, AR FY24-25 Note 22(xiv), FY25): Current Ratio
10.79x, Debt Equity Ratio "Not Applicable" (zero debt) — consistent
direction, standalone figures even stronger than consolidated (parent
carries essentially no trade payables at all: Note 4, both FY24 and FY25
= "-").

**Block D = 20/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Most recent promoter shareholding data available in the provided corpus is
**as at 31-Mar-2025** (AR FY24-25, Note 1, p.76) — no later shareholding
pattern filing is present. This is 17 months stale relative to the
29-Aug-2026 run date; flagged as a data gap, not treated as "latest
quarter."

- **E1 Promoter holding (most recent available, 31-Mar-2025)**: Vinita
  Rathi 36.32% + Nilesh Rathi 35.69% + Priyesh Rathi 0.06% + Suresh Chand
  Rathi 0.00% + Mayur Khandelwal 0.01% = **72.07%** total promoter group
  (AR FY24-25 p.76, Note 1D) → ≥60% → **Score 5**
- **E2 Promoter holding change**: available window is 2 years, not 3
  (AR only tabulates 31-Mar-2023 / 2024 / 2025): 71.96% (FY23) → 71.96%
  (FY24, unchanged) → 72.07% (FY25) (AR FY24-25 p.76, Notes 1D & 1E) →
  net change over the available window = **+0.11pp** → within ±1% →
  **Score 3**
- **E3 Promoter pledge**: **N/A (not in provided data)**. This AR states
  SEBI LODR Schedule V Para C corporate-governance disclosures (which
  would normally carry pledge detail) do not apply because the company is
  listed on the SME Emerge platform (AR FY24-25 Board's Report, corporate
  governance note). No pledge percentage found in any provided document.
  Scored 0 per the grounding rule — **this reflects a data gap, not a
  confirmed pledge.** → **Score 0**
- **E4 Contingent liabilities ÷ Net Worth**: Standalone Contingent
  Liabilities (claims, guarantees, other contingent money) = **NIL** for
  both FY24 and FY25 (AR FY24-25 p.88, Note 21C.4) → 0% → <5% →
  **Score 5**

**Block E = 5+3+0+5 = 13/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

- **M1 Pricing Power**: EBITDA margin FY23→FY26: 30.2%→37.6% (deck p.30,
  "EBITDA Margin"), +7.4pp expansion, ≥2pp; revenue CAGR 19.97% ≥10% →
  **Score 5**
- **M2 Cost Advantage vs peer median**: no peer EBITDA-margin data
  provided in corpus → **PEER DATA NEEDED → Score 0**
- **M3 Capital Efficiency**: FAT (Revenue ÷ Net Block) FY26 = 90.38cr /
  4.93cr (screener-Data_Sheet.csv) = 18.3x, FAT>3x; ROCE FY26 = 33% >20%
  → **Score 5**
- **M4 Customer Stickiness**: zero revenue-decline years (FY20-26), but
  receivable days NOT stable ±10 (swung 45→84→48 days, Block B4 table
  above) → top band's dual condition not fully met; closest matching band
  = "max 1 decline year, fully recovered" → **Score 3**
- **M5 Scale & Dominance**: no peer market-cap/segment ranking data
  provided → **PEER DATA NEEDED → Score 0**
- **M6 Technology/R&D**: R&D as % of revenue not disclosed separately in
  any provided document → **N/A → Score 0**
- **M7 Regulatory/License**: IT/software services, unregulated segment,
  no license/quota → **Score 0**
- **M8 Distribution**: B2B software services, no physical distribution
  network; not quantified → **Score 0**
- **M9 Brand**: Gross-margin proxy = (Revenue − Employee Cost) ÷ Revenue
  (employee cost used as the primary input-cost proxy for an IT services
  business; no material cost line applicable) = (90.38−39.33)/90.38 =
  56.5% FY26 (screener-Data_Sheet.csv). No peer median GM available to
  compare against → **PEER DATA NEEDED → Score 0**
- **M10 Switching Costs**: revenue grew every year FY20-26 AND net
  receivable-days change over FY23-FY26 = +2.28 days (45.35→47.63), ≤10
  days → **Score 5** (intra-period volatility noted above as context, not
  penalised here since the test is defined on net change over the
  period)
- **M11 Network Effects**: 7 years available (≥6, two-window test
  applies). Latest 3yr revenue CAGR (FY23-26) = 19.97% vs prior 3yr CAGR
  (FY20-23) = 54.2% (screener-Data_Sheet.csv) — latest CAGR is LOWER than
  prior, i.e. decelerating, not accelerating; selling-expense % trend for
  FY23-26 not separately disclosed (screener's "Selling and admin" row is
  blank from FY23 onward) → top and middle bands fail → **Score 0**.
  Deceleration off a shrinking base is an expected scaling pattern, not
  necessarily adverse — noted, not penalised further.
- **M12 Negative WC / Float**: WC days (Block B4 table): FY23=43.95,
  FY24=68.35, FY25=82.13, FY26=43.59 — no negative-WC years, 2/4 years
  >45 days, 2/4 (incl. latest, FY26) in the 15-45 band → scored on the
  latest, most decision-relevant year → **Score 1**

**Block F (moat) = 5+0+5+3+0+0+0+0+0+5+0+1 = 19/60**

Moats "present" (score ≥3): M1, M3, M4, M10 = **4 moats confirmed**

**Moat classification: 4-5 present = STRONG**

---

## CLASSIFICATION AND OVERRIDES

**Core score** (Blocks A+B+C+D+E) = 20+15+20+20+13 = **88/100**
**Moat score** (Block F) = **19/60**
**Grand total** = 88+19 = **107/160**

### Deal-breaker check (none triggered)
1. Block A <8 → Block A = 20 → not triggered
2. Block B <8 → Block B = 15 → not triggered
3. median ROCE <10% → 27.71% → not triggered
4. cumulative CFO/PAT <0.50 → 0.732 (7yr) / 0.693 (4yr alt) → not
   triggered under either window
5. pledge >15% → status unknown (NOT FOUND), not a confirmed breach; not
   triggered, but flagged as a gap (see E3, and flags below)
6. ND/EBITDA >3x AND IC <3x → net cash position → not triggered
7. revenue declined majority of years → never declined → not triggered
8. PAT negative in any of last 3 years → positive every year FY20-26 →
   not triggered
9. history <3 years → 4-year primary scoring window → not triggered as a
   hard deal-breaker, but the confidence-band downgrade below applies

**deal_breakers: []**

### Data confidence / history downgrade
Primary scoring window = 4 years (FY2023-FY2026) → **3-4 years = LIMITED
band → one-tier classification downgrade applies** (per operator
instruction to flag short history for this recently-listed, SME-platform
name; listed Mar-2023, first full FY as a listed entity FY24).
**history_downgrade = true**

### Classification matrix
Core = 88 (≥80) + Moat = STRONG → matrix says **EXCELLENT** → downgraded
one tier for LIMITED history → **Classification = GOOD+**

---

## STRONGEST / WEAKEST BLOCK

**Strongest**: Blocks A, C, D — each 20/20 (return on capital, growth, and
balance sheet strength are all unambiguous over the 4-year audited
window: zero debt, ROCE 27-33%, revenue/PAT CAGR ~20%/32%, never a
down-year).

**Weakest**: Block E (13/20) — driven by an unconfirmed pledge status
(data gap, not a known breach) and only marginal promoter accumulation
(+0.11pp over 2 years). Block B (15/20) is the next-weakest, dragged by a
sub-1.0x cumulative CFO/PAT ratio, though the year-by-year trend within
that block is clearly improving (0.37x FY23 → 1.06x FY26).

---

## DECISION LINE

GOOD+ on a 4-year audited, post-listing window: unambiguous returns
(ROCE 27-33%, ROE 21-27%), zero debt, ~20% revenue CAGR / 32% PAT CAGR,
and a cash-conversion trend that is recovering fast (CFO now exceeds PAT
in the latest year). The classification is capped one tier below what the
raw score would otherwise support (EXCELLENT) purely because the audited
public-company track record is short (LIMITED band). Four items outside
the numeric formula are load-bearing for the next stage and are carried
forward as flags: unsecured, no-security, on-demand loans of Rs 5.30cr to
undisclosed non-related "Others" that are growing year over year;
gratuity/leave encashment recognised on a cash basis rather than accrued
(profit comparability caveat, unquantified); a large gap between an
earlier revenue guide (~Rs 250cr / $25M by FY26) and FY26 actual delivery
(Rs 90.38cr), even as EBITDA-margin guidance was beaten; and a promoter
shareholding data point that is 17 months stale with pledge status
unconfirmed.

---

```yaml
stage: B01-gate0
company: "SYSTANGO"
run_date: "2026-08-29"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Promoter pledge %: NOT FOUND in any provided document (E3 scored 0 on data-availability grounds)"
  - "Promoter shareholding: most recent available is 31-Mar-2025 (AR FY24-25), 17 months stale vs run date; no later shareholding pattern in corpus"
  - "FY2020-FY2022 balance-sheet granularity (trade payables, current-liability split, capex breakout) not available; those years excluded from Blocks A/B(FCF)/D/E scoring"
  - "Peer comparison data (EBITDA margin, market cap/segment ranking, gross margin) not provided: affects M2, M5, M9 (all scored 0, PEER DATA NEEDED)"
  - "R&D as % of revenue not separately disclosed: M6 scored 0"
  - "Selling-expense % trend FY23-FY26 not separately disclosed (screener row blank from FY23): affects M11 second-tier test"
flags:
  - {type: FLAG-CASH, reason: "Unsecured, no-security, on-demand loans to unnamed non-related 'Others' grew to Rs 5.30cr outstanding at FY25 close (Rs 2.18cr freshly advanced during FY25 alone) from Rs 4.55cr at FY24 close (CARO Annexure-A AR FY24-25 p.65-66; Note 14/14.1 p.83); operating cash is being extended to undisclosed counterparties."}
  - {type: FLAG-ACCOUNTING, reason: "Gratuity and leave encashment recognised on cash/payment basis, not accrued (AR FY24-25 Note 21B.7, p.86); reported profit not directly comparable to accrual-basis peers, unrecognised liability quantum undisclosed."}
  - {type: FLAG-DATA-GAP, reason: "Promoter pledge status and current shareholding both unconfirmed/stale (see input_gaps); E3 scored 0 is a data gap, not a known pledge breach."}
  - {type: FLAG-GUIDANCE, reason: "Prior revenue guidance of ~Rs 250cr ($25M) by FY26 vs FY26 actual Rs 90.38cr (screener-data; SYSTANGO_14052026200758_Intimation.pdf), roughly a 64% miss, while EBITDA-margin guidance (>25%) was exceeded (37.6% actual, deck p.30). Outside Gate 0's numeric formula; load-bearing for downstream credibility work per SPEAR priority."}
data_years: 4
fy_range: "FY2023 to FY2026"
blocks: {A: 20, B: 15, C: 20, D: 20, E: 13}
core_score: 88
moat_score: 19
grand_total: 107
moats_confirmed: 4
moat_class: "STRONG"
classification: "GOOD+"
deal_breakers: []
history_downgrade: true
data_notes:
  - "No loss-to-profit PAT swing: PAT positive every year FY2020-FY2026 (screener-Data_Sheet.csv)"
  - "M9 gross-margin proxy used: (Revenue - Employee Cost) / Revenue, employee cost as input-cost proxy for IT services (no material cost line applicable)"
  - "PEER DATA NEEDED: M2, M5, M9 all scored 0 for lack of peer comparison data in corpus"
  - "Block B1 computed on two windows: 7yr (FY20-26) cumulative CFO/PAT = 0.732, score 2 (primary, maximal anchored data); 4yr post-listing (FY23-26) alternate = 0.693, would score 1 -- both reported, primary used"
  - "Block C1/C2 CAGR computed on two windows: primary 3yr FY23-26 (~20% revenue / ~32% PAT, matches deck's own stated figures) used for scoring; supplementary 7yr FY20-26 (36.0% revenue) not used, distorted by tiny pre-listing FY20 base"
  - "Input file 'Annual_Report_2023.pdf' is actually the 21st Annual Report FY2024-25 (year ended 31-Mar-2025); all AR anchors above cite it as AR FY24-25"
  - "WC days: net change latest-vs-earliest (-0.36 days) masks a large intra-period swing (45 to 84 to 48 days, FY23-FY26); plausibly tied to client concentration (SPEAR priority item, ~46-48% top-3 concentration reported H1FY26)"
  - "Parent-only (standalone) trade payables are NIL for both FY24 and FY25 (AR FY24-25 Note 4, p.78); the small non-zero consolidated payables used in WC-days calc come from subsidiary-level balances"
block_b_trend: "improving -- CFO/PAT ratio rose from 0.37x (FY23) to 1.06x (FY26), first year CFO exceeded PAT"
analyst_note: "Classification is GOOD+, one tier below what the raw score (Core 88 + STRONG moat) would otherwise support, solely on the LIMITED history band (4-year audited window, SME listing Mar-2023). The financial picture itself is clean: zero debt, ROCE 27-33%, ~20%/32% revenue/PAT CAGR, no down-year ever. Four qualitative items are more decision-relevant than the numeric score suggests and should carry forward: (1) growing unsecured loans to undisclosed non-related parties (Rs 5.30cr, CARO-confirmed) -- a capital-allocation and disclosure-quality question independent of Section 1B mechanics; (2) cash-basis gratuity/leave accounting -- profit is not accrual-clean, quantum unknown; (3) a large revenue-guidance miss (~64%) alongside an EBITDA-margin guidance beat, which is a mixed signal on management credibility worth resolving before FTTCP; (4) promoter data is 17 months stale with pledge unconfirmed. None of these are deal-breakers under the Gate 0 formula, but all four should be named explicitly in the Halt-1 dossier."
```
