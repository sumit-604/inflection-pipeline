# LEDGER presentation SONACOMS q2fy27 (A2) rev 2 (correction loop 1)

ids_in_structured: 317 | ids_referenced_in_ledger: 317 | orphan_ids: [] | match: yes | missing_from_structured: 15 (M01-M15)

```
=== A2 COUNT TEST (rev 2: second method is an independent fulltext token sweep, not the structured file) ===
category: slides          grep_count: 36   sweep_count: 36   match: yes   (fulltext [page N] markers 36; pdfinfo 36; formfeeds 36)
category: slide_numbers   structured NUMBER rows 201 + 12 MISSING numeric rows (M01, M04-M14)
                          fulltext sweep: every numeric token on all 36 slides checked against same-slide structured rows
                          unmatched tokens: 22% (L291), 57,136, 25.1, 24.1, 44,752, 35,545, 31,866, 26,756, 21,306, 28,568 (L523), 12 plants, 34 products
                          remaining unmatched tokens are slide footer page numbers (p4 L109, p9 L163, p12 L218, p15 L274, p17 L320, p18 L371, p22 L462, p27 L579 etc.),
                          address/postcode digits (p1 L21-23) and product-catalogue callout markers (p33-p36, covered by ENTITY-SUMMARY R310, R312, R314, R316)
                          match: yes after M01-M15 added
category: footnotes       grep_count: 42   sweep_count: 42   match: yes   (no fulltext footnote lacks a QUALIFIER row)
category: forward         grep_count: 12   sweep_count: 12   match: yes
category: dates           grep_count: 22   sweep_count: 22   match: yes
category: entities        grep_count: 40   sweep_count: 40 (+3 missing: M02, M03, M15)   match: yes after additions
category: missing_from_structured  count: 15 (M01-M15)
gate_a2: pass (CORRECTED: rev 1 count test was circular; A5 M1 accepted)
=== END COUNT TEST ===
```

Slides with no A1 rows (7): 8, 9, 12, 15, 17, 19, 25. Fulltext shows divider titles, a tab bar ("EPIC Mobility Global Market Diversification Technology Significance") and photo captions only (p8 CES 2026 products, p19 IREE 2025 booth, p25 hub traction motor cross section). No numbers; flagged NO_ROWS, not MISSING_FROM_STRUCTURED.

## Table 1. Slides

slide | title / content type | A1 ROW IDs | count | A2 flags
---|---|---|---|---
1 | Reg 30 cover letter (text) | R001-R009 | 9 | 
2 | Title: Q2 FY27 Earnings Presentation (text) | R010-R011 | 2 | 
3 | Disclaimer (text) | R012-R013 | 2 | 
4 | Our Management (photo+text) | R014-R019 | 6 | 
5 | Business Performance Highlights divider (photo) | R020-R020 | 1 | 
6 | Q2 FY27 Financial Performance Highlights (KPI) | R021-R033 | 13 | 
7 | H1 FY27 Financial Performance Highlights (KPI) | R034-R047 | 14 | 
8 | Update on Strategic Priorities divider (photo) | none | 0 | NO_ROWS
9 | Update on Strategic Priorities, EPIC Mobility divider (text) | none | 0 | NO_ROWS
10 | Sizeable and Increasing Presence in EPIC Mobility (chart/KPI) | R048-R059 | 12 | 
11 | Q2 order wins (table) | R060-R076 | 17 | 
12 | Our Strategic Priorities divider (text) | none | 0 | NO_ROWS
13 | Non-electric program portfolio expands (table) | R077-R090 | 14 | 
14 | Net order book Rs 251 bn (chart) | R091-R108 | 18 | 
15 | Our Strategic Priorities divider (text) | none | 0 | NO_ROWS
16 | Diversified Revenue Mix (chart) | R109-R121 | 13 | 
17 | Our Strategic Priorities divider (text) | none | 0 | NO_ROWS
18 | Technology Roadmap for E.P.I.C. Mobility (diagram) | R122-R128 | 7 | 
19 | Q2 FY27 Financial Update divider (photo) | none | 0 | NO_ROWS
20 | Q2 FY27 Financials (chart/table) | R129-R152 | 24 | 
21 | H1 FY27 Financials (chart/table) | R153-R176 | 24 | 
22 | FCFO of INR 4,456 mn in H1 FY27 (bridge chart) | R177-R192 | 16 | 
23 | Key Ratios (table) | R193-R220 | 28 | 
24 | Q&A (photo) | R221-R221 | 1 | 
25 | Appendix divider (photo) | none | 0 | NO_ROWS
26 | Our story so far (chart) | R222-R240 | 19 | 
27 | One Vision (text) | R241-R241 | 1 | 
28 | Guided by Values (text/KPI) | R242-R246 | 5 | 
29 | Established Global Presence (map/table) | R247-R262 | 16 | 
30 | BEV revenue and share over the years (chart) | R263-R281 | 19 | 
31 | 75 EPIC mobility programs across 37 customers (chart) | R282-R288 | 7 | 
32 | Market Shares, Differential Gears and Starter Motors (chart) | R289-R309 | 21 | 
33 | Product Summary PV/CV (diagram) | R310-R311 | 2 | 
34 | Product Summary Buses/OHV/LCV/3W (diagram) | R312-R313 | 2 | 
35 | Product Summary E2W/E3W/Advanced Robotics (diagram) | R314-R315 | 2 | 
36 | Product Summary Railways (diagram) | R316-R317 | 2 | 

