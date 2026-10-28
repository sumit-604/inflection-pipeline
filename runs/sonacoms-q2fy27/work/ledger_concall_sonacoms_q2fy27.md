# LEDGER concall SONACOMS q2fy27 (A2 enumerator)

Source: A1 structured extraction (R001-R336). Anchors are fulltext L### lines and [hh:mm:ss] timestamps, not pages. Speakers unnamed in source: all turn speaker labels are INFERRED from moderator introductions and content. No claim text is re-copied; rows reference A1 IDs. MISSING_FROM_STRUCTURED rows carry their own text and line number.

=== A2 COUNT TEST ===
category: structured_rows     grep_count: 336  sweep_count: 336  match: yes   (NUMBER 122 | ENTITY 86 | FORWARD 62 | DATE 33 | QUALIFIER 33; A1 header and independent grep agree)
category: participants       grep_count: 15   sweep_count: 15   match: yes   (8 management R126-R133, 1 host R124, 5 analysts R158/R165-R168, 1 unnamed moderator; R134 and R164 are alias rows, not extra people)
category: turns              grep_count: 53   sweep_count: 53   match: yes   (grep: 9 INFERRED TURN BOUNDARY rows R200-R208, 6 moderator Q&A cues, plus change-of-speaker sweep of fulltext; sweep T01-T53)
category: questions          grep_count: 18   sweep_count: 18   match: yes   (grep fulltext "question|second question|final one|last question" cues cross-checked against sweep: Arvind 3, Chandra 2, Gunjan 3, Basudev 3, Ramod 4, chat 3)
category: mgmt_numbers       grep_count: 110  sweep_count: 110  match: yes   (122 NUMBER rows less 12 analyst/moderator-spoken: R001,R081,R082,R087,R088,R089,R095,R097,R098,R099,R100,R106)
category: forward_hedge       grep_count: 62 FORWARD + 5 policy/hedge QUALIFIER (R309,R310,R332,R333,R336)  sweep_count: same  match: yes
category: zero_standing       grep_count: 0    sweep_count: 0    match: yes   (no nil/zero standing line items in a transcript; A1 header says none)
category: missing_from_structured  fulltext sweep found 9 units not in A1 (M01-M09, section 8)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 336 | ids_referenced_in_ledger: 336 | orphan_ids: [] | match: yes
(plus 9 MISSING_FROM_STRUCTURED rows M01-M09 carrying their own line numbers)

## 1. Participants (both sides)
| ROW_ID | category | A2 flags | note |
|---|---|---|---|
| R124 | participant:host analyst |  | Kapil Singh, Nomura; hosts call |
| R125 | participant:host firm |  | Nomura |
| R126 | participant:management |  | MD and Group CEO; present |
| R127 | participant:management | ASR_NAME | Drive Line CEO, full-time director |
| R128 | participant:management |  | CEO Motor Business |
| R129 | participant:management |  | Group CTO |
| R130 | participant:management |  | Group CFO |
| R131 | participant:management |  | Head Railway Business |
| R132 | participant:management |  | Investor Relations |
| R133 | participant:management | ASR_NAME | Head Strategy and MMA |
| R134 | participant:alias | ASR_NAME | ASR self-name of CEO speaker, not a separate person |
| R158 | participant:analyst |  | Q1 |
| R164 | participant:alias |  | Sat = Satmohan Gupta (R128) |
| R165 | participant:analyst |  | Q2 |
| R166 | participant:analyst |  | Q3 |
| R167 | participant:analyst |  | Q4 |
| R168 | participant:analyst | ASR_NAME | Q5 |

MGMT_ABSENCE: none. MD and Group CEO present and speaks T03 and through Q&A. Management present: 8 named (R126-R133). Analyst firms: NOT FOUND in source for all five analysts; moderator gives names only. Chat-box questioners unnamed (T44, T46, T49).

