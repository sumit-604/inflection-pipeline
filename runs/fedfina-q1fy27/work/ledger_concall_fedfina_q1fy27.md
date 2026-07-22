# LEDGER — Concall Transcript — Fedbank Financial Services Ltd (FEDFINA) — Q1 FY27

Source: extract_concall_fedfina_q1fy27.txt (20 pages, 1189 lines, 100% page coverage)

Prior-quarter ledger: not available (not supplied for this run) — no DROPPED_SLIDE / cross-quarter diff possible.

```
=== A2 COUNT TEST ===
category: participants_header   grep_count: 8    sweep_count: 8    match: yes
category: participants_total    grep_count: 21   sweep_count: 21   match: yes   # 8 header-listed + 13 additional identified only by their speaker turns (12 analysts/Moderator-generic + 1 unattributed "Management")
category: turns                 grep_count: 109  sweep_count: 109  match: yes
category: questions             grep_count: 36   sweep_count: 36   match: yes   # grep = total analyst-side turns (44) minus non-question analyst turns (8: intro/rejoin/thanks/audio-check); sweep = independent per-analyst enumeration
category: mgmt_numbers          grep_count: 172  sweep_count: 172  match: yes   # regex sweep over concatenated per-turn text blocks (currency/%/bps/x-multiple/bare unit tokens; page furniture excluded; cross-line splits joined)
category: forward_commitment    grep_count: 43   sweep_count: 43   match: yes   # lexicon regex (guidance | will continue | we will | remains the same | reaffirm | committed | sustain | continue to) over management turns
category: hedge_phrases         grep_count: 53   sweep_count: 53   match: yes   # lexicon regex (may | might | could | hope | expect* | believe* | watchful | unknown | calibrating | unsure | cautious | aberrations | don't know | not indicative/comparable | watch it) over management turns
gate_a2: pass
=== END COUNT TEST ===
```

## 1. Participants

| # | Name | Designation / Firm | Side | Header-listed | Spoke (turns) | Flags |
|---|------|---------------------|------|----------------|----------------|-------|
| 1 | Mr. Parvez Mulla | Managing Director & CEO | Management | Yes (line 60-61) | Yes (30) |  |
| 2 | Mr. C.V. Ganesh | Chief Financial Officer | Management | Yes (line 62) | Yes (10: 1 as "C. V. Ganesh" + 7 as "C.V. Ganesh" + 2 as "CV Ganesh") | SPEAKER_LABEL_VARIANT — 3 different textual renderings of the same person |
| 3 | Mr. Jagadeesh Rao | Chief Business Officer, Gold Loans & Mortgages (Small Ticket) | Management | Yes (line 63-64) | Yes (3) |  |
| 4 | Mr. Shardul Kadam | Chief Transformation Officer | Management | Yes (line 65) | No (0 turns) | SILENT_ATTENDEE |
| 5 | Mr. K. Suresh | Chief Business Officer, Medium Ticket LAP | Management | Yes (line 66) | No (0 turns) | SILENT_ATTENDEE |
| 6 | Mr. Vikram Rathi | Chief Risk Officer | Management | Yes (line 67) | No (0 turns) | SILENT_ATTENDEE |
| 7 | Mr. Lokesh Pareek | Head of Investment Relations | Management | Yes (line 68) | Yes (1) |  |
| 8 | Mr. Shreepal Doshi | Equirus Securities | Moderator/Host (analyst side, call convener) | Yes (line 73, as MODERATOR) | Yes (1) |  |
| 9 | Moderator (generic conference operator) | Unnamed call operator | Neutral | No | Yes (19) | not a named individual |
| 10 | Digant Haria | Greenedge Wealth | Analyst | No | Yes (4) |  |
| 11 | Chetan Gindodia | Mahindra Manulife Mutual Fund | Analyst | No | Yes (2) |  |
| 12 | Rajiv Mehta | YES Securities | Analyst | No | Yes (3) |  |
| 13 | Renish | ICICI Securities (surname not given in transcript) | Analyst | No | Yes (4) | INCOMPLETE_NAME — no surname captured |
| 14 | Rahul Kumar | Vaikarya Fund | Analyst | No | Yes (2) |  |
| 15 | Yash Dantewadia | Dante | Analyst | No | Yes (8) |  |
| 16 | Devansh Dhruv | Equentis | Analyst | No | Yes (4) |  |
| 17 | Mohit M | Manglani Investments Private Limited | Analyst | No | Yes (2) | INCOMPLETE_NAME — surname abbreviated to "M" |
| 18 | Dinesh Loni | SHPL | Analyst | No | Yes (1) | NAME_INCONSISTENCY — Moderator addresses him as "Dinesh Lohani" at turn 77 (line 1023) |
| 19 | Pawan Kumar | Edelweiss | Analyst | No | Yes (6) |  |
| 20 | Ghansham Joshi | GJ's Techno Funda | Analyst | No | Yes (8) | call-quality disruption across turns 91-105 ("voice is breaking" x3) |
| 21 | Management (generic/unattributed) | Not identified individually | Management | No | Yes (1, turn 92, line 1104, "Yes.") | UNATTRIBUTED_SPEAKER |

MGMT_ABSENCE check: MD & CEO Parvez Mulla present and delivers 30 of 109 turns (opening remarks + majority of Q&A answers). No promoter/CMD absence on this call.

## 2. Speaker Turns (sequential, all 109)

