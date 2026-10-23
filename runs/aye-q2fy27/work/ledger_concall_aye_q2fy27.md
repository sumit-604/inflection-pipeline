# A2 LEDGER - Aye Finance (AYE) Q2 FY27 concall (ASR machine transcript)
Source: A1 structured extraction only (fulltext used for count-test sweep). "line" = fulltext line; turn mapping is best effort (ASR does not separate speakers).

ids_in_structured: 346 | ids_referenced_in_ledger: 346 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: ids_by_type        grep_count: 346 (NUMBER 191, ENTITY 48, FORWARD 56, DATE 26, QUALIFIER 25)   sweep_count: 346 (191/48/56/26/25)   match: yes
category: participants       grep_count: 16 (mgmt/host R197-R203 = 7; analysts R212-R220 = 9)   sweep_count: 16 + 1 unidentified analyst (Q2, no row)   match: yes
category: speaker_turns      grep_count: 11 [MODERATOR TURN] tags (10 hand-overs + 1 mid-question ASR artefact at fulltext line 525)   sweep_count: 26 turns (T1-T26; 10 Q&A exchanges x2 + 6 framing turns)   match: yes (10 = 11 - 1 artefact)
category: questions          grep_count: 10   sweep_count: 10   match: yes
category: mgmt_numbers       grep_count: 191 NUMBER rows   sweep_count: 191   match: yes
category: forward_hedge      grep_count: 56 FORWARD + 25 QUALIFIER   sweep_count: 56 + 25   match: yes
fulltext number-line sweep: 164 number-bearing lines (timestamps stripped) after line 27; 149 within +/-1 line of a structured row; 15 uncovered, of which 7 listed as MISSING_FROM_STRUCTURED (section 9) and 8 restate covered rows or are low-value ASR noise
gate_a2: pass
=== END COUNT TEST ===

### 1. Participants (both sides)

| ROW ID | category | A2 flags | note |
|---|---|---|---|
| R197 | participant-mgmt/host | | host, IIFL Capital |
| R198 | participant-mgmt/host | | operator Renju (ASR) |
| R199 | participant-mgmt/host | | MD and co-founder (principal speaker) |
| R200 | participant-mgmt/host | | Deputy CEO |
| R201 | participant-mgmt/host | | management, designation not stated |
| R202 | participant-mgmt/host | | Strategy and IR Officer (ASR name) |
| R203 | participant-mgmt/host | | IR advisor SGA |
| R212 | participant-analyst | ASR_UNCERTAIN | ampersand capital [ASR_UNCERTAIN] |
| R213 | participant-analyst | ASR_UNCERTAIN | Urban Kumar, Evil Voice Public Alternates [ASR_UNCERTAIN] |
| R214 | participant-analyst | ASR_UNCERTAIN | Winning Akarwal, Bajaj Altnetz [ASR_UNCERTAIN] |
| R215 | participant-analyst |  | Viralsha, ISL capital |
| R216 | participant-analyst |  | Rudraksha Pahija, I-Thought Financial Consulting |
| R217 | participant-analyst |  | Rahul Kumar, Vaikarya fund |
| R218 | participant-analyst | ASR_UNCERTAIN | Samir Bisse, time in Asia [ASR_UNCERTAIN] |
| R219 | participant-analyst | ASR_UNCERTAIN | Aditya McClary, Berman Capital [ASR_UNCERTAIN] |
| R220 | participant-analyst |  | Varun Tube, Share India Securities |
| (none) | participant-analyst Q2 | ANALYST_UNIDENTIFIED | no row; moderator line truncated at fulltext line 282. MD/co-founder present, so no MGMT_ABSENCE |

### 2. Speaker turns (best effort; speaker split not machine-detectable)

