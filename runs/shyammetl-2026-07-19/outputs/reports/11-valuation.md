# STAGE 11: ROLE 1 MULTI-MODAL VALUATION (PIPELINE MODE)
## Shyam Metalics & Energy Limited (SHYAMMETL)
**Run Date:** 2026-07-19 | **Model:** claude-opus-4-8 | **Status:** complete
**Frameworks:** Master v3.3 (Role 1 + Section 1B) / Section 1B v3.5.1 Reconciliation (Pillar 1 normalization) / Section 1B v3.3 Amendments / FTTCP v1.2

> PIPELINE MODE: all STOP gates are written as interim checkpoints, then execution continues in one pass. Every input is drawn only from the B10 table / B10 YAML. Operator deliberation rulings carried on B10 are applied, not re-derived.

---

## OPERATOR-AUTHORITATIVE INPUTS APPLIED (from B10 / fttcp-deliberation, NON-NEGOTIABLE)

| Input | Ruling | Applied |
|---|---|---|
| Pillar 1 ROCE forward verdict | RECOVERING at 40-60% probability | Sole Pillar 1 authority |
| Pillar 1 normalization route | Route A FAILS (CWIP 106.47cr = 0.85% of CE 12,527.88cr, < 20%); Route B candidate | Route B applied (see worksheet) |
| ROCE recovery credited via | Pillar 1 only; Strategic Premium ROCE re-rating BARRED | Single credit enforced |
| Cash determination | GROWTH-INDUCED; Pillar 2 multiplier 1.0x provisional | Applied 1.0x |
| Pillar 3 | ~+3x (3a +2x, 3b +1x, 3c 0), within +6x cap | Applied +3x |
| UA multiplier | NOT APPLIED (FII+DII ~16.7% > 3% ceiling) | ua_qualifiers.all_met = false |
| Return hurdle | Tier A, 25% (divisor 1.953) | Applied |
| Sector cap | 20x (commodity-cyclical integrated steel); manifest "Pharma/CDMO" 38x OVERRIDDEN | 20x used; 38x never used |
| Approved destination (exit) PE | 20x FLAT (operator elects sector ceiling over computed build) | Applied to fair values |
| Earnings basis | FORWARD (one-year-forward, FY27E EPS) | 20x applied to FY27E EPS |
| Shared catalyst | YES (capex commissioning drives Pillar 1 ROCE AND Pillar 3a) | Flagged for Role 3 |

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

Business model (B04): integrated metals producer, capital-heavy, commodity-cyclical. Net cash balance sheet (net cash Rs 20.39cr, B12a). FCF negative in capex phase (FY26 -613.68cr). This profile drives method choice.

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (forward, Four-Pillar destination) | 60% | Operator-approved forward earnings basis; Section 1B is sole exit-multiple authority; earnings positive and the four-pillar destination governs the exit multiple |
| SECONDARY | EV/EBITDA | 25% | Capital-heavy manufacturer with varying leverage across the cycle; standard for integrated steel; cross-checks the 20x forward PE |
| TERTIARY | P/B | 15% | Cyclical at mid-cycle; book anchors a floor when ROCE/ROE are depressed; theoretical P/B = ROE/CoE cross-check |
| NOT USED | DCF | 0% | FCF negative in capex phase (FY26 -613.68cr); cyclical + heavy near-term capex make terminal value dominate and unreliable. Excluded per Master v3.3 DCF suitability rule. |

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE FRAMEWORK v3.3 (with v3.5.1 Pillar 1 normalization)

### Pillar 1 — ROCE Base Multiple (continuous formula, FTTCP verdict as sole authority)

**Normalization route selection (Section 1B v3.5.1 consolidated Amendment 9):**

