# A2 COMPLETENESS LEDGER — DATAPATTNS Q1 FY27 CONCALL

Source: `runs/datapattns-q1fy27/work/extract_concall_datapattns_q1fy27.txt`
(extract file has 245 physical lines; transcript body runs from file line 55
`===== TRANSCRIPT BEGINS =====` to file line 225 `===== TRANSCRIPT ENDS =====`,
carrying the source's own native turn/line numbering 1-175, of which lines
6-174 fall strictly between the markers). "Turn #" below = the transcript's
own native line numbering (1-175, matches A1's TURN STRUCTURE convention).
"File line" = the physical line in the extract file (Read/Grep addressable).

```
=== A2 COUNT TEST ===
category: turns         grep_count: 84   sweep_count: 84   match: yes
category: questions     grep_count: 39   sweep_count: 39   match: yes
category: mgmt_numbers  grep_count: 66   sweep_count: 66   match: yes
category: notes         grep_count: 0    sweep_count: 0    match: yes  (N/A — concall doctype, no numbered-notes section)
category: line_items    grep_count: 0    sweep_count: 0    match: yes  (N/A — concall doctype, no financial table)
category: agenda_items  grep_count: 0    sweep_count: 0    match: yes  (N/A — not a Board Outcome letter)
category: auditor_paras grep_count: 0    sweep_count: 0    match: yes  (N/A — not an auditor report)
category: entities      grep_count: 0    sweep_count: 0    match: yes  (N/A — no consolidation list in a concall)
category: slides        grep_count: 0    sweep_count: 0    match: yes  (N/A — not an investor presentation)
gate_a2: pass
=== END COUNT TEST ===
```

**Method note (turns count reconciliation):** GREP pass = counted every
non-blank content line between file line 55 (BEGINS) and file line 225 (ENDS)
using `perl -ne 'if ($. >= 56 && $. <= 224) {...}'` matching the
`^\s*(\d+)\s\s(.*)$` line-number-prefix pattern and testing for non-empty
trailing text = **84**. This independently reproduces A1's own header claim
of 84. SWEEP pass = manual walk-through of the full transcript text (Read
tool, all 245 lines read in full), tallying each distinct speaker turn by
hand = **84**, with an identical breakdown by tag: 39 `[Q — <firm>]`, 28
`[A — Mgmt]`, 1 `[Moderator]`, 1 `[Closing — Mgmt]`, 15 unbracketed
(operator/narration, including the 2 unbracketed management turns 9 and 11 —
Chairman opening remarks and CFO financial remarks — which carry no `[A —
Mgmt]` bracket because they precede the Q&A session). GATE A2: pass.

---

## 1. PARTICIPANTS

| # | Name | Designation | Side | First turn # | Flags |
|---|------|-------------|------|---------------|-------|
| 1 | Mr. Srinivasagopalan Rangarajan ("Sranga Rajan" / "Ranga Rajan Sur" — ASR variants) | Chairman & Managing Director | Management | 9 (opening remarks) | Promoter-CMD present — no MGMT_ABSENCE |
| 2 | Mr. Venkata Subramanian Venkatachalam ("Weneta Subman" / "Vener" — ASR variants) | CFO | Management | 11 (financial remarks) | AMBIGUOUS_SPEAKER — after turn 11, all 28 `[A — Mgmt]` Q&A answers are attributed to the generic tag "Mgmt", not split between CMD and CFO; content register (first-person "I", detailed technical/strategic answers) reads as the CMD throughout, but the transcript never confirms the CFO answered zero questions. Flag for A3/A4: cannot verify CFO's individual answer share. |
| 3 | Ms. Prayasi Patel ("Miss Pasi Patel" / "Pasi" — ASR variants) | Moderator, Go India Advisors | Moderator | 7 (introduces call) | Also turn 125 (interjects to redirect Individual investor to rejoin queue) |
| 4 | Har Kraat | Analyst, IIFL Capital ("IFL Capital" ASR) | Analyst | 15 | 4 turns (15,19,23,27) |
| 5 | Rishika | Analyst, Goldman Sachs | Analyst | 31 | 3 turns (31,35,39) |
| 6 | Deepen Wakil | Analyst, Philip Capital | Analyst | 43 | 4 turns (43,47,51,55) |
| 7 | Venit Prasad | Analyst, Invest Capital | Analyst | 59 | 3 turns (59,63,67) |
| 8 | Kavesh Parik | Analyst, 361 Capital | Analyst | 71 | 3 turns (71,75,79) |
| 9 | Neil Obal Sahu | Analyst, JM Financial | Analyst | 83 | 8 turns (83,87,91,95,99,103,107,111) — heaviest Q&A share of any single analyst |
| 10 | "Arab" (per operator introduction) | Individual investor | Analyst/Retail | 115 | 4 turns (115,119,123,127); interrupted by Moderator at turn 125 |
| 11 | Krishnan Sha | Analyst, DAM Capital | Analyst | 131 | 4 turns (131,135,139,143) |
| 12 | Abijit Singh | Analyst, Systematix ("systematics" ASR) | Analyst | 147 | 3 turns (147,151,155) |
| 13 | Bhavya Gandhi | Analyst, Bajaad Alternate Investment Managers ("Bajad" ASR) | Analyst | 159 | 3 turns (159,163,167) |

Participants total: 13 (2 management, 1 moderator, 10 analyst-firm representatives). No MGMT_ABSENCE — both named management (CMD, CFO) present and both deliver prepared remarks.

---

## 2. SPEAKER TURNS (all 84, numbered sequentially)

| Turn # | File line | Speaker/Tag | First ~10 words | Flags |
|---|---|---|---|---|
| 7 | 57 | Operator (unbracketed) | "Ladies and gentlemen, good day and welcome to Data Patterns..." | — |
| 9 | 59 | Mgmt — Chairman & MD, opening remarks (unbracketed) | "Thank you Pasi. Good afternoon ladies and gentlemen and a warm..." | — |
| 11 | 61 | Mgmt — CFO, financial remarks (unbracketed) | "Thank you sir. Good afternoon ladies and gentlemen and thank you..." | — |
| 13 | 63 | Operator, Q&A transition (unbracketed) | "Thank you very much. We will now begin the question..." | — |
| 15 | 65 | [Q — IIFL Capital] | "Thanks for the opportunity sir. Uh first question would be..." | — |
| 17 | 67 | [A — Mgmt] | "Uh see increase in other expenses. is due to some..." | — |
| 19 | 69 | [Q — IIFL Capital] | "Sir and sir on revenue uh in the press release..." | — |
| 21 | 71 | [A — Mgmt] | "Uh we can't be specific because it involves customers..." | HEDGE |
| 23 | 73 | [Q — IIFL Capital] | "Got it. So that's really helpful. So one last question..." | — |
| 25 | 75 | [A — Mgmt] | "Okay, this question was asked during our AGM warning..." | — |
| 27 | 77 | [Q — IIFL Capital] | "Got it. So that's really helpful. I have more questions..." | NO_NEW_QUESTION (session close) |
| 29 | 79 | Operator, transition to Goldman Sachs (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 31 | 81 | [Q — Goldman Sachs] | "Uh good afternoon sir. Thank you for the opportunity..." | — |
| 33 | 83 | [A — Mgmt] | "Okay. As that product is going on well the developer..." | HEDGE |
| 35 | 85 | [Q — Goldman Sachs] | "Thank you sir. Uh so secondly could you please share..." | — |
| 37 | 87 | [A — Mgmt] | "actually we didn't have lower margin uh I don't know..." | HEDGE |
| 39 | 89 | [Q — Goldman Sachs] | "Sure sir. Thank you." | NO_NEW_QUESTION (session close) |
| 41 | 91 | Operator, transition to Philip Capital (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 43 | 93 | [Q — Philip Capital] | "Hi uh thank you for this opportunity and congratulations on..." | — |
| 45 | 95 | [A — Mgmt] | "okay see I this this varies with the contract..." | — |
| 47 | 97 | [Q — Philip Capital] | "Got it. Got it. Increasing to hear that it's out..." | — |
| 49 | 99 | [A — Mgmt] | "We are not in the platform business as a block..." | — |
| 51 | 101 | [Q — Philip Capital] | "Yeah. Got it. So yeah. Uh so just one last..." | — |
| 53 | 103 | [A — Mgmt] | "Technically very sound company. small company very sound and..." | HEDGE |
| 55 | 105 | [Q — Philip Capital] | "Got it. Sir, thank you so much for answering my..." | NO_NEW_QUESTION (session close) |
| 57 | 107 | Operator, transition to Invest Capital (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 59 | 109 | [Q — Invest Capital] | "Um, hi sir, good afternoon. Um, just a couple of..." | — |
| 61 | 111 | [A — Mgmt] | "okay on the larger platforms there's a male program..." | HEDGE |
| 63 | 113 | [Q — Invest Capital] | "understood um and so lastly uh on the hawk radars..." | — |
| 65 | 115 | [A — Mgmt] | "sure we we've done the hardware for both Nick..." | HEDGE |
| 67 | 117 | [Q — Invest Capital] | "Understood. Understood. Uh thank you so much sir." | NO_NEW_QUESTION (session close) |
| 69 | 119 | Operator, transition to 361 Capital (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 71 | 121 | [Q — 361 Capital] | "Hi sir, thanks for the opportunity. Uh sir, do we..." | — |
| 73 | 123 | [A — Mgmt] | "We expect this to happen this year, this financial year..." | — |
| 75 | 125 | [Q — 361 Capital] | "Further do you have any comments on development of new..." | — |
| 77 | 127 | [A — Mgmt] | "see uh what happens is once you develop a product..." | — |
| 79 | 129 | [Q — 361 Capital] | "Got it sir. Thank you so much. All the very best." | NO_NEW_QUESTION (session close) |
| 81 | 131 | Operator, transition + "2 questions per participant" reminder to JM Financial (unbracketed) | "Thank you. A request to all participants. Please restrict your..." | POLICY_REMINDER (1 of 2) |
| 83 | 133 | [Q — JM Financial] | "Hi sir, good afternoon. Thank you for the opportunity..." | — |
| 85 | 135 | [A — Mgmt] | "I don't know. I'm not classified accordingly. Give you..." | HEDGE |
| 87 | 137 | [Q — JM Financial] | "Thank you. Will you have a classification of" | — |
| 89 | 139 | [A — Mgmt] | "sorry sir can you please come but not give you..." | HEDGE |
| 91 | 141 | [Q — JM Financial] | "uh sure secondly on this order prospect that you have..." | — |
| 93 | 143 | [A — Mgmt] | "Yeah. Seeker also is a potential order until the..." | — |
| 95 | 145 | [Q — JM Financial] | "Pardon?" | — |
| 97 | 147 | [A — Mgmt] | "These are included in our prospects for uh 20..." | — |
| 99 | 149 | [Q — JM Financial] | "Yes. Yes. And the HAL order would also be..." | — |
| 101 | 151 | [A — Mgmt] | "Um I I believe so some portion of it..." | — |
| 103 | 153 | [Q — JM Financial] | "Uh understood understood. Uh also sir can you highlight..." | — |
| 105 | 155 | [A — Mgmt] | "See we uh I don't know how long you've been..." | HEDGE |
| 107 | 157 | [Q — JM Financial] | "it's If I may squeeze in a small question..." | — |
| 109 | 159 | [A — Mgmt] | "Yeah, there is another thing which we are going..." | — |
| 111 | 161 | [Q — JM Financial] | "Got it sir. Thank you so much." | NO_NEW_QUESTION (session close) |
| 113 | 163 | Operator, transition to individual investor (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 115 | 165 | [Q — Individual investor] | "Hello Sir, am I audible? Yes. Uh sir, uh I..." | — |
| 117 | 167 | [A — Mgmt] | "We discussed this in the board meeting yesterday also..." | HEDGE |
| 119 | 169 | [Q — Individual investor] | "thank you sir uh my second question will be will..." | — |
| 121 | 171 | [A — Mgmt] | "Contribution contribution company doesn't have to come only on..." | — |
| 123 | 173 | [Q — Individual investor] | "Uh thank you sir just one last suggestion." | — |
| 125 | 175 | [Moderator] | "Can if you can interrupt you Mr. Ara but can..." | — |
| 127 | 177 | [Q — Individual investor] | "Uh no yeah I had no questions. I was done..." | NO_NEW_QUESTION (session close, post-moderator interrupt) |
| 129 | 179 | Operator, transition + "2 questions per participant" reminder to DAM Capital (unbracketed) | "Thank you. A request to all participants please restrict your..." | POLICY_REMINDER (2 of 2) |
| 131 | 181 | [Q — DAM Capital] | "Uh hi sir, thank you for taking my question. So..." | — |
| 133 | 183 | [A — Mgmt] | "Um the hawk radar is ours. There's no partner." | — |
| 135 | 185 | [Q — DAM Capital] | "No radar is yours, sir. But what I'm trying to..." | — |
| 137 | 187 | [A — Mgmt] | "Uh it's not a DCP partner here. AA is a..." | — |
| 139 | 189 | [Q — DAM Capital] | "So, okay, just to understand for my uh understanding s..." | — |
| 141 | 191 | [A — Mgmt] | "I tell you this is one one option other option..." | — |
| 143 | 193 | [Q — DAM Capital] | "Got it. Thank you so much sir. Thank you so..." | NO_NEW_QUESTION (session close) |
| 145 | 195 | Operator, transition to Systematix (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 147 | 197 | [Q — Systematix] | "Thank you for the opportunity sir. Uh my question is..." | — |
| 149 | 199 | [A — Mgmt] | "we hope to work with DRDO on the platforms..." | — |
| 151 | 201 | [Q — Systematix] | "right sir. Uh and lastly on the order inflow prospects..." | — |
| 153 | 203 | [A — Mgmt] | "are already on tenders are already on we already..." | — |
| 155 | 205 | [Q — Systematix] | "Thank you sir. Thank you for answering my questions." | NO_NEW_QUESTION (session close) |
| 157 | 207 | Operator, transition to Bajaad Alternate (unbracketed) | "Thank you. The next question is from the line of..." | — |
| 159 | 209 | [Q — Bajaad Alternate] | "Yeah. Hi sir, thanks for the opportunity. So just wanted..." | — |
| 161 | 211 | [A — Mgmt] | "Okay. Um if I start investing in products with..." | — |
| 163 | 213 | [Q — Bajaad Alternate] | "So on the 40,000 cr adjustable market that would..." | — |
| 165 | 215 | [A — Mgmt] | "I don't want to say this because I have no..." | HEDGE |
| 167 | 217 | [Q — Bajaad Alternate] | "Right. Got it. Thank you so much and all the..." | NO_NEW_QUESTION (session close) |
| 169 | 219 | Operator, "last question" + hand to Mgmt for closing (unbracketed) | "Thank you ladies and gentlemen. Due to time constraints..." | — |
| 171 | 221 | [Closing — Mgmt] | "Thank you. Thank you. Uh thanks all of you for..." | — |
| 173 | 223 | Operator sign-off (unbracketed) | "Thank you. On behalf of Go India Advisor, that concludes..." | — |

Total turns: 84 (39 Q + 28 A + 1 Moderator + 1 Closing + 15 unbracketed). Matches COUNT TEST.

---

## 3. QUESTIONS (analyst turns, one row per `[Q — ...]` turn)

Where an analyst turn is a session-closing courtesy ("Got it, thank you") with
no new substantive ask, it is flagged `NO_NEW_QUESTION` (still enumerated per
operating rule — nothing is dropped) rather than a topic.

| Turn # | Analyst / Firm | Topic | Flags |
|---|---|---|---|
| 15 | IIFL Capital | Other expenses up 64% YoY vs 17% revenue growth — driver? | REPEAT_QUESTION (margin/cost-variance cluster, w/ turn 35) |
| 19 | IIFL Capital | Revenue slippage from delayed customer approvals — quantum? | — |
| 23 | IIFL Capital | Timeline for Rs 1,726 Cr negotiated-pending orders to convert to confirmed order book | REPEAT_QUESTION (order-book/negotiated-pipeline cluster, w/ 43,91,95,99,103,151) |
| 27 | IIFL Capital | (session close, "will call back") | NO_NEW_QUESTION |
| 31 | Goldman Sachs | SPJ-230 ("Java ports for 230") testing update + medium-term revenue contribution | — |
| 35 | Goldman Sachs | Why margins lower this quarter, outlook for FY27 | REPEAT_QUESTION (margin/cost-variance cluster, w/ turn 15) |
| 39 | Goldman Sachs | (session close) | NO_NEW_QUESTION |
| 43 | Philip Capital | HAL order (>Rs 10bn) conversion timeline; confirms it sits outside 17bn negotiated | REPEAT_QUESTION (order-book/negotiated-pipeline cluster) |
| 47 | Philip Capital | Counter-drone / export business — product portfolio, platform vs subsystem | REPEAT_QUESTION (counter-drone cluster, w/ turn 159) |
| 51 | Philip Capital | ST Advance acquisition — rationale, target applications (MiG-29/Su-30 upgrades?) | — |
| 55 | Philip Capital | (session close) | NO_NEW_QUESTION |
| 59 | Invest Capital | Larger platforms targeted as subsystem developer (3-5yr horizon); Himshakti project status | — |
| 63 | Invest Capital | Hawk radars — monetization path, Su-30 upgrade fit | REPEAT_QUESTION (hawk-radar cluster, w/ turns 131,135,139) |
| 67 | Invest Capital | (session close) | NO_NEW_QUESTION |
| 71 | 361 Capital | Brahmos fire-control/seeker — commercial order timeline | REPEAT_QUESTION (Brahmos cluster, w/ turns 91 context, mgmt opening turn 9) |
| 75 | 361 Capital | New Brahmos subsystems — incremental wallet share; capacity to meet rising demand | REPEAT_QUESTION (Brahmos cluster) |
| 79 | 361 Capital | (session close) | NO_NEW_QUESTION |
| 83 | JM Financial | Rs 2,600 Cr order book — production vs development split | — |
| 87 | JM Financial | Follow-up: will a classification be provided | — |
| 91 | JM Financial | Rs 20-40bn order prospect — does it include HAL + Brahmos seeker orders | REPEAT_QUESTION (order-book/negotiated-pipeline cluster) |
| 95 | JM Financial | "Pardon?" (clarification request) | NO_NEW_QUESTION |
| 99 | JM Financial | Confirms these are prospects, not confirmed orders | — |
| 103 | JM Financial | Confirms HAL order included in same prospect bucket | REPEAT_QUESTION (order-book/negotiated-pipeline cluster) |
| 107 | JM Financial | Other prospects beyond Brahmos converting to production over next 2-3 years | — |
| 111 | JM Financial | Capex plan for next two years | — |
| 115 | Individual investor | Space business — stance revisited (deferred ~1-2 years ago) | — |
| 119 | Individual investor | Subsidiary (aggregation/composites business) — value-add plan | — |
| 123 | Individual investor | "One last suggestion" | interrupted by Moderator (turn 125) before completing |
| 127 | Individual investor | (confirms no further question, done) | NO_NEW_QUESTION |
| 131 | DAM Capital | Hawk radar development — Astra Microwave's role as alleged DCP partner | REPEAT_QUESTION (hawk-radar cluster) |
| 135 | DAM Capital | Clarifies asking about DCP partner generally, not ownership | REPEAT_QUESTION (hawk-radar cluster) |
| 139 | DAM Capital | DRDO software / Astra hardware split — confirm division of labor | REPEAT_QUESTION (hawk-radar cluster) |
| 143 | DAM Capital | (session close) | NO_NEW_QUESTION |
| 147 | Systematix | Naval program — plans to raise share of naval-platform exposure | — |
| 151 | Systematix | Risk of Rs 20bn order-inflow prospects slipping to FY28 | REPEAT_QUESTION (order-book/negotiated-pipeline cluster) |
| 155 | Systematix | (session close) | NO_NEW_QUESTION |
| 159 | Bajaad Alternate | Addressable market size for key products; counter-drone revenue/order outlook | REPEAT_QUESTION (addressable-market cluster w/ turn 163; counter-drone cluster w/ turn 47) |
| 163 | Bajaad Alternate | Rs 40,000 Cr addressable market — over how many years? | REPEAT_QUESTION (addressable-market cluster) |
| 167 | Bajaad Alternate | (session close) | NO_NEW_QUESTION |

Questions total: 39. Matches COUNT TEST.

REPEAT_QUESTION clusters identified (topic asked by 2+ distinct analysts,
each instance flagged above): (1) order-book/negotiated-pipeline scope &
timeline — IIFL, Philip, JM Financial (x4), Systematix — heaviest cluster,
6 distinct turns across 4 firms; (2) margin/cost-variance — IIFL, Goldman;
(3) hawk-radar program — Invest Capital, DAM Capital (x3 turns); (4)
counter-drone business — Philip, Bajaad; (5) addressable-market (~Rs
40,000 Cr TAM) sizing — Bajaad (x2 turns, and volunteered unprompted by
management at JM Financial's turn 107 answer); (6) Brahmos — 361 Capital
(x2 turns), echoing management's own opening-remarks mention (turn 9).

---

## 4. MANAGEMENT NUMBERS (every discrete quantitative claim, for Role-5
arithmetic-consistency reconciliation against the filing baseline)

Rows marked `[ANALYST_STATED]` are numbers an analyst introduced in a `[Q]`
turn that management then engaged with/confirmed in the following `[A]`
turn — included per task instruction because they anchor a management
confirmation and must reconcile against the filing (e.g. the Rs 1,726 Cr
and Rs 20-40bn figures never appear verbatim in a management sentence, only
in management's confirmatory response to the analyst's number).

| # | Claim | Value | Turn # | Flags |
|---|---|---|---|---|
| 1 | Order book incl. negotiated | Rs 2,654 Cr | 9 | — |
| 2 | International order book | Rs 39 Cr | 9 | — |
| 3 | Fresh order-inflow target, FY27 | ~Rs 2,000 Cr | 9 | RECONCILE w/ #27, #47 |
| 4 | Revenue growth guidance, FY27 | 20-25% (transcript garbled "2025%") | 9 | NUMBER_TRANSCRIPTION_AMBIGUITY |
| 5 | EBITDA margin guidance, FY27 | 35-40% | 9 | — |
| 6 | Revenue, Q1 FY27 | Rs 116 Cr | 11 | — |
| 7 | Revenue YoY growth | 17% | 11 | — |
| 8 | Gross profit | Rs 91.5 Cr | 11 | — |
| 9 | Gross profit YoY growth | 16% | 11 | — |
| 10 | Gross margin | 78.9% | 11 | — |
| 11 | EBITDA | Rs 31.4 Cr | 11 | — |
| 12 | EBITDA margin | 27% | 11 | — |
| 13 | PAT | Rs 22.1 Cr | 11 | — |
| 14 | PAT margin | 19% | 11 | — |
| 15 | Cash + bank balances + investments (as on 30-Jun-2026) | Rs 530 Cr | 11 | — |
| 16 | Confirmed order book (as on 30-Jun-2026, transcript mis-transcribes "order book" as "audible") | Rs 920 Cr | 11 | — |
| 17 | Order book incl. negotiated (reiteration) | Rs 2,654 Cr | 11 | RECONCILE w/ #1 — consistent, same figure restated |
| 18 | [ANALYST_STATED] Other expenses YoY growth | 64% | 15 | ANALYST_STATED; addressed by mgmt turn 17 |
| 19 | Receivables provision (additional, this quarter) | ~Rs 2 Cr | 17 | — |
| 20 | Target order-book horizon for stable quarterly delivery | "at least three years" of revenue visibility | 21 | qualitative/timeframe |
| 21 | [ANALYST_STATED] Negotiated-pending order book (outside confirmed order book) | ~Rs 1,726 Cr ("17 odd billion rupees") | 23 | ANALYST_STATED; RECONCILE w/ #35, #48 |
| 22 | [ANALYST_STATED] Proposed conversion window queried | 6-9 months | 23 | ANALYST_STATED |
| 23 | Program delay already incurred | additional 6 months | 25 | — |
| 24 | Additional extension granted (on one program) | 2 months | 25 | — |
| 25 | Expected conversion timeline (safer-side estimate; could be as fast as 2 weeks) | "3 months" | 25 | — |
| 26 | Total program stretch (vs original timeline) | "more than one and a half years" | 25 | — |
| 27 | Additional simulator-contract opportunity | ~Rs 2,000 Cr | 25 | RECONCILE w/ #3 — unclear if same FY27 pool or a distinct upside bucket |
| 28 | SPJ-230 qualification/flight-trial timing | "before December [2026]" | 33 | — |
| 29 | SPJ-230 contract materialization timeline | "maybe next two years" | 33 | — |
| 30 | SPJ-230 deal-size description | "several thousand crores" (unquantified) | 33 | vague/unquantified |
| 31 | [ANALYST_STATED] Total prospect pipeline referenced | "70 billion" (~Rs 7,000 Cr) | 43 | ANALYST_STATED; not explicitly confirmed by mgmt — RECONCILE |
| 32 | [ANALYST_STATED] HAL order size referenced | "more than 10 billion" (~Rs 1,000 Cr+) | 43 | ANALYST_STATED |
| 33 | Project execution timeframe (large single-lot orders) | 18-24 months | 45 | — |
| 34 | Typical delivery timeframe observed generally | "two to three years" | 45 | — |
| 35 | Clarification: HAL order is NOT part of the Rs 1,726 Cr negotiated figure | qualitative | 45 | RECONCILE FLAG vs #21, confirmed again at #48 |
| 36 | L1 status disclosed on one large contract, value undisclosed | qualitative | 45 | vague/unquantified |
| 37 | MOD pilot/experimental counter-drone order quantities | "10 to 20 systems" per vendor | 49 | — |
| 38 | Counter-drone contract fortification timeline | "next 3 to 6 months" | 49 | — |
| 39 | UK antenna-redesign export delivery timeline | "next 6 to 8 months" | 49 | — |
| 40 | Export business near-term scale | "multi-million dollar business" within "next few months" | 49 | vague/unquantified |
| 41 | Export scaling horizon | "next two to three years" | 49 | — |
| 42 | SPJ platform aircraft-fleet reference | "270 aircrafts" | 61 | — |
| 43 | Hawk-radar software/hardware breakthrough timeline | "next two to three months" | 65 | — |
| 44 | Advanced hawk-radar (2nd-gen) systems ready | "next six months" | 65 | — |
| 45 | Brahmos seeker commercial order timing | "this financial year" (FY27) — product intake, not revenue | 73 | — |
| 46 | [ANALYST_STATED] Order-prospect pipeline range | "20 to 40 billion" (~Rs 2,000-4,000 Cr) | 91 | ANALYST_STATED; RECONCILE w/ #3, #47 |
| 47 | Single-vendor order target confirmed | Rs 20 billion (~Rs 2,000 Cr) prospects | 97 | RECONCILE w/ #46 (lower bound), #3 |
| 48 | HAL order confirmed within "additional 20 billion" prospect pool, not negotiated bucket | qualitative | 101 | RECONCILE w/ #35, #21 |
| 49 | Radar-program contract opportunity size | "few thousands of crores" | 105 | vague/unquantified |
| 50 | Timeline for radar contract wins | "next 1.5 to 2 years" | 105 | — |
| 51 | Total addressable market (TAM), self-corrected mid-sentence from garbled "40-50 billion" | "Rs 40,000-50,000 Cr" | 105 | NUMBER_TRANSCRIPTION_AMBIGUITY; RECONCILE w/ #57, #60, #61 |
| 52 | Capex plan, next two years | "Rs 200 Cr+" (minimum) | 109 | — |
| 53 | Capex timeframe | "next one to two years" | 109 | — |
| 54 | Decision timeline on space-business investment | "3 to 4 months" | 117 | — |
| 55 | Naval/coast-guard radar order (potential) | "30 systems" | 149 | — |
| 56 | Self-imposed contract-conversion timeline for the 20-40bn pipeline | "9 months" | 153 | — |
| 57 | TAM reiteration | "40 billion market" — unit ambiguous (Rs 4,000 Cr if billion=100cr taken literally, vs Rs 40,000 Cr implied by context) | 153 | NUMBER_TRANSCRIPTION_AMBIGUITY; RECONCILE w/ #51 |
| 58 | Addressable market — already-developed products | Rs 30,000 Cr | 161 | — |
| 59 | Additional repeat-contract addressable market | Rs 10,000-12,000 Cr | 161 | — |
| 60 | Total TAM (sum of #58+#59) | ~Rs 40,000 Cr | 161 | RECONCILES/CONFIRMS #51, #57 |
| 61 | [ANALYST_STATED] TAM restated by analyst | Rs 40,000 Cr | 163 | ANALYST_STATED; consistent w/ #60 |
| 62 | Mechanical design team size | "more than 100 engineers" | 171 | — |
| 63 | Radar payload capacity handled | "140 tons" movement mechanism | 171 | — |
| 64 | EW business maturation timeline | "six months to one year" | 171 | — |
| 65 | AI product development timeline | "one to one-and-a-half years" | 171 | — |
| 66 | Export program start timeline | "next few months" | 171 | — |

Management numbers total: 66. Matches COUNT TEST.

**Reconciliation flags for A3/A4 (summary):**
- **RECONCILE_FLAG — order-book/pipeline stack**: three overlapping but
  not-obviously-additive figures in play — Rs 920 Cr confirmed order book
  (#16), Rs 1,726 Cr negotiated-pending (#21, analyst-stated, mgmt-adjacent
  #17/#25 do not explicitly restate the figure), Rs 2,654 Cr order book
  incl. negotiated (#1/#17 — appears to be roughly 920 + 1,726 but 920 +
  1,726 = 2,646, a Rs 8 Cr gap vs the stated 2,654 that should be checked
  against the filing), Rs 2,000 Cr FY27 fresh-inflow target (#3), and Rs
  20bn/Rs 20-40bn additional prospect pipeline (#46/#47) which explicitly
  excludes the HAL order from the negotiated bucket (#35/#48) but explicitly
  includes it in the pipeline bucket — A3/A4 must map which HAL order size
  (#32, "more than 10 billion") sits inside which bucket.
- **RECONCILE_FLAG — TAM figures**: Rs 40,000-50,000 Cr (#51, turn 105) vs
  "40 billion" (#57, turn 153, unit-ambiguous) vs Rs 30,000 + 10-12,000 =
  ~40,000 Cr (#58-60, turn 161) vs analyst restatement of Rs 40,000 Cr
  (#61, turn 163) — these appear to converge on ~Rs 40,000 Cr but the
  transcript's own arithmetic self-corrections (#4, #51, #57) are ASR/human
  transcription artifacts per the A1 fidelity note, not confirmed filing
  figures — do not treat as anchored without corroboration.
- **NUMBER_TRANSCRIPTION_AMBIGUITY**: #4 (revenue growth guidance rendered
  "2025%", almost certainly "20-25%"), #51 (self-corrected "40-50 billion"
  to "40,000-50,000 crores" mid-sentence), #57 ("40 billion" market size
  stated without the crore-scale correction seen at #51/#60).

---

## 5. FORWARD-COMMITMENT PHRASES (management turns only; analyst turns
using similar phrasing, e.g. "are we targeting..." at turns 51 and 75, are
excluded as those are analyst framing, not management commitment)

| # | Turn # | Phrase (context) | Flags |
|---|---|---|---|
| 1 | 9 | "we believe data patterns is well positioned to benefit" | — |
| 2 | 9 | "we remain committed to investing in the technology innovation..." | — |
| 3 | 21 | "we believe that our revenue will be met quarter to quarter as we go along" | — |
| 4 | 25 | "we expect out of the programs...the order can get placed" | — |
| 5 | 25 | "we expect that two months those contracts should happen" | — |
| 6 | 25 | "the order has got postponed...we expected" | — |
| 7 | 25 | "another 2,000 crores which we expect to happen during the course of this financial year" | numeric — see mgmt_numbers #27 |
| 8 | 25 | "coming years substantively is what we believe" | — |
| 9 | 25 | "[contract] should happen" (negotiated orders) | — |
| 10 | 33 | "we believe that...should happen before December" | numeric — see mgmt_numbers #28 |
| 11 | 33 | "should happen" (qualification/trials) | — |
| 12 | 33 | "we expecting out of it" (deal scale, hedged immediately after — see hedge #2) | — |
| 13 | 87 | "we are confident of achieving the full year...targeted margins" | — |
| 14 | 99 | "we believe we have a good order pipeline" | — |
| 15 | 99 | "we expect the far more healthier order on the active detection" | — |
| 16 | 99 | "we believe will cover the entire specification" | — |
| 17 | 99 | "we expect that those contracts will also start [happening]" | — |
| 18 | 103 | "we believe it's an important acquisition" | — |
| 19 | 111 | "we believe we should make a mark providing our products" | — |
| 20 | 111 | "we expect that...with the technology edge...we should be able to convince the customer" | — |
| 21 | 123 | "the contract should happen...believe that it should happen this year" | numeric — see mgmt_numbers #45 |
| 22 | 127 | "what we expect and we'll deliver this" | — |
| 23 | 147 | "included in our prospects for...20 [billion]" ("targeting") | numeric — see mgmt_numbers #47 |
| 24 | 155 | "we expect repeat contracts and all of that" | — |
| 25 | 155 | "already work well so we expect repeat contracts" | duplicate of #24 within same turn (2 instances) |
| 26 | 171 | "this is our belief. I believe we will do this" | — |
| 27 | 203 | "this contact should happen" | — |
| 28 | 211 | "we believe that contact will happen" | — |
| 29 | 221 | "grow the business very fast is what we believe" | — |

Forward-commitment total: 29 distinct phrase instances across 16 management
turns (9, 21, 25 [×5], 33 [×2], 87, 99 [×4], 103, 111 [×2], 123 [×2], 127,
147, 155 [×2], 171, 203, 211, 221). This is a mechanical lexicon sweep
("we believe" / "we expect" / "should happen" / "committed to" / "our
belief" / "we are confident" / "targeting") cross-checked against a manual
re-read of every `[A — Mgmt]`, `[Closing — Mgmt]`, and the two unbracketed
management turns (9, 11); it is not claimed exhaustive of every possible
softer future-tense phrasing in this highly discursive, unedited transcript,
but every instance of the core forward-commitment lexicon is captured with
turn number.

---

## 6. HEDGE PHRASES (management turns; lexicon: "can't be specific" / "don't
want to" / "too early" / "not appropriate" / "no control" / "can't comment"
/ "can't say" / "not classified" / "I don't know" / "unsure" / "can't
guess")

| # | Turn # | Phrase (context) | Flags |
|---|---|---|---|
| 1 | 21 | "we can't be specific because it involves customers...can't talk about open channel" | re: revenue-slippage quantum (IIFL Q19) |
| 2 | 33 | "I don't want to...out I have a number in mind" | re: SPJ-230 order size |
| 3 | 33 | "it's not appropriate to talk about a future order" | re: SPJ-230 order size |
| 4 | 37 | "I don't know look at the last margins" | re: margin trend framing |
| 5 | 53 | "it's a bit too early because yesterday only finalized" | re: ST Advance acquisition scope, deal closed day before call |
| 6 | 61 | "I can't comment exactly on when the contact will [happen]" | re: SNS/next-gen platform program |
| 7 | 65 | "I can't very clearly say which will happen when faster" | re: hawk-radar OEM software collaboration |
| 8 | 85 | "I don't know. I'm not classified accordingly" | re: order-book production vs development split — declined outright |
| 9 | 89 | "I have not classified it...don't have a needed answer" | re: same order-book classification, repeated decline |
| 10 | 105 | "I don't want to be specific on what products being developed" | re: undisclosed pipeline products |
| 11 | 117 | "I'm still unsure about what investments will happen from government" | re: space-business funding decision |
| 12 | 161 | "it's a bit premature for me to talk about it now" | re: TAM monetization timing |
| 13 | 161 | "we can't comment much on it on when exactly it will happen" | re: same, second hedge in same turn |
| 14 | 165 | "I don't want to say this because I have no control over the market" | re: TAM realization timeline (Bajaad Q163) |

Hedge total: 14 distinct phrase instances across 12 management turns (21,
33 [×2], 37, 53, 61, 65, 85, 89, 105, 117, 161 [×2], 165). Same
mechanical-lexicon-plus-manual-reread method as Section 5; not claimed
exhaustive of every softer deflection in the transcript, but every instance
of the core hedge lexicon is captured with turn number. Notably, turns 85
and 89 are consecutive hedges on the identical question (order-book
production/development classification) — management declines twice running
before the analyst moves on; worth flagging to A3/A4 as a clean refusal, not
an oversight.

---

## FLAGS SUMMARY (for downstream A3/A4/A5 reconciliation)

- **REPEAT_QUESTION** — 6 topic clusters spanning 15 of 39 question-turns
  (order-book/pipeline, margin/cost-variance, hawk-radar, counter-drone,
  addressable-market, Brahmos). See Section 3.
- **ANALYST_STATED** — 4 quantitative claims (mgmt_numbers #18, #21, #22,
  #31, #32, #46, #61 — 7 rows) that originate from an analyst's own
  figure, not a management utterance; management's response is a
  confirmation/engagement, not a restatement of the number itself in most
  cases. Flag so A3/A4 do not mis-attribute these as company-disclosed.
- **RECONCILE_FLAG** — order-book/pipeline stack arithmetic (Rs 920 + 1,726
  ≈ 2,654, off by Rs 8 Cr against the stated total) and the TAM figure
  family (Rs 40,000-50,000 Cr / "40 billion" / Rs 30,000+10-12,000 Cr / Rs
  40,000 Cr) both need explicit reconciliation against the Q1 FY27 filing
  baseline in stage A3/A4.
- **NUMBER_TRANSCRIPTION_AMBIGUITY** — 3 instances (revenue-growth guidance
  "2025%", TAM "40-50 billion" self-corrected mid-sentence, TAM "40
  billion" restated without crore-scale correction) reflecting the
  transcript's own auto-transcribed/uncorrected status per A1's fidelity
  note. Treat as directional, not anchored, until corroborated.
- **AMBIGUOUS_SPEAKER** — all 28 `[A — Mgmt]` Q&A answers are unattributed
  between CMD and CFO; cannot verify individual answer share.
- **NO_NEW_QUESTION** — 11 of 39 `[Q]` turns are session-closing courtesies
  carrying no new substantive ask (enumerated per operating rule, not
  dropped). See Section 3.
- **POLICY_REMINDER** — operator invokes the "restrict to two questions,
  rejoin the queue" rule twice (turns 81, 129).
- **ZERO_STANDING** — not applicable to this doctype (concall transcript
  carries no financial line-item table; the CFO's spoken figures in turn 11
  are a narrative summary, not a tabulated statement, so no zero/nil/dash
  standing items exist to enumerate).
- **MGMT_ABSENCE** — not raised; Chairman & MD (promoter) and CFO both
  present and both deliver prepared remarks.
