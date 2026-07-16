# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 3: VALUATION + ROLE 2)
# HCP Plastene Bulkpack Ltd (526717) | Run 2026-07-15 | Model: claude-opus-4-8
# Scope: deferred VALUATION-ADHERENCE audit of B10 (assembly), B11 (valuation),
# B14 (thesis), extended to Role 2 decision rules and position sizing.
# Gate 0 (B01) and Emerging Moat (B07) checks were completed in phase 1 and are
# NOT re-audited here. Fresh context; artifacts and framework docs only.

---

## METHOD

Every Section 1B v3.3 / Master v3.3 / FTTCP v1.2 rule in scope was re-derived from
the stated inputs and the framework text, then compared to what B10/B11/B14
actually did. Numbers were recomputed only where needed to test rule application
(number-sourcing itself is Verifier A's domain). Each rule is marked PASS / FAIL
with the recomputed value beside any FAIL.

---

## PART 1 — PILLAR 1 (ROCE BASE, CONTINUOUS FORMULA, AMENDMENT 9)

| # | Rule (as written) | Applied value | Recompute | Verdict |
|---|---|---|---|---|
| P1.1 | Continuous formula 0.5 × ROCE + 7.5, floor 9x cap 24x (Amdt 5) | 21.8x | 0.5×28.62+7.5 = 21.81 → 21.8x; 9 < 21.8 < 24, caps not binding | PASS |
| P1.2 | ROCE selection per FTTCP verdict table: FIRING → CURRENT ROCE (FTTCP Pillar 1 Integration table) | current 28.62% | FTTCP forward verdict FIRING (B10 deliberation_inputs) → current ROCE is the only table mapping; used verbatim | PASS |
| P1.3 | Amendment 9 route selection — Route A test: (CWIP+idle capital+capex advances) > 20% of capital employed | Route A FAILS | CWIP Rs 0.06 cr vs cap employed ~168.9 cr = 0.04% << 20% | PASS |
| P1.4 | Amendment 9 Route B test: FTTCP verdict TEMPORARILY DEPRESSED or RECOVERING with 📄 pre-depression history | Route B FAILS | Verdict is FIRING, not TEMPORARILY DEPRESSED/RECOVERING; Route B unavailable | PASS |
| P1.5 | Neither route holds → statutory ROCE feeds Pillar 1; worksheet declares route | "route: NONE" stated (11.md l.46) | Correct — no normalization; statutory 28.62% direct | PASS |

Pillar 1 clean. Note (not a fail): the SHARED-CATALYST concern is that RP payables
SHRINK capital employed and thereby OVERSTATE the 28.62% ROCE. Amendment 9 provides
routes only for the opposite distortion (denominator bloat / numerator trough that
UNDER-state ROCE). The framework therefore offers no downward-normalization lever
here, and B11 correctly handled the overstatement as a bear-case stress (RP add-back
→ ~18% ROCE → Pillar 1 ~16.5x → destination ~11x), not as a base-case Pillar 1
adjustment. This is the framework-correct treatment and is transparently flagged.

---

## PART 2 — PILLAR 2 (CASH CONVERSION MULTIPLIER)

| # | Rule | Applied | Recompute / test | Verdict |
|---|---|---|---|---|
| P2.1 | Base multiplier from cash quality band under INDETERMINATE determination | 0.80x | See finding V-1 below | PASS (with MINOR) |
| P2.2 | Growth offset applies ONLY to confirmed growth-induced drag; barred under INDETERMINATE/structural | offset BARRED | INDETERMINATE ≠ confirmed growth-induced → offset correctly barred (Master l.259-266) | PASS |
| P2.3 | No offset on structural drag | 0 | Consistent | PASS |
| P2.4 | INDETERMINATE must not resolve to a clean pass; missing evidence named (CLAUDE.md) | capped, FLAG-CASH carried, FY27 standalone cash named | Verdict capped at AVOID; missing evidence (structural-vs-growth; FY27 standalone CFO) named | PASS |
| P2.5 | Quality-Adjusted Base = ROCE base × multiplier | 17.4x | 21.8 × 0.80 = 17.44 → 17.4x | PASS |

**Finding V-1 (MINOR).** The band table (Master l.242-248) reads: "CFO/PAT below 30%
or CFO negative (growth-phase drag) → 0.80x" and "Structurally negative — rating
agency confirms persistent WC → 0.65x." Infomerics (RATING.txt p.5) confirms
persistent working-capital intensity, and cumulative 6-yr CFO/PAT is -0.888x (5 of 6
years CFO-negative), which on a strict structural read supports 0.65x. Conversely,
the naive LATEST-year read (FY26 CFO/PAT 0.70x, FCF positive) would map to the 1.00-
1.15x bands. B11 chose 0.80x — the conservative midpoint — because the structural-vs-
growth test is INDETERMINATE and CLAUDE.md bars a clean pass. This is defensible and
was faithfully carried from the authoritative FTTCP deliberation (fttcp-deliberation
p.2 l.30), which B10/B11 are required to treat as anchor-only. The bear leg does use
the 0.65x structural read. Net: not a misapplication by B10/B11 (they honoured the
authoritative input), but the 0.80-vs-0.65 reconciliation in the base could be
tighter. Verdict-invariant (AVOID stands regardless). MINOR.

---

## PART 3 — PILLAR 3, STRATEGIC PREMIUM, SINGLE-CREDIT, UA, SECTOR CAP

| # | Rule | Applied | Test | Verdict |
|---|---|---|---|---|
| P3.1 | 3a Growth Visibility: +2x needs any TWO 📄 qualifiers; grade C caps 3a at +2x | +0x | Qualifiers: capex-growth ≥15% NO; order book ≥1.0x NOT FOUND; SOM CAGR ≥20% w/ capacity cross-check YES; delivery grade A/B NO. Only ONE holds → +0x | PASS |
| P3.2 | 3b Moat Formation: EM below 25 → +0x | +0x | EM 12 < 25 (Master Pillar 3 table) | PASS |
| P3.3 | 3c Duration: +1x only at ≥2.5-yr 📄 documented visibility | +0x | No order-book/annuity tenor disclosed | PASS |
| P3.4 | Combined 3a+3b+3c ≤ +6x cap | +0x total | 0 ≤ 6 | PASS |
| SP.1 | Strategic Premium requires genuine scarcity; strong-but-replicable moats pay 0 | +0x base | No regulatory monopoly; port/certification moats STRONG not scarcity-tier | PASS |
| SP.2 | FII inflow is passive institutional flow, not "turnaround with institutional backing (GIC/Tata)" | not credited | Correct — 0.07%→4.50% passive FII ≠ strategic anchor | PASS |
| SC.1 | Single-credit: ROCE recovery via Pillar 1 OR Strategic, never both; route stated | Pillar 1; Strategic ROCE route BARRED (l.48) | Under FIRING the high current ROCE already sits in Pillar 1; a strategic ROCE re-rating would double-credit → correctly barred; route declared | PASS |
| UA.1 | UA needs ALL THREE qualifiers, each evidenced | not applied | Listed ≥12m MET; Gate0≥60 OR EM≥25 FAIL (27/12); FII+DII<3% FAIL (9.29%) → NO | PASS |
| UA.2 | Ordering: min(Raw × 1.25, cap), UA on Raw BEFORE cap (Amdt 3) | F2 = F = 17.4x | UA not applied → F2 = F; H = min(17.4, 22) = 17.4x | PASS |
| SCAP.1 | Sector cap ABSOLUTE; Packaging 22x (FTTCP override of manifest Pharma/CDMO 38x) | 22x absolute | Business is FIBC/woven packaging → Packaging 22x is the correct row; override applied | PASS |
| SCAP.2 | No quality uplift on cap unless UA triggered + durability Moderate-Strong | no uplift | UA not triggered → cap stays 22x | PASS |
| SCAP.3 | Cap binds only if destination > cap | not binding | 17.4 < 22 | PASS |
| SCAP.4 | No exit PE from outside Section 1B (NEVER rule; no round numbers) | compliant | Bull 20.5x = 21.8×0.90 + 0.9 strat, < 22 cap; EV/EBITDA via 0.6-0.7x-of-PE rule (Master l.518), not a round-number default | PASS |

Pillar 3 / Strategic / single-credit / UA / sector cap all clean.

---

## PART 4 — RRM TRACK 1, DUAL-TRACK, DIVERGENCE

| # | Rule | Applied | Recompute | Verdict |
|---|---|---|---|---|
| RRM.1 | RRM = 1 + (13.5 − r) × 0.12, percentage-point reading (Amdt 4.4), bounded 0.70-1.60 | 0.70 | 1 + (13.5−16.0)×0.12 = 1 − 0.30 = 0.70; at floor | PASS |
| RRM.2 | Base r small/micro 14%, adjusted for durability/governance/leverage, bound [9,18] | r = 16.0% | Raised for MODERATE durability + CONCERN governance + binding leverage; 16.0 ∈ [9,18] | PASS |
| RRM.3 | Track 1 destination = Fundamental Base × RRM, capped at sector cap | 12.2x | 17.4 × 0.70 = 12.18 → 12.2x; 22x cap not binding | PASS |
| RRM.4 | BOTH tracks present and carried through every fair value + verdict card | both carried | Track 1 & Track 2 in destination PE, all scenario FVs, entry, verdict card 4H | PASS |
| RRM.5 | Divergence >15% → conservative track sets entry zone | Track 1 governs | (17.4−12.2)/17.4 = 29.9% ≈ 30% > 15% → Track 1 (conservative) governs entry | PASS |

---

## PART 5 — HURDLE RATIO + TWO-TIER

| # | Rule | Applied | Recompute | Verdict |
|---|---|---|---|---|
| HR.1 | Tier B needs ALL: FII+DII≥3% AND Gate0 GOOD+/EM≥25 AND Promoter TRUSTWORTHY+ AND no structural FLAG-CASH (Amdt 4.3) | Tier A | Gate0 27/EM 12 FAIL; Promoter CONCERN FAIL; FLAG-CASH present FAIL → Tier B barred → Tier A | PASS |
| HR.2 | Tier A hurdle 25%, threshold 1.953 | 25% / 1.953 | Correct divisor/threshold | PASS |
| HR.3 | HR = (1+EPS CAGR)³ × (Destination PE mid ÷ Current PE) | see cells | Current PE 194/21.60 = 8.98x; base EPS CAGR 18%, 1.18³ = 1.6430 | PASS |
| HR.4 | HR Track 2 | 3.18 | 1.6430 × (17.4/8.98) = 1.6430 × 1.938 = 3.183 → 3.18 | PASS |
| HR.5 | HR Track 1 (governing) | 2.23 | 1.6430 × (12.2/8.98) = 1.6430 × 1.359 = 2.232 → 2.23 | PASS |
| HR.6 | PASS/CONDITIONAL/STOP mapping: HR(Base) ≥ 1.953 → PASS | PASS | 3.18 and 2.23 both ≥ 1.953 → PASS on base, both tracks | PASS |
| HR.7 | Bull EPS CAGR usable only if grade Good/Excellent; else Base+5% max (Amdt 2 note) | 23% (Base+5) | Grade C (Mixed) → bull capped at 18+5 = 23%; applied | PASS |

**Sensitivity note (see finding V-2).** Under the alternate results-line EBIT basis
(39.98 → ROCE ~23.7% → Pillar 1 ~19.3x → base ~15.5x → Track 1 ~10.8x), HR Track 1
recomputes to 1.6430 × (10.8/8.98) = 1.6430 × 1.203 = 1.976 — still above 1.953 but
by a hair. B11 disclosed this. Decision unaffected (AVOID). Recorded so the operator
sees the near-miss.

---

## PART 6 — ENTRY, RETURNS, WEIGHTS, SOM, UNRESOLVED INPUTS

| # | Rule | Applied | Recompute | Verdict |
|---|---|---|---|---|
| E.1 | Entry = base FV ÷ (1+hurdle)³, Tier A divisor 1.953 (Amdt 4.3) | Rs 222 | 433 / 1.953 = 221.7 → 222 (governing Track 1 base) | PASS |
| E.2 | MoS = 20% below entry | Rs 177 | 222 × 0.80 = 177.6 → 177 | PASS |
| E.3 | Upside/Downside ratio, ≥2x threshold check | 3.27x | 123.2% / 37.6% = 3.27; ≥2 | PASS |
| E.4 | 4D probability weights match grade (Master l.627-631) | 35/45/20 | Grade C = Mixed → Bear 35 / Base 45 / Bull 20 | PASS |
| E.5 | Prob-weighted expected CAGR arithmetic | +17.4% | 0.35(−14.6)+0.45(30.6)+0.20(43.9) = −5.11+13.77+8.78 = 17.44 → +17.4% | PASS |
| E.6 | SOM cross-check performed (assumption vs SOM-implied CAGR, capacity gate) | consistent | Base rev 18% < SOM-implied 30.7% (3-yr); bull 26% < capacity gate; performed | PASS |
| E.7 | Every unresolved input handled by stated conservative rule; NO silent fills (NEVER rule) | 3 gaps, NOT FOUND | RP add-back, peer multiples, FY26 utilisation each carried as NOT FOUND with conservative assumption, not invented | PASS |
| E.8 | Verdict card first line states "Tier: [A/B] | Hurdle: [25%/20%]" (Amdt 4.3) | "Tier: A | Hurdle: 25%" (11.md l.278) | Present | PASS |

**Finding V-2 (MINOR).** ROCE-basis internal inconsistency carried from B10 into B11.
B10 built EBITDA from results-line EBIT 39.98 (RESULTS_1.txt p.7), yet the ROCE fed
to Pillar 1 (28.62%) is derived from EBIT ex-other-income 48.33 — an 8.35 cr basis
gap. B11 used the FTTCP deliberation's authoritative 28.62% (anchor-only, correctly
not re-litigated) and disclosed the ~1.9-PE-point sensitivity. Which EBIT basis is
correct is a NUMBERS question owned by Verifier A, not a framework misapplication:
Pillar 1 correctly consumed the authoritative ROCE. Flagged because the sensitivity
narrows the Track-1 Hurdle margin (see HR sensitivity) though it does not flip the
AVOID decision. MINOR.

