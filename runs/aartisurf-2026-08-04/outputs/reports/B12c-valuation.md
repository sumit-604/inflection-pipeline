# B12c — VERIFIER C: FRAMEWORK ADHERENCE (VALUATION HALF)
# Aarti Surfactants Ltd (AARTISURF) | Run Date 2026-08-04
# Model: claude-opus-4-8 | PHASE 3 valuation-adherence pass ONLY
# Gate 0 + Emerging Moat checks ran in phase 1 (recorded in B12c phase-1); NOT redone here.

**Scope.** Audits the valuation (B10 assembly, B11 valuation) and, extended, Role 2's decision
rules and position-sizing logic (B14) against Master v3.3 / Section 1B v3.3+v3.5.1 / FTTCP v1.2.
Authoritative base = fttcp-deliberation OPERATOR-APPROVED VALUATION PILLARS block. Every rule
re-derived from the framework text; every FAIL carries the recomputed value. Raw number existence
is Verifier A's domain; I audit rule application.

---

## 1. PILLAR 1 — ROCE BASE MULTIPLE

| # | Rule (framework anchor) | Applied value | Re-derivation | Verdict |
|---|---|---|---|---|
| P1.1 | Continuous formula, Amendment 5 (Sec1B v3.3 L75): `0.5×ROCE+7.5` | 12.2x | 0.5×9.30 + 7.5 = 4.65+7.5 = **12.15 → 12.2x** | PASS |
| P1.2 | Floor 9x / cap 24x (Amendment 5) | within band | 9 < 12.15 < 24 | PASS |
| P1.3 | FTTCP ROCE verdict is sole Pillar 1 authority (STAGNANT → current ROCE) | 9.30% statutory | fttcp maps STAGNANT → current ROCE 9.30% (year-end); not normalized | PASS |
| P1.4 | Normalization route (v3.5.1 Amendment 9 route-selection, L22-25) | NONE | Route A needs CWIP+idle+advances >20% of cap employed; CWIP 12.8% < 20% → A fails. Route B needs verdict TEMPORARILY DEPRESSED / RECOVERING; verdict is STAGNANT → B barred. Neither holds → **NONE**, statutory ROCE feeds directly | PASS |
| P1.5 | Single-credit rule (Master v3.3 L228): recovery via Pillar 1 OR Strategic, never both | not credited | STAGNANT = no forward recovery to credit; Strategic Premium ROCE re-rating route correctly barred. Worksheet states route explicitly | PASS |

Pillar 1 = **12.2x**, matching the operator-approved base. Continuous formula used (not the retired
band table). No double-credit. **All 5 rules PASS.**

---

## 2. PILLAR 2 — CASH CONVERSION MULTIPLIER

Determination carried from B10/fttcp (not re-litigated, per rubric): FY26 CFO/PAT 6.05x is a
**one-time working-capital release** (inventory liquidation + payables stretch), NOT structural,
NOT growth-induced.

| # | Rule | Applied | Re-derivation | Verdict |
|---|---|---|---|---|
| P2.1 | Multiplier matches stated determination — volatile band → neutral 1.00x | 1.00x | Volatile band (single non-repeatable good year on a WC release) → neutral 1.00x. Correct band assignment | PASS |
| P2.2 | 0.65x structural penalty requires a rating agency confirming *persistent* WC leakage | not applied | CARE calls liquidity "Adequate" (B10); no persistent-leakage finding → 0.65x correctly withheld | PASS |
| P2.3 | 1.15x/1.30x good-cash rewards require sustained conversion | not applied | Single good year on a WC release does not qualify → rewards correctly withheld | PASS |
| P2.4 | Growth offset attaches ONLY to growth-induced 0.80x-band drag; none on one-time/structural | +0.00 | Cash is one-time WC release, not growth-induced → **no offset**. Effective multiplier 1.00x | PASS |
| P2.5 | Quality-Adjusted Base = Pillar1 × Pillar2 | 12.2x | 12.2 × 1.00 = 12.2x | PASS |

The volatile-band assignment and the no-growth-offset call are both correct given the
one-time-WC-release determination. **All 5 rules PASS.**

