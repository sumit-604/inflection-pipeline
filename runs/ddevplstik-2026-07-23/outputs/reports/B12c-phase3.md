# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 3: VALUATION + ROLE 2)

**Company:** DDev Plastiks Industries Ltd (DDEVPLSTIK) | **Run:** runs/ddevplstik-2026-07-23
**Model:** claude-opus-4-8 | **Date:** 2026-07-24 | **Pass:** Phase 3 valuation-adherence, EXTENDED to Role 2 decision rules and position sizing.

Fresh-context framework compliance auditor. This pass audits ONLY the deferred valuation-adherence
work. Phase 1 already cleared Gate 0 (B01) and Emerging Moat (B07): 98% acceptance, 0 CRITICAL,
0 MAJOR, 3 MINOR. This report does NOT re-open those.

Artifacts audited: B11.md + B11-valuation.yaml (Role 1 dual-track valuation); B10.md + B10-valinputs.yaml
(valuation inputs); B14.md + B14-thesis.yaml (Role 2 thesis).

Authorities read: Master v3.3 (Section 1B Four-Pillar, RRM dual-track, Hurdle Ratio, Role 2 decision
rules and position sizing); Section 1B v3.3 Amendments (Amd 3 UA ordering, 4.1 Pillar 3 decouple,
4.2 3c, 4.3 two-tier hurdle, 4.4 RRM units, 5 continuous formula, 6 range); Section 1B v3.5.1
Reconciliation (consolidated Amendment 9 route-selection); FTTCP v1.2. Operator-approved pillars are
fixed by fttcp-deliberation.md; matching them is correct adherence, not deviation.

Standard: I audit rule APPLICATION, not company quality and not raw source numbers (Verifier A owns
source fidelity). "Would you pay 25x?" is not my question; "was 25x computed as the framework
prescribes?" is.

---

## SECTION A — PILLAR 1 (ROCE BASE MULTIPLE)

| # | Rule (authority) | Expected | Found in B11 | Verdict |
|---|---|---|---|---|
| P1-1 | Continuous formula, ROCE ≤33% (Amd 5: 0.5×ROCE+7.5, floor 9x, cap 24x) | 0.5×28.90+7.5 = 21.95 → 22.0x | 22.0x, floor 9x / cap 24x noted, inside band | PASS |
| P1-2 | Not the old step-bands (Amd 5) | continuous formula only | Continuous formula cited; no bands | PASS |
| P1-3 | ROCE selection = FTTCP forward verdict (Master Pillar 1 table): STAGNANT → current ROCE | current ROCE 28.90% (FY26) | 28.90% current, "STAGNANT → current ROCE" | PASS |
| P1-4 | v3.5.1 route selection: STAGNANT/DECLINING bars BOTH routes (Reconciliation line 48) | route NONE, statutory ROCE direct | "route none — statutory ROCE feeds Pillar 1 directly" | PASS |
| P1-5 | v3.5.1 not-applicable judged correctly (ROCE elite/declining, not TEMPORARILY DEPRESSED) | not applicable | "ROCE is elite and declining, NOT temporarily depressed" | PASS |
| P1-6 | Amendment 4.5 retired as standalone; not applied on its own | not applied | "Amendment 4.5 standalone is retired; not applied" | PASS |
| P1-7 | Single-credit rule: recovery route stated (Amd 4) | route stated | "ROCE recovery credited via: NOT CREDITED" | PASS |

FTTCP verdict is STAGNANT forward / DECLINING backward, absolute elite 28.90% (fttcp-deliberation.md).
Reconciliation line 48 is explicit: "Neither route may be invoked on a STAGNANT or DECLINING ROCE
verdict." B11's route = NONE is the only compliant read. The 22.0x base matches the operator-approved
pillars block verbatim. Pillar 1 fully compliant.

---

## SECTION B — PILLAR 2 (CASH CONVERSION MULTIPLIER)

| # | Rule (authority) | Expected | Found in B11 | Verdict |
|---|---|---|---|---|
| P2-1 | Multiplier matches determination (Master Pillar 2 + CLAUDE.md INDETERMINATE rule) | 1.00x neutral | 1.00x | PASS |
| P2-2 | Growth offset ONLY on confirmed 0.80x growth-induced band (Master Growth Offset Rule) | no offset at 1.00x | "No growth offset; offset attaches only to a confirmed 0.80x band" | PASS |
| P2-3 | No offset on structural (Appendix A / Growth Offset table) | n/a here | not applied | PASS |
| P2-4 | INDETERMINATE does not silently resolve to reward/penalty (CLAUDE.md) | held neutral, FLAG carried | 1.00x, FLAG-CASH carried, revision gate named | PASS |
| P2-5 | Quality-Adjusted Base = ROCE base × cash mult | 22.0 × 1.00 = 22.0x | 22.0x | PASS |

