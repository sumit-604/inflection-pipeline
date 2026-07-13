=== FILE: verifier-summary.md ===

# Verifier Summary (final, phase 3) — AMAGI, run 2026-07-12

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance |
|---|---|---|---|
| Numerical accuracy | 93.6 | A (B12a, haiku) | 93.6% — 47 numbers checked, 0 CRITICAL, 0 MAJOR, 3 MINOR |
| Red flag coverage | 63 | B (B12b, opus) | 63% — 19 independent flags found, 12 caught, 4 partial, 4 MAJOR/3 MINOR |
| Framework adherence | 96.8 | C (B12c phase-1 + B12c-valuation phase-3, opus) | phase-1 96.7% (61 checked, 6 MINOR); phase-3 97% (38 rules, 4 MINOR); 0 CRITICAL/0 MAJOR both halves |
| Peer utilisation | 92 | D (B12d, sonnet) | 92% — 12 peers audited, 11 substantive, 1 MAJOR/1 MINOR |
| **Overall** | **63** | min of four | band 60-74; PROCEED-family downgrades one level; not forced REWORK (>=60, 0 CRITICAL) |

Binding component: red flag coverage 63 (Verifier B, B05 under-weighted cash conversion and FX flattered revenue quality). The clean 97% phase-3 valuation audit does not move the minimum. REWORK check: verifier A CRITICAL 0, verifier C valuation CRITICAL 0 / MAJOR 0, minimum acceptance 63 above the 60 floor, forced_rework false.

## CRITICAL findings

None. Zero CRITICAL across all four verifiers and both phases.

## MAJOR findings

| # | Verifier | Location | Note |
|---|---|---|---|
| 1 | B | B05 cash-conversion gap (Feb call p.5-6; May call p.9) | No cash conversion red flag raised: FY26 adjusted FCF ₹38cr about 24% of adjusted EBITDA ₹156cr; 9M reported OCF negative ₹76cr; adjusted OCF strips IPO and ESOP buyback cash, against the INDETERMINATE-cash rule. |
| 2 | B | B05 §2A/§4D revenue quality | FX flattered growth not flagged: 30% reported versus 23% CC (about 7pt FX); NRR 127->126; CC NRR only north of 120%. |
| 3 | B | B05 §3C customer adds | Net logo adds decelerated more than 50% (67->29) and Q4 net-negative (27 add/30 churn); B05 rated risk Low, under-weighted alongside softening CC NRR. |
| 4 | B | B05 contradiction, Feb call (p.11 vs p.18) | Missed intra-call contradiction on perpetual-license overhang: Vijay (drove H1 swing) versus Baskar (no overhang), same Feb 2026 call. |
| 5 | D | B06 Part 1 Claim 5; B06 flags (RateGain) | B06 overstated RateGain disclosure proactiveness: the lost client (4% of MarTech revenue) and NRR figures (110 to 100) were first raised by analysts in the Nov 11 2025 call, not volunteered by management. Underlying comparison to Amagi's initial purely strategic framing still holds; framing corrected before reliance. |

## MINOR findings

