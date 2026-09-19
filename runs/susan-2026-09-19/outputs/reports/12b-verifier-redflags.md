# STAGE 12 VERIFIER B: CONCALL RED FLAGS -- SUSAN (Susan Electricals India Ltd)
Run date: 2026-09-19 | Model: claude-opus-5 | Phase 1

## SCOPE AND METHOD

Inputs read in full, fresh, before the pipeline reports were compared:
- SUSAN Q1 FY27 transcript (call held 19-Aug-2026, filed 22-Aug-2026):
  `inputs/concalls/20260822-587aa8e9-...txt` (cited below as SUSAN-T, file page + line).
- SUSAN Q1 FY27 results (`inputs/results/20260814-fd652fd2-...txt`, SUSAN-R) and press
  release (`inputs/announcements/20260814-c94cd689-...txt`, SUSAN-PR), used as written
  company statements.
- Seven peer transcripts: DYCL Oct-2025, Feb-2026, May-2026, Jul-2026; DIACABS Aug-2026;
  VIDYAWIRES Dec-2025, May-2026 (cited as file name short form + [page N] + line).
- Pipeline reports: B05 (`outputs/reports/05-concall.md`), B06 (`outputs/reports/06-peers.md`).

Corpus limit. The instruction file expects 15 transcripts (3 main, 12 peer). The corpus
holds 8 (1 main, 7 peer). SUSAN listed 18-Jun-2026 and has filed one transcript. No
cross-quarter test on the main company is possible. So "repeated evasion across 2+
quarters" (the CRITICAL trigger) cannot occur on this corpus. Every severity below is
graded on this one call plus peer context.

Page references. The .txt files carry `[page N]` markers. Line numbers are the file line
numbers. SUSAN-T "p.N" means `[page N]` in the .txt file.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from raw transcripts only)

Severity scale: CRITICAL / MAJOR / MINOR (shared scale). Items are graded before comparison.

### Main company (SUSAN Q1 FY27 call)

**R1. HT/MVCC revenue-share guidance appears in three incompatible forms. MAJOR.**
- Opening script: "from ~5-10% currently toward ~15% by year-end and higher thereafter"
  (SUSAN-T p.3, line 64).
- Q2 answer and Q4 answer: "~50% by year-end" / "increase to around 50% by the end of
  FY27" (SUSAN-T p.6, lines 168-170).
- Third form, stated twice: "Expected FY27 revenue mix roughly balanced ~30-35% each across
  HT/MVCC, LT/conductors, and winding wires" (SUSAN-T p.3, lines 66-67; p.6, lines 143-144).
- Arithmetic: Q1 FY27 HT/MVCC share was 7.11% (SUSAN-PR p.3, line 83). A full-year FY27
  average of 30-35% needs roughly 38-44% in Q2-Q4 if Q1 is about a quarter of FY27
  revenue. [INFERENCE] That path matches the ~50% exit figure and makes the ~15% figure
  the outlier. The order-book mix (~30% HT/MVCC, SUSAN-T p.4, line 82) points the same way.
  Two readings: (a) ~50% exit is the real target and ~15% is a script error; (b) ~15% is
  the real target and the 30-35% and 50% figures are aspirational. Separating observation:
  the call audio (SUSAN-T p.11, lines 302-303) and the Q2 FY27 product-mix table.

**R2. Current HT/MVCC share stated two ways in one call. MINOR.**
- Q4 answer: "around 5%-10% of revenue" (SUSAN-T p.6, line 168).
- Q9 answer: "around 10% to 15%" (SUSAN-T p.8, line 222).
- Filed figure: 7.11% (SUSAN-PR p.3, line 83). The Q9 figure is above the filed number.

**R3. The transcript is an edited summary, not a verbatim record. MAJOR.**
- Q10 and Q11 are third-person paraphrase: "The participant requested...", "Management
  acknowledged the suggestion..." (SUSAN-T p.9, lines 230-234, 237-238).
- Q12 answer is blank in the body ("maximum focus going forward will remain on   .",
  line 248). The words "HT cables and MVCC cables" sit orphaned at line 257.
- The ~50% figure in Q4 extracts out of reading order, after a gap (line 169, "around   .
  50% by the end of FY27"). The Q2 answer body is broken ("HT & MVCC ... thereafter)",
  lines 140-142). The ~50% bullet text sits separately at line 170. [INFERENCE] Both ~50%
  instances look like overlay text placed on the page after drafting. The ~15% figure sits
  in the body of the opening script. The PDF could not be rendered in this container to
  confirm this visually.
- Dates conflict. Cover letter: call held "Wednesday, August 19, 2026" (SUSAN-T p.1,
  lines 21-22). Title page: "August 14, 2026" (p.2, line 39). The press release gave the
  call as "18th August-26" (SUSAN-PR p.3, line 108).
- The disclaimer says the transcript "may have been slightly edited" and names an audio
  file on the website and exchange (SUSAN-T p.11, lines 298-303).
- Why it matters. R1's load-bearing number (LBF4, ~50%) rests on the edited text. The
  audio file is the one observation that settles which number management said.

