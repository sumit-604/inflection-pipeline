# STAGE 12c — VERIFIER C, PHASE 3 VALUATION-ADHERENCE AUDIT

**Company:** JUBLCPL (Jubilant Agri and Consumer Products Ltd) | **Run:** 2026-08-18
**Verifier:** verifier-c-framework (B12c) | **Model:** claude-opus-4-8
**Scope:** Role 1 valuation (B11) + input assembly (B10), EXTENDED to Role 2 decision/sizing (B14).
**Rule sources:** Master v3.3 Role 1/Role 2 · Section 1B v3.3 Amendments · Section 1B v3.5.1 Reconciliation · FTTCP v1.2.
**Not in scope this phase:** Gate 0 (B01) and Emerging Moat (B07) — audited in phase 1.
**Subordination:** Verifier A (Haiku) is the sole authority on whether a number exists at its source anchor. This audit owns framework/judgment only and does not re-adjudicate number existence.

This is a demerger SUM-OF-THE-PARTS valuation (operator direction 18-Aug-2026): Business A = Performance Polymers & Chemicals (retained, specialty chemicals); Business B = Agri (P&K Fertilizers + Agri Nutrients, demerging as JASL). Both businesses re-derived from the frameworks below.

---

## 1. PILLAR 1 — CONTINUOUS FORMULA BASE (re-derived)

| Item | Framework rule | Report value | Re-derivation | Verdict |
|---|---|---|---|---|
| Business A base | ROCE>33% → 24 + 0.3×(ROCE−33), cap 30x (Master v3.3) | 30.0x on ROCE 67.5% | 24 + 0.3×(67.5−33) = 24 + 10.35 = **34.35 → capped 30x** | PASS |
| Business A ROCE selection | FTTCP FIRING → Current ROCE | Current (segment 67.5%) | FIRING → current; no midpoint smoothing | PASS |
| Business B base | ROCE≤33% → 0.5×ROCE + 7.5, floor 9x | 17.5x on ROCE 19.9% | 0.5×19.9 + 7.5 = **17.45 ≈ 17.5x** | PASS |
| Business B ROCE selection | FTTCP STAGNANT → Current ROCE | Current (19.9%) | STAGNANT → current | PASS |

**Note (MINOR, immaterial):** Business A base rests on segment ROCE 67.5%, which B10 itself flags as "inflated by segment allocation / unconfirmable," while the "authoritative current ROCE" is group 36%. Group 36% → 24 + 0.3×3 = 24.9x, not 30x. However this does NOT change the destination: A's cap-bound destination is 35x under BOTH inputs (24.9×1.15 + 2 = 30.6 raw → ×1.25 = 38.3 → capped 35x; 30×1.15 + 2 = 36.5 raw → ×1.25 = 45.6 → capped 35x). Using the polymer-segment ROCE for a polymer-only SOTP leg is also defensible (group 36% dilutes with agri). Immaterial to destination PE, hurdle, or decision.

---

## 2. PILLAR 1 — NORMALIZATION ROUTE SELECTION (Section 1B v3.5.1)

| Business | Route A test (CWIP+idle+advances >20% of CE) | Route B test (TEMP DEPRESSED / RECOVERING + 📄 pre-cycle) | Route declared | Re-derivation | Verdict |
|---|---|---|---|---|---|
| A | fails (no >20% capital bloat) | barred — verdict is FIRING (v3.5.1: never on FIRING) | **NONE** | Correct: neither route qualifies | PASS |
| B | fails | barred — verdict is STAGNANT (v3.5.1: "Neither route may be invoked on a STAGNANT or DECLINING verdict") | **NONE** | Correct | PASS |

Both routes correctly declared NONE. The v3.5.1 route-selection rule (Route A governs where both hold; neither on STAGNANT/DECLINING) is honored. No double-credit of any recovery through the denominator/numerator channels.

---

## 3. PILLAR 2 — CASH / ASSET-QUALITY MULTIPLIER

