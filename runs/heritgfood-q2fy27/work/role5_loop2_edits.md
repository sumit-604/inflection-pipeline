### EDIT 1 (S-2)
FIND:
<<<
the A5 Role 5 audit (work/audit_heritgfood_q2fy27_role5.md) findings
>>>
REPLACE:
<<<
the A5 Role 5 audit (work/audit_heritgfood_q2fy27_role5_run1.md) findings
>>>

### EDIT 2 (header, loop record)
FIND:
<<<
The protocol verdict and every filed number are unchanged. See the Role 5 loop 1 disposition table at the end.
>>>
REPLACE:
<<<
The protocol verdict and every filed number are unchanged. See the Role 5 loop 1 disposition table at the end.
Role 5 correction loop 2 (2026-10-20): the A5 Role 5 loop-1 re-audit (work/audit_heritgfood_q2fy27_role5_loop1.md) findings C-A, C-B, M-B and M-C were applied after a check against the A1 fulltexts. They are cited with the prefix R5L2-. Style notes S-1 to S-6 were applied; S-7 concerns a block file outside this review. M-A is an A2 ledger item, run in parallel: the concall row total and split below are A2's final figures. The protocol verdict and every filed number are unchanged. See the Role 5 loop 2 disposition table at the end.
>>>

### EDIT 3 (C-A)
FIND:
<<<
the concall ledger also carries 24 analyst questions and 336 structured rows.
>>>
REPLACE:
<<<
the concall ledger also carries 24 analyst questions and {{LEDGER_TOTAL}} rows (336 structured rows R001-R336 plus A2's MISSING_FROM_STRUCTURED rows M01-M32).
>>>

### EDIT 4 (C-A)
FIND:
<<<
concall 336 of 336 rows (R001-R336)
>>>
REPLACE:
<<<
concall {{LEDGER_TOTAL}} of {{LEDGER_TOTAL}} rows (R001-R336 and M01-M32)
>>>

### EDIT 5 (preamble findings list)
FIND:
<<<
R5-M1 (A2 ledger) handled separately; disposition table at the end.
>>>
REPLACE:
<<<
R5-M1 (A2 ledger) handled separately; disposition table at the end.
- Role 5 loop 2 (A5 Role 5 loop-1 re-audit): R5L2-C-A, R5L2-C-B, R5L2-M-B, R5L2-M-C applied; R5L2-S-1 to R5L2-S-6 applied; R5L2-S-7 (a block file) not in this review; R5L2-M-A (A2 ledger) handled in parallel; disposition table at the end.
>>>

### EDIT 6 (M-B, Q35 why and forks; S-5)
FIND:
<<<
Which is the Q3 guide, and what was the October landed cost per litre? | Each Rs 1/L is about Rs 15.90 Cr a quarter, 1.2% of Q2 revenue [derived]. Two readings of the Q3 level (Role 5 Step 2): last year's Q2-to-Q3 step reaches Rs 50.29/L; the slide 9 Jul-Sep slope gives Rs 48.4-50.1/L, where 11% needs the monthly climb to speed up about 1.3-1.7x [derived; INFERENCE]. October and November landed cost separate them. | October landed cost below Rs 50.0/L and easing into November. | October at or above Rs 50.0/L; 11% YoY holds.
>>>
REPLACE:
<<<
Which is the Q3 guide, and what were the September and October landed costs per litre? | Each Rs 1/L is about Rs 15.90 Cr a quarter, 1.2% of Q2 revenue [derived]. Two readings of the Q3 level (Role 5 Step 2): last year's Q2-to-Q3 step reaches Rs 50.29/L; the slide 9 slope gives Rs 48.4-50.1/L on the flat and Jul-Sep average-step paths and Rs 49.8-50.5/L on the September-step and rising-step paths, where 11% needs a monthly step 1.25-1.55x the September step [derived; INFERENCE]. KMF's Rs 6/L farm step from 1 November sits outside any slope (CC-L396-400) [MGMT, ASR; INFERENCE on transmission]. October lands near Rs 48.4-49.5/L on every path, so the October level alone does not separate the readings. The October step over September and the Q3 average do [derived]. | October up over September by no more than the September step (about Rs 0.7-0.8/L), and a Q3 average below Rs 50.0/L, easing into November. | October up by more than the September step, toward the Rs 1.0-1.1/L that 11% needs, or a Q3 average at or above Rs 50.0/L; 11% YoY holds.
>>>

### EDIT 7 (M-C, Q36)
FIND:
<<<
At Rs 50.0-50.56/L the floor needs Q3 realisation about 2.7-3.4% above Q2 on the same volume and mix [derived]. Q2 is the seasonal gross-margin high.
>>>
REPLACE:
<<<
Across the Q3 cost paths (Rs 48.40-50.56/L) the floor needs Q3 realisation about 0.8-3.4% above Q2 on the same volume and mix: about 0.8% flat at September, 2.4-2.8% on the average-step path, 3.4% at 11%; 2.7-3.4% at management's two statements (Rs 50.0-50.56/L) [derived]. Q2 is the seasonal gross-margin high.
>>>

### EDIT 8 (C-A, Role 5 ledger line)
FIND:
<<<
Ledger contains 81 turns / 24 analyst questions / 336 structured rows (NUMBER 162, ENTITY 52, FORWARD 60, DATE 20, QUALIFIER 42). All 336 rows reviewed. The A2 count test matched on every category, with no orphan IDs. A3 reconciled 336 of 336 (100%). No row is unreviewed. Findings incorporated: CC-A3-01 to CC-A3-21 (21), plus A4-OBS-2 (sequential bridge claim, FC-1) and A4-OBS-3 (competition exchange). A3's turn-cite slips (ledger C5, C6) affect no row. The A5 Role 5 audit found ten units (U1-U10) absent from the structured file and the ledger. This review cites U1-U8 directly from the fulltext by CC-L line. The A2 addendum is handled separately (R5-M1); the row count above stands until it lands.
>>>
REPLACE:
<<<
Ledger contains 81 turns / 24 analyst questions / {{LEDGER_TOTAL}} rows ({{LEDGER_SPLIT}}). That is the 336 structured rows R001-R336 (NUMBER 162, ENTITY 52, FORWARD 60, DATE 20, QUALIFIER 42) plus A2's MISSING_FROM_STRUCTURED addendum: M01-M10 (the A5 run1 units U1-U10, Role 5 loop 1) and M11-M32 (the A5 loop-1 units V1-V22, Role 5 loop 2). All {{LEDGER_TOTAL}} rows reviewed. Each M-row is a fulltext unit at a stated CC-L line, and this review cites every material one directly (U1-U8; V6, V8, V9, V11, V12, V13, V15, V16, V18, V20, V22). No orphan IDs (A5 role5-loop1 orphan check). A3 reconciled 336 of 336 structured rows (100%); the M-rows need no new forensic work. No row is unreviewed. Findings incorporated: CC-A3-01 to CC-A3-21 (21), plus A4-OBS-2 (sequential bridge claim, FC-1) and A4-OBS-3 (competition exchange). A2's turn-cite slips (ledger C5, C6) were corrected in the ledger in Role 5 loop 1 and affect no row. The two M-rows that are management FORWARD units (V14, V16) enter the 6B count.
>>>

### EDIT 9 (S-6)
FIND:
<<<
the NutriVate CEO thanks "Ramnigaru" (CC-L696).
>>>
REPLACE:
<<<
a speaker thanks "Ramnigaru" just before the NutriVate CEO introduces himself (CC-L696; the A1 turn map puts the line in T066, "moderator or management") [INFERENCE: ASR].
>>>

### EDIT 10 (S-4)
FIND:
<<<
Q3 FY26 base "about 45.55" (CC-L620-621).
>>>
REPLACE:
<<<
Q3 FY26 base "about 45.55" (CC-L620-621). In the same answer: "we also expect that ... the farmers should produce more milk and prices should come down" (CC-L616-617, V16); it leans toward reading 2.
>>>

### EDIT 11 (M-B, Step 2 reading 2)
FIND:
<<<
Reading 2 puts Q3 at Rs 48.4-50.1/L, nearer "not 47 to 50" than "11% might continue".
>>>
REPLACE:
<<<
Reading 2 puts Q3 at Rs 48.4-50.1/L on the flat and Jul-Sep average-step paths, nearer "not 47 to 50" than "11% might continue". The monthly step was not flat, though. It rose: on B by +Rs 0.20, +0.60 and +0.70/L in July, August and September; on A by +0.30, +0.71 and +0.82 (P-l276-288) [derived]. On the September step, Q3 is Rs 49.80/L (+9.3% YoY) on B or Rs 50.15/L (+10.1%) on A. If the step keeps rising at the August-to-September pace, Q3 is Rs 50.14/L (+10.1%) on B or Rs 50.51/L (+10.9%) on A, above the Rs 50.0 cap [derived; INFERENCE]. Against the September step, 11% needs a step 1.55x (B) or 1.25x (A) as large. So "nearer 'not 47 to 50'" holds on the flat and average-step paths only; on the rising-step path reading 2 sits near 11%. A slope also cannot see a discrete farm-price step. KMF passes Rs 6/L to farmers from 1 November (CC-L396-400), after the chart's last point, in a belt management calls cow-milk country, where it says the inflation sits (CC-L681-686) [MGMT, ASR; INFERENCE on transmission]. Aavin's two farm steps are dated "in this quarter" on an ASR line that does not fix the quarter (CC-L393-395).
>>>

### EDIT 12 (M-C, Step 2 floor)
FIND:
<<<
A move to Rs 50.0/L costs Rs 36.09 Cr a quarter; to Rs 50.56/L, Rs 44.99 Cr. Q2 operating EBITDA was Rs 73.97 Cr. Holding the floor needs Q3 realisation about 2.7% to 3.4% above Q2 on the same volume and mix [derived].
>>>
REPLACE:
<<<
Across the Q3 cost paths, holding the floor needs Q3 realisation above Q2, on the same volume and mix, of about 0.8-0.9% if cost holds at the September level (Rs 48.40-48.51/L; Rs 10.65-12.40 Cr a quarter), 2.4-2.8% on the Jul-Sep average-step path (Rs 49.69-50.05/L), 2.5-2.9% on the September step (Rs 49.80-50.15/L), 2.9-3.3% on the rising step (Rs 50.14-50.51/L), 3.1% on last year's step (Rs 50.29/L, Rs 40.70 Cr) and 3.4% at 11% (Rs 50.56/L, Rs 44.99 Cr). At management's two statements (Rs 50.0-50.56/L; Rs 36.09-44.99 Cr) it is 2.7-3.4%. Q2 operating EBITDA was Rs 73.97 Cr [derived].
>>>

### EDIT 13 (M-B, Exchange 1)
FIND:
<<<
Reading 2: the slide 9 Jul-Sep slope continues and takes Q3 to Rs 49.69-50.05/L (Rs 48.40-48.51/L if cost holds at the September level), nearer "not 47 to 50". On reading 2, 11% needs the monthly climb to speed up about 1.3-1.7x [derived; INFERENCE].
>>>
REPLACE:
<<<
Reading 2: the slide 9 slope. At the Jul-Sep average step Q3 is Rs 49.69-50.05/L (Rs 48.40-48.51/L if cost holds at the September level), nearer "not 47 to 50". The monthly step rose, though: at the September step Q3 is Rs 49.80-50.15/L, and a step still rising at the Aug-Sep pace gives Rs 50.14-50.51/L, near 11%. Against the September step, 11% needs a step 1.25-1.55x as large [derived; INFERENCE]. KMF's Rs 6/L farm step from 1 November sits outside any slope (CC-L396-400) [MGMT, ASR; INFERENCE on transmission].
>>>

### EDIT 14 (S-3)
FIND:
<<<
near 124 t a day at Rs 70/kg [derived]
>>>
REPLACE:
<<<
near 125 t a day at Rs 70/kg [derived]
>>>

### EDIT 15 (S-1, 6B rule)
FIND:
<<<
6B. Specificity score (A2 FORWARD rows; rule: quantified = carries a number or a named date or quarter).
>>>
REPLACE:
<<<
6B. Specificity score (A2 FORWARD rows; rule: quantified = carries a number or a named date or quarter. A festival anchor such as "post Diwali" (R223, CC-L296-297; R229, CC-L373) counts as unquantified, because no calendar date for it is in the corpus, as for M25).
>>>

### EDIT 16 (C-A, 6B rows and R236 wording)
FIND:
<<<
- Management forward rows: 57 (60 rows, less two analyst-voice rows R235 and R259 and the A2-flagged duplicate R247). R236, "Yes, that's what we are hoping" (CC-L408), is management's reply: A1 places it in turn T024 and labels it a management hope. The A2 analyst-voice flag on R236 is a ledger slip (R5-C1). 6C counts the same words as a hedge, so both steps now treat them the same way.
>>>
REPLACE:
<<<
- Management forward rows: 59. That is the 60 structured FORWARD rows, less two analyst-voice rows R235 and R259 and the A2-flagged duplicate R247, plus two management FORWARD units in A2's loop-2 addendum: V14 "If it comes down, well and good actually it is going to be tremendous" (CC-L606) and V16 "we also expect ... prices should come down" (CC-L616-617). R236, "Yes, that's what we are hoping" (CC-L408), is management's reply: A1 places it in turn T024 and labels it a management hope. The A2 analyst-voice flag on R236 was a ledger slip (R5-C1), now corrected: the ledger re-flags it FORWARD_MGMT at T024. 6C counts the same words as a hedge, so both steps treat them the same way.
>>>

### EDIT 17 (C-A, 6B unquantified)
FIND:
<<<
Unquantified: 41 (R236 included).
>>>
REPLACE:
<<<
Unquantified: 43 (R236, V14 and V16 included).
>>>

### EDIT 18 (C-A and S-1, 6B ratio)
FIND:
<<<
- Ratio: 16 / 57 = 0.28. Stricter counts give 0.25 (14 / 55, without the two third-party Karnataka rows) and 0.23 (12 / 53, also merging the three ice cream restatements). Below 0.3 on every count: heavy hedge.
>>>
REPLACE:
<<<
- Ratio: 16 / 59 = 0.27. Stricter counts give 0.25 (14 / 57, without the two third-party Karnataka rows) and 0.22 (12 / 55, also merging the three ice cream restatements). Below 0.3 on every count under the stated rule: heavy hedge. Counted with the two Diwali anchors, the ratio is 18 / 59 = 0.31, just above 0.3. The 6E row (0.5 or below) holds either way.
>>>

### EDIT 19 (C-A, 6E)
FIND:
<<<
6E. Management archetype. Specificity 0.28 puts the call
>>>
REPLACE:
<<<
6E. Management archetype. Specificity 0.27 (16 / 59) puts the call
>>>

### EDIT 20 (M-B, 8A seed row)
FIND:
<<<
or the slide 9 Jul-Sep slope (Rs 48.4-50.1/L); October and November landed cost separate them (Q35). Price step unquantified |
>>>
REPLACE:
<<<
or the slide 9 slope (Rs 48.4-50.1/L on the flat and Jul-Sep average-step paths; Rs 49.8-50.5/L on the September-step and rising-step paths, near 11%); the 1 Nov KMF farm step sits outside any slope (CC-L396-400); October and November landed cost separate them (Q35). Price step unquantified |
>>>

### EDIT 21 (C-B, Role 5 8C)
FIND:
<<<
The call moves the seed gross-margin item toward its red side (wider than -271 bps) on cost evidence only.
>>>
REPLACE:
<<<
On cost evidence alone, the call does not move the seed gross-margin item toward its red side. Every Q3 cost path in Step 2 puts YoY landed-cost inflation at +6.3% to +11.0% (Rs 48.40-50.56/L against the Rs 45.55/L base, +Rs 2.85 to +5.01/L), at or below Q2's +11.03% (Rs 47.73/L against Rs 42.99/L, +Rs 4.74/L; PR-L76-77) [derived]. On the same YoY price rise, the YoY gap holds or narrows. The call's price evidence points the same way: September hikes "much higher than 8%" and October opened "with much higher price levels" (CC-L364-367). The direction of the YoY gap rests on two items the call did not quantify: the Q3 price step (CC-L638-639) and the loss of the Q2 stock-drawdown benefit (Q34). The weaker reading is QoQ: season (FY26 H2 gross margin 183 bps below Q2) and Q3 cost Rs 0.67-2.83/L above Q2's Rs 47.73/L [derived].
>>>

### EDIT 22 (C-B, Concall Verdict)
FIND:
<<<
The evidence leans weaker on the Q3 margin path.
>>>
REPLACE:
<<<
The evidence leans weaker on the Q3 margin path QoQ (season; Q3 cost Rs 0.67-2.83/L above Q2). On cost alone the YoY gross-margin gap holds or narrows (8C).
>>>

### EDIT 23 (C-A, Concall Verdict archetype)
FIND:
<<<
- Management archetype (6E): NOT CLASSIFIABLE (specificity 0.28, lower row; credibility ND).
>>>
REPLACE:
<<<
- Management archetype (6E): NOT CLASSIFIABLE (specificity 0.27, lower row; credibility ND).
>>>

### EDIT 24 (C-B, Combined verdict)
FIND:
<<<
| Net thesis impact | n/a (pre-thesis); weaker on the Q3 margin path |
>>>
REPLACE:
<<<
| Net thesis impact | n/a (pre-thesis); weaker on the Q3 margin path QoQ (season, Q3 cost above Q2); on cost alone the YoY gap holds or narrows (8C) |
>>>

### EDIT 25 (M-B, F12)
FIND:
<<<
the slide 9 Jul-Sep slope gives Rs 48.4-50.1/L, where 11% needs the monthly climb to speed up about 1.3-1.7x [derived; INFERENCE]. October and November landed cost separate them (Q35).
>>>
REPLACE:
<<<
the slide 9 slope gives Rs 48.4-50.1/L on the flat and Jul-Sep average-step paths and Rs 49.8-50.5/L on the September-step and rising-step paths, where 11% needs a monthly step 1.25-1.55x the September step [derived; INFERENCE]. KMF's Rs 6/L farm step from 1 November sits outside any slope [MGMT, ASR; INFERENCE on transmission]. October and November landed cost separate them (Q35).
>>>

### EDIT 26 (M-C, F13)
FIND:
<<<
At Rs 50.0-50.56/L it needs Q3 realisation about 2.7-3.4% above Q2 on the same volume and mix [derived]; Q2 is the seasonal gross-margin high.
>>>
REPLACE:
<<<
Across the Q3 cost paths (Rs 48.40-50.56/L) it needs Q3 realisation about 0.8-3.4% above Q2 on the same volume and mix: about 0.8% flat at September, 2.4-2.8% on the average-step path, 3.4% at 11%; 2.7-3.4% at management's two statements (Rs 50.0-50.56/L) [derived]. Q2 is the seasonal gross-margin high.
>>>

### EDIT 27 (C-A, F17)
FIND:
<<<
| F17 | Hedge-heavy call: specificity 0.28 (below 0.3);
>>>
REPLACE:
<<<
| F17 | Hedge-heavy call: specificity 0.27 (below 0.3 under the stated rule; 0.31 with two festival anchors counted);
>>>

### EDIT 28 (C-A, protocol verdict paragraph)
FIND:
<<<
all four ledgers reconciled (concall 336 of 336)
>>>
REPLACE:
<<<
all four ledgers reconciled (concall {{LEDGER_TOTAL}} of {{LEDGER_TOTAL}} rows; A3 336 of 336 structured rows)
>>>

### EDIT 29 (M-B, brief part 1)
FIND:
<<<
The company's own monthly cost chart gives a second reading: Q3 at Rs 48.4-50.1, nearer the lower statement. October and November cost will decide [MGMT, derived; INFERENCE].
>>>
REPLACE:
<<<
The company's own monthly cost chart gives a second reading: Q3 at Rs 48.4-50.1 if the monthly rise holds at its Jul-Sep average, nearer the lower statement. The rise grew each month to September; if it keeps growing, Q3 reaches Rs 50.1-50.5, close to 11%. Karnataka's farm-price step from 1 November is not in the chart. October and November cost will decide [MGMT, derived; INFERENCE].
>>>

### EDIT 30 (M-C, brief part 1)
FIND:
<<<
It gave no Q3 price number [MGMT, ASR].
>>>
REPLACE:
<<<
It gave no Q3 price number [MGMT, ASR]. Holding it needs Q3 prices about 0.8-3.4% above Q2, depending on the cost path [derived].
>>>

### EDIT 31 (YAML loop field)
FIND:
<<<
loop: "role5-loop1"
>>>
REPLACE:
<<<
loop: "role5-loop2"
>>>

### EDIT 32 (YAML loop-2 record)
FIND:
<<<
role5_loop1_deferred: ["M1 (A2 ledger addendum, handled separately)"]
>>>
REPLACE:
<<<
role5_loop1_deferred: ["M1 (A2 ledger addendum, handled separately)"]
role5_loop2_findings_applied: [C-A, C-B, M-B, M-C, S-1, S-2, S-3, S-4, S-5, S-6]
role5_loop2_not_applied: ["M-A (A2 ledger addendum M11-M32, run in parallel; review carries A2's final total and split)", "S-7 (run1 block file, outside the review)"]
>>>

### EDIT 33 (C-A, YAML ledger_reconciliation)
FIND:
<<<
concall_rows: 336
>>>
REPLACE:
<<<
concall_rows: "{{LEDGER_TOTAL}}"   # R001-R336 plus M01-M32
  concall_split: "{{LEDGER_SPLIT}}"
>>>

### EDIT 34 (S-5, YAML Q35)
FIND:
<<<
or 'not 47 to 50'? October landed cost per litre?
>>>
REPLACE:
<<<
or 'not 47 to 50'? September and October landed cost per litre? (October level Rs 48.4-49.5 on every slide 9 path; the October step over September and the Q3 average separate the readings)
>>>

### EDIT 35 (M-B, YAML F12)
FIND:
<<<
two readings of the Q3 level: last year's step Rs 50.29/L vs slide 9 Jul-Sep slope Rs 48.4-50.1/L (11% needs a 1.3-1.7x faster climb); October-November landed cost separates them
>>>
REPLACE:
<<<
two readings of the Q3 level: last year's step Rs 50.29/L vs slide 9 slope Rs 48.4-50.1/L (flat and average-step paths) or Rs 49.8-50.5/L (September and rising-step paths; 11% needs 1.25-1.55x the September step); 1 Nov KMF farm step outside any slope; October-November landed cost separates them
>>>

### EDIT 36 (M-C, YAML F13)
FIND:
<<<
F13 EBITDA floor promised without a price number; at Rs 50.0-50.56/L needs ~2.7-3.4% Q3 realisation step on Q2 volume
>>>
REPLACE:
<<<
F13 EBITDA floor promised without a price number; across the Q3 cost paths (Rs 48.40-50.56/L) needs ~0.8-3.4% Q3 realisation step on Q2 volume (2.4-2.8% on the average-step path; 2.7-3.4% at management's Rs 50.0-50.56/L); Q2 is the seasonal gross-margin high
>>>

### EDIT 37 (C-A, YAML F17)
FIND:
<<<
F17 Hedge-heavy call: specificity 0.28;
>>>
REPLACE:
<<<
F17 Hedge-heavy call: specificity 0.27 (0.31 with festival anchors counted);
>>>

### EDIT 38 (C-A, YAML role5 ledger)
FIND:
<<<
ledger: {turns: 81, analyst_questions: 24, rows: 336, all_reviewed: true}
>>>
REPLACE:
<<<
ledger: {turns: 81, analyst_questions: 24, rows: "{{LEDGER_TOTAL}}", structured_rows: 336, addendum_rows: "M01-M32", split: "{{LEDGER_SPLIT}}", all_reviewed: true}
>>>

### EDIT 39 (C-A, YAML specificity)
FIND:
<<<
specificity_ratio: 0.28   # 16/57; stricter 0.25 and 0.23 (R5-C1)
>>>
REPLACE:
<<<
specificity_ratio: 0.27   # 16/59 (60 FORWARD rows less R235, R247, R259, plus V14, V16); stricter 0.25 and 0.22; 18/59 = 0.31 with festival anchors counted (R5-C1, R5L2-C-A, R5L2-S-1)
>>>

### EDIT 40 (C-A, YAML archetype)
FIND:
<<<
archetype_6e: "NOT CLASSIFIABLE (specificity 0.28, lower row; credibility ND)"
>>>
REPLACE:
<<<
archetype_6e: "NOT CLASSIFIABLE (specificity 0.27, lower row; credibility ND)"
>>>

### EDIT 41 (C-B, YAML net impact)
FIND:
<<<
net_concall_impact: "n/a (pre-thesis); evidence leans weaker on the Q3 margin path"
>>>
REPLACE:
<<<
net_concall_impact: "n/a (pre-thesis); evidence leans weaker on the Q3 margin path QoQ (season; Q3 cost Rs 0.67-2.83/L above Q2); on cost alone the YoY gross-margin gap holds or narrows (Q3 cost +6.3% to +11.0% YoY vs Q2 +11.03%)"
>>>

### EDIT 42 (M-B, M-C, C-B, C-A: analyst note)
FIND:
<<<
analyst_note: "Role 5 on the 16 Oct call, Role 5 loop 1 applied; merge done 2026-10-19. The transcript is machine ASR: call claims are [MGMT, ASR] and filings win. Verdict PROCEED WITH FLAGS; cash INDETERMINATE (no cash evidence on the call). The load-bearing signal is Q3 milk cost. Management said 11% YoY 'might continue' (Rs 50.56 on its Rs 45.55 base) and that cost will not go 'from 47 to 50'; they conflict. Two readings of the Q3 level: last year's Q2-to-Q3 step gives Rs 50.29; the slide 9 Jul-Sep slope gives Rs 48.4-50.1, where 11% needs a 1.3-1.7x faster climb. October and November landed cost separate them. Cow milk, about 80% of procurement, is the more inflationary species (working reading B). The EBITDA floor at Rs 50.0-50.56 needs about 2.7-3.4% more Q3 realisation. FC-1 fails on growth rates and holds on margin bps, with the cause overstated. Curd 'Rs 320 Cr' is most likely quarterly on the tonnage arithmetic, so curd, paneer and ghee are 81-86% of broader VAP; quarterly curd revenue settles it. KMF's Rs 6/L farm step is a cost risk as well as a sales opening."
>>>
REPLACE:
<<<
analyst_note: "Role 5 on the 16 Oct call; Role 5 loops 1 and 2 applied. The transcript is machine ASR: call claims are [MGMT, ASR] and filings win. Verdict PROCEED WITH FLAGS; cash INDETERMINATE. The load-bearing signal is Q3 milk cost. Management said 11% YoY 'might continue' (Rs 50.56 on its Rs 45.55 base) and that cost will not go 'from 47 to 50'; they conflict. Last year's Q2-to-Q3 step gives Rs 50.29. The slide 9 slope gives Rs 48.4-50.1 at the flat or average monthly step, but the step rose each month to September; on the September or a still-rising step Q3 is Rs 49.8-50.5, near 11%. KMF's 1 Nov farm step sits outside any slope. October and November landed cost separate the readings. Across that range the EBITDA floor needs about 0.8-3.4% more Q3 realisation. On cost alone the YoY gross-margin gap holds or narrows (Q3 cost +6.3% to +11.0% YoY vs Q2 +11.03%); the weaker read is QoQ. FC-1 fails on growth rates and holds on margin bps. Curd 'Rs 320 Cr' is most likely quarterly. The concall row total is A2's final count."
>>>

### EDIT 43 (S-2)
FIND:
<<<
Audit: work/audit_heritgfood_q2fy27_role5.md (A5, loop role5-run1)
>>>
REPLACE:
<<<
Audit: work/audit_heritgfood_q2fy27_role5_run1.md (A5, loop role5-run1)
>>>

### EDIT 44 (disposition table)
FIND:
<<<
| M1 | MISSING (A2) | Not applied by A4. It is an A2 ledger item, handled separately; the ledger was not edited. The Role 5 ledger line now notes the ten units and that U1-U8 are cited directly by CC-L line. | Audit Coverage table U1-U10. | Role 5 ledger reconciliation line (R-L842) |
>>>
REPLACE:
<<<
| M1 | MISSING (A2) | Not applied by A4. It is an A2 ledger item, handled separately; the ledger was not edited. The Role 5 ledger line now notes the ten units and that U1-U8 are cited directly by CC-L line. | Audit Coverage table U1-U10. | Role 5 ledger reconciliation line (R-L842) |

## Role 5 loop 2 disposition

Audit: work/audit_heritgfood_q2fy27_role5_loop1.md (A5, loop role5-loop1). Line references (R-L###) are to the 1,706-line review that A5's findings were applied to. Each fix was checked against the A1 fulltexts before writing; nothing under inputs/ was opened, and the A2 ledger was not edited. A5's text was supported in every case; nothing was rejected. The protocol verdict (PROCEED WITH FLAGS), cash conversion (INDETERMINATE) and every filed number are unchanged. The concall row total and split are A2's final figures, entered by the orchestrator.

| Finding | Type | Action | Verification (fulltext) | Sections changed |
|---|---|---|---|---|
| C-A | CONTRADICTION | Applied. The concall ledger reads {{LEDGER_TOTAL}} rows ({{LEDGER_SPLIT}}): R001-R336 plus M01-M32. "Until it lands" removed. The C5 and C6 turn slips are A2's, corrected in the ledger. The R236 flag "was" a ledger slip, now corrected. 6B is re-scored with the two management FORWARD units in the addendum (V14, V16): 16 / 59 = 0.27; stricter 0.25 and 0.22. The conclusion (below 0.3 under the rule; lower 6E row) is unchanged. | Ledger LG-L14 (M01-M10), LG-L350 (R236 FORWARD_MGMT at T024), LG-L538 (C5, C6 corrected); A5 V1-V22 table. CC-L606 (V14), CC-L616-617 (V16), both management (T049, T051). 14 / 57 = 0.246; 12 / 55 = 0.218. A5 supported. | Preamble (R-L22, R-L32); Role 5 ledger line (R-L844); 6B (R-L1138-1141); 6E (R-L1172); Concall Verdict (R-L1313); F17 (R-L1354); protocol verdict (R-L1359); YAML concall_rows, concall_split, role5 ledger, F17, specificity_ratio, archetype_6e |
| C-B | CONTRADICTION | Applied. 8C now says the call does not move the YoY gross-margin gap toward red on cost evidence: every Q3 cost path is at or below Q2's YoY cost inflation. The YoY direction rests on the unquantified Q3 price step and the lost Q2 stock-drawdown benefit (Q34). "Weaker on the Q3 margin path" is marked QoQ. | PR-L77 (Rs 47.73/L, +Rs 4.74/L: 47.73 / 42.99 = +11.03%); CC-L620-621 (Rs 45.55/L); Q3 paths Rs 48.40-50.56/L = +6.3% to +11.0% (+Rs 2.85 to +5.01/L); QoQ +Rs 0.67 to +2.83/L; CC-L364-367 (September hikes, October opening prices); CC-L638-639. A5 supported. | Role 5 8C (R-L1254); Concall Verdict (R-L1315); Combined verdict (R-L1328); YAML net_concall_impact, analyst note |
| M-B | MISSING | Applied. Reading 2 now carries the September-step path (Rs 49.80-50.15/L, +9.3% to +10.1%) and the rising-step path (Rs 50.14-50.51/L, +10.1% to +10.9%), tagged [derived; INFERENCE]. Against the September step, 11% needs 1.25-1.55x. "Nearer 'not 47 to 50'" now holds on the flat and average-step paths only. The 1 November KMF farm step is a discrete step outside any slope [MGMT, ASR; INFERENCE on transmission]. The separating observation is unchanged (Q35). | P-l276-288 (Rs 51.59-54.65 and Rs 38.80-40.73 series). B (0.8 x lower + 0.2 x upper): Jun 42.014, Jul 42.216, Aug 42.814, Sep 43.514; steps +0.20, +0.60, +0.70. A: Jul 50.334, Aug 51.046, Sep 51.866; steps +0.30, +0.71, +0.82. September step: 43.514 + 1.400 + 4.882 = 49.80; 51.866 + 1.640 - 3.352 = 50.15. Rising step (+0.102 / +0.108 a month): B average 45.254 + 4.882 = 50.14; A 53.866 - 3.352 = 50.51. 11%: 1.082 / 0.700 = 1.55x; 1.023 / 0.820 = 1.25x. CC-L396-400, CC-L681-686, CC-L393-395. A5 supported. | Step 2 diagnostics (R-L959); Exchange 1 (R-L1047); Role 5 8A seed (R-L1246); Q35 (R-L760); F12 (R-L1349); brief part 1 (R-L1380); YAML F12, Q35, analyst note |
| M-C | MISSING | Applied. The floor's price need is stated across the review's own range: about 0.8-0.9% flat at September, 2.4-2.8% on the average step, 2.5-2.9% on the September step, 2.9-3.3% on the rising step, 3.1% on last year's step, 3.4% at 11%; 2.7-3.4% at management's two statements. The seasonal headwind note stays. | PR-L121 (17.28 LLPD x 92 days = Rs 15.90 Cr per Rs 1/L); L407 (Q2 revenue Rs 1,319.58 Cr). (cost - 47.73) x 15.898 / 1,319.58: 48.40 0.81%; 48.51 0.94%; 49.69 2.36%; 49.80 2.49%; 50.00 2.73%; 50.05 2.80%; 50.14 2.90%; 50.15 2.92%; 50.29 3.08%; 50.51 3.35%; 50.56 3.41%. A5 supported. | Step 2 floor bullet (R-L960); Q36 (R-L761); F13 (R-L1350); brief part 1 (R-L1381); YAML F13, analyst note |
| S-1 | STYLE | Applied. 6B states that festival anchors ("post Diwali", R223, R229) count as unquantified, as for M25. Counted, the ratio is 18 / 59 = 0.31; "below 0.3" holds only under the rule. | CC-L296-297, CC-L373. | 6B (R-L1138, R-L1141); F17; YAML F17, specificity_ratio |
| S-2 | STYLE | Applied. The run1 audit path is work/audit_heritgfood_q2fy27_role5_run1.md. | File present; its header reads loop role5-run1. | Header (R-L10); Role 5 loop 1 disposition intro (R-L1687) |
| S-3 | STYLE | Applied. 125 t a day, not 124 t. | 3,200 m / Rs 70 per kg / 365 = 125.2 t. | 5A row 14 (R-L1088) |
| S-4 | STYLE | Applied. The Step 2 procurement row carries "prices should come down", which leans toward reading 2. | CC-L616-617. | Step 2 cost row (R-L943) |
| S-5 | STYLE | Applied. Q35 asks for September and October landed cost. The forks now use the October step over September against the September step, and the Q3 average against Rs 50.0/L. The October level alone (Rs 48.4-49.5/L on every path) does not separate the readings. | October landed, derived: B 48.40 flat, 49.05 average step, 49.10 September step, 49.20 rising step, 49.48 11% path; A 48.51 to 49.54. October step: 0.65-0.82 vs 1.02-1.08 for 11%. | Q35 (R-L760); YAML Q35 |
| S-6 | STYLE | Applied. "A speaker thanks Ramnigaru" with the T066 placement and [INFERENCE: ASR]; the line is no longer assigned to the NutriVate CEO. | A1 turn map: T066 lines 695-696, moderator or management; T067 lines 697-710, Dr. Bridge Mohan. | 0B Unmapped row (R-L872) |
| S-7 | STYLE | Not applied. It concerns work/blocks/a4-role5.yaml, a block file outside the review. | n/a | none |
| M-A | MISSING (A2) | Not applied by A4. A2 appends V1-V22 as M11-M32 and runs a closing sweep in parallel; the ledger was not edited. The review carries A2's final total and split. | A5 Coverage table V1-V22. | none (figures entered by the orchestrator) |
>>>