**R4. Winding-wire segment margin of 24.39% is internally implausible. MAJOR.**
- Q1 answer: "Winding wires: Approximately 24.39% EBITDA margin" (SUSAN-T p.5, line 131).
- The same figure, 24.39%, is the winding-wire REVENUE SHARE for Q1 FY27 (SUSAN-PR p.3,
  line 81). A margin that matches the revenue share to two decimals is a possible
  transcription or column-transfer error. [INFERENCE]
- Management's own opening script says "winding wires & LT/conductors typically 10-15%"
  (SUSAN-T p.3, lines 69-70).
- The stated strategy moves mix AWAY from winding wire toward LT/HT/MVCC for "stronger
  margin potential" (SUSAN-PR p.3, lines 93-94; SUSAN-T p.3, lines 53-55). On the Q1
  segment figures, winding wire (24.39%) earns 3.5x LT (6.5%) and HT (7%). The strategy
  and the segment figures cannot both be right as stated.
- Winding-wire share fell from 47.74% to 24.39% YoY (SUSAN-PR p.3, line 81). If winding
  wire truly earns ~24%, that mix shift should have cut the blended margin. The blended
  margin instead rose from 4.18% to 11.9% (SUSAN-PR p.2, line 54).
- Counter-reading, stated with the same bar. On the disclosed mix, the 24.39% figure is
  what brings the blend near the reported 11.9%. Revenue-weighted: 24.39% x 24.39% +
  65.68% x 6.5% + 7.11% x 7% = 10.7% on total revenue, about 11.0% excluding the 2.82%
  "other". With winding wire at 12.5% (midpoint of management's own 10-15%), the blend is
  about 7.8%, which misses 11.9% by about 4 points. So either the winding-wire figure is
  real and the "typically 10-15%" script is wrong, or more than one segment figure is
  wrong. Separating observation: the audio file, and the "greater clarity" segment
  disclosure promised in Q10 (SUSAN-T p.9, line 233).
- The peer check (VIDYAWIRES at 4.3%-4.66% company-wide, see R20 context) points to a
  problem. The first problem is internal to SUSAN's own call.

**R5. The ~20% HT/MVCC figure is called "net margin" in Q&A and "EBITDA" in the script. MINOR.**
- Opening: "HT/MVCC per-unit EBITDA potential ~20% (or 20-25%)" (SUSAN-T p.3, line 69).
- Q3 answer: "approximately 20% net margins" (SUSAN-T p.6, lines 157-158).
- Q4 answer: "product-level profitability potential" (line 164). The basis is never fixed.

**R6. Segment margins do not reconcile to the blended margin. MINOR.**
- See R4 arithmetic. The gap is about 0.8-1.2 points with the disclosed figures. The
  company-level figure is given as "~11.9%" (line 71) and "approximately 12%" (Q8,
  lines 211-212).

**R7. Long-term debt question answered with no content. MAJOR.**
- Q14, Ankur Gulati: "clarity on the company's debt position and whether there are any
  plans for increasing long-term debt". Answer: "will evaluate funding requirements based
  on business growth ... Any requirement for additional funding will be considered
  accordingly" (SUSAN-T p.10, lines 271-277). No debt figure, no plan.
- Context: finance cost Rs 233.47 Lakh in Q1 FY27 vs Rs 125.41 Lakh in Q1 FY26 (SUSAN-R
  p.2, line 69), up 86% YoY.

**R8. Raw-material pass-through question answered with no mechanism. MAJOR.**
- Q13, Chandan Jain, on aluminium rod volatility. Answer: "monitored closely ...
  appropriate pricing mechanisms and operational measures" (SUSAN-T p.10, lines 262-268).
- All three peers name a mechanism: DYCL price-variation clause plus raw-material booking
  on fixed-price orders, ~20% fixed-price (DYCL-Jul26 [page 4] lines 136-142; [page 9]
  lines 341-342); DIACABS "completely back-to-back" (DIACABS [page 4] line 152);
  VIDYAWIRES LME back-to-back with forex hedge (VIDYA-Dec25 [page 10] lines 347-352).

**R9. FY27 revenue guidance declined, then an implicit anchor given. MINOR.**
- "We would not like to provide an absolute revenue number" then "Investors can look at
  our performance over the last two to three years ... We expect the business to continue
  growing in a similar manner" (SUSAN-T p.7, lines 190-196).
- [INFERENCE] The historical trajectory includes FY26 aluminium-rod trading revenue (B05
  cites B02 at 26.8% of FY26 revenue; not verifiable from verifier inputs). The anchor
  mixes trading and manufacturing growth.

**R10. Sequential decline not volunteered; "strong start" framed only YoY. MAJOR.**
- Q4 FY26 to Q1 FY27 (SUSAN-R p.2): revenue Rs 11,560.98 Lakh to Rs 9,535.68 Lakh
  (-17.5%); PBT Rs 1,388.18 Lakh to Rs 858.22 Lakh (-38.2%); PAT Rs 1,032.05 Lakh to
  Rs 639.13 Lakh (-38.1%) (lines 59, 57, 73, 83).
- Operating margin derived from the same statement: Q4 FY26 about 14.0% (11,560.98 -
  9,401.86 + 9.15 - 212.77 - 339.95 = 1,615.55 Lakh), Q1 FY27 11.9%. The margin fell
  about 200 bps sequentially. The script says "Blended operating margin improved to
  ~11.9%" (SUSAN-T p.3, line 71). That is true only against Q1 FY26 (4.18%).
- Q4 FY26 was 42.9% of FY26 revenue (11,560.98 / 26,935.66 Lakh). Q1 annualised is about
  Rs 381 Cr against a Q4 FY26 run rate of about Rs 462 Cr.
- Benign reading: peers state Q1 is the seasonal low for T&D cables (DIACABS [page 3]
  lines 125-126; [page 13] lines 533-539; DYCL-Oct25 [page 16] line 43). SUSAN's call
  gives no seasonality explanation, and no analyst asked.

**R11. "Peak ... potential of ~700 to 800cr in revenue" left unprobed. MAJOR.**
- "Peak capex reference potential of ~700 to 800cr in revenue" (SUSAN-T p.4, line 92).
  The line is ambiguous: it may mean total revenue at 12,000 km/yr.
- FY27 capex guided at Rs 15-20 Cr (Q5, p.7, line 178). The IPO capex object is
  Rs 10.30 Cr (SUSAN-R p.3, line 143). FY26 revenue was Rs 269.36 Cr (SUSAN-R p.2,
  line 63).
- Peer benchmark: DYCL states 6x-7x asset turns on gross block (DYCL-Jul26 [page 10]
  lines 397-398; DYCL-May26 [page 15] line 594). At 6-7x, Rs 15-20 Cr of capex adds about
  Rs 90-140 Cr of revenue. [INFERENCE] Pro-rating the Q1 annualised Rs 381 Cr by capacity
  (12,000 / 7,500 km) gives about Rs 610 Cr. So Rs 700-800 Cr needs a price or mix uplift
  on top of full use of the new capacity. No analyst tested this. It is a forward revenue
  anchor of the kind the 26.1 basis hierarchy would pick up.

**R12. "Ahead of schedule" heading vs "on track" body. MINOR.**
- Heading: "Completing our capacity expansion ahead of schedule" (SUSAN-T p.4, line 88).
  Body: "On track for commercial operations from Feb 2027" (line 89). The IPO capex object
  is 11.7% used at 30-Jun-2026 (Rs 1.20 of Rs 10.30 Cr, SUSAN-R p.3, line 143).

**R13. Order-book execution language is softer in the press release than on the call. MINOR.**
- Call script: "expected to execute over next ~3 months" (SUSAN-T p.4, lines 78-79).
- Press release: "a significant portion expected to be executed within the next three
  months" (SUSAN-PR p.2, lines 62-64; p.3, line 99).

**R14. Cash conversion and working-capital build never mentioned. MAJOR.**
- No cash-flow, receivable, or inventory reference on the call (SUSAN-T pp.3-11). No
  analyst asked.
- The P&L shows a finished-goods inventory build of Rs 932.66 Lakh in Q1 FY27 (SUSAN-R
  p.2, line 67), 9.8% of quarterly revenue, against Rs 9.15 Lakh in Q4 FY26.

**R15. Disclosure request acknowledged, not committed. MINOR.**
- Q10: management "indicated that greater clarity would be provided in future disclosures"
  (SUSAN-T p.9, lines 233-234). No date and no form.

**R16. Tender conversion assumption with no track record. MINOR.**
- "Regularly bidding Rs 800-1,200 Cr of tenders; expected conversion ~15% to 20%. Many
  pipeline items already L1/L2 awaiting LOI" (SUSAN-T p.4, lines 84-85). No historical
  hit rate.

**R17. No volume vs price split of the 279% growth. MINOR.**
- "EBITDA per unit improving across our products" (SUSAN-T p.3, line 57) with no unit,
  tonnage, or km figure anywhere on the call.
- Peers split it routinely: DYCL Q1 FY27 volume growth 5-6%, the rest aluminium price
  (DYCL-Jul26 [page 5] lines 173-176). DIACABS: aluminium moved about 20% up then 22% down
  April-June 2026 (DIACABS [page 13] lines 528-530).

**R18. "Only a limited number of companies operate in this space" (HT/MVCC). MINOR.**
- SUSAN-T p.6, lines 145-146.
- Peer evidence is mixed. DIACABS supports a narrower field in MV/EHV (DIACABS [page 6]
  lines 219-221). DYCL confirms "a lot of expansion ... amongst all the players" after an
  analyst says "nearly every major player is expanding its capacity in HV or the EHV
  cable" (DYCL-Jul26 [page 13] lines 512-519).

### Peer statements that bear on SUSAN

**R19. Industry-wide weak order booking in April-May 2026. MINOR.**
- DYCL: "April, May was very, very weak order booking for not only for us, I think it
  should be a common phenomenon" (DYCL-Jul26 [page 5-6] lines 199-208); "industry-wide
  slowdown" (DYCL-Jul26 [page 9] lines 332-339); only near-term orders being placed
  ([page 16] lines 634-639).
- SUSAN reports Rs 142.39 Cr unexecuted order book at 30-Jun-2026 plus Rs 150 Cr pipeline
  and does not mention any booking softness.

**R20. B2B cable EBITDA ceiling of 10-11%. MINOR.**
- DYCL: "the long-term sustainable margins will be between 10% to 11% ... because it is a
  competitive business, in a B2B competition, you have to compete on the lowest price"
  (DYCL-Feb26 [page 15] line 46).
- This bears on SUSAN's ~20% HT/MVCC potential and on the 24.39% winding-wire figure.
  VIDYAWIRES company-wide EBITDA margin: 4.3% H1 FY26 (VIDYA-Dec25 [page 5] lines
  178-179), 4.66% FY26 (VIDYA-May26 [page 4] lines 158-159).

**R21. MV/HT cable off-take is seasonal and site-delivered. MINOR.**
- DIACABS: Q1 is "always the most seasonally demanding"; monsoon flooding stopped MV
  laying; LV and conductor mix is higher in Q1; "Medium voltage cable and extra voltage
  cables are always delivered at the project site. They cannot be stored in warehouses at
  the customers" (DIACABS [page 3] lines 118-126; [page 13] lines 533-539).
- [INFERENCE] This gives a benign reading for SUSAN's Q1 FY27 finished-goods build and its
  low 7.11% HT/MVCC share: goods made but held for post-monsoon site dispatch. The
  pipeline did not bring this reading to its inventory flag.

Independent list: 21 items. Material (CRITICAL + MAJOR): 8 (R1, R3, R4, R7, R8, R10, R11,
R14). CRITICAL: 0. Single transcript, so no repeated-evasion test is possible.

---

## PART 2: COMPARISON AGAINST PIPELINE ANALYSES (B05, B06)

### 2A. My items vs the pipeline

| # | Item | Sev | Verdict | Where / why |
|---|---|---|---|---|
| R1 | HT/MVCC share, three forms | MAJOR | PARTIALLY CAUGHT | B05 1C, 4D caught 15% vs 50% and rated it HIGH. B05 missed the third form (FY27 mix ~30-35% each, stated twice). That form changes which figure is the outlier. B05 1A/1B do not list it. |
| R2 | Current share 5-10% vs 10-15% | MINOR | MISSED | B05 quotes only 5-10%. The Q9 "10-15%" is absent. |
| R3 | Edited transcript; overlay 50%; date conflicts | MAJOR | PARTIALLY CAUGHT | B05 notes a revised call date (methodology) and one "paraphrased" answer (3C). It does not flag the record as non-verbatim, does not note the blank Q12 answer, and does not name the audio file as the tie-breaker for LBF4. |
| R4 | Winding wire 24.39% = revenue share; contradicts own 10-15% and strategy | MAJOR | MISSED | B05 uses 24.39% as fact (1B, 2D, 4B Q6). B06 Q6 builds its "single most consequential contradiction" on a peer gap (VIDYAWIRES) and does not see the internal contradiction or the coincidence with the revenue share. The direction of B06's concern is right. The diagnosis is incomplete. |
| R5 | "Net" vs "EBITDA" 20% | MINOR | MISSED | B05 1A/1B and B06 Q2 treat it as EBITDA. |
| R6 | Blend does not reconcile | MINOR | CAUGHT | B05 2D, 4D (MEDIUM). Arithmetic confirmed (10.7% total, ~11.0% ex-other). |
| R7 | Debt question dodged | MAJOR | CAUGHT | B05 2B, 3C. |
| R8 | Pass-through dodged; peers name mechanisms | MAJOR | CAUGHT | B05 2B, 3C; B06 Q3 (VERIFIED, quotes checked). |
| R9 | Guidance declined + historical anchor | MINOR | PARTIALLY CAUGHT | B05 3C records the decline. It does not note the "look at the last two to three years" anchor or its trading content. |
| R10 | QoQ decline not volunteered | MAJOR | MISSED | Neither report mentions the Q4 FY26 to Q1 FY27 decline in revenue, PBT, or margin. |
| R11 | Rs 700-800 Cr peak revenue claim | MAJOR | MISSED | Absent from B05 1A/1B and 4A. B06 Q5 covers lead time, not asset turn, though DYCL's 6-7x is in its own peer set. |
| R12 | "Ahead of schedule" heading | MINOR | PARTIALLY CAUGHT | B05 flags thin capex pace (4D). It does not flag the overclaim wording. |
| R13 | PR vs call order-book wording | MINOR | MISSED | B05 2A quotes the PR as "expected to be executed over the next 3 months". The PR says "a significant portion". |
| R14 | Cash / WC silence | MAJOR | CAUGHT | B05 2D, 4D; B06 2E(5). |
| R15 | Disclosure acknowledged, not committed | MINOR | CAUGHT | B05 3C. |
| R16 | Conversion assumption unbenchmarked | MINOR | CAUGHT | B05 3B; B06 Q7. |
| R17 | No volume/price split | MINOR | MISSED | Not raised in B05 or B06. |
| R18 | "Limited companies" moat claim | MINOR | CAUGHT | B05 3A (credibility LOW); B06 2C capacity race. |
| R19 | Industry-wide weak April-May booking | MINOR | PARTIALLY CAUGHT | B06 2A, 2E(1) record DYCL's deferment. It does not set this against SUSAN's order book claim. |
| R20 | DYCL 10-11% B2B ceiling | MINOR | PARTIALLY CAUGHT | B06 Q1/Q2 state "DYCL discloses no segment figures" and "DYCL silent". DYCL's explicit B2B margin ceiling statement (Feb-2026) is not used. |
| R21 | MV seasonal, site-delivered | MINOR | MISSED | B06 2E(4) notes weather risk in general. Neither report links it to SUSAN's Q1 inventory build. |

Tally: CAUGHT 7, PARTIALLY CAUGHT 6, MISSED 8 (total 21).
Material subset (8): CAUGHT 3 (R7, R8, R14), PARTIALLY CAUGHT 2 (R1, R3), MISSED 3 (R4,
R10, R11).

### 2B. Pipeline red flags I did not raise, or raised differently

| Pipeline flag | Source | Verdict | Reason |
|---|---|---|---|
| Q1 FY27 operating profit "includes" a Rs 932.66 Lakh inventory-build credit (~82%); stripping it "flips PBT to a small loss"; profit is "unrealised (inventory-embedded)" | B05 2D, 4D (HIGH), 4A #3 | OVERSTATED | The arithmetic is right: 932.66 / 1,137.34 = 82.0%; 858.22 - 932.66 = -74.44 Lakh (SUSAN-R p.2, lines 67, 73). The reading is wrong. "Changes in inventories of finished goods" reverses the cost of goods made but not yet sold. Inventory sits at cost, not selling price. No margin is booked on unsold goods. Removing the credit charges the cost of unsold goods against the quarter's revenue, which is not a margin-quality test. Q4 FY26 printed a ~14.0% operating margin with only a Rs 9.15 Lakh inventory credit, so SUSAN earns double-digit margin without inventory build. What IS real: Rs 9.33 Cr of cash went into finished goods in one quarter (9.8% of revenue) while revenue fell 17.5% QoQ. That is a working-capital and cash flag, with a benign seasonal reading (R21). Graded HIGH as a profit-quality flag, it would mislead the Section 1B margin bridge. |
| "Segment margins were given only after three separate analyst prompts"; "three analysts had to press before segment margins were given at all" | B05 2C (Transparency 2/5), 3C, 4C | NOT SUPPORTED | The first question (Q1, Nishita) asked for segment margins. The first answer gave all three figures (SUSAN-T p.5, lines 124-132). The later questions (Q3, Q4, Q8, Q10) sought clarification of figures already given. The WEAK disclosure verdict still stands on other grounds (R1, R4, R5). |
| "The two hardest topics (cash conversion, raw-material formula pricing, the trading-revenue base) were raised only when an analyst pushed" | B05 2B | NOT SUPPORTED (internal inconsistency) | Cash conversion and trading were never raised by anyone. B05 2D says so itself. Only raw-material pricing was asked. |
| HT/MVCC 15% vs 50% (HIGH) | B05 4D | SUPPORTED | R1. |
| Segment arithmetic gap (MEDIUM) | B05 4D | SUPPORTED | R6. Under-weighted relative to R4. |
| Cash conversion silence (MEDIUM) | B05 4D | SUPPORTED | R14. |
| Aluminium-rod trading line collapse unexplained (MEDIUM) | B05 4D | SUPPORTED (silence only) | Call silent; PR "other operating revenue including trading" = 2.82% (SUSAN-PR p.3, line 84). The FY26 26.8% baseline comes from B02 and is outside verifier inputs. |
| Capex pace thin (MEDIUM) | B05 4D | SUPPORTED | SUSAN-R p.3, line 143. Note: the Rs 1.20 Cr covers only ~12 days from listing (18-Jun) to 30-Jun. It is weak evidence of pace either way. |
| AR Chairman's message vs Board's Report (LOW-MEDIUM) | B05 4D | NOT ASSESSED | The AR is not in Verifier B's inputs. |
| Winding-wire margin CONTRADICTED by VIDYAWIRES 4.3%-4.66% | B06 Q6 | SUPPORTED, misdiagnosed | Peer figures confirmed (VIDYA-Dec25 [page 5] lines 178-179; VIDYA-May26 [page 4] lines 158-159). The stronger evidence is internal to SUSAN (R4). |
| HT/MVCC ~20% closer to DIACABS EHV band than MV band | B06 Q2 | SUPPORTED | DIACABS [page 17] lines 708-713. Add DYCL's 10-11% B2B ceiling (R20). |
| Feb-2027 target "looks aggressive rather than conservative" | B06 Q5 | OVERSTATED | The comparators are DYCL's Rs 40-45 Cr greenfield plant with AERB approval (DYCL-May26 [page 7] lines 249-255) and DIACABS CCV lines at ~Rs 100 Cr (DIACABS [page 15] lines 604-609). SUSAN's project is a Rs 10.30 Cr brownfield add. DIACABS says a silane MV line costs Rs 15-20 Cr (same page) and B06 itself notes such lines commission in weeks to two months. Directional caution is fair. "Aggressive" is not shown. |
| DYCL plant "at the end of H2 only ... next financial year" cited to Q3 FY26 call p.13-14 | B06 Q5 | ANCHOR MISATTRIBUTED | The quote is in the Q2 FY26 call (DYCL-Oct25 [page 14] line 43). The Q3 FY26 call says "expected to be commissioned by the end of FY26" (DYCL-Feb26 [page 3] line 10). The slippage conclusion survives. |
| DIACABS "order book that grew from roughly INR1,900 crore to INR3,688 crore" | B06 2A | NOT SUPPORTED | INR 1,900 Cr is DIACABS revenue ("grow from INR1,900 crores to INR4,500 crores", DIACABS [page 10] line 397). The INR 3,688 Cr order book is "about 2 times of last year's revenue" ([page 7] lines 266-267). Context only, not a flag against SUSAN. |
| DYCL "actively reducing government-sales share (11-16% of revenue across the four calls, falling)" | B06 Q4 | NOT SUPPORTED (direction) | The share went 12% (DYCL-Oct25 [page 4]), 13% (DYCL-Feb26 [page 4]), 13% (DYCL-May26 [page 3] line 134), 16% (DYCL-Jul26 [page 3] line 116). It rose in the latest quarter. The stated intent to reduce it is real (DYCL-Oct25 [page 12]). Context only. |

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 Section 2A)

