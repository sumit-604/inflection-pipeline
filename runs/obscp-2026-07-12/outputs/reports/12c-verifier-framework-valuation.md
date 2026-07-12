# STAGE 12c: VERIFIER C — FRAMEWORK ADHERENCE (VALUATION HALF, PHASE 3)
## OBSC Perfection Ltd (OBSCP) | Run 2026-07-12 | Model: claude-opus-4-8

**Scope:** Valuation-adherence audit deferred from Phase 1. Gate 0 (B01) and
Emerging Moat (B07) checks already ran in Phase 1 and are NOT re-audited here.
This half audits B11-valuation and B14-thesis against Master v3.3 / Section 1B
v3.3 (Amendments 1-8 + v3.4 4.1-4.4) / FTTCP v1.2, rule-by-rule. Numbers-in-
sources belongs to Verifier A; here the question is only whether each framework
rule was applied AS WRITTEN.

Authorities read: Master_Project_Prompt_v3.3.md (Pillar tables L238-315, RRM
L388-393, Role 2 decision/sizing L804-818), Section_1B_v3.3_Amendments.md
(Amendments 1-8, 4.1-4.4), FTTCP_v1.2_Consolidated.md (ROCE map L328-330,
single-credit L337).

---

## A. PILLAR 1 — ROCE BASE (continuous formula + STAGNANT mapping)

| Rule (as written) | Applied? | Recompute | Verdict |
|---|---|---|---|
| Continuous formula `0.5 × ROCE + 7.5`, floor 9x cap 24x (Amend 5) | Yes | 0.5×15.1 + 7.5 = 15.05 → **15.1x** | PASS |
| FTTCP STAGNANT → **current ROCE**, no midpoint smoothing (FTTCP L330 / Amend-tbl L225) | Yes | STAGNANT ⇒ current 15.1% used; no smoothing | PASS |
| FTTCP verdict is SOLE Pillar 1 authority (FTTCP L402) | Yes | Deliberation STAGNANT consumed, not re-derived (supersedes B07 RECOVERING) | PASS |
| Sensitivity (avg-basis 19.5%) | Yes | 0.5×19.5 + 7.5 = 17.25 → 17.3x | PASS |

No old band table used; continuous formula applied. Year-end 15.1% chosen over
average 19.5% on stated consistency + conservative-bias grounds, average carried
as explicit sensitivity. Compliant.

## B. PILLAR 2 — CASH CONVERSION MULTIPLIER

| Rule (as written) | Applied? | Recompute | Verdict |
|---|---|---|---|
| Base band: CFO/PAT <30% OR CFO negative → 0.80x (Master L247) | Yes | FY26 CFO −1.95 Cr (negative) ⇒ 0.80x band | PASS |
| Structural vs growth-induced test; structural → 0.65x, NO offset (L254) | Yes | Growth-induced (FTTCP Override 1, CRISIL-validated); structural path correctly stated as 0.65x/no-offset falsifier | PASS |
| Growth-offset band: >40% CAGR + growth-induced → +0.20; 25-40% → +0.10 (L263-264) | **Partial** | See finding VAL-1 below | **MINOR** |
| Effective multiplier = base + offset | Yes | 0.80 + 0.20 = **1.00x** | PASS |
| Quality-Adjusted Base = ROCE base × cash mult | Yes | 15.1 × 1.00 = 15.1x | PASS |
| No premium-scaling by cash mult (Appendix A rejected) | Yes | Additive structure preserved | PASS |

**Finding VAL-1 (MINOR).** The +0.20 offset is justified in B11 by "PAT/revenue
CAGR >40% (FY26 revenue growth ~54%; PAT CAGR 48.7%)." The cleanest multi-year
revenue metric anchored in B10 is **revenue CAGR FY24-26 = 38.5%**, which sits
in the 25-40% band → +0.10 (not +0.20). Under a strict revenue-CAGR reading of
the offset rule combined with the 0.80x base, the cash multiplier would be 0.90x,
quality base 13.6x, raw destination ~18.6x. HOWEVER, the framework offset table
does not specify revenue-vs-PAT CAGR, and — decisively — the 1.00x outcome is
**independently supported**: 5-yr cumulative CFO/PAT = 0.31 (31%) falls in the
30-50% "neutral 1.00x" band (Master L246). So the 1.00x multiplier and the 20.1x
destination are robust to the offset-band question; only the stated justification
is aggressive/imprecise. Destination PE and decision UNCHANGED. Severity MINOR.

