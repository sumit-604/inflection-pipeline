# VERIFIER C — FRAMEWORK ADHERENCE (VALUATION HALF, B12c)

**Company:** RAMRAT | **Run:** 2026-07-29 | **Model:** claude-opus-4-8
**Scope:** Phase 3 valuation-adherence audit of B11 (Role 1) + B10 inputs, EXTENDED to B14 (Role 2) decision rules and position sizing. Gate 0 (B01) and Emerging Moat (B07) compliance were completed in Phase 1 and are NOT re-run here.
**Frameworks audited against:** Master v3.3 (Section 1B Four-Pillar, Role 1, Role 2, Amendment 4.3), Section 1B v3.3 Amendments, Section 1B v3.5.1 Reconciliation (Route A/B), FTTCP v1.2.
**Discipline:** I audit RULE APPLICATION, re-deriving each value. Verifier A owns raw-number existence; I do not re-check that a figure appears in a source PDF.

---

## TABLE 1 — PILLAR-BY-PILLAR (B11) COMPLIANCE

| # | Rule (framework) | Recomputed | Report value | PASS/FAIL |
|---|---|---|---|---|
| V1 | Pillar 1 continuous formula 0.5×ROCE+7.5 (Amdt 5 / Master L211) on ROCE 23.55% | 0.5×23.55+7.5 = 19.275 → **19.3x** | 19.3x | PASS |
| V2 | FTTCP RECOVERING (~55%) handled per Pillar 1 table; recovery NOT credited via documented deliberation override (FTTCP override conditions; single-credit) | Current-ROCE treatment; base 19.3x | recovery not-credited, 19.3x | PASS (see Obs 1) |
| V3 | Route A CWIP test: (CWIP+capex advances) > 20% of capital employed? (v3.5.1) | 2.7% < 20% → Route A FAILS | Route A fails | PASS |
| V4 | Route B applicability: backward TEMPORARILY DEPRESSED + 📄 pre-depression median? (v3.5.1 / Amdt 4.5) | Backward SUSTAINED, ROCE at 5-yr high, no trough → Route B N/A; route NONE | Route NONE | PASS |
| V5 | Single-credit: Strategic Premium ROCE re-rating barred; +0x strategic | Recovery not credited → strategic route disclosed & +0x (also no archetype support) | +0x, barred | PASS |
| V6 | Pillar 2 cash multiplier matches determination. INDETERMINATE; 0.65x needs rating-agency structural confirmation (CARE quote FY25-dated, predates reversal) → 0.65x unsupported; negative-CFO growth-phase band = 0.80x | **0.80x** | 0.80x | PASS |
| V7 | Growth offset WITHHELD on non-affirmed-growth (offset applies only to growth-induced; CLAUDE.md INDETERMINATE cannot resolve favourably) | +0.10x withheld | withheld | PASS |
| V8 | Quality-adjusted base = 19.3 × 0.80 | 15.44 → **15.4x** | 15.4x | PASS |
| V9 | Pillar 3a Growth Visibility: +2x needs any two of four 📄 tests | 1 of 4 pass (capex 14%<15%, no order book, SOM 10.9-11.4%<20%, grade B) → **+0x** | +0x | PASS |
| V10 | Pillar 3b Moat Formation: EM<25 → +0x | EM 21 < 25 → +0x | +0x | PASS |
| V11 | Pillar 3c Duration: ≥2.5yr documented order book | none → +0x | +0x | PASS |
| V12 | Strategic Premium (rare licence/brand/turnaround) | none → +0x | +0x | PASS |
| V13 | UA Amendment 3 ordering min(F×1.25, Cap), UA on RAW PE before cap | UA not applied → min(15.4×1.00, 25)=15.4 | 15.4x | PASS |
| V14 | UA three-qualifier gate: Q1 listed≥12m TRUE; Q2 Gate0≥60 OR EM≥25 FALSE (40, 21); Q3 FII+DII<3% UNANCHORED → all_met FALSE | NOT APPLIED (1.00x) | NOT APPLIED | PASS |
| V15 | Sector cap ABSOLUTE, Cables/Industrial products = 25x (Master L355), supersedes manifest 38x | 25x | 25x | PASS |
| V16 | Final Destination PE H = min(F2, G) | min(15.4, 25) = **15.4x** | 15.4x | PASS |

