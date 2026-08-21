# FTTCP v2.1 PART B — Financial Normalization Engine — JUBLCPL

Run date 2026-08-18. Part B computed 2026-08-21. Model claude-opus-4-8
(orchestrator, /fttcp normalization layer).

Purpose. The 20-Aug v3.6 recompute (11-valuation-v2) ran Section 1B v3.6,
Debt Capacity, and Market-Implied, but scoped out FTTCP v2.1 PART B. Part B
is the normalization engine Role 1 consumes. This document runs Modules
B1-B8 for both demerger businesses and closes each with the CONSOLIDATED
FTTCP PART B OUTPUT SHEET. Role 1 (11-valuation-v3) reads these sheets and
does not recompute any line.

Method note. SOTP per operator direction (18-Aug). Business A =
Performance Polymers & Chemicals (retained, becomes Jubilant Industries
Ltd). Business B = Agri Division (P&K Fertilizers + Agri Nutrients,
demerges as Jubilant Agri Solutions Ltd). Part A forward verdicts are held
from the 18-Aug gate. Signal Gate caveat stated at the close.

Source anchors: B10-valinputs.yaml, B02-notes.yaml, B03-ardeep.yaml, AR
Note 39 p.150 (segments), Note 50 p.163 / Cash Flow p.101 (cash),
Debt Capacity output (COMFORTABLE), Market-Implied output (FAIRLY PRICED).

---

## CYCLICAL MARGIN RULE — applied per business

**Business A — Performance Polymers & Chemicals: FLAGGED CYCLICAL (mild).**
VP latex and SBR latex are commodity-linked processing (butadiene
feedstock, tyre-demand-linked); PVAc food-grade is specialty and stabilises
the mix. The archetype list flags commodity-linked processors, so the flag
holds, tempered by the specialty share. FY26 segment EBIT margin 14.2%
(EBIT 165.46 / rev 1,164.84). Core segment profit grew only +0.5 to +0.79%
YoY (PBIT Rs 166.3 Mn-scale, Note 39 / MD&A p.19), so FY25 margin was
near-identical. The band is narrow because the specialty mix damps the
cycle.
- Base (full-cycle avg) 14.0%. Bear (trough, feedstock spike) 11.5%.
  Bull (peak) 16.0%.

**Business B — Agri Division: FLAGGED CYCLICAL (strong).** P&K fertilizer,
NBS-subsidy and monsoon dependent. FY26 EBIT 46.8 Cr is a PEAK, inflated by
a +57.17 Cr P&K Fertilizers swing OUT of an FY25 LOSS. FY25 is the trough
(negative). FY26 margin 6.76% is the peak, not normal.
- Base (full-cycle avg) 3.5%. Bear (trough, FY25 loss) negative to ~ -2%.
  Bull (peak, FY26) 6.76%.
- The three-year-average convention is RETIRED here. Normalized PAT
  16 to 18 Cr (valuation-sotp.md) is the full-cycle read; FY26 peak PAT
  allocation is NOT the base.

---

## BUSINESS A — Performance Polymers & Chemicals

### B1 Reinvestment Funding Check
Projected path: FY27 revenue 1,367 Cr (+17.4% on 1,164.84), FY28 1,545 Cr
(+13.0%).
- Channel 1 new reinvestment: incremental ROCE is very high (segment 67.5%;
  even group 36%). Implied reinvestment rate = growth / incremental ROCE =
  17.4% / 67.5% = 25.8% of earnings, or 17.4% / 36% = 48% on the group read.
  FY26 FCF 35.68 Cr and FY27 PAT 125 Cr fund this internally. Debt Capacity
  COMFORTABLE (headroom 93.3%) backs any shortfall.
- Channel 2 utilization ramp: Samlaya Phase 1 partial (3-Jun-2026) to full
  run-rate end Q1 FY27, Phase 2 SBR latex end Q3 FY27 (documented capacity
  headroom). 92.8% of FY26 capex went to PP&C (Note 39).
- Verdict: **PASS FY27 / PASS FY28 / PASS FY29.** Funded by internal cash
  plus documented Samlaya headroom. Shared-catalyst flag: Samlaya funds
  revenue, margin, and ROCE together (single point of failure, counted
  once).

### B2 Forward ROCE vs Minimum ROCE
- Minimum ROCE requirement = r = 14.75% (RRM-derived, Business A r
  worksheet; not the 13.5% default, RRM r is available).