---

## PART 7 — ROLE 2 DECISION RULES + POSITION SIZING (B14)

| # | Rule | Applied | Test | Verdict |
|---|---|---|---|---|
| R2.1 | Promoter CONCERN → default AVOID regardless of everything else (Master l.916) | AVOID | Promoter verdict CONCERN → AVOID applied and stated verbatim (14.md l.133) | PASS |
| R2.2 | AVOID trigger mapping: Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR Hurdle STOP (Master l.809) | AVOID on first two | Gate0 AVOID and Promoter CONCERN each independently trigger; correctly identified | PASS |
| R2.3 | BUY NOW needs CMP≤MoS AND Gate0≥GOOD AND Promoter≥TRUSTWORTHY AND Hurdle PASS | not BUY NOW | Fails Gate0 (AVOID) and Promoter (CONCERN); correctly excluded | PASS |
| R2.4 | Entry conjunction (anti-value-trap): BUY/BUY-ON-DIPS only if price in zone AND no thesis-broken trigger fired (Master l.811) | zone WITHDRAWN | CMP 194 in Rs 177-222 zone BUT leverage/governance/cash caps live → zone withdrawn, value trap called | PASS |
| R2.5 | Hardest-verdict-wins across contradicting outputs (Master l.914) | AVOID | FTTCP DEEP WATCH-leaning-BUY-ON-DIPS is a gated conditional; Role 1 AVOID, Gate0 AVOID, Promoter CONCERN → hardest = AVOID; resolved correctly | PASS |
| R2.6 | Tier B barred by Promoter CONCERN (Amdt 4.3 gate: Promoter TRUSTWORTHY+) | Tier B barred | Stated: Promoter CONCERN bars Tier B and caps hypothetical size at Small (14.md l.138) | PASS |
| R2.7 | Position size: Promoter Verdict caps always bind; None on AVOID (Master l.815-818) | None | AVOID → position size None; hypothetical capped Small; consistent | PASS |
| R2.8 | Thesis-broken trigger specific and measurable | measurable | FY27 standalone CFO negative 2nd yr AND consolidated reverts negative AND gearing >3x | PASS |