Note (MINOR, Verifier-A domain): the CFO/PAT range is quoted inconsistently across artifacts —
B10/B11 say "0.90x FY25 / 6.05x FY26" while the operator-approved pillars say "0.77x to 6.21x."
Band = volatile under either set, so the multiplier (1.00x) is invariant. Flagged for Verifier A,
not decision-relevant here.

---

## 3. PILLAR 3, STRATEGIC PREMIUM, UA, SECTOR CAP

| # | Rule | Applied | Re-derivation | Verdict |
|---|---|---|---|---|
| P3.1 | 3a Growth Visibility, grade-C cap; needs ≥2 of 4 criteria | +0x | Only 1 of 4 qualifies (SOM CAGR 10.6-11.2% < 20% bar; no order book; capex tonnage NOT FOUND); grade C caps at +2x but <2 criteria → **+0x** | PASS |
| P3.2 | 3b Moat Formation floor: EM < 25 → +0x | +0x | EM 13.5 (phase-1 corrected) < 25 → +0x | PASS |
| P3.3 | 3c Duration Premium: needs documented order book / tenor | +0x | none documented → +0x | PASS |
| P3.4 | Strategic Premium; ROCE re-rating route barred by single-credit | +0x | No scarcity, weak pricing power (CARE: limited price pass-through), 71% 2-customer concentration; ROCE route barred (no recovery to credit) | PASS |
| P3.5 | UA Amendment 3 ordering `min(Raw×1.25, Cap)`; all three qualifiers must be evidenced | NOT applied | Listed ≥12m ✓; FII+DII 0.08% < 3% ✓; quality gate Core 55<60 AND EM 13.5<25 ✗. 2 of 3 met → UA NOT applied. Ordering moot (F2 = F) | PASS |
| P3.6 | Sector cap absolute: H = min(F2, G) | 12.2x | min(12.2, 35) = 12.2x; Specialty chemicals 35x **non-binding** | PASS |

**All 6 rules PASS.** Pillar 3 = +0x, Strategic +0x, UA off, cap non-binding — all match the
injected inputs and the operator-approved base.

---

## 4. DESTINATION PE — BOTH TRACKS & DIVERGENCE

| # | Rule | Applied | Re-derivation | Verdict |
|---|---|---|---|---|
| D.1 | Additive F = C + D + E | 12.2x | 12.2 + 0 + 0 = **12.2x**. Governing per operator override (Override 2) | PASS |
| D.2 | RRM formula (Master v3.3 L392; Amendment 4.4 percentage-point reading): `1 + (13.5 − r)×0.12`, floor ×0.70 | 0.70 | r = 14% (small/micro) +2% (weak durability: grade C, 71% concentration, CARE BBB+/BBB, pricing weakness) = 16%, within [9,18]. 1+(13.5−16)×0.12 = 1−0.30 = **0.70** (at floor) | PASS |
| D.3 | Track 1 destination = base × RRM | 8.5x | 12.2 × 0.70 = **8.5x** (range 7.9-9.2x) | PASS |
| D.4 | Both tracks carried through every fair value and the verdict card | yes | Verdict card 4H shows both tracks, RRM 8.5x, divergence, override citation | PASS |
| D.5 | On >15% divergence the conservative track governs entry (Master v3.3 L599; Sec1B) — UNLESS overridden | override | Divergence 43.5% (>15%); framework default = RRM 8.5x governs. Operator Override 2 (phase-3 authority) selects additive 12.2x for the decision; RRM carried as documented conservative alternative and its lower entry (Rs 141-176) disclosed. Deviation from default is authorized, logged, and transparent | PASS (via override) |

**Framework note on D.2/D.5.** The `13.5` in the RRM formula is a **fixed framework constant**
(Master v3.3 L392; confirmed Amendment 4.4), not the EM score — it coincidentally equals AARTISURF's
corrected EM 13.5, so the result (0.70) is unaffected either way. B11 wrote it as `(13.5 − 16)`,
matching the framework literal. No error. All 5 rules PASS; D.5 passes only because the deviation
from the conservative-governs default is carried by a documented operator override.

---

## 5. HURDLE RATIO — THE SFL CONSISTENCY DISCIPLINE (decision-critical)

