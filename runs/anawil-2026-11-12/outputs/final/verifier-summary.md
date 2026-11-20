=== FILE: verifier-summary.md ===

# Verifier summary, phase 3 final

Anawil Wire and Engineering Ltd (ANAWIL). Run 2026-11-12. Phase 1 verifiers A, B, C (Gate 0 and Emerging Moat half) and D ran 2026-11-12. Verifier C's valuation adherence half ran in phase 3 on 2026-11-17 (deferred half of one run; manifest verifier_runs A 1, B 1, C 1, D 1).

## Confidence delta (full four components, phase 3, computed by the orchestrator)

| Component | Value | Block | Basis |
|---|---|---|---|
| numerical_acceptance | 97 | B12a | 418 numbers checked; mandatory tier 183 of 183 |
| redflag_coverage | 100 | B12b | material_found 7, material_caught 7 (4 caught, 3 partly caught counted as caught). Operator ruled 100 as written on 2026-11-15 (handover dossier Section 7 ruling 1); strict caught only reading 4 of 7 = 57 not adopted |
| framework_adherence | 86.5 | B12c (merged) | 167 of 193 rules: phase 1 70 of 79 (Gate 0 47 of 52, Emerging Moat 23 of 27); phase 3 97 of 114 (valuation 89 of 106 including check 15 at 15 of 17 and Role 2 at 20 of 22; ledger gates 8 of 8) |
| peer_utilisation | 100 | B12d | 12 of 12 peers SUBSTANTIVE |
| overall | 86.5 | confidence.yaml | Minimum of the four; set by framework_adherence; band 75 to 89, normal, note specifics. Phase 1 overall was 88.6 |

REWORK test on the values as written: not triggered. Confirmed Verifier A CRITICAL: 0. No acceptance rate below 60 on a denominator of 4 or more. Verifier C phase 3 logged 2 CRITICAL; a Verifier C CRITICAL is not a REWORK trigger (orchestrator Section 4; Verifier C note N8: "No REWORK trigger fires from this verifier").

## Acceptance rates and counts

| Verifier | Model | Acceptance | CRITICAL | MAJOR | MINOR | Other |
|---|---|---|---|---|---|---|
| A, numerical | claude-sonnet-5-5 | 97 | 0 | 3 | 5 | 3 false positives struck under its rule 5b; material universe about 600; mandatory 183 of 183 |
| B, red flags | claude-opus-5-5 | 100 (strict reading 57, not adopted) | 0 | 3 | 12 | 25 independent flags: 12 caught, 10 partly caught, 3 missed (all MINOR); promise spot checks 5, confirmed 4, wrong 1 |
| C, framework, phase 1 | claude-opus-5-5 | 88.6 (70 of 79) | 0 | 2 | 7 | Gate 0 52 rules, 5 fails; Emerging Moat 27 rules, 4 fails |
| C, framework, phase 3 | claude-opus-5-5 | 85.1 (97 of 114) | 2 | 4 | 10 | Valuation 106 rules (67 Role 1, 17 check 15, 22 Role 2); ledger 8 of 8 gates pass; rule 9 (business understanding narrative) NOT ASSESSED, B13 absent at the time |
| C, combined | | 86.5 (167 of 193) | 2 | 6 | 17 | |
| D, peers | claude-sonnet-5-5 | 100 | 0 | 0 | 4 | 12 peers audited, 12 SUBSTANTIVE; claims_all_addressed true |

## Run state of these findings

Phase 1 findings describe the run 1 reports. One remediation cycle ran (the cap) on stages 1, 4 and 5. The current 01-gate0.md, 04-bizmodel.md, 05-concall.md and their blocks are the corrected run 2 versions; run 1 copies are kept as *.run1.md and *.run1.yaml. No verifier re-checked the corrected lines. The Disposition column for phase 1 comes from the run log and the makers' remediation notes, not from a verifier. Phase 3 findings P1 to P16 are open: Verifier C states that P1 to P6 "need operator rulings, not maker rework" (note N8), and the remediation cap is reached.

Gate 0 as it stands (B01, run 2): blocks A 20, B 3, C 20, D 8, E 15; core 66 of 100; moat 5 of 60; grand total 71 of 160; moats confirmed 1; THIN; AVERAGE. Verifier C recomputed_gate0 gives the same figures. Verifier C recomputed_emoat: 10.8, NONE.

