# LEDGER concall DYCL q2fy27 (A2 ENUMERATOR)
Source: runs/dycl-q2fy27/extracted/dycl-concall-q2fy27-structured.md (A1). Fulltext used only to classify question answers and sweep for misses.
Management-tier, unverified; machine transcript (ASR).

ids_in_structured: 207 | ids_referenced_in_ledger: 207 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: NUMBER      grep_count: 58   sweep_count: 58   header_count: 58   match: yes
category: ENTITY      grep_count: 54   sweep_count: 54   header_count: 54   match: yes
category: FORWARD     grep_count: 30   sweep_count: 30   header_count: 30   match: yes
category: DATE        grep_count: 17   sweep_count: 17   header_count: 17   match: yes
category: QUALIFIER   grep_count: 15   sweep_count: 15   header_count: 15   match: yes
category: QUESTION    grep_count: 33   sweep_count: 33   header_count: 33   match: yes
category: turns       grep_count: 115   sweep_count: 115   header_count: 115   match: yes (T00-T114)
category: asr_doubt   grep_count: 56   header_count: 56   match: yes
category: ids_total   grep_count: 207   header_range R001-R207 = 207   match: yes
category: notes / line_items / agenda_items / auditor_paras / slides: N/A for concall
sweep_missing_from_structured: 5 (M01-M05, section 8)
gate_a2: pass
=== END COUNT TEST ===

ZERO_STANDING: 0 (no tables).

## Zero-standing items
None: transcript has no financial tables. ZERO_STANDING count = 0.

## 1. Participants and entities

### 1a. Management side
ROW_ID | turn | category | A2 flags | note
--- | --- | --- | --- | ---
R062 | T02 | participant-mgmt | ASR_DOUBT | MD; speaks T03 (opening remarks); present
R063 | T02 | participant-mgmt | ASR_DOUBT | CFO; only identified CFO turn is T36 (L191-193, ASR-garbled)
R064 | T02 | participant-mgmt | ASR_DOUBT | IR advisor; no identified turn

MGMT_ABSENCE: none flagged for MD or CFO. Promoter / CMD not named separately; MD (R062) present. Management Q&A turns carry no speaker name in the transcript, so MD vs CFO per answer is unresolvable: flag SPEAKER_UNRESOLVED on all MGMT turns.

### 1b. Analyst side
ROW_ID | turn | category | A2 flags | note
--- | --- | --- | --- | ---
R070 | T05 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R071 | T05 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R073 | T16 | participant-analyst | - | name or firm as heard; pair with adjacent row
R074 | T16 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R075 | T17 | participant-analyst | - | name or firm as heard; pair with adjacent row
R076 | T17 | participant-analyst | - | name or firm as heard; pair with adjacent row
R079 | T22 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R080 | T22 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R081 | T33 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R082 | T33 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R083 | T37 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R084 | T37 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R085 | T45 | participant-analyst | - | name or firm as heard; pair with adjacent row
R086 | T45 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R088 | T55 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R089 | T55 | participant-analyst | - | name or firm as heard; pair with adjacent row
R091 | T63 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R092 | T63 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R094 | T71 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R095 | T71 | participant-analyst | - | name or firm as heard; pair with adjacent row
R096 | T75 | participant-analyst | - | name or firm as heard; pair with adjacent row
R097 | T75 | participant-analyst | - | name or firm as heard; pair with adjacent row
R098 | T79 | participant-analyst | - | name or firm as heard; pair with adjacent row
R099 | T87 | participant-analyst | - | name or firm as heard; pair with adjacent row
R100 | T88 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R103 | T92 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R104 | T92 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R106 | T98 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R107 | T98 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R108 | T103 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R109 | T103 | participant-analyst | ASR_DOUBT | name or firm as heard; pair with adjacent row
R110 | T106 | participant-analyst | - | name or firm as heard; pair with adjacent row

