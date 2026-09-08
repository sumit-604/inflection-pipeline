# STAGE 1: GATE 0 SCORECARD — Borana Weaves Ltd (BORANA)
Run date: 2026-09-07 | Model: claude-sonnet-5 | Mode: PIPELINE

Data available: 5 years (FY22 to FY26). Scoring adapted to 5-year history.
Primary sources: audited standalone results (Results_Q4FY26_and_FY26,
Results_Q4FY25_and_FY25), RHP restated statements (FY22-FY24), AR FY2026,
shareholding pattern filings. Screener export used only where it does not
conflict with an audited filing; every conflict is resolved in favour of
the audited number and both figures are shown.

Basis notes (apply throughout):
- EBIT = PBT + Finance costs (computed; screener carries no ROCE/ROE field
  for this company, so both are computed here per the formula definitions).
- Capital Employed = Total Assets − Total Current Liabilities (per year-end
  balance sheet).
- Working Capital Days computed on a Revenue basis throughout (Receivable,
  Inventory and Payable days all ÷ Revenue × 365); COGS basis not used.
- EBITDA = Revenue from operations − (Cost of materials + change in
  inventory + Employee cost + Other expenses), i.e. Total Expenses less
  Depreciation and Finance costs. Other income excluded.

---

## SPEAR LOAD-BEARING FACTS — VERIFICATION

**1. FY26 EBITDA margin ~23.6% and cost stack.**
Confirmed. Audited FY26 (Results_Q4FY26_and_FY26 p.3, cross-verified by direct
PDF read against the OCR twin): Revenue from operations Rs 388.59cr, Cost of
materials consumed Rs 227.78cr, Employee cost Rs 28.14cr (all match the
screener-data figures cited in the brief). Power and Fuel Rs 23.47cr and
Other Mfr. Exp Rs 15.56cr are screener-data line items that net into the
audited "Other expenses" Rs 41.09cr line (Results_Q4FY26 p.3); this
sub-split is not separately re-stated in the audited P&L but reconciles
(23.47+15.56+1.47 Selling&admin+0.41 Other Expenses = 40.91cr vs printed
41.09cr, a Rs 0.18cr rounding/regroup gap, immaterial).
Computed EBITDA FY26 = Revenue 388.59 − (Total Expenses 318.38 − Depreciation
17.81 − Finance costs 3.49) = Rs 91.52cr. Margin = 91.52/388.59 = **23.55%**
(Results_Q4FY26_and_FY26 p.3, direct PDF read). Matches the spear brief.
Quarterly margin history (screener-data, Operating Profit ÷ Sales) confirms
the volatility flagged in the brief: Q4FY24 margin = 16.68/61.36 = **27.19%**,
falling to Q2FY25 (Sep-2024) = 11.68/70.81 = **16.49%** — the ~16.5% low cited
— before recovering through FY26 (Q4FY26 = 25.61/100.73 = 25.43%). The
full-year trend (FY22 12.22% → FY23 19.25% → FY24 20.68% → FY25 21.76% →
FY26 23.55%, all computed from audited/RHP P&L figures) reads as smooth
expansion; the quarterly series shows it was not smooth underneath. This
quarter-level swing straddles the anti-dumping-duty change window named in
the brief and is not resolved by this stage — it is a diligence item, not a
scorecard input.

**2. Related-party yarn/input purchases.**
Partially confirmed. AR FY2026 Note "Related Party Transaction," section
I.Purchase (AR_FY2026 p.117): FY25 Rs 1,583.37 lakh (Rs 15.83cr) from R&B
Denims Limited (Rs 625.31 lakh) and RB Industries (Rs 958.06 lakh); FY26
collapsed to Rs 10.11 lakh (Rs 0.10cr) from Ricon Textiles Private Limited
only. Both counterparties are promoter-group entities (R&B Denims and RB
Industries appear as promoter-group shareholders in the pre-listing
shareholding pattern, Shareholding_27.05.2025 p.14). NOT FOUND: whether
these purchases are yarn specifically (the note does not itemise by material
type) and NOT FOUND: the price basis / arm's-length confirmation for these
transactions — the AR note discloses rupee value and counterparty only. The
FY25→FY26 collapse in related-party purchases (Rs 15.83cr to Rs 0.10cr) is
itself a fact worth carrying forward to diligence.

