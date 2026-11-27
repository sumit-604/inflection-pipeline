# INVPRECQ verifier summary, run invprecq-2026-11-15, PHASE 1

## Phase 1 confidence delta

| Component | Value | Verifier | Denominator and counts |
|---|---|---|---|
| numerical_acceptance | 98 | A (B12a, claude-sonnet-5-5) | 441 numbers checked; mandatory tier 111 of 111 (every Gate 0 scorecard input); about 330 of about 600 material numbers in the sample tier; 6 rows struck on self check |
| redflag_coverage | 71 | B (B12b, claude-opus-5-5) | 7 material items: 2 CAUGHT, 3 PARTIALLY CAUGHT, 2 MISSED; strict CAUGHT only rate 29 (2 of 7); 49 independent items in all (17 caught, 12 partial, 20 missed) |
| framework_adherence | 89.5 | C (B12c, claude-opus-5-5), phase 1 scope | 86 rules (Gate 0 58, Emerging Moat 28); 77 passed; valuation rules 0 checked, PENDING PHASE 3 |
| peer_utilisation | 100 | D (B12d, claude-sonnet-5-5) | 12 of 12 peer transcripts SUBSTANTIVE and confirmed; 9 of 9 peer questions carry a verdict |
| overall | 71 | min of applicable | set by redflag_coverage; band 60 to 74 (PROCEED verdicts downgrade one level); rework false |

Severity counts: A 0 CRITICAL, 1 MAJOR, 6 MINOR. B 0 CRITICAL, 5 MAJOR, 9 MINOR (consolidated findings F1 to F14). C 0 CRITICAL, 4 MAJOR, 5 MINOR. D 0 CRITICAL, 0 MAJOR, 4 MINOR.

Verifier B notes two readings of its own rate: 71% counting partial catches (the block field, used here) and 29% on full catches only. On the strict count the component falls below 60% and REWORK would fire. This is an open item for the operator at Halt 1.

## Findings, sorted by severity

No CRITICAL finding in any verifier.

### MAJOR

| Verifier | ID | Location anchor | Note (as the verifier wrote it) |
|---|---|---|---|
| A | A-1 | 05-concall.md section 3B (India defence production bullet) | Claimed "required growth about 14.8% a year over four years (derived), from Rs 1,50,590 crore FY25 to Rs 3 lakh crore by 2029". Same two inputs (Q2 FY27 presentation p.16) over four years give (300,000/150,590)^(1/4) less 1 = 18.8%; 14.8% is the five year rate. Inputs match the source; the derived rate is wrong on the report's own stated period. Context statistic, not a decision input. source_fidelity: false |
| B | F1 | B05 (05-concall.md 4D, 1C) | Missed R5: FY26 growth auto led, non auto down about 13%; AR "broad-based" claim, CFO diversification margin claim and CARE auto share claim contradicted by AR26 p.24. Fix: add to 4D as HIGH; use FY26 segment rupees in stage 13 and Role 1 |
| B | F2 | B05 (05-concall.md 4D) | Missed R6: Rs 18 Cr managerial pay cap resolution, CMD +41.10% and WTD/CFO +50.27% vs median +7%, CMD take 36.7% of FY26 profit, guarantee commission +91.5% H1 on H1. Fix: add to 4D; carry to Role 2 governance ledger as a tripwire |
| B | F3 | B05 (05-concall.md fact 1, fact 3) | R4 partial: cash flag treats other assets (651.51) as working capital though management said capex sat there in H1 FY26; H1 FY26 0.11x comparator carries about 11 Cr solar capex (derived); 2.41 Cr capex gap ties to CWIP +241.43 lakh, not advances. Fix: state both readings (0.32x filed, up to about 0.61x) and the separating observation; restate or drop the H1 FY26 comparator |
| B | F4 | B05 (05-concall.md 4D; repeated_evasions) | R1 under weighted: order value withheld in 5 filings over 4 quarters graded MEDIUM; repeated_evasions empty. Fix: re-grade HIGH; name it a repeated non-disclosure |
| B | F5 | B06 (06-peers.md Part 4; contradicted list) | R22 misclassified: "Claims contradicted: 0" while Steelcast calls defence "one of the most riskiest" with worse pricing, against I&PCL "strategic pillar". Fix: add to contradicted with moderate weight |
| C | G-04 | 01-gate0.md Block A, M3 (Gate 0) | Rule: ROCE fixed as EBIT / (Total Assets less Current Liabilities); missing input = NOT FOUND, score 0. Filed EBIT / (equity + reserves + borrowings); A1 1, A4 5, M3 1; Block A 6; core 49. As written: A1 0, A4 0, M3 0; Block A 0; core 43, AVERAGE; any true TA less CL ROCE keeps core 43 to 58 (AVERAGE). Decision effect none alone; with G-07 also strict, core 38 = AVOID; flag for Halt 1 |
| C | G-07 | 01-gate0.md Block B, B2 and B3 (Gate 0) | Rule: FCF fixed as CFO less purchase of PPE and intangibles; missing input = NOT FOUND, score 0. Filed CFO + CFI proxy; B2 2, B3 3; Block B 10. As written: B2 0, B3 0; Block B 5; core 44, AVERAGE; FY25 to FY26 AR capex check holds the B3 band (0.48). Decision effect none alone; with G-04 also strict, core 38 = AVOID; separating observation: FY17 to FY24 current liabilities and PPE purchases from prior ARs |
| C | EM-11 | 07-emoat.md Section 5 matrix (rows E2, G1, G2, H2, C1, F1) | Rule: Section 5 matrix, no evidence = 0, LL = 1; Section 3 evidence table or NO EVIDENCE FOUND. Filed: unwritten offset rule zeroes E2, G1, G2, H2, C1, F1; em_score 7.8 NONE. Recomputed on the written matrix: narrow set 10.8 to 11.2 (NONE); wide set 12.2 to 12.6 (MODEST, edge 12). Band NONE vs MODEST; UA qualifier (EM 25 or above) unmet either way; Pillar 3 effect checked in phase 3; operator ruling needed on offset evidence |
| C | EM-12 | 07-emoat.md Section 5, row A1 | Rule: multiplier by evidence tier, DOC 1.0, CLAIM 0.7, INF 0.5. Filed A1 at 0.7; A1 evidence is DOC (furnace, GTRE order) + INF (rarity), no CLAIM. Recomputed 0.5 by the stage's weakest leg convention: A1 1.0, total 7.4; 1.0 on the documented furnace: A1 2.0, total 8.4. Decision effect none; NONE either way on the filed set |

