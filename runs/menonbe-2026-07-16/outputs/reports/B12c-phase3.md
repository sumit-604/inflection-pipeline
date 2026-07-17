# B12c (PHASE 3) — VERIFIER C: FRAMEWORK ADHERENCE (MENONBE, 2026-07-16)
Model: claude-opus-4-8 | Scope: PHASE 3 — VALUATION-ADHERENCE half (B10 / B11 / B14),
EXTENDED to Role 2 decision rules and position sizing.
Phase-1 Gate 0 (B01) + Emerging Moat (B07) sections are carried forward UNCHANGED (audited clean:
99% adherence, 0 CRITICAL / 0 MAJOR, 5 immaterial MINOR). This file does NOT overwrite phase-1 B12c.md.

Method: rule-by-rule re-derivation of the Section 1B v3.3 four-pillar build, both valuation tracks,
the Hurdle Ratio, entry/MoS cascade, and the Master v3.3 Role 2 decision rules and sizing rules,
against `frameworks/Master_Project_Prompt_v3.3.md`, `frameworks/Section_1B_v3.3_Amendments.md`, and
`frameworks/FTTCP_v1.2_Consolidated.md`. I audit rule APPLICATION only, not raw-number accuracy
(Verifier A owns numbers) and not company quality. Where an operator override is the input, I test
whether it was correctly APPLIED and LABELED, and whether it reconciles arithmetically.

═══════════════════════════════════════════════════════════════════
## PART 3 — VALUATION (B10 / B11) COMPLIANCE  [NEW THIS PHASE]
═══════════════════════════════════════════════════════════════════

### 3.0 B10 input-assembly discipline
| Rule | Check | Verdict |
|---|---|---|
| Values anchored | Every input carries a source anchor (B01-B09 / deliberation / screener) | PASS |
| Destination PE carried not invented | 25x sourced from deliberation as **Operator Override 2**, labeled | PASS |
| Sector cap carried not invented | Manufacturing/Industrial 25x, "corrected from manifest Agri 20x", labeled | PASS |
| EPS ladder to year AFTER exit | FY31E (exit+1) present in all three ladders; exit year FY30 | PASS |
| Ladder marked ILLUSTRATIVE | Line 271 caveat + line 284 "illustrative pending stage 11" | PASS |
| Pillar 1 illustrative formula (line 211) | `(1+ROCE-CoE)×target ROCE ≈ 22.4x` is arithmetically incoherent (0.8+ fraction), but is tagged "illustrative"; B11 re-derived correctly via Amendment 5 | MINOR (no downstream impact) |
| Bull-cap illustration (line 297) | B10 caps bull off the 5yr base (11.2%+5=16.2%); the Hurdle needs the 3yr base. B10 tagged illustrative; B11 correctly used 3yr 19%+5=24% | MINOR (B11 corrected; no impact) |

### 3.1 Section 1B four-pillar build (B11 §1B) — re-derived
| Rule (authority) | Re-derivation | B11 | Verdict |
|---|---|---|---|
| Pillar 1 continuous (Amd 5: 0.5×ROCE+7.5, floor 9, cap 24) | 0.5×29.8+7.5 = **22.4x** (<24 cap) | 22.4x | PASS |
| Pillar 1 alt (closing ROCE 24%) | 0.5×24.0+7.5 = **19.5x** | 19.5x | PASS |
| FTTCP verdict is sole Pillar 1 authority | SUSTAINED → current ROCE, no trajectory blend; Amd 4.5 N/A (not depressed) | as stated | PASS |
| Single-credit rule stated + route | "ROCE recovery credited via: NOT CREDITED (no depression)"; Strategic re-rating route BARRED | stated | PASS |
| Pillar 2 multiplier matches determination | GROWTH-INDUCED → 0.80 base + 0.05 growth offset = **0.85x**; matches deliberation lock | 0.85x | PASS |
| No offset on structural | Determination is growth-induced, so +0.05 offset is permitted (offset barred only on structural) | correct | PASS |
| Quality-adjusted base | 22.4 × 0.85 = **19.0x** (19.04 → 19.0) | 19.0x | PASS |
| Pillar 3 = injected EM/catalyst input, override labeled | Draft +0x (EM 11, NONE band); carried **+1x as Operator Override 1**, labeled | +1x | PASS |
| Strategic premium single-credit | +0x, ROCE re-rating barred | +0x | PASS |
| Raw destination PE (Row F) | 19.0 + 1.0 + 0.0 = **20.0x** | 20.0x | PASS |
| UA order = min(F×1.25, cap) (Amd 3) | F2 = 20.0×1.25 = **25.0x**; H = min(25.0, 25) = **25.0x** | 25.0x | PASS |
| UA three qualifiers evidenced | listed 30+ yrs; Gate0 grand 70>60; FII+DII ~0.24%<3% — all three | evidenced | PASS |
| Sector cap absolute, not invented | 25x = Section 1B base table row "Cables/Industrial products" & "Recycling/Manufacturing" (Master L355-356) | 25x | PASS |
| Sector cap not breached by UA | UA-adjusted raw lands exactly ON the cap (25.0 = 25); cap not exceeded | PASS |
| Quality-uplift on cap (Master L370) | NOT applied — requires durability ≥Moderate-Strong; EM is NONE. Conservative and moot (raw = cap) | PASS |

