# A5 ADVERSARY AUDIT: Kross Limited (KROSS), Q2 FY27, ROLE 5 ADDENDUM

Agent: A5 adversary | model claude-opus-5-5 | date 2026-10-20
Scope: the ROLE 5 ADDENDUM (Review L829-L1574) and its PLAIN-LANGUAGE BRIEF (UPDATED) (Review L1399-L1469), which replaces the Role 4 brief in full (Review L1401). Role 4 text is checked only where it meets the addendum.
Inputs read: A4 review (runs/kross-q2fy27/work/review_kross_q2fy27.md); A1 concall fulltext and structured file (primary); A1 results, press-release and deck fulltexts (filed cross-checks); A2 concall ledger. Not read: source files, inputs/, A3 reasoning (A3 finding IDs were listed by an ID-only grep for the coverage tie).
SOURCE CAVEAT (binds every finding below): the concall is a MACHINE TRANSCRIPT (faster-whisper; CC L2, L19). Speakers are inferred. Numbers may be mis-heard. Where a call number meets a filed number, the filed number wins.

Anchor key: CC Lnnn = concall fulltext line. STR Lnnn = concall structured file line. LED Lnnn = A2 concall ledger line. RES / PR / PPT Lnnn = results, press-release, deck fulltext lines. Review Lnnn = A4 review line.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

Brief under test: PLAIN-LANGUAGE BRIEF (UPDATED), Review L1399-L1469.

| Part | Heading line | Content | Status |
|---|---|---|---|
| 1. Summary narrative | Review L1403 | 16 lines (L1404-L1419), about 260 words; bull reading, bear reading and separating observations present | present |
| 2. Sector intelligence | Review L1421 | 7 lines (L1422-L1428) | present |
| 3. Business-model intelligence | Review L1430 | 13 lines (L1431-L1443) | present |
| 4. Competition intelligence | Review L1445 | 6 lines (L1446-L1451) | present |
| 5. Forward map | Review L1453 | make-or-break line plus 12 catalyst rows (L1458-L1469), each with a bull and a bear fork; two rows undated (preferential, HPML), recorded as ND, as accepted at Role 4 (Review L813, A5-S9) | present |

Gate: PASS. All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Method: my own pass over the concall fulltext (CC L18-L509, 487 source lines in 5 blocks). I mapped the A1 speaker-turn index (STR L354-L419) to fulltext lines (offset +18 / +19 / +20 / +21 / +22 by block), greped the question hand-offs, and walked every numeric token, forward statement, date, qualifier and entity. Then I diffed against the A2 ledger (LED L1-L474) and checked each ledger unit against A4's citations.

| Category | A2 count | My fresh count | Orphan rows (ledger, absent from A4) | Missing from ledger | Status |
|---|---|---|---|---|---|
| Speaker turns | 65 (LED L7, L35-L102) | 65 | none: every turn sits inside a cited CC range (0B L885-L891 for T1-T3; Step 1 L913-L942 for T4-T6; 4A L1025-L1048 for T8-T63; 0B L891 and 0C L897 for T64-T65); T15/T21 moderator turns covered by R178 (6B L1149) and the 4A ranges | none | PASS |
| Question slots / unique analysts / analyst turns | 9 / 7 / 22 (LED L8, L105-L116) | 9 / 7 / 22 (hand-offs at CC L137, L201, L250, L298, L341, L360, L401, L462, L490) | none (4A rows 1-24 cover all 9 slots) | none | PASS |
| NUMBER | 105 (LED L2) | 106 | none | CC L326: analyst-spoken seamless figure "1 6 3 7 or 4 routes" (ASR garble; "routes" = crores as elsewhere, cf. CC L333 "corollars", L356 "corrodes"). STR has only the question row R299 (STR L317). A1 rows every other analyst figure as NUMBER (R039, R040, R044, R068, R070, R081, R082, R086, R088, R095, R097, R098, R101, R103) | FAIL (A2) |
| FORWARD | 57 (LED L4) | 57 content units | none | none. Two restatements carry no new content: CC L95-L97 (focus on backward integration, cost, capacity; content in R151, R153, R162-R165) and CC L192 ("it would be getting better", content in R174-R175) | PASS |
| DATE | 37 (LED L5) | 37 rowed | none | none in content. A1 tags date tokens inside some FORWARD rows (R215 for CC L56, R218 for L73) and not others (CC L158-L159 in R173, L211 in R177, L274 in R180, L319 in R184, L355-L357 in R191/R192, L441 in R200, L479 in R331, L363 in R082). Each date sits verbatim in an existing row | PASS (STYLE S13) |
| QUALIFIER | 92 (LED L6) | 92 content units | none | none. CC L434-L435 (like-for-like competition) restates R319-R321; CC L483-L484 (industry escalation) restates R205 | PASS |
| ENTITY | 43 (LED L3) | 43 | none | none (furnace and piercing mill CC L330 inside R300; Diwali CC L269 inside R285; GST CC L157 inside R227) | PASS |
| Structured IDs to A4 | 334 (LED L9) | 334 | none: Review L851 marks all 334 "reviewed"; spot-check of material rows below | n/a | PASS |
| A3 concall findings to A4 | 25 (Review L863) | 25 distinct IDs (CC-F6-01..09, F7-01..05, F16-01..02, F17-01..09) | none; CC-F7-04 is routed "to monitoring" (Review L1333) but no M21-M35 row names it | n/a | PASS (STYLE S9) |