| Business | Framework band | Report | Structural test | Growth offset | Verdict |
|---|---|---|---|---|---|
| A | CFO/PAT 50-70% + FCF positive → 1.15x | 1.15x | Drag located in demerging B; A "clean at segment level" | 0 (correct; no offset claimed) | PASS (minor) |
| B | below 30% / CFO neg → 0.80x base; structural test | 0.80x, STRUCTURAL | Structural (NBS subsidy receivable) | 0 — no offset on structural | PASS (minor) |

**Business A note (MINOR):** the 50-70% band requires "FCF positive," but per-entity FCF is NOT FOUND in B10 (capex detail insufficient). The 0.59x CFO/PAT used is the CONSOLIDATED figure that itself carries the agri drag the model locates OUTSIDE Business A; a truly clean Business A would sit higher (arguably 1.30x territory), so 1.15x is conservative and operator-approved. The FCF-positive qualifier is asserted, not evidenced — an evidence gap (Verifier A territory on existence), not a formula error.

**Business B note (MINOR, flagged for transparency):** Master Pillar 2 maps a *structural* cash drag to **0.65x** ("Assign 0.65x. NO growth offset"), whereas the report holds 0.80x with a STRUCTURAL label and no offset. The 0.65x band, however, is explicitly gated on "rating agency confirms persistent WC," and the rating WC commentary is NOT FOUND (rating_wc_quote NOT FOUND). Absent that confirmation, 0.80x is the defensible floor, and this is the operator-approved determination. Impact if 0.65x were forced: B destination 17.5×0.65 = 11.4x vs 14.0x — a >1x move on B's leg, but B is an AVOID value stub (~5% of SOTP, ~Rs 250 Cr); base value would shift ~Rs 45 Cr (~1% of the ~Rs 4,625 Cr SOTP) and the STOP/AVOID verdict is unchanged. Not decision-material.

Structural-vs-growth-induced test performed for both; no growth offset applied to the structural drag (correct). Rejected Appendix-A premium-scaling (do NOT scale premiums by cash multiplier) was not invoked — correct.

---

## 4. PILLAR 3 — GROWTH VISIBILITY (Amendments 4.1/4.2)

| Business | 3a growth-visibility | 3b moat-formation (EM-gated) | 3c duration | Total | Verdict |
|---|---|---|---|---|---|
| A | 1 of 2 qualifiers → below "any two"; grade C caps 3a at +2x but threshold not met → +0x | EM 22.5 < 25 gate → +0x | no 📄 long order book → +0x | **+0x** | PASS |
| B | commodity, none | EM nil | none | **+0x** | PASS |

3a qualifiers checked for A: capex-embedded growth (📄 uncertain, at most 1); order book (n/a); SOM-CAGR ≥20% WITH capacity cross-check passing (FAILS — capacity gap Rs 633 Cr, "SOM optimistic," cross-check does not pass); delivery grade A/B (grade is C). At most one qualifier → below the "any two" bar → +0x. Correct. EM 22.5 < 25 correctly pays 3b +0x.

---

## 5. STRATEGIC PREMIUM + SINGLE-CREDIT

