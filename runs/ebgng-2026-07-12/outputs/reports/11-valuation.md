# STAGE 11 — ROLE 1 DUAL-TRACK VALUATION

**Company:** GNG Electronics Ltd (EBGNG) | **Run date:** 2026-07-12 | **Model:** claude-opus-4-8
**Frameworks:** Master v3.3 / Section 1B v3.3 (through Amendment 4.5) / FTTCP v1.2
**Mode:** pipeline (all sections executed in one pass; interim STOP lines written as checkpoints, then continued)

Every input carries a B10 anchor the first time it is used. Deliberation-authoritative operator rulings (fttcp-deliberation.md) supersede any conflicting value and are honored exactly.

---

## INPUT DISCIPLINE — RESOLVED AND UNRESOLVED

| Field | Value used | Source / treatment |
|---|---|---|
| CMP | Rs 634 | manifest / B10 |
| Diluted shares | 11.401 Cr | B10 (equity capital 228.02 M / Rs 2 face) |
| Market cap | Rs 7,227 Cr | manifest / B10 |
| Net debt | Rs 287.51 Cr | B10 (405.75 gross − 118.24 cash) |
| Enterprise value | Rs 7,514.51 Cr | B10 |
| FY26 revenue | Rs 1,891.08 Cr | Results Q4 FY26 p.20 (B10) |
| FY26 PAT | Rs 132.02 Cr | Results Q4 FY26 p.20 (B10) |
| FY26 diluted EPS | Rs 11.58 | Results Q4 FY26 Note 5 (B10) |
| FY26 PAT margin | 6.98% | B10 |
| Pillar 1 ROCE | 28.3% operational ex-surplus-cash | fttcp-deliberation Override 1 (supersedes reported 24.06%) |
| ROCE forward verdict | RECOVERING (40–60%, 12m) | fttcp-deliberation |
| Cash conversion | INDETERMINATE (not overridden) | fttcp-deliberation |
| Destination/exit PE | **20x, forward basis (20x × FY30 EPS at FY29 exit)** | fttcp-deliberation Overrides 2 & 4 (governs) |
| Sector cap | Recycling / Manufacturing, 25x | fttcp-deliberation Override 3 |
| Credibility grade | B (Good) | B05-concall |
| Promoter verdict | CAUTION | B08 / fttcp-deliberation |
| EM score | 23.0 (MODEST) | B07-emoat |
| SOM-implied 3yr rev CAGR | 35.7% | B09-tam |

**INPUT UNRESOLVED: EBITDA (FY26).** Conservative assumption used: EBITDA = EBIT 190.15 Cr (deliberation ROCE calc) + D&A 10.35 Cr = **Rs 200.50 Cr** (margin 10.6%), because the results PDF does not state an EBITDA line and the framework requires reconstruction from P&L rather than a peer proxy. Used only for the EV/EBITDA cross-check.

**INPUT UNRESOLVED: FY[Y+2] expected ROCE.** Conservative assumption used: RECOVERING blend defaults to the current operational figure 28.3%, because FY[Y+2] ROCE is NOT FOUND (fttcp-deliberation ruling 9) and NOT FOUND is the only valid fill. No mechanical uplift to the ROCE base.

**INPUT UNRESOLVED: FY27–FY30 EPS.** Conservative assumption used: projected from the FY26 EPS 11.58 base with the documented bear/base/bull set in Section 2, all held below management guidance / SOM / history.

**INPUT UNRESOLVED: peer P/E, EV/EBITDA, P/B medians.** NOT FOUND in B10; peer multiple triangulation is unavailable. The P/E method therefore rests on the Section 1B / operator-set exit PE, exactly as the framework intends (exit multiple is earned, not borrowed from peers).

---

## SECTION 1A — METHOD SELECTION

| Role | Method | Weight | Justification |
|---|---|---|---|
| PRIMARY | P/E | 85% | Asset-light refurbisher/trader with clean reported PAT; the exit multiple is governed by Section 1B and fixed by operator override at 20x forward. Earnings are the value driver. |
| SECONDARY | EV/EBITDA | 15% | Cross-check only. EBITDA is reconstructed (NOT FOUND), so this is a sanity rail, not an independent anchor. |
| NOT USED | DCF | 0% | Rejected. CFO negative (Rs -215.30 Cr FY26), FCF negative (Rs -238.15 Cr), cash conversion INDETERMINATE. The framework forbids assuming cash conversion "magically improves" in a DCF for a structural-WC name (CARE: negative CFO since FY20). Terminal value would dominate and mislead. |
| NOT USED | P/B | cross-ref | Not a lender; book value (Rs 66.5/sh) does not capture the business. Noted only: P/B at CMP = 634/66.5 = 9.5x, rich. |

