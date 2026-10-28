=== A2 COUNT TEST ===
category: structured_rows    grep_count: 492   sweep_count: 492   match: yes
category: mgmt_numbers   header_count: 206  sweep_count: 206  match: yes
category: entities       header_count: 72  sweep_count: 72  match: yes
category: forward        header_count: 74  sweep_count: 74  match: yes
category: dates          header_count: 29  sweep_count: 29  match: yes
category: qualifiers     header_count: 90  sweep_count: 90  match: yes
category: questions      header_count: 21  sweep_count: 21  match: yes
category: mechanical_sweep_of_fulltext: 270 body lines with numeric/forward tokens; 261 covered by a structured row within +-1 line; 9 lines uncovered, 5 of them real units (see MFS)
category: turns  structured_boundaries: 21 QUESTION rows + opening + closing  sweep_count: 45 (APPROXIMATE, ASR untagged)  match: yes
MFS_count: 5 (below 15 loop threshold)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 492 | ids_referenced_in_ledger: 492 | orphan_ids: [] | match: yes
zero_standing: 0 (concall; no standing financial table). No nil/zero-valued rows found.

TURN NOTE: ASR transcript has no speaker tags. Turn = boundary derived from QUESTION rows: T1 moderator intro, T2 prepared remarks (P. Ramakrishnan), then analyst turn (odd, 3..43) and management answer turn (even, 4..44) per QUESTION row, T45 closing. Multi-part questions (Q2-Q5, Q7, Q8) may be one analyst turn in reality; turn numbers are approximate. Q&A turns 3-44 of 45; prepared remarks begin ~line 28, first question line 345, so Q&A is roughly 504 of 849 lines.

