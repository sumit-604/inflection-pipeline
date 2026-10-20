# A5 ADVERSARY AUDIT: Heritage Foods (HERITGFOOD) Q2 FY27, Role 5 concall addendum, loop 1 re-audit

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-19 | loop: role5-loop1
Review under audit: runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md (1,705 lines; Role 5 section R-L833-1330; Role 5 loop 1 disposition R-L1685-1705)
Prior audit re-checked: runs/heritgfood-q2fy27/work/audit_heritgfood_q2fy27_role5_run1.md (findings F1, M1-M4, C1, C2; style S1-S8)
Inputs read: A1 concall fulltext CC-L1-853 in full (header turn map and body CC-L130-853 line by line); A1 concall structured file in full (R001-R336); A2 concall ledger (count test, turns, questions, FORWARD section, Section 9 conflicts, Section 10 loop-1 addendum); A2 count-test headers of the results, presentation and release ledgers; results fulltext L400-431; presentation fulltext P-l258-299 (slide 9); press release fulltext PR-L68-162; the A4 review in full for the Role 5 section and every line the loop-1 disposition names. Also grep of work/blocks/ for the C2 check. No source file and nothing under inputs/ was opened.
Scope: the Role 4 body was audited COMPLETE in loop 2. This audit covers the Role 5 section, every line the Role 5 change log and loop-1 disposition name, and the resolution of each run1 finding.

Anchors: "CC-L###" = concall fulltext line. "R-L###" = current review line. "L###" = results fulltext line. "P-l###" = presentation fulltext line. "PR-L###" = press release fulltext line. "LG-L###" = concall ledger line.

---

## RUN1 FINDING RESOLUTION

| Run1 finding | Type | Status now | Evidence |
|---|---|---|---|
| F1 curd run-rate | FACTUAL | RESOLVED | Two readings with the curd-quarterly working reading at R-L838, R-L1026, R-L1088, R-L1234-1235, R-L763, R-L1289, R-L1404, YAML. Arithmetic re-checked: Rs 69.6/kg, Rs 17.5/kg, 80.9-86.0%, 40.2-41.6%, 71.0% all tie. The added peak-day caveat is sound (PR-L92 "surpassed 500 tons per day during the quarter"). |
| M1 spine units U1-U10 | MISSING (A2) | RESOLVED at A2; review text open | Ledger LG-L14, LG-L20 and Section 10 (LG-L524-538) add M01-M10, re-flag R236 FORWARD_MGMT at T024 (LG-L350), relabel C3 (LG-L517), fix C5 and C6 (LG-L519-520). The review still reads 336 rows "until it lands" (R-L844). See C-A. |
| M2 FC-1 two readings | MISSING | RESOLVED | R-L29, R-L774, R-L1186, R-L1222, R-L1278, R-L1327, R-L1345, YAML. All margin and growth figures tie (Arithmetic table). |
| M3 slide 9 second reading | MISSING | RESOLVED, with two new gaps | Added at R-L959, R-L1047, R-L1246, R-L760, R-L1349, R-L1380, YAML. A4's one departure is correct: the flat-at-September path does not expect an October rise, so the October point does not separate reading 1 from the continued-step path. New: the reading-2 range rests on the Jul-Sep average step (M-B), and the EBITDA-floor math was not carried across the range (M-C). |
| M4 KMF procurement fork | MISSING | RESOLVED | R-L770, R-L812, R-L699, R-L1276, R-L1417, R-L1428, YAML; tagged [MGMT, ASR; INFERENCE on transmission]. |
| C1 specificity 16/57 | CONTRADICTION | RESOLVED | R-L1139-1141, R-L1172, R-L1313, R-L1354, YAML R-L1586. |
| C2 merge-pending YAML | CONTRADICTION | RESOLVED | R-L1446-1448, R-L1612-1613; work/blocks/a4-role5-loop1.yaml carries "done 2026-10-19" and 0.28. The run1 copy work/blocks/a4-role5.yaml is left as the run1 record (STYLE S-7). |
| S1, S2, S3, S5, S6, S7 | STYLE | APPLIED | R-L1186 and R-L1222 (+19.57%, +23.57%), R-L980, R-L799 and R-L1252 (tally 1/6/7 ties), R-L865, R-L872, R-L1202. |
| S4, S8 | STYLE | LOGGED | S8 is now overtaken by the ledger fix; folded into C-A. |

---

## DELIVERABLE-COMPLETENESS AUDIT (gate)

| Brief part | Heading (review line) | Status |
|---|---|---|
| 1. Summary narrative | R-L1367 | PRESENT. 18 lines (R-L1369-1386), inside the 10-20 line band. Carries both Q3 cost readings, the floor, cow inflation and the ice cream target. |
| 2. Sector intelligence | R-L1388 | PRESENT. Six bullets; call content tagged [MGMT, ASR]. |
| 3. Business-model intelligence | R-L1398 | PRESENT. Nine bullets; the run-rate bullet now carries both readings (R-L1404). |
| 4. Competition intelligence | R-L1410 | PRESENT. Seven bullets, including the conglomerate entrant and the KMF procurement fork (R-L1417). |
| 5. Forward map | R-L1420 | PRESENT. Make-or-break line plus 11 dated rows (R-L1426-1436), each with a bull fork and a bear fork; the 1 Nov row now carries the procurement-side bear fork. |

