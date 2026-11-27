=== FILE: verifier-summary.md ===

# Verifier summary: DEEDEV, run 2026-11-15, Phase 1

## Phase 1 confidence delta (outputs/blocks/confidence.yaml)

| Component | Score | Basis |
|---|---|---|
| numerical_acceptance | 98.6 | B12a: 442 numbers checked, 6 findings (0 CRITICAL, 3 MAJOR, 3 MINOR); mandatory tier 112 of 112 |
| redflag_coverage | 88.9 | B12b.acceptance_rate: 16 of 18 material items already in the pipeline (8 fully caught, 8 partially caught) |
| framework_adherence | 87.5 | B12c phase 1 scope only: Gate 0 40/45 + Emerging Moat 23/27 = 63/72 |
| peer_utilisation | 83.3 | B12d: 10 peer transcripts used substantively of 12 provided |
| overall | 83.3 | overall_set_by: peer_utilisation; band "75-89 normal, note specifics" |

Valuation framework adherence: PENDING PHASE 3. Stages 10 and 11 have not run. Verifier C's valuation rules (0 checked), expectation ledger rules 13 and 14, and business narrative rule 9 are all pending.

## Acceptance rates and counts

| Verifier | Model | Block acceptance_rate | Counts | Coverage |
|---|---|---|---|---|
| A, numerical (B12a) | claude-sonnet-5-5 | 98.6 | CRITICAL 0, MAJOR 3, MINOR 3; 5 false positives struck | 442 checked of a material universe of about 700; mandatory 112 of 112 |
| B, red flags (B12b) | claude-opus-5-5 | 88.9 (caught plus partially caught); 44.4 on fully caught only | CRITICAL 0, MAJOR 7, MINOR 14 | 37 independent flags; 18 material (1 CRITICAL, 17 MAJOR): 8 caught, 8 partially caught, 2 missed |
| C, framework (B12c) | claude-opus-5-5 | 87.5 | CRITICAL 0, MAJOR 3, MINOR 6 | Gate 0 45 rules, Emerging Moat 27 rules; valuation pending phase 3 |
| D, peers (B12d) | claude-sonnet-5-5 | 92 | CRITICAL 0, MAJOR 1, MINOR 1 | 12 peer transcripts audited; 10 substantive confirmed; claims all addressed; no verdict discipline fails |

Open item for the operator (confidence.yaml): "Verifier B states two readings of its own acceptance rate. The block field is 88.9% (caught plus partially caught, the prompt definition 'ones the pipeline already had'). Counting only fully caught items it is 8 of 18 = 44.4%, below the 60% REWORK line. The orchestrator used the block field as written. The operator rules which basis governs."

Verifier B's one CRITICAL independent item (repeated evasion on margin split and order book mix across all three calls) has status CAUGHT. It is not a finding against the pipeline.

Verifier B spot checks of promise delivery: 5 checked, 3 confirmed, 2 wrong. Credibility grade concurrence: "lower: rows 12 and 22 fail the spot check and row 13 rests on an unfiled MOM, so hard deliveries are 5 of the 8 claimed, and candour items (equity board approval 12 days after 'nothing decided', Thailand three-year claim, unflagged Q4 one-off) sit on top of the cash and debt misses; B/C borderline".

Verifier C recomputed decision: "concur: Gate 0 AVOID and B07 combined AVOID stand under every reading tested".

## Source fidelity dispositions (confidence.yaml)

| Verifier A finding | Disposition |
|---|---|
| B12a row 1, 03-ardeep.md contingent liabilities total | GATE HELD: figure corrected at source (25,475.26 INR lacs, 28.7%; AR Note 32B p.229, Note 46 p.251, Note 32(e) p.230) |
| B12a row 2, 05-concall.md and 09-tam.md oil and gas 890.12 | GATE HELD: figure corrected at source (889.95; order filing 13 Nov 2026 p.2) |
| B12a row 3, 09-tam.md India book 59.6% power | GATE HELD: figure corrected at source (59.05%; order filing 13 Nov 2026 p.2) |

