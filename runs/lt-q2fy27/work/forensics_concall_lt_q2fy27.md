# A3 FORENSIC NOTES: Larsen & Toubro (LT) Q2 FY27, doctype CONCALL (ASR machine transcript)

Stage: A3-forensics | Model: claude-opus-5-5 | Date: 2026-10-28
Inputs read: extracted/lt-concall-q2fy27-structured.md (R001-R492, all rows), extracted/lt-concall-q2fy27-fulltext.md (L1-L849, all lines), work/ledger_concall_lt_q2fy27.md (492 IDs + 5 MFS units).
Not read: source audio/transcript, anything under inputs/. No prior-quarter fulltext held (first LT run). No Notion page and no companies/LT.md; this is a PRE-THESIS READ. F17 uses the operator watch list from the task message.

Source caveat: faster-whisper small.en, untagged speakers. Every number below is management-tier and UNVERIFIED as heard. Garbled figures are listed, not repaired. "Derived" marks arithmetic on two heard figures; A4 re-derives from the filed results and deck.

## 1. LEDGER RECONCILIATION

| Item | Count | Read at cited line | Status |
|---|---|---|---|
| Structured rows in ledger (R001-R492) | 492 | 492 | 100% |
| MISSING_FROM_STRUCTURED units (L430, L484, L571, L608, L707) | 5 | 5 | 100% |
| Orphan IDs | 0 | n.a. | none |
| ZERO_STANDING rows | 0 | n.a. | concall, no standing table |

ledger_reconciled_pct = 497 / 497 = 100.

Reconciliation notes (attribution and reading risks found while reading rows at their lines; A4 should not treat these as management claims without care):
- R291 / R292 (L367-L369) are typed QUALIFIER as if management said them. The text opens "Sure, but in terms of execution, we have not seen any major slow down" and the management reply starts at L370 "So let me put it like this". These read as the ANALYST's assertions.
- R394 (L596-L599) is the analyst's statement that there is no margin impact. Management endorsed it only as "Yeah, more or less your understanding is correct." (L600).
- R412 (L623) "You will not bid if they do not get differentiated margin." A1 attributes to analyst. ASR has no tags; it may be management. Attribution unresolved.
- R460 (L754) A1 annotates "PPS (heard; PPM)". The prepared remarks place data centers in "technology platforms and services" (L284-L287). "PPS" more likely means TPS, not PPM. This changes which segment carries the AI capex. Treated as AMBIGUOUS in C-09.
- MFS-2 (L484) "I hope that we break the record again." sits in the same answer that later guides NWC moderation (L493-L494). Speaker is not identifiable.

ASR garble register (load-bearing numbers that look misheard; NOT repaired):
| Line | Heard | Problem |
|---|---|---|
| L138 (R103) | "The share of private sector orders increased by Rs 1.7 trillion." | Rupee figure where a share is expected; L140 gives 39% from 30% |
| L147 (R110) | "The PSU exposure remains largely stable at 31." | No unit |
| L159 (R121/R122) | "In Russia revenue contributed to 58% of the total revenues" | "In Russia" likely another word; segment of 58% unknown |
| L231 (R190) | "carbon right solutions at rupees 0.71" | Unit dropped |
| L426-L427 (R313/R314) | "60 percent 60 percent all will be on the menu. 50% could be under the new one." | Share of hydrocarbon book below threshold unclear |
| L559 vs L564 (R379/R382) | "around 12 to 30 percent" then "10 to 12 percent" | Domestic NWC intensity stated two ways |
| L780 (R471) | "solid at 15-15%" | Analyst core growth figure garbled |

