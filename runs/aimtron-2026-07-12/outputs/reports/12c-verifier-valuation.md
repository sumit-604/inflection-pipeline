# VERIFIER C — FRAMEWORK ADHERENCE (PHASE 3: VALUATION ADHERENCE)

**Company:** Aimtron Electronics Ltd (AIMTRON) | **Run:** 2026-07-12 | **Model:** claude-opus-4-8
**Scope:** Valuation (B11) + inputs (B10) vs Section 1B v3.3 (+Amendments 1-9, 4.1-4.5, Reconciliation 3.5.1); EXTENDED to Role 2 (B14) decision rules and position sizing vs Master v3.3.
**Out of scope (done in phase 1):** Gate 0 (B01), Emerging Moat (B07).
**Verdict summary:** CONCUR with B11 and B14. Destination PE, Hurdle verdict, and decision all reproduce cleanly. No CRITICAL or MAJOR findings. Two MINOR notes, both conservative and decision-neutral.

---

## A. PILLAR 1 — ROCE BASE (continuous formula, Amendment 5; Reconciliation 3.5.1)

| Rule | Framework authority | B11 application | Recompute | Verdict |
| --- | --- | --- | --- | --- |
| Continuous formula, not old bands | Amdt 5: 0.5×ROCE+7.5, floor 9x, cap 24x | 0.5×24.0+7.5 = 19.5x | 19.5x | PASS |
| ROCE = FTTCP forward verdict as sole authority | FTTCP verdict STAGNANT → current ROCE | Uses current 24.0% | — | PASS |
| Normalization route (Amdt 9 Route A/B, 4.5) | Reconciliation L48: "Neither route may be invoked on a STAGNANT or DECLINING ROCE verdict." | Route = NONE; Amdt 4.5/9 explicitly barred; recovery NOT credited | — | PASS |
| Floor/cap clip | 19.5 within [9,24] | No clip needed | 19.5x | PASS |
| Single-credit route stated | Amdt 4: worksheet must state route | "ROCE recovery credited via: NOT CREDITED"; Strategic ROCE re-rating route barred | — | PASS |

The maker correctly recognized ROCE 24.0% is SUSTAINED (STAGNANT verdict), not a depressed trough, so neither the Route A operational-ROCE fix (denominator bloat) nor the Route B pre-cycle normalized anchor (numerator trough) is eligible. Statutory 24.0% feeds the formula directly. This is the exact case the reconciliation doc bars. Correct.

---

## B. PILLAR 2 — CASH CONVERSION MULTIPLIER

| Rule | Framework authority | B11 application | Verdict |
| --- | --- | --- | --- |
| Multiplier matches determination | Master Pillar 2 bands | INDETERMINATE (FTTCP) → conservative 0.65x | PASS (see MINOR-1) |
| No offset on non-growth-induced drag | Master: offset applies ONLY to growth-induced | Offset = 0 (growth-induced not affirmable) | PASS |
| No premium-scaling on structural (Appendix A not reversed) | Appendix A: premiums NOT scaled by cash mult | Premiums independently gated; not scaled | PASS |
| QAB math | A×B | 19.5×0.65 = 12.675 → 12.7x | PASS |

**MINOR-1.** The Master 0.65x band description is "Structurally negative — rating agency confirms persistent WC," and the rating-agency WC quote is NOT FOUND (B10 unresolved, HIGH priority). A strict band reading with no rating-agency confirmation would land at 0.80x (CFO-negative growth-phase drag), which raises QAB to 15.6x. The maker instead applied the documented INDETERMINATE-conservative pipeline rule ("use the more conservative multiplier and say so"), supported by three years of cumulative CFO/PAT −0.13x, FY25 CFO −Rs17.69 Cr, and receivables +417% YoY. This is the MORE conservative (lower-PE) choice and is decision-neutral: the report itself notes 0.80x → QAB 15.6x still yields a Hurdle STOP and AVOID. No value is inflated; the deviation, if any, is in the direction of caution. Recorded as MINOR, no recompute.

---

## C. PILLAR 3 (3a/3b/3c) + STRATEGIC PREMIUM

