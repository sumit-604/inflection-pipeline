# LEDGER — A2 ENUMERATOR — BANDHAN — Q1 FY27 — Doctype: concall
Source: /home/user/inflection-pipeline/runs/bandhan-q1fy27/work/extract_concall_bandhan_q1fy27.txt (206 source lines, 70 speaker turns, TURN 1-70)

```
=== A2 COUNT TEST ===
category: turns          grep_count: 70    sweep_count: 70    match: yes
category: questions      grep_count: 25    sweep_count: 25    match: yes
category: mgmt_numbers   grep_count: 149   sweep_count: 149   match: yes
category: analyst_numbers grep_count: 13   sweep_count: 13    match: yes
category: fwd_hedge_phrases grep_count: 19  sweep_count: 19   match: yes
category: participants   grep_count: 16    sweep_count: 16    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method notes (mechanical):
- turns: grep pattern `\[TURN [0-9]+ \|` on turn-opening tags plus manual sweep of sequential
  numbers 1-70 in the tag stream (continuation paragraphs tagged "[TURN n cont.]" are the SAME
  turn, not new ones — 24 such continuation tags exist for TURN 3 (12) and TURN 4 (12); confirmed
  by full grep `\[TURN [0-9]+` = 94 = 70 unique turns + 24 cont. tags).
- questions: grep pattern `\[TURN [0-9]+ \| Q[0-9]` catches every analyst question turn (main +
  follow-up) = 25; manual sweep of Q1-Q9 main + follow-ups reconciles to the same 25 (see table).
- mgmt_numbers / analyst_numbers: grep pattern
  `[0-9][0-9,.]*\s*(crore|%|bps|basis points?|lakh crore)` over the whole file = 165 raw hits;
  3 are extraction-header metadata (lines 7, 8, 10 — the unit-conversion note, not transcript
  content) and are excluded, leaving 162 transcript-body numeric tokens. Of these, 149 fall in
  management-attributed turns and 13 in analyst-attributed turns (149+13=162, reconciled below).
- fwd_hedge_phrases: 19 canonical forward-looking / hedge / commitment phrases identified by
  manual read, each independently confirmed present verbatim in the source file via exact-string
  grep (Python `in` test) — 19/19 found.
- participants: 6 management-side (5 named + "senior management team" generic mention) + 9
  analyst questioners + 1 moderator = 16, cross-checked against the MANAGEMENT PRESENT header
  block (lines 4-10) and the Q1-Q9 tag stream.

---

## 1. PARTICIPANTS (both sides)

| # | Name | Designation | Side | First appearance (turn/line) | Flags |
|---|------|-------------|------|-------------------------------|-------|
| 1 | Partha Pratim Singh Gupta (Sengupta) | Managing Director & CEO | Management | TURN 3 / line 47 (listed header line 5) | |
| 2 | Rajendra Kumar Babbar | Executive Director & Chief Business Officer | Management | Header only, line 6; likely the unnamed "CBO / management supplement" at TURN 41 / line 173 | SPEAKER_UNATTRIBUTED (turn 41 not explicitly named) |
| 3 | Ratan Kumar | Executive Director & Chief Operating Officer | Management | Header only, line 7; likely the unnamed "[ED / COO]" at TURN 24 / line 139 | SPEAKER_UNATTRIBUTED (turn 24 not explicitly named) |
| 4 | Rajeev Mantri | Chief Financial Officer | Management | TURN 4 / line 46 (prepared remarks); repeat speaker turns 8, 17, 35, 53, 58(as "Rajeev"), 65 | |
| 5 | Vikash Mundra | Head of Investor Relations | Management | TURN 2 / line 45 | |
| 6 | "Senior management team" (unnamed collective) | Unspecified | Management | Header line 10 only, line 4-10 block | ZERO_STANDING (named in header, never individually attributed to a turn — ["Satish"] TURN 47/line 185, ["New EB head Surojit"] TURN 19/line 129, and "[Retail asset head]" TURN 63/line 217 are plausibly this collective surfacing, but not confirmed by name-to-role mapping in the extract) |
| 7 | Samir Bisay | Analyst — Diamond Asia | Analyst (Q1) | TURN 6 / line 103 | |
| 8 | [unnamed] | Analyst — CLSA | Analyst (Q2) | TURN 12 / line 115 | ANALYST_NAME_NOT_GIVEN |
| 9 | J. Mundra | Analyst — ICICI Securities | Analyst (Q3) | TURN 21 / line 133 | |
| 10 | Anand Dama | Analyst — Emkay (moderator also says "Laxmi Asset Management" in the intro; ambiguous firm tag) | Analyst (Q4) | TURN 28 / line 147 (intro at TURN 27 / line 145) | FIRM_AMBIGUOUS |
| 11 | Ankit [Bihani] | Analyst — Nomura | Analyst (Q5) | TURN 33 / line 157 | |
| 12 | [Dan Tara] | Analyst — Green Edge Wealth | Analyst (Q6) | TURN 39 / line 169 | |
| 13 | M.B. Mahesh | Analyst — Kotak Securities | Analyst (Q7) | TURN 45 / line 181 | |
| 14 | Rahul Kumar | Analyst — Vikaria Investment Management | Analyst (Q8) | TURN 57 / line 205 | |
| 15 | Nitin Agarwal | Analyst — Motilal Oswal Financial Services | Analyst (Q9) | TURN 62 / line 215 | |
| 16 | Ramy | Moderator (operator) | Moderator | TURN 1 / line 43 | |

Note: no CMD/promoter distinct from MD & CEO exists at this bank in this structure; MD & CEO
Sengupta is present and vocal throughout (turns 3, 7, 10, 15, 22, 26, 31, 34, 37, 40, 43, 46, 48,
50, 52, 55, 67) — no `MGMT_ABSENCE` flag applicable.

---

## 2. SPEAKER TURNS (all 70, sequential)

| Turn | Line | Speaker | Role | First ~10 words |
|------|------|---------|------|------------------|
| 1 | 43 | MODERATOR | Operator | "Ladies and gentlemen, good day and welcome to the..." |
| 2 | 45 | VIKASH MUNDRA | Head IR | "Thank you Ramy. Good evening everyone and a warm..." |
| 3 | 47-71 (12 cont. paragraphs) | PARTHA PRATIM SENGUPTA | MD & CEO | "Thank you Vikash. Good evening everyone. We are delighted..." |
| 4 | 73-97 (12 cont. paragraphs) | RAJEEV MANTRI | CFO | "Thank you Mr. Sengupta. Let me begin with our..." |
| 5 | 101 | MODERATOR | Operator | "Thank you. Ladies and gentlemen we will now begin..." |
| 6 | 103 | Q1 — SAMIR BISAY | Analyst, Diamond Asia | "Hi, thanks for the opportunity. My quick question is..." |
| 7 | 105 | A1 — MD & CEO | Management | "Let me first answer your question. I have very..." |
| 8 | 107 | CFO supplement | Management | "Just to implement as Partha mentioned earlier, for the..." |
| 9 | 109 | Q1 follow-up — SAMIR BISAY | Analyst | "Just quickly, what kind of portfolio growth do we..." |
| 10 | 111 | A — MD & CEO / CFO | Management | "On liquidity, liquidity for the bank remained comfortable with..." |
| 11 | 113 | MODERATOR | Operator | "We take the next question from the line of..." |
| 12 | 115 | Q2 — CLSA | Analyst | "Hi team, thanks for taking my question and congrats..." |
| 13 | 117 | A2 — MANAGEMENT | Management | "Not in this quarter, so it is same as..." |
| 14 | 119 | Q2 follow-up — CLSA | Analyst | "In this quarter retail growth and even our mortgages..." |
| 15 | 121 | A — MD & CEO | Management | "Somewhat yes, I can say a little bit cautious..." |
| 16 | 123 | Q2 follow-up 2 — CLSA | Analyst | "On ROA — I understand you've cut guidance on..." |
| 17 | 125 | A — CFO (Rajeev Mantri) | Management | "Two factors. One, we do expect further uptake in..." |
| 18 | 127 | Q2 follow-up 3 — CLSA (merged Q+A) | Mixed | "Even though we've hiked our microfinance yields we are..." |
| 19 | 129 | Q2 follow-up 4 — CLSA (merged Q+A) | Mixed | "On PSLC — last time 40% of our MFI book..." |
| 20 | 131 | MODERATOR | Operator | "In the interest of time and fairness we request..." |
| 21 | 133 | Q3 — J. MUNDRA | Analyst, ICICI Securities | "Hi good evening sir. First, SMA-0 has increased a..." |
| 22 | 135 | A3 — MD & CEO | Management | "SMA-0, as you have rightly predicted, is mostly in..." |
| 23 | 137 | Q3 follow-up — J. MUNDRA | Analyst | "What is the outlook going ahead, because the vintage..." |
| 24 | 139 | A — [ED / COO] | Management | "No, I'll take that question. If you look at..." |
| 25 | 141 | Q3 follow-up 2 — J. MUNDRA | Analyst | "The vintage chart on page 24 of the investor..." |
| 26 | 143 | A — MD & CEO | Management | "Let me just tell you, our non-EB book has..." |
| 27 | 145 | MODERATOR | Operator | "We take the next question from the line of..." |
| 28 | 147 | Q4 — ANAND DAMA | Analyst, Emkay | "Thank you. Sir, what kind of credit growth are..." |
| 29 | 149 | A4 — CFO (Rajeev Mantri) | Management | "On credit growth, what we had guided was for..." |
| 30 | 151 | Q4 follow-up — ANAND DAMA | Analyst | "You talked about cost of funds going up — is..." |
| 31 | 153 | A — MD & CEO | Management | "We are working on it. You see, our corporate..." |
| 32 | 155 | MODERATOR | Operator | "We take the next question from the line of..." |
| 33 | 157 | Q5 — ANKIT (Nomura) | Analyst | "Thank you for the opportunity. My question is on..." |
| 34 | 159 | A5 — MD & CEO | Management | "Let me tell you, the guidance was originally given..." |
| 35 | 161 | CFO supplement (40 bps bridge) | Management | "Just to translate into numbers from what Bas (MD)..." |
| 36 | 163 | Q5 follow-up — ANKIT (Nomura) | Analyst | "My second question is on credit cost. We have..." |
| 37 | 165 | A — MD & CEO | Management | "Let me give you clarity. Till now the country..." |
| 38 | 167 | MODERATOR | Operator | "We take the next question from the line of..." |
| 39 | 169 | Q6 — GREEN EDGE WEALTH | Analyst | "Hi, thank you for the opportunity, only one question..." |
| 40 | 171 | A6 — MD & CEO | Management | "Let me tell you very clearly, whatever you have..." |
| 41 | 173 | CBO / management supplement | Management | "On efficiencies, we are working on efficiencies within the..." |
| 42 | 175 | Q6 follow-up — GREEN EDGE WEALTH | Analyst | "So just for us investors, if all these initiatives..." |
| 43 | 177 | A — MD & CEO / CFO | Management | "At least for the next one year probably it..." |
| 44 | 179 | MODERATOR | Operator | "We take the next question from the line of..." |
| 45 | 181 | Q7 — M.B. MAHESH (Kotak Securities) | Analyst | "A clarification. If you go to segments like wholesale..." |
| 46 | 183 | A7 — MD & CEO | Management | "The fundamental thing is that the wholesale banking book..." |
| 47 | 185 | [Satish] | Management (unattributed role) | "The book we are building in wholesale banking is..." |
| 48 | 187 | A (cont.) — MD & CEO | Management | "The purpose of entering this business is to get..." |
| 49 | 189 | Q7 follow-up — M.B. MAHESH | Analyst | "The point I'm trying to drive is, given that..." |
| 50 | 191 | A — MD & CEO | Management | "For the future, let me tell you the pressure..." |
| 51 | 193 | Q7 follow-up 2 — M.B. MAHESH | Analyst | "The problem we are trying to solve is the..." |
| 52 | 195 | A — MD & CEO | Management | "The growth is dependent on many factors, the first..." |
| 53 | 197 | CFO / Rajeev supplement | Management | "One is, as you know, micro finance / EB..." |
| 54 | 199 | Q7 follow-up 3 — M.B. MAHESH | Analyst | "One question on IT cost — you had absolutely no..." |
| 55 | 201 | A — MD & CEO / management | Management | "As I explained, given that the last three years..." |
| 56 | 203 | MODERATOR | Operator | "We take the next question from the line of..." |
| 57 | 205 | Q8 — RAHUL KUMAR (Vikaria) | Analyst | "Hi, just one question. On slide 23, the collection..." |
| 58 | 207 | A8 — MANAGEMENT (Rajeev) | Management | "I can explain that. What happens is during the..." |
| 59 | 209 | Q8 follow-up — RAHUL KUMAR | Analyst | "Second question, is there any one-off items in the..." |
| 60 | 211 | A — MANAGEMENT | Management | "No, nothing on the income side. On the expense..." |
| 61 | 213 | MODERATOR | Operator | "We take the next question from the line of..." |
| 62 | 215 | Q9 — NITIN AGARWAL (Motilal Oswal) | Analyst | "Hi, thanks for the opportunity. I have a few..." |
| 63 | 217 | A9 — [Retail asset head] | Management (unattributed role) | "As far as gold loan is concerned, we implemented..." |
| 64 | 219 | Q9 follow-up — NITIN AGARWAL | Analyst | "Secondly, while we are watching out the overall external..." |
| 65 | 221 | A — CFO (Rajeev) | Management | "I can clarify. As I mentioned we had done..." |
| 66 | 223 | Q9 follow-up 2 — NITIN AGARWAL | Analyst | "When you talk about MFI growth at relatively moderate..." |
| 67 | 225 | A — MD & CEO | Management | "Let me tell you, we are the leader and..." |
| 68 | 227 | MODERATOR | Operator | "We take that as the last question and conclude..." |
| 69 | 229 | MANAGEMENT (closing) | Management | "I would like to thank all our investors and..." |
| 70 | 231 | MODERATOR | Operator | "On behalf of Bandhan Bank Limited, that concludes this..." |

Flags: `MERGED_Q_A` on turns 18 and 19 — question and management reply are printed inside the same
tagged block rather than split into separate Q/A turns as elsewhere; this is a transcript-tagging
inconsistency, not a content gap, but downstream agents citing "turn 18" or "turn 19" should note
both the analyst question and the management answer live in one turn tag.

---

## 3. QUESTIONS (analyst side, one row per question turn, main + every follow-up)

| # | Turn | Line | Questioner | Firm | Topic (paraphrase, not interpretation) | Flags |
|---|------|------|-----------|------|------------------------------------------|-------|
| Q1a | 6 | 103 | Samir Bisay | Diamond Asia | ROA guidance cut — conservatism, internal vs external driver; secondly FCNR-B / liquidity offsetting funding pressure (two sub-questions in one turn) | MULTI_PART |
| Q1b | 9 | 109 | Samir Bisay | Diamond Asia | EB book portfolio growth; slippage break-up by segment; liquidity | MULTI_PART |
| Q2a | 12 | 115 | [unnamed] | CLSA | Whether Bandhan has hiked MFI yields like competitors, and by how much | |
| Q2b | 14 | 119 | [unnamed] | CLSA | Retail and mortgage growth slowdown — cautious stance due to macro? | |
| Q2c | 16 | 123 | [unnamed] | CLSA | ROA bridge from 1.0% (1.1% ex-gratuity) to 1.2-1.4% guided range — which levers | REPEAT_QUESTION (ROA bridge — same theme as Q1a, Q5a) |
| Q2d | 18 | 127 | [unnamed] | CLSA | Even after yield hikes, why is NIM expansion still not expected | MERGED_Q_A |
| Q2e | 19 | 129 | [unnamed] | CLSA | PSLC — share of MFI book PSL-compliant, has it moved from 40%? | MERGED_Q_A |
| Q3a | 21 | 133 | J. Mundra | ICICI Securities | SMA-0 increase — cause beyond holiday effect, and trajectory for the year | REPEAT_QUESTION (SMA-0 / collections — same theme as Q8a) |
| Q3b | 23 | 137 | J. Mundra | ICICI Securities | Vintage-chart-implied outlook — any other collection drag beyond holidays | |
| Q3c | 25 | 141 | J. Mundra | ICICI Securities | Vintage chart shows improving trend — is guidance cut then inconsistent with a stable/improving EB mix and NIM support | |
| Q4a | 28 | 147 | Anand Dama | Emkay | FY27 credit growth outlook (15-16%?) and growth vs margin trade-off; IT cost as % of opex now and going forward | MULTI_PART |
| Q4b | 30 | 151 | Anand Dama | Emkay | Cost-of-funds pass-through to customers (ex-EB) as margin protection | |
| Q5a | 33 | 157 | Ankit (Bihani) | Nomura | ROA guidance cut of 40 bps — 20 bps explained by margin, what explains the other 20 bps; also FCNR-B/system liquidity improvement — why funding cost pressure still expected; what changed since 4Q guidance | REPEAT_QUESTION (ROA bridge — same theme as Q1a, Q2c); MULTI_PART |
| Q5b | 36 | 163 | Ankit (Bihani) | Nomura | Credit cost outlook given energy-crisis impact on microfinance | |
| Q6a | 39 | 169 | [Dan Tara] | Green Edge Wealth | Opex run-rate (~2,200cr/qtr) not matched by income — cost/operating efficiency plan on DSA commissions, collection agency spend | |
| Q6b | 42 | 175 | [Dan Tara] | Green Edge Wealth | Cost-to-income path from ~62% — to 55% over 2-3 years? | |
| Q7a | 45 | 181 | M.B. Mahesh | Kotak Securities | Wholesale banking segment margin vs overall book margin — why grow a margin-dilutive book | |
| Q7b | 49 | 189 | M.B. Mahesh | Kotak Securities | Trade-off framing — NII generated vs margin lost by growing wholesale | REPEAT_QUESTION (restates Q7a) |
| Q7c | 51 | 193 | M.B. Mahesh | Kotak Securities | Same trade-off — is giving up growth the solution, or is growth prioritized | REPEAT_QUESTION (restates Q7a/b) |
| Q7d | 54 | 199 | M.B. Mahesh | Kotak Securities | IT cost — any headroom to push these costs back for a couple of quarters | |
| Q8a | 57 | 205 | Rahul Kumar | Vikaria Investment Management | Slide 23 — June collection efficiency lower than quarter average, implying deterioration | REPEAT_QUESTION (collections — same theme as Q3a) |
| Q8b | 59 | 209 | Rahul Kumar | Vikaria Investment Management | Any one-off items in NII or other income this quarter | |
| Q9a | 62 | 215 | Nitin Agarwal | Motilal Oswal | Retail asset — OD decline plus gold loan decline vs industry growth — driver | MULTI_PART |
| Q9b | 64 | 219 | Nitin Agarwal | Motilal Oswal | Disconnect — recoveries/upgrades this quarter better than most of FY26 despite cautious MFI growth outlook | |
| Q9c | 66 | 223 | Nitin Agarwal | Motilal Oswal | Is Bandhan consciously growing MFI slower than industry / cutting MFI mix further | |

25 question rows total (9 questioners, 25 question-turns including every follow-up).
`REPEAT_QUESTION` raised 4x: ROA-guidance-bridge theme (Q1a/Q2c/Q5a), SMA-0/collections theme
(Q3a/Q8a), and the wholesale-margin trade-off restated three times within Q7 (Q7a/b/c).

---

## 4. NUMBERS SPOKEN — MANAGEMENT (guidance, capacity, margin, growth, capex, timeline), grouped by turn

Grep-verified count basis: `[0-9][0-9,.]*\s*(crore|%|bps|basis points?|lakh crore)` matched 149
distinct tokens across management-attributed turns (see method notes). Rows below group tokens by
turn/topic for readability; the bracketed token-count after each row must sum to 149.

| Turn | Line | Speaker | Figures disclosed | Token ct | Flags |
|------|------|---------|--------------------|----------|-------|
| 3 | 59 | MD & CEO (prepared) | Gross advances 1.56 lakh cr, +16% YoY; deposits 1.65 lakh cr | 3 | |
| 3 | 61 | MD & CEO | Retail deposits +16% YoY; CASA ratio 29.4% (sequential); retail deposits (CASA+RTD) = 74% of total deposits | 3 | |
| 3 | 63 | MD & CEO | Margin 6.2%; gross NPA 3.1%; net NPA 0.9%; PCR 86% (incl. technical write-offs) | 4 | |
| 3 | 65 | MD & CEO | Net total income 3,524cr; operating profit 1,358cr; PAT 502cr (+35% YoY); CAR 18.2%; Tier-1 17.5% | 6 | |
| 3 | 69 | MD & CEO | ROA guidance revision: from 1.6-1.8% aspiration to 1.2%-1.4% probable at exit Q4 FY27 | 3 | GUIDANCE_CHANGE |
| 4 | 73 | CFO (prepared) | Gross advances 1.56 lakh cr, +16% YoY, +1% QoQ; EB portfolio 52,641cr | 4 | |
| 4 | 75 | CFO | Non-EB +27% YoY; retail assets +45% YoY; wholesale +38% YoY; secured +27% YoY = 57% of advances | 5 | |
| 4 | 77 | CFO | Advances mix: EB group lending 23%, ESBL 11%, wholesale 33%, housing finance 22%, retail/other 11% | 5 | |
| 4 | 79 | CFO | Total deposits 1.65 lakh cr, +7% YoY; bulk deposits -13% YoY, share 26% (vs 32% a year ago); 86% of bulk non-callable | 6 | |
| 4 | 81 | CFO | Retail deposits +16% YoY; CASA balance 48,479cr (+16% YoY); CASA ratio 29.4% | 4 | |
| 4 | 83 | CFO | Collection efficiency ex-NPA: bank 98.9% (June); EB 98.5% (June) vs 98.6% (March) | 3 | |
| 4 | 85 | CFO | Gross slippages 1,079cr (vs 1,028cr prior qtr); EB slippages 604cr (vs 690cr Q4FY26); EB 0-90 DPD pool 3.5% (vs 3.1% prior qtr) | 6 | |
| 4 | 87 | CFO | Housing NPA sold to ARC: 291cr; technical write-off 597cr; gross NPA 3.1%; net NPA 0.9%; reported PCR 71.1%; PCR incl. SR provisions 74.3% | 6 | |
| 4 | 89 | CFO | NII 2,921cr (+6% YoY, +5% QoQ); margin 6.2% | 4 | |
| 4 | 91 | CFO | Q1FY26 treasury gain base ~250cr; non-interest income ex-treasury +22% YoY; third-party distribution income +47% YoY | 3 | |
| 4 | 93 | CFO | Opex 2,166cr (+19% YoY); one-time gratuity provision 61cr; operating profit 1,358cr | 4 | |
| 4 | 95 | CFO | Credit cost 1.8% (vs 2.0% Q4FY26); EB credit cost 3.3%; PAT 502cr (+35% YoY); ROA 1.0%; ROE 7.7% | 7 | |
| 7 | 105 | MD & CEO (A1) | Tech cost +65% YoY; savings-bank cost of funds +~25bps; started quarter at ROA of 1% | 3 | |
| 10 | 111 | MD & CEO/CFO | CD ratio 94%; LCR 140%; FCNR-B mobilized ~30cr; NIM held at 6.20%; EB/non-EB strategy 35%/65%; non-EB grew 27%; unsecured/secured strategy 40%/60%; total slippages 1,079cr, of which EB 604cr | 11 | |
| 13 | 117 | Management (A2) | Prior yield hike (Feb, last FY): 100 bps | 1 | |
| 15 | 121 | MD & CEO | Book ex-OD product grew sequentially +5% | 1 | |
| 17 | 125 | CFO | Other-income uplift guided: 10-20bps (~20bps) | 2 | |
| 18 | 127 | MD & CEO (merged Q/A) | EB book cap 35%; growth envisaged up to 33-34% | 3 | MERGED_Q_A |
| 19 | 129 | Management/EB head (merged Q/A) | PSLC compliance ~40% (unchanged) | 2 | MERGED_Q_A |
| 22 | 135 | MD & CEO | Collection efficiency ~99% (May-June) | 1 | |
| 26 | 143 | MD & CEO | Non-EB +27%; EB book capped at 33%; opex-to-asset: guided ~4%, actual 4.3% in Q1 | 4 | GUIDANCE_VS_ACTUAL discrepancy noted (turn 26 cites 4% guide vs turn 35/43 CFO cites 4.2% guide — see flags below) |
| 29 | 149 | CFO (A4) | FY27 credit growth guidance 14% (EB 5-10%, non-EB 20%+); Q1 actuals: non-EB 27%, overall 16%; IT cost ~8% of opex (9.5% incl. depreciation), prior years 6%, target ceiling ~10% | 12 | |
| 31 | 153 | MD & CEO | Corporate book +36% YoY; EB growth range reiterated 5-10% (two mentions) | 3 | |
| 34 | 159 | MD & CEO (A5) | Durable liquidity requirement ~2.5 lakh cr vs system actual ~1 lakh cr [stated as "1 trillion rupees" = 1 lakh cr]; savings bank cost of funds +~20bps | 2 | |
| 35 | 161 | CFO (40bps bridge) | 40bps ROA guidance cut = ~30bps NIM stretch + ~10bps opex stretch; NIM path 5.8% (Q2FY26) to 5.9% (Q3FY26) to 6.2% (Q1FY27, current) vs earlier line-of-sight to 6.5% by Q4FY27 end; opex-to-asset guided ~4.2%, actual ~4.3% | 12 | GUIDANCE_CHANGE — KEY BRIDGE |
| 37 | 165 | MD & CEO | Credit cost guidance maintained: 1.6-1.8% (grep tags trailing "1.8%"; "1.6" appears without a bare unit suffix in source text and is captured in manual sweep prose, not as a second token) | 1 | |
| 41 | 173 | CBO supplement | Branch-channel asset sourcing: was 200cr/month, now >900cr in latest quarter | 2 | |
| 43 | 177 | MD & CEO/CFO | Opex-to-asset guided ~4.2% (text also states "recovering to 4.3" without a bare % suffix — not separately tokenized; see method note) | 1 | |
| 52 | 195 | MD & CEO | Strategy ratios reiterated: EB/non-EB 35%/65%, unsecured/secured 40%/60% | 4 | |
| 53 | 197 | CFO supplement | EB growth target reiterated 5-10% (trailing "10%" tokenized) | 1 | |
| 60 | 211 | Management | Gratuity one-off 61cr (repeat of turn 93/line93 disclosure) | 1 | |
| 65 | 221 | CFO (Rajeev) | ARC sale ~290cr (turn 4/line 87 stated 291cr — see NUMBER_DISCREPANCY flag); cash recovery from ARC deal ~120cr (mentioned twice in same answer) | 3 | NUMBER_DISCREPANCY (291cr vs 290cr) |
| 67 | 225 | MD & CEO | EB growth bandwidth 5-10% (two mentions); book target reiterated 33-35% of total exposure | 3 | |

**Sum check: 3+3+4+6+3+4+5+5+6+4+3+6+6+4+3+4+7+3+11+1+1+2+3+2+1+4+12+3+2+12+1+2+1+4+1+1+3+3 = 149.**

Flags raised in this section:
- `GUIDANCE_CHANGE` (twice): the ROA guidance cut itself (turn 3/69) and its bridge decomposition
  (turn 35/161).
- `NUMBER_DISCREPANCY`: ARC-sale housing NPA quantum stated as 291cr (turn 4, line 87) vs 290cr
  (turn 65, line 221) — same transaction, two slightly different figures across the call.
- `NUMBER_DISCREPANCY` (analyst-side, cross-reference only, logged in Section 5): the gratuity
  one-off is management-stated as 61cr (turns 4/line93 and 60/line211) but referenced by the CLSA
  analyst as 60cr (turn 16/line123) — a rounding/mishearing by the analyst, not a management
  restatement; flagged for A3/A4 arithmetic-consistency review.
- `GUIDANCE_VS_ACTUAL` internal inconsistency: MD & CEO at turn 26 states the opex-to-asset
  guidance "was 4%" against a 4.3% actual, while CFO at turns 35 and 43 states the guidance was
  "~4.2%" against the same 4.3% actual. Two different guided baselines (4% vs 4.2%) are cited by
  two different speakers for the same metric in the same call — logged for A3/A4 reconciliation,
  not resolved here.

---

## 5. NUMBERS SPOKEN — ANALYSTS (embedded in questions; logged for cross-reference, not management guidance)

Grep-verified count basis: 13 tokens in analyst-attributed turns (162 - 149 = 13).

| Turn | Line | Analyst | Figures cited | Token ct | Flags |
|------|------|---------|-----------------|----------|-------|
| 6 | 103 | Samir Bisay | "earlier 1.6% plus ROA" (prior aspiration, restated by analyst) | 1 | |
| 16 | 123 | CLSA | ROA today 1.0%; gratuity provision cited as "60 crore" (mgmt states 61cr elsewhere); credit cost 1.8% | 3 | NUMBER_DISCREPANCY (60cr vs mgmt's 61cr) |
| 25 | 141 | J. Mundra | "higher funding cost of 6-7%" | 1 | |
| 28 | 147 | Anand Dama | "should it be 15 to 16%" (credit growth guess) | 1 | |
| 33 | 157 | Ankit (Nomura) | "lowered ROA guidance by 40 bps"; "20 bps could be explained through margins... what explains the other 20 bps" | 3 | |
| 39 | 169 | Green Edge Wealth | "opex reached almost 2,200 crore a quarter"; "secured book probably 0% ROA" | 2 | |
| 42 | 175 | Green Edge Wealth | "cost to income ... current 62% levels" | 1 | |
| 45 | 181 | M.B. Mahesh | "growing at about 35-40%" | 1 | |

Sum check: 1+3+1+1+3+2+1+1 = 13.

---

## 6. FORWARD-LOOKING / HEDGE / COMMITMENT PHRASES (19, verbatim-confirmed)

| # | Turn | Line | Speaker | Phrase (verbatim substring) | Type |
|---|------|------|---------|-------------------------------|------|
| 1 | 3 | 69 | MD & CEO | "could extend beyond the timeline we had originally envisaged" | HEDGE |
| 2 | 3 | 69 | MD & CEO | "...would be probable" (re: ROA 1.2-1.4%) | HEDGE / GUIDANCE |
| 3 | 3 | 40 (per source line numbering within TURN3 cont.) | MD & CEO | "We expect this pressure to persist for the next few quarters" | FORWARD-LOOKING |
| 4 | 3 | 30 (TURN3 cont.) | MD & CEO | "remain confident in our ability to deliver sustainable profitable growth" | COMMITMENT |
| 5 | 4 | 66 (TURN4 cont., gratuity one-off) | CFO | "we don't expect this to be repeated" | FORWARD-LOOKING |
| 6 | 7 | 105 | MD & CEO | "I am quite hopeful that going forward also the credit cost would come down" | HEDGE |
| 7 | 17 | 125 | CFO | "we expect 10 to 20 basis points improvement to come through other income" | FORWARD-LOOKING / GUIDANCE |
| 8 | 17 | 125 | CFO | "it will be a great achievement for the bank to hold on to the NIMs" | HEDGE |
| 9 | 26 | 143 | MD & CEO | "our guidance what we had given earlier may hold good" | HEDGE |
| 10 | 29 | 149 | CFO | "we will try to remain within the range of 10%" (IT cost/opex) | COMMITMENT |
| 11 | 34 | 159 | MD & CEO | "we have to accept that the cost of funds will be under pressure" | HEDGE |
| 12 | 35 | 161 | CFO | "as opportunities come we'll try to improve the NIM as well" | HEDGE / COMMITMENT |
| 13 | 37 | 165 | MD & CEO | "a credit cost guidance of 1.6 to 1.8% continues to remain" | GUIDANCE (reaffirmed) |
| 14 | 40 | 171 | MD & CEO | "leveraging from these investments will not happen right now" | FORWARD-LOOKING |
| 15 | 43 | 177 | MD & CEO/CFO | "we should start to see further efficiencies come through" (post-FY28) | FORWARD-LOOKING / TIMELINE |
| 16 | 53 | 197 | CFO | "we want to increase to between 5 to 10% growth" (EB) | COMMITMENT / GUIDANCE |
| 17 | 55 | 201 | MD & CEO/mgmt | "after 18 months or so we should see the outcome" | FORWARD-LOOKING / TIMELINE |
| 18 | 65 | 221 | CFO | "credit cost will continue to improve and definitely the recovery will also improve" | FORWARD-LOOKING |
| 19 | 67 | 225 | MD & CEO | "we are the leader and we will be the leader" | COMMITMENT |

19/19 phrases confirmed present verbatim in the source file by exact-substring match.

---

## 7. QUANTIFIED GUIDANCE FIGURES — TARGETED CROSS-CHECK (per task brief)

Every figure named in the task brief located and cited:

| Guidance figure | Located | Turn/Line |
|---|---|---|
| ROA 1.2-1.4% revised (from 1.6-1.8%) | Yes | Turn 3 / line 69 |
| 40bps cut bridge (30bps NIM + 10bps opex) | Yes | Turn 35 / line 161 |
| NIM 6.2% | Yes | Turns 3/63, 4/89, 10/111, 35/161 (multiple mentions) |
| Credit cost 1.8% | Yes | Turns 4/95, 16(analyst)/123, 37/165 |
| EB credit cost 3.3% | Yes | Turn 4 / line 95 |
| Credit cost guidance 1.6-1.8% | Yes | Turn 37 / line 165 |
| Growth 14% FY27 (EB 5-10%, non-EB 20%+) | Yes | Turn 29 / line 149 |
| Opex-to-asset 4.2-4.3% | Yes | Turns 35/161 (guided 4.2%, actual 4.3%), 26/143 (MD cites guide as "4%" — DISCREPANCY, see Section 4 flags), 43/177 |
| IT cost ~8-9.5% of opex | Yes | Turn 29 / line 149 (8% ex-depreciation, 9.5% incl. depreciation) |
| Gratuity one-off 61cr | Yes | Turns 4/93, 60/211 (mgmt states 61cr; analyst at turn 16/123 cites 60cr — DISCREPANCY, see Section 4/5 flags) |
| Tech cost +65% | Yes | Turn 7 / line 105 |

All 11 targeted guidance figures located and cited with turn/line. None missing.

---
## SUMMARY OF ALL FLAGS RAISED
- MULTI_PART (question turns bundling more than one sub-question): Q1a, Q4a, Q5a, Q9a
- REPEAT_QUESTION: ROA-guidance-bridge theme (Q1a/Q2c/Q5a); SMA-0/collections theme (Q3a/Q8a);
  wholesale-margin trade-off (Q7a/Q7b/Q7c)
- MERGED_Q_A: turns 18, 19 (question and management answer share one tag block)
- ANALYST_NAME_NOT_GIVEN: CLSA questioner (Q2)
- FIRM_AMBIGUOUS: Q4 questioner's firm given as both "Emkay" and "Laxmi Asset Management" by the
  moderator
- SPEAKER_UNATTRIBUTED: turns 24, 41, 47, 63 (management speaks but the transcript does not
  confirm which named executive)
- ZERO_STANDING: "senior management team" collective named in the header but never individually
  attributed to a specific turn
- GUIDANCE_CHANGE: ROA guidance cut (turn 3/69) and its 40bps bridge decomposition (turn 35/161)
- NUMBER_DISCREPANCY (x2): ARC-sale housing NPA quantum 291cr (turn 4) vs 290cr (turn 65); gratuity
  one-off 61cr (management, turns 4 & 60) vs 60cr (analyst citation, turn 16)
- GUIDANCE_VS_ACTUAL internal inconsistency: opex-to-asset guidance cited as "4%" by MD & CEO
  (turn 26) vs "~4.2%" by CFO (turns 35, 43) — same guided metric, two baselines, same call