- Route A test (denominator fix): (CWIP + idle raised capital + capex advances) > 20% of capital employed? CWIP = 106.47cr (Mar-26; B10 YAML, results Q4 FY26 blocks 6c) vs capital employed 12,527.88cr (B10 unresolved / B12a proxy) = **0.85%**. **Route A FAILS** (far under 20%; no material idle raised capital or capex-advance block anchored).
- Route B test (numerator fix): denominator clean AND FTTCP verdict TEMPORARILY DEPRESSED / RECOVERING with 📄-evidenced pre-depression ROCE history? Backward ROCE verdict = TEMPORARILY DEPRESSED (fttcp-deliberation); forward = RECOVERING 40-60%. Pre-depression history: ROCE 23.4% FY18 anchored (B01 gate0; B10 "ROCE 2-Year Trend: DECLINING 23.4% FY18 → 13.21% FY26"); pre-cycle median ~20% (FY18-21 band, per fttcp-deliberation, capped at the evidenced level). Named, dated unwind catalyst = the documented commissioning schedule (Aluminium FRP end-Sep-2026; Wagon Phase-I Sep-2026; DRI 0.5 MTPA by Mar-2027 — B07 catalysts_12m). **Route B conditions HOLD.**
- **Pillar 1 normalization route: B — Pre-Cycle Normalized ROCE.**

**Worksheet line (v3.5.1):** Route B. Pre-cycle median 20% (source: AR/screener history, FY18-21 band; FY18 23.4% firmly anchored in B10, capped at 20% ≤ evidenced print — no extrapolation above what the company printed). Unwind catalyst: capex commissioning schedule (Aluminium FRP end-Sep-2026, Wagon Phase-I Sep-2026, DRI 0.5 MTPA by Mar-2027; 📄 B07). Blend weight 60% current / 40% anchor (RECOVERING 40-60% band, v3.5.1). Self-withdrawal date: next quarterly refresh after Mar-2027 if FY27 ROCE print does not turn up (+1 quarter grace).

> ANCHORING NOTE: only FY18 ROCE (23.4%) is a firmly anchored single print in B10; the full FY18-21 series is not individually anchored. The ~20% pre-cycle median is the operator-authoritative figure carried on the deliberation and is capped below the one evidenced print (23.4%). It is applied as the Route B anchor per the authoritative ruling. Had the anchor been unavailable, the fallback (standard FTTCP 60/40 current/FY[Y+2]) would apply; it is not needed here.

**Blended Pillar 1 ROCE** = 0.60 × current 13.21% + 0.40 × pre-cycle anchor 20% = 7.926 + 8.000 = **15.93%**.

**ROCE Base Multiple** = 0.5 × 15.926 + 7.5 = 7.963 + 7.5 = **15.46x → 15.5x** (floor 9x / cap 24x not binding).

- FTTCP ROCE forward verdict: RECOVERING 40-60%
- ROCE used for base: 15.93% (Route B 60/40 blend)
- ROCE Base Multiple: **15.5x**
- **ROCE recovery credited via: Pillar 1 (Route B blend). Strategic Premium ROCE re-rating BARRED (single-credit rule).**

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT (9-yr): 1.35x (B01); Latest FY26 CFO/PAT: 1.89x (2,023.56/1,070.24). FCF positive? NO — FY26 FCF -613.68cr (capex phase).
- Determination (operator, from B10, not re-litigated): **GROWTH-INDUCED** cash drag (consolidated conversion strong ~1.9x; FCF negative purely from capex 2,637.24cr). CRISIL: "Working capital management has been prudent... low receivables of 15-30 days" (ratings.pdf p.2, Nov-05-2025). Not structural.
- Operator-set multiplier: **1.0x provisional** (B10 fttcp_pillar_inputs). Applied as given. Growth offset: 0 (operator delivered the 1.0x determination directly; no additional offset stacked — single-credit discipline).
- **Quality-Adjusted Base = 15.5x × 1.0x = 15.5x.**

### Pillar 3 — Growth Visibility Premium (decoupled 3a/3b/3c, +6x cap)

- 3a Growth Visibility: **+2x** — capex-embedded growth 150% (B07), delivery grade B (B05). (Amendment 4.1: two+ qualifiers, grade B.)
- 3b Moat Formation: **+1x** — EM 30 STRENGTHENING (B07); catalyst 0-12m; evidence mixed (19 documented / 10 claim / 6 inference).
- 3c Duration: **+0x** — no 📄 order book / contracted revenue tenor ≥2.5yr documented.
- **Pillar 3 total: +3x** (within +6x cap). **SHARED CATALYST: YES** — the capex commissioning schedule drives both the Pillar 1 ROCE recovery and Pillar 3a. Flagged for Role 3 (single point of failure).