**5. Capex vs three flat revenue quarters.**
Confirmed. Audited FY26 balance sheet (Results_Q4FY26_and_FY26 p.2, direct
PDF read): Capital work-in-progress Rs 80.94cr (8,093.62 lakh) against Net
Block (PP&E + ROU) Rs 147.61cr (14,648.93+112.14 lakh) at FY26 close.
Audited FY26 cash flow (Results_Q4FY26_and_FY26 p.4): Purchase of PP&E
including CWIP Rs 178.98cr, Net cash used in investing activities Rs
178.69cr (17,868.82 lakh) — matches the brief. Quarterly revenue
(screener-data, quarters row): Q3FY26 Rs 111.36cr, Q4FY26 Rs 100.73cr,
Q1FY27 Rs 100.84cr — three flat quarters against a near-doubling of the
asset base, confirmed. This stage does not resolve capacity-commissioning
timing; it is named here as a diligence item.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 20/20

Computed ROCE (EBIT = PBT + Finance costs; Capital Employed = Total Assets −
Total Current Liabilities, year-end):

| FY | PBT (cr) | Finance costs (cr) | EBIT (cr) | Total Assets (cr) | Curr. Liab (cr) | Cap. Employed (cr) | ROCE |
|----|---------|---------------------|-----------|--------------------|-------------------|----------------------|------|
| 22 | 2.19 | 1.40 | 3.59 | 31.90 | 10.93 | 20.97 | 17.10% |
| 23 | 19.90 | 2.21 | 22.11 | 74.98 | 29.04 | 45.94 | 48.12% |
| 24 | 28.39 | 4.18 | 32.57 | 137.05 | 39.95 | 97.10 | 33.54% |
| 25 | 49.12 | 5.05 | 54.17 | 155.95 | 29.78 | 126.17 | 42.94% |
| 26 | 78.40 | 3.49 | 81.89 | 366.37 | 28.13 | 338.24 | 24.21% |

(FY22/23 PBT and Interest: RHP_Borana_Weaves_2025 p.83; FY22/23 Total
Assets/Current Liabilities: RHP p.82. FY24 figures: Results_Q4FY25_and_FY25
p.13 comparator column, cross-checked against RHP p.82/83. FY25 figures:
Results_Q4FY25_and_FY25 p.12-13. FY26 figures: Results_Q4FY26_and_FY26 p.2-3,
direct PDF read.)

**A1 Median ROCE** (sorted: 17.10, 24.21, 33.54, 42.94, 48.12 → median 33.54%):
≥25% → **5**
**A2 Minimum single-year ROCE**: 17.10% (FY22) ≥15% → **5**
**A3 Median ROE**: PAT ÷ average Net Worth; FY22 uses closing net worth only
(opening unavailable — company capitalised with Rs 1 lakh share capital at
incorporation, RHP p.82).

| FY | PAT (cr) | Opening NW (cr) | Closing NW (cr) | Avg NW (cr) | ROE |
|----|----------|------------------|-------------------|--------------|-----|
| 22 | 1.80 | n/a (closing only) | 1.81 | 1.81 | 99.4% |
| 23 | 16.30 | 1.81 | 24.11 | 12.96 | 125.8% |
| 24 | 23.59 | 24.11 | 47.70 | 35.91 | 65.7% |
| 25 | 40.20 | 47.70 | 87.55 | 67.63 | 59.4% |
| 26 | 64.61 | 87.55 | 281.58 | 184.57 | 35.0% |

Median (sorted 35.0, 59.4, 65.7, 99.4, 125.8) = 65.7% ≥20% → **5**
**A4 ROCE trend, latest (24.21%) vs earliest (17.10%)**: latest ≥ earliest → **5**

**DISTORTION NOTE (does not change the score, changes how to read it):**
The FY22-23 ROE figures (99-126%) are an artifact of a near-zero opening
equity base (Rs 1-24 lakh), not a demonstration of durable high-return
compounding on a mature capital base. The FY26 ROCE (24.21%) is understated
relative to the FY23-25 run rate (33-48%) because year-end Capital Employed
carries the full post-IPO equity (Rs 281.58cr closing) and Rs 80.94cr of
idle CWIP that earned nothing in FY26 — per the run brief, this spot figure
should not be read as a trend break.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 6/20 — WEAKEST BLOCK

