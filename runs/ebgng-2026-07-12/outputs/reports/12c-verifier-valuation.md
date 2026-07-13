# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 3, VALUATION HALF)

**Company:** GNG Electronics Ltd (EBGNG) | **Run date:** 2026-07-12 | **Model:** claude-opus-4-8
**Scope:** Role 1 valuation (B11) audited against Section 1B v3.3 as written, EXTENDED to Role 2 (B14) decision rules + position sizing vs Master v3.3 Role 2. Gate 0 and Emerging Moat adherence were audited and recorded in Phase 1; NOT redone here.
**Frameworks read:** Master_Project_Prompt_v3.3.md (Role 1 Section 1B, Role 2), Section_1B_v3.3_Amendments.md (Amendments 1-8, 4.1-4.5), FTTCP_v1.2.
**Discipline:** I audit rule APPLICATION, not raw numbers (Verifier A owns numbers) and not company quality. Operator overrides are audited for CORRECT APPLICATION only, not for wisdom.

---

## OPERATOR OVERRIDES — CORRECT-APPLICATION CHECK (the four flagged in the task)

| Override | Instruction | Where B11 applies it | Correct? |
|---|---|---|---|
| Destination/exit PE 20x, FORWARD basis (20x × FY30 EPS at FY29 exit) | governs fair value, entry, Hurdle | B11 Section 1B "GOVERNING DESTINATION PE", Section 3 table, 4H card | YES — applied on forward FY30 EPS throughout; exit target = 20 × FY30 EPS per scenario |
| Pillar 1 ROCE anchor = operational ex-cash 28.3% | supersedes reported 24.06% | Pillar 1, roce_used 28.3 | YES — 28.3% fed to continuous formula; reported 24.06% not used |
| Cash conversion INDETERMINATE, growth offset BARRED | multiplier gets no growth offset | Pillar 2, growth_offset 0, 0.65x | YES — offset explicitly barred; no offset applied |
| Sector cap Recycling/Manufacturing 25x | absolute ceiling | sector_cap_used 25 | YES — 20x sits below 25x, admissible |

**20x-below-cap test:** 20x governing < 25x sector cap → admissible. Correct. No override misapplication that changes destination PE >1x, flips the Hurdle, or flips the decision. No CRITICAL, no MAJOR on override application.

---

## VALUATION RULE-BY-RULE (Section 1B v3.3 + Master Role 1)

| # | Rule (as written) | Applied in B11 | Recompute | PASS/FAIL |
|---|---|---|---|---|
| 1 | Continuous Pillar 1 formula (Amendment 5: 0.5×ROCE+7.5, floor 9 / cap 24), NOT old bands | 0.5×28.3+7.5 = 21.65x | 21.65 ✓, within [9,24] | PASS |
| 2 | FTTCP ROCE forward verdict is sole Pillar 1 authority | RECOVERING (40-60%,12m) drives Pillar 1; ROCE 28.3% operational | matches FTTCP/deliberation | PASS |
| 3 | Amendment 4.5 (Normalized-ROCE) applies ONLY if backward TEMPORARILY DEPRESSED AND forward RECOVERING AND 📄-gated (pre-depression median + named unwind catalyst); else standard blend | Declined: operator fixed anchor at 28.3%; FY[Y+2] NOT FOUND; no clean pre-depression-median + unwind-catalyst pair; cash INDETERMINATE | Immaterial to destination PE either way (mechanical already < governing 20x); declining is defensible and 📄-gate not met | PASS |
| 4 | Single-credit rule (Amendment 4): recovery via Pillar 1 OR Strategic Premium, never both; route stated | "credited via Pillar 1 midpoint; Strategic ROCE re-rating BARRED" | route stated, strategic +0 | PASS |
| 5 | Pillar 2 multiplier matches determination; INDETERMINATE never clean-passes; NO offset on structural/INDETERMINATE | 0.65x, INDETERMINATE, growth_offset 0 | conservative bottom of 0.65-0.80 band; offset barred | PASS |
| 6 | Pillar 3a growth visibility (📄, +2x if any two qualify) | SOM CAGR 35.7%≥20% (capacity cross-check pass) + grade B → two → +2x | +2x ✓ | PASS |
| 7 | Pillar 3b moat formation (EM-gated, EM<25 → +0x) | EM 23 <25 → +0x | +0x ✓ | PASS |
| 8 | Pillar 3c duration (📄 order book ≥2.5yr) and combined +6x cap | no documented tenor → +0x; total +2x ≤ 6x | +0x ✓ | PASS |
| 9 | Strategic Premium single-credit (barred if credited in Pillar 1) | +0x, barred | +0x ✓ | PASS |
| 10 | UA in Amendment 3 order min(Raw×1.25, Cap); all three qualifiers evidenced | listed 347d<12m FAIL; Gate0 48<60 AND EM 23<25 FAIL; FII+DII 3.94%≥3% FAIL → all_met false → UA off | all three qualifiers evidenced and each fails; UA not applied; F2=16.07 | PASS |
| 11 | Sector cap absolute | min(16.07,25)=16.07 mechanical; governing 20x<25x | ✓ | PASS |
| 12 | BOTH tracks present and carried through fair value + verdict card | RRM (16.5x) + additive (16.1x) both shown; operator 20x supersedes both and carries to fair values / card | ✓ | PASS |
| 13 | RRM computed correctly (percentage-point reading, Amendment 4.4) | 1+(13.5−15.5)×0.12 = 0.76; 21.65×0.76=16.45 | 0.76 ✓, 16.5x ✓ | PASS |
| 14 | Conservative track governs entry on >15% divergence | divergence 2.4% <15% → no split; operator 20x governs | ✓ (rule not triggered) | PASS |
| 15 | Operator 20x forward applied on forward FY30 EPS at FY29 exit | exit target = 20×FY30 EPS per scenario | ✓ | PASS |
| 16 | Hurdle Ratio = (EPS_exit_forward/EPS_now)×(DestPE/CurrPE), threshold 1.953 | base 0.90, bull 1.20 | 573/634=0.904≈0.90 ✓; 758/634=1.196≈1.20 ✓ | PASS |
| 17 | Credibility-grade gate on Bull row (bull EPS CAGR only if grade A/B) | grade B → bull permitted | ✓ | PASS |
| 18 | Hurdle verdict: HR(Bull)<1.953 → STOP | 1.20<1.953 → STOP | ✓ | PASS |
| 19 | Two-tier hurdle (4.3): Tier B needs ALL gates; else Tier A (1.953) | fails Tier B (Gate0 AVERAGE, promoter CAUTION, structural FLAG-CASH) → Tier A | ✓ | PASS |
| 20 | 4D weights match grade (B/Good = 25/50/25) | 25/50/25; expected −5.6% | 0.25(−21.9)+0.5(−3.3)+0.25(6.1)=−5.6 ✓ | PASS |
| 21 | Entry (÷1.953), 30% entry (÷2.197), MoS (−20%) | 293 / 261 / 235 | 573/1.953=293 ✓; 573/2.197=261 ✓; 293×0.8=235 ✓ | PASS |
| 22 | Upside/downside ratio | 0.37x | 19.6/52.4=0.374 ✓ | PASS |
| 23 | SOM cross-check performed | base 3yr rev CAGR 22.3% < SOM 35.7% → consistent | ✓ | PASS |
| 24 | Every unresolved input handled by stated conservative rule, no silent fills | EBITDA reconstructed (cross-check only); FY[Y+2] ROCE NOT FOUND→current 28.3% no uplift; EPS below guidance; peer medians NOT FOUND→no triangulation | all four named and conservative | PASS |
| 25 | One-improvement-one-mechanism (no double credit) | ROCE recovery once (Pillar 1); growth via 3a; shared catalyst flagged | ✓ | PASS |

