# A5 ADVERSARY AUDIT: Heritage Foods (HERITGFOOD) Q2 FY27, Role 5 concall addendum

Agent: A5 adversary | model: claude-opus-5-5 | date: 2026-10-19 | loop: role5-run1
Review under audit: runs/heritgfood-q2fy27/work/review_heritgfood_q2fy27.md (1,677 lines; Role 5 section R-L831-1327; change log R-L1649-1676)
Inputs read: A1 concall fulltext and structured file in full; presentation fulltext P-l255-299 and P-l614, P-l1168 (slide 9, MD); press release fulltext PR-L60-229; results fulltext L400-431; all four A2 ledgers (concall ledger in full); the A4 review in full. No source file and nothing under inputs/ was opened.
Scope: the Role 4 body was audited COMPLETE in loop 2. This audit covers the Role 5 section and every Role 4 line that the change log names.

Anchors: "CC-L###" = concall fulltext line. "R-L###" = review line. "L###" = results fulltext line. "P-l###" = presentation fulltext line. "PR-L###" = press release fulltext line.

---

## DELIVERABLE-COMPLETENESS AUDIT (gate)

| Brief part | Heading (review line) | Status |
|---|---|---|
| 1. Summary narrative | R-L1364 | PRESENT. 17 lines (R-L1366-1382), inside the 10-20 line band. Carries the call's Q3 cost, floor, species and ice cream items. |
| 2. Sector intelligence | R-L1384 | PRESENT. Six bullets; call content added with [MGMT, ASR] tags. |
| 3. Business-model intelligence | R-L1394 | PRESENT. Nine bullets. Content defect in the run-rate bullet R-L1400 (finding F1). |
| 4. Competition intelligence | R-L1406 | PRESENT. Seven bullets, includes the conglomerate entrant (CQ14). |
| 5. Forward map | R-L1416 | PRESENT. 11 dated rows, each with a bull fork and a bear fork. The 1 Nov 2026 row lacks a procurement-side bear fork (finding M4). |

Gate: PASS. All five parts exist and carry real content.

---

## COVERAGE AUDIT

Fresh pass: I read the concall fulltext CC-L130-853 line by line and listed every unit of the A1 row types (NUMBER including unquantified comparatives of the R070, R071 and R161 class; ENTITY; FORWARD; DATE; QUALIFIER), then diffed against the structured rows R001-R336 and the A2 ledger.

| Category | A2 count | Fresh count | Orphan rows (ledger row absent from A4) | Status |
|---|---|---|---|---|
| Turns | 81 | 81 | none | PASS |
| Analyst questions | 24 | 24 (Jay Dangir's second part folded into Q03, CWC's four parts into Q24, as A1 does) | none | PASS |
| NUMBER | 162 | 169 | none | FAIL: 7 units missing (U2-U8) |
| ENTITY | 52 | 53 | none | FAIL: 1 unit missing (U10) |
| FORWARD | 60 | 60 | none | PASS |
| DATE | 20 | 22 | none | FAIL: 2 units missing (U1, U9) |
| QUALIFIER | 42 | 42 | none | PASS |
| Total rows | 336 | 346 | none | FAIL (A2) |

Orphan check: A4 marks all 336 concall rows "reviewed" (R-L21, R-L842). That blanket statement is the explicit "reviewed, no finding" mark for uncited rows, as accepted in loops 1 and 2. Orphan rows: none.

Units the fresh pass found that the structured file and the A2 ledger lack (ledger Section 10 says "none found"):

| U | Fulltext line | Verbatim unit | Type (class analog) | Used in A4 (proof it is material) |
|---|---|---|---|---|
| U1 | CC-L479-481 | "in the beginning of the year, we had capitalized some large projects" | DATE (R282, R291 class) | K10, Q43, 7A "CONFIRMED", 5A row 18, Step 2 capex row |
| U2 | CC-L481-482 | "the EBITDA improvement sequential is far better than PVT or VAT. The reason is depreciation is much higher" | NUMBER, unquantified comparative (R071 class) | FC-1, Q49, F8, 8E |
| U3 | CC-L667-669 | "what is really affected is the buffalo milk supply ... cow milk supply is reasonably growing" | NUMBER, unquantified comparative | CQ20 substance |
| U4 | CC-L672 | "cow milk on a solid basis is cheaper than buffalo milk" | NUMBER, unquantified comparative | Working reading B (slide 9 note), F3, Q29, M14, brief part 2 |
| U5 | CC-L677 | "cow [milk] is becoming dearer now" | NUMBER, unquantified comparative | Exchange 2 |
| U6 | CC-L686 | "the significant inflationary trend we have seen also is in the hardcore cow milk" | NUMBER, unquantified comparative | Working reading B, F3, 5A row 4, brief parts 1-2 |
| U7 | CC-L699-701 | "we have a strong quarter two ... we had a difficult quarter one due to the very, very high cost of the ingredients" | NUMBER, unquantified comparative | FC-5, Q9 ANSWERED |
| U8 | CC-L798-799 | "our bottom line is suffering whenever there is a raw milk price increase" | NUMBER, unquantified comparative | 6A, 6D, 8D |
| U9 | CC-L725-726 | "over let's say next 2-3-4 quarters" (analyst horizon) | DATE (R131 analyst-lookback class) | none (minor) |
| U10 | CC-L779-780 | "Middle East and West Asia as well as Southeast Asia and Far East Asia" | ENTITY (R185, R206 geography class) | none (minor) |