## C. PILLAR 3 — DECOUPLED 3a/3b/3c (combined +6x cap)

| Component | Rule | Applied? | Verdict |
|---|---|---|---|
| 3a Growth Visibility | +3x iff ≥3 qualifiers AND grade A/B (Amend 4.1) | Capex-embedded 18%≥15%; order book 5.5x≥1.0x; SOM 39.1%≥20%; grade B — 4 qualify, grade B → **+3x** | PASS |
| 3b Moat Formation | EM-gated table; EM<25 → +0x | EM 23 < 25 → **+0x** | PASS |
| 3c Duration Premium | +2x when documented visibility ≥4yr (Amend 4.2) | Order book "5-6 fiscals," 5.5x revenue → ≥4yr → **+2x**; CRISIL-filed + operator Override 2 (genuine) | PASS |
| Combined cap | 3a+3b+3c ≤ +6x | 3+0+2 = **+5x** ≤ 6x | PASS |
| SHARED CATALYST flag | required when catalyst spans pillars (Amend 4) | Flagged (Pillar 1 context + 3a + 3c) | PASS |

3c rests on CRISIL-filed order book plus operator Override 2 rather than raw
signed LoAs; Amendment 4.2 prefers 📄 LoAs, but the operator override is
authoritative and matches the B10-injected `pillar_3_order_book_3c_x: 2`.
Compliant with injected inputs — no finding.

## D. PILLAR 4 — STRATEGIC PREMIUM + SINGLE-CREDIT

| Rule | Applied? | Verdict |
|---|---|---|
| Strategic Premium value | +0x | PASS |
| Single-credit: ROCE recovery in Pillar 1 OR Strategic, never both; route stated (FTTCP L337) | Route = "not credited" (STAGNANT ⇒ nothing entered Pillar 1; nothing in Strategic) | PASS |
| No double-credit of one improvement | ROCE not credited anywhere; qualification lock-in credited once (3a), not re-credited in P4 | PASS |

## E. UA MULTIPLIER (Amendment 3 ordering)

| Qualifier | Framework | B11 | Verdict |
|---|---|---|---|
| Listed ≥12m | required | MET (Oct 2024, ~21m) | ok |
| Gate 0 ≥60 OR EM ≥25 | required | **NOT MET** (core 52<60 AND EM 23<25) | ok |
| FII+DII <3% | required | MET (2.94%) | ok |
| All three | AND | NO → **UA NOT applied** | PASS |
| Ordering `min(Raw×1.25, Cap)`, BEFORE cap, cap absolute (Amend 3) | H = min(F2, G); since UA off, F2 = F = 20.1 | PASS |

## F. SECTOR CAP

Manufacturing **25x** used (fttcp-deliberation), correctly superseding manifest
EPC/Civil 20x. Cap is absolute; UA cannot breach it (UA off anyway). 20.1x <
25x → not binding. PASS.

## G. FOUR-PILLAR ARITHMETIC & RANGE

Raw = QualityBase 15.1 + Growth +5.0 + Strategic +0.0 = **20.1x** ✓.
F2 (UA off) = 20.1x; H = min(20.1, 25) = **20.1x** ✓.
Range ±7.5% (Amend 6): 20.1×0.925 = 18.59; 20.1×1.075 = 21.61 → **18.5–21.5x** ✓.
Avg-basis sensitivity 22.3x (0.5×19.5+7.5=17.25; +5 = 22.25 → 22.3x) ✓. All PASS.

## H. HURDLE RATIO (Amend 2 / 4.3)

| Item | Framework | Recompute | Verdict |
|---|---|---|---|
| Formula | HR = (1+EPS CAGR)³ × (DestPE mid / Current PE) | — | PASS |
| Tier / threshold | Tier A (FII+DII 2.94%<3%) → **1.953** | 1.953 | PASS |
| HR base (33%) | | 1.33³ × (20.1/63.7) = 2.353 × 0.3155 = **0.74** | PASS |
| HR bull (43.4%) | Bull permitted only if grade Good/Excellent (Amend 2 note) | grade B = Good ⇒ permitted; 1.434³ × 0.3155 = **0.93** | PASS |
| Verdict | HR(Bull) < 1.953 → STOP | 0.93 << 1.953 → **STOP** | PASS |

