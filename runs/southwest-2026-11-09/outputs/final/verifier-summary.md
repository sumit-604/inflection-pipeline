# Verifier summary: SOUTHWEST, phase 1, run 2026-11-09

## Confidence delta

| Component | Score | Note |
|---|---|---|
| Numerical acceptance (Verifier A) | 98 | |
| Red flag coverage (Verifier B) | 86.4 | |
| Framework adherence (Verifier C) | 90.3 | Gate 0 + Emerging Moat only; valuation adherence pending phase 3 |
| Peer utilisation (Verifier D) | 83.3 | 10 substantive of 12 peer transcripts |
| **Overall** | **83.3** | Set by peer utilisation; band 75-89, normal, note specifics |

Rework: does not fire. OR-29: no CONFIRMED Verifier A CRITICAL; acceptance rates 98, 86.4, 90.3, 100 all >= 60 on denominators >= 4. B12b CRITICAL and B12c CRITICAL are not REWORK triggers. Remediation cycles: 0.

## Acceptance rates and counts

| Verifier | Acceptance | CRITICAL | MAJOR | MINOR | Coverage |
|---|---|---|---|---|---|
| A (numerical) | 98 | 0 | 4 | 4 | 375 numbers checked; mandatory 170 of 170; material universe 500; false positives struck 8 |
| B (red flag) | 86.4 | 1 | 8 | 8 | 22 material of 47 listed; 15 caught, 4 partially caught, 3 missed; strict rate 68.2% (15/22); 15 of 15 transcripts read in full |
| C (framework, Gate 0 + EM) | 90.3 | 1 | 2 | 11 | Gate 0 64 rules; Emerging Moat 60 rules; valuation 0 rules, pending phase 3 |
| D (peer) | 100 | 0 | 1 | 1 | 12 peers audited; 10 substantive confirmed |

SF = Verifier A source_fidelity. Rows marked yes state the source value only; the source value governs every downstream use.

## CRITICAL

| Verifier | Location | Note | SF |
|---|---|---|---|
| B | B05 2E, repeated_evasions | Phasing asked and refused on all three calls; peers answer the same question. Rule 5, missed repeated evasion; forward revenue basis depends on book burn. | |
| C | B01 E1, 01-gate0.md L50 | Prompt 01 rule 5. E1 = 5 on 68.85% at 31 Mar 2026 with latest-quarter pattern NOT FOUND; recomputed E1 = 0, Block E 3, core 57, AVERAGE. E3 scored 0 on the same empty folder. Second reading: dated quarter-end is the latest available, GOOD stands. Separator: Sep 2026 shareholding pattern; GOOD stands at 40% or above. | |

## MAJOR

| Verifier | Location | Note | SF |
|---|---|---|---|
| A | 09-tam.md Section 3B cross-check line and Section 5B runway | Screener Sales row: FY22 117.73, FY23 124.26, FY26 243.02. FY23 to FY26 CAGR = (243.02 / 124.26)^(1/3) - 1 = 25.1%, agrees with 01-gate0.md M11. 117.73 is the FY22 cell. Saturation years recompute to about 10.9 on the 1.251 ratio. No verdict-card or Section 1B pillar input is touched. | yes |
| A | 04-bizmodel.md Section 4D question 4 (receivables vs revenue growth) | Standalone revenue 24,292.95 less 17,919.32 = 6,373.63 L (Results_Q2FY27 p.5 col Mar-26; AR26 S p.114). Consolidated 24,302.17 less 18,029.50 = 6,272.67 L (AR26 C p.167). Receivable figure 4,456.25 L beside it ties (AR26 S p.115). | yes |
| A | 03-ardeep.md Phase 2-V rank 10 and B03 yaml triple_pass_verification.discrepancies rank 10 | Related-party exposure 855.35 reproduces exactly: loans 668.20 (257.86 + 410.34; AR26 S Note 48/49, [page 148-149]) + Other Receivables 56.91 (AR26 S Note 16, [page 132]) + debtors 130.24 (AR26 S Note 48, [page 148]); 855.35 / 20,251.42 = 4.22%. B02 pass 2 P2-2 shows this build. B03 verified count reads 13 of 15 on this row. | yes |
| A | 03-ardeep.md Phase 2-V rank 11 and B03 yaml triple_pass_verification.discrepancies rank 11 | Plant depreciation for the year 780.24 (FY25) to 930.74 (FY26) = +150.50 (AR26 S Note 2, near [page 127]). Total depreciation +184.48 is a different basis (1,144.33 vs 959.85). B03 verified count reads 14 of 15 once ranks 10 and 11 are cleared. | yes |
| B | B05 1B, 1C | FY28-29 needs plan approval by about March 2027; plan not started in July. Inference; sets within-hold or beyond-hold for coal. | |
| B | B05 3D, FLAG-CONCENTRATION, trigger 4 | Deck CBM Rs 222.2 Cr; two anchors 529.2/761.3 = 69.5%; ex-both Rs 232.1 Cr. Derivation basis, not source fidelity; four of five segment lines show no Q1 burn; ask for a book roll. | |
| B | B05 2E | Per-rig capex refused on two calls. Partially caught; add to repeated_evasions. | |
| B | B05 2E | Drilling competitors asked and unnamed on three calls. Partially caught; add to repeated_evasions. | |
| B | B05 1C, 4D, YAML guidance | FY27 about 20% asked twice in July; not reaffirmed. Partially caught; state that July did not reaffirm. | |
| B | B05 4D | 'Consistent returns' against no dividend and a stabilisation loan. Partially caught; JV share is 16.7% of H1 FY27 PAT. | |
| B | B05 2A row 14 | Q1 FY27 [p.5] 'was also received'; past tense. Delivered 8 to 7, scored 15 to 14. | |
| B | B05 2B, 4D, FLAG-MARGIN-EXPLANATION; B06 Q2, 2B | Direct cost flat only year on year, with materials +16.0 points netted against other operating -15.9; sequentially materials +5.4 points, employee +4.6; diesel sits in materials. OVERSTATED; numbers correct, basis is the issue; employee cost rise stands. | |
| C | B01 M11, 01-gate0.md L69 | Prompt 01 M11 tier 2. M11 = 3 on FY23-26 CAGR 25.1%; recomputed M11 = 0, moats present 2, MODERATE, moat score 7, grand total 69 alone, 64 with F1. M1 and C1 read revenue CAGR at 14.1%. Second reading: tier 2 inherits tier 1 window, score 3. Separator: operator clarification of the term. | |
| C | B07 C1 L81, E1 L88, R1 L158, total L186 | Prompt 12 Verifier C rule 3; Prompt 07 Section 5. 12.8 MODEST stated; recomputed 11.3 NONE at 0.7x on all three, 13.4 MODEST at 1.0x on all three, 11.9 NONE on C1 alone. EM >= 25 UA qualifier unmet on every reading. FLAG-THRESHOLD-SENSITIVE omits the multiplier. | |
| D | B06 Q10; JINDRILL Aug 2026 p.3 line 93 | Q10 VERIFIED on a single peer; B06 argues four calls and two speakers meet the two-peer rule, but they are one company, not independent peers. | |

