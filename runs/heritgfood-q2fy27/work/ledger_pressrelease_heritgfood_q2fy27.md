=== A2 COUNT TEST ===
category: slides(pages)       grep_count: 5    sweep_count: 5    match: yes   (page anchors p1-p5 in structured; press release, no slide deck)
category: numbers             grep_count: 117  sweep_count: 117  match: yes   (header NUMBER 117)
category: entities            grep_count: 27   sweep_count: 27   match: yes   (header ENTITY 27)
category: entity_summaries    grep_count: 3    sweep_count: 3    match: yes
category: forward             grep_count: 8    sweep_count: 8    match: yes
category: dates               grep_count: 12   sweep_count: 12   match: yes
category: qualifiers          grep_count: 13   sweep_count: 13   match: yes
category: line_items(tables)  grep_count: 0    sweep_count: 0    match: yes   (no financial tables; headline metrics captured as NUMBER rows)
category: zero_standing       grep_count: 0    sweep_count: 0    match: yes   (no nil/dash rows; no tables)
category: footnotes           grep_count: 0    sweep_count: 0    match: yes   (R174 records none; R175 LLPD undefined)
total_ids                     grep_count: 180  sweep_count: 180  match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 180 | ids_referenced_in_ledger: 180 | orphan_ids: [] | match: yes

DROPPED_SLIDE: not assessable (no prior-quarter ledger, ND). MGMT_ABSENCE / ENTITY_CHANGE: not assessable (no prior list; no call).
Page map: p1 cover letter (R001-R004,R118-R122,R145,R148,R156-R159,R168-R169); p2 press-release top, procurement, milk, VAP, Q2 table (R005-R048); p3 H1 table, segment metrics, subsidiaries (R049-R105); p4 wind farm, commentary, call details (R106-R111); p5 about/contact (R112-R117).