U4 and U6 carry the call's most consequential change, the slide 9 working reading B. A4 cites all of U1-U8 straight from the fulltext, so the review itself drops nothing. The spine guarantee failed one level up: the structured file dropped them and the ledger did not catch it. Finding M1 (MISSING, loop A2).

Ledger hygiene found on the way (no effect on A4's numbers):
- R236 ("Yes, that's what we are hoping", CC-L408) is flagged FORWARD_ANALYST_VOICE at T025. The A1 turn map assigns those words to T024, management. The ledger's shared-line rule (a shared line resolves to the later turn) mis-assigns it. This feeds finding C1.
- Conflict C3 ("paneer 1200 vs 200-230") rests on the misreading in finding F1.
- Conflict C5 labels the 1.8 m L/day statement "analyst ... T055"; R125 sits in T054, management. Conflict C6 cites T045 for R089; CC-L477 sits in T032. A4 calls these "A3's turn-cite slips" (R-L842); they are ledger slips. STYLE S8.

---

## ARITHMETIC AUDIT

Every derived number in the Role 5 section and the changed Role 4 lines, recomputed from the extracts.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| 11% on Q3 FY26 base | Rs 50.56/L | 45.55 x 1.11 = 50.5605 | CC-L381, CC-L621 | PASS |
| "Not 50" as YoY | about +9.8% | 50.0 / 45.55 = +9.77% | CC-L618 | PASS |
| Q2 FY26 landed cost; Q2-to-Q3 FY26 step | 42.99; +Rs 2.56 (+6.0%) | 47.73 - 4.74 = 42.99; 45.55 - 42.99 = 2.56, +5.96% | PR-L76-77, CC-L621 | PASS |
| Same rupee step this year | Rs 50.29 (+10.4%) | 47.73 + 2.56 = 50.29; / 45.55 = +10.41% | derived | PASS |
| Rs 1/L of landed cost a quarter | Rs 15.90 Cr; 1.20% of revenue | 17.28 lakh L x 92 x Rs 1 = Rs 15.898 Cr; / 1,319.58 = 1.205% | PR-L121, L407 | PASS |
| Cost of Rs 50.0 and Rs 50.56 | Rs 36.09 Cr; Rs 44.99 Cr | 2.27 x 15.898 = 36.09; 2.83 x 15.898 = 44.99 | derived | PASS |
| Realisation step the floor needs | 2.7-3.4% | 36.09 / 1,319.58 = 2.73%; 44.99 / 1,319.58 = 3.41% | L407 | PASS |
| Rs 0.5/L a month (FC-4) | Rs 2.65 Cr; 0.60% of Rs 439.86 Cr | 17.28 lakh x 0.5 x 30.67 = Rs 2.650 Cr; 1,319.58 / 3 = 439.86; 0.602% | PR-L121, L407 | PASS |
| Procured milk not sold as liquid (Q48, FC-3) | 4.10 to 4.93 LLPD, +20% | 17.28/1.07 - 12.35/1.025 = 16.150 - 12.049 = 4.10; 17.28 - 12.35 = 4.93; +20.3% | PR-L121-127 | PASS |
| Cost ratios, consolidated (Q37, FC-2) | employee -0.91 pp YoY, +0.23 QoQ; other -0.47 YoY, -0.58 QoQ | 889.55/11,125.17 = 8.00% to 935.20/13,195.80 = 7.09% (-0.91); 917.95/13,380.94 = 6.86% (+0.23 QoQ); other 9.61% to 9.14% (-0.47), 9.72% Q1 (-0.58 QoQ) | L407, L414, L418 | PASS |
| Cost ratios, standalone | -0.86, -0.80, sum -1.66 pp | 7.77% to 6.91%; 9.32% to 8.52%; sum -1.66 | L75, L82, L86 (Step 1B values) | PASS |
| QoQ operating EBITDA | +19.58% (Role 5) vs +19.57% (Step 3A) | 739.67 / 618.63 = +19.57% | L407-420 | STYLE S1 (rounded-Cr input) |
| QoQ PBT | +26.97% | 425.99 / 335.49 = +26.97% | L424 | PASS |
| QoQ PAT | +23.59% | 308.57 / 249.71 = +23.57% | L428 | STYLE S1 (rounded-Cr input) |
| QoQ D&A; finance cost | +Rs 0.98 Cr; -Rs 0.97 Cr | 274.70 - 264.89 = 9.81 m; 72.64 - 82.34 = -9.70 m | L415-416 | PASS |
| Sequential margins (not computed by A4) | n/a | EBITDA 4.62% to 5.61% (+98.2 bps); PBT 2.51% to 3.23% (+72.1 bps); PAT 1.87% to 2.34% (+47.2 bps); D&A +10.2 bps, other income -22.4 bps, finance cost -6.5 bps | L407-428 | Feeds finding M2 |
| Fat products vs consumer ghee and butter | within Rs 2.00 Cr | 91.80 - (540.8 - 451.0) = 2.00 | P-l187-214, PR-L131-136 | PASS |
| Q1 FY27 landed cost; Q1 volume | Rs 46.42; 18.10 LLPD | (17.69 x 183 - 17.28 x 92) / 91 = 18.105; (47.06 x 3,237.27 - 47.73 x 1,589.76) / 1,647.51 = 46.41 | PR-L121-123 | PASS |
| Get-A-Way supply at Rs 200/L | Rs 6.0 Cr a quarter; Rs 23.9 Cr a year | 3,272 x 92 x 200 = Rs 6.02 Cr; x 365 = Rs 23.89 Cr | CC-L231, CC-L427 | PASS |
| Ice cream target CAGR; current growth | 14-24%; 55-82% | (500/200)^(1/7) = 14.0%; (500/170)^(1/5) = 24.1%; 170/110 = +55%, 200/110 = +82% | CC-L770-775 | PASS |
| NutriVate PBT margin | 4.3% Q2; 3.5% H1 | 37/853 = 4.34%; 56/1,581 = 3.54% | PR-L142-144 | PASS |
| H2 FY26 D&A average | Rs 21.09 Cr | (80.98 - 38.80) / 2 = 21.09 | L416 | PASS |
| Opening and Q&A share of call | 11:05, 16.7%; 53:03, 79.9% | 665 s / 3,985 s = 16.69%; 3,183 / 3,985 = 79.87% | CC-L150, CC-L265-266, CC-L845, CC-L117 | PASS |
| Opening claims quantified | 21 of 29, 72.4% | rows 2-6, 8, 10, 12-18, 20-25, 27 = 21; 72.41% | R-L894-924 | PASS |
| Response grades; C or worse | A5 B8 C9 D1 E1; 11 of 24 (46%) | recount of CQ01-CQ24 grades ties; 45.8% | R-L1000-1025 | PASS |
| Hedge phrases | 19 | 9 single + "hoping" 6 (CC-L373, L382, L383, L408, L736 x2) + "expecting/expect" 3 (CC-L372, L402, L616) + "We believe" 1 | fulltext | PASS |
| Specificity ratio (6B) | 16 / 56 = 0.29 | R236 is management voice (A1 turn T024), so 16 / 57 = 0.28; stricter counts 14/55 = 0.25, 12/53 = 0.23 | R-L1136-1138 | CONTRADICTION C1 (conclusion "below 0.3" unchanged) |
| Run-rates vs "90%" (Q38) | curd + paneer + ghee = 40-42% of annualised broader VAP | Arithmetic on A4's inputs ties (870-900 / 2,163.2 = 40.2-41.6%). The input reading is wrong: curd Rs 320 Cr is quarterly (F1). Corrected: (1,200-1,280 + 200-230 + 350) / 2,163.2 = 81-86% | CC-L715-719, CC-L205-206, PR-L76, PR-L136 | FACTUAL F1 |
| Monitorable status tally | answered 2, partly 5, silent 7 | M4, M5; M1, M2, M6, M13, M14; rest | R-L794-807 | PASS (STYLE S3 on M4 wording) |
| Question call-status tally | 1 / 7 / 26 | Q9; Q1, Q4, Q10, Q15, Q17, Q29, Q31; 26 silent | R-L724-757 | PASS |
| M20 opex share of revenue | 16.23% | (93.52 + 120.65) / 1,319.58 = 16.23% | L414, L418 | PASS |

No mismatch above rounding on A4's own arithmetic. The two failures sit in an input reading (F1) and a denominator (C1).

---

## ADVERSARIAL READ

The three most positive claims in the Role 5 section, each with the strongest bear counter from the same extracts.

P1. EBITDA floor: "the bull side gains an EBITDA floor promise (CC-L603-604)" (R-L697; K6, M16).
- Bear counter: the floor rests on prices taken by September, yet the Q3 price decision is open ("we will take a call", CC-L638-639). Thirteen minutes later management restated it as "relatively better off in terms of EBITDA" if inflation continues (CC-L736-737), a comparative, not a floor. Season works against it: in FY26 the operating margin fell from 6.94% in Q2 to a 5.06% H2 average (L407-418, derived). The floor needs a 2.7-3.4% Q3 realisation step.
- Survives? Already in A4: Step 2 confidence MEDIUM-LOW with CC-L736-739 quoted (R-L940), F13 (R-L1347), 8C seasonal note (R-L709), Q36. No graft needed.

P2. One-way price ratchet: "The asymmetry is the bull case: each Rs 1/L fall in landed cost adds about 1.2% of revenue to margin if consumer prices hold" (R-L1060).
- Bear counter: management's own conditional says a cost fall takes margins "back to our steady-state levels" (CC-L738-739), so the ratchet restores lost margin, it does not add new margin. Liquid milk passed about 72% of the cost rise and "cannot go up by 11%" (CC-L784-786); "our bottom line is suffering whenever there is a raw milk price increase" (CC-L798-799). The down-cycle price depends on cooperatives, which management refused to discuss (CC-L492-497).
- Survives? Already in A4: "Bull claim, untested" with the cooperative caveat (R-L1060), Step 2 steady-state text (R-L940), strategic-premium row (R-L1261), Q51. No graft needed.

P3. Karnataka catalyst: KMF's +Rs 8/L consumer price from 1 November is "A dated third-party catalyst, sales side only (CC-L396-403)" (Q45, R-L768); M17; forward-map row "1 November 2026" with a Bangalore-only bear fork (R-L1424).
- Bear counter: the same move passes "6 rupees out of that to the farmer" (CC-L397-398). Management names Nandini's area among the "cow milk belts" with Aavin, Tamil Nadu and Southern Andhra (CC-L681-683), and says "the significant inflationary trend we have seen also is in the hardcore cow milk" (CC-L686). On management's own causal account, a cooperative farm-price step in a cow belt is a cost input, and this one follows Aavin's Rs 6/L (CC-L394-395). Heritage's Karnataka procurement is "not significant" (CC-L400-401), so the channel to Heritage is farm-price competition in adjacent cow catchments [INFERENCE].
- Survives: YES. The review calls the event sales side only and gives the forward map no procurement fork. Graft: add a procurement-side bear fork to M17, Q45 and the 1 November forward-map row ("cow-belt farm prices step up again from November; Q3 and Q4 landed cost rises"), tagged [MGMT, ASR; INFERENCE on transmission]. Finding M4.

Mandatory acquisition-economics probe. The call describes stake changes: "Getaway, in which we now hold 71 percent stake" and "Heritage Novandee Foods now a wholly owned subsidiary" (CC-L229-233).
- Multiple: consideration NOT FOUND in any extract. Target earnings are negative: dairy subsidiaries' segment result H1 FY27 -Rs 3.15 Cr (L468 minus L125, Step 5F); NCI-implied Get-A-Way H1 loss about Rs 2.60 Cr [INFERENCE, single-NCI-entity assumption]. Price / target PAT = NOT FOUND / negative: no positive multiple exists. ROCE, debt, cash and customer tenure: NOT FOUND.
- New from the call: Heritage manufactures 3,272 L/day of ice cream for Get-A-Way (CC-L230-232). At Rs 200/L that is about Rs 23.9 Cr a year, about 13-14% of own ice cream revenue of Rs 170-180 Cr (CC-L771-772) [derived; transfer price NOT FOUND]. Get-A-Way's "robust revenue growth" is partly Heritage-made product resold through a loss-making 71%-owned entity.
- Bear reading: more of a loss-making asset was bought at an undisclosed price. It survives but is already in A4 (Step 5F; Q32, Q39, Q42; F5). There is no "cheap, accretive" claim to stress. No graft beyond the existing rows.

Symmetry check on A4's bear claims (CLAUDE.md Rule J; completeness, not one of the three mandated reads):
- Q3 cost bear lean (Step 2 R-L956; Exchange 1 R-L1044; 8A R-L1243). A4 says "11% might continue" is the "last year repeats" path, and that the October data point "does not support" the "not 50" statement. The company's own slide 9 monthly series gives a second reading (finding M3).
- FC-1 "CONTRADICTED sequentially" (R-L1183, R-L1219). On margins the call's statement holds (finding M2).

---

## FINDINGS (tagged)

F1. FACTUAL. Loop: A4 (A2 to re-label ledger conflict C3).
Gap: A4 reads the CC-L715-719 run-rates as curd about Rs 320 Cr a year and treats "1200" as an ASR artefact for paneer (R-L836, R-L1085, R-L1231-1232, Q38 R-L761, R-L1286, brief R-L1400). The extract supports a second reading, and it fits the numbers better. The text runs: "curd is roughly around 320 crores kind of revenue, paneer is you know and this is a you know you can say an annualized about 1200 kind of thing. On here on an annualized basis will be about 200 crores plus 200 230 crores" (CC-L715-718). "Annualized about 1200" is curd's annual figure (320 x 4 = 1,280); the speaker then gives paneer explicitly "on an annualized basis". Arithmetic: daily curd sales above 500 t (CC-L205-206; PR-L92) give about 46,000 t a quarter. Rs 320 Cr over 46,000 t is about Rs 70/kg. Rs 320 Cr a year over 182,500 t is about Rs 17.5/kg, below the Rs 47.73/L landed milk cost (PR-L76) [INFERENCE: about 1 L of milk per kg of curd]. Ghee at Rs 350 Cr annualised (Rs 87.5 Cr a quarter) ties to consumer ghee and butter of Rs 89.80 Cr (PR-L131, PR-L136), so "annualized" belongs to ghee and paneer, not curd.
Consequence: Q38's "sum to about 40-42% of annualised broader VAP, not 90%" is wrong. Under the curd-quarterly reading, curd plus paneer plus ghee is Rs 1,750-1,860 Cr a year, 81-86% of annualised Q2 broader VAP (Rs 2,163 Cr), close to the "about 90%" (CC-L520-521). IC-4 "Not a revenue share" and IC-5 fall away. Curd alone would be about 71% of the Rs 451.0 Cr Q2 VAP line.
Fix: state both readings, name the curd-tonnage arithmetic as the evidence that favours curd-quarterly, and re-write Q38 (why, forks), 5A row 14, IC-4, IC-5, the Step 0 source caveat list, 8F Q38 and the brief part 3 run-rate bullet. Separating observation: quarterly curd revenue (Q38 already asks for it).

M1. MISSING. Loop: A2.
Gap: ten fresh-pass units (U1-U10, Coverage Audit) are absent from the structured file and the ledger, whose Section 10 says "none found". U4 and U6 (CC-L672, CC-L686) carry working reading B; U1 and U2 carry K10, Q43 and FC-1.
Fix: A2 lists U1-U10 under MISSING_FROM_STRUCTURED (or A1 adds rows R337 onward). A2 also re-flags R236 FORWARD_MGMT (T024) and re-labels conflict C3 as two readings (F1). A4 already cites U1-U8 by CC-L, so A4 needs only the row-count text (R-L21, R-L842).

M2. MISSING. Loop: A4.
Gap: FC-1 (R-L1183, R-L1219, Q49 R-L772, F8 R-L1342, 8E R-L1275, combined verdict R-L1324, YAML FC-1) tests the call's "EBITDA improvement sequential is far better than PBT or PAT" (CC-L481-482) on growth rates only. The call states EBITDA in margin terms ("98 basis points", CC-L166-167, CC-L597, CC-L601). On margins the claim holds: operating EBITDA margin +98.2 bps, PBT margin +72.1 bps, PAT margin +47.2 bps (L407-428, recomputed). Depreciation explains 10.2 bps of the 26-bp EBITDA-to-PBT gap; the fall in other income explains 22.4 bps; lower finance cost offsets 6.5 bps.
Fix: FC-1 carries two readings. On growth rates it fails (EBITDA +19.57%, PBT +26.97%, PAT +23.57%). On margins it holds, with the cause overstated (other income, not depreciation, is the larger part). Re-word "CONTRADICTED sequentially" to "two readings; holds on margins, cause overstated", and align Q49, F8, 8E, the combined verdict and the YAML.

M3. MISSING. Loop: A4.
Gap: A4 leans bear on Q3 cost from last year's step (Rs 50.29) and says the October point "does not support" the "not 50" statement (R-L956, R-L1044, R-L1243, F12, analyst note). The company's own slide 9 series (P-l276-288) gives a second reading. Q2 average standard cost and its Jul-Sep monthly step, at 80/20 volume weights (CC-L502, P-l265), with landed cost = standard cost + a fixed add-on [INFERENCE; reading B's YoY rupee change +4.92 tracks landed +4.74]:

| Path | Reading B (cow = Rs 39-41 series) | Reading A (cow = Rs 52-55 series) |
|---|---|---|
| Q2 average standard cost | 42.85 | 51.08 |
| Jul-Sep monthly step | +0.65/month | +0.77/month |
| Q3 flat at September level | landed Rs 48.40 (+6.3% YoY) | Rs 48.51 (+6.5%) |
| Q3 continues the Jul-Sep step | landed Rs 49.69 (+9.1% YoY) | Rs 50.05 (+9.9%) |
| Monthly step needed for Rs 50.56 (11%) | +1.08/month (1.67x) | +1.02/month (1.34x) |

A "slight increase" in October over September (CC-L375) is what both paths expect. The series puts Q3 at Rs 48.4-50.1, nearer "not 47 to 50" than "11% might continue"; 11% needs the monthly climb to speed up by about 1.3-1.7x. The two management statements still conflict (IC-1 and F12 stand).
Fix: add this reading beside the last-year-step reading in Step 2 diagnostics, Exchange 1 and 8A; replace "Bear lean on Q3 cost" with the two readings. Separating observation: October and November landed cost per litre (Q35 already asks).

M4. MISSING (surviving bear counter P3). Loop: A4.
Gap: Q45 and M17 call KMF's 1 November move "sales side only" and the forward map has no procurement fork. CC-L397-398, CC-L681-686 show a Rs 6/L farm-price step in a cow-milk belt, the species management says carries the inflation.
Fix: graft a procurement-side bear fork into Q45, M17 and the 1 November forward-map row, tagged [MGMT, ASR; INFERENCE on transmission].

C1. CONTRADICTION. Loop: A4 (root cause A2 flag on R236).
Gap: 6B removes R236 from management forward rows as analyst voice (R-L1136), while 6C counts the same words, "Yes, that's what we are hoping" (CC-L408), as a management hedge (R-L1154). The A1 turn map gives the words to T024, management.
Fix: management forward rows 57; ratio 16/57 = 0.28 (stricter counts 0.25 and 0.23). Update 6B, 6E, Step 9 archetype line, F17 and YAML specificity_ratio. The conclusion (below 0.3, lower 6E row) does not change.

C2. CONTRADICTION. Loop: A4.
Gap: the review body carries the merged Role 5 section (R-L831-1327) and the change log says "Applied 2026-10-19" (R-L1651). The review's own YAML still says merge_into_review "pending: no Edit tool ..." (R-L1444), review_path "(Role 5 merge pending; addendum in work/review_role5_part1..part6)" (R-L1606), and the analyst note ends "MERGE PENDING" (R-L1605).
Fix: set merge_into_review to "done 2026-10-19", drop the pending text from review_path and the analyst note, and align the work/blocks/a4-role5.yaml copy.

---

## VERDICT

INCOMPLETE.
- Failing agents: A2 (M1, plus the R236 flag and conflict C3 label), then A4 (F1, M2, M3, M4, C1, C2).
- Finding types: FACTUAL 1, MISSING 4, CONTRADICTION 2.
- The protocol verdict PROCEED WITH FLAGS and cash conversion INDETERMINATE are not at stake. No fix touches a filed number.
- Sequencing: A2 adds a ledger addendum; A3 needs no new forensic work, because A4 already cites U1-U8 by CC-L; A4 applies F1, M2-M4, C1, C2; A5 re-checks.

---

## STYLE NOTES (logged, no loop)

- S1. QoQ operating EBITDA reads +19.58% in Role 5 (R-L1183, R-L1219, Q49) and +19.57% in Step 3A (R-L410); unrounded 739.67 / 618.63 = +19.57%. QoQ PAT +23.59% vs unrounded 308.57 / 249.71 = +23.57%. Rounded-Cr inputs; use the unrounded values.
- S2. K4 tests "at or above Rs 50.5/L" (R-L977); 8C and M15 use Rs 50.56/L. Use one threshold.
- S3. M4 reads "call: answered" (R-L797), while CQ23 on the margin path is graded C (R-L1024) and 6A marks the margin outlook DOWNGRADED (R-L1127). "Partly" fits better; if kept, say that "answered" means "addressed".
- S4. 6B counts R251 ("whatever is EBITDA now", no number or named quarter) as quantified, and leaves out R254, which names Q2. The net count is unchanged.
- S5. Speaker mapping [INFERENCE: ASR]: T078 says third-party lending again "like I said earlier" (CC-L822), which repeats T028's "Ramani" answer (CC-L441-443). "Edie" (CC-L803) reads as "ED", and NutriVate's CEO thanks "Ramnigaru" (CC-L696). "Ramani" is likely Brahmani Nara, the ED, which gives her two turns, not one (R-L863, R-L870). A1 does not infer speakers from content, so A4 may add this only as a labelled inference.
- S6. "Her answer covered procurement, not vision" (R-L863). The question routed to the ED was Q24 part 1, procurement CAGR adequacy (CC-L740-743). She answered it, but with no number.
- S7. 7A marks the ice cream facility PARTIALLY CONFIRMED by H1 PPE +Rs 28.26 Cr (R-L1199). The filing does not identify the facility, and "when we commissioned the ice cream factory, we said our vision is..." (CC-L769-770) suggests the commissioning may predate FY27. UNVERIFIABLE is the conservative label.
- S8. Ledger conflicts C5 (analyst, T055) and C6 (T045) carry turn slips; R125 is management in T054, and CC-L477 sits in T032. A4 attributes them to A3 (R-L842).

---

```yaml
stage: A5-adversary
company: "HERITGFOOD"
quarter: "q2fy27"
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
    - "U1 CC-L479-481 DATE 'in the beginning of the year, we had capitalized some large projects'"
    - "U2 CC-L481-482 NUMBER-unquantified 'EBITDA improvement sequential is far better than PVT or VAT ... depreciation is much higher'"
    - "U3 CC-L667-669 NUMBER-unquantified buffalo supply constrained, cow supply growing"
    - "U4 CC-L672 NUMBER-unquantified 'cow milk on a solid basis is cheaper than buffalo milk'"
    - "U5 CC-L677 NUMBER-unquantified 'cow [milk] is becoming dearer now'"
    - "U6 CC-L686 NUMBER-unquantified 'significant inflationary trend ... in the hardcore cow milk'"
    - "U7 CC-L699-701 NUMBER-unquantified NutriVate 'strong quarter two ... difficult quarter one ... high cost of the ingredients'"
    - "U8 CC-L798-799 NUMBER-unquantified 'our bottom line is suffering whenever there is a raw milk price increase'"
    - "U9 CC-L725-726 DATE analyst horizon 'next 2-3-4 quarters'"
    - "U10 CC-L779-780 ENTITY export regions Middle East, West Asia, Southeast Asia, Far East Asia"
arithmetic_mismatches:
  - {metric: "Q38 curd+paneer+ghee share of annualised broader VAP", a4_value: "40-42% (curd Rs 320 Cr a year)", recomputed: "81-86% (curd Rs 320 Cr a quarter, 1,200-1,280 a year; 500 t/day curd gives Rs 70/kg vs Rs 17.5/kg)", source_line: "CC-L715-719, CC-L205-206, PR-L76, PR-L136"}
  - {metric: "6B specificity ratio", a4_value: "16/56 = 0.29", recomputed: "16/57 = 0.28 (R236 is management, T024)", source_line: "CC-L408; R-L1136 vs R-L1154"}
surviving_bear_counters:
  - {claim: "KMF +Rs 8/L from 1 Nov 2026 is a sales-side catalyst only (Q45, M17, forward map)", counter: "KMF passes Rs 6/L to farmers in a cow-milk belt; management names cooperative farm-price moves in cow belts as the inflation driver; add a procurement-side bear fork", source_line: "CC-L397-398, CC-L681-686, CC-L394-395", type: MISSING}
findings_by_type:
  factual:
    - {id: F1, loop: A4, gap: "CC-L715-719 run-rates misread: curd Rs 320 Cr is quarterly on the extract's tonnage arithmetic; Q38 'not 90%' wrong (81-86%); IC-4, IC-5, 5A row 14, Step 0 caveat, 8F Q38, brief part 3 to carry both readings"}
  missing:
    - {id: M1, loop: A2, gap: "U1-U10 absent from structured file and ledger (Section 10 says none); U4/U6 carry working reading B; also re-flag R236 FORWARD_MGMT and re-label conflict C3"}
    - {id: M2, loop: A4, gap: "FC-1 tested on growth rates only; on margins the call claim holds (EBITDA +98.2, PBT +72.1, PAT +47.2 bps; D&A 10.2 of 26 bps, other income 22.4); restate as two readings in 7A, 7D, Q49, F8, 8E, combined verdict, YAML"}
    - {id: M3, loop: A4, gap: "Q3 cost bear lean one-sided; slide 9 Jul-Sep slope puts Q3 landed at Rs 48.4-50.1; Rs 50.56 needs a 1.3-1.7x faster monthly climb; add to Step 2, Exchange 1, 8A"}
    - {id: M4, loop: A4, gap: "surviving bear counter P3: procurement-side fork for KMF Rs 6/L farm pass-through in Q45, M17, forward map"}
  contradiction:
    - {id: C1, loop: A4, gap: "6B excludes R236 as analyst voice while 6C counts the same CC-L408 words as a management hedge; ratio 0.28 not 0.29 (conclusion unchanged)"}
    - {id: C2, loop: A4, gap: "review YAML says merge pending (R-L1444, R-L1605-1606) while the body carries the merged Role 5 section and the change log says applied"}
  style:
    - "S1 QoQ op EBITDA +19.58% vs unrounded +19.57%; PAT +23.59% vs +23.57%"
    - "S2 K4 threshold Rs 50.5/L vs Rs 50.56/L in 8C and M15"
    - "S3 M4 'answered' vs CQ23 grade C and 6A DOWNGRADED"
    - "S4 6B counts R251 (no number) and omits R254 (names Q2); net unchanged"
    - "S5 'Ramani' likely Brahmani Nara (CC-L822 'like I said earlier', 'Edie' = ED, 'Ramnigaru'); label as INFERENCE if added"
    - "S6 ED answered Q24 part 1 (procurement adequacy), not a vision question"
    - "S7 7A ice cream facility PARTIALLY CONFIRMED; UNVERIFIABLE is conservative (CC-L769-770)"
    - "S8 ledger C5/C6 turn slips are A2's, not A3's"
loop_back_to: "A2"
gap: "A2: list U1-U10 under MISSING_FROM_STRUCTURED, re-flag R236 FORWARD_MGMT (T024), re-label C3 as two readings. Then A4: F1 (curd run-rate reading; Q38 'not 90%' wrong), M2 (FC-1 two readings), M3 (slide 9 Q3 cost reading), M4 (KMF procurement fork), C1 (specificity 16/57 = 0.28), C2 (stale merge-pending YAML). A3 needs no new forensic work; A4 already cites U1-U8 by CC-L."
style_notes:
  - "S1 use unrounded QoQ +19.57% and +23.57%"
  - "S2 one Q3 cost threshold, Rs 50.56/L"
  - "S3 M4 status 'partly' or define 'answered'"
  - "S4 R251/R254 quantified-rule consistency"
  - "S5 optional labelled inference: Ramani = Brahmani Nara"
  - "S6 reword the ED vision remark"
  - "S7 7A facility label UNVERIFIABLE"
  - "S8 ledger C5/C6 turn slips"
analyst_note: "Role 5 audit only; the Role 4 body was COMPLETE in loop 2. A4's own arithmetic ties to rounding. The failures are readings, not sums. (1) CC-L715-719: curd Rs 320 Cr is far more likely quarterly. 500 t/day of curd at Rs 320 Cr a year is Rs 17.5/kg, below the Rs 47.73/L milk cost. That reverses Q38's 'not 90%' (81-86%). (2) FC-1 fails on growth rates but holds on margin bps (98 vs 72 vs 47); the cause is overstated, not contradicted. (3) The Q3 cost bear lean ignores the company's own slide 9 slope, which puts Q3 landed at Rs 48.4-50.1. Rs 50.56 needs the monthly climb to speed up 1.3-1.7x. IC-1 still stands. (4) KMF passes Rs 6/L to farmers in a cow belt, so the 1 Nov move is not sales side only. The A2 gap is ten units, including the cow-vs-buffalo lines that carry working reading B. A4 already cites them from the fulltext, so the fix is a ledger addendum. PROCEED WITH FLAGS is not at stake."
```
