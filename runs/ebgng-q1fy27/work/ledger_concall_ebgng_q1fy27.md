# A2 ENUMERATION LEDGER — GNG Electronics Limited (EBGNG), Q1 FY27, Concall Transcript
Source: `runs/ebgng-q1fy27/work/extract_concall_ebgng_q1fy27.txt` (113 lines, verbatim ASR-transcribed text)
Prior-quarter ledger: not supplied — no diff possible (no `DROPPED_SLIDE` / prior-turn comparison performed).

```
=== A2 COUNT TEST ===
category: turns          grep_count: 61   sweep_count: 61   match: yes
category: questions      grep_count: 26   sweep_count: 26   match: yes
category: mgmt_numbers   grep_count: 79   sweep_count: 79   match: yes
category: zero_standing  grep_count: 7    sweep_count: 7    match: yes
category: notes            n/a (no numbered-notes section in a concall transcript)
category: line_items       n/a (no financial table in this document; figures are spoken, captured under mgmt_numbers)
category: agenda_items     n/a (not a Board Outcome letter)
category: auditor_paras    n/a (not an auditor report)
category: entities         n/a (no consolidation list in a concall transcript)
category: slides           n/a (not an investor presentation)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on the mgmt_numbers / zero_standing count test: this is free-text transcript, not a
structured table, so the "grep pass" cannot be a single regex the way `^\s*[0-9]+\.` works for numbered
notes. Grep pass = (a) `grep -n "^\[A"` to isolate all management-attributed lines (30 lines), (b)
`grep -n` over MD opening / CFO remarks / closing lines (lines 28-56, 128-129), (c) `grep -oE` numeric-token
extraction over both sets (94 raw tokens in [A] lines + 69 raw tokens in opening/closing/lead-in lines).
Manual sweep = every raw numeric token traced back to the single disclosure unit it belongs to (e.g.
"329" + "basis points" = one GM-YoY-delta fact; "27,500" = one ASP-comparator fact), with duplicate
utterances of the same fact in a later turn logged as a separate ledger row flagged RESTATED rather than
merged. Every raw token surfaced by the grep pass was traced to a row below; no orphan token remained
outside the sweep. Zero/negligible-value claims ("no disruption," "negligible competition," "no fixed
capital," "no challenge," "no significant cause of concern," implicit "no slowdown") are counted separately
as `zero_standing` per the SOUTHWEST convention (a claimed-zero line is still a line).

---
## 1. PARTICIPANTS

| # | Name | Side | Designation / Firm | Speaking turns? | Flags |
|---|------|------|---------------------|-----------------|-------|
| P1 | Sharad Khandelwal | Management | Founder & MD | Yes (opening, closing, most Q&A answers) | — |
| P2 | AJ Pancholi | Management | Director | No speaking turn attributed in transcript | SILENT_PARTICIPANT |
| P3 | Rakesh Jhunjhunwala | Management | CFO | Yes (financial remarks, several Q&A answers) | — |
| P4 | Rohit Arora | Management | Strategy & IR | No speaking turn attributed in transcript | SILENT_PARTICIPANT |
| P5 | Abhin Karumanjik | Analyst-side / Moderator | Motilal Oswal Financial Services | Yes (moderator intro, Q6 questioner) | dual role: moderator AND questioner |
| P6 | Chirag Jain | Analyst | MK Global | Yes (Q1 block, turns 5,7,9) | — |
| P7 | Shanik Mata | Analyst | "Indo (?)" — firm name uncertain in transcript (ASR) | Yes (Q2 block, turns 12,14) | FIRM_UNCERTAIN (ASR) |
| P8 | Sunil J | Analyst | Nirmal Bang Securities | Yes (Q3 block, turns 17,19,22,24,26,28) | — |
| P9 | Shri | Analyst | Equirus Wealth Advisor | Yes (Q4 block, turn 31) | first name only given in transcript |
| P10 | Paras Chira | Analyst | Purplino / Vertex Ventures | Yes (Q5 block, turns 33,35,37,39,41,43,45) | dual-firm attribution as supplied |

Note: MD (Sharad Khandelwal) is present and substantively engaged throughout — `MGMT_ABSENCE` does NOT
apply to the CMD/promoter role. Two named management attendees (AJ Pancholi, Rohit Arora) are introduced
by name at the top of the call but have zero attributed lines in the transcript body — flagged
`SILENT_PARTICIPANT` (not the formal `MGMT_ABSENCE`, which is reserved for the promoter/CMD).

---
## 2. SPEAKER TURNS (sequential, line-cited)

| Turn | Line(s) | Speaker | Side | First ~10 words |
|------|---------|---------|------|------------------|
| 1 | 24 | Operator (unnamed conference operator) | Neutral | "Good evening everyone and welcome to the Q1 FY27 earnings..." |
| 2 | 26 | Abhin Karumanjik | Moderator | "Thank you team. Good evening everyone. On behalf of Motilal..." |
| 3 | 28-53 | Sharad Khandelwal (MD) | Management | "Good evening and thank you everyone. I welcome you all..." (MD Opening Remarks, one continuous turn spanning 13 paragraphs) |
| 4 | 55-56 | Rakesh Jhunjhunwala (CFO) | Management | "Thank you Sharad and good evening everyone. Let me walk..." (CFO Financial Remarks, one continuous turn) |
| 5 | 61 | Chirag Jain (MK Global) | Analyst [Q] | "Congratulations on very strong performance. My first question: can..." |
| 6 | 62 | Rakesh Jhunjhunwala (CFO) | Management [A] | "So exact number... [audio breaking]... Laptop, desktops and others is..." |
| 7 | 63 | Chirag Jain | Analyst [Q] | "Thank you. Also if you can share update on the..." |
| 8 | 64 | CFO | Management [A] | "So in terms of net debt that we had at..." |
| 9 | 65 | Chirag Jain | Analyst [Q] | "And just last thing, in terms of our profitability the..." |
| 10 | 66 | CFO | Management [A] | "No, it's more of more acceptability, more deeper penetration..." |
| 11 | 67 | Sharad Khandelwal (MD) | Management [A] | "This is Sharad. Also, I would like to mention a..." |
| 12 | 70 | Shanik Mata | Analyst [Q] | "Broadly a question around the margin versus the global margins..." |
| 13 | 71 | CFO | Management [A] | "I would say you have done the breakup absolutely and..." |
| 14 | 72 | Shanik Mata | Analyst [Q] | "Can you reiterate your directional target once again please?" |
| 15 | 73 | MD | Management [A] | "Two things before I give guidance. Our products — we..." |
| 16 | 74 | MD | Management [A] | "And the idea is that we are always conservative in..." |
| 17 | 77 | Sunil J (Nirmal Bang) | Analyst [Q] | "My question relates to volume growth. The volume growth is..." |
| 18 | 78 | CFO | Management [A] | "That's right. That's right." |
| 19 | 79 | Sunil J | Analyst [Q] | "And the balance growth we are getting is on account..." |
| 20 | 80 | CFO | Management [A] | "In terms of the overall unit numbers you're right, it..." |
| 21 | 81 | MD | Management [A] | "There's an expansion on account of two things: one is..." |
| 22 | 82 | Sunil J | Analyst [Q] | "My question comes from the point that we are seeing..." |
| 23 | 83 | MD | Management [A] | "Absolutely. See we have been keeping, as I mentioned in..." |
| 24 | 84 | Sunil J | Analyst [Q] | "This quarter again you had seen memory prices increasing by..." |
| 25 | 85 | MD | Management [A] | "The memory price rose by 10% this quarter and I..." |
| 26 | 86 | Sunil J | Analyst [Q] | "One strategic question — you are in B2B, have you..." |
| 27 | 87 | MD | Management [A] | "So we get a better appreciation of quality, consistency and..." |
| 28 | 88 | Sunil J | Analyst [Q] | "Just a data question — what's the inventory at the..." |
| 29 | 89 | CFO | Management [A] | "The inventory at the end of Q1 is about 700..." |
| 30 | 90 | CFO | Management [A, additional] | "I would want to address another operational highlight in terms..." |
| 31 | 93 | Shri (Equirus) | Analyst [Q] | "A bit on the other expenses side. I see that..." |
| 32 | 94 | CFO | Management [A] | "Coming to the second question first — the tax rate..." |
| 33 | 97 | Paras Chira | Analyst [Q] | "With this recent disruption again, is our UAE refurbishment facility..." |
| 34 | 98 | MD | Management [A] | "There is no disruption at all in our UAE. All..." |
| 35 | 99 | Paras Chira | Analyst [Q] | "Can you quantify your targets for — I know inventory..." |
| 36 | 100 | MD | Management [A] | "Situation is very evolving and current situation demands that..." |
| 37 | 101 | Paras Chira | Analyst [Q] | "So your inventory is also one of the strategic levers..." |
| 38 | 102 | MD | Management [A] | "Absolutely. We buy from banks, we buy from leasing companies..." |
| 39 | 103 | Paras Chira | Analyst [Q] | "What contribution do you expect from Redington, Supertron, Ingram..." |
| 40 | 104 | MD | Management [A] | "It's not correct for me to give exact numbers, but..." |
| 41 | 105 | Paras Chira | Analyst [Q] | "You said one of the key factors for improving margins..." |
| 42 | 106 | MD | Management [A] | "Currently we are pegging our product around 30% (of new)..." |
| 43 | 107 | Paras Chira | Analyst [Q] | "So that kind of room may be there." |
| 44 | 108 | MD | Management [A] | "Absolutely, and also the procurement remains lumpy because we have..." |
| 45 | 109 | Paras Chira | Analyst [Q] | "Do you see yourself becoming one of the Dell or..." |
| 46 | 110 | MD | Management [A] | "I don't want to compare — they are big guys..." |
| 47 | 113 | Abhin Karumanjik (Motilal) | Analyst [Q] | "Congratulations on a good set of numbers. My first question..." |
| 48 | 114 | MD | Management [A] | "Yes, both are correct actually. But the prices of the..." |
| 49 | 115 | Abhin Karumanjik | Analyst [Q] | "If you can give a rough indication of how much..." |
| 50 | 116 | MD | Management [A] | "We have been able to procure, thanks to our reach..." |
| 51 | 117 | Abhin Karumanjik | Analyst [Q] | "So it's safe to assume that at least for the..." |
| 52 | 118 | MD | Management [A] | "No challenge — we are well positioned to address the..." |
| 53 | 119 | Abhin Karumanjik | Analyst [Q] | "Regarding opex — if I look at employee cost and..." |
| 54 | 120 | MD | Management [A] | "We are on the expansion path and we have to..." |
| 55 | 121 | Abhin Karumanjik | Analyst [Q] | "So these should run ahead of the revenue at least..." |
| 56 | 122 | MD | Management [A] | "I won't say they won't rise in proportion. The operating..." |
| 57 | 123 | Abhin Karumanjik | Analyst [Q] | "A small clarification — your guidance is 25% and you..." |
| 58 | 124 | MD | Management [A] | "This is a low seasonality quarter. First quarter is usually..." |
| 59 | 125 | Abhin Karumanjik | Analyst [Q] | "My question is — we have beefed up the inventory..." |
| 60 | 126 | MD | Management [A] | "I don't think growth will slow down. I think that..." |
| 61 | 128-129 | Sharad Khandelwal (MD) | Management, Closing | "Thank you everyone for joining this call. We really appreciate..." |

Turn arithmetic check: 4 preamble/opening/closing turns (1,2,3,4) + 56 Q&A turns (26 `[Q]` + 30 `[A]`, turns
5-60) + 1 closing turn (61) = 61. Matches grep (`[Q]`=26, `[A`=30, plus 5 non-bracketed turns: operator,
moderator-intro, MD-opening, CFO-remarks, closing = 61).

---
## 3. QUESTIONS (one row per `[Q]` marker, analyst/firm/topic/turn)

| Q# | Turn | Line | Analyst | Firm | Topic | Flags |
|----|------|------|---------|------|-------|-------|
| Q-1 | 5 | 61 | Chirag Jain | MK Global | Q1 unit volume (laptops/desktops/others split), vs 41,000 units in Q4 FY26 (analyst-cited comparator) | — |
| Q-2 | 7 | 63 | Chirag Jain | MK Global | Working capital cycle and associated debt | — |
| Q-3 | 9 | 65 | Chirag Jain | MK Global | Standalone (India) vs overseas profitability divergence — one-off or structural? | — |
| Q-4 | 12 | 70 | Shanik Mata | "Indo (?)" (ASR-uncertain) | Decompose consolidated GM lift: geo-mix shift vs seasonally soft India vs genuine like-for-like improvement; ask for underwritten blended GM as India volume scales via Redington | — |
| Q-5 | 14 | 72 | Shanik Mata | "Indo (?)" | Reiterate directional (margin) guidance | follow-up to Q-4, same analyst |
| Q-6 | 17 | 77 | Sunil J | Nirmal Bang Securities | Confirm volume growth ~18% (combined) | — |
| Q-7 | 19 | 79 | Sunil J | Nirmal Bang Securities | Realization growth drivers: geo/product mix vs price increase | — |
| Q-8 | 22 | 82 | Sunil J | Nirmal Bang Securities | Inventory gain from cost/price inflation given high inventory holding | — |
| Q-9 | 24 | 84 | Sunil J | Nirmal Bang Securities | Memory price trend — plateauing or further rise | — |
| Q-10 | 26 | 86 | Sunil J | Nirmal Bang Securities | Strategic: any B2C ambitions beyond B2B | — |
| Q-11 | 28 | 88 | Sunil J | Nirmal Bang Securities | Data ask: inventory balance at end of Q1 | — |
| Q-12 | 31 | 93 | Shri | Equirus Wealth Advisor | Other expenses jump (analyst cites >65% YoY) and FY27 effective tax rate guidance | analyst figure (65%) vs CFO figure (68%) — see NUMBER_DISCREPANCY in mgmt_numbers table |
| Q-13 | 33 | 97 | Paras Chira | Purplino / Vertex Ventures | UAE facility/logistics impact from regional disruption | — |
| Q-14 | 35 | 99 | Paras Chira | Purplino / Vertex Ventures | Targets for inventory days, receivable days, cash conversion cycle, OCF improvement steps | — |
| Q-15 | 37 | 101 | Paras Chira | Purplino / Vertex Ventures | Confirm inventory as a deliberate strategic margin lever | — |
| Q-16 | 39 | 103 | Paras Chira | Purplino / Vertex Ventures | Expected contribution from Redington / Supertron / Ingram over 12-18 months | — |
| Q-17 | 41 | 105 | Paras Chira | Purplino / Vertex Ventures | Is refurb realization capped as a % of new-laptop price? | — |
| Q-18 | 43 | 107 | Paras Chira | Purplino / Vertex Ventures | Confirm margin "room" framing (30%→50% of new) | follow-up to Q-17 |
| Q-19 | 45 | 109 | Paras Chira | Purplino / Vertex Ventures | Long-term vision: become "the Dell/HP of refurbished" in 5-10 years | — |
| Q-20 | 47 | 113 | Abhin Karumanjik | Motilal Oswal | Procurement challenges as new-laptop prices rise; disposal-cycle extension risk | — |
| Q-21 | 49 | 115 | Abhin Karumanjik | Motilal Oswal | Quantify procurement cost inflation vs new-laptop +20-30% (analyst estimate) | analyst-supplied 20-30% figure not confirmed with a specific number by MD |
| Q-22 | 51 | 117 | Abhin Karumanjik | Motilal Oswal | Confirm no procurement challenge for next couple of quarters | — |
| Q-23 | 53 | 119 | Abhin Karumanjik | Motilal Oswal | Employee cost / other expenses opex running ahead of revenue — when does operating leverage show up? | — |
| Q-24 | 55 | 121 | Abhin Karumanjik | Motilal Oswal | Confirm opex continues ahead of revenue for next couple of years | follow-up to Q-23 |
| Q-25 | 57 | 123 | Abhin Karumanjik | Motilal Oswal | Growth deceleration vs raised guidance (~40% odd prior quarters to ~30% now) — seasonal? | analyst-supplied growth-deceleration figures not restated with specific numbers by MD |
| Q-26 | 59 | 125 | Abhin Karumanjik | Motilal Oswal | Inventory build amid slowing growth — balance sheet strain risk | — |

No verbatim `REPEAT_QUESTION` across different analysts identified (each question is topically distinct in
its specific ask), though margin/inventory is a recurring theme across 4 of 6 questioner blocks (Chirag,
Shanik, Sunil J, Paras Chira) — thematic clustering noted for A3/A4, not flagged as a formal repeat.

---
## 4. MANAGEMENT NUMBERS (every number spoken by management, or explicitly affirmed by management
in response to an analyst-stated figure, one row per disclosure instance — restatements in a later
turn get their own row flagged RESTATED rather than being merged)

| # | Turn | Line | Speaker | Disclosure | Flags |
|---|------|------|---------|------------|-------|
| N1 | 3 | 33 | MD | Revenue grew 32% YoY to Rs412.5cr | — |
| N2 | 3 | 33 | MD | Gross margin 24.65%, +329bps YoY | — |
| N3 | 3 | 33 | MD | Gross margin +542bps QoQ | — |
| N4 | 3 | 35 | MD | Memory prices +5-10% in the last quarter | — |
| N5 | 3 | 35 | MD | 8GB DDR5 at $126 | — |
| N6 | 3 | 35 | MD | 16GB DDR5 at $231, as of June 30 | — |
| N7 | 3 | 35 | MD | Memory prices "more than doubled" since Oct 2025 | CONTRADICTION — MD self-corrects in Q&A (see N51: "not doubled... gone up by five times") |
| N8 | 3 | 35 | MD | Entry-level laptop (8GB RAM/512GB SSD) price risen Rs40,000 → Rs48,000 | — |
| N9 | 3 | 35 | MD | IDC: global PC shipments -11.3% for CY2026 | — |
| N10 | 3 | 35 | MD | IDC: H2 CY2026 -20% YoY decline | — |
| N11 | 3 | 35 | MD | Unit decline of ~30 million in two quarters (vs counterfactual growth) | — |
| N12 | 3 | 35 | MD | No meaningful memory-shortage relief expected before end of 2027 | forward timeline |
| N13 | 3 | 41 | MD | India installed PC base ~55-60 million | — |
| N14 | 3 | 41 | MD | India mobile phone users ~1 billion | — |
| N15 | 3 | 41 | MD | India student population ~300 million | — |
| N16 | 3 | 41 | MD | Africa student population ~250 million | — |
| N17 | 3 | 47 | MD | Channel partners believe refurb market can grow "four to five times" over coming years | forward-looking, partner belief not company guidance |
| N18 | 3 | 47, 49 | MD | Warranty: 3-year (India) / 1-year (international) | restated at line 49 |
| N19 | 3 | 51 | MD | 49 countries served, up from 46 (end-FY26) | — |
| N20 | 3 | 51 | MD | 5,130 customer touchpoints | — |
| N21 | 3 | 51 | MD | 773 suppliers | — |
| N22 | 3 | 51 | MD | 2,420 employees as of June 2026, up from 2,148 | — |
| N23 | 4 | 56 | CFO | Revenue Rs412.5cr, +32% YoY | RESTATED (ref N1) |
| N24 | 4 | 56 | CFO | Gross profit Rs101.6cr | — |
| N25 | 4 | 56 | CFO | Gross margin 24.6%, +329bps YoY, +542bps QoQ | RESTATED (ref N2/N3); note 24.6% vs MD's 24.65% (line33) — immaterial rounding, not flagged as contradiction |
| N26 | 4 | 56 | CFO | EBITDA Rs52.8cr, margin 12.8%, +156bps YoY | — |
| N27 | 4 | 56 | CFO | Q1 FY26 EBITDA margin comparator 11.3% | — |
| N28 | 4 | 56 | CFO | PAT Rs28.9cr, +56% YoY | — |
| N29 | 4 | 56 | CFO | PAT margin 7% vs 5.9% in Q1 FY26, +108bps YoY | — |
| N30 | 6 | 62 | CFO | Units ~42,000 (laptops + desktops + others combined) | — |
| N31 | 6 | 62 | CFO | 81% of revenue from laptops, balance from others | — |
| N32 | 6 | 62 | CFO | Geo mix: India 36% | — |
| N33 | 6 | 62 | CFO | Geo mix: Middle East 12% | — |
| N34 | 6 | 62 | CFO | Geo mix: US + Europe combined 47% | — |
| N35 | 6 | 62 | CFO | Geo mix: US 24% | — |
| N36 | 6 | 62 | CFO | Geo mix: Europe 23% | — |
| N37 | 6 | 62 | CFO | Geo mix: Others ~5% | — |
| N38 | 8 | 64 | CFO | Net debt at end of March-26 ~Rs300cr (rounded) | — |
| N39 | 8 | 64 | CFO | Net debt at Q1 FY27 Rs406cr | — |
| N40 | 8 | 64 | CFO | Net debt increase ~Rs100cr QoQ | — |
| N41 | 8 | 64 | CFO | Working capital "marginally gone down" vs March-26 | no magnitude given — IMPRECISE_MAGNITUDE |
| N42 | 13 | 71 | CFO | India standalone gross margin 21% (affirming analyst's figure) | CFO-affirmed analyst-computed figure |
| N43 | 13 | 71 | CFO | International/overseas gross margin "almost touching 30%" (affirming analyst's figure) | CFO-affirmed analyst-computed figure |
| N44 | 13 | 71 | CFO | Geo spread: US+Europe ~47% of total | RESTATED (ref N34) |
| N45 | 15 | 73 | MD | Revenue growth guidance raised: 25% → 30% (FY27) | guidance revision |
| N46 | 15 | 73 | MD | PAT margin guidance raised: 0.5% → 0.75-1% (FY27) | guidance revision |
| N47 | 18 | 78 | CFO | Volume growth 18% (combined) — confirmed | — |
| N48 | 20 | 80 | CFO | Volume growth 18% | RESTATED (ref N47) |
| N49 | 20 | 80 | CFO | Overall (value) growth 32% | RESTATED (ref N1) |
| N50 | 25 | 85 | MD | Memory price +10% this quarter | — |
| N51 | 25 | 85 | MD | Correction: memory prices up "five times" since Oct 2025, NOT doubled | CONTRADICTION with N7 (self-correction mid-call) |
| N52 | 25 | 85 | MD | Expectation memory prices continue rising 5-10% every quarter | forward-looking |
| N53 | 29 | 89 | CFO | Inventory at end of Q1 ~Rs700cr | — |
| N54 | 29 | 89 | CFO | Inventory at end of March-26 ~Rs740cr | — |
| N55 | 30 | 90 | CFO | Laptop ASP Rs30,763 (Q1 FY27) | — |
| N56 | 30 | 90 | CFO | Laptop ASP comparator Rs27,500 (Q1 FY26) | — |
| N57 | 30 | 90 | CFO | Laptop ASP comparator Rs30,000 (previous quarter, Q4 FY26) | — |
| N58 | 30 | 90 | CFO | Laptop ASP +12% YoY | — |
| N59 | 30 | 90 | CFO | Laptop ASP +2.5% QoQ | — |
| N60 | 30 | 90 | CFO | Others ASP ~Rs19,326 (Q1 FY27; also stated as "19,300 odd") | internal figure varies 19,300 vs 19,326 within same turn — AMBIGUOUS_FIGURE |
| N61 | 30 | 90 | CFO | Others ASP comparator ~Rs17,500 (Q1 FY26) | — |
| N62 | 30 | 90 | CFO | Others ASP +10% YoY | — |
| N63 | 30 | 90 | CFO | Others ASP comparator Rs19,900 (previous quarter) | — |
| N64 | 30 | 90 | CFO | Others ASP QoQ change stated as both "~1.5% better" and, in the same breath, "on an overall basis 12%" | AMBIGUOUS_FIGURE — the 12% appears to be a restatement of the laptop YoY figure (N58) misattributed to others/QoQ by the transcript; needs A3 forensic review against filing |
| N65 | 32 | 94 | CFO | ETR guidance 10-12% for FY27, consolidated basis | — |
| N66 | 32 | 93/94 | CFO | Other expenses +68% YoY (CFO figure) | NUMBER_DISCREPANCY — analyst had stated ">65%" at line 93; CFO states 68% at line 94 |
| N67 | 34 | 98 | MD | ~500 missiles fired at UAE (regional conflict context) | — |
| N68 | 34 | 98 | MD | ~2,000 drones fired at UAE | — |
| N69 | 36 | 100 | MD | US bank opportunity: ~60,000 units of stock | — |
| N70 | 36 | 100 | MD | Target ~30-40 days of finished inventory | — |
| N71 | 38 | 102 | MD | Australia customer bought ~3,000 laptops in one shot | — |
| N72 | 40 | 104 | MD | Distributor ranking (India): Redington #1, Ingram #2, Supertron #5 | — |
| N73 | 42 | 106 | MD | Refurb currently priced ~30% of new-laptop price | — |
| N74 | 42 | 106 | MD | If pushed 30% → 35%, implies ~17% margin expansion | illustrative math, not guidance (MD explicitly disclaims "not giving guidance") |
| N75 | 42 | 106 | MD | Refurb pricing ceiling ~50% of new (won't go beyond) | — |
| N76 | 42 | 106 | MD | Comparator: phone/car refurbished pricing ~50% of new | — |
| N77 | 12/13 | 70/71 | Analyst (Shanik Mata) stated, CFO-affirmed | India entity built Rs75cr of inventory QoQ | CFO affirms breakup "absolutely and directionally correct" without isolating this specific rupee figure — CONFIRMED_BY_MGMT (qualified) |
| N78 | 12/13 | 70/71 | Analyst stated, CFO-affirmed | Group net inventory drew down Rs38cr QoQ | same qualification as N77 — CONFIRMED_BY_MGMT (qualified) |
| N79 | 12 | 70 | Analyst (Shanik Mata) stated, NOT confirmed by management | "your consolidated revenue fell almost 37%" this quarter | CONTRADICTION — directly conflicts with the +32% consolidated revenue growth stated by both MD (line33) and CFO (line56); management does not repeat or correct this specific figure in the response (line71); likely ASR/transcription anomaly — flagged for A3 forensic reconciliation against the filed results, not merely accepted |

mgmt_numbers total = 79 rows (N1-N79).

---
## 5. ZERO / NEGLIBLE-VALUE STANDING CLAIMS (`ZERO_STANDING` — claimed-zero or claimed-negligible
disclosures; the SOUTHWEST convention applied to a spoken-word document: a claim of "none/negligible"
on a metric that could plausibly be nonzero is still a line, not a silence)

| # | Turn | Line | Speaker | Claim | Flag |
|---|------|------|---------|-------|------|
| Z1 | 11 | 67 | MD | "We are actually facing negligible competition" | ZERO_STANDING |
| Z2 | 15 | 73 | MD | "We are finding negligible competition in the areas and customers that we deal with" | ZERO_STANDING (RESTATED, ref Z1) |
| Z3 | 34 | 98 | MD | "There is no disruption at all in our UAE... we see no visible damage anywhere" (despite ~500 missiles / ~2,000 drones fired at UAE, N67/N68) | ZERO_STANDING |
| Z4 | 32 | 94 | CFO | "I don't think there's any significant cause of concern" (re +68% other-expenses growth) | ZERO_STANDING |
| Z5 | 36 | 100 | MD | "We don't have any fixed capital worth talking about, there are no machinery involved" | ZERO_STANDING |
| Z6 | 52 | 118 | MD | "No challenge — we are well positioned" (procurement, next couple of quarters) | ZERO_STANDING |
| Z7 | 60 | 126 | MD | "I don't think growth will slow down" (implicit zero-deceleration claim, against analyst's observed deceleration from ~40% to ~30%, Q-25/line123) | ZERO_STANDING |

zero_standing total = 7 rows (Z1-Z7).

---
## 6. CROSS-CUTTING FLAGS SUMMARY

- `CONTRADICTION`: N7/N51 (memory price "doubled" vs corrected "five times" since Oct-2025, both spoken by
  MD in the same call); N79 (analyst's "revenue fell almost 37%" vs the +32% revenue growth stated twice by
  management — likely transcription anomaly, needs A3 reconciliation against the filed P&L).
- `NUMBER_DISCREPANCY`: N66 (analyst states other expenses ">65%" YoY at line 93; CFO states 68% at line 94).
- `AMBIGUOUS_FIGURE`: N60 (others ASP given as both "19,300 odd" and "19,326" within the same turn); N64
  (others ASP QoQ change given as "~1.5% better" then "on an overall basis 12%" in the same breath — the
  12% looks like a misplaced restatement of the laptop YoY figure, N58).
  `SILENT_PARTICIPANT`: AJ Pancholi (Director) and Rohit Arora (Strategy & IR) — both named as joining the
  call, neither has an attributed speaking turn.
- `CONFIRMED_BY_MGMT` (qualified): N42, N43, N77, N78 — analyst-computed figures that CFO blanket-affirms
  ("absolutely and directionally correct") without re-stating each rupee/percentage figure individually.
- No `ENTITY_CHANGE`, `DROPPED_SLIDE`, `MGMT_ABSENCE` (CMD/promoter present and highly engaged), or
  verbatim `REPEAT_QUESTION` identified in this transcript.
