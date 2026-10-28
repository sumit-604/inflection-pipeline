# A2 LEDGER | SYNGENE | q2fy27 | presentation

ids_in_structured: 350 | ids_referenced_in_ledger: 350 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: structured_total      grep_count: 350  sweep_count: 350  match: yes   (R001-R350 contiguous; header COUNTS 249+51+7+20+23=350)
category: slides                grep_count: 32   sweep_count: 32   match: yes   (pdfinfo 32, formfeeds 32, [page N] markers 32)
category: slide_numbers (NUMBER rows)  grep_count: 249  sweep_count: 249  match: yes (107 non-table rows + 142 table/BS cells)
category: slide_numbers (independent FULLTEXT sweep): 796 numeric tokens over 32 pages; 759 found in a same-page structured row; 37 unmatched = 28 page-footer / divider / list-marker tokens (M09) + 9 tokens in M01-M08 (phone, pincodes, ISO 45001/50001/17025, Management 5.0, 29th HRD, URL/email). Token vs row cardinality differs by design (one row can hold several tokens). match: yes after M-rows added; 8 real gaps raised as MISSING_FROM_STRUCTURED
category: line_items          grep_count: 45   sweep_count: 45   match: yes   (p27 P&L 17 + BS 5; p28 P&L 18 incl PAT Margin + BS 5 distinct lines; 142 cells)
category: zero_standing       grep_count: 1   sweep_count: 1   match: yes   (R149; no zero cells in tables; n/m cells R230/R235/R245 flagged NM_AS_PRINTED)
category: footnotes_qualifiers grep_count: 10 line-start markers (fulltext lines 228,429,582,650-652,714,718,720,722)  sweep_count: 23 QUALIFIER rows  match: yes (10 marker-anchored + p6 fn1/fn2 R048,R049 + R050 + R260 A1 flags + R340/R341 + 5 basis/unit lines R079,R125,R155,R254,R318 + R009 + R013 = 23)
category: forward_statements   grep_count: 7   sweep_count: 7   match: yes
category: dates               grep_count: 20  sweep_count: 19+1 boilerplate (R350)  match: yes
category: entities            grep_count: 51  sweep_count: 45+6 boilerplate summaries (R344-R349)  match: yes
category: agenda / auditor / turns / questions / mgmt_numbers: not applicable (deck)
category: dropped_slides       prior-quarter ledger none available: DROPPED_SLIDE not assessable
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (PDF page; footer prints PDF page minus 1)
page | title | type | structured IDs | flags
1 | Cover letter to exchanges | text | R001-R348 (12) | 
2 | Investor Presentation (title) | divider | R012-R012 (1) | 
3 | Safe harbour | text | R013-R347 (2) | 
4 | Contents | text | R014-R349 (2) | 
5 | 1 Q2 FY27 Highlights | divider | none (sparse divider) | SPARSE_DIVIDER
6 | Q2 FY27 financial and operating highlights | text+KPI tiles | R015-R051 (37) | 
7 | 2 Syngene - Putting Science to Work | divider | none (sparse divider) | SPARSE_DIVIDER
8 | Who we are and what we do | text | R052-R055 (4) | 
9 | Our journey so far | timeline | R056-R069 (14) | 
10 | Key facts and figures | text+KPI | R070-R080 (11) | 
11 | One of the largest integrated CRDMO players in India | chart+text | R081-R099 (19) | 
12 | 3-pronged growth strategy | text | R100-R104 (5) | 
13 | Our Strategy | text | R105-R108 (4) | 
14 | 3 Syngene strengths | divider | none (sparse divider) | SPARSE_DIVIDER
15 | Syngene strengths | text | R109-R117 (9) | 
16 | Experienced workforce | text+KPI | R118-R125 (8) | 
17 | Infrastructure and global presence | text/map | R126-R126 (1) | 
18 | Collaboration models | text | R127-R129 (3) | 
19 | Industry segments and partners | logos | R130-R344 (3) | 
20 | Operational robustness | text+KPI | R132-R139 (8) | 
21 | Digital initiatives | text | R140-R141 (2) | 
22 | Safety and sustainability | text+KPI | R142-R156 (15) | 
23 | Accreditations | text | R157-R346 (2) | 
24 | Awards and recognition | text | R158-R350 (9) | 
25 | Enterprise risk oversight | diagram | R165-R165 (1) | 
26 | 4 Financials | divider | none (sparse divider) | SPARSE_DIVIDER
27 | Q2 FY27 financial highlights | table | R166-R260 (95) | 
28 | FY26 financial highlights | table | R261-R325 (65) | 
29 | 5 Shareholding and Share Information | divider | none (sparse divider) | SPARSE_DIVIDER
30 | Syngene and Biocon Group | text | R326-R329 (4) | 
31 | Shareholding and Share Information | table/chart | R330-R341 (12) | 
32 | For more details | text/contact | R342-R343 (2) | 

