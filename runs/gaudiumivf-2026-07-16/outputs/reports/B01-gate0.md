# GATE 0 SCORECARD — Gaudium IVF and Women Health Ltd (GAUDIUMIVF)
Run date: 2026-07-16 | Model: Sonnet 5 | Stage: B01-gate0

Data available: 4 years (FY2023 to FY2026), consolidated basis. Scoring adapted
to 4-year history.

**Basis note (read before the numbers):** Gaudium listed on NSE/BSE on 27 Feb
2026 (RHP dated 13 Feb 2026). The RHP's own Restated Consolidated Financial
Information covers only FY2023–FY2025 plus a stub half-year (period ended 30
Sep 2025); FY2026 is sourced from the audited standalone/consolidated results
filed 28 May 2026. Screener.in's Data_Sheet.csv also carries an FY2022 column,
but (a) it is not in the RHP's restated set and (b) RHP cash-flow note (b)
states FY2023 cash flows reflect the first-time consolidation of an acquired
subsidiary (M/s Gaudium Bawa IVF), making FY2022 non-comparable on a
consistent consolidated basis. FY2022 is therefore excluded from the scored
window and only referenced in data_notes. All P&L/BS/CF figures below are
**consolidated** (Group), cross-checked between Data_Sheet.csv, the RHP
restated statements, and the FY26 audited results — all three sources tie out.

Sources used: RHP (Gaudium_RHP.pdf) restated consolidated financials p.75–79,
122–123, 255–260, 266; RHP capital structure/shareholding p.88–95; FY26
audited standalone+consolidated results (results PDF, board outcome
18-Mar-2026 for 9M and 28-May-2026 for FY26); screener-Data_Sheet.csv
(cross-check only, since screener-Profit_Loss/Balance_Sheet/Cash_Flow/Quarters
CSVs were exported empty — headers only, no data rows).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

RoCE and RoE use the RHP's own disclosed KPI formulas (screener.in's own
ROCE/ROE fields were not populated — Data_Sheet.csv and the ratio CSVs
contained no data rows — so the source-provided RHP figures are used for
FY23–FY25, "computed" using the identical RHP formula for FY26).

RoCE (RHP definition: EBIT ÷ (Net worth + Total Borrowings + Lease
Liabilities + Deferred Tax Liabilities)):

| FY | RoCE | Source |
|---|---|---|
| FY23 | 54.40% | RHP p.123, KPI table |
| FY24 | 38.74% | RHP p.123, KPI table |
| FY25 | 39.37% | RHP p.123, KPI table |
| FY26 | 20.11% | computed — EBIT 3,568.72L ÷ (NW 15,230.21L + Borrowings 2,307.48L + Lease 149.54L + DTL 59.39L) = 20.11%, audited consolidated BS/P&L, results PDF (28-May-2026) |

RoE / RoNW (RHP definition: PAT ÷ Net worth, closing basis, not averaged):

| FY | RoE | Source |
|---|---|---|
| FY23 | 59.51% | RHP p.123, KPI table |
| FY24 | 38.23% | RHP p.123, KPI table |
| FY25 | 41.31% | RHP p.123, KPI table |
| FY26 | 16.08% | computed — PAT 2,448.85L ÷ Net worth 15,230.21L, audited consolidated, results PDF |

**A1 Median RoCE**: sorted {20.11, 38.74, 39.37, 54.40} → median = 39.06% →
**≥25% band → score 5**

**A2 Minimum single-year RoCE**: 20.11% (FY26) → **≥15% band → score 5**

**A3 Median RoE**: sorted {16.08, 38.23, 41.31, 59.51} → median = 39.77% →
**≥20% band → score 5**

**A4 RoCE trend, latest vs earliest**: FY26 20.11% vs FY23 54.40% = decline of
34.29pp → **>5pp decline → score 0**
*(Note: this decline is substantially a denominator effect — see data_notes.
FY26's capital-employed base was inflated by ~Rs 81 Cr of IPO proceeds parked
in bank deposits that had not yet been deployed into operations as of
31-Mar-2026, per the IPO-proceeds-utilisation table in the FY26 results PDF.)*

**Block A = 5+5+5+0 = 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO, Capex (Purchase of PPE + Intangibles, ex-acquisitions) and FCF, all
consolidated:

| FY | CFO (₹L) | Capex (₹L) | FCF (₹L) | PAT (₹L) |
|---|---|---|---|---|
| FY23 | 2,385.34 | 1,525.64 | 859.70 | 1,352.54 |
| FY24 | 344.06 | 278.66 | 65.40 | 1,031.69 |
| FY25 | 871.76 | 887.84 | -16.08 | 1,912.74 |
| FY26 | 724.72 | 671.91 | 52.81 | 2,448.85 |
| **Cumulative** | **4,325.88** | **3,364.05** | **961.83** | **6,745.82** |

Source: RHP restated Statement of Cash Flows p.78 (FY23–FY25); FY26 audited
consolidated Statement of Cash Flows (results PDF, 28-May-2026) — "Net cash
[used in/generated from] operating activities" line 724.72L; FY26 Capex =
"Purchase of PPE incl. ROU" 213.58L + "Development cost of intangible asset
under development" 458.33L = 671.91L.

**B1 Cumulative CFO ÷ Cumulative PAT** = 4,325.88 ÷ 6,745.82 = 64.1% →
**0.50–0.69 band → score 1**

**B2 FCF-positive years** = 3 of 4 (FY23, FY24, FY26 positive; FY25 negative
-16.08L) = 75% → **75-99% band → score 4**

**B3 Cumulative FCF ÷ Cumulative PAT** = 961.83 ÷ 6,745.82 = 14.3% →
**<0.20 band → score 0**

**B4 Change in WC Days, latest vs earliest**: FY23 = 11.32 days → FY26 =
156.33 days → increase of **145.0 days → >15 days increase → score 0**
(detail in block_b_trend below)

**Block B = 1+4+0+0 = 5/20** — triggers deal-breaker #2 (Block B<8 → max GOOD)

---

## BLOCK C: GROWTH (Max 20)

| FY | Revenue (₹L) | PAT (₹L) |
|---|---|---|
| FY23 | 4,423.69 | 1,352.54 |
| FY24 | 4,789.01 | 1,031.69 |
| FY25 | 7,072.40 | 1,912.74 |
| FY26 | 10,435.70 | 2,448.85 |

Source: RHP restated P&L p.76 (FY23–FY25); consolidated audited P&L (results
PDF, 28-May-2026) for FY26. Cross-checked against screener-Data_Sheet.csv
Sales/Net profit rows FY23–FY26 — all tie out.

**C1 Revenue CAGR** (FY23→FY26, 3yr) = (104.357/44.2369)^(1/3)-1 = 33.12% →
**≥20% band → score 5**

**C2 PAT CAGR** (FY23→FY26, 3yr) = (24.4885/13.5254)^(1/3)-1 = 21.89% →
**≥20% band → score 5**

**C3 Positive YoY revenue years**: FY24>FY23, FY25>FY24, FY26>FY25 — 3 of 3
transitions positive = 100% → **score 5**

**C4 PAT CAGR − Revenue CAGR** = 21.89% − 33.12% = -11.23pp →
**<-8pp band → score 0** (growth is real, but PAT is not compounding as fast
as revenue — margin compression, see M1 below)

**Block C = 5+5+5+0 = 15/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

FY26 consolidated audited balance sheet (results PDF, 28-May-2026):

- Total Borrowings (current, non-current is nil) = 2,307.48L
- Lease Liabilities (current+non-current) = 149.54L
- Cash & Cash Equivalents = 878.57L
- Net Worth = 15,230.21L
- EBITDA (computed: PBT 3,219.56 + Finance cost 349.16 + D&A 254.79 − Other
  income 53.12) = 3,770.39L
- EBIT = 3,568.72L; Interest (finance cost) = 349.16L
- Current Assets = 7,330.20L; Current Liabilities = 3,852.73L

**D1 Net Debt ÷ EBITDA** = (2,307.48 − 878.57) ÷ 3,770.39 = 1,428.91 ÷
3,770.39 = 0.379x → **0-1.0x band → score 4**
*(Formula uses reported Cash & Equivalents only. Note: the company also holds
Rs 8,113.08L of bank deposits with 3–12 month maturity, booked as non-current
"Other Financial Assets" — not cash-equivalents by definition — largely
unutilised IPO proceeds. Including this near-cash pile would flip the company
to net-cash. Scored per strict formula definition; near-cash noted for
context.)*

**D2 Interest Coverage (EBIT ÷ Interest)** = 3,568.72 ÷ 349.16 = 10.22x →
**≥10x band → score 5**