| Turn | Line | Speaker | First 10 words | Flags |
|------|------|---------|-----------------|-------|
| 1 | 84 | Moderator | Ladies and gentlemen, good day, and welcome to the Q1 |  |
| 2 | 95 | Shreepal Doshi | Good afternoon, everyone. We welcome you all to the earnings |  |
| 3 | 105 | Lokesh Pareek | Thank you, Shreepal. Good afternoon, everyone. I would like to |  |
| 4 | 116 | Parvez Mulla | Thank you, Lokesh. Good afternoon, everyone. I would like to |  |
| 5 | 225 | C. V. Ganesh | Thank you, Parvez. Thanks everyone for your participation on the |  |
| 6 | 412 | Moderator | Thank you very much. We will now begin the question-and-answer |  |
| 7 | 416 | Digant Haria | Congratulations to Parvez, Ganeshji and the entire team, including Jagadeesh, |  |
| 8 | 428 | Parvez Mulla | Digant, thank you so much for the question, and thank |  |
| 9 | 464 | Digant Haria | Okay. Got it. My second question is around this entire |  |
| 10 | 472 | Parvez Mulla | Digant, our guidance remains the same, which we have been |  |
| 11 | 499 | Digant Haria | All right. That's very detailed. Thank you, Parvez. And last |  |
| 12 | 504 | Parvez Mulla | Mr. Jagadeesh already has earlier also along with Shardul, he |  |
| 13 | 543 | Digant Haria | Got it. Lastly, just a data point, did we have |  |
| 14 | 547 | Jagadeesh Rao | No, it's very less, less than INR1 crores. |  |
| 15 | 550 | Moderator | The next question is from the line of Chetan Gindodia |  |
| 16 | 553 | Chetan Gindodia | Hi sir, many congratulations on very good quarter. Just had |  |
| 17 | 561 | Parvez Mulla | Chetan, thank you so much. The medium ticket LAP and |  |
| 18 | 609 | Chetan Gindodia | Understood. Helpful. Sir, one thing is the credit cost margin |  |
| 19 | 614 | Parvez Mulla | Our regular credit cost has been around 0.7, so a |  |
| 20 | 618 | Moderator | The next question is from the line of Rajiv Mehta |  |
| 21 | 621 | Rajiv Mehta | Congrats on good numbers. I just want to understand this |  |
| 22 | 642 | Parvez Mulla | Rajiv, 2 ways to look at it. The Disbursals on |  |
| 23 | 649 | Rajiv Mehta | Sir, I was actually asking from a flow data point |  |
| 24 | 656 | Parvez Mulla | No. If I just give you one number and I'll |  |
| 25 | 668 | Jagadeesh Rao | Rajiv, it's the reverse, which has happened. If you look |  |
| 26 | 682 | Rajiv Mehta | Okay. I'll just come back because I've got more questions, |  |
| 27 | 685 | Parvez Mulla | Thank you, Rajiv. |  |
| 28 | 688 | Moderator | The next question is from the line of Renish from |  |
| 29 | 691 | Renish | Congrats on a good set of numbers. Sir, just one |  |
| 30 | 704 | CV Ganesh | Renish, thank you for that question. So you're right. I |  |
| 31 | 720 | Renish | Got it. So just a follow-up on that, sir. So |  |
| 32 | 726 | Jagadeesh Rao | Renish in the first quarter, the regime, we were all |  |
| 33 | 735 | Parvez Mulla | Overall, Renish, the credit cost guidance remains same. At the |  |
| 34 | 751 | Renish | Okay. Sir, just a last clarification. So now since we |  |
| 35 | 764 | Parvez Mulla | The yields, if you remember, last year also, we had |  |
| 36 | 774 | Renish | Got it. So just a shift from, let's say, 3 |  |
| 37 | 778 | Parvez Mulla | Correct. Thank you, Renish. |  |
| 38 | 781 | Moderator | The next question is from the line of Rahul Kumar |  |
| 39 | 784 | Rahul Kumar | Just on the ST LAP segment or the mortgage actually, |  |
| 40 | 788 | Parvez Mulla | After the slippages in this quarter also have been quite |  |
| 41 | 803 | Rahul Kumar | Okay. And if you can help us understand the guidance |  |
| 42 | 807 | Parvez Mulla | What we have guided, Rahul, for the year FY '27 |  |
| 43 | 827 | Moderator | Rahul Kumar, I will request you to rejoin the queue. |  |
| 44 | 831 | Yash Dantewadia | Congratulations on a great set of numbers. So, I brought |  |
| 45 | 837 | Parvez Mulla | So if the price doesn't move, then we are expecting |  |
| 46 | 842 | Yash Dantewadia | No, I meant gold AUM as a percentage of your |  |
| 47 | 845 | Parvez Mulla | Okay. Yes. So that mix will arithmetic be slightly higher. |  |
| 48 | 849 | Yash Dantewadia | If it stays stagnant then? |  |
| 49 | 852 | Parvez Mulla | No, the mix gold percentage will be higher. |  |
| 50 | 855 | Yash Dantewadia | Right. But can you quantify higher, just assume gold does |  |
| 51 | 858 | Parvez Mulla | See, we track it as a percentage of our AUM, |  |
| 52 | 863 | Yash Dantewadia | Right. And there is some stress on small ticket size |  |
| 53 | 870 | Parvez Mulla | Yash. We are not seeing any stress on the LAP |  |
| 54 | 874 | Yash Dantewadia | No, I'm seeing as a sector, on small LAP loans, |  |
| 55 | 877 | Parvez Mulla | See, you will have to look at the ticket size, |  |
| 56 | 885 | Yash Dantewadia | Right. So on the 18% growth, where is this going |  |
| 57 | 894 | Parvez Mulla | The AUM growth, which I said at an entity level |  |
| 58 | 899 | Yash Dantewadia | Yes. And so in the LAP segment, what's going to |  |
| 59 | 905 | Parvez Mulla | See, right now, no, because it operates at a different |  |
| 60 | 925 | Moderator | The next question is from the line of Devansh Dhruv |  |
| 61 | 928 | Devansh Dhruv | Congratulations on a great set of numbers. My question was |  |
| 62 | 934 | Parvez Mulla | So Devansh, thank you so much. That's a good question. |  |
| 63 | 947 | Devansh Dhruv | Okay. so, historically, we have on a maximum basis open |  |
| 64 | 960 | Parvez Mulla | Yes. It should be -- you should see the spillover |  |
| 65 | 963 | Devansh Dhruv | Okay. So our guidance remains for 200 branches, right? |  |
| 66 | 966 | Parvez Mulla | Yes, sir. |  |
| 67 | 969 | Devansh Dhruv | Okay, okay. And my second question would be what are |  |
| 68 | 973 | Parvez Mulla | See, the 1-plus numbers right now are looking different, because |  |
| 69 | 979 | CV Ganesh | I'll just maybe add to that. See, I think in |  |
| 70 | 984 | Moderator | Mr. Devansh Dhruv, I would request to please rejoin the |  |
| 71 | 988 | Mohit M | Firstly, many congratulations on this earnings. I just wanted some |  |
| 72 | 992 | Parvez Mulla | Mohit, right now we are not seeing anything. Maybe it |  |
| 73 | 997 | Mohit M | All right. Thank you so much. |  |
| 74 | 1000 | Moderator | Thank you. The next question is from the line of |  |
| 75 | 1003 | Dinesh Loni | Many congratulation to the team. I just want to ask |  |
| 76 | 1007 | Parvez Mulla | As far as expansion is concerned, we are present in |  |
| 77 | 1023 | Moderator | Mr. Dinesh Lohani, I would request you to rejoin the | NAME_INCONSISTENCY (moderator says "Dinesh Lohani"; speaker was introduced/labeled "Dinesh Loni") |
| 78 | 1027 | Pawan Kumar | Mostly around some of the numbers. Like the provisions have |  |
| 79 | 1035 | Parvez Mulla | Yes. So Pawan, first of all, the number that you |  |
| 80 | 1040 | C.V. Ganesh | Thank you, Parvez. Pawan, the credit cost during the year, |  |
| 81 | 1055 | Pawan Kumar | So you have done INR589 crores of LAP DA, right? |  |
| 82 | 1059 | C.V. Ganesh | I got -- so basically, the DA numbers there now |  |
| 83 | 1062 | Pawan Kumar | Okay. But these are 37 months of outstanding maturity. So |  |
| 84 | 1065 | C.V. Ganesh | Just 1 second. I'm a little unsure, you're looking at |  |
| 85 | 1068 | Pawan Kumar | I'm looking at Page 7 of the quarterly numbers? Not |  |
| 86 | 1073 | C.V. Ganesh | So that would be an average across the gold loan |  |
| 87 | 1079 | Pawan Kumar | We had a loss on DA this quarter, right? |  |
| 88 | 1088 | C.V. Ganesh | That is correct. The way the accounting for DA works |  |
| 89 | 1094 | Pawan Kumar | Got it. Thank you so much. |  |
| 90 | 1097 | Moderator | Thank you. The next question is from the line of |  |
| 91 | 1101 | Ghansham Joshi | Yes. Am I audible? |  |
| 92 | 1104 | Management | Yes. | UNATTRIBUTED_SPEAKER (labeled "Management", not a named individual) |
| 93 | 1107 | Ghansham Joshi | Yes. Thank you for giving me the opportunity. Prime Facie |  |
| 94 | 1111 | Moderator | Sorry to interrupt you, sir, your voice is breaking. |  |
| 95 | 1114 | Ghansham Joshi | The next 3 percentage from mortgage. |  |
| 96 | 1117 | Moderator | Mr. Ghansham Joshi your voice is breaking. |  |
| 97 | 1120 | Ghansham Joshi | Hello. |  |
| 98 | 1123 | Moderator | Hello. Sir, your voice is breaking can you please repeat |  |
| 99 | 1126 | Ghansham Joshi | Am I audible now? |  |
| 100 | 1129 | Moderator | Yes, sir. It's better. |  |
| 101 | 1132 | Ghansham Joshi | Yes. So, the net percentage -- net Stage 3 percentage |  |
| 102 | 1136 | C.V. Ganesh | In the last call, the March call, we had mentioned |  |
| 103 | 1147 | Ghansham Joshi | Okay. Thanks for the reply and… |  |
| 104 | 1150 | Moderator | Sorry to interrupt you, sir. Ghansham Joshi, sir your voice |  |
| 105 | 1159 | Ghansham Joshi | While publishing the results while taking by when you are |  |
| 106 | 1163 | C.V. Ganesh | Okay. Your suggestion is we converted into PDF and do |  |
| 107 | 1167 | Moderator | This was the last question of today. I now hand |  |
| 108 | 1171 | Parvez Mulla | Thank you so much. It was an interesting quarter. I |  |
| 109 | 1182 | Moderator | On behalf of Equirus Securities, that concludes this conference. Thank |  |
## 3. Questions (36, one row per distinct question/follow-up turn)

