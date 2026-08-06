# STAGE 11 — ROLE 1 MULTI-METHOD VALUATION

**Company:** United Foodbrands Limited (UFBL), erstwhile Barbeque Nation Hospitality Ltd
**Ticker:** UFBL | **CMP:** Rs 772.00 | **Market cap:** Rs 3,017 cr | **Shares (diluted):** 3.898 cr | **Run date:** 2026-08-05
**Frameworks:** Master Project Prompt v3.3 (Role 1) / Section 1B v3.5.1 Reconciliation / FTTCP v1.2
**Model:** claude-opus-4-8

> **OPERATOR-APPROVED BASE (authoritative, not re-derived).** Per the FTTCP deliberation record (Section 5) and B10, the destination exit multiple, its basis, and every pillar were approved by the operator at the FTTCP pillar-approval gate. This stage values ON that approved base. Where my independent Section 1B derivation would diverge, I report the divergence but value on the approved base, per the wrapper's OPERATOR-APPROVED BASE rule.

---

## SECTION 1A — METHOD SELECTION

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | **Pre-Ind AS EV/EBITDA** | 60% | Operator ruling (FTTCP Section 5; B10 `primary_method`). Restaurant operator is a leased, capital-light-per-store, depreciation-heavy services business. Pre-Ind AS basis strips Ind AS 116 lease grossing so rent sits as an operating cost — the basis on which listed QSR peers are judged and on which the 25% pre-Ind AS ROCE was set. |
| CROSS-CHECK (governing) | **Forward pre-Ind AS P/E @ 25.0x** | 40% | Operator-selected governing exit multiple (B10 `approved_exit_pe_x` 25.0x). "Forward ending method" — one-year-forward pre-Ind AS EPS (B10 `earnings_basis`). |
| REJECTED | Trailing P/E | — | Arithmetically impossible: FY26 reported EPS −Rs 15.13 (B10 `eps_diluted_reported_rs`). |
| REJECTED | P/B | — | Asset-light brand/services value not captured by book; not a lender. |
| REJECTED | DCF | — | Loss-making base year, thin-to-negative near-term FCF-after-lease, terminal-value-dominated for a turnaround; unreliable here. |

**Basis consistency guard (the SFL lesson, per deliberation Section 5 and B10 `fttcp_approved_valuation_pillars_authoritative`).** The ROCE basis, the EPS the multiple is applied to, and the EV/EBITDA basis are ALL pre-Ind AS. Financial net debt Rs 102 cr enters the pre-Ind AS EV bridge; lease liabilities Rs 750.84 cr belong only to the reported/post-Ind AS bridge and are excluded here. The Hurdle Ratio holds one consistent pre-Ind AS forward basis on both sides (numerator PE and denominator EPS growth).

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE (operator-approved; recorded, not re-litigated)

All pillar values are AUTHORITATIVE from B10 `fttcp_approved_valuation_pillars_authoritative` / deliberation Section 5. My independent divergence is stated after.

### Pillar 1 — ROCE Base
- FTTCP ROCE forward verdict: RECOVERING (deliberation Section 1). **Pillar 1 normalization route: NONE** (B10 `pillar_1_normalization_route`; operator anchor supersedes mechanical Route A / Route B per Section 1B v3.5.1). Route-selection guard checked: verdict is RECOVERING (not STAGNANT/DECLINING), so a route COULD be invoked, but the operator's conviction-led anchor is used in its place and declared NONE.
- ROCE used: **25.0%** — pre-Ind AS operational mature anchor (B10 `pillar_1_roce_base_pct`). Not from printed history (best lease-inclusive year ~9%); middle of the defensible 22–25% mature range.
- **ROCE Base PE = 0.5 × 25 + 7.5 = 20.0x** (Amendment 5; B10 `pillar_1_base_pe_x`). Floor 9x / cap 24x not binding.
- **ROCE recovery credited via: Pillar 1 midpoint.** Strategic Premium ROCE re-rating option BARRED (single-credit rule, Amendment 4; B10).

### Pillar 2 — Cash Conversion Multiplier
- Determination: **GROWTH-INDUCED** (B10 `cash_conversion_determination.classification`; FTTCP Section 1). Customers pay at table, receivables <1 day, WC negative, CFO 91.5% FY25 / 115.6% FY26 of EBITDA, cumulative CFO +1,477 cr vs PAT −267 cr FY17–26.
- **Cash multiplier = 1.15x** (B10 `pillar_2_cash_multiplier_x`). Applied as given; not re-litigated per wrapper rule.
- FLAG-CASH carried: standalone cash −85%, first WC loan drawn, current ratio 0.46; classified growth-induced, not structural. Falsifier: consolidated interest-bearing net debt >Rs 102 cr while store count grows.
- **Quality-adjusted base = 20.0 × 1.15 = 23.0x** (B10 `quality_adjusted_base_pe_x`).