🛑 *Checkpoint: methods selected. Primary P/E, exit PE from Section 1B / operator override.*

---

## SECTION 1B — FOUR-PILLAR EXIT MULTIPLE (mechanical build for transparency; operator 20x governs)

### Pillar 1 — ROCE Base Multiple
- FTTCP ROCE forward verdict: **RECOVERING (40–60%, 12m)** (fttcp-deliberation).
- ROCE used: **28.3%** operational ex-surplus-cash (Override 1). FY[Y+2] NOT FOUND → blend defaults to current 28.3%.
- Continuous formula (Amendment 5): Base PE = 0.5 × 28.3 + 7.5 = **21.65x** (deliberation rounds to ~21.5x).
- ROCE recovery credited via: **Pillar 1 midpoint.** Strategic Premium ROCE re-rating **BARRED** (single-credit rule, Amendment 4).
- Amendment 4.5 (Normalized-ROCE anchor) does **not** apply: backward verdict is TEMPORARILY DEPRESSED and forward RECOVERING, but the operator has already anchored Pillar 1 on the operational (ex-cash) figure and FY[Y+2] is NOT FOUND; no pre-depression median + named unwind catalyst pair is cleanly evidenced, so the standard blend stands.

### Pillar 2 — Cash Conversion Multiplier
- Cumulative CFO/PAT −0.93; latest FY26 CFO/PAT −1.63; FCF negative. CARE: WC intensity structural, negative CFO since FY20 (verbatim quote, B10).
- Determination: **INDETERMINATE** (not overridden). Per framework and deliberation, INDETERMINATE never resolves to a clean pass; the **growth offset is BARRED**; the multiplier sits in the 0.65x (structural, CARE precedence) to 0.80x (growth-phase, no offset) band.
- **Multiplier applied: 0.65x** (conservative primary, CARE structural precedence). Upper rail 0.80x shown for range.
- Quality-adjusted base = 21.65 × 0.65 = **14.07x** (at 0.80x: 17.32x).

### Pillar 3 — Growth Visibility (decoupled, Amendments 4.1–4.2, combined cap +6x)
- **3a Growth Visibility:** qualifiers met = SOM-implied revenue CAGR 35.7% (≥20%, capacity runway MASSIVE) **and** management delivery grade B. Two qualify → **+2x**. (Order book / capex-embedded growth NOT documented.)
- **3b Moat Formation:** EM 23 (<25) → **+0x**.
- **3c Duration:** no documented order book / contracted tenor ≥2.5yr → **+0x**.
- Pillar 3 total = **+2x** (shared macro catalyst flagged).

### Strategic Premium
- No regulatory monopoly; certifications attainable by any compliant competitor (B07). ROCE re-rating barred (credited in Pillar 1). **+0x.**

### UA Multiplier
- Qualifiers: listed <12 months (347 days) FAIL; Gate 0 core 48 <60 AND EM 23 <25 FAIL; FII+DII 3.94% ≥3% FAIL. **all_met = false → UA NOT applied** (F2 = F).

### Four-Pillar Summary (Track 2, additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | 0.5×28.3+7.5 | 21.65x |
| B. Cash Multiplier | 0.65x (INDETERMINATE, offset barred) | 0.65x |
| C. Quality-Adjusted Base | 21.65 × 0.65 | 14.07x |
| D. Growth Visibility (3a+3b+3c) | +2 +0 +0 | +2x |
| E. Strategic Premium | barred / none | +0x |
| F. Raw Destination PE | 14.07 + 2 + 0 | **16.07x** |
| F2. UA-Adjusted | UA not applied | 16.07x |
| G. Sector Cap | Recycling/Manufacturing | 25x |
| H. Mechanical Final (min(F2,G)) | | **16.1x** |

**Track 2 additive mechanical destination = 16.1x** (±7.5% → 14.9x–17.3x). At cash 0.80x the additive rises to ~19.3x.

