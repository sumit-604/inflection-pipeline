# STAGE 1: GATE 0 SCORECARD — N R Agarwal Industries Ltd (NRAIL)
Run date: 2026-07-22 | Model: claude-sonnet-5 | Run type: full (no prior run)

Data available: 5 years (FY22 to FY26) for headline Revenue/EBITDA/PAT and company-disclosed
ROCE%/EPS/D-E/ICR (source: Annual Report 2024-25 "How we have grown over the years" and
"Key numbers" pages). Full balance sheet, cash-flow and working-capital note detail is
available for 3 years (FY24 to FY26), drawing on the AR 2024-25 (FY24 & FY25 audited
financials) and the Q4/FY26 audited results filing (FY26, with FY25 comparatives). Scoring is
adapted to this blended 5-year/3-year history; data confidence is capped at the "5-6 years,
lower" tier (flag: may not have seen a full sector cycle — the FY24 capacity more than
doubled paperboard output mid-cycle, so pre-expansion and post-expansion economics are not
directly comparable across the window).

**Data source note (per orchestrator):** No NRAIL screener extract exists in this run. The
screening/ folder holds only JKPAPER (peer) CSVs, explicitly excluded from this company's
scorecard per instruction. All figures below are extracted directly from the NRAIL Annual
Report 2024-25 and the Q4/FY26 audited results filing. Peer-comparison moat tests (M2, M5,
M9) are scored 0/PEER DATA NEEDED as a result.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Source series — ROCE% company-disclosed for FY22-25 (AR p.5, "RoCE" bar chart; cross-checked
AR p.17 Key Numbers table for FY24/FY25); FY26 computed (no company disclosure in the
results filing).

| Year | ROCE % | Source |
|---|---|---|
| FY22 | 17.83% | AR p.5 (disclosed) |
| FY23 | 18.13% | AR p.5 (disclosed) |
| FY24 | 11.06% | AR p.5 & p.17 (disclosed) |
| FY25 | 5.55% | AR p.5 & p.17 (disclosed) |
| FY26 | 8.04% | computed: EBIT ÷ (Total Assets − Current Liabilities) = ₹123.77cr ÷ (₹2,031.45cr − ₹491.68cr) = ₹123.77cr ÷ ₹1,539.77cr (Results Q4FY26 p.5) |

**A1 Median ROCE:** sorted 5.55, 8.04, 11.06, 17.83, 18.13 → median = **11.06%** → band
10-14.9% → **score 1**

**A2 Minimum single-year ROCE:** min = 5.55% (FY25) → band <8% → **score 0**

**A3 Median ROE (PAT ÷ avg Net Worth):** computed independently — the company's own
"Return on Equity" line (AR p.17: FY25 1.04%, FY24 7.37%) is **not** true ROE; AR Note 57
(p.159) shows its denominator is "Avg Shareholder Equity = (Op. Share capital + Cls share
capital)" — i.e. PAT ÷ paid-up share capital only (₹17.02cr, unchanged), not net worth. That
figure is not used here; true ROE is computed from Balance Sheet net worth.

| Year | PAT (₹cr) | Opening NW (₹cr) | Closing NW (₹cr) | ROE % | Basis |
|---|---|---|---|---|---|
| FY23 | 99.30 | NOT FOUND | 635.63 | 15.62% | closing-only (opening NW for FY22 not disclosed anywhere in the provided documents) |
| FY24 | 125.46 | 635.63 | 760.29 | 17.98% | average |
| FY25 | 17.65 | 760.29 | 774.59 | 2.30% | average |
| FY26 | 43.70 | 774.59 | 815.40 | 5.50% | average |

Sources: PAT — AR p.4 (FY23), AR p.99 Statement of P&L (FY24/FY25), Results Q4FY26 p.4
(FY26). Net worth — AR p.102 Statement of Changes in Equity (opening Apr-1-2023 balance =
₹635.63cr), AR p.98 Balance Sheet (FY24/FY25 closing), Results Q4FY26 p.5 (FY26 closing).

Median of 4 values (15.62, 17.98, 2.30, 5.50) = (5.50+15.62)/2 = **10.56%** → band <12% →
**score 0**