Gate: PASS. All five parts exist and carry real content.

---

## COVERAGE AUDIT

Fresh pass: I read the concall fulltext CC-L130-853 line by line and listed every unit of the A1 row types, then diffed against the structured rows R001-R336 and the ledger's M01-M10. Class rule applied (the A1 rule as the run1 audit and A2 accepted it): NUMBER = any stated number, or a stated direction or level of a named metric (the R071 class); FORWARD = a management expectation, intent or conditional (R228, R264 class); ENTITY = a person, firm, place, channel or pack type (R194, R199, R212 class); DATE = a named period or horizon, including analyst horizons (R288, M09 class); QUALIFIER = a decline, refusal or data caveat (R313, R316, R325, R319, R329, R332 class).

| Category | A2 count (ledger with M01-M10) | Fresh count | Orphan rows (ledger row absent from A4) | Status |
|---|---|---|---|---|
| Turns | 81 | 81 (81 turn lines in the fulltext header) | none | PASS |
| Analyst questions | 24 | 24 (24 [Qnn] tags) | none | PASS |
| NUMBER | 169 | 179 | none | FAIL: 10 units missing (V1, V3, V5, V6, V7, V8, V12, V17, V21, V22) |
| ENTITY | 53 | 56 | none | FAIL: 3 units missing (V10, V19, V20) |
| FORWARD | 60 | 62 | none | FAIL: 2 units missing (V14, V16) |
| DATE | 22 | 24 | none | FAIL: 2 units missing (V2, V4) |
| QUALIFIER | 42 | 47 | none | FAIL: 5 units missing (V9, V11, V13, V15, V18) |
| Total rows | 346 | 368 | none | FAIL (A2) |

Structured counts re-verified by grep: NUMBER 162, ENTITY 52, FORWARD 60, DATE 20 (R275 is a "page header" row), QUALIFIER 42 (R295 is a "page header" row), total 336. Filed-document ledgers (results 1,242; presentation 696 = 45 slides + 651; release 180) are unchanged since the loop-2 COMPLETE audit; their header counts tie to the structured files and were not re-enumerated in this Role 5 loop.

Orphan check: A4 marks all 336 structured rows reviewed (R-L22, R-L844) and cites M01-M10 by CC-L (M01 R-L946, R-L768; M02 R-L1186; M03 R-L1024; M04 and M06 R-L393; M05 R-L1052; M07 R-L1197; M08 R-L1136; M09 R-L1027; M10 R-L1093). Orphan rows: none.

Units the fresh pass found that the structured file and the ledger lack. "Material" = A4 cites the unit by CC-L line and builds on it. The run1 pass under-counted: it reported FORWARD 60 = 60 and QUALIFIER 42 = 42 as PASS.

