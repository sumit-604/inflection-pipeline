# GATE 0 SCORECARD — Millworks Technologies Limited (MILLWORKS)
Run date: 2026-08-22 | Stage: B01-gate0 | Model: claude-sonnet-5

Data available: 3 years (FY24 to FY26). Scoring adapted to 3-year history.

## DATA SOURCE NOTE (read before the numbers below)

Two source files were provided:
1. `screener-Data_Sheet.csv` — only populated main screener sheet (P&L,
   Balance Sheet, Cash Flow, Quarters CSVs are empty).
2. RHP (Red Herring Prospectus, filed 2026-07-07) — contains the audited
   **Restated Financial Statements**. These restated statements cover only
   **FY24, FY25 and FY26** (RHP p.55-57, Annexure I/II/III). The company
   was incorporated in 2021 (CIN U29200KA2021PLC153863) and the RHP does
   not restate FY22 or FY23. The RHP substitutes for the annual report on
   this run, per orchestrator instruction.

Reconciliation finding: the Data_Sheet.csv column layout is misleading.
It shows five date headers (FY22-FY26) but only four data values per row.
Cross-matching the values against the RHP restated P&L (Revenue FY24 =
₹9.386cr / FY25 = ₹22.10cr / FY26 = ₹148.767cr, RHP p.56) proves the four
Data_Sheet values are right-aligned to **FY23-FY26**, not FY22-FY25 as the
task brief assumed. FY22 has no data anywhere in Data_Sheet. Data_Sheet's
FY23 figures (Sales ₹1.77cr, Net Profit ₹0.33cr) are **not corroborated by
any RHP restated statement** (RHP restated history starts at FY24) and are
therefore excluded from all scored formulas below; they are noted as
unverified/secondary only. All scored metrics use the RHP restated 3-year
window FY24-FY26, which is the only audited, anchor-grade data available.

sector_cap_row flag: the run manifest's "Pharma / CDMO" sector tag is
confirmed WRONG. The RHP's own peer set (Unimech Aerospace and
Manufacturing Ltd, Azad Engineering Ltd — RHP p.94-95) and AS9100D /
ISO 9001:2015 quality certification (RHP p.158) and SCOMET export-control
references (RHP p.~112) identify the actual business as precision-machined
components for Defence, Railways, Aerospace and Semiconductors.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 20/20

All ROE/ROCE figures below are the RHP's own source-computed figures
(RHP p.98-99, "Key Performance Indicators"; cross-verified against RHP
p.234, "Significant Accounting Ratios" annexure) — used per the formula
rule that a source-provided ROCE/ROE is used directly, not recomputed.

| Metric | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| ROCE | 38.61% | 23.02% | 56.44% | RHP p.98-99 / p.234 |
| ROE | 144.46% | 40.94% | 69.94% | RHP p.98-99 / p.234 |

- A1 Median ROCE = 38.61% (sorted 23.02/38.61/56.44) → ≥25% → **5/5**
- A2 Minimum single-year ROCE = 23.02% (FY25) → ≥15% → **5/5**
- A3 Median ROE = 69.94% (sorted 40.94/69.94/144.46) → ≥20% → **5/5**
- A4 ROCE trend, latest (FY26=56.44%) vs earliest (FY24=38.61%): latest ≥
  earliest (dipped to 23.02% in FY25, recovered above FY24 by FY26) → **5/5**

Cross-check (self-computed, standard formula EBIT/(Total Assets − Current
Liabilities), RHP p.55-56): ROCE FY24=85.86%, FY25=26.08%, FY26=58.94% —
directionally different trend (shows decline FY24→FY26) because the RHP's
own Capital Employed definition is "Tangible net-worth + total debt +
deferred tax liabilities" (RHP p.98, note 9), not Total Assets − Current
Liabilities. Per the formula rule, the source-provided figure governs; the
divergence is noted here for transparency and does not change the score
mechanically, but the analyst should be aware A4 is sensitive to which
capital-employed definition is used (score would be 0/20 for A4 under the
standard-formula version instead of 5/20).

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20