Internal arithmetic checks on heard figures (all tie, so the order book block looks cleanly heard): segment order book shares 42/34/17/5/2 sum to 100 and match the rupee figures (3.61, 2.87, 1.436, 0.429, 0.184 of 8.54 trn); international 54% of 8.54 trn = 4.61 trn vs 4.62 heard; prospects 5.84+2.07+2.04+0.33 = 10.28 trn vs 10.3 heard; energy green order book 703+168+565 = 1,436 bn; domestic book 39% private + 30% central/state + 31 PSU = 100.

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| C-01 | F6 | R256, R257, R261, R262, R263 | L313, L319-L320 | "robust 22 percent" (L313); "achieving our order-in-flow guidance of 10% to 12% for FI27" (L320) | FORWARD-SIGNAL | Inflow guidance held, not raised, after H1 group inflow +22%. If the guide is group-level, H2 inflow growth must run below 10-12% to land inside it. Either H2 decelerates sharply or the guide is conservative. Guide basis (group vs PPM) not stated on the call. |
| C-02 | F6 | R080, R083, R084, R085, R086, R192, R194, R214, R215 | L126-L128, L260 | "is for 2.07 trillion vis-a-vis rupees 3.35 trillion last year" (L127); "rupees 2.04 trillion as compared to 0.93 trillion last year" (L128) | FORWARD-SIGNAL | Pipeline is flat (10.3 trn) only through mix. Energy conventional prospects fell 38% YoY (derived), the segment that drove the record Q2 inflow. Energy green doubled, and solar EPC is 1.47 of 2.04 trn (72%, derived), the line being deferred in the Middle East (C-14). H2 inflow now leans on the deferral-prone line. |
| C-03 | F6 | R268, R270, R339, R390, R391, R392 | L490-L492, L592-L595 | "the target revenue that we are talking about is quite a tall ask or steep ask for" (L491); "we are still maintaining the revenue guidance of 10 to 12 percent" (L592-L593) | AMBIGUOUS | Q2 PPM revenue +20% and group +16%, yet FY27 10-12% is kept "because" of Middle East supply chain disruption (L593-L595), and H2 is called a "steep ask". Two readings: H2 seasonality makes the absolute H2 number hard, or management expects logistics to cut H2 growth below the band. Basis of the revenue guide (group vs PPM) unstated. |
| C-04 | F6 | R131, R132, R133, R271, R272, R273 | L169, L331-L332 | "AVIDTA margin for Q2FI 27 was at 7% and declined by 30 basis points" (L169); "we are reasonably confident of meeting our EBITDA margin target of 7.8 percent for F527" (L332) | FORWARD-SIGNAL | Q2 PPM margin 7% heard vs FY27 target 7.8%. H2 must run above 7.8% if H1 is near 7% (H1 margin not stated on call). The hedge grade drops from "confident" (inflow L319, revenue L329) to "reasonably confident" for margin, and the margin is tied "in line with our revenue growth guidance" (L331). Margin is the weakest-held guide. |
| C-05 | F6 | R140, R142, R143, R144, R145, R275, R276, R277, R278, R336, R337, R340, R341, R343, MFS-2 | L182-L186, L336-L338, L486, L493-L494 | "along with customer advances received against the recently secured large orders" (L185-L186); "this could have some amount of toning down or you know moderating the overall working capital trend" (L493-L494) | FORWARD-SIGNAL | The only guidance change on the call: NWC now "below our earlier guidance of 10%" (L337-L338). The 1.7% record (4.1% in March) rests partly on advances against large new orders; PPM NWC is "negative 4 percent" (L486). Advances unwind as those orders execute, and management already guides H2 moderation. Treat 1.7% as a float peak, not a run-rate. |
| C-06 | F6 | R135, R136, R137 | L173-L176 | "coupled with higher treasury income supported by the release of funds through improved working capital management within the PPM portfolio" (L175-L176) | FORWARD-SIGNAL | Group PAT +33% (Rs 52 bn heard) is attributed in part to treasury income on the advance float. If NWC moderates (C-05), that income support shrinks. Treasury income amount not stated on the call. PAT growth quality question. |
| C-07 | F6 | R057, R058, R059, R060, R061, R062, R063, R064 | L108-L112 | "The expected completion date for this transaction has been revised from September 30th to December 31st, 2026." (L111-L112) | FORWARD-SIGNAL | Hyderabad Metro (L&T Metro Rail Hyderabad Ltd) divestment to the Telangana-owned HMRL slipped one quarter. No reason, no consideration, no conditions precedent stated. Deconsolidation and the ROE lift management links to exiting it (L768-L770) move out with it. First recorded slip; track for a second. |
| C-08 | F6 | R133, R181, R202, R312, R313, R314, R315, R316, MFS-1 | L172-L173, L221-L222, L248-L249, L426-L430 | "achieve that threshold maybe in the next, in the Q4 part of it." (L428-L429); "Yeah, Q4 and beyond." (L430) | FORWARD-SIGNAL | Three segments cite jobs below the margin recognition threshold: PPM (L172), infra (L222), carbon lite (L248-L249). For hydrocarbon a large share of the book (figure garbled, "60 percent ... 50%") crosses it "maybe" in Q4 "and beyond". The 7.8% margin target depends on this timing. A slip past Q4 moves margin into FY28. |
| C-09 | F6 | R037, R041, R345-R367, R460 | L506-L508, L515, L521, L525-L528, L754 | "this is close to maybe around 750 million US dollars" (L507); "So 100 megawatts plus is what we are looking for in the next one and a half to two years." (L515); "the data center investment is coming under our PPS segment" (L754) | AMBIGUOUS | AI capex: USD 750 m for 10,000 GPUs on the existing 30 MW, then 70 MW more in 1.5-2 years funded by "a combination of taking a new debt" (L521). The analyst's USD 1.8 bn for the balance was not confirmed or denied ("it is not right to mention that", L527). Segment home unclear: A1 reads "PPS" as PPM, but L284-L287 put data centers in Technology Platforms and Services. Size, funding and segment all need confirming. |
| C-10 | F6 | R317, R318, R321, R322, R421-R430 | L444-L447, L641-L649, L654-L655 | "Possibly in the most likely by the end of this year." (L447); "too early to comment on the timelines" (L654-L655) | AMBIGUOUS | Defence conversion is stacked with hedges ("hopefully", "possibly", "most likely"). "This year" may mean calendar 2026 or FY27. The AMCA bid date was given as "month end", "October end" and "End of this week" (L641-L649). Treat defence inflow as unscheduled. |
| C-11 | F6 | R025-R029, R402-R411, MFS-4 | L614-L622 | "range of 6 to 7 billion US dollars over the next 4 or 5 years" (L616); "6 to 7 billion over the next 3 to 4 years, for hydrocarbons from Umar" (L621-L622) | AMBIGUOUS | The PDO (Oman) framework opportunity horizon is stated two ways within one answer. L&T is one of four contractors (Egyptian, Chinese, Korean peers, L617-L618), and management calls it a "right to bid" that "depends on how well we are placed" (L619-L620). This is addressable opportunity, not booked share. |
| C-12 | F6 | R417, R419, R420, R463-R468, R484-R487 | L759-L770, L823-L829 | "almost touching a one lakh crore" (L824); "this is not going to be dilutive of the L&T ROE" (L767-L768) | AMBIGUOUS | About Rs 1 lakh crore of cash and temporary surplus heard. Part of it goes to Lakshya 31 investments (data centers, green energy, equity share), with the claim that take-or-pay makes them ROE-safe. The 2026 analyst challenge cites past development-asset trouble (L749-L750). Deployment pace and leverage at the subsidiary level are not quantified. |
| C-13 | F6 | R041, R042, R053, R054, R055, R369, R371, R372 | L86, L102, L105-L106, L534-L535 | "The commissioning is targeted in January 27th." (L86); "commercial production scheduled to commence in Q3 FI27" (L105-L106); "the next one or two quarters this business also we will see revenue traction" (L534-L535) | NEUTRAL-FACT | Three dated milestones for the Role 5 tracker: AI factory commissioning January 2027 (heard "January 27th"), EV traction motor production Q3 FY27, semiconductor revenue traction in one or two quarters. Each is a promise-vs-delivery test next quarter. |
| C-14 | F7 | R207, R208, R209, R258, R285-R290, R306-R309, R327, R329, R437, R438, R439 | L255-L256, L365-L366, L417-L419, L668-L677 | "declining 45% Y on Y, primarily due to deferrals of certain solar projects in the Middle East" (L255-L256); "If not, there could be some shortfall on that particular business." (L419) | FORWARD-SIGNAL | Middle East solar carries the biggest named hit: "significant impact" (L668), modules from China, revenue deferment, a possible shortfall, materials that "may be delayed" (L674-L676). The H2 inflow recovery rests on "hope" and "hopefully" (L358, L365). Energy green order book is Rs 1,436 bn, of which solar is Rs 703 bn. Expect H2 green revenue and inflow risk. |
| C-15 | F7 | R442, R444, R445, R446, R447, R448, MFS-5 | L697-L709 | "it has to cross the state of Hormuz." (L699); "now we are exploring possibility to move the balance." (L703-L704); "Maybe there will be some delay," (L707) | FORWARD-SIGNAL | Hydrocarbon output fabricated in Oman yards must transit Hormuz. One large consignment moved; the balance is still being "explored". Management cites "70% of the pre-war barrels" moving, "though it is not publicly declared" (L701-L702), so the claim cannot be checked. A delayed module delays site milestones, billing and the threshold crossing in C-08. Middle East is 73% of the Rs 4.62 trn international book (about 39% of the total book, derived). |
| C-16 | F7 | R432, R433, R434, R445 | L662-L664 vs L697-L699 | "the least impact is on hydrocarbon ... or it is getting done in yards which are not affected by this logistic." (L662-L664) | AMBIGUOUS | Internal contradiction. One answer says the yards are not affected. The next says yard output from Oman "has to cross the state of Hormuz". Which hydrocarbon projects need a Hormuz transit, and what value of modules is still waiting? |
| C-17 | F7 | R304, R306, R330, R331, R332, R394, R396 | L412-L416, L476-L481, L596-L600 | "We are very hopeful that a good part of it will get compensated by the customer." (L478); "there could be a bit of a timing issue" (L479-L480); "Yeah, more or less your understanding is correct." (L600) | AMBIGUOUS | Logistics and insurance costs show "fast escalation" (L476). L&T is paying some of them now and "agreeing to get that reimbursed" (L414). Recovery is hoped for, not agreed, with a timing gap. Management still endorsed the analyst's "no margin impact" reading. Lean bear: unagreed reimbursement claims are a margin and receivable risk if customers do not pay. |
| C-18 | F7 | R158, R159, R176, R179, R180, R181, R453, R455, R456 | L199-L200, L213, L218-L222, L738-L743 | "our ability to convert into actionable claims from the customers will take time." (L741); "Until then, this segment will have some amount of, I would say, execution pressure and margin pressure." (L742-L743) | FORWARD-SIGNAL | Infra is 42% of the order book. In Q2 it showed inflow -13%, revenue +6% and margin 5.7% vs 6.2%. The Middle East T&D business "saw a marginal moderation in the activity level" (L218). WET time and cost overruns need claims that "will take time". Management itself guides continued infra margin pressure. |
| C-19 | F7 | R179, R180, R451 | L729-L730 vs L219-L220 | "The infra margins actually have been moving northward" (L729-L730) | AMBIGUOUS | This contradicts the prepared remarks: infra EBITDA margin 5.7% in Q2 vs 6.2% a year ago (L219-L220). "Northward" may mean sequential or ex-WET (ex-WET would be 40-50 bps better, L736). Ask for the basis. |
| C-20 | F16 | R127, R129, R130, R479, R480 | L165-L166, L808-L812 | "we are maintaining the evidence margin. That is A." (L810); "you don't have to too much scrutinize the growth," (L811) | AMBIGUOUS | The group EBITDA margin excluding other income fell from 10% to 8.7% (L166, L797). In Q&A management called this "maintaining" and asked analysts not to scrutinise the divergence between revenue and EBITDA growth. This frames the margin story differently from the reported figure. Note as a framing data point. |
| C-21 | F16 | R472, R473, R474, R475, R476, R477, R478 | L789-L804 | "you can take around 80 basis points is arising because of the segment related margin compression, but getting compensated to other income" (L801-L803); "the balance 40 to 50 basis points coming at the timing mismatch of cost that we have booked in corporate." (L803-L804) | FORWARD-SIGNAL | Segment and PPM EBITDA include allocated other income (L790-L792). About 80 bps of the 130 bps group drop is segment compression that other income fills. So the reported PPM 7% and the 7.8% target are partly an other-income construct. The 40-50 bps corporate "timing mismatch" implies a reversal that is not dated. Whether the allocation basis is new is unknown. |
| C-22 | F16 | R237-R243 | L293-L295 | "partly offset by a one-time gain on the smart world communications divestment by LTTS." (L294-L295) | FORWARD-SIGNAL | The Technology Platforms segment margin was held up by a one-off LTTS divestment gain. The amount was not stated, and no segment margin figure was given. The cushion drops out next quarter, so tech segment margin optics weaken unless LTM salary and forex pressure eases. |
| C-23 | F16 | R089, R090, R098, R248-R254 | L130, L305-L307 | "reality segment which is now being reported as a separate segment following the segregation from the erstwhile projects and manufacturing portfolio." (L305-L307) | AMBIGUOUS | Realty has been carved out of PPM, while the total order book is quoted "including the reality segment" (L130). Open points: are the PPM comparatives restated, and were the 7.8% PPM margin and 10-12% guides set on the post-segregation basis? |
| C-24 | F15 | R030-R034, R043, R058-R060, R240, R243, R248 | L77-L80, L88-L89, L108-L110, L288-L289, L294-L295 | "is being reorganized under Vyoma AI Limited," (L78); "developed through its Holyon subsidiary LNTN Compute Private Limited" (L80) | NEUTRAL-FACT | Entity changes stated on the call: (1) data center business moving into Vyoma AI Ltd, (2) AI compute in a wholly owned subsidiary (LNTN Compute Pvt Ltd, as heard), (3) L&T Metro Rail Hyderabad Ltd exit pending to 31 Dec 2026, (4) LTTS Smart World & Communications divestment done, (5) L&T Semiconductor Technologies named as a wholly owned subsidiary. A4 verifies against the filed consolidation list. No prior list is held. |
| C-25 | F17 | R237-R247, R469, R472, R473 | L296-L302, L778-L786 | "I will not dwell too much on this segment" (L296); "the detailed results are available in the public domain." (L301-L302) | AMBIGUOUS | Watch item "group vs core split" got a partial answer. Tech (LTM/LTTS) and L&T Finance were waved to public filings: no segment margin, no FS revenue or PAT, no minority-interest split. The Kotak question on core vs group divergence was answered through the other-income bridge (C-21), not a core PAT figure. Silence count 1 (first observed quarter, no prior log). |
| C-26 | F17 | R075, R076, R089-R101, R111, R112 | L120-L121, L130-L136, L148-L149 | "International orders accounted for 62% of the portfolio mix" (L120) | NEUTRAL-FACT | Book-to-bill was not stated, and the Middle East share of INFLOW was not stated (only international 62% of PPM inflow and the Middle East at 73% of the international BOOK). Derived from heard figures, Q2 inflow/revenue is 1.88x group and 2.16x PPM. A4 computes the TTM book-to-bill from filed revenue. |