| FY | CFO (cr) | Capex (cr, cash-flow basis) | FCF (cr) |
|----|----------|-------------------------------|----------|
| 22 | -8.33 | 15.78 | -24.11 |
| 23 | 6.90 | 21.91 | -15.02 |
| 24 | 22.13 | 48.42 | -26.29 |
| 25 | 22.64 | 9.97 | 12.67 |
| 26 | 36.96 | 178.98 | -142.02 |

(FY22/23 CFO and capex: RHP p.84-85. FY24 CFO/capex: Results_Q4FY25_and_FY25
p.14 comparator column [22.13cr; screener-data shows 22.46cr, audited
figure used]. FY25: Results_Q4FY25_and_FY25 p.14. FY26: Results_Q4FY26_and_FY26
p.4, direct PDF read [CFO Rs 36.96cr; screener-data shows Rs 44.4cr — the
Rs 7.44cr gap traces to "IPO Expenses written off Rs 743.65 lakh," an item
the audited cash flow nets inside operating working-capital movements
(Results_Q4FY26 p.4) that screener-data appears to classify differently;
audited figure used per sourcing rule]).

**B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO = 80.31cr, ΣPAT = 146.50cr →
0.548. Band 0.50-0.69 → **1**. (This clears the 0.50 deal-breaker threshold
by 0.048 — a near miss, not a pass by a comfortable margin.)
**B2 FCF-positive years**: 1 of 5 (FY25 only) = 20% → **0**
**B3 Cumulative FCF ÷ Cumulative PAT**: ΣFCF = -194.77cr ÷ 146.50cr = -1.33
(negative) → **0**
**B4 Change in WC Days, latest vs earliest**: see table below; FY26 66.45
days vs FY22 90.09 days = -23.64 days (decreased >5) → **5**

Working Capital Days (Revenue basis throughout):

| FY | Receivable days | Inventory days | Payable days | WC days |
|----|-------------------|------------------|-----------------|---------|
| 22 | 60.87 | 32.19 | 2.97 | 90.09 |
| 23 | 19.99 | 54.66 | 13.36 | 61.29 |
| 24 | 20.26 | 43.58 | 24.42 | 39.42 |
| 25 | 27.43 | 31.96 | 4.74 | 54.65 |
| 26 | 22.21 | 44.46 | 0.22 | 66.45 |

block_b_trend = **deteriorating**. The one number: WC days bottomed at 39.4
(FY24) and has since risen to 66.5 (FY26), +27 days in two years, driven by
inventory build (31.96→44.46 days) and payables collapsing toward zero
(24.42→0.22 days — Borana is no longer stretching suppliers at all). B4
scores on endpoint-to-endpoint (FY22 vs FY26) and nets to an improvement,
but that masks a U-shape; the recent direction is the opposite of what B4
alone shows.

---

## BLOCK C: GROWTH (Max 20) — Score: 20/20

Revenue (cr): FY22 42.33 → FY23 135.40 → FY24 199.06 → FY25 290.31 → FY26
388.59 (RHP p.83 for FY22-24; Results_Q4FY25 p.12 for FY25; Results_Q4FY26
p.3 for FY26, all audited).
PAT (cr): FY22 1.80 → FY23 16.30 → FY24 23.59 → FY25 40.20 → FY26 64.61
(same sources).

**C1 Revenue CAGR** (FY22→FY26, 4 years): (388.59/42.33)^(1/4)-1 = **74.1%**
≥20% → **5**
**C2 PAT CAGR** (FY22→FY26, 4 years): (64.61/1.80)^(1/4)-1 = **144.8%** ≥20%
→ **5**
**C3 Positive YoY revenue years**: 4 of 4 transitions positive (FY22→23,
23→24, 24→25, 25→26) = 100% → **5**
**C4 PAT CAGR − Revenue CAGR** = 144.8 − 74.1 = **+70.7pp** ≥+3pp → **5**

**BASE-EFFECT NOTE:** These CAGRs compound off a tiny FY22 base (Revenue
Rs 42cr, PAT Rs 1.8cr) in a company's second full year of scaled operation.
The percentages are correct arithmetic but should not be read as evidence
of a mature, repeatable growth engine; FY24→FY26 (a more representative
two-year window) shows Revenue CAGR of (388.59/199.06)^(1/2)-1 = 39.7% and
PAT CAGR of (64.61/23.59)^(1/2)-1 = 65.4% — still strong, but well below
the headline FY22-anchored figures.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 18/20