## slide_numbers (page-anchored number)
ROW_ID | page/line | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R001 | p1 L23 | NUMBER | - | -
R002 | p1 L27 | NUMBER | - | -
R003 | p1 L29 | NUMBER | RESTATED | also R011
R004 | p1 L54 | NUMBER | - | -
R005 | p2 L63 | NUMBER | RESTATED | also R039,R059,R108
R006 | p2 L64 | NUMBER | RESTATED | also R047,R109
R007 | p2 L64 | NUMBER | RESTATED | also R037,R110
R008 | p2 L65 | NUMBER | - | -
R009 | p2 L65 | NUMBER | RESTATED | also R083
R010 | p2 L65 | NUMBER | RESTATED | also R085
R011 | p2 L66 | NUMBER | RESTATED | also R003
R012 | p2 L72 | NUMBER | RESTATED | also R064
R013 | p2 L72 | NUMBER | RESTATED | also R066
R014 | p2 L76 | NUMBER | RESTATED | also R068
R015 | p2 L76 | NUMBER | RESTATED | also R067
R016 | p2 L77 | NUMBER | - | -
R017 | p2 L81 | NUMBER | - | -
R018 | p2 L82 | NUMBER | RESTATED | also R072
R019 | p2 L83 | NUMBER | RESTATED | also R076
R020 | p2 L84 | NUMBER | RESTATED | also R075
R021 | p2 L86 | NUMBER | - | -
R022 | p2 L86 | NUMBER | - | -
R023 | p2 L87 | NUMBER | - | -
R024 | p2 L87 | NUMBER | - | -
R025 | p2 L87 | NUMBER | - | -
R026 | p2 L89 | NUMBER | - | -
R027 | p2 L89 | NUMBER | - | -
R028 | p2 L90 | NUMBER | - | -
R029 | p2 L90 | NUMBER | - | -
R030 | p2 L90 | NUMBER | - | -
R031 | p2 L92 | NUMBER | - | -
R032 | p2 L93 | NUMBER | - | -
R033 | p2 L94 | NUMBER | - | -
R034 | p2 L100 | NUMBER | RESTATED | also R060
R035 | p2 L100 | NUMBER | - | -
R036 | p2 L100 | NUMBER | - | -
R037 | p2 L100 | NUMBER | RESTATED | also R007,R110
R038 | p2 L100 | NUMBER | - | -
R039 | p2 L101 | NUMBER | RESTATED | also R005,R059,R108
R040 | p2 L101 | NUMBER | - | material: gross margin -271 bps YoY
R041 | p2 L101 | NUMBER | - | -
R042 | p2 L101 | NUMBER | - | material: EBITDA margin -133 bps YoY
R043 | p2 L101 | NUMBER | - | material: PAT -39% YoY
R044 | p2 L102 | NUMBER | - | -
R045 | p2 L102 | NUMBER | - | -
R046 | p2 L102 | NUMBER | - | EBITDA QoQ shown unsigned (20%); positive implied, ties to R051-R036
R047 | p2 L102 | NUMBER | RESTATED | also R006,R109
R048 | p2 L102 | NUMBER | - | -
R049 | p3 L110 | NUMBER | RESTATED | also R062
R050 | p3 L110 | NUMBER | - | -
R051 | p3 L110 | NUMBER | - | -
R052 | p3 L110 | NUMBER | - | -
R053 | p3 L110 | NUMBER | - | -
R054 | p3 L111 | NUMBER | RESTATED | also R061
R055 | p3 L111 | NUMBER | - | -
R056 | p3 L111 | NUMBER | - | -
R057 | p3 L111 | NUMBER | - | -
R058 | p3 L111 | NUMBER | - | -
R059 | p3 L117 | NUMBER | RESTATED | also R005,R039,R108
R060 | p3 L117 | NUMBER | RESTATED | also R034
R061 | p3 L118 | NUMBER | RESTATED | also R054
R062 | p3 L118 | NUMBER | RESTATED | also R049
R063 | p3 L121 | NUMBER | - | -
R064 | p3 L121 | NUMBER | RESTATED | also R012
R065 | p3 L122 | NUMBER | - | -
R066 | p3 L122 | NUMBER | RESTATED | also R013
R067 | p3 L122 | NUMBER | RESTATED | also R015
R068 | p3 L122 | NUMBER | RESTATED | also R014
R069 | p3 L123 | NUMBER | - | -
R070 | p3 L123 | NUMBER | - | -
R071 | p3 L126 | NUMBER | - | -
R072 | p3 L126 | NUMBER | RESTATED | also R018
R073 | p3 L127 | NUMBER | - | -
R074 | p3 L127 | NUMBER | - | -
R075 | p3 L127 | NUMBER | RESTATED | also R020
R076 | p3 L127 | NUMBER | RESTATED | also R019
R077 | p3 L128 | NUMBER | - | -
R078 | p3 L128 | NUMBER | - | -
R079 | p3 L130 | NUMBER | - | -
R080 | p3 L131 | NUMBER | - | -
R081 | p3 L131 | NUMBER | - | -
R082 | p3 L131 | NUMBER | - | -
R083 | p3 L132 | NUMBER | RESTATED | also R009
R084 | p3 L132 | NUMBER | - | -
R085 | p3 L132 | NUMBER | RESTATED | also R010
R086 | p3 L133 | NUMBER | - | -
R087 | p3 L135 | NUMBER | - | -
R088 | p3 L136 | NUMBER | - | -
R089 | p3 L136 | NUMBER | - | -
R090 | p3 L136 | NUMBER | - | -
R091 | p3 L137 | NUMBER | - | -
R092 | p3 L137 | NUMBER | - | -
R093 | p3 L138 | NUMBER | - | -
R094 | p3 L138 | NUMBER | - | -
R095 | p3 L142 | NUMBER | - | -
R096 | p3 L143 | NUMBER | - | -
R097 | p3 L143 | NUMBER | - | -
R098 | p3 L143 | NUMBER | - | -
R099 | p3 L144 | NUMBER | - | -
R100 | p3 L144 | NUMBER | - | -
R101 | p3 L146 | NUMBER | - | -
R102 | p3 L147 | NUMBER | - | -
R103 | p3 L150 | NUMBER | - | -
R104 | p3 L151 | NUMBER | - | -
R105 | p3 L151 | NUMBER | - | -
R106 | p4 L162 | NUMBER | - | -
R107 | p4 L162 | NUMBER | - | -
R108 | p4 L170 | NUMBER | RESTATED | also R005,R039,R059
R109 | p4 L171 | NUMBER | RESTATED | also R006,R047
R110 | p4 L171 | NUMBER | RESTATED | also R007,R037
R111 | p4 L194 | NUMBER | - | dial-in
R112 | p5 L202 | NUMBER | RESTATED | also R167
R113 | p5 L205 | NUMBER | - | -
R114 | p5 L211 | NUMBER | - | -
R115 | p5 L212 | NUMBER | - | -
R116 | p5 L224 | NUMBER | - | -
R117 | p5 L224 | NUMBER | - | -

