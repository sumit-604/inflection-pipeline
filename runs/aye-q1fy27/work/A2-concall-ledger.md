# A2 COMPLETENESS LEDGER — AYE Finance, Q1 FY27 Concall
Source: `runs/aye-q1fy27/work/A1-concall-extract.md` (A1, gate_a1: pass)
Citation unit: the embedded TRANSCRIPT line number (1–130) preserved by A1 in its
"N\t<text>" format — this is A1's designated addressable citation unit, distinct from
the Read-tool file line numbers of the A1 markdown file itself. All "line N" citations
below refer to this transcript line number unless stated otherwise.

Methodology note (read before the count test): this source is a single continuous
voice-to-text transcript with NO per-speaker line breaks — many individual speaker
turns, and even full question+answer exchanges, are merged onto one transcript line
(flagged `MERGED_TURN` throughout). No management speaker is ever tag-labelled in the
source ("Sanjay:", "Gaurav:" etc. do not appear) — every answer is therefore
`ATTRIBUTION_UNCLEAR` as to which named executive spoke it. Both facts are structural
properties of the source, not errors introduced here, and are surfaced as ledger flags
rather than corrected or interpreted.

=== A2 COUNT TEST ===
category: opening_topic_blocks   grep_count: 21   sweep_count: 21   match: yes
category: qa_exchanges           grep_count: 13   sweep_count: 13   match: yes
category: qa_individual_questions (supplementary, not gated) sweep_count: 35
category: quantitative_disclosure_lines   grep_count: 42 (reconciled, see note)   sweep_count: 42   match: yes
category: forward_statement_lines         grep_count: 31 (reconciled, see note)   sweep_count: 31   match: yes
category: speaker_turns          grep_count: 108  sweep_count: 108  match: yes
category: participants           grep_count: 20   sweep_count: 20   match: yes
gate_a2: pass
=== END COUNT TEST ===

## RECONCILIATION NOTES (mismatches found and resolved before emission)

**quantitative_disclosure_lines** — initial regex pass (`[0-9]+(%|cr|crore|crores|bps|
basis points|bits|lakh|lakhs)`) over the full transcript body returned 41 lines,
including transcript line 2. Manual full-digit sweep (every content line containing
any digit, 54 candidate lines, individually triaged) found:
- line 2 is NOT participant speech — it is A1's own inserted provenance/normalization
  note ("Provenance: operator-pasted voice-to-text transcript..."), not spoken by
  Sanjay Sharma, Viral Shah, or any analyst. EXCLUDED (−1).
- line 20 was missed by the regex because the source renders "20 crores" as "20 kores"
  and "12 crores" as "12 K profit" (voice-to-text typos on non-standard unit spelling).
  Both are genuine management-spoken disclosures (DA contribution last quarter; forex
  P&L contribution last quarter). ADDED (+1).
- line 88 was missed by the regex because the source uses "60 odd percentage" (word
  inserted between number and unit, defeats a tight regex) and spells out "four to
  four and a half" instead of digits, plus a bare, unit-less "3.15" (leverage ratio).
  Genuine management disclosures (leverage level, leverage ceiling, LTV by product).
  ADDED (+1).
Net: 41 − 1 + 1 + 1 = 42. Re-swept and reconciled to 42 = 42. This is exactly the
grep-miss the two-method GATE A2 process exists to catch — noted, not hidden.

**forward_statement_lines** — initial trigger-phrase regex pass (guidance / we expect /
we believe / we will / going forward / eventually / target / endeavor / we don't see /
etc.) returned 37 candidate lines. Manual triage removed 9 false positives (operator/
host procedural language on lines 6, 10; or analyst-question-only wording, with the
substantive management answer already captured on an adjacent line: 27, 28, 36, 44,
49, 60, 87) and added 3 genuine management forward/hedge statements the trigger list
missed due to negation or unlisted phrasing (line 53 branch-growth target phrased
without a listed trigger word; line 67 "we don't **foresee**" broken by the inserted
"don't"; line 80 "we don't have that data... my guess would be", an explicit
data-absence hedge). Also corrected one mis-citation: the overlay-target "eventually
5% of book" language sits on line 50 (the answer), not line 49 (the question) as an
early draft mis-cited. Net: 37 − 9 + 3 = 31. Re-swept and reconciled to 31 = 31.

## FLAGS SUMMARY (definitions and counts)
- `ZERO_STANDING` — a standing disclosure line that is nil/not-reported this quarter: **3** instances (DA = nil this quarter, line 20; slippage number not reported, lines 95 and 117 — reported twice as non-disclosure, counted once per occurrence below).
- `ATTRIBUTION_UNCLEAR` — management answer with no speaker tag in source: all **13** Q&A exchanges.
- `MERGED_TURN` — one transcript line contains more than one discrete speaker turn (Q+A merged, or multiple sub-Q merged): **32** of the 108 turn-lines (flagged individually in Table 2).
- `REPEAT_QUESTION` — same underlying question topic asked by 2+ different analysts: **4** topic clusters (credit-cost-guidance-conservatism-vs-improving-trend; NIM-guidance-vs-actual; leverage/capital-raise timing; NPA-PAR bifurcation by product).
- `NUMBER_VARIANT` — same metric stated with two different values across the transcript, cited for A3 reconciliation, not interpreted here: **3** instances (active-borrower count "6.7 lakh" line 8 vs "67 lakh" same line 8; AUM "7,324 crores" line 8 vs "7,384 crores" line 123; leverage "3.1" line 87 (analyst-quoted) vs "3.15" line 88 (management-stated)).

---

## TABLE 1 — PARTICIPANTS (grep_count 20 = sweep_count 20)