## Table 2. Slide numbers (every NUMBER row)

ROW_ID | slide | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R002 | 1 | slide_number |  | 
R021 | 6 | slide_number | RESTATED | restated at R129
R022 | 6 | slide_number | RESTATED | restated at R131
R023 | 6 | slide_number | RESTATED | restated at R134
R024 | 6 | slide_number | RESTATED | restated at R136
R025 | 6 | slide_number | RESTATED | restated at R139
R026 | 6 | slide_number | RESTATED | restated at R141
R027 | 6 | slide_number | RESTATED | restated at R138
R028 | 6 | slide_number | RESTATED | restated at R143
R029 | 6 | slide_number | RESTATED | restated at R133
R030 | 6 | slide_number | RESTATED | restated at R146
R031 | 6 | slide_number | RESTATED | restated at R147
R034 | 7 | slide_number | RESTATED | restated at R153
R035 | 7 | slide_number | RESTATED | restated at R155
R036 | 7 | slide_number | RESTATED | restated at R158
R037 | 7 | slide_number | RESTATED | restated at R160
R038 | 7 | slide_number | RESTATED | restated at R163
R039 | 7 | slide_number | RESTATED | restated at R165
R040 | 7 | slide_number | RESTATED | restated at R162
R041 | 7 | slide_number | RESTATED | restated at R167
R042 | 7 | slide_number | RESTATED | restated at R198
R043 | 7 | slide_number | RESTATED | restated at R201
R048 | 10 | slide_number | RESTATED | restated at R171,R280
R049 | 10 | slide_number | RESTATED | restated at R157,R271
R050 | 10 | slide_number | RESTATED | restated at R170
R051 | 10 | slide_number |  | Q1 program count
R052 | 10 | slide_number |  | bracket string for Q1 count; R051=71 vs (20+20+31)+4: arithmetic for A3
R053 | 10 | slide_number |  | 
R054 | 10 | slide_number | RESTATED | restated at R282
R055 | 10 | slide_number |  | bracket sum 21+23+31=75 ties R054
R056 | 10 | slide_number | RESTATED | restated at R282
R062 | 11 | slide_number |  | Q2 EV adds R062+R066+R070+R074 = 24,300 mn
R066 | 11 | slide_number |  | 
R070 | 11 | slide_number |  | 
R074 | 11 | slide_number |  | 
R078 | 13 | slide_number |  | 
R080 | 13 | slide_number |  | 
R084 | 13 | slide_number |  | 
R088 | 13 | slide_number |  | 
R091 | 14 | slide_number | RESTATED | restated at R096
R092 | 14 | slide_number |  | 
R093 | 14 | slide_number |  | orderbook bridge start; 240-25+36=251 ties R096
R094 | 14 | slide_number |  | bridge consumed
R095 | 14 | slide_number |  | bridge added
R096 | 14 | slide_number | RESTATED | bridge end; ties R091; restated at R091
R097 | 14 | slide_number |  | split 152+77+13+9=251 ties R091
R098 | 14 | slide_number |  | 
R099 | 14 | slide_number |  | 
R100 | 14 | slide_number |  | 
R101 | 14 | slide_number | LABEL_UNMAPPED | 
R102 | 14 | slide_number | LABEL_UNMAPPED | 
R103 | 14 | slide_number | LABEL_UNMAPPED | 
R104 | 14 | slide_number | LABEL_UNMAPPED | 
R109 | 16 | slide_number | LABEL_UNMAPPED | 
R110 | 16 | slide_number | LABEL_UNMAPPED | 
R111 | 16 | slide_number |  | 
R112 | 16 | slide_number |  | 
R113 | 16 | slide_number |  | 
R114 | 16 | slide_number |  | 
R115 | 16 | slide_number |  | 
R116 | 16 | slide_number |  | 
R117 | 16 | slide_number |  | 
R118 | 16 | slide_number |  | 
R119 | 16 | slide_number |  | 
R120 | 16 | slide_number |  | 
R129 | 20 | slide_number | RESTATED | restated at R021
R130 | 20 | slide_number |  | prior-year comparator, label by position
R131 | 20 | slide_number | RESTATED | restated at R022
R132 | 20 | slide_number |  | 
R133 | 20 | slide_number | RESTATED | restated at R029
R134 | 20 | slide_number | RESTATED | restated at R023
R135 | 20 | slide_number |  | 
R136 | 20 | slide_number | RESTATED | restated at R024
R137 | 20 | slide_number |  | 
R138 | 20 | slide_number | RESTATED | restated at R027
R139 | 20 | slide_number | RESTATED | restated at R025
R140 | 20 | slide_number |  | 
R141 | 20 | slide_number | RESTATED | restated at R026
R142 | 20 | slide_number |  | 
R143 | 20 | slide_number | RESTATED | restated at R028
R144 | 20 | slide_number |  | derived: Q2 EBITDA margin delta (25.3 to 23.0)
R145 | 20 | slide_number |  | derived: PAT margin delta
R146 | 20 | slide_number | RESTATED | restated at R030
R147 | 20 | slide_number | RESTATED | restated at R031
R153 | 21 | slide_number | RESTATED | restated at R034
R154 | 21 | slide_number |  | prior-year comparator, label by position
R155 | 21 | slide_number | RESTATED | restated at R035
R156 | 21 | slide_number |  | 
R157 | 21 | slide_number | RESTATED | restated at R049,R271
R158 | 21 | slide_number | RESTATED | restated at R036
R159 | 21 | slide_number |  | 
R160 | 21 | slide_number | RESTATED | restated at R037
R161 | 21 | slide_number |  | 
R162 | 21 | slide_number | RESTATED | restated at R040
R163 | 21 | slide_number | RESTATED | restated at R038
R164 | 21 | slide_number |  | 
R165 | 21 | slide_number | RESTATED | restated at R039
R166 | 21 | slide_number |  | 
R167 | 21 | slide_number | RESTATED | restated at R041
R168 | 21 | slide_number |  | derived: H1 EBITDA margin delta
R169 | 21 | slide_number |  | derived: H1 PAT margin delta
R170 | 21 | slide_number | RESTATED | restated at R050
R171 | 21 | slide_number | RESTATED | restated at R048
R177 | 22 | slide_number |  | 
R179 | 22 | slide_number |  | 
R180 | 22 | slide_number |  | 
R181 | 22 | slide_number |  | 
R182 | 22 | slide_number | LABEL_UNMAPPED | 
R183 | 22 | slide_number |  | closing cash; bridge items R182,R187-R190 unresolved
R184 | 22 | slide_number |  | 
R185 | 22 | slide_number |  | 
R186 | 22 | slide_number |  | 
R187 | 22 | slide_number | LABEL_UNMAPPED | 
R188 | 22 | slide_number | LABEL_UNMAPPED | 
R189 | 22 | slide_number | LABEL_UNMAPPED | 
R190 | 22 | slide_number | LABEL_UNMAPPED | 
R193 | 23 | slide_number |  | 
R194 | 23 | slide_number |  | 
R195 | 23 | slide_number |  | 
R196 | 23 | slide_number |  | 
R197 | 23 | slide_number |  | 
R198 | 23 | slide_number | RESTATED | restated at R042
R199 | 23 | slide_number |  | 
R200 | 23 | slide_number |  | 
R201 | 23 | slide_number | RESTATED | restated at R043
R202 | 23 | slide_number |  | 
R203 | 23 | slide_number |  | 
R204 | 23 | slide_number |  | 
R205 | 23 | slide_number |  | 
R206 | 23 | slide_number |  | 
R207 | 23 | slide_number |  | 
R208 | 23 | slide_number |  | 
R209 | 23 | slide_number |  | 
R210 | 23 | slide_number |  | 
R215 | 23 | slide_number | RESTATED | restated at R214
R222 | 26 | slide_number |  | 
R223 | 26 | slide_number |  | 
R224 | 26 | slide_number |  | 
R227 | 26 | slide_number |  | 
R228 | 26 | slide_number |  | 
R229 | 26 | slide_number |  | 
R230 | 26 | slide_number |  | 
R231 | 26 | slide_number |  | 
R232 | 26 | slide_number |  | 
R233 | 26 | slide_number |  | 
R234 | 26 | slide_number |  | 
R235 | 26 | slide_number |  | 
R236 | 26 | slide_number |  | 
R237 | 26 | slide_number |  | 
R238 | 26 | slide_number | LABEL_UNMAPPED | 
R239 | 26 | slide_number | LABEL_UNMAPPED | 
R242 | 28 | slide_number |  | 
R243 | 28 | slide_number |  | 
R244 | 28 | slide_number |  | 
R247 | 29 | slide_number |  | 
R248 | 29 | slide_number |  | 
R249 | 29 | slide_number |  | 
R250 | 29 | slide_number |  | 
R251 | 29 | slide_number |  | 
R252 | 29 | slide_number |  | 
R253 | 29 | slide_number |  | 
R254 | 29 | slide_number | LABEL_UNMAPPED | 
R255 | 29 | slide_number | LABEL_UNMAPPED | 
R256 | 29 | slide_number | LABEL_UNMAPPED | 
R264 | 30 | slide_number |  | 
R265 | 30 | slide_number |  | 
R266 | 30 | slide_number |  | 
R267 | 30 | slide_number |  | 
R268 | 30 | slide_number |  | 
R269 | 30 | slide_number |  | 
R270 | 30 | slide_number |  | 
R271 | 30 | slide_number | RESTATED | restated at R049,R157
R272 | 30 | slide_number |  | 
R273 | 30 | slide_number |  | 
R274 | 30 | slide_number |  | 
R275 | 30 | slide_number |  | 
R276 | 30 | slide_number |  | 
R277 | 30 | slide_number |  | 
R278 | 30 | slide_number |  | 
R279 | 30 | slide_number |  | 
R280 | 30 | slide_number | RESTATED | restated at R048
R282 | 31 | slide_number | RESTATED | restated at R054,R056
R283 | 31 | slide_number |  | 
R284 | 31 | slide_number | LABEL_UNMAPPED | 
R289 | 32 | slide_number |  | 
R290 | 32 | slide_number |  | 
R291 | 32 | slide_number |  | 
R292 | 32 | slide_number |  | 
R293 | 32 | slide_number |  | 
R294 | 32 | slide_number |  | 
R295 | 32 | slide_number |  | 
R296 | 32 | slide_number |  | 
R297 | 32 | slide_number |  | 
R298 | 32 | slide_number |  | 
R299 | 32 | slide_number |  | 
R300 | 32 | slide_number |  | 
R301 | 32 | slide_number |  | 
R302 | 32 | slide_number |  | 
R303 | 32 | slide_number | LABEL_UNMAPPED | 
R304 | 32 | slide_number | LABEL_UNMAPPED | 
R305 | 32 | slide_number | LABEL_UNMAPPED | 