**A4 ROCE trend, latest vs earliest:** latest (FY26) 8.04% vs earliest (FY22) 17.83% =
decline of 9.79pp → band >5pp decline → **score 0**

**BLOCK A TOTAL = 1 + 0 + 0 + 0 = 1 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Full cash-flow-statement detail is only available for FY24-FY26 (3 years); this block uses
that window.

| Year | CFO (₹cr) | Capex, gross (₹cr) | FCF (₹cr) | PAT (₹cr) |
|---|---|---|---|---|
| FY24 | 135.22 | 534.43 | -399.21 | 125.46 |
| FY25 | 176.11 | 119.66 | 56.44 | 17.65 |
| FY26 | 94.87 | 293.52 | -198.65 | 43.70 |

Sources: CFO & Capex — AR p.100 Statement of Cash Flows (FY24/FY25 col), Results Q4FY26 p.6
(FY26 col, "Purchase of property, plant and equipment and intangible assets, including
capital advances" line — gross, per formula definition, acquisitions n/a, no
subsidiaries/JVs per AR p.47). PAT — as in Block A.

**B1 Cumulative CFO ÷ Cumulative PAT (FY24-26):** ΣCFO = 406.20cr; ΣPAT = 186.81cr →
ratio = **2.174** → band ≥1.00 → **score 5**

**B2 FCF-positive years as proportion:** FY24 negative, FY25 positive, FY26 negative → 1 of
3 = 33% → band <50% → **score 0**

**B3 Cumulative FCF ÷ Cumulative PAT:** ΣFCF = -541.42cr; ratio = -541.42/186.81 = **-2.898**
→ band <0.20 or negative → **score 0**

**B4 Change in WC Days, latest (FY26) vs earliest (FY24) in this window:**
Revenue basis used throughout (COGS not separately broken out as a single line; stated per
formula rule).

| Year | Trade Recv. (₹cr) | Inventory (₹cr) | Trade Payables (₹cr) | Revenue (₹cr) | Recv. Days | Inv. Days | Pay. Days | WC Days |
|---|---|---|---|---|---|---|---|---|
| FY24 | 86.96 | 169.41 | 62.81 | 1,293.38 | 24.53 | 47.81 | 17.72 | 54.62 |
| FY25 | 186.43 | 167.55 | 230.37 | 1,659.03 | 41.03 | 36.87 | 50.70 | 27.20 |
| FY26 | 246.52 | 253.69 | 246.74 | 2,145.45 | 41.94 | 43.16 | 41.99 | 43.11 |

Sources: AR p.98 Balance Sheet (FY24/FY25), Results Q4FY26 p.5 (FY26); Revenue from AR p.142
Note 30 (FY24/FY25) and Results Q4FY26 p.4 (FY26).

Latest (43.11 days) vs earliest (54.62 days) = **decreased 11.51 days** → band decreased >5
days → **score 5**

**BLOCK B TOTAL = 5 + 0 + 0 + 5 = 10 / 20**