**Note on Hurdle math (rule 16), worth surfacing:** the maker uses the 4-year EPS ratio FY30/FY26 (2.474), which is CORRECT here only because the operator exit convention values the FY29 exit on FORWARD FY30 EPS. HR then equals the true 3-year price ratio 573/634 = 0.904. Had a trailing exit multiple been used, FY29 EPS (23.98) would have been the numerator and HR ≈ 0.76. The maker matched the convention; not an error.

---

## ROLE 2 EXTENSION — DECISION RULES + POSITION SIZING (Master v3.3 Role 2, B14)

| # | Rule (as written) | Applied in B14 | PASS/FAIL |
|---|---|---|---|
| 26 | AVOID triggers: Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR Hurdle STOP | three fire (Gate0 AVERAGE, U/D 0.37<2x, Hurdle STOP) → AVOID; Gate0<60 WATCHLIST default explicitly overridden by hardest-verdict rule | PASS |
| 27 | Entry conjunction (anti-value-trap) stated explicitly in Section 7 box | present: price-in-zone AND no thesis-broken trigger fired; withdrawn-zone logic stated | PASS |
| 28 | Position sizing: Large/Medium gates; else Small if qualifies as BUY; Promoter cap binds | Small (2-3%), contingent on future BUY-ON-DIPS in zone; Medium/Large criteria explicitly not met; Promoter CAUTION cap noted; no operator override recorded | PASS |

**Position-sizing detail:** Medium requires Gate0 GOOD+ AND Promoter TRUSTWORTHY (GNG is AVERAGE / CAUTION — fails). Large requires Gate0 EXCELLENT + Promoter EXEMPLARY/TRUSTWORTHY + EM EXPANSION + CMP<MoS (fails on all). Small is the correct floor; and B14 correctly makes any sizing conditional because the CMP verdict is AVOID, not BUY. Promoter CAUTION cap binds and is honored. Compliant.

---

## FINDINGS

No CRITICAL. No MAJOR. One MINOR (presentational, non-rule):

- **MINOR (presentational):** B11 Section 4A computes a weighted triangulation of Rs 566 (P/E 85% × 573 + EV/EBITDA 15% × 528) then rounds/anchors the base fair value to the governing P/E figure Rs 573 rather than carrying Rs 566. The rounding is immaterial (P/E is the operator-governed primary; +1.2% on base fair value does not move entry Rs 293, MoS Rs 235, the Hurdle STOP, or the AVOID decision). Not a rule violation; the underlying "both tracks carried" rule substantively passes.

## DESTINATION PE / DECISION — CONCUR

Destination PE 20x forward is applied correctly and admissibly (below the 25x cap). Hurdle STOP (base 0.90 / bull 1.20) and the AVOID (on-valuation) decision follow from correct rule application. No recomputation of destination PE or decision is warranted. I CONCUR with B11 and B14 on every rule checked.

**Rules checked:** 28 (25 valuation + 3 Role 2 extension). **Passed:** 28. **Acceptance rate:** 100%.