## CRITICAL

| # | Verifier | Location anchor | Finding (as the verifier wrote it, shortened) | Source fidelity | Disposition |
|---|---|---|---|---|---|
| 1 | C (P1), phase 3 | 11-valuation.md l.683 to 690; B11 FLAG-4G-ROCE; deliberation l.140 | Rule V-49 (Master 4G l.897). Stated: governing Track 1 16.1x, Track 2 20.3x; 4G FAIL reported, approved base kept. Recomputed: revise downward on FY29 ROCE 17.72%: base 16.4x, Track 2 18.4x, Track 1 14.4x; Year 3 base FV about Rs 398; entry about Rs 181 to 204; FV today about Rs 284. Effect: minus 1.7x Track 1; decision of record unchanged (AVOID); not a maker error; operator ruling before /finalize; separating observation Kutch approval by 31-Mar-2027. | n/a | Open operator ruling |
| 2 | C (P2), phase 3 | 11-valuation.md l.209, l.213, l.451; deliberation l.61, l.127 | Rule V-09 (Master l.617; v3.10 l.79; chunk 03 l.18, l.51). Stated: 3a +2x on order book 2.76x and capex embedded growth 22.5%; SHARED CATALYST 2. Recomputed: order book already in base revenue at 100%; capex embedded growth 12.6% on TTM revenue; 3a +0x; Track 2 18.3x; Track 2 base FV about Rs 504. Effect: minus 2.0x Track 2; Track 1 governs, decision and entry zone unchanged; Track 2 FVs and 26% divergence overstated; operator re-ruling on 3a. | n/a | Open operator ruling |

Verifier A, Verifier B and Verifier D logged no CRITICAL. The orchestrator identity check had no Verifier A CRITICAL row to test.

## MAJOR

