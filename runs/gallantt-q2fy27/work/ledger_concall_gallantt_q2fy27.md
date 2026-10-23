# LEDGER: concall GALLANTT Q2 FY27 (A2 enumerator). Source: A1 structured extraction. All attributions INFERRED; all numbers ASR.
ids_in_structured: 263 | ids_referenced_in_ledger: 263 | orphan_ids: [] | match: yes
(ID accountability counts R001-R263; T01-T60 and Q1a-Q7 are separate handle tables, also fully enumerated below.)

=== A2 COUNT TEST ===
category: notes            grep_count: 0    sweep_count: 0    match: yes (n/a: concall)
category: line_items       grep_count: 0    sweep_count: 0    match: yes (n/a)
category: participants     grep_count: 15   sweep_count: 15   match: yes (R133-R139 7 mgmt/IR/moderator rows + R164-R171 8 analysts/closing)
category: turns            grep_count: 60   sweep_count: 60   match: yes (T01-T60)
category: questions        grep_count: 17   sweep_count: 17   match: yes (Q1a-Q7; 7 analysts)
category: mgmt_numbers     grep_count: 115  sweep_count: 115  match: yes (NUMBER 127 minus 7 header R001-R007 minus 5 analyst-spoken R099,R101,R102,R103,R117)
category: number_rows_all  grep_count: 127  sweep_count: 127  match: yes
category: entity_rows      grep_count: 44   sweep_count: 44   match: yes
category: forward_rows     grep_count: 45   sweep_count: 45   match: yes
category: date_rows        grep_count: 28   sweep_count: 28   match: yes
category: qualifier_rows   grep_count: 19   sweep_count: 19   match: yes
category: zero_standing    grep_count: 3    sweep_count: 3    match: yes (R014,R034,R075)
category: ids_total        grep_count: 263  sweep_count: 263  match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. PARTICIPANTS (MGMT_ABSENCE check: Vice Chairman, CEO and CFO all present; no absence)
ROW_ID | category | A2 flags | note
R133 | participant | - | IR presenter
R134 | participant | - | IR firm
R135 | participant | ASR_VARIANT | moderator, ASR name
R136 | participant | ASR_VARIANT | management: Vice Chairman
R137 | participant | - | management: CEO
R138 | participant | - | management: CFO
R139 | participant | ASR_VARIANT | Vice Chairman, ASR spelling variant of R136
R164 | participant | - | analyst Q1 (T09)
R165 | participant | ASR_VARIANT | analyst Q2 (T15)
R166 | participant | ASR_VARIANT | analyst Q3 (T23)
R167 | participant | ASR_VARIANT | analyst Q4 (T35)
R168 | participant | ASR_VARIANT | analyst Q5 (T39)
R169 | participant | ASR_VARIANT | analyst Q6 (T44)
R170 | participant | - | analyst Q7 (T54)
R171 | participant | ASR_VARIANT | closing IR speaker (ASR variant of R133)

