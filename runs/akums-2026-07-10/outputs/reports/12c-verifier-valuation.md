# STAGE 12C — VERIFIER C: FRAMEWORK ADHERENCE (PHASE 3, VALUATION-ADHERENCE AUDIT)

**Run:** akums-2026-07-10  |  **Model:** claude-opus-4-8  |  **Verifier:** C (framework adherence), valuation half
**Scope:** Section 1B v3.3 (+v3.4 Amendment 4), Master v3.3 Role 2 decision rules, FTTCP v1.2 single-credit / Pillar 1 authority.
**Artifacts audited:** B10 (10-assembly.md + B10-valinputs.yaml), B11 (11-valuation.md + B11-valuation.yaml), B14 (14-thesis.md + inline B14 block).
**Discipline:** rule application only, not company quality and not raw-number sourcing (Verifier A owns numbers). Gate 0 + Emerging Moat adherence was recorded in phase 1 and is NOT re-audited here.

---

## A. PILLAR 1 — ROCE BASE MULTIPLE

| # | Rule (as written) | Applied value | PASS/FAIL | Recompute / note |
|---|---|---|---|---|
| 1 | Continuous formula, ROCE ≤33%: Base PE = 0.5×ROCE + 7.5, floor 9x, cap 24x (Amendment 5 / Master Pillar 1). Old bands not used. | 0.5×29.0 + 7.5 = 22.0x | **PASS** | 0.5×29+7.5 = 22.0x exact. Range 0.5×28+7.5=21.5x, 0.5×30+7.5=22.5x correct. Continuous formula used, not bands. |
| 2 | ROCE selection: FTTCP ROCE forward verdict is SOLE Pillar 1 authority; STAGNANT → "current ROCE" (FTTCP v1.2 table). | STAGNANT → current ROCE = 29.0% (idle-cash-adjusted operator override, 28-30% band; reported 13.7% correctly rejected) | **PASS** | STAGNANT mapped to current ROCE as written. The "current ROCE" is the deliberation-authoritative idle-cash-adjusted 29% (operator override, recorded in B10 deliberation_authoritative). No ad-hoc trajectory judgment inserted. |
| 3 | Single-credit rule: ROCE recovery credited via Pillar 1 OR Strategic Premium, never both; state the route. | Strategic Premium = +0x; report states "credited via Pillar 1"; B11 YAML route = "pillar1-midpoint" | **FAIL (MINOR)** | No double-credit in substance (Strategic = +0x, so single-credit is honoured and the number is unaffected). But the route label is inaccurate: STAGNANT uses *current* ROCE with NO forward/midpoint smoothing, so no "recovery" actually entered Pillar 1 and no "midpoint" was taken. The framework-honest label is "not credited (STAGNANT, current ROCE)", not "pillar1-midpoint". Presentational; destination PE unchanged. |

Pillar 1 result: **22.0x (range 21.5-22.5x)** — CONFIRMED, no numeric error.

---

## B. PILLAR 2 — CASH CONVERSION MULTIPLIER

| # | Rule | Applied | PASS/FAIL | Note |
|---|---|---|---|---|
| 4 | Structural vs growth-induced test; structural → 0.65x with NO offset; growth-induced → not structural penalty. CARE/rating structural assessment takes precedence. | GROWTH-INDUCED (ICRA "liquidity Strong", Total Debt/OPBDITA 0.2x, no structural-WC language); 0.65x explicitly NOT applied; Kernex-cap tail closed. | **PASS** | Determination is authoritative from FTTCP deliberation and applied as written. The 0.65x structural penalty correctly withheld. |
| 5 | Cash multiplier band assignment; growth offset applies ONLY to the 0.80x growth-phase band, not to neutral. | 1.00x neutral (deliberation midpoint of 0.90-1.15x); no growth offset added. | **PASS** | Report is at the 1.00x neutral band, not the 0.80x band, so no offset is due; correctly not added. OBSERVATION (conservative-direction, not a violation): adjusted CFO/PAT of 0.99x taken literally sits above the 70% band (which would justify 1.15x-1.30x); the pipeline instead read it as volatile/distorted (headline 4.61x vs adjusted 0.99x) and assigned the lower 1.00x. This depresses, not inflates, the destination PE and supports the AVOID — conservative bias respected. |

