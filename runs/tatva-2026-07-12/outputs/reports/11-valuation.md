# STAGE 11: ROLE 1 MULTI-MODAL VALUATION
## Tatva Chintan Pharma Chem Ltd (TATVA)
**Run Date:** 2026-07-12 | **Model:** claude-opus-4-8 | **CMP:** Rs 1,326
**Frameworks applied:** Master Project Prompt v3.3 (Role 1) / Section 1B v3.3 + v3.4 amendments (Pillar 3 decoupled 3a/3b/3c, two-tier hurdle) / FTTCP v1.2

> Pipeline mode: all sections executed in one pass, no interactive stops. Interim checkpoint lines are written where the framework says STOP, then execution continues. All inputs are drawn ONLY from the B10 table. Where a value sits in B10.unresolved, the conservative-assumption line is stated explicitly. All figures in Rs Crore unless marked. Rupee-Mn to Cr conversions carry the B10 anchor the first time each input is used.

---

## INPUT RECONCILIATION (B10, sole source)

| Input | Value | Anchor (carried from B10) |
|---|---|---|
| CMP | Rs 1,326 | Manifest |
| Market Cap | Rs 3,103 Cr | Manifest |
| Shares (diluted) | 2.339 Cr | Q4 FY26 results line 388 |
| Net Debt | Rs 114.6 Cr (1,146.1 Mn) | Q4 FY26 balance sheet |
| Enterprise Value | Rs 3,217.6 Cr (32,176.1 Mn) | Computed Mcap + ND |
| Revenue FY26 (Y0) | Rs 505.86 Cr (5,058.6 Mn) | Consol Q4 FY26 line 325 |
| EBITDA FY26 | Rs 96.71 Cr (967.1 Mn), 19.1% | Computed PBT+Int+Dep |
| PAT FY26 | Rs 42.05 Cr (420.5 Mn), 8.3% | Consol Q4 FY26 line 352 |
| Diluted EPS FY26 | Rs 17.98 | Consol Q4 FY26 line 386 |
| CFO FY26 | Rs 31.49 Cr (314.9 Mn) | Consol CF line 501 |
| FCF FY26 | Rs -82.28 Cr (-822.8 Mn) | CFO - Capex |
| BVPS FY26 | Rs 334.6 | Equity 7,817.59 Mn / 2.339 Cr |
| Capex FY26 | Rs 113.77 Cr (1,137.7 Mn) | Consol CF line 503 |
| Depreciation FY26 | Rs 36.85 Cr (368.5 Mn) | Consol results line 340 |
| ROCE FY26 | 6.6% | Deliberation record line 45 (authoritative) |
| ROE (standalone) | 5.4% | Standalone results |
| CFO/PAT latest | 0.75x | 314.9 / 420.5 |
| CFO/PAT cumulative FY19-26 | -1.32x | B01 line 41 |
| FCF/PAT | -1.95x | B10 |
| Rev CAGR 3yr | 14.7% | Screener FY24-FY26 |
| Current P/E (trailing) | **73.75x** (1,326 / 17.98) | Computed |
| Current EV/EBITDA | 33.3x | 3,217.6 / 96.71 |
| Current P/B | 3.96x | 1,326 / 334.6 |

**Deliberation-confirmed authoritative inputs (applied as given, not re-litigated):**
- FTTCP ROCE forward verdict = **RECOVERING, probability 40-60%** -> Pillar 1 ROCE = 60/40 weighted average of current ROCE 6.6% (FY26) and FY28 expected ROCE (base 8.5%, bear 6.3%, bull 10.6%). Recovery credited via **Pillar 1 only** (single-credit; NOT Strategic Premium).
- Cash conversion = **INDETERMINATE leaning structural** -> Pillar 2 multiplier **0.80x, no growth offset** (conservative band applied per B10).
- Sector cap = **Specialty chemicals 35x** (absolute; corrects manifest 38x).
- UA all_met = **false** -> no 1.25x; F2 row shown as F.
- **SHARED CATALYST** flag on Dahej commissioning (Pillar 1 forward ROCE and Pillar 3a).
- credibility_grade **B** -> 4D weights 25/50/25; Bull EPS CAGR usable in Hurdle check.

**INPUT UNRESOLVED: rating_wc_quote.** Conservative assumption used: no rating-agency confirmation of *structural* WC, therefore Pillar 2 is held at the 0.80x band (not the 0.65x structural band which requires rating-agency confirmation), while ALSO withholding any growth offset, because B10 marks the determination INDETERMINATE leaning structural. This is the more conservative reading available without the rating PDF (it neither rewards a growth offset nor lets an unconfirmed structural label push the multiplier below 0.80x arbitrarily). Rule basis: Section 1B Pillar 2 CRITICAL DISTINCTION + wrapper INPUT DISCIPLINE.

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

Tatva is a capital-heavy, four-product specialty chemicals manufacturer (PTC 33.0%, SDA 31.5%, ESS 1.6%, PASC 33.9% FY26 mix; B10) with cyclical earnings (FY25 EPS trough Rs 2.44, FY26 Rs 17.98), high working-capital intensity, negative FCF in all 8 computable years, and depressed ROCE (6.6%). The business is asset-intensive with varying leverage across the capex cycle.

