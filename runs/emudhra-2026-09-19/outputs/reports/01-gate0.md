# Stage 1 — Gate 0 Scorecard: eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19
Data available: 8 years (FY19 to FY26). Scoring adapted to 8-year history.
Units: screener Data_Sheet figures are INR Cr. AR/results figures cited
separately are INR Million (source states unit on the face of the
document; no silent conversion — Mn values are marked Mn throughout).

## CORRECTION 2026-09-19 (FLAG-DISAGREEMENT, settled at source)

The original draft of this report misread FY26 capex. It used Rs 814.21
Mn — the MD&A prose's "mainly includes" subset (product development Rs
124.62 Mn + new product development Rs 476.38 Mn + Data Center/Server Rs
213.21 Mn, AR p.156) — as if it were the FULL "Purchase of Property,
plant and equipment and Intangible assets" line from the cash flow
statement. It is not; it is a partial narrative breakdown of a larger
line.

The clean mupdf extraction of the Consolidated Cash Flow Statement, AR
p.218, gives the actual line:
- Purchase of Property, plant and equipment and Intangible assets:
  **Rs 1,853.68 Mn (FY26) / Rs 832.02 Mn (FY25)**
- Payment towards acquisition of business (net of assets acquired), a
  SEPARATE line, correctly excluded from capex per the FCF formula:
  Rs 629.03 Mn (FY26) / Rs 743.23 Mn (FY25)
- Net cash from operating activities: Rs 1,328.49 Mn (FY26) / Rs
  1,016.16 Mn (FY25) — unchanged from the original draft, matches
  screener-data exactly.

**Corrected FY26 FCF = 1,328.49 − 1,853.68 = -Rs 525.19 Mn (-Rs 52.52
Cr)**, was reported as +Rs 51.43 Cr. **Corrected FY25 FCF = 1,016.16 −
832.02 = +Rs 184.14 Mn (+Rs 18.41 Cr)**, newly available now that two
years are clean-anchored. The corrected FY26 figure matches the
operator's original load-bearing fact (-Rs 52 Cr) and Stage 3's
independent reading; the original draft's contradiction of that fact was
the error, not a genuine divergence.

Effect: B2, B3, Block B total, core_score, grand_total, classification
and block_b_trend all move (see below); the deal-breaker check now
triggers #2 (Block B <8), capping classification at GOOD (was GOOD+).
Blocks A, C, D, E and F (moat) are unaffected — no other scoring rule
in this stage reads FCF or capex.

## LOAD-BEARING FACTS CHECK (companies/EMUDHRA.md, first verification priority)

1. **ORGANIC GROWTH vs GUIDANCE** — out of scope for this quantitative
   scorecard (needs segment/organic-vs-acquired revenue split not present
   in the screener Data_Sheet or Block A-F formulas). Flagged for stage 2+.
2. **CASH CONVERSION** ("FY26 FCF Rs -52 Cr; days payable 420 vs debtor
   days 98') — CONFIRMED on FCF (see Correction above: FY26 FCF -Rs
   52.52 Cr, matches). NOT reproducible on the payables-days leg:
   consolidated trade-payables balance could not be reliably isolated
   from the FY26 AR's OCR-scrambled Note 18 (see data_notes). The only
   clean payable-days figure found is **standalone** (AR Note 50,
   p.364): 251.7 days (FY26) — well short of 420, and on a different
   consolidation basis than debtor days (92-98d, which are
   consolidated, AR p.57). The "420 days" claim may conflate trade
   payables with the Rs 881.16 Mn non-current "payable for acquisition
   of business — contingent consideration" (AR p.216/255). Flag for
   downstream verification.
3. **3i INFOTECH CLAIM** — AR Note 36 (Contingent Liabilities, p.264-265,
   consolidated) quantifies contingent liabilities at only Rs 34.55 Mn
   (Rs 3.46 Cr: income-tax appeal Rs 32.29 Mn + GST appeal Rs 1.48 Mn).
   The 3i Infotech claim (>Rs 128 Cr) is disclosed only as narrative Note
   36(f), NOT included in the quantified total — the company disputes it
   in full. E4 (contingent liabilities/net worth) is scored on the
   quantified figure per the standard note, which structurally excludes
   this disputed claim; see the E4 flag below.
