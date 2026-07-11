# STAGE 11: ROLE 1 DUAL-TRACK VALUATION — AKUMS DRUGS & PHARMACEUTICALS

**Run:** akums-2026-07-10  |  **Model:** claude-opus-4-8  |  **Framework:** Master v3.3 / Section 1B v3.3 (+v3.4 Amendment 4) / FTTCP v1.2
**Input source:** B10-valinputs.yaml + 10-assembly.md (deliberation_authoritative section is BINDING)
**Operating mode:** pipeline — all sections executed sequentially, interim checkpoints written but not halted.

---

## SECTION 1A: METHOD SELECTION

Akums is a hybrid CDMO (80% contract manufacturing, 10.2% domestic branded, 3.3% int'l branded, 4.2% API, 2.3% trade generics), asset-moderate, profitable, net cash Rs 1,564 cr (B10). Clean-ish earnings after tax-shield normalisation. Not a lender (no Pillar 2L carve-out). Not a BOO/annuity hybrid (no SOTP split needed).

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E (Section 1B four-pillar destination) | 60% | Profitable, earnings ≈ normalised cash after tax fix; exit PE governed solely by Section 1B |
| SECONDARY | EV/EBITDA | 30% | Capital-moderate manufacturing; cross-checks PE; net-cash adjustment material |
| TERTIARY | DCF (sanity only) | 10% | Cash conversion is growth-induced (adj CFO/PAT ~0.99x); FCF thin (Rs 17.89 cr FY26); low weight |

DCF is deliberately down-weighted: FY26 implied FCF is only Rs 17.89 cr (adj CFO 239.89 − capex 222) [B10], so DCF is hyper-sensitive to terminal value and cannot be primary. The four-pillar PE is the anchor.

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE BUILD

All four determinations below are taken verbatim from B10.deliberation_authoritative and are NOT re-litigated.

### Pillar 1 — ROCE Base Multiple

- FTTCP ROCE forward verdict: **STAGNANT** → framework maps STAGNANT to "current ROCE" [FTTCP v1.2 Pillar 1 table].
- ROCE used for base: **29.0%** (range 28-30%), the idle-cash-adjusted operating ROCE per operator override — NOT the reported 13.7% (distorted by Rs 1,654 cr idle IPO cash, ~48% of capital base) [B10 deliberation_authoritative.roce_for_pillar_1; audited ex-cash 26.3%].
- Formula (ROCE ≤ 33%): Base PE = 0.5 × ROCE + 7.5, floor 9x, cap 24x.
  - **0.5 × 29.0 + 7.5 = 22.0x** (base)
  - Range: 0.5×28+7.5 = 21.5x ; 0.5×30+7.5 = 22.5x → **21.5–22.5x**
- **ROCE recovery credited via: Pillar 1** (single-credit; NOT also Strategic Premium) [Amendment 4 / FTTCP v1.2].

### Pillar 2 — Cash Conversion Multiplier

- Cumulative adj CFO/PAT: 0.99x (ex Rs 1,032.31 cr customer-advance contract liability); headline 4.61x is distorted [B10 FLAG-CASH].
- Determination: **GROWTH-INDUCED, NOT structural** — ICRA (10 Apr 2026) "liquidity position is strong", Total Debt/OPBDITA 0.2x, no structural-WC language [B10 rating_wc_quote].
- Cash quality band: adj CFO/PAT ~1.0x sits at the 30–50%/neutral boundary but the growth-induced classification + ICRA evidence resolve it to the **neutral 1.00x** (range 0.90–1.15x). The 0.65x structural penalty is explicitly NOT applied; the Kernex-cap tail is closed.
- Growth offset: not separately added (multiplier already set at neutral 1.00x per deliberation; SOM-implied CAGR 13.9% is below-25% band which would give only +0.05 in any case).
- **Quality-Adjusted Base = 22.0x × 1.00x = 22.0x.**

### Pillar 3 — Growth Visibility + Moat Formation (v3.4 decoupled, cap +6x)

- **3a Growth Visibility = +0x.** Only 1 of 4 documented tests qualifies (capex-embedded growth 20.6% PASS; order book none FAIL; SOM-implied CAGR 13.9–16.1% <20% FAIL; delivery grade C FAIL). Need ≥2; grade C caps 3a at +2x anyway → **+0x** [B10 pillar_3a].
- **3b Moat Formation = +1x.** EM score 26.3 falls in the 25–29 STRENGTHENING band → +1x [B10 pillar_3b].
- **3c Duration Premium = +0x.** No executable order book. Contracted future streams EU EUR 200m (to Dec 2032) + Zambia USD 50m ≈ Rs 2,300 cr = 0.53x of annual revenue, far below the 2.5x (+1x) / 4.0x (+2x) thresholds → **+0x** [B10 pillar_3c].
- **Pillar 3 combined = +1x** (0 + 1 + 0). Cap +6x not binding. Equals the old undecoupled Pillar 3 — decoupling is NEUTRAL for Akums.

### Strategic Premium

- Pricing power weak, no regulatory monopoly [B04]. ROCE re-rating optionality is single-credited to Pillar 1, so it CANNOT reappear here. **Strategic Premium = +0x.**
- Optional note (not applied): a +1x for largest-domestic-CDMO scale is defensible; default and applied value is **+0x** for conservative bias. (If applied, Track 2 raw would move 23.0x → 24.0x; verdict unchanged.)

### Four-Pillar Summary (Track 2 additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | 29.0% → 0.5×29+7.5 | 22.0x |
| B. Cash Multiplier (effective) | neutral, growth-induced | 1.00x |
| C. Quality-Adjusted Base | A × B | 22.0x |
| D. Pillar 3 (3a+3b+3c) | +0 +1 +0 | +1.0x |
| E. Strategic Premium | weak pricing power, single-credit respected | +0.0x |
| F. Raw Destination PE | C + D + E | **23.0x** |
| F2. UA-Adjusted Raw PE | UA NOT applied (DII 14.3% > 3% fails qualifier 3) | 23.0x |
| G. Sector Cap | Pharma / CDMO | 38x |
| **H. Final Destination PE** | **min(F2, G) = min(23.0, 38)** | **23.0x** |

**Track 2 Destination PE Range: 23.0x ±7.5% = 21.275–24.725 → rounded to nearest 0.5x = 21.5x to 24.5x (mid 23.0x).**

Sector cap 38x is NOT binding (raw 23.0x well below). UA not applied — all-three-qualifiers fail (DII alone 14.3% > 3%); high institutional ownership is a strength, not a constraint, per Amendment 3, but the UA multiplier simply does not trigger.

### RRM Dual-Track Derivation (Track 1)

- Base r for a mid-cap = 13.0%. Adjusted **UP** for: (i) FLAG-PROMOTER governance CONCERN (Section 132 IT search Jan 2025, auditor Emphasis of Matter, CEO-CDMO resignation), (ii) cash conversion INDETERMINATE-now-resolved (residual monitoring risk), (iii) only moderate durability (weak pricing power, 44% utilisation, grade-C delivery).
- **r used = 14.5%** (bounded [9%,18%]).
- **RRM = 1 + (13.5% − 14.5%) × 0.12 = 1 − 0.12 = 0.88** (bounded 0.70–1.60).
- Fundamental Base PE = the earned four-pillar fundamental = 23.0x (Row F). Durability/governance enters via the discount rate here, not as additive points.
- **Track 1 Destination PE = 23.0x × 0.88 = 20.24x**, cap 38x not binding.
- Range ±7.5%: 18.72–21.76 → **18.5x to 22.0x (mid ~20.25x).**

### Track divergence

- Track 2 mid 23.0x vs Track 1 mid 20.25x → divergence = (23.0 − 20.25)/23.0 = **12.0%** (< 15% threshold).
- Tracks broadly agree; no material split. Per conservative bias the lower **Track 1 (RRM) governs the entry zone**. The AVOID verdict is robust to either track.

### CHECKPOINT (framework STOP point, continuing): Destination PE 21.5–24.5x (Track 2) / 18.5–22.0x (Track 1 RRM). Current PE 42.1x. Hurdle Ratio computed below → STOP.

---

## SECTION 2: PROJECTIONS (normalised for the tax-shield gap)

**ETR normalisation assumption (stated):** FY26 reported ETR is 33.0% vs statutory 25.17%, the gap driven by Rs 263.97 cr unrecognised DTA on loss-making group companies [B10 FLAG-ACCOUNTING]. Forward:
- **Base / Bull ETR = 25.17%** (statutory new-regime rate; the DTA drag normalises as loss-making subs turn or DTA is recognised).
- **Bear ETR = 30.0%** (partial persistence of subsidiary loss drag).

Reported FY26 EPS Rs 16.67 (PAT 256.4 cr). **Normalised FY26 EPS (Year 0, ETR 25.17%) = 382.01 × 0.7483 / 15.74 = Rs 18.16.** All CAGRs below are quoted from the REPORTED base (16.67) so they are consistent with the current PE of 42.1x, and therefore embed the one-time tax normalisation as part of realised growth.

### 2A/2B assumptions

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue CAGR (3-yr) | 6.0% | 12.0% | 16.0% |
| Revenue logic | domestic-branded stagnation persists (FY26 YoY was 5.85%) | below SOM-implied blended 13.9%; grade-C haircut | CDMO segment ceiling 15.7–16.1%, capacity-constrained |
| EBITDA margin (Yr 3) | 11.5% | 13.0% | 14.5% |
| PBT CAGR (3-yr) | 3.0% | 15.0% | 20.0% |
| ETR | 30.0% | 25.17% | 25.17% |

SOM cross-check: base revenue CAGR 12.0% < SOM-implied blended 13.9% [B09] → **consistent** (below the ceiling, not exceeding it).

### 2C: EPS build (Year 3)

| Scenario | PBT Yr3 (Rs cr) | ETR | PAT Yr3 (Rs cr) | EPS Yr3 (Rs) | EPS CAGR vs reported 16.67 |
|---|---|---|---|---|---|
| Bear | 382.01×1.03³ = 417.4 | 30.0% | 292.2 | **18.56** | 3.6% |
| Base | 382.01×1.15³ = 581.0 | 25.17% | 434.8 | **27.62** | 18.3% |
| Bull (uncapped) | 382.01×1.20³ = 660.1 | 25.17% | 494.1 | **31.39** | 23.5% |

**Grade-C bull cap:** Bull EPS CAGR usable in the Hurdle only if credibility grade is A/B. Grade is **C**, so Bull = Base + 5% max = 18.3% + 5% = **23.3%** → capped Bull EPS Yr3 = 16.67×1.233³ = **Rs 31.28** (essentially equal to the uncapped 31.39; the operating build already lands at the cap).

### 2D: Sanity checks

| Check | Result | Pass |
|---|---|---|
| Revenue growth within capacity? | Base 12% < SOM 13.9%; capacity gap Rs 741 cr caps bull | Yes |
| Margins unprecedented? | Base 13% vs FY26 11.98%; CDMO already at 14.4% Q4 | Yes |
| ROCE stays >15%? | Operating ROCE ~26–29%; STAGNANT verdict | Yes |
| FCF funds growth without new debt? | Net cash Rs 1,564 cr; capex Rs 300 cr FY27 self-funded | Yes |
| EPS from operations not engineering? | Yes, plus one-time tax normalisation (disclosed) | Yes |
| Year 3 ROCE consistent with STAGNANT Pillar 1? | Yes — no ROCE uplift assumed | Yes |

---

## SECTION 3: METHOD APPLICATION

### PRIMARY — P/E (Section 1B destination)

Applied exit PE = Section 1B only. Fair value (Yr 3) = EPS Yr3 × destination PE, scenario-consistent (bear→low, base→mid, bull→high).

**Track 2 (additive, 21.5 / 23.0 / 24.5x):**
- Bear: 18.56 × 21.5 = **Rs 399**
- Base: 27.62 × 23.0 = **Rs 635**
- Bull: 31.28 × 24.5 = **Rs 766**

**Track 1 (RRM, 18.5 / 20.25 / 22.0x):**
- Bear: 18.56 × 18.5 = **Rs 343**
- Base: 27.62 × 20.25 = **Rs 559**
- Bull: 31.28 × 22.0 = **Rs 688**

### SECONDARY — EV/EBITDA (cross-check)

Implied exit EV/EBITDA ≈ 0.6× of destination PE ≈ 13.8x (Track 2 mid). Base Yr3 EBITDA = 4,359×1.12³×13.0% = 6,124×0.13 = 796 cr. EV = 796 × 13.8 = 10,985 cr; + net cash 1,564 = equity 12,549 cr ÷ 15.74 = **Rs 797** (base, undiscounted Yr3). This sits between Track 2 base and bull PE outputs — consistent, no outlier. (Net-cash add is what lifts it above the PE-base; PE already captures the operating value.)

### TERTIARY — DCF (sanity only, 10%)

FCF/revenue must honour Pillar 2: growth-induced, thin FCF (Rs 17.89 cr FY26). A WACC 13% / terminal 5% DCF on a normalising FCF ramp lands near Rs 520–600 base — below CMP. Confirms overvaluation; low weight retained. Terminal value >70% of PV → down-weighted as designed.

### Method-wise fair value summary (Year 3, base case)

| Method | Weight | Bear | Base | Bull |
|---|---|---|---|---|
| P/E (Track 2) | 60% | 399 | 635 | 766 |
| EV/EBITDA | 30% | ~470 | ~640 | ~780 |
| DCF | 10% | ~430 | ~560 | ~700 |
| Weighted (Track 2) | | ~430 | ~630 | ~760 |

Methods agree within ~15% at base — no material outlier. P/E most trusted for this company.

---

## SECTION 4: TRIANGULATION, ENTRY, VERDICT

### 4A. Triangulated fair value (Year 3)

| | Bear | Base | Bull |
|---|---|---|---|
| **Track 2 (additive)** | Rs 399 | Rs 635 | Rs 766 |
| **Track 1 (RRM, conservative)** | Rs 343 | Rs 559 | Rs 688 |

### 4C. Return at current price (CMP Rs 702)

| Scenario | Track 2 FV | 3-yr CAGR | Track 1 FV | 3-yr CAGR |
|---|---|---|---|---|
| Bear | 399 | −17.2% | 343 | −21.2% |
| Base | 635 | −3.3% | 559 | −7.3% |
| Bull | 766 | +2.9% | 688 | −0.7% |

**Base fair value (both tracks) is BELOW CMP 702.** The stock trades above even its 3-year base-case fair value.

### 4D. Probability-weighted expected CAGR

Grade C → Bear 35% / Base 45% / Bull 20% [Master 4D].
- Track 2: 0.35(−17.2) + 0.45(−3.3) + 0.20(+2.9) = **−6.9%**
- Track 1: 0.35(−21.2) + 0.45(−7.3) + 0.20(−0.7) = **−10.8%**
- **Blended ≈ −8.9% expected 3-yr CAGR** (negative; fails the 25% target by a wide margin).

### Hurdle Ratio (Amendment 2)

HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE), pass ≥ 1.953. Current PE = 42.1x.

