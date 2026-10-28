# A2 LEDGER: SONACOMS pressrelease Q2 FY27
Source: extracted/sonacoms-pressrelease-q2fy27-structured.md (R001-R127). Prior ledger: none (no DROPPED_SLIDE test possible).

ids_in_structured: 127 | ids_referenced_in_ledger: 127 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides(pages)  grep_count: 4    sweep_count: 4    match: yes
category: slide_numbers  grep_count: 52   sweep_count: 52   match: yes   (NUMBER rows)
category: entities       grep_count: 33   sweep_count: 33   match: yes
category: forward        grep_count: 8    sweep_count: 8    match: yes
category: dates          grep_count: 20   sweep_count: 20   match: yes
category: footnotes_qual grep_count: 14   sweep_count: 14   match: yes   (QUALIFIER rows; 1 footnote + 1 disclaimer)
category: total_ids      grep_count: 127  sweep_count: 127  match: yes
category: zero_standing  grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES / PAGES (content type: text; no charts or tables in extraction)
| Page | Title/content | Type | IDs on page |
|---|---|---|---|
| 1 | Exchange intimation letter (Reg 30), signature block | text | R001-R002, R053-R058, R094-R097, R114 |
| 2 | Results Release Q2 FY27, highlights, CEO quote | text | R003-R039, R059-R067, R092, R098-R103, R115-R121 |
| 3 | Operational highlights: Deming, new products, orders won | text | R040-R049, R068-R079, R086-R091, R104-R112, R122-R125 |
| 4 | About, contacts, disclaimer | text | R050-R052, R080-R085, R093, R113, R126-R127 |
No prior deck: DROPPED_SLIDE not testable.

## 2. SLIDE NUMBERS (every NUMBER row)
ROW_ID | category | flags | cross-ref / note
R001 | admin code | RESTATED | = R052, R084
R002 | admin code | | exchange PINs
R003 | headline growth | RESTATED | = R010, R033
R004 | headline share | RESTATED | = R009, R034; base Automotive revenue (R121)
R005 | order additions | RESTATED | = R036 (Rs bn)
R006 | net order book | RESTATED | = R037, R028 (Rs bn vs crore); 'net' undefined (R115, R120)
R007 | Q2 revenue | | Rs crore
R008 | Q2 revenue YoY | RESTATED | = R030
R009 | BEV share | RESTATED | = R004
R010 | BEV growth | RESTATED | = R003
R011 | Q2 EBITDA | |
R012 | Q2 EBITDA margin | |
R013 | Q2 EBITDA YoY | RESTATED | = R031. EBITDA growth (23%) below revenue growth (35%)
R014 | Q2 PAT | |
R015 | Q2 PAT margin | |
R016 | Q2 PAT YoY | RESTATED | = R032
R017 | BEV programs won | | count; relates R018, R019
R018 | connected program won | |
R019 | ICE programs won | | R017+R018+R019 = 7 programs; order list R044-R049 = 6 items
R020 | H1 revenue | |
R021 | H1 revenue YoY | |
R022 | H1 EBITDA | |
R023 | H1 EBITDA margin | | same 23.0% as Q2 (R012)
R024 | H1 PAT | |
R025 | H1 PAT margin | |
R026 | H1 PAT YoY | |
R027 | EV+Robotics share of order book | | 65% of R028 base
R028 | net order book | FOOTNOTE_UNRESOLVED | asterisked; = R006/R037
R029 | Deming journey | RESTATED | = R042, R102
R030 | CEO quote revenue YoY | RESTATED | = R008
R031 | CEO quote EBITDA YoY | RESTATED | = R013
R032 | CEO quote PAT YoY | RESTATED | = R016
R033 | CEO quote BEV YoY | RESTATED | = R003
R034 | CEO quote BEV share | RESTATED | = R004
R035 | new products | RESTATED | = R043; items R073-R075
R036 | new business Rs 36bn | RESTATED | = R005
R037 | order book Rs 251bn | RESTATED | = R006
R038 | FCFO 1.5x FY26 | | no rupee FCFO figure in doc; qualitative multiple; material
R039 | 10X ambition | | pairs with FORWARD R092
R040 | Deming outside-Japan count | |
R041 | Deming inception year | RESTATED | = R105
R042 | nine years | RESTATED | = R029
R043 | new products | RESTATED | = R035
R044 | order Rs 7.0bn | | LSD; SOP R086
R045 | order Rs 3.8bn | | motor controllers; SOP R087
R046 | order Rs 12.5bn | | traction motor; SOP R088 (H2 FY27, nearest)
R047 | order Rs 1.6bn | | ICE differential; SOP R089
R048 | order Rs 3.3bn | | starter motors; SOP R090
R049 | order Rs 1.0bn | | radar; SOP R091
R050 | founding year | RESTATED | = R113
R051 | IR phone | |
R052 | BSE code | RESTATED | = R001, R084
Cross-check note: R044-R049 sum Rs 29.2bn vs R005/R036 Rs 36bn (arithmetic only; no interpretation; A3 to reconcile).

