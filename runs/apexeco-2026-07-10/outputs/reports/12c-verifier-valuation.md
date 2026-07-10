# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (B12c)
## Phase 3: Valuation + Role 2 Decision-Rule Adherence
## Apex Ecotech Ltd (APEXECO) — Run Date 2026-07-10

**Scope of this run:** PHASE 3 valuation-adherence half only. Gate 0 (B01) and
Emerging Moat (B07) compliance were audited and closed in Phase 1 and are NOT
re-computed here (see `gate0` / `emoat` marked "completed phase 1" in the YAML).

**Inputs audited:** B11 valuation (`.../reports/11-valuation.md`), B10 assembly
(`.../reports/10-assembly.md`, carried-input cross-check only), B14 Role 2 thesis
(`.../reports/14-thesis.md`). Frameworks: Master v3.3 (Role 1 Section 1B + Role 2),
Section 1B v3.3 Amendments, FTTCP v1.2.

**Discipline:** I audit rule APPLICATION, not raw numbers (Verifier A owns numbers)
and not company quality. Where CLAUDE.md leniency calibrates a Master gate
(no STOP verdict; company quality never halts; low institutional ownership is
never a risk), I audit against the calibrated rule, not the literal Master text.

---

## PART 1 — ROLE 1 SECTION 1B (B11) RULE-BY-RULE

| # | Rule (as written) | Applied? | Verdict | Recomputed / Note |
|---|---|---|---|---|
| V1 | Pillar 1 continuous formula; **elite branch for ROCE>33%** | Partially | **MINOR** | ROCE 33.39% > 33% → elite branch `24 + 0.3×(33.39−33) = 24.12 → 24.1x`. Report used **24.0x**, citing Amendment 5 single-branch cap 24x as primary and treating the elite branch as a "materially identical" cross-check. Master v3.3 body is the operative form (elite cap 30x). Deviation 0.1x. Immaterial: Track 2 capped at 20x regardless; Track 1 = 24.1×0.70 = 16.9x vs reported 16.8x. No output flips. |
| V2 | FTTCP ROCE verdict is the SOLE Pillar 1 authority | Yes | PASS | FTTCP verdict FIRING → mapping table row "Current ROCE" → 33.39% used. Ex-cash ~77% correctly held as CONTEXT ONLY, not the input. Correct. |
| V3 | Single-credit rule; route stated in writing | Yes | PASS | "ROCE recovery credited via: Pillar 1." Strategic-Premium route explicitly NOT used. FIRING uses current ROCE (no smoothing, no forward uplift), so no recovery is even being credited twice. Stated as required. |
| V4 | Pillar 2 multiplier matches growth-induced determination; correct offset | Yes | PASS | Determination GROWTH-INDUCED. Base 0.80x (growth-phase drag, FY25 CFO negative) + 0.20 offset (PAT/Rev CAGR 60.2%/67.3% both >40% + growth-induced) = 1.00x. Convergence check to neutral band (0.40–0.41 → 1.00x, no offset) lands identically. Effective 1.00x. |
| V5 | Offset-stacking trap: offset applies only to the 0.80x drag band, not above neutral | Yes | PASS | Report explicitly did NOT stack +0.20 on the 1.00x neutral band (would have wrongly produced 1.20x for a FLAG-CASH name). Held at 1.00x. Conservative bias honoured. |
| V6 | No offset if structural | Yes (N/A path handled) | PASS | Correctly classified growth-induced (offset allowed). Structural path would be 0.65x, no offset; not taken. Falsification trigger (H1 FY27 CFO/PAT <0.7x AND WC days > revenue) named. |
| V7 | Pillar 3 matches EM / catalyst / evidence inputs | Yes | PASS | EM 10.1 (<25) → table row "EM below 25 → +0x" regardless of catalyst proximity. Growth Visibility Premium +0x. Correct. |
| V8 | Strategic Premium correct (single-credit) | Yes | PASS | No licence/monopoly/IP; Veolia "alliance" contradicted by management. ROCE re-rating route NOT used (ROCE already in Pillar 1). +0x. |
| V9 | UA in Amendment 3 order; all three qualifiers evidenced | Yes | PASS | Q1 listed ≥12m: B10's ~7-month listing-date error CORRECTED (listed Dec-2024 → ~19 months) → MET. Q2 Gate0 86 ≥60 → MET. Q3 FII+DII<3%: **unevidenced** (only promoter 69.29% disclosed) → treated as NOT satisfied → UA NOT applied. Correct conservative handling: an unevidenced qualifier cannot be assumed favourable. F2 = F = 24.0. Ordering min(F×1.25, cap) respected in form. |
| V10 | Sector cap absolute (EPC 20x) | Yes | PASS | EPC/Civil construction → 20x per table. H = min(24.0, 20.0) = 20.0. No quality uplift (UA not triggered → correctly none). Cap treated as absolute. |
| V11 | BOTH tracks present and carried through every fair value and the verdict | Yes | PASS | Track 1 (RRM 15.5/16.8/18.0) and Track 2 (additive 18.5/20.0/20.0) both derived, both in 3/4A fair-value tables and the 4H verdict card. |
| V12 | Conservative track governs entry on >15% divergence | Yes | PASS | Divergence (20.0−16.8)/20.0 = 16.0% > 15% → Track 1 (RRM, more conservative) governs entry. Correct. |
| V13 | Hurdle Ratio computed correctly; credibility-grade gate on Bull | Yes | PASS | Current PE 18.7x. Track 1: (1.22)³×(16.8/18.7)=1.8158×0.8984=1.63; Bull (1.35)³×0.8984=2.460×0.8984=2.21. Track 2: 1.8158×1.0695=1.94; 2.460×1.0695=2.63. Base FAIL / Bull PASS → CONDITIONAL both tracks. Bull EPS CAGR permitted because grade B (A/B gate). Correct. |
| V14 | Hurdle CONDITIONAL cap (WATCHLIST/BUY-ON-DIPS; no BUY NOW) | Yes | PASS | Flag "growth-dependent with de-rating headwind" applied; verdict capped accordingly. |
| V15 | 4D probability weights match the grade | Yes | PASS | Grade B (Good) → Bear 25 / Base 50 / Bull 25, exactly the Master 4D "Good" row. No Role 4 re-weighting trigger fired. |
| V16 | SOM cross-check performed | Yes | PASS | SOM-implied 3yr CAGR 23.1%; base revenue CAGR set to 23% = cut to SOM ceiling. Stated "consistent (cut to SOM)". |
| V17 | Every unresolved input handled by stated conservative rule; no silent fills | Yes | PASS | FCF estimated with ±20% flagged, tertiary weight only; FII+DII NOT FOUND → UA withheld (conservative); peer medians NOT COMPUTED → relative multiples qualitative; capex flat-ratio assumption stated. No estimated number substituted for a NOT FOUND. |
| V18 | One-improvement-one-mechanism (no ROCE double-credit) | Yes | PASS | ROCE credited once (Pillar 1). RRM r built from governance (+1.5%) + durability (+0.5%), NOT from ROCE. Strategic premium 0. SHARED-CATALYST (WC unwind drives both Pillar 1 ROCE and Pillar 2 cash) flagged for Role 3, not double-credited into the multiple. |

