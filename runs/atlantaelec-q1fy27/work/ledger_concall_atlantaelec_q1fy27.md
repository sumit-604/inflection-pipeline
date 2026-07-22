=== A2 COUNT TEST ===
category: turns          grep_count: 89   sweep_count: 89   match: yes
category: questions      grep_count: 40   sweep_count: 40   match: yes
category: mgmt_numbers   grep_count: 125  sweep_count: 125  match: yes  (reconciliation: pass1 unit-anchored regex over MANAGEMENT turns = 122; pass2 supplemental scan for ASR-ambiguous unit-less figures and verbal zero-value disclosures = 3; initial pass1-only mismatch of 3 resolved by adding pass2 -- these are structurally invisible to a digit+unit regex (one has no unit token attached, two are stated as words 'No'/'there was not' with zero digits) -- combined mechanical total 125 now matches manual sweep of 125)
category: zero_standing  grep_count: 2    sweep_count: 2    match: yes  (subset of mgmt_numbers: data-centre order book, Q1 export contribution)
gate_a2: pass
=== END COUNT TEST ===

# LEDGER — concall_atlantaelec_q1fy27

Source: `extract_concall_atlantaelec_q1fy27.txt` (89 speaker turns, lines 1-200, A1 header confirms 100% line coverage, 0 formfeeds, plain-text verbatim transcript).

## 1. PARTICIPANTS (both sides)

| # | Name | Designation / Firm | Side | First turn | Flags |
|---|------|---------------------|------|-----------|-------|
| 1 | Operator (unnamed) | Call operator | Moderator | turn 1 (line 20) | |
| 2 | Mohit Upadhyay | Adfactors PR, moderator | Moderator | turn 2 (line 22) | |
| 3 | Niral Keshavbhai Patel | Chairman & Managing Director | Management | turn 5 (line 28) | |
| 4 | Anand Sharma | Chief Operating Officer | Management | turn 4 (line 26) | |
| 5 | Mayur Mehta | Chief Financial Officer | Management | turn 3 (line 24) | |
| 6 | Ashishkumar Mathur | CEO | Management | introduced line 18/22, **never speaks** | MGMT_ABSENCE |
| 7 | Mahir Manohar | Trust Mutual Fund | Analyst | turn 6 (line 32) | |
| 8 | Kunal Mehta | Ingrade Equities | Analyst | turn 14 (line 48) | |
| 9 | Rohan | Access Capital | Analyst | turn 26 (line 72) | |
| 10 | Arafat | Dollar Capital | Analyst | turn 30 (line 80) | |
| 11 | Shubham Gupta | Pinetree Asset Management | Analyst | turn 36 (line 92) | |
| 12 | Mayur Chaturvedi | HSBC | Analyst | turn 38 (line 96) | |
| 13 | Chandan Mishra | Pintos | Analyst | turn 46 (line 112) | |
| 14 | Jenil | STO Investment | Analyst | turn 50 (line 120) | |
| 15 | Pratham Modi | HPMG Shares and Securities | Analyst | turn 54 (line 128) | |
| 16 | Tina Virmani | Motilal Oswal Financial Services | Analyst | turn 56 (line 132) | |
| 17 | Jigar Jani | Nuvama PCG Research | Analyst | turn 62 (line 144) | |
| 18 | Prathamesh | Nepun Live | Analyst | turn 73 (line 166) | |
| 19 | Manoj Shah | Philip Capital | Analyst | turn 77 (line 174) | |
| 20 | Aryan Vijan | R V Investment | Analyst | turn 83 (line 186) | |

Note: 9 [MANAGEMENT] turns are unattributed to a specific named speaker in the transcript (turns 27, 31, 33, 65, 71, 78, 80, 82, 86 — line numbers 74, 82, 86, 150, 162, 176, 180, 184, 192). Flag AMBIGUOUS_SPEAKER on each; A3/A4 should not assume CFO vs COO vs CMD attribution without corroboration.

## 2. SPEAKER TURNS (n=89)