### 1c. Host, operator, company, other entities
ROW_ID | turn | category | A2 flags | note
--- | --- | --- | --- | ---
R059 | T01 | entity | - | -
R060 | T01 | entity | ASR_DOUBT | -
R061 | T02 | entity | - | -
R065 | T00 | entity | - | -
R066 | T03 | entity | - | -
R067 | T03 | entity | - | -
R068 | T03 | entity | - | -
R069 | T04 | entity | ASR_DOUBT | -
R072 | T13 | entity | - | -
R077 | T20 | entity | - | aluminium restated (R077/R093)
R078 | T20 | entity | - | -
R087 | T46 | entity | - | -
R090 | T59 | entity | - | -
R093 | T68 | entity | - | aluminium restated (R077/R093)
R101 | T90 | entity | ASR_DOUBT | same competitor, two spellings (R100/R101)
R102 | T91 | entity | - | -
R105 | T96 | entity | - | -
R111 | T106 | entity | - | -
R112 | T114 | entity | ASR_DOUBT;ENTITY_MISHEARD | company name heard as Dynamic Tables; same entity as R065

## 2. Speaker turns (T00-T114; 115 turns)
Turn | lines | role | A2 flags | structured rows in turn
--- | --- | --- | --- | ---
T00 | L001-L002 | HEADER | - | R001, R002, R144, R160, R161
T01 | L003-L011 | OPERATOR | - | R059,R060,R143
T02 | L012-L024 | MODERATOR | - | R061,R062,R063,R064
T03 | L025-L058 | MGMT_MD | - | R066,R067,R068,R113,R114,R115+1 more
T04 | L059-L061 | UNATTRIBUTED | UNATTRIBUTED | R003,R069
T05 | L062-L067 | OPERATOR | - | R070,R071 | Q: R175
T06 | L068-L072 | MGMT | SPEAKER_UNRESOLVED | R004,R005,R006,R116,R117
T07 | L073-L073 | ANALYST | - | -
T08 | L074-L074 | MGMT | SPEAKER_UNRESOLVED | -
T09 | L075-L076 | ANALYST | - | -
T10 | L077-L078 | MGMT | SPEAKER_UNRESOLVED | R007,R008,R118
T11 | L079-L086 | ANALYST | - | R146 | Q: R176
T12 | L087-L090 | MGMT | SPEAKER_UNRESOLVED | R009,R010,R119
T13 | L091-L097 | ANALYST | - | R072 | Q: R177
T14 | L098-L100 | MGMT | SPEAKER_UNRESOLVED | R120
T15 | L101-L101 | ANALYST | - | -
T16 | L102-L102 | OPERATOR | - | R073,R074
T17 | L103-L103 | ANALYST | - | R075,R076 | Q: R178
T18 | L104-L104 | MGMT | SPEAKER_UNRESOLVED | -
T19 | L105-L106 | ANALYST | - | -
T20 | L107-L109 | MGMT | SPEAKER_UNRESOLVED | R077,R078
T21 | L110-L110 | OPERATOR | - | -
T22 | L111-L116 | ANALYST | - | R079,R080 | Q: R179,R180
T23 | L117-L122 | MGMT | SPEAKER_UNRESOLVED | R011,R012,R121,R162,R163
T24 | L123-L125 | ANALYST | - | R013,R014,R015 | Q: R181
T25 | L126-L126 | MGMT | SPEAKER_UNRESOLVED | -
T26 | L127-L127 | ANALYST | - | -
T27 | L128-L142 | MGMT | SPEAKER_UNRESOLVED | R164,R165
T28 | L143-L148 | ANALYST | - |  | Q: R182
T29 | L149-L154 | MGMT | SPEAKER_UNRESOLVED | R122,R123
T30 | L155-L160 | ANALYST | - |  | Q: R183
T31 | L161-L167 | MGMT | SPEAKER_UNRESOLVED | R169,R170
T32 | L168-L170 | OPERATOR | - | R016
T33 | L171-L171 | ANALYST | - | R081,R082 | Q: R184
T34 | L172-L182 | MGMT | SPEAKER_UNRESOLVED | R166,R171
T35 | L183-L190 | ANALYST | - | R017,R018,R147,R148 | Q: R185
T36 | L191-L193 | MGMT_CFO | - | R019,R020,R021,R022,R023,R149
T37 | L194-L196 | OPERATOR | - | R083,R084
T38 | L197-L200 | ANALYST | - | R024 | Q: R186
T39 | L201-L201 | MGMT | SPEAKER_UNRESOLVED | R025,R124
T40 | L202-L202 | ANALYST | - | R026
T41 | L203-L205 | MGMT | SPEAKER_UNRESOLVED | R027,R125,R168
T42 | L206-L207 | ANALYST | - |  | Q: R187
T43 | L208-L209 | MGMT | SPEAKER_UNRESOLVED | R028,R029,R030,R126
T44 | L210-L210 | ANALYST | - | -
T45 | L211-L213 | OPERATOR | - | R085,R086
T46 | L214-L218 | ANALYST | - | R087 | Q: R188
T47 | L219-L219 | MGMT | SPEAKER_UNRESOLVED | R127
T48 | L220-L222 | ANALYST | - | -
T49 | L223-L224 | MGMT | SPEAKER_UNRESOLVED | -
T50 | L225-L228 | ANALYST | - | R031,R032
T51 | L229-L232 | OPERATOR | - | -
T52 | L233-L234 | ANALYST | - |  | Q: R189
T53 | L235-L236 | MGMT | SPEAKER_UNRESOLVED | -
T54 | L237-L238 | ANALYST | - | -
T55 | L239-L242 | OPERATOR | - | R033,R088,R089
T56 | L243-L243 | ANALYST | - | -
T57 | L244-L244 | OPERATOR | - | -
T58 | L245-L248 | ANALYST | - |  | Q: R190
T59 | L249-L249 | MGMT | SPEAKER_UNRESOLVED | R090
T60 | L250-L253 | ANALYST | - |  | Q: R191
T61 | L254-L260 | MGMT | SPEAKER_UNRESOLVED | R034,R035,R167
T62 | L261-L261 | ANALYST | - | -
T63 | L262-L263 | OPERATOR | - | R091,R092
T64 | L264-L265 | ANALYST | - | R036 | Q: R192
T65 | L266-L266 | MGMT | SPEAKER_UNRESOLVED | -
T66 | L267-L269 | ANALYST | - | R037,R038,R150 | Q: R193
T67 | L270-L271 | MGMT | SPEAKER_UNRESOLVED | R128
T68 | L272-L275 | ANALYST | - | R039,R040,R093,R151 | Q: R194
T69 | L276-L276 | MGMT | SPEAKER_UNRESOLVED | R129
T70 | L277-L277 | OPERATOR | - | -
T71 | L278-L281 | ANALYST | - | R041,R094,R095 | Q: R195
T72 | L282-L283 | MGMT | SPEAKER_UNRESOLVED | R130,R131
T73 | L284-L286 | ANALYST | - |  | Q: R196
T74 | L287-L288 | MGMT | SPEAKER_UNRESOLVED | R042,R174
T75 | L289-L291 | OPERATOR | - | R096,R097
T76 | L292-L292 | OPERATOR | - | -
T77 | L293-L304 | ANALYST | - | R152 | Q: R197
T78 | L305-L308 | MGMT | SPEAKER_UNRESOLVED | R132
T79 | L309-L310 | OPERATOR | - | R098
T80 | L311-L315 | ANALYST | - | R153 | Q: R198
T81 | L316-L319 | MGMT | SPEAKER_UNRESOLVED | R133
T82 | L320-L321 | ANALYST | - |  | Q: R199
T83 | L322-L326 | MGMT | SPEAKER_UNRESOLVED | R043,R044,R045
T84 | L327-L328 | ANALYST | - | R046,R047 | Q: R200
T85 | L329-L331 | MGMT | SPEAKER_UNRESOLVED | R048,R049,R050,R173
T86 | L332-L332 | ANALYST | - | -
T87 | L333-L335 | OPERATOR | - | R099
T88 | L336-L342 | ANALYST | - | R100 | Q: R201
T89 | L343-L344 | MGMT | SPEAKER_UNRESOLVED | R134
T90 | L345-L346 | ANALYST | - | R101
T91 | L347-L349 | MGMT | SPEAKER_UNRESOLVED | R102
T92 | L350-L351 | OPERATOR | - | R103,R104
T93 | L352-L352 | ANALYST | - |  | Q: R202
T94 | L353-L354 | MGMT | SPEAKER_UNRESOLVED | R135
T95 | L355-L361 | ANALYST | - | R051,R052,R154 | Q: R203
T96 | L362-L364 | MGMT | SPEAKER_UNRESOLVED | R105,R136
T97 | L365-L365 | OPERATOR | - | -
T98 | L366-L371 | ANALYST | - | R053,R054,R055,R056,R057,R106+3 more | Q: R204
T99 | L372-L373 | MGMT | SPEAKER_UNRESOLVED | R137
T100 | L374-L375 | ANALYST | - | R058,R157 | Q: R205
T101 | L376-L378 | MGMT | SPEAKER_UNRESOLVED | R138
T102 | L379-L379 | ANALYST | - | -
T103 | L380-L380 | OPERATOR | - | R108,R109
T104 | L381-L383 | ANALYST | - |  | Q: R206
T105 | L384-L390 | MGMT | SPEAKER_UNRESOLVED | R158,R159,R172
T106 | L391-L397 | ANALYST | - | R110,R111 | Q: R207
T107 | L398-L405 | MGMT | SPEAKER_UNRESOLVED | R139,R140
T108 | L406-L406 | ANALYST | - | -
T109 | L407-L407 | MGMT | SPEAKER_UNRESOLVED | R141
T110 | L408-L409 | UNATTRIBUTED | UNATTRIBUTED | -
T111 | L410-L412 | OPERATOR | - | -
T112 | L413-L415 | MODERATOR | - | -
T113 | L416-L416 | MGMT | SPEAKER_UNRESOLVED | R142
T114 | L417-L418 | OPERATOR | - | R112