Spot-check of material rows marked reviewed: R006 PAT +143% (STR L16) ties to filed +143.5% (196.86 / 80.84, RES L427); R020 PBT ">100%" (STR L30) ties to +127.9% (269.54 / 118.27, RES L422); R025 H1 FY26 revenue 270 (STR L35) ties to 270.28 (RES L412). None is cited in 7A (STYLE S5). R097 Q1 axle volume 9,500 (STR L107, analyst recall, not contested) is reviewed but unused; its substance is a surviving bear counter (finding M3).

Coverage result: one fresh-pass unit missing from the structured file and ledger (finding M1, loop A2). No orphan rows.

---

## 2. ARITHMETIC AUDIT

All filed figures recomputed from RES L412-L508 (Rs Mn, x0.1 to Rs Cr) and deck lines. Call figures from CC lines.

| Metric | A4 value (Review line) | Recomputed | Source line | Status |
|---|---|---|---|---|
| Q&A share of call | 37 min 48 s = 76% (L898) | 2,268 / 2,968 s = 76.4% | CC L133, L495, L509 | PASS |
| Results-to-call gap | 2 days (L896) | 17-Oct to 19-Oct = 2 | RES L18; CC L18 | PASS |
| Quantified opening claims | 17 / 30 = 57% (L945) | 17 / 30 = 56.7% | Review L913-L942 | PASS |
| Quantified forward claims | 5 / 11 = 45% (L945) | 5 / 11 = 45.5% | Review L913-L942 | PASS |
| H2 at +20% / FY27 | ~503 / ~923 (L972) | 1.2 x 419.43 = 503.32; 922.75 | RES L412; CC L64 | PASS |
| H2 at deck +10-15% | 461-482 (L972) | 461.37-482.34 | PPT L102 | PASS |
| Preferential cash at allotment | 39.75 Cr (L972) | 31.8 + 7.95 = 39.75 (63.6 / 2 = 31.8 ties to CC L50) | CC L50; Notion memory | PASS |
| FY26-end gross borrowings | 52.37 (L973) | 29.14 + 23.22 = 52.37 (291.42 + 232.23 Mn) | RES L458, L463 | PASS |
| 30-Sep gross borrowings | 117.14 (L1075) | 77.94 + 39.20 = 117.14 | RES L458, L463 | PASS |
| FY27-end debt multiple | ~3.2x (L973, L1075, L1094, L1413) | 165 / 52.37 = 3.15; 170 / 52.37 = 3.25 | CC L373-L374 | PASS on arithmetic; input range incomplete (finding M2): sanction reading gives 149.2-159.2 Cr = 2.85-3.04x |
| Credibility ratio | 12.5%; 16.7%; 25.0% (L1000-L1001) | 0.5 / 4; 0.5 / 3; 0.5 / 2 | Review L986-L995 | PASS |
| 4A grade count | A3 B14 C4 D1 E1 none1 (L1050) | 24 rows tally | Review L1025-L1048 | PASS |
| Trailer value YoY / QoQ | +98% / +53% (L1081) | 115 / 58 = 1.983; 115 / 75 = 1.533 | CC L238-L244 | PASS |
| Value per axle YoY | "about 28-32%" (L1083) | 1.983 / 1.55 = 1.279; 1.983 / 1.50 = 1.322 | CC L229-L235, L242 | PASS on number; wording STYLE S1 |
| Run rate per quarter | 12,000-13,500 (L1083) | 4,000-4,500 x 3 | CC L209-L214 | PASS |
| QoQ trailer rise | ~41 Cr (L1084) | 115.92 - 74.95 = 40.97 | PPT L395-L397 x RES L412 | PASS |
| Other four of top 5 | ~12% each (L1099) | (64.21 - 15 to 16) / 4 = 12.05-12.30 | PPT L788; CC L398 | PASS |
| Trailer revenue, deck x filed | 115.92 / 74.95 / 57.05 (L1104, L1199) | 49.31% x 235.09; 40.66% x 184.34; 43.58% x 130.92 | PPT L395-L397; RES L412 | PASS |
| Specificity ratio | 0.43 = 23 / 53 (L1149-L1152) | 23 / 53 = 0.434 on A4's count; uniform count under A4's own rule = 31 / 52 = 0.60 (31 / 53 = 0.58); minimal pairwise fix = 28 / 52 = 0.54 | STR L163-L219; LED L227-L286 | FAIL: count (finding F1) |
| Hedge count | 17 (L1157-L1162) | 3 + 2 + 5 + 5 + 2 = 17 (grep: "we expect" CC L45, L63, L77, L87, L125; hope family L150, L304, L307, L332, L357, analyst L139 excluded; believe L479, L485) | CC lines as listed | PASS |
| Receivable days H1 / Q2 / like-for-like | 90.0 / 80.7 / 89.1 (L1189-L1190) | 206.29 / 419.43 x 183 = 90.01; 2,062.91 / 2,350.92 x 92 = 80.73; 197.17 / 402.93 x 182 = 89.06 | RES L412, L448 | PASS |
| Exports share of revenue | ~4.1% (L1201) | 8% x 50.69% = 4.06% | CC L82; PPT L395 | PASS |
| Seamless margin, company basis | ~1.5-2.0 pts (L1344) | 3-4% x 49% = 1.47-1.96 | CC L449-L451, L119 | PASS |
| Tipping jacks by Q4 | 400-480 / month (L961, L987) | 50-60% x 800 kits/month | CC L257-L258; PPT L236 | PASS |
| 7A Q2 revenue, EBITDA, margin, PBT, PAT | 235.09; 30.60; 13.02%; 26.95; 19.69 (L1185-L1187) | 2,350.92; 2,350.92 - 1,339.24 + 20.46 - 107.22 - 618.92 = 306.00; 13.016%; 269.54; 196.86 | RES L412-L427 | PASS |
| 7A H1 EBITDA | 53.32 (L1188) | 533.18 Mn on the H1 column; Q1 + Q2 = 225.53 + 306.00 = 531.53 Mn (53.15 Cr) | RES L412-L421, L564-L566 | PASS (the call repeats the H1 column, which carries the 1.65 Mn footing gap; STYLE S5) |
| Short-term borrowing rise | +15.98 Cr (L1194) | 159.75 Mn | RES L508; L463 | PASS |
| H1 capex / CWIP | 59.16 / 54.92 (L1195) | 591.60 / 549.16 Mn | RES L497, L439 | PASS |
| Operating margin QoQ | +79 bps (L1197) | 13.02 - 12.23 (13.016 - 12.235 = 78 bps unrounded) | RES L412-L421 | PASS (rounding) |
| Gross margin QoQ / YoY | -89 / -232 bps (L1196) | 43.904 - 44.792; 43.904 - 46.226 | RES L412-L416 | PASS |
| Brief core PBT, +129.9% | 24.78 (L1405) | 247.81 / 107.80 = 2.299 | RES L412-L422 | PASS |
| Brief H1 vs H2 FY26 | revenue +4.1%, core -12.1% (L1407) | 4,194.31 / 4,029.26 = 1.041; 423.81 / 482.32 = 0.879 | RES L412-L422 | PASS |
| Brief CFO / PAT | 4.73 Cr, 14.3% (L1412) | 47.28 / 331.63 = 14.26% | RES L427, L496 | PASS |
| Reg 33 dates | 14-Feb-2027; 30-May-2027 (L1369, L1375) | 31-Dec + 45; 31-Mar + 60 | rule | PASS |
| Q1-Q22 status totals | 0 / 11 / 1 / 10 (L1330) | 22 rows tally | Review L1307-L1328 | PASS |

