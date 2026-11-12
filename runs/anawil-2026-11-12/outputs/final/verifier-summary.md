=== FILE: verifier-summary.md ===

# Verifier summary, phase 1

Anawil Wire and Engineering Ltd (ANAWIL). Run 2026-11-12. Verifiers A, B and D in full; Verifier C on the Gate 0 and Emerging Moat portion only (valuation audit PENDING PHASE 3).

## Confidence delta (phase 1, computed by the orchestrator)

| Component | Value | Block | Basis |
|---|---|---|---|
| numerical_acceptance | 97 | B12a | 418 numbers checked; mandatory tier 183 of 183 |
| redflag_coverage | 100 | B12b | material_found 7, material_caught 7 (4 caught, 3 partly caught counted as caught) |
| framework_adherence | 88.6 | B12c | 70 of 79 rules (Gate 0 47 of 52, Emerging Moat 23 of 27) |
| peer_utilisation | 100 | B12d | 12 of 12 peers SUBSTANTIVE |
| overall | 88.6 | confidence.yaml | Minimum of the four; set by framework_adherence; band 75 to 89 |

REWORK test on the values as written: not triggered (0 confirmed Verifier A CRITICAL; no acceptance rate below 60 on a denominator of 4 or more).

OPEN OPERATOR RULING (OR-29, carried to Halt 1): Verifier B wrote acceptance_rate 100, counting 3 PARTIALLY CAUGHT material items as caught. Verifier B states: "Strict caught-only reading would be 4 of 7 (57%)." That is below the OR-29 line of 60% on a denominator of 4 or more. It would set overall to 57 and force REWORK. The orchestrator used the value as written and substituted no number. The 3 partly caught items (Kutch promise scoring, IPO proceeds scoring, order book slippage) went into the one remediation cycle on stage 5.

## Acceptance rates and counts

| Verifier | Model | Acceptance | CRITICAL | MAJOR | MINOR | Other |
|---|---|---|---|---|---|---|
| A, numerical | claude-sonnet-5-5 | 97 | 0 | 3 | 5 | 3 false positives struck by Verifier A under its rule 5b; material universe about 600; mandatory 183 of 183 |
| B, red flags | claude-opus-5-5 | 100 (strict reading 57) | 0 | 3 | 12 | 25 independent flags: 12 caught, 10 partly caught, 3 missed (all MINOR); promise spot checks 5, confirmed 4, wrong 1 |
| C, framework (phase 1) | claude-opus-5-5 | 88.6 | 0 | 2 | 7 | Gate 0 52 rules, 5 fails; Emerging Moat 27 rules, 4 fails; valuation 0 rules (PENDING PHASE 3) |
| D, peers | claude-sonnet-5-5 | 100 | 0 | 0 | 4 | 12 peers audited, 12 SUBSTANTIVE; claims_all_addressed true; no verdict discipline fails |

## Run state of these findings

Every finding below describes the run 1 reports. One remediation cycle ran (the cap) on stages 1, 4 and 5. The current 01-gate0.md, 04-bizmodel.md, 05-concall.md and their blocks are the corrected run 2 versions; run 1 copies are kept as *.run1.md and *.run1.yaml. No verifier re-checked the corrected lines: each verifier ran once (manifest verifier_runs A 1, B 1, C 1, D 1). The Disposition column comes from the run log and the makers' remediation notes, not from a verifier.

Gate 0 as it now stands (B01, run 2): blocks A 20, B 3, C 20, D 8, E 15; core 66 of 100; moat 5 of 60; grand total 71 of 160; moats confirmed 1; moat class THIN; classification AVERAGE. Verifier C's recomputed_gate0 gives the same figures.

## CRITICAL

None. Verifier A 0, Verifier B 0, Verifier C 0, Verifier D 0. The orchestrator identity check had no CRITICAL row to test.

## MAJOR

