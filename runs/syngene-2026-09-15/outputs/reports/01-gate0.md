# STAGE 1 — GATE 0 SCORECARD: SYNGENE INTERNATIONAL LTD (SYNGENE)
Run date: 2026-09-15 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 9 years (FY2018 to FY2026) for revenue, PAT, cash-flow-summary
and Total-Assets series (screener-data, Data_Sheet.csv rows 10-63). Scoring
adapted to 9-year history for Blocks B and C. Block A (ROCE) and parts of
Block B (Working Capital Days, FCF) are restricted to a 3-year or 2-year
computable window because the Data_Sheet does not split Current Liabilities
or Trade Payables for FY2018-FY2023 (see LIMITATIONS below); those windows
are stated explicitly against each metric.

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
  1,040.4 cr (results FY26 audited p.6, consolidated BS) — same order,
  small gap likely a consolidation/Trust adjustment. **CONFIRMED (~Rs 1,046
  cr).**
- Net Block, Mar-2026 = **Rs 3,000.0 cr** (screener-data, Data_Sheet row 44).
  **CONFIRMED.**
- CWIP/Net Block = 1,045.7/3,000.0 = **34.9%.** A third of the fixed-asset
  base is not yet earning. CWIP fell from Rs 1,266.1 cr (FY25) to Rs 1,045.7
  cr (FY26) (screener-data) as the Stelis-acquired biologics licence (Rs
  3,438 million) was capitalised into PP&E during Q1FY26, raising
  depreciation by Rs 247 million for the year (results FY26 audited p.10,
  note 9). This capacity is not yet matched by proportional revenue —
  the direct driver of the weak ROCE and FAT scores below (Block A, M3).