### Strategic Premium

- ROCE re-rating optionality route BARRED (recovery already credited in Pillar 1 — single credit). No rare licence/regulatory monopoly (safeguard duty provisional, PLI lapsed — B05/B07). **Strategic Premium: +0x.**

### Undiscovered Alpha Multiplier

- Qualifiers (all three required): listed ≥12m ✓; Gate 0 ≥60 OR EM ≥25 (EM 30 ✓); FII+DII <3% ✗ (~16.7%, exceeds 3% ceiling). all_met = **false**. **UA NOT applied.**

### Four-Pillar Summary — Track 2 (Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 15.93% (Route B) → 0.5×15.93+7.5 | 15.5x |
| B. Cash Multiplier (effective) | 1.0x + offset 0 | 1.0x |
| C. Quality-Adjusted Base | 15.5 × 1.0 | 15.5x |
| D. Growth Visibility Premium | 3a +2 / 3b +1 / 3c 0 | +3x |
| E. Strategic Premium | barred (single credit) | +0x |
| F. Raw Destination PE | 15.5 + 3 + 0 | **18.5x** |
| F2. UA-Adjusted Raw PE | UA not qualified → F unchanged | 18.5x |
| G. Sector Cap | commodity-cyclical integrated steel | 20x |
| **H. Additive Destination PE** | **min(18.5, 20)** | **18.5x** |

**Track 2 (Additive) Destination Range: 18.5x ±7.5% → 17.0x to 20.0x.**

### RRM Dual-Track Derivation — Track 1

- Base r: mid-cap (mcap 28,541cr) → 13%. Adjustments: governance penalty +1.25% (promoter CONCERN — live ED-PMLA attachment on SSPL Rs 159.51cr 15-Apr-2026; accounting quality 5/10 B02; circular related-party structure); durability +0.5% (cost leadership durable but commodity-cyclical, regulatory tailwinds at-risk). **r = 14.75%** (bounded [9%,18%] ✓).
- RRM = 1 + (13.5 − 14.75) × 0.12 = 1 − 0.15 = **0.85** (bounds ×0.70–×1.60 ✓; percentage-point reading per Amendment 4.4).
- Fundamental Base PE = QAB + growth premium (strategic 0) = 15.5 + 3 = 18.5x.
- **Track 1 (RRM) Destination PE = 18.5 × 0.85 = 15.7x** (cap 20x not binding).

**Track 1 (RRM) Destination Range: 15.7x ±7.5% → 14.5x to 17.0x.**

### Dual-Track reconciliation and operator override

| Track | Destination PE (mid) | Range |
|---|---|---|
| Track 1 (RRM) | 15.7x | 14.5x – 17.0x |
| Track 2 (Additive) | 18.5x | 17.0x – 20.0x |
| Divergence | (18.5−15.7)/18.5 = **15.1%** (>15%) | RRM is more conservative; fits a governance-flagged commodity cyclical, so RRM would govern the entry zone on a self-derived basis |
| **OPERATOR-APPROVED (applied)** | **20x FLAT** | Authoritative; supersedes both tracks |

> DIVERGENCE FLAG (reported plainly per pipeline override rule): the operator-approved 20x exceeds BOTH computed tracks (additive 18.5x, RRM 15.7x). The operator elected the sector-cap ceiling, a richer exit multiple than the pillar build supports. Per the pipeline override rule the fair values are computed on the operator-approved 20x, NOT overwritten with a self-derived multiple. The material consequence: even on the generous 20x the Hurdle Ratio STOPS (below), and it STOPS harder on both self-derived tracks — the conclusion is robust to the destination choice.

### Destination PE Sanity Check — Hurdle Ratio (Tier A, threshold 1.953)

