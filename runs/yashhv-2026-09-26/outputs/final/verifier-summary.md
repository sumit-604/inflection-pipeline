# YASHHV verifier summary (phase 1)

Yash Highvoltage Ltd. Run 2026-09-26. Phase 1 scope: Verifiers A, B, D in full; Verifier C on the Gate 0 and Emerging Moat half only. The valuation half of Verifier C, the expectation ledger audit and the business understanding narrative audit are PENDING PHASE 3.

## Phase 1 confidence delta

| Component | Score | Basis |
| --- | --- | --- |
| numerical_acceptance | 100 | B12a run 1 (not re-run): 35 of 35 numbers clean; 35 of 85 material numbers checked, 41% coverage |
| redflag_coverage | 88 | B12b run 2: 15 of 17 MATERIAL items held upstream (9 caught, 6 partially caught, 2 missed); strict caught only reading 9 of 17 = 53%, recorded, not used |
| framework_adherence | 69.4 | B12c run 2, phase 1 portion: 25 of 36 rules passed, 11 fails, all MINOR |
| peer_utilisation | 66.7 | B12d run 1 (not re-run): 8 of 12 peer transcripts SUBSTANTIVE |
| overall | 66.7 | min of the four applicable components |
| overall_set_by | peer_utilisation | |
| not_applicable | none | every component has a denominator of 4 or more |

Band: 60 to 74. PROCEED verdicts downgrade one level (set by peer_utilisation).

REWORK gate: NOT TRIGGERED. Verifier A CRITICAL 0; identity check strikes 0; no governed acceptance rate below 60. Verifier B's strict reading (53%) sits below 60; the block acceptance_rate (88) is the governed figure.

## Acceptance rates, final run

| Verifier | Model | Run used | CRITICAL | MAJOR | MINOR | Acceptance |
| --- | --- | --- | --- | --- | --- | --- |
| A numerical | claude-haiku-4-5 | run 1 | 0 | 0 | 0 | 100 |
| B red flags | claude-opus-5-5 | run 2 | 0 | 8 | 12 | 88 (strict 53) |
| C framework (phase 1 half) | claude-opus-5-5 | run 2 | 0 | 0 | 11 | 69.4 |
| D peers | claude-sonnet-5 | run 1 | 0 | 0 | 5 | 100 (peer utilisation 66.7) |

## Findings, sorted by severity

### CRITICAL

None in the final run.

### MAJOR

| Verifier | Location | Note | Evidence anchor |
| --- | --- | --- | --- |
| B | B05 3B | MISSED export premium drift 2.2-2.4x (Call-1) vs 30-40% (Call-2) | Call-1 p11-12; Call-2 p22 |
| B | B06 Part 1/2E; coverage map POWERINDIA Aug-2026 | MISSED Chinese transformer/GIS entry allowed (policy moat easing) | POWERINDIA Aug-2026 l.508-514; QPOWER Aug-2026 l.762-772 |
| B | B06 Part 1/Part 4 | PARTIAL: Chinese-restriction peer question never adjudicated; should be CONTRADICTED, B06 reports 0 contradictions | Call-3 p23; POWERINDIA Feb-2026 l.558-561; QPOWER Nov-2025 l.654-656 |
| B | B06 Claim 1 | PARTIAL, sign reversed: insulator scarcity is an input risk for bushings, contradicts Yash 'buttoned up' supply chain | QPOWER Aug-2026 l.902-904; QPOWER Feb-2026 l.548-553; Call-3 p25 |
| B | B05 2A/4D | PARTIAL: FY27 margin guided 24-25% below FY26 25.7% vs Call-2 1.5-2 year maintain/increase promise; steep became gradual; no 4D flag | Call-2 p11; Call-3 p8-9 |
| B | B05 2E/2C | PARTIAL: disclosure regression from Call-A segment EBITDA to refusals on price hike, realisation, retrofit margin, Sukrut EBITDA | Call-A p6; Call-1 p24; Call-3 p13, p21, p26, p27 |
| B | B05 Correction #13/3B/4A | PARTIAL: customer-channel report of RIP scarcity easing plus four localisers; RIP pricing implication not drawn | Call-3 p13-14, p20 |
| B | B05 Correction #4/1C/2E | PARTIAL and partly overstated: misses Call-2 'developed in-house' and same-page Call-3 over/ongoing conflict; Call-A/Call-1 accounts reconcile as two counterparties | Call-2 p18; Call-3 p15; Call-A p9; Call-1 p18-21 |

All eight are open. Stage 5 was re-run once before this Verifier B pass; stage 6 was not re-run. None of the eight is absorbed into B05 or B06.

### MINOR