| V | Fulltext line | Turn | Verbatim unit | Type (class analog) | Material? A4 use |
|---|---|---|---|---|---|
| V1 | CC-L275 | T005 (analyst) | "normally it doesn't happen that for two consecutive years we have persistent inflation" | NUMBER, analyst-stated duration (R118) | minor |
| V2 | CC-L319-322 | T008 | "weather helped in Q1 ... compared to let's say previous year Q1" | DATE, comparison base (R278) | minor; CQ02 R-L1006 |
| V3 | CC-L335-337 | T008 | "temperature sensitive products ... it is sustained at the same levels as Q1" | NUMBER, unquantified comparative (R071) | minor; CQ02 |
| V4 | CC-L346-349 | T011 (analyst) | "are we planning further price hikes in 3Q and beyond" ... "over the next few months" | DATE, analyst horizon (M09) | minor |
| V5 | CC-L369-371 | T014 | "village level, farm level procurement prices also increasing" | NUMBER, unquantified comparative (R071) | minor |
| V6 | CC-L400-402 | T022 (CEO) | "our procurement footprint in Karnataka is not significant ... we have some sales volume in Bangalore city now it is significant enough for us" | NUMBER, unquantified comparative (R071) | MATERIAL: the basis of the R5-M4 fork; Q45 R-L770, M17 R-L812, 8A-W R-L699, brief R-L1417, forward map R-L1428 |
| V7 | CC-L426 | T026 | "Our yoghurt's contribution share is going up, ice cream's share is going up" | NUMBER, unquantified comparative (R071) | minor |
| V8 | CC-L444-451 | T028 | farmer metrics "very encouraging and very positive ... the number of farmers that they are adding ... the volume per farmer ... capacity utilization per milk collection center have all been very positive" | NUMBER, unquantified comparative (R071) | MATERIAL: CQ08 R-L1012; M5 status "answered" R-L800 |
| V9 | CC-L486-487 | T032 (A1 map shares L487 with T033) | "normal crisis is speculative and I do not wish to make any comment" | QUALIFIER, decline (R313) | MATERIAL: 6C #2 R-L1149; CQ09 R-L1013; Step 2 R-L962 |
| V10 | CC-L490-491 | T033 (analyst; A1 map puts L491 in T034) | "the cooperators in the Southern region, Arvind, Pichaya, and Nandari" | ENTITY, ASR names (R188, R192); "Pichaya" unresolved | minor; CQ10 R-L1014 |
| V11 | CC-L510-511 | T041 | "For example, I'm just making it up" | QUALIFIER, data caveat (R319) | MATERIAL: Q21 status R-L746; 5B R-L1114 |
| V12 | CC-L522-524 | T041 | "except in the case of ghee, we were able to sustain the volume growth in all other both curd and paneer. As far as ghee is concerned you will see that the volume growth has been flat" | NUMBER, unquantified (about 0% volume growth) (R071) | MATERIAL: CQ12 R-L1016; Q17 R-L742; 5A row 13 R-L1087; 7A R-L1195; Q46 R-L771; brief R-L1404 |
| V13 | CC-L527-528 | T041 | "please don't use that graph to calibrate and calculate to that granularity" | QUALIFIER, data caveat (R319, R332) | MATERIAL: 6C #5 R-L1152; CQ12; 4B R-L1037 |
| V14 | CC-L606 | T049 | "If it comes down, well and good actually it is going to be tremendous" | FORWARD, conditional (R264) | minor |
| V15 | CC-L612-615 | T051 | "you are answering questions yourself ... Will it go to 100 rupees per litre ... I don't know" | QUALIFIER, decline (R313) | MATERIAL: 6C #7 R-L1154; CQ16 R-L1020; 4B R-L1037 |
| V16 | CC-L616-617 | T051 | "we also expect that, you know, with such high prices, the farmers should produce more milk and prices should come down" | FORWARD, management expectation (R228) | MATERIAL: 6C #16-18 R-L1158; a third management statement on the load-bearing Q3 cost row |
| V17 | CC-L623-624 | T051 | "our consumer prices are at much higher level than it was earlier" | NUMBER, unquantified comparative (R227, R071) | minor |
| V18 | CC-L624 | T051 | "That's all I can say" | QUALIFIER, decline (R325) | MATERIAL: 6C #8 R-L1155 |
| V19 | CC-L696 | T066 per A1 map | "Ramnigaru" | ENTITY, person name, ASR (R194) | minor; 0B Unmapped inference R-L872 |
| V20 | CC-L703-704 | T067 | "in all the verticals including our integration as well as the outside general trade market" | ENTITY, sales channels (R199, R212) | MATERIAL: Q6 R-L731; Q47 R-L772; 5A row 17 R-L1091; brief R-L1406 |
| V21 | CC-L705-706 | T067 | "we have seen that in our PBT ... we have grown significantly during quarter two" | NUMBER, unquantified comparative (R071); M07 holds the separate "strong quarter two" claim | minor; CQ21 R-L1025 |
| V22 | CC-L784-786 | T076 | "if milk procurement prices go by 11% you can't take up all products by 11% ... I can't increase consumer milk prices by 11 percentage ... milk ... cannot go up by 11%" | NUMBER, stated number (R157 is only the analyst-frame reference at L782) | MATERIAL: 6A R-L1136; 6D R-L1168; 8D R-L1264; brief R-L1401, R-L1415 |

Eleven units are material (V6, V8, V9, V11, V12, V13, V15, V16, V18, V20, V22). A4 cites every one of them straight from the fulltext, so the review drops nothing. The spine failed again one level up. Finding M-A (MISSING, loop A2). Units checked and ruled out as duplicates: CC-L508-509 (R319 holds the same caveat), CC-L634-635 (R329), CC-L790 (R063 and R158 quantify it), CC-L797-798 (M08 and R271 hold it), CC-L803-804 "Edie", "Anshit" (in the A1 turn map at T077-T078).

---

## ARITHMETIC AUDIT

