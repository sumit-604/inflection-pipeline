# A5 ADVERSARY AUDIT: Kross Limited (KROSS), Q2 FY27, ROLE 5 ADDENDUM, LOOP 1 RE-AUDIT

Agent: A5 adversary | model claude-opus-5-5 | date 2026-10-20
Prior audit: runs/kross-q2fy27/work/audit_kross_q2fy27_role5.md (INCOMPLETE: F1, F2, M1-M4, C1; STYLE S1-S13).
Scope (task message): (1) confirm each prior FACTUAL / MISSING / CONTRADICTION item is closed; (2) re-run the deliverable-completeness gate on the updated brief and the concall coverage audit; (3) check new or changed addendum text for new FACTUAL / MISSING / CONTRADICTION errors, with arithmetic and consistency with the Role 4 body. No new full adversarial pass on unchanged text.
Inputs read: A4 review (runs/kross-q2fy27/work/review_kross_q2fy27.md; ROLE 5 ADDENDUM L829-L1638); A1 concall fulltext and structured file (primary); A1 results and deck fulltexts (filed and deck cross-checks); A2 concall ledger. Not read: source files, inputs/, A3 reasoning. A3 was touched by one ID-only grep (M1 appears 13 times in forensics_concall_kross_q2fy27.md).
Merge check: the merged addendum (Review L833-L1638, 806 lines) matches A4's standalone file review_kross_q2fy27_role5.md (806 lines). Six key strings from the loop 1 fixes give 29 hits in each file.
SOURCE CAVEAT (binds every finding below): the concall is a MACHINE TRANSCRIPT (faster-whisper; CC L2, L19). Speakers are inferred. Numbers may be mis-heard. Where a call number meets a filed number, the filed number wins.

Anchor key: CC Lnnn = concall fulltext line. STR Lnnn = concall structured file line. LED Lnnn = A2 concall ledger line. RES / PPT Lnnn = results and deck fulltext lines. Review Lnnn = A4 review line (merged file).

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

Brief under test: 6. PLAIN-LANGUAGE BRIEF (UPDATED), Review L1417-L1489. It replaces the Role 4 brief in full (Review L831, L1419).

| Part | Heading line | Content | Status |
|---|---|---|---|
| 1. Summary narrative | Review L1421 | 18 lines (L1422-L1439). Bull reading, bear reading and two separating observations present | present |
| 2. Sector intelligence | Review L1441 | 7 lines (L1442-L1448) | present |
| 3. Business-model intelligence | Review L1450 | 13 lines (L1451-L1463) | present |
| 4. Competition intelligence | Review L1465 | 6 lines (L1466-L1471) | present |
| 5. Forward map | Review L1473 | Make-or-break line (L1474) plus 12 catalyst rows (L1478-L1489), each with a bull and a bear fork. Two rows are undated (preferential, HPML) and say so, as accepted at Role 4 (A5-S9) | present |

Gate: PASS. All five parts present and non-empty.

---

## 1. PRIOR FINDINGS: CLOSURE CHECK