- Current PE = CMP 1022 / trailing FY26 diluted EPS 38.70 = **26.41x**.
- Destination PE mid (applied) = 20x → Destination/Current = 20/26.41 = **0.757** (a de-rating).
- Base EPS CAGR (3yr) = 18% (see Section 2). Bull EPS CAGR = 30% (grade B permits bull in the HR check).

| Row | Calculation | HR | vs 1.953 |
|---|---|---|---|
| HR(Base) | (1.18)³ × 0.757 = 1.643 × 0.757 | **1.24** | FAIL |
| HR(Bull) | (1.30)³ × 0.757 = 2.197 × 0.757 | **1.66** | FAIL |

**HR verdict = STOP.** HR(Bull) < 1.953 → 25% CAGR is infeasible even on bull-case earnings at the operator-approved 20x. (For the record: HR STOPS on Track 2 additive 18.5x — bull 1.54 — and on Track 1 RRM 15.7x — bull 1.31 — as well. STOP is robust across all three destination assumptions.)

**Would I personally pay 20x forward for this quality of business?** No — a commodity-cyclical integrated steel producer with ROCE 13.21%, ROE 9.52%, accounting quality 5/10, and a live ED-PMLA attachment does not warrant 20x forward; the operator election is the ceiling, not a fundamentals-earned multiple.

> 🛑 CHECKPOINT (Section 1): Methods selected. Four-pillar destination — Additive 17.0–20.0x (mid 18.5x), RRM 14.5–17.0x (mid 15.7x). Operator-approved applied destination 20x. Current PE 26.4x. Hurdle Ratio → STOP. Continuing.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS

### 2A. Forward EPS derivation (FORWARD basis — FY27E)

FY27E EPS is NOT quantified by management (B10 input gap). Derived transparently from FY26 base: PAT owners 1,070.24cr, diluted EPS 38.70 (audited, results Q4 FY26 p.10), shares 27.92cr, minimal dilution assumed.

Guidance context: medium-term 15-20% revenue CAGR repeated Q2/Q3; FY27-only raised to ~30% in Q4 call, **unreconciled** (B05, flagged). Grade B credibility. Historical PAT CAGR (FY25-26) 17.96%; 3-yr revenue CAGR 22.12%.

| Scenario | EPS growth logic | FY27 EPS growth | FY27E EPS |
|---|---|---|---|
| Bear | Capex/commissioning slip + margin compression; below historical | 12% | 38.70 × 1.12 = **43.34** |
| **Base (used)** | Historical PAT CAGR (~18%), discounts the unreconciled 30% guide to grade-B reality; modest margin expansion offset by capex-driven depreciation/interest | **18%** | 38.70 × 1.18 = **45.67** |
| Bull | Management FY27 revenue guide (~30%) at face value (grade B permits); operating leverage | 30% | 38.70 × 1.30 = **50.31** |

**Base FY27E EPS used = 45.67.** (Note: the FTTCP honest-consequence line used a more aggressive ~25-30% central figure ~48-50; that maps to my bull case, not base. Conservative-bias base = historical PAT CAGR.)

### 2B. Profitability / margin

EBITDA margin FY26 13.67%; guided +200-300bps improvement (B05). Base holds ~14% (commissioning ramp offsets mix); bull ~15-16%; bear ~12.5% (cyclical compression). Depreciation rising as capex commissions (FY26 D&A 248.51cr low relative to gross block — expect step-up FY27+). Tax ~25%. Dilution ~nil.

### 2C. Projection summary (3-year illustrative, BASE)

| Line | FY26 (Yr0) | FY27E (Yr1) | FY28E (Yr2) | FY29E (Yr3) |
|---|---|---|---|---|
| Revenue (Rs cr) | 18,552 | ~21,900 | ~25,800 | ~30,400 |
| EBITDA margin | 13.67% | ~14% | ~14% | ~14.5% |
| PAT owners (Rs cr) | 1,070 | ~1,263 | ~1,490 | ~1,760 |
| EPS (diluted) | 38.70 | 45.67 | ~53.9 | ~63.6 |
| Est. ROCE | 13.21% | ~14-15% | ~15-16% | ~16-17% |

(Base assumes ~18% EPS CAGR sustained; revenue ~16-18% with modest leverage.)

