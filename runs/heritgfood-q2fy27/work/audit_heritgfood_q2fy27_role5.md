# A5 ADVERSARY AUDIT: Heritage Foods (HERITGFOOD) Q2 FY27, Role 5 concall addendum, loop 2 final re-audit

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-20 | loop: role5-loop2 (final; no further loop follows)
Review under audit: runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md (1,730 lines; Role 5 section R-L835-1332; brief R-L1365-1438; YAML R-L1442-1619; Role 5 loop 2 disposition R-L1712-1730)
Prior audits re-checked: work/audit_heritgfood_q2fy27_role5_run1.md (F1, M1-M4, C1, C2; S1-S8) and work/audit_heritgfood_q2fy27_role5_loop1.md (M-A, M-B, M-C, C-A, C-B; S-1 to S-7)
Inputs read: A1 concall fulltext CC-L1-853 in full (header turn map, then body CC-L130-853 line by line); A1 concall structured file in full (R001-R336); A2 concall ledger count test and Sections 9, 10 and 10B (M01-M61) in full; count-test headers of the results, presentation and release ledgers; results fulltext L117-126, L400-431, L460-471; presentation fulltext P-l255-302 (slide 9); press release fulltext PR-L68-147; the A4 review in full for the Role 5 section, Step 8, Step 8.5, Monitorables, flags, brief, YAML and the disposition tables; work/blocks/a4-role5-loop2.yaml and a grep of work/blocks/. No source file and nothing under inputs/ was opened.
Scope: the Role 4 body was audited COMPLETE in loop 2. This audit covers the Role 5 section, every line the Role 5 loop 1 and loop 2 dispositions name, and the resolution of every earlier Role 5 finding.

Anchors: "CC-L###" = concall fulltext line. "R-L###" = current review line. "L###" = results fulltext line. "P-l###" = presentation fulltext line. "PR-L###" = press release fulltext line. "LG-L###" = concall ledger line. "BLK-L###" = line of work/blocks/a4-role5-loop2.yaml.

---

## EARLIER FINDING RESOLUTION

| Finding | Type | Status now | Evidence |
|---|---|---|---|
| Run1 F1 curd run-rate | FACTUAL | RESOLVED | Two readings, curd-quarterly working reading: R-L840, R-L1028, R-L1090, R-L1236-1237, R-L765, R-L1406, YAML. 125 t now correct (R-L1090). |
| Run1 M1 spine U1-U10 | MISSING (A2) | RESOLVED | M01-M10, LG-L526-540. |
| Run1 M2 FC-1 two readings | MISSING | RESOLVED | R-L1188, R-L1224, R-L776, R-L1280, R-L1329, R-L1347, YAML. |
| Run1 M3 slide 9 second reading | MISSING | RESOLVED | R-L961, R-L1049, R-L1248, R-L762, R-L1351, R-L1382. |
| Run1 M4 KMF procurement fork | MISSING | RESOLVED | R-L772, R-L814, R-L701, R-L1278, R-L1419, R-L1430. |
| Run1 C1 R236 voice | CONTRADICTION | RESOLVED | R-L1141; ledger LG-L350 re-flag. |
| Run1 C2 merge-pending YAML | CONTRADICTION | RESOLVED in the review (R-L1450). The run1 block work/blocks/a4-role5.yaml still reads "pending" (loop-1 S-7, still open, STYLE S2-4). |
| Loop1 M-A spine V1-V22 | MISSING (A2) | RESOLVED for V1-V22 (M11-M32, LG-L542-566). A2's closing sweep added M33-M61 and declared the ledger closed (LG-L568-569). My fresh pass finds 22 more units (finding M2-2). |
| Loop1 M-B reading-2 step sensitivity | MISSING | RESOLVED. September-step and rising-step results at R-L961, R-L1049, R-L1248, R-L762, R-L1351, R-L1382, YAML F12, analyst note. Arithmetic ties (table below). One wording defect in the brief (F2-2). |
| Loop1 M-C floor need across the range | MISSING | RESOLVED. R-L962, R-L763, R-L1352, R-L1383, YAML F13. All eleven points tie. New qualifier gap on the flat path (M2-3). |
| Loop1 C-A ledger counts | CONTRADICTION | RESOLVED for M01-M32: 397 rows, split 197/57/65/29/49 (R-L23, R-L846, YAML); "until it lands" gone; C5, C6 and R236 attributed to A2 and marked corrected (R-L846, R-L1141). Residual: M33-M61 enter the total but not the 6B count (F2-1), and the status fields disagree (C2-1). |
| Loop1 C-B 8C direction | CONTRADICTION | RESOLVED. R-L1256, R-L1317, R-L1330, YAML R-L1599. |
| Loop1 S-1 to S-6 | STYLE | APPLIED. R-L1140, R-L10, R-L1090, R-L945, R-L762, R-L874. |
| Loop1 S-7 | STYLE | NOT APPLIED (block file outside the review). Logged again as S2-4. |

---

## DELIVERABLE-COMPLETENESS AUDIT (gate)

| Brief part | Heading (review line) | Status |
|---|---|---|
| 1. Summary narrative | R-L1369 | PRESENT. 18 lines (R-L1371-1388), inside the 10-20 line band. One misattributed path range at R-L1382 (F2-2). |
| 2. Sector intelligence | R-L1390 | PRESENT. Seven bullets (R-L1392-1398). |
| 3. Business-model intelligence | R-L1400 | PRESENT. Nine bullets (R-L1402-1410). |
| 4. Competition intelligence | R-L1412 | PRESENT. Seven bullets (R-L1414-1420). |
| 5. Forward map | R-L1422 | PRESENT. Make-or-break line (R-L1424) plus 11 dated rows (R-L1428-1438), each with a bull fork and a bear fork. |