**Operator-override reconciliation (CHECK a).** 22.4 × 0.85 = 19.0 → +1.0 (Override 1) = 20.0 → ×1.25 (UA)
= 25.0 = cap (Override 2). Reconciles EXACTLY. Both overrides are clearly labeled "Operator Override 1/2",
distinguished from the framework-derived draft (+0x / 19x-24x), and the coherence check ties out. PASS.

### 3.2 Both tracks + divergence (B11 §1B–§1C)
| Rule (authority) | Re-derivation | B11 | Verdict |
|---|---|---|---|
| Track 1 RRM present, Amd 4.4 pp-reading | RRM = 1 + (13.5 − 14)×0.12 = 1 − 0.06 = **0.94** | 0.94 | PASS |
| RRM r base + bounds | r = 14% (small/micro), bounded [9,18] | 14% | PASS |
| RRM pre-UA + UA + cap | 19.0×0.94 = 17.9 → ×1.25 = 22.4 → min(22.4,25) = **22.4x** | 22.4x | PASS |
| Track 2 additive present | mid **25.0x**, range 23.0–25.0 | 25.0x | PASS |
| Amd 6 proportional range ±7.5% | 25.0 ±7.5% = 23.1–26.9, capped → **23.0–25.0** | 23.0–25.0 | PASS |
| Divergence computed | (25.0 − 22.4)/22.4 = **11.6%** | 11.6% | PASS |
| >15% → conservative track sets entry | 11.6% < 15% → NOT forced; Track 2 (operator-authoritative) governs, RRM carried as conservative x-check with STOP disclosed | PASS (see MINOR) |

*MINOR observation:* at 11.6% divergence the framework does not force the conservative track, so choosing
the operator-authoritative Track 2 for entry is compliant; the maker transparently carries the RRM entry
(FV 260 → entry 133 / MoS 106) and states the RRM-track Hurdle STOPs. No fail; disclosed.

### 3.3 Hurdle Ratio (B11 §1C) — CHECK (c)
| Rule (authority) | Re-derivation | B11 | Verdict |
|---|---|---|---|
| HR formula = (1+g)³ × (Dest mid ÷ Current PE) | PE ratio 25.0/24.3 = 1.0288 | 1.0288 | PASS |
| HR base | (1.19)³ × 1.0288 = 1.6852 × 1.0288 = **1.73** | 1.73 | PASS |
| HR bull (capped) | (1.24)³ × 1.0288 = 1.9066 × 1.0288 = **1.96** | 1.96 | PASS |
| Grade-C bull cap = base + 5 | 19.0 + 5 = **24.0%** (not management 26–30%) | 24% | PASS |
| Verdict mapping (Amd 2) | base FAIL & bull PASS → **CONDITIONAL**, cap WATCHLIST/BUY-ON-DIPS | CONDITIONAL | PASS |
| EPS-basis consistency (SFL lesson) | numerator growth (FY26→FY29 reported EPS) AND denominator current PE (TTM reported EPS 7.83) are BOTH reported-EPS basis — no cash-vs-reported mix; SFL spurious-pass trap avoided | PASS (see MINOR) |
| No exit PE from outside Section 1B (CHECK d) | destination governed solely by Section 1B; no round-number import anywhere | PASS |