### 2D. Projection sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue growth faster than capacity allows? | ~16-18% below actual 3yr 22%; capex commissioning supports | ✓ |
| Margins require something unprecedented? | ~14% within historical band (was 20.85% earlier cycle) | ✓ |
| ROCE stays above 15%? | Reaches ~15% only Yr2-3 in base; FY26 13.21% below 15% | ⚠ marginal |
| FCF funds growth without excessive new debt? | Net cash 20.39cr; capex-heavy so FCF negative near term, but CRISIL AA+/A1+ and strong CFO cushion | ⚠ growth-dependent |
| EPS growth operational not engineered? | B02 flags FY24 one-off tax 338.57cr + treasury-driven PBT; base excludes one-offs | ⚠ watch |
| Implied market-share gain realistic? | Base revenue ~16-18% vs SOM-implied 14.8% (3yr) — mild excess, cushioned by 22% actual | ✓ (flagged) |
| CFO/PAT trajectory consistent with Pillar 2 1.0x? | Consolidated CFO/PAT ~1.9x supports ≥1.0x | ✓ |
| **Yr3 ROCE consistent with FTTCP RECOVERING used in Pillar 1?** | Base Yr3 ROCE ~16-17% consistent with a RECOVERING (not FIRING) blend of 15.93% | ✓ |

**SOM cross-check:** base ~18% EPS growth maps to ~16-18% revenue growth vs SOM-implied 14.8% (3yr) / 12.7% (5yr). Mild excess, JUSTIFIED by actual 3-yr revenue CAGR of 22.12% (well above SOM) and the near-term commissioning schedule; flagged as above bottom-up SOM. Capacity-gap alert (B09: Rs 8,500cr gap between bottom-up SOM 33,815cr and mgmt FY31E 42,500cr) noted — base does NOT rely on the aggressive stainless ramp.

> 🛑 CHECKPOINT (Section 2): Projections built. FY27E EPS base 45.67 (bear 43.34 / bull 50.31). Continuing.

---

## SECTION 3: APPLY EACH VALUATION METHOD

### PRIMARY — P/E (FORWARD, operator-approved 20x on FY27E EPS)

Exit PE applied = **20x FLAT** (operator-approved; Section 1B sole authority; supersedes computed additive 18.5x / RRM 15.7x).

| Scenario | FY27E EPS | Fair value @ 20x | vs CMP 1022 |
|---|---|---|---|
| Bear | 43.34 | **867** | −15.2% |
| Base | 45.67 | **913** | −10.7% |
| Bull | 50.31 | **1,006** | −1.6% |

Every scenario, including bull, lands BELOW CMP 1022 → the stock trades above even its bull-case forward fair value. (This matches the FTTCP honest-consequence: "20x forward implies fair value ~960-1,000, around or below CMP 1,022.")

For the record — fair values on the self-derived tracks (more conservative):
- Track 1 (RRM 15.7x): bear 680 / base 717 / bull 790.
- Track 2 (Additive 18.5x): bear 802 / base 845 / bull 931.

### SECONDARY — EV/EBITDA (cross-check)

Current EV/EBITDA = 28,520.61 / 2,536.65 = **11.24x** — already rich for integrated steel (sector norm ~5-7x). A 20x forward PE implies EV/EBITDA ~11-12x, well above the sector's structural range. This divergence confirms the 20x forward multiple is generous and the current price embeds a full-recovery premium. Cross-check leans bearish.

### TERTIARY — P/B (cross-check)

BVPS 402.56; current P/B = 1022/402.56 = **2.54x**. Theoretical P/B = ROE/CoE = 9.52% / 14% = **0.68x** → book-anchored fair value ~274. Even normalizing ROE toward a recovered ~14-15% gives P/B ~1.0-1.1x → ~400-440. Current 2.54x P/B is well above the ROE-justified level; cross-check strongly bearish (cyclical trading above mid-cycle book multiple).

### Method-wise fair value summary (applied 20x for P/E)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E (fwd @20x) | 60% | 867 | 913 | 1,006 |
| EV/EBITDA | 25% | ~760 | ~840 | ~960 |
| P/B | 15% | ~300 | ~420 | ~520 |

