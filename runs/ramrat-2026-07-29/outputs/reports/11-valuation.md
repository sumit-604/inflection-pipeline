# STAGE 11 — ROLE 1 MULTI-METHOD VALUATION (PIPELINE MODE)

**Company:** Ram Ratna Wires Ltd (RAMRAT) | **Run:** 2026-07-29 | **Model:** claude-opus-4-8
**Frameworks:** Master v3.3 / Section 1B v3.5.1 (consolidated Amendment 9) / FTTCP v1.2
**CMP:** Rs 454.40 | **Diluted shares:** ~9.33 Cr (PROVISIONAL, post 1:1 bonus 29-Dec-2025, unconfirmed) | **Market cap:** Rs 4,238.57 Cr | **Net debt:** Rs 611.27 Cr | **EV:** Rs 4,849.84 Cr

> INPUT DISCIPLINE NOTE: every input below is taken from B10-valinputs.yaml. Basis (SA = standalone / CN = consolidated) is declared on every figure. Forward-year EPS (FY27, FY28, FY29) is a PROJECTION, not sourced; the build and its assumptions are stated in full in Section 2. The operator-approved destination PE base (Track 2 additive 15.4x, FORWARD basis) is carried authoritatively; my independent Section 1B computation is shown and reconciled against it.

---

## SECTION 1A — METHOD SELECTION

RAMRAT is a capital-heavy, low-margin (5.26% EBITDA SA) copper winding-wire and copper-tube manufacturer with rising leverage (net debt/equity 1.043x SA), a confirmed FY26 negative-CFO working-capital breakdown (FLAG-CASH), and INDETERMINATE cash conversion. This is a standard operating business (four standard transitions), not a lender — no Pillar 2L carve-out.

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (Section 1B destination PE) | 60% | Standard profitable manufacturer; Section 1B is the sole exit-multiple authority. Earnings basis FORWARD (operator ruling). |
| SECONDARY | EV/EBITDA | 30% | Capital-heavy, rising leverage; normalises for capital structure. Cross-check only. |
| TERTIARY | P/B | 10% | Cyclical/asset-heavy sanity check (ROE 18.4% SA). |
| EXCLUDED | DCF | 0% | FCF NOT FOUND (no capex breakdown; B10 marks FCF N/A); INDETERMINATE cash conversion + negative FY26 CFO make terminal value unreliable. Excluding DCF is the conservative choice. |
| EXCLUDED | DDM | 0% | DPS Rs 2.50 flat despite +52% PAT CAGR; not a dividend story. |

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE (BOTH TRACKS)

### Pillar 1 — ROCE Base (continuous formula)

- FTTCP ROCE forward verdict: **RECOVERING (~55%)** (B10 cash/FTTCP + deliberation).
- Standard FTTCP RECOVERING (40-60%) row would use a 60/40 current/FY[Y+2] blend, which would RAISE ROCE and Pillar 1. **The deliberation OVERRIDES this: recovery NOT CREDITED, no forward blend** — the recovery is unconfirmed and sits behind the same FY26 inventory build that broke cash. This is MORE conservative than the framework default; I defer to it.
- **Pillar 1 normalization route (v3.5.1): NONE.** Route A fails (CWIP + capex advances 2.7% < 20% threshold). Route B N/A (no depression trough; ROCE at a 5-year high, verdict is not TEMPORARILY DEPRESSED). Statutory ROCE feeds Pillar 1 directly.
- ROCE used = **current 23.55% SA** (AUTHORITATIVE, AR Note 37 p.234, average capital employed; CN cross-check 23.3%).
- **Pillar 1 base = 0.5 x 23.55 + 7.5 = 19.275 → 19.3x**
- ROCE recovery credited via: **not-credited** (Strategic Premium ROCE re-rating route therefore BARRED — single-credit rule; also independently +0x below).

### Pillar 2 — Cash Conversion Multiplier