| turn | speaker | fulltext lines | structured row IDs in turn | A2 flags |
|---|---|---|---|---|
| T1 | Moderator (Renju) opening | 27-32 | R197..R197 (1) |  |
| T2 | Viral Shah (IIFL Capital) intro | 33-37 | R198..R306 (2) |  |
| T3 | MD Sanjay Sharma opening remarks; later presenters not separable | 38-233 | R002..R346 (149) | MULTI_SPEAKER_MERGED |
| T4 | Moderator Q&A instructions | 234-244 | none |  |
| T5 | Analyst Q1 (ampersand capital (name not captured)) question | 245 (answer start not separable) | part of E1 range | |
| T6 | Management answer to Q1 | E1 range 245-280 | R096..R341 (20) | |
| T7 | Analyst Q2 (unidentified (moderator line truncated at "line of a")) question | 281 (answer start not separable) | part of E2 range | |
| T8 | Management answer to Q2 | E2 range 281-383 | R107..R316 (22) | |
| T9 | Analyst Q3 (Urban Kumar) question | 384 (answer start not separable) | part of E3 range | |
| T10 | Management answer to Q3 | E3 range 384-448 | R120..R334 (21) | |
| T11 | Analyst Q4 (Winning Akarwal) question | 449 (answer start not separable) | part of E4 range | |
| T12 | Management answer to Q4 | E4 range 449-517 | R134..R337 (19) | |
| T13 | Analyst Q5 (Viral(sha)) question | 518 (answer start not separable) | part of E5 range | |
| T14 | Management answer to Q5 | E5 range 518-615 | R144..R284 (26) | |
| T15 | Analyst Q6 (Rudraksha Pahija) question | 616 (answer start not separable) | part of E6 range | |
| T16 | Management answer to Q6 | E6 range 616-663 | R159..R287 (12) | |
| T17 | Analyst Q7 (Rahul Kumar) question | 664 (answer start not separable) | part of E7 range | |
| T18 | Management answer to Q7 | E7 range 664-683 | R164..R217 (3) | |
| T19 | Analyst Q8 (Samir Bisse) question | 684 (answer start not separable) | part of E8 range | |
| T20 | Management answer to Q8 | E8 range 684-738 | R166..R338 (18) | |
| T21 | Analyst Q9 (Aditya McClary) question | 739 (answer start not separable) | part of E9 range | |
| T22 | Management answer to Q9 | E9 range 739-804 | R176..R344 (27) | |
| T23 | Analyst Q10 (Varun Tube) question | 805 (answer start not separable) | part of E10 range | |
| T24 | Management answer to Q10 | E10 range 805-854 | R190..R345 (7) | |
| T25 | Management closing remarks | 855-862 | R321..R321 (1) | |
| T26 | Moderator close | 863-864 | none | |

Q&A share: T5-T24 = 20 of 26 turns; Q&A lines 245-854 = 610 lines of about 838 spoken lines (about 73%); opening remarks lines 38-233 about 196 lines.

### 3. Questions ledger

| Q# | turn | analyst ROW ID | analyst / firm | topic | flags |
|---|---|---|---|---|---|
| Q1 | T5 | R212 | ampersand capital (name not captured) | AUM upper end of guide, credit cost, capital/dilution |  |
| Q2 | T7 | NONE | unidentified (moderator line truncated at "line of a") | asset quality under lender stress; cattle portfolio behaviour; manpower/productivity answers | ANALYST_UNIDENTIFIED |
| Q3 | T9 | R213 | Urban Kumar, Evil Voice Public Alternates (ASR) | ECL provision Q1 vs now (stage 2 39 cr, stage 3 194 cr as asked), monthly disclosures, credit quality, festive disbursals |  |
| Q4 | T11 | R214 | Winning Akarwal, Bajaj Altnetz (ASR) | share of customers with MFI loans, lender count, exposure; collections |  |
| Q5 | T13 | R215 | Viral(sha), ISL capital (ASR) | insurance commission mitigation %, opex, credit cost, rate, gold loan |  |
| Q6 | T15 | R216 | Rudraksha Pahija, I-Thought Financial Consulting | state/regional caution; drought; PAR X; mortgage/microlap |  |
| Q7 | T17 | R217 | Rahul Kumar, Vaikarya fund | portfolio behaviour in past rural/drought shocks |  |
| Q8 | T19 | R218 | Samir Bisse, time in Asia (ASR) | asset-side rate action, ROA vs rates, NIM, sensitivity |  |
| Q9 | T21 | R219 | Aditya McClary, Berman Capital (ASR) | fixed vs floating mix, foreclosure rates (mortgage), branch count flat / expansion timeline |  |
| Q10 | T23 | R220 | Varun Tube, Share India Securities | collections/condition (garbled), insurance/CGS cover |  |

REPEAT_QUESTION: none verifiable from the structured file alone. Topic overlaps for A3: insurance commission (opening R255 and Q5), gold loans (opening R258 and Q5), drought (Q6 and Q7), branch expansion (Q9 and Q10 tail).

