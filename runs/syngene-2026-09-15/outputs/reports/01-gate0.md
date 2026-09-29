# STAGE 1 — GATE 0 SCORECARD: SYNGENE INTERNATIONAL LTD (SYNGENE)
Run date: 2026-09-15 | Model: claude-sonnet-5 | Stage: B01-gate0
**CORRECTION RUN — full replacement of prior 01-gate0.md / B01-gate0.yaml**

Data available: 9 years (FY2018 to FY2026) for revenue, PAT, cash-flow-summary
and Total-Assets series (screener-data, Data_Sheet.csv rows 10-63). Scoring
adapted to 9-year history for Blocks B and C. Block A (ROCE) runs on a 3-year
computable window (FY2024-FY2026); Block B's FCF and WC-days tests (B2, B3,
B4) and M12 now also run on a 3-year window (FY2024-FY2026), rebuilt this run
from AR2025 consolidated comparatives — see CORRECTIONS LOG item 2.

---

## CORRECTIONS LOG (against independent audit of the prior run)

1. **MAJOR — A1 band misapplied.** Prior run scored A1 = 3 on median ROCE
   13.20%. Rule band: "10-14.9 = 1". 13.20% sits in that band, not in
   "15-19.9 = 3". **Fixed: A1 = 1.** Block A total recomputed 1+1+2+1 = **5**
   (was 7). Flows through: Core 57→56 after all fixes below (see item 2 for
   the offsetting Block B change), Grand total 67→66.
2. **MAJOR — B2/B3/B4/M12 scored on a 2-year window; 3 years of AR
   comparatives were available and unused.** Prior run restricted these
   tests to FY2025-FY2026 only, citing missing Trade Payables and capex
   splits before FY2025. The FY25 Annual Report's consolidated balance sheet
   and cash flow statement (AR2025 p.266-267, p.270, FY2024 comparative
   column) carry exactly these figures for FY2024: Trade payables Rs
   200mn+2,355mn = Rs 2,555mn (255.5cr); Trade receivables Rs 4,416mn
   (441.6cr, ties to screener-data); Inventories Rs 2,385mn (238.5cr, ties to
   screener-data); Purchase of PPE Rs 4,920mn + intangibles Rs 188mn = Rs
   5,108mn capex (510.8cr); Net cash flow from operating activities Rs
   10,421mn (1,042.1cr, ties to screener-data row 57). Rebuilt below on
   FY2024-FY2026. Where a year is still genuinely absent (FY2018-FY2023,
   Trade Payables never disclosed in the Data_Sheet and not in the two ARs
   held), the N/A floor from rule 5 continues to apply — no further
   extension is possible from the provided corpus.
3. **MINOR — WC-days basis not stated.** Fixed: stated explicitly in Block B
   below (Revenue basis throughout; COGS not disclosed as a single line in
   any provided source).
4. **MINOR — deal-breakers #2 and #6 not stated as checked.** Fixed: both
   now stated explicitly in the Deal-breakers section with their inputs and
   non-trigger reasoning.
5. **MINOR — E2 scored 1 on a 2-year proxy window; rule 5 gives 0.** The
   provided shareholding table starts Jun-2024, so the specified 3-year-back
   data point (Jun-2023 promoter holding) is NOT FOUND. Per GROUNDED CLAIMS
   rule 5, a missing data point is marked N/A and scored 0, not substituted
   with a shorter window. **Fixed: E2 = 0** (was 1). Block E total
   recomputed 4+0+0+3 = **7** (was 8).
6. **MINOR — data_notes incomplete / M6 label conflict.** Fixed: added the
   M9 gross-margin-proxy basis note and the M5/M7 PEER DATA NEEDED note to
   data_notes. Resolved the M6 conflict: M6 (Technology/R&D) is a genuine
   data gap — the AR Annexure carries an R&D-expenditure line with no rupee
   figure filled in (AR2026 p.78) — so M6 is now labelled NOT FOUND, scored
   0 per the PEER-DATA/data-gap rule. M8 (Distribution) remains
   archetype-inapplicable (CRO/CDMO has no distribution network), a
   different reason, kept separate.
7. **MINOR — analyst_note conflated two different sites.** Fixed. Unit 3
   Bengaluru (the ex-Stelis Biopharma site) was capitalised into PP&E in
   Q1FY26, Rs 3,438 million (results FY26 audited p.9-10, note 9). Bayview
   (Baltimore, USA, acquired from Emergent Manufacturing Operations
   Baltimore, LLC) remained in Capital Work in Progress at 31 March 2026,
   not capitalised — FY26 added a further Rs 786 million of eligible
   pre-operating cost to its CWIP balance (results FY26 audited p.9, note
   8; AR2026 p.324, note 3(a)(f)). The two sites are not interchangeable;
   only the Bengaluru site drove the FY26 depreciation step-up.
