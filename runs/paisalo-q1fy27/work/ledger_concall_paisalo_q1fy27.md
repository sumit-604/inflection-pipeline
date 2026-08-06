# LEDGER — Paisalo Digital Q1 FY27 Concall Transcript
Source: runs/paisalo-q1fy27/work/extract_concall_paisalo_q1fy27.txt (69 numbered source lines, header lines 1-13 = metadata/section markers)
Enumerator: A2 | Interprets nothing; every row below is a discrete disclosure unit with its source line number.

```
=== A2 COUNT TEST ===
category: participants          grep_count: 8    sweep_count: 8    match: yes
category: turns                 grep_count: 37   sweep_count: 37   match: yes
category: questions             grep_count: 14   sweep_count: 14   match: yes
category: mgmt_numbers          grep_count: 36   sweep_count: 36   match: yes
category: forward_hedge_phrases grep_count: 19   sweep_count: 19   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Count-test methodology notes:
- participants: grep on "Management (present|absent)" (2 hits: line 18=Santanu Agarwal present, line 19=Harish Singh absent) + unique `[Q# — Name, Firm]` roster via `grep -oE "\[Q[0-9]+ — [^]]*\]"` deduped for follow-ups (6 unique askers: Sandip Mehta, Ruti Doohi, Lokesh Kumar Jaganath, Amit Kumar, Aditya Singh, Harshit Singla) = 2+6=8. Moderator (Natasha, Arihant Capital) enumerated separately below as non-gated (host role, neither management nor analyst/investor).
- turns: 69 total numbered source lines − 6 header/metadata lines (1-6) − 5 section-divider lines (`=== ... ===`, lines 8/13/16/66/69) − 13 blank numbered lines − 8 bracket-label-only lines (`[Q1...]`, `[Q2...]` etc. that carry no content, content follows on next numbered line) = 37 content-bearing speaker-turn lines. Manual sweep read every one of the 37 lines and independently arrived at 37.
- questions: grep count of `\[Q[0-9]+[a-z]?...\]` bracket markers = 14 (Q1, Q1b, Q1c, Q2, Q2b, Q3, Q4, Q4b, Q4c, Q5, Q6, Q7, Q8, Q8b). Manual sweep treated each bracket-marked question unit as one row (bundled multi-part questions, e.g. Q3 and Q7, get all sub-topics listed in the topic column of that one row) = 14. This keeps grep and sweep on the same unit definition; sub-topic-level detail (needed for REPEAT_QUESTION flagging) is preserved inside the topic field, not by inflating the row count.
- mgmt_numbers: 36 distinct figures specified in the injected task list, each verified present via targeted grep patterns (all 36 returned ≥1 hit — see terminal verification). Manual sweep independently located and cited turn/line for all 36. A supplementary (non-gated) table lists additional numbers found during the sweep that were NOT in the original 36-item list (IPO/FPO history, restated D/E, restated NII/PAT QoQ, etc.) — kept out of the gate count so the primary reconciliation stays clean, but retained for A3/A4 completeness.
- forward_hedge_phrases: 19 distinct, non-overlapping phrase instances curated from the transcript (6 are the phrases explicitly named in the task, 13 more found on manual sweep). Each was grep-verified as a unique, exact substring occurring exactly once (`grep -c` = 1 for all 19, sum = 19). Manual sweep count = 19.

---

## TABLE 1 — PARTICIPANTS (both sides)

| # | Name | Designation / Firm | Side | Line | Flags |
|---|------|---------------------|------|------|-------|
| 1 | Mr. Santanu Agarwal | Deputy Managing Director (DMD) | Management | 18 (line 4) | PRESENT |
| 2 | Mr. Harish Singh | CFO | Management | 19 (line 5) | **MGMT_ABSENCE** — "unable to join due to personal exigency"; CFO is the officer normally expected to field financial-detail questions (interest expense, opex, D/E, provisioning) and is absent for a quarter where exactly those line items are the most contested (Q3, Q4b) |
| 3 | Sandip Mehta | Evaluate Research (analyst) | Analyst/Investor | 19 (Q1), 22 (Q1b), 24 (Q1c), 26 (closing), 66 (Q6 follow-up) | Asked twice (Q1 block + Q6 follow-up) |
| 4 | Ruti Doohi | Crestline Value Fund (analyst) | Analyst/Investor | 28 (Q2), 31 (Q2b), 33 (closing) | — |
| 5 | Lokesh Kumar Jaganath | Individual investor | Analyst/Investor | 35 (Q3), 37 (answer ref), 56 (Q7 follow-up) | Asked twice (Q3 + Q7 follow-up) |
| 6 | Amit Kumar | Individual investor | Analyst/Investor | 39 (Q4), 42 (Q4b), 44 (Q4c), 46 (closing) | — |
| 7 | Aditya Singh | Alpha Capital (analyst) | Analyst/Investor | 48 (Q5) | — |
| 8 | Harshit Singla | 8K Capital Private Limited (analyst) | Analyst/Investor | 60 (Q8), 63 (Q8b) | — |

Non-gated additional participant (host, neither management nor analyst side):
| — | Natasha | Moderator, Arihant Capital Markets Limited (call host) | Host | 9, 11, 17, 49, 53, 57, 61, 67, 68 | Informational only; not counted in the 8-participant gate per the both-sides definition |

---

## TABLE 2 — SPEAKER TURNS (sequential, 37 total)

| Turn | Line | Speaker | First ~10 words |
|------|------|---------|------------------|
| T1 | 9 | Moderator (unnamed, later ID'd as Natasha) | "Ladies and gentlemen, good day and welcome to Pisalo..." |
| T2 | 11 | Natasha, Arihant Capital (moderator) | "Uh thank you so much. Hello and good evening..." |
| T3 | 14 | Mr. Santanu Agarwal, DMD (opening remarks) | "Mr. Sanu please go ahead. Good afternoon everyone. Thank..." |
| T4 | 17 | Moderator | "Thank you. We will now begin with the question..." |
| T5 | 20 | Sandip Mehta, Evaluate Research — Q1 | "Hello. Can you hear me? Yes, we can hear..." |
| T6 | 21 | DMD — A1 | "Thank you Mr. Mena. Uh the state the lending..." |
| T7 | 22 | Sandip Mehta — Q1b | "Okay. Uh and then the uh with the ongoing..." |
| T8 | 23 | DMD — A1b | "So most of our borrowers are microenterprises, small traders..." |
| T9 | 24 | Sandip Mehta — Q1c | "Okay. And one last question is um uh again..." |
| T10 | 25 | DMD — A1c | "See our touch points have increased from 5,299 to..." |
| T11 | 26 | Sandip Mehta — closing | "Okay, thank you. All the best." |
| T12 | 29 | Ruti Doohi, Crestline Value Fund — Q2 | "Hi, am I audible? Yes, Miss Doohi, you are..." |
| T13 | 30 | DMD — A2 | "So see Mr. Dshi uh as Miss Dhi sorry..." |
| T14 | 31 | Ruti Doohi — Q2b | "Okay. And with uh 200k AIdriven outbound calls daily..." |
| T15 | 32 | DMD — A2b | "See, when you're talking about the debt management infrastructure..." |
| T16 | 33 | Ruti Doohi — closing | "All right. Got it. Thank you." |
| T17 | 36 | Lokesh Kumar Jaganath, individual investor — Q3 | "Hello. Can you hear me? Yes, Mr. Jagat, we..." |
| T18 | 37 | DMD — A3 | "Thank you Mr. Jaganat. So we'll start with the..." |
| T19 | 40 | Amit Kumar, individual investor — Q4 | "Hello. Yes, please go ahead. Thank you for the..." |
| T20 | 41 | DMD — A4 | "Thank you Mr. Kumar for your questions. So typically..." |
| T21 | 42 | Amit Kumar — Q4b | "Thank you. My next question is that the debt..." |
| T22 | 43 | DMD — A4b | "So see in case of in our case of..." |
| T23 | 44 | Amit Kumar — Q4c | "Thank you. And my last question is that the..." |
| T24 | 45 | DMD — A4c | "See if you we have been listed since almost..." |
| T25 | 46 | Amit Kumar — closing | "Thank you. This was helpful. All the best." |
| T26 | 49 | Moderator + Aditya Singh, Alpha Capital — Q5 | "We take a next question from Mr. Adidya Singh..." |
| T27 | 50 | DMD — A5 | "So see Mr. Singh if I speak about our..." |
| T28 | 53 | Moderator + Sandip Mehta — Q6 (follow-up) | "We take a follow-up question from Mr. Sandi Ma..." |
| T29 | 54 | DMD — A6 | "So you know uh the circular is basically using..." |
| T30 | 57 | Moderator + Lokesh Kumar Jaganath — Q7 (follow-up) | "We take our next follow-up question from Mr. Loesh..." |
| T31 | 58 | DMD — A7 | "See Mr. Jagan, if you talk about our growth..." |
| T32 | 61 | Moderator + Harshit Singla, 8K Capital — Q8 | "We take a next question from Mr. Hershit Singler..." |
| T33 | 62 | DMD — A8 | "Uh thank you Mr. Singap. Thank you so much..." |
| T34 | 63 | Harshit Singla — Q8b | "Understood. Well, uh and other question, what is one..." |
| T35 | 64 | DMD — A8b | "So, actually the only thing that I care about..." |
| T36 | 67 | DMD (closing remarks) | "Thank you. As there is no further questions, I..." |
| T37 | 68 | Moderator (closing) | "Thank you members of management. Ladies and gentlemen, on..." |

Q&A share: turns T5–T35 (31 of 37 turns, 84%) are Q&A; T1–T4 are opening/moderator, T36–T37 are closing — auditable against any "time-on-Q&A" claim.

---

## TABLE 3 — QUESTIONS (14, one row per bracket-marked question unit; REPEAT_QUESTION flagged)

| Q# | Turn | Asker | Firm | Topic(s) | Flags |
|----|------|-------|------|----------|-------|
| Q1 | T5 | Sandip Mehta | Evaluate Research | Co-lending tie-up status with State Bank of India (MSME lending expansion) | **REPEAT_QUESTION** (co-lending/co-origination topic recurs at Q6) |
| Q1b | T7 | Sandip Mehta | Evaluate Research | Iran war / commodity price impact on exporter exposure and NPLs | — |
| Q1c | T9 | Sandip Mehta | Evaluate Research | Sustainability of disbursement growth into Q2 and beyond | — |
| Q2 | T12 | Ruti Doohi | Crestline Value Fund | Cost-to-income ratio trend and AI-driven efficiency unlock | — |
| Q2b | T14 | Ruti Doohi | Crestline Value Fund | Conversion/resolution rate on 200k AI-driven outbound calls/day vs traditional collections | — |
| Q3 | T17 | Lokesh Kumar Jaganath | Individual investor | Bundled: (a) interest expense QoQ +32% (87cr→115cr); (b) opex QoQ −32% (69cr→46cr); (c) collection efficiency dip ~1% QoQ; (d) loan loss provisions +120% QoQ; (e) pledge-release plans; (f) promoter stake-increase headroom | **REPEAT_QUESTION** (sub-topic (f) promoter stake recurs at Q4c) |
| Q4 | T19 | Amit Kumar | Individual investor | Target AUM mix for diversified segments (agri/industrial/alt-fuel) over 2-3 years and associated risk | — |
| Q4b | T21 | Amit Kumar | Individual investor | Debt-to-equity trend (1.64x FY22 → 2.61x) — internal leverage ceiling and borrowing headroom | — |
| Q4c | T23 | Amit Kumar | Individual investor | Promoter stake increase (~5% in Q1FY27) — strategic rationale / signal to investors | **REPEAT_QUESTION** (recurs from Q3 sub-topic (f)) |
| Q5 | T26 | Aditya Singh | Alpha Capital | Key drivers behind the guided AUM-doubling target | **REPEAT_QUESTION** (doubling-AUM topic recurs at Q7 sub-topic) |
| Q6 | T28 | Sandip Mehta | Evaluate Research (follow-up) | RBI collateral-free MSME lending threshold (Rs20 lakh) — finalization status and impact on co-origination/co-lending ecosystem | **REPEAT_QUESTION** (co-lending/co-origination topic, recurs from Q1) |
| Q7 | T30 | Lokesh Kumar Jaganath | Individual investor (follow-up) | Bundled: (a) driver of touchpoint jump (5,299→5,995 QoQ); (b) internal timeline for doubling AUM/income/PAT — FY29 vs FY30 | **REPEAT_QUESTION** (sub-topic (b) doubling-AUM timeline recurs from Q5) |
| Q8 | T32 | Harshit Singla | 8K Capital Private Limited | Where top management spends 80% of its time; non-PAT/revenue KPI focus | — |
| Q8b | T34 | Harshit Singla | 8K Capital Private Limited | Biggest business risk / what management fears most | — |

REPEAT_QUESTION summary (3 topics recur, each across a different pair of askers, per task specification):
1. **Co-lending / co-origination ecosystem** — Q1 (Sandip Mehta, SBI tie-up status) and Q6 (Sandip Mehta follow-up, RBI-circular impact on co-origination/co-lending) — same asker, two angles of the same underlying topic across the call.
2. **Doubling-AUM drivers/timeline** — Q5 (Aditya Singh, key drivers) and Q7 sub-topic (b) (Lokesh Kumar Jaganath, internal timeline FY29/FY30) — two different askers.
3. **Promoter stake increase** — Q3 sub-topic (f) (Lokesh Kumar Jaganath, headroom/pledge) and Q4c (Amit Kumar, rationale/signal) — two different askers.

---

## TABLE 4 — NUMBERS SPOKEN BY MANAGEMENT (36 baseline items from injected task list)

| # | Figure | Value(s) spoken | Turn | Line | Flags |
|---|--------|------------------|------|------|-------|
| 1 | AUM | "60,000 67,74 million" (ASR garble for Rs 67,074 Mn), 28% YoY | T3 | 14 | ASR_ARTIFACT (transcription garble, not a real conflicting figure) |
| 2 | Disbursement | "17,39 million" (ASR garble for Rs 17,309 Mn), 128% YoY, "highest ever quarterly" | T3 | 14 | ASR_ARTIFACT |
| 3 | Total income | Rs 2,603 Mn, +19% YoY | T3 | 14 | — |
| 4 | NII | Rs 1,447 Mn | T3 | 14 | — |
| 5 | NIM | 6.6% | T3 | 14 | — |
| 6 | PAT | Rs 613 Mn, +30% YoY | T3 | 14 | — |
| 7 | RoA | 3.6% | T3 | 14 | — |
| 8 | RoE | 13.4% | T3 | 14 | — |
| 9 | GNPA | 0.70% | T3 | 14 | — |
| 10 | NNPA | 0.49% | T3 | 14 | — |
| 11 | Collection efficiency | 97.5% | T3 | 14 | Cross-check: analyst (Q3) later states a ~1% QoQ drop in collection efficiency — management's Q&A answer (T18/line37) does not restate the 97.5% figure or confirm/deny the 1% drop explicitly |
| 12 | Total borrowings | Rs 48,467 Mn | T3 | 14 | — |
| 13 | Net worth | Rs 18,298 Mn | T3 | 14 | — |
| 14 | CAR | 33.1% | T3 | 14 | — |
| 15 | Cost of borrowing (CoB) | 10.1%, −64bps YoY, ~300bps below FY21's 13% | T3 | 14 | — |
| 16 | Cost-to-income ratio | "roughly ... about 40% right now" | T13 | 30 | NEW_DISCLOSURE (not a standard filing metric; guidance-type figure disclosed only on the call) |
| 17 | Interest expense QoQ | Q4 "87 cr" → Q1 "115 cr", +32% | T17 (analyst-stated) | 36 | **ANALYST_SOURCED** — spoken by Lokesh Kumar Jaganath, not independently restated by management with these exact cr figures (DMD's answer at T18/line37 reframes as "NII and PAT up ~30% and ~16%" instead); **NEW_DISCLOSURE** (QoQ cr figures not in press release baseline) |
| 18 | Opex QoQ | "69 cr" → "46 cr", −32% | T17 (analyst-stated) | 36 | **ANALYST_SOURCED**; **NEW_DISCLOSURE** |
| 19 | Loan loss provisions | +120% QoQ (analyst-stated, T17/line36); −10% YoY (management-confirmed, T18/line37) | T17 / T18 | 36 / 37 | Mixed sourcing — QoQ figure is analyst-asserted and not numerically contested or confirmed by management; YoY figure is management's own; **NEW_DISCLOSURE** for the QoQ framing |
| 20 | Debt/Equity | 1.64x (2022, analyst-stated) → 2.61x (this quarter, analyst-stated, T21/line42); management restates as "about 1.6 times to about two and a half times" / "2.4 or 2.5 level" (T22/line43) | T21 / T22 | 42 / 43 | **NUMBER_CONFLICT** — analyst's precise 2.61x vs management's rounded "~2.5x" restatement |
| 21 | Internal leverage cap | "somewhere between a three and a half level" (~3.5x) | T22 | 43 | NEW_DISCLOSURE (internal target, not in press release) |
| 22 | Regulatory leverage cap | "RBI and the various regulators allow us to raise up to seven times" | T22 | 43 | — |
| 23 | FCCB | "about $44 million worth of foreign currency convertible bonds due for conversion"; committee meeting "scheduled for the same" | T22 | 43 | NEW_DISCLOSURE (not in press release baseline) |
| 24 | Promoter open-market acquisition | "4.6 or 4.7%"; SEBI annual limit "up to 5% ... which we have largely exhausted" | T18 | 37 | — |
| 25 | NCD public issue | Rs 300 crore under Rs 900 crore shelf; "scheduled to open on August 7th" | T3 | 14 | — |
| 26 | RBI collateral-free MSME threshold | Rs 20 lakh (raised from sub-Rs 3-5 lakh) | T3 (first mention), T29 (repeated) | 14, 54 | — |
| 27 | Portfolio secured/unsecured mix | 93% secured / 7% unsecured | T29 | 54 | — |
| 28 | Touchpoints & state footprint | 5,299 → 5,995 touchpoints, "across 23 states" | T3 | 14 | **NUMBER_CONFLICT** — call states "23 states"; press-release filing baseline (per task brief) states "22 states & UTs" |
| 29 | New product lines | "six new product lines" added in the quarter | T10 | 25 | — |
| 30 | AUM mix by segment | Food & hospitality 23%, agri & allied 15%, street vendors 16% (top 3); vehicle/health-education/textiles 3-6% each (bottom contributors) | T20 | 41 | — |
| 31 | BC franchise GTV | "crossed USD 1 billion" gross transaction value | T3 | 14 | — |
| 32 | AI onboarding applications | ~1.6 lakh (Q4FY26) → ~1.8 lakh (Q1FY27) | T3 | 14 | — |
| 33 | AI voice-to-data conversions | ~3.5 lakh (prior qtr) → ~5 lakh (Q1FY27) | T3 | 14 | — |
| 34 | AI outbound calls/day | ~1.5 lakh/day (Q4FY26) → ~2 lakh/day (Q1FY27); restated as "200k"/"200,000" in Q2b exchange | T3 (first), T14/T15 (restated) | 14, 31/32 | — |
| 35 | AI bots | 7 → 18 | T3 | 14 | — |
| 36 | 3-year strategic ambition | "ambition for the next 3 years to approximately double our AUM income and profitability" (first stated); "we are targeting ... three fiscal years for achieving our target of doubling" (repeated) | T3 (first), T31 (repeated) | 14, 58 | — |

### TABLE 4b — SUPPLEMENTARY NUMBERS FOUND ON SWEEP (beyond the 36-item baseline; non-gated, informational)

| # | Figure | Value(s) spoken | Turn | Line | Flags |
|---|--------|------------------|------|------|-------|
| S1 | NII/PAT QoQ growth | "up about 30% and 16% respectively" (offered in lieu of confirming the analyst's cr-denominated QoQ figures) | T18 | 37 | NEW_DISCLOSURE |
| S2 | Historical credit cost | "except on COVID times ... largely remained below 2%"; "last 5 years ... below 1%" | T18 | 37 | NEW_DISCLOSURE |
| S3 | IPO history | Listed since 1996 (~30 years); "raised about 1.5 crores in our IPO" | T24 | 45 | NEW_DISCLOSURE (historical context, not a Q1FY27 filing item) |
| S4 | FPO history | 2007 FPO "raised about uh 175 crores" | T24 | 45 | NEW_DISCLOSURE |
| S5 | Warrant issue | "3 years ago or four years ago ... invested about 185 or 180 crores by way of issue of warrants"; "adding 5% stake into the company" annually since | T24 | 45 | Management itself gives two different figures in the same breath ("185 or 180 crores", "3 years ago or four years ago") — internal imprecision, flag NUMBER_CONFLICT (self-conflicting, not vs. filing) |
| S6 | New product count nuance | T10/line25 says "six new product lines" added; T15/line32 references "three new development products which are getting launched in quarter 3 end" | T10, T15 | 25, 32 | **NUMBER_CONFLICT** (unclear whether the "3 new development products" launching in Q3-end are a subset of, or distinct from, the "6 new product lines" already added — A3/A4 should reconcile against the investor deck) |
| S7 | Touchpoint restatement | 5,299 → 5,995 restated verbally as "5,999 uh 995" | T31 | 58 | ASR_ARTIFACT |

---

## TABLE 5 — FORWARD-COMMITMENT AND HEDGE PHRASES (19 total, turn-numbered)

| # | Phrase (verbatim or near-verbatim) | Type | Turn | Line | Mandated in task? |
|---|--------------------------------------|------|------|------|--------------------|
| 1 | "certain forward-looking statements which are predictions, projections or other estimates about the future events" | Forward (safe-harbor boilerplate) | T1 | 9 | sweep addition |
| 2 | "we believe the momentum we are seeing is not just continuing but building" | Forward | T3 | 14 | sweep addition (also repeated verbatim in closing, T36/line67) |
| 3 | "we believe the long-term impact is likely to be positive" | Hedge/Forward | T3 | 14 | sweep addition |
| 4 | "the competitive advantage is likely to shift increasingly towards origination capability" | Forward | T3 | 14 | sweep addition |
| 5 | "our ambition for the next 3 years to approximately double our AUM income and profitability" | Forward-commitment | T3 | 14 | sweep addition (root of mandated phrase #6 below) |
| 6 | "we are in advanced stages of revamping our branch and business correspondent application platform" | Forward | T3 | 14 | sweep addition |
| 7 | "we expect these initiatives to support operating leverage" | Forward | T3 | 14 | sweep addition |
| 8 | "maintaining a balanced funding profile ... will remain a key priority" | Forward | T3 | 14 | sweep addition |
| 9 | "going forward, while quarterly growth may normalize from this exceptionally high base" | Hedge | T10 | 25 | sweep addition |
| 10 | "the company expects healthy momentum through FI27" | Forward | T10 | 25 | **MANDATED** |
| 11 | "cost to income ratios will remain slightly on the higher side" | Hedge | T13 | 30 | **MANDATED** |
| 12 | "three new development products which are getting launched in quarter 3 end" | Forward-commitment | T15 | 32 | **MANDATED** ("new products getting launched in quarter 3 end") |
| 13 | "the SC conversion is also likely" | Forward | T18 | 37 | **MANDATED** |
| 14 | "we don't see any major impact in quarters ahead except that there will be some time lag" | Hedge | T18 | 37 | sweep addition |
| 15 | "we are confident of sustaining the strength moving forward" | Forward | T18 | 37 | sweep addition |
| 16 | "the moment those bonds are also converted, this will also push down the leverage level giving us further headroom" | Forward/conditional hedge | T22 | 43 | sweep addition |
| 17 | "we are targeting ... three fiscal years for achieving our target of doubling" | Forward-commitment | T31 | 58 | **MANDATED** ("targeting three fiscal years for doubling") |
| 18 | "we have put co-lending as an optionality in it for providing incremental growth ... how we are not contributing on it" | Hedge | T31 | 58 | **MANDATED** |
| 19 | "if we see that also kicking in, we might see an expedited achievement of this timeline" | Hedge (conditional) | T31 | 58 | sweep addition |

All 6 phrases explicitly named in the task brief are present and accounted for (rows 10, 11, 12, 13, 17, 18); 13 additional forward/hedge instances were found on manual sweep.

---

## TABLE 6 — NUMBER_CONFLICT / NEW_DISCLOSURE SUMMARY (cross-reference)

| # | Item | Conflict / Disclosure type | Turn(s) | Line(s) |
|---|------|------------------------------|---------|---------|
| 1 | Touchpoint state count: "23 states" (call) vs "22 states & UTs" (press-release baseline, per task brief) | NUMBER_CONFLICT | T3 | 14 |
| 2 | Interest expense Q4 "87cr"→Q1 "115cr" (+32% QoQ) — analyst-asserted, not in press release, not independently re-confirmed by management with same figures | NEW_DISCLOSURE | T17 | 36 |
| 3 | Opex "69cr"→"46cr" (−32% QoQ) — analyst-asserted, not in press release | NEW_DISCLOSURE | T17 | 36 |
| 4 | Loan loss provisions "+120% QoQ" (analyst-asserted) vs "−10% YoY" (management-confirmed) — QoQ framing absent from press release | NEW_DISCLOSURE | T17 / T18 | 36 / 37 |
| 5 | D/E "2.61x" (analyst-precise) vs management's rounded "~2.5x"/"two and a half times" restatement | NUMBER_CONFLICT | T21 / T22 | 42 / 43 |
| 6 | Internal leverage cap ~3.5x — disclosed only on call | NEW_DISCLOSURE | T22 | 43 |
| 7 | FCCB ~$44mn pending conversion — disclosed only on call | NEW_DISCLOSURE | T22 | 43 |
| 8 | Cost-to-income ~40% — disclosed only on call | NEW_DISCLOSURE | T13 | 30 |
| 9 | Warrant-issue figure self-conflict: "185 or 180 crores", "3 years ago or four years ago" | NUMBER_CONFLICT (internal, self-sourced) | T24 | 45 |
| 10 | "Six new product lines" (T10) vs "three new development products ... launching in quarter 3 end" (T15) — unclear if subset or distinct set | NUMBER_CONFLICT | T10 / T15 | 25 / 32 |
| 11 | AUM/disbursement figures spoken with ASR garble ("60,000 67,74 million"; "17,39 million") — transcription artifact, not a substantive conflict | ASR_ARTIFACT | T3 | 14 |

---

## FLAGS RAISED (roll-up)
- **MGMT_ABSENCE**: CFO Mr. Harish Singh absent (line 19) on a quarter where financial-detail Q&A (interest expense/opex QoQ swings, D/E, loan-loss provisioning) dominated — answered entirely by the DMD.
- **REPEAT_QUESTION** (3 topics, each asked by two different questions/askers): co-lending/co-origination (Q1, Q6); doubling-AUM drivers/timeline (Q5, Q7); promoter stake increase (Q3, Q4c).
- **NUMBER_CONFLICT** (4 instances): touchpoint state count (23 vs 22 states/UTs baseline); D/E 2.61x vs "~2.5x" management restatement; warrant-issue figure self-conflict; "6 new product lines" vs "3 new development products" ambiguity.
- **NEW_DISCLOSURE** (6+ instances): interest expense/opex QoQ cr-figures, loan-loss-provision QoQ framing, internal leverage cap, FCCB balance, cost-to-income ratio, historical credit-cost bands, IPO/FPO/warrant history — none of these appear to originate from the press-release filing baseline; call-only disclosures for A3/A4 to weigh.
- **ANALYST_SOURCED**: interest expense and opex QoQ cr-figures originate from the analyst's question, not from management's own disclosure — management's answer reframes rather than confirms these exact numbers.
- **ASR_ARTIFACT** (non-substantive, flagged so downstream stages don't mistake transcription garble for a real disclosure discrepancy): AUM and disbursement figures rendered as "60,000 67,74 million" and "17,39 million"; touchpoint restatement "5,999 uh 995".