### 4. Management numbers (all NUMBER rows) with turn

| ROW ID | category | A2 flags | turn | cross-ref / note |
|---|---|---|---|---|
| R001 | mgmt_number |  | T0-header | non-management metadata |
| R002 | mgmt_number |  | T3 |  |
| R003 | mgmt_number |  | T3 | RESTATED w/ R346 |
| R004 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R005 | mgmt_number |  | T3 | RESTATED w/ R014 |
| R006 | mgmt_number |  | T3 | RESTATED w/ R049 |
| R007 | mgmt_number |  | T3 |  |
| R008 | mgmt_number |  | T3 | RESTATED w/ R036 |
| R009 | mgmt_number |  | T3 | RESTATED w/ R038 |
| R010 | mgmt_number |  | T3 |  |
| R011 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R012 | mgmt_number |  | T3 | RESTATED w/ R346 |
| R013 | mgmt_number |  | T3 |  |
| R014 | mgmt_number |  | T3 | RESTATED w/ R005 |
| R015 | mgmt_number |  | T3 |  |
| R016 | mgmt_number |  | T3 | RESTATED w/ R243 |
| R017 | mgmt_number |  | T3 |  |
| R018 | mgmt_number |  | T3 |  |
| R019 | mgmt_number |  | T3 |  |
| R020 | mgmt_number |  | T3 | RESTATED w/ R021 |
| R021 | mgmt_number |  | T3 | RESTATED w/ R020 |
| R022 | mgmt_number |  | T3 |  |
| R023 | mgmt_number |  | T3 |  |
| R024 | mgmt_number |  | T3 |  |
| R025 | mgmt_number |  | T3 |  |
| R026 | mgmt_number |  | T3 | RESTATED w/ R308 |
| R027 | mgmt_number |  | T3 |  |
| R028 | mgmt_number |  | T3 | RESTATED w/ R309 |
| R029 | mgmt_number |  | T3 |  |
| R030 | mgmt_number |  | T3 | RESTATED w/ R246 |
| R031 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R032 | mgmt_number |  | T3 |  |
| R033 | mgmt_number |  | T3 |  |
| R034 | mgmt_number |  | T3 |  |
| R035 | mgmt_number |  | T3 |  |
| R036 | mgmt_number |  | T3 | RESTATED w/ R008 |
| R037 | mgmt_number |  | T3 |  |
| R038 | mgmt_number |  | T3 | RESTATED w/ R009 |
| R039 | mgmt_number |  | T3 |  |
| R040 | mgmt_number |  | T3 |  |
| R041 | mgmt_number |  | T3 |  |
| R042 | mgmt_number |  | T3 |  |
| R043 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R044 | mgmt_number |  | T3 |  |
| R045 | mgmt_number |  | T3 |  |
| R046 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R047 | mgmt_number |  | T3 | RESTATED w/ R249 |
| R048 | mgmt_number |  | T3 | RESTATED w/ R304 |
| R049 | mgmt_number |  | T3 | RESTATED w/ R006 |
| R050 | mgmt_number |  | T3 |  |
| R051 | mgmt_number |  | T3 |  |
| R052 | mgmt_number |  | T3 |  |
| R053 | mgmt_number |  | T3 |  |
| R054 | mgmt_number |  | T3 |  |
| R055 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R056 | mgmt_number |  | T3 |  |
| R057 | mgmt_number |  | T3 |  |
| R058 | mgmt_number |  | T3 |  |
| R059 | mgmt_number |  | T3 |  |
| R060 | mgmt_number |  | T3 |  |
| R061 | mgmt_number |  | T3 |  |
| R062 | mgmt_number |  | T3 |  |
| R063 | mgmt_number |  | T3 |  |
| R064 | mgmt_number |  | T3 |  |
| R065 | mgmt_number |  | T3 |  |
| R066 | mgmt_number |  | T3 |  |
| R067 | mgmt_number |  | T3 |  |
| R068 | mgmt_number |  | T3 |  |
| R069 | mgmt_number | ASR_UNCERTAIN | T3 |  |
| R070 | mgmt_number |  | T3 |  |
| R071 | mgmt_number |  | T3 |  |
| R072 | mgmt_number |  | T3 |  |
| R073 | mgmt_number |  | T3 |  |
| R074 | mgmt_number |  | T3 |  |
| R075 | mgmt_number |  | T3 |  |
| R076 | mgmt_number |  | T3 |  |
| R077 | mgmt_number |  | T3 |  |
| R078 | mgmt_number |  | T3 |  |
| R079 | mgmt_number |  | T3 |  |
| R080 | mgmt_number |  | T3 |  |
| R081 | mgmt_number |  | T3 |  |
| R082 | mgmt_number |  | T3 |  |
| R083 | mgmt_number |  | T3 |  |
| R084 | mgmt_number |  | T3 |  |
| R085 | mgmt_number |  | T3 |  |
| R086 | mgmt_number |  | T3 |  |
| R087 | mgmt_number |  | T3 |  |
| R088 | mgmt_number |  | T3 |  |
| R089 | mgmt_number |  | T3 |  |
| R090 | mgmt_number |  | T3 |  |
| R091 | mgmt_number |  | T3 |  |
| R092 | mgmt_number |  | T3 |  |
| R093 | mgmt_number |  | T3 |  |
| R094 | mgmt_number |  | T3 |  |
| R095 | mgmt_number |  | T3 |  |
| R096 | mgmt_number |  | E1:T5/T6 |  |
| R097 | mgmt_number |  | E1:T5/T6 |  |
| R098 | mgmt_number | ASR_UNCERTAIN | E1:T5/T6 |  |
| R099 | mgmt_number |  | E1:T5/T6 |  |
| R100 | mgmt_number |  | E1:T5/T6 |  |
| R101 | mgmt_number |  | E1:T5/T6 |  |
| R102 | mgmt_number |  | E1:T5/T6 |  |
| R103 | mgmt_number | ASR_UNCERTAIN | E1:T5/T6 |  |
| R104 | mgmt_number |  | E1:T5/T6 |  |
| R105 | mgmt_number | ASR_UNCERTAIN | E1:T5/T6 |  |
| R106 | mgmt_number |  | E1:T5/T6 |  |
| R107 | mgmt_number |  | E2:T7/T8 |  |
| R108 | mgmt_number |  | E2:T7/T8 |  |
| R109 | mgmt_number |  | E2:T7/T8 |  |
| R110 | mgmt_number |  | E2:T7/T8 |  |
| R111 | mgmt_number |  | E2:T7/T8 |  |
| R112 | mgmt_number | ASR_UNCERTAIN | E2:T7/T8 |  |
| R113 | mgmt_number |  | E2:T7/T8 |  |
| R114 | mgmt_number |  | E2:T7/T8 |  |
| R115 | mgmt_number |  | E2:T7/T8 |  |
| R116 | mgmt_number |  | E2:T7/T8 |  |
| R117 | mgmt_number |  | E2:T7/T8 |  |
| R118 | mgmt_number |  | E2:T7/T8 |  |
| R119 | mgmt_number |  | E2:T7/T8 |  |
| R120 | mgmt_number |  | E3:T9/T10 |  |
| R121 | mgmt_number |  | E3:T9/T10 |  |
| R122 | mgmt_number |  | E3:T9/T10 |  |
| R123 | mgmt_number |  | E3:T9/T10 |  |
| R124 | mgmt_number |  | E3:T9/T10 |  |
| R125 | mgmt_number | ASR_UNCERTAIN | E3:T9/T10 |  |
| R126 | mgmt_number |  | E3:T9/T10 |  |
| R127 | mgmt_number |  | E3:T9/T10 |  |
| R128 | mgmt_number |  | E3:T9/T10 |  |
| R129 | mgmt_number |  | E3:T9/T10 |  |
| R130 | mgmt_number | ASR_UNCERTAIN | E3:T9/T10 |  |
| R131 | mgmt_number |  | E3:T9/T10 |  |
| R132 | mgmt_number |  | E3:T9/T10 |  |
| R133 | mgmt_number |  | E3:T9/T10 |  |
| R134 | mgmt_number |  | E4:T11/T12 |  |
| R135 | mgmt_number |  | E4:T11/T12 |  |
| R136 | mgmt_number |  | E4:T11/T12 |  |
| R137 | mgmt_number |  | E4:T11/T12 |  |
| R138 | mgmt_number |  | E4:T11/T12 |  |
| R139 | mgmt_number |  | E4:T11/T12 |  |
| R140 | mgmt_number |  | E4:T11/T12 |  |
| R141 | mgmt_number |  | E4:T11/T12 |  |
| R142 | mgmt_number |  | E4:T11/T12 |  |
| R143 | mgmt_number |  | E4:T11/T12 |  |
| R144 | mgmt_number |  | E5:T13/T14 |  |
| R145 | mgmt_number |  | E5:T13/T14 |  |
| R146 | mgmt_number |  | E5:T13/T14 |  |
| R147 | mgmt_number |  | E5:T13/T14 |  |
| R148 | mgmt_number |  | E5:T13/T14 |  |
| R149 | mgmt_number | ASR_UNCERTAIN | E5:T13/T14 |  |
| R150 | mgmt_number |  | E5:T13/T14 |  |
| R151 | mgmt_number |  | E5:T13/T14 |  |
| R152 | mgmt_number |  | E5:T13/T14 |  |
| R153 | mgmt_number |  | E5:T13/T14 |  |
| R154 | mgmt_number |  | E5:T13/T14 |  |
| R155 | mgmt_number |  | E5:T13/T14 |  |
| R156 | mgmt_number |  | E5:T13/T14 |  |
| R157 | mgmt_number |  | E5:T13/T14 |  |
| R158 | mgmt_number |  | E5:T13/T14 |  |
| R159 | mgmt_number |  | E6:T15/T16 |  |
| R160 | mgmt_number |  | E6:T15/T16 |  |
| R161 | mgmt_number |  | E6:T15/T16 |  |
| R162 | mgmt_number |  | E6:T15/T16 |  |
| R163 | mgmt_number |  | E6:T15/T16 |  |
| R164 | mgmt_number |  | E7:T17/T18 |  |
| R165 | mgmt_number |  | E7:T17/T18 |  |
| R166 | mgmt_number |  | E8:T19/T20 |  |
| R167 | mgmt_number |  | E8:T19/T20 |  |
| R168 | mgmt_number |  | E8:T19/T20 |  |
| R169 | mgmt_number |  | E8:T19/T20 |  |
| R170 | mgmt_number |  | E8:T19/T20 |  |
| R171 | mgmt_number |  | E8:T19/T20 |  |
| R172 | mgmt_number | ASR_UNCERTAIN | E8:T19/T20 |  |
| R173 | mgmt_number |  | E8:T19/T20 |  |
| R174 | mgmt_number | ASR_UNCERTAIN | E8:T19/T20 |  |
| R175 | mgmt_number |  | E8:T19/T20 |  |
| R176 | mgmt_number |  | E9:T21/T22 |  |
| R177 | mgmt_number |  | E9:T21/T22 |  |
| R178 | mgmt_number |  | E9:T21/T22 |  |
| R179 | mgmt_number |  | E9:T21/T22 |  |
| R180 | mgmt_number |  | E9:T21/T22 | RESTATED w/ R292,R293 |
| R181 | mgmt_number |  | E9:T21/T22 |  |
| R182 | mgmt_number |  | E9:T21/T22 |  |
| R183 | mgmt_number |  | E9:T21/T22 |  |
| R184 | mgmt_number |  | E9:T21/T22 |  |
| R185 | mgmt_number |  | E9:T21/T22 |  |
| R186 | mgmt_number |  | E9:T21/T22 |  |
| R187 | mgmt_number | ASR_UNCERTAIN | E9:T21/T22 |  |
| R188 | mgmt_number |  | E9:T21/T22 |  |
| R189 | mgmt_number |  | E9:T21/T22 |  |
| R190 | mgmt_number |  | E10:T23/T24 |  |
| R191 | mgmt_number | ASR_UNCERTAIN | E10:T23/T24 |  |

