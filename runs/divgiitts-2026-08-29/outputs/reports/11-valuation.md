# STAGE 11 — ROLE 1 DUAL-TRACK VALUATION — DIVGIITTS

**Company:** Divgi Torqtransfer Systems Ltd (DIVGIITTS)
**Run:** divgiitts-2026-08-29 | **Model:** claude-opus-4-8
**Framework:** Master v3.6 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9 / FTTCP v2.1
**Entity count:** 1 (single-entity pass; no consolidated split; entity-count gate not triggered)

> **Authority note.** The operator approved the destination PE base (30x), the earnings
> basis (FY27 forward operating EPS, treasury stripped) and the pillar build at the FTTCP
> pillar-approval gate (B10.operator_approved_pillars). Per Master v3.6 consumption clause
> and v3.9 Amendment 20.9, this run VALUES on the operator-approved base. Where my
> independent Section 1B derivation diverges, I REPORT the divergence plainly and value on
> the approved base. I never silently overwrite the operator's call.

---

## UNIT DISCIPLINE (carried from B10.orchestrator_unit_correction)

Every absolute Rs figure from the audited AR/results is in **Rs MILLION**; divided by 10 for
Rs Cr per B10.key_figures_corrected_to_cr: revenue Rs 352.89 Cr FY26, net cash Rs 294.38 Cr,
EV ~Rs 3,300 Cr. **Per-share figures are correct** (operating EPS Rs 24 FY27, net cash Rs 95-96/share,
reported EPS Rs 15.34 FY26). The valuation runs on the operator-approved per-share base; fair
value is unaffected by the unit mislabel. (B10 analyst_note item 6.)

---

## SECTION 1A: METHOD SELECTION & JUSTIFICATION

### Method Suitability Matrix

| Method | Fit for DIVGIITTS | Suitable? | Weight |
|---|---|---|---|
| **P/E (operating)** | Build-to-spec driveline component maker; clean operating earnings once treasury income (Rs 222.83 Mn ≈ Rs 22 Cr, on ~Rs 294 Cr cash pile) is stripped. Framework default and operator-approved primary. | YES — PRIMARY | 70% |
| **EV/EBITDA** | Capital-heavy manufacturing in a capex cycle (FY26 capex Rs 44.32 Cr > D&A Rs 29.24 Cr). Neutralises the cash pile that wrecks reported P/E. Must use OPERATING EBITDA and add cash in the bridge. | YES — SECONDARY | 20% |
| **P/B** | Asset-heavy manufacturer; BVPS Rs 207.72 (B10). Book misses design-win IP and OEM qualification value; cross-check only. | Partial — TERTIARY | 10% |
| PEG | Growth predictable only 1-2 yrs (auto cycle + 3-quarter EV-SOP slip); base too volatile. | No | — |
| DCF | FY26 FCF **negative** (Rs -3.24 Cr); high terminal-value sensitivity on an early-cycle capex build. Fails the DCF suitability test. | No | — |
| EV/Sales, EV/Capacity, NAV, DDM, P/AUM, P/EV | Not a commodity/capacity, holding, dividend, lender or insurer. | No | — |

**Final selection.** PRIMARY P/E (operating EPS × Section 1B exit multiple) 70%; SECONDARY
EV/EBITDA 20%; TERTIARY P/B 10%. Two methods applied with weighted triangulation (below).
The exit multiple is the framework default primary, not the only method (override 6 satisfied).

### Converter classification (v3.7 Amendment 17.0)

**NON-CONVERTER.** DIVGIITTS is a spec-in, design-win driveline/transmission supplier (torque
transfer cases, DCT, EV transmissions). Raw material (steel/aluminium castings) is not a quoted
spread; pricing rests on OEM qualification (PPAP) and switching cost, not cost-plus on a traded
commodity. Amendments 17.1-17.4 do NOT bind. **But the demand side is CYCLICAL** (auto OEM
volumes), so the Section 2B cyclical margin override applies (base = full-cycle margin, bear =
trough, bull = peak). The CLAUDE.md converter bar on spot-year ROCE does not apply (not a converter).

---

## SECTION 1B: FOUR-PILLAR EXIT MULTIPLE WORKSHEET (BOTH TRACKS)

FTTCP v2.1 ran before this role (B10). ROCE forward verdict **RECOVERING** is the sole Pillar 1
authority. Debt Capacity: effectively debt-free (total debt Rs 0.18 Cr; COMFORTABLE by inspection).