Every derived number added or changed in Role 5 loop 1, recomputed from the extracts, plus the numbers behind this audit's findings.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| QoQ margin, operating EBITDA | +98.2 bps | 618.63/13,380.94 = 4.6232% to 739.67/13,195.80 = 5.6053%; +98.21 bps | L407-420 | PASS |
| QoQ margin, PBT; PAT | +72.1; +47.2 bps | 335.49/13,380.94 = 2.5072% to 425.99/13,195.80 = 3.2282% (+72.10); 249.71 to 308.57: 1.8662% to 2.3384% (+47.22) | L424, L428 | PASS |
| Margin bridge D&A; OI; FC | +10.2; -22.4; -6.5 bps; 98.2 - 72.1 = 26.1 | 264.89 to 274.70: 1.9796% to 2.0817% (+10.21); 64.09 to 33.66: 0.4790% to 0.2551% (-22.39); 82.34 to 72.64: 0.6154% to 0.5505% (-6.49); 10.21 + 22.39 - 6.49 = 26.11 | L408, L415-416 | PASS |
| QoQ growth EBITDA; PBT; PAT | +19.57%; +26.97%; +23.57% | 739.67/618.63 = 1.19566; 425.99/335.49 = 1.26975; 308.57/249.71 = 1.23571 | L407-428 | PASS |
| YoY EBITDA; PBT; D&A (FC-1 note) | -4.17%; -37.13%; +36.61% | 73.97/77.19 = 0.9583; 425.99/677.60 = 0.6287; 274.70/201.09 = 1.3661 | L416, L424, Step 1A | PASS |
| Slide 9 reading B: Q2 average, step, add-on | 42.85; +0.649; 4.88 | 0.8 x S2 + 0.2 x S1: Jul 42.216, Aug 42.814, Sep 43.514; average 42.848; step 0.649; 47.73 - 42.848 = 4.882 | P-l276-288, CC-L502, PR-L76 | PASS |
| Slide 9 reading A: Q2 average, step, add-on | 51.08; +0.766; -3.35 | Jul 50.334, Aug 51.046, Sep 51.866; average 51.082; step 0.766; -3.352 | P-l276-288 | PASS |
| Q3 flat at September | 48.40 (+6.3%); 48.51 (+6.5%) | 43.514 + 4.882 = 48.396, /45.55 = +6.25%; 51.866 - 3.352 = 48.514, +6.51% | CC-L621 | PASS |
| Q3 continued average step | 49.69 (+9.1%); 50.05 (+9.9%) | 43.514 + 2 x 0.649 + 4.882 = 49.694 (+9.10%); 51.866 + 2 x 0.766 - 3.352 = 50.046 (+9.87%) | derived | PASS |
| Step for Rs 50.56 | +1.08 (1.67x); +1.02 (1.34x) | (45.678 - 43.514)/2 = 1.082, /0.649 = 1.67; (53.912 - 51.866)/2 = 1.023, /0.766 = 1.34 | derived | PASS (range incomplete: M-B) |
| Monthly step series (not computed by A4) | n/a | Reading B: May +0.33, Jun +0.33, Jul +0.20, Aug +0.60, Sep +0.70. Reading A: +0.65, +0.35, +0.30, +0.71, +0.82 | P-l276-288 | Feeds M-B |
| Q3 on the September step (not computed by A4) | n/a | B: 43.514 + 2 x 0.700 + 4.882 = 49.80 (+9.3%); A: 51.866 + 2 x 0.820 - 3.352 = 50.15 (+10.1%). 11% needs 1.082/0.700 = 1.55x (B) or 1.023/0.820 = 1.25x (A) the September step | derived | Feeds M-B |
| Q3 if the step keeps rising at the Aug-Sep pace (not computed by A4) | n/a | B: steps 0.802, 0.904, 1.006; levels 44.316, 45.220, 46.226; average 45.254 + 4.882 = 50.14 (+10.1%). A: steps 0.928, 1.036, 1.144; average 53.866 - 3.352 = 50.51 (+10.9%) [INFERENCE] | derived | Feeds M-B |
| EBITDA floor price need | 2.7-3.4% (Rs 50.0-50.56) | Rs 1/L = 17.28 lakh x 92 = Rs 15.898 Cr. Need = (Q3 cost - 47.73) x 15.898 / 1,319.58: Rs 48.40 0.81%; 49.69 2.37%; 49.80 2.49%; 50.05 2.79%; 50.15 2.92%; 50.29 3.08%; 50.51 3.35%; 50.56 3.41% | PR-L121, L407 | PASS at the two statements; range incomplete (M-C) |
| Q3 YoY landed-cost inflation vs Q2 (8C claim) | "moves the gap toward its red side on cost evidence" | Q2: 47.73/42.99 = +11.03% (+Rs 4.74). Q3 paths on the 45.55 base: +6.25% (+2.85) to +11.0% (+5.01); September-step and rising-step paths +9.3% to +10.9% | PR-L76-77, CC-L621 | CONTRADICTION C-B |
| Curd tonnage and shares (R5-F1) | Rs 70/kg; Rs 17.5/kg; 81-86%; 40-42%; 71% | 3,200 m / 46.0 m kg = 69.6; 3,200 m / 182.5 m kg = 17.5; 1,750-1,860 / 2,163.2 = 80.9-86.0%; 870-900 / 2,163.2 = 40.2-41.6%; 320/451.0 = 71.0% | CC-L715-719, PR-L92, PR-L131, PR-L136 | PASS |
| Peak-day caveat volume | "near 124 t a day" | 3,200 m / Rs 70 / 365 = 125.2 t | derived | STYLE S-3 |
| Ghee annualised vs consumer ghee and butter | 87.5 vs 89.80 | 350/4 = 87.5; 540.8 - 451.0 = 89.8 | PR-L131, PR-L136 | PASS |
| Specificity (6B) | 16/57 = 0.28; 14/55 = 0.25; 12/53 = 0.23 | 0.2807; 0.2545; 0.2264. Management rows 60 - R235 - R259 - R247 = 57 | LG-L329-388 | PASS under the stated rule (STYLE S-1 on festival anchors) |
| Monitorable tally M1-M14 | answered 1, partly 6, silent 7 | M5; M1, M2, M4, M6, M13, M14; M3, M7-M12 | R-L796-809 | PASS |
| Question call-status tally | 1 / 7 / 26 | Q9; Q1, Q4, Q10, Q15, Q17, Q29, Q31; 34 - 8 = 26 | R-L726-759 | PASS |
| Q3 YoY on "not 47 to 50" | about +9.8% | 50.0/45.55 = +9.77% | CC-L618-621 | PASS |

No mismatch above rounding in A4's own sums. The failures sit in a direction claim (C-B) and two ranges cut short (M-B, M-C).

---

## ADVERSARIAL READ

The three most positive claims in the Role 5 section after loop 1, each with the strongest bear counter from the same extracts.

P1. EBITDA floor: "whatever is EBITDA now is not going to come down" (CC-L603-604); "the bull side gains an EBITDA floor promise" (R-L699); K6, M16.
- Bear counter: the Q3 price decision is open ("we will take a call", CC-L638-639). Thirteen minutes later management restated the floor as "relatively better off in terms of EBITDA" (CC-L736-737). Season works against it (FY26 H2 gross margin 183 bps below Q2).
- Survives? Already in A4: Step 2 confidence MEDIUM-LOW (R-L942), F13 (R-L1350), Q36 (R-L761), 8C seasonal note (R-L711). No graft needed. The symmetric gap runs the other way (M-C).

