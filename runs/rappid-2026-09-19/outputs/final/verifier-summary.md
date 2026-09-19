=== FILE: verifier-summary.md ===

# Verifier summary, RAPPID, phase 1 (2026-09-19)

## Confidence delta (phase 1)

| Component | Score | Verifier and round | Basis |
|---|---|---|---|
| numerical_acceptance | 100 | A (B12a), single round | 49 of 58 material numbers checked; 0 mismatches |
| redflag_coverage | 75 | B (B12b), round 2 | 9 of 12 material caught incl. 2 partial; strict full catch 7/12 = 58% |
| framework_adherence | 75.5 | C (B12c), round 2, phase 1 scope | 40 of 53 rules (Gate 0 24/29, Emerging Moat 16/24); valuation half pending phase 3 |
| peer_utilisation | 100 | D (B12d), round 2 | 8 of 8 peer transcripts substantive |
| overall | 75 | set by redflag_coverage | band 75 to 89, normal confidence |

Acceptance rates by round:

| Verifier | Round 1 | Round 2 | Round 1 counts | Round 2 counts |
|---|---|---|---|---|
| A (B12a) | 100 | not rerun | 0 CRITICAL, 0 MAJOR, 0 MINOR | n/a |
| B (B12b) | 71 | 75 | 0 CRITICAL, 8 MAJOR, 14 MINOR | 0 CRITICAL, 3 MAJOR, 7 MINOR |
| C (B12c) | 79 (46/58) | 75.5 (40/53) | 0 CRITICAL, 2 MAJOR, 10 MINOR | 0 CRITICAL, 2 MAJOR, 10 MINOR |
| D (B12d) | 100 | 100 | 0 CRITICAL, 2 MAJOR, 7 MINOR | 0 CRITICAL, 0 MAJOR, 2 MINOR |

REWORK trigger: none on the partial counts as caught convention. On the strict count, redflag_coverage is 58% (round 2) and 50% (round 1), below the 60% line. Flagged for operator ruling at Halt 1.

Verifier A basis: B12a audited the numbers in the round 1 reports. The round 2 B01 changes are score re-basings on filed AR and RHP figures, audited by Verifier C round 2. Stage 7 was refreshed after Verifier C round 2 (F11) and is not re-verified.

Verifier C scope: Gate 0 and Emerging Moat only. The valuation, expectation ledger and business understanding narrative rules are NOT RUN, pending phase 3.

Verifier A disagreement log: none. B12a carries no findings, so no downstream step conflicted with a source fidelity finding.

## CRITICAL

None, in any verifier, in either round.

## MAJOR

