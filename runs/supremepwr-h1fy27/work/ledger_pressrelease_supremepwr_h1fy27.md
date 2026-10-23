# A2 LEDGER: SUPREMEPWR pressrelease H1 FY27 (presentation-class rules; 4 pages treated as 4 slides)
ids_in_structured: 166 | ids_referenced_in_ledger: 166 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides          grep_count: 4    sweep_count: 4    match: yes  (p1 cover letter, p2 highlights, p3 orders, p4 about/disclaimer; page field rows 14/61/73/17 + R166 'page all' = 166)
category: slide_numbers   grep_count: 78   sweep_count: 78   match: yes  (R001-R078)
category: entities        grep_count: 34   sweep_count: 34   match: yes  (R079-R108 = 30, summaries R109-R112 = 4)
category: forward         grep_count: 28   sweep_count: 28   match: yes  (R113-R140)
category: dates           grep_count: 13   sweep_count: 13   match: yes  (R141-R153)
category: footnotes_qualifiers grep_count: 13 sweep_count: 13 match: yes (R154-R166)
category: zero_standing   grep_count: 0    sweep_count: 0    match: yes  (no zero/nil/dash value rows)
category: dropped_slides  grep_count: 0    sweep_count: 0    match: yes  (PRIOR_LEDGER_PATH none)
total ids                 grep_count: 166  sweep_count: 166  match: yes
arithmetic cross-check (enumeration only): the 11 order values R033,R036,R040,R043,R046,R050,R053,R056,R059,R063,R066 sum to 209.24 = R027/R031. Ties.
gate_a2: pass
=== END COUNT TEST ===

## 1. Slides (page = slide)
S1 | p1 cover letter to NSE, text | rows R001,R078-R083,R109,R112,R141-R144,R154 | Reg 30 intimation; signed 2026.10.21 20:48:24
S2 | p2 highlights, text + table | rows R002-R031 (except R032), R084-R088,R113-R126,R145-R148,R153,R155-R161 | consolidated H1 table R006-R017
S3 | p3 order list, graphic labels + text + about-company start | rows R032-R072,R089-R105 (except none), R127-R138,R149-R150,R162 | 11 orders; pairing caveat R162
S4 | p4 about/FY26/disclaimer | rows R073-R077,R106-R108,R110,R111,R139,R140,R151-R152,R163-R165 |
All-pages | R166 negative finding

## 2. Numbers on slides (ROW | category | flags | note)
R001 | date number | RESTATED(R141) | letter date
R002 | headline | RESTATED(R008,R019) | TI growth
R003 | headline | RESTATED(R006,R020) | TI
R004 | headline | RESTATED(R014,R021) | NP growth
R005 | headline | RESTATED(R012,R022) | NP
R006 | table | | TI H1FY27
R007 | table | | TI H1FY26
R008 | table | RESTATED | TI YoY
R009 | table | | EBITDA H1FY27
R010 | table | | EBITDA H1FY26
R011 | table | | EBITDA YoY
R012 | table | RESTATED | NP H1FY27
R013 | table | | NP H1FY26
R014 | table | RESTATED | NP YoY
R015 | table | LAYOUT_OFFSET | EPS value on line below its row
R016 | table | | EPS H1FY26
R017 | table | | EPS YoY 45.21% vs NP 45.09%
R018 | order book | RESTATED(R029) | "over" floor
R019 | CMD quote | RESTATED | 
R020 | CMD quote | RESTATED | 
R021 | CMD quote | RESTATED | 
R022 | CMD quote | RESTATED | 
R023 | margin | | EBITDA margin 17.42% quoted, not tabulated; prior-year margin not in doc
R024 | margin | | NP margin 10.07%; prior-year not in doc
R025 | order book PVC | | approximate range
R026 | orders count | RESTATED(R030) |
R027 | orders value | RESTATED(R031) | ties to order sum
R028 | execution range | RESTATED(R032,R153) |
R029 | order book | RESTATED(R018) |
R030 | orders count | RESTATED |
R031 | orders value | RESTATED |
R032 | execution range | RESTATED |
R033,R034,R035 | order 1 value/rating/period | |
R036,R037,R038,R039 | order 2 value/rating/kV/period | |
R040,R041,R042 | order 3 value/rating/period | | no voltage given
R043,R044,R045 | order 4 | |
R046,R047,R048,R049 | order 5 value/rating/kV/period | |
R050,R051,R052 | order 6 | |
R053,R054,R055 | order 7 | | same value as order 8
R056,R057,R058 | order 8 | | same value as order 7
R059,R060,R061,R062 | order 9 incl 66/11 kV | |
R063,R064,R065 | order 10 | |
R066,R067,R068,R069 | order 11 incl 330 kV | |
R070 | history | RESTATED(R149) |
R071 | history | RESTATED(R150) |
R072 | history | | 3 decades
R073 | cumulative units | | "over"
R074 | listing | RESTATED(R151) |
R075 | FY26 revenue | | labelled Revenue not Total Income (R164)
R076 | FY26 EBITDA | |
R077 | FY26 NP | |
R078 | address pin | | non-financial

