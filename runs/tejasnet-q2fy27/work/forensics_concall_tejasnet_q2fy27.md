# A3 FORENSIC NOTES: TEJASNET Q2 FY27, doctype CONCALL (filed transcript, call 16-Oct-2026, filed 22-Oct-2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date 2026-10-23
Inputs read: A1 structured (R001-R324), A1 fulltext (624 lines), A2 ledger, Q1 FY27 concall extract (ASR, prior), Notion digest sections 4, 5, 8 only. No source PDF opened, nothing under inputs/ opened, digest section 9 and Key Notes not read.

Line references: "l.N" = A1 fulltext line of the Q2 transcript. "prior l.N" = line of the Q1 FY27 extract file. "dig. N" = Notion digest section.
Transcript qualifier: Q2 text is "edited for clarity and readability and does not purport to be a verbatim record" (l.622). Q1 text is machine ASR with garbles. Quotes below are verbatim from the A1 files, not from the call audio.

## 0. LEDGER RECONCILIATION

- Rows in ledger: 324 (R001-R324; orphan_ids none). Rows read at their cited line in the fulltext: 324. Reconciled: 100%.
- Ledger count test re-checked: 52 turns, 15 questions, 53 management numbers, 64 forward phrases, 37 qualifiers, 38 dates, 72 non-turn entities, 0 ZERO_STANDING. All agree with the structured file.
- Line offsets found (immaterial, no row lost): R285 "Navratri" cited l.606 (turn start), text sits at l.607. R040 "2030" spans l.204-205. R286 "end of next quarter" spans l.616-617.
- A2 flags carried and used: LABEL net debt (R032/R033, R292/R299), UNQUANTIFIED_INVENTORY_DEBT_PATH (R189, R212, R219, R235-R237), NON_DISCLOSURE (R301, R304, R315, R320), NEGATIVE_COMMITMENT (R233, R234), TITLE_DISCREPANCY (R068), MGMT_ABSENCE (R071, R072), FOOTNOTE_UNRESOLVED (R317), MISMATCH (R006 vs analyst R050/R054).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | R214, R220, R272, R274 | l.297-298; l.317-318; prior l.78 | "achieving quarterly positive EBITDA performance" / "visible path to profitability in the upcoming years" vs Q1 "12 to 18 months is a reasonable time to expect" | FORWARD-SIGNAL | EBITDA-positive target lost its date. Chain: AGM-26 Q4 FY27 -> Q1 "12 to 18 months" -> Q2 undated "upcoming years". Second consecutive softening, unacknowledged. Gate 4 (re-dated named quarter) not met. |
| A3-F6-02 | F6 | R221, R222, R275, R276, R301 | l.334; l.338-341; prior l.46 | "this is the quarter when we will see a significant amount of collections coming from BSNL" | FORWARD-SIGNAL | Q1 promised BSNL receivables "cleared during the quarter" (prior l.46). Analyst flagged the miss (l.334). Promise re-dated one quarter to Q3 FY27, amount withheld (l.340). Q3 is the test; a second slip breaks the deleveraging narrative. |
| A3-F6-03 | F6 | R032, R033, R190, R219, R235, R236, R237, R294, R315 | l.139-141; l.315-316; l.514; l.528-530 | "debt has increased to INR4,384 crores ... on account of continued investments in terms of capex ... and also in terms of funding operational costs" | FORWARD-SIGNAL | Debt +Rs107 Cr QoQ (4,277 -> 4,384). If net (see F16-02), Rs116 Cr headroom to the Rs4,500 Cr break; RED band (>Rs4,000 Cr). Debt now funds operating costs (cash burn continues). Reduction is promised only "with the order", undated and unquantified ("I cannot give exact numbers", l.514). Inventory converts to receivables first (l.523), so debt can peak before it falls. |
| A3-F6-04 | F6 | R030, R031, R189, R212, R264, R283, R300 | l.134-137; l.515-518 | "compared to INR2,358 crores, we are at around INR2,314 crores" | AMBIGUOUS | Inventory fell only Rs44 Cr in the quarter BSNL deliveries started (Q1 fell Rs80 Cr, prior l.32). Target "earlier levels ... in line with the kind of quarterly business" (l.517-518) has no date or number. Question: inventory consumed per Rs of BSNL revenue, and the quarter inventory reaches the target level. |
| A3-F6-05 | F6 | R057, R059, R124, R125, R233, R234, R281, R313, R314, R316 | l.478-481; l.485; l.494; l.498-499 | "It's September 2025. There is no provisioning of that sort in the current quarter." / "This was connected to the major amount of manufacturing that we did for the first 100,000 site order." | FORWARD-SIGNAL | Management commits to non-recurrence, but names the cause as volume manufacturing for the first BSNL order. The 18,685-site expansion repeats that manufacturing on "the same lines" economics (prior l.92). Recurrence risk on the expansion order is open. Question: what failed in the contract-manufacturing process and what control prevents a repeat. |
| A3-F6-06 | F6 | R012, R034, R052, R082 | l.98; l.145; l.349; prior l.34, l.196 | "receiving the LOI for 18,685 sites" vs Q1 "the uh BSNL 4G that additional 26,000 sites" | AMBIGUOUS | Scope matches the Notion baseline (Rs1,526 Cr / 18.7k sites, dig. 5b), so item #7 RED does not fire. But Q1 management twice said 26,000 sites; Q2 says 18,685 with no reconciliation. Q1 text is ASR, so a garble is possible. Question: was the add-on ever 26,000 sites, and is a further tranche expected. |
| A3-F6-07 | F6 | R223, R277, R302, R006 | l.95; l.346-350 | "all of INR1,500 crores is not there in the order book yet, but they will come -- most of it, we expect to come by the end of this quarter" | NEUTRAL-FACT | Dated commitment: most remaining BSNL POs by 31-Dec-2026. Part of the PO value sits in the 30-Sep order book (l.95, l.346), which is the transcript's only evidence that a PO landed by the Sep-2026 thesis-break deadline. The LOI date itself is not stated ("recently won", l.290). |
| A3-F7-01 | F7 | R301, R304, R315, R320, R312 | l.340; l.355; l.514; l.584 | "I cannot specify the exact number" / "I don't think I can share the exact details" / "I cannot give exact numbers" / "I cannot comment on the NEC's revenue number" | FORWARD-SIGNAL | Four refusals, each on a cash or backlog quantum: BSNL collections, order-book split, inventory and debt reduction, NEC revenue. Q1 had four refusals too (dig. 8e: AMC size, NEC TAM, wireless/wireline split, site counts). The deleveraging case rests on assertion only. R317 (l.528-529) cites a "financial outlook" in the presentation that the transcript does not carry in numbers. |
| A3-F7-02 | F7 | R058, R232, R279, R312, R123 | l.458-460; l.476; prior l.220 | "we are indeed winning several business in this area" | AMBIGUOUS | Analyst asked for a range or quantum of AI DCI orders over 6 to 8 months; none given. Q1 said the new DCI product would see "customer deployment ... towards the end of the financial year or early financial year" (prior l.220). Q2 does not say if trials converted. Question: count and value of DCI orders on the new product. |
| A3-F7-03 | F7 | R230, R231, R238, R239, R240, R310, R311, R319 | l.464-466; l.535; l.546; l.549-551 | "We are well-positioned if this network were to happen" / "It will potentially be used for Kavach" | NEUTRAL-FACT | D2M RFP still not issued (Q1: "no clarity on when exactly the tender happens", prior l.166). Second quarter undated. Railways: trial-section PO only, expansion conditional on trial results. Both stay optionality with no date. |
| A3-F14-01 | F14 | R068, R075 | l.55-56; l.83 | "MR. ARNOB ROY - MANAGING DIRECTOR AND CHAIRMAN" vs "Arnob Roy, Managing Director and Chief Executive Officer" | AMBIGUOUS | The filed participant page gives a Chairman title. The host intro and Q1 (prior l.28, "managing director and CEO") do not. Either a board-level redesignation (a Reg 30 event to verify) or a drafting error in a filed document. Question: has the Chairman role changed. |
| A3-F14-02 | F14 | R323, R142, R155, R071, R072 | l.622; l.601; l.603 | "does not purport to be a verbatim record" / "I think we can close the call a bit early" | NEUTRAL-FACT | Edited transcript. Two analysts (Q1: 8) and 15 questions (Q1: 37). Call closed early with an empty queue. COO and CSBO listed, zero turns. Answers were lightly tested; route open questions through IR email. |
| A3-F16-01 | F16 | R029, R291, R032, R033 | l.128-129; l.139-140; prior l.32 | "the net working capital compared to Q1 FY27 is lower at INR4,235 crores" | CONFIRMATORY-NEGATIVE | Q1 spoken disclosures (prior l.32): cash Rs489 Cr, gross borrowings Rs4,866 Cr, net borrowings Rs4,277 Cr, net receivables Rs2,232 Cr. Q2 drops cash, the gross/net split and the receivables figure. It calls NWC "lower" against a Q1 NWC that neither call disclosed. Disclosure narrowed on the metrics nearest the tripwires. |
| A3-F16-02 | F16 | R292, R299 | l.139-140; l.316 | "At the net debt position compared to INR4,277 crores in Q1 FY27, debt has increased to INR4,384 crores" / "bring down our inventory and gross debt significantly" | AMBIGUOUS | The base Rs4,277 Cr was Q1 net borrowings (prior l.32), so Rs4,384 Cr reads as net debt (conservative read). If it were gross, gross fell Rs482 Cr from Rs4,866 Cr, which contradicts "has increased". Basis must come from the results filing. Question: Q2 gross borrowings, cash, and net debt. |
| A3-F16-03 | F16 | R021, R022, R027, R028, R289, R313 | l.111; l.115-116; l.125-126; l.479; l.494 | "The improved scale reflects the continued recovery" / "compared to the last quarter EBITDA of negative INR99 crores, we are at negative INR108 crores" | AMBIGUOUS | CFO leads with YoY. The Q2 FY26 base (EBITDA -Rs293 Cr) carried the Rs145 Cr provision, which the analyst placed in COGS (l.479). Arithmetic: ex-provision base about -Rs148 Cr, so YoY gain about Rs40 Cr, not Rs185 Cr. QoQ EBITDA worsened Rs9 Cr on Rs4 Cr more revenue. Question: confirm the provision sat above EBITDA in Q2 FY26. |
| A3-F16-04 | F16 | R006, R007, R050, R054, R302, R303, R304 | l.95; l.346-349; l.355-358 | "as we keep on getting the POs, they come into our order book" / "a substantial portion of it and the rest of it has come from non-BSNL customers" | AMBIGUOUS | Order book is PO-only (LOI excluded). BSNL share withheld. Arithmetic on stated figures, same-basis assumption: inflow = 2,315 - 1,529 + 406 = Rs1,192 Cr. Ex-BSNL inflow NOT FOUND. Q1 order book already held BSNL AMC/service items (prior l.116). Question: BSNL PO value inside the Rs2,315 Cr. |
| A3-F16-05 | F16 | R008, R009, R010, R011, R216 | l.96-97; l.302; prior l.30, l.104, l.114 | "India was 88% compared to the international revenues of 12%" / "We are seeing increasing international engagements" | FORWARD-SIGNAL | Q1 revenue was "evenly split" (prior l.30, l.104). Arithmetic: international about Rs201 Cr Q1 to about Rs49 Cr Q2. International order book fell 7% to 4% (prior l.114 vs l.97), against Q1's "we hope to change that profile". The call narrates engagement growth and does not explain the revenue drop. Item #6: 12% sits between RED (<10%) and GREEN (>15%), and the 4% book points lower next quarter. |
| A3-F16-06 | F16 | R080, R293 | l.130-132 | "we do a nonrecourse bill discounting which also has customer advance settlements ... The reduction is on account of increased collections and nonrecourse discounting." | AMBIGUOUS | Part of the receivables drop is off-balance-sheet financing, not customer cash. That flatters NWC and DSO, carries a discount cost, and debt still rose. Question: nonrecourse discounting outstanding at Q1 and Q2, and its cost. |
| A3-F17-01 | F17 | R139-R141 context; R294 | l.139-141; l.315-318; dig. 8c | Debt discussion runs l.139-141 and l.315-318 with no capital-raise or DTA reference | FORWARD-SIGNAL | QIP/equity intent and DTA recoverability: second consecutive silence (count 2). Digest 8c pre-registers that a second silence on DTA or QIP escalates to RED at Q2 (A4 decides). Deleveraging is again sold on one order, not on capital. |
| A3-F17-02 | F17 | R015-R024 | l.115-117; l.140-141 | "at the PAT level compared to INR307 crores negative in Q2 FY26, we are at negative INR207 crores" | CONFIRMATORY-NEGATIVE | Silent: Rs950 Cr intangibles under development (count 2), PLI income #8 (2), book value/share #9 (2), 3-year cash-loss track (2), finance cost #10 (1). Arithmetic: the PAT-below-EBITDA gap widened from Rs14 Cr (Q2 FY26: -307 vs -293) to Rs99 Cr (Q2 FY27: -207 vs -108). Consistent with rising finance cost and D&A, or a smaller tax credit. The results filing must decompose it. |
| A3-F17-03 | F17 | none (absent topics) | prior l.88; prior l.100; prior l.128; prior l.150; absent l.69-624 | Q1: "the warranty costs are expected to normalize" / "It's going to start in the next few quarters" (AMC) | AMBIGUOUS | Three Q1 commitments got no follow-up: BSNL AMC start, value and 8-year term (count 1); warranty normalisation (count 1); flat employee cost (count 1). AMC was Q1's higher-margin path-to-profit lever (prior l.150). Question: AMC start quarter and value; last two quarters' warranty charge. |
| A3-F17-04 | F17 | R085, R192 | l.151-155; prior l.30; prior l.34 | "we are engaged with discussions with several Tier 1 mobile network operators for custom 5G radio development" | AMBIGUOUS | Q1 headline items got no Q2 status: the Europe 5G radio customer (the Q1 international revenue driver, count 1) and the "selected by a global tier one telco for a joint R&D project" (count 1). Q2 replaces them with Tier 1 "discussions". This links to F16-05. Question: did Europe shipments stop; is the joint R&D project live. |