Gate: PASS. All five parts exist and carry real content.

---

## COVERAGE AUDIT

Fresh pass: I read CC-L130-853 line by line and listed every unit under the class rule A2 adopted for its closing sweep (LG-L568): NUMBER = stated number, or stated direction or level of a named metric; FORWARD = expectation, intent or conditional; ENTITY = person, firm, place, channel, pack type; DATE = named period or horizon, analyst horizons included; QUALIFIER = decline, refusal or data caveat. I diffed the list against R001-R336 and M01-M61. I followed A2's exclusions: greeting, programme and narrative lines, and clause-level restatements inside a row's sentence. Each unit below has a named analog row of the same class.

| Category | A2 count (closed ledger) | Fresh count | Orphan rows (ledger rows A4 marks not reviewed) | Status |
|---|---|---|---|---|
| Turns | 81 | 81 | none | PASS |
| Analyst questions | 24 | 24 | none | PASS |
| NUMBER | 197 | 211 | M33-M36, M39, M40, M44-M55 (18) | FAIL: 14 units missing; 18 orphans |
| ENTITY | 57 | 58 | M56 | FAIL: 1 unit missing; 1 orphan |
| FORWARD | 65 | 69 | M41-M43 | FAIL: 4 units missing; 3 orphans |
| DATE | 29 | 32 | M57-M61 | FAIL: 3 units missing; 5 orphans |
| QUALIFIER | 49 | 49 | M37, M38 | FAIL: 2 orphans (count PASS) |
| Total rows | 397 | 419 | M33-M61 (29) | FAIL (A3 orphans; A2 missing units) |

Ledger arithmetic re-checked: M11-M32 = NUMBER 10, ENTITY 3, FORWARD 2, DATE 2, QUALIFIER 5; M33-M61 = NUMBER 18, FORWARD 3, DATE 5, QUALIFIER 2, ENTITY 1; split 162+7+10+18 = 197, 52+1+3+1 = 57, 60+2+3 = 65, 20+2+2+5 = 29, 42+5+2 = 49; total 336 + 61 = 397 (LG-L14-16). Filed-document ledgers unchanged: results 1,242, presentation 651 + 45 slides = 696, release 180, orphan_ids [] in each header.

### Orphan rows (finding M2-1)

The review states that M33-M61 "landed after A4 wrote loop 2 and are not reviewed by A4 [orchestrator note; open item OI-1]" (R-L23, R-L846, R-L1361, R-L1462, R-L1583). That is an explicit not-reviewed mark, the opposite of "reviewed, no finding". All 29 rows are orphans under the protocol.

What my check of the body shows:
- The five MATERIAL rows are already cited in substance. M33 at R-L921 (Step 1 row 22, CC-L229-230) and R-L1135. M35 verbatim at R-L1062. M39 inside CQ12 (R-L1018, CC-L508-528) and 5A row 13 (R-L1089, CC-L522-531). M47 inside CQ20 (R-L1026, CC-L662-688, "18-month supply gap"). M53 verbatim at R-L1190 (7A, CC-L727-733).
- Most minor rows fall inside a cited CC-L range (CQ01, CQ07, CQ12, CQ14, CQ15, CQ20, CQ24, 5A row 20).
- Four rows have no cite at all: M56 (CC-L388), M58 (CC-L274-275), M60 (CC-L750-751), M61 (CC-L636-637). M57 is cited only at CC-L429, the last line of CQ07's range.
- One number moves: M41, M42 and M43 are management FORWARD rows (T045, CC-L554, CC-L557-558, CC-L562-563), none quantified. 6B leaves them out (finding F2-1).
- I found no new forensic signal in M33-M61 beyond the 6B count.

### Units the closed ledger lacks (finding M2-2)