## 3. Entities
R079 filer | R080 exchange | R081 symbol | R082 regulation | R083 CS/compliance officer | R084 dateline | R085 venue | R086 CMD Vee Rajmohan (named in quote only) | R087 Maharashtra new geography | R088 Kannur facility
R089-R099 eleven unnamed order customers | flag UNNAMED_CUSTOMERS (all 11 counterparties undisclosed)
R100 graphic labels (11 items) | cross-ref R089-R099; layout caveat R162
R101 partnership firm | R102 Pvt Ltd | R103 Tamil Nadu | R104 windmill segment | R105 local electric utilities | R106 NSE Emerge | R107 Kirin Advisors | R108 Sunil Mudgal
R109 address block | R110 contact block | R111 disclaimer (see R140) | R112 signature block
ENTITY_CHANGE: none (no consolidation list in doc; no prior ledger). No subsidiaries listed although basis is "consolidated" (R156).
MGMT_ABSENCE: n/a (no call).

## 4. Forward-looking statements
R113-R126 management claims (p2): R115 historical margin-pressure CLAIM; R125 targets not quantified (UNQUANTIFIED_TARGET); R122-R124 Kannur/capacity (no capacity or utilisation figure in doc)
R127 execution window; R128-R138 delivery commitments orders 1-11
R139 positioning claim | R140 safe-harbour disclaimer (cross-ref R111)

## 5. Dates
R141 letter date (RESTATED R001) | R142 period end | R143 reg year | R144 signature timestamp (RESTATED R112) | R145 PR date | R146 H1FY27 | R147 H1FY26 | R148 order book date | R149 1994 | R150 2005 | R151 Dec 23 | R152 FY26 | R153 durations (RESTATED R028)
Board meeting times are not in this doc, so the signature timestamp cannot be compared.

## 6. Footnotes, qualifiers, fine print
R154 unaudited (p1) | R155 unaudited (p2) | R156 consolidated | R157 glyph lost | R158 glyph lost | R159 order book floor, no definition (FOOTNOTE_UNRESOLVED) | R160 PVC approximate | R161 cumulative | R162 order pairing layout (FOOTNOTE_UNRESOLVED) | R163 lower bound | R164 Revenue vs Total Income label | R165 glyph lost | R166 no asterisks or Note lines (negative finding)
Numbered notes: 0. Unnumbered footnotes: 0 (R166).

## 7. Other flags
ZERO_STANDING: none. DROPPED_SLIDE: not assessable (no prior ledger). MISSING_FROM_STRUCTURED: none found.
Absences (enumeration only): no segment split, no balance sheet or cash flow, no Q2 standalone split, no H1 FY26 margins, no order-book definition, no capacity figures.
