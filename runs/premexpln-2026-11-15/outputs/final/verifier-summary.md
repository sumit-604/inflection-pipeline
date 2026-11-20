# PREMEXPLN: verifier summary (phase 1, run 2026-11-15)

## Confidence delta (phase 1)

| Component | Value | Source | Basis |
|---|---|---|---|
| numerical_acceptance | 96 | B12a | 272 numbers checked; mandatory tier 142 of 142; 0 CRITICAL, 1 MAJOR (source_fidelity true), 4 MINOR; 6 false positives struck |
| redflag_coverage | 73 | B12b | material_caught 11 of material_found 15 (CAUGHT only); 32 independent flags listed |
| framework_adherence | 90.1 | B12c | phase 1 portion: 82 of 91 rules (Gate 0 62, Emerging Moat 29); valuation component PENDING PHASE 3 |
| peer_utilisation | NOT APPLICABLE | B12d | 2 of 3 peers substantive (SOLARINDS 4 transcripts, ASTRAMICRO 4, BDL 0); denominator below 4 |
| overall | 73 | confidence.yaml | set by redflag_coverage; band 60-74, PROCEED verdicts downgrade one level |

Acceptance rates: Verifier A 96; Verifier B 73; Verifier C 90.1 (phase 1 portion); Verifier D 100 (2 of 2 peers with transcripts; 67% if BDL is counted).

Each verifier ran once (manifest verifier_runs A 1, B 1, C 1, D 1). Remediation cycles: 0. REWORK triggers: none. Verifier A shadow: skipped (manifest).

Verifier C scope note: the valuation audit (rules_checked 0), the expectation ledger and the business understanding narrative checks are NOT EVALUATED in phase 1; their fields hold template defaults, not findings.

Row labels A-n, B-n and D-n are assigned here in source order for reference; Verifier C IDs are the verifier's own.

## CRITICAL

None. Verifier A 0, Verifier B 0, Verifier C 0, Verifier D 0.

## MAJOR

| Verifier | ID | Location anchor | Note (as written by the verifier) |
|---|---|---|---|
| A | A-1 | 02-notes.md: Top findings rank 3, FLAG-CASH reason, receivables_trend (B02 Pass 3 consolidation) | Claimed receivables over one year 887.36 L (FY25) to 888.35 L (FY26), "nothing collected net". Source: FY26 over one year = 298.38 + 556.28 + 332.07 = 1,186.73 L (AR FY26 Note 11(c) ageing row, p.127, txt line 8311); FY25 over one year = 575.62 + 123.87 + 187.87 = 887.36 L (Note 11(d), p.128); 888.35 L is the over two year sum only. MISMATCH on the FY26 label. Stage 3 and the orchestrator correction already state 1,186.73 L (+33.7%); the B02 report body and YAML still carry 888.35 L. Not a verdict card or Section 1B pillar input, so MAJOR. Gate 0 does not use the figure. source_fidelity: true |
| B | B-1 | B05 0.2 and 2D item 2 | Credit loss provisions and forex losses in earlier quarters' other expenses not captured. MISSED. Anchor Q1 FY27 p4, TVC. Only call evidence on receivable impairment; bears on load bearing fact 2 (cash conversion); amount NOT FOUND in transcripts, read Q4 FY26 results notes and AR |
| B | B-2 | B05 3B pricing bullet and T7; B06 Q3 and 2B | Q3 FY26 claim that escalation clauses protect margin carried as fact; Q1 FY27 says price rises wait until contracts are completed. PARTIALLY CAUGHT, misclassified as industry intelligence. Anchor Q3 FY26 p7, VK/TVC; Q1 FY27 p11, VK; SOLARINDS Q4 FY26 p7-8. Stage 11 margin bridge must not cite escalation clause protection without the contrary Q1 FY27 statement |
| C | C-G03 | B01; rule P01 l.27-31 fixed ROCE formula, P01 l.19-22 NOT FOUND scores 0; claim at 01 l.12, l.31 | Claimed ROCE on proxy capital employed (equity + reserves + borrowings); A4 5, Block A 5, core 53. Recomputed: current liabilities NOT FOUND FY17-FY24, so ROCE NOT FOUND: A4 0, Block A 0, core 48, grand 57; DB1 fires, DB3 not testable; M3 ROCE input open. Operator may rule the proxy acceptable, then A4 5 stands. Decision effect: none; AVERAGE in every reading |
| C | C-G06 | B01; rule P01 l.39-40 FCF = CFO - capex (PPE + intangibles), P01 l.19-22; claim at 01 l.36-37 | Claimed investing cash flow as capex proxy FY17-FY23; B2 2, B3 1, Block B 8. Recomputed: strict NOT FOUND gives B2 0, B3 0, Block B 5, DB2 fires (not binding). Filed years FY24-FY26: B2 2 (2 of 3), B3 5 (131.53 / 102.87 = 1.28), Block B 12. Decision effect: none; core 45-57 across readings, all AVERAGE |
| C | C-E12 | B07; rule P07 l.172-173 evidence multiplier, P07 l.37-38 rule 4, rubric rule 3; claim at 07 l.142, l.201, l.204 | Claimed H2 H x M = 3 x 1.0 = 3.0; em_score 12.3 MODEST. Recomputed: forming advantage (orders, technology, capital) is CLAIM only (07 l.141-142): factor 0.7 gives H2 2.1, em_score 11.4; likelihood M gives 2.0, em_score 11.3. Class NONE. Decision effect: em_classification MODEST to NONE; combined AVERAGE unchanged; Pillar 3 re-check in phase 3 |
| C | C-E13 | B07; rule P07 l.21-24 moats currently forming; claim at 07 l.102, B07 l.51 | Claimed B2 scored 2.1 while described as existing, not new, already present. Recomputed: B2 0, em_score 10.2 NONE; with C-E12, 9.3 NONE. Alternative reading (lock-in not in historical financials, M10 = 1) keeps 2.1. Decision effect: em_classification MODEST to NONE; combined AVERAGE unchanged; KNIFE-EDGE flag (B07 l.13) omits B2 as a swing row |