### Pillar 3 — Growth / Moat / Duration (decoupled, Amendments 4.1/4.2)
- **3a Growth Visibility = +2.0x** (B10 `pillar_3a_growth_premium_x`). Delivery grade B, SOM-implied growth 20.6% (B09). **SHARED CATALYST flagged** — store rollout + SSSG recovery drives both Pillar 1 ROCE and this premium (single point of failure; Role 3 must stress-test).
- **3b Moat Formation = +0.0x** — Emerging Moat 9.1 (B12c corrected), below 25 threshold.
- **3c Duration = +0.0x** — no order book / contracted revenue.
- Combined 3a+3b+3c = +2.0x, within the +6x cap.

### Strategic Premium & UA
- **Strategic Premium = +0.0x** — brand without documented pricing power fails the gate; ROCE re-rating barred (single-credit).
- **Undiscovered Alpha: NOT applied** — institutions ~27.8% >> 3% qualifier (B10 `undiscovered_alpha_applied` NO). F2 row = F (no ×1.25).

### Four-Pillar Summary — Track 2 (Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | 0.5×25 + 7.5 | 20.0x |
| B. Cash Multiplier | (growth-induced) | 1.15x |
| C. Quality-Adjusted Base | 20.0 × 1.15 | 23.0x |
| D. Growth Visibility (3a+3b+3c) | +2.0 + 0 + 0 | +2.0x |
| E. Strategic Premium | — | +0.0x |
| F. Raw Destination PE | 23.0 + 2.0 | **25.0x** |
| F2. UA-Adjusted Raw PE | UA not qualified → = F | 25.0x |
| G. Sector Cap (Hotels) | B10 `sector_cap_x` | 30.0x (not binding) |
| **H. Final Destination PE (Track 2)** | **min(F2, G)** | **25.0x** |

**Track 2 destination PE range (±7.5%):** 23.1x to 26.9x (B10). **APPROVED / GOVERNING = 25.0x.**

### RRM Dual-Track — Track 1 (recorded, not selected)
- Base r = 16% (small/micro 14% base, +2% for governance/durability weakness). r bound [9%,18%] respected.
- **RRM = 1 + (13.5 − 16) × 0.12 = 1 + (−2.5)(0.12) = 1 − 0.30 = 0.70** (Amendment 4.4 percentage-point reading; bounded ×0.70–×1.60, at floor).
- **Track 1 Destination PE = 25.0 (fundamental base) × 0.70 = 17.5x** (B10 `rrm_destination_pe_track_1_x`; range 16.2–18.8x).

### Track divergence
Additive 25.0x vs RRM 17.5x → divergence **(25.0 − 17.5) / 25.0 = 30.0%** (>15% trigger). The RRM track is the more conservative (framework default would let it set the entry zone). **However the operator OVERRODE this and selected the additive 25.0x as the governing exit multiple** (deliberation Override 2), to price the full pillar stack rather than the RRM risk haircut. Governing track = **additive (Track 2)**; RRM carried through for the record.

### Independent-divergence note (reported, not applied)
My mechanical Section 1B read on a RECOVERING verdict would blend current ROCE 1.64% with FY[Y+2] ~11% (60/40 → ~5.4%), giving base PE ~10.2x, and the RRM track (17.5x) would govern the 30% divergence. The operator override to 25% pre-Ind AS ROCE and additive 25.0x is authoritative; I value on it and flag the gap. This is the single largest sensitivity in the file: the approved base prices the FY30 steady state today.

---

## SECTION 2 — FORWARD PRE-IND AS EARNINGS BUILD

**Consistency:** all figures pre-Ind AS (rent expensed as operating cost; ROU depreciation and lease interest EXCLUDED; only owned-asset depreciation and financial interest deducted).