## I. RRM DUAL-TRACK (Amend 4.4)

| Item | Recompute | Verdict |
|---|---|---|
| r build | 14.0 (small-cap) + 0.5 (durability MODERATE) + 0.5 (governance CAUTION) = **15.0%**, in [9,18] | PASS |
| RRM = 1 + (13.5 − r)×0.12, pct-points | 1 + (13.5−15.0)×0.12 = 1 − 0.18 = **0.82**, in [0.70,1.60] | PASS |
| Track 1 dest PE | 20.1 × 0.82 = 16.48 → **16.5x**; range ±7.5% → 15.5–17.5x | PASS |
| Both tracks carried through fair values / verdict card | Track 1 & Track 2 in every FV row + verdict card | PASS |
| Divergence / conservative track governs entry (>15%) | (20.1−16.5)/18.3 = 19.7% > 15% → Track 1 (16.5x) sets entry | PASS |
| Reconciliation stated | Both tracks STOP; choice does not change decision | PASS |

## J. DESTINATION-PE RANGE, ENTRY, MoS

Entry = base FV / 1.953 (Tier A, Amend 4.3): Track 2 492/1.953 = **252**;
Track 1 404/1.953 = **207**. MoS = entry × 0.80 = 207×0.80 = **166**. All ✓ PASS.
SOM cross-check performed: base 33% < SOM 39.1% → CONSISTENT ✓.

## K. ROLE 2 (B14) DECISION RULES & POSITION SIZING

| Rule (Master L804-818) | B14 | Verdict |
|---|---|---|
| AVOID if Gate0 AVERAGE OR U/D<2x OR Hurdle STOP | Verdict AVOID (all three fire: AVERAGE, 0.5x, STOP) | PASS |
| Position None at CMP (no BUY when Hurdle STOP) | Position "None" at CMP | PASS |
| Sizing caps: Gate0 AVERAGE blocks Medium/Large; Promoter cap binds | Re-engagement "Small max" — Gate 0 AVERAGE + Promoter CAUTION | PASS |
| Entry conjunction stated in Section 7 (Amend Role 2 / L811) | Stated explicitly (withdrawn-zone logic) | PASS |
| Both tracks + verdict card consistency with B11 | Entry 207-252, MoS 166, targets 404/492 match B11 | PASS |

---

## SUMMARY

34 valuation-adherence rules checked. 33 clean; 1 MINOR (VAL-1, growth-offset
justification — outcome robust via cumulative-band independent support). No CRITICAL,
no MAJOR. Recomputed destination PE **concurs at 20.1x** (Track 2) / 16.5x (Track 1);
recomputed decision **concurs: AVOID / Hurdle STOP**. The valuation applies Section
1B v3.3 + v3.4 amendments and FTTCP v1.2 as written; the single MINOR is a stated-
rationale imprecision that does not move the destination PE, the Hurdle verdict, or
the decision.

acceptance_rate = 33/34 = **97%**.

---

```yaml
stage: B12c
component: valuation-adherence   # PHASE 3 half; gate0/emoat done in phase 1
company: "OBSCP"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
valuation:
  rules_checked: 34
  fails:
    - rule: "Pillar 2 growth-offset band selection (Master L263-264)"
      severity: "minor"
      recompute: "B11 used +0.20 (>40% via PAT CAGR 48.7% / FY26 rev +54%); anchored 3yr revenue CAGR 38.5% sits in 25-40% band → +0.10. Offset table does not specify revenue-vs-PAT CAGR. 1.00x multiplier independently upheld by cumulative CFO/PAT 0.31 (31%) in 30-50% neutral band, so destination PE unchanged."
recomputed_destination_pe: ""   # concur: 20.1x Track 2 / 16.5x Track 1
recomputed_decision: ""         # concur: AVOID / Hurdle STOP
findings:
  - {severity: "minor", location: "B11 Section 1B, Pillar 2 growth offset", note: "+0.20 offset justified on PAT CAGR 48.7% / single-year revenue 54%; anchored 3yr revenue CAGR is 38.5% (<40%, → +0.10 band). Outcome (1.00x cash mult, 20.1x destination) robust because cumulative CFO/PAT 31% independently supports the 1.00x neutral band. Stated rationale imprecise; no effect on destination PE, Hurdle (STOP), or decision (AVOID)."}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 97   # rules passed (33) / checked (34)
```