Latest = FY26 (Results_Q4FY26_and_FY26 p.2, direct PDF read).
Total borrowings (incl. lease liabilities, NC+CL) = Rs 70.81cr. Cash = Rs
1.68cr. Net Debt = Rs 69.13cr. EBITDA (per basis note above) = Rs 91.52cr.
Total Current Assets = Rs 121.91cr. Total Current Liabilities = Rs 28.13cr.
Total Equity = Rs 281.58cr.

**D1 Net Debt ÷ EBITDA**: 69.13/91.52 = 0.755x. Band 0-1.0x → **4**
**D2 Interest Coverage** (EBIT 81.89cr ÷ Finance costs 3.49cr) = 23.46x
≥10x → **5**
**D3 Debt ÷ Equity**: 70.81/281.58 = 0.252x. Band 0.1-0.5 → **4**
**D4 Current Ratio**: 121.91/28.13 = 4.33x ≥2.0x → **5**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 15/20

**E1 Promoter holding (latest quarter, 30-Jun-2026)**: 65.24%
(Shareholding_30.06.2026 p.4/6) ≥60% → **5**
**E2 Promoter holding change over 3 years**: **N/A (not in provided data)**.
Borana listed 27-May-2025; no public shareholding pattern exists further
back than the pre-listing filing dated 23-May-2025, which itself shows
65.24% (Shareholding_27.05.2025 p.4/6) — identical to the latest quarter.
A genuine 3-year window cannot be built from a 16-month listed history.
Score **0** per the grounding rule (no estimate substituted). Best
available evidence: promoter holding has been flat at 65.24% across the
entire listed history (13 months) and shows no pledge.
**E3 Promoter pledge (latest)**: 0 shares pledged, "Whether any shares held
by promoters are encumbered under Pledged? No" (Shareholding_30.06.2026
p.2) → 0% → **5**
**E4 Contingent liabilities ÷ Net Worth (latest, FY26)**: Contingent
liabilities (bank guarantees for Ricon Textile Limited, HDFC Cash Credit +
Term Loan) = Rs 0 as at 31-03-2026 (both lines show "-"; FY25 comparator was
Rs 9.82cr) (AR_FY2026 p.127, direct PDF read). 0 ÷ Net Worth 281.58cr = 0%
<5% → **5**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 27/60 — FORTRESS (6 moats present)

Peer set: FILATEX (Filatex India), SANGAMIND (Sangam India), SANATHAN
(Sanathan Textiles) — all screener-data. Peer EBITDA margin computed as
Revenue − (RM + Δinventory + Power&Fuel + Other Mfr. Exp + Employee +
Selling&admin + Other Expenses), same basis as Borana.

| Peer | FY24 margin | FY25 margin | FY26 margin |
|------|-------------|-------------|-------------|
| FILATEX | n/a (screener gap FY20-24) | 5.98% | 8.73% |
| SANGAMIND | 6.44% | 9.25% | 13.70% |
| SANATHAN | 7.89% | 9.33% | 3.35% |
| **Borana** | **20.68%** | **21.76%** | **23.55%** |

FILATEX-Data_Sheet.csv exports only FY2015-19 then jumps to FY25-26 (a
screener export gap, not a company data gap); FY24 comparator unavailable
for FILATEX. FY26 peer median = 8.73% (FILATEX). Borana is 14.8pp above the
FY26 peer median and above every peer in every year shown.