### Pillar 1 — ROCE Base Multiple

- **Normalization route (v3.5.1):** the distortion is a post-IPO cash pile (~Rs 294 Cr net cash)
  inflating capital employed — a **denominator bloat**. By the v3.5.1 route-selection rule that is
  **Route A (operational ROCE, strip non-operating cash both sides)**, not Route B (numerator/pre-cycle).
  B10/deliberation labelled it "Route B cash-strip." **Label divergence flagged**; the mechanism
  (treasury stripped both sides → 20% ROCE) and the resulting base are unchanged either way. Single
  credit: recovery credited via Pillar 1; Strategic Premium ROCE re-rating **barred** (0x).
- **FTTCP ROCE forward verdict:** RECOVERING.
- **ROCE used (operator-approved, sole authority):** 20% (treasury stripped both sides). Blended,
  fair-case; B10 notes it rests on a 24% FY29 op margin above the 20-22% guide (at guide, ROCE 16-19%).
- **Base PE (operator-approved):** **19x.**

> **DIVERGENCE REPORTED (valued on approved base).** The continuous formula (Amendment 11) at
> ROCE 20% gives Base PE = 0.5×20 + 7.5 = **17.5x**, not 19x. 19x corresponds to ROCE ~23% on the
> formula. The operator-approved 19x therefore embeds an ROCE anchor ~3pp above the stated 20%.
> My base-case projection (below) lands operating ROCE at ~16-17% (FY29 op PAT ~Rs 94 Cr / op CE
> ~Rs 575 Cr = 16.3%), which the formula would price at ~15.5-16x. I value on the operator's 19x
> and flag that both the ROCE (20% fair-case) and the base PE (19x) sit at the optimistic edge.

- **ROCE recovery credited via:** Pillar 1 midpoint (single-credit; Strategic Premium route barred).

### Pillar 2 — Cash Conversion Multiplier

- Cumulative CFO/PAT FY20-26: 0.969 (B10). Latest FY26 CFO/PAT: **0.876** (B10). FCF FY26: Rs -3.24 Cr
  (negative, capex cycle).
- No credit rating exists (finding, not gap) → structural-vs-growth determination is **INDETERMINATE**
  (B10; no rating rationale). Per the framework, the more conservative multiplier is used and stated.
- **Cash multiplier applied: 1.00x (INDETERMINATE, neutral). No growth offset** (no rating rationale
  exists to license one; a finding, not a gap). FLAG-CASH carried.
- **Quality-Adjusted Base = 19x × 1.00x = 19x** (operator base) [formula-strict: 17.5x × 1.00 = 17.5x].

### Pillar 3 — Growth Visibility Premium

- Growth-eligibility gate (Amendment 16): base-case ROCE ~16% crosses the ~13-14% minimum → **growth
  premium eligible YES**.
- EM 30 (STRENGTHENING, 30/92, B07). Primary catalyst Sigma EV transmission SOP — **slipped 3
  consecutive quarters, proof gate NOT fired** (B07/B10). Evidence mostly documented (61%).
- Table default for EM 30-39 + catalyst 0-12m + mixed evidence would be +2 to +3x. **Operator docked
  to +1x** for the 3-quarter catalyst slip and proof-not-fired. **Growth premium applied: +1x**
  (operator-approved).
- FTTCP Signal Gate (override 5): the growth catalyst cites downstream candidates (all unverified,
  Role 5.5 outside pipeline): Sigma EV SOP; Indonesia Scorpio Pik Up CY2026 exports (35,000-unit
  program); BorgWarner tech-licensing; named NA OEM automatic-transmission decision; Project
  Mayflower capex/hiring; Mahindra/Tata 4x4 monthly sales (B09). demand_externally_verifiable =
  true → composite NOT capped at DEEP WATCH on that ground. Catalyst magnitude caps at MODERATE
  (evidence-thin on the SOP; repeated slips).
- Shared-catalyst flag: **false**. ROCE recovery is credited via cash-strip normalization (Pillar 1),
  a different lever from the SOP/Indonesia growth catalyst.

### Strategic Premium

- **+0x.** ROCE re-rating optionality barred by single-credit (recovery credited in Pillar 1). No
  licence monopoly; OEM qualification is a moat but not documented pricing-power scarcity → 0x
  (operator-approved).

### Undiscovered Alpha Multiplier

