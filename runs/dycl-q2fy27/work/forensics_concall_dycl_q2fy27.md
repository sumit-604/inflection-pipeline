# FORENSICS concall DYCL q2fy27 (A3 FORENSIC NOTES)

Company: Dynamic Cables Limited (DYCL). Quarter: Q2 FY27. Doctype: concall (call 27-Oct-2026).
Inputs read: A1 structured (runs/dycl-q2fy27/extracted/dycl-concall-q2fy27-structured.md, R001-R207),
A1 fulltext (runs/dycl-q2fy27/extracted/dycl-concall-q2fy27-fulltext.md, L001-L418, all lines read),
A2 ledger (runs/dycl-q2fy27/work/ledger_concall_dycl_q2fy27.md, 207 IDs + M01-M05).
Prior-quarter extract: none (first pipeline review). Notion checklist: none; operator batch watch list used (7 items).
Source PDF and inputs/ not opened.

Evidence tier: every number is management tier (or analyst tier where marked), from a machine
transcript (faster-whisper small.en), unverified. Speakers are not named in Q&A; MD vs CFO per answer
is unresolved (A2 SPEAKER_UNRESOLVED). A row tagged ASR_DOUBT never carries a finding alone in this
report; where an ASR_DOUBT row appears below it is context, and the finding rests on a non-doubt line.
Line cites use the A1 Lnnn prefix (fulltext file line = Lnnn + 20).

## RECONCILIATION
- Structured IDs in ledger: 207 of 207 (R001-R207); orphan IDs none. Every structured row read at its
  cited line in the fulltext. MISSING_FROM_STRUCTURED M01-M05 read at L055, L141-L142, L344, L266, L099.
- Answer-loss register re-read: L060 (T04), L089 (T12), L191-L193 (T36), L276 (T69), L287-L288 (T74),
  L229-L238 (T51-T54), L416 (T113).
- A2 answer split confirmed on read: 7 answered with number, 10 answered without number, 15 deflected,
  1 lost to ASR (R185). No disagreement with A2 classification.