## 3. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | Concall has no standing financial table. Ledger zero_standing = 0. |
| F2 Standalone vs consolidated decomposition | N.A. | No S-vs-C tables on a concall. The group vs core gap is covered in F17 (C-25). Needs the filed results. |
| F3 Shell-entity detection | N.A. | Needs standalone and consolidated cost lines from the filed results. |
| F4 Unaudited contribution ratio | N.A. | Needs the auditor's Other Matters paragraph. Not on a concall. |
| F5 Going concern / EoM scope | N.A. | No auditor EoM on a concall, and no prior-quarter text held. |
| F6 Forward-commitment phrase mining | FINDING | C-01 to C-13. Lexicon hits include "expected to" (L328, L394, L654), "commenc" (L102, L106, L263), "is being reorganized" (L78), "targeted" (L86), "revised" (L111) and "going to be below" (L487, L497). |
| F7 Hedge phrase mining | FINDING | C-14 to C-19. Lexicon hits: "subject to" (L42, boilerplate), "in discussion" (L413), "exploring" (L703), "could have some amount of toning down" (L493). Non-lexicon timing hedges logged in Section 5. |
| F8 Tax forensics | N.A. | No ETR, deferred tax or prior-year tax figures on the call. Needs the filed results. |
| F9 OCI forensics | N.A. | OCI not discussed. Needs the filed results. |
| F10 Share count and dilution | N.A. | Paid-up capital and EPS not discussed. Needs the filed results. |
| F11 Reserves and net worth tie-out | N.A. | Net worth not stated. Cash of about 1 lakh crore (L824) is not a net worth figure. |
| F12 Segment forensics (assets / liabilities) | N.A. | No segment assets or liabilities on a concall. Segment results are covered under F7 and F16. |
| F13 Board outcome beyond the results | N.A. | No board outcome, AGM or director items on the call. |
| F14 Note drafting inconsistencies | N.A. | No notes or auditor letter on a concall. Spoken-number inconsistencies are logged in the ASR garble register (Section 1), and the PDO horizon one is C-11. |
| F15 Entity list diffs | FINDING | C-24 lists the entity changes stated on the call. The consolidation list itself needs the filed results. No prior list held. |
| F16 Dropped and reframed disclosures | FINDING | C-20 to C-23 cover reframings stated on the call itself: margin framing, the other-income allocation to segments, the one-off cushion and the realty carve-out. Deck-to-deck comparison belongs to the presentation A3. |
| F17 Silence audit | FINDING | C-25 and C-26, plus the What Was NOT Discussed table (Section 6). |

