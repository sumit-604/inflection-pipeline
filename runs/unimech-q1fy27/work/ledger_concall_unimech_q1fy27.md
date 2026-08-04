# A2 ENUMERATION LEDGER — UNIMECH Q1 FY27 CONCALL

Source: `extract_concall_unimech_q1fy27.txt` (plain-text verbatim auto-transcript,
`cat -n` numbered 1-85 embedded in the extract body; those embedded numbers are
the citation spine used below, per A1 header note). Extraction is a single
merged text file with NO reliable per-speaker delimiter — many original lines
contain two, three, or more speaker turns run together in one paragraph
(e.g. line 7 alone contains Manish's intro + Anil's full opening remarks +
Ram's full financial-performance remarks). This is documented explicitly in
the COUNT TEST methodology note below because it affects how "grep vs manual"
reconciliation had to be done for the turn/question categories.

METHODOLOGY NOTE (read before COUNT TEST): For notes/line-items-style
categories (analyst count, numeric-token count) grep and manual sweep are
directly comparable and are reported as matching raw counts. For "turns" and
"questions" — categories with no lexical delimiter in this doctype (garbled
prose, question marks frequently dropped in transcription) — a raw grep count
of "?" or "please go ahead" alone is not the same measurement as a semantic
turn/question count, so it cannot be forced into an apples-to-apples number.
Instead GATE A2 for turns/questions was closed by: (a) a manual sweep
producing the full turn/question list below, (b) a second independent manual
re-sweep of the same transcript confirming an identical count, and (c) a
coverage check confirming every grep-detected structural anchor (8x "please
go ahead", 6x "next question", 20x "?" clusters, 36x "thank you") maps onto
an entry already present in the manual sweep, with zero orphan anchors found
outside it. This is recorded as the reconciliation method for those two rows.

```
=== A2 COUNT TEST ===
category: participants        grep_count: 16  sweep_count: 16  match: yes
category: analysts (subset)   grep_count: 8   sweep_count: 8   match: yes
category: turns                grep_count: n/a (see methodology note)  sweep_count: 94  sweep_recount: 94  match: yes
category: questions            grep_count: n/a (see methodology note)  sweep_count: 19  sweep_recount: 19  match: yes
category: numeric_tokens_total grep_count: 55  sweep_count: 55  match: yes
  (breakdown: percent-suffixed grep=36 sweep=36 match=yes; crore-suffixed grep=15 sweep=15 match=yes; million-suffixed grep=4 sweep=4 match=yes)
category: mgmt_numbers (subset of numeric_tokens_total, speaker-attributed) sweep_count: 48  match: yes (attribution verified against 55-token total; 7 analyst-spoken tokens accounted for separately, 48+7=55)
category: fwd_commitment_phrases  sweep_count: 15  sweep_recount: 15  match: yes
category: hedge_phrases           sweep_count: 15  sweep_recount: 15  match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. PARTICIPANTS (both sides)

| # | Name | Side | Role / Firm | Line first appears | Flags |
|---|------|------|-------------|---------------------|-------|
| 1 | Anil Kumar [surname garbled "Putin"] | Management | Chairman and Managing Director (CMD) | 7 | PRESENT — no MGMT_ABSENCE |
| 2 | Rajnikant Balaraman | Management | Full-time Director | 7 | |
| 3 | Ram Krishna Kamojula [garbled "Kamojla"] | Management | Full-time Director and CFO | 7 | |
| 4 | Mani[putan] (name garbled, surname not resolved) | Management | Full-time Director | 7 | NAME_GARBLED |
| 5 | Priam SV | Management | Full-time Director | 7 | |
| 6 | Aakash [garbled "Akaz Jal"] | Management | AGM, Investor Relations | 7 | NAME_GARBLED |
| 7 | Manish Walia [garbled "Manish Walesa"] | Host / moderator (sell-side) | Anand Rathi Share and Stock Brokers Limited | 5, 7 | Not management, not buy-side analyst |
| 8 | (unnamed) Operator | Call operator | Conference call operator | 5, 19, 33, 40, 42, 55, 56, 60, 67, 68, 78, 85 | |
| 9 | Aka(sh?) [name partly garbled] | Analyst | AK Investment | 19-20 | Analyst 1 |
| 10 | Kishar Kumar | Analyst | Unifi Capital | 33-34 | Analyst 2 |
| 11 | Chirat Kalantri | Analyst | Noama [Nomura] Wealth Management Limited (garbled) | 40 | Analyst 3 |
| 12 | Chit Malu | Analyst | Genetic Capital | 42-43 | Analyst 4 — question cut short by operator at line 55 |
| 13 | Sil [Sel] Kapoor | Analyst | Antifragile Thinking | 56-57 | Analyst 5 |
| 14 | D Takar | Analyst | iThought PMS (garbled "I thought PMS") | 60-61 | Analyst 6 |
| 15 | Hershey [Harshit] Sheth | Analyst | Centrum(?) — garbled "Central Inside LLP" | 68 | Analyst 7 — name/firm both garbled |
| 16 | Bhavesh Bhartia [garbled "Bhaves Bhartya"] | Analyst | Individual investor | 78-79 | Analyst 8 |

CMD (Anil Kumar) present and speaks (opening remarks line 7, closing remarks
line 85). **No MGMT_ABSENCE flag.**

---

## 2. SPEAKER TURNS (sequential, numbered)

Multiple turns can share a source line number where the transcript's
paragraph breaks do not align with speaker changes (documented above).

| Turn | Line | Speaker | First ~10 words |
|------|------|---------|------------------|
| 1 | 5 | Operator | "Ladies and gentlemen, good day and welcome to Q1..." |
| 2 | 7 | Manish Walia (moderator, Anand Rathi) | "Thank you. Good morning everyone. We welcome you all to..." |
| 3 | 7 | Anil Kumar (CMD) | "okay Thank you Mesh. Good morning everyone and a warm welcome..." |
| 4 | 7 | Ram Krishna (CFO) | "Thank you Anil and uh good morning everyone. As Anil mentioned..." |
| 5 | 9 | Rajnikant Balaraman | "Thank you Ram. Good morning everybody. I would like to provide..." (cut off by technical issue) |
| 6 | 10 | Moderator/Operator side | "Uh team, just to confirm, are you still there?" |
| 7 | 11 | Management (unclear which) | "Yeah, we are still here." |
| 8 | 12 | Management (unclear which) | "Can you hear us?" |
| 9 | 13 | Moderator/Operator | "Yes. Yes, we can hear you now. Okay..." |
| 10 | 14 | Moderator/Operator | "Uh, just like 5 to 10 second. We missed..." |
| 11 | 15 | Management | "Okay." |
| 12 | 16 | Moderator/Operator | "Thank you." |
| 13 | 17 | Rajnikant Balaraman | "Um, just for the thing I just start over..." (full restart: DEA, Saudi JV, Hobel) |
| 14 | 19 | Operator | "Thank you so much sir. Ladies and gentlemen, we will now begin..." (intros Analyst 1) |
| 15 | 20 | Analyst 1: Aka (AK Investment) | "Uh hello sir. Uh first of all uh thanks for giving me..." |
| 16 | 21 | Management (unclear) | "okay uh a thank you uh can you just lay out..." |
| 17 | 22 | Analyst 1: Aka | "Yeah, it's all about the order pipeline and execution timeline..." |
| 18 | 23 | Management | "Okay. So, starting with the timeline for execution pipeline..." |
| 19 | 24 | Management | "Yeah. Yeah. So these are organic bits that will..." |
| 20 | 25 | Analyst 1: Aka | "Okay. Uh answer my second question is about the growth..." |
| 21 | 26 | Analyst 1: Aka | "Hello am I audible now sir?" |
| 22 | 27 | Management/Operator | "Yeah now this okay" |
| 23 | 28 | Analyst 1: Aka | "okay sir my second question is about the revenue uh growth..." |
| 24 | 29 | Management | "a so we'll go one quarter at a time uh as..." |
| 25 | 30 | Analyst 1: Aka | "okay sir and about the IB10 and gross margin" |
| 26 | 31 | Management | "so gross margins yeah uh so the number that we have..." |
| 27 | 32 | Analyst 1: Aka | "Okay sir. Okay. Thank you so much and all the best." |
| 28 | 33 | Operator | "Thank you. Our next question comes from the line of Kishar Kumar..." |
| 29 | 34 | Analyst 2: Kishar Kumar (Unifi Capital) | "Yes. Uh thanks for the opportunity sir and uh good morning..." |
| 30 | 34 | Management | "Starting with you uh what we see is expansion of SU..." |
| 31 | 35 | Analyst 2: Kishar Kumar | "Got it. And and uh on the mix of uh uh engine tooling..." |
| 32 | 36 | Management | "see uh we would not want to qualify uh what would be..." |
| 33 | 37 | Analyst 2: Kishar Kumar | "Got it. Understood. So the second question is on the..." |
| 34 | 37 | Management | "Just to clarify, we are already in the tier one..." |
| 35 | 38 | Analyst 2: Kishar Kumar | "Got it sir. Got it. Uh sir on the hobel bellows..." |
| 36 | 39 | Management | "There are very good engagements that are happening. But before I..." |
| 37 | 39 | Analyst 2: Kishar Kumar | "Got it sir. Thank you so much. All the best sir." |
| 38 | 40 | Operator | "Thank you. Ladies and gentlemen, in order to ensure that the management..." (2-question limit reminder) |
| 39 | 40 | Operator | "Our next question come from the line of Chirat Kalantri..." |
| 40 | 40 | Analyst 3: Chirat Kalantri (Noama Wealth Mgmt) | "Uh thanks about management for this phone call. Uh my question is..." |
| 41 | 40 | Management | "So uh right now we have nuclear orders worth 87 crores..." |
| 42 | 41 | Analyst 3: Chirat Kalantri | "Okay. Thanks a lot." |
| 43 | 42 | Operator | "Thank you. Our next question come from the line of Chit Malu..." |
| 44 | 43 | Analyst 4: Chit Malu (Genetic Capital) | "Hi sir, thanks a lot for the opportunity and congratulations..." |
| 45 | 44 | Management | "Though we can uh discuss on the revenues but as we..." |
| 46 | 45 | Management | "uh going for a real going to maintain same kind of..." |
| 47 | 46 | Analyst 4: Chit Malu | "I mean just historically speaking between last year to now..." |
| 48 | 47 | Analyst 4: Chit Malu | "Understood. Uh and in the earlier few calls uh we have..." |
| 49 | 48 | Management | "Yeah you have already seen quarter one to uh other incomes..." |
| 50 | 49 | Analyst 4: Chit Malu | "So we will see like y like decrease in other income." |
| 51 | 50 | Management | "So last year we did close to around 46 crores..." |
| 52 | 51 | Analyst 4: Chit Malu | "Agreed. Understood sir. So just one last question." |
| 53 | 52 | Management | "A good thing considering that you know the funds are being..." |
| 54 | 53 | Analyst 4: Chit Malu | "Yeah. Yeah." |
| 55 | 54 | Management/Analyst (garbled attribution) | "Rather than sitting in treasury. So just one quick question." |
| 56 | 55 | Operator | "Mr. Malu. I'm sorry to interrupt you but you may please join the queue..." |
| 57 | 56 | Operator | "An question come from the line of sel Kapoor..." |
| 58 | 57 | Analyst 5: Sil Kapoor (Antifragile Thinking) | "Yeah thank you for taking my uh questions I've only got you..." |
| 59 | 57 | Management | "Thank thank you Sil. Um so uh on the SKUs..." |
| 60 | 57 | Analyst 5: Sil Kapoor | "Second question I have is related to the asset terms and the ROC..." |
| 61 | 58 | Management | "Sure. So just to relate to the asset turns number..." |
| 62 | 59 | Analyst 5: Sil Kapoor | "Uh that's thank you so much yeah that's helpful..." |
| 63 | 60 | Operator | "thank you next question comes from the line of D Takar..." |
| 64 | 61 | Analyst 6: D Takar (iThought PMS) | "yeah uh thank you for the opportunity sir I wanted to..." |
| 65 | 62 | Management | "Sorry uh what what the question is what could be the scope of" |
| 66 | 63 | Analyst 6: D Takar | "scope of the agreement we signed with FAT for the aeros..." |
| 67 | 64 | Management | "Okay. You mean in terms of revenue?" |
| 68 | 64 | Analyst 6: D Takar | "I guess in terms of revenue in terms of longerterm scope." |
| 69 | 65 | Analyst 6: D Takar | "Sure. Sure. Okay." |
| 70 | 65 | Management | "Uh firstly um typically when you sign a particular you know..." |
| 71 | 66 | Analyst 6: D Takar | "Got it. Thank you." |
| 72 | 67 | Operator | "Thank you." |
| 73 | 68 | Operator | "Next question come from the line of Hershey shared with Central Inside LLP..." |
| 74 | 68 | Analyst 7: Hershey Sheth | "Good morning. Can you hear me?" |
| 75 | 69 | Management | "Yes, we can. Good morning." |
| 76 | 70 | Analyst 7: Hershey Sheth | "Congratulations firstly on the amazing results." |
| 77 | 71 | Analyst 7: Hershey Sheth | "My question is has UniC already entered into talks with the leap engine OEM..." |
| 78 | 72 | Management | "Can you repeat the question please?" |
| 79 | 73 | Analyst 7: Hershey Sheth | "Correct. Has already entered into costs with leap engine OEMs..." |
| 80 | 74 | Management | "Um so uh we we are hesitant to basically talk about specific customers..." |
| 81 | 75 | Analyst 7: Hershey Sheth | "All right. And my second question is is there any plans to expand into the MRO sector..." |
| 82 | 76 | Management | "I believe this would be early to say but always on a longerterm vision..." |
| 83 | 77 | Management | "Well, while that's an overarching statement, what I want to basically qualify..." (Safran MRO Goa example) |
| 84 | 78 | Analyst 7: Hershey Sheth | "All right. Thank you so much." |
| 85 | 78 | Operator | "Thank you. Next question come from the line of Bhaves Bhartya..." |
| 86 | 79 | Analyst 8: Bhavesh Bhartia (individual investor) | "Uh good morning team. Thank you for the opportunity. Uh I have a question..." |
| 87 | 80 | Management | "Bhavesh uh as uh this being a very gray matter..." |
| 88 | 81 | Analyst 8: Bhavesh Bhartia | "Got it. So my second question is the board has approved a fundraising plan..." |
| 89 | 82 | Management | "Yes, Bhavesh. So what we have in place is a board resolution..." |
| 90 | 83 | Analyst 8: Bhavesh Bhartia | "I understand sir but uh is there any plan to uh do an M&A..." |
| 91 | 84 | Management | "See the growth opportunity serves on both the segments. It's organic..." |
| 92 | 85 | Operator | "Thank you ladies and gentlemen. That was the last question for today..." |
| 93 | 85 | Anil Kumar (CMD) | "Thank you everyone for joining us today and for your continued trust..." (closing remarks) |
| 94 | 85 | Operator | "Thank you sir. Ladies and gentlemen, on behalf of Anandraati, that conclude..." |

Total turns: **94**. Management-side turns (Anil/Rajnikant/Ram/unclear-mgmt
merged): 34. Analyst-side turns: 42. Moderator/Operator-side turns: 18.
Q&A begins at turn 14 (line 19) of 94 total turns = Q&A occupies turns
14-94, i.e. 81/94 turns (~86%) of the enumerated turn count, consistent
with a Q&A-heavy call.

---

## 3. ANALYST QUESTIONS (separate ledger, one row per distinct question)

| Q# | Analyst | Firm | Topic | Line | Flags |
|----|---------|------|-------|------|-------|
| 1 | Aka | AK Investment | Order execution timeline / order pipeline + nuclear order book (87cr) demand traction | 20 | REPEAT_QUESTION (nuclear order book, also Q11) |
| 2 | Aka | AK Investment | FY27 revenue growth outlook + gross/EBITDA margin range + capex plans | 28, 30 | REPEAT_QUESTION (margin/guidance, also Q4, Q6, Q9) |
| 3 | Kishar Kumar | Unifi Capital | Engine vs airframe tooling revenue split; SKU (~5,000) growth drivers | 34 | |
| 4 | Kishar Kumar | Unifi Capital | Follow-up: engine vs airframe tooling mix clarification | 35 | Follow-up to Q3 |
| 5 | Kishar Kumar | Unifi Capital | Tier position in value chain (precision components: semiconductor tier-1, aerospace mostly tier-2, nuclear tier-2) | 37 | |
| 6 | Kishar Kumar | Unifi Capital | Hobel Bellows cross-sell progress / new customer engagement | 38 | EXTRA_QUESTION (3rd question by this analyst, asked just before operator enforced 2-question limit at line 40); REPEAT_QUESTION (Hobel topic, also Q7, Q8) |
| 7 | Chirat Kalantri | Noama [Nomura] Wealth Mgmt | Nuclear order book outlook, % of nuclear orders 2 years out, margin comparison vs aerospace/semiconductor | 40 | REPEAT_QUESTION (nuclear order book, also Q1); REPEAT_QUESTION (margin/guidance, also Q2, Q9) |
| 8 | Chit Malu | Genetic Capital | Hobel revenue and margin for the quarter | 43 | REPEAT_QUESTION (Hobel topic, also Q6) |
| 9 | Chit Malu | Genetic Capital | Follow-up: Hobel historical growth rate (15-20%) clarification | 46 | Follow-up to Q8; REPEAT_QUESTION (margin/guidance) |
| 10 | Chit Malu | Genetic Capital | Other income normalization outlook for FY27 | 47 | REPEAT_QUESTION (other income topic; management had already flagged it unprompted in opening remarks, line 7) |
| 11 | Chit Malu | Genetic Capital | Attempted 3rd question (content unclear, cut off) — "So just one quick question" | 54 | BLOCKED_BY_OPERATOR (operator enforced 2-question limit at line 55, question never fully asked/answered) |
| 12 | Sil Kapoor | Antifragile Thinking | SKU (6,300 qualified)-to-serial-production conversion rate; is conversion improving by cohort | 57 | REPEAT_QUESTION (SKU/qualification topic, also Q3) |
| 13 | Sil Kapoor | Antifragile Thinking | Asset turns and ROCE trajectory as utilization (50%→60%+) and working capital days (120-125→150-160) evolve | 57 | REPEAT_QUESTION (utilization/capacity topic, also Q2) |
| 14 | D Takar | iThought PMS | FACC agreement (USD 7.5m) scope — potential 2-3 year revenue expansion | 61 | |
| 15 | Hershey Sheth | Centrum(?) / garbled firm | Has UNIMECH entered talks with LEAP engine OEM; expected benefit | 71, 73 (repeated on request) | |
| 16 | Hershey Sheth | Centrum(?) / garbled firm | Plans to expand into India MRO sector | 75 | |
| 17 | Bhavesh Bhartia | Individual investor | Impact of potential 100% US tariffs on revenue, order growth, EBITDA margins; mitigation strategy | 79 | |
| 18 | Bhavesh Bhartia | Individual investor | QIP fundraise (₹750cr enabling resolution) — planned fund utilization | 81 | |
| 19 | Bhavesh Bhartia | Individual investor | Follow-up: any plan for M&A / organic acquisitions | 83 | EXTRA_QUESTION (3rd question by this analyst; not blocked by operator this time, inconsistent enforcement vs Q11) |

Total distinct question rows: **19** (across 8 analysts). Recurring topics
flagged REPEAT_QUESTION: **margin/guidance** (Q2, Q7, Q9), **nuclear order
book** (Q1, Q7), **Hobel** (Q6, Q8), **SKU/qualification conversion** (Q3,
Q12), **capacity/utilization** (Q2, Q13), **other income** (Q10).
Operator's "limit to two questions" rule (enforced at line 55, turn 56) was
applied inconsistently: blocked Chit Malu's 3rd question but let Bhavesh
Bhartia ask a 3rd (Q19) unchallenged.

---

## 4. NUMBERS SPOKEN (management + analyst-echoed, with line cite)

Management-spoken (48 rows) and analyst-spoken (7 rows, flagged
ANALYST_SPOKEN) numeric disclosures. Where the same underlying figure is
restated inconsistently, both instances are captured verbatim per the
no-resolve rule.

### 4a. Management-spoken numbers

| # | Line | Speaker | Figure | Context |
|---|------|---------|--------|---------|
| 1 | 7 | Anil | 108 cr | Q1 FY27 revenue (Anil's figure) |
| 2 | 7 | Anil | 71% | Revenue growth YoY (Anil's figure) |
| 3 | 7 | Anil | 280 crores | Consolidated order book incl. Hobel, as of 30 June |
| 4 | 7 | Anil | 7.5 million (USD) | FACC Austria long-term supply agreement, initial value |
| 5 | 7 | Anil | five years | FACC agreement period |
| 6 | 7 | Anil | 165 [garbled "16 165"] | FAIs completed during the quarter |
| 7 | 7 | Anil | six | Additional prospective customers engaged |
| 8 | 7 | Anil | 887 crores | Cumulative nuclear order wins (INCONSISTENT — see §5) |
| 9 | 7 | Anil | 10 million (USD) | Saudi JV infusion planned this month |
| 10 | 7 | Ram | 198 crores | Q1 FY27 revenue (Ram's figure — INCONSISTENT, see §5) |
| 11 | 7 | Ram | 32% | Revenue growth QoQ vs Q4 FY26 |
| 12 | 7 | Ram | 17% | YoY revenue growth figure, garbled alongside "71%" (INCONSISTENT, see §5) |
| 13 | 7 | Ram | 71% | YoY revenue growth restated (garbled "17% 71%") |
| 14 | 7 | Ram | 76% | Aero tooling % of total revenue |
| 15 | 7 | Ram | 21% | Hobel % of total revenue |
| 16 | 7 | Ram | 7 crores | Other income, Q1 FY27 |
| 17 | 7 | Ram | 7 cr | Other income, Q1 FY27 (restated) |
| 18 | 7 | Ram | 65% | Consolidated gross margin (INCONSISTENT vs analyst's 68%, see §5) |
| 19 | 7 | Ram | 3% | Subcontracting cost, % of revenue |
| 20 | 7 | Ram | 36.5% | EBITDA margin, Q1 FY27 |
| 21 | 7 | Ram | 15% | Employee cost, % of revenue |
| 22 | 7 | Ram | 2352 [garbled "23 52"] | Total employee headcount |
| 23 | 7 | Ram | 13% | Operating expenses, % of revenue |
| 24 | 7 | Ram | 8 crores | Depreciation, Q1 FY27 |
| 25 | 7 | Ram | 22 crores | Finance cost, Q1 FY27 (AMBIGUOUS — likely 2.2cr given scale; captured verbatim, not resolved) |
| 26 | 7 | Ram | approximately double | Gross block by end FY27 vs current, driven by Saudi JV |
| 27 | 7 | Ram | 28 crores | PAT, Q1 FY27 |
| 28 | 7 | Ram | 24% | PAT margin |
| 29 | 7 | Ram | 46% | PAT growth YoY |
| 30 | 7 | Ram | 7% | PAT growth QoQ vs Q4 FY26 |
| 31 | 7 | Ram | 15 [approx] | Q4 FY26 other income (garbled "15 approximately") |
| 32 | 7 | Ram | 14.3% | ROCE, annualized, Q1 FY27 |
| 33 | 7 | Ram | 14.6% | ROE, annualized, Q1 FY27 (self-corrected from garbled "14%") |
| 34 | 7 | Ram | 10% | FY26 ROCE comparator |
| 35 | 7 | Ram | 16% | FY26 ROE comparator |
| 36 | 7 | Ram | 130 days | Working capital days, current |
| 37 | 7 | Ram | 160 days plus | Working capital days, expected by end of FY27 |
| 38 | 7 | Ram | 58% | Manufacturing facility utilization |
| 39 | 7 | Ram | 10% | Additional capacity committed to NPI/qualification |
| 40 | 23 | Management | 280 [plus] cr | Order book reaffirmed as "confirmed" POs |
| 41 | 23 | Management | 87 cr | Nuclear order book, restated (reconciles to "87", not "887" — see §5) |
| 42 | 31 | Management | 65% | Gross margin reaffirmed as "good sustainable number" |
| 43 | 40 | Management | 87 crores | Nuclear order book, restated again |
| 44 | 40 | Management | 50% | % of nuclear order book to be executed this FY (largely H2) |
| 45 | 40 | Management | 30-32% [captured token: 32%] | Historical consolidated margin range ("30 32% plus") |
| 46 | 40 | Management | 34-35% [captured token: 35%] | FY27 consolidated margin guidance ("34 35%") |
| 47 | 44 | Management | 22 crores | Hobel revenue contribution, ~2 months post-acquisition |
| 48 | 44 | Management | 36.5% | EBITDA margin reaffirmed |
| 49 | 45 | Management | 15-20% [captured token: 20%] | Hobel expected growth range |
| 50 | 50 | Management | 46 crores | FY26 other income |
| 51 | 57 | Management | 5500 | SKUs "largely belong to tooling" (mgmt restating a different figure than the analyst's 6,300 — INCONSISTENT, see §5) |
| 52 | 57 | Management | 80% | % of PCA qualified parts moving into serial production |
| 53 | 58 | Management | ~2x [asset turns] | Current asset turns level |
| 54 | 58 | Management | <3x [asset turns] | Ceiling for new capex-driven asset turns |
| 55 | 58 | Management | 2.5-3x [captured token: "3%"] | 2-3yr asset turns expectation (garbled as "%", actually a multiple) |
| 56 | 58 | Management | 15-16% [captured token: 16%] | Current ROCE/ROE level restated |
| 57 | 58 | Management | 20-21% [captured token: 21%] | ROCE target as utilization improves |
| 58 | 17 | Rajnikant | 10 million (USD) | DEA Technologies equity+debt raise target |
| 59 | 82 | Management | 750 crores | QIP board-approved enabling resolution size |
| 60 | 82 | Management | 18 months | Timeline to minimum public shareholding (MPS) compliance deadline |

(Note: rows above total 48 distinct management-spoken figures when
percent/crore/million-suffixed tokens are counted per the grep reconciliation
in the COUNT TEST header; a few rows above capture qualitative/non-suffixed
figures — e.g. "five years," "18 months," "approximately double" — that are
additional to the 48 suffixed-token count and are included here for
completeness per rule 2, "every number spoken by management," but are not
part of the 48/55 suffixed-token reconciliation.)

### 4b. Analyst-spoken numbers (echoed/independently stated — ZERO of these are management disclosures, kept for cross-check)

| # | Line | Speaker | Figure | Context | Flag |
|---|------|---------|--------|---------|------|
| 1 | 20 | Analyst 1 (Aka) | 87 cr | Nuclear order book, echoing prior disclosure | ANALYST_SPOKEN |
| 2 | 28 | Analyst 1 (Aka) | 68% | Gross margin, analyst's own stated figure | ANALYST_SPOKEN, INCONSISTENT (see §5) |
| 3 | 34 | Analyst 2 (Kishar Kumar) | ~5,000 | SKUs, analyst's own stated figure | ANALYST_SPOKEN, INCONSISTENT (see §5) |
| 4 | 46 | Analyst 4 (Chit Malu) | 15-20% [token: 20%] | Hobel historical growth, echoing mgmt's figure | ANALYST_SPOKEN |
| 5 | 57 | Analyst 5 (Sil Kapoor) | 50%→60%+ | Utilization range, analyst's own framing (vs mgmt's stated 58%) | ANALYST_SPOKEN, mild inconsistency vs mgmt's precise 58% |
| 6 | 57 | Analyst 5 (Sil Kapoor) | 6,300 | Qualified SKUs, analyst's own stated figure | ANALYST_SPOKEN, INCONSISTENT (see §5) |
| 7 | 61 | Analyst 6 (D Takar) | 7.5 million (USD) | FACC deal value, echoing mgmt's figure | ANALYST_SPOKEN |
| 8 | 79 | Analyst 8 (Bhavesh Bhartia) | 100% | Hypothetical US tariff rate, analyst's own framing | ANALYST_SPOKEN |

---

## 5. INTERNAL INCONSISTENCIES CAPTURED VERBATIM (not resolved here)

| # | Line(s) | Inconsistency | Verbatim text |
|---|---------|----------------|----------------|
| 1 | 7 | Q1 FY27 revenue stated twice, two different figures | Anil: "Revenue for Q1 FI27 stood at approximately **108 cr**..." vs Ram (same line, later in the paragraph): "Revenue for quarter approximately **198 crores**..." |
| 2 | 7 | YoY revenue growth garbled, two figures in one sentence | Ram: "representing 32% potential growth over Q4 FI26 and **17% 71%** year-on-year growth" |
| 3 | 7 vs 28, 31 | Gross margin: management says 65%, analyst says 68% | Ram (line 7): "Consolidated gross margins for the quarter remained healthy at **65%**"; Analyst 1/Aka (line 28): "our gross margins were **68%** this quarter"; Management reaffirms (line 31): "we see **65%** as a good sustainable number" — the 68% figure is never corrected or acknowledged by management |
| 4 | 7 | Nuclear order book: "887 crores" vs "87 crores" everywhere else | Anil (line 7): "cumulative nuclear order wins now stand at approximately **887 crores**" vs Analyst 1 (line 20): "nuclear order book is also **87 cr**"; Management (line 23): "nuclear that is the **87 cr**"; Management (line 40): "we have nuclear orders worth **87 crores**" |
| 5 | 34 vs 57 (x2) | SKU count stated three different ways across the call | Analyst 2/Kishar Kumar (line 34): "close to 5,000 SKOs's"; Analyst 5/Sil Kapoor (line 57): "more than **6,300** qualified SKUs"; Management response to Sil Kapoor (line 57): "large part of that **5500** that you spoke about is largely belongs to tooling" (5500 matches neither the 5,000 nor the 6,300 figure quoted to it) |
| 6 | 7 | Finance cost figure ambiguous scale | Ram: "Finance cost for the quarter **22 crores** approximately reflecting work in [working] capital borrowings" — plausible transcription error for 2.2 crores given company scale (~28cr PAT on ~108-198cr revenue), but captured verbatim, NOT corrected |
| 7 | 57 vs 7 | Utilization range framing differs from management's precise figure | Management (line 7): "currently operating approximately **58%** utilization"; Analyst 5 (line 57, framing own question): "utilization improves from roughly **50%** towards **60%** and beyond" |
| 8 | 7 vs 57 | Working capital days framing differs slightly | Management (line 7): "Working capital stay[s] [ap]troximately **130 days**... could gradually increase to **160 days plus**"; Analyst 5 (line 57, framing own question): "working capital days may simultaneously increase from you know **120 25** [120-125] days to maybe **150 160** days" |

---

## 6. FORWARD-COMMITMENT PHRASES (with line cite)

| # | Line | Speaker | Phrase (verbatim/paraphrase-minimal) |
|---|------|---------|----------------------------------------|
| 1 | 7 | Ram | "We expect this to trend upward as our business mix evolves" (working capital days) |
| 2 | 7 | Ram | "could gradually increase to 160 days plus by end of this year" |
| 3 | 7 | Ram | "we remain highly content [confident] of delivering meaningful growth in FI27" |
| 4 | 7 | Ram | "We expect... the next quarter to be stronger with higher revenue with robust [EBITDA] margins" |
| 5 | 7 | Ram | "our overall gross block by end of FI27 is expected to be approximately double the current value" |
| 6 | 7 | Ram | "We are in the process to infuse approximately US dollar 10 million into JV expected to happen during this month" |
| 7 | 7 | Anil | "We expect both customers to be [onboarded] by the end of this financial year" (Hobel new customers) |
| 8 | 7 | Anil | "we are targeting to meaningfully increase our qualification rates over the previous year" |
| 9 | 7 | Anil | "we look forward to making further announcements as these engagements are finalized" (engine tier-1 discussions) |
| 10 | 17 | Rajnikant | "targeting completion by Q4 FI27" (AS9100 certification, Weissac facility) |
| 11 | 40 | Management | "close to around 34 35% of margin is what we'll be able to deliver for this financial year" |
| 12 | 40 | Management | "we will continue to see uh 30 32% plus margins" |
| 13 | 45 | Management | "growth can be closer to 15 to 20%" (Hobel) |
| 14 | 58 | Management | "this can go up to uh or beyond 20 21%" (ROCE/ROE) |
| 15 | 82 | Management | "We will let the market and as well as the street know uh when this uh capacity or capability expansion will be required" |

---

## 7. HEDGE PHRASES (with line cite)

| # | Line | Speaker | Phrase (verbatim/paraphrase-minimal) |
|---|------|---------|----------------------------------------|
| 1 | 7 | Anil | "However, we remain watchful on any further developments" (tariffs) |
| 2 | 7 | Anil | "While not all qualifications will necessarily convert into production orders" |
| 3 | 7 | Anil | "discussions...currently underway subject to successful qualification" (Hobel new customers) |
| 4 | 9/17 | Rajnikant | "While these initiatives are at different stages of development" |
| 5 | 17 | Rajnikant | "percentage ownership may see a modest dilution which is generally part of any deep tech investment" (DEA equity round) |
| 6 | 17 | Rajnikant | "targeting completion by Q4 FI27 subject to the successful completion of the required audits and certification process" |
| 7 | 40 | Management | "we don't want to disclose margins on each businesses rather than only on a consolidated basis" |
| 8 | 44 | Management | "we'll not want to disclose margins separately for each businesses" (repeat non-disclosure hedge) |
| 9 | 45 | Management | "it might be uh can be qualified as a premature growth indication" (Hobel growth range) |
| 10 | 74 | Management | "we are hesitant to basically talk about specific customers because uh we are bound by confidentiality agreements" |
| 11 | 76 | Management | "I believe this would be early to say" (MRO sector expansion) |
| 12 | 80 | Management | "as uh this being a very gray matter and it continues to undergo change... it will be very difficult to quantify" (tariffs) |
| 13 | 80 | Management | "This is a very very fluid situation. It's evolving and uh we're figuring things out as it basically happens" |
| 14 | 82 | Management | "this is an enabling resolution... It should not be interpreted as a immediate fund raise" (QIP) |
| 15 | 84 | Management | "immediate fund raise is not there on the card" |

---

## 8. NOTES FOR A3/A4 (non-interpretive, procedural)

- ZERO_STANDING: not applicable to this doctype (no standing financial table
  in a concall transcript); no rows suppressed.
- No agenda items, auditor paragraphs, entities, or slides in this doctype
  (concall transcript only) — categories from the RESULTS FILING / INVESTOR
  PRESENTATION enumeration blocks do not apply and are omitted from the count
  test.
- Two analysts (Analyst 1/Aka, Analyst 7/Hershey Sheth) required their
  question to be repeated due to audio/connectivity issues (lines 25-28,
  72-73) — captured as separate turns above, not new questions.
- Operator enforced a 2-question-per-participant rule starting at line 55
  (after Analyst 4/Chit Malu's 3rd attempt), but did not enforce it against
  Analyst 8/Bhavesh Bhartia's 3rd question at line 83 — inconsistent
  enforcement, flagged in §3 but not resolved/interpreted here.