Turn roles (T01-T114): {'OPERATOR': 21, 'MODERATOR': 2, 'MGMT_MD': 1, 'UNATTRIBUTED': 2, 'MGMT': 40, 'ANALYST': 47, 'MGMT_CFO': 1}
Prepared remarks: T02 moderator, T03 MD (L025-L058, 34 lines). Q&A runs T05-T114, 110 of 114 turns (96%). Seven operator cut-offs of management or analyst (T32, T37, T45, T63, T75, T79, T92).

## 3. Question ledger (33 analyst questions)
ROW_ID | turn | caller | answer class | REPEAT | note
--- | --- | --- | --- | --- | ---
R175 | T05 | Viri Trivedi | ANSWERED_WITH_NUMBER | - | 15% working-capital finance cost; around 10 on six-month basis, sub 15 (units ASR_DOUBT)
R176 | T11 | Viri Trivedi | ANSWERED_WITH_NUMBER | - | 240-250 crore initial potential only; installed capacity and FY27/28 expectation not answered (PARTIAL)
R177 | T13 | Viri Trivedi | ANSWERED_NO_NUMBER | REPEAT_QUESTION -> R182,R202 (exports asked 3x) | qualitative: opportunity very huge; Middle East not addressed
R178 | T17 | Abhishek Maheshwari | ANSWERED_NO_NUMBER | - | direct: no scrap; aluminium used, recycled aluminium not used
R179 | T22 | Gita (Kogito) | DEFLECTED | REPEAT_QUESTION -> R186,R194 (volume vs price growth asked 3x) | no volume or price split given; T23 pivots to operating-profit guidance
R180 | T22 | Gita (Kogito) | DEFLECTED | - | other expenses called interchangeable with gross profit; sustainability not answered; 10-11% restated (PARTIAL)
R181 | T24 | Gita (Kogito) | DEFLECTED | - | EBITDA per ton not addressed; reframed to value growth, budget not volume based
R182 | T28 | Gita (Kogito) | ANSWERED_NO_NUMBER | REPEAT_QUESTION -> R177,R202 | agreed: near-term hard to predict, long-term strong
R183 | T30 | Gita (Kogito) | ANSWERED_NO_NUMBER | - | no link to new facility, working-capital borrowings, no specific debt; depreciation part not addressed (PARTIAL)
R184 | T33 | Bhumna (Kamana) | ANSWERED_NO_NUMBER | - | mix, pass-through, fixed-price contracts; no gross margin figure
R185 | T35 | Bhumna (Kamana) | LOST_TO_ASR | REPEAT_QUESTION -> R203 | T36 L191-193 garbled; 184 / 10-15 crore / around 200 crore gross block / 7x fragments unreliable; operator cut off at L194
R186 | T38 | Aamkit/Ankit Shah (Anand Rati) | DEFLECTED | REPEAT_QUESTION -> R179,R194 | cannot predict volume vs price; restates 20% value growth (different metric)
R187 | T42 | Aamkit/Ankit Shah (Anand Rati) | ANSWERED_WITH_NUMBER | REPEAT_QUESTION -> R191,R193 (margin decline/guidance asked 3x) | 10-11% operating margin restated; no explanation of the decline
R188 | T46 | Akash Dubey (Amrappalli) | DEFLECTED | - | no market guidance; US order flow not disclosed
R189 | T52 | Akash Dubey | DEFLECTED | - | audio fault (T51); management asked analyst to email question; no answer on call
R190 | T58 | Chintan (Sagun) | DEFLECTED | REPEAT_QUESTION -> R192 (product mix asked 2x) | miscellaneous cables; no product split
R191 | T60 | Chintan (Sagun) | ANSWERED_WITH_NUMBER | REPEAT_QUESTION -> R187,R193 | 80-90% of contracts pass-through; cause = product/revenue mix
R192 | T64 | Nikhil Purovit (Fident) | DEFLECTED | REPEAT_QUESTION -> R190 | not very different to earlier; no split (see M04)
R193 | T66 | Nikhil Purovit (Fident) | DEFLECTED | REPEAT_QUESTION -> R187,R191 | no exact margin guidance; refers to long-run range
R194 | T68 | Nikhil Purovit (Fident) | DEFLECTED | REPEAT_QUESTION -> R179,R186 | market-guidance answer repeated; ASR tail gap at L276 (partial loss)
R195 | T71 | Vidant (Canara) | DEFLECTED | - | closing order book tricky to guide; over a period, reaching the optimum
R196 | T73 | Vidant (Canara) | ANSWERED_WITH_NUMBER | - | 100% raw material covered on fixed-price (ASR_DOUBT); answer cut off by operator T75 (PARTIAL)
R197 | T77 | Kevin Shah (ABC) | ANSWERED_NO_NUMBER | - | only new-plant additional volume answered; demand moderation vs deliberate not answered (PARTIAL)
R198 | T80 | Shikhar Tiwari | ANSWERED_NO_NUMBER | - | order booking improved; will improve as commodity prices dip; no figure
R199 | T82 | Shikhar Tiwari | ANSWERED_WITH_NUMBER | - | 70-80% quarterly / more than 80% yearly from repeat customers
R200 | T84 | Shikhar Tiwari | ANSWERED_WITH_NUMBER | - | top 10 = 40-45% of sales; top 5 not given
R201 | T88 | Ankit Shah (Anand Rati) | ANSWERED_NO_NUMBER | - | no impact seen; house wire market may be hit
R202 | T93 | Sahil Patani (Strokes) | DEFLECTED | REPEAT_QUESTION -> R177,R182 | export/domestic split difficult to predict
R203 | T95 | Sahil Patani (Strokes) | ANSWERED_NO_NUMBER | REPEAT_QUESTION -> R185 (capex) | capex ongoing, brownfield; no amount or timing
R204 | T98 | Divi Gosar (Shukkam) | DEFLECTED | REPEAT_QUESTION -> R186 (20% growth guidance re-asked) | no quantitative short-term guidance for FY27
R205 | T100 | Divi Gosar (Shukkam) | DEFLECTED | REPEAT_QUESTION -> R204 | no quantitative guidance for FY28; revisit after year close
R206 | T104 | Hoshong (Elio) | ANSWERED_NO_NUMBER | - | days not up much; H2 seasonality; raw material value up; no figure
R207 | T106 | Hoshong (Elio) | DEFLECTED | - | no order or customer commitment disclosed for electron beam solar; data centre timeline depends on market (PARTIAL)

