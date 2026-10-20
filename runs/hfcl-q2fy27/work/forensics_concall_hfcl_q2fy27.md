# A3 FORENSIC NOTES: HFCL Limited (HFCL) Q2 FY27, doctype CONCALL (Role 5 addendum)

CAVEAT (binds every finding below): MACHINE TRANSCRIPT (faster-whisper, local CPU, medium.en and small.en mixed; fulltext lines 19-21). Not an official transcript. Speakers are INFERRED, not labelled. Numbers and names may be mis-heard. Filed results win on any number conflict. Where a spoken number ties to a filing, the filing figure comes from the Role 4 review (runs/hfcl-q2fy27/work/review_hfcl_q2fy27.md) and is marked [ROLE 4]. Figures from the Notion page are marked [MEMORY] and are memory to weigh, not anchored evidence.

Inputs read: A1 structured (runs/hfcl-q2fy27/extracted/hfcl-concall-q2fy27-structured.md, R001-R470 + T001-T145); A1 fulltext (runs/hfcl-q2fy27/extracted/hfcl-concall-q2fy27-fulltext.md, lines 1-1020, read in full); A2 ledger (runs/hfcl-q2fy27/work/ledger_concall_hfcl_q2fy27.md); Notion brief sections 4, 7, 8 (runs/hfcl-q2fy27/work/notion-brief.md); Role 4 review Step 8.5 (42 questions). Prior-quarter fulltext: none (Q1 FY27 transcript never supplied). Source file and inputs/ NOT opened.

Finding IDs carry the prefix CC-FN (concall) so they do not collide with RES-FN, PPT-FN and MA-FN in the merged review.

---

## 1. LEDGER RECONCILIATION

| Item | Count |
|---|---|
| Structured IDs in ledger (R001-R470 + T001-T145) | 615 |
| IDs read at cited fulltext line | 615 |
| Orphan / MISSING_FROM_STRUCTURED | 0 / 0 |
| ledger_reconciled_pct | 100 |

Method: the fulltext was read end to end (lines 1-1020), so every R-row line and every T-range was read in place. Spot ties of the value to its line: R002 (60), R010 (64), R029 (85), R036 (126), R047 (253), R048 (273), R063 (361), R064 (362), R072 (405), R074 (440), R075 (441), R133 (755), R138 (765), R140 (768), R143 (770), R155 (819), R245 (124), R289 (404), R307 (541), R309 (552), R312 (582), R401 (48). All values are verbatim substrings of the cited line.

A2 flag clusters, as read at the lines:

| Cluster (A2) | Lines | A3 reading |
|---|---|---|
| Order book 28,900 / 29,000 / 28,000 / 30,000 | 85, 695, 743, 751, 763, 782 | RESOLVED. MD anchor Rs28,900 Cr (85, 751) ties to the filed Rs28,911 Cr [ROLE 4]. 29,000 / 28,000 / 30,000 are rounded or analyst figures. |
| Quarter orders 3,000 vs 5,500 | 752, 755, 764-765 | RESOLVED arithmetically. 3,000 = book increase (26,000 to ~29,000); 5,500 = inflow (2,500 delivered + 3,000 increase). See CC-FN-20 for the base-period issue. |
| Aerospace book 1,600 vs 1,800 | 126, 273, 405 | UNRESOLVED. The MD gives both in one call and "16 or 1800 crores" (405). See CC-FN-05. |
| Capacity 63m vs 43m vs 53m | 361-362, 716-717, 768 | MOSTLY RESOLVED. 43 is the FIBRE target (28 to 34 to 43, line 361); 63 is the CABLE target (362, 717, stated twice). "34 to 53" (768) is the single outlier (ASR or slip). See CC-FN-13. |
| Defence horizon 3 years vs 2 years | 252-253, 770 | UNRESOLVED. See CC-FN-04. |
| Q2 connectivity 200-300 / 300+ / 300 | 796-802, 815 | RESOLVED to ~Rs300 Cr, hedged ("I do not have the right number", 796). Line 815 calls the completed Q2 an "expectation". |
| EPC loss 121 / 7,500 ceiling | 440-441 | 121 ties to the filed Turnkey loss Rs122.58 Cr [ROLE 4]. "7500 crores" (441) is unreadable as a two-quarter loss ceiling; no figure is inferred. |
| OFC illustrative arithmetic 89,000 / 9,000 / 1,670 / 500 | 723-731 | UNUSABLE. The MD disowns the analyst's figure (725: "I have not said that you have said that") and declines a monetary OFC scale (719, 721). |
| DATE_ANOMALY R401 | 48 | "half year ended September 13, 2026": ASR garble of 30 September. NEUTRAL. |
| MISSING_QUESTION R420 | 249-250 | Defence question lost in a 32 s gap; answer begins mid-stream (250). See CC-FN-21. |
| ZERO_STANDING R155 | 819 | See CC-FN-01 (F1). |

Turn-mapping notes for A4 (A2 maps turns by coarse line ranges):
- R316 (line 600), R441 (line 599) and R387 (line 600) sit in T070, labelled ANALYST Kushi Soni. The words are management speech: "Percentage in the work all cost is so low price would not be much impacted, but yes supply / We have to tie up in advance. That's what we are working because we would be needing germanium two years from now". Treat them as MD commitments.
- R383 "March 27 and March 28" (553) is the analyst's phrase. The MD affirms it at 555 ("Yes, it will substantially go down"). The date is analyst-framed, MD-affirmed.
- Line 664 "It is largely because of the hyperscaler mix." has no clear speaker; it falls inside T082 (analyst) just before a 30 s gap.
- CFO V.R. Jain is introduced (42-43) and has no attributed turn. Every management answer is attributed to the MD by inference.