- Qualifiers: listed ≥12m YES (Mar-2023 IPO); Gate0≥60 OR EM≥25 YES (EM 30); **FII+DII <3% NO**
  (FII 1.86% + DII 26.16% = 28.02%). **all_met = false → UA NOT applied** (F2 = F).

### Sector Reality Cap

- Sector: Auto components / industrial products. Framework cap **25x**.
- **OPERATOR OVERRIDE to 30x** (DIVGIITTS this run only, peer-anchored). Recorded as an **operator
  override, not a framework change**. FLAG-SECTOR-CAP-OVERRIDE carried (adds ~Rs 120/share vs the
  25x default per B10 analyst_note).

### Four-Pillar Summary (Track 2 — Additive)

| Step | Calculation | Value |
|---|---|---|
| A. ROCE Base | ROCE 20% → operator 19x [formula-strict 17.5x] | 19.0x |
| B. Cash Multiplier (effective) | 1.00x + offset 0 | 1.00x |
| C. Quality-Adjusted Base | A × B | 19.0x |
| D. Growth Visibility Premium | EM 30 + slipped catalyst → operator +1x | +1.0x |
| E. Strategic Premium | single-credit bars ROCE re-rating | +0.0x |
| F. Raw Destination PE | C + D + E | **20.0x** |
| F2. UA-Adjusted Raw PE | no UA (FII+DII 28%) | 20.0x |
| G. Sector Cap | auto components 25x → operator override | 30.0x |
| G2/G3. Category-Break Override | NOT invoked | 30.0x |
| **H. Final Destination PE (additive track)** | **min(F2, G3) = min(20, 30)** | **20.0x** |

**Track 2 (additive) destination PE: 20.0x, range ±7.5% → 18.5x to 21.5x.**

### RRM Dual-Track Derivation (Track 1)

- r-adjustment worksheet: r base 14% (small/micro, operator-fixed "standard band"); durability adj
  0 (Unproven band owns short-record risk per 12C; listed 3.4 yrs); governance adj 0 held by operator;
  cyclical surcharge — capped at +0.75 per 12B if applied, held at 0 by operator; complexity adj —
  Amendment 13 triggers (dense RPT, subsidiary/disclosure opacity: FLAG-RPT-COMPLETENESS,
  FLAG-SUBSIDIARY-CONTRADICTION) would add +0.5, held at 0 by operator; cash-conversion r-UP none
  (12A); short-record r-UP none (12C). **Final r = 14% (operator-fixed, standard band).**
- RRM = 1 + (13.5 − 14) × 0.12 = 1 − 0.06 = **0.94** (percentage-point reading, Amendment 4.4).
- **Track 1 (RRM) destination PE = 19.0x × 0.94 = 17.9x**, range ±7.5% → 16.5x to 19.5x.

> **CONSERVATIVE FLAG.** A complexity/governance-adjusted r (+0.5 complexity, Amendment 13) = 14.5%
> gives RRM 0.88 → Track 1 15.8x; at r 15% → 15.6x. The operator held r at the standard 14% band.
> Adjusting for the flagged disclosure opacity would push the framework floor LOWER, not higher.

### Relative PE expression (Amendment 15)

Absolute governing H 30x | market PE ~22-24x (macro, not injected — NOT FOUND live) | relative
destination ~1.3x. FTTCP Module B8 re-rating potential is not carried as HIGH; the 30x sits above,
not below, the framework additive 20x, so the relative expression is a check that 30x is NOT
assuming a re-rating the framework pillars support. It does not.

### Destination PE — three-way reconciliation (GOVERNING vs floor)

| Track | Destination PE (mid) | Range | Role |
|---|---|---|---|
| Track 1 — RRM (r=14%) | 17.9x | 16.5-19.5x | Framework floor / cross-check |
| Track 2 — Additive Four-Pillar | 20.0x | 18.5-21.5x | Framework floor / cross-check |
| **GOVERNING — operator override** | **30.0x forward** | at overridden cap | **Sets exit multiple + entry zone** |

- Two framework tracks diverge (20 vs 17.9) by **11.7% (<15%)**; between them the more conservative
  (RRM 17.9x) would set entry.
- **BOTH framework tracks sit ~50% BELOW the governing 30x.** The operator override lifts the exit
  multiple 50% above the framework's own additive output, on a peer anchor. **FLAG-MULTIPLE-OVERRIDE.**
  Per override 12/Amendment 20.9 the operator-approved 30x GOVERNS; the framework tracks are retained
  as the floor/cross-check.

### Hurdle Ratio (Amendment 2 / v3.3)