Arithmetic result: every derived number ties within rounding. One count fails under A4's own stated rule (F1). One input range is incomplete (M2).

---

## 3. ADVERSARIAL READ (bull and bear at the same bar, Master v3.7 Rule J)

Acquisition-economics probe: NOT APPLICABLE. The call describes no acquisition, purchase or stake buy. The preferential issue (CC L49-L50) is a fundraise; the seamless, shaft, robotics and cold drawn lines (CC L98-L107, L288) are capex. No price-to-target-earnings multiple exists to test.

### 3A. The three most positive claims, each with its strongest bear counter

P1. Trailer revenue ~Rs 115 Cr in Q2, +53% QoQ, sustainable "in this range or higher" in Q3-Q4 (CC L238-L242, L318-L320); Q2 volumes a record (CC L67); Q3-Q4 volumes stronger (CC L63).
- Strongest bear counter, from the same text: axle VOLUME rose only about 5-11% QoQ. Q2 was "in excess of 10,500" (CC L223), later "in excess of 10,000" (CC L412). Q1 was 9,500 (analyst recall, CC L413, not contested), which ties to the H1 figure, "almost crossed 20,000" (CC L225), less Q2 ~10,500. Trailer VALUE rose 53% (115 / 75, CC L238-L242; 54.7% on deck shares x filed revenue, PPT L395-L397, RES L412). So value per axle rose about 39-47% in one quarter. Management assigns the rest to suspensions and price: "a lot on the suspension plus due to commodity increases there has been a surge in prices as well" (CC L415-L416). Suspension volumes were not given; they were promised privately (CC L408-L417). The "sustainable" answer trails off: "unless something" (CC L323). Part of Q2 was monsoon-deferred buying (CC L148-L153) and Chhattisgarh orders (CC L313-L316).
- Survives: YES. The addendum carries the YoY version only (volume +50-55% vs value +98%, Review L1081-L1083), plus Q32 (L1346) and M23 "guidance (hedged)" (L1369). The QoQ figure, which is the sharper test of the Q2 step, is absent, and the brief line "axle volume grew less than value" (L1411) sits beside a QoQ revenue move without the QoQ volume. Must be grafted (finding M3). Caveat: machine transcript; 9,500 is an analyst recall; the 20,000 metric is unclear (STR L58).