## Table 3. Footnotes, qualifiers, fine print (every QUALIFIER row)

ROW_ID | slide | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R007 | 1 | footnote_qualifier |  | results unaudited
R013 | 3 | footnote_qualifier |  | safe harbor
R032 | 6 | footnote_qualifier |  | same def at R044,R151,R175
R033 | 6 | footnote_qualifier |  | same def at R058,R281
R044 | 7 | footnote_qualifier | FOOTNOTE_UNRESOLVED | marker numbering scrambled in source; def same as R032
R045 | 7 | footnote_qualifier |  | ROCE def p7 (NOVELIC only) vs R213 p23 (NOVELIC + Railway): scope differs
R046 | 7 | footnote_qualifier |  | ROE def p7 vs R214 p23: scope differs
R058 | 10 | footnote_qualifier | FOOTNOTE_UNRESOLVED | truncated in source
R059 | 10 | footnote_qualifier |  | 
R105 | 14 | footnote_qualifier |  | qualifies headline R091
R106 | 14 | footnote_qualifier |  | see R107
R128 | 18 | footnote_qualifier |  | 
R148 | 20 | footnote_qualifier |  | qualifies R144
R149 | 20 | footnote_qualifier |  | qualifies R145
R150 | 20 | footnote_qualifier |  | qualifies R129
R151 | 20 | footnote_qualifier |  | 
R172 | 21 | footnote_qualifier |  | qualifies R168
R173 | 21 | footnote_qualifier |  | qualifies R169; names exceptional expenses in H1FY26
R174 | 21 | footnote_qualifier |  | 
R175 | 21 | footnote_qualifier |  | 
R178 | 22 | footnote_qualifier |  | 
R212 | 23 | footnote_qualifier |  | 
R213 | 23 | footnote_qualifier |  | 
R214 | 23 | footnote_qualifier |  | cites Rs 301 mn labour code (R215)
R216 | 23 | footnote_qualifier |  | 
R217 | 23 | footnote_qualifier |  | 
R218 | 23 | footnote_qualifier |  | 
R219 | 23 | footnote_qualifier |  | Railway annualised; qualifies R196-R210
R226 | 26 | footnote_qualifier |  | 
R246 | 28 | footnote_qualifier |  | 5-yr ROE def; compare R045,R213
R262 | 29 | footnote_qualifier |  | source for OEM rank claims R247-R251
R281 | 30 | footnote_qualifier |  | 
R285 | 31 | footnote_qualifier |  | 
R286 | 31 | footnote_qualifier |  | qualifies R282-R283
R287 | 31 | footnote_qualifier |  | 
R306 | 32 | footnote_qualifier |  | dominance claim vs R303-R305 (dated Feb 2021, R308/R309)
R307 | 32 | footnote_qualifier |  | 
R308 | 32 | footnote_qualifier |  | India share data dated Feb 2021: stale
R311 | 33 | footnote_qualifier |  | under development
R313 | 34 | footnote_qualifier |  | under development
R315 | 35 | footnote_qualifier |  | under development
R317 | 36 | footnote_qualifier | FOOTNOTE_UNRESOLVED | asterisk not matched to a product