### Method Suitability

| Method | Suitable here? | Why |
|---|---|---|
| P/E | YES (Primary) | Section 1B destination PE is the exit-multiple authority. Earnings cyclical but recovering; the four-pillar framework prices the ROCE/cash quality directly. Cyclicality handled via bear/base/bull EPS. |
| EV/EBITDA | YES (Secondary) | Capital-intensive, varying leverage across the Dahej/Jolva capex cycle; neutralises capital structure. Caveat: capex (113.8 Cr) >> depreciation (36.9 Cr), so EBITDA overstates cash -> multiple discounted. |
| P/B | YES (Tertiary) | Asset-heavy; BVPS Rs 334.6 meaningful. Theoretical P/B = ROE/CoE disciplines a below-cost-of-capital return to sub-1x. Cross-check on the cyclical earnings methods. |
| DCF | NO | FCF negative across all 8 computable years; cyclical; terminal value would dominate. Fails the "predictable stable cash flow" test. Excluded. |
| EV/Sales, DDM, EV/Capacity, SOTP | NO | Not business-appropriate; margins/cash are the value question, not revenue proxy or capacity proxy. |

### Final Method Selection

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (Section 1B four-pillar destination) | 50% | Sole exit-multiple authority; prices ROCE + cash quality |
| SECONDARY | EV/EBITDA | 30% | Capital-intensity and leverage neutralisation; capex-adjusted |
| TERTIARY | P/B (ROE/CoE) | 20% | Asset-heavy cross-check; disciplines sub-CoE return |
| | | 100% | |

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3/v3.4

### Pillar 1: ROCE Base Multiple (continuous formula)

FTTCP ROCE forward verdict = **RECOVERING, probability 40-60%**. Per the FTTCP v1.2 Pillar 1 table (sole authority), ROCE used = **60/40 weighted average of current (FY26 6.6%) and FY[Y+2] (FY28) expected ROCE**. 60% weight on current (the known, conservative anchor), 40% on the forward estimate.

| Scenario | FY28 est ROCE | Blend = 0.6x6.6 + 0.4xFY28 | Base PE = 0.5xROCE + 7.5 (floor 9, cap 24) |
|---|---|---|---|
| Bear | 6.3% | 0.6(6.6)+0.4(6.3) = **6.48%** | 0.5(6.48)+7.5 = **10.7x** |
| Base | 8.5% | 0.6(6.6)+0.4(8.5) = **7.36%** | 0.5(7.36)+7.5 = **11.2x** |
| Bull | 10.6% | 0.6(6.6)+0.4(10.6) = **8.20%** | 0.5(8.20)+7.5 = **11.6x** |

- FTTCP ROCE forward verdict: RECOVERING (40-60%)
- ROCE used for base (base case): **7.36%**
- ROCE Base Multiple (base): **11.2x** (above the 9x floor, below 24x cap)
- **ROCE recovery credited via: Pillar 1 (midpoint blend).** Strategic Premium ROCE re-rating optionality is therefore withheld (single-credit rule, Amendment 4).

### Pillar 2: Cash Conversion Multiplier

- Cumulative CFO/PAT (FY19-26): -1.32x | Latest FY CFO/PAT: 0.75x | FCF positive? **No** (negative all 8 years)
- Cash quality band: CFO negative / cumulative negative -> nominal 0.80x band.
- Structural or growth-induced? **INDETERMINATE leaning structural** (B10). Evidence: debtor days 48 -> 86 across FY22-FY26 through flat-revenue years (growth does not explain); receivables +18.1% while revenue fell; top-3 customer 61% of receivables, zero ECL; WC days 175.3 -> 185.3. The "if growth stopped tomorrow, would WC days stay high?" test leans YES.
- Rating-agency confirmation of structural: **NOT FOUND** (no rating PDF). INPUT UNRESOLVED handled above.
- Growth offset applicable? **No** (leaning structural; deliberation withholds offset). Offset = +0.
- **Effective Cash Multiplier: 0.80x.**

**Quality-Adjusted Base = ROCE Base x Cash Multiplier:**

| Scenario | ROCE Base | x Cash 0.80x | Quality-Adjusted Base |
|---|---|---|---|
| Bear | 10.7x | x0.80 | **8.56x** |
| Base | 11.2x | x0.80 | **8.96x** |
| Bull | 11.6x | x0.80 | **9.28x** |

### Pillar 3: Growth Visibility Premium (v3.4 decoupled: 3a + 3b + 3c, combined cap +6x)

**3a Growth Visibility Premium** (documented growth machinery, 📄 only):

| Qualifier | Status | Evidence |
|---|---|---|
| Capex-embedded growth >=15% (committed capex x FA-turnover / revenue) | **NOT MET** | No clean 📄 committed forward-capex figure in B10; Jolva (Rs 400-500cr guided) sits on weakest execution track (3x slipped, FLAG-EMOAT). Not documented-tier quantifiable. |
| Order book >=1.0x rev or book-to-bill >=1.2x | **NOT MET** | Specialty-chemical maker; no order book disclosed. |
| SOM-implied revenue CAGR >=20% with capacity cross-check | **NOT MET** | SOM-implied CAGR 14.3% (3yr) / 13.9% (5yr), below 20% (B09). |
| Management delivery grade A or B | **MET** | Grade B (B05). |

