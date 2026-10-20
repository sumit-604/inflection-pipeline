# ROLE 5 ADDENDUM: IN-PLACE EDITS TO THE ROLE 4 BODY (exact find / replace)

Apply each edit to work/review_heritgfood_q2fy27.md. FIND text is copied verbatim from the current file. Where a FIND is a single sentence or cell, replace only that text and leave the rest of the line unchanged.

## E1. Header (lines 3-14)

E1a. FIND (line 3): `Agent: A4 analyst | model: claude-opus-5-5 | date: 2026-10-17`
REPLACE: `Agent: A4 analyst | model: claude-opus-5-5 | date: 2026-10-17 | Role 5 addendum: 2026-10-19`

E1b. FIND (line 4): `Protocol loaded: frameworks/Quarterly_Results_Review_Protocol_v1_4.md (Role 4). Role 5 not passed: no concall transcript in this run.`
REPLACE: `Protocols loaded: frameworks/Quarterly_Results_Review_Protocol_v1_4.md (Role 4); frameworks/Quarterly_Concall_Analysis_Protocol_v1_1.md (Role 5), added in the 2026-10-19 addendum on the 16 Oct 2026 concall. Role 4 ran first, without a transcript.`

E1c. FIND (line 5, end): `press release (5 pages).`
REPLACE: `press release (5 pages); Role 5 addendum: the 16 Oct 2026 concall, a machine (ASR) transcript of the call recording, not a company-filed transcript.`

E1d. FIND (line 6): `A1 structured and fulltext for all three documents, A2 ledgers for all three, A3 forensics for all three, orchestrator Notion note.`
REPLACE: `A1 structured and fulltext for all four documents (concall added 2026-10-19), A2 ledgers for all four, A3 forensics for all four, orchestrator Notion note.`

E1e. INSERT after line 8 (Correction loop 2):
`Role 5 addendum (2026-10-19): Role 5 run on the concall in full step sequence. New section "ROLE 5: CONCALL ANALYSIS (ADDENDUM 2026-10-19)" sits after Step 9. In-place updates are listed in the Role 5 addendum change log at the end. Source caveat: the concall is an ASR transcript; most speakers are unattributed; the engine misspells names. Concall claims carry [MGMT, ASR]. Filings win on any number conflict (Role 5 Step 7D).`

E1f. FIND (line 10, end): `No HOLD/ADD/TRIM/EXIT framing appears in this review.`
REPLACE: `No HOLD/ADD/TRIM/EXIT framing appears in this review. Re-verified for Role 5 on 2026-10-19: no change.`

E1g. FIND (line 14, end): `A5 loop-2 (re-audit) finding IDs are prefixed L2- (L2-F1, L2-F2, L2-S9 to L2-S12).`
REPLACE: `A5 loop-2 (re-audit) finding IDs are prefixed L2- (L2-F1, L2-F2, L2-S9 to L2-S12). Role 5: "CC-L###" = concall fulltext line (extracted/heritgfood-concall-q2fy27-fulltext.md); concall A3 finding IDs are prefixed CC-A3-; CQ01-CQ24 = analyst questions on the call; K1-K24 = concall commitment register; FC-n and IC-n = filing-vs-call and in-call conflicts.`

## E2. Ledger reconciliation preamble (lines 20-28)

E2a. FIND (line 20, first sentence): `Ledger contains 12 notes / 0 turns / 50 slides (45 presentation slides + 5 press-release pages). All 12 notes, 0 turns and 50 slides reviewed.`
REPLACE: `Ledger contains 12 notes / 81 turns / 50 slides (45 presentation slides + 5 press-release pages); the concall ledger also carries 24 analyst questions and 336 structured rows. All 12 notes, 81 turns and 50 slides reviewed.`

