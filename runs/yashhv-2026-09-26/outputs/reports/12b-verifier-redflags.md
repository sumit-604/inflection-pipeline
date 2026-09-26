# STAGE 12 VERIFIER B: CONCALL RED FLAGS — Yash Highvoltage Ltd (YASHHV)

Run date: 2026-09-26. Phase 1. Model: claude-opus-5-5. Fresh context.

Inputs read: 4 main-company transcripts (Call-A 11-Jan-2025 Tiger Assets investor meet; Call-1
28-May-2025 FY25; Call-2 15-Oct-2025 H1FY26; Call-3 14-May-2026 FY26), read in full. 12 peer
transcripts (QPOWER x4, POWERINDIA x4, VILAS x4), read by targeted full-text search on bushing,
Sukrut, Yash, Chinese/China, overcapacity, price war, slowdown, insulator, localisation, LD,
affordability, then read in context around every hit. Audited: B05 (05-concall.md, labelled
RUN 2 CORRECTED) and B06 (06-peers.md). No other RUN output was opened.

Anchor convention. Main-company calls: (Call, speaker, PDF page from the `[page N]` marker).
Peer calls: (peer file, speaker, line number in the pre-extracted .txt), because the peer
extracts are long and the line is the more exact locator.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from raw transcripts, before reading B05/B06)

Severity is graded on the common scale. Status column is filled after the comparison in Part 2.