**Block B cash trend — the one number.** Cash from Operating Activity fell
from **Rs 1,167.6 cr in FY25 to Rs 915.2 cr in FY26** (screener-data,
Data_Sheet row 57), a **-21.6% YoY decline**, even as revenue grew +2.6% and
capex fell (Rs 770.1 cr FY25 → Rs 368.2 cr FY26, results FY26 audited p.8,
consolidated CF). **CONFIRMED per Data_Sheet.** The multi-year Block B ratios
below score well only because FY24-25 were strong; the direction of travel in
the latest year is down. `block_b_trend: deteriorating`.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 7/20

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (fixed formula,
not the AR's own ROCE definition — see LIMITATIONS). Current-liability splits
exist only for FY2024-FY2026 (from filed/AR balance sheets, consolidated
basis to match Data_Sheet); FY2018-FY2023 ROCE = **NOT FOUND**.

| FY | EBIT = PBT+Interest (cr) | Capital Employed = TA−CL (cr) | ROCE |
|---|---|---|---|
| FY24 | 620.8+47.2=668.0 (screener-data) | 6,151.6−1,144.3=5,007.3 (screener-data Total; AR2025 p. consol BS, Total current liabilities FY24) | **13.34%** |
| FY25 | 659.9+53.1=713.0 (screener-data) | 6,795.9−1,396.4=5,399.5 (results FY26 audited p.6, consol BS FY25 col) | **13.20%** |
| FY26 | 410.9+48.8=459.7 (screener-data) | 7,054.7−1,552.3=5,502.4 (results FY26 audited p.6, consol BS FY26 col) | **8.35%** |

- A1 Median ROCE (n=3): 13.20% → 10-14.9% band → **score 3**
- A2 Minimum single-year ROCE: 8.35% (FY26) → 8-11.9% band → **score 1**
- A3 Median ROE (n=9, full history, ROE needs no CL split):
  computed PAT ÷ average Net Worth per year (screener-data rows 24, 39-40):
  FY18 17.75% (closing NW only, opening NFY17 unavailable, stated) · FY19
  17.98% · FY20 19.89% · FY21 16.21% · FY22 12.94% · FY23 13.43% · FY24
  12.95% · FY25 11.04% · FY26 6.62%. Median = **13.43%** → 12-14.9% band →
  **score 2**
- A4 ROCE trend, latest (FY26=8.35%) vs earliest computable (FY24=13.34%):
  decline of **4.99pp** → 3-5pp band (borderline) → **score 1**

**Deal-breaker 1 triggered: Block A = 7 (<8) → caps classification at max
GOOD.** Non-binding here since the Core score lands in AVERAGE anyway (see
CLASSIFICATION).

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 18/20

| Test | Value | Anchor | Score |
|---|---|---|---|
| B1 Cumulative CFO ÷ Cumulative PAT (FY18-26, n=9) | 6,983.9 ÷ 3,637.1 = **1.92** | screener-data rows 24, 57 | ≥1.00 → **5** |
| B2 FCF-positive years / total | FY25 +397.5cr, FY26 +547.0cr — **2 of 2 computable years positive (100%)** | FCF=CFO−Capex; Capex = purchase of PPE+intangibles, results FY26 audited p.8 consol CF (FY26: 3,440+242=3,682mn; FY25: 7,603+98=7,701mn); CFO from screener-data row 57 | **5** (flagged: only 2 of 9 years computable — Data_Sheet's aggregate "Cash from Investing Activity" mixes capex with large treasury deposit/MF flows and cannot be used as a capex proxy for FY18-24; those years = NOT FOUND) |
| B3 Cumulative FCF ÷ Cumulative PAT | (397.5+547.0) ÷ (496.2+316.7) = 944.5 ÷ 812.9 = **1.16** | as above, n=2 years only | ≥0.60 → **5** (same 2-year caveat) |
| B4 Change in WC Days, latest vs earliest computable | FY25 33.08 days → FY26 29.56 days = **decreased 3.52 days** | Receivable/Inventory: screener-data rows 49-50; Payables: FY26 consol 3,475mn / FY25 consol 3,520mn from results FY26 audited p.6 (Data_Sheet has no Trade Payables row, any year) | ±5 days band → **3** (flagged: only FY25→FY26 computable, not FY18→FY26, because payables data does not exist further back) |

Block B score is inflated relative to the current trajectory: see Block B
cash trend note above (CFO -21.6% YoY in the latest year).

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
screener-data row 24), driven by exceptional items (labour-code gratuity
re-measurement, termination benefits — results FY26 audited p.9-10, note 11-12,
net Rs 462 million consolidated exceptional charge for FY26) and higher
depreciation from newly capitalised biologics capacity (LBF3 above). This is
the single item dragging both C2 and C4 to zero over an otherwise-growing
revenue base.

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

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 8/20

- E1 Promoter holding, latest quarter (Jun-2026) = **52.59%** (shareholding
  table, SECONDARY tier, screener aggregator) → 50-59.9% → **score 4**
- E2 Promoter holding change: available window is Jun-2024 (54.72%) to
  Jun-2026 (52.59%) = **-2.13pp over 2 years** (shareholding table; full
  3-year window NOT FOUND — the provided table starts Jun-2024) → decreased
  1-3% band → **score 1**
- E3 Promoter pledge, latest: **N/A (not in provided data)** — neither the
  shareholding table nor the AR text (searched for "pledge"/"encumbrance")
  discloses a promoter-pledge percentage → **score 0**
- E4 Contingent Liabilities ÷ Net Worth: Contingent liabilities (claims not
  acknowledged as debt + bank guarantees) = Rs 5,308mn+4mn = Rs 531.2cr
  (AR2026 p.276-277, Note 31, standalone); Net Worth standalone FY26 = Rs
  4,703.8cr (results FY26 audited p.5, standalone BS) → 531.2/4,703.8 =
  **11.29%** → 5-15% band → **score 3**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 10/60

Peers: ANTHEM (Anthem Biosciences), SAILIFE (Sai Life Sciences), PPLPHARMA
(Piramal Pharma), all screener-data Data_Sheet.csv, FY26 column.

| Test | Finding | Score |
|---|---|---|
| M1 Pricing Power | EBITDA margin (=PBT−OtherIncome+Dep+Interest, ÷Revenue) FY18 33.29% → FY26 24.64% (screener-data): **declined 8.65pp** despite revenue CAGR 12.83% (≥10%) → decline exceeds the 2-5pp "1" band | **0** |
| M2 Cost Advantage vs peer median | Syngene FY26 EBITDA margin 24.64% vs peer median 28.91% (ANTHEM 39.26%, SAILIFE 28.91%, PPLPHARMA 10.39%, all screener-data) → **4.27pp below** median | **0** |
| M3 Capital Efficiency | FAT = Revenue/Net Block = 3,738.7/3,000.0 = **1.25x**; ROCE (computed above) FY26 = **8.35%** → fails all positive tiers (needs ROCE>12% at FAT>1x) | **0** |
| M4 Customer Stickiness | Zero revenue-decline years (screener-data); receivable days FY18 68.43 → FY26 49.68 = **-18.75 days**, outside the ±10 "stable" band (though improving, not deteriorating) → falls to the "max 1 decline year, recovered" tier | **3** |
| M5 Scale & Dominance | Mcap: ANTHEM Rs 53,005cr > SAILIFE Rs 33,664cr > PPLPHARMA Rs 28,138cr > **SYNGENE Rs 15,446cr** (screener-data META rows) — smallest of the 4 named names. Full listed-CDMO-universe ranking beyond these 3 peers **PEER DATA NEEDED** | **0** |
| M6 Technology / R&D | AR Annexure discloses "expenditure incurred on Research and Development" as a line item with **no rupee figure filled in** (AR2026 p.78) — consistent with a contract-research business model where R&D is client-funded revenue, not own-account spend. N/A (not in provided data) | **0** |
| M7 Regulatory / License | Count of listed players in the CRDMO/CDMO segment not evidenced in any provided source beyond the 3 supplied peers → **PEER DATA NEEDED** | **0** |
| M8 Distribution | Not a distribution-network archetype (B2B contract research/manufacturing) — N/A | **0** |
| M9 Brand (GM proxy) | GM=(Revenue−RawMaterial±ΔInventory)/Revenue: Syngene 75.82%, peer median 71.06% (ANTHEM 71.06%, SAILIFE 73.30%, PPLPHARMA 59.24%, all screener-data) → **+4.76pp above median**, just under the 5pp/8%-growth "3" tier; revenue CAGR 12.83% clears growth condition | **1** |
| M10 Switching Costs | Revenue grew every year (100%, C3); receivable days moved -18.75 days (a decrease, which satisfies "≤10 day increase") | **5** |
| M11 Network Effects (9yr history, test valid) | Latest 3yr revenue CAGR FY23→FY26 = **5.40%**; prior 3yr CAGR FY20→FY23 = **16.65%** (screener-data row 11) — decelerating, not accelerating | **0** |
| M12 Negative WC / Float | WC Days computable only FY25 (33.08) and FY26 (29.56) — both in the 15-45 day band (2-year sample; FY18-24 NOT FOUND, no Trade Payables data) | **1** |

**Moats present (score ≥3): M4, M10 = 2 of 12 → Moat classification:
MODERATE** (2-3 present band).

---

## LIMITATIONS / INPUT GAPS

1. Data_Sheet.csv has no Current Liabilities split for FY2018-FY2023 → ROCE
   NOT FOUND for those years; Block A A1/A2/A4 use a 3-year window
   (FY2024-FY2026) built from filed/AR consolidated balance sheets.
2. Data_Sheet.csv has no Trade Payables row for any year → Working Capital
   Days (B4, M12) computable only for FY2025-FY2026 from filed results
   balance sheets.
3. Data_Sheet.csv's "Cash from Investing Activity" aggregates capex with
   large treasury deposit/mutual-fund flows and cannot be used as a capex
   proxy → FCF (B2, B3) computable only for FY2025-FY2026 from the filed cash
   flow statement's explicit "Purchase of property, plant and equipment" /
   "Purchase of intangible assets" lines.
4. Promoter pledge % not found in any provided source (E3 = N/A, scored 0).
5. Promoter shareholding table (SECONDARY tier) starts Jun-2024, so E2 uses a
   2-year change, not the specified 3-year window.
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

---

## CLASSIFICATION

Core score = A(7) + B(18) + C(8) + D(16) + E(8) = **57/100**
Moat score = **10/60**
Grand total = **67/160**
Moat classification: **MODERATE** (2 of 12 tests present: M4, M10)

Data confidence: 9 years overall = moderate tier (7-9 band); no automatic
downgrade. Block A specifically runs on a 3-year computable window — flagged
above, not treated as an overall-history downgrade.

Classification matrix: Core 40-59 → **AVERAGE** (moat tier does not change
this band).

Deal-breakers checked: #1 Block A=7 (<8) → caps at max GOOD (non-binding,
AVERAGE is already below GOOD). #3 median ROCE 13.20% (not <10%, not
triggered). #4 cumulative CFO/PAT 1.92 (not <0.50, not triggered). #7 revenue
did not decline in any year (not triggered). #8 PAT positive in all of the
last 3 years, FY24-26 (not triggered). #9 history is 9 years (not triggered).
#5 pledge unknown (N/A, not triggered as "triggered" requires evidence of
>15%, which is absent, not assumed).