### MINOR

| Verifier | ID | Location anchor | Note (as the verifier wrote it) |
|---|---|---|---|
| A | A-2 | 07-emoat.md A1 evidence table (CARE p.1, p.4) and section 2B plant table (CARE p.1) | Claimed vacuum casting capacity up to 100 MTPA at CARE p.1, vacuum casting since FY18 at CARE p.4. Capacity sentence is on CARE rationale p.2; FY18 vacuum casting sentence is on p.3. Values exist in the document; the cited pages do not contain them. source_fidelity: true |
| A | A-3 | 02-notes-pass1.md, 02-notes-pass2.md, 02-notes.md and B02 block (all AR page anchors) | AR anchors one page above the PDF page, e.g. CF p.111, P&L p.109, BS p.108, Note 23 p.127, Cons Note 38 p.174, Notice item 4 pp.46 and 53, Board report p.76. PDF pages are 110 (cash flow), 108 (P&L), 107 (BS), 126 (Note 23), 173 (Cons Note 38), 45 and 52 (Notice item 4), 75 (Board report). Values and note numbers all match. Systematic off by one anchor, logged in the run log erratum and corrected in the 03-ardeep Phase 2 table. Counted once. source_fidelity: true |
| A | A-4 | 03-ardeep.md section 0 fact 2 | Claimed KPI p.21 and p.24 show 5.86%. 5.86% is printed on AR p.22 (Aerospace & Defence 10.87 Cr, 5.86% of revenue). p.21 prints defence 7.90 Cr and aerospace 2.97 Cr; p.24 prints segment percentages 1.60 and 4.26 that sum to 5.86. Value exists in the AR; the cited pages do not print it as 5.86%. source_fidelity: true |
| A | A-5 | 01-gate0.md D1 (net debt) | Claimed net debt Rs 67.70 Cr from debt plus lease 71.59 less cash and bank 3.88. 71.59 less 3.88 = 67.71 (AR p.107: 7,158.75 less 387.51 = 6,771.24 lakh). Ratio 2.19x and score 1 unchanged. Rounding slip of 0.01 Cr in a Gate 0 input. source_fidelity: false |
| A | A-6 | 01-gate0.md block F M12 and data_notes (WC days FY25) | Claimed 139.2 days FY25. AR p.107 and p.108: (4,158.33 + 4,872.15 less 2,737.68) / 16,507.37 x 365 = 139.14 days. 0.1 day rounding difference; FY26 121.6 matches; score unchanged (M12 0). source_fidelity: false |
| A | A-7 | 01-gate0.md D2 | Claimed EBIT 2,308.95 lakh / finance cost 617.97 = 3.74x (AR p.108). 2,308.95 = PBT after the 52.51 exceptional item (1,690.98) + 617.97. Pre-exceptional EBIT is 2,361.46 (3.82x, used in 03-ardeep). Basis not stated in Gate 0. Band 3 to 4.9 and score 2 unchanged on either basis. source_fidelity: false |
| B | F6 | B05 (05-concall.md 1C, 2A row 1) | Solar slip understated; FY26 AR target line is copied text printed after commissioning; FY25 AR said "second half of FY 2025"; decks listed the solar farm as existing before it was built. Fix: replace the "met by one day" reading |
| B | F7 | B05 (05-concall.md 2A row 4) | 2A row 4 (growth across auto and non auto) scored DELIVERED; non auto fell in FY26. Fix: re-score PARTIAL; counts 4/2/0 |
| B | F8 | B05, B06 (05-concall.md fact 1; 06-peers.md PEER-WIP-MARGIN) | 13.9% margin "excluding inventory credit" removes the whole change in inventories line; only fixed overhead absorption is a quality risk; 13.9% is a floor. Fix: label 13.9% a lower bound with the reason |
| B | F9 | B05 (05-concall.md 1B, 2C) | R11 debt framing and R12 interest coverage comparator not caught; 1B carries 3.40x as fact. Fix: note both in 2C Consistency |
| B | F10 | B05 (05-concall.md 2D) | R8 segment drop not read as lost disclosure; R9 re-filing cause not found. Fix: add both to 2D |
| B | F11 | B05 (05-concall.md 2C, 2D) | R13 (beyond headcount), R14, R15, R17, R18, R19 not listed. Fix: add to 2C and 2D |
| B | F12 | B06 (06-peers.md risks_peers_raise) | No peer evasions, intra call contradictions or slips logged (R26, R27, R29, R30, R32 to R36, R39, R41 to R45). Fix: optional add to risks_peers_raise; R33 and R43 are useful base rates |
| B | F13 | B06 (06-peers.md 2C) | "one of four expanders in a six company set"; the set is four companies. Fix: cosmetic correction |
| B | F14 | B05 (05-concall.md 2A row 2) | 2A row 2 scores a status statement as a delivered promise; evidence not tied to the customer. Fix: move outside the counts or tie to PLR evidence |
| C | G-02 | 01-gate0.md C1/C2 endpoints, C3 decline years, M11 window CAGRs (Gate 0 rule 4) | Filed: C1/C2 endpoints 92.04, 4.17, 11.76, C3 decline years, M11 3.5% and 21.4% carry no anchor. No score change; routed to Verifier A. Decision effect none |
| C | G-40 | 01-gate0.md M3 (FAT denominator) | Filed FAT 188.45/100.82 = 1.87x, M3 1; denominator unnamed. Net block 1.91x = 1; gross block 0.93x = 0, moat 2, grand total 51. Decision effect none; moats_confirmed 0 and class NONE either way |
| C | EM-03 | 07-emoat.md evidence items at E L45, L66, L148, L172, L209 | Rule 3 document anchor on each evidence item: items anchored to B03, B04 and B05 (beyond the promise record), not document pages. No score change; no scored row rests on these alone. Decision effect none |
| C | EM-06 | 07-emoat.md Section 1A, GTRE and MKU rows | Section 1A status from the prescribed set: GTRE and MKU rows read "PO received". ANNOUNCED for both on the stated facts. Decision effect none |
| C | EM-18 | 07-emoat.md completionist recount and evidence_mix | Filed 16 documented across 9 categories plus the approval; evidence_mix 16/15/6. Recount: 15 in 9 categories + 1 Section 2 = 16; ledger omits 3 DOC and 2 CLAIM table items: documented 19 or more, claim 17 or more. Decision effect none; guard outcome unchanged (6 of 23 scored) |
| D | D-1 | B06 Q4 and Part 2C, Alicon Q1 FY27 Rs 125 Cr / Rs 500 Cr / possession 1 Sep 2026 | Cited [page 6] and [page 20]; text sits on marker page 5 (lines before the [page 6] marker) and marker page 19. Content exists as quoted; anchor off by one, against B06's own start of page convention |
| D | D-2 | B06 Q3, Steelcast Q1 FY27 inventory "time lag of 1 to 2 months" | Cited [page 11]; quote is on marker page 12. Content exists as quoted |
| D | D-3 | B06 Q9, Alicon EV "market has not grown in the manner we were thinking for the EV" | Attributed to Q3 FY26 call (Feb 2026) [page 16]; quote is in the Q4 FY26 call (May 2026) on marker page 18. Q3 file has no such quote. Also the Q4 [page 9] anchor shows the order book cut but not EV as the named cause (EV cause is at Q4 page 18) |
| D | D-4 | B06 Q5 and Q8 verdict labels | Q5 listed under verified though the nickel, cobalt and scrap trend half is unverifiable (3 independent peers meet the 2 anchor bar for pass through, so no discipline fail). Q8: no peer claims share gain; Azad GTRE engine delivery is indigenisation, not share gain; PARTIALLY VERIFIED is generous but not an upgrade from silence |