**M1 Pricing Power**: margin expanded FY22 12.22% → FY26 23.55% (+11.3pp,
≥2pp) AND revenue CAGR 74.1% (≥10%) → **5**
**M2 Cost Advantage vs peer median** (FY26): +14.8pp above → **5**
**M3 Capital Efficiency**: FAT = Revenue 388.59 ÷ Net Block 147.61 = 2.63x
(>2x); ROCE 24.21% (>15% but not >20% threshold pairing required for 5,
since 5 requires FAT>3x) → **3**
**M4 Customer Stickiness**: zero revenue-decline years, but receivable days
are NOT stable ±10 across the full window (60.9 days FY22 vs 20-27 days
FY23-26) → does not clear the "zero decline AND stable ±10" bar for 5;
zero decline years (better than the "max 1 decline" tier) → **3**
**M5 Scale & Dominance**: **PEER DATA NEEDED** for the full listed-segment
mcap ranking (only 3 named peers available, not an exhaustive segment
list). Among the 3 named peers, Borana mcap (Rs 870.03cr) is the smallest
of the four (FILATEX Rs 3,405.86cr, SANGAMIND Rs 2,884.74cr, SANATHAN Rs
3,968.49cr — all screener-data) despite having the highest margin → **0**
**M6 Technology/R&D**: no R&D disclosure in any provided source →
**N/A (not in provided data)** → **0**
**M7 Regulatory/License**: unregulated segment (greige fabric weaving; the
anti-dumping duty referenced in the run brief is a trade-policy input to
the industry, not a licence/quota on Borana) → **0**
**M8 Distribution**: no quantified distribution network in provided sources
(B2B weaving, not a distribution-network business model) →
**N/A (not in provided data)** → **0**
**M9 Brand** (GM proxy = (Revenue−Material Cost)÷Revenue, stated per rule):
Borana FY26 = (388.59−227.78)/388.59 = 41.39%. Peer FY26 GM proxy: FILATEX
24.30%, SANATHAN 27.92%, SANGAMIND 45.51%; peer median = 27.92%. Borana is
+13.5pp above peer median (≥10pp) AND revenue CAGR 74.1% (≥10%) → **5**
**M10 Switching Costs**: revenue grew every year AND receivable days moved
-38.7 days over the period (a decrease, which clears "rose ≤10 days") →
**5**
**M11 Network Effects**: only 5 years of history, below the 6-year
two-window test threshold — scored conservatively on the overall trend and
stated so. Revenue CAGR 74.1% (≥20%) but Selling & admin expense as % of
revenue rose slightly (0.07% FY22 → 0.38% FY26, screener-data) rather than
holding stable/declining → **1**
**M12 Negative WC / Float**: WC days never negative; 4 of 5 years exceed 45
days (FY22 90.1, FY23 61.3, FY25 54.7, FY26 66.5), only FY24 (39.4) falls in
the 15-45 band → majority-year classification is >45 days → **0**

Moat profile:
```
M1  Pricing Power        [#####] 5  present
M2  Cost Advantage       [#####] 5  present
M3  Capital Efficiency   [###..] 3  present
M4  Customer Stickiness  [###..] 3  present
M5  Scale & Dominance    [.....] 0
M6  Technology/R&D       [.....] 0
M7  Regulatory/License   [.....] 0
M8  Distribution         [.....] 0
M9  Brand                [#####] 5  present
M10 Switching Costs      [#####] 5  present
M11 Network Effects      [#....] 1
M12 Negative WC/Float    [.....] 0
```
Moats present (score ≥3): M1, M2, M3, M4, M9, M10 = **6** → **FORTRESS**
(6+ present threshold met, but note M5-M8 and M12 are all zero — the moat
is narrow-and-deep [pricing, cost, brand-proxy, switching] rather than
broad; scale, regulation, distribution and float contribute nothing).

---

## CLASSIFICATION

Data confidence: 5 years (FY22-FY26) → **5-6 band: lower confidence, flag
"may not have seen full cycle."** No automatic downgrade (downgrade only
applies at 3-4 years). history_downgrade = **false**.

| Block | Score | Max |
|-------|-------|-----|
| A — Return on Capital | 20 | 20 |
| B — Cash Generation Quality | 6 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 18 | 20 |
| E — Shareholder Alignment | 15 | 20 |
| **Core Score** | **79** | **100** |
| F — Moat Score | 27 | 60 |
| **Grand Total** | **106** | **160** |

Moat classification: FORTRESS (6 moats present).
Raw matrix lookup: Core 79 sits in the 60-79 band; FORTRESS/STRONG moat →
**GOOD+**.