## 4. COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Line / turn | Status word |
|---|---|---|---|---|
| 1 | AI factory (LNTN Compute, over 10,000 NVIDIA B300 GPUs, Chennai) commissioning; together.ai deployment agreement | January 2027 (heard "January 27th") | L81-L86 / T2 | underway ("is establishing") |
| 2 | Data center business reorganised under Vyoma AI Ltd (co-location) | not dated | L77-L80 / T2 | underway ("is being reorganized") |
| 3 | EV traction motors commercial production | Q3 FY27 | L105-L106 / T2 | initiated ("production readiness", "scheduled to commence") |
| 4 | BESS assembly capacity expansion at Kanchipuram (heard "Kanchi Purim") | not dated | L102-L103 / T2 | underway ("commenced") |
| 5 | Hyderabad Metro (L&T Metro Rail Hyderabad Ltd) divestment completion | 31 Dec 2026, revised from 30 Sep 2026 | L108-L112 / T2 | underway, SLIPPED once |
| 6 | FY27 order inflow growth 10-12% | FY27 (Mar 2027) | L319-L320 / T2 | reaffirmed ("confident") |
| 7 | FY27 revenue growth 10-12% | FY27 | L329-L330, L592-L593 / T2, T26 | reaffirmed ("still maintaining") |
| 8 | FY27 PPM EBITDA margin 7.8% | FY27 | L331-L332 / T2 | reaffirmed ("reasonably confident") |
| 9 | FY27 group NWC below 10% (earlier guide 10%) | FY27 | L336-L338, L487-L499 / T2, T18 | revised (improved) |
| 10 | Solar ordering recovery outside India | H2 FY27 (Q3-Q4) | L357-L366, L469-L472 / T4, T14 | expected (hope) |
| 11 | Offshore wind execution pick-up; meaningful FY27 growth vs FY26 | following quarters / FY27 | L327-L328, L404 / T2, T8 | underway |
| 12 | Hydrocarbon jobs cross margin recognition threshold | Q4 FY27 "and beyond" | L428-L430 / T10 | expected ("maybe") |
| 13 | MHI JV profitable on carbon lite order | not dated | L392-L395 / T6 | expected |
| 14 | Defence order conversion | "by the end of this year" (CY26 or FY27 unclear) | L444-L447 / T12 | expected ("possibly") |
| 15 | AMCA bid submission | October-end 2026 ("End of this week") | L641-L649 / T32 | imminent |
| 16 | AI data center capacity 100 MW+ (30+50+30); 50 MW adjoining Chennai site | 1.5-2 years (to about mid-2028) | L511-L524 / T20 | planned ("may be putting up") |
| 17 | Semiconductor revenue traction; selling designs with chips | next 1-2 quarters | L530-L535 / T22 | expected |
| 18 | Logistics and insurance cost compensation from customers | not dated ("timing issue") | L476-L481 / T16 | in discussion |
| 19 | Remaining Oman-yard hydrocarbon consignments through Hormuz | not dated ("maybe some delay") | L697-L709 / T36 | exploring |
| 20 | PDO Oman framework: USD 6-7 bn opportunity | 4-5 years (L616) or 3-4 years (L622) | L614-L622 / T28 | framework signed (right to bid) |
| 21 | T&D Middle East: not much impact in H2 | H2 FY27 | L665-L667 / T34 | expected |
| 22 | Infra claims conversion; margin pressure until then | not dated ("will take time") | L738-L743 / T38 | pending |
| 23 | Green hydrogen/ammonia only with take-or-pay; not ROE-dilutive | not dated | L759-L770 / T40 | policy stated |
| 24 | Realty Lakshya L31 plan (71 m sq ft per analyst) unchanged | L31 horizon | L630-L635 / T30 | unchanged |
| 25 | Cash surplus of about 1 lakh crore partly deployed into L31 investments with subsidiary leverage | not dated | L822-L829 / T44 | policy stated |
| 26 | Working-capital discipline: execution paced to customer payments | ongoing | L830-L836 / T44 | policy stated |

