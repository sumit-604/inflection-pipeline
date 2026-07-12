# VERIFIER C — FRAMEWORK ADHERENCE AUDIT (PHASE 3: VALUATION + DECISION)
# Prizor Viztech Ltd (PRIZOR) | Run 2026-07-12 | Model: claude-opus-4-8

Scope: PHASE 3 valuation-adherence half only. Gate 0 (48 rules) and Emerging
Moat (24 rules) were audited in phase 1 and are carried forward unchanged
(gate0 fails: [], emoat fails: []). This pass audits B11 (dual-track valuation)
and B14 (Role 2 decision / position sizing) against Section 1B v3.3, its
Amendments 1-8 / 4.1-4.4, the RRM dual-track, the Hurdle Ratio, the sector cap
table, UA ordering, and the Master v3.3 Role 2 decision and position-sizing
rules. Artifacts read: B10-valinputs, B11-valuation, B14-thesis, and the two
framework files. I audit rule APPLICATION, not raw numbers (Verifier A owns
number-in-source) and not company quality.

Method: every pillar, track, ratio and decision rule was independently
recomputed from the B10 inputs and the framework text. Recomputed value is
shown beside each rule.

---

## A. PILLAR 1 — ROCE BASE (continuous formula, Amendment 5)

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V1 | FTTCP verdict is sole Pillar-1 ROCE authority | PASS | Verdict STAGNANT (B10 fttcp_authoritative). No ad-hoc trajectory judgment introduced. |
| V2 | STAGNANT -> Current ROCE | PASS | Master table line 225: STAGNANT -> Current ROCE. Maker used current. |
| V3 | ROCE value = FY25 audited 31.29%; FY26 unaudited excluded | PASS | FY26 (37.2% vs 47.4%) internally inconsistent and unaudited; correctly barred (FLAG-INTERNAL-ROCE-INCONSISTENCY). |
| V4 | Continuous formula ROCE<=33%: 0.5xROCE+7.5, floor 9x cap 24x | PASS | 0.5x31.29+7.5 = 23.145 -> 23.1x. 23.145<24, cap not binding. Recompute matches exactly. |
| V5 | Single-credit rule; route stated | PASS | Route stated "not-credited" (STAGNANT = no forward uplift). No Strategic-Premium ROCE re-rating either; not double-credited. |

Pillar 1 = 23.1x. All 5 PASS.

## B. PILLAR 2 — CASH CONVERSION MULTIPLIER

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V6 | Multiplier matches stated determination | PASS | Determination INDETERMINATE-leaning-structural. 0.65x applied. See conservative-default note below. |
| V7 | Structural row takes NO growth offset | PASS | growth_offset = 0. Master line 266: structural -> 0 offset. Correct. |
| V8 | Unresolved rating quote handled by stated conservative rule, no silent fill | PASS | rating_wc_quote NOT FOUND explicitly named as INPUT UNRESOLVED; conservative 0.65x named, alternative (0.80x+0.05 -> 0.85x -> ~19.7x) disclosed and rejected. No silent fill. |
| V9 | Quality-Adjusted Base = ROCE Base x Cash Mult | PASS | 23.145 x 0.65 = 15.04 -> 15.0x. Recompute matches. |