Framework: Sec1B v3.5.1 Reconciliation L26-34. **HR = (1+EPS CAGR)³ × (Destination PE mid ÷ Current PE)**,
pass threshold 1.953 (Tier A = 1.25³). Verdict map: HR(Base)≥1.953 PASS; HR(Base)<1.953 but
HR(Bull)≥1.953 CONDITIONAL; HR(Bull)<1.953 STOP.

| # | Rule | Applied | Re-derivation | Verdict |
|---|---|---|---|---|
| H.1 | Current PE uses TTM EPS 22.09, NOT B10's 14.10 | 23.68x | 523 / 22.09 = **23.68x**. B11 correctly used 22.09 and flagged B10's 14.10 | PASS |
| H.2 | TTM constructed correctly (roll FY26 forward one quarter) | 22.09 | Correct TTM = FY26 14.99 − Q1FY26 3.62 + Q1FY27 10.72 = **22.09**. (B10's 14.10 = 14.99 − **Q4FY25 11.63** + 10.72 subtracts the WRONG quarter — see Finding VAL-1) | PASS (B11) |
| H.3 | EPS-basis CONSISTENCY: numerator CAGR base = denominator current-PE base | both TTM 22.09 | Base CAGR = (40.40/22.09)^(1/3)−1 = 22.3%; current PE denominator = 22.09. **Both TTM 22.09 — consistent.** This is the SFL discipline honoured | PASS |
| H.4 | HR formula computed correctly | 0.94 base | (1.223)³ × (12.2/23.68) = 1.829 × 0.5152 = **0.94**. Identity check: HR = FV/CMP = 492.9/523 = 0.94 ✓ | PASS |
| H.5 | Credibility-grade gate on Bull (grade C caps bull CAGR at base+5%) | 27.3% | Modeled bull CAGR ~53% barred; capped 22.3+5 = 27.3%. HR(Bull) = (1.273)³ × 0.5152 = 2.063 × 0.5152 = **1.06** | PASS |
| H.6 | STOP verdict: HR(Bull capped) < 1.953 | STOP | 1.06 < 1.953 → **STOP** confirmed | PASS |

**Consistency stress-test.** Because HR = FV/CMP whenever numerator and denominator share one EPS
basis, the decision is invariant to the 22.09-vs-14.10 choice *provided the bases match* — the SFL
trap is an *inconsistent mix* (e.g., TTM denominator against a non-TTM CAGR base). B11 avoided the
trap: both legs are TTM 22.09, HR resolves to 492.9/523 = 0.94, STOP. **HURDLE RATIO STOP confirmed.
All 6 rules PASS.**

---

## 6. ENTRY ZONE, RISK-REWARD, EXPECTED RETURN

| # | Rule | Applied | Re-derivation | Verdict |
|---|---|---|---|---|
| E.1 | Tier A entry = base fair value ÷ 1.953 (Master v3.3 L640; Amendment 4.3) | Rs 252 | 492.9 / 1.953 = **252.4 → Rs 252** | PASS |
| E.2 | MoS = 20% below entry | Rs 202 | 252 × 0.80 = **201.6 → Rs 202** | PASS |
| E.3 | RRM reference entry / MoS | Rs 176 / 141 | 343.4/1.953 = 175.8 → 176; ×0.8 = 141 | PASS |
| E.4 | Upside/Downside ≥ 2x check (Master v3.3 L654) | 0.09x fails | base upside (492.9−523)/523 = −5.8%; bear downside (188.5−523)/523 = −64.0%; ratio 0.09x < 2x. (Base "upside" is itself negative, which already fails — see MINOR VAL-3) | PASS |
| E.5 | Prob-weighted expected CAGR, grade-C weights 35/45/20 | −7.1% | −28.8×.35 −2.0×.45 +19.3×.20 = −10.08 −0.90 +3.86 = **−7.1%** | PASS |
| E.6 | Fair-value ladder = FY30 EPS × destination PE | Rs 189/493/889 | 15.45/40.40/72.85 × 12.2 = 188.5/492.9/888.8 ✓ | PASS |
| E.7 | SOM cross-check performed | done | base rev CAGR 11.1% vs SOM 10.6-11.2% — consistent (B11 §2D) | PASS |

**All 7 rules PASS.** Entry Rs 202-252, MoS Rs 202, both recomputed exactly.

---

## 7. ROLE 2 (B14) — DECISION RULES & POSITION SIZING

| # | Rule (Master v3.3 Role 2, L809-816) | Applied | Re-derivation | Verdict |
|---|---|---|---|---|
| R.1 | AVOID if Gate0 AVERAGE OR Promoter CONCERN/AVOID OR U/D<2x OR HR STOP | AVOID | Gate0 AVERAGE ✓, U/D 0.09x<2x ✓, HR STOP ✓ — three independent triggers → AVOID over-determined | PASS |
| R.2 | Decision AVOID consistent with Hurdle STOP | consistent | HR STOP → verdict card AVOID-on-valuation | PASS |
| R.3 | Position None consistent with no-BUY at CMP | None | No BUY/BUY-ON-DIPS supported at CMP → no position initiated | PASS |
| R.4 | Tier A sizing; Medium/Large barred without Gate0 GOOD+ & Promoter TRUSTWORTHY | Small ceiling | Correctly states: were price in zone, ceiling = Small (2-3%); Gate0 AVERAGE bars Medium/Large; Promoter CAUTION caps; UA not applied. No position-size operator override recorded | PASS |
| R.5 | Thesis-broken condition well-formed (falsifiable, dated) | well-formed | "Q2 AND Q3 FY27 op margin both ≥7.5% (Reg 52(4)) → Margin to STARTING." Clear, testable, tied to the decisive tripwire | PASS |

**All 5 rules PASS.** One presentational nuance (MINOR VAL-4): B14's decision-trace calls Gate0
AVERAGE a "default WATCHLIST superseded by STOP," whereas Master L809 lists Gate0 AVERAGE as a
direct AVOID trigger. Net verdict (AVOID) is correct and over-determined; nuance only.

---

## 8. FINDINGS

**VAL-1 (MAJOR) — B10 assembly TTM EPS mis-constructed.**
B10 reports TTM EPS 14.10 = "FY26 14.99 − Q4FY25 11.63 + Q1FY27 10.72" (B10 L79, and B10 YAML
`ttm_eps_rs: 14.10`). Rolling FY26 forward one quarter requires removing **Q1FY26**, not Q4FY25
(which is not part of FY26). Correct TTM = 14.99 − Q1FY26 3.62 + Q1FY27 10.72 = **22.09**. B11
independently caught and corrected this (B11 L232) and used 22.09 throughout. **Decision-invariant**
because (a) B11 did not propagate the error, and (b) HR = FV/CMP is invariant to the EPS basis when
numerator and denominator stay consistent. Anchor: Sec1B v3.5.1 HR consistency rule; B10 L79 vs
B11 L232. Severity MAJOR (materially wrong number in the assembly, ~23.7x vs 37.1x current PE);
decision survives. Source-existence of Q1FY26 EPS 3.62 (anchor "results 81847a21", outside B10) is
referred to Verifier A.

**VAL-2 (MINOR) — CFO/PAT range quoted inconsistently across artifacts.**
B10/B11 "0.90x FY25 / 6.05x FY26" vs operator-approved "0.77x to 6.21x." Volatile band and 1.00x
multiplier invariant under either. Verifier-A domain; not decision-relevant.

**VAL-3 (MINOR) — Upside/Downside ratio presentation.**
Base upside is itself negative (−5.8%); the 0.09x ratio is |−5.8|/|−64|. The negative base upside
already fails the ≥2x test on its own, so the reported 0.09x is directionally correct but the sign
context should be stated. Cosmetic.

**VAL-4 (MINOR) — B14 decision-trace characterisation.**
Gate0 AVERAGE is a direct AVOID trigger (Master L809), not a "WATCHLIST default superseded by STOP."
Net verdict unaffected (over-determined AVOID). Presentational.

No CRITICAL findings. No finding changes the destination PE (12.2x), the Hurdle verdict (STOP), or
the decision (AVOID).

---

## 9. COMPLIANCE SUMMARY

| Cluster | Rules checked | Pass | Fail |
|---|---|---|---|
| Pillar 1 | 5 | 5 | 0 |
| Pillar 2 | 5 | 5 | 0 |
| Pillar 3 / Strategic / UA / cap | 6 | 6 | 0 |
| Destination PE / tracks / divergence | 5 | 5 | 0 |
| Hurdle Ratio (incl. SFL consistency) | 6 | 6 | 0 |
| Entry / risk-reward / expected return | 7 | 7 | 0 |
| Role 2 decision & sizing (B14) | 5 | 5 | 0 |
| B10 assembly TTM construction | 1 | 0 | 1 (VAL-1) |
| **TOTAL** | **40** | **39** | **1** |

**Valuation framework_adherence = 39/40 = 97.5%.** The single FAIL is an upstream B10 assembly
error that B11 detected and corrected before it reached the decision. The B11 valuation and B14
thesis apply every framework rule as written: continuous Pillar 1 formula, FTTCP STAGNANT as sole
Pillar 1 authority, single-credit honoured, correct volatile-band cash multiplier with no offset,
Pillar 3 +0x on the injected inputs, UA correctly off, sector cap absolute and non-binding, both
tracks carried, RRM computed correctly, the operator-override divergence handling documented and
transparent, the Hurdle Ratio computed with the SFL EPS-basis consistency intact (STOP confirmed),
entry zone and MoS exact, and the Role 2 decision AVOID over-determined and consistent throughout.

Recomputed destination PE: **concur, 12.2x.** Recomputed decision: **concur, AVOID (STOP).**

---

```yaml
stage: B12c-valuation
company: "AARTISURF"
run_date: "2026-08-04"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: []}   # ran in phase 1; not re-audited here
emoat: {rules_checked: 0, fails: []}   # ran in phase 1; not re-audited here
valuation:
  rules_checked: 40
  fails:
    - {id: "VAL-1", severity: "MAJOR", rule: "TTM EPS construction (Sec1B v3.5.1 HR consistency)", location: "B10 L79 / B10 YAML ttm_eps_rs", claimed: "14.10 (14.99 - Q4FY25 11.63 + Q1FY27 10.72)", correct: "22.09 (14.99 - Q1FY26 3.62 + Q1FY27 10.72)", note: "wrong quarter removed; B11 caught and corrected to 22.09; decision-invariant (HR=FV/CMP)"}
recomputed_destination_pe: ""   # concur 12.2x
recomputed_decision: ""         # concur AVOID (Hurdle STOP)
findings:
  - {severity: "MAJOR", location: "B10 assembly (L79, YAML)", claimed: "TTM EPS 14.10 -> current PE 37.1x", recomputed: "TTM EPS 22.09 -> current PE 23.68x", note: "VAL-1; corrected in B11; decision-invariant"}
  - {severity: "MINOR", location: "B10/B11 vs fttcp-deliberation", claimed: "CFO/PAT 0.90x/6.05x vs 0.77x/6.21x", recomputed: "volatile band either way", note: "VAL-2; Verifier-A domain; multiplier 1.00x invariant"}
  - {severity: "MINOR", location: "B11 4F", claimed: "Upside/Downside 0.09x", recomputed: "base upside -5.8% is itself negative; already fails 2x", note: "VAL-3; cosmetic sign context"}
  - {severity: "MINOR", location: "B14 decision-trace", claimed: "Gate0 AVERAGE default WATCHLIST superseded by STOP", recomputed: "Gate0 AVERAGE is a direct AVOID trigger (Master L809)", note: "VAL-4; net AVOID over-determined; presentational"}
critical_count: 0
major_count: 1
minor_count: 3
acceptance_rate: 97.5   # 39 of 40 valuation rules passed
coverage_note: "Valuation-adherence half only: B10 assembly, B11 four-pillar valuation + Hurdle + entry, B14 Role 2 decision/sizing. Gate 0 and Emerging Moat audited in phase 1. Raw number existence deferred to Verifier A. Destination PE 12.2x and decision AVOID(STOP) both concur; single MAJOR is an upstream B10 TTM error corrected in B11 before the decision."
```
