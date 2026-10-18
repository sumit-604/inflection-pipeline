# A5 ADVERSARY / COMPLETENESS AUDIT: ROLE 5 ADDENDUM. Tata Communications Limited (TATACOMM), Q2 FY27

Review under audit: runs/tatacomm-q2fy27/work/review_tatacomm_q2fy27.md (1,478 lines; Role 5 section rev L761-1225; addendum passages tagged "(Role 5 addendum)" elsewhere).
Scope (task brief): (0) deliverable gate on the whole review; (1) coverage of the CONCALL ledger and the A3 concall findings; (2) arithmetic on every Role 5 figure and every addendum passage; (3) adversarial test of the three most management-favourable Role 5 readings and of the answer-status grades; plus a check that no Role 4 table or number changed.
Inputs read: A1 concall fulltext and structured file; A2 concall ledger; results and presentation fulltexts (filing cross-checks only); the review. Role 4 baseline for the "unchanged" check: audit_tatacomm_q2fy27_loop1.md (prior A5 output). From the A3 block I took the finding ID tokens only (grep -o), to fix the finding set. I read no A3 reasoning, no source transcript, no audio, nothing under inputs/.
Model: claude-opus-5-5. Audit date 2026-10-18.

Anchors. "C-L###" = concall fulltext line. "L###" = results fulltext line. "P-L###" = deck fulltext line. "rev L###" = review line. Source caveat applied throughout: the transcript is machine-made with inferred speakers. I treat a doubtful number as a transcription issue unless the context makes it clear.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading | Content | Status |
|---|---|---|---|
| 1. Summary narrative | rev L1233 | 17 lines (rev L1235-1251), inside the 10-20 band; addendum line rev L1250. Parts 1a (rev L1253-1257) and 1b (rev L1259-1269) added | PRESENT |
| 2. Sector intelligence | rev L1271 | rev L1273, with addendum sentence | PRESENT |
| 3. Business-model intelligence | rev L1275 | rev L1277, with addendum sentence | PRESENT |
| 4. Competition intelligence | rev L1279 | rev L1281, with addendum sentence | PRESENT |
| 5. Forward map | rev L1283 | Make-or-break reading plus 14 catalysts, each with a Bull and a Bear fork (rev L1285-1299) | PRESENT |

Gate result: PASS. Content issues inside parts 1a and 5 are findings C-A, C-B and F-F below. They are not gate failures.

---

## ROLE 4 UNCHANGED CHECK

| Test | Result |
|---|---|
| Role 4 P&L figures vs filing | 1A values match L135-L167 (revenue 6,687.89; Op EBITDA inputs; parent PAT 341.03 / 134.23 / 183.06) |
| Role 4 cash and debt figures vs filing | 5A values match L439-L441, L458-L480 (CFO 1,562.70; capex 1,500.69; associates 356.10; lease 292.51; dividend 498.78; interest 353.80) |
| Loop-1 audited values still in place | CCC -55.83 (rev L373); 185.39 / 192.08 attribution (rev L433-434); H1 +14.78% and +83 bps (rev L256-257); associate 21.4x / 139.96x (rev L449); Reg 52(4) 1.90% to 8.57% (rev L402) |
| Loop-1 STYLE notes L1-S1 to L1-S5 | All still unapplied (rev L345, L1242, L263, L1277, L22). This confirms that nobody edited the Role 4 text |
| Additions to Role 4 parts | All declared in the change log (rev L1213-1225): an answer-status column in 8.5A and 8.5B; paragraphs in 8.5C and 8.5D; the 8.5E table; monitorable rows 1, 2, 6 and 12 edited and rows 18-26 added; flag 16 replaced and flags 17-23 added; the verdict paragraph; brief additions; the merged YAML |

Result: no Role 4 number changed. One wording point is logged as STYLE S1: rev L4 and L763 say "Role 4 tables ... unchanged", but the review added columns and rows to Role 4 tables and edited existing cells, as its own log shows.

---

## 1. COVERAGE AUDIT

Method. I made a fresh pass over the concall fulltext. Turns: I used the moderator cues (analyst introductions at C-L183, L225, L244, L370, L443, L459; hand-overs at C-L37 and C-L144; Q&A opens at C-L176-178; connection lost at C-L240-242 and C-L442; poor audio at C-L448; close at C-L507-512) and every change of speaker. I merged one-word acknowledgements into the adjacent turn, as A1 does. Questions: I used the analyst's own numbering where the analyst gave it (C-L228 "That's my first question"; C-L239 "Second"), and a change of topic otherwise. Numbers: every line with a digit after its timestamp, plus numbers spoken as words. Forward statements: a grep for will, going to, should, coming quarters, future, goal, commit, planned, expect, next year, ahead of us.