- Cash determination: **INDETERMINATE** (B10/deliberation). Mechanical test reads growth-induced, but the evidence does not close: inventory +108.1% YoY (233.68 → 486.09 Cr CN) vs ~40% revenue with ZERO write-downs and no management explanation; receivables +64.2% YoY; CFO/PAT -0.88x (SA) vs +3.14x FY25; CFO/EBITDA -0.38x (<0.7x breached); pre-tax CFO -51.02 Cr (SA) rules out tax-timing; CARE WC quote is FY25-dated and predates the reversal.
- Cash multiplier = **0.80x** (operator-approved) with the **growth offset WITHHELD** (+0.10x withheld) because the drag cannot be affirmed growth-induced. Per CLAUDE.md, INDETERMINATE cash cannot silently resolve favourably.
- **Quality-adjusted base = 19.3 x 0.80 = 15.44 → 15.4x**

### Pillar 3 — Growth Visibility (decoupled 3a/3b/3c, +6x cap)

- **3a Growth Visibility: +0x.** Qualifying tests: capex-embedded growth 14% (<15%, fails); no order book ≥1.0x revenue; SOM-implied CAGR 10.9-11.4% (<20%, fails); delivery grade B (1 test passes). Only 1 of 4 qualifies; +2x needs any two → **+0x**.
- **3b Moat Formation: +0x.** EM score 21/80 (< 25 threshold).
- **3c Duration: +0x.** No documented ≥2.5-year order book / annuity stream.
- **Pillar 3 total = +0x.**

### Strategic Premium

- Rare licence/monopoly: none. Brand pricing power: none (commodity, copper pass-through). ROCE re-rating optionality: BARRED (recovery not credited, but single-credit rule aside, no archetype support). Institutional turnaround backing: none.
- **Strategic Premium = +0x.**

### Undiscovered Alpha (Amendment 3 order)

- Qualifier 1 (listed ≥12m): TRUE. Qualifier 2 (Gate 0 ≥60 OR EM ≥25): FALSE (Gate 0 AVERAGE 40/80; EM 21). Qualifier 3 (FII+DII <3%): UNANCHORED (shareholding filing absent).
- all_met = FALSE → **UA NOT APPLIED (1.00x).**

### Four-Pillar Summary (Track 2 additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | 0.5 x 23.55 + 7.5 | 19.3x |
| B. Cash Multiplier (effective) | 0.80x, offset withheld | 0.80x |
| C. Quality-Adjusted Base | 19.3 x 0.80 | 15.4x |
| D. Growth Visibility (3a+3b+3c) | +0 +0 +0 | +0x |
| E. Strategic Premium | none | +0x |
| F. Raw Destination PE | 15.4 + 0 + 0 | 15.4x |
| F2. UA-Adjusted Raw PE | F x 1.00 (not qualified) | 15.4x |
| G. Sector Cap | Cables / Industrial products (NOT manifest 38x) | 25x |
| **H. Final Destination PE** | **min(F2, G) = min(15.4, 25)** | **15.4x** |

**Track 2 mechanical range (H ±7.5%): 14.25-16.56 → 14.0-16.5x.** Operator-approved range **14.5-16.5x**; I defer to the operator range. **Independent computation = 15.4x = operator-approved base. NO DIVERGENCE.**

### RRM Dual-Track Derivation (Track 1)

- Fundamental Base PE = quality-adjusted base 15.4x.
- Base r (small/micro-cap) = 14%; +1.5% for governance CONCERN (promoter-family board 5/10, Ankit Kedia 33%/40% attendance, R R Kabel cross-holding) and Moderate durability → **r = 15.5%** (within [9%,18%]).
- **RRM = 1 + (13.5 - 15.5) x 0.12 = 1 - 0.24 = 0.76** (percentage-point reading per Amendment 4.4; within bounds 0.70-1.60).
- **Track 1 destination PE = 15.4 x 0.76 = 11.70x** (range 11.0-12.5x). Matches deliberation 11.7x.

### Track divergence & governing track