| Y | Fulltext line | Turn | Verbatim unit | Type (analog row) | Material? A4 use |
|---|---|---|---|---|---|
| Y1 | CC-L441-443 | T028 | "We organize a lot of third-party lending to meet with their working capital needs, as well as to help them purchase more animals" (restated CC-L822-824, T078, "like I said earlier"; CC-L306-309, T006, "tying up with the funds") | NUMBER, unquantified level of a named activity (M18) | MATERIAL: CC-A3-14 rests on it; Q41 (R-L768), 5A row 20 (R-L1096), F15 (R-L1354), M10 (R-L807), brief part 3 (R-L1409) |
| Y2 | CC-L816-817 | T078 | "we supply subsidized cattle feed very conveniently to them" | NUMBER, unquantified price level (M18) | MATERIAL: Q41 (R-L768), 5A row 20 (R-L1096), brief part 3 (R-L1409) |
| Y3 | CC-L393 | T022 | "In the month, in this quarter, we saw two significant events" | DATE, named period of the Aavin farm steps (R288) | MATERIAL: Step 2 dating caveat (R-L961), 5A row 12 (R-L1088) |
| Y4 | CC-L651-654 | T062 (analyst Q20) | "the cow milk has been more inflationary versus the buffalo milk" | NUMBER, unquantified, ANALYST_STATED (R091) | MATERIAL: quoted in Exchange 2 (R-L1053); an analyst's reading of slide 9 that management did not correct |
| Y5 | CC-L183 | T003 | "milk procurement inflation remains elevated across the country" | NUMBER, unquantified level (M05) | minor; 6C note (R-L1163) |
| Y6 | CC-L185-186 | T003 | "driven by sustained demand, limited improvement in milk arrivals and higher feed and fodder costs" | NUMBER, unquantified directions (M15) | minor; the release text (PR-L77-78) is cited in brief part 2 |
| Y7 | CC-L187-188 | T003 | "These pressures continue to weigh on near-term profitability across the dairy industry" | NUMBER, unquantified direction (M08) | minor; Step 1 row 11 (R-L910) |
| Y8 | CC-L195-196 | T003 | "Our focus remains on balancing volume growth with calibrated pricing while protecting the strength of our consumer franchise" | FORWARD, management intent (R219) | minor; enters 6B as unquantified |
| Y9 | CC-L225-226 | T003 | "nutrition-led categories with attractive long-term growth potential" | FORWARD, management expectation (M43) | minor; enters 6B as unquantified |
| Y10 | CC-L286 | T006 | "situation could be difficult in the coming months" | DATE, horizon (M14) | minor |
| Y11 | CC-L316 | T007 (analyst Q02) | "this 32% growth" | NUMBER, ANALYST_STATED restatement (R116, R139) | minor |
| Y12 | CC-L324-328 | T008 | metro rainfall "normal or even above normal"; Bangalore and Mumbai "more than normal rainfall" | NUMBER, unquantified level (M13) | minor; CQ02 (R-L1008) |
| Y13 | CC-L378 | T015 (analyst Q04) | "So in Q3 we are expecting softer than that" | FORWARD, ANALYST_STATED (R235) | minor; analyst voice, outside 6B |
| Y14 | CC-L422-423 | T026 | "the percentage of our premium portfolio contribution is going up" | NUMBER, unquantified direction (M17) | minor |
| Y15 | CC-L466-467 | T031 (analyst Q09) | "it could only be normalizing post-agorn monsoon" | DATE, analyst horizon, ASR (M09) | minor |
| Y16 | CC-L473-474 | T032 | "So, we will continue to do this." | FORWARD, management intent (R242) | minor; enters 6B as unquantified |
| Y17 | CC-L506-507 | T040 (analyst Q12) | "near zero price increases" | NUMBER, ANALYST_STATED (R072) | minor; CQ12 (R-L1018) |
| Y18 | CC-L510 | T041 | "rural Andhra" | ENTITY, place (R206); inside the M21 caveat | minor |
| Y19 | CC-L673 | T063 | "Protein is also lower" (cow vs buffalo) | NUMBER, unquantified comparative (M04) | minor |
| Y20 | CC-L718 | T070 | "It's growing on a quarterly basis" (paneer) | NUMBER, unquantified direction (M17) | minor |
| Y21 | CC-L742-743 | T075 (analyst Q24) | "maintain a McTean's revenue value world" [read as mid-teens revenue growth; INFERENCE: ASR] | NUMBER, ANALYST_STATED, ASR_GARBLE (R145) | minor |
| Y22 | CC-L840-841 | T078 | "all payments happen online at the farmer level" | NUMBER, stated level of 100% (R095) | minor |

Units checked and ruled out as covered: CC-L806 (R272 context names procurement security), CC-L485 Q2-over-Q1 leverage (R245), CC-L471 (quantified by R087/R088), CC-L404-407 (R309, R289), CC-L416 (M36 sentence), CC-L532 (restates R095). Borderline and not counted: CC-L242-243 (NutriVate "increasing contribution"), CC-L283-285 (north and south states, floods, drought), CC-L559-561 (fresh category "humongous", packaged dairy "a minute fraction"), CC-L834 ("a lot of social security programs").