Basis-consistent (18.1): exit multiple 30x is an **ex-cash operating** multiple (cash added
separately). Current PE must match: **current ex-cash operating PE = (1175 − 95) / 24 = 45.0x**
(incl-cash 48.9x; ex-cash is the like-for-like figure).

- Base operating EPS CAGR (FY27 Rs 24 → FY30 Rs 34.3, base projection): **12.6%.**
- **HR(base) = (1.126)³ × (30 / 45) = 1.429 × 0.667 = 0.95.** FAIL (< 1.953).
- Bull operating EPS CAGR (grade B allows bull face value): FY30 Rs 45.2 → **23.5%.**
- **HR(bull) = (1.235)³ × (30 / 45) = 1.883 × 0.667 = 1.26.** FAIL (< 1.953).
- Required operating EPS CAGR to clear 1.953 from CMP = **~43%.** Even bull (23.5%) falls short.

**HURDLE VERDICT: STOP.** The 25% CAGR is infeasible from CMP Rs 1,175 even on bull-case earnings.
Per the framework, remaining sections are completed for the record and the verdict card reads
AVOID-on-valuation.

🛑 CHECKPOINT (pipeline continues): Destination PE governing 30x (framework floor 17.9-20x).
Current ex-cash PE 45x. Hurdle Ratio 0.95 base / 1.26 bull → STOP.

---

## SECTION 2: EARNINGS & CASH FLOW PROJECTIONS (Year 0 = FY27, to Year 4 = FY31; v3.8 18.0)

Cyclical override (2B): base = full-cycle op margin ~22%; bear = trough ~17%; bull = peak ~28%
(B10 / task cash-flow facts, clean operating, treasury stripped). **The FY27 operator base uses a
24% fair-case margin, 2pp above the 22% through-cycle midpoint — flagged optimism.** Fade horizon
(Amendment 14): EM STRENGTHENING → growth fades by Year 4. Year-4 industry-growth anchor = **12%
(NAMED ASSUMPTION, 18.0** — corpus holds no India transfer-case industry growth rate; B09 TAM is
apportionment-proxy, confidence Low).

### 2C. Base-case projection (operating, treasury stripped)

| Line (Rs Cr unless EPS) | Yr0 FY27 | Yr1 FY28 | Yr2 FY29 | Yr3 FY30 | Yr4 FY31 |
|---|---|---|---|---|---|
| Revenue | 545 | 632 | 733 | 836 | 936 |
| Revenue growth | (base) | 16% | 16% | 14% | 12% |
| Op EBITDA margin | 24.0% | 23.5% | 23.0% | 22.5% | 22.0% |
| Op EBITDA | 130.8 | 148.6 | 168.7 | 188.1 | 206.0 |
| D&A | 33 | 38 | 43 | 48 | 53 |
| Op EBIT | 97.8 | 110.6 | 125.7 | 140.1 | 153.0 |
| Op PAT (tax 25.2%) | 73.2 | 82.7 | 94.0 | 104.8 | 114.4 |
| **Op EPS (Rs)** | **24.0** | **27.0** | **30.7** | **34.3** | **37.4** |
| Est. op ROCE (PAT/op CE) | ~20%* | ~17% | ~16% | ~17% | ~17% |

*FY27 op ROCE at the operator's fair-case; base projection lands ~16-17% from FY28 (op CE ~Rs 575 Cr
FY29). This is the flagged gap vs the 20% Pillar 1 ROCE.

Revenue base CAGR (FY27-30) 15.3% vs **B10 SOM-implied 16.1%** → **CONSISTENT** (assumption not cut).

### 2A/2B scenario operating EPS (FY27 snapshot, revenue Rs 545 Cr held, margin flexed)

| Case | Op EBITDA margin | Op EBITDA | Op EBIT | Op PAT | **Op EPS FY27** |
|---|---|---|---|---|---|
| Bear (trough) | 17% | 92.65 | 59.65 | 44.6 | **14.6** |
| Base (fair-case) | 24% | 130.8 | 97.8 | 73.2 | **24.0** |
| Bull (peak) | 28% | 152.6 | 119.6 | 89.5 | **29.3** |

### 2D. Sanity checks