## 2. Speaker turns (sequential, INFERRED boundaries)
Prepared remarks T01-T05, Q&A T06-T53. By line span, Q&A = L377-L921 = 545 of 921 lines (59%); prepared L3-L376 (41%).
| turn | lines | speaker (inferred) | structured IDs in turn | note |
|---|---|---|---|---|
| T01 | L1-L14 | Moderator (Nomura/Webex operator, unnamed) | R001..R307 (8 rows) |  |
| T02 | L15-L28 | Kapil Singh (Nomura host) introduces management | R124..R133 (10 rows) |  |
| T03 | L29-L280 | MD and Group CEO (opening remarks; ASR self-name "Gopal") | R002..R327 (94 rows) | boundary row R206 (INFERRED TURN BOUNDARY) |
| T04 | L281-L302 | Praveen Rao, Group CTO (prepared remarks) | R152..R207 (6 rows) | boundary row R207 (INFERRED TURN BOUNDARY) |
| T05 | L303-L376 | Rohit Nanda, Group CFO (prepared remarks) | R043..R324 (60 rows) | boundary row R208 (INFERRED TURN BOUNDARY) |
| T06 | L377-L384 | Moderator opens Q&A, rules | R081..R308 (3 rows) |  |
| T07 | L385-L396 | Arvind Sharma (Q1 analyst; firm NOT FOUND) | R082..R200 (3 rows) | boundary row R200 (INFERRED TURN BOUNDARY) |
| T08 | L397-L432 | MD and Group CEO answer (suspension motors) | R159..R332 (7 rows) |  |
| T09 | L433-L434 | Arvind Sharma follow-up (Denso tie up) | R161..R161 (1 rows) |  |
| T10 | L435-L440 | MD/CEO and CFO answer (JV1) | R162..R290 (6 rows) |  |
| T11 | L441-L445 | Satmohan Gupta, CEO Motor Business (JV2) | R163..R291 (4 rows) |  |
| T12 | L446-L448 | Arvind Sharma thanks | none |  |
| T13 | L449-L453 | MD/CEO clarification (holidays) | none |  |
| T14 | L454-L455 | Arvind Sharma closes | none |  |
| T15 | L456-L456 | Moderator introduces Chandra Moli Mutia | R165..R201 (2 rows) | boundary row R201 (INFERRED TURN BOUNDARY) |
| T16 | L457-L478 | Chandra Moli Mutia (Q2 analyst; firm NOT FOUND) | R169..R171 (2 rows) |  |
| T17 | L479-L511 | MD and Group CEO answer (Europe, actuators) | R083..R329 (9 rows) |  |
| T18 | L512-L512 | Chandra Moli Mutia closes | none |  |
| T19 | L513-L513 | Moderator introduces Gunjan Prithyani | R166..R202 (2 rows) | boundary row R202 (INFERRED TURN BOUNDARY) |
| T20 | L514-L539 | Gunjan Prithyani (Q3 analyst; firm NOT FOUND) | R199..R199 (1 rows) |  |
| T21 | L540-L545 | MD and Group CEO answer opens, hands to Sat | none |  |
| T22 | L546-L556 | Satmohan Gupta answer (traction motors) | R229..R229 (1 rows) |  |
| T23 | L557-L557 | Gunjan Prithyani follow-up (3W size, inferred) | none |  |
| T24 | L558-L575 | Satmohan Gupta answer (3W, magnets, light rare earth) | R188..R231 (3 rows) |  |
| T25 | L576-L596 | MD/CEO answer (differential assemblies) | R292..R292 (1 rows) |  |
| T26 | L597-L597 | Gunjan Prithyani closes | none |  |
| T27 | L598-L598 | Moderator introduces Basudev Banerjee | R167..R203 (2 rows) | boundary row R203 (INFERRED TURN BOUNDARY) |
| T28 | L599-L609 | Basudev Banerjee (Q4 analyst; firm NOT FOUND) Q1 margin | R087..R089 (3 rows) |  |
| T29 | L610-L616 | MD and Group CEO answer (margin range) | R090..R233 (3 rows) |  |
| T30 | L617-L638 | Rohit Nanda, CFO answer (margin range) | R091..R333 (10 rows) |  |
| T31 | L639-L643 | Basudev Banerjee Q2 (cash, gross or net) | R095..R095 (1 rows) |  |
| T32 | L644-L644 | CFO reply: gross | R096..R314 (2 rows) |  |
| T33 | L645-L659 | Basudev Banerjee (net cash estimate, M&A deployment) | R097..R330 (10 rows) |  |
| T34 | L660-L704 | MD and Group CEO answer (cash deployment, M&A) | R101..R296 (13 rows) |  |
| T35 | L705-L705 | Basudev closes; moderator introduces Ramod Kumar | R168..R204 (2 rows) | boundary row R204 (INFERRED TURN BOUNDARY) |
| T36 | L706-L726 | Ramod Kumar (Q5 analyst; firm NOT FOUND) humanoid, EV driver infra | R106..R173 (3 rows) |  |
| T37 | L727-L767 | MD and Group CEO answer (robotics) | R107..R309 (16 rows) |  |
| T38 | L768-L771 | Ramod Kumar follow-up (inflection year) | none |  |
| T39 | L772-L800 | MD and Group CEO answer (no timeline) | R111..R336 (12 rows) |  |
| T40 | L801-L807 | Ramod Kumar or host: railway outlook question (speaker ambiguous) | R178..R178 (1 rows) |  |
| T41 | L808-L825 | Amit Mishra, Head Railway Business answer | R117..R310 (14 rows) |  |
| T42 | L826-L829 | Questioner thanks | none |  |
| T43 | L830-L838 | MD and Group CEO (25% CAGR aspiration) | R119..R260 (4 rows) |  |
| T44 | L839-L844 | Moderator reads chat Q1 (heavy rare earth) | R183..R205 (2 rows) | boundary row R205 (INFERRED TURN BOUNDARY) |
| T45 | L845-L855 | MD/CEO answer (heavy rare earth) | R184..R262 (3 rows) |  |
| T46 | L856-L857 | Moderator reads chat Q2 (pass-through) | none |  |
| T47 | L858-L859 | MD and Group CEO answer (pass-through) | none |  |
| T48 | L860-L882 | CFO / MD answer (lead-lag, numerator-denominator) | R120..R334 (7 rows) |  |
| T49 | L883-L885 | Moderator reads chat Q3 (humanoid deployment) | none |  |
| T50 | L886-L898 | MD and Group CEO answer (humanoid deployment) | R266..R335 (4 rows) |  |
| T51 | L899-L900 | Moderator closes Q&A, hands to CEO | none |  |
| T52 | L901-L916 | MD and Group CEO closing remarks | R269..R269 (1 rows) |  |
| T53 | L917-L921 | Moderator concludes call | none |  |

Row IDs per turn are by anchor line (rows are not contiguous in ID order); section 7 is the full per-ID map.

## 3. Questions ledger
| Q | turn | analyst | firm | topic | flags | note |
|---|---|---|---|---|---|---|
| Q01 | T07 | Arvind Sharma (R158) | NOT FOUND | suspension motors: key driver of strong growth (L393-L395) |  | 2-question rule R308; also R037/R082 |
| Q02 | T07 | Arvind Sharma (R158) | NOT FOUND | suspension motors: order pipeline in segment (L396) |  | part of question 1; answer R220-R222 |
| Q03 | T09 | Arvind Sharma (R158) | NOT FOUND | Denso tie up / JV timelines (L433-L434) |  | answers R223-R226; entities R161-R163 |
| Q04 | T16 | Chandra Moli Mutia (R165) | NOT FOUND | Europe competitive situation, legacy business growth runway (L459-L469) |  | answers R227,R228 |
| Q05 | T16 | Chandra Moli Mutia (R165) | NOT FOUND | robotics actuators, internal milestones (L470-L477) | REPEAT_QUESTION (robotics: Q05,Q12,Q13,Q14,Q18) | answer in T17 |
| Q06 | T20 | Gunjan Prithyani (R166) | NOT FOUND | traction motor scale-up, wallet share, 3W, new program (L514-L530) |  | answers T21-T24; R229-R231 |
| Q07 | T20 | Gunjan Prithyani (R166) | NOT FOUND | differential assembly improvement, North America, program or geo-mix (L531-L539) |  | answer T25 |
| Q08 | T23 | Gunjan Prithyani (R166) | NOT FOUND | follow-up: how significant is 3W within traction motors (L557) |  | speaker inferred; third ask (exceeds R308) |
| Q09 | T28 | Basudev Banerjee (R167) | NOT FOUND | EBITDA margin 23-25% range given mix (motor controller, robotics, railways) (L599-L609) | REPEAT_QUESTION (margin: Q09,Q17) | answers R232-R238 |
| Q10 | T31 | Basudev Banerjee (R167) | NOT FOUND | cash and liquid investments 1,900 cr: net or gross (L640-L643) |  | answer R096,R314 |
| Q11 | T33 | Basudev Banerjee (R167) | NOT FOUND | deployment of 2,800-3,000 cr net cash, M&A, aerospace (L645-L659) |  | third ask; answers R239-R243 |
| Q12 | T36 | Ramod Kumar (R168) | NOT FOUND | humanoid robot opportunity: 60% BOM, validation spend, timeline, capital allocation (L711-L722) | REPEAT_QUESTION (robotics: Q05,Q12,Q13,Q14,Q18) | answer R244-R249 |
| Q13 | T36 | Ramod Kumar (R168) | NOT FOUND | positioning EV driveline infrastructure as supplier for large robotics projects (L723-L726) | REPEAT_QUESTION (robotics: Q05,Q12,Q13,Q14,Q18) | customer-name rule R306/R309 invoked |
| Q14 | T38 | Ramod Kumar (R168) | NOT FOUND | which year is the big robotics inflection point (L768-L771) | REPEAT_QUESTION (robotics: Q05,Q12,Q13,Q14,Q18) | answer R250,R251; no guidance |
| Q15 | T40 | Ramod Kumar or host (ambiguous) | NOT FOUND | railway growth outlook next couple of years (L801-L805) |  | fourth ask by Ramod if same speaker, exceeds R308; answer R253-R258 |
| Q16 | T44 | chat-box (unnamed) | NOT FOUND | heavy rare earth: switch back for performance motors (L841-L844) |  | answer R261,R262 |
| Q17 | T46 | chat-box (unnamed) | NOT FOUND | pass-through arrangements to insulate margins (L856-L857) | REPEAT_QUESTION (margin: Q09,Q17) | answer R263-R265, illustration R120-R122 |
| Q18 | T49 | chat-box (unnamed) | NOT FOUND | humanoid robots on Sona Comstar production flows (L883-L885) | REPEAT_QUESTION (robotics: Q05,Q12,Q13,Q14,Q18) | answer R266-R268 |