| Check | Rule | Report | Verdict |
|---|---|---|---|
| A premium | "Strong brand/franchise, limited competition, pricing power" → +2 to +4x | +2x (VP-latex #1 India/#2 global ex-China; sole food-grade PVAc India) | PASS |
| A single-credit | ROCE recovery via Pillar 1 OR Strategic Premium, never both | A is FIRING at current ROCE → no recovery credited in Pillar 1; +2x paid for SCARCITY not ROCE re-rating → the ROCE re-rating route stays barred | PASS |
| B premium | commodity, no scarcity | +0x | PASS |
| One-improvement-one-mechanism | no double-credit | Scarcity (+2x) is not credited in Pillar 1 or Pillar 3; no double count | PASS |

The +2x is taken at the conservative bottom of the strong-franchise band. FTTCP single-credit rule and Amendment 4 honored: because Business A is FIRING at current ROCE, no forward uplift entered Pillar 1, and the strategic premium is explicitly for scarcity (a different lever), so the arrangement is compliant. Correctly matches the task's "A is FIRING at current ROCE so no recovery credited."

---

## 6. UNDISCOVERED ALPHA — ORDERING + QUALIFIERS (Amendment 3)

| Business | Ordering min(Raw×1.25, Cap) | Qualifier 1 listed ≥12m | Qualifier 2 Gate0≥60 or EM≥25 | Qualifier 3 FII+DII<3% | Applies? | Verdict |
|---|---|---|---|---|---|---|
| A | F 36.5 → F2 45.6 → min(45.6, 35) = 35 | JACPL listed Feb-2025 (>12m) ✓ | Gate0 71 ≥60 ✓ | 0.45% <3% ✓ | YES | PASS |
| B | not applied | JASL fresh listing <12m ✗ | — | — | NO | PASS |

UA applied to the RAW PE before the sector-cap comparison; the cap is absolute and UA never breaches it (45.6 → capped 35). All three qualifiers evidenced for Business A (the continuing listed entity). Business B (fresh spin-off) correctly excluded. Matches task: "A applies, B fresh-listing does not."

---

## 7. SECTOR CAP + NO-OUTSIDE-PE

| Item | Rule | Report | Verdict |
|---|---|---|---|
| A cap | Specialty chemicals 35x | 35x (binds) | PASS |
| B cap | Agri processing 20x | 20x (not binding; 14x<20x) | PASS |
| Blended cap | revenue-weighted (SOTP-sanctioned) | 0.627×35 + 0.373×20 = 29.4 ≈ **29.5x** | PASS |
| No exit PE from outside Section 1B | sole authority | A 35x cap, B 14x derived, blended 29.5x — all Section 1B; report states "no round-number default used" | PASS |
| No quality uplift misuse | uplift only if UA + durability ≥ Mod-Strong, stated | No uplift taken (operator-approved); caps kept absolute | PASS |

Revenue-weighted blended cap is a sanctioned SOTP technique (FTTCP SOTP rule blends sector caps revenue-weighted). Blended figure is context-only; SOTP is primary. No exit multiple originates outside Section 1B.

---

## 8. RRM DUAL-TRACK (v3.2 spine + Amendment 4.4)

| Business | r used | RRM = 1+(13.5−r)×0.12 (pct-point) | Track 1 PE | Track 2 PE | Divergence | Governing | Verdict |
|---|---|---|---|---|---|---|---|
| A | 13.5% | 1+(0)×0.12 = **1.00** | 36.5×1.00×1.25 → cap 35x | 35x | 0% | cap binds both | PASS |
| B | 14.0% | 1+(−0.5)×0.12 = **0.94** | 14.0×0.94 = **13.2x** | 14.0x | 6% (<15%) | Track 1 more conservative, moot (stub) | PASS |

Percentage-point reading applied (Amendment 4.4: r=14 → (13.5−14)=−0.5, not −0.005). Both tracks produced and carried through fair values and the verdict card. Divergence <15% on both, so no >15% conservative-track override triggered; the more-conservative Track 1 is correctly noted for B. r=13.5% for A is a modest 0.5pp durability reduction (Moderate-Strong, near-debt-free) within bounds; immaterial as the cap binds A on both tracks.

---

## 9. HURDLE RATIO + VERDICT MAPPING (Amendment 2 / Tier A 1.953)

| Business | HR(Base) re-derivation | HR(Bull) re-derivation | Verdict | Check |
|---|---|---|---|---|
| A | (1.13)³ × (35/27) = 1.4429 × 1.2963 = **1.87** | grade C → bull cap Base+5%=18%; (1.18)³×(35/27) = 1.6430×1.2963 = **2.13** | Base<1.953, Bull≥1.953 → **CONDITIONAL** | PASS (minor) |
| B | (1.03)³ × (14/14) = **1.09** | n/a (fails by nature) | **STOP** | PASS |
| Blended | (1.12)³ × (29.5/25.35) = 1.4049×1.1637 = **1.64** | — | **CONDITIONAL** | PASS |

Tier A threshold 1.953 applied. CONDITIONAL correctly caps the verdict at WATCHLIST/BUY-ON-DIPS with the "growth-dependent with de-rating headwind" flag; no BUY NOW. STOP for the agri stub correctly maps to AVOID.

**MINOR:** the grade-C bull gate is "Base EPS CAGR + 5% *maximum*," so the bull input should be min(modelled 17%, cap 18%) = 17%; the report computes HR(Bull) with 18% (the cap). Recomputed at 17%: (1.17)³×(35/27) = 1.6016×1.2963 = **2.08** — still ≥ 1.953, so CONDITIONAL stands. No verdict change; presentational/computational only.

---

## 10. ROLE 2 (B14) — DECISION RULES + POSITION SIZING

| Rule | Master v3.3 Role 2 | Facts | Verdict |
|---|---|---|---|
| BUY NOW | CMP≤MoS AND Gate0≥GOOD AND Promoter≥TRUSTWORTHY AND HR=PASS | CMP 2,342 > MoS 1,766; Promoter CAUTION; HR CONDITIONAL | correctly excluded |
| BUY ON DIPS | CMP in [MoS, Entry]; ceiling when HR CONDITIONAL | CMP 2,342 ABOVE entry 2,208 | correctly not current |
| WATCHLIST | CMP above Entry, thesis strong | CMP 2,342 > entry 2,208 | **WATCHLIST** — PASS |
| AVOID gates | Gate0 AVG/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR HR STOP | Gate0 GOOD+; Promoter CAUTION; U/D 2.6x; HR CONDITIONAL | AVOID correctly not triggered |
| Position — Large | Gate0 EXCELLENT + Promoter EXEMPLARY/TRUSTWORTHY + EM EXPANSION + CMP<MoS | none hold | excluded |
| Position — Medium | Gate0 GOOD+ + Promoter TRUSTWORTHY + CMP≤Entry | Promoter CAUTION, CMP>Entry | excluded |
| Position — Small | everything else qualifying | 3 constraints (HR CONDITIONAL, grade C, Promoter CAUTION cap) | **Small** — PASS |
| Entry conjunction | must be stated in Section 7 box | present and explicit (Samlaya false-dip warning) | PASS |
| Promoter cap binds | CAUTION caps sizing | applied (Small) | PASS |
| 4D weights | grade C → 35/45/20 | 35/45/20; expected CAGR ~19.9%≈20% | PASS |
| Shared-catalyst flag | Samlaya to Role 3 | flagged as single point of failure | PASS |

WATCHLIST + Small are consistent with CONDITIONAL hurdle + grade C + Tier A + Promoter CAUTION. Position_size_override correctly empty. Entry-conjunction anti-value-trap rule honored.

---

## 11. OPERATOR-APPROVED BASE — APPLIED, NOT SILENTLY RE-DERIVED

B11 §8 states the exit-PE bases were used EXACTLY as operator-approved (A 35x, B 14x, blended 29.5x) and the independent four-pillar math *reproduces* them (A raw 36.5x → cap 35x; B raw 14.0x). The independent re-derivation in this audit confirms the reproduction. No silent re-derivation overrode the approved bases; every FY27+ figure is labelled projected/illustrative; every unresolved input (standalone accounts, per-entity FCF, unit economics, rating WC, forward guidance) is carried as NOT FOUND / illustrative with no estimated fill. Conservative-rule handling of unresolved inputs is honored.

---

## 12. FINDINGS SUMMARY

All four findings are MINOR and none change destination PE materially, flip the Hurdle verdict, or alter the decision. Destination PEs (A 35x, B 14x, blended 29.5x), all three Hurdle verdicts (CONDITIONAL / STOP / CONDITIONAL), and the WATCHLIST / Small decision are CONCURRED.

1. **[MINOR] B11 §2.1 Pillar 1 (Business A):** base 30x rests on segment ROCE 67.5% (B10 flags as inflated/unconfirmable) rather than the "authoritative" group 36% (→24.9x). Immaterial: A's destination caps at 35x under either input.
2. **[MINOR] B11 §2.1 Pillar 2 (Business A):** the 50-70% → 1.15x band requires FCF positive, but per-entity FCF is NOT FOUND; qualifier asserted, not evidenced. Conservative and operator-approved; existence question belongs to Verifier A.
3. **[MINOR] B11 §3.1 Pillar 2 (Business B):** a structural cash drag maps to 0.65x in Master Pillar 2, but 0.80x is held; the 0.65x band is gated on rating-agency confirmation which is NOT FOUND, so 0.80x is defensible and operator/task-endorsed. A 0.65x reading moves B's leg >1x but shifts SOTP ~1% and leaves STOP/AVOID unchanged.
4. **[MINOR] B11 §2.5 Hurdle (Business A):** grade-C bull input should be min(17%, cap 18%)=17%; report used 18%. Recomputed HR(Bull)=2.08 vs 2.13 — still passes; CONDITIONAL stands.

**Rules checked:** 43. **Clean:** 39. **Minor caveats:** 4. **Material/decision-changing fails:** 0.

---

## 13. RECOMPUTED OUTPUTS

- Recomputed destination PE: A **35.0x**, B **14.0x**, blended **29.5x** — CONCUR (no change).
- Recomputed Hurdle: A **1.87 → CONDITIONAL**, B **1.09 → STOP**, blended **1.64 → CONDITIONAL** — CONCUR.
- Recomputed decision: **WATCHLIST / Small** — CONCUR.

---

```yaml
stage: B12c
company: "JUBLCPL"
run_date: "2026-08-18"
model: claude-opus-4-8
status: complete
scope: "phase-3 valuation (B10 + B11 + B14 decision/sizing); gate0/emoat audited in phase 1"
gate0: {rules_checked: 0, fails: [], note: "phase-1 scope, not re-audited"}
emoat: {rules_checked: 0, fails: [], note: "phase-1 scope, not re-audited"}
valuation:
  rules_checked: 43
  fails: []   # zero material/decision-changing fails; 4 MINOR caveats in findings
recomputed_destination_pe: ""   # concur: A 35.0x / B 14.0x / blended 29.5x
recomputed_decision: ""         # concur: WATCHLIST / Small
findings:
  - {severity: "MINOR", location: "B11 §2.1 Pillar 1 (Business A)", description: "Base 30x rests on segment ROCE 67.5% (B10 flags inflated/unconfirmable) vs authoritative group 36% (->24.9x); immaterial, destination caps at 35x under either input."}
  - {severity: "MINOR", location: "B11 §2.1 Pillar 2 (Business A)", description: "50-70% -> 1.15x band requires FCF positive but per-entity FCF is NOT FOUND; qualifier asserted not evidenced; conservative and operator-approved."}
  - {severity: "MINOR", location: "B11 §3.1 Pillar 2 (Business B)", description: "Structural drag maps to 0.65x in Master Pillar 2 but 0.80x held; 0.65x band gated on rating-agency confirmation which is NOT FOUND, so 0.80x defensible/operator+task-endorsed; 0.65x reading shifts SOTP ~1%, STOP/AVOID unchanged."}
  - {severity: "MINOR", location: "B11 §2.5 Hurdle (Business A)", description: "Grade-C bull input should be min(modelled 17%, cap 18%)=17%; report used 18%; recomputed HR(Bull)=2.08 vs 2.13, still passes, CONDITIONAL stands."}
critical_count: 0
major_count: 0
minor_count: 4
acceptance_rate: 91   # 39 clean of 43 checks; all material checks (destination PE, hurdle, decision) fully clean
valuation_framework_adherence: 91
```