## 2. LEDGER ROWS (ROW_ID | page | category | A2 flags | cross-ref / note)
Verbatim values stay at the structured file ID.

### slide_numbers (107 rows)
R003 | p1 | slide_numbers | - | -
R005 | p1 | slide_numbers | RESTATED | xref R334 (BSE code restated)
R014 | p4 | slide_numbers | - | -
R025 | p6 | slide_numbers | RESTATED | xref R166 (Q2 revenue ops 833 restated p6/p27)
R026 | p6 | slide_numbers | RESTATED | xref R169 (QoQ +13% restated)
R027 | p6 | slide_numbers | RESTATED | xref R170 (YoY -9% restated)
R028 | p6 | slide_numbers | - | -
R029 | p6 | slide_numbers | - | -
R030 | p6 | slide_numbers | RESTATED | xref R219 (Op EBITDA margin 18% restated)
R031 | p6 | slide_numbers | RESTATED | xref R220 (Q1 op margin 12% restated)
R032 | p6 | slide_numbers | RESTATED | xref R221 (Q2FY26 op margin 22% restated)
R033 | p6 | slide_numbers | - | -
R034 | p6 | slide_numbers | - | -
R035 | p6 | slide_numbers | RESTATED | xref R237 (PAT pre-exc 38 restated)
R036 | p6 | slide_numbers | RESTATED | xref R238 (Q1 PAT pre-exc 1 restated)
R037 | p6 | slide_numbers | RESTATED | xref R239 (Q2FY26 PAT 67 restated)
R038 | p6 | slide_numbers | - | -
R039 | p6 | slide_numbers | AS_PRINTED_DUP | H1FY26 PAT pre-exc = post-exc 154 (A1 render-verified)
R040 | p6 | slide_numbers | RESTATED | xref R242 (PAT post-exc 32 restated)
R041 | p6 | slide_numbers | RESTATED,NEGATIVE_VALUE | xref R243 (Q1 PAT post-exc -9 restated) Q1FY27 loss
R042 | p6 | slide_numbers | RESTATED | xref R244 (Q2FY26 PAT post-exc 67 restated)
R043 | p6 | slide_numbers | - | -
R044 | p6 | slide_numbers | AS_PRINTED_DUP | see R039/R050
R045 | p6 | slide_numbers | HEADLINE_QUALIFIED | "mid-20s" adjusted margin is a range, no point value; qualifier R048
R046 | p6 | slide_numbers | RESTATED | xref R256 (Rs 6 Cr term cost restated)
R047 | p6 | slide_numbers | - | -
R052 | p8 | slide_numbers | RESTATED | xref R091/R111 (~5,700+ scientists restated)
R053 | p8 | slide_numbers | RESTATED | xref R113 (headcount 8,300+ restated p8/p15)
R054 | p8 | slide_numbers | - | -
R061 | p9 | slide_numbers | - | -
R064 | p9 | slide_numbers | - | -
R065 | p9 | slide_numbers | - | -
R070 | p10 | slide_numbers | RESTATED | xref R086/R110/R131 (~400 clients restated)
R071 | p10 | slide_numbers | RESTATED | xref R090 (16 of top 20 restated)
R072 | p10 | slide_numbers | RESTATED | xref R115 (400+ patents restated)
R073 | p10 | slide_numbers | RESTATED | xref R261 (FY26 revenue 3,739 restated p10/p28)
R074 | p10 | slide_numbers | RESTATED | xref R304 (FY26 PAT 380 restated p10/p28)
R075 | p10 | slide_numbers | RESTATED | xref R084/R118 (headcount 8,373 restated p10/p11/p16)
R076 | p10 | slide_numbers | RESTATED | xref R119 (5,778 scientists restated)
R077 | p10 | slide_numbers | BASIS_DIFF_NOTE | renewable energy 92% (slide 10) vs 95% (slide 22); both as-on 31-Mar-26 per R079/R155; basis difference not stated; for A3
R081 | p11 | slide_numbers | - | -
R082 | p11 | slide_numbers | - | -
R083 | p11 | slide_numbers | - | -
R084 | p11 | slide_numbers | RESTATED | xref R075/R118 (headcount 8,373 restated p10/p11/p16)
R085 | p11 | slide_numbers | - | -
R086 | p11 | slide_numbers | RESTATED | xref R070/R110/R131 (~400 clients restated)
R087 | p11 | slide_numbers | - | -
R088 | p11 | slide_numbers | - | -
R089 | p11 | slide_numbers | - | -
R090 | p11 | slide_numbers | RESTATED | xref R071 (16 of top 20 restated)
R091 | p11 | slide_numbers | RESTATED | xref R052/R111 (~5,700+ scientists restated)
R092 | p11 | slide_numbers | RESTATED | xref R059 (BMS restated)
R104 | p12 | slide_numbers | - | -
R109 | p15 | slide_numbers | RESTATED | xref R135 (85 audits restated)
R110 | p15 | slide_numbers | RESTATED | xref R070/R086/R131 (~400 clients restated)
R111 | p15 | slide_numbers | RESTATED | xref R052/R091 (~5,700+ scientists restated)
R112 | p15 | slide_numbers | - | -
R113 | p15 | slide_numbers | RESTATED | xref R053 (headcount 8,300+ restated p8/p15)
R114 | p15 | slide_numbers | - | -
R115 | p15 | slide_numbers | RESTATED | xref R072 (400+ patents restated)
R118 | p16 | slide_numbers | RESTATED | xref R075/R084 (headcount 8,373 restated p10/p11/p16)
R119 | p16 | slide_numbers | RESTATED | xref R076 (5,778 scientists restated)
R120 | p16 | slide_numbers | - | -
R121 | p16 | slide_numbers | - | -
R122 | p16 | slide_numbers | - | -
R128 | p18 | slide_numbers | - | -
R129 | p18 | slide_numbers | - | -
R131 | p19 | slide_numbers | RESTATED | xref R070/R086/R110 (~400 clients restated)
R132 | p20 | slide_numbers | - | -
R133 | p20 | slide_numbers | - | -
R134 | p20 | slide_numbers | - | -
R135 | p20 | slide_numbers | RESTATED | xref R109 (85 audits restated)
R136 | p20 | slide_numbers | - | -
R137 | p20 | slide_numbers | - | -
R138 | p20 | slide_numbers | - | -
R142 | p22 | slide_numbers | - | -
R143 | p22 | slide_numbers | - | -
R144 | p22 | slide_numbers | BASIS_DIFF_NOTE | 61% reduction vs 54.6% SBTi target; different measures, for A3 read
R145 | p22 | slide_numbers | - | -
R146 | p22 | slide_numbers | BASIS_DIFF_NOTE | see R077
R147 | p22 | slide_numbers | - | -
R148 | p22 | slide_numbers | - | -
R149 | p22 | slide_numbers | ZERO_STANDING | nil standing item: zero waste to direct landfill
R150 | p22 | slide_numbers | - | -
R151 | p22 | slide_numbers | - | -
R152 | p22 | slide_numbers | - | -
R158 | p24 | slide_numbers | - | -
R159 | p24 | slide_numbers | - | -
R160 | p24 | slide_numbers | - | -
R161 | p24 | slide_numbers | - | -
R162 | p24 | slide_numbers | - | -
R163 | p24 | slide_numbers | - | -
R256 | p27 | slide_numbers | RESTATED | xref R046 (Rs 6 Cr term cost restated)
R257 | p27 | slide_numbers | - | -
R320 | p28 | slide_numbers | - | -
R321 | p28 | slide_numbers | - | -
R323 | p28 | slide_numbers | - | -
R329 | p30 | slide_numbers | - | -
R330 | p31 | slide_numbers | - | -
R331 | p31 | slide_numbers | - | -
R332 | p31 | slide_numbers | - | -
R333 | p31 | slide_numbers | RESTATED,TYPE_NOTE | xref R006 (NSE symbol restated) tagged NUMBER but value is text ticker
R334 | p31 | slide_numbers | RESTATED | xref R005 (BSE code restated)
R335 | p31 | slide_numbers | - | -
R336 | p31 | slide_numbers | - | -
R337 | p31 | slide_numbers | - | -
R338 | p31 | slide_numbers | - | -