Answer split: {'ANSWERED_WITH_NUMBER': 7, 'ANSWERED_NO_NUMBER': 10, 'DEFLECTED': 15, 'LOST_TO_ASR': 1}
Partial answers (counted by dominant class): R176, R180, R183, R196, R197, R207.

## 4. Numbers (R001-R058)
ROW_ID | turn | speaker class | A2 flags | note
--- | --- | --- | --- | ---
R001 | T00 | TOOL_METADATA | - | -
R002 | T00 | TOOL_METADATA | - | -
R003 | T04 | UNATTRIBUTED | ASR_DOUBT | -
R004 | T06 | MGMT_SPOKEN | ASR_DOUBT | RESTATED 15% finance cost (R004,R005,R006)
R005 | T06 | MGMT_SPOKEN | ASR_DOUBT | RESTATED 15% finance cost (R004,R005,R006)
R006 | T06 | MGMT_SPOKEN | ASR_DOUBT | RESTATED 15% finance cost (R004,R005,R006)
R007 | T10 | MGMT_SPOKEN | ASR_DOUBT | -
R008 | T10 | MGMT_SPOKEN | ASR_DOUBT | -
R009 | T12 | MGMT_SPOKEN | ASR_DOUBT | RESTATED 240-250 crore new facility (R009/R010; analyst R017,R018 round to 250)
R010 | T12 | MGMT_SPOKEN | ASR_DOUBT | RESTATED 240-250 crore new facility (R009/R010; analyst R017,R018 round to 250)
R011 | T23 | MGMT_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R012 | T23 | MGMT_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R013 | T24 | ANALYST_SPOKEN | - | analyst 18% EBITDA growth; management did not confirm
R014 | T24 | ANALYST_SPOKEN | - | RESTATED 6% volume growth (R014,R024); analyst figure
R015 | T24 | ANALYST_SPOKEN | - | -
R016 | T32 | OPERATOR | - | -
R017 | T35 | ANALYST_SPOKEN | ASR_DOUBT | RESTATED 240-250 crore new facility (R009/R010; analyst R017,R018 round to 250)
R018 | T35 | ANALYST_SPOKEN | - | RESTATED 240-250 crore new facility (R009/R010; analyst R017,R018 round to 250)
R019 | T36 | MGMT_SPOKEN | ASR_DOUBT | CFO answer T36; metric unclear; ASR-unreliable
R020 | T36 | MGMT_SPOKEN | ASR_DOUBT | CFO answer T36; metric unclear; ASR-unreliable
R021 | T36 | MGMT_SPOKEN | ASR_DOUBT | CFO answer T36; metric unclear; ASR-unreliable
R022 | T36 | MGMT_SPOKEN | - | CFO answer T36; metric unclear; ASR-unreliable
R023 | T36 | MGMT_SPOKEN | ASR_DOUBT | CFO answer T36; metric unclear; ASR-unreliable
R024 | T38 | ANALYST_SPOKEN | - | RESTATED 6% volume growth (R014,R024); analyst figure
R025 | T39 | MGMT_SPOKEN | - | RESTATED 20% growth (R025,R027 mgmt; R026 analyst misreading, corrected at T41)
R026 | T40 | ANALYST_SPOKEN | - | RESTATED 20% growth (R025,R027 mgmt; R026 analyst misreading, corrected at T41)
R027 | T41 | MGMT_SPOKEN | - | RESTATED 20% growth (R025,R027 mgmt; R026 analyst misreading, corrected at T41)
R028 | T43 | MGMT_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R029 | T43 | MGMT_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R030 | T43 | MGMT_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R031 | T50 | ANALYST_SPOKEN | ASR_DOUBT | -
R032 | T50 | ANALYST_SPOKEN | ASR_DOUBT | -
R033 | T55 | OPERATOR | - | -
R034 | T61 | MGMT_SPOKEN | - | pass-through share: 80-90% (R034/R035) vs 100% on fixed-price (R042)
R035 | T61 | MGMT_SPOKEN | - | pass-through share: 80-90% (R034/R035) vs 100% on fixed-price (R042)
R036 | T64 | ANALYST_SPOKEN | - | -
R037 | T66 | ANALYST_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R038 | T66 | ANALYST_SPOKEN | - | RESTATED 10-11% margin (R011/R012, R028-R030 mgmt; R037/R038 analyst)
R039 | T68 | ANALYST_SPOKEN | ASR_DOUBT | -
R040 | T68 | ANALYST_SPOKEN | ASR_DOUBT | -
R041 | T71 | ANALYST_SPOKEN | - | -
R042 | T74 | MGMT_SPOKEN | ASR_DOUBT | pass-through share: 80-90% (R034/R035) vs 100% on fixed-price (R042)
R043 | T83 | MGMT_SPOKEN | - | repeat-customer share
R044 | T83 | MGMT_SPOKEN | - | repeat-customer share
R045 | T83 | MGMT_SPOKEN | - | repeat-customer share
R046 | T84 | ANALYST_SPOKEN | - | -
R047 | T84 | ANALYST_SPOKEN | - | -
R048 | T85 | MGMT_SPOKEN | - | top-10 share 40-45%
R049 | T85 | MGMT_SPOKEN | - | top-10 share 40-45%
R050 | T85 | MGMT_SPOKEN | - | top-10 share 40-45%
R051 | T95 | ANALYST_SPOKEN | - | -
R052 | T95 | ANALYST_SPOKEN | - | -
R053 | T98 | ANALYST_SPOKEN | - | analyst premise; not management-confirmed
R054 | T98 | ANALYST_SPOKEN | - | analyst premise; not management-confirmed
R055 | T98 | ANALYST_SPOKEN | - | analyst premise; not management-confirmed
R056 | T98 | ANALYST_SPOKEN | ASR_DOUBT | analyst premise; not management-confirmed
R057 | T98 | ANALYST_SPOKEN | - | analyst premise; not management-confirmed
R058 | T100 | ANALYST_SPOKEN | - | analyst premise; not management-confirmed