Quality-Adjusted Base: 22.0x × 1.00x = **22.0x** — CONFIRMED.

---

## C. PILLAR 3 — v3.4 AMENDMENT 4 (DECOUPLED)

**Framework as written (Amendment 4 v3.4):** Pillar 3 splits into **TWO** additive components only — **3a Growth Visibility Premium** and **3b Moat Formation Premium** — combined hard cap +6x. The version-history line confirms: "3a Growth Visibility ... and 3b Moat Formation ... Combined 3a+3b hard-capped at +6x." There is **no 3c** in Section 1B.

| # | Rule | Applied | PASS/FAIL | Note |
|---|---|---|---|---|
| 6 | 3a: award +2x if any two of {capex-embedded ≥15%, order book ≥1.0x / B2B ≥1.2x, SOM CAGR ≥20% w/ capacity pass, delivery grade A/B} qualify; +3x if ≥3 AND grade A/B; grade C caps 3a at +2x; else +0x. | 1 of 4 qualify (capex-embedded 20.6% PASS; order book none FAIL; SOM 13.9-16.1% <20% FAIL; grade C FAIL). Need ≥2 → +0x; grade C cap also binds. | **PASS** | Test evaluation and award correct: +0x. |
| 7 | 3b: existing EM-gated table, unchanged. EM 25-29 → +1x. | EM 26.3, 25-29 STRENGTHENING band → +1x. | **PASS** | Correct band and premium. (EM used = 26.3; the 27.3 operator rescore is in the same band, no change.) |
| 8 | Combined 3a+3b ≤ +6x hard cap. | 0 + 1 = +1x; cap +6x not binding. | **PASS** | Correct combined value; equals correct framework output. |
| 9 | Apply "each sub-scale as written." | Pipeline added a THIRD sub-scale, "3c Duration Premium" (thresholds 2.5x rev → +1x, 4.0x → +2x), scored +0x on contracted streams (EU EUR 200m + Zambia USD 50m ≈ Rs 2,300 cr = 0.53x revenue). | **FAIL (MINOR)** | 3c is **not part of Section 1B v3.4 Amendment 4**, which defines only 3a + 3b. Numerically harmless here because 3c = +0x, so combined Pillar 3 (+1x) equals the correct 3a+3b framework result and the destination PE is unaffected. Flagged for framework integrity: (i) inventing a sub-scale departs from "as written"; (ii) structurally it creates a latent path to exceed the +6x cap that governs 3a+3b, since a positive 3c would be additive on top. Recommend Role-3/operator confirm whether 3c is a sanctioned local extension or should be dropped. The 3c tenure basis was at least applied conservatively — it rests on documented stated-tenure streams (EU to Dec 2032, Zambia) and correctly excludes the relationship-length-only domestic CDMO base. |

Pillar 3 combined = **+1x** — number CONFIRMED correct; structure carries one MINOR deviation.

---

## D. STRATEGIC PREMIUM & RAW PE

| # | Rule | Applied | PASS/FAIL | Note |
|---|---|---|---|---|
| 10 | Strategic Premium additive; ROCE re-rating optionality only if NOT credited in Pillar 1 (single-credit). | +0x (weak pricing power, no monopoly; ROCE kept in Pillar 1). Optional +1x scale premium noted but NOT applied (conservative). | **PASS** | Single-credit respected; no re-rating optionality double-counted. |
| 11 | Raw Destination PE F = C + D + E. | 22.0 + 1.0 + 0.0 = **23.0x**. | **PASS** | Arithmetic correct. |

---

## E. UA MULTIPLIER, SECTOR CAP, DUAL TRACK