- ledger_reconciled_pct: 100.
- F6/F7 lexicon grep over the fulltext: F6 hits in management speech at L038 ("We expect this
  facility"), L048 ("expected to gain momentum"), L363 ("will be expanding"), L403 ("is still underway").
  F7 note lexicon ("subject to", "evaluating", "exploring", "in discussions", "endeavour",
  "no assurance", "may sometimes", "could have an effect"): zero hits. Spoken hedges outside the
  lexicon are mined below.

## FINDINGS TABLE

id | check | ledger row ref | line/turn | short verbatim quote | classification | forward implication
--- | --- | --- | --- | --- | --- | ---
A3-01 | F6 | R066, R113, R145, R119 (ASR_DOUBT), R176 (PARTIAL), R147 | L036-L039 T03; L089-L090 T12; L186 T35 | "installation of our plant and machinery at our new manufacturing facility" / "We expect this facility to start contributing from the second half of the year" | FORWARD-SIGNAL | H2 FY27 (Oct-26 to Mar-27) is the dated test of the new plant. Installed capacity was asked (L083) and not given; the only size figure is "240, 250 crore potential initially" (L089-L090, ASR_DOUBT, answer opening lost). The Q3 and Q4 FY27 prints must show the plant's revenue; there is no stated tonnage or utilisation path to track it against.
A3-02 | F6 | R164, R165, R168, R124, R125, R137, R133; analyst R014, R024, R053 | L139-L140 T27; L200 T38; L201-L203 T39-T41; L317 T81; L372 T99 | "The budget is not volume based." / "of the growth revenue growth is coming from a price increase" (analyst) / "not price growth, overall value growth, overall sales growth of 20%" / "we are into a dipping raw material kind of scenario" | FORWARD-SIGNAL | Management steers to value growth and refused a volume/price split three times (R179, R186, R194). The analyst said 6% volume growth (L123, L198) and that price drives revenue growth (L200); management did not dispute either. With metal now "dipping" (L317) and contracts mostly pass-through (L255), the price part of value growth turns negative in H2. The 20% guide was not raised despite the analyst-cited H1 growth above 30% (L367, analyst tier), and FY27/FY28 numbers were refused (L372, L376). Lean bear: H2 value growth depends on a volume pickup that management will not quantify.
A3-03 | F7 | R121, R126, R128, R137, R138 | L122 T23; L208-L209 T43; L270-L271 T67 | "we have always maintained our guidance of 10 to 11% going forward" vs "We don't give exact margin guidance for quantitative guidance" | AMBIGUOUS | Within one call the 10-11% figure moves from "guidance ... going forward" (L122) to "typically do" (L208) to "something of margin range" (L271), and an H2 return to the upper half was refused (L267-L271). Status of 10-11% (commitment vs historical range) is unresolved; A4 must ask which, so Role 5 can score it.
A3-04 | F7 | R166, R167, R034, R035, R171, M04, R042 (ASR_DOUBT) | L181 T34; L254-L257 T61; L266 T65 | "Only price, which are on fixed price basis. So, that gets impacted" / "the attribution is not because of the commodity price increase" / "It is largely to do with some kind of product mixes" / "it wasn't very different to how we've done earlier" | AMBIGUOUS | The Q2 margin decline (analyst premise L207, not disputed) gets three explanations that do not fit together. L181 says fixed-price contracts took the commodity hit. L254 says commodity is not the cause. L256 blames product mix. L266, answering the product-mix question, says mix "wasn't very different". If mix did not change and commodity is not the cause, the decline is unexplained. 80-90% pass-through (L255) leaves 10-20% of contracts exposed to metal moves in both directions. Lean bear: A4 question to split the decline into fixed-price commodity loss, mix and other expenses.
A3-05 | F7 | R162, R163 (ASR_DOUBT); Q R180 (DEFLECTED/PARTIAL) | L115-L116 T22; L117-L121 T23 | "we've seen a very sharp drop in the other expenses" (analyst) / "gross profit largely interchangeable items which keep on varying on a quarter on quarter basis" / "as per the terms of the trade" | AMBIGUOUS | Management says other expenses and gross profit swap quarter to quarter by terms of trade (likely freight or delivery terms; the word is ASR-garbled at L121). Gross margin and other-expense ratios are then not comparable across quarters, and the "sharp drop" in other expenses was not called sustainable. A4 question: which cost line moves between other expenses and material cost, and why it moved this quarter.
A3-06 | F6 | R169, R170, R183 (Q), R004-R008, R116-R118 (all ASR_DOUBT) | L161-L166 T31; L071-L072 T06 (ASR_DOUBT, context only) | "it's nothing to do with the new facility. It's completely on the working capital borings. We don't have any specific debt for the new plant" / "the vendor financing facility, which is a part of our working capital cycle" | AMBIGUOUS | Finance cost rose (analyst premise L157) on working-capital borrowing, and the company runs a vendor-finance facility inside its working-capital cycle. Vendor finance (supplier credit or acceptances) can sit in trade payables rather than borrowings, which understates debt. The "15%" finance-cost metric (L071-L072) is ASR_DOUBT and its base is unknown; it carries nothing here. A4 question: vendor-finance amount at 30-Sep-2026 and its balance-sheet line.
A3-07 | F6 | R183 (Q, depreciation part unanswered), R136, R105, R203 (Q); R019-R023 (ASR_DOUBT, context only) | L157-L160 T30; L161 T31; L362-L364 T96; L191-L193 T36 | "Have you capitalized it yet and that's why depreciation has gone up" (analyst) / "it's nothing to do with the new facility" / "CAPEX will be ongoing thing ... largely it would be on a brown field basis" | FORWARD-SIGNAL | If the H1 cost increases have nothing to do with the new plant (L161), the plant was not yet capitalised at 30-Sep, so its depreciation lands from H2 FY27. The CFO's capex answer (L191-L193: 184 crore, 10-15 crore H1 capitalisation, gross block around 200 crore, 7x) is garbled and cut off at L194; it is not used. Future capex has no amount or timing (L363-L364), and funding is stated only as "no specific debt" (L162). Forward: H2 depreciation step-up of unknown size; the capex amount must come from the filed H1 balance sheet.
A3-08 | F7 | R114, M05, R120, R122, R127, R135, R087 (analyst), R188/R202 (Q, DEFLECTED) | L048-L049 T03; L099 T14; L149-L150 T29; L219 T47; L353 T94 | "expected to gain momentum as global macros normalize" / "tariff fear which keep on emerging" / "yes you are right" (to near-term exports hard to predict) / "We don't give market challenging quarter" / "it's difficult to predict and how much would be export led" | FORWARD-SIGNAL | The export outlook is conditional in prepared remarks (L048-L049), names tariff risk (L099), and management agreed near-term export growth is hard to predict over 6-12 months (L147-L150). US order flow was refused twice (L219, L223-L224) after the analyst noted US market entry (L215). The export/domestic split was refused (L353). Lean bear: near-term exports soft, and US tariff exposure size unknown.
A3-09 | F17 | R130, R131 (ASR_DOUBT), R133, M01, R041 (analyst), R195/R198 (Q) | L055 T03; L282 T72; L312-L313 T80; L316 T81 | "With a healthy order pipeline" / "closing order book is again a tricky thing to tell you or to guide you" / "there was a slowdown in the order putting momentum" (analyst, prior call) / "the other booking scenario has improved" | AMBIGUOUS | No order book number, no inflow number. Order intake slowed last quarter on the metal spike (analyst recollection L312-L313, L272-L273, not verifiable without the prior extract). Management says booking "has improved" but gives no figure (L316). The analyst cited a historical 35% order-book growth target (L280, analyst tier), and management declined to guide against it (L282). Capacity is rising while the order book is undisclosed. A4 question: order book at 30-Sep-2026 against 30-Jun-2026 and 31-Mar-2026.
A3-10 | F17 | R172, R158, R159; R206 (Q); R003 (UNATTRIBUTED, ASR_DOUBT, not used) | L382-L383 T104; L385-L390 T105; L053 T03; L317 T81 | "the inventory has gone up significantly" (analyst, from cash flow statement) / "in number of days if you look, the inventory has not increased very significantly" / "the value of the material has also increased" | AMBIGUOUS | Inventory rose in the H1 cash flow (analyst tier). Management gave no days figure, and no OCF, receivable-days or payable-days figure anywhere on the call. September inventory was carried at higher metal value (L389-L390) as metal now dips (L317). On pass-through contracts that reprice to current metal, high-cost stock can create an H2 inventory loss. "Prudent working capital management" (L053) is unquantified. A4 question: H1 OCF, inventory, receivable and payable days at 30-Sep-2026 vs 30-Sep-2025.
A3-11 | F6 | R110 (analyst), R111, R139, R140, R141; R207 (Q, DEFLECTED/PARTIAL) | L398-L401 T107; L403-L405 T107; L407 T109 | "So we should soon see the results in place." / "the product readiness is still underway" / "it all depends upon ... data center market itself is under the stage of..." | AMBIGUOUS | Electron-beam solar cable: no order or customer commitment disclosed, "soon" undated. Data-centre cable: still before type testing, with timing tied to the market. Both are unproven optionality; neither carries revenue weight until an order or type-test pass is filed. Status word "underway" (L403) is the baseline for next quarter's transition check.
A3-12 | F7 | R100, R101 (ASR_DOUBT), R102, R134, M03 (ASR_DOUBT); R201 (Q) | L343 T89; L347-L349 T91 | "nobody can answer this question with certainty" / "the house wire market is seeing the impact or would be impacted we won't be impacted" | AMBIGUOUS | A large new entrant ("Alta Tech", ASR spelling, identity not confirmed) is said to hit house wire (B2C) but not DYCL (B2B, analyst framing L341). The same answer says nobody can be certain. The claim rests on B2B tender insulation; it is untested if the entrant moves into power cables or bids utility tenders. A4 question.
A3-13 | F17 | R043-R045, R048-R050, R173; R199, R200 (Q) | L324-L326 T83; L329-L331 T85 | "70-80 percent of our sales" / "more than 80% of us from the repeat customers" / "top 10 customers contribute around 40-45% of our sales" / "those top 10 customers are also churning out" | NEUTRAL-FACT | Watch item 6 partly answered: top-10 share 40-45%, repeat share above 80% yearly. "Churning out" reads as rotation within the top 10. Utilities vs EPC split never given. Baseline for next quarter.
A3-14 | F17 | R185 (LOST_TO_ASR), R189 (DEFLECTED, email), R063, R142 (TRUNCATED); A2 answer split | L191-L194 T36-T37; L235-L236 T53; L416 T113 | "Can you just email your question? I think we'll get back to you" / "I'm sorry to interrupt you" (operator cut-off of CFO) | NEUTRAL-FACT | 15 of 33 questions deflected, 1 lost to ASR, 7 operator cut-offs; the only identified CFO turn (capex) is garbled and cut off. The call carries few verifiable numbers. Capex, H1 finance cost, depreciation, inventory and OCF must come from the filed H1 results and balance sheet, not this transcript.
A3-15 | F17 | none (no row; silence) | whole transcript L001-L418 | (no mention of promoter holding, pledge, utility or EPC customer split) | NEUTRAL-FACT | Watch item 7 (promoter holding, pledge) and the utility/EPC part of item 6 were not raised by any participant. Promoter holding and pledge are not normal call topics; route to the 30-Sep-2026 shareholding pattern filing. One quarter of silence; prior quarters NOT FOUND.

Finding count: 15. FORWARD-SIGNAL 4 (A3-01, A3-02, A3-07, A3-08). AMBIGUOUS 8 (A3-03, A3-04, A3-05,
A3-06, A3-09, A3-10, A3-11, A3-12). CONFIRMATORY-NEGATIVE 0. NEUTRAL-FACT 3 (A3-13, A3-14, A3-15).
All FORWARD-SIGNAL and AMBIGUOUS findings (12) are flagged for A4 management questions.

ASR caveat on findings: no finding rests on an ASR_DOUBT row alone. A3-01 (240-250 crore), A3-06 (15%),
A3-07 (capex figures) and A3-12 (entrant name) cite ASR_DOUBT rows as context only; each finding
stands on the non-doubt line cited first.

## CHECKLIST SCORECARD

check | status | basis
--- | --- | ---
F1 Zero-value standing items | N.A. | Concall; no financial tables; A2 ZERO_STANDING = 0.
F2 Standalone vs consolidated | N.A. | Concall; no S/C figures stated on the call.
F3 Shell-entity detection | N.A. | Concall; no standalone vs consolidated cost lines.
F4 Unaudited contribution ratio | N.A. | Concall; no auditor Other Matters paragraph.
F5 Going concern / EoM scope | N.A. | Concall; no auditor report; no prior extract to diff.
F6 Forward-commitment mining | FINDING | 13 commitments registered; A3-01, A3-02, A3-06, A3-07, A3-11.
F7 Hedge mining | FINDING | Note lexicon zero hits; spoken hedges at L099, L122 vs L270, L178, L181 vs L254 vs L266, L205, L347; A3-03, A3-04, A3-05, A3-08, A3-12.
F8 Tax forensics | N.A. | Concall; no ETR, deferred tax or prior-year tax figures discussed.
F9 OCI forensics | N.A. | Concall; OCI not discussed.
F10 Share count / dilution | N.A. | Concall; no paid-up capital, EPS or warrant figures discussed.
F11 Reserves / net worth tie-out | N.A. | Concall; no net worth figure stated.
F12 Segment forensics | N.A. | Concall; no segment assets or liabilities; product split refused (L249, L266).
F13 Board outcome | N.A. | Concall; no board outcome, AGM or director items discussed.
F14 Note drafting inconsistencies | N.A. | Concall; no notes or auditor letter. Name variants (Mangal L019 / Mandal L026; "Dynamic Tables" L417) are ASR artefacts, not drafting.
F15 Entity list diffs | N.A. | Concall; no consolidation list; no subsidiaries named.
F16 Presentation dropped/reframed | N.A. | Concall, not a deck; no prior extract to diff. Analyst references to the prior call (L272-L273, L284-L285, L312-L313) are routed to F17 and A4.
F17 Silence audit | FINDING | Watch items 2, 4, 5, 7 and the utility/EPC part of 6 unquantified or silent; A3-09, A3-10, A3-13, A3-14, A3-15. One quarter of silence (prior quarters NOT FOUND).

## COMMITMENT REGISTER (F6)

# | commitment | implied date | turn / line ref | status word
--- | --- | --- | --- | ---
C01 | New facility starts contributing; plant and machinery installation done | H2 FY27 (Oct-2026 to Mar-2027) | T03 L036-L039 (R066, R113, R145) | underway (installation completed; contribution pending)
C02 | New facility initial revenue potential 240-250 crore (ASR_DOUBT) | undated, "initially" | T12 L089-L090 (R119) | initiated
C03 | Overall value (sales) growth around 20%, not price growth | FY27 and long term (undated) | T39-T41 L201-L203 (R124, R125, R168) | restated (underway)
C04 | Operating (EBITDA) margin 10-11% | "going forward" | T23 L122; T43 L208-L209 (R121, R126) | restated; status disputed in-call (A3-03)
C05 | Finance cost "15%" maintained; same for new facility (ASR_DOUBT; base unknown) | ongoing | T06 L071-L072; T08 L074 (R116, R117) | restated
C06 | Export market to gain momentum as global macros normalise | conditional, undated | T03 L048-L049 (R114) | initiated (conditional)
C07 | Order booking to improve as commodity prices dip | near term, undated | T81 L316-L318 (R133) | underway
C08 | Order book reaching the optimum over a period (ASR_DOUBT) | undated | T72 L283 (R131) | initiated
C09 | Capex ongoing; capacity added with demand, largely brownfield; no specific debt | next 18-24 months (analyst frame L361) | T96 L363-L364; T31 L162 (R136, R105, R169) | initiated (no amount)
C10 | Electron-beam solar cable: sales team engaging; results "soon" | "soon", undated | T107 L398-L401 (R139) | initiated
C11 | Data-centre cable: product readiness, then market entry and type testing | undated, market-dependent | T107 L403-L405; T109 L407 (R140, R141) | underway
C12 | Email reply to Akash Dubey's order-size / open-order question | post-call | T53 L236 (R189) | initiated
C13 | FY28 visibility after FY27 closes | after Mar-2027 (Q4 FY27 call) | T101 L377-L378 (R138) | initiated

## WHAT WAS NOT DISCUSSED (F17 silence audit)

Watch item (operator batch brief) | addressed on call? | evidence | consecutive quarters of silence | read
--- | --- | --- | --- | ---
1 Volume growth vs metal pass-through | Asked 3x, deflected; no split | L201, L204-L205, L276; analyst 6% (L123, L198) not disputed | 1 (prior NOT FOUND) | A3-02
2 Order book | No number; guide refused | L282; "healthy order pipeline" L055 unquantified | 1 | A3-09
3 EBITDA per unit / margin | Per-ton refused; margin as range; decline cause conflicting | L134-L140; L122 vs L270; L254 vs L266 | 1 | A3-03, A3-04
4 Working capital days and OCF | Inventory days "not increased very significantly", no figure; OCF, receivable days, payable days not mentioned | L385; L164-L166 vendor finance, no amount | 1 | A3-10, A3-06
5 Capacity expansion and funding | Plant installed; capacity unquantified; capex amount lost to ASR; future capex no amount; "no specific debt" | L036-L039, L083 (unanswered), L191-L194, L362-L364, L162 | 1 | A3-01, A3-07
6 Customer mix (utilities, EPC, exports) | Top-10 and repeat share given; export split refused; utility/EPC split never raised | L324-L331; L353; L042-L043 (ASR-garbled sector list) | 1 | A3-08, A3-13
7 Promoter holding and pledge | Not raised | none | 1 | A3-15
Prior-call item: customer shift to smaller orders, 2-4 months (analyst, ASR_DOUBT) | Unanswered; emailed | L225-L226, L233, L236 | 1 | A3-14
Prior-call item: fixed-price contracts buy metal same day | Answer cut off by operator | L285, L287-L289 | 1 | A3-04

## HAND-OFF NOTES FOR A4
- Every FORWARD-SIGNAL and AMBIGUOUS finding (A3-01 to A3-12, excluding NEUTRAL-FACT rows) needs a
  management question. The highest-value three: margin-decline decomposition (A3-04), volume vs price in
  H1 and H2 with metal falling (A3-02), new-plant capacity, capitalisation date and H2 depreciation (A3-01, A3-07).
- Numbers that must come from the filed Q2 FY27 results / H1 balance sheet, not this transcript: H1 capex
  and CWIP, gross block, finance cost, depreciation, inventory, OCF, borrowings including vendor finance.
- OR-30: pillar-relevant facts (Role 4 Steps 6.5/7, Role 5 Step 8D) are deferred to /fttcp and Role 1.

```yaml
stage: A3-forensics
company: "DYCL"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/dycl-q2fy27/work/forensics_concall_dycl_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
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
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "L036-L039; L089-L090 (ASR_DOUBT context); L083 unanswered", classification: "FORWARD-SIGNAL", implication: "New plant installed; contribution dated H2 FY27; installed capacity not given; Q3/Q4 FY27 prints are the test with no tonnage path to track"}
  - {id: "A3-02", check: "F6", line: "L139; L200 (analyst); L203; L317; L372", classification: "FORWARD-SIGNAL", implication: "Growth framed as value; analyst 6% volume and price-led growth not disputed; metal now dipping so pass-through deflates H2 value growth; 20% guide not raised, FY27/FY28 refused"}
  - {id: "A3-03", check: "F7", line: "L122 vs L208-L209 vs L270-L271", classification: "AMBIGUOUS", implication: "10-11% margin shifts from guidance going forward to typical range to no exact guidance; Role 5 cannot score it until status is fixed"}
  - {id: "A3-04", check: "F7", line: "L181; L254-L257; L266", classification: "AMBIGUOUS", implication: "Q2 margin decline blamed on fixed-price commodity hit, then commodity denied, then mix blamed, then mix not very different; cause unexplained; 10-20% fixed-price exposure both ways"}
  - {id: "A3-05", check: "F7", line: "L115-L116 (analyst); L117-L121", classification: "AMBIGUOUS", implication: "Other expenses and gross profit swap by terms of trade; gross margin not comparable QoQ; other-expense drop not called sustainable"}
  - {id: "A3-06", check: "F6", line: "L161-L166; L071-L072 (ASR_DOUBT context)", classification: "AMBIGUOUS", implication: "Finance cost from WC borrowing plus vendor-finance facility; vendor finance may sit in payables and understate debt; 15% metric unresolved"}
  - {id: "A3-07", check: "F6", line: "L157-L161; L362-L364; L191-L194 (ASR, not used)", classification: "FORWARD-SIGNAL", implication: "H1 cost rise not from new plant implies plant capitalised from H2, so depreciation steps up of unknown size; capex amount and funding undisclosed beyond no specific debt"}
  - {id: "A3-08", check: "F7", line: "L048-L049; L099; L149-L150; L219; L353", classification: "FORWARD-SIGNAL", implication: "Exports conditional on macros, tariff risk named, near-term hard to predict agreed, US orders and export split refused; near-term exports soft, US tariff exposure unsized"}
  - {id: "A3-09", check: "F17", line: "L055; L282; L312-L313 (analyst); L316", classification: "AMBIGUOUS", implication: "No order book or inflow number while capacity rises; prior-quarter intake slowdown cited by analyst; booking improved with no figure"}
  - {id: "A3-10", check: "F17", line: "L382-L383 (analyst); L385-L390; L317", classification: "AMBIGUOUS", implication: "Inventory up in H1 cash flow; no days, OCF, receivable or payable figure; high-cost September stock with metal dipping risks H2 inventory loss"}
  - {id: "A3-11", check: "F6", line: "L398-L401; L403-L405; L407", classification: "AMBIGUOUS", implication: "Solar and data-centre cables unproven: no orders, data-centre pre type testing, undated; underway is next quarter's baseline"}
  - {id: "A3-12", check: "F7", line: "L343; L347-L349", classification: "AMBIGUOUS", implication: "New large entrant said to hit house wire, not DYCL B2B, while nobody can be certain; untested if entrant moves into power cables or utility tenders"}
  - {id: "A3-13", check: "F17", line: "L324-L326; L329-L331", classification: "NEUTRAL-FACT", implication: "Top-10 share 40-45%, repeat share above 80% yearly; utility/EPC split not given; baseline"}
  - {id: "A3-14", check: "F17", line: "L191-L194; L235-L236; L416", classification: "NEUTRAL-FACT", implication: "15 of 33 deflected, 1 lost to ASR, 7 cut-offs, CFO capex turn garbled; numbers must come from filed H1 results"}
  - {id: "A3-15", check: "F17", line: "L001-L418 (absent)", classification: "NEUTRAL-FACT", implication: "Promoter holding, pledge and utility/EPC mix never raised; route to shareholding pattern filing; one quarter silence"}
forward_signals: ["A3-01", "A3-02", "A3-07", "A3-08"]
ambiguous: ["A3-03", "A3-04", "A3-05", "A3-06", "A3-09", "A3-10", "A3-11", "A3-12"]
commitments:
  - {commitment: "New facility starts contributing (plant and machinery installed)", implied_date: "H2 FY27", ref: "T03 L036-L039", status_word: "underway"}
  - {commitment: "New facility initial revenue potential 240-250 crore (ASR_DOUBT)", implied_date: "undated, initially", ref: "T12 L089-L090", status_word: "initiated"}
  - {commitment: "Overall value growth around 20%", implied_date: "FY27 and long term", ref: "T39-T41 L201-L203", status_word: "underway"}
  - {commitment: "Operating margin 10-11%", implied_date: "going forward", ref: "T23 L122; T43 L208-L209", status_word: "underway"}
  - {commitment: "Finance cost 15% maintained incl. new facility (ASR_DOUBT, base unknown)", implied_date: "ongoing", ref: "T06 L071-L072", status_word: "underway"}
  - {commitment: "Exports gain momentum as global macros normalise", implied_date: "conditional, undated", ref: "T03 L048-L049", status_word: "initiated"}
  - {commitment: "Order booking improves as commodity prices dip", implied_date: "near term, undated", ref: "T81 L316-L318", status_word: "underway"}
  - {commitment: "Order book reaching the optimum over a period (ASR_DOUBT)", implied_date: "undated", ref: "T72 L283", status_word: "initiated"}
  - {commitment: "Capex ongoing, brownfield, no specific debt", implied_date: "next 18-24 months (analyst frame)", ref: "T96 L363-L364; T31 L162", status_word: "initiated"}
  - {commitment: "Electron-beam solar cable results soon", implied_date: "soon, undated", ref: "T107 L398-L401", status_word: "initiated"}
  - {commitment: "Data-centre cable product readiness then type testing", implied_date: "undated, market-dependent", ref: "T107 L403-L405; T109 L407", status_word: "underway"}
  - {commitment: "Email reply on order-size / open-order question", implied_date: "post-call", ref: "T53 L236", status_word: "initiated"}
  - {commitment: "FY28 visibility after FY27 close", implied_date: "after Mar-2027", ref: "T101 L377-L378", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Machine transcript with no speaker names; every number is management or analyst tier and unverified, and no finding rests on an ASR_DOUBT row alone. The call is thin: 15 of 33 questions deflected and the CFO capex turn lost, so capex, depreciation, finance cost, inventory and OCF must come from the filed H1 results. The core forensic point is the margin story. Management gave three causes for the Q2 margin decline that cancel out (fixed-price commodity hit at L181, commodity denied at L254, mix blamed at L256, mix not different at L266). The second point is value framing. Management steers to value growth and will not split volume from price. The analyst's 6% volume and price-led revenue were not disputed, and metal is now falling. Pass-through then cuts H2 revenue unless the new plant adds volume, and the plant has no stated capacity. Depreciation should step up from H2 because H1 costs were said to be unrelated to the plant. Vendor finance inside the working-capital cycle may understate debt. Order book, OCF and pledge are silent for one quarter; prior quarters NOT FOUND."
```