Finding count: 22. FORWARD-SIGNAL 7 | AMBIGUOUS 10 | CONFIRMATORY-NEGATIVE 2 | NEUTRAL-FACT 3.

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Transcript; A2 ZERO_STANDING count 0 (ledger section 9). |
| F2 Standalone vs consolidated | N.A. | No S-vs-C tables on a concall; CFO gives one set of figures, basis unstated. |
| F3 Shell-entity detection | N.A. | No cost-line tables on a concall. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters in a transcript. |
| F5 Going concern / EoM scope | N.A. | No auditor report in a transcript. |
| F6 Forward-commitment mining | FINDING | 64 forward rows read. 7 findings: EBITDA date dropped, BSNL collections re-dated, debt up and unquantified, slow inventory unwind, provision-recurrence risk, site-count gap, dated PO commitment. |
| F7 Hedge mining | FINDING | 37 qualifier rows read. 3 findings: four quantum refusals, DCI unquantified, D2M/rail conditional. "supposed to" market forecasts (l.204, l.209) repeat Q1 (prior l.34); boilerplate, no finding. |
| F8 Tax forensics | N.A. | No PBT, tax or ETR on the call. The PAT-EBITDA gap is carried under F17-02 for the results-filing A3. |
| F9 OCI forensics | N.A. | No OCI on a concall. |
| F10 Share count and dilution | N.A. | No share count or EPS on the call. Equity-raise silence carried under F17-01. |
| F11 Reserves and net worth tie-out | N.A. | No equity figure on the call. |
| F12 Segment forensics | N.A. | No segment assets or liabilities; wireless/wireline split not given. |
| F13 Board outcome | N.A. | No board outcome in a transcript. Chairman title anomaly carried under F14-01. |
| F14 Drafting inconsistencies | FINDING | Applied to the filed transcript: title discrepancy (l.55-56 vs l.83); edited, thin, early-closed call (l.622, l.601). |
| F15 Entity list diffs | N.A. | No consolidation list on a concall. Participant changes (host ICICI to Emkay; COO/CSBO zero turns) logged in F14-02. |
| F16 Dropped / reframed disclosures | FINDING | Applied to the spoken deck walkthrough ("right-hand side of the slide", l.175-176; "end of my presentation", l.320). Measured against Q1's spoken disclosure set. 6 findings: dropped cash/gross/receivables, net-vs-gross label, YoY framing over provision base, PO-only order book, international collapse narrated as growth, discounting inside the NWC drop. |
| F17 Silence audit | FINDING | 13 items silent, 4 partial (table section 5). 4 findings. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| 1 | Significant BSNL collections tied to milestones achieved | Q3 FY27 (by 31-Dec-2026) | T10 l.338-341 (R221, R276) | underway (re-dated from Q2) |
| 2 | Receivables to reduce substantially | Q3 FY27 | T10 l.340-341 (R222) | underway |
| 3 | Most remaining BSNL POs into the order book | end Q3 FY27 (31-Dec-2026) | T12 l.349-350 (R223, R277) | underway |
| 4 | Deliver BSNL 4G expansion order within required timelines | per BSNL schedule (not stated) | T07 l.290-291; T04 l.136-137 (R211, R263) | underway (deliveries started Q2) |
| 5 | Significant portion of inventory used on BSNL order; back to "earlier levels" | "coming quarters" / "next few quarters" | T04 l.135-136; T39 l.515-518 (R189, R235, R264, R283) | underway |
| 6 | Gross debt down significantly with BSNL execution | undated | T07 l.315-316; T41 l.528-530 (R219, R236, R237) | initiated (debt still rising) |
| 7 | Achieve quarterly positive EBITDA | undated (Q1: 12-18 months; AGM-26: Q4 FY27) | T07 l.297-298 (R214, R272) | undated / softened |
| 8 | Visible path to profitability | "upcoming years" | T07 l.317-318 (R220, R274) | undated |
| 9 | Rs145 Cr contract-manufacturing provision not recurring | standing | T31 l.494; T33 l.498 (R233, R234) | negative commitment |
| 10 | Capex continuing as per plan | ongoing | T04 l.140-141 (R190) | underway |
| 11 | BSNL milestone delivery requirements met | done in Q2 | T10 l.338 (R112) | completed |
| 12 | South America end-to-end 5G shipments | started Q2 | T03 l.103-105 (R188) | initiated |
| 13 | NEC radio technology supply to NEC and new customers | ongoing | T48 l.585-590 (R243, R244) | underway |
| 14 | Radio development partner for NEC's future radios | not stated | T49 l.598-600 (R245, R246) | underway |
| 15 | Custom 5G radio development with several Tier 1 MNOs | not stated | T05 l.151-153; T46 l.568-573 (R192, R242) | initiated (discussions) |
| 16 | Railway 700 MHz network expansion on trial results | conditional, undated | T25 l.465-466 (R230) | initiated (trial deployed) |
| 17 | D2M: supply broadcast radio heads to RFP winners | once RFP issued, undated | T44 l.538-551 (R238-R240) | initiated (trials done) |
| 18 | Product roadmap: compact baseband (5 bands), radio 700 MHz-4.9 GHz, IP/MPLS higher rates, 200G access, terabit backbone, TOP rollout | undated | T06 l.232-266 (R200-R206) | underway |
| 19 | Revenue momentum from BSNL | "next few quarters" | T51 l.611-612 (R247, R287) | underway |
| 20 | Next call | end of next quarter | T51 l.616-617 (R286) | scheduled |

