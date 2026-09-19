# SSWL verifier summary (phase 1)

Run: sswl-2026-09-19. Scope: Verifiers A, B, D in full; Verifier C Gate 0 and Emerging Moat portion only. Verifier C valuation audit pending phase 3.

## Confidence delta (phase 1)

| Component | Score | Verifier | Counts |
|---|---|---|---|
| numerical_acceptance | 94 | A (B12a) | 18 of 47 material numbers checked (38% coverage); 0 CRITICAL, 1 MAJOR, 1 MINOR |
| redflag_coverage | 71 | B (B12b) | material caught 10 of 14 (3 caught, 7 partially caught, 4 missed); strict 21%, half credit 46% |
| framework_adherence | 86 | C (B12c, phase 1) | 67 of 78 rules pass (Gate 0 43/48, EM 24/30) |
| peer_utilisation | 92 | D (B12d) | 11 of 12 peer transcripts substantive and confirmed |
| overall | 71 | set by redflag_coverage | band 60-74: PROCEED verdicts downgrade one level |

Verifier A identity check: no CRITICAL rows; nothing struck.

## Acceptance rates

| Verifier | Model | Acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| A numerical | claude-haiku-4-5-20251001 | 94 | 0 | 1 | 1 |
| B red flags | claude-opus-5 | 71 | 0 | 12 | 13 |
| C framework (phase 1) | claude-opus-5 | 86 | 0 | 4 | 7 |
| D peers | claude-sonnet-5 | 92 | 0 | 1 | 2 |

Verifier B coverage basis (verbatim): "14 material (1 CRITICAL + 13 MAJOR) of 30 listed; 3 caught, 7 partially caught, 4 missed." The one CRITICAL item in its material set (R12, the steel versus alloy segment split stonewall) was CAUGHT upstream and is not a finding against the pipeline.

## CRITICAL

None.

## MAJOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 1 | A | Stage 1 Block A (computed EBITDA) | Claimed Rs 510.23 Cr (screener formula) vs AR Board's Report line E (p.19): Rs 522.956 Cr standalone or Rs 513.40 Cr consolidated. Delta 2.4% on standalone. Stage 1 does not state the basis or reconcile to AR EBITDA. Material because EBITDA drives ROCE/FCF/leverage downstream. source_fidelity: true |
| 2 | B | B05 1A/2A/block trigger 2 | MISSED: Bhuj knuckle capacity conflict 1.1mn (MD) vs 0.6mn (CFO); pipeline adopts 1.1mn. Anchor: Q1 FY27 p.4, p.7 |
| 3 | B | B05 3A/4D; B06 Q4 | MISSED: alloy domestic margin/pricing pressure admitted twice and contradicted within the same call; LBF2 central. Anchor: Q3 FY26 p.19; Q1 FY27 p.12 |
| 4 | B | B05 2A | MISSED: knuckle FY26 revenue guide miss and customer count stagnation. Anchor: Q2 FY26 p.12; Q4 FY26 p.4; Q1 FY27 p.6, p.13 |
| 5 | B | B05/B06 | MISSED: Bhuj aftermarket export orientation with Arays support. Anchor: Q1 FY27 p.14 |
| 6 | B | B05 2A row 6, 4A trigger 2, block timeline_slippages | Promise direction WRONG: Bhuj graded on track for Oct-2026 trial; transcript moves trial to Q4 FY27; 4-5 month delay quote misdated (Q4 FY26 p.19, not Q1 FY27); "external guide unchanged" is false. Anchor: Q3 FY26 p.10, p.16; Q4 FY26 p.5, p.19; Q1 FY27 p.4 |
| 7 | B | B05 1A/1C | PARTIAL: stalled alloy share (35-37% across 4 calls vs promised rise) not flagged; EBITDA/wheel gain is price, not mix. Anchor: Q2 FY26 p.3; Q3 FY26 p.4; Q4 FY26 p.4; Q1 FY27 p.3, p.12 |
| 8 | B | B05 1B/4D | PARTIAL: capex creep Rs460cr to Rs550cr to Rs650cr, reversed no steel capex statement, unchanged +Rs200cr debt guide not flagged. Anchor: Q3 FY26 p.8, p.10, p.16-17; Q4 FY26 p.16-17; Q1 FY27 p.7 |
| 9 | B | B05 3B | PARTIAL: management's own contradictions of "absolute pass-through" and working capital admissions not flagged. Anchor: Q3 FY26 p.5; Q4 FY26 p.20-21; Q1 FY27 p.9, p.13 |
| 10 | B | B05 2E/4D | PARTIAL: offline via SGA deferral pattern (selective disclosure risk) not named; US run rate deferral missed. Anchor: Q2 FY26 p.6-7; Q3 FY26 p.9, p.14; Q1 FY27 p.10-11 |
| 11 | B | B05 2A tally | PARTIAL: FY26 export target Rs600-650cr vs Rs454cr actual omitted from promise table; tally overstates delivery. Anchor: Q2 FY26 p.11; Q4 FY26 p.15 |
| 12 | B | B05 block flag 1, 1B, analyst note | PARTIAL/misclassified: management describes DEBTOR (receivables) factoring; pipeline treats it as confirming the payables supplier finance arrangement (LBF3). Anchor: Q3 FY26 Jain p.9; Q1 FY27 Jain p.9 |
| 13 | B | B05 1B, block guidance, 2A row 7 | FY27 EBITDA guide misread as Rs650-750cr; transcript gives ~Rs650cr FY27 and ~Rs700-750cr the following year. Anchor: Q4 FY26 p.8, p.17; Q1 FY27 p.11 |
| 14 | C | B01 Block A | ROCE formula substitution (proxy CE FY22-24 as Equity + Borrowings). Recomputed on exact year window FY25-FY26: Block A 15, Core 67, GOOD |
| 15 | C | B01 B2/B3/B4/E2/M12 | Partial window scoring vs rules 5/6. Strict reading (N/A scores 0): Core 47, AVERAGE. Operator ruling needed |
| 16 | C | B01 M5 | Margin rank set reading. Parallel reading: M5 3, STRONG, GOOD+. Strict segment reading: M5 0, MODERATE, GOOD |
| 17 | C | B07 B1 + H2 + recount | One improvement, one mechanism: Echanda Urja and Clean Max Astria captive power credited in B1 and again in H2 and counted twice in the DOC recount. em_score 17, MODEST unchanged |
| 18 | D | B06 Part 1 Q2 + Part 3 coverage map, UNOMINDA Q1 FY27 (04-Aug-2026) row | Monthly settlement quote attributed to UNOMINDA Q1 FY27 is absent from that transcript; it sits in UNOMINDA Q4 FY26 (18-May-2026) p.14. Wrong quarter citation; Q2 VERIFIED verdict unchanged (3 peers, 5 other anchors). source_fidelity: false |

## MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 19 | A | Stage 1 Block A (FY22 ROCE) | FY22 ROCE 21.73% NOT FOUND in AR FY26 (FY25-26 comparatives only); source is screener Data_Sheet row 73; Stage 1 cites screener correctly; no contradiction. source_fidelity: false |
| 20 | B | B05 FLAG-SILENCE-CASH | OVERSTATED: working capital strain volunteered twice; interest cost gap pressed in 2 quarters. Anchor: Q4 FY26 p.21; Q1 FY27 p.9; Q3 FY26 p.8-9 |
| 21 | B | B05 FLAG-SILENCE-CUSTOMS | OVERSTATED at RED: SCN ~Rs1.7cr, already repaid with interest, penalty unquantified. Anchor: SSWL-showcause_2026-06-17 p.1-2 |
| 22 | B | B06 Q9 | Capex benchmark uses total FY27 capex Rs600cr as Bhuj alloy base; Bhuj is Rs420cr for 1.2mn alloy plus 0.6mn knuckles; direction survives. Anchor: Q3 FY26 p.8; Q1 FY27 p.7 |
| 23 | B | B05 FLAG-STONEWALL/2E | Omits Q2 FY26 segment margin % ranges and Q3 FY26 ">Rs450" implicit confirmation. Anchor: Q2 FY26 p.7; Q3 FY26 p.13 |
| 24 | B | B05 2C | MISSED: FY26 EBITDA/wheel Rs262 vs Rs272 in the same call. Anchor: Q4 FY26 p.4, p.8 |
| 25 | B | B05 1C | MISSED: US loss magnitude grows between calls (~Rs200cr/yr to Rs300-400cr/yr; FY26 export drop Rs108cr). Anchor: Q2 FY26 p.11; Q3 FY26 p.5; Q4 FY26 p.4 |
| 26 | B | B05 | MISSED: truck demand blip June 2026. Anchor: Q1 FY27 p.15 |
| 27 | B | B05 header | PARTIAL: Deputy MD "family issues" absence on 02-Jun, resignation 03-Jun; reason consistent, not assessed. Anchor: Q4 FY26 p.17; SSWL-dir-resign_2026-06-03 p.3 |
| 28 | B | B05 2A/3C | PARTIAL: LCV self contradiction in the MHCV share answer. Anchor: Q3 FY26 p.9 |
| 29 | B | B05 3D | PARTIAL: Maruti exit vs Maruti pull contradiction; "what contracts" evasion. Anchor: Q3 FY26 p.17-18 |
| 30 | B | B05 4B | PARTIAL: "sole supplier for knuckles" not sent for peer testing; ALICON reports rising die casting capacity. Anchor: Q4 FY26 p.19; ALICON Q1 FY27 p.23 |
| 31 | B | B06 2E(b) | "No SSWL transcript surfaces" labour code risk; SSWL mentions wage increases. Anchor: SSWL Q4 FY26 p.9 |
| 32 | B | B05 2A | Inconsistent gradeability: one quarter of EBITDA/wheel guide graded Delivered while export target held not gradeable. Anchor: Q4 FY26 p.4, p.8; Q1 FY27 p.3 |
| 33 | C | B01 B4/M12 | WC days formula: inventory/payable basis (revenue vs COGS) not stated. No score change determinable |
| 34 | C | B01 M6 | R&D data marked N/A but present in AR (1.14% FY25, 0.40% FY26 of turnover). M6 0 unchanged |
| 35 | C | B07 Section 3 recount | Recount claims 15 documented items; listed items sum to 13, 11 distinct after the B1/H2 duplicate |
| 36 | C | B07 Section 5 R1/H1/F2 | Evidence multiplier outside the defined set (R1 0.67) or inconsistent (H1 INFER 0.5 on a claim; F2 DOC 1.0 on DOC/CLAIM). Recomputed range 16.5-18.1, MODEST holds |
| 37 | C | B07 anchors | Page anchors (AR p.1190, p.2363, p.9666, p.13238) exceed the AR page count and appear to be text file line numbers; some anchors point to company memory or derived blocks rather than source documents |
| 38 | C | B07 2C | Standalone/consolidated basis mix: Rs 5,182.80 Cr labelled standalone vs consolidated in B01; FAT 2.85x vs 2.63x. At 2.63x, capex embedded growth ~30% (vs 33%) |
| 39 | C | B07 H2 strength | "Moderate-Strong" is outside the strength enum (Strong/Moderate/Weak/None); score unaffected |
| 40 | D | B06 Part 1 Q6, WHEELS Q4 FY26 (15-May-2026) row | GST 2.0 "turbocharge the domestic industry" quote cited at p.4; it sits on p.3. Off by one page anchor. source_fidelity: false |
| 41 | D | B06 Part 1 Q3 net read | "No mention" of Vietnam/Thailand overstated: UNOMINDA Q2 FY26 (07-Nov-2025) line 374 has one "Vietnam" token (its own tech centre location, unrelated). UNVERIFIABLE verdict unaffected. source_fidelity: false |

## Verifier C classification sensitivity (verbatim)

- Gate 0: "B01 GOOD (Core 63, MODERATE) holds on its own readings, but three rule readings move it: strict partial-window N/A = AVERAGE (Core 47); M5 parallel reading = GOOD+ (STRONG, 4 moats); exact-year ROCE window = GOOD (Core 67). Operator ruling needed on partial-window treatment and the M5 margin-rank set."
- Emerging Moat: "em_score 17 (17.1) MODEST; recomputed range 16.5 to 18.1 across all multiplier readings; classification robust."
- Credibility (Verifier B): "lower: B- bordering C; misses cluster in management-controlled items (Bhuj timing, knuckles, FY26 exports, speaker contradictions) and B05's two RED silence flags are overstated."
- Promise delivery spot checks (Verifier B): 6 checked, 5 confirmed, 1 wrong.
