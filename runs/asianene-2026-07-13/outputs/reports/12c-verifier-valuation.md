# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 3: VALUATION-ADHERENCE AUDIT)
## Asian Energy Services Limited (ASIANENE) | Run 2026-07-13 | Model Opus 4.8

**Scope this run:** Rule 4 valuation-adherence audit of B11 (Role 1), EXTENDED to Role 2 (B14)
decision rules and position sizing. Gate 0 (B01) and Emerging Moat (B07) checks already ran in
Phase 1 and are NOT re-done. This audits rule application only — not company quality, not raw
numbers (Verifier A owns numbers). Framework authorities read: Master v3.3 (Role 1 Section 1B,
RRM dual-track, Hurdle, UA ordering, sector cap, Role 2 decision/sizing), Section 1B v3.3
Amendments (3, 4, 4.1-4.5, 5, 6, 8), FTTCP v1.2 single-credit + ROCE authority.

---

## PART A — PILLAR-BY-PILLAR COMPLIANCE (B11)

| # | Rule (as written) | B11 application | Verdict |
|---|---|---|---|
| 1 | Pillar 1 continuous formula 0.5×ROCE+7.5, floor 9 cap 24 (Amdt 5) | 0.5×13.71+7.5 = 14.355 → 14.4x; within [9,24] | PASS |
| 2 | FTTCP ROCE forward verdict = sole Pillar 1 authority; STAGNANT → current ROCE | STAGNANT → current 13.71% used; no ad-hoc trajectory | PASS |
| 3 | Single-credit rule: recovery via Pillar 1 OR Strategic, never both; route stated | "credited via: not credited"; Strategic ROCE re-rating BARRED | PASS |
| 4 | Amdt 4.5 normalized-ROCE anchor applies ONLY if backward TEMPORARILY DEPRESSED AND forward RECOVERING | Correctly NOT applied (backward STRUCTURALLY LOW, forward STAGNANT); stated | PASS |
| 5 | Pillar 2 determination matches FTTCP (growth-induced, not structural) → base band | GROWTH-INDUCED + RP overlay → 0.80x band (CFO/PAT <30%/growth-phase) | PASS |
| 6 | Offset rule: growth-induced eligible; NO offset on structural | Offset applied (growth-induced), not zeroed; not treated as structural | PASS (see M1) |
| 7 | Effective multiplier and QA base arithmetic | 0.80+0.05 = 0.85x; 14.4×0.85 = 12.24x | PASS |
| 8 | Pillar 3a "any two qualify → +2x"; grade-C caps 3a at +2x | Only 1 of 4 qualifiers (order book) → +0x | PASS |
| 9 | Pillar 3b EM-gated table; EM 25-29 any timeline → +1x | EM 28.0 → +1x | PASS |
| 10 | Pillar 3c duration: +1x if ≥2.5yr visibility | 1,750/791 = 2.21yr < 2.5 → +0x | PASS |
| 11 | Pillar 3 combined +6x cap; shared-catalyst flag; no double-credit | +1x (within cap); SHARED CATALYST flagged; no double-credit (Pillar 1 got 0 ROCE uplift) | PASS |
| 12 | Strategic Premium; single-credit bars ROCE re-rating | +0x; re-rating BARRED; no monopoly/institutional backing | PASS |
| 13 | UA Amendment 3 order; all 3 qualifiers must hold | listed YES, EM≥25 YES, FII+DII<3% UNRESOLVED → UA NOT applied (conservative) | PASS |
| 14 | Sector cap absolute; UA never breaches | min(13.24, 20) = 13.2x; cap not binding; Agri-processing rejected, 20x used | PASS |
| 15 | Both tracks present, carried through all FV + verdict card | Track 2 (12-14x) and Track 1 RRM (8.5-10x) in worksheet, 4A, verdict card | PASS |
| 16 | RRM formula percentage-point reading (Amdt 4.4), bounds ×0.70-×1.60 | 1+(13.5−16)×0.12 = 0.70 (= floor); r=16% derived 14+1.5+0.5 | PASS |
| 17 | >15% divergence → more conservative track governs entry | 30% divergence → Track 1 RRM governs entry Rs75-93 | PASS |
| 18 | Hurdle Ratio (1+CAGR)³ × (DestPE mid/Current PE); Tier A ≥1.953 | HR base 1.728×(13.2/29.98)=0.76; bull 1.953×0.4403=0.86 | PASS |
| 19 | Grade C → Bull EPS CAGR capped at Base+5% | Bull 25% = Base 20% +5%; mgmt 30-40% correctly not used | PASS |
| 20 | SOM cross-check performed | SOM 28.2% vs base rev CAGR 20% (cut for capacity gap); Sec 2D | PASS |
| 21 | Every unresolved input → stated conservative rule, no silent fills | FCF, share count, UA, Oilmax, FY27 margin all handled explicitly | PASS |
| 22 | Destination PE range = mid ±7.5%, nearest 0.5x (Amdt 6) | 13.2 → 12.0-14.0; 9.27 → 8.5-10.0 | PASS |