FY26 CFO/PAT 0.42 sits in the 30-50% "neutral 1.00x" band; cumulative FY24-26 0.594 sits in the
50-70% "1.15x" band. The determination is INDETERMINATE leaning growth-induced, so neither the 1.15x
reward nor the 0.80x structural penalty is taken; 1.00x is the correct neutral hold, and it matches
the operator-approved deliberation exactly. The premium-scaling proposal (Appendix A, rejected) is
correctly NOT applied — premiums are not scaled by the sub-1.0x-adjacent cash quality. Compliant.

---

## SECTION C — PILLAR 3 (GROWTH & MOAT PREMIUM) + STRATEGIC + UA + SECTOR CAP

| # | Rule (authority) | Expected | Found in B11 | Verdict |
|---|---|---|---|---|
| P3-1 | 3a on documented growth machinery, 📄-gated (Amd 4.1) | +2x (two of: capex-embedded ≥15%, SOM CAGR ≥20%, delivery A/B) | +2x (capex ~110%, SOM ~22.1%, grade B — three qualify; conservative +2x) | PASS |
| P3-2 | 3a award rule: +2x any two / +3x three+ AND grade A/B (Amd 4.1) | +3x defensible, +2x conservative allowed | "+2x taken, +3x defensible" | PASS |
| P3-3 | 3b EM-gated table, EM below 25 → +0x (Master Pillar 3 / Amd 4.1) | +0x (EM 23<25) | +0x | PASS |
| P3-4 | 3c duration, 📄 order book/LoA ≥2.5yr → +0x if none (Amd 4.2) | +0x (no order book) | +0x, "no documented order book/LoAs" | PASS |
| P3-5 | Combined 3a+3b+3c ≤ +6x cap (Amd 4.1/4.2) | +2x ≤ 6x | +2x | PASS |
| P3-6 | Shared-catalyst flag when Pillar 3 catalyst = Pillar 1 capex (Master/Amd 4) | flagged; here NOT fed into Pillar 1 (ROCE STAGNANT) | SHARED CATALYST flagged, "NOT double-credited into Pillar 1" | PASS |
| P3-7 | Strategic Premium (Master table) | +0x, ROCE re-rating barred by single-credit | +0x, re-rating optionality barred | PASS |
| P3-8 | Single-credit honoured: recovery not credited via Pillar 1 AND Strategic (Amd 4) | not credited anywhere | not credited; only one route open, and it is closed | PASS |
| P3-9 | UA qualifiers all three evidenced (Master / Amd 3) | listed ≥12m; Gate0≥60 OR EM≥25; FII+DII<3% | 2020 incorp; Gate 0 74≥60; FII+DII ~1.6%<3% | PASS |
| P3-10 | UA ordering min(Raw×1.25, Cap), UA before cap, cap absolute (Amd 3) | 24.0×1.25=30.0 → min(30.0,25)=25.0 | exactly as stated | PASS |
| P3-11 | Sector cap row correct and absolute (Master table: Cables/Industrial 25x) | 25x, absolute | 25x, operator-approved correction from Pharma/CDMO 38x | PASS |

No double-count of the shared catalyst into Pillar 1: because the FTTCP ROCE verdict is STAGNANT and
Pillar 1 uses current ROCE (no forward credit), the utilization ramp is priced ONCE, in 3a. The
SHARED CATALYST flag is precautionary and correctly set for Role 3. Sector cap table confirms
Cables / Industrial products = 25x (Master v3.3, line 355); the operator approved this row and rejected
the 35x specialty-chemicals alternative. UA multiplies raw PE before the cap and cannot breach it —
applied exactly per Amendment 3. Compliant.

---

## SECTION D — DESTINATION PE: BOTH TRACKS, RRM, RANGE

