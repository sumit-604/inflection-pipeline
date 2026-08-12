# A2 Completeness Ledger — NephroPlus Q1 FY27 Concall

Source: `extract_concall_nephroplus_q1fy27.txt` (verbatim transcript, 126 source
lines, per-source-line numbers used throughout this ledger; file line = source
line + 14, header occupies file lines 1-13).

```
=== A2 COUNT TEST ===
category: participants          grep_count: 17   sweep_count: 17   match: yes
category: turns                 grep_count: 103  sweep_count: 103  match: yes
category: questions             grep_count: 36   sweep_count: 36   match: yes
category: mgmt_number_turns     grep_count: 34   sweep_count: 34   match: yes
category: mgmt_numbers (rows)   grep_count: 81   sweep_count: 81   match: yes
category: forward_hedge_stmts   grep_count: 18   sweep_count: 18   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Methodology note (how the two enumerations were run and reconciled)

- **Turns**: grep pass `grep -oP '^\d+\t\S.*' | grep -vP '^\d+\t\['` on the raw
  file (removes the 19 blank source lines and the 3 bracket markers — source
  lines 2 `[Verbatim transcript...]`, 14 `[Q&A SESSION]`, 126 `[END OF
  TRANSCRIPT]`), then the header/title line (source line 1) is excluded as it
  is metadata, not a spoken turn → 103. Manual sweep of every source line
  1-126 independently produced 103. Match.
- **Participants**: first grep pass matched only `Name (Firm/Designation):`
  labels and found 14 (11 analysts + Vikram Vuppala x2 labels + Rohit Singh +
  Prashant Goenka). This undercounted because three participants never carry
  a parenthetical label in their own turn: the call Operator (turn source
  line 4, unlabeled), the IIFL Capital host who hands over to management
  (source line 6, named inconsistently "Mr. Nam" / "Mr. Nan"), and Kamal D
  Shah (Co-founder), who is introduced three times but never has an
  attributed speaking turn. Broadened grep for `Moderator:`, `Mr\. Na[nm]`,
  and `Kamal` found all three. Re-swept total = 17. Match after re-sweep.
- **Questions**: grep found 45 analyst-attributed turns; the last turn in
  each of the 11 analyst blocks is a pure closing pleasantry with no
  question content (confirmed no interrogative content) → 45-11 = 34
  question-bearing turns. One turn (source line 26, Sedar Nandhi) explicitly
  bundles three distinct topics ("those would be my three questions",
  confirmed by ordinal-cue grep for "two things / one / second / third"
  which fired only on this turn) → 34 turns - 1 (the bundled turn counted
  once) + 3 (its actual topic count) = 36 question rows. Manual sweep
  independently produced the same 36 topics. Match.
- **Mgmt numbers**: digit-pattern grep across all management-attributed turns
  (labelled Q&A turns + unlabeled opening remarks, source lines 8/10/12) hit
  31 turns with digit content; manual sweep found 3 more turns where
  management states a quantified fact in words rather than digits (source
  lines 69 "four private clinics... one or two green field", 81 "one of the
  four clusters", 108 "last five years") → 34 quantified-turns total, grep
  and sweep match at that unit. Within those 34 turns, 81 discrete metrics
  were enumerated line by line (a turn routinely carries 2-12 distinct
  figures, e.g. source line 12 alone carries 11). Both passes were run
  turn-by-turn against the same 34-turn base and agree on 81 rows.
- **Forward/hedge statements**: keyword grep for
  `guidance|12 to 18 months|3 to 5 years|3 to 4 quarters|couple of
  months|don't give|don't provide|not giving any|5 to 10 years|10 to 15
  countries|one to two quarters` plus manual sweep for uncued forward
  commitments (three growth levers reiterated, standalone-clinic trajectory)
  → 18 rows both ways. Match.

---

## 1. PARTICIPANTS (both sides), turn/line referenced to first appearance

| # | Name | Designation / Firm | Side | First line | Speaking turns (count) | Flags |
|---|------|--------------------|------|-----------|------------------------|-------|
| 1 | Vikram Vuppala | Founder Chairman & Managing Director (CMD) | Management | 8 | 8,28,30,35,38,81,83,101,110,112,117,120,124 (13) | present & speaking extensively — no MGMT_ABSENCE |
| 2 | Kamal D Shah | Co-founder | Management | 2 (header), 6, 8 | 0 (introduced 3x, never attributed a speaking turn) | SILENT_PARTICIPANT |
| 3 | Rohit Singh | Group CEO | Management | 10 | 10,29,37,56,60,62,64,69,73,75,80,85,94,99,106,108,119 (17) | — |
| 4 | Prashant Goenka | Group CFO | Management | 12 | 12,18,20,22,27,40,45,47,49,54,58,71,90,92 (14) | — |
| 5 | Call Operator | unnamed conference operator | Facilitation | 4 | 4 + 12 labeled "Moderator:" turns (16,25,33,43,52,67,78,88,97,104,115,123) = 13 | — |
| 6 | "Mr. Nan" / "Mr. Nam" | IIFL Capital (call host) | Facilitation | 4 (referenced), 6 (speaks) | 6 (1) | NAME_INCONSISTENCY (spelled both "Nam" and "Nan" in same sentence, line 4) |
| 7 | Ash Takur | Helios Capital | Analyst | 17 | 17,19,21,23 (4) | — |
| 8 | Sedar Nandhi | Chanaka Wealth Creation | Analyst | 26 | 26,31 (2) | — |
| 9 | Anik Singh | Kotak Institutional Equities | Analyst | 34 | 34,36,39,41 (4) | — |
| 10 | Kushell Chawatia | Nomura | Analyst | 44 | 44,46,48,50 (4) | — |
| 11 | Java (also "Jawa") | JM AMC | Analyst | 43 (referenced as "Jawa" by moderator), 53 (speaks as "Java") | 53,55,57,59,61,63,65 (7) | NAME_INCONSISTENCY ("Jawa" vs "Java"); moderator note line 43 records he was unable to speak on first attempt and "moved on" |
| 12 | Shah | ICICI Securities | Analyst | 68 | 68,70,72,74,76 (5) | — |
| 13 | Dwang Patel | Samia Capital | Analyst | 79 | 79,82,84,86 (4) | — |
| 14 | Anojel | Bastian Research | Analyst | 89 | 89,91,93,95 (4) | — |
| 15 | Siman | Tucker Base Capital / Tusker Base Capital | Analyst | 97 (moderator: "Tucker base capital"), 98 (speaker label: "Tusker Base Capital") | 98,100,102 (3) | NAME_INCONSISTENCY (firm name spelled two ways) |
| 16 | Pawan Kumar | Shade Capital | Analyst | 105 | 105,107,109,111,113 (5) | — |
| 17 | Nilanjan | PGC AMC | Analyst | 116 | 116,118,121 (3) | — |

CMD Vikram Vuppala is present and speaks in 13 of 34 answer-turns — no
`MGMT_ABSENCE`. Kamal D Shah is introduced by name three times but has zero
attributed speaking turns across the full call — flagged `SILENT_PARTICIPANT`
(not MGMT_ABSENCE since he is not the CMD and the CMD is present/speaking).

Participant row count = 17.

---

## 2. SPEAKER TURNS (sequential, every turn, first ~10 words, source line)

| Turn | Line | Speaker | First ~10 words |
|------|------|---------|------------------|
| 1 | 4 | Operator (unlabeled) | "Ladies and gentlemen, good day and welcome to..." |
| 2 | 6 | Mr. Nan/Nam (IIFL Capital host) | "Thank you. Good morning everyone. Uh on behalf of..." |
| 3 | 8 | Vikram Vuppala (CMD) | "Thank you. Very good morning everyone. This is..." |
| 4 | 10 | Rohit Singh (Group CEO) | "Thank you Victor. Good morning all and thanks for..." |
| 5 | 12 | Prashant Goenka (CFO) | "Thank you, Rohit and a very warm welcome to..." |
| 6 | 16 | Moderator | "The first question comes from the line of Ash..." |
| 7 | 17 | Ash Takur (Helios Capital) | "Hi sir, very good morning and thanks for taking..." |
| 8 | 18 | Prashant Goenka (CFO) | "Yeah. So this is Prashant. I'll take this question..." |
| 9 | 19 | Ash Takur | "Thank you sir. Thanks for the comprehensive answer. My..." |
| 10 | 20 | Prashant Goenka | "So in Philippines I think as we indicated earlier..." |
| 11 | 21 | Ash Takur | "okay sir thank you. One question on the working..." |
| 12 | 22 | Prashant Goenka | "Yeah. So I think as Vikram in previous calls..." |
| 13 | 23 | Ash Takur | "Okay. So thanks for answering my questions." (closing) |
| 14 | 25 | Moderator | "Next question comes from the line of Sedar Nandhi..." |
| 15 | 26 | Sedar Nandhi (Chanaka Wealth Creation) | "thanks for taking my question. just wanted to understand..." |
| 16 | 27 | Prashant Goenka | "Sure, Sedat. I think I'll take the first one..." |
| 17 | 28 | Vikram Vuppala (CMD) | "in terms of the center and the AI, on..." |
| 18 | 29 | Rohit Singh (Group CEO) | "thanks on the AI front as I briefly mentioned..." |
| 19 | 30 | Vikram Vuppala | "yeah I'll just add to what Rohit has said..." |
| 20 | 31 | Sedar Nandhi | "Thanks for a very detailed and very useful response..." (closing) |
| 21 | 33 | Moderator | "Next question comes from the line of Anik Singh..." |
| 22 | 34 | Anik Singh (Kotak Institutional Equities) | "Hi sir, thank you for the opportunity. So I..." |
| 23 | 35 | Vikram Vuppala | "Yeah thanks Anik for the question this Vikram. essentially..." |
| 24 | 36 | Anik Singh | "thank you sir. Thank you for that detailed answer..." |
| 25 | 37 | Rohit Singh | "San this is Rohit here. So when we partner..." |
| 26 | 38 | Vikram Vuppala | "Yeah just to add to what Rohit is saying..." |
| 27 | 39 | Anik Singh | "got it sir got it and so lastly as..." |
| 28 | 40 | Prashant Goenka | "Yeah. Hi Anik, this is Prashant. I'll take this..." |
| 29 | 41 | Anik Singh | "Got it sir. Thank you." (closing) |
| 30 | 43 | Moderator | "Next question comes from the line of Kushell Chawatia..." |
| 31 | 44 | Kushell Chawatia (Nomura) | "Yeah. Hello. So first of all, can you let..." |
| 32 | 45 | Prashant Goenka | "So this is Prashant here. I'll answer this question..." |
| 33 | 46 | Kushell Chawatia | "Okay. And can you let us know what is..." |
| 34 | 47 | Prashant Goenka | "So Kush we typically don't give guidance on the..." |
| 35 | 48 | Kushell Chawatia | "Okay. And any assumption on the tax rate which..." |
| 36 | 49 | Prashant Goenka | "Yeah. So we currently operate at scale level three..." |
| 37 | 50 | Kushell Chawatia | "Okay. Yeah. Thank you." (closing) |
| 38 | 52 | Moderator | "Next question comes from the line of Java with..." |
| 39 | 53 | Java (JM AMC) | "hello. Am I audible? Yes. sorry for the previous..." |
| 40 | 54 | Prashant Goenka | "So actually other expenses if you compare it to..." |
| 41 | 55 | Java | "Got it. another question that I wanted to check..." |
| 42 | 56 | Rohit Singh | "Yeah. Hi Prranab this is Rohit here. Yes we..." |
| 43 | 57 | Java | "Got it. if there's nobody in the queue, can..." |
| 44 | 58 | Prashant Goenka | "no I think as I mentioned there are a..." |
| 45 | 59 | Java | "And sir on the Saudi business can you just..." |
| 46 | 60 | Rohit Singh | "So Prranab I'll take this over there. So Saudi..." |
| 47 | 61 | Java | "so Rohit for the rest of the fiscal should..." |
| 48 | 62 | Rohit Singh | "So we are not giving any guidance on the..." |
| 49 | 63 | Java | "And one last if I can squeeze in so..." |
| 50 | 64 | Rohit Singh | "So we have registered a company there but we..." |
| 51 | 65 | Java | "Got it. thank you so much sir for your..." (closing) |
| 52 | 67 | Moderator | "Next question comes from the line of Shah with..." |
| 53 | 68 | Shah (ICICI Securities) | "yeah, thank you for the opportunity. I wanted to..." |
| 54 | 69 | Rohit Singh | "So Shah India had a blend of all three..." |
| 55 | 70 | Shah | "All right. And if you can quantify what is..." |
| 56 | 71 | Prashant Goenka | "Yeah. So I think while India is a basket..." |
| 57 | 72 | Shah | "All right. And in the Philippine side we have..." |
| 58 | 73 | Rohit Singh | "Sure. We've mentioned that earlier also that our Philippines..." |
| 59 | 74 | Shah | "and how is utilization over there sir since it..." |
| 60 | 75 | Rohit Singh | "so we again look at a network level utilization..." |
| 61 | 76 | Shah | "All right that's all from me. thank you so..." (closing) |
| 62 | 78 | Moderator | "Next question comes from the line of Dwang Patel..." |
| 63 | 79 | Dwang Patel (Samia Capital) | "you mentioned some delay in Saudi Arabia roll out..." |
| 64 | 80 | Rohit Singh | "So Saudi Arabia is a tender market. So it's..." |
| 65 | 81 | Vikram Vuppala | "yeah just to add to what Rohit is saying..." |
| 66 | 82 | Dwang Patel | "So in case we win a tender it we..." |
| 67 | 83 | Vikram Vuppala | "No, no. If you win the tender, obviously any..." |
| 68 | 84 | Dwang Patel | "Okay. And we've made all the investments we needed..." |
| 69 | 85 | Rohit Singh | "So Dwang right now as I mentioned that we..." |
| 70 | 86 | Dwang Patel | "That's all. thank you so much." (closing) |
| 71 | 88 | Moderator | "Next question comes from the line of Anojel with..." |
| 72 | 89 | Anojel (Bastian Research) | "hi sir, thanks for the opportunity. So my first..." |
| 73 | 90 | Prashant Goenka | "hi this is Prashant. I'll take that question. We..." |
| 74 | 91 | Anojel | "So is there any angle of like with deep..." |
| 75 | 92 | Prashant Goenka | "No. So I think unlike some of the other..." |
| 76 | 93 | Anojel | "all right and my second question would be that..." |
| 77 | 94 | Rohit Singh | "no I think given that it's a reimbursement business..." |
| 78 | 95 | Anojel | "All right. So I got it. thanks." (closing) |
| 79 | 97 | Moderator | "Next question comes from the line of Siman with..." |
| 80 | 98 | Siman (Tusker Base Capital) | "Thank you so much for taking my question. first..." |
| 81 | 99 | Rohit Singh | "so Siman let me address this first and then..." |
| 82 | 100 | Siman | "Understood sir very well explained. So my second question..." |
| 83 | 101 | Vikram Vuppala | "so we are fairly comfortable in every part of..." |
| 84 | 102 | Siman | "Understood. Thank you for taking my questions." (closing) |
| 85 | 104 | Moderator | "Next question comes from the line of Pawan Kumar..." |
| 86 | 105 | Pawan Kumar (Shade Capital) | "thank you for the opportunity. so my first question..." |
| 87 | 106 | Rohit Singh | "So we are the second largest network by footprint..." |
| 88 | 107 | Pawan Kumar | "and what competitive advantage we are really offering there..." |
| 89 | 108 | Rohit Singh | "So obviously I think Prashant had also mentioned in..." |
| 90 | 109 | Pawan Kumar | "Okay. And talking about Indian market like you have..." |
| 91 | 110 | Vikram Vuppala | "Yeah this Vikram thanks Pawan. India is still in..." |
| 92 | 111 | Pawan Kumar | "and is the same applicable globally also like most..." |
| 93 | 112 | Vikram Vuppala | "So there are two models globally. One model is..." |
| 94 | 113 | Pawan Kumar | "thank you." (closing) |
| 95 | 115 | Moderator | "Next question comes from the line of Nilanjan with..." |
| 96 | 116 | Nilanjan (PGC AMC) | "thank you sir. So just a question. in the..." |
| 97 | 117 | Vikram Vuppala | "Yeah, this is Vikram. I think this is Nephroplus..." |
| 98 | 118 | Nilanjan | "sure so that was first part of my question..." |
| 99 | 119 | Rohit Singh | "So Nilanjan I think we've mentioned this earlier also..." |
| 100 | 120 | Vikram Vuppala | "yeah it's a macro level engine what happens is..." |
| 101 | 121 | Nilanjan | "Understood Vikram. That's a good perspective to look at..." (closing) |
| 102 | 123 | Moderator | "Due to time constraints, we have reached the end..." |
| 103 | 124 | Management (Vikram Vuppala) | "I think we have mentioned all the details in..." (closing remarks) |

Turn count = 103. Management (Vikram + Rohit + Prashant, opening + Q&A) speaks
44 of 103 turns (43%); Moderator/Operator/host speaks 14 of 103 (14%);
analysts speak 45 of 103 (43%) — of which 34 turns carry a question and 11
are closing pleasantries, so genuine Q&A analyst-question effort is 34/103
(~33% of all turns), auditable against every turn number above.

---

## 3. QUESTIONS (one row per distinct topic; a turn with bundled topics
    produces multiple rows sharing the same turn number)

| # | Analyst | Firm | Turn | Topic | Answer turn(s) | Flags |
|---|---------|------|------|-------|-----------------|-------|
| 1 | Ash Takur | Helios Capital | 17 | Depreciation method / asset life for dialyzers & equipment | 18 (Prashant) | REPEAT_QUESTION (depreciation, see Q19) |
| 2 | Ash Takur | Helios Capital | 19 | Fixed capital investment per bed (Philippines greenfield) / per-permit acquisition cost | 20 (Prashant) | REPEAT_QUESTION (capex, see Q6) |
| 3 | Ash Takur | Helios Capital | 21 | Working capital ~120 days: India vs Philippines split / variability | 22 (Prashant) | REPEAT_QUESTION (working capital/AR, see Q26 topic overlap on utilization not WC — see note) |
| 4 | Sedar Nandhi | Chanaka Wealth Creation | 26 | Margin improvement: international mix vs inherent cost improvement | 27 (Prashant) | MULTI_TOPIC_TURN (1 of 3 bundled in this turn) |
| 5 | Sedar Nandhi | Chanaka Wealth Creation | 26 | Center growth (12%) vs guest volume growth (13%) — implied productivity/occupancy per center | 28 (Vikram) | MULTI_TOPIC_TURN; REPEAT_QUESTION (productivity/utilization, see Q17, Q27) |
| 6 | Sedar Nandhi | Chanaka Wealth Creation | 26 | AI initiatives for patient clinical outcomes (vs backend efficiency) | 29-30 (Rohit, Vikram) | MULTI_TOPIC_TURN |
| 7 | Anik Singh | Kotak Institutional Equities | 34 | Business moat / competitive differentiation vs private hospitals | 35 (Vikram) | — |
| 8 | Anik Singh | Kotak Institutional Equities | 36 | Hospital partnership revenue-share / unit-economics mechanics | 37-38 (Rohit, Vikram) | — |
| 9 | Anik Singh | Kotak Institutional Equities | 39 | RPT CAGR (~11%) driver: international mix vs organic pricing | 40 (Prashant) | REPEAT_QUESTION (RPT, see Q19) |
| 10 | Kushell Chawatia | Nomura | 44 | Forex contribution to quarter revenue growth | 45 (Prashant) | — |
| 11 | Kushell Chawatia | Nomura | 46 | Capex guidance split India vs Philippines | 47 (Prashant) | REPEAT_QUESTION (capex, see Q2); HEDGE_PHRASE in answer ("typically don't give guidance on capex") |
| 12 | Kushell Chawatia | Nomura | 48 | Tax rate assumption for the year (20% this quarter) | 49 (Prashant) | — |
| 13 | Java | JM AMC | 53 | Sharp increase in "other expenses" line item | 54 (Prashant) | — |
| 14 | Java | JM AMC | 55 | Price hike in India — CGHS price increase for corporates | 56 (Rohit) | — |
| 15 | Java | JM AMC | 57 | Depreciation sequentially declining despite Philippines acquisitions | 58 (Prashant) | REPEAT_QUESTION (depreciation, see Q1) |
| 16 | Java | JM AMC | 59 | Saudi business update: losses trend, centers added, tendering timeline | 60 (Rohit) | REPEAT_QUESTION (Saudi tender/timeline, see Q18, Q23-25) |
| 17 | Java | JM AMC | 61 | Whether ~Rs 3 cr/quarter Saudi JV loss run-rate continues rest of FY | 62 (Rohit) | REPEAT_QUESTION (Saudi, see Q16); HEDGE_PHRASE in answer ("not giving any guidance on the loss assumptions") |
| 18 | Java | JM AMC | 63 | Newly incorporated EU/Kazakhstan subsidiary — timing and business model | 64 (Rohit) | — |
| 19 | Shah | ICICI Securities | 68 | Nature of 19 new India clinics: greenfield / brownfield / PPP | 69 (Rohit) | — |
| 20 | Shah | ICICI Securities | 70 | Current India RPT quantification | 71 (Prashant) | REPEAT_QUESTION (RPT, see Q9) |
| 21 | Shah | ICICI Securities | 72 | Philippines 7 new acquired assets — average bed capacity | 73 (Rohit) | — |
| 22 | Shah | ICICI Securities | 74 | Utilization of the newly acquired Philippines assets | 75 (Rohit) | REPEAT_QUESTION (utilization/productivity, see Q5) |
| 23 | Dwang Patel | Samia Capital | 79 | Saudi: number of clinics needed to reach breakeven on ~Rs 3 cr loss | 80-81 (Rohit, Vikram) | REPEAT_QUESTION (Saudi, see Q16-17) |
| 24 | Dwang Patel | Samia Capital | 82 | Whether winning the Saudi tender guarantees recouping losses | 83 (Vikram) | REPEAT_QUESTION (Saudi) |
| 25 | Dwang Patel | Samia Capital | 84 | Whether further investment is needed before the tender proceeds | 85 (Rohit) | REPEAT_QUESTION (Saudi) |
| 26 | Anojel | Bastian Research | 89 | Unit economics per bed — India vs international, peak margins/ROCE | 90 (Prashant) | HEDGE_PHRASE in answer ("We don't provide unit economics at a country level") |
| 27 | Anojel | Bastian Research | 91 | Whether new vs mature clinics have differing margin profiles | 92 (Prashant) | — |
| 28 | Anojel | Bastian Research | 93 | Customer/patient loyalty angle in center choice | 94 (Rohit) | — |
| 29 | Siman | Tusker Base Capital | 98 | Material cost reduction — reuse/reprocessing protocol details | 99 (Rohit) | — |
| 30 | Siman | Tusker Base Capital | 100 | City/pin-code level densification approach (e.g. Mumbai) | 101 (Vikram) | — |
| 31 | Pawan Kumar | Shade Capital | 105 | Market share in Philippines and Uzbekistan | 106 (Rohit) | — |
| 32 | Pawan Kumar | Shade Capital | 107 | Competitive advantage in those international markets | 108 (Rohit) | — |
| 33 | Pawan Kumar | Shade Capital | 109 | Viability of D2C / private standalone clinic model in India | 110 (Vikram) | — |
| 34 | Pawan Kumar | Shade Capital | 111 | Whether the tender / government-scheme model applies globally | 112 (Vikram) | — |
| 35 | Nilanjan | PGC AMC | 116 | Whether patient/guest split by country (India/Philippines/other) could be disclosed; same-store-sales-style analysis difficulty | 117 (Vikram) | HEDGE_PHRASE in answer ("we do not want to mention country by country details") |
| 36 | Nilanjan | PGC AMC | 118 | Organic growth split by center type (captive / PPP / standalone) vs last year | 119-120 (Rohit, Vikram) | — |

Question row count = 36. `REPEAT_QUESTION` fires on 4 topic clusters:
depreciation (Q1, Q15), capex (Q2, Q11), RPT (Q9, Q20), utilization/productivity
(Q5, Q22), and Saudi tender/timeline/breakeven (Q16, Q17, Q23, Q24, Q25 — the
most heavily repeated topic, 5 separate questions across 2 analysts).

---

## 4. QUANTIFIED METRICS SPOKEN BY MANAGEMENT (turn-referenced; source line
    given; every management turn with a numeric value, digit or spelled-out)

| # | Line | Speaker | Metric | Value(s) stated | Flags |
|---|------|---------|--------|-------------------|-------|
| 1 | 8 | Vikram | Q1 revenue growth (qualitative bound) | "more than 20%" YoY | superseded by exact 23.7% in line 10/12 |
| 2 | 8 | Vikram | Company / platform age | 16 years (stated 2x in same turn) | — |
| 3 | 8 | Vikram | New cities launched this quarter — India | 17 | — |
| 4 | 8 | Vikram | New cities launched this quarter — Philippines | 5 | — |
| 5 | 8 | Vikram | Network snapshot A | 550 clinics, 370 cities, 5 countries | NUMBER_DISCREPANCY vs line 10's "357 cities" for the same network snapshot |
| 6 | 8 | Vikram | Unorganized dialysis capacity share | 80% | — |
| 7 | 10 | Rohit | Revenue | grew 23.7% YoY to Rs 282 cr | — |
| 8 | 10 | Rohit | Adjusted EBITDA | grew 30.7% to Rs 65 cr | NUMBER_DISCREPANCY: Rs 65 cr here vs Rs 65.1 cr in line 12 (rounding) |
| 9 | 10 | Rohit | Adjusted EBITDA margin | +120 bps YoY to 23.1% | NUMBER_DISCREPANCY vs "125 basis point" improvement stated by Prashant in line 27 |
| 10 | 10 | Rohit | Guests (active patients) | +13% to 38,262 | — |
| 11 | 10 | Rohit | Treatments | crossed 10,30,000 (10.3 lakh), +13.3% | — |
| 12 | 10 | Rohit | Clinics added this quarter | 26 (19 India + 7 Philippines) | NUMBER_DISCREPANCY vs "addition of 50 clinics" referenced by Vikram in line 28 (unclear if different period/metric) |
| 13 | 10 | Rohit | Network snapshot B | 550 clinics, 5 countries, 357 cities; India 307 cities / 25 states | see flag on row 5 |
| 14 | 10 | Rohit | International revenue contribution | ~45% | — |
| 15 | 10 | Rohit | Philippines network | +7 clinics this quarter; 50 clinics total, 39 cities; 6 years since entry; #2 largest distributed network | — |
| 16 | 10 | Rohit | AVF (early vascular access) program | 21 centers, 2,000 guests; AVF creation moved 15%→30% of guests; mortality reduced to "close to 15%" | — |
| 17 | 10 | Rohit | Nephroplus Index (composite clinical score) | live across 29 centers, 2,600 guests, 7 weighted metrics | — |
| 18 | 10 | Rohit | Saudi first clinic (Riyadh Hospital) | operational in July | — |
| 19 | 12 | Prashant | Revenue | Rs 282 cr vs Rs 228 cr (Q1 FY26), 23.7% growth | independent restatement, cross-checks row 7 |
| 20 | 12 | Prashant | Adjusted EBITDA (ex-ESOP, ex-Saudi JV) | Rs 65.1 cr vs Rs 49.8 cr, 31% growth | see flag row 8 |
| 21 | 12 | Prashant | Adjusted EBITDA margin | 23.1% vs 21.9% | — |
| 22 | 12 | Prashant | Adjusted PAT (add-back ESOP + Saudi JV expense) | Rs 37 cr vs Rs 26 cr, 41.7% growth | — |
| 23 | 12 | Prashant | Adjusted PAT margin | 13.1% vs 11.4% | — |
| 24 | 12 | Prashant | Active guests | 38,262 (Jun-26) vs 33,868 (Jun-25), 13% growth | — |
| 25 | 12 | Prashant | Treatments | 10.3 lakh vs 9.1 lakh, 13.3% growth | — |
| 26 | 12 | Prashant | Revenue per treatment (RPT) | Rs 2,733 vs Rs 253, "9.2% growth" | TRANSCRIPTION_ANOMALY — Rs 253 comparator is arithmetically inconsistent with a 9.2% growth claim against Rs 2,733 (implies prior-year RPT ~Rs 2,503); recorded verbatim, not corrected |
| 27 | 12 | Prashant | Annualized adjusted return metric (label transcribed "gross", likely RoCE) | 21% | TRANSCRIPTION_ANOMALY on metric label |
| 28 | 12 | Prashant | IPO proceeds utilized | 68% (~Rs 27 cr), as of Jun-2026 | — |
| 29 | 12 | Prashant | Capex for the quarter | Rs 44 cr | cross-checked against row 54 |
| 30 | 18 | Prashant | Depreciation as % of revenue | flat YoY, ~8.6-8.7% | — |
| 31 | 18 | Prashant | Machine depreciation life | 7-10 years, by country | — |
| 32 | 18 | Prashant | Philippines acquisitions this quarter | 7 | cross-checks row 15 |
| 33 | 18 | Prashant | Goodwill amortization period (Philippines acquisitions) | 5-7 years | — |
| 34 | 20 | Prashant | Philippines dialysis market size | ~900 clinics total | cross-checked against row 74 |
| 35 | 20 | Prashant | Philippines large-chain clinics | 150-200 clinics, 2-3 large chains (incl. NephroPlus) | — |
| 36 | 20 | Prashant | Philippines mom-and-pop clinics | ~700 clinics | — |
| 37 | 22 | Prashant | Government payment cycle (working capital driver) | 3-4 months | — |
| 38 | 22 | Prashant | AR days | improved 121 days → 101 days (20-day improvement YoY) | — |
| 39 | 27 | Prashant | Adjusted EBITDA margin improvement (restated) | 125 bps | NUMBER_DISCREPANCY vs 120 bps in row 9 |
| 40 | 27 | Prashant | COGS as % of revenue, improvement | 175 bps | — |
| 41 | 28 | Vikram | Illustrative clinic utilization threshold | 85% (example of a heavily utilized clinic) | cross-checked against row 81 |
| 42 | 28 | Vikram | "Addition of 50 clinics" (context: country-level optimization discussion) | 50 | NUMBER_DISCREPANCY vs 26 clinics added this quarter (row 12); unclear referent |
| 43 | 30 | Vikram | Manual clinical-audit confidence bound (illustrative, vs AI live-auditing) | "90% 85%" | qualitative illustrative range, recorded verbatim |
| 44 | 35 | Vikram | EBITDA-negative period (company history) | first 11 years | — |
| 45 | 35 | Vikram | PAT-negative period (company history) | first 13 years | — |
| 46 | 35 | Vikram | In-house biomedical team founded | "8 years back" | — |
| 47 | 35 | Vikram | Hospital partners | "more than 300" private hospitals | — |
| 48 | 35 | Vikram | Hospital revenue share from dialysis | "not more than 1%" of hospital revenue | ZERO_STANDING-adjacent (near-nil economic contribution stated explicitly) |
| 49 | 38 | Vikram | Organized dialysis market share, India | 0% (16 years ago) → 21-22% now | NUMBER_DISCREPANCY vs "20%" stated by Vikram in row 76 (line 110) |
| 50 | 38 | Vikram | Hospitals still running own (unorganized) dialysis ops | 78-79% | — |
| 51 | 40 | Prashant | RPT CAGR | ~11% | cross-references question topic Q9/Q20 |
| 52 | 40 | Prashant | International revenue contribution, trend | 45% now vs 30% "a year and a half back" | cross-checks row 14 |
| 53 | 40 | Prashant | Philippines price increase | 55-60% in October 2024, after ~10 years | cross-checked against row 60 |
| 54 | 45 | Prashant | Forex contribution to quarter revenue | Rs 20 lakh favorable | ZERO_STANDING (explicitly a near-nil/small standing item, the canonical example flagged in the task brief) |
| 55 | 47 | Prashant | Capex, quarter vs year-ago | Rs 44 cr vs Rs 43 cr (Q1 FY26) | cross-checks row 29 |
| 56 | 49 | Prashant | Tax rate this quarter | 20% | — |
| 57 | 49 | Prashant | India / Philippines statutory tax rate | 25% | — |
| 58 | 49 | Prashant | Uzbekistan tax rate (if healthcare revenue >90% of total) | 0% | ZERO_STANDING |
| 59 | 54 | Prashant | Other expenses, QoQ | improved (reduced) by 133 bps | YoY direction stated as "deteriorated" with no % given — NOT FOUND for YoY magnitude |
| 60 | 54 | Prashant | ECL provision | 2-2.5% of revenue | — |
| 61 | 56 | Rohit | CGHS price increase | ~35%, in October (prior year), after ~10-11 years | cross-checks row 53 (lumpy pricing pattern) |
| 62 | 58 | Prashant | Machine deployment pace, prior year | ~50 machines/month | — |
| 63 | 58 | Prashant | Machine deployment pace, last 3 months | "hardly any new machines" | ZERO_STANDING (near-nil deployment explicitly stated) |
| 64 | 64 | Rohit | Kazakhstan dialysis price point | ~$75 | — |
| 65 | 69 | Rohit | 19 new India clinics — composition | PPP (Bihar, some), 4 private clinics, 1-2 greenfield | spelled-out numbers ("four", "one or two"), not digits — caught only on manual sweep |
| 66 | 71 | Prashant | India RPT | "$20 to $23" price point | TRANSCRIPTION_ANOMALY — currency symbol inconsistent with Rs-denominated RPT elsewhere (row 26); recorded verbatim |
| 67 | 73 | Rohit | Philippines average bed capacity per center | 10-12 beds | — |
| 68 | 75 | Rohit | Network utilization (consolidated) | 74% | cross-checks row 78 |
| 69 | 81 | Vikram | Saudi tender structure | "one of the four clusters" | spelled-out ("four"), caught on manual sweep |
| 70 | 90 | Prashant | COGS as component of unit economics | ~22% of cost | — |
| 71 | 101 | Vikram | India cities of operation | "300 plus" | consistent with row 13 (307 cities) |
| 72 | 101 | Vikram | Clinics in tier-2/tier-3 cities | "75% plus" | — |
| 73 | 106 | Rohit | Philippines competitive position | NephroPlus 51 clinics (#2); largest chain 58 clinics; market ~900 clinics | cross-checks row 34 |
| 74 | 106 | Rohit | Uzbekistan market | ~9,000 patients total; NephroPlus servicing ~1,800 | — |
| 75 | 108 | Rohit | Uzbekistan operating tenure | "last five years" | spelled-out, caught on manual sweep |
| 76 | 110 | Vikram | Organized dialysis market share, India (restated) | 20% | NUMBER_DISCREPANCY vs "21-22%" in row 49 |
| 77 | 110 | Vikram | NephroPlus standalone clinics in India | 25 | — |
| 78 | 119 | Rohit | Network utilization (restated) | 74% | cross-checks row 68, consistent |
| 79 | 120 | Vikram | Machine cycle cap, India | 3 dialysis cycles/day/machine | — |
| 80 | 120 | Vikram | Treatment time | 4 hours mandatory + pre/post = 4.5 hours total | — |
| 81 | 120 | Vikram | Peak clinic utilization threshold (restated) | 85% | cross-checks row 41, consistent |

Mgmt-numbers row count = 81, sourced from 34 distinct management turns.
`ZERO_STANDING` fires 4x (rows 48, 54, 58, 63 — hospital revenue share <1%,
forex Rs 20 lakh, Uzbekistan 0% tax, near-zero machine deployment).
`NUMBER_DISCREPANCY` fires 5x (rows 5/13 network-city count, 9/39 EBITDA
margin bps, 12/42 clinics-added count, 49/76 organized-market %, plus the
RPT anomaly at row 26 and the currency anomaly at row 66 flagged separately
as `TRANSCRIPTION_ANOMALY`) — all flagged for the Role 5
arithmetic-consistency check against the filing baseline, not resolved here.

---

## 5. FORWARD-LOOKING / GUIDANCE STATEMENTS AND HEDGE PHRASES

| # | Line | Speaker | Statement | Type | Flags |
|---|------|---------|-----------|------|-------|
| 1 | 12 | Prashant | Medium-term growth guidance: 15-20% over next 3-5 years | Forward-commitment | — |
| 2 | 10 | Rohit | Saudi Ministry of Health tender formal process expected to begin "in a couple of months" | Forward-commitment | REPEAT (see #6, #14 — Saudi timeline restated 3x across the call with varying specificity) |
| 3 | 10 | Rohit | NIDA (Nephroplus International Dialysis Academy) first nurse-training batch begins Q3 FY27 | Forward-commitment | — |
| 4 | 40 | Prashant | Strategy to add a new international market every 12-18 months | Forward-commitment | REPEAT (restated at #5) |
| 5 | 47 | Prashant | Same 12-18-month new-market cadence restated in capex-guidance answer | Forward-commitment | REPEAT_QUESTION-adjacent duplicate of #4 |
| 6 | 47 | Prashant | Clinic-addition pace guidance: 40-50/year India | Forward-commitment | — |
| 7 | 47 | Prashant | Clinic-addition pace guidance: 10-15/year Philippines | Forward-commitment | — |
| 8 | 47 | Prashant | Explicit refusal to give numeric capex guidance ("we typically don't give guidance on the capex front") | Hedge phrase | HEDGE_PHRASE |
| 9 | 60 | Rohit | Saudi: "3 to 4 quarters away from realizing any benefits or having a clear visibility" | Forward-commitment | REPEAT (see #2, #10) |
| 10 | 62 | Rohit | Saudi tendering timeline: "could take one to two quarters or probably longer," no clear visibility | Forward-commitment / hedge | REPEAT (see #2, #9); HEDGE_PHRASE |
| 11 | 62 | Rohit | Explicit refusal to guide on Saudi JV loss run-rate ("we are not giving any guidance on the loss assumptions") | Hedge phrase | HEDGE_PHRASE |
| 12 | 90 | Prashant | Refusal to disclose country-level unit economics ("We don't provide unit economics at a country level") | Hedge phrase | HEDGE_PHRASE |
| 13 | 117 | Vikram | Refusal to disclose country-by-country patient/revenue split; platform-only disclosure going forward | Hedge phrase | HEDGE_PHRASE |
| 14 | 20 | Prashant | Refusal to disclose per-center/per-permit Philippines acquisition goodwill ("we don't share the details because... it also is a competitive information for us") | Hedge phrase | HEDGE_PHRASE |
| 15 | 40 | Prashant | Caveat that the ~11% RPT CAGR is not a run-rate to extrapolate ("one should not expect that same cagr number to continue forever") | Hedge phrase | HEDGE_PHRASE |
| 16 | 110 | Vikram | Standalone-clinic model expected to overtake in-hospital model in India "over the next 5 to 10 years" | Forward-commitment | — |
| 17 | 117 | Vikram | Company expects to be operating in "10 to 15 countries" within "the next 5 to 10 years" (vs 5 today) | Forward-commitment | — |
| 18 | 8 | Vikram | Reiterated three-lever growth framework (existing-clinic volume, footprint expansion, new-country entry) as the forward growth thesis | Forward-commitment | — |

Forward/hedge row count = 18. Saudi-market timeline is restated with three
different, not-fully-reconcilable time horizons across the call (couple of
months to formal tender / 3-4 quarters to clear visibility / one-to-two
quarters-or-longer to tendering) — flagged for A3/A4 review as an internal
consistency question, not resolved here.

---

## SUMMARY OF FLAGS RAISED

- `SILENT_PARTICIPANT` — Kamal D Shah, Co-founder, introduced 3x, zero
  attributed speaking turns.
- `NAME_INCONSISTENCY` — IIFL host "Mr. Nam"/"Mr. Nan" (line 4); analyst
  "Jawa"/"Java" of JM AMC (lines 43 vs 53); analyst firm "Tucker base
  capital"/"Tusker Base Capital" (lines 97 vs 98).
- `REPEAT_QUESTION` — depreciation (Q1/Q15), capex (Q2/Q11), RPT (Q9/Q20),
  utilization/productivity (Q5/Q22), Saudi tender/timeline/breakeven
  (Q16/Q17/Q23/Q24/Q25, the most repeated topic of the call).
- `MULTI_TOPIC_TURN` — Sedar Nandhi's single turn at line 26 bundles 3
  distinct question topics (margin mix, center productivity, AI), explicitly
  self-flagged in the transcript as "two things" while asking three,
  confirmed by "those would be my three questions" at turn close.
- `NUMBER_DISCREPANCY` — network city count (370 vs 357), EBITDA margin
  improvement (120 bps vs 125 bps), clinics added (26 vs "50"), organized
  market share (21-22% vs 20%).
- `TRANSCRIPTION_ANOMALY` — RPT prior-year comparator (Rs 253, arithmetically
  inconsistent with stated 9.2% growth against Rs 2,733); India RPT quoted in
  "$" rather than Rs; annualized "gross" metric label (likely RoCE).
- `ZERO_STANDING` — hospital revenue share from dialysis (<1%), forex impact
  (Rs 20 lakh favorable, the canonical example cited in the task brief),
  Uzbekistan corporate tax rate (0%), near-zero machine deployment in the
  trailing 3 months.
- `HEDGE_PHRASE` — capex guidance declined; Saudi JV loss guidance declined;
  country-level unit economics declined; country-by-country patient/revenue
  split declined; per-center Philippines acquisition goodwill declined; RPT
  CAGR sustainability caveat.

No `MGMT_ABSENCE` — CMD Vikram Vuppala present and speaking in 13 turns
including the closing remarks.