### RRM Dual-Track (Track 1)
- Base r (small/micro-cap) = 14%. Adjust up for governance CAUTION + FLAG-CASH + INDETERMINATE cash + MODEST durability → **r = 15.5%** (bounded [9%,18%]).
- RRM = 1 + (13.5 − 15.5) × 0.12 = 1 − 0.24 = **0.76** (percentage-point reading, Amendment 4.4; bounds ×0.70–×1.60 OK).
- Track 1 destination = Fundamental Base PE (Pillar 1 ROCE base 21.65x) × RRM 0.76 = **16.45x ≈ 16.5x**, capped at 25x → 16.5x (±7.5% → 15.2x–17.7x). Cash and governance quality are priced through r here rather than as additive haircuts.

### Track divergence
- Track 1 (RRM) mid 16.5x vs Track 2 (additive) mid 16.1x → **divergence ~2.4%** (<15%). The two mechanical tracks converge on ~16x.

### GOVERNING DESTINATION PE
The operator override (fttcp-deliberation Overrides 2 & 4) sets the destination/exit PE at **20x on a forward basis (20x × projected FY30 EPS, applied at the FY29 exit)**. This supersedes the ~16x mechanical stack (both tracks). It sits below the 25x Recycling/Manufacturing sector cap, so it is admissible. **20x governs fair value and the Hurdle.** Destination PE range (±7.5% around 20x) = 18.5x–21.5x, still under the 25x cap.

🛑 *Checkpoint: Section 1 complete. Mechanical four-pillar ~16.1x additive / ~16.5x RRM; operator-governing exit PE 20x forward. Current PE ~55x. Hurdle computed in Section 4.*

---

## SECTION 2 — EARNINGS PROJECTIONS

Shares held constant at 11.401 Cr (asset-light, IPO complete, no dilution modeled). FY26 = Year 0.
Exit convention (Override 4): FY29 exit price = 20x × **FY30** EPS.

### 2A/2B assumptions (all below guidance / SOM / history; conservative bias)

| Driver | Bear | Base | Bull |
|---|---|---|---|
| Revenue growth FY27 / FY28 / FY29 / FY30 | 18 / 12 / 10 / 8% | 25 / 22 / 20 / 18% | 30 / 28 / 25 / 22% |
| Logic | Memory/component supercycle normalizes early; forced destocking; margin reversion to 15–17% GM | Guidance-consistent FY27 (25%, sandbagging track record), decelerating as base scales; below SOM 35.7% | Supercycle sustains to ~2028; distributor (Ingram/Supertron) + EU/US convert; below history 40.6% |
| PAT margin FY27 / FY28 / FY29 / FY30 | 6.5 / 6.0 / 5.8 / 5.8% | 7.48 / 7.7 / 7.9 / 8.0% | 7.6 / 8.2 / 8.6 / 9.0% |
| Margin logic | Component prices reverse; write-down risk | +50bps FY27 (guidance) then modest operating leverage, capped by thin-GM/FLAG-MARGIN | Mix + leverage; still below peers' 27–47% GM structurally |

### 2C EPS path (Rs)

| | FY26 (0) | FY27 (1) | FY28 (2) | FY29 (3, exit) | FY30 (4, exit-EPS) |
|---|---|---|---|---|---|
| **Bear** Revenue (Cr) | 1,891.08 | 2,231.5 | 2,499.3 | 2,749.2 | 2,969.1 |
| Bear PAT (Cr) | 132.02 | 145.05 | 149.96 | 159.45 | 172.21 |
| **Bear EPS** | 11.58 | 12.72 | 13.15 | 13.99 | **15.11** |
| **Base** Revenue (Cr) | 1,891.08 | 2,363.9 | 2,883.9 | 3,460.7 | 4,083.6 |
| Base PAT (Cr) | 132.02 | 176.82 | 222.06 | 273.39 | 326.69 |
| **Base EPS** | 11.58 | 15.51 | 19.48 | 23.98 | **28.65** |
| **Bull** Revenue (Cr) | 1,891.08 | 2,458.4 | 3,146.8 | 3,933.4 | 4,798.8 |
| Bull PAT (Cr) | 132.02 | 186.84 | 258.03 | 338.28 | 431.89 |
| **Bull EPS** | 11.58 | 16.39 | 22.63 | 29.67 | **37.88** |

**EPS CAGR:** Base FY26→FY29 = 27.6%; Base FY26→FY30 = **25.5%**. Bull FY26→FY30 = **34.5%**. Bear FY26→FY30 = 6.9%.