| # | Verifier | Location anchor | Finding (as the verifier wrote it, shortened) | Source fidelity | Disposition |
|---|---|---|---|---|---|
| 3 | A | 01-gate0.md Block C line C1 (line 74); repeated in M1 (line 113) and M11 (line 123) | Claimed revenue CAGR FY23 to FY26 177.1%. Source truth 77.1%: SC Data_Sheet FY23 sales 25.78; Prospectus p.173 FY26 revenue 14,326.69 lakh = 143.2669 Cr; 143.2669/25.78 = 5.557, cube root 1.771. Score line C1 stays 5; printed value wrong by 100pp. | true | GATE HELD. Corrected at source in cycle 1: C1, M1, M11 and data_notes now 77.1%. No verifier re-check. Phase 3 stages carry 77.1% |
| 4 | A | 01-gate0.md Block C line C4 (line 77); flows to Core 61, Block C 15, Grand 68 | Claimed C4 = 91.9 minus 177.1 = minus 85.2pp, score 0. Source truth C4 = +14.8pp, score 5; Block C 20; Core 66; Grand 73. Classification unchanged. 07-emoat.md section 6C repeats Core 61 and Grand 68. | true | GATE HELD. Corrected at source in cycle 1: C4 5, Block C 20, core 66, grand total 71 (71, not 73, because Verifier C F2 also took M11 from 3 to 1). No verifier re-check |
| 5 | A | 04-bizmodel.md section 3D unit economics table, FY26 column, material cost 21.6 (anchor H1 Res. p.4) | Claimed 21.6 lakh per tower. Source truth 19.85 on the cited page: cost of materials 4,372.06 less inventory change 203.30 = 4,168.76 lakh / 210 towers (AFS p.17 prints the same). 21.6 is the Prospectus restated basis (4,528.28 / 210, Pros p.173). Column did not foot. | true | GATE HELD. Corrected at source in cycle 1: 19.9 on the audited basis, restated 21.6 named in a basis note. No verifier re-check |
| 6 | B | B05 2A row 4; promise_delivery row 4; peer_questions item 5 | Kutch promise scored Partial; evidence reads MISSED or REGRESSED. B05 did not use the Prospectus statement that Kutch supplied 16 towers (Rs 877.74 lakh) in March 2026 or the 4,822.20 MT March output. Evidence: Pros p.232; List p.9; PR(11-06) p.3; Pres p.18, p.23. | n/a | Accepted in cycle 1: row moved to Missed; FLAG-KUTCH-CONTRADICTION added (HIGH) |
| 7 | B | B05 2A row 1; promise_delivery row 1 | CARE "Deviation: Yes" scored Delivered; omits "all utilisation as per offer document: No", Rs 2 Cr of the debt object to working capital borrowings, Rs 0.04 Cr excess to the promoter selling shareholder, and the clash with results note 10. Evidence: MA p.3, p.4, p.6; H1 p.5 to 6; Pros p.6. | n/a | Accepted in part in cycle 1: row moved to Partial; FLAG-IPO-USE-CARE added at MEDIUM. Maker holds that the Rs 2 Cr may sit inside the object (Pros p.74). Weighting disputed; open item |
| 8 | B | B05 2A row 5; timeline_slippages | Order book slip under weighted: at least 182 of 225 towers (81%) due by 2026-12-31 open at 2026-10-31; one tower past its 2026-09-30 date. Evidence: Pros p.114; Pres p.18, p.21. | n/a | Accepted in cycle 1: slip quantified, FLAG-ORDERBOOK-SLIP added; row kept Partial until the 31-Dec-2026 dates pass |
| 9 | C (F1), phase 1 | 01-gate0.md l.74, l.77; B01 blocks.C, core_score, grand_total | Rules G0-06, G0-20. Stated revenue CAGR 177.1%, C4 minus 85.2pp = 0, Block C 15, core 61, grand total 68. Recomputed 77.1%, +14.8pp = 5, Block C 20, core 66, grand total 73 (71 with F2). Classification unchanged AVERAGE. | n/a | Corrected in cycle 1 (same fix as rows 3 and 4) |
| 10 | C (F2), phase 1 | 01-gate0.md l.123, l.135; B01 moat_score, moats_confirmed, moat_class | Rule G0-40. Stated M11 3, moats 2, MODERATE, moat score 7. Recomputed M11 1 under the fewer than 6 years clause; moats 1; THIN; moat score 5. | n/a | Corrected in cycle 1; reading of 3 shown as a sensitivity |
| 11 | C (P3), phase 3 | 11-valuation.md l.155 to 159, l.270; deliberation l.44 to 47, l.61 to 62 | Rule V-17 (chunk 01 l.23; FTTCP l.437). Stated: Pillar 1 21.61% midpoint under FIRING. Recomputed: current ROCE 23.45%: 19.2x / 21.2x / 16.9x. Effect: within tolerance; operator override, flagged; composite uses FIRING, Pillar 1 uses the RECOVERING midpoint; moot if P1 ruled. | n/a | Open operator ruling |
| 12 | C (P4), phase 3 | deliberation l.64 to 71; 11-valuation.md l.163 to 184, l.479, l.655 | Rule V-39 (one improvement, one mechanism). Stated: approved FY28 ROCE 19.76% on 277 towers. Recomputed: 277 holds 30 of the 60 JSW pull towers as a level while T3 and FV today credit JSW; own 247 tower base: 20.54%, 17.8x / 19.8x / 15.7x. Effect: minus 0.4x Track 1; deliberation applied the count once rule to Kutch, not JSW; subsumed if P1 ruled. | n/a | Open operator ruling |
| 13 | C (P5), phase 3 | expectation-ledger.md l.21 to 22, l.47 to 48; 11-valuation.md l.630 to 631; 14-thesis.md l.550 | Rules V-41, R2-15 (A22 v3.9 l.79). Stated: D1 0.35, D2 0.30 (proposals); starter FAILS; "fails either way". Recomputed: starter passes at Rs 381 if downside netting is Rs 0.76 Cr PAT or less (D1 p 0.17 or less with D2 struck): T1 + T2 75.0%, residual 7.9%. Effect: A25 starter rests on unruled inputs; decision of record unchanged (AVOID on Gate 0 and U/D); operator to rule D1/D2. | n/a | Open operator ruling |
| 14 | C (P6), phase 3 | 11-valuation.md l.734; B11 decision; 14-thesis.md l.505 to 521 | Rule V-54 (Master l.1129, l.947). Stated: WATCHLIST, hard watch; starter band at Rs 339 or lower. Recomputed: AVOID: U/D 0.26x at Rs 381, 0.52x at Rs 339, 2x at about Rs 241; Gate 0 AVERAGE. Effect: B14 applies AVOID; B13 must carry AVOID with WATCHLIST as operator ruling 7; action unchanged. | n/a | Applied in this synthesis: AVOID carried as the decision of record, WATCHLIST as open ruling 7 |