- Forward ROCE path: FY27 ~36% (group, conservative) to 67.5% (segment);
  well above 14.75% in every year. Crossover already passed (Year 0).
- Flag Role 1 reads: **growth premium eligible: YES from FY26.**
- Note for Role 1: B2 clears the ROCE gate, but Amendment 16 sits on top of
  the OTHER Pillar 3 evidence gates. EM score 22.5 < 25 bars the Pillar 3
  premium independently. Net Pillar 3 = +0x. B2 says the ROCE is not the
  constraint; the moat-evidence gate is.

### B3 Normalized Base-Year EPS
Reported EPS is not depressed; FY26 is a normal-to-improving year (margins
and coverage rising). No trough base, no unwind catalyst needed.
**Normalization not applicable, reported EPS stands.** Operating EPS
proceeds from B4.

### B4 Operating Earnings Separation
Non-operating income is immaterial: consolidated other income Rs 4.041 Cr
(2.4% of PBT-scale, AR / 03-ardeep p.257). Finance costs correctly flow
through operating P&L. One classification adjust: Rs 2.284 Cr Labour Code
cost booked as "exceptional" (Note 45 p.157) is arguably recurring; add it
back to operating cost (a small drag), roughly offsetting the treasury
strip.
- Stripped items: treasury/other income Rs ~4.0 Cr (re-enters equity bridge
  as investment value); Labour Code recurring cost Rs 2.284 Cr added back to
  operating expense. Net effect on operating EPS < 1%.
- **Operating EPS (Business A, FY27 forward): ~Rs 82** (reported forward 83,
  less ~Rs 1 net strip). This is the EPS that enters every Role 1 multiple.

### B5 Incentive and Tax Normalization
No PLI, no SEZ, no tax holiday identified for the polymer segment.
Effective tax rate 25.5% FY26, stable, no expiring benefit. No incentive
expires within three years. **Post-expiry economics = current economics;
no restatement.**

### B6 Capex / R&D / Brand Restatement
Polymer/latex R&D and product development are not disclosed as a separate
material expensed intangible; brand spend is B2B and immaterial. The
capital base is not distorted by expensed durable spend at a material
level. **NOT FOUND at a restatable magnitude; module does not apply.
Statutory ROCE stands. Section 1B governs the capital base (no B6
restatement).**

### B7 Post-Deleveraging Earnings Picture
Consumes Debt Capacity (COMFORTABLE). The deleveraging has already
happened: D/E 0.17 to 0.06, interest coverage 8.93x to 23.91x, finance
cost 0.87% to 0.35% of revenue (FY25 to FY26). Consolidated net debt
Rs 45 Cr; the retained polymer entity carries the cash and near-zero net
debt (agri WC borrowing demerges out with Business B).
- Paydown schedule (Business A): net debt Y0 ~0 to slightly net cash; Y1-Y3
  net cash. Interest saving to PAT is immaterial (< Rs 2 Cr), post-delever
  EPS uplift < 1%.
- **Year 3 net debt for the EV bridge: ~0 (net cash).** A small net-cash
  add-back accrues to equity value, not a deleveraging migration.
- Read for Role 1: the lender-to-shareholder migration is SPENT. It is not
  a forward source of return; it is banked. This corroborates the
  Market-Implied FAIRLY PRICED flag.

### B8 Relative Convergence and Re-rating Potential
- (a) Relative position: absolute destination 35x / market PE 20.5x (Nifty
  TTM) = 1.71x relative. Current trading relative 1.36x. The name has
  ALREADY re-rated (+58% in 5 months).
- (b) Companion-variable test: the discount that existed pre-re-rating is
  largely closed; the current multiple is no longer unexplained-cheap. ROCE
  and growth justify a premium, but the market has paid most of it.
- (c) Sector dislocation: specialty chemicals smallcap trades ~34.4x; the
  sector is not collectively cheap. Cheapest-name-in-cheap-sector does not
  apply.
- (d) **Verdict: re-rating potential NONE (fading from MODERATE).**
  Convergence target 35x already within reach of the 1.71x relative; the
  re-rating is banked, not forward. Destination PE sits at the LOW end of
  the range (32.5x) on this read.