> 🛑 CHECKPOINT (Section 3): All methods point below CMP. Continuing.

---

## SECTION 4: TRIANGULATION, ENTRY PRICE & FINAL VERDICT

### 4A. Triangulated fair value (weighted)

| | Bear | Base | Bull |
|---|---|---|---|
| P/E ×60% | 520 | 548 | 604 |
| EV/EBITDA ×25% | 190 | 210 | 240 |
| P/B ×15% | 45 | 63 | 78 |
| **Weighted FV** | **755** | **821** | **922** |

Note: the primary (P/E @20x) is the operator-designated basis; the weighted blend is shown for triangulation but the operator-approved P/E fair values (867/913/1,006) govern the decision fields below, per operator authority. Both point to the same conclusion (below CMP).

### 4B. Methods agreement

All three methods point the same direction (below CMP). Spread base 913 (P/E) to ~420 (P/B) is wide because P/B prices depressed ROE while P/E prices a recovery; P/E (forward, operator basis) is the most appropriate given the RECOVERING verdict. No method supports CMP 1022.

### 4C. Return expectation at current price (3-year, P/E @20x fair values as targets)

| Scenario | FV | CMP | 3yr CAGR | ≥25%? |
|---|---|---|---|---|
| Bear | 867 | 1022 | −5.3% | 🔴 |
| Base | 913 | 1022 | −3.7% | 🔴 |
| Bull | 1,006 | 1022 | −0.5% | 🔴 |

### 4D. Probability-weighted expected return (grade B → 25/50/25)

| Scenario | Prob | 3yr CAGR | Weighted |
|---|---|---|---|
| Bear | 25% | −5.3% | −1.33% |
| Base | 50% | −3.7% | −1.84% |
| Bull | 25% | −0.5% | −0.13% |
| **Expected CAGR** | 100% | | **−3.3%** |

### 4E. Entry price (Tier A, divisor 1.953)

| Calculation | Value |
|---|---|
| Base fair value | 913 |
| Entry (25% CAGR) = 913 / 1.953 | **468** |
| Entry (30% CAGR extra safety) = 913 / 2.197 | 416 |
| Entry range | **416 – 468** |
| MoS price (20% below 25% entry) = 468 × 0.80 | **374** |

CMP 1022 is ~2.2x the top of the entry range — no proximity to a buyable zone.

### 4F. Risk-reward asymmetry

| | Value |
|---|---|
| Bull target | 1,006 → +(−1.6%) i.e. no upside |
| Base target | 913 → −10.7% |
| Bear floor | 867 → −15.2% |
| Upside(base)/Downside(bear) | 10.7/15.2 = **0.7x** (base offers no upside; fails ≥2x) |

### 4G. Four-Pillar exit-multiple validation

| Check | Result | Pass? |
|---|---|---|
| Yr3 ROCE justifies the 15.93% Route B base and matches RECOVERING verdict? | Base Yr3 ~16-17% consistent | ✓ |
| Yr3 CFO/PAT justifies 1.0x cash multiplier? | Consolidated ~1.9x supports | ✓ |
| Primary catalyst fired by Yr3 (base)? | Commissioning FY27-29 — partial by Yr3 | ⚠ |
| Strategic premium justified? | 0x (single credit) — respected | ✓ |
| UA ordering min(F×1.25, cap)? | UA not qualified — correctly not applied | ✓ |
| Would I buy a different stock at 20x fwd with these Yr3 metrics? | No | ✗ |

Validation confirms the destination multiple is generous, not earned; the STOP holds.

### 4H. FINAL VALUATION VERDICT CARD

**Tier: A | Hurdle: 25%**