## 2. SPEAKER TURNS (60; all INFERRED)
TURN | category | A2 flags | note
T01 | turn | INFERRED | fulltext lines 26-31; speaker: Moderator (opening)
T02 | turn | INFERRED | fulltext lines 32-33; speaker: Moderator (hand-off to IR)
T03 | turn | INFERRED | fulltext lines 34-45; speaker: IR host Vanessa Hernandez, AdFactors PR
T04 | turn | INFERRED | fulltext lines 46; speaker: IR host (hand-over)
T05 | turn | INFERRED | fulltext lines 47-119; speaker: Vice Chairman ("Dean Dayal Jalan"/"Dindayal Jalan")
T06 | turn | INFERRED | fulltext lines 120-174; speaker: CEO ("Mayank Agarwal")
T07 | turn | INFERRED | fulltext lines 175-207; speaker: CFO ("Amit Jalan")
T08 | turn | INFERRED | fulltext lines 208-214; speaker: Moderator (Q&A open, introduces Q1)
T09 | turn | INFERRED | fulltext lines 215-217; speaker: Analyst Vinny Jain, Jain Investments (Q1a)
T10 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 218-223; speaker: Management respondent, CEO or Vice Chairman UNCERTAIN
T11 | turn | INFERRED | fulltext lines 224-226; speaker: Analyst Vinny Jain (Q1b)
T12 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 227-237; speaker: Management respondent, speaker UNCERTAIN (addressed as "Vidhi", ASR)
T13 | turn | INFERRED | fulltext lines 238-241; speaker: Analyst Vinny Jain (thanks)
T14 | turn | INFERRED | fulltext lines 242-246; speaker: Moderator (introduces Q2)
T15 | turn | INFERRED | fulltext lines 247-252; speaker: Analyst Preeti Sharma, Inverse Force Advisors (Q2a)
T16 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 253-259; speaker: Management respondent, speaker UNCERTAIN
T17 | turn | INFERRED | fulltext lines 260-262; speaker: Analyst Preeti Sharma (Q2b)
T18 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 263-273; speaker: Management respondent, speaker UNCERTAIN (cost detail, CEO or CFO)
T19 | turn | INFERRED | fulltext lines 274-276; speaker: Analyst Preeti Sharma (Q2c)
T20 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 276-281; speaker: Management respondent, speaker UNCERTAIN
T21 | turn | INFERRED | fulltext lines 281-282; speaker: Analyst Preeti Sharma (close) then moderator
T22 | turn | INFERRED | fulltext lines 282-283; speaker: Moderator (introduces Q3)
T23 | turn | INFERRED | fulltext lines 283-286; speaker: Analyst Anirudh Sharma (Q3a)
T24 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 287-291; speaker: Management respondent, speaker UNCERTAIN
T25 | turn | INFERRED | fulltext lines 291-293; speaker: Analyst Anirudh Sharma (Q3b)
T26 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 293-297; speaker: Management respondent, speaker UNCERTAIN
T27 | turn | INFERRED | fulltext lines 298-299; speaker: Analyst Anirudh Sharma (Q3c)
T28 | turn | INFERRED | fulltext lines 300; speaker: Management respondent
T29 | turn | INFERRED,REPEAT_QUESTION | fulltext lines 301; Q3c re-asked; speaker: Analyst Anirudh Sharma (repeats Q3c)
T30 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 302-304; speaker: Management respondent, speaker UNCERTAIN
T31 | turn | INFERRED | fulltext lines 305-306; speaker: Management respondent and Analyst exchange; CFO invited ("Amighi, are you on the call?")
T32 | turn | INFERRED | fulltext lines 307-314; speaker: CFO ("Amit Jalan", ASR "Bifumi")
T33 | turn | INFERRED | fulltext lines 315-317; speaker: Analyst Anirudh Sharma (thanks)
T34 | turn | INFERRED | fulltext lines 318-320; speaker: Moderator then Analyst Vedant Trivedi, Vinayat Capital
T35 | turn | INFERRED | fulltext lines 321-322; speaker: Analyst Vedant Trivedi, Vinayat Capital (Q4a)
T36 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 323-337; speaker: Management respondent, speaker UNCERTAIN (IT detail, CFO likely by content)
T37 | turn | INFERRED,SPEAKER_UNCERTAIN,QUESTION_NOT_TRANSCRIBED | fulltext lines 338-342; Q4b question segment absent; speaker: Management respondent, speaker UNCERTAIN; Q4b question segment absent in ASR
T38 | turn | INFERRED | fulltext lines 343-344; speaker: Analyst Vedant Trivedi (thanks) then Moderator
T39 | turn | INFERRED | fulltext lines 345-355; speaker: Analyst Namesh Pandya (Q5a, Q5b intro) and management reply
T40 | turn | INFERRED | fulltext lines 356-358; speaker: Analyst Namesh Pandya (Q5b) then management reply lines 340-341
T41 | turn | INFERRED | fulltext lines 359-362; speaker: Analyst Namesh Pandya (Q5c)
T42 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 363-365; speaker: Management respondent, speaker UNCERTAIN
T43 | turn | INFERRED | fulltext lines 366-367; speaker: Moderator (reminder, introduces Q6)
T44 | turn | INFERRED | fulltext lines 368-375; speaker: Analyst jimma maitha, maitha investments (Q6a), audio check with moderator
T45 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 376-379; speaker: Management respondent, speaker UNCERTAIN
T46 | turn | INFERRED | fulltext lines 380-382; speaker: Analyst jimma maitha (Q6b)
T47 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 382-387; speaker: Management respondent, speaker UNCERTAIN
T48 | turn | INFERRED | fulltext lines 388; speaker: Analyst jimma maitha (Q6c)
T49 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 389-394; speaker: Management respondent, speaker UNCERTAIN
T50 | turn | INFERRED | fulltext lines 395; speaker: Analyst jimma maitha (follow-up on utilization)
T51 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 396-399; speaker: Management respondent, speaker UNCERTAIN
T52 | turn | INFERRED | fulltext lines 400-402; speaker: Analyst jimma maitha and others (thanks, noise)
T53 | turn | INFERRED | fulltext lines 403-418; speaker: Moderator introduces Dhanraj Tolani, Kuber Advisors; audio-connection delay
T54 | turn | INFERRED | fulltext lines 419-422; speaker: Analyst Dhanraj Tolani, Kuber Advisors (Q7)
T55 | turn | INFERRED,SPEAKER_UNCERTAIN | fulltext lines 423-432; speaker: Management respondent, speaker UNCERTAIN
T56 | turn | INFERRED | fulltext lines 433-435; speaker: Analyst Dhanraj Tolani (thanks)
T57 | turn | INFERRED | fulltext lines 436-438; speaker: Moderator (reminder, closes Q&A, hands to IR)
T58 | turn | INFERRED | fulltext lines 439-441; speaker: IR host (closing)
T59 | turn | INFERRED | fulltext lines 442-443; speaker: Moderator (conclusion)
T60 | turn | INFERRED,NO_CONTENT | fulltext lines 444; speaker: Residual "You" segment (no content)