A4 cites all four material units (Y1-Y4) straight from the fulltext. The review therefore drops nothing of substance. The spine is still open one level up. This is the third pass under this class rule (run1 10 units, loop1 22, A2's sweep 29, now 22), so the rule as worded does not converge. Analyst-stated restatements and unquantified directions keep surfacing on each pass.

---

## ARITHMETIC AUDIT

Every derived number that Role 5 loop 2 added or changed, plus the numbers behind this audit's findings, recomputed from the extracts.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Slide 9 reading B blend Jul/Aug/Sep (0.8 x lower + 0.2 x upper) | 42.216 / 42.814 / 43.514 (disposition R-L1720) | 0.8 x 39.51 + 0.2 x 53.04 = 42.216; 0.8 x 40.07 + 0.2 x 53.79 = 42.814; 0.8 x 40.73 + 0.2 x 54.65 = 43.514 | P-l276-288 | PASS |
| Reading B monthly steps Jul/Aug/Sep | +0.20, +0.60, +0.70 | Jun 42.014: +0.202, +0.598, +0.700 | P-l276-288 | PASS |
| Reading A blend and steps | 50.334 / 51.046 / 51.866; +0.30, +0.71, +0.82 | Jun 50.036: +0.298, +0.712, +0.820 | P-l276-288 | PASS |
| Q2 averages and add-ons | B 42.85, add-on 4.88; A 51.08, add-on -3.35 | 128.544 / 3 = 42.848; 47.73 - 42.848 = 4.882; 153.246 / 3 = 51.082; -3.352 | PR-L76 | PASS |
| Reading B YoY rupee change vs landed | +4.92 vs +4.74 | prior-year B Jul 37.336, Aug 37.909, Sep 38.550 (values / (1 + YoY)); average 37.932; 42.848 - 37.932 = 4.916 | P-l270-283, PR-L77 | PASS |
| Q3 flat at September | 48.40 (+6.3%); 48.51 (+6.5%) | 48.396 / 45.55 = +6.25%; 48.514 = +6.51% | CC-L621 | PASS |
| Q3 Jul-Sep average step | 49.69 (+9.1%); 50.05 (+9.9%) | 43.514 + 1.298 + 4.882 = 49.694; 51.866 + 1.532 - 3.352 = 50.046 | derived | PASS |
| Q3 September step | 49.80 (+9.3%); 50.15 (+10.1%) | 43.514 + 1.400 + 4.882 = 49.796; 51.866 + 1.640 - 3.352 = 50.154 | derived | PASS |
| Q3 rising step | 50.14 (+10.1%); 50.51 (+10.9%) | B steps 0.802/0.904/1.006, average level 45.254 + 4.882 = 50.136; A steps 0.928/1.036/1.144, 53.866 - 3.352 = 50.514 | derived | PASS |
| Step needed for 11% | +1.08 (1.67x), +1.02 (1.34x) avg; 1.55x, 1.25x Sep | (45.678 - 43.514) / 2 = 1.082; / 0.649 = 1.67; / 0.700 = 1.55; (53.912 - 51.866) / 2 = 1.023; / 0.766 = 1.34; / 0.820 = 1.25 | derived | PASS |
| October landed level (Q35) | Rs 48.4-49.5 on every path | B 48.40, 49.05, 49.10, 49.20, 49.48; A 48.51, 49.28, 49.33, 49.44, 49.54 | derived | PASS |
| Rs 1/L of landed cost a quarter | Rs 15.90 Cr; 1.20% | 17.28 lakh L x 92 = 158.976 m L = Rs 15.898 Cr; / 1,319.58 = 1.205% | PR-L121, L407 | PASS |
| Floor need across paths | 0.8-0.9%; 2.4-2.8%; 2.5-2.9%; 2.9-3.3%; 3.1%; 3.4%; 2.7-3.4% | (cost - 47.73) x 15.898 / 1,319.58: 48.40 0.81% (Rs 10.65 Cr); 48.51 0.94% (Rs 12.40 Cr); 49.69 2.36%; 50.05 2.80%; 49.80 2.49%; 50.15 2.92%; 50.14 2.90%; 50.51 3.35%; 50.29 3.08% (Rs 40.70 Cr); 50.56 3.41% (Rs 44.99 Cr); 50.00 2.73% (Rs 36.09 Cr) | PR-L121, L407 | PASS |
| 8C Q3 YoY cost paths vs Q2 | +6.3% to +11.0% (+Rs 2.85 to +5.01); Q2 +11.03% (+Rs 4.74) | 48.40 / 45.55 = +6.26%, +2.85; 50.56 / 45.55 = +11.00%, +5.01; 47.73 / 42.99 = +11.03%, +4.74 | PR-L76-77, CC-L621 | PASS |
| 8C QoQ cost | Rs 0.67-2.83/L above Q2 | 48.40 - 47.73 = 0.67; 50.56 - 47.73 = 2.83 | PR-L76 | PASS |
| Gross-margin YoY gap; H2 FY26 | -271 bps; 22.71% | Q2 FY27 materials (9,505.12 + 326.12 + 483.18) / 13,195.80 = 78.165%; Q2 FY26 (7,480.10 + 247.72 + 666.74) / 11,125.17 = 75.456%; gap -270.9 bps; H2 FY26 (34,652.78 - 17,056.05) / (45,259.91 - 22,492.72) = 77.288%, GM 22.71% | L407, L411-413 | PASS |
| 8C base effect at the 11% path (not computed by A4) | "holds or narrows" | Same materials-ratio change as Q2 (x 1.0359) on the H2 FY26 proxy base 77.288% gives 80.062%, a gap of about -277 bps, about 6 bps wider than -271 [INFERENCE: Q3 FY26 single quarter ND] | L407, L411-413 | STYLE S2-2 |
| 6B specificity | 16/59 = 0.27; stricter 0.25, 0.22; 18/59 = 0.31 with festival anchors, "just above 0.3" | Closed ledger adds three management FORWARD rows, all unquantified: M41, M42, M43 (T045). 16/62 = 0.258; 14/60 = 0.233; 12/58 = 0.207; 18/62 = 0.290, below 0.3. With Y8, Y9, Y16 also counted: 16/65 = 0.246; 18/65 = 0.277 | LG-L579-581; R-L1141-1143 | FACTUAL F2-1 |
| Concall rows reviewed by A4 | 368 of 397 | 336 + 32 = 368; 397 - 368 = 29 (M33-M61) | LG-L22 | PASS |
| A4 block row count | "397 # R001-R336 plus M01-M32" (BLK-L20, BLK-L141) | 336 + 32 = 368, not 397 | BLK-L20, BLK-L141 | CONTRADICTION C2-1 |
| Brief part 1 reading-2 range on the average step | "Rs 48.4-50.1 if the monthly rise holds at its Jul-Sep average" (R-L1382) | Average step gives Rs 49.69-50.05; Rs 48.40-48.51 is the flat path (as R-L961 and the analyst note R-L1617 state) | derived | FACTUAL F2-2 |
| Dairy subsidiaries' segment result (5F, probe) | H1 FY27 -Rs 3.15 Cr; Q2 -Rs 2.05 Cr | L468 813.83 - L125 845.31 = -31.48 m; 438.07 - 458.58 = -20.51 m | L125, L468 | PASS |
| Get-A-Way supply at Rs 200/L | Rs 6.0 Cr a quarter; Rs 23.9 Cr a year | 3,272 x 92 x 200 = Rs 6.02 Cr; x 365 = Rs 23.89 Cr | CC-L231, CC-L427 | PASS |
| Curd run-rate shares; peak-day volume | 81-86%; 40-42%; 71%; 125 t | 1,750-1,860 / 2,163.2 = 80.9-86.0%; 870-900 / 2,163.2 = 40.2-41.6%; 320 / 451.0 = 71.0%; 3,200 m / 70 / 365 = 125.2 t | CC-L715-719, PR-L92, PR-L136 | PASS |
| Feed result margin | 3.91% vs 9.03%; +162 bps QoQ | 33.29 / 852.50 = 3.905%; 52.50 / 581.12 = 9.034%; 16.68 / 728.67 = 2.289% | L463, L470 | PASS |

No mismatch above rounding in A4's own sums. The failures are a stale denominator (F2-1), a misattributed path (F2-2) and a block-copy count (C2-1).

---

## ADVERSARIAL READ

The three most positive claims in the Role 5 section after loop 2, each with the strongest bear counter from the same extracts.

P1. Gross-margin direction on cost: "On cost evidence alone, the call does not move the seed gross-margin item toward its red side ... On the same YoY price rise, the YoY gap holds or narrows" (8C, R-L1256; Concall Verdict R-L1317; combined verdict R-L1330; YAML R-L1599). This is the most bull-leaning sentence that loop 2 added.
- Bear counter: at the 11% path the rupee step is +Rs 5.01/L, above Q2's +Rs 4.74/L. The comparison base is also weaker. In FY26 the H2 materials share was 77.29% against 75.46% in Q2 (L407, L411-413). The same proportional cost-to-price change on that base gives about -277 bps, about 6 bps wider than -271 [derived; INFERENCE, H2 FY26 used as the proxy because Q3 FY26 is ND]. Q2 FY27 also carried a Rs 48.32 Cr stock drawdown (L413).
- Survives? No, not as a material counter. Six bps is inside what "holds" means on an ND base. 8C already makes the YoY direction depend on the unquantified Q3 price step and on the drawdown (Q34). Logged as STYLE S2-2.

P2. Bull end of the floor test and low end of reading 2: "about 0.8-0.9% if cost holds at the September level (Rs 48.40-48.51/L)" (R-L962); "Reading 2 puts Q3 at Rs 48.4-50.1/L on the flat and Jul-Sep average-step paths, nearer 'not 47 to 50'" (R-L961). The same paths appear in Exchange 1 (R-L1049), 8A (R-L1248), Q35 and Q36 (R-L762-763), F12 and F13 (R-L1351-1352), brief part 1 (R-L1382-1383, "about 0.8-3.4%"), YAML F12/F13 and the analyst note.
- Bear counter: management already reported "slight increase of procurement prices in October compared to September" (CC-L375). Cost has therefore not held at the September level. A Q3 average at the September level needs November and December below September. That is the post-Diwali cooling and buffalo flush that management only "hopes" for (CC-L372-374, CC-L382-383) and declined to forecast ("The only thing we are not willing to speculate is if the raw milk prices will come down in the flush", CC-L605; CC-L486-487). A4 itself wrote in its loop-1 disposition that "The flat-at-September path does not expect a rise" (R-L1698). Its Step 2 names only the continued-step path and reading 1 as fitting the October point (R-L961). Yet the flat path still sets the low end of the range, the floor's bull end and the brief figure with no qualifier.
- Survives: YES. Graft a qualifier at each location: the flat path (Rs 48.40-48.51/L; floor need 0.8-0.9%) needs November-December cost below September to offset the October rise already reported (CC-L375). It rests on the hoped-for flush (CC-L372-374; M25) [derived; MGMT, ASR]. Finding M2-3. The numbers stay.

P3. Price ratchet: "The asymmetry is the bull case: each Rs 1/L fall in landed cost adds about 1.2% of revenue to margin if consumer prices hold" (Exchange 3, R-L1065).
- Bear counter: (a) the ratchet evidence is an observation, not a policy: "at least we have not seen it coming down" (CC-L411-412, ledger M35). (b) Management caps the upside: if milk falls, "the margins will go back to our steady-state levels" (CC-L738-739). (c) Liquid milk "cannot go up by 11%" (CC-L784-786), and "our bottom line is suffering whenever there is a raw milk price increase" (CC-L798-799). (d) The down-cycle depends on cooperatives, which management refused to discuss (CC-L492-497). (e) The sensitivity is overstated: Rs 0.5/L is 0.60% of revenue on filed volume, not 0.7% (FC-4).
- Survives? Already in A4: Step 2 EBITDA row (R-L944, steady state), Exchange 3 "Bull claim, untested" with the cooperative caveat (R-L1065), FC-4 (R-L1227), 8D single-credit rule (R-L1266), Q51 (R-L778). No graft needed.

Mandatory acquisition-economics probe. The call describes holdings: "Getaway, in which we now hold 71 percent stake, delivered robust revenue growth" and "Heritage Novandee Foods now a wholly owned subsidiary" (CC-L229-233).
- Multiple: consideration is NOT FOUND in any extract. Target earnings are negative. Dairy subsidiaries' segment result is H1 FY27 -Rs 3.15 Cr and Q2 -Rs 2.05 Cr (L468 minus L125, recomputed). Price / target PAT = NOT FOUND / negative, so no positive multiple exists. ROCE, debt, cash and customer tenure: NOT FOUND.
- From the call: "robust revenue growth" is unquantified (ledger M33, a row A4 has not marked reviewed). Heritage makes 3,272 L/day of ice cream for Get-A-Way, about Rs 6.0 Cr a quarter at Rs 200/L [derived; transfer price NOT FOUND], so part of Get-A-Way's growth is Heritage-made product.
- Bear reading: more of a loss-making asset was bought at an undisclosed price. It is already in A4 (Step 5F, Q32, Q39, Q42, F5). No "cheap, accretive" claim exists to stress. No graft.

Symmetry check on a bear-leaning reading (CLAUDE.md Rule J): the curd-quarterly working reading (R-L1090) leaves Rs 73.5-81 Cr a quarter of the Rs 451.0 Cr VAP line for ice cream, lassi, buttermilk, yogurt and the rest (451.0 - 320 - 50 to 57.5) [derived]. Own ice cream at Rs 170-180 Cr a year averages Rs 42.5-45 Cr a quarter (CC-L771-772). The residual is tight but positive, so reading 1 survives its own cross-check. No finding.

---

## FINDINGS (tagged)

M2-1. MISSING (orphan rows). Loop: A3 under the protocol rule for an unreviewed row. The work is a review mark, plus the 6B recount (F2-1).
Gap: A4 marks M33-M61 (29 rows; MATERIAL M33, M35, M39, M47, M53) as not reviewed (R-L23, R-L846, R-L1361, YAML R-L1462, R-L1583). The protocol needs each ledger row cited or marked "reviewed, no finding". My check finds the five material rows already cited in substance (R-L921, R-L1062, R-L1018, R-L1089, R-L1026, R-L1190). Four rows carry no cite at all: M56, M58, M60 and M61.
Fix: mark each of M33-M61 cited (with the R-L lines above) or "reviewed, no finding". Count M41-M43 in 6B. No new forensic signal was found.

F2-1. FACTUAL. Loop: A4.
Gap: 6B scores specificity on 59 management FORWARD rows (R-L1141-1143). The closed ledger the section names ("A2 FORWARD rows", 65) holds three more management FORWARD rows: M41, M42 and M43 (T045, all unquantified). The ratio is 16/62 = 0.26, not 0.27. The stricter counts are 0.23 and 0.21. With the festival anchors it is 18/62 = 0.29, below 0.3. The review says "0.31, just above 0.3". The lower 6E row and "below 0.3 under the stated rule" both hold. If Y8, Y9 and Y16 also land, the ratio is 16/65 = 0.25 (0.28 with anchors).
Fix: restate 6B (R-L1141-1143), 6E (R-L1174), the Concall Verdict (R-L1315), F17 (R-L1356), the R-L846 sentence on which M-rows enter 6B, and YAML F17, specificity_ratio and archetype_6e.

F2-2. FACTUAL. Loop: A4.
Gap: brief part 1 says "Q3 at Rs 48.4-50.1 if the monthly rise holds at its Jul-Sep average" (R-L1382). The average step gives Rs 49.7-50.1. Rs 48.4-48.5 is the flat path. Step 2 (R-L961) and the analyst note (R-L1617) state it correctly. The operator reads the brief first.
Fix: "Q3 at Rs 48.4-50.1 if the monthly rise stops or holds at its Jul-Sep average", with the M2-3 qualifier on the flat end.

M2-3. MISSING (surviving bear counter P2). Loop: A4.
Gap: the flat-at-September path sets the low end of reading 2 (Rs 48.40-48.51/L) and the floor's bull end (0.8-0.9%). It carries no qualifier, although management reported October above September (CC-L375). A4's own loop-1 disposition says this path "does not expect a rise" (R-L1698). A flat Q3 average needs November-December below September, which rests on the hoped-for flush that management would not forecast (CC-L372-374, CC-L605).
Fix: add the qualifier at R-L961, R-L962, R-L1049, R-L1248, R-L762, R-L763, R-L1351, R-L1352, R-L1382-1383, YAML F12, YAML F13 and the analyst note, tagged [derived; MGMT, ASR]. No number changes.

M2-2. MISSING (spine). Loop: A2.
Gap: 22 fresh-pass units (Y1-Y22, Coverage Audit) are absent from the structured file and from the ledger, which declares itself closed (LG-L569). Four are material: facilitated third-party lending (CC-L441-443), subsidised cattle feed (CC-L816-817), the "in this quarter" dating of the Aavin steps (CC-L393), and the analyst's cow-more-inflationary reading of slide 9 (CC-L651-654). A4 cites each of the four by CC-L, so the review drops nothing of substance.
Fix: append Y1-Y22 as M62-M83, or record them as an open spine gap. Three management FORWARD units (Y8, Y9, Y16) would also enter 6B (F2-1).

C2-1. CONTRADICTION. Loop: A4.
Gap: the review's ledger status disagrees with itself and with A4's block:
(a) YAML ledger_reconciliation.all_reviewed: true (R-L1464) against role5.ledger all_reviewed: false, unreviewed_by_a4 M33-M61 (R-L1583).
(b) "Every ledger row was reviewed against the fulltext ... concall 368 of 397 rows" (R-L23).
(c) "No orphan IDs (A5 role5-loop1 orphan check)" (R-L846). That check predates M33-M61.
(d) "all four ledgers reconciled" (R-L1361) while 29 rows are open.
(e) A4's own block work/blocks/a4-role5-loop2.yaml says concall_rows "397 # R001-R336 plus M01-M32" (BLK-L20; 336 + 32 = 368), addendum_rows "M01-M32" and all_reviewed: true twice (BLK-L22, BLK-L141). The review's YAML says M01-M61 and M33-M61 unreviewed.
Fix: one status in all places: concall 368 of 397 reviewed, M33-M61 open, all_reviewed false. Align the block copy, or replace it after M2-1 closes.

---

## VERDICT

INCOMPLETE.
- Failing agents, in sequence: A2 (M2-2), then A3 (M2-1, under the protocol rule), then A4 (F2-1, F2-2, M2-3, C2-1).
- Finding types: FACTUAL 2, MISSING 3, CONTRADICTION 1. STYLE 4 logged.
- All earlier Role 5 findings are resolved (run1 F1, M1-M4, C1, C2; loop1 M-A, M-B, M-C, C-A, C-B). A4's new arithmetic ties to rounding throughout.
- This is the final loop. The open items above go to the operator as flags, not to a further re-run.
- The protocol verdict PROCEED WITH FLAGS and cash conversion INDETERMINATE are not at stake. No fix touches a filed number. The 6E row, IC-1 and both Q3 cost readings stand.

---

## STYLE NOTES (logged, no loop)

- S2-1. "The rise grew each month to September" (R-L1382) and "the step rose each month to September" (analyst note, R-L1617). This is true within Q2: on reading B the steps were Jul +0.20, Aug +0.60, Sep +0.70. It is not true from April: May +0.33, Jun +0.33, then Jul +0.20 on B; +0.65, +0.35, +0.30 on A. Say "each month from July to September".
- S2-2. 8C "the YoY gap holds or narrows" (R-L1256). At the 11% path the higher FY26 H2 materials base gives about -277 bps on an unchanged proportional change, about 6 bps wider [INFERENCE; Q3 FY26 ND]. Optional qualifier: "holds (within about 6 bps at the 11% path) or narrows".
- S2-3. Provenance: R-L23, R-L846, R-L1361, R-L1462, R-L1583 and R-L1714 carry text entered by the orchestrator ("[orchestrator note; open item OI-1]", "entered by the orchestrator"). BLK-L8 says A4's 44 edits were "applied by the orchestrator". The OI-1 text is accurate. The review is no longer A4's text alone; keep the labels.
- S2-4. Loop-1 S-7 remains open: work/blocks/a4-role5.yaml (run1) still reads merge "pending" with no superseded header.

---

```yaml
stage: A5-adversary
company: "HERITGFOOD"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: "role5-loop2"
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows:
    - "M33-M61 (29 rows; MATERIAL M33, M35, M39, M47, M53): A4 marks them not reviewed (R-L23, R-L846, R-L1583). Material ones are cited in substance (R-L921, R-L1062, R-L1018, R-L1089, R-L1026, R-L1190). No cite at all: M56 CC-L388, M58 CC-L274-275, M60 CC-L750-751, M61 CC-L636-637"
  missing_from_ledger:
    - "Y1 CC-L441-443 T028 NUMBER-unquantified 'a lot of third-party lending' (restated CC-L822-824, CC-L306-309) (MATERIAL)"
    - "Y2 CC-L816-817 T078 NUMBER-unquantified 'we supply subsidized cattle feed' (MATERIAL)"
    - "Y3 CC-L393 T022 DATE 'in this quarter, we saw two significant events' (Aavin steps) (MATERIAL)"
    - "Y4 CC-L651-654 T062 NUMBER-unquantified ANALYST_STATED 'cow milk has been more inflationary versus the buffalo milk' (MATERIAL)"
    - "Y5 CC-L183 T003 NUMBER-unquantified 'milk procurement inflation remains elevated across the country'"
    - "Y6 CC-L185-186 T003 NUMBER-unquantified cost drivers: sustained demand, limited arrivals, higher feed and fodder"
    - "Y7 CC-L187-188 T003 NUMBER-unquantified 'pressures continue to weigh on near-term profitability across the dairy industry'"
    - "Y8 CC-L195-196 T003 FORWARD 'Our focus remains on balancing volume growth with calibrated pricing'"
    - "Y9 CC-L225-226 T003 FORWARD 'attractive long-term growth potential'"
    - "Y10 CC-L286 T006 DATE 'in the coming months'"
    - "Y11 CC-L316 T007 NUMBER ANALYST_STATED 'this 32% growth'"
    - "Y12 CC-L324-328 T008 NUMBER-unquantified metro rainfall 'normal or even above normal'"
    - "Y13 CC-L378 T015 FORWARD ANALYST_STATED 'in Q3 we are expecting softer than that'"
    - "Y14 CC-L422-423 T026 NUMBER-unquantified 'premium portfolio contribution is going up'"
    - "Y15 CC-L466-467 T031 DATE ANALYST_STATED 'normalizing post-agorn monsoon' (ASR)"
    - "Y16 CC-L473-474 T032 FORWARD 'So, we will continue to do this'"
    - "Y17 CC-L506-507 T040 NUMBER ANALYST_STATED 'near zero price increases'"
    - "Y18 CC-L510 T041 ENTITY 'rural Andhra'"
    - "Y19 CC-L673 T063 NUMBER-unquantified 'Protein is also lower'"
    - "Y20 CC-L718 T070 NUMBER-unquantified paneer 'growing on a quarterly basis'"
    - "Y21 CC-L742-743 T075 NUMBER ANALYST_STATED ASR 'McTean's revenue value world' (mid-teens, INFERENCE)"
    - "Y22 CC-L840-841 T078 NUMBER 'all payments happen online at the farmer level'"
arithmetic_mismatches:
  - {metric: "6B specificity ratio", a4_value: "16/59 = 0.27; 18/59 = 0.31 with festival anchors ('just above 0.3')", recomputed: "16/62 = 0.26; 18/62 = 0.29 (M41-M43 management FORWARD, T045, unquantified); 16/65 = 0.25 if Y8, Y9, Y16 land", source_line: "LG-L579-581; R-L1141-1143"}
  - {metric: "Brief part 1 reading-2 range on the Jul-Sep average step", a4_value: "Rs 48.4-50.1", recomputed: "Rs 49.69-50.05 (48.40-48.51 is the flat path)", source_line: "R-L1382 vs R-L961; P-l276-288"}
  - {metric: "A4 block concall_rows", a4_value: "397 = R001-R336 plus M01-M32", recomputed: "336 + 32 = 368; 397 needs M01-M61", source_line: "work/blocks/a4-role5-loop2.yaml L20, L141"}
surviving_bear_counters:
  - {claim: "Floor bull end 0.8-0.9% and reading-2 low end Rs 48.40-48.51/L 'if cost holds at the September level'", counter: "October already ran above September (CC-L375); a flat Q3 average needs Nov-Dec below September, i.e. the flush management only hopes for and will not forecast (CC-L372-374, CC-L605); A4's own disposition says the flat path does not expect a rise (R-L1698); qualify the flat path at every location", source_line: "CC-L375, CC-L372-374, CC-L605; R-L961-962, R-L1698", type: MISSING}
findings_by_type:
  factual:
    - {id: F2-1, loop: A4, gap: "6B on 59 management FORWARD rows; closed ledger adds M41-M43: 16/62 = 0.26 (not 0.27), festival variant 18/62 = 0.29 (not 0.31 'just above 0.3'); fix 6B, 6E, Concall Verdict, F17, R-L846, YAML; 6E row unchanged"}
    - {id: F2-2, loop: A4, gap: "brief part 1 R-L1382 gives Rs 48.4-50.1 for the Jul-Sep average step; that path is Rs 49.7-50.1, 48.4 is the flat path"}
  missing:
    - {id: M2-1, loop: A3, gap: "orphan rows M33-M61 marked not reviewed by A4; material ones cited in substance; M56, M58, M60, M61 uncited; mark each cited or 'reviewed, no finding'"}
    - {id: M2-2, loop: A2, gap: "22 fresh-pass units Y1-Y22 absent from the closed ledger; 4 material (CC-L441-443 lending, CC-L816-817 subsidised feed, CC-L393 'this quarter', CC-L651-654 analyst cow reading), all already cited by A4"}
    - {id: M2-3, loop: A4, gap: "surviving bear counter P2: flat-at-September path (Rs 48.40-48.51; floor 0.8-0.9%) needs Nov-Dec below September after the reported October rise (CC-L375); qualify at R-L961-962, R-L1049, R-L1248, R-L762-763, R-L1351-1352, R-L1382-1383, YAML F12/F13, analyst note"}
  contradiction:
    - {id: C2-1, loop: A4, gap: "ledger status: YAML all_reviewed true (R-L1464) vs false (R-L1583); 'every ledger row was reviewed' (R-L23), 'No orphan IDs' (R-L846), 'all four ledgers reconciled' (R-L1361) vs 29 rows open; A4 block says 397 = R001-R336 plus M01-M32 and all_reviewed true"}
  style:
    - "S2-1 'rose/grew each month to September' true only from July (R-L1382, R-L1617)"
    - "S2-2 8C 'holds or narrows': about -277 bps (6 bps wider) at the 11% path on the H2 FY26 base proxy [INFERENCE]"
    - "S2-3 provenance: orchestrator-entered text inside the A4 review (OI-1 notes; edits applied by the orchestrator)"
    - "S2-4 loop-1 S-7 still open: run1 block a4-role5.yaml reads merge pending, no superseded header"
loop_back_to: "A2"
gap: "FINAL LOOP: flag, do not re-run. A2: 22 fresh-pass units Y1-Y22 missing from the closed ledger (4 material, all already cited by A4). A3 (protocol): orphan rows M33-M61 marked not reviewed by A4; material ones cited in substance; M56, M58, M60, M61 uncited. A4: F2-1 6B ratio 0.26 not 0.27 and festival variant 0.29 not 0.31 (M41-M43); F2-2 brief R-L1382 path range misattributed; M2-3 flat-path qualifier (October above September, CC-L375); C2-1 all_reviewed true vs false and block '397 = M01-M32'. PROCEED WITH FLAGS and cash INDETERMINATE not at stake."
style_notes:
  - "S2-1 say 'each month from July to September'"
  - "S2-2 optional 8C qualifier: within about 6 bps at the 11% path"
  - "S2-3 keep orchestrator-provenance labels in the A4 review"
  - "S2-4 mark the run1 A4 block superseded"
analyst_note: "Final Role 5 re-audit. All earlier findings are resolved, and A4's loop-2 arithmetic ties: slide 9 paths, floor need 0.8-3.4%, 8C cost YoY. Open items: (1) A4 marks M33-M61 not reviewed. The five material rows are already cited in substance, so the gap is mostly a review mark, but one number moves. M41-M43 are management FORWARD rows, so 6B is 0.26, not 0.27, and the festival variant is 0.29, not 'just above 0.3'. The 6E row holds. (2) The YAML and A4's block disagree on whether every row was reviewed, and the block's 397 = M01-M32 does not add up. (3) My spine pass finds 22 more class units. Four are material: lending, subsidised feed, the 'this quarter' date, and the analyst's cow reading. A4 cites all four. Three passes have not closed the class rule. (4) The flat-at-September path, which sets the floor's 0.8% bull end, needs Nov-Dec below September, because October already rose (CC-L375). Nothing touches a filed number or PROCEED WITH FLAGS."
```