| Verifier | Location | Note | Evidence anchor or recompute |
| --- | --- | --- | --- |
| B | B06 2A | MISSED POWERINDIA Q4FY26 slowdown admission | POWERINDIA Jun-2026 l.154, l.671-677 |
| B | B06 2C/2E | MISSED QPOWER entry into bushing-adjacent insulators | QPOWER Aug-2026 l.413-417, l.901-906 |
| B | B05 1A/2A | MISSED brownfield slip | Call-2 p9-10; Call-3 p11, p13-14 |
| B | B05 1B | MISSED greenfield unit-addition drift | Call-1 p13; Call-3 p6, p11 |
| B | B05 Correction #5/#4 | PARTIAL: MGC exclusivity 'at least three more years' shortened to mid-2027; exclusivity direction inverted in #4 | Call-1 p20; Call-3 p15 |
| B | B05 3B | Mis-anchor: 'no price war 7-8 years' is Call-2, not Call-3 | Call-2 p13-14 |
| B | B05 Correction #3 | Misattribution: 'around INR235 crores' is analyst wording | Call-3 p20 |
| B | B05 1A | Rs153cr presented as fact in 1A, as unconfirmed in 1C/2A | B05 1A vs 1C |
| B | B05 1C | Overstated: export-restriction removal tied to MGC agreement end; Call-3 ties it to own core | Call-3 p14, p21 |
| B | B06 Part 5 | Overstated: ~70% capex escalation rests on unconfirmed analyst Rs153cr | Call-2 p16; Call-3 p27 |
| B | B05 preamble | Items claimed folded into 2C/3A/3C/4D (Israel/Oman, 1%/1.5%) are absent | B05 preamble vs body |
| B | B05 3B/4D | PARTIAL: repeated analyst overcapacity insistence not flagged as pattern | Call-2 p13-14; Call-3 p11-12; VILAS May-2026 l.882-885 |
| C | 01-gate0.md Block B capex FY20-21 (F-G1) | FY20-21 capex proxied by CFI against the fixed capex formula; no score effect | none (B2=2, B3=0 either way) |
| C | 01-gate0.md E4, Block B/B4 anchors (F-G2) | E4 anchor placeholder '[page in extracted text]' and bracketed page guesses | fill page numbers |
| C | 01-gate0.md Block A table FY24 (F-G3) | FY24 CE 47.13 stated vs 47.71 from stated inputs; FY24 ROCE 41.8% not 42.3% | CE 47.71cr, ROCE 41.8%, A4 -14.3pp, score 0 |
| C | 01-gate0.md M8 (F-G4) | M8 scored 0; rubric 'mentioned unquantified = 1' fits disclosed agency agreements | M8=1, moat 22/60, grand 89, STRONG, GOOD |
| C | 01-gate0.md M11, data_notes (F-G5) | M11 uses selling-and-admin ratio for 'selling exp %' without a proxy label | label selling-and-admin as proxy |
| C | 01-gate0.md E2 note, B01 data_notes (F-G6) | E2 note overclaims 'CAUSE FOUND/not ongoing': 70,000-share gap vs 11,30,000 OFS unexplained; listing to 30-Sep-2025 window unobserved | reword to consistent-with-OFS; gaps NOT VERIFIED |
| C | 07-emoat.md B2, recount line (F-E1) | 550kV test infra inside the Rs153cr Vadodara capex credited in B1 also counted as a B2 documented item | recount 13; em_score 17.7 unchanged |
| C | B07 evidence_mix (F-E2) | documented=14 omits documented items in scored Weak rows A4, C1 and the E2 export-geography count | documented about 19, not 14 |
| C | 07-emoat.md 1A, B2, catalysts (F-E3) | 'Board's Report' anchors without page; secondary-stage anchors (B03/B05) | add AR pages |
| C | 07-emoat.md 6C (F-E4) | 6C carries B01 run-1 Core 70; current B01 Core 67; band and GOOD unchanged | Core 67 |
| C | 07-emoat.md A1 (F-E5) | A1 zeroed by importing the Family I leg-(a) bar; valid ground is existing-vs-emerging | zero holds; worst case 18.4, MODEST |
| D | B06 Part 2D, QPOWER Feb-2026 JV-name mention | Quote genuine and correctly transcribed, page anchor off by one | claimed p.3, source p.4 |
| D | B06 Claim 2, Sukrut order book Rs4-5cr | Quote genuine, page anchor off by five | claimed p.12, source p.17 |
| D | B06 Claim 2, Sukrut 'three times' 12-24mo growth | Quote genuine, page anchor off by two | claimed p.16, source p.18 |
| D | B06 Claim 2, Sukrut Rs25cr legacy losses | Quote genuine, page anchor off by one | claimed p.18, source p.19 |
| D | B06 Claim 3 / Part 2D, VILAS OIP-shortage and first Ramachandran quotes | Both quotes genuine and correctly transcribed, page anchor off by one | claimed p.14, source p.15 |