Sections: T01-T07 prepared remarks (IR, Vice Chairman, CEO, CFO); T08-T57 Q&A; T58-T60 close. Q&A is 50 of 60 turns. Management turns with UNCERTAIN speaker: T10,T12,T16,T18,T20,T24,T26,T30,T36,T37,T42,T45,T47,T49,T51,T55.

## 3. QUESTION LEDGER (17 questions, 7 analysts)
Q | analyst, firm | topic | turn | A2 flags
Q1a | Vinny Jain, Jain Investments | strategic meaning of coal block; iron ore plus coal; cost position next few years | answered T10 | REPEAT_QUESTION (mines/coal; cf Q2c,Q6a)
Q1b | Vinny Jain | funding of medium-term growth plan: accruals vs debt and equity | answered T12 | REPEAT_QUESTION (funding; cf Q3c)
Q2a | Preeti Sharma, Inverse Force Advisors | sustainability of TMT price rise; October market read | answered T16 | REPEAT_QUESTION (price outlook; cf Q3a)
Q2b | Preeti Sharma | attribution of margin decline: shutdown vs input cost; H2 margin level | answered T18 | -
Q2c | Preeti Sharma | is Rs 2000 EBITDA benefit from captive iron ore right; ramp after FY28 | answered T20 | REPEAT_QUESTION (mines Rs2000/t; cf Q1a)
Q3a | Anirudh Sharma | net importer status; effect of imports on rebar price or demand | answered T24 | REPEAT_QUESTION (price/imports; cf Q2a)
Q3b | Anirudh Sharma | inventory rise of about 118 cores in H1; when working capital normalises | answered T26 | -
Q3c | Anirudh Sharma | full-year capex spend expected and how the balance is funded | answered T30-T32 | REPEAT_QUESTION (asked twice T27,T29; funding cf Q1b)
Q4a | Vedant Trivedi, Vinayat Capital | cost initiatives beyond mines and solar, e.g. digital, process | answered T36 | -
Q4b | Vedant Trivedi | question segment absent in ASR; answer at lines 321-326 is on brand premium | NOT_TRANSCRIBED | NOT_TRANSCRIBED
Q5a | Namesh Pandya | Gorakhpur ramp-up speed and utilization Q4 FY27, FY28 | answered T39 | REPEAT_QUESTION (utilization; cf Q6c)
Q5b | Namesh Pandya | power requirement still outsourced after 22 MW addition | answered T40 | -
Q5c | Namesh Pandya | rolling mill utilization: actions taken, where it settles | answered T42 | -
Q6a | jimma maitha, maitha investments | coal block next steps, approvals, share of coal needs met | answered T45 | REPEAT_QUESTION (coal block; cf Q1a)
Q6b | jimma maitha | South African coal imports; change from new coal block | answered T47 | -
Q6c | jimma maitha | guidance for coming years; utilization increase | answered T49,T51 | REPEAT_QUESTION (utilization/guidance; cf Q5a,Q7)
Q7 | Dhanraj Tolani, Kuber Advisors | Gujarat debottlenecking timing and benefits | answered T55 | -

