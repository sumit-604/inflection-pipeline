# A3 FORENSIC NOTES: Tejas Networks (TEJASNET), Q2 FY27, Doctype: presentation
Inputs read: A1 structured (R001-R210), A1 fulltext (349 lines), A2 ledger (210 rows), prior-quarter fulltext (Q1 FY27 press release, 107 lines), Notion digest sections 4 and 5 only. Source PDF and inputs/ not opened.
Basis caveat: the Q1 FY27 presentation-class document was a 3-page press release, not a deck. Every Q1-vs-Q2 diff below is basis-limited.
Derived numbers are labelled "derived" and show their arithmetic. The deck states no standalone/consolidated basis; Q1 comparators (402, 271, 202, 1,529, 4,277, 589) tie to the Q1 press release.

## LEDGER RECONCILIATION
- Rows in ledger: 210. Rows read verbatim at cited line: 210. Reconciled: 100%.
- Value mismatches: none. Every ledger value was found verbatim in the fulltext.
- Line drift (value found within 1-5 lines of the cite, interleaved layout; extraction artefact, not a document finding): R006-R009 cited L58-59, values at L59-60 and in the reading-order block L83-84; R099 at L19 (cited L18); R100 at L21 (cited L19); R102 name at L45 (signature block L40-42); R105 at L73 (cited L72); R119 at L238 (cited L237); R177 at L33 (cited L32); R093 axis top "5,000" at L251 (cited L247, chart-title line); R204 attribution spans L170-172.
- Internal tie-outs (deck arithmetic): H1 FY27 = Q1 + Q2 on all five P&L rows (808 = 406 + 402; (207) = (108) + (99); (393) = (199) + (194); (548) = (277) + (271); (409) = (207) + (202)). H1 FY26 less Q2 FY26 gives Q1 FY26 revenue 202, PBT (297), PAT (194). These tie to the Q1 press release prior L57-60. Net debt + cash = 4,866 at Q1 (4,277 + 589). This ties to the Q1 press release gross debt, prior L82 "gross debt of Rs. 4,866 Cr". So the deck's undefined "Net Debt" behaves as gross borrowings less cash.

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R024, R026, R028 (ZERO_STANDING); R025, R027 | p4 L129 | "Other Operating Revenue - 5 0 5 0" | AMBIGUOUS | The Other Operating Revenue line carries PLI incentive income (checklist #8). Q2 FY27 is nil ("-"); Q1 FY27 and H1 FY27 round to 0, against 5 Cr in Q2/H1 FY26. That is two quarters with no visible PLI recognition. The data cannot separate "claims pending/delayed" (checklist #8 RED wording) from "no accrual policy". Lean bear. A4 question: PLI claims filed, accrued and received in H1 FY27, and the FY27 accrual policy. The FY28 tripwire is "Other Operating Revenue < Rs 100 Cr". |
| A3-02 | F6 | R128, R129, R137, R163, R016, R081, R107 | p6 L187-189; p5 L175; p3 L69 | "Received LoI from TCS for 18,685 add-on sites. Started initial" ... "shipments" | AMBIGUOUS | BSNL add-on status moved from silent (Q1 release) to LoI with shipments started. The step is initiated -> underway. The deck says LoI, not PO, and gives no rupee value. The Sep-2026 confirmation deadline (thesis-broken trigger #3; checklist #7) has passed with no "PO" word. Site scope holds at 18,685 (about 18.7k), so the scope is not reduced in sites. Per item #7 the human decides whether shipments under an LoI count as confirmation. A4 question: PO date, PO issuer (BSNL to TCS, TCS to Tejas), rupee value vs the Rs 1,526 Cr on record, and how much is in the 2,315 Cr order book. |
| A3-03 | F6 | R166, R034, R038, R174 | p11 L318; p4 L131; p12 L339 | "Achieve quarterly positive EBITDA financial performance" | AMBIGUOUS | The EBITDA-positive goal carries no quarter or year. QoQ EBITDA worsened from (99) to (108) (L131). Gate 4 on the page needs a re-dated, named EBITDA-positive quarter; the last spoken guidance was "12-18 months". The deck gives no date. A4 question: name the quarter. |
| A3-04 | F6 | R136, R164, R173, R067, R068 | p12 L337; p5 L174; p11 L314 | "Execution of BSNL expansion order will bring down inventory and gross debt" | FORWARD-SIGNAL | This is a trackable, undated commitment linking BSNL execution to deleveraging. In the first delivery quarter, inventory fell only 44 Cr (2,358 to 2,314, L167). Revenue rose 4 Cr QoQ (402 to 406, L128) even with "initial shipments for BSNL 4G add-on" (L72). Track inventory and gross debt each quarter against this line. |
| A3-05 | F7 | R134, R133, R131 | p6 L199; p6 L195; p6 L190 | "Engaged in discussions with Tier-1 MNOs for custom 5G Radio" | AMBIGUOUS | Lexicon hit "in discussions". It sits beside pre-commercial items: "Initiated multiple POC engagements" (L195) and "Declared L1" (L190, pre-award). None carries a customer name, value or date. Treat these as pipeline, not order book. A4 question: count of POCs, expected decision dates, and the OTN L1 award timing and value. |
| A3-06 | F8 | R044, R049, R045, R050, R046, R051 | p4 L133-134 | "PBT (277) (473) (548) (770) (271)" / "PAT (207) (307) (409) (501) (202)" | FORWARD-SIGNAL | Derived tax credit = PBT less PAT. Q2 FY27 70 Cr (25.3% of PBT), Q1 FY27 69 Cr (25.5%), H1 FY27 139 Cr (25.4%). Q2 FY26 166 Cr (35.1%), H1 FY26 269 Cr (34.9%). The loss is still tax-effected at about the 25.17% statutory rate, so the tax credit shields PAT by about 2,530 bps of PBT. If the credit is fully deferred, DTA grows about 70 Cr in Q2 from about Rs 434 Cr at Q1 (Notion 5d). The deck does not split current and deferred tax. DTA recoverability depends on the undated EBITDA-positive goal (A3-03). Verify the DTA and its current/deferred split from the filed results. |
| A3-07 | F11 | R072, R073, R074, R079, R080, R205, R069-R071, R200 | p5 L169; p5 L176-177 | "Net Debt 3,531 4,277 4,384" / "on account of increased operational and capex funding" | FORWARD-SIGNAL | Net debt rose for a second quarter (3,531, then 4,277, then 4,384). This is checklist #4 RED for a second quarter. Headroom to the Rs 4,500 Cr break is 116 Cr, down from 223 Cr at Q1. Derived gross debt (net debt + cash) is 4,835 Cr against 4,866 at Q1 (prior L82). So the 107 Cr net-debt rise came from a 138 Cr cash drawdown (589 to 451), with gross debt about 31 Cr lower. "Capex funding" is new attribution language in a cash-loss quarter. A4 question: the Q2 capex amount and the expected net-debt peak against the 4,500 Cr line. |
| A3-08 | F14 | R128, R104, R129, R107 | p3 L69 vs p6 L187 | "Received the LOI for 18k+ 4G sites for BSNL" vs "Received LoI from TCS" | AMBIGUOUS | Slide 3 reads as a BSNL-issued LOI. Slide 6 names TCS as the issuer. Tejas's contracting counterparty is TCS, a Tata Group company and a related-party-adjacent counterparty (Tejas's majority holder is Panatone, a Tata Sons subsidiary, prior L91-92). Payment terms, credit risk and receivable timing pass through TCS, not BSNL. A4 question: is the Tejas counterparty TCS, and on what payment terms (back-to-back with BSNL or not)? |
| A3-09 | F14 | R205, R199, R200, R209, R198, R017, R018, R085 | p5 L169 vs L178-180; p4 L125; p3 L75 vs p7 L222-223 | "1Net working capital taken as..." / "2Cash and cash equivalents includes..." (no Net Debt note) | NEUTRAL-FACT | Drafting gaps, each immaterial. (a) The deck defines NWC and cash in footnotes but not Net Debt. (b) No slide states standalone or consolidated basis. (c) Slide 3 says "cumulative global patent filing count to 748" and slide 7 says "cumulative global patent count to 748"; 722 + 26 = 748 ties to the Q1 filing count. (d) The IR contact changed from ir@india.tejasnetworks.com (prior L95) to ir@tejasnetworks.com (L346). |
| A3-10 | F16 | R210, R126 | p2 L54 (Q2) vs prior L98-107 | Q1: "SAFE HARBOUR" ... Q2: "All rights reserved." only | NEUTRAL-FACT | The Q1 release carried a forward-looking safe-harbour paragraph. The Q2 deck carries none, yet it holds 48 forward statements (R128-R175). This is basis-limited (release vs deck). It is recorded so the next deck can be checked. |
| A3-11 | F16 | R069-R074, R173 | p5 L161-169 vs prior L81-82 | Q1: "gross debt of Rs. 4,866 Cr and cash of Rs. 589 Cr" | AMBIGUOUS | Gross debt was disclosed in Q1 and is absent from the Q2 table. In the same deck the company commits to "bring down ... gross debt" (L337). The metric the commitment names is not shown. Derived Q2 gross debt is 4,835 Cr (A3-07). A4 question: confirm Q2 gross debt and the finance cost. |
| A3-12 | F16 | R010, R011, R209, R167 | p3 L85 | "Order book at end of Q2: INR 2,315 Cr (1,529 Cr in Q1FY27)" | AMBIGUOUS | No order-book definition (FOOTNOTE_UNRESOLVED R209): LoI vs PO, gross vs net of GST, L1 included or not. Derived implied Q2 inflow = 2,315 - 1,529 + 406 = about 1,192 Cr, assuming the book burns at sales revenue with no cancellations. That is below the Rs 1,526 Cr BSNL add-on value on record, before adding BharatNet routers, GPON POs and the Africa DWDM win. Reading A: the add-on is partly booked (LoI-stage portion excluded). Reading B: the TCS LoI value is lower than 1,526 Cr (checklist #7 RED if confirmed materially reduced). The rupee value of the BSNL portion in the book separates the two readings. |
| A3-13 | F16 | R012-R015, R191, R192 | p3 L88; p3 L90-91 | "International: 12%" / "Closing Order Book Mix ... International: 4%" | FORWARD-SIGNAL | This is a new metric, the first disclosed revenue and order-book geographic mix. Q2 international revenue is 12% (derived about 49 Cr, excluding other operating revenue): checklist #6 AMBER band, between the 10% RED and 15% GREEN lines. The closing book is 4% international (derived about 93 Cr) and 96% India. As BSNL executes, forward revenue mix drifts toward the less-than-10% RED line unless international inflow outruns booking. |
| A3-14 | F16 | R054-R059, R197, R174, R023, R038, R053 | p4 L135-138; p12 L339; vs prior L80 | Q1: "a QoQ growth of 21%"; Q2: "Revenue is 406 Cr in Q2FY27 vs 262 Cr in Q2FY26"; "Steadily improving financial performance" | CONFIRMATORY-NEGATIVE | The comparison baseline changed. Q1 commentary used QoQ when QoQ was +21%. The Q2 callouts are YoY only, in a quarter where QoQ revenue grew 1% (402 to 406), EBITDA worsened ((99) to (108)) and PAT worsened ((202) to (207)). "Steadily improving" holds YoY only. Checklist #2: 406 Cr is a second quarter just above the 400 Cr RED line. The FY27 Rs 2,000 Cr floor now needs derived (2,000 - 808) / 2 = 596 Cr a quarter in H2, up from 533 Cr. |
| A3-15 | F16 | R204, R061-R065, R203 | p5 L170-172 | "due to decreased Trade Receivables on account of collections, non-recourse discounting and Customer advance settlements" | AMBIGUOUS | The 243 Cr NWC fall (4,478 to 4,235) is attributed in part to non-recourse discounting, a receivables sale that is financing-like, not an operating collection. The metric is also stated "Net of Cust Advance" (L164-165), so advance settlements can move net receivables without cash collection. The split is not quantified. Cash conversion stays INDETERMINATE. A4 question: rupee amount discounted in Q2, the cost, and gross receivables and customer advances separately. |
| A3-16 | F17 | R024-R028; R060-R080 (table rows) | p4 L129; p5 L161-169 | "Net Working Capital(1) 4,138 4,478 4,235" ... "Net Debt 3,531 4,277 4,384" (no equity, DTA, PLI or cash-flow row) | CONFIRMATORY-NEGATIVE | Silence on deteriorating metrics across two consecutive presentation-class documents (Q1 release, Q2 deck). The silent items are PLI income, DTA, book value/QIP and cash-loss/CFO. Each carries an adverse prior read (Notion 5d: DTA about Rs 434 Cr, about 52% of equity; BV in the AMBER band; PLI FY26 collapse). See the What Was NOT Discussed table. The concall is the stronger venue; this count covers decks and releases only. |
| A3-17 | F17 | R166, R193, R194, R150; prior L74 | p11 L318; p4 L119; p10 L286; prior L74 | "1EBIT = PBT - Other Income + Finance Cost including Net forex loss" | AMBIGUOUS | Some commitment and checklist items are only partly addressed. (a) Finance cost (#10) is not shown. Derived EBIT less PBT = finance cost incl. net forex less other income = 78 Cr in Q2 vs 77 Cr in Q1, so gross finance cost cannot be tested against the 90-100 Cr AMBER band. (b) Intangibles under development: "Investments in 5G-Advanced, 6G" (L286) gives no capitalised amount. (c) The Q1 power-utility vendor selection (prior L74 "Selected as a vendor for the communication network modernization of a large power") is not mentioned in Q2. (d) The EBITDA-positive date is absent (A3-03). |
| A3-18 | F11 | R049, R051 | p4 L134 | "PAT (207) (307) (409) (501) (202)" | FORWARD-SIGNAL | The deck carries no equity, so net worth and checklist #9 cannot be tied out from it. Against the 13-Oct pre-registered test (Notion 5e: "A Q2 loss above about Rs 185 Cr takes it below Rs 140"), Q2 PAT is (207) Cr, so #9 is likely RED. This is not computed here; A4 must confirm book value per share from the filed results, including OCI and ESOP. No QIP is mentioned in the deck. |

## CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 | FINDING | 3 ZERO_STANDING cells on Other Operating Revenue (PLI line), nil for two quarters (A3-01). |
| F2 | N.A. | The deck presents one unlabelled basis; it has no standalone vs consolidated columns. The missing label is logged under F14 (A3-09). |
| F3 | N.A. | No standalone and consolidated cost lines in a presentation. |
| F4 | N.A. | No auditor report or Other Matters paragraph in a presentation. |
| F5 | N.A. | No Emphasis of Matter or going-concern language in a presentation. |
| F6 | FINDING | 14 commitments registered. BSNL LoI not PO (A3-02), EBITDA goal undated (A3-03), inventory and gross debt commitment (A3-04). |
| F7 | FINDING | "in discussions" hit at L199 plus pre-commercial POC and L1 items (A3-05). No "subject to", "no assurance", "evaluating" or "exploring" hits. |
| F8 | FINDING | Derived tax credit at about 25.3-25.5% of the pre-tax loss implies continued DTA build of about 70 Cr in Q2 (A3-06). |
| F9 | N.A. | The deck carries no OCI. |
| F10 | N.A. | The deck carries no share count, paid-up capital or EPS. |
| F11 | FINDING | Net debt and gross debt tie-out against the Q1 release: 116 Cr headroom to the break (A3-07). Net worth not in the deck; BV test likely breached (A3-18). |
| F12 | N.A. | No segment assets or liabilities in the deck. Wireless and wireline appear as narrative only. |
| F13 | N.A. | The cover letter (L28-33) is a Reg 30/46 presentation intimation, not a board outcome. |
| F14 | FINDING | LoI issuer wording BSNL vs TCS (A3-08). Net Debt undefined, basis unlabelled, patent count wording drift (A3-09). |
| F15 | N.A. | No consolidation entity list in a presentation. The Tata endorsement logo (L209) is a brand change, not an entity change. |
| F16 | FINDING | Safe harbour dropped (A3-10), gross debt dropped (A3-11), order book undefined with implied-inflow gap (A3-12), new geographic mix metric (A3-13), QoQ-to-YoY baseline switch (A3-14), non-recourse discounting attribution (A3-15). |
| F17 | FINDING | Deck-level silence audit against the Notion checklist and F6 commitments (A3-16, A3-17). The basis is decks and releases, not a transcript. |

## COMMITMENT REGISTER (F6)

| # | commitment | implied date | ref | status word |
|---|---|---|---|---|
| C1 | BSNL 4G add-on, TCS LoI for 18,685 sites; deliveries | "within timelines" (L313), timelines undisclosed | p6 L187-189; p5 L175; p3 L69, L72 | underway (shipments started Q2 FY27; Q1 release silent) |
| C2 | Significant inventory reduction through BSNL execution | undated | p5 L174; p11 L314; p12 L337 | initiated (inventory -44 Cr QoQ) |
| C3 | Bring down gross debt through BSNL execution | undated | p12 L337 | initiated (derived gross debt 4,866 to 4,835) |
| C4 | Achieve quarterly positive EBITDA | undated | p11 L318 | not started (EBITDA (108) Q2) |
| C5 | BharatNet Phase 3 middle-mile IP routers, three states (SI partner LOI) | undated | p6 L184-187 | initiated (LOI) |
| C6 | Strategic pan-India OTN/WDM, GoI tender | award date undisclosed | p6 L189-193 | initiated (declared L1, pre-award) |
| C7 | GPON OLT supply to leading ISPs | undated | p6 L195-198 | initiated (POs received) |
| C8 | 400G DWDM, tier-1 pan-African operator | undated | p6 L200-203 | initiated (vendor selection) |
| C9 | End-to-end 5G network, South America | phase 1 in Q2 FY27 | p6 L190-193; p3 L72-73; prior L65 | underway (Q1 "first commercial win", Q2 "Shipped Tejas RAN equipment for the first phase"; "deployed 5G Core") |
| C10 | Wireless POCs, North America and Asia-Pacific | undated | p6 L195-197 | initiated |
| C11 | Custom 5G radio development with Tier-1 MNOs | undated | p6 L199-201 | in discussions |
| C12 | Increased focus on collections | undated | p11 L317 | underway (receivables 2,232 to 2,042, partly via discounting) |
| C13 | Scale international business through partnerships | undated | p11 L305-306 | underway (international 12% of Q2 revenue) |
| C14 | Next-generation Connectivity Lab | Q2 FY27 | p7 L225-227 | completed (inaugurated) |

## WHAT WAS NOT DISCUSSED (F17, deck-level)
Count = consecutive presentation-class documents silent (Q1 FY27 release, Q2 FY27 deck). Concall silence is counted separately.

| item | Q2 deck treatment | consecutive silent | direction of last known read |
|---|---|---|---|
| #8 PLI income | No "PLI" word; Other Operating Revenue nil (L129) | 2 | deteriorating (FY26 collapse; RED) |
| #9 Book value/share; QIP below Rs 400 | No equity row (L161-169); no QIP mention | 2 | deteriorating (AMBER, likely RED, A3-18) |
| DTA | No tax split; no DTA | 2 | deteriorating (about 434 Cr, about 52% of equity) |
| Cash-loss track / CFO | EBITDA only; no cash flow | 2 | adverse (year 2 of a 3-year track) |
| EBITDA-positive date | Goal stated, date absent (L318) | 2 | undated (last "12-18 months", concall) |
| #10 Finance cost | Not shown; net derivable only (78 Cr) | 2 | AMBER trending RED at Q1 |
| Intangibles under development | "Investments in 5G-Advanced, 6G" (L286), no amount | 2 | Rs 950 Cr impairment item ND |
| #7 BSNL PO value / PO word | LoI from TCS, shipments; no PO, no value | 2 (value) | Q1 silent entirely |
| Gross debt | Dropped vs Q1 (prior L82) | 1 | derived 4,835 Cr |
| Q1 power-utility vendor selection (prior L74) | Absent; only generic "Modernization of Utility networks" (L274) | 1 | n/a |
| #2, #4, #6 | Addressed (406 Cr; net debt 4,384 Cr; international 12%) | 0 | #2 AMBER, #4 RED, #6 AMBER |

```yaml
stage: A3-forensics
company: "TEJASNET"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tejasnet-q2fy27/work/forensics_presentation_tejasnet_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F1", line: "p4 L129", classification: "AMBIGUOUS", implication: "Other Operating Revenue (PLI line) nil/0 for Q1 and Q2 FY27 vs 5 Cr in Q2 FY26; PLI claims pending or not accrued; checklist #8"}
  - {id: "A3-02", check: "F6", line: "p6 L187-189; p5 L175; p3 L69", classification: "AMBIGUOUS", implication: "BSNL add-on is a TCS LoI with shipments, no PO word and no value after the Sep-2026 deadline; trigger #3 ruling is human"}
  - {id: "A3-03", check: "F6", line: "p11 L318; p4 L131", classification: "AMBIGUOUS", implication: "EBITDA-positive goal undated while QoQ EBITDA worsened (99) to (108); Gate 4 needs a named quarter"}
  - {id: "A3-04", check: "F6", line: "p12 L337; p5 L174; p11 L314", classification: "FORWARD-SIGNAL", implication: "Undated commitment: BSNL execution cuts inventory and gross debt; Q2 inventory -44 Cr only"}
  - {id: "A3-05", check: "F7", line: "p6 L199; p6 L195; p6 L190", classification: "AMBIGUOUS", implication: "Custom radio 'in discussions', POCs and OTN L1 are pipeline with no name, value or date, not order book"}
  - {id: "A3-06", check: "F8", line: "p4 L133-134", classification: "FORWARD-SIGNAL", implication: "Derived tax credit 70 Cr Q2 (25.3% of PBT), 139 Cr H1; DTA keeps building (about 434 Cr at Q1) against an undated profit date"}
  - {id: "A3-07", check: "F11", line: "p5 L169; p5 L176-177", classification: "FORWARD-SIGNAL", implication: "Net debt 4,384 Cr, RED for a second quarter, 116 Cr headroom to the 4,500 break; derived gross 4,835; new 'capex funding' attribution"}
  - {id: "A3-08", check: "F14", line: "p3 L69 vs p6 L187", classification: "AMBIGUOUS", implication: "LoI issuer is TCS (Tata Group), not BSNL; payment and credit chain runs through TCS"}
  - {id: "A3-09", check: "F14", line: "p5 L169, L178-180; p4 L125; p3 L75 vs p7 L222-223", classification: "NEUTRAL-FACT", implication: "Net Debt undefined, basis unlabelled, patent count wording drift, IR email changed"}
  - {id: "A3-10", check: "F16", line: "p2 L54; prior L98-107", classification: "NEUTRAL-FACT", implication: "Safe harbour present in Q1 release, absent in Q2 deck with 48 forward statements; basis-limited"}
  - {id: "A3-11", check: "F16", line: "p5 L161-169; prior L81-82", classification: "AMBIGUOUS", implication: "Gross debt dropped from disclosure while L337 commits to reducing it"}
  - {id: "A3-12", check: "F16", line: "p3 L85", classification: "AMBIGUOUS", implication: "Order book undefined; derived Q2 inflow about 1,192 Cr below the 1,526 Cr BSNL add-on on record; partial booking or lower value"}
  - {id: "A3-13", check: "F16", line: "p3 L88; p3 L90-91", classification: "FORWARD-SIGNAL", implication: "New mix metric: international 12% of revenue (AMBER) but 4% of the closing book; forward mix drifts toward the <10% RED line"}
  - {id: "A3-14", check: "F16", line: "p4 L135-138; p12 L339; prior L80", classification: "CONFIRMATORY-NEGATIVE", implication: "Baseline switched QoQ to YoY when QoQ EBITDA and PAT worsened; H2 needs 596 Cr per quarter for the 2,000 Cr floor"}
  - {id: "A3-15", check: "F16", line: "p5 L170-172", classification: "AMBIGUOUS", implication: "NWC fall partly from non-recourse discounting (financing-like); cash conversion stays INDETERMINATE"}
  - {id: "A3-16", check: "F17", line: "p4 L129; p5 L161-169", classification: "CONFIRMATORY-NEGATIVE", implication: "PLI, DTA, BV/QIP and cash-loss silent across 2 presentation-class documents, all with adverse prior reads"}
  - {id: "A3-17", check: "F17", line: "p11 L318; p4 L119; p10 L286; prior L74", classification: "AMBIGUOUS", implication: "Finance cost only derivable net (78 vs 77 Cr); IUD amount, power-utility win and EBITDA date absent"}
  - {id: "A3-18", check: "F11", line: "p4 L134", classification: "FORWARD-SIGNAL", implication: "Q2 PAT (207) Cr exceeds the pre-registered about 185 Cr loss for BV below Rs 140; #9 likely RED; confirm from the filed result"}
forward_signals: ["A3-04", "A3-06", "A3-07", "A3-13", "A3-18"]
ambiguous: ["A3-01", "A3-02", "A3-03", "A3-05", "A3-08", "A3-11", "A3-12", "A3-15", "A3-17"]
commitments:
  - {commitment: "BSNL 4G add-on, TCS LoI 18,685 sites, deliveries", implied_date: "within timelines (undisclosed)", ref: "p6 L187-189; p5 L175; p11 L313", status_word: "underway"}
  - {commitment: "Inventory reduction via BSNL execution", implied_date: "undated", ref: "p5 L174; p11 L314; p12 L337", status_word: "initiated"}
  - {commitment: "Gross debt reduction via BSNL execution", implied_date: "undated", ref: "p12 L337", status_word: "initiated"}
  - {commitment: "Quarterly positive EBITDA", implied_date: "undated", ref: "p11 L318", status_word: "not started"}
  - {commitment: "BharatNet Phase 3 IP routers, three states (SI LOI)", implied_date: "undated", ref: "p6 L184-187", status_word: "initiated"}
  - {commitment: "GoI strategic OTN/WDM network, L1", implied_date: "award undisclosed", ref: "p6 L189-193", status_word: "initiated (L1, pre-award)"}
  - {commitment: "GPON OLT POs from leading ISPs", implied_date: "undated", ref: "p6 L195-198", status_word: "initiated"}
  - {commitment: "400G DWDM, tier-1 pan-African operator", implied_date: "undated", ref: "p6 L200-203", status_word: "initiated"}
  - {commitment: "South America end-to-end 5G, phase 1", implied_date: "Q2 FY27", ref: "p6 L190-193; prior L65", status_word: "underway"}
  - {commitment: "Wireless POCs, North America and APAC", implied_date: "undated", ref: "p6 L195-197", status_word: "initiated"}
  - {commitment: "Custom 5G radio with Tier-1 MNOs", implied_date: "undated", ref: "p6 L199-201", status_word: "in discussions"}
  - {commitment: "Increased focus on collections", implied_date: "undated", ref: "p11 L317", status_word: "underway"}
  - {commitment: "Scale international business via partnerships", implied_date: "undated", ref: "p11 L305-306", status_word: "underway"}
  - {commitment: "Next-generation Connectivity Lab", implied_date: "Q2 FY27", ref: "p7 L225-227", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The deck is single-basis and unaudited, with no notes, so F2-F5, F9, F10, F12, F13 and F15 are N.A. The load-bearing reads come from deck arithmetic and are labelled derived. Three thesis lines moved toward break. Net debt of 4,384 Cr leaves 116 Cr to the 4,500 Cr break, down from 223 Cr. Q2 PAT of (207) Cr exceeds the roughly 185 Cr loss that the 13-Oct pre-registered test said takes BV/share below Rs 140. The deck carries no equity, so A4 must confirm from the filed result. Tax credits at about 25% of the pre-tax loss keep building DTA (about 70 Cr in Q2). The BSNL add-on is still a TCS LoI with no PO word and no value after the Sep-2026 deadline. Shipments did start, so the trigger #3 ruling is human. Derived Q2 inflow (about 1,192 Cr) sits below the 1,526 Cr add-on value. The value of the BSNL portion in the book separates partial booking from a lower value. The deck switched from QoQ to YoY-only callouts in a quarter where QoQ EBITDA and PAT worsened. The Q1 baseline was a press release, so dropped-item reads are basis-limited."
```