B05 built its tracker from written statements against the Q1 FY27 print, because only one
transcript exists. I checked every row that my inputs can reach.

| B05 row | Earlier statement present? | Later outcome as B05 states? | Result |
|---|---|---|---|
| Capacity 7,500 to 12,000 km by Feb-2027; capex object Rs 1.20 of 10.30 Cr used (11.7%) = PARTIAL | Yes: Feb-2027 on the call (SUSAN-T p.4, line 89) and in the PR (SUSAN-PR p.2, lines 66-68) | Yes: 10.30 / 1.20 / 9.10 (SUSAN-R p.3, line 143) | CONFIRMED |
| Working capital object Rs 13.64 of 33.00 Cr used (41.3%) = PARTIAL (early) | Yes (object in results table) | Yes: 33.00 / 13.64 / 19.36 (SUSAN-R p.3, line 146) | CONFIRMED |
| Shift to HT/MVCC: share 2.07% to 7.11% = DELIVERED directionally | Yes: strategy in PR (SUSAN-PR p.3, lines 93-96) | Yes: 2.07% to 7.11% (SUSAN-PR p.3, line 83) | CONFIRMED |
| Order book Rs 142.39 Cr "expected to be executed over the next 3 months" = TOO EARLY | Yes, but the PR says "a significant portion" (SUSAN-PR p.2, lines 62-64). The call says "over next ~3 months" (SUSAN-T p.4, lines 78-79) | Not yet due; correctly ungraded | CONFIRMED (wording caveat, R13) |
| FY27 capex Rs 15-20 Cr = TOO EARLY | Yes (SUSAN-T p.7, line 178) | Not yet due | Not counted (no outcome to test) |
| AR Chairman "global distribution" = MISSED | AR not in verifier inputs | Not testable | Not counted |