- Track 2 additive 15.4x vs Track 1 RRM 11.7x → divergence **24.0%** (Track 1 is 24% below Track 2), well above the 15% materiality line.
- **Track fit:** for a governance-CONCERN, FLAG-CASH, low-margin capital-heavy commodity name, the RRM track (which prices governance and durability into the discount rate) is the more appropriate and more conservative read and would set the entry zone under the framework's conservative-governs rule. **The operator has elected Track 2 additive 15.4x as the approved destination base**, overriding conservative-governs. I carry BOTH through all fair values. **Decisively: the stock is AVOID-on-valuation on BOTH tracks, so the track election does not change the decision.**

**INTERIM CHECKPOINT (framework STOP point):** Methods selected (P/E primary). Four-pillar destination PE = **15.4x (Track 2, range 14.5-16.5x); RRM Track 1 = 11.7x (range 11.0-12.5x).** Earnings basis FORWARD. Current forward PE ~36.1x; current trailing PE ~39.2x. Hurdle Ratio computed in Section 4 → STOP (see below). Continuing.

---

## SECTION 2 — EARNINGS & CASH FLOW PROJECTIONS (SA basis, 9.33 Cr shares)

### FY27 forward EPS build (conservative — NO concall, NO guidance)

Trailing anchor: FY26 EPS **Rs 11.60 SA** (Q4 results p.7, restated for 1:1 bonus); PAT 108.32 Cr SA. Forward EPS is built off FY26, carrying the operator-mandated headwinds: (a) a FULL year of Bhiwadi depreciation (commissioned Jun-2025, so FY26 carried only ~9 months); (b) interest on borrowings that rose ~Rs 305 Cr to ~Rs 675 Cr; (c) Silvassa capex (~Rs 86 Cr) run-rate depreciation. Forward EPS is therefore NOT automatically above trailing — the growth is partly consumed by depreciation and interest.

**Base-case FY27 build:**
- Revenue: 5,076.10 x 1.11 = **5,634.5 Cr** (11% growth, aligned to SOM-implied 10.9-11.4%)
- EBITDA @ 5.3% = 298.6 Cr (FY26 5.26%; held ~flat — Q4 copper-tube revenue fell QoQ 361→347, winding-wire is copper pass-through)
- less Depreciation 45 Cr (FY26 35.09 + full-year Bhiwadi + Silvassa) → EBIT 253.6 Cr
- less Interest 95 Cr (FY26 80.72; full-year higher debt ~675 Cr) → PBT 158.6 Cr
- Tax @ 26% (FY26 effective 28.3%; normalised) → PAT 117.4 Cr
- **FY27 base EPS = 117.4 / 9.33 = Rs 12.58** (+8.4% over trailing)

INPUT UNRESOLVED: FY27 depreciation and interest. Conservative assumptions used: dep Rs 45 Cr, interest Rs 95 Cr (full-year Bhiwadi + higher debt), because no capex breakdown or debt schedule is sourced and the operator mandates a full-year drag.

### Scenario projections (EPS, Rs, SA)

| Year | Bear | Base | Bull |
|---|---|---|---|
| Revenue CAGR | 7% | 11% | 14% (= capex-embedded) |
| EBITDA margin | 4.8% | 5.3% | 5.6→6.0% |
| FY27 EPS | 9.18 | 12.58 | 14.84 |
| FY28 EPS | 10.54 | 15.19 | 19.64 |
| FY29 EPS | 12.17 | 18.08 | 25.24 |
| 3yr EPS CAGR (FY26→FY29) | 1.6% | 15.9% | 29.6% |

### 2C. Base-case complete projection

| Line | FY26 (Y0) | FY27 | FY28 | FY29 |
|---|---|---|---|---|
| Revenue (Cr) | 5,076.1 | 5,634.5 | 6,254.3 | 6,942.2 |
| EBITDA (Cr) | 266.9 | 298.6 | 331.5 | 367.9 |
| EBITDA margin | 5.26% | 5.30% | 5.30% | 5.30% |
| PAT (Cr) | 108.3 | 117.4 | 141.7 | 168.7 |
| EPS (Rs) | 11.60 | 12.58 | 15.19 | 18.08 |
| Est. ROCE | 23.55% | ~21-22% | ~22% | ~22-23% |