### 5. Forward commitments and hedges (FORWARD)

| ROW ID | category | A2 flags | turn | cross-ref / note |
|---|---|---|---|---|
| R240 | forward_commitment | | T3 |  |
| R241 | forward_commitment | | T3 |  |
| R242 | forward_commitment | | T3 |  |
| R243 | forward_commitment | | T3 | RESTATED w/ R016 |
| R244 | forward_commitment | | T3 |  |
| R245 | forward_commitment | | T3 |  |
| R246 | forward_commitment | | T3 | RESTATED w/ R030,R315 |
| R247 | forward_commitment | | T3 |  |
| R248 | forward_commitment | | T3 |  |
| R249 | forward_commitment | | T3 | RESTATED w/ R047,R285 |
| R250 | forward_commitment | | T3 |  |
| R251 | forward_commitment | | T3 |  |
| R252 | forward_commitment | | T3 |  |
| R253 | forward_commitment | | T3 | RESTATED w/ R290 |
| R254 | forward_commitment | | T3 |  |
| R255 | forward_commitment | | T3 |  |
| R256 | forward_commitment | | T3 |  |
| R257 | forward_commitment | | T3 | RESTATED w/ R307 |
| R258 | forward_commitment | | T3 |  |
| R259 | forward_commitment | | T3 |  |
| R260 | forward_commitment | | E1:T5/T6 |  |
| R261 | forward_commitment | | E1:T5/T6 |  |
| R262 | forward_commitment | | E1:T5/T6 |  |
| R263 | forward_commitment | | E1:T5/T6 |  |
| R264 | forward_commitment | | E1:T5/T6 |  |
| R265 | forward_commitment | | E1:T5/T6 |  |
| R266 | forward_commitment | | E2:T7/T8 |  |
| R267 | forward_commitment | | E2:T7/T8 |  |
| R268 | forward_commitment | | E2:T7/T8 |  |
| R269 | forward_commitment | | E2:T7/T8 |  |
| R270 | forward_commitment | | E2:T7/T8 |  |
| R271 | forward_commitment | | E2:T7/T8 |  |
| R272 | forward_commitment | | E2:T7/T8 |  |
| R273 | forward_commitment | | E3:T9/T10 |  |
| R274 | forward_commitment | | E3:T9/T10 |  |
| R275 | forward_commitment | | E5:T13/T14 |  |
| R276 | forward_commitment | | E5:T13/T14 |  |
| R277 | forward_commitment | | E5:T13/T14 |  |
| R278 | forward_commitment | | E5:T13/T14 |  |
| R279 | forward_commitment | | E5:T13/T14 |  |
| R280 | forward_commitment | | E5:T13/T14 |  |
| R281 | forward_commitment | | E5:T13/T14 |  |
| R282 | forward_commitment | | E5:T13/T14 |  |
| R283 | forward_commitment | | E5:T13/T14 |  |
| R284 | forward_commitment | | E5:T13/T14 |  |
| R285 | forward_commitment | | E6:T15/T16 | RESTATED w/ R249 |
| R286 | forward_commitment | | E6:T15/T16 |  |
| R287 | forward_commitment | | E6:T15/T16 |  |
| R288 | forward_commitment | | E8:T19/T20 |  |
| R289 | forward_commitment | | E8:T19/T20 |  |
| R290 | forward_commitment | | E8:T19/T20 | RESTATED w/ R253 |
| R291 | forward_commitment | | E8:T19/T20 |  |
| R292 | forward_commitment | | E9:T21/T22 | RESTATED w/ R180 |
| R293 | forward_commitment | | E9:T21/T22 | RESTATED w/ R180 |
| R294 | forward_commitment | | E9:T21/T22 |  |
| R295 | forward_commitment | | E9:T21/T22 |  |

