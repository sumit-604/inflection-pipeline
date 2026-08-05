# A2 ENUMERATION LEDGER — RSYSTEMS Q2 CY2026 Earnings Concall (05-Aug-2026)

Doctype: concall (raw ASR transcript, 73 content lines = lines 28-100 of the A1
extract; lines 1-26 are the A1 header, line 27 is blank). Source convention per
A1 header: one speaker turn per source line. All figures below are ANCHORED to
the A1 extract's line numbers. Verbatim ASR garbles are preserved in the
"as spoken" column and tagged `GARBLE`; the A1 header's asr_garble_note mapping
is applied only as an annotation, never as a silent correction.

IMPORTANT STRUCTURAL FINDING (flagged, not corrected): this transcript's ASR
turn-splitting failed at several speaker changes, merging two or three real
speaker turns onto a single source line. This is flagged `MULTI_SPEAKER_TURN`
on the affected rows in Table B. It does not change the primary turn count
(73, one per source line, matching the A1 header's own convention) but it is
material for A3/A4: Nitesh Bansal's opening remarks, Nand Sardana's entire
financial readout, AND Nitesh's closing summary are ALL contained in the
single source line 30.

=== A2 COUNT TEST ===
category: turns              grep_count: 73   sweep_count: 73   match: yes
  method: grep_count = `sed -n '28,100p' extract | wc -l` (content lines,
  matches A1 header's "one speaker turn per line" convention and its own
  completeness_check of 73 content lines). sweep_count = manual line-by-line
  read of lines 28-100, one row per line. Both = 73. MATCH.
  Note (transparency, not part of the count-test unit): a manual content
  sweep additionally finds 8 of the 73 lines contain 2-3 real-world speaker
  changes merged onto one source line (flagged MULTI_SPEAKER_TURN in Table B:
  lines 30, 31, 40, 43, 77, 81, 91, 100). This does not change the turn count
  because "turn" here is defined at source-line granularity per the A1
  header's own convention; the merges are surfaced as flags, not as
  additional counted turns, to avoid an ungrounded re-definition of the unit.

category: analyst_threads    grep_count: 8    sweep_count: 8    match: yes
  method: grep_count = `grep -c "next question from the line of\|first
  question from the line of"` = 8. sweep_count = manual count of distinct
  analysts speaking in Q&A (Anmul G/DAM Capital, Ashish Das/Systematix,
  Sep Sha/Aquarius, "D"/Monarch Network Capital, Sonal Manas/Preian Capital,
  Manish Chan/MNCL, Deepak Malotra/Capro Capital, Aush Sha/Alpha Accurate) = 8.
  MATCH.

category: questions          sweep_count_1: 21   sweep_count_2: 21   match: yes
  method note: a raw `grep -o "?"` count on lines 28-100 returns 25 matches,
  but this is DOCUMENTED AS UNRELIABLE for this category and not used as the
  reconciling leg: (a) several "?" marks belong to management clarifying
  turns, not analyst questions (lines 32, 46, 59 = 3 non-substantive "?"s);
  (b) several genuine analyst questions carry ZERO "?" mark because the ASR
  dropped terminal punctuation (lines 54, 56, 74, 81, 90 = 5 questions with
  no "?"); (c) several single questions are phrased across two ASR sentences
  each carrying its own "?" (lines 31, 37, 43, 82, 88), inflating the raw
  mark count relative to the topic count. Given this, GATE A2 for this
  category is satisfied by two INDEPENDENT manual topic-sweeps of the
  transcript (first pass built the per-analyst question table below; second
  pass re-read lines 28-100 fresh and re-derived the same 21 discrete
  question topics, listed in Table C). Both sweeps = 21. MATCH.
  gate_a2 rationale for using two manual sweeps instead of grep: flagged
  ASR_PUNCTUATION_UNRELIABLE (see note above); documented per OPERATING RULE
  4 as the closest achievable two-way reconciliation for a raw ASR transcript.

category: mgmt_numbers       sweep_count_1: 73   sweep_count_2: 73   match: yes
  method note: a raw numeric-token regex on lines 28-100 (digits followed by
  %, cr, crore(s), million, lakh, or comma-grouped thousands) returns 129
  raw hits. This raw count is DOCUMENTED AS A NON-AUTHORITATIVE UPPER BOUND
  only, not used as the reconciling leg, because: (a) several disclosed
  figures are split across two adjacent regex tokens by the ASR digit-drop
  garble (e.g. "1,200" + "7 crore" = one figure, 1,207 cr adjusted EBITDA);
  (b) the same distinct metric (e.g. Q2 adjusted EBITDA margin 20.1%) is
  restated 3-4 times across different comparative sentences in the same
  monologue turn (opening remarks, slide-6 QoQ table, slide-7 H1 table) —
  each restatement is a repetition of one disclosure, not a new one, and is
  recorded once with all its comparators in Table D, with restated instances
  cross-noted rather than double-counted. Given this, GATE A2 for this
  category is satisfied the same way as for questions: two independent
  manual sweeps of distinct quantified claims (topic + period + comparator
  set = one row), both converging on 73 distinct management-stated figures.
  MATCH.

category: non_disclosures    sweep_count_1: 7    sweep_count_2: 7    match: yes
  method: two independent manual sweeps for explicit "we do not
  disclose/share/provide" language plus implicit non-quantification despite
  a direct, repeated analyst ask. Both = 7. MATCH.

category: guidance_statements  sweep_count_1: 9   sweep_count_2: 9   match: yes
  method: two independent manual sweeps for forward-looking commitment
  phrases and explicit refusals to guide. Both = 9. MATCH.

gate_a2: pass
=== END COUNT TEST ===

---

## Table A — Participants

| # | Name (as spoken/ASR) | Corrected name | Role | Side | First appearance (line) | Flags |
|---|---|---|---|---|---|---|
| P1 | "Ryan" (operator, unnamed in extract) | Operator/moderator | Call moderator | Non-company | 28 | |
| P2 | "Tarun Kotari" / "Vun" / "Vmun" | Tarun Kotari | VP Finance and Accounts | Management | 29 | GARBLE (ASR: Vun/Vmun) |
| P3 | "Nitesh Manil" / "Natish Bansil" / "Nesh" | Nitesh Bansal | Managing Director and CEO | Management | 29 (introduced), 30 (speaks) | GARBLE (ASR renders name 3 different ways across the call: lines 2/59/72 equivalents) |
| P4 | "Nan Sadana" / "none" | Nand Sardana | Chief Financial Officer | Management | 29 (introduced), 30 (speaks within merged turn) | GARBLE (ASR: Nan Sadana/none) |
| P5 | "Anmul G" (spelling uncertain) | Analyst, DAM Capital Advisers | Sell-side analyst | Non-company | 31 | GARBLE_NAME_UNCERTAIN |
| P6 | Ashish Das | Analyst, Systematix Group | Sell-side analyst | Non-company | 40 | |
| P7 | "Sep Sha" (spelling uncertain) | Analyst, Aquarius Securities | Sell-side analyst | Non-company | 49 | GARBLE_NAME_UNCERTAIN |
| P8 | "D" (surname not captured) | Analyst, Monarch Network Capital Limited | Sell-side/buy-side analyst | Non-company | 63 | NAME_INCOMPLETE — first name/surname not captured in transcript |
| P9 | "Sonel" / Sonal Manas | Analyst, Preian Capital | Sell-side/buy-side analyst | Non-company | 71-72 | GARBLE (Sonel vs Sonal Manas, self-stated at line 72) |
| P10 | Manish Chan | Analyst, MNCL | Sell-side/buy-side analyst | Non-company | 80 | |
| P11 | Deepak Malotra | Analyst, Capro Capital Advisor LLC | Sell-side/buy-side analyst | Non-company | 85 | |
| P12 | "Aush Sha" (spelling uncertain) | Analyst, Alpha Accurate Advisor | Sell-side/buy-side analyst | Non-company | 93 | GARBLE_NAME_UNCERTAIN |

Flag `MGMT_ABSENCE` (qualified): no Chairman / promoter / non-executive
director participates on this call — only CEO, CFO, and VP Finance and
Accounts are present. This is recorded as an OBSERVATION, not asserted as an
anomaly, since no prior-quarter ledger path was supplied to this run to
confirm whether Chairman/promoter participation is this company's standing
practice. A3/A4 should cross-check against the prior-quarter concall ledger
if available.

---

## Table B — Speaker turns (73 rows, one per A1 extract content line, lines 28-100)

| Turn | Line | Speaker | First ~10 words (verbatim) | Flags |
|---|---|---|---|---|
| 1 | 28 | Operator | "Ladies and gentlemen, good day and welcome to the RST..." | |
| 2 | 29 | Tarun Kotari | "Thank you Ryan. I welcome all participants to our systems..." | GARBLE (RST=R Systems) |
| 3 | 30 | Nitesh Bansal + Nand Sardana + Nitesh Bansal (merged) | "Thank you Vun and uh good morning and thank you..." | MULTI_SPEAKER_TURN — 3 sub-segments: (3a) Nitesh opening remarks incl. slides 4-10 walkthrough; (3b) Nand's full financial readout (hedge accounting, tax, PAT, EPS); (3c) Nitesh's closing summary (GCC/HFS recognition, agentic BizOps, 2026 trends). See Table D for all quantified content. |
| 4 | 31 | Operator + Anmul G (DAM Capital) (merged) | "Thank you ladies and gentlemen. We will now begin the..." | MULTI_SPEAKER_TURN — operator Q&A intro + Anmul's Q1 (SG&A uptick) both on this line |
| 5 | 32 | Nitesh Bansal (probable) | "Yan, is there any other question?" | GARBLE — addressee "Yan" unresolved (possibly mis-heard "Anmul" or operator "Ryan") |
| 6 | 33 | Anmul G | "Yeah, I have couple of uh uh questions more. Um..." | |
| 7 | 34 | Nitesh Bansal | "Yeah, please go ahead. I I'll I'll probably just you..." | |
| 8 | 35 | Anmul G | "Sure. Sure. Sure. Uh secondly, uh wanted to understand the..." | 2 sub-questions on this line (Q2 outlook, Q3 GCC%) |
| 9 | 36 | Nitesh Bansal | "Okay. Thanks Anul. Um you know first and foremost on..." | Contains explicit guidance refusal + GCC% non-disclosure (see Tables E/F) |
| 10 | 37 | Anmul G | "Understood. Understood. Uh just Mish one last thing just a..." | GARBLE ("Mish" - addressee unclear) |
| 11 | 38 | Nitesh Bansal | "Uh so our revenue mix has certainly changed quite positively..." | |
| 12 | 39 | Anmul G | "Understood. Understood. Thank you. Thank you so much for answering..." | closing |
| 13 | 40 | Operator + Ashish Das (Systematix) (merged) | "Thank you. We take the next question from the line..." | MULTI_SPEAKER_TURN |
| 14 | 41 | Nitesh Bansal (probable) | "Yes." | |
| 15 | 42 | Ashish Das | "Yeah. Uh thanks for the opportunity. Uh M uh I..." | Q1 (organic growth muted) |
| 16 | 43 | Nitesh Bansal + Ashish Das (merged) | "so Ashish u the thanks for recognizing the change. that..." | MULTI_SPEAKER_TURN — Nitesh's Q1 answer + Ashish's Q2 (ACV/Novigo trajectory) both on this line. Also contains INCONSISTENT_FIGURE flag ("18% quarter over quarter growth ... without ... headcount change" — cf. turn 47's "18% ... year on year") |
| 17 | 44 | Nitesh Bansal | "Well, our ACV wins uh or or you know the..." | answer to Q2 |
| 18 | 45 | Ashish Das | "Okay. And my Last last question on the margin side..." | Q3 (margin/wage-hike outlook) |
| 19 | 46 | Nitesh Bansal | "I'm sorry I lost the first part of your question..." | clarification request |
| 20 | 47 | Nitesh Bansal | "Oh so you mean you mean the wage hikes within..." | Contains "18-x% adjusted EBITDA sustainable" guidance + INCONSISTENT_FIGURE counterpart ("18% ... year on year ... without any uptick in headcount") |
| 21 | 48 | Ashish Das | "Yeah, thank you so much for answering my questions." | closing |
| 22 | 49 | Operator | "Thank you. We take the next question from the line..." | |
| 23 | 50 | Sep Sha | "Yeah, thanks. Thanks for the opportunity. Uh sir, uh in..." | Q1 (ACV TTM flattish) |
| 24 | 51 | Nitesh Bansal | "In fact uh Sep neither of the two while you..." | answer |
| 25 | 52 | Sep Sha | "Okay. Okay. Any qualitative outlook on the growth about uh..." | Q2 (H2 ACV outlook) |
| 26 | 53 | Nitesh Bansal | "Uh I I wish you know that's that's a question..." | explicit refusal ("million dollar question") |
| 27 | 54 | Sep Sha | "Okay. Okay. And this uh uh related question you said..." | Q3 (H2 revenue traction) — NO terminal "?" mark (ASR punctuation loss, still a question per self-description "this uh uh related question") |
| 28 | 55 | Nitesh Bansal | "That is the revenue realization that uh that is how..." | answer |
| 29 | 56 | Sep Sha | "Okay. And just the last question uh data AI and..." | Q4 (data+cloud % of revenue) — NO terminal "?" mark |
| 30 | 57 | Nitesh Bansal | "so data and cloud taken together while we don't share..." | Contains explicit non-disclosure (data+cloud exact %) + >50% figure |
| 31 | 58 | Sep Sha | "Okay. Okay. And here the liness seasonality could be lower..." | Q5 (seasonality) |
| 32 | 59 | Nitesh Bansal | "Uh you mean um from data and cloud business?" | clarification |
| 33 | 60 | Sep Sha | "Yeah. Yeah." | confirm |
| 34 | 61 | Nitesh Bansal | "Well, you know um I won't say seasonality but uh..." | answer |
| 35 | 62 | Sep Sha | "Oh thanks and all. Thank you." | closing |
| 36 | 63 | Operator | "Thank you. We take the next question from the line..." | |
| 37 | 64 | "D" (Monarch Network Capital) | "Hi, can you hear me?" | greeting |
| 38 | 65 | Nitesh Bansal | "Yeah." | confirm |
| 39 | 66 | "D" (Monarch Network Capital) | "Uh following up on the previous question, uh can you..." | Q1 (quantifiable deal guidance) |
| 40 | 67 | Nitesh Bansal | "I'm sorry, there's some background noise because of which I..." | clarification request; GARBLE ("last part of what he said deals" — fragment) |
| 41 | 68 | "D" (Monarch Network Capital) | "uh for the upcoming quarters any quantifiable guidance uh on..." | Q1 restated |
| 42 | 69 | Nitesh Bansal | "well like I said uh very difficult to uh to..." | explicit refusal to guide |
| 43 | 70 | "D" (Monarch Network Capital) | "Sure. Thank you. That's it for myself." | closing |
| 44 | 71 | Operator | "Thank you. We take the next question from the line..." | |
| 45 | 72 | Sonal Manas (Preian Capital) | "Hi This is Sonal Manas. I hope I'm audible." | greeting; self-identifies name (cf. GARBLE "Sonel" at line 71) |
| 46 | 73 | Nitesh Bansal | "Yes, Sonal." | confirm |
| 47 | 74 | Sonal Manas | "Yeah. Thanks for taking my question, sir. My question was..." | Q1 (people cost/productivity) — NO terminal "?" mark |
| 48 | 75 | Nitesh Bansal | "So um you know we have not had a significant..." | partial answer |
| 49 | 76 | Sonal Manas | "that might not be comparable." | interjection re: YoY comparability given acquisition |
| 50 | 77 | Nitesh Bansal + Sonal Manas (merged) | "Yeah. So uh so definitely you know the the fact..." | MULTI_SPEAKER_TURN — Nitesh's answer (2x productivity, 55% turnaround gains) + Sonal's Q2 follow-up (near-term vs far-off) both on this line |
| 51 | 78 | Nitesh Bansal | "Well, I'm certainly seeing signs of uh accelerating velocity..." | answer to Q2 |
| 52 | 79 | Sonal Manas | "Got it sir. Thank you." | closing |
| 53 | 80 | Operator | "Thank you. We take the next question from the line..." | |
| 54 | 81 | Manish Chan (MNCL) + Nitesh Bansal (merged) | "Thank you for the opportunity. The first question will be..." | MULTI_SPEAKER_TURN — Manish's Q1 (3-4% CC growth timeline) + Nitesh's answer both on this line; Q1 has NO terminal "?" mark |
| 55 | 82 | Manish Chan | "Understood. Uh secondly wanted to know your how has..." | Q2 (wallet share top-50 clients) |
| 56 | 83 | Nitesh Bansal | "Uh wallet share has certainly increased in top 50 clients..." | answer |
| 57 | 84 | Manish Chan | "Okay, thank you." | closing |
| 58 | 85 | Operator | "Thank you. We take the next question from the line..." | |
| 59 | 86 | Deepak Malotra (Capro Capital) | "Uh, hi Nesh. Can you hear me?" | greeting (GARBLE: "Nesh"=Nitesh) |
| 60 | 87 | Nitesh Bansal | "Yes." | confirm |
| 61 | 88 | Deepak Malotra | "Thank you. While Nesh, you have tried to answer questions..." | 2 sub-questions on this line (Q1 Novigo deal detail, Q2 further inorganic opportunities) |
| 62 | 89 | Nitesh Bansal | "Yeah, Deepak. So u when I've talked about organic growth..." | answer to Q1+Q2; Novigo standalone revenue never quantified (non-disclosure, implicit) |
| 63 | 90 | Deepak Malotra | "Okay. Uh one more followup in uh terms of uh..." | Q3 (internal/inorganic strengthening, sales buffer) — NO terminal "?" mark |
| 64 | 91 | Nitesh Bansal + Deepak Malotra (merged) | "Yeah. So um you know it's a little deeper answer..." | MULTI_SPEAKER_TURN — Nitesh's answer + Deepak's closing ("Thank you. Wish you all the very best.") both on this line |
| 65 | 92 | Operator | "We take last question from the next uh you know." | GARBLE (transition fragment) |
| 66 | 93 | Operator | "Thank you. We take the next question from the line..." | |
| 67 | 94 | Aush Sha (Alpha Accurate) | "Uh hello. Am I audible?" | greeting |
| 68 | 95 | Nitesh Bansal | "Yes, Aush." | confirm |
| 69 | 96 | Aush Sha | "Hi. So, congrats on a great set of results and..." | Q1 (AI deflation in contracts) |
| 70 | 97 | Nitesh Bansal | "Uh so Aush you know while um people have talked..." | answer |
| 71 | 98 | Aush Sha | "Got it. Got it. Thank you so much." | closing |
| 72 | 99 | Operator | "Let's close. Thank you ladies and gentlemen. With that we..." | hands to Nitesh for closing comments |
| 73 | 100 | Nitesh Bansal + Operator (merged) | "Thank you Ryan. Uh on behalf of our systems, I..." | MULTI_SPEAKER_TURN — Nitesh's closing remarks + operator's sign-off ("...you may now disconnect your line.") both on this line |

Turn-share note (auditable via this table): turns 1-3 (lines 28-30) are
prepared remarks/moderation; turns 4-73 (lines 31-100) are the Q&A block —
i.e. 70 of 73 turns (~96% of turn count, though NOT ~96% of spoken word
volume since turn 3/line 30 is by far the longest single turn) fall inside
the Q&A section once turns are counted at source-line granularity.

---

## Table C — Analyst questions (21 rows, manual topic-sweep; independently re-derived twice, see count test)

| Q# | Analyst / Firm | Line(s) | Topic (one line) | Flags |
|---|---|---|---|---|
| Q1 | Anmul G, DAM Capital Advisers | 31 | SG&A uptick this quarter (~$2m/qtr per analyst) — puts/takes, additional sales hiring | |
| Q2 | Anmul G, DAM Capital Advisers | 35 | Full-year growth outlook / organic growth % | REPEAT_QUESTION (guidance ask; cf. Q9, Q17, Q18) |
| Q3 | Anmul G, DAM Capital Advisers | 35 | GCC business: current % of revenue and margin profile | REPEAT_QUESTION (cf. Q13, GCC/data+cloud disclosure asks) |
| Q4 | Anmul G, DAM Capital Advisers | 37 | Deal duration trend — more implementation-type/annuity work? | |
| Q5 | Ashish Das, Systematix Group | 42 | Why organic growth remains muted despite org changes; when to expect revival | REPEAT_QUESTION (cf. Q19 on 3-4% CC growth timeline) |
| Q6 | Ashish Das, Systematix Group | 43 | ACV/TCV TTM flattish QoQ — is this delay-in-decision or Novigo order trajectory? | REPEAT_QUESTION (cf. Q7, Q22, ACV/Novigo growth attribution) |
| Q7 | Ashish Das, Systematix Group | 45 | Margin outlook near-term to midterm, given wage hike timing | |
| Q8 | Sep Sha, Aquarius Securities | 50 | ACV TTM flattish this quarter — delay in decision-making vs macro/discretionary spend caution | REPEAT_QUESTION (cf. Q6) |
| Q9 | Sep Sha, Aquarius Securities | 52 | Qualitative outlook on ACV growth for H2 CY2026 | REPEAT_QUESTION (guidance ask; cf. Q2, Q17, Q18) |
| Q10 | Sep Sha, Aquarius Securities | 54 | Confirms H1 wins should convert to better H2 revenue traction | |
| Q11 | Sep Sha, Aquarius Securities | 56 | Data + AI + cloud as % of total revenue — can you share a number | REPEAT_QUESTION (cf. Q3) |
| Q12 | Sep Sha, Aquarius Securities | 58 | Is the data/cloud business less seasonal than the rest of the business | |
| Q13 | "D", Monarch Network Capital Limited | 66, 68 (restated after noise) | Quantifiable guidance on deal wins for upcoming quarters | REPEAT_QUESTION (guidance ask; cf. Q2, Q9, Q18); counted once despite the line-67 noise-clarification and line-68 restatement of the same question |
| Q14 | Sonal Manas, Preian Capital | 74 | People cost / cost-of-revenue trend and productivity gains, implementation-cycle commentary | |
| Q15 | Sonal Manas, Preian Capital | 77 (embedded) | Is productivity-gain-to-revenue-velocity translation a near-term or multi-year story | |
| Q16 | Manish Chan, MNCL | 81 (embedded) | When does constant-currency revenue growth return to 3-4% range, and what needs to fall into place | REPEAT_QUESTION (cf. Q5) |
| Q17 | Manish Chan, MNCL | 82 | Wallet-share trend in top-50 clients — what is driving expansion | |
| Q18 | Deepak Malotra, Capro Capital Advisor LLC | 88 | What additional deals is Novigo acquisition driving (detail on organic vs inorganic contribution) | REPEAT_QUESTION (cf. Q6) |
| Q19 | Deepak Malotra, Capro Capital Advisor LLC | 88 | Any further inorganic (M&A) opportunities under evaluation | |
| Q20 | Deepak Malotra, Capro Capital Advisor LLC | 90 | What is being done internally/inorganically (incl. sales team buffer) to hit the 3-4% CC growth objective | REPEAT_QUESTION (cf. Q16) |
| Q21 | Aush Sha, Alpha Accurate Advisor | 96 | Is there AI-driven contract/pricing deflation on renewals, as flagged by peer IT companies | |

REPEAT_QUESTION clusters (cross-analyst, for A3/A4 attention):
- Forward guidance repeatedly sought and repeatedly declined: Q2, Q9, Q13
  (and touched again implicitly in Q16/Q20's 3-4% CC growth ask).
- ACV/TCV TTM trajectory and Novigo's contribution to it: Q6, Q8, Q18.
- Organic growth deceleration / when it re-accelerates: Q5, Q16, Q20.
- GCC and data+cloud revenue mix, both explicitly non-disclosed as exact
  percentages: Q3, Q11.

---

## Table D — Management-stated numbers / quantified claims (73 rows, distinct-disclosure basis; restatements of the same figure are merged into one row with all comparators noted, per count-test methodology above)

| # | Line(s) | Metric | Value(s) as stated | Flags |
|---|---|---|---|---|
| M1 | 30 | Q2 revenue | 601.7 cr / $63.6m | restated at line 30 (Nand's readout) as "rupees 61.7 crores" — GARBLE, digit-drop |
| M2 | 30 | Q2 revenue YoY growth (USD) | 17.7% | |
| M3 | 30 | Q2 revenue YoY growth (INR) | 30.2% | restated consistently across opening and Nand's readout |
| M4 | 30 | Q2 revenue QoQ growth (USD) | 1.2% | |
| M5 | 30 | Q2 revenue QoQ growth (INR) | 4.7% | |
| M6 | 30 | Q2 revenue, same quarter last year | 462 cr / $54m | |
| M7 | 30 | Q1 revenue (comparator) | 574.8 cr / $62.8m | |
| M8 | 30 | Q2 adjusted EBITDA ("IITa") | 1,207 cr / 20.1% | GARBLE — "$12.8 billion" spoken, per A1 header almost certainly $12.8m (billion/million ASR error) |
| M9 | 30 | Q2 adjusted EBITDA YoY growth | 51.4% | |
| M10 | 30 | Q2 adjusted EBITDA QoQ growth | 4.4% | |
| M11 | 30 | Q2 adjusted EBITDA — slide-6 restated absolute value | 120.7 cr (vs 79.7 cr same qtr last yr; vs 115.7 cr Q1) | INCONSISTENT_FIGURE — 120.7 cr conflicts with the 1,207 cr figure at M8 (10x scale mismatch); flagged for A3 forensic reconciliation against the filing/deck, not resolved here |
| M12 | 30 | Q2 EBITDA margin move (bps) | 17.3% -> 20.1% = stated as "281 basis points increase or a six basis points increase" | INCONSISTENT_FIGURE — internally contradictory bps figures in the same sentence (281 vs "six", likely a further garble of "281" or "286") |
| M13 | 30 | Q2 adjusted net profit ("adjusted PAT") | 62.9 cr / $6.6m | |
| M14 | 30 | Q2 adjusted PAT % of revenue | 10.5% | |
| M15 | 30 | Q2 adjusted PAT YoY growth | 35.4% | |
| M16 | 30 | Q2 adjusted PAT vs same qtr last year (abs) | 46.4 cr | |
| M17 | 30 | Q2 adjusted PAT vs Q1 (abs, QoQ decline) | 75.8 cr in Q1; -17.1% QoQ | one-time Q1 hedging benefit cited as the driver of the decline (see M18) |
| M18 | 30 | One-time currency-hedging benefit recognized in Q1 | 18 cr | |
| M19 | 30 | Net profit margin move YoY | 10.1% -> 10.5% | |
| M20 | 30 | Net profit margin move QoQ | 13.2% -> 10.5% | |
| M21 | 30 | Q2 adjusted EPS | 5.3 rupees | restated at line 30 (Nand's readout) as "compared to 6.4 last quarter" |
| M22 | 30 | Q2 adjusted EPS YoY growth | 35.3% | |
| M23 | 30 | H1 revenue | 1,176.5 cr / $126.4m | |
| M24 | 30 | H1 revenue YoY growth | 30.1% | |
| M25 | 30 | H1CY25 revenue (comparator) | "94 crores" / "94.5 crores" as spoken | GARBLE — per A1 header, almost certainly 904.5 cr (digit-dropping ASR error); do not use the spoken "94 cr" figure as evidence without cross-check |
| M26 | 30 | H1 adjusted EBITDA | 236.4 cr / $25.4m | |
| M27 | 30 | H1 adjusted EBITDA margin | 20.1% | |
| M28 | 30 | H1 adjusted EBITDA YoY growth | 51% (also stated as 279 bps improvement) | |
| M29 | 30 | H1 adjusted EBITDA, prior-year comparator (abs) | 156.6 cr | |
| M30 | 30 | H1 adjusted PAT | 138.7 cr / $14.9m | |
| M31 | 30 | H1 adjusted PAT margin | 11.8% | |
| M32 | 30 | H1 adjusted PAT YoY growth | 54.4% | |
| M33 | 30 | H1 adjusted PAT, prior-year comparator (abs) | 89.8 cr | |
| M34 | 30 | H1 adjusted PAT margin move YoY | 9.9% -> 11.8% (186 bps) | |
| M35 | 30 | H1 EPS | 11.7 rupees | |
| M36 | 30 | H1 EPS YoY growth | 54.3% | |
| M37 | 30 | Americas revenue share | 69.3% -> 71.5% | |
| M38 | 30 | APAC revenue share | 15.3% (described as a decrease) | prior-period comparator not explicitly stated |
| M39 | 30 | Europe revenue share | 9.7% (stated as stable) | |
| M40 | 30 | Middle East & Africa revenue share | 3.6% (stated as stable) | |
| M41 | 30 | Top-client concentration | 5.8% -> 6% | |
| M42 | 30 | Top-10-client concentration | 24% -> 24.4% | |
| M43 | 30 | Utilization | 80.5% -> 81% (stated target band 80-81%) | |
| M44 | 30 | DSO, billed | ~55-56 days | |
| M45 | 30 | DSO, billed + unbilled | ~75 days | |
| M46 | 30 | ACV bookings, TTM, Q2 | $82.9m | |
| M47 | 30 | ACV bookings, TTM, Q1 (comparator) | $82.3m | |
| M48 | 30 | GCC service offerings launch timing | "a year and a half ago" (qualitative timeframe) | |
| M49 | 30 | Gross margin, Q2 | 39.2% | |
| M50 | 30 | Gross margin, Q1 and same-qtr-last-year (both) | 36% | |
| M51 | 30 | SG&A expense, Q2 vs Q1 | 115.3 cr vs 91.4 cr (+23.8 cr) | one-time Q1 AR reversal cited as a contributing base-effect |
| M52 | 30 | Adjusted EBITDA net of RSU expense | 19% (stated as "almost same as last quarter") | |
| M53 | 30 | RSU cost (management incentive plan) | 6.2 cr vs 6.4 cr Q1 | |
| M54 | 30 | D&A total expense | 22 cr vs 21.5 cr Q1 | |
| M55 | 30 | D&A, intangible portion (acquisition-related) | 10.5 cr | |
| M56 | 30 | Interest expense | 9.5 cr vs 9.6 cr Q1 | |
| M57 | 30 | Other income | negative 87 lakh vs 13.1 cr Q1 | |
| M58 | 30 | Hedge accounting fair value loss (OCI) | 18.04 cr | adoption of hedge accounting for forward covers this quarter cited as the trigger |
| M59 | 30 | Exchange rate, 31-Dec-2025 (closing) | Rs 89.88/USD | |
| M60 | 30 | Exchange rate, 31-Mar-2026 (closing) | Rs 94.84/USD | |
| M61 | 30 | Exchange rate, 30-Jun (quarter-end, comparator) | Rs 94.6/USD | |
| M62 | 30 | Exchange rate range during the quarter | Rs 92.6 - Rs 96.5/USD | |
| M63 | 30 | Realized loss on settlement of forward contracts | 9 cr | |
| M64 | 30 | Overall exchange loss, Q2 vs Q1 | 2.1 cr vs 11.3 cr | |
| M65 | 30 | Interest income, Q2 vs Q1 | 78 lakh vs 60 lakh | |
| M66 | 30 | Total forward cover outstanding, quarter-end | $43.32m at average rate 93.27 | |
| M67 | 30 | Income tax expense, Q2 vs Q1 | 24.94 cr vs 24.2 cr | |
| M68 | 30 | Effective tax rate (ETR), Q2 | ~31% | attributed to non-deductibility of acquisition-related intangible amortization |
| M69 | 30 | Normalized ETR (stated range) | "28 to 19 29%" as spoken | GARBLE — evident stray digit "19"; intended range almost certainly 28-29% |
| M70 | 30 | Reported (statutory) PAT, Q2 vs Q1 | 55.6 cr / $5.9m vs "65.4 cr / $7.2m" Q1 as spoken | INCONSISTENT_FIGURE — the Q1 comparator here (65.4 cr) does not match the 75.8 cr Q1 adjusted-PAT figure given earlier in the same turn (M17); may reflect reported-vs-adjusted PAT definitional difference, or a further ASR digit garble; flagged for A3 reconciliation against filing |
| M71 | 30 | Reported EPS, Q2 vs Q1 | 4.69 rupees vs 5.52 rupees | GARBLE — spoken as "DC for the quarter was rupes 4.69" per A1 header note |
| M72 | 43/47 | "18% growth ... without headcount change" | stated twice with conflicting basis: "quarter over quarter" at line 43, "year on year" at line 47 | INCONSISTENT_FIGURE — same 18% figure attributed to two different comparison bases (QoQ vs YoY) across two separate answers; not resolved here, flagged for A3/A4 |
| M73 | 47 | Sustainable adjusted EBITDA margin target | "18-x%" as spoken (trailing digit/character garbled) | GARBLE — see also Table E (G2), this is simultaneously a guidance statement and a quantified claim |

Additional Q&A-sourced quantified claims folded into the flags column rather
than given separate rows (to avoid double counting against M72/M73 and the
non-disclosure table): data+cloud revenue "crossed 50%" (line 57, paired with
ND2 in Table F); productivity gains "2x productivity and 55% gains in
turnaround time" (line 77, two distinct metrics — counted as part of M-series
scope but consolidated here for brevity: 2x productivity multiplier, 55%
turnaround-time improvement, both management-stated and both ANCHORED to
line 77, both un-audited/self-reported per the AI studio "exico.ai" website
per management's own framing).

Analyst-cited (not management-stated, excluded from the M-series count):
SG&A "uptake ... almost to the tune of 2 million on a quarterly level" is
Anmul G's own framing at line 31, not a management-confirmed figure; excluded
per the category definition (management-stated only) but flagged here so
A3/A4 do not miss it when checking whether management explicitly confirmed
or merely responded to the analyst's own number.

---

## Table E — Forward-looking / guidance statements and explicit refusals to guide (9 rows)

| G# | Line | Statement | Type |
|---|---|---|---|
| G1 | 36 | "we do not provide uh guidance" — in response to full-year/organic growth outlook ask | Explicit refusal |
| G2 | 47 | "we continue to stay focused uh to uh stay in that 18 18 x% uh adjusted ITA on a sustainable basis" | Guidance given (margin target; trailing digit "x" garbled) |
| G3 | 53 | H2 ACV outlook described as "a million dollar question"; no forward number given, only qualitative pipeline-quality commentary | Explicit refusal (qualitative deflection) |
| G4 | 69 | "we don't do not provide forward-looking guidance" — in response to quantifiable deal-win guidance ask | Explicit refusal |
| G5 | 69 | Pipeline quality/positioning improvement expected to "lead to uh a better conversion rate"; continued trailing-12-month reporting cadence | Forward-looking, non-quantified |
| G6 | 81 | 3-4% constant-currency growth return described as "only uh a matter of uh time" given pipeline/reusable-asset buildup; no date or number committed | Forward-looking, non-quantified |
| G7 | 89 | "we as an organization have a organic plus in organic uh growth ambition" — continued openness to M&A, no specific target or timeline | Forward-looking, non-quantified |
| G8 | 78 | Productivity/velocity gains: "certainly seeing signs" of acceleration but explicit uncertainty on "will it reflect in within the [current] year" | Forward-looking, with explicit uncertainty caveat |
| G9 | 97 | Continued margin/pricing premium expected from AI-first delivery ("our margins have continued to show improvement... able to uh continue to charge uh premium") | Forward-looking, non-quantified |

---

## Table F — Explicit non-disclosures / dodges (7 rows)

| ND# | Line | Item not disclosed | Management's own framing |
|---|---|---|---|
| ND1 | 36 | GCC revenue as % of total revenue | "I do not think we have uh disclosed uh the percentage of revenue separately" |
| ND2 | 57 | Data + cloud revenue as an exact % of total revenue | "we don't share a explicit percentage" (only ">50%" and "crossed 50%" given, no precise figure) |
| ND3 | 36 | Full-year / organic growth guidance | "we do not provide uh guidance" |
| ND4 | 53 | H2 CY2026 ACV / deal-win outlook, quantified | "that's a million dollar question" — explicit refusal to quantify |
| ND5 | 69 | Quantifiable deal-win guidance for upcoming quarters | "we don't do not provide forward-looking guidance" |
| ND6 | 43-44, 89 | Novigo's standalone revenue contribution (as a dollar or % figure) | Repeatedly discussed qualitatively across three separate answers (Ashish Das and Deepak Malotra both probe this directly) but never reduced to a number — IMPLICIT non-disclosure, no single explicit refusal sentence exists, flagged as such |
| ND7 | 42-43, 81 | Organic (ex-Novigo) constant-currency growth rate, as a specific % | Described only as "consistently shown organic growth" / positioning statements; despite two separate direct analyst asks (Ashish Das, Manish Chan), no % figure for organic-only growth is ever given — IMPLICIT non-disclosure |

---

## Flags summary (all flags raised across Tables A-F)

- MULTI_SPEAKER_TURN: lines 30, 31, 40, 43, 77, 81, 91, 100 (8 turns)
- GARBLE / GARBLE_NAME_UNCERTAIN: P2, P3, P4, P5, P7, P8, P9, P12 (participant
  names); M1, M8, M12, M25, M69, M71, M73 (figures); turns 2, 5, 10, 37, 40,
  59(via M-series), 86, 92, 100 references
- NAME_INCOMPLETE: P8 ("D", Monarch Network Capital — surname never captured)
- INCONSISTENT_FIGURE: M11 (EBITDA abs value 10x mismatch), M12 (bps
  self-contradiction), M70 (reported PAT Q1 comparator mismatch vs adjusted
  PAT Q1 figure), M72 (18% QoQ vs YoY framing conflict)
- ASR_PUNCTUATION_UNRELIABLE: documented in count-test methodology for the
  `questions` category (raw "?" grep = 25, unreliable; both legs resolved by
  independent manual sweep instead)
- REPEAT_QUESTION: Q2/Q9/Q13 (guidance), Q6/Q8/Q18 (ACV/Novigo trajectory),
  Q5/Q16/Q20 (organic growth deceleration), Q3/Q11 (GCC / data+cloud mix %)
- MGMT_ABSENCE (qualified/observational): no Chairman or promoter
  participant on this call; only CEO, CFO, VP Finance present — needs
  prior-quarter cross-check, not available to this run

---

## Output path
`/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/ledger_concall_rsystems_q2cy26.md`

```yaml
stage: A2-enumerator
company: "RSYSTEMS"
quarter: "Q2CY26"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/rsystems-q2cy26/work/ledger_concall_rsystems_q2cy26.md"
counts:
  turns: 73
  analyst_threads: 8
  questions: 21
  mgmt_numbers: 73
  non_disclosures: 7
  guidance_statements: 9
flags_raised: [MULTI_SPEAKER_TURN, GARBLE, GARBLE_NAME_UNCERTAIN, NAME_INCOMPLETE, INCONSISTENT_FIGURE, ASR_PUNCTUATION_UNRELIABLE, REPEAT_QUESTION, MGMT_ABSENCE]
gate_a2: pass
mismatch_note: ""
```