**Strongest block: B (Cash Generation, 18/20)** — but flagged as trailing-4-
year-driven; latest-year direction is down (CFO -21.6% YoY).
**Weakest block: A (Return on Capital, 7/20)**, closely followed by Moat
(10/60) — both driven by the same FY26 capacity-expansion/one-off cost drag.

## DECISION LINE

**AVERAGE.** Core score of 57/100 sits mid-band on its own; the moat profile
is thin (MODERATE, 2/12) rather than a mitigating strength. The FY26
deterioration (ROCE 13.34%→8.35% over FY24-26, PAT -36% YoY, CFO -21.6% YoY)
is traceable to named, dated items — exceptional charges, a large newly
capitalised biologics facility (CWIP 34.9% of net block), and a Q1FY27 Rs 50
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
  - "Data_Sheet.csv has no Trade Payables row any year: WC Days (B4, M12) computed for FY2025-FY2026 only, from filed results BS"
  - "Data_Sheet.csv 'Cash from Investing Activity' mixes capex with treasury deposit/MF flows: FCF (B2, B3) computed for FY2025-FY2026 only, from filed CF statement"
  - "Promoter pledge % not found in shareholding table or AR text: E3 scored 0 as N/A"
  - "Promoter shareholding table (SECONDARY tier) starts Jun-2024: E2 uses 2-year change, not 3-year"
  - "Sector-wide listed-peer universe beyond ANTHEM/SAILIFE/PPLPHARMA not evidenced: M5, M7 flagged PEER DATA NEEDED"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE with named historical depressors: FY26 ROCE fell 13.34% (FY24) to 8.35% (FY26, computed) and PAT fell -36% YoY (Rs 496.2cr to Rs 316.7cr, screener-data), driven by exceptional items (labour-code gratuity re-measurement and termination benefits, net Rs 462mn consolidated FY26, results FY26 audited p.9-10) and depreciation step-up from newly capitalised biologics capacity (CWIP 34.9% of net block at Mar-2026, LBF3); Q1FY27 carried a further Rs 50 cr forex hedge loss (results Q1FY27 p.3). Distinguish capacity-expansion drag from a structural moat failure before any position-size decision."