Only 1 of 4 qualifiers met. Award rule: +2x needs any two; +3x needs three-plus and grade A/B. **3a = +0x.**

**3b Moat Formation Premium** (EM-gated): EM score 19.2 (below 25 threshold) -> **3b = +0x.**

**3c Duration Premium** (documented forward revenue visibility >=2.5yr): no order book / contracted-revenue tenor documented -> **3c = +0x.**

- **Pillar 3 total = +0x.**
- **SHARED CATALYST flag (Dahej commissioning):** the Dahej commissioning that underpins the Pillar 1 forward-ROCE blend is also the growth driver that *would* have fed 3a. Flagged per deliberation so Role 3 stress-tests the single point of failure. Because 3a resolves to +0x on documented-evidence grounds, no premium is actually credited through the shared catalyst, but the flag stands.

### Strategic Asset Premium

- ROCE re-rating optionality: **withheld** (recovery already credited in Pillar 1; single-credit rule).
- Rare licence / regulatory monopoly: No. Moats present (switching costs HIGH durability; proprietary electrolysis route, niche global SDA scale) but B10 rates most durability MODERATE and pricing power moderate; company competes with global peers. Not "genuine scarcity limiting new entry."
- Strong brand/franchise with *documented* pricing power: pricing power is moderate (B10), not documented-strong. Does not qualify.
- **Strategic Premium = +0x** (conservative). Sensitivity: even a generous +2x for the niche SDA switching-cost position would lift Raw PE to ~11x and does not change the Hurdle verdict (shown in the Hurdle section).

### Four-Pillar Summary Calculation (base case)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 7.36% -> 0.5(7.36)+7.5 | 11.2x |
| B. Cash Multiplier (effective) | 0.80x + offset 0 | 0.80x |
| C. Quality-Adjusted Base | A x B = 11.2 x 0.80 | 8.96x |
| D. Growth Visibility Premium (3a+3b+3c) | 0 + 0 + 0 | +0x |
| E. Strategic Premium | (single-credit; none qualifying) | +0x |
| F. Raw Destination PE | C + D + E | **8.96x** |
| F2. UA-Adjusted Raw PE | F x 1.25 only if all 3 UA qualifiers hold; **all_met=false** -> F2 = F | **8.96x** |
| G. Sector Cap | Specialty chemicals (no UA uplift) | 35x |
| **H. Final Destination PE** | **min(F2, G) = min(8.96, 35)** | **8.96x (~9.0x)** |

**Track 2 (Additive) Destination PE Range: 8.96x +/-7.5% = 8.29-9.63x -> rounded 8.5x to 9.5x (mid 9.0x).**
Scenario destination PEs (from scenario ROCE blends): bear 8.56x, base 8.96x, bull 9.28x.

### RRM Dual-Track Derivation

**Track 1 (RRM):** Destination PE = Fundamental Base PE x RRM, capped at sector cap.
- Base r: small/micro-cap = 14%. Adjustment for governance (FLAG-PROMOTER CAUTION: GPCB plant closure Sept 2024; promoter remuneration +27.89% while standalone PAT fell 98.9%; two CRISIL downgrades in the window) and moderate durability -> **r = 15%** (within [9%, 18%]).
- RRM = 1 + (13.5 - r) x 0.12, percentage-point reading (Amendment 4.4) = 1 + (13.5 - 15) x 0.12 = 1 + (-1.5)(0.12) = 1 - 0.18 = **0.82** (within [0.70, 1.60]).
- Fundamental Base PE = Quality-Adjusted Base = Raw F = 8.96x (premiums are zero, so C = F here).
- **Track 1 Destination PE (base) = 8.96 x 0.82 = 7.35x (~7.3x).** Range +/-7.5% = 6.80-7.90x -> rounded 7.0x to 8.0x (mid 7.3x).
- Scenario: bear 8.56x0.82 = 7.0x; base 7.3x; bull 9.28x0.82 = 7.6x.

**Track divergence:** Track 2 mid 9.0x vs Track 1 mid 7.3x. Divergence = (9.0 - 7.3)/9.0 = **18.9%** (>15%). **Governing (more conservative) track = Track 1 (RRM).** It is also the more *appropriate* track here: RRM prices the governance amber cluster (FLAG-PROMOTER) and moderate durability through the discount rate, whereas the additive track applies no negative for governance. Track 1 sets the entry zone.

> **CHECKPOINT (framework STOP point):** Section 1 complete. Methods P/E (50) / EV/EBITDA (30) / P/B (20). Four-pillar destination PE: Track 2 additive **8.5x-9.5x**, Track 1 RRM **7.0x-8.0x**. Current PE **73.75x**. The destination PE is ~1/8th of the current PE. Hurdle Ratio computed below. Continuing.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS

Year 0 = FY26 (Rs 505.86 Cr revenue, EPS 17.98). Years 1/2/3/5 = FY27/28/29/31.