### 2D. Sanity checks

| Check | Result | Pass |
|---|---|---|
| Revenue growth within capacity? | Base 11% < physical capacity headroom (36k MTPA tube / 41.4k MTPA wire SUFFICIENT) | ✔ |
| Margins require the unprecedented? | Base holds 5.3% (near FY26); no expansion assumed | ✔ |
| ROCE stays >15%? | Yes, ~21-23% | ✔ |
| FCF funds growth without excess new debt? | UNKNOWN — FCF NOT FOUND; FY26 CFO negative. Conservatively assume debt stays elevated | ✘ (flag) |
| EPS growth operational, not engineered? | Yes; but FY27 partly consumed by dep+interest | ✔ |
| Year-3 ROCE consistent with FTTCP verdict used? | Pillar 1 used current 23.55% (no forward credit); Year-3 ~22-23% consistent | ✔ |
| SOM cross-check | Base 11% vs SOM 10.9-11.4% → **CONSISTENT**; Bull 14% = capex-embedded ceiling (exceeds SOM, flagged, bull-only) | ✔/flag |

**INTERIM CHECKPOINT:** Projections built. FY27 forward EPS Rs 12.58 (base). Continuing.

---

## SECTION 3 — APPLY VALUATION METHODS

### PRIMARY: P/E (Section 1B destination PE, both tracks)

**3-year target (exit end FY29) = FY29 EPS x Destination PE mid.** Destination PE applied on the FORWARD basis (a one-year-forward exit multiple).

| | Bear EPS 12.17 | Base EPS 18.08 | Bull EPS 25.24 |
|---|---|---|---|
| **Track 2 @ 15.4x** | Rs 187.4 → 🔴 -25.6% | Rs 278.4 → 🔴 -15.1% | Rs 388.7 → 🔴 -5.1% |
| **Track 1 @ 11.7x** | Rs 142.4 → 🔴 -32.1% | Rs 211.5 → 🔴 -22.5% | Rs 295.3 → 🔴 -13.4% |

CAGR measured from CMP Rs 454.40. **Every one of the six cells is a negative return.** The stock trades ABOVE even the bull-case Track 2 fair value.

### SECONDARY: EV/EBITDA cross-check

Destination EV/EBITDA ≈ 0.65 x destination PE ≈ 15.4 x 0.65 ≈ **10x** (generous for a 5% margin commodity manufacturer; peers trade ~8-10x). FY29 base EBITDA 367.9 Cr x 9x = EV 3,311 Cr; less est. net debt ~500 Cr = equity 2,811 Cr / 9.33 = **Rs 301** — consistent with the P/E base fair value (Rs 278, Track 2) and well below CMP. Confirms overvaluation.

### TERTIARY: P/B cross-check

Theoretical P/B = ROE / CoE = 18.4% / 14% = **1.31x**. BVPS Rs 63.02 x 1.31 = **Rs 82.7** current fair; even growing book to ~Rs 100 by FY29 gives ~Rs 131 at 1.31x. Deeply below CMP. Cross-check confirms.

### Method-wise fair value (FY29, Rs)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E Track 2 (primary) | 60% | 187.4 | 278.4 | 388.7 |
| EV/EBITDA | 30% | ~205 | ~301 | ~410 |
| P/B | 10% | ~110 | ~131 | ~160 |

**INTERIM CHECKPOINT:** All methods applied; all point below CMP. Continuing.

---

## SECTION 4 — TRIANGULATION, ENTRY & VERDICT

### 4A. Triangulated fair value (Year 3 = FY29)

Primary track carried is the operator-approved **Track 2 additive 15.4x**; Track 1 RRM 11.7x shown alongside.

| Track | Bear | Base | Bull |
|---|---|---|---|
| **Track 2 (additive, approved)** | Rs 187 | Rs 278 | Rs 389 |
| **Track 1 (RRM, conservative)** | Rs 142 | Rs 211 | Rs 295 |