| # | Verifier | Location anchor | Finding (as the verifier wrote it, shortened) | Source fidelity | Disposition |
|---|---|---|---|---|---|
| 1 | A | 01-gate0.md Block C line C1 (line 74); repeated in M1 (line 113) and M11 (line 123) | Claimed revenue CAGR FY23 to FY26 177.1%. Source truth 77.1%: SC Data_Sheet FY23 sales 25.78; Prospectus p.173 FY26 revenue 14,326.69 lakh = 143.2669 Cr; 143.2669/25.78 = 5.557, cube root 1.771. Score line C1 stays 5; printed value wrong by 100pp. | true | GATE HELD. Corrected at source by the maker in cycle 1: C1, M1, M11 and data_notes now 77.1%. No verifier re-check. |
| 2 | A | 01-gate0.md Block C line C4 (line 77); flows to Core 61, Block C 15, Grand 68 (lines 140 to 142 and YAML) | Claimed C4 = 91.9 minus 177.1 = minus 85.2pp, score 0. Source truth C4 = +14.8pp, score 5; Block C 20; Core 66; Grand 73. Classification unchanged. 07-emoat.md section 6C repeats Core 61 and Grand 68. | true | GATE HELD. Corrected at source in cycle 1: C4 5, Block C 20, core 66, grand total 71 (71, not 73, because Verifier C F2 also took M11 from 3 to 1). No verifier re-check. The 07-emoat.md carry stands (stage 7 outside the cycle). |
| 3 | A | 04-bizmodel.md section 3D unit economics table, FY26 column, Material cost 21.6 (anchor H1 Res. p.4) | Claimed 21.6 lakh per tower. Source truth 19.85 on the cited page: cost of materials 4,372.06 less inventory change 203.30 = 4,168.76 lakh / 210 towers (AFS p.17 prints the same). 21.6 is the Prospectus restated basis (4,528.28 / 210, Pros p.173). Column did not foot. | true | GATE HELD. Corrected at source in cycle 1: cell now 19.9 on the audited basis, restated 21.6 named in a basis note, column foots to 68.2. No verifier re-check. |
| 4 | B | B05 2A row 4; promise_delivery row 4; peer_questions item 5 | Kutch promise scored Partial; evidence reads MISSED or REGRESSED. B05 did not use the Prospectus statement that Kutch supplied 16 towers (Rs 877.74 lakh) in March 2026 or the 4,822.20 MT March output. Evidence: Pros p.232; List p.9; PR(11-06) p.3; Pres p.18, p.23. | n/a | Accepted in cycle 1: row moved to Missed; FLAG-KUTCH-CONTRADICTION added (HIGH). Peer question 5 left unchanged. |
| 5 | B | B05 2A row 1; promise_delivery row 1 | CARE "Deviation: Yes" scored Delivered; omits "all utilisation as per offer document: No", Rs 2 Cr of the debt object to working capital borrowings, Rs 0.04 Cr excess to the promoter selling shareholder, and the clash with results note 10. Evidence: MA p.3, p.4, p.6; H1 p.5 to 6; Pros p.6. | n/a | Accepted in part in cycle 1: row moved to Partial; every CARE point added; FLAG-IPO-USE-CARE added at MEDIUM. The maker holds that the Rs 2 Cr may sit inside the object (Pros p.74). Weighting disputed; open item. |
| 6 | B | B05 2A row 5; timeline_slippages | Order book slip under weighted: at least 182 of 225 towers (81%) due by 2026-12-31 open at 2026-10-31; one tower past its 2026-09-30 date. Evidence: Pros p.114; Pres p.18, p.21. | n/a | Accepted in cycle 1: slip quantified, FLAG-ORDERBOOK-SLIP added. Row kept Partial until the 31 Dec 2026 dates pass. |
| 7 | C (F1) | 01-gate0.md l.74, l.77; B01 blocks.C, core_score, grand_total, data_notes, analyst_note | Rules G0-06, G0-20. Stated revenue CAGR 177.1%, C4 minus 85.2pp = 0, Block C 15, core 61, grand total 68. Recomputed 77.1%, +14.8pp = 5, Block C 20, core 66, grand total 73 (71 with F2). Classification unchanged AVERAGE. | n/a | Corrected in cycle 1 (same fix as rows 1 and 2); analyst_note claim on C4 and B4 removed. |
| 8 | C (F2) | 01-gate0.md l.123, l.135; B01 moat_score, moats_confirmed, moat_class | Rule G0-40. Stated M11 3, moats 2, MODERATE, moat score 7. Recomputed M11 1 under the fewer than 6 years clause; moats 1; THIN; moat score 5. B07 6C carries the stale MODERATE. | n/a | Corrected in cycle 1: M11 1, moats 1, THIN, moat score 5; reading of 3 shown as a sensitivity. 07-emoat.md carry stands. |