**Track derivations independently re-checked:**
- RRM = 1 + (13.5 − 16.0)×0.12 = 1 − 0.30 = 0.70 (exactly the ×0.70 lower bound). r = 16.0% within [9,18]. Track 1 = 24.0×0.70 = 16.8x < cap 20x. Correct.
- Fundamental Base PE for RRM = raw four-pillar 24.0x (C+D+E). Correct input.

---

## PART 2 — ROLE 2 DECISION & POSITION-SIZING (B14)

| # | Rule (Master 804-817, CLAUDE.md-calibrated) | Verdict | Note |
|---|---|---|---|
| R1 | BUY NOW gate: CMP≤MoS AND Gate0≥GOOD AND Promoter≥TRUSTWORTHY AND Hurdle=PASS | PASS | Correctly fails all four (CMP 242>MoS 161; Gate0 AVERAGE; Promoter CAUTION; Hurdle CONDITIONAL). No BUY NOW. |
| R2 | BUY ON DIPS: CMP between MoS and Entry (ceiling when Hurdle CONDITIONAL) | PASS | CMP 242 > Entry high 202, so not active today. Correctly not selected. |
| R3 | WATCHLIST: CMP above Entry, thesis strong | PASS | CMP 242 > Entry 202, FTTCP +5 forward thesis → WATCHLIST. Correct mapping. |
| R4 | AVOID triggers: Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR Hurdle=STOP | PASS (MINOR note) | Under CLAUDE.md ("only mechanical failures halt; company quality never halts; no STOP verdict"), Gate0 AVERAGE (a cash-driven quality cap) surfaces as a flag, not a forced AVOID — the calibrated reading. Promoter=CAUTION (not CONCERN/AVOID) → no trigger. Hurdle=CONDITIONAL (not STOP) → no trigger. **U/D:** the framework-defined 4F ratio is base-upside ÷ modal-bear-downside ≈ 62.8% / 4.1% ≈ 15x (>2x) → AVOID does not fire. Report instead **headlines U/D = 1.9x**, which is a constructed structural-cash *tail* metric, not the 4F ratio; it is explicitly reconciled ("modal-bear U/D benign") but headlining a non-standard tail figure as "the" U/D could invite a literal AVOID misread. Decision (WATCHLIST) is correct and unaffected. |
| R5 | Position size — Large / Medium / Small; promoter cap always binds | PASS | Large fails (Gate0 not EXCELLENT, EM not EXPANSION, Promoter not EXEMPLARY/TRUSTWORTHY, CMP>MoS). Medium fails (Gate0 not GOOD+, Promoter not TRUSTWORTHY, CMP>Entry). Promoter CAUTION binds → Small (2-3%), to be taken only if/when CMP enters ₹161-202. Correct. |
| R6 | Position-size operator override | PASS | "none recorded" — consistent with FTTCP deliberation (operator ruled ROCE + cash only, not sizing). Not fabricated. |
| R7 | Return-matrix cross-check (Master Section 5) | PASS | 3x3 (Track 1): cells ≥25% = 3/9 (bull row); ≥15% = 5/9 (bull row + base at 16.8x/18.0x). Independently recomputed and confirmed. |