### line_items_PL (132 rows)
R166 | p27 | line_items_PL | RESTATED | xref R025 (Q2 revenue ops 833 restated p6/p27)
R167 | p27 | line_items_PL | - | -
R168 | p27 | line_items_PL | - | -
R169 | p27 | line_items_PL | RESTATED | xref R026 (QoQ +13% restated)
R170 | p27 | line_items_PL | RESTATED | xref R027 (YoY -9% restated)
R171 | p27 | line_items_PL | - | -
R172 | p27 | line_items_PL | - | -
R173 | p27 | line_items_PL | - | -
R174 | p27 | line_items_PL | - | -
R175 | p27 | line_items_PL | - | -
R176 | p27 | line_items_PL | - | -
R177 | p27 | line_items_PL | - | -
R178 | p27 | line_items_PL | - | -
R179 | p27 | line_items_PL | - | -
R180 | p27 | line_items_PL | - | -
R181 | p27 | line_items_PL | - | -
R182 | p27 | line_items_PL | - | -
R183 | p27 | line_items_PL | - | -
R184 | p27 | line_items_PL | - | -
R185 | p27 | line_items_PL | - | -
R186 | p27 | line_items_PL | - | -
R187 | p27 | line_items_PL | - | -
R188 | p27 | line_items_PL | - | -
R189 | p27 | line_items_PL | ZERO_VALUE_CELL | 0% change cell, not a standing nil line
R190 | p27 | line_items_PL | - | -
R191 | p27 | line_items_PL | - | -
R192 | p27 | line_items_PL | - | -
R193 | p27 | line_items_PL | - | -
R194 | p27 | line_items_PL | - | -
R195 | p27 | line_items_PL | - | -
R196 | p27 | line_items_PL | - | -
R197 | p27 | line_items_PL | - | -
R198 | p27 | line_items_PL | - | -
R199 | p27 | line_items_PL | - | -
R200 | p27 | line_items_PL | - | -
R201 | p27 | line_items_PL | - | -
R202 | p27 | line_items_PL | - | -
R203 | p27 | line_items_PL | - | -
R204 | p27 | line_items_PL | - | -
R205 | p27 | line_items_PL | OUTLIER_AS_PRINTED | FX YoY 421%
R206 | p27 | line_items_PL | - | -
R207 | p27 | line_items_PL | - | -
R208 | p27 | line_items_PL | - | -
R209 | p27 | line_items_PL | - | -
R210 | p27 | line_items_PL | - | -
R211 | p27 | line_items_PL | - | -
R212 | p27 | line_items_PL | - | -
R213 | p27 | line_items_PL | - | -
R214 | p27 | line_items_PL | - | -
R215 | p27 | line_items_PL | - | -
R216 | p27 | line_items_PL | - | -
R217 | p27 | line_items_PL | - | -
R218 | p27 | line_items_PL | - | -
R219 | p27 | line_items_PL | RESTATED | xref R030 (Op EBITDA margin 18% restated)
R220 | p27 | line_items_PL | RESTATED | xref R031 (Q1 op margin 12% restated)
R221 | p27 | line_items_PL | RESTATED | xref R032 (Q2FY26 op margin 22% restated)
R222 | p27 | line_items_PL | - | -
R223 | p27 | line_items_PL | - | -
R224 | p27 | line_items_PL | - | -
R225 | p27 | line_items_PL | ZERO_VALUE_CELL | 0% change cell, not a standing nil line
R226 | p27 | line_items_PL | - | -
R227 | p27 | line_items_PL | - | -
R228 | p27 | line_items_PL | NEGATIVE_VALUE | Q1FY27 PBT loss
R229 | p27 | line_items_PL | - | -
R230 | p27 | line_items_PL | NM_AS_PRINTED | n/m change cell
R231 | p27 | line_items_PL | - | -
R232 | p27 | line_items_PL | - | -
R233 | p27 | line_items_PL | NEGATIVE_VALUE | Q1FY27 tax credit
R234 | p27 | line_items_PL | - | -
R235 | p27 | line_items_PL | NM_AS_PRINTED | n/m change cell
R236 | p27 | line_items_PL | - | -
R237 | p27 | line_items_PL | RESTATED,FOOTNOTE_MARKER | xref R035 (PAT pre-exc 38 restated) superscript marker on value; see qualifier rows
R238 | p27 | line_items_PL | RESTATED,FOOTNOTE_MARKER | xref R036 (Q1 PAT pre-exc 1 restated) superscript marker on value; see qualifier rows
R239 | p27 | line_items_PL | RESTATED | xref R037 (Q2FY26 PAT 67 restated)
R240 | p27 | line_items_PL | - | -
R241 | p27 | line_items_PL | - | -
R242 | p27 | line_items_PL | RESTATED | xref R040 (PAT post-exc 32 restated)
R243 | p27 | line_items_PL | RESTATED,NEGATIVE_VALUE | xref R041 (Q1 PAT post-exc -9 restated) Q1FY27 PAT after exceptional loss
R244 | p27 | line_items_PL | RESTATED | xref R042 (Q2FY26 PAT post-exc 67 restated)
R245 | p27 | line_items_PL | NM_AS_PRINTED | n/m change cell
R246 | p27 | line_items_PL | - | -
R261 | p28 | line_items_PL | RESTATED | xref R073 (FY26 revenue 3,739 restated p10/p28)
R262 | p28 | line_items_PL | - | -
R263 | p28 | line_items_PL | - | -
R264 | p28 | line_items_PL | - | -
R265 | p28 | line_items_PL | - | -
R266 | p28 | line_items_PL | - | -
R267 | p28 | line_items_PL | - | -
R268 | p28 | line_items_PL | - | -
R269 | p28 | line_items_PL | - | -
R270 | p28 | line_items_PL | - | -
R271 | p28 | line_items_PL | - | -
R272 | p28 | line_items_PL | - | -
R273 | p28 | line_items_PL | - | -
R274 | p28 | line_items_PL | - | -
R275 | p28 | line_items_PL | - | -
R276 | p28 | line_items_PL | - | -
R277 | p28 | line_items_PL | - | -
R278 | p28 | line_items_PL | - | -
R279 | p28 | line_items_PL | - | -
R280 | p28 | line_items_PL | - | -
R281 | p28 | line_items_PL | - | -
R282 | p28 | line_items_PL | - | -
R283 | p28 | line_items_PL | - | -
R284 | p28 | line_items_PL | OUTLIER_AS_PRINTED | FX YoY 3104% on base of 2
R285 | p28 | line_items_PL | - | -
R286 | p28 | line_items_PL | - | -
R287 | p28 | line_items_PL | - | -
R288 | p28 | line_items_PL | - | -
R289 | p28 | line_items_PL | - | -
R290 | p28 | line_items_PL | - | -
R291 | p28 | line_items_PL | - | -
R292 | p28 | line_items_PL | - | -
R293 | p28 | line_items_PL | - | -
R294 | p28 | line_items_PL | - | -
R295 | p28 | line_items_PL | - | -
R296 | p28 | line_items_PL | - | -
R297 | p28 | line_items_PL | - | -
R298 | p28 | line_items_PL | - | -
R299 | p28 | line_items_PL | - | -
R300 | p28 | line_items_PL | - | -
R301 | p28 | line_items_PL | - | -
R302 | p28 | line_items_PL | - | -
R303 | p28 | line_items_PL | - | -
R304 | p28 | line_items_PL | RESTATED,FOOTNOTE_MARKER | xref R074 (FY26 PAT 380 restated p10/p28) superscript marker on value; see qualifier rows
R305 | p28 | line_items_PL | FOOTNOTE_MARKER | superscript marker on value; see qualifier rows
R306 | p28 | line_items_PL | - | -
R307 | p28 | line_items_PL | - | -
R308 | p28 | line_items_PL | - | -
R309 | p28 | line_items_PL | - | -
R310 | p28 | line_items_PL | - | -
R311 | p28 | line_items_PL | - | -