### Base-year anchor (FY27, one-year-forward)
- FY26 consolidated revenue Rs 1,338.7 cr (B10). Q1 FY27 revenue Rs 425.9 cr, annualises to Rs 1,704 cr (B10 `revenue_consolidated_q1_fy27_rs_cr`).
- FY27 revenue: **Bear 1,500 / Base 1,640 / Bull 1,704 cr** (Bear +12%; Base +22.5% ≈ task illustrative, below Q1 run-rate; Bull = Q1 FY27 annualised run-rate +27.3%).
- Pre-Ind AS adjusted operating EBITDA margin FY27: **Bear 8.0% / Base 9.0% / Bull 10.0%** (B10 guidance 9–10%; Q1 FY27 actual 8.1%).

**INPUT UNRESOLVED: owned-asset depreciation ex-ROU.** B10 discloses only total D&A inclusive of Ind AS 116 ROU depreciation (consolidated Rs 189.99 cr FY26). Conservative assumption used: owned-asset depreciation Rs 100 cr FY27 rising to Rs 120–145 cr FY30, because (i) lease liabilities Rs 750.84 cr imply ROU depreciation ~Rs 90–110 cr, leaving owned-asset D&A ~Rs 80–100 cr of the Rs 189.99 cr total, and (ii) a higher owned-depreciation figure lowers pre-Ind AS EPS and fair value (conservative bias). Financial interest Rs 14 cr FY27 / Rs 12 cr FY30 (on ~Rs 134 cr borrowings / ~Rs 100 cr net debt held per guidance). Tax 25.17% (normalised full rate; accumulated-loss carryforward treated as unquantified near-term upside, not credited).

### Pre-Ind AS build

| FY27 (base year) | Bear | Base | Bull |
|---|---|---|---|
| Revenue (Rs cr) | 1,500 | 1,640 | 1,704 |
| Pre-Ind AS EBITDA margin | 8.0% | 9.0% | 10.0% |
| Pre-Ind AS EBITDA (Rs cr) | 120.0 | 147.6 | 170.4 |
| Less owned depreciation (ex-ROU) | 100 | 100 | 100 |
| Less financial interest | 14 | 14 | 14 |
| Pre-Ind AS PBT | 6.0 | 33.6 | 56.4 |
| Tax @25.17% | 1.51 | 8.46 | 14.19 |
| **Pre-Ind AS PAT** | 4.49 | 25.14 | 42.21 |
| **Pre-Ind AS EPS (÷3.898)** | **1.15** | **6.45** | **10.83** |

| FY30 (exit year, +3 yrs) | Bear | Base | Bull |
|---|---|---|---|
| Revenue CAGR FY27→FY30 | 10% | 15% | 20% |
| Revenue (Rs cr) | 1,996.5 | 2,494.2 | 2,944.5 |
| Pre-Ind AS EBITDA margin | 9.0% | 11.0% | 13.0% |
| Pre-Ind AS EBITDA (Rs cr) | 179.7 | 274.4 | 382.8 |
| Less owned depreciation (ex-ROU) | 120 | 130 | 145 |
| Less financial interest | 12 | 12 | 12 |
| Pre-Ind AS PBT | 47.7 | 132.4 | 225.8 |
| Tax @25.17% | 12.00 | 33.32 | 56.83 |
| **Pre-Ind AS PAT** | 35.69 | 99.05 | 168.96 |
| **Pre-Ind AS EPS (÷3.898)** | **9.16** | **25.41** | **43.35** |

**Implied pre-Ind AS EPS CAGR FY27→FY30:** Bear 99.6% / Base 57.9% / Bull 58.8%. These are inflated by operating leverage off a near-breakeven FY27 base and are an artifact of the thin base — see the Hurdle-Ratio simplification in Section 4, where the base year cancels and the check becomes robust.

### 2D — Sanity checks
| Check | Result | Pass |
|---|---|---|
| Base revenue CAGR 15% vs SOM-implied 20.6% (B09) | Below SOM; conservative | PASS (consistent) |
| Margins require the unprecedented? | FY30 11% pre-Ind AS vs 9–10% guided FY27 + back-end cost to 6.0%; plausible | PASS |
| FY30 ROCE consistent with 25% pre-Ind AS anchor? | Approved anchor prices FY30 steady state; forward EBIT trajectory supports recovery, absolute 25% is conviction-led (flagged) | CAVEAT (operator-anchored) |
| EPS growth operational, not financial engineering? | Yes — margin + volume; net debt held flat | PASS |
| Bull only if grade A/B? | Grade B → bull usable | PASS |

---

## SECTION 3 — VALUATION METHODS APPLIED

### 3.1 PRIMARY — Pre-Ind AS EV/EBITDA (destination multiple derived consistent with 25.0x forward P/E)