## Table 4. Forward-looking statements

ROW_ID | slide | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R060 | 11 | forward | | 
R063 | 11 | forward | | 
R067 | 11 | forward | | 
R071 | 11 | forward | | 
R075 | 11 | forward | | 
R077 | 13 | forward | | 
R081 | 13 | forward | | 
R085 | 13 | forward | | 
R089 | 13 | forward | | 
R107 | 14 | forward | | restates R106
R122 | 18 | forward | | 
R241 | 27 | forward | | 

## Table 5. Dates

ROW_ID | slide | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R001 | 1 | date | | 
R005 | 1 | date | | 
R009 | 1 | date | | 
R010 | 2 | date | | 
R011 | 2 | date | | 
R057 | 10 | date | | 
R064 | 11 | date | | 
R068 | 11 | date | | 
R072 | 11 | date | | 
R076 | 11 | date | | 
R082 | 13 | date | | 
R086 | 13 | date | | 
R090 | 13 | date | | 
R108 | 14 | date | | 
R121 | 16 | date | | 
R152 | 20 | date | | 
R176 | 21 | date | | 
R191 | 22 | date | | 
R211 | 23 | date | | 
R240 | 26 | date | | 
R263 | 30 | date | | 
R309 | 32 | date | | 

## Table 6. Entities (ENTITY and ENTITY-SUMMARY)

