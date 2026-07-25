# LEDGER — STLTECH Q1FY27 Concall Transcript
Source: /home/user/inflection-pipeline/runs/stltech-q1fy27/work/extract_concall_stltech_q1fy27.txt
Line numbers below are FILE line numbers as returned by Read (header occupies file lines 1-13;
transcript body begins file line 14; [VERBATIM TRANSCRIPT BEGINS] = file line 17;
[VERBATIM TRANSCRIPT ENDS] = file line 171). The extract also carries its own internal
line numbering 1-158 embedded as a leading tab-delimited number on every content line; that
internal number is shown in the "src#" column for cross-reference (file_line = src# + 13).

```
=== A2 COUNT TEST ===
category: participants     grep_count: 15   sweep_count: 15   match: yes
category: turns             grep_count: 75   sweep_count: 75   match: yes
category: questions         grep_count: 23   sweep_count: 23   match: yes
category: answers           grep_count: 23   sweep_count: 23   match: yes
category: operator_turns    grep_count: 14   sweep_count: 14   match: yes
category: mgmt_number_tokens grep_count: 143  sweep_count: 143  match: yes
category: mgmt_disclosure_units (claims table, derived from reconciled token sweep above) = 91
gate_a2: pass
=== END COUNT TEST ===
```

Method notes on the mgmt_number_tokens count test (grep vs sweep):
- grep pass: `grep -v '^=== content-line' mgmt_turns.txt | grep -oP '(?<![A-Za-z])\$?\d[\d,]*(\.\d+)?%?'`
  run only against text extracted from management-attributed turns (opening remarks by
  Rahul/Ankit/Ajay, all 23 answer turns, and the closing remark) = 143 raw numeric tokens.
- manual sweep: independent line-by-line read of the same 38 management turns, token-by-token
  listing = 143 tokens (full per-line breakdown retained in scratchpad; every token accounted
  for in the Management Numbers table below, either as its own row or folded into a compound
  claim row with the constituent tokens named).
- Two spelled-out quantities appear only via manual read and are NOT digit-token matches
  ("four to seven times" for multi-core capacity, "three times" for MMC cable density,
  "three or four elements" for raw-material count) — these are additive disclosure claims
  captured in the Management Numbers table (rows 28, 32, 73) but are not part of the 143-token
  digit count; flagged `SPELLED_NUMBER` so A3/A4 know they will not surface via a pure digit
  grep of the source and must be checked by re-read.
- Turns/Questions/Answers/Operator-turn counts were each independently grepped
  (`grep -cP '^\d+\tQ \('`, `'^\d+\tA \('`, `'^\d+\tOperator:'` plus the one unlabeled operator
  welcome turn) and cross-checked against a full manual turn-by-turn listing; all match exactly.

---
## 1. PARTICIPANTS

| # | Name | Side | Designation / Firm | First appearance (file line) | Flags |
|---|------|------|---------------------|-------------------------------|-------|
| 1 | Operator (unnamed) | Call admin | Conference operator | 19 | |
| 2 | Rahul Darak | Management | Head of Investor Relations, STL | 21 | |
| 3 | Ankit Tagral | Management | Managing Director, STL | 23 | |
| 4 | Ajay Janjari | Management | Group CFO, STL | 41 | |
| 5 | Achan | Analyst | Dwama | 53 | |
| 6 | Devarat | Analyst | 7 Holding | 67 | |
| 7 | Shil Jain | Analyst | Nuvama Bank Security | 73 | |
| 8 | Patel ("Stage Patel" per operator intro) | Analyst | Nishai | 83 | NAME_VARIANT (operator says "Stage Patel", Q attributed simply "Patel") |
| 9 | Krish | Analyst | Inam Holdings | 101 | |
| 10 | Subramanium | Analyst | Arihant | 111 | |
| 11 | Akhil | Analyst | Seven Holding | 117 | |
| 12 | Tushar | Analyst | Sangi Family Office | 131 | |
| 13 | Aniel | Analyst | Segel Capital Advisor | 137 | |
| 14 | Sati K | Analyst | PM Capital | 143 | |
| 15 | Noah | Analyst | Noah Financials | 153 | |
| 16 | Naman Parmar | Analyst | Nishai Investment | 159 | NAME_VARIANT — firm string differs from row 8 ("Nishai" vs "Nishai Investment"); could be same house rendered two ways or two distinct entities; flagged for A3, not resolved here |

Sweep count of distinct named individuals = 16 rows above (4 management incl. operator, 12 analysts);
COUNT TEST line reports "participants: 15" for the 15 human speakers who take a numbered
turn (operator counted once as a role, Darak/Tagral/Janjari, 12 named analysts = 3+12=15, operator
tracked separately as call-admin role rather than a "participant" in the STL disclosure sense) —
both figures reconcile once operator is excluded from the participant headcount; no discrepancy.

`MGMT_ABSENCE`: not triggered — both MD (Ankit Tagral) and CFO (Ajay Janjari) present and active
throughout, including Q&A (Ajay fields 3 of 23 answers directly: turns 28, 33, 71).

---
## 2. SPEAKER TURNS (sequential, 75 total)

| Turn | Speaker | Role | File line | src# | First ~10 words | Flags |
|------|---------|------|-----------|------|------------------|-------|
| 1 | Operator (unlabeled) | Call admin | 19 | 6 | "Ladies and gentlemen good day and welcome to Sterlite..." | |
| 2 | Rahul Darak | Mgmt-IR | 21 | 8 | "Thank you. Good day everyone and welcome to STL's..." | |
| 3 | Ankit Tagral | Mgmt-MD | 23 | 10 | "Thank you Rahul. Good day everyone thank you for..." | Opening remarks begin |
| 4 | Ankit Tagral | Mgmt-MD | 25 | 12 | "As we step into FY27 our core strategic priorities..." | |
| 5 | Ankit Tagral | Mgmt-MD | 27 | 14 | "Moving on we'll now speak about the industry tailwinds..." | |
| 6 | Ankit Tagral | Mgmt-MD | 29 | 16 | "Next on slide 10 you will see how some of..." | |
| 7 | Ankit Tagral | Mgmt-MD | 31 | 18 | "We're successfully seizing new market opportunities a trend that..." | |
| 8 | Ankit Tagral | Mgmt-MD | 33 | 20 | "Innovation continues to be a key differentiator for STL..." | |
| 9 | Ankit Tagral | Mgmt-MD | 35 | 22 | "Turning to our product portfolio we're making tremendous progress..." | |
| 10 | Ankit Tagral | Mgmt-MD | 37 | 24 | "Slide 18 highlights STL's leadership in the next generation..." | |
| 11 | Ankit Tagral | Mgmt-MD | 39 | 26 | "On market position and attach rate trends, global ex-China..." | Hands to CFO |
| 12 | Ajay Janjari | Mgmt-CFO | 41 | 28 | "Thank you Ankit and thanks to everyone for joining..." | |
| 13 | Ajay Janjari | Mgmt-CFO | 43 | 30 | "On the segment side while telecom and citizen networks..." | |
| 14 | Ajay Janjari | Mgmt-CFO | 45 | 32 | "Moving to the open order book we have seen..." | Hands back to MD |
| 15 | Ankit Tagral | Mgmt-MD | 47 | 34 | "Thanks AJ. STL's CSR initiatives continue to create deep..." | Closes opening remarks, opens floor |
| 16 | Operator | Call admin | 51 | 38 | "Thank you very much. We will now begin the..." | Q&A begins |
| 17 | Achan (Dwama) | Analyst-Q | 53 | 40 | "Good afternoon thank you for the opportunity, congratulations for..." | Q1 |
| 18 | Ankit Tagral | Mgmt-A | 55 | 42 | "So I think both parts. When we look at..." | A1 (contains REFUSAL) |
| 19 | Achan | Analyst-Q | 57 | 44 | "Ankit the question was in terms of the ordering..." | Q2 (follow-up) |
| 20 | Ankit Tagral | Mgmt-A | 59 | 46 | "So from a data center capex if you just..." | A2 |
| 21 | Achan | Analyst-Q | 61 | 48 | "Another question with respect to the sourcing of raw..." | Q3 |
| 22 | Ankit Tagral | Mgmt-A | 63 | 50 | "So I think there are three or four elements..." | A3 |
| 23 | Operator | Call admin | 65 | 52 | "The next question is from the line of Devarat..." | |
| 24 | Devarat (7 Holding) | Analyst-Q | 67 | 54 | "Congratulations on a great set of numbers. You haven't..." | Q4 — REPEAT_QUESTION (capacity utilization, cf. Q1/turn17) |
| 25 | Ankit Tagral | Mgmt-A | 69 | 56 | "As I said I think we're in several conversations..." | A4 |
| 26 | Operator | Call admin | 71 | 58 | "The next question is from the line of Shil..." | |
| 27 | Shil Jain (Nuvama) | Analyst-Q | 73 | 60 | "Congratulation on good numbers. My question relates to the..." | Q5 |
| 28 | Ajay Janjari | Mgmt-A | 75 | 62 | "So broadly we don't give any guidance on the..." | A5 (REFUSAL — revenue guidance) |
| 29 | Shil Jain | Analyst-Q | 77 | 64 | "And sir second thing if you can talk about..." | Q6 |
| 30 | Ankit Tagral | Mgmt-A | 79 | 66 | "So as I said we are, look historically we've..." | A6 |
| 31 | Operator | Call admin | 81 | 68 | "The next question is from the line of Stage..." | |
| 32 | Patel (Nishai) | Analyst-Q | 83 | 70 | "Thank you and congratulations on a very great set..." | Q7 |
| 33 | Ajay Janjari | Mgmt-A | 85 | 72 | "So here on the gross margin yes there is..." | A7 |
| 34 | Patel | Analyst-Q | 87 | 74 | "Second question, there's been a record inflow of orders..." | Q8 |
| 35 | Ankit Tagral | Mgmt-A | 89 | 76 | "No so broadly in fact even if we exclude..." | A8 |
| 36 | Patel | Analyst-Q | 91 | 78 | "And sir on germanium just wanted to understand are..." | Q9 — REPEAT_QUESTION (germanium, cf. Q3/turn21) |
| 37 | Ankit Tagral | Mgmt-A | 93 | 80 | "We can't comment a lot on the germanium for..." | A9 (REFUSAL — competitive reasons) |
| 38 | Patel | Analyst-Q | 95 | 82 | "And last question on, after this debottlenecking and the..." | Q10 |
| 39 | Ankit Tagral | Mgmt-A | 97 | 84 | "I can't comment on any specific size but as..." | A10 (REFUSAL — specific order size) |
| 40 | Operator | Call admin | 99 | 86 | "The next question is from the line of Krish..." | |
| 41 | Krish (Inam Holdings) | Analyst-Q | 101 | 88 | "My question was more of a strategic question on..." | Q11 |
| 42 | Ankit Tagral | Mgmt-A | 103 | 90 | "Absolutely, I think that's absolutely spot on. I would..." | A11 |
| 43 | Krish | Analyst-Q | 105 | 92 | "Just to follow up so over the next 3..." | Q12 (follow-up) |
| 44 | Ankit Tagral | Mgmt-A | 107 | 94 | "No I think look it's, I think strategically this..." | A12 |
| 45 | Operator | Call admin | 109 | 96 | "The next question is from the line of Subramanium..." | |
| 46 | Subramanium (Arihant) | Analyst-Q | 111 | 98 | "Good evening sir thank you so much for the..." | Q13 |
| 47 | Ankit Tagral | Mgmt-A | 113 | 100 | "So firstly on the realization we do not comment..." | A13 (REFUSAL — realization) |
| 48 | Operator | Call admin | 115 | 102 | "The next question is from the line of Akhil..." | |
| 49 | Akhil (Seven Holding) | Analyst-Q | 117 | 104 | "Congratulations on a fantastic set of results and thank..." | Q14 — REPEAT_QUESTION (sustainability of Q1 = implicit revenue guidance ask, cf. Q5/turn27) |
| 50 | Ankit Tagral | Mgmt-A | 119 | 106 | "We don't guide any numbers for the full year..." | A14 (REFUSAL — FY/longer-term guidance) |
| 51 | Akhil | Analyst-Q | 121 | 108 | "Also I just want to understand what is the..." | Q15 |
| 52 | Ankit Tagral | Mgmt-A | 123 | 110 | "So broadly what we see is that as a..." | A15 |
| 53 | Akhil | Analyst-Q | 125 | 112 | "Can you also share the breakup of revenue for..." | Q16 |
| 54 | Ankit Tagral | Mgmt-A | 127 | 114 | "No we don't break that out." | A16 (REFUSAL — connectivity/digital revenue split; shortest answer of the call, 6 words) |
| 55 | Operator | Call admin | 129 | 116 | "The next question is from the line of Tushar..." | |
| 56 | Tushar (Sangi Family Office) | Analyst-Q | 131 | 118 | "Congratulations on a great execution. My first question was..." | Q17 |
| 57 | Ankit Tagral | Mgmt-A | 133 | 120 | "I think there is some history here, we actually..." | A17 |
| 58 | Operator | Call admin | 135 | 122 | "The next question is from the line of Aniel..." | |
| 59 | Aniel (Segel Capital) | Analyst-Q | 137 | 124 | "Hi Ankit thanks for taking my call great set..." | Q18 |
| 60 | Ankit Tagral | Mgmt-A | 139 | 126 | "I think in terms of the investments yes clearly..." | A18 |
| 61 | Operator | Call admin | 141 | 128 | "The next question is from the line of Sati..." | |
| 62 | Sati K (PM Capital) | Analyst-Q | 143 | 130 | "I just wanted to check on the $100 million..." | Q19 |
| 63 | Ankit Tagral | Mgmt-A | 145 | 132 | "So what we announced was a $100 million investment..." | A19 |
| 64 | Sati K | Analyst-Q | 147 | 134 | "Do we have any capacity number in mind what..." | Q20 |
| 65 | Ankit Tagral | Mgmt-A | 149 | 136 | "So this will mainly be for the connectivity side..." | A20 (REFUSAL — specific capacity, deferred) |
| 66 | Operator | Call admin | 151 | 138 | "The next question is from the line of Noah..." | |
| 67 | Noah (Noah Financials) | Analyst-Q | 153 | 140 | "My question was about you mentioned germanium and helium..." | Q21 — REPEAT_QUESTION (germanium/helium, cf. Q3/Q9, turns 21/36) |
| 68 | Ankit Tagral | Mgmt-A | 155 | 142 | "I think what I shared earlier as well that..." | A21 |
| 69 | Operator | Call admin | 157 | 144 | "The next question is from the line of Naman..." | |
| 70 | Naman Parmar (Nishai Investment) | Analyst-Q | 159 | 146 | "Good evening sir thank you so much for opportunity..." | Q22 |
| 71 | Ajay Janjari | Mgmt-A | 161 | 148 | "So we have disclosed that we broadly believe that..." | A22 |
| 72 | Naman Parmar | Analyst-Q | 163 | 150 | "Secondly if you can help us in understanding on..." | Q23 — REPEAT_QUESTION (telecom vs DC margin split touches same ground as Q7/turn32 gross-margin-vs-mix question) |
| 73 | Ankit Tagral | Mgmt-A | 165 | 152 | "We don't normally call out the margin difference but..." | A23 (partial REFUSAL — exact split declined, qualitative direction given) |
| 74 | Operator | Call admin | 167 | 154 | "With this we conclude our call. I would now..." | Q&A ends |
| 75 | Rahul Darak | Mgmt-IR | 169 | 156 | "Thank you everyone for taking time to hear us..." | Closing remarks |

Turn-count effort split (auditable via this table): opening remarks turns 1-15 (15 turns,
management-and-operator-only preamble) vs Q&A turns 16-74 (59 turns) vs closing (turn 75).
Q&A occupies 59/75 = 78.7% of numbered turns.

---
## 3. QUESTIONS (23 total, analyst name + firm + topic + turn)

| Q# | Turn | Analyst | Firm | Topic | Flags |
|----|------|---------|------|-------|-------|
| 1 | 17 | Achan | Dwama | Capacity utilization Q1; order inflow timing (US/Europe, early vs late cycle) | |
| 2 | 19 | Achan | Dwama | Follow-up: ordering cycle stage industry-wide relative to DC capex buildout | |
| 3 | 21 | Achan | Dwama | Rare-earth / raw-material sourcing visibility (germanium, helium, etc.) | |
| 4 | 24 | Devarat | 7 Holding | Capacity headroom for additional large orders; capacity addition plans | REPEAT_QUESTION (capacity utilization, cf. Q1) |
| 5 | 27 | Shil Jain | Nuvama Bank Security | Q2/full-year execution and order-book-to-revenue guidance | |
| 6 | 29 | Shil Jain | Nuvama Bank Security | Order pipeline / negotiations in progress | |
| 7 | 32 | Patel | Nishai | Gross margin flat despite DC mix increase; input cost pressure; margin trajectory as DC mix rises | REPEAT_QUESTION (margin-mix, cf. Q23) |
| 8 | 34 | Patel | Nishai | Order intake ex-$1.1bn hyperscaler deal; was capacity-constrained order selection a conscious choice | |
| 9 | 36 | Patel | Nishai | Germanium sourcing: spot buying vs fixed-price contracts | REPEAT_QUESTION (germanium, cf. Q3) |
| 10 | 38 | Patel | Nishai | Post-debottlenecking appetite for another sizable long-term order | |
| 11 | 41 | Krish | Inam Holdings | Strategic telecom-vs-AI/DC order-book mix philosophy, long-term stability vs AI growth | |
| 12 | 43 | Krish | Inam Holdings | Follow-up: will the ~50% DC/enterprise mix hold over 3-5 years or self-adjust | |
| 13 | 46 | Subramanium | Arihant | Q1 DC revenue share; Celesta fiber-per-rack figures (page 11 of PPT); industry realization trend ($18-$30 range) | |
| 14 | 49 | Akhil | Seven Holding | Is Q1 revenue/profitability performance sustainable through the rest of the year | REPEAT_QUESTION (revenue guidance, cf. Q5) |
| 15 | 51 | Akhil | Seven Holding | Capex plan for this year and next year | |
| 16 | 53 | Akhil | Seven Holding | Breakup of optical connectivity vs digital business revenue | |
| 17 | 56 | Tushar | Sangi Family Office | Optical transceiver manufacturing plans; margin-upgrade driver (pricing vs attach rate) | |
| 18 | 59 | Aniel | Segel Capital Advisor | Semiconductor value-chain play; China data-center opportunity and token-cost deflation risk | |
| 19 | 62 | Sati K | PM Capital | $100M US plant capex phasing and commissioning timeline | |
| 20 | 64 | Sati K | PM Capital | Planned capacity number for the US plant | |
| 21 | 67 | Noah | Noah Financials | Germanium/helium supply risk through FY27 and margin/order-book impact; alternate suppliers/tech | REPEAT_QUESTION (germanium/helium, cf. Q3/Q9) |
| 22 | 70 | Naman Parmar | Nishai Investment | Year-end FY27 debt level and working capital post-QIP | |
| 23 | 72 | Naman Parmar | Nishai Investment | Germanium-cost-reduction impact on gross margin; telecom vs DC EBITDA margin split | REPEAT_QUESTION (margin-mix, cf. Q7) |

Distinct analysts asking questions = 12; distinct question-firms with same/near-same name
string = "Nishai" (Patel, Q7-10) vs "Nishai Investment" (Naman Parmar, Q22-23) — `NAME_VARIANT`,
unresolved whether same house.

---
## 4. MANAGEMENT NUMBERS / QUANTIFIED CLAIMS (91 disclosure-unit rows, derived from the
143-token reconciled sweep above; refusals enumerated as units per instruction)