Destination EV/EBITDA is derived so it is arithmetically consistent with the approved 25.0x pre-Ind AS forward P/E on the same pre-Ind AS build (net debt ~Rs 100 cr, owned-depreciation and financial-interest structure above):

**EV/EBITDA = (P/E × PAT + Net Debt) ÷ EBITDA** (FY30 base): = (25.0 × 99.05 + 100) ÷ 274.4 = (2,476 + 100) ÷ 274.4 = **9.39x**.

**Destination pre-Ind AS EV/EBITDA ≈ 9.4x** (range ±7.5%: 8.7x–10.1x). The multiple is low relative to the "0.6–0.7× of PE" rule of thumb because owned depreciation is ~47% of pre-Ind AS EBITDA and the pre-Ind AS EV excludes the Rs 750.84 cr lease liability — both structurally compress EV/EBITDA versus a post-Ind AS lens.

**PEER EV/EBITDA MEDIANS: UNRESOLVED** (B10 `peer_set_multiples.ev_ebitda_median` — no peer financial CSVs for Westlife / Sapphire / RBA / Speciality). The 9.4x destination is therefore **framework-internal, not peer-validated.** Gap flagged: listed QSR peers trade at high post-Ind AS EV/EBITDA (~20–30x inclusive of leases), which is NOT comparable to a pre-Ind AS 9.4x; a like-basis peer check cannot be performed without the CSVs.

EV/EBITDA fair value (FY30, base): EV = 9.39 × 274.4 = 2,577 cr; less net debt 100 = equity 2,477 cr; ÷ 3.898 = **Rs 635.5**. By construction this equals the P/E cross-check below (same pre-Ind AS build), so the two methods AGREE but are not independent — the peer gap is the reason independent validation is absent.

**Current pre-Ind AS EV/EBITDA for context:** EV Rs 3,119 cr (B10; mcap 3,017 + net debt 102) ÷ FY27 base EBITDA 147.6 = **21.1x**; ÷ FY26 pre-Ind AS EBITDA ~99–100 = **~31x**. Market pays ~2.2–3.3× the 9.4x destination today.

### 3.2 GOVERNING CROSS-CHECK — Forward pre-Ind AS P/E @ 25.0x (Track 2) and @ 17.5x (Track 1)

Fair value (Year 3 / FY30 target) = FY30 pre-Ind AS EPS × destination PE:

| | Bear EPS 9.16 | Base EPS 25.41 | Bull EPS 43.35 |
|---|---|---|---|
| **Track 2 @ 25.0x (governing)** | Rs 229 | **Rs 635** | Rs 1,084 |
| **Track 1 @ 17.5x (RRM, record)** | Rs 160 | Rs 445 | Rs 759 |

---

## SECTION 4 — TRIANGULATION, HURDLE, ENTRY, VERDICT

### 4A — Triangulated fair value (Year 3, FY30 target)
Primary EV/EBITDA and the P/E cross-check coincide by construction. Fair values:

| Track | Bear | Base | Bull |
|---|---|---|---|
| **Track 2 (Additive 25.0x) — GOVERNING** | Rs 229 | **Rs 635** | Rs 1,084 |
| **Track 1 (RRM 17.5x) — record** | Rs 160 | Rs 445 | Rs 759 |

### 4C — Return at current price (CMP Rs 772)
| Scenario | Track 2 target | 3-yr CAGR from CMP | ≥25%? |
|---|---|---|---|
| Bear | 229 | −33.3% | 🔴 |
| Base | 635 | −6.3% | 🔴 |
| Bull | 1,084 | +12.0% | 🔴 |

Even the bull 3-year target (Rs 1,084) delivers only +12% CAGR; the base target sits BELOW today's price.

### 4D — Probability-weighted expected CAGR
Credibility grade **B** (B10) → weights Bear 25% / Base 50% / Bull 25%.
Track 2: 0.25(−33.3%) + 0.50(−6.3%) + 0.25(+12.0%) = **−8.5% expected 3-yr CAGR.**
(Track 1 RRM: −18.7%.)

### 4 — HURDLE RATIO
**HR = (1 + EPS CAGR)³ × (Destination PE mid ÷ Current PE).** On a consistent pre-Ind AS forward basis the FY27 base year cancels and HR reduces to **(FY30 pre-Ind AS EPS × Destination PE) ÷ CMP = Year-3 target ÷ CMP** — robust to the thin-base EPS-CAGR artifact.