Speaker split: MGMT_SPOKEN 28, ANALYST_SPOKEN 25, OPERATOR 2, TOOL_METADATA 2, UNATTRIBUTED 1 = 58. Role 5 feed rows: R004, R005, R006, R007, R008, R009, R010, R011, R012, R019, R020, R021, R022, R023, R025, R027, R028, R029, R030, R034, R035, R042, R043, R044, R045, R048, R049, R050.

## 5. Forward commitments and no-guidance statements
ROW_ID | turn | category | A2 flags | note
--- | --- | --- | --- | ---
R113 | T03 | forward | - | forward commitment
R114 | T03 | forward | - | forward commitment
R115 | T03 | forward | - | forward commitment
R116 | T06 | forward | ASR_DOUBT | forward commitment; RESTATED finance cost 15%
R117 | T06 | forward | ASR_DOUBT | forward commitment; RESTATED finance cost 15%
R118 | T10 | forward | ASR_DOUBT | forward commitment; RESTATED finance cost 15%
R119 | T12 | forward | ASR_DOUBT | forward commitment
R120 | T14 | forward | - | forward commitment
R121 | T23 | forward | - | forward commitment; RESTATED guidance (R121,R126 margin 10-11%; R124,R125 growth 20%)
R122 | T29 | forward | - | HEDGED_COMMITMENT
R123 | T29 | forward | - | forward commitment
R124 | T39 | forward | - | forward commitment; RESTATED guidance (R121,R126 margin 10-11%; R124,R125 growth 20%)
R125 | T41 | forward | - | forward commitment; RESTATED guidance (R121,R126 margin 10-11%; R124,R125 growth 20%)
R126 | T43 | forward | - | forward commitment; RESTATED guidance (R121,R126 margin 10-11%; R124,R125 growth 20%)
R127 | T47 | forward | - | NO_GUIDANCE (refusal)
R128 | T67 | forward | - | NO_GUIDANCE (refusal)
R129 | T69 | forward | - | NO_GUIDANCE (refusal)
R130 | T72 | forward | - | NO_GUIDANCE (refusal); same statement split by ASR (R130/R131)
R131 | T72 | forward | ASR_DOUBT | forward commitment; same statement split by ASR (R130/R131)
R132 | T78 | forward | - | HEDGED_COMMITMENT
R133 | T81 | forward | - | HEDGED_COMMITMENT
R134 | T89 | forward | - | HEDGED_COMMITMENT
R135 | T94 | forward | - | NO_GUIDANCE (refusal)
R136 | T96 | forward | - | forward commitment
R137 | T99 | forward | - | NO_GUIDANCE (refusal)
R138 | T101 | forward | - | NO_GUIDANCE (refusal)
R139 | T107 | forward | - | HEDGED_COMMITMENT
R140 | T107 | forward | - | HEDGED_COMMITMENT
R141 | T109 | forward | - | HEDGED_COMMITMENT
R142 | T113 | forward | - | TRUNCATED (closing remark cut off); incomplete