- **CMP:** Rs 1,022 | **Market Cap:** Rs 28,541 cr
- **FOUR-PILLAR EXIT PE:** ROCE Base 15.5x (Route B blended ROCE 15.93% = 60% current 13.21% / 40% pre-cycle 20%; FTTCP RECOVERING 40-60%; recovery credited via Pillar 1) × Cash Mult 1.0x (growth-induced) = QAB 15.5x; + Growth +3x (EM 30, catalyst 0-12m, mixed evidence; SHARED CATALYST) + Strategic +0x (barred) = Raw 18.5x; UA not applied; Sector Cap 20x. **Additive Destination 18.5x (17.0–20.0x).**
- **RRM TRACK:** r 14.75%, RRM 0.85 → **Destination 15.7x (14.5–17.0x).**
- **DIVERGENCE:** 15.1% (>15%); RRM more conservative. **OPERATOR-APPROVED APPLIED DESTINATION: 20x FLAT** (exceeds both computed tracks — flagged; valued on 20x per operator authority).
- **EARNINGS BASIS:** FORWARD, FY27E EPS. Base 45.67 (bear 43.34 / bull 50.31).
- **HURDLE RATIO:** Base 1.24, Bull 1.66 — both < 1.953 → **STOP** (25% CAGR infeasible even on bull earnings, even at the generous 20x).
- **FAIR VALUES (P/E @20x, applied):** Bear 867 / Base 913 / Bull 1,006 — all below CMP.
- **EXPECTED CAGR (prob-weighted, grade B):** −3.3%.
- **UPSIDE/DOWNSIDE:** 0.7x (fails ≥2x; no upside in any scenario).
- **ENTRY RANGE:** 416 – 468. **MoS PRICE:** 374.
- **DECISION: AVOID (on valuation and governance).** CMP 1022 sits above even the bull fair value 1,006; HR = STOP; independently, Gate 0 AVOID and Promoter CONCERN each force AVOID.

**Key assumptions that could change the valuation:**
- ▲ ROCE recovery prints faster/higher than the Route B 15.93% blend (Pillar 1 base rises) — but self-withdrawing if FY27 ROCE does not turn up.
- ▲ FY27 revenue actually delivers the ~30% guide (bull EPS 50.31) — still only reaches fair value ~1,006, at/below CMP.
- ▼ Commissioning slips (SHARED CATALYST fails) — hits Pillar 1 AND Pillar 3a simultaneously; both fair value and the ROCE base fall.
- ▼ ED-PMLA / CPCB outcomes crystallize as cash costs — governance discount widens, r rises, RRM destination falls further.

**Exit framework:** target exit — n/a (AVOID, not held). Thesis re-open (from AVOID) requires: FY27 ROCE print turning up toward pre-depression band AND cash conversion holding AND price entering 416-468 zone with no thesis-broken trigger fired (entry conjunction). Time stop / PE-compression floor: if held, thesis broken if forward PE re-rates below 15x with no ROCE turn.