### 2A. Revenue Projection

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| Growth logic | 1-2 triggers fail (SDA slips, Jolva 4th slip); demand soft | Historical/SOM-anchored; SDA ramps, Dahej block earns | FY27 guidance ~25% at face (grade B), tapering |
| Revenue CAGR | 9% | **14%** | 20% |
| Y1 (FY27) | 551.4 | 576.7 | 607.0 |
| Y2 (FY28) | 601.0 | 657.4 | 728.4 |
| Y3 (FY29) | 655.1 | 749.4 | 874.1 |
| Y5 (FY31) | 778.3 | 974.0 | 1,258.8 |

Growth-rule compliance: Bear = historical 14.7% - ~5.7% floored near industry -> 9%. Base = lower of (management 25% discounted by grade-B track record) and (historical 14.7% / SOM 14.3%) -> **14%**. Bull = FY27 guidance ~25% at face (grade B permits), tapered to 20% 3yr CAGR for Jolva execution risk.

**SOM cross-check:** Base 3yr revenue Rs 749.4 Cr vs B09 SOM-implied 3yr Rs 754 Cr (14.3% CAGR). Base assumption 14% <= SOM-implied 14.3% -> **CONSISTENT** (does not exceed the SOM ceiling; no cut required). Y5 base Rs 974 Cr vs SOM 5yr Rs 968 Cr, within rounding.

### 2B. Profitability Projection

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| EBITDA margin | 18% | 20% | 22% |
| Margin logic | current -110bps; utilisation stalls | low end of FY27 guided 20-22% band, sustained | guided 22% at face (grade B) |
| Depreciation (Y3) | 50 | 48 | 46 |
| Interest (Y3) | 6 | 5 | 4 |
| Tax rate | 26% | 26% | 26% |
| Dilution | ~0% | ~0% | ~0% |

Margin rules: Bear = current 19.1% - ~110bps to 18%. Base = 20% (low end of guided band; recovery credible given Q2->Q4 FY26 trajectory 18.0%->20.9%). Bull = guided 22%. Tax rate from FY26 effective (57.0 PBT vs 42.05 PAT = 26.2%).

### 2C. Complete Projection Table (BASE CASE primary)

| Line Item | Y0 (FY26) | Y1 | Y2 | Y3 (FY29) | Y5 (FY31) |
|---|---|---|---|---|---|
| Revenue | 505.86 | 576.7 | 657.4 | 749.4 | 974.0 |
| EBITDA | 96.71 | 115.3 | 131.5 | 149.9 | 194.8 |
| EBITDA margin | 19.1% | 20% | 20% | 20% | 20% |
| Depreciation | 36.85 | 40.5 | 44.0 | 48.0 | 56.0 |
| Interest | 2.85 | 3.5 | 4.0 | 5.0 | 5.0 |
| PBT | 57.0 | 71.3 | 83.5 | 96.9 | 133.8 |
| PAT (26% tax) | 42.05 | 52.8 | 61.8 | 71.7 | 99.0 |
| EPS (diluted) | 17.98 | 22.6 | 26.4 | **30.65** | 42.3 |
| Book Value/share | 334.6 | ~355 | ~379 | ~408 | ~470 |
| Est. CFO | 31.5 | ~55 | ~70 | ~90 | ~150 |
| Est. FCF | -82.3 | ~-30 | ~+5 | ~+30 | ~+80 |
| Est. Net Debt | 114.6 | ~145 | ~150 | ~150 | ~120 |
| Est. ROCE | 6.6% | ~7.5% | ~8.7% | ~9.7% | ~11.5% |
| Est. ROE | 5.4% | ~6.4% | ~7.0% | ~7.5% | ~9.0% |

**Scenario EPS (Year 3):** Bear **Rs 17.69** (CAGR -0.5%), Base **Rs 30.65** (CAGR 19.5%), Bull **Rs 43.74** (CAGR 34.5%).
Bear Y3: rev 655.1 x18% = 117.9 EBITDA; -50 dep -6 int = 61.9 EBIT; PBT 55.9; PAT 41.4; EPS 17.69.
Bull Y3: rev 874.1 x22% = 192.3 EBITDA; -46 dep -4 int = 142.3 EBIT; PBT 138.3; PAT 102.3; EPS 43.74.

### 2D. Projection Sanity Checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | Base 14% <= SOM 14.3%; capacity ceiling ~731 Cr (Jolva-inclusive) vs Y3 749 Cr -> marginal, binding if Jolva slips again | BORDERLINE |
| Margins require something unprecedented? | 20% base is inside guided 20-22% and below Q4 FY26 20.9% run-rate | Yes (pass) |
| ROCE stays above 15%? | **No** - Y3 base ~9.7%, structurally sub-15% and below CoE ~14% | **FAIL (drives the low destination PE)** |
| FCF funds growth without excess debt? | FCF turns marginally positive only by Y2-Y3; net debt creeps to ~150 Cr | Marginal |
| EPS growth operational, not financial engineering? | Driven by revenue + margin recovery + operating leverage, no buybacks/dilution games | Yes (pass) |
| Implied market share realistic? | Base revenue at/below SOM -> realistic | Yes (pass) |
| CFO/PAT trajectory consistent with Pillar 2 (0.80x)? | Improving toward ~1.0x+ by Y3 in base, but cumulative history and receivables risk keep the conservative 0.80x defensible for the *exit* multiple | Consistent (conservative) |
| **FTTCP-consistency:** Is Y3 ROCE consistent with the RECOVERING verdict used in Pillar 1? | Y3 base ROCE ~9.7% (FY29) vs FY28 base 8.5% feeding Pillar 1 -> continued gradual recovery, still below 15%, does NOT exceed the RECOVERING profile. Pillar 1 blend (7.36%) is deliberately more conservative than the projected path. | **CONSISTENT** |