## 4. MANAGEMENT NUMBERS (115 mgmt-spoken; header 7 and analyst-spoken 5 listed separately)

### 4a management-spoken numbers
ROW_ID | category | A2 flags | cross-ref / materiality note
R008 | mgmt_number | RESTATED | L63; xref R036
R009 | mgmt_number | RESTATED | L64; xref R037
R010 | mgmt_number | NO_FIGURE_STATED | L65; -
R011 | mgmt_number | - | L76; -
R012 | mgmt_number | - | L87; -
R013 | mgmt_number | RESTATED | L87; xref R019,R126 (1.23 vs 1.3 MT)
R014 | mgmt_number | ZERO_STANDING,RESTATED | L91; xref R034,R075
R015 | mgmt_number | RESTATED | L92; xref R033,R085,R103
R016 | mgmt_number | - | L125; -
R017 | mgmt_number | - | L125; -
R018 | mgmt_number | RESTATED | L128; xref R098; R093 says 20% (inconsistent)
R019 | mgmt_number | ASR_SUSPECT,RESTATED | L134; xref R013,R126
R020 | mgmt_number | SELF_CORRECTED_IN_SPEECH,RESTATED | L136; xref R022,R029,R104 (22 vs 18 MW solar)
R021 | mgmt_number | SELF_CORRECTED_IN_SPEECH | L136; -
R022 | mgmt_number | RESTATED | L136; xref R020,R117
R023 | mgmt_number | - | L137; -
R024 | mgmt_number | ASR_SUSPECT | L142; -
R025 | mgmt_number | ASR_SUSPECT | L142; -
R026 | mgmt_number | - | L143; -
R027 | mgmt_number | - | L143; -
R028 | mgmt_number | ASR_SUSPECT | L146; -
R029 | mgmt_number | RESTATED | L152; xref R104,R154
R030 | mgmt_number | RESTATED | L153; xref R119,R155
R031 | mgmt_number | ASR_SUSPECT,RESTATED | L154; xref R125,R184 (330-40 vs 30-40)
R032 | mgmt_number | RESTATED | L166; xref R094,R124,R188
R033 | mgmt_number | RESTATED | L168; xref R015,R085,R103
R034 | mgmt_number | ZERO_STANDING,RESTATED | L169; xref R014,R075
R035 | mgmt_number | RESTATED | L170; xref R082,R101
R036 | mgmt_number | RESTATED | L179; xref R008
R037 | mgmt_number | RESTATED | L179; xref R009
R038 | mgmt_number | - | L179; -
R039 | mgmt_number | - | L180; -
R040 | mgmt_number | - | L181; -
R041 | mgmt_number | - | L181; -
R042 | mgmt_number | RESTATED | L181; xref R252 (basis unstated)
R043 | mgmt_number | - | L182; -
R044 | mgmt_number | - | L182; -
R045 | mgmt_number | - | L182; -
R046 | mgmt_number | ASR_SUSPECT,RESTATED | L182; xref R066 (12.91% twice)
R047 | mgmt_number | ASR_SUSPECT | L183; -
R048 | mgmt_number | ASR_SUSPECT | L183; -
R049 | mgmt_number | ASR_SUSPECT | L185; -
R050 | mgmt_number | ASR_SUSPECT | L185; -
R051 | mgmt_number | - | L186; -
R052 | mgmt_number | - | L186; -
R053 | mgmt_number | - | L187; -
R054 | mgmt_number | - | L187; -
R055 | mgmt_number | - | L188; -
R056 | mgmt_number | - | L188; -
R057 | mgmt_number | - | L188; -
R058 | mgmt_number | - | L189; -
R059 | mgmt_number | - | L189; -
R060 | mgmt_number | - | L189; -
R061 | mgmt_number | ASR_SUSPECT | L191; -
R062 | mgmt_number | - | L191; -
R063 | mgmt_number | - | L191; -
R064 | mgmt_number | - | L192; -
R065 | mgmt_number | - | L192; -
R066 | mgmt_number | RESTATED | L192; xref R046
R067 | mgmt_number | - | L193; -
R068 | mgmt_number | - | L193; -
R069 | mgmt_number | - | L193; -
R070 | mgmt_number | - | L194; -
R071 | mgmt_number | ASR_SUSPECT | L194; -
R072 | mgmt_number | ASR_SUSPECT | L195; -
R073 | mgmt_number | - | L196; -
R074 | mgmt_number | - | L196; -
R075 | mgmt_number | ZERO_STANDING,RESTATED | L197; xref R014,R034
R076 | mgmt_number | - | L198; -
R077 | mgmt_number | - | L199; -
R078 | mgmt_number | - | L200; -
R079 | mgmt_number | - | L200; -
R080 | mgmt_number | - | L201; -
R081 | mgmt_number | - | L201; -
R082 | mgmt_number | RESTATED | L202; xref R035,R101
R083 | mgmt_number | - | L202; -
R084 | mgmt_number | ASR_SUSPECT,RESTATED | L203; xref R102 (650 vs 660)
R085 | mgmt_number | RESTATED | L203; xref R015,R033,R103
R086 | mgmt_number | - | L204; -
R087 | mgmt_number | ASR_SUSPECT | L225; -
R088 | mgmt_number | - | L268; -
R089 | mgmt_number | - | L269; -
R090 | mgmt_number | - | L269; -
R091 | mgmt_number | - | L270; -
R092 | mgmt_number | ASR_SUSPECT | L271; -
R093 | mgmt_number | RESTATED | L272; xref R018,R098,R263
R094 | mgmt_number | RESTATED | L276; xref R032,R124,R197
R095 | mgmt_number | - | L278; -
R096 | mgmt_number | - | L279; -
R097 | mgmt_number | - | L288; -
R098 | mgmt_number | RESTATED | L291; xref R018,R093
R100 | mgmt_number | - | L297; -
R104 | mgmt_number | ASR_SUSPECT,RESTATED | L302; xref R029 (22 vs 18)
R105 | mgmt_number | RESTATED | L307; xref R106,R202,R203
R106 | mgmt_number | RESTATED | L309; xref R105,R202
R107 | mgmt_number | - | L310; -
R108 | mgmt_number | ASR_SUSPECT | L311; -
R109 | mgmt_number | ASR_SUSPECT | L311; -
R110 | mgmt_number | ASR_SUSPECT | L311; -
R111 | mgmt_number | - | L339; -
R112 | mgmt_number | - | L340; -
R113 | mgmt_number | - | L342; -
R114 | mgmt_number | - | L350; -
R115 | mgmt_number | RESTATED | L350; xref R205,R206
R116 | mgmt_number | RESTATED | L351; xref R240
R118 | mgmt_number | - | L357; -
R119 | mgmt_number | RESTATED | L357; xref R030
R120 | mgmt_number | - | L358; -
R121 | mgmt_number | - | L358; -
R122 | mgmt_number | - | L377; -
R123 | mgmt_number | - | L379; -
R124 | mgmt_number | RESTATED | L390; xref R032,R094,R212
R125 | mgmt_number | RESTATED | L390; xref R031
R126 | mgmt_number | RESTATED | L392; xref R013,R019
R127 | mgmt_number | ASR_SUSPECT | L399; -