## MINOR

| Verifier | Location | Note | SF |
|---|---|---|---|
| A | 01-gate0.md Block E, E2 (and B01 data_notes) | The two printed lines sum to -4.34. Total promoter-group holding moved 73.61% to 68.85% = -4.76pp (AR25 promoter table, line 6936; AR26 [page 133] FY25 column). Headline omits the group-wide figure. E2 score (0) unchanged. | no |
| A | 01-gate0.md Load-bearing fact 1 (standalone Q2 FY27 margin) | (5,750.03 - 4,949.32) / 5,750.03 = 13.925%, rounds to 13.93%. Truncation, 0.01pp. Derived value. | no |
| A | 01-gate0.md Block F, M11 (prior 3-yr CAGR) | (124.26 / 85.80)^(1/3) - 1 = 13.14%, rounds to 13.1%. Rounding, 0.1pp. Latest 25.1% ties. Tier unchanged. | no |
| A | 02-notes.md rank 9; 02-notes-pass2.md P2-7; B02 yaml rank 9 | 61.2% = 1,390.57 / 2,273.57 non-fund limits. On bank guarantees 2,250.07 the ratio is 61.8% (AR26 Note 14 S [page 131], Note 9 S [page 130], Note 42 C [page 185]). Basis label wrong, not the arithmetic. | no |
| B | B05 4B Q6, 4D | Rig delivery: fleet count unreconciled; same-rig slip not shown. OVERSTATED. | |
| B | B06 contradicted, 2A | CHP civil work in the quarter SOUTHWEST grew 128%. OVERSTATED; work-type split. | |
| B | B06 Part 4, FLAG-Q2-CAUSE-UNSUPPORTED | One peer has a Q2 FY27 call; DEEPINDS says it has no seasonality. OVERSTATED. | |
| B | B06 Q1, Part 4 | JINDRILL global rates USD 80-90k to above 100k; B06 grades the item low weight elsewhere. OVERSTATED; supported for India only. | |
| B | B05 throughout | Later anchors in each call run one page high. Verifier A owns anchors. | |
| B | B05 2E-6, 2A counts sentence | YAML says deflected every time; counts sentence garbled. Internal inconsistency. | |
| B | B05 2A rows 1, 2 | Both locked in when said. Low information. | |
| B | B05, B06 | 12 missed and 5 partially caught minor items: items 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 41, 43, 44, 45. | |
| C | B01 M8, L66 | Prompt 01 M8. None quantified, 0; recomputed 0 or 1. State which tier applies. | |
| C | B01 L17, L18, L28, L32, L56, L61, L69 | Prompt 01 rule 4. Figures without page or source: AR FY25 pages and moat inputs. | |
| C | B01 output | Prompt 01 Output. Moat profile bars absent. Presentational. | |
| C | B01 L75, data_years | Prompt 01 data confidence. Text passes. 6 of 20 core metrics rest on 3 years. Rule silent on mixed coverage. If keyed to 3 years, GOOD downgrades to AVERAGE. Operator ruling closes it. | |
| C | B01 analyst_note, L128 | Consistency with E2 basis. Stated 'not to evidence of a problem'; E2 scores 0 on an observed fall above 3pp (L51). | |
| C | B01 M2, M5, M9, L95, L123 | Prompt 01 Block F peer rule. PEER DATA NEEDED, 0; recomputed not determinable. input_gaps record Data_Sheet populated for peers. Separator: stage 1 dispatch input list. | |
| C | B07 I2, L106 | Prompt 07 I2 each moat. Answered for C1, B2, E1; A1, G1, H2, R1 not answered. Score stays 0. | |
| C | B07 YAML L287-L294 | Prompt 07 Optionality Register. 7 of 9 rows in block. Mineral block auctions and HZL ramp dropped. | |
| C | B07 L150-L153, L155 | Prompt 07 rule 2. Five items untagged, Section 4B policy rows. | |
| C | B07 L16, L21, L29, L47, L71, L76, L92 | Prompt 07 rule 3. Placeholder or secondary anchors; AR p.? at L71. | |
| C | B07 L135, L277 | Prompt 07 evidence_mix item counts. Stated 12 / 11 / 3; recomputed claim tags 24, inference tags 1. Claim and inference counts do not reproduce from the body. | |
| D | JINDRILL-Concall_Aug_2026 lines 361-367 | Q1 omits JINDRILL Q1 FY27 management expectation that day rates will improve (direction consistent with the contradiction, but a counter-quote left out). | |