Questions: 18 asks across 6 questioner groups (5 named analysts plus chat). Q&A rule is max two per participant (R308); Ramod Kumar shows up to four asks, Arvind, Gunjan and Basudev three each (follow-ups). Absence of ask (not management silence): no analyst question on working capital, receivables, tax rate, customer concentration percentages or Novelic ramp.

## 4. Management numbers (turn-tagged)
| ROW_ID | turn | A2 flags | cross-ref / note |
|---|---|---|---|
| R002 | T03 |  |  |
| R003 | T03 |  |  |
| R004 | T03 | RESTATED | RESTATED R209 (10x over 10 yrs) |
| R005 | T03 |  |  |
| R006 | T03 | ASR | ASR (freight as "Prey trades") |
| R007 | T03 | RESTATED | RESTATED R014,R047 (129% BEV/EV growth) |
| R008 | T03 |  |  |
| R009 | T03 |  | see R275 |
| R010 | T03 |  |  |
| R011 | T03 | RESTATED | RESTATED R043 (35% Q2 rev growth) |
| R012 | T03 | RESTATED | RESTATED R049 (23% EBITDA growth; collides with 23% margin R051/R088); AMBIGUOUS: "23%" appears as EBITDA growth (R049) and as margin (R051); keep distinct |
| R013 | T03 | RESTATED | RESTATED R053 (29% PAT growth) |
| R014 | T03 | RESTATED | RESTATED R007,R047 |
| R015 | T03 | RESTATED | RESTATED R048,R115 (BEV >half of auto revenue; 51%) |
| R016 | T03 |  |  |
| R017 | T03 | RESTATED | RESTATED R050 (356 cr Q2 EBITDA) |
| R018 | T03 | RESTATED | RESTATED R057 (43% H1 rev) |
| R019 | T03 | RESTATED,ASR | RESTATED R062 (34% H1 EBITDA); ASR ("India impact") |
| R020 | T03 | RESTATED,ASR | RESTATED R066 (36% H1 PAT); ASR |
| R021 | T03 | ASR | ASR unit "10 billion"; RECONCILE A3: "10 billion" EV H1 revenue vs R060 2,042 cr BEV H1 revenue vs R058 2,857 cr total; units and basis differ |
| R022 | T03 |  | see R023,R061 (EV share) |
| R023 | T03 | RESTATED | RESTATED R061 (48%) |
| R024 | T03 |  |  |
| R025 | T03 |  |  |
| R026 | T03 |  |  |
| R027 | T03 |  |  |
| R028 | T03 |  |  |
| R029 | T03 |  |  |
| R030 | T03 |  |  |
| R031 | T03 | ASR | see R313; unit as spoken "billion" |
| R032 | T03 | RESTATED,ASR | RESTATED R108 (251 billion); see R313; unit as spoken "billion" |
| R033 | T03 | RESTATED | RESTATED R108 (4% robotics) |
| R034 | T03 |  | historic look-east ref |
| R035 | T03 |  | historic ref vs R034 |
| R036 | T03 | RESTATED | RESTATED R282 |
| R037 | T03 | RESTATED,ASR | RESTATED R082 (7%, analyst); ASR |
| R038 | T03 |  |  |
| R039 | T03 |  |  |
| R040 | T03 |  | see R327 annualised |
| R041 | T03 |  |  |
| R042 | T03 |  | see R326 |
| R043 | T05 | RESTATED | RESTATED R011 |
| R044 | T05 |  |  |
| R045 | T05 |  |  |
| R046 | T05 |  |  |
| R047 | T05 | RESTATED | RESTATED R007,R014 |
| R048 | T05 | RESTATED | RESTATED R015,R115 |
| R049 | T05 | RESTATED | RESTATED R012 |
| R050 | T05 | RESTATED | RESTATED R017 |
| R051 | T05 |  |  |
| R052 | T05 |  | CHECK A3: "2.3%" margin delta vs 23% margin (R051); possible ASR merge |
| R053 | T05 | RESTATED | RESTATED R013 |
| R054 | T05 | ASR | ASR truncated: 23 crores vs 29% and 14.4% margin; A3 verify against press release |
| R055 | T05 |  |  |
| R056 | T05 |  | approx ("about half percent") |
| R057 | T05 | RESTATED | RESTATED R018 |
| R058 | T05 |  |  |
| R059 | T05 | ASR | ASR ("BV") |
| R060 | T05 |  | RECONCILE A3: vs R021 (10 billion) and R061/R023 (48% share); basis automotive product sales vs total |
| R061 | T05 | RESTATED | RESTATED R023 |
| R062 | T05 | RESTATED | RESTATED R019 |
| R063 | T05 |  | see R050 (H1 vs Q2 EBITDA) |
| R064 | T05 |  |  |
| R065 | T05 |  | approx ("about one and a half percent") |
| R066 | T05 | RESTATED | RESTATED R020 |
| R067 | T05 |  |  |
| R068 | T05 |  |  |
| R069 | T05 |  |  |
| R070 | T05 |  |  |
| R071 | T05 |  | cash conversion 90% of EBITDA (CFO) |
| R072 | T05 |  | WC release (CFO) |
| R073 | T05 |  | capex H1 (CFO) |
| R074 | T05 |  |  |
| R075 | T05 |  |  |
| R076 | T05 |  |  |
| R077 | T05 |  |  |
| R078 | T05 |  |  |
| R079 | T05 |  |  |
| R080 | T05 | RESTATED | RESTATED R095 (analyst reads 1,900) |
| R083 | T17 | ASR | ASR ("differential years") |
| R084 | T17 |  |  |
| R085 | T17 | ASR | ASR ambiguity |
| R086 | T17 |  | ex-China basis, see R328 |
| R090 | T29 | RESTATED | RESTATED R091,R232,R234 (23-25% margin range) |
| R091 | T30 | RESTATED | RESTATED R090,R232,R234 |
| R092 | T30 |  | see R237 |
| R093 | T30 |  | tolerance statement |
| R094 | T30 |  | HYPOTHETICAL scenario (oil 150), not guidance |
| R096 | T32 |  |  |
| R101 | T34 | RESTATED | RESTATED R192 |
| R102 | T34 |  | see R241 |
| R103 | T34 |  | see R241 filter 1 |
| R104 | T34 |  | see R241 filter 2 |
| R105 | T34 | ASR | ASR ("cash to a better"); capital allocation threshold |
| R107 | T37 |  |  |
| R108 | T37 | RESTATED,ASR | RESTATED R032,R033; unit differs ($250 billion vs R032 251 billion) |
| R109 | T37 | RESTATED | RESTATED R248 (62 cr robotics capex) |
| R110 | T37 | RESTATED | RESTATED R297 |
| R111 | T39 |  | ANECDOTE (2016) |
| R112 | T39 |  | ANECDOTE |
| R113 | T39 |  | ANECDOTE |
| R114 | T39 |  | see R115 (1% in 2019 to 51%); ANECDOTE |
| R115 | T39 | RESTATED | RESTATED R015,R048 |
| R116 | T39 |  | external compute-cost anecdote (CEO) |
| R117 | T41 | RESTATED | RESTATED R300,R253 |
| R118 | T41 | RESTATED | RESTATED R301,R258 |
| R119 | T43 | RESTATED | RESTATED R259,R260 (25% CAGR) |
| R120 | T48 |  | ILLUSTRATIVE (hypothetical), not a company figure |
| R121 | T48 |  | ILLUSTRATIVE |
| R122 | T48 |  | ILLUSTRATIVE |