Verifier C report note on C-E12 (12c-verifier-framework.md l.188): if the factor rates the documented look-for item instead of the load bearing claim, H2 keeps 1.0, A1 and B2 rise to 1.0 (3.0 each), and the total is 14.1, MODEST (derived). The maker declared the load bearing claim method; Verifier C grades against the declared method.

## MINOR

| Verifier | ID | Location anchor | Note (as written by the verifier) |
|---|---|---|---|
| A | A-2 | 05-concall.md: anchors for Q4 FY26 call "Rs 600-700 Cr" and "15-20%" (cited p5), Q1 FY27 call "Q1 only Rs 21 Cr" (cited p6), Q3 FY26 call "targeting Rs 500 Cr" (cited p9) and FY26 export "Rs 40 Cr nine months" (cited p8) | On the transcripts' own "Page n of N" labels the quotes sit on Q4 FY26 p4 (Concall_Jun txt lines 184, 186), Q1 FY27 p5 (Concall_Aug txt line 235), Q3 FY26 p8 (Concall_Feb txt lines 349-356) and p7 (line 316). Every quoted number exists in the source and the values match; the page is off by one on these rows. Weak anchor, not a missing number. source_fidelity: false |
| A | A-3 | 07-emoat.md (CWIP "AR p.110 BS", 2C and F2) and 04-bizmodel.md ("AR p.133 (Note 21)" for sale of services 3,593.78 L and the 34,874.95 + 238.41 + 3,593.78 + 127.00 cross-check) | Balance sheet is on [page 109] (CWIP 2,639.23 L, txt line 6813); p.110 is the P&L. The sale of products/services table is on [page 132] (txt lines 8580-8585). Values match. Wrong page only. Stage 3 anchors these correctly. source_fidelity: false |
| A | A-4 | 03-ardeep.md 2.0 rank 7: "Note 32(B) p.142-143: 94.66 vs 85.58 per USD" | No rate is printed. Implied from the unhedged table: FY26 1,101.50 L / 11,63,707 USD = 94.65; 2,804.73 L / 29,63,126 USD = 94.65; FY25 793.23 L / 9,26,872 USD = 85.58 (txt lines 9052, 9057, 9082). The 10.6% move still holds. Derived figure with no (derived) tag; FY26 rate differs by 0.01. UNANCHORED as printed, immaterial. source_fidelity: false |
| A | A-5 | 01-gate0.md load bearing line 7 and Block A memo: "Other income FY26 Rs 35.93 cr (screener-data), 59% of PBT" set beside note 6 items 3,417.80 L + 500 L | Data_Sheet row 19 col FY26 = 35.93 (matches as labelled). The filing prints consolidated other income 4,214.24 L = Rs 42.14 cr (Q4 FY26 results p.15, txt line 741) and standalone 4,214.49 L (AR p.110). 35.93 reconciles to 4,214.24 less 520.00 ex-gratia, 100.00 accident loss and 1.21 JV loss = 3,593.03 L. Unlabelled basis difference, rated UNANCHORED MINOR because FLAG-GATE0 and FLAG-CASH already fire and B03 carries the filing basis 64.8% / 69.7%. The screener derivation itself is the verifier's inference. source_fidelity: false |
| B | B-3 | B05 2B | Shifting shortfall explanations; Q1 FY27 denial of customer acceptance delay vs Q3 FY26 inspection narrative; MIL reason presented as said before but absent in Q3 FY26. PARTIALLY CAUGHT. Anchor Q3 FY26 p6, p8; Q4 FY26 p5; Q1 FY27 p8-9. Reclassify as cross call contradiction |
| B | B-4 | B05 1C, 2A row 11, 4A P6 | FY27 growth drivers (mines, drone payloads, ammunition) blocked another 6 months; Q3 FY26 said mines already delivering. PARTIALLY CAUGHT, under weighted. Anchor Q4 FY26 p15, p5, p16; Q1 FY27 p6; Q3 FY26 p5, p7. Tie to F1 FY27 guide credibility; absent from 4D |
| B | B-5 | B05 4D F4 | Export "this quarter" figure read against Q2 FY27 revenue. OVERSTATED. Anchor Q1 FY27 p5, Paras Kulkarni / TVC. Question asked about FY27; Q3 FY26 export misstatement is real |
| B | B-6 | B05 4D F8 | Management called the acquisition done before SPA close. OVERSTATED. Anchor Q1 FY27 p3 vs p7, TVC. Same call treats Apollo as pending; rest of F8 supported |
| B | B-7 | B05 2B pattern check | Accident and its cost volunteered in Q4 closing. OVERSTATED. Anchor Q4 FY26 p16 closing; Q3 FY26 p8. Cost was elicited by an analyst; accident volunteered inside a Q4 FY26 p5 answer |
| B | B-8 | B05 2E rows 2 and 3 | Deflected every time (guidance; LD timing). OVERSTATED. Anchor Q3 FY26 p8; Q1 FY27 p5. Guide was cut with reasons; LD window was given; both remain repeated question signals |
| B | B-9 | B06 Q8 net read | BEL QRSAM main order not signed by August 2026; Premier position consistent. OVERSTATED (inference as fact); peer tension MISSED. Anchor ASTRAMICRO Q1 FY27 p6, p13; ASTRAMICRO Q4 FY26 p16; Premier Q1 FY27 p8. Astra transcript does not state the BEL contract status |
| B | B-10 | B05 1C QIP row | QIP not discussed on Q3 FY26 call. MISSED skipped question. Anchor Q3 FY26 p11, Varun Jain / TVC. Fund raise raised, answer on land only |
| B | B-11 | B05 and B06 anchors | Page anchors mix footer and PDF marker bases; several one page off. Weak anchors. Anchor B05 Q3 FY26 p9 (is p8), Q4 FY26 p11 (p10), Q1 FY27 p10 (p9), Q4 FY26 p6 (p5), Q3 FY26 p5 VK (p6); B06 ASTRAMICRO Q1 FY27 p14 (p13). No quote fabricated; anchor fidelity is Verifier A's domain |
| B | B-12 | B05 2A row 5 | July 2023 order remaining value stated four ways; MD/CFO contradiction. MISSED. Anchor Q3 FY26 p10; Q4 FY26 p7; Q1 FY27 p5. Slippage itself caught |
| B | B-13 | B05 3D | Identical explosives and services order books two quarters running. MISSED. Anchor Q3 FY26 p3; Q1 FY27 p3, p8. Ask how the split is built |
| B | B-14 | B05 1C, 2A row 7, 2C | Skipped post board call for land travel; within call capex conflict; Q4 FY26 to Q1 FY27 tone shift. PARTIALLY CAUGHT. Anchor Q3 FY26 p13, p11; Q4 FY26 p2-3, p10; Q1 FY27 p2-3. Presentational |
| C | C-G36 | B01; rule P01 l.120-122 M8 bands; claim at 01 l.69 | Claimed M8 0, evidence "not quantified in inputs". Recomputed 0 (none) or 1 (mentioned, unquantified); stated input does not separate the bands. Decision effect: none; below moat threshold either way |
| C | C-G39 | B01; rule P01 l.129-133 M11 selling leg; claim at 01 l.72 | Claimed M11 5; selling and admin 8.40% to 5.69%, no years. 5 holds only if the selling leg falls across the test windows; years and basis not stated. If it fails, M11 1 or 0, moats present 1, THIN. Decision effect: none; core band governs classification |
| C | C-G54 | B01; rule P01 l.151-154 state which years drive a deal breaker; claim at B01 l.26, 01 l.81, B01 l.41 | Claimed DB1/DB3 driving years FY17-FY23. Recomputed FY18-FY23; FY17 ROCE 16.8% (01 l.16) is not a depressor; B01 l.14 already says FY18-FY23. Decision effect: none; the years feed the post IPO rebase / legacy cleanup override |
| C | C-E15 | B07; rule P07 l.173-174 full scoring table, all 23 rows; claim at 07 l.203 | Scorecard lists 6 rows plus one line for 17 zero rows. List all 23 rows; total unchanged. Decision effect: none |
| C | C-E25 | B07; rule P07 l.201-203, l.208-210 combine with the injected Gate 0 block; claim at 07 l.250-255 | 6E column "Existing (Gate 0)" lists technology qualification, switching costs, licence/regulatory. B01 confirms M3 and M11 only (01 l.75); M6 0, M7 0, M10 1. Relabel to the B04 source or carry the B01 moats. Decision effect: none |
| D | D-1 | ASTRAMICRO-202606-Q4FY26 lines 532-534 | Q1 inspection delay evidence omits Astra Q4 FY26 programme/DRDO delay remarks (lines 532-534, 665); already carried by two Astra anchors, no verdict change |
| D | D-2 | B06 Part 3 | BDL has 0 transcripts; B06 records UNUSED honestly. Corpus gap, not a pipeline miss; buyer side PSU view absent |
| D | D-3 | B06 Q4 net read | Q4 VERIFIED uses 6 anchors across 2 peers but neither sells countermeasures; B06 states this caveat. Acceptable; a PARTIALLY label would also be defensible |