| Prior ID | Type | What I checked | Status |
|---|---|---|---|
| F1 | FACTUAL | 6B states one rule (Review L1153) and lists all 52 management rows (L1155-L1156). I walked R149-R205 (STR L163-L219) under that rule and got the same 30 quantified IDs: 30 / 52 = 0.577 (L1158). R181 is excluded as analyst text (CC L276-L277). 6E re-derives OVERPROMISER (provisional) from specificity above 0.5 and provisional credibility 12.5% (L1001, L1182). EVASIVE appears only in the withdrawal notes (L1185, L1617). Copies aligned: verdict block L1307, 8D L1280, 8E L1284, Key Notes L1301, Section 5 L1405-L1413, YAML L1524-L1526, L1594 | CLOSED |
| F2 | FACTUAL | Brief L1430 now reads "difficult currently" to say WHEN margin returns (CC L480-L482). The same reading sits at L959, L972, L987, L1048, L1143, L1323, L1301, L1595. The sentence after it adds a new error (finding L1-F1) | CLOSED (new error in adjacent sentence) |
| M1 | MISSING | Ledger-only row M1 exists (LED L10, L477-L480; NUMBER 106). A3 carries M1 (ID grep). A4 cites it (Review L851, L856, L1038, L1071-L1072, L1352, L1559). A1 issued no R335; the MISSING_FROM_STRUCTURED path keeps the unit in the ledger, which the prior fix allowed. The ledger turn label is wrong (finding L1-C1) | CLOSED (label error logged as L1-C1) |
| M2 | MISSING | Two FY27-end debt readings carried in every listed place: Step 2 L965, L974; Exchange 2 L1076-L1077; 5A L1097; 5B L1127; 8A L1249; 8B L1260; 8D L1275; 8E L1286; Step 9 L1301; Q24 L1353; M29 L1392; Section 5 L1413; brief L1433, L1488; YAML L1528-L1532, L1596. "Confirmed" is gone. Filed Rs 117.14 Cr is in the brief (L1433). Q23 is the separating observation (L1077, L1352) | CLOSED |
| M3 | MISSING | QoQ test present in Exchange 3 (L1085, with the analyst-recall caveat), 5A (L1109, "on the analyst's Q1 9,500"), 8A L1248, Q32 L1361, M23 L1386, Section 5 L1413, YAML L1599. The brief line (L1429) carries the test but drops the caveat that the prior fix named, and tags the derived figure [MGMT-CALL] (finding L1-M2) | CLOSED in body; OPEN in brief (L1-M2) |
| M4 | MISSING | Brief L1428 restores the 81% / 81% line. Q3 forward-map row (L1483) carries the top-5 test in both forks. M23 L1386 adds the top-5 read | CLOSED |
| C1 | CONTRADICTION | Forward-map bull fork (L1479) now needs warrant conversion within H2 FY27, with Rs 39.75 Cr at allotment. Matches Step 2 (b) L973, Q26 L1355 and flag L1597 | CLOSED |
| S1-S13 | STYLE | Actioned at L1084 (S1), L1426 (S2), L1443 (S3), L1101 / L1279 / L1462 (S4), L1198-L1201 (S5), L1205 (S6), L1380 (S7), L1318 (S8), L1348 / L1399 (S9), L962 / L1485 (S10), L1309 / L1405 (S11), L961 (S12); S13 no action | logged |

---

## 2. COVERAGE AUDIT (concall, re-run)

Method: my own pass over the concall fulltext (CC L18-L509). (a) I listed every fulltext line that carries a digit after its timestamp (144 lines) and matched each numeric token to a structured row by line. I treated quarter and year labels as DATE and dial-in digits (CC L23, L134-L135) as process text, which is A1's practice. Echoes of a figure already rowed in the same exchange (CC L206, L212-L213, L230, L241, L243, L246, L351, L411) are not separate units. (b) I counted question hand-offs (CC L137, L201, L250, L298, L341, L360, L401, L462, L490). (c) I walked all 57 FORWARD rows for the 6B recount. (d) I re-counted ENTITY, DATE and QUALIFIER rows by category grep and spot-checked place and firm names (STR L127-L157). The structured file is unchanged since the prior full pass (no R335).

| Category | A2 count | My fresh count | Orphan rows (ledger, absent from A4) | Missing from ledger | Status |
|---|---|---|---|---|---|
| Speaker turns | 65 (LED L7, L39-L103) | 65 | none | none | PASS |
| Question slots / unique analysts | 9 / 7 (LED L8, L109-L117) | 9 / 7 (hand-offs as listed) | none | none | PASS |
| NUMBER | 106 = 105 structured + M1 (LED L10) | 107 | none | CC L454: analyst-spoken "So phase 1 would be 2 percent of that" (ASR garble of the phase-1 share; management then gives 30%, CC L458, R102). No structured row (R323 is at L453 only; R101 at L457) and no ledger row (LED grep "454": no hit). Same class as prior M1 (CC L326) | FAIL (A2) |
| FORWARD | 57 (LED L4) | 57 | none | none | PASS |
| ENTITY / DATE / QUALIFIER | 43 / 37 / 92 (LED L3, L5, L6) | 43 / 37 / 92 (sum 229 by grep) | none | none | PASS |
| Ledger units to A4 | 334 structured + 1 ledger-only (M1) | 335 | none: Review L851 marks all 335 reviewed; M1 cited at L856, L1038, L1071-L1072, L1352 | n/a | PASS |
| A3 concall findings to A4 | 25 (Review L864) | 25 | none; CC-F7-04 now has monitoring row M36 (L1348, L1399) | n/a | PASS |
| Ledger row M1 turn label | T39, "Vignesh IAF seamless spend question, Q5" (LED L480) | T35, Batra, Q4 slot. CC L325-L326 = src 304-305 (block 4 offset +21), inside the ledger's own T35 (src 303-306, LED L73) and Q4 (T31, T33, T35, LED L112). LED T39 (src 324-338) is the management answer at CC L345-L359. A4 records the conflict (Review L856) | n/a | n/a | CONTRADICTION (A2) |