> **CHECKPOINT (framework STOP point):** Section 2 complete. Base Y3 EPS Rs 30.65 (19.5% CAGR). Continuing to methods.

---

## SECTION 1B HURDLE RATIO (25% CAGR feasibility)

**Two-tier assignment (Amendment 4.3):** Tier B requires ALL of {FII+DII >=3%, Gate 0 GOOD+ or EM>=25, promoter TRUSTWORTHY+, no structural FLAG-CASH}. Tatva: Gate 0 = 48 (AVERAGE, fails), EM 19.2 (<25, fails), promoter CAUTION (fails), FLAG-CASH structural-leaning (fails). -> **Tier A (default), hurdle 25% CAGR, HR pass threshold 1.953.**

**HR = (1 + EPS CAGR)^3 x (Destination PE mid / Current PE). Current PE = 1,326 / 17.98 = 73.75x.**

| EPS CAGR | (1+g)^3 | Track 1 mid 7.3x -> HR | Track 2 mid 9.0x -> HR |
|---|---|---|---|
| Base 19.5% | 1.7047 | 1.7047 x (7.3/73.75) = **0.169** | 1.7047 x (9.0/73.75) = **0.208** |
| Bull 34.5% (grade B permits) | 2.4327 | 2.4327 x (7.3/73.75) = **0.241** | 2.4327 x (9.0/73.75) = **0.297** |

Every cell is far below 1.953. **HR(Bull) = 0.24-0.30 << 1.953 -> HURDLE VERDICT: STOP.** Overvalued; 25% CAGR is infeasible even on bull-case earnings.

**Why:** the destination PE (7-9x, earned by a ~7% ROCE below cost of capital and cash leakage) is roughly one-eighth of the current 73.75x trailing PE. The de-rating from 73.75x toward 9x (~-88%) overwhelms any plausible EPS growth. Even the +2x strategic-premium sensitivity (Raw PE ~11x, Track 2) gives HR(Bull) = 2.4327 x (11/73.75) = 0.363 -> still STOP.

Per the wrapper and Master v3.3: HR = STOP means the verdict card says **AVOID-on-valuation**; all remaining sections are completed for the record.

Would I personally pay ~9x for this quality of business (sub-CoE ROCE, negative cumulative FCF, FLAG-CASH, FLAG-PROMOTER)? No. The destination PE stands; the current price does not.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY: P/E (Section 1B destination)

| Source | Exit PE Range |
|---|---|
| Track 2 additive destination PE | 8.5x - 9.5x (mid 9.0x) |
| Track 1 RRM destination PE | 7.0x - 8.0x (mid 7.3x) |
| Sector cap | 35x (not binding) |
| Applied | Track-specific mids above |

**Target price matrix (Year 3), Track 2 additive (mid 9.0x):**

| | Exit 8.5x | Exit 9.0x | Exit 9.5x |
|---|---|---|---|
| Bear EPS 17.69 | Rs 150 (-52%/yr) | Rs 159 (-51%/yr) | Rs 168 (-50%/yr) |
| Base EPS 30.65 | Rs 260 (-42%/yr) | Rs 276 (-41%/yr) | Rs 291 (-40%/yr) |
| Bull EPS 43.74 | Rs 372 (-34%/yr) | Rs 393 (-33%/yr) | Rs 415 (-32%/yr) |

All 9 cells 🔴 (<15% CAGR); all deliver capital loss from CMP 1,326. Colour: 9/9 red, 0/9 above 15%.

**Track 1 RRM (mid 7.3x):** Bear Rs 129, Base Rs 224, Bull Rs 319.

**Reverse-engineered entry (25% CAGR, base EPS, Track 1 governing mid 7.3x):** Year 3 target = 30.65 x 7.3 = Rs 224; required entry = 224 / 1.953 = **Rs 115**.

**P/E method fair value (Year 3): Track 1 Rs 129-319 (base 224); Track 2 Rs 159-393 (base 276).**

### SECONDARY: EV/EBITDA

Exit EV/EBITDA ~= 0.6-0.7x of PE destination, further discounted because capex (113.8) >> depreciation (36.9). Track 2 PE 9.0x -> ~5.5x base; Track 1 PE 7.3x -> ~4.5x base.

| | Bear EBITDA 117.9 | Base EBITDA 149.9 | Bull EBITDA 192.3 |
|---|---|---|---|
| Exit multiple (Track 2) | 5.0x | 5.5x | 6.0x |
| EV | 589.5 | 824.5 | 1,153.8 |
| Less Y3 Net Debt | 200 | 150 | 100 |
| Equity Value | 389.5 | 674.5 | 1,053.8 |
| / 2.339 Cr shares | **Rs 166** | **Rs 288** | **Rs 451** |