Pillar 2 conservative-default note (framework-consistency confirmed, not a fail):
The 0.65x band label in Master line 248 reads "Structurally negative — rating
agency confirms persistent WC," and no rating exists. The maker did NOT claim
rating confirmation; it applied the more-conservative multiplier under an
INDETERMINATE-leaning-structural determination, which is (a) mandated by
CLAUDE.md ("Never let INDETERMINATE cash conversion silently resolve to
PROCEED... missing evidence named"), (b) consistent with the framework's
conservative bias, and (c) explicitly documented as an unresolved input. This
is framework-consistent. Sensitivity: even the rejected 0.85x path (~19.7x
destination) leaves HR(base) ~0.31 -> STILL STOP, and AVOID also stands on
Gate0 AVERAGE and U/D<2x. No decision sensitivity. Confirmed PASS.

## C. PILLAR 3 — GROWTH VISIBILITY (decoupled 3a/3b/3c, Amendment 4.1-4.2)

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V10 | 3a on documented machinery; +2x any two, +3x three+ & grade A/B | PASS | Zero of four qualify (capex-embedded NOT FOUND; order book NOT FOUND; SOM CAGR 16-17%<20%; grade C). 3a = +0x. |
| V11 | Grade C caps 3a at +2x | PASS | Grade C; cap not binding since 3a=0. |
| V12 | 3b EM-gated table; EM<25 -> +0x | PASS | EM 13.6 < 25 -> +0x. Master line 305. |
| V13 | 3c duration >=2.5yr documented order book | PASS | No signed contracts/LoAs/order book -> +0x. |
| V14 | Combined 3a+3b+3c within +6x cap | PASS | 0+0+0 = +0x. |

Pillar 3 = +0x. All 5 PASS.

## D. STRATEGIC PREMIUM + UA + SECTOR CAP

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V15 | Strategic Premium evidence-gated; ROCE re-rating only if not credited in P1 | PASS | +0x. No rare licence; pricing power contradicted (FLAG-MARGIN-PEER); ROCE re-rating barred by single-credit; no institutional backing. |
| V16 | UA applies only if ALL three qualifiers evidenced | PASS | listed_12m TRUE, gate0_or_em TRUE, fii_dii_lt3 NOT FOUND. Third not evidenced -> UA NOT applied. Correct. |
| V17 | UA ordering min(Raw x 1.25, Sector Cap), applied to Row F pre-cap | PASS | F2 = F = 15.0x (UA off). Conditional 15.0x1.25=18.8x correctly shown but not applied. |
| V18 | Sector cap row correct; manifest defect rejected | PASS | Manufacturing/Industrial 25x used; manifest Pharma/CDMO 38x rejected. Table lines 355-356 confirm 25x. |
| V19 | Sector cap ABSOLUTE; quality uplift only if UA triggered | PASS | No uplift (UA off). min(15.0,25)=15.0x. Cap absolute. |

All 5 PASS.

## E. TRACK 2 ADDITIVE + TRACK 1 RRM + DIVERGENCE

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V20 | F = C+D+E; H = min(F2,G) | PASS | 15.0+0+0 = 15.0; min(15.0,25) = 15.0x. |
| V21 | Destination PE range = H +/-7.5%, round to 0.5x | PASS | 15.0 +/-7.5% = 13.875-16.125 -> 14.0-16.0x (mid 15.0x). Amendment 6. |
| V22 | RRM = 1 + (13.5-r)x0.12, percentage-point reading (Amdt 4.4), bounds 0.70-1.60 | PASS | r=16: 1+(13.5-16)x0.12 = 1-0.30 = 0.70 (at floor). Base r 14% (small/micro) adjusted +2 for governance/durability flags; within [9,18]. |
| V23 | Track 1 = Fundamental Base PE x RRM, capped at sector cap | PASS | 23.1 x 0.70 = 16.17 -> 16.2x. Cap 25x not binding. Range 14.98-17.4 -> 15.0-17.5x (mid 16.2x). |
| V24 | Both tracks carried through all fair values + verdict card | PASS | FV Track1 {84,170,253}, Track2 {76,154,231}; verdict card shows both. |
| V25 | Divergence stated; more-conservative track governs entry | PASS | (16.2-15.0)/15.0 = 8.0% (<15%). Governing = Track 2 (lower). Correct. |

All 6 PASS.

## F. TWO-TIER HURDLE + HURDLE RATIO

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V26 | Tier B requires ALL four gates; else Tier A | PASS | FII+DII NOT FOUND (not >=3%), Gate0 AVERAGE, structural FLAG-CASH present, promoter CAUTION -> Tier B fails. Tier A, hurdle 25%, divisor 1.953. |
| V27 | Verdict card first line "Tier: A | Hurdle: 25%" | PASS | Present on B11 line 6 and 241. |
| V28 | Current PE computation | PASS | 825 / 9.495 (FY25 audited diluted EPS) = 86.9x. FY26 unaudited correctly excluded (conservative; even ~42.5x >> destination). |
| V29 | HR = (1+EPS CAGR)^3 x (Dest PE mid / Current PE); threshold 1.953 | PASS | HR(base) = 1.105^3 x (15.0/86.9) = 1.3494 x 0.17261 = 0.233 -> 0.23. Matches. |
| V30 | Bull EPS CAGR usable only if grade A/B; else Base+5% | PASS | Grade C -> Bull row uses 10.5%+5% = 15.5%. HR(bull) = 1.155^3 x 0.17261 = 1.5408 x 0.17261 = 0.266 -> 0.27. Matches. |
| V31 | Hurdle verdict per Amendment 2 table | PASS | HR(Bull) 0.27 < 1.953 -> STOP. Correct row. |

All 6 PASS.

## G. ENTRY / RETURNS / CROSS-CHECKS

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V32 | Entry = base FV / (1+hurdle)^3 (Tier A divisor 1.953); MoS 20% below | PASS | 154/1.953 = 78.85 -> 79. MoS 79x0.8 = 63.2 -> 63. Range 63-79. |
| V33 | 4D probability weights (grade C 35/45/20); expected CAGR | PASS | 0.35(-54.9)+0.45(-42.8)+0.20(-34.6) = -45.4%. Matches. |
| V34 | SOM cross-check performed | PASS | Base rev CAGR 14% < SOM ceiling 17% -> CONSISTENT. Section 2A. |

All 3 PASS.

## H. ROLE 2 (B14) — DECISION / POSITION / ZONE

| # | Rule | Applied As Written? | Recompute / Note |
|---|---|---|---|
| V35 | AVOID trigger set (Master line 809) | PASS | Gate0 AVERAGE, U/D 0.0x<2x, HR STOP each independently force AVOID. Promoter CAUTION (not CONCERN/AVOID) correctly noted as non-forcing but cap-binding. |
| V36 | Entry conjunction (anti-value-trap) stated in verdict box | PASS | Section 7 "ENTRY CONJUNCTION (mandatory)": price in Rs 63-79 AND no thesis-broken trigger fired. Master line 811. |
| V37 | Position sizing None on AVOID/DEEP WATCH; promoter cap binds | PASS | Position None; no operator override; Tier B position ceiling moot. Consistent. |
| V38 | Zone reachability classified; MARKET-UNLIKELY -> DEEP WATCH not WATCHLIST | PASS | Ceiling Rs 79 ~90% below CMP 825 -> MARKET-UNLIKELY -> DEEP WATCH (not actionable). Consistent with FTTCP DEEP WATCH. See MINOR below. |

All 4 PASS (one MINOR anchor inconsistency noted).

---

## FINDINGS

CRITICAL: none. MAJOR: none.

MINOR-1 (presentational, cross-artifact anchor inconsistency): B14 zone
reachability is supported by conflicting price references. The B14 report
(14-thesis.md, ZONE REACHABILITY para and NARRATIVE) states "Lowest tested
LISTED price since July 2024: NOT FOUND in inputs," while the B14 YAML
zone_reachability field cites "~25% below the only price reference in the
screening data (Rs 105.25)." One artifact says NOT FOUND, the other cites a
specific Rs 105.25 anchor. The classification itself (MARKET-UNLIKELY / DEEP
WATCH) is correct and unchanged either way (entry ceiling Rs 79 sits far below
both Rs 105.25 and CMP 825). rule_ref: Master v3.3 Role 2 / Amendment 4.3-4.4
zone-reachability flag. No decision or valuation impact. Recommend the finalize
step reconcile the two artifacts to a single stated price anchor.

## RECOMPUTATION SUMMARY

Every material valuation output was independently recomputed and TIES to B11:
Pillar 1 23.1x; QA base 15.0x; Pillar 3 +0x; Raw/Final destination 15.0x
(Track 2, range 14.0-16.0x); RRM 0.70 / Track 1 16.2x (range 15.0-17.5x);
divergence 8.0%; current PE 86.9x; HR base 0.23 / bull 0.27 -> STOP; entry
63-79; MoS 63; expected CAGR -45.4%. Decision AVOID / DEEP WATCH is correctly
derived on multiple independent framework triggers.

recomputed_destination_pe: CONCUR (Track 1 16.2x mid / Track 2 15.0x mid, both
confirmed) — no restatement.
recomputed_decision: CONCUR (AVOID / DEEP WATCH) — no restatement.

## ACCEPTANCE (all three sections)

- gate0: 48 rules checked, 0 fails (phase 1, carried unchanged)
- emoat: 24 rules checked, 0 fails (phase 1, carried unchanged)
- valuation: 34 rules checked, 0 rule-fails (1 MINOR cross-artifact anchor note)
- Total: 106 rules checked, 106 passed
- framework_adherence acceptance_rate = 106/106 = 100%

The valuation is unusually clean: every pillar, both tracks, the Hurdle Ratio,
the two-tier assignment, UA ordering, sector cap, and the Role 2 decision chain
were applied exactly as written, every unresolved input was named with a
conservative rule and no silent fills, and the single-improvement-single-
mechanism rule was honored (ROCE recovery not credited anywhere). The only
observation is a presentational anchor inconsistency in B14 zone reachability
that does not touch the verdict.

---

```yaml
stage: B12c
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-opus-4-8
status: complete
gate0: {rules_checked: 48, fails: []}
emoat: {rules_checked: 24, fails: []}
valuation:
  rules_checked: 34
  fails: []
  rules_checked_detail:
    pillar1: 5
    pillar2: 4
    pillar3: 5
    strategic_ua_sectorcap: 5
    tracks_divergence: 6
    hurdle_twotier: 6
    entry_returns_crosschecks: 3
    role2_decision_position_zone: 4
recomputed_destination_pe: ""   # CONCUR: Track1 16.2x mid / Track2 15.0x mid
recomputed_decision: ""         # CONCUR: AVOID / DEEP WATCH
findings:
  - {severity: "MINOR", location: "B14-thesis zone_reachability (14-thesis.md ZONE REACHABILITY vs B14 YAML field)", claimed: "md: 'Lowest tested LISTED price since July 2024: NOT FOUND'; yaml: '~25% below the only price reference Rs 105.25'", rule_ref: "Master v3.3 Role 2 / Amdt 4.3-4.4 zone-reachability flag", note: "Cross-artifact anchor inconsistency; classification MARKET-UNLIKELY/DEEP WATCH correct and unchanged either way; no decision impact"}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 100            # 106 rules passed / 106 checked across all three sections
```