## Verifier B: independent items the pipeline missed

From the B12b missed list. Severity is Verifier B's, graded against the I&PCL decision.

| Severity | Item | Anchor |
|---|---|---|
| MAJOR | R5 FY26 growth auto led (auto about 91% of +22.85 Cr, derived); non auto 26.55% to 20.28% (about 43.2 to 37.6 Cr, derived) against AR "broad-based acceleration across all five business segments", the CFO diversification led margin claim and CARE auto share 66% to 64% | AR26 p.21, p.22, p.24, p.19; CARE p.2; P-Q2FY27 p.9 |
| MAJOR | R6 AGM special resolution: managerial pay cap Rs 18 Cr p.a. in no or inadequate profit years (1.5x FY26 profit); CMD +41.10%, WTD and CFO +50.27% vs median +7%; CMD 431.63 lakh incl 84.52 guarantee commission = 36.7% of FY26 profit; guarantee commission about 40.25 to 77.09 lakh H1 on H1 | AR26 p.45, p.52, p.72, p.75; R-Q4FY26 PAGE 10; R-Q2FY27 PAGE 7 (OCR) |
| MINOR | R11 CFO letter: D/E improved 0.71 to 0.68 "supported by healthy cash generation" while total debt rose 560.32 lakh | AR26 p.19, p.71 |
| MINOR | R12 Deck FY26 interest coverage comparator 3.40x equals CARE TD/GCA; deck method gives 3.74x (derived); CARE coverage 5.04x | P-Q2FY27 p.11; CARE p.2; R-Q4FY26 PAGE 5 |
| MINOR | R14 Deck errors: Q4 FY25 PAT change 80.48% and 63.29% (actual +414% and +171%, derived); Empire State address; Q4 FY26 deck places the Q3 exceptional item beside Q4 | P-Q4FY25 p.8, p.9, p.12; P-Q4FY26 p.9; R-Q4FY26 PAGE 5 |
| MINOR | R15 AR has no management explanation of FY26 results (MD&A industry text and SWOT only; ratio reasons "Increase in profit"); stale "Six Directors" and "no material changes" text | AR26 p.76, p.77, p.78, p.55, p.136 |
| MINOR | R17 BSE price movement query 29 Jun 2026, reply 30 Jun 2026 "no pending material information", CARE upgrade 9 Jul 2026; knowledge on 30 Jun NOT FOUND | A-20260630 p.1; CARE p.1 |
| MINOR | R18 RPT: Meche Pvt Ltd purchases 319.88 lakh FY26 (254.93 FY25); HUF rent 24.00; relative consulting 6.00 | AR26 p.134, p.135 |
| MINOR | R19 CRISIL suspended ratings 18 Sep 2014 for non cooperation by IPCL | CARE p.3 |
| MINOR | R27 Azad speakers contradict each other on FX lift: "few percentages" vs "5%, 6%" | AZAD Q1 FY27, Chopdar and Malpani, [page 15] |
| MINOR | R29 Azad dodges: capex not quantified, factory count withheld, utilisation deflected, hot section margin withheld, some order values undisclosed with book flat at Rs 6,500 Cr after Rs 600 Cr delivered | AZAD Q2 FY26 [page 12], [page 17], [page 19]; Q4 FY26 [page 6], [page 17], [page 18] |
| MINOR | R30 Azad volunteered churn: "selectively replacing certain functional roles internally" | AZAD Q4 FY26, Chopdar, [page 4] to [page 5] |
| MINOR | R33 Steelcast 2.4 MW power plant "by 30th June, 2026" moved to "before 31st December 26", no reason given | STEELCAS Q2 FY26 [page 5]; Q3 FY26 [page 5]; Q4 FY26 [page 5]; Q1 FY27 [page 4] |
| MINOR | R34 Steelcast contradicts itself: Alang scrap 20 to 25% vs none; two segment mixes in one call; exports about 65% vs "historically 45% to 50%" | STEELCAS Q3 FY26 [page 9]; Q1 FY27 [page 8], [page 9], [page 10], [page 11]; Q2 FY26 [page 5] |
| MINOR | R35 Steelcast dodges: US share "you need to figure this out"; "SEBI doesn't allow us"; "these are aberrations" | STEELCAS Q2 FY26 [page 8]; Q3 FY26 [page 12]; Q4 FY26 [page 10] |
| MINOR | R39 Steelcast drops US railroad after two calls of unresolved issues | STEELCAS Q2 FY26 [page 10]; Q4 FY26 [page 9]; Q1 FY27 [page 6] |
| MINOR | R41 Alicon margin gains "will continue in coming two quarters", then Q3 margin 10.9% vs 12.9%; FY27 outlook deferred twice | ALICON Q2 FY26 [page 11], [page 12]; Q3 FY26 [page 6], [page 18] |
| MINOR | R42 Alicon CFO "8% to 10%" vs CEO "12% to 15%" FY27 growth in the same call | ALICON Q1 FY27, Gupta [page 9]; Bhatnagar [page 10], [page 15] |
| MINOR | R43 Alicon "underlying volume growth about 17.5%" vs tonnage "close to 1% higher" | ALICON Q1 FY27, Bhatnagar, [page 3], [page 14] |
| MINOR | R45 Alicon leadership transition: Q3 call without CEO or CEO designate; succession costs and impairment; plans "have not yielded the results"; Rs 25 to 26 Cr one time costs incl unspecified provisions | ALICON Q3 FY26 [page 2], [page 5], [page 16]; Q4 FY26 [page 11], [page 14], [page 17] |