P2. Price ratchet: "The asymmetry is the bull case: each Rs 1/L fall in landed cost adds about 1.2% of revenue to margin if consumer prices hold" (R-L1063).
- Bear counter: a cost fall takes margins "back to our steady-state levels" (CC-L738-739); liquid milk "cannot go up by 11%" (CC-L784-786); "our bottom line is suffering whenever there is a raw milk price increase" (CC-L798-799); management refused to discuss cooperatives (CC-L492-497).
- Survives? Already in A4: "Bull claim, untested" (R-L1063), Step 2 (R-L942, R-L944), 8D strategic premium (R-L1264), Q51. No graft needed.

P3. Slide 9 second reading (new in loop 1): "Reading 2 puts Q3 at Rs 48.4-50.1/L, nearer 'not 47 to 50' than '11% might continue'" and "11% needs the monthly climb to speed up about 1.3-1.7x" (R-L959; R-L1047; F12 R-L1349; brief R-L1380; analyst note R-L1612).
- Bear counter: the range uses the Jul-Sep AVERAGE step. The monthly step was not flat; it rose. On reading B it ran +0.33, +0.33, +0.20, +0.60, +0.70 from May to September; on reading A +0.65, +0.35, +0.30, +0.71, +0.82 (P-l276-288, derived). On the September step alone, Q3 lands at Rs 49.80 (B) to Rs 50.15 (A), +9.3% to +10.1% YoY. If the step keeps rising at the August-to-September pace, Q3 lands at Rs 50.14 (B) to Rs 50.51 (A), +10.1% to +10.9%: above the Rs 50.0 cap and, on A, within Rs 0.05 of 11% [derived; INFERENCE]. Against the September step, 11% needs 1.25-1.55x, not 1.34-1.67x. A slope also cannot see a discrete farm-price step. KMF passes Rs 6/L to farmers from 1 November (CC-L396-400), after the slope's last point, in a belt management calls cow-milk country, where it says the inflation sits (CC-L681-686) [INFERENCE on transmission, as R5-M4]. The same answer also names Aavin's two farm steps "in this quarter" (CC-L393-395); the quarter is not clear on the ASR line.
- Survives: YES. The review states the range as if the average step were the only slope. Graft: add the September-step and rising-step results and the discrete-step caveat beside reading 2 in Step 2 (R-L959), Exchange 1 (R-L1047), the 8A seed row (R-L1246), F12 (R-L1349), Q35 why (R-L760), brief part 1 (R-L1380), YAML F12 and the analyst note. "Nearer 'not 47 to 50'" then holds on the flat and average-step paths only. IC-1 and the two-reading structure stand. Finding M-B.

Mandatory acquisition-economics probe. The call describes stake changes: "Getaway, in which we now hold 71 percent stake" and "Heritage Novandee Foods now a wholly owned subsidiary" (CC-L229-233).
- Multiple: consideration NOT FOUND in any extract. Target earnings are negative: dairy subsidiaries' segment result H1 FY27 -Rs 3.15 Cr (L468 minus L125; R-L564); NCI-implied Get-A-Way H1 loss about Rs 2.60 Cr [INFERENCE, single-NCI-entity assumption]. Price / target PAT = NOT FOUND / negative, so no positive multiple exists. ROCE, debt, cash and customer tenure: NOT FOUND.
- From the call: Heritage makes 3,272 L/day of ice cream for Get-A-Way (CC-L230-232), about Rs 6.0 Cr a quarter at Rs 200/L (CC-L427) [derived; transfer price NOT FOUND].
- Bear reading: more of a loss-making asset was bought at an undisclosed price. It is already in A4 (Step 5F, Q32, Q39, Q42, F5). No "cheap, accretive" claim exists to stress. No graft.

Symmetry check on A4's bear claims (CLAUDE.md Rule J):
- F13 and Q36 state the floor's price need only at management's two cost statements: "At Rs 50.0-50.56/L it needs ... about 2.7-3.4%" (R-L960, R-L1350, R-L761). The review's own reading 2 runs from Rs 48.40. Across Rs 48.40-50.56 the need is 0.8% to 3.4%; on the average-step path 2.4-2.8%. The bull end of the floor test is missing. Finding M-C.
- Role 5 8C (R-L1254): "The call moves the seed gross-margin item toward its red side (wider than -271 bps) on cost evidence only." On every Q3 cost path the YoY cost inflation is at or below Q2's +11.03%. On cost alone the YoY gap holds or narrows. Finding C-B.

---

## FINDINGS (tagged)

M-A. MISSING. Loop: A2.
Gap: 22 fresh-pass units (V1-V22, Coverage Audit) are absent from the structured file and the ledger; ledger Section 10 lists only M01-M10. Eleven are material and A4 builds on them: V22 "milk cannot go up by 11%" (CC-L784-786), V12 ghee volume flat (CC-L522-524), V6 Karnataka procurement "not significant" (CC-L400-402, the basis of the R5-M4 fork), V16 "prices should come down" (CC-L616-617), V20 the "integration" and "outside general trade" channels (CC-L703-704), V8 farmer metrics (CC-L444-451), and five declines or caveats counted in 6C (V9, V11, V13, V15, V18).
Fix: A2 appends V1-V22 as M11-M32 under MISSING_FROM_STRUCTURED with turn and flags (V1, V4, V10 ANALYST_STATED; V10, V19 ASR_NAME), then runs one closing sweep of CC-L130-853 under the class rule stated in the Coverage Audit, so the set closes in this loop. No A3 work: A4 already cites every material unit by CC-L line.