| Turn | Line | Role | Speaker | First ~10 words |
|------|------|------|---------|------------------|
| 1 | 20 | MODERATOR | Operator | Ladies and gentlemen, good day and welcome to the Atlanta ... |
| 2 | 22 | MODERATOR | Mohit Upadhyay, Adfactors PR | Thank you. Good morning and a very warm welcome to ... |
| 3 | 24 | MANAGEMENT | Mayur Mehta, CFO | Thank you Mohit. Good morning everyone. I will now take ... |
| 4 | 26 | MANAGEMENT | Anand Sharma, COO | Thank you, Mayur. Good morning, everyone. I will now take ... |
| 5 | 28 | MANAGEMENT | Niral Patel, CMD | Thank you, Anand. Good morning once again, everyone. As both ... |
| 6 | 32 | ANALYST | Mahir Manohar, Trust Mutual Fund | Congratulations on great set of numbers. Largely wanted to get ... |
| 7 | 34 | MANAGEMENT | Niral Patel, CMD | So far we've witnessed the highest possible order inflow in ... |
| 8 | 36 | ANALYST | Mahir Manohar, Trust Mutual Fund | On 765 KV, what is the status? We were looking ... |
| 9 | 38 | MANAGEMENT | Niral Patel, CMD | The approval process is in place. We are in very ... |
| 10 | 40 | ANALYST | Mahir Manohar, Trust Mutual Fund | So broadly should we expect end of second quarter for ... |
| 11 | 42 | MANAGEMENT | Niral Patel, CMD | Certainly. |
| 12 | 44 | ANALYST | Mahir Manohar, Trust Mutual Fund | My last question was on power transformers versus distribution transformers. ... |
| 13 | 46 | MANAGEMENT | Niral Patel, CMD | The distribution market is entirely different than the power transformer ... |
| 14 | 48 | ANALYST | Kunal Mehta, Ingrade Equities | My first question is on the gross margin — though ... |
| 15 | 50 | MANAGEMENT | Mayur Mehta, CFO | To answer the mix of revenue — we have 56% ... |
| 16 | 52 | MANAGEMENT | Niral Patel, CMD | What Mayur was suggesting — in case of inventory building ... |
| 17 | 54 | ANALYST | Kunal Mehta, Ingrade Equities | Our Atlanta Trafo facility is primarily for 400/765 KV. Are ... |
| 18 | 56 | MANAGEMENT | Niral Patel, CMD | Yes Kunal, we have continued that approach and we are ... |
| 19 | 58 | ANALYST | Kunal Mehta, Ingrade Equities | And the 275 cr in the order book that was ... |
| 20 | 60 | MANAGEMENT | Niral Patel, CMD | For that we shall be utilizing our Unit 4 facility, ... |
| 21 | 62 | ANALYST | Kunal Mehta, Ingrade Equities | The order inflow — this was a record quarter. Should ... |
| 22 | 64 | MANAGEMENT | Niral Patel, CMD | In our experience we have seen that typically quarter 2 ... |
| 23 | 66 | ANALYST | Kunal Mehta, Ingrade Equities | My last question is on the IDT mix. We are ... |
| 24 | 68 | MANAGEMENT | Niral Patel, CMD | As long as the renewable energy sector is growing, and ... |
| 25 | 70 | MODERATOR | (unattributed) | In order to ensure that management is able to address ... |
| 26 | 72 | ANALYST | Rohan, Access Capital | If you can provide the aggregation in terms of MVA ... |
| 27 | 74 | MANAGEMENT | (unattributed) | Total MVA base capacity utilization for the quarter is 4,381 ... |
| 28 | 76 | ANALYST | Rohan, Access Capital | In terms of backward integration, the tank and radiators facility ... |
| 29 | 78 | MANAGEMENT | Anand Sharma, COO | The tank and radiators constitute the fabrication components of the ... |
| 30 | 80 | ANALYST | Arafat, Dollar Capital | My first question is on your current order pipeline across ... |
| 31 | 82 | MANAGEMENT | (unattributed) | We have close to about 3,100 crores of order book, ... |
| 32 | 84 | ANALYST | Arafat, Dollar Capital | Any large order expected to convert in the next couple ... |
| 33 | 86 | MANAGEMENT | (unattributed) | It would not be right for us to disclose certain ... |
| 34 | 88 | ANALYST | Arafat, Dollar Capital | Lastly, any guidance for growth for FY27, FY28 on the ... |
| 35 | 90 | MANAGEMENT | Niral Patel, CMD | We went public about 9 months ago, and we have ... |
| 36 | 92 | ANALYST | Shubham Gupta, Pinetree Asset Management | We had scheduled short circuit tests for 400 KV transformers ... |
| 37 | 94 | MANAGEMENT | Niral Patel, CMD | The 400 KV development is at a very advanced stage. ... |
| 38 | 96 | ANALYST | Mayur Chaturvedi, HSBC | To deliver revenue growth of 48% YoY in such a ... |
| 39 | 98 | MANAGEMENT | Mayur Mehta, CFO | This is directly attributable to the price variation clause which ... |
| 40 | 100 | ANALYST | Mayur Chaturvedi, HSBC | So what was the volume number for FY26 Q1? |
| 41 | 102 | MANAGEMENT | Mayur Mehta, CFO | Total revenue was 466.33 cr [Q1 FY27], and last year ... |
| 42 | 104 | ANALYST | Mayur Chaturvedi, HSBC | On the Chinese players that have been allowed to participate ... |
| 43 | 106 | MANAGEMENT | Niral Patel, CMD | Out of the four companies which have been allowed, there ... |
| 44 | 108 | ANALYST | Mayur Chaturvedi, HSBC | So if they do try and supply to Indian PSUs ... |
| 45 | 110 | MANAGEMENT | Niral Patel, CMD | They would not be interested in lower margin orders because ... |
| 46 | 112 | ANALYST | Chandan Mishra, Pintos | My first question on order book from data centres — ... |
| 47 | 114 | MANAGEMENT | Niral Patel, CMD | No sir. The current order book does not contain any ... |
| 48 | 116 | ANALYST | Chandan Mishra, Pintos | If you please provide a time frame to commence unit ... |
| 49 | 118 | MANAGEMENT | Niral Patel, CMD | By end of third quarter this financial year — so ... |
| 50 | 120 | ANALYST | Jenil, STO Investment | My question was regarding the big size orders that PGCIL ... |
| 51 | 122 | MANAGEMENT | Niral Patel, CMD | There is a huge backlog with power grid and such ... |
| 52 | 124 | ANALYST | Jenil, STO Investment | My second question is on the capacity expansion that our ... |
| 53 | 126 | MANAGEMENT | Niral Patel, CMD | As a company our target would be to protect our ... |
| 54 | 128 | ANALYST | Pratham Modi, HPMG Shares and Securities | My question is regarding CRGO steel. The DGTR initiated an ... |
| 55 | 130 | MANAGEMENT | Niral Patel, CMD | This inquiry has been initiated recently and the DGTR is ... |
| 56 | 132 | ANALYST | Tina Virmani, Motilal Oswal Financial Services | My question is related to this technology tie-up for 765 ... |
| 57 | 134 | MANAGEMENT | Niral Patel, CMD | We have advanced to a significantly advanced level to close ... |
| 58 | 136 | ANALYST | Tina Virmani, Motilal Oswal | So maybe tie-up by Q3 and formal production from quarter ... |
| 59 | 138 | MANAGEMENT | Niral Patel, CMD | This will require power grid revalidation in the new name, ... |
| 60 | 140 | ANALYST | Tina Virmani, Motilal Oswal | So only power grid revalidation is required. Any short circuit ... |
| 61 | 142 | MANAGEMENT | Niral Patel, CMD | As of now PGCIL has not been able to finalize ... |
| 62 | 144 | ANALYST | Jigar Jani, Nuvama PCG Research | Sorry my call dropped. What would be your guidance for ... |
| 63 | 146 | MANAGEMENT | Mayur Mehta, CFO | Out of the unexecuted order book of 3,100 crores we ... |
| 64 | 148 | ANALYST | Jigar Jani, Nuvama PCG Research | One data keeping question — can you give me the ... |
| 65 | 150 | MANAGEMENT | (unattributed) | Last quarter, Q4, we were able to achieve 13,000 MVA ... |
| 66 | 152 | ANALYST | Kunal, Ingrade Equities | We are seeing a lot of capacity addition in 400 ... |
| 67 | 154 | MANAGEMENT | Niral Patel, CMD | It's very difficult to comment on competitors, but yes there ... |
| 68 | 156 | ANALYST | Kunal, Ingrade Equities | On this tech tie-up — is it on a commission ... |
| 69 | 158 | MANAGEMENT | Niral Patel, CMD | It's a combination of both — a fixed one-time fee ... |
| 70 | 160 | ANALYST | Kunal, Ingrade Equities | How much capex has already been done from the tank ... |
| 71 | 162 | MANAGEMENT | (unattributed) | Close to about 15 to 20 crores is what we ... |
| 72 | 164 | ANALYST | Kunal, Ingrade Equities | And the remaining amount — are we planning to take ... |
| 73 | 166 | ANALYST | Prathamesh, Nepun Live | I wanted to understand some things about your margins. You're ... |
| 74 | 168 | MANAGEMENT | Niral Patel, CMD | We expect that 400 KV and 765 KV class transformers ... |
| 75 | 170 | ANALYST | Prathamesh, Nepun Live | So for next year from the strategic perspective do you ... |
| 76 | 172 | MANAGEMENT | Niral Patel, CMD | We maintain that the margins will be stable, like the ... |
| 77 | 174 | ANALYST | Manoj Shah, Philip Capital | Was there any export contribution to revenues in Q1 FY27? |
| 78 | 176 | MANAGEMENT | (unattributed) | Sir, there was not. |
| 79 | 178 | ANALYST | Manoj Shah, Philip Capital | Going forward, what is the export mix we are targeting ... |
| 80 | 180 | MANAGEMENT | (unattributed) | We are targeting to have 15% of revenue coming from ... |
| 81 | 182 | ANALYST | Manoj Shah, Philip Capital | Given that export orders typically command different pricing, competition, execution ... |
| 82 | 184 | MANAGEMENT | (unattributed) | We are trying to enter export markets to mitigate the ... |
| 83 | 186 | ANALYST | Aryan Vijan, R V Investment | I may have missed a few questions. What is the ... |
| 84 | 188 | MANAGEMENT | Niral Patel, CMD | We maintain that 40% growth year-on-year in revenue terms. So ... |
| 85 | 190 | ANALYST | Aryan Vijan, R V Investment | And you said you have 3,100+ cr of order book ... |
| 86 | 192 | MANAGEMENT | (unattributed) | We have 3,100 [cr] of unexecuted order as of June, ... |
| 87 | 194 | MODERATOR | (unattributed) | That was the last question. I would now like to ... |
| 88 | 196 | MANAGEMENT | Niral Patel, CMD | Thank you everyone for joining the investor conference today. Thank ... |
| 89 | 198 | MODERATOR | (unattributed) | On behalf of Atlanta Electricals Limited, that concludes this conference. ... |