### 4B. Methods agreement

All three methods and both tracks point the same direction (overvalued). Spread modest; P/E (Section 1B) is trusted most and is the framework authority.

### 4C. Return at current price (Track 2, primary)

| Scenario | FV (FY29) | CMP | 3yr CAGR | Meets 25%? |
|---|---|---|---|---|
| Bear | 187.4 | 454.40 | -25.6% | 🔴 |
| Base | 278.4 | 454.40 | -15.1% | 🔴 |
| Bull | 388.7 | 454.40 | -5.1% | 🔴 |

### 4D. Probability-weighted expected return (credibility grade B = Good → 25/50/25, sole source)

| Scenario | Prob | Track 2 CAGR | Weighted |
|---|---|---|---|
| Bear | 25% | -25.6% | -6.40% |
| Base | 50% | -15.1% | -7.55% |
| Bull | 25% | -5.1% | -1.28% |
| **Expected CAGR (Track 2)** | 100% | | **-15.2%** |

Track 1 (RRM) expected CAGR = **-22.6%** (bear -32.1 / base -22.5 / bull -13.4). Both tracks: deeply negative expected return at CMP.

### 4E. Hurdle Ratio (Tier A — hurdle 25%, threshold 1.953)

**Tier assignment:** FII+DII UNANCHORED → the UA institutional-absence test cannot be affirmed → **default Tier A (25%)** per Amendment 4.3. Gate 0 AVERAGE and EM 21 also fail Tier B's quality gates, so Tier A stands regardless.

**HR = (1 + EPS CAGR)³ x (Destination PE mid ÷ Current PE).** Earnings basis FORWARD → current PE = forward PE on FY27 EPS.

- Current forward PE = 454.40 / 12.58 = **36.1x**
- Base EPS CAGR 15.9% → (1.159)³ = 1.557
- **HR(base, Track 2) = 1.557 x (15.4 / 36.1) = 0.66** → FAIL
- HR(base, Track 1) = 1.557 x (11.7 / 36.1) = 0.50 → FAIL
- Bull EPS CAGR 29.6% (usable, credibility B) → (1.296)³ = 2.177
- **HR(bull, Track 2) = 2.177 x (15.4 / 36.1) = 0.93** → FAIL

**Trailing cross-check:** current trailing PE = 454.40 / 11.60 = 39.2x. HR(base, Track 2) = 1.557 x (15.4/39.2) = **0.61** → FAIL.

**HURDLE RATIO VERDICT = STOP** — bull case fails (HR 0.93 < 1.953). A ~36x forward / ~39x trailing entry multiple de-rating to a 15.4x earned destination PE cannot deliver 25% CAGR even on bull-case earnings. Per the framework, remaining sections are completed for the record and the verdict card reads AVOID-on-valuation.

### 4F. Entry price & margin of safety

Entry (25% CAGR, Tier A divisor 1.953) on the operator-approved Track 2 base fair value:
- Track 2 base FV 278.4 / 1.953 = **Rs 142.5** (band across destination PE range 14.5-16.5x: Rs 134 to Rs 153).
- Track 1 (conservative) entry = 211.5 / 1.953 = **Rs 108.3**.
- **Entry range (Track 2, approved): Rs 134-153.**
- **MoS price (20% below the 25% CAGR entry): 142.5 x 0.80 = Rs 114.**

CMP Rs 454.40 is ~3.0x the entry range and ~4.0x the MoS price.

### 4G. Risk-reward asymmetry

Base-case fair value (Rs 278) is BELOW CMP → no upside at current price. Bear floor Rs 187 → -59% downside. **Upside/downside ratio at CMP = 0.0 (no positive upside; fails the ≥2x test decisively).**

### 4H. Four-Pillar validation