---

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| CC-FN-01 | F1 | R155, R459, R153, R154 | 819-820 (T116); 796-802, 815-816 | "Quarter one was nil, but there was no quarter one." ... "Quarter one was fixed." | AMBIGUOUS | Q1 FY27 connectivity revenue spoken as nil, Q2 ~Rs300 Cr, FY27 target Rs800 Cr. If true, the FY27 target needs only ~Rs500 Cr in H2 (~Rs250 Cr a quarter, below Q2), so it is a low bar. But the Q2 figure is hedged (796) and line 820 contradicts "nil". The zero line exists because management carries a stand-alone connectivity target; the template will be tested each quarter. Ask Q1 and Q2 connectivity revenue in Rs Cr. |
| CC-FN-02 | F6 | R032, R242, R250, R317, R388, R408, R409, R442 | 107-109 (T003); 181 (T009); 560-561 (T062); 607-609 (T072) | "we expect revenue growth of at least 80% in this financial year" / "This is a lower number and I surprise you by better numbers" / "there will definitely be growth in Q3" | FORWARD-SIGNAL | The MD's own path beats his guide. H1 Rs4,456.77 Cr [COMPUTED 1,914.98 + 2,541.79] plus Q3 and Q4 at Q2's Rs2,541.79 Cr gives FY27 Rs9,540.35 Cr, +92.76% on FY26 Rs4,949.27 Cr [MEMORY]. The "at least 80%" floor is Rs8,908.69 Cr. Reading A: a sandbagged floor (181 says so). Reading B: Q4 falls (contract timing, price reset). Separating observation: Q3 revenue against Rs2,541.79 Cr. The basis (consolidated FY26) is still not stated. Q2 is "no ... very high margin business" (560-561), so not one-off. The MD's guide history "20-40, 40-80" (109) omits the "at least 60%" relayed via a broker on 05-Oct [MEMORY, MGMT via broker, not verified]. |
| CC-FN-03 | F6 | R034, R082, R243, R302, R303, R304, R410, R432, R433 | 109-110 (T003); 484-487 (T044) | "I would avoid giving any guidance for 28 but I can say you know this 10,000 crore number would be achieved much sooner than we projected in 29 because you can see the run rate by yourself" | FORWARD-SIGNAL | Guidance by inference. The Q2 run-rate annualises to Rs10,167.16 Cr [COMPUTED 2,541.79 x 4]. "No FY28 guide" plus "see the run rate" points to FY28 revenue at or above Rs10,000 Cr. Testable at FY28. Year of the milestone not named. |
| CC-FN-04 | F6 | R037, R045, R046, R047, R049, R050, R070, R073, R141, R142, R143, R145, R246, R261, R262, R263, R269, R291, R328, R329, R361-R363 | 129-130 (T003); 251-253, 278-279 (T018); 407-408 (T034); 769-770 (T099) | "this year, as I said, maintain 500 to 600 crores, next year we look at least 2000 crores" / "possibly 5,000 crores in next two years" | FORWARD-SIGNAL | Defence targets rise inside one call and against memory. FY27: "approximately ... 500" (129) to "500 to 600" (251) to "We'll surely be able to achieve it" (408). FY28: at least Rs2,000 Cr against ~Rs1,500 Cr relayed via broker on 05-Oct [MEMORY]. Rs5,000 Cr: "three years" (252) and "next two years" (770), against "by FY30" [MEMORY]. H1 defence ~Rs80 Cr (776, analyst; filed Rs78.68 Cr [ROLE 4]). H2 needs Rs421.32-521.32 Cr, 5.35x to 6.63x H1. Candidate entry for the narrative-amplification counter (now 2 [MEMORY]); operator rules. |
| CC-FN-05 | F6 | R036, R048, R072, R181, R245, R267, R268, R289, R290, R357, R365, R366, R372, R411, R427 | 124-126 (T003); 273-277 (T018); 402-407 (T034) | "We expect to complete the acquisition during the current quarter" / "just getting completed within November" / "That has an order book of about 16 or 1800 crores. So that will start giving us revenue from this quarter. So all put together 500 crore is not an issue." | FORWARD-SIGNAL | The FY27 Rs500 Cr defence figure leans on consolidating an unnamed, unpriced aerospace target from about November 2026. The book is stated as 1,600 (126), 1,800 (273) and "16 or 1800" (405) in one call, against ~Rs2,000 Cr in Q1 and Rs1,930 Cr for HASPL [MEMORY]. Line 125 calls it an "executed order book", which reads as unexecuted. "All the orders are for exports" (276). No name, consideration or target financials. Separating observation: the completion filing in November, with price and target financials. |
| CC-FN-06 | F13 | R214, R215, R216, R307, R308, R380, R381, R438 | 532-547 (T055-T056) | "that committee is already on the just finishing line of making the recommendation ... maybe week or 10 days time, we would be calling for board meeting ... another couple of weeks, I think we should be able to finalize whatever restructuring we finally do." | FORWARD-SIGNAL | Trigger #6 test is close. A board decision on restructuring is due about early to mid November 2026 [INFERENCE: 19-Oct + ~10 days + ~2 weeks]. The E&Y-advised committee ("E and Y probably", 536) is at recommendation stage. The analyst framed the question as the "EPC business" (532). The deck says "evaluating various strategic options" for verticals in the plural (PPT-FN-01). The call does not state the scope or whether listed HFCL keeps 100% of OFC, defence and aerospace economics. Line 546-547 is cut off: "one thing which is under active consideration." Lean bear until the structure is filed. |
| CC-FN-07 | F6 | R074, R075, R202-R206, R292-R297, R373-R375, R428 | 409-443 (T035-T038) | "the expenses were incurred but bills were not raised because the milestones are yet to be completed" / "This quarter those bills will be getting submitted" / "first quarter of next year you would start seeing profit in this segment." | FORWARD-SIGNAL | (a) Q2 Turnkey loss "121 or some crores" (440; filed Rs122.58 Cr [ROLE 4]) is above the Rs80-90 Cr a quarter guide [MEMORY, broker]. (b) Turnkey profit moves to Q1 FY28 (443). (c) Q3 Turnkey will carry catch-up billing for Q2 cost (436-437: "what had been debited as expense in the last quarter, again that billing would be done in this quarter"), so Q3 is not a run-rate. (d) Army AMC cost is being incurred before the contract is signed (422-425: "may be a week or 10 days it will get approved and will get signed"); recoverability rides on signature. (e) The two-quarter loss ceiling (441) is unreadable. O&M margin "could be something like 15 to 20 percent" (530) sits against a loss-making segment. |
| CC-FN-08 | F6 | R088, R202, R203, R213, R292 | 418-423 (T036); 522-523 (T053-T054) | "in the order book, we are seeing 5000 crore of O&M order book." "Yes." ... "BSNL is in final stage of approval, may be a week or 10 days it will get approved and will get signed" | AMBIGUOUS | Does the Rs5,000 Cr O&M book inside the Rs28,900 Cr "secured" book (85-86) count the unsigned Army AMC (year 1 via BSNL)? If yes, part of the confirmed book is not yet a signed contract. |
| CC-FN-09 | F6 | R309, R310, R382, R383, R090, R148 | 548-555 (T057-T060); 785 (T106) | "we have taken some new debts for CAPEX, finally the debt reduction will start in the current year." ... "Yes, it will substantially go down." | FORWARD-SIGNAL | Dated debt commitment: gross debt at 31-Mar-2027 below 30-Sep-2026 and "substantially" lower at 31-Mar-2028. Gross borrowings rose Rs126.76 Cr in H1 to Rs1,840.13 Cr consolidated [ROLE 4]. "Pending CAPEX is 1800 crores" (785) with no funding split; warrant money not mentioned. Testable at the FY27 balance sheet. |
| CC-FN-10 | F6 | R060, R061, R113-R116, R164-R166, R273, R323, R334, R336-R339, R462, R463, R466-R468 | 330-334 (T026); 703-709 (T088-T089); 874-878 (T127); 927-944 (T135) | "whenever those contracts expire, of course, price variation has to be there" / "they have gone up by 600%. I don't have to suffer because of that because I have pre-determined contracts" | FORWARD-SIGNAL | Preform input-cost reset. Supplier contracts run yearly, 18 or 24 months (330-333). Spot preform is "up by 600%" (930, ASR-caveated). Own 600 MT covers "roughly about half" of capacity (705-708) and only from Oct-2028; the rest is bought "for which we have some long-term contracts also" (709). "No chance I see of getting it worse" (202) rests on contract timing that is not dated. Customer side: reset clause in "most of long term contracts" (877), none in 4-6 month contracts (878). Separating observation: preform contract expiry dates and the fixed-price share of FY28 preform need. |
| CC-FN-11 | F7 | R312, R335, R384, R385, R439, R464 | 580-583 (T067); 882-890 (T128-T131) | "we are going to have a midterm solution for our own preform starting from the first quarter of the next year itself, calendar year itself" / "I cannot elaborate this is a trade statement" | AMBIGUOUS | A new, undisclosed preform arrangement from Jan-Mar 2027. Nature (tolling, partner, acquisition, related party) withheld under "commercial confidentiality" (581). Only claim: "it would reduce cost" (889-890). It may carry a capital or related-party commitment. |
| CC-FN-12 | F6 | R065-R067, R153, R154, R157, R158, R279-R282, R333, R369, R370, R425 | 364-371 (T032); 815-816 (T114); 857-858 (T124); 898-900 (T133) | "this year itself we have a connectivity solution revenue of about more than 800 crores we had projected which may be better rather and next year we have projected revenue 2000 crores" | FORWARD-SIGNAL | FY28 connectivity Rs2,000 Cr against the Q1 promise log of Rs800-1,000 Cr for FY27-28 [MEMORY], a 2x to 2.5x raise. In-data-centre products start "last quarter of the current financial year or ... beginning of the next" (367-369). The Rs215 Cr DC-connectivity facility (Sep-2027 [MEMORY]) is not mentioned. Certification for in-DC connectivity "is already there" (899). |
| CC-FN-13 | F14 | R062-R064, R068, R094, R117, R118, R140, R276-R278, R285, R313, R314, R324, R371, R386, R440 | 360-362 (T032); 377-378; 584-588 (T067); 716-717 (T093); 768 (T099) | "fiber itself is going from 28 million to 34 and 34 to 43, cable is going to about from 34 to 63 million fiber kilometers" / "October 28 timeline" | AMBIGUOUS | Capacity steps restated with no dates on the call. The interim fibre step 28 to 34 (Dec-2026 33.9 [MEMORY]) is still named but undated. Current cable is "34" (361, 716) against the deck's 39 current (PPT-FN-10) and Q1's 30.5 [MEMORY]. "34 to 53" (768) conflicts with 63. Machine delays of "two three months" are "already taken into account" (585-586). |
| CC-FN-14 | F7 | R055, R058, R059, R083-R085, R422-R424, R453 | 318-322 (T024); 502-509 (T046); 733-741 (T093) | "in terms of money terms, whatever capacity utilization we have invested, that is 100%" / "34 is the political capacity" | AMBIGUOUS | Utilisation is defined on revenue, not physical output. With a ~20% Q2 price rise (647), money-based utilisation reads 100% or more while some cable lines "may be lying idle" (736). Volume headroom from 34 to 63 cannot be read off this metric. Ask physical fkm output by line. |
| CC-FN-15 | F7 | R042, R171, R413-R415, R435, R439, R444, R447, R455-R458, R460, R464 | 42-43 (T002); 168-171 (T007); 516 (T050); 796 (T110); 853 (T122); 885 (T129) | "I do not have the exact number" / "I do not have that number in particular" / "I do not have the right number" / "Cannot give you a ballpark number" | AMBIGUOUS | Precision asymmetry. Delivered-period splits (hyperscaler revenue, Q2 connectivity, price vs volume, preform solution) are declined or hedged. Forward figures (defence 2,000 and 5,000, connectivity 2,000, Rs10,000 Cr) come as round numbers with "surely" (408) and "no chance" (202). The CFO is present (42-43) and has no attributed turn (speaker inference caveat). Fits the "provisional OVERPROMISER-watch" archetype [MEMORY]. |
| CC-FN-16 | F7 | R040, R041, R042, R185, R413, R414, R415, R087 | 163-172 (T006-T007); 514-520 (T049-T052) | "out of 18,500 crore large portion would be from hyperscalers only ... maybe 70 percent" | AMBIGUOUS | Hyperscaler book ~Rs12,950 Cr [COMPUTED 0.70 x 18,500] = 44.81% of Rs28,900 Cr. The $1.1B / Rs10,159 Cr single order [MEMORY] can be up to 78.4% of that. Customer names "under NDA" (170). "We have some other Hyperscaler orders" (518-520) is the only answer on a second customer. |
| CC-FN-17 | F7 | R099-R103, R159, R160, R162, R163, R320, R331, R445, R460, R461 | 641-648 (T078-T079); 839-853 (T120-T122); 865-870 (T126-T127); 915-926 (T134) | "I said this in the last quarter also that looks to be stabilizing but then it has gone up by some 20%." | FORWARD-SIGNAL | Q2 margin carries a ~20-25% fibre price rise (647, 869-870) that the MD did not foresee in Q1. Price vs volume split is withheld (853). Outlook: "some increase, but not as much" (647). Bear reading: margin reverts when prices flatten or fall as global capacity rises 40-50% (921, analyst). Separating observation: Q3 realisation per fkm. |
| CC-FN-18 | F7 | R218, R219, R315, R316, R340, R387, R392, R441, R469 | 589-600 (T068-T070); 963-974 (T139) | "It's too early to finalize content" / "Country to country, there are export restrictions" / "two years from now geopolitical situation may be completely different" | AMBIGUOUS | Germanium for the Oct-2028 preform plant is not contracted. Export restrictions are acknowledged (968). Input risk to the backward-integration margin step. |
| CC-FN-19 | F14 | R019-R027, R405 | 58-70 (T003) | "EBITDA margin expanded to 25.89% improving by 640 basis points year on year and 264 basis points quarter on quarter. While PED margin rose to 15.51%" | NEUTRAL-FACT | Opening arithmetic ties on every line checked (PBT +406.49%, PAT +448.14%, H1 PBT +1311.6%, H1 PAT +1401.3%, revenue QoQ +32.73%). EBITDA +47.78% QoQ and +264 bps tie to Q1 Rs445.27 Cr / 23.25% [MEMORY], the OTHER-INCOME-INCLUSIVE basis (operating Q1 was Rs414.12 Cr / 21.63% [MEMORY]). So the spoken 25.89% includes other income. "PED margin" 15.51% = PAT / revenue [COMPUTED 394.22 / 2,541.79]. Bears on Q18 by arithmetic only; the basis is not stated. |
| CC-FN-20 | F14 | R029, R108, R125, R128-R139, R146 | 750-755 (T095); 764-765 (T097) | "like when I met you last time I think order book was 26,000 crore ... now you guys we have 28,900 crores" | NEUTRAL-FACT | The MD's prior base, 26,000, is below the Q1 deck's Rs26,665 Cr [MEMORY]. On filed figures Q2 inflow is about Rs4,788 Cr [ROLE 4: 28,911 - 26,665 + 2,541.79], about Rs700 Cr below the spoken 5,500. Book-to-bill about 1.9x either way. The filed figure governs. |
| CC-FN-21 | F14 | R401, R420, R431, R446, R349; T018, T043, T083, T102, T103 | 48; 249-250; 482-483; 665-666; 776-778 | "[00:20:00] ... [00:20:32] give a very short answer and a very long answer." / "Hello, so the current participant seems to have dropped from the queue." | NEUTRAL-FACT | Untranscribed audio at three load-bearing points: a defence question (32 s; question lost), the FY28 guidance question (21 s), and the margin-source answer (30 s). The H1-defence-gap question (T102) was cut off when the participant dropped. Two of three defence questions have no recorded question. Half-year end spoken as "September 13" (48). Obtain the company's official transcript when filed and re-read these four points. |
| CC-FN-22 | F17 | none (silence); nearest R293-R295 | 427-438 (T036); 1011-1012 (T143) | "the expenses were incurred but bills were not raised" / "I think you know all questions that can be there have already been answered" | CONFIRMATORY-NEGATIVE | Tripwire #4. No receivables ageing, DSO or unbilled-revenue figure on the call, and no analyst asked. The only working-capital content is qualitative (BharatNet milestones). Q1 was the first silent quarter [MEMORY, 13-Oct review]; the Q2 call is silent. The trigger wording is "Two consecutive quarters of receivables silence". A4 rules on firing against the Q2 filing (Role 4 Q2: receivables Rs2,889.58 Cr; other current assets up Rs317.31 Cr in H1). |
| CC-FN-23 | F17 | R086, R087, R435 | 513-517 (T049-T050) | "Sir, I do not have that number in particular, only thing I can say we have already started delivering" | CONFIRMATORY-NEGATIVE | Notion's "single cleanest metric" (export-OFC / hyperscaler revenue in Rs Cr) is withheld again: second consecutive quarter, and all three Q2 channels (results, deck, call). Thesis-broken trigger #1 (delivery below 60% pro-rata by H1 FY28) has no delivery metric to test. Exports given only as "approximately 493%" growth (78). |
| CC-FN-24 | F17 | R177, R191, R264, R265, R288, R364, R052, R271 | 122 (T003); 259-264 (T018); 284-285; 396-399 (T034) | "electronic fuses" (product list only) / "second trial is expected to happen in another two weeks" / "that has almost been through approval another couple of weeks" | CONFIRMATORY-NEGATIVE | Fuze approval (checklist #4 green: by Q2 FY27) is not discussed. History: "couple of months" for 5 quarters to Q4 FY26 and SILENT in Q1 [MEMORY]. The same short-horizon idiom now attaches to the foliage penetration radar, stated two ways in one call (a pending trial at 262-263; "almost ... approval" at 398-399). MMHG: tender "participated" (284), not won. BMP-2: silent. |
| CC-FN-25 | F17 | R344 | 1011-1014 (T143) | "any further query which is left unanswered please send a mail to Amitagarwal and we will immediately reply" | AMBIGUOUS | Governance and cash items were silent: promoter pledge, warrants (Rs416.25 Cr balance), Nivetti closure, standalone-vs-consolidated PAT gap and subsidiary profit location, HASPL Rs90 Cr object, QIP fund use, tax accrued but unpaid (Rs123.40 Cr H1 [ROLE 4]), export-share guide. The MD commits to "immediately reply" to emailed queries. Route every SILENT and DECLINED Step 8.5 question to IR and score the reply speed as a dated commitment. |

Classification totals: FORWARD-SIGNAL 10; AMBIGUOUS 9; CONFIRMATORY-NEGATIVE 3; NEUTRAL-FACT 3. All FORWARD-SIGNAL and AMBIGUOUS findings go to A4 for questions.

---

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | A2 flagged one ZERO_STANDING row (R155, Q1 connectivity revenue nil); CC-FN-01. |
| F2 Standalone vs consolidated | N.A. | Concall; no S-vs-C table. The PAT gap went unasked (F17 row). |
| F3 Shell-entity detection | N.A. | Concall; no cost lines by entity. |
| F4 Unaudited contribution | N.A. | Concall; no auditor paragraphs. |
| F5 Going concern / EoM | N.A. | Concall; no EoM paragraph. |
| F6 Forward-commitment mining | FINDING | 34 commitments registered (section 4); CC-FN-02 to 05, 07 to 10, 12. |
| F7 Hedge mining | FINDING | CC-FN-11, 14 to 18. Hedges sit on delivered-period numbers; forward numbers come unhedged. |
| F8 Tax forensics | N.A. | Concall; no tax data spoken. Tax-accrual cash reading silent (F17). |
| F9 OCI forensics | N.A. | Concall; no OCI data. |
| F10 Share count / dilution | N.A. | Concall; no EPS or share data. Warrants silent (F17). |
| F11 Net worth tie-out | N.A. | Concall; no equity figures. |
| F12 Segment forensics | N.A. | No segment assets or liabilities spoken. Segment narrative logged under F6 (CC-FN-07). |
| F13 Board outcome beyond results | FINDING | An E&Y-advised restructuring committee is near recommendation; a board meeting is promised in ~10 days plus ~2 weeks; CC-FN-06. |
| F14 Drafting inconsistencies | FINDING | Spoken-number inconsistencies and transcript integrity; CC-FN-13, 19, 20, 21. |
| F15 Entity list diffs | N.A. | No consolidation list on a call. The forthcoming aerospace consolidation is logged under CC-FN-05. |
| F16 Dropped / reframed disclosures | N.A. | Presentation-specific. Guidance reframing on the call is logged under F6 (CC-FN-02, 04, 12). |
| F17 Silence audit | FINDING | Section 5. Role 4 42: 1 ANSWERED, 11 PARTIAL, 1 DECLINED, 29 SILENT. Q1 15: 1 ANSWERED, 6 PARTIAL, 0 DECLINED, 8 SILENT. CC-FN-22 to 25. |

GATE A3: pass (17 of 17 marked, 0 blank).

---

## 4. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Line / turn | Status word |
|---|---|---|---|---|
| 1 | FY27 revenue growth at least 80% (third raise: 20, 40, 80) | FY27 | 104-108 (T003) | initiated |
| 2 | Q3 revenue above Q2 ("definitely be growth in Q3") | Q3 FY27 | 607-611 (T072) | initiated |
| 3 | Q2 is "not ... a peak" | undated | 88-89 (T003) | initiated |
| 4 | Rs10,000 Cr revenue "much before" FY29 | before FY29 | 109-110; 484-485 (T044) | initiated |
| 5 | FY28 "better than what we are doing now" | FY28 | 487-495 (T044) | initiated |
| 6 | Pipeline converting; order book to strengthen | undated | 86-87, 93, 99-100 (T003) | underway |
| 7 | ~Rs1,800 Cr capex across OF, OFC, preform ("pending") | to Oct-2028 | 112-113 (T003); 785 (T106) | underway |
| 8 | Fibre 28 to 34 to 43; cable 34 to 63 mn fkm | undated on call | 360-362 (T032); 716-717 (T093) | underway |
| 9 | Preform plant construction "going to start soon" | near term, undated | 377 (T032) | initiated |
| 10 | Own preform 600 MT, "late 28" / "October 28" | Oct-2028 | 377-378 (T032); 584-588 (T067) | underway |
| 11 | Preform "midterm solution", undisclosed | Q1 CY2027 | 580-583 (T067) | initiated |
| 12 | Germanium supply tie-up | before Oct-2028 | 593-600 (T069-T070); 963-970 (T139) | initiated |
| 13 | Margins "going to get better only"; "no chance ... worse" | undated | 201-202 (T015); 343 (T028) | initiated |
| 14 | Connectivity revenue more than Rs800 Cr | FY27 | 369-370 (T032); 815-816 (T114) | underway |
| 15 | Connectivity revenue Rs2,000 Cr | FY28 | 371 (T032); 858 (T124) | initiated |
| 16 | In-data-centre connectivity products start revenue | Q4 FY27 or early FY28 | 366-369 (T032) | initiated |
| 17 | Aerospace acquisition completes | within Nov-2026 | 124 (T003); 273-274 (T018); 404 (T034) | underway |
| 18 | Aerospace revenue consolidated from this quarter | Q3 FY27 | 275 (T018); 406 (T034) | initiated |
| 19 | Large aerospace export orders | "next few months" | 276-277 (T018) | initiated |
| 20 | Defence revenue ~Rs500 Cr ("500 to 600") | FY27 | 129-130; 251; 407-408 | underway |
| 21 | Defence revenue at least Rs2,000 Cr | FY28 | 251-252, 278 (T018); 769 (T099) | initiated |
| 22 | Defence revenue ~Rs5,000 Cr | "three years" (252) / "next two years" (770) | 252-253; 770 | initiated |
| 23 | Foliage penetration radar second trial / approval | ~2 weeks (early Nov-2026) | 262-263 (T018); 397-399 (T034) | underway |
| 24 | Ground surveillance radar export orders | undated | 268-269 (T018) | initiated |
| 25 | Ammunition complex construction start; revenue in ~2 years | "soon"; ~late 2028 | 134 (T003); 281-283 (T018) | initiated |
| 26 | MMHG 800,000-unit tender (participated) | undated | 284-285 (T018) | underway |
| 27 | Army AMC (year 1 via BSNL) approved and signed | ~1-1.5 weeks (end-Oct 2026) | 418-423 (T036) | underway |
| 28 | BharatNet milestone bills submitted | Q3 FY27 | 435-437 (T036) | underway |
| 29 | Turnkey loss from unbilled expense "will not happen this quarter"; two-quarter ceiling (unreadable) | Q3-Q4 FY27 | 438-441 (T036) | initiated |
| 30 | Turnkey segment profit | Q1 FY28 | 443 (T038) | initiated |
| 31 | Restructuring recommendation, board meeting, finalisation | ~10 days + ~2 weeks (by ~mid-Nov 2026) | 535-545 (T056) | underway |
| 32 | Debt reduction starts in FY27; "substantially" lower at Mar-27 and Mar-28 | 31-Mar-2027 / 31-Mar-2028 | 551-555 (T058-T060) | initiated |
| 33 | Large telco orders ("very concrete inquiries") | undated | 243-245 (T017) | initiated |
| 34 | IR to "immediately reply" to emailed queries | immediate | 1011-1014 (T143) | initiated |

Status transitions against the Q1 promise log [MEMORY]: preform moves from 300 MT Rs580 Cr Jul-2029 to 600 MT Oct-2028 (raised and pulled forward). Aerospace moves from "proposed" to "within November". The growth guide moves from 40% to at least 80%. Connectivity FY28 moves from Rs800-1,000 Cr to Rs2,000 Cr. EBITDA 22-25% by FY29 is superseded by "no chance ... worse" (the deck says above 27%). Fuze: no transition (silent).

---

## 5. F17 SILENCE AUDIT

Status key: ANSWERED (specific answer) / PARTIAL (some content, the core ask unmet) / DECLINED (asked, refused or "do not have") / SILENT (not addressed). Consecutive-quarter counts: the Q1 FY27 call was never transcribed or scored, so call-based counts start at Q2 = 1. Where memory records Q1 silence in the filings or the Q4 FY26 call, the count uses that mixed basis and says so.

### 5A. Role 4 Step 8.5 questions (42)

| Q | Topic | Status | Transcript line / note |
|---|---|---|---|
| 1 | Strategic options: under 100% economics? Yes/no | PARTIAL | 535-547: committee, E&Y, board in ~2-4 weeks; scope and yes/no not given; question framed as "EPC business" (532). CC-FN-06 |
| 2 | Receivables over 6 months; unbilled revenue | SILENT | Not asked. Qualitative only, 427-438. CC-FN-22 |
| 3 | Consol vs standalone PAT gap; which entity; transfer price | SILENT | Not asked |
| 4 | "At least 80%" basis; Q3 below Q2? | PARTIAL | Yes/no answered: Q3 growth (607-608); "lower number" (181). Basis not stated. CC-FN-02 |
| 5 | Defence consolidation CPs; Rs90 Cr HASPL by 31-Dec | PARTIAL | Close "within November" (404). CPs and Rs90 Cr SILENT |
| 6 | Aerospace consideration, target financials, customers, tenure | SILENT | Only "all the orders are for exports" (276) and the book size. No price or financials. CC-FN-05 |
| 7 | Quarter Turnkey reaches zero | ANSWERED | "first quarter of next year you would start seeing profit" (443). CC-FN-07 |
| 8 | Q2 export-OFC revenue to hyperscalers, Rs Cr | DECLINED | "I do not have that number in particular" (516). CC-FN-23 |
| 9 | Warrant conversion, Rs416.25 Cr balance | SILENT | Not asked |
| 10 | Turnkey liabilities -Rs185.25 Cr: advances vs payables | SILENT | Not asked |
| 11 | Subsidiary inventory release in Q2 revenue | SILENT | Not asked |
| 12 | Name target; book includes target? | SILENT | Target unnamed (124-126, 273) |
| 13 | Defence Rs500 Cr dependence on acquisition, Rs Cr | PARTIAL | Aerospace listed in the "all put together 500" (402-407); no Rs split; gap question cut off (776-778) |
| 14 | Target book ~2,000 to ~1,600: executed or cancelled? | SILENT | MD's own "16 or 1800" (405) |
| 15 | Capex funding split; FY27 capex | PARTIAL | "taken some new debts for CAPEX" (551-552); "pending CAPEX is 1800 crores" (785); no split or FY27 figure |
| 16 | Export guide >70% vs 65%+ | SILENT | Exports only "approximately 493%" (78) |
| 17 | Order book executing in FY27 and FY28, Rs Cr | PARTIAL | "4 to 6 months ... 3 years, 4 years" (697-698); "next 5 years" (702); "not evenly distributed" (759); no Rs split |
| 18 | >27% EBITDA target includes other income? | SILENT | Not stated. A3 arithmetic: the spoken 25.89% is the incl-OI basis (CC-FN-19) |
| 19 | OF 33.9 / OFC 42.36 mn fkm by Dec-2026? | PARTIAL | Steps 28 to 34 to 43 and 34 to 63 restated, undated (361-362). CC-FN-13 |
| 20 | Held-for-sale buyer; group entity? | SILENT | Not asked |
| 21 | Other equity debit ~Rs30.6 Cr | SILENT | Not asked |
| 22 | Recurring deferred-tax credit | SILENT | Not asked |
| 23 | OCI investment gain / reversal | SILENT | Not asked |
| 24 | Rs407.48 Cr intangibles under development | SILENT | Radars "under trial" (259-262); no capitalisation content |
| 25 | QIP-funded R&D payroll: expensed or capitalised? | SILENT | Not asked |
| 26 | Remaining QIP R&D money by 31-Mar-2027 | SILENT | Not asked |
| 27 | QIP money in cash-credit account | SILENT | Not asked |
| 28 | Rs10.30 Cr FD; Rs21.22 Cr QIP FD | SILENT | Not asked |
| 29 | Rs93 Cr QIP GCP use | SILENT | Not asked |
| 30 | Rs175 Cr preform money: equity or loan; cost-plus | SILENT | Not asked; preform solution withheld (885) |
| 31 | Rs90 Cr deadline extension; Reg 32 statement | SILENT | Not asked |
| 32 | Other 19-Oct board items | SILENT | A future board meeting on restructuring is promised (541) |
| 33 | Rs10,000 Cr year; defence forecast or aspiration | PARTIAL | "much sooner than we projected in 29" (484-485), no year; defence "aspiration" (129) vs "surely" (408) |
| 34 | Promoter pledge zero? | SILENT | Not asked |
| 35 | Defence further investment FY27, Rs Cr | SILENT | Ammunition complex "start soon" (134); no Rs |
| 36 | Para-7 subsidiaries' H1 OCF; receivable from HFCL | SILENT | Not asked |
| 37 | Q2 PCS/DC revenue and order book | PARTIAL | ~Rs300 Cr, hedged (796-802, 815); book SILENT |
| 38 | Secured raw materials: suppliers, volume, tenor, price | PARTIAL | Tenors 12/18/24 months (330-333); "pre-determined contracts" (931); suppliers withheld (581) |
| 39 | Q2 OFC realisation per fkm; LT contracts below spot | PARTIAL | Fibre ~$15 vs ~$25-27 (629-631); +~20% (647); reset clause in most LT contracts (877); price/volume split declined (853) |
| 40 | "#1 in OFC": India or global | SILENT | Not asked |
| 41 | BharatNet III Q2 revenue; remaining book | SILENT | Qualitative only (427-438) |
| 42 | H2 advance tax due, Rs Cr (tax-accrual cash reading) | SILENT | Not asked |

Totals: ANSWERED 1; PARTIAL 11; DECLINED 1; SILENT 29 (sum 42).

### 5B. Q1 FY27 questions (Notion section 8; 15)

| Q1 # | Topic | Status | Line / note |
|---|---|---|---|
| 1 | Export-OFC revenue; hyperscaler share of book | PARTIAL | Share "maybe 70 percent" of Rs18,500 Cr (171); revenue declined (516) |
| 2 | Guide floor or sandbag; aspiration or estimate | ANSWERED | "we expect ... at least 80%" (108); "lower number" (181) |
| 3 | Consol vs standalone PAT; subsidiary; transfer price | SILENT | |
| 4 | Auditor other-matter coverage | SILENT | |
| 5 | Turnkey; BharatNet III revenue, margin, receivables | PARTIAL | Loss cause explained (427-438); no Rs figures |
| 6 | Receivables, DSO, unbilled; inventory deferral | SILENT | CC-FN-22 |
| 7 | Steady-state ETR | SILENT | |
| 8 | OCI swing | SILENT | |
| 9 | Diluted EPS vs warrants | SILENT | |
| 10 | Rs215 Cr DC facility funding, revenue, margin | PARTIAL | "installing higher capacity for connectivity solutions" (364); no Rs215 Cr, funding or margin |
| 11 | Defence via entity to be acquired: target, price, structure, close | PARTIAL | Close in November (404); target, price, structure silent |
| 12 | Promoter holding; pledge zero | SILENT | |
| 13 | Capacity completion date (Dec-2026) | PARTIAL | Steps restated, undated (361-362) |
| 14 | Export share base; durability | SILENT | |
| 15 | Order book executable vs L1; margins | PARTIAL | Delivery tenor (697-702); "secured" vs "pipeline" wording (85-87); no L1 split or margins |

Totals: ANSWERED 1; PARTIAL 6; DECLINED 0; SILENT 8 (sum 15). AR deep-dive top five [MEMORY]: Turnkey recovery ANSWERED (443); defence Rs500 Cr underwrite PARTIAL (402-407); export-OFC WOS transfer price SILENT; HASPL-level strategic stake SILENT (CC-FN-06 scope open); Rs127 Cr receivables over 3 years SILENT.

### 5C. WHAT WAS NOT DISCUSSED (monitoring checklist, seed promises, Role 4 open items)

| Item | Source | Status on Q2 call | Consecutive quarters silent | Note |
|---|---|---|---|---|
| Tripwire #4: receivables ageing, DSO, unbilled | Notion s4, s7; Role 4 Q2 | SILENT (qualitative BharatNet only, 427-438) | 2 (Q1 per memory; Q2 call). Mixed basis 3 counting Q4 FY26 call deferral [MEMORY] | CC-FN-22, CONFIRMATORY-NEGATIVE. Trigger wording matches; A4 rules |
| Trigger #6: strategic options / restructuring structure | Notion s4; Role 4 Q1 | PARTIAL (timing only, 535-547) | n.a. (timing given) | CC-FN-06. Decision ~mid-Nov 2026 |
| Aerospace acquisition price and target financials | Role 4 Q6, Q12, Q14 | SILENT | 2 (Q1 Q11 unanswered in filings [ROLE 4 0F]; Q2 call) | CC-FN-05 |
| Tax-accrual cash reading (Rs123.40 Cr charged, unpaid) | Role 4 Q42 | SILENT | 1 (new item) | CC-FN-25 |
| "At least 80%" guide basis | Role 4 Q4; Q1 Q2 | PARTIAL (direction yes; basis no) | 2 on basis (Q1 filings, Q2 call) | CC-FN-02 |
| HASPL Rs90 Cr object | Role 4 Q5, Q31 | SILENT | 1 (new item) | CC-FN-25 |
| Export-OFC / hyperscaler revenue Rs Cr (checklist #1) | Notion s7 | DECLINED (516) | 2 (Q1 RED/SILENT [MEMORY]; Q2 all channels) | CC-FN-23, CONFIRMATORY-NEGATIVE |
| Cash conversion (H1 CFO, inventory) | Notion s7 | SILENT (analyst mention only, 549-550) | 1 on call | |
| Telecom product PBT margin (checklist #3) | Notion s7 | PARTIAL (analyst 32-33%, 661; MD does not confirm, 667) | 0 | |
| Fuze approval (checklist #4) | Notion s7, s8 | SILENT (product list only, 122) | 2 (Q1 SILENT [MEMORY]; Q2 call), after 5 quarters of "couple of months" | CC-FN-24, CONFIRMATORY-NEGATIVE |
| MMHG tender won; BMP-2 sample | Notion s7 | PARTIAL (MMHG participated, 284) / SILENT (BMP-2) | BMP-2: 2 | |
| Promoter holding and pledge (checklist #5) | Notion s7; Q1 Q12; Role 4 Q34 | SILENT | 2 (Q1 pledge SILENT [MEMORY]; Q2 call) | CC-FN-25 |
| BharatNet III revenue, WC, PBT margin (checklist #6, #7) | Notion s7 | PARTIAL (qualitative, 427-438; generic turnkey margin 15-20%, 528-530) | #7: 2 on Rs figures | CC-FN-07 |
| Mobilisation / LC terms (checklist #8, #12) | Notion s7 | SILENT | 2 (Q1 SILENT [MEMORY]) | |
| Nivetti closure by 31-Dec-2026 (checklist #9) | Notion s7, s8 | SILENT | 2 (Q1 SILENT [MEMORY]; Q2 call) | |
| 10-Jul export order: second customer, PBT >=8%, Dec-2026 execution (#10, #11, #13) | Notion s7 | PARTIAL (#10: "other Hyperscaler orders", 518-520) / SILENT (#11, #13) | 1 on call | |
| Rs215 Cr DC facility, Sep-2027 | Notion s8 promise log | SILENT on amount and date | 1 on call | CC-FN-12 |
| Exports 60%+ FY27 onward | Notion s8 promise log | SILENT | 1 on call | |
| Promoter warrant balance ~Nov-2027 | Notion s8; Role 4 Q9 | SILENT | 1 on call | |
| HTL minority holding; transfer price | Notion s7 | SILENT | 2 (unverified since AGM [MEMORY]) | |
| Preform technology partner | Notion s7 (14-Sep) | DECLINED ("commercial confidentiality", 581; "trade statement", 885) | 1 | CC-FN-11 |
| Standalone vs consolidated PAT gap | Q1 Q3; Role 4 Q3 | SILENT | 2 (Q1 filings, Q2 call) | |

---

## 6. NOTES FOR A4

- Top three forward reads: (1) CC-FN-06, restructuring decision within ~4 weeks with scope unstated (trigger #6); (2) CC-FN-02 with CC-FN-17, the guide sits below the MD's own Q3 path, but Q2 margin carries a ~20% price rise he did not foresee; (3) CC-FN-10, preform cost reset at contract expiry against a "no chance worse" margin claim.
- Confirmatory negatives: receivables silence (CC-FN-22), export-OFC revenue withheld (CC-FN-23), fuze silence (CC-FN-24).
- Every SILENT and DECLINED Step 8.5 question goes to IR by email (channel committed at 1011-1014).
- Machine-transcript caveat applies to all 25 findings. Filed figures govern any conflict.
- Fulltext and structured inputs were sufficient. No pipeline error; no need for the source.

---

```yaml
stage: A3-forensics
company: "HFCL"
quarter: "Q2 FY27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/hfcl-q2fy27/work/forensics_concall_hfcl_q2fy27.md"
ledger_reconciled_pct: 100        # 615 of 615 IDs (R001-R470 + T001-T145); fulltext lines 1-1020 read in full
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "CC-FN-01", check: "F1", line: "819-820; 796-802, 815-816", classification: "AMBIGUOUS", implication: "Q1 connectivity nil (ZERO_STANDING R155), Q2 ~Rs300 Cr hedged, FY27 Rs800 Cr needs only ~Rs250 Cr/q in H2; line 820 contradicts nil; ask Q1/Q2 in Rs Cr"}
  - {id: "CC-FN-02", check: "F6", line: "107-109; 181; 560-561; 607-609", classification: "FORWARD-SIGNAL", implication: "MD's Q3>Q2 path implies FY27 >= Rs9,540 Cr (+92.8%) vs 'at least 80%' floor Rs8,909 Cr; sandbag or Q4 drop; basis unstated; guide history omits broker '60%' step"}
  - {id: "CC-FN-03", check: "F6", line: "109-110; 484-487", classification: "FORWARD-SIGNAL", implication: "'avoid giving any guidance for 28' plus 'see the run rate' (Q2 x4 = Rs10,167 Cr) = implicit FY28 >= Rs10,000 Cr; year unnamed"}
  - {id: "CC-FN-04", check: "F6", line: "129-130; 251-253; 278-279; 407-408; 769-770", classification: "FORWARD-SIGNAL", implication: "defence FY27 500 -> 500-600 -> 'surely'; FY28 >=2,000 vs ~1,500 broker 05-Oct; 5,000 in 3 vs 2 years vs FY30 memory; H2 needs 5.4-6.6x H1 Rs78.68 Cr; amplification-counter candidate"}
  - {id: "CC-FN-05", check: "F6", line: "124-126; 273-277; 402-407", classification: "FORWARD-SIGNAL", implication: "FY27 defence Rs500 Cr leans on consolidating an unnamed, unpriced aerospace target 'within November'; book 1,600/1,800/'16 or 1800' in one call; no price or target financials"}
  - {id: "CC-FN-06", check: "F13", line: "532-547", classification: "FORWARD-SIGNAL", implication: "E&Y-advised restructuring committee at recommendation; board meeting ~10 days then finalise ~2 weeks (~mid-Nov 2026); scope (EPC only vs verticals) and 100%-economics not stated; trigger #6 test imminent; line 547 cut off"}
  - {id: "CC-FN-07", check: "F6", line: "409-443; 526-530", classification: "FORWARD-SIGNAL", implication: "Turnkey loss ~121 (filed 122.58) above Rs80-90 Cr guide; profit moved to Q1 FY28; Q3 carries catch-up billing of Q2 cost (not run-rate); Army AMC cost incurred before contract signature; 2-quarter ceiling unreadable"}
  - {id: "CC-FN-08", check: "F6", line: "418-423; 522-523", classification: "AMBIGUOUS", implication: "Rs5,000 Cr O&M book inside 'secured' Rs28,900 Cr may count the unsigned Army/BSNL AMC"}
  - {id: "CC-FN-09", check: "F6", line: "548-555; 785", classification: "FORWARD-SIGNAL", implication: "debt to fall from FY27 and 'substantially' by Mar-27/Mar-28 (analyst-framed, MD-affirmed) though gross debt rose Rs126.76 Cr in H1 and Rs1,800 Cr capex pending with no funding split"}
  - {id: "CC-FN-10", check: "F6", line: "330-334; 703-709; 874-878; 927-944", classification: "FORWARD-SIGNAL", implication: "preform supplier contracts 12-24 months, spot up ~600%, own 600 MT covers ~half capacity only from Oct-2028; 'price variation has to be there' at expiry vs 'no chance worse' margins; expiry dates undisclosed"}
  - {id: "CC-FN-11", check: "F7", line: "580-583; 882-890", classification: "AMBIGUOUS", implication: "undisclosed preform 'midterm solution' from Q1 CY2027; nature, counterparty and capital withheld ('trade statement'); possible capital or related-party commitment"}
  - {id: "CC-FN-12", check: "F6", line: "364-371; 815-816; 857-858; 898-900", classification: "FORWARD-SIGNAL", implication: "connectivity FY28 Rs2,000 Cr vs Rs800-1,000 Cr Q1 promise log (2-2.5x raise); in-DC products from Q4 FY27; Rs215 Cr DC facility unmentioned"}
  - {id: "CC-FN-13", check: "F14", line: "360-362; 377-378; 584-588; 716-717; 768", classification: "AMBIGUOUS", implication: "capacity steps undated on call; interim 28->34 fibre step (Dec-2026 memory) still named; current cable 34 vs deck 39 vs Q1 30.5; '34 to 53' outlier vs 63"}
  - {id: "CC-FN-14", check: "F7", line: "318-322; 502-509; 733-741", classification: "AMBIGUOUS", implication: "utilisation defined 'in money terms'; with ~20% price rise it reads 100%+ while some lines idle; volume headroom unreadable; ask physical fkm output"}
  - {id: "CC-FN-15", check: "F7", line: "42-43; 168-171; 516; 796; 853; 885", classification: "AMBIGUOUS", implication: "delivered-period splits declined or hedged while forward targets stated as round numbers with 'surely'/'no chance'; CFO present with no attributed turn; overpromiser-watch pattern"}
  - {id: "CC-FN-16", check: "F7", line: "163-172; 514-520", classification: "AMBIGUOUS", implication: "~Rs12,950 Cr hyperscaler book = 44.8% of total book; $1.1B order up to ~78% of it; names under NDA; one line on 'other Hyperscaler orders'"}
  - {id: "CC-FN-17", check: "F7", line: "641-648; 839-853; 865-870; 915-926", classification: "FORWARD-SIGNAL", implication: "Q2 margin carries ~20-25% fibre price rise MD did not foresee in Q1; price/volume split withheld; 'some increase, but not as much'; reversion risk as global capacity adds 40-50%"}
  - {id: "CC-FN-18", check: "F7", line: "589-600; 963-974", classification: "AMBIGUOUS", implication: "germanium for Oct-2028 preform not contracted; export restrictions acknowledged; input risk to backward-integration margin step"}
  - {id: "CC-FN-19", check: "F14", line: "58-70", classification: "NEUTRAL-FACT", implication: "opening arithmetic ties; 25.89% EBITDA and +264 bps tie to Q1 reported Rs445.27 Cr / 23.25%, the other-income-inclusive basis; 'PED margin' 15.51% = PAT/revenue"}
  - {id: "CC-FN-20", check: "F14", line: "750-755; 764-765", classification: "NEUTRAL-FACT", implication: "MD's prior base 26,000 vs Q1 deck 26,665; filed inflow ~Rs4,788 Cr vs spoken 5,500; book-to-bill ~1.9x either way; filing governs"}
  - {id: "CC-FN-21", check: "F14", line: "48; 249-250; 482-483; 665-666; 776-778", classification: "NEUTRAL-FACT", implication: "audio gaps at defence question, FY28 guidance question and margin-source answer; defence-gap question cut off; 'September 13' ASR; re-read against official transcript"}
  - {id: "CC-FN-22", check: "F17", line: "427-438; 1011-1012", classification: "CONFIRMATORY-NEGATIVE", implication: "no receivables ageing/DSO/unbilled number on call, none asked; second consecutive quarter of receivables silence (Q1 memory + Q2 call) = tripwire #4 limb wording; A4 rules against Q2 filing"}
  - {id: "CC-FN-23", check: "F17", line: "513-517; 78", classification: "CONFIRMATORY-NEGATIVE", implication: "export-OFC/hyperscaler revenue withheld second consecutive quarter across results, deck and call; trigger #1 delivery pace untestable"}
  - {id: "CC-FN-24", check: "F17", line: "122; 259-264; 284-285; 396-399", classification: "CONFIRMATORY-NEGATIVE", implication: "fuze approval silent (after 5 quarters of 'couple of months' and Q1 silence); same short-horizon idiom now on foliage radar, stated two ways; MMHG participated not won; BMP-2 silent"}
  - {id: "CC-FN-25", check: "F17", line: "1011-1014", classification: "AMBIGUOUS", implication: "pledge, warrants, Nivetti, S-vs-C PAT gap, HASPL Rs90 Cr, QIP use, tax accrued unpaid Rs123.40 Cr all silent; MD commits to 'immediately reply' by email; route all SILENT/DECLINED questions to IR and date the reply"}
forward_signals: ["CC-FN-02", "CC-FN-03", "CC-FN-04", "CC-FN-05", "CC-FN-06", "CC-FN-07", "CC-FN-09", "CC-FN-10", "CC-FN-12", "CC-FN-17"]
ambiguous: ["CC-FN-01", "CC-FN-08", "CC-FN-11", "CC-FN-13", "CC-FN-14", "CC-FN-15", "CC-FN-16", "CC-FN-18", "CC-FN-25"]
commitments:
  - {commitment: "FY27 revenue growth at least 80% (third raise: 20, 40, 80)", implied_date: "FY27", ref: "lines 104-108 (T003)", status_word: "initiated"}
  - {commitment: "Q3 revenue above Q2", implied_date: "Q3 FY27", ref: "lines 607-611 (T072)", status_word: "initiated"}
  - {commitment: "Q2 not a peak", implied_date: "undated", ref: "lines 88-89 (T003)", status_word: "initiated"}
  - {commitment: "Rs10,000 Cr revenue much before FY29", implied_date: "before FY29", ref: "lines 109-110; 484-485 (T044)", status_word: "initiated"}
  - {commitment: "FY28 better than current", implied_date: "FY28", ref: "lines 487-495 (T044)", status_word: "initiated"}
  - {commitment: "pipeline converting; order book to strengthen", implied_date: "undated", ref: "lines 86-87, 93 (T003)", status_word: "underway"}
  - {commitment: "~Rs1,800 Cr capex OF/OFC/preform (pending)", implied_date: "to Oct-2028", ref: "lines 112-113; 785 (T106)", status_word: "underway"}
  - {commitment: "fibre 28->34->43, cable 34->63 mn fkm", implied_date: "undated on call", ref: "lines 360-362 (T032); 716-717 (T093)", status_word: "underway"}
  - {commitment: "preform plant construction start", implied_date: "soon, undated", ref: "line 377 (T032)", status_word: "initiated"}
  - {commitment: "own preform 600 MT", implied_date: "Oct-2028", ref: "lines 377-378; 584-588 (T067)", status_word: "underway"}
  - {commitment: "preform midterm solution (undisclosed)", implied_date: "Q1 CY2027", ref: "lines 580-583 (T067)", status_word: "initiated"}
  - {commitment: "germanium supply tie-up", implied_date: "before Oct-2028", ref: "lines 593-600; 963-970", status_word: "initiated"}
  - {commitment: "margins only improve, 'no chance' worse", implied_date: "undated", ref: "lines 201-202 (T015); 343 (T028)", status_word: "initiated"}
  - {commitment: "connectivity revenue more than Rs800 Cr", implied_date: "FY27", ref: "lines 369-370; 815-816", status_word: "underway"}
  - {commitment: "connectivity revenue Rs2,000 Cr", implied_date: "FY28", ref: "line 371; 858", status_word: "initiated"}
  - {commitment: "in-DC connectivity products start revenue", implied_date: "Q4 FY27 or early FY28", ref: "lines 366-369 (T032)", status_word: "initiated"}
  - {commitment: "aerospace acquisition completes", implied_date: "within Nov-2026", ref: "lines 124; 273-274; 404", status_word: "underway"}
  - {commitment: "aerospace revenue consolidated", implied_date: "Q3 FY27", ref: "lines 275; 406", status_word: "initiated"}
  - {commitment: "large aerospace export orders", implied_date: "next few months", ref: "lines 276-277 (T018)", status_word: "initiated"}
  - {commitment: "defence revenue ~Rs500 Cr (500-600)", implied_date: "FY27", ref: "lines 129-130; 251; 407-408", status_word: "underway"}
  - {commitment: "defence revenue at least Rs2,000 Cr", implied_date: "FY28", ref: "lines 251-252, 278; 769", status_word: "initiated"}
  - {commitment: "defence revenue ~Rs5,000 Cr", implied_date: "three years (252) / next two years (770)", ref: "lines 252-253; 770", status_word: "initiated"}
  - {commitment: "foliage penetration radar second trial / approval", implied_date: "~2 weeks (early Nov-2026)", ref: "lines 262-263; 397-399", status_word: "underway"}
  - {commitment: "ground surveillance radar export orders", implied_date: "undated", ref: "lines 268-269 (T018)", status_word: "initiated"}
  - {commitment: "ammunition complex construction; revenue in ~2 years", implied_date: "soon; ~late 2028", ref: "lines 134; 281-283", status_word: "initiated"}
  - {commitment: "MMHG 800,000-unit tender (participated)", implied_date: "undated", ref: "lines 284-285 (T018)", status_word: "underway"}
  - {commitment: "Army AMC (year 1 via BSNL) approved and signed", implied_date: "~end-Oct 2026", ref: "lines 418-423 (T036)", status_word: "underway"}
  - {commitment: "BharatNet milestone bills submitted", implied_date: "Q3 FY27", ref: "lines 435-437 (T036)", status_word: "underway"}
  - {commitment: "no repeat of unbilled-expense Turnkey loss; two-quarter ceiling (unreadable)", implied_date: "Q3-Q4 FY27", ref: "lines 438-441 (T036)", status_word: "initiated"}
  - {commitment: "Turnkey segment profit", implied_date: "Q1 FY28", ref: "line 443 (T038)", status_word: "initiated"}
  - {commitment: "restructuring recommendation, board meeting, finalisation", implied_date: "~mid-Nov 2026", ref: "lines 535-545 (T056)", status_word: "underway"}
  - {commitment: "debt reduction starts FY27; substantially lower Mar-27 and Mar-28", implied_date: "31-Mar-2027 / 31-Mar-2028", ref: "lines 551-555 (T058-T060)", status_word: "initiated"}
  - {commitment: "large telco orders", implied_date: "undated", ref: "lines 243-245 (T017)", status_word: "initiated"}
  - {commitment: "IR to immediately reply to emailed queries", implied_date: "immediate", ref: "lines 1011-1014 (T143)", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Machine transcript; filings govern. Three reads matter. First, trigger #6 gets tested within weeks: an E&Y-advised committee is at recommendation, a board meeting is promised in ~10 days, then ~2 weeks to finalise. The scope (EPC only, or the deck's 'verticals') was never stated, and line 547 is cut off. Second, the guide sits below the MD's own words. 'Definitely growth in Q3' with Q4 flat implies ~+93% against an 'at least 80%' floor. But he admits a ~20% fibre price rise he did not foresee. The preform contracts that shield margin run 12-24 months, spot is up ~600%, and own preform covers half the capacity only from Oct-2028. Reading A: floor plus durable mix. Reading B: a price-cycle peak with a cost reset to come. Separating observation: Q3 realisation per fkm and preform contract expiry dates. Third, the pattern: delivered-period splits are withheld (export-OFC, connectivity Q2, price/volume), while defence and connectivity targets rise inside the call and against broker figures from two weeks earlier. Receivables were not discussed at all: the second silent quarter under tripwire #4's wording. A4 rules on firing."
```