M-B. MISSING (surviving bear counter P3). Loop: A4.
Gap: reading 2 is stated as Rs 48.4-50.1/L, "nearer 'not 47 to 50'", with 11% needing a 1.3-1.7x faster climb (R-L959, R-L1047, R-L1246, R-L760, R-L1349, R-L1380, YAML F12, analyst note). The range uses the Jul-Sep average step only. The September step gives Rs 49.80-50.15; a step that keeps rising gives Rs 50.14-50.51; against the September step 11% needs 1.25-1.55x. KMF's Rs 6/L farm step from 1 November sits outside any slope.
Fix: add the September-step and rising-step results, tagged [derived; INFERENCE], and the discrete-step caveat [MGMT, ASR; INFERENCE on transmission] at each location. State that "nearer 'not 47 to 50'" holds on the flat and average-step paths only. Separating observation unchanged: October and November landed cost (Q35).

M-C. MISSING (symmetry, bull-side qualifier). Loop: A4.
Gap: the EBITDA-floor price need is shown only at Rs 50.0-50.56/L (2.7-3.4%) in Step 2 (R-L960), F13 (R-L1350), Q36 (R-L761) and YAML F13 (R-L1566). The review's own Q3 range starts at Rs 48.40/L.
Fix: state the need across the range: about 0.8% at Rs 48.40 (flat at September), 2.4-2.8% on the average-step path, 3.1% on last year's step, 3.4% at 11% [derived]. Keep the seasonal headwind note.