| # | Rule | Applied | PASS/FAIL | Note |
|---|---|---|---|---|
| 12 | UA (Amendment 3): applies only if ALL three qualifiers hold (listed ≥12m; Gate 0 ≥60 OR EM ≥25; FII+DII <3%); ordering H = min(F×1.25, Cap). | UA NOT applied — qualifier 3 fails (DII alone 14.3% > 3%). Qualifiers 1 (23m) and 2 (Gate 0 79 / EM 26.3) met. F2 = F = 23.0x. | **PASS** | All three qualifiers evidenced; correct fail on qualifier 3; low-institutional-as-risk trap avoided (high DII treated as strength, not constraint). Ordering moot (not applied) but stated correctly. |
| 13 | Sector cap absolute; Pharma/CDMO = 38x; UA can never breach. | Cap 38x used; H = min(23.0, 38) = 23.0x; cap not binding. | **PASS** | Correct row and absolute treatment. |
| 14 | BOTH tracks (Additive + RRM) present and carried through every fair value AND the verdict card. | Track 2 (23.0x) and Track 1 RRM (20.25x) present in Sec 3, 4A, 4C, 4H verdict card and B14 valuation summary. | **PASS** | Dual-track discipline maintained end to end. |
| 15 | RRM = 1 + (13.5% − r)×0.12, bounded 0.70-1.60; base r mid-cap 13% adjusted for durability/governance; bound r [9%,18%]. | r = 14.5% (13% base +1.5% for FLAG-PROMOTER governance + weak durability); RRM = 1+(13.5-14.5)×0.12 = 0.88; Track 1 dest = 23.0×0.88 = 20.24 ≈ 20.25. | **PASS** | RRM math exact; adjustment direction (up for governance/durability) correct; within bounds. |
| 16 | On >15% track divergence, state which track is more appropriate; the more conservative track sets the entry zone. | Divergence (23.0−20.25)/23.0 = 12.0% (<15%); conservative Track 1 governs entry regardless. | **PASS** | Divergence recomputed 12.0% — matches. Below 15% threshold; conservative Track 1 correctly governs entry zone. |

Final Destination PE: **23.0x Track 2 (21.5-24.5x) / 20.25x Track 1 RRM (18.5-22.0x)** — CONFIRMED.

---

## F. HURDLE RATIO (Amendment 2)

| # | Rule | Applied | PASS/FAIL | Recompute |
|---|---|---|---|---|
| 17 | HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE); pass ≥ 1.953. | Base 18.3%, current PE 42.1x. Track 2: 0.91; Track 1: 0.80. | **PASS** | 1.183³=1.6556; ×(23.0/42.1=0.5463)=0.905≈0.91 ✓; ×(20.25/42.1=0.4810)=0.796≈0.80 ✓. |
| 18 | Credibility-grade gate on Bull: Bull EPS CAGR usable only if grade A/B; grade C/D → Bull row uses Base + 5% max. | Grade C → Bull capped at 18.3%+5% = 23.3%. Track 2: 1.02; Track 1: 0.90. | **PASS** | 1.233³=1.8746; ×0.5463=1.024≈1.02 ✓; ×0.4810=0.902≈0.90 ✓. Gate correctly applied — uncapped bull (23.5%) not used. |
| 19 | Verdict: HR(Bull) < 1.953 → STOP. | Both base and capped-bull HR far below 1.953 → **STOP**. | **PASS** | Correct verdict; consistent with B10 (~0.99). |
| 20 | No exit PE from outside Section 1B (CLAUDE.md NEVER rule; Master). | Exit PE = Section 1B four-pillar only; EV/EBITDA derived as 0.6× of Section 1B PE (cross-check); no round-number defaults. | **PASS** | Sole exit-multiple authority respected. |

---

## G. ROLE 2 (B14) DECISION RULES