### line_items_BS (10 rows)
R247 | p27 | line_items_BS | - | -
R248 | p27 | line_items_BS | - | -
R249 | p27 | line_items_BS | NEGATIVE_VALUE | other net assets negative
R250 | p27 | line_items_BS | BS_ITEM | net cash 1,392 vs 1,800 at Mar-26 (R315)
R251 | p27 | line_items_BS | - | -
R312 | p28 | line_items_BS | - | -
R313 | p28 | line_items_BS | - | -
R314 | p28 | line_items_BS | NEGATIVE_VALUE | other net assets negative
R315 | p28 | line_items_BS | BS_ITEM | see R250
R316 | p28 | line_items_BS | - | -

### footnotes_qualifiers (23 rows)
R009 | p1 | footnotes_qualifiers | - | -
R013 | p3 | footnotes_qualifiers | - | -
R048 | p6 | footnotes_qualifiers | HEADLINE_QUALIFIER | qualifies R030 operating EBITDA margin 18%
R049 | p6 | footnotes_qualifiers | RESTATED | xref R255 (termination footnote restated p6/p27)
R050 | p6 | footnotes_qualifiers | AS_PRINTED_DUP | A1 flag, see R039/R044
R079 | p10 | footnotes_qualifiers | - | -
R080 | p10 | footnotes_qualifiers | - | -
R125 | p16 | footnotes_qualifiers | - | -
R130 | p19 | footnotes_qualifiers | - | -
R155 | p22 | footnotes_qualifiers | - | -
R164 | p24 | footnotes_qualifiers | - | -
R254 | p27 | footnotes_qualifiers | - | -
R255 | p27 | footnotes_qualifiers | RESTATED | xref R049 (termination footnote restated p6/p27)
R258 | p27 | footnotes_qualifiers | - | -
R259 | p27 | footnotes_qualifiers | - | -
R260 | p27 | footnotes_qualifiers | - | -
R318 | p28 | footnotes_qualifiers | - | -
R319 | p28 | footnotes_qualifiers | - | -
R322 | p28 | footnotes_qualifiers | - | -
R324 | p28 | footnotes_qualifiers | - | -
R325 | p28 | footnotes_qualifiers | - | -
R340 | p31 | footnotes_qualifiers | TYPO_AS_PRINTED | "30st September" as printed
R341 | p31 | footnotes_qualifiers | - | -