4. **ASSET BUILD** (fixed assets Rs 419 Cr to Rs 727 Cr) — confirmed
   directionally (screener Net Block + CWIP). The full FY26 capex line
   is now confirmed clean at Rs 1,853.68 Mn (AR p.218, see Correction
   above). The MD&A prose (AR p.156) itemises only Rs 814.21 Mn of that
   total (product development + Data Center/Server); the remaining ~Rs
   1,039 Mn is not broken out in the narrative and could not be split
   between acquired intangibles, goodwill-adjacent capitalisation, and
   other PPE/intangible additions from the provided corpus. Separately,
   the Rs 629.03 Mn (FY26) acquisition-of-business payment (net of
   assets acquired) is its own line, correctly excluded from capex.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 12/20 (unchanged)

Methodology note: screener's own ROCE/ROE ratios were not in the
provided data (Customization sheet came out empty per B00). Computed
here as "computed" for FY19-FY23 using Capital Employed = Equity Share
Capital + Reserves + Borrowings (screener's 4-bucket Data_Sheet model;
Total Assets − Other Liabilities, since a reliable current/non-current
liability split could not be extracted — see data_notes). For FY24-FY26,
the company's own consolidated ROCE/RoE (AR p.57, "Return ratios" chart)
is used per the "use the source's figure" rule — it is close to but not
identical to this stage's own computed method (FY26: 15.0% disclosed vs
14.51% computed), a small definitional gap, not a discrepancy.

| Year | EBIT (PBT+Interest, Cr) | Capital Employed (Cr) | ROCE | Source |
|---|---|---|---|---|
| FY19 | 21.91 | 104.37 | 20.99% | computed (screener-data) |
| FY20 | 23.69 | 133.92 | 17.69% | computed (screener-data) |
| FY21 | 32.02 | 158.68 | 20.18% | computed (screener-data) |
| FY22 | 55.02 | 219.94 | 25.02% | computed (screener-data) |
| FY23 | 76.76 | 416.92 | 18.41% | computed (screener-data) |
| FY24 | — | — | 19.5% | AR p.57 (consolidated, disclosed) |
| FY25 | — | — | 18.2% | AR p.57 (consolidated, disclosed) |
| FY26 | 136.38 | 939.91 | 15.0% | AR p.57 (disclosed; 14.51% computed, screener-data) |

**A1 Median ROCE** = 18.955% (avg of 4th/5th of 8 sorted values: 18.41,
19.5) → band 15-19.9% → **score 3**
**A2 Minimum single-year ROCE** = 15.0% (FY26, AR p.57) → band ≥15% →
**score 5**
**A3 Median ROE** = 18.675% (see table below) → band 15-19.9% → **score
4**
**A4 ROCE trend, latest vs earliest** = 15.0% (FY26) vs 20.99% (FY19,
computed) = decline of 5.99pp → band decline >5pp → **score 0**

ROE table (Net Worth = Equity Capital + Reserves, screener-data; FY19
uses closing net worth only, opening not available, stated per protocol;
FY24-26 company-disclosed, AR p.57):

| Year | PAT (Cr) | Avg Net Worth (Cr) | ROE | Source |
|---|---|---|---|---|
| FY19 | 17.44 | 75.64 (closing only) | 23.06% | computed |
| FY20 | 16.65 | 83.89 | 19.85% | computed |
| FY21 | 17.46 | 99.75 | 17.50% | computed |
| FY22 | 41.40 | 130.09 | 31.83% | computed |
| FY23 | 61.68 | 272.21 | 22.66% | computed |
| FY24 | — | — | 14.9% | AR p.57 |
| FY25 | — | — | 13.3% | AR p.57 |
| FY26 | — | — | 12.4% | AR p.57 |

A total: 3+5+4+0 = **12/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 7/20 (was 13/20, CORRECTED)

CFO (screener-data, Cr): FY19 16.79, FY20 23.24, FY21 40.94, FY22 21.61,
FY23 33.57, FY24 72.52, FY25 101.62, FY26 132.85. Cumulative = 443.14 Cr.
PAT cumulative (screener-data) = 422.12 Cr.