| # | Item | Anchor | Sev | Status |
|---|---|---|---|---|
| I1 | Greenfield RIP plant slips each call and is called "on track" each call. Call-A: "RIP by March 2026... Facility will be ready for commissioning". Call-1: "by the middle of next year... up and running", "By next year this time... fully operational". Call-2: "on the dot... We don't see any delay", trial Feb-Mar 2026. Call-3: "Trial production remains on track", then trial "by end of Q2 FY27" and indigenous RIP revenue "towards the end of this year". | Call-A Nirav Patel p10; Call-1 Keyur Shah p4, p10; Call-2 Keyur Shah p10; Call-3 Keyur Shah p5, p9 | MAJOR | CAUGHT |
| I2 | Historical CAGR restated upward while forward guide ratchets. Call-A "close to 25% or more"; Call-1 "historically between 25 to 35%"; Call-2 "minimum CAGR of 35%, as we have been maintaining historically"; Call-3 "38% to 40% CAGR last five to six years", forward 40-42%. Call-2 also moves the guide to 40% in-call after Deepak Poddar shows 35% cannot fill capacity in 3 years. | Call-A Nirav Patel p8; Call-1 Keyur Shah p3, p29; Call-2 Keyur Shah p5, p16; Call-3 Keyur Shah p8 | MAJOR | CAUGHT |
| I3 | FY27 guide contradicts itself inside Call-3: 40-45% growth (to Disha, confirmed to Rushin Shah) vs Rs360-400cr invoicing (to Mehul Panjuani). On Rs235.1cr FY26 that is Rs329-341cr vs Rs360-400cr. | Call-3 Keyur Shah p10, p16, p20; FY26 base Darshan Thakkar p6-7 | MAJOR | CAUGHT |
| I4 | Capex drift and funding reversal. Greenfield Rs90cr / Rs85-90cr (Call-1), "INR100 crores plus" (Call-2), analyst-cited Rs153cr with only "close to INR80 crores is already done" confirmed (Call-3). Call-1 "we don't see any further CapEx for two or three years... till 2030"; Call-3 equity approval up to Rs150cr, Rs100-110cr expected, "we are compelled to invest there also". | Call-1 Keyur Shah p3, p23-24; Call-2 Keyur Shah p16; Call-3 Keyur Shah p11, p27 | MAJOR | CAUGHT |
| I5 | RIP core technology source told three ways, including one in-call conflict. Call-A: core tech from an unnamed "other technology consultant... also a Swiss group". Call-2: "We have developed in-house capability". Call-3 to Naman Parmar: "That contract has already got over... the technology agreement"; Call-3 to Rushin Shah on the same page: "the contract is ongoing with them and we have been able to successfully transfer the knowledge... contract is continuous ongoing". | Call-A Nirav Patel p9; Call-2 Keyur Shah p18; Call-3 Keyur Shah p15 (both answers) | MAJOR | PARTIALLY CAUGHT |
| I6 | MGC supply horizon shortened. Call-1: MGC exclusive to Yash in India for "At least three more years" (to about 2028). Call-3: supply "till mid of '27", contract "already got over". | Call-1 Keyur Shah p20; Call-3 Keyur Shah p15 | MINOR | PARTIALLY CAUGHT |
| I7 | Related-party premise dodged. Keshav: MGC "was earlier a related party and held by the same promoter"; answer covers only contracts and non-compete, not ownership. | Call-2 Keshav / Keyur Shah p14 | MAJOR | CAUGHT |
| I8 | Unit-economics disclosure regresses. Call-A CFO gives segment EBITDA (HC 45%, RIP 20-22%, OIP 13-15%) and MSR by line. Later calls refuse: margin bps "reserve that answer" (Call-1); price hike "won't be able to tell" (Call-3); Sukrut EBITDA "too early" (Call-3); retrofit margin "won't be able to give you an exact bifurcation" (Call-3); realisation "would not be able to generalize" (Call-3). Repeated across 2+ calls. | Call-A Sumit Poddar p6; Call-1 Keyur Shah p24; Call-3 Keyur Shah p13, p21, p26, p27 | MAJOR | PARTIALLY CAUGHT |
| I9 | FY27 margin walked back. Call-2: "maintain or slightly increase for one and a half or two years", then "steep increase" / "considerable margin expansion from '27-'28". Call-3: FY27 "around 24%, 25%" against FY26 25.7%, "we don't let it fall down further", and FY28 becomes "gradual increase". | Call-2 Keyur Shah p11; Call-3 Keyur Shah p8-9; FY26 25.7% Darshan Thakkar p7 | MAJOR | PARTIALLY CAUGHT |
| I10 | Two margin explanations in one call. To Disha: cyclic purchasing, "Not, not any very specific reason". To Rohan Khera: scale, "extract better prices from the customer" in shortage, supplier terms, hedging, mix. | Call-3 Keyur Shah p9-10, p18-19 | MAJOR | CAUGHT |
| I11 | Customer concentration self-corrected in one breath: "Around 70%. No, if product mix based, then it is 40 to 45%." Never revisited. | Call-A Nirav Patel p7 | MAJOR | CAUGHT |
| I12 | Order-book number withheld until pressed: "I cannot reveal the numbers" (Call-A); qualitative only (Call-1); "I don't know whether it is allowed... Yes, it is more than INR300 crores" (Call-2). | Call-A p10; Call-1 p16; Call-2 Keyur Shah p18 | MINOR | CAUGHT |
| I13 | FY24 to FY25 units flat (5,800 to 5,752) under 38% revenue growth; answer addresses FY25 to FY26 instead. | Call-3 Naman Parmar / Keyur Shah p14 | MINOR | CAUGHT |
| I14 | RIP scarcity easing, told by a customer channel. Vineet Khatri relays a transformer maker: "RIP's capacities in the domestic market has come up, but the OIP is facing shortage". Keyur Shah agrees OIP is short and RIP supply is "stabilize[d]". Same call: four domestic RIP localisers (CG Power, Hitachi India, MIM, Yash). Call-1 had said "two or three players" and "Ours will not be more than the others". RIP is 80%+ of revenue and the greenfield product. | Call-3 Vineet Khatri / Keyur Shah p13-14, p20; Call-1 Keyur Shah p26 | MAJOR | PARTIALLY CAUGHT |
| I15 | Export price premium shrinks across calls. Call-1: domestic OIP Rs100 exports at "220 or 240"; RIP:OIP "four or five times" in India, "close to double" abroad. Call-2: domestic vs export delta "between 30%-40%". Call-A: RIP price index 4x OIP. The export premium drives the FY28 margin bridge. | Call-A Sumit Poddar p4; Call-1 Keyur Shah p11-12; Call-2 Keyur Shah p22 | MAJOR | MISSED |
| I16 | Sukrut. Yash never says Sukrut loses money ("Unfortunately, today they are not doing business to what they should"). The multiple drops from "8 to 10 times... not more than 5-6 years" to "5x to 6x... next four, five years". EBITDA is withheld twice. QPOWER discloses "very low margin", about Rs25cr legacy losses, "stopped losing money... losses... half", then "extremely profitable this quarter". | Call-2 Keyur Shah p13, p20; Call-3 Keyur Shah p17, p21; QPOWER Nov-2025 l.618; QPOWER Feb-2026 l.785; QPOWER May-2026 l.903-907; QPOWER Aug-2026 l.929-930 | MAJOR | CAUGHT (B05 + B06) |
| I17 | Cyber fraud surfaces only on an analyst question. "No, there is no recovery... already expensed it out." | Call-3 Akshay / Keyur Shah p28 | MINOR | CAUGHT |
| I18 | Analysts keep pushing on overcapacity. Call-2 Keshav cites a peer on global overcapacity; Call-3 Hussain asks about sub-400kV margin compression; VILAS May-2026 analyst cites weak Voltamp/Shilchar margins. Management denies every time. The "no price war for 7-8 years" answer is in Call-2. | Call-2 Keshav / Keyur Shah p13-14; Call-3 Hussain / Keyur Shah p11-12; VILAS May-2026 Hardik Gandhi l.882-885 | MINOR | PARTIALLY CAUGHT |
| I19 | Export geography contradiction: Call-2 lists "Israel... Oman... Africa"; Call-3 "we do not have any exports in those areas of the world". | Call-2 Management p19; Call-3 Keyur Shah p8 | MINOR | PARTIALLY CAUGHT |
| I20 | Peer disclosure: Yash's "founder promoter" Mr. Ramachandran is CEO and board member of VILAS's new 12-400kV bushing venture (OIP first, RIP later). VILAS announced this 12-May-2026. Yash does not mention it in Call-3 on 14-May-2026. | VILAS May-2026 Nilesh Patel l.143-145, l.584-587, l.596-600 (p15) | MAJOR | CAUGHT (B06) |
| I21 | Peers contradict Yash on Chinese access. Yash: "Chinese bushings are never restricted in India since last 6 years, 7 years." POWERINDIA: "they don't allow any imports from neighboring countries, border countries". QPOWER: "we cannot use a lot of Chinese material in the Indian markets because of regulations"; "Chinese insulators... are not available for some of the critical projects in India". | Call-3 Keyur Shah p23; POWERINDIA Feb-2026 N. Venu l.558-561; QPOWER Nov-2025 Bharanidharan Pandyan l.654-656; QPOWER Feb-2026 l.550-552 | MAJOR | PARTIALLY CAUGHT |
| I22 | Chinese liberalisation is live. Aug-2026 analysts report government allowing four Chinese players (transformer and GIS) with 60-65% local content. QPOWER confirms TVA Power Transformers, an insulator plant "somewhere in Baroda" and two GIS makers are allowed. Feb-2026: "Chinese relaxation... would also be covering transformers". Yash's own Call-3 analyst raised the same proposal for bushings. | POWERINDIA Aug-2026 Jason Soans / Venu Nuguri l.508-514; QPOWER Aug-2026 Bhavya Shah / Bharanidharan Pandyan l.762-772; QPOWER Feb-2026 Nemish Sunder l.520-522; Call-3 Hussain p23 | MAJOR | MISSED |
| I23 | A peer contradicts Yash's supply-chain claim. Yash: "At the moment everything is buttoned up, no problem for next two, three years." QPOWER: "all transformer bushings need porcelain or composite"; insulators "still a cause of concern", "how big is the shortage"; the mismatch will get "even more extreme". Yash's own named constraint is supply chain (Call-1 p28; Call-3 p24). | Call-3 Keyur Shah p25; QPOWER Aug-2026 l.902-904; QPOWER Feb-2026 l.548-553 | MAJOR | PARTIALLY CAUGHT |
| I24 | POWERINDIA admits a "temporary industry slowdown" in Q4FY26, "delays in some transmission projects" and "a small dip in the growth in transmission orders". Yash said "Today, the order flow is unlimited" and denies any slowdown. | POWERINDIA Jun-2026 l.154, l.671-677; Call-2 Keyur Shah p18 | MINOR | MISSED |
| I25 | Sukrut JV partner QPOWER moves into bushing-adjacent parts. Winwin composite insulators "what they use for normally bushings"; "now with WS we are getting with insulators and bushings for GIS". Yash said no QPOWER collaboration beyond Sukrut. | QPOWER Aug-2026 l.413-417, l.901-906; Call-2 Vineet / Keyur Shah p15 | MINOR | MISSED |
| I26 | Brownfield slips. Call-2: addition "will again get commissioned in next four to five months". Call-3: still investing ("compelled to invest there"); OIP autoclave bottleneck; OIP deliveries late to customers. | Call-2 Keyur Shah p9-10; Call-3 Keyur Shah p11, p13-14, p16 | MINOR | MISSED |
| I27 | Greenfield unit addition drifts. Call-1: about 5,000 units, all RIP, total 15-16k. Call-3: "5,000 to 7,000 units", total "close to 15,000" now includes brownfield. | Call-1 Keyur Shah p13; Call-3 Keyur Shah p6, p11 | MINOR | MISSED |
| I28 | IR head retitled Head-IR, then IR, then Strategic Advisor. CMD takes a question put to him. | Call-1 p2; Call-2 p2, p6; Call-3 p2 | MINOR | CAUGHT |
| I29 | PLI scheme for RIP ("RIP bushing is at No.1") raised once, never again. | Call-A Nirav Patel p9 | MINOR | CAUGHT |
| I30 | Share figures move inside single answers: RIP share 70% then 75% (Call-A); global share "around 1%" then "1.5%" (Call-2). | Call-A p10; Call-2 p5, p15 | MINOR | CAUGHT |
| I31 | Promotional escalation: "headquarter near by Apple" (Call-A); "8x to 10x... in next 8 to 10 years" (Call-2). | Call-A p11; Call-2 p7-8 | MINOR | CAUGHT |
| I32 | Debt repayment: Keyur Shah will not commit to repaying the Rs27-28cr of debt and says "we might be open to take some additional debt or create some equity inclusion". This foreshadows the Call-3 raise. | Call-2 Rohit Bahirwani / Keyur Shah p20 | MINOR | CAUGHT |