| Component | Evidence / gate | Award | Verdict |
| --- | --- | --- | --- |
| 3a Growth Visibility (📄 only) | capex-embedded NOT FOUND; order book NOT FOUND; SOM CAGR ≥20% but capacity cross-check FAILS (Vinyas Rs500-600/line vs asserted Rs100); delivery grade C. 0/4 qualifiers; grade C caps 3a at +2x | +0x | PASS |
| 3b Moat Formation (EM-gated) | EM 23 < 25 → Master table "EM below 25 = +0x" | +0x | PASS |
| 3c Duration (📄 order-book tenor) | No signed order book / LoA tenor disclosed | +0x | PASS |
| Pillar 3 combined ≤ +6x cap | 0 ≤ 6 | +0x | PASS |
| Strategic Premium | ROCE re-rating barred (recovery not credited + STAGNANT); no licence/monopoly/brand/turnaround | +0x | PASS |
| Shared-catalyst flag | No premium awarded → N/A | false | PASS |

All Pillar 3 awards match the injected EM/catalyst/evidence inputs. RDSO primary catalyst correctly pays +0x at EM 23 with no documented order value.

---

## D. UNDISCOVERED ALPHA + SECTOR CAP + BOTH TRACKS

| Rule | Framework authority | B11 application | Verdict |
| --- | --- | --- | --- |
| UA three-qualifier gate | Amdt 3: listed ≥12m; Gate0≥60 or EM≥25; FII+DII <3% — ALL three | listed YES; Gate0 72 YES; FII+DII NOT FOUND → not all three | PASS |
| UA correctly withheld | Amdt 3 | UA NOT applied (FII+DII unverifiable) | PASS |
| UA ordering | Amdt 3: min(Raw×1.25, Cap), UA before cap | F2 = F = 12.7 (no uplift); min(12.7, 25) = 12.7 | PASS |
| Sector cap value | B10 override: Recycling/Manufacturing 25x supersedes manifest Pharma/CDMO 38x | 25x used, not 38x | PASS |
| Sector cap absolute | Master: cap cannot be breached | 25x binding | PASS |
| Track 2 additive raw PE | A+B+C+D+E chain | 12.7 + 0 + 0 = 12.7x | PASS |
| ±7.5% range | Amdt 6 | 11.75-13.65 → 11.5-13.5x | PASS |
| Both tracks carried through | Master RRM Dual-Track | Track 1 and Track 2 present in every FV table and verdict card | PASS |

The manifest 38x was correctly overridden to 25x per FTTCP deliberation. No quality uplift on the cap (UA not triggered) — correct, since uplift requires UA.

---

## E. RRM DUAL-TRACK

| Rule | Framework authority | B11 application | Recompute | Verdict |
| --- | --- | --- | --- | --- |
| Base r + governance/durability adjust | Master: small/micro 14%; adjust; bound [9,18] | 14% +1.5% (CONCERN+grade C) +1.0% (INDETERMINATE cash+RPT) = 16.5% | in-bound | PASS |
| RRM formula, percentage-point reading | Amdt 4.4 | 1+(13.5−16.5)×0.12 = 0.64 | 0.64 | PASS |
| Floor at ×0.70 | Amdt 4.4 bounds ×0.70-×1.60 | 0.64 floored to 0.70 | 0.70 | PASS |
| Track 1 dest PE | Fundamental Base PE × RRM, capped | 12.675×0.70 = 8.87 → 8.9x (cap 25 no effect) | 8.9x | PASS |
| Track 1 range | Amdt 6 | 8.2-9.5x | 8.23-9.57 | PASS |
| Divergence + conservative governs | Master: >15% → more conservative sets entry | (12.7−8.9)/12.7 = 30% → Track 1 governs | 29.9% | PASS |

---

## F. TWO-TIER HURDLE + HURDLE RATIO

| Rule | Framework authority | B11 application | Recompute | Verdict |
| --- | --- | --- | --- | --- |
| Tier assignment | Amdt 4.3: Tier B needs ALL (FII+DII≥3%, promoter TRUSTWORTHY+, no structural FLAG-CASH, Gate0 GOOD/EM≥25) | Fails 3 gates → Tier A default, hurdle 25%, threshold 1.953 | — | PASS |
| Current PE | 1390/18.49 | 75.2x | 75.17 | PASS |
| HR formula | Amdt 2: (1+EPS CAGR)³ × (Dest PE mid ÷ Current PE) | see below | — | PASS |
| HR Track 1 base | 1.24³=1.9066 × (8.9/75.2) | 0.226 | 0.2257 | PASS |
| HR Track 1 bull | 1.29³=2.1467 × (8.9/75.2) | 0.254 | 0.2541 | PASS |
| HR Track 2 base/bull | ×(12.7/75.2) | 0.322 / 0.363 | 0.322 / 0.362 | PASS |
| Bull EPS CAGR credibility gate | Amdt 2: grade C (Mixed) → Base+5% max = 29% | 29% used, face-value bull disallowed | — | PASS |
| Verdict | HR(Bull) < 1.953 → STOP | STOP both tracks | — | PASS |

