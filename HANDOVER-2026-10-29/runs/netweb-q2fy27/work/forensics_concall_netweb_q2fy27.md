# A3 FORENSIC NOTES: concall, NETWEB (Netweb Technologies India Ltd), Q2 FY27

Source tier: MACHINE TRANSCRIPT (faster-whisper small.en). Speakers are unidentified. Every figure is management tier, unverified, and may be misheard. Line numbers refer to the A1 fulltext (`extracted/netweb-concall-q2fy27-fulltext.md`). Turn numbers (T#) follow the A2 ledger convention: a management answer sits inside the preceding questioner's turn.
Memory inputs (weighed, never evidence): Notion checklist file (`work/notion_checklist_2026-10-26.md`) and Notion context sections [page lines 573,606] and [page lines 642,680] (`work/notion_context_2026-10-26.md`). Every figure taken from them is labelled "(Notion memory)".
Prior-quarter fulltext: not available. No verbatim diff against the Q1 FY27 call was possible; prior-quarter comparisons use Notion memory only.
Arithmetic marked [arithmetic] is computed only from stated figures. No missing number is estimated.

---

## 0. LEDGER RECONCILIATION

- Ledger rows accounted: 261 of 261 structured IDs (R001-R261). Each row was read at its cited fulltext line (fulltext lines 22-780 read in full). Reconciled: 100%.
- A2 count test accepted (participants 8, turns 20, questions 15, numbers 111, mgmt numbers 90, forward 44, dates 27, qualifiers 31).
- Line-cite defects found on reading (no change to any claim; non-material, logged for A1/A2 hygiene):

| Row | Cited line | Where the claim actually sits | Note |
|---|---|---|---|
| R153 NVIDIA | 257 | 411 ("reference architecture of NVIDIA chips"), 663 | cited line has no NVIDIA mention |
| R157 top five / top ten | 219 | 216, 225, 230 | cited line holds "449 new customers" |
| R158 IPO | 505 | 487 ("while we did the IPO"), 690 | cited line has no IPO mention |
| R159 three working areas | 743 | 748 ("three areas we work into") | offset 5 |
| R152 Vera Rubin | 289 | 258, 291, 298, 305 | offset 2 |
| R193 CSP orders | 647 | 649-650 | offset 2-3 |
| R018, R020, R023, R034, R084, R089, R097, R107, R129, R130, R137, R150, R220, R221, R223 | +/-1 | adjacent line (ASR line wrap) | no effect |
| R231 ASR header | 24 | 22 | header line |

---

## 1. TRANSCRIPT NUMBER CONFLICT REGISTER (recorded, not resolved)

Per the task instruction, where a number conflicts with itself in the transcript the conflict is recorded and no value is picked. These are transcript defects or management restatements. They are not governance findings against management unless also listed in the findings table.

| # | Item | Readings (line) | Rows |
|---|---|---|---|
| K1 | Order book, 30-Sep-2026 | "2,629 crore" (68); "26,629 crore" (183); "2600 crores" (344); "2,600 crore" (597); with L1 "around 31-3200 crores" (345) | R018, R048, R062, R099, R063, R257 |
| K2 | Q2 PAT growth YoY | "348.8%" (59); "334.8% year-on-year" (168) | R010, R031 |
| K3 | Year H1 PAT surpassed | "full year financially at 26% of 206 crores" (57); "full-year FI27 pad" (175) | R003, R236 |
| K4 | Last-year working capital | analyst "some 14 days" (376); management "it was 84 days" (378) | R066, R068, R256 |
| K5 | Last-quarter order book | "2500 crores last class quarter" (344); "about 24-2500" (511) | R061, R082 |
| K6 | Pipeline | "approximately 11,152 crores" (120); "more than 10,000 crores" (514); analyst "11,000 CR plus" (471), "around 10,000" (539) | R021, R085, R074, R087 |
| K7 | New customers | "449 new customers in this H1" (219-220); "three and a half year ... close to like 500" (220) | R052, R053 |
| K8 | Growth horizon | "for at least three to, next two to three years" (500) | R080 |
| K9 | PAT sentence fragment | "stood at 0.9%" (166) next to "Rs. 137 crore" (168) and "10.2%" (169) | R029 |
| K10 | HPC / private cloud growth | "1068%, 68.1% year-on-year" (65) | R015 |
| K11 | GPU count | analyst "10,000 CPUs" (581, 583) in a GPU context | R097, R255 |
| K12 | H1 operating EBITDA | see finding A3-17 (Q1 + Q2 do not sum to stated H1) | R025, R027, R036, R038 |

---

## 2. FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R042, R043, R044, R100, R101, R250, R251 | 176-178 (T3); 614-618 (T15) | "we achieved a zero net debt position ... net cash position of Rs. 14 crore ... In addition ... Rs. 403 crore unutilised from the QIP proceeds"; "large part of it is because of the money which was raised in the QLP and not yet utilized. So that cannot be considered as cash." | AMBIGUOUS | The zero net debt is a QIP outcome, not an operating outcome. The call does not say whether the Rs 403 Cr unspent QIP money sits inside the Rs 14 Cr net cash. If it does, net position ex-QIP balance is about minus Rs 389 Cr [arithmetic: 14 - 403]. Q1 net debt was Rs 199.9 Cr (Notion memory). Also Rs 767 Cr used + Rs 403 Cr unused = Rs 1,170 Cr vs Rs 1,200 Cr raised (192, 178, 71): Rs 30 Cr unexplained [arithmetic]. Ask for gross borrowings, the net-cash definition, and the QIP bridge. |
| A3-02 | F6 | R073, R077, R183, R034 | 458-459 (T11); 488-489 (T12); 170 (T3) | "we are targeting to achieve 4,000 crores of revenues is this particular financial"; H1 "Rs.2143 crore" | FORWARD-SIGNAL | New hard FY27 number (Q1 declined one, Notion memory). It implies H2 revenue of about Rs 1,857 Cr [arithmetic: 4,000 - 2,143], about Rs 929 Cr a quarter, 30% below the Q2 print of Rs 1,323 Cr. Management declined to say whether 2H exceeds 1H: "I'll leave that calculation on your end" (457). The analyst premise "the bulk of the strategic order ... is behind us" (447-448) was not contested. Lean bear: H2 steps down from Q2. |
| A3-03 | F6 | R018, R092, R259, R073 | 68 (T2); 547-549 (T13); 458 (T11) | "order books stood at 2,629 crore"; "It depends it is 10 to 16 weeks ... that's the standard with any order" | AMBIGUOUS | A Rs 2,629 Cr book that executes in 10 to 16 weeks would bill by about mid-January 2027, which alone exceeds the implied H2 of Rs 1,857 Cr. Either the 4,000 target is a floor, or part of the book is long-dated (Q1 conversion tenure 18-24 months, Notion memory), or the 10-16 weeks is a per-order norm, not the book. The cycle guide also moved: Q1 16-20 weeks, Q4 FY26 8-12 weeks (Notion memory), now 10-16 weeks, with no explanation. Ask what share of the book is deliverable in H2 FY27. |
| A3-04 | F6 | R079, R093, R184, R186, R190, R189, R246 | 491-493, 508-509 (T12); 562 (T14); 545-546 (T13) | "we have always constantly kept our growth numbers around 30 to 40% CAGR"; "planned to grow by 30%, 30, 40% CAGR"; "I cannot give a guidance on a guidance. My guidance stands where it is." | FORWARD-SIGNAL | The Q4 FY26 band was 35-40% organic CAGR (Notion memory promise log). The floor is now 30%. Management states the band as constant ("always"), so the change is unacknowledged. Three analysts (T12, T13, T14) pressed on growth after FY27; this is a reframe toward a lower floor on a much larger FY27 base. Feed the promise tracker as SOFTENED. |
| A3-05 | F7 | R108, R201, R247, R059, R177, R239, R240, R086, R248 | 728-729 (T18); 333-334, 324-326 (T8); 527 (T12) | "13-14% we have slightly crossed that in this H1 but not to be quoted for the entire year"; "gross margin is very difficult to monitor on a quarter on quarter basis"; "memory prices have gone up by 200% or maybe even more" | FORWARD-SIGNAL | New pre-emptive hedge. H1 operating EBITDA margin is 15.1% (171); management pre-warns that the full year will not hold it, so H2 sits nearer 13-14%. The analyst's gross-margin decline (321) went unrefuted; management moved the frame to EBITDA. With component cost up about 200%, the margin rests on opex leverage from large deals (330-333). No operating leverage shows at 4x revenue (analyst 716-719, unrefuted). Watch H2 against the 12% thesis-broken floor (Notion memory). |
| A3-06 | F6 | R047, R058, R175, R237, R249 | 314-315 (T7); 594-595 (T15); 181-183 (T3); 312 (T7) | "this inventory actually is to the order book only"; "it is a bit intentional that we are preparing for the upcoming orders"; "inventory days stood at 117 days" | AMBIGUOUS | Two answers give two purposes for the same inventory: the existing book (314, 182) and upcoming orders (594-595). The analyst-stated inventory of Rs 1,900 Cr (312) is about 72% of the Rs 2,629 Cr book [arithmetic], and inventory days of 117 exceed the ~110 "going forward" level said in Q1 (Notion memory). Lean bear: part of the stock is bought ahead of orders at memory prices that are up about 200%. That is a price and obsolescence risk. The 25-Oct marker "inventory tied to named Q3/Q4 deliveries" (Notion memory) was answered only with "Yeah, yeah" and no named deliveries. |
| A3-07 | F6 | R152, R172, R173, R174, R216 | 296-299, 306-308 (T7); 259-261 (T7 question) | "very soon, we'll be having first Verarubin system set up in the country"; "start offering this product to be sold to the customers by January. So we'll see if we can pull in the timelines." | AMBIGUOUS | First dated Rubin commitment (Q1 was silent on Rubin, Notion memory). Status: underway ("that all has already started", 296). Not answered: whether the current book already holds Rubin orders (259-261), and NVIDIA OEM terms (thesis-broken #4, Notion memory). January is undated by year; read as January 2027. Track the commercial launch against that date. |
| A3-08 | F6 | R178, R218, R094, R095, R191, R192 | 346-348 (T8); 565-568 (T14) | Analyst: "when can we start expecting some orders from it early 27th?" Answer: "Yeah you are right."; "more than half of it we should be targeting ... that's a five-year program so that will come as slowly as it comes" | AMBIGUOUS | The NSM 2.0 date is analyst-supplied and management only assented. "Early 27" can mean calendar 2027 or FY27. The target of more than half of a five-year outlay carries no outlay figure. Weak commitment; ask for the expected first-order quarter in management's own words. |
| A3-09 | F6 | R018, R019, R062, R063, R021, R160, R083 | 67-69 (T2); 343-345 (T8); 510-512 (T12); 120 (T2) | "2,629 crore, with an additional L1 position of 653 crore, providing strong revenue visibility"; "after billing about 1300 plus crores we are actually above the last quarter's order" | FORWARD-SIGNAL | The book alone rose. Book plus L1 fell: Rs 3,282 Cr now [arithmetic: 2,629 + 653] vs Rs 3,354.9 Cr in Q1 (2,506.9 + 848.0, Notion memory), down about Rs 73 Cr. L1 fell about Rs 195 Cr. Implied Q2 order inflow is about Rs 1,445 Cr [arithmetic: 2,629 - 2,506.9 + 1,323], book-to-bill about 1.09. Pipeline is Rs 11,152 Cr vs about Rs 10,410 Cr in Q1 (Notion memory), up about 7%. Visible coverage is flat. H2 growth depends on pipeline conversion inside the quarter. |
| A3-10 | F6 | R150, R151, R193, R194, R149 | 631-632, 649-651 (T15); 339-340 (T8) | "this is definitely going to result into you know more pipeline addition for us"; "They have an option of placing orders on us and as the orders are placed we will be delivering ... This is not CDAC trying to deploy these many clusters." | AMBIGUOUS | The India AI / CDAC 10,000-GPU RFP reaches Netweb only through empanelled CSPs. Sovereign demand therefore lands as CSP or neocloud orders, not as a direct government order. Checklist #9 ("new sovereign AI order >= Rs 500 Cr", Notion memory) may never fire in its written form even if the demand arrives. Neocloud names are confirmed customers ("all the names which you mentioned all are customers", 339), which adds a CSP concentration angle. Ask what share of pipeline is CSP-routed India AI demand. |
| A3-11 | F7 | R098, R249 | 587-592, 602 (T15) | "we haven't seen any substitution because if you see there is a significant improvement in the receivable days"; "So there is no, as such on these cash flows"; "there is no any pressure on that" | AMBIGUOUS | The analyst asked about cash blocked in orders. Management gave no CFO figure and answered with receivable days only. Notion memory records filed H1 CFO of minus Rs 639.1 Cr and an inventory build from Rs 805 Cr to Rs 1,931 Cr. If that memory holds, "no pressure" does not match the filed cash flow. The ASR word "substitution" is uncertain. Lean bear: treat as a reassurance that conflicts with the filing until reconciled. |
| A3-12 | F7 | R244, R245, R198, R199, R252 | 340-342 (T8); 553-554 (T14); 705-706, 710-712 (T18); 457 (T11) | "we don't specifically state the numbers of the orders or the quantities of particular customers"; "unfortunately we don't share the break of the order book"; "at this point of time we are not willing to disclose more"; "I don't think we want to speculate" | AMBIGUOUS | Refusals cluster on the same open thesis items as Q1 (funnel or order-book split, physical AI / quantum spend; Notion memory lists both as Q1 refusals). Second consecutive quarter for each. The AI order-mix answer (T10, 421-428) is largely lost in an ASR gap (R252), and the segment-driver question (461-462) went unanswered ("I think you are not audible", 463). Carry forward. |
| A3-13 | F7 | R052, R053, R054, R055, R056, R157, R243 | 218, 236-239 (T6); 219-223 (T6) | "25 to 30 customers probably have churned over the last two, three years to take the top five, top 10 place. Hence, while in statistics, it looks like a very heavy concentration activity is not." | AMBIGUOUS | No concentration figure on the call. Management pointed to the deck (218), which per Notion memory shows top 10 at 85.2% and top 5 at 76.5% (checklist #6 red on headline). The churn defence carries a hedge ("probably") and no evidence. The new-customer figures conflict (K7). The operator decides whether this counts as the "repeat evasion" that turns checklist #6 RED (Notion memory, 21-Oct note). The answer is a reframe with engagement, not a refusal. |
| A3-14 | F7 | none (turn text) | 389-390 (T10); 734 (T18); 738 (T18) | "there will be other comparable or competing players who will also be able to offer the platform"; "none of our competitors are even close to what we are"; "we have no idea about that" | AMBIGUOUS | Three statements on competition do not agree. "Not even close" is a moat claim. "We have no idea" about Indian competitors weakens that claim. Low priority. Ask for named competitors in the bids lost from the 60% strike rate (506, 513-514). |
| A3-15 | F7 | R049, R050, R238 | 189-191 (T3) | "return on equity and return on capital employed stood at 31.4% and 38.6% respectively. These ratios reflect the impact of QIP proceeds on our capital base." | NEUTRAL-FACT | Pillar-relevant fact, flagged for A4 per OR-30 (no pillar change on concall narrative). ROCE fell from 48.2% on the Q1 call (Notion memory) to 38.6%, with QIP equity given as the cause. FTTCP ROCE verdict stays the authority. |
| A3-16 | F10 | R197, R229, R103, R104, R020 | 690-692 (T17); 674-675 (T17); 70-71 (T2) | "the trance which we had given at the time of before the IPO they got vested fully last year itself ... whenever the new ESOP schemes are being distributed then it will have an impact in this area" | FORWARD-SIGNAL | ESOP cost is near zero now because the pre-IPO grant has fully vested. New schemes are expected, so both ESOP expense and share dilution return. Employee cost has risen for five to six quarters (analyst, 674-675) and headcount is up 120+ YoY (684). QIP of Rs 1,200 Cr closed (71); share count change not stated on the call (4.40% dilution, Notion memory). A4 runs the ESOP cross-check against Notion (285,000-share issuance, Q1 question 16). |
| A3-17 | F14 | R025, R027, R028, R036, R038, R024, R032, R030, R040 | 165-166 (T3); 171 (T3); 164, 168 (T3) | "Operating EBITDA for the quarter stood at Rs 197 crore increasing ... 63.7% quarter on quarter"; "Operating IBDAS stood at Rs.323 crore ... with a margin of 15.1%" | AMBIGUOUS | Q1 EBITDA implied by the QoQ rate is about Rs 120.3 Cr [arithmetic: 197 / 1.637]. Q1 + Q2 is about Rs 317.3 Cr vs the stated H1 of Rs 323 Cr, a gap of about Rs 5.7 Cr. An H1 margin of 15.1% cannot sit above both quarters (Q2 14.9%; Q1 implied 14.7% [arithmetic: 120.3 / 819.7], also 14.7% per Notion memory). Revenue ties (Q1 implied 819.7 + 1,323 = 2,142.7 vs 2,143) and PAT ties (85.5 + 137 = 222.5 vs 222). Only EBITDA fails. Causes: ASR misread, a different H1 definition, or a restated Q1 (FIFO to moving-weighted-average, Q1 question 12, Notion memory). Reconcile against the filed results. |
| A3-18 | F14 | R013, R014, R016, R017, R015, R005 | 63-66 (T2) | "contributing 773 crores or 58.4% of revenue"; "HPC and private cloud ... contributing 248 crore and 245 crore respectively" | NEUTRAL-FACT | Segments sum to Rs 1,266 Cr vs revenue of Rs 1,323 Cr. Rs 57 Cr (4.3%) is unallocated on the call [arithmetic]. Software/spares at 2.65% of revenue (about Rs 35 Cr, Notion memory) covers part of it. The segment growth rates are garbled (K10). Minor; ask for a segment table that ties. |
| A3-19 | F15 | R131, R165, R166, R057, R170, R171, R179, R258 | 147-149 (T2); 265-270, 280-288 (T7); 366-369 (T9) | "our board has also approved the establishment of a wholly owned subsidiary of Netweb in Taiwan for advancing our R&D efforts"; "This is the only purpose of that subsidiary in Taiwan."; "we don't intend to become an ODM" | FORWARD-SIGNAL | New entity in the consolidation perimeter. No prior entity list exists (no prior run), so this is logged as an addition. Status: initiated (board approved). No capital outlay, headcount, opex budget or start date was given. Forward cost: an overseas R&D cost centre with hiring ("to hire more manpower ... locally in Taiwan", 281-282). The cost lands in opex against the 13-14% margin band. Track ODI filings, transfer pricing, and first-year spend. The ODM denial is a strategy commitment to log. |
| A3-20 | F17 | R098 (topic), Notion checklist #1, thesis-broken #1 | 587-602 (T15) | "So all our debtors that is being reported are all very healthy and top notch" (no CFO figure given) | CONFIRMATORY-NEGATIVE | No CFO or CFO/PAT figure for the second consecutive call (Q1 call also gave none, Notion memory). This is the master cash gate. Per Notion memory, filed H1 CFO is minus Rs 639.1 Cr, which fires thesis-broken #1 if H1 counts. Sustained silence on a deteriorating metric. |
| A3-21 | F17 | R073 (topic), Notion checklist #3, thesis-broken #3 | 447-448 (T11 analyst); 455-459 (T11 answer) | Analyst: "now that the bulk of the strategic order of around the middle billion is behind us"; Answer: "if you see the order book, that will itself give you an indication" | AMBIGUOUS | Management did not state strategic-order progress against the Rs 1,734 Cr by H2 FY27 milestone or the remaining balance. Second consecutive call with the milestone unaddressed (Notion memory). Q1 question 8 (per-quarter schedule for about Rs 1,170 Cr remaining) is unanswered. The analyst premise, not contested, implies the order is mostly executed. That would support thesis-broken #3 not firing, but it is unconfirmed. |
| A3-22 | F17 | none (topic absent), Notion checklist #5 | 403-404 (T10, only software-adjacent line) | "and the layer above that, which includes our cloud stack also" | CONFIRMATORY-NEGATIVE | Skylus.ai / Velox software share was not mentioned. Third consecutive silent disclosure (Q1 recorded "silent two disclosures running", Notion memory). Notion memory puts software/spares at 2.65% of revenue, below the 4% red line on checklist #5. Sustained silence on a metric that is below its red line. |

---

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | One ZERO_STANDING row (R042 zero net debt). It is a QIP outcome. The net-cash definition vs Rs 403 Cr unused QIP is not stated (A3-01). |
| F2 Standalone vs consolidated | N.A. | Concall; no standalone or consolidated statements read out. |
| F3 Shell-entity detection | N.A. | Concall; no cost-line tables. Taiwan WOS is not yet operating (handled under F15). |
| F4 Unaudited contribution ratio | N.A. | Concall; no auditor Other Matters paragraph. |
| F5 Going concern / EoM tracking | N.A. | Concall; no EoM paragraph; no prior-quarter fulltext. |
| F6 Forward-commitment mining | FINDING | 9 findings (A3-02, 03, 04, 06, 07, 08, 09, 10, and register below). New hard FY27 target; growth floor lowered; Rubin date; NSM assent; book plus L1 down. |
| F7 Hedge phrase mining | FINDING | New margin hedge "not to be quoted for the entire year"; cash reassurance with no figure; repeat refusals; concentration reframe (A3-05, 11, 12, 13, 14, 15). |
| F8 Tax forensics | N.A. | Concall; no tax line, ETR or deferred-tax figure stated. |
| F9 OCI forensics | N.A. | Concall; no OCI figures. |
| F10 Share count and dilution | FINDING | New ESOP schemes expected to add cost and dilution; QIP closed (A3-16). No paid-up or EPS figures on the call. |
| F11 Reserves and net worth tie-out | N.A. | Concall; no net worth stated. The deck vs filing cash difference is logged under F1 (A3-01). |
| F12 Segment forensics | N.A. | Concall gives segment revenue only, no segment assets or liabilities. The revenue tie gap is logged under F14 (A3-18). |
| F13 Board outcome beyond results | PASS | Only board outcome mentioned is the Taiwan WOS approval (147), logged under F15. No AR, AGM, director-term or new enabling resolution on the call. |
| F14 Drafting inconsistencies | FINDING | Applied to management-stated figures. Q1 + Q2 EBITDA does not equal stated H1 EBITDA, and the H1 margin sits above both quarters (A3-17). Segment sum gap of Rs 57 Cr (A3-18). ASR causes are possible; conflict register K1-K12 lists them. |
| F15 Entity list diffs | FINDING | New wholly owned Taiwan subsidiary (A3-19). |
| F16 Presentation dropped/reframed | N.A. | Presentation-specific; deck not in this document scope. Guidance changes vs Q1 are carried under F6 via Notion memory. |
| F17 Silence audit | FINDING | CFO silent 2 calls; strategic milestone silent 2 calls; software share silent 3 disclosures; full table below (A3-20, 21, 22). |

---

## 4. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Line / turn ref | Status word |
|---|---|---|---|---|
| C01 | FY27 revenue "targeting to achieve 4,000 crores" | 31-Mar-2027 | 458-459 (T11); 489 (T12) | initiated (first hard number; Q1 declined one, Notion memory) |
| C02 | Growth "30 to 40% CAGR" for "next two to three years" | FY28-FY30 | 491-500, 508-509 (T12); 562 (T14) | maintained in wording; floor down from 35% (Q4 FY26, Notion memory) |
| C03 | Operating EBITDA margin "around 14%" / 13-14%; H1 level "not to be quoted for the entire year" | FY27 | 333-334 (T8); 728-729 (T18) | maintained (band); H2 step-down pre-warned |
| C04 | "we will maintain our IBITDA and PAT" | ongoing | 723-724 (T18) | maintained |
| C05 | CCC "will operate between 90 to 110 days ... even going forward" | FY27 onward | 374-375, 381 (T9) | maintained (94 days at Sep; 84 days FY26, 378) |
| C06 | Order book execution "10 to 16 weeks" | per order | 547-549 (T13) | changed (Q1 16-20 weeks, Notion memory) |
| C07 | Pipeline conversion "around 60%" | gradual | 506, 513-514 (T12) | maintained (tenure not restated; Q1 18-24 months, Notion memory) |
| C08 | Vera Rubin: first system set up "very soon"; offered to customers "by January"; may "pull in the timelines" | January 2027 (year implied) | 296-299, 306-308 (T7) | underway ("has already started", 296) |
| C09 | Taiwan wholly owned subsidiary, R&D only, local hiring | not stated | 147-149 (T2); 265-288 (T7); 368-372 (T9) | initiated (board approved) |
| C10 | No ODM model; no laptop or client devices | standing | 366-367 (T9); 669 (T16) | standing exclusion |
| C11 | NSM 2.0: first orders "early 27" (analyst date, management assent); target "more than half" of the outlay over a five-year program | early 2027 or FY27 (ambiguous) | 346-348 (T8); 565-570 (T14) | initiated (assent only) |
| C12 | India AI / CDAC RFP "definitely going to result into ... more pipeline addition" | not stated | 631-632, 649-650 (T15) | initiated |
| C13 | Inventory "will be churning from this inventory" into the order book | Q3-Q4 FY27 (analyst-framed, 313) | 314-315 (T7) | underway |
| C14 | New ESOP schemes "will have an impact" on cost | not stated | 691-692 (T17) | initiated (intent) |
| C15 | Physical AI and quantum: "initial development stage"; numbers when ready | not stated | 137 (T2); 704, 710-712 (T18) | underway (R&D); no milestone |
| C16 | Product roadmap "will serve at least for two to three years" | FY27-FY29 | 391-392 (T10) | standing |
| C17 | QIP: Rs 767 Cr utilised, Rs 403 Cr unutilised as of Sep 2026 | balance to deploy, date not stated | 178, 192-193 (T3) | underway (Rs 30 Cr of Rs 1,200 Cr not bridged, A3-01) |

---

## 5. WHAT WAS NOT DISCUSSED (F17 SILENCE AUDIT)

Consecutive-quarter counts use the Notion memory record of the Q1 FY27 call. Where the Q1 status is not in the sections supplied, the count says so.

| Item (source) | Addressed on this call? | Consecutive quarters of silence | Note |
|---|---|---|---|
| Checklist #1 CFO/PAT; thesis-broken #1 | NO (no CFO figure; receivable-days answer only, 587-592) | 2 (Q1 "No CFO number on call", Notion memory) | A3-20. CONFIRMATORY-NEGATIVE. |
| Checklist #2 CCC | YES (94 days; 90-110 band) | 0 | |
| Checklist #3 Blackwell / strategic order Rs 1,734 Cr by H2 FY27; thesis-broken #3 | NO (analyst premise only, 447-448) | 2 (Q1 "milestone unaddressed", Notion memory) | A3-21 |
| Checklist #4 EBITDA margin; thesis-broken #2 | YES (14.9% Q2; caveat for full year) | 0 | A3-05 |
| Checklist #5 Skylus.ai / Velox software share | NO | 3 (Q1 "silent two disclosures running", Notion memory) | A3-22. CONFIRMATORY-NEGATIVE. |
| Checklist #6 customer concentration | PARTIAL (reframe, no figure, 218-239) | 0 for topic; figure withheld on the call 2 calls running (Q1 Q6 "evaded again", Notion memory) | A3-13; operator rules on the repeat-evasion test |
| Checklist #7 promoter stake sales; thesis-broken #5 | NO | 2 (Q1 "not discussed", Notion memory) | Exchange-data item; call silence carries little weight |
| Checklist #8 inventory audit remediation | NO | 1 (Q1 status NOT FOUND in the sections supplied) | AR item |
| Checklist #9 new strategic AI order >= Rs 500 Cr | NO new named order; CSP-routed RFP discussed (620-651) | 1 (Q1 status NOT FOUND in the sections supplied) | A3-10 |
| Checklist #10 Chandelier | N.A. for a call | n/a | Price indicator |
| Thesis-broken #4 NVIDIA OEM terms / Rubin | PARTIAL (Rubin launch by January; NVIDIA terms not stated) | Rubin: 0 (silent in Q1, now addressed); terms: 2 | A3-07 |
| Q1 Q1: H1 CFO and CCC components | PARTIAL (CCC 94, receivable 62, inventory 117; no CFO, no payable days) | CFO 2 | Payable days implied about 85 [arithmetic: 62 + 117 - 94] |
| Q1 Q2: why execution cycle doubled | PARTIAL (now 10-16 weeks, no explanation) | 1 | A3-03 |
| Q1 Q3: conversion tenure drift | NO (60% ratio restated, tenure not) | 1 | |
| Q1 Q4: Rs 1,200 Cr enabling resolution | YES (overtaken: QIP closed, 70-71; utilisation 192) | 0 | |
| Q1 Q5: AI mix durability | NO (AI 58.4% realised, 63; order-book mix answer lost in ASR gap, 427) | 1 | |
| Q1 Q6: top-customer shares | NO figure (A3-13) | 2 | |
| Q1 Q7: "growing at 90%" / PBT-to-EBITDA bridge | NO | 2 | Related EBITDA tie-out defect A3-17 |
| Q1 Q8: strategic-order schedule | NO | 2 | A3-21 |
| Q1 Q9: memory prices and WC intensity | PARTIAL (memory +200%, 527; inventory intentional) | 0 | A3-05, A3-06 |
| Q1 Q10: physical AI / quantum spend | NO (refused, 705, 712) | 2 | A3-12 |
| Q1 Q11: like-for-like pipeline split | NO (refused, 553-554) | 2 | A3-12 |
| Q1 Q12: FIFO to moving-weighted-average restatement | NO | 2 | Possible link to A3-17 |
| Q1 Q13: ST borrowing balance and rate | PARTIAL (zero net debt; gross borrowings not stated) | gross borrowings 2 | A3-01 |
| Q1 Q14: software share | NO | 3 (see checklist #5) | A3-22 |
| Q1 Q15: NVIDIA OEM terms and Rubin | PARTIAL | terms 2 | A3-07 |
| Q1 Q16: 285,000-share issuance, deferred tax / ETR, Labour Codes, Netweb Foundation | NO | 2 | A3-16 links the ESOP part |
| 25-Oct marker: finance cost | NO | 1 | Net cash claim does not address interest cost |
| 25-Oct marker: H2 CFO path vs Rs 887-922 Cr hurdle | NO | 1 | A3-20 |
| 25-Oct marker: inventory tied to named Q3/Q4 deliveries | PARTIAL ("Yeah", no names, 314) | 0 | A3-06 |
| 25-Oct marker: Taiwan WOS | YES (purpose, ownership; no capital or date) | 0 | A3-19 |
| Unanswered questioner | R133 (211-213) did not come on line | n/a | Not a management silence |

---

## 6. FLAGS FOR A4 (management questions)

FORWARD-SIGNAL: A3-02, A3-04, A3-05, A3-09, A3-16, A3-19.
AMBIGUOUS: A3-01, A3-03, A3-06, A3-07, A3-08, A3-10, A3-11, A3-12, A3-13, A3-14, A3-17, A3-21.
CONFIRMATORY-NEGATIVE: A3-20, A3-22.
NEUTRAL-FACT: A3-15, A3-18.
Pillar-relevant facts (OR-30, flag only): ROCE 38.6% / ROE 31.4% (A3-15); CFO silence vs Notion-memory filed CFO (A3-20); margin caveat (A3-05).

---

```yaml
stage: A3-forensics
company: "NETWEB"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/forensics_concall_netweb_q2fy27.md"
ledger_reconciled_pct: 100
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
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-01", check: "F1", line: "176-178; 614-618", classification: "AMBIGUOUS", implication: "Zero net debt is a QIP outcome; unclear if Rs 403 Cr unused QIP sits inside Rs 14 Cr net cash (if so, about -389 Cr ex-QIP); Rs 30 Cr of the 1,200 Cr QIP not bridged"}
  - {id: "A3-02", check: "F6", line: "458-459; 489; 170", classification: "FORWARD-SIGNAL", implication: "FY27 target Rs 4,000 Cr implies H2 about Rs 1,857 Cr, about Rs 929 Cr a quarter, 30% below Q2 Rs 1,323 Cr; 2H vs 1H answer declined"}
  - {id: "A3-03", check: "F6", line: "68; 547-549", classification: "AMBIGUOUS", implication: "Rs 2,629 Cr book at 10-16 weeks exceeds implied H2; either target is a floor or part of book is long-dated; cycle guide moved from 16-20 weeks (Q1, Notion memory) without explanation"}
  - {id: "A3-04", check: "F6", line: "491-493; 562; 545-546", classification: "FORWARD-SIGNAL", implication: "Growth band floor lowered from 35% (Q4 FY26, Notion memory) to 30%, presented as unchanged"}
  - {id: "A3-05", check: "F7", line: "728-729; 324-334; 527", classification: "FORWARD-SIGNAL", implication: "New hedge: H1 15.1% margin not to be quoted for full year; gross margin decline unrefuted; memory +200%; H2 margin step-down signalled"}
  - {id: "A3-06", check: "F6", line: "314-315; 594-595; 181-183; 312", classification: "AMBIGUOUS", implication: "Inventory said to serve both the existing book and upcoming orders; about 72% of book; 117 days above ~110 guide; procurement-ahead-of-orders risk at high memory prices"}
  - {id: "A3-07", check: "F6", line: "296-299; 306-308; 259-261", classification: "AMBIGUOUS", implication: "Rubin offered to customers by January (2027 implied), underway; book inclusion of Rubin and NVIDIA OEM terms not answered"}
  - {id: "A3-08", check: "F6", line: "346-348; 565-568", classification: "AMBIGUOUS", implication: "NSM 2.0 first-order date is analyst-supplied with management assent; 'early 27' ambiguous; >half of outlay target with no outlay figure"}
  - {id: "A3-09", check: "F6", line: "67-69; 343-345; 510-512; 120", classification: "FORWARD-SIGNAL", implication: "Book plus L1 Rs 3,282 Cr vs Rs 3,354.9 Cr Q1 (Notion memory), down about 73 Cr; L1 down about 195 Cr; implied inflow about 1,445 Cr, book-to-bill about 1.09; pipeline up about 7%"}
  - {id: "A3-10", check: "F6", line: "631-632; 649-651; 339-340", classification: "AMBIGUOUS", implication: "India AI RFP reaches Netweb only via CSPs; checklist #9 direct sovereign order may never fire as written; CSP/neocloud concentration angle"}
  - {id: "A3-11", check: "F7", line: "587-592; 602", classification: "AMBIGUOUS", implication: "'no pressure' on cash flows with no CFO figure; conflicts with filed H1 CFO of -Rs 639.1 Cr per Notion memory"}
  - {id: "A3-12", check: "F7", line: "340-342; 553-554; 705-712; 457", classification: "AMBIGUOUS", implication: "Repeat refusals on order-book split and physical AI / quantum spend, second consecutive call; AI order-mix answer lost to ASR gap"}
  - {id: "A3-13", check: "F7", line: "218; 236-239; 219-223", classification: "AMBIGUOUS", implication: "Concentration reframed as churn with 'probably'; no figure on call; deck top 10 85.2% (Notion memory); operator rules on repeat-evasion test"}
  - {id: "A3-14", check: "F7", line: "389-390; 734; 738", classification: "AMBIGUOUS", implication: "Competition statements disagree ('not even close' vs 'no idea'); moat claim unverified"}
  - {id: "A3-15", check: "F7", line: "189-191", classification: "NEUTRAL-FACT", implication: "ROCE 38.6% vs 48.2% Q1 call (Notion memory), QIP equity cited; pillar fact flagged per OR-30"}
  - {id: "A3-16", check: "F10", line: "690-692; 674-675; 70-71", classification: "FORWARD-SIGNAL", implication: "Pre-IPO ESOPs fully vested; new schemes expected to add ESOP cost and dilution; QIP closed"}
  - {id: "A3-17", check: "F14", line: "164-166; 171", classification: "AMBIGUOUS", implication: "Q1 implied EBITDA about 120.3 + Q2 197 = about 317.3 vs stated H1 323; H1 margin 15.1% above both quarters; revenue and PAT tie; ASR, definition, or Q1 restatement"}
  - {id: "A3-18", check: "F14", line: "63-66", classification: "NEUTRAL-FACT", implication: "Segments sum Rs 1,266 Cr vs Rs 1,323 Cr revenue; Rs 57 Cr (4.3%) unallocated on the call"}
  - {id: "A3-19", check: "F15", line: "147-149; 265-288; 366-369", classification: "FORWARD-SIGNAL", implication: "New wholly owned Taiwan R&D subsidiary; no capital, headcount, budget or date; overseas opex against 13-14% band; ODM denied"}
  - {id: "A3-20", check: "F17", line: "587-602", classification: "CONFIRMATORY-NEGATIVE", implication: "No CFO figure for second consecutive call while filed H1 CFO is negative per Notion memory; thesis-broken #1 exposure"}
  - {id: "A3-21", check: "F17", line: "447-448; 455-459", classification: "AMBIGUOUS", implication: "Strategic-order Rs 1,734 Cr H2 milestone unaddressed for second call; analyst premise 'bulk behind us' not contested"}
  - {id: "A3-22", check: "F17", line: "403-404", classification: "CONFIRMATORY-NEGATIVE", implication: "Software share silent for third consecutive disclosure; 2.65% per Notion memory is below the 4% red line"}
forward_signals: ["A3-02", "A3-04", "A3-05", "A3-09", "A3-16", "A3-19"]
ambiguous: ["A3-01", "A3-03", "A3-06", "A3-07", "A3-08", "A3-10", "A3-11", "A3-12", "A3-13", "A3-14", "A3-17", "A3-21"]
commitments:
  - {commitment: "FY27 revenue targeting Rs 4,000 Cr", implied_date: "2027-03-31", ref: "lines 458-459, 489", status_word: "initiated"}
  - {commitment: "Growth 30-40% CAGR next two to three years", implied_date: "FY28-FY30", ref: "lines 491-500, 562", status_word: "maintained (floor down from 35%)"}
  - {commitment: "Operating EBITDA margin around 14% / 13-14%; H1 level not for full year", implied_date: "FY27", ref: "lines 333-334, 728-729", status_word: "maintained"}
  - {commitment: "CCC 90-110 days going forward", implied_date: "FY27 onward", ref: "lines 374-375, 381", status_word: "maintained"}
  - {commitment: "Order execution 10-16 weeks", implied_date: "per order", ref: "lines 547-549", status_word: "changed (Q1 16-20 weeks)"}
  - {commitment: "Pipeline conversion around 60%", implied_date: "gradual", ref: "lines 506, 513-514", status_word: "maintained"}
  - {commitment: "Vera Rubin offered to customers by January; first system set up very soon", implied_date: "2027-01 (year implied)", ref: "lines 296-299, 306-308", status_word: "underway"}
  - {commitment: "Taiwan wholly owned R&D subsidiary with local hiring", implied_date: "not stated", ref: "lines 147-149, 265-288", status_word: "initiated"}
  - {commitment: "No ODM model; no laptop or client devices", implied_date: "standing", ref: "lines 366-367, 669", status_word: "standing"}
  - {commitment: "NSM 2.0 first orders early 27 (analyst date, assent); target more than half of outlay", implied_date: "early 2027 or FY27 (ambiguous)", ref: "lines 346-348, 565-570", status_word: "initiated"}
  - {commitment: "India AI / CDAC RFP adds pipeline via CSPs", implied_date: "not stated", ref: "lines 631-632, 649-650", status_word: "initiated"}
  - {commitment: "Inventory to churn into order book", implied_date: "Q3-Q4 FY27 (analyst-framed)", ref: "lines 312-315", status_word: "underway"}
  - {commitment: "New ESOP schemes will add cost", implied_date: "not stated", ref: "lines 691-692", status_word: "initiated"}
  - {commitment: "Physical AI and quantum numbers when ready", implied_date: "not stated", ref: "lines 704, 710-712", status_word: "underway"}
  - {commitment: "Product roadmap covers two to three years", implied_date: "FY27-FY29", ref: "lines 391-392", status_word: "standing"}
  - {commitment: "QIP Rs 767 Cr utilised, Rs 403 Cr unutilised", implied_date: "balance date not stated", ref: "lines 178, 192-193", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "The call's centre of gravity is H2. The new Rs 4,000 Cr FY27 target implies H2 about Rs 1,857 Cr, 30% below the Q2 run-rate. Management pre-warned that the 15.1% H1 margin will not hold for the year. Book plus L1 fell QoQ while the book alone rose. Read together, these say Q2 was a peak quarter driven by the strategic order, not a new base. The tension A4 must press: a Rs 2,629 Cr book at 10-16 weeks should bill more than the implied H2. Either the target is a floor or the book is long-dated. Cash is the second axis. Zero net debt came from the QIP. No CFO figure was given for the second call running, and 'no pressure' conflicts with the filed negative H1 CFO in Notion memory. Inventory was described two ways (existing book vs upcoming orders) at memory prices up about 200%. All figures are ASR; the H1 EBITDA tie-out failure (A3-17) may be a transcript artefact and needs the filed numbers. Order book readings 2,629 / 26,629 / 2,600 are recorded, not resolved (register K1)."
```