### 6. Entities

| ROW ID | category | A2 flags | turn | note |
|---|---|---|---|---|
| R192 | entity |  | T0-header |  |
| R193 | entity |  | T0-header | RESTATED w/ R215,R327 |
| R194 | entity |  | T0-header |  |
| R195 | entity |  | T0-header |  |
| R196 | entity | ASR_UNCERTAIN | T0-header |  |
| R197 | entity |  | T1 |  |
| R198 | entity | ASR_UNCERTAIN | T2 |  |
| R199 | entity |  | T3 |  |
| R200 | entity |  | T3 |  |
| R201 | entity |  | T3 |  |
| R202 | entity | ASR_UNCERTAIN | T3 |  |
| R203 | entity |  | T3 |  |
| R204 | entity | ASR_UNCERTAIN | T3 |  |
| R205 | entity |  | T3 |  |
| R206 | entity |  | T3 |  |
| R207 | entity |  | T3 |  |
| R208 | entity |  | T3 |  |
| R209 | entity |  | T3 |  |
| R210 | entity | ASR_UNCERTAIN | T3 |  |
| R211 | entity | ASR_UNCERTAIN | T3 |  |
| R212 | entity | ASR_UNCERTAIN | E1:T5/T6 |  |
| R213 | entity | ASR_UNCERTAIN | E3:T9/T10 |  |
| R214 | entity | ASR_UNCERTAIN | E4:T11/T12 |  |
| R215 | entity |  | E5:T13/T14 | RESTATED w/ R193 |
| R216 | entity |  | E6:T15/T16 |  |
| R217 | entity |  | E7:T17/T18 |  |
| R218 | entity | ASR_UNCERTAIN | E8:T19/T20 |  |
| R219 | entity | ASR_UNCERTAIN | E9:T21/T22 |  |
| R220 | entity |  | E10:T23/T24 |  |
| R221 | entity |  | E2:T7/T8 |  |
| R222 | entity |  | E4:T11/T12 |  |
| R223 | entity |  | E4:T11/T12 |  |
| R224 | entity |  | E6:T15/T16 |  |
| R225 | entity |  | E6:T15/T16 |  |
| R226 | entity |  | E6:T15/T16 |  |
| R227 | entity | ASR_UNCERTAIN | E8:T19/T20 |  |
| R228 | entity |  | T3 |  |
| R229 | entity | ASR_UNCERTAIN | E10:T23/T24 |  |
| R230 | entity |  | E3:T9/T10 |  |
| R231 | entity |  | E9:T21/T22 |  |
| R232 | entity |  | E9:T21/T22 |  |
| R233 | entity |  | E9:T21/T22 |  |
| R234 | entity |  | E9:T21/T22 |  |
| R235 | entity |  | E9:T21/T22 |  |
| R236 | entity |  | E9:T21/T22 |  |
| R237 | entity |  | E10:T23/T24 |  |
| R238 | entity |  | E10:T23/T24 |  |
| R239 | entity |  | T3 |  |