## Verifier B missed list (as written)

| Severity | Item | Anchor |
|---|---|---|
| MAJOR | Expected credit loss provisions and forex losses sat in earlier quarters' other expenses (analyst: Rs 20 Cr to Rs 11 Cr); only call statement on receivable quality; amount NOT FOUND in transcripts; absent from B05 and B06 | Q1 FY27 call 14 Aug 2026, p4, TVC answering Paras Kulkarni |
| MINOR | QRSAM peer tension: Astra says BEL placed FOPM orders on all vendors and Astra holds QRSAM FOPM orders, while Premier (claimed sole propellant source) has no order and says tenders are not called; B06 Q8 calls Premier's position consistent | Premier Q3 FY26 p9 and Q1 FY27 p8, TVC; ASTRAMICRO Q4 FY26 p16, Q1 FY27 p6 and p13 |
| MINOR | Explosives and services order books identical two quarters running (Rs 51.8/51.8 Cr; Rs 42/42 Cr); CFO then calls the non-defence 6% industrial explosives | Q3 FY26 p3, VK; Q1 FY27 p3 and p8, VK |
| MINOR | Board fund raise permission raised by analyst, MD answered on land only; B05 1C says QIP not discussed in Q3 FY26 | Q3 FY26 p11, Varun Jain / TVC |
| MINOR | July 2023 order remaining value stated four ways (Rs 110-112 Cr; Rs 60 Cr flare part; little portion; Rs 75 Cr); MD and CFO contradicted each other on whether stock awaiting inspection was included | Q3 FY26 p10, TVC/VK; Q4 FY26 p7, VK; Q1 FY27 p5, VK |

Verifier B: pipeline flags not supported, none (four B05 statements and one B06 statement OVERSTATED, rows B-5 to B-9). Promise delivery spot checks 5 of 5 confirmed. Credibility grade: concur, D.

Verifier D: substantive_unsupported none; claims_all_addressed true; verdict_discipline_fails none. Unused but relevant: ASTRAMICRO Q4 FY26 programme delays "for various reasons as these are all government-" and DRDO order delays question (lines 532-534, 665), supportive of the cited inspection slip read.