**B1 Cumulative CFO ÷ Cumulative PAT** = 443.14/422.12 = 1.05x → band
≥1.00 → **score 5**

**FCF — corrected, n=2 years (FY25, FY26).** Capex is the AR's
"Purchase of Property, plant and equipment and Intangible assets" line,
Consolidated Cash Flow Statement, AR p.218 (mupdf clean extraction),
excluding the separate "Payment towards acquisition of business (net of
assets acquired)" line per the formula's own instruction:

| Year | CFO (Mn) | Capex (Mn) | Acquisition payment excluded (Mn) | FCF (Mn) | FCF (Cr) |
|---|---|---|---|---|---|
| FY25 | 1,016.16 | (832.02) | (743.23) | +184.14 | +18.41 |
| FY26 | 1,328.49 | (1,853.68) | (629.03) | -525.19 | -52.52 |

FY19-FY24 capex is not extractable from provided data (screener
Data_Sheet has no capex line; no earlier-year AR cash-flow statement in
this corpus), so cumulative FCF/PAT below covers FY25-FY26 only.

**B2 FCF-positive years as proportion** = 1/2 measurable years positive
→ 50% → band 50-74% → **score 2 (LIMITED confidence: n=2, below the
3-year floor)**

**B3 Cumulative FCF ÷ Cumulative PAT** = (184.14 − 525.19)/(846.4 +
1,077.9 Mn PAT, i.e. Rs 84.64 Cr + Rs 107.79 Cr = Rs 192.43 Cr) =
-34.11/192.43 = **-17.7%** → band <0.20 or negative → **score 0
(LIMITED confidence, n=2, same caveat)**

**B4 Change in WC Days, latest vs earliest** = **N/A (not in provided
data), score 0.** Trade Payables are not a line item in the screener
Data_Sheet for any year, and the AR's consolidated Note 18 (Trade
payables, p.255) is OCR-scrambled in the pdftotext-layout extraction:
the label/value pairing could not be confirmed against independent
cross-checks (candidate readings ranged from Rs 172 Mn to Rs 1,030 Mn
for the same year depending on which scrambled row is trusted, an
eight-fold spread — none usable as an anchor even after the mupdf
cross-check on p.218 resolved the cash-flow-statement figures). This is
unaffected by the FCF correction above (different note, different
extraction problem). Standalone Trade Payables turnover IS clean (AR
Note 50, p.364: 1.45x FY26, 1.65x FY25 → 251.7d / 221.2d) but mixing a
standalone payables figure with consolidated receivables/inventory
would combine two different entities' balance sheets, which this stage
declines to do.

Block B total: 5+2+0+0 = **7/20** (was 5+5+3+0 = 13/20)

**block_b_trend: deteriorating** — FCF swung from +Rs 18.41 Cr (FY25) to
-Rs 52.52 Cr (FY26), AR p.218 (mupdf clean extraction), driven by capex
nearly doubling (Rs 832.02 Mn to Rs 1,853.68 Mn) while CFO grew only
~31% (Rs 1,016.16 Mn to Rs 1,328.49 Mn). This sits alongside a genuinely
improving accrual-quality signal — CFO/PAT rose from 0.54x (FY23:
33.57/61.68, screener-data) to 1.23x (FY26: 132.85/107.79, screener-data)
— so the cash *quality* of reported profit is improving even as free
cash flow itself worsened on heavier capex. WC-days trend remains N/A
(consolidated payables gap, unaffected by this correction).

## BLOCK C: GROWTH (Max 20) — Score: 18/20 (unchanged)

Revenue (screener-data, Cr): FY19 101.58 → FY26 701.58, 7-year span, all
7 YoY comparisons positive (101.58→116.45→131.59→182.64→248.76→
373.12→519.39→701.58).
PAT (screener-data, Cr): FY19 17.44 → FY26 107.79.

**C1 Revenue CAGR** = (701.58/101.58)^(1/7)−1 = **31.8%** → band ≥20% →
**score 5**
**C2 PAT CAGR** = (107.79/17.44)^(1/7)−1 = **29.7%** → band ≥20% →
**score 5**
**C3 Positive YoY revenue years** = 7/7 = 100% → **score 5**
**C4 PAT CAGR − Revenue CAGR** = 29.7 − 31.8 = **−2.1pp** → band ±3pp →
**score 3**

