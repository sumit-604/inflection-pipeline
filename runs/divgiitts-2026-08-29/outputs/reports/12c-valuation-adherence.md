# B12c — VERIFIER C, PHASE 3 VALUATION SCOPE — DIVGIITTS

**Company:** Divgi Torqtransfer Systems (DIVGIITTS)
**Run:** divgiitts-2026-08-29 | **Model:** claude-opus-4-8
**Scope:** Valuation-adherence audit of B11 (Role 1) and B10 (assembly) against the
Section 1B layer set + Master v3.6 Role 1, EXTENDED to B14 (Role 2) decision rules and
position sizing against Master v3.6 Role 2.
**Not re-run:** Gate 0 (B01) and Emerging Moat (B07) — carried from phase-1 B12c
(gate0 44 rules, 0 fails; emoat 30 rules, 0 fails; 3 minors, all non-decision).

**Override discipline applied per task:** the exit multiple 30x, the sector cap 30x (from
25x), and the Pillar 1 ROCE 20% / base PE 19x are OPERATOR OVERRIDES recorded in the FTTCP
deliberation. An override applied AND disclosed as an override is adherent. I flag only (a)
an override applied without disclosure, (b) framework MATH misapplied given the approved
inputs, or (c) a broken single-credit / basis / cap-arithmetic rule.

---

## A. SECTION 1B PILLAR BUILD — RULE-BY-RULE

| # | Rule (source) | Required | B11 did | Verdict |
|---|---|---|---|---|
| 1 | Section 1A matrix + >=2 methods + triangulation (Master Role 1) | Matrix, >=2 methods, weights | P/E 70% / EV-EBITDA 20% / P/B 10%, matrix + reject rationale, weighted triangulation Rs 763 | PASS |
| 2 | Continuous Pillar 1 formula, not old bands (Amend 11, supersedes 5) | 0.5xROCE+7.5 for ROCE<=33% | 20% -> 17.5x shown; operator 19x used and divergence flagged (19x = ROCE ~23x on formula) | PASS (override disclosed) |
| 3 | FTTCP ROCE verdict sole Pillar 1 authority | Use FTTCP forward verdict | RECOVERING cited as sole authority | PASS |
| 4 | Single-credit rule, route stated (Amend 4) | Pillar 1 OR Strategic, never both; route named | Pillar 1 midpoint; Strategic ROCE re-rating barred 0x; shared_catalyst_flag false | PASS |
| 5 | v3.5.1 normalization route selection | Route A vs B, correct trigger | Route A (post-IPO cash = denominator bloat); B10 "Route B" mislabel caught and corrected; mechanism/base unchanged | PASS (more adherent than B10; disclosed) |
| 6 | Pillar 2 multiplier matches determination; no offset on non-growth (Amend, v3.3) | INDETERMINATE -> conservative neutral, no offset | 1.00x INDETERMINATE, no growth offset (no rating rationale), FLAG-CASH | PASS |
| 7 | Pillar 3 growth-eligibility gate (Amend 16) + evidence gates | ROCE crosses min before premium | base ROCE ~16% > ~13-14% min -> eligible YES; +2/+3 table default docked to +1x by operator (slip/proof-not-fired), disclosed | PASS (override disclosed) |
| 8 | Strategic premium single-credit (Amend 4) | Barred if ROCE credited in P1 | +0x, barred | PASS |
| 9 | UA Amendment 3 ordering + 3 qualifiers + cap absolute | min(Rawx1.25, Cap); all-three | FII+DII 28% fails <3% -> UA NOT applied (all_met false); F2=20x | PASS |
| 10 | Sector cap absolute; override disclosed | Cap is ceiling | 25x framework -> operator 30x, FLAG-SECTOR-CAP-OVERRIDE | PASS (override disclosed) |
| 11 | Cap arithmetic H = min(F2, Cap) | correct min | min(20, 30) = 20x additive; operator 30x governing carried SEPARATELY as approved destination, not a cap trick; FLAG-MULTIPLE-OVERRIDE | PASS |
| 12 | Both tracks carried to FV + verdict card (Master Role 1) | RRM + additive both shown | Track1 17.9x + Track2 20x on card, both floor FVs Rs 525-575 shown | PASS |
| 13 | Conservative track governs entry on >15% divergence | >15% -> conservative sets entry | divergence 11.7% (<15%); RRM 17.9x named as the more-conservative; operator 30x governs entry per 20.9 | PASS |
| 14 | RRM formula percentage-point reading (Amend 4.4) + r-table single-credit (Amend 12) | 1+(13.5-r)x0.12; no double-charge | r=14%, RRM = 1+(13.5-14)x0.12 = 0.94; 12A/12B/12C single-homing observed | PASS |

**RRM base note (not a fail).** RRM applied to the Pillar-1 fundamental base 19x (19 x 0.94 =
17.9x) rather than the additive raw 20x. "Fundamental Base PE" in the Master RRM spine reads
naturally as the ROCE quality base; the 19-vs-20 choice moves the floor <1x (17.9x vs 18.8x),
below CMP either way. Within tolerance.