| Metric | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| CFO (₹cr) | 0.65 | -2.92 | -10.76 | RHP p.57, Annexure III |
| PAT (₹cr) | 1.95 | 5.25 | 37.06 | RHP p.56, Annexure II |
| Capex (₹cr, PPE+intangibles, excl. acquisitions) | 2.69 | 9.31 | 7.79 | RHP p.57 |
| FCF (₹cr) = CFO − Capex | -2.04 | -12.22 | -18.56 | computed |

- Cumulative CFO (FY24-26) = 0.65 − 2.92 − 10.76 = **-13.03cr**
- Cumulative PAT (FY24-26) = 1.95 + 5.25 + 37.06 = **44.27cr**
- B1 Cumulative CFO ÷ Cumulative PAT = -13.03/44.27 = **-0.29** → <0.50 → **0/5**
- B2 FCF-positive years: 0 of 3 (all three years negative FCF) = 0% → <50% → **0/5**
- B3 Cumulative FCF ÷ Cumulative PAT = -32.82/44.27 = **-0.74** → negative → **0/5**
- B4 Change in WC Days, latest vs earliest (see table below) = +55.1 days → increased >15 → **0/5**

Working Capital Days (Revenue basis; RHP does not disclose a standalone
COGS line, only Cost of Material Consumed, so Revenue basis used
throughout per formula rule; closing balances from RHP p.55, Annexure I):

| | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| Trade Receivables (₹L) | 188.22 | 680.65 | 13,868.68 | RHP p.55 |
| Inventory (₹L) | 361.01 | 751.20 | 1,146.60 | RHP p.55 |
| Trade Payables (₹L) | 199.22 | 437.27 | 7,223.36 | RHP p.55 |
| Receivable Days | 73.2 | 112.4 | 340.3 | computed |
| Inventory Days | 140.4 | 124.1 | 28.1 | computed |
| Payable Days | 77.5 | 72.2 | 177.2 | computed |
| **WC Days** | **136.1** | **164.3** | **191.2** | computed |