## MINOR

| # | Verifier | Location anchor | Finding (as the verifier wrote it, shortened) | Source fidelity | Disposition |
|---|---|---|---|---|---|
| 15 | A | 01-gate0.md Block E line E1 (line 101): "PR p.66 post-IPO 65.26%" | Value 65.26% correct; it prints on Prospectus p.68, not p.66. Primary anchor is the 2026-09-30 XBRL. | true | GATE HELD. Anchor corrected to Prospectus p.68 in cycle 1. No verifier re-check |
| 16 | A | 07-emoat.md section 6C "Gate 0 core score = 61 of 140 core points" | Wrong denominator in a report to report carry. Gate 0 prints Core 61 / 100 and Grand 68 / 160. | false | Stands. Stage 7 outside the cycle. B01 governs |
| 17 | A | 05-concall.md section 1C order book row (line 69): "Rs 359.81 Cr, 379 towers" | Pros p.114 prints 35,981.72 lakh = Rs 359.82 Cr. Rounding slip. | false | Corrected to 359.82 in cycle 1 |
| 18 | A | 02-notes.md section P2 (line 52): "funded by debt 7,313.88" in an audited basis paragraph (AFS p.15) | AFS p.15 shows 5,973.82 + 1,367.30 = 7,341.12; 7,313.88 is the restated figure (Pros p.174). FCF 8,053.92 unaffected. | false | Stands. Stage 2 outside the cycle |
| 19 | A | 01-gate0.md header (line 5) and input_gaps: "audited statements file is blank on all 103 pages" | The file carries OCR text on all 103 pages; Gate 0 figures were correct and labelled. Not a number finding. | false | Corrected in cycle 1 |
| 20 | B | B05 2A reproduction check; FLAG-METRIC-REFRAME; input_gaps | Overstated: Rs 32.82 lakh reproduces as cash flow operating profit before working capital changes 3,511.65 lakh / 107 towers (FY26 base 28.58 lakh, +14.8%); withdraw "implies 109.9 towers"; the defect is the EBITDA label. Evidence: H1 p.8; PR(11-06) p.2. | n/a | Accepted in cycle 1 in stages 4 and 5 |
| 21 | B | B05 FLAG-FIRST-GUIDANCE | Overstated: first guidance issued with a results print is routine. Evidence: PR(11-06) p.2. | n/a | Flag dropped in cycle 1; kept as a LOW line |
| 22 | B | B06 FLAG-WC-ABOVE-PEERS | Overstated: CRISIL gross current asset days (292) compared with peer net cycles; Anawil net working capital about 178 days at Mar-26 (derived), inside the 86 to 210 day peer range. Evidence: CRISIL p.2; INOX Q3FY26 p.7; H1 p.4, p.7. | n/a | Stands. Stage 6 outside the cycle |
| 23 | B | B06 Q3, Q9, flags, coverage map | Anchor error: Inox South India tower plant quote is on INOX Q2FY26 [page 4], not [page 3]. | n/a | Stands. Same point as row 39 |
| 24 | B | B05 (absent) | Missed: CS and Compliance Officer exit with three reasons and a 30 day letter to disclosure gap. Evidence: Ann 2026-10-31 letter p.1; Ann 2026-10-31 p.1, p.3. | n/a | Added in cycle 1 as FLAG-KMP-EXIT (LOW) |
| 25 | B | B05 (absent) | Missed: no forward looking statement undertaking followed by forward looking margin statements. Evidence: Ann 2026-09-21 p.1; Ann 2026-09-24 p.1; Ann 2026-10-05 p.2. | n/a | Added in cycle 1 as a LOW red flag |
| 26 | B | B06 (absent) | Missed: "4XM" order book line likely ties Inox as a small customer that is insourcing towers [INFERENCE]. Evidence: Pres p.21; INOX Q1FY27 p.4. | n/a | B06 unchanged; stage 5 added the 4XM line to its report |
| 27 | B | B05 1C LOI row; 2A row 2 | Under weighted: Q1 FY27 LOI absent from Prospectus post balance sheet events, then used to market the listing four days later. Evidence: Pros p.236 to 237; List p.2, p.8; CRISIL p.1. | n/a | Added in cycle 1; row stays Delivered |
| 28 | B | B05 2A row 5 | Under weighted: derived inflow of 48 towers equals the two announced orders (38 + 10), so firm inflow outside them is about zero for seven months. Evidence: Pros p.114; Order(09-10) p.2; Ann 2026-10-29 p.2; Pres p.21. | n/a | Added in cycle 1 |
| 29 | B | B05 2C consistency; 3D | Under weighted: deck placeholder "Text", ROE 57% against RONW 40.92% unlabelled, counterparty names withheld on the two orders that make 48.6% of the book. Evidence: Pres p.7, p.21, p.25; List p.15. | n/a | Added to FLAG-CONSISTENCY in cycle 1 |
| 30 | B | B06 2B | Under weighted: Suzlon FY27 EBITDA guidance cut from about 17% to 15% plus 1% on mix not named. Evidence: SUZ Q2FY27 p.9 to 10. | n/a | Stands. Stage 6 outside the cycle |
| 31 | B | B05 2A, 2C | Under weighted: no sequential comparison (H2 FY26 to H1 FY27 PAT down 57%; EBITDA per tower 34.5 to 33.7 lakh on P&L basis); completeness only. Evidence: H1 p.4; Pres p.18. | n/a | Added in cycle 1 as a completeness note |
| 32 | C (F3), phase 1 | 01-gate0.md l.81, l.95, l.101, l.103 | Rule G0-25. Block D on 31-Mar-2026 and E1/E3 on 30-Sep-2026. Block D 15 on the Sep-26 basis; core 73 with F1. If latest = Sep-26, Block D and B07 G1 credit the same IPO deleveraging. | n/a | RULED 2026-11-15: Block D date 31-Mar-2026 (handover dossier Section 7 ruling 3) |
| 33 | C (F4), phase 1 | 01-gate0.md l.106, l.157 to 188 | Rule G0-51. Embedded YAML abbreviated; text after the block. B01-gate0.yaml is the copy of record. Presentational. | n/a | Fixed in cycle 1 |
| 34 | C (F5), phase 1 | 01-gate0.md l.40, l.148 | Rule G0-08 (observation). FY23 ROCE NOT FOUND; floor 11.88% from EBIT 9.61 / TA 80.90; Block A floor 15; recomputed core floor 61 (60 with filed CFO). | n/a | Tested in cycle 1; AVERAGE holds at the floor |
| 35 | C (F6), phase 1 | 07-emoat.md l.188, l.218, l.225 to 234 | Rule EM-21. R1 scored 0.7 on claim only evidence, no optionality register row. EM NONE unchanged; E1 to 2.0 path reaches 11.4, not 12.1, without R1. | n/a | Stands. Stage 7 outside the cycle |
| 36 | C (F7), phase 1 | 07-emoat.md l.104, l.179 | Rule EM-02. Meet Outcome 2026-10-05 tagged DOC; it is a management claim. No score change. | n/a | Stands |
| 37 | C (F8), phase 1 | 07-emoat.md l.175; B07 completionist_recount | Rule EM-10. Recount text names 6 claim categories as 5; B1 documented item is the unattributed CWIP rise; count unchanged. | n/a | Stands |
| 38 | C (F9), phase 1 | 07-emoat.md l.261 to 263; B07 combined_reasoning | Rule EM-24. States core 61 of 140, grand total 68, MODERATE. Recomputed core maximum 100; core 66, grand total 71, THIN. Combined AVERAGE unchanged. | n/a | Stands. B01 governs |
| 39 | D | 06-peers.md Q3, 2D, flags, risks | Page anchor error: Inox Q2 FY26 South India blade and tower plant is on [page 4] (file line 110), cited as [page 3]. Quote and fact confirmed. | n/a | Stands |
| 40 | D | 06-peers.md Q4, 2B, coverage map | Page anchor error: Suzlon Q1 FY27 ASP Rs 6.3 Cr is on [page 4] (file lines 118 to 119), cited as [page 3]. Fact confirmed. | n/a | Stands |
| 41 | D | 06-peers.md Q7 | Q7 headlined VERIFIED although the first half of the claim (who buys the plate) is UNVERIFIABLE; PARTIALLY VERIFIED would match. Pass through has 3 independent peers. | n/a | Stands |
| 42 | D | 06-peers.md Q1 | Q1 VERIFIED while the 80% top of Anawil's 70 to 80% sits above every peer figure (peer max 75%). Disclosed in the net read and FLAG-H2-RANGE-TOP; the headline verdict does not carry it. | n/a | Stands |
| 43 | C (P7), phase 3 | 11-valuation.md l.240 to 249 | Rule V-26 (v3.3 A6 l.95). Stated 18.8 to 21.8x; 14.9 to 17.3x. Recomputed 19.0 to 22.0x; 15.0 to 17.5x; Track 1 bear about Rs 140.8, bull about Rs 717.5, width about 130%. No decision change. | n/a | Open (A6 rounding ruling) |
| 44 | C (P8), phase 3 | 11-valuation.md l.246, l.755 | Rule V-27 (chunk 15 l.36, l.38). Durability adj 0, Unproven band, no basis; 12C leaves the short record unpriced at 0; no second reading named. Operator-approved r 14.5% stands. | n/a | Open |
| 45 | C (P9), phase 3 | 11-valuation.md l.471; deliberation l.33 to 36 | Rule V-36 (v3.9 A21 l.67 to 70). A21 base is the FY27 forward scenario PAT 43.33; trailing two halves 48.09 gives T1 81.3%; T1 + T2 74.9% without D3, 67.0% with D3. Starter fails on every combination; operator-ruled. | n/a | Stands (operator Ruling 1) |
| 46 | C (P10), phase 3 | 11-valuation.md l.345 to 347, l.477; expectation-ledger.md l.17 | Rule V-40 (single credit). EN-182 slice +3.6 Cr PAT on top of a base FY28 that already assumes new orders at a pace set by the first EN-182 order; overlap up to Rs 23.2 a share of Year 3 base, about 5% of base FV; state the split. | n/a | Open |
| 47 | C (P11), phase 3 | 11-valuation.md l.403 to 405 | Rule V-15 (A17.3). Bear FY28 Rs 25.6 lakh a tower stand-in; 5 year median spread NOT FOUND; stand-in uses an "about 22" point and mixed contract models. Bear FY28 row only; Year 3 bear FV unchanged. | n/a | Open |
| 48 | C (P12), phase 3 | 11-valuation.md l.294 to 303, l.729 | Rule V-52 (MIA l.30; chunk 14 l.19). PRICED-WE-ARE-LATE on the 16.1x reading; protocol reading 2 at the 25x cap: price implies 9.7% against 17.3% evidence, OPPORTUNITY. Both readings in 1B.12; card carries one; flag never sets the verdict. | n/a | Stands; both readings carried |
| 49 | C (P13), phase 3 | expectation-ledger.md l.18; 11-valuation.md l.478 | Rule V-67 (A23). Row 2 credits 58 towers a year; confirms on Rs 8.78 Cr a half = 16 towers, about 55% of the credited volume; sized threshold about Rs 16 Cr a half. Not a rule 13 REWORK condition. | n/a | Open |
| 50 | C (P14), check 15 | chunk 06 l.92; Master l.897 | Rule C-06. Chunk says "revise the exit PE and recalculate"; Master says "revise the exit PE downward and recalculate". No B11 value changes; fix the chunk. | n/a | Framework follow-up, outside this run |
| 51 | C (P15), check 15 | Master l.296; FTTCP l.288, l.433, l.438; chunk 01 l.24 | Rule C-01. Master: RECOVERING-to-FIRING (probability above 60%) gives midpoint; FTTCP and chunk: RECOVERING, probability above 60% with Strong catalysts gives midpoint; hybrid banned. No B11 value changes; fix Master l.296 on a framework branch. | n/a | Framework follow-up, outside this run |
| 52 | C (P16), Role 2 | B14-thesis.yaml l.8; 14-thesis.md l.484 to 485 | Rule R2-16 (Master l.1158). position_size Small under verdict AVOID; recomputed zero (ceiling Small). Presentational; avoids a Small position being read downstream. | n/a | Applied in this synthesis: position today zero, Small is a ceiling |