## 6. Dates and timelines
ROW_ID | turn | category | A2 flags | note
--- | --- | --- | --- | ---
R143 | T01 | date | - | metadata
R144 | T00 | date | - | metadata
R145 | T03 | date | - | H1/H2 timing anchor
R146 | T11 | date | ASR_DOUBT | H1/H2 timing anchor
R147 | T35 | date | - | -
R148 | T35 | date | - | H1/H2 timing anchor
R149 | T36 | date | - | H1/H2 timing anchor
R150 | T66 | date | - | -
R151 | T68 | date | - | -
R152 | T77 | date | - | -
R153 | T80 | date | - | -
R154 | T95 | date | - | -
R155 | T98 | date | - | H1/H2 timing anchor
R156 | T98 | date | ASR_DOUBT | FY27 / FY28 as heard
R157 | T100 | date | ASR_DOUBT | FY27 / FY28 as heard
R158 | T105 | date | - | -
R159 | T105 | date | - | -

## 7. Qualifiers, hedges, definitions
ROW_ID | turn | category | A2 flags | note
--- | --- | --- | --- | ---
R160 | T00 | qualifier | - | -
R161 | T00 | qualifier | - | -
R162 | T23 | qualifier | - | -
R163 | T23 | qualifier | ASR_DOUBT | -
R164 | T27 | qualifier | - | -
R165 | T27 | qualifier | - | -
R166 | T34 | qualifier | - | RESTATED pass-through (R166,R167)
R167 | T61 | qualifier | - | RESTATED pass-through (R166,R167)
R168 | T41 | qualifier | - | RESTATED definition of 20% guidance (R125,R168)
R169 | T31 | qualifier | - | -
R170 | T31 | qualifier | - | -
R171 | T34 | qualifier | - | HEDGE: unfair to judge on one quarter
R172 | T105 | qualifier | - | RESTATED seasonality (R158,R159,R172)
R173 | T85 | qualifier | - | -
R174 | T74 | qualifier | - | -