Analyst or moderator spoken numbers (excluded from the management count): R081(moderator,T06), R082(analyst,T07), R087(analyst,T28), R088(analyst,T28), R089(analyst,T28), R095(analyst,T31), R097(analyst,T33), R098(analyst,T33), R099(analyst,T33), R100(analyst,T33), R106(analyst,T36), R001(moderator,T01).

## 5. Forward commitments and hedges (turn-tagged)
| ROW_ID | turn | class | note |
|---|---|---|---|
| R209 | T03 | forward | COMMITMENT-AMBITION |
| R210 | T03 | forward | CONFIDENCE |
| R211 | T03 | forward | HEDGE (uncertain) |
| R212 | T03 | forward | HEDGE (difficult to predict) |
| R213 | T03 | forward |  |
| R214 | T03 | forward |  |
| R215 | T03 | forward |  |
| R216 | T03 | forward |  |
| R217 | T03 | forward | ASPIRATION |
| R218 | T03 | forward |  |
| R219 | T05 | forward |  |
| R220 | T08 | forward |  |
| R221 | T08 | forward |  |
| R222 | T08 | forward | HEDGE (potential) |
| R223 | T10 | forward |  |
| R224 | T10 | forward | COMMITMENT (target date) |
| R225 | T10 | forward | HEDGE (may spill) |
| R226 | T11 | forward | COMMITMENT (target date) |
| R227 | T17 | forward |  |
| R228 | T17 | forward | SOFT |
| R229 | T22 | forward | HEDGE (pretty good) |
| R230 | T24 | forward | COMMITMENT (launch) |
| R231 | T24 | forward |  |
| R232 | T29 | forward | COMMITMENT (range held) |
| R233 | T29 | forward |  |
| R234 | T30 | forward | COMMITMENT (range held) |
| R235 | T30 | forward | CONDITIONAL |
| R236 | T30 | forward | CONDITIONAL |
| R237 | T30 | forward | HEDGE (ballpark) |
| R238 | T30 | forward | CONDITIONAL |
| R239 | T34 | forward |  |
| R240 | T34 | forward |  |
| R241 | T34 | forward |  |
| R242 | T34 | forward |  |
| R243 | T34 | forward | COMMITMENT (threshold) |
| R244 | T37 | forward | ASPIRATION |
| R245 | T37 | forward |  |
| R246 | T37 | forward | CONDITIONAL |
| R247 | T37 | forward |  |
| R248 | T37 | forward |  |
| R249 | T37 | forward |  |
| R250 | T39 | forward | HEDGE/NO_GUIDANCE |
| R251 | T39 | forward |  |
| R252 | T39 | forward |  |
| R253 | T41 | forward | COMMITMENT-soft |
| R254 | T41 | forward |  |
| R255 | T41 | forward |  |
| R256 | T41 | forward |  |
| R257 | T41 | forward |  |
| R258 | T41 | forward | COMMITMENT-soft |
| R259 | T43 | forward | COMMITMENT-AMBITION |
| R260 | T43 | forward | COMMITMENT-AMBITION |
| R261 | T45 | forward |  |
| R262 | T45 | forward | CONDITIONAL |
| R263 | T48 | forward |  |
| R264 | T48 | forward |  |
| R265 | T48 | forward |  |
| R266 | T50 | forward |  |
| R267 | T50 | forward |  |
| R268 | T50 | forward |  |
| R269 | T52 | forward | IR statement |
| R270 | T01 | forward | SAFE HARBOUR |
| R332 | T08 | hedge/policy (QUALIFIER) | HEDGE |
| R333 | T30 | hedge/policy (QUALIFIER) | HEDGE |
| R336 | T39 | hedge/policy (QUALIFIER) | HEDGE/NO_GUIDANCE |
| R310 | T41 | hedge/policy (QUALIFIER) | NO_GUIDANCE policy |
| R309 | T37 | hedge/policy (QUALIFIER) | DISCLOSURE policy |

## 6. Other categories (entities, dates, qualifiers)
ZERO_STANDING: none. ENTITY_CHANGE: not assessable (no prior SONACOMS ledger). DROPPED_SLIDE: n/a for concall.
Entities: 86 rows = 17 participants/aliases (section 1) + 9 turn boundaries (R200-R208) + 60 products, markets, customers, events, counterparties (section 7). Unnamed-customer entities R193-R196 reflect the customer confidentiality rule (R306,R307). R160 "Neo" is an end-customer name as heard, flagged ASR_NAME and CUSTOMER_NAME_RISK (R331 says public information; A3 to check).