### forward_statements (7 rows)
R018 | p6 | forward_statements | FORWARD_TIMELINE | Bayview timeline
R021 | p6 | forward_statements | FORWARD_STRATEGY | aspiration without quantification
R024 | p6 | forward_statements | FORWARD_TIMELINE | cost benefits "over coming quarters", no figure
R106 | p13 | forward_statements | FORWARD_STRATEGY | aspiration without quantification
R107 | p13 | forward_statements | FORWARD_STRATEGY | aspiration without quantification
R108 | p13 | forward_statements | FORWARD_STRATEGY | aspiration without quantification
R141 | p21 | forward_statements | FORWARD_TIMELINE | 1-3-5 yr digital roadmap, no numbers

### dates (19 rows)
R001 | p1 | dates | - | -
R008 | p1 | dates | - | -
R011 | p1 | dates | - | -
R012 | p2 | dates | - | -
R051 | p6 | dates | - | -
R056 | p9 | dates | - | -
R057 | p9 | dates | - | -
R078 | p10 | dates | - | -
R098 | p11 | dates | - | -
R099 | p11 | dates | - | -
R124 | p16 | dates | - | -
R154 | p22 | dates | - | -
R156 | p22 | dates | - | -
R252 | p27 | dates | - | -
R253 | p27 | dates | - | -
R317 | p28 | dates | - | -
R327 | p30 | dates | - | -
R328 | p30 | dates | - | -
R339 | p31 | dates | TYPO_AS_PRINTED | see R340