| # | Rule | Applied | PASS/FAIL | Note |
|---|---|---|---|---|
| 21 | AVOID triggers (Master Sec 7): Gate 0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR Upside/Downside <2x OR Hurdle STOP. | All four fire and are cited (Gate 0 AVERAGE; Promoter CONCERN; HR STOP; U/D 0.21x <2x). Verdict AVOID. | **PASS** | Over-determined AVOID; each trigger anchored to its block. |
| 22 | Position sizing for AVOID; Promoter Concern cap binds absolutely; override only if recorded. | Position size ZERO; position_size_override empty; report shows even a Gate0→GOOD lift would still AVOID on the other three; Promoter CONCERN cap binds. | **PASS** | Sizing handled correctly; no unrecorded override invented. |
| 23 | v3.4 ENTRY CONJUNCTION rule stated explicitly in the Section 7 verdict box. | Present and load-bearing: BUY/BUY-ON-DIPS only if price in zone AND no thesis-broken trigger fired; withdrawn-zone logic spelled out; entry_conjunction_stated: true. | **PASS** | Explicitly present in the verdict box with concrete trigger list. |

---

## RECOMPUTATION SUMMARY

- Destination PE recomputed independently: **23.0x Track 2 (21.5-24.5x); 20.25x Track 1 RRM (18.5-22.0x)** — **concur** with B11.
- Hurdle Ratio recomputed: **0.91 base / 1.02 grade-C-capped bull → STOP** — **concur**.
- Decision recomputed: **AVOID** (four independent triggers) — **concur**.
- Every FAIL is MINOR and numerically inert: neither changes destination PE by >1x, nor flips the Hurdle verdict, nor flips the decision. No CRITICAL, no MAJOR.

## FINDINGS

1. **MINOR** — B11 pillar_detail.roce_recovery_route = "pillar1-midpoint" mislabels the route. Under a STAGNANT FTTCP verdict, Pillar 1 uses *current* ROCE with no midpoint smoothing and no recovery uplift; the framework-honest label is "not credited (STAGNANT / current ROCE)". Single-credit substance is intact (Strategic Premium +0x); destination PE unaffected.

2. **MINOR** — Pipeline introduced a "3c Duration Premium" sub-scale (2.5x/4.0x contracted-revenue thresholds) inside Pillar 3. Section 1B v3.4 Amendment 4 defines only 3a + 3b (combined cap +6x); 3c is extra-framework. Harmless here (3c = +0x, combined Pillar 3 = +1x = correct 3a+3b result), but it is a departure from "apply each sub-scale as written" and structurally opens a latent path around the +6x cap. Recommend operator confirm or drop.

## COUNTS

- Rules checked: 23
- Passed: 21
- MINOR fails: 2 | MAJOR: 0 | CRITICAL: 0
- Acceptance rate: 21/23 = 91%

---

```yaml
stage: B12c
company: "AKUMS"
run_date: "2026-07-10"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}   # completed in phase 1; not re-audited this phase
emoat: {rules_checked: 0, fails: []}   # completed in phase 1; not re-audited this phase
valuation:
  rules_checked: 23
  fails:
    - {severity: MINOR, rule: "Single-credit route label (Pillar 1)", detail: "route recorded as 'pillar1-midpoint' but STAGNANT uses current ROCE, no midpoint/recovery credited; honest label is 'not credited'. Substance intact (Strategic +0x), destination PE unchanged."}
    - {severity: MINOR, rule: "Pillar 3 sub-scale as written (v3.4 Amendment 4)", detail: "pipeline added a '3c Duration Premium' not defined in Section 1B (framework has only 3a+3b, cap +6x). Nets to +0x so combined +1x and destination PE are correct; extra-framework structure flagged, latent +6x-cap bypass risk."}
recomputed_destination_pe: ""   # concur: 23.0x Track 2 / 20.25x Track 1 RRM
recomputed_decision: ""         # concur: AVOID
findings:
  - {severity: MINOR, location: "B11-valuation.yaml pillar_detail.roce_recovery_route", note: "'pillar1-midpoint' mislabels a STAGNANT current-ROCE route; no recovery credited; no numeric impact."}
  - {severity: MINOR, location: "B10 deliberation_authoritative.pillar_3_growth_premium / B11 Section 1B Pillar 3", note: "'3c Duration Premium' is not in Section 1B v3.4 Amendment 4 (3a+3b only); scored +0x so destination PE unaffected; framework-integrity deviation."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 91
```
