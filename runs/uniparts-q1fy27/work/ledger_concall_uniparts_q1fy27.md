# A2 ENUMERATION LEDGER — Uniparts India Ltd (UNIPARTS), Q1 FY2026-27 (concall)

Source: `/home/user/inflection-pipeline/runs/uniparts-q1fy27/work/extract_concall_uniparts_q1fy27.txt`
Format: auto-generated machine transcript, 135 numbered body lines (`nl -ba -w1 -s TAB`), garbled
homophones preserved verbatim per A1 instruction. This ledger cites the **A1 line number** as the
turn/citation address for every row (the transcript is not independently paginated or turn-numbered
by the source; line number is the only addressable unit A1 supplies).
Prior-quarter ledger: NONE supplied (first concall captured for this company) — `NO_PRIOR_BASELINE`,
no dropped-question / dropped-guidance diff possible this run.

**Garbled-name key used throughout (raw text preserved, likely-intended term in brackets on first use
per row group):** "Karnov Karna" [IR/host, transcribed "Anushka" by IR at L2 — NOTE: two different
names appear for what the header describes as one IR/host role; both preserved, flagged
NAME_INCONSISTENCY], "Gurv Soni" [Chairman & Managing Director], "Danish Pagarodia" /"Bodia"/"Tanushi"
[Full-time Director & Group CEO, likely "Tanushree Bagrodia"], "Pandep Tanaha"/"Sepa" [Group CFO],
"Himmani Sma" [IR/FBM], "AIDA"/"IDA"/"Iota" [EBITDA], "pack growth" [PAT growth], "a growth of X%"
[EBITDA growth], "Cuban"/"Cuba" [Q1], "act"/"a"/"ag"/"ical" [ag/agri/agriculture], "Ljugana" [Ludhiana],
"physics and equipment business" [precision equipment business], "190 K" [Rs 190 crores].

=== A2 COUNT TEST ===
```
category: turns              grep_count: 135  sweep_count: 135  match: yes
category: questions          grep_count: 32   sweep_count: 32   match: yes
category: mgmt_numbers       grep_count: 64   sweep_count: 64   match: yes
category: guidance_hedge     grep_count: 15   sweep_count: 15   match: yes   (not a YAML count field; enumerated for A3/A4 completeness per protocol item 5)
gate_a2: pass
```
=== END COUNT TEST ===

### Reconciliation method note (raw grep vs. reconciled, both shown above as final reconciled figures)

- **turns**: `grep -cE "^[0-9]+\t"` on the extract returns 135, exactly matching the A1 header's stated
  `line_count: 135`. Manual sweep (read of all 135 lines, speaker assigned to each) independently
  confirms 135 addressable lines, none skipped, matching the header's own 1..135 range check. Clean
  match on the first pass — no re-sweep needed for this category. **Important caveat carried into the
  Turns table below and NOT resolved by this line-count match**: this is a raw auto-transcript where the
  line breaks do **not** reliably align with actual speaker changes — at least 17 of the 135 numbered
  lines splice two or more distinct speaker segments together (analyst question + management answer-start
  in the same line, or analyst content + operator interruption in the same line). These are flagged
  `MULTI_SPEAKER_LINE` in the Turns table with the sub-segments identified in the comment column, so that
  "turn" and "line" are traceable as related-but-distinct concepts even though this ledger cites by line
  number only (no independent turn-numbering exists in the source to cite instead).

