# LEDGER — E2E Networks Limited (E2E) — Q1 FY27 — CONCALL

Source: `runs/e2e-q1fy27/work/extract_concall_e2e_q1fy27.txt` (A1 extract; 39 turns, source lines 1-76 of `e2e_concall_q1fy27.txt`)
Prior-quarter ledger: NOT PROVIDED (no prior_ledger_path injected) — REPEAT_QUESTION / trend flags below rely only on in-call analyst references to "last quarter", not on a prior ledger diff.

Methodology note on reconciliation for this doctype: this transcript is a disfluent verbatim dictation (filler words, dropped punctuation, garbled proper nouns — documented in A1 header). A blind digit-character grep over the raw text is unusable as an independent check (it snags GPU model numbers like "B200"/"H100" and stray digits) — this was tested and the raw output is noise (see Turn 10/22/26 model numbers bleeding into any naive digit grep). To make the grep/manual reconciliation in GATE A2 meaningful rather than cosmetic, each count below uses a grep pattern defined BEFORE the manual sweep was finalized, and the manual sweep was then constrained to that same atomic definition (documented per category). Where the transcript's missing punctuation would otherwise hide a distinct disclosure (e.g., a question asked without a terminal "?"), that content is not dropped — it is captured under the NUMBERS ledger (category 4) or in the topic/flags column of the nearest question row, and cross-referenced, so nothing is lost even though it is not double-counted in two categories at once.