HR(Bull) 0.254/0.363 is an order of magnitude below the 1.953 threshold. STOP is unambiguous. The credibility-grade gate on Bull was correctly applied (grade C caps bull at Base+5%).

---

## G. PROJECTIONS, FAIR VALUES, ENTRY (spot recompute)

| Item | B11 value | Recompute | Verdict |
| --- | --- | --- | --- |
| Bear EPS (7% CAGR) | Rs22.65 | 18.49×1.07³ = 22.65 | PASS |
| Base EPS (24%) | Rs35.25 | 18.49×1.9066 = 35.25 | PASS |
| Bull EPS (29%) | Rs39.69 | 18.49×2.1467 = 39.70 | PASS |
| Track 1 FV bear/base/bull | 202/314/353 | 202/314/353 | PASS |
| Track 2 FV bear/base/bull | 288/448/504 | 288/448/504 | PASS |
| Expected CAGR (35/45/20) | −41.6% | 0.35(−47.5)+0.45(−39.1)+0.20(−36.7) = −41.6% | PASS |
| Entry (Tier A ÷1.953) | Rs161 | 314/1.953 = 160.8 | PASS |
| MoS (20% below entry) | Rs129 | 161×0.8 = 128.8 | PASS |
| Upside/downside | ≈0 (best −64%) | fails ≥2x | PASS |
| SOM cross-check | consistent (27% < 46.6%) | performed | PASS |

Grade-C probability weights 35/45/20 are correct per Master Section 4D. Track 1 (conservative, governing) correctly sets the entry zone.

---

## H. ROLE 2 (B14) — DECISION RULES + POSITION SIZING (Master v3.3)

| Rule | Framework authority | B14 application | Verdict |
| --- | --- | --- | --- |
| BUY/WATCHLIST/AVOID rule | Master L809: AVOID if Gate0 AVERAGE/AVOID OR Promoter CONCERN/AVOID OR U/D<2x OR Hurdle STOP | Four AVOID triggers fire → AVOID | PASS |
| Promoter CONCERN → AVOID regardless | Master L916/818 | AVOID; CONCERN cap acknowledged | PASS |
| Valuation not re-derived in Role 2 | Master: B11 authoritative | "no exit multiple re-derived"; B11 carried verbatim | PASS |
| Entry = FV ÷ (1+hurdle)³ | Amdt 4.3 / Master 4E | 314/1.953 = 161 | PASS |
| MoS 20% below entry | Master 4E | 129 | PASS |
| Position sizing | Master L813-818: promoter cap always binds | NONE (AVOID takes no position); notes CONCERN cap would bind to bottom rung had it cleared | PASS |
| Entry conjunction (anti-value-trap) | Master L811 | Stated explicitly in Section 7 verdict box | PASS |
| Position-size override | operator only | none recorded | PASS |

**MINOR-2.** B14 Section 7 frames Gate 0 AVOID as a "default WATCHLIST floor, overridden downward" (tracking Master L915, Gate0<60→WATCHLIST default), whereas Master L809 lists Gate 0 AVERAGE/AVOID as a direct AVOID trigger (and B14's own YAML lists it as an avoid_trigger). The two framings coexist in the framework itself; with three other independent AVOID triggers firing (Hurdle STOP, Promoter CONCERN, U/D<2x), the verdict is robustly AVOID under either reading. Presentational only; no decision impact.

---

## COVERAGE + CONCLUSION

~38 valuation-scope rules checked across Pillars 1-3, Strategic, UA, sector cap, both tracks, RRM, two-tier hurdle, Hurdle Ratio, projections, entry/MoS, and Role 2 decision + sizing. Every value-bearing rule reproduces within tolerance. Zero CRITICAL, zero MAJOR. Two MINOR notes, both conservative and decision-neutral (Pillar 2 0.65x rating-agency nuance; Role 2 Gate0 framing).

**recomputed_destination_pe:** none (concur — 8.9x RRM / 12.7x additive stand).
**recomputed_decision:** none (concur — AVOID on valuation, Hurdle STOP).