## 4. PROMISE VS DELIVERY (Q1 FY27 call -> Q2 FY27 call)

| Q1 commitment | Q1 ref | Q2 evidence | read |
|---|---|---|---|
| BSNL add-on award "probably in this quarter" | prior l.34 | LOI 18,685 sites, POs partly in order book (l.145, l.346-349) | DELIVERED; scope differs from Q1's 26,000 sites (F6-06) |
| BSNL receivables "cleared during the quarter" | prior l.46 | "this is the quarter" re-dated to Q3 (l.338-339) | SLIPPED one quarter (F6-02) |
| Positive EBITDA "12 to 18 months" | prior l.78 | undated (l.298, l.317-318) | SOFTENED (F6-01) |
| Inventory to "go away" with the add-on | prior l.74 | -Rs44 Cr (l.134) | UNDERWAY, slow (F6-04) |
| International "hope to change that profile" (7% of order book) | prior l.114 | 4% of order book, 12% of revenue (l.96-97) | REVERSED (F16-05) |
| AMC revenue "start in the next few quarters" | prior l.100, l.150 | silent | SILENT (F17-03) |
| Warranty to normalise | prior l.88 | silent | SILENT (F17-03) |
| Employee cost flat | prior l.128 | silent | SILENT (F17-03) |
| New DCI product deployment by end FY27 / early FY28 | prior l.220 | "winning several business" (l.476) | UNVERIFIABLE (F7-02) |
| D2M tender | prior l.166 | RFP not yet issued (l.535, l.546) | UNCHANGED (F7-03) |
| South America further orders after initial order | prior l.124 | initial shipments started (l.103-105) | INITIAL DELIVERED; no add-on order yet |
| 6G capability demos "starting next year" | prior l.226 | ISAC demo at IMC 2026 (l.246-249) | ON TRACK |