### 4b analyst-spoken numbers (not management)
ROW_ID | category | A2 flags | cross-ref / materiality note
R099 | analyst_number | ASR_SUSPECT | L292; -
R101 | analyst_number | RESTATED | L298; xref R035,R082
R102 | analyst_number | ASR_SUSPECT,RESTATED | L298; xref R084
R103 | analyst_number | RESTATED | L298; xref R015,R033,R085
R117 | analyst_number | - | L357; -

### 4c header metadata numbers
ROW_ID | category | A2 flags | cross-ref / materiality note
R001 | header_number | HEADER_METADATA | L19; -
R002 | header_number | HEADER_METADATA | L20; -
R003 | header_number | HEADER_METADATA | L20; -
R004 | header_number | HEADER_METADATA | L21; -
R005 | header_number | HEADER_METADATA | L22; -
R006 | header_number | HEADER_METADATA | L22; -
R007 | header_number | HEADER_METADATA | L22; -

Turn map (fulltext line to turn): L63-119 T05; L120-174 T06; L175-207 T07; L215-237 T09-T13; L250-281 T15-T21; L285-317 T23-T33; L321-342 T35-T38; L346-365 T39-T42; L374-399 T44-T52; L419-432 T54-T55.

## 5. FORWARD COMMITMENTS AND HEDGES

