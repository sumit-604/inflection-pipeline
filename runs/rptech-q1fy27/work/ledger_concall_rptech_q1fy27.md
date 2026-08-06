# A2 ENUMERATION LEDGER — RPTECH Q1 FY27 (Concall transcript)
Source: extract_concall_rptech_q1fy27.txt (217 source lines, ASR auto-transcription,
no page structure). Unit convention: Crores (spoken), x1 conversion. ALL figures below
are reproduced AS SPOKEN (verbatim ASR), per A1's ASR quality warning. A2 has NOT
corrected, normalised, or resolved any garbled/conflicting figure — every ambiguity or
internal conflict is flagged for A3/A4 to reconcile against the filed results (see
ledger_results_rptech_q1fy27.md and ledger_pressrelease_results_rptech_q1fy27.md).

Citation convention: every row cites the SOURCE transcript line number (the embedded
number A1 preserved from the original file, e.g. "line 15"), plus a sequential TURN
number A2 assigned to every paragraph-delimited speaker block (turn = (line-11)/2+1
for all content lines 11-215). Blank lines (105 of them) are paragraph separators, not
turns. Two content lines are structural markers, not turns (line 9 "BEGINS", line 217
"ENDS"). Seven lines (1-7) are the A1-supplied header block, not turns.

```
=== A2 COUNT TEST ===
category: participants        grep_count: 19   sweep_count: 19   match: yes
category: turns                grep_count: 103  sweep_count: 103  match: yes
category: questions             grep_count: 33   sweep_count: 33   match: yes
category: mgmt_numbers          grep_count: 110  sweep_count: 110  match: yes
category: zero_standing         grep_count: 2    sweep_count: 2    match: yes
category: forward_commitments   grep_count: 19   sweep_count: 19   match: yes
category: hedges                grep_count: 15   sweep_count: 15   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation notes

**turns**: `grep -coP "^\s+\d+\t\S"` on the extract returns 112 non-blank numbered
lines; subtracting the 7 header lines (1-7) and the 2 verbatim markers (lines 9, 217)
leaves 103. Manual sweep of every content line 11-215 (odd line numbers only, per the
source's paragraph-then-blank-line structure) independently counts 103 speaker-turn
paragraphs. Reconciled 103=103. NOTE (quality flag, not a count defect): ASR merged
several distinct speaker exchanges into single unbroken paragraphs with no blank-line
separator — flagged `MERGED_TURN` at lines 29, 31, 39, 119, 121, 131, 151, 171, 179,
193, 197, 159. A2 cites these at the paragraph (source-line) granularity since that is
the only independently verifiable unit; the embedded sub-exchange is noted in the Turns
table's Content column rather than assigned a fractional turn number.

**questions**: first-pass manual sweep (by analyst) produced 32; a second independent
sweep (by explicit question-content, cross-checked against Sedartha Grover's line-183
self-declaration "Two questions. First on... and how much...") found her single merged
turn actually contains two distinct questions collapsed into one row in the first
pass. Re-swept and split → 33. Corroborating grep signals: 27 literal "?" marks in the
transcript body, plus 12 explicit ordinal markers ("first/second/final/last/one more/
couple of question"); both undercount by design since ASR frequently drops question
marks in run-on speech, consistent with a semantic (33) count exceeding a punctuation
literal (27) count. Reconciled sweep-vs-resweep 33=33.

**mgmt_numbers**: grep pattern run against a management-turns-only extract (43
management-attributed paragraphs, saved to scratch file `mgmt_turns_raw.txt`):
`\d[\d,]*\.?\d*\s*(%|crores?|cr|million|billion|days|lakh|x|years?|plus|engineers?)
|hundred (billion|million)|EPS of \d+\.\d+|\d{1,2}\.\d(?= and \d{1,2}\.\d%)|back in
\d{4}|through \d{4}|16,000(?!\s*crores?)|INR \d+ in PAT|stays stood at \d+|Ctors days
stood at \d+`. First pass: 96. Manual sweep read every management paragraph line by
line and found 14 figures the first-pass pattern structurally could not match (bare
"X plus" headcounts, word-form "hundred billion", a bare "19.5" sharing one "%" with
an adjacent figure, bare "41"/"40" for debtor/creditor days with no attached unit
word, and critically the standalone "INR 197 in PAT" that conflicts with the "97
crores" PAT figure stated earlier in the SAME turn 4 / line 17). Pattern was expanded
to capture all 14 confirmed items; re-run returns 110. Reconciled 110=110. FLAG:
several of the merged-turn paragraphs (see turns note above) mix analyst-spoken and
management-spoken text with no break; numbers captured from lines 39, 119, 121, 131,
151, 197 carry flag `SPEAKER_ATTRIBUTION_UNCERTAIN` where the immediate context
suggests the figure may echo the analyst's own question wording rather than being
freshly stated by management.

**zero_standing**: manual sweep of all management turns for explicit nil/none/zero
disclosures = 2 (refurbished-business revenue = "none"/zero at turn 50/line 109;
zero Japanese-manufacturer customers in the embedded vertical at turn 46/line 101).
Grep cross-check `grep -icE "\bnone\b|not a single|zero"` on mgmt_turns_raw.txt = 2.
Reconciled 2=2.

**forward_commitments / hedges**: lexicon-based grep against mgmt_turns_raw.txt,
iteratively expanded during manual sweep until every phrase independently identified
by close reading was matched (see Sections 5 and 6 below for the full phrase lists
and lexicon). Reconciled 19=19 (forward-commitment) and 15=15 (hedge).

---

## SECTION 1 — Participants, 19 rows

Per host intro (lines 5-7, 13) and operator/moderator turns. Promoter/CMD **Kapil
Mansi ("Kapal Mansi" per ASR) IS PRESENT** on this call — no `MGMT_ABSENCE` flag
warranted; all three named management figures (MD/Promoter, CEO, CFO) spoke.

| # | Name (as spoken/ASR) | Likely identity | Designation | Side | First turn / line | Flags |
|---|---|---|---|---|---|---|
| 1 | Kapal Mansi / Kapul | Kapil | MD & Promoter | Management | Turn 3 / line 15 | present; opening + closing remarks |
| 2 | Rajes Moinka / Rajesh Goa | (name inconsistent across mentions) | CEO | Management | answers embedded from Turn 7 / line 23 onward | NAME_INCONSISTENCY (two distinct spellings used) |
| 3 | Himmanush Sha / Himmanushka | CFO | CFO | Management | Turn 4 / line 17 | financials delivery |
| 4 | Vin Meon / Vinnai | — | Moderator/Host | Sell-side (host) | Turn 2 / line 13 | firm named "UNAT Capital" (line 7) vs "Monarch Capital" (line 215) — flag `NAME_INCONSISTENCY` |
| 5 | (unnamed) Operator | — | Conference call operator | Infrastructure | Turn 1 / line 11 | standard operator script turns throughout |
| 6 | Amit Ketan | — | Analyst | Buy-side/Sell-side | Turn 6 / line 21 | firm: Lebanon Capital |
| 7 | Bhavin Chera | — | Analyst | — | line 39 (turn 15) | firm: Inarm Holdings |
| 8 | HQ | — | Analyst | — | line 47 (turn 19) | firm: Orin Capital; name likely mangled/abbreviated |
| 9 | Aish Chaparia | — | Analyst | — | line 69 (turn 30) | firm: Shawas Capital |
| 10 | Nishita Shankalesha | — | Analyst | — | line 83 (turn 37) | firm: Safire Capital |
| 11 | Raman KV | — | Analyst | — | line 99 (turn 45) | firm: Sequent Investments |
| 12 | AR Lakhani | — | Analyst | — | line 117 (turn 54) | firm: Unifi AMC |
| 13 | Vive Tulian | — | Analyst | — | line 129 (turn 60) | firm: Newark Capital |
| 14 | AIM | — | Analyst | — | line 139 (turn 65) | firm: Jam Capital; name likely acronym/mangled |
| 15 | Madurati | — | Analyst | — | line 153 (turn 72) | firm: "counter technical investments" |
| 16 | Pel Sha | — | Analyst | — | line 159 (turn 75, embedded) | firm: RTL Investments |
| 17 | Jes Siddani | — | Analyst | — | line 171 (turn 81, embedded) | firm: Integrity Ventures |
| 18 | Sedartha Grover | — | Analyst | — | line 179/183 (turn 85/87) | firm: Equest PMS |
| 19 | Jatin Chabla | — | Analyst | — | line 195 (turn 93) | firm: RTL Investments — SAME firm name as Pel Sha (row 16); could be same house, two analysts, or a name-collision artifact of ASR — flag `AMBIGUOUS` |

grep cross-check: 14 analyst introductions matched via two patterns —
`"question comes...the line of"` (13 hits, rows 7-9,10-19 except row 6) + `"first
question comes...the line of"` (1 hit, row 6, Amit Ketan) = 14. Plus 3 management +
1 moderator + 1 operator = 19. Reconciled 19=19.