## TABLE 2 — DUAL-TRACK, HURDLE, TIER, 4D (B11)

| # | Rule (framework) | Recomputed | Report value | PASS/FAIL |
|---|---|---|---|---|
| V17 | BOTH tracks present and carried through every fair value + verdict card (Master L390, L599) | Track 1 RRM 11.7x + Track 2 15.4x in Sec 1B, Sec 3-4, verdict card, YAML | both present | PASS |
| V18 | RRM = 1 + (13.5 − r)×0.12, percentage-point reading (Amdt 4.4), r=15.5% | 1 + (13.5−15.5)×0.12 = 1−0.24 = **0.76** (in [0.70,1.60]) | 0.76 | PASS |
| V19 | r build: small/micro base 14% +1.5% governance CONCERN/Moderate durability, bound [9,18] | 15.5% in bounds | 15.5% | PASS |
| V20 | Track 1 destination PE = 15.4 × 0.76 | 11.704 → **11.7x** | 11.7x | PASS |
| V21 | Divergence >15% → conservative track governs by default; operator override to Track 2 must be RECORDED not silent (Master L599) | (15.4−11.7)/15.4 = **24.0%**; override recorded L85/262 + YAML governing_track | 24.0%, recorded | PASS (see Obs 2) |
| V22 | Hurdle Ratio HR = (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE), forward basis (Amdt 2 / 4.3) | base (1.159)³=1.557; 1.557×(15.4/36.1)=**0.66** | 0.66 | PASS |
| V23 | Bull HR usable (grade B permits bull, Amdt 2 note); STOP if bull HR < 1.953 | (1.296)³=2.177; 2.177×(15.4/36.1)=**0.93** < 1.953 → STOP | 0.93, STOP | PASS |
| V24 | Current forward PE = CMP ÷ FY27 EPS | 454.40/12.58 = **36.1x** | 36.1x | PASS |
| V25 | Bull-case gate: bull EPS CAGR permitted only if credibility A/B | grade B (Good) → bull permitted | permitted | PASS |
| V26 | Tier assignment: Tier A default; Tier B needs FII+DII≥3% AND Gate0 GOOD+/EM≥25 AND promoter TRUSTWORTHY+ AND no structural FLAG-CASH (Amdt 4.3) | FII+DII unanchored, Gate0 AVERAGE, promoter CONCERN, FLAG-CASH → Tier A, threshold 1.953 | Tier A / 1.953 | PASS |
| V27 | 4D weights match credibility grade B = Good → Bear 25 / Base 50 / Bull 25 (Master L629) | 25/50/25 | 25/50/25 | PASS |
| V28 | Entry = base FV ÷ Tier A divisor 1.953; MoS = entry × 0.80 | 278.4/1.953 = **142.5**; ×0.80 = **114** | 142.5 (134-153), 114 | PASS |
| V29 | SOM cross-check performed; base within SOM CAGR, bull ceiling flagged | base 11% within 10.9-11.4%; bull 14% capex-ceiling flagged bull-only | performed | PASS |
| V30 | Earnings basis FORWARD applied as operator-approved; unresolved inputs handled by conservative rule, no silent fills; one-improvement-one-mechanism (no double credit) | FORWARD applied; FCF NOT FOUND→DCF excluded; FII+DII unanchored→UA not applied; dep/interest flagged estimates; recovery credited once (Pillar1 route + strategic barred) | all honoured | PASS |

**Valuation rules checked: 30. Fails: 0.**

---

## TABLE 3 — B14 (ROLE 2) DECISION-RULE & POSITION-SIZING COMPLIANCE

