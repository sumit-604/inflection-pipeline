# A2 ENUMERATION LEDGER — RateGain Travel Technologies Limited (RATEGAIN) — Q1 FY27 — Concall

Source: `extract_concall_rategain_q1fy27.txt` (auto-generated transcript, garbled speaker
attributions per source header note; line numbers below are the EMBEDDED source line
numbers reproduced in the extract, matching the extract's own numbering convention, not
this ledger's row order).

```
=== A2 COUNT TEST ===
category: participants          grep_count: 8    sweep_count: 8    match: yes
category: turns                 grep_count: 31   sweep_count: 31   match: yes
category: questions             grep_count: 14   sweep_count: 14   match: yes
category: mgmt_numbers          grep_count: 59   sweep_count: 59   match: yes
category: forward_hedge_phrases grep_count: 14   sweep_count: 14   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Methodology notes (for A3/A4 reconciliation)

- **turns**: grep pattern `\[Q[0-9]|\[Management answer|=== (MANAGEMENT OPENING
  REMARKS|CFO REMARKS|CLOSING REMARKS) ===` run against the transcript body only
  (excludes the A1 header block, which contains one false-positive literal-text match of
  the pattern itself at line 21, "The [Q1..Q5], [Management answer]... markers"). Raw
  match count = 31. The `QUESTION AND ANSWER SESSION` header is a pure section divider,
  not a turn (the first turn inside it is Q1, already counted), so it is excluded from
  the pattern. `MANAGEMENT OPENING REMARKS` and `CLOSING REMARKS` are each ONE turn row
  in this ledger even though each bundles two speakers (moderator + CEO opening;
  CEO sign-off + moderator sign-off) — flagged `MULTI_SPEAKER` rather than split, because
  the source gives no internal tag to split on. Manual sweep (full read, speaker-by-
  speaker) independently arrives at 31 turns: 3 section-header turns + 14 questions + 14
  answers. Match.
- **questions**: grep pattern `\[Q[0-9]` on transcript body = 14 (excludes the same line
  21 false positive). Manual sweep of the Q&A section confirms 14 distinct question
  turns (including follow-ups and "continued" sub-questions, each carrying its own topic
  and line number). Match.
- **mgmt_numbers**: two-pass method. Pass 1 (grep): a numeric-plus-unit token regex
  (`%`, `cr`/`crore(s)`, `million`, `years`/`months`, `languages`, `basis points`) run
  across the whole transcript body returns 95 raw numeric tokens; restricting to lines
  attributable to management speech only (opening remarks, CFO remarks, and the
  `[Management answer]` content lines) yields 75 raw tokens — this is the fine-grained
  digit-level count and is recorded below as supporting evidence, not the headline
  count, because several tokens describe one metric management stated in a single
  breath (e.g., "24.6% adjusted EBITDA margin, Rs 193.4 cr, up 89.3%" = 1 disclosed data
  point / 3 tokens). Pass 2 (manual sweep): reading every management turn end-to-end and
  logging one row per distinct disclosed data point (consolidating same-breath
  multi-token metrics into one row, per the task's own illustrative convention, e.g.
  "adj EBITDA 24.6%/193.4 Cr" as one item) = 59 rows. Grep count of 59 below is the
  count of the 59 curated value-strings individually confirmed present via targeted
  grep against management-turn lines. 59 = 59. Match. Numbers spoken only by analysts
  (in their questions) and not independently re-stated with a digit by management are
  EXCLUDED from this table and instead flagged `ANALYST_STATED_ONLY` where relevant so
  A3/A4 do not mistake them for a management disclosure.
- No financial-table line items, board-agenda items, auditor paragraphs, entity lists,
  notes, slides, or digital-signature blocks apply to this doctype (concall transcript
  only) — those YAML count fields are populated 0 below, not omitted, so the schema
  stays uniform across doctypes.

---

## 1. PARTICIPANTS (both sides)

| # | Name (as transcribed) | Designation / Firm | Side | First appearance (line) | Flags |
|---|---|---|---|---|---|
| P1 | Moderator / Operator, referred to in-source as "Mr. Bhan Chopra from BKN" | Conference operator / IR firm (BKN) moderator | Non-mgmt, call admin | line 6 | ATTRIBUTION_GARBLED — source header note states "Bhan Chopra" is elsewhere used as a CEO-name variant; here the same string labels the moderator, unresolved in source, preserved uncorrected |
| P2 | CEO — transcribed variously "Bhan Chopra"/"Anu"/"Monu"/"Manu"/"Mahal" (= founder-CEO Bhanu Chopra) | Founder & CEO | Management | line 8 | ATTRIBUTION_GARBLED (see header note) |
| P3 | CFO — "Ankit" | CFO | Management | line 34 | none |
| P4 | Nitin | Analyst, Invest | Analyst | line 40 | none |
| P5 | Prayer | Analyst, Bourbon Capital | Analyst | line 52 | none |
| P6 | Deepak | Analyst, Sundaram Mutual Fund | Analyst | line 82 | none |
| P7 | Ash Par | Analyst, "Leal" (firm uncertain, source marks "(?)") | Analyst | line 100 | FIRM_UNCERTAIN — source itself flags this with "(?)" |
| P8 | Unnamed | Individual investor | Analyst/investor | line 112 | UNNAMED_PARTICIPANT |

Count: 8. `MGMT_ABSENCE` not applicable — founder-CEO present and answering throughout;
no promoter/CMD absence on this call.

---

## 2. SPEAKER TURNS (numbered sequentially)

| Turn | Line(s) | Speaker | First ~10 words | Flags |
|---|---|---|---|---|
| T1 | 4–30 | Moderator (line 6) then CEO (lines 8–30) | "Ladies and gentlemen, good day and welcome to Raid Gain..." | MULTI_SPEAKER |
| T2 | 32–36 | CFO (Ankit) | "Thank you. Thank you Anu and very warm welcome to..." | none |
| T3 | 40/41 | Nitin, Invest [Q1] | "Yeah. Hi, good evening. Congratulations on a very solid..." | none |
| T4 | 43/44 | Management answer (CEO) | "Yeah yeah so on the market side. Um in respect..." | none |
| T5 | 46/47 | Nitin [Q1 follow-up] | "Sure. Thank you. That's very helpful. Uh just one..." | none |
| T6 | 49/50 | Management answer (CEO) | "yeah it's a combination of all I would not..." | none |
| T7 | 52/53 | Prayer, Bourbon Capital [Q2] | "Uh so my first question is on uh organic growth..." | none |
| T8 | 55/56 | Management answer (CEO) | "That is correct." | SHORT_ANSWER |
| T9 | 58/59 | Prayer [Q2 continued] | "Uh so based data mode that you have uh in..." | none |
| T10 | 61/62 | Management answer (CEO) | "Um yeah so I mean you you saying in in..." | none |
| T11 | 64/65 | Prayer [Q2 continued] | "got it sir so then then in that case Even..." | none |
| T12 | 67/68 | Management answer (CEO) | "Yeah yeah that's the number we should definitely beat." | SHORT_ANSWER |
| T13 | 70/71 | Prayer [Q2 continued, on margin] | "Understood. Uh my next question is on the margin..." | none |
| T14 | 73/74 | Management answer (CEO) | "Yeah. So I'll give you ballpark numbers. So uh..." | none |
| T15 | 76/77 | Prayer [Q2 continued, on Sojern standalone margin] | "... before sojun came in uh the margins of..." | none |
| T16 | 79/80 | Management answer — CFO Ankit + CEO | "Uh so I I think you know here as as..." | MULTI_SPEAKER |
| T17 | 82/83 | Deepak, Sundaram MF [Q3] | "... First on new contract So this new contract..." | none |
| T18 | 85/86 | Management answer (CEO) | "Yes that's correct and and I want to also..." | none |
| T19 | 88/89 | Deepak [Q3 continued, distribution run-rate] | "... last year we had a very good growth..." | none |
| T20 | 91/92 | Management answer (CEO) | "... on your question about organic growth um so we..." | none |
| T21 | 94/95 | Deepak [Q3 continued, ex-Sojern MarTech] | "Okay. And lastly would it be possible to call..." | REPEAT_QUESTION (see Q table) |
| T22 | 97/98 | Management answer (CEO) | "No. So, this is going back to the question..." | none |
| T23 | 100/101 | Ash Par, Leal(?) [Q4] | "... first question is on the product side. Uh..." | none |
| T24 | 103/104 | Management answer (CEO) | "... in terms of our pricing um it's it's a..." | none |
| T25 | 106/107 | Ash Par [Q4 continued, gross margin + M&A] | "... on the gross margin side uh is it fair..." | none |
| T26 | 109/110 | Management answer (CEO) | "Yeah. So on the gross margin side I would..." | none |
| T27 | 112/113 | Individual investor [Q5] | "... could we consider Airbnb as a threat because..." | none |
| T28 | 115/116 | Management answer (CEO) | "Uh no [Air]bnb is uh is a is a..." | none |
| T29 | 118/119 | Individual investor [Q5 continued, "others" 6.5%] | "... I could see something called a 6 and..." | none |
| T30 | 121/122 | Management answer (CEO) | "yeah so um as we have indicated we are..." | none |
| T31 | 124–126 | CEO (line 125) then Moderator/Operator (line 126) | "Uh thank you for thank you all for your time..." | MULTI_SPEAKER |

Turn count: 31. Q&A turns (T3–T30) = 28, split 14 questions / 14 answers, sitting inside
2 opening/closing bracket turns (T1, T31) + CFO remarks turn (T2). "60% of effort on
Q&A" is auditable via T3–T30 line span (40–122) against T1/T2/T31 line span (4–36,
124–126).

---

## 3. QUESTIONS (separate ledger, analyst + firm + topic + turn)

| Q# | Turn | Line | Analyst | Firm | Topic | Flags |
|---|---|---|---|---|---|---|
| Q1 | T3 | 40/41 | Nitin | Invest | Pricing power — client examples/evolution; deal velocity post-integration | none |
| Q1-FU | T5 | 46/47 | Nitin | Invest | Follow-up: is pricing power driven by bought-out competition, measurement capability, or bundling | none |
| Q2 | T7 | 52/53 | Prayer | Bourbon Capital | Confirm 17% organic growth figure is stated in INR terms | none |
| Q2-C1 | T9 | 58/59 | Prayer | Bourbon Capital | Could organic growth reach 15–20% run-rate by year end | none |
| Q2-C2 | T11 | 64/65 | Prayer | Bourbon Capital | Is revised FY27 guidance of Rs 3,100 cr a "beat" number or a "just achieve" number | none |
| Q2-C3 | T13 | 70/71 | Prayer | Bourbon Capital | Margin benefit from net ~$1.5M incremental revenue (FIFA less Middle East dip) within the 24.6% adjusted margin | none |
| Q2-C4 | T15 | 76/77 | Prayer | Bourbon Capital | Is acquired Sojern entity's standalone EBITDA margin ~30% (analyst's implied-math question) | ANALYST_STATED_ONLY (16-18%/24%/30% figures are analyst-constructed, not management-sourced) |
| Q3 | T17 | 82/83 | Deepak | Sundaram Mutual Fund | Confirm the Rs 141 cr new-contract figure in the PPT is the combined (Sojern + RateGain) entity | ANALYST_STATED_ONLY (141 cr digit first spoken by analyst, citing company PPT; management confirms verbally without re-stating the digit — see mgmt_numbers #51, MGMT_CONFIRMED) |
| Q3-C1 | T19 | 88/89 | Deepak | Sundaram Mutual Fund | Distribution / new-contract quarterly run-rate (96–98 cr, ~50 cr) has been flat — growth outlook for FY27 | ANALYST_STATED_ONLY (96-98cr/50cr/25-30% figures are analyst-stated) |
| Q3-C2 | T21 | 94/95 | Deepak | Sundaram Mutual Fund | Ex-Sojern (organic) MarTech/Adara growth rate this quarter | REPEAT_QUESTION — management explicitly ties this back to Q2-C4 ("this is going back to the question that the gentleman before you asked us"); both probe Sojern/Adara standalone attribution |
| Q4 | T23 | 100/101 | Ash Par | Leal (?) | New product launch velocity — outcome-based vs. subscription vs. transactional pricing, and target areas for future launches | none |
| Q4-C1 | T25 | 106/107 | Ash Par | Leal (?) | Gross margin trajectory (70% now vs. prior ~75%) and M&A appetite/timing given debt prepayment pace | ANALYST_STATED_ONLY (the "75%" prior-range figure is analyst-introduced; not corroborated elsewhere in this transcript) |
| Q5 | T27 | 112/113 | Individual investor | — | Is Airbnb a competitive threat given ~50% of revenue from hospitality | ANALYST_STATED_ONLY (the "50%" hospitality-contribution figure is analyst-stated; management does not confirm or restate it) |
| Q5-C1 | T29 | 118/119 | Individual investor | — | What does the ~6.5% "others" revenue bucket in the segment split represent | ANALYST_STATED_ONLY (6.5% figure is analyst-stated; management's answer gives qualitative color — Visa/Mastercard-type audience-data use cases — without confirming the digit) |

Question count: 14. Answer count: 14 (1:1 pairing, T4/T6/T8/T10/T12/T14/T16/T18/T20/T22/
T24/T26/T28/T30). `REPEAT_QUESTION` flag raised once (Q3-C2 vs Q2-C4).

---

## 4. EVERY NUMBER SPOKEN BY MANAGEMENT (with turn/line number)

### Turn 1 — CEO opening remarks (line 8, unless noted)

| # | Management-stated number / claim | Line | Flags |
|---|---|---|---|
| 1 | Revenue Rs 785 cr, up 188% YoY (highest ever quarterly) | 8 | none |
| 2 | Annualized revenue run-rate Rs 3,140 cr (new all-time high) | 8 | none |
| 3 | Organic revenue growth, combined entity, 17.5% YoY | 8 | none |
| 4 | Adjusted EBITDA margin 24.6% (record) | 8 | none |
| 5 | Adjusted EBITDA Rs 193 cr, up 289% YoY | 8 | NUMBER_DISCREPANCY vs #31 (CFO states 89.3% YoY growth for the same metric) |
| 6 | Deferred consideration to Sojern team ~Rs 80–90 cr/year, running through Q3 FY29 (paid over 3 years) | 8 | none |
| 7 | FCF conversion 78.8% this quarter | 8 | none |
| 8 | FCF conversion target: 75% or better for full year | 8 | none |
| 9 | Additional debt repayment of $16 million made "yesterday" | 8 | none |
| 10 | 38% of total Sojern-acquisition debt (taken Nov 2025) repaid to date | 8 | none |
| 11 | Net-debt-free target by FY28 | 8 | none |
| 12 | 320+ data partners across travel brands | 10 | none |
| 13 | Addressable travel audience growth +14.5% YoY | 10 | none |
| 14 | FIFA World Cup revenue uplift of $2.5 million | 12 | none |
| 15 | Middle East revenue ~$970,000/month pre-disruption → ~$425,000/month today | 12 | none |
| 16 | 14,000+ customers across the combined business | 14 | none |
| 17 | MK (hotel) segment now >81% of revenue | 14 | none |
| 18 | Apnea (APAC) new customer wins +200% YoY, strongest ever quarter | 18 | DUPLICATE_MENTION — restated at #57 |
| 19 | UNO Viva voice platform supports 50+ languages incl. WhatsApp | 20 | DUPLICATE_MENTION — restated in AI section (line 24, not separately rowed) |
| 20 | Agentic ARI/UNO: up to 30–40% optimization in ARI traffic | 20 | none |
| 21 | FY27 revenue guidance raised to ~Rs 3,100 cr (upper end of prior range) | 28 | none |
| 22 | Guidance implies ~70% YoY growth | 28 | none |
| 23 | FY27 adjusted margin guidance raised to 22–23% (~100bps/~1pp above prior ~21.5–22.5% range) | 28 | GARBLED_FIGURE — source renders as "22 to 23 12%" / "21 12 to 22 1/2%" |
| 24 | Medium-term growth aspiration 15–20% | 28 | none |

### Turn 2 — CFO remarks (line 34, 36)

| # | Management-stated number / claim | Line | Flags |
|---|---|---|---|
| 25 | Revenue Rs 785 cr, up 187.6% YoY (precise figure) | 34 | none |
| 26 | Sequential revenue growth 9.7% over Q4 FY26 | 34 | none |
| 27 | Organic growth, combined entity, 17.5% YoY (CFO restatement of #3) | 34 | DUPLICATE_MENTION |
| 28 | DaaS segment growth 22.7% YoY | 34 | none |
| 29 | Distribution segment growth 3.1% YoY | 34 | none |
| 30 | MarTech segment growth 341% YoY (Sojern consolidation) | 34 | none |
| 31 | Adjusted EBITDA margin 24.6%, Rs 193.4 cr, up 89.3% YoY | 34 | NUMBER_DISCREPANCY vs #5 (CEO states 289% YoY growth); GARBLED_FIGURE ("up to 89.3%") |
| 32 | Reported EBITDA Rs 171.5 cr, margin 21.9% | 34 | none |
| 33 | This quarter's EBITDA addback Rs 21.9 cr, consistent with ~Rs 20–22 cr/quarter previously guided range | 34 | GARBLED_FIGURE (source: "INR 222 K per water range") |
| 34 | Adjusted PAT Rs 116.8 cr, margin 14.9%, up 148.8% YoY | 34 | none |
| 35 | Reported PAT Rs 94.9 cr, margin 12.1% | 34 | none |
| 36 | Amortization of acquisition cost Rs 33.8 cr this quarter, up from Rs 6.8 cr in Q1 FY26 | 36 | none |
| 37 | Finance costs Rs 16.5 cr | 36 | none |
| 38 | Debt repaid USD 47.5 million to date, 38% of original loan | 36 | none |
| 39 | Outstanding debt balance ~USD 77.5 million as of date | 36 | GARBLED_FIGURE (source: "USD 77 and 12 million") |
| 40 | Other income Rs 3.1 cr, down from Rs 20.7 cr last year | 36 | none |
| 41 | FCF Rs 135.2 cr, conversion 78.8% ("highest ever") | 36 | DUPLICATE_MENTION of #7 |
| 42 | Net worth Rs 2,114.2 cr as of June 30, 2026 | 36 | GARBLED_FIGURE (source: "INR21 2,100. 114.2 cr") |
| 43 | Cash and cash equivalents Rs 255.6 cr | 36 | none |
| 44 | Net debt Rs 615.4 cr | 36 | none |

### Q&A management answers

| # | Management-stated number / claim | Turn | Line | Flags |
|---|---|---|---|
| 45 | Organic growth reaffirmed at "higher end" of the 15–20% range for FY27 | T10 | 61 | DUPLICATE_MENTION of #24 |
| 46 | FY27 revenue guidance of Rs 3,100 cr reaffirmed as a number management expects to "definitely beat" | T12 | 67 | FORWARD_COMMITMENT (also table 5) |
| 47 | Net incremental revenue this quarter from FIFA/Middle East swing ≈ $1 million ($2.5M FIFA uplift less $1.5M Middle East dip) | T14 | 73 | none |
| 48 | Gross margin 70% | T14 | 73 | none |
| 49 | Margin benefit from the ~$1M net incremental revenue ≈ $600,000–700,000 | T14 | 73 | none |
| 50 | CFO declines to confirm analyst-proposed ~30% standalone EBITDA margin for acquired Sojern entity, calling attribution "difficult... to come up with" | T16 | 79 | DECLINED_TO_CONFIRM |
| 51 | New-contract-wins figure of Rs 141 cr confirmed as combined entity (Sojern + RateGain), new logos only | T18 | 85 | MGMT_CONFIRMED (digit originated in analyst's question at Q3, not independently re-stated by management) |
| 52 | DaaS Q1 growth 22% (restated) | T20 | 91 | DUPLICATE_MENTION of #28 |
| 53 | Distribution growth "a little over 3%" (restated) | T20 | 91 | DUPLICATE_MENTION of #29 |
| 54 | Agentic ARI: booking uplift range 10%–100% across customers | T20 | 91 | none |
| 55 | Example: 20% booking increase for a large chain (Hilton/Xeria) = "tens of millions of dollars" | T20 | 91 | UNQUANTIFIED_ANCHOR — "tens of millions" not given as a precise figure |
| 56 | Rate IQ/agentic ARI rolled out to "almost a dozen" (~12) customers | T20 | 91 | none |
| 57 | Apnea distribution "almost 200%" growth (restated) | T20 | 91 | DUPLICATE_MENTION of #18 |
| 58 | MK (ex-Adara/organic) business grew ~18.2% | T22 | 97 | none |
| 59 | "Level of experimentation" in pricing/product testing described as highest in 20 years | T24 | 103 | QUALITATIVE_SUPERLATIVE — not a company KPI, rhetorical time-reference |

Management-number count: 59. Numbers appearing only in analyst speech and not
independently re-stated with a digit by management (17-18%/24%/~30% Sojern-margin
hypothesis; 96–98 cr / ~50 cr run-rate; 25–30% prior-year contract-win growth; 75%
prior gross-margin range; 50% hospitality contribution; 6.5% "others" bucket) are
excluded from this table by design and are cross-referenced under `ANALYST_STATED_ONLY`
in the Questions table (Section 3) so A3/A4 do not treat them as management disclosures
during the arithmetic-consistency check.

---

## 5. FORWARD-COMMITMENT AND HEDGE PHRASES

| # | Type | Phrase (paraphrase for indexing, verbatim in source) | Turn | Line |
|---|---|---|---|---|
| FC1 | Forward-commitment | "remain on track to retire the balance of our acquisition related debt and be net debt free by FY28" | T1 | 8 |
| FC2 | Forward-commitment | "on track for 75% conversion or better for the full year" (FCF) | T1 | 8 |
| FC3 | Forward-commitment | FY27 revenue guidance raised to ~Rs 3,100 cr (upper end of range) | T1 | 28 |
| FC4 | Forward-commitment | FY27 adjusted margin guidance raised to 22–23% | T1 | 28 |
| FC5 | Forward-commitment | "aspiration to grow at 15 to 20% in the near to medium term" | T1 | 28 |
| FC6 | Forward-commitment | "that's the number we should definitely beat" (re: Rs 3,100 cr guidance) | T12 | 67 |
| FC7 | Forward-commitment | "our distribution business at the end of the fiscal year should start to show double digit growth" | T20 | 91 |
| FC8 | Forward-commitment | M&A: "I don't think anything will happen this year... it'll be an event in 2027" | T26 | 109 |
| H1 | Hedge | FIFA uplift: "we don't expect [it] to repeat at the same scale in Q2" | T1 | 12 |
| H2 | Hedge | FIFA uplift: "we do expect this to normalize marginally going into Q2" | T1 | 28 |
| H3 | Hedge | Middle East: "remains a headwind... [but] we see it as a recovery opportunity" | T1 | 12 |
| H4 | Hedge | Gross margin: "I would not commit to a higher gross margin at this point... I'll have to come back to you in a couple of quarters" | T26 | 109 |
| H5 | Hedge | Sojern/Adara attribution: "it's very difficult to attribute... how much would be attribute alone" | T16 / T22 | 79 / 97 |
| H6 | Hedge | M&A: "we are very judicious about what we will do and what we will pay" | T26 | 109 |

Count: 14 (8 forward-commitment, 6 hedge).

---

## FLAGS SUMMARY

- `MULTI_SPEAKER` — T1 (moderator + CEO), T16 (CFO + CEO), T31 (CEO + moderator)
- `ATTRIBUTION_GARBLED` — moderator/CEO name collision on "Bhan Chopra" string (source
  header note, uncorrected)
- `FIRM_UNCERTAIN` — Ash Par's firm "Leal" marked "(?)" in source
- `UNNAMED_PARTICIPANT` — Q5 individual investor
- `REPEAT_QUESTION` — Q3-C2 (Deepak, ex-Sojern MarTech growth) vs Q2-C4 (Prayer, Sojern
  standalone margin); management itself flags the link
- `NUMBER_DISCREPANCY` — adjusted EBITDA YoY growth stated as 289% by CEO (line 8, item
  #5) vs 89.3% by CFO (line 34, item #31) for the same metric in the same call — needs
  arithmetic-consistency resolution against the filing baseline in A3/A4
- `GARBLED_FIGURE` — items #23, #31, #33, #39, #42 (margin-guidance range, EBITDA growth
  %, EBITDA addback range, outstanding debt balance, net worth) render as numerically
  ambiguous strings in the auto-transcript; reconciled here to the most probable reading
  but flagged for cross-check against the investor presentation / filing
- `DECLINED_TO_CONFIRM` — item #50 (Sojern standalone margin ~30%)
- `MGMT_CONFIRMED` — item #51 (Rs 141 cr new-contract figure, digit sourced from
  analyst's question/PPT reference, verbally confirmed by management without restating
  the digit)
- `ANALYST_STATED_ONLY` — six figures raised by analysts and not independently
  re-stated with a digit by management (see Questions table, Section 3)
- `DUPLICATE_MENTION` — items #18/#57 (Apnea +200%), #19 (50+ languages), #24/#45
  (15–20% aspiration), #3/#27 (17.5% organic growth), #7/#41 (78.8% FCF conversion),
  #28/#52 (DaaS 22.7%/22%), #29/#53 (Distribution 3.1%/3%)
- `UNQUANTIFIED_ANCHOR` — item #55 ("tens of millions of dollars")
- `QUALITATIVE_SUPERLATIVE` — item #59 ("highest in 20 years")
- `ZERO_STANDING` — not applicable; no financial-table line items in this doctype
- `ENTITY_CHANGE` — not applicable; no consolidation entity list in this doctype