| Check | Result | Pass? |
|---|---|---|
| Revenue faster than capacity? | Shirwal + Mayflower capex funds the build | OK |
| Margins unprecedented? | Base 24% FY27 > 20-22% guide; fades to 22% | MARGINAL (flagged) |
| ROCE stays >15%? | Base ~16-17% | MARGINAL |
| FCF funds growth without new debt? | FY26 FCF -3.24 Cr; cash pile funds it | OK (near-term FCF negative) |
| EPS growth operational, not engineered? | Yes; treasury stripped | PASS |
| Implied market share realistic? | 15.3% CAGR vs SOM 16.1% | PASS |
| CFO/PAT consistent with Pillar 2 1.0x? | 0.88x latest, INDETERMINATE neutral | PASS |
| Yr3 ROCE consistent with FTTCP RECOVERING Pillar 1? | Base ~16-17% at LOW edge of 20% fair-case | FLAG |

---

## SECTION 3: APPLY EACH VALUATION METHOD

Operating earnings only (FTTCP B4). Net cash enters the equity bridge at face (Rs 95/share), never
multiplied by the exit PE. **NEVER multiply reported EPS Rs 15.34 or Rs 28** (that prices the Rs 294 Cr
treasury cash at 30x its yield).

### PRIMARY — P/E (operating EPS × exit multiple + net cash), GOVERNING 30x

Fair value = op EPS × 30 + Rs 95 net cash/share:

| Case | Op EPS FY27 | × 30x | + net cash | **Fair value (Rs)** |
|---|---|---|---|---|
| Bear | 14.6 | 438 | 95 | **533** |
| Base | 24.0 | 720 | 95 | **815** |
| Bull | 29.3 | 879 | 95 | **974** |

**Base fair value Rs 815 = operator-approved (Rs 24 × 30 + Rs 95).** CMP Rs 1,175 = **44% above**
base fair value; above even the bull Rs 974.

**Framework-floor P/E fair values (for the record):**

| Track | Multiple | Bear | Base | Bull |
|---|---|---|---|---|
| Additive floor | 20x | 387 | 575 | 681 |
| RRM floor | 17.9x | 356 | 525 | 619 |

On the framework's own multiple, base fair value is **Rs 525-575** — less than half of CMP.

### SECONDARY — EV/EBITDA (operating EBITDA, cash in bridge)

- FY27 operating EBITDA Rs 130.8 Cr. The governing 30x P/E ⇔ implied 16.8x EV/op-EBITDA
  (fair EV Rs 2,198 Cr / 130.8), rich for auto components (typical exit 10-14x).
- At a peer-reasonable **13x**: fair EV Rs 1,700 Cr + net cash Rs 294 Cr = Rs 1,994 Cr / 3.0582 =
  **Rs 652/share.** Corroborates: CMP Rs 1,175 is expensive; the 30x P/E embeds a stretched EV/EBITDA.

### TERTIARY — P/B (cross-check)

- BVPS Rs 207.72; market P/B 5.65x at CMP. A fair ~3.0-3.5x for a mid-teens-ROCE manufacturer →
  Rs 620-725. Below CMP. Book misses design-win IP; cross-check only.

### Weighted triangulation

| Method | Weight | Fair value (base) |
|---|---|---|
| P/E (governing 30x) | 70% | 815 |
| EV/EBITDA (13x) | 20% | 652 |
| P/B (3.25x) | 10% | ~675 |
| **Weighted** | 100% | **~763** |

Governing base fair value = **Rs 815** (operator-approved primary P/E). Secondary/tertiary methods
sit BELOW it (Rs 652-675) and all sit far below CMP Rs 1,175. Every method points to overvaluation.

---

## STEP 1C: RELATIVE VALUATION CROSS-CHECK (v3.9 Amendment 20)

**Live peer table: PENDING LIVE PEER TABLE.** Claude Code holds no live web access; per 20.1 /
override 11 the pipeline cannot populate or govern step 1C. Peers named (ENDURANCE, HAPPYFORGE,
SANSERA, SONACOMS); no live dated multiples fetched (memory-pulled multiples barred, Correction 6).

**Carried from the FTTCP deliberation only:** peer **downside line 27x forward**. Applying the 20.5
governance test to what is carried: the governing operator destination 30x is **ABOVE** the 27x peer
downside line, i.e. NOT more than 30% below any adjusted peer base. **The 30% test does NOT trigger;
the relative multiple does NOT govern.** Per 20.9 the operator-approved base binds regardless.
B10 records **both Amendment 20 gates fail** in the deliberation. **Result: pillar/operator base (30x)
governs; relative table is the cross-check.** A live peer table lands at Role 5.5 (claude.ai); this
slot re-runs there.

---