E2b. FIND (line 20, continuing): `press release 180 of 180 rows (R001-R180). No ledger row is unreviewed. A2 gate passed on all three ledgers; A3 reconciled 100% on all three.`
REPLACE: `press release 180 of 180 rows (R001-R180), concall 336 of 336 rows (R001-R336). No ledger row is unreviewed. A2 gate passed on all four ledgers; A3 reconciled 100% on all four.`

E2c. FIND (line 22): `Findings incorporated (48: 47 A3 findings plus 1 A4 observation):`
REPLACE: `Findings incorporated (71: 68 A3 findings plus 3 A4 observations):`

E2d. INSERT after line 25 (Press release):
`- Concall (21, Role 5 addendum): CC-A3-01 to CC-A3-21.`

E2e. FIND (line 26): `- A4 addition (1): A4-OBS-1 (identical results commentary attributed to two different people; see Section 0F).`
REPLACE: `- A4 additions (3): A4-OBS-1 (identical results commentary attributed to two different people; see Section 0F); A4-OBS-2 (the call's sequential EBITDA-vs-PAT bridge contradicts the filing, Role 5 FC-1); A4-OBS-3 (unnamed conglomerate entrant raised on the call, CQ14).`

## E3. A3 finding disposition index: APPEND after the PR-A3-10 row (line 82)

| CC-A3-01 | FORWARD-SIGNAL | Role 5 Steps 2, 4C-1; Q35; M15; flag F12 |
| CC-A3-02 | FORWARD-SIGNAL | Role 5 Step 2; Q36; M16; flag F13 |
| CC-A3-03 | FORWARD-SIGNAL | Role 5 Step 7A; Q43 (and Q2); flag F4 |
| CC-A3-04 | FORWARD-SIGNAL | Q1 call status; Q44; M22 |
| CC-A3-05 | FORWARD-SIGNAL | Q45; M17 |
| CC-A3-06 | FORWARD-SIGNAL | Q46; M18 |
| CC-A3-07 | FORWARD-SIGNAL | Q9 call status; Q47; M19 |
| CC-A3-08 | AMBIGUOUS | Q39; M21 |
| CC-A3-09 | AMBIGUOUS | Role 5 Step 7A (resolved to YoY on the filing, FC-2); Q37 |
| CC-A3-10 | NEUTRAL-FACT | Role 5 Steps 2, 4C-3; Q51 |
| CC-A3-11 | FORWARD-SIGNAL | Role 5 Step 6C; Q35; M25; flag F12 |
| CC-A3-12 | AMBIGUOUS | Q38 |
| CC-A3-13 | AMBIGUOUS | Q40 |
| CC-A3-14 | AMBIGUOUS | Q41; M10 |
| CC-A3-15 | AMBIGUOUS | Q42 (and Q15, Q32); flag F5 |
| CC-A3-16 | FORWARD-SIGNAL | Slide 9 note (working reading B); Q29 status and revised forks; M14; flag F3 |
| CC-A3-17 | AMBIGUOUS | Section 0G VAP row; product-walk note; Q39; flag F5 |
| CC-A3-18 | AMBIGUOUS | Q10 call status; Q48 (FC-3) |
| CC-A3-19 | AMBIGUOUS | Q30 call status; flag F8 |
| CC-A3-20 | NEUTRAL-FACT | Step 8.5 call-status column; M23, M24; flag F14 |
| CC-A3-21 | NEUTRAL-FACT | Q22 call status; flag F8 |
| A4-OBS-2 | AMBIGUOUS | Role 5 Step 7D FC-1; Q49; flag F8 |
| A4-OBS-3 | AMBIGUOUS | Role 5 Steps 4A (CQ14), 5A; Q50; brief part 4 |

## E4. Section 0G, VAP row (line 171): APPEND to the end of the Status cell, after `(Q19, Q31).`