C total: 5+5+5+3 = **18/20**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 20/20 (unchanged)

FY26 (screener-data, Cr): Borrowings 28.78, Cash & Bank 107.31, Reserves
870.11, Equity Share Capital 41.02 (Net Worth 911.13), Interest 5.07,
EBIT (computed, PBT+Interest) 136.38.

**D1 Net Debt ÷ EBITDA** = Borrowings 28.78 − Cash 107.31 = **net cash
(-78.53 Cr)** → **score 5**
**D2 Interest Coverage** = EBIT 136.38 / Interest 5.07 = **26.9x** →
band ≥10x → **score 5**
**D3 Debt ÷ Equity** = 28.78/911.13 = **0.032x** → band <0.1 →
**score 5**
**D4 Current Ratio** = **2.90x (FY26), FLAGGED — STANDALONE basis only**
(AR Note 50, p.364: "Current Ratio 2.90 / 5.40", explicitly standalone).
Consolidated current assets/current liabilities could not be split from
the OCR-scrambled balance sheet (AR p.216-217; same issue as Note 18).
Band ≥2.0 → **score 5**, but this figure is basis-inconsistent with the
rest of this analysis (consolidated) and should be re-verified against
the source PDF directly before being relied on.

D total: 5+5+5+5 = **20/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 14/20 (unchanged)