| Check | Result | Pass |
|---|---|---|
| Year-3 ROCE justifies ROCE base (matches FTTCP)? | ~22-23% vs 23.55% used, recovery not credited | ✔ |
| Year-3 CFO/PAT justifies 0.80x cash multiplier? | UNRESOLVED (INDETERMINATE); 0.80x with offset withheld is the conservative floor | ✔ (conservative) |
| Primary catalyst fired by Year 3 (base)? | Bhiwadi ramp assumed; SHARED CATALYST flagged | flag |
| Strategic premium justified at Year 3 (single-credit)? | +0x, none; single-credit respected | ✔ |
| UA ordering correct — min(F x 1.25, Cap)? | UA not applied; H = min(15.4, 25) | ✔ |
| Would you buy this quality at 15.4x? | Only far below CMP; not at Rs 454 | n/a |

---

## VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP Rs 454.40 | Market cap Rs 4,238.57 Cr** (both PROVISIONAL on unconfirmed post-bonus 9.33 Cr share count)
- **FOUR-PILLAR EXIT PE:** ROCE base 19.3x (FTTCP RECOVERING ~55%, recovery NOT credited, ROCE used 23.55% current, normalization route NONE) → Cash mult 0.80x (INDETERMINATE, growth offset withheld) → Quality base 15.4x → Growth +0x (EM 21, 3a/3b/3c all 0) → Strategic +0x → Raw 15.4x → UA not applied → Sector cap 25x (Cables/Industrial, supersedes manifest 38x) → **DESTINATION PE 15.4x (range 14.5-16.5x, operator-approved).**
- **RRM TRACK:** r 15.5%, RRM 0.76 → **Track 1 destination 11.7x (range 11.0-12.5x).** Divergence 24% (>15%); RRM is the more conservative/appropriate read but operator elected Track 2; decision is AVOID on both.
- **EARNINGS BASIS: FORWARD** (FY27 EPS Rs 12.58 base; trailing cross-check FY26 EPS Rs 11.60).
- **HURDLE RATIO: 0.66 base / 0.93 bull (Track 2, forward) → STOP.** (Trailing cross-check 0.61.)
- **METHODS:** P/E 60% / EV/EBITDA 30% / P/B 10%; DCF excluded (FCF NOT FOUND, INDETERMINATE cash).
- **WEIGHTED FAIR VALUE (FY29):** Track 2 — Bear 187 / Base 278 / Bull 389. Track 1 — Bear 142 / Base 211 / Bull 295.
- **EXPECTED CAGR (prob-weighted, grade B 25/50/25):** Track 2 **-15.2%**; Track 1 -22.6%.
- **UPSIDE/DOWNSIDE: 0.0x** (no upside at CMP).
- **ENTRY RANGE Rs 134-153 (Track 2) | MoS PRICE Rs 114.** CMP is ~3-4x these levels.
- **DECISION: AVOID (on-valuation).** The stock fails the 25% hurdle at current price on both tracks and even on bull earnings; fair value sits below CMP in every scenario.
- **KEY ASSUMPTIONS THAT COULD CHANGE IT:** ▲ Cash conversion resolving to genuinely growth-induced (Q1 FY27 CFO print + inventory unwind + management explanation) would restore the +0.10x offset and lift the cash multiplier toward 0.90-1.00x, raising Pillar 1-2 base toward ~17-19x — still far below the ~36x forward entry PE. ▲ FTTCP recovery confirming in reported numbers would credit Pillar 1 midpoint ROCE. ▼ Overcapacity race (Vidya, Bhagyanagar, Adani, Hindalco) compressing margins below 4.8% pushes bear fair value under Rs 180. None of these plausibly close a ~3x valuation gap.
- **EXIT/RE-ENGAGE FRAMEWORK:** re-engage only near the Rs 134-153 entry zone AND with the FY26 cash reversal explained/reversed (Q1 FY27 CFO positive, inventory days normalising). Price entering the zone because a thesis-broken trigger fired is a withdrawn zone.
- **SHARED CATALYST: YES (Bhiwadi)** — carried for Role 3 stress-test; single point of failure behind both any forward ROCE and the FY26 inventory build.
- **ONE-LINE THESIS:** Ram Ratna Wires at Rs 454 trades at ~36x forward / ~39x trailing against a four-pillar destination PE of only 15.4x (ROCE 23.55%, cash 0.80x INDETERMINATE, EM 21, sector cap 25x); even bull-case FY29 EPS of Rs 25 at 15.4x gives Rs 389, a negative return from here, so the name is AVOID-on-valuation until price reaches the Rs 134-153 entry zone and the FY26 cash reversal is explained. Cash quality: INDETERMINATE.