Status-change language: none can be diffed (no prior-quarter transcript). Item 5 is the only explicit date revision. Item 9 is the only explicit guidance revision.

## 5. HEDGE INVENTORY ON EXECUTION TIMING (operator special attention)

| Line | Verbatim | Topic |
|---|---|---|
| L357-L359 | "we hope to pick up momentum in the quarter two and and sorry quarter three and quarter four" | solar ordering |
| L365-L366 | "hopefully I think the ordering momentum for this segment from outside of India will regain traction in the second half" | solar ordering |
| L374-L375 | "Now it needs to be seen depending on the situation how we see the next six months or so." | ME execution |
| L404 | "offshore wind will pick up execution in the following quarters" | offshore wind |
| L417-L419 | "we expect some deferment of revenue on the renewable business ... there could be some shortfall" | renewables revenue |
| L428-L430 | "achieve that threshold maybe ... in the Q4 part of it. ... Q4 and beyond." | hydrocarbon margin |
| L444-L447 | "hopefully some order info conversion ... Possibly in the most likely by the end of this year." | defence |
| L466-L467 | "execution momentum also has not been, until now has not been disturbed" | ME execution |
| L479-L481 | "there could be a bit of a timing issue that when we recognize the cost and when we get compensated" | cost recovery |
| L490-L492 | "quite a tall ask or steep ask for the next 6 months" | H2 revenue |
| L513 | "looks like over the next two years, we may be putting up data center capacity" | AI capex |
| L654-L655 | "too early to comment on the timelines" | defence |
| L674-L676 | "some of these materials may be delayed because the cost is very high" | solar materials |
| L705-L707 | "I think we are quite hopeful. It should happen. Maybe there will be some delay," | Hormuz transit |
| L741 | "our ability to convert into actionable claims from the customers will take time" | infra claims |