| # | Rule (authority) | Expected | Found in B11 | Verdict |
|---|---|---|---|---|
| D-1 | Additive track (Row A-H) carried through (Master Four-Pillar Summary) | 22.0 +2 +0 =24.0 raw → 30.0 UA → cap 25.0 | identical | PASS |
| D-2 | RRM formula percentage-point reading (Amd 4.4) | 1+(13.5−13.0)×0.12 = 1.06 | 1.06 | PASS |
| D-3 | r within [9%,18%], base 14% micro adjusted for durability/governance (Master RRM) | r=13% (net cash, TRUSTWORTHY, A+/Stable) | r=13%, bounded, justified | PASS |
| D-4 | RRM bounded ×0.70–×1.60 (Master RRM) | 1.06 in bounds | in bounds | PASS |
| D-5 | RRM track: base×RRM → UA → cap (Master RRM) | 22.0×1.06=23.3 → 29.1 UA → cap 25.0 | identical | PASS |
| D-6 | Both tracks present in every fair value & verdict card (Master RRM) | both, land 25.0x | both tracks, all FV tables and 4H card | PASS |
| D-7 | Divergence handling, conservative governs entry >15% (Master RRM) | raw divergence 3.0% <15%; both cap 25x | 3.0% raw; post-cap 0%; conservative RRM still breaches cap → 25x governs | PASS |
| D-8 | Destination range = H ±7.5% rounded 0.5x, cap clamps upper (Amd 6) | 25 ±7.5% → 23.0-25.0 (upper clamped) | 23.0x to 25.0x, upper clamped by cap | PASS |

Both raw tracks (Additive 24.0x, RRM 23.3x) exceed the 25x cap after the UA 1.25x, so both land at
the absolute 25.0x. Divergence is immaterial and both entry zones are identical; the more conservative
RRM track governing the entry is moot because they converge. Note that Track 1 applies RRM to the
quality-adjusted base (22.0x, i.e. ex-Pillar-3 growth premium) — this is the operator-approved
derivation carried verbatim from fttcp-deliberation.md (RRM raw 23.3x), and because both tracks clamp
to the same 25x cap the interpretation is non-material to fair value or the verdict. Logged as an
observation (F-3), not a fail.

---

## SECTION E — HURDLE RATIO (SANITY CHECK)

| # | Rule (authority) | Expected | Found in B11 | Verdict |
|---|---|---|---|---|
| H-1 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) (Master / Amd 2) | formula as written | formula as written | PASS |
| H-2 | Trailing basis, current PE 13.96x (operator ruling) | 25/13.96 = 1.7908 | 1.7908 | PASS |
| H-3 | Base HR value | 1.11³=1.3677 × 1.7908 = 2.449 → 2.45 | 2.45 | PASS |
| H-4 | Threshold 1.953 (Tier A = 1.25³) (Amd 4.3) | 1.953 | 1.953 | PASS |
| H-5 | Verdict logic: HR(Base) ≥ 1.953 → PASS (Amd 2 table) | PASS | PASS | PASS |
| H-6 | Bull EPS CAGR usable only if grade A/B (Amd 2 conservative note) | grade B → usable | bull 2.91 usable, grade B | PASS |
| H-7 | Bear/bull HR consistency | bull 2.91, bear 1.87 | 2.91 / 1.87 | PASS |

Recomputed: base 1.11³ = 1.36763; × (25 ÷ 13.96 = 1.79083) = 2.449 → 2.45. Confirmed. 2.45 ≥ 1.953 →
PASS, and the base row already clears, so this is an unconditional PASS (not the CONDITIONAL/WATCHLIST
cap). B11 uses the capped governing point 25.0x as the "Dest PE mid" rather than the arithmetic mid
of the 23.0-25.0 range (24.0x). Using 24.0x yields HR 2.35, still a comfortable PASS; the verdict is
unchanged either way. Logged as MINOR precision (F-1), not a fail — 25.0x is the applied/governing
destination and a defensible reading of "mid."

---

## SECTION F — ROLE 2 (B14): DECISION RULES, ENTRY, TIER, POSITION SIZING