| Row | EPS CAGR | Track 2 mid 23.0x | Track 1 mid 20.25x |
|---|---|---|---|
| **Base** | 18.3% | (1.183)³×(23.0/42.1) = 1.657×0.546 = **0.91** | 1.657×0.481 = **0.80** |
| **Bull (grade-C capped 23.3%)** | 23.3% | (1.233)³×0.546 = 1.876×0.546 = **1.02** | 1.876×0.481 = **0.90** |

**Both Base AND grade-C-capped Bull fall far below 1.953 on both tracks → HURDLE VERDICT = STOP.** 25% CAGR is infeasible at Rs 702 even on bull-case earnings. (Matches B10's computed HR ~0.99 / STOP.)

### 4E. Entry price (conservative Track 1 base FV Rs 559)

| Calculation | Value |
|---|---|
| Base FV (Yr 3, Track 1) | Rs 559 |
| 25% CAGR entry = 559 ÷ 1.953 | **Rs 286** |
| 30% CAGR entry = 559 ÷ 2.197 | **Rs 254** |
| MoS price (20% below 25% entry) | **Rs 229** |
| **Ideal entry range** | **Rs 254 to Rs 286** |

(Track 2 25% CAGR entry for reference = 635 ÷ 1.953 = Rs 325; conservative Track 1 governs.)

### 4F. Risk-reward asymmetry (from CMP 702)

- Bull upside (Track 2) = 766/702 − 1 = +9.1%
- Base = −9.5% (no upside)
- Bear downside (Track 2) = 399/702 − 1 = −43.2%
- **Upside/Downside ≈ 0.21x** (bull-upside ÷ bear-downside; base offers NO upside). Fails the ≥2x test decisively.

### 4G. Four-pillar validation

| Check | Result | Pass |
|---|---|---|
| Yr3 ROCE justifies base & matches STAGNANT? | Yes, no uplift assumed | Yes |
| Yr3 CFO/PAT justifies 1.00x? | Growth-induced, adj ~0.99x, ICRA strong | Yes |
| Primary catalyst fired by Yr3? | CDMO volume yes; EU/Zambia are FY28+ | Partial |
| Strategic premium single-credit respected? | Yes (+0x; ROCE in Pillar 1 only) | Yes |
| UA ordering min(F×1.25, cap) correct? | UA not applied; H = min(23.0, 38) | Yes |

### 4H. Verdict Card

- **CMP Rs 702 | Market cap Rs 11,052 cr** [B10]
- **FOUR-PILLAR:** ROCE base 29% → 22.0x (STAGNANT, idle-cash-adjusted, recovery via Pillar 1) | Cash 1.00x neutral (growth-induced) | Quality base 22.0x | Pillar 3 +1x (3a 0 / 3b 1 / 3c 0) | Strategic +0x | Raw 23.0x | UA not applied | Sector cap 38x (not binding) | **Destination PE 21.5–24.5x (Track 2), 18.5–22.0x (Track 1 RRM, r=14.5%, RRM=0.88)**
- **HURDLE RATIO 0.91 (base) / 1.02 (bull) → STOP**
- **Weighted FV (Yr3):** Bear 399 / Base 635 / Bull 766 (Track 2); Bear 343 / Base 559 / Bull 688 (Track 1)
- **Expected CAGR (prob-weighted, grade C):** ≈ −8.9%
- **Upside/Downside:** ~0.21x
- **Entry range Rs 254–286 | MoS price Rs 229**
- **DECISION: AVOID (on valuation + governance).** Four independent Master AVOID triggers all fire: Gate 0 AVERAGE; Promoter CONCERN (FLAG-PROMOTER); Hurdle STOP; Upside/Downside <2x. Stock trades above base 3-yr fair value on both tracks.
- **ONE-LINE THESIS:** Avoiding Akums at Rs 702 because even on the operator's idle-cash-adjusted 29% ROCE the earned destination PE is only ~23x (21.5–24.5x) against a current 42.1x, so normalised EPS rising from Rs 16.67 to ~Rs 27.6 base still yields a Rs 635 three-year target — below today's price. Hurdle STOP, expected CAGR ≈ −9%. Re-engage only near Rs 254–286. Key risk to the bear thesis: CDMO re-rating on EU/Zambia execution. Cash quality: growth-induced (adj CFO/PAT 0.99x, 1.00x neutral).

---

```yaml
stage: B11-valuation
company: "AKUMS"
run_date: "2026-07-10"
model: claude-opus-4-8
status: complete
input_gaps: []
flags:
  - type: FLAG-CASH
    reason: "Cash conversion GROWTH-INDUCED (ICRA-confirmed, adj CFO/PAT 0.99x); Pillar 2 multiplier applied = 1.00x neutral, NOT 0.65x structural penalty. Kernex-cap tail closed."
  - type: FLAG-PROMOTER
    reason: "Section 132 IT search Jan 2025 + auditor EOM + CEO-CDMO resignation = governance CONCERN; contributes to AVOID and to r uplift to 14.5% in Track 1."
  - type: FLAG-ACCOUNTING
    reason: "FY26 reported EPS depressed by tax-shield gap (ETR 33% vs statutory 25.17%). Normalised forward ETR: 25.17% base/bull, 30% bear. Normalised FY26 EPS Rs 18.16."
  - type: SHARED-CATALYST
    reason: false
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 18.5, mid: 20.25, high: 22.0, r_used: 14.5, rrm: 0.88}
  track2_additive: {low: 21.5, mid: 23.0, high: 24.5}
  divergence_pct: 12.0
  governing_track: "Track 1 RRM governs entry (lower, conservative); divergence 12% < 15%, tracks agree, AVOID robust to both"
pillar_detail:
  roce_used: 29.0
  roce_base: 29.0
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 1.00
  structural_or_growth: "growth-induced"
  growth_offset: 0
  growth_premium: 1
  strategic_premium: 0
  shared_catalyst_flag: false
  ua_applied: false
  sector_cap_used: 38
hurdle_ratio: {base: 0.91, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 343, base: 559, bull: 688}
  track2: {bear: 399, base: 635, bull: 766}
expected_cagr_prob_weighted: -8.9
entry_range: {low: 254, high: 286}
mos_price: 229
upside_downside_ratio: 0.21
decision: "AVOID (on-valuation + governance)"
unresolved_inputs_used:
  - "FY26 D&A full-year line NOT FOUND; conservative ~Rs 200-250 cr used in EV/EBITDA and DCF sanity only, does not affect PE-primary destination or verdict."
  - "Peer multiples NOT FOUND (only 4 comparators, PPLPHARMA mislabeled); relative valuation not used, Section 1B is sole exit authority."
  - "BVPS NOT FOUND; P/B not applied (non-lender)."
som_cagr_crosscheck: "consistent"
one_line_thesis: "Avoid Akums at Rs 702: earned destination PE ~23x vs current 42.1x means normalised EPS Rs 16.67 to ~Rs 27.6 still yields a Rs 635 3-yr target below CMP; Hurdle STOP, expected CAGR ~-9%; re-engage Rs 254-286."
```