## 6. WHAT WAS NOT DISCUSSED (F17 silence audit)

Watch list from the operator. Silence count = consecutive quarters. All counts are 1 because this is the first observed quarter and no prior log exists.

| Watch item / commitment | Addressed on call? | What is missing | Line ref of nearest coverage | Quarters of silence |
|---|---|---|---|---|
| Order inflow and international (Middle East) share | PARTIAL | Middle East share of INFLOW not stated; only international 62% of PPM inflow | L114-L121 | 1 |
| Order book and book-to-bill | PARTIAL | Book-to-bill not stated (quarterly 1.88x group derived) | L130-L136 | 1 |
| Core E&C margin | YES | PPM 7% (-30 bps). No figure for energy green ("largely stable"), M&P ("improvement") or tech | L169, L266-L267, L281 | 1 (segment figures) |
| Working capital as share of sales | YES | Advance quantum behind the 1.7% not quantified | L182-L186, L486 | 1 (advance quantum) |
| Group vs core split (IT, FS vs core) | PARTIAL | No FS revenue or PAT, no tech margin, no core PAT, no minority split | L296-L302, L789-L804 | 1 |
| FY27 guidance (inflow, revenue, margin) | YES | Guide basis (group vs PPM) unstated for inflow and revenue; H1 PPM margin not stated | L319-L332 | 1 (basis) |
| Hyderabad Metro slip | PARTIAL | No reason for the slip, consideration or conditions precedent | L108-L112 | 1 |
| LTTS one-time gain | PARTIAL | Amount not stated | L294-L295 | 1 |
| Treasury income in PAT | PARTIAL | Amount not stated | L175-L176 | 1 |
| Hormuz pending consignments | PARTIAL | Value and number of modules still to move not stated | L703-L704 | 1 |
| Logistics cost claims | PARTIAL | Rupee amount incurred and recovered not stated | L476-L481 | 1 |
| Chairman/MD participation | NOT IDENTIFIABLE | Only P. Ramakrishnan and the Dy MD & President named; ASR untagged | L28, L37-L38 | 1 |

No silence item can be scored CONFIRMATORY-NEGATIVE yet. That needs two or more quarters of silence on a deteriorating metric.

## 7. ITEMS FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: C-01, C-02, C-04, C-05, C-06, C-07, C-08, C-14, C-15, C-18, C-21, C-22.
AMBIGUOUS: C-03, C-09, C-10, C-11, C-12, C-16, C-17, C-19, C-20, C-23, C-25.
Verify against the filed results and deck first: every heard figure, the guide basis (group vs PPM), H1 PPM margin, the treasury income and LTTS gain amounts, and the segment home of the data center capex.