ROW_ID | slide | category | A2 flags | cross-ref / materiality
---|---|---|---|---
R003 | 1 | entity | | 
R004 | 1 | entity | | 
R006 | 1 | entity | | 
R008 | 1 | entity | | 
R012 | 3 | entity | | multi-item summary row; items not split by A1
R014 | 4 | entity | | 
R015 | 4 | entity | | 
R016 | 4 | entity | | 
R017 | 4 | entity | | 
R018 | 4 | entity | | 
R019 | 4 | entity | | 
R020 | 5 | entity | | 
R047 | 7 | entity | | also R220
R061 | 11 | entity | | 
R065 | 11 | entity | | 
R069 | 11 | entity | | 
R073 | 11 | entity | | 
R079 | 13 | entity | | 
R083 | 13 | entity | | 
R087 | 13 | entity | | 
R123 | 18 | entity | | 
R124 | 18 | entity | | 
R125 | 18 | entity | | 
R126 | 18 | entity | | 
R127 | 18 | entity | | 
R192 | 22 | entity | | 
R220 | 23 | entity | | also R047
R221 | 24 | entity | | 
R225 | 26 | entity | | 
R245 | 28 | entity | | 
R257 | 29 | entity | | 
R258 | 29 | entity | | 
R259 | 29 | entity | | 
R260 | 29 | entity | | 
R261 | 29 | entity | | 
R288 | 31 | entity | | 
R310 | 33 | entity | | multi-item summary row; items not split by A1
R312 | 34 | entity | | multi-item summary row; items not split by A1
R314 | 35 | entity | | multi-item summary row; items not split by A1
R316 | 36 | entity | | multi-item summary row; items not split by A1