| Verifier | Round | Location | Finding | Disposition |
|---|---|---|---|---|
| B | 2 | B05 3B, 4D, trigger 5 | MISSED non-ferrous pricing contradiction between answers to different analysts (Concall p.10 vs p.3-4, p.5-6, p.15); B05 "consistent throughout" conclusion wrong on pricing risk | OPEN. Carried as a residual finding |
| B | 2 | B05 3D, 2D | MISSED Rs14-15Cr March dispatch concentration (Concall p.23), about 57-61% of H2 FY26 revenue | OPEN. Carried as a residual finding |
| B | 2 | B05 2A, 3D, 4A row 4 | MISSED Praj ARC "sign on thursday" (p.22) and PSU bids "7 to 8 days" (p.26) claims, unreported in the 09/10-Jul-2026 Q1 FY27 update | OPEN. Carried as a residual finding |
| C | 2 | B01 Block A, ROCE (F1, G03, G04) | 5-year ROCE series mixes computed (FY22-24) and AR-disclosed (FY25-26) bases; RHP disclosed ROCE rejected for a denominator that AR p.69 Note 36 K (H + I + DTL) shares; report wrongly says AR denominator not shown. Uniform source: A 12, core 62, GT 75, raw GOOD. Uniform computed: A 15, core 65, moat 15 STRONG, GT 80, raw GOOD+. Final AVERAGE both | OPEN. Operator ruling needed on ROCE source precedence. Decision impact none |
| C | 2 | B07 6C, 6E (F11, E21) | Stale round-1 Gate 0 values (68/15/83, 4 STRONG) in 6C and 6E; current B01 is 63/13/76, 3 MODERATE; 6D AVERAGE survives | FIXED in stage 7 run 2 (6C and 6E refreshed to current B01). Not re-verified |
| B | 1 | B05 (absent) | MISSED: CMD misstated FY26 capex as ~Rs 3.65 Cr then retracted; audited capex Rs 179.4 L; 3.65 Cr equals the unspent IPO capex balance (Rs 364.51 L); current capex funded by bank WC loan while IPO capex money moved to WC (Concall p.12, p.22; 27May2026 results p.10) | FIXED round 2. B05 FLAG-CAPEX-MISSTATEMENT added, plus a High 4D red flag |
| B | 1 | B05 2D | MISSED: results note attributes WC build to "higher order volumes" against +2.1% revenue and Rs 10 Cr held material (results p.9-10) | FIXED round 2. Added to 2B, 2D and 4D. Round 2 Verifier B rates the receivables leg overstated; the inventory leg holds |
| B | 1 | B05 3D | MISSED: Rs 119 Cr GeM bid pipeline (16Oct2025 GBU p.1) never reported on | FIXED round 2. Added to 1A to 1C, 3D and 4D. Round 2 Verifier B rates the severity Medium, not High |
| B | 1 | B06 2B | MISSED: KSB treats the commodity spike as prospective in Mar-2026 while Rappid's order book fell by Sep-2025 [INFERENCE; ferrous caveat] | FIXED round 2. In B06 industry cross-read and peer risks, labelled INFERENCE |
| B | 1 | B06 flags, Part 4 | NOT SUPPORTED: FLAG-MARGIN-CONTRADICTION compared Quest Flow EBITDA 23-25% with Rappid PAT 12.17%; CMD never framed 12% as structural | FIXED round 2. Replaced by FLAG-MARGIN-GAP-VS-NICHE-PEER on like for like bases (4.3-5.6 pts EBITDA, 2.1-2.7 pts PAT) |
| B | 1 | B05 4D | PARTIALLY CAUGHT: WC stress ("no working capital is enough", 50% advances, funding need in 4-5 months, ST debt Rs 841.4 L to Rs 1,784.3 L) not in the red flag table | FIXED round 2. One High 4D row |
| B | 1 | B05 3D | PARTIALLY CAUGHT: order book definitions shift and do not reconcile after the BHEL Rs 18.05 Cr win | FIXED round 2. 3D names the three decompositions |
| B | 1 | B05 3D, 4A | PARTIALLY CAUGHT: Praj Rs 13-14 Cr/yr, ~24-26% of FY26 revenue, concentration unflagged | FIXED round 2. Medium 4D red flag and trigger 4 rewrite |
| C | 1 | B01 A2, M3 (G3) | AR p.69 Note 36 ROCE FY26 14% / FY25 17% omitted and unreconciled; computed 18.7% / 20.2% used; A2 5, M3 3, 4 moats STRONG | FIXED round 2. B01 uses Note 36 figures; A2 3, M3 1, 3 moats MODERATE. Round 2 F1 reopens the mixed basis question |
| C | 1 | B01 E2 (G22) | E2 window substituted; 3-year rule gives 69.46% to 51.58% = -17.88pp, score 0 not 3 | FIXED round 2. E2 scored 0. Round 2 F3 notes the window is about 18 months, not 3 years; score unchanged |
| D | 1 | B06 Quest Flow citations | Page anchors unverifiable: transcript said to hold zero page markers | STRUCK. False: the file carries 32 [page N] markers (orchestrator check and stage 6 round 2). The anchor corrections were applied anyway |
| D | 1 | B06 Part 2D, KSB-Concall_Sep_2025 | Cited p.16; source truth p.11 (line 646) | FIXED round 2. Round 2 Verifier D reports no MAJOR |

## MINOR