Verifier A: no findings. 35 of 35 checked numbers match source; no MISMATCH, ANCHOR NOT FOUND or UNANCHORED rows. Source fidelity gate clear.

Verifier C score effects, if the MINOR recomputes were applied: Gate 0 moat 22 of 60 and grand total 89 (F-G4), FY24 ROCE 41.8% (F-G3); classification GOOD and moat class STRONG unchanged; em_score 17.7 unchanged, worst case 18.4, class MODEST unchanged.

## Correction cycle history (run 1 to run 2)

Source: verifier-cycle-1-orchestrator-note.md. Run 1 files carry the -run1 suffix.

Run 1 results:

| Verifier | CRITICAL | MAJOR | MINOR | Acceptance |
| --- | --- | --- | --- | --- |
| A | 0 | 0 | 0 | 100 (35 numbers) |
| B | 0 | 13 | 12 | 71 (12 of 17 material, partial counted as caught; strict 29%) |
| C (phase 1 half) | 1 | 4 | 5 | 87.0 (60 of 69) |
| D | 0 | 0 | 5 | 100; 8 of 12 transcripts substantive |

Run 1 confidence delta: numerical 100, redflag 71, framework 87.0, peer_utilisation 66.7, overall 66.7 (set by peer_utilisation). REWORK gate not triggered.

Orchestrator decision (precedent SYNGENE 2026-09-15): stages 1, 5 and 7 re-run once with the run 1 B12b and B12c findings as correction inputs; Verifiers B and C re-run in fresh contexts on the corrected reports. Verifier A not re-run, because the corrections changed scores, not source numbers. Verifier D not re-run, because stage 6 was not re-run. The run 1 B06 findings (QPOWER fixed price contracts, cost pass through read) were carried to synthesis as open findings.

Run 1 Verifier C material findings and their disposition in run 2:

| Run 1 ID | Severity | Finding | Run 2 disposition |
| --- | --- | --- | --- |
| CR-1 | CRITICAL | B07 credited Ensales, Weidmann and Electrolink in both E2 and H2; em_score 25.7 sat 0.7 above the 25 band edge | Fixed at stage 7: agreements scored under E2 only, H2 rescored on Sukrut alone; em_score 25.7 to 17.7, STRENGTHENING to MODEST, combined GOOD+ to GOOD |
| MJ-1 | MAJOR | B07 A1 and B2 rested on the same qualification evidence; existing versus emerging test applied unevenly | Fixed at stage 7: A1 to 0, B2 rescoped to the 2026 qualification pipeline (IEEE US, CENELEC Europe, 550 kV) |
| MJ-2 | MAJOR | B01 ROCE capital employed proxy for FY20-23 broke the fixed formula rule | Fixed at stage 1: A4 scored on FY24-26 exact years only; Block A 18 to 15, core 70 to 67, grand total 91 to 88; classification GOOD unchanged |
| MJ-3 | MAJOR | B01 E2 "dilution, not sell-down" note conflicted with B01's own share counts | Fixed at stage 1: decline traced to the RHP promoter offer for sale; run 2 Verifier C still finds the note overclaims (F-G6, MINOR) |
| MJ-4 | MAJOR | B07 Section 2C prescribed formula not run | Fixed at stage 7: 153 x 4.54 FAT = Rs 694.6 Cr = 295% of FY26 revenue, caveated as a mechanical ceiling |

Run 1 Verifier B material items and their state in run 2: the FY27 growth versus invoicing contradiction, the three technology source accounts, the customer concentration answer in Call-A, the margin explanation split, and the restated historical CAGR moved from MISSED or PARTIAL to CAUGHT or PARTIAL after the stage 5 re-run. The run 1 flag "EBITDA step change pushed one year" was NOT SUPPORTED and stage 5 withdrew it. Items that sat in B06 stayed open because stage 6 was not re-run: the Chinese restriction contradiction, the Chinese liberalisation evidence, and the QPOWER fixed price read (run 1 item 27: QPOWER "98% is fixed prices", Q1-Q2 FY27 margin hit, against Yash "we are protected"; Call-3 p8, p12-13; QPOWER Feb-2026 p9; QPOWER May-2026 p21; VILAS May-2026 p12). The run 2 Verifier B pass did not re-list item 27; it is carried here and in the gate recommendation from run 1.

Movement between runs: redflag_coverage 71 to 88; framework_adherence 87.0 to 69.4; overall 66.7 in both runs, set by peer_utilisation in both. The framework fall reflects a fresh run 2 audit over 36 rules with 11 MINOR fails, against run 1's 69 rules with 1 CRITICAL and 4 MAJOR fails. No MAJOR or CRITICAL framework finding remains.

## Verifier disagreement log

none. Verifier A returned zero findings (35 of 35 numbers clean); no downstream step conflicted with a Verifier A source fidelity verdict. Source: verifier-disagreements-phase1.md.