### CONSOLIDATED FTTCP PART B OUTPUT SHEET — BUSINESS A
```
FTTCP PART B — NORMALIZATION OUTPUT SHEET  (Business A: Performance Polymers & Chemicals)
Cyclical flag: YES (mild)  cycle: peak FY26 16.0%-scale, trough 11.5%, full-cycle avg 14.0%
Scenario margins: base 14.0%, bear 11.5%, bull 16.0%

B1 Reinvestment funding:   Y1 Channel1+2 PASS / Y2 PASS / Y3 PASS (internal cash + Samlaya headroom; Debt Cap COMFORTABLE)
B2 ROCE crossover:         ROCE path 36-67.5% every year; min ROCE req 14.75% (RRM r);
                           growth premium eligible: YES from FY26  [but EM 22.5<25 bars Pillar 3 independently -> net +0x]
B3 Base-year EPS:          reported ~83 fwd, normalization NOT APPLICABLE, reported stands
B4 Operating EPS:          operating EPS ~82 (FY27 fwd); stripped: other income ~4.0 Cr (to bridge), +Labour Code 2.284 Cr recurring add-back
B5 Incentives:             none (no PLI/SEZ/holiday); post-expiry margin = current 14.0%, post-expiry EPS unchanged
B6 Restated efficiency:    statutory ROCE stands (no material expensed intangible); route: Section 1B governs
B7 Deleveraging:           net debt Y0~0 -> Y3 ~0 (net cash); post-delever EPS uplift <1%; Year 3 net debt ~0 (small net-cash add to bridge)
B8 Re-rating potential:    NONE (fading from MODERATE); convergence target 35x already ~banked; destination at LOW end 32.5x; gate: first standalone polymer accounts
```

---

## BUSINESS B — Agri Division (P&K Fertilizers + Agri Nutrients)

### B1 Reinvestment Funding Check
Projected path: FY27 revenue 727 Cr (+5.0% on 692.34), stepping down from
the FY26 peak on a weak monsoon Q1.
- Growth is trivial and cyclical, not a compounding path. Agri took only
  7.2% of FY26 capex. Funded by Channel 2 utilization on existing assets.
- Verdict: **PASS (low-growth, utilization-funded).** No Channel 1
  reinvestment thesis; the growth is cyclical mean-drift, not funded
  expansion.

### B2 Forward ROCE vs Minimum ROCE
- Minimum ROCE requirement = r = 15.5% (RRM-derived, Business B r
  worksheet).
- Forward ROCE: normalized 19.9% > 15.5% on the segment allocation, but the
  trough year prints a LOSS (FY25 P&K Fert). On a full-cycle basis ROCE is
  well below the peak read and near the requirement.
- Flag Role 1 reads: **growth premium eligible: NO** (marginal crossover on
  the peak-allocation number, fails on a full-cycle basis; ROCE verdict
  STAGNANT, no growth to pay for). Pillar 3 = +0x.

### B3 Normalized Base-Year EPS
FY26 is a PEAK, not a depressed base. B3 normalizes UPWARD off troughs; it
does not apply here. The required normalization is DOWNWARD and is handled
by the cyclical margin rule (base = full-cycle avg, not the FY26 peak).
**Normalization not applicable (base is a peak); cyclical rule governs the
downward normalization to PAT 16-18 Cr.**

### B4 Operating Earnings Separation
Subsidy income is operating revenue for a fertilizer processor, not
treasury. No material non-operating income in the segment. **Operating
(normalized) PAT Rs 17 Cr (midpoint 16-18); this is the earnings that enter
the Business B multiple.** Valued absolute for SOTP, not per JACPL share.

### B5 Incentive and Tax Normalization
The NBS fertilizer subsidy is STRUCTURAL government policy revenue, not a
time-limited PLI/SEZ/holiday. It does not "expire" inside the hold; it
fluctuates with notified rates (a cyclicality input, not a B5 expiry). Its
cash-collection lag is a Pillar 2 issue (0.80x cash multiplier), not a B5
restatement. **No incentive expires within three years; no post-expiry
restatement. Subsidy-rate risk is carried as cyclicality and cash quality,
not here.**

### B6 Capex / R&D / Brand Restatement
No material expensed durable spend. **Does not apply; statutory stands.**

### B7 Post-Deleveraging Earnings Picture
The agri working-capital borrowing (subsidy-receivable-driven) demerges
with Business B. Modest WC debt, funded against subsidy receivables.
- Year 3 net debt: small positive (seasonal WC), no deleveraging thesis.
  **Year 3 net debt for the EV bridge: modest positive; no migration
  value.** The cash-conversion drag (CFO/PAT 0.59x, >6m subsidy bucket
  7.86%) lives here (FLAG-CASH, Pillar 2 0.80x).