**Earnings-quality red flag (drives Block B to zero and trips deal-breaker
#4):** FY26 closing trade receivables (₹138.69cr) equal 93% of FY26
revenue (₹148.77cr) — receivable days jumped from 73 to 340 in two years.
The RHP itself discloses (p.93): "certain receivables for fiscal 2026 are
linked to arrangements with Quik Pay Private Limited, where collections
depend on their receipt of funds... subject to completion of ongoing
customer testing processes." Peer receivable days for context (RHP p.93):
Azad Engineering 155-165 days, Unimech Aerospace 44-92 days, industry
average ~129 days — Millworks FY26 is more than double the stated
industry average. Every rupee of FY24-26 growth has been financed
externally: net financing cash inflow was +₹2.00cr (FY24), +₹13.27cr
(FY25), +₹27.17cr (FY26) (RHP p.57) against cumulative negative CFO.

---

## BLOCK C: GROWTH (Max 20) — Score: 20/20

| Metric | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| Revenue (₹cr) | 9.386 | 22.100 | 148.767 | RHP p.56 |
| PAT (₹cr) | 1.954 | 5.249 | 37.064 | RHP p.56 |

- C1 Revenue CAGR (FY24→FY26, n=2) = (148.767/9.386)^0.5 − 1 = **+298.1%** → ≥20% → **5/5**
- C2 PAT CAGR (FY24→FY26, n=2) = (37.064/1.954)^0.5 − 1 = **+335.5%** → ≥20% → **5/5**
- C3 Positive YoY revenue years: FY25>FY24 ✓, FY26>FY25 ✓ = 2/2 = 100% → **5/5**
- C4 PAT CAGR − Revenue CAGR = 335.5% − 298.1% = **+37.4pp** → ≥+3pp → **5/5**

Note: no CAGR edge case applies — both endpoints positive, no loss-to-profit
swing (PAT positive in all three restated years).

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 15/20

Latest = FY26. Not a bank/NBFC/Insurance company; standard bands apply.

| Metric | FY26 value | Source | Score |
|---|---|---|---|
| D1 Net Debt ÷ EBITDA | 15.6666 / 56.3043 = **0.28x** | Borrowings & Cash: RHP p.55; EBITDA: RHP p.98 | 0-1.0x → **4/5** |
| D2 Interest Coverage (EBIT÷Interest) | 53.352 / 3.4006 = **15.69x** | EBIT=EBITDA−Dep, RHP p.56/98 | ≥10x → **5/5** |
| D3 Debt ÷ Equity | **0.21** | RHP p.98 (KPI table) / p.234 (source-provided) | 0.1-0.5 → **4/5** |
| D4 Current Ratio | **1.43** | RHP p.234 (Significant Accounting Ratios annexure, source-provided) | 1.2-1.49 → **2/5** |

Supporting figures: Total borrowings FY26 = LT ₹7.87cr + ST ₹9.15cr =
₹17.02cr (RHP p.55); Cash & Bank FY26 = ₹1.35cr (RHP p.55); Net Debt =
₹15.67cr. Net worth FY26 = ₹82.67cr (RHP p.98). Current Ratio trend for
context: FY24=0.96 → FY25=1.99 → FY26=1.43 (RHP p.234) — the balance
sheet strengthened sharply around the FY25 pre-IPO capital raise, then
current ratio eased back down in FY26 as current liabilities (mostly
trade payables, up to ₹72.23cr) grew faster than current assets.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 15/20

| Metric | Value | Source | Score |
|---|---|---|---|
| E1 Promoter (+ Promoter Group) holding | **65.08%** pre-issue (Promoter 59.22% + Promoter Group entity V3 Technologies 5.86%) | RHP p.79 | ≥60% → **5/5** |
| E2 Promoter holding change, 3yr | N/A (not in provided data) | no historical shareholding pattern supplied; RHP gives only a single pre-issue snapshot dated 2026-07-07 | **0/5** |
| E3 Promoter pledge | **0%** — "none of the Equity Shares held by our Promoters are pledged" | RHP p.81 (and repeated p.~90, p.~93) | **5/5** |
| E4 Contingent Liabilities ÷ Net Worth | 8.45L / 8,266.99L = **0.10%** | Contingent liabilities RHP p.58; Net worth RHP p.98 | <5% → **5/5** |

Caveat on E1: post-issue promoter % is shown as "[●]" (placeholder) in the
RHP — not finalized at filing. Pre-issue 65.08% is the best available
anchored figure; post-listing dilution from the fresh issue will lower it,
direction unknown from this document. Committed lock-in requirements
(SEBI ICDR minimum promoter contribution, 3-year lock-in, RHP p.81-82)
apply but the post-issue percentage itself is not disclosed here.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 11/60

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | **5/5** | EBITDA margin (RHP p.98, % of total income) FY24=29.55% → FY26=36.71%, expanded +7.16pp; Revenue CAGR +298.1% ≥10%. Both conditions met. |
| M2 Cost Advantage vs peers | **0/5** | PEER DATA NEEDED — RHP peer table (p.94-95, Unimech/Azad) discloses EPS, P/E, RoNW, NAV, Total Income only; no peer EBITDA margin disclosed. |
| M3 Capital Efficiency | **5/5** | FAT (FY26) = Revenue 148.767cr / Net Fixed Assets (PPE+Intangibles, RHP p.55) 25.08cr = 5.93x >3x; ROCE FY26=56.44% >20%. Both met. |
| M4 Customer Stickiness | **1/5** | Zero revenue-decline years (0/2), but receivable days are the opposite of stable (+267 days FY24→FY26, RHP p.55/93) — fails the "stable ±10 days" leg of the top tier; scored low given the scale of the collections deterioration and the third-party (Quik Pay) collection contingency disclosed at RHP p.93. |
| M5 Scale & Dominance | **0/5** | PEER DATA NEEDED — only 2 named peers disclosed (RHP p.94-95); no market-cap ranking across the full listed segment universe is available to test "largest/top 3/top 5". |
| M6 Technology / R&D | **0/5** | N/A (not in provided data) — RHP describes an "in-house R&D function" qualitatively (p.~139, p.~150) but discloses no R&D spend or R&D/Revenue % anywhere in the document. |
| M7 Regulatory / License | **0/5** | PEER DATA NEEDED — segment is regulated (AS9100D/ISO9001:2015 certification RHP p.158; SCOMET export controls referenced) but RHP's own Competition section (p.159) describes "domestic and international manufacturers... large organized manufacturers and mid-sized enterprises" with no count of listed players in the segment. |
| M8 Distribution | **0/5** | Not applicable — direct B2B manufacturing/OEM supply model, no outlet/distribution-network concept in the business (RHP p.120+, Our Business). |
| M9 Brand | **0/5** | PEER DATA NEEDED — no peer gross-margin disclosure to benchmark against. Company's own GM proxy (Revenue − Material Cost)/Revenue for reference only: FY24=73.0%, FY25=52.0%, FY26=48.9% (declining trend; RHP p.56), not scoreable without a peer median. |
| M10 Switching Costs | **0/5** | Revenue grew every year (2/2), but receivable days rose 267 days over the window, far beyond the ≤10-day ceiling required at any scoring tier that pairs with 100%/near-100% growth consistency; none of the defined tiers is met — falls to "else". |
| M11 Network Effects | **0/5** | Only 3 years available (test requires ≥6 for the two-window comparison); scored conservatively per the rule for short history. Selling/distribution expense is not separately broken out in the RHP P&L, so the "selling % declining/rising" leg cannot be tested. Business model (B2B precision component supply) also shows no structural network-effect economics. |
| M12 Negative WC / Float | **0/5** | WC Days FY24=136.1, FY25=164.3, FY26=191.2 — all >45 days in every year, and rising. |

**Moats confirmed (score ≥3): 2 — M1 (Pricing Power), M3 (Capital Efficiency).**
Moat classification: 2-3 confirmed → **MODERATE**

Moat profile:
```
M1  Pricing Power        █████ 5/5  CONFIRMED
M2  Cost Advantage       ----- 0/5  PEER DATA NEEDED
M3  Capital Efficiency   █████ 5/5  CONFIRMED
M4  Customer Stickiness  █---- 1/5
M5  Scale & Dominance    ----- 0/5  PEER DATA NEEDED
M6  Technology / R&D     ----- 0/5  N/A (not disclosed)
M7  Regulatory / License ----- 0/5  PEER DATA NEEDED
M8  Distribution         ----- 0/5  N/A (not applicable)
M9  Brand                ----- 0/5  PEER DATA NEEDED
M10 Switching Costs      ----- 0/5
M11 Network Effects      ----- 0/5  <6yr history
M12 Negative WC / Float  ----- 0/5
```

---

## SCORECARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 20 | 20 |
| B — Cash Generation Quality | 0 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 15 | 20 |
| E — Shareholder Alignment | 15 | 20 |
| **Core Score** | **70** | **100** |
| F — Quantitative Moat | 11 | 60 |
| **Grand Total** | **81** | **160** |

Strongest block: **C — Growth (20/20)**, closely followed by A — Return on
Capital (20/20, but see the ROCE-definition caveat above).
Weakest block: **B — Cash Generation Quality (0/20)** — every sub-metric
scored zero; this is the block that drives the deal-breaker overrides
below.

---

## CLASSIFICATION

Data confidence: 3 years of restated history → **LIMITED band (3-4 yrs)**
→ classification downgraded one tier per the data-confidence rule.
`history_downgrade = true`.

Matrix (before overrides): Core 70 (60-79 band) + Moat MODERATE →
**GOOD** (native matrix result).

Deal-breaker overrides triggered:
1. Block B = 0 (<8) → caps classification at max **GOOD** (FY24-FY26, all
   three years of the only restated history available).
2. Cumulative CFO ÷ Cumulative PAT = -0.29 (<0.50) → caps classification
   at max **AVERAGE** (FY24-FY26 cumulative; driven almost entirely by
   FY25 and FY26, where CFO went to -₹2.92cr and -₹10.76cr respectively
   against rising PAT).

Deal-breakers NOT triggered: Block A ≥8 (20/20); median ROCE 38.61%
(≥10%); pledge 0%; ND/EBITDA 0.28x with IC 15.69x (nowhere near the
AVOID trigger); no revenue decline in any year; PAT positive all 3 years;
history = 3 years (not <3, so rule 9 itself does not fire — but the
separate LIMITED-history downgrade below still applies).

Applying, in order: matrix (GOOD) → strictest deal-breaker cap (max
AVERAGE) → LIMITED-history one-tier downgrade (AVERAGE → **AVOID**).

```
┌─────────────────────────────────────────────┐
│  CLASSIFICATION: AVOID                       │
│  Core Score: 70/100  |  Moat: MODERATE (2)   │
│  Grand Total: 81/160                         │
│  Capped by: cumulative CFO/PAT < 0.50x       │
│  Downgraded: LIMITED history (3 yrs)         │
└─────────────────────────────────────────────┘
```

**Decision line:** Explosive, cleanly-anchored revenue and PAT growth
(RHP-restated, audited) sits on top of three straight years of negative
operating cash flow that is getting worse, not better, plus an FY26
receivables balance equal to 93% of revenue with a disclosed third-party
collection contingency (Quik Pay Pvt Ltd, pending customer testing). Only
3 audited years exist for a company incorporated in 2021. Per pipeline
rule, this does not halt the run — it flags forward. Downstream stages
should treat the cash-conversion picture as the central open question,
not the growth numbers, which are unambiguous and well anchored.

---
```yaml
stage: B01-gate0
company: "MILLWORKS"
run_date: "2026-08-22"
model: claude-sonnet-5
status: complete
input_gaps:
  - "RHP restated financial statements cover only FY24-FY26 (Annexure I/II/III, RHP p.55-57); company incorporated 2021, no FY22 or FY23 audited restated data exists in this filing"
  - "screener-Data_Sheet.csv column alignment required manual correction: 5 date headers (FY22-FY26) but only 4 data values per row, right-aligned to FY23-FY26; verified against RHP restated Revenue (FY24/25/26 match exactly); FY22 has no Data_Sheet values at all"
  - "Data_Sheet FY23 figures (Sales 1.77cr, Net Profit 0.33cr) are NOT corroborated by any RHP restated statement and were excluded from scoring as unverified/secondary"
  - "screener P&L/Balance_Sheet/Cash_Flow/Quarters CSVs are empty; only Data_Sheet populated, used only as secondary cross-check per orchestrator instruction"
  - "No shareholding-pattern history available (RHP gives one pre-issue snapshot dated 2026-07-07 only) — E2 scored 0, N/A"
  - "Peer EBITDA margin, peer gross margin, and full listed-peer-count for the precision-components segment not available beyond the 2-company RHP comparison set (Unimech Aerospace, Azad Engineering) — M2, M5, M7, M9 scored 0, PEER DATA NEEDED"
  - "R&D spend as % of revenue not quantified anywhere in RHP — M6 scored 0, N/A"
  - "Post-issue promoter shareholding % shown as placeholder [•] in RHP, not finalized at filing — E1 used pre-issue 65.08% (Promoter 59.22% + Promoter Group 5.86%, RHP p.79)"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID (<=AVERAGE) driven by cumulative CFO/PAT of -0.29x across FY24-FY26 (RHP p.57), the only restated history the RHP provides; caps at max AVERAGE per deal-breaker #4, then downgraded one tier to AVOID for LIMITED (3yr) history"}
  - {type: FLAG-CASH, reason: "Deteriorating cash conversion every year despite triple-digit revenue/PAT growth: CFO +0.65cr (FY24) -> -2.92cr (FY25) -> -10.76cr (FY26), RHP p.57; FY26 trade receivables (138.69cr) = 93% of FY26 revenue with disclosed third-party (Quik Pay Pvt Ltd) collection contingency pending customer testing, RHP p.93; growth entirely financed externally"}
  - {type: FLAG-SECTOR, reason: "Manifest sector_cap_row (Pharma / CDMO) is mislabeled; RHP identifies business as precision-machined components for Defence, Railways, Aerospace, Semiconductors (peer set: Unimech Aerospace and Manufacturing Ltd, Azad Engineering Ltd, RHP p.94-95; AS9100D/ISO9001:2015 certification, RHP p.158)"}
data_years: 3
fy_range: "FY24 to FY26"
blocks: {A: 20, B: 0, C: 20, D: 15, E: 15}
core_score: 70
moat_score: 11
grand_total: 81
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "Block B (cash generation) = 0/20 (<8) -> caps at max GOOD, FY24-FY26 (all 3 restated years)"
  - "Cumulative CFO/PAT = -0.29x (<0.50) -> caps at max AVERAGE, driven by FY25 (-2.92cr) and FY26 (-10.76cr) CFO against rising PAT"
history_downgrade: true
data_notes:
  - "ROCE/ROE scored on RHP source-provided figures (p.98-99, p.234); self-computed standard-formula ROCE (EBIT/(Total Assets-Current Liabilities)) gives a different A4 trend result (decline, not improvement) because RHP's own Capital Employed definition differs (Tangible net-worth + total debt + DTL vs Total Assets - Current Liabilities); flagged for downstream awareness, source figure used per formula rule"
  - "EBITDA used for Block D and M1 is the RHP's own source-provided figure (p.98: FY24=277.64L, FY25=788.61L, FY26=5630.43L); an independent line-item reconciliation attempt landed ~35L higher on FY26, an immaterial (<1%) unreconciled variance that does not change any threshold band"
  - "Working Capital Days computed on Revenue basis throughout (Receivable/Inventory/Payable), since RHP discloses Cost of Material Consumed only, not a full COGS line"
  - "M9 gross-margin proxy (Revenue - Material Cost)/Revenue computed for company only (FY24 73.0%, FY25 52.0%, FY26 48.9%, declining) but not scoreable without a peer median"
  - "No loss-to-profit swing: PAT positive in all 3 restated years (FY24-26)"
block_b_trend: "deteriorating — CFO swung from +0.65cr (FY24) to -10.76cr (FY26) even as PAT grew to 37.06cr (RHP p.57, p.56); FY26 receivables reached 93% of FY26 revenue"
analyst_note: "The growth numbers (Block C, 20/20) and the RHP-source ROCE/ROE (Block A, 20/20) are real and well anchored, but Block A is sensitive to which capital-employed definition is used; a standard-formula recompute shows a declining ROCE trend instead. The number that should drive any position-sizing conversation is Block B: three straight years of negative operating cash flow, worsening each year, with FY26 receivables at 93% of revenue and a disclosed third-party (Quik Pay) collection dependency pending customer testing. That is a going-concern-adjacent working-capital pattern, not a rounding issue, and it is the sole reason cumulative CFO/PAT is negative and the classification is capped and then downgraded to AVOID. Only 3 audited years exist (incorporated 2021); this is a recently-listed SME IPO with no track record through a downturn. Sector tag in the manifest is wrong (real business: Defence/Railways/Aerospace/Semiconductor precision components) — downstream peer and margin work should use Unimech Aerospace and Azad Engineering as the comparison set, not any pharma/CDMO peer group."
```