**ONE-LINE THESIS (bearish):** Avoiding Shyam Metalics at Rs 1,022 because even at the operator-approved 20x forward (a multiple above the pillar build's 18.5x additive / 15.7x RRM), FY27E EPS of ~45.67 supports fair value ~913 (bull ~1,006), all below CMP, giving a −3.3% expected CAGR and a STOP Hurdle Ratio; key risk to any bull is the SHARED CATALYST commissioning schedule that drives both ROCE and growth; cash quality: growth-induced (1.0x).

> 🛑 Valuation complete. Four-pillar exit PE: additive 18.5x / RRM 15.7x, operator-applied 20x. Hurdle Ratio STOP. Entry 416-468 (MoS 374). Decision: AVOID (on valuation + governance).

---

```yaml
stage: B11-valuation
company: "SHYAMMETL"
run_date: "2026-07-19"
model: claude-opus-4-8
status: complete
input_gaps:
  - "FY27E EPS not quantified by management; derived from FY26 EPS 38.70 x stated growth (base 18% = historical PAT CAGR); bear 12% / bull 30%"
  - "Pre-cycle ROCE median ~20% is operator-authoritative (FY18-21 band); only FY18 23.4% firmly anchored in B10; 20% capped below the one evidenced print; Route B applied per ruling"
  - "Peer comparables for stainless/aluminium/nickel absent; EV/EBITDA and P/B cross-checks use sector norms and company book only"
  - "3-year PAT CAGR requires FY23 (not extracted); base growth anchored on 2-yr PAT CAGR 17.96% and 3-yr revenue CAGR 22.12%"
flags:
  - "FLAG-CASH: cash conversion GROWTH-INDUCED (not INDETERMINATE); Pillar 2 multiplier applied 1.0x provisional per operator; consolidated CFO/PAT ~1.9x, FY26 FCF -613.68cr from capex"
  - "SHARED CATALYST YES: capex commissioning schedule drives BOTH Pillar 1 ROCE recovery and Pillar 3a growth premium; single point of failure; Role 3 stress test required"
  - "OPERATOR 20x EXCEEDS COMPUTED TRACKS: applied destination 20x > additive 18.5x and RRM 15.7x; operator elected sector-cap ceiling; valued on 20x per override rule; HR STOPS even at 20x and harder on both self-derived tracks"
  - "Hurdle Ratio STOP: base 1.24, bull 1.66, both < 1.953; 25% CAGR infeasible even on bull earnings; stock above bull fair value"
  - "Gate 0 AVOID (Core 34/100) and Promoter CONCERN (live ED-PMLA attachment on SSPL Rs 159.51cr 15-Apr-2026; CPCB Rengali closure) each independently force AVOID"
  - "FY27 guidance escalated unreconciled (Q2/Q3 15-20% CAGR vs Q4 ~30% FY27-only); base discounts to grade-B reality"
  - "Route B self-withdrawal: if FY27 ROCE print does not turn up by Mar-2027 +1 quarter, pre-cycle anchor withdrawn and Pillar 1 reverts to statutory ROCE"
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "forward"
exit_pe_base_approved: "20x flat (operator-approved sector-cap ceiling; commodity-cyclical integrated steel; manifest Pharma/CDMO 38x overridden)"
destination_pe:
  track1_rrm: {low: 14.5, mid: 15.7, high: 17.0, r_used: 14.75, rrm: 0.85}
  track2_additive: {low: 17.0, mid: 18.5, high: 20.0}
  divergence_pct: 15.1
  governing_track: "RRM more conservative and fits a governance-flagged commodity cyclical; but operator-approved 20x (above both tracks) is authoritative and applied to fair values"
pillar_detail:
  roce_used: 15.93
  roce_base: 15.5
  roce_recovery_route: "pillar1-midpoint"
  pillar1_normalization_route: "B-pre-cycle"
  cash_multiplier: 1.0
  structural_or_growth: "growth-induced"
  growth_offset: 0
  growth_premium: 3
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 20
hurdle_ratio: {base: 1.24, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 867, base: 913, bull: 1006}
  track2: {bear: 867, base: 913, bull: 1006}
expected_cagr_prob_weighted: -3.3
entry_range: {low: 416, high: 468}
mos_price: 374
upside_downside_ratio: 0.7
decision: "AVOID (on valuation and governance; CMP above bull fair value, Hurdle Ratio STOP, Gate 0 AVOID, Promoter CONCERN)"
unresolved_inputs_used:
  - "FY27E EPS: conservative base growth 18% (historical PAT CAGR) applied to FY26 EPS 38.70; per Section 2A base rule (lower of discounted guidance or historical CAGR)"
  - "Pre-cycle ROCE anchor 20%: operator-authoritative FY18-21 median, capped below the single evidenced print FY18 23.4%; Route B applied per ruling"
  - "CoE/r 14.75%: mid-cap base 13% + governance 1.25% + durability 0.5% for RRM track"
som_cagr_crosscheck: "justified excess — base ~18% EPS maps to ~16-18% revenue vs SOM-implied 14.8% (3yr); justified by actual 22.12% historical revenue CAGR and near-term commissioning; flagged as above bottom-up SOM; base does not rely on aggressive stainless ramp"
one_line_thesis: "Avoid SHYAMMETL at Rs 1,022: even at operator-approved 20x forward (above the 18.5x additive / 15.7x RRM pillar build), FY27E EPS ~45.67 gives fair value ~913 (bull ~1,006), all below CMP; expected CAGR -3.3%, Hurdle Ratio STOP; SHARED CATALYST commissioning drives both ROCE and growth; cash growth-induced (1.0x)."
```