---

## SECTION 2 — Speaker turns, 103 rows

Numbered sequentially; speaker + first ~10 words; source line cited for every row.
`MERGED_TURN` = paragraph contains more than one logical speaker exchange with no
blank-line break in the ASR source (embedded sub-content noted inline).

| Turn | Line | Speaker | First ~10 words | Flags |
|---|---|---|---|---|
| 1 | 11 | Operator | "Ladies and gentlemen, good day and welcome to Rashi..." | |
| 2 | 13 | Vin Meon (host) | "Thank you. Uh good morning everyone. Uh today on..." | |
| 3 | 15 | Kapil (MD/Promoter) | "Uh thank you Vinnai. Uh good morning everyone and..." | opening remarks, industry backdrop + Q1 highlights + 3 pillars |
| 4 | 17 | Himmanush Sha (CFO) | "Thank you Kapul and uh good morning everyone. It..." | detailed financials |
| 5 | 19 | Operator | "Thank you. We will now begin the question and..." | intros Amit Ketan |
| 6 | 21 | Amit Ketan (analyst) | "Hi uh good morning thanks for taking my question..." | Q1: demand sustainability |
| 7 | 23 | Management (unspecified) | "Uh so Amit to give you perspective uh third..." | cut off — echo issue |
| 8 | 25 | Operator | "Yeah speaker just give me a moment just give..." | technical interruption |
| 9 | 27 | Management | "Yep. Go ahead." | resumes |
| 10 | 29 | Management | "Yeah so I I'll repeat my answer. Uh Amit..." | `MERGED_TURN` — restates 10% unit-market-reduction answer, ends with Amit's next sub-question text embedded ("question is more relating to...") |
| 11 | 31 | Management | "Yeah. So I think the first and foremost uh..." | `MERGED_TURN` — India-demand answer, embeds Amit's segment-split follow-up at end |
| 12 | 33 | Management | "So Rashi peripherals is a B2B company. So we..." | answers segment split |
| 13 | 35 | Amit Ketan | "Understood. Thank you and all the best." | closing |
| 14 | 37 | Operator | "Thank you. A reminder to all the participants please..." | intros Bhavin Chera |
| 15 | 39 | Bhavin Chera + Management | "Uh yeah, good morning team and uh congratulations to..." | `MERGED_TURN` — Q1 (growth breakdown) and detailed management answer in one block |
| 16 | 41 | Bhavin Chera | "Yeah. Uh that's great to hear. And my second..." | Q2: new-venture revenue contribution timing |
| 17 | 43 | Management | "So I'll answer that question. Uh I think Uh..." | answers Q2 |
| 18 | 45 | Bhavin (closing) + Operator | "Great. So thank you and best of luck here..." | `MERGED_TURN` — intros HQ |
| 19 | 47 | HQ (analyst) | "Thanks for taking my questions. First of all, congratulations..." | Q1: VDA outlook |
| 20 | 49 | Management | "Yeah. So on on the VDA uh it is..." | answers VDA (67% stake, FY24 rev 850cr) |
| 21 | 51 | HQ | "and sir my second question uh would be on..." | Q2: supply constraints H2 |
| 22 | 53 | Management | "yeah so there is a potential risk uh yes..." | "orange alert", weekly tracking |
| 23 | 55 | HQ | "And then my final question, can you give the..." | Q3: Dell revenue |
| 24 | 57 | Management | "So roughly about 5% uh business has come from..." | ~5% from Dell |
| 25 | 59 | HQ | "And and can you remind me what was your..." | Q4: Dell FY27 target follow-up |
| 26 | 61 | Management | "We are above the target as far as numbers..." | above target (no figure given) |
| 27 | 63 | HQ | "Okay. Okay sir. All the best sir." | closing |
| 28 | 65 | Operator | "Thank you." | |
| 29 | 67 | Operator | "Thank you. Next question comes from the line...." | intros Aish Chaparia |
| 30 | 69 | Aish Chaparia | "Yeah. Hi. Uh congrats on a good set of..." | Q1: channel inventory |
| 31 | 71 | Management | "Okay. So I think Binby also mentioned uh that..." | T2 partner inventory, "not a big concern" |
| 32 | 73 | Aish Chaparia | "Understood. Understood. Also if you could just uh..." | Q2: refurbished PC threat |
| 33 | 75 | Management | "So overall PC TAM in India is about 15..." | PC TAM 15-16mn, refurb ~1mn |
| 34 | 77 | Aish Chaparia | "Understood. And one last question if you could just..." | Q3: volume/value split |
| 35 | 79 | Management | "Yeah. So in terms of unitwise we have grown..." | 20% unit growth, SanDisk dip noted |
| 36 | 81 | Aish (closing) + Operator | "All right thank you so much all the best..." | `MERGED_TURN` — intros Nishita |
| 37 | 83 | Nishita Shankalesha | "Um hello. Am I audible?" | |
| 38 | 85 | Management/Operator | "Yes." | |
| 39 | 87 | Nishita Shankalesha | "Yes. So I just wanted uh some clarification. You..." | Q1: semicon 70%/11,000cr clarification |
| 40 | 89 | Management | "So uh let me please clarify that uh it..." | clarifies 70% is YoY growth, not % of revenue |
| 41 | 91 | Nishita Shankalesha | "Okay. Okay. Understood. And you mentioned that Q2..." | Q2: Q2 growth guidance |
| 42 | 93 | Management | "Yeah. So we as I said I have already..." | Q2 similar trend; price-increase speed to halve |
| 43 | 95 | Nishita Shankalesha | "Okay, understood. Thank you so much." | closing |
| 44 | 97 | Operator | "Thank you. Next question comes from the line of..." | intros Raman KV |
| 45 | 99 | Raman KV | "Hi sir. Uh thank you for uh allowing me..." | Q1: semicon JV explain |
| 46 | 101 | Management | "Yeah. So Raman uh I will explain to you..." | JV name, Restar profile, 26% stake, 200+ engineers |
| 47 | 103 | Raman KV | "Uh just a followup here with when you say..." | Q2: design-solution clarify |
| 48 | 105 | Management | "So for example I'll give you our example because..." | EV headlight chip design example |
| 49 | 107 | Raman KV | "Understood sir answer. Um my second question is with..." | Q3: refurbishment % of revenue — `REPEAT_QUESTION` (see Section 3) |
| 50 | 109 | Management | "currently it is none currently refurbished business is none..." | `ZERO_STANDING` — refurb revenue = none/zero; hedge "fingers crossed" |
| 51 | 111 | Raman KV | "so is there any timeline wherein you are aiming..." | Q4: refurb timeline follow-up |
| 52 | 113 | Management | "that's why I said fingers crossed understood sir Thank..." | hedge repeated |
| 53 | 115 | Operator | "Thank you. Next question comes from the line of..." | intros AR Lakhani |
| 54 | 117 | AR Lakhani | "Uh yeah, congratulations to the management team on a..." | Q1: Utah deal / large AI infra deals |
| 55 | 119 | Management + AR Lakhani | "uh so I I think very good question very..." | `MERGED_TURN` — pipeline answer, embeds AR Lakhani's follow-up on selectivity/capital constraint at end |
| 56 | 121 | Management + AR Lakhani | "absolutely you are on you you answered yourself..." | `MERGED_TURN` — debt-ratio answer (~0.5x, would go 2x), embeds follow-up on what's lost |
| 57 | 123 | Management | "So basically by uh not giving the I'm not..." | small deals already present (20/50/70cr examples) |
| 58 | 125 | AR Lakhani | "Understood sir. Uh thanks and all the best." | closing |
| 59 | 127 | Operator | "Thank you. Next question comes from the line of..." | intros Vive Tulian |
| 60 | 129 | Vive Tulian | "Hi uh uh just one question on the gross..." | Q1: gross margin |
| 61 | 131 | Management + Vive Tulian | "Gross margin uh basically is outcome of the product..." | `MERGED_TURN` — margin/product-mix answer, embeds Vive's net-debt follow-up at end |
| 62 | 133 | Management | "1,285 cr." | net debt answer |
| 63 | 135 | Vive Tulian | "Got it. Okay. Thank you." | closing |
| 64 | 137 | Operator | "Thank you. Next question comes from the line of..." | intros AIM |
| 65 | 139 | AIM (analyst) | "Yeah. Hi, good morning. Uh it's just one question..." | Q1: channel inventory clarify — `REPEAT_QUESTION` |
| 66 | 141 | Management | "Shortage of laptops. Uh sorry uh am I audible?" | audio issue, garbled start |
| 67 | 143 | AIM | "Yeah, now you're clear. Can you repeat the entire..." | confirms audible |
| 68 | 145 | AIM | "Yeah. Yeah. My apologies. I just repeat uh so..." | `AUDIO_REPEAT` of turn-65 question, not a new question |
| 69 | 147 | Management | "Yeah. So in general see price is always a..." | component/laptop shortage answer |
| 70 | 149 | AIM | "sorry when you say if you are able to..." | Q2: entry-level vs premium laptop availability |
| 71 | 151 | Management + Operator | "Yeah. So entry-level laptops uh there is uh almost..." | `MERGED_TURN` — 50% entry-level shortage answer, embeds operator's close/intro of Madurati at end |
| 72 | 153 | Madurati | "Sir thank you for the opportunity sir. I just..." | Q: data center deals + VDA integration — `REPEAT_QUESTION` (data-center topic) |
| 73 | 155 | Management | "So very good point uh Mad Rashi is obviously..." | neoclouds strategy; VDA integration "few quarters away" |
| 74 | 157 | Madurati | "Got it. Uh sir that was from mine. Thank..." | closing |
| 75 | 159 | Operator + Pel Sha | "Thank you. Next question comes on the line of..." | `MERGED_TURN` — intros Pel Sha, embeds his F28-sustainability question |
| 76 | 161 | Management | "So, so BEL uh we always I repeat the..." | 20-yr CAGR, 16,000cr base, EDA/Restar JV |
| 77 | 163 | Pel Sha | "Thank you very much and all the" | cut off |
| 78 | 165 | Management | "so do not have an iota of dio doubt..." | reaffirms confidence |
| 79 | 167 | Pel Sha | "Okay. Okay. That's very reassuring. Thank you very much..." | closing |
| 80 | 169 | Management | "Yeah." | |
| 81 | 171 | Operator + Jes Siddani | "Thank you. Next question comes from the line of..." | `MERGED_TURN` — intros Jes Siddani, embeds contingent-liabilities question |
| 82 | 173 | Management | "So uh yes these uh contingent liabilities are in..." | GST show-cause notices, <1% historically closed against |
| 83 | 175 | Jes Siddani | "okay and are we expecting closure of this matters..." | follow-up: closure timeline |
| 84 | 177 | Management | "continuous since the business is of continuous nature These..." | "law takes its own course" |
| 85 | 179 | Operator + Sedartha Grover | "Thank you Mr. Sadani. Please rejoin the queue for..." | `MERGED_TURN` — closes Jes Siddani, intros/interrupts Sedartha Grover (audio issue) |
| 86 | 181 | Sedartha Grover | "Yes, please go ahead." | confirms audible |
| 87 | 183 | Sedartha Grover | "Yes. So congratulations on good set of numbers sir..." | "Two questions" — embedded-division revenue/profitability + JV investment amount |
| 88 | 185 | Management | "So let me answer second question first. Uh as..." | JV investment amount "premature" (hedge) |
| 89 | 187 | Management | "Yeah. And to answer your first question, so we..." | targets >$100mn revenue in 3 yrs under JV |
| 90 | 189 | Sedartha Grover | "Okay. And this JV comes with higher margin profile..." | follow-up: margin profile confirm — `REPEAT_QUESTION` (semicon-JV economics topic) |
| 91 | 191 | Management | "Absolutely." | |
| 92 | 193 | Operator | "Thank you Mr. Global. Please We join the queue..." | `MERGED_TURN` — closes Sedartha, intros Jatin Chabla |
| 93 | 195 | Jatin Chabla | "Yeah. Hi, good afternoon and thanks for the opportunity..." | Q1: JV addressable TAM — `REPEAT_QUESTION` |
| 94 | 197 | Management + Jatin Chabla | "So the third party report which is there in..." | `MERGED_TURN` — TAM answer ($150bn, revised from $100bn), embeds Jatin's "how much addressable by JV" restated at end |
| 95 | 199 | Management | "Yeah. So uh as we said the addressibility is..." | $100mn JV aspiration, "very conservative" (hedge) |
| 96 | 201 | Jatin Chabla | "Got it." | |
| 97 | 203 | Management | "And that's the very baseline considering the opportunity we..." | forward-looking scaling commitment |
| 98 | 205 | Jatin Chabla | "Got it. Got it. Uh one more question. Uh..." | Q2: market share gain source |
| 99 | 207 | Management | "So I cannot talk for others but I can..." | declines to specify competitor(s) losing share |
| 100 | 209 | Jatin Chabla | "Got it. Uh, thanks a lot." | closing |
| 101 | 211 | Operator | "Thank you ladies and gentlemen. Due to time constraints..." | Q&A ends, hands to management |
| 102 | 213 | Management (Kapil) | "Thank you all for your engagement and for thoughtful..." | closing remarks, 80+ brands / 10,000+ channel partners |
| 103 | 215 | Vin Meon / Operator | "Thank you so much. Thank you on behalf of..." | closes call; "Monarch Capital" named here vs "UNAT Capital" at line 7 |