### 7. Dates

| ROW ID | category | A2 flags | turn | note |
|---|---|---|---|---|
| R296 | date |  | T0-header | RESTATED w/ R330 |
| R297 | date |  | T0-header |  |
| R298 | date |  | T0-header |  |
| R299 | date |  | T3 | RESTATED w/ R300,R306 |
| R300 | date |  | T3 | RESTATED w/ R299 |
| R301 | date |  | T3 |  |
| R302 | date |  | T3 |  |
| R303 | date |  | T3 |  |
| R304 | date |  | T3 | RESTATED w/ R048 |
| R305 | date |  | T3 |  |
| R306 | date |  | T2 | RESTATED w/ R299 |
| R307 | date |  | T3 | RESTATED w/ R257 |
| R308 | date |  | T3 | RESTATED w/ R026 |
| R309 | date |  | T3 | RESTATED w/ R028 |
| R310 | date |  | E1:T5/T6 |  |
| R311 | date |  | E4:T11/T12 |  |
| R312 | date |  | E4:T11/T12 |  |
| R313 | date |  | E4:T11/T12 |  |
| R314 | date |  | T3 |  |
| R315 | date |  | T3 | RESTATED w/ R246 |
| R316 | date |  | E2:T7/T8 |  |
| R317 | date |  | E3:T9/T10 |  |
| R318 | date |  | T3 |  |
| R319 | date |  | E8:T19/T20 |  |
| R320 | date |  | E9:T21/T22 |  |
| R321 | date |  | T25 |  |