**Recomputed destination PE:** CONCUR — Track 2 13.2x, Track 1 RRM 9.3x. No FAIL beside any row.

---

## PART B — HURDLE / DECISION RE-DERIVATION

- Current PE 29.98x = 340 / 11.34 (diluted). Correct basis.
- HR(Base 20%) = 1.20³ × (13.2/29.98) = 1.728 × 0.4403 = **0.76**.
- HR(Bull 25%, grade-C capped) = 1.25³ × 0.4403 = 1.953 × 0.4403 = **0.86**.
- HR(Bull) < 1.953 → **STOP** (Amendment 2: overvalued, 25% infeasible even on bull earnings). Correct.
- Note: Hurdle uses Track 2 mid (13.2). Using the governing conservative Track 1 mid (9.3) gives
  HR base 0.53 / bull 0.60 — deeper STOP. Choice of the higher Track 2 mid is the LESS favourable-to-STOP
  reading and still yields STOP, so the verdict is robust to track choice (M3, immaterial).

---

## PART C — STRESS TEST OF THE ONE JUDGEMENT DEVIATION (Pillar 2 offset)

The Master offset table maps ">40% CAGR + growth-induced → +0.20". B11 applied **+0.05** (tempered
for RP-receivable concentration, single positive CFO print, cumulative CFO/PAT 0.21x), per the FTTCP
handoff "growth offset eligible but tempered" and the Master conservative-bias operating rule.

Materiality test — take the strict table maximum +0.20 (the LEAST conservative reading):
- Effective multiplier 0.80+0.20 = 1.00x; QA base 14.355×1.00 = 14.4x
- Raw PE = 14.4 + 1 + 0 = 15.4x; UA not applied; min(15.4, 20) = **15.4x**
- HR(Base) = 1.728 × (15.4/29.98) = 0.89; HR(Bull) = 1.953 × 0.5137 = 1.00 — **both still < 1.953 → STOP**

Conclusion: the tempering is (a) conservative (lowers PE), (b) framework-authorized via the FTTCP
determination + conservative-bias rule, and (c) IMMATERIAL — even the strict table maximum keeps
Hurdle STOP and decision AVOID. Logged as **M1 (MINOR)**, not a rule fail. Destination-PE swing
from tempering (13.2x vs 15.4x) does not cross into a decision or Hurdle flip.

(Out of scope note: B10 records cumulative CFO/PAT 0.53x while B11 uses 0.21x — a numbers question
owned by Verifier A, not adjudicated here. Either figure sits below the 30% band, so the 0.80x band
assignment is unaffected regardless.)

---

## PART D — EXTENDED ROLE 2 (B14) DECISION-RULE + POSITION-SIZING AUDIT

| # | Rule (Master Role 2 / Amdt 4.3) | B14 application | Verdict |
|---|---|---|---|
| 23 | Role 2 verdict consistent with Role 1 (hardest verdict wins) | Both AVOID; Role 1 valuation + Role 2 promoter cap reconciled | PASS |
| 24 | AVOID triggers: Gate0 AVERAGE/AVOID OR Promoter CONCERN OR U/D<2x OR Hurdle STOP | All three cited (Gate0 core 37 AVOID; Promoter CONCERN; Hurdle STOP + U/D ~0). Triple-bound | PASS |
| 25 | BUY NOW gate (CMP≤MoS AND Gate0≥GOOD AND Promoter≥TRUSTWORTHY AND Hurdle PASS) | Correctly fails all four; not offered | PASS |
| 26 | Tier assignment (Amdt 4.3): Tier A when TURNAROUND / FII+DII<3% | Tier A / 25% declared on verdict-card line 1; entry divisor 1.953 used | PASS |
| 27 | Tier B Medium-ceiling logic applies ONLY to Tier B | Correctly NOT invoked — this is Tier A; sizing driven by promoter cap instead | PASS |
| 28 | Position size: Promoter caps always bind; Small = 2-3% | Large/Medium fail their gates; Promoter CONCERN cap → Small (2-3%) ceiling; size ZERO at CMP | PASS |
| 29 | Entry-conjunction anti-value-trap rule stated in verdict box | Present ("BOTH hold — price in zone AND no falsifier fired") | PASS |
| 30 | Role 2 valuation numbers must match B11 (no invention) | Entry 75-93, MoS 75, FV 249/182 base, 300/222 bull, U/D ~0, Hurdle STOP — all match | PASS |