Verifier C also lists R2-15 (B14 says the starter fails either way; D1 is also unruled; MINOR, with P5) inside its valuation fails. It is counted with P5 above.

## Verifier A source fidelity dispositions

| Number or claim | Verifier A verdict and anchor | Downstream position | Disposition |
|---|---|---|---|
| Revenue CAGR 177.1% (01-gate0.md C1, M1, M11) | MAJOR, source_fidelity true; truth 77.1% (SC Data_Sheet; Pros p.173) | Maker agreed; phase 3 stages use 77.1% | GATE HELD, corrected at source in cycle 1 |
| C4 minus 85.2pp; core 61; grand 68 (01-gate0.md C4 and totals) | MAJOR, source_fidelity true; truth +14.8pp, score 5 | Maker agreed; Verifier C F2 also moved M11 | GATE HELD, corrected at source in cycle 1 (core 66, grand total 71) |
| FY26 material cost 21.6 lakh per tower (04-bizmodel.md 3D) | MAJOR, source_fidelity true; truth 19.85 (H1 Res. p.4; AFS p.17) | Maker agreed | GATE HELD, corrected at source in cycle 1 (19.9, basis labelled) |
| Prospectus p.66 anchor for 65.26% (01-gate0.md E1) | MINOR, source_fidelity true; number on Pros p.68 | Maker agreed | GATE HELD, anchor corrected in cycle 1 |