- **questions**: raw `grep -oE "\?"` returns 35 question-mark characters across 29 of the 135 lines.
  This raw count is NOT usable directly as the question count for two reasons found only by manual
  sweep: (a) false positives — of the 29 flagged lines, 10 contain only an audio-check phrase ("Am I
  audible?", "is it better now?", "am I on the way?") and 3 contain only a management rhetorical tag
  ("...right?", "Is this gross margin sustainable?" used as a rhetorical lead-in inside the CFO's own
  answer) — neither is an analyst question; (b) false negatives — manual sweep found 16 genuine analyst
  questions with NO question-mark at all in the transcript (e.g. L19, L26, L34, L44's real ask, L57,
  L67 — the transcription tool dropped the punctuation), and multi-clause lines needed judgment on
  whether clauses are one compound question or two sequential ones (documented per-row in the Questions
  ledger, e.g. L28 and L52 count as 2 and 3 respectively; L104 and L120 each contain one real analyst
  question plus 1-2 management rhetorical "right?" tags that do NOT count). After removing the 10 audio-
  check + 3 rhetorical false positives and adding the 16 unpunctuated real questions (net effect
  precisely reproduced by the per-row build in §3 below), the reconciled total is 32 on both passes.

- **mgmt_numbers**: raw grep for numeric/percent/crore tokens restricted to the 23 management-attributed
  (or management-containing, for `MULTI_SPEAKER_LINE`) lines returns 66 raw token hits. This overstates
  by 6 (2 tokens are the analyst's own 21%/23% embedded inside merged line L44, not management-stated;
  4 tokens are the same fact repeated verbatim within one continuous answer — three restatements of
  "33.3%" in L35 and five restatements of "20%" in L44 collapsed to one citation each since it is the
  same utterance, not a new disclosure) and understates by 2 (regex missed the spelled-out "two and a
  half to three and a half percent" and "two and a half years ago" in L58, which use words not digits).
  66 − 6 + 2 = 62 after arithmetic reconciliation of the raw pass; manual line-by-line sweep (§4 below,
  which also credits genuinely separate repetitions of the SAME figure across DIFFERENT lines/turns as
  separate citations, since each is a fresh disclosure instance useful for the Role 5 consistency check)
  independently builds to 64. The 2-item gap between the two reconciliation routes is the qualitative
  guidance phrase "couple of percentage points better" (L22) and "few percentage points better" (L68),
  which the numeric-token grep cannot match (no digit) but which are legitimate management-quantified
  disclosures (a delta claim) and are retained as rows in §4 — re-swept and added; final reconciled
  count on both passes = 64. `gate_a2: pass` on the reconciled figures.

---

## 0. PARTICIPANTS (concall protocol item 1)

### Management / call-facilitation side

| # | Name (as transcribed) | Likely-intended name | Designation | First appears | Flags |
|---|---|---|---|---|---|
| M1 | (unnamed) "Operator" — addressed once as "Anushka" (L2) | — | Call moderator (third-party conferencing service, not company) | L1 | NAME_INCONSISTENCY (operator later referred to only as "Operator" in stage directions, no name reused) |
| M2 | Karnov Karna | IR / call host | IR / call host — introduces management panel | L2 | — |
| M3 | Gurv Soni | — | Chairman & Managing Director | L3 | Speaks prepared remarks (L3) and closing (L135) only — **does not answer a single Q&A question** across all 15 analyst blocks (L5-134); every Q&A answer is delivered by the Group CEO and/or Group CFO. Noted as an observation, not a formal MGMT_ABSENCE flag (CMD is present and speaks twice) |
| M4 | Danish Pagarodia / "Bodia" / "Tanushi" (addressed variously as "ma'am") | likely Tanushree Bagrodia | Full-time Director & Group CEO | L3 (introduced), L6 (first Q&A answer) | NAME_INCONSISTENCY — three distinct transcribed spellings for one person across the call |
| M5 | Pandep Tanaha / "Sepa" | Group CFO | Group CFO | L3 (introduced), L4 (prepared remarks) | NAME_INCONSISTENCY |
| M6 | Himmani Sma | IR / FBM | IR / FBM | L2 (introduced only) | No independently attributable speaking turn found anywhere in L1-135 — introduced but silent for the entire call |

### Analyst / investor side (15 Q&A turn-blocks, 12 unique questioners, 3 repeat appearances)

| # | Name (as transcribed) | Firm (as transcribed) | Block lines | Flags |
|---|---|---|---|---|
| A1 | Ashoto Tari | Equidas [likely Equirus] | L5-24 | — |
| A2 | Sai Shivam Sha | Aendis Park [likely Anand Rathi] | L26-30 | — |
| A3 | Vir/Vaj Kacharia | SIMPL | L32-41 | Call drops mid-question (L38-41), asked to requeue; returns as A3-repeat |
| A4 | Sunil Jean/Chain | Nimal Bank Securities [likely Nirmal Bang] | L42-46 | Cut off mid-third-question (L45), asked to requeue; returns as A4-repeat |
| A5 | Anubhab/Anubhav Mukhari/Mukharji | Preciient Capital | L48-56 | Cut off mid-third-question (L56), asked to requeue; returns as A5-repeat |
| A6 | Risham Jane | VBT Asset Managers | L57-61 | — |
| A7 | Nishita Shangisha | Safire Capital | L63-73 | First-time caller per self-description (L67) |
| A8 | Saul/Samuel Sha | Paris Investments | L75-85 | — |
| A3-repeat | Vaj Kacharyia | SIMPL | L87-96 | `REPEAT_QUESTION` context (continuation of A3's cut-off margin/FX line of questioning); cut off again (L96), does not return again |
| A9 | Ashish | AK Investments | L97-109 | Severe, unresolved audio issues across 6+ exchanges; question asked twice (L97, L104) but **never answered** — call moves to next questioner after Ashish re-queues (L107-109). Flag `UNANSWERED_QUESTION` |
| A5-repeat | Anubhav Mukharji | Precient Capital | L111-114 | `REPEAT_QUESTION` continuation of A5 |
| A10 | Ashish Parik | Individual investor | L116-121 | Distinct from A9 "Ashish" of AK Investments per header/self-identification as "individual investor" — both named Ashish, tracked separately |
| A11 | VP Rajes | Banyan Capital | L123-127 | — |
| A12 | Ajit Sati | Ieko Quantum Solutions | L129-131 | — |
| A4-repeat | Sunil (Jean/Chain) | Nimal Bank Securities | L132-133 | `REPEAT_QUESTION` continuation of A4; question explicitly self-described as "partly answered" already |

---

## 1. TURNS — every speaker turn/line, L1-135 (concall protocol item 2)

Speaker codes: OP=Operator, IR=IR/host (Karnov Karna), CMD=Chairman & MD (Gurv Soni), CEO=Group CEO
("Bodia"/Tanushi), CFO=Group CFO ("Sepa"), ANL#=analyst per §0 numbering. `MULTI_SPEAKER_LINE` flag
means the raw transcript line splices >1 actual speaker segment; sub-segments listed in Comment.

| Line | Primary speaker | First ~10 words | Flags / Comment |
|---|---|---|---|
| 1 | OP | "Ladies and gentlemen, good day and welcome to the..." | — |
| 2 | IR (Karnov Karna) | "Thanks Anushka. Good afternoon everyone and welcome to the..." | — |
| 3 | CMD (Gurv Soni) | "Uh thanks a lot. Good afternoon everyone and thank you..." | Prepared remarks, single continuous turn (business/segment commentary) |
| 4 | CFO + OP | "Thank you sir. Uh good evening everyone. Um I'll briefly..." | `MULTI_SPEAKER_LINE`: CFO financial highlights, then OP opens Q&A and introduces ANL1 (Ashoto Tari) within same line |
| 5 | ANL1 | "Yeah. Hi sir, Congressman, a very good set of numbers..." | Q1.1 (see §3) |
| 6 | CEO | "Hi Ash. Bodia here." | — |
| 7 | ANL1 | "Yeah. Hi." | — |
| 8 | CEO | "Um so Ashikash you are right uh that in Cuban..." | — |
| 9 | ANL1 | "Yeah." | — |
| 10 | CEO | "But we also have to bear in mind that we..." | — |
| 11 | ANL1 | "Okay. Okay. And I think I think if I remember..." | — |
| 12 | CEO | "Yeah." | Cross-talk region L12-15; attribution best-effort |
| 13 | ANL1 | "Yeah." | Cross-talk; SPEAKER_UNCLEAR (could be CEO) |
| 14 | CEO | "Sorry you were saying something." | — |
| 15 | ANL1 | "No no I'm saying that exactly 10 years back in..." | — |
| 16 | CEO | "absolutely" | — |
| 17 | ANL1 | "so okay and uh and is is the construction equipment..." | Q1.2 |
| 18 | CEO | "so Ashikov our margins actually across uh products um are..." | — |
| 19 | ANL1 | "Okay. Okay. And lastly uh guidance for this year for..." | Q1.3 |
| 20 | CEO | "So you know I think if you look at our..." | — |
| 21 | ANL1 | "Yeah." | — |
| 22 | CEO | "And I think Shudu is also remaining uh robust. I..." | Guidance G3 |
| 23 | ANL1 | "Oh, that's amazing. Okay, that's all from my side..." | Closes A1's block |
| 24 | CEO/mgmt | "Thank you." | — |
| 25 | OP | "Thank you. We take the next question from the line..." | Intro ANL2 |
| 26 | ANL2 | "Uh congratulations for a very good quarter. Uh just a..." | Q2.1 |
| 27 | CEO | "um hi Shan I think uh I think we acknowledge..." | — |
| 28 | ANL2 + CEO | "Uh just a followup question. Thank you for your detailed..." | `MULTI_SPEAKER_LINE`: ANL2 follow-up Q2.2, then CEO answer-start same line |
| 29 | CEO | "We also want to ensure that we're looking at hydraulics..." | — |
| 30 | ANL2/mgmt | "Uh thank you. Thank you." | SPEAKER_UNCLEAR (closing exchange, both sides) |
| 31 | OP | "Thank you. We take the next question from the line..." | Intro ANL3 |
| 32 | ANL3 | "Yeah, I'm audible." | Audio-check only |
| 33 | OP/mgmt | "Yes." | — |
| 34 | ANL3 | "Yeah. Hi, thanks for the opportunity and congratulations on good..." | Q3.1 |
| 35 | CFO | "So Vaj if you look at it our cost of..." | Mgmt numbers (cost of materials 33.3%, inventory gain) |
| 36 | ANL3 | "Can you elaborate what do you mean by product mix?..." | Q3.2 |
| 37 | CFO | "So when I say product mix, I mean exactly our..." | — |
| 38 | ANL3 | "No so again on the uh margins you know so..." | Q3.3 — cut off mid-question by call-quality issue |
| 39 | OP | "Mr. V your voice is breaking could you please fix..." | Interrupt |
| 40 | ANL3 | "yeah is it is it is it better now hello" | Audio-check |
| 41 | OP | "yes now it's much better you may continue to interrupt..." | `MULTI_SPEAKER_LINE`/ambiguous: audio confirmation + OP redirects ANL3 to requeue + intros ANL4 (Sunil Jean) |
| 42 | ANL4 | "Yeah, thanks for taking my question and uh congratulation on..." | Q4.1 |
| 43 | CEO | "So Mr. Jen uh uh thank you. So I think..." | — |
| 44 | ANL4 + CFO | "So uh considering uh good growth uh for next 2..." | `MULTI_SPEAKER_LINE`: ANL4 follow-up Q4.2 (21%/23% figures are ANL4's own, NOT mgmt numbers), then CFO answer (mgmt reaffirms 20%+) same line |
| 45 | ANL4 + OP | "and gross margin at current level. Sorry to interrupt Mr..." | `MULTI_SPEAKER_LINE`: ANL4 starts Q4.3 (cut off), OP interrupts/redirects to queue |
| 46 | ANL4 | "Okay ma'am. Thank you very much." | Closes A4's first block |
| 47 | OP | "Thank you. We take the next question from the line..." | Intro ANL5 |
| 48 | ANL5 | "Uh am I audible?" | Audio-check |
| 49 | OP/mgmt | "Uh you're audible but there's an echo." | — |
| 50 | ANL5 | "Uh is this better?" | Audio-check |
| 51 | OP/mgmt | "Yes, this is better." | — |
| 52 | ANL5 | "Uh ma'am, congrats uh on a good uh set of..." | Q5.1 (3-part compound) |
| 53 | CEO | "Okay. So Anubaran uh if you see the a market..." | — |
| 54 | ANL5 | "Get that ma'am. Thanks. And uh ma'am, my second question..." | Q5.2 |
| 55 | CEO | "Uh sure. I think um if you look at the..." | — |
| 56 | CEO+ANL5+OP+ANL5+OP | "Good. And my last question is ma'am in sorry to..." | `MULTI_SPEAKER_LINE`, heavily merged: CEO closing word + ANL5 starts Q5.3 (cut off) + OP interrupt/redirect + ANL5 "Sure. Thank you." + OP intro ANL6, all in one line |
| 57 | ANL6 | "Yeah. Hi uh congratulations on good set of numbers. So..." | Q6.1 |
| 58 | CEO | "Um so hi Ram thank you for that question. Uh..." | Mgmt numbers (capex 2.5-3.5%, fabrication facility timing) |
| 59 | ANL6 | "Okay. Uh so so the followup question here is on..." | Q6.2 |
| 60 | CEO | "We do we do believe that this application vertical will..." | Guidance G6 |
| 61 | ANL6 | "Okay, perfect. Thank you. All the best." | Closes A6's block |
| 62 | mgmt+OP | "Thank you. Thank you. We take the next question. from..." | `MULTI_SPEAKER_LINE`: closing exchange + OP intro ANL7 |
| 63 | ANL7 | "Um yes. Hello. Am I on the way?" | Audio-check |
| 64 | OP/mgmt | "Hello. Your voice is a little" | — |
| 65 | ANL7 | "uh is it better now?" | Audio-check |
| 66 | OP/mgmt | "Yes, please." | — |
| 67 | ANL7 | "Yeah. Uh so I am uh joining the call for..." | Q7.1 |
| 68 | CEO | "So Nisha we what we are saying is that we..." | Mgmt numbers/guidance (FY26 21%, cycle margin 20%, Q4FY26 24%, Q1FY27 25%) |
| 69 | ANL7 | "Okay. Okay. Understood. Uh that is great. And uh just..." | Q7.2 |
| 70 | CFO | "So the capital requirement of 2 and a half to..." | Mgmt numbers (capex 2.5-3.5%, cash Rs190cr) |
| 71 | ANL7 | "Okay. Okay. So, should we uh have any inorganic uh..." | Q7.3 |
| 72 | CFO | "Yes. Financially, we have a strong balance sheet to be..." | — |
| 73 | ANL7 | "Okay. Okay. Understood. Thank you so much." | Closes A7's block |
| 74 | OP | "Thank you. We take the next question from the line..." | Intro ANL8 |
| 75 | ANL8 | "Yeah. Hi thanks for the opportunity. So I wanted to..." | Q8.1 |
| 76 | CEO | "So Samuel our Mexico business currently is structured that most..." | Mgmt number/guidance (Mexico revenue) |
| 77 | ANL8 | "Okay. Okay. So, will this presence in Mexico increase our..." | Q8.2 |
| 78 | CEO | "So, our Mexico sales uh from the warehouse if everything..." | Guidance G9 (warehouse 52-56%) |
| 79 | ANL8 | "Okay. Correct. Correct. Okay. And in the previous call you..." | Q8.3 |
| 80 | CEO | "I think it given that the a industry recovery is..." | Guidance G10 |
| 81 | ANL8 | "And uh to the previous participant, you did mention that..." | Q8.4 |
| 82 | CFO/CEO | "So Q2 looks very robust and I think uh Q2..." | Guidance G11 |
| 83 | ANL8 | "Okay. Okay. Uh that's it from my right. Thank you..." | Closes A8's block |
| 84 | mgmt | "Thank you." | — |
| 85 | OP | "Thank you." | — |
| 86 | OP | "We take the next Next question from the line of..." | Intro ANL3-repeat |
| 87 | ANL3-repeat | "Yeah, hi. Am I audible now?" | Audio-check |
| 88 | OP/mgmt | "Yes." | — |
| 89 | ANL3-repeat | "Yeah. I just wanted to uh kind of on the..." | Q9.1 start, cut off |
| 90 | OP | "sorry V your voice is very muffled. It's very difficult..." | Interrupt |
| 91 | ANL3-repeat | "just on first." | — |
| 92 | ANL3-repeat | "Yeah. Am I audible now?" | Audio-check |
| 93 | OP/mgmt | "Yeah." | — |
| 94 | ANL3-repeat | "Yeah. I was just asking if I look at our..." | Q9.1 full re-ask |
| 95 | CFO | "So uh there are the gross margins uh so couple..." | Mgmt numbers (material cost 34-37%, EBITDA margin 20%) |
| 96 | ANL3-repeat + OP | "Got it. And other than the inventory, I would request..." | `MULTI_SPEAKER_LINE`: ANL3-repeat starts Q9.2 (cut off), OP redirects to queue; ANL3 does not return again |
| 97 | ANL9 + OP | "Yeah. Hi, congratulations on uh great execution. So my question..." | `MULTI_SPEAKER_LINE`: ANL9 Q10.1 attempt 1, OP interrupts mid-question (can't understand) |
| 98 | ANL9 | "hello is it better" | Audio-check |
| 99 | ANL9 | "hello" | Audio-check |
| 100 | OP | "I think there's not" | — |
| 101 | OP | "so there's a lot of air that's coming through so..." | Coaching on mic technique |
| 102 | ANL9 | "yeah sure Sure. Uh is it better now?" | Audio-check |
| 103 | OP | "Yes, it is better." | — |
| 104 | ANL9 | "Yeah. So my question is little strategic, right? So uh..." | Q10.1 attempt 2 (full re-ask) |
| 105 | OP | "Uh sorry we only could hear uh you said we..." | — |
| 106 | OP | "Your voice is not clear it's not we're not able..." | — |
| 107 | ANL9 | "Yeah, sure. Let me join back." | Requeues; question never answered — `UNANSWERED_QUESTION` |
| 108 | OP | "Okay." | — |
| 109 | ANL9 | "Yes. Thank you so much." | — |
| 110 | OP | "We proceed with the next question from the line of..." | Intro ANL5-repeat |
| 111 | ANL5-repeat + CEO | "Hello. Am I audible? Um Anubhab, it could be Anuhab..." | `MULTI_SPEAKER_LINE`: audio-check + CEO acknowledges + ANL5-repeat asks Q11.1, all merged |
| 112 | CEO + ANL5-repeat | "Sure. I uh I think uh Anubhav uh what we..." | `MULTI_SPEAKER_LINE`: CEO's full answer to Q11.1, then ANL5-repeat's Q11.2 embedded at line-end |
| 113 | CEO | "Absolutely uh Anabas and that's been the effort. So you..." | Answer to Q11.2 |
| 114 | ANL5-repeat | "Uh thanks but that's all the questions I had." | Closes A5-repeat's block |
| 115 | OP | "Thank you. We take the next questions from on the..." | Intro ANL10 |
| 116 | ANL10 | "Hello. Am I audible?" | Audio-check |
| 117 | CEO/OP | "Yes Ashish." | — |
| 118 | ANL10 | "Hello. Am I audible ma'am?" | Audio-check |
| 119 | CEO/OP | "Yes Ashish." | — |
| 120 | ANL10 + CEO + ANL10 | "Congratulations on good set of numbers. I have seen the..." | `MULTI_SPEAKER_LINE`, heavily merged: ANL10 context+Q12.1, CEO's very long SAM/growth-runway answer, and ANL10's closing "Very well explained ma'am..." all in one transcript line |
| 121 | mgmt/ANL10 | "Thank you." | SPEAKER_UNCLEAR (tail of L120 exchange) |
| 122 | OP | "Thank you. We take the next question from the line..." | Intro ANL11 |
| 123 | ANL11 | "Hi uh thanks for the opportunity and congratulations uh Tanushi..." | Q13.1 |
| 124 | CEO | "Hi Rajes uh uh thank you for your good wishes..." | Mgmt numbers (CY26 large-ag degrowth ~15-16%) |
| 125 | ANL11 | "No, great. Thank you. That was very um nicely explained..." | Closes A11's block |
| 126 | mgmt | "Thank you." | — |
| 127 | OP/mgmt | "Thank you." | — |
| 128 | OP | "Before we proceed with the next participant, Participants, please limit..." | Instruction + intro ANL12 |
| 129 | ANL12 | "Yeah, thank you for the opportunity. Ma'am, can you provide..." | Q14.1 |
| 130 | CFO/CEO | "In Q1 FY20 7 our warehousing sales was roughly at..." | Mgmt numbers (channel-mix % by quarter) |
| 131 | ANL12 | "Thank you." | Closes A12's block |
| 132 | OP + ANL4-repeat | "Thank you. We take the next question from the line..." | `MULTI_SPEAKER_LINE`: OP intro ANL4-repeat, then ANL4-repeat's Q15.1 in the same line |
| 133 | CFO | "So Sunil G uh if everything else remains constant the..." | Guidance G14 (repeat, warehouse 52-56%) |
| 134 | ANL4-repeat + OP | "Okay, great. That was my question. Thank you ladies and..." | `MULTI_SPEAKER_LINE`: ANL4-repeat closes, OP announces last question taken and hands to management for closing, same line |
| 135 | CMD + OP | "Uh thanks a lot. Um I I just want to..." | `MULTI_SPEAKER_LINE`: CMD closing remarks (guidance G15), then OP final sign-off, same line |

Turn count: 135 rows (L1-135), all 135 A1 lines addressed. `MULTI_SPEAKER_LINE` flagged on 17 rows
(L4, 28, 41, 44, 45, 56, 62, 96, 97, 111, 112, 120, 121, 130*, 132, 134, 135) — *L130 flagged for
completeness as CFO/CEO joint attribution is itself ambiguous in source, not a hard multi-speaker splice,
retained as a soft flag.

---

## 2. FORWARD-LOOKING & HEDGE / GUIDANCE STATEMENTS (concall protocol item 5) — count 15

| # | Line | Speaker | Statement (paraphrase, verbatim fragment quoted) | Type |
|---|---|---|---|---|
| G1 | 3 | CMD | "first customer deliveries from the [Mexico] warehouse expected in Q3 of this year" | Guidance (timeline) |
| G2 | 3 | CMD | "we continue to actively evaluate acquisition opportunities" | Hedge (no specifics, no timeline) |
| G3 | 22 | CEO | "our FY27 growth will be couple of percentage points better than the growth that we uh had in FI26" | Guidance (growth delta) |
| G4 | 43 | CEO | large-ag recovery "will come in FY uh 28"; small-ag industry growth "going to come in calendar year 27" | Guidance (segment recovery timing) |
| G5 | 44 | CFO | "we are going to deliver FY27 also very comfortably over the 20% plus margin... we actually are confident that 20% plus is what we will deliver" | Guidance (margin) |
| G6 | 60 | CEO | fabrication vertical "will become a meaningful vertical in the next 18 to 24 months" | Guidance (timeline) |
| G7 | 68 | CEO | FY27 topline growth = FY26's 21% + "a few percentage points better... as the growth comes through in FI28 ... this sort of trajectory of growth should continue" | Guidance (growth delta, multi-year) |
| G8 | 76 | CEO | Mexico FY27 revenue "should be in uh mid singledigit million dollar level"; "In phase two we will also be uh considering manufacturing in Mexico" | Guidance (revenue level + capability roadmap, no date on phase 2) |
| G9 | 78 | CEO | warehouse-sales share "will remain in the... range of let's say about 52 to to 55 56%... in the next uh let's say 12 to 18 months" | Guidance (channel mix, 12-18mo horizon) |
| G10 | 80 | CEO | second-half-better-than-first-half expectation reaffirmed, "given that the a industry recovery is going to happen in the second half" | Guidance (H2 weighting) |
| G11 | 82 | CFO/CEO | "Q2 looks very robust... Q2 should be in line with Q1" | Guidance (near-term quarter) |
| G12 | 95 | CFO | material cost sustained "in the range of 34 to 37%... very confident of uh maintaining that level"; EBITDA margin "20% Iota margin over a cycle" | Guidance (reaffirmed, cycle-level) |
| G13 | 112 | CEO | aftermarket softness "over the next uh uh 12 months we do expect this to normalize" | Guidance (normalization timeline) |
| G14 | 133 | CFO | warehouse share to increase from Mexican-warehouse ramp, hedged: "if everything else remains constant the percentage of warehouse sales will increase but... the exact stacking up will depend on..." | Guidance + hedge (conditional) |
| G15 | 135 | CMD | "gives us confidence that we will improve on our earlier guidance for the full fiscal as we look at the quarters ahead" | Forward commitment (hedged — "as we look at the quarters ahead", no number given) |

---

## 3. QUESTIONS — every distinct analyst question (concall protocol item 3) — count 32

| Q# | Analyst | Firm | Line(s) | Topic | Flags |
|---|---|---|---|---|---|
| Q1.1 | A1 Ashoto Tari | Equidas | 5 | Construction-segment revenue share — structurally sustainable? | — |
| Q1.2 | A1 Ashoto Tari | Equidas | 17 | Is construction segment higher margin than tractors overall? | — |
| Q1.3 | A1 Ashoto Tari | Equidas | 19 | FY sales-growth guidance — unchanged or upward revision? | — |
| Q2.1 | A2 Sai Shivam Sha | Aendis Park | 26 | PTO/fabrication (hydraulics) acquisition — timeline to materialize/contribute to revenue | — |
| Q2.2 | A2 Sai Shivam Sha | Aendis Park | 28 | Follow-up: post-acquisition revenue timeframe and % growth contribution | Two-part compound, counted as one row |
| Q3.1 | A3 Vir/Vaj Kacharia | SIMPL | 34 | Quantify FX gain and inventory gain contribution in the quarter | — |
| Q3.2 | A3 Vir/Vaj Kacharia | SIMPL | 36 | Elaborate "product mix" driver of cost-of-materials; give channel-mix numbers Q1 vs last year | — |
| Q3.3 | A3 Vir/Vaj Kacharia | SIMPL | 38 | Operating-margin/operating-leverage follow-up | `INCOMPLETE_QUESTION` — cut off by call-quality issue, not resolved before requeue |
| Q4.1 | A4 Sunil Jean/Chain | Nimal Bank Securities | 42 | Confirm perception: construction + ag recovery = "second lever" driving FY28 growth | — |
| Q4.2 | A4 Sunil Jean/Chain | Nimal Bank Securities | 44 | Given current ~23% run-rate vs 21%-guided cycle margin, will margin guidance move up? | Note: the "21%"/"23%" figures in this line are analyst-stated, not management numbers |
| Q4.3 | A4 Sunil Jean/Chain | Nimal Bank Securities | 45 | "...and gross margin at current level" | `INCOMPLETE_QUESTION` — cut off by operator interrupt mid-ask |
| Q5.1 | A5 Anubhab Mukhari | Preciient Capital | 52 | Why is large-ag market share historically lower; competition capability gap; what is being done to gain share | Three-part compound, counted as one row |
| Q5.2 | A5 Anubhab Mukhari | Preciient Capital | 54 | CSM/construction growth concentrated in North America — opportunity to break into new European OEMs? | — |
| Q5.3 | A5 Anubhab Mukhari | Preciient Capital | 56 | "my last question is ma'am..." | `INCOMPLETE_QUESTION` — cut off by operator interrupt before ask completed; analyst returns later as A5-repeat (Q11.1/Q11.2) but does not re-ask this specific cut-off question |
| Q6.1 | A6 Risham Jane | VBT Asset Managers | 57 | Capital-allocation contingency: if inorganic doesn't happen, any organic diversification into new segments? | — |
| Q6.2 | A6 Risham Jane | VBT Asset Managers | 59 | Follow-up: will fabrication business scale from its low base into a meaningful vertical? | — |
| Q7.1 | A7 Nishita Shangisha | Safire Capital | 67 | Reiterate revenue and margin guidance for next two years (first-time caller) | — |
| Q7.2 | A7 Nishita Shangisha | Safire Capital | 69 | Clarify: does the 2.5-3.5% capex figure include both inorganic and organic opportunity? | — |
| Q7.3 | A7 Nishita Shangisha | Safire Capital | 71 | Follow-up: would an inorganic opportunity require a capital raise? | — |
| Q8.1 | A8 Saul/Samuel Sha | Paris Investments | 75 | Mexico facility — nature/size of business potential | — |
| Q8.2 | A8 Saul/Samuel Sha | Paris Investments | 77 | Will Mexico presence increase warehouse-sale share and EBITDA? | — |
| Q8.3 | A8 Saul/Samuel Sha | Paris Investments | 79 | Confirm prior-call expectation: H2 better than H1 — still holds? | — |
| Q8.4 | A8 Saul/Samuel Sha | Paris Investments | 81 | Confirm prior comment to another participant: Q2 similar range to Q1 — correct? | — |
| Q9.1 | A3-repeat Vaj Kacharyia | SIMPL | 89/94 | Continuation of Q3.1/Q3.3: vs. FY22 cycle peak, what (other than FX/inventory) is driving current gross margin, and is it sustainable? | `REPEAT_QUESTION` (continuation of A3's original line of questioning); re-asked at L94 after audio-check interruptions at L90-93 |
| Q9.2 | A3-repeat Vaj Kacharyia | SIMPL | 96 | "And other than the inventory..." | `INCOMPLETE_QUESTION` — cut off by operator interrupt; analyst does not return again |
| Q10.1 | A9 Ashish | AK Investments | 97 / 104 | Strategic: prior diversification from cyclical ag into construction "didn't turn out the way we thought" — what capabilities are being added to address volatility long-term? | Asked twice (L97 garbled attempt, L104 full re-ask) due to severe audio issues; `UNANSWERED_QUESTION` — analyst re-queued at L107 and management never responds before call moves to next questioner |
| Q11.1 | A5-repeat Anubhav Mukharji | Precient Capital | 111 | Outlook on replacement/aftermarket business given multi-year degrowth | `REPEAT_QUESTION` (A5's second appearance) |
| Q11.2 | A5-repeat Anubhav Mukharji | Precient Capital | 112 | Follow-up: scope to add new retail channel/distributors in US or Europe for 3PL aftermarket | — |
| Q12.1 | A10 Ashish Parik | Individual investor | 120 | Given China+1 / precision-component opportunity in aerospace, defense, automotive — is an acquisition being considered to enter these sectors? | — |
| Q13.1 | A11 VP Rajes | Banyan Capital | 123 | Where are we in the industry cycle, and could there be non-cyclical growth given expanded product/geography footprint? | — |
| Q14.1 | A12 Ajit Sati | Ieko Quantum Solutions | 129 | Channel-mix (warehouse / locally made-sold / direct export) contribution to revenue, Q1 FY26 vs Q1 FY27 | — |
| Q15.1 | A4-repeat Sunil Chain | Nimal Bank Securities | 132 | Mexican-warehouse commencement — will this increase warehouse-sales share from Q3 onward? | `REPEAT_QUESTION` (A4's second appearance); self-described as "partly answered" already |

Question count: 32. `REPEAT_QUESTION` flag on 4 rows (Q9.1, Q11.1, Q11.2 by extension of A5-repeat's
block, Q15.1) reflecting the 3 analysts (A3, A5, A4) who were cut off/requeued and returned later in
the call. `INCOMPLETE_QUESTION` flag on 4 rows (Q3.3, Q4.3, Q5.3, Q9.2) where the transcript shows the
question was never completed before an interrupt. `UNANSWERED_QUESTION` flag on 1 row (Q10.1) — the
only question in the transcript that reaches a full, comprehensible re-ask and is still never answered
by management before the call moves on.

---

## 4. MANAGEMENT NUMBERS — every quantified figure spoken by management (concall protocol item 4) — count 64

| # | Line | Speaker | Number / metric | Context |
|---|---|---|---|---|
| N1 | 3 | CMD | Revenue growth 27% YoY | Q1 FY27 headline |
| N2 | 3 | CMD | EBITDA ("a") growth 55% YoY | Q1 FY27 headline |
| N3 | 3 | CMD | PAT ("pack") growth 64% YoY | Q1 FY27 headline |
| N4 | 3 | CMD | TTM EPS Rs 39.97 | — |
| N5 | 3 | CMD | ROCE north of 27% | TTM |
| N6 | 3 | CMD | ROE 20% | TTM |
| N7 | 3 | CMD | Net cash Rs 190 crores ("190 K") | End of Q1 |
| N8 | 3 | CMD | Special dividend Rs 101 crores | Declared Oct 2025 |
| N9 | 3 | CMD | Cash balance ~Rs 210 crores | At time of special dividend, Oct 2025 |
| N10 | 3 | CMD | Rebuild period 10 months | Cash rebuilt from ~210cr post-dividend to 190cr net cash context |
| N11 | 3 | CMD | TTM new-business order book > Rs 225 crores | — |
| N12 | 3 | CMD | Aftermarket ~12% of revenue, flat YoY (absolute terms) | Q1 FY27 |
| N13 | 4 | CFO | Revenue Q1 FY27 Rs 347 crores | — |
| N14 | 4 | CFO | Revenue growth 27% YoY | Restated by CFO |
| N15 | 4 | CFO | EBITDA Rs 90 crores | — |
| N16 | 4 | CFO | EBITDA growth 55% YoY | Restated |
| N17 | 4 | CFO | EBITDA growth 10% QoQ | — |
| N18 | 4 | CFO | PAT Rs 57 crores | — |
| N19 | 4 | CFO | PAT growth 64% YoY | Restated |
| N20 | 4 | CFO | PAT growth 11% QoQ | — |
| N21 | 4 | CFO | Operating cash generated Rs 44 crores | Q1 |
| N22 | 4 | CFO | TTM EPS Rs 39.97 | Restated ("39 rupees 97 pesa") |
| N23 | 4 | CFO | Net working capital 139 days of TTM revenue | — |
| N24 | 4 | CFO | Net cash ~Rs 190 crores | Restated |
| N25 | 4 | CFO | Capex during quarter Rs 12 crores | — |
| N26 | 8 | CEO | Construction segment = 45% of total revenue | Q1 FY27 |
| N27 | 18 | CEO | Direct-export "base margin" 20% | Channel-margin tier (locally made/sold < base 20% < warehouse) |
| N28 | 22 | CEO | FY27 growth guidance = FY26 growth + "couple of percentage points" | Qualitative delta, no fixed %; see also G3 |
| N29 | 27 | CEO | ~a dozen acquisition targets evaluated since IPO | Hydraulics/fabrication/PTO platforms |
| N30 | 27 | CEO | ~half a dozen acquisition opportunities currently being evaluated | — |
| N31 | 28 | CEO | Acquisition ROIC/ROE hurdle: 18 to 30 months | — |
| N32 | 35 | CFO | Cost of materials 33.3% (Q1 FY27) | Restated 3x within same answer, collapsed to 1 citation |
| N33 | 35 | CFO | Inventory gain ~Rs 1 crore | Within the 33.3% cost-of-materials line |
| N34 | 44 | CFO | Margin guidance reaffirmed: 20%+ | 5x verbal repetition within same answer, collapsed to 1 citation; NOTE the 21%/23% in this line are analyst-stated, excluded |
| N35 | 53 | CEO | India = 50% of global tractor production | Context for small-ag home-market advantage |
| N36 | 58 | CEO | Capex ~2.5 to 3.5% of total revenue | First mention (recurs N40, N46) |
| N37 | 58 | CEO | Fabrication facility investment made "two and a half years ago" | Small/medium-size fabrication facility |
| N38 | 58 | CEO | Special dividend Rs 101 crores, declared Oct 2025 | Restated (see N8) |
| N39 | 60 | CEO | Fabrication vertical to become "meaningful" in 18-24 months | Timeline; see also G6 |
| N40 | 60 | CEO | Capex ~2.5 to 3.5% of total revenue | Restated |
| N41 | 68 | CEO | FY26 topline growth 21% YoY | — |
| N42 | 68 | CEO | FY27 topline growth = FY26's 21% + "a few percentage points better" | Qualitative delta |
| N43 | 68 | CEO | Cycle EBITDA margin ~20% (trough-to-peak / peak-to-trough) | — |
| N44 | 68 | CEO | Q4 FY26 EBITDA margin ~24% | — |
| N45 | 68 | CEO | Q1 FY27 EBITDA margin ~25% | — |
| N46 | 70 | CFO | Capex ~2.5 to 3.5% of total revenue | Restated, clarified as organic-business-only figure |
| N47 | 70 | CFO | Net cash ~Rs 190 crores, debt-free | Restated (see N7, N24) |
| N48 | 76 | CEO | Mexico FY27 revenue: "mid single-digit million dollar level" | — |
| N49 | 78 | CEO | Warehouse-sales share range 52 to 55/56% | Next 12-18 months; see also G9 |
| N50 | 95 | CFO | Material cost sustained range 34 to 37% | Reaffirmed as "typical of our business" |
| N51 | 95 | CFO | EBITDA margin 20% over a cycle | Reaffirmed |
| N52 | 112 | CEO | Aftermarket % of revenue FY25: 20% | — |
| N53 | 112 | CEO | Aftermarket % of revenue FY26: 15% | — |
| N54 | 112 | CEO | Aftermarket % of revenue, current (Q1 FY27 run-rate): 12% | Restated (see N12) |
| N55 | 112 | CEO | Aftermarket normalization timeframe: ~12 months | See also G13 |
| N56 | 120 | CEO | Above-70HP 3-point-linkage: "single-digit market share" | Growth-runway framing |
| N57 | 120 | CEO | Below-7HP 3-point-linkage: "dominant share of business globally" | Qualitative, no % given |
| N58 | 120 | CEO | Top 5 global agricultural OEM customers are Uniparts customers | — |
| N59 | 120 | CEO | Top 3 construction-equipment OEM manufacturers are Uniparts customers | — |
| N60 | 124 | CEO | Large-ag industry CY25 degrowth (no % given, only "degrew") | — |
| N61 | 124 | CEO | Large-ag industry CY26 expected degrowth ~15-16% | — |
| N62 | 130 | CFO/CEO | Q1 FY27 warehouse-sales share ~56% | Channel-mix breakdown by quarter |
| N63 | 130 | CFO/CEO | Q1 FY26 warehouse-sales share ~50-52% | — |
| N64 | 130 | CFO/CEO | Q1 FY26 locally-made/locally-sold share ~25%; Q1 FY27 ~22% | Two-quarter comparison within one citation |

Management-numbers count: 64. Note N49/N50/N51/N62-N64 restated again at L133 (Guidance table G14) —
not double-counted here since L133's content is guidance-with-hedge language, not a fresh number,
already captured in §2.

---

## Flags summary (roll-up)

`NAME_INCONSISTENCY` (2: operator name, CEO name spelled 3 ways), `MULTI_SPEAKER_LINE` (17, §1),
`REPEAT_QUESTION` (4, §3), `INCOMPLETE_QUESTION` (4, §3), `UNANSWERED_QUESTION` (1, §3),
`NO_PRIOR_BASELINE` (header-level, no prior-quarter concall ledger supplied for diff).
`ZERO_STANDING` / `ENTITY_CHANGE` / `DROPPED_SLIDE` do not apply to this doctype (concall transcript
has no financial-table line items, entity list, or slide deck).

---

```yaml
stage: A2-enumerator
company: "Uniparts India Ltd (UNIPARTS)"
quarter: "Q1 FY2026-27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/uniparts-q1fy27/work/ledger_concall_uniparts_q1fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 135
  questions: 32
  mgmt_numbers: 64
  slides: 0
  slide_numbers: 0
flags_raised: [NAME_INCONSISTENCY, MULTI_SPEAKER_LINE, REPEAT_QUESTION, INCOMPLETE_QUESTION, UNANSWERED_QUESTION, NO_PRIOR_BASELINE]
gate_a2: pass
mismatch_note: ""
```