C-A. CONTRADICTION. Loop: A4 (after A2's M-A addendum lands).
Gap: the review gives the concall ledger as 336 rows with NUMBER 162, ENTITY 52, DATE 20, and says "the row count above stands until it lands" (R-L22, R-L844; YAML R-L1458, R-L1578). The A2 addendum has landed: the ledger reads 346 rows, NUMBER 169, ENTITY 53, DATE 22 (LG-L14, LG-L20, LG-L524-538). R-L844 also calls the C5 and C6 turn slips A3's; the ledger records them as A2 loop-1 corrections (LG-L519-520). R-L1139 says the R236 flag "is" a ledger slip; the ledger has re-flagged it (LG-L350).
Fix: one edit after M-A lands. Use the final ledger counts (368 rows on this audit's count; M01-M32), drop "until it lands", set "A2's turn slips (corrected in the ledger)" and "the R236 flag was a ledger slip, now corrected". Align the YAML ledger blocks.

C-B. CONTRADICTION. Loop: A4.
Gap: Role 5 8C (R-L1254) says "The call moves the seed gross-margin item toward its red side (wider than -271 bps) on cost evidence only." Step 2 (R-L958-959) and the 8A seed row (R-L1246) put Q3 YoY landed-cost inflation at +6.3% to +11.0% (+Rs 2.85 to +5.01/L) on the Rs 45.55 base, against Q2's +11.03% (+Rs 4.74/L, PR-L76-77). Even the September-step and rising-step paths (M-B) give +9.3% to +10.9%. On cost alone the YoY gap holds or narrows. The call's price evidence (September hikes "much higher than 8%", October opened higher, CC-L364-367) points the same way.
Fix: restate 8C: on cost evidence the call puts Q3 YoY cost inflation at or below Q2's; the YoY gap's direction rests on the unquantified Q3 price step and on the loss of the Q2 stock-drawdown benefit (Q34). State "weaker on the Q3 margin path" (R-L1315, R-L1328, YAML R-L1594) as a QoQ reading: season, and Q3 cost Rs 0.67-2.83/L above Q2.

---

## VERDICT

INCOMPLETE.
- Failing agents: A2 (M-A), then A4 (C-A, C-B, M-B, M-C).
- Finding types: FACTUAL 0, MISSING 3, CONTRADICTION 2. STYLE 7 logged.
- All seven run1 findings are resolved. A4's arithmetic ties to rounding throughout.
- The protocol verdict PROCEED WITH FLAGS and cash conversion INDETERMINATE are not at stake. No fix touches a filed number.
- Sequencing: A2 appends M11-M32 and closes the class sweep; A3 needs no new forensic work; A4 applies C-A once on the final count, plus C-B, M-B and M-C; A5 re-checks.

---

## STYLE NOTES (logged, no loop)

- S-1. 6B rule "a number or a named date or quarter": R223 ("after Diwali festival", CC-L296-297) and R229 ("post Diwali", CC-L373) are left uncounted. That matches M25's "date not in corpus" but the rule does not say so. Counted, the ratio is 18/57 = 0.32. State the exclusion; "below 0.3 on every count" (R-L1141) holds only under it. The run1 S4 swap (R251 counted, R254 not) nets to zero.
- S-2. R-L10 and R-L1687 cite work/audit_heritgfood_q2fy27_role5.md as the run1 audit. Run1 now sits at work/audit_heritgfood_q2fy27_role5_run1.md; this path holds the loop-1 re-audit.
- S-3. 5A row 14 (R-L1088): "near 124 t a day" recomputes to 125 t (3,200 m / Rs 70 / 365).
- S-4. The Step 2 procurement-cost row (R-L943) could carry management's in-answer "prices should come down" (CC-L616-617; V16) beside "not 47 to 50". It leans toward reading 2.
- S-5. Q35 forks (R-L760): "October below Rs 50.0/L" does not separate the readings. On the slide 9 add-on, October landed is about Rs 48.40 (flat), 49.05 (average step), 49.10 (September step), 49.20 (rising step) and 49.48 (the 11% path) [derived; INFERENCE]. Use the October step over September (about +0.65 vs about +1.1 per litre) or the Q3 average against Rs 50.0.
- S-6. The 0B Unmapped row says the NutriVate CEO thanks "Ramnigaru" (R-L872); the A1 turn map places CC-L696 in T066 ("moderator or management"). Say "a speaker thanks" or add [INFERENCE: ASR] to the speaker.
- S-7. work/blocks/a4-role5.yaml (the run1 copy) still reads merge "pending". A one-line "superseded by a4-role5-loop1.yaml" header would stop a mis-read.

---

```yaml
stage: A5-adversary
company: "HERITGFOOD"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: "role5-loop1"
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger:
    - "V1 CC-L275 T005 NUMBER analyst 'two consecutive years' persistent inflation (minor)"
    - "V2 CC-L319-322 T008 DATE Q1 vs previous-year Q1 weather base (minor)"
    - "V3 CC-L335-337 T008 NUMBER-unquantified temperature-sensitive growth 'sustained at the same levels as Q1' (minor)"
    - "V4 CC-L346-349 T011 DATE analyst horizon '3Q and beyond', 'next few months' (minor)"
    - "V5 CC-L369-371 T014 NUMBER-unquantified 'farm level procurement prices also increasing' (minor)"
    - "V6 CC-L400-402 T022 NUMBER-unquantified Karnataka procurement 'not significant', Bangalore sales 'significant enough' (MATERIAL)"
    - "V7 CC-L426 T026 NUMBER-unquantified yogurt and ice cream share 'going up' (minor)"
    - "V8 CC-L444-451 T028 NUMBER-unquantified farmer metrics 'very positive' (MATERIAL)"
    - "V9 CC-L486-487 T032 QUALIFIER decline 'I do not wish to make any comment' (MATERIAL)"
    - "V10 CC-L490-491 T033 ENTITY analyst 'Arvind, Pichaya, and Nandari' (ASR; minor)"
    - "V11 CC-L510-511 T041 QUALIFIER caveat 'I'm just making it up' (MATERIAL)"
    - "V12 CC-L522-524 T041 NUMBER-unquantified ghee 'volume growth has been flat'; curd, paneer volume sustained (MATERIAL)"
    - "V13 CC-L527-528 T041 QUALIFIER caveat 'please don't use that graph to calibrate' (MATERIAL)"
    - "V14 CC-L606 T049 FORWARD conditional 'if it comes down ... tremendous' (minor)"
    - "V15 CC-L612-615 T051 QUALIFIER decline 'you are answering questions yourself ... I don't know' (MATERIAL)"
    - "V16 CC-L616-617 T051 FORWARD 'we also expect ... prices should come down' (MATERIAL)"
    - "V17 CC-L623-624 T051 NUMBER-unquantified 'consumer prices are at much higher level than it was earlier' (minor)"
    - "V18 CC-L624 T051 QUALIFIER decline 'That's all I can say' (MATERIAL)"
    - "V19 CC-L696 T066 ENTITY 'Ramnigaru' (ASR; minor)"
    - "V20 CC-L703-704 T067 ENTITY channels 'integration', 'outside general trade market' (MATERIAL)"
    - "V21 CC-L705-706 T067 NUMBER-unquantified NutriVate PBT 'grown significantly during quarter two' (minor)"
    - "V22 CC-L784-786 T076 NUMBER 'can't take up all products by 11% ... consumer milk ... cannot go up by 11%' (MATERIAL)"
arithmetic_mismatches:
  - {metric: "8C direction of the YoY gross-margin gap on the call's cost evidence", a4_value: "toward red (wider than -271 bps)", recomputed: "Q3 YoY landed-cost inflation +6.3% to +11.0% (+Rs 2.85 to +5.01/L) vs Q2 +11.03% (+Rs 4.74/L): gap holds or narrows on cost alone", source_line: "R-L1254 vs R-L958-959; PR-L76-77; CC-L621"}
  - {metric: "Slide 9 reading 2 Q3 range and step multiple", a4_value: "Rs 48.4-50.1/L; 11% needs 1.34-1.67x the Jul-Sep step", recomputed: "September step Rs 49.80-50.15; rising step Rs 50.14-50.51; 11% needs 1.25-1.55x the September step", source_line: "P-l276-288; R-L959"}
  - {metric: "EBITDA floor Q3 realisation need", a4_value: "2.7-3.4% (Rs 50.0-50.56/L)", recomputed: "0.8% (Rs 48.40) to 3.4% (Rs 50.56); 2.4-2.8% on the average-step path", source_line: "PR-L121, L407; R-L960, R-L1350, R-L761"}
surviving_bear_counters:
  - {claim: "Slide 9 reading 2 puts Q3 landed cost at Rs 48.4-50.1/L, nearer 'not 47 to 50'; 11% needs a 1.3-1.7x faster climb", counter: "the monthly step rose (B +0.20, +0.60, +0.70); September step gives Rs 49.80-50.15, a rising step Rs 50.14-50.51 (+10.1% to +10.9%), above the Rs 50 cap; KMF's Rs 6/L farm step from 1 Nov in a cow belt sits outside any slope", source_line: "P-l276-288, CC-L396-400, CC-L681-686, CC-L393-395", type: MISSING}
findings_by_type:
  factual: []
  missing:
    - {id: M-A, loop: A2, gap: "22 fresh-pass units V1-V22 absent from structured file and ledger (Section 10 has M01-M10 only); 11 material (V6, V8, V9, V11, V12, V13, V15, V16, V18, V20, V22); append as M11-M32 and close one sweep under the stated class rule"}
    - {id: M-B, loop: A4, gap: "surviving bear counter P3: reading 2 range rests on the Jul-Sep average step; add September-step (Rs 49.80-50.15) and rising-step (Rs 50.14-50.51) results and the 1 Nov KMF discrete-step caveat at R-L959, R-L1047, R-L1246, R-L760, R-L1349, R-L1380, YAML F12, analyst note"}
    - {id: M-C, loop: A4, gap: "EBITDA floor need shown only at Rs 50.0-50.56 (2.7-3.4%); across the review's own range it is 0.8-3.4%; update R-L960, F13 R-L1350, Q36 R-L761, YAML F13"}
  contradiction:
    - {id: C-A, loop: A4, gap: "review says concall ledger 336 rows (162/52/60/20/42) 'until it lands' (R-L22, R-L844, YAML R-L1458, R-L1578); ledger now 346 (169/53/60/22/42) and 368 after M-A; C5/C6 slips are A2's and fixed (LG-L519-520); R236 flag fixed (LG-L350)"}
    - {id: C-B, loop: A4, gap: "8C R-L1254 'moves the seed gross-margin item toward its red side on cost evidence only' vs Step 2: every Q3 path gives YoY cost +6.3% to +11.0% vs Q2 +11.03%; restate, and mark 'weaker on the Q3 margin path' (R-L1315, R-L1328, YAML) as QoQ"}
  style:
    - "S-1 6B: Diwali-anchored R223, R229 uncounted without a stated rule; counted, 18/57 = 0.32; state the exclusion"
    - "S-2 R-L10, R-L1687 point to the run1 audit at a path that now holds the loop-1 re-audit; use audit_heritgfood_q2fy27_role5_run1.md"
    - "S-3 5A row 14 'near 124 t a day' recomputes to 125 t"
    - "S-4 Step 2 procurement row could carry 'prices should come down' (CC-L616-617)"
    - "S-5 Q35 fork 'October below Rs 50.0' does not separate readings; October lands Rs 48.4-49.5 on every slide 9 path"
    - "S-6 'Ramnigaru' line CC-L696 sits in T066 per the A1 map; do not assign it to the NutriVate CEO without an INFERENCE tag"
    - "S-7 run1 block work/blocks/a4-role5.yaml still reads merge pending; add a superseded header"
loop_back_to: "A2"
gap: "A2 first: append V1-V22 as M11-M32 (11 material: V6, V8, V9, V11, V12, V13, V15, V16, V18, V20, V22) and close one sweep under the stated class rule. Then A4: C-A row count on the final ledger (368 on this count), C-B restate 8C 'toward red' (Q3 YoY cost +6.3% to +11.0% vs Q2 +11.03%), M-B graft the reading-2 step sensitivity (Rs 49.80-50.51) and the 1 Nov KMF discrete-step caveat, M-C floor need 0.8-3.4% across the range. No A3 work. Verdict PROCEED WITH FLAGS and cash INDETERMINATE not at stake."
style_notes:
  - "S-1 state the festival-anchor exclusion in 6B"
  - "S-2 fix the run1 audit path at R-L10 and R-L1687"
  - "S-3 125 t, not 124 t"
  - "S-4 add CC-L616-617 to the Step 2 cost row"
  - "S-5 re-cut the Q35 October threshold"
  - "S-6 tag the Ramnigaru speaker as INFERENCE"
  - "S-7 mark the run1 A4 block superseded"
analyst_note: "Role 5 loop-1 re-audit. All seven run1 findings are resolved, and A4's correction on the flat-at-September path is right. A4's new arithmetic ties. Three gaps remain. (1) Spine: my line-by-line pass found 22 more units that the structured file and ledger lack. Eleven are material and A4 already cites them by CC-L, including 'milk cannot go up by 11%' (CC-L784-786), ghee volume flat (CC-L522-524), Karnataka procurement 'not significant' (CC-L400-402, the basis of the R5-M4 fork) and 'prices should come down' (CC-L616-617). The run1 pass under-counted FORWARD and QUALIFIER. (2) Reading 2 rests on the Jul-Sep average step, but the monthly step rose (B +0.20, +0.60, +0.70). On the September step Q3 is Rs 49.80-50.15; if the rise continues, Rs 50.14-50.51, above the Rs 50 cap. The floor needs 0.8-3.4% across the range, not only 2.7-3.4%. (3) 8C says the call moves the YoY gap toward red on cost alone, but every cost path is at or below Q2's 11.0% YoY. No filed number and not PROCEED WITH FLAGS is at stake."
```