**Finding V-3 (MINOR, cosmetic).** The B14 one-line thesis frames the block as "two
hard caps bind at once ... with cash conversion INDETERMINATE on top," whereas B11
and the risk matrix treat three overlapping caps (Gate0 leverage, Promoter CONCERN,
INDETERMINATE cash). The substance is identical (all three surfaced and drive AVOID);
only the headline count differs. Presentational, decision-invariant. MINOR.

---

## RECOMPUTATION SUMMARY

- Recomputed destination PE (Track 1 governing): 12.2x — CONCUR with B11.
- Recomputed destination PE (Track 2 additive): 17.4x — CONCUR with B11.
- Recomputed Hurdle: Track 2 3.18 / Track 1 2.23, PASS — CONCUR.
- Recomputed entry Rs 177-222, MoS Rs 177 — CONCUR.
- Recomputed prob-weighted CAGR +17.4% — CONCUR.
- Recomputed decision: AVOID (Promoter CONCERN + binding Gate0 leverage, hardest-
  verdict-wins, entry-conjunction zone withdrawn) — CONCUR.

No CRITICAL or MAJOR framework misapplication found. Every scored valuation and Role
2 rule was applied as written; the three MINOR findings are transparency/robustness
observations that do not overturn any rule or the AVOID decision. The destination PE,
Hurdle verdict, and decision are all unchanged on recomputation.