8. **MINOR (numerical) — exceptional items figure was a sub-component, not
   the total.** The prior run's data_notes cited "net Rs 462 million"
   consolidated FY26 exceptional items. Rs 462 million (results FY26
   audited p.9, note 11) is only the labour-code gratuity re-measurement
   component. The filed consolidated P&L line "Exceptional items, net
   gain/(loss)" for FY26 = **Rs (766) million pre-tax** (results FY26
   audited p.4, line 4), which reconciles exactly as Rs 462 million
   (gratuity re-measurement, note 11, consolidated) + Rs 304 million
   (termination benefits, note 12, common to standalone and consolidated) =
   Rs 766 million. The standalone P&L line for FY26 = Rs (732) million
   (results FY26 audited p.3, line 4) = Rs 429 million (note 11, standalone)
   + Rs 304 million (note 12) = Rs 733 million (Rs 1 million rounding). The
   audit's cited "(732)" figure is the STANDALONE line, not the
   consolidated one at p.4; the consolidated total is Rs 766 million. No
   net-of-tax figure is separately disclosed for notes 11/12 (NOT FOUND);
   Block C and data_notes below now cite the correct pre-tax consolidated
   total (Rs 766 million) with its two named components, and flag the
   net-of-tax gap.
9. **CHECK (no change) — Block B FCF figures re-confirmed against the filed
   consolidated cash flow statement.** FY26: Net cash flow from operating
   activities Rs 9,152mn − (Purchase of PPE Rs 3,440mn + Purchase of
   intangible assets Rs 242mn = Rs 3,682mn) = Rs 5,470mn = **Rs 547.0 cr**
   (results FY26 audited p.8, consolidated cash flow statement). FY25: Rs
   11,676mn − (Rs 7,603mn + Rs 98mn = Rs 7,701mn) = Rs 3,975mn = **Rs 397.5
   cr** (same source, FY25 column). 1 crore = 10 million, so these are
   internally consistent with the mn-denominated filed lines; neither figure
   is overstated. **Confirmed, no change.**