## 8. MISSING_FROM_STRUCTURED (units found in sweep that A1 lacks)
ID | line | turn | flag | claim text
--- | --- | --- | --- | ---
M01 | L055 | T03 | MISSING_FROM_STRUCTURED | "With a healthy order pipeline, expanding manufacturing capabilities and favorable industry tailwinds" (qualitative forward claim in MD remarks)
M02 | L141-L142 | T27 | MISSING_FROM_STRUCTURED | "There is unlimited latent demand in power to any infrastructure from volume number" (ASR-garbled demand claim)
M03 | L344 | T89 | MISSING_FROM_STRUCTURED | "this has been happening for the last 20-30 years, 40 years" (number; new-entrant history; ASR_DOUBT)
M04 | L266 | T65 | MISSING_FROM_STRUCTURED | "it wasn't very different to how we've done earlier" (whole answer to R192 product-mix question; no split)
M05 | L099 | T14 | MISSING_FROM_STRUCTURED | "tariff fear which keep on emerging" (export risk named by management)

## 9. ASR and answer-loss register
L060 (T04, R003): "Less than 60 days", unattributed, subject unknown.
L089 (T12, R009/R010): 240-250 crore; answer opening lost.
L191-L193 (T36, R019-R023): CFO capex answer garbled; operator cut-off at L194.
L276 (T69): ordering-outlook answer truncated.
L287-L288 (T74): fixed-price answer cut by operator.
L416 (T113, R142): closing remark truncated.
L229-L238 (T51-T54, R189): audio fault; email requested; unanswered.