P2. Receivables improving: Q2 ~81 days, target ~80, WC cycle under 90-95 days (CC L190-L197).
- Strongest bear counter: 81 days is on quarter revenue, which growth flatters; on a like-for-like half basis days are flat at 89.1 to 90.0 (RES L412, L448; Review L284). The filed cash cycle is 124.4 days (Review L287), about 109 days on revenue days (inventory 1,096.56, payables 657.28, receivables 2,062.91 Mn on H1 revenue, RES L446-L448, L465-L466), against the "<90-95" target, undated and with no basis.
- Survives: YES, and incorporated (7A L1190, 8B #2 L1242, Section 5 L1389-L1390). The cash-cycle gap is not stated beside the target (STYLE S6; no conclusion changes).

P3. Seamless backward integration: 8-10% below buying price, "3 to 4 percent" margin, full integration by end H1 FY28 (CC L438-L451).
- Strongest bear counter: the basis is axles or overall, unclear (CC L449-L451; ~1.5-2.0 pts at company level on a 49% trailer share); "commodity prices keep changing quite significantly" (CC L446); equipment still "in transit", trials "hopefully" by end Q4 (CC L331-L333); phase 1 is 30% of capacity (CC L458); the ~Rs 120 Cr spend vs CWIP 54.92 Cr question was lost in the audio gap (CC L491-L494; RES L439).
- Survives: YES, and incorporated (Q30 L1344, Q36 L1350, 8A L1228, M31 L1377).

(Also tested: "price revisions concluded" and "all of it will be compensated ... retrospective" (CC L56-L57, L485-L489). Counter: gross margin fell 89 bps QoQ after the revisions (RES L412-L416); OEMs expect another steel increase in Q3 (CC L479). Incorporated in Exchange 1, L1062-L1068.)

### 3B. The addendum's three heaviest bear claims, each with its strongest bull counter (same bar)

N1. "FY27-end gross debt ~Rs 165-170 Cr, ~3.2x FY26-end", called "confirmed" (Q24 L1338) and stated as fact in the brief: "Debt will reach about Rs 165-170 Cr by March 2027" (L1413).
- Strongest counter: 165-170 is the analyst's sum, 115 + "that 50 crores which we have not drawn" (CC L371-L374), answered "Yeah, correct" and then "our total term loan is that 80 crores ... CC limit ... approximately 32 crores. The further which will go on is basically on the balance of the seamless [loan]" (CC L375-L377). Management's own term-loan figure is 110 (CC L335-L336) or "110-120" (CC L367). Filed non-current borrowings are 77.94 Cr (RES L458), and the H1 long-term draw of 48.80 Cr (RES L506) ties to the first answer, "spent approximately 50 crores ... from our term borrowing" (CC L328). So the undrawn balance is about 30-42 Cr, not 50. With working-capital debt flat at the filed 39.20 Cr (RES L463), FY27-end gross debt is about 117.14 + 32.06 to 42.06 = Rs 149-159 Cr, 2.85-3.04x FY26-end. The analyst's 50 matches the "balance capex of close to 50 odd crores" (CC L350-L351), and CC L366 puts "50 crores" on internal accruals. The 165-170 reading needs a 70 Cr draw (CC L338-L339) on a 120 Cr sanction.
- Survives: YES. The extract supports a range of about Rs 149-170 Cr, not one figure. Direction is unchanged (debt roughly triples before seamless revenue). The addendum names the conflict in the body (4A grade "conditional, conflicting", L1039; Q23 asks for the sanction, L1337) but carries only the top of the range into Step 2 (L964), Exchange 2 (L1075), 5A (L1094), 8A (L1235), 8D (L1261), 8E (L1272), Key Notes (L1287), Q24 (L1338), M29 (L1375), Section 5 (L1395), the brief (L1413, L1468) and YAML flags (L1567). The brief also drops the filed 30-Sep level of Rs 117.14 Cr that the Role 4 brief carried (L644). Finding M2.

N2. "Margin guide withdrawn in effect" and, in the brief, "It said a return is 'difficult currently'" (L1409).
- Strongest counter: the question was WHEN: "would be difficult to give a sense of when we can return to maybe like a guided 14-15% kind of a [EBITDA] margin" (CC L480-L481). The answer was "Yeah, it is difficult currently" (CC L482). A1 reads it the same way: "difficult currently to say when return to guided margin" (R332, STR L350). Management then said "We do believe all of it will be compensated obviously ... retrospective" (CC L485-L489), with conversion settled and its impact in Q3-Q4 (CC L474-L477).
- Survives: YES, in part. The body carries both readings (Exchange 1, L1067) and Step 2 shows its basis ("not reaffirmed, no date", L958). The brief changes the object from timing to feasibility. Finding F2.

N3. "Specificity 0.43 ... archetype EVASIVE (provisional)" (L1152, L1173-L1174), carried into Key Notes (L1287), the verdict block (L1293) and YAML (L1502-L1504).
- Strongest counter: A4's own rule is "Quantified (number, date or binary milestone)" (L1150). It counts R203, "conversion impact in Q3, mostly Q3 and Q4" (STR L217), but not R152, "price revisions ... expected to support Q3 and Q4" (STR L166). It counts R154, "expect Q3 and Q4 volumes stronger than Q2" (STR L168), but not R172 or R173, the same dated outlook (STR L186-L187). It counts R180 (Q3 agri, STR L194) but not R158 (Q3 agri, STR L172); R199 (Q4, STR L213) but not R200 (Q4, STR L214); R193 ("this financial year", STR L207) but not R185 (STR L199); and it leaves out R169 ("coming two quarters", STR L183) and R191 (H2, STR L205). R181 (STR L195) is the analyst speaking (CC L276-L277), like the excluded R197. A uniform count is 31 / 52 = 0.60; the minimal pairwise fix is 28 / 52 = 0.54. Both cross the 0.5 line that 6E uses.
- Survives: YES. The archetype label rests on a miscount. Finding F1.

### 3C. Internal consistency (addendum vs itself and vs the Role 4 body)

- Forward-map bull fork, preferential row (L1459): "Allotted on the approved terms; equity funds the Rs 60 Cr of H2 lines". The addendum's own Step 2 diagnostic (b) (L972) and flag (L1568) put cash at allotment at Rs 39.75 Cr; the balance needs warrant conversion, which Q26 (L1340) asks about. The bull fork cannot happen on allotment alone. Finding C1.
- Brief regression against a Role 4 A5 requirement: A5 loop 1 finding A5-F3 grafted bear counter B into the brief (change log L801: "Where: ... brief"): "About 81% of the rise from Q1 came from trailer axles, and about 81% came from the top 5 customers" (L642), with a Q3 test, "trailer and top-5 shares fall back" (L696). The updated brief replaces the Role 4 brief in full (L1401) but drops the 81% line, and its Q3 row keeps the trailer test but drops the top-5 test (L1463). Only a qualitative "Growth moved to the trailer half and to fewer customers" remains (L1440). Finding M4.
- No other contradiction found. Trigger statuses (8A L1225-L1235 vs Role 4 6D L423-L430), watchlist numbering (8B L1239-L1248 vs Role 4 6B L387-L397), Q1-Q22 topics (3A L1307-L1328 vs Role 4 L508-L534), verdict and cash class (Section 5 L1387-L1388 vs Role 4 L623-L624) all align.

---

## 4. FINDINGS (tagged)

| ID | Type | Loop | Gap (exact) | Fix |
|---|---|---|---|---|
| M1 | MISSING | A2 | Fresh-pass NUMBER unit absent from structured file and ledger: CC L326, analyst-spoken seamless figure "1 6 3 7 or 4 routes" (ASR garble, likely Rs Cr; cf. deck ~Rs 167 Cr, PPT L251). Only the question row R299 exists (STR L317). Low materiality; the coverage rule is categorical | A2: add the row (ANALYST_FIGURE, ASR_GARBLE) via MISSING_FROM_STRUCTURED, so A1 issues R335; A3: one-line disposition for that row only; A4: cite it or mark it reviewed |
| F1 | FACTUAL | A4 | 6B specificity 0.43 (23 / 53, Review L1149-L1152) miscounts under A4's own rule; uniform recount 31 / 52 = 0.60 (minimal 28 / 52 = 0.54) crosses the 0.5 line that sets EVASIVE in 6E (L1173-L1174) | State one rule and apply it to all 57 rows; drop R181 as analyst text; recount; re-derive the 6E archetype from the protocol matrix; align the verdict block (L1293), Key Notes (L1287), Section 5 flags (L1395) and YAML (L1502-L1504, L1565) |
| F2 | FACTUAL | A4 | Brief L1409, "It said a return is 'difficult currently'", changes the object from timing to feasibility; the extract says it is difficult to say WHEN (CC L480-L482; R332 STR L350), and management expects full retrospective compensation (CC L485-L489) | Reword, for example: "On the call, management did not confirm its 14-15% margin target. It said it is 'difficult currently' to say when margin returns there, and it expects retrospective compensation [MGMT-CALL]." |
| M2 | MISSING | A4 | FY27-end debt carries only the analyst's 165-170 Cr (3.2x) as "confirmed". Management's sanction (110, CC L335-L336; 110-120, CC L367) less ~78-80 drawn (CC L375; RES L458, L506) gives ~Rs 149-159 Cr (2.85-3.04x) with WC flat at the filed 39.20 Cr (RES L463). The brief also drops the filed Rs 117.14 Cr level | Carry both readings and the separating observation (sanction and drawn amount, Q23) in Step 2 L964, Exchange 2 L1075, 5A L1094, 8A L1235, 8D L1261, 8E L1272, Key Notes L1287 (label "gross"), Q24 L1338 (replace "was confirmed" with "an analyst's sum, which management assented to"), M29 L1375, Section 5 L1395, brief L1413 and L1468, YAML L1567. Keep "Borrowings were Rs 117.14 Cr at 30-Sep [FILED]" in the brief |
| M3 | MISSING | A4 | Surviving bear counter to P1 not grafted: QoQ axle volume +5-11% (CC L223, L225, L412-L413) against trailer value +53% (CC L238-L242), so value per axle rose ~39-47% QoQ, mostly suspensions and price (CC L415-L416) | Add the QoQ test to Exchange 3 implication (L1083) and the brief line (L1411), with the caveat that Q1 9,500 is an analyst recall in a machine transcript; tie it to Q32 and M23 |
| M4 | MISSING | A4 | Updated brief drops bear counter B that A5 loop 1 required in the brief (A5-F3, L801): the 81% / 81% concentration line (Role 4 L642) and the top-5 test in the Q3 row (Role 4 L696 vs updated L1463) | Restore one summary sentence (about 81% of the QoQ rise from the trailer half and about 81% from the top 5 [MGMT-DECK]) and add "top-5 share falls back" to the Q3 bear fork (and "top-5 share at or below 64.21%" or similar to the bull fork) |
| C1 | CONTRADICTION | A4 | Forward-map bull fork (L1459) says allotment lets equity fund the Rs 60 Cr of H2 lines; Step 2 (b) (L972) and flag (L1568) say allotment brings Rs 39.75 Cr | Bull fork: "Allotted, and warrants converted within H2 FY27, so equity funds the ~Rs 60 Cr of H2 lines (Rs 39.75 Cr lands at allotment)"; bear fork unchanged |

---

## 5. VERDICT

INCOMPLETE.
- Failing agents and loop: A2 first (M1, one row), then A3 (disposition for that one row only), then A4 (F1, F2, M2, M3, M4, C1). loop_back_to is set to A2 because the chain starts there; the A2 and A3 work is one row. The bulk of the correction is A4's.
- Types that trigger the loop: FACTUAL (F1, F2), MISSING (M1, M2, M3, M4), CONTRADICTION (C1).
- What does not change: the arithmetic ties; the brief is complete; Role 4 verdict PROCEED WITH FLAGS and the cash class INDETERMINATE-WITH-DIRECTION are not affected; the addendum's net reading (WEAKENED) likely holds after the fixes. The fixes change numbers and labels (debt range, archetype, brief wording), so they are not STYLE.

---

## 6. STYLE NOTES (logged; no loop)

| ID | Where | Note and fix |
|---|---|---|
| S1 | Review L1083 | "about 28-32% of the YoY value growth per unit" reads as a share of growth; say "value per axle rose about 28-32% YoY" |
| S2 | Review L1408 | "so the margin gain came from volume" has no referent after the operating-margin line was dropped; restore "Operating margin rose to 13.02% (+79 bps QoQ) [FILED]" |
| S3 | Review L1423 | "Part of the Q2 trailer jump was timing" is tagged [MGMT-CALL]; "timing" is [INFERENCE]; management also said Q3-Q4 should sustain or rise (CC L150, L158-L159) and every region contributed (CC L315-L316) |
| S4 | Review L1442 (also 5A L1098, 8D L1265) | "About 70% of seamless output will be sold outside, like a commodity [MGMT-CALL]": the call gives phase 1 = 30% of capacity for own use (CC L438-L458); outside sale of surplus capacity is in the deck (PPT L254); "like a commodity" is [INFERENCE]; say "capacity", not "output", and add the reading that phase 1 may be a 30% first build |
| S5 | Review L1185-L1188 | 7A omits three backward claims that tie (PAT +143% vs +143.5%; PBT ">100%" vs +127.9%; H1 FY26 revenue 270 vs 270.28); also note that the call's H1 EBITDA 53.32 repeats the H1 column, which carries the 1.65 Mn footing gap (Q1 + Q2 = 53.15, RES L564-L566) |
| S6 | Review L1201 area | Add a 7A row: WC cycle "<90-95 days" (CC L196-L197) vs filed cash cycle 124.4 days (Review L287), about 109 days on revenue days |
| S7 | Review L552 | Role 4 M2 ("Q2 FY27 concall transcript ... pending") is stale; mark it closed by the 19-Oct recording |
| S8 | Review L542 vs L1330 | Role 4 set the status words ANSWERED / PARTIALLY ANSWERED / EVADED / NOT ADDRESSED; the addendum uses PARTIAL / DECLINED / SILENT; add a one-line mapping |
| S9 | Review L1333 | CC-F7-04 (NEUTRAL-FACT) goes "to monitoring" but no M21-M35 row names it; name the row |
| S10 | Review L1465 | "50-60% of 800 kits" should read "800 kits/month" (PPT L236) |
| S11 | Review L1387 | "every dated lever slipped" is broader than the evidence (extrusion fired, L1227); use "every dated Q1-call promise", as the brief does (L1414) |
| S12 | Review L960 | "Seamless Rs 167 Cr (memory)": the same-quarter deck states ~Rs 167 Cr (PPT L251); cite it |
| S13 | STR L222-L258 | A1 DATE tagging is uneven for date tokens inside forward rows (Section 1 table); no content lost |

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
    - "CC L326: analyst-spoken seamless figure '1 6 3 7 or 4 routes' (NUMBER, ANALYST_FIGURE, ASR_GARBLE); only question row R299 (STR L317) exists"
arithmetic_mismatches:
  - {metric: "6B specificity ratio (count under A4's own rule: number, date or binary milestone)", a4_value: "0.43 (23 / 53)", recomputed: "0.60 (31 / 52) uniform; 0.54 (28 / 52) minimal pairwise fix", source_line: "STR L166 R152 vs L217 R203; L186-L187 R172-R173 vs L168 R154; L172 R158 vs L194 R180; L214 R200 vs L213 R199; L199 R185 vs L207 R193; L183 R169; L205 R191; L195 R181 analyst (CC L276-L277)"}
surviving_bear_counters:
  - {claim: "Trailer revenue ~Rs 115 Cr (+53% QoQ) sustainable in Q3-Q4 (CC L318-L320)", counter: "Axle volume rose only ~5-11% QoQ (Q2 10,000-10,500 vs Q1 9,500; CC L223, L225, L412-L413) against value +53%; value per axle +39-47% QoQ, mostly suspensions and commodity price (CC L415-L416); suspension volumes undisclosed (CC L408-L417). Machine transcript; Q1 figure is an analyst recall", source_line: "CC L223, L225, L238-L242, L412-L416", type: MISSING}
  - {claim: "BEAR CLAIM (Rule J): FY27-end gross debt ~Rs 165-170 Cr, 3.2x, 'confirmed'", counter: "BULL COUNTER: analyst's sum (115 + 50 undrawn) assented 'Yeah, correct'; management's sanction 110 / 110-120 less ~78-80 drawn (filed NCL 77.94 Cr; H1 LT draw 48.80 Cr) leaves ~30-42 Cr, so ~Rs 149-159 Cr (2.85-3.04x) with WC flat at filed 39.20 Cr", source_line: "CC L335-L336, L366-L367, L371-L377; RES L458, L463, L506", type: MISSING}
  - {claim: "BEAR CLAIM (Rule J): brief 'It said a return is difficult currently'", counter: "BULL COUNTER: management said it is difficult to say WHEN; it expects full retrospective compensation, conversion impact Q3-Q4", source_line: "CC L474-L489; STR L350 (R332)", type: FACTUAL}
  - {claim: "BEAR CLAIM (Rule J): specificity 0.43, archetype EVASIVE", counter: "Uniform count under A4's own rule gives 0.54-0.60, above the 0.5 line used in 6E", source_line: "Review L1149-L1152, L1173-L1174; STR L163-L219", type: FACTUAL}
  - {claim: "Updated brief replaces the Role 4 brief in full (Review L1401)", counter: "Drops A5-F3 bear counter B: ~81% of QoQ rise from trailer half and ~81% from top 5 (Role 4 L642) and the top-5 test in the Q3 forward-map row (Role 4 L696 vs L1463)", source_line: "Review L642, L696, L801, L1440, L1463", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): 6B specificity miscount under A4's stated rule; uniform recount 0.54-0.60 crosses the 0.5 line that sets EVASIVE (Review L1149-L1152, L1173-L1174); re-derive 6E and every copy of the archetype"
    - "F2 (A4): brief L1409 paraphrases 'difficult to say when' (CC L480-L482, R332) as 'a return is difficult'; reword and keep the retrospective-compensation half (CC L485-L489)"
  missing:
    - "M1 (A2): CC L326 analyst figure '1 6 3 7 or 4 routes' has no NUMBER row; add via MISSING_FROM_STRUCTURED; A3 disposition for that row only; A4 cite"
    - "M2 (A4): FY27-end debt shows only 165-170 Cr as confirmed; add the sanction reading ~Rs 149-159 Cr (CC L335-L336, L367, L375; RES L458, L463, L506) with Q23 as the separating observation; keep filed Rs 117.14 Cr in the brief"
    - "M3 (A4): graft QoQ test: axle volume +5-11% vs trailer value +53% (CC L223, L225, L238-L242, L412-L416) into Exchange 3 (L1083) and brief (L1411)"
    - "M4 (A4): restore A5-F3 concentration counter (81% / 81%) in the brief summary and the top-5 test in the Q3 forward-map row (Role 4 L642, L696 vs L1463)"
  contradiction:
    - "C1 (A4): forward-map bull fork (L1459) has allotment funding Rs 60 Cr of H2 lines; Step 2 (b) (L972) and flag (L1568) put allotment cash at Rs 39.75 Cr; make the bull fork require warrant conversion within H2"
  style:
    - "S1: Review L1083 reword '28-32% of the YoY value growth per unit' to 'value per axle rose ~28-32% YoY'"
    - "S2: Review L1408 'the margin gain' lacks a referent; restore the operating-margin line"
    - "S3: Review L1423 'timing' is INFERENCE, not MGMT-CALL"
    - "S4: Review L1442, L1098, L1265 '70% of seamless output sold outside': capacity not output; MGMT-DECK (PPT L254) plus INFERENCE; phase 1 may be a 30% first build"
    - "S5: 7A omits three tying claims (PAT +143%, PBT >100%, H1 FY26 rev 270); H1 EBITDA 53.32 repeats the H1 column with the 1.65 Mn footing gap"
    - "S6: 7A could set the WC-cycle target <90-95 days against the filed 124.4-day cash cycle"
    - "S7: Role 4 M2 (Review L552) still 'pending'; close it"
    - "S8: status vocabulary differs from Role 4 L542; add a mapping"
    - "S9: CC-F7-04 routed to monitoring with no M-row named"
    - "S10: Review L1465 '800 kits' should be '800 kits/month'"
    - "S11: Review L1387 'every dated lever slipped' should be 'every dated Q1-call promise'"
    - "S12: Review L960 seamless Rs 167 Cr is also MGMT-DECK (PPT L251)"
    - "S13: A1 DATE tagging uneven for date tokens inside forward rows; no content lost"
loop_back_to: "A2"
gap: "A2: add a NUMBER row for CC L326 analyst figure '1 6 3 7 or 4 routes' (ANALYST_FIGURE, ASR_GARBLE) via MISSING_FROM_STRUCTURED (M1). A3: disposition for that one row only. A4: F1 recount 6B specificity under one stated rule and re-derive the 6E archetype in every copy; F2 fix the brief's margin paraphrase (timing, not feasibility); M2 carry both FY27-end debt readings (~Rs 149-159 Cr on sanction 110-120 less ~78-80 drawn vs ~Rs 165-170 Cr analyst sum), drop 'confirmed', keep filed Rs 117.14 Cr in the brief; M3 graft the QoQ axle-volume (+5-11%) vs trailer-value (+53%) test; M4 restore the A5-F3 81%/81% concentration line and the top-5 Q3 test in the brief; C1 make the preferential bull fork require warrant conversion (Rs 39.75 Cr lands at allotment)."
style_notes:
  - "S1-S13 logged in runs/kross-q2fy27/work/audit_kross_q2fy27_role5.md section 6; no re-run"
analyst_note: "Role 5 addendum audit on a machine transcript; filed numbers win throughout. The brief gate passes. Arithmetic is clean: every derived figure I recomputed ties within rounding to RES L412-L508 and deck lines. Coverage ties on 65 turns, 9 slots, 22 analyst turns and 25 A3 IDs; one analyst figure (CC L326) has no row, so the chain restarts at A2 for one row. The substantive failures are same-bar failures. Three bear claims are stated above the extract. FY27-end debt 165-170 is the analyst's sum; management's own sanction less the filed draw gives about 149-159. The brief turns 'difficult to say when' into 'a return is difficult'. The specificity count mixes rules, and a uniform count crosses the 0.5 line that sets EVASIVE. On the bull side, the trailer step needs its QoQ test: axle volume +5-11% against value +53%, so most of the step is suspensions and price. The updated brief also dropped the 81% concentration counter that A5 required in loop 1. The addendum's direction (WEAKENED, Role 4 verdict unchanged) likely survives; numbers and labels need fixing before save."
```