## entities (named)
ROW_ID | page/line | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R118 | p1 L23 | ENTITY | - | -
R119 | p1 L26 | ENTITY | - | -
R120 | p1 L29 | ENTITY | - | -
R121 | p1 L39 | ENTITY | - | -
R122 | p1 L52 | ENTITY | RESTATED | also R144
R123 | p2 L63 | ENTITY | - | -
R124 | p2 L86 | ENTITY | - | -
R125 | p2 L86 | ENTITY | - | -
R126 | p2 L87 | ENTITY | - | -
R127 | p2 L87 | ENTITY | - | -
R128 | p2 L87 | ENTITY | - | -
R129 | p2 L92 | ENTITY | - | -
R130 | p2 L93 | ENTITY | - | -
R131 | p3 L135 | ENTITY | - | -
R132 | p3 L135 | ENTITY | - | -
R133 | p3 L142 | ENTITY | - | -
R134 | p3 L146 | ENTITY | - | -
R135 | p3 L147 | ENTITY | - | -
R136 | p3 L150 | ENTITY | - | -
R137 | p3 L151 | ENTITY | - | -
R138 | p4 L158 | ENTITY | - | -
R139 | p4 L159 | ENTITY | - | -
R140 | p4 L162 | ENTITY | - | -
R141 | p4 L163 | ENTITY | - | -
R142 | p4 L169 | ENTITY | - | -
R143 | p5 L224 | ENTITY | - | -
R144 | p5 L224 | ENTITY | RESTATED | also R122

## entities (block summary)
ROW_ID | page/line | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R145 | p1 L23 | ENTITY-SUMMARY | - | -
R146 | p5 L202 | ENTITY-SUMMARY | - | -
R147 | p5 L224 | ENTITY-SUMMARY | - | -

## forward_statements
ROW_ID | page/line | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R148 | p1 L39 | FORWARD | - | administrative, not business forward
R149 | p2 L73 | FORWARD | - | -
R150 | p4 L175 | FORWARD | - | no numeric target
R151 | p4 L177 | FORWARD | - | no numeric target
R152 | p4 L180 | FORWARD | - | margin-improvement claim, no numeric target
R153 | p4 L182 | FORWARD | - | -
R154 | p4 L191 | FORWARD | RESTATED | also R166; call 16 Oct; release dated 15 Oct
R155 | p4 L195 | FORWARD | - | -

## dates
ROW_ID | page/line | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R156 | p1 L19 | DATE | - | -
R157 | p1 L20 | DATE | RESTATED | also R160
R158 | p1 L31 | DATE | RESTATED | also R161,R168
R159 | p1 L49 | DATE | RESTATED | also R169; signature 15:26 on 15 Oct; board meeting times not given in release
R160 | p2 L66 | DATE | RESTATED | also R157
R161 | p2 L66 | DATE | RESTATED | also R158
R162 | p2 L77 | DATE | - | -
R163 | p2 L99 | DATE | - | -
R164 | p3 L107 | DATE | - | -
R165 | p4 L163 | DATE | - | -
R166 | p4 L191 | DATE | RESTATED | also R154
R167 | p5 L202 | DATE | RESTATED | also R112

## qualifiers_footnotes
ROW_ID | page/line | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R168 | p1 L31 | QUALIFIER | RESTATED | also R158; results unaudited
R169 | p1 L45 | QUALIFIER | RESTATED | also R159
R170 | p2 L76 | QUALIFIER | - | -
R171 | p2 L100 | QUALIFIER | - | -
R172 | p2 L101 | QUALIFIER | - | -
R173 | p3 L107 | QUALIFIER | - | consolidated basis
R174 | p3 L110 | QUALIFIER | - | absence note: no footnotes in release
R175 | p3 L121 | QUALIFIER | FOOTNOTE_UNRESOLVED | FOOTNOTE_UNRESOLVED: LLPD not defined in release
R176 | p3 L127 | QUALIFIER | - | -
R177 | p3 L130 | QUALIFIER | - | -
R178 | p3 L132 | QUALIFIER | - | -
R179 | p3 L135 | QUALIFIER | - | -
R180 | p4 L187 | QUALIFIER | - | segment results not in release; on website