```yaml
stage: A3-forensics
company: "LT"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/lt-q2fy27/work/forensics_concall_lt_q2fy27.md"
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
  F15: FINDING
  F16: FINDING
  F17: FINDING
findings:
  - {id: "C-01", check: "F6", line: "L313, L319-L320", classification: "FORWARD-SIGNAL", implication: "Inflow guide 10-12% held after H1 +22%; if group-level, H2 inflow growth must run below the band. Guide basis unstated."}
  - {id: "C-02", check: "F6", line: "L126-L128, L260", classification: "FORWARD-SIGNAL", implication: "Pipeline flat only by mix: energy conventional prospects -38% YoY (3.35 to 2.07 trn); energy green doubled, 72% solar, the line being deferred."}
  - {id: "C-03", check: "F6", line: "L490-L492, L592-L595", classification: "AMBIGUOUS", implication: "Revenue guide 10-12% kept despite Q2 PPM +20% because of ME logistics; H2 called a steep ask. Seasonality or expected H2 slowdown?"}
  - {id: "C-04", check: "F6", line: "L169, L331-L332", classification: "FORWARD-SIGNAL", implication: "Q2 PPM margin 7% vs FY27 target 7.8%; only guide held at 'reasonably confident'; H2 must exceed target."}
  - {id: "C-05", check: "F6", line: "L182-L186, L336-L338, L486, L493-L494", classification: "FORWARD-SIGNAL", implication: "NWC guide revised below 10%; 1.7% record partly advance-funded; management already guides H2 moderation. Float peak, not run-rate."}
  - {id: "C-06", check: "F6", line: "L173-L176", classification: "FORWARD-SIGNAL", implication: "PAT +33% partly from treasury income on WC float; shrinks as advances unwind. Amount unstated."}
  - {id: "C-07", check: "F6", line: "L108-L112", classification: "FORWARD-SIGNAL", implication: "Hyderabad Metro divestment slipped 30 Sep to 31 Dec 2026, no reason given; deconsolidation and ROE lift move out with it."}
  - {id: "C-08", check: "F6", line: "L172-L173, L221-L222, L248-L249, L426-L430", classification: "FORWARD-SIGNAL", implication: "Jobs below margin recognition threshold in PPM, infra, carbon lite; hydrocarbon crossing 'maybe' Q4 and beyond; a slip moves margin into FY28."}
  - {id: "C-09", check: "F6", line: "L506-L508, L515, L521, L525-L528, L754", classification: "AMBIGUOUS", implication: "AI capex USD 750m plus 70 MW more in 1.5-2 yrs with new debt; USD 1.8bn not confirmed; segment home PPM vs TPS unclear."}
  - {id: "C-10", check: "F6", line: "L444-L447, L641-L649, L654-L655", classification: "AMBIGUOUS", implication: "Defence conversion heavily hedged, 'this year' undefined, timelines 'too early'; treat defence inflow as unscheduled."}
  - {id: "C-11", check: "F6", line: "L614-L622", classification: "AMBIGUOUS", implication: "PDO USD 6-7bn horizon stated as 4-5 yrs and 3-4 yrs; one of four contractors; right to bid, not share."}
  - {id: "C-12", check: "F6", line: "L759-L770, L823-L829", classification: "AMBIGUOUS", implication: "About 1 lakh crore cash partly to L31 investments; ROE-safe claim rests on take-or-pay; pace and subsidiary leverage unquantified."}
  - {id: "C-13", check: "F6", line: "L86, L102, L105-L106, L534-L535", classification: "NEUTRAL-FACT", implication: "Dated milestones for tracker: AI factory Jan 2027, EV motors Q3 FY27, semis revenue in 1-2 quarters."}
  - {id: "C-14", check: "F7", line: "L255-L256, L365-L366, L417-L419, L668-L677", classification: "FORWARD-SIGNAL", implication: "ME solar: inflow -45%, significant impact, revenue deferment, possible shortfall; H2 recovery rests on hope. Green H2 revenue and inflow risk."}
  - {id: "C-15", check: "F7", line: "L697-L709", classification: "FORWARD-SIGNAL", implication: "Oman-yard hydrocarbon output must cross Hormuz; balance consignments still being explored; delay hits milestones, billing and threshold timing."}
  - {id: "C-16", check: "F7", line: "L662-L664, L697-L699", classification: "AMBIGUOUS", implication: "Contradiction: yards 'not affected' vs yard output 'has to cross' Hormuz. Which projects and what value is stuck?"}
  - {id: "C-17", check: "F7", line: "L412-L416, L476-L481, L596-L600", classification: "AMBIGUOUS", implication: "Logistics and insurance costs incurred now; reimbursement hoped, not agreed; management endorsed 'no margin impact'. Claim and margin risk."}
  - {id: "C-18", check: "F7", line: "L199-L200, L213, L218-L222, L738-L743", classification: "FORWARD-SIGNAL", implication: "Infra (42% of book): inflow -13%, revenue +6%, margin 5.7 vs 6.2; WET claims will take time; management guides continued margin pressure."}
  - {id: "C-19", check: "F7", line: "L729-L730, L219-L220", classification: "AMBIGUOUS", implication: "'Infra margins moving northward' contradicts the reported YoY decline; basis (sequential or ex-WET) unstated."}
  - {id: "C-20", check: "F16", line: "L165-L166, L808-L812", classification: "AMBIGUOUS", implication: "Group EBITDA 10% to 8.7% described as 'maintaining' margin; analysts told not to scrutinise divergence. Framing data point."}
  - {id: "C-21", check: "F16", line: "L789-L804", classification: "FORWARD-SIGNAL", implication: "Segment/PPM EBITDA includes allocated other income; about 80 bps of compression filled by it; 40-50 bps corporate timing reversal undated. PPM margin partly other-income built."}
  - {id: "C-22", check: "F16", line: "L293-L295", classification: "FORWARD-SIGNAL", implication: "Tech segment margin cushioned by one-time LTTS Smart World divestment gain, amount unstated; cushion drops next quarter."}
  - {id: "C-23", check: "F16", line: "L130, L305-L307", classification: "AMBIGUOUS", implication: "Realty carved out of PPM; are PPM comparatives restated and are FY27 guides on the new basis?"}
  - {id: "C-24", check: "F15", line: "L77-L80, L88-L89, L108-L110, L288-L289, L294-L295", classification: "NEUTRAL-FACT", implication: "Entity changes stated: Vyoma AI Ltd, LNTN Compute Pvt Ltd, L&T Metro Rail Hyderabad exit pending, LTTS SWC divestment, L&T Semiconductor Technologies; verify in filed list."}
  - {id: "C-25", check: "F17", line: "L296-L302, L778-L786", classification: "AMBIGUOUS", implication: "Group vs core split partial: tech and L&T Finance waved to public domain; no core PAT or minority split. Silence 1 quarter."}
  - {id: "C-26", check: "F17", line: "L120-L121, L130-L136, L148-L149", classification: "NEUTRAL-FACT", implication: "Book-to-bill and ME share of inflow not stated; derived Q2 inflow/revenue 1.88x group, 2.16x PPM; A4 computes TTM from filings."}
forward_signals: ["C-01", "C-02", "C-04", "C-05", "C-06", "C-07", "C-08", "C-14", "C-15", "C-18", "C-21", "C-22"]
ambiguous: ["C-03", "C-09", "C-10", "C-11", "C-12", "C-16", "C-17", "C-19", "C-20", "C-23", "C-25"]
commitments:
  - {commitment: "AI factory (LNTN Compute, 10,000+ B300 GPUs, Chennai) commissioning", implied_date: "Jan 2027", ref: "L81-L86", status_word: "underway"}
  - {commitment: "Data center business reorganised under Vyoma AI Ltd", implied_date: "not dated", ref: "L77-L80", status_word: "underway"}
  - {commitment: "EV traction motors commercial production", implied_date: "Q3 FY27", ref: "L105-L106", status_word: "initiated"}
  - {commitment: "BESS capacity expansion at Kanchipuram", implied_date: "not dated", ref: "L102-L103", status_word: "underway"}
  - {commitment: "Hyderabad Metro divestment completion", implied_date: "31 Dec 2026 (revised from 30 Sep 2026)", ref: "L108-L112", status_word: "underway, slipped"}
  - {commitment: "FY27 order inflow growth 10-12%", implied_date: "FY27", ref: "L319-L320", status_word: "reaffirmed"}
  - {commitment: "FY27 revenue growth 10-12%", implied_date: "FY27", ref: "L329-L330, L592-L593", status_word: "reaffirmed"}
  - {commitment: "FY27 PPM EBITDA margin 7.8%", implied_date: "FY27", ref: "L331-L332", status_word: "reaffirmed (reasonably confident)"}
  - {commitment: "FY27 group NWC below 10%", implied_date: "FY27", ref: "L336-L338, L487-L499", status_word: "revised (improved)"}
  - {commitment: "Solar ordering recovery outside India", implied_date: "H2 FY27", ref: "L357-L366, L469-L472", status_word: "expected"}
  - {commitment: "Offshore wind execution pick-up", implied_date: "following quarters / FY27", ref: "L327-L328, L404", status_word: "underway"}
  - {commitment: "Hydrocarbon jobs cross margin recognition threshold", implied_date: "Q4 FY27 and beyond", ref: "L428-L430", status_word: "expected"}
  - {commitment: "MHI JV profitable on carbon lite order", implied_date: "not dated", ref: "L392-L395", status_word: "expected"}
  - {commitment: "Defence order conversion", implied_date: "end of this year (CY26 or FY27 unclear)", ref: "L444-L447", status_word: "expected"}
  - {commitment: "AMCA bid submission", implied_date: "Oct-end 2026", ref: "L641-L649", status_word: "imminent"}
  - {commitment: "AI data center capacity 100 MW+", implied_date: "1.5-2 years", ref: "L511-L524", status_word: "planned"}
  - {commitment: "Semiconductor revenue traction", implied_date: "next 1-2 quarters", ref: "L530-L535", status_word: "expected"}
  - {commitment: "Logistics and insurance cost compensation from customers", implied_date: "not dated", ref: "L476-L481", status_word: "in discussion"}
  - {commitment: "Remaining Oman-yard consignments through Hormuz", implied_date: "not dated", ref: "L697-L709", status_word: "exploring"}
  - {commitment: "PDO Oman USD 6-7bn opportunity", implied_date: "4-5 yrs or 3-4 yrs", ref: "L614-L622", status_word: "framework signed"}
  - {commitment: "ME T&D: not much impact in H2", implied_date: "H2 FY27", ref: "L665-L667", status_word: "expected"}
  - {commitment: "Infra claims conversion; margin pressure until then", implied_date: "not dated", ref: "L738-L743", status_word: "pending"}
  - {commitment: "Green hydrogen/ammonia only with take-or-pay; not ROE dilutive", implied_date: "not dated", ref: "L759-L770", status_word: "policy stated"}
  - {commitment: "Realty Lakshya L31 plan unchanged", implied_date: "L31 horizon", ref: "L630-L635", status_word: "unchanged"}
  - {commitment: "Cash surplus partly to L31 investments with subsidiary leverage", implied_date: "not dated", ref: "L822-L829", status_word: "policy stated"}
  - {commitment: "Execution paced to customer payments (WC discipline)", implied_date: "ongoing", ref: "L830-L836", status_word: "policy stated"}
gate_a3: pass
blank_checks: []
analyst_note: "The forward tell is mix, not level. The pipeline is flat at Rs 10.3 trn only because energy green doubled (72% solar EPC) while energy conventional, the Q2 inflow engine, fell 38%. Growth now sits in the line management says Middle East logistics is deferring. Guidance was held, not raised, after H1 inflow +22% and Q2 PPM revenue +20%. If the guide is group-level, H2 inflow growth must fall below 10-12%, and management calls H2 revenue a steep ask. The 1.7% NWC record is advance-funded with moderation already guided, and Q2 PAT growth leans on treasury income from that float. Margin optics are cushioned twice: segment EBITDA carries allocated other income (about 80 bps), and tech margin carries a one-time LTTS gain. The best A4 questions are two internal contradictions: hydrocarbon 'least impact' vs the Hormuz crossing, and infra 'moving northward' vs 5.7% vs 6.2%. ASR attribution: R291/R292 and R394 read as analyst assertions. R460 'PPS' is likely Technology Platforms and Services, not PPM (L284-L287). Every figure is heard, unverified."
```