**D3 Debt ÷ Equity** (Borrowings + Lease Liabilities, consistent with the
prior lead) = (2,307.48+149.54) ÷ 15,230.21 = 2,457.02 ÷ 15,230.21 = 0.161x →
**0.1-0.5x band → score 4**. [Borrowings-only basis: 2,307.48÷15,230.21 =
0.151x — same band.] Cross-check for FY25 on the identical basis:
(1,720.71+172.73+149.54+17.92)÷4,629.74 = 2,060.90÷4,629.74 = 0.445x. **The
prior lead's "D/E fell 0.45x FY25 → 0.16x FY26" is confirmed and anchored**
(RHP p.75/consolidated audited BS).

**D4 Current Ratio** = 7,330.20 ÷ 3,852.73 = 1.90x → **1.5-1.99 band → score 4**

**Block D = 4+5+4+4 = 17/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding (latest available)** = 71.30% (post-offer, fully
diluted) — RHP Capital Structure p.90, Post-Offer indicative basis. Actual
IPO completed exactly as structured in the RHP (Fresh issue 1,13,92,500
shares / Rs 9,000.08L; OFS 94,93,700 shares / Rs 7,500.02L — both match the
FY26 results PDF note 6 exactly), so the RHP indicative post-offer % is a
reliable proxy for actual post-listing holding. **No actual post-listing
shareholding-pattern (BSE/NSE Reg. 31) filing was provided among inputs —
flagged as an input gap.** → **≥60% band → score 5**