*MINOR observation (SFL check):* the growth window (FY26→FY29) and the current-PE anchor (TTM through
Q1 FY27, i.e. between FY26 and FY27) are on the same reported basis but a slightly different start point
(6.82 vs 7.83). Compounding off the LOWER 6.82 while dividing by the HIGHER 7.83-based PE is conservative
(it understates HR), and both legs are reported-EPS, so the SFL basis-consistency requirement is met.
Label looseness only; the CONDITIONAL verdict is robust (STOP on RRM track and on SOM-only base).

### 3.4 Projections, methods, triangulation, entry (B11 §2–§4)
| Rule (authority) | Re-derivation | B11 | Verdict |
|---|---|---|---|
| SOM cross-check performed | base FY29 domestic ~Rs 241 Cr ≈ B09 SOM Rs 240.8 Cr | consistent | PASS |
| §2D sanity checks (incl. Yr3 ROCE vs FTTCP, CFO/PAT vs Pillar 2) | all 8 rows present; FLAG-CASH watch surfaced | present | PASS |
| §4G exit-multiple validation | ROCE / CFO-PAT / catalyst / single-credit / UA-ordering all validated | present | PASS |
| Both fair-value sets carried to verdict card | Track2 153/290/584, Track1 137/260/523 | carried | PASS |
| 4D prob weights match grade (Master L630) | Mixed(C) = 35/45/20; 0.35(−6.9)+0.45(15.1)+0.20(45.3) = **13.4%** | 35/45/20, 13.4 | PASS |
| U/D asymmetry | 52.6% / 19.5% = **2.7x** (≥2x) | 2.7x | PASS |
| Entry = base FV ÷ 1.953 (Tier A) | 290 / 1.953 = **148.5 → 148** | 148 | PASS |
| 30% entry = FV ÷ 2.197 | 290 / 2.197 = **132** | 132 | PASS |
| MoS = 25%-entry × 0.80 | 148.5 × 0.80 = **118.8 → 118** | 118 | PASS |
| No silent fills on unresolved inputs | pledge NOT FOUND (no valuation use); SOTP not applied (no audited segment P&L) — both conservative | PASS |
| Shared-catalyst flag (Amd 4) | export ramp = Pillar 3 driver AND Pillar 2 receivables cause — flagged for Role 3 | flagged | PASS |

═══════════════════════════════════════════════════════════════════
## PART 4 — ROLE 2 (B14) DECISION-RULE & SIZING COMPLIANCE  [EXTENSION]
═══════════════════════════════════════════════════════════════════

| Rule (Master v3.3 Role 2, L806–816) | Check | Verdict |
|---|---|---|
| Verdict consistent with Role 1 | B14 WATCHLIST = B11 WATCHLIST; entry/MoS identical | PASS |
| Entry / MoS not re-invented | Rs 132–148, MoS Rs 118 carried verbatim from B11 §4E | PASS |
| Hurdle-CONDITIONAL ceiling honored | CONDITIONAL → capped at WATCHLIST/BUY-ON-DIPS, no BUY NOW (L807/Amd 2) | PASS |
| AVOID leg: Promoter | CAUTION ≠ CONCERN/AVOID → not triggered (correct) | PASS |
| AVOID leg: Upside/Downside | 2.7x ≥ 2x → not triggered (correct) | PASS |
| AVOID leg: Hurdle | CONDITIONAL ≠ STOP → not triggered (correct) | PASS |
| AVOID leg: Gate 0 (L809: Gate0 AVERAGE/AVOID → AVOID) | Gate 0 IS AVOID; maker overrode to WATCHLIST as "backward artifact" and cited "Gate 0 below GOOD defaults to WATCHLIST" — NOT the literal rule | **FAIL (MAJOR)** — see below |
| Position sizing (L813–816) | Small: Medium needs Gate0 GOOD+ & Promoter TRUSTWORTHY; Large needs Gate0 EXCELLENT & EM EXPANSION. Gate0 AVOID, EM NONE, Promoter CAUTION → **Small** correct | PASS |
| No position-size override | Both operator overrides were valuation-side (Pillar 3, dest PE); none on sizing → override empty | PASS |
| Tier assignment (Amd 4.3) | FII+DII 0.24% < 3% → **default Tier A** by definition; Tier B correctly barred | PASS (see MINOR) |
| Entry conjunction / anti-value-trap (L811) | Stated explicitly in the verdict box and §7 | PASS |
| Thesis-broken conditions | Falsification metric + CFO/PAT + export stall + margin + credibility/governance tripwires stated | PASS |