## Table 7. Accountability (all IDs by slide)

p1: R001, R002, R003, R004, R005, R006, R007, R008, R009
p2: R010, R011
p3: R012, R013
p4: R014, R015, R016, R017, R018, R019
p5: R020
p6: R021, R022, R023, R024, R025, R026, R027, R028, R029, R030, R031, R032, R033
p7: R034, R035, R036, R037, R038, R039, R040, R041, R042, R043, R044, R045, R046, R047
p10: R048, R049, R050, R051, R052, R053, R054, R055, R056, R057, R058, R059
p11: R060, R061, R062, R063, R064, R065, R066, R067, R068, R069, R070, R071, R072, R073, R074, R075, R076
p13: R077, R078, R079, R080, R081, R082, R083, R084, R085, R086, R087, R088, R089, R090
p14: R091, R092, R093, R094, R095, R096, R097, R098, R099, R100, R101, R102, R103, R104, R105, R106, R107, R108
p16: R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R120, R121
p18: R122, R123, R124, R125, R126, R127, R128
p20: R129, R130, R131, R132, R133, R134, R135, R136, R137, R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149, R150, R151, R152
p21: R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175, R176
p22: R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R192
p23: R193, R194, R195, R196, R197, R198, R199, R200, R201, R202, R203, R204, R205, R206, R207, R208, R209, R210, R211, R212, R213, R214, R215, R216, R217, R218, R219, R220
p24: R221
p26: R222, R223, R224, R225, R226, R227, R228, R229, R230, R231, R232, R233, R234, R235, R236, R237, R238, R239, R240
p27: R241
p28: R242, R243, R244, R245, R246
p29: R247, R248, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258, R259, R260, R261, R262
p30: R263, R264, R265, R266, R267, R268, R269, R270, R271, R272, R273, R274, R275, R276, R277, R278, R279, R280, R281
p31: R282, R283, R284, R285, R286, R287, R288
p32: R289, R290, R291, R292, R293, R294, R295, R296, R297, R298, R299, R300, R301, R302, R303, R304, R305, R306, R307, R308, R309
p33: R310, R311
p34: R312, R313
p35: R314, R315
p36: R316, R317

## Flags summary

- LABEL_UNMAPPED (from A1): R101, R102, R103, R104, R109, R110, R182, R187, R188, R189, R190, R238, R239, R254, R255, R256, R284, R303, R304, R305
- FOOTNOTE_UNRESOLVED: R044, R058, R317
- NO_ROWS slides: 8, 9, 12, 15, 17, 19, 25
- RESTATED: Q2/H1 headline p6/p7 vs p20/p21; BEV figures p6/p10/p20/p21/p30; orderbook p14 internal
- Definition drift: ROCE/ROE scope p7 (R045,R046) vs p23 (R213,R214) vs p28 (R246)
- ZERO_STANDING: none. DROPPED_SLIDE: not assessable (no prior ledger).

