# STAGE 12, VERIFIER B: CONCALL RED FLAGS. ACCORD (Accord Transformer & Switchgear Ltd, BSE SME 544710)

Run date 2026-10-06. Phase 1. Model claude-opus-5-5. Fresh context. Units: Rs Cr unless the source states lakh. "calc" marks arithmetic on a sourced figure.

## 0. Scope, inputs and anchor key

Inputs read:
- Company transcript, one call only: H2 FY26 / FY26 results call, 1-Jun-26 (inputs/concalls/Concall_Jun_2026_Transcript.txt). Speakers: Pradeep Verma (Founder and MD), Nitin Gupta (CFO).
- Communication record against filed sources, as the task directs: Annual Report FY26 (Directors' Report, MD&A, explanatory statement, notes), Investor Presentation filed with the call on 1-Jun-26, Q1 FY27 business update (27-Jul-26), H1 FY27 business update (5-Oct-26), all order, land and board filings in inputs/announcements, and the prospectus (26-Feb-26) where a call statement refers to the IPO.
- Peer transcripts: Danish Power (8-Nov-25, 11-May-26), Shilchar Technologies (22-Apr-25, 18-Oct-25, 5-May-26, 14-Aug-26). Read for statements that bear on Accord's claims.
- Pipeline reports read only after the independent list was complete: outputs/reports/05-concall.md with its block, outputs/reports/06-peers.md with its block.

Anchor key:
- Tr. Lnnn = line in the transcript text file. Page markers [pN] are the "[page N]" markers in that file.
- Deck Lnnn = Investor_Presentation_1.txt (cover states it is the presentation for the 1-Jun-26 call, Deck L17, L36).
- AR p.N = printed Annual Report page, with file line Lnnn.
- Prospectus Lnnn = Accord_Prospectus_Feb2026.txt.
- Filings = inputs/announcements file name and line.
- Peer keys as in B06: D-N25, D-M26, S-A25, S-O25, S-M26, S-A26, with file line numbers.

Method limits:
- One company call. A cross-quarter evasion test cannot run. No CRITICAL can arise under the "repeated evasion across 2+ quarters" rule.
- Live web was not used. Every external claim is marked PENDING LIVE VERIFICATION where it needs it.
- A search hit showed one line of inputs/operator-notes.md, which is not a named input. It did not inform any item or grade.

## 1. Independent red-flag list (read before the pipeline reports)

Severity on the common scale. Material = CRITICAL + MAJOR. 23 items: 8 MAJOR, 15 MINOR, 0 CRITICAL.

### R1. MAJOR. Opening remarks present FY26 as growth and better profit. Every filed line fell.
- Claim: "FY26 has been a year of steady growth and improved profitability for the company" (Pradeep Verma, Tr. L162-163 [p4]). H2 "remained equally encouraging... highlighting strong business momentum" (Tr. L168-170 [p4]).
- Filed, same-day deck: H2 FY26 revenue 4,235.36 lakh vs H2 FY25 5,753.19 lakh, -26.4% (calc). H2 EBITDA 493.64 vs 796.66 lakh, -38.0% (calc). H2 PAT 325.32 vs 545.00 lakh, -40.3% (calc) (Deck L1211-1225). FY EBITDA margin 11.68% (FY25) to 10.39% (FY26); PAT margin 7.51% to 6.40% (Deck L1243-1248).
- Filed, AR: revenue 7,006.92 vs 7,902.25 lakh, -11.3% (calc); PAT 450.43 vs 594.37 lakh, -24.2% (calc) (AR p.55, L1650-1668). MD&A three months later: "a moderation in revenue and profitability compared to the previous financial year" (AR p.81, L3046-3047).
- Deflection inside Q&A: Aditya Khetan asked about the half-year fall (Tr. L194-195 [p5]). The CFO answered with the full-year gap, "around INR9 crores" (Tr. L197). The H2 gap was Rs 15.18 Cr (calc, deck). Fenil stated that EBITDA margin "improved... to almost 11% in... FY26" (Tr. L431-434 [p11]). The CFO accepted the premise ("Yes, yes", Tr. L435). FY26 margin fell 1.29 points year on year (calc, deck).
- The other reading: H2 FY26 margin (11.77% as said, Tr. L177) is above the FY26 full year 10.39%, so "improved" holds sequentially, H2 over H1. Year on year it does not hold on any line. The deck that management filed the same day carries the year-on-year figures.

### R2. MAJOR. FY27 guidance has two forms that do not agree.
- Nitin Gupta: growth "60% to 80%" due to the deferment, then "around INR120 crores to INR180 crores" for FY27 (Tr. L250-264 [p6-p7]).
- 60-80% on 70.07 gives Rs 112.1-126.1 Cr (calc). Rs 120-180 Cr is +71% to +157% (calc). The upper end also exceeds the CFO's own capacity arithmetic: Rs 120 Cr at "around 90%" (Tr. L489-491) implies a ceiling near Rs 133 Cr (calc).

### R3. MAJOR. Capacity statements do not reconcile. The MVA question was dodged. The call-day deck carries two capacity figures.
- Pradeep: Rs 150 Cr "without any hurdles", up to Rs 200 Cr if no customer delays (Tr. L273-277 [p7]).
- Fenil asked twice about 1,200 MVA (Tr. L482-486 [p12]). Pradeep: "I'm not getting question" (L484), then "capacity about uh 120 to 180" (L487), which is the revenue band. Nitin: "75% to 80%" now, "around 90%" at Rs 120 Cr+ (L488-491).
- Deck, same day: "1200+ MVA Installed manufacturing capacity (FY26)" (Deck L454-456) and "installed capacity of 900.36 MVA per annum" (Deck L867-878).
- Prospectus: FY26 900.36 MVA installed, 628.30 MVA production, of which only 400.50 MVA is actual to Q3 and the rest "extrapolated", 69.78% (Prospectus L8919-8925, CE certificate 31-Jan-26).
- AR and Q1 update say 1,200+ MVA (AR L163-164, p.80 L2986; Q1 update L79). IPO machinery spend was 0.00% to 2-Sep-26 (AR p.50, L1394-1396). FY26 PP&E purchase was Rs 146.19 lakh (AR L3864).
- [INFERENCE] The 300 MVA step from 900.36 to 1,200+ has no filed capex behind it. Reading A: a basis change, for example a rating mix or a shift basis. Reading B: a promotional figure. Separating observation: a chartered engineer certificate or a filed capacity note for 1,200 MVA.

### R4. MAJOR. Rs 1,600 Cr NHEV claim with exclusivity and "LOI already issued". No Regulation 30 filing.
- Pradeep: "approximately INR1,600 crores worth of compact substations"; "only our brand is approved there... Accord only can supply there. This LOI is already issued" (Tr. L572-575 [p14]). Then "I am talking about the total project cost" (L578), and in the next sentence "revenue of around INR1,600 crores will be generated" (L580). The analyst asked for the share of revenue (L576-577). No share was given.
- Filed record: no NHEV LOI among the order, board and update filings 23-May to 5-Oct-26. Q1 update says only "Continued supplying transformers and switchgear solutions for NHEV fast-charging infrastructure" (Q1 update L106-107). The H1 update has no NHEV line. The prospectus says only "Our collaboration with NHEV" (Prospectus L8477).
- Scale check (calc): Rs 1,600 Cr over 450 stations = Rs 3.56 Cr per station. The one filed compact substation order prices two units (800 kVA and 400 kVA) at Rs 50.40 lakh basic (20260905 L93-95, L102), about Rs 0.25 Cr per unit. The claim is about 14 times the filed unit price (calc).
- [INFERENCE] The Rs 1,600 Cr is a programme figure, not Accord's supply value. If an LOI of that size exists, it was not disclosed. If it does not exist, the call statement is false. Separating observation: the LOI text, with Accord's scope and value, filed on BSE. NHEV, NHAI, Tata and Infosys roles: PENDING LIVE VERIFICATION.

### R5. MAJOR. IPO machinery object drifted twice. The AR's reason for the change contradicts the prospectus.
- Prospectus: Rs 1,302.67 lakh for machinery (VPD plant, transformer test system, tan delta set). The machinery is "to be installed at the existing manufacturing unit... Plot No. E-11". Free area 1,424.11 sq m against 700 sq m required (Prospectus L5361, L5468-5496, printed p.66-68). The prospectus also placed the 220 kV / 315 MVA capability "at our existing facility" (Prospectus L8472-8473).
- Call, 1-Jun-26: Kanishk Agarwal asked about tangible benefits from the machinery investment (Tr. L286-287). Pradeep moved to the IPO fund. Nitin: "for the plant and machinery, it is still in there... we will utilize those funds towards the purchase of new machinery for the new plant only" (Tr. L290-299 [p7-p8]). That already departs from the existing-unit object. No analyst challenged it.
- Board, 3-Sep-26: Rs 700 lakh moved from machinery to "Construction of building/civil structure... and expansion of plant capacity" (20260903-0bf73e52 L56-79). That is 53.7% of the object (calc).
- AR explanatory statement: machinery 0.00% used to 2-Sep-26. Reason: "effective and optimum use of such machinery and equipment is contingent upon the Company first establishing adequate built-up space" (AR p.50-51, L1394-1453). The prospectus said the existing unit had twice the free space the machinery needed.
- A shareholder exit offer applies if dissent reaches 10% (AR p.52, L1500-1504). The variation needs a special resolution.

### R6. MAJOR. Full pass-through claimed. No word on the oil price spike. Peers and the company's own AR say otherwise.
- Call: on pricing power, Pradeep says "Yes you can say" (Tr. L317), and then describes pass-through, not pricing power. "We are confident on this, we will not lose anything into the price variation" (Tr. L449-450 [p11]). Orders delivered within 3 months are fixed price (Tr. L321-322, L326-328). Oil is mentioned only as availability: "there is a cut at the procurement side" (Tr. L400-401 [p10]).
- Peers, three to four weeks before the call: Shilchar, "oil prices have become almost double... February till today... almost 100%", other commodities +10-25% (S-M26 L318-320). Danish, "in transformer oil there is an 100% plus rise"; firm-price orders "are having some impact" (D-M26 L569-577, L599-600). After the call: Shilchar passed on "about 50-60%" of the rise on in-hand orders (S-A26 L101).
- Company AR: the FY26 net margin fell "primarily due to changes in product mix, increase in operating costs and competitive pricing during the year" (AR p.82, L3114-3116).
- Filed H1 FY27 orders (11-Jun to 29-Sep-26): about Rs 19.4 Cr carry 1-3 month execution (calc, mixed GST basis). Under Accord's own rule these are fixed price. The two wind orders (Rs 36.95 Cr, calc) run 4-5 months, between the fixed and PVC windows the MD described.
- Two readings. A: the book is short-cycle and repriced, so the margin held. B: the fixed-price share took the oil shock, as at peers. Separating observation: H1 FY27 gross margin against FY26 24.1% (B06 names the same test).

### R7. MAJOR. The reason for the revenue decline changed three times.
- Answer 1: customer site delays and a customer dispute with the Maharashtra Government, "not just because of the demand" (Nitin, Tr. L197-211 [p5]).
- Answer 2, to the second analyst who asked: adds "the availability of the transformer oil also... a cut at the procurement side" (Tr. L400-402 [p10]).
- AR: "a calibrated business approach amid evolving market conditions" (AR p.81, L3047-3048).
- Thesis weight: the 60-80% FY27 growth is "due to the deferment" (Tr. L251). The explanation of the miss carries the guidance.

### R8. MAJOR. Expansion scope and timeline moved, and sit far inside peer norms.
- Call: land "identified", about 2.50 lakh sq ft, for EHV and in-house sheet metal (Tr. L146-149 [p4]). Ground work "after 2 to 3 months", "6 months minimum" to start manufacturing (Tr. L284-285 [p7]). EHV needs "one technical person... maybe end of February or March" (Tr. L472-474 [p12]).
- Q1 update: "new 5,000 MVA transformer manufacturing facility" (Q1 update L95-96). The scope is 5.55 times the 900.36 MVA base (calc).
- AR: construction "within approximately 9-10 months from the date of approval of the Members" (AR p.51, L1467-1468).
- Peers: 12-18 months from decision to production, on land they already owned, with slips (S-A25 via B06; D-M26 L481-482 via B06). Peers climbed the kV ladder in steps (S-O25 via B06). One EHV hire against a step from 33 kV (Deck L643-644) to EHV is a multi-rung leap.

### R9. MINOR. Analyst insistence: the revenue decline was asked twice.
- Aditya Khetan (Tr. L194-195 [p5]) and Fenil, "despite the strong industry tailwinds" (Tr. L384-387 [p10]).

### R10. MINOR. Customer concentration answer deferred and not delivered.
- "I will get back to you on this on the proper note" (Nitin, Tr. L422-423 [p11]). No later filing carries it. Torrent was 35-40% of FY25. FY26: "six or seven customer... 45%" (Tr. L424-427).

### R11. MINOR. "Rs 31 Cr business" from BESS clients may be the same Rs 31 Cr order that was deferred.
- "In this year also, we achieved about INR31 crores business from this segment" (Pradeep, Tr. L244-245 [p6]) against the Rs 31 Cr deferred order (Tr. L200-201 [p5]). If they are the same, "achieved" describes unbilled work.

### R12. MINOR. Volunteered negative: no pricing power at the lower end.
- "There definitely we have price concern... either we go for the less price, less margin to take the order or... say no" (Pradeep, Tr. L348-350 [p9]).

### R13. MINOR. Reputational claim about a named listed peer.
- "Voltamp earlier was manufacturing few transformers from our factory" (Pradeep, Tr. L366-367 [p9]). No filed contract. PENDING LIVE VERIFICATION.

### R14. MINOR. Rs 225 Cr of named bids, no outcome disclosed.
- MVVNL bids about Rs 125 Cr of a Rs 356 Cr tender; Torrent about Rs 100 Cr; government quotes "INR200 something crores" (Tr. L140-145 [p4], L311-313 [p8]). No line in the Q1 or H1 updates. No order filing from either buyer.

### R15. MINOR. Margin defence by moving to state tenders. Both peers avoid that channel.
- "That is the reason we are moving into the tender-based projects like government projects" (Pradeep, Tr. L309-312 [p8]).
- Danish: government discom work "very, very minimum... We face issues with respect to some payment delays" (D-N25 L1409-1417). Shilchar: "we won't be doing any business with any state utility companies" (S-A26 L122).

### R16. MINOR. The balance sheet shows a small footprint for 25 manufactured sets worth Rs 21-22 Cr. [INFERENCE]
- Claim: "Out of 35, we have manufactured around 25 sets, which is valuing around INR21 crores or INR22 crores" (Nitin, Tr. L202-203 [p5]).
- AR Note 14 at 31-Mar-26: finished goods 329.07 lakh, WIP 820.94 lakh, stock in transit 619.50 lakh (new line), raw material 665.36 lakh (AR L4412-4416). FG plus WIP fell from 1,178.68 to 1,150.01 lakh (calc); the P&L change in inventories is +28.67 lakh (AR L3803).
- Reading A: the sets sit in WIP and transit at cost, about Rs 15.1 Cr at the FY26 material ratio of 70.4% (calc, AR L3801 over L3797). That would use nearly all of the WIP and transit for one order. Reading B: "manufactured" overstates completion. Separating observation: the 30-Sep-26 inventory note in the H1 FY27 results, and whether the customer appears on a dispatch.

### R17. MINOR. Siemens is a "partner" in the deck and a competitor on the call.
- Deck: "Partnerships with Schneider Electric, Siemens (Germany), and Lucy Electric (England)" (Deck L1569-1574). The prospectus summary repeats it (Prospectus L8524). The prospectus detail names only SGB-SMIT GmbH, which has "expressed mutual interest in engaging in discussions" (Prospectus L8994-8999).
- Call: Siemens and ABB named as competitors (Tr. L346, L351 [p9]).

### R18. MINOR. Global presence claimed. FX earnings are nil.
- Q1 update: "Pan India & Global (Middle East, USA, Africa & Asia)" (Q1 update L83). AR: "expanding into international markets, including the Middle East, the USA, Africa and Asia" (AR p.80, L2992-2993); "expanded internationally through a MoU" (AR L1685). Deck: "1000+ Clients served over the world" (Deck L449-451).
- AR: Foreign Exchange Earnings Nil for FY26 and FY25 (AR L2609-2613). Prospectus: "we do not have any export operations" (Prospectus L9065-9069).

### R19. MINOR. PGCIL approval, Schneider and Lucy partnerships: listed in the deck, left out of the call.
- The call listed approvals (MVVNL, DHBVNL, UGVNL, Toyota, SMC-C) (Tr. L136-139 [p4]). It did not name PGCIL, which the same-day deck lists (Deck L533-543) and the Q1 update repeats (Q1 update L102-103).
- The deck rates power transformers "up to 33KV" (Deck L643-644). Shilchar, a 132 kV maker, says it will seek PGCIL approval only once its 220 kV plant is ready (S-M26 L329-335). Scope of Accord's PGCIL approval: PENDING LIVE VERIFICATION.

### R20. MINOR. The Moscow counterparty is named three ways. Sanctions are not addressed.
- "Western Administrative District of Moscow" (Tr. L152-153 [p4]); "Industrial Federation of Industrial Moscow" (Tr. L537 [p13]); "Federation of Moscow" (Tr. L548 [p14]). Filings use the first name (Q1 update L93-94; AR L3017-3018).
- The prospectus risk factors name sanctions on Russia (Prospectus L2988-2989). The call did not address them. No revenue was given: "until the approval comes from the Federation, the final data will not come" (Tr. L598-600 [p15]).

### R21. MINOR. Filing hygiene.
- Accord's 23-May-26 order filing states "Gabion Technologies India Limited has received multiple routine work/supply orders" (20260523 L34-35).
- The pre-listing CIN "U31500..." appears on post-listing filings (20260523 L7; 20260611 L61; 20260624 L61; 20260803 L64). The listed CIN is "L31500..." (Tr. L7).
- The 24-Jun-26 filing names "Sunsure Energy Private Limited (Refer Note)" under a note that says the name cannot be disclosed (20260624 L77-85).

### R22. MINOR. AR MD&A narrative contradicts its own ratio table.
- Table: receivables turnover 4.48 to 3.22, "a relatively slower conversion" (AR p.82, L3102-3106). Narrative: "The improvement in receivables turnover indicates better working capital management" (AR p.83, L3128).
- DSCR 0.81 (AR p.82, L3091), described as "comfortable debt servicing capability" (AR p.83, L3127-3128).

### R23. MINOR. Superlative claim on the CPRI test.
- The 17.60 MVA inverter duty transformer is "the highest rating in the transformer industry for the renewable segment" (Pradeep, Tr. L123-125 [p4]). Filings say only that the test was completed (Q1 update L91-92; AR L3009-3011). PENDING LIVE VERIFICATION.

## 2. Comparison against the pipeline (B05, B06)

| # | Sev | Item | Status | Pipeline location | Note |
|---|---|---|---|---|---|
| R1 | MAJOR | FY26 called growth and better profit; all filed lines fell | PARTIALLY CAUGHT | B05 2C "Over-promotion" cites "strong execution capabilities against a revenue decline year" (L179-181) | B05 does not record "improved profitability" (L162-163), the FY25 margin of 11.68%, the H2 declines, the H2-to-full-year deflection, or the accepted false premise. Not in B05 4D. |
| R2 | MAJOR | Guidance has two forms | CAUGHT | B05 0.1, 4D HIGH, flag LBF-1-GUIDANCE-INCONSISTENT; B06 LBF-1 check | Correctly weighted. |
| R3 | MAJOR | Capacity irreconcilable; MVA dodge | CAUGHT | B05 2C, 2E(c), 3C, 4D HIGH, CAPACITY-IRRECONCILABLE; B06 Q3 | B05 has not noted that the same call-day deck states both 1,200+ and 900.36 MVA (Deck L454-456, L867-878). Not a status change. |
| R4 | MAJOR | NHEV Rs 1,600 Cr, LOI not filed | CAUGHT | B05 0.1, 3C, 4D HIGH, NHEV-NOT-FILED | Scale check (Rs 3.56 Cr per station vs about Rs 0.25 Cr per filed CSS unit, calc) is new support. |
| R5 | MAJOR | IPO machinery object drift; AR reason contradicts prospectus | PARTIALLY CAUGHT | B05 2A P9 (PARTIAL), timeline_slippages, 2D | B05 scores it as a partly delivered promise. It misses that the call promise already departed from the prospectus (existing E-11 unit, 1,424.11 sq m free vs 700 needed) and that the AR's built-up-space reason contradicts the offer document. Not in B05 4D. |
| R6 | MAJOR | Full pass-through claimed; oil spike unmentioned | PARTIALLY CAUGHT | B06 Q1, Q2, 2A, 2B, PVC-SHARE-OUTLIER, cross_peer_hypothesis; B05 3C | B06 catches the peer contradiction. Neither catches the AR's own "competitive pricing" admission (AR p.82) or that about Rs 19.4 Cr of filed H1 orders sit in Accord's own fixed-price window (calc). B06 Q5 files Accord's oil remark as "VERIFIED"; on a price shock the call is silent, not verified. |
| R7 | MAJOR | Three explanations for the revenue miss | CAUGHT | B05 2B (call, oil, AR "calibrated"), 2E(a) | Correctly classed as external blame plus deflection. |
| R8 | MAJOR | Expansion relabelled; timeline inside peer norms | CAUGHT | B05 1C, 2A P6, 4D MEDIUM, timeline_slippages; B06 Q8 CONTRADICTED, PEER-TIMELINE-CONTRADICTION | B06 weights it well. |
| R9 | MINOR | Revenue decline asked twice | CAUGHT | B05 2E(a) | |
| R10 | MINOR | Concentration note never delivered | CAUGHT | B05 2A P8 MISSED, 4D | |
| R11 | MINOR | BESS Rs 31 Cr may be the deferred order | CAUGHT | B05 3D, analyst_note (4) | |
| R12 | MINOR | Lower-end price concern | CAUGHT | B05 3A | |
| R13 | MINOR | Voltamp contract-manufacture claim | CAUGHT | B05 3A; B06 Q7 UNVERIFIABLE | |
| R14 | MINOR | Rs 225 Cr bids, no outcome | CAUGHT | B05 2A P7, 4D MEDIUM, TENDER-SILENCE | B05 grades MEDIUM. I grade MINOR: an undisclosed bid outcome does not breach a filing rule. |
| R15 | MINOR | State-tender pivot vs peer avoidance | CAUGHT | B06 Q6, PEER-CHANNEL-AVOIDANCE | Anchor D-N25 L1409-1417 re-read: holds. |
| R16 | MINOR | Deferred-order footprint vs inventory note | MISSED | none | [INFERENCE]; two readings stated. |
| R17 | MINOR | Siemens partner vs competitor | MISSED | none | |
| R18 | MINOR | Global presence vs nil FX earnings | PARTIALLY CAUGHT | B05 3D notes "nil FX earnings" | The claim inflation itself is not flagged. |
| R19 | MINOR | PGCIL, Schneider, Lucy left out of the call; PGCIL scope | PARTIALLY CAUGHT | B05 1C NEW row | B05 says these "appeared in July". The call-day deck already lists all three (see section 3). |
| R20 | MINOR | Moscow counterparty named three ways; sanctions | PARTIALLY CAUGHT | B05 1A T10, 3C, 4A row 8 | Aspirational status caught. Naming and sanctions not caught. |
| R21 | MINOR | Filing hygiene (Gabion, old CIN, Sunsure note) | MISSED | none | B05 cites a different feed error (Tipco, via B00). |
| R22 | MINOR | AR narrative contradicts its ratio table | PARTIALLY CAUGHT | B05 4C "AR narrative (B03 P4 near RED)" | Specific contradictions not recorded. |
| R23 | MINOR | CPRI "highest rating" superlative | MISSED | B05 1A T11 records the test as committed fact | |

Totals: 23 listed. CAUGHT 12. PARTIALLY CAUGHT 7. MISSED 4, all MINOR.
Material subset (8 MAJOR): CAUGHT 5 (R2, R3, R4, R7, R8). PARTIALLY CAUGHT 3 (R1, R5, R6). MISSED 0.

## 3. Pipeline red flags not on my independent list

| Pipeline flag | Assessment | Evidence |
|---|---|---|
| B05 ORDER-FILING-GAP and 4D MEDIUM: "~Rs 17 Cr of Aditya Birla orders not filed [INFERENCE]". Repeated in B06 Part 2E item 8 ("It does not explain the named Aditya Birla order... one order") and in the B06 analyst_note ("conversion and unfiled orders... are the weak point") | NOT SUPPORTED. MAJOR (rule 5). | The 29-Jun-26 filing: Rs 19.97 Cr including GST, 3.6 MVA wind turbine transformers, "Leading Private Sector EPC company", "within 5 Months" (20260629-order19.97Cr L84, L94-97, L102-107). Ex GST that is Rs 16.93 Cr (calc). The 23-Sep-26 LOA: Rs 20.02 Cr ex GST, 57 wind turbine transformers of 3.6 and 5.5 MVA for Aditya Birla Renewables, the same EPC descriptor, 4-5 months (20260923-d54c506f L91, L99-111). Sum Rs 36.95 Cr (calc) against "orders worth Rs 37 crore for Aditya Birla projects, excluding GST... 119 transformers... four to five months" (H1 update L78-80). B05 listed the 29-Jun order itself but added it at the GST-inclusive figure and did not test it against the Aditya Birla balance. The valid residue: the June filing did not name the end project owner. Separating observation: the end client of the Gadag-1 order. |
| B05 1C "NEW" row: Schneider and Lucy partnerships and PGCIL approval "absent when the call listed approvals 2 months earlier: question why they appeared in July" | OVERSTATED. MINOR. | All three are in the 1-Jun-26 call-day deck (Deck L515-543). Schneider and Lucy are in the prospectus (Prospectus L9012-9036). They did not appear in July. The valid residue is R19: management left them out of its spoken list. |
| B05 4D MEDIUM: customer names withheld on the largest order filings | SUPPORTED | 20260523 L78-80; 20260611 L131-133; 20260629 L77-79; 20260923-d54c506f L85-91; 20260929 L95 ("Private Sector Electrical Company", Rs 8.39 Cr). |
| B05 4D MEDIUM (part): land 12.6% under the call figure | SUPPORTED | 20,300 sq m = 2.185 lakh sq ft (calc) against "approximately 2.50 lakh" (Tr. L146-147). Low weight: the call said "approximately". |
| B05 4D LOW: FY26 total income 70.60 (call) vs 70.36 | SUPPORTED | AR p.55, L1653: 7,035.71 lakh. Call: "INR70.60 crores" (Tr. L163). |
| B05 4D LOW: segment percentages loose | SUPPORTED | Tr. L406-413 against AR p.81 L3055-3058 (transformer 82.7%, CSS and PSS 11.3%). |
| B06 PEER-CAPACITY-CEILING-GAP | SUPPORTED in direction | Peer per-MVA statements re-read in S-M26 L472 and D-M26 context. The data-sheet arithmetic belongs to Verifier A. |
| B06 LBF-1-SEASONALITY-CHECK | SUPPORTED | 52.68 / 0.381 = 138.3 and 52.68 / 0.506 = 104.1 (calc). Peer H1 shares belong to Verifier A. |
| B06 DEFERRAL-SIZE-OUTLIER | SUPPORTED | Shilchar March export shortfall Rs 35-40 Cr (S-M26 L253-255). |
| B06 RECEIVABLE-PRECEDENT | SUPPORTED in direction | Data-sheet tier. Not testable against transcripts. Numbers belong to Verifier A. |
| B06 PEER-MARGIN-SHOCK | SUPPORTED | S-M26 L218-227 ("7% to 8% kind of a hit"); S-A26 L83-88. |
| B06 PVC-SHARE-OUTLIER | SUPPORTED, basis note | Accord's "100%" applies to orders beyond 3 months (Tr. L329-330). Danish's "around 30%" is the share of its book (D-M26 L342-346). B06 names both bases. The comparison is a lower bound on the risk: under Accord's own rule its short-cycle orders are fixed price (R6). |

## 4. Promise-delivery spot checks (B05 2A)

| Row | Promise in the call? | Outcome in the later record? | Direction |
|---|---|---|---|
| P1 land, ~2.50 lakh sq ft | Yes, "identified land... approximately 2.50 lakh square feet" (Tr. L146-147) | Yes. 20,300 sq m bought for Rs 8.85 Cr plus Rs 1.82 Cr (20260703 L32-35, L118, L123) | CONFIRMED (DELIVERED) |
| P2 order book ~Rs 156 Cr | Yes, "approximately INR156 crores as of May 25, 2026" (Tr. L149-151) | Yes. Rs 159 Cr at 22-Jul (Q1 update L77); Rs 173 Cr at 30-Sep, inflow Rs 77 Cr (H1 update L70-71, L81) | CONFIRMED. Note: this is a status fact, not a promise. |
| P6 expansion: ground work 2-3 months, manufacturing 6 months minimum | Yes (Tr. L284-285) | Board reallocation 3-Sep (20260903 L56-79); build 9-10 months from AGM approval (AR p.51, L1467-1468) | CONFIRMED (PARTIAL, slipping) |
| P7 MVVNL and Torrent bids to open Jun / early Jul | Yes (Tr. L140-145) | No line in the Q1 update (L76-110) or the H1 update (L65-90). No order filing from either buyer | CONFIRMED in direction. Label caveat: the call promised a bid opening, not a win. "MISSED" here means "no outcome disclosed". |
| P9 IPO machinery funds "for the new plant only" | Yes (Tr. L290-299) | Rs 700 lakh moved to civil works; machinery 0.00% used to 2-Sep-26 (AR p.50-51, L1394-1406; 20260903 L56-79) | CONFIRMED (PARTIAL; Rs 602.67 lakh stays on machinery). The promise itself departed from the prospectus (R5). |

Checked 5. Confirmed 5. Wrong 0.

## 5. Credibility grade (B05: C)

Would grade lower: D.
- For D: the opening remarks misstated the year (R1). A Rs 1,600 Cr LOI claim was made on the call and never filed (R4). B05 explicitly keeps it out of the grade, but an unfiled claim of that size is credibility evidence. The IPO-variation reason contradicts the offer document seven months after listing (R5). The same-day deck carries two capacity figures (R3). The two guidance forms do not agree (R2). Global presence is claimed with nil FX earnings (R18). The delivered items (land, order book) are facts the company controls.
- For C: H1 FY27 revenue rose 90.07% (H1 update L66-67). The order book grew to Rs 173 Cr. Management admitted lower-end price pressure and declined BESS for a stated channel reason (R12; Tr. L242-247).
- Separating observation: the H1 FY27 results (due Nov-26). If the H1 EBITDA margin, gross margin and inventory note reconcile with the call's pass-through and deferral claims (R6, R16), C stands. If not, D.

## 6. Consolidated findings

| Sev | Location | Finding | Status |
|---|---|---|---|
| MAJOR | B05 2C, 4D | R1. FY26 called "steady growth and improved profitability"; filed revenue -11.3%, PAT -24.2%, EBITDA margin 11.68% to 10.39%, H2 revenue -26.4%, H2 PAT -40.3% (calc); H2 question answered with the smaller full-year gap; false margin premise accepted | PARTIALLY CAUGHT |
| MAJOR | B05 2A P9 | R5. Prospectus placed the machinery in the existing unit with free space; call said "new plant only"; AR says the machinery needs new built-up space first; Rs 700 lakh (53.7%) moved, 0.00% spent | PARTIALLY CAUGHT |
| MAJOR | B06 Q1, Q5, 2B; B05 3C | R6. "Will not lose anything into the price variation" and silence on the oil price spike, against two peers and the AR's own "competitive pricing"; about Rs 19.4 Cr of filed H1 orders in the fixed-price window (calc) | PARTIALLY CAUGHT |
| MAJOR | B05 ORDER-FILING-GAP, 4D; B06 2E item 8, analyst_note | Aditya Birla "~Rs 17 Cr not filed" is contradicted by the 29-Jun-26 filing (Rs 16.93 Cr ex GST, calc), which closes the Rs 37 Cr to within Rs 0.05 Cr | NOT SUPPORTED |
| MINOR | none | R16. Deferred-order footprint vs inventory note [INFERENCE] | MISSED |
| MINOR | none | R17. Siemens partner vs competitor | MISSED |
| MINOR | none | R21. Filing hygiene: Gabion named as recipient, old CIN, Sunsure note | MISSED |
| MINOR | B05 1A T11 | R23. CPRI "highest rating" superlative | MISSED |
| MINOR | B05 3D | R18. Global presence claim vs nil FX earnings and "no export operations" | PARTIALLY CAUGHT |
| MINOR | B05 1C | R19 plus OVERSTATED B05 1C timing: the items were in the call-day deck; PGCIL scope for a 33 kV maker unverified | PARTIALLY CAUGHT |
| MINOR | B05 1A T10, 4A | R20. Moscow counterparty named three ways; sanctions not addressed | PARTIALLY CAUGHT |
| MINOR | B05 4C | R22. AR narrative contradicts its ratio table (receivables, DSCR 0.81) | PARTIALLY CAUGHT |

Finding rows: CRITICAL 0, MAJOR 4, MINOR 8.

Scoring (rules 6 and 7): material items found 8, all MAJOR. Material caught in full 5. Material partially caught 3. Material missed 0. The denominator is 8, so the rate applies. Strict rule used: only full catches count as caught. acceptance_rate = 5 / 8 = 62.5%. If partials counted as caught, the rate would be 8 / 8 = 100%. The strict figure is reported.

```yaml
stage: B12b
company: "ACCORD"
run_date: "2026-10-06"
model: "claude-opus-5-5"  # must equal .claude/agents frontmatter; the orchestrator compares it
status: complete
independent_flags_found: 23
caught: 12
partially_caught: 7
missed:
  - {severity: "MINOR", item: "R16 Deferred-order footprint: 25 of 35 sets 'manufactured' worth Rs 21-22 Cr, but FG+WIP fell from 1,178.68 to 1,150.01 lakh at 31-Mar-26; fits only if WIP plus new stock in transit (619.50 lakh) is nearly all this one order [INFERENCE]", anchor: "Tr. L202-203 (Nitin Gupta); AR Note 14 L4412-4416; AR P&L L3803"}
  - {severity: "MINOR", item: "R17 Siemens called a partner in the deck and prospectus summary, a competitor on the call; prospectus detail shows only SGB-SMIT 'expressed mutual interest'", anchor: "Deck L1569-1574; Prospectus L8524, L8994-8999; Tr. L346, L351 (Pradeep Verma)"}
  - {severity: "MINOR", item: "R21 Filing hygiene: 23-May-26 filing says 'Gabion Technologies India Limited has received' the orders; pre-listing CIN U31500 on four post-listing filings; 24-Jun-26 filing names Sunsure under a name-withheld note", anchor: "20260523 L7, L34-35; 20260611 L61; 20260624 L61, L77-85; 20260803 L64"}
  - {severity: "MINOR", item: "R23 Superlative: 17.60 MVA inverter duty transformer is 'the highest rating in the transformer industry for the renewable segment'; PENDING LIVE VERIFICATION", anchor: "Tr. L123-125 (Pradeep Verma)"}
pipeline_flags_not_supported:
  - "NOT SUPPORTED (MAJOR): B05 ORDER-FILING-GAP and 4D MEDIUM, repeated in B06 Part 2E item 8 and analyst_note: '~Rs 17 Cr of Aditya Birla orders not filed'. The 29-Jun-26 filing (Rs 19.97 Cr incl GST = Rs 16.93 Cr ex GST, calc; 3.6 MVA wind turbine transformers; 'Leading Private Sector EPC company'; 5 months; 20260629 L84, L94-107) plus the 23-Sep-26 LOA (Rs 20.02 Cr ex GST; 20260923-d54c506f L91-111) sum to Rs 36.95 Cr against Rs 37 Cr in the H1 update (L78-80). Residue: the June filing did not name the end project owner."
  - "OVERSTATED (MINOR): B05 1C NEW row says Schneider and Lucy partnerships and PGCIL approval 'appeared in July'. All three are in the 1-Jun-26 call-day deck (Deck L515-543); Schneider and Lucy are in the prospectus (L9012-9036). Residue: the call left them out of the spoken approvals list (Tr. L136-139)."
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "lower: D. B05 keeps the unfiled Rs 1,600 Cr NHEV LOI claim out of the grade and misses the FY26 'improved profitability' misstatement and the IPO-variation reason that contradicts the prospectus; delivered items are facts the company controls. C stands only if H1 FY27 results reconcile with the pass-through and deferral claims."
findings:
  - {severity: "MAJOR", location: "B05 2C, 4D", issue: "R1 FY26 called 'steady growth and improved profitability' (Tr. L162-163); filed revenue -11.3%, PAT -24.2%, EBITDA margin 11.68% to 10.39%, H2 revenue -26.4%, H2 PAT -40.3% (calc, Deck L1211-1225, L1243-1248; AR p.55 L1650-1668); H2 question answered with the full-year gap (Tr. L194-197); false margin premise accepted (Tr. L431-435)", status: "PARTIALLY CAUGHT"}
  - {severity: "MAJOR", location: "B05 2A P9, timeline_slippages", issue: "R5 Prospectus put the IPO machinery in the existing E-11 unit with 1,424.11 sq m free vs 700 sq m needed (Prospectus L5468-5496); call said 'for the new plant only' (Tr. L290-299); AR variation reason says machinery needs new built-up space first (AR p.51 L1441-1453); Rs 700 lakh = 53.7% of the object moved (calc), 0.00% of machinery spent (AR p.50 L1394-1396)", status: "PARTIALLY CAUGHT"}
  - {severity: "MAJOR", location: "B06 Q1, Q5, 2B, PVC-SHARE-OUTLIER; B05 3C", issue: "R6 'we will not lose anything into the price variation' (Tr. L449-450) and only an oil availability remark (Tr. L400-401), weeks after Shilchar (S-M26 L318-320) and Danish (D-M26 L569-577, L599-600) reported oil +100% and firm-price hits; AR blames 'competitive pricing' for the FY26 margin fall (AR p.82 L3114-3116); about Rs 19.4 Cr of filed H1 FY27 orders sit in Accord's own fixed-price window (calc, mixed GST)", status: "PARTIALLY CAUGHT"}
  - {severity: "MAJOR", location: "B05 ORDER-FILING-GAP, 4D MEDIUM; B06 Part 2E item 8, analyst_note", issue: "Pipeline flag '~Rs 17 Cr of Aditya Birla orders not filed' is contradicted by the 29-Jun-26 filing (Rs 16.93 Cr ex GST, calc), which closes the Rs 37 Cr H1-update figure to within Rs 0.05 Cr", status: "NOT SUPPORTED"}
  - {severity: "MINOR", location: "not in B05 or B06", issue: "R16 deferred-order footprint vs AR inventory note [INFERENCE]; separating observation: 30-Sep-26 inventory note", status: "MISSED"}
  - {severity: "MINOR", location: "not in B05 or B06", issue: "R17 Siemens labelled partner (Deck L1569-1574; Prospectus L8524) and competitor (Tr. L346, L351)", status: "MISSED"}
  - {severity: "MINOR", location: "not in B05 or B06", issue: "R21 filing hygiene: Gabion named as recipient in Accord's 23-May-26 filing; pre-listing CIN on four filings; Sunsure named under a name-withheld note", status: "MISSED"}
  - {severity: "MINOR", location: "B05 1A T11", issue: "R23 CPRI 'highest rating in the transformer industry' superlative recorded as fact (Tr. L123-125)", status: "MISSED"}
  - {severity: "MINOR", location: "B05 3D", issue: "R18 global presence claimed (Q1 update L83; AR L1685, L2992-2993) against Nil FX earnings FY25-FY26 (AR L2609-2613) and 'no export operations' (Prospectus L9065-9069); claim inflation not flagged", status: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 1C NEW row", issue: "R19 B05 misdates Schneider, Lucy and PGCIL as July items (OVERSTATED); residue: call omitted them; PGCIL scope for a 33 kV maker (Deck L643-644) unverified while Shilchar seeks PGCIL only after its 220 kV plant (S-M26 L329-335)", status: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 1A T10, 4A row 8", issue: "R20 Moscow counterparty named three ways (Tr. L153, L537, L548); Russia sanctions in prospectus risk factors (L2988-2989) not addressed", status: "PARTIALLY CAUGHT"}
  - {severity: "MINOR", location: "B05 4C (via B03)", issue: "R22 AR narrative 'improvement in receivables turnover' and 'comfortable debt servicing' vs its own table: 4.48 to 3.22 and DSCR 0.81 (AR p.82 L3091, L3102-3106; p.83 L3127-3128)", status: "PARTIALLY CAUGHT"}
critical_count: 0
major_count: 4
minor_count: 8
material_found: 8
material_caught: 5
acceptance_rate: 62.5
coverage_basis: "8 material (all MAJOR, 0 CRITICAL) of 23 listed; 5 caught in full, 3 partially caught (R1, R5, R6) and counted as not caught under the strict rule (8 of 8 if partials counted); 0 material missed. One company transcript, so no cross-quarter evasion test ran and no CRITICAL can arise under that rule. critical/major/minor_count count finding rows (12), not list items."
```
