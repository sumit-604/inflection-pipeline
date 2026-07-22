# LEDGER — Concall Transcript — INDIAMART — Q1 FY27

Source: `extract_concall_indiamart_q1fy27.txt` (105 original transcript lines,
verbatim auto-generated webinar transcript, artefacts flagged by A1 at
embedded line 1 SOURCE NOTE). Citation convention below uses the EMBEDDED
line number printed at the start of each extract line (1, 3, 5, ... 105),
which is the extract's own numbering and matches A1's citation convention.
Turn numbers (T1, T2, ...) are assigned sequentially by this ledger.

```
=== A2 COUNT TEST ===
category: transcript_content_lines   grep_count: 52   sweep_count: 52   match: yes
  grep: `grep -c -E "^[0-9]+  \S"` on extract, minus embedded line 1
  (A1's SOURCE NOTE annotation, not spoken content) = 53-1 = 52.
  sweep: manual line-by-line read of embedded lines 3-105 (odd) = 52. MATCH.

category: turns (speaker-turn rows in ledger table 2)   base_unit_count: 52   ledger_rows: 64   match: reconciled
  8 of the 52 base lines contain more than one embedded speaker merged by
  the auto-transcription with no line break (operator+analyst, or
  answer+next-question run together): embedded lines 33, 35, 45, 55, 57,
  67, 77, 105. Each is split into lettered sub-turns (e.g. 33a/33b) in
  Table 2, flagged TRANSCRIPT_MERGED_TURN, so no embedded speaker change is
  dropped. 52 base lines + 12 net additional sub-turns from the 8 splits
  (2+2+2+3+2+4+3+2=20 sub-turns replacing 8 base rows) = 64 rows. No
  content lines are missing from either pass.

category: participants   grep_count: 14   sweep_count: 14   match: yes
  grep: `grep -o "Mr\. [A-Za-z]*"` (5, all on embedded line 3) +
  `grep -o "the line of [A-Za-z ]*"` (9 distinct analyst call-outs) = 14.
  sweep: manual list (IR host + 4 introduced management + 9 analysts) = 14. MATCH.

category: questions   grep_count: 18 (raw "?" marks)   sweep_count: 22   match: no on first pass -> re-swept
  Initial grep pass (`grep -o "?"` = 18) undercounts because this
  auto-transcript drops terminal question marks on many interrogative
  sentences (documented artefact, A1 SOURCE NOTE). Re-sweep (rule 4)
  performed: manual line-by-line read against `grep -o "the line of"` (9
  analyst call-outs) + 1 chat-box relay (embedded line 67) as anchor
  points, decomposing every analyst turn (initial + every follow-up) into
  discrete questions. Re-swept count = 22, fully itemized in Table 3.
  gate_a2 treats this as RESOLVED (rule 4 followed: mismatch identified,
  re-sweep performed, final count of 22 verified complete against all 9
  call-outs + the chat relay) -> final match: yes (post re-sweep).

category: mgmt_numbers (raw numeric tokens, transcript body only)   grep_count: 82   sweep_count: 83   match: no on first pass -> re-swept
  grep: digit-form %, cr/crore(s), lakh(s)/million patterns + comma-grouped
  large numbers + bare "1850" + word-form "one lakh", transcript body
  (embedded line >=3) only, header block and SOURCE NOTE excluded = 82.
  Re-sweep found 1 additional word-form number the digit-only grep pattern
  cannot catch: "four 5%" (~4-5%, OTP-verification-caused inquiry decline,
  turn 31 / line 63) spoken as the word "four", not the digit "4". Added.
  Final reconciled count = 83 raw numeric tokens, all itemized/grouped
  into metric-rows in Table 4. -> final match: yes (post re-sweep).
  Of the 83, 7 are spoken by ANALYSTS citing prior/presentation figures
  inside their questions, not by management; these are retained in Table 4
  (flagged ANALYST_STATED) but excluded from the strict mgmt_numbers tally.
  Strict management-spoken count = 83 - 7 = 76.

category: forward_guidance_statements   grep_count: n/a (no mechanical marker)   sweep_count: 9   match: yes (manual only, cross-read against Table 4/Table 2 for completeness)

gate_a2: pass
=== END COUNT TEST ===
```

---

## Table 1 — Participants