### entities (45 rows)
R002 | p1 | entities | - | -
R004 | p1 | entities | - | -
R006 | p1 | entities | RESTATED | xref R333 (NSE symbol restated)
R007 | p1 | entities | - | -
R010 | p1 | entities | - | -
R015 | p6 | entities | - | -
R016 | p6 | entities | - | -
R017 | p6 | entities | - | -
R019 | p6 | entities | - | -
R020 | p6 | entities | - | -
R022 | p6 | entities | - | -
R023 | p6 | entities | - | -
R055 | p8 | entities | - | -
R058 | p9 | entities | - | -
R059 | p9 | entities | RESTATED | xref R092 (BMS restated)
R060 | p9 | entities | - | -
R062 | p9 | entities | RESTATED | xref R095 (Zoetis restated)
R063 | p9 | entities | RESTATED | xref R094 (Stelis restated)
R066 | p9 | entities | - | -
R067 | p9 | entities | - | -
R068 | p9 | entities | - | -
R069 | p9 | entities | - | -
R093 | p11 | entities | - | -
R094 | p11 | entities | RESTATED | xref R063 (Stelis restated)
R095 | p11 | entities | RESTATED | xref R062 (Zoetis restated)
R096 | p11 | entities | - | -
R097 | p11 | entities | RESTATED | xref R117 (regulator list restated)
R100 | p12 | entities | - | -
R101 | p12 | entities | - | -
R102 | p12 | entities | - | -
R103 | p12 | entities | - | -
R105 | p13 | entities | - | -
R116 | p15 | entities | - | -
R117 | p15 | entities | RESTATED | xref R097 (regulator list restated)
R123 | p16 | entities | - | -
R126 | p17 | entities | - | -
R127 | p18 | entities | - | -
R139 | p20 | entities | - | -
R140 | p21 | entities | - | -
R153 | p22 | entities | - | -
R157 | p23 | entities | REPEAT_LIST | overlaps R346 and p22 certifications; see M03-M05
R165 | p25 | entities | - | -
R326 | p30 | entities | - | -
R342 | p32 | entities | - | -
R343 | p32 | entities | CONTACT_DIFF | email in fulltext line 803 differs; see M08