Track 1 (multiples ~0.82x of above: 4.0x/4.5x/5.0x): Bear Rs 116, Base Rs 224, Bull Rs 368.

**EV/EBITDA method fair value (Year 3): Track 1 Rs 116-368 (base 224); Track 2 Rs 166-451 (base 288).**

### TERTIARY: P/B (ROE / CoE)

Theoretical P/B = ROE / CoE. Base recovering ROE ~9.5-10% / CoE 14% = **~0.71x**. Bear ROE ~7% / 14% = 0.50x. Bull ROE ~13-14% / 14% = ~0.9x. Applied to Year 3 BVPS (base ~Rs 408, bear ~Rs 395, bull ~Rs 425):

| | Bear | Base | Bull |
|---|---|---|---|
| Y3 BVPS | 395 | 408 | 425 |
| Fair P/B | 0.50x | 0.71x | 0.90x |
| Fair value | **Rs 198** | **Rs 290** | **Rs 383** |

(Track-agnostic; ROE/CoE already prices the below-cost-of-capital return. Note current P/B 3.96x vs fair ~0.71x confirms the same overvaluation.)

### Method-wise Fair Value Summary (Year 3)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E (Track 1 / Track 2) | 50% | 129 / 159 | 224 / 276 | 319 / 393 |
| EV/EBITDA (Track 1 / Track 2) | 30% | 116 / 166 | 224 / 288 | 368 / 451 |
| P/B (both) | 20% | 198 | 290 | 383 |

> **CHECKPOINT (framework STOP point):** Section 3 complete. Continuing to triangulation.

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & FINAL VERDICT

### 4A. Triangulated Fair Value (both tracks, Year 3)

**Track 1 (RRM, governing):**
| | Bear | Base | Bull |
|---|---|---|---|
| P/E x0.50 | 64.5 | 112.0 | 159.5 |
| EV/EBITDA x0.30 | 34.8 | 67.2 | 110.4 |
| P/B x0.20 | 39.6 | 58.0 | 76.6 |
| **Weighted FV** | **Rs 139** | **Rs 237** | **Rs 347** |

**Track 2 (Additive):**
| | Bear | Base | Bull |
|---|---|---|---|
| P/E x0.50 | 79.5 | 138.0 | 196.5 |
| EV/EBITDA x0.30 | 49.8 | 86.4 | 135.3 |
| P/B x0.20 | 39.6 | 58.0 | 76.6 |
| **Weighted FV** | **Rs 169** | **Rs 282** | **Rs 408** |

Fair-value divergence (base): (282 - 237)/282 = 16.0% (>15%) -> **Track 1 governs the entry zone.**

### 4B. Methods Agreement Check

| Check | Result |
|---|---|
| All methods same direction? | Yes - all point far below CMP 1,326 |
| Spread high-low method (base, Track 2) | P/E 276, EV/EBITDA 288, P/B 290 -> ~5% spread. Tight. |
| Outlier? | None material |
| Most-trusted method here | P/E (Section 1B destination) - it is the exit-multiple authority and directly prices the sub-CoE ROCE and cash leakage |

### 4C. Return Expectation at Current Price (Track 1 governing)

| Scenario | Weighted FV (Y3) | CMP | Total Return | 3yr CAGR | Meets 25%? |
|---|---|---|---|---|---|
| Bear | 139 | 1,326 | -89.5% | -52.9% | 🔴 |
| Base | 237 | 1,326 | -82.1% | -43.7% | 🔴 |
| Bull | 347 | 1,326 | -73.8% | -36.0% | 🔴 |

(Track 2: Bear -48.9%, Base -39.9%, Bull -31.9% CAGR - same conclusion.)

### 4D. Probability-Weighted Expected Return (grade B: 25/50/25)

| Scenario | Probability | 3yr CAGR (Track 1) | Weighted |
|---|---|---|---|
| Bear | 25% | -52.9% | -13.2% |
| Base | 50% | -43.7% | -21.9% |
| Bull | 25% | -36.0% | -9.0% |
| **Expected CAGR** | 100% | | **-44.1%** |

Grade source: B05 credibility grade B (25/50/25). Track 2 expected CAGR = -40.0%. Both deeply negative.

### 4E. My Entry Price (Tier A, divisor 1.953; Track 1 governing base FV Rs 237)

| Calculation | Value |
|---|---|
| Base Case Fair Value (Y3) | Rs 237 |
| Price for 25% CAGR = 237 / 1.953 | **Rs 121** |
| Price for 30% CAGR = 237 / 2.197 | Rs 108 |
| Margin-of-Safety price (20% below 25% entry) | **Rs 97** |
| Ideal entry range | **Rs 97 to Rs 121** |

CMP Rs 1,326 sits ~11x above the top of the entry zone. (Track 2 entry Rs 145, MoS Rs 116 - still ~9x below CMP.)

### 4F. Risk-Reward Asymmetry (Track 1)