| Verifier | Round | Location | Finding | Disposition |
|---|---|---|---|---|
| B | 2 | B05 1C, 2A row 3 | PARTIALLY CAUGHT: CMD calls acquisition money redirection pending and the search open on 01-Jun-2026 (p.22-23) though e-voting closed 29-Apr-2026 | OPEN |
| B | 2 | B05 2A/2B, B06 2B | PARTIALLY CAUGHT: KSB 17-Mar-2026 LPG passage (lines 321-331) dates the foundry gas restriction to about March 2026; unused | OPEN |
| B | 2 | B05 2D, 4D row 4 | OVERSTATED: CMD ties receivables to March dispatches (p.23), not held material; written against spoken WC conflict holds for inventory only (+Rs1,050L); High should be Medium | OPEN |
| B | 2 | B05 4D row 5 | OVERSTATED severity: Rs119Cr GeM figure was a bid pipeline "where result is awaited", not a promise; Medium, not High | OPEN |
| B | 2 | B05 1C | Misread: 09-Mar-2026 deck "2 units on 10th March" is the first bench installation phase, not 2 VMCs | OPEN |
| B | 2 | B05 | MISSED/PARTIAL: arithmetic slips (p.14, p.17); six-month margin guidance deferral (p.13); IPO FD parking Rs4.7Cr alongside 8.25% bank debt (p.22, p.24) | OPEN |
| B | 2 | B06 FLAG-MARGIN-GAP-VS-NICHE-PEER | QUESTFLOW H2/FY24 margins compared with Rappid FY26 without qualifying the two-year period mismatch in a commodity shock year | OPEN |
| C | 2 | B01 D2 (F2, G13) | Disclosed 7.52x EBIT/interest used over formula; recomputed 7.27x (9.67/1.33) | OPEN. Score 4 unchanged |
| C | 2 | B01 E2 (F3, G16) | 18-month window labelled as approximating 3 years; Mar-2023 holding NOT FOUND | OPEN. Score 0 unchanged |
| C | 2 | B01 M1 (F4, G18) | M1 on FY23-26 while FY22-26 available; FY22-26 +3.4pp | OPEN. Score 5 unchanged |
| C | 2 | B07 taxonomy (F5, E02) | Concall and presentation items tagged documented; evidence_mix documented overstated | FIXED in stage 7 run 2 (C1 items retagged management claim; H2 memory anchor dropped). Not re-verified |
| C | 2 | B07 multipliers (F6, E07) | A3 documented item scored at 0.5 (should be 1.0); F2 "mixed 0.5" not a defined multiplier | PARTLY FIXED in stage 7 run 2. F2 moved to 1.0. A3 kept at 0.5 by stated reasoning: the process innovation leg is inference, anchor NOT FOUND. Not re-verified |
| C | 2 | B07 H1 (F7, E08) | H1 "Weak" scored MM=2; recomputed 0.7 (-0.7) | FIXED in stage 7 run 2 (H1 raw LM=1). Not re-verified |
| C | 2 | B07 recount (F8, E12) | "Approximately 9"; UL double-counted (8 distinct); H2 omitted; 6D contradicts recount on C1 | FIXED in stage 7 run 2 (exact recount; 6D corrected). B07 run 2 states 9 distinct items with UL counted once, against Verifier C's 8. Not re-verified |
| C | 2 | B07 I2 (F9, E16) | I2 test run for B2 only; A1, C1, E2, R1 not shown | FIXED in stage 7 run 2 (worked for all five; score 0 stands). Not re-verified |
| C | 2 | B07 optionality register (F10, E20) | YAML omits A3 row; H1 claim-only not registered | FIXED in stage 7 run 2 (A3, H1, C2 rows; 9 rows in report and YAML). Not re-verified |
| C | 2 | B07 catalysts_12m (F12, E24) | 24-36m and "long" windows inside the 12-month list | FIXED in stage 7 run 2 (both rows removed; 4 rows remain). Not re-verified |
| D | 2 | B06 Part 2C, ATAM-Concall_Nov_2023 | Cited p.6-9; claim content sits on p.3-8 (capex plan p.3-4, delay p.5-6, ROI p.7, WC framing p.8); p.9 unrelated. Content verbatim-accurate | OPEN. Page range one page too wide at the top end |
| D | 2 | B06 Part 2B, KSB-Concall_Nov_2025 | Cited p.31-32; source truth p.31; p.32 unrelated. Content verbatim-accurate | OPEN. Page range one page too wide |
| B | 1 | B05 2A row 4, 4D | OVERSTATED: Jul-2025 acceleration graded MISSED/High; Q2 FY26 ~Rs 17.19 Cr vs Q1 Rs 11.63 Cr | FIXED round 2. Regraded PARTIAL/Medium; tally 1 delivered, 2 partial, 2 missed |
| B | 1 | B05 2C | Quote misread: Concall p.4 admits the shortfall, not a positive surprise framing | FIXED round 2. Over-promotion score 3 to 2 |
| B | 1 | B05 2E | Overstated: only Nishita Shanklesha pressed the capacity arithmetic (p.11) | FIXED round 2 |
| B | 1 | B05 1C, 2A | "17-Apr-2026 EGM"; approval was by postal ballot, results 30-Apr-2026 (company filing error transcribed) | FIXED round 2 |
| B | 1 | B05 1C | MISSED narrative drift: AR 2026 p.24 names data centre cooling as intended, against the CMD's "not scouted" and "not focusing on export" | FIXED round 2 |
| B | 1 | B05 (absent) | MISSED: no raw material hedge; Rs 15-20 Cr WC needed to hedge (Concall p.26) | FIXED round 2. Folded into the WC stress red flag |
| B | 1 | B05 3B | PARTIALLY CAUGHT: PSU no clause, private clause; within-call reversal p.6 vs p.16 | Superseded. Round 2 Verifier B raises the wider non-ferrous pricing contradiction as a MAJOR (OPEN) |
| B | 1 | B05 1C | PARTIALLY CAUGHT: Mar-2026 install dates missed; counts drift 4 to 5 to 6 benches, 1 to 2 VMCs | FIXED round 2. Watch row in 4D |
| B | 1 | B05 3B | PARTIALLY CAUGHT: FSS "all the valves" and 90% foundry dedication claims unverifiable, alongside "20 warships" | FIXED round 2. Added to 3A |
| B | 1 | B05 4C | PARTIALLY CAUGHT: PIT correction, NSE segment query, ballot corrigendum, results note mislabels | FIXED round 2. Watch row in 4D |
| B | 1 | B05 4B Q1 | PARTIALLY CAUGHT: "I would not use the word delay"; Rs 207.1 L over 6 months | FIXED round 2. Watch row in 4D |
| B | 1 | B06 Claim 1 | MISSED corroboration: KSB Mar-2026 p.9-10 domestic project business without PVC | FIXED round 2. Claim 1 upgraded |
| B | 1 | B06 Claim 4 | MISSED: KSB Aug-2026 p.25 pumps 3-5% of project value | FIXED round 2. Claim 4 upgraded |
| B | 1 | B06 Claim 2 | PARTIALLY CAUGHT: Meson says under 5% of Indian valve makers are non-ferrous and non-ferrous earns better margins; unused | FIXED round 2. Cited in the B06 margin gap flag |
| C | 1 | B01 A3 (G6) | FY22 ROE excluded, rule has no exclusion | FIXED round 2. Median 22.9%, score 5 unchanged |
| C | 1 | B01 M10 (G30) | Stated reason misstates the loosest tier | No change needed. Score 0 correct |
| C | 1 | B01 YAML (G34) | "May not have seen full cycle" flag absent from YAML | FIXED round 2. Added to data_notes |
| C | 1 | B01 FLAG-GATE0 (G37) | Reason mixes FY23-26 CFO with FY22-26 PAT window | FIXED round 2. Matched windows stated |
| C | 1 | B07 H2 (M-2) | H2 documented item anchored partly to company memory | FIXED in stage 7 run 2 |
| C | 1 | B07 F2 (M-4) | F2 multiplier 0.5 on D-tier evidence | FIXED in stage 7 run 2 (1.0) |
| C | 1 | B07 6D (M-5) | 6D calls C1 documented-grade; scored as claim | FIXED in stage 7 run 2 |
| C | 1 | B07 recount (M-9) | "Approximately 9", UL double-counted | FIXED in stage 7 run 2. See round 2 F8 row for the residual count difference |
| C | 1 | B07 I2 (M-12) | I2 test worked for B2 only | FIXED in stage 7 run 2 |
| C | 1 | B07 register (M-14) | A3 row dropped from YAML; H1 and C2 claim-only rows absent | FIXED in stage 7 run 2 |
| D | 1 | B06 Claim 1, ATAM-Concall_Apr_2024 | Cited p.6; source truth p.5 | Applied in stage 6 round 2 |
| D | 1 | B06 Claim 1, ATAM-Concall_Apr_2024 | Cited p.14; source truth p.13 | Applied in stage 6 round 2 |
| D | 1 | B06 Claim 1, KSB-Concall_Sep_2025 | Cited p.11; source truth p.10 | Applied in stage 6 round 2 |
| D | 1 | B06 Claim 2 / 2B, KSB-Concall_Aug_2026 | Cited p.24; source truth p.23 | Applied in stage 6 round 2 |
| D | 1 | B06 Claim 5, KSB-Concall_Aug_2026 | Cited p.9; source truth p.7 | Applied in stage 6 round 2 |
| D | 1 | B06 Claim 1, KSB-Concall_Aug_2026 | Cited p.29-30; source truth p.27 | Applied in stage 6 round 2 |
| D | 1 | B06 Claim 5, KSB-Concall_Nov_2025 | Cited p.39; source truth p.37 | Applied in stage 6 round 2 |

Verifier B round 2 concurs on credibility grade C: "missed items 5, 6, 9 and under-weighted item 4 show spoken claims running ahead of filings, pulling toward the bottom of C, not below it." Promise delivery spot checks: 5 checked, 5 confirmed.

Verifier C round 2 concurs on the phase 1 classifications: Gate 0 AVERAGE, Emerging Moat MODEST (18.2 to 19.7 recomputed range), combined AVERAGE.

Verifier D round 2: 8 of 8 peer transcripts substantive, all claims addressed, no verdict discipline fails.