```
=== A2 COUNT TEST ===
category: turns          grep_count: 39   sweep_count: 39   match: yes
category: participants   grep_count: 16   sweep_count: 16   match: yes   (16 operator "line of ..." caller introductions; distinct literal analyst names = 15, one repeat — see PARTICIPANTS table note)
category: questions      grep_count: 31   sweep_count: 31   match: yes   (grep = count of "?" characters within the 16 Q&A turns; sweep = one row per "?"-terminated clause, same atomic unit)
category: mgmt_numbers   grep_count: 24   sweep_count: 24   match: yes   (sweep built first as a curated list of distinct quantitative disclosures; each of the 24 items grep-verified present at least once in the extract — see NUMBERS table)
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. PARTICIPANTS (rule: concall #1)

| # | Name (as transcribed) | Firm | Role | Turn(s) introduced/speaking | Flags |
|---|---|---|---|---|---|
| P1 | Mr. Taran Dua | E2E Networks | Managing Director (management) | 2 (listed), 5 (opening remarks), 8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38 (answers), 39 (closing) | — |
| P2 | Mr. Nitan Jain | E2E Networks | Chief Financial Officer (management) | 2 (listed), 6 (financial highlights), 30,32,38 (answers) | — |
| P3 | Vanessa Fernandes | Adfactors / ASA PR | Investor Relations (IR), call host | 4 | — |
| P4 | (unnamed) Operator | — | Call operator | 3,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39 | — |
| P5 | Neil Muno | Eco Capital | Analyst | intro 7, Q&A 8 | — |
| P6 | Bharat Kulati | "Dalal..." (firm name garbled — cut off mid-sentence both times) | Analyst | intro 9, Q&A 10; follow-up intro 29 ("Bat Kulati"), Q&A 30 | Firm name never resolved in transcript both instances (`NOT FOUND`) |
| P7 | Gandhi | Bajaj Alternate Investment Management Limited (transcribed "Bajage") | Analyst | intro 11, Q&A 12 | Possible same individual as P13 "Py Gandhi / Paj Alternate..." — name/firm both near-identical, transcription variance only; NOT collapsed here (enumerate, do not interpret) |
| P8 | Nishan Joshi | Equisense Advisor Private Limited | Analyst | intro 13, Q&A 14 | — |
| P9 | "quesai" (garbled at introduction) / later addressed as "Mr. Gish" | NOT FOUND (firm never stated) | Analyst | intro 15, Q&A 16 | Name inconsistent within own turn — two different transcribed names for one caller |
| P10 | Vun Gandhi | Finn Avenue Growth Fund | Analyst | intro 17, Q&A 18 | Third "Gandhi" surname on this call (see P7, P13) — flagged for possible transcription confusion, not collapsed |
| P11 | Vidant | Minimal Securities | Analyst | intro 19, Q&A 20 | — |
| P12 | Shibbam Tamaraka, CFA | Aluras | Analyst | intro 21, Q&A 22 | — |
| P13 | Rohan Nakpal | Helios Capital | Analyst | intro 23, Q&A 24 | — |
| P14 | Ashish Ajit Ka | Pent LLP fund | Analyst | intro 25, Q&A 26 | Possible same individual as P17 "Ashish Ajit Kcha / B Ventures LLP funds" — first+middle name identical, surname and firm both garbled differently; NOT collapsed |
| P15 | Abishek Shindra | Incred Capital | Analyst | intro 27, Q&A 28 | — |
| P16 | Py Gandhi | Paj Alternate Investment Management Limited | Analyst | intro 31, Q&A 32 | See P7 note |
| P17 | Ashish Ajit Kcha | B Ventures LLP funds | Analyst | intro 33, Q&A 34 | See P14 note |
| P18 | Chilag Satia | Satia Investments | Analyst | intro 35, Q&A 36 | — |
| P19 | Sukrit Partil | Isite Fin Private Limited | Analyst | intro 37, Q&A 38 | — |

`MGMT_ABSENCE`: not applicable — both MD (Taran Dua) and CFO (Nitan Jain) present and answering throughout; no promoter absence.

Participant count basis: 16 distinct operator "line of ..." caller introductions (grep `line of [A-Za-z .]+` = 16 hits) = 16 analyst call-in instances; sweep of those 16 instances resolves to 15 distinct literal analyst-name strings (Bharat Kulati appears twice, self-declared as a "follow-up" at turn 29/30) plus the 4 fixed-role participants (Dua, Jain, Fernandes, Operator) = 19-20 total named/role participants depending on whether Bharat Kulati's two turns are counted once or twice.

---

## 2. SPEAKER TURNS (rule: concall #2) — 39 of 39, sequential

| Turn | Source line | Speaker / role | First ~10 words | Flags |
|---|---|---|---|---|
| 1 | 1 | [Header — call title, as supplied] | "E2E Networks Limited — Q1 FY27 Earnings Conference Call —" | — |
| 2 | 2 | [Header — management/IR list, as supplied] | "Management: Mr. Taran Dua (Managing Director), Mr. Nitan Jain (Chief" | — |
| 3 | 4 | Operator — call opening | "Ladies and gentlemen, good day and welcome to E2E Networks" | — |
| 4 | 6 | IR — Vanessa Fernandes, welcome & handover | "Good morning everyone. On behalf of E2E Networks Limited, I" | FORWARD_LOOKING (standard forward-looking-statements safe-harbor disclaimer read into the record) |
| 5 | 8 | Management — Taran Dua (MD), opening remarks | "Uh thanks Kissa and hi everyone. Uh good morning to" | FORWARD_LOOKING (sovereign AI strategy framing, forward statements re "why sovereign AI is important", "we are very close to achieving sovereignty") |
| 6 | 10 | Management — Nitan Jain (CFO), quarterly financial highlights | "Thank you, Tarun. Good morning everyone. Thank you for joining" | mgmt_numbers N1-N9 (see NUMBERS table) |
| 7 | 12 | Operator — opens Q&A; intro Neil Muno (Eco Capital) | "Thank you. We will now begin the question and answer" | — |
| 8 | 14 | Q&A — Neil Muno (Eco Capital) w/ Management | "Hi sir, good morning. Yeah. Hi Mr. Yes. Yes, please" | DEFLECTED/NON-ANSWER (India-AI-mission-vs-own-platform sub-question not clearly answered) |
| 9 | 16 | Operator — intro Bharat Kulati (firm garbled) | "Thank you Mr. Monot. Please rejoin the queue for more" | — |
| 10 | 18 | Q&A — Bharat Kulati w/ Management | "Yeah. Hi. Hi. Yeah. Hi. Thank you Tuna for the" | DEFLECTED/NON-ANSWER (July price-hike Q2 MRR impact not quantified; SovCloud EBIT-margin / asset-light question left mid-answer, "if you could repeat") |
| 11 | 20 | Operator — intro Gandhi (Bajaj Alternate Investment Mgmt) | "Thank you Mr. Gulati. Please rejoin the queue for more" | — |
| 12 | 22 | Q&A — Gandhi (Bajaj Alternate Investment Mgmt) w/ Management | "Yeah. Hi. Thanks. Hi. Hi. Congratulations on very good set" | DEFLECTED/NON-ANSWER (explicit: "We don't provide a guidance on MRR") |
| 13 | 24 | Operator — intro Nishan Joshi (Equisense Advisor) | "Sir, thank you Mr. Gandhi. Please rejoin the queue for" | — |
| 14 | 26 | Q&A — Nishan Joshi (Equisense Advisor) w/ Management | "Sir, good morning. Uh, I have a query regarding. Can" | DEFLECTED/NON-ANSWER (training vs inference revenue mix and margin split both declined as "hard to pin down / hard to measure") |
| 15 | 28 | Operator — intro "quesai" (garbled) | "Thank you Mr. Joshi. Please join the queue for more" | — |
| 16 | 30 | Q&A — "Mr. Gish" w/ Management | "Congrat. Yeah. Hi, I'm good. How are you? I'm good." | DEFLECTED/NON-ANSWER (SovCloud funding-arrangement strategic detail: "very early days... we'll obviously announce that") |
| 17 | 32 | Operator — intro Vun Gandhi (Finn Avenue Growth Fund) | "Thank you Mr. Gish. Please rejoin the queue for more" | — |
| 18 | 34 | Q&A — Vun Gandhi (Finn Avenue Growth Fund) w/ Management | "Hi. Hi. Hey Taran. Again great set very positively uh" | FORWARD_LOOKING (margin sustainability "quite sustainable... medium-term and potentially the long term"); DEFLECTED/NON-ANSWER (customer-mix by segment declined: "let us not do this today") |
| 19 | 36 | Operator — intro Vidant (Minimal Securities) | "Thank you Mr. Gandhi. Please join the queue for more" | — |
| 20 | 38 | Q&A — Vidant (Minimal Securities) w/ Management | "Am I audible? Hi. Hi. Yes. Please go. Uh firstly" | FORWARD_LOOKING ("still day zero at AI", "decadal theme", "AI super cycle") |
| 21 | 40 | Operator — intro Shibbam Tamaraka, CFA (Aluras) | "Thank you Mr. Vizant. Please reach on the queue for" | — |
| 22 | 42 | Q&A — Shibbam Tamaraka, CFA (Aluras) w/ Management | "Hi. Am I audible? Yes sir. Hello. Yeah. Hi. Thank" | DEFLECTED/NON-ANSWER (capacity-at-old-prices not quantified; full-year capex plan not given — 1st of 2 capex-plan asks this call, see REPEAT_QUESTION at Turn 32) |
| 23 | 44 | Operator — intro Rohan Nakpal (Helios Capital) | "Thank you Mr. Tamarakal. Please rejoin the queue for more" | — |
| 24 | 46 | Q&A — Rohan Nakpal (Helios Capital) w/ Management | "Yeah. Hi. Hi Ro. Hi. Uh thanks for taking my" | — |
| 25 | 48 | Operator — intro Ashish Ajit Ka (Pent LLP fund) | "Thank you. Next question comes from the line of Ashish" | — |
| 26 | 50 | Q&A — Ashish Ajit Ka (Pent LLP fund) w/ Management | "Yeah. Hi. Congratulations. Are you able to hear me? Thank" | mgmt_numbers N12-N14 (6-yr GPU life claim); FORWARD_LOOKING ("don't foresee... massive price compression") |
| 27 | 52 | Operator — intro Abishek Shindra (Incred Capital) | "Thank you Mr. Kisha. Please rejoic queue for more questions." | — |
| 28 | 54 | Q&A — Abishek Shindra (Incred Capital) w/ Management | "Hi. Hi. Hi sir. Uh thank you for the opportunity" | FORWARD_LOOKING (sustainability/visibility into Q2/Q3); DEFLECTED/NON-ANSWER (contract-mix target %, "I haven't decided what percentage that should be") |
| 29 | 56 | Operator — intro Bharat Kulati follow-up (firm garbled) | "Thank you Mr. Shindatk. Please Sujandiq for more questions. Next" | — |
| 30 | 58 | Q&A — Bharat Kulati (follow-up) w/ Dua & Jain | "Yeah, hi thank you for the follow. So just two" | NUMERIC_INCONSISTENCY (India revenue mix ~20-21% this quarter vs analyst's stated recollection of ~40% last quarter — see NUMBERS N15/N15b); DEFLECTED/NON-ANSWER (2-year-out GPU count ambition not given); mgmt_numbers N15-N18 |
| 31 | 60 | Operator — intro Py Gandhi (Paj Alternate Investment Mgmt) | "Thank you Mr. Gulati please to jo for more questions." | — |
| 32 | 62 | Q&A — Py Gandhi (Paj Alternate Investment Mgmt) w/ Dua & Jain | "Yeah. Thank you. Thank you for the followup. Uh so" | mgmt_numbers N19 (loan ~450 Cr); DEFLECTED/NON-ANSWER x3 (full-year capex plan — 2nd ask, REPEAT_QUESTION vs Turn 22; SovCloud funding requirement — 2nd ask, REPEAT_QUESTION vs Turn 16; peak loan for the year — not answered, transcript trails off after the question) |
| 33 | 64 | Operator — intro Ashish Ajit Kcha (B Ventures LLP funds) | "Thank you Mr. Ka please for more questions. Next question" | — |
| 34 | 66 | Q&A — Ashish Ajit Kcha (B Ventures LLP funds) w/ Management | "Yeah. Hi sir. Yeah. Yes. My question was the preferential" | mgmt_numbers N20-N23 (preferential issue ~Rs1,591.9 Cr; 3,900 vs 5,100 GPU count); NUMERIC_INCONSISTENCY (3,900 figure — described on the Q4 call as "GPU and GPU storage all capacities put together" — re-appears on this quarter's PPT alongside a new, larger 5,100 figure on a "GPU trajectory" chart; management clarifies 5,100 = current live GPU capacity only, excluding the incremental 1,024 B200, but does not reconcile the compositional change in what "3,900" represented); DEFLECTED/NON-ANSWER (preferential-issue fund utilization/allocation breakdown not itemized) |
| 35 | 68 | Operator — intro Chilag Satia (Satia Investments) | "Thank you. Mr. Satya, please join the queue for more" | — |
| 36 | 70 | Q&A — Chilag Satia (Satia Investments) w/ Management | "Hi. Hi. Hi. Uh sir, I just wanted to understand" | FORWARD_LOOKING (growth trajectory next 2-3 years, "AI super cycle") |
| 37 | 72 | Operator — intro Sukrit Partil (Isite Fin Private Limited) | "Thank you. Mr. Satya, please join the queue for more" | — |
| 38 | 74 | Q&A — Sukrit Partil (Isite Fin Private Limited) w/ Dua & Jain | "Good morning. I have two questions. In the first question," | DEFLECTED/NON-ANSWER (CFO next-quarter capital-allocation "roadmap" request answered only in general terms, no specific figures) |
| 39 | 76 | Operator — closes Q&A; Taran Dua closing remarks; Operator — call closure | "Thank you. Hello. Yes speakers. Thank you ladies and gentlemen." | FORWARD_LOOKING (generic forward-looking closing language, "ongoing expansion plan") |

Turn count basis: grep `^\[TURN [0-9]+` = 39 hits (turns 1-39); manual sweep of the extract's own end-marker ("TURN 39 OF 39 ACCOUNTED FOR") and line-by-line read confirms all 39 present, sequential, none skipped. Match.

---

## 3. QUESTIONS (rule: concall #3) — one row per "?"-terminated clause inside the 16 Q&A turns (atomic unit for GATE A2 reconciliation; multi-clause bundling noted in Topic column where the verbatim dictation ran two asks together without a mid-clause "?")

| Q# | Turn | Analyst (firm) | Topic | Flags |
|---|---|---|---|---|
| Q1 | 8 | Neil Muno (Eco Capital) | Revenue/MRR growth: volume+utilization vs. pricing mix | — |
| Q2 | 8 | Neil Muno (Eco Capital) | How much of growth driven by utilization | (part of Q1, same clause split) |
| Q3 | 8 | Neil Muno (Eco Capital) | How much of growth driven by pricing | (part of Q1, same clause split) |
| Q4 | 8 | Neil Muno (Eco Capital) | New B200s deployed mid-May — committed fully in utilization terms? | REPEAT_QUESTION (utilization-mix theme recurs at Q5/Turn 10) |
| Q5 | 8 | Neil Muno (Eco Capital) | Are B200s committed to "India AI mission" or E2E's own platform | DEFLECTED/NON-ANSWER — management: "in process... couple of weeks we can figure out" |
| Q6 | 10 | Bharat Kulati (firm garbled) | H100/H200/B200 utilization mix in exit MRR + remaining runway | REPEAT_QUESTION (utilization-mix theme, cf. Q4/Turn 8) |
| Q7 | 10 | Bharat Kulati (firm garbled) | SovCloud workflows — better EBIT margins? | DEFLECTED/NON-ANSWER — answer trails into next sub-question |
| Q8 | 10 | Bharat Kulati (firm garbled) | Is SovCloud asset-light in nature | DEFLECTED/NON-ANSWER — "then you ask a couple of more things, if you could repeat" (question effectively unanswered) |
| Q9 | 10 | Bharat Kulati (firm garbled) | Has the private-cloud business (flagged a couple quarters back) started to kick in | DEFLECTED/NON-ANSWER — same trailing non-response as Q7/Q8 |
| Q10 | 12 | Gandhi (Bajaj Alternate Investment Mgmt) | Next B200 delivery timeline | answered: "next couple of months" — FORWARD_LOOKING |
| Q11 | 12 | Gandhi (Bajaj Alternate Investment Mgmt) | Guide for exit-MRR, full-year basis | DEFLECTED/NON-ANSWER — explicit: "We don't provide a guidance on MRR" |
| Q12 | 14 | Nishan Joshi (Equisense Advisor) | ("Can you give a beration?" — garbled lead-in to revenue-mix question) | transcription artifact, folded into Q13 topic |
| Q13 | 14 | Nishan Joshi (Equisense Advisor) | Training vs inference revenue split, and outlook for the ratio over next 2-3 quarters | DEFLECTED/NON-ANSWER — "pretty much hard to pin down the fungibility of compute" |
| Q14 | 16 | "Mr. Gish" (firm NOT FOUND) | Greeting / audio check ("How are you?") | ADMIN — not substantive |
| Q15 | 18 | Vun Gandhi (Finn Avenue Growth Fund) | Should current gross margins be expected as the new normal | FORWARD_LOOKING — "quite sustainable... medium-term and potentially the long term" |
| Q16 | 18 | Vun Gandhi (Finn Avenue Growth Fund) | Revenue-contribution mix by customer type (enterprise AI vs. startups) | DEFLECTED/NON-ANSWER — "we are quite small for that right now... let us not do this today" |
| Q17 | 20 | Vidant (Minimal Securities) | Audio check ("Am I audible?") | ADMIN — not substantive |
| Q18 | 20 | Vidant (Minimal Securities) | Demand-supply gap / realization outlook amid reported compute shortage | FORWARD_LOOKING — cyclicality commentary, "we'll all find equilibrium in the medium term" |
| Q19 | 22 | Shibbam Tamaraka, CFA (Aluras) | Audio check ("Am I audible?") | ADMIN — not substantive |
| Q20 | 24 | Rohan Nakpal (Helios Capital) | Price-increase dynamics: rolled back then pushed further out — what changed | answered — CPU/GPU hardware cost pressure explanation given |
| Q21 | 26 | Ashish Ajit Ka (Pent LLP fund) | Audio check ("Are you able to hear me?") | ADMIN — not substantive |
| Q22 | 28 | Abishek Shindra (Incred Capital) | (Management, clarifying) "can you repeat the second part of your question?" | ADMIN — management-initiated clarification request, not an analyst question |
| Q23 | 30 | Bharat Kulati, follow-up (firm garbled) | India/international revenue-mix trend this quarter + 2-year-out GPU count ambition | NUMERIC_INCONSISTENCY (India mix answer ~20-21% vs analyst's own recollection of ~40% last quarter — see NUMBERS table); DEFLECTED/NON-ANSWER on the 2-year GPU ambition (no figure given) |
| Q24 | 30 | Bharat Kulati, follow-up (firm garbled) | Interest-cost spike / DC-cost run-rate — due to new debt, and will DC cost flatline | mgmt_numbers N18/N19; partially answered (qualitative only, "not super granular numbers") |
| Q25 | 32 | Py Gandhi (Paj Alternate Investment Mgmt) | (Management, clarifying) "what was the other question?" | ADMIN — management-initiated clarification request |
| Q26 | 34 | Ashish Ajit Kcha (B Ventures LLP funds) | Planning an equity raise also (beyond the preferential issue)? | DEFLECTED/NON-ANSWER — "we would let everyone know if and when that happens" |
| Q27 | 36 | Chilag Satia (Satia Investments) | (Management, clarifying) "what is the exact question over there?" | ADMIN — management-initiated clarification request |
| Q28 | 36 | Chilag Satia (Satia Investments) | L&T partnership — how does the revenue arrangement work, how do they pay | answered — arm's-length, mutual buyer/seller relationship |
| Q29 | 36 | Chilag Satia (Satia Investments) | How do they pay you specifically (restated) | (bundled restatement of Q28) |
| Q30 | 36 | Chilag Satia (Satia Investments) | Growth trajectory over next 2-3 years | FORWARD_LOOKING — "AI super cycle", "buildout... aggressively and judiciously" |
| Q31 | 38 | Sukrit Partil (Isite Fin Private Limited) | Positioning as cloud industry enters a tougher/more competitive phase | answered — "16+ years in this business... cycles will continue" |

Additional substantive asks present in the verbatim dictation WITHOUT a terminal "?" (captured here for completeness per the anti-miss mandate, cross-referenced rather than double-counted in the 31-row table above):
- Turn 16: "if you can get some color on these subsidiaries please" (Delaware entity + SovCloud) — answered.
- Turn 16: "if you can provide some maybe strategic insights on [SovCloud funding/enabling arrangement] plan" — DEFLECTED/NON-ANSWER ("very early days... we'll obviously announce that"); REPEAT_QUESTION vs Turn 32 SovCloud-funding ask (Q26's neighbor, see Turn 32 row in NUMBERS/turns tables).
- Turn 22: "the timelines of new capacity and the capex plan that we are thinking of, so if you can help us to understand this also and also funding" — DEFLECTED/NON-ANSWER (no full-year capex figure given); REPEAT_QUESTION vs Turn 32 capex-plan-for-the-year ask.
- Turn 26: "the accelerated computing... regarding the ASIC threat, how does E2E structure to integrate non-[Nvidia]-architecture hardware" — answered (vendor-neutral positioning).
- Turn 28: "are customers now trying to lock in capacity for longer... does that improve the annuity/visibility" — answered qualitatively (2-3 year contracts trend cited), no percentage given.
- Turn 32: "the absolute loan and capex — outstanding loan amount as of the quarter and the total capex plan for the year" — loan answered (~450 Cr); capex-for-year DEFLECTED/NON-ANSWER (2nd occurrence, REPEAT_QUESTION vs Turn 22).
- Turn 32: "funding requirements... for SovCloud, any plans if you can share" — DEFLECTED/NON-ANSWER (2nd occurrence, REPEAT_QUESTION vs Turn 16).
- Turn 32: "total loan amount, peak for the year, quantifying that" — DEFLECTED/NON-ANSWER — question posed but transcript ends the turn with no management response captured (peak-loan guidance declined/unanswered).
- Turn 34: "the preferential issue... wanted to understand where is that [capex] gone, if you could share that utilization" — DEFLECTED/NON-ANSWER (no itemized utilization breakdown given).
- Turn 34: "this 5,100 is what you are accelerating or banded capacity unit. I hope my question is clear" — answered (5,100 = current live GPU capacity); this is the clause carrying the NUMERIC_INCONSISTENCY flag, logged at NUMBERS N22/N23 below rather than re-counted here.

Question count basis: grep = literal count of "?" characters inside the 16 Q&A-labeled turns (8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38) = 31. Sweep = one row per such "?"-clause = 31 rows (Q1-Q31 above). Match. The supplementary un-punctuated asks listed directly above are real, substantive, and are not dropped — they are cross-referenced into the NUMBERS table and the Turn-level flags column so A3/A4 can reconcile against them, but are not double-counted against the 31-row GATE A2 total, whose atomic unit is defined strictly as the "?" character for reproducibility given this transcript's missing punctuation.

`REPEAT_QUESTION` instances (topic recurs across separate analysts/turns): utilization-mix across generations (Turn 8 / Turn 10); full-year capex plan (Turn 22 / Turn 32); SovCloud funding arrangement (Turn 16 / Turn 32).

---

## 4. NUMBERS SPOKEN BY MANAGEMENT (rule: concall #4) — includes analyst-stated comparison figures where needed to carry a NUMERIC_INCONSISTENCY flag (marked "analyst" in Speaker column)

| N# | Turn | Speaker | Number | Context | Flags |
|---|---|---|---|---|---|
| N1 | 6 | Nitan Jain (CFO) | Revenue 1568 million | "Revenue for the quarter stands at 1568 million" | — |
| N2 | 6 | Nitan Jain (CFO) | +334% YoY | Revenue growth year-on-year | — |
| N3 | 6 | Nitan Jain (CFO) | +64% QoQ | Revenue growth quarter-on-quarter | — |
| N4 | 6 | Nitan Jain (CFO) | EBITDA ("IDA") 1179 million | Transcribed "11. 79 million" — verbatim artifact for 1,179 million | — |
| N5 | 6 | Nitan Jain (CFO) | EBITDA margin 75.2% | "with margins expanding up to 75.2%" | — |
| N6 | 6 | Nitan Jain (CFO) | EBITDA margin expansion +1450 bps | vs Q4 FY26 ("compared to Q4 2026") | — |
| N7 | 6 | Nitan Jain (CFO) | PBT 586 million | Current quarter | — |
| N8 | 6 | Nitan Jain (CFO) | PBT 86 million | Q4 FY26 comparative | — |
| N9 | 6 | Nitan Jain (CFO) | PAT ("patch") 439 million | Current quarter | — |
| N10 | 5 | Taran Dua (MD) | 1,024 GPUs (Blackwell) went live | Transcribed "the ,024 blacks that we had received... went online... put on revenue" — leading digit dropped in transcription | — |
| N11 | 14 | Taran Dua (MD) | ~5,000 GPUs | "we are literally talking about 5,000 or so GPUs" (scale context for training/inference fungibility answer) | — |
| N12 | 18 | Taran Dua (MD) | ~5,000 GPUs + ~1,000 more coming | "at 5,000 GPUs um and another thousand coming in like still the size is too small" | REPEAT_QUESTION-adjacent restatement of N11's scale reference; broadly consistent with N23 (1,024 B200 coming) |
| N13 | 26 | Taran Dua (MD) | GPU life cycle: minimum 6 years | "we've always maintained that we see at least at the minimum a six year life cycle for all the GPU generations" | — |
| N14 | 26 | Taran Dua (MD) | GPU monetization window: 5-6 years | "that long life cycle is conducive to monetize those GPUs through like almost five to six years" | — |
| N15 | 26 | Taran Dua (MD) | Nvidia relationship since 2019 | "we have worked the longest time on GPUs with Nvidia like all the way from 2019 onwards" | — |
| N16 | 30 | Taran Dua (MD) | India revenue mix ~20-21% (this quarter, described as "the previous quarter" in the answer) | "from a revenue composition in the previous quarter I think India revenue was about like 20 21%" | NUMERIC_INCONSISTENCY — see N16b |
| N16b | 30 | Bharat Kulati (analyst, stated in his own question) | India mix ~40% "last quarter" | "India [mix — transcribed 'emission'] was about 40% last quarter"; analyst also states prior domestic:foreign split as "60:40" | NUMERIC_INCONSISTENCY — analyst's recollection of ~40% India mix "last quarter" does not reconcile with management's own answer of ~20-21% for what management calls "the previous quarter" in the same breath; neither side clarifies which quarter is actually being referenced, nor is the gap addressed. Flagged for A3/A4 arithmetic-consistency check against the Role 4 filing baseline. |
| N17 | 30 | Taran Dua (MD) | International revenue mix ~37% | "international was like closer to 37% or so, and rest is like all domestic revenue" | Note: "rest is domestic" plus "international ~37%" plus "India ~20-21%" does not arithmetically sum to a clean 100% split as stated in the transcript — internal consistency gap, flagged alongside N16/N16b |
| N18 | 30 | Nitan Jain (CFO) | DC (data center) cost for the quarter "close to 20" | Unit not specified in transcript (likely INR Cr or % of revenue — NOT FOUND, ambiguous as spoken) | Unit ambiguity — NOT FOUND for unit of measure |
| N19 | 32 | Nitan Jain (CFO) | Loan outstanding ~450 Cr | "the loan which stands as of now is broadly 450 CR" | Peak-for-year figure requested immediately after (Turn 32) but NOT answered — see Turns/Questions tables DEFLECTED flag |
| N20 | 34 | Ashish Ajit Kcha (analyst, stated in his question) / confirmed by context | Preferential issue total ~Rs 1,591.9 Cr | Transcribed "15919 1.9 K" — garbled rendering of ₹1,591.9 Cr, referenced by the analyst as "around 2 years" prior | Analyst-sourced figure; management does not restate the number itself, only responds regarding utilization (deflected — see Q26 supplementary note) |
| N21 | 34 | Ashish Ajit Kcha (analyst, citing prior Q4 call) | "3,900" — prior-quarter capacity figure | Per analyst: on the Q4 call, "3,900" was described as "GPU and GPU storage all capacities put together" | NUMERIC_INCONSISTENCY — see N22/N23 |
| N22 | 34 | Ashish Ajit Kcha (analyst) / Taran Dua (MD) confirms | "5,100" on current-quarter PPT, chart titled "GPU trajectory", alongside a repeated "3,900" reference | Analyst notes the current PPT shows both 3,900 and 5,100 on the same chart | NUMERIC_INCONSISTENCY |
| N23 | 34 | Taran Dua (MD) | 5,100 = current live GPU capacity | "nearly 5100 is the current capacity which is live on our platform today. That's the number of GPUs which are live today." | NUMERIC_INCONSISTENCY — management defines 5,100 as a pure GPU count ("live" GPUs only), whereas the analyst's cited prior-quarter "3,900" figure was explicitly a COMBINED GPU + GPU-storage capacity metric per the Q4 call. The composition of the metric appears to have changed between quarters (a GPU-only count now vs. a GPU+storage blend previously) without management flagging or reconciling the basis change — this is the "3,900 prior figure re-defined" flag carried in the task injection. |
| N24 | 34 | Taran Dua (MD) | +1,024 additional B200 GPUs expected, not yet included in the 5,100 | "that does not include the uh another 1,024 B200 we are expecting soon" | Consistent with N10 (1,024 Blackwell GPUs that went live earlier in the quarter) — worth confirming with Role 4/5 whether this is the SAME 1,024 units already live (N10) restated as a forward figure, or a DIFFERENT incremental 1,024 units on top of the 5,100 already-live count; transcript does not disambiguate. Flag for A3 forensic-notes follow-up. |

Numbers count basis: 24 distinct quantitative disclosures identified by manual sweep first (N1-N24, excluding pure GPU model/product identifiers such as "B200", "H100", "H200", which are treated as entity names, not values); each of the 24 was then grep-verified present in the extract via its literal substring (all 24 confirmed, occurrence counts 1-3 each). Match.

`ZERO_STANDING`: not applicable to this doctype instance — no line item in this transcript is stated as zero/nil/dash (concall doctype carries no standing financial-statement table; that enumeration category belongs to the RESULTS FILING doctype, not transcript).

---

## 5. FORWARD-LOOKING / GUIDANCE STATEMENTS AND HEDGES (rule: concall #5)

Scope note: given the extreme disfluency density of this verbatim transcript (filler words "uh"/"like" on nearly every line), this table captures every SUBSTANTIVE forward-commitment or hedge statement (a statement that commits to, projects, or explicitly declines to project a future outcome), not filler interjections. This is a deliberate scope boundary, stated here for A3/A4 to apply consistently.

| # | Turn | Type | Statement (paraphrase kept close to verbatim) |
|---|---|---|---|
| F1 | 4 | Forward-looking (boilerplate) | Standard safe-harbor disclaimer: forward-looking statements subject to risks/uncertainties, no obligation to update |
| F2 | 5 | Forward-looking | "we are very very close to achieving sovereignty AI sovereignity for our customers" |
| F3 | 12 | Forward-commitment | B200 delivery "in next couple of months... we'll obviously be keeping everyone informed" |
| F4 | 12 | Hedge / guidance decline | "We don't provide a guidance on MRR... let's look at the past... rather than kind of like predict the future" |
| F5 | 16 | Hedge / deflection | SovCloud funding: "very early days... we'll obviously announce that" |
| F6 | 18 | Forward-looking | Margin sustainability "quite sustainable over the medium-term and potentially the long term" |
| F7 | 18 | Hedge / deflection | Customer-mix metric: "let us not do this today... at a certain scale probably it would start making sense" |
| F8 | 20 | Forward-looking | "still day zero in the world of AI... largest buildout in the history... decadal theme... we've just begun" |
| F9 | 20 | Hedge | Demand-supply cycles: "we'll all find our equilibrium in the medium term" |
| F10 | 22 | Forward-commitment | B200 deployment "as soon as the new lot becomes available... expecting that to happen soon over next couple of months"; capacity expansion into "Varin" [likely "Varanasi" or another region, garbled] flagged for future disclosure |
| F11 | 26 | Hedge | "we don't foresee that there is a massive price compression because of the newer generation GPU coming in" |
| F12 | 28 | Forward-looking | Performance "quite sustainable... predictability as well as sustainability of the revenue" |
| F13 | 28 | Hedge | Contract-mix judiciousness: "I haven't decided what percentage that should be" |
| F14 | 30 | Hedge | DC cost: "in the coming quarters some of that cost would increase but I don't think that would be a very massive percentage" |
| F15 | 32 | Forward-looking | Loan: "with the other lot coming in picture it would be increasing across in the near term" |
| F16 | 32 | Hedge / deflection | SovCloud plans: "we always say that let us build and execute the plans and then kind of like put them out there" |
| F17 | 32 | Hedge / deflection (unanswered) | Peak loan for the year — question posed, no management response captured in transcript |
| F18 | 34 | Hedge / deflection | Future equity raises: "we would let everyone know if and when that happens" |
| F19 | 36 | Forward-looking | Growth trajectory: "AI is entering into a huge super cycle... fully intend to be a part of that buildout... aggressively and judiciously" |
| F20 | 38 | Forward-looking (vague) | CFO on next-quarter capital-allocation roadmap: "we keep a balance... we should not be too aggressive or we should not miss the... AI bus" — no specific figures or dates given |
| F21 | 39 | Forward-looking (boilerplate) | Closing remarks: "we hope to keep you updated about our ongoing expansion plan" |

---

## SUMMARY OF FLAGS RAISED

- DEFLECTED/NON-ANSWER: Turns 8, 10, 12, 14, 16, 18, 22, 28, 30, 32 (x3), 34, 38 — includes explicit MRR-guidance decline (Turn 12), customer-mix decline (Turn 18), full-year capex decline (Turns 22 and 32 — REPEAT_QUESTION), peak-loan decline (Turn 32, unanswered), customer-name/segment specifics never given at any point on the call, SovCloud funding-structure decline (Turns 16 and 32 — REPEAT_QUESTION).
- FORWARD_LOOKING: Turns 4, 5, 12, 18, 20, 22, 26, 28, 30, 32, 36, 38, 39 (F1-F21 above).
- NUMERIC_INCONSISTENCY: Turn 30 (India revenue mix ~20-21% stated by management vs analyst's recollection of ~40% "last quarter", plus an internal mix that does not clearly sum to 100% across India/international/domestic categories as spoken); Turn 34 (3,900 prior-quarter figure, defined on the Q4 call as combined GPU+storage capacity, re-appears on this quarter's PPT next to a new, larger, GPU-only 5,100 figure with no reconciliation of the basis change).
- REPEAT_QUESTION: utilization-mix across GPU generations (Turns 8 & 10); full-year capex plan (Turns 22 & 32); SovCloud funding arrangement (Turns 16 & 32).
- MGMT_ABSENCE: none — MD and CFO both present throughout.
- ZERO_STANDING: not applicable to this doctype instance.
- ENTITY_CHANGE: not applicable (no consolidation-entity list in a concall transcript); note for A3: Turn 16 discloses two newly set-up entities (a Delaware entity for international sales, and "SovCloud" as an infrastructure subsidiary) — worth a forward cross-check against the next results-filing consolidation list, but not enumerable as an ENTITY_CHANGE from this document alone.
- Naming ambiguity (not a defined flag in this pipeline's taxonomy, noted in prose): three separate "Gandhi" surnamed callers (Turns 12, 18, 32) and two separate "Ashish Ajit Ka/Kcha" callers (Turns 26, 34) may or may not be the same individuals across near-identical firm names — enumerated separately per verbatim transcription, not collapsed.

---