## MGMT PARTICIPANTS (both sides)
Management: R008/R491 P. Ramakrishnan (opening and closing); R015 Subram Sharma, Dy MD and President (Q&A, R284 "Mr. Sharma"); R010 moderator Sagar. No CMD/CEO named in any row. MGMT_ABSENCE: Chairman/MD not named as a speaker anywhere in the structured file (ASR untagged, so absence cannot be confirmed from audio).
Analysts: Aditya Vartiya (Investech) R282,R294; Mohith Pandey (Citi) R299,R310,R317; Puneet Gulati (heard Asia's PC) R323,R330,R333,R344,R368; unnamed Axis Capital R373,R386; Rahul Bajare (Macquarie) R398,R413,R421,R431; Atul Devari (JP Morgan) R442; Hamid Anwani (PL Capital) R449,R457; Aditya Mongia (Kotak) R469,R481. 8 analysts, 21 questions.

## questions (21)
ROW_ID | category | turn | page/line | A2 flags | note
R282 | questions | T3 | p3/L345 | - | Q1 firm Investech
R294 | questions | T5 | p4/L377 | - | Q1 follow-up
R299 | questions | T7 | p4/L398 | - | Q2 firm Citi
R310 | questions | T9 | p4/L420 | - | Q2 part 2
R317 | questions | T11 | p4/L432 | REPEAT_QUESTION(with R421 DAC/precision engineering) | Q2 part 3
R323 | questions | T13 | p4/L451 | - | Q3 firm heard Asia's PC
R330 | questions | T15 | p4/L473 | - | Q3 follow-up
R333 | questions | T17 | p5/L482 | REPEAT_QUESTION(with R373 working capital) | Q3 working capital
R344 | questions | T19 | p5/L500 | - | Q3 capex
R368 | questions | T21 | p5/L529 | - | Q3 part 4
R373 | questions | T23 | p5/L540 | REPEAT_QUESTION(with R333 working capital) | Q4 firm Axis Capital heard
R386 | questions | T25 | p5/L574 | REPEAT_QUESTION(with R431,R442 Middle East logistics) | Q4 follow-up
R398 | questions | T27 | p5/L605 | - | Q5 firm Macquarie
R413 | questions | T29 | p6/L624 | - | Q5 part 2
R421 | questions | T31 | p6/L636 | REPEAT_QUESTION(with R317 DAC/precision engineering) | Q5 part 3
R431 | questions | T33 | p6/L657 | REPEAT_QUESTION(with R386,R442 Middle East logistics/Hormuz) | Q5 part 4
R442 | questions | T35 | p6/L686 | REPEAT_QUESTION(with R386,R431 Middle East logistics/Hormuz) | Q6 firm JP Morgan heard
R449 | questions | T37 | p6/L713 | - | Q7 firm PL Capital
R457 | questions | T39 | p6/L747 | - | Q7 part 2
R469 | questions | T41 | p7/L774 | - | Q8 firm Kotak
R481 | questions | T43 | p7/L816 | - | Q8 part 2

## mgmt_numbers (206)
ROW_ID | category | turn | page/line | A2 flags | note
R002 | mgmt_numbers | T1 | p1/L21 | ASR_UNVERIFIED | source audio duration
R006 | mgmt_numbers | T1 | p1/L27 | ASR_UNVERIFIED | operator assistance keypress
R012 | mgmt_numbers | T2 | p1/L33 | ASR_UNVERIFIED | presentation upload timing before call
R014 | mgmt_numbers | T2 | p1/L36 | ASR_UNVERIFIED | prepared remarks duration
R018 | mgmt_numbers | T2 | p1/L45 | ASR_UNVERIFIED | location of detailed disclaimer
R026 | mgmt_numbers | T2 | p1/L65 | ASR_UNVERIFIED | contractors selected under PDO framework
R027 | mgmt_numbers | T2 | p1/L67 | ASR_UNVERIFIED | PDO EPC framework agreement term
R037 | mgmt_numbers | T2 | p1/L81 | ASR_UNVERIFIED | planned NVIDIA B300 GPUs
R044 | mgmt_numbers | T2 | p1/L93 | ASR_UNVERIFIED | semiconductor products and platforms unveiled
R046 | mgmt_numbers | T2 | p1/L94 | ASR_UNVERIFIED | silicon carbide MOSFET platform voltage
R066 | mgmt_numbers | T2 | p1/L114 | ASR_UNVERIFIED | group order inflow Q2FY27 highest ever quarterly
R067 | mgmt_numbers | T2 | p1/L114 | ASR_UNVERIFIED | group order inflow growth Q2
R071 | mgmt_numbers | T2 | p1/L117 | ASR_UNVERIFIED | PPM order inflow Q2FY27 record
R072 | mgmt_numbers | T2 | p1/L118 | ASR_UNVERIFIED | PPM order inflow growth Q2
R073 | mgmt_numbers | T2 | p1/L119 | ASR_UNVERIFIED | domestic order inflow growth rate
R074 | mgmt_numbers | T2 | p1/L120 | ASR_UNVERIFIED | international order inflow growth rate
R075 | mgmt_numbers | T2 | p1/L120 | ASR_UNVERIFIED | international share of PPM portfolio mix Q2FY27
R076 | mgmt_numbers | T2 | p1/L121 | ASR_UNVERIFIED | international share corresponding quarter prior year
R078 | mgmt_numbers | T2 | p1/L123 | ASR_UNVERIFIED | PPM core prospects pipeline balance six months FY27
R079 | mgmt_numbers | T2 | p1/L123 | ASR_UNVERIFIED | pipeline horizon
R081 | mgmt_numbers | T2 | p1/L125 | ASR_UNVERIFIED | infrastructure utilities prospects
R082 | mgmt_numbers | T2 | p1/L126 | ASR_UNVERIFIED | infrastructure utilities prospects last year
R083 | mgmt_numbers | T2 | p1/L127 | ASR_UNVERIFIED | energy conventional prospects
R084 | mgmt_numbers | T2 | p1/L127 | ASR_UNVERIFIED | energy conventional prospects last year
R085 | mgmt_numbers | T2 | p1/L128 | ASR_UNVERIFIED | energy green prospects
R086 | mgmt_numbers | T2 | p1/L128 | ASR_UNVERIFIED | energy green prospects last year
R087 | mgmt_numbers | T2 | p1/L129 | ASR_UNVERIFIED | manufacturing and products prospects
R088 | mgmt_numbers | T2 | p1/L129 | ASR_UNVERIFIED | manufacturing and products prospects last year
R089 | mgmt_numbers | T2 | p1/L130 | ASR_UNVERIFIED | total order book as on September 26 including realty segment
R092 | mgmt_numbers | T2 | p1/L131 | ASR_UNVERIFIED | order book growth vs September 25
R094 | mgmt_numbers | T2 | p1/L131 | ASR_UNVERIFIED | order book share infrastructure utilities
R095 | mgmt_numbers | T2 | p1/L132 | ASR_UNVERIFIED | order book share energy conventional
R096 | mgmt_numbers | T2 | p1/L132 | ASR_UNVERIFIED | order book share energy green
R097 | mgmt_numbers | T2 | p1/L133 | ASR_UNVERIFIED | order book share manufacturing and products
R098 | mgmt_numbers | T2 | p1/L133 | ASR_UNVERIFIED | order book share realty
R099 | mgmt_numbers | T2 | p1/L134 | ASR_UNVERIFIED | order book domestic share
R100 | mgmt_numbers | T2 | p1/L134 | ASR_UNVERIFIED | order book international share
R101 | mgmt_numbers | T2 | p1/L136 | ASR_UNVERIFIED | average execution period of order book
R102 | mgmt_numbers | T2 | p1/L137 | ASR_UNVERIFIED | total domestic PPM order book
R103 | mgmt_numbers | T2 | p1/L138 | ASR_UNVERIFIED | heard as share of private sector orders increased by (ASR garbled)
R104 | mgmt_numbers | T2 | p2/L140 | ASR_UNVERIFIED | private sector share domestic PPM order book Sept 2026
R105 | mgmt_numbers | T2 | p2/L140 | ASR_UNVERIFIED | private sector share domestic PPM order book Sept 2025
R106 | mgmt_numbers | T2 | p2/L144 | ASR_UNVERIFIED | central plus state government share of domestic order book
R107 | mgmt_numbers | T2 | p2/L145 | ASR_UNVERIFIED | central government share of domestic order book
R108 | mgmt_numbers | T2 | p2/L146 | ASR_UNVERIFIED | state government share of domestic order book
R109 | mgmt_numbers | T2 | p2/L146 | ASR_UNVERIFIED | central plus state government share a year ago
R110 | mgmt_numbers | T2 | p2/L147 | ASR_UNVERIFIED | PSU exposure largely stable (unit not heard)
R111 | mgmt_numbers | T2 | p2/L148 | ASR_UNVERIFIED | international order book
R112 | mgmt_numbers | T2 | p2/L148 | ASR_UNVERIFIED | Middle East share of international order book
R113 | mgmt_numbers | T2 | p2/L150 | ASR_UNVERIFIED | Europe share of international order book
R114 | mgmt_numbers | T2 | p2/L151 | ASR_UNVERIFIED | balance share other international markets
R116 | mgmt_numbers | T2 | p2/L152 | ASR_UNVERIFIED | share of total order book funded via bilateral and multilateral agenci
R117 | mgmt_numbers | T2 | p2/L153 | ASR_UNVERIFIED | slow moving orders share of overall order book Sept 2026
R118 | mgmt_numbers | T2 | p2/L155 | ASR_UNVERIFIED | orders deleted during quarter
R119 | mgmt_numbers | T2 | p2/L158 | ASR_UNVERIFIED | group revenue Q2FY27 (heard)
R120 | mgmt_numbers | T2 | p2/L158 | ASR_UNVERIFIED | group revenue growth Q2
R121 | mgmt_numbers | T2 | p2/L159 | ASR_UNVERIFIED | heard as revenue share in total (ASR; likely international share)
R123 | mgmt_numbers | T2 | p2/L160 | ASR_UNVERIFIED | PPM portfolio revenue Q2FY27
R124 | mgmt_numbers | T2 | p2/L160 | ASR_UNVERIFIED | PPM revenue growth Q2
R127 | mgmt_numbers | T2 | p2/L165 | ASR_UNVERIFIED | group EBITDA margin excluding other income Q2FY27
R129 | mgmt_numbers | T2 | p2/L166 | ASR_UNVERIFIED | group EBITDA margin excluding other income Q2FY26
R131 | mgmt_numbers | T2 | p2/L169 | ASR_UNVERIFIED | PPM EBITDA margin Q2FY27 (heard Evita/AVIDTA)
R132 | mgmt_numbers | T2 | p2/L169 | ASR_UNVERIFIED | PPM margin decline YoY
R135 | mgmt_numbers | T2 | p2/L173 | ASR_UNVERIFIED | group PAT Q2FY27
R136 | mgmt_numbers | T2 | p2/L173 | ASR_UNVERIFIED | group PAT growth Q2
R140 | mgmt_numbers | T2 | p2/L182 | ASR_UNVERIFIED | group NWC percentage record low Sept 2026
R142 | mgmt_numbers | T2 | p2/L183 | ASR_UNVERIFIED | group NWC percentage March 26
R143 | mgmt_numbers | T2 | p2/L184 | ASR_UNVERIFIED | gross working capital percentage March 26
R144 | mgmt_numbers | T2 | p2/L185 | ASR_UNVERIFIED | gross working capital percentage September 26
R146 | mgmt_numbers | T2 | p2/L187 | ASR_UNVERIFIED | group collections excluding financial services Q2FY27
R148 | mgmt_numbers | T2 | p2/L188 | ASR_UNVERIFIED | group collections excluding financial services Q2FY26
R149 | mgmt_numbers | T2 | p2/L189 | ASR_UNVERIFIED | cash flow from operations excluding financial services Q2FY27
R151 | mgmt_numbers | T2 | p2/L190 | ASR_UNVERIFIED | cash flow from operations excluding financial services Q2FY26
R153 | mgmt_numbers | T2 | p2/L193 | ASR_UNVERIFIED | trailing 12-month ROE Q2FY27 (percent not heard)
R155 | mgmt_numbers | T2 | p2/L193 | ASR_UNVERIFIED | trailing 12-month ROE Q2FY26 (percent not heard)
R158 | mgmt_numbers | T2 | p2/L199 | ASR_UNVERIFIED | infrastructure and utility segment order inflow Q2FY27
R159 | mgmt_numbers | T2 | p2/L199 | ASR_UNVERIFIED | infra and utility order inflow decline
R162 | mgmt_numbers | T2 | p2/L203 | ASR_UNVERIFIED | private sector share of domestic ordering flows infra segment
R164 | mgmt_numbers | T2 | p2/L205 | ASR_UNVERIFIED | infra segment order book Sept 2026
R165 | mgmt_numbers | T2 | p2/L206 | ASR_UNVERIFIED | infra segment average execution cycle
R166 | mgmt_numbers | T2 | p2/L207 | ASR_UNVERIFIED | infra utilities prospects remaining six months
R168 | mgmt_numbers | T2 | p2/L208 | ASR_UNVERIFIED | infra domestic prospects
R169 | mgmt_numbers | T2 | p2/L209 | ASR_UNVERIFIED | infra international prospects
R170 | mgmt_numbers | T2 | p2/L210 | ASR_UNVERIFIED | infra prospects share transportation infra
R171 | mgmt_numbers | T2 | p2/L210 | ASR_UNVERIFIED | infra prospects share heavy civil infra
R172 | mgmt_numbers | T2 | p2/L211 | ASR_UNVERIFIED | infra prospects share buildings and factories
R173 | mgmt_numbers | T2 | p2/L211 | ASR_UNVERIFIED | infra prospects share power transmission distribution
R174 | mgmt_numbers | T2 | p2/L212 | ASR_UNVERIFIED | infra prospects share metals and minerals
R175 | mgmt_numbers | T2 | p2/L212 | ASR_UNVERIFIED | infra prospects share water and effluent treatment
R176 | mgmt_numbers | T2 | p2/L212 | ASR_UNVERIFIED | infra segment revenue growth Q2
R179 | mgmt_numbers | T2 | p2/L219 | ASR_UNVERIFIED | infra and utility EBITDA margin Q2FY27
R180 | mgmt_numbers | T2 | p2/L219 | ASR_UNVERIFIED | infra and utility EBITDA margin Q2FY26
R183 | mgmt_numbers | T2 | p2/L225 | ASR_UNVERIFIED | energy conventional order inflow Q2FY27
R187 | mgmt_numbers | T2 | p2/L229 | ASR_UNVERIFIED | Lara stage 3 plant capacity (2 x 800 MW)
R188 | mgmt_numbers | T2 | p2/L230 | ASR_UNVERIFIED | energy conventional order book Sept 2026
R189 | mgmt_numbers | T2 | p2/L230 | ASR_UNVERIFIED | hydrocarbon order book
R190 | mgmt_numbers | T2 | p2/L231 | ASR_UNVERIFIED | carbon light solutions order book (unit not heard)
R192 | mgmt_numbers | T2 | p3/L236 | ASR_UNVERIFIED | energy conventional prospects remaining six months FY27
R194 | mgmt_numbers | T2 | p3/L237 | ASR_UNVERIFIED | hydrocarbon prospects
R195 | mgmt_numbers | T2 | p3/L238 | ASR_UNVERIFIED | carbon light solution prospects
R196 | mgmt_numbers | T2 | p3/L239 | ASR_UNVERIFIED | energy conventional revenue Q2FY27
R197 | mgmt_numbers | T2 | p3/L239 | ASR_UNVERIFIED | energy conventional revenue growth
R199 | mgmt_numbers | T2 | p3/L244 | ASR_UNVERIFIED | hydrocarbon margin Q2FY26
R200 | mgmt_numbers | T2 | p3/L244 | ASR_UNVERIFIED | hydrocarbon margin Q2FY27
R203 | mgmt_numbers | T2 | p3/L250 | ASR_UNVERIFIED | energy conventional segment margin Q2FY27
R204 | mgmt_numbers | T2 | p3/L250 | ASR_UNVERIFIED | energy conventional margin decline YoY
R207 | mgmt_numbers | T2 | p3/L255 | ASR_UNVERIFIED | energy green order inflow Q2FY27
R208 | mgmt_numbers | T2 | p3/L255 | ASR_UNVERIFIED | energy green order inflow decline
R210 | mgmt_numbers | T2 | p3/L257 | ASR_UNVERIFIED | energy green order book (heard)
R211 | mgmt_numbers | T2 | p3/L257 | ASR_UNVERIFIED | solar order book
R212 | mgmt_numbers | T2 | p3/L258 | ASR_UNVERIFIED | onshore wind order book
R213 | mgmt_numbers | T2 | p3/L258 | ASR_UNVERIFIED | offshore wind order book
R214 | mgmt_numbers | T2 | p3/L260 | ASR_UNVERIFIED | energy green pipeline
R215 | mgmt_numbers | T2 | p3/L260 | ASR_UNVERIFIED | solar EPC prospects
R216 | mgmt_numbers | T2 | p3/L261 | ASR_UNVERIFIED | onshore wind prospects
R217 | mgmt_numbers | T2 | p3/L261 | ASR_UNVERIFIED | offshore wind prospects (primarily Europe)
R218 | mgmt_numbers | T2 | p3/L262 | ASR_UNVERIFIED | energy green revenue Q2FY27
R219 | mgmt_numbers | T2 | p3/L262 | ASR_UNVERIFIED | energy green revenue growth
R225 | mgmt_numbers | T2 | p3/L271 | ASR_UNVERIFIED | manufacturing and product order book Sept 2026
R226 | mgmt_numbers | T2 | p3/L272 | ASR_UNVERIFIED | precision engineering order book
R227 | mgmt_numbers | T2 | p3/L272 | ASR_UNVERIFIED | heavy engineering order book
R228 | mgmt_numbers | T2 | p3/L273 | ASR_UNVERIFIED | electronic products and systems order book
R230 | mgmt_numbers | T2 | p3/L274 | ASR_UNVERIFIED | construction equipment, industrial product and design and development 
R231 | mgmt_numbers | T2 | p3/L275 | ASR_UNVERIFIED | manufacturing segment prospects remaining six months
R232 | mgmt_numbers | T2 | p3/L276 | ASR_UNVERIFIED | precision engineering and electronic prospects
R233 | mgmt_numbers | T2 | p3/L277 | ASR_UNVERIFIED | heavy engineering prospects
R234 | mgmt_numbers | T2 | p3/L278 | ASR_UNVERIFIED | manufacturing and product segment revenue Q2FY27
R235 | mgmt_numbers | T2 | p3/L278 | ASR_UNVERIFIED | manufacturing segment revenue growth
R241 | mgmt_numbers | T2 | p3/L290 | ASR_UNVERIFIED | technology platforms segment revenue Q2FY27
R242 | mgmt_numbers | T2 | p3/L291 | ASR_UNVERIFIED | technology platforms revenue growth
R246 | mgmt_numbers | T2 | p3/L304 | ASR_UNVERIFIED | L&T Finance return on asset Q2FY27
R250 | mgmt_numbers | T2 | p3/L307 | ASR_UNVERIFIED | realty order inflow Q2FY27 (L&T share of pre-sales)
R252 | mgmt_numbers | T2 | p3/L308 | ASR_UNVERIFIED | realty segment order book (unrecognized revenue) September 2026
R256 | mgmt_numbers | T2 | p3/L313 | ASR_UNVERIFIED | group order inflow growth H1 FY27 (heard)
R259 | mgmt_numbers | T2 | p3/L315 | ASR_UNVERIFIED | prospects pipeline remaining six months
R262 | mgmt_numbers | T2 | p3/L320 | ASR_UNVERIFIED | FY27 order inflow growth guidance
R270 | mgmt_numbers | T2 | p3/L330 | ASR_UNVERIFIED | FY27 revenue growth guidance
R272 | mgmt_numbers | T2 | p3/L332 | ASR_UNVERIFIED | PPM EBITDA margin target FY27
R275 | mgmt_numbers | T2 | p3/L334 | ASR_UNVERIFIED | group NWC record low September 2026
R278 | mgmt_numbers | T2 | p3/L337 | ASR_UNVERIFIED | earlier group NWC guidance for the year
R280 | mgmt_numbers | T2 | p3/L341 | ASR_UNVERIFIED | question queue keypress
R281 | mgmt_numbers | T2 | p3/L342 | ASR_UNVERIFIED | queue removal keypress
R287 | mgmt_numbers | T4 | p4/L357 | ASR_UNVERIFIED | solar award delay period
R311 | mgmt_numbers | T10 | p4/L421 | ASR_UNVERIFIED | analyst asked early-stage share of hydrocarbon book (garbled)
R313 | mgmt_numbers | T10 | p4/L426 | ASR_UNVERIFIED | major part of hydrocarbon order book (heard; figure unclear)
R314 | mgmt_numbers | T10 | p4/L427 | ASR_UNVERIFIED | could be under the new one (heard; unclear)
R325 | mgmt_numbers | T14 | p4/L457 | ASR_UNVERIFIED | period of order inflow observation
R334 | mgmt_numbers | T18 | p5/L482 | ASR_UNVERIFIED | group working capital quoted by analyst
R335 | mgmt_numbers | T18 | p5/L482 | ASR_UNVERIFIED | working capital guidance quoted by analyst
R336 | mgmt_numbers | T18 | p5/L486 | ASR_UNVERIFIED | PPM portfolio net working capital as of September
R338 | mgmt_numbers | T18 | p5/L487 | ASR_UNVERIFIED | group NWC guidance
R342 | mgmt_numbers | T18 | p5/L498 | ASR_UNVERIFIED | working capital at start of year
R345 | mgmt_numbers | T20 | p5/L502 | ASR_UNVERIFIED | Nvidia chips quoted by analyst
R346 | mgmt_numbers | T20 | p5/L506 | ASR_UNVERIFIED | GPUs
R347 | mgmt_numbers | T20 | p5/L506 | ASR_UNVERIFIED | investment for 10,000 GPUs
R348 | mgmt_numbers | T20 | p5/L509 | ASR_UNVERIFIED | current data center near Chennai
R350 | mgmt_numbers | T20 | p5/L511 | ASR_UNVERIFIED | planned additional AI data center
R352 | mgmt_numbers | T20 | p5/L514 | ASR_UNVERIFIED | AI factory capacity build-up megawatt
R353 | mgmt_numbers | T20 | p5/L515 | ASR_UNVERIFIED | AI capacity target
R355 | mgmt_numbers | T20 | p5/L515 | ASR_UNVERIFIED | AI capacity horizon
R357 | mgmt_numbers | T20 | p5/L519 | ASR_UNVERIFIED | AI data center capacity
R358 | mgmt_numbers | T20 | p5/L520 | ASR_UNVERIFIED | already set up, structure in place
R360 | mgmt_numbers | T20 | p5/L521 | ASR_UNVERIFIED | balance AI capacity
R362 | mgmt_numbers | T20 | p5/L524 | ASR_UNVERIFIED | AI capacity horizon
R363 | mgmt_numbers | T20 | p5/L524 | ASR_UNVERIFIED | total AI capacity near term
R364 | mgmt_numbers | T20 | p5/L525 | ASR_UNVERIFIED | analyst: spend for 30 megawatt chips
R365 | mgmt_numbers | T20 | p5/L525 | ASR_UNVERIFIED | megawatts balance quoted by analyst
R366 | mgmt_numbers | T20 | p5/L526 | ASR_UNVERIFIED | analyst estimate for balance 70 MW (management says depends on chip va
R372 | mgmt_numbers | T22 | p5/L535 | ASR_UNVERIFIED | semiconductor revenue traction horizon
R375 | mgmt_numbers | T24 | p5/L545 | ASR_UNVERIFIED | PPM net working capital September quarter quoted
R376 | mgmt_numbers | T24 | p5/L549 | ASR_UNVERIFIED | traditional domestic PPM NWC to sales quoted
R377 | mgmt_numbers | T24 | p5/L550 | ASR_UNVERIFIED | domestic share of order book quoted
R378 | mgmt_numbers | T24 | p5/L558 | ASR_UNVERIFIED | earlier domestic working capital
R379 | mgmt_numbers | T24 | p5/L559 | ASR_UNVERIFIED | domestic working capital now (heard; likely 12 to 13 percent, unclear)
R381 | mgmt_numbers | T24 | p5/L563 | ASR_UNVERIFIED | overall PPM portfolio net working capital
R382 | mgmt_numbers | T24 | p5/L564 | ASR_UNVERIFIED | domestic working capital intensity
R383 | mgmt_numbers | T24 | p5/L565 | ASR_UNVERIFIED | international portfolio net working capital implied
R384 | mgmt_numbers | T24 | p5/L569 | ASR_UNVERIFIED | gross working capital September over March
R387 | mgmt_numbers | T26 | p5/L578 | ASR_UNVERIFIED | hydrocarbon revenue growth year on year quoted by analyst (heard)
R390 | mgmt_numbers | T26 | p5/L592 | ASR_UNVERIFIED | Q2 PPM revenue growth
R391 | mgmt_numbers | T26 | p5/L592 | ASR_UNVERIFIED | full year revenue guidance maintained
R395 | mgmt_numbers | T26 | p5/L598 | ASR_UNVERIFIED | hydrocarbon margin improvement year on year in Q2 quoted by analyst
R400 | mgmt_numbers | T28 | p6/L611 | ASR_UNVERIFIED | Oman budget flat period
R401 | mgmt_numbers | T28 | p6/L612 | ASR_UNVERIFIED | Oman budget range quoted by analyst
R402 | mgmt_numbers | T28 | p6/L612 | ASR_UNVERIFIED | selected for PDO framework
R403 | mgmt_numbers | T28 | p6/L614 | ASR_UNVERIFIED | PDO framework period
R405 | mgmt_numbers | T28 | p6/L615 | ASR_UNVERIFIED | PDO order prospects
R406 | mgmt_numbers | T28 | p6/L616 | ASR_UNVERIFIED | PDO prospects horizon
R407 | mgmt_numbers | T28 | p6/L617 | ASR_UNVERIFIED | PDO framework peers
R410 | mgmt_numbers | T28 | p6/L621 | ASR_UNVERIFIED | PDO opportunities
R411 | mgmt_numbers | T28 | p6/L621 | ASR_UNVERIFIED | PDO opportunities horizon (as heard here)
R414 | mgmt_numbers | T30 | p6/L626 | ASR_UNVERIFIED | realty ramp horizon
R415 | mgmt_numbers | T30 | p6/L627 | ASR_UNVERIFIED | potential development portfolio quoted by analyst
R423 | mgmt_numbers | T32 | p6/L640 | ASR_UNVERIFIED | DAC approvals strong traction period
R432 | mgmt_numbers | T34 | p6/L661 | ASR_UNVERIFIED | main businesses in Middle East
R441 | mgmt_numbers | T34 | p6/L683 | ASR_UNVERIFIED | per participant limit
R446 | mgmt_numbers | T36 | p6/L701 | ASR_UNVERIFIED | pre-war oil barrels still moving through Strait of Hormuz (stated by m
R454 | mgmt_numbers | T38 | p6/L736 | ASR_UNVERIFIED | infra margin better if water and effluent treatment excluded
R459 | mgmt_numbers | T40 | p6/L750 | ASR_UNVERIFIED | period of EPC-only strategy quoted
R471 | mgmt_numbers | T42 | p7/L779 | ASR_UNVERIFIED | core growth quoted by analyst
R475 | mgmt_numbers | T42 | p7/L797 | ASR_UNVERIFIED | group EBITDA margin Q2FY26 (percent)
R476 | mgmt_numbers | T42 | p7/L797 | ASR_UNVERIFIED | group EBITDA margin Q2FY27 (percent)
R477 | mgmt_numbers | T42 | p7/L801 | ASR_UNVERIFIED | part of drop from segment margin compression compensated in other inco
R478 | mgmt_numbers | T42 | p7/L803 | ASR_UNVERIFIED | part of drop from timing mismatch of cost booked in corporate
R482 | mgmt_numbers | T44 | p7/L817 | ASR_UNVERIFIED | core cash generation first half FY27 quoted by analyst
R484 | mgmt_numbers | T44 | p7/L823 | ASR_UNVERIFIED | group cash and cash equivalents with temporary surplus

## forward_commitments (74)
ROW_ID | category | turn | page/line | A2 flags | note
R016 | forward_commitments | T2 | p1/L37 | - | call structure
R020 | forward_commitments | T2 | p1/L52 | - | macro outlook
R023 | forward_commitments | T2 | p1/L57 | - | operating environment
R028 | forward_commitments | T2 | p1/L69 | - | PDO framework
R029 | forward_commitments | T2 | p1/L74 | - | PDO framework
R031 | forward_commitments | T2 | p1/L78 | - | data centers
R032 | forward_commitments | T2 | p1/L79 | - | data centers
R033 | forward_commitments | T2 | p1/L80 | - | AI compute
R036 | forward_commitments | T2 | p1/L81 | - | AI factory
R040 | forward_commitments | T2 | p1/L83 | - | AI factory
R041 | forward_commitments | T2 | p1/L86 | - | AI factory commissioning
R049 | forward_commitments | T2 | p1/L99 | - | semiconductors
R053 | forward_commitments | T2 | p1/L102 | - | electronics
R054 | forward_commitments | T2 | p1/L105 | - | electronics mobility
R056 | forward_commitments | T2 | p1/L106 | - | electronics mobility
R061 | forward_commitments | T2 | p1/L110 | - | development projects
R062 | forward_commitments | T2 | p1/L111 | - | Hyderabad Metro divestment
R080 | forward_commitments | T2 | p1/L123 | - | pipeline
R167 | forward_commitments | T2 | p2/L207 | - | pipeline
R178 | forward_commitments | T2 | p2/L217 | - | infra segment
R191 | forward_commitments | T2 | p2/L232 | - | pipeline
R222 | forward_commitments | T2 | p3/L265 | - | energy green
R255 | forward_commitments | T2 | p3/L311 | - | guidance preface
R260 | forward_commitments | T2 | p3/L316 | - | pipeline
R261 | forward_commitments | T2 | p3/L319 | - | order inflow guidance
R264 | forward_commitments | T2 | p3/L321 | - | revenue outlook
R265 | forward_commitments | T2 | p3/L323 | - | revenue outlook
R266 | forward_commitments | T2 | p3/L327 | - | revenue outlook
R268 | forward_commitments | T2 | p3/L329 | - | revenue guidance
R271 | forward_commitments | T2 | p3/L332 | - | margin guidance
R274 | forward_commitments | T2 | p3/L333 | - | working capital outlook
R277 | forward_commitments | T2 | p3/L336 | - | NWC guidance
R279 | forward_commitments | T2 | p3/L339 | - | transition
R285 | forward_commitments | T4 | p4/L357 | - | solar ordering
R288 | forward_commitments | T4 | p4/L360 | - | offshore wind
R290 | forward_commitments | T4 | p4/L364 | - | solar ordering
R293 | forward_commitments | T4 | p4/L374 | - | outlook
R298 | forward_commitments | T6 | p4/L394 | - | JV profitability
R302 | forward_commitments | T8 | p4/L404 | - | offshore wind
R307 | forward_commitments | T8 | p4/L417 | - | renewable revenue
R308 | forward_commitments | T8 | p4/L418 | - | renewable revenue
R309 | forward_commitments | T8 | p4/L419 | - | renewable revenue
R315 | forward_commitments | T10 | p4/L428 | - | hydrocarbon margin recognition
R321 | forward_commitments | T12 | p4/L444 | - | defence orders
R322 | forward_commitments | T12 | p4/L447 | - | defence order conversion timing
R329 | forward_commitments | T14 | p4/L469 | - | solar ordering
R332 | forward_commitments | T16 | p5/L478 | - | cost recovery
R337 | forward_commitments | T18 | p5/L487 | - | NWC guidance
R340 | forward_commitments | T18 | p5/L493 | - | NWC outlook
R341 | forward_commitments | T18 | p5/L495 | - | NWC outlook
R343 | forward_commitments | T18 | p5/L499 | - | NWC outlook
R349 | forward_commitments | T20 | p5/L511 | - | AI data center expansion
R351 | forward_commitments | T20 | p5/L513 | - | AI capacity
R354 | forward_commitments | T20 | p5/L515 | - | AI capacity
R361 | forward_commitments | T20 | p5/L521 | - | AI capex
R369 | forward_commitments | T22 | p5/L532 | - | semiconductors
R371 | forward_commitments | T22 | p5/L535 | - | semiconductors
R392 | forward_commitments | T26 | p5/L592 | - | revenue guidance
R404 | forward_commitments | T28 | p6/L615 | - | PDO prospects
R419 | forward_commitments | T30 | p6/L633 | - | realty plan
R420 | forward_commitments | T30 | p6/L635 | - | realty plan
R424 | forward_commitments | T32 | p6/L641 | - | AMCA bid
R426 | forward_commitments | T32 | p6/L650 | - | defence pipeline
R427 | forward_commitments | T32 | p6/L653 | - | defence pipeline
R436 | forward_commitments | T34 | p6/L666 | - | T&D outlook
R439 | forward_commitments | T34 | p6/L674 | - | renewable outlook
R448 | forward_commitments | T36 | p6/L705 | - | Hormuz transit
R456 | forward_commitments | T38 | p6/L742 | - | infra margin outlook
R463 | forward_commitments | T40 | p7/L760 | - | investment policy
R466 | forward_commitments | T40 | p7/L767 | - | ROE outlook
R468 | forward_commitments | T40 | p7/L770 | - | investment policy
R486 | forward_commitments | T44 | p7/L826 | - | capital allocation
R487 | forward_commitments | T44 | p7/L828 | - | capital allocation
R488 | forward_commitments | T44 | p7/L831 | - | working capital discipline

## hedge_qualifiers (90)
ROW_ID | category | turn | page/line | A2 flags | note
R001 | hedge_qualifiers | T1 | p1/L21 | - | ASR provenance qualifier
R005 | hedge_qualifiers | T1 | p1/L24 | - | call format
R007 | hedge_qualifiers | T1 | p1/L27 | - | recording notice
R017 | hedge_qualifiers | T2 | p1/L39 | - | forward-looking disclaimer
R019 | hedge_qualifiers | T2 | p1/L45 | - | disclaimer pointer
R090 | hedge_qualifiers | T2 | p1/L130 | - | order book definition
R126 | hedge_qualifiers | T2 | p2/L164 | - | execution qualifier
R128 | hedge_qualifiers | T2 | p2/L165 | - | metric definition
R130 | hedge_qualifiers | T2 | p2/L167 | - | margin explanation
R133 | hedge_qualifiers | T2 | p2/L170 | - | margin qualifier
R137 | hedge_qualifiers | T2 | p2/L174 | - | PAT driver
R138 | hedge_qualifiers | T2 | p2/L178 | - | pointer
R145 | hedge_qualifiers | T2 | p2/L186 | - | NWC qualifier
R147 | hedge_qualifiers | T2 | p2/L187 | - | metric definition
R150 | hedge_qualifiers | T2 | p2/L189 | - | metric definition
R152 | hedge_qualifiers | T2 | p2/L191 | - | disclosure note
R154 | hedge_qualifiers | T2 | p2/L193 | - | metric definition
R156 | hedge_qualifiers | T2 | p2/L195 | - | ROE qualifier
R163 | hedge_qualifiers | T2 | p2/L203 | - | private share comparison
R181 | hedge_qualifiers | T2 | p2/L221 | - | margin qualifier
R184 | hedge_qualifiers | T2 | p2/L226 | - | energy conventional order inflow growth (no figure)
R201 | hedge_qualifiers | T2 | p3/L245 | - | margin qualifier
R202 | hedge_qualifiers | T2 | p3/L248 | - | margin qualifier
R209 | hedge_qualifiers | T2 | p3/L256 | - | inflow qualifier
R220 | hedge_qualifiers | T2 | p3/L263 | - | revenue driver
R223 | hedge_qualifiers | T2 | p3/L266 | - | margin statement
R224 | hedge_qualifiers | T2 | p3/L269 | - | inflow qualifier
R229 | hedge_qualifiers | T2 | p3/L273 | - | order book definition
R236 | hedge_qualifiers | T2 | p3/L281 | - | margin statement
R243 | hedge_qualifiers | T2 | p3/L293 | - | margin qualifier
R245 | hedge_qualifiers | T2 | p3/L303 | - | L&T Finance
R249 | hedge_qualifiers | T2 | p3/L306 | - | segment reporting change
R251 | hedge_qualifiers | T2 | p3/L307 | - | metric definition
R253 | hedge_qualifiers | T2 | p3/L308 | - | metric definition
R254 | hedge_qualifiers | T2 | p3/L309 | - | realty qualifier
R258 | hedge_qualifiers | T2 | p3/L314 | - | H1 qualifier
R276 | hedge_qualifiers | T2 | p3/L335 | - | NWC qualifier
R289 | hedge_qualifiers | T4 | p4/L363 | - | ordering qualifier
R291 | hedge_qualifiers | T4 | p4/L367 | - | execution statement
R292 | hedge_qualifiers | T4 | p4/L368 | - | margin statement
R296 | hedge_qualifiers | T6 | p4/L386 | - | margin location qualifier
R297 | hedge_qualifiers | T6 | p4/L391 | - | margin location
R301 | hedge_qualifiers | T8 | p4/L403 | - | revenue driver
R304 | hedge_qualifiers | T8 | p4/L407 | - | logistics qualifier
R305 | hedge_qualifiers | T8 | p4/L409 | - | logistics qualifier
R306 | hedge_qualifiers | T8 | p4/L412 | - | logistics qualifier
R312 | hedge_qualifiers | T10 | p4/L423 | - | order book qualifier
R320 | hedge_qualifiers | T12 | p4/L437 | - | export order
R326 | hedge_qualifiers | T14 | p4/L457 | - | order inflow qualifier
R327 | hedge_qualifiers | T14 | p4/L460 | - | segment statement
R328 | hedge_qualifiers | T14 | p4/L466 | - | execution statement
R331 | hedge_qualifiers | T16 | p4/L476 | - | cost statement
R339 | hedge_qualifiers | T18 | p5/L490 | - | revenue qualifier
R356 | hedge_qualifiers | T20 | p5/L516 | - | chip cost qualifier
R359 | hedge_qualifiers | T20 | p5/L520 | - | capex qualifier
R367 | hedge_qualifiers | T20 | p5/L528 | - | capex qualifier
R370 | hedge_qualifiers | T22 | p5/L534 | - | semiconductor qualifier
R380 | hedge_qualifiers | T24 | p5/L559 | - | domestic NWC qualifier
R385 | hedge_qualifiers | T24 | p5/L571 | - | working capital qualifier
R388 | hedge_qualifiers | T26 | p5/L584 | - | execution qualifier
R394 | hedge_qualifiers | T26 | p5/L597 | - | margin statement
R396 | hedge_qualifiers | T26 | p5/L600 | - | confirmation
R397 | hedge_qualifiers | T26 | p5/L601 | - | margin qualifier
R409 | hedge_qualifiers | T28 | p6/L619 | - | PDO qualifier
R412 | hedge_qualifiers | T28 | p6/L623 | - | margin statement
R416 | hedge_qualifiers | T30 | p6/L630 | - | realty qualifier
R428 | hedge_qualifiers | T32 | p6/L655 | - | defence qualifier
R429 | hedge_qualifiers | T34 | p6/L657 | - | defence statement
R434 | hedge_qualifiers | T34 | p6/L662 | - | logistics qualifier
R435 | hedge_qualifiers | T34 | p6/L665 | - | logistics qualifier
R437 | hedge_qualifiers | T34 | p6/L669 | - | logistics qualifier
R440 | hedge_qualifiers | T34 | p6/L680 | - | moderator rule
R445 | hedge_qualifiers | T36 | p6/L697 | - | logistics qualifier
R447 | hedge_qualifiers | T36 | p6/L703 | - | logistics qualifier
R451 | hedge_qualifiers | T38 | p6/L729 | - | margin qualifier
R452 | hedge_qualifiers | T38 | p6/L732 | - | order basis qualifier
R453 | hedge_qualifiers | T38 | p6/L735 | - | margin qualifier
R455 | hedge_qualifiers | T38 | p6/L738 | - | margin qualifier
R460 | hedge_qualifiers | T40 | p7/L754 | - | segment qualifier
R464 | hedge_qualifiers | T40 | p7/L760 | - | investment qualifier
R467 | hedge_qualifiers | T40 | p7/L768 | - | ROE qualifier
R472 | hedge_qualifiers | T42 | p7/L789 | - | margin definition
R473 | hedge_qualifiers | T42 | p7/L792 | - | margin definition
R474 | hedge_qualifiers | T42 | p7/L797 | - | margin bridge
R479 | hedge_qualifiers | T42 | p7/L806 | - | management qualifier
R480 | hedge_qualifiers | T42 | p7/L810 | - | management statement
R483 | hedge_qualifiers | T44 | p7/L817 | - | cash flow qualifier
R485 | hedge_qualifiers | T44 | p7/L823 | - | cash qualifier
R489 | hedge_qualifiers | T44 | p7/L835 | - | management statement
R490 | hedge_qualifiers | T44 | p7/L840 | - | call structure

## dates (29)
ROW_ID | category | turn | page/line | A2 flags | note
R003 | dates | T1 | p1/L21 | - | transcript production time
R004 | dates | T1 | p1/L23 | - | call subject periods
R011 | dates | T2 | p1/L32 | - | earnings call period
R013 | dates | T2 | p1/L35 | - | highlights period
R042 | dates | T2 | p1/L86 | - | AI factory commissioning target
R055 | dates | T2 | p1/L105 | - | EV traction motors production start
R057 | dates | T2 | p1/L108 | - | share project agreement signing
R063 | dates | T2 | p1/L111 | - | original completion date
R064 | dates | T2 | p1/L111 | - | revised completion date
R065 | dates | T2 | p1/L113 | - | group performance period
R091 | dates | T2 | p1/L130 | - | order book date
R093 | dates | T2 | p1/L131 | - | order book comparison date
R139 | dates | T2 | p2/L180 | - | working capital period
R141 | dates | T2 | p2/L182 | - | NWC date
R157 | dates | T2 | p2/L196 | - | labor code provision quarter
R193 | dates | T2 | p3/L236 | - | prospects horizon
R221 | dates | T2 | p3/L264 | - | first offshore wind orders secured
R247 | dates | T2 | p3/L305 | - | L&T Finance ROA period
R257 | dates | T2 | p3/L313 | - | period
R263 | dates | T2 | p3/L320 | - | guidance year
R267 | dates | T2 | p3/L328 | - | offshore wind growth base year
R269 | dates | T2 | p3/L329 | - | guidance year
R273 | dates | T2 | p3/L332 | - | margin target year
R286 | dates | T4 | p4/L357 | - | solar ordering pick-up
R316 | dates | T10 | p4/L428 | - | margin recognition threshold timing
R393 | dates | T26 | p5/L592 | - | prior call referenced
R418 | dates | T30 | p6/L631 | - | reference to realty plan communication
R425 | dates | T32 | p6/L641 | - | AMCA bid date (heard)
R465 | dates | T40 | p7/L766 | - | L31 plan communication month

## entities_participants (72)
ROW_ID | category | turn | page/line | A2 flags | note
R008 | entities_participants | T2 | p1/L28 | - | opening remarks speaker
R009 | entities_participants | T2 | p1/L28 | - | company
R010 | entities_participants | T2 | p1/L30 | - | moderator addressed by speaker
R015 | entities_participants | T2 | p1/L37 | - | joins for Q&A
R021 | entities_participants | T2 | p1/L55 | - | macro risk named
R022 | entities_participants | T2 | p1/L55 | - | macro variable named
R024 | entities_participants | T2 | p1/L65 | - | segment
R025 | entities_participants | T2 | p1/L65 | - | framework counterparty
R030 | entities_participants | T2 | p1/L78 | - | data center reorganisation subsidiary
R034 | entities_participants | T2 | p1/L80 | - | AI compute subsidiary
R035 | entities_participants | T2 | p1/L81 | - | facility
R038 | entities_participants | T2 | p1/L82 | - | AI factory hardware
R039 | entities_participants | T2 | p1/L83 | - | long-term deployment agreement counterparty
R043 | entities_participants | T2 | p1/L88 | - | wholly owned subsidiary
R045 | entities_participants | T2 | p1/L93 | - | first SiC product
R047 | entities_participants | T2 | p1/L97 | - | SiC partnership
R048 | entities_participants | T2 | p1/L98 | - | semiconductor manufacturing partner
R050 | entities_participants | T2 | p1/L100 | - | segment
R051 | entities_participants | T2 | p1/L101 | - | order secured
R052 | entities_participants | T2 | p1/L102 | - | capacity expansion site
R058 | entities_participants | T2 | p1/L108 | - | divestment counterparty
R059 | entities_participants | T2 | p1/L109 | - | owner of Hyderabad Metro Rail Limited
R060 | entities_participants | T2 | p1/L110 | - | stake being divested
R068 | entities_participants | T2 | p1/L115 | - | ultra mega and mega order sources
R069 | entities_participants | T2 | p1/L115 | - | segment
R070 | entities_participants | T2 | p1/L117 | - | portfolio
R077 | entities_participants | T2 | p1/L122 | - | PPM core
R115 | entities_participants | T2 | p2/L151 | - | other international markets
R122 | entities_participants | T2 | p2/L159 | - | ASR phrase unclear; possibly international revenue
R125 | entities_participants | T2 | p2/L163 | - | recently secured projects
R134 | entities_participants | T2 | p2/L171 | - | cost pressure source
R160 | entities_participants | T2 | p2/L201 | - | major orders
R161 | entities_participants | T2 | p2/L202 | - | orders
R177 | entities_participants | T2 | p2/L216 | - | infra segment
R182 | entities_participants | T2 | p2/L223 | - | segment composition
R185 | entities_participants | T2 | p2/L229 | - | mega order customer
R186 | entities_participants | T2 | p2/L229 | - | order main plant package
R198 | entities_participants | T2 | p3/L243 | - | carbon light orders translating into revenue
R205 | entities_participants | T2 | p3/L251 | - | segment composition
R206 | entities_participants | T2 | p3/L252 | - | solar presence
R237 | entities_participants | T2 | p3/L284 | - | segment composition
R238 | entities_participants | T2 | p3/L286 | - | listed entity
R239 | entities_participants | T2 | p3/L286 | - | listed entity
R240 | entities_participants | T2 | p3/L289 | - | small portion in segment
R244 | entities_participants | T2 | p3/L300 | - | subsidiary
R248 | entities_participants | T2 | p3/L305 | - | separate segment now reported
R283 | entities_participants | T4 | p3/L345 | - | analyst, first question
R284 | entities_participants | T4 | p4/L354 | - | management respondent
R295 | entities_participants | T6 | p4/L381 | - | joint ventures carbon light
R300 | entities_participants | T8 | p4/L398 | - | analyst, second question
R303 | entities_participants | T8 | p4/L407 | - | respondent
R318 | entities_participants | T12 | p4/L435 | - | defence approvals
R319 | entities_participants | T12 | p4/L437 | - | export order origin (precision engineering)
R324 | entities_participants | T14 | p4/L451 | - | analyst, third question
R374 | entities_participants | T24 | p5/L540 | - | analyst firm, fourth question
R389 | entities_participants | T26 | p5/L588 | - | execution sites
R399 | entities_participants | T28 | p5/L605 | - | analyst, fifth question
R408 | entities_participants | T28 | p6/L617 | - | other PDO framework contractors
R417 | entities_participants | T30 | p6/L630 | - | corporate strategy
R422 | entities_participants | T32 | p6/L636 | - | defence programme
R430 | entities_participants | T34 | p6/L657 | - | defence segments
R433 | entities_participants | T34 | p6/L661 | - | three Middle East businesses
R438 | entities_participants | T34 | p6/L671 | - | solar module source
R443 | entities_participants | T36 | p6/L686 | - | analyst, sixth question
R444 | entities_participants | T36 | p6/L691 | - | shipping chokepoint
R450 | entities_participants | T38 | p6/L713 | - | analyst, seventh question
R458 | entities_participants | T40 | p6/L748 | - | development asset
R461 | entities_participants | T40 | p7/L757 | - | earlier development projects
R462 | entities_participants | T40 | p7/L759 | - | investment areas
R470 | entities_participants | T42 | p7/L774 | - | analyst, eighth question
R491 | entities_participants | T45 | p7/L842 | - | closing comments
R492 | entities_participants | T45 | p7/L847 | - | call conclusion

## RESTATED / CROSS-REFS
R314/R315/R316 (hydrocarbon 50%/Q4 margin recognition) restate with MFS-1 L430. R104/R105 private share 39% vs 30%. R474/R475/R476/R477 EBITDA 10 to 8.7 restated across L797-801. R272-R277 working capital 1.7% vs <10% guide: R277 FORWARD, R333 question.

## MISSING_FROM_STRUCTURED (5)
MFS-1 | FORWARD/DATE | L430 | heard: "Yeah, Q4 and beyond." (restates R315/R316 timing; no own row)
MFS-2 | FORWARD | L484 (heard 00:40:34-40) | heard: "This is something we are breaking the record every quarter. I hope that we break the record again." (NWC record; forward hope)
MFS-3 | NUMBER | L571 | heard: "securing good amount of orders over the last six months" (six months)
MFS-4 | NUMBER | L608 | heard: "Now, regarding the six-year-old..." (fragment; likely PDO six-year framework, R027)
MFS-5 | FORWARD | L707 | heard: "Maybe there will be some delay," (Middle East logistics context, hedge)
Noted as covered, not MFS: L504 "next one year, two year" (inside question R344), L525 "30 megawatt" (R364), L721 "impact expected" (inside R449).
```yaml
stage: A2-enumerator
company: "LT"
quarter: "q2fy27"
doctype: "concall"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/lt-q2fy27/work/ledger_concall_lt_q2fy27.md"
counts:
  turns: 45
  questions: 21
  mgmt_numbers: 206
  zero_standing: 0
  entities: 72
  forward_commitments: 74
  qualifiers: 90
  dates: 29
flags_raised: [REPEAT_QUESTION, MGMT_ABSENCE, MISSING_FROM_STRUCTURED]
ids_in_structured: 492
ids_referenced: 492
orphan_ids: []
missing_from_structured: ["L430 Q4 and beyond", "L484 break the record again", "L571 last six months", "L608 six-year-old fragment", "L707 will be some delay"]
gate_a2: pass
mismatch_note: ""
analyst_note: "MFS count is 5, below the 15 loop threshold. Mechanical sweep: 270 body lines carry digit, number-word or forward tokens; 261 sit within one line of a structured row; the 9 others yield 5 real units. Turns are approximate: ASR has no speaker tags, so boundaries come from the 21 QUESTION rows (8 analysts, 3 REPEAT_QUESTION clusters: working capital, DAC/precision engineering, Middle East logistics/Hormuz). No Chairman/CMD is named; only P. Ramakrishnan and Subram Sharma (Dy MD) appear. No zero/nil rows."
```
