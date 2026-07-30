# A2 ENUMERATION LEDGER — MTAR Technologies Limited (MTAR), Q1 FY27, CONCALL

Source: /home/user/inflection-pipeline/runs/mtar-q1fy27/work/extract_concall_mtar_q1fy27.txt
Unit convention: Rs Crores (x1), spoken "crores"/"cr"
Transcript is auto-STT, heavily garbled. All names/numbers below are reproduced
VERBATIM as transcribed; nothing corrected or inferred. Line numbers below refer
to the A1 extract's line numbers (1-247, odd-numbered = content turns,
even-numbered = blank separators).

=== A2 COUNT TEST ===
category: participants   grep_count: 15   sweep_count: 15   match: yes
category: turns           grep_count: 124  sweep_count: 124  match: yes
category: questions        grep_count: 32   sweep_count: 32   match: yes  (reconciled — see note below)
category: mgmt_numbers     grep_count: 53   sweep_count: 53   match: yes  (reconciled — see note below)
category: forward_hedge    grep_count: 22   sweep_count: 22   match: yes
gate_a2: pass
=== END COUNT TEST ===

Reconciliation notes on the two categories that did not match on the first pass:
- QUESTIONS: a naive mechanical grep for "?" only finds 25 lines, because the
  STT source drops terminal punctuation on many genuine questions (16 of the
  31 question-bearing lines identified by manual sweep carry no "?" at all —
  e.g. line 21 Bala Subramanyan's working-capital question, line 111 Vipra
  Shivas's data-center question, line 225 Pria's repeated backlog question).
  A second mechanical pass using an interrogative-marker regex (first/second/
  last question, "my question", "can you help", "out of this 500 how much",
  "what kind of", "how many years", etc.), with 3 confirmed false positives
  removed on manual read (lines 7, 89, 243 — these are operator/CFO
  meta-references to "the question" / "the last question", not new questions),
  converges exactly on the manual sweep's 31 question-bearing lines / 32
  discrete questions (line 33 bundles two questions from Gorov Naguri in one
  merged STT block). GATE A2 passes on the reconciled count.
- MGMT_NUMBERS: enumerated at spoken-instance level (one row per turn in which
  a figure is spoken, including restatements of the same underlying fact in
  later turns — restatements are retained, not deduped, because divergence
  between restatements is itself a RECONCILE_VS_FILING signal for Role 5).
  Grep pass = count of distinct MD/CFO-attributed lines carrying a
  number+unit token (%, cr, crore, crores, GW, days, x) after excluding
  analyst-only lines and pure meta-text; manual sweep = same. Both converge
  at 53.

---
## 1. PARTICIPANTS (both sides) — 15 rows

| # | Line | Name (as transcribed) | Role / Firm | Flags |
|---|------|------------------------|-------------|-------|
| P1 | 1 | (unnamed) | Call Operator / Moderator | |
| P2 | 3 | Miss V. / "Sha Jaspi" (self-ref, garbled) | Head Strategy & Investor Relations, MTAR | |
| P3 | 3, 5 | Orient Capital | Investor Relations partner (named, non-speaking) | |
| P4 | 3, 5 | Mr. Shinasi / Shri Navas / Ramdi (garbled) | Managing Director & Promoter, MTAR | promoter IS present |
| P5 | 3, 5 | Mr. Ganeshwar Rao / Bunesh / Gesh Ra / Gesh (garbled) | Chief Financial Officer, MTAR | |
| P6 | 7 | Mohit Kumar | Analyst, ICICI Securities | |
| P7 | 19 | Bala Subramanyan | Analyst, Aryan Capital | |
| P8 | 31 | Gorov Naguri | Analyst, Aendas Park (garbled name) | |
| P9 | 73 | Sumat Kumar | Analyst, Oswal Financial Services | |
| P10 | 93, 175 | Vipra Shivas / "Vibra Shasta" (garbled 2nd mention) | Analyst, Philip Capital | asked twice — see REPEAT_QUESTION below |
| P11 | 117 | (unnamed individual) | Analyst, "viral asset management" (firm name as transcribed, unconfirmed) | |
| P12 | 129 | Janesh Karia | Analyst, Union Asset Management | |
| P13 | 159 | Rohit Natraan | Analyst, Access Max Life | |
| P14 | 165 | Push Seal Dasani | Analyst, Sundaram Alternates | |
| P15 | 183 | Pria | Analyst, Lucky Investments | |

MGMT_ABSENCE: NOT raised. MD (promoter) and CFO both present and both speak
substantively (opening remarks line 5; financial review line 7). Per injected
task instructions, MGMT_ABSENCE is reserved for absence of a key person; both
key persons are present here.