` Role 5 (16 Oct call) [MGMT, ASR]: management repeated 35.4% and +4.1 pp without stating the basis (CC-L200-201, CC-L476-477); Q19 not addressed. The call adds one element. Heritage supplies Get-A-Way 3,272 L/day of ice cream (CC-L230-232), about Rs 6.0 Cr a quarter at the stated Rs 200/L revenue (CC-L427) [derived; transfer price NOT FOUND]. Under reading B the parent's VAP line may hold this intra-group sale, which eliminates on consolidation; under reading A the line would hold Get-A-Way's external sales instead. Management also called own ice cream revenue "excluding getaway, because that's a subsidiary company" (CC-L774-775). Neither point separates the readings. Status unchanged: PARTLY RESOLVED, two readings.`

## E5. Product-walk note (line 344)

E5a. FIND: `and Get-A-Way (product line not stated in this corpus, PR-L147)`
REPLACE: `and Get-A-Way (an ice cream business per the 16 Oct call: the new facility adds capacity "for AlpenV and Getaway" and Heritage supplies it ice cream, CC-L227-232 [MGMT, ASR]; the filings and the release do not state its product line, PR-L147)`

E5b. APPEND to the end of line 344:
` Role 5 (16 Oct call): Heritage supplies Get-A-Way 3,272 L/day of ice cream (CC-L230-232) [MGMT, ASR], about Rs 6.0 Cr a quarter at Rs 200/L (CC-L427) [derived; transfer price NOT FOUND]. If that supply sits inside the release's ice cream growth (+81% revenue, +44% volume, PR-L87-90), part of the ice cream growth is intra-group and eliminates on consolidation [INFERENCE; Q39]. The call does not separate readings A and B.`

## E6. Operating KPI table, slide 9 rows (lines 358-359): replace the Source cell only

E6a. FIND: `P-l270-277 (positional; species unresolved)`
REPLACE: `P-l270-277 (positional; species not printed; buffalo under working reading B after the 16 Oct call, CC-L672, CC-L686 [MGMT, ASR])`

E6b. FIND: `P-l278-288 (positional; species unresolved)`
REPLACE: `P-l278-288 (positional; species not printed; cow under working reading B after the 16 Oct call, CC-L500-502, CC-L686 [MGMT, ASR])`

## E7. Slide 9 note (lines 364-366)

E7a. FIND (end of line 364): `A4 does not pick a reading: the species mapping is not printed.`
REPLACE: `Before the call A4 did not pick a reading: the species mapping is not printed.`

E7b. INSERT a new bullet after line 365 ("What holds in both readings"):
`- What the 16 Oct call adds (Role 5; CC-A3-16) [MGMT, ASR]: cow milk is about 80% of procurement "by volume" (CC-L500-502; "Kaunulk" read as cow milk [INFERENCE: ASR]). Cow milk "on a solid basis is cheaper than buffalo milk" (CC-L672). "The significant inflationary trend we have seen also is in the hardcore cow milk" (CC-L686). An analyst read the slide as showing cow milk "more inflationary" (CC-L651-654), and management did not correct it. Cheaper and more inflationary describes Series 2 (Rs 38.80-40.73/L; +15.5%, +15.0%, +14.5% YoY in Jul-Sep). Both statements fit reading B and contradict reading A. Working reading after the call: B. It is also the conservative reading. Reading A stays as the fallback until a filed transcript or a labelled slide prints the mapping. The call gave no per-litre cost by species.`

E7c. FIND (line 366): `- Separating observation: the species split of Q2 procurement cost (Q2 concall transcript, or a labelled Q3 FY27 slide 9). Question Q29; monitorable M14.`
REPLACE: `- Separating observation: the species split of Q2 procurement cost. The 16 Oct call met it in words, not in numbers. A company-filed transcript or a labelled Q3 FY27 slide 9 confirms it. Question Q29; monitorable M14.`

## E8. Step 3C, last bullet (line 402): replace the whole bullet