## 7. Per-ID accountability map (all 336)
| ROW_ID | line | turn | category | A2 flags | cross-ref / materiality |
|---|---|---|---|---|---|
| R001 | L003 | T01 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R002 | L042 | T03 | mgmt_number |  |  |
| R003 | L040 | T03 | mgmt_number |  |  |
| R004 | L046 | T03 | mgmt_number | RESTATED | RESTATED R209 (10x over 10 yrs) |
| R005 | L060 | T03 | mgmt_number |  |  |
| R006 | L067 | T03 | mgmt_number | ASR | ASR (freight as "Prey trades") |
| R007 | L076 | T03 | mgmt_number | RESTATED | RESTATED R014,R047 (129% BEV/EV growth) |
| R008 | L111 | T03 | mgmt_number |  |  |
| R009 | L115 | T03 | mgmt_number |  | see R275 |
| R010 | L117 | T03 | mgmt_number |  |  |
| R011 | L122 | T03 | mgmt_number | RESTATED | RESTATED R043 (35% Q2 rev growth) |
| R012 | L123 | T03 | mgmt_number | RESTATED | RESTATED R049 (23% EBITDA growth; collides with 23% margin R051/R088); AMBIGUOUS: "23%" appears as EBITDA growth (R049) and as margin (R051); keep distinct |
| R013 | L124 | T03 | mgmt_number | RESTATED | RESTATED R053 (29% PAT growth) |
| R014 | L130 | T03 | mgmt_number | RESTATED | RESTATED R007,R047 |
| R015 | L131 | T03 | mgmt_number | RESTATED | RESTATED R048,R115 (BEV >half of auto revenue; 51%) |
| R016 | L134 | T03 | mgmt_number |  |  |
| R017 | L142 | T03 | mgmt_number | RESTATED | RESTATED R050 (356 cr Q2 EBITDA) |
| R018 | L151 | T03 | mgmt_number | RESTATED | RESTATED R057 (43% H1 rev) |
| R019 | L151 | T03 | mgmt_number | RESTATED,ASR | RESTATED R062 (34% H1 EBITDA); ASR ("India impact") |
| R020 | L151 | T03 | mgmt_number | RESTATED,ASR | RESTATED R066 (36% H1 PAT); ASR |
| R021 | L163 | T03 | mgmt_number | ASR,UNIT_AMBIGUOUS | ASR unit "10 billion"; RECONCILE A3: "10 billion" EV H1 revenue vs R060 2,042 cr BEV H1 revenue vs R058 2,857 cr total; units and basis differ |
| R022 | L165 | T03 | mgmt_number |  | see R023,R061 (EV share) |
| R023 | L166 | T03 | mgmt_number | RESTATED | RESTATED R061 (48%) |
| R024 | L167 | T03 | mgmt_number |  |  |
| R025 | L168 | T03 | mgmt_number |  |  |
| R026 | L168 | T03 | mgmt_number |  |  |
| R027 | L170 | T03 | mgmt_number |  |  |
| R028 | L170 | T03 | mgmt_number |  |  |
| R029 | L171 | T03 | mgmt_number |  |  |
| R030 | L172 | T03 | mgmt_number |  |  |
| R031 | L215 | T03 | mgmt_number | ASR,UNIT_AMBIGUOUS | see R313; unit as spoken "billion" |
| R032 | L219 | T03 | mgmt_number | RESTATED,ASR,UNIT_AMBIGUOUS | RESTATED R108 (251 billion); see R313; unit as spoken "billion" |
| R033 | L222 | T03 | mgmt_number | RESTATED | RESTATED R108 (4% robotics) |
| R034 | L231 | T03 | mgmt_number |  | historic look-east ref |
| R035 | L233 | T03 | mgmt_number |  | historic ref vs R034 |
| R036 | L236 | T03 | mgmt_number | RESTATED | RESTATED R282 |
| R037 | L241 | T03 | mgmt_number | RESTATED,ASR | RESTATED R082 (7%, analyst); ASR |
| R038 | L249 | T03 | mgmt_number |  |  |
| R039 | L258 | T03 | mgmt_number |  |  |
| R040 | L260 | T03 | mgmt_number |  | see R327 annualised |
| R041 | L275 | T03 | mgmt_number |  |  |
| R042 | L276 | T03 | mgmt_number |  | see R326 |
| R043 | L306 | T05 | mgmt_number | RESTATED | RESTATED R011 |
| R044 | L306 | T05 | mgmt_number |  |  |
| R045 | L307 | T05 | mgmt_number |  |  |
| R046 | L309 | T05 | mgmt_number |  |  |
| R047 | L310 | T05 | mgmt_number | RESTATED | RESTATED R007,R014 |
| R048 | L311 | T05 | mgmt_number | RESTATED | RESTATED R015,R115 |
| R049 | L313 | T05 | mgmt_number | RESTATED | RESTATED R012 |
| R050 | L313 | T05 | mgmt_number | RESTATED | RESTATED R017 |
| R051 | L314 | T05 | mgmt_number |  |  |
| R052 | L314 | T05 | mgmt_number |  | CHECK A3: "2.3%" margin delta vs 23% margin (R051); possible ASR merge |
| R053 | L320 | T05 | mgmt_number | RESTATED | RESTATED R013 |
| R054 | L320 | T05 | mgmt_number | ASR,ASR_TRUNCATED_FIGURE | ASR truncated: 23 crores vs 29% and 14.4% margin; A3 verify against press release |
| R055 | L321 | T05 | mgmt_number |  |  |
| R056 | L321 | T05 | mgmt_number |  | approx ("about half percent") |
| R057 | L327 | T05 | mgmt_number | RESTATED | RESTATED R018 |
| R058 | L327 | T05 | mgmt_number |  |  |
| R059 | L328 | T05 | mgmt_number | ASR | ASR ("BV") |
| R060 | L328 | T05 | mgmt_number |  | RECONCILE A3: vs R021 (10 billion) and R061/R023 (48% share); basis automotive product sales vs total |
| R061 | L329 | T05 | mgmt_number | RESTATED | RESTATED R023 |
| R062 | L330 | T05 | mgmt_number | RESTATED | RESTATED R019 |
| R063 | L330 | T05 | mgmt_number |  | see R050 (H1 vs Q2 EBITDA) |
| R064 | L331 | T05 | mgmt_number |  |  |
| R065 | L332 | T05 | mgmt_number |  | approx ("about one and a half percent") |
| R066 | L340 | T05 | mgmt_number | RESTATED | RESTATED R020 |
| R067 | L340 | T05 | mgmt_number |  |  |
| R068 | L341 | T05 | mgmt_number |  |  |
| R069 | L341 | T05 | mgmt_number |  |  |
| R070 | L350 | T05 | mgmt_number |  |  |
| R071 | L351 | T05 | mgmt_number |  | cash conversion 90% of EBITDA (CFO) |
| R072 | L352 | T05 | mgmt_number |  | WC release (CFO) |
| R073 | L354 | T05 | mgmt_number |  | capex H1 (CFO) |
| R074 | L354 | T05 | mgmt_number |  |  |
| R075 | L355 | T05 | mgmt_number |  |  |
| R076 | L356 | T05 | mgmt_number |  |  |
| R077 | L357 | T05 | mgmt_number |  |  |
| R078 | L358 | T05 | mgmt_number |  |  |
| R079 | L359 | T05 | mgmt_number |  |  |
| R080 | L361 | T05 | mgmt_number | RESTATED | RESTATED R095 (analyst reads 1,900) |
| R081 | L382 | T06 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R082 | L394 | T07 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R083 | L507 | T17 | mgmt_number | ASR | ASR ("differential years") |
| R084 | L508 | T17 | mgmt_number |  |  |
| R085 | L481 | T17 | mgmt_number | ASR | ASR ambiguity |
| R086 | L486 | T17 | mgmt_number |  | ex-China basis, see R328 |
| R087 | L600 | T28 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R088 | L604 | T28 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R089 | L607 | T28 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R090 | L611 | T29 | mgmt_number | RESTATED | RESTATED R091,R232,R234 (23-25% margin range) |
| R091 | L618 | T30 | mgmt_number | RESTATED | RESTATED R090,R232,R234 |
| R092 | L632 | T30 | mgmt_number |  | see R237 |
| R093 | L633 | T30 | mgmt_number |  | tolerance statement |
| R094 | L637 | T30 | mgmt_number |  | HYPOTHETICAL scenario (oil 150), not guidance |
| R095 | L642 | T31 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R096 | L644 | T32 | mgmt_number |  |  |
| R097 | L646 | T33 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R098 | L648 | T33 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R099 | L649 | T33 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R100 | L650 | T33 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R101 | L669 | T34 | mgmt_number | RESTATED | RESTATED R192 |
| R102 | L670 | T34 | mgmt_number |  | see R241 |
| R103 | L674 | T34 | mgmt_number |  | see R241 filter 1 |
| R104 | L678 | T34 | mgmt_number |  | see R241 filter 2 |
| R105 | L698 | T34 | mgmt_number | ASR | ASR ("cash to a better"); capital allocation threshold |
| R106 | L713 | T36 | analyst_or_moderator_number | NOT_MGMT_SPOKEN |  |
| R107 | L728 | T37 | mgmt_number |  |  |
| R108 | L745 | T37 | mgmt_number | RESTATED,ASR,UNIT_AMBIGUOUS | RESTATED R032,R033; unit differs ($250 billion vs R032 251 billion) |
| R109 | L763 | T37 | mgmt_number | RESTATED | RESTATED R248 (62 cr robotics capex) |
| R110 | L766 | T37 | mgmt_number | RESTATED | RESTATED R297 |
| R111 | L773 | T39 | mgmt_number |  | ANECDOTE (2016) |
| R112 | L773 | T39 | mgmt_number |  | ANECDOTE |
| R113 | L773 | T39 | mgmt_number |  | ANECDOTE |
| R114 | L774 | T39 | mgmt_number |  | see R115 (1% in 2019 to 51%); ANECDOTE |
| R115 | L775 | T39 | mgmt_number | RESTATED | RESTATED R015,R048 |
| R116 | L786 | T39 | mgmt_number |  | external compute-cost anecdote (CEO) |
| R117 | L813 | T41 | mgmt_number | RESTATED | RESTATED R300,R253 |
| R118 | L822 | T41 | mgmt_number | RESTATED | RESTATED R301,R258 |
| R119 | L831 | T43 | mgmt_number | RESTATED | RESTATED R259,R260 (25% CAGR) |
| R120 | L879 | T48 | mgmt_number |  | ILLUSTRATIVE (hypothetical), not a company figure |
| R121 | L880 | T48 | mgmt_number |  | ILLUSTRATIVE |
| R122 | L881 | T48 | mgmt_number |  | ILLUSTRATIVE |
| R123 | L003 | T01 | entity |  |  |
| R124 | L015 | T02 | participant |  |  |
| R125 | L016 | T02 | participant |  |  |
| R126 | L018 | T02 | participant |  |  |
| R127 | L019 | T02 | participant | ASR | ASR name |
| R128 | L020 | T02 | participant |  |  |
| R129 | L021 | T02 | participant |  |  |
| R130 | L022 | T02 | participant |  |  |
| R131 | L023 | T02 | participant |  |  |
| R132 | L024 | T02 | participant |  |  |
| R133 | L025 | T02 | participant | ASR | ASR name |
| R134 | L029 | T03 | participant | ASR | ASR name (CEO self-intro "Gopal") |
| R135 | L115 | T03 | entity |  |  |
| R136 | L115 | T03 | entity |  |  |
| R137 | L116 | T03 | entity | ASR | ASR name |
| R138 | L156 | T03 | entity |  |  |
| R139 | L176 | T03 | entity |  |  |
| R140 | L186 | T03 | entity |  |  |
| R141 | L193 | T03 | entity |  |  |
| R142 | L196 | T03 | entity |  |  |
| R143 | L203 | T03 | entity |  |  |
| R144 | L209 | T03 | entity |  |  |
| R145 | L210 | T03 | entity |  |  |
| R146 | L239 | T03 | entity |  |  |
| R147 | L242 | T03 | entity |  |  |
| R148 | L248 | T03 | entity |  |  |
| R149 | L256 | T03 | entity |  |  |
| R150 | L256 | T03 | entity |  |  |
| R151 | L230 | T03 | entity |  |  |
| R152 | L291 | T04 | entity |  |  |
| R153 | L292 | T04 | entity |  |  |
| R154 | L293 | T04 | entity |  |  |
| R155 | L296 | T04 | entity |  |  |
| R156 | L301 | T04 | entity |  |  |
| R157 | L379 | T06 | entity |  |  |
| R158 | L385 | T07 | participant |  |  |
| R159 | L401 | T08 | entity |  |  |
| R160 | L403 | T08 | entity | ASR,CUSTOMER_NAME_RISK | ASR name ("Neo") |
| R161 | L433 | T09 | entity | ASR | ASR spelling |
| R162 | L435 | T10 | entity |  |  |
| R163 | L443 | T11 | entity |  |  |
| R164 | L441 | T11 | participant |  |  |
| R165 | L456 | T15 | participant |  |  |
| R166 | L513 | T19 | participant |  |  |
| R167 | L598 | T27 | participant |  |  |
| R168 | L705 | T35 | participant | ASR | ASR name |
| R169 | L459 | T16 | entity |  |  |
| R170 | L498 | T17 | entity |  |  |
| R171 | L471 | T16 | entity |  |  |
| R172 | L711 | T36 | entity |  |  |
| R173 | L716 | T36 | entity |  |  |
| R174 | L734 | T37 | entity |  |  |
| R175 | L735 | T37 | entity |  |  |
| R176 | L736 | T37 | entity |  |  |
| R177 | L765 | T37 | entity |  |  |
| R178 | L806 | T40 | entity |  |  |
| R179 | L814 | T41 | entity |  |  |
| R180 | L816 | T41 | entity |  |  |
| R181 | L818 | T41 | entity |  |  |
| R182 | L832 | T43 | entity | ASR | ASR name |
| R183 | L842 | T44 | entity |  |  |
| R184 | L847 | T45 | entity |  |  |
| R185 | L653 | T33 | entity |  |  |
| R186 | L649 | T33 | entity |  |  |
| R187 | L647 | T33 | entity |  |  |
| R188 | L568 | T24 | entity |  |  |
| R189 | L064 | T03 | entity |  |  |
| R190 | L065 | T03 | entity |  |  |
| R191 | L046 | T03 | entity | ASR | ASR variants |
| R192 | L669 | T34 | entity |  |  |
| R193 | L188 | T03 | entity |  |  |
| R194 | L179 | T03 | entity |  |  |
| R195 | L194 | T03 | entity |  |  |
| R196 | L205 | T03 | entity |  |  |
| R197 | L367 | T05 | entity |  |  |
| R198 | L358 | T05 | entity |  |  |
| R199 | L535 | T20 | entity |  |  |
| R200 | L385 | T07 | turn_boundary |  |  |
| R201 | L456 | T15 | turn_boundary |  |  |
| R202 | L513 | T19 | turn_boundary |  |  |
| R203 | L598 | T27 | turn_boundary |  |  |
| R204 | L705 | T35 | turn_boundary |  |  |
| R205 | L839 | T44 | turn_boundary |  |  |
| R206 | L050 | T03 | turn_boundary |  |  |
| R207 | L281 | T04 | turn_boundary |  |  |
| R208 | L303 | T05 | turn_boundary |  |  |
| R209 | L046 | T03 | forward_commitment |  |  |
| R210 | L048 | T03 | forward_commitment |  |  |
| R211 | L069 | T03 | forward_commitment | HEDGE |  |
| R212 | L070 | T03 | forward_commitment | HEDGE |  |
| R213 | L071 | T03 | forward_commitment |  |  |
| R214 | L152 | T03 | forward_commitment |  |  |
| R215 | L155 | T03 | forward_commitment |  |  |
| R216 | L221 | T03 | forward_commitment |  |  |
| R217 | L223 | T03 | forward_commitment |  |  |
| R218 | L267 | T03 | forward_commitment |  |  |
| R219 | L367 | T05 | forward_commitment |  |  |
| R220 | L417 | T08 | forward_commitment |  |  |
| R221 | L419 | T08 | forward_commitment |  |  |
| R222 | L422 | T08 | forward_commitment | HEDGE |  |
| R223 | L435 | T10 | forward_commitment |  |  |
| R224 | L439 | T10 | forward_commitment |  |  |
| R225 | L440 | T10 | forward_commitment | HEDGE |  |
| R226 | L444 | T11 | forward_commitment |  |  |
| R227 | L498 | T17 | forward_commitment |  |  |
| R228 | L506 | T17 | forward_commitment |  |  |
| R229 | L554 | T22 | forward_commitment | HEDGE |  |
| R230 | L561 | T24 | forward_commitment |  |  |
| R231 | L566 | T24 | forward_commitment |  |  |
| R232 | L610 | T29 | forward_commitment |  |  |
| R233 | L615 | T29 | forward_commitment |  |  |
| R234 | L618 | T30 | forward_commitment |  |  |
| R235 | L624 | T30 | forward_commitment | HEDGE |  |
| R236 | L626 | T30 | forward_commitment | HEDGE |  |
| R237 | L632 | T30 | forward_commitment | HEDGE | see R092 |
| R238 | L637 | T30 | forward_commitment | HEDGE |  |
| R239 | L661 | T34 | forward_commitment |  |  |
| R240 | L665 | T34 | forward_commitment |  |  |
| R241 | L670 | T34 | forward_commitment |  |  |
| R242 | L689 | T34 | forward_commitment |  |  |
| R243 | L698 | T34 | forward_commitment |  |  |
| R244 | L728 | T37 | forward_commitment |  |  |
| R245 | L744 | T37 | forward_commitment |  |  |
| R246 | L748 | T37 | forward_commitment | HEDGE |  |
| R247 | L761 | T37 | forward_commitment |  |  |
| R248 | L763 | T37 | forward_commitment |  |  |
| R249 | L765 | T37 | forward_commitment |  |  |
| R250 | L778 | T39 | forward_commitment | HEDGE |  |
| R251 | L779 | T39 | forward_commitment |  |  |
| R252 | L793 | T39 | forward_commitment |  |  |
| R253 | L812 | T41 | forward_commitment |  |  |
| R254 | L815 | T41 | forward_commitment |  |  |
| R255 | L816 | T41 | forward_commitment |  |  |
| R256 | L818 | T41 | forward_commitment |  |  |
| R257 | L820 | T41 | forward_commitment |  |  |
| R258 | L822 | T41 | forward_commitment |  |  |
| R259 | L830 | T43 | forward_commitment |  |  |
| R260 | L836 | T43 | forward_commitment |  |  |
| R261 | L847 | T45 | forward_commitment |  |  |
| R262 | L849 | T45 | forward_commitment | HEDGE |  |
| R263 | L861 | T48 | forward_commitment |  |  |
| R264 | L875 | T48 | forward_commitment |  |  |
| R265 | L878 | T48 | forward_commitment |  |  |
| R266 | L886 | T50 | forward_commitment |  |  |
| R267 | L893 | T50 | forward_commitment |  |  |
| R268 | L898 | T50 | forward_commitment |  |  |
| R269 | L909 | T52 | forward_commitment |  |  |
| R270 | L008 | T01 | forward_commitment |  |  |
| R271 | L003 | T01 | date |  |  |
| R272 | L046 | T03 | date |  |  |
| R273 | L110 | T03 | date |  |  |
| R274 | L112 | T03 | date |  |  |
| R275 | L115 | T03 | date |  |  |
| R276 | L117 | T03 | date |  |  |
| R277 | L150 | T03 | date |  |  |
| R278 | L163 | T03 | date |  |  |
| R279 | L165 | T03 | date |  |  |
| R280 | L169 | T03 | date |  |  |
| R281 | L231 | T03 | date |  |  |
| R282 | L236 | T03 | date |  |  |
| R283 | L305 | T05 | date |  |  |
| R284 | L307 | T05 | date |  |  |
| R285 | L315 | T05 | date |  |  |
| R286 | L333 | T05 | date |  |  |
| R287 | L355 | T05 | date |  |  |
| R288 | L360 | T05 | date |  |  |
| R289 | L439 | T10 | date |  |  |
| R290 | L440 | T10 | date |  |  |
| R291 | L445 | T11 | date |  |  |
| R292 | L580 | T25 | date |  |  |
| R293 | L648 | T33 | date |  |  |
| R294 | L649 | T33 | date |  |  |
| R295 | L669 | T34 | date |  |  |
| R296 | L674 | T34 | date |  |  |
| R297 | L766 | T37 | date |  |  |
| R298 | L773 | T39 | date |  |  |
| R299 | L774 | T39 | date |  |  |
| R300 | L813 | T41 | date |  |  |
| R301 | L822 | T41 | date |  |  |
| R302 | L045 | T03 | date |  |  |
| R303 | L229 | T03 | date |  |  |
| R304 | L001 | T01 | qualifier |  |  |
| R305 | L008 | T01 | qualifier |  |  |
| R306 | L011 | T01 | qualifier |  |  |
| R307 | L014 | T01 | qualifier |  |  |
| R308 | L382 | T06 | qualifier |  |  |
| R309 | L727 | T37 | qualifier | POLICY |  |
| R310 | L809 | T41 | qualifier | POLICY |  |
| R311 | L306 | T05 | qualifier |  |  |
| R312 | L320 | T05 | qualifier | ASR,ASR_TRUNCATED_FIGURE | ASR flag |
| R313 | L215 | T03 | qualifier | ASR,UNIT_AMBIGUOUS | unit flag |
| R314 | L644 | T32 | qualifier |  | metric definition/basis |
| R315 | L361 | T05 | qualifier |  | metric definition/basis |
| R316 | L351 | T05 | qualifier |  | metric definition/basis |
| R317 | L354 | T05 | qualifier |  | metric definition/basis |
| R318 | L363 | T05 | qualifier |  |  |
| R319 | L365 | T05 | qualifier |  |  |
| R320 | L367 | T05 | qualifier |  | metric definition/basis |
| R321 | L316 | T05 | qualifier |  | metric definition/basis |
| R322 | L323 | T05 | qualifier |  | metric definition/basis |
| R323 | L343 | T05 | qualifier |  | metric definition/basis |
| R324 | L311 | T05 | qualifier |  | metric definition/basis |
| R325 | L248 | T03 | qualifier |  | metric definition/basis |
| R326 | L276 | T03 | qualifier |  | metric definition/basis |
| R327 | L260 | T03 | qualifier |  | metric definition/basis |
| R328 | L485 | T17 | qualifier |  | metric definition/basis |
| R329 | L507 | T17 | qualifier | ASR | ASR ambiguity; metric definition/basis |
| R330 | L646 | T33 | qualifier |  | metric definition/basis |
| R331 | L403 | T08 | qualifier |  |  |
| R332 | L427 | T08 | qualifier | HEDGE |  |
| R333 | L633 | T30 | qualifier | HEDGE |  |
| R334 | L866 | T48 | qualifier |  |  |
| R335 | L889 | T50 | qualifier |  |  |
| R336 | L777 | T39 | qualifier | HEDGE |  |