### 2D Sanity checks

| Check | Result | Pass |
|---|---|---|
| Revenue faster than capacity? | 150k units/mo delivered, 46 countries; SOM MASSIVE; base FY30 rev 4,084 Cr well inside SOM 5yr 11,154 Cr | Yes |
| Margins require the unprecedented? | Base PAT margin 8.0% by FY30 vs 6.98% now; +102bps over 4y; conservative vs guidance | Yes |
| ROCE stays >15%? | Operational base ~28.3%, thin capex; yes in base/bull | Yes |
| FCF funds growth without excess debt? | **No** — CFO/FCF negative, WC-funded. FLAG-CASH; caps at PROCEED WITH CAVEATS | **Flagged** |
| EPS growth operational, not engineered? | Yes — revenue × margin, no buyback/dilution games | Yes |
| Year-3 ROCE consistent with FTTCP RECOVERING? | Yes — base holds ~28% operational, consistent with RECOVERING credited in Pillar 1 | Yes |
| **SOM cross-check** | Base 3yr revenue CAGR 22.3% **< SOM-implied 35.7%** → **consistent** (below ceiling) | Yes |

🛑 *Checkpoint: Section 2 complete. Base FY30 EPS Rs 28.65; bear 15.11; bull 37.88.*

---

## SECTION 3 — VALUATION METHODS APPLIED

### PRIMARY — P/E (exit governed by operator 20x forward)

FY29 exit target = 20x × FY30 EPS:

| Scenario | FY30 EPS | Exit (20x) = FY29 target | 3yr CAGR from CMP 634 |
|---|---|---|---|
| Bear | 15.11 | **Rs 302** | −21.9% 🔴 |
| Base | 28.65 | **Rs 573** | −3.3% 🔴 |
| Bull | 37.88 | **Rs 758** | +6.1% 🔴 |

For transparency, the mechanical ~16x stack would give: bear Rs 242 / base Rs 458 / bull Rs 606 — even lower. The operator 20x is the more generous, governing anchor and still lands base fair value **below** CMP.

**P/E fair value range (governing, 20x): Rs 302 (bear) – Rs 573 (base) – Rs 758 (bull).**

### SECONDARY — EV/EBITDA (cross-check)
Exit EV/EBITDA ≈ 0.6–0.7× of 20x PE ≈ 12–14x. Base FY30 EBITDA ≈ margin ~12% × 4,083.6 = ~490 Cr → EV ~490×13 = 6,370 Cr; less FY29 net debt (assume ~350 Cr, WC-funded) → equity ~6,020 Cr / 11.401 = **~Rs 528**. Consistent with the P/E base ~Rs 573 (within 8%). Cross-check agrees: fair value clusters Rs 530–575 base, below CMP.

🛑 *Checkpoint: Section 3 complete. Both methods place base fair value (Rs 528–573) below CMP Rs 634.*

---

## SECTION 4 — TRIANGULATION, HURDLE, ENTRY, VERDICT

### 4A Triangulated fair value (Year-3, FY29)
Operator 20x forward governs; both dual-tracks collapse to it. P/E 85% (573) + EV/EBITDA 15% (528) → **base ~Rs 566**. Rounded to the governing P/E anchor for consistency: **Bear 302 / Base 573 / Bull 758.**

### 4B Methods agreement
P/E and EV/EBITDA agree within ~8% at base; same direction (both below CMP). No outlier. P/E trusted most (operator-set, earnings-driven).

### 4C Return at CMP 634 (3-year to FY29)

| Scenario | FY29 target | Total return | CAGR | Meets 25%? |
|---|---|---|---|---|
| Bear | 302 | −52.4% | −21.9% | 🔴 |
| Base | 573 | −9.6% | −3.3% | 🔴 |
| Bull | 758 | +19.6% | +6.1% | 🔴 |

### 4D Probability-weighted expected return (grade B → 25/50/25)

| Scenario | Prob | 3yr CAGR | Weighted |
|---|---|---|---|
| Bear | 25% | −21.9% | −5.48% |
| Base | 50% | −3.3% | −1.65% |
| Bull | 25% | +6.1% | +1.53% |
| **Expected CAGR** | 100% | | **−5.6%** |