**Valuation complete. Four-pillar exit PE 15.4x (Track 2) / 11.7x (Track 1). Hurdle Ratio STOP. Entry Rs 134-153; MoS Rs 114. Decision: AVOID (on-valuation).**

---

```yaml
stage: B11-valuation
company: "RAMRAT"
run_date: "2026-07-29"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Diluted share count post 1:1 bonus (29-Dec-2025) ~9.33 Cr unconfirmed; EPS and market cap PROVISIONAL"
  - "FY27-FY29 EPS are projections (no concall, no guidance); build stated in Section 2"
  - "Capex/FCF NOT FOUND; DCF excluded"
  - "FII+DII shareholding unanchored; UA Qualifier 3 cannot be tested; Tier defaults to A"
  - "FY27 depreciation/interest estimated (dep Rs 45 Cr, interest Rs 95 Cr) under operator full-year-drag mandate"
flags:
  - "FLAG-CASH: INDETERMINATE cash conversion; multiplier 0.80x APPLIED, growth offset +0.10x WITHHELD; caps quality at PROCEED WITH CAVEATS per CLAUDE.md"
  - "SHARED-CATALYST: YES (Bhiwadi) — carried for Role 3 stress-test"
  - "PROVISIONAL SHARE COUNT: 9.33 Cr post-bonus unconfirmed; all per-share figures provisional"
  - "GOVERNANCE CONCERN priced into RRM via r=15.5% (Track 1)"
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "forward"
exit_pe_base_approved: "15.4x (Track 2 additive, operator-approved over conservative Track 1 RRM 11.7x)"
destination_pe:
  track1_rrm: {low: 11.0, mid: 11.7, high: 12.5, r_used: 15.5, rrm: 0.76}
  track2_additive: {low: 14.5, mid: 15.4, high: 16.5}
  divergence_pct: 24.0
  governing_track: "Track 2 additive (operator override of conservative-governs); Track 1 RRM 11.7x is more conservative but decision is AVOID on both, so non-binding"
pillar_detail:
  roce_used: 23.55
  roce_base: 19.3
  roce_recovery_route: "not-credited"
  pillar1_normalization_route: "none"
  cash_multiplier: 0.80
  structural_or_growth: "INDETERMINATE (conservative 0.80x, offset withheld)"
  growth_offset: 0.0
  growth_premium: 0.0
  strategic_premium: 0.0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 0.66, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 142, base: 211, bull: 295}
  track2: {bear: 187, base: 278, bull: 389}
expected_cagr_prob_weighted: -15.2
entry_range: {low: 134, high: 153}
mos_price: 114
upside_downside_ratio: 0.0
decision: "AVOID (on-valuation)"
unresolved_inputs_used:
  - "Share count 9.33 Cr (provisional post-bonus) — used as given, flagged provisional"
  - "FY27 EPS Rs 12.58 base — conservative projection with full-year Bhiwadi dep + higher interest"
  - "FY27 depreciation Rs 45 Cr / interest Rs 95 Cr — conservative estimates (no schedule sourced)"
  - "FCF NOT FOUND — DCF excluded (conservative)"
  - "FII+DII unanchored — UA not applied; Tier A default"
som_cagr_crosscheck: "consistent (base 11% within SOM-implied 10.9-11.4%; bull 14% = capex-embedded ceiling, flagged bull-only)"
one_line_thesis: "RAMRAT at Rs 454 trades ~36x forward vs a 15.4x four-pillar destination PE; even bull FY29 EPS at 15.4x gives Rs 389 (negative return from CMP), so AVOID-on-valuation until Rs 134-153 with the FY26 cash reversal explained; cash quality INDETERMINATE."
```