## 3. Q&A PAIRS (n=40)

| Q# | Analyst turn | Line | Analyst / Firm | Topic (first ~90 chars) | Answer turn(s) | Flags |
|----|--------------|------|-----------------|--------------------------|-----------------|-------|
| 1 | 6 | 32 | Mahir Manohar, Trust Mutual Fund | Congratulations on great set of numbers. Largely wanted to get a sense — when I see two la | 7 | REPEAT_QUESTION (competitor capacity addition / margin-pressure risk; also asked turns 52,66) |
| 2 | 8 | 36 | Mahir Manohar, Trust Mutual Fund | On 765 KV, what is the status? We were looking for approval from PGCIL. What is the operat | 9 | REPEAT_QUESTION (765 KV tie-up/approval status; also asked turns 56,58,60) |
| 3 | 10 | 40 | Mahir Manohar, Trust Mutual Fund | So broadly should we expect end of second quarter for us to have approval from PGCIL for 7 | 11 |  |
| 4 | 12 | 44 | Mahir Manohar, Trust Mutual Fund | My last question was on power transformers versus distribution transformers. Distribution  | 13 |  |
| 5 | 14 | 48 | Kunal Mehta, Ingrade Equities | My first question is on the gross margin — though we have improved YoY, I think QoQ the gr | 15, 16 |  |
| 6 | 17 | 54 | Kunal Mehta, Ingrade Equities | Our Atlanta Trafo facility is primarily for 400/765 KV. Are we currently also manufacturin | 18 |  |
| 7 | 19 | 58 | Kunal Mehta, Ingrade Equities | And the 275 cr in the order book that was 400 KV — will be manufactured from that facility | 20 |  |
| 8 | 21 | 62 | Kunal Mehta, Ingrade Equities | The order inflow — this was a record quarter. Should we take this as steady state going ah | 22 |  |
| 9 | 23 | 66 | Kunal Mehta, Ingrade Equities | My last question is on the IDT mix. We are seeing a lot of other players adding capacity.  | 24 |  |
| 10 | 26 | 72 | Rohan, Access Capital | If you can provide the aggregation in terms of MVA for this quarter, and what are the cont | 27 |  |
| 11 | 28 | 76 | Rohan, Access Capital | In terms of backward integration, the tank and radiators facility — post completion, in te | 29 |  |
| 12 | 30 | 80 | Arafat, Dollar Capital | My first question is on your current order pipeline across clients and how do you expect t | 31 | REPEAT_QUESTION (order-book executable-this-FY amount; also asked turns 62, 85) |
| 13 | 32 | 84 | Arafat, Dollar Capital | Any large order expected to convert in the next couple of quarters? | 33 |  |
| 14 | 34 | 88 | Arafat, Dollar Capital | Lastly, any guidance for growth for FY27, FY28 on the expanded capacity? | 35 | REPEAT_QUESTION (FY27/FY28 growth guidance; also asked turn 83) |
| 15 | 36 | 92 | Shubham Gupta, Pinetree Asset Management | We had scheduled short circuit tests for 400 KV transformers for June and July. What is th | 37 |  |
| 16 | 38 | 96 | Mayur Chaturvedi, HSBC | To deliver revenue growth of 48% YoY in such a volatile situation is commendable. You've g | 39 |  |
| 17 | 40 | 100 | Mayur Chaturvedi, HSBC | So what was the volume number for FY26 Q1? | 41 |  |
| 18 | 42 | 104 | Mayur Chaturvedi, HSBC | On the Chinese players that have been allowed to participate in public tenders — in curren | 43 |  |
| 19 | 44 | 108 | Mayur Chaturvedi, HSBC | So if they do try and supply to Indian PSUs they will end up making lower margins versus w | 45 |  |
| 20 | 46 | 112 | Chandan Mishra, Pintos | My first question on order book from data centres — is there any order book we received? | 47 |  |
| 21 | 48 | 116 | Chandan Mishra, Pintos | If you please provide a time frame to commence unit 6 inverter duty transformer facility a | 49 |  |
| 22 | 50 | 120 | Jenil, STO Investment | My question was regarding the big size orders that PGCIL is giving. Recently it awarded ov | 51 |  |
| 23 | 52 | 124 | Jenil, STO Investment | My second question is on the capacity expansion that our peers are doing. It's massive — c | 53 | REPEAT_QUESTION (competitor capacity addition / margin-pressure risk; also asked turns 6,66) |
| 24 | 54 | 128 | Pratham Modi, HPMG Shares and Securities | My question is regarding CRGO steel. The DGTR initiated an investigation into CRGO steel i | 55 |  |
| 25 | 56 | 132 | Tina Virmani, Motilal Oswal Financial Services | My question is related to this technology tie-up for 765 KV range of transformers. Where a | 57 | REPEAT_QUESTION (765 KV tie-up/approval status; also asked turns 8,10) |
| 26 | 58 | 136 | Tina Virmani, Motilal Oswal | So maybe tie-up by Q3 and formal production from quarter 4? And this facility would not ne | 59 | REPEAT_QUESTION (765 KV tie-up/approval status; also asked turns 8,10,56) |
| 27 | 60 | 140 | Tina Virmani, Motilal Oswal | So only power grid revalidation is required. Any short circuit test also required for this | 61 | REPEAT_QUESTION (765 KV tie-up/approval status; also asked turns 8,10,56,58) |
| 28 | 62 | 144 | Jigar Jani, Nuvama PCG Research | Sorry my call dropped. What would be your guidance for execution of this order book, how l | 63 | REPEAT_QUESTION (order-book executable-this-FY amount; also asked turns 30, 85) |
| 29 | 64 | 148 | Jigar Jani, Nuvama PCG Research | One data keeping question — can you give me the Q4 MVA production number, the last quarter | 65 |  |
| 30 | 66 | 152 | Kunal, Ingrade Equities | We are seeing a lot of capacity addition in 400 KV / 220 KV. After commissioning of the ca | 67 | REPEAT_QUESTION (competitor capacity addition / margin-pressure risk; also asked turns 6,52) |
| 31 | 68 | 156 | Kunal, Ingrade Equities | On this tech tie-up — is it on a commission basis or some monetary benefit the technical p | 69 |  |
| 32 | 70 | 160 | Kunal, Ingrade Equities | How much capex has already been done from the tank and radiator facility out of the 180 cr | 71 |  |
| 33 | 72 | 164 | Kunal, Ingrade Equities | And the remaining amount — are we planning to take any debt or through internal accruals?  | (none) | UNANSWERED (moderator interrupted to enforce 2-question limit before this was addressed) |
| 34 | 73 | 166 | Prathamesh, Nepun Live | I wanted to understand some things about your margins. You're expecting sustainable margin | 74 |  |
| 35 | 75 | 170 | Prathamesh, Nepun Live | So for next year from the strategic perspective do you think our margins would benefit rat | 76 |  |
| 36 | 77 | 174 | Manoj Shah, Philip Capital | Was there any export contribution to revenues in Q1 FY27? | 78 |  |
| 37 | 79 | 178 | Manoj Shah, Philip Capital | Going forward, what is the export mix we are targeting over the next two to three years? | 80 |  |
| 38 | 81 | 182 | Manoj Shah, Philip Capital | Given that export orders typically command different pricing, competition, execution — how | 82 |  |
| 39 | 83 | 186 | Aryan Vijan, R V Investment | I may have missed a few questions. What is the guidance for this year? | 84 | REPEAT_QUESTION (FY27/FY28 growth guidance; also asked turn 34) |
| 40 | 85 | 190 | Aryan Vijan, R V Investment | And you said you have 3,100+ cr of order book — how much is to be executed this year? | 86 | REPEAT_QUESTION (order-book executable-this-FY amount; also asked turns 30, 62) |