| # | Analyst | Firm | Turn | Line | Topic | Flags |
|---|---------|------|------|------|-------|-------|
| 1 | Digant Haria | Greenedge Wealth | 7 | 416 | New LTV/RBI guideline positioning vs banks (NBFC IGL product comparison) |  |
| 2 | Digant Haria | Greenedge Wealth | 9 | 464 | Gold price correction impact on growth outlook (AUM guidance sensitivity) | REPEAT_QUESTION — gold AUM growth guidance re-asked; see Q4/#22 below |
| 3 | Digant Haria | Greenedge Wealth | 11 | 499 | Jagadeesh Rao's expanded mandate — new products or existing mortgage piece? |  |
| 4 | Digant Haria | Greenedge Wealth | 13 | 543 | Auctions this quarter — did any occur, and quantum? |  |
| 5 | Chetan Gindodia | Mahindra Manulife Mutual Fund | 16 | 553 | Medium/small ticket LAP disbursement outlook and 1-2 year growth aspiration |  |
| 6 | Chetan Gindodia | Mahindra Manulife Mutual Fund | 18 | 609 | Credit cost margin sequential uptick — driven by write-offs, and quantum? | REPEAT_QUESTION — credit cost trend; see #10 (Renish) |
| 7 | Rajiv Mehta | YES Securities | 21 | 621 | Gold loan disbursement growth (15-20% YoY) vs gold price (+35-40%) and capacity growth (20%) — where is the volume hit? |  |
| 8 | Rajiv Mehta | YES Securities | 23 | 649 | Follow-up: clarifying the disbursement-vs-AUM-growth flow-data framing |  |
| 9 | Renish | ICICI Securities | 29 | 691 | PCR at historical high (38-40%) — should credit cost trend down for rest of FY27? | REPEAT_QUESTION — credit cost trend |
| 10 | Renish | ICICI Securities | 31 | 720 | Follow-up: Stage 2 increase of 50 bps QoQ — confirm it is entirely the gold regulatory reclassification |  |
| 11 | Renish | ICICI Securities | 34 | 751 | Follow-up: mortgage GNPA/West Asia crisis/monsoon exposure |  |
| 12 | Renish | ICICI Securities | 36 | 774 | Follow-up: shift from bullet/3-6 month loans to 1-month loans — impact on yields/spreads |  |
| 13 | Rahul Kumar | Vaikarya Fund | 39 | 784 | ST LAP/mortgage flow-to-stress this quarter vs previous quarter | REPEAT_QUESTION — asset-quality-stress topic; see #22 (Mohit M), #17 (Yash Dantewadia) |
| 14 | Rahul Kumar | Vaikarya Fund | 41 | 803 | Opex-to-assets / opex-to-income guidance for FY27 |  |
| 15 | Yash Dantewadia | Dante | 44 | 831 | AUM expansion by segment (gold vs rest) for the next 3 quarters | REPEAT_QUESTION — gold AUM growth guidance; see #2 (Digant Haria) |
| 16 | Yash Dantewadia | Dante | 46 | 842 | Follow-up: gold AUM as % of total book, not absolute growth |  |
| 17 | Yash Dantewadia | Dante | 48 | 849 | Follow-up: mix % if gold price stays stagnant |  |
| 18 | Yash Dantewadia | Dante | 50 | 855 | Follow-up: quantify the mix-shift in percentage points |  |
| 19 | Yash Dantewadia | Dante | 52 | 863 | Stress on small ticket LAP this quarter — sector-level color | REPEAT_QUESTION — asset-quality-stress topic |
| 20 | Yash Dantewadia | Dante | 54 | 874 | Follow-up: reiterating sector-level small-LAP stress claim |  |
| 21 | Yash Dantewadia | Dante | 56 | 885 | 18% LAP growth — what will drive it? New segments? |  |
| 22 | Yash Dantewadia | Dante | 58 | 899 | Follow-up: small vs medium LAP growth driver, entry into prime/ultra-luxury (>5cr) segment |  |
| 23 | Devansh Dhruv | Equentis | 61 | 928 | Branch expansion strategy — 200-branch guidance, zero branches added in Q1, reason |  |
| 24 | Devansh Dhruv | Equentis | 63 | 947 | Follow-up: historical max branch run-rate (50-60), spillover quantum and timing |  |
| 25 | Devansh Dhruv | Equentis | 65 | 963 | Follow-up: confirm 200-branch guidance still stands |  |
| 26 | Devansh Dhruv | Equentis | 67 | 969 | 1+ DPD, 30+ DPD, 60+ DPD numbers for the quarter |  |
| 27 | Mohit M | Manglani Investments Private Limited | 71 | 988 | Any pockets of stress emerging from macroeconomic conditions? | REPEAT_QUESTION — asset-quality-stress topic |
| 28 | Dinesh Loni | SHPL | 75 | 1003 | Territorial expansion plans and 3-4 year growth plans |  |
| 29 | Pawan Kumar | Edelweiss | 78 | 1027 | Provisions down ~40cr on GS3 assets, apparent ~75cr write-off, FVOCI loss of 585cr in OCI, ~12-15cr loss on 589cr LAP assignment — reconcile all three |  |
| 30 | Pawan Kumar | Edelweiss | 81 | 1055 | Follow-up: INR589cr LAP DA — confirm classification and closure |  |
| 31 | Pawan Kumar | Edelweiss | 83 | 1062 | Follow-up: 37-month outstanding maturity on the 489cr transferred — implies all LAP? |  |
| 32 | Pawan Kumar | Edelweiss | 85 | 1068 | Follow-up: clarifying source document (LODR filing vs quarterly financial results page 7) |  |
| 33 | Pawan Kumar | Edelweiss | 87 | 1079 | Follow-up: confirm a loss on DA this quarter |  |
| 34 | Ghansham Joshi | GJ's Techno Funda | 95 | 1114 | Mortgage-related question (garbled by call-quality issue, restated at #35) | call-quality disruption |
| 35 | Ghansham Joshi | GJ's Techno Funda | 101 | 1132 | Net Stage 3 % of mortgage rising QoQ/YoY — how will this be tackled? | restatement of #34 after 3 interruptions |
| 36 | Ghansham Joshi | GJ's Techno Funda | 105 | 1159 | Suggestion: convert results to PDF with digital signature before publishing (not a financial question) | not a financial/operating question — procedural suggestion |

REPEAT_QUESTION clusters identified: (a) credit cost trend — Chetan Gindodia #6, Renish #9; 
(b) asset-quality-stress pockets — Rahul Kumar #13, Yash Dantewadia #19, Mohit M #27; 
(c) gold AUM growth guidance (25-30%) — Digant Haria #2, Yash Dantewadia #15.
## 4. Numbers Spoken by Management (172; feeds Role 5 arithmetic-consistency check)

Unit: mechanical regex sweep over each management turn's text (currency ₹/INR/Rs + Cr/crore/lakh, %, bps, x-multiple, and bare digit + branches/states/years/months), cross-line splits joined, page furniture excluded. One row per matched token, in document order.