## SEVERITY TALLY

- CRITICAL: 0
- MAJOR: 0
- MINOR: 3 (V-1 Pillar 2 band reconciliation; V-2 ROCE-basis sensitivity carried
  from B10; V-3 cosmetic "two caps" wording in B14 one-line)

## FRAMEWORK ADHERENCE

Rules checked: 41 (valuation 33 + Role 2 8). Rules applied correctly: 41/41. Rules
fully clean (no attached MINOR): 38/41. Valuation framework_adherence (% of
valuation + thesis rules checked clean) = 38/41 = 92.7% → 93%.

```yaml
stage: B12c-valuation
company: "526717"
run_date: "2026-07-15"
model: claude-opus-4-8
status: complete
scope: "phase3 valuation-adherence + role2 decision rules & position sizing (B10, B11, B14); Gate0 + EmergingMoat done in phase1, not re-audited"
valuation:
  rules_checked: 33
  rules_clean: 30
  pillar1_formula: "PASS (0.5x28.62+7.5=21.8x; floor/cap not binding)"
  pillar1_roce_selection: "PASS (FTTCP FIRING -> current ROCE 28.62%)"
  amendment9_route: "PASS (route NONE; Route A CWIP 0.04%<20%, Route B verdict not TEMPORARILY DEPRESSED/RECOVERING)"
  pillar2_multiplier: "PASS with MINOR (0.80x under INDETERMINATE; 0.65x structural read also defensible; carried from authoritative FTTCP deliberation; bear uses 0.65x)"
  pillar2_growth_offset: "PASS (barred; INDETERMINATE is not confirmed growth-induced)"
  pillar3_total: "PASS (+0x: 3a one qualifier only, 3b EM12<25, 3c no >=2.5yr visibility)"
  strategic_premium: "PASS (+0x; no scarcity; FII passive not strategic anchor)"
  single_credit: "PASS (ROCE via Pillar 1; Strategic ROCE route BARRED; route stated)"
  ua_ordering_and_qualifiers: "PASS (all-three fail -> not applied; F2=F; H=min(17.4,22)=17.4x)"
  sector_cap: "PASS (Packaging 22x absolute, FTTCP override applied, not binding, no exit PE outside 1B)"
  rrm_track1: "PASS (r=16.0%; RRM=1+(13.5-16.0)x0.12=0.70 floor; 17.4x0.70=12.2x)"
  dual_track_and_divergence: "PASS (both tracks carried; divergence 30%>15% -> conservative Track 1 governs entry)"
  hurdle_ratio: "PASS (Tier A 1.953; current PE 8.98x; T2 3.18 / T1 2.23; base>=1.953 -> PASS; bull EPS CAGR capped Base+5%=23% for grade C)"
  entry_and_returns: "PASS (entry 433/1.953=222; MoS 177; U/D 3.27x>=2; grade-C weights 35/45/20; prob-weighted +17.4%)"
  som_crosscheck: "PASS (base 18% < SOM-implied 30.7%; capacity-gated)"
  unresolved_inputs: "PASS (RP add-back, peer multiples, FY26 utilisation carried NOT FOUND, no silent fills)"
  fails: []
role2:
  rules_checked: 8
  rules_clean: 8
  promoter_concern_default_avoid: "PASS (CONCERN -> AVOID regardless, Master l.916)"
  avoid_trigger_mapping: "PASS (Gate0 AVOID + Promoter CONCERN each trigger independently)"
  buy_now_gate: "PASS (correctly excluded; fails Gate0 and Promoter conditions)"
  entry_conjunction: "PASS (CMP in zone but caps live -> zone WITHDRAWN, value trap called)"
  hardest_verdict_wins: "PASS (FTTCP conditional DEEP WATCH overridden by AVOID caps)"
  tier_b_barred: "PASS (Promoter CONCERN bars Tier B; Tier A anyway)"
  position_sizing: "PASS (None on AVOID; hypothetical capped Small; promoter cap binds)"
  fails: []
findings:
  - severity: "MINOR"
    location: "B11 11.md l.54 / Pillar 2; B10 cash_conversion_and_wc"
    description: "Cash multiplier 0.80x under INDETERMINATE. Band table also supports 0.65x (Infomerics confirms persistent WC; cumulative 6yr CFO/PAT -0.888x, 5/6 yrs negative), while naive latest-year 0.70x would map 1.00-1.15x. 0.80x is the conservative midpoint faithfully carried from the authoritative FTTCP deliberation; base-case 0.80-vs-0.65 reconciliation could be tighter. Bear correctly uses 0.65x. Verdict-invariant."
  - severity: "MINOR"
    location: "B11 11.md l.117-119 / EBIT-basis reconciliation; carried from B10 ebitda build"
    description: "ROCE-basis inconsistency: B10 EBITDA uses results-line EBIT 39.98 but Pillar 1 ROCE 28.62% derives from EBIT ex-other-income 48.33 (8.35cr gap). B11 correctly used the authoritative FTTCP ROCE (anchor-only) and disclosed the ~1.9-PE-point sensitivity; under the alternate basis Track-1 Hurdle recomputes to ~1.98 (still >1.953, narrow). Which EBIT basis is right is Verifier A's domain; not a framework misapplication. Decision unchanged."
  - severity: "MINOR"
    location: "B14 14.md l.17 / Section 1 one-line thesis"
    description: "One-line frames 'two hard caps' with cash INDETERMINATE 'on top', while B11 and the risk matrix carry three overlapping caps (Gate0 leverage, Promoter CONCERN, INDETERMINATE cash). Cosmetic count mismatch; all three are surfaced and drive AVOID. Decision-invariant."
recomputed_destination_pe: ""   # concur: Track 1 12.2x / Track 2 17.4x
recomputed_decision: ""         # concur: AVOID
critical_count: 0
major_count: 0
minor_count: 3
valuation_framework_adherence: 93   # rules clean 38 / rules checked 41 = 92.7% -> 93%
acceptance_rate: 93
```