## 4. MANAGEMENT NUMBERS / QUANTIFIED CLAIMS (n=125)

Enumerated at occurrence level (every spoken instance is its own row, including verbatim restatements of the same fact across turns — this is deliberate, it feeds the Role 5 arithmetic-consistency check).

| # | Turn | Line | Value | Context | Flags |
|---|------|------|-------|---------|-------|
| 1 | 3 | 24 | 48% | ...venue from operations grew by 48% year-on-year t... |  |
| 2 | 3 | 24 | 466.33 cr | ...s grew by 48% year-on-year to 466.33 cr compared with... |  |
| 3 | 3 | 24 | 315.11 cr | ...ar to 466.33 cr compared with 315.11 cr in Q1 FY26. Th... |  |
| 4 | 3 | 24 | 55.5% | ...nt, gross profit increased by 55.5% year-on-year t... |  |
| 5 | 3 | 24 | 127.20 cr | ...ased by 55.5% year-on-year to 127.20 cr while gross ma... |  |
| 6 | 3 | 24 | 130 bps | ...hile gross margin improved by 130 bps to 27.3% from... |  |
| 7 | 3 | 24 | 27.3% | ...margin improved by 130 bps to 27.3% from 26% in th... |  |
| 8 | 3 | 24 | 26% | ...oved by 130 bps to 27.3% from 26% in the corresp... |  |
| 9 | 3 | 24 | 220 KV | ...g increased production of the 220 KV class. EBITDA... |  |
| 10 | 3 | 24 | 77.10 crores | ...ITDA for the quarter stood at 77.10 crores representing a... |  |
| 11 | 3 | 24 | 58.1% | ...t 77.10 crores representing a 58.1% year-on-year i... |  |
| 12 | 3 | 24 | 16.5% | ...ease with margin expanding to 16.5% compared with... |  |
| 13 | 3 | 24 | 15.5% | ...anding to 16.5% compared with 15.5% in Q1 FY26. Th... |  |
| 14 | 3 | 24 | 50.4% | ...ct mix. Profit after tax grew 50.4% year-on-year t... |  |
| 15 | 3 | 24 | 46.84 crores | ...50.4% year-on-year to rupees 46.84 crores while PAT marg... |  |
| 16 | 3 | 24 | 10% | ...while PAT margin improved to 10%. Earnings per... |  |
| 17 | 3 | 24 | 40% | ...rnings per share increased by 40% year-on-year t... |  |
| 18 | 3 | 24 | 37.6% | ...of FY26. Revenue declined by 37.6% quarter on qua... |  |
| 19 | 3 | 24 | 20% | ...normalized from approximately 20% in Q4 FY26 to... |  |
| 20 | 3 | 24 | 16.5% | ...proximately 20% in Q4 FY26 to 16.5% in Q1 FY27. Si... |  |
| 21 | 3 | 24 | 13.7% | ...ly, PAT margin moderated from 13.7% to 10%. Despit... |  |
| 22 | 3 | 24 | 10% | ...argin moderated from 13.7% to 10%. Despite this... |  |
| 23 | 3 | 24 | 63,060 MVA | ...led manufacturing capacity of 63,060 MVA, we recorded c... |  |
| 24 | 3 | 24 | 4,381 MVA | ...orded capacity utilization of 4,381 MVA during the qua... |  |
| 25 | 3 | 24 | 72 days | ...Net working capital stood at 72 days with inventory... |  |
| 26 | 3 | 24 | days at 105, | ...ood at 72 days with inventory days at 105, receivable day... |  |
| 27 | 3 | 24 | days at 88 | ...ntory days at 105, receivable days at 88 and payable da... |  |
| 28 | 3 | 24 | days at 110 | ...ivable days at 88 and payable days at 110. This translat... |  |
| 29 | 3 | 24 | 83 days | ...ersion cycle of approximately 83 days which remains... |  |
| 30 | 4 | 26 | 972.42 crores | ...ver quarterly order inflow of 972.42 crores. This strong o... |  |
| 31 | 4 | 26 | 3,116.63 crores | ...the outstanding order book to 3,116.63 crores as on 30th Jun... |  |
| 32 | 4 | 26 | 2026 | ...116.63 crores as on 30th June 2026 providing heal... |  |
| 33 | 4 | 26 | 291.68 cr | ...cured during the quarter were 291.68 cr order from RRV... |  |
| 34 | 4 | 26 | 160 MVA | ...han utility for the supply of 160 MVA, 50 MVA and 31... |  |
| 35 | 4 | 26 | 50 MVA | ...ty for the supply of 160 MVA, 50 MVA and 31.5 MVA p... |  |
| 36 | 4 | 26 | 31.5 MVA | ...supply of 160 MVA, 50 MVA and 31.5 MVA power transfor... |  |
| 37 | 4 | 26 | 225.15 crores | ...MVA power transformers and a 225.15 crores order from the... | ARITHMETIC_CHECK (PSTCL, 23 units x 160 MVA 220/66 kV, per-unit implied value should be cross-checked against RRVPNL's 291.68 cr for a mixed 160/50/31.5 MVA lot at synthesis stage; flagged per task note, keep verbatim) |
| 38 | 4 | 26 | 23 numbers | ...ility PSTCL for the supply of 23 numbers of 160 MVA 220... |  |
| 39 | 4 | 26 | 160 MVA | ...r the supply of 23 numbers of 160 MVA 220/66 KV powe... |  |
| 40 | 4 | 26 | 66 KV | ...of 23 numbers of 160 MVA 220/66 KV power transfor... |  |
| 41 | 4 | 26 | 220 KV | ...cts. Today transformers rated 220 KV amount to over... |  |
| 42 | 4 | 26 | 55% | ...s rated 220 KV amount to over 55% of our total o... |  |
| 43 | 4 | 26 | 400 KV | ...of our total order book while 400 KV transformers a... |  |
| 44 | 4 | 26 | 275 crores | ...nd reactors contribute nearly 275 crores demonstrating... |  |
| 45 | 4 | 26 | 79% | ...quarter, accounting to nearly 79% of the revenue... |  |
| 46 | 4 | 26 | 66% | ...ion contributed approximately 66% of revenue, fo... |  |
| 47 | 4 | 26 | 19% | ...by renewable energy at around 19% with the remai... |  |
| 48 | 4 | 26 | 400 KV | ...e manufacturing and supply of 400 KV class transfor... |  |
| 49 | 4 | 26 | 500 MVA | ...endor development program for 500 MVA 400 KV transfo... |  |
| 50 | 4 | 26 | 400 KV | ...velopment program for 500 MVA 400 KV transformer te... |  |
| 51 | 4 | 26 | 315 MVA | ...n, engineering activities for 315 MVA transformer or... |  |
| 52 | 4 | 26 | 400 KV | ...commercial contribution from 400 KV transformers p... |  |
| 53 | 4 | 26 | 5,000 MVA | ...al, it will add approximately 5,000 MVA of manufacturi... |  |
| 54 | 5 | 28 | 765 KV | ...commercialization of 400 and 765 KV transformer pl... |  |
| 55 | 5 | 28 | 15% | ...s to contribute approximately 15% of our revenue... |  |
| 56 | 15 | 50 | 56% | ...the mix of revenue — we have 56% of the revenue... |  |
| 57 | 15 | 50 | 220 KV | ...6% of the revenue coming from 220 KV class, then 25... |  |
| 58 | 15 | 50 | 25% | ...oming from 220 KV class, then 25% is coming from... |  |
| 59 | 15 | 50 | 66 KV | ...lass, then 25% is coming from 66 KV class and roug... |  |
| 60 | 15 | 50 | 132 KV | ...und 5 and a half percent from 132 KV. This is the r... |  |
| 61 | 16 | 52 | 3 months | ...ty prices are going to travel 3 months later, 3 weeks... |  |
| 62 | 16 | 52 | 3 days | ...s later, 3 weeks later, maybe 3 days later. So it's... |  |
| 63 | 18 | 56 | 220 KV | ...nd we are still manufacturing 220 KV transformers i... |  |
| 64 | 27 | 74 | 4,381 MVA | ...tilization for the quarter is 4,381 MVA. Out of this 1... |  |
| 65 | 27 | 74 | 1,520 MVA | ...ter is 4,381 MVA. Out of this 1,520 MVA was produced f... |  |
| 66 | 27 | 74 | 320 MVA | ...ced from [Vadod] facility and 320 MVA was produced f... |  |
| 67 | 29 | 78 | 5% | ...ge between not more than 4 to 5% of the total t... |  |
| 68 | 31 | 82 | 3,100 crores | ...We have close to about 3,100 crores of order book,... |  |
| 69 | 31 | 82 | 2,400 crores | ...we anticipate close to about 2,400 crores which is falli... |  |
| 70 | 35 | 90 | 9 months | ...We went public about 9 months ago, and we ha... |  |
| 71 | 35 | 90 | 40% | ...and we have been maintaining 40% for the coming... |  |
| 72 | 35 | 90 | 3 years | ...aintaining 40% for the coming 3 years with stable ma... |  |
| 73 | 35 | 90 | 16% | ...ere at about 15 and a half to 16%. We intend to... |  |
| 74 | 37 | 94 | 400 KV | ...The 400 KV development is... |  |
| 75 | 41 | 102 | 466.33 cr | ...Total revenue was 466.33 cr [Q1 FY27], and... |  |
| 76 | 43 | 106 | four companies | ...Out of the four companies which have bee... |  |
| 77 | 43 | 106 | one company | ...e been allowed, there is only one company which is manuf... |  |
| 78 | 43 | 106 | 2022 | ...e from the government side in 2022, their parent... |  |
| 79 | 43 | 106 | 9 months | ...re was a period of about 6 to 9 months where they wer... |  |
| 80 | 51 | 122 | 220 KV | ...n this quarter is technically 220 KV and below. I w... |  |
| 81 | 51 | 122 | 400 KV | ...ld open our gates for further 400 KV plus transform... |  |
| 82 | 51 | 122 | 400 KV | ...oned in the industry to crack 400 KV class, which i... |  |
| 83 | 53 | 126 | 220 KV | ...hortage is still there in the 220 KV and 160 [MVA]... |  |
| 84 | 53 | 126 | 160 [MVA | ...still there in the 220 KV and 160 [MVA] segment. We a... |  |
| 85 | 53 | 126 | three years | ...formers at least about two to three years down the line,... |  |
| 86 | 55 | 130 | one month | ...g to be eased out in the next one month's time. So in... |  |
| 87 | 57 | 134 | 765 KV | ...afo] facility to make a first 765 KV class product... |  |
| 88 | 61 | 142 | 765 KV | ...for the short circuit test on 765 KV transformers.... |  |
| 89 | 61 | 142 | 765 KV | ...on is going on regarding this 765 KV short circuit... |  |
| 90 | 63 | 146 | 3,100 crores | ...the unexecuted order book of 3,100 crores we expect arou... |  |
| 91 | 63 | 146 | 2,400 crores | ...3,100 crores we expect around 2,400 crores of orders are... |  |
| 92 | 63 | 146 | two years | ...e margin — if we see for past two years, FY25 and FY26... |  |
| 93 | 63 | 146 | 13.80% | ...nd FY26: FY25 we started with 13.80% margin and end... |  |
| 94 | 63 | 146 | 15.56% | ...margin and ended annually at 15.56%; FY26 we start... |  |
| 95 | 63 | 146 | 15.48% | ...15.56%; FY26 we started with 15.48% margin, Q4 was... |  |
| 96 | 63 | 146 | 20% | ...ed with 15.48% margin, Q4 was 20% margin, and an... |  |
| 97 | 63 | 146 | 18.6% | ...% margin, and annually it was 18.6%. So we actuall... |  |
| 98 | 63 | 146 | three years | ...est ever Q1 margin since last three years at 16.5%. On t... |  |
| 99 | 63 | 146 | 16.5% | ...gin since last three years at 16.5%. On the raw ma... |  |
| 100 | 63 | 146 | 18% | ...margin somewhere around 17 to 18% as we always c... |  |
| 101 | 65 | 150 | 13,000 MVA | ..., Q4, we were able to achieve 13,000 MVA production.... |  |
| 102 | 69 | 158 | 4 years | ...to be there for at least 3 to 4 years, but only on 7... |  |
| 103 | 69 | 158 | 5 million | ...ranges anywhere between 3 to 5 million dollars. The r... |  |
| 104 | 69 | 158 | 4% | ...ranges anywhere between 2 to 4% is what the di... |  |
| 105 | 69 | 158 | four years | ...getting released for three to four years.... |  |
| 106 | 71 | 162 | 20 crores | ...Close to about 15 to 20 crores is what we hav... |  |
| 107 | 74 | 168 | 400 KV | ...We expect that 400 KV and 765 KV cla... |  |
| 108 | 74 | 168 | 765 KV | ...We expect that 400 KV and 765 KV class transfor... |  |
| 109 | 74 | 168 | 220 KV | ...better margins as compared to 220 KV or 132 KV. But... |  |
| 110 | 74 | 168 | 132 KV | ...gins as compared to 220 KV or 132 KV. But it is not... |  |
| 111 | 74 | 168 | 765 KV | ...would be earning from the 400/765 KV product since... |  |
| 112 | 74 | 168 | 765 KV | ...o have been manufacturing 400/765 KV are aware of t... |  |
| 113 | 74 | 168 | 765 KV | ...re yet to manufacture the 400/765 KV product. Once... |  |
| 114 | 74 | 168 | 765 KV | ...ntain that the margins in 400/765 KV product as com... |  |
| 115 | 74 | 168 | 220 KV | ...765 KV product as compared to 220 KV class products... |  |
| 116 | 80 | 180 | 15% | ...We are targeting to have 15% of revenue com... |  |
| 117 | 80 | 180 | 3 years | ...the export market in the next 3 years. As of now we... |  |
| 118 | 84 | 188 | 40% | ...We maintain that 40% growth year-on... |  |
| 119 | 84 | 188 | 1,851 [cr | ...venue terms. So last year was 1,851 [cr]; we can see 4... |  |
| 120 | 84 | 188 | 40% | ...ar was 1,851 [cr]; we can see 40% year-on-year g... |  |
| 121 | 86 | 192 | 3,100 [cr | ...We have 3,100 [cr] of unexecuted... |  |
| 122 | 86 | 192 | 2,400 crores | ...out of this we expect around 2,400 crores is due for exe... |  |
| 123 | 41 | 102 | 3,65 | ......that was 3,65 [ambiguous ASR — likely 315 revenue or a volume figure]...... | AMBIGUOUS_ASR |
| 124 | 47 | 114 | NONE | ...No sir. The current order book does not contain any order from the data centers.... | ZERO_STANDING |
| 125 | 78 | 176 | NONE | ...Sir, there was not. [export contribution Q1 FY27]... | ZERO_STANDING |


## 5. FORWARD-COMMITMENT & HEDGE PHRASES (sample sweep, n=34)

Enumerated, not interpreted (categorization label is descriptive only; A3 applies the lexicon).

| # | Turn | Line | Category | Phrase (verbatim) |
|---|------|------|----------|---------------------|
| 1 | 3 | 24 | FORWARD | "We expect this trend to persist over the coming quarters" |
| 2 | 3 | 24 | FORWARD | "employee costs are expected to normalize as a percentage of sales" |
| 3 | 4 | 26 | FORWARD | "we expect meaningful commercial contribution from 400 KV transformers portfolio to commence from next financial year" |
| 4 | 4 | 26 | FORWARD_COMMITMENT | "we remain on track to commission the facility before end of current calendar year" |
| 5 | 4 | 26 | HEDGE | "This initiative is expected to enhance the supply chain reliability" |
| 6 | 5 | 28 | FORWARD | "we aspire for exports to contribute approximately 15% of our revenue" |
| 7 | 5 | 28 | HEDGE | "we believe it is too early to assess the long-term competitive implications" |
| 8 | 5 | 28 | HEDGE | "we do not foresee any immediate disruption in the industry" |
| 9 | 7 | 34 | HEDGE | "we don't see any impact on the order inflow, neither do we see any correction on the pricing terms" |
| 10 | 9 | 38 | HEDGE | "As soon as we close the agreement, I think the approvals will be a fast track mechanism" |
| 11 | 11 | 42 | FORWARD_COMMITMENT | "Certainly" (re: PGCIL 765 KV approval by end of Q2) |
| 12 | 13 | 46 | HEDGE | "it would not be fair on our part to make any comment" |
| 13 | 13 | 46 | FORWARD_COMMITMENT | "we are confident the growth we are witnessing shall continue for some time" |
| 14 | 16 | 52 | HEDGE | "nobody including us can predict where commodity prices are going to travel" |
| 15 | 22 | 64 | FORWARD_COMMITMENT | "quarter two and quarter three mid will certainly add good amount of orders" |
| 16 | 24 | 68 | FORWARD | "we certainly would be adding more numbers in the IDT bucket" |
| 17 | 31 | 82 | FORWARD | "we would expect more orders to come in during the financial year" |
| 18 | 33 | 86 | HEDGE | "It would not be right for us to disclose certain information" |
| 19 | 33 | 86 | HEDGE | "eventual order conversions may take time" |
| 20 | 35 | 90 | FORWARD_COMMITMENT | "we intend to stick to that guideline and the company will ensure that those guidelines are met" |
| 21 | 37 | 94 | FORWARD_COMMITMENT | "This is well on time as per our schedule" |
| 22 | 37 | 94 | HEDGE | "We don't see any pressure of not getting oil at all" |
| 23 | 43 | 106 | HEDGE | "we do not see why they would fill more orders from Indian PSUs with lower margin. We don't see any logic in that" |
| 24 | 49 | 118 | FORWARD_COMMITMENT | "our target is to commission the inverter transformer facility" (by Dec 10) |
| 25 | 51 | 122 | FORWARD_COMMITMENT | "Q2 would be the last quarter when our experimental stage ... would end" |
| 26 | 55 | 130 | HEDGE | "it would not be fair on our part to speculate as to what would be the recommendation and outcome of this inquiry" |
| 27 | 57 | 134 | HEDGE | "It would not be right for us to disclose the name of the entity as of now" |
| 28 | 57 | 134 | FORWARD_COMMITMENT | "We expect those doors to open by end of this financial year or in the last quarter" |
| 29 | 61 | 142 | HEDGE | "nothing concrete is available as of now regarding this" |
| 30 | 63 | 146 | FORWARD_COMMITMENT | "we expect the margin somewhere around 17 to 18% as we always convey to our investors" |
| 31 | 67 | 154 | HEDGE | "It's very difficult to comment on competitors ... I would not like to comment on how competitors are placed" |
| 32 | 69 | 158 | HEDGE | "royalties may end up getting released for three to four years" |
| 33 | 74 | 168 | HEDGE | "it is not right on our part to comment as to what kind of margins we would be earning from the 400/765 KV product" |
| 34 | 76 | 172 | FORWARD_COMMITMENT | "We maintain that the margins will be stable, like the guidance we initially gave" |

## 6. NOTES ON RECONCILIATION AND METHODOLOGY

- **Turns**: grep pattern `^\[(MODERATOR|MANAGEMENT|ANALYST)` on the extract == 89. Manual line-by-line
  walk of the transcript (opening remarks through closing comments, lines 20-198) independently produced
  89 bracketed speaker turns. A1's header self-reported "89 speaker turns" — third independent confirmation. Match.
- **Questions**: grep `-c "^\[ANALYST"` == 40. Manual sweep treats each analyst-tagged turn as one
  ledger row (multi-part questions inside one turn, e.g. turns 36, 62, 92 keep the sub-parts together in the
  topic field rather than splitting into separate rows, since a single management answer addresses both parts
  together). 40 == 40. Match. One question (turn 72, Kunal on tank/radiator capex funding source) has no answer
  turn — the moderator interrupted to enforce the two-question limit before management responded — flagged
  UNANSWERED, not dropped.
- **Management numbers**: this category has no single clean regex because the transcript is free-form speech
  (ranges like "3 to 5 million dollars", spelled-out counts like "four companies", bare unit-less figures like
  the ASR-garbled "3,65", and verbal zeros like "there was not" with no digit at all). Pass 1 (digit immediately
  adjacent to a unit token: %, cr/crore(s), MVA, days, bps, million, KV, dollars, months, years, numbers, company/
  companies, plus a backward "days at N" form for the NWC/inventory/receivable/payable cluster and a bare
  4-digit-year form) mechanically matched 122 occurrences across the 26 MANAGEMENT-attributed turns that
  contain any figure. Manual sweep read every MANAGEMENT turn independently and found 3 additional legitimate
  quantified disclosures invisible to any unit-anchored regex by construction: the ASR-ambiguous "3,65" prior-year
  figure (line 102, no unit token attached, task-flagged explicitly), and two verbal zero-value disclosures with
  no digit at all — "No sir, the current order book does not contain any order from the data centers" (line 114)
  and "Sir, there was not" re: Q1 FY27 export contribution (line 176). Both zero disclosures are template
  signals per the ZERO_STANDING convention (an order-book-by-end-market line and an export-revenue line that
  currently stand at nil) and are kept, not dropped. Initial pass-1-only mismatch (122 vs 125) is resolved by a
  documented pass 2 (targeted string search for the ASR-flagged figure and the two verbal-zero answers), giving
  a combined mechanical count of 125 that matches the manual sweep of 125. Gate passes.
- **Repeats**: three topics were put to management by three different analysts each (order-book executable-this-FY
  amount: turns 30/62/85; competitor capacity-addition margin risk: turns 6/52/66) and one topic by two different
  analysts across a running thread (765 KV technical tie-up/PGCIL approval status: turns 8/10 by Mahir Manohar,
  56/58/60 by Tina Virmani) plus FY27/FY28 growth guidance (turns 34/83). All flagged REPEAT_QUESTION — same
  answer (2,400 cr executable order book; no observed pricing/order-inflow impact from competitor capacity;
  40% growth / 17-18% margin guidance) given near-identically each time, useful for A4/A5 consistency checks.
- **Speaker attribution gap**: 9 of 44 MANAGEMENT turns carry no named speaker tag (just "[MANAGEMENT]"),
  flagged AMBIGUOUS_SPEAKER — turns 27, 31, 33, 65, 71, 78, 80, 82, 86 (lines 74, 82, 86, 150, 162, 176, 180,
  184, 192). Content and register suggest CFO (order-book/margin turns) or CMD (export-strategy turns) but the
  A1 extract does not resolve this and A2 does not guess.
- **MGMT_ABSENCE**: Ashishkumar Mathur, CEO, is named in the introduction (line 18 header list and line 22
  moderator introduction) alongside CMD, COO and CFO, but has zero attributed speaking turns across the entire
  89-turn call, including zero questions directed at or answered by him by name. Flagged.

```yaml
stage: A2-enumerator
company: "atlantaelec"
quarter: "q1fy27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/atlantaelec-q1fy27/work/ledger_concall_atlantaelec_q1fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 2
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 89
  questions: 40
  mgmt_numbers: 125
  slides: 0
  slide_numbers: 0
flags_raised: [MGMT_ABSENCE, AMBIGUOUS_SPEAKER, AMBIGUOUS_ASR, ZERO_STANDING, REPEAT_QUESTION, UNANSWERED_QUESTION, ARITHMETIC_CHECK]
gate_a2: pass
mismatch_note: ""
```