Numbers that sit only in a non-NUMBER row (content captured, no unit lost): CC L196 "around 80" receivable days in FORWARD R175; CC L211 "100%" in R177; CC L356 "50" in R192; CC L440 "100%" in R200; CC L453 "1 lakh" capacity in QUALIFIER R323. This extends prior S13 (uneven A1 tagging). STYLE L1-S8.

Coverage result: one fresh-pass unit missing from the structured file and the ledger (L1-M1, loop A2). One ledger label contradicts the ledger's own turn table and the fulltext (L1-C1, loop A2). No orphan rows.

---

## 3. ARITHMETIC AUDIT (new and changed figures)

Filed figures from RES L412-L508 (Rs Mn, x0.1 to Rs Cr). Deck shares from PPT L397, L787-L788.

| Metric | A4 value (Review line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| 6B specificity | 0.58 = 30 / 52; 0.60 with R198 (L1155-L1158) | 30 / 52 = 0.577; 31 / 52 = 0.596; same 30 IDs on my walk | STR L163-L219 | PASS |
| 6E archetype | OVERPROMISER (provisional) (L1182) | specificity > 0.5; provisional credibility 0.5 / 4 = 12.5% < 60% | Review L1001, L1158 | PASS (internal) |
| FY26-end / 30-Sep gross borrowings | 52.37 / 117.14 | 29.14 + 23.22; 77.94 + 39.20 | RES L458, L463 | PASS |
| FY27-end debt, management basis | ~149-159 (L965, L1076) | 110 + 39.20 = 149.20; 120 + 39.20 = 159.20 (= 117.14 + 32.06 / 42.06) | CC L335-L336, L367; RES L458, L463 | PASS |
| Undrawn term loan | ~32-42 "less ~78-80 drawn" (L965, L1076) | 110 - 77.94 = 32.06; 120 - 77.94 = 42.06; on "80": 110 - 80 = 30.00 | CC L375; RES L458 | PASS on the filed draw; wording STYLE L1-S3 |
| Debt multiples | 2.85-3.04x; 3.15-3.25x (L974, L1097, L1596) | 149.20 / 52.37 = 2.849; 159.20 / 52.37 = 3.040; 165 / 52.37 = 3.151; 170 / 52.37 = 3.246 | as above | PASS |
| Cash at allotment | Rs 39.75 Cr (L973, L1355, L1479) | 63.6 Cr / 30,00,000 units = Rs 212; 15,00,000 x 212 = 31.80 Cr; 25% of 15,00,000 x 212 = 7.95 Cr; total 39.75. Full conversion adds 23.85, total 63.60, which covers ~60 | CC L50; RES L238-L239; 25% upfront is Notion memory (Role 4 M18, L567) | PASS (split basis flagged as memory) |
| Axle volume QoQ | ~5-11% (L1085, L1429) | 10,000 / 9,500 = +5.3%; 10,500 / 9,500 = +10.5% | CC L223, L412, L413 | PASS |
| Trailer value QoQ | ~53% (deck basis 54.7%) | 115 / 75 = +53.3%; 115.92 / 74.95 = +54.7% | CC L238-L242; PPT L397; RES L412 | PASS |
| Value per axle QoQ | ~39-47% (L1085, L1461) | 1.533 / 1.105 = 1.387; 1.547 / 1.053 = 1.469 | as above | PASS (38.7% rounds to 39) |
| Trailer share of QoQ rise | ~81% (L1428) | (115.92 - 74.95) / (235.09 - 184.34) = 40.97 / 50.75 = 80.7% | PPT L397; RES L412 | PASS |
| Top-5 share of QoQ rise | ~81% (L1428) | (64.21% x 235.09 - 59.47% x 184.34) / 50.75 = (150.95 - 109.63) / 50.75 = 81.4% | PPT L788; RES L412 | PASS |
| Brief margins | op 13.02% "rose"; GM 43.90% from 46.23% (L1426) | Q2 FY27 op 306.00 / 2,350.92 = 13.02%; Q2 FY26 147.53 / 1,309.20 = 11.27%; Q1 FY27 12.23%; GM 1,032.14 / 2,350.92 = 43.90%; Q2 FY26 605.19 / 1,309.20 = 46.23% | RES L412-L420 | PASS (op margin rose YoY and QoQ) |
| 7A new rows | PAT +143.5%; PBT +127.9%; H1 FY26 270.28 (L1198-L1200) | 196.86 / 80.84 = 2.435; 269.54 / 118.27 = 2.279; 2,702.75 Mn | RES L412, L422, L427 | PASS |
| 7A WC-cycle gap | ~30-35 days (L1205) | 124.4 - 95 = 29.4; 124.4 - 90 = 34.4 | Review L287 | PASS |
| Brief H1 vs H2 FY26 | revenue +4.1%; core PBT -12.1% (L1425) | 4,194.31 / 4,029.26 = 1.041; 423.81 / 482.32 = 0.879 | RES L412-L422 | PASS |
| Brief CFO / PAT | 14.3% (L1432) | 47.28 / 331.63 = 14.26% | RES L427, L496 | PASS |
| H2 deck band | 461-482 (L1439, L1487) | 1.10 x 419.43 = 461.37; 1.15 x 419.43 = 482.34 | RES L412; PPT L102 | PASS |
| Q1-Q22 status totals | 0 / 11 / 1 / 10 (L1345) | 22 rows tally | Review L1322-L1343 | PASS |
| 4A grade count | A3 B14 C4 D1 E1 none1 (L1051) | 24 rows tally | Review L1026-L1049 | PASS |

Arithmetic result: every new or changed figure ties within rounding. No mismatch above rounding.

---

## 4. ADVERSARIAL READ (new and changed text only; same bar for bull and bear, Master v3.7 Rule J)

Acquisition-economics probe: NOT APPLICABLE. The call describes no acquisition, purchase or stake buy. The preferential issue (CC L49-L50; RES L238-L239) is a fundraise. Seamless, shaft, robotics and cold drawn lines (CC L98-L107, L288) are capex. No price-to-target-earnings multiple exists to test.

Prior P1-P3 (trailer step sustainable; receivables improving; seamless margin): counters from the prior audit are now in the body (Exchange 3 L1085; 7A L1203-L1205; Q30 L1359). The P1 graft is incomplete in the brief (L1-M2).

### New-text claim A (bull side): "It expects full retrospective compensation for steel and conversion costs, mostly in Q3 and Q4 [MGMT-CALL]" (brief L1431; same merge in Step 2 L959)
- Counter from the same text: the call dates only the conversion settlement. "We have very recently settled with most of our OEMs and TAFE companies on a conversion front ... that impact would be coming in ... quarter 3, mostly in quarter 3 and quarter 4" (CC L474-L477). The retrospective claim has no date: "We do believe all of it will be compensated obviously ... retrospective ... There will be compensation retrospective, but there's a lot of escalation and settlements are underway" (CC L485-L489). Steel catch-up is also undated ("there will be further", CC L471-L472), and OEMs expect another steel increase in Q3 (CC L479). The body keeps the two apart (Exchange 1 "Said specifically", L1066).
- Survives: YES. The brief puts a Q3-Q4 date on the steel and full-compensation claim, which the extract does not support. That date feeds the brief's bull reading ("price recovery lands in Q3 and Q4", L1437). It is the bull-side mirror of prior F2. Finding L1-F1 (FACTUAL, A4).

### New-text claim B (bear side): "Trailer revenue rose about 53% from Q1, but axle volume rose only about 5-11% [MGMT-CALL]. Most of the step was suspensions and price." (brief L1429)
- Counter from the same text: the Q1 base of 9,500 is an analyst's recall (CC L413), not a management statement. Management did not contest it ("Yeah, there has been a growth on the actual and a lot on the suspension plus ... prices", CC L415-L416). The H1 "20,000 numbers" metric is unclear (CC L224-L225 sits inside a suspension sentence; STR L58). "Most" is A4's arithmetic reading, not a management word. The arithmetic itself ties (section 3).
- Survives: YES, as a dropped qualifier. The body carries the caveat (Exchange 3 L1085; 5A L1109). The brief tags the derived figure [MGMT-CALL] with no caveat. The prior fix (M3) named this caveat for the brief line. Direction holds; the evidence tier is overstated. Finding L1-M2 (MISSING, A4).

### New-text claim C (bull side of the debt readings): "Gross debt within the management-basis Rs 149-159 Cr" (forward map L1488)
- Counter: the 149-159 range assumes working-capital debt flat at the filed Rs 39.20 Cr and treats filed non-current borrowings as the whole term-loan draw. Current maturities are not split (7A L1207, ND). At the stated CC limit of ~Rs 32 Cr (CC L376), the figure would be ~Rs 142-152 Cr.
- Survives: NO new gap. Q24 already asks for CC-limit use against filed current borrowings (L1353). The fork wording leaves gaps (STYLE L1-S4).

### Consistency with the Role 4 body
- 81% / 81% (brief L1428) matches Role 4 Step 4 note B and flag (5) (L626). Gross-margin history and thresholds (brief L1474) match 8C (L486-L493). Re-engage trigger 1 status matches 6B (L399). Cash class and verdict match Role 4 (L306, L623). Debt and preferential figures match Step 5 (L290, L304). No contradiction found.

---

## 5. FINDINGS (tagged)

| ID | Type | Loop | Gap (exact) | Fix |
|---|---|---|---|---|
| L1-M1 | MISSING | A2 | Fresh-pass NUMBER unit absent from the structured file and the ledger: CC L454, analyst-spoken "So phase 1 would be 2 percent of that" (ASR garble of the seamless phase-1 share; management answers 30%, CC L458, R102). Turn T58 (src 432, LED L96). Low materiality; the coverage rule is categorical, as with prior M1 | A2: add ledger-only row M2 via MISSING_FROM_STRUCTURED (ANALYST_FIGURE, ASR_GARBLE), NUMBER units 107. A3: one-line disposition for that row only. A4: cite it (4A row 21 already spans L453-L457) and update the preamble counts (L851, L856) |
| L1-C1 | CONTRADICTION | A2 | Ledger row M1 places CC L325-L326 at T39 "Vignesh IAF seamless spend question, Q5" (LED L480). The ledger's own turn table and question ledger put src 304-305 in T35, Batra, Q4 (LED L73, L112); the fulltext agrees (CC L298-L299, L324-L326). A4 records the conflict (Review L856) | A2: relabel M1 to T35 (Shubham Batra, Q4 slot) in the same pass as L1-M1. A4: drop the conflict note at L856 and L1506 once the ledger agrees |
| L1-F1 | FACTUAL | A4 | Brief L1431 and Step 2 L959 date the full retrospective compensation of steel and conversion costs to "mostly Q3 and Q4". The call dates only the conversion-settlement impact to Q3-Q4 (CC L474-L477). Retrospective compensation is undated, with settlements "underway" (CC L485-L489); steel catch-up is undated (CC L471-L472) | Brief L1431, for example: "It expects all cost increases to be compensated retrospectively, but gave no date; settlements are 'underway'. The conversion-cost settlement should show mostly in Q3 and Q4 [MGMT-CALL]." Step 2 L959: split the two claims the same way |
| L1-M2 | MISSING | A4 | Brief L1429 tags "axle volume rose only about 5-11%" as [MGMT-CALL] and drops the caveat that the Q1 base of 9,500 is an analyst's recall (CC L413), which prior M3 named for this line. "Most of the step was suspensions and price" is A4's arithmetic reading of CC L415-L416, untagged | Brief L1429, for example: "...axle volume rose only about 5-11% [MGMT-CALL, INFERENCE: the Q1 base of 9,500 is an analyst's figure that management did not contest]. Most of the step was suspensions and price [INFERENCE]." |

---

## 6. VERDICT

INCOMPLETE.
- Failing agents and loop: A2 first (L1-M1 one row; L1-C1 one label), then A3 (disposition for the one new row only), then A4 (L1-F1, L1-M2, and the citation for the new row). loop_back_to is A2 because the chain starts there. Every fix is one row, one label or one sentence.
- Types that trigger the loop: MISSING (L1-M1, L1-M2), CONTRADICTION (L1-C1), FACTUAL (L1-F1).
- What does not change: the brief gate passes; arithmetic ties; all seven prior items are closed in the body; Role 4 verdict PROCEED WITH FLAGS, cash class INDETERMINATE-WITH-DIRECTION, net concall impact WEAKENED and archetype OVERPROMISER (provisional) stand.

---

## 7. STYLE NOTES (logged; no loop)

| ID | Where | Note and fix |
|---|---|---|
| L1-S1 | Review L1427 | "So the margin gain came from volume, not price." is an untagged inference; add [INFERENCE] |
| L1-S2 | Review L1428 | "came from trailer axles": the deck segment is "Trailer Axles and Suspensions" (PPT L787). The next line says most of the step was suspensions and price. Say "the trailer axle and suspension segment" |
| L1-S3 | Review L965, L1076 | "less ~78-80 drawn ... leaves ~Rs 32-42 Cr": 110 - 80 = 30. The 32-42 range and 149-159 use the filed 77.94. Say "less the filed Rs 77.94 Cr" |
| L1-S4 | Review L1488 | Debt forks leave Rs 159-165 Cr unassigned, and "within Rs 149-159 Cr" excludes a print below 149 (for example ~142-152 at the stated ~Rs 32 Cr CC limit). Use "at or below Rs 159 Cr" and name 159-165 as inconclusive |
| L1-S5 | Review L1483 | Top-5 share falling appears in both forks; trailer revenue is the discriminator. Say so: bull = share holds or falls while trailer revenue holds; bear = both fall |
| L1-S6 | Review L1454 | "makes about 4,000-4,500 trailer axles a month" sits against Q2 ~10,000-10,500 a quarter (~3,300-3,500 a month; CC-F16-01, Q31 L1360). Add the conflict as a qualifier. Likely unchanged text; logged only |
| L1-S7 | LED L475, L509 | Ledger line "MISSING_FROM_STRUCTURED none" is stale against section 11 (LED L477-L480); the analyst_note still says 15 analyst-spoken NUMBER rows. Align in the A2 pass for L1-M1 |
| L1-S8 | STR L163-L219, L341 | Some numbers sit only in FORWARD or QUALIFIER rows (CC L196 in R175, L211 in R177, L356 in R192, L440 in R200, L453 in R323). Content captured; extends prior S13 |

---

```yaml
stage: A5-adversary
company: "KROSS"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
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
    - "CC L454: analyst-spoken 'So phase 1 would be 2 percent of that' (NUMBER, ANALYST_FIGURE, ASR_GARBLE; T58 src 432); no structured row (R323 is L453, R101 is L457) and no ledger row"
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "Brief L1431 / Step 2 L959: full retrospective compensation for steel and conversion costs, mostly in Q3 and Q4", counter: "Only the conversion-settlement impact is dated Q3-Q4 (CC L474-L477); retrospective compensation is undated, settlements 'underway' (CC L485-L489); steel catch-up undated (CC L471-L472); OEMs expect another steel rise in Q3 (CC L479)", source_line: "CC L471-L489", type: FACTUAL}
  - {claim: "Brief L1429: axle volume rose only about 5-11% QoQ [MGMT-CALL]; most of the step was suspensions and price", counter: "Q1 base 9,500 is an analyst's recall (CC L413), uncontested; 'most' is A4 arithmetic on CC L415-L416; body carries the caveat (L1085, L1109), the brief drops it though prior M3 required it", source_line: "CC L223, L412-L416", type: MISSING}
findings_by_type:
  factual:
    - "L1-F1 (A4): brief L1431 and Step 2 L959 date full retrospective compensation of steel and conversion to 'mostly Q3 and Q4'; the call dates only the conversion settlement (CC L474-L477); retrospective compensation undated (CC L485-L489)"
  missing:
    - "L1-M1 (A2): CC L454 analyst figure 'phase 1 would be 2 percent of that' has no structured or ledger row; add ledger-only row M2 via MISSING_FROM_STRUCTURED; A3 one-line disposition; A4 cite"
    - "L1-M2 (A4): brief L1429 drops the analyst-recall caveat on the Q1 base (CC L413) that prior M3 required and tags the derived 5-11% as MGMT-CALL; retag MGMT-CALL plus INFERENCE with the caveat; tag 'most of the step' INFERENCE"
  contradiction:
    - "L1-C1 (A2): ledger row M1 says T39 Vignesh Q5 (LED L480); ledger's own T35 (LED L73) and Q4 row (LED L112) and the fulltext (CC L298-L326) put it in Batra's Q4 question; relabel to T35"
  style:
    - "L1-S1: Review L1427 untagged inference; add INFERENCE"
    - "L1-S2: Review L1428 'trailer axles' should be the trailer axle and suspension segment (PPT L787)"
    - "L1-S3: Review L965, L1076 'less ~78-80 drawn leaves 32-42': say 'less the filed Rs 77.94 Cr'"
    - "L1-S4: Review L1488 debt forks leave 159-165 unassigned; 'within 149-159' excludes lower prints"
    - "L1-S5: Review L1483 top-5 share falling appears in both forks; name trailer revenue as the discriminator"
    - "L1-S6: Review L1454 4,000-4,500 axles/month vs Q2 ~10,000-10,500 per quarter; add the conflict"
    - "L1-S7: LED L475, L509 stale 'MISSING_FROM_STRUCTURED none' and analyst-row count; align in the A2 pass"
    - "L1-S8: some numbers sit only in FORWARD or QUALIFIER rows (CC L196, L211, L356, L440, L453); content captured; extends S13"
loop_back_to: "A2"
gap: "A2: add ledger-only row M2 for CC L454 analyst figure 'phase 1 would be 2 percent of that' (ANALYST_FIGURE, ASR_GARBLE, T58) via MISSING_FROM_STRUCTURED (L1-M1), and relabel row M1 from T39/Vignesh/Q5 to T35/Batra/Q4 (L1-C1). A3: disposition for the new row only. A4: cite the new row and update preamble counts; L1-F1 split the brief L1431 and Step 2 L959 sentence so only the conversion settlement carries the Q3-Q4 date and retrospective compensation stays undated (CC L474-L489); L1-M2 retag brief L1429 as MGMT-CALL plus INFERENCE with the analyst-recall caveat on the Q1 base (CC L413) and tag 'most of the step' INFERENCE."
style_notes:
  - "L1-S1 to L1-S8 logged in runs/kross-q2fy27/work/audit_kross_q2fy27_role5_loop1.md section 7; no re-run"
analyst_note: "Role 5 loop 1 re-audit on a machine transcript; filed numbers win. The brief gate passes. All seven prior items are closed in the body. The 6B recount ties at 30/52 = 0.58 on my own walk, so OVERPROMISER holds. Debt readings tie: 149.20-159.20 on sanction plus filed WC, 2.85-3.04x; 165-170 is 3.15-3.25x. Allotment cash ties at Rs 39.75 Cr. The 81%/81% and QoQ volume figures tie. Four small defects remain. Coverage: CC L454 carries an unrowed analyst figure, the same class as prior M1, so the chain restarts at A2. A2 also labelled M1 as T39 when its own turn table says T35. In the brief, the F2 rewrite dates full retrospective compensation to Q3-Q4, but the call dates only the conversion settlement. That is the bull-side mirror of F2. The brief also drops the analyst-recall caveat on the 5-11% QoQ volume figure that M3 required. Each fix is one row, one label or one sentence. Verdict, cash class, net impact and archetype stand."
```