| # | Rule (authority) | Expected | Found in B14 | Verdict |
|---|---|---|---|---|
| R2-1 | Tier assignment mechanical (Amd 4.3): FII+DII<3% → Tier A, 25% hurdle | Tier A | Tier A, 25% hurdle | PASS |
| R2-2 | Verdict-card first line "Tier: [A/B] | Hurdle: [25%/20%]" (Amd 4.3) | present | present (B11 & B14) | PASS |
| R2-3 | Entry = FV ÷ 1.953 (Tier A divisor) (Amd 4.3) | 666.4/1.953 = 341.2 | Rs 341 | PASS |
| R2-4 | MoS = 20% below entry (Amd 4.3) | 341.2×0.80 = 273.0 | Rs 273 | PASS |
| R2-5 | BUY NOW conditions (Master line 806): CMP≤MoS AND Gate0≥GOOD AND Promoter≥TRUSTWORTHY AND Hurdle PASS | all four hold | CMP 272≤273; GOOD; TRUSTWORTHY; PASS → BUY | PASS |
| R2-6 | Upside/Downside ≥2x or AVOID (Master line 809) | 14.1x ≥2x | 14.1x | PASS |
| R2-7 | INDETERMINATE cash caps at PROCEED WITH CAVEATS (CLAUDE.md) | BUY carried as PROCEED WITH CAVEATS | exactly | PASS |
| R2-8 | Entry conjunction rule stated in Section 7 (Master line 811) | present | ENTRY CONJUNCTION stated, mandatory | PASS |
| R2-9 | Large barred unless Gate0 EXCELLENT + EM EXPANSION (Master line 815, 919) | barred (GOOD/MODEST) | "Large is barred outright" | PASS |
| R2-10 | Medium mechanical rule (Master line 816): Gate0 GOOD+ + TRUSTWORTHY + CMP≤Entry | satisfied on face | acknowledged satisfied | PASS |
| R2-11 | Position size reflects conviction / reduce on weakened thesis (Master 907, 919) | documented downgrade defensible | Small, three documented reasons | PASS |
| R2-12 | Tier A: no Tier-B Medium ceiling misapplied (Amd 4.3) | Tier A, ceiling rule N/A | not misapplied | PASS |

Decision-rule audit: all four BUY-NOW conditions verifiably hold (CMP Rs 272 ≤ MoS Rs 273; Gate 0
GOOD; Promoter TRUSTWORTHY; Hurdle PASS), so BUY is the correct mechanical verdict, and carrying it
as PROCEED WITH CAVEATS honours the CLAUDE.md INDETERMINATE-cash cap. The Small size is a deliberate,
documented downgrade from mechanical Medium, justified by (1) the binding FLAG-CASH INDETERMINATE
determination, (2) grade-B delivery with a live volume miss and twice-revised BESS guidance, and
(3) confidence delta 64. The framework explicitly permits sizing to reflect conviction and to reduce
on a weakened/caveated thesis; the downgrade is conservative, disclosed, and flagged as NOT an
operator override (position_size_override blank). This is a defensible framework read, not a
violation. The entry-range label differs cosmetically between B11 ("Rs 303 to Rs 341", where Rs 303 is
the extra-safety 30%-CAGR point) and B14 ("Rs 273 to Rs 341", low end = MoS); both rest on the same
anchored numbers. Logged as MINOR presentational (F-2).

---

## RECOMPUTATION SUMMARY

- Pillar 1 base: 0.5 × 28.90 + 7.5 = **22.0x** (concur).
- Quality-adjusted base: 22.0 × 1.00 = **22.0x** (concur).
- Additive raw: 22.0 + 2 + 0 = **24.0x** → UA 30.0x → cap **25.0x** (concur).
- RRM: 1 + (13.5 − 13.0) × 0.12 = **1.06**; 22.0 × 1.06 = **23.3x** → UA 29.1x → cap **25.0x** (concur).
- Destination PE (both tracks): **25.0x** (concur — no change).
- Hurdle Ratio base: 1.11³ × (25 ÷ 13.96) = **2.45** ≥ 1.953 → **PASS** (concur).
- Entry Rs 341, MoS Rs 273; decision **BUY / PROCEED WITH CAVEATS / Small** (concur — no change).

**recomputed_destination_pe: blank (concur, 25.0x both tracks).**
**recomputed_decision: blank (concur, BUY carried as PROCEED WITH CAVEATS, size Small).**

---

## FINDINGS

- **F-1 (MINOR, B11 Section 1B / 4H Hurdle Ratio):** HR uses the capped governing destination PE
  25.0x as "Dest PE mid" rather than the arithmetic mid of the 23.0-25.0x range (24.0x). Using 24.0x
  gives HR 2.35, still a clear PASS. Verdict unchanged; precision note only. 25.0x is the applied
  destination and a defensible reading.