No downstream step cleared, downgraded or reasoned around a Verifier A source fidelity finding. No verifier re-checked the corrections.

## Other verifier statements

- Verifier A struck 3 rows before emit: Gate 0 computed ROCE 26.79/26.25/16.39 against Prospectus printed 23.05/21.84/13.68 (basis labelled in Gate 0); "PRES p.27" (deck slide 27 = file page 28); Pros Annexure N not due 3,841.82 against AFS 3,841.81.
- Verifier A NOT CHECKED: stage 9 web sourced figures, stage 8 web and aggregator items, most peer transcript quotes beyond ten spot checks (all ten matched), the remaining stage 2 and 3 AFS note cells.
- Verifier B credibility: "concur: C holds on the delivery record (re-scored 3 delivered, 2 partial, 1 missed) but sits at its floor". Verifier B pipeline_flags_not_supported: none.
- Verifier D: substantive_unsupported none; unused_but_relevant none.
- Verifier C phase 3 recomputed destination PE: "approved (governing): Track 1 16.1x (14.9-17.3x), Track 2 20.3x (18.8-21.8x); framework as written: Track 1 14.4x (13.5-15.5x) on the 4G Year-3 revision (P1), Track 2 16.4x (15.0-17.5x) with 3a +0x (P1, P2); Pillar 1 FIRING rule alone 19.2x/21.2x/16.9x (P3); A18.0 haircut not applied (judgment, would be -1.0x)".
- Verifier C phase 3 recomputed decision: "concur AVOID (B14; Master l.1129: Gate 0 AVERAGE and U/D 0.26x); no position on every reading; B11 WATCHLIST label and Rs 339 starter band do not follow the AVOID rule (P6); Track 1 entry zone about Rs 181-204 on the 4G reading vs Rs 202-227 approved".
- Verifier C expectation ledger: present, downside row present, every row has a confirm-by date and a metric threshold, probabilities in range, decay status valid, no off ledger credit, residual 16.0% of CMP, starter cap OK; 8 of 8 gates pass.
- Verifier C phase 3 notes (not scored): N1 template defect at prompts/12-verifiers-pipeline.md line 379, carried from phase 1. N2 B11 expected_cagr_prob_weighted 17.3 is the EPS CAGR; the expected price return at Rs 381 is minus 3.0% (Track 1) and 4.7% (Track 2). N3 Pillar 2 is the largest single swing (Track 1 16.1x against 10.5x on the structural 0.65x row). N4 Amendment 14 upward reading: FY30 EPS about Rs 30.56 against base Rs 26.16; base treated as compliant. N5 Route A on the 30-Sep-2026 balance sheet could read about 23.9% if the capital advances stayed near Rs 30.04 Cr, which would open Route A. N6 the A18.0 haircut names no separating observation; candidate: FY29 tower order intake against the wind roadmap at the H1 FY28 print. N7 on bear-consistent pillars (Track 1 11.1x) the bear FV would be about Rs 103 and upside/downside about 0.22x. N8 no REWORK trigger fires; P1 to P6 need operator rulings.
- Verifier C rule 9 (business understanding narrative): NOT ASSESSED, because B13 was not produced when Verifier C ran.