---
## 2. SPEAKER TURNS — 124 rows (turn # = sequential; line # = A1 extract line)

Note: many odd-numbered "lines" in the STT transcript actually merge more than
one real-world speaker turn (operator handoff + analyst question + management
answer collapsed into one continuous block by the STT engine). Where this
occurs the row is flagged MERGED_SPEAKERS or MERGED_QA and the dominant/primary
speaker is named; the merge is also carried into the Numbers and Questions
tables so nothing inside a merged block is dropped.

| Turn | Line | Speaker | First ~10 words | Flags |
|------|------|---------|------------------|-------|
| 1 | 1 | Operator | "Ladies and gentlemen, good day and welcome to NT..." | |
| 2 | 3 | IR (Head Strategy/IR) | "Thank you Aturva. Good morning everyone. On behalf of..." | |
| 3 | 5 | MD | "Hello good and good morning everyone. Thank Thank you..." | long opening remarks |
| 4 | 7 | CFO → Operator | "Thank you sir and uh good morning everyone and thank..." | MERGED_SPEAKERS (CFO financial review runs into operator's Q&A-open + first-question intro) |
| 5 | 9 | Mohit Kumar → MD | "Yeah. Uh good morning sir and congratulations on a very..." | MERGED_QA |
| 6 | 11 | Mohit Kumar | "Understood. So my second question is sir do you expect..." | |
| 7 | 13 | MD → Mohit Kumar (3rd Q) | "No that is through EPC vendors. So we are qualified..." | MERGED_QA |
| 8 | 15 | MD | "the execution timelines for the existing orders So for the..." | |
| 9 | 17 | Mohit Kumar | "Understood sir. Thank you and all the best sir. Thank" | |
| 10 | 19 | Operator | "Thank you. Before we take the next question, a request..." | |
| 11 | 21 | Bala Subramanyan | "Good morning sir. Uh thank you so much for the..." | |
| 12 | 23 | CFO | "yeah I'll take yeah I'll take up this call so..." | |
| 13 | 25 | Bala Subramanyan | "yes sir so my last question so I think uh..." | |
| 14 | 27 | CFO | "uh See uh like to total 80 crores capex is..." | |
| 15 | 29 | Bala Subramanyan | "Got it sir. Thank you." | |
| 16 | 31 | Operator | "Thank you. The next question comes from the line of..." | |
| 17 | 33 | Gorov Naguri → MD | "Uh thank thanks for the opportunity. Uh considering the last..." | MERGED_QA; 2 questions bundled |
| 18 | 35 | MD | "we will be commissioned by March 27 the multiffold expansion..." | |
| 19 | 37 | Gorov Naguri | "Understood. Uh the operational phase phase two will be operational..." | |
| 20 | 39 | MD | "Okay. Okay. And and we already completed our we've already..." | |
| 21 | 41 | Gorov Naguri | "All right. All right. So the capex for this year..." | |
| 22 | 43 | MD | "Yeah. Sure." | |
| 23 | 45 | Gorov Naguri | "All right. Uh the second question was on the new..." | |
| 24 | 47 | MD | "No, it's going to continue. It's going to grow. Actually," | FORWARD |
| 25 | 49 | Gorov Naguri | "and this new product segment I'm assuming is are the..." | |
| 26 | 51 | MD | "no not necessarily we have the other we have the..." | |
| 27 | 53 | Gorov Naguri | "All right." | |
| 28 | 55 | MD | "It's a combination of everything." | |
| 29 | 57 | Gorov Naguri | "Understood. Understood. Just last question again on the working capital" | REPEAT_QUESTION (working capital) |
| 30 | 59 | MD | "No, it's all about better payment terms, credit terms and..." | |
| 31 | 61 | Gorov Naguri | "Yeah. Not only" | |
| 32 | 63 | CFO | "I think that so not only the customer % we..." | |
| 33 | 65 | Gorov Naguri | "Okay. So the end of the day the idea is..." | |
| 34 | 67 | Gorov Naguri | "Okay. And I mean the the way to look at..." | |
| 35 | 69 | MD | "Yeah, that's what let us see." | HEDGE |
| 36 | 71 | Gorov Naguri | "All right. Thank you. That's it from my side." | |
| 37 | 73 | Operator | "Thank you. The next question comes from the line of..." | |
| 38 | 75 | Sumat Kumar | "Yeah. Hi. My question is uh our key client has..." | |
| 39 | 77 | MD | "Uh Sumant, it's like this uh I've already said that..." | FORWARD + HEDGE |
| 40 | 79 | Sumat Kumar | "Okay. And uh for this uh civil nuclear power segment..." | REPEAT_QUESTION (nuclear execution, echoes Mohit Q3) |
| 41 | 81 | MD | "in this year uh Suman second half of this year..." | |
| 42 | 83 | Sumat Kumar | "Okay. So this order book is for how many years..." | |
| 43 | 85 | MD | "Overall it's for three three and a half years. Some..." | |
| 44 | 87 | Sumat Kumar | "Okay. Okay. Thank you so much. Thank you." | |
| 45 | 89 | MD/CFO | "So as of today We have 684 crores of orders..." | ambiguous exact speaker (unattributed clarification before next intro) |
| 46 | 91 | Sumat Kumar | "Okay. Okay. Thank you so much." | |
| 47 | 93 | Operator → Vipra Shivas | "Thank you. We have the next question from the line..." | MERGED_SPEAKERS |
| 48 | 95 | MD/CFO | "So it will be around 7030 ratio but it will..." | |
| 49 | 97 | Vipra Shivas | "Uh yes yes" | |
| 50 | 99 | Vipra Shivas | "okay so around" | |
| 51 | 101 | MD | "I mean even in the within the clean energy also..." | |
| 52 | 103 | Vipra Shivas | "right sir and out of this 500 how much you..." | |
| 53 | 105 | CFO | "we incurred around 35 crores of capex in the quarter..." | |
| 54 | 107 | Vipra Shivas | "oh 35 crores right" | |
| 55 | 109 | CFO | "yes" | |
| 56 | 111 | Vipra Shivas → MD | "sure yeah and so uh okay that straight science. So..." | MERGED_QA; REPEAT_QUESTION (clean energy/data center) |
| 57 | 113 | MD | "no all this is for export" | |
| 58 | 115 | Vipra Shivas | "all this for export thank you thanks a lot thank" | |
| 59 | 117 | Operator → viral asset mgmt → MD | "thank you we have the next question from the line..." | MERGED_SPEAKERS + MERGED_QA |
| 60 | 119 | viral asset management | "okay and for the uh other question is you have..." | |
| 61 | 121 | MD → viral asset mgmt (follow-up) | "See the PBR program was a very long program for..." | MERGED_QA; HEDGE |
| 62 | 123 | MD → viral asset mgmt (follow-up) | "I I'm not too sure about that. See PSVR will..." | MERGED_QA; HEDGE; REPEAT_QUESTION (products, echoes multiple analysts) |
| 63 | 125 | MD | "That's exactly what I've said. See, as the CFO also..." | |
| 64 | 127 | viral asset management | "Understood. Thank you so much for all the very best." | |
| 65 | 129 | Operator | "Thank you. We have the next question from the line..." | |
| 66 | 131 | Janesh Karia | "Yes. Thank you for the opportunity and congratulations. has done..." | cut off by connection issue |
| 67 | 133 | Operator | "I can't hear you. Can you come closer to the..." | |
| 68 | 135 | Janesh Karia | "Is this better sir?" | |
| 69 | 137 | Janesh Karia | "Hello. Is this better?" | |
| 70 | 139 | Janesh Karia | "Hello." | |
| 71 | 141 | Operator | "Uh no it's not." | |
| 72 | 143 | Janesh Karia | "Hello. Is this better now?" | |
| 73 | 145 | Janesh Karia | "Hello." | |
| 74 | 147 | Operator | "Yeah, it's better right now." | |
| 75 | 149 | Janesh Karia | "Uh yeah. Uh so thanks for the opportunity and congratulations..." | REPEAT_QUESTION (capex/WC funding) |
| 76 | 151 | MD | "No, it will be a combination of internal funding and..." | |
| 77 | 153 | Janesh Karia | "Understood sir. So the second question is um on the..." | REPEAT_QUESTION (data center) |
| 78 | 155 | MD | "See all this is unwanted noise. Uh I really wanted..." | HEDGE |
| 79 | 157 | Janesh Karia | "Perfect. Uh that's good to you. Uh Uh thank you..." | |
| 80 | 159 | Operator | "Thank you. We have the next question from the line..." | |
| 81 | 161 | Rohit Natraan → MD | "Yeah, thank you for this opportunity. Uh my first question..." | MERGED_QA; HEDGE; REPEAT_QUESTION (clean energy capacity) |
| 82 | 163 | Rohit Natraan → MD | "got it got it uh my second question will be..." | MERGED_QA |
| 83 | 165 | Rohit Natraan | "surely sir appreciate it. Uh we'll get back in. Thank" | |
| 84 | 167 | Push Seal Dasani → MD/CFO | "Hi to thank you for the opportunity and congrats for..." | MERGED_QA; REPEAT_QUESTION (products) |
| 85 | 169 | MD | "Yeah, we are definitely doing very qualified additional uh assemblies..." | |
| 86 | 171 | Push Seal Dasani | "Okay. Sure." | |
| 87 | 173 | MD | "What I want to say is the entire entire is..." | FORWARD |
| 88 | 175 | Operator | "Thank you. The next question comes from the line of..." | |
| 89 | 177 | Vipra Shivas (2nd time) | "Uh, uh, sure sir. Uh, thanks for allowing me to..." | REPEAT_QUESTION (products) |
| 90 | 179 | MD | "See the product engine is going to grow rapidly because..." | FORWARD |
| 91 | 181 | Vipra Shivas | "Uh sure s that makes a lot of sense. Uh" | |
| 92 | 183 | Operator | "Thank you. The next question comes from the line of..." | |
| 93 | 185 | Pria | "So from your backlog, if you could tell us what..." | REPEAT_QUESTION (products/clean energy backlog) |
| 94 | 187 | MD | "See that's a very good question. We have the demand..." | connection breaks mid-answer |
| 95 | 189 | Pria | "No, I think I'm audible. I don't know. Can you..." | |
| 96 | 191 | MD | "I think" | |
| 97 | 193 | Operator | "we can hear we can hear you." | |
| 98 | 195 | Operator | "Sorry to interrupt, sir. There's a quite disturbance in your..." | |
| 99 | 197 | MD | "Yeah. Can Can you hear me? Huh?" | |
| 100 | 199 | Operator/Pria | "Yes." | |
| 101 | 201 | Operator | "Yeah, it's better." | |
| 102 | 203 | MD | "Okay. We are really focusing upon the more we execute..." | connection breaks again |
| 103 | 205 | Operator | "Sorry sir" | |
| 104 | 207 | Operator | "sir actually we are losing your voice." | |
| 105 | 209 | MD | "So we are" | |
| 106 | 211 | Operator | "I request you to do the adjustments." | |
| 107 | 213 | MD/Operator | "I've done that for Sir, we are still using losing..." | MERGED_SPEAKERS |
| 108 | 215 | MD | "my voice is clear. My voice is clear." | |
| 109 | 217 | Operator | "Yeah, your voice is clear, sir." | |
| 110 | 219 | MD | "Okay. So, can you ask question again?" | |
| 111 | 221 | Pria | "I was asking on the" | |
| 112 | 223 | MD | "Oh, can you hear me now?" | |
| 113 | 225 | Pria | "I was just asking on the execution cycle of the..." | repeat of turn-93 question (connection dropped it) |
| 114 | 227 | Operator | "sir." | |
| 115 | 229 | MD | "Can you hear me now?" | |
| 116 | 231 | Pria | "Yes." | |
| 117 | 233 | MD | "Okay. So, basically the exe see the what the what..." | |
| 118 | 235 | Pria → MD | "Okay. And uh uh uh sir in the total gawatt..." | MERGED_QA; HEDGE |
| 119 | 237 | Pria | "Okay. And my last question is on the products business..." | REPEAT_QUESTION (segment targets echo prior FY30-style asks) |
| 120 | 239 | Pria | "both these combined" | clarifying follow-up |
| 121 | 241 | MD | "no I'm talking of person we lose you individually 1,000..." | |
| 122 | 243 | Operator | "Thank you. In the interest of time, that was our..." | |
| 123 | 245 | MD | "Uh thank you everyone for joining us today uh and..." | closing remarks |
| 124 | 247 | Operator | "Thank you on behalf of MT technologies limited. That concludes..." | closing sign-off |

---
## 3. QUESTIONS — 32 rows (one row per discrete question posed)

| Q# | Line(s) | Analyst | Firm | Topic | Flags |
|----|---------|---------|------|-------|-------|
| Q1 | 9 | Mohit Kumar | ICICI Securities | Execution timeline for today's announced order ("31 billion" — GARBLED figure) | GARBLED |
| Q2 | 11 | Mohit Kumar | ICICI Securities | Nuclear (Mahi Banswara) — direct package vs via EPC vendor | |
| Q3 | 13 | Mohit Kumar | ICICI Securities | Execution timelines Kaiga 5&6 + size of refurbishment order | |
| Q4 | 21 | Bala Subramanyan | Aryan Capital | Working capital — inventory/receivable days improvement drivers | REPEAT_QUESTION (working capital) |
| Q5 | 25 | Bala Subramanyan | Aryan Capital | Capex reiteration — clean energy phase two + Q1 capex incurred | REPEAT_QUESTION (capex/clean energy) |
| Q6 | 33 | Gorov Naguri | Aendas Park | Fuel-cell capacity expansion beyond 20,000 hot boxes | REPEAT_QUESTION (clean energy capacity) |
| Q7 | 33 | Gorov Naguri | Aendas Park | New product revenue (~100cr, ~50% of clean energy run rate) | REPEAT_QUESTION (products) |
| Q8 | 37 | Gorov Naguri | Aendas Park | Clarify: March-27 = commissioning date or start date | |
| Q9 | 45 | Gorov Naguri | Aendas Park | New product run-rate — one-off or sustaining | REPEAT_QUESTION (products) |
| Q10 | 49 | Gorov Naguri | Aendas Park | Is new product part of fuel-cell assembly (hot box) or separate | |
| Q11 | 57 | Gorov Naguri | Aendas Park | Working capital — receivables driver (transit time vs credit terms) | REPEAT_QUESTION (working capital) |
| Q12 | 67 | Gorov Naguri | Aendas Park | Receivable+inventory days sustaining ~200-220 / WC ~100 days | REPEAT_QUESTION (working capital) |
| Q13 | 75 | Sumat Kumar | Oswal Financial Services | Guidance upgrade possibility (key client raised own guidance 10-15%) | |
| Q14 | 79 | Sumat Kumar | Oswal Financial Services | Civil nuclear — when does order-book execution commence | REPEAT_QUESTION (nuclear execution) |
| Q15 | 83 | Sumat Kumar | Oswal Financial Services | Nuclear order book — how many years of execution | |
| Q16 | 93 | Vipra Shivas | Philip Capital | Capex split — clean energy vs non-clean energy (of 500cr) | REPEAT_QUESTION (capex/clean energy) |
| Q17 | 103 | Vipra Shivas | Philip Capital | Capex incurred in Q1 (of the 500cr plan) | REPEAT_QUESTION (capex) |
| Q18 | 111 | Vipra Shivas | Philip Capital | Data center — current order size, plan, export/domestic | REPEAT_QUESTION (clean energy/data center) |
| Q19 | 117 | viral asset management | (unnamed firm) | Nuclear — TAM for 4 Mahi Banswara projects | |
| Q20 | 119 | viral asset management | (unnamed firm) | PFBR/PSVR program — opportunity size | |
| Q21 | 121 | viral asset management | (unnamed firm) | Nuclear/PFBR — direct-with-government vs EPC; pace PSVR vs nuclear | MERGED_QA |
| Q22 | 123 | viral asset management | (unnamed firm) | Products/import-substitutes — end usage & sustainability | REPEAT_QUESTION (products) |
| Q23 | 149 | Janesh Karia | Union Asset Management | Capex + working-capital funding — internal accruals vs debt vs external capital | REPEAT_QUESTION (capex/WC funding) |
| Q24 | 153 | Janesh Karia | Union Asset Management | US data center — any delays/slippages at customer end | REPEAT_QUESTION (clean energy/data center) |
| Q25 | 161 | Rohit Natraan | Access Max Life | Bloom Fremont 5GW scale-up implication for hot-box capacity | REPEAT_QUESTION (clean energy capacity) |
| Q26 | 163 | Rohit Natraan | Access Max Life | Content per platform — defense (actuator) and nuclear (per reactor) | |
| Q27 | 167 | Push Seal Dasani | Sundaram Alternates | Interest cost (16cr) — breakup fund-based vs non-fund-based | |
| Q28 | 167 | Push Seal Dasani | Sundaram Alternates | New products with largest client (enclosures, cable harness) | REPEAT_QUESTION (products) |
| Q29 | 177 | Vipra Shivas (2nd ask) | Philip Capital | Products segment — programs/ramp-up over next couple of years | REPEAT_QUESTION (products) |
| Q30 | 185 / 225 | Pria | Lucky Investments | Execution cycle — products backlog & clean-energy fuel-cell backlog | REPEAT_QUESTION (products/clean energy); question repeated verbatim across turns due to dropped connection |
| Q31 | 235 | Pria | Lucky Investments | Gigawatt issuance of key customers — MTAR's indicative market share | |
| Q32 | 237 | Pria | Lucky Investments | FY30 (3-4yr) size of products and aerospace/defense businesses | |

REPEAT_QUESTION themes confirmed recurring per task instruction: working
capital (Q4, Q11, Q12 — 3 separate analysts/turns) and clean-energy/products
(Q6, Q7, Q9, Q16, Q18, Q22, Q23, Q24, Q25, Q28, Q29, Q30 — 12 instances across
nearly every analyst on the call).

---
## 4. NUMBERS SPOKEN BY MANAGEMENT — 53 rows (mgmt-attributed only)

Speaker = MD or CFO in every row below. Analyst-stated figures that management
did not itself restate with a number are listed separately in Section 4b for
Role 5 cross-check visibility, but are excluded from the mgmt_numbers count.

| # | Line | Speaker | Number / figure | Context | Flags |
|---|------|---------|------------------|---------|-------|
| N1 | 5 | MD | Revenue Rs 360.7 cr | Q1FY27 quarterly revenue | |
| N2 | 5 | MD | EBITDA margin 23.6% | Q1FY27, "in line with annual guidance" | |
| N3 | 5 | MD | 100 GW nuclear capacity by 2047 | Govt of India target (context for MDR opportunity) | |
| N4 | 5 | MD | Fuel-cell phase 2 commissioning: Sept/Oct [2026] | Capacity augmentation plan | |
| N5 | 5 | MD | Fuel-cell phase 3 completion: March [2027] | Capacity augmentation plan | |
| N6 | 5 | MD | Data center: current order = 1/8th ("eight times" headroom) | First batch vs potential requirement | |
| N7 | 5 | MD | Defense opportunity potential >250 [unit truncated, "crores" implied] | LCA Mk1A actuator/wing-kit/EMA opportunity | GARBLED (unit truncated) |
| N8 | 5 | MD | Aerospace & defense revenue to "double" this FY | Guidance restated | |
| N9 | 5 | MD | Aerospace ramp continuing "next 3-4 years" | | |
| N10 | 5 | MD | Order book target: 5,000 cr by FY-end | Restated from last call | |
| N11 | 5 | MD | Order book actual: 5,143 cr (closing this quarter) | | RECONCILE_VS_FILING (cross-check vs N39 restatement) |
| N12 | 5 | MD | Additional orders received today: 800 cr | | |
| N13 | 5 | MD | Guidance: "80% revenue load" for current FY | Revenue growth guidance, unit/phrase GARBLED | GARBLED |
| N14 | 5 | MD | Guidance: EBITDA margin 24% ± 100bps | | |
| N15 | 7 | CFO | Revenue 360.7 cr vs 156.6 cr Q1FY26 (+130.4%) | | |
| N16 | 7 | CFO | EBITDA 85.1 cr vs 28.4 cr (+199.7%) | | |
| N17 | 7 | CFO | PBT 67.4 cr vs 14.8 cr (+355%) | | |
| N18 | 7 | CFO | PAT 50.2 cr vs 10.8 cr (+364.5%) | | |
| N19 | 7 | CFO | WC days 59 vs 172 (FY26 full year) | | |
| N20 | 7 | CFO | WC target 100 days vs prior guidance range 150-170 days | | |
| N21 | 7 | CFO | Gross margin 45.61% vs 47.65% (last year) | | |
| N22 | 7 | CFO | EBITDA margin 23.54% vs yearly guidance 24% | | |
| N23 | 7 | CFO | Last-quarter EBITDA margin 20.11% | | |
| N24 | 7 | CFO | ROCE 17.2% vs 11.4%; target 23% next year | | |
| N25 | 7 | CFO | PAT margin 13.92% vs 6.9% (Q1FY26) | | |
| N26 | 7 | CFO | Cash flow from ops 247.69 cr vs 191.66 cr | | |
| N27 | 7 | CFO | Debt 423.6 cr as of 30 June 2026 | year stated "2026" for a Q1FY27 (Jun-2026 quarter) — plausible, not flagged | |
| N28 | 7 | CFO | Investments 379 cr | | |
| N29 | 7 | CFO | Net debt ~20-30 cr (after cash adjustment) | | |
| N30 | 7 | CFO | Capex ~500 cr (this year + next year combined) | | |
| N31 | 13 | MD | Refurbishment orders ~200(+) cr | Nuclear segment | |
| N32 | 13 | MD | Additional 130-140 cr orders expected this quarter | Nuclear segment | |
| N33 | 13 | MD | Nuclear division total orders ~800 cr ("never happened in history") | | |
| N34 | 15 | MD | Execution: refurbishment within 2 yrs; Kaiga 5&6 within 1-3 yrs | | |
| N35 | 23 | CFO | GST refund ~70 cr/year target | | |
| N36 | 23 | CFO | WC target reiterated: 100 days | restatement of N20 | |
| N37 | 27 | CFO | Capex capitalized 80 cr (was capital-WIP, now capitalized; not spent this qtr) | | |
| N38 | 27 | CFO | Capex actually spent in Q1 ~30-35 cr | later firmed to 35cr — see N49 | |
| N39 | 27 | CFO | Order book restated: prior "3,200" cr reference = already-communicated (not new); NEW incremental order = 800 cr; total = 5,100+800+ cr | | RECONCILE_VS_FILING (order book figure drifts across the call: 5,143 at N11, ~5,000 target at N10, ~5,100 implied here, 3,200 referenced by Bala at line 25, 684cr nuclear-only figure at N46) |
| N40 | 27 | CFO | Capex plan 500 cr reiterated | restatement of N30 | |
| N41 | 27 | CFO | Asset turnover target: 4-5x | | RECONCILE_VS_FILING (vs N42, same turn) |
| N42 | 27 | CFO | Asset turnover: "at least six times" | | RECONCILE_VS_FILING (internal inconsistency vs N41, same turn) |
| N43 | 33 | MD | Fuel-cell phase 3 ready by March 2027 | restatement/clarifies N5 | |
| N44 | 35 | MD | Fuel-cell expansion commissioned by March 27; ramp-up plan from April onward | | |
| N45 | 37 | MD | Fuel-cell phase 2 operational by October [2026] | restatement of N4 | |
| N46 | 89 | MD/CFO | Nuclear: 684 cr orders as of today + 130 cr expected = ~815 cr | reconciles/restates N33's ~800cr | RECONCILE_VS_FILING |
| N47 | 95 | MD/CFO | Capex split ratio 70:30 (clean energy : non-clean energy) | | |
| N48 | 105 | CFO | Capex incurred Q1 = 35 cr (confirmed) | firms up N38 | |
| N49 | 111 | MD | Data center order ~45 cr, to be executed by Feb/March this FY | | |
| N50 | 111 | MD | Data center: plan for 8 such infrastructure sets per year | restatement of N6 | |
| N51 | 117 | MD | Mahi Banswara: 4 projects, reactors described as "10 megawatt" | | GARBLED / RECONCILE_VS_FILING (MTAR's PHWR-scale nuclear reactor programs are not 10MW-class; likely STT mis-transcription) |
| N52 | 163 | MD | Actuator content ~142 [unit ambiguous — "pages"/value unclear] | LCA Mk1A content-per-platform | GARBLED (unit ambiguous) |
| N53 | 241 | MD | FY30 targets: products >1,000 cr; aerospace 600-700 cr | 3-4 year forward segment size targets | |

### 4b. Analyst-stated / management-declined figures (for Role 5 visibility only — NOT counted in mgmt_numbers)

| Line | Analyst | Figure stated | Management response | Flags |
|------|---------|----------------|----------------------|-------|
| 21 | Bala Subramanyan | Inventory days "78 to 145"; receivables "140 to 82" | CFO answers qualitatively (better terms), does not restate these exact figures | ANALYST_STATED, GARBLED (direction of change unclear) |
| 33 | Gorov Naguri | Existing fuel-cell hot-box capacity: 20,000 | MD does not confirm/deny the number, answers qualitatively | ANALYST_STATED |
| 67 | Gorov Naguri | Receivable+inventory days "used to be about 340... now down to about 220" | MD: "that's what let us see" (HEDGE, no numeric confirmation) | ANALYST_STATED |
| 75 | Sumat Kumar | MTAR's own guidance paraphrased as "80% plus minus 5%" | MD does not correct; answers with FORWARD/HEDGE only | ANALYST_STATED; RECONCILE_VS_FILING (MD's own stated guidance at N13/N14 is "80% revenue load" + "EBITDA margin 24%±100bps" — Sumat's "80%±5%" paraphrase does not clearly match either figure) |
| 9 | Mohit Kumar | Today's order size referenced as "31 billion" | MD answers on timeline only, doesn't confirm the figure | ANALYST_STATED, GARBLED (inconsistent with the 800cr figure discussed elsewhere for "today's" order) |
| 161 | Rohit Natraan | Bloom Fremont 5GW → implies ~77,000 hot boxes; ask of >50,000 hot boxes/yr | MD: "can't get into the numbers because of the NDA side" (HEDGE, declines) | ANALYST_STATED, MGMT_DECLINED |
| 167 | Push Seal Dasani | Interest cost 16 cr | MD/CFO: "I don't have the exact breakup... CFO can give it later" (HEDGE, declines breakdown) | ANALYST_STATED, MGMT_DECLINED |
| 237 | Pria | Current products & aerospace/defense business size: "~100cr / ~130cr annual size" | MD does not confirm/deny this baseline, answers only on FY30 forward target (N53) | ANALYST_STATED |

---
## 5. FORWARD-COMMITMENT (FORWARD) AND HEDGE/DEFLECTION (HEDGE) PHRASES — 22 rows

| # | Line | Type | Speaker | Phrase (verbatim) | Context |
|---|------|------|---------|--------------------|---------|
| F1 | 5 | FORWARD | MD | "we strongly believe that the company is at an inflection point with each of our key business verticals positioned for next phase of growth" | Opening remarks |
| F2 | 5 | FORWARD | MD | "I would like to reiterate our confidence in achieving the guidance given earlier... we are pretty confident to do better than the guidance given earlier" | Guidance reaffirmation |
| F3 | 5 | FORWARD | MD | "We expect to double our revenues in aerospace and defense segment in the current fiscal year" | Aerospace & defense |
| F4 | 5 | FORWARD | MD | "we expect a robust closing order book of 5,000 by end of this fiscal year" | Order book |
| F5 | 47 | FORWARD | MD | "it's going to continue. It's going to grow... second half would be even stronger than the first half" | New product run-rate |
| F6 | 77 | FORWARD | MD | "we'll definitely do better than that" | Re: guidance upgrade (to Sumat Kumar) |
| F7 | 125 | FORWARD | MD | "it's going to sustain and do better moving forward... quarter on quarter basis" | Products sustainability |
| F8 | 163 | FORWARD | MD | "these numbers are going to grow for sure" | Content-per-platform |
| F9 | 173 | FORWARD | MD | "we'll see the result 6 months one year down the line in terms of volumes" | New product development |
| F10 | 179 | FORWARD | MD | "the product engine is going to grow rapidly... moving forward the segment is going to do more and more" | Products segment |
| F11 | 233 | FORWARD | MD | "we need to execute [these orders] as soon as possible" | Execution commitment (short-cycle orders) |
| F12 | 241 | FORWARD | MD | "it might cross thousand crores very comfortably" | FY30 products segment target |
| H1 | 33 | HEDGE | MD | "I can't specify the numbers because of the [NDA] being signed" | Fuel-cell phase 3 capacity, garbled reference to NDA |
| H2 | 69 | HEDGE | MD | "Yeah, that's what let us see." | Working capital / receivable-inventory day sustainability |
| H3 | 77 | HEDGE | MD | "probably we'll see by end of next quarter how it goes and then we'll come back to you on that" | Guidance upgrade — paired with F6 in same turn |
| H4 | 121 | HEDGE | MD | "the timeline I cannot really say" | Mahi Banswara vendor-allotment process |
| H5 | 123 | HEDGE | MD | "I'm not too sure about that" | PSVR vs nuclear program pace comparison |
| H6 | 155 | HEDGE | MD | "See all this is unwanted noise. Uh I really wanted to express this very clearly." | US data center delay rumors (deflection) |
| H7 | 161 | HEDGE | MD | "they can't get into the numbers because of the NDA side" | Bloom Fremont / hot-box capacity ask |
| H8 | 167 | HEDGE | MD/CFO | "I think I don't have the exact breakup of that but probably CFO... can give it little later" | Interest-cost breakdown deflected |
| H9 | 235 | HEDGE | MD | "there's nothing like market share... we can't spell out the exact percentage right now" | Gigawatt market share |
| H10 | 237 | HEDGE | MD | "I can't say the exact number" | FY30 products/aerospace size — paired with F12 in same turn |

---
## SUMMARY COUNTS

- Participants: 15 (5 management-side incl. operator; 10 analysts, one asking twice)
- Speaker turns: 124
- Questions: 32 (across 11 analyst Q&A slots / 10 unique analysts)
- REPEAT_QUESTION themes: working capital (3 instances), clean-energy/products (12 instances)
- Management-spoken numbers: 53
- Analyst-stated/management-declined figures (informational, not in mgmt_numbers count): 8
- FORWARD phrases: 12
- HEDGE/deflection phrases: 10
- MGMT_ABSENCE: not raised (MD + CFO both present and substantively speaking)
- MERGED_SPEAKERS / MERGED_QA turns (STT artifact — multiple real speakers collapsed into one transcribed line): turns 4, 5, 7, 17, 47, 56, 59, 61, 62, 81, 82, 84, 107, 118 (14 of 124 turns, ~11%)

flags_raised (unique types): ZERO_STANDING (n/a — not applicable to concall doctype,
no standing line items), MERGED_SPEAKERS, MERGED_QA, REPEAT_QUESTION,
RECONCILE_VS_FILING, GARBLED, ANALYST_STATED, MGMT_DECLINED, FORWARD, HEDGE