Checked 4, confirmed 4, wrong 0.

---

## PART 4: CREDIBILITY GRADE

B05 grade: C. Concur. The single-transcript cap limits the grade to C by default. The
evidence here does not lift it to B. R1, R3, and R4 point to weak control over the
numbers management speaks. R7 and R8 are content-free answers on the two questions with
the most cash at stake. One correction to the grounds: remove "segment margins given
only after three prompts" (not supported). Add R4, R10, and R11. The grade holds either
way.

---

## PART 5: CONSOLIDATED FINDINGS

| # | Severity | Location | Finding |
|---|---|---|---|
| F1 | MAJOR | B05 1B/2D/4B, B06 Q6 | MISSED R4. The 24.39% winding-wire margin matches the winding-wire revenue share to two decimals. It contradicts management's own "typically 10-15%" (SUSAN-T p.3, lines 69-70) and the stated mix-shift logic. Both reports use it as a fact. Hold any margin-bridge input off this figure until the audio or the promised segment disclosure resolves it. |
| F2 | MAJOR | B05 1A/1B/4A | MISSED R11. The "~700 to 800cr in revenue" peak-potential claim (SUSAN-T p.4, line 92) is not recorded or tested. DYCL's 6-7x asset turn puts Rs 15-20 Cr of capex at about Rs 90-140 Cr of added revenue. |
| F3 | MAJOR | B05 (all sections) | MISSED R10. Q1 FY27 revenue fell 17.5% QoQ, PBT 38.2%, and operating margin about 200 bps (SUSAN-R p.2). Management framed only YoY. The seasonal reading exists (DIACABS, DYCL) but the pipeline states neither the fact nor the reading. |
| F4 | MAJOR | B05 2D, 4A #3, 4D | OVERSTATED pipeline flag. The inventory-change credit is a cost reversal, not unrealised profit. The "PBT flips to loss" test is not a margin test. Re-state it as a working-capital and cash flag (Rs 9.33 Cr FG build in one quarter), with the monsoon/site-delivery reading (R21) beside it. |
| F5 | MAJOR | B05 2C, 3C, 4C | NOT SUPPORTED. "Segment margins given only after three prompts" is wrong. They were given in the first answer (SUSAN-T p.5, lines 124-132). |
| F6 | MINOR | B05 1A/1B/1C | PARTIAL R1. Third form of the HT/MVCC guidance (FY27 mix ~30-35% each, SUSAN-T p.3, lines 66-67; p.6, lines 143-144) is missing. It supports ~50% over ~15%. |
| F7 | MINOR | B05 methodology, 1C | PARTIAL R3. The transcript is an edited summary. The ~50% figures extract as out-of-order text. The call date appears as 14, 18, and 19 Aug across filings. Name the audio file (SUSAN-T p.11, lines 302-303) as the tie-breaker for LBF4. |
| F8 | MINOR | B05 1B | MISSED R2. Current HT/MVCC share also stated as 10-15% (SUSAN-T p.8, line 222). |
| F9 | MINOR | B05 1A/1B, B06 Q2 | MISSED R5. ~20% is called "net margins" in Q3 (SUSAN-T p.6, lines 157-158). |
| F10 | MINOR | B05 2A | MISSED R13. The PR says "a significant portion" of the order book in three months, not the whole. |
| F11 | MINOR | B05, B06 | MISSED R17. No volume or price split of 279% growth; peers disclose one. |
| F12 | MINOR | B05 4D, B06 Q5 | PARTIAL R12. "Ahead of schedule" heading vs "on track" body. |
| F13 | MINOR | B05 3C | PARTIAL R9. "Look at the last two to three years" anchor not recorded. |
| F14 | MINOR | B06 Q1/Q2 | PARTIAL R20. DYCL's explicit 10-11% B2B margin ceiling (DYCL-Feb26 [page 15]) is not used; B06 calls DYCL "silent". |
| F15 | MINOR | B06 2A/2E | PARTIAL R19. DYCL's industry-wide April-May booking slump is not set against SUSAN's order-book claims. |
| F16 | MINOR | B05 2D, B06 2E | MISSED R21. DIACABS' MV seasonality and site-delivery statements are not linked to SUSAN's Q1 FG build. |
| F17 | MINOR | B06 Q5 | OVERSTATED. "Aggressive" timeline compares a Rs 10.30 Cr brownfield add to greenfield and CCV projects. |
| F18 | MINOR | B06 Q5 | Anchor misattributed: "end of H2 only" quote is DYCL Q2 FY26 (Oct-2025 [page 14]), not Q3 FY26. |
| F19 | MINOR | B06 2A | NOT SUPPORTED (context): DIACABS INR 1,900 Cr is revenue, not a prior order book. |
| F20 | MINOR | B06 Q4 | NOT SUPPORTED (context): DYCL government share rose to 16% in Q1 FY27; it did not fall. |
| F21 | MINOR | B05 2B | Internal inconsistency: says cash conversion and trading were raised under analyst pressure; they were never raised. |