block_b_trend: **deteriorating** — CFO fell from ₹176.11cr (FY25) to ₹94.87cr (FY26), a 46%
decline even as revenue grew 29% YoY; FCF swung from +₹56.44cr (FY25) to -₹198.65cr (FY26) on
₹293.52cr of capex (pulp-mill balancing program + second-unit exploration, per AR p.44 and
Chairman's letter AR p.7-8).

---

## BLOCK C: GROWTH (Max 20)

Revenue and PAT series, widest available window (FY22-FY26, n=4 periods):

| Year | Revenue (₹cr) | PAT (₹cr) | Source |
|---|---|---|---|
| FY22 | 1,616.51 | 61.02 | AR p.4 |
| FY23 | 1,766.07 | 99.30 | AR p.4 |
| FY24 | 1,293.38 | 125.46 | AR p.142 (Note 30) / AR p.99 |
| FY25 | 1,659.03 | 17.65 | AR p.142 / AR p.99 |
| FY26 | 2,145.45 | 43.70 | Results Q4FY26 p.4 |

No loss-to-profit swing (PAT positive in every year FY22-FY26).

**C1 Revenue CAGR (FY22→FY26, n=4):** (2,145.45/1,616.51)^(1/4)−1 = **7.34%** → band
5-9.9% → **score 1**

**C2 PAT CAGR (FY22→FY26, n=4):** both endpoints positive (not N/M). (43.70/61.02)^(1/4)−1 =
**-8.00%** → negative → **score 0**

**C3 Positive YoY revenue years, proportion (4 YoY comparisons FY23-FY26):** FY23>FY22
(positive), FY24<FY23 (decline), FY25>FY24 (positive), FY26>FY25 (positive) = 3 of 4 = 75%
→ band 75-99% → **score 3**

**C4 PAT CAGR minus Revenue CAGR:** -8.00% − 7.34% = **-15.34pp** → band <-8pp → **score 0**

**BLOCK C TOTAL = 1 + 0 + 3 + 0 = 4 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — latest = FY26

Not a bank/NBFC/Insurance company; standard formulas apply.

**D1 Net Debt ÷ EBITDA (latest):**

| Year | Total Borrowings (₹cr) | Cash & bank balances (₹cr) | Net Debt (₹cr) | EBITDA (₹cr) | ND/EBITDA |
|---|---|---|---|---|---|
| FY24 | 548.84 | 20.53 | 528.31 | 185.59 | 2.85x |
| FY25 | 617.23 | 4.60 | 612.62 | 142.44 | 4.30x |
| FY26 | 788.91 | 4.94 | 783.97 | 197.93 | **3.96x** |

Sources: Borrowings/cash — AR p.159 Note 46 Capital Risk Management (FY24/FY25, company's
own net-debt reconciliation), Results Q4FY26 p.5 (FY26, computed as current+non-current
borrowings less cash-and-equivalents plus other bank balances). EBITDA computed as PBT
(pre-exceptional) + Finance Costs + D&A — this reconciles exactly to the company's own
disclosed EBITDA for FY24/FY25 (₹185.59cr / ₹142.44cr, AR p.4), confirming methodology; FY26
= ₹65.13cr (PBT pre-exceptional) + ₹64.14cr (finance costs) + ₹68.65cr (D&A) = ₹197.93cr
(Results Q4FY26 p.4).

Latest (FY26) = **3.96x** → band >3x → **score 0**

**D2 Interest Coverage, EBIT ÷ Interest (latest):** computed per pipeline formula (EBIT =
PBT + total Finance Costs; Interest = total Finance Costs). Note: this differs from the
company's own disclosed "Interest Coverage Ratio" (AR p.5/17: FY24 17.60x, FY25 2.34x),
whose exact denominator basis is not reconcilable from the disclosed interest breakup
(AR p.143, Note 35) — both figures are shown for transparency; the pipeline-formula figure is
the one scored.

| Year | EBIT (₹cr) | Finance Costs (₹cr) | IC (computed) | IC (company-disclosed) |
|---|---|---|---|---|
| FY24 | 148.17 | 10.54 | 14.06x | 17.60x |
| FY25 | 76.87 | 60.91 | 1.26x | 2.34x |
| FY26 | 123.77 | 64.14 | **1.93x** | not disclosed |

Latest (FY26, computed) = **1.93x** → band 1.5-2.9x → **score 1**

**D3 Debt ÷ Equity (latest):** computed as Total Borrowings (current+non-current) ÷ Total
Equity per pipeline formula. This differs from the company's own disclosed D/E (AR p.5/17:
FY24 0.63x, FY25 0.70x), which uses gross long-term borrowings only, excluding
working-capital borrowings — reconciled: FY25 LT-debt-only/equity = ₹545.07cr/₹774.59cr =
0.70x, matching AR exactly. The pipeline formula (all borrowings) is scored below.

| Year | Total Borrowings (₹cr) | Total Equity (₹cr) | D/E (computed, all borrowings) | D/E (company-disclosed, LT only) |
|---|---|---|---|---|
| FY24 | 548.84 | 760.29 | 0.72x | 0.63x |
| FY25 | 617.23 | 774.59 | 0.80x | 0.70x |
| FY26 | 788.91 | 815.40 | **0.97x** | NOT FOUND (split not disclosed in Q4FY26 results) |

Latest (FY26) = **0.97x** → band 0.5-1.0x → **score 3**