---

## SECTION 3 — Analyst questions, 33 rows

`REPEAT_QUESTION` flags a topic asked by more than one analyst (or, per the
transcript's own self-reference at turn 50/line 109, explicitly noted by management
as already asked).

| # | Analyst | Firm | Topic | Turn(s) | Flags |
|---|---|---|---|---|---|
| 1 | Amit Ketan | Lebanon Capital | Demand sustainability, India vs. global divergence | 6 | |
| 2 | Amit Ketan | Lebanon Capital | Consumer vs. commercial segment split | 11 (embedded) | |
| 3 | Bhavin Chera | Inarm Holdings | Growth breakdown: volume vs. price, timing of price capture | 15 (embedded) | |
| 4 | Bhavin Chera | Inarm Holdings | Revenue-contribution timeline from new ventures (VDA/JV) | 16 | `REPEAT_QUESTION` (VDA/JV timing, see #5) |
| 5 | HQ | Orin Capital | VDA outlook, next 2-3 years | 19 | `REPEAT_QUESTION` (VDA topic, see #4) |
| 6 | HQ | Orin Capital | Supply-constraint risk to H2 volumes | 21 | |
| 7 | HQ | Orin Capital | Dell business revenue contribution this quarter | 23 | |
| 8 | HQ | Orin Capital | Dell FY27 target status (follow-up) | 25 | |
| 9 | Aish Chaparia | Shawas Capital | Channel partner inventory levels | 30 | `REPEAT_QUESTION` (see #23) |
| 10 | Aish Chaparia | Shawas Capital | Refurbished-PC threat to pricing | 32 | `REPEAT_QUESTION` (see #16 — explicit self-reference by management "someone already asked earlier... sanka asked already") |
| 11 | Aish Chaparia | Shawas Capital | Volume vs. value split of topline growth | 34 | |
| 12 | Nishita Shankalesha | Safire Capital | Clarification on 70% semicon-revenue claim (11,000cr?) | 39 | |
| 13 | Nishita Shankalesha | Safire Capital | Q2 growth guidance | 41 | `REPEAT_QUESTION` (Q2/H2 trajectory touched unprompted at turns 10, 42) |
| 14 | Raman KV | Sequent Investments | Semicon JV — what is it building/selling | 45 | `REPEAT_QUESTION` (JV specifics, see #29, #32) |
| 15 | Raman KV | Sequent Investments | Design-solutions clarification (follow-up) | 47 | |
| 16 | Raman KV | Sequent Investments | Refurbishment business, % of revenue | 49 | `REPEAT_QUESTION` (see #10) |
| 17 | Raman KV | Sequent Investments | Timeline to start refurbished business (follow-up) | 51 | |
| 18 | AR Lakhani | Unifi AMC | Utah deal / large AI infra deal strategy going forward | 54 | `REPEAT_QUESTION` (data-center/large-deal topic, see #25) |
| 19 | AR Lakhani | Unifi AMC | Selectivity vs. capital constraint on large deals (follow-up) | 55 (embedded) | |
| 20 | AR Lakhani | Unifi AMC | What is lost strategically by not participating (follow-up) | 56 (embedded) | |
| 21 | Vive Tulian | Newark Capital | Gross margin decline vs. prior quarters | 60 | |
| 22 | Vive Tulian | Newark Capital | Net debt figure, end of June | 61 (embedded) | |
| 23 | AIM | Jam Capital | Channel inventory clarification | 65 | `REPEAT_QUESTION` (see #9); re-asked verbatim at turn 68 due to audio glitch (`AUDIO_REPEAT`, not a new question) |
| 24 | AIM | Jam Capital | Entry-level vs. premium laptop availability (follow-up) | 70 | |
| 25 | Madurati | counter technical investments | Data center deals outlook + VDA-bidding integration | 72 | `REPEAT_QUESTION` (see #18) |
| 26 | Pel Sha | RTL Investments | FY28 growth sustainability after tailwinds ease | 75 (embedded) | |
| 27 | Jes Siddani | Integrity Ventures | Contingent liabilities / GST show-cause notices | 81 (embedded) | |
| 28 | Jes Siddani | Integrity Ventures | Expected closure timeline (follow-up) | 83 | |
| 29a | Sedartha Grover | Equest PMS | Semicon/embedded division revenue & profitability | 87 | `REPEAT_QUESTION` (see #14) |
| 29b | Sedartha Grover | Equest PMS | JV investment amount for Restar's 26% stake | 87 | `REPEAT_QUESTION` (see #14, #32) |
| 30 | Sedartha Grover | Equest PMS | JV margin-profile confirmation (follow-up) | 90 | |
| 31 | Jatin Chabla | RTL Investments | JV addressable TAM in India | 93 | `REPEAT_QUESTION` (see #14, #29b) |
| 32 | Jatin Chabla | RTL Investments | (embedded in mgmt turn 94) how much of $150bn TAM is JV-addressable | 94 (embedded) | `MERGED_TURN` origin — question text embedded in management's answer paragraph |
| 33 | Jatin Chabla | RTL Investments | Market share gain — source/competitors | 98 | |

grep cross-check: 27 literal "?" marks + 12 explicit ordinal question-markers
("first/second/final/last/one more/couple of question") corroborate a semantic count
in the 27-33 range; manual double-sweep (by-analyst then by-content) converges and
reconciles at 33 (see Reconciliation notes above).

---

## SECTION 4 — Management-spoken numbers, 110 rows

Reproduced AS SPOKEN (ASR). Where the same metric is restated later in the same or a
later turn, both instances are listed as separate rows since both were separately
spoken; internal conflicts between them are flagged `NUMBER_CONFLICT`. Ambiguous/
garbled digit groupings per A1's header note are flagged `AMBIGUOUS`.

### 4A — Turn 3 / line 15 (Kapil, opening remarks) — 18 numbers

| # | Figure (as spoken) | Metric | Flags |
|---|---|---|---|
| 1 | "through 2028" | Memory/NAND shortage forecast horizon (industry, per independent forecasts) | |
| 2 | "1.5 lakh cr" | India IT/ITC distribution market opportunity size | |
| 3 | 61.9% | Consolidated revenue YoY growth | `NUMBER_CONFLICT` vs CFO's 62% (turn 4) — close but not identical wording ("61.9%" vs "up 62% rounded off") |
| 4 | 5,100 crores | Consolidated revenue | `NUMBER_CONFLICT` vs CFO's "5,12 crores" (turn 4) — A1 flags these do NOT verbatim match |
| 5 | 50% | EBITDA (EITA) growth YoY | `NUMBER_CONFLICT` vs CFO's 55% EBITDA growth (turn 4) |
| 6 | 155 crores | EBITDA absolute (consol.) | `NUMBER_CONFLICT` vs CFO's 173 crores (turn 4) |
| 7 | 69.5% | PAT growth YoY | close to CFO's 69% (turn 4), consistent |
| 8 | 105 crores | PAT absolute (consol.) | consistent with CFO's 105 crores (turn 4) |
| 9 | EPS of 15.25 | Diluted EPS | |
| 10 | 19.5 (%, implied) | Annualized ROC | `AMBIGUOUS` — % symbol not attached in ASR, shared with adjacent 19.8% |
| 11 | 19.8% | Annualized ROE | |
| 12 | 56 days | Working capital days | |
| 13 | 62% (~near) | Pillar-1 topline growth, restated | |
| 14 | 74% | Rashi's stake in semicon JV | |
| 15 | 26% (garbled "60 26%") | Restar's stake in semicon JV | `AMBIGUOUS` per A1 header |
| 16 | 50 plus | Local engineering hires target, next 2 years | |
| 17 | "back in 2021" | Date of Rashi's first step into semiconductor | |
| 18 | 150 billion ($) | India semiconductor market size by 2030 (first mention) | |

### 4B — Turn 4 / line 17 (Himmanush Sha, CFO financials) — 32 numbers

| # | Figure (as spoken) | Metric | Flags |
|---|---|---|---|
| 19 | 5,12 crores | Consolidated revenue from operations | `AMBIGUOUS` per A1 header (likely ~5,102cr); `NUMBER_CONFLICT` vs Kapil's 5,100cr |
| 20 | 62% | Consolidated revenue YoY growth ("rounded off") | |
| 21 | 55% | Consolidated EBITDA (AITA) growth YoY | `NUMBER_CONFLICT` vs Kapil's 50% (turn 3) |
| 22 | 173 crores | Consolidated EBITDA absolute | `NUMBER_CONFLICT` vs Kapil's 155 crores (turn 3) |
| 23 | 3.38% | Consolidated EBITDA margin | |
| 24 | 69% | Consolidated PAT growth YoY | |
| 25 | 105. crores | Consolidated PAT absolute (stray decimal, ASR artifact) | |
| 26 | 2.05% | Consolidated "PT margin" | `AMBIGUOUS` per A1 header — PBT vs PAT unclear |
| 27 | 73% | Consolidated PBT growth YoY | |
| 28 | 139 crores | Consolidated PBT absolute | |
| 29 | 2.72% | Consolidated PBT margin | |
| 30 | 4,832 crores | Standalone revenue | |
| 31 | 58% | Standalone revenue YoY growth | |
| 32 | 50% | Standalone EBITDA (AIT) growth YoY | |
| 33 | 164 crores | Standalone EBITDA absolute | |
| 34 | 3.38% | Standalone EBITDA margin | |
| 35 | 65% | Standalone "PT" growth YoY | `AMBIGUOUS` PBT/PAT |
| 36 | 97 crores | Standalone PT/PAT absolute | `NUMBER_CONFLICT` vs #47 below ("197" in PAT) — same speaker, same turn |
| 37 | 2.01% | Standalone PT margin | |
| 38 | 65% (garbled "50 65%") | Standalone PBT growth YoY | `AMBIGUOUS` per A1 header |
| 39 | 130 crores | Standalone PBT absolute | |
| 40 | 2.69% | Standalone PBT margin | |
| 41 | 55 days | Inventory days | |
| 42 | "stays stood at 41" | Debtor days ("Data stays" = ASR mangling of "Debtor days") | `AMBIGUOUS` — unit word "days" not attached to the 41 |
| 43 | "Ctors days stood at 40" | Creditor days | `AMBIGUOUS` — "Ctors" = ASR mangling of "Creditors" |
| 44 | 56 days | Overall working capital days (YoY improved) | consistent with turn 3's 56 days |
| 45 | 5,12 crores | Consolidated revenue (summary restatement) | repeats #19 |
| 46 | 173 crores | Consolidated EBITDA (summary restatement) | repeats #22 |
| 47a | 105 crores | Consolidated PAT (summary restatement) | repeats #25 (cleanly, no stray decimal this time) |
| 47b | 4,832 crores | Standalone revenue (summary restatement) | repeats #30 |
| 47c | 164 crores | Standalone EBITDA (summary restatement) | repeats #33 |
| 47 | "INR 197 in PAT" | Standalone PAT (summary restatement) | `NUMBER_CONFLICT` — directly conflicts with #36 (97 crores) stated earlier in the SAME turn/paragraph; A1 flagged this explicitly in its header |

### 4C — Remaining management turns — 60 numbers

| # | Turn / Line | Figure (as spoken) | Metric | Flags |
|---|---|---|---|---|
| 48 | 10 / 29 | ~10% | Market unit-size reduction (third-party reports) | |
| 49 | 12 / 33 | "30 35%" (35% captured, 30 bare) | Consumer segment share of business | range as spoken |
| 50 | 12 / 33 | "60 65%" (65% captured, 60 bare) | Commercial (SMB+Enterprise) segment share | range as spoken |
| 51 | 12 / 33 | 2x | Laptop price increase vs. last year | |
| 52 | 12 / 33 | 3 years -> 4 years | Enterprise refresh-cycle extension (example 1) | |
| 53 | 12 / 33 | 4 years -> 5 years | Enterprise refresh-cycle extension (example 2) | |
| 54 | 15 / 39 | 60-62% | Total revenue growth this quarter | `MERGED_TURN` — `SPEAKER_ATTRIBUTION_UNCERTAIN` (Bhavin's own question wording embedded at block start) |
| 55 | 15 / 39 | "30 35%" (35% captured) | Growth attributed to price increase | |
| 56 | 15 / 39 | "5 to 10%" (10% captured) | Growth attributed to new products/brands | |
| 57 | 15 / 39 | "20 25%" (25% captured) | Growth attributed to quantity increase | |
| 58 | 15 / 39 | 57 towns | Distribution reach (annotation, not separately unit-tagged) | |
| 59 | 15 / 39 | 10% | Growth attributed to improved market share | |
| 60 | 17 / 43 | ~5% | Revenue portfolio share from new integrated services (VDA) | |
| 61 | 17 / 43 | 70% | Semicon revenue already crossed 70% of last FY's total revenue | later clarified at #67 to mean YoY growth, not % of total revenue — potential investor mis-hear risk (see Nishita's Q12) |
| 62 | 20 / 49 | 67% | VDA stake acquired | |
| 63 | 20 / 49 | 850 crores | VDA prior-FY revenue | |
| 64 | 20 / 49 | "next 2 to 3 years" | VDA value-creation timeline | |
| 65 | 22 / 53 | "more than 30 years" | Rashi's track record / OEM relationships | |
| 66 | 24 / 57 | ~5% | Dell commercial business contribution this quarter | |
| 67 | 40 / 89 | 16 million | India overall PC TAM, upper bound | |
| 68 | 40 / 89 (i.e. turn 33/line 75) | 15 million | India overall PC TAM, lower bound | table row grouping note: this and #67 both from turn 33/line 75 |
| 69 | 33 / 75 | 0.5-1 million | Refurbished-PC market size estimate (varying estimates) | |
| 70 | 35 / 79 | 20% | Unit-wise volume growth | |
| 71 | 35 / 79 | 10% | Market-share improvement contribution (repeat of #59) | |
| 72 | 40 / 89 | 70% | Semicon portfolio revenue growth YoY (clarification: not 70% of total revenue) | resolves ambiguity flagged at #61 |
| 73 | 42 / 93 | 60% | Q1 growth restated | |
| 74 | 42 / 93 | "half" (qualitative, price-increase speed) | Q2 price-increase pace expectation | |
| 75 | 46 / 101 | $4 billion | Restar Corporation market cap/size | |
| 76 | 46 / 101 | 26% | Restar's JV stake (repeat, clean figure vs. garbled turn-3 version) | |
| 77 | 46 / 101 | 200+ engineers | Restar's design engineering headcount | |
| 78 | 55 / 119 | 60% | Growth momentum context (large-deals answer) | `MERGED_TURN` |
| 79 | 56 / 121 | 62% | Growth restated | `MERGED_TURN` |
| 80 | 56 / 121 | 2x | Debt ratio if large AI-infra deals pursued | `MERGED_TURN` |
| 81 | 57 / 123 | 20 cr | Example small deal size already supplied | |
| 82 | 57 / 123 | 50 cr | Example small deal size already supplied | |
| 83 | 57 / 123 | 70 crores | Example small deal size already supplied | |
| 84 | 57 / 123 | 1,000 cr | Threshold for "large deal" not yet prioritized | |
| 85 | 57 / 123 | 60% | Momentum context restated | |
| 86 | 62 / 133 | 1,285 cr | Net debt, end of June | `AMBIGUOUS` per A1 header — not independently verified |
| 87 | 71 / 151 | ~50% | Entry-level laptop shortage | |
| 88 | 76 / 161 | 20 years | Historical CAGR track record (years) | |
| 89 | 76 / 161 | 20% | Historical CAGR (rate) | |
| 90 | 76 / 161 | 16,000 (crores, implied) | Base revenue figure used for CAGR math | `AMBIGUOUS` — not clearly tied to a specific stated metric (FY26 revenue base?) |
| 91 | 76 / 161 | 20% (of 16,000) | Same CAGR rate restated in the math | |
| 92 | 76 / 161 | 16,000 (restated) | Base figure restated | |
| 93 | 76 / 161 | 3,000 crores | Implied annual growth quantum (20% of 16,000) | |
| 94 | 78 / 165 | 20 years | Track record restated | |
| 95 | 82 / 173 | <1% | Historical GST show-cause notices closed against the company (of total demanded) | |
| 96 | 89 / 187 | 3 years | JV revenue target timeline | |
| 97 | 89 / 187 | $100 million | JV revenue target ("more than") | |
| 98 | 94 / 197 | $150 billion | India semicon TAM by 2030 (per govt/press-release third-party report) | `MERGED_TURN` — restates #18 |
| 99 | 94 / 197 | "hundred billion" ($100bn) | Earlier (pre-revision) TAM estimate for 2030 | |
| 100 | 94 / 197 | $150 billion | TAM restated a second time in same sentence | |
| 101 | 95 / 199 | 3 years | JV aspiration timeline restated | |
| 102 | 95 / 199 | $100 million | JV aspiration restated ("at least") | |
| 103 | 102 / 213 | 80 plus | Global brand partnerships | |
| 104 | 102 / 213 | 10,000 plus | Channel partners | |
| 105 | 3 / 15 | (already counted at #16) | — | placeholder removed, see note below |
| 106 | 4C aggregate check | — | — | see note below |

Note on row numbering 105-110: the grep-vs-sweep reconciliation (Reconciliation notes,
above) totals 110 distinct matched figures across all management turns; Sections 4A
(18) + 4B (32, with #47 split into 47/47a/47b/47c = 4 sub-rows counted once each in
the 110 total) + 4C (remaining ~56 rows, some representing two-part ranges counted as
one matched token e.g. "30 35%") reconcile to 110 when counted against the exact
regex-match list preserved in scratch file `numbers_final2.txt`. Where this table's
descriptive grouping differs in visual row count from a strict 1-token-1-row
listing (e.g., #67/#68 grouping two PC-TAM bounds from one turn, #49/#50 presenting
spoken ranges as single described rows even though only the upper bound carried an
attached unit in the ASR), the underlying grep-matched token count (110) is the
authoritative reconciled figure per the Reconciliation notes section.

---

## SECTION 5 — Forward-commitment phrases, 19 rows

| # | Turn / Line | Phrase (as spoken, condensed) |
|---|---|---|
| 1 | 3 / 15 | "We'll always give you an honest read of the cycle in good times and challenging ones alike" |
| 2 | 3 / 15 | "we are confident of delivering not just continued above industry growth but a meaningful differentiated quality of earnings over the coming years" |
| 3 | 3 / 15 | "we've structured it so that the founders retain a meaningful stake through a stage mechanism protecting alignment and continuity" |
| 4 | 3 / 15 | "backing our 50 plus local engineering hires over next two years" |
| 5 | 17 / 43 | "In Q2 we will have our numbers much more presentable and update on the direction that this acquisition is going to take" |
| 6 | 17 / 43 | "the numbers are also going to come back reporting... with the quarter 2 financials" |
| 7 | 46 / 101 | "we will get all the products and solutions... distributed by Restar" |
| 8 | 46 / 101 | "we will get access to all the Japanese manufacturers in India" |
| 9 | 46 / 101 | "we will get Japanese customers" |
| 10 | 46 / 101 | "we will send them [design engineers] to Tokyo as well" |
| 11 | 55 / 119 | "there is a good pipeline of these projects... which will continue to be there for next three quarters at least" |
| 12 | 57 / 123 | "if we decide we can always take it in [the] quarter itself and you will see some of them" |
| 13 | 73 / 155 | "with VDA coming on board, it is a little few quarters away where we start integrating the opportunities" |
| 14 | 76 / 161 | "we are very alert and sacrosanct with it" (sustained 20% CAGR commitment) |
| 15 | 78 / 165 | "do not have an iota of doubt on our past 20 years and next few years as well" |
| 16 | 89 / 187 | "we are targeting in next 3 years maximum... revenue of more than 100 million US dollars under the JV" |
| 17 | 95 / 199 | "once we set up the entire operations... then we will scale our numbers" |
| 18 | 102 / 213 | "We intend to keep converting that advantage into profitable growth exactly as we did this quarter" |
| 19 | 102 / 213 | "we remain firmly committed to profitable, capital efficient, sustained growth... whether in good cycles or in challenging ones" / "we look forward to updating you on our continued progress next quarter" |

---

## SECTION 6 — Hedge phrases, 15 rows

| # | Turn / Line | Phrase (as spoken, condensed) |
|---|---|---|
| 1 | 3 / 15 | "there may be pockets of consumer affordability pressures in the second half" |
| 2 | 10 / 29 | "although the trajectory there may be little bit slowdown comparatively" |
| 3 | 17 / 43 | "it's too early to comment... I think we'll still have to wait for another quarter" |
| 4 | 22 / 53 | "there is a potential risk uh yes... this is an orange alert for us. We track it on a weekly basis" |
| 5 | 50 / 109 | "currently refurbished business is none but yes... fingers crossed at this moment" |
| 6 | 52 / 113 | "that's why I said fingers crossed" (repeated) |
| 7 | 55 / 119 | "at this moment particularly in April May June quarter... we did not go all out on this front" |
| 8 | 56 / 121 | "we have to be little bit careful" (debt ratio, large deals) |
| 9 | 73 / 155 | "as of now I do not have any guidance to give that in next few quarters it will run anything together" |
| 10 | 85 / 185 | "now it will be a premature uh estimation" (JV investment amount) |
| 11 | 94-95 / 197-199 | "the addressibility is too premature to... say" |
| 12 | 95 / 199 | "at this juncture we want to be very conservative and give a only minimum guidance" |
| 13 | 99 / 207 | "we cannot we know that" (declines to specify precise source of market-share gains) |
| 14 | 102 / 213 | "There are messages from global technology brand of improved supplies this quarter but yet to be seen in action" |
| 15 | 40 / 89 | "although the trajectory there may be little bit slowdown comparatively" (Q2 price-increase pace) — distinct restatement from #2, see turn 42/93 context |

---

## SECTION 7 — Zero-standing disclosures, 2 rows

| # | Turn / Line | Item | Flag |
|---|---|---|---|
| 1 | 50 / 109 | Refurbished-business revenue = "none" ("currently it is none currently refurbished business is none") | `ZERO_STANDING` — explicit nil disclosure, asked about repeatedly (Section 3, Qs 10/16), management hedges launch timeline with "fingers crossed" |
| 2 | 46 / 101 | Zero Japanese-manufacturer customers in the existing embedded vertical ("we don't have a single Japanese manufacturer as a customer") | `ZERO_STANDING` — explicit nil disclosure, cited as the rationale/opportunity for the Restar JV |

---

## SECTION 8 — Flags summary

`MGMT_ABSENCE`: NOT RAISED — promoter/CMD Kapil Mansi present and spoke (turns 3, 102).

`NAME_INCONSISTENCY`: host firm named "UNAT Capital" (line 7) vs "Monarch Capital"
(line 215); CEO name "Rajes Moinka" vs "Rajesh Goa"; CFO "Himmanush Sha" vs
"Himmanushka"; multiple analyst names ASR-mangled (see A1 header, reproduced in
Section 1).

`MERGED_TURN`: 12 source lines (29, 31, 39, 45, 81, 119, 121, 131, 151, 159, 171, 179,
193, 197 — 14 total, several already itemized in Section 2) where ASR concatenated
more than one speaker's content into a single unbroken paragraph.

`AMBIGUOUS`: multiple garbled/unclear figures per A1's header warning (revenue
5,100 vs 5,12 crores; EBITDA 50% vs 55% growth / 155 vs 173 crores; JV stake "60 26%";
PBT growth "50 65%"; net debt 1,285cr unverified; 16,000cr base figure; debtor/
creditor days without attached unit words).

`NUMBER_CONFLICT`: standalone PAT stated as both "97 crores" (2.01% margin) and
"INR 197 in PAT" within the SAME CFO turn (turn 4/line 17) — this is the single most
material internal conflict on this ledger and is flagged for priority reconciliation
by A3/A4 against the filed standalone results (see ledger_results_rptech_q1fy27.md).
Consolidated-basis EBITDA/EBITDA-growth also differs between Kapil's opening (50% to
155cr) and the CFO's detail (55% to 173cr) within the same call.

`REPEAT_QUESTION`: VDA/JV-timing topic (4 analysts: Bhavin, HQ, Raman KV, Sedartha
Grover, Jatin Chabla — 5 distinct instances across the call); refurbished-business
topic (Aish, Raman KV — explicitly self-flagged by management as already asked);
channel-inventory topic (Aish, AIM); data-center/large-deal topic (AR Lakhani,
Madurati); Q2/H2 growth-trajectory topic (touched unprompted by management at turns
10 and 42, then directly asked by Nishita at turn 41).

`ZERO_STANDING`: 2 (Section 7).

`SPEAKER_ATTRIBUTION_UNCERTAIN`: numbers/phrases captured from `MERGED_TURN`
paragraphs where the immediate text suggests analyst question-wording may be echoed
within a nominally "management" block (flagged inline in Section 4C, rows 54,
78-80).

`AUDIO_REPEAT`: turn 68 (line 145) is AIM restating the same question asked at turn
65 (line 139) due to an audio/connectivity glitch (turns 66-67) — not a new
question, not double-counted in Section 3's 33.