Counts: CRITICAL 0, MAJOR 5 (F1-F5), MINOR 16 (F6-F21).

## COVERAGE AND SCORE

- Transcripts read: 8 of 8 in corpus (1 main, 7 peer). The 15-transcript design is not
  reachable; SUSAN has one call since listing.
- Independent list: 21 items; material (CRITICAL + MAJOR) 8.
- Rule for material_caught: CAUGHT plus PARTIALLY CAUGHT, per the rule 3 definition
  ("found but under-weighted or misclassified"). Found: 5 of 8 (R1, R3, R7, R8, R14).
  Fully caught only: 3 of 8 (R7, R8, R14). Missed: 3 of 8 (R4, R10, R11).
- acceptance_rate = 5 / 8 = 62.5%. On the strict fully-caught count it would be 37.5%.
  The orchestrator should read both. The three misses all bear on the margin bridge or
  the revenue base.

```yaml
stage: B12b
company: "SUSAN"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 21
caught: 7
partially_caught: 6
missed:
  - {severity: "MAJOR", item: "Winding-wire EBITDA margin 24.39% equals winding-wire revenue share 24.39%; contradicts management's own 'winding wires typically 10-15%' and the mix-shift logic; B05 and B06 use it as fact", anchor: "SUSAN-T p.5 l.131; p.3 l.69-70; SUSAN-PR p.3 l.81"}
  - {severity: "MAJOR", item: "Q1 FY27 sequential decline not volunteered: revenue -17.5% QoQ, PBT -38.2%, operating margin ~14.0% to 11.9%; script frames margin as 'improved'", anchor: "SUSAN-R p.2 l.57-83; SUSAN-T p.3 l.71"}
  - {severity: "MAJOR", item: "'Peak ... potential of ~700 to 800cr in revenue' unrecorded and unprobed; DYCL 6-7x asset turn implies Rs 90-140 Cr from Rs 15-20 Cr capex", anchor: "SUSAN-T p.4 l.92; p.7 l.178; DYCL-Jul26 [page 10] l.397-398"}
  - {severity: "MINOR", item: "Current HT/MVCC share also stated as 10-15% (vs 5-10% and filed 7.11%)", anchor: "SUSAN-T p.8 l.222; p.6 l.168"}
  - {severity: "MINOR", item: "~20% HT/MVCC figure called 'net margins' in Q&A, 'EBITDA' in script", anchor: "SUSAN-T p.6 l.157-158; p.3 l.69"}
  - {severity: "MINOR", item: "Press release says 'a significant portion' of order book in 3 months; B05 quotes it as the whole", anchor: "SUSAN-PR p.2 l.62-64"}
  - {severity: "MINOR", item: "No volume vs price split of 279% growth; peers disclose one", anchor: "SUSAN-T p.3 l.57; DYCL-Jul26 [page 5] l.173-176"}
  - {severity: "MINOR", item: "DIACABS: MV cable Q1 seasonal low and site-delivered only; benign reading for SUSAN Q1 FG build not linked", anchor: "DIACABS [page 3] l.118-126; [page 13] l.533-539"}
pipeline_flags_not_supported:
  - "B05 2C/3C/4C: 'segment margins given only after three analyst prompts' -- NOT SUPPORTED (given in first answer, SUSAN-T p.5 l.124-132)"
  - "B05 2B: cash conversion and trading 'raised only when an analyst pushed' -- NOT SUPPORTED (never raised)"
  - "B05 2D/4A/4D: inventory-change credit as unrealised profit, 'PBT flips to loss' -- OVERSTATED (cost reversal; real issue is Rs 9.33 Cr cash into FG)"
  - "B06 Q5: Feb-2027 target 'aggressive' -- OVERSTATED (Rs 10.30 Cr brownfield compared to greenfield/CCV projects)"
  - "B06 2A: DIACABS order book 'grew from INR1,900 crore' -- NOT SUPPORTED (1,900 is revenue), context only"
  - "B06 Q4: DYCL government share 'falling' -- NOT SUPPORTED (12/13/13/16%), context only"
promise_delivery_spot_checks: {checked: 4, confirmed: 4, wrong: 0}
credibility_grade_concur: "concur -- C holds under the single-transcript cap; drop the unsupported 'three prompts' ground and add the 24.39% implausibility, the unvolunteered QoQ decline and the Rs 700-800 Cr claim"
findings:
  - {severity: "MAJOR", location: "B05 1B/2D/4B; B06 Q6", finding: "MISSED: 24.39% winding-wire margin equals revenue share and contradicts management's own 10-15% range; hold margin-bridge inputs until audio or segment disclosure resolves it"}
  - {severity: "MAJOR", location: "B05 1A/1B/4A", finding: "MISSED: Rs 700-800 Cr peak revenue claim unrecorded and untested against peer asset turns"}
  - {severity: "MAJOR", location: "B05 all sections", finding: "MISSED: QoQ revenue -17.5%, PBT -38.2%, margin down ~200 bps not stated; seasonal reading also not stated"}
  - {severity: "MAJOR", location: "B05 2D, 4A #3, 4D", finding: "OVERSTATED: inventory-change credit is a cost reversal, not unrealised profit; restate as working-capital/cash flag with the seasonal reading"}
  - {severity: "MAJOR", location: "B05 2C, 3C, 4C", finding: "NOT SUPPORTED: segment margins were given in the first answer, not after three prompts"}
  - {severity: "MINOR", location: "B05 1A/1B/1C", finding: "PARTIAL: third form of HT/MVCC guidance (FY27 mix ~30-35%) missing"}
  - {severity: "MINOR", location: "B05 methodology/1C", finding: "PARTIAL: transcript is edited summary; 50% text out of order; call date 14/18/19 Aug; name audio as LBF4 tie-breaker"}
  - {severity: "MINOR", location: "B05 1B", finding: "MISSED: current HT/MVCC share also stated 10-15%"}
  - {severity: "MINOR", location: "B05 1A/1B; B06 Q2", finding: "MISSED: ~20% called net margin in Q3"}
  - {severity: "MINOR", location: "B05 2A", finding: "MISSED: PR says 'significant portion' of order book in 3 months"}
  - {severity: "MINOR", location: "B05; B06", finding: "MISSED: no volume/price split of growth"}
  - {severity: "MINOR", location: "B05 4D; B06 Q5", finding: "PARTIAL: 'ahead of schedule' heading vs 'on track' body"}
  - {severity: "MINOR", location: "B05 3C", finding: "PARTIAL: implicit 'last two to three years' growth anchor not recorded"}
  - {severity: "MINOR", location: "B06 Q1/Q2", finding: "PARTIAL: DYCL 10-11% B2B margin ceiling not used; DYCL called silent"}
  - {severity: "MINOR", location: "B06 2A/2E", finding: "PARTIAL: DYCL industry-wide Apr-May booking slump not set against SUSAN order book"}
  - {severity: "MINOR", location: "B05 2D; B06 2E", finding: "MISSED: DIACABS MV seasonality/site delivery not linked to SUSAN Q1 FG build"}
  - {severity: "MINOR", location: "B06 Q5", finding: "OVERSTATED: 'aggressive' Feb-2027 timeline rests on non-comparable projects"}
  - {severity: "MINOR", location: "B06 Q5", finding: "Anchor misattributed: 'end of H2 only' quote is DYCL Oct-2025 call, not Q3 FY26"}
  - {severity: "MINOR", location: "B06 2A", finding: "NOT SUPPORTED (context): DIACABS 1,900 Cr is revenue, not prior order book"}
  - {severity: "MINOR", location: "B06 Q4", finding: "NOT SUPPORTED (context): DYCL government share rose to 16%"}
  - {severity: "MINOR", location: "B05 2B", finding: "Internal inconsistency on which topics analysts raised"}
critical_count: 0
major_count: 5
minor_count: 16
material_found: 8
material_caught: 5
acceptance_rate: 62.5
coverage_basis: "8 material of 21 listed; 5 found by pipeline (3 fully caught, 2 partially caught; partial counted as found per rule 3 definition); strict fully-caught rate 37.5%; 8 of 8 corpus transcripts read (1 main, 7 peer), 15-transcript design unreachable"
```