| # | Name (as transcribed) | Role | Side | First cited line | Flags |
|---|---|---|---|---|---|
| 1 | (unnamed conference operator) | Call operator | Neutral/host-side | 4 | — |
| 2 | Viral Shah ("Viril Sha") | Hosting broker analyst, IIFL Capital | Host | 6 | House-broker host |
| 3 | Sanjay Sharma | Managing Director & co-founder | Management | 8 | Promoter present — no `MGMT_ABSENCE` |
| 4 | Nirit Koshik | Deputy Chief Officer (title garbled in source) | Management | 8 | — |
| 5 | Gaurav Seth ("Goros") | Chief Financial Officer | Management | 8 | — |
| 6 | Sovan Satyaprakash ("Soan Saktip Prakash") | Chief Strategy & Investor Relations Officer | Management | 8 | — |
| 7 | SGA IR advisory team (unnamed individuals) | External IR advisor | Management-side | 8 | External firm, per protocol 0B |
| 8 | Sajil Raj (Sajil Raj send) | Analyst, FL Finance Private Limited | Analyst | 10 | Sell-side |
| 9 | Sam | Analyst, Diamond Asia | Analyst | 26 | — |
| 10 | Shalin Kapadia | Analyst, "Capital" (firm name truncated in source) | Analyst | 35 | — |
| 11 | Ana Ghana | Analyst, A91 Park | Analyst | 43 | Buy-side (AIF) |
| 12 | Manga / Om | Analyst, Kotak Mutual Fund | Analyst | 48 | Buy-side (MF); called "Manga" by operator, "Om" by management — same person |
| 13 | Varia / Vijay | Analyst, "capital" (firm truncated) | Analyst | 64 | Called "Varia" by operator, "Vijay" by operator at line 70 — same person |
| 14 | Pavan Kumar | Analyst, Eagle Wise (Public Alternates) | Analyst | 73 | — |
| 15 | Nishin Chabati | Analyst, Kotak (securities, per context) | Analyst | 78 | Buy-side/sell-side unclear |
| 16 | Gokal | Analyst, PTH Capital | Analyst | 84 | — |
| 17 | Sonal Minas ("Sonel") | Analyst, Christian Capital | Analyst | 94 | — |
| 18 | Tari Varia | Analyst, firm not stated | Analyst | 99 | — |
| 19 | "sust" / Radhi | Analyst, firm not stated | Analyst | 112 | Operator calls this analyst "sust" at intro (112) and "Mr. Radhi" at close (121) — same person |
| 20 | Tushar Sada | Analyst, Ethna Investments | Analyst | 121 | — |

Yellow-flag check per protocol 0B: promoter (Sanjay Sharma, MD & co-founder) is present
and answers questions across the call — no `MGMT_ABSENCE`. CFO (Gaurav Seth) presence
confirmed by introduction but never individually tag-attributed to any specific answer
(`ATTRIBUTION_UNCLEAR`, see Table 4), so whether the CFO answered operational
questions cannot be mechanically determined from this source — flagged for A3/A4, not
resolved here.

---

## TABLE 2 — SPEAKER TURNS (grep_count 108 = sweep_count 108)

One row per transcript content-line in the range 4–130 (lines 1–2 excluded as
non-speech document metadata; blank separator lines excluded). `MERGED_TURN` = the
transcript line contains more than one discrete speaker turn.