Verifier A identity check: "B12a carries no CRITICAL row; nothing to test, nothing struck."

Verifier disagreements: none.

Verifier A shadow: not run in this session; the single shadow run belongs to the TD Power session (operator batch instruction 2026-11-15).

## Findings, CRITICAL

None. No verifier logged a CRITICAL finding.

## Findings, MAJOR (14)

| # | Verifier | ID | Location anchor | Note (verifier's words) |
|---|---|---|---|---|
| 1 | A | B12a row 1 (source fidelity) | 03-ardeep.md Phase 2C closing paragraph (contingent liabilities total) | Claimed 25,152.11 lacs (28.4%). Source: 22,970.21 (AR Note 32B p.229) + 1,384.96 (Note 46 p.251) + 1,120.09 (Note 32(e) p.230) = 25,475.26 lacs = 28.7% of 88,706.85. "Derived sum is 323.15 lacs below its own components. Still above the report's 25% flag, so no decision change. Components all verified." |
| 2 | A | B12a row 2 (source fidelity) | 05-concall.md Section 3D 'Mix at 31 Oct' (also 09-tam.md 3A filter table, oil and gas 890.12) | Source: Reg 30 order filing 13 Nov 2026 p.2, Thailand Oil & Gas closing 0.00; closing oil and gas = 889.95; 1,677.48 + 889.95 + 19.00 = 2,586.43 ties to the printed total. "Component read from the opening column instead of the closing column. Value effect 0.17 cr (0.007% of the book); percentages unchanged at one decimal." |
| 3 | A | B12a row 3 (source fidelity) | 09-tam.md 3A 'Indicative power versus non-power' and Section 6 row 1 (India piping book 59.6% power) | Source: 1,304.47 / 2,209.04 = 59.05% power / 40.95% non-power (OB p.2 closing column). "Arithmetic on correct source inputs is off by 0.55 pp. Downstream Rs 321 cr / Rs 218 cr split would read Rs 318 cr / Rs 221 cr. No decision change." |
| 4 | B | B12b-01 (MISSED and SPOT-CHECK WRONG) | B05 2A row 12; Concall Aug 2026, Bansal, [txt p.5], [txt p.6], [txt p.13]; Concall May 2026, Bansal, [txt p.11] | Thailand "practically 100% booked for three years" accepted as DELIVERED; same call puts Thailand at about Rs 200 cr of book against Rs 170-200 cr a year. Fix: re-score UNVERIFIED; separating observation is the Thailand line in the next order-position filing. |
| 5 | B | B12b-02 (MISSED) | B05; Concall May 2026, Kamlesh and 'Krishna Kumar', [txt p.15]; Yadav, [txt p.4]; Concall Aug 2026, Pranay Roop Chatterjee, [txt p.7] | Q4 FY26 includes about Rs 5 cr one-time retrospective Malwa tariff credit; Q4 margin ex-credit about 16.8% (verifier's arithmetic). Fix: record the one-off; Verifier A to confirm the amount and the line it sits in. |
| 6 | B | B12b-03 (PARTIALLY CAUGHT, under-weighted) | B05 4D; Concall May 2026, Bansal, [txt p.15]; announcement 20260603 lines 29-42; Concall Aug 2026, Bansal, [txt p.4] | 22 May "immediately nothing is decided"; 3 Jun board approves the Rs 300 cr preferential, 12 days later. Fix: raise to a candour flag (MEDIUM-HIGH); carry into the credibility grade. |
| 7 | B | B12b-04 (PARTIALLY CAUGHT, omitted from red flags) | B05 2D, 3C, 4D; Concall May 2026, Pankaj Agarwal, [txt p.9]; Concall Aug 2026, Bansal, [txt p.5], [txt p.15] | GE line of about Rs 380 cr (about 15.6% of the June book) is an LOI with "no inputs"; May vs Aug contradiction not drawn. Fix: add to red_flags; discount order-book visibility by the LOI share until a PO and drawings arrive. |
| 8 | B | B12b-05 (PARTIALLY CAUGHT, misclassified) | B06 contradicted list; B05 2D; ISGEC Jun 2026, Puri, [txt p.5]; ANUP May 2026, [txt p.2]; ANUP Aug 2026, [txt p.3]; RATNAMANI May 2026, [txt p.19]; ISGEC Aug 2026, [txt p.3]; Concall Feb 2026, [txt p.14]; Concall Aug 2026, [txt p.9], [txt p.15] | Peers report war-driven input, gas and freight cost rises; ANUP cut FY27 EBITDA guide to about 15%; DEE holds above 19%; B06 lists 0 contradictions. Fix: classify as a peer contradiction against load-bearing fact 1b; carry to synthesis as the margin risk with two readings. |
| 9 | B | B12b-06 (PARTIALLY CAUGHT, misclassified) | B05 T8; B06 Q7; Concall Feb 2026, Bansal, [txt p.10]; Concall Aug 2026, Bansal, [txt p.11]; RATNAMANI May 2026, Sanghvi, [txt p.6] | B05 labels DEE "NPCIL-qualified" with no DEE source; RATNAMANI says RFSS is the only NPCIL-approved nuclear facility from India. Fix: drop the label; record two readings; separating observation is a DEE NPCIL approval disclosure or a nuclear-island order. |
| 10 | B | B12b-07 (PARTIALLY CAUGHT) | B05 1B, 2A row 10; Concall May 2026, Bansal, [txt p.7]; Concall Feb 2026, Bansal, [txt p.7]; Concall Aug 2026, Bansal and Yadav, [txt p.9], [txt p.18] | CMD: "our EBITDA margin may drop on the face of it in terms of percentage, but value-wise, it will increase"; guide basis moved from core 18-20% to consolidated above 19%. Fix: record the admission and the basis shift against load-bearing fact 1b. |
| 11 | C | F-G0-1 | 01 Gate 0; rule P01 FORMULA DEFINITIONS (ROCE = EBIT / (TA - CL)) | Proxy capital employed used for all 7 years incl. FY25-FY26 where strict inputs exist. Reading 1: Block A 7, Core 41, deal-breaker 3 off, Block F 13. Reading 2: Block A 0, Core 34. "none: AVOID holds via override 6 (ND/EBITDA 3.51x AND IC 2.58x), which uses no capital employed". |
| 12 | C | F-G0-2 | 01 Gate 0; rule P01 Block F (PEER DATA NEEDED scores 0) | M5 scored 3 while data_notes mark the full segment peer list PEER DATA NEEDED. Reading b: M5 0, Block F 9, moats_confirmed 1, THIN, grand_total 48. "none: Core 39 < 40 and override 6 hold AVOID". |
| 13 | C | F-EM-1 | 07 Emerging Moat; rule P07 Section 5 matrix; verifier rule 3 | A3 (DOC), H3 (DOC), C1 (CLAIM) evidenced but scored 0 while Weak rows take the matrix floor. Recomputed 12.1 MODEST (A3, H3), 12.8 MODEST with C1. "B07 combined AVOID unchanged; em_classification NONE to MODEST feeds stage 11 Pillar 3. Phase-3 Verifier C: CRITICAL if the band change moves the destination PE by more than 1x". |
| 14 | D | B12d rule 3 | ANUP Q3 FY26 p.14 | "B06 Q3 net read and Part 4 'most consequential gap' state no peer supports 190-200 days. ANUP Q3 FY26 p.14 carries an analyst figure of 190-200 days for ANUP itself, undisputed." Verdict PARTIALLY VERIFIED stands; the "above every peer figure" sentence and flag need softening. |

## Findings, MINOR (24)

| # | Verifier | ID | Location anchor | Note (verifier's words) |
|---|---|---|---|---|
| 1 | A | B12a row 4 | 05-concall.md Section 0 row 24 (net debt at Sep-26) | "'excludes Rs 72.4 cr trade credits and leases'": 72.4 is trade credits alone (7,242.76 lacs, Q2 FY27 p.5); leases 22.43 cr more, together 94.86 cr. "Ambiguous wording, so left as imprecision." |
| 2 | A | B12a row 5 | 02-notes-pass2.md C1 customer table bullet (John Zink FY25) | AR Note 33(c) p.234 prints John Zink FY25 6,026.67, same as consolidated; printed 10.10% does not match its own amount (9.43%). The Numaligarh FY25 gap in the same bullet stands. |
| 3 | A | B12a row 6 | 01-gate0.md Section 1 note (EBITDA basis for D1) | Four FY26 quarterly operating profit rows sum to 191.21; 195.84 is arithmetic on annual expense rows. "D1 would read 3.59x on 191.21 and still score 0 (>3x). Override 6 unchanged." |
| 4 | B | B12b-08 | B05 2B, 4D; Concall Feb 2026, Yadav, [txt p.4]; Bagmar and Bansal, [txt p.5]-[txt p.7] | Feb transcript revised after the call; in-call power-loss figures conflict (Rs 6.4 cr vs Rs 14.3-14.6 cr). Fix: one row with the revision and the four numbers. |
| 5 | B | B12b-09 | B05 1B, 1C; Concall May 2026, [txt p.14]; Concall Aug 2026, [txt p.7], [txt p.9], [txt p.15] | Order inflow "definitely contingent to BHELs orders" (May) vs "absolutely no worry... the customer may change" (Aug); remainder rises within the Aug call. |
| 6 | B | B12b-10 | B06 Q6, 2C; Concall May 2026, [txt p.12]; RATNAMANI Nov 2025 [txt p.5], [txt p.14]; RATNAMANI Nov 2026 [txt p.4]; ISGEC Feb 2026 [txt p.5]; ISGEC Aug 2026 [txt p.5]; ANUP May 2026 [txt p.4] | "Practically no competition" vs RFSS thermal and oil and gas spools, ISGEC piping shops and skids, ANUP first skids order. Fix: competitive-entry watch item against the 65% power book. |
| 7 | B | B12b-11 | B05 2A row 22; Concall Aug 2026, [txt p.11]; announcement 20261016 p.1, p.3 | Export pre-qualification partner promised; outcome is a domestic EPC framework filed 16 Oct, "not, by itself, an order". Fix: re-score PARTIAL; tally 6 delivered, 9 partial, 5 missed with row 12 also re-scored. |
| 8 | B | B12b-12 | B05 2A row 13; Concall May 2026, [txt p.9] vs [txt p.11]; Concall Aug 2026, [txt p.5] | Siemens scored DELIVERED on "a sort of understanding or an MOM", no filing. Fix: re-score UNVERIFIED until a filing or PO. |
| 9 | B | B12b-13 | B05 2E row 5; Concall Feb 2026, [txt p.12] | Paraphrase error: the PSERC hearing was held 10-15 days earlier; order expected "at any given time". |
| 10 | B | B12b-14 | B06 Q3; RATNAMANI Nov 2026, Salil Desai and Katta, [txt p.12] | Attribution error: "negative in H1" was the analyst's premise, not a Ratnamani CFO statement. |
| 11 | B | B12b-15 | B05; Concall May 2026, [txt p.2], [txt p.15] | Unidentified speaker "Krishna Kumar" answers two material questions. Fix: transcript-integrity caveat. |
| 12 | B | B12b-16 | B05 1B; Concall Aug 2026, [txt p.8], [txt p.17]; Concall Feb 2026, [txt p.12] | Anjar "almost 100%" vs "70-75% or maybe a little higher" next year on one call; Anjar Rs 1,500 cr by FY28-29 not set against the Rs 2,300-2,500 cr ceiling. Fix: record 70-100% for FY28. |
| 13 | B | B12b-17 | B05; Concall Feb 2026, [txt p.3], [txt p.11] | Seamless capex Rs 90 cr with Rs 22.5 cr from internal accruals while the same call promises no new term loan. |
| 14 | B | B12b-18 | B05; Concall Aug 2026, [txt p.7] | Biomass fuel supply limits running both the power plant and the pellet plant until October; bears on the FY27 "EBITDA neutral" promise. |
| 15 | B | B12b-19 | B05; Concall Aug 2026, [txt p.6] | "Considerable reduction in the manpower headcount" with no major recruitment while guiding about 31% revenue growth. |
| 16 | B | B12b-20 | B05 2E; Concall May 2026, [txt p.6] | Q4 FY26 gross-margin dip blamed on trading at 95-100% material value; recorded as excuse, not revenue quality. Fix: Q4 trading revenue share NOT FOUND; ask. |
| 17 | B | B12b-21 | B05 2C; Concall Feb 2026 [txt p.5], [txt p.7]; May 2026 [txt p.6], [txt p.15]; Aug 2026 [txt p.16], [txt p.17] | CMD routes numeric questions to CFO or COO, who defer back or lack the data, on all three calls. Fix: finance-bench depth signal. |
| 18 | C | F-G0-3 | 01 Gate 0; rule P01 E4 | E4 numerator omits Note 30B(e) 815.09 + 305.00; with them 27.05%, E4 unchanged; "Others" amount NOT FOUND (referred to Verifier A). "none". |
| 19 | C | F-G0-4 | 01 Gate 0; rule P01 rule 4 | M3 FAT denominator 653.78 carries no source anchor. "none". |
| 20 | C | F-G0-5 | 01 Gate 0; rule P01 OUTPUT | Dashboard has no per-test moat profile bars M1-M12. "none". |
| 21 | C | F-EM-2 | 07 Emerging Moat; P07 completionist guard recount | Report says 10 residual documented items, block says 9; block correct (21 - 12 = 9); H3 items outside the count. "none". |
| 22 | C | F-EM-3 | 07 Emerging Moat; P07 I2 | I2 answered for 3 claimed moats only; E2, F2, G1, H2, R1 and the B2 certification stack unanswered; I2 0 stands. "none". |
| 23 | C | F-EM-4 | 07 Emerging Moat; one improvement, one mechanism | R1 4C rests on vendor approvals repeated from the B2 table; R1 0.7 sustainable on its own 4B items; under B07's own logic R1 would be 0 and the total 9.4. "no numeric change". |
| 24 | D | B12d rule 3 | ISGEC Q3 FY26 (Feb 2026 transcript, .txt line 443) | B06 flag 3 and Part 2E tie FGD retention to a BHEL-weighted book; ISGEC CFO says the stuck FGD retention is "not really BHEL" (NTPC). The PSU-terms point holds; the BHEL link does not. |

## Verifier B missed items (as listed in B12b.missed)

| Severity | Item (short) | Anchor |
|---|---|---|
| MAJOR | Thailand three years booked vs about Rs 200 cr book | Concall Aug 2026, Bansal, [txt p.5], [txt p.6], [txt p.13] |
| MAJOR | Q4 FY26 one-time Malwa tariff credit of about Rs 5 cr | Concall May 2026, [txt p.15], [txt p.4]; Concall Aug 2026, [txt p.7] |
| MINOR | Anjar utilisation two figures on one call | Concall Aug 2026, [txt p.8] vs [txt p.17] |
| MINOR | Seamless internal accruals vs no new term loan | Concall Feb 2026, [txt p.3] vs [txt p.11] |
| MINOR | Speaker "Krishna Kumar" not on the roster | Concall May 2026, [txt p.2], [txt p.15] |
| MINOR | Biomass fuel constraint | Concall Aug 2026, [txt p.7] |
| MINOR | Headcount reduction vs +31% revenue guide | Concall Aug 2026, [txt p.6]; Concall May 2026, [txt p.4] |

Verifier D unused but relevant item: ANUP Q3 FY26 analyst figure of 190 to 200 days for ANUP's own cycle (ANUP-Concall_Feb_2026_Transcript, page 14, lines 545-550 of .txt).