## Table 8. MISSING_FROM_STRUCTURED (found by fulltext sweep; loop back to A1 for rows)

ID | fulltext line | slide | category | claim text (verbatim) | A2 flags | note
---|---|---|---|---|---|---
M01 | L291 | 16 | slide_number | 22% | MISSING_FROM_STRUCTURED LABEL_UNMAPPED | pie label on same line as 51%; belongs to the H1 FY27 geography pie (sum test); related R109
M02 | L504 | 26 | entity | Became publicly listed (Phase 4) | MISSING_FROM_STRUCTURED | Phase 4 event; compare R225 Phase 3
M03 | L505 | 26 | entity | Acquisition of NOVELIC and Railway Business (Phase 4) | MISSING_FROM_STRUCTURED | see R047, R220
M04 | L506 | 26 | slide_number | 12 plants (Phase 4) | MISSING_FROM_STRUCTURED | restates R252 (p29, 12 manufacturing plants); compare R224 Phase 3 9 plants
M05 | L507 | 26 | slide_number | 34 products (Phase 4) | MISSING_FROM_STRUCTURED | compare R224 Phase 3 10 products
M06 | L510 | 26 | slide_number | 57,136 H1FY27 (Ann.) | MISSING_FROM_STRUCTURED | revenue Rs mn, annualised H1 (2 x 28,568)
M07 | L512-513 | 26 | slide_number | FY22-H1FY27 Ann. Avg. EBITDA margin 25.1% | MISSING_FROM_STRUCTURED | compare R227 (25.3%, FY99 onward)
M08 | L515 | 26 | slide_number | FY22-H1FY27 Ann. Revenue CAGR 24.1% | MISSING_FROM_STRUCTURED | compare R228 (33.9%), R242 (23% FY22-FY26)
M09 | L516 | 26 | slide_number | 44,752 | MISSING_FROM_STRUCTURED LABEL_UNMAPPED | revenue bar Rs mn, no year label in text; by descending height
M10 | L518 | 26 | slide_number | 35,545 | MISSING_FROM_STRUCTURED LABEL_UNMAPPED | revenue bar Rs mn, by position
M11 | L519 | 26 | slide_number | 31,866 | MISSING_FROM_STRUCTURED LABEL_UNMAPPED | revenue bar Rs mn, by position
M12 | L520 | 26 | slide_number | 26,756 | MISSING_FROM_STRUCTURED LABEL_UNMAPPED | revenue bar Rs mn, by position
M13 | L522 | 26 | slide_number | 21,306 | MISSING_FROM_STRUCTURED LABEL_UNMAPPED | revenue bar Rs mn, by position
M14 | L523 | 26 | slide_number | 28,568 H1FY27 | MISSING_FROM_STRUCTURED | restates R153 (p21 H1 FY27 revenue); H1 actual bar
M15 | L156 and L378 | 8, 19 | entity | p8 caption: Integrated Motor Controllers, EVTOL Gearbox, AMR Drive Unit at CES 2026; p19 caption: Exhibition Booth at Indian Railway Equipment Exhibition (IREE) 2025 | MISSING_FROM_STRUCTURED | photo captions on NO_ROWS slides 8 and 19; CES 2026 relates to R020, R221

Note: the coordinator list ran L504-L523 as 12 units plus L291; row M14 (28,568 H1FY27, L523) is the 13th. Slide footer page numbers, address digits and p33-p36 callout markers swept and excluded as non-disclosure (not enumerated). Slides 8 and 19 now have M15 only; slides 9, 12, 15, 17, 25 remain no-row dividers.

Closing block below mirrors work/blocks/a2-presentation.yaml.

```yaml
stage: A2-enumerator
company: "SONACOMS"
quarter: "q2fy27"
doctype: "presentation"
model: claude-sonnet-5-5
status: complete
revision: 2
counts:
  entities: 40
  slides: 36
  slide_numbers: 201
  missing_from_structured: 15
ids_in_structured: 317
ids_referenced: 317
orphan_ids: []
missing_from_structured: [M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13, M14, M15]
gate_a2: pass
```
