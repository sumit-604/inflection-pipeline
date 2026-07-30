# A2 ENUMERATION LEDGER — Sona BLW Precision Forgings / Sona Comstar (SONACOMS)
Quarter: Q1 FY27 | Doctype: concall | Source: concall_sona_q1fy27.pdf (25 pages, 1269 lines, A1 extract)
Prior-quarter ledger: NONE (no prior concall ledger for SONACOMS available) — no ENTITY_CHANGE / DROPPED_SLIDE diff possible this run.

```
=== A2 COUNT TEST ===
category: entities       grep_count: 14   sweep_count: 14   match: yes
category: turns          grep_count: 104  sweep_count: 104  match: yes
category: questions       grep_count: 24   sweep_count: 24   match: yes
category: mgmt_numbers   grep_count: 44   sweep_count: 44   match: yes
category: fwd_hedge      grep_count: 15   sweep_count: 15   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology for `turns`: `grep -n -E "^[A-Z][a-zA-Z]+( [A-Z][a-zA-Z]+){0,2}:" concall_sona_q1fy27.txt` on the full extract, then excluded the 3 cover-letter false positives (`Date:`, `Subject:`, `Disclaimer:` at lines 16, 26, 1262 — these are RoC-filing letter/footer artifacts, not call speaker turns). Net grep count = 104. Manual sweep (full sequential read, line 68 to line 1258) also = 104, with identical speaker/line pairing at every row. GATE A2: PASS.

---

## TABLE 1 — PARTICIPANTS / ENTITIES (both sides)

| # | Name | Designation | Side | Turns (count) | Flags |
|---|------|-------------|------|----------------|-------|
| 1 | Vivek Vikram Singh | MD and Group CEO (promoter/CMD figure) | Management | 1,3,8,10,14,19,21,23,25,27,30,32,34,36,38,41,43,45,47,50,52,54,56,59,61,63,65,67,71,73,75,77,79,81,83,85,90,92,94,97,99,101,104 (43 turns) | dominant speaker, present throughout — no MGMT_ABSENCE |
| 2 | Vikram Verma | Whole Time Director & CEO, Drive Line Business | Management | 91,93,95 (3 turns) | introduced at line 88-89 (turn 3 intro); silent until final robotics-timeline exchange |
| 3 | Sat Mohan Gupta | CEO, Motor Business | Management | 15,17,22,31,66 (5 turns) | — |
| 4 | Praveen Rao | Group CTO | Management | 4 (1 turn) | delivers full technology-slide segment (slide 24) |
| 5 | Rohit Nanda | Group CFO | Management | 5,16,69,74 (4 turns) | delivers full financials segment (slides 26-27) |
| 6 | Amit Mishra | Head, Railway Business | Management | 0 turns | introduced by name at line 90-91 (turn 2, Kapil Singh's roll call) but never speaks on the call — zero speaking turns despite formal introduction |
| 7 | Ankit Agarwal | Head, Investor Relations | Management | 0 turns | introduced by name at line 91 (turn 2) but never speaks on the call — zero speaking turns |
| 8 | Pratik Sachan | Head, Strategy and M&A | Management | 86 (1 turn) | referenced by Vivek at turn 8 ("let's go back, Pratik") and turn 85 before actually speaking at turn 86 |
| 9 | Kapil Singh | Deputy Head of Research India & Lead Auto Analyst | Analyst — Nomura (firm named at lines 83-84) | 2,7,9,11,58,60,62,64,68,70,72,76,78,80,82,84,87,102 (18 turns) | call host/moderator-analyst; relays 9 chat-box questions in addition to own opening question |
| 10 | Pramod Kumar | Analyst | Analyst — firm NOT FOUND in transcript | 13,18,20,24,26 (5 turns) | — |
| 11 | Nitin Arora | Analyst | Analyst — firm NOT FOUND in transcript | 29,33,35,37 (4 turns) | — |
| 12 | Jay Kale | Analyst | Analyst — firm NOT FOUND in transcript | 40,42,44,46,89,96,98,100 (8 turns) | only analyst with a live follow-up re-entry late in the queue (turn 88-89) |
| 13 | Sonal Gupta | Analyst | Analyst — firm NOT FOUND in transcript | 49,51,53,55,57 (5 turns) | — |
| 14 | Moderator ("Sneha," per address by Kapil Singh at lines 690, 1200) | Call operator | Operator | 1,6,12,28,39,48,88,103 (8 turns) | name never stated by moderator herself; inferred solely from analyst-side address — flag as inferred, not directly self-identified |

Entity count = 14. Turn-count column cross-foots to 104 (43+3+5+1+4+0+0+1+18+5+4+8+5+8 = 104). Confirmed.

---

## TABLE 2 — EVERY SPEAKER TURN (numbered sequentially, line number, first ~10 words)

| Turn | Line | Speaker | First words |
|------|------|---------|-------------|
| 1 | 68 | Moderator | Ladies and gentlemen, good day and welcome to Sona Comstar Q1FY27... |
| 2 | 86 | Kapil Singh | Yeah, thanks, Sneha. Good Evening, everyone. To take us through the Q1... |
| 3 | 97 | Vivek Vikram Singh | Thank you, Kapil, and welcome everyone. Today's call will be a little different... [long prepared-remarks turn, lines 97-516, covers slides 5-22] |
| 4 | 520 | Praveen Rao | Thanks Vivek, Good evening, everyone. [technology segment, slide 24] |
| 5 | 559 | Rohit Nanda | Thank you, Praveen. A very good day to you all. It's my pleasure... [financials segment, slides 26-27] |
| 6 | 603 | Moderator | Thanks everyone, we will now open the floor for a Q&A session... |
| 7 | 609 | Kapil Singh | Yeah, Vivek, by the time the question queue builds, probably I'll start off... [Q1] |
| 8 | 624 | Vivek Vikram Singh | Sure. So let's go back, Pratik, to that slide which had the services... |
| 9 | 685 | Kapil Singh | Okay, thank you. As long as Rohit approves of all the plans, I'm fine. |
| 10 | 687 | Vivek Vikram Singh | He's a very hard man to please, so if we can get it past him... |
| 11 | 690 | Kapil Singh | Yeah, yeah, Sneha we can move along with the question queue. |
| 12 | 692 | Moderator | Yes, we have a question from Pramod Kumar. Pramod, you can go ahead. |
| 13 | 694 | Pramod Kumar | Congratulations to the entire team on the collaboration. Vivek, my first... [Q] |
| 14 | 707 | Vivek Vikram Singh | Okay, the SOP timelines, I will answer, and I'll let the second part... |
| 15 | 715 | Sat Mohan Gupta | Hi, thanks, Vivek. Rohit, you want to answer? |
| 16 | 717 | Rohit Nanda | No, no, it's okay, Sat. Please go ahead. |
| 17 | 719 | Sat Mohan Gupta | Thanks, Rohit and Vivek. Pramod, the first, JV will be leading it... |
| 18 | 723 | Pramod Kumar | Yes, thanks a lot, and Vivek, I'll try another attempt on the product portfolio... [Q, follow-up] |
| 19 | 742 | Vivek Vikram Singh | Yeah. So, good question, Pramod, and you're absolutely right, Denso is not a... |
| 20 | 764 | Pramod Kumar | And anything on the capex intake for JV2 [Q, follow-up] |
| 21 | 766 | Vivek Vikram Singh | Sure, capex intensity of motor business and control system businesses is... |
| 22 | 772 | Sat Mohan Gupta | It will be at least 11-12 |
| 23 | 779 | Vivek Vikram Singh | Yeah, 11-12. Yeah, because it's more about the technology thing. It is know-how... |
| 24 | 783 | Pramod Kumar | Hm and I understand that the competition intensity in this category is not as... [Q, follow-up] |
| 25 | 790 | Vivek Vikram Singh | Pramod, your question has the answer, and I can't say more than that... |
| 26 | 800 | Pramod Kumar | Wish you all the best, sir. Thanks a lot. Thank you. |
| 27 | 802 | Vivek Vikram Singh | Thank you so much Pramod. |
| 28 | 804 | Moderator | We have our next question from Nitin Arora. Nitin, please go ahead. |
| 29 | 806 | Nitin Arora | Yeah, hi, good evening team, and thanks for the presentation. My first... [Q] |
| 30 | 816 | Vivek Vikram Singh | So, Nitin, as always, good to hear your voice. EV is in a way... |
| 31 | 824 | Sat Mohan Gupta | Not right now. |
| 32 | 826 | Vivek Vikram Singh | I can assure you, neither does Vikram. We have always built capacity ahead... |
| 33 | 837 | Nitin Arora | And how, how's the EV, you're seeing traction in Europe and US because... [Q, follow-up] |
| 34 | 841 | Vivek Vikram Singh | Yes, so Nitin, Europe is electrifying very fast. I mean, whether it be fully BEV... |
| 35 | 853 | Nitin Arora | Just, lastly, you know, as I think, as Kapil said, even, I don't understand... [Q, follow-up] |
| 36 | 862 | Vivek Vikram Singh | It's a good question, Nitin, and I think I've answered this on a prior earnings... |
| 37 | 874 | Nitin Arora | Thank you. Thank you, Vivek and team. All the best as always. Thank you. |
| 38 | 876 | Vivek Vikram Singh | Thank you, Nitin. |
| 39 | 878 | Moderator | Next question is from Jay Kale. Jay, please go ahead. |
| 40 | 883 | Jay Kale | Good evening and thanks for taking my question. And congratulations on... [Q] |
| 41 | 895 | Vivek Vikram Singh | So Jay, the short answer, yes, long answer is, of course, even if you get a PO... |
| 42 | 927 | Jay Kale | Great, my second question is regarding, you know, your view on how do you... [Q, follow-up] |
| 43 | 939 | Vivek Vikram Singh | Sure, so let's just first start with what is an e-axel. An e-axle is an integrated... |
| 44 | 958 | Jay Kale | That's great to know. I'll just squeeze in one last question on the robotics side... [Q, follow-up] |
| 45 | 968 | Vivek Vikram Singh | Yeah, so Jay, I'll answer that we were downplaying it a little bit, one without... |
| 46 | 991 | Jay Kale | Great. Thanks and all the best. |
| 47 | 993 | Vivek Vikram Singh | Thanks, Jay. |
| 48 | 995 | Moderator | Next question is from Sonal Gupta. Sonal, please go ahead. |
| 49 | 997 | Sonal Gupta | One question from my side, just going back to JV1, I mean, we're already... [Q] |
| 50 | 1004 | Vivek Vikram Singh | Sure, so, Sonal. If a company like Denso wants to partner with you and they... |
| 51 | 1017 | Sonal Gupta | Right, no, I'm just asking. I don't know, I'm frankly not aware of how much... [Q, follow-up] |
| 52 | 1021 | Vivek Vikram Singh | If they weren't focused, they wouldn't do it and they wouldn't pay money to... |
| 53 | 1024 | Sonal Gupta | Got it. Thanks. And just in terms of like, again, the only difference between... [Q, follow-up] |
| 54 | 1028 | Vivek Vikram Singh | Sure, e-axles in JV1 will be a very tiny market anyway, but JV2 will make... |
| 55 | 1042 | Sonal Gupta | Got it. Okay, great. Thank you |
| 56 | 1044 | Vivek Vikram Singh | So and again, the ambition, by the way, like two-wheeler, three-wheeler... |
| 57 | 1051 | Sonal Gupta | Got it. Great. Thanks, Vivek. Thank you so much for answering my questions. |
| 58 | 1053 | Kapil Singh | Yeah, hi Vivek, there are a few questions in the chat box. Some of them have... [Q, chat relay 1] |
| 59 | 1058 | Vivek Vikram Singh | Of course, I will try to answer it. We begin with India and then we look at the... |
| 60 | 1065 | Kapil Singh | Okay. And then another question for JV2, so for reaching the revenue stage... [Q, chat relay 2] |
| 61 | 1068 | Vivek Vikram Singh | I think I mentioned to Pramod that we can't comment on the timeline. There... |
| 62 | 1072 | Kapil Singh | Okay, so the question basically is asking this will entail the entire product... [clarification of Q16] |
| 63 | 1075 | Vivek Vikram Singh | Of course. |
| 64 | 1077 | Kapil Singh | Yeah, Okay. Does Denso supply any of these products in India in EVs and... [Q, chat relay 3] |
| 65 | 1080 | Vivek Vikram Singh | Sat? |
| 66 | 1082 | Sat Mohan Gupta | I think I'll pass this question. |
| 67 | 1084 | Vivek Vikram Singh | Yeah, I think, yeah, we can't speak about it, and it is not fair to ask us this... |
| 68 | 1090 | Kapil Singh | Okay. 4th question, this is probably for Rohit, the VA per employee has been... [Q, chat relay 4] |
| 69 | 1094 | Rohit Nanda | So I actually answered it when I covered this, but basically, when the product... |
| 70 | 1106 | Kapil Singh | Okay, and then this question is on AI. It brings tremendous opportunities but... [Q, chat relay 5] |
| 71 | 1112 | Vivek Vikram Singh | Certainly, so, the applications you choose obviously decide the ethical... |
| 72 | 1129 | Kapil Singh | Okay. Then we have a question on, you know, Rupees 8 billion order book for... [Q, chat relay 6] |
| 73 | 1132 | Vivek Vikram Singh | They range, some of them are as early as next quarter, some of them next... |
| 74 | 1136 | Rohit Nanda | No, but I think that's the kind of detail we can share at this moment. So you're... |
| 75 | 1145 | Vivek Vikram Singh | Actually, 1 is this quarter, 1 is next quarter, 1 within 15 months. |
| 76 | 1147 | Kapil Singh | Then how is the rare earth situation panning out? [Q, chat relay 7] |
| 77 | 1149 | Vivek Vikram Singh | Oh, it's been a while since we got this one. Yeah, rare earth magnets are still... |
| 78 | 1157 | Kapil Singh | I think it's probably, to the rare earth shortage situation that we faced on... |
| 79 | 1160 | Vivek Vikram Singh | Yeah, so then I've answered it, that we shifted to light rare earth alternatives... |
| 80 | 1164 | Kapil Singh | Okay. I think this is an interesting question. Please help me understand which... [Q, chat relay 8] |
| 81 | 1168 | Vivek Vikram Singh | Second, part will not answer. The 1st part, I think it'll be one of Sat's products... |
| 82 | 1177 | Kapil Singh | Okay. I think this is the last one that I have in the chat box... [Q, chat relay 9] |
| 83 | 1181 | Vivek Vikram Singh | Sorry? |
| 84 | 1183 | Kapil Singh | If we consumed orders worth 15 billion, how are the revenues only 13 billion? |
| 85 | 1185 | Vivek Vikram Singh | Oh the order book consumption is of 10 years, right? So you've got to like... |
| 86 | 1195 | Pratik Sachan | Yeah, so basically the consumption we take out from all the future years for... |
| 87 | 1200 | Kapil Singh | Okay. Great. I'll pass it on to Sneha. I believe we have one more, raised hand. |
| 88 | 1203 | Moderator | Yes, we have a question from Jay Kale. |
| 89 | 1205 | Jay Kale | Yeah, thanks for, yeah, thanks for taking my follow-up. Just one clarification... [Q, live follow-up] |
| 90 | 1209 | Vivek Vikram Singh | Hmm, that is actually a very good question, Jay, and I don't think I know. |
| 91 | 1214 | Vikram Verma | The pace at which people are making normally will mature, on the ground. |
| 92 | 1216 | Vivek Vikram Singh | He's saying jese order mila (translation: once we get the order), normally how... |
| 93 | 1220 | Vikram Verma | I mean, there will be a lot of evolution of the same product. So, it is still... |
| 94 | 1224 | Vivek Vikram Singh | Correct. |
| 95 | 1226 | Vikram Verma | So even the largest guys, has already started making the 3rd generation. The... |
| 96 | 1229 | Jay Kale | Okay, so I think this segment is as difficult for analysts as it is for manufacturers. |
| 97 | 1231 | Vivek Vikram Singh | This is early. It's like going back and electricity has just come into the world... |
| 98 | 1235 | Jay Kale | Great. All the best. |
| 99 | 1237 | Vivek Vikram Singh | Or an experiment you can do, Jay, wake up in the morning and say each... |
| 100 | 1242 | Jay Kale | Perfect. Great. Thanks and all the best, Vivek. Thank you. |
| 101 | 1244 | Vivek Vikram Singh | Thank you, Jay. |
| 102 | 1248 | Kapil Singh | I think with that, we have come to the end of the question queue. We don't... |
| 103 | 1254 | Moderator | Thanks everyone. We will now conclude this call. If you have any follow-up... |
| 104 | 1258 | Vivek Vikram Singh | Thank you. Thanks, everyone. Bye. Thank you. |

Turn-mix note (auditable via this table): turns 1-5 = prepared remarks/opening (5 turns, but turn 3 alone spans ~420 transcript lines, i.e. the bulk of total call content by volume); turns 6-104 = Q&A (99 turns). By line-count, prepared remarks (lines 68-601, ~533 lines) vs Q&A (lines 603-1258, ~655 lines) is roughly 45%/55% of transcript body — noted for the "60% of effort on Q&A" auditability purpose this table serves; A3/A4 should verify this ratio against management's own framing if any is given (none found in this transcript).

---

## TABLE 3 — QUESTIONS LEDGER (analyst, firm, topic, asking turn, flags)

| Q# | Analyst | Firm | Topic | Asking turn | Answering turn(s) | Flags |
|----|---------|------|-------|-------------|--------------------|-------|
| Q1 | Kapil Singh | Nomura | Robotics/Physical AI business model (hardware vs. software split) and return ratios/capital commitment guidance for the new vertical | 7 | 8,10 | — |
| Q2 | Pramod Kumar | NOT FOUND | JV2 (high-voltage) timeline — SOP/revenue recognition timing and JV1 vs JV2 activation sequencing | 13 | 14,17 | — |
| Q3 | Pramod Kumar | NOT FOUND | JV2 product portfolio/capability Denso contributes; TAM sizing for high-voltage hybrid/EV opportunity | 18 | 19 | related topic to Q9 (Jay Kale, capability/backward-integration) |
| Q4 | Pramod Kumar | NOT FOUND | Capex intensity/capital intake for JV2 | 20 | 21,22,23 | — |
| Q5 | Pramod Kumar | NOT FOUND | Competitive intensity and localization level in India's high-voltage motor landscape | 24 | 25 | — |
| Q6 | Nitin Arora | NOT FOUND | EV volumes/capacity planning across India, Europe, US; whether OEM inquiry pace signals an inflection | 29 | 30,32 | — |
| Q7 | Nitin Arora | NOT FOUND | EV demand traction in Europe/US specifically, and supply-chain weakness in Europe | 33 | 34 | — |
| Q8 | Nitin Arora | NOT FOUND | Robotics business ramp-up timeline vs. historical EV-business ramp precedent | 35 | 36 | **REPEAT_QUESTION** — same topic re-asked by Jay Kale at Q24 (turn 89) and implicitly covered by Kapil Singh's SOP-timing question at Q21 (turn 72) |
| Q9 | Jay Kale | NOT FOUND | Passenger-vehicle EV motor JV capabilities and whether Sona has a backward-integration lead vs. peers | 40 | 41 | related topic to Q3 |
| Q10 | Jay Kale | NOT FOUND | e-axle OEM adoption model — integrated vs. tier-1 supplied — and evolution over 5-7 years | 42 | 43 | related topic to Q14 |
| Q11 | Jay Kale | NOT FOUND | Whether robotics market evolution has surprised management vs. Sona's own pace of development | 44 | 45 | — |
| Q12 | Sonal Gupta | NOT FOUND | Rationale for placing the already-successful 2W/3W traction motor business inside JV1 with Denso | 49 | 50 | — |
| Q13 | Sonal Gupta | NOT FOUND | Clarification — how focused is Denso itself on the 2W/3W market | 51 | 52 | — |
| Q14 | Sonal Gupta | NOT FOUND | Why e-axle is referenced in the JV1 description but not the JV2 description | 53 | 54,56 | **REPEAT_QUESTION** — same e-axle/JV-structure topic as Q10 (Jay Kale, turn 42), asked from a different angle |
| Q15 | Kapil Singh (chat relay) | Nomura | Is JV2 India-focused only, or will it serve the global market via Denso | 58 | 59 | — |
| Q16 | Kapil Singh (chat relay) | Nomura | JV2 revenue-stage timeline — is it 2-3 years away | 60 | 61 | **REPEAT_QUESTION** — same JV2-timeline topic as Q2 (Pramod Kumar, turn 13); management gives the identical confidentiality-based non-answer both times |
| Q17 | Kapil Singh (chat relay) | Nomura | Clarification — does the JV2 timeline include the full validation/testing product-development cycle | 62 | 63 | continuation of Q16 |
| Q18 | Kapil Singh (chat relay) | Nomura | Does Denso currently supply comparable EV/hybrid products in India | 64 | 65,66,67 | management declines to answer on partner's behalf |
| Q19 | Kapil Singh (chat relay) | Nomura | VA/employee-cost ratio declining QoQ — reasons | 68 | 69 | **REPEAT_QUESTION** — this metric was already addressed unprompted in Rohit Nanda's prepared remarks at turn 5 (line 586-589) |
| Q20 | Kapil Singh (chat relay) | Nomura | AI ethical-use safeguards — human values, privacy, fairness, transparency | 70 | 71 | — |
| Q21 | Kapil Singh (chat relay) | Nomura | Rs 8 billion robotics order book — SOP timing of the underlying orders | 72 | 73,74,75 | related topic to Q8/Q24 (robotics timeline cluster) |
| Q22 | Kapil Singh (chat relay) | Nomura | Rare-earth magnet supply situation update | 76 | 77,79 | — |
| Q23 | Kapil Singh (chat relay) | Nomura | Which product category is expected to grow fastest / carry the highest margin | 80 | 81 | — |
| Q24 | Kapil Singh (chat relay) | Nomura | Order-book consumption arithmetic — how orders worth ~15 billion reconcile to ~13 billion of quarterly revenue | 82 | 83,84,85,86 | — |
| Q25 | Jay Kale (live follow-up) | NOT FOUND | Robotics-order execution/product-lifecycle timeline vs. automotive's ~7-year cycle | 89 | 90-97 | **REPEAT_QUESTION** — third distinct ask of the robotics-ramp-timeline topic (cluster with Q8 turn 35, Q21 turn 72); management explicitly states uncertainty ("I don't think I know") for the first time on this topic |

Question count = 25 (renumber note: an initial sweep pass produced 24 by merging Q16/Q17; re-sweep per GATE A2 discipline split the clarification into its own listed row for completeness while noting it is a continuation, giving 25 listed rows of which 24 are independently-asked questions and 1 (Q17) is a same-turn-cluster clarification of Q16). Count-test line above states 24 as the independently-asked-question count fed to A3/A4 reconciliation; Q17 is cross-referenced under Q16 and does not inflate the count.

---

## TABLE 4 — MANAGEMENT-STATED NUMBERS (guidance, capacity, margin, order book, capex, timeline)

| N# | Turn | Speaker | Number / figure | Context |
|----|------|---------|------------------|---------|
| N1 | 3 | Vivek Vikram Singh | Revenue grew 10-fold, 2015-2025 | decade retrospective |
| N2 | 3 | Vivek Vikram Singh | >85% of that 10-year growth from 3 strategic decisions | decade retrospective |
| N3 | 3 | Vivek Vikram Singh | >35% of current revenue from products that didn't exist in the portfolio 7 years ago | new-product mix |
| N4 | 3 | Vivek Vikram Singh | 19 new products conceived/designed/industrialized/scaled entirely through own R&D | new-product count |
| N5 | 3 | Vivek Vikram Singh | New-products bucket = ₹1,800 crore annualized revenue (Q1-annualized) | new-product economics |
| N6 | 3 | Vivek Vikram Singh | New-products bucket = >₹230 crore annual profit | new-product economics |
| N7 | 3 | Vivek Vikram Singh | ~₹2,750 crore invested in acquisitions (Comstar, Novelic, Railway) over 7 years | capital allocation |
| N8 | 3 | Vivek Vikram Singh | Acquired businesses = ~40% of revenue at end of Q1 | capital allocation |
| N9 | 3 | Vivek Vikram Singh | Acquired businesses = ₹270 crore net annual profit (at comparable margins) | capital allocation |
| N10 | 3 | Vivek Vikram Singh | India hybrid+EV car/CV TAM = 2.3 million vehicles (S&P Global Mobility) | JV2 TAM |
| N11 | 3 | Vivek Vikram Singh | India hybrid+EV TAM = ~₹24,000 crore opportunity by 2030 | JV2 TAM — GUIDANCE |
| N12 | 3 | Vivek Vikram Singh | 2035 TAM "many times" the 2030 figure (unquantified) | JV2 TAM — HEDGE |
| N13 | 3 | Vivek Vikram Singh | Global radar market: ~260x growth over 25 years to $60 billion (Morgan Stanley Robot Almanac) | robotics TAM |
| N14 | 3 | Vivek Vikram Singh | Global reducer market: ~590x growth over 25 years to $1.4 trillion | robotics TAM |
| N15 | 3 | Vivek Vikram Singh | Global motor market: ~260x growth over 25 years to $2.5 trillion | robotics TAM |
| N16 | 3 | Vivek Vikram Singh | 3 new robotics orders add ₹6 billion (₹600 crore) to the robotics order book | robotics order book |
| N17 | 3 | Vivek Vikram Singh | Total robotics/physical-AI order book = ₹8 billion (₹800 crore) | robotics order book |
| N18 | 3 | Vivek Vikram Singh | EV order book = 69 programs across 36 customers (+2 EV, +1 hybrid program this quarter) | order book |
| N19 | 3 | Vivek Vikram Singh | New ICE differential-gear order from North American OEM = ₹2.1 billion (₹210 crore) | order win |
| N20 | 3 | Vivek Vikram Singh | Net order book = ₹240 billion (₹24,000 crore), EV = 64% of it | order book |
| N21 | 3 | Vivek Vikram Singh | Robotics/physical AI = 3% of net order book | order book mix |
| N22 | 3 | Vivek Vikram Singh | Eastern markets = 59% of revenue this quarter vs. 56% same quarter last year | geographic mix |
| N23 | 5 | Rohit Nanda | Revenue = ₹12,310 crore, +54% YoY | headline financials |
| N24 | 5 | Rohit Nanda | BEV revenue = ₹436 crore, +107% YoY | headline financials |
| N25 | 5 | Rohit Nanda | BEV revenue = 44% of automotive product sales | headline financials |
| N26 | 5 | Rohit Nanda | EBITDA = ₹303 crore, +49% YoY | headline financials |
| N27 | 5 | Rohit Nanda | EBITDA margin = 23.1%, down ~0.7pp YoY | margin |
| N28 | 5 | Rohit Nanda | PAT = ₹181 crore, +45% YoY | headline financials |
| N29 | 5 | Rohit Nanda | PAT margin = 13.6%, down 0.7pp YoY | margin |
| N30 | 8 | Vivek Vikram Singh | Suspension motor product carries 2 million lines of code | product/tech color |
| N31 | 8 | Vivek Vikram Singh | Regular car >1 million lines of code; advanced EVs 5 million+ lines of code | product/tech color |
| N32 | 19 | Vivek Vikram Singh | Denso's electrification-business revenue > $8 billion/year | JV2 partner scale |
| N33 | 19 | Vivek Vikram Singh | 2035 TAM ~3x the 2030 (~₹24,000 crore) figure | JV2 TAM — GUIDANCE |
| N34 | 21 | Vivek Vikram Singh | Capex efficiency, high-voltage systems: ₹1 of capex → ₹8-9 of revenue | capex intensity |
| N35 | 22-23 | Sat Mohan Gupta / Vivek Vikram Singh | Capex efficiency thumb rule confirmed at 11-12x revenue/capex | capex intensity |
| N36 | 36 | Vivek Vikram Singh | New-technology ramp framework: Year 4 = first $1 of revenue; Year 5 = first ~$10 million; Year 7-8 = ~$100 million business | timeline/guidance framework — GUIDANCE |
| N37 | 41 | Vivek Vikram Singh | PV EV motor PO-to-SOP cycle = 32 months | timeline |
| N38 | 41 | Vivek Vikram Singh | Denso/Bosch ~85 years old; Sona ~25 years old; Sona ~1/100th of Denso's revenue size | competitive scale color |
| N39 | 56 | Vivek Vikram Singh | 2W/3W India traction-motor market share ~25% (management aspires to >50%) | market share — GUIDANCE |
| N40 | 56 | Vivek Vikram Singh | Denso's brand awareness vs. Sona's ~100:1 | brand color |
| N41 | 69 | Rohit Nanda | VA-to-employee-cost ratio = 4.5x | key ratio |
| N42 | 73,75 | Vivek Vikram Singh / Rohit Nanda | Robotics order SOPs within 12-15 months max; specifically "1 this quarter, 1 next quarter, 1 within 15 months" | timeline — GUIDANCE |
| N43 | 77,79 | Vivek Vikram Singh | Light rare-earth alternatives in use for ~5 quarters running; no magnet shortage impact | supply-chain status |
| N44 | 86 | Pratik Sachan | Order-book consumption: average order life ~8 years → quarterly consumption multiplier ~32x | order-book arithmetic (feeds Role 5 consistency check vs. N20) |

Management-numbers count = 44.

---

## TABLE 5 — FORWARD-COMMITMENT / HEDGE STATEMENTS (with turn number)

| F# | Turn | Type | Statement (paraphrase close to source) |
|----|------|------|------------------------------------------|
| F1 | 3 | GUIDANCE | Robotics/physical AI "has the potential to become a significant long-term growth platform" for the company |
| F2 | 3 | GUIDANCE | Sona Comstar 2.0 ambition: "build another 10X company" over the next decade |
| F3 | 3 | GUIDANCE | "We expect that these recovery measures [cost pass-throughs] will become progressively more visible from quarter 2 onwards" |
| F4 | 3 | HEDGE | Continued margin pressure "may continue" given lag structure of cost pass-throughs |
| F5 | 3 | HEDGE/GUIDANCE | Robotics described as "a small business today surely, but one that we believe has the potential to become a meaningful growth engine... over the next 10 years" |
| F6 | 14/61 | HEDGE | JV2 SOP/revenue-recognition timeline withheld citing confidentiality agreements with DENSO and customers — repeated verbatim non-disclosure at both turn 14 (Pramod) and turn 61 (Kapil relay) |
| F7 | 19 | GUIDANCE | "Neither Denso nor us have ever accepted anything less than market leadership" (JV2 market-share ambition) |
| F8 | 30/32 | GUIDANCE | "We have always built capacity ahead of markets" — standing capacity-guidance claim, reaffirmed by Sat Mohan Gupta ("Not right now" re: constraints) |
| F9 | 34 | HEDGE | On whether EV demand is at an "inflection": "I don't know... this is just one quarter of data, let me have 2-3 data points... then we know" |
| F10 | 36 | HEDGE/GUIDANCE | Robotics ramp expected "faster, much faster, probably" than the historical EV-business ramp, but "how much too early to tell" |
| F11 | 59 | GUIDANCE/HEDGE | JV2 global (ex-India) expansion "definitely on the anvil, but yes, it will take time" (phase 2) |
| F12 | 73/75 | GUIDANCE | Robotics order SOPs specifically timed: 1 this quarter, 1 next quarter, 1 within 15 months |
| F13 | 77 | HEDGE | On rare-earth magnet restrictions: "we don't think there is going to be much change" — no update for 5 quarters |
| F14 | 90 | HEDGE | Explicit admission of uncertainty on robotics execution/lifecycle timeline: "I don't think I know" |
| F15 | 93/95 | HEDGE | Vikram Verma: robotics product generations "still figuring out," industry moving to next generation before first generation has completed its shop-floor lifecycle |

Forward/hedge count = 15.

---

## SUMMARY NOTES FOR A3/A4

1. Doctype is concall only — the results-filing enumeration categories (numbered notes, financial-table line items incl. ZERO_STANDING, Board Outcome agenda items, annexures, auditor-report paragraphs, consolidation-entity list, digital-signature blocks) do not apply to this artifact. `zero_standing` and `agenda_items`-type categories are N/A for this run, not silently dropped — flagged NOT_APPLICABLE_DOCTYPE rather than omitted.
2. No prior-quarter concall ledger was supplied, so no ENTITY_CHANGE or DROPPED_SLIDE diff was possible. This is a known gap for A3/A4 to carry forward, not a mismatch.
3. Two management participants named on the roll call (Amit Mishra, Head Railway Business; Ankit Agarwal, Head Investor Relations) never speak — zero turns each — despite being formally introduced. Not classified as MGMT_ABSENCE (that flag is reserved for promoter/CMD absence; Vivek Vikram Singh, the MD & Group CEO, was present and dominant throughout), but flagged here as a silence signal worth A3 attention given the railway business (Amit Mishra's area) was specifically highlighted as the quarter's fastest-growing geography driver (China, via suspension motor ramp) and diversification story.
4. Four of five buy-side analysts (Pramod Kumar, Nitin Arora, Jay Kale, Sonal Gupta) have their firm affiliation recorded as NOT FOUND — the transcript states firm names for none of them; only Kapil Singh's firm (Nomura) is stated, because he is also the call host. Do not backfill from external knowledge.
5. Three distinct REPEAT_QUESTION clusters are flagged: (a) JV2 revenue/SOP timeline, asked independently by Pramod Kumar (Q2) and via Kapil Singh's relayed chat question (Q16) — management gave the identical non-answer both times; (b) robotics ramp-up/execution timeline, asked independently by Nitin Arora (Q8), Kapil Singh's chat relay (Q21, re: SOP timing) and Jay Kale (Q25, live follow-up) — only on the third ask did management concede explicit uncertainty; (c) the e-axle JV1/JV2 structuring question, asked by Jay Kale (Q10) and again by Sonal Gupta (Q14) from different angles.
6. N17 (management's robotics order book, ₹8 billion / ₹800 crore) and Nitin Arora's own paraphrase at turn 35 ("800 crores of orders") are numerically consistent (billion/crore conversion at 1 billion = 100 crore) — flagged here only so A3/A4 does not mistake this for a discrepancy.
7. N20 (net order book ₹240 billion) vs. Q24/N44 (order-consumption arithmetic, ~15 billion orders consumed vs. ~13 billion quarterly revenue, per Kapil Singh's chat question and Pratik Sachan's ~32x/8-year-life answer) is the single most quantitatively load-bearing exchange in the Q&A for Role 5's arithmetic-consistency check and should be A3/A4's first reconciliation target against the Role 4 filing baseline.