## Verifier B missed items

Items Verifier B found independently that the pipeline did not catch. The CRITICAL and two MAJOR rows repeat findings above.

| Severity | Item | Anchor |
|---|---|---|
| CRITICAL | Order-book execution phasing refused on all three calls, to three analysts; not in B05 2E or repeated_evasions | Q2 FY26 Ankur Kumar, Piyush Jain [p.12]; Q4 FY26 Maitri Shah, Vikas Jain [p.6]; Q1 FY27 Raman KV, Piyush Jain [p.6] |
| MAJOR | Coal production FY28-29 has no slack on management's own two-year lead from mining plan approval | Q4 FY26 Vikas Jain [p.13]; Q1 FY27 Vikas Jain [p.7], [p.8] |
| MAJOR | Order-book composition does not reconcile: CBM Rs 222 Cr equals extension plus Rs 55 Cr, CMD denies; 62% should be 69.5%; four of five segment lines show no Q1 burn | Q1 FY27 Rahul, Vikas Jain [p.14]; Piyush Jain [p.6]; Vikas Jain [p.9]; decks filed 20260505 [page 18], 20260721 [page 17] |
| MINOR | Debt-free became conditional on no further equipment purchase | Q4 FY26 Vikas Jain [p.13]; Q1 FY27 Vikas Jain [p.18] |
| MINOR | Margin 'contract to contract' against 'not project to project' | Q2 FY26 Vikas Jain [p.17]; Q4 FY26 Vikas Jain [p.6] |
| MINOR | HZL 'as soon as possible' became consistent revenue over four years | Q4 FY26 Vikas Jain [p.6], [p.9]; Q1 FY27 Piyush Jain [p.9] |
| MINOR | CBM 'revenue should increase' became 'same quarterly results' | Q4 FY26 Vikas Jain [p.13]; Q1 FY27 Piyush Jain [p.8], [p.9] |
| MINOR | 'Super cycle' against 'quite cyclical' | Q4 FY26 Vikas Jain [p.17]; Q1 FY27 Vikas Jain [p.8], [p.15] |
| MINOR | Aquifer tender question answered with execution status | Q1 FY27 Rahul, Vikas Jain [p.14] |
| MINOR | Oman contract tenor, value, margin and stake drift; CMD said Yes to analyst figures | Q4 FY26 Vikas Jain [p.5]; Q1 FY27 Vikas Jain [p.6], [p.17] |
| MINOR | 'Owner of the mines' before mining plan or clearances | Q1 FY27 Vikas Jain [p.10]; Q4 FY26 Vikas Jain [p.16] |
| MINOR | CMD and Joint MD differ on what FY26 capex bought | Q4 FY26 Vikas Jain, Piyush Jain [p.12] |
| MINOR | 'Two or three competitors everywhere' against 'only players'; 'competitive market' against 'huge shortage' | Q4 FY26 [p.6], [p.9]; Q1 FY27 [p.16]; Q2 FY26 [p.13] |
| MINOR | Reliance block life asked, rig deployment answered | Q4 FY26 Keshav Garg, Vikas Jain [p.13] |
| MINOR | 'Entry barriers quite high' against two onshore drillers raising IPO capital; analyst statement, low tier | Q1 FY27 Vikas Jain [p.16]; DEEPINDS May 2026 Srikar Sai, Rohan Shah [p.18] |

Verifier B promise spot checks: 5 checked, 4 confirmed, 1 wrong. Credibility grade: lower; B rests on 8-4-3, but row 14 is not a promise and rows 1 and 2 were locked in when said; recount 5-4-3 of 12, and the last two calls score 2-2-2 with both misses on growth and margin; carry as B- with a C bias until Q3 FY27.