| # | Verifier | Location | Note |
|---|---|---|---|
| 1 | A | B02 Finding #2; B04 §1E | AWS six-year commitment ₹24,176.20mn sourced via B02 secondary interpretation, not independently extracted (Sep 30 2025 contingent ₹22,531.72mn confirmed). |
| 2 | A | B02 Finding #3; B03 p.41 | Transfer-pricing contingent ₹592.48mn and total tax litigation ₹1,175.07mn cited via Prospectus p.417-420 but not independently extracted; governance material, no core-metric impact. |
| 3 | A | B04 §1C line 60 | H1 FY26 segment split (Streaming 52.86%, Monetization 25.28%, Cloud 21.86%) cites Prospectus p.236 but not independently verified; sums to 100%. |
| 4 | B | B05 §1B | Underlying growth drifts 30%->27%->26% within the Feb call; pipeline fixes it as a single 25-30%. |
| 5 | B | B05 red_flags | Q3 largely able to hold price versus Q4 rate-haircut admission not called out as its own contradiction. |
| 6 | B | B05 §3B | Streaming (over half of revenue) is the slowest segment (26% reported, ~19% CC); all three over 25% is reported-INR framing. |
| 7 | C (phase-1) | B01 Block C / C2 | PAT CAGR 28.18% scored 5 via the endpoint-CAGR edge rule; correct per the literal rubric, loss path logged. DECISION-SENSITIVE: if C2 were 0, Core = 39 -> AVOID; the AVERAGE rests on this convention crediting a 28% CAGR across the FY22-FY25 loss window. |
| 8 | C (phase-1) | B01 Block B / B3 | Mechanical band 5 for literal +0.82 overridden to 0 as a double-negative artifact; unauthorised by the written rubric but conservative, flagged, immaterial (Core would be 49, still AVERAGE). |
| 9 | C (phase-1) | B01 Block A / ROCE denominator | Used Other Liabilities as a current-liabilities proxy FY2021-FY2025 because the source does not split current/non-current; disclosed, immaterial, every A-line scores 0. |
| 10 | C (phase-1) | B07 §2C / capex_embedded_growth_pct | NOT APPLICABLE correctly un-estimated in prose but rendered as numeric 0 in YAML; risks a downstream misread as a scored zero-growth input. |
| 11 | C (phase-1) | B07 §6D combined classification | HIGH POTENTIAL on AVERAGE-backward + STRENGTHENING-forward (30.0, below the 40 EXPANSION threshold); disclosed and symmetric, sits at the generous end; combined matrix not in the stage prompt, so not a hard fail. |
| 12 | C (phase-1) | B07 D1/D2 throughput KPIs | D1 and D2 both draw on the same KPI dashboard; maker separated the network-effect double-count and discounted D1 to 0.7x, overlap handled; noted so synthesis does not re-credit a third time. |
| 13 | C (phase-3) | B11 §1B Pillar 3b | 3b +3x rests on a claim-tier 0-12m catalyst (NEWSPULSE) and 0.7x-weighted self-characterized D1; sits at the generous edge of the EM-gated table. Even at +2x, destination PE 20.0x, Hurdle STOP / AVOID unchanged. |
| 14 | C (phase-3) | B11 RRM derivation | Cash uncertainty double-penalized (0.80x in base AND +1.0% in r). Self-disclosed and conservative; a double-penalty not a double-credit, single-credit rule not breached; decision unaffected. |
| 15 | C (phase-3) | B14 §7 verdict card | Verdict labeled WATCHLIST while three Master AVOID triggers fire (Gate0 AVERAGE, HR STOP, U/D<2x); reconciled via Gate0<60 default-WATCHLIST rule plus authoritative FTTCP investable override. Identical operating instruction (no buy at CMP); no decision impact. |
| 16 | C (phase-3) | B11 Hurdle Ratio | Invariant-to-EPS-basis phrasing is loose; HR computed as Exit/CMP on FY30 EPS honors the forward-PE-at-exit instruction and is correct; STOP unaffected. |
| 17 | D | B06 Part 3 Peer Coverage Map (Newgen Q2 FY26) | The nothing material competitive-framing quote attributed to the Nov 2025 call appears only in Newgen's Jul 2025 (Q1 FY26) call; does not affect Claim 3, which cites a verified Jan 2026 quote. |

## Phase-3 valuation-adherence audit (Verifier C, B12c-valuation)

Scope: valuation-adherence (B10, B11) plus Role 2 (B14) decision and position sizing. 32 valuation rules checked, 0 fails. 6 Role 2 rules checked, 0 fails. Acceptance 97% (38 rules, 0 material fails; the discount reflects the 4 MINOR imprecisions above, findings 13 to 16). Destination PE Track 2 21.0x / Track 1 14.7x concurred; Hurdle STOP concurred; decision AVOID on valuation / WATCHLIST at CMP concurred. Role 2 decision adherence: no BUY NOW under INDETERMINATE cash, Small starter ceiling correct, entry conjunction stated, no exit PE sourced outside Section 1B. Position sizing: Large and Medium correctly excluded on Gate0 band / EM band / CMP above entry; PROCEED WITH CAVEATS cap honored.

## Positive confirmations (Verifier C phase-1)

- FLAG-GATE0 is legitimate driver-attribution, not laundering: classification stays AVERAGE, binding deal-breakers stay binding, driver years FY22-FY25 named, self-limited to one clean post-IPO year.
- Deal-breaker logic correct and complete; the only AVOID trigger (net debt/EBITDA above 3x AND interest cover below 3x) correctly not triggered (net cash, interest cover 15.42x).
- EM evidence taxonomy honest; D1 (CEO self-characterisation) correctly held at claim-tier 0.7x/Moderate.
- No-double-counting enforced (A3->F2, B2->C1/D2, B3->D2 each redirected item scored 0); completionist recount performed (7 active < 12 guard); em_score 30.0 arithmetic correct; EM and FTTCP not conflated.
- Promise-delivery spot checks (Verifier B): 5 checked, 5 confirmed, 0 wrong. Credibility grade B concurred, at the low end of B.

## Devil's advocate note (B15, carried for weighting, not a verifier finding)

WEAKENED BUT ALIVE on all four dimensions. Challenges the adopted operating-ROCE override: argues the ₹109-155 zone is about 2x inflated versus a reported-ROCE floor of ₹55-80, and that FY26 negative OCF makes INDETERMINATE lean DECLINING. The AVOID at CMP ₹580 is robust to this; both floors sit far below the price.