**Deal-breaker check:**
1. Block A <8 → not triggered (A=20)
2. **Block B <8 → TRIGGERED (B=6) → caps classification at max GOOD**
3. Median ROCE <10% → not triggered (33.54%)
4. Cumulative CFO/PAT <0.50 → not triggered (0.548 — a 0.048 near miss)
5. Pledge >15% → not triggered (0%)
6. ND/EBITDA >3x AND IC <3x → not triggered (0.755x / 23.46x)
7. Revenue declined in majority of years → not triggered (0 decline years)
8. PAT negative in any of last 3 years → not triggered (all positive)
9. History <3 years → not triggered (5 years)

**Final classification: GOOD** (capped down from GOOD+ by deal-breaker
rule 2 — Block B, Cash Generation Quality, scores 6/20).

Strongest block: A (Return on Capital) and C (Growth), both 20/20 — but
both carry base-effect/tiny-denominator caveats documented above; the
cleanest strong score without an asterisk is D (Balance Sheet Strength,
18/20).
Weakest block: B (Cash Generation Quality, 6/20) — cumulative FCF is
deeply negative (-Rs 194.8cr over 5 years) because the FY26 capex cycle
(Rs 178.98cr) outran operating cash generation; only 1 of 5 years produced
positive free cash flow.

**Decision line:** GOOD (capped from GOOD+ by the Block B deal-breaker,
rule 2). The return, growth and balance-sheet profile is strong on paper,
but every year bar FY25 burned free cash, and the two headline growth
blocks (A, C) are inflated by a near-zero FY22 starting base. Proceed to
Stage 2 with the cash-conversion weakness and the FY26 capex-versus-flat-
revenue question (spear fact 5) named as first-priority diligence items,
alongside the unresolved related-party purchase price basis (spear fact 2).

---
## DATA NOTES
- Loss-to-profit swings: none (PAT positive every year, FY22-FY26).
- Proxy bases used: M9 Brand test uses GM proxy (Revenue − Material Cost) ÷
  Revenue, stated per the scoring rule; Working Capital Days computed on a
  Revenue basis throughout (not COGS), stated per the formula rule.
- PEER DATA NEEDED: M5 Scale & Dominance (full segment mcap ranking beyond
  the 3 named peers).
- Screener-vs-audited conflicts resolved to audited: FY26 CFO (audited
  Rs 36.96cr vs screener-data Rs 44.4cr, Rs 7.44cr IPO-expense-write-off
  classification gap); FY26 Revenue (audited Rs 388.59cr vs screener-data
  Rs 388.52cr, immaterial); FY24 CFO (audited/RHP Rs 22.13cr vs
  screener-data Rs 22.46cr, immaterial); FY23 Interest (RHP Rs 2.21cr vs
  screener-data Rs 2.26cr, immaterial).
- E2 (promoter holding 3-year change) marked N/A — company listed only 13
  months as of the shareholding filing used; a genuine 3-year window does
  not exist in any provided source.
- The four OCR-scanned filings named in the run brief (FY26 results,
  Q3FY26 results, AR FY2024, 11-Aug-2026 filing) — every figure drawn from
  the FY26 results PDF in this scorecard (balance sheet, P&L, cash flow)
  was independently confirmed by a direct PDF page read against the OCR
  text twin, per the run's verification instruction. AR FY2026 (not one of
  the four flagged OCR files) showed a garbled table-extraction on the
  contingent-liabilities note; that figure was also confirmed by direct
  PDF read (AR_FY2026 p.127).

## INPUT GAPS (carried from B00, plus one addition)
- inputs/research/ empty, no broker note.
- NO-CONCALL MODE: one Borana transcript only (Q3FY26).
- Missing Brickwork rating rationale for the 11-May-2026 upgrade to BWR
  BBB+/Stable.
- Missing text of the SEBI Section 11C(9) search order cited in the
  25-Apr-2026 Reg 30 filing.
- No standalone Q1FY27 results filing, only the board-meeting outcome.
- Screener CSV export defect (screener-Profit_Loss.csv, -Balance_Sheet.csv,
  -Cash_Flow.csv, -Quarters.csv export header-only) — not a data gap, the
  Data_Sheet.csv carries the full series.
- ADDED: FILATEX-Data_Sheet.csv exports only FY2015-19 then jumps to
  FY25-26 (a screener export gap for that peer, not a Borana data gap);
  FILATEX FY24 EBITDA margin unavailable for the M2/peer table.