**E1 Promoter holding (latest quarter)** = **54.40%** (BSE Reg 31
summary, scrip 543533, quarter ending June 2026, retrieved 2026-09-19)
→ band 50-59.9% → **score 4**
**E2 Promoter holding change over 3 years** = **N/A (not in provided
data), score 0.** Only two data points exist: BSE summaries for Mar-2026
and Jun-2026 (both 54.40%, unchanged) and the AR's FY26-vs-FY25
promoter-holding note (p.251), which shows FY25→FY26 change of 0% for
most holders (one intra-family transfer between Mythili Srinivasan and
Taarav Pte Ltd, net promoter total unchanged: 54.41%→54.40%). No
data point from ~3 years before run date (circa Sep-2023) is in the
provided corpus. Directionally flat over the ~1-2 years actually
observed, but the formula's 3-year window is not verifiable.
**E3 Promoter pledge (latest)** = **0%** (BSE Reg 31 summary, Jun-2026:
"Whether any shares held by promoters are pledge or otherwise
encumbered? No") → **score 5**
**E4 Contingent liabilities ÷ Net Worth (latest)** = Rs 34.55 Mn (Rs 3.46
Cr, AR Note 36, p.264, consolidated, FY26) / Rs 911.13 Cr net worth
(screener-data) = **0.38%** → band <5% → **score 5**. **FLAG: this
figure structurally excludes the disputed 3i Infotech claim (>Rs 128
Cr, ~14% of FY26 net worth if it were included), which sits only in AR
Note 36(f) narrative disclosure, not the quantified total** (see
load-bearing fact #3 above). The clean E4 score materially understates
the tail risk named in the run's own priority verification list.

E total: 4+0+5+5 = **14/20**

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 17/60 (unchanged; no M-test reads FCF/capex)

EBITDA computed as Sales − (Raw Material + Δ Inventory + Power&Fuel +
Other Mfr. Exp + Employee Cost + Selling&Admin + Other Expenses), all
screener-data, Cr. FY19 EBITDA margin 31.83% (32.33/101.58); FY26 EBITDA
margin 21.97% (154.12/701.58) — a 9.86pp decline over the period, mostly
concentrated in "Other Mfr. Exp" rising from Rs 11.9 Cr (FY19) to Rs
280.91 Cr (FY26), consistent with scale-up of trust-services/hardware
cost lines and the Cryptas acquisition; not independently decomposable
from provided data.

**M1 Pricing Power** — margin declined 9.86pp (FY19→FY26) despite 31.8%
revenue CAGR; decline exceeds the 2-5pp "declined despite growth" band →
**score 0**

**M2 Cost Advantage vs peer median EBITDA margin** — peer FY26 EBITDA
margins (screener-data): NEWGEN 25.78% (405.78/1574.4), QUICKHEAL
-11.54% (-30.11/261.02), PROTEAN 11.58% (115.52/997.75). Peer median =
11.58%. eMudhra 21.97% is +10.39pp above → band ≥5pp above → **score 5**

**M3 Capital Efficiency** — FAT (Sales/Net Block, screener-data) =
701.58/726.86 = 0.97x (<1x) with ROCE 15.0% → fails all bands → **score
0**

**M4 Customer Stickiness** — zero revenue-decline years (7/7 positive)
satisfies the "max 1 decline year, fully recovered" tier on decline-year
count alone; the top tier additionally needs receivable days stable
±10, which fails on the full-period screener-computed basis (76.7d FY19
→ 98.4d FY26, computed as Receivables÷Sales×365, screener-data — a
21.7-day lengthening). Company-disclosed net-of-GST/VAT receivable days
(AR p.57) show a materially flatter recent window: 94d (FY24), 96d
(FY25), 92d (FY26). Both readings are reported; scored on the stricter
full-period formula-consistent basis → **score 3**

**M5 Scale & Dominance** — among the four names in this run's peer set
(mcap, screener-data): NEWGEN Rs 7,087 Cr > EMUDHRA Rs 5,080 Cr > PROTEAN
Rs 1,999 Cr > QUICKHEAL Rs 827 Cr. EMUDHRA ranks 2nd by mcap and 2nd by
FY26 EBITDA margin (21.97%, behind NEWGEN's 25.78%) → "top 3 mcap AND
margin top 2" → **score 3**. Caveat: this is the run's 3 auto-selected
peers only (B00), not a verified exhaustive competitive-segment universe.

**M6 Technology / R&D** — **N/A (not in provided data), score 0.**
No R&D-to-revenue % is disclosed on a comparable multi-year basis; the
BRSR disclosure (AR p.148 area) marks the specific "sustainable R&D
capex %" question "NA." AR narrative states an "R&D team of over 200+
people" (headcount only, not spend). FY26 capitalised product
development (Rs 814.21 Mn, AR p.156, a subset of the Rs 1,853.68 Mn full
capex line per the Correction above) is 8.6% of FY26 revenue for one
year only — suggestive but does not satisfy "consistently."

**M7 Regulatory / License** — eMudhra holds a Controller of Certifying
Authorities (CCA) license (Trust Services, ~20% of FY26 revenue per
B00). Listed-player count within the licensed Certifying Authority
segment specifically is not in the provided data. **PEER DATA NEEDED →
score 0**

**M8 Distribution** — channel mix is quantified for one year (AR p.55:
Direct 60% / Partner-led 40%) but no partner-count growth trend or
"revenue per outlet" metric exists in the provided data → **score 1**

**M9 Brand** — Gross margin proxy (Revenue − Material Cost)/Revenue,
screener-data: eMudhra FY26 91.84% (material cost Rs 57.25 Cr = Raw
Material 54.75 + Δ Inventory 2.5). Peers: NEWGEN and PROTEAN report zero
in the Raw Material Cost line for all years (blank field, a data-
structure artifact of their cost classification, not a real advantage),
producing a distorted "100%" GM proxy; QUICKHEAL 98.08%. This comparison
is not meaningful. **PEER DATA NEEDED (comparable COGS/GM basis) → score
0**

**M10 Switching Costs** — revenue grew every year (7/7), but receivable
days rose 21.7 days over the full period on the formula-consistent
screener basis (see M4), which fails both the top-tier "≤10 days" test
and the "stable" qualifier on the next tier down; the rubric has no
clean slot for "perfect growth + lengthening receivables" → **score 0**
(same tension flagged in M4 and in the CASH CONVERSION load-bearing
fact; company-disclosed net-of-GST days for FY24-26 alone are flat)

**M11 Network Effects** — 8 years available (≥6 required). Latest 3-year
window (FY23→FY26) revenue CAGR = 41.3%; prior 3-year window (FY20→FY23)
= 28.8% (accelerating). Selling & admin expense as % of revenue declined
from 12.77% (FY23: 31.77/248.76) to 8.86% (FY26: 62.17/701.58). Both
conditions met → **score 5**

**M12 Negative WC / Float** — **N/A (not in provided data), score 0**,
same payables gap as B4. Standalone-only figures (AR Note 50) show
negative WC (-159d FY26, -104d FY25) but mix bases with the rest of this
analysis and are not scored.

F total: 0+5+0+3+3+0+0+1+0+0+5+0 = **17/60**

**Moats present (score ≥3):** M2 (5), M4 (3), M5 (3), M11 (5) = **4
confirmed**
**Moat classification:** 4 present → **STRONG**

---

## SCORECARD SUMMARY (CORRECTED)

| Block | Score | Max | Change |
|---|---|---|---|
| A — Return on Capital | 12 | 20 | unchanged |
| B — Cash Generation Quality | 7 | 20 | was 13, corrected |
| C — Growth | 18 | 20 | unchanged |
| D — Balance Sheet Strength | 20 | 20 | unchanged |
| E — Shareholder Alignment | 14 | 20 | unchanged |
| **Core Score** | **71** | **100** | was 77 |
| F — Quantitative Moat | 17 | 60 | unchanged |
| **Grand Total** | **88** | **160** | was 94 |

Moats confirmed: 4 (M2 Cost Advantage, M4 Customer Stickiness, M5 Scale
& Dominance, M11 Network Effects) — unchanged.
Moat classification: **STRONG** — unchanged.

Data confidence: 8 years (FY19-FY26) → **moderate** tier (7-9 band, no
downgrade required).

Deal-breaker check (ONE now triggered):
1. Block A <8 → Block A = 12, not triggered.
2. **Block B <8 → Block B = 7. TRIGGERED → max GOOD.**
3. Median ROCE <10% → 18.955%, not triggered.
4. Cumulative CFO/PAT <0.50 → 1.05x, not triggered.
5. Pledge >15% → 0%, not triggered.
6. ND/EBITDA >3x AND IC <3x → net cash / 26.9x, not triggered.
7. Revenue declined majority of years → 7/7 grew, not triggered.
8. PAT negative in any of last 3 years → FY24/25/26 all positive
   (75.06, 84.64, 107.79 Cr), not triggered.
9. History <3 years → 8 years, not triggered.

**Classification matrix:** Core 71 (60-79 band) + Moat STRONG would
ordinarily give GOOD+; **deal-breaker #2 (Block B <8) caps this at
GOOD.**

**Classification: GOOD** (was GOOD+ before correction)

**Strongest block:** D — Balance Sheet Strength (20/20; net cash,
26.9x interest coverage, 0.03x D/E — though D4's current ratio is
standalone-basis, flagged above).
**Weakest block:** B — Cash Generation Quality (7/20), now the
deal-breaker binding constraint: FY26 FCF is confirmed negative (-Rs
52.52 Cr) against a heavier capex year, even as accrual cash conversion
(CFO/PAT) keeps improving.

**Decision line:** GOOD (deal-breaker capped) on the corrected
scorecard. The two areas the operator asked this stage to check hardest
— cash conversion and the 3i Infotech tail claim — both confirm real
caution: FY26 FCF is genuinely negative (-Rs 52.5 Cr), matching the
original load-bearing fact and now the binding deal-breaker on
classification; and E4's clean 0.38% contingent-liability ratio does not
carry the Rs 128 Cr+ disputed claim that sits outside the quantified
note. The payables/WC-days picture needed to judge whether the FY26
capex spike is a one-off infrastructure build (Cryptas integration) or a
durable pattern is still not extractable from this corpus's OCR text (a
corpus problem, not answered by this correction). Flag both for stage 2+
and for claude.ai live verification.

---

## DATA NOTES

- No loss-to-profit PAT swing in FY19-FY26 (PAT positive throughout);
  CAGR edge rules not triggered.
- ROCE/ROE computed basis (FY19-FY23): Capital Employed = Equity Share
  Capital + Reserves + Borrowings (screener's 4-bucket Data_Sheet model).
  A true current/non-current liability split was attempted from the
  AR's consolidated balance sheet (p.216-217) and Note 18 Trade Payables
  (p.255) but the pdftotext-layout extraction scrambles the label/value
  pairing (values consistently appear 1-6 lines removed from their
  correct label, with the offset growing down the table); multiple
  candidate readings for the same cell diverged by up to 8x and could
  not be arbitrated with confidence, so this stage did not use them.
  The mupdf extraction (used for the FCF correction above) resolved the
  cash-flow-statement page cleanly but was not re-run against the
  balance-sheet/Note-18 pages in this pass; recommend a downstream
  verifier do so if a precise consolidated current-liabilities figure is
  needed.
- **FCF (B2/B3) corrected 2026-09-19**: now computed for FY25 and FY26
  (n=2) using the clean AR p.218 mupdf extraction; the original draft's
  FY26 figure (+Rs 51.43 Cr, from a misread capex line) is superseded by
  -Rs 52.52 Cr. FY19-FY24 capex remains not extractable from provided
  data (screener Data_Sheet has no capex line; no earlier-year AR
  cash-flow statement in this corpus). Flagged LIMITED / n=2, still
  below the pipeline's 3-year floor.
- D4 Current Ratio is standalone-basis (AR Note 50, p.364); no reliable
  consolidated figure could be extracted. Flagged for re-verification.
- M6 (R&D) and M7/M9 (peer data) marked NOT FOUND / PEER DATA NEEDED
  per protocol; scored 0, not estimated.
- M9 Gross-margin peer comparison is a proxy — GM = (Revenue − Material
  Cost)/Revenue, stated per instructions — and is distorted because 2 of
  3 peers (NEWGEN, PROTEAN) report zero in the Raw Material Cost line
  for every year in the screener Data_Sheet (a cost-classification
  artifact, not a real 100% gross margin). Not used as a scored signal
  beyond the 0 assigned.
- E2 (promoter holding, 3-year change) marked N/A: only ~1-2 years of
  data points exist in the provided corpus (see Block E).
- The FY26 AR consolidated cash-flow MD&A table (p.155-156) is clean and
  was used directly for CFO/CFI cross-checks: consolidated CFO Rs
  1,328.49 Mn (= Rs 132.85 Cr, matches screener-data exactly); consolidated
  CFI Rs -2,250.53 Mn (= Rs -225.05 Cr, vs screener-data Rs -197.76 Cr —
  a ~Rs 27 Cr gap, immaterial to sign/direction, not reconciled further
  in this stage). The mupdf extraction of AR p.218-219 (used for the FCF
  correction) confirms this same Net cash used in investing activities
  total (-2,250.53 Mn FY26 / -2,113.40 Mn FY25) line by line.
- input_gaps carried from B00 (stage 0): FRESHNESS FAIL — ICRA June-2026
  rating rationale absent (only the reaffirmation letter is held; latest
  full rationale on file is dated 02-Jun-2025). Gate recommendation caps
  at PROCEED WITH CAVEATS per B00. Not scored by this stage (no rating
  metric in the Gate 0 formula set) but carried forward per instruction.

## ANALYST NOTE

GOOD (deal-breaker capped, was GOOD+ before the FY26 capex/FCF
correction). Growth remains excellent (C=18/20, 32% revenue CAGR/30%
PAT CAGR, 7/7 positive years) and the balance sheet is genuinely clean
(D=20/20, net cash, 27x interest cover). The corrected read confirms
both operator-flagged priorities point the same direction: FY26 FCF is
confirmed negative (-Rs 52.5 Cr, AR p.218), matching the original
load-bearing fact and now the deal-breaker that caps classification at
GOOD regardless of the moat profile; and E4's clean 0.38%
contingent-liability score still cannot carry the disputed Rs 128 Cr+
3i Infotech claim, which sits in narrative disclosure only. What remains
genuinely open: whether the FY26 capex jump (Rs 832 Mn to Rs 1,854 Mn)
is a one-off Cryptas-integration/infrastructure build that reverses, or
a new steady-state spend level — the corpus does not have FY19-FY24
capex or a clean consolidated payables/WC-days trend to judge that
either way. Recommend: (1) source a clean copy of AR Note 18/BS pages
216-219 (mupdf or direct PDF read) to settle consolidated payables and
current ratio; (2) ask claude.ai / management commentary whether the
FY26 capex step-up is expected to persist into FY27; (3) continue to
treat the 3i Infotech claim as a named, unquantified tail risk
regardless of E4's score.