| # | Turn | Line | Speaker | Value | Context |
|---|------|------|---------|-------|---------|
| 1 | 4 | 125 | Parvez Mulla | 1% | ...to hold credit costs at around 1%. This consistency is the foundation on... |
| 2 | 4 | 130 | Parvez Mulla | 14% | ...priorities, Our Disbursements increased 14% YoY to ₹6,760 Cr, and our AUM grew... |
| 3 | 4 | 130 | Parvez Mulla | ₹6,760 Cr | ...Our Disbursements increased 14% YoY to ₹6,760 Cr, and our AUM grew                   35%... |
| 4 | 4 | 131 | Parvez Mulla | 35% | ...Cr, and our AUM grew                   35% YoY to ₹21,136 Cr.... |
| 5 | 4 | 131 | Parvez Mulla | ₹21,136 Cr | ...r AUM grew                   35% YoY to ₹21,136 Cr.                     Our Gold Loan busi... |
| 6 | 4 | 134 | Parvez Mulla | 15% | ...this growth, with disbursements rising 15% YoY to ₹6,087                   Cr and... |
| 7 | 4 | 134 | Parvez Mulla | ₹6,087 | ...h, with disbursements rising 15% YoY to ₹6,087                   Cr and AUM increasing... |
| 8 | 4 | 135 | Parvez Mulla | 77% | ...Cr and AUM increasing 77% YoY to ₹11,191 Cr. Our Doorstep Gold Lo... |
| 9 | 4 | 135 | Parvez Mulla | ₹11,191 Cr | ...Cr and AUM increasing 77% YoY to ₹11,191 Cr. Our Doorstep Gold Loan offering mainta... |
| 10 | 4 | 136 | Parvez Mulla | 96.5% | ...strong momentum, with AUM growing 96.5% YoY to ₹1,787 Cr. AUM per branch stood... |
| 11 | 4 | 136 | Parvez Mulla | ₹1,787 Cr | ...momentum, with AUM growing 96.5% YoY to ₹1,787 Cr. AUM per branch stood at ₹17.7... |
| 12 | 4 | 136 | Parvez Mulla | ₹17.7 | ...Y to ₹1,787 Cr. AUM per branch stood at ₹17.7                   Cr, while gold tonnage... |
| 13 | 4 | 138 | Parvez Mulla | 67.9% | ...ith the                   LTV on AUM at 67.9%.    Our Mortgage business continued to... |
| 14 | 4 | 146 | Parvez Mulla | 4% | ...y growth, with disbursements increasing 4% YoY to ₹673 Cr and AUM rising 14% YoY t... |
| 15 | 4 | 147 | Parvez Mulla | ₹673 Cr | ...with disbursements increasing 4% YoY to ₹673 Cr and AUM rising 14% YoY to ₹9,777 Cr. Ou... |
| 16 | 4 | 147 | Parvez Mulla | 14% | ...easing 4% YoY to ₹673 Cr and AUM rising 14% YoY to ₹9,777 Cr. Our focus remains fir... |
| 17 | 4 | 147 | Parvez Mulla | ₹9,777 Cr | ...oY to ₹673 Cr and AUM rising 14% YoY to ₹9,777 Cr. Our focus remains firmly on prudent po... |
| 18 | 4 | 163 | Parvez Mulla | 6.86% | ...5.7 million equity shares, representing 6.86% of the Company’s paid-up equity share c... |
| 19 | 4 | 172 | Parvez Mulla | 30 years | ...siness Head – Gold Loans, bringing over 30 years of experience across retail banking. He... |
| 20 | 4 | 192 | Parvez Mulla | ₹13 Cr | ...a negative direct assignment income of ₹13 Cr during the quarter — a direct consequen... |
| 21 | 4 | 194 | Parvez Mulla | 33% | ...expand its core earnings, delivering a 33%                          YoY increase i... |
| 22 | 4 | 204 | Parvez Mulla | 0.8% | ...in net income. Credit costs remained at 0.8%, well within our guided range of below... |
| 23 | 4 | 205 | Parvez Mulla | 1% | ...ided range of below                     1%.                       On asset quality... |
| 24 | 4 | 208 | Parvez Mulla | 1.6% | ...On asset quality, our GNPA moved to 1.6% from 1.9% in Q4, our provision coverage... |
| 25 | 4 | 208 | Parvez Mulla | 1.9% | ...et quality, our GNPA moved to 1.6% from 1.9% in Q4, our provision coverage increased... |
| 26 | 4 | 209 | Parvez Mulla | 38% | ...verage increased to                     38%, and net NPA stood at 1.0%.... |
| 27 | 4 | 209 | Parvez Mulla | 1.0% | ...38%, and net NPA stood at 1.0%.                       The quarter conc... |
| 28 | 4 | 212 | Parvez Mulla | ₹114.4 Cr | ...er concluded with a profit after tax of ₹114.4 Cr, a YoY growth of 52.5%, an ROA of 2.6%... |
| 29 | 4 | 212 | Parvez Mulla | 52.5% | ...after tax of ₹114.4 Cr, a YoY growth of 52.5%, an ROA of 2.6%                     and... |
| 30 | 4 | 212 | Parvez Mulla | 2.6% | ....4 Cr, a YoY growth of 52.5%, an ROA of 2.6%                     and an ROE of 15.4%... |
| 31 | 4 | 213 | Parvez Mulla | 15.4% | ...2.6%                     and an ROE of 15.4%.                       Taken together,... |
| 32 | 5 | 235 | C. V. Ganesh | 5% | ...odest AUM growth in Q1. AUM grew almost 5% sequentially QOQ, and 34.7% YOY.... |
| 33 | 5 | 235 | C. V. Ganesh | 34.7% | ...UM grew almost 5% sequentially QOQ, and 34.7% YOY.                 •   Gold loans rem... |
| 34 | 5 | 238 | C. V. Ganesh | ₹11,191 Cr | ...•   Gold Loan AUM increased to ₹11,191 Cr, up nearly 77% year-on-year. Mortgage A... |
| 35 | 5 | 238 | C. V. Ganesh | 77% | ...AUM increased to ₹11,191 Cr, up nearly 77% year-on-year. Mortgage AUM also... |
| 36 | 5 | 239 | C. V. Ganesh | ₹9,777 Cr | ...d on a healthy trajectory and closed at ₹9,777 Cr, growing approximately 15% year-on-year... |
| 37 | 5 | 239 | C. V. Ganesh | 15% | ...sed at ₹9,777 Cr, growing approximately 15% year-on-year.                 •   Conse... |
| 38 | 5 | 240 | C. V. Ganesh | ₹21,000 Cr | ...•   Consequently, total AUM crossed the ₹21,000 Cr milestone during the quarter coming in... |
| 39 | 5 | 240 | C. V. Ganesh | ₹21,136 | ...lestone during the quarter coming in at ₹21,136                     Cr                 •... |
| 40 | 5 | 243 | C. V. Ganesh | 15% | ...d-winds of declining domestic prices of 15% between Jan 31st to June 30th.... |
| 41 | 5 | 246 | C. V. Ganesh | 8.1 % | ...changes, we delivered a 8.1 % QOQ sequential growth in Gold loan AUM.... |
| 42 | 5 | 247 | C. V. Ganesh | 1% | ...able to marginally grow gold tonnage by 1% sequentially QOQ in Q1.... |
| 43 | 5 | 253 | C. V. Ganesh | 12.3% | ...rong. Our Core Net Interest income grew 12.3%                     sequentially QOQ an... |
| 44 | 5 | 254 | C. V. Ganesh | 40.6% | ...sequentially QOQ and 40.6% YOY.                 •   We consciously... |
| 45 | 5 | 255 | C. V. Ganesh | 6.6% | ...ncome. NII (net of DA income) increased 6.6% sequentially QOQ                     an... |
| 46 | 5 | 256 | C. V. Ganesh | 38.7% | ...equentially QOQ                     and 38.7% YOY.                 •   So, while NII... |
| 47 | 5 | 257 | C. V. Ganesh | 2.4% | ...e NII grew, Operating expenses declined 2.4% sequentially, resulting in a very stron... |
| 48 | 5 | 258 | C. V. Ganesh | 50% | ...rong PPOP                     growth of 50% YOY which I will cover separately.... |
| 49 | 5 | 271 | C. V. Ganesh | 10 bps | ...elds (exc. DA) grew QOQ sequentially by 10 bps to 15.7% on Avg loan book and 15% on Av... |
| 50 | 5 | 271 | C. V. Ganesh | 15.7% | ...DA) grew QOQ sequentially by 10 bps to 15.7% on Avg loan book and 15% on Avg     tot... |
| 51 | 5 | 271 | C. V. Ganesh | 15% | ...by 10 bps to 15.7% on Avg loan book and 15% on Avg     total assets. •   We had adv... |
| 52 | 5 | 275 | C. V. Ganesh | 30 bps | ...g costs in Q1 remained heightened by 20/30 bps over Q4,     we were able to bring in o... |
| 53 | 5 | 276 | C. V. Ganesh | 3 bps | ...ted average COB marginally lower QOQ by 3 bps. •   That being said we remain cautious... |
| 54 | 5 | 282 | C. V. Ganesh | 10 bps | ...Interest expenses     showing a rise by 10 bps in the ROA tree. •   We hope that most... |
| 55 | 5 | 296 | C. V. Ganesh | 2.2 % | ...rm.       Our increase in Stage II from 2.2 % to 2.7% is entirely due to this re-adju... |
| 56 | 5 | 296 | C. V. Ganesh | 2.7% | ...Our increase in Stage II from 2.2 % to 2.7% is entirely due to this re-adjustment.... |
| 57 | 5 | 303 | C. V. Ganesh | 30 bps | ...On asset quality, our GNPAs reduced 30 bps to 1.6% in Q1 (from 1.9% in Q4) and net... |
| 58 | 5 | 303 | C. V. Ganesh | 1.6% | ...et quality, our GNPAs reduced 30 bps to 1.6% in Q1 (from 1.9% in Q4) and net NPA als... |
| 59 | 5 | 303 | C. V. Ganesh | 1.9% | ...NPAs reduced 30 bps to 1.6% in Q1 (from 1.9% in Q4) and net NPA also     reduced 30... |
| 60 | 5 | 304 | C. V. Ganesh | 30 bps | ....9% in Q4) and net NPA also     reduced 30 bps falling marginally below 1.0% for the f... |
| 61 | 5 | 304 | C. V. Ganesh | 1.0% | ...reduced 30 bps falling marginally below 1.0% for the first time.       While flows h... |
| 62 | 5 | 306 | C. V. Ganesh | 30 bps | ...oved policy, which has resulted in this 30 bps drop in GNPA.     Without the write-off... |
| 63 | 5 | 307 | C. V. Ganesh | 1.87 % | ...rite-offs the GNPAs would have stood at 1.87 %.       Our provision coverage increased... |
| 64 | 5 | 310 | C. V. Ganesh | 38.36 % | ...Our provision coverage increased to 38.36 % in Q1. This is because of the mortgage... |
| 65 | 5 | 315 | C. V. Ganesh | 6 bps | ...Our Credit costs are marginally up 6 bps Q0Q due to the combined effect of the a... |
| 66 | 5 | 316 | C. V. Ganesh | 0.8% | ...have been able to contain it at the 0.8% levels.       The increase in gold loan... |
| 67 | 5 | 319 | C. V. Ganesh | 7% | ...The increase in gold loan LTVs by 7% - is attributable primarily to the decl... |
| 68 | 5 | 333 | C. V. Ganesh | Rs 187.5 Cr | ...in Pre-provisioning Operating Profit at Rs 187.5 Cr growing 15.2% sequentially and 50% YOY.... |
| 69 | 5 | 333 | C. V. Ganesh | 15.2% | ...Operating Profit at Rs 187.5 Cr growing 15.2% sequentially and 50% YOY. Our PAT also... |
| 70 | 5 | 333 | C. V. Ganesh | 50% | ...187.5 Cr growing 15.2% sequentially and 50% YOY. Our PAT also grew 52.5% YOY.   In... |
| 71 | 5 | 333 | C. V. Ganesh | 52.5% | ...entially and 50% YOY. Our PAT also grew 52.5% YOY.   In the last quarter we reported... |
| 72 | 5 | 343 | C. V. Ganesh | 15% | ...crossed the psychological milestone of 15% - coming in at 15.4 %. This represents... |
| 73 | 5 | 343 | C. V. Ganesh | 15.4 % | ...logical milestone of 15% - coming in at 15.4 %. This represents an expansion of 380 bp... |
| 74 | 5 | 343 | C. V. Ganesh | 380 bps | ...15.4 %. This represents an expansion of 380 bps YOY in ROE (from 11.6% in Q1’26)   We r... |
| 75 | 5 | 344 | C. V. Ganesh | 11.6% | ...n expansion of 380 bps YOY in ROE (from 11.6% in Q1’26)   We remain deeply grateful t... |
| 76 | 5 | 359 | C. V. Ganesh | 5.5% | ...of Average total assets had reduced to 5.5% (from 5.9% a year ago) giving some gree... |
| 77 | 5 | 359 | C. V. Ganesh | 5.9% | ...total assets had reduced to 5.5% (from 5.9% a year ago) giving some green shoots on... |
| 78 | 5 | 361 | C. V. Ganesh | 4.8% | ...in with an Opex to Avg. total assets of 4.8% (an improvement of 70 bps) sequentially... |
| 79 | 5 | 361 | C. V. Ganesh | 70 bps | ...total assets of 4.8% (an improvement of 70 bps) sequentially QoQ.   This creates space... |
| 80 | 5 | 368 | C. V. Ganesh | 400 bps | ...come also showed an improvement of over 400 bps sequentially Q0Q – coming in at 52.8% (... |
| 81 | 5 | 369 | C. V. Ganesh | 52.8% | ...400 bps sequentially Q0Q – coming in at 52.8% (from the annualised number of 57.2% in... |
| 82 | 5 | 369 | C. V. Ganesh | 57.2% | ...at 52.8% (from the annualised number of 57.2% in FY26). While we have kept a keen eye... |
| 83 | 5 | 394 | C. V. Ganesh | 20.71 % | ...Our CRAR came in at 20.71 % (compared to 22.4% in q4). Some part of... |
| 84 | 5 | 394 | C. V. Ganesh | 22.4% | ...ur CRAR came in at 20.71 % (compared to 22.4% in q4). Some part of this reduction was... |
| 85 | 8 | 430 | Parvez Mulla | 85% | ...tor has permitted that you can go up to 85% on certain ticket sizes in certain... |
| 86 | 8 | 431 | Parvez Mulla | 85% | ...categories. But, if you go 85% on bullet loans, then you have to subtr... |
| 87 | 8 | 432 | Parvez Mulla | 15% | ...means you'll have to subtract 15% interest if you're charging, then the L... |
| 88 | 10 | 475 | Parvez Mulla | 25% | ...old                 AUM growth of about 25% to 30%. And that we are saying, first,... |
| 89 | 10 | 475 | Parvez Mulla | 30% | ...AUM growth of about 25% to 30%. And that we are saying, first, is will... |
| 90 | 10 | 476 | Parvez Mulla | 5 years | ...growth. As we have shown in the past 5 years, our tonnage growth has been consistent... |
| 91 | 10 | 476 | Parvez Mulla | 10% | ...nage growth has been consistently about 10%                 to 12%. Last year also... |
| 92 | 10 | 477 | Parvez Mulla | 12% | ...nsistently about 10%                 to 12%. Last year also we gave a tonnage growt... |
| 93 | 10 | 477 | Parvez Mulla | 12% | ...t year also we gave a tonnage growth of 12%. The first quarter and second quarter a... |
| 94 | 10 | 495 | Parvez Mulla | INR134 | ...So if this last 30-day average price is INR134 and the spot                 price is IN... |
| 95 | 10 | 496 | Parvez Mulla | INR129, | ...4 and the spot                 price is INR129, then I will take INR129 into my calculat... |
| 96 | 10 | 496 | Parvez Mulla | INR129 | ...price is INR129, then I will take INR129 into my calculation, and I will lend at... |
| 97 | 12 | 518 | Parvez Mulla | 200 branches | ...means our existing ST LAP branches, the 200 branches which were distributing... |
| 98 | 12 | 539 | Parvez Mulla | 4 years | ...that we have in the future of, say 3 to 4 years down the line making the branch, the... |
| 99 | 14 | 547 | Jagadeesh Rao | INR1 crores | ...Rao:     No, it's very less, less than INR1 crores.... |
| 100 | 17 | 566 | Parvez Mulla | 20% | ...s that we will grow the entity at about 20% to 25%.                    So if gold w... |
| 101 | 17 | 566 | Parvez Mulla | 25% | ...we will grow the entity at about 20% to 25%.                    So if gold without... |
| 102 | 17 | 567 | Parvez Mulla | 25% | ...old without the price increase grows at 25% to 30%, the LAP segment will also grow... |
| 103 | 17 | 567 | Parvez Mulla | 30% | ...hout the price increase grows at 25% to 30%, the LAP segment will also grow at 20%.... |
| 104 | 17 | 567 | Parvez Mulla | 20% | ...30%, the LAP segment will also grow at 20%.                    Within that, the me... |
| 105 | 22 | 643 | Parvez Mulla | 8% | ...ok at our gold loan AUM growth is about 8%, if I have to break that 8% for you, 1%... |
| 106 | 22 | 643 | Parvez Mulla | 8% | ...th is about 8%, if I have to break that 8% for you, 1%                  has come f... |
| 107 | 22 | 643 | Parvez Mulla | 1% | ...8%, if I have to break that 8% for you, 1%                  has come from the tonn... |
| 108 | 22 | 645 | Parvez Mulla | 4% | ...rs, there is a price drop. So of almost 4% to 5%. So, you will have a plus 1, minu... |
| 109 | 22 | 645 | Parvez Mulla | 5% | ...ere is a price drop. So of almost 4% to 5%. So, you will have a plus 1, minus 5% a... |
| 110 | 22 | 645 | Parvez Mulla | 5% | ...o 5%. So, you will have a plus 1, minus 5% and                  about my LTV has m... |
| 111 | 22 | 646 | Parvez Mulla | 61% | ...about my LTV has moved up from 61% to 68%. So that is the 7%, that is 10%.... |
| 112 | 22 | 646 | Parvez Mulla | 68% | ...about my LTV has moved up from 61% to 68%. So that is the 7%, that is 10%. So tha... |
| 113 | 22 | 646 | Parvez Mulla | 7% | ...oved up from 61% to 68%. So that is the 7%, that is 10%. So that's the math.... |
| 114 | 22 | 646 | Parvez Mulla | 10% | ...61% to 68%. So that is the 7%, that is 10%. So that's the math.... |
| 115 | 24 | 662 | Parvez Mulla | INR5,000 crores | ....                    So, if I did about INR5,000 crores of disbursement, I got a INR400 crores... |
| 116 | 24 | 662 | Parvez Mulla | INR400 crores | ...NR5,000 crores of disbursement, I got a INR400 crores of growth last year first... |
| 117 | 24 | 663 | Parvez Mulla | INR6,000 crores | ...quarter. And this time with the INR6,000 crores, I got a INR800 crores growth in AUM. S... |
| 118 | 24 | 663 | Parvez Mulla | INR800 crores | ...time with the INR6,000 crores, I got a INR800 crores growth in AUM. So the... |
| 119 | 25 | 674 | Jagadeesh Rao | INR2.5 lakhs | ...ticket size more than                  INR2.5 lakhs.                    Even though you hav... |
| 120 | 25 | 677 | Jagadeesh Rao | INR2.5 lakhs | ...lending, plus being in LTV controls at INR2.5 lakhs                  - anything above INR2.... |
| 121 | 25 | 678 | Jagadeesh Rao | INR2.5 lakhs | ...lakhs                  - anything above INR2.5 lakhs you can't give that 85% LTV range – tha... |
| 122 | 25 | 678 | Jagadeesh Rao | 85% | ...above INR2.5 lakhs you can't give that 85% LTV range – that has played a lot. Ther... |
| 123 | 33 | 736 | Parvez Mulla | 1% | ...credit cost guidance will be sub-1%. And as far as the mortgage GNPAs are c... |
| 124 | 35 | 766 | Parvez Mulla | 12% | ...at a particular yield of about 12%, 12.5%. That is coming under pressure.... |
| 125 | 35 | 766 | Parvez Mulla | 12.5% | ...at a particular yield of about 12%, 12.5%. That is coming under pressure. And gol... |
| 126 | 42 | 808 | Parvez Mulla | 30 bps | ...the ROA by                 about 20 to 30 bps over the average ROA, that we had given... |
| 127 | 42 | 809 | Parvez Mulla | 2.4% | ...given an average ROA of about 2.4%. So we had guided that we will do avera... |
| 128 | 42 | 812 | Parvez Mulla | 30 bps | ...er.                   That is the 20 to 30 bps expansion. And that 20 to 30 bps expans... |
| 129 | 42 | 812 | Parvez Mulla | 30 bps | ...20 to 30 bps expansion. And that 20 to 30 bps expansion will happen with a combinatio... |
| 130 | 42 | 815 | Parvez Mulla | 10 bps | ...ay out. So it could be a combination of 10 bps here and 20 bps into the... |
| 131 | 42 | 815 | Parvez Mulla | 20 bps | ...uld be a combination of 10 bps here and 20 bps into the                 other element,... |
| 132 | 45 | 838 | Parvez Mulla | 25% | ...AUM should grow by about 25% to 30%. And at an entity level, we are... |
| 133 | 45 | 838 | Parvez Mulla | 30% | ...AUM should grow by about 25% to 30%. And at an entity level, we are expecti... |
| 134 | 45 | 838 | Parvez Mulla | 20% | ...y level, we are expecting to grow about 20%                    to 22%. And the mort... |
| 135 | 45 | 839 | Parvez Mulla | 22% | ...to grow about 20%                    to 22%. And the mortgage AUM will grow between... |
| 136 | 45 | 839 | Parvez Mulla | 15% | ...And the mortgage AUM will grow between 15% to 20%.... |
| 137 | 45 | 839 | Parvez Mulla | 20% | ...e mortgage AUM will grow between 15% to 20%.... |
| 138 | 51 | 858 | Parvez Mulla | 51.4% | ...as a percentage of our AUM, it is about 51.4%. I will just have to do the arithmetic.... |
| 139 | 51 | 859 | Parvez Mulla | 2% | ...If gold is growing at 2%, 3% higher than the other one, and that... |
| 140 | 51 | 859 | Parvez Mulla | 3% | ...If gold is growing at 2%, 3% higher than the other one, and that is... |
| 141 | 51 | 859 | Parvez Mulla | 50% | ...higher than the other one, and that is 50% of the book. So maybe it will... |
| 142 | 55 | 878 | Parvez Mulla | 7 lakhs | ...operate in a ticket size between 7 lakhs to 35 lakhs, as a small ticket LAP. The... |
| 143 | 55 | 878 | Parvez Mulla | 35 lakhs | ...ate in a ticket size between 7 lakhs to 35 lakhs, as a small ticket LAP. There could hav... |
| 144 | 55 | 879 | Parvez Mulla | 7 lakhs | ...en                    stressed at below 7 lakhs. The segment that we operate between 7... |
| 145 | 55 | 879 | Parvez Mulla | 7 lakhs | ...hs. The segment that we operate between 7 lakhs to 35 lakhs has not seen stress... |
| 146 | 55 | 879 | Parvez Mulla | 35 lakhs | ...ment that we operate between 7 lakhs to 35 lakhs has not seen stress... |
| 147 | 55 | 880 | Parvez Mulla | 35 lakhs | ...s medium ticket LAP, we operate between 35 lakhs                    to 3 crores. That ha... |
| 148 | 55 | 881 | Parvez Mulla | 3 crores | ...between 35 lakhs                    to 3 crores. That has also not seen stress. The sma... |
| 149 | 55 | 882 | Parvez Mulla | 16% | ...at a yield of                    about 16%. And the medium ticket LAP, we operate... |
| 150 | 55 | 882 | Parvez Mulla | 12% | ...ket LAP, we operate at a yield of about 12% to 12.5%.... |
| 151 | 55 | 882 | Parvez Mulla | 12.5% | ..., we operate at a yield of about 12% to 12.5%.... |
| 152 | 57 | 894 | Parvez Mulla | 50% | ...which I said at an entity level will be 50% of my gold book will grow at about... |
| 153 | 57 | 895 | Parvez Mulla | 25% | ...k will grow at about                    25% to 30%. And my LAP book, which comprise... |
| 154 | 57 | 895 | Parvez Mulla | 30% | ...grow at about                    25% to 30%. And my LAP book, which comprises of my... |
| 155 | 57 | 896 | Parvez Mulla | 15% | ...ket LAP                    will grow by 15% to 20%.... |
| 156 | 57 | 896 | Parvez Mulla | 20% | ...will grow by 15% to 20%.... |
| 157 | 59 | 922 | Parvez Mulla | 15% | ...s will                    grow at about 15% to 20%.... |
| 158 | 59 | 922 | Parvez Mulla | 20% | ...grow at about 15% to 20%.... |
| 159 | 62 | 934 | Parvez Mulla | 150 branches | ...ood question. Last year, we added about 150 branches.                    This year, we plan... |
| 160 | 62 | 935 | Parvez Mulla | 200 branches | ...This year, we plan to add 200 branches. Our guidance remains, we have not chan... |
| 161 | 62 | 936 | Parvez Mulla | 200 branches | ...We will continue to add 200 branches Q1, we identified the premises. We did... |
| 162 | 68 | 975 | Parvez Mulla | 300 bps | ...ly higher. And it could be about 200 to 300 bps higher                  on the entity l... |
| 163 | 76 | 1007 | Parvez Mulla | 18 states | ...n is concerned, we are present in about 18 states and so our penetration, our... |
| 164 | 76 | 1012 | Parvez Mulla | 150 branches | ...are definitely there. Last year, we put 150 branches. This year,                  we are put... |
| 165 | 76 | 1013 | Parvez Mulla | 200 branches | ...s year,                  we are putting 200 branches, and we'll continue to put more branche... |
| 166 | 79 | 1036 | Parvez Mulla | 51 crores | ...e write-off is somewhere close to about 51 crores and we request CVG                 to r... |
| 167 | 80 | 1042 | C.V. Ganesh | 1.87% | ...continued to be same as March, which is 1.87%.                   We wrote off a littl... |
| 168 | 80 | 1045 | C.V. Ganesh | 50 crores | ...We wrote off a little above 50 crores. which resulted in a 30-bps reduction i... |
| 169 | 80 | 1045 | C.V. Ganesh | 30-bps | ...le above 50 crores. which resulted in a 30-bps reduction in the GNPA. So that's... |
| 170 | 86 | 1074 | C.V. Ganesh | 15 years | ...e                 tenure of about 10 to 15 years. And the gold loan would have a month.... |
| 171 | 86 | 1076 | C.V. Ganesh | 300 crores | ...one about a little                 over 300 crores of gold loan DA, right and which doesn'... |
| 172 | 108 | 1174 | Parvez Mulla | 15% | ...ly. The mortgage growth has shown about 15%, Y-o-Y.                   And we contin... |

## 5. Forward-Commitment Phrases (43; lexicon: guidance / will continue / we will / remains the same / reaffirm / committed / sustain / continue to)

| # | Turn | Line | Speaker | Trigger | Sentence (truncated) |
|---|------|------|---------|---------|------------------------|
| 1 | 4 | 122 | Parvez Mulla | continue to | We continue to allocate capital to businesses that earn a strong and consistent return; to |
| 2 | 4 | 137 | Parvez Mulla | continue to | Cr, while gold tonnage remained stable, and we continue to maintain a prudent risk profile |
| 3 | 4 | 156 | Parvez Mulla | continue to | interest-due structure, and we continue to operate at LTVs below the regulatory limits. As |
| 4 | 5 | 339 | C. V. Ganesh | sustainability | sustainability of this number. |
| 5 | 5 | 365 | C. V. Ganesh | sustain | some investment opex increase - while attempting to sustain the ROA. |
| 6 | 5 | 378 | C. V. Ganesh | continue to | We are building the business for the long-run and while we continue to monitor and measure |
| 7 | 5 | 379 | C. V. Ganesh | we will | metric, we only see this as a re-affirmation in terms of the investments we will seek to c |
| 8 | 8 | 441 | Parvez Mulla | remains same | and NBFCs are concerned, it remains same. |
| 9 | 10 | 472 | Parvez Mulla | guidance | Parvez Mulla:   Digant, our guidance remains the same, which we have been giving for the p |
| 10 | 10 | 472 | Parvez Mulla | remains the same | Parvez Mulla:   Digant, our guidance remains the same, which we have been giving for the p |
| 11 | 10 | 488 | Parvez Mulla | guidance | LTV this year, even if the price remains flat. And if you've taken our guidance last year, |
| 12 | 12 | 505 | Parvez Mulla | will continue | was driving the LAP business. He's done a LAP business. He's done gold business. So he wil |
| 13 | 17 | 563 | Parvez Mulla | we will | said that we will continue to invest into these 2 segments and grow these 2 segments. |
| 14 | 17 | 563 | Parvez Mulla | continue to | said that we will continue to invest into these 2 segments and grow these 2 segments. |
| 15 | 17 | 566 | Parvez Mulla | guidance | The guidance that we have given for this year is that we will grow the entity at about 20% |
| 16 | 17 | 566 | Parvez Mulla | we will | The guidance that we have given for this year is that we will grow the entity at about 20% |
| 17 | 17 | 598 | Parvez Mulla | we will | market is playing. So, we will play it accordingly, but we will give your company the grow |
| 18 | 17 | 598 | Parvez Mulla | we will | market is playing. So, we will play it accordingly, but we will give your company the grow |
| 19 | 30 | 717 | CV Ganesh | we will | group. So we will watch it. |
| 20 | 33 | 735 | Parvez Mulla | guidance | Parvez Mulla:    Overall, Renish, the credit cost guidance remains same. At the start of t |
| 21 | 33 | 735 | Parvez Mulla | remains same | Parvez Mulla:    Overall, Renish, the credit cost guidance remains same. At the start of t |
| 22 | 33 | 736 | Parvez Mulla | guidance | credit cost guidance will be sub-1%. And as far as the mortgage GNPAs are concerned, they  |
| 23 | 33 | 738 | Parvez Mulla | guidance | how it will in Q2, the monsoon effect in Q2, Q3. So, we are well within the guidance. And  |
| 24 | 33 | 746 | Parvez Mulla | guidance | well. So the guidance remains. All our guidances, which we had given at the start of the y |
| 25 | 35 | 766 | Parvez Mulla | we will | at a particular yield of about 12%, 12.5%. That is coming under pressure. And gold, we wil |
| 26 | 35 | 770 | Parvez Mulla | we will | Q4 that we will hold the yields. Q2, it will be the operating dynamics, which will play, a |
| 27 | 42 | 807 | Parvez Mulla | we will | Parvez Mulla:   What we have guided, Rahul, for the year FY '27 start, I had guided that w |
| 28 | 42 | 809 | Parvez Mulla | we will | given an average ROA of about 2.4%. So we had guided that we will do average ROA much bett |
| 29 | 59 | 907 | Parvez Mulla | we will | and the small ticket LAP, we will look at the quarter two and quarter three. Alternatively |
| 30 | 59 | 911 | Parvez Mulla | We will | And as I have always said, growth is an outcome for us. We will look at the quality that i |
| 31 | 59 | 921 | Parvez Mulla | guidance | guidance that we'll grow both these segments together at an entity level. These two segmen |
| 32 | 62 | 935 | Parvez Mulla | guidance | This year, we plan to add 200 branches. Our guidance remains, we have not changed our guid |
| 33 | 62 | 935 | Parvez Mulla | guidance | This year, we plan to add 200 branches. Our guidance remains, we have not changed our guid |
| 34 | 62 | 936 | Parvez Mulla | We will | We will continue to add 200 branches Q1, we identified the premises. We did all the work,  |
| 35 | 62 | 936 | Parvez Mulla | continue to | We will continue to add 200 branches Q1, we identified the premises. We did all the work,  |
| 36 | 76 | 1008 | Parvez Mulla | We will | expansion is decent enough. We will continue with our extra penetration. That means if we  |
| 37 | 76 | 1013 | Parvez Mulla | continue to | we are putting 200 branches, and we'll continue to put more branches. We believe our distr |
| 38 | 76 | 1014 | Parvez Mulla | we will | capabilities and our branch expansion is very, very important to our growth strategy, and  |
| 39 | 76 | 1015 | Parvez Mulla | continue to | continue to do that, sir. |
| 40 | 108 | 1176 | Parvez Mulla | guidance | guidance, our credit cost guidance, our growth guidance remains the same. Quarter-on-quart |
| 41 | 108 | 1176 | Parvez Mulla | guidance | guidance, our credit cost guidance, our growth guidance remains the same. Quarter-on-quart |
| 42 | 108 | 1176 | Parvez Mulla | guidance | guidance, our credit cost guidance, our growth guidance remains the same. Quarter-on-quart |
| 43 | 108 | 1176 | Parvez Mulla | remains the same | guidance, our credit cost guidance, our growth guidance remains the same. Quarter-on-quart |

## 6. Hedge Phrases (53; lexicon: may / might / could / hope / expect* / believe* / watchful / unknown / calibrating / unsure / cautious / aberrations / don't know / not indicative / not comparable / watch it)

| # | Turn | Line | Speaker | Trigger | Sentence (truncated) |
|---|------|------|---------|---------|------------------------|
| 1 | 4 | 151 | Parvez Mulla | expect | This quarter there has been a regulatory transition for the gold lending industry, which I |
| 2 | 4 | 157 | Parvez Mulla | expected | repayment behaviour is unlikely to change immediately, reported overdue levels are expecte |
| 3 | 4 | 219 | Parvez Mulla | believe | is now in place, and we believe it positions us well for the quarters ahead. |
| 4 | 5 | 277 | C. V. Ganesh | cautious | •   That being said we remain cautious in terms of outlook, but optimistic in terms of rat |
| 5 | 5 | 283 | C. V. Ganesh | hope | •   We hope that most of these issues will get streamlined over the next few months and ou |
| 6 | 5 | 374 | C. V. Ganesh | expect | few quarters, we expect sourcing-related expenses and operating costs to increase correspo |
| 7 | 5 | 401 | C. V. Ganesh | believe | We believe that Q1 FY27 has set a strong foundation for the year. |
| 8 | 8 | 459 | Parvez Mulla | could | behaviours will also change. So, the NBFCs will also come out with innovative products, wh |
| 9 | 10 | 487 | Parvez Mulla | might | That is how the industry is operating. So what you might see is that companies will have a |
| 10 | 10 | 489 | Parvez Mulla | could | price was going up, we kept the LTV lower only when the price has been flat, there could b |
| 11 | 10 | 490 | Parvez Mulla | could | bit of LTV, which could move up. Also, if you noticed last quarter since January, the pric |
| 12 | 12 | 524 | Parvez Mulla | believe | And I think the unification of command will lead to a proposition, which we believe is a u |
| 13 | 12 | 526 | Parvez Mulla | believe | LAP. So that is a resource utilization, which we believe will be very strong. Plus the tar |
| 14 | 12 | 530 | Parvez Mulla | believe | Thirdly, our penetration into either of the products has been less. We believe that penetr |
| 15 | 12 | 531 | Parvez Mulla | believe | increase. And fourth, we believe that the distribution for both these products is very sim |
| 16 | 12 | 538 | Parvez Mulla | believe | strike rate. And that is where we believe strategically it makes sense. And it also falls  |
| 17 | 17 | 568 | Parvez Mulla | might | Within that, the medium ticket LAP or the small ticket LAP, one might grow faster than the |
| 18 | 17 | 599 | Parvez Mulla | expecting | are expecting for the year in the LAP segment and the gold segment. But we are watchful in |
| 19 | 17 | 599 | Parvez Mulla | watchful | are expecting for the year in the LAP segment and the gold segment. But we are watchful in |
| 20 | 19 | 614 | Parvez Mulla | could | Parvez Mulla:      Our regular credit cost has been around 0.7, so a little bit 10 basis p |
| 21 | 25 | 672 | Jagadeesh Rao | believe | lending like consumption and income-generating loan etc., (I believe, even the industry is |
| 22 | 30 | 705 | CV Ganesh | expect | or expect any increase in credit cost. It is just that we remain watchful of this new stru |
| 23 | 30 | 705 | CV Ganesh | watchful | or expect any increase in credit cost. It is just that we remain watchful of this new stru |
| 24 | 30 | 709 | CV Ganesh | unknown | but there is a provisioning nevertheless, so that is an unknown. As I said, we are into a  |
| 25 | 30 | 712 | CV Ganesh | calibrating | We are also calibrating and understanding how this works. Now clearly, the collateral is v |
| 26 | 30 | 713 | CV Ganesh | believe | There is no reason for any stress, we believe, in the asset book just because we miss our  |
| 27 | 30 | 714 | CV Ganesh | watchful | payment. And so we remain watchful. So, your hypothesis is correct. The only thing which m |
| 28 | 30 | 714 | CV Ganesh | may | payment. And so we remain watchful. So, your hypothesis is correct. The only thing which m |
| 29 | 30 | 716 | CV Ganesh | believe | happens to us, we believe will be on a relative basis, similar to what happens to the rest |
| 30 | 30 | 717 | CV Ganesh | watch it | group. So we will watch it. |
| 31 | 33 | 737 | Parvez Mulla | don't know | tracking well. We're not seeing anything on the West Asia crisis hitting us as of now. I d |
| 32 | 40 | 791 | Parvez Mulla | expected | is similar or it is going in the expected trend. So we are not seeing any adverse movement |
| 33 | 42 | 813 | Parvez Mulla | might | of credit cost and cost to average assets. These are the two levers, which will play out.  |
| 34 | 42 | 814 | Parvez Mulla | might | not play out quarter-to-quarter. There might be aberrations within the quarter. But on a y |
| 35 | 42 | 814 | Parvez Mulla | aberrations | not play out quarter-to-quarter. There might be aberrations within the quarter. But on a y |
| 36 | 42 | 815 | Parvez Mulla | could | that's how you will see it play out. So it could be a combination of 10 bps here and 20 bp |
| 37 | 45 | 837 | Parvez Mulla | expecting | Parvez Mulla:      So if the price doesn't move, then we are expecting the gold AUM on a b |
| 38 | 45 | 838 | Parvez Mulla | expecting | AUM should grow by about 25% to 30%. And at an entity level, we are expecting to grow abou |
| 39 | 55 | 878 | Parvez Mulla | could | operate in a ticket size between 7 lakhs to 35 lakhs, as a small ticket LAP. There could h |
| 40 | 59 | 907 | Parvez Mulla | could | and the small ticket LAP, we will look at the quarter two and quarter three. Alternatively |
| 41 | 59 | 908 | Parvez Mulla | could | grow either segment. I mean, it could depend on the market. |
| 42 | 59 | 912 | Parvez Mulla | could | and decide the growth where we want to push, which particular distribution. So it could be |
| 43 | 59 | 917 | Parvez Mulla | could | So it could be a combination, and it could be also in the vernacular markets that we opera |
| 44 | 59 | 917 | Parvez Mulla | could | So it could be a combination, and it could be also in the vernacular markets that we opera |
| 45 | 62 | 941 | Parvez Mulla | could | getting into. And those openings could not be done. That is why we couldn't disclose the n |
| 46 | 68 | 975 | Parvez Mulla | could | for because of the gold piece is looking slightly higher. And it could be about 200 to 300 |
| 47 | 69 | 980 | CV Ganesh | may | 30 plus may not be comparable because of the new structure in which gold loans will operat |
| 48 | 76 | 1009 | Parvez Mulla | might | entered one particular territory with one or two branches, we might add more branches ther |
| 49 | 76 | 1010 | Parvez Mulla | might | is the territories of Orissa, which is a wide space for us. So, we might expand there this |
| 50 | 76 | 1011 | Parvez Mulla | could | there are other territories in the north where we could expand within the territory where  |
| 51 | 76 | 1013 | Parvez Mulla | believe | we are putting 200 branches, and we'll continue to put more branches. We believe our distr |
| 52 | 84 | 1065 | C.V. Ganesh | unsure | C.V. Ganesh:    Just 1 second. I'm a little unsure, you're looking at the LODR, is it? |
| 53 | 86 | 1074 | C.V. Ganesh | may | tenure of about 10 to 15 years. And the gold loan would have a month. So it may not be ind |
## 7. Analyst-Cited Numbers (supplementary — not "spoken by management" but load-bearing for Role 5 arithmetic cross-check against the filing baseline)

| # | Analyst | Turn | Line | Figure cited | Context |
|---|---------|------|------|--------------|---------|
| 1 | Pawan Kumar | 78 | 1027 | 40 crores | provisions "gone down by 40 crores on GS 3 assets" |
| 2 | Pawan Kumar | 78 | 1028 | 75 crores | alleged write-off quantum — management corrects this to ~51 crores at turn 79 (line 1036) |
| 3 | Pawan Kumar | 78 | 1029 | 585 crores | fair value loss on loans in Other Comprehensive Income |
| 4 | Pawan Kumar | 78 | 1030 | INR589 crores | LAP assignment (DA) transacted |
| 5 | Pawan Kumar | 78 | 1031 | 12 to 15 crores | loss on the INR589cr LAP assignment |
| 6 | Pawan Kumar | 83 | 1069-1070 | 489 crores | transferred-out assignment amount per quarterly financial results, page 7 |
| 7 | Pawan Kumar | 83 | 1070 | 37 months | outstanding maturity disclosed for the assignment transfer |

DATA_DISCREPANCY flag: Pawan Kumar's cited write-off of "75 crores" (turn 78, line 1028) is explicitly corrected by Parvez Mulla to "somewhere close to about 51 crores" (turn 79, line 1036), and by C.V. Ganesh to "a little above 50 crores" (turn 80, line 1045). Three different write-off figures (75 / 51 / ~50 crores) appear across three consecutive turns for the same disclosure — carry to A3/A4 for reconciliation against the filed financial statements.

## 8. Zero / Nil / Dash-Valued Standing Items

Not applicable to this document. This A1 extract is a concall transcript (management commentary and Q&A) with no embedded financial statement line-item table; there is no standing-line-item grid to sweep for ZERO_STANDING rows. (If the investor presentation or results filing for this quarter is enumerated separately, run the ZERO_STANDING sweep there.)

## 9. Notes for A3 / A4 Reconciliation

- SPEAKER_LABEL_VARIANT: CFO C.V. Ganesh is transcribed three different ways across his 10 turns — "C. V. Ganesh" (turn 5), "CV Ganesh" (turns 30, 69), "C.V. Ganesh" (turns 80, 82, 84, 86, 88, 102, 106). No substantive risk, but a QC signal on transcript consistency.
- NAME_INCONSISTENCY: analyst "Dinesh Loni" (turn 75) is addressed as "Mr. Dinesh Lohani" by the Moderator at turn 77 (line 1023).
- UNATTRIBUTED_SPEAKER: turn 92 (line 1104) attributes "Yes." to generic "Management" rather than a named individual — likely Parvez Mulla or C.V. Ganesh, but not identifiable from the transcript.
- SILENT_ATTENDEE (3): Shardul Kadam (CTO), K. Suresh (CBO Medium Ticket LAP), Vikram Rathi (CRO) are listed on the management roster (page 2) but have zero speaking turns across the entire call.
- REPEAT_QUESTION clusters (3): credit cost trend; asset-quality-stress pockets; gold AUM growth guidance — see Section 3 notes.
- DATA_DISCREPANCY: write-off quantum stated three ways (75cr / 51cr / ~50cr) across turns 78-80 — see Section 7.
- Board meeting / signature timestamp: cover letter (lines 1-50) is digitally signed by Parthasarathy Iyengar, Company Secretary & Compliance Officer, dated 2026-07-21 17:25:41 +05'30 — this is the NSE/BSE submission cover letter for the transcript, not a results-announcement signature block; no board-meeting start/end times are disclosed in this document (concall transcript only, not the Board Outcome letter).

---

```yaml
stage: A2-enumerator
company: "FEDFINA"
quarter: "Q1FY27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "runs/fedfina-q1fy27/work/ledger_concall_fedfina_q1fy27.md"
counts:
  participants: 21
  turns: 109
  questions: 36
  mgmt_numbers: 172
  forward_commitment_phrases: 43
  hedge_phrases: 53
  analyst_cited_numbers: 7
flags_raised: [SILENT_ATTENDEE, REPEAT_QUESTION, NAME_INCONSISTENCY, UNATTRIBUTED_SPEAKER, SPEAKER_LABEL_VARIANT, DATA_DISCREPANCY]
gate_a2: pass
mismatch_note: ""
```