| Scenario | Track 2 HR = target/772 | Result |
|---|---|---|
| Bear | 229/772 = 0.30 | fail |
| Base | 635/772 = **0.82** | fail |
| Bull | 1,084/772 = **1.40** | fail |

**Bull HR 1.40 < 1.953 → VERDICT: STOP.** Bull EPS CAGR is admissible (grade B) and still fails; 25% CAGR is infeasible even on bull-case pre-Ind AS earnings at Rs 772.

Sensitivity to the one unresolved input (owned depreciation): to lift bull HR to 1.953 requires FY30 owned-plus-financial charge ≈ Rs 57 cr against Rs 382.8 cr bull EBITDA — implausibly low for a ~400–425 store base. **STOP is robust to the depreciation assumption.**

### 4E — Entry price (Tier A, hurdle 25%, divisor 1.953; governing additive track, base FV Rs 635)
| Calculation | Value |
|---|---|
| Base fair value (FY30) | Rs 635 |
| Entry @25% CAGR = 635 ÷ 1.953 | **Rs 325** |
| Entry @30% CAGR = 635 ÷ 2.197 (extra safety) | Rs 289 |
| **Ideal entry range** | **Rs 289 – Rs 325** |
| **MoS price (20% below the 25% entry)** | **Rs 260** |
| CMP vs entry | Rs 772 = **2.4× the entry ceiling** |
| (RRM track, record) entry @25% = 445 ÷ 1.953 | Rs 228; MoS Rs 182 |

### 4F — Risk-reward
Base target Rs 635 is below CMP (no base upside). Bull upside +40.4% vs bear downside −70.3% → ratio **0.57** (< 2× required). Base offers negative return; asymmetry fails.

### 4G — Four-pillar validation
| Check | Result | Pass |
|---|---|---|
| FY30 ROCE justifies 25% base? | Operator conviction anchor, not printed; flagged | CAVEAT |
| FY30 CFO/PAT justifies 1.15x? | Growth-induced, WC negative; consistent | PASS |
| Shared catalyst fired by Year 3 (base)? | SSSG + rollout; single point of failure | FLAG (Role 3) |
| Strategic premium single-credit respected? | +0x; ROCE via Pillar 1 only | PASS |
| UA ordering min(F×1.25, cap)? | UA not qualified; = F | PASS |
| Sector cap absolute (30x) | Not binding at 25.0x | PASS |

### 4H — VERDICT CARD

- **Tier: A | Hurdle: 25%**
- CMP Rs 772 | Mkt cap Rs 3,017 cr | EV Rs 3,119 cr (pre-Ind AS, financial net debt Rs 102 cr)
- **Four-pillar exit PE:** ROCE base 20.0x (ROCE 25% pre-Ind AS, FTTCP RECOVERING, recovery via Pillar 1) × cash 1.15x (growth-induced) = 23.0x quality base + 2.0x growth (EM 9.1, shared catalyst) + 0 strategic = **Raw 25.0x; UA n/a; Final 25.0x (range 23.1–26.9x).** Sector cap 30x (Hotels), not binding.
- **RRM track:** r 16%, RRM 0.70 → **17.5x** (range 16.2–18.8x).
- **Primary EV/EBITDA destination:** ~9.4x pre-Ind AS (peer medians UNRESOLVED — framework-internal only).
- **Hurdle Ratio:** Base 0.82 / Bull 1.40 → **STOP** (bull fails 1.953).
- **Fair value (Yr 3):** Track 2 Bear 229 / Base 635 / Bull 1,084; Track 1 Bear 160 / Base 445 / Bull 759.
- **Expected CAGR (prob-weighted, grade B):** −8.5%.
- **Upside/downside:** 0.57 (fails ≥2×; base below CMP).
- **Entry range Rs 289–325 | MoS Rs 260** (governing additive). CMP is 2.4× the entry ceiling.
- **DECISION: AVOID (on valuation).** Gate-0-backward AVOID, promoter CAUTION, EM NONE and the accounting-quality flags all reinforce; but the binding reason is price — even bull-case pre-Ind AS earnings clear only +12% CAGR.
- **Key valuation sensitivities:** ▲ if pre-Ind AS EBITDA margin sustainably exceeds 13% AND revenue CAGR nears the 20.6% SOM ceiling (bull); ▼ if SSSG lapses to low-single-digit as the H2 FY26 base is lapped (the shared catalyst) — margin and growth collapse together.
- **Exit framework:** the name re-enters the buy conversation only near Rs 289–325 AND with the SSSG/gross-margin catalyst still firing (entry conjunction). Thesis-broken: net debt >Rs 102 cr while stores grow, or SSSG to low single digits.
- **ONE-LINE THESIS:** Buying UFBL at Rs 772 fails the 25% hurdle because forward pre-Ind AS EPS of ~Rs 6.5 (FY27) compounding to ~Rs 25 (FY30) at the approved 25.0x destination PE yields a Rs 635 base target BELOW today's price; even bull earnings clear only +12% CAGR, so the operator-approved pillar stack does not rescue an order-of-magnitude overvaluation. AVOID on valuation; revisit near Rs 289–325.