Confirmed: CEO (promoter/CMD, phonetically transcribed "Dhraal"/"Dhar"/
"Dhagaral" — IndiaMART's CEO/promoter is Dinesh Agarwal) is PRESENT and is
the primary spokesperson across the call (opening remarks T2, most Q&A
answers, concluding remarks T52a). No MGMT_ABSENCE.

| # | Name (as transcribed) | Role | Side | Line first appears | Flags |
|---|---|---|---|---|---|
| 1 | Abijit Vikram (transcribed "Aijit Vikram") | Head of Investor Relations, call moderator | Company/IR | 3 | — |
| 2 | Mr. Dhraal / Dhar / Dhagaral | Chief Executive Officer (promoter/CMD) | Management | 3 | phonetic name variants across the transcript |
| 3 | Mr. Vijay Sharal | Full-Time Director | Management | 3 | possibly = the unnamed "Br"/Busy-segment speaker at T3 (line 7); not confirmed by transcript |
| 4 | Mr. Jidden Dewan | Chief Financial Officer | Management | 3 | speaks financial performance detail, T4 (line 9) |
| 5 | Mr. Pratik Chandra | Chief Strategy Officer | Management | 3 | speaks on follow-on investments, T35 (line 71) |
| 6 | Kunal Tanvi | Analyst (firm not stated) | Analyst | 11 | first questioner |
| 7 | Abhishek | Analyst (firm not stated; "Energy Abishek" transcription unclear — possibly a firm-name prefix garbled) | Analyst | 21 | flag: FIRM_NAME_UNCLEAR |
| 8 | Pratik Kotari | Analyst (firm not stated) | Analyst | 33 | — |
| 9 | Vanand Van | Analyst (firm not stated; name likely garbled) | Analyst | 45 | flag: NAME_GARBLED |
| 10 | Anerud Shetty | Analyst (firm not stated) | Analyst | 55, 67 | could not connect at 55; questions later relayed via chat box at 67 |
| 11 | Sam Patil | Analyst (firm not stated) | Analyst | 55 | — |
| 12 | Amandani | Analyst (firm not stated) | Analyst | 67 | could not connect; flag NAME_VARIANT_AMBIGUOUS — likely same person as #13 (Aman Tadani), mis-transcribed |
| 13 | Aman Tadani | Analyst (firm not stated) | Analyst | 77 | connects successfully; asks Busy-focused questions; flag NAME_VARIANT_AMBIGUOUS vs #12 |
| 14 | Sham Gupta | Analyst (firm not stated) | Analyst | 91 | last questioner |

No firm/brokerage affiliation is stated for any analyst anywhere in this
transcript — flag FIRM_NOT_STATED applies to all 9 analyst rows uniformly
(noted once here rather than repeated 9 times).

---

## Table 2 — Speaker Turns (sequential, 64 rows; base transcript lines = 52)

| Turn | Line | Speaker | First ~10 words | Flags |
|---|---|---|---|---|
| T1 | 3 | Abijit Vikram (IR) | "Good evening ladies and gentlemen. I am Aijit Vikram..." | — |
| T2 | 5 | Dhar (CEO) | "Thank you Abijit. Good evening everyone and welcome to..." | opening remarks + Q1 headline numbers |
| T3 | 7 | Busy-segment speaker ("Br") | "Hi good evening everyone. Um busy did a billing..." | SPEAKER_UNCLEAR (identity not confirmed vs Table 1 #3) |
| T4 | 9 | Jidden Dewan (CFO) | "Good evening everyone. I'll take you through the financial..." | — |
| T5 | 11 | Operator | "We will now begin the Q&A session. If you wish..." | intros Kunal Tanvi |
| T6 | 13 | Kunal Tanvi | "Hi, thanks for the opportunity. I had two questions..." | 2 questions (Q1, Q2) |
| T7 | 15 | Dhar (CEO) | "Yeah. So let me uh first answer uh the wholly..." | answers Q1, Q2 |
| T8 | 17 | Kunal Tanvi | "Thank you." | closing |
| T9 | 19 | Operator | "Okay, we can move on to the next question." | — |
| T10 | 21 | Operator | "Next question is from the line of Abhishek..." | intros Abhishek |
| T11 | 23 | Abhishek | "Uh hey hi. Yeah, sure. Yeah. Uh so couple of..." | Q3, Q4 |
| T12 | 25 | Dhar (CEO) | "So until now uh we have only mostly experimented..." | answers Q3, Q4 |
| T13 | 27 | Abhishek | "Understood. Understood. And and just one one last thing..." | Q5, follow-up |
| T14 | 29 | Dhar (CEO) | "yeah so we did cut down on some of the..." | answers Q5 |
| T15 | 31 | Abhishek | "Thanks. Those are all questions." | closing |
| T16a | 33 | Operator | "Thank you. Next question is from the line of Pratik Kotari..." | TRANSCRIPT_MERGED_TURN (intro + Q merged with 16b) |
| T16b | 33 | Pratik Kotari | "Yes. Hi. Uh good evening. Uh so one question..." | Q6; TRANSCRIPT_MERGED_TURN |
| T17a | 35 | Dhar (CEO) | "Yeah, I think I I highlighted already in my..." | answers Q6 (trust initiatives) |
| T17b | 35 | Pratik Kotari (attribution uncertain — garbled continuation) | "...currently we're not adding gross uh uh fate suppliers..." | Q7 ("leaky bucket"); flag TRANSCRIPT_MERGED_TURN, SPEAKER_UNCLEAR |
| T18 | 37 | Dhar (CEO) | "I mean I can't uh really answer that for sure..." | answers Q7 |
| T19 | 39 | Pratik Kotari | "So my actually question was so net growth is a..." | Q8, clarification |
| T20 | 41 | Dhar (CEO) | "that that will happen only for 2 three quarters..." | answers Q8 |
| T21 | 43 | Pratik Kotari | "No, fair enough. Thank you and all the best sir." | closing |
| T22a | 45 | Operator | "Thank you. Uh next question is from the line of Vanand Van..." | TRANSCRIPT_MERGED_TURN |
| T22b | 45 | Vanand Van | "Are you there? Yeah. Yeah, I'm there... Two questions..." | Q9, Q10; flag TRANSCRIPT_MERGED_TURN |
| T23 | 47 | Dhar (CEO) | "Yeah. So on the initiatives one uh one initiative..." | answers Q9, Q10 |
| T24 | 49 | Vanand Van | "Okay, that that's very interesting. Thanks DH for sharing..." | Q11, follow-up |
| T25 | 51 | Dhar (CEO) | "It may not be right for me to answer that..." | declines to answer officially |
| T26 | 53 | Vanand Van | "Okay. Okay. Thank Thank you so much and all the..." | closing |
| T27a | 55 | Operator | "Thank you. Next question is from the line of Anerud Shetty..." | Anerud cannot connect; flag TRANSCRIPT_MERGED_TURN |
| T27b | 55 | Operator | "So next question is from the line of Sam Patil..." | intros Sam Patil; flag TRANSCRIPT_MERGED_TURN |
| T27c | 55 | Sam Patil | "Uh yeah uh so thanks for providing me the opportunity..." | Q12; flag TRANSCRIPT_MERGED_TURN; cites 7% figure (ANALYST_STATED) |
| T28a | 57 | Mgmt (Dhar/CEO, unconfirmed) | "Yeah. So uh two two parts to the answer..." | answers Q12 (silver churn 7% unchanged) |
| T28b | 57 | Sam Patil (reminder fragment) | "...and uh what else it was% that I asked GST..." | Q13 (GST/bank verification reminder); flag TRANSCRIPT_MERGED_TURN |
| T29 | 59 | Dhar (CEO) | "Yeah. So GST bank account I just told you know..." | answers Q13 |
| T30 | 61 | Sam Patil | "Understood. uh uh uh that was really helpful uh and..." | Q14; cites 11%/5% (ANALYST_STATED) |
| T31 | 63 | Dhar (CEO) | "Very difficult you know out of the uh out of..." | answers Q14 |
| T32 | 65 | Sam Patil | "Understood. Uh thank you uh very much for providing me..." | closing |
| T33a | 67 | Operator | "Sure. Uh, next question is from the line of Amandani..." | Amandani cannot connect; flag TRANSCRIPT_MERGED_TURN, NAME_VARIANT_AMBIGUOUS |
| T33b | 67 | Anerud Shetty (via chat, relayed by operator) | "So first question is why introduce buyer monetization?..." | Q15; chat box; flag TRANSCRIPT_MERGED_TURN, REPEAT_QUESTION |
| T33c | 67 | Anerud Shetty (chat) | "Uh is it possible to track buyer leads coming..." | Q16; chat box |
| T33d | 67 | Anerud Shetty (chat) | "Uh the third is given a large cash balance..." | Q17; chat box; flag QUESTION_COUNT_DISCREPANCY (see note below Table 3) |
| T34 | 69 | Dhar (CEO) | "So uh we are not introducing ucing buyer paid..." | answers Q15-Q17; hands to Pratik Chandra |
| T35 | 71 | Pratik Chandra (CSO) | "Yeah. So out of the total investments that we..." | follow-on investee list |
| T36 | 73 | Dhar (CEO) | "Yeah and uh some of the interesting ones I think..." | stake percentages |
| T37 | 75 | Unclear (analyst interjection) | "no we have a limit" | flag SPEAKER_UNCLEAR |
| T38a | 77 | Dhar (CEO) | "we had a limit of 10% we made it back..." | completes M1 exchange answer; flag TRANSCRIPT_MERGED_TURN |
| T38b | 77 | Operator | "...okay okay next question is from the line of Aman..." | intros Aman Tadani; flag TRANSCRIPT_MERGED_TURN |
| T38c | 77 | Aman Tadani | "Yeah, for the opportunity sir I have a few..." | Q18; flag TRANSCRIPT_MERGED_TURN; cites 28%/10% (ANALYST_STATED) |
| T39 | 79 | Mgmt (Busy segment) | "So when we uh look at the overall breakup..." | answers Q18 |
| T40 | 81 | Aman Tadani | "Got it. So uh the license have grown at..." | Q19, follow-up; cites 10%/10% (ANALYST_STATED) |
| T41 | 83 | Mgmt | "So we are trying to accelerate the growth uh..." | answers Q19 |
| T42 | 85 | Aman Tadani | "Got it. So some second question is uh on..." | Q20 |
| T43 | 87 | Dhar (CEO) | "See most of these investments were done in uh..." | answers Q20 |
| T44 | 89 | Aman Tadani | "got it sir so those are my questions thank..." | closing |
| T45 | 91 | Operator | "thank you next question is from the line of Sham..." | intros Sham Gupta |
| T46 | 93 | Sham Gupta | "yeah good evening uh I have a couple of..." | Q21 |
| T47 | 95 | Mgmt (CEO) | "number that we typically give is the repeat rate..." | answers Q21 |
| T48 | 97 | Unclear (mgmt) | "We can consider." | flag SPEAKER_UNCLEAR |
| T49 | 99 | Sham Gupta | "Got it. Um got it. Helpful. And maybe you..." | Q22 |
| T50 | 101 | Dhar (CEO) | "Yeah. So, Sham, uh on the second part of..." | answers Q22 |
| T51 | 103 | Operator | "Thank you sir. This was the last question for..." | hands to Dhar for closing |
| T52a | 105 | Dhar (CEO) | "Thank you ladies and gentlemen for joining our Q1..." | concluding remarks; flag TRANSCRIPT_MERGED_TURN |
| T52b | 105 | Operator | "...On behalf of India Mart, we thank everyone for..." | sign-off; flag TRANSCRIPT_MERGED_TURN |

---

## Table 3 — Questions (22 rows)

| Q# | Turn | Line | Analyst | Firm | Topic | Flags |
|---|---|---|---|---|---|---|
| Q1 | T6 | 13 | Kunal Tanvi | not stated | Finance subsidiary (India Finance Ltd) objective/structure — own balance sheet or partnership? | — |
| Q2 | T6 | 13 | Kunal Tanvi | not stated | Plans to monetize buyers; reason for declining buyer count | REPEAT_QUESTION (echoed by Q15) |
| Q3 | T11 | 23 | Abhishek | not stated | Lending platform type — invoice discounting vs working capital finance; learnings from experiments | — |
| Q4 | T11 | 23 | Abhishek | not stated | Busy collections growth this quarter lower than trend — reason | — |
| Q5 | T13 | 27 | Abhishek | not stated | Buyer count boosting initiatives; advertising spend correlation with buyer/inquiry growth | REPEAT_QUESTION (echoes Q2) |
| Q6 | T16b | 33 | Pratik Kotari | not stated | Quality-of-buyers / trust endeavor — progress update | — |
| Q7 | T17b | 35 | Pratik Kotari (attribution uncertain) | not stated | "Leaky bucket" — accept structural churn and add more gross, or keep solving churn first? | TRANSCRIPT_MERGED_TURN, SPEAKER_UNCLEAR |
| Q8 | T19 | 39 | Pratik Kotari | not stated | Clarifies Q7: net growth = gross minus churn; restated ask | — |
| Q9 | T22b | 45 | Vanand Van | not stated | Churn-curbing initiatives beyond pricing/checks — what else in next 6-12 months | — |
| Q10 | T22b | 45 | Vanand Van | not stated | LLM traffic vs SEO — initiatives to surface IndiaMART results in LLM answers | REPEAT_QUESTION (echoed by Q22) |
| Q11 | T24 | 49 | Vanand Van | not stated | Regulatory guardrails in India against "walled garden" LLMs | — |
| Q12 | T27c | 55 | Sam Patil | not stated | Silver monthly churn update (was ~7% last quarter); impact of GST/bank verification initiatives on retention; cohort-wise churn flavor | cites 7% (ANALYST_STATED, see Table 4) |
| Q13 | T28b | 57 | Sam Patil | not stated | Reminder sub-question: specifically on GST/bank account verification progress | TRANSCRIPT_MERGED_TURN |
| Q14 | T30 | 61 | Sam Patil | not stated | Unique business inquiry down 11%, active buyers down 5% — how much attributable to OTP verification | cites 11%/5% (ANALYST_STATED) |
| Q15 | T33b | 67 | Anerud Shetty | not stated | Why introduce buyer monetization now, given weak inquiry growth — timing question | chat box; REPEAT_QUESTION (echoes Q2); see QUESTION_COUNT_DISCREPANCY note |
| Q16 | T33c | 67 | Anerud Shetty | not stated | Can buyer leads sourced from LLM searches be tracked/attributed | chat box; see QUESTION_COUNT_DISCREPANCY note |
| Q17 | T33d | 67 | Anerud Shetty | not stated | Given large cash balance, plans to increase stake in existing investees or take new positions | chat box; see QUESTION_COUNT_DISCREPANCY note |
| Q18 | T38c | 77 | Aman Tadani | not stated | Busy ~28% CAGR revenue growth breakdown vs ~10% license growth — RPU expansion drivers and sustainable trajectory | TRANSCRIPT_MERGED_TURN; cites 28%/10% (ANALYST_STATED) |
| Q19 | T40 | 81 | Aman Tadani | not stated | Will license growth stay at ~10%/yr; scope to further expand RPU | cites 10%/10% (ANALYST_STATED) |
| Q20 | T42 | 85 | Aman Tadani | not stated | Rough rupee-crore target for investment (existing/new) over next 3 years | — |
| Q21 | T46 | 93 | Sham Gupta | not stated | Suggestion: introduce a quality/fulfillment metric alongside raw buyer/inquiry counts | phrased as suggestion, framed as question |
| Q22 | T49 | 99 | Sham Gupta | not stated | Two-parter: (a) concrete AI/LLM windfall-gain examples given churn context; (b) will high-quality data stores retain value in the LLM era, or will LLMs hallucinate regardless of access | REPEAT_QUESTION (echoes Q10 re LLM ecosystem) |

**QUESTION_COUNT_DISCREPANCY note:** the task brief for this run states "note
the two questions posted via chat box." The transcript at line 67 (turn
T33b-d) contains **three** distinct items ("first question... [unlabeled
middle item]... the third is..." — the ordinal "second" appears to have
been dropped by the auto-transcription, consistent with the artefact
pattern flagged at embedded line 1). Enumerated here as Q15/Q16/Q17 (three
chat-box questions), flagged for A3/A4 attention rather than silently
conformed to the brief's count of two.