**MAJOR — Gate 0 AVOID leg override + inaccurate citation (B14 §7, L138).**
Master Role 2 decision rule (L809) lists **"Gate 0 AVERAGE/AVOID"** as an AVOID trigger. Gate 0 here is
AVOID, so a literal reading forces the decision to AVOID. B14 lands on WATCHLIST/BUY-ON-DIPS, justifying
it as a "backward filing-continuity artifact" and citing **"Gate 0 below GOOD defaults to WATCHLIST,"**
which is not in the framework (the framework says: Gate0 < GOOD *bars BUY NOW* per L806, and Gate0
AVERAGE/AVOID *triggers AVOID* per L809). The substantive resolution is defensible under the pipeline's
governing convention — CLAUDE.md ("flags propagate; only mechanical failures halt"), the FTTCP-first
sequencing, and the documented FLAG-GATE0 backward artifact (core AVERAGE 54 downgraded one tier for a
15-year filing gap, not distress) — and it is consistent with Role 1's independently-reached WATCHLIST.
It is also action-neutral at the current price: the verdict explicitly reads "AVOID-on-valuation at CMP
190," so no purchase is authorized today either way. **Why MAJOR not CRITICAL:** the actionable outcome
(no buy at CMP; act only in the Rs 132–148 zone with a clean trigger) is unchanged and the destination PE
/ Hurdle verdict are untouched. **Why not MINOR:** the literal L809 rule points to AVOID and the cited
justification misstates the rule; whether a future dip-buy is *authorized* (WATCHLIST) vs *forbidden*
(strict AVOID) is a real, non-cosmetic decision-label difference. The operator should adjudicate the
label (decision stays human); the recommended fix is to name L809 explicitly and record the Gate0-AVOID
override on backward-artifact grounds, rather than cite a non-existent "defaults to WATCHLIST" rule.

**MINOR — Tier B bar reasoning (B14 §7 tier call).** B14 bars Tier B citing "FLAG-CASH + promoter CAUTION
+ credibility C." Those are valid, but the cleaner and primary reason is mechanical: FII+DII 0.24% < 3%
makes it **Tier A by definition** (Amd 4.3: Tier A is the default when FII+DII < 3%). Conclusion (Tier A)
is correct; only the stated rationale is over-elaborated.

═══════════════════════════════════════════════════════════════════
## CONSOLIDATED FINDINGS (PHASE 3, valuation + Role 2)
═══════════════════════════════════════════════════════════════════
| # | Severity | Location | Description |
|---|---|---|---|
| V1 | MAJOR | B14 §7 decision-rule trace (Gate 0 leg) | Verdict WATCHLIST overrides Master L809 (Gate0 AVERAGE/AVOID → AVOID) and cites non-existent "Gate 0 below GOOD defaults to WATCHLIST." Defensible under pipeline flag-not-gate convention and consistent with Role 1; action-neutral at CMP (AVOID-on-valuation stated). Operator should adjudicate the label. |
| V2 | MINOR | B10 §Pillar 1 (line 211) | Illustrative Pillar 1 formula `(1+ROCE−CoE)×target ROCE ≈ 22.4x` is arithmetically incoherent; tagged illustrative and B11 re-derived correctly via Amendment 5. No downstream impact. |
| V3 | MINOR | B10 bull-cap illustration (line 297) | B10 caps bull off the 5yr base (16.2%); the Hurdle needs the 3yr base. Tagged illustrative; B11 correctly used 3yr 19%+5=24%. No impact. |
| V4 | MINOR | B11 §1C Hurdle EPS window | Growth compounds off FY26 6.82 while current PE uses TTM 7.83 (same reported basis, different start point). Conservative (understates HR); SFL basis-consistency met. Label looseness only. |
| V5 | MINOR | B14 §7 tier call | Tier B bar rationale over-elaborated; primary mechanical reason is FII+DII<3% → default Tier A. Conclusion correct. |