### 8. Qualifiers

| ROW ID | category | A2 flags | turn | note |
|---|---|---|---|---|
| R322 | qualifier | ASR_UNCERTAIN | T0-header |  |
| R323 | qualifier | ASR_UNCERTAIN | T0-header |  |
| R324 | qualifier | ASR_UNCERTAIN | T0-header |  |
| R325 | qualifier | ASR_UNCERTAIN | T0-header |  |
| R326 | qualifier | ASR_UNCERTAIN | T0-header |  |
| R327 | qualifier | ASR_UNCERTAIN | T0-header | RESTATED w/ R193 |
| R328 | qualifier | ASR_UNCERTAIN | T0-header |  |
| R329 | qualifier |  | T0-header |  |
| R330 | qualifier |  | T0-header | RESTATED w/ R296 |
| R331 | qualifier |  | T3 | RESTATED w/ R332 |
| R332 | qualifier |  | T3 | RESTATED w/ R331 |
| R333 | qualifier |  | E3:T9/T10 |  |
| R334 | qualifier |  | E3:T9/T10 |  |
| R335 | qualifier |  | E4:T11/T12 |  |
| R336 | qualifier |  | E4:T11/T12 |  |
| R337 | qualifier |  | E4:T11/T12 |  |
| R338 | qualifier |  | E8:T19/T20 |  |
| R339 | qualifier |  | T3 |  |
| R340 | qualifier | ASR_UNCERTAIN | T3 |  |
| R341 | qualifier |  | E1:T5/T6 |  |
| R342 | qualifier |  | T3 |  |
| R343 | qualifier |  | T3 |  |
| R344 | qualifier |  | E9:T21/T22 |  |
| R345 | qualifier |  | E10:T23/T24 |  |
| R346 | qualifier |  | T3 | RESTATED w/ R003,R012 |