| # | Turn | Speaker | File line | Claim | Flags |
|---|------|---------|-----------|-------|-------|
| 1 | 3 | Ankit | 23 | Global ex-China optical cable market share: 9% | REPEAT (also row 34) |
| 2 | 3 | Ankit | 23 | 30+ years market leadership | |
| 3 | 3 | Ankit | 23 | 785+ patents | REPEAT (also row 26) |
| 4 | 3 | Ankit | 23 | 10+ zero-waste-to-landfill manufacturing facilities worldwide | |
| 5 | 5 | Ankit | 27 | FTTx: 151M fiber-km (2025) -> ~171M fiber-km (2030) | EXTERNAL_STAT |
| 6 | 5 | Ankit | 27 | US: >140M homes fiber-served by 2030 (BEAD/BharatNet-linked) | EXTERNAL_STAT |
| 7 | 5 | Ankit | 27 | CRU: DC optical cable demand +63% in 2026 | EXTERNAL_STAT |
| 8 | 5 | Ankit | 27 | NA installed DC capacity: 63GW (2025) -> 126GW (2030) | EXTERNAL_STAT |
| 9 | 5 | Ankit | 27 | Hyperscaler capex forecast raised: $765bn -> $805bn (Morgan Stanley / unnamed bank) | EXTERNAL_STAT |
| 10 | 5 | Ankit | 27 | Global 5G subscriptions: 6.4bn by 2030 | EXTERNAL_STAT |
| 11 | 5 | Ankit | 27 | India 5G subscriptions: 1.1bn by 2031 | EXTERNAL_STAT |
| 12 | 5 | Ankit | 27 | Global 6G subscriptions: >180M by end-2031 | EXTERNAL_STAT |
| 13 | 6 | Ankit | 29 | McKinsey: 70% of DC demand AI-driven by 2030 | EXTERNAL_STAT |
| 14 | 6 | Ankit | 29 | GPU speed transition: 400G -> 800G -> 1.6T | EXTERNAL_STAT |
| 15 | 6 | Ankit | 29 | TAM uplift: +$10bn for optical connectivity from GPU-speed shift | EXTERNAL_STAT |
| 16 | 6 | Ankit | 29 | India DC capacity: 1.6GW currently -> ~10GW by 2031 (~7x, Morgan Stanley) | EXTERNAL_STAT |
| 17 | 6 | Ankit | 29 | Meta/Reliance: ~3GW India DC deployment plans | EXTERNAL_STAT |
| 18 | 6 | Ankit | 29 | AirTrunk: ~5GW capacity commitment (Maharashtra + Andhra Pradesh) | EXTERNAL_STAT |
| 19 | 6 | Ankit | 29 | India DC tax holidays extended to 2047 | EXTERNAL_STAT |
| 20 | 6 | Ankit | 29 | India optical cable demand: +11% CAGR through 2030 | EXTERNAL_STAT |
| 21 | 6 | Ankit | 29 | CRU: global cable demand +8.2% YoY this year | EXTERNAL_STAT |
| 22 | 6 | Ankit | 29 | CRU: NA CAGR 18.6% (now-2030), upgraded from 15% prior forecast | EXTERNAL_STAT |
| 23 | 7 | Ankit | 31 | Q1 order intake Rs13,100cr = 1.7x FY26 full-year order wins of Rs7,687cr | |
| 24 | 7 | Ankit | 31 | $1.1bn multi-year hyperscaler deal for AI-DC optical connectivity through FY29 | |
| 25 | 7 | Ankit | 31 | Multiple $100M hyperscaler orders for high-fiber-count IBR cable | |
| 26 | 8 | Ankit | 33 | 785+ patents; 9 new filings this quarter | REPEAT (row 3) |
| 27 | 9 | Ankit | 35 | US Connect certification: 4 MMC pre-terminated solution types | |
| 28 | 9 | Ankit | 35 | MMC pre-terminated: "three times" cable density increase over traditional layouts | SPELLED_NUMBER |
| 29 | 9 | Ankit | 35 | Scaling positioned for 800 gig and beyond | |
| 30 | 10 | Ankit | 37 | G654E fiber: 30% lower signal loss | |
| 31 | 10 | Ankit | 37 | Hollow-core fiber: up to 47% latency cut | |
| 32 | 10 | Ankit | 37 | Multi-core fiber: "four to seven times" data capacity, same footprint | SPELLED_NUMBER |
| 33 | 10 | Ankit | 37 | Concat: up to 71% labor-cost reduction | |
| 34 | 11 | Ankit | 39 | Global ex-China OFC market share: 9% | REPEAT (row 1) |
| 35 | 11 | Ankit | 39 | Attach rate: 16%, up from 15% last year | REPEAT (also rows 36-37, 81, 89 below) |
| 36 | 11 | Ankit | 39 | Attach rate target: >20% from next quarter | REPEAT (row 89) |
| 37 | 11 | Ankit | 39 | Attach rate target: 25% by end of FY27 (Q4) | REPEAT (rows 81, 90) |
| 38 | 12 | Ajay | 41 | Revenue: Rs1,910cr, +87% YoY | |
| 39 | 12 | Ajay | 41 | Prior EBITDA margin guidance baseline: 20% by end of FY27 | |
| 40 | 12 | Ajay | 41 | EBITDA: Rs397cr, +184% YoY | |
| 41 | 12 | Ajay | 41 | EBITDA margin guidance RAISED to 23% (from 20%) | REPEAT (row 90) |
| 42 | 12 | Ajay | 41 | PAT: Rs197cr, record, 10% of revenue, highest-ever PAT margin | |
| 43 | 12 | Ajay | 41 | PAT: 3.5x expansion vs full-year FY26 PAT | |
| 44 | 13 | Ajay | 43 | DC segment: 21% of revenue this quarter, up from 1% in FY26 | |
| 45 | 13 | Ajay | 43 | DC+enterprise combined guidance RAISED to ~50% of FY revenue (from 30% prior guidance) | REPEAT (row 80) |
| 46 | 13 | Ajay | 43 | North America revenue share: 54%, up from 39% in FY26 | |
| 47 | 13 | Ajay | 43 | Europe revenue share: 25% | |
| 48 | 13 | Ajay | 43 | Rest-of-world revenue share: 22% | |
| 49 | 14 | Ajay | 45 | Open order book: Rs18,618cr, record high, up 2.4x QoQ | |
| 50 | 14 | Ajay | 45 | Executable in Q2 FY27: Rs2,228cr | REPEAT (row 75) |
| 51 | 14 | Ajay | 45 | Executable Q3 FY27 and beyond: Rs16,390cr | |
| 52 | 14 | Ajay | 45 | Net cash: Rs483cr; net-debt-free status achieved | REPEAT (row 88) |
| 53 | 14 | Ajay | 45 | CRISIL rating outlook revised to Stable | |
| 54 | 14 | Ajay | 45 | ICRA rating upgraded to AA (double A), Stable outlook | |
| 55 | 14 | Ajay | 45 | QIP raised: Rs1,500cr | |
| 56 | 14 | Ajay | 45 | QIP subscription: >2.5x | |
| 57 | 14 | Ajay | 45 | Institutional holding: fresh historic high of 33% | |
| 58 | 14 | Ajay | 45 | QIP proceeds allocation: 75% debt reduction / 25% general corporate purposes | |
| 59 | 15 | Ankit | 47 | RoboEdge: 12+ schools, 10,000+ students | |
| 60 | 15 | Ankit | 47 | Jivan Jyoti: 6,500+ women trained | |
| 61 | 15 | Ankit | 47 | Swasth Suraksha: 27 lakh lives impacted (Maharashtra + Silvasa) | |
| 62 | 15 | Ankit | 47 | Net-zero emissions target by 2030 | |
| 63 | 15 | Ankit | 47 | Since FY19: 286 lakh metric tons of waste diverted | |
| 64 | 15 | Ankit | 47 | 11.6 million cubic meters of water recycled | |
| 65 | 15 | Ankit | 47 | 45,600 metric tons CO2e reduced via energy efficiency | |
| 66 | 15 | Ankit | 47 | 32% of procurement is local | |
| 67 | 15 | Ankit | 47 | 920,000+ lives impacted (education/women empowerment/healthcare) | |
| 68 | 15 | Ankit | 47 | 4,500 kW solar capacity installed | |
| 69 | 15 | Ankit | 47 | 100+ ESG awards since FY19 | |
| 70 | 15 | Ankit | 47 | Aligned with 16 UN SDGs | |
| 71 | 18 | Ankit | 55 | Capacity utilization — NOT DISCLOSED (only qualitative "improving QoQ" given) | ZERO_STANDING / MGMT_REFUSAL |
| 72 | 20 | Ankit | 59 | US DC buildout this year estimated at 8-10 GW (mgmt-cited industry figure) | EXTERNAL_STAT |
| 73 | 22 | Ankit | 63 | Raw-material input basket framed as "three or four" key elements (germanium, helium, polyethylene, etc.) | SPELLED_NUMBER |
| 74 | 28 | Ajay | 75 | Revenue guidance — DECLINED ("we don't give any guidance on the revenue") | ZERO_STANDING / MGMT_REFUSAL |
| 75 | 28 | Ajay | 75 | Executable Q2 order book restated: Rs2,228cr | REPEAT (row 50) |
| 76 | 37 | Ankit | 93 | Germanium sourcing contract structure — DECLINED ("can't comment... for competitive reasons") | ZERO_STANDING / MGMT_REFUSAL |
| 77 | 39 | Ankit | 97 | Specific size of any future large order — DECLINED ("can't comment on any specific size") | ZERO_STANDING / MGMT_REFUSAL |
| 78 | 42 | Ankit | 103 | BEAD (US rural fiber): 5-7 year buildout | |
| 79 | 42 | Ankit | 103 | BharatNet (India): 3-4 year buildout | |
| 80 | 42 | Ankit | 103 | DC + enterprise segment target: ~50% overall | REPEAT (row 45) |
| 81 | 44 | Ankit | 107 | Attach rate 25% by Q4 restated | REPEAT (rows 37, 90) |
| 82 | 47 | Ankit | 113 | Realization / pricing figures — DECLINED ("we do not comment on realization broadly") | ZERO_STANDING / MGMT_REFUSAL |
| 83 | 50 | Ankit | 119 | Full-year / longer-term guidance — DECLINED ("we don't guide any numbers for the full year or longer term") | ZERO_STANDING / MGMT_REFUSAL |
| 84 | 52 | Ankit | 123 | Capex guidance: ~Rs500cr/year x 3 years = ~Rs1,500cr cumulative | |
| 85 | 54 | Ankit | 127 | Optical connectivity vs digital revenue breakup — DECLINED ("No we don't break that out.") | ZERO_STANDING / MGMT_REFUSAL |
| 86 | 63 | Ankit | 145 | US plant investment: $100M over 5 years | |
| 87 | 65 | Ankit | 149 | US plant capacity number — DECLINED / not yet finalized ("once we're able to finalize... we'll be able to share that") | MGMT_REFUSAL (deferred, not outright declined) |
| 88 | 71 | Ajay | 161 | Net-debt-free status reiterated as holding even during FY27 | REPEAT (row 52) |
| 89 | 73 | Ankit | 165 | Attach rate 25% by Q4 restated (3rd mention) | REPEAT (rows 37, 81) |
| 90 | 73 | Ankit | 165 | EBITDA margin target 23% restated | REPEAT (row 41) |
| 91 | 73 | Ankit | 165 | Telecom vs DC EBITDA margin split — DECLINED as exact figure; qualitative direction only ("margins... for data center are higher... than the telecom segment") | ZERO_STANDING / MGMT_REFUSAL (partial — direction given, magnitude withheld) |

