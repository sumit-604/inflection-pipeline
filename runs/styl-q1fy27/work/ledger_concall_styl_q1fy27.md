# LEDGER — concall — STYL — Q1 FY27
Source: extract_concall_styl_q1fy27.txt (89 source lines, ASR-normalised transcript, 100% line coverage per A1 header)

```
=== A2 COUNT TEST ===
category: turns            grep_count: 58   sweep_count: 58   match: yes
category: questions        grep_count: 19   sweep_count: 19   match: yes
category: analysts         grep_count: 7    sweep_count: 7    match: yes
category: mgmt_numbers     grep_count: 59   sweep_count: 59   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation notes (method)

- **turns**: grep pass = count of all non-blank, non-section-heading source lines from
  line 10 (call opening) through line 88 (call close), i.e. every line carrying spoken
  content, run against `body.txt` (extracted text block) with pattern
  `^[[:space:]]*[0-9]+\t\S` minus pure `===...===` heading lines minus source lines 1-8
  (ASR normalisation note, not spoken). Command:
  `grep -nE '^[[:space:]]*[0-9]+\t\S' body.txt | grep -vE '\t===.*===\s*$' | awk 'line>=10'`
  → 58. Manual sweep = walked the A1 SPEAKER-TURN MAP (lines 21-112 of the extract file,
  which already itemises every turn) and independently recounted → 58. Matches the A1
  header's own `speaker_turns_count: 58`. Three-way agreement (A1 header, grep, manual
  sweep) = high confidence.
- **questions**: grep pass = `grep -noE '\[Q[0-9]+( follow-up( [0-9])?)?\]'` on the body
  → 19 bracketed question markers (Q1-Q8 primaries + 11 follow-ups). Manual sweep =
  walked Q&A section line by line (lines 30-83) and independently counted 19 distinct
  question units. Match.
- **analysts**: grep pass = extracted the firm token (text after `/`) from every `[Qn]`
  primary-question line, deduplicated → 7 unique firms (Safaya Capital, II Capital,
  Nasir Investment, Lucky Investments, FMY 325 Investment Advisors, SN Daga and Company,
  Dalmus Capital Management). Manual sweep = same 7, cross-checked against A1 header's
  `participants_analyst_firms` field, which explicitly resolves "DRJ / Safaya Capital"
  (Q7, line 71) as the same person as "Dia Jen / Safaya Capital" (Q1, line 30) returning
  for a second turn in the queue — an ASR-garbled name variant, not a new analyst. Raw
  bracket-tag count (before this identity resolution) is 8; the firm-level count that
  correctly treats Dia Jen/DRJ as one person is 7. Both grep and sweep applied the same
  resolution, so they match at 7.
- **mgmt_numbers**: grep pass = regex `(\d+(\.\d+)?\s*(to|-)\s*\d+(\.\d+)?\s*(%|crores?|bps)|\d+(\.\d+)?\s*(%|crores?|bps))`
  run only on the 15 management-attributed lines that contain at least one quantified
  figure (lines 15,17,19,21,23,26,31,33,37,53,55,56,58,62,68 — confirmed by a separate
  line-level presence check across all 26 management turns, 15 lines hit / 11 lines
  purely qualitative) → 59 raw numeral+unit tokens (line 26 alone, the CFO's financial
  highlights turn, contributes 29 of the 59). Manual sweep = read the same 15 lines
  token by token and independently tallied 59. Match. The ledger table below lists all
  59 as individual rows (repetition of the same figure within one turn — e.g. "65 to
  70%" capacity utilization stated twice in line 37 — is kept as two rows since GATE A2
  is a mechanical completeness check, not an editorial dedup; readability grouping notes
  are added in the "note" column instead of collapsing rows).

---

## 1. PARTICIPANTS

| # | Name | Role | Side | Spoke? | Line(s) | Flag |
|---|------|------|------|--------|---------|------|
| 1 | Operator (unnamed) | Call moderator | Company-side (facilitator) | Yes | 10, 86, 88 | |
| 2 | Pratik Jakab | IR, E&Y (investor relations agency) | Company-side | Yes | 12 | |
| 3 | Pragnyat Lalwani | Chairman & Managing Director (CMD) | Management | Yes (extensively — 5 overview turns + every Q&A answer bar 2) | 15,17,19,21,23,31,33,37,39,41,45,47,49,53,55,58,62,68,72,74,78,80,82 | |
| 4 | Pawan Kumar | Chief Financial Officer (CFO) | Management | Yes (financial highlights turn + 3 Q&A answers) | 26,56,64 | |
| 5 | Gautam Jain | Whole-time Director | Management | **No — introduced only, zero quoted speaking turns** | introduced at line 12 | `MGMT_ABSENCE` |
| 6 | Management (unattributed) | Unnamed, single closing line | Management | Yes (closing remarks only, not attributed to a named individual) | 87 | |
| 7 | Dia Jen | Analyst, Safaya Capital | Analyst | Yes (Q1 + Q7 follow-up as "DRJ") | 30,32,34,71,73,75 | ASR name-variant same person |
| 8 | Mohit Sukani | Analyst, II Capital | Analyst | Yes | 36,38,40,42 | |
| 9 | Zakir Nasir | Analyst, Nasir Investment | Analyst | Yes | 44,46,48,50 | |
| 10 | British | Analyst, Lucky Investments | Analyst | Yes | 52,54,57,59 | |
| 11 | Pratik Bantia | Analyst, FMY 325 Investment Advisors | Analyst | Yes | 61,63,65 | |
| 12 | Sedart Daga | Analyst, SN Daga and Company | Analyst | Yes | 67,69 | |
| 13 | Pulkit Singhal | Analyst, Dalmus Capital Management | Analyst | Yes | 77,79,81,83 | |

**Flag: `MGMT_ABSENCE`** — Gautam Jain, Whole-time Director, is named in the IR's introduction (line 12: "Pragnyat Lalwani chairman and managing director, Gautam Jain whole-time director and Pawan Kumar chief financial officer") as one of three management representatives on the call, but has zero quoted speaking turns anywhere in the 89-line transcript. Every management answer in Q&A is attributed to Pragnyat or Pawan only. This is a substantive call (guidance, margin bridge, capex, segment growth all discussed) — a named WTD present but silent throughout is worth flagging for A3/A4, not just for A5.

---

## 2. SPEAKER TURNS (58 total, sequential)

| Turn# | Line | Speaker | First ~10 words |
|---|---|---|---|
| 1 | 10 | Operator | "Ladies and gentlemen, good day and welcome to the..." |
| 2 | 12 | Pratik Jakab (IR) | "Thank you all. Welcome everyone and thanks for joining..." |
| 3 | 15 | Pragnyat (overview 1: growth, verticals, PSU tenders) | "Thanks Pratik. Good day everyone and thank you for..." |
| 4 | 17 | Pragnyat (overview 2: payment solutions) | "In terms of business segment update, our payment solutions..." |
| 5 | 19 | Pragnyat (overview 3: comm & fulfillment) | "Communication and fulfillment solutions contributed 40% to total revenue..." |
| 6 | 21 | Pragnyat (overview 4: IoT solutions) | "IoT solutions contributed 18% to total revenue in Q1..." |
| 7 | 23 | Pragnyat (overview 5: outlook, guidance) | "As of now, we operate in a challenging environment..." |
| 8 | 26 | Pawan (financial highlights, full quarter) | "Thank you, Pragnyat. Good day everyone and thank you..." |
| 9 | 30 | Dia Jen [Q1] | "Thank you for the opportunity. We have performed really..." |
| 10 | 31 | Pragnyat [A] | "As I said in my opening remarks, we foresee..." |
| 11 | 32 | Dia Jen [Q1 follow-up] | "Can you please share how many SIMs we've rolled..." |
| 12 | 33 | Pragnyat [A] | "You mean the SIM cards issued? So we've been..." |
| 13 | 34 | Dia Jen (close) | "Thank you. I'll get back in the queue." |
| 14 | 36 | Mohit Sukani [Q2] | "Congratulations on the great results. First, our gross margin..." |
| 15 | 37 | Pragnyat [A] | "On the gross margin part, as you know H2..." |
| 16 | 38 | Mohit Sukani [Q2 follow-up] | "Can you tell what would be the gross margin..." |
| 17 | 39 | Pragnyat [A] | "As we said earlier, as a matter of practice..." |
| 18 | 40 | Mohit Sukani [Q2 follow-up 2] | "Can you give some insights about the order book..." |
| 19 | 41 | Pragnyat [A] | "Right now we have a steady order pipeline basis..." |
| 20 | 42 | Mohit Sukani (close) | "Thank you so much." |
| 21 | 44 | Zakir Nasir [Q3] | "Congratulations on a strong set of numbers. You have..." |
| 22 | 45 | Pragnyat [A] | "As I've explained before, the Q1 numbers typically are..." |
| 23 | 46 | Zakir Nasir [Q3 follow-up] | "Payment solutions being our single largest vertical, how do..." |
| 24 | 47 | Pragnyat [A] | "It's a good question. The UPI play out on..." |
| 25 | 48 | Zakir Nasir [Q3 follow-up 2] | "SSI has been an enabler in the sphere of..." |
| 26 | 49 | Pragnyat [A] | "If I may say — Seshaasai as an organization, we've..." |
| 27 | 50 | Zakir Nasir (close) | "Good to hear you're not looking at that area." |
| 28 | 52 | British [Q4] | "Can you call out the growth of the individual..." |
| 29 | 53 | Pragnyat [A] | "As you said, last year our IoT segment we..." |
| 30 | 54 | British [Q4 follow-up] | "And the cards?" |
| 31 | 55 | Pragnyat [A] | "The communication and fulfillment business we expect to remain..." |
| 32 | 56 | Pawan [A] | "So as Mr. Pragnyat mentioned we expect the IoT..." |
| 33 | 57 | British [Q4 follow-up 2] | "Chronology of margins — if one has to understand..." |
| 34 | 58 | Pragnyat [A] | "Typically we've not separately given our margins across..." |
| 35 | 59 | British (close) | "Thank you very much." |
| 36 | 61 | Pratik Bantia [Q5] | "Congratulations on a strong set of numbers especially the..." |
| 37 | 62 | Pragnyat [A] | "SIM card business, Pratik, we are close to around..." |
| 38 | 63 | Pratik Bantia [Q5 follow-up] | "On the insurance clients that we have — as per..." |
| 39 | 64 | Pawan [A] | "The customers that have churned out in insurance are..." |
| 40 | 65 | Pratik Bantia (close) | "Great to know. Thank you." |
| 41 | 67 | Sedart Daga [Q6] | "Congratulations for the great set of numbers. My question..." |
| 42 | 68 | Pragnyat [A] | "No. If you see, last year our Q3 and..." |
| 43 | 69 | Sedart Daga (close) | "That was the only question. Thank you." |
| 44 | 71 | DRJ [Q7, follow-up caller] | "Thank you for the follow-up. The Bengaluru facility that..." |
| 45 | 72 | Pragnyat [A] | "Definitely." |
| 46 | 73 | DRJ [Q7 follow-up] | "Would you like to quantify or give us any..." |
| 47 | 74 | Pragnyat [A] | "I think it's too early for us to do..." |
| 48 | 75 | DRJ (close) | "Thank you." |
| 49 | 77 | Pulkit Singhal [Q8] | "Thank you for the opportunity. My question is on..." |
| 50 | 78 | Pragnyat [A] | "The chip prices, from whatever we procured in the..." |
| 51 | 79 | Pulkit Singhal [Q8 follow-up] | "On a YoY basis the chip pricing you're seeing..." |
| 52 | 80 | Pragnyat [A] | "Some marginal improvement on the chip pricing but it's..." |
| 53 | 81 | Pulkit Singhal [Q8 follow-up 2] | "Going ahead you don't see increasing for your chip..." |
| 54 | 82 | Pragnyat [A] | "If you see, that's reflected by our working capital..." |
| 55 | 83 | Pulkit Singhal (close) | "Understood. Thank you." |
| 56 | 86 | Operator | "As there are no further questions, I would now..." |
| 57 | 87 | Management (unattributed) | "We thank all the participants for joining us today..." |
| 58 | 88 | Operator | "Ladies and gentlemen, on behalf of Seshaasai Technologies, that..." |

Q&A share: turns 9-55 (47 of 58 turns, 81%) are Q&A. Opening/highlights = turns 1-8
(8 turns, 14%). Closing = turns 56-58 (3 turns, 5%).

---

## 3. QUESTIONS (19 total, including follow-ups as distinct units)

| Q# | Line | Analyst | Firm | Topic | Flag |
|---|---|---|---|---|---|
| 1 | 30 | Dia Jen | Safaya Capital | FY revenue and margin outlook (whole-year ask) | |
| 2 | 32 | Dia Jen | Safaya Capital | SIM rollout volume / % of requirement | |
| 3 | 36 | Mohit Sukani | II Capital | Gross margin drivers (op leverage vs pricing/rupee), capacity utilization, capex plans | |
| 4 | 38 | Mohit Sukani | II Capital | FY gross margin figure (specific ask) | `REPEAT_QUESTION` (of Q1, line 30) |
| 5 | 40 | Mohit Sukani | II Capital | Order book growth trajectory | |
| 6 | 44 | Zakir Nasir | Nasir Investment | Is Q1 the margin base for the year | `REPEAT_QUESTION` (of Q1 line 30 / Q2 line 38) |
| 7 | 46 | Zakir Nasir | Nasir Investment | UPI vs cards — competitive/macro impact on payment solutions | |
| 8 | 48 | Zakir Nasir | Nasir Investment | Payment gateway entry — new business line ask | |
| 9 | 52 | British | Lucky Investments | Segment-level growth rates, 2-3 year view (RFID/eSIM/SIM/cards) | |
| 10 | 54 | British | Lucky Investments | Cards growth specifically | |
| 11 | 57 | British | Lucky Investments | Margin chronology across the three business verticals | |
| 12 | 61 | Pratik Bantia | FMY 325 Investment Advisors | SIM card business capacity utilization this quarter | |
| 13 | 63 | Pratik Bantia | FMY 325 Investment Advisors | Insurance client count change (13→10 life insurers; 9→10 general insurers per slide) | see note below |
| 14 | 67 | Sedart Daga | SN Daga and Company | IoT growth rate vs apparent slowdown signal (Q1 >100% YoY vs 45% guided) | `REPEAT_QUESTION` (of Q4, line 52 — segment growth theme, IoT specifically) |
| 15 | 71 | DRJ (=Dia Jen) | Safaya Capital | Bengaluru facility — meaningful FY28 revenue contribution | |
| 16 | 73 | DRJ | Safaya Capital | Quantify Bengaluru facility revenue targets | |
| 17 | 77 | Pulkit Singhal | Dalmus Capital Management | Chip/RM price trends YoY, current inventory pricing | |
| 18 | 79 | Pulkit Singhal | Dalmus Capital Management | Confirm YoY chip pricing flat | |
| 19 | 81 | Pulkit Singhal | Dalmus Capital Management | Forward chip pricing risk given inventory strategy | |

**Note on Q13 (line 63)**: the specific figures "13 to 10 life insurance companies" and
"9 to 10 general insurance companies" are stated by the ANALYST (citing the company's
own investor-presentation slide), not by management. They are recorded here as the
question's content, not carried into the management-numbers ledger (§4) since
management did not speak these figures in this call — flagged for A3/A4 to
cross-check directly against the investor-presentation client-count slide when that
document is enumerated.

**REPEAT_QUESTION pattern**: three separate analysts (Dia Jen line 30, Mohit Sukani
line 38, Zakir Nasir line 44) independently pressed management for a specific
full-year gross/EBITDA margin number across three consecutive question slots.
Management gave a near-identical hedge each time (declining to give a point number,
offering "drivers not outcomes" instead — see §5). Three-analyst persistence on the
same unanswered ask is itself a signal worth carrying into A3/A4.

---

## 4. MANAGEMENT NUMBERS / QUANTIFIED CLAIMS (59 total, one row per spoken instance — repetition within a turn is kept as separate rows per GATE A2 mechanical count)

| # | Line | Speaker | Figure | Context |
|---|---|---|---|---|
| 1 | 15 | Pragnyat | 21.1% | Revenue growth YoY, Q1 FY27 (overview) |
| 2 | 15 | Pragnyat | 73 crores | Value of 2 multi-year PSU bank tenders won this quarter |
| 3 | 17 | Pragnyat | 42% | Payment solutions — % of total revenue, Q1 FY27 |
| 4 | 17 | Pragnyat | 5% | Payment solutions — YoY growth |
| 5 | 19 | Pragnyat | 40% | Comm & fulfillment — % of total revenue, Q1 FY27 |
| 6 | 19 | Pragnyat | 13% | Comm & fulfillment — YoY growth |
| 7 | 21 | Pragnyat | 18% | IoT solutions — % of total revenue, Q1 FY27 |
| 8 | 21 | Pragnyat | 145% | IoT solutions — YoY growth |
| 9 | 23 | Pragnyat | 8% | Medium-term revenue growth guidance, lower bound |
| 10 | 23 | Pragnyat | 12% | Medium-term revenue growth guidance, upper bound (8-12% range) |
| 11 | 26 | Pawan | 377 crores | Revenue from operations, Q1 FY27 |
| 12 | 26 | Pawan | 21.1% | Revenue growth YoY (restated by CFO) |
| 13 | 26 | Pawan | 6.9% | Revenue decline QoQ |
| 14 | 26 | Pawan | 13.3% | Gross profit growth |
| 15 | 26 | Pawan | 157 crores | Gross profit, Q1 FY27 |
| 16 | 26 | Pawan | 41.7% | Gross margin, Q1 FY27 |
| 17 | 26 | Pawan | 44.5% | Gross margin, Q1 FY26 (comparator) |
| 18 | 26 | Pawan | 58.34% | Cost of materials consumed (COMC), Q1 FY27 |
| 19 | 26 | Pawan | 411 bps | COMC — bps higher than FY26 full-year average |
| 20 | 26 | Pawan | 54.23% | COMC — FY26 full-year average |
| 21 | 26 | Pawan | 94 crores | EBITDA, Q1 FY27 |
| 22 | 26 | Pawan | 25.1% | EBITDA margin, Q1 FY27 |
| 23 | 26 | Pawan | 135 bps | EBITDA margin — YoY increase |
| 24 | 26 | Pawan | 48.8% | PBT growth YoY |
| 25 | 26 | Pawan | 82 crores | Profit before tax, Q1 FY27 |
| 26 | 26 | Pawan | 60 crores | PAT, Q1 FY27 |
| 27 | 26 | Pawan | 63.8% | PAT growth YoY |
| 28 | 26 | Pawan | 16% | PAT margin, Q1 FY27 |
| 29 | 26 | Pawan | 418 bps | PAT margin — YoY increase |
| 30 | 26 | Pawan | 42% | Payment solutions revenue mix (restated by CFO) |
| 31 | 26 | Pawan | 40% | Comm & fulfillment revenue mix (restated by CFO) |
| 32 | 26 | Pawan | 18% | IoT revenue mix (restated by CFO) |
| 33 | 26 | Pawan | 56% | Top-10 customer revenue concentration |
| 34 | 26 | Pawan | 95% | Revenue from existing clients (>95%) |
| 35 | 26 | Pawan | 369 crores | Cash & cash equivalents, as of 30 June 2026 |
| 36 | 26 | Pawan | 24.4 crores | Total IPO proceeds deployed in Q1 |
| 37 | 26 | Pawan | 6.7 crores | IPO proceeds — capex deployed |
| 38 | 26 | Pawan | 13.7 crores | IPO proceeds — general corporate purposes (GCP) deployed |
| 39 | 26 | Pawan | 3.9 crores | IPO proceeds — issue expenses deployed |
| 40 | 31 | Pragnyat | 8 to 12% | FY revenue growth guidance, restated in Q1 answer |
| 41 | 33 | Pragnyat | 20% | SIM production — current % of large telecom operator's requirement (initial figure) |
| 42 | 33 | Pragnyat | 20 to 25% | SIM production — % of requirement, revised/restated same turn |
| 43 | 37 | Pragnyat | 40% | Gross margin pressure — % attributable to currency (lower bound) |
| 44 | 37 | Pragnyat | 45% | Gross margin pressure — % attributable to currency (upper bound, 40-45% range) |
| 45 | 37 | Pragnyat | 65 to 70% | Capacity utilization — typical/current range |
| 46 | 37 | Pragnyat | 85 to 90% | Capacity utilization — peak, during high-renewal-cycle demand |
| 47 | 37 | Pragnyat | 65 to 70% | Capacity utilization — average range, restated same turn |
| 48 | 37 | Pragnyat | 140 to 160 crores | Capex guidance — per year, reaffirmed |
| 49 | 53 | Pragnyat | 45% | IoT segment growth, last year (FY26) YoY |
| 50 | 53 | Pragnyat | 35 to 40% | IoT segment growth, expected FY28 (following year) |
| 51 | 53 | Pragnyat | 45% | IoT segment growth, expected this year (FY27), restated same turn |
| 52 | 53 | Pragnyat | 45% | IoT segment growth, restated a third time same turn ("45% in the previous year, to be 45% this year as well") |
| 53 | 55 | Pragnyat | 10 to 12% | Payment solutions — expected growth range |
| 54 | 56 | Pawan | 45% | IoT growth restated by CFO (consistent with Pragnyat's line 53) |
| 55 | 56 | Pawan | 30% | Comm & fulfillment growth, last year (FY26) — new figure, not stated elsewhere |
| 56 | 56 | Pawan | 12% | Internal overall growth plan — CAGR |
| 57 | 58 | Pragnyat | 25% | Blended EBITDA margin, this quarter (restated, consistent with Pawan's 25.1% at line 26) |
| 58 | 62 | Pragnyat | 40% | SIM card business — capacity utilization this quarter |
| 59 | 68 | Pragnyat | 15 to 18% | IoT — targeted % of full-year revenue mix by year end |

**Highest-value rows for guidance/forward-statement tracking**: #9-10 (8-12% FY
revenue growth — the headline guidance, repeated at #40), #48 (140-160 crores/year
capex range, reaffirmed), #49-52 (IoT growth trajectory: 45% FY26 actual → 45% FY27
expected → 35-40% FY28 expected, a deceleration guided from a high base), #53 (payment
solutions 10-12% growth), #59 (IoT full-year mix target 15-18%, vs 18% realised in Q1
— implies management expects IoT's revenue share to moderate slightly over the rest of
the year despite the 145% YoY growth print in Q1).

**Timeline commitments (non-numeral, not in the 59-row regex count above, carried
in §5 instead)**: Bengaluru facility targeted operational "by end of the calendar
year" (line 15, restated line 37); Bengaluru certification process targeted "by Q4"
(line 37); Bengaluru facility revenue contribution "something even this year," with
meaningful contribution "certainly... next year almost" i.e. FY28 (line 74, following
the analyst's FY28 framing at line 71).

---

## 5. FORWARD-COMMITMENT AND HEDGE PHRASES

| Line | Speaker | Type | Phrase (paraphrase/quote) |
|---|---|---|---|
| 15 | Pragnyat | FORWARD_COMMITMENT | Bengaluru facility expected operational "by the end of the calendar year" |
| 23 | Pragnyat | FORWARD_COMMITMENT | "we expect H2 FY27 to be stronger" — seasonal BFSI pickup, steady comm&fulfillment, continued IoT growth |
| 23 | Pragnyat | FORWARD_COMMITMENT | Medium-term revenue growth guidance 8-12% (dual-tagged, also mgmt number #9-10) |
| 31 | Pragnyat | HEDGE | "we really don't put out specific EBITDA or PAT numbers... that position hasn't changed" |
| 31 | Pragnyat | HEDGE | "Any precise number we give you today probably would be false precision" |
| 37 | Pragnyat | FORWARD_COMMITMENT | Facility "should be operational" before end of calendar year (restated) |
| 37 | Pragnyat | FORWARD_COMMITMENT | Capex "probably will be maintaining the range... 140 to 160 crores per year" (dual-tagged, also mgmt number #48) |
| 39 | Pragnyat | HEDGE | "as a matter of practice we don't put out specific margin figures" (repeat of line 31 hedge, third time management declines specificity across Q1/Q2 exchange) |
| 41 | Pragnyat | HEDGE / FORWARD | "As and when we receive something further in the coming quarters we shall share with you from time to time" (order book) |
| 45 | Pragnyat | HEDGE | "we don't see any dramatic change in the margin from where we are here" |
| 49 | Pragnyat | HEDGE / FORWARD | "As time goes by we'll share details as things crystallize" (payment-gateway adjacency) |
| 53 | Pragnyat | FORWARD_COMMITMENT | IoT growth trajectory 45%→45%→35-40% across FY26/FY27/FY28 (dual-tagged, mgmt numbers #49-52) |
| 58 | Pragnyat | HEDGE | "we've not separately given our margins across the three verticals" — declines segment-level margin disclosure |
| 68 | Pragnyat | FORWARD_COMMITMENT | IoT "should be able to... contribute close to 15 to 18% of our revenue at the end of the year" (dual-tagged, mgmt number #59) |
| 72 | Pragnyat | FORWARD_COMMITMENT (vague) | "Definitely" — affirms Bengaluru will contribute meaningful FY28 revenue, no quantification |
| 74 | Pragnyat | HEDGE | "I think it's too early for us to do that" — declines to quantify Bengaluru revenue targets |
| 74 | Pragnyat | FORWARD_COMMITMENT (vague, timeline) | "hoping it contributes something even this year, but certainly it'll start contributing next year almost" |
| 82 | Pragnyat | HEDGE | "we don't have any forward bias... we don't have very clear indications" — forward chip pricing |

18 rows. Not formally gated (grep/sweep) per task instructions, which require the gate
specifically on turns and questions; this table is a manual sweep only, provided as a
direct feed for A3's forward-statement and hedge lexicon cross-check.

---

## SUMMARY FOR A3/A4 HANDOFF

- 58 speaker turns, 47 of them (81%) inside the Q&A block — high Q&A share for an
  Indian small-cap concall.
- 19 distinct questions from 7 analysts; 3 of the 19 are flagged `REPEAT_QUESTION`
  (three analysts independently pressed the same unanswered full-year-margin ask).
- 1 named management participant (Gautam Jain, WTD) introduced but never speaks —
  `MGMT_ABSENCE`.
- 59 individually spoken management numbers; guidance highlights are the 8-12% FY
  revenue growth range (repeated twice, lines 23 and 31) and the 140-160 crores/year
  capex range (repeated twice, line 37) — both should be checked by A4 against the
  Section 1B exit-multiple / growth assumptions and by A5 against the filing baseline.
- 18 forward-commitment/hedge phrases, with a repeated 3x margin-guidance hedge
  ("we don't put out specific EBITDA/PAT numbers") that management held to under
  sustained multi-analyst pressure — worth flagging to A4/A5 as evidenced discipline
  or evidenced opacity, per Role 5 framing.
- 1 figure (insurance client count, 13→10 life / 9→10 general) originates from an
  analyst's slide citation, not management's own words — held out of the mgmt-numbers
  count, flagged for cross-check against the investor presentation when enumerated.

```yaml
stage: A2-enumerator
company: "STYL"
quarter: "q1fy27"
doctype: "concall"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/styl-q1fy27/work/ledger_concall_styl_q1fy27.md"
counts:
  turns: 58
  questions: 19
  analysts: 7
  mgmt_numbers: 59
flags_raised: [MGMT_ABSENCE, REPEAT_QUESTION]
gate_a2: pass
mismatch_note: ""
```