**E2 Promoter holding change**: pre-IPO 99.98% (RHP p.91, "Equity
shareholding of our Promoter and Promoter Group") → post-IPO 71.30% = decrease
of 28.68pp. This is a mechanical IPO effect (Offer-for-Sale by Dr. Manika
Khanna + dilution from the fresh issue), not organic post-listing selling;
20% of post-offer capital is locked in for 3 years and the balance for 1 year
per SEBI ICDR minimum promoter contribution (RHP p.92). By the literal
formula: **decreased >3% → score 0**

**E3 Promoter pledge** = 0% — RHP p.92 ("none of the Equity Shares held by
our Promoters are pledged") and shareholding pattern table col. XIII, RHP
p.95 → **0% band → score 5**

**E4 Contingent Liabilities ÷ Net Worth**: RHP Note 39 (p.266) discloses an
income-tax survey assessment (AY2022-23, Section 133A) plus related orders
totalling a disclosed demand of **Rs 30,89,06,525 (Rs 3,089.07L)**, under
appeal with a stay granted on a 20% deposit (Rs 617.81L in EMIs of Rs 5L);
plus a pending consumer-forum patient claim of ~Rs 52.71L (Rs 50L + Rs 2.20L
+ Rs 0.51L). Total disclosed CL ≈ Rs 3,141.78L (principal only — "interest
thereon" on item (i) is referenced but not separately quantified, so this is
a floor, not a ceiling). Against FY26 Net Worth of Rs 15,230.21L: **CL/NW =
20.63% → 15-30% band → score 1**. Management/legal opinion in the RHP expects
no liability on all items, but the ratio is scored on the gross disclosed
figure per the mechanical rule.

**Block E = 5+0+5+1 = 11/20**

---

## CORE SCORE

| Block | Score | /20 |
|---|---|---|
| A: Return on Capital | 15 | 75% |
| B: Cash Generation Quality | 5 | 25% |
| C: Growth | 15 | 75% |
| D: Balance Sheet Strength | 17 | 85% |
| E: Shareholder Alignment | 11 | 55% |
| **Core Total** | **63** | **63/100** |

**Strongest block: D (Balance Sheet Strength, 17/20)**
**Weakest block: B (Cash Generation Quality, 5/20)**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 0 | EBITDA margin FY23 45.36% → FY26 36.13% (computed: 3,770.39÷10,435.70), decline of 9.23pp despite rev CAGR 33.12% — exceeds the "2-5pp decline" band, so falls to else=0 |
| M2 | Cost Advantage vs peer | 5 | Gaudium EBITDA margin FY24 40.25% vs peer median (Progyny Inc 6.05%, Inspire IVF 26.63%, FY24 basis per RHP peer table p.124) = 16.34% → +23.9pp above → ≥5pp band. Cross-border comparability caveat noted (different business models/jurisdictions) |
| M3 | Capital Efficiency | 5 | FAT = Revenue 10,435.70 ÷ Net Block 746.44 = 13.98x (>3x); RoCE FY26 20.11% (>20%... at boundary, treated as meeting "≥20%" reading since 20.11%>20%) → top band |
| M4 | Customer Stickiness | 0 | Zero revenue-decline years (positive) but receivable days rose 7.5→186.7 days, failing the "stable ±10" leg of the top band; no lower band fits a 0-decline/unstable-receivables profile — scored conservatively 0 |
| M5 | Scale & Dominance | 0 | PEER DATA NEEDED — RHP itself states "there is no Indian listed company in similar business" (p.123); no Indian peer mcap/market-share data available |
| M6 | Technology / R&D | 0 | No R&D/Revenue ratio disclosed; "Intangible assets under development" (GAAT) is capitalised, not expensed/reported as an R&D ratio — N/A, not estimated |
| M7 | Regulatory / License | 1 | IVF/ART is regulated in India (ART Regulation Act 2021, registration with National ART & Surrogacy Registry) but the segment has well over 10 significant players (Indira IVF, Nova IVF, Milann, Oasis, etc. — fragmented market per RHP industry section) → "regulated but >10 players" band |
| M8 | Distribution | 3 | MD&A (RHP p.282): "PAN-India presence... 30+ locations... 7 hubs and 28 spokes" (quantified, growing; IPO proceeds partly earmarked for new IVF centres) and revenue CAGR 33.12% ≥15% → network-growing band. Revenue-per-outlet trend not computable (no prior-year location count disclosed) so top band (5) not reached |
| M9 | Brand | 0 | PEER DATA NEEDED — no comparable Indian gross-margin peer data; foreign peers (Progyny, Inspire IVF) not comparable on gross-margin basis (different business models/cost structures/currencies) |
| M10 | Switching Costs | 0 | Revenue grew every year (positive) but receivable days rose 179.2 days over the period (7.5→186.7), far outside "≤10 days" — same mismatch as M4, scored conservatively 0 |
| M11 | Network Effects | 1 | Only 4 years available (<6yr two-window test not possible) — scored conservatively. Revenue CAGR 33.12%>15%, but Advertisement % of revenue is not clearly declining (FY23 7.45% → FY24 11.90% → FY25 8.27% → FY26 ~9.40% standalone proxy, consolidated FY26 breakout not disclosed in results PDF) → "growth>15% but selling% rising" band |
| M12 | Negative WC / Float | 0 | WC days: FY23 11.3 (0-15 band), FY24 113.8, FY25 135.0, FY26 156.3 — 3 of 4 years >45 days (majority) → >45 band |

**Moat Score = 0+5+5+0+0+0+1+3+0+0+1+0 = 15/60**

**Moats present (score≥3): M2, M3, M8 = 3 moats confirmed**

**Moat classification: 2-3 present → MODERATE**

```
Moat profile:
M1  [          ] 0/5
M2  [XXXXXXXXXX] 5/5  *
M3  [XXXXXXXXXX] 5/5  *
M4  [          ] 0/5
M5  [          ] 0/5  (peer data needed)
M6  [          ] 0/5
M7  [XX        ] 1/5
M8  [XXXXXX    ] 3/5  *
M9  [          ] 0/5  (peer data needed)
M10 [          ] 0/5
M11 [XX        ] 1/5
M12 [          ] 0/5
```

---

## CLASSIFICATION

Grand total (core + moat) = 63 + 15 = **78**

Base classification matrix: Core 63 (60-79 band) + MODERATE moat (not
STRONG/FORTRESS) → **"Core 60-79 + else = GOOD"**

**Deal-breaker check:**
1. Block A<8 → not triggered (A=15)
2. **Block B<8 → TRIGGERED (B=5) → max GOOD**
3. Median RoCE<10% → not triggered (39.06%)
4. Cumulative CFO/PAT<0.50 → not triggered (0.641)
5. Pledge>15% → not triggered (0%)
6. ND/EBITDA>3x AND IC<3x → not triggered (0.379x / 10.22x)
7. Revenue declined majority of years → not triggered (0 decline years)
8. PAT negative in any of last 3 years → not triggered (all positive, growing)
9. History<3 years → not triggered (data_years=4, meets the 3-year minimum)

Base + deal-breaker: **GOOD** (already consistent with the base matrix result;
deal-breaker #2 confirms the cap rather than lowering it further).

**Data confidence check**: 4 fiscal years of consolidated audited/restated
history (FY23-FY26) → **"3-4 = LIMITED, downgrade classification one tier"**
per the classification-matrix data-confidence rule. GOOD → one tier down →
**AVERAGE**.

### FINAL CLASSIFICATION: AVERAGE

`history_downgrade: true` — the depressor is **short post-IPO history (4
fiscal years) plus working-capital/cash-conversion weakness (Block B)**, not
evidence of fundamental business deterioration: revenue and PAT grew in
every scored year, RoCE/RoE remain elevated in absolute terms even after the
FY26 IPO-cash-driven denominator effect, promoter pledge is zero, and
interest coverage is 10.2x.

**Decision line**: Gate 0 mechanical classification = AVERAGE. No STOP verdict
issued at this stage (Gate 0 does not halt runs on company quality). Flags
below propagate to downstream stages; the primary quality signal to carry
forward is working-capital/cash-conversion deterioration (Block B / WC days),
not growth or leverage.

---

## DATA NOTES

1. FY2022 data exists in screener-Data_Sheet.csv (Sales Rs 36.52 Cr, PAT
   Rs 8.83 Cr) but is excluded from the scored 4-year window: it predates the
   RHP's restated financial set (which begins FY2023) and RHP cash-flow
   note (b), p.79, states FY2023 cash flows reflect first-time consolidation
   of an acquired subsidiary (M/s Gaudium Bawa IVF), making FY2022
   non-comparable on a consistent consolidated basis.
2. FY26 RoCE decline (54.40%→20.11%) is substantially a denominator effect:
   per the IPO-proceeds-utilisation table in the FY26 results PDF, Rs 81.31 Cr
   of the Rs 90.00 Cr fresh-issue proceeds remained unutilised as of
   31-Mar-2026, sitting in bank deposits (booked as non-current "Other
   Financial Assets", Rs 8,113.08L) that inflate capital employed without
   yet generating EBIT.
3. D1 (Net Debt/EBITDA) is scored using reported Cash & Cash Equivalents only
   (Rs 878.57L). Including the Rs 8,113.08L of near-cash bank deposits
   referenced in note 2 would flip the company to net-cash positive — noted
   for context, not used in the mechanical score.
4. M4 (Customer Stickiness) and M10 (Switching Costs) both hinge on the same
   underlying tension: zero revenue-decline years (positive) vs. receivable
   days that rose from 7.5 to 186.7 days (very negative). Neither test's
   scoring bands cleanly address this combination; both scored conservatively
   at 0 rather than estimated.
5. M5 (Scale & Dominance) and M9 (Brand) are marked PEER DATA NEEDED. The RHP
   itself states there is no Indian listed peer in this business; the two
   disclosed peers (Progyny Inc — NASDAQ, insurance-network platform;
   Inspire IVF — Thailand SET) are not comparable for Indian market-share
   ranking or like-for-like gross-margin benchmarking.
6. M6 (Technology/R&D): no R&D/Revenue ratio is disclosed anywhere in the
   provided sources. The company capitalises development costs for a
   proprietary protocol ("Gaudium Advanced Analysis and Treatment", GAAT) as
   an intangible asset under development, not as a P&L R&D expense ratio —
   scored 0, not estimated.
7. Contingent liabilities (E4) are sourced from RHP Note 39 (p.266), the
   nearest available disclosure to FY26 close (tax order dated 10-Oct-2025,
   within FY26). No separate FY26 annual-report contingent-liability note was
   included among the provided FY26 results PDFs, so this figure should be
   treated as an approximation, not a FY26-year-end-dated figure.
8. E2's -28.68pp promoter-holding "decline" is a mechanical IPO artifact
   (Offer-for-Sale + fresh-issue dilution), not organic post-listing selling;
   see Block E detail.
9. WC-days ratios throughout use the Revenue basis (Balance ÷ Revenue × 365)
   for Receivable/Inventory/Payable Days — no single "COGS" line is reported
   (cost is split across Cost of Rendering Services, Purchase of Drugs &
   Medical Consumables, and Inventory change), so a COGS basis was not used.
10. No loss-to-profit swings observed — PAT is positive and growing in all
    four scored years (FY23-FY26).
11. FY26 capex = "Purchase of PPE incl. ROU" (Rs 213.58L) + "Development cost
    of intangible asset under development" (Rs 458.33L) = Rs 671.91L, per the
    formula's PPE+intangibles definition (results PDF consolidated CF stmt).

## BLOCK B TREND (feeds FLAG-CASH)

**Deteriorating.** Working capital days rose from **11.3 days (FY23) to
156.3 days (FY26)** — an increase of 145.0 days — driven overwhelmingly by
trade receivables growing from 2.1% of revenue (Rs 90.84L / Rs 4,423.69L,
FY23) to 51.2% of revenue (Rs 5,337.93L / Rs 10,435.70L, FY26), i.e.
receivables grew ~59x while revenue grew only ~2.4x over the same period
(RHP p.255-256, results PDF FY26 audited consolidated BS). Cumulative
CFO/PAT of 64.1% and cumulative FCF/PAT of 14.3% (both well under the 1.00x
threshold) despite consistently positive and growing accounting profit
confirm this is a genuine cash-conversion quality issue, not a one-off.

---

```yaml
stage: B01-gate0
company: "GAUDIUMIVF"
run_date: "2026-07-16"
model: claude-sonnet-5
status: complete
input_gaps: ["rating", "announcements", "shareholding (no post-listing Reg.31 filing provided; RHP pre-listing indicative used)", "research"]
flags:
  - type: FLAG-GATE0
    reason: "Classification downgraded GOOD -> AVERAGE by the data-confidence rule (only 4 fiscal years of consolidated audited/restated history, FY23-FY26; company listed 27-Feb-2026). Depressor is short post-IPO history, not deterioration -- revenue and PAT grew every scored year."
  - type: FLAG-GATE0
    reason: "Block B (Cash Generation Quality) = 5/20 triggers deal-breaker #2 (max GOOD). Working capital days rose 11.3 (FY23) to 156.3 (FY26), receivables grew from 2.1% to 51.2% of revenue; cumulative CFO/PAT=64.1%, cumulative FCF/PAT=14.3%. Feeds block_b_trend / FLAG-CASH downstream."
data_years: 4
fy_range: "FY23 to FY26"
blocks: {A: 15, B: 5, C: 15, D: 17, E: 11}
core_score: 63
moat_score: 15
grand_total: 78
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers: ["#2 Block B score 5 (<8) -> capped at max GOOD", "Data-confidence LIMITED (4 yrs) -> one-tier downgrade GOOD->AVERAGE"]
history_downgrade: true
data_notes:
  - "FY2022 screener data (Sales Rs36.52Cr, PAT Rs8.83Cr) excluded from scored window -- pre-dates RHP restated set and pre-dates subsidiary consolidation (RHP CF note b)."
  - "FY26 RoCE decline (54.40%->20.11%) substantially a denominator effect: ~Rs81Cr of IPO proceeds sitting unutilised in bank deposits (non-current, not cash-equivalents) as of 31-Mar-2026."
  - "D1 Net Debt/EBITDA scored on reported Cash & Equivalents only (Rs878.57L); including Rs8,113.08L near-cash bank deposits would flip company net-cash."
  - "M4/M10 scored 0: zero revenue-decline years (positive) but receivable days rose 7.5->186.7 days -- no scoring band fits this combination cleanly, scored conservatively."
  - "M5/M9 PEER DATA NEEDED -- RHP states no Indian listed peer exists; foreign peers (Progyny Inc, Inspire IVF) not comparable for scale/brand ranking."
  - "M6 N/A -- no R&D/Revenue ratio disclosed anywhere in sources."
  - "E4 contingent liabilities Rs3,141.78L (tax demand Rs3,089.07L under appeal + patient claim ~Rs52.71L) sourced from RHP Note 39 (p.266), nearest available disclosure to FY26 close; not a FY26-year-end-dated figure."
  - "E2 -28.68pp promoter holding change is a mechanical IPO dilution artifact (OFS + fresh issue), not organic post-listing selling."
  - "No loss-to-profit swings -- PAT positive and growing in all 4 scored years."
block_b_trend: "deteriorating -- WC days rose from 11.3 (FY23) to 156.3 (FY26), a 145-day increase, driven by trade receivables growing from 2.1% to 51.2% of revenue while revenue grew only ~2.4x (receivables grew ~59x); cumulative CFO/PAT=64.1%, cumulative FCF/PAT=14.3%."
```