### 5a forward-commitment rows (45)
ROW_ID | category | A2 flags | cross-ref / materiality note
R172 | forward | - | L69; -
R173 | forward | - | L73; -
R174 | forward | - | L83; -
R175 | forward | - | L100; -
R176 | forward | - | L103; -
R177 | forward | - | L108; -
R178 | forward | - | L131; -
R179 | forward | ASR_SUSPECT | L144; -
R180 | forward | - | L146; -
R181 | forward | - | L150; -
R182 | forward | ASR_SUSPECT | L152; -
R183 | forward | - | L153; -
R184 | forward | ASR_SUSPECT | L154; -
R185 | forward | - | L155; -
R186 | forward | - | L157; -
R187 | forward | - | L161; -
R188 | forward | - | L165; -
R189 | forward | - | L168; -
R190 | forward | - | L172; -
R191 | forward | - | L205; -
R192 | forward | - | L221; -
R193 | forward | - | L228; -
R194 | forward | - | L256; -
R195 | forward | - | L265; -
R196 | forward | - | L273; -
R197 | forward | - | L276; -
R198 | forward | - | L278; -
R199 | forward | - | L293; -
R200 | forward | - | L297; -
R201 | forward | - | L302; -
R202 | forward | - | L307; -
R203 | forward | ASR_SUSPECT | L311; -
R204 | forward | - | L337; -
R205 | forward | - | L350; -
R206 | forward | - | L352; -
R207 | forward | - | L355; -
R208 | forward | - | L357; -
R209 | forward | ASR_SUSPECT | L364; -
R210 | forward | - | L378; -
R211 | forward | - | L383; -
R212 | forward | - | L389; -
R213 | forward | - | L397; -
R214 | forward | - | L398; -
R215 | forward | - | L425; -
R216 | forward | - | L428; -

### 5b qualifier / hedge rows (19)
ROW_ID | category | A2 flags | cross-ref / materiality note
R245 | qualifier | - | L18; -
R246 | qualifier | - | L22; -
R247 | qualifier | - | L23; -
R248 | qualifier | - | L24; -
R249 | qualifier | - | L20; -
R250 | qualifier | - | L41; -
R251 | qualifier | - | L136; -
R252 | qualifier | BASIS_UNSTATED | L181; -
R253 | qualifier | - | L196; -
R254 | qualifier | - | L199; -
R255 | qualifier | - | L203; -
R256 | qualifier | - | L312; -
R257 | qualifier | - | L352; -
R258 | qualifier | - | L269; -
R259 | qualifier | - | L279; -
R260 | qualifier | - | L324; -
R261 | qualifier | - | L333; -
R262 | qualifier | - | L103; -
R263 | qualifier | - | L272; -

## 6. ENTITIES (44)

### entities
ROW_ID | category | A2 flags | cross-ref / materiality note
R128 | entity | ASR_VARIANT | L18; -
R129 | entity | - | L19; -
R130 | entity | - | L20; -
R131 | entity | - | L21; -
R132 | entity | - | L22; -
R133 | entity | - | L32; -
R134 | entity | - | L33; -
R135 | entity | ASR_VARIANT | L32; -
R136 | entity | ASR_VARIANT | L36; -
R137 | entity | - | L37; -
R138 | entity | - | L37; -
R139 | entity | ASR_VARIANT | L46; -
R140 | entity | - | L51; -
R141 | entity | - | L54; -
R142 | entity | - | L54; -
R143 | entity | ASR_VARIANT | L78; -
R144 | entity | - | L80; -
R145 | entity | - | L88; -
R146 | entity | - | L135; -
R147 | entity | ASR_VARIANT | L130; -
R148 | entity | - | L137; -
R149 | entity | ASR_VARIANT | L142; -
R150 | entity | ASR_VARIANT | L146; -
R151 | entity | - | L146; -
R152 | entity | ASR_VARIANT | L146; -
R153 | entity | ASR_VARIANT | L149; -
R154 | entity | - | L152; -
R155 | entity | - | L153; -
R156 | entity | ASR_VARIANT | L135; -
R157 | entity | - | L304; -
R158 | entity | - | L325; -
R159 | entity | - | L326; -
R160 | entity | - | L329; -
R161 | entity | - | L357; -
R162 | entity | - | L381; -
R163 | entity | ASR_VARIANT | L426; -
R164 | entity | - | L214; -
R165 | entity | ASR_VARIANT | L244; -
R166 | entity | ASR_VARIANT | L282; -
R167 | entity | ASR_VARIANT | L318; -
R168 | entity | ASR_VARIANT | L345; -
R169 | entity | ASR_VARIANT | L367; -
R170 | entity | - | L403; -
R171 | entity | ASR_VARIANT | L438; -