## 8. MISSING_FROM_STRUCTURED (A1 loop-back; the only rows that carry claim text)
| ID | line | turn | flag | unit |
|---|---|---|---|---|
| M01 | L092 | T03 | MISSING_FROM_STRUCTURED | "ended Q2 with the second highest order book in our history" (order-book rank, CEO) |
| M02 | L101 | T03 | MISSING_FROM_STRUCTURED | "most companies would count themselves fortunate if they have three new products in three years" (rarity framing for 3 new products, R003) |
| M03 | L144 | T03 | MISSING_FROM_STRUCTURED | CEO: Q2 EBITDA 356 cr was roughly the whole-year revenue when he joined the company (L143-L144) |
| M04 | L149 | T03 | MISSING_FROM_STRUCTURED | CEO: at IPO, roughly the annual revenue was what the company now does in a quarter (L149-L150) |
| M05 | L243 | T03 | MISSING_FROM_STRUCTURED | "suspension motors already equal to that [railway brake system] for the first half" (H1 scale comparison, ties R037/R147) |
| M06 | L558 | T24 | MISSING_FROM_STRUCTURED | Sat: three-wheeler traction business "pretty small so far" (answer to Gunjan follow-up, qualifies R231) |
| M07 | L577 | T25 | MISSING_FROM_STRUCTURED | CEO: "all three of our large customers" in EV differential assemblies picked up this quarter (breadth, customer count 3) |
| M08 | L136 | T03 | MISSING_FROM_STRUCTURED | CEO: US EV market deliveries broadly unchanged while BEV revenue grew (diversification claim, L135-L136; ties R199) |
| M09 | L217 | T03 | MISSING_FROM_STRUCTURED | CEO: Q2 order additions not anchored on one very large order, spread across several (L216-L218) |