**Recomputation.** Destination PE re-derives EXACTLY: Track 2 additive **25.0x** (22.4×0.85=19.0, +1.0=20.0,
×1.25=25.0=cap), Track 1 RRM **22.4x** (0.94 RRM, UA, cap). Hurdle base **1.73 FAIL** / bull **1.96 PASS**
→ **CONDITIONAL**. Entry **132–148**, MoS **118**. All concur — no destination-PE or Hurdle-verdict change.
The only open item is the Role 2 verdict LABEL (WATCHLIST under pipeline convention vs AVOID under a
literal reading of L809); the actionable outcome (no buy at CMP; buy only in the Rs 132–148 zone) is the
same under both, so the decision survives.

**Rules checked this phase:** Valuation (B10/B11) = 40; Role 2 (B14) = 12. Combined phase-3 = **52 checked,
50 clean, 1 MAJOR fail (V1), 1 soft MINOR fail counted (V2), 3 immaterial MINOR notes (V3–V5).**
Valuation-and-Role-2 **framework_adherence = 94%.**

═══════════════════════════════════════════════════════════════════
## PART 1 — GATE 0 (B01) COMPLIANCE  [CARRIED FORWARD FROM PHASE 1, UNCHANGED]
═══════════════════════════════════════════════════════════════════
Phase-1 result: fully compliant. Core 54, moat 16, grand total 70/160; LIMITED-history one-tier
downgrade of AVERAGE core to **AVOID** applied exactly as written; Block-B<8 deal-breaker correctly
non-binding; all 9 deal-breakers checked; NOT-FOUND fills (pledge, cont-liab) honored, not fabricated.
48 rules checked, 47 clean, 1 soft MINOR (M10 switching-costs scored 1 vs strict-band 0, immaterial to
moat count/classification). Recomputed classification = AVOID — concur. (Full tables in phase-1 B12c.md.)

═══════════════════════════════════════════════════════════════════
## PART 2 — EMERGING MOAT (B07) COMPLIANCE  [CARRIED FORWARD FROM PHASE 1, UNCHANGED]
═══════════════════════════════════════════════════════════════════
Phase-1 result: fully compliant. All 21 categories addressed or explicit NO EVIDENCE; evidence
multipliers applied correctly (no 🎙️-only category scored as 📄); completionist recount performed;
em_score 10.6 → **11**, band **NONE**; double-count discipline honored (B1 not scored, B2 folded into
E2/C1, F2 not force-fit); FTTCP non-conflation stated; combined backward-AVOID + forward-NONE = AVOID.
26 rules checked, 0 fails; 4 immaterial MINOR notes (F2 injected B05 gap, scale-ceiling cosmetic, plus
E2-window and M9 carried under Gate 0). Recomputed em_score/classification — concur. (Full tables in
phase-1 B12c.md.)

---