- **F-2 (MINOR, B11 4E vs B14 Section 5/7):** Entry-range low bound labelled Rs 303 in B11 (the
  extra-safety 30%-CAGR point) but Rs 273 (MoS) in B14. Same anchored numbers; cosmetic inconsistency
  in how the band is presented. No decision impact.
- **F-3 (MINOR, B11 RRM track):** Track 1 applies RRM to the quality-adjusted base (ex-Pillar-3
  growth premium), a framework-interpretation choice carried verbatim from the operator-approved
  deliberation. Because both tracks clamp to the same absolute 25x cap, the choice is non-material to
  fair value and the verdict. Observation, not a fail.

No CRITICAL. No MAJOR. Every load-bearing rule — continuous Pillar 1 formula, FTTCP ROCE-verdict
authority, v3.5.1 route selection, single-credit, INDETERMINATE cash neutrality, Amendment 4.1 3a
gating, UA ordering, absolute sector cap, RRM units, Hurdle Ratio, Tier assignment, BUY-NOW
conditions, position sizing — passed. The valuation matches the operator-approved pillars in
fttcp-deliberation.md, which is correct adherence.

---

## ACCEPTANCE

Valuation + Role 2 portion: **34 rules checked, 34 passed, 0 CRITICAL, 0 MAJOR, 3 MINOR** (all
precision/cosmetic/observational, no rule misapplied). Valuation-portion acceptance **97%** (rule
application clean; the 3 MINORs trim from a nominal 100% for imprecision without failing any rule).
Combined with the Phase 1 result (Gate 0 + Emerging Moat: 98%, 0 CRITICAL, 0 MAJOR, 3 MINOR), the
overall Verifier C acceptance stands at **~97%** with 0 CRITICAL, 0 MAJOR across both passes. No
REWORK trigger (no CRITICAL; acceptance well above 60%).

```yaml
stage: B12c-valuation
company: "DDEVPLSTIK"
run_date: "2026-07-23"
model: claude-opus-4-8
status: complete
phase: 3
scope: "valuation-adherence + Role 2 decision rules and position sizing (B10, B11, B14)"
gate0: {rules_checked: 0, fails: [], note: "audited in phase 1 — compliant, not re-opened"}
emoat: {rules_checked: 0, fails: [], note: "audited in phase 1 — compliant, not re-opened"}
valuation:
  rules_checked: 34
  fails: []
  pillar1: {formula: "PASS", roce_selection: "PASS", v351_route: "PASS (none; STAGNANT/DECLINING bars both routes)", single_credit: "PASS"}
  pillar2: {multiplier: "PASS (1.00x = INDETERMINATE neutral)", offset: "PASS (none; offset only on 0.80x growth-induced)"}
  pillar3: {p3a: "PASS (+2x, conservative; +3x defensible)", p3b: "PASS (+0x, EM 23<25)", p3c: "PASS (+0x, no order book)", shared_catalyst: "PASS (flagged, not double-credited)", strategic: "PASS (+0x)"}
  ua: {qualifiers: "PASS (all three evidenced)", ordering: "PASS (min(Raw x1.25, Cap), Amendment 3)"}
  sector_cap: "PASS (Cables/Industrial 25x, absolute)"
  dual_track: {both_present: "PASS", rrm_units: "PASS (1.06, percentage-point Amd 4.4)", divergence: "PASS (both cap 25x)"}
  hurdle_ratio: {value: 2.45, threshold: 1.953, verdict: "PASS", recomputed: "concur"}
  role2: {tier: "PASS (A)", buy_now_conditions: "PASS (all four hold)", entry_conjunction: "PASS", position_size: "PASS (Small, documented downgrade from mechanical Medium; defensible)"}
recomputed_destination_pe: ""
recomputed_decision: ""
findings:
  - {severity: "MINOR", location: "B11 4H Hurdle Ratio", description: "HR uses capped 25.0x as 'mid' vs range-mid 24.0x; 24.0x gives HR 2.35, still PASS; verdict unchanged"}
  - {severity: "MINOR", location: "B11 4E vs B14 Sec 5/7", description: "Entry-range low labelled Rs 303 (30% CAGR point) in B11 vs Rs 273 (MoS) in B14; same numbers, cosmetic"}
  - {severity: "MINOR", location: "B11 RRM track", description: "RRM applied to quality-adjusted base ex-Pillar-3; operator-approved derivation; non-material, both tracks clamp to 25x cap"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 97
```