## 5. WHAT WAS NOT DISCUSSED (F17 silence audit)

Sources: F6 commitments, Q1 FY27 promise log and residual questions (dig. 8b-8d), monitoring checklist (dig. 5), TBC items named in the task. Count = consecutive quarterly calls with no mention (Q1 FY27 call checked line by line for items not in the Q1 silence table).

| # | item | why it matters | Q2 status | consecutive quarters silent |
|---|---|---|---|---|
| 1 | QIP / equity raise | Net debt RED and rising; pre-committed QIP-below-Rs400 thesis-break (dig. 4g) | SILENT | 2 |
| 2 | DTA recoverability (~Rs434 Cr, ~52% equity KAM) | Earnings-cliff and equity risk if recognition halts | SILENT | 2 |
| 3 | Intangibles under development Rs950 Cr (KAM) | Impairment risk; "continued investments in terms of capex" (l.140-141) keeps it growing | SILENT | 2 |
| 4 | PLI income (#8) | FY26 collapse Rs468 Cr to Rs6 Cr; RED/UNKNOWN | SILENT | 2 |
| 5 | Book value per share (#9) | QIP-trigger floor; Q2 PAT -Rs207 Cr (l.93) | SILENT | 2 |
| 6 | 3-year cash-loss track (cash balance also dropped; Q1 Rs489 Cr, prior l.32) | Going-concern-adjacent KAM | SILENT | 2 |
| 7 | Finance cost (#10) | Q1 Rs85 Cr; AMBER/RED thresholds; PAT-EBITDA gap widened (F17-02) | SILENT (Q1 qualitative, prior l.74) | 1 |
| 8 | Warranty charge | Q1 called it "one-off" (prior l.88) | SILENT | 1 |
| 9 | BSNL AMC value, start quarter, 8-year term | Higher-margin profit lever (prior l.150) | SILENT | 1 |
| 10 | Vodafone Idea backhaul | Thesis-core catalyst | SILENT (Vi raised only as wireless POC, l.407; names withheld, l.412) | 2 |
| 11 | Global Tier 1 telco joint R&D project | Q1 headline (prior l.34) | SILENT (replaced by Tier 1 "discussions", l.151-152) | 1 |
| 12 | Europe 5G radio customer | Q1 international revenue driver (prior l.30) | SILENT; international share fell to 12% | 1 |
| 13 | Employee cost guidance (flat) | Opex path to EBITDA break-even | SILENT | 1 |

Partially addressed (spoken, not resolved):

| item | Q2 evidence | gap |
|---|---|---|
| EBITDA-positive date | l.298, l.317-318 | date dropped (F6-01) |
| Net receivables / DSO | "lower trade receivables" (l.129-130) | Q1 gave Rs2,232 Cr; Q2 gives no figure; nonrecourse discounting mixed in (F16-06) |
| International mix (#6) | 12% revenue, 4% book (l.96-97) | drop from ~50% unexplained (F16-05) |
| Inventory and debt reduction quantum | l.514-530 | refused (F7-01) |

Addressed (Q1 silence broken or item answered): revenue #2 (Rs406 Cr, l.92), net debt #4 (Rs4,384 Cr, l.140), BSNL PO #7 (LOI 18,685 sites / Rs1,500 Cr, l.145, l.349), BharatNet (new SI LOI, middle mile in 3 states, l.157-159; count resets to 0), D2M (l.538-551), NEC (l.584-600), Rs145 Cr provision (l.485-499).

Silence count: 13 items silent (6 at 2 consecutive quarters, 7 at 1), plus 4 partial.

## 6. FLAGS FOR A4 (FORWARD-SIGNAL and AMBIGUOUS, convert to management questions)

FORWARD-SIGNAL: A3-F6-01, A3-F6-02, A3-F6-03, A3-F6-05, A3-F7-01, A3-F16-05, A3-F17-01.
AMBIGUOUS: A3-F6-04, A3-F6-06, A3-F7-02, A3-F14-01, A3-F16-02, A3-F16-03, A3-F16-04, A3-F16-06, A3-F17-03, A3-F17-04.

```yaml
stage: A3-forensics
company: "TEJASNET"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tejasnet-q2fy27/work/forensics_concall_tejasnet_q2fy27.md"
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
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-F6-01", check: "F6", line: "l.297-298; l.317-318; prior l.78", classification: "FORWARD-SIGNAL", implication: "EBITDA-positive target undated ('upcoming years') vs Q1 '12 to 18 months'; second consecutive softening"}
  - {id: "A3-F6-02", check: "F6", line: "l.334; l.338-341; prior l.46", classification: "FORWARD-SIGNAL", implication: "BSNL collections re-dated from Q2 to Q3 FY27, amount withheld; Q3 is the test"}
  - {id: "A3-F6-03", check: "F6", line: "l.139-141; l.315-316; l.514; l.528-530", classification: "FORWARD-SIGNAL", implication: "Debt +Rs107 Cr to Rs4,384 Cr, funds capex and operating costs; Rs116 Cr to Rs4,500 Cr break if net; reduction undated and unquantified"}
  - {id: "A3-F6-04", check: "F6", line: "l.134-137; l.515-518", classification: "AMBIGUOUS", implication: "Inventory down only Rs44 Cr as BSNL deliveries began; target level and date absent"}
  - {id: "A3-F6-05", check: "F6", line: "l.478-481; l.485; l.494; l.498-499", classification: "FORWARD-SIGNAL", implication: "Rs145 Cr provision called non-recurring but caused by BSNL volume manufacturing, which recurs on the 18,685-site expansion"}
  - {id: "A3-F6-06", check: "F6", line: "l.98; l.145; l.349; prior l.34, l.196", classification: "AMBIGUOUS", implication: "18,685 sites vs Q1 '26,000 sites' unreconciled; matches Notion Rs1,526 Cr/18.7k baseline"}
  - {id: "A3-F6-07", check: "F6", line: "l.95; l.346-350", classification: "NEUTRAL-FACT", implication: "Most remaining BSNL POs by 31-Dec-2026; partial PO value in 30-Sep order book is the only by-deadline evidence"}
  - {id: "A3-F7-01", check: "F7", line: "l.340; l.355; l.514; l.584", classification: "FORWARD-SIGNAL", implication: "Four refusals on collections, order-book split, inventory/debt reduction, NEC revenue; deleveraging rests on assertion"}
  - {id: "A3-F7-02", check: "F7", line: "l.458-460; l.476; prior l.220", classification: "AMBIGUOUS", implication: "AI DCI orders unquantified; Q1 deployment timeline for new DCI product not updated"}
  - {id: "A3-F7-03", check: "F7", line: "l.464-466; l.535; l.546; l.549-551", classification: "NEUTRAL-FACT", implication: "D2M RFP not issued (2nd quarter), railways trial-only; optionality undated"}
  - {id: "A3-F14-01", check: "F14", line: "l.55-56; l.83", classification: "AMBIGUOUS", implication: "Filed page titles Arnob Roy 'Managing Director and Chairman' vs 'MD and CEO'; verify board change or drafting error"}
  - {id: "A3-F14-02", check: "F14", line: "l.622; l.601; l.603", classification: "NEUTRAL-FACT", implication: "Edited transcript, 2 analysts (Q1: 8), early close; answers lightly tested"}
  - {id: "A3-F16-01", check: "F16", line: "l.128-129; l.139-140; prior l.32", classification: "CONFIRMATORY-NEGATIVE", implication: "Cash, gross/net debt split and net receivables dropped vs Q1; NWC called 'lower' against an undisclosed Q1 base"}
  - {id: "A3-F16-02", check: "F16", line: "l.139-140; l.316", classification: "AMBIGUOUS", implication: "Rs4,384 Cr labelled 'net debt' heading, 'debt', later 'gross debt'; conservative read is net"}
  - {id: "A3-F16-03", check: "F16", line: "l.111; l.115-116; l.125-126; l.479; l.494", classification: "AMBIGUOUS", implication: "YoY EBITDA gain flattered by Rs145 Cr provision in Q2 FY26 base (about Rs40 Cr ex-provision); QoQ EBITDA worse"}
  - {id: "A3-F16-04", check: "F16", line: "l.95; l.346-349; l.355-358", classification: "AMBIGUOUS", implication: "PO-only order book, BSNL share withheld; implied inflow Rs1,192 Cr, ex-BSNL NOT FOUND"}
  - {id: "A3-F16-05", check: "F16", line: "l.96-97; l.302; prior l.30, l.104, l.114", classification: "FORWARD-SIGNAL", implication: "International ~50% to 12% of revenue, order book 7% to 4%, unexplained while 'increasing international engagements' narrated"}
  - {id: "A3-F16-06", check: "F16", line: "l.130-132", classification: "AMBIGUOUS", implication: "Receivables drop partly nonrecourse discounting, not customer cash; quantum and cost undisclosed"}
  - {id: "A3-F17-01", check: "F17", line: "l.139-141; l.315-318", classification: "FORWARD-SIGNAL", implication: "QIP and DTA silent for 2nd consecutive call; digest 8c pre-registers RED escalation"}
  - {id: "A3-F17-02", check: "F17", line: "l.115-117; l.140-141", classification: "CONFIRMATORY-NEGATIVE", implication: "Rs950 Cr intangibles, PLI, BV/share, cash-loss track, finance cost silent; PAT-EBITDA gap widened Rs14 Cr to Rs99 Cr"}
  - {id: "A3-F17-03", check: "F17", line: "prior l.88, l.100, l.128, l.150; absent l.69-624", classification: "AMBIGUOUS", implication: "Q1 AMC start, warranty normalisation, flat employee cost not followed up"}
  - {id: "A3-F17-04", check: "F17", line: "l.151-155; prior l.30, l.34", classification: "AMBIGUOUS", implication: "Europe 5G customer and Tier 1 joint R&D project (Q1 headlines) given no status"}
forward_signals: ["A3-F6-01", "A3-F6-02", "A3-F6-03", "A3-F6-05", "A3-F7-01", "A3-F16-05", "A3-F17-01"]
ambiguous: ["A3-F6-04", "A3-F6-06", "A3-F7-02", "A3-F14-01", "A3-F16-02", "A3-F16-03", "A3-F16-04", "A3-F16-06", "A3-F17-03", "A3-F17-04"]
commitments:
  - {commitment: "Significant BSNL collections tied to milestones", implied_date: "Q3 FY27", ref: "T10 l.338-341", status_word: "underway"}
  - {commitment: "Receivables to reduce substantially", implied_date: "Q3 FY27", ref: "T10 l.340-341", status_word: "underway"}
  - {commitment: "Most remaining BSNL POs into order book", implied_date: "31-Dec-2026", ref: "T12 l.349-350", status_word: "underway"}
  - {commitment: "Deliver BSNL 4G expansion within required timelines", implied_date: "not stated", ref: "T07 l.290-291; T04 l.136-137", status_word: "underway"}
  - {commitment: "Inventory used on BSNL order, back to earlier levels", implied_date: "next few quarters", ref: "T04 l.135-136; T39 l.515-518", status_word: "underway"}
  - {commitment: "Gross debt down significantly with BSNL execution", implied_date: "undated", ref: "T07 l.315-316; T41 l.528-530", status_word: "initiated"}
  - {commitment: "Quarterly positive EBITDA", implied_date: "undated (Q1: 12-18 months)", ref: "T07 l.297-298", status_word: "softened"}
  - {commitment: "Visible path to profitability", implied_date: "upcoming years", ref: "T07 l.317-318", status_word: "undated"}
  - {commitment: "Rs145 Cr manufacturing provision not recurring", implied_date: "standing", ref: "T31 l.494; T33 l.498", status_word: "negative commitment"}
  - {commitment: "Capex continuing as per plan", implied_date: "ongoing", ref: "T04 l.140-141", status_word: "underway"}
  - {commitment: "BSNL milestone deliveries met", implied_date: "Q2 FY27", ref: "T10 l.338", status_word: "completed"}
  - {commitment: "South America end-to-end 5G shipments", implied_date: "Q2 FY27", ref: "T03 l.103-105", status_word: "initiated"}
  - {commitment: "NEC radio tech supply to NEC and new customers", implied_date: "ongoing", ref: "T48 l.585-590", status_word: "underway"}
  - {commitment: "Custom 5G radio with Tier 1 MNOs", implied_date: "not stated", ref: "T05 l.151-153", status_word: "initiated"}
  - {commitment: "Railway 700 MHz expansion on trial results", implied_date: "conditional", ref: "T25 l.465-466", status_word: "initiated"}
  - {commitment: "D2M radio heads to RFP winners", implied_date: "once RFP issued", ref: "T44 l.538-551", status_word: "initiated"}
  - {commitment: "Revenue momentum from BSNL", implied_date: "next few quarters", ref: "T51 l.611-612", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Rs4,384 Cr reads as net debt because its comparison base, Rs4,277 Cr, was Q1 net borrowings (prior l.32). On that read it sits Rs116 Cr under the Rs4,500 Cr break, rose Rs107 Cr QoQ, and now funds operating costs. Management asserted every deleveraging lever (BSNL collections, inventory unwind, debt cut) and refused to quantify any of them. The BSNL collection date slipped one quarter. Q3 FY27 therefore tests three dated items together: BSNL cash, remaining POs, and the debt turn. The Rs185 Cr YoY EBITDA gain sits on a Q2 FY26 base that carried the Rs145 Cr provision. Ex-provision the gain is about Rs40 Cr, and QoQ EBITDA worsened. The provision's named cause recurs on the expansion order. International revenue fell from about half to 12% with no explanation. The Q2 PAT loss of Rs207 Cr exceeds the Rs185 Cr line in digest 5e for book value below Rs140; A4 must confirm this with comprehensive loss from the filing. QIP and DTA are second-consecutive silences, and digest 8c pre-registers that as RED escalation."
```