Net effect of all fixes on the scorecard: Block A 7→5, Block B 18→20, Block
E 8→7; Blocks C and D unchanged. Core score 57→**56**. Moat score unchanged
at 10 (M12's score is unchanged by the 3-year rebuild — see Block F).
**Grand total 67→66.** Classification unchanged: **AVERAGE** (Core 56 sits
in the 40-59 band regardless of moat tier).

---

## FIRST VERIFICATION PRIORITY — LOAD-BEARING FACTS (checked before own work)

**LBF1 — Q1FY27 print vs claim.** Claim: "revenue Rs 736 cr, down 16% YoY;
operating EBITDA margin 12% with a Rs 50 cr forex hedge loss; PAT before
exceptional Rs 1 cr, reported -Rs 9 cr."
- Revenue: Rs 7,360 million = **Rs 736 cr** (results Q1FY27 p.3, consolidated,
  "3 months ended 30 June 2026" column). Corresponding Q1FY26 = Rs 8,745
  million = Rs 874.5 cr (results Q1FY27 p.3). YoY change = (7,360-8,745)/8,745
  = **-15.8%, rounds to -16%. CONFIRMED.**
- Operating profit (Sales − Expenses, screener convention) Jun-2026 quarter =
  736.0 − 645.2 = **Rs 90.8 cr** (screener-data, quarterly row 28-29-36) →
  margin = 90.8/736.0 = **12.3% ≈ 12%. CONFIRMED.**
- Forex fluctuation loss, net, consolidated, current quarter (Q1FY27) = Rs 501
  million = **Rs 50.1 cr** (results Q1FY27 p.3, line "g) Foreign exchange
  fluctuation loss, net", first data column = current quarter). **CONFIRMED
  (Rs 50 cr).**
- Reported PAT (loss), consolidated, Q1FY27 = -Rs 90 million = **-Rs 9 cr**
  (results Q1FY27 p.3, line 7 "Profit for the period/year"). **CONFIRMED
  exactly.**
- PAT before exceptional items: the filed statement discloses two subtotals —
  "Profit before tax and exceptional items" (consolidated Q1FY27 = -Rs 5.7 cr;
  standalone Q1FY27 = +Rs 3.5 cr) (results Q1FY27 p.2-3, line 3) — and
  "Exceptional items, net loss" (consolidated -Rs 13.5 cr / standalone -Rs
  13.5 cr, both from termination-benefit charges, line 4). There is no single
  filed line labelled "PAT before exceptional." Reconstructing it (PBT before
  exceptional less tax at the FY26 effective rate) gives an estimate in the
  Rs 0-5 cr range on either basis, i.e. **near-breakeven, directionally
  consistent with "Rs 1 cr" but not independently reproducible as an exact
  filed figure.** Flagged as a partial-confirmation, not a clean match
  (results Q1FY27 p.2-3).

**LBF3 — CWIP vs net block, Mar-2026.**
- CWIP, Mar-2026 = **Rs 1,045.7 cr** (screener-data, Data_Sheet row 45,
  2026-03-31 column). Consolidated filed CWIP = Rs 10,404 million = Rs
  1,040.4 cr (results FY26 audited p.6, consolidated BS; ties to AR2026
  p.323, note 3(a), "At 31 March 2026" CWIP column). **CONFIRMED (~Rs 1,046
  cr).**
- Net Block, Mar-2026 = **Rs 3,000.0 cr** (screener-data, Data_Sheet row 44).
  **CONFIRMED.**
- CWIP/Net Block = 1,045.7/3,000.0 = **34.9%.** A third of the fixed-asset
  base is not yet earning. CWIP fell from Rs 1,266.1 cr (FY25) to Rs 1,045.7
  cr (FY26) (screener-data) as the ex-Stelis Unit 3 Bengaluru biologics
  facility (Rs 3,438 million) was capitalised into PP&E during Q1FY26,
  raising depreciation by Rs 247 million for the year (results FY26 audited
  p.9-10, note 9). The Bayview (Baltimore, USA) biologics site remained in
  CWIP at 31-Mar-2026 (note 8) and is not part of this capitalisation — see
  CORRECTIONS LOG item 7. This capacity is not yet matched by proportional
  revenue — the direct driver of the weak ROCE and FAT scores below (Block
  A, M3).

**Block B cash trend — the one number.** Cash from Operating Activity fell
from **Rs 1,167.6 cr in FY25 to Rs 915.2 cr in FY26** (screener-data,
Data_Sheet row 57), a **-21.6% YoY decline**, even as revenue grew +2.6% and
capex fell (Rs 770.1 cr FY25 → Rs 368.2 cr FY26, results FY26 audited p.8,
consolidated CF). **CONFIRMED per Data_Sheet and re-confirmed against the
filed consolidated cash flow statement (CORRECTIONS LOG item 9).** The
multi-year Block B ratios below now score at their maximum precisely because
FY24-25 were strong and FY26 stayed FCF-positive; the direction of travel in
the latest year is still down. `block_b_trend: deteriorating`.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 5/20 (was 7/20)

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (fixed formula,
not the AR's own ROCE definition — see LIMITATIONS). Current-liability splits
exist only for FY2024-FY2026 (from filed/AR balance sheets, consolidated
basis to match Data_Sheet); FY2018-FY2023 ROCE = **NOT FOUND**.

| FY | EBIT = PBT+Interest (cr) | Capital Employed = TA−CL (cr) | ROCE |
|---|---|---|---|
| FY24 | 620.8+47.2=668.0 (screener-data) | 6,151.6−1,144.3=5,007.3 (screener-data Total; AR2025 p. consol BS, Total current liabilities FY24) | **13.34%** |
| FY25 | 659.9+53.1=713.0 (screener-data) | 6,795.9−1,396.4=5,399.5 (results FY26 audited p.6, consol BS FY25 col) | **13.20%** |
| FY26 | 410.9+48.8=459.7 (screener-data) | 7,054.7−1,552.3=5,502.4 (results FY26 audited p.6, consol BS FY26 col) | **8.35%** |

- A1 Median ROCE (n=3): 13.20% → rule band **"10-14.9 = 1"** → **score 1**
  (corrected; prior run misapplied the "15-19.9 = 3" band to this value — see
  CORRECTIONS LOG item 1).
- A2 Minimum single-year ROCE: 8.35% (FY26) → 8-11.9% band → **score 1**
- A3 Median ROE (n=9, full history, ROE needs no CL split):
  computed PAT ÷ average Net Worth per year (screener-data rows 24, 39-40):
  FY18 17.75% (closing NW only, opening NFY17 unavailable, stated) · FY19
  17.98% · FY20 19.89% · FY21 16.21% · FY22 12.94% · FY23 13.43% · FY24
  12.95% · FY25 11.04% · FY26 6.62%. Median = **13.43%** → 12-14.9% band →
  **score 2**
- A4 ROCE trend, latest (FY26=8.35%) vs earliest computable (FY24=13.34%):
  decline of **4.99pp** → 3-5pp band (borderline) → **score 1**

Block A total: 1+1+2+1 = **5/20**.

**Deal-breaker 1 triggered: Block A = 5 (<8) → caps classification at max
GOOD.** Non-binding here since the Core score lands in AVERAGE anyway (see
CLASSIFICATION).

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 20/20 (was 18/20)

**Basis note (CORRECTIONS LOG item 3):** all Working Capital Days figures in
this scorecard (B4, M12, and the receivable/inventory/payable-day components
feeding M4/M10) use the **Revenue basis** throughout — Receivable Days =
Trade Receivables ÷ Revenue × 365; Inventory Days = Inventory ÷ Revenue ×
365; Payable Days = Trade Payables ÷ Revenue × 365. No provided source (
Data_Sheet, filed results, or either AR) presents a single explicit "Cost of
Goods Sold" line — the P&L splits raw material cost, power & fuel, and other
manufacturing expenses separately — so the fixed-formula default (Revenue
basis, used "only if COGS is explicitly available" otherwise) applies.

**Window note (CORRECTIONS LOG item 2):** B2, B3, B4 and M12 are rebuilt this
run on **FY2024-FY2026** (3 years), using AR2025's FY2024 comparative
consolidated balance sheet and cash flow statement for the newly-added year.
FY2018-FY2023 remain NOT FOUND for Trade Payables (no source in the
corpus discloses them) and are not included.

| FY | Capex = PPE + intangibles purchased (cr) | CFO (cr) | FCF (cr) | Receivable days | Inventory days | Payable days | WC days |
|---|---|---|---|---|---|---|---|
| FY24 | 492.0+18.8=510.8 (AR2025 p.270, consol CF, FY24 col) | 1,042.1 (screener-data row 57; ties to AR2025 p.270, "10,421") | **531.3** | 441.6/3,488.6×365=46.19 (screener-data rows 49,11) | 238.5/3,488.6×365=24.95 (screener-data rows 50,11) | 255.5/3,488.6×365=26.73 (AR2025 p.267, consol BS, FY24 col Trade payables 200+2,355=2,555mn) | **44.41** |
| FY25 | 760.3+9.8=770.1 (results FY26 audited p.8, consol CF FY25 col) | 1,167.6 (screener-data row 57) | **397.5** | 526.7/3,642.4×365=52.78 | 155.5/3,642.4×365=15.58 | 352.0/3,642.4×365=35.28 (results FY26 audited p.6, consol BS FY25 col, Trade payables 3,520mn) | **33.08** |
| FY26 | 344.0+24.2=368.2 (results FY26 audited p.8, consol CF FY26 col) | 915.2 (screener-data row 57) | **547.0** | 508.8/3,738.7×365=49.68 | 141.3/3,738.7×365=13.79 | 347.5/3,738.7×365=33.92 (results FY26 audited p.6, consol BS FY26 col, Trade payables 3,475mn) | **29.56** |

- B1 Cumulative CFO ÷ Cumulative PAT (FY18-26, n=9, full history, no gap for
  this pair): 6,983.9 ÷ 3,637.1 = **1.92** (screener-data rows 24, 57) →
  ≥1.00 → **score 5**
- B2 FCF-positive years / total (FY24-26, n=3): FY24 +531.3cr, FY25 +397.5cr,
  FY26 +547.0cr — **3 of 3 positive (100%)** → **score 5** (corrected window;
  was scored on 2 of 2 years)
- B3 Cumulative FCF ÷ Cumulative PAT (FY24-26): (531.3+397.5+547.0) ÷
  (510.0+496.2+316.7) = 1,475.8 ÷ 1,322.9 = **1.12** → ≥0.60 → **score 5**
  (corrected window; was 2-year, now 3-year, same score but on stronger
  evidence)
- B4 Change in WC Days, latest (FY26) vs earliest (FY24): 44.41 → 29.56 =
  **decreased 14.85 days** → ">5 days decrease" band → **score 5** (corrected
  from 3; the 2-year-only window in the prior run understated the
  improvement, which is materially larger over the full available 3-year
  span)

Block B total: 5+5+5+5 = **20/20**.

Block B score reflects genuinely improving multi-year cash-conversion ratios;
see Block B cash trend note above (CFO -21.6% YoY in the latest year) for
why the direction of travel still needs watching despite the perfect score.

---

## BLOCK C: GROWTH (Max 20) — Score: 8/20

- C1 Revenue CAGR FY18→FY26 (8yr): (3,738.7/1,423.1)^(1/8)−1 = **12.83%**
  (screener-data row 11) → 10-14.9% band → **score 3**
- C2 PAT CAGR FY18→FY26 (8yr): (316.7/305.4)^(1/8)−1 = **0.46%**
  (screener-data row 24) → <5% band → **score 0**
- C3 Positive YoY revenue years: 8 of 8 comparisons FY19-FY26 all positive
  (screener-data row 11) = 100% → **score 5**
- C4 PAT CAGR − Revenue CAGR = 0.46% − 12.83% = **-12.37pp** → <-8pp band →
  **score 0**

Depressor named: FY26 PAT fell -36.2% YoY (Rs 496.2cr → Rs 316.7cr,
screener-data row 24), driven by (i) the FY26 consolidated exceptional items
line, a net pre-tax loss of **Rs 766 million** (results FY26 audited p.4,
line 4) — comprising Rs 462 million labour-code gratuity re-measurement
(note 11, consolidated) and Rs 304 million termination benefits (note 12) —
and (ii) higher depreciation from the newly capitalised Unit 3 Bengaluru
biologics capacity (LBF3 above, Rs 247 million incremental depreciation,
note 9). This is the single item cluster dragging both C2 and C4 to zero
over an otherwise-growing revenue base. (Corrected from the prior run's
"Rs 462 million" total — see CORRECTIONS LOG item 8; the correct total is
Rs 766 million, of which Rs 462 million is the gratuity sub-component.)

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 16/20

Latest = FY26, consolidated (matches Data_Sheet basis).
- D1 Net Debt ÷ EBITDA: Borrowings Rs 458.4cr (screener-data row 41; reconciles
  to consol lease liabilities 449.0cr + current borrowings 9.4cr, results FY26
  audited p.6) − Cash & Bank Rs 833.0cr (screener-data row 51) = **net cash of
  Rs 374.6cr** → **score 5**
- D2 Interest Coverage EBIT÷Interest: 459.7 ÷ 48.8 = **9.42x** (screener-data
  rows 21-22) → 5-9.9x band → **score 4**
- D3 Debt ÷ Equity: 458.4 ÷ (402.9+4,436.2=4,839.1) = **0.095** (screener-data
  rows 39-41) → <0.1 → **score 5**
- D4 Current Ratio: Total current assets 21,428mn ÷ Total current liabilities
  15,523mn (results FY26 audited p.6, consolidated BS) = **1.38** → 1.2-1.49
  band → **score 2**

Block D total: 5+4+5+2 = **16/20** (unchanged).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 7/20 (was 8/20)

- E1 Promoter holding, latest quarter (Jun-2026) = **52.59%** (shareholding
  table, SECONDARY tier, screener aggregator) → 50-59.9% → **score 4**
- E2 Promoter holding change over 3 years: the specified data point (promoter
  holding as of Jun-2023) is **NOT FOUND** — the provided shareholding table
  starts Jun-2024. Per GROUNDED CLAIMS rule 5, a missing required data point
  is marked N/A and scored 0, not substituted with a shorter window →
  **score 0** (corrected; was 1 on a 2-year proxy). Context only, not scored:
  Jun-2024 (54.72%) to Jun-2026 (52.59%) = -2.13pp over the 2 years that are
  available.
- E3 Promoter pledge, latest: **N/A (not in provided data)** — neither the
  shareholding table nor the AR text (searched for "pledge"/"encumbrance")
  discloses a promoter-pledge percentage → **score 0**
- E4 Contingent Liabilities ÷ Net Worth: Contingent liabilities (claims not
  acknowledged as debt + bank guarantees) = Rs 5,308mn+4mn = Rs 531.2cr
  (AR2026 p.276-277, Note 31, standalone); Net Worth standalone FY26 = Rs
  4,703.8cr (results FY26 audited p.5, standalone BS) → 531.2/4,703.8 =
  **11.29%** → 5-15% band → **score 3**

Block E total: 4+0+0+3 = **7/20**.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 10/60 (unchanged)

Peers: ANTHEM (Anthem Biosciences), SAILIFE (Sai Life Sciences), PPLPHARMA
(Piramal Pharma), all screener-data Data_Sheet.csv, FY26 column.

| Test | Finding | Score |
|---|---|---|
| M1 Pricing Power | EBITDA margin (=PBT−OtherIncome+Dep+Interest, ÷Revenue) FY18 33.29% → FY26 24.64% (screener-data): **declined 8.65pp** despite revenue CAGR 12.83% (≥10%) → decline exceeds the 2-5pp "1" band | **0** |
| M2 Cost Advantage vs peer median | Syngene FY26 EBITDA margin 24.64% vs peer median 28.91% (ANTHEM 39.26%, SAILIFE 28.91%, PPLPHARMA 10.39%, all screener-data) → **4.27pp below** median | **0** |
| M3 Capital Efficiency | FAT = Revenue/Net Block = 3,738.7/3,000.0 = **1.25x**; ROCE (computed above) FY26 = **8.35%** → fails all positive tiers (needs ROCE>12% at FAT>1x) | **0** |
| M4 Customer Stickiness | Zero revenue-decline years (screener-data); receivable days FY18 68.43 → FY26 49.68 = **-18.75 days**, outside the ±10 "stable" band (though improving, not deteriorating) → falls to the "max 1 decline year, recovered" tier | **3** |
| M5 Scale & Dominance | Mcap: ANTHEM Rs 53,005cr > SAILIFE Rs 33,664cr > PPLPHARMA Rs 28,138cr > **SYNGENE Rs 15,446cr** (screener-data META rows) — smallest of the 4 named names. Full listed-CDMO-universe ranking beyond these 3 peers **PEER DATA NEEDED** | **0** |
| M6 Technology / R&D | AR Annexure discloses "expenditure incurred on Research and Development" as a line item with **no rupee figure filled in** (AR2026 p.78). This is a genuine data gap, not an archetype exclusion — a CRO/CDMO's technology capability is central to its model, but own-account R&D spend (vs client-funded contract research revenue) is simply not quantified in the provided sources → **NOT FOUND**, corrected label from the prior run's "archetype-inapplicable" (see CORRECTIONS LOG item 6) | **0** |
| M7 Regulatory / License | Count of listed players in the CRDMO/CDMO segment not evidenced in any provided source beyond the 3 supplied peers → **PEER DATA NEEDED** | **0** |
| M8 Distribution | Not a distribution-network archetype (B2B contract research/manufacturing) — archetype-inapplicable, distinct from M6's data-gap reasoning | **0** |
| M9 Brand (GM proxy) | GM=(Revenue−RawMaterial±ΔInventory)/Revenue: Syngene 75.82%, peer median 71.06% (ANTHEM 71.06%, SAILIFE 73.30%, PPLPHARMA 59.24%, all screener-data) → **+4.76pp above median**, just under the 5pp/8%-growth "3" tier; revenue CAGR 12.83% clears growth condition | **1** |
| M10 Switching Costs | Revenue grew every year (100%, C3); receivable days moved -18.75 days (a decrease, which satisfies "≤10 day increase") | **5** |
| M11 Network Effects (9yr history, test valid) | Latest 3yr revenue CAGR FY23→FY26 = **5.40%**; prior 3yr CAGR FY20→FY23 = **16.65%** (screener-data row 11) — decelerating, not accelerating | **0** |
| M12 Negative WC / Float | WC Days now computable FY24 (44.41), FY25 (33.08), FY26 (29.56) — all three years fall in the 15-45 day band, none negative and none in 0-15 → **score unchanged at 1** despite the wider window (CORRECTIONS LOG item 2; the 2-year sample happened to land in the same band as the corrected 3-year sample) | **1** |

**Moats present (score ≥3): M4, M10 = 2 of 12 → Moat classification:
MODERATE** (2-3 present band). Unchanged by the corrections.

---

## LIMITATIONS / INPUT GAPS

1. Data_Sheet.csv has no Current Liabilities split for FY2018-FY2023 → ROCE
   NOT FOUND for those years; Block A A1/A2/A4 use a 3-year window
   (FY2024-FY2026) built from filed/AR consolidated balance sheets.
2. Data_Sheet.csv has no Trade Payables row for any year → Working Capital
   Days (B4, M12) are now computable for FY2024-FY2026 (corrected this run
   using AR2025's FY2024 comparative consolidated balance sheet, in addition
   to the FY2025-FY2026 filed results balance sheets already used).
   FY2018-FY2023 remain NOT FOUND — no source in the held corpus discloses
   Trade Payables further back.
3. Data_Sheet.csv's "Cash from Investing Activity" aggregates capex with
   large treasury deposit/mutual-fund flows and cannot be used as a capex
   proxy → FCF (B2, B3) is now computable for FY2024-FY2026 (corrected this
   run using AR2025's FY2024 comparative consolidated cash flow statement, in
   addition to FY2025-FY2026 from the filed cash flow statement's explicit
   "Purchase of property, plant and equipment" / "Purchase of intangible
   assets" lines). FY2018-FY2023 remain NOT FOUND.
4. Promoter pledge % not found in any provided source (E3 = N/A, scored 0).
5. Promoter shareholding table (SECONDARY tier) starts Jun-2024, so the
   Jun-2023 data point required for a true 3-year E2 change is NOT FOUND. Per
   rule 5, E2 is scored 0 (N/A), not computed on the available 2-year window
   (corrected this run — see CORRECTIONS LOG item 5). The 2-year change
   (-2.13pp, Jun-2024 to Jun-2026) is shown as context only in Block E.
6. AR Note 38 "Financial ratios" (standalone) discloses the company's OWN
   ROE/ROCE definitions (ROCE denominator = Tangible Net Worth + Borrowings −
   Deferred Tax Asset, not Total Assets − Current Liabilities) for
   FY2024-FY2026: ROCE 14% (FY24), 13.24% (FY25), 10.78% (FY26); ROE 12%
   (FY24), 10% (FY25), 8% (FY26) (AR2025 p.252, AR2026 p.286-287). These are
   cited here as a cross-check only — not used for scoring, per the fixed
   formula rule — and are on a STANDALONE basis vs the CONSOLIDATED basis used
   for Data_Sheet-driven scores elsewhere in this scorecard.
7. Sector-wide listed-peer universe for M5/M7 is not evidenced beyond the 3
   supplied peers (ANTHEM, SAILIFE, PPLPHARMA) — PEER DATA NEEDED for a
   definitive ranking/player-count.
8. Net-of-tax figure for the FY26 exceptional items (notes 11 and 12) is not
   separately disclosed anywhere in the provided results — only the pre-tax
   amounts (Rs 766mn consolidated / Rs 733mn standalone) and, for a different
   exceptional item (note 10, the FX-driven receivables write-off), an
   explicit after-tax figure (Rs 202mn) are given. NOT FOUND for notes 11/12.

---

## CLASSIFICATION

Core score = A(5) + B(20) + C(8) + D(16) + E(7) = **56/100** (was 57/100)
Moat score = **10/60** (unchanged)
Grand total = **66/160** (was 67/160)
Moat classification: **MODERATE** (2 of 12 tests present: M4, M10)

Data confidence: 9 years overall = moderate tier (7-9 band); no automatic
downgrade. Block A, and now Block B's B2/B3/B4/M12, run on a 3-year
computable window — flagged above, not treated as an overall-history
downgrade.

Classification matrix: Core 40-59 → **AVERAGE** (moat tier does not change
this band). Unchanged by the corrections — the Block A/Block B/Block E
offsetting moves keep Core inside the same band.

**Deal-breakers checked** (all nine, per rule):
- #1 Block A = 5 (<8) → **triggered**, caps at max GOOD (non-binding,
  AVERAGE is already below GOOD).
- #2 Block B = 20 (not <8) → **checked, not triggered.**
- #3 median ROCE 13.20% (not <10%) → **checked, not triggered.**
- #4 cumulative CFO/PAT 1.92 (not <0.50) → **checked, not triggered.**
- #5 pledge N/A, no evidence of >15% → **checked, not triggered** (absence of
  data is not treated as a trigger).
- #6 ND/EBITDA is net cash (not >3x; the >3x AND IC<3x conjunction requires
  both legs, and neither leg is met — IC is 9.42x, also not <3x) →
  **checked, not triggered.**
- #7 revenue did not decline in any year → **checked, not triggered.**
- #8 PAT positive in all of the last 3 years, FY24 Rs 510.0cr / FY25 Rs
  496.2cr / FY26 Rs 316.7cr (screener-data) → **checked, not triggered.**
- #9 history is 9 years (not <3) → **checked, not triggered.**

**Strongest block: B (Cash Generation, 20/20)** — corrected to a perfect
score on the wider 3-year window, but still flagged as trailing-window-
driven; latest-year direction is down (CFO -21.6% YoY).
**Weakest block: A (Return on Capital, 5/20)**, closely followed by Moat
(10/60) — both driven by the same FY26 capacity-expansion/one-off cost drag.

## DECISION LINE

**AVERAGE.** Core score of 56/100 sits mid-band on its own; the moat profile
is thin (MODERATE, 2/12) rather than a mitigating strength. The FY26
deterioration (ROCE 13.34%→8.35% over FY24-26, PAT -36% YoY, CFO -21.6% YoY)
is traceable to named, dated items — a Rs 766 million consolidated pre-tax
exceptional charge (gratuity re-measurement plus termination benefits), a
large newly capitalised biologics facility at Unit 3 Bengaluru (CWIP 34.9% of
net block, with Bayview USA still uncapitalised in CWIP), and a Q1FY27 Rs 50
cr forex hedge loss — not to a broad-based operating breakdown. This is a
flag for the operator to weigh at Halt 1, not a mechanical failure; no
deal-breaker forces a lower tier than AVERAGE.

```yaml
stage: B01-gate0
company: "SYNGENE"
run_date: "2026-09-15"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Data_Sheet.csv has no Current Liabilities split FY2018-FY2023: ROCE NOT FOUND those years; Block A A1/A2/A4 use computed FY2024-FY2026 window only"
  - "Data_Sheet.csv has no Trade Payables row any year: WC Days (B4, M12) computed for FY2024-FY2026 using AR2025 FY2024 comparative plus FY2025-FY2026 filed results BS; FY2018-FY2023 still NOT FOUND"
  - "Data_Sheet.csv 'Cash from Investing Activity' mixes capex with treasury deposit/MF flows: FCF (B2, B3) computed for FY2024-FY2026 using AR2025 FY2024 comparative plus FY2025-FY2026 filed CF statement; FY2018-FY2023 still NOT FOUND"
  - "Promoter pledge % not found in shareholding table or AR text: E3 scored 0 as N/A"
  - "Promoter shareholding table (SECONDARY tier) starts Jun-2024: Jun-2023 data point NOT FOUND, so E2 scored 0 (N/A) per rule 5 rather than a 2-year proxy"
  - "Sector-wide listed-peer universe beyond ANTHEM/SAILIFE/PPLPHARMA not evidenced: M5, M7 flagged PEER DATA NEEDED"
  - "Net-of-tax figure for FY26 exceptional items (notes 11, 12) not separately disclosed: NOT FOUND"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE with named historical depressors: FY26 ROCE fell 13.34% (FY24) to 8.35% (FY26, computed) and PAT fell -36% YoY (Rs 496.2cr to Rs 316.7cr, screener-data), driven by a Rs 766 million consolidated pre-tax exceptional items charge (Rs 462mn labour-code gratuity re-measurement, note 11, plus Rs 304mn termination benefits, note 12; results FY26 audited p.4 and p.9-10) and depreciation step-up from the newly capitalised ex-Stelis Unit 3 Bengaluru biologics facility (CWIP 34.9% of net block at Mar-2026, LBF3; Bayview USA remains uncapitalised in CWIP separately); Q1FY27 carried a further Rs 50 cr forex hedge loss (results Q1FY27 p.3). Distinguish capacity-expansion drag from a structural moat failure before any position-size decision."
data_years: 9
fy_range: "FY2018 to FY2026"
blocks: {A: 5, B: 20, C: 8, D: 16, E: 7}
core_score: 56
moat_score: 10
grand_total: 66
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "1: Block A = 5 (<8) -> caps max GOOD (non-binding; Core score already AVERAGE)"
history_downgrade: false
data_notes:
  - "AR Note 38 (standalone) discloses its own ROE/ROCE definitions differing from the fixed formula (ROCE denominator = Tangible Net Worth + Borrowings - DTA): ROCE 14%/13.24%/10.78% and ROE 12%/10%/8% for FY24/FY25/FY26 (AR2025 p.252, AR2026 p.286-287); cited as cross-check only, not scored, and on a standalone basis vs consolidated Data_Sheet basis used elsewhere"
  - "PAT-before-exceptional figure in LBF1 claim (Rs 1 cr) could not be exactly reproduced from the two disclosed filed subtotals (PBT before exceptional and exceptional items, net); directionally consistent (near-breakeven) but not an exact filed line item (results Q1FY27 p.2-3)"
  - "M6 (R&D) scored 0 as NOT FOUND: AR Annexure R&D-expenditure line has no rupee figure filled in (AR2026 p.78); this is a data gap, not an archetype exclusion. M8 (Distribution) scored 0 as archetype-inapplicable (CRO/CDMO business model has no distribution network) - a distinct reason, corrected from a prior-run label conflict"
  - "M9 gross-margin test used a proxy: GM = (Revenue - Raw Material Cost +/- Change in Inventory) / Revenue, since no explicit COGS or gross-margin line is disclosed; peer figures (ANTHEM 71.06%, SAILIFE 73.30%, PPLPHARMA 59.24%) computed on the same proxy basis from screener-data FY26 column"
  - "M5 (Scale & Dominance) and M7 (Regulatory/License) both flagged PEER DATA NEEDED: full listed-CDMO/CRO universe ranking and regulated-player count not evidenced beyond the 3 supplied peers (ANTHEM, SAILIFE, PPLPHARMA)"
  - "FY26 consolidated exceptional items, net loss, pre-tax = Rs 766 million (results FY26 audited p.4, line 4) = Rs 462 million labour-code gratuity re-measurement (note 11, consolidated) + Rs 304 million termination benefits (note 12); standalone equivalent = Rs 732-733 million (p.3, line 4) = Rs 429 million (note 11, standalone) + Rs 304 million (note 12). Net-of-tax figure for these two items is NOT FOUND in the provided results"
block_b_trend: "deteriorating - CFO fell to Rs 915.2 cr in FY26 from Rs 1,167.6 cr in FY25 (screener-data), -21.6% YoY, despite +2.6% revenue growth and lower capex; re-confirmed against the filed FY26 audited consolidated cash flow statement (p.8): CFO Rs 9,152mn less capex Rs 3,682mn = Rs 5,470mn (Rs 547.0cr) FY26, and Rs 11,676mn less Rs 7,701mn = Rs 3,975mn (Rs 397.5cr) FY25 - both figures confirmed unchanged"
analyst_note: "FY26 weakness is concentrated and datable, not diffuse: a Rs 766mn consolidated pre-tax exceptional charge (gratuity re-measurement plus termination benefits) and depreciation from the newly capitalised ex-Stelis Unit 3 Bengaluru biologics facility (CWIP fell Rs1,266cr to Rs1,046cr as it moved to PP&E) explain most of the ROCE and PAT decline; the separate Bayview, USA site remained uncapitalised in CWIP through FY26. Block B's ratios now score a perfect 20/20 on the corrected 3-year (FY24-26) window, but CFO itself still fell 21.6% YoY in FY26 - the trailing multi-year average is doing the scoring work, not the current trajectory. Moat score of 10/60 is driven down by peer-relative margin tests (M1, M2) failing against ANTHEM and SAILIFE's higher and more stable EBITDA margins, while stickiness tests (M4, M10) pass because receivable days improved, not because pricing power exists. Treat the Block A/moat weakness as evidence to verify at Halt 1 (is FY26 capacity a one-off drag or a durable margin reset), not as a standalone AVOID signal."
```