`- Implied Q3 FY27 base rate: the Q3 FY26 single-quarter base is ND in the filings; the call gives a Q3 FY26 landed cost of about Rs 45.55/L (CC-L620-621) [MGMT, ASR]. Against the H2 FY26 average (Op EBITDA margin 5.06%, core PBT Rs 31.92 Cr per quarter), Q3 FY27 holding Q2 FY27's 5.61% margin and Rs 39.23 Cr core PBT would show YoY improvement on the half-year average. Against Q2 FY27, three things point to pressure: the seasonal Q2-to-H2 step (-183 bps gross margin in FY26); the cost level still rising into September in both slide-9 series (PRE-A3-05; working reading B after the call puts cow-milk inflation at +14.5% YoY in September, slide 9 note); and management's own Q3 view that 11% procurement inflation "might continue", with October cost above September (CC-L375, CC-L381) [MGMT, ASR].`

## E9. Step 5.5B (line 560)

FIND: `The YoY inflation rate either rose every month or peaked in July, depending on the unresolved species mapping (slide 9 note).`
REPLACE: `The YoY inflation rate either rose every month or peaked in July, depending on the species mapping (slide 9 note); the 16 Oct call favours the July-peak reading for cow milk (working reading B, CC-L686) [MGMT, ASR].`

## E10. Step 7 (line 652)

FIND: `Revised fair values: none (deferred).`
REPLACE: `Revised fair values: none (deferred). Role 5 Step 8D flags the concall's pillar-relevant facts; the recompute stays deferred (OR-30).`

## E11. Step 8A-W: INSERT after line 670 ("The observation that separates them")

`- Role 5 addendum (16 Oct call) [MGMT, ASR]: the bull side gains an EBITDA floor promise (CC-L603-604), a one-way price ratchet (CC-L411-418) and a dated Karnataka price move from 1 November (CC-L396-403). The bear side gains a Q3 procurement-inflation view of about 11% (CC-L381), October cost above September (CC-L375), cow milk (about 80% of procurement) as the more inflationary species (CC-L686), and silence on the CWIP project and the subsidiary results. None of this is filed evidence. The separating observation is unchanged. Q3 landed cost against Rs 50.0/L checks management's two cost statements (Role 5 Step 2).`

## E12. Step 8C: INSERT after line 685 ("Cross-check, not a threshold")

`- Secondary checks from the 16 Oct call (Role 5) [MGMT, ASR], not thresholds: Q3 landed cost per litre against Rs 50.0/L (below confirms "not 47 to 50", CC-L618; at or above Rs 50.56/L confirms "11% might continue" on the Rs 45.55 base, CC-L381, CC-L621); Q3 operating EBITDA against Rs 73.97 Cr and 5.61% (management's floor, CC-L603-604).`

## E13. Step 9 (line 767): APPEND to the end of the Key Notes line, inside the quotes

` | 2026-10-19 | Q2 FY27 concall (ASR): Q3 milk cost +11% YoY 'might continue' vs 'not 47 to 50'; EBITDA floor promised; cow (80% of procurement) the more inflationary species; 26 of 34 questions not addressed (not asked); credibility ND (first call); PROCEED WITH FLAGS.`

## E14. New section placement

Insert work/review_role5_part1_steps0-4.md then work/review_role5_part2_steps5-9.md (strip their MERGE NOTE comments) between the end of STEP 9 (after line 767 and its `---`) and `## FLAGS AND PROTOCOL VERDICT`. Follow with `---`.

## E15. Replacement sections (separate files)

- Step 8.5 (lines 690-736): replace with work/review_role5_part4_step85.md.
- Monitorables (lines 740-761): replace with the Monitorables block in work/review_role5_part5_flags_brief.md.
- FLAGS AND PROTOCOL VERDICT (lines 771-787) and PLAIN-LANGUAGE BRIEF (lines 791-852): replace with work/review_role5_part5_flags_brief.md.
- YAML block (lines 856-947): replace with work/blocks/a4-role5.yaml (fenced as ```yaml).
- After the Loop 2 disposition table (end of file): append work/review_role5_part6_changelog.md.