### boilerplate_group (7 rows)
R344 | p19 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row
R345 | p24 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row
R346 | p23 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row
R347 | p3 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row
R348 | p1 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row
R349 | p4 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row
R350 | p24 | boilerplate_group | BOILERPLATE_GROUP | A1 grouped summary row

## 3. LINE-ITEM LEDGER (p27, p28; every line incl. margin lines)
page | line label | IDs
p27 | Revenue from operations | R166-R170 (5)
p27 | Other income | R171-R175 (5)
p27 | Reported revenue | R176-R180 (5)
p27 | Material costs | R181-R185 (5)
p27 | Staff costs | R186-R190 (5)
p27 | Other direct costs | R191-R195 (5)
p27 | Other expenses | R196-R200 (5)
p27 | Foreign exchange (gain)/loss, net | R201-R205 (5)
p27 | EBITDA | R206-R210 (5)
p27 | EBITDA Margin | R211-R213 (3)
p27 | Operating EBITDA (ex-other income) | R214-R218 (5)
p27 | Operating EBITDA Margin | R219-R221 (3)
p27 | Depreciation and Finance Cost | R222-R226 (5)
p27 | PBT | R227-R231 (5)
p27 | Tax | R232-R236 (5)
p27 | PAT before exceptional items | R237-R241 (5)
p27 | PAT after exceptional items | R242-R246 (5)
p27 | Shareholders' funds | R247-R247 (1)
p27 | Net Fixed assets | R248-R248 (1)
p27 | Other net assets (2) | R249-R249 (1)
p27 | Net cash/(debt) (3) | R250-R250 (1)
p27 | Total Use of Funds | R251-R251 (1)
p28 | Revenue from operations | R261-R263 (3)
p28 | Other income | R264-R266 (3)
p28 | Reported revenue | R267-R269 (3)
p28 | Material costs | R270-R272 (3)
p28 | Staff costs | R273-R275 (3)
p28 | Other direct costs | R276-R278 (3)
p28 | Other expenses | R279-R281 (3)
p28 | Foreign exchange (gain)/loss, net | R282-R284 (3)
p28 | EBITDA | R285-R287 (3)
p28 | EBITDA Margin | R288-R289 (2)
p28 | Operating EBITDA (ex-other income) | R290-R292 (3)
p28 | Operating EBITDA Margin | R293-R294 (2)
p28 | Depreciation and Finance Cost | R295-R297 (3)
p28 | PBT | R298-R300 (3)
p28 | Tax | R301-R303 (3)
p28 | PAT before exceptional items | R304-R306 (3)
p28 | PAT Margin | R307-R308 (2)
p28 | PAT after exceptional items | R309-R311 (3)
p28 | Shareholders' funds | R312-R312 (1)
p28 | Net Fixed assets | R313-R313 (1)
p28 | Other net assets (3) | R314-R314 (1)
p28 | Net cash/(debt) (4) | R315-R315 (1)
p28 | Total Use of Funds | R316-R316 (1)