### HURDLE RATIO (governing 20x, forward basis)
Current trailing PE = 634 / 11.58 = **54.75x**. Destination PE = 20x.
HR = (FY30 EPS ÷ FY26 EPS) × (Destination PE ÷ Current PE):
- **Base:** (28.65/11.58) × (20/54.75) = 2.474 × 0.3653 = **0.90**
- **Bull:** (37.88/11.58) × (20/54.75) = 3.271 × 0.3653 = **1.20** (grade B permits bull use)

Threshold (Tier A) = 1.953. **HR(Base) 0.90 < 1.953 AND HR(Bull) 1.20 < 1.953 → STOP.** Even on bull-case earnings, exiting at 20x after entering at ~55x cannot deliver 25% over three years. The de-rating from 55x to 20x overwhelms the 2.5–3.3x earnings growth. This is a price problem, not a business problem.

### Two-tier hurdle assignment
**Tier A (25% CAGR, divisor 1.953).** GNG fails Tier B quality gates (structural/INDETERMINATE FLAG-CASH present; Gate 0 core 48 not GOOD), so Tier A stands. Verdict card line: **Tier: A | Hurdle: 25%.**

### 4E Entry price (Tier A, off base fair value Rs 573)

| Calculation | Value |
|---|---|
| Base fair value (FY29) | Rs 573 |
| 25% CAGR entry = 573 ÷ 1.953 | **Rs 293** |
| 30% CAGR entry (extra safety) = 573 ÷ 2.197 | Rs 261 |
| MoS price = 20% below 25% entry (293 × 0.80) | **Rs 235** |
| Ideal entry range | **Rs 261 – Rs 293** |

### 4F Risk-reward at CMP
Bull upside +19.6%; bear downside −52.4% → **upside/downside 0.37x** (base upside is negative). Far below the ≥2x requirement. At CMP the asymmetry is adverse.

### 4G Exit-multiple validation
- Year-3 ROCE (~28% operational base) justifies Pillar 1 and matches RECOVERING verdict — pass.
- CFO/PAT trajectory does **not** yet justify a clean cash multiplier — INDETERMINATE; 0.65x applied; caps disposition at PROCEED WITH CAVEATS — flagged.
- Catalyst (supercycle + FY27 delivery) plausibly fires by FY29 base — pass, but SHARED-MACRO-CATALYST single point of failure.
- Strategic premium correctly zero (single-credit respected).
- UA ordering correct — not applied (qualifiers fail).
- The operator 20x is more generous than the ~16x mechanical stack, so no downward revision is warranted; if anything the mechanical build argues the exit PE is generous, reinforcing the STOP at CMP.

### 4H VERDICT CARD

**Tier: A | Hurdle: 25% | Disposition cap: PROCEED WITH CAVEATS (INDETERMINATE cash)**

- **CMP** Rs 634 | **Market cap** Rs 7,227 Cr | **Trailing PE** ~55x
- **Four-pillar (mechanical):** ROCE base 21.65x (RECOVERING, ROCE 28.3% operational, credited via Pillar 1) × cash 0.65x (INDETERMINATE, offset barred) = 14.07x quality base; +2x growth (3a); +0x strategic; UA off; **raw 16.1x**, sector cap 25x.
- **RRM track:** r 15.5%, RRM 0.76, destination **16.5x** (converges with additive; divergence ~2.4%).
- **GOVERNING exit PE:** **20x forward (20x × FY30 EPS at FY29 exit)** — operator Overrides 2 & 4, below 25x cap.
- **Fair value (FY29):** Bear Rs 302 | Base Rs 573 | Bull Rs 758.
- **Hurdle Ratio:** Base 0.90 / Bull 1.20 → **STOP** (25% infeasible even on bull earnings at current price).
- **Expected CAGR (prob-weighted, grade B):** **−5.6%.**
- **Upside/downside at CMP:** 0.37x (<2x).
- **Entry range:** Rs 261 – Rs 293 | **MoS price:** Rs 235.
- **DECISION:** **AVOID (on valuation) at Rs 634.** Becomes actionable only in the Rs 261–293 entry zone (MoS Rs 235), and only if the entry-conjunction holds (no thesis-broken trigger firing as price falls) and the cash flag resolves. The thesis is not dead; the price is wrong by ~2.2x.
- **Key assumptions that move it:** ▲ supercycle sustains + margin holds → bull Rs 758 (still only +6% CAGR at CMP); ▼ component prices normalize + WC write-down → bear Rs 302. The exit multiple is fixed at 20x by operator override; the swing is entirely EPS.
- **Exit framework:** target exit FY29 at 20x forward FY30 EPS; thesis broken if FY27 revenue growth <20% or gross margin reverts <15% or first statutory cash flow confirms structural leak; PE compression floor already at the governing 20x.