- ADDED: Related-party purchase note (AR_FY2026 p.117) does not itemise
  purchases by material type (yarn vs other input) or disclose the price
  basis / arm's-length confirmation — spear fact 2 only partially
  resolvable from provided sources.

---

```yaml
stage: B01-gate0
company: "BORANA"
run_date: "2026-09-07"
model: claude-sonnet-5
status: complete
input_gaps:
  - "inputs/research/ empty, no broker note"
  - "NO-CONCALL MODE: one transcript only (Q3FY26)"
  - "Missing Brickwork rating rationale for 11-May-2026 upgrade to BWR BBB+/Stable"
  - "Missing text of SEBI Section 11C(9) search order (25-Apr-2026 Reg 30 filing)"
  - "No standalone Q1FY27 results filing, only board-meeting outcome"
  - "Screener CSV export defect (Profit_Loss/Balance_Sheet/Cash_Flow/Quarters header-only) - not a data gap, Data_Sheet.csv carries full series"
  - "FILATEX-Data_Sheet.csv exports only FY2015-19 then FY25-26; FILATEX FY24 EBITDA margin unavailable"
  - "AR FY2026 related-party purchase note does not itemise by material type or disclose price basis; spear fact 2 only partially resolved"
flags: []
data_years: 5
fy_range: "FY22 to FY26"
blocks: {A: 20, B: 6, C: 20, D: 18, E: 15}
core_score: 79
moat_score: 27
grand_total: 106
moats_confirmed: 6
moat_class: "FORTRESS"
classification: "GOOD"
deal_breakers:
  - "Rule 2: Block B (Cash Generation Quality) = 6, below the 8-point floor -> caps classification at max GOOD, overriding the GOOD+ the raw Core/Moat matrix lookup would otherwise assign"
history_downgrade: false
data_notes:
  - "No loss-to-profit swings; PAT positive every year FY22-FY26"
  - "M9 Brand test uses GM proxy (Revenue - Material Cost) / Revenue, stated per rule"
  - "Working Capital Days computed on Revenue basis throughout (not COGS), stated per rule"
  - "M5 Scale & Dominance: PEER DATA NEEDED for full segment mcap ranking beyond 3 named peers"
  - "FY26 CFO: audited Rs 36.96cr used over screener-data Rs 44.4cr (Rs 7.44cr gap traces to IPO-expense write-off classification, Results_Q4FY26 p.4)"
  - "FY26/FY24 Revenue and FY23 Interest: minor audited-vs-screener deltas, all immaterial, audited figure used per sourcing rule"
  - "E2 (promoter holding 3-yr change) marked N/A: company listed only 13 months, no 3-year window exists in any provided source"
block_b_trend: "deteriorating - WC days bottomed at 39.4 (FY24), risen to 66.5 (FY26), +27 days in two years, driven by inventory build and payables collapsing toward zero (24.4 to 0.2 days); B4's endpoint score (FY22 90.1 vs FY26 66.5, net improvement) masks this recent reversal"
analyst_note: "Classification GOOD, capped down from a raw GOOD+ (Core 79, FORTRESS moat) solely by the Block B deal-breaker: cumulative FCF is -Rs194.8cr over 5 years and only 1 of 5 years produced positive FCF, because FY26 capex (Rs178.98cr, mostly still CWIP) outran operating cash generation (CFO Rs36.96cr). Blocks A and C both score 20/20 but are inflated by a near-zero FY22 base (Revenue Rs42cr, PAT Rs1.8cr, opening equity ~Rs1.8cr) - FY24-26 CAGRs are materially lower (Revenue 39.7%, PAT 65.4%) and still strong but not headline-strong. FY26 ROCE (24.2%) is a spot figure depressed by mid-year equity raise plus idle CWIP per the run brief; FY23-25 ROCE ran 33-48%, the more representative range. Moat is narrow-and-deep (pricing power, cost advantage, brand-proxy margin, switching costs all score 5) with zero contribution from scale, regulation, distribution or float (M5-M8, M12 all 0) - six figures short of a broad moat. Cumulative CFO/PAT (0.548) clears the 0.50 deal-breaker by only 0.048, a near miss worth carrying into Stage 2. Quarterly margin history (27.2% Q4FY24 to 16.5% Q2FY25 to 25.4% Q4FY26) shows real volatility the smooth annual series hides."
```