| # | Rule (Master v3.3 Role 2) | Report value | PASS/FAIL |
|---|---|---|---|
| B1 | AVOID if Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D <2x OR Hurdle STOP (L809) | AVOID; all four conditions met (AVERAGE 40, CONCERN, 0.0x, STOP) | PASS |
| B2 | Promoter CONCERN → default AVOID regardless of everything (L916) | verdict AVOID, CONCERN cap cited as overriding | PASS |
| B3 | Position size caps: Large=Gate0 EXCELLENT+Promoter TRUSTWORTHY+; Medium=Gate0 GOOD++Promoter TRUSTWORTHY; Promoter cap binds (L815-818) | Small ceiling only; both Large/Medium gates fail; Promoter CONCERN cap binds; zero at CMP | PASS |
| B4 | Operator position-size override must be recorded, not silently applied | position_size_override blank; explicitly states no override recorded this session | PASS |
| B5 | Entry conjunction (anti-value-trap) stated in Section 7 verdict box (L811) | stated (price zone AND no thesis-broken trigger; withdrawn-zone rule) | PASS |
| B6 | FLAG-CASH INDETERMINATE caps quality at PROCEED WITH CAVEATS (CLAUDE.md); decision consistency | AVOID (harder) governs; cap acknowledged, not silently upgraded | PASS |

**B14 decision-rule rules checked: 6. Fails: 0.**

---

## OBSERVATIONS (non-graded, immaterial to destination PE / verdict / decision)

**Obs 1 (V2) — "would RAISE ROCE" characterization.** B11 line 30 states the mechanical FTTCP RECOVERING (40-60%) 60/40 current/FY[Y+2] blend "would RAISE ROCE and Pillar 1." Read against the RECOVERING expectation (FY[Y+2] > current post-capex) this is internally consistent and defensible; read against the report's own conservative FY28 estimate (~22%, below current 23.55%) the blend would instead land ~19.0x, marginally BELOW the 19.3x used. Either way the impact is ≤0.3x on Pillar 1 (~0.24x on destination PE), well within the 1x tolerance, and the value used (current 23.55% → 19.3x) is the correct, conservative-in-intent treatment (recovery not credited). No finding.

**Obs 2 (V21) — operator override of conservative-governs.** Framework default (Master L599) is that the conservative track (Track 1 RRM 11.7x) sets the entry zone when divergence >15% (here 24%). The operator elected Track 2 additive 15.4x. This is a documented operator override (B11 L85/262, YAML governing_track; B10 flags it AUTHORITATIVE OPERATOR OVERRIDE), carried transparently through both tracks, and immaterial because the decision is AVOID on BOTH tracks. Recorded, not silent — the audit requirement is satisfied.

**Obs 3 — r governance adjustment magnitude.** The +1.5% governance/durability adder on r (14%→15.5%) is a judgment magnitude; it is within [9,18] and affects only the non-governing Track 1. No decision impact.

---

## CONCLUSION

The valuation (B11) and the Role 2 decision layer (B14) apply Master v3.3 / Section 1B v3.5.1 / FTTCP v1.2 as written. Every destination-PE-relevant computation re-derives cleanly (Pillar 1 19.3x, cash 0.80x, quality base 15.4x, RRM 0.76 → Track 1 11.7x, sector cap 25x, HR base 0.66 / bull 0.93 STOP, entry 142.5, MoS 114). The FTTCP recovery is single-credited (Pillar 1 route with strategic barred), UA is correctly withheld on failed/unanchored qualifiers, the sector cap is applied absolute at 25x (not the manifest 38x), both tracks are carried, and the operator override of conservative-governs is recorded rather than silently applied. The AVOID decision is supported on all four independent Role 2 triggers, position sizing caps bind correctly, and no position-size override is silently applied.

**Destination PE: CONCUR (Track 2 15.4x / Track 1 11.7x). Decision: CONCUR (AVOID). No CRITICAL, MAJOR, or MINOR findings.**

Total rules checked: 36 (30 valuation + 6 B14). Passed: 36. Acceptance rate: 100%.

---

```yaml
stage: B12c-valuation
company: "RAMRAT"
run_date: "2026-07-29"
model: claude-opus-4-8
valuation: {rules_checked: 30, fails: []}
b14_decision_check: {rules_checked: 6, fails: []}
recomputed_destination_pe: ""
recomputed_decision: ""
findings: []
critical_count: 0
major_count: 0
minor_count: 0
acceptance_rate: 100
```