```yaml
stage: B12c
company: "MENONBE"
run_date: "2026-07-16"
model: claude-opus-4-8
status: complete
phase: 3
gate0:                       # carried forward from phase 1, unchanged
  rules_checked: 48
  fails:
    - {rule: "M10 Switching Costs", severity: MINOR, expected: 0, reported: 1, impact: "moat total 16->15 possible; moat count (3), MODERATE, grand-total band and AVOID classification all unchanged"}
emoat:                       # carried forward from phase 1, unchanged
  rules_checked: 26
  fails: []
valuation:                   # NEW this phase (B10/B11 four-pillar + Role 2 B14 decision rules/sizing)
  framework_adherence_pct: 94
  rules_checked: 52
  fails:
    - {rule: "Role 2 decision rule — Gate 0 AVOID leg (Master L809)", location: "B14 §7", severity: MAJOR, description: "Verdict WATCHLIST overrides literal L809 (Gate0 AVERAGE/AVOID -> AVOID); cites non-existent 'Gate 0 below GOOD defaults to WATCHLIST'. Defensible under pipeline flag-not-gate convention + FLAG-GATE0 backward artifact + Role 1 consistency; action-neutral at CMP (AVOID-on-valuation stated). Operator to adjudicate label."}
    - {rule: "B10 Pillar 1 illustrative formula (line 211)", location: "B10", severity: MINOR, description: "Arithmetically incoherent illustrative formula; tagged illustrative, B11 re-derived correctly via Amendment 5. No impact."}
  notes:
    - "V3 MINOR: B10 line 297 bull-cap off 5yr base (16.2%); B11 correctly used 3yr 19%+5=24%. No impact."
    - "V4 MINOR: Hurdle growth compounds off FY26 6.82 vs current PE on TTM 7.83 — same reported basis (SFL check met), conservative, label looseness only."
    - "V5 MINOR: Tier B bar rationale over-elaborated; primary reason FII+DII<3% -> default Tier A. Conclusion correct."
recomputed_destination_pe: ""   # concur: Track2 additive 25.0x and Track1 RRM 22.4x both re-derive exactly
recomputed_decision: "Actionable outcome concurs (no buy at CMP; buy only Rs 132-148). Open item: Role 2 label WATCHLIST (pipeline convention) vs AVOID (literal Master L809 on Gate 0 AVOID) — operator to adjudicate; no change to destination PE, Hurdle verdict (CONDITIONAL), entry (132-148) or MoS (118)."
findings:
  - {severity: MAJOR, location: "B14 §7 decision-rule trace", description: "Gate 0 AVOID leg (Master L809) overridden to WATCHLIST with inaccurate 'defaults to WATCHLIST' citation; defensible under pipeline convention + Role 1 consistency, action-neutral at CMP; operator to adjudicate label"}
  - {severity: MINOR, location: "B10 Pillar 1 line 211", description: "Illustrative Pillar 1 formula incoherent; tagged illustrative, B11 corrected via Amendment 5; no impact"}
  - {severity: MINOR, location: "B10 line 297", description: "Bull-cap illustrated off 5yr base 16.2%; B11 correctly used 3yr 24%; no impact"}
  - {severity: MINOR, location: "B11 §1C Hurdle EPS window", description: "Growth off FY26 6.82 vs current PE on TTM 7.83; same reported basis (SFL met), conservative; label looseness"}
  - {severity: MINOR, location: "B14 §7 tier call", description: "Tier B bar rationale over-elaborated; primary reason FII+DII<3% -> default Tier A; conclusion correct"}
  # phase-1 MINORs (carried, unchanged):
  - {severity: MINOR, location: "B01 Block F M10", description: "Scored 1 vs strict-band 0; immaterial to moat count/classification"}
  - {severity: MINOR, location: "B01 Block E E2", description: "~2.75yr promoter-change window vs 3yr spec (data limitation, flagged); band unaffected"}
  - {severity: MINOR, location: "B01 Block F M9", description: "+4.05pp GM/rev-CAGR falls between bands; score 1 defensible; no impact"}
  - {severity: MINOR, location: "B07 F2", description: "B05 promise-delivery record absent; self-service concall substitute flagged; F2=0, no scoring impact"}
  - {severity: MINOR, location: "B07 Section 5", description: "Scale ceiling ~84 vs prompt ~0-80; cosmetic, absolute bands unaffected"}
critical_count: 0
major_count: 1
minor_count: 10          # 5 valuation/Role2 (this phase) + 5 gate0/emoat (phase 1)
acceptance_rate: 96      # combined 126 rules checked (48 gate0 + 26 emoat + 52 valuation), 121 clean of a decision-material sense; valuation-half adherence 94%, phase-1 halves 99%
```