**ONE-LINE THESIS:** GNG can grow EPS from Rs 11.58 to ~Rs 28.65 (FY30) on the memory/component supercycle, but at Rs 634 (~55x trailing) a governing 20x forward exit yields a Rs 573 base target = negative 3-year CAGR (Hurdle STOP); AVOID on valuation until the Rs 261–293 entry zone, cash quality still INDETERMINATE.

🛑 *Valuation complete. Mechanical four-pillar ~16x; operator-governing exit PE 20x forward. Hurdle Ratio STOP (base 0.90, bull 1.20). Entry Rs 261–293. Decision: AVOID (on valuation) at CMP.*

---

```yaml
stage: B11-valuation
company: "EBGNG"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
input_gaps: [ebitda_fy26_reconstructed, fy27_fy30_eps_projected, fy_y2_roce_not_found, peer_medians_not_found]
flags:
  - {type: FLAG-CASH, applied_multiplier: 0.65, note: "INDETERMINATE; growth offset BARRED; caps disposition at PROCEED WITH CAVEATS"}
  - {type: FLAG-PROMOTER, note: "CAUTION — KKOC multi-role RPT + Rs 305.32M tax demand"}
  - {type: SHARED-MACRO-CATALYST, note: "Memory/component supercycle drives revenue, margin and Rs 743 Cr inventory bet"}
  - {type: FLAG-MARGIN, note: "Gross margin ~12% trails peers 27-47%"}
  - {type: FLAG-GATE0, note: "Core 48/100 AVERAGE, Block B 0/20"}
framework_versions: "Master v3.3 / Section 1B v3.3 / FTTCP v1.2"
destination_pe:
  track1_rrm: {low: 15.2, mid: 16.5, high: 17.7, r_used: 15.5, rrm: 0.76}
  track2_additive: {low: 14.9, mid: 16.1, high: 17.3}
  divergence_pct: 2.4
  governing_track: "Operator override 20x forward (deliberation Overrides 2 & 4) supersedes both ~16x mechanical tracks; sets fair value, entry and Hurdle."
pillar_detail:
  roce_used: 28.3
  roce_base: 21.65
  roce_recovery_route: "pillar1-midpoint"
  cash_multiplier: 0.65
  structural_or_growth: "INDETERMINATE"
  growth_offset: 0
  growth_premium: 2
  strategic_premium: 0
  shared_catalyst_flag: true
  ua_applied: false
  sector_cap_used: 25
hurdle_ratio: {base: 0.90, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 302, base: 573, bull: 758}
  track2: {bear: 302, base: 573, bull: 758}
expected_cagr_prob_weighted: -5.6
entry_range: {low: 261, high: 293}
mos_price: 235
upside_downside_ratio: 0.37
decision: "AVOID (on-valuation) at CMP Rs 634; actionable only in entry zone Rs 261-293, MoS Rs 235"
unresolved_inputs_used:
  - "EBITDA FY26 NOT FOUND -> reconstructed EBIT 190.15 + D&A 10.35 = Rs 200.50 Cr (EV/EBITDA cross-check only)"
  - "FY[Y+2] ROCE NOT FOUND -> RECOVERING blend defaults to current operational 28.3% (no uplift)"
  - "FY27-FY30 EPS NOT FOUND -> projected from FY26 EPS 11.58 + guidance, all below guidance/SOM/history"
  - "Peer P/E, EV/EBITDA, P/B medians NOT FOUND -> exit PE rests on Section 1B/operator override, no peer triangulation"
som_cagr_crosscheck: "consistent — base 3yr revenue CAGR 22.3% below SOM-implied 35.7%"
one_line_thesis: "GNG can grow EPS from Rs 11.58 to ~Rs 28.65 (FY30) on the memory supercycle, but at Rs 634 (~55x trailing) a governing 20x forward exit gives a Rs 573 base target = negative 3yr CAGR (Hurdle STOP); AVOID on valuation until Rs 261-293, cash quality still INDETERMINATE."
```