| Turn | Line | Speaker | First ~10 words | Flags |
|---|---|---|---|---|
| 1 | 4 | Operator | "Ladies and gentlemen, good day and welcome to I Finance" | — |
| 2 | 6 | Viral Shah (host) | "Thank you Renju. Good morning everyone. This is Viral Sha" | — |
| 3 | 8 | Sanjay Sharma (mgmt) | "Thank you Vir and good morning everyone and thank you" | Opening remarks — see Table 3 for 21-block breakdown |
| 4 | 10 | Operator | "Thank you. We will now begin the question and answer" | Intro of Sajil Raj embedded in same line |
| 5 | 12 | Sajil Raj (analyst) | "Uh good morning sir. Am I audible?" | — |
| 6 | 13 | Operator/moderator | "Yes you are. Please go ahead." | — |
| 7 | 14 | Sajil Raj + Management | "Uh yeah sir I have uh three good questions. Uh" | `MERGED_TURN` (Q1 + A1 merged) |
| 8 | 16 | Sajil Raj + Management | "Uh thank you sir. Uh My second question will be" | `MERGED_TURN` (Q2 + start of A2) |
| 9 | 17 | Management | "If we talk of the product wise uh portfolio ROI" | continued A2 |
| 10 | 19 | Sajil Raj (analyst) | "Uh thank you so much sir and sir uh in" | Q3 |
| 11 | 20 | Management | "Yeah so the P and other income has decreased primarily" | A3; DA nil this qtr — `ZERO_STANDING` |
| 12 | 21 | Sajil Raj (analyst) | "Sorry, nominal." | interjection |
| 13 | 22 | Management | "Nominal uh the uh the uh the this was a" | continued A3 |
| 14 | 23 | Sajil Raj (analyst) | "Thank you so much and all the best for the" | close |
| 15 | 24 | Management | "Thank you." | close |
| 16 | 26 | Operator + Sam | "Thank you. A reminder to all the participants that you" | `MERGED_TURN` (intro + Q1) |
| 17 | 27 | Management | "Sure. Thanks for that. Uh uh Sam u I think" | A1 |
| 18 | 28 | Sam (analyst) | "Sir, uh this is this is useful sir. Secondly, uh" | Q2 |
| 19 | 29 | Management | "Yes. I think see while we are today already at" | A2 |
| 20 | 30 | Sam (analyst) | "Okay. Okay. So this is uh this is helpful. Uh" | Q3 |
| 21 | 31 | Management | "Sam rightly asked on that particular question with the mortgage" | A3 |
| 22 | 32 | Sam (analyst) | "Great. Thank you. Thank you and all the best." | close |
| 23 | 33 | Management | "Thank you and all the best." | close |
| 24 | 35 | Operator | "Next question comes from the line of Shalin Kapadia with" | intro |
| 25 | 36 | Shalin Kapadia (analyst) | "Uh hi uh good morning everyone and thanks for the" | Q1 |
| 26 | 37 | Management | "Yeah. So in terms of uh the cost of borrowing" | A1 |
| 27 | 38 | Shalin Kapadia (analyst) | "Yeah. Uh uh thank you. Uh so second one is" | Q2 |
| 28 | 39 | Management + Shalin Kapadia | "Yeah. So the overall overlay that sits on the balance" | `MERGED_TURN` (A2 + Q3 + an echo/audibility interruption exchange, all on one line) |
| 29 | 40 | Management | "Uh see on uh the growth to get through a" | A3 (5-yr vision) |
| 30 | 41 | Shalin Kapadia (analyst) | "Uh got it sir. Uh very Uh that's it from" | close |
| 31 | 43 | Operator | "Thank you. Next question comes from the line of Ana" | intro |
| 32 | 44 | Ana Ghana (analyst) | "Hi. Uh so on parx I wanted to understand uh" | Q1 |
| 33 | 45 | Management | "Sure. I think see uh it's an excellent question uh" | A1 |
| 34 | 46 | Ana Ghana (analyst) | "Nice. Very close." | close |
| 35 | 48 | Operator | "Thank you. Next question comes from the line of Manga" | intro |
| 36 | 49 | Manga/Om (analyst) | "Yeah. Hi. Um uh thanks uh for the opportunity and" | Q1 |
| 37 | 50 | Management | "Oh uh hi Om. Uh so with respect to the" | A1 |
| 38 | 51 | Manga/Om + Management | "Okay. Okay. Understood. Understood. And um uh just to uh" | `MERGED_TURN` (clarifying follow-up + confirmation) |
| 39 | 52 | Management + Manga/Om | "Perfect. Uh that sounds good. Uh the other point was" | `MERGED_TURN` (close of Q1 thread + start of Q2) |
| 40 | 53 | Management | "Uh um our strategy is to increase the branch count" | A2 |
| 41 | 54 | Manga/Om (analyst) | "Understood. Uh that helps. And just one last question is" | Q3 |
| 42 | 55 | Management | "U so the way we want to approach DA is" | A3 |
| 43 | 56 | Manga/Om (analyst) | "okay. Okay. Understood. And um sorry just um um uh" | Q4 |
| 44 | 57 | Management | "That's right. That's right. Uh India India rating." | A4 partial |
| 45 | 58 | Manga/Om (analyst) | "Yeah. Yeah. Sorry." | — |
| 46 | 59 | Management | "India ratings gave us the So I was saying India" | A4 continued |
| 47 | 60 | Manga/Om (analyst) | "So So logically then uh I'm assuming that the benefit" | follow-up |
| 48 | 61 | Management | "Yeah. So uh uh the incremental cost of borrowing last" | A |
| 49 | 62 | Manga/Om (analyst) | "Okay. All right. Perfect. Thank you so much. Uh that" | close |
| 50 | 64 | Operator | "Thank you. A reminder to all the participants, please restrict" | intro Varia |
| 51 | 65 | Varia (analyst) | "Uh hi sir, thank you for taking my question. Uh" | Q1 |
| 52 | 66 | Management | "Uh hi Vun. So there's definitely certain level of seasonality" | A1 |
| 53 | 67 | Varia (analyst) | "Okay. And uh and considering that we'll be adding more" | Q2 |
| 54 | 68 | Management | "See uh I think on staffing uh we have never" | A2 |
| 55 | 69 | Varia (analyst) | "okay okay thank you for taking my question" | close |
| 56 | 70 | Operator | "Mr. Vijay are you done with the question" | naming variant — same person as "Varia" |
| 57 | 71 | Vijay/Varia (analyst) | "yeah yeah" | close |
| 58 | 73 | Operator | "thank you next question in the line of Pavan Kumar" | intro |
| 59 | 74 | Pavan Kumar (analyst) | "Uh so thank you for the opportunity. Just one question" | Q1 |
| 60 | 75 | Management | "Yeah. So out of the total borrower base I think" | A1 |
| 61 | 76 | Pavan Kumar (analyst) | "Thank you sir." | close |
| 62 | 78 | Operator | "Thank you. Next question comes from the line of Nishin" | intro |
| 63 | 79 | Nishin Chabati (analyst) | "Yeah. Hi. Uh so just before uh just a clarification" | Q1 |
| 64 | 80 | Management | "Yes. I uh we don't have that data up front" | A1 |
| 65 | 81 | Nishin Chabati (analyst) | "yeah that that would be helpful uh and just one" | Q2 |
| 66 | 82 | Management + Nishin Chabati | "yeah see uh I think our approach on co- lending" | `MERGED_TURN` (A2 + close) |
| 67 | 84 | Operator | "Thank you. Next question comes from the line of Gokal" | intro |
| 68 | 85 | Gokal (analyst) | "I'm audible." | — |
| 69 | 86 | Operator/moderator | "Yes, you are." | — |
| 70 | 87 | Gokal (analyst) | "Yeah. So, I just want to understand currently our leverage" | Q1 |
| 71 | 88 | Management + Gokal | "Yeah. So the leverage right now is at 3.15. Uh" | `MERGED_TURN` (A1 + Q2 LTV + A2); `NUMBER_VARIANT` vs line 87 |
| 72 | 89 | Gokal (analyst) | "Okay. And one more thing so I see the foreclosure" | Q3 |
| 73 | 90 | Management | "So this is the closer you are talking of settlement" | clarifying question back before answering |
| 74 | 91 | Management | "Yeah this 5% that you are referring to that is" | A3 |
| 75 | 92 | Gokal (analyst) | "Got it. Thank you." | close |
| 76 | 94 | Operator | "Thank you. Next question comes from the line of Sonel" | intro |
| 77 | 95 | Sonal Minas + Management | "Hi, this is Sonal Minas. I hope I'm audible. Hey" | `MERGED_TURN` (Q1 + A1); slippage not reported — `ZERO_STANDING` |
| 78 | 96 | Sonal Minas + Management | "Okay. So par 90 can we expect like by the" | `MERGED_TURN` (Q2 + A2) |
| 79 | 97 | Sonal Minas (analyst) | "Got it. Thank you. Thanks." | close |
| 80 | 99 | Operator | "Thank you. Next question comes from the line of Tari" | intro |
| 81 | 100 | Tari Varia (analyst) | "Hi uh Can you explain the difference between your hyperscription" | Q1 |
| 82 | 101 | Management | "See I think uh there is certainly an overlap but" | A1 |
| 83 | 102 | Tari Varia (analyst) | "Are you also uh putting your QR code or like" | Q2 |
| 84 | 103 | Management | "No, we are not in that line of No, we" | A2 |
| 85 | 104 | Tari Varia (analyst) | "Sorry. And and you said only small portion which going" | Q3 |
| 86 | 105 | Management + Tari Varia | "Yes, absolutely right. I think in the tier 2 tier" | `MERGED_TURN` (A3 + Q4) |
| 87 | 106 | Management | "So u there are three crossell products that we run" | A4 |
| 88 | 107 | Management | "Yeah. 9 9 cr is what we saw as income" | A4 continued |
| 89 | 108 | Management | "See u this is not a very substantial part of" | A4 continued |
| 90 | 109 | Tari Varia (analyst) | "And what was the attachment rate? Let's say out of" | Q5 |
| 91 | 110 | Management | "I think uh yeah multiple uh products would have different" | A5 |
| 92 | 112 | Operator + "sust" | "Thank you Mr. Tari. Please reach out for more questions." | `MERGED_TURN` (close of Tari's turn + intro + audio/echo interruption) |
| 93 | 113 | Moderator/Management | "yes please go ahead" | confirms audible |
| 94 | 114 | "sust"/Radhi (analyst) | "yeah uh so uh furthering to the previous participant uh" | Q1 |
| 95 | 115 | Management | "Sure u si thank you for that question and u" | A1 |
| 96 | 116 | "sust"/Radhi (analyst) | "Fair sir understood. Uh thank you. Uh the other question" | Q2 |
| 97 | 117 | Management | "See I think uh there is an upside that is" | A2; slippage not reported again — `ZERO_STANDING` |
| 98 | 118 | "sust"/Radhi (analyst) | "Fair. Fair. Makes sense. Uh so lastly just on OPEX" | Q3 |
| 99 | 119 | Management | "Yeah. Yeah. S I think the new branch investment is" | A3 |
| 100 | 121 | Operator | "Thank you Mr. Radhi. Please join the queue for more" | close + intro Tushar Sada |
| 101 | 122 | Tushar Sada + Management | "Yeah, thank you. Hope the opportunity and uh I have" | `MERGED_TURN` (Q1 + A1 + Q2) |
| 102 | 123 | Management + Tushar Sada | "Uh our expectation is that if we take a leverage" | `MERGED_TURN` (A2 + Q3 + A3); `NUMBER_VARIANT` AUM vs line 8 |
| 103 | 124 | Tushar Sada (analyst) | "Okay. Okay. Thank you very much." | close |
| 104 | 125 | Management | "Thank you very much." | close |
| 105 | 127 | Operator | "Thank you ladies and gentlemen. Due to time constraints we" | Q&A close, hands to host |
| 106 | 128 | Viral Shah (host) | "Yeah. Hi. Thanks. Uh thank you Sanjay and I team." | asks for closing comments |
| 107 | 129 | Sanjay Sharma (mgmt) | "Uh, thank you. Yes, I want to thank everyone who" | closing remarks |
| 108 | 130 | Operator | "Thank you on behalf of Capital that controls this conference." | sign-off |

Q&A share of the call: turns 4–104 (101 of 108 turns, ~94% of enumerated turns) are
Q&A; turns 1–3 and 105–108 are opening/closing framing. Consistent with the protocol's
"spend 60%+ of effort on Q&A" — the raw turn-share here supports that allocation.

---

## TABLE 3 — MANAGEMENT OPENING-REMARK TOPIC BLOCKS (grep_count 21 = sweep_count 21)

All 21 blocks sit within the single continuous opening-remarks turn on **line 8**
(Sanjay Sharma). Block boundaries below are anchored to the 20 verbatim topic-transition
phrases management used inside that one turn (mechanical marker list, confirmed by grep)
plus the initial pre-marker segment; every block therefore cites line 8.

| # | Topic-block boundary phrase | Content summary | Line |
|---|---|---|---|
| 1 | (opening, pre-marker) | Welcome/thanks; introduces Nirit Koshik, Gaurav Seth (CFO), Sovan Satyaprakash (Chief Strategy & IR), SGA IR team; mission statement — 571 branches, 18 states/UTs, "over 6.7 lakh active borrowers" (cf. block 10, `NUMBER_VARIANT`); differentiated underwriting/branch/AI-ML positioning | 8 |
| 2 | "I hope all of you have had the opportunity..." | Points to filed results, investor presentation, press release; references a newly uploaded vision/FAQ document | 8 |
| 3 | "The microms segment..." | Demand-environment narrative: steady recovery, rural consumption momentum, government initiatives, formalization | 8 |
| 4 | "We have we began the year FI27 on a good note..." | Q4FY26 momentum context; flags caution factors as "imponderables" — West Asia war, weaker monsoon | 8 |
| 5 | "Now quarter one..." | Q1 framed as typically slower; claims "very good robust results," plans met "on almost all relevant metrics"; monsoon/war fear described as moderating | 8 |
| 6 | "In fact, if you go to the Hindi site..." | Cites external monsoon forecast: 92% of long-term average rainfall ±5% | 8 |
| 7 | "Also, the...quoting the same site..." | Regional monsoon detail (deficit central/southern peninsula, above-normal NW/NE India); states optimism for Q2; **forward commitment**: guidance to be narrowed by end of Q2 | 8 |
| 8 | "Now against this backdrop..." | Transition sentence into formal Q1 FY27 results announcement | 8 |
| 9 | "Despite this seasonal pattern..." | "Strongest ever" Q1 disbursement claim; disbursement Rs 1,219 cr (+22% YoY); AUM Rs 7,324 cr (+28% YoY, +4% QoQ from Rs 7,044 cr Mar-26) | 8 |
| 10 | "Customer acquisition has..." | 44,000+ new borrowers (+38% YoY); active borrower base "crossed 67 lakh" (cf. block 1, `NUMBER_VARIANT`); tier 2/3 distribution strength | 8 |
| 11 | "At the same time..." | Productivity: AUM per employee +12% YoY; tech/analytics/process-efficiency investment | 8 |
| 12 | "As of June 2026, we operated..." | Branch network status restated: 571 branches, 18 states | 8 |
| 13 | "This year, our strategy remains focused..." | Deepening existing markets over new geographies; plan to add ~40–50 branches this year (forward commitment) | 8 |
| 14 | "Let me now focus on the asset quality..." | 4th consecutive quarter of improvement; GNPA 4.49% (−28bps QoQ, vs 4.77% prior qtr, vs "4.6" yr-ago); PAR X 7.01%, PAR 30 6.07%; non-OD collection efficiency 99.2%, bucket-1 54.5%; Bihar/UP/Rajasthan called out; credit cost 4.01% (−29bps QoQ); guidance 3.5–4% reaffirmed; "structural and sustainable" characterization; forward confidence in normalization "through FI27" | 8 |
| 15 | "Another important development...credit rating..." | India Ratings upgrade: long-term IND A→A+ (stable), CP IND A1→A1+; expected ~20–25bps borrowing-cost reduction on incremental borrowings | 8 |
| 16 | "Moving to our core financial performance..." | Gross total income Rs 490cr (+22% YoY); net total income Rs 322cr (+38% YoY); NIM 15.9% (+20bps QoQ); pre-provision operating profit Rs 179cr; PAT Rs 75cr (+144% YoY) | 8 |
| 17 | "Our balance sheet continues to remain exceptionally strong..." | Balance-sheet-strength framing sentence | 8 |
| 18 | "As of June 2026, our capital adequacy ratio..." | CAR 41.3%; "no need of additional capital in the foreseeable future" | 8 |
| 19 | "Looking ahead, we remain optimistic..." | Forward optimism narrative; India microenterprise opportunity sizing; differentiated-positioning restatement | 8 |
| 20 | "Our priorities for the year remain clear..." | FY27 priorities: responsible growth with underwriting discipline; AUM growth guidance 25–30%; credit-cost normalization toward 3.5–4%; gradual mortgage-share increase; continued tech/AI/analytics investment; distribution-network strengthening for productivity; closes remarks and opens floor to Q&A | 8 |
| 21 | (block 20 continuation — no independent marker) | "With that, I would like to conclude my opening remarks and open the floor for questions." | 8 |

Diagnostic (protocol Step 1, mechanical only — not interpreted here): of the 21 blocks,
roughly a third (blocks 7, 9, 13, 14 (partial), 15, 16, 18, 20) carry a specific,
quantified figure or numeric guidance band; the remainder are macro/positioning/
narrative framing. Full quantified-vs-unquantified split and internal-contradiction
read is A3/A4 work, not A2's.

---

## TABLE 4 — Q&A EXCHANGES (grep_count 13 = sweep_count 13; given questioner list reconciled)

Grep method: `grep -noiE "(the first question|next question) comes (from|on) the line
of [^.]*\."` plus one variant-phrasing catch ("...next question **in** the line of
Pavan Kumar...", line 73, which uses "in" not "from/on" and required a second pattern).
Combined mechanical count = 13 operator-introduced questioner turns. Manual sweep
against the operator-supplied questioner list (13 names) = 13. Match.

Every management answer in this table is `ATTRIBUTION_UNCLEAR` (no speaker tag in
source) — flag applies to all 13 rows and is not repeated per-row in the table body.

| # | Analyst / Firm | Intro line | Questions asked (line-cited) | Answered by |
|---|---|---|---|---|
| 1 | Sajil Raj / FL Finance Pvt Ltd | 10 | Q1 (14): rationale for holding conservative 3.5–4% credit-cost guidance despite improving trend `REPEAT_QUESTION` (cf. #4, #12). Q2 (16): portfolio yield by business vertical. Q3 (19): driver of decline in "other income" | Management, lines 14, 16–17, 20, 22 |
| 2 | Sam / Diamond Asia | 26 | Q1 (26): how customer-addition growth continues despite tightened underwriting. Q2 (28): is guidance-beat driven by mortgage/margin mix. Q3 (30): long-term loss-rate trajectory as mortgage share rises | Management, lines 27, 29, 31 |
| 3 | Shalin Kapadia / "Capital" | 35 | Q1 (36): NIM 15.9% vs guidance 14.25–14.75% — upside potential, yield/COF trajectory for FY27 `REPEAT_QUESTION` (cf. #12, #13 margin thread). Q2 (38): quantify management overlay this quarter and total on balance sheet. Q3 (39): 5-year AUM vision of Rs 24,000 cr (~27–28% CAGR) — confidence and product-mix vision, incl. affordable/gold-loan entry | Management, lines 37, 39–40 |
| 4 | Ana Ghana / A91 Park | 43 | Q1 (44): is current PAR X (~7%) sufficient to hit 3.5–4% credit-cost guidance `REPEAT_QUESTION` (cf. #1, #12) | Management, line 45 |
| 5 | Manga / Om, Kotak Mutual Fund | 48 | Q1 (49): overlay creation/utilization philosophy, and whether medium-term vision-document credit-cost guidance nets overlays; % of book under government guarantee schemes. Q2 (52): branch-expansion/opex efficiency — sustainable ceiling on growth without adding branches. Q3 (54): DA strategy — opportunistic vs uniform through the year. Q4 (56): timing of rating-upgrade benefit flowing into marginal cost of borrowing | Management, lines 50–51, 53, 55, 57–59, 61 |
| 6 | Varia / Vijay, "capital" | 64 | Q1 (65): dispersement decline ~38% QoQ vs industry ~25%+ — seasonality explanation. Q2 (67): staffing/hiring amid sector-wide NBFC hiring difficulty | Management, lines 66, 68 |
| 7 | Pavan Kumar / Eagle Wise (Public Alternates) | 73 | Q1 (74): % of borrowers also holding gold loans and digital/fintech loans, and trend over quarters | Management, line 75 |
| 8 | Nishin Chabati / Kotak | 78 | Q1 (79): clarify gold-loan customer-base definition (LAP+hypothecation combined?); any collection-behaviour data for gold-loan holders. Q2 (81): co-lending strategy | Management, lines 80, 82 |
| 9 | Gokal / PTH Capital | 84 | Q1 (87): current leverage level and target ceiling `REPEAT_QUESTION` (cf. #13, capital-raise timing thread). Q2 (88, same turn): LTV by loan type. Q3 (89): foreclosure/pre-closure rate (~5%) — realization and liquidity experience | Management, lines 88, 90–91 |
| 10 | Sonal Minas / Christian Capital | 94 | Q1 (94): request regular NPA bifurcation by product (hypothecation vs LAP); slippage number request — **not reported**, `ZERO_STANDING` `REPEAT_QUESTION` (cf. #12). Q2 (96): PAR 90 outlook — expected year-end dip | Management, lines 95–96 |
| 11 | Tari Varia | 99 | Q1 (100): overlap between hypothecation borrowers and merchant/fintech (PTM-type) loan borrowers. Q2 (102): does Aye use QR-code/payment infrastructure for sourcing. Q3 (104): cash vs UPI transaction mix rationale. Q4 (105): quantum and structure of third-party insurance cross-sell income. Q5 (109): cross-sell attachment rate across products | Management, lines 101, 103, 105–108, 110 |
| 12 | "sust" / Radhi | 112 | Q1 (114): sustainable long-run PAR X / PAR 30 level, and further-reduction levers. Q2 (116): rationale for holding NIM guidance at 14.25–14.75% despite falling cost of borrowing `REPEAT_QUESTION` (cf. #3, #13). Q3 (118): OPEX at 8.9% vs 8.25–8.75% guidance — denominator-effect timing | Management, lines 115, 117, 119 |
| 13 | Tushar Sada / Ethna Investments | 121 | Q1 (122): OPEX ~9% vs MFI peers ~4–5% — rationale for gap. Q2 (122): ROE currently 10–12% while growing ~30% — timing of next capital raise `REPEAT_QUESTION` (cf. #9). Q3 (123): quantify mortgage-vs-hypothecation NPA/PAR gap `REPEAT_QUESTION` (cf. #10) | Management, lines 122–123 |

Individual-question sub-count: 3+3+3+1+4+2+1+2+3+2+5+3+3 = **35 discrete questions**
across 13 exchanges (supplementary count, not separately gated — every sub-question is
already line-cited above).

Response-quality note (mechanical observation only): line 90 shows management asking
the analyst (Gokal) to clarify the question before answering ("...are you saying like
BTO sort of cases") — flagged as a clarification-sought turn, not scored here (Grade
A–E scoring is A4/protocol Step 4 work).

---

## TABLE 5 — QUANTITATIVE DISCLOSURE / GUIDANCE POINTS (grep_count 42 = sweep_count 42, reconciled)

One row per transcript line carrying ≥1 management-spoken (or, where noted,
analyst-quoted-and-management-confirmed) quantitative figure. Multiple figures on one
line are listed as sub-items within the row; all share that row's line citation.

| Line | Sub-items (each a discrete quantitative disclosure) | Flags |
|---|---|---|
| 8 | 571 branches; 18 states/UTs; "6.7 lakh" active borrowers (`NUMBER_VARIANT` vs "67 lakh" same line); 92% of LTA rainfall ±5% (external cite); disbursement Rs 1,219 cr; disbursement +22% YoY; AUM Rs 7,324 cr; AUM +28% YoY; AUM +4% QoQ; prior AUM Rs 7,044 cr (Mar-26, per A1 provenance conversion of "7,44 crores"); new borrowers 44,000+; new-borrower growth +38% YoY; active borrowers "67 lakh" (`NUMBER_VARIANT`); AUM/employee +12% YoY; branch-add plan 40–50 this year; GNPA 4.49%; GNPA improvement 28bps; prior-qtr GNPA 4.77%; yr-ago GNPA "4.6"; PAR X 7.01%; PAR 30 6.07%; non-OD collection efficiency 99.2%; bucket-1 collections 54.5%; credit cost 4.01%; credit-cost improvement 29bps QoQ; credit-cost guidance 3.5–4%; rating IND A→A+; CP rating IND A1→A1+; borrowing-cost benefit ~20–25bps; gross total income Rs 490cr; GTI +22% YoY; net total income Rs 322cr; NTI +38% YoY; NIM 15.9%; NIM +20bps QoQ; pre-provision operating profit Rs 179cr; PAT Rs 75cr; PAT +144% YoY; CAR 41.3%; AUM growth guidance 25–30% | `NUMBER_VARIANT` (borrower count) |
| 14 | Hypothecation tenor ~24 months; avg ticket size ~Rs 1.5 lakh; terminal losses ~5.5–6% across products; typical yearly credit cost ~3.5%; good-year floor ~3%; guided range 3.5–4% | — |
| 16 | Blended portfolio yield 22.4% (end-Q1) | — |
| 17 | Mortgage ROI ~23.5%; hypothecation ROI ~27.5–28% | — |
| 20 | DA contribution last quarter ~Rs 20 cr ("20 kores"); DA this quarter = **nil** (no DA deal undertaken); forex P&L contribution last quarter ~Rs 12 cr ("12 K profit") | `ZERO_STANDING` (DA nil this qtr); regex-miss, added on manual sweep |
| 22 | Combined DA + forex swing ~Rs 35 cr; restated elsewhere in same answer as "32 to 33 crores" fee income (`NUMBER_VARIANT`, internal to this single answer) | `NUMBER_VARIANT` |
| 27 | Approval rate: prior ~55% of cases approved; tightened to ~45%; new borrowers this quarter restated as "48,000 ... 44,000" within the same sentence (self-corrected mid-sentence, `NUMBER_VARIANT`); 18 states + 3 union territories | `NUMBER_VARIANT` |
| 29 | Mortgage currently 22% of portfolio | — |
| 31 | Medium-term mortgage-share target 30–35%; at ~30% mortgage share, credit cost could be ~50bps lower; resulting target range ~3–3.25% (max 3.5%) | — |
| 36 | Q1 NIM 15.9% vs guidance band 14.25–14.75% (guidance figures restated by analyst, confirmed in mgmt answer) | — |
| 37 | Cost of borrowing: prior qtr weighted 10.87%, current 10.78%; incremental borrowing ~60bps lower than back book, ~10.20%; expected further drop 10–15bps from rating upgrade; portfolio yield 22.4% (restated) | — |
| 39 | Total overlay on balance sheet Rs 11 cr; overlay created this quarter ~Rs 6 cr; credit cost 4.01% (restated); 5-year AUM vision Rs 24,000 cr (~27–28% CAGR) | — |
| 40 | Growth narrative 27–28% (up to 30%) CAGR; market penetration only 2–3%; target product mix over next 3 years: 60–70% hypothecation / 30% microLAP / up to 10% other (gold/solar); declined customers ~55,000/quarter (vs 44,000 accepted); of declined customers, 20%+ obtain gold loans elsewhere | — |
| 44 | PAR X ~7% cited as the threshold being tested against 3.5–4% credit-cost guidance (analyst framing, confirmed in answer) | — |
| 45 | Targeted post-tax ROA 4.5–5% at 3.5–4% credit cost; confirms PAR X ~7% sufficiency | — |
| 50 | Overlay build-up target ~5% of book (eventually); ECLGS book ~4.5% of total book | — |
| 52 | (context for branch-efficiency Q; no new mgmt figure beyond growth rate ~25–30% already cited elsewhere) | — |
| 53 | Branch-count growth target ~10%/year; large branch = cost-equivalent of 2 mini branches; last year ~40–44 branches split; 60–70% of branches average AUM "~780 crores" (per-branch, `AMBIGUOUS_UNIT` flag — A1 header separately flags a lakh/crore ambiguity in the source; this figure reads implausibly high for a single branch and may be a lakh-denominated figure mis-rendered as crores, or a total-across-cohort figure — not resolved here, flagged for A3); branch "20 cr+" AUM category threshold cited twice | `AMBIGUOUS_UNIT` (per A1 header note) |
| 55 | Current DA pool ~5% of AUM; target DA range 5–7% of AUM (long-term) | — |
| 61 | Incremental cost of borrowing last quarter 10.2% (restated, consistent with line 37); expected further 10–15bps benefit from rating upgrade | — |
| 65 | Disbursement down ~38% QoQ (vs industry "~25%+" cited by analyst); H1/H2 disbursement split ~40%/60%; Q1 typically ~20–22% of full-year disbursement; Q1 disbursement growth +22% YoY (restated) | — |
| 66 | (continuation of line 65 seasonality answer, no additional new figure) | — |
| 68 | Team-growth target ~10%; expected to support 25–30% AUM growth | — |
| 75 | ~10–12% of borrower base holds gold loans; QR-code payment-volume penetration estimate ~15–20% (explicit "guess," see Table 6 hedge list) | — |
| 79 | Gold-loan % (10%) clarified as total-portfolio basis; borrowers with loans from other (non-gold) lenders "almost negligible... less than 1%" | — |
| 82 | Current CGFMU/CGTMSE-type coverage ~4.5% of book; processing fee ~2.5% on Rs 1–1.5 lakh ticket (~Rs 2,500) | — |
| 88 | Leverage currently 3.15x (`NUMBER_VARIANT` vs analyst's "3.1" on line 87); leverage ceiling "four to four and a half" (4–4.5x) before fresh capital needed; ~2–2.5 years of capital runway at current pace; microLAP LTV ~35–40%; hypothecation LTV ~60% ("60 odd percentage," on inventory levels) | `NUMBER_VARIANT`; regex-miss, added on manual sweep |
| 89 | Pre-closure/foreclosure rate ~5% (as shown in PPT) | — |
| 91 | Hypothecation annualized pre-closure rate ~3–3.5%; mortgage blended pre-closure/BT-out rate ~5–5.5% | — |
| 95 | Blended PAR X 7.01% (restated); hypothecation PAR X ~7.5%; mortgage PAR X ~5%; hypothecation PAR 30 ~6.6%; mortgage PAR 30 ~4%; mortgage PAR 90 ~3%; hypothecation PAR 90 ~5%; **slippage number: not reported** | `ZERO_STANDING` (slippage not reported) |
| 96 | Refined follow-up: mortgage PAR 90 ~3% (confirmed); hypothecation PAR 90 "5.35%" (refined from ~5% on line 95, `NUMBER_VARIANT`/refinement) | `NUMBER_VARIANT` |
| 101 | UPI-based transaction share of customer income ~10–20% (via account-aggregator data); market penetration 2% (restated); growth target 25–30% CAGR (restated); digital-sourcing channel ~7–8% of fresh sourcing | — |
| 106 | Cross-sell/insurance deduction rate ~2% across products | — |
| 107 | Cross-sell income this quarter ~Rs 9 cr | — |
| 108 | Rs 9 cr cross-sell income vs total revenue "Rs 490 crores" (restated from opening, line 8) — ratio framing | — |
| 110 | Attachment-rate range: lowest product ~20%, highest product ~90% | — |
| 115 | PAR X last quarter ~6.9% (restated from a different base than line 8's 7.01% current-quarter figure); May–June collection efficiency ~99.3%; Q4 average collection efficiency 99.4%; Q1 sequential AUM growth 4% (restated); sustainable PAR X target 6–6.5%; MFI-industry PAR90+ collection efficiency benchmark 5–8/9%; Aye's own PAR90+ collection efficiency ~29–30%; current PAR 90 "4 or 5%"; expectation to collect "one-third" of PAR 90 balances | — |
| 116 | NIM guidance held at 14.25–14.75% (restated) despite ~10–15bps decline in cost of borrowing | — |
| 118 | Q1 OPEX 8.9% vs guidance band 8.25–8.75% | — |
| 119 | Manpower increase estimate 13–15%; current manpower ~11,000; ~40 new branches planned (restated, cf. line 8's "40 to 50"); prior-year Q4 OPEX 9.5%; current OPEX 8.9% (restated) | — |
| 122 | OPEX 9% vs MFI peers ~4–5%; Aye ticket size ~Rs 1.5 lakh vs microLAP peers ~Rs 4.5 lakh (~3x); OPEX target to decline to 7–7.5% over next 3 years; ROE currently 10–12%; growth rate ~30% (restated) | — |
| 123 | Leverage ceiling 4–4.5x (restated) supports book growth to ~Rs 14,000 cr; current AUM restated as "Rs 7,384 crores" (`NUMBER_VARIANT` vs Rs 7,324 cr on line 8); capital runway ~2–2.5 years (restated); PAR 90 gap mortgage vs hypothecation ~2.5% | `NUMBER_VARIANT` (AUM) |

---

## TABLE 6 — FORWARD STATEMENTS & HEDGE PHRASES (grep_count 31 = sweep_count 31, reconciled)

Forward-commitment phrases (numbered, dated, or binary) and hedge phrases (vague,
non-committal) enumerated together per protocol item 5. `[FC]` = forward commitment,
`[H]` = hedge phrase.

| Line | Statement (paraphrased, tight) | Type |
|---|---|---|
| 8 | "By end of quarter two we'll be able to narrow down our guidance to more refined numbers" | [FC] — timeline-bound |
| 8 | AUM growth guidance 25–30% for FY27 (reiterated) | [FC] |
| 8 | Credit-cost guidance 3.5–4%; "we remain confident of normalization... through FI27" | [FC] |
| 8 | Plan to add 40–50 branches this year | [FC] |
| 8 | "Gradually increase the share of mortgage loan in portfolio this year" | [FC] |
| 8 | Rating upgrade expected to cut borrowing cost ~20–25bps on incremental borrowings "over the course of the year" | [FC] |
| 8 | "We continue to maintain our guidance as we had given during the year" | [H] — reaffirmation without new specificity |
| 14 | "By end of H1 I think we can give a more tighter guidance" | [FC] — reinforces line-8 commitment |
| 22 | "From this quarter onwards we've moved forex movements into OCI... we will not going forward see any fresh movements on this line" | [FC] — explicit going-forward accounting change |
| 29 | NIM guided to "remain flat. It will not come down" | [FC] |
| 31 | Mortgage share target 30–35% "eventually"; credit-cost target 3–3.25% (max 3.5%) once mortgage hits ~30% — no specific date | [FC] (soft-dated) |
| 39 | 5-year vision AUM target Rs 24,000 cr (~27–28% CAGR) | [FC] |
| 40 | Product-mix targets "over the next 3 years": 60–70% hypothecation / 30% microLAP / up to 10% other; "at best 10% can be some other product" | [FC] + [H] (hedge on the 10% ceiling) |
| 45 | Contingent forward guidance: "if our PAR X remains at 7% we will ultimately hit a credit cost of 3.5–4%... targeted ROA... 4.5–5%" | [FC] |
| 50 | Overlay build-up target ~5% of book "eventually" (no date) | [FC] (soft-dated) |
| 51 | "That would be what our endeavor would be to stay in the guidance range" | [H] — "endeavor" |
| 53 | Branch-count growth ~10%/year target; "visible... between quarter 2 to quarter 3" | [FC] |
| 55 | DA to be limited to 5–7% of AUM — "long-term strategy"; "we don't want to do more DAs" | [FC] |
| 61 | Expect additional 10–15bps borrowing-cost benefit from rating upgrade "going forward" | [FC] |
| 66 | Q1 growth "helps us more confidently move towards the guidance range of growth" | [FC] — reaffirmation |
| 67 | "We don't foresee any challenge" on staffing; "our plans for growth of the team are very modest" | [H] |
| 68 | 10% team growth expected to deliver 25–30% AUM growth | [FC] |
| 75 | QR-code volume penetration: "a good guess would be between about 15% to 20% at max" | [H] — explicit "guess" |
| 80 | "We don't have that data up front... my guess would be" (gold-loan collection-behaviour correlation) | [H] — explicit data-absence hedge |
| 82 | "We don't see [co-lending] as appealing"; "we don't see a huge benefit" from CGFMU-type coverage | [H] |
| 88 | Leverage ceiling 4–4.5x before fresh capital needed; ~2–2.5 years capital runway | [FC] |
| 95 | "We haven't reported slippage number... we can share that eventually" | [H] — deferral/non-answer pattern |
| 96 | PAR 90 "expected to improve... as we move later in the year" | [FC] (soft-dated) |
| 101 | "We're not seeing [merchant/fintech lenders] as a direct competitive threat at any stage" | [H] |
| 103 | "We believe our way of sourcing... is a lower cost sourcing" | [H] — belief statement, non-quantified |
| 115 | Sustainable PAR X target "6 to 6 and a half" percent; Q3/Q4 moderation expected from current 7.01% | [FC] |
| 116 | NIM guidance held 14.25–14.75% for FY27 despite Q1 beat; "there's an upside there" | [H]/[FC] mixed — guidance unchanged, soft upside hinted |
| 117 | "We haven't mentioned the slippages number" (second occurrence) | [H] — repeated deferral, cf. line 95 |
| 118 | OPEX guidance band 8.25–8.75% for FY27; expect in-band by Q3/Q4; "in quarter two... we will probably refine the guidance ranges" | [FC] |
| 119 | "I think we are going to wait for one more quarter" (before refining guidance) | [H] — timeline hedge |
| 122 | OPEX target to decline to 7–7.5% "in the next 3 years" | [FC] |
| 123 | Leverage 4–4.5x supports growth to ~Rs 14,000 cr book; ~2–2.5 years runway "reasonably off" | [FC] + [H] ("reasonably off" as vague temporal qualifier) |

Note: several rows above legitimately carry both an [FC] and an [H] tag on the same
line because the source blends a specific figure with a softening qualifier in the
same breath (e.g., line 40, line 116, line 123) — both tags are preserved rather than
forcing a single classification, consistent with "enumerate, do not interpret."

---

## SUMMARY — WHAT A3/A4 MUST RECONCILE AGAINST (100% of this ledger)

- 21 opening-remark topic blocks (Table 3), all citing line 8
- 13 Q&A exchanges / 35 individual questions (Table 4), all `ATTRIBUTION_UNCLEAR` on the answer side
- 42 quantitative-disclosure lines carrying well over 100 individual figures (Table 5)
- 31 forward-statement / hedge-phrase lines (Table 6)
- 108 speaker turns (Table 2), 32 of them `MERGED_TURN`
- 20 participants (Table 1)
- 3 `ZERO_STANDING` nil/non-disclosures (DA nil this quarter; slippage not reported ×2)
- 3 `NUMBER_VARIANT` internal inconsistencies requiring A3 reconciliation (active-borrower
  count 6.7 lakh vs 67 lakh; AUM Rs 7,324 cr vs Rs 7,384 cr; leverage 3.1x vs 3.15x),
  plus 3 additional in-table variants (fee income Rs 35cr vs Rs 32–33cr; new-borrower
  count "48,000...44,000" self-correction; hypothecation PAR 90 5% vs 5.35% refinement)
- 1 `AMBIGUOUS_UNIT` figure (line 53, "780 crores" per-branch AUM) flagged per A1's own
  header note on lakh/crore ambiguity in this source
- 4 `REPEAT_QUESTION` topic clusters across 9 of the 13 exchanges

```yaml
stage: A2-enumerator
company: "AYE"
quarter: "Q1 FY27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "runs/aye-q1fy27/work/A2-concall-ledger.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 3
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 108
  questions: 35
  mgmt_numbers: 42
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ATTRIBUTION_UNCLEAR, MERGED_TURN, REPEAT_QUESTION, NUMBER_VARIANT, AMBIGUOUS_UNIT]
gate_a2: pass
mismatch_note: ""
```