## 3. ENTITIES (R053-R085)
R053-R054 | exchanges | |
R055 | NSE symbol | | = R084
R056 | regulator | |
R057 | signatory | | signature timestamp R097
R058 | issuer | | = R060
R059 | CEO quoted | | promoter status not stated here
R060 | issuer brand | |
R061 | Deming Prize | |
R062 | JUSE | |
R063 | Driveline Division | | Deming recipient
R064 | Sona Comstar 2.0 | | with R039, R092
R065-R067 | program categories | |
R068-R072 | customers (unnamed) | | R072 new customer; others existing
R073-R075 | new products | | R073 LSD, R074 air springs (railway), R075 radar; R074 has no order row
R076-R079 | products | |
R080 | footprint | | five countries
R081 | railway products | |
R082-R083 | contacts | |
R084 | listing | | = R001, R052, R055
R085 | website | |
ENTITY_CHANGE: not testable (no prior list); consolidation list absent in document.

## 4. FORWARD (R086-R093)
R086-R091 | SOP guidance | | dates R107-R112; R088 H2 FY27 is in current year
R092 | CEO confidence statement | | with R039
R093 | disclaimer no-update | | = R126

## 5. DATES (R094-R113)
R094 | letter date | | = R099 (same date)
R095 | regulation ref | |
R096 | results period | | = R100
R097 | signature timestamp 17:23:54 IST | | no board meeting time in doc to compare
R098 | Q2 FY27 | | = R104
R099 | release date | |
R100 | quarter end | |
R101 | H1 FY27 | |
R102 | 9-year | RESTATED | = R029, R042
R103 | FCFO periods | | with R038
R104 | Q2 FY27 | |
R105 | 1951 | RESTATED | = R041
R106 | 2026 Deming | |
R107-R112 | SOP half-years | | = R086-R091 in order
R113 | 1995 | RESTATED | = R050

## 6. FOOTNOTES / QUALIFIERS (R114-R127)
R114 | unaudited | | status
R115 | asterisk on net order book | FOOTNOTE_UNRESOLVED | no footnote text; grep of fulltext shows asterisk only at line 83
R116 | release label | |
R117 | unit mix crore/billion | | with R118
R118 | 25,100 cr vs 251bn | RESTATED | units agree
R119 | CEO attribution | |
R120 | 'net' undefined | | with R115
R121 | BEV share base | | Automotive only
R122 | ICE differential entry | | new product entry
R123 | existing vs new customer | |
R124 | order = order-book addition | |
R125 | footer page 2 vs PDF 3 | |
R126 | disclaimer | | = R093
R127 | footer page 3 vs PDF 4 | |

## 7. Other categories
Notes (numbered): none in a press release. Line items / zero_standing: none (no financial tables; 0 ZERO_STANDING). Agenda, auditor paras, turns, questions: not applicable.
MISSING_FROM_STRUCTURED: none found.