## MINOR

| # | Verifier | Location anchor | Finding (as the verifier wrote it, shortened) | Source fidelity | Disposition |
|---|---|---|---|---|---|
| 9 | A | 01-gate0.md Block E line E1 (line 101): "PR p.66 post-IPO 65.26%" | Value 65.26% correct; it prints on Prospectus p.68, not p.66. Primary anchor is the 2026-09-30 XBRL. | true | GATE HELD. Anchor corrected to Prospectus p.68 in cycle 1. No verifier re-check. |
| 10 | A | 07-emoat.md section 6C "Gate 0 core score = 61 of 140 core points" | Wrong denominator in a report to report carry. Gate 0 prints Core 61 / 100 and Grand 68 / 160. | false | Stands. Stage 7 outside the cycle. B01 governs (core 66 of 100, grand total 71 of 160). |
| 11 | A | 05-concall.md section 1C order book row (line 69): "Rs 359.81 Cr, 379 towers" | Pros p.114 prints 35,981.72 lakh = Rs 359.82 Cr. Rounding slip. | false | Corrected to 359.82 in cycle 1. |
| 12 | A | 02-notes.md section P2 (line 52): "funded by debt 7,313.88" in an audited basis paragraph (AFS p.15) | AFS p.15 shows 5,973.82 + 1,367.30 = 7,341.12; 7,313.88 is the restated figure (Pros p.174). FCF 8,053.92 unaffected. | false | Stands. Stage 2 outside the cycle; stage 3 had already flagged the 27.24 gap. |
| 13 | A | 01-gate0.md header (line 5) and input_gaps: "audited statements file is blank on all 103 pages" | The file carries OCR text on all 103 pages; Gate 0 figures were correct and labelled. Not a number finding. | false | Corrected in cycle 1 (header, input_gaps, cash section). |
| 14 | B | B05 2A reproduction check; FLAG-METRIC-REFRAME; input_gaps | Overstated: Rs 32.82 lakh reproduces as cash flow operating profit before working capital changes 3,511.65 lakh / 107 towers (FY26 base 28.58 lakh, +14.8%); withdraw "implies 109.9 towers"; the defect is the EBITDA label. Evidence: H1 p.8; PR(11-06) p.2. | n/a | Accepted in cycle 1 in stages 4 and 5: tower count text withdrawn; flags relabelled. |
| 15 | B | B05 FLAG-FIRST-GUIDANCE | Overstated: first guidance issued with a results print is routine. Evidence: PR(11-06) p.2. | n/a | Flag dropped in cycle 1; kept as a LOW line. |
| 16 | B | B06 FLAG-WC-ABOVE-PEERS | Overstated: CRISIL gross current asset days (292) compared with peer net cycles; Anawil net working capital about 178 days at Mar-26 (derived), inside the 86 to 210 day peer range. Evidence: CRISIL p.2; INOX Q3FY26 p.7; H1 p.4, p.7. | n/a | Stands. Stage 6 outside the cycle. |
| 17 | B | B06 Q3, Q9, flags, coverage map | Anchor error: Inox South India tower plant quote is on INOX Q2FY26 [page 4], not [page 3]. | n/a | Stands. Stage 6 outside the cycle. Same point as row 33. |
| 18 | B | B05 (absent) | Missed: CS and Compliance Officer exit with three reasons and a 30 day letter to disclosure gap. Evidence: Ann 2026-10-31 letter p.1; Ann 2026-10-31 p.1, p.3. (Also in Verifier B's missed list.) | n/a | Added in cycle 1 as FLAG-KMP-EXIT (LOW). |
| 19 | B | B05 (absent) | Missed: no forward looking statement undertaking followed by forward looking margin statements. Evidence: Ann 2026-09-21 p.1; Ann 2026-09-24 p.1; Ann 2026-10-05 p.2. (Also in Verifier B's missed list.) | n/a | Added in cycle 1 as a LOW red flag. |
| 20 | B | B06 (absent) | Missed: "4XM" order book line likely ties Inox as a small customer that is insourcing towers [INFERENCE]. Evidence: Pres p.21; INOX Q1FY27 p.4. (Also in Verifier B's missed list.) | n/a | B06 unchanged (stage 6 outside the cycle). Stage 5 added the 4XM line to its own report. |
| 21 | B | B05 1C LOI row; 2A row 2 | Under weighted: Q1 FY27 LOI absent from Prospectus post balance sheet events, then used to market the listing four days later. Evidence: Pros p.236 to 237; List p.2, p.8; CRISIL p.1. | n/a | Added in cycle 1 (whole file text search; pp.236 to 237 not read). Row stays Delivered. |
| 22 | B | B05 2A row 5 | Under weighted: derived inflow of 48 towers equals the two announced orders (38 + 10), so firm inflow outside them is about zero for seven months. Evidence: Pros p.114; Order(09-10) p.2; Ann 2026-10-29 p.2; Pres p.21. | n/a | Added in cycle 1. |
| 23 | B | B05 2C consistency; 3D | Under weighted: deck placeholder "Text", ROE 57% against RONW 40.92% unlabelled, counterparty names withheld on the two orders that make 48.6% of the book. Evidence: Pres p.7, p.21, p.25; List p.15; Order(09-10) p.2; Ann 2026-10-29 p.2. | n/a | Added to FLAG-CONSISTENCY in cycle 1. |
| 24 | B | B06 2B | Under weighted: Suzlon FY27 EBITDA guidance cut from about 17% to 15% plus 1% on mix not named. Evidence: SUZ Q2FY27 p.9 to 10. | n/a | Stands. Stage 6 outside the cycle. |
| 25 | B | B05 2A, 2C | Under weighted: no sequential comparison (H2 FY26 to H1 FY27 PAT down 57%; EBITDA per tower 34.5 to 33.7 lakh on P&L basis); completeness only. Evidence: H1 p.4; Pres p.18. | n/a | Added in cycle 1 as a completeness note. |
| 26 | C (F3) | 01-gate0.md l.81, l.95, l.101, l.103 | Rule G0-25. Block D on 31-Mar-2026 and E1/E3 on 30-Sep-2026. Block D 15 on the Sep-26 basis (D1 4, D2 2, D3 4, D4 5); core 73 with F1. If latest = Sep-26, Block D and B07 G1 credit the same IPO deleveraging; operator ruling requested. | n/a | Open operator ruling. One headline basis stated; Sep-26 shown as a sensitivity. |
| 27 | C (F4) | 01-gate0.md l.106, l.157 to 188 | Rule G0-51. Embedded YAML abbreviated; text after the block; truncated "1.38 crore... see note". B01-gate0.yaml is the copy of record. Presentational. | n/a | Fixed in cycle 1: full block reproduced; 13.8 lakh shares (Pros p.213). |
| 28 | C (F5) | 01-gate0.md l.40, l.148 | Rule G0-08 (observation). FY23 ROCE NOT FOUND; floor 11.88% from EBIT 9.61 / TA 80.90; Block A floor 15; recomputed core floor 61 (60 with filed CFO). | n/a | Tested in cycle 1; AVERAGE holds at the floor. |
| 29 | C (F6) | 07-emoat.md l.188, l.218, l.225 to 234 | Rule EM-21. R1 scored 0.7 on claim only evidence, no optionality register row. EM NONE unchanged; E1 to 2.0 path reaches 11.4, not 12.1, without R1. | n/a | Stands. Stage 7 outside the cycle. |
| 30 | C (F7) | 07-emoat.md l.104, l.179 | Rule EM-02. Meet Outcome 2026-10-05 tagged DOC; it is a management claim. No score change. | n/a | Stands. Stage 7 outside the cycle. |
| 31 | C (F8) | 07-emoat.md l.175; B07 completionist_recount | Rule EM-10. Claims 6 across 5 categories (six named); attributable B1 documented item is Rs 0.89 Cr GCP machinery (CARE p.8). Recount unchanged. | n/a | Stands. Stage 7 outside the cycle. |
| 32 | C (F9) | 07-emoat.md l.261 to 263; B07 combined_reasoning | Rule EM-24. States 61 of 140 core points, grand total 68, MODERATE. Recomputed core maximum 100; core 66, grand total 71, THIN. Combined AVERAGE unchanged. | n/a | Stands. Stage 7 outside the cycle. B01 governs. |
| 33 | D | 06-peers.md Q3, 2D, flags, risks | Page anchor error: Inox Q2 FY26 South India blade and tower plant is on [page 4] (file line 110), cited as [page 3]. Quote and fact confirmed. | n/a | Stands. Stage 6 outside the cycle. |
| 34 | D | 06-peers.md Q4, 2B, coverage map | Page anchor error: Suzlon Q1 FY27 ASP Rs 6.3 Cr is on [page 4] (file lines 118 to 119), cited as [page 3]. Fact confirmed. | n/a | Stands. |
| 35 | D | 06-peers.md Q7 | Q7 headlined VERIFIED although the first half of the claim (who buys the plate) is UNVERIFIABLE; PARTIALLY VERIFIED would match. Pass through has 3 independent peers. | n/a | Stands. |
| 36 | D | 06-peers.md Q1 | Q1 VERIFIED while the 80% top of Anawil's 70 to 80% sits above every peer figure (peer max 75%). Disclosed in the net read and FLAG-H2-RANGE-TOP; the headline verdict does not carry it. | n/a | Stands. |

## Verifier A source fidelity dispositions

| Number or claim | Verifier A verdict and anchor | Downstream position | Disposition |
|---|---|---|---|
| Revenue CAGR 177.1% (01-gate0.md C1, M1, M11) | MAJOR, source_fidelity true; truth 77.1% (SC Data_Sheet; Pros p.173) | Maker agreed | GATE HELD, corrected at source in cycle 1 |
| C4 minus 85.2pp; core 61; grand 68 (01-gate0.md C4 and totals) | MAJOR, source_fidelity true; truth +14.8pp, score 5 | Maker agreed; Verifier C F2 also moved M11 | GATE HELD, corrected at source in cycle 1 (core 66, grand total 71) |
| FY26 material cost 21.6 lakh per tower (04-bizmodel.md 3D) | MAJOR, source_fidelity true; truth 19.85 (H1 Res. p.4; AFS p.17) | Maker agreed | GATE HELD, corrected at source in cycle 1 (19.9, basis labelled) |
| Prospectus p.66 anchor for 65.26% (01-gate0.md E1) | MINOR, source_fidelity true; number on Pros p.68 | Maker agreed | GATE HELD, anchor corrected in cycle 1 |

No downstream step cleared, downgraded or reasoned around a Verifier A source fidelity finding. No verifier re-checked the corrections.

## Other verifier statements

- Verifier A struck 3 rows before emit: Gate 0 computed ROCE 26.79/26.25/16.39 against Prospectus printed 23.05/21.84/13.68 (basis labelled in Gate 0); "PRES p.27" (deck slide 27 = file page 28); Pros Annexure N not due 3,841.82 against AFS 3,841.81 (both faithfully transcribed).
- Verifier A NOT CHECKED: stage 9 web sourced figures (IWTMA, MNRE, JMK, Devdiscourse), stage 8 web and aggregator items (qorpiq.com, Chittorgarh, AmbitionBox), most peer transcript quotes beyond ten spot checks (all ten matched), and the remaining stage 2 and 3 AFS note cells.
- Verifier B credibility: "concur: C holds on the delivery record (re-scored 3 delivered, 2 partial, 1 missed) but sits at its floor". After the cycle the stage 5 tracker reads 2 delivered, 3 partial, 1 missed, grade C.
- Verifier B pipeline_flags_not_supported: none.
- Verifier C: recomputed_emoat em_score 10.8, em_classification NONE (concur). Recomputed combined AVERAGE (concur). Valuation, expectation ledger and business understanding narrative rules not assessed in phase 1.
- Verifier D: substantive_unsupported none; unused_but_relevant none.