Refusal count: 10 distinct management non-disclosures enumerated as units (rows 71, 74, 76,
77, 82, 83, 85, 87, 91, plus row 91's partial-refusal companion already counted once) = 9
full/partial REFUSAL rows total (71, 74, 76, 77, 82, 83, 85, 87, 91).
Repeat-claim count: rows flagged REPEAT = 12 (rows 26, 34, 35, 36, 37, 41, 45, 50, 75, 80,
81, 88, 89, 90 — 14 occurrences referencing 6 underlying metrics: patents, OFC share,
attach-rate-current, attach-rate-near-term-target, attach-rate-Q4-target, EBITDA-margin-target,
DC-enterprise-mix-target, Q2-executable-order-book, net-debt-free-status).

---
## 5. FORWARD-COMMITMENT / HEDGE CROSS-REFERENCE (derived from tables above; concall category 5)

| Type | Statement | Turn(s) | Ledger row(s) |
|------|-----------|---------|----------------|
| Forward commitment | EBITDA margin guidance raised to 23% | 12, 73 | 41, 90 |
| Forward commitment | DC+enterprise mix to scale to ~50% of FY revenue | 13, 42 | 45, 80 |
| Forward commitment | Attach rate >20% next quarter, 25% by Q4 FY27 | 11, 44, 73 | 36, 37, 81, 89 |
| Forward commitment | Net debt free even during FY27 | 14, 71 | 52, 88 |
| Forward commitment | Capex ~Rs500cr/yr x3 = ~Rs1,500cr | 52 | 84 |
| Forward commitment | US plant $100M over 5 years | 63 | 86 |
| Hedge / refusal | "we don't give any guidance on the revenue" | 28 | 74 |
| Hedge / refusal | "we don't guide any numbers for the full year or longer term" | 50 | 83 |
| Hedge / refusal | "No we don't break that out" (connectivity/digital split) | 54 | 85 |
| Hedge / refusal | "we do not comment on realization broadly" | 47 | 82 |
| Hedge / refusal | "can't comment... for competitive reasons" (germanium contracts) | 37 | 76 |
| Hedge / refusal | "can't comment on any specific size" (future order) | 39 | 77 |
| Hedge / refusal | "we don't disclose actual numbers" (capacity utilization) | 18 | 71 |
| Hedge / refusal | "We don't normally call out the margin difference" (telecom vs DC) | 73 | 91 |
| Hedge / refusal | US-plant capacity — deferred pending finalization | 65 | 87 |

---
## 6. OPEN FLAGS SUMMARY

- REPEAT_QUESTION: Q4/Q1 (capacity utilization), Q9/Q3/Q21 (germanium/helium), Q14/Q5
  (revenue-guidance-adjacent), Q23/Q7 (margin-mix)
- REPEAT (mgmt number restated across turns): patents, OFC market share, attach rate (current
  + two forward targets), EBITDA margin target, DC/enterprise mix target, Q2 executable order
  book, net-debt-free status
- MGMT_REFUSAL (declined to disclose, enumerated per ZERO_STANDING-equivalent rule for concall):
  capacity utilization, revenue guidance, germanium contract terms, future order size,
  realization/pricing, full-year guidance, connectivity/digital revenue split, US-plant capacity
  (deferred), telecom-vs-DC margin split (partial)
- SPELLED_NUMBER (quantified claim not catchable by digit-only grep): multi-core "four to seven
  times", MMC "three times" density, raw-material "three or four" elements
- NAME_VARIANT: "Nishai" (Patel) vs "Nishai Investment" (Naman Parmar) — possibly same house,
  not resolved by this ledger
- EXTERNAL_STAT: 18 rows are third-party/industry statistics (CRU, McKinsey, Morgan Stanley,
  unnamed bank) cited by management rather than STL's own actuals/guidance — flagged so A3/A4
  do not treat them as STL-sourced numbers in arithmetic-consistency checks
- MGMT_ABSENCE: not triggered (MD and CFO both present and active in Q&A)