## SECTION 4: ENTRY, RISK-REWARD, FV PATH (Amendment 19), VERDICT

### Entry zone and MoS (governing 30x basis)

- Exit-consistent Year-3 fair value FV₃ (below) = Rs 1,109. **Entry (25% CAGR) = 1,109 / 1.953 = Rs 568.**
- **20% MoS on today's fair value Rs 815 = Rs 652.**
- **ENTRY ZONE Rs 570-650** (operator-approved; reconciles: low = 25%-CAGR entry on the Year-3 exit
  value; high = 20% MoS on today's fair value).
- **MoS price Rs 570** (evidence-scaled 30% below fair value Rs 815; EM STRENGTHENING with a
  3-quarter-slipped catalyst warrants the mid band, not 20%).

### Risk-reward from CMP Rs 1,175

| Reference | Value (Rs) | vs CMP |
|---|---|---|
| Bull fair value | 974 | −17.1% |
| Base fair value | 815 | −30.6% |
| Bear fair value | 533 | −54.6% |

No positive upside from CMP to any case. **Upside/downside ratio = (815 − 1,175) / (1,175 − 533) =
−0.56** (negative → overvalued; there is no favourable skew at CMP).

### 4D probability-weighted expected CAGR (grade B → 25/50/25)

Year-3 exit price = FY30 op EPS × 30x + tapered cash Rs 80 (cash deploys into Shirwal/Mayflower):

| Case | FY30 op EPS | Exit price (Rs) | 3-yr price CAGR from Rs 1,175 |
|---|---|---|---|
| Bear (25%) | 16.8 | 584 | −20.8% |
| Base (50%) | 34.3 | 1,109 | −1.9% |
| Bull (25%) | 45.2 | 1,436 | +6.9% |

**Prob-weighted expected CAGR from CMP = −4.4%.** Far below the 25% target. (Note: bear holds the
peak 30x multiple on trough earnings — generous; a de-rated bear multiple pushes this lower. From
the entry-zone midpoint ~Rs 610 the base case clears 25%, which is the point of the entry zone.)

### FV PATH TABLE (governing track = operator 30x, base case; Amendment 19.0)

Cash tapers 95 → 90 → 85 → 80 as it deploys; forward EPS rolled one year each step (18.1 symmetry):

| Point | Fwd op EPS | × 30x | + cash | **Fair value (Rs)** |
|---|---|---|---|---|
| Today (FY27 fwd) | 24.0 | 720 | 95 | **815** |
| End-Yr1 (FY28 fwd) | 27.0 | 810 | 90 | **900** |
| End-Yr2 (FY29 fwd) | 30.7 | 921 | 85 | **1,006** |
| End-Yr3 exit (FY30 fwd) | 34.3 | 1,029 | 80 | **1,109** |

**FV CAGR over the hold: 10.8% (today Rs 815 to end-Year-3 Rs 1,109, governing track, base case).**
→ **HYBRID (10-20%).**

**Decomposition (19.3).** Fair value grows because operating EPS compounds ~12.6% (Rs 24 → Rs 34.3),
dragged DOWN to 10.8% by the static/declining cash slice (Rs 95 → Rs 80, non-compounding as it
deploys) and by **no re-rating lever remaining** — the multiple already sits at the operator's 30x
ceiling. Return comes partly from FV growth, partly from any discount closing; the entry zone
matters proportionally. No SOTP option slices (no within-hold FV-step events; proof gate not fired,
EV/optionality leg valued at zero per B10).

### Recognition-gap resolution (override 13)

Current ex-cash operating PE **45x** already sits ABOVE the governing destination 30x AND far above
the TO-rung neighbourhood (R3 value-added supplier ~19x; even R4 ~21x, CLAUDE.md ladder). The
FROM→TO migration (R2 cost-advantaged converter → R3 value-added supplier) is worth a re-rating to
~19-21x on the framework; the market prices 45x. **The recognition gap is CLOSED and over-priced:
the re-rating engine is not merely spent, the market prices a DE-RATING headwind (45x → 30x).**
Return must ride EPS CAGR alone, and even 43% CAGR would be needed to clear the Hurdle from CMP —
infeasible. This feeds the STOP.

### Transition Decision Matrix (CLAUDE.md)

Proof gate NOT FIRED (Sigma EV SOP slipped 3 quarters) + ugliness ARTIFACT-OF-CLIMB (depressed
blended ROCE 7.68% is an artifact of the post-IPO cash pile inflating capital employed, not
structural decay) + recognition gap CLOSED → **PRICED NARRATIVE (TRAP).** The most seductive cell:
clean optics, transition narrated but unproven, TO state already priced; downside is double
(transition fails AND multiple compresses). Posture: AVOID / hard WATCH with no position until the
proof gate FIRES and the price re-opens the gap.

---

## VERDICT CARD

| Field | Read |
|---|---|
| **Company** | Divgi Torqtransfer Systems (DIVGIITTS) |
| **CMP** | Rs 1,175 (ex-cash operating PE 45x; incl-cash 48.9x) |
| **Earnings basis** | FY27 forward operating EPS Rs 24, treasury stripped (18.1 symmetry both ends) |
| **Destination PE — governing** | **30.0x forward** (operator override at 30x cap, peer-anchored) |
| **Destination PE — Track 2 additive (floor)** | 20.0x (18.5-21.5x) |
| **Destination PE — Track 1 RRM (floor)** | 17.9x (16.5-19.5x), r=14%, RRM 0.94 |
| **Base fair value** | **Rs 815** (Rs 24 × 30 + Rs 95); framework-floor base Rs 525-575 |
| **Bear / Bull fair value** | Rs 533 / Rs 974 |
| **Entry zone** | **Rs 570-650** | 
| **MoS price** | Rs 570 (30% evidence-scaled) |
| **Hurdle Ratio** | base 0.95 / bull 1.26 → **STOP** (need ~43% EPS CAGR from CMP) |
| **Upside/downside from CMP** | −0.56 (no upside; −31% to base FV, −55% to bear) |
| **Prob-weighted expected CAGR from CMP** | **−4.4%** |
| **FV CAGR** | **10.8% — HYBRID** |
| **Return source** | EPS compounding (~12.6%) net of a declining cash slice; no re-rating lever left |
| **Relative cross-check (Step 1C)** | PENDING LIVE PEER TABLE; carried 27x peer downside line; 30% test not triggered (30x > 27x); operator base governs; both Amendment 20 gates fail |
| **Transition posture** | PRICED NARRATIVE (TRAP): proof NOT fired + ARTIFACT + gap CLOSED |
| **Governance context** | CONCERN — operator ruled WATCHLIST defaulting to AVOID until 18-Sep-2026 AGM and FY27 AR clear it (FLAG-PROMOTER, FLAG-RPT-COMPLETENESS, FLAG-SUBSIDIARY-CONTRADICTION) |
| **DECISION (on the numbers)** | **AVOID (on valuation).** CMP Rs 1,175 is 44% above base fair value Rs 815; Hurdle STOPs even on bull; expected CAGR from CMP negative; return-source HYBRID with no re-rating lever. |

**Coherence.** The valuation decision (AVOID-on-valuation, computed) and the independent governance
ruling (WATCHLIST defaulting to AVOID until the AGM/FY27 AR) POINT THE SAME WAY. Even on the
optimistic operator base (30x override, 24% fair-case margin, 20% ROCE / 19x), the stock does not
clear. On the framework's own floor (17.9-20x, base fair value Rs 525-575) it is more than 55%
overvalued. AVOID.

**Would I pay 30x forward for this business here?** No — not with proof not fired, an ROCE that is
fair-case not delivered, three live disclosure flags, and the market already 44% above the
operator's own generous fair value.

---

### Flags carried forward
- FLAG-CASH (Pillar 2 INDETERMINATE; multiplier 1.00x applied)
- FLAG-PROMOTER / FLAG-RPT-COMPLETENESS / FLAG-SUBSIDIARY-CONTRADICTION / GOVERNANCE-PATTERN
- FLAG-ROCE-OPTIMISM (operator 20% ROCE → 19x base vs formula 17.5x; base projection ROCE ~16-17%)
- FLAG-SECTOR-CAP-OVERRIDE (30x vs 25x framework default)
- FLAG-MULTIPLE-OVERRIDE (governing 30x is ~50% above framework additive 20x)

```yaml
stage: B11-valuation
company: "DIVGIITTS"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
entity: "consolidated single-entity"
entity_count: 1
input_gaps:
  - "Live peer table (Amendment 20 / step 1C): PENDING LIVE PEER TABLE, re-runs at Role 5.5"
  - "Customer/OEM revenue concentration: NOT DISCLOSED"
  - "Promoter pledge %: NOT FOUND"
  - "Indonesia per-unit ASP: NOT FOUND (bounded Rs 105-140 Cr total program)"
  - "3-year historical revenue/PAT CAGR: NOT FOUND"
  - "Live market PE for relative-PE denominator (Amendment 15): NOT FOUND"
flags:
  - "FLAG-CASH: Pillar 2 INDETERMINATE (no rating); cash multiplier 1.00x applied, no growth offset"
  - "FLAG-PROMOTER: US-subsidiary narrative, Tejal RPT omission, KMP pay, Section 197 (B08)"
  - "FLAG-RPT-COMPLETENESS: Tejal Transmission omitted from Note 34"
  - "FLAG-SUBSIDIARY-CONTRADICTION: US subsidiary narrative vs Board's Report Item 13"
  - "GOVERNANCE-PATTERN: cross-document contradiction cluster; WATCHLIST defaults to AVOID until 18-Sep-2026 AGM/FY27 AR"
  - "FLAG-ROCE-OPTIMISM: operator ROCE 20% -> base PE 19x vs continuous-formula 17.5x; base-case op ROCE ~16-17%"
  - "FLAG-SECTOR-CAP-OVERRIDE: 30x operator override from 25x framework default (this run only)"
  - "FLAG-MULTIPLE-OVERRIDE: governing 30x ~50% above framework additive 20x / RRM 17.9x"
framework_versions: "Master v3.6 / Section 1B v3.3+v3.5.1+v3.6+v3.7+v3.8+v3.9 / FTTCP v2.1"
pe_basis: "forward"
exit_pe_base_approved: 30
destination_pe:
  track1_rrm: {low: 16.5, mid: 17.9, high: 19.5, r_used: 14, rrm: 0.94}
  track2_additive: {low: 18.5, mid: 20.0, high: 21.5}
  divergence_pct: 11.7
  governing_track: "OPERATOR-APPROVED 30x forward (overridden sector cap, peer-anchored) governs and sets the entry zone; both framework tracks (RRM 17.9x, additive 20x) sit ~50% below and are retained as floor/cross-check per Amendment 20.9"
pillar_detail:
  roce_used: 20
  roce_base: 19
  roce_recovery_route: "pillar1-midpoint"
  pillar1_normalization_route: "A-operational (cash-strip both sides; B10 labeled Route B, corrected: post-IPO cash-pile is denominator bloat = Route A; 20% ROCE / 19x unchanged)"
  cash_multiplier: 1.0
  structural_or_growth: "INDETERMINATE (no credit rating exists; conservative neutral multiplier)"
  growth_offset: 0
  growth_premium: 1
  strategic_premium: 0
  shared_catalyst_flag: false
  ua_applied: false
  sector_cap_used: 30
hurdle_ratio: {base: 0.95, bull_used: true, verdict: "STOP"}
fair_values:
  track1: {bear: 533, base: 815, bull: 974}
  track2: {bear: 387, base: 575, bull: 681}
expected_cagr_prob_weighted: -4.4
entry_range: {low: 570, high: 650}
mos_price: 570
upside_downside_ratio: -0.56
decision: "AVOID (on-valuation). CMP Rs 1,175 is 44% above base fair value Rs 815; Hurdle STOPs even on bull EPS CAGR; prob-weighted expected CAGR from CMP -4.4%; return-source HYBRID (FV CAGR 10.8%) with no re-rating lever left. Governance CONCERN independently defaults to AVOID until the 18-Sep-2026 AGM and FY27 AR."
unresolved_inputs_used:
  - "Year-4/FY31 industry-growth fade anchor 12%: NAMED ASSUMPTION per v3.8 18.0 (corpus holds no transfer-case industry growth rate; B09 TAM confidence Low)"
  - "Cash taper 95->90->85->80 over the hold: assumption, no committed schedule; modest deploy into Shirwal/Mayflower capex"
  - "Bear/bull exit multiple held at governing 30x (earnings flexed only); bear thus generous (peak multiple on trough earnings) - flagged"
  - "Governing exit multiple 30x, ROCE 20%/19x base, r=14%, +1x growth: operator-approved at FTTCP gate, used as-is; framework floor (17.9-20x, base FV Rs 525-575) reported as divergence"
som_cagr_crosscheck: "consistent"
one_line_thesis: "A build-to-spec driveline maker priced at 45x ex-cash forward earnings against a Rs 815 fair value: the transition is narrated but unproven (EV-SOP slipped 3 quarters), the TO-rung re-rating is already over-priced, and even the operator's generous 30x override cannot clear the 25% hurdle. AVOID on valuation."
```