| | Value |
|---|---|
| Bull target (Y3) | Rs 347 -> -73.8% |
| Base target (Y3) | Rs 237 -> -82.1% |
| Bear floor (Y3) | Rs 139 -> -89.5% |
| Upside(bull)/Downside(bear) magnitude ratio | 73.8 / 89.5 = **0.82x** (needs >=2x; **FAILS**) |

There is no positive upside at CMP; the entire distribution is capital loss. Asymmetry is inverted.

### 4G. Four-Pillar Exit Multiple Validation

| Validation Check | Result | Pass? |
|---|---|---|
| Y3 ROCE justifies ROCE base used & matches FTTCP? | Y3 base ~9.7%; Pillar 1 blend 7.36% is more conservative; RECOVERING verdict honoured | Yes |
| Y3 CFO/PAT justifies 0.80x cash multiplier? | Trajectory improving but cumulative -1.32x and receivables risk keep 0.80x defensible for the exit | Yes (conservative) |
| Primary catalyst fired by Y3 in base? | SDA invoicing (~Aug 2026), Dahej block earning - yes in base | Yes |
| Strategic premium justified (single-credit respected)? | +0x; recovery credited only in Pillar 1 | Yes |
| UA ordering correct - min(F x 1.25, Cap)? | UA not applied (all_met false); F2 = F; min(8.96, 35) | Yes |
| Would I buy a different stock at ~9x with these Y3 metrics? | Only at a price giving 25% CAGR - i.e. ~Rs 121, not Rs 1,326 | Consistent |

No check fails; exit PE stands at ~9x (Track 2) / ~7.3x (Track 1).

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP:** Rs 1,326 | **Market Cap:** Rs 3,103 Cr
- **FOUR-PILLAR EXIT PE:** ROCE Base 11.2x (FTTCP RECOVERING 40-60%; ROCE used 7.36% = 60/40 blend of 6.6% and FY28 8.5%) x Cash Mult 0.80x (INDETERMINATE leaning **structural**, no offset) = Quality Base **8.96x**; Growth Prem +0x (3a 0 / 3b 0 / 3c 0; EM 19.2, SOM 14.3%, no order book); Strategic +0x (single-credit: recovery in Pillar 1); Raw PE **8.96x**; UA applied **N** (all_met false); Sector Cap 35x (not binding, no quality uplift); **DESTINATION PE 8.5x-9.5x (mid 9.0x).**
- **RRM TRACK:** r = 15% (small-cap 14% + governance FLAG-PROMOTER); RRM 0.82; **RRM destination PE 7.0x-8.0x (mid 7.3x);** FV bear/base/bull Rs 139 / 237 / 347.
- **HURDLE RATIO:** Base 0.169, Bull 0.241 (both << 1.953) -> **STOP.**
- **METHODS:** P/E 50% / EV/EBITDA 30% / P/B 20%.
- **WEIGHTED FAIR VALUE (Y3):** Track 1 (governing) Bear 139 / Base **237** / Bull 347; Track 2 Bear 169 / Base 282 / Bull 408.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25):** **-44.1%** (Track 1); -40.0% (Track 2).
- **UPSIDE/DOWNSIDE:** 0.82x (fails >=2x; inverted).
- **ENTRY PRICE:** Rs 97 (MoS) to Rs 121 (25% CAGR entry). **MoS price Rs 97.**
- **DECISION: AVOID (on-valuation).** Hurdle Ratio STOP is decisive; independently, Gate 0 AVERAGE (default WATCHLIST) and Promoter CAUTION reinforce. Hardest verdict wins.
- **KEY ASSUMPTIONS THAT COULD CHANGE THE VALUATION:**
  - ▲ ROCE re-rates faster (FY28 >10.6% bull, sustained) -> Pillar 1 blend rises; but each +2% ROCE adds only ~+0.8x to destination PE. To reach even 20x destination needs ROCE ~25% (a different company).
  - ▲ Cash conversion turns structurally clean (rating confirms, receivables normalise, debtor days fall to <60) -> Pillar 2 could move 0.80x -> 1.00-1.15x, lifting destination ~15-40%. Still leaves a ~10-11x PE vs 73.75x current.
  - ▼ Jolva 4th slip / SDA delay -> bear path, ROCE stalls, destination toward 8x, EPS toward flat.
  - ▼ Receivables event (top-3 = 61%, zero ECL) -> cash multiplier toward 0.65x structural, destination toward 7x.
- **EXIT FRAMEWORK:** Target exit destination PE ~9x on normalised (recovered-ROCE) earnings; thesis-broken if ROCE fails to exit the 6-8% band by FY28 or FLAG-CASH resolves adverse; time stop 3 years; PE compression floor - at current 73.75x the compression IS the thesis risk.
- **ONE-LINE THESIS:** Avoiding Tatva Chintan at Rs 1,326 because even as EPS recovers from Rs 17.98 to a base Rs 30.65 over 3 years on the Dahej/SDA ramp, a ~7% ROCE below cost of capital and structural-leaning cash leakage earn only a four-pillar destination PE of ~9x (Track 1 RRM ~7.3x) versus a current 73.75x, so the Year 3 target of ~Rs 237 implies a -44% CAGR; Hurdle Ratio STOP. Key risk to any long: the de-rating is mathematical, not sentiment. Cash quality: INDETERMINATE leaning structural.