**D4 Current Ratio (latest):** company-disclosed for FY24/FY25 (AR p.17, verified against
Balance Sheet); FY26 computed.

| Year | Current Ratio | Source |
|---|---|---|
| FY24 | 1.60x | AR p.17 (disclosed) |
| FY25 | 1.33x | AR p.17 (disclosed; ties to Current Assets ₹510.60cr ÷ Current Liabilities ₹384.69cr = 1.328x, AR p.98) |
| FY26 | **1.155x** | computed: Current Assets ₹567.80cr ÷ Current Liabilities ₹491.68cr (Results Q4FY26 p.5) |

Latest (FY26) = **1.155x** → band 1.0-1.19x → **score 1**

**BLOCK D TOTAL = 0 + 1 + 3 + 1 = 5 / 20**

---

## CORE SCORE = A(1) + B(10) + C(4) + D(5) = **20 / 80**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding (latest quarter):** 73.96% as at March 31, 2025 (no more recent
shareholding pattern was provided; shareholding/ folder is empty — this is the latest
available). Source: AR p.3 and AR p.82 (Categories of Shareholders table, 1,25,88,166 shares
= 73.96%). → band ≥60% → **score 5**

**E2 Promoter holding change over 3 years:** NOT FOUND — no FY22/FY23 shareholding pattern
was provided in this run; only the single FY25 snapshot (73.96%) is available. Per rule, a
missing data point scores 0. → **score 0**

**E3 Promoter pledge (latest):** NOT FOUND in SEBI shareholding-pattern format (no exact %
disclosed; shareholding/ folder empty). However, AR Note 18 (p.135-136) — loan security
terms for the Punjab National Bank term loan — discloses: **"Pledge over entire equity shares
of Promoters. (Request to convert in non-diposed [sic] undertaking is pending with the
bank)"** as of the FY25 AR sign-off (May 28, 2025). The equivalent SBI facility's promoter
pledge had already been converted to a non-disposal undertaking (AR p.134, same note). This
is a material, unresolved item: it indicates a lender-held pledge over the promoters' full
shareholding may still exist on at least one facility, but the run provides no verified
percentage to score against the 0%/≤5%/5-15%/>15% bands. Scored 0 per the "missing data → 0"
rule; **flagged** for downstream follow-up (obtain SEBI shareholding-pattern filing). →
**score 0**

**E4 Contingent liabilities ÷ Net Worth (latest available full disclosure = FY25; FY26 note
not included in the Q4FY26 results filing, which carries summary financials only):**

Contingent liabilities (AR p.145, Note 38): disputed Excise/Service Tax/Customs ₹3.23cr +
disputed Income Tax ₹29.42cr + bank guarantees ₹12.01cr + labour claims ₹0.73cr + other
claims (pipeline) ₹4.42cr = **₹49.81cr**. Net Worth FY25 = ₹774.59cr (AR p.98). Ratio =
49.81/774.59 = **6.43%** → band 5-15% → **score 3**

**BLOCK E TOTAL = 5 + 0 + 0 + 3 = 8 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

**M1 Pricing Power:** EBITDA margin FY22 = 154.24/1,616.51 = 9.54%; FY26 = 197.93/2,145.45 =
9.23%. Change = -0.31pp (within ±2pp, "stable"). Revenue CAGR FY22-26 = 7.34% (<10%).
Neither the ≥10%-growth-with-expansion tier nor the ≥10%-growth-with-stable-margin tier is
met, and the -0.31pp change does not fall in the 2-5pp decline band either. → **score 0**

**M2 Cost Advantage vs peer median EBITDA margin:** peer data explicitly excluded from this
run (JKPAPER CSVs not to be used). → **score 0, PEER DATA NEEDED**

**M3 Capital Efficiency:** FAT (Revenue ÷ Net PPE) FY26 = 2,145.45/1,185.25 = 1.81x; ROCE
FY26 = 8.04% (<12%). Fails all positive tiers (needs ROCE ≥12% at minimum). → **score 0**