**Position-sizing note:** The task flagged "Tier B ceiling logic vs FLAG-PROMOTER CONCERN." The
correct framework path here is that Tier B does NOT apply (ASIANENE is Tier A: TURNAROUND, FII+DII<3%
test unresolved-but-Tier-A-holds). B14 correctly sizes via the Master Small/Medium/Large gates and the
binding Promoter-CONCERN cap → Small ceiling, ZERO at CMP. No misapplication.

**M2 (MINOR):** B14 offers a re-engagement zone (Rs75-93) for a name that is Gate0-AVOID AND
Promoter-CONCERN. The strict Master rule is "Promoter CONCERN → AVOID regardless." B14 mitigates this
correctly: it holds the current decision at AVOID, caps any future ceiling at "BUY-ON-DIPS at most, small
speculative tranche," states explicitly that Gate0 and Promoter caps "never clear," and gates re-entry on
the checklist. The current decision (AVOID) is unaffected; this is presentational nuance, not a flip.

---

## PART E — RECOMPUTATION SUMMARY

| Item | B11/B14 | Verifier C recompute | Concur? |
|---|---|---|---|
| Pillar 1 base | 14.4x | 14.36 → 14.4x | YES |
| Cash multiplier | 0.85x | 0.85x (conservative; 1.00x strict still STOP) | YES |
| QA base | 12.24x | 12.24x | YES |
| Pillar 3 | +1x | +1x (3a 0 / 3b 1 / 3c 0) | YES |
| Raw / Final destination PE (Track 2) | 13.24 / 13.2x | 13.24 / 13.2x | YES |
| Track 1 RRM | 9.3x (r16, RRM 0.70) | 9.27 → 9.3x | YES |
| Hurdle | 0.76 / 0.86 → STOP | 0.76 / 0.86 → STOP | YES |
| Decision | AVOID | AVOID | YES |

**recomputed_destination_pe:** (blank — concur, 13.2x Track 2 / 9.3x Track 1)
**recomputed_decision:** (blank — concur, AVOID)

---

## FINDINGS

- **M1 (MINOR)** — B11 Pillar 2: growth offset tempered from the table +0.20 to +0.05. Conservative,
  FTTCP-authorized, documented; immaterial (strict +0.20 → PE 15.4x still Hurdle STOP / AVOID).
- **M2 (MINOR)** — B14 Section 7: re-engagement zone offered for a Gate0-AVOID + Promoter-CONCERN name;
  strict "Promoter CONCERN → AVOID regardless" mitigated by ceiling caps and checklist gate; current
  decision AVOID unaffected.
- **M3 (MINOR)** — B11 Hurdle uses Track 2 mid (13.2x) rather than the governing conservative Track 1
  mid (9.3x). Using Track 1 gives a deeper STOP; verdict robust to track choice; immaterial.

No CRITICAL and no MAJOR: no misapplication changes destination PE across a decision/Hurdle threshold,
flips the Hurdle verdict, or flips the decision. All 30 rules substantively applied as written; the three
MINOR items are conservative/presentational and do not fail their rules.

```yaml
stage: B12c-valuation
company: "ASIANENE"
run_date: "2026-07-13"
model: claude-opus-4-8
status: complete
scope: "Phase 3 valuation-adherence (rule 4) + extended Role 2 (B14) decision/sizing. Gate0 & EMoat done in Phase 1, not re-run."
valuation:
  rules_checked: 22
  fails: []
role2_check:
  rules_checked: 8
  verdict_consistent_with_role1: true
  decision_rule_trace_correct: true      # AVOID triple-bound: Gate0 AVOID, Promoter CONCERN, Hurdle STOP + U/D<2x
  tier_assignment: "A (25%) — correct; Tier B Medium-ceiling logic correctly NOT invoked"
  position_sizing_correct: true          # Promoter-CONCERN cap binds -> Small (2-3%) ceiling, ZERO at CMP
  fails: []
recomputed_destination_pe: ""            # concur: Track2 13.2x / Track1 RRM 9.3x
recomputed_decision: ""                  # concur: AVOID (on-valuation)
findings:
  - {severity: "MINOR", location: "B11 Pillar 2 offset", note: "Offset tempered +0.20->+0.05; conservative, FTTCP-authorized; immaterial (strict +0.20 -> 15.4x still Hurdle STOP)."}
  - {severity: "MINOR", location: "B14 Section 7 re-engagement zone", note: "Zone offered for Gate0-AVOID + Promoter-CONCERN name; mitigated by ceiling caps + checklist gate; current decision AVOID unaffected."}
  - {severity: "MINOR", location: "B11 Hurdle Ratio track choice", note: "Uses Track 2 mid 13.2x not governing Track 1 mid 9.3x; Track 1 gives deeper STOP; verdict robust."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100    # 30/30 rules substantively passed; 3 MINOR notes are conservative/presentational, no rule failed
```