**FLAGS carried forward:** FLAG-CASH (multiplier applied 1.15x, growth-induced); SHARED-CATALYST (store rollout + SSSG → Pillar 1 and Pillar 3a; Role 3 stress-test); FLAG-ACCOUNTING-QUALITY (Rule 11(g) audit-trail, MENA impairment, Note 25b reconciliation gap); FLAG-EMOAT (EM 9.1 NONE, digital moat unproven). Input gap: owned-asset depreciation ex-ROU and peer EV/EBITDA medians UNRESOLVED (neither changes the STOP verdict).

---

```yaml
stage: B11-valuation
company: "UFBL"
run_date: "2026-08-05"
model: claude-opus-4-8
status: complete
input_gaps:
  - "Owned-asset depreciation ex-ROU not disclosed (only total D&A incl Ind AS 116 ROU given); conservative assumption used, does not change STOP verdict"
  - "Peer EV/EBITDA medians UNRESOLVED (no peer CSVs); destination 9.4x is framework-internal, not peer-validated"
flags:
  - "FLAG-CASH: cash multiplier applied 1.15x, GROWTH-INDUCED (not structural); falsifier net debt >Rs 102 cr while stores grow"
  - "SHARED-CATALYST: store rollout + SSSG recovery drives both Pillar 1 ROCE and Pillar 3a; single point of failure; Role 3 must stress-test"
  - "FLAG-ACCOUNTING-QUALITY: Rule 11(g) audit-trail limitation, MENA impairment inconsistency, Note 25b FY24 reconciliation gap"
  - "FLAG-EMOAT: EM 9.1 (NONE); digital/captive-channel moat unproven at scale"
framework_versions: "Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2"
pe_basis: "forward"
exit_pe_base_approved: "25.0x additive (operator-selected governing exit multiple; one-year-forward pre-Ind AS basis)"
destination_pe:
  track1_rrm: {low: 16.2, mid: 17.5, high: 18.8, r_used: 16, rrm: 0.70}
  track2_additive: {low: 23.1, mid: 25.0, high: 26.9}
  divergence_pct: 30.0
  governing_track: "additive Track 2 (operator override of RRM per deliberation); RRM more conservative but does not govern"
pillar_detail:
  roce_used: 25.0
  roce_base: 20.0
  roce_recovery_route: "pillar1-midpoint"
  pillar1_normalization_route: "none"
  cash_multiplier: 1.15
  structural_or_growth: "growth-induced"
  growth_offset: 0
  growth_premium: 2.0
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 30.0
hurdle_ratio: {base: 0.82, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 160, base: 445, bull: 759}
  track2: {bear: 229, base: 635, bull: 1084}
expected_cagr_prob_weighted: -8.5
entry_range: {low: 289, high: 325}
mos_price: 260
upside_downside_ratio: 0.57
decision: "AVOID (on valuation)"
unresolved_inputs_used:
  - "Owned-asset depreciation ex-ROU: assumed Rs 100 cr FY27 / Rs 120-145 cr FY30 (conservative; higher dep lowers EPS/FV); STOP robust to this input"
  - "Financial interest: Rs 14 cr FY27 / Rs 12 cr FY30 on ~Rs 134 cr borrowings, net debt held ~Rs 100 cr per guidance"
  - "Tax 25.17% normalised full rate; accumulated-loss carryforward not credited (conservative)"
som_cagr_crosscheck: "consistent (base revenue CAGR 15% below SOM-implied 20.6%)"
one_line_thesis: "At Rs 772 UFBL fails the Tier A 25% hurdle: forward pre-Ind AS EPS ~Rs 6.5 (FY27) to ~Rs 25 (FY30) at the approved 25.0x destination PE gives a Rs 635 base target below today's price, and even bull earnings clear only +12% CAGR; AVOID on valuation, revisit Rs 289-325."
```