data_years: 9
fy_range: "FY2018 to FY2026"
blocks: {A: 7, B: 18, C: 8, D: 16, E: 8}
core_score: 57
moat_score: 10
grand_total: 67
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "1: Block A = 7 (<8) -> caps max GOOD (non-binding; Core score already AVERAGE)"
history_downgrade: false
data_notes:
  - "AR Note 38 (standalone) discloses its own ROE/ROCE definitions differing from the fixed formula (ROCE denominator = Tangible Net Worth + Borrowings - DTA): ROCE 14%/13.24%/10.78% and ROE 12%/10%/8% for FY24/FY25/FY26 (AR2025 p.252, AR2026 p.286-287); cited as cross-check only, not scored, and on a standalone basis vs consolidated Data_Sheet basis used elsewhere"
  - "PAT-before-exceptional figure in LBF1 claim (Rs 1 cr) could not be exactly reproduced from the two disclosed filed subtotals (PBT before exceptional and exceptional items, net); directionally consistent (near-breakeven) but not an exact filed line item (results Q1FY27 p.2-3)"
  - "M6 (R&D) and M8 (Distribution) scored 0 as archetype-inapplicable (CRO/CDMO business model), not as pure data gaps"
block_b_trend: "deteriorating - CFO fell to Rs 915.2 cr in FY26 from Rs 1,167.6 cr in FY25 (screener-data), -21.6% YoY, despite +2.6% revenue growth and lower capex"
analyst_note: "FY26 weakness is concentrated and datable, not diffuse: exceptional items (gratuity re-measurement, termination benefits) and depreciation from the newly capitalised Stelis/Baltimore biologics licence (CWIP fell Rs1,266cr to Rs1,046cr as it moved to PP&E) explain most of the ROCE and PAT decline. Block B's strong cumulative ratios (CFO/PAT 1.92x over 9yr) mask that CFO itself fell 21.6% YoY in FY26 - the trailing multi-year average is doing the scoring work, not the current trajectory. Moat score of 10/60 is driven down by peer-relative margin tests (M1, M2) failing against ANTHEM and SAILIFE's higher and more stable EBITDA margins, while stickiness tests (M4, M10) pass because receivable days improved, not because pricing power exists. Treat the Block A/moat weakness as evidence to verify at Halt 1 (is FY26 capacity a one-off drag or a durable margin reset), not as a standalone AVOID signal."
```