> **CHECKPOINT (framework close):** Valuation complete. Four-pillar exit PE ~7.0x-9.5x across tracks. Hurdle Ratio STOP. Entry price Rs 97-121. Decision: AVOID (on-valuation).

---

```yaml
stage: B11-valuation
company: "TATVA"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps:
  - "rating_wc_quote NOT FOUND (no rating PDF); Pillar 2 held at 0.80x, no offset - conservative"
  - "Peer medians (P/E, EV/EBITDA, P/B, ROCE) NOT COMPUTED per B10; peer-relative cross-check unavailable"
  - "FY26 facility-level utilization % NOT FOUND; ROCE 6.6% accepted from deliberation, not independently re-verified"
flags:
  - type: "FLAG-CASH"
    multiplier_applied: 0.80
    note: "INDETERMINATE leaning structural; 0.80x band, no growth offset; rating confirmation absent"
  - type: "SHARED-CATALYST"
    note: "Dahej commissioning underpins Pillar 1 forward ROCE and would-be Pillar 3a; 3a resolved +0x so no premium credited, flag stands for Role 3"
  - type: "FLAG-PROMOTER"
    note: "CAUTION cluster (GPCB closure, remuneration vs PAT, 2x CRISIL downgrade) priced into RRM r=15%"
  - type: "HURDLE-STOP"
    note: "AVOID-on-valuation; destination PE ~9x vs current PE 73.75x"
framework_versions: "Master v3.3 / Section 1B v3.3+v3.4 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 7.0, mid: 7.3, high: 8.0, r_used: 15, rrm: 0.82}
  track2_additive: {low: 8.5, mid: 9.0, high: 9.5}
  divergence_pct: 18.9
  governing_track: "Track 1 RRM - more conservative and prices governance (FLAG-PROMOTER) via r; sets entry zone"
pillar_detail:
  roce_used: 7.36
  roce_base: 11.2
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 0.80
  structural_or_growth: "INDETERMINATE leaning structural (conservative 0.80x, no offset)"
  growth_offset: 0
  growth_premium: 0
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 35
hurdle_ratio: {base: 0.169, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 139, base: 237, bull: 347}
  track2: {bear: 169, base: 282, bull: 408}
expected_cagr_prob_weighted: -44.1
entry_range: {low: 97, high: 121}
mos_price: 97
upside_downside_ratio: 0.82
decision: "AVOID (on-valuation)"
unresolved_inputs_used:
  - "rating_wc_quote NOT FOUND -> Pillar 2 held at 0.80x band, no growth offset (more conservative than rewarding an offset; not pushed to 0.65x absent rating confirmation)"
  - "Peer medians unavailable -> triangulation used absolute four-pillar/EV-EBITDA/P-B only, no peer-relative multiple"
  - "Y3 net debt estimated ~150 Cr (Y0 114.6 Cr + capex-funded creep, FCF turning positive by Y2-Y3) for EV/EBITDA equity bridge"
som_cagr_crosscheck: "consistent (base revenue CAGR 14.0% <= SOM-implied 14.3% 3yr; no cut required)"
one_line_thesis: "Avoiding TATVA at Rs 1,326: EPS recovers to base Rs 30.65 by FY29 but a ~7% ROCE below CoE and structural-leaning cash leakage earn only a ~9x (Track1 7.3x) four-pillar destination PE vs current 73.75x, implying -44% CAGR to a Rs 237 target; Hurdle Ratio STOP."
```

---

## NOTES FOR VERIFIER

1. **Framework version applied:** the injected Section 1B document carries v3.4 amendments (Pillar 3 decoupled 3a/3b/3c, two-tier hurdle, RRM percentage-point reading), which the task message explicitly directs and which supersede the wrapper's v3.3 label. framework_versions reflects "v3.3+v3.4".
2. **Tier assignment:** Tier A (all four Tier B quality gates fail - Gate 0 48, EM 19.2, promoter CAUTION, FLAG-CASH). Hurdle 25%, divisor 1.953.
3. **Single-credit enforced:** ROCE recovery credited only in Pillar 1 (60/40 blend). Strategic ROCE re-rating optionality withheld.
4. **SHARED CATALYST (Dahej):** feeds Pillar 1 forward ROCE; would have fed Pillar 3a but 3a resolved +0x on documented-evidence grounds (no committed-capex 📄 figure, no order book, SOM CAGR 14.3% < 20%). Flag retained for Role 3.
5. **UA:** not applied (all_met false); F2 row shown as F per contract.
6. **Governing track:** Track 1 (RRM), destination PE mid 7.3x, base FV Rs 237; divergence vs Track 2 is 18.9% (destination PE) / 16.0% (fair value), both >15%.
7. **Decision driver:** Hurdle Ratio STOP (destination PE ~9x vs current PE 73.75x). Even a hypothetical +2x strategic premium leaves HR(Bull) ~0.36 << 1.953. AVOID-on-valuation is robust to reasonable pillar sensitivities.
8. **Sensitivity to reach the 25% hurdle at CMP:** would require destination PE ~50-70x (a >25% ROCE, cash-elite business) - not this company at this ROCE. The overvaluation is structural, not a rounding artefact.