---

## PART 3 — CARRIED-INPUT CROSS-CHECK (B10 → B11)

- B10 assembly recorded the UA listing-date qualifier as **NO** (~7 months) and
  `listed_12m: false`. B11 correctly identified and **overrode** this as a factual
  error (listed Dec-2024 → ~19 months at run date → qualifier 1 MET). The net UA
  outcome (NOT applied) is unchanged because qualifier 3 (FII+DII<3%) remains
  unevidenced. Correction is properly documented in B11 and its YAML input_gaps.
  No silent propagation of the B10 error. PASS.
- Cash determination GROWTH-INDUCED, ROCE 33.39%, credibility B, sector cap 20x,
  EM 10.1/NONE all carried faithfully from B10 into B11 pillar inputs. PASS.

---

## FINDINGS (valuation + Role 2 only)

1. **MINOR — Pillar 1 elite branch not used as primary (B11 Pillar 1).** For
   ROCE 33.39% (>33%) the Master v3.3 body's operative continuous formula is the
   elite branch: `24 + 0.3×(33.39−33) = 24.1x`. B11 used **24.0x** citing the
   Amendment 5 single-branch cap (24x), relegating the elite branch to a
   cross-check. Correct value 24.1x. Impact: none — Track 2 is capped at the
   20x EPC sector cap either way, and Track 1 shifts only 16.8x → 16.9x; Hurdle,
   fair values, and verdict all unchanged. Presentational imprecision.

2. **MINOR — U/D ratio headlined as a tail metric (B11 4F / B14 Section 5).**
   The reported/YAML `upside_downside_ratio: 1.9` is the structural-cash *tail*
   scenario, not the Master 4F base-upside/modal-bear-downside ratio (≈15x). The
   report reconciles this ("modal-bear U/D benign"), so no rule is broken and the
   AVOID gate (U/D<2x) does not actually fire on the framework metric — but
   surfacing 1.9x as the headline U/D could invite a literal AVOID misapplication
   by a downstream reader. Decision unaffected.

**No CRITICAL, no MAJOR.** No misapplication changes the destination PE by >1x,
flips the Hurdle verdict, or flips the decision.

## RECOMPUTE

- **Destination PE:** CONCUR. Track 1 (RRM) 15.5/16.8/18.0x; Track 2 (additive)
  18.5/20.0/20.0x; Final governing 16.8x. The elite-branch correction (24.1 vs
  24.0) does not move the capped Track 2 (20.0x) and moves Track 1 mid by ≤0.1x.
  No restated value required.
- **Decision:** CONCUR. WATCHLIST, position Small, entry ₹161-202. Correct under
  the Hurdle CONDITIONAL cap and CLAUDE.md-calibrated AVOID gates.

## ACCEPTANCE

Rules checked: 25 (18 Section 1B/Role 1 + 7 Role 2). Rules with a genuine (if
immaterial) misapplication: 1 (V1, elite branch). Second finding is a
presentational note on a rule (R4) that was otherwise correctly navigated.
Acceptance rate = 24/25 = 96%. Well above the 60% REWORK floor.

```yaml
stage: B12c
company: "APEXECO"
run_date: "2026-07-10"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 0, fails: [], note: "completed phase 1 - not recomputed"}
emoat: {rules_checked: 0, fails: [], note: "completed phase 1 - not recomputed"}
valuation:
  rules_checked: 25
  fails:
    - {rule: "Pillar 1 elite branch for ROCE>33%", severity: "MINOR", used: "24.0x", correct: "24.1x", impact: "none - Track2 capped at 20x, Track1 mid shifts <=0.1x"}
recomputed_destination_pe: ""   # concur: Track1 16.8x / Track2 20.0x, governing 16.8x
recomputed_decision: ""         # concur: WATCHLIST, Small, entry 161-202
findings:
  - {severity: "MINOR", location: "B11 Pillar 1 / Four-Pillar Summary row A", claimed: "ROCE base 24.0x (Amendment 5 cap 24x)", correct: "elite branch 24.1x (Master v3.3 body, ROCE>33%)", note: "Immaterial; Track2 sector-capped at 20x, Track1 16.8x->16.9x; Hurdle/verdict unchanged"}
  - {severity: "MINOR", location: "B11 4F / B14 Section 5 & YAML upside_downside_ratio", claimed: "U/D 1.9x headlined", correct: "framework 4F U/D (base upside / modal bear) ~15x", note: "1.9x is a structural-cash tail metric; reconciled in text; AVOID gate does not fire on framework metric; decision unaffected"}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 96             # 24 of 25 valuation+Role2 rules passed clean
```