**M4 Customer Stickiness:** 1 revenue-decline year in the window (FY24); revenue recovered
in both following years (FY25 > FY24, FY26 > FY25). Receivable days moved from 24.53
(FY24) to 41.94 (FY26), not stable, but the qualifying condition at this tier ("max 1 decline
year, fully recovered") is met on the revenue leg. → **score 3**

**M5 Scale & Dominance:** requires verified peer mcap/margin ranking; AR self-describes the
Company as "largest paperboard manufacturer (greyback/white-back)" and "largest recycled
paper manufacturer" (AR p.8) but this is an unverified company claim, not independent peer
data, and peer data is out of scope for this run. → **score 0, PEER DATA NEEDED**

**M6 Technology/R&D:** AR Annexure 3 (p.57) states "Expenditure incurred on Research and
Development: Nil." R&D/Revenue = 0%. → **score 0**

**M7 Regulatory/License:** paper/paperboard manufacturing is an unregulated, non-licensed
segment (no entry-barrier licensing regime disclosed). → **score 0**

**M8 Distribution:** AR (p.7-8) states "~30% exported, ~60% sold in western India... marketed
pan-India" but provides no outlet count, distributor count, or revenue-per-outlet trend —
mentioned but unquantified. → **score 1**

**M9 Brand:** requires peer gross-margin comparison; peer data out of scope for this run. →
**score 0, PEER DATA NEEDED**

**M10 Switching Costs:** revenue grew in all but 1 year (FY24 decline), but receivable days
rose materially (24.53 → 41.94 days, FY24→FY26), failing the "stable" leg of the qualifying
tier; the "2+ decline years" tier does not apply either (only 1 decline year). → **score 0**

**M11 Network Effects:** only 5 years of data available (<6-year minimum for the two-window
test) — scored conservatively on overall trend, as instructed. Selling & distribution expense
rose as % of revenue (0.89% FY24 → 1.19% FY25, AR p.144 Note 37) while revenue CAGR was
modest (7.34%) — trend does not support network-effect scoring. → **score 0**

**M12 Negative WC/Float:** WC days FY24/25/26 = 54.62/27.20/43.11 — never negative; latest
and majority of the window fall in the 15-45 day band (FY24 slightly exceeds it at 54.62).
→ **score 1**

**MOAT PROFILE**
```
M1  Pricing Power        [----------]  0
M2  Cost Advantage        PEER DATA NEEDED  0
M3  Capital Efficiency   [----------]  0
M4  Customer Stickiness  [######----]  3  (present)
M5  Scale & Dominance      PEER DATA NEEDED  0
M6  Technology/R&D       [----------]  0
M7  Regulatory/License   [----------]  0
M8  Distribution         [##--------]  1
M9  Brand                  PEER DATA NEEDED  0
M10 Switching Costs      [----------]  0
M11 Network Effects      [----------]  0
M12 Negative WC/Float    [##--------]  1
```

**MOAT TOTAL = 0+0+0+3+0+0+0+1+0+0+0+1 = 5 / 60**
**Moats present (score ≥3): 1 (M4 only)**
**Moat classification: 1 present → THIN**

---

## GRAND TOTAL = Core (20) + Moat (5) = **25**

---

## DEAL-BREAKER CHECK

| # | Rule | Triggered? | Detail |
|---|---|---|---|
| 1 | Block A <8 → max GOOD | **YES** | Block A = 1 |
| 2 | Block B <8 → max GOOD | No | Block B = 10 |
| 3 | Median ROCE <10% → max AVERAGE | No | Median ROCE = 11.06% |
| 4 | Cumul. CFO/PAT <0.50 → max AVERAGE | No | Ratio = 2.174 |
| 5 | Pledge >15% → max AVERAGE | Unresolved | Exact % NOT FOUND; qualitative loan-security note (AR p.135-136) suggests a pledge over the *entire* promoter shareholding may exist on the PNB facility — flagged, not scored as a numeric trigger |
| 6 | ND/EBITDA >3x AND IC <3x → **AVOID** | **YES** | FY26: ND/EBITDA 3.96x AND IC 1.93x (computed); FY25 also breaches on the same computed basis (4.30x / 1.26x) — this is a two-year pattern, not a single-year artifact, coinciding with the FY24 debt-funded ₹1,000cr paperboard-capacity expansion (₹665cr debt, AR p.9) landing into a sector downturn |
| 7 | Revenue declined in majority of years → max AVERAGE | No | 1 of 4 YoY periods declined (25%) |
| 8 | PAT negative in any of last 3 years → max AVERAGE | No | PAT positive every year FY24-FY26 |
| 9 | History <3 years → AVERAGE | No | 5 years available |

Deal-breaker 6 (AVOID) is the controlling override, and is independently consistent with the
Core Score matrix outcome below.

---

## CLASSIFICATION

Core Score = 20 (<40) → matrix outcome = **AVOID**, independent of moat class.
Deal-breaker 6 also mandates **AVOID**.

**FINAL CLASSIFICATION: AVOID**

Data confidence: 5-year window → "lower" tier → flag applied: **may not have seen a full
sector cycle** (the FY24 capacity step-change makes pre/post-expansion periods not directly
comparable). `history_downgrade` is recorded true given that the metrics driving the
deal-breaker (Blocks B and D) rely on the narrower 3-year (FY24-FY26) full-statement window,
not the full 5-year headline series.

**Strongest block:** Block B, Cash Generation Quality (10/20 = 50% of max) — driven by strong
cumulative CFO/PAT conversion (2.17x) and a genuine, if volatile, improvement in working-
capital days over the window.

**Weakest block:** Block A, Return on Capital (1/20 = 5% of max) — ROCE nearly halved from
FY22 (17.83%) to FY26 (8.04%), and true ROE (not the company's mislabeled disclosure) fell
from ~18% (FY24) to ~5.5% (FY26).

**Decision line:** Mechanical AVOID on both the core-score floor (20/80) and the
leverage/coverage deal-breaker (ND/EBITDA 3.96x with IC 1.93x, FY26 — and the same breach
pattern in FY25). The story underneath is a debt-funded doubling of paperboard capacity
(commissioned March 2024) landing into a sector-wide realization downturn, compressing EBITDA
and coverage just as debt service ramped up; a moat scan finds essentially no confirmed
moats (THIN, 1/12 present) under the peer-data constraints of this run. This is a mechanical
scorecard output only — no qualitative judgment on company quality is implied or intended;
flags propagate to downstream stages per pipeline rules.

---

## DATA NOTES

- No loss-to-profit PAT swing in FY22-FY26 (PAT positive throughout).
- Company's own disclosed "Return on Equity" (AR p.17, Note 57 p.159) is PAT ÷ paid-up share
  capital, not PAT ÷ net worth — mislabeled relative to the standard definition. True ROE was
  computed independently for FY23 (closing-net-worth-only basis, opening not disclosed),
  FY24, FY25 and FY26 (average-net-worth basis).
- Company's own disclosed Debt-Equity ratio (0.70x FY25, 0.63x FY24) uses gross long-term
  borrowings only, excluding working-capital borrowings. D3 here is computed on total
  borrowings (current + non-current) ÷ equity per the pipeline's formula definition, giving
  materially higher ratios (0.80x FY25, 0.97x FY26). The FY26 long-term-only split needed to
  reproduce the company's own convention was not disclosed in the Q4/FY26 results filing.
- Company's own disclosed Interest Coverage Ratio (2.34x FY25, 17.60x FY24) methodology is
  not reconcilable from the disclosed interest breakup (AR Note 35, p.143). D2 here is
  computed as EBIT (PBT + total Finance Costs) ÷ total Finance Costs per the pipeline formula,
  giving materially lower ratios (1.26x FY25, 1.93x FY26).
- M2 (Cost Advantage), M5 (Scale & Dominance), M9 (Brand) — all scored 0, PEER DATA NEEDED.
  The run's screening/ folder contains only JKPAPER (peer) CSVs, explicitly excluded from
  this company's scorecard per the orchestrator's instruction.
- E3 Promoter pledge: exact % NOT FOUND (no SEBI shareholding-pattern filing provided). AR
  Note 18 (p.135-136) loan-security language for the Punjab National Bank facility states a
  pledge over the "entire equity shares of Promoters" was pending conversion to a
  non-disposal undertaking as of the FY25 AR sign-off (May 28, 2025); the SBI facility's
  equivalent pledge had already been converted. Flagged for downstream follow-up.
- E2 (3-year promoter-holding change): NOT FOUND — only the FY25 snapshot (73.96%) was
  available in the documents provided.
- E4 uses FY25 contingent-liability figures (latest full note disclosure); the Q4/FY26
  results filing carries summary financials only, without a contingent-liabilities note.
- FY26 P&L carries a ₹1.07cr one-time exceptional charge (Labour Code past-service cost,
  recognised Q3FY26) and a ₹4.44cr loss on assets discarded; EBITDA/ROCE for FY26 are computed
  on a pre-exceptional PBT basis to preserve comparability with the FY22-FY25 company-
  disclosed figures (which carried no exceptional items).
- Other income is unusually large in FY25 (₹31.40cr, including ₹14.73cr of unrealised gains
  on the Company's listed-equity/mutual-fund portfolio) and FY26 (₹23.51cr); since it sits
  inside PBT it flows into the EBITDA figures used for D1 and M1 — a quality-of-earnings
  caveat for downstream stages, as these are investment-portfolio gains, not core
  paper-manufacturing income.
- input_gaps carried forward: announcements/ empty; shareholding/ empty; research/ empty;
  screening/ is peer (JKPAPER) data, not NRAIL; presentation stale (May-2022); prospectus
  absent (long-listed, not expected).

---

```yaml
stage: B01-gate0
company: "NRAIL"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps: ["announcements/ empty", "shareholding/ empty", "research/ empty", "screening/ is peer (JKPAPER) data not NRAIL", "presentation stale May-2022", "prospectus absent (long-listed, not-expected)"]
flags:
  - {type: FLAG-GATE0, reason: "Core score 20/80 and deal-breaker 6 (ND/EBITDA 3.96x AND IC 1.93x, FY26, with the same breach pattern in FY25) both independently drive AVOID. Historical depressor: FY24 debt-funded doubling of paperboard capacity (~Rs1,000cr, ~Rs665cr debt) commissioned into a sector-wide realization downturn, compressing EBITDA/coverage. Also flagging: E3 promoter-pledge % NOT FOUND but AR Note 18 loan-security language indicates a pledge over the entire promoter shareholding was pending release on the PNB facility as of the FY25 AR sign-off — needs SEBI shareholding-pattern confirmation downstream."}
data_years: 5
fy_range: "FY22 to FY26"
blocks: {A: 1, B: 10, C: 4, D: 5}
core_score: 20
moat_score: 5
grand_total: 25
moats_confirmed: 1
moat_class: "THIN"
classification: "AVOID"
deal_breakers: ["1: Block A(1)<8 -> max GOOD (superseded by AVOID)", "6: ND/EBITDA(3.96x FY26, 4.30x FY25)>3x AND IC(1.93x FY26, 1.26x FY25)<3x -> AVOID", "5: promoter pledge % NOT FOUND, qualitative loan-security note suggests possible full-shareholding pledge on PNB facility pending release -- unresolved, not scored as numeric trigger"]
history_downgrade: true
data_notes: ["no loss-to-profit PAT swing FY22-FY26", "company's disclosed ROE is PAT/share-capital not PAT/net-worth, true ROE computed independently", "company's disclosed D/E uses LT debt only, D3 computed on total borrowings per pipeline formula", "company's disclosed ICR methodology not reconcilable, D2 computed as EBIT/total finance costs per pipeline formula", "M2/M5/M9 PEER DATA NEEDED, JKPAPER peer CSVs excluded per orchestrator instruction", "E3 pledge % NOT FOUND, qualitative pledge disclosure in AR Note 18 flagged", "E2 3-year promoter holding change NOT FOUND, only FY25 snapshot available", "E4 uses FY25 contingent liabilities, FY26 note not in results filing", "FY26 EBITDA/ROCE computed pre-exceptional for comparability", "other income unusually large FY25/FY26 including unrealised investment gains, quality-of-earnings caveat on EBITDA"]
block_b_trend: "deteriorating -- CFO fell from Rs176.11cr (FY25) to Rs94.87cr (FY26), a 46% decline despite 29% revenue growth; FCF swung from +Rs56.44cr (FY25) to -Rs198.65cr (FY26) on Rs293.52cr capex"
```