Sweep method: fulltext lines carrying digits or number words and not cited by any structured row were reviewed by hand; continuation lines of cited rows excluded. All 9 gaps are comparative, rank or breadth statements; none changes a headline figure.

## 9. Cross-row items for A3/A4 (enumeration, not interpretation)
- Unit and basis tangle: R021 ("10 billion" EV H1), R060 (2,042 cr BEV H1), R023/R061 (48% on two bases), R324. Filing baseline needed.
- R054 PAT "23 crores" ASR-truncated; R312 flags it; use press release.
- R052 "2.3%" EBITDA margin delta vs R051 23%: possible ASR merge.
- R031/R032/R108 order wins and order book in "billion" as spoken; no crore equivalent given in the transcript.
- Margin: R232/R234 hold 23-25% range, R092 "around 23% ballpark", R090 reaffirmed; R213 absolute margins improve at high clip; R212 predictability hedge.
- Customer confidentiality rule (R306,R307,R309): R160 end-customer "Neo" named by CEO as public information (R331).
- M06 3W traction "pretty small so far" vs R231 "share should kick in".

```yaml
stage: A2-enumerator
company: "SONACOMS"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/ledger_concall_sonacoms_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 86
  turns: 53
  questions: 18
  mgmt_numbers: 110
  slides: 0
  slide_numbers: 0
flags_raised: [RESTATED, ASR, UNIT_AMBIGUOUS, ASR_TRUNCATED_FIGURE, HEDGE, REPEAT_QUESTION, CUSTOMER_NAME_RISK, MISSING_FROM_STRUCTURED, NOT_MGMT_SPOKEN]
ids_in_structured: 336
ids_referenced: 336
orphan_ids: []
missing_from_structured: [M01 L092 second highest order book, M02 L101 three new products in three years, M03 L144 EBITDA vs revenue at CEO joining, M04 L149 IPO annual revenue vs quarterly now, M05 L243 suspension motors equal railway brake H1, M06 L558 3W traction pretty small, M07 L577 all three large EV diff customers picked up, M08 L136 US EV deliveries unchanged, M09 L217 order additions not one large order]
gate_a2: pass
mismatch_note: ""
analyst_note: "Turns are 53 inferred (source has no speaker labels); 9 are moderator-anchored rows R200-R208. 18 asks, 6 questioner groups; Ramod Kumar shows up to 4 asks (ambiguous speaker at L801), over the two-question rule R308. Robotics asked 5 ways (Q05,Q12,Q13,Q14,Q18) and margin twice (Q09,Q17). mgmt_numbers 110 excludes 12 analyst or moderator numbers. A3 should reconcile against the press release: R021 10 billion EV H1 vs R060 2,042 cr BEV vs R023/R061 48% (differing bases); R054 PAT 23 cr is ASR-truncated; R052 2.3% margin delta possible ASR merge; order wins and order book as spoken in billion (R031,R032,R108). R160 names an end customer despite the call rule. No ZERO_STANDING or ENTITY_CHANGE (no prior ledger). Analyst firms NOT FOUND."
```