Verifier B promise delivery spot checks: checked 5, confirmed 4, wrong 1 (row 4). Credibility grade: concur with C; the delivery record is delivered 4, partial 2, missed 0, and five written statements contradicted by the company's own filings (R5 twice, R10, R11, R12) put the C at its low end. Pipeline flags not supported: none.

## Status of the verification set

- Verifier C valuation half: PENDING PHASE 3. B10 and B11 do not exist in phase 1, so valuation rules (0 checked), the expectation ledger (rules 13 to 14), the narrative rule 9, recomputed destination PE and recomputed decision are all unchecked.
- Verifier A shadow: did not run in this session. The single shadow run for 2026-11-15 belongs to the TD Power session; .claude/shadow.yaml was not touched.
- Verifier runs this Phase 1: A 1, B 1, C 1, D 1. Remediation cycles: 0.

## Source fidelity findings and how this synthesis applied them

The three B12a findings with source_fidelity: true are MINOR anchor page findings. The values exist in the documents. They bind, and the synthesis files use the corrected anchors:

| Finding | Corrected anchor used in the final files |
|---|---|
| A-2 vacuum capacity 100 MTPA; vacuum casting since FY18 | CARE rationale p.2 (capacity); p.3 (FY18) |
| A-3 stage 2 AR anchors one page high | AR cash flow p.110, P&L p.108, balance sheet p.107, Note 23 p.126, Cons Note 38 p.173, Notice Item 4 pp.45 and 52, Board report Annexure 5 p.75, Note 2 p.116, Note 11 pp.120 to 121 |
| A-4 aerospace and defence 5.86% | AR p.22 |

Verifier A's arithmetic corrections are used as corrected: India defence production growth 18.8% a year over four years (not 14.8%); net debt ₹67.71 Cr (6,771.24 ₹ lakh); FY25 working capital days 139.14.

Verifier disagreements: none. No downstream step in this synthesis took a position against a Verifier A source fidelity finding.