## 7. DATES (28)

### dates
ROW_ID | category | A2 flags | cross-ref / materiality note
R217 | date | - | L20; -
R218 | date | - | L22; -
R219 | date | - | L21; -
R220 | date | - | L26; -
R221 | date | - | L48; -
R222 | date | - | L73; -
R223 | date | - | L79; -
R224 | date | - | L109; -
R225 | date | ASR_SUSPECT | L144; -
R226 | date | ASR_SUSPECT | L152; -
R227 | date | - | L153; -
R228 | date | - | L157; -
R229 | date | - | L180; -
R230 | date | - | L182; -
R231 | date | - | L192; -
R232 | date | - | L195; -
R233 | date | - | L196; -
R234 | date | - | L204; -
R235 | date | - | L205; -
R236 | date | - | L205; -
R237 | date | ASR_SUSPECT | L225; -
R238 | date | - | L256; -
R239 | date | - | L265; -
R240 | date | - | L351; -
R241 | date | - | L352; -
R242 | date | - | L376; -
R243 | date | - | L428; -
R244 | date | - | L432; -

## 8. ZERO_STANDING (3)
R014 | zero_standing | ZERO_STANDING | no term loans (opening, T05)
R034 | zero_standing | ZERO_STANDING | no term loans (CEO capex, T06)
R075 | zero_standing | ZERO_STANDING | no term loan (CFO, T07)
Same zero-term-loan statement three times; matching forward rows R189, R193.

## 9. A2 INDEPENDENT FLAGS (no MISSING_FROM_STRUCTURED found)
- MGMT_ABSENCE: none. DROPPED_SLIDE, ENTITY_CHANGE: n/a (no prior ledger; not a deck).
- Internal-inconsistency clusters for A3: capacity 1.23 vs 1.3 MT (R013,R019,R126); solar MW 18/22 (R020,R029,R104,R117); capex spent 650 vs 660 (R084,R102); remaining-capex split 400+240+170+100=910 vs 500 (R105-R110,R202,R203); savings 330-40 vs 30-40 (R031,R125,R184,R212); price rise 20 vs 21 (R018,R093,R098,R263); Q2 FY26 EBITDA 135/1113=12.1% vs spoken 12.91% (R045,R046; 12.91% also H1 FY27, R066).
- Arithmetic seeds: Q2 FY27 EBITDA 111 / revenue 1146 = 9.69% vs spoken 9.64% (R041,R042,R036); basis with/without other income 18 unstated (R252). Revenue spoken 1146 for both Q2 and Q1 FY27 (R036,R039); H1 2292 = 2 x 1146 (R063), consistent with Q1 = Q2.
- Q4b question not transcribed; its answer (brand premium R112,R113) sits in T37.

```yaml
stage: A2-enumerator
company: "GALLANTT"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/gallantt-q2fy27/work/ledger_concall_gallantt_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 3
  agenda_items: 0
  auditor_paras: 0
  entities: 44
  turns: 60
  questions: 17
  mgmt_numbers: 115
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, REPEAT_QUESTION, RESTATED, ASR_SUSPECT, ASR_VARIANT, SPEAKER_UNCERTAIN, QUESTION_NOT_TRANSCRIBED, BASIS_UNSTATED]
ids_in_structured: 263
ids_referenced: 263
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "All 263 R rows, 60 turns and 17 questions accounted for; no orphans. 115 management numbers = 127 NUMBER rows minus 7 header and 5 analyst-spoken (R099,R101,R102,R103,R117). Zero-term-loan stated three times (R014,R034,R075). Seven inconsistency clusters flagged for A3 (capacity 1.23/1.3, solar 18/22 MW, capex 650/660, remaining capex split 910 vs 500, savings 330-40/30-40, price rise 20/21, Q2 FY26 EBITDA margin). A2 arithmetic seeds: 111/1146 = 9.69% vs spoken 9.64%; EBITDA basis vs other income unstated. 16 of 24 management Q&A turns have uncertain speaker, so commitment ownership (CEO vs Vice Chairman) is unresolved. Q4b question not transcribed."
```