Totals: 32 items. 0 CRITICAL, 17 MAJOR, 15 MINOR.

No item rates CRITICAL. The one repeated evasion across 2+ calls is I8 (unit economics withheld).
B05 catches its core, the margin-bps deflection logged in 2E as "Deflected every time". So no
repeated evasion was MISSED.

---

## PART 2: COMPARISON AGAINST THE PIPELINE

### 2A. Status of each independent item (material items in detail)

| # | Sev | Status | Where the pipeline has it / what it lacks |
|---|---|---|---|
| I1 | MAJOR | CAUGHT | B05 1B, 1C, 2A, 2B, 4D ("slipped ~6-9 months without any call naming it"). |
| I2 | MAJOR | CAUGHT | B05 Correction #9, 1B, 1C, 4D. Note: B05 grades it LOW-MEDIUM. A restated history corrupts the HISTORICAL CAGR cross-check that Section 1B v3.10 A26.1 requires. Stage 11 must use filed revenue, never the concall's "38-40%". |
| I3 | MAJOR | CAUGHT | B05 Correction #3, 1B, 4A, 4D. |
| I4 | MAJOR | CAUGHT | B05 Corrections #10, 1B, 1C, 2A, 4D. |
| I5 | MAJOR | PARTIALLY CAUGHT | B05 #4 and 2E log "three framings". They leave out the Call-2 claim "We have developed in-house capability" (p18), the most direct conflict with a consultant-sourced core. They also leave out the same-page Call-3 conflict ("already got over" vs "continuous ongoing", p15). Reading two different counterparties (MGC for assembly/supply, a separate Swiss consultant for core-making) makes the Call-A and Call-1 accounts reconcilable. B05 calls them "incompatible", which OVERSTATES that pair and UNDERSTATES the real conflicts. |
| I7 | MAJOR | CAUGHT | B05 2D, 2C. |
| I8 | MAJOR | PARTIALLY CAUGHT | B05 2E catches the margin-bps deflection. 2C says Sukrut EBITDA is "consistently withheld". B05 does not record that the CFO gave segment EBITDA in Call-A and that later calls regress. It also omits the Call-3 refusals on price hike, realisation and retrofit margin. The regression affects the Stage 11 margin bridge: Call-A's segment EBITDA is the only line-level margin data in the concall record. |
| I9 | MAJOR | PARTIALLY CAUGHT | B05 1B records "FY27 EBITDA margin guide 24-25%... a guided dip, not 'flat'". But 2A marks Call-2's "maintain or slightly increase" promise "Delivered, beat" on FY26 alone, though the promise covered "one and a half or two years", which includes FY27. 4D has no flag. Correction #1 rightly withdraws "pushed one year", but it misses the magnitude downgrade from "steep" / "considerable" to "gradual". |
| I10 | MAJOR | CAUGHT | B05 Correction #8, 2B, 3C, 4D. |
| I11 | MAJOR | CAUGHT | B05 Correction #2, 1B, 2D, 3D, 4D. |
| I14 | MAJOR | PARTIALLY CAUGHT | B05 fixes the quote (#13) and records the four localisers (#12). But it frames the exchange as a peer saying "bushing demand had reduced" (context misread) and concludes only that RIP demand has not fallen. It never states the implication that RIP scarcity pricing is easing on the product that is 80%+ of revenue and the whole greenfield. 4A trigger 3 has a generic kill condition ("OIP/RIP supply normalises") but does not tie it to this Call-3 evidence. |
| I15 | MAJOR | MISSED | B05 3B: "RIP:OIP price differential and domestic-vs-export realisation deltas stand as previously reported (Call-1, Call-2)". It does not see that the two calls disagree: OIP export at 2.2-2.4x domestic in Call-1, a 30-40% delta in Call-2. |
| I16 | MAJOR | CAUGHT | B05 1B, 1C, 2A, 4A (downshift, EBITDA withheld). B06 Claim 2 (loss quantum and turnaround from QPOWER). |
| I20 | MAJOR | CAUGHT | B06 2D, 2E, Part 4 (MEDIUM-HIGH). |
| I21 | MAJOR | PARTIALLY CAUGHT | B05 flags it as "MEDIUM, PENDING VERIFICATION" and adds it to the peer_questions list. B06 never rules on it. The claim is absent from B06 Part 1, and Part 4 reports "Claims contradicted: 0". The contradicting text sits in two peer files B06 says it read in full. B06 marks POWERINDIA Feb-2026 CITED-ONLY with "no new load-bearing evidence", but that file holds the border-country import statement. |
| I22 | MAJOR | MISSED | Neither report mentions the Aug-2026 peer evidence that Chinese transformer and GIS makers are now allowed to bid. B06 marks POWERINDIA Aug-2026 CITED-ONLY ("general growth commentary"). Before this evidence, the import-substitution moat rested on a policy barrier. It now rests on qualification time and local-content rules alone. |
| I23 | MAJOR | PARTIALLY CAUGHT | B06 Claim 1 cites the QPOWER insulator shortage and "all transformer bushings need porcelain or composite" only as demand corroboration. The same text shows an input-supply risk for a bushing maker. It contradicts Yash's "buttoned up... next two, three years" (Call-3 p25). B06 read the evidence with the sign reversed. |

Minor items: I12, I13, I17, I28, I29, I30, I31 and I32 are CAUGHT. I6, I18 and I19 are PARTIALLY
CAUGHT. B05 Correction #5 has MGC supply to mid-2027 but not the earlier "at least three more
years" exclusivity. B05 records the price-war denial but not the analyst pattern, and it
mis-anchors the "7-8 years" answer (see F-m1). B05's preamble says the Israel/Oman item is
"folded into 2C, 3A, 3C and 4D", but it does not appear in any of those sections. I24, I25, I26
and I27 are MISSED.

### 2B. Pipeline red flags I did not list independently

| Pipeline flag | Assessment |
|---|---|
| B05 4D: cash-conversion weakness never raised on any call | SUPPORTED as a transcript absence. No analyst asks about CFO/PAT or FCF. The Call-2 answers on receivables and inventory are qualitative (p13-14, p21). The underlying metric is B03's, outside this audit. |
| B05 4D: Note 45 bank-vs-books discrepancy never mentioned | SUPPORTED as an absence. Not found in any of the four calls. |
| B05 Correction #4: "three incompatible accounts" | OVERSTATED (see I5). The Call-A and Call-1 accounts describe two counterparties and reconcile. The real conflicts are Call-2 "in-house" and the same-page Call-3 over/ongoing pair. |
| B05 1C: Swiss/MGC technology-agreement conclusion "cited as removing the RIP export restriction" | OVERSTATED. Call-3 ties the removal to Yash's own core ("Once we have our own bushing, we can sell anywhere", p14). A separate answer says no residual IP restriction ("Clean. No restrictive clause.", p21). No answer ties the removal to the end of the MGC agreement. |
| B06 Part 5: greenfield "capex-escalated ~70% against original guidance" | OVERSTATED. The 70% uses the analyst-cited Rs153cr, which B05 itself says management never confirmed (B05 1C, 2A). The figure management confirms is "INR100 crores plus" (Call-2 p16). |
| B06 2D: Ramachandran founder-promoter | SUPPORTED (VILAS May-2026 l.584-600). |
| B06 2E: LD exposure, affordability ceiling | SUPPORTED (QPOWER Nov-2025 l.439-442; POWERINDIA Nov-2025 l.589-591). |
| B06 Claim 7: VILAS CRGO price reversal after Chinese BIS approvals | SUPPORTED (VILAS Nov-2025 l.161-165). |
| B06 Claim 6: QPOWER "blanket for three years", "framework orders" | SUPPORTED (QPOWER Nov-2025 l.469-470; QPOWER Aug-2026 l.536). |

No pipeline flag is NOT SUPPORTED. Three are OVERSTATED (MINOR each).

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| # | B05 row | Earlier call contains the promise? | Later call shows the outcome? | Verdict |
|---|---|---|---|---|
| 1 | Call-A: OIP expansion live end-Feb-2025, Delivered | Yes. "The OIP expansion which will go live by end of February this year" (Call-A p10) | Yes. "new manufacturing capacity for OIP products last year, which was commissioned in the last financial" (Call-1 p10) | CONFIRMED |
| 2 | Call-A: greenfield ready by March-2026, Missed | Yes. "RIP by March 2026, that the Facility will be ready for commissioning" (Call-A p10) | Yes. "final stage... installation is in progress"; trial end-Q2FY27 (Call-3 p5, p9) | CONFIRMED |
| 3 | Call-1: FY26 growth 25-30%, Delivered/exceeded | Yes. "order book, which can take care of our next year invoicing if we have to target 25- 30% growth" (Call-1 p16) | Yes. Rs235.1cr vs Rs150cr, +57% (Call-3 p6-7) | CONFIRMED |
| 4 | Call-1: no further capex till 2030, Reversed | Yes. "we don't see any further CapEx for two or three years... till 2030" (Call-1 p23) | Yes. Rs150cr approval, Rs100-110cr for 550kV, testing, brownfield (Call-3 p11) | CONFIRMED |
| 5 | Call-2: FY26 margin "maintain or slightly increase", Delivered/beat | Yes (Call-2 p11) | Yes for FY26: 25.7% vs 23.1% (Call-3 p7). Caveat: the promise covered "one and a half or two years". FY27 is now guided at 24-25%, below FY26 (I9). | CONFIRMED (direction right for FY26; FY27 half open) |
| 6 | Call-2: Sukrut completion, Partial | Yes. "Sukrut acquisition is still not completed" (Call-2 p18) | Yes. "the Sukrut acquisition closed during the year" (Call-3 p6); EBITDA deferred (p21) | CONFIRMED |

6 checked, 6 confirmed, 0 wrong. The direction of every row checked holds.

---

## PART 4: CREDIBILITY GRADE

B05 grade: C (Mixed). **Concur.** Delivery against financial guidance is strong. All three
revenue and margin promises checked were met or beaten. But the record shows plant slips
described as "on track" (I1), a restated history (I2), contradictions between answers in one
call (I3, I5, I10), shrinking disclosure (I8), a shrinking export premium (I15), and a
supply-chain claim that peers contradict (I23). Two items this audit adds (I15, I22) and three it
sharpens (I9, I14, I23) would, if anything, push toward the low edge of C. None of them moves the
grade a full band.

---

## PART 5: CONSOLIDATED FINDINGS

| ID | Severity | Location | Finding | Evidence |
|---|---|---|---|---|
| F1 | MAJOR | B05 3B | MISSED. The export price premium falls from 2.2-2.4x domestic (Call-1) to a 30-40% delta (Call-2). B05 says both calls' deltas "stand as previously reported". This is a load-bearing input to the FY28 export margin bridge. | Call-1 Keyur Shah p11-12; Call-2 Keyur Shah p22 |
| F2 | MAJOR | B06 Part 1 / 2E; B06 coverage map (POWERINDIA Aug-2026) | MISSED. Chinese transformer and GIS makers are now allowed to bid, with 60-65% local content, per POWERINDIA and QPOWER Aug-2026 analyst exchanges. Not raised as a policy risk to the import-substitution moat. | POWERINDIA Aug-2026 l.508-514; QPOWER Aug-2026 l.762-772; QPOWER Feb-2026 l.520-522 |
| F3 | MAJOR | B06 Part 1 / Part 4 ("Claims contradicted: 0") | PARTIALLY CAUGHT. B06 never rules on the Chinese-restriction peer question B05 added. Two peers contradict Yash's "never restricted": POWERINDIA, border-country import bar; QPOWER, "cannot use a lot of Chinese material... because of regulations". The correct verdict is CONTRADICTED. | Call-3 p23; POWERINDIA Feb-2026 l.558-561; QPOWER Nov-2025 l.654-656; QPOWER Feb-2026 l.550-552 |
| F4 | MAJOR | B06 Claim 1 | PARTIALLY CAUGHT, sign reversed. B06 reads QPOWER's insulator scarcity only as demand support. It is also an input risk for bushings ("all transformer bushings need porcelain or composite"), and it contradicts Yash's "everything is buttoned up... next two, three years". | QPOWER Aug-2026 l.902-904; QPOWER Feb-2026 l.548-553; Call-3 p25 |
| F5 | MAJOR | B05 2A row "Call-2 margin maintain/slightly increase"; 4D | PARTIALLY CAUGHT. FY27 is guided at 24-25%, below FY26's 25.7%, against a Call-2 promise that covered 1.5-2 years. "Steep" became "gradual". 2A shows "Delivered, beat" and 4D has no flag. | Call-2 p11; Call-3 p8-9 |
| F6 | MAJOR | B05 2E, 2C | PARTIALLY CAUGHT. Disclosure regresses: Call-A gives segment EBITDA, later calls refuse price hike, realisation, retrofit margin and Sukrut EBITDA. B05 catches only the margin-bps deflection and Sukrut EBITDA. | Call-A p6; Call-1 p24; Call-3 p13, p21, p26, p27 |
| F7 | MAJOR | B05 Correction #13, 3B, 4A | PARTIALLY CAUGHT. A customer channel reports RIP scarcity easing ("RIP's capacities in the domestic market has come up"), with four domestic localisers. B05 misreads the question's context and does not draw the RIP pricing implication for 80%+ of revenue and the greenfield. | Call-3 p13-14, p20 |
| F8 | MAJOR | B05 Correction #4, 1C, 2E | PARTIALLY CAUGHT and partly OVERSTATED. Missing: Call-2 "We have developed in-house capability" and the same-page Call-3 over/ongoing conflict. Call-A and Call-1 are called incompatible, but they describe two counterparties. | Call-2 p18; Call-3 p15; Call-A p9; Call-1 p18-21 |
| F9 | MINOR | B06 2A | MISSED. POWERINDIA reports a Q4FY26 "temporary industry slowdown", transmission project delays and a dip in transmission order growth. B06 reports only strength. | POWERINDIA Jun-2026 l.154, l.671-677 |
| F10 | MINOR | B06 2C/2E | MISSED. Sukrut JV partner QPOWER moves into bushing-adjacent insulators and "bushings for GIS". | QPOWER Aug-2026 l.413-417, l.901-906 |
| F11 | MINOR | B05 1A/2A | MISSED. The brownfield addition, promised "in next four to five months" (Call-2), is still being funded in Call-3. OIP customers face delays. | Call-2 p9-10; Call-3 p11, p13-14 |
| F12 | MINOR | B05 1B | MISSED. The greenfield unit addition drifts from about 5,000 RIP (Call-1) to "5,000 to 7,000" (Call-3), and the ~15,000 total now includes brownfield. | Call-1 p13; Call-3 p6, p11 |
| F13 | MINOR | B05 Correction #5 | PARTIALLY CAUGHT. MGC exclusivity "At least three more years" (Call-1) becomes supply "till mid of '27" (Call-3). B05 #4 also inverts the exclusivity: it binds MGC to supply only Yash ("they can exclusively supply to us only"), not "in MGC's favour". | Call-1 p20; Call-3 p15 |
| F14 | MINOR | B05 3B | Mis-anchor. The "no price war for 7-8 years" answer is in Call-2 (Keshav, p13-14), not in Call-3 answers to Gunjan Kabra or Hussain. | Call-2 p13-14; Call-3 p11-12 |
| F15 | MINOR | B05 Correction #3 | Misattribution. "we have generated a revenue of around INR235 crores" is the analyst's (Mehul Panjuani) wording, not Darshan Thakkar's or Keyur Shah's. The base figure itself is correct (Rs235.1cr, Darshan Thakkar p6-7). | Call-3 p20 |
| F16 | MINOR | B05 1A | Internal inconsistency. The trigger table gives "Rs80cr of Rs153cr spent" as fact, while 1C and 2A say Rs153cr is an unconfirmed analyst figure. | B05 1A vs 1C |
| F17 | MINOR | B05 1C (export row) | OVERSTATED. Call-3 ties the lifting of the RIP export restriction to Yash's own core, not to the end of the MGC agreement. | Call-3 p14, p21 |
| F18 | MINOR | B06 Part 5 | OVERSTATED. "~70%" capex escalation rests on the unconfirmed analyst Rs153cr. | Call-2 p16; Call-3 p27 |
| F19 | MINOR | B05 preamble | Items said to be "folded into 2C, 3A, 3C and 4D" (Israel/Oman exports; 1%/1.5% share) are absent from those sections. | B05 preamble vs 2C, 3A, 3C, 4D |
| F20 | MINOR | B05 3B / 4D | PARTIALLY CAUGHT. B05 records the overcapacity denial but not the repeated analyst insistence across two Yash calls plus a VILAS analyst. | Call-2 p13-14; Call-3 p11-12; VILAS May-2026 l.882-885 |

Totals: 0 CRITICAL, 8 MAJOR, 12 MINOR.

Scoring basis. Material independent items (CRITICAL + MAJOR) = 17. CAUGHT = 9 (I1, I2, I3, I4,
I7, I10, I11, I16, I20). PARTIALLY CAUGHT = 6 (I5, I8, I9, I14, I21, I23). MISSED = 2 (I15, I22).
Rule 3 defines PARTIALLY CAUGHT as "found but under-weighted or misclassified", meaning the
pipeline had the item. So material_caught = 15 and acceptance_rate = 15/17 = 88%. Strict
reading, counting only full CAUGHT: 9/17 = 53%. The orchestrator should see both numbers. The
material denominator is 17, above the rule-7 floor of 4, so a rate is reported.

Stage 11 and synthesis consequences (flags, not decisions):
- Do not use the concall's restated "38-40% historical CAGR" as the Amendment 26.1 cross-check.
  Use filed revenue.
- Carry I15 into the margin bridge: the export premium is 30-40% (Call-2), not 2.2-2.4x
  (Call-1), until a filed number separates the two readings.
- Carry I22 and I21 into the import-substitution thesis. The policy barrier is contested and
  easing.
- Carry I23 as an input-supply risk against the "buttoned up" claim.

```yaml
stage: B12b
company: "YASHHV"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 32
caught: 17
partially_caught: 9
missed:
  - {severity: "MAJOR", item: "Export price premium shrinks across calls: OIP export 2.2-2.4x domestic (Call-1) vs 30-40% delta (Call-2); B05 3B says deltas stand as reported", anchor: "Call-1 Keyur Shah p11-12; Call-2 Keyur Shah p22"}
  - {severity: "MAJOR", item: "Chinese liberalisation live: four Chinese transformer/GIS players allowed to bid with 60-65% local content; not raised as moat/policy risk", anchor: "POWERINDIA Aug-2026 l.508-514; QPOWER Aug-2026 l.762-772; QPOWER Feb-2026 l.520-522"}
  - {severity: "MINOR", item: "POWERINDIA admits Q4FY26 temporary industry slowdown, transmission project delays, dip in transmission order growth", anchor: "POWERINDIA Jun-2026 l.154, l.671-677"}
  - {severity: "MINOR", item: "Sukrut JV partner QPOWER moves into bushing-adjacent insulators and bushings for GIS", anchor: "QPOWER Aug-2026 l.413-417, l.901-906"}
  - {severity: "MINOR", item: "Brownfield addition promised in 4-5 months (Call-2) still being funded in Call-3; OIP deliveries delayed", anchor: "Call-2 p9-10; Call-3 p11, p13-14"}
  - {severity: "MINOR", item: "Greenfield unit addition drifts ~5,000 RIP (Call-1) to 5,000-7,000 (Call-3); 15,000 total now includes brownfield", anchor: "Call-1 p13; Call-3 p6, p11"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 6, confirmed: 6, wrong: 0}
credibility_grade_concur: "concur - C (Mixed): strong financial delivery vs slips called on-track, restated history, same-call contradictions, shrinking disclosure; added items push toward low edge of C, not a band"
findings:
  - {severity: "MAJOR", location: "B05 3B", finding: "MISSED export premium drift 2.2-2.4x (Call-1) vs 30-40% (Call-2)", anchor: "Call-1 p11-12; Call-2 p22"}
  - {severity: "MAJOR", location: "B06 Part 1/2E; coverage map POWERINDIA Aug-2026", finding: "MISSED Chinese transformer/GIS entry allowed (policy moat easing)", anchor: "POWERINDIA Aug-2026 l.508-514; QPOWER Aug-2026 l.762-772"}
  - {severity: "MAJOR", location: "B06 Part 1/Part 4", finding: "PARTIAL: Chinese-restriction peer question never adjudicated; should be CONTRADICTED, B06 reports 0 contradictions", anchor: "Call-3 p23; POWERINDIA Feb-2026 l.558-561; QPOWER Nov-2025 l.654-656"}
  - {severity: "MAJOR", location: "B06 Claim 1", finding: "PARTIAL, sign reversed: insulator scarcity is an input risk for bushings, contradicts Yash 'buttoned up' supply chain", anchor: "QPOWER Aug-2026 l.902-904; QPOWER Feb-2026 l.548-553; Call-3 p25"}
  - {severity: "MAJOR", location: "B05 2A/4D", finding: "PARTIAL: FY27 margin guided 24-25% below FY26 25.7% vs Call-2 1.5-2 year maintain/increase promise; steep became gradual; no 4D flag", anchor: "Call-2 p11; Call-3 p8-9"}
  - {severity: "MAJOR", location: "B05 2E/2C", finding: "PARTIAL: disclosure regression from Call-A segment EBITDA to refusals on price hike, realisation, retrofit margin, Sukrut EBITDA", anchor: "Call-A p6; Call-1 p24; Call-3 p13, p21, p26, p27"}
  - {severity: "MAJOR", location: "B05 Correction #13/3B/4A", finding: "PARTIAL: customer-channel report of RIP scarcity easing plus four localisers; RIP pricing implication not drawn", anchor: "Call-3 p13-14, p20"}
  - {severity: "MAJOR", location: "B05 Correction #4/1C/2E", finding: "PARTIAL and partly overstated: misses Call-2 'developed in-house' and same-page Call-3 over/ongoing conflict; Call-A/Call-1 accounts reconcile as two counterparties", anchor: "Call-2 p18; Call-3 p15; Call-A p9; Call-1 p18-21"}
  - {severity: "MINOR", location: "B06 2A", finding: "MISSED POWERINDIA Q4FY26 slowdown admission", anchor: "POWERINDIA Jun-2026 l.154, l.671-677"}
  - {severity: "MINOR", location: "B06 2C/2E", finding: "MISSED QPOWER entry into bushing-adjacent insulators", anchor: "QPOWER Aug-2026 l.413-417, l.901-906"}
  - {severity: "MINOR", location: "B05 1A/2A", finding: "MISSED brownfield slip", anchor: "Call-2 p9-10; Call-3 p11, p13-14"}
  - {severity: "MINOR", location: "B05 1B", finding: "MISSED greenfield unit-addition drift", anchor: "Call-1 p13; Call-3 p6, p11"}
  - {severity: "MINOR", location: "B05 Correction #5/#4", finding: "PARTIAL: MGC exclusivity 'at least three more years' shortened to mid-2027; exclusivity direction inverted in #4", anchor: "Call-1 p20; Call-3 p15"}
  - {severity: "MINOR", location: "B05 3B", finding: "Mis-anchor: 'no price war 7-8 years' is Call-2, not Call-3", anchor: "Call-2 p13-14"}
  - {severity: "MINOR", location: "B05 Correction #3", finding: "Misattribution: 'around INR235 crores' is analyst wording", anchor: "Call-3 p20"}
  - {severity: "MINOR", location: "B05 1A", finding: "Rs153cr presented as fact in 1A, as unconfirmed in 1C/2A", anchor: "B05 1A vs 1C"}
  - {severity: "MINOR", location: "B05 1C", finding: "Overstated: export-restriction removal tied to MGC agreement end; Call-3 ties it to own core", anchor: "Call-3 p14, p21"}
  - {severity: "MINOR", location: "B06 Part 5", finding: "Overstated: ~70% capex escalation rests on unconfirmed analyst Rs153cr", anchor: "Call-2 p16; Call-3 p27"}
  - {severity: "MINOR", location: "B05 preamble", finding: "Items claimed folded into 2C/3A/3C/4D (Israel/Oman, 1%/1.5%) are absent", anchor: "B05 preamble vs body"}
  - {severity: "MINOR", location: "B05 3B/4D", finding: "PARTIAL: repeated analyst overcapacity insistence not flagged as pattern", anchor: "Call-2 p13-14; Call-3 p11-12; VILAS May-2026 l.882-885"}
critical_count: 0
major_count: 8
minor_count: 12
material_found: 17
material_caught: 15
acceptance_rate: 88
coverage_basis: "17 material (0 CRITICAL, 17 MAJOR) of 32 listed; 9 CAUGHT + 6 PARTIALLY CAUGHT = 15 had by pipeline (88%); 2 MISSED; strict CAUGHT-only reading 9/17 = 53%"
```
