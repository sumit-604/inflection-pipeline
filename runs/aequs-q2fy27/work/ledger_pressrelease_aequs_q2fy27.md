# LEDGER pressrelease | AEQUS | q2fy27 | doctype presentation (press release, 5 PDF pages = 5 "slides")
Source: extracted/aequs-pressrelease-q2fy27-structured.md (IDs R001-R171). No prior ledger: DROPPED_SLIDE/ENTITY_CHANGE diffs not testable.

ids_in_structured: 171 | ids_referenced_in_ledger: 171 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides(pages)   grep_count: 5    sweep_count: 5    match: yes
category: slide_numbers   grep_count: 112  sweep_count: 112  match: yes  (NUMBER rows)
category: dates           grep_count: 8    sweep_count: 8    match: yes
category: entities        grep_count: 19   sweep_count: 19   match: yes
category: entity_summary  grep_count: 5    sweep_count: 5    match: yes
category: footnotes_qualifiers grep_count: 17 sweep_count: 17 match: yes
category: forward         grep_count: 10   sweep_count: 10   match: yes
category: total_ids       grep_count: 171  sweep_count: 171  match: yes
category: zero_standing   grep_count: 0    sweep_count: 0    match: yes
page split: p1=19 p2=82 p3=40 p4=22 p5=8 (sum 171)
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (pages)
| Page | Title / content | Content type | ROW IDs |
|1|Reg 30 cover letter, signature, addresses|text|R001-R019|
|2|Headline, Key Financial Highlights table, consolidated/JV/segment bullets|text+table|R020-R101|
|3|Consumer H1, EBITDA, loss, order book, Safran, warrants, capacity, Consumer ramp, CFO|text|R102-R141|
|4|Chairman quote, About Aequs|text|R142-R163|
|5|Consumer portfolio, footprint, capacity footnote, safe harbor, contacts|text|R164-R171|

## 2. DATES (8)
| ID | category | flags | note |
|R001,R003,R020,R024,R025,R125,R156|date|-|R001/R003/R024 restate 26 Oct 2026 release date (RESTATED)|
|R007|date|SIGNATURE_TS|signature 2026.10.26 16:22:41 +05:30; no board meeting time in this document|

## 3. NUMBERS (112) by block
| IDs | block | flags | note |
|R002,R008-R013|identifiers/contact (scrip, membership, CIN, phones, pincodes)|-|administrative|
|R004,R005,R006|title headline rev/growth|RESTATED|= R021-R023, R033, R072-R075, R143-R144|
|R021-R023|page 2 headline|RESTATED|as above|
|R030-R032|table YoY/QoQ/H1 header cells|-|R032 restates 50%|
|R033-R037|Revenue row (5 cells)|-|R033 = R004/R021/R072; R036 = R074/R144|
|R038-R045|EBITDA row (8 cells)|-|R038/R043 restated R109/R112; YoY (45)% on comparability-qualified base (R070)|
|R046-R053|EBITDA margin row (8)|-|(>100) bps cells are A1 verbatim|
|R054-R061|PAT row (8)|-|R054 = R114; R057 = R115; R059 = R117; R060 = R118; R071 garble resolved|
|R062-R069|PAT margin row (8)|-|-|
|R072-R075|consolidated revenue bullets|RESTATED|-|
|R078-R087|JV-inclusive revenue/EBITDA (10)|-|basis R077 proportionate JV|
|R088-R095|Aerospace revenue/EBITDA (8)|-|R091=R145 (42%); EBITDA pairing R096|
|R100-R103|Consumer revenue (4)|-|R101/R102 growth; R146 restates "more than doubling"|
|R104-R106|Consumer EBITDA loss (3)|-|Q2 401, Q1 361, H1 763|
|R109-R112|reported EBITDA text (4)|RESTATED|= R038, R041-style, R043|
|R114-R118|net loss text (5)|RESTATED|-|
|R119-R120,R147|order book USD 1.1bn / 9% QoQ / USD 1,096 Mn|RESTATED|R119 = R147|
|R122,R149|Safran tenure >15 yrs|RESTATED|-|
|R123,R124,R161|SKUs 5,978 / 238 added|RESTATED|R123=R161|
|R127,R157|six Safran entities|RESTATED|also R129|
|R131,R154|promoter warrants 6,500 Mn|RESTATED|-|
|R134-R136,R166|CNC machines 9 added, 229 total, 4.93m hrs|RESTATED|R136=R166; basis R137/R167|
|R141|CFO ~two decades|-|-|
|R143-R146|chairman quote numbers|RESTATED|-|
|R153|H1 capex 1,597 Mn|-|only capex figure; no Q2 split|

## 4. ENTITIES (19) and ENTITY-SUMMARY (5)
| IDs | category | flags | note |
|R014,R015|issuer/legal name|ENTITY_CHANGE (name: formerly Aequs Private Limited; no prior list to diff)|-|
|R016,R017|exchanges|-|-|
|R018|Co Secretary Ravi Mallikarjun Hugar|-|-|
|R026,R098,R099|dateline, segments|-|-|
|R121,R126|Safran A320 wheels agreement; Safran|-|-|
|R128|Belagavi and Hosur|-|Hosur upcoming (R130)|
|R132|promoter group preferential warrants|-|related-party funding|
|R140|Reenah Joseph, CFO appointed|MGMT_CHANGE|CFO appointment in release; no board-letter agenda here|
|R142|Aravind Melligeri, Exec Chairman and CEO|-|promoter quote present (no MGMT_ABSENCE)|
|R159,R163,R165,R170,R171|boilerplate/customers/footprint/IR firms|-|-|
|R019,R160,R162,R164,R169|ENTITY-SUMMARY (addresses, capabilities, part categories, consumer segments, contacts)|-|grouped|

## 5. FOOTNOTES / QUALIFIERS (17)
| IDs | flags | note |
|R027|-|uniqueness claim|
|R028,R029|-|table basis/unit|
|R070,R113|COMPARABILITY|consumer electronics costs expensed vs pre-operative FY26; restated in text|
|R071|FOOTNOTE_RESOLVED|garbled layout cells resolved by A1|
|R076,R077|-|attribution; JV basis|
|R096|-|EBITDA pairing|
|R107,R116|-|stated causes (loss widening, net loss)|
|R108|-|reported EBITDA basis|
|R137,R167|-|4.93m hrs annualised on Q2 FY27 basis|
|R138|-|ramp slower than anticipated (qualification, supply chain)|
|R150|-|"timing-related shift" framing|
|R168|-|safe harbor|

## 6. FORWARD (10)
| IDs | flags | note |
|R097,R129,R130,R133,R139,R148,R151,R152,R155,R158|FORWARD_NO_DATE|R151 breakeven path "recalibrated", no date; R130/R155 Hosur upcoming, no date; R133/R155 warrants use RESTATED|

## 7. MISSING_FROM_STRUCTURED
None found. Absences (not units): no ZERO_STANDING items, no balance sheet/cash flow, no guidance figures, no board meeting times, no auditor content (press release).