### B8 Relative Convergence and Re-rating Potential
Agri processing, cyclical, at a subsidy-driven peak. No unexplained
discount; no re-rating candidate. **Re-rating potential: NONE.** Destination
stays on normalized earnings at the additive-track 14x (Agri processing 20x
cap not binding).

### CONSOLIDATED FTTCP PART B OUTPUT SHEET — BUSINESS B
```
FTTCP PART B — NORMALIZATION OUTPUT SHEET  (Business B: Agri Division)
Cyclical flag: YES (strong)  cycle: peak FY26 6.76%, trough FY25 ~ -2% (P&K Fert loss), full-cycle avg 3.5%
Scenario margins: base 3.5%, bear ~ -2% (trough), bull 6.76% (peak)

B1 Reinvestment funding:   Y1-Y3 PASS (low-growth, Channel 2 utilization; no funded expansion thesis)
B2 ROCE crossover:         normalized ROCE 19.9% (peak-allocation) vs full-cycle near req; min ROCE req 15.5% (RRM r);
                           growth premium eligible: NO (STAGNANT, fails full-cycle)
B3 Base-year EPS:          FY26 is a PEAK not a trough; normalization NOT APPLICABLE; cyclical rule normalizes DOWN to PAT 16-18 Cr
B4 Operating EPS:          normalized operating PAT ~17 Cr (subsidy is operating revenue, no treasury strip)
B5 Incentives:             NBS subsidy is structural (not an expiring incentive); no post-expiry restatement; rate risk carried as cyclicality
B6 Restated efficiency:    statutory stands (no expensed intangible); Section 1B governs
B7 Deleveraging:           agri WC debt (subsidy-receivable-driven) demerges here; Year 3 net debt modest positive; no migration value; FLAG-CASH lives here (0.80x)
B8 Re-rating potential:    NONE (cyclical peak, no unexplained discount); destination 14x on normalized earnings
```

---

## SINGLE-CREDIT MAP (must hold; Role 1 verifies before valuing)
- ROCE recovery: lives in Section 1B Pillar 1 (current ROCE base), NOT also
  in the Strategic Premium. Business A Strategic +2x is the VP-latex market
  position, not a ROCE re-rating. HOLDS.
- Capital-base distortion: B6 does NOT apply (no material expensed
  intangible); Section 1B governs. No double-fix. HOLDS.
- Depressed base year: B3 does NOT apply to either business (A not
  depressed; B is at a peak). No Route B double-count. HOLDS.
- Cash quality: priced once in Pillar 2 (A 1.15x, B 0.80x); the r-table
  cash-conversion r-UP is DELETED per Amendment 12A. HOLDS.
- Complexity: priced once in r (+0.5, Amendment 13); does not dock a pillar
  or scale a premium. HOLDS.

## SIGNAL GATE CAVEAT (FTTCP v2.1)
The v2.1 Signal Gate requires Role 5.5 Step 4 to have PASSED: the six
rank-1-3 downstream signals physically WRITTEN to the Notion Downstream
Signal Tracker (data source 926b65ce-...) with row URLs. That write is
operator-gated and NOT yet performed. Per the gate, the Part A catalysts
therefore rest on described-but-unwritten signals, so the FTTCP composite
reference is CAVEATED, not gated-clean. This does not change the Part B
normalization outputs (financial, not signal-dependent); it flags that the
Part A verdicts feeding B2's growth-premium context are not yet
tracker-anchored. Clear by writing the tracker rows.

## WHAT PART B CHANGES FOR ROLE 1 (vs the 20-Aug v3.6 recompute)
Part B CONFIRMS the v2 recompute and adds two documented refinements:
1. B7 makes explicit that Business A is ~net cash at Year 3 (deleveraging
   spent). Role 1 adds a small net-cash back-add to the equity bridge; it
   is not a forward return source.
2. B8 NONE hardens the Business A destination to the LOW end (32.5x),
   corroborating the Amendment 15 relative-PE lean already applied in v2.
No Part B module moves the earnings base materially (B4 operating EPS ~82
vs reported 83; B3/B5/B6 not applicable). The valuation direction is
unchanged: WATCHLIST, more marginal on every metric.