### 9. MISSING_FROM_STRUCTURED (own line numbers; loop back to A1)

| M# | fulltext line | turn | flag | claim text (verbatim as heard) |
|---|---|---|---|---|
| M1 | 396 | E3 question | MISSING_FROM_STRUCTURED | "from the time that we have made the monthly disclosures it has been like 15, 20 days" (analyst, monthly disclosure lag) |
| M2 | 500 | E4 answer | MISSING_FROM_STRUCTURED | "the 99.2 also would [improve] over the last four months of the financial year" (collection efficiency; related R286 line 644) |
| M3 | 656 | E6 answer | MISSING_FROM_STRUCTURED | "the 1% movement that we have seen, we have identified which specific branches are contributing" (mortgage PAR X; partial overlap R162 line 652) |
| M4 | 721 | E8 question | MISSING_FROM_STRUCTURED | "is it at 10 or 2, add in the 25 dips, borrow at far lower rates than my existing blended cost" (analyst, ASR garbled) |
| M5 | 745 | E9 question | MISSING_FROM_STRUCTURED | "foreclosure rates ... FY26 versus 1H FY27, not materially higher, but they are inching higher" (analyst) |
| M6 | 762 | E9 question | MISSING_FROM_STRUCTURED | "branch count throughout F5.26 and now 1H F5.27 has largely been flat" (analyst) |
| M7 | 72 | T3 opening | MISSING_FROM_STRUCTURED | "The year FY 27 has started on a good note as reflected in the robust trends" (period reference, low materiality) |

Covered/restated lines, not MISSING: 635 (18 states, R003), 724 (14.25-14.75, R253/R290), 712-713 (4Q/1Q liability raise, ASR period tokens, low value), 787 (35 branches, RESTATED R180/R292), 27 (header Q2 FY27, R299), 453 and 524 (word "percentage" only).

## ID ACCOUNTABILITY
All 346 IDs R001-R346 appear in sections 4-8 (NUMBER 191 s4, FORWARD 56 s5, ENTITY 48 s6, DATE 26 s7, QUALIFIER 25 s8); participant rows in s1 repeat IDs by reference. ZERO_STANDING rows: 0 (A1 states none; transcript has no standing line items). ENTITY_CHANGE: n/a (no prior ledger).

```yaml
stage: A2-enumerator
company: "AYE"
quarter: "Q2 FY27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/aye-q2fy27/work/ledger_concall_aye_q2fy27.md"
counts:
  participants: 16
  turns: 26
  questions: 10
  mgmt_numbers: 191
  forward_hedge: 81
  entities: 48
  dates: 26
  zero_standing: 0
flags_raised: [ASR_UNCERTAIN, ANALYST_UNIDENTIFIED, MULTI_SPEAKER_MERGED, RESTATED, MISSING_FROM_STRUCTURED]
ids_in_structured: 346
ids_referenced: 346
orphan_ids: []
missing_from_structured: ["line 396 monthly disclosure lag 15-20 days (Q3)", "line 500 99.2 collection efficiency over last four months", "line 656 1% mortgage PAR X movement, branches identified", "line 721 analyst borrowing cost 10 or 2 / 25 bp (garbled)", "line 745 foreclosure FY26 vs 1H FY27 (analyst)", "line 762 branch count flat FY26 and 1H FY27 (analyst)", "line 72 FY27 started on good note (low)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "Machine transcript: speakers are not separated, so turns are best effort (26 turns: 10 Q&A pairs plus 6 framing turns); opening remarks T3 merge several presenters. 11 moderator tags equal 10 questions plus one mid-question ASR artefact at fulltext line 525. Q2 analyst is unidentified (moderator line truncated). Seven fulltext lines carry figures that A1 lacks, mostly analyst-side question content; M2 (99.2 over last four months) and M3 (1% mortgage PAR X) are management-side and the more material. No ZERO_STANDING items and no prior ledger, so no diffs. REPEAT_QUESTION not raised; topic overlaps listed for A3."
```