| Category | A2 count | My fresh count | Orphan / missing | Status |
|---|---|---|---|---|
| Participants | 11 | 11 (4 management named, 6 analysts, 1 moderator) | none | PASS |
| Turns | 58 | 58 (A1 merge convention). Basis note: C-L435 "I don't think so." may be a CEO interjection inside analyst turn T044 | none | PASS (STYLE S11) |
| Questions | 19 | 19. C-L237 ("So we should expect this converting into revenue in the coming years, right?") is a confirming follow-up inside Q03, because the analyst numbers his next question "Second" at C-L239. The review cites its content (P15, C-L237-238). C-L436 sits inside Q16. C-L223 is not a question | none | PASS |
| Management numbers | 51 | 51, plus 2 spoken counts not emitted: "two significant wins" (C-L101) and "the last three calls" (C-L194). A1 emitted similar counts ("three buckets" R040, "four forms" R054) | rows not emitted, content cited (claims #15-#16) | PASS (STYLE S11) |
| Analyst numbers | 8 | 8 (C-L226 x2, L227, L362 x2, L420, L447, L488) | none | PASS |
| Forward statements | 55 | 55, plus C-L232 "Our focus is going to be constant currency growth" not emitted. A1 emitted similar focus or goal lines (R107, R136). Borderline lines not emitted: C-L229, L236, L485 | row not emitted; the line is cited (C-L232) | PASS (STYLE S11; substance used in finding C-B) |
| Qualifiers | 25 | 25 (spot check) | none | PASS |
| Entities | 40 | 40. UK, APAC and Americas (C-L64-65) are not emitted, while Middle East and Europe are. R091, R093 and R094 contexts point to other lines | none material | PASS (STYLE S11) |
| Dates | 19 | 19 | none | PASS |
| Structured IDs | 199 | 199 (R001-R199); ledger 199 of 199 referenced | none | PASS |
| A3 concall findings | 19 (C01-C19, from the ID tokens of the A3 block) | 19 in the review: preamble (rev L771); 7 FORWARD-SIGNAL and 9 AMBIGUOUS each map to an RQ row (rev L666-685); C16, C17 and C18 are marked NEUTRAL-FACT, with no question needed (rev L666) | none | PASS |

From ledger to review:
- Turns. Every T row falls inside a cited range: T001 (C-L27-37, rev L792); T002 (C-L38-144, rev L822); T003 (C-L145-176, rev L822); the CQ ranges (rev L946-964, from C-L188 to C-L504); the close (C-L510-512, rev L809).
- Questions. Q01-Q19 each have a CQ row (rev L946-964).
- A2 flags. The preamble dispositions them (rev L776-782). The flags it does not name are covered by line cites: SETTLEMENT_NOT_FINAL R186 and R188 (rev L857); NON_DISCLOSURE R197 (rev L956, L1075); SOURCE_PROVENANCE R175-R178 (rev L765); REPEAT_QUESTION (rev L969); CUT_OFF Q04 (rev L949).
- Orphan rows: none. Missing from ledger: none that changes a review number. The row-emission items are logged as STYLE S11, following the loop-0 precedent (S6-S11 were A1/A2 emission items). Each affected line is cited in the review. The specificity ratio stays at 0.20 (11 / 56 = 0.196).

Coverage verdict: PASS.

---

## 2. ARITHMETIC AUDIT (every Role 5 figure and addendum passage)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Lag from filing to call | 2 h 15 min | 13:45 to 16:00 = 2 h 15 min | L33; the call time is at P-L34 (review cites P-L33) | PASS (STYLE S2) |
| Call duration | 57.4 min | 00:57:22 = 57.37 min | C-L27, C-L512 | PASS |
| Q&A duration and share | 40.5 min; 70.6% | 00:16:43 to 00:57:13 = 40.50 min; 40.50 / 57.37 = 70.6% | C-L178, C-L510 | PASS |
| Claims inventory | 21 YES / 1 PARTIAL / 18 NO of 40; 52.5%; 16 backward | recount rev L826-865: 21 / 1 / 18; 21 / 40 = 52.5%; YES-and-Backward = 16 | rev L826-868 | PASS |
| FY27 double-digit bar | 5,304.71 | 1.10 x 4,822.46 = 5,304.71 | Role 4 1B (L135-146) | PASS (basis: see C-B) |
| H2 need and growth | 2,652.69; +5.60% | 5,304.71 - 2,652.02 = 2,652.69; H2 FY26 4,822.46 - 2,310.43 = 2,512.03; 2,652.69 / 2,512.03 = +5.60% | Role 4 1B | PASS (basis: see C-B) |
| Headroom at Q2 run-rate | 191.07 | 2 x 1,421.88 - 2,652.69 = 191.07 | Role 4 1B | PASS |
| CQ grade tally | A0 B9 C8 D1 E0 n.a.1 = 19 | recount rev L946-964: same | rev L966 | PASS (CQ17 judgment: STYLE S8) |
| Analyst mix | 12 + 3 + 4 = 19 | same | rev L971 | PASS |
| "Most repeated": Digital margin path | "four questions, three analysts" | CQ02 Balaji, CQ09 Vibhor, CQ14 Avneesh, CQ17 Harbik = 4 analysts | rev L969; C-L218, L351-356, L414, L447-453 | **FAIL (minor, F-F b)** |
| Congratulations | 4 of 6 | C-L186, L246, L446, L460 | rev L972 | PASS |
| Specificity ratio | 11 / 55 = 0.20 | 0.200 | rev L1065-1068 | PASS (criterion note: STYLE S9) |
| Defensive phrases | 15 (deferral 4) | deferral 5: C-L213, L217, **L408 "You will hear more from us on this."**, L409, L416; total 16 | rev L1074, L1080; flag 23 rev L757; YAML rev L1353 | **FAIL (minor, F-F c)** |
| Answer-status count | 0 / 7 / 2 / 22 of 31 | recount rev L613-648: 0 / 7 / 2 / 22 | rev L607, L911, L1359 | Arithmetic PASS. Grade validity: F-A |
| 7A tally | 7 / 4 / 1 / 9 of 21 | recount rev L1102-1122: same | rev L1124, L1356 | Arithmetic PASS. Tag validity: F-B, F-C, F-D |
| Revenue YoY | +9.64% | 6,687.89 / 6,099.75 = +9.64% | L135 | PASS |
| Op EBITDA YoY; margin | +21.15%; 21.26% | 1,421.88 / 1,173.62 = +21.15%; 1,421.88 / 6,687.89 = 21.26% | L135-146 | PASS |
| H1 Op EBITDA YoY | +14.78% | 2,652.02 / 2,310.43 = +14.78% | L135-146 | PASS |
| Parent PAT YoY | +86.29% | 341.03 / 183.06 = +86.29% | L166 | PASS |
| Data revenue YoY, filed vs PR | +11.65% vs 12.2% | 5,810.99 / 5,204.47 = +11.65%; 5,810 / 5,179 = +12.18% | L235, L1383 | PASS |
| Digital revenue; margin | +18.6%; -3.6% | 3,016 / 2,542 = +18.65%; 107 / 3,016 = 3.55% | L1384, P-L138 | PASS |
| "Less than half" test | Q1 loss > 214; Q1 revenue > 3,101; 107 = 51.4% of 208.10 | 2 x 107 = 214; 214 / 0.069 = 3,101.4; 0.069 x 3,016 = 208.10; 107 / 208.10 = 51.4% | C-L59, P-L138, P-L142, L1384 | PASS |
| Net debt / TTM Op EBITDA | 2.17x | TTM 4,822.46 - 2,310.43 + 2,652.02 = 5,164.05; 11,197.04 / 5,164.05 = 2.168 | Role 4 5A, 1B | PASS |
| Role 4 basis | 2.11x | 11,197.04 / 5,304.04 = 2.111 | Role 4 5A | PASS |
| 31-Mar-2026 ratio; change | 1.99x; +0.18x | 9,590.44 / 4,822.46 = 1.989; 2.168 - 1.989 = 0.18 | Role 4 5A | Arithmetic PASS. Tag: F-B |
| Q1 FCF, conditional | (149.99) | 62.01 - 212 = -149.99 | C-L164; Role 4 5A | PASS |
| H1 CFO / Op EBITDA | 58.92% | 1,562.70 / 2,652.02 = 58.92% | L441 | PASS |
| H1 capex YoY | +31.71% | 1,500.69 / 1,139.43 = +31.71% | L458 | Arithmetic PASS. Tag: F-C |
| ROCE, filed bases | 15.84% | H1 annualised 2,343.28 / 14,796.19 = 15.84%; **TTM 2,201.40 / 14,796.19 = 14.88%** (TTM EBIT = 1,995.72 - 965.96 + 1,171.64); Q2 annualised 2,723.76 / 14,796.19 = 18.41% | L247; Role 4 6A | Arithmetic PASS. Tag: F-D |
| CRA contingent vs 31-Mar-2026 parent equity | 48.1% | 1,658 / 3,447.04 = 48.10% | C-L162; L363 | PASS |
| Digital margin QoQ gain (analyst) | 330 bps | -6.9% to -3.6% = 3.3 pp | C-L58, C-L447 | PASS |
| DoT reconciliation | 7,513.71 | 7,844.57 - 276.68 - 54.18 = 7,513.71 | L545-548, L560-562 | PASS |
| Currency share, Data | "about half" | (12.2 - 6) / 12.2 = 51%; on filed growth (11.65 - 6) / 11.65 = 48.5% | C-L148, C-L152, L235 | PASS |
| Currency share, EBITDA | "about half" (~10% vs 21.2%) | if Q2: (21.15 - 10) / 21.15 = 53%; **if H1: (14.78 - 10) / 14.78 = 32%** | C-L232 (period not stated) | Not resolvable from the extract: C-B |
| Media catalyst timing | about 7 quarters | Q3 FY27 to Q2 FY29 = 7 quarters | RQ44; date PENDING LIVE VERIFICATION | PASS |

Two minor count mismatches (F-F b, F-F c). Every other sum ties.

---

## 3. ADVERSARIAL READ

### 3A. The three most management-favourable readings in the Role 5 section

**Read 1. 7A: Cash capex "trended up" = CONFIRMED on H1 (rev L1117).**
- Bear counter, from the extract. C-L166 says "Cash CapEx trended up **this quarter**". That is a claim about a quarter. The filing gives cash capex only for H1 FY27, H1 FY26 and FY26 (L458). Neither Q1 FY27 nor Q2 FY26 capex is filed. The review's own cell says "Q2 vs Q1 ND".
- Survives? Yes. A half-year YoY rise (+31.71%) does not confirm a quarterly claim.
- Graft: re-tag UNVERIFIABLE, with H1 +31.71% as context. This is the mirror image of Read B1 below: one "this quarter" claim is confirmed on half-year data and another is contradicted on half-year data. Use the same rule for both (finding F-C).

**Read 2. 7A: ROCE 15.9% = PARTIALLY CONFIRMED, "level close" (rev L1118; 8D rev L1170).**
- Bear counter. The definition is ND. Three filed bases give three answers: 14.88% (TTM operating EBIT on closing capital), 15.84% (H1 annualised) and 18.41% (Q2 annualised) (L247; Role 4 6A capital). The review tied the CFO's 2.17 to TTM EBITDA (rev L1113). On that same TTM basis, ROCE is 14.88%, 102 bps below 15.9%. A match on one chosen basis is not a confirmation, and the +71 bps YoY cannot be tested (no 30-Sep-2025 balance sheet).
- Survives? Yes.
- Graft: re-tag UNVERIFIABLE (definition ND; filed bases 14.88% to 18.41%) (finding F-D).

**Read 3. The answer-status grades (8.5A and 8.5B, rev L613-648; 7 PARTIALLY).**
- Q5 (capex guidance; net debt / EBITDA ceiling, rev L617). Its cell says "no guidance, no ceiling". "Trended up" (C-L166) and "held steady" (C-L171) look backward. Neither requested item was given.
- Q31 (GPU cost in Rs; share in use; depreciation treatment, rev L648). Its cell says "no rupee, no %, no treatment". C-L412 states a focus only. None of the three items was given.
- Q2 (Digital rupee losses for Q1 FY27, Q2 FY26 and FY26, rev L614). Its cell says "no rupee series". The -6.9% (C-L58) repeats the deck (P-L142). "Less than half" (C-L59) repeats the press release "halved" (L1366). Q2 FY26 and FY26 were not mentioned. The call added nothing beyond the documents the question was built on. This is the weakest of the three, but it still gives no requested item.
- Forks. Every 8.5 row was written with a Bull and a Bear answer before the call. The addendum grades a status but never records which fork the call matched. Several rows match their pre-set bear text word for word:
  - Q1 bear "or no number given" (rev L613): no number came (C-L365-366).
  - Q2 bear "series not given".
  - Q3 bear "No date" (C-L415). Its definition half lands on the bull side: "EBITDA" (C-L158).
  - Q5 bear "No ceiling".
  - Q25 bear "No reconciliation": the CFO repeats 12.2% (C-L148).
  - Q30 bear "Not disclosed" (C-L379).
- The forward-map concall fork (rev L1287) reads "Bear: no number, or a large one-off". The outcome line then says "no number given ... Neither fork resolved". That contradicts its own bear text. 8.5C (rev L656) records Q1 as "PARTIALLY (an assertion, no number)" and does not say that the pre-set bear answer fired.
- Symmetric bar (Rule J). Q28 is graded EVADED (rev L645). The CEO said "We are on track" (C-L197) and "This year, we will absolutely deliver what we have promised" (C-L211). Those words sit near the Q28 bull text ("Target stands and is on track"), but name no target. Exchange 3 (rev L998) lists "whether they stand" as "Not said". That overstates the silence. The grade can stand, but the cell must quote C-L197 and C-L211.
- Survives? Yes.
- Grafts:
  - Regrade Q2, Q5 and Q31. PARTIALLY needs at least one requested item. Use NOT ADDRESSED and widen its definition at rev L607 to "no requested item given", or state why each row keeps PARTIALLY. The recount becomes 0 / 4 / 2 / 25 (finding F-A).
  - Record the fork outcome per graded row. Correct the forward-map concall line and 8.5C so that each says the bear answer fired (findings C-A, M-A).

### 3B. Other favourable readings tested (no new graft, or STYLE only)

| Reading | Counter | Result |
|---|---|---|
| 8A Digital breakeven "ON TRACK on direction" (rev L1149) | Two data points; the rupee series does not reconcile (7A "less than half" row, rev L1109); the perimeter moves (Role 4 cross-read) | The counter is already in the review (rev L1109, RQ35, rev L312-320). STYLE S6: add a pointer |
| 6D "Candour on currency is a positive"; "the cc growth figures, both in the CFO's script" (rev L1090) | The cc EBITDA "around 10%" came from the CEO in Q&A, after an analyst's cc question (T012, C-L232). Only cc Data ~6% and Digital cc "double digits" were in the CFO's script (C-L151-153). Neither appears in the press release (rev L1011) | The candour credit stands for cc Data. The attribution is wrong: F-F e |
| 7A Q2 FCF 212 = PARTIALLY CONFIRMED on sign (rev L1115) | The sign test alone is weak. A stronger, two-sided check exists. On CFO less capex, the 212 FCF and 72% conversion give Q2 CFO about 1,024 (0.72 x 1,422) and Q2 capex about 812. Q1 capex is then about 689 (1,500.69 - 812), which fits "trended up" and the filed H1 totals (L441, L458) [DERIVED, MGMT basis] | Tag stands. STYLE S5: add the joint check, labelled MGMT-on-MGMT |
| 0C "the Q&A share is healthy" (rev L814) | 10 gaps over 25 s lose Q&A content (C-L18); CQ04 was cut off; one analyst dropped twice | The review notes all three (rev L812, L778-779). Stands |

### 3C. Bear readings that go past the extract (Rule J: same bar both ways)

**B1. "Held steady" = CONTRADICTED (7A rev L1114; diag 4(b) rev L871; 5B rev L1034; brief 1b rev L1265; flag 19 rev L753; 8E rev L1181; net impact rev L1194; RQ37 rev L675).**
- C-L171 reads: "The net debt to EBITDA has held steady despite dividend payments **this quarter**." The comparator is the start of Q2, 30-Jun-2026. The filing has no 30-Jun-2026 balance sheet. The 7A cell itself says "UNVERIFIABLE against 30-Jun-2026".
- Testing against 31-Mar-2026 (1.99x to 2.17x) tests a half-year claim that management did not make.
- The claim fits the filing if about 1,077 of the 1,606.60 H1 rise fell in Q1. Q1 TTM Op EBITDA is 4,822.46 - 1,136.81 + 1,230.14 = 4,915.79, and 2.17 x 4,915.79 = 10,667 [DERIVED]. The H1 dividend paid was 498.78 (L479).
- Re-tag UNVERIFIABLE, with the March-to-September rise as context. Remove "Leverage was called steady when it rose" and the 8E "narrative contradicts filing" bullet, or restate both as unverified (finding F-B).

**B2. cc EBITDA ~10% read as Q2, and the FY27 promise read on the reported basis (flag 17 rev L751; brief 1a rev L1257; Exchange 1 rev L983; 5A rev L1011; 8D rev L1172; flag 22 rev L756; Exchange 3 rev L999; Step 2 rev L899).**
- C-L232 gives "around 10% on a year to year basis" with no period. RQ32 (rev L670) asks whether it is Q2 or H1. If it is H1 (reported 14.78%), currency is about a third of EBITDA growth, not half.
- The same line also says "Our focus is going to be constant currency growth" (C-L232). That bears on RQ33 (rev L671): is the FY27 double-digit promise reported or cc? Flag 22, brief 1a and Exchange 3 treat the bar as +5.60% reported in H2. On a cc basis, the bar is cc growth of about 10% or more.
- The review leaves both points open in RQ32 and RQ33, but closes them in the flags and the brief. Name both readings and the separating observation in each place. "About half" stands for Data (finding C-B).

**B3. The CRA contingent called "new" and "undisclosed" (flag 18 rev L752; 8E rev L1180; net impact rev L1194; 5A type rev L1010).**
- C-L161-162 describes "a long-standing tax matter" whose "contingent liability as on 31st of March 2026 stood at Rs. 1658 crores". That dates it to the last audited year-end. 7A (rev L1119) and brief 1b (rev L1268) correctly say it cannot be checked here, because the FY26 Annual Report is not in this run.
- What is new is the in-principle settlement. Its direction is ND: management says "pleased" (C-L161); amount, provision and cash are ND.
- Reword flag 18, 8E and the net-impact bullet. Change the 5A type from "Negative surprise" to "tax resolution, direction ND" (finding C-C).

**B4. VAT silence read as selective disclosure (5B rev L1029; flag 20 rev L754; 6D rev L1090).**
- The same-day filing says "the Group awaits the National Court's decision" (L572). The call's silence fits a second reading: there was no decision to report.
- RQ38 (rev L676) already holds the separating observation (delivered, deferred or reserved). 5B and flag 20 must name both readings (finding M-B).

### 3D. Mandatory acquisition-economics probe

The call describes the Commotion acquisition ("Through our commotion acquisition", C-L87; "the AI operating system we have acquired", C-L427; "Our real moat", C-L99).
- Consideration: FY26 "Acquisition of Subsidiary (net off acquired cash)" 136.96 (L463). The link to Commotion is an INFERENCE by date (wef 01-Dec-2025, L1253-1254).
- Target PAT: NOT FOUND. Commotion revenue: NOT FOUND, because management runs Commotion and SaaS "as one entity ... as one PNO" (C-L397-398).
- Multiple: 136.96 / PAT NOT FOUND, so it cannot be computed. Quality markers (ROCE, debt, cash, customer tenure): ND.
- The call makes no "cheap" or "accretive" claim. It claims a moat with no revenue line.
- The bear reading (moat and contribution untestable) is in the review (5A rev L1014; RQ41 rev L679).
- Probe SATISFIED. STYLE S12: state the multiple as NOT FOUND in the 5A Commotion row and add Commotion PAT or EBITDA to RQ41.

---

## FINDINGS (tagged; every FACTUAL, MISSING and CONTRADICTION finding loops to A4)

| ID | Type | Gap | Fix | Loop |
|---|---|---|---|---|
| F-A | FACTUAL | Q2, Q5 and Q31 are graded PARTIALLY, but the review's own cells say that no requested item came (rev L614, L617, L648) | Regrade to NOT ADDRESSED and widen the definition at rev L607, or justify each row. Recount 0 / 4 / 2 / 25. Align rev L607, L656, L662, L684, L718, L754, L911, L1194, the YAML (rev L1359, flag rev L1469) and the analyst note | A4 |
| C-A | CONTRADICTION | The forward-map concall fork (rev L1287) has bear text "no number", and the outcome line says "no number given ... Neither fork resolved". 8.5C (rev L656) logs Q1 as PARTIALLY, though its pre-set bear answer "or no number given" (rev L613) fired | State that the bear fork fired for the concall bullet and for Q1. Keep "Q3 margin now decides" as the next test | A4 |
| M-A | MISSING | No fork outcome is recorded for the graded 8.5 rows. Bear text matched for Q1, Q2, Q3 (date half), Q5, Q25 and Q30. Q3's definition half matched the bull side. Q28's wording (C-L197, C-L211) sits near its bull text | Add the fork outcome (bull / bear / neither) to each graded row. Quote C-L197 and C-L211 in Q28, and correct Exchange 3 "Not said: whether they stand" (rev L998) | A4 |
| F-B | FACTUAL | "Held steady" is tagged CONTRADICTED against 31-Mar-2026. C-L171 ("this quarter") sets the comparator at 30-Jun-2026, which the filing does not give | Re-tag UNVERIFIABLE (context: 1.99x to 2.17x; the claim holds if about 1,077 of the H1 rise fell in Q1). Update rev L871, L1034, L1114, L1124, L1265, L753, L1181, L1194, L675, the YAML (flag rev L1468, filing_crosscheck rev L1356) and the analyst note | A4 |
| F-C | FACTUAL | "Cash CapEx trended up this quarter" is tagged CONFIRMED on H1 YoY data. No quarterly capex is filed (L458) | Re-tag UNVERIFIABLE, with H1 +31.71% as context (rev L1117); retally rev L1124 and the YAML | A4 |
| F-D | FACTUAL | ROCE 15.9% is tagged PARTIALLY CONFIRMED on one chosen basis. Filed bases run from 14.88% (TTM, the basis that ties 2.17) to 18.41% | Re-tag UNVERIFIABLE (definition ND); show the bases (rev L1118, L1170) | A4 |
| C-B | CONTRADICTION | RQ32 and RQ33 leave the cc EBITDA period and the FY27 promise basis open. Flags 17 and 22, brief 1a, Exchanges 1 and 3, 5A, 8D and Step 2 state them as Q2 and reported. C-L232 "Our focus is going to be constant currency growth" is not used | Name both readings in each place: Q2 = about half, H1 = about a third; reported bar +5.60% in H2, cc bar about 10% or more. "About half" stands for Data. Update the YAML flags (rev L1466, L1471) and the analyst note | A4 |
| C-C | CONTRADICTION | The CRA contingent is called "new" (flag 18) and an "undisclosed material risk" (8E, rev L1180). C-L161-162 dates it to 31-Mar-2026 as "long-standing", and 7A and 1b say it cannot be checked in this run | Reword as a pre-existing contingent (FY26 AR status ND) moving to settlement, direction ND. Change the 5A type (rev L1010); update the net impact (rev L1194) and the YAML flag (rev L1467) | A4 |
| M-B | MISSING | VAT silence is read only as selective disclosure (rev L1029, L754). The same-day filing says the decision is still awaited (L572) | Add the second reading and name RQ38 as the separating observation | A4 |
| F-F | FACTUAL (minor) | (a) Brief 1a (rev L1257): "Management did not raise them". The CFO raised net debt (C-L169-171) and a tax dispute (C-L161-163). (b) 4B (rev L969): "three analysts" should be four. (c) 6C (rev L1074, L1080): deferral 4 should be 5 (C-L408), total 15 should be 16; also flag 23 (rev L757) and the YAML (rev L1353). (d) Step 1 diag 2 (rev L869) lists #2 (the new transformation head) as new on the call, but the same-day deck names "Narottam Sharma" under Transformation (P-L101-104). (e) 6D (rev L1090): the cc EBITDA figure was not in the CFO's script (C-L232, CEO, Q&A) | Correct each item | A4 |

Effect on the concall verdict. WEAKENED (rev L1194) rests on five reasons. B1 removes one ("leverage called steady when it rose"). B3 reframes one ("a new 1,658 Cr contingent"). B2 halves one for EBITDA. These remain: cc Data about half (C-L152); the cause of the profit step still unnamed; specificity 0.20 and 16 hedges; pre-set bear answers fired on six rows; 25 of 31 rows not addressed after the regrade. WEAKENED probably survives, but A4 must restate its reasons. The protocol verdict PROCEED WITH FLAGS and the INDETERMINATE-WITH-DIRECTION cash classification do not change.

---

## VERDICT

**INCOMPLETE. Loop back to A4.** Five FACTUAL findings (F-A, F-B, F-C, F-D, F-F), two MISSING (M-A, M-B) and three CONTRADICTION (C-A, C-B, C-C). None needs a new extraction or enumeration. A1, A2 and A3 do not re-run. Gate 0 passes. Coverage passes. Arithmetic passes, apart from two minor counts. No Role 4 number changed.

---

## STYLE NOTES (logged, no re-run)

- S1. Rev L4 and L763 say "Role 4 tables and numbers unchanged". The 8.5A and 8.5B tables gained a column, monitorable cells were edited and rows added, and flag 16 was replaced (log rev L1213-1225). Write "Role 4 numbers and question text unchanged; columns, rows and status notes added as logged". The merged YAML analyst note (rev L1474) now holds Role 5 content only. The change log says "merged".
- S2. 0C (rev L806) cites P-L33 for the call time. The time is on P-L34.
- S3. 0B (rev L792, L797). The moderator is probably "Inba" (C-L38, C-L43; A1 R066). Cite the deck spelling "Narottam Sharma" (P-L104); "Narotan" is the machine rendering.
- S4. 7A (rev L1110): "cost reduction carries the rest" overstates. The part outside Digital is unexplained, and Digital loss reduction can itself run through cost lines. The CFO's claim (C-L157) reads YoY, but the bound is QoQ.
- S5. 7A FCF row (rev L1115): add the joint MGMT check (Q2 capex about 812 vs Q1 about 689) as the stronger consistency test.
- S6. 8A (rev L1149): add "two points; the rupee series does not reconcile (7A)" to "ON TRACK on direction".
- S7. 8B (rev L1161): "The company uses TTM" is an inference (RQ37 asks for the definition). Label it INFERENCE.
- S8. CQ17 grade B (rev L962) looks generous. The answer gives YoY revenue growth for a QoQ question and no split. C fits the review's own pattern ("narrative, not numbers"). This is a judgment. A4 may regrade in the same loop.
- S9. 6B criterion (rev L1066). R101 and R106 are treated as binary events in the promise log (P18, P9), and R111 and R114 carry a binary event or a named period, but none of the four is counted as quantified. Counting them gives 15 / 55 = 0.27. That is still below 0.3, so the conclusion holds.
- S10. YAML RQ47 from_finding_id is "C01" (rev L1422). The 8.5E table (rev L685) says "Role 5 Step 7A".
- S11. A1/A2 row emission, following the loop-0 precedent:
  - Spoken counts not emitted as NUMBER rows: "two significant wins" (C-L101), "the last three calls" (C-L194).
  - Focus line not emitted as a FORWARD row: C-L232 "Our focus is going to be constant currency growth".
  - Regions not emitted as entities: UK, APAC, Americas (C-L64-65).
  - Row contexts that point to other lines: R091, R093, R094.
  - C-L435 may be a CEO interjection inside T044.
  - The review cites every affected line. No review number changes.
- S12. Acquisition probe: state "136.96 / PAT NOT FOUND" in the 5A Commotion row (rev L1014). Add Commotion PAT or EBITDA to RQ41 (rev L679).
- S13. Brief 1a (rev L1257): "Management moved them to an investor call in February 2027". The CEO deferred "the longer-term growth" (C-L213-214), not the targets by name. Tag it INFERENCE.
- S14. The loop-1 STYLE notes L1-S1 to L1-S5 remain unapplied in Role 4 and carry forward.

---

```yaml
stage: A5-adversary
company: "TATACOMM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - {metric: "4B most-repeated Digital margin path: analyst count", a4_value: "three analysts", recomputed: "four analysts (CQ02 Balaji, CQ09 Vibhor, CQ14 Avneesh, CQ17 Harbik)", source_line: "rev L969; C-L218, C-L351-356, C-L414, C-L447-453"}
  - {metric: "6C defensive phrases (deferral)", a4_value: "deferral 4; total 15", recomputed: "deferral 5 (adds C-L408 'You will hear more from us on this.'); total 16", source_line: "rev L1074, L1080, L757, L1353; C-L213, C-L217, C-L408, C-L409, C-L416"}
surviving_bear_counters:
  - {claim: "7A: cash capex 'trended up' CONFIRMED on H1 (rev L1117)", counter: "C-L166 is a 'this quarter' claim; no quarterly capex is filed (L458 gives H1 and FY only); re-tag UNVERIFIABLE", source_line: "C-L166; L458", type: "FACTUAL"}
  - {claim: "7A: ROCE 15.9% PARTIALLY CONFIRMED, level close (rev L1118)", counter: "definition ND; filed bases 14.88% (TTM, the basis that ties 2.17) to 18.41% (Q2 annualised); re-tag UNVERIFIABLE", source_line: "C-L172; L247; rev L1113", type: "FACTUAL"}
  - {claim: "Answer status: 7 PARTIALLY of 31 (rev L607, L613-648)", counter: "Q2, Q5, Q31 give no requested item (the review's own cells say so); Q1 and the forward-map concall fork hit their pre-set bear answer 'no number' yet are logged as partial or unresolved", source_line: "rev L613, L614, L617, L648, L656, L1287; C-L58-59, C-L166-171, C-L365-366, C-L412; L1366; P-L142", type: "FACTUAL"}
findings_by_type:
  factual:
    - "F-A Q2, Q5, Q31 graded PARTIALLY with no requested item given (rev L614, L617, L648); regrade or justify; recount 0/4/2/25 and align rev L607, L656, L662, L684, L718, L754, L911, L1194, YAML, analyst note"
    - "F-B 'held steady' tagged CONTRADICTED vs 31-Mar-2026; C-L171 'this quarter' sets the 30-Jun-2026 comparator, not filed; re-tag UNVERIFIABLE (rev L1114, L871, L1034, L1265, L753, L1181, L1194, L675)"
    - "F-C 'Cash CapEx trended up this quarter' tagged CONFIRMED on H1 YoY; no quarterly capex filed (L458); re-tag UNVERIFIABLE (rev L1117)"
    - "F-D ROCE 15.9% tagged PARTIALLY CONFIRMED on one basis; filed bases 14.88% TTM to 18.41% Q2 annualised; re-tag UNVERIFIABLE (rev L1118, L1170)"
    - "F-F minor: (a) brief 1a rev L1257 'Management did not raise them' but CFO raised net debt C-L169-171 and a tax dispute C-L161-163; (b) rev L969 three analysts should be four; (c) rev L1074/L1080 deferral 4 to 5 (C-L408), total 15 to 16, also flag 23 and YAML; (d) rev L869 #2 listed new on call but deck names Narottam Sharma P-L101-104; (e) rev L1090 cc EBITDA was CEO in Q&A (C-L232), not the CFO script"
  missing:
    - "M-A fork outcomes not recorded on graded 8.5 rows: bear text matched for Q1, Q2, Q3 (date), Q5, Q25, Q30; Q3 definition and Q28 wording (C-L197, C-L211) near bull; Exchange 3 rev L998 'whether they stand' overstated"
    - "M-B VAT silence read only as selective disclosure (rev L1029, L754); same-day filing L572 says decision still awaited; add second reading, RQ38 as separator"
  contradiction:
    - "C-A forward-map concall fork rev L1287 bear 'no number' fired but outcome says 'Neither fork resolved'; 8.5C rev L656 logs Q1 PARTIALLY though its bear 'or no number given' (rev L613) fired"
    - "C-B RQ32/RQ33 (rev L670-671) leave cc EBITDA period and FY27 promise basis open; flags 17 and 22, brief 1a, Exchanges 1 and 3, 5A, 8D, Step 2 state Q2 and reported; if H1, currency is about a third of EBITDA growth; C-L232 'Our focus is going to be constant currency growth' unused"
    - "C-C CRA contingent called 'new' (flag 18 rev L752) and 'undisclosed material risk' (8E rev L1180) though C-L161-162 dates it to 31-Mar-2026 as long-standing and 7A/1b say it cannot be checked in this run; 5A type 'Negative surprise' prejudges direction"
  style:
    - "S1 rev L4/L763 'Role 4 tables unchanged' vs added column, rows, edited cells, flag 16 replaced (logged rev L1213-1225); merged YAML analyst note is Role 5 only"
    - "S2 call time is P-L34, not P-L33"
    - "S3 moderator likely 'Inba' (C-L38, C-L43); cite deck spelling Narottam Sharma P-L104"
    - "S4 7A rev L1110 'cost reduction carries the rest' overstates; remainder unexplained; CFO claim YoY vs QoQ bound"
    - "S5 7A FCF row: add joint MGMT check (Q2 capex ~812 vs Q1 ~689)"
    - "S6 8A rev L1149 add two-point and non-reconciling rupee series caveat"
    - "S7 8B rev L1161 'company uses TTM' label INFERENCE"
    - "S8 CQ17 grade B looks generous (YoY data for a QoQ question, no split); judgment"
    - "S9 6B criterion: R101, R106, R111, R114 not counted; 15/55 = 0.27, still below 0.3"
    - "S10 YAML RQ47 from_finding_id C01 vs table 'Role 5 Step 7A'"
    - "S11 A1/A2 row emission: C-L101, C-L194 counts; C-L232 focus line; UK/APAC/Americas entities; R091/R093/R094 contexts; C-L435 interjection in T044; all lines cited in review"
    - "S12 acquisition probe: state '136.96 / PAT NOT FOUND' in 5A Commotion row; add Commotion PAT/EBITDA to RQ41"
    - "S13 brief 1a 'moved them to an investor call in February 2027' tag INFERENCE (C-L213-214)"
    - "S14 loop-1 STYLE notes L1-S1 to L1-S5 still unapplied in Role 4; carry"
loop_back_to: "A4"
gap: "Role 5 readings fail on ten findings, all A4-side. FACTUAL: Q2/Q5/Q31 graded PARTIALLY with no requested item; 'held steady' CONTRADICTED and capex 'trended up' CONFIRMED both tested on half-year data for 'this quarter' claims (both UNVERIFIABLE); ROCE 15.9% PARTIALLY CONFIRMED on one basis (filed bases 14.88%-18.41%); five minor count/attribution errors. MISSING: fork outcomes per graded row; second reading of VAT silence (L572 'awaits'). CONTRADICTION: forward-map concall bear fork fired but called unresolved, Q1 likewise; cc EBITDA period and FY27 promise basis open in RQ32/RQ33 but closed in flags 17/22 and brief 1a; CRA called new/undisclosed though C-L162 dates it to 31-Mar-2026. Restate WEAKENED reasons; recount answer status and 7A tally."
style_notes:
  - "S1 reword 'Role 4 tables unchanged' to 'numbers and question text unchanged; additions as logged'"
  - "S2 P-L33 to P-L34"
  - "S3 moderator Inba; deck spelling Narottam Sharma"
  - "S4 'cost reduction carries the rest' to 'the rest is unexplained'"
  - "S5 add joint MGMT FCF/capex check"
  - "S6 add caveat to 8A Digital ON TRACK"
  - "S7 tag 8B TTM statement INFERENCE"
  - "S8 reconsider CQ17 B to C"
  - "S9 note specificity criterion sensitivity (0.20-0.27)"
  - "S10 align RQ47 source label"
  - "S11 A1/A2 emission items carried, no loop"
  - "S12 state Commotion multiple as NOT FOUND; add PAT ask"
  - "S13 tag February move of targets INFERENCE"
  - "S14 loop-1 Role 4 style notes carried"
analyst_note: "Coverage and sums are clean. My fresh pass gives 58 turns and 19 questions on A1's convention. All 199 rows fall in cited ranges, and C01-C19 all map. Every Role 5 sum recomputes, apart from two minor counts. The failures are in the readings, and they run both ways. The answer grades are soft. Q2, Q5 and Q31 are PARTIALLY, but the review's own cells say no requested item came. Q1 and the forward-map concall fork hit their pre-set bear answer, 'no number', yet are logged as partial or unresolved. 7A tests two 'this quarter' claims on half-year data. It confirms capex 'trended up' and contradicts 'held steady'. No quarterly comparator is filed for either, so both are UNVERIFIABLE. ROCE 15.9% is called partly confirmed, but the filed bases run from 14.88% to 18.41%. Three bear readings go past the extract: the cc EBITDA period and the FY27 promise basis, the CRA contingent called new, and VAT silence read only as selective. WEAKENED probably survives on cc Data, the unnamed profit cause, specificity 0.20 and six bear forks. A4 must restate its reasons. No Role 4 number changed."
```

---
---

# LOOP 1 RE-AUDIT (Role 5 addendum, correction loop 1; fresh A5 instance, 2026-10-18)

This section supersedes the run-1 verdict and YAML block above. The run-1 record stays as written. The block at the end of this section is the current one; the same block is in work/blocks/a5-role5.yaml.

Scope (task brief, strictly):
1. Deliverable gate on the revised review.
2. Closure of run-1 findings F-A, F-B, F-C, F-D, F-F(a-e), M-A, M-B, C-A, C-B and C-C, with every changed figure recomputed from the concall and filing fulltexts.
3. The edited passages add no new FACTUAL, MISSING or CONTRADICTION finding, and no Role 4 number changed.
4. One fresh adversarial pass on three management-favourable Role 5 readings that run 1 did not test.
There is no full arithmetic sweep beyond the changed figures.

Inputs read:
- The revised review: 1,499 lines, with 68 "(Role 5 addendum, loop 1)" tags.
- A4's edit file (77 FIND/REPLACE pairs) and A4's loop-1 block. I used both only as a map to the edited passages and checked each one in the review.
- The concall fulltext and structured file, and the concall ledger (Q03 row).
- The results and deck fulltexts at the cited lines.
I read no A3 reasoning, no source transcript, no audio and nothing under inputs/.

Anchors are as in run 1. "rev L###" here is the revised review's numbering; the run-1 section above uses the pre-loop numbering.

## L0. DELIVERABLE-COMPLETENESS AUDIT (revised review)

| Brief part | Heading | Content | Status |
|---|---|---|---|
| 1. Summary narrative | rev L1253 | 17 lines (rev L1255-1271), inside 10-20. Part 1a (rev L1273-1277) and part 1b (rev L1279-1289) follow | PRESENT |
| 2. Sector intelligence | rev L1291 | rev L1293 | PRESENT |
| 3. Business-model intelligence | rev L1295 | rev L1297 | PRESENT |
| 4. Competition intelligence | rev L1299 | rev L1301 | PRESENT |
| 5. Forward map | rev L1303 | A make-or-break line and 14 catalysts, each with a Bull and a Bear fork (rev L1305-1319). The concall bullet now records its outcome (rev L1307) | PRESENT |

Gate: PASS.

## L1. CLOSURE OF RUN-1 FINDINGS

| ID | Fix found in the review | My check (recomputed or re-read) | Status |
|---|---|---|---|
| F-A | Q2, Q5 and Q31 are now NOT ADDRESSED, topic touched (rev L614, L617, L648). The definition is widened (rev L607). Aligned at 8.5C rev L656, 8.5D rev L662, RQ46 rev L684, monitorable 26 rev L718, flag 20 rev L754, 3E rev L911, net impact rev L1195, YAML rev L1379, L1442, L1490 and the analyst note rev L1495 | Recount of rev L613-648: PARTIALLY Q1, Q3, Q25, Q29 = 4. EVADED Q28, Q30 = 2. NOT ADDRESSED Q2, Q4, Q5, Q6-Q24, Q26, Q27, Q31 = 25. Total 31. The RQ46 list (Q2, Q4-Q24, Q26, Q27, Q31) = 1 + 21 + 2 + 1 = 25. Cells re-read at C-L58-59, C-L166, C-L171, C-L412, P-L142 and L1366 | CLOSED |
| C-A | The forward-map concall bullet (rev L1307) and 8.5C (rev L656) say the bear fork fired. The Q1 cell (rev L613) says the same | C-L365-366 gives an assertion with no figure. The bear text is "or no number given" (rev L613) | CLOSED |
| M-A | Fork outcomes on 9 rows. Q28 quotes C-L197 and C-L211 (rev L645). Exchange 3 is corrected (rev L998-999) | BEAR fired on Q1 (C-L365-366), Q2 (no series), Q5 ("No ceiling"; the FY28 half is untested), Q25 (C-L148) and Q30 (C-L379-380). Q3 is SPLIT ("EBITDA" at C-L158; no date at C-L415). Q28, Q29 and Q31 are NEITHER. 5 + 1 + 3 = 9; bear fired, counting the split, = 6 | CLOSED for the 9 rows. Q27 is a new inconsistency (L1-C1) |
| F-B | 7A rev L1115 is UNVERIFIABLE. Aligned at diag 4(b) rev L871, 5B rev L1035, flag 19 rev L753, brief 1b rev L1285, 8E rev L1182, net impact rev L1195, RQ37 rev L675 and YAML rev L1376, L1489 | Q1 FY27 Op EBITDA 6,582.82 - 3,144.09 - 1,239.73 - 968.86 = 1,230.14. Q1 FY26 2,310.43 - 1,173.62 = 1,136.81 (L135-143). Q1 TTM 4,822.46 - 1,136.81 + 1,230.14 = 4,915.79. 2.17 x 4,915.79 = 10,667.26; less 9,590.44 = 1,076.82, about 1,077. Dividend 498.78 (L479). No CONTRADICTED tag is left | CLOSED |
| F-C | 7A rev L1118 is UNVERIFIABLE | L458 files H1 FY27, H1 FY26 and FY26 only. 1,500.69 / 1,139.43 = +31.71% | CLOSED |
| F-D | 7A rev L1119 and 8D rev L1171 are UNVERIFIABLE, with the bases shown | TTM segment result 1,995.72 - 965.96 + 1,171.64 = 2,201.40 (L247); / 14,796.19 = 14.88%. H1 x 2 = 2,343.28, so 15.84%. Q2 x 4 = 680.94 x 4 = 2,723.76, so 18.41% | CLOSED |
| C-B | Two readings are named in flags 17 and 22 (rev L751, L756), brief 1a (rev L1277), Exchange 1 (rev L983), Exchange 3 (rev L1000), 5A (rev L1012), 8D (rev L1173), Step 2 (rev L899), diag 4(a) (rev L871), RQ32 (rev L670), YAML rev L1487 and L1492, and the note. The C-L232 focus line is now used | (21.15 - 10) / 21.15 = 52.7%. (14.78 - 10) / 14.78 = 32.3%. Data: (12.2 - 6) / 12.2 = 50.8%. Reported bar: 1.10 x 4,822.46 = 5,304.71. H2 need: 2,652.69 / 2,512.03 = +5.60%. The cc bar is 10% or more | CLOSED. Two residual wordings are logged as STYLE LS3 |
| C-C | Flag 18 rev L752; 5A type and cell rev L1011; 8E rev L1181; net impact rev L1195; YAML rev L1488 | C-L161-162 says "long-standing" and dates the contingent to 31-Mar-2026. In the results fulltext, "Canada" appears only at L1187 (entity list) and L1245 (Campaign Registry Inc). There is no CRA note | CLOSED |
| M-B | 5B rev L1030; flag 20 rev L754; 6D rev L1091; RQ38 rev L676; YAML rev L1490 | L572: "the Group awaits the National Court's decision" | CLOSED |
| F-F a | Brief 1a rev L1277 | C-L161-163, C-L169-171 | CLOSED |
| F-F b | 4B rev L969 | CQ02 Balaji (C-L218), CQ09 Vibhor (C-L351-356), CQ14 Avneesh (C-L414), CQ17 Harbik (C-L447-453): 4 analysts | CLOSED |
| F-F c | 6C rev L1075, L1081, L1083; flag 23 rev L757; YAML rev L1373, L1493 | Deferral at C-L213, L217, L408, L409, L416 = 5. Non-disclosure 1 (C-L379). "We believe" 3 (C-L76, L364, L426). Hope 5 (C-L230, L234, L286, L412, L415). "Too early" 2 (C-L305, L315). 5 + 1 + 3 + 5 + 2 = 16 | CLOSED |
| F-F d | Diag 2 rev L869; 0B rev L797 | P-L101-104: "Transformation Group ... Narottam Sharma" | CLOSED (STYLE LS4 on the 5A row) |
| F-F e | 6D rev L1091 | C-L151-153 sit in the CFO's script. C-L232 is a Q&A answer to Sanjay Jain's cc question (C-L227). "Constant currency" appears in neither the results fulltext nor the deck fulltext | CLOSED |

STYLE notes applied:
- S1: rev L4, L763.
- S2: rev L806 (P-L34 reads "at 4:00 pm IST").
- S3: rev L792, L797.
- S4: rev L1111.
- S5: rev L1116 (sums in L1A below).
- S6: rev L1150.
- S7: rev L1162.
- S9: rev L1069. R101, R106, R111 and R114 are FORWARD rows at structured L201, L206, L211 and L214.
- S12: rev L1015, L679 and YAML L1437.
- S13: rev L1277, L756.
Not applied, carried: S8, S10, S11, S14.

Result: all ten run-1 findings are CLOSED.

### L1A. ARITHMETIC AUDIT (changed figures only)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Answer status | 0 / 4 / 2 / 25 of 31 (rev L607, L754, L911, L1379) | 0 / 4 / 2 / 25 | rev L613-648 | PASS |
| Fork outcomes | 9 rows: BEAR 5, SPLIT 1, NEITHER 3; bear fired 6 (rev L607, L1380) | Same on those 9 rows | rev L613-648 | PASS (row set: L1-C1) |
| RQ46 / monitorable 26 count | 25 NOT ADDRESSED | 1 + 21 + 2 + 1 = 25; monitorable 26 adds EVADED Q28 and Q30 | rev L684, L718, L1442 | PASS |
| 7A tally | 6 / 3 / 0 / 12 of 21 | Recount of rev L1103-1123: CONFIRMED rows 1-4, 11, 12; PARTIALLY rows 5, 9, 14; UNVERIFIABLE the other 12 | rev L1125, L1376 | Arithmetic PASS. Row 9 tag: L1-F1 |
| Q1 TTM Op EBITDA | 4,915.79 | 4,822.46 - 1,136.81 + 1,230.14 = 4,915.79 | L135-143 | PASS |
| "Held steady" Q1 share | about 1,077 of 1,606.60 | 10,667.26 - 9,590.44 = 1,076.82 | L135-143; Role 4 5A | PASS |
| ROCE bases | 14.88% / 15.84% / 18.41% | 14.878% / 15.837% / 18.408% | L247; Role 4 6A | PASS |
| cc EBITDA currency share | 53% (Q2) / 32% (H1) | 52.7% / 32.3% | C-L232; L135-146 | PASS |
| Data currency share | about half | 50.8% | C-L148, C-L152 | PASS |
| FY27 reported bar | 5,304.71; H2 +5.60% | 5,304.71; 1.05600 | L135-146 | PASS |
| Joint FCF check | Q2 CFO about 1,024; Q2 capex about 812; Q1 capex about 689; Q1 FCF about (150) | 0.72 x 1,421.88 = 1,023.75; 1,023.75 - 212 = 811.75; 1,500.69 - 811.75 = 688.94; Q1 CFO 1,562.70 - 1,023.75 = 538.95; 538.95 - 688.94 = (149.99) | L441, L458; C-L164-165 | PASS (wording: LS1) |
| Defensive phrases | 16 (deferral 5) | 16 | C-L lines above | PASS |
| Specificity sensitivity | 15 / 55 = 0.27 | 0.273 | rev L1069 | PASS |
| Digital-path analysts | four | four | rev L969 | PASS |

There is no arithmetic mismatch.

### L1B. COVERAGE AUDIT (carried; scope check only)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| All run-1 categories | as run 1 | Not re-run (outside the loop scope). Loop 1 edited no enumeration and no ledger row | none | PASS (carried) |
| Citations after the edits | n.a. | Every C-L cite in the 77 FIND strings reappears in its REPLACE. C-L163 left flag 18, but it stays cited at rev L857, L894, L921 and L713 | none | PASS |

## L2. ROLE 4 UNCHANGED, AND NEW DEFECTS IN THE EDITED PASSAGES

Role 4 numbers:
- All 77 FIND strings sit in Role 5 text: the 8.5A/8.5B status column, the 8.5C and 8.5D addendum paragraphs, 8.5E, monitorable 26, flags 17-23, the Role 5 section, the brief addendum parts, the Role 5 YAML fields and the header and intro wording. None touches a Role 4 number or question text.
- Spot checks are unchanged: CCC -55.83 (rev L373), +83 bps (rev L257), 192.08 (rev L434), 8.57% vs 1.90% (rev L402) and 139.96x (rev L449).
- Op EBITDA recomputed from L135-143: Q2 FY27 1,421.88; Q1 FY27 1,230.14; Q2 FY26 1,173.62; H1 FY27 2,652.02; H1 FY26 2,310.43; FY26 4,822.46. These match every Role 5 use.
Result: no Role 4 number changed.

New defects in the edited passages:
- L1-C1 (CONTRADICTION). This is the fork rule at rev L607 against the Q27 row at rev L644. Details are in the findings table.
- L1-C2 (CONTRADICTION, minor). The loop-1 analyst note and the body give different counts of dated commitments.
- Edit E48 put "The CFO's claim reads YoY; the bound is QoQ" into 7A rev L1111, beside a PARTIALLY CONFIRMED tag. This is Read A below (L1-F1).

## L3. ADVERSARIAL READ (fresh pass; readings run 1 did not test)

**Read A. 7A rev L1111: "driven by significant reduction in losses across the digital portfolio" (C-L157) is tagged PARTIALLY CONFIRMED.**
- Bear counter, from the extract. The claim follows YoY figures (C-L154-156: EBITDA +21.2% YoY, H1 +14.8%, margin 21.3%). The review's own cell says it "reads YoY".
- No document gives the YoY Digital comparator. The deck shows Digital margins for FY25 (-9.7%, -886 Cr), Q1 FY27 (-6.9%) and Q2 FY27 (-3.6%, -107 Cr) only (P-L137-151). The press release gives Digital revenue of 3,016 vs 2,542, but no Q2 FY26 margin (L1384). Q2 asks for the Q2 FY26 loss and is NOT ADDRESSED (rev L614).
- The cell's only test is a QoQ ceiling ("at most 101.10 of the 195.09"). That ceiling is built on MGMT Digital figures, which the same table tags UNVERIFIABLE (rev L1109). A ceiling can cap the claim. It cannot confirm it.
- The filing does show the YoY split. The 248.26 Op EBITDA gain is the spread change +122.02 (revenue +588.14 less network +466.12) plus staff and other cost reduction +126.24 (90.82 + 35.42) (L135-143). The Digital share of either part is ND.
- Loop 1 applied the period rule both ways: to a bear claim at rev L1115 and to a bull claim at rev L1118. A test on another period, or a check of MGMT figures against MGMT figures, leaves the claim UNVERIFIABLE. Brief 1b (rev L1283) already says "the cause is still open".
- Survives. Graft: re-tag the row UNVERIFIABLE (YoY Digital comparator not disclosed; the QoQ ceiling on MGMT data is context). Retally to 6 / 2 / 0 / 13 at rev L1125 and YAML rev L1376. Finding L1-F1, FACTUAL.

**Read B. P2, "let's wait one more quarter, you will definitely see" (C-L234), is read as a cc Data step-up from about 6%.**
- Where the reading appears: P2 (rev L918); monitorable 19 (rev L711); Step 2 (rev L885); 8A (rev L1154); RQ42 (rev L680), bull "Q3 cc Data growth above 6%"; forward map (rev L1315), bull "growth steps up from about 6%"; YAML (rev L1462).
- Bear counter, from the extract. The promise answers this question: "So when should we see this constant currency growth of double digit in data business" (C-L227). The review's own CQ03 row says "when double digit" (rev L948). So do the A2 ledger Q03 row (ledger L101) and A1's context for R121, "constant currency growth in data" (structured L221).
- Under the review's bars, a Q3 cc print of 7% scores the bull fork and could score P2 DELIVERED. That print fails the frame in which the answer was given. P2's filed test metric (Data Services YoY vs +11.65%) is reported growth, so a currency tailwind can also meet it.
- Two readings: (A) double-digit cc Data growth from Q3 FY27, which is the question's frame; (B) any visible step-up from about 6%, which is the review's reading. The separating observation is management's own definition (RQ42) or the Q3 FY27 cc Data print against 10%.
- Survives. Graft: name both readings and the separator in each place listed above. State that, at the next Role 5, a cc print between about 6% and 10% scores DELIVERED only under reading B. Mark the filed reported metric as context, not the test. Finding L1-M1, MISSING.

**Read C. 7A rev L1114: net debt to EBITDA "2.17F" is CONFIRMED on TTM, and "A3 C07's 2.17 vs 2.11 gap is a basis difference, not an error".**
- Bear counter attempted. The definition is ND (RQ37). Under the F-D rule, a match on one chosen basis is not a confirmation.
- Test on all filed bases:
  - TTM Op EBITDA: 11,197.04 / 5,164.05 = 2.168.
  - H1 x 2: 2.111.
  - Q2 x 4: 11,197.04 / 5,687.52 = 1.969.
  - TTM including other income: 11,197.04 / (5,164.05 + 331.22) = 2.038. TTM other income from L136 is 301.73 + 0.14 + 29.35 = 331.22.
- Only the TTM operating basis gives 2.17, and it is the market-standard basis. The CFO's net debt of 11,197 also ties to the filed ex-lease 11,197.04 (C-L169). ROCE was different: no filed basis gave 15.9% (14.88%, 15.84%, 18.41%).
- Does not survive. The exact tie identifies the basis. 8B (rev L1162) labels the company's use of TTM as INFERENCE, and RQ37 asks for the definition. The tag stands.

### L3B. Other favourable readings tested (no graft, or STYLE only)

| Reading | Counter | Result |
|---|---|---|
| 4B "No evidence of pre-screening" (rev L974) | Four of six analysts opened with congratulations (C-L186, L246, L446, L460). The one challenger dropped twice (C-L240-242, L442). No analyst asked about net debt, contingents or subsidiaries | This is not evidence of screening, and the queue is not visible. STYLE LS5 |
| 6E UNCLASSIFIED, not EVASIVE (rev L1093) | 16 hedges, specificity 0.20, customer count withheld | The archetype keys on credibility, which is ND, and the review gives no credit. Stands |
| Step 1 diag 1: 21 of 40 quantified (rev L868) | #2 (binary), #5 (superlative), #9 and #27 (thresholds) and #15 and #16 (named, no size) all count as YES | On a number-or-date criterion the count is 15 of 40 (37.5%). The conclusion holds. STYLE LS6 |
| 8E "Undisclosed material risk: not established" (rev L1181) | The Q2 notes carry the 365.80 VAT contingent (L572-574) and the DoT contingent, but not the larger 1,658 CRA one | Quarterly notes are not the full contingent list, and the FY26 AR is not in this run. The cell states the absence. Stands |

Acquisition probe: the loop adds no acquisition text. The Commotion multiple is now stated as NOT FOUND (rev L1015). Probe satisfied.

## L4. FINDINGS (loop 1; tagged)

| ID | Type | Gap | Fix | Loop |
|---|---|---|---|---|
| L1-F1 | FACTUAL | 7A rev L1111 tags the C-L157 Digital-driver claim PARTIALLY CONFIRMED. The test is a QoQ ceiling on MGMT data. The claim reads YoY, and no Q2 FY26 Digital loss is disclosed (P-L137-151; L1384; rev L614). Rev L1109, L1115 and L1118 set the opposite standard | Re-tag UNVERIFIABLE (YoY comparator ND; the QoQ ceiling is context). Retally rev L1125 and YAML rev L1376 to 6 / 2 / 0 / 13 | A4 |
| L1-M1 | MISSING | P2 (C-L234) answers a double-digit cc Data question (C-L227; rev L948; ledger L101). P2 rev L918, monitorable 19 rev L711, Step 2 rev L885, 8A rev L1154, RQ42 rev L680, the forward map rev L1315 and YAML rev L1462 test only a step-up above about 6%. Reading A and its separator are missing | Name reading A (double-digit cc from Q3 FY27) and reading B (any step-up from about 6%). Name the separator (RQ42 definition, or the Q3 cc print against 10%). Set the next-Role 5 scoring note. Mark the reported filed metric as context | A4 |
| L1-C1 | CONTRADICTION | Rev L607 says each touched row records a fork outcome, and rows with no concall line have none. Q27 (rev L644) cites C-L87 and C-L397-398, where the call raised Commotion and said it runs with SaaS "as one PNO", which is why no split exists. Q27 has no "topic touched" mark and no fork outcome. Q31 got both for a focus-only line (C-L412). Q4 and Q6 also cite concall lines, but only to show that their topic did not come up | Mark Q27 "NOT ADDRESSED, topic touched", fork NEITHER (no item given). Recount: touched 10; BEAR 5, SPLIT 1, NEITHER 4 (Q27, Q28, Q29, Q31); bear fired stays 6. Reword the rule to "rows the call did not touch have no fork outcome". Align rev L607, L911 ("6 of the 10 rows"), L974 ("22 Role 4 questions" becomes 21 untouched rows of the 25 NOT ADDRESSED), YAML rev L1380 and the loop log rev L1236 | A4 |
| L1-C2 | CONTRADICTION (minor) | Rev L936 and L1191 say P1, P2, P3 and P5 are dated. The YAML analyst note (rev L1495), rewritten in loop 1, says "P1, P2 and P3 dated". P5's own row (rev L921) and monitorable 21 (rev L713) say "Undated ... Q3 FY27 results at the latest [INFERENCE]". The note's wording is inherited from the pre-loop note | Use one wording at rev L936, L1191 and L1495: "P1, P2 and P3 dated; P5 by INFERENCE (Q3 FY27 results at the latest)" | A4 |

Effect on the verdicts:
- None of the four changes the protocol verdict (PROCEED WITH FLAGS), the cash class (INDETERMINATE-WITH-DIRECTION), the branch (8A-W) or the concall net impact (WEAKENED).
- L1-F1 adds one row to the UNVERIFIABLE list. The WEAKENED reason "the cause of the profit step is still unnamed" (rev L1195) already rests on that list.
- L1-M1 raises the bar against which P2 may be scored at the next Role 5.

## L5. VERDICT (loop 1)

**INCOMPLETE. Loop back to A4.**
- All ten run-1 findings are closed, and every changed figure recomputes.
- Gate 0 passes. No Role 4 number changed. Coverage is carried from run 1 as PASS, and the loop removed no ledger citation.
- Four new A4-side findings: one FACTUAL (L1-F1), one MISSING (L1-M1) and two CONTRADICTION (L1-C1, L1-C2).
- A1, A2 and A3 do not re-run.

## L6. STYLE NOTES (loop 1; logged, no re-run)

- LS1. 7A joint check (rev L1116). The parenthesis "(Q1 CFO 1,562.70 - 1,024, L441)" shows the CFO step, not the FCF step. Write "Q1 CFO 538.95 (1,562.70 - 1,023.75) less Q1 capex 688.94 = (149.99)".
- LS2. Brief 2 (rev L1293): "Management credits a strengthening dollar for about half of data growth (MGMT, C-L151-152)". Management named the dollar. "About half" is DERIVED from about 6% vs 12.2%. Tag it.
- LS3. Residual C-B wording:
  - Monitorable 18 (rev L710) and YAML rev L1461 give the reported bar only. Add "cc basis asked (RQ33)", as P1 does (rev L917).
  - The Step 2 row (rev L881) says "low bar (see diagnostics)". Write "low bar on reported basis; real test on cc (RQ33)".
- LS4. 5A (rev L1018) lists Narotan Sharma under new disclosures as "New senior management". The deck names him the same day (P-L104). Add "named in the deck; the call adds the join timing (C-L45)".
- LS5. 4B (rev L974): "No evidence of pre-screening". Write "pre-screening cannot be tested from the transcript".
- LS6. Step 1 diag 1 (rev L868). Add a criterion sensitivity note: 15 of 40 (37.5%) on a number-or-date basis. The conclusion holds.
- LS7. Run-1 S8 (CQ17 grade B kept; A4's judgment accepted), S10, S11 and S14 are carried, not applied.

```yaml
stage: A5-adversary
company: "TATACOMM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 1
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "7A rev L1111: Digital loss reduction 'drove' the profit improvement (C-L157) = PARTIALLY CONFIRMED", counter: "The claim reads YoY (C-L154-156), and no Q2 FY26 Digital loss is disclosed: the deck gives FY25, Q1 FY27 and Q2 FY27 Digital margins only (P-L137-151); the press release gives no Q2 FY26 margin (L1384); Q2 is NOT ADDRESSED (rev L614). The cell's only test is a QoQ upper bound on MGMT Digital figures, which rev L1109 tags UNVERIFIABLE. Loop 1 set this period rule at rev L1115 and L1118. Re-tag UNVERIFIABLE", source_line: "C-L154-157; P-L137-151; L135-143; L1384; rev L1109, L1111, L1115, L1118, L1283", type: "FACTUAL"}
  - {claim: "P2 'let's wait one more quarter, you will definitely see' (C-L234) tested as a cc Data step-up above ~6% (rev L918, L711, L885, L1154, L680, L1315, L1462)", counter: "The promise answers 'when should we see this constant currency growth of double digit in data business' (C-L227). The review's CQ03 row says 'when double digit' (rev L948), and so do ledger Q03 (ledger L101) and R121's context (structured L221). A 7% Q3 cc print would score the bull fork. The filed P2 metric is reported growth, which a currency tailwind can meet. Name both readings and the separator", source_line: "C-L227, C-L234; rev L680, L711, L885, L918, L948, L1154, L1315, L1462; ledger L101; structured L221", type: "MISSING"}
findings_by_type:
  factual:
    - "L1-F1 7A rev L1111 Digital-driver claim (C-L157) tagged PARTIALLY CONFIRMED on a QoQ ceiling built on MGMT data. The claim reads YoY, and no YoY Digital comparator is disclosed (P-L137-151; L1384; rev L614). Re-tag UNVERIFIABLE. Retally 6/2/0/13 at rev L1125 and YAML rev L1376"
  missing:
    - "L1-M1 P2 (C-L234) answers a double-digit cc Data question (C-L227; rev L948; ledger L101), but P2 rev L918, monitorable 19 rev L711, Step 2 rev L885, 8A rev L1154, RQ42 rev L680, forward map rev L1315 and YAML rev L1462 test only a step-up above ~6%. The second reading (double-digit cc from Q3 FY27) and its separator are missing"
  contradiction:
    - "L1-C1 The rev L607 rule says every touched row records a fork outcome. Q27 (rev L644) cites C-L87 and C-L397-398, where the call raised Commotion and said it runs with SaaS 'as one PNO', yet it has no 'topic touched' mark and no fork outcome. Q31 got both for a focus-only line (C-L412). Recount: touched 10; BEAR 5, SPLIT 1, NEITHER 4; bear fired stays 6"
    - "L1-C2 minor: rev L936 and L1191 say P1, P2, P3 and P5 are dated; the loop-1 YAML analyst note (rev L1495) says P1, P2 and P3; P5's own row says 'Undated ... [INFERENCE]' (rev L921, L713)"
  style:
    - "LS1 7A rev L1116 joint check: the '(Q1 CFO 1,562.70 - 1,024)' parenthesis shows the CFO step, not the FCF step; write Q1 CFO 538.95 less Q1 capex 688.94 = (149.99)"
    - "LS2 brief 2 rev L1293: 'about half' of Data growth is DERIVED (~6% vs 12.2%), not management's words; tag it"
    - "LS3 C-B residual wording: monitorable 18 rev L710 and YAML rev L1461 give the reported bar only (add 'cc basis asked, RQ33' as P1 rev L917 does); Step 2 rev L881 'low bar' becomes 'low bar on reported basis; real test on cc (RQ33)'"
    - "LS4 5A rev L1018 lists Narotan Sharma as a new disclosure; the deck names him the same day (P-L104); the join timing (C-L45) is what the call adds"
    - "LS5 4B rev L974 'No evidence of pre-screening': the transcript cannot test it"
    - "LS6 Step 1 diag 1 rev L868: a number-or-date criterion gives 15 of 40 (37.5%), not 21; the conclusion holds"
    - "LS7 run-1 S8 (CQ17 B kept, A4 judgment accepted), S10, S11, S14 carried, not applied"
loop_back_to: "A4"
gap: "Run-1 findings F-A, F-B, F-C, F-D, F-F(a-e), M-A, M-B, C-A, C-B, C-C are all CLOSED. Four new A4-side items. (1) L1-F1 FACTUAL: rev L1111 re-tag the C-L157 Digital-driver claim UNVERIFIABLE. The claim reads YoY; no Q2 FY26 Digital loss is in the deck (P-L137-151) or the press release (L1384); the QoQ ceiling uses MGMT data that rev L1109 tags UNVERIFIABLE. Retally rev L1125 and YAML rev L1376 to 6/2/0/13. (2) L1-M1 MISSING: in P2 rev L918, monitorable 19 rev L711, Step 2 rev L885, 8A rev L1154, RQ42 rev L680, forward map rev L1315 and YAML rev L1462, name two readings of C-L234. Reading A: double-digit cc Data growth from Q3 FY27, the frame of the question at C-L227 (rev L948). Reading B: any step-up from ~6%. Separator: management's definition (RQ42), or the Q3 cc Data print against 10%. State that a 6-10% print scores DELIVERED only under reading B. Mark the filed reported metric as context, not the test. (3) L1-C1 CONTRADICTION: mark Q27 rev L644 'NOT ADDRESSED, topic touched' with fork NEITHER (C-L87, C-L397-398). Recount touched 10 (BEAR 5, SPLIT 1, NEITHER 4 = Q27, Q28, Q29, Q31) at rev L607 and YAML rev L1380. Write '6 of the 10 rows' at rev L911. Rev L974 '22 Role 4 questions' becomes 21 untouched of the 25 NOT ADDRESSED. Update log rev L1236. Reword the rev L607 rule to 'rows the call did not touch have no fork outcome'. (4) L1-C2 CONTRADICTION: at rev L936, L1191 and the YAML note rev L1495, use one wording: 'P1, P2, P3 dated; P5 by INFERENCE'. No change to verdict, cash class, branch or WEAKENED."
style_notes:
  - "LS1 split the joint FCF parenthesis into CFO and FCF steps (rev L1116)"
  - "LS2 tag brief 2 'about half' DERIVED (rev L1293)"
  - "LS3 add the cc reading to monitorable 18 / YAML P1 and Step 2 'low bar' (rev L710, L1461, L881)"
  - "LS4 5A Narotan Sharma: deck names him; the join timing is new (rev L1018)"
  - "LS5 'pre-screening cannot be tested from the transcript' (rev L974)"
  - "LS6 diag 1 criterion sensitivity 15 of 40 (rev L868)"
  - "LS7 run-1 S8, S10, S11, S14 carried"
analyst_note: "Loop 1 closed all ten run-1 findings. My recounts tie: answer status 0/4/2/25, forks 5/1/3 with six bear hits, 7A 6/3/0/12 as tagged, and 16 hedges. Each changed figure recomputes from the filing and the call. Every edit sits in a Role 5 cell. No Role 4 number moved, and no ledger cite was lost. Two fresh bear counters survive. First, 7A still calls the Digital-loss driver partly confirmed. The test is a QoQ ceiling on MGMT figures. The claim reads YoY, and no YoY Digital comparator is disclosed. Loop 1 applied this period rule to 'held steady' and to capex, so this row must follow. Second, P2 is scored as any step-up above 6%. The promise answered a question about double-digit cc Data growth, so both readings need naming before next quarter's score. The 2.17x TTM tie stands, because no other filed basis gives 2.17. Two minor contradictions remain: Q27 lacks the new topic-touched mark, and the body and note count dated commitments differently. Verdict, cash class, branch and WEAKENED do not change."
```

---
---

# LOOP 2 RE-AUDIT (Role 5 addendum, correction loop 2; final loop; fresh A5 instance, 2026-10-18)

This section supersedes the loop-1 verdict and YAML block above. The run-1 and loop-1 records stay as written. The block at the end of this section is the current one; the same block is in work/blocks/a5-role5.yaml.

Scope (task brief, strictly):
1. Deliverable gate on the loop-2 review.
2. Closure of loop-1 findings L1-F1, L1-M1, L1-C1 and L1-C2, with every changed figure recomputed.
3. The loop-2 edits add no new FACTUAL, MISSING or CONTRADICTION finding and touch no Role 4 number.
There is no new adversarial pass beyond the edited passages and no full arithmetic sweep. No further loop exists. Anything still open is listed as an open item, to be flagged, not looped.

Inputs read:
- The loop-2 review: 1,512 lines. 29 of the 30 edits carry a loop-2 marker; E30 is the loop counter itself (rev L1511).
- A4's loop-2 edit file (30 FIND/REPLACE pairs) and A4's loop-2 block. I used both only as a map and checked each edit in the review.
- The concall fulltext at C-L40-99, C-L145-239 and C-L385-419.
- The deck fulltext at P-L98-152. The results fulltext at L132-145, L436-461 and L1360-1389.
- The concall ledger, Q03 row (ledger L101).
I read no A3 reasoning, no source transcript, no audio and nothing under inputs/.

"rev L###" here is the loop-2 review's numbering. The sections above use earlier numbering.

## M0. DELIVERABLE-COMPLETENESS AUDIT (loop-2 review)

| Brief part | Heading | Content | Status |
|---|---|---|---|
| 1. Summary narrative | rev L1266 | 17 lines (rev L1268-1284), inside 10-20. Part 1a (rev L1286-1290) and part 1b (rev L1292-1302) follow | PRESENT |
| 2. Sector intelligence | rev L1304 | rev L1306 | PRESENT |
| 3. Business-model intelligence | rev L1308 | rev L1310 | PRESENT |
| 4. Competition intelligence | rev L1312 | rev L1314 | PRESENT |
| 5. Forward map | rev L1316 | A make-or-break line (rev L1318) and 14 catalysts, each with a Bull and a Bear fork (rev L1319-1332). The cc Data bullet now carries both P2 readings (rev L1328) | PRESENT |

Gate: PASS.

## M1. CLOSURE OF LOOP-1 FINDINGS

| ID | Fix found in the review | My check (recomputed or re-read) | Status |
|---|---|---|---|
| L1-F1 | 7A rev L1111 re-tagged UNVERIFIABLE (E01). Tally rev L1125 (E02). YAML filing_crosscheck rev L1389 (E03). Analyst note rev L1508 (E21). Loop-2 log rev L1253 | The claim follows YoY figures: "up 21.2% on a YOY basis" (C-L154), H1 "on a YOY basis" (C-L155), margin 21.3% (C-L156). It reads "The improvement in profitability is driven by significant reduction in losses across the digital portfolio" (C-L157). The deck gives Digital margins for FY25 (-9.7%, -INR 886 Cr), Q1 FY27 (-6.9%) and Q2 FY27 (-3.6%, -INR 107 Cr) only (P-L137-151). The press release table gives Digital revenue 3,016 vs 2,542 (L1384). Its highlight gives Q2 FY27 -3.6% and "halved from last quarter" (L1366). No input holds a Q2 FY26 Digital loss or margin. On a QoQ reading, the only test is MGMT against MGMT (rev L1109-1110, both UNVERIFIABLE). The tag is UNVERIFIABLE under either reading. Recount of rev L1103-1123: CONFIRMED at rev L1103, L1104, L1105, L1106, L1113, L1114 = 6. PARTIALLY at rev L1107, L1116 = 2. CONTRADICTED 0. UNVERIFIABLE at rev L1108-1112, L1115, L1117-1123 = 13. Total 21. No "6 / 3 / 0 / 12" wording is left | CLOSED. One dependent cell is not aligned: brief 1b rev L1296 (L2-C1) |
| L1-M1 | Two readings, the separator and the scoring note in P2 rev L918 (E04), monitorable 19 rev L711 (E05), Step 2 rev L885 (E06), 8A rev L1154 (E07), RQ42 rev L680 (E08), forward map rev L1328 (E09), YAML monitorable rev L1475 (E10) and YAML RQ42 rev L1451 (E11) | C-L227: "So when should we see this constant currency growth of double digit in data business now that order book has been quite strong." C-L234: "let's wait one more quarter, you will definitely see." Ledger L101: "when constant currency data growth turns double digit". Reading A, reading B (from "about 6%", C-L152) and the separator (RQ42, or the Q3 cc print against 10%) appear in all eight places. The note "a print between about 6% and 10% scores DELIVERED only under B" is in P2, monitorable 19, 8A, RQ42, the forward map and the YAML monitorable. "The filed reported metric is context, not the test" is in P2, monitorable 19 and the YAML monitorable. Exchange 1 (rev L983) points to P2, so it inherits both readings. No "above 6%" or "steps up from about 6%" wording is left | CLOSED |
| L1-C1 | Q27 rev L644 is "NOT ADDRESSED, topic touched", fork NEITHER (E12). The rule is reworded at rev L607 (E13). Recount at rev L607 (E14). 3E rev L911 (E15). 4B rev L974 (E16). YAML rev L1393 (E17). Loop-1 log M-A rev L1236 (E18) | C-L87: "Through our commotion acquisition, we have the capability". C-L397-398: "We run commotion and SaaS together as one entity under one leader as one PNO." The call gives no restatement answer and no perimeter split. It says neither fork text, so NEITHER fits. Touched rows: PARTIALLY Q1, Q3, Q25, Q29 (4), EVADED Q28, Q30 (2), NOT ADDRESSED topic touched Q2, Q5, Q27, Q31 (4) = 10. Forks: BEAR Q1, Q2, Q5, Q25, Q30 (5), SPLIT Q3 (1), NEITHER Q27, Q28, Q29, Q31 (4) = 10. Bear fired 5 + 1 = 6. Untouched NOT ADDRESSED: 25 - 4 = 21. Answer status unchanged: 0 + 4 + 2 + 25 = 31. RQ46 (rev L684) still lists 25, including Q27. Monitorable 26 (rev L718) lists 27 = 25 + 2 EVADED. No "9 touched" wording is left outside the loop-1 log history | CLOSED (rule wording: STYLE L2-S2) |
| L1-C2 | 3B scoring rule rev L936 (E19). Concall verdict rev L1191 (E20). Analyst note rev L1508 (E21) | All three now read "P1, P2 and P3 dated; P5 by INFERENCE (Q3 FY27 results at the latest)". The P5 row (rev L921), monitorable 21 (rev L713) and the YAML P5 item (rev L1477) say "Undated ... Q3 FY27 results at the latest [INFERENCE]". C-L163 "in due course" gives no date. No "P1, P2, P3 and P5" wording is left | CLOSED |

STYLE notes applied:
- LS1: rev L1116 (E22).
- LS2: rev L1306 (E23).
- LS3: rev L710, L1474 and L881 (E24-E26).
- LS4: rev L1018 (E27).
- LS5: rev L974 (E16).
- LS6: rev L868 (E28).
Carried, not applied: LS7 (rev L1258).

Result: all four loop-1 findings are CLOSED.

### M1A. ARITHMETIC AUDIT (changed figures only)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| 7A tally | 6 / 2 / 0 / 13 of 21 (rev L1125, L1389, L1508) | 6 / 2 / 0 / 13 | rev L1103-1123 | PASS |
| YoY Op EBITDA gain and split (the re-tagged cell's context) | 248.26; 126.24 is cost reduction | Q2 FY27 6,687.89 - 3,181.47 - 1,178.75 - 905.79 = 1,421.88. Q2 FY26 6,099.75 - 2,715.35 - 1,269.57 - 941.21 = 1,173.62. Gain 248.26. Employee 90.82 + other 35.42 = 126.24. Spread 588.14 - 466.12 = 122.02; 122.02 + 126.24 = 248.26 | L135-143 | PASS (unchanged figure, re-checked) |
| Digital revenue YoY (context) | 3,016 vs 2,542 | +18.65% | L1384 | PASS |
| Fork outcomes | 10 touched; BEAR 5, SPLIT 1, NEITHER 4; bear fired 6 (rev L607, L911, L1393, L1508) | 10; 5 / 1 / 4; 6 | rev L613-648 | PASS |
| Untouched NOT ADDRESSED | 21 of 25 (rev L974) | 25 - 4 (Q2, Q5, Q27, Q31) = 21 | rev L614, L617, L644, L648 | PASS |
| P2 bars | about 6% cc; 10% separator; reported +11.65% as context | "about 6%" (C-L152); "double digit" (C-L227); 5,810.99 / 5,204.47 = +11.65% | C-L152, C-L227; L235 via rev L1107 | PASS |
| LS1 joint FCF | Q1 CFO 538.95; Q1 capex 688.94; Q1 FCF (149.99) | 0.72 x 1,421.88 = 1,023.75. 1,562.70 - 1,023.75 = 538.95. 1,023.75 - 212 = 811.75. 1,500.69 - 811.75 = 688.94. 538.95 - 688.94 = -149.99. Check: -149.99 + 212 = 62.01 = 1,562.70 - 1,500.69 | L441 (H1 CFO), L458 (H1 capex); C-L164-165 | PASS. A4's relabel of 1,562.70 as H1 CFO is right: L441 sits in the half-year cash flow statement (L450) |
| LS2 currency share | about half, DERIVED | (12.2 - 6) / 12.2 = 50.8% | C-L148, C-L152 | PASS |
| LS3 reported bar | 5,304.71; H2 2,652.69; +5.60% | FY26 24,802.72 - 11,361.83 - 4,938.93 - 3,679.50 = 4,822.46; x 1.10 = 5,304.71. H1 FY27 13,270.71 - 6,325.56 - 2,418.48 - 1,874.65 = 2,652.02; need 2,652.69. H2 FY26 4,822.46 - 2,310.43 = 2,512.03; 2,652.69 / 2,512.03 = 1.0560 | L135-143 | PASS |
| LS6 strict count | 15 of 40 (37.5%) | YES rows at rev L826-864 = 21. Less #2 (binary), #5 (superlative), #9 and #27 (thresholds), #15 and #16 (named, no size) = 15. 15 / 40 = 37.5% | rev L826-868 | PASS |

There is no arithmetic mismatch.

### M1B. COVERAGE AUDIT (carried; scope check only)

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| All run-1 categories | as run 1 | Not re-run (outside the loop scope). Loop 2 edited no enumeration and no ledger row | none | PASS (carried) |
| Citations after the edits | n.a. | Every C-L, P-L and L cite in the 30 FIND strings reappears in its REPLACE. E01 keeps C-L455. E04-E10 keep C-L152 and C-L234. E12 keeps C-L87 and C-L397-398. E22 keeps L441. Loop 2 adds C-L45, C-L154-156, C-L227, P-L104, P-L137-151 and L1384 | none | PASS |
| Ledger frame for reading A | n.a. | Ledger Q03 (ledger L101): "when constant currency data growth turns double digit" | none | PASS |

## M2. ROLE 4 UNCHANGED, AND NEW DEFECTS IN THE EDITED PASSAGES

Role 4 numbers:
- All 30 FIND strings sit in Role 5 text or Role 5 YAML fields. They cover the 7A table and tally, Step 1 diag 1, the Step 2 table, the 3B rule, 3E, 4B, 5A, 8A, the concall verdict, the Q27 answer-status cell, the 8.5 intro, RQ42, monitorables 18 and 19, the brief 2 addendum sentence, the forward-map addendum bullet, the loop logs and the Role 5 YAML fields.
- E12 replaces only the Role 5 answer-status cell of Q27. The Q27 question, bull and bear text are unchanged (rev L644).
- E21 rewrites the YAML analyst note. It has held Role 5 content only since run 1 (S1). It keeps the DoT reconciliation, 7,844.57 - 276.68 - 54.18 = 7,513.71.
- Op EBITDA recomputed from L135-143: Q2 FY27 1,421.88; Q2 FY26 1,173.62; H1 FY27 2,652.02; H1 FY26 2,310.43; FY26 4,822.46. These match every Role 5 use.
- Spot checks are still present: CCC -55.83, +83 bps, 192.08, 8.57% vs 1.90% and 139.96x.
Result: no Role 4 number changed.

New defects in the edited passages:
- L2-C1 (CONTRADICTION, minor). E01 re-tags the 7A Digital-driver row. The dependent brief 1b row (rev L1296) was not aligned. Details are in M4.
- Three wording points in the edited text are STYLE (L2-S1 to L2-S3).

## M3. READ OF THE EDITED PASSAGES (no new adversarial pass)

I tested each edited reading from both sides on the same text. No new graft survives apart from the 1b alignment.

| Edited reading | Counter tested | Result |
|---|---|---|
| 7A rev L1111: the Digital-driver claim is UNVERIFIABLE | Bull side: is the tag too harsh? The CEO and the press release give a QoQ "less than half" and "halved" (C-L58-59, L1366). On a QoQ reading the test is MGMT on MGMT, and rev L1109-1110 tag those figures UNVERIFIABLE. On a YoY reading no comparator exists | The tag stands under both readings |
| P2 two readings (rev L918) | Is reading A too harsh? The answer turns to cc EBITDA "around 10%" and to the order book that "should convert to revenue" (C-L232-234). "You will definitely see" has no stated object. Reading B fits the text as well as reading A. P15 (rev L931) logs the conversion itself | Both readings are named, with one separator. The forks are symmetric: bull 10% or more, bear near 6%. Stands |
| Q27 fork NEITHER (rev L644) | Bear side: "one PNO" (C-L397-398) means Commotion cannot be split out, which supports the perimeter worry | The bear text is "Not restated; growth is perimeter". The call said neither half. NEITHER stands |
| 4B rev L974 "Pre-screening cannot be tested from the transcript" | n.a. | Matches LS5. Stands |

Acquisition probe: E12 names Commotion again but adds no purchase economics. The multiple stays 136.96 (L463; the link to Commotion is an INFERENCE by date) divided by Commotion PAT NOT FOUND (rev L1015), so it cannot be computed. Probe satisfied, carried.

## M4. FINDINGS (loop 2; tagged)

| ID | Type | Gap | Fix | Owner | Disposition |
|---|---|---|---|---|---|
| L2-C1 | CONTRADICTION (minor) | Brief 1b rev L1296 still reads the C-L157 claim as "Filing wins; the cause is still open". It also puts "Digital explains about half of the subsidiary jump at most" under "Filing shows (FILED)". After E01, 7A rev L1111 says three things. The claim is UNVERIFIABLE, because no YoY Digital comparator exists. The QoQ ceiling "rests on MGMT Digital figures" and is "context, not a test". "Digital loss reduction can itself run through cost lines", so the filed cost split (126.24 of 248.26, L135-143) does not refute the claim. In the same 1b table, loop 1 aligned the "held steady" row to "Cannot be checked" (rev L1298) when 7A re-tagged it. "Filing wins" is used where filed and MGMT numbers diverge (rev L1299) | At rev L1296, set the Read column to "Cannot be checked; no YoY Digital comparator is disclosed; the cause is still open". Keep "Half the yearly EBITDA gain is lower staff and other costs" in the FILED column. Tag the Digital ceiling "QoQ ceiling on MGMT Digital figures, context only", or move it out of that column. One cell. No number, tally or verdict moves | A4 | OPEN ITEM. Final loop: flag, not loop |

Effect on the verdicts: none. The protocol verdict (PROCEED WITH FLAGS), the cash class (INDETERMINATE-WITH-DIRECTION), the branch (8A-W) and WEAKENED do not change. WEAKENED reason (2), "The cause of the profit step is still unnamed" (rev L1195), already matches the UNVERIFIABLE tag.

## M5. VERDICT (loop 2; final)

**INCOMPLETE, on one open item. No loop remains, so the item goes forward as a flag.**
- All four loop-1 findings are CLOSED. Every changed figure recomputes from the filing and the call.
- Gate 0 passes. No Role 4 number changed. Coverage is carried as PASS, and loop 2 removed no ledger citation.
- One new minor CONTRADICTION (L2-C1). Brief 1b rev L1296 was not aligned with the 7A re-tag. The fix is one cell, and A4 owns it.
- A1, A2 and A3 do not re-run.
- Only COMPLETE proceeds to save. The orchestrator and the operator decide how to treat the open item. Its fix changes one reconciliation word and one tier label, and moves no number, tally or verdict.

## M6. STYLE NOTES (loop 2; logged, no re-run)

- L2-S1. 7A rev L1111 (E01):
  - "the press release gives Digital revenue but no margin (L1384)". The press release highlight gives the Q2 FY27 margin, -3.6%, and "halved from last quarter" (L1366). Write "the press release gives no Q2 FY26 Digital margin (L1384; L1366 gives Q2 FY27 only)".
  - "and Q2 is NOT ADDRESSED" can be read as the quarter. Write "and 8.5A Q2 is NOT ADDRESSED".
  - The tag and the conclusion do not move.
- L2-S2. The 8.5 rule at rev L607 (E13) says "Q4 and Q6 cite concall lines only to show that their topic did not come up". That fits Q4. Q6's cell uses C-L408-409 as a forward signal ("signals more"). Write "Q4 and Q6 cite concall lines as context; neither topic came up". No count changes: C-L408-409 names no staff-cost programme, total, remainder or end date.
- L2-S3. P2 rev L918, monitorable 19 rev L711 and YAML rev L1475. The test is a MGMT cc print, and the filing cannot verify it (7A rev L1108). Add "If Q3 gives no cc Data figure, P2 scores UNCLEAR (excluded)".
- L2-S4. Brief 1a rev L1290: "Currency gains made up about half of data revenue growth" has no DERIVED tag. Brief 2 now has one (LS2). This passage is outside the loop-2 edits, so it is logged only.
- L2-S5. Carried, not applied: LS7 (run-1 S8, S10, S11 and S14).

```yaml
stage: A5-adversary
company: "TATACOMM"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2
final_loop: true
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
closed_this_loop: ["L1-F1", "L1-M1", "L1-C1", "L1-C2"]
role4_numbers_changed: false
findings_by_type:
  factual: []
  missing: []
  contradiction:
    - "L2-C1 minor: brief 1b rev L1296 reads the C-L157 Digital-driver claim as 'Filing wins; the cause is still open' and lists 'Digital explains about half of the subsidiary jump at most' under 'Filing shows (FILED)'. After loop-2 E01, 7A rev L1111 tags the claim UNVERIFIABLE (no YoY Digital comparator: P-L137-151, L1366, L1384) and calls the QoQ ceiling MGMT-based context, not a test; Digital loss reduction can run through the filed cost lines (126.24 of 248.26, L135-143). Loop 1 aligned the matching held-steady row (rev L1298); this row was missed"
  style:
    - "L2-S1 7A rev L1111: 'press release gives Digital revenue but no margin (L1384)' should read 'no Q2 FY26 Digital margin (L1384; L1366 gives Q2 FY27 -3.6% only)'; 'Q2 is NOT ADDRESSED' should read '8.5A Q2 is NOT ADDRESSED'; tag unchanged"
    - "L2-S2 8.5 rule rev L607: Q6 cites C-L408-409 as a forward signal, not only to show its topic did not come up; write 'Q4 and Q6 cite concall lines as context; neither topic came up'; no count change"
    - "L2-S3 P2 rev L918, monitorable 19 rev L711, YAML rev L1475: add 'if Q3 gives no cc Data figure, P2 scores UNCLEAR (excluded)'; the cc print is MGMT (7A rev L1108)"
    - "L2-S4 brief 1a rev L1290 'about half' lacks the DERIVED tag that brief 2 now carries (LS2); outside the loop-2 edits, logged only"
    - "L2-S5 LS7 carried (run-1 S8, S10, S11, S14)"
loop_back_to: "A4"   # owner of the open item; final loop, so it is flagged, not looped
gap: "Final loop (loop 2). L1-F1, L1-M1, L1-C1 and L1-C2 are CLOSED; every changed figure recomputes; no Role 4 number moved. One open item, to be flagged, not looped: L2-C1 CONTRADICTION (minor), owner A4. Brief 1b rev L1296 reads the C-L157 Digital-driver claim as 'Filing wins' and lists the QoQ Digital ceiling under 'Filing shows (FILED)'. 7A rev L1111 (loop-2 E01) now tags the claim UNVERIFIABLE (no YoY Digital comparator: P-L137-151, L1366, L1384) and calls the ceiling MGMT-based context. Fix: rev L1296 Read column 'Cannot be checked; no YoY Digital comparator is disclosed; the cause is still open'; tag the ceiling 'QoQ ceiling on MGMT Digital figures, context only' or move it out of the FILED column. No number, tally, verdict, cash class, branch or WEAKENED moves."
open_items:
  - {id: "L2-C1", type: "CONTRADICTION", severity: "minor", owner: "A4", location: "rev L1296 (brief 1b, Digital-driver row)", fix: "Read column: 'Cannot be checked; no YoY Digital comparator is disclosed; the cause is still open'. Keep the filed cost split (126.24 of 248.26, L135-143) in the FILED column; tag the Digital ceiling 'QoQ ceiling on MGMT Digital figures, context only' or move it out of that column", moves: "no number, tally, verdict, cash class, branch or WEAKENED", disposition: "flag, not loop (final loop)"}
style_notes:
  - "L2-S1 7A rev L1111: press release gives no Q2 FY26 Digital margin (L1366 gives Q2 FY27 only); write '8.5A Q2'"
  - "L2-S2 rev L607 rule: 'Q4 and Q6 cite concall lines as context; neither topic came up'"
  - "L2-S3 P2: no cc figure at Q3 means P2 scores UNCLEAR"
  - "L2-S4 brief 1a rev L1290: tag 'about half' DERIVED, as brief 2 does"
  - "L2-S5 LS7 carried (run-1 S8, S10, S11, S14)"
analyst_note: "Loop 2 closed all four loop-1 findings. The 7A Digital-driver claim is now UNVERIFIABLE. It reads YoY, and no input holds a Q2 FY26 Digital loss (deck P-L137-151; press release L1366, L1384). On a QoQ reading it is MGMT against MGMT, so the tag holds either way. The tally recounts to 6/2/0/13. P2 now names both readings in eight places, with RQ42 or the Q3 cc print against 10% as the separator. Q27 is touched with fork NEITHER. Touched rows are 10, bear fired stays 6, and the call never touched 21 of the 25 NOT ADDRESSED rows. The three dated-commitment passages now use one wording. Every changed figure recomputes. No Role 4 number moved and no cite was lost. One minor contradiction is new. Brief 1b still says 'Filing wins' on the Digital claim and lists a MGMT-based ceiling as FILED. 7A now calls that ceiling context, and the claim unverifiable. Loop 1 aligned the matching held-steady row; this row was missed. The fix is one cell. No loop remains, so it goes forward as a flagged open item. Verdict, cash class, branch and WEAKENED do not change."
```
