# A2 LEDGER: IndiaMART Q2FY27 press release (doctype presentation; 1 PDF page = 1 slide)
ids_in_structured: 140 | ids_referenced_in_ledger: 140 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides          grep_count: 5    sweep_count: 5    match: yes  (page_count_pdfinfo 5, formfeed 5)
category: slide_numbers   grep_count: 97   sweep_count: 97   match: yes  (A1 NUMBER 97; per-page recon below)
category: line_items      grep_count: 11   sweep_count: 11   match: yes  (p4 table metric rows; 58 cells R072-R129)
category: zero_standing   grep_count: 3    sweep_count: 3    match: yes  (R127-R129 dash cells)
category: footnotes       grep_count: 7    sweep_count: 7    match: yes  (A1 QUALIFIER 7)
category: type_totals     grep_count: 140  sweep_count: 140  match: yes  (NUMBER 97 + ENTITY 14 + FORWARD 7 + DATE 15 + QUALIFIER 7 = 140)
per-page reconciliation (fulltext numeric-token sweep vs structured rows):
 p1: R001-R012 = 12 rows | fulltext tokens: date, BSE 542726, period date, Reg 30/2015, signature stamp, F5164 -> match
 p2: R013-R044 = 32 rows | fulltext figures 429/10%/156/40%/135/391/389/37/443/9%/394/46/2,029/16%/1,863/155/91/3,234 + dates + stray 66 -> match
 p3: R045-R069 = 25 rows | fulltext 389/360/8%/394/8%/1,863/14%/156/40%/106/27m/8.9m/4%/217K -> match
 p4: R070-R130 = 61 rows | 58 table cells (TI6 Rev6 EBITDA6 EBm2 NP6 NPm2 Coll6 CFO6 DR6 Cash6 Pay6) + header/unit/period/check-log -> match
 p5: R131-R140 = 10 rows | fulltext date/time, Zoom link, CIN, addresses -> match
gate_a2: pass
=== END COUNT TEST ===

## 1. Slides (pages)
ROW_ID | category | flags | note
R001-R012 | slide 1 Reg 30 cover letter to BSE/NSE (text) | - | signed 15:35:42 IST Oct 27 (R012); webinar at 17:00 IST (R131), so release precedes call
R013-R044 | slide 2 consolidated highlights (text) | RESTATED | headline figures restated in body (R019/R024/R081, R021/R056/R084, R023/R042/R109, R043/R121)
R045-R069 | slide 3 standalone + operational + CEO quote (text) | RESTATED | R046/R027/R078 revenue; R051/R032/R100 collections; R053/R037/R112 deferred
R070-R130 | slide 4 Q2FY27 Performance Metrics (table) | RENDER_VERIFIED | text layer displaced rows; render governs (R130)
R131-R140 | slide 5 call notice + About + addresses (text) | - | -

## 2. Line items, slide 4 table (11 metric rows x Standalone/Consolidated x Q2FY27, YoY, QoQ)
ROW_ID | category | flags | note
R072-R077 | Total Income | - | Standalone QoQ (18%), Consol QoQ (19%): sequential fall; YoY 3%/5% below revenue growth 8%/10%
R078-R083 | Revenue from Operations | RESTATED | ties to R046, R019
R084-R089 | EBITDA | RESTATED | YoY 36%/23% vs revenue 8%/10%
R090-R091 | EBITDA Margin | RESTATED | 40% = R057, R022
R092-R097 | Net Profit | RESTATED | QoQ (40%)/(47%)
R098-R099 | Net Profit Margin | - | -
R100-R105 | Collections from Customer | RESTATED | QoQ (2%)/(4%)
R106-R111 | Cash flow from Operations | RESTATED | standalone 124 appears only in table
R112-R117 | Deferred Revenue | RESTATED | standalone QoQ 0%
R118-R123 | Cash and Investments | RENDER_VERIFIED | no YoY/QoQ in text layer, render values
R124-R129 | Paying Suppliers (In 000) | RENDER_VERIFIED | R124-R126 standalone; R127-R129 consolidated dash
R070-R071 | table unit and period headers | - | -
R130 | column-to-period check log | RENDER_VERIFIED | A1 process note

## 3. Zero / nil / dash standing items
ROW_ID | category | flags | note
R127 | Consolidated Paying Suppliers Q2FY27 | ZERO_STANDING | no consolidated paying-supplier count disclosed
R128 | Consolidated Paying Suppliers YoY | ZERO_STANDING | -
R129 | Consolidated Paying Suppliers QoQ | ZERO_STANDING | -
(R114 0% and R126 (0%) are real zero-percent values, not dashes; noted, not counted as ZERO_STANDING.)

## 4. Slide numbers (all NUMBER and DATE units by slide)
ROW_ID | category | flags | note
R004, R011, R018-R028, R030-R033, R035-R038, R041-R043 | numbers p1-p2 | RESTATED where tied above | R018 stray "66" from headline graphic, no label
R046-R048, R051-R054, R056-R062 | numbers p3 | RESTATED | R062 paying suppliers 217K ties R124
R072-R129 | numbers p4 (58 cells) | see section 2 | -
R139 | CIN | - | -
R001, R005, R012, R013-R016, R040, R044, R045, R055, R069, R071, R131, R133 | dates | - | period/timestamp/balance dates

## 5. Entities
ROW_ID | category | flags | note
R002, R003, R006, R008, R009, R010, R017, R029, R049, R063, R134, R136, R137, R140 | entities (14) | - | Busy Infotech (R029) only subsidiary named; no ENTITY_CHANGE (no prior ledger)

## 6. Forward-looking statements
ROW_ID | category | flags | note
R064-R068 | CEO quote strategic statements | - | R067 "explore new monetisation avenues" unquantified
R132, R135 | webinar and recording | - | scheduled event; availability commitment

## 7. Footnotes, qualifiers, fine print
ROW_ID | category | flags | note
R007 | audited-results qualifier | - | -
R034 | "primarily comprising" (collections) | FOOTNOTE_UNRESOLVED | composition 394+46=440 vs 443 stated; Rs 3 Cr unexplained in text
R039 | "This primarily includes" (deferred) | FOOTNOTE_UNRESOLVED | 1,863+155=2,018 vs 2,029; Rs 11 Cr unexplained
R050 | growth driver: realization from paying suppliers | - | paying suppliers YoY (2%) (R125), so growth is price not count
R070 | unit convention | - | -
R130 | text-layer displacement log | - | -
R138 | "largest online B2B marketplace" | - | self-described claim

## MISSING_FROM_STRUCTURED
none. Observation: deferred 1,863+155 and revenue 389+37=426 vs 429 consolidated: same style gap (Rs 3 Cr), arithmetic only, no interpretation.