## 4. ZERO_STANDING
R149 | p22 | zero waste to direct landfill | ZERO_STANDING | sustainability KPI stated at nil.

## 5. MISSING_FROM_STRUCTURED (loop to A1)
ID | page | line | claim text | kind | flag
M01 | p1 | line 23 | Company phone "T +91 80 6891 9191" in letterhead | boilerplate | MISSING_FROM_STRUCTURED
M02 | p1 | line 31 | Exchange address pincodes: Mumbai 400 001 (BSE), 400 051 (NSE) | boilerplate | MISSING_FROM_STRUCTURED
M03 | p22 | line 488 | ISO 45001:2018 Occupational Health accreditation (p22 bullet; R157 is on p23) | certification | MISSING_FROM_STRUCTURED
M04 | p22 | line 508 | ISO 50001:2018 Energy Management Certificate for Bengaluru & Mangaluru (p22 bullet) | certification | MISSING_FROM_STRUCTURED
M05 | p23 | line 524 | NABL (ISO/IEC 17025) certification for Safety Assessment and Large Molecule Bioanalytical Laboratory (R157 omits 17025) | certification | MISSING_FROM_STRUCTURED
M06 | p24 | line 546 | "Management 5.0 summit" event name in award text | award fine print | MISSING_FROM_STRUCTURED
M07 | p24 | line 559 | "29th Edition of the World HRD" Dream Companies to Work Award | award fine print | MISSING_FROM_STRUCTURED
M08 | p32 | line 795/803 | IR email in fulltext line 803 reads soudabi.neduvanchery1@syngeneintl.com; R343 shows investor@syngeneintl.com; digits in YouTube URL line 795 | contact discrepancy | MISSING_FROM_STRUCTURED
M09 | p3,5,7,11-14,16-20,25,26,29,32 | line 262-805 | Footer page numbers (10,11,12,15,16,17,18,19,24,31) and divider section numbers (1-5): navigation furniture, no structured rows; not disclosures | furniture | MISSING_FROM_STRUCTURED

## 6. ID ACCOUNTABILITY
Every R001-R350 appears once in section 2. Category counts: dates=19; entities=45; slide_numbers=107; footnotes_qualifiers=23; forward_statements=7; line_items_PL=132; line_items_BS=10; boilerplate_group=7
ids_in_structured: 350 | ids_referenced_in_ledger: 350 | orphan_ids: [] | match: yes