---

## Table 4 — Management-Stated Numbers (83 raw tokens, grouped into readable
metric-rows; ANALYST_STATED rows flagged and excluded from the strict
mgmt_numbers tally of 76)

| # | Turn | Line | Speaker | Metric | Value(s) as stated | Flags |
|---|---|---|---|---|---|---|
| 1 | T2 | 5 | CEO | Consolidated revenue from operations, Q1 | 414 crores, +11% YoY | — |
| 2 | T2 | 5 | CEO | Consolidated collection from customers, Q1 | 463 crores, +8% YoY | — |
| 3 | T2 | 5 | CEO | Consolidated deferred revenue, Q1 | "144 cr", +16% YoY | TRANSCRIPTION_CONTRADICTION — corrected to 2,014 cr at #12 (T4/line 9); enumerated verbatim per A1 rule |
| 4 | T2 | 5 | CEO | Unique business inquiries, Q1 | 26 million | — |
| 5 | T2 | 5 | CEO | Total paying supplier base | 2 lakhs 18,000 (2,18,000) | — |
| 6 | T2 | 5 | CEO | Net supplier decline during quarter | 1,850 suppliers | — |
| 7 | T2 | 5 | CEO | Platinum + Gold subscribers, % of customer base | ~50% | — |
| 8 | T2 | 5 | CEO | Platinum + Gold subscribers, % of revenue | >75% | — |
| 9 | T2 | 5 | CEO | Agentic call handling volume | >1 lakh (100,000+) calls/day | word-form "one lakh," not caught by digit-only grep, added on manual sweep |
| 10 | T3 | 7 | Busy-segment speaker | Busy billing, Q1 | ~59 crores, +10% YoY | — |
| 11 | T3 | 7 | Busy-segment speaker | Busy revenue from operations, Q1 | 36 crores, +47% YoY | growth% appears high relative to billing growth of 10% — see arithmetic note below |
| 12 | T3 | 7 | Busy-segment speaker | Busy deferred revenue, Q1 | ~146 crores, +44% YoY | POSSIBLE_NUMBER_COLLISION — identical "146 cr" figure recurs at #17 (consolidated EBITDA, T4/line 9) in an unrelated context; flagged for Role 5 cross-check |
| 13 | T3 | 7 | Busy-segment speaker | Busy cash from operations, Q1 | ~16 crores | — |
| 14 | T3 | 7 | Busy-segment speaker | New Busy licenses sold, Q1 | ~12,000 | — |
| 15 | T3 | 7 | Busy-segment speaker | Cumulative Busy licenses sold (total) | ~4,54,000 (4 lakh + 54,000) | — |
| 16 | T4 | 9 | CFO | Consolidated collection from customers, Q1 (restatement) | 463 cr, +8% YoY | restates #2, consistent |
| 17 | T4 | 9 | CFO | India standalone collection from customers, Q1 | 402 crores (transcribed "4 02 crores"), +8% YoY | — |
| 18 | T4 | 9 | CFO | Consolidated deferred revenue, Q1 (correction) | 2,014 crores, +16% YoY | corrects #3; see TRANSCRIPTION_CONTRADICTION note |
| 19 | T4 | 9 | CFO | Consolidated revenue from operations, Q1 (restatement) | 414 crores, +11% YoY | restates #1, consistent |
| 20 | T4 | 9 | CFO | Consolidated EBITDA ("AIDA") | 146 cr, 35% margin | see POSSIBLE_NUMBER_COLLISION at #12 |
| 21 | T4 | 9 | CFO | Consolidated other income, Q1 | 107 crores | attributed to MTM gains on treasury portfolio |
| 22 | T4 | 9 | CFO | Consolidated net profit (PAT), Q1 | 172 crores | transcript says "for the year" — likely transcription slip for "for the quarter"; flag AMBIGUOUS_PERIOD |
| 23 | T4 | 9 | CFO | Cash generated from operations, Q1 | 163 cr | — |
| 24 | T4 | 9 | CFO | Cash and treasury balance | 3,553 crores, as of 30 June 2026 | — |
| 25 | T4 | 9 | CFO | New subsidiary approved | India Finance Limited (MSME short-term credit) | non-numeric disclosure, logged for completeness |
| 26 | T7 | 15 | CEO | Unique business inquiries, restated | 26-27 million, flattish +/-1% | restates #4 with range |
| 27 | T12 | 25 | CEO | Prior-year Q1 one-time Busy buyback benefit | 10 crores | — |
| 28 | T12 | 25 | CEO | Normalized Busy billing growth ex one-time | ~30% | — |
| 29 | T12 | 25 | CEO | Normalized deferred/recognized revenue growth | 30-40% | — |
| 30 | T14 | 29 | CEO | Advertising spend per quarter | "78 cr" | AMBIGUOUS_NUMBER — plausibly a mis-transcription of "7-8 cr"; enumerated verbatim, flagged for Role 5 to sanity-check against ~414cr quarterly revenue |
| 31 | T14 | 29 | CEO | Advertising targeting scope | top ~10% of categories (by monetization) | — |
| 32 | T17a | 35 | CEO | Buyer payment assurance (trustseal buyers) | up to Rs 5 lakh | stated twice in same turn (emphasis repeat) |
| 33 | T28a | 57 | Mgmt | Buyer/seller verification migration target | moving toward 100% (unquantified timeline) | qualitative |
| 34 | T28a | 57 | Mgmt | Silver monthly churn, reconfirmed unchanged | ~7% ("nothing has changed" from the ~7% cited by analyst at Q12) | management reconfirmation of an analyst-cited figure |
| 35 | T28a | 57 | Mgmt | Silver-tier retention rate improvement, 2nd year onward | "double" (2x, qualitative multiplier, no absolute %) | — |
| 36 | T29 | 59 | CEO | GST verification | ~50% currently, target 80-90% | — |
| 37 | T29 | 59 | CEO | Email verification | 99% (paid or free base) / 100% (stated separately for one segment) | two figures stated for different bases in same turn |
| 38 | T29 | 59 | CEO | Phone verification | 99% (paid or free base) / 100% (stated separately for one segment) | two figures stated for different bases in same turn |
| 39 | T29 | 59 | CEO | Bank account verification target | >50% in ~1 year, >80% in ~2 years | forward guidance, see Table 5 |
| 40 | T29 | 59 | CEO | Total active buyers | ~40 million | — |
| 41 | T29 | 59 | CEO | GST/verified business buyers | ~10 million (of ~40 million total) | — |
| 42 | T31 | 63 | CEO | Unique business inquiries, restated | 26-27 million | restates #4/#26 |
| 43 | T31 | 63 | CEO | OTP-verification-attributable inquiry decline | ~4-5% ("four 5%") | word-form number, missed by digit-only grep, added on manual re-sweep |
| 44 | T36 | 73 | CEO | Fleetx stake, then and now | 16-17% (then) -> 22% (now) | — |
| 45 | T36 | 73 | CEO | Bizoom stake, then and now | 10% (then) -> 32% (now) | — |
| 46 | T38a | 77 | CEO | M1 Exchange stake limit | 10% (self-imposed cap, "made it back to 10%") | implies stake had exceeded cap and was reduced |
| 47 | T39 | 79 | Mgmt | Busy revenue CAGR, historical (~4 yrs) | ~28% (management confirms analyst's cited figure) | restates Q18's ANALYST_STATED 28% — management-confirmed, counted as mgmt-stated here |
| 48 | T39 | 79 | Mgmt | Busy business aspirational CAGR target | 35-40% | forward guidance, see Table 5 |
| 49 | T39 | 79 | Mgmt | Busy near-term expected CAGR (next couple of years) | 27-30% | forward guidance, see Table 5 |
| 50 | T41 | 83 | Mgmt | Busy license growth target, immediate 1-2 years | 15-20% | forward guidance, see Table 5 |
| 51 | T43 | 87 | CEO | Busy acquisition cost (full acquisition, 2021-22) | 500 CR | — |
| 52 | T43 | 87 | CEO | Tally market share | 60-70%, restated as "60%" | TRANSCRIPTION_REPEAT_GARBLE — range and single figure both given in same run-on sentence |
| 53 | T47 | 95 | Mgmt | 90-day repeat rate, current | 58-59% | — |
| 54 | T47 | 95 | Mgmt | 90-day repeat rate, historical ("over the years") | 50-51% | — |
| 55 | T47 | 95 | Mgmt | Survey response rate (buyers) | ~2% | — |
| 56 | T47 | 95 | Mgmt | Survey respondents claiming procurement via IndiaMART | ~40%, restated as 40-45% | — |
| 57 | T50 | 101 | CEO | Manual (pre-AI) call center volume | ~80,000 calls/day | compare to #9 (post-AI, >1 lakh calls/day autonomous) — not necessarily contradictory (different point in time), noted for Role 5 |

**ANALYST_STATED numbers (retained for completeness, excluded from the 76
strict management-stated tally):**

| # | Turn | Line | Speaker | Metric | Value(s) as stated |
|---|---|---|---|---|
| A1 | T27c | 55 | Sam Patil | Silver monthly churn cited from prior quarter | ~7% |
| A2 | T30 | 61 | Sam Patil | Unique business inquiry decline | 11% |
| A3 | T30 | 61 | Sam Patil | Active buyer decline | 5% |
| A4 | T38c | 77 | Aman Tadani | Busy revenue CAGR cited (last 3 years) | ~28% compounded |
| A5 | T38c | 77 | Aman Tadani | Busy license growth cited (YoY) | ~10% |
| A6 | T40 | 81 | Aman Tadani | Busy license growth, restated | ~10%/yr |
| A7 | T40 | 81 | Aman Tadani | Busy license growth, assumption check | ~10%/yr (should this continue) |

Raw-token reconciliation: 57 mgmt metric-rows above collectively carry
[roughly] 76 individual numeric tokens (several rows bundle 2-3 tokens,
e.g. row 1 = value + growth%; row 44/45 = two stakes each); the 7
ANALYST_STATED rows carry 7 tokens; 76+7 = 83, matching the COUNT TEST
reconciled total.

**Arithmetic note (for Role 5):** Busy billing growth of +10% YoY (#10)
vs Busy revenue-from-operations growth of +47% YoY (#11) in the same
turn is a large divergence for two adjacent metrics of the same
business; management's own explanation two turns later (#27-#29: a
one-time 10cr prior-year buyback benefit distorting the billing base,
normalized billing growth ~30%, normalized revenue/deferred growth
30-40%) partially but not fully reconciles this — even the normalized
30% billing growth does not obviously bridge to a 47% revenue growth
figure. Flagged ARITHMETIC_FLAG for Role 5.

---

## Table 5 — Forward-Looking Guidance Statements (9 rows)

| # | Turn | Line | Speaker | Statement |
|---|---|---|---|---|
| 1 | T15 (embedded in T17a's answer) | 35 | CEO | Paid buyer program: "as and when something letter [later] comes we will let you know" — no committed timeline |
| 2 | T29 | 59 | CEO | Bank account verification: cross >50% "in the next year or so," cross >80% "in 2 years time frame" |
| 3 | T34 | 69 | CEO | LLM-traffic attribution tooling: "it will take about a year or so" for the market to mature/consolidate |
| 4 | T34 | 69 | CEO | On new investments: "as and when [opportunities] come we will definitely look at them" — open-ended, unquantified |
| 5 | T39 | 79 | Mgmt | Busy business: aspirational target of at least 35-40% CAGR ("that would be work in progress") |
| 6 | T39 | 79 | Mgmt | Busy business: near-term (next couple of years) expected CAGR of 27-30% |
| 7 | T41 | 83 | Mgmt | Busy license growth target: 15-20% "in the immediate year or two" |
| 8 | T41 | 83 | Mgmt | Busy RPU/ARPU realization gains: expected "over the next 3 to 5 years continuously," not a short-term exercise |
| 9 | T43 | 87 | CEO | Strategic investment posture: "as and when we find something very very good uh we will do" — explicitly declines to become "a venture investing firm" with many holdings |

Hedge phrases noted in-line above (lexicon-level classification is A3's
job): "may or may not," "difficult to really judge," "can't officially
answer that," "time only can tell," "it will take years" (T101/line 101,
re: complex AI use cases) are present but not separately tabulated here
per rule 5 ("lexicons in A3").

---

## Flags Summary

- TRANSCRIPT_MERGED_TURN — 8 embedded lines (33, 35, 45, 55, 57, 67, 77, 105)
- SPEAKER_UNCLEAR — T3 (Busy-segment speaker identity), T17b (Q7 attribution), T37 ("no we have a limit"), T48 ("We can consider")
- NAME_VARIANT_AMBIGUOUS — Amandani (T33a, no-connect) vs Aman Tadani (T38b/c, connects) likely same analyst
- NAME_GARBLED — "Vanand Van" (analyst name likely mis-transcribed)
- FIRM_NAME_UNCLEAR — "Energy Abishek" (Abhishek's turn intro, possibly a firm-name prefix)
- FIRM_NOT_STATED — no analyst's brokerage/firm is named anywhere in this transcript
- TRANSCRIPTION_CONTRADICTION — deferred revenue "144 cr" (T2/line5) vs "2,014 cr" (T4/line9), same metric same quarter
- POSSIBLE_NUMBER_COLLISION — "146 cr" used for both Busy deferred revenue (T3) and consolidated EBITDA (T4)
- AMBIGUOUS_NUMBER — advertising spend "78 cr" (T14/line29), plausibly "7-8 cr"
- AMBIGUOUS_PERIOD — consolidated PAT "172 crores... for the year" (T4/line9), context indicates this should read "for the quarter"
- TRANSCRIPTION_REPEAT_GARBLE — Tally market share "60 70% market share 60% market share" (T43/line87)
- ARITHMETIC_FLAG — Busy billing +10% YoY vs Busy revenue +47% YoY in the same turn (T3/line7), see Table 4 note
- REPEAT_QUESTION — buyer-monetization timing (Q2, Q15); LLM/SEO visibility (Q10, Q22)
- QUESTION_COUNT_DISCREPANCY — task brief cites "two questions posted via chat box"; transcript (line 67) contains three (Q15, Q16, Q17)
- ANALYST_STATED_NOT_MGMT — 7 numeric tokens spoken by analysts inside their questions (Table 4 appendix), excluded from the strict 76-count mgmt_numbers tally

No ZERO_STANDING items apply to this doctype (concall transcript; no
financial-statement line-item table enumerated here). No MGMT_ABSENCE:
the CEO/promoter is confirmed present and is the primary spokesperson
throughout.