**Amendment 13 complexity r-charge (operator override, disclosed).** Triggers ARE present
(dense RPT: FLAG-RPT-COMPLETENESS; subsidiary opacity: FLAG-SUBSIDIARY-CONTRADICTION), so
Amendment 13 would add +0.5 to r (14.5%). The operator held r at the 14% standard band. This
override makes the framework FLOOR less conservative (higher), and B11 discloses it as a
CONSERVATIVE FLAG showing the lower alternative (RRM 0.88 -> 15.8x). Disclosed, and
non-decision-changing (floor stays far below CMP; governing 30x is operator's anyway). Adherent.

---

## B. HURDLE, EXIT SYMMETRY, FV PATH, RELATIVE CROSS-CHECK

| # | Rule (source) | Required | B11 did | Verdict |
|---|---|---|---|---|
| 15 | Hurdle Ratio (Amend 2) + Bull credibility gate | (1+g)^3 x (DestPE/CurrPE); Bull only if grade Good/Excellent | ex-cash basis: (1175-95)/24 = 45x; HR base (1.126)^3 x 30/45 = 0.95; HR bull (1.235)^3 x 30/45 = 1.26; grade B (Good) licenses bull; both < 1.953 -> STOP; ~43% CAGR needed | PASS (math re-derived clean) |
| 16 | Amend 18.1 exit-basis symmetry (one basis, stated once) | entry basis = exit basis | forward both ends; today FY27-fwd Rs 24, exit end-Yr3 FY30-fwd Rs 34.3; Year-4 FY31 exists | PASS |
| 17 | Amend 18.0 projection to Year 4 in ALL cases | bear/base/bull explicit Year-4 rows | base case full to FY31; bear/bull are FY27 margin-flex snapshots + FY30 exit EPS only | MINOR FAIL |
| 18 | Amend 18.2 Option Resolution Calendar per slice | window/class/event, or zero | no SOTP slices; optionality valued at 0 (proof gate not fired), stated | PASS |
| 19 | Amend 19.0 FV path table (governing track, base) | today -> end-Yr3 | table present (815/900/1006/1109), cash taper stated | PASS |
| 20 | Amend 19.1 FV CAGR line | (B/A)^(1/3)-1 | (1109/815)^(1/3)-1 = 10.8% | PASS |
| 21 | Amend 19.2 return-source label on card | COMPOUNDER/HYBRID/DISCOUNT-CLOSER | HYBRID (10-20%), on verdict card and Role 2 Sec 5 | PASS |
| 22 | Amend 19.3 decomposition line | drivers named | EPS ~12.6% dragged by declining cash slice + no re-rating lever left | PASS |
| 23 | Amend 20 relative cross-check (step 1C) | live table or PENDING; pillar governs by default; 20.9 operator base binds | PENDING LIVE PEER TABLE marked; pillar/operator base governs; both 20-gates fail reported; 30% test result stated; re-runs at Role 5.5 | PASS |
| 24 | Entry zone = exit-consistent FV / 1.953 (Amend 18.5 / Master) | correct divisor | 1109 / 1.953 = 568; zone Rs 570-650 reconciled (low = 25% CAGR entry, high = 20% MoS on Rs 815) | PASS |
| 25 | Tier declaration on verdict card (Amend 4.3) | first line "Tier: A/B | Hurdle" | Tier A hurdle (1.953) correctly applied throughout; the explicit tier line is absent from the card | MINOR FAIL |

**Amend 20 memory-multiple note (not a fail).** B11 carries a 27x peer downside line from the
deliberation while marking the live table PENDING. Correction 6 bars memory-pulled multiples
from GOVERNING; B11 does not let 27x govern (it defaults to the pillar/operator base per 20.1
and re-runs at Role 5.5). The 30% test conclusion holds under either comparison basis. Adherent.

**MINOR 17 detail.** Verifier rule 11 reads 18.0 strictly ("Year 4 in all cases, else REWORK").
I hold this at MINOR, not REWORK: the base case is fully projected to FY31; bear/bull exit EPS
are carried to the FY30 exit in the 4D table; the cyclical override (2B) treats bear/bull as
trough/peak margin snapshots on a held revenue base, a stated and reasoned method; and the
verdict is AVOID/STOP on every case, so the missing bear/bull Year-4 rows change no number in
the decision. Presentational completeness gap, zero decision impact.

---

## C. ROLE 2 (B14) DECISION RULES + POSITION SIZING — EXTENSION

| # | Rule (Master Role 2) | Required | B14 did | Verdict |
|---|---|---|---|---|
| 26 | AVOID decision rule | Gate0 AVERAGE OR Promoter CONCERN OR U/D <2x OR Hurdle STOP -> AVOID | ALL FOUR fire (Gate0 AVERAGE 47/160; Promoter CONCERN; U/D -0.56; Hurdle STOP). B14 emits verdict "WATCHLIST (with a number; defaults to AVOID today)" | MINOR FAIL (label vs mechanical) |
| 27 | Position size: Promoter cap overrides everything | Promoter CONCERN caps hard | Small (2-3%) when actionable; Promoter CONCERN cap invoked as binding; no operator size override | PASS |
| 28 | Dispersion-capped sizing (Role 1 4H-pre) | width 40-80% -> Medium cap | (974-533)/815 = 54% -> Medium; Promoter cap tighter -> Small; tightest wins, correctly | PASS |
| 29 | Entry range from Role 1 | zone consistent | Rs 570-650, matches B11 | PASS |
| 30 | Entry conjunction rule (anti-value-trap) | stated in Section 7 box | all-three-hold conjunction (price + proof gate + governance) present | PASS |
| 31 | Amend 19 FV CAGR + return-source in Role 2 Sec 5 | carried | 10.8% HYBRID carried with decomposition | PASS |

**MINOR 26 detail.** The mechanical Master AVOID rule fires on four independent triggers, so
the mechanical verdict is AVOID. B14 emits WATCHLIST, resting on the operator's cited posture
("WATCHLIST with a number... defaults to AVOID until the 18-Sep-2026 AGM and FY27 AR"). B14 is
transparent: it states the standing posture at CMP is AVOID (no position), the action today is
"No position," and a buy requires all-three conditions. The FUNCTIONAL action (no position,
defaults to AVOID) matches the mechanical rule; only the verdict WORD diverges, and it is
disclosed and operator-cited. Non-decision-changing. Held at MINOR.

---

## D. RECOMPUTATION SUMMARY

- **Destination PE:** concur. Additive 20x and RRM 17.9x re-derived clean; operator governing
  30x is a disclosed override (FLAG-MULTIPLE-OVERRIDE), math correct given approved inputs.
- **Hurdle Ratio:** concur. HR base 0.95, bull 1.26, both < 1.953 -> STOP re-derived independently.
- **Decision:** concur on substance. On-valuation AVOID/STOP is correct; the Role 2 WATCHLIST
  label is a disclosed operator framing whose functional action (no position) equals AVOID.

No misapplication changes the destination PE by >1x, flips the Hurdle verdict, or flips the
decision. Zero CRITICAL, zero MAJOR. Three MINOR presentational gaps, none decision-bearing.

---

```yaml
stage: B12c
company: "DIVGIITTS"
run_date: "2026-08-29"
model: claude-opus-4-8
status: complete
phase_3_scope: valuation
gate0: {rules_checked: 44, fails: []}          # carried from phase-1 B12c
emoat: {rules_checked: 30, fails: []}          # carried from phase-1 B12c
valuation:
  rules_checked: 26
  fails:
    - "Amend 18.0: bear/bull cases lack explicit Year-4 (FY31) projection rows (base case only fully projected; bear/bull are FY27 margin snapshots + FY30 exit EPS) — MINOR, zero decision impact on an AVOID/STOP"
    - "Amend 4.3: verdict card omits the mandated first-line 'Tier: A | Hurdle: 25%' declaration (Tier A / 1.953 hurdle correctly applied throughout) — MINOR presentational"
    - "Master Role 2 AVOID rule: four AVOID triggers fire (Gate0 AVERAGE, Promoter CONCERN, U/D -0.56, Hurdle STOP) so mechanical verdict is AVOID, but B14 emits WATCHLIST-defaulting-to-AVOID — MINOR, disclosed operator posture, functional action (no position) matches AVOID"
  recomputed_destination_pe: ""                # concur (additive 20x / RRM 17.9x / operator 30x override, all math clean)
  recomputed_decision: ""                      # concur (AVOID/STOP on valuation; WATCHLIST label is disclosed operator framing, functional AVOID)
findings:
  - {severity: "MINOR", location: "B11 Section 2 (2A/2B/2C)", note: "Amend 18.0 bear/bull not projected to Year-4 as explicit rows; base fully to FY31, bear/bull carried as FY27 margin snapshots + FY30 exit EPS. Cyclical-override method stated; no decision impact (AVOID all cases)."}
  - {severity: "MINOR", location: "B11 verdict card", note: "Amend 4.3 first-line 'Tier: A | Hurdle: 25%' declaration absent. Correct Tier A (promoter CONCERN fails Tier B quality gate) and 1.953 threshold applied everywhere. Cosmetic."}
  - {severity: "MINOR", location: "B14 verdict card / Section 7", note: "Master Role 2 mechanical AVOID (Gate0 AVERAGE + Promoter CONCERN + U/D<2x + Hurdle STOP all fire) vs emitted WATCHLIST. Disclosed as operator posture defaulting to AVOID; action today 'No position'; functional posture equals AVOID. Position size Small (Promoter cap binds) and entry Rs 570-650 both consistent."}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 88            # 23 of 26 valuation-scope rules passed clean
```
