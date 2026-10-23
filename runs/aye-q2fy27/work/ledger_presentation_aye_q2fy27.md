# A2 LEDGER: Aye Finance Limited (AYE) Q2 FY27 investor presentation

Correction loop 1 (A5 COV-1..COV-4): section 8 previously said none missing; corrected. Added M01 (fulltext line 667, p28) and M02 (line 807, p34) as MISSING_FROM_STRUCTURED. Added A1 label correction for R076/R077 (section 8b). A1 file not edited. Structured IDs unchanged (913).

Source: A1 structured extraction only. Rows are referenced by ID; claim text stays in the structured file.

ids_in_structured: 913 | ids_referenced_in_ledger: 913 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides            grep_count: 44   sweep_count: 44   match: yes (38 slides with rows + 6 divider slides, 44 total)
category: slide_numbers     grep_count: 744   sweep_count: 744   match: yes
category: footnotes_qualifiers grep_count: 56   sweep_count: 56   match: yes
category: entities (incl summary) grep_count: 55   sweep_count: 55   match: yes
category: forward           grep_count: 25   sweep_count: 25   match: yes
category: dates             grep_count: 33   sweep_count: 33   match: yes
category: zero_standing     grep_count: 5   sweep_count: 5   match: yes
category: all_ids           grep_count: 913   sweep_count: 913   match: yes
A1 header counts: NUMBER 744 | ENTITY 48 + 7 summary | FORWARD 25 | DATE 33 | QUALIFIER 56 -> recount NUMBER 744 ENTITY 48 SUMMARY 7 FORWARD 25 DATE 33 QUALIFIER 56
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (number | title | content type | row IDs | counts | flags)
SLIDE | TITLE (fulltext) | CONTENT | ROW_IDS | N/E/F/D/Q | A2 FLAGS
1 | AYE FINANCE LIMITED | text | R001-R015 | 1/9/0/3/2 | 
2 | Aye Finance Limited | text | R016-R016 | 0/0/0/1/0 | 
3 | Safe Harbor | text | R017-R019 | 0/1/2/0/0 | 
4 | Index                           Page 4-9 | text | R020-R020 | 0/1/0/0/0 | 
5 | Performance Highlights | section divider (text) | none | 0 | NO_ROWS (divider; section named in R020)
6 | Management Commentary | chart/table | R021-R070 | 38/2/4/2/4 | 
7 | Key Highlights – Q2FY27 | chart/table | R071-R096 | 24/0/0/1/1 | 
8 | Key Highlights – Q2FY27 | chart/table | R097-R127 | 27/0/0/1/3 | 
9 | Key Highlights – H1FY27 | chart/table | R128-R146 | 18/0/0/0/1 | 
10 | Key Highlights – H1FY27 | chart/table | R147-R164 | 16/0/0/0/2 | 
11 | Company Overview | section divider (text) | none | 0 | NO_ROWS (divider; section named in R020)
12 | India’s Leading Micro-enterprise Lender | table | R165-R180 | 11/3/0/1/1 | 
13 | Journey So Far | chart/table | R181-R211 | 27/1/1/2/0 | ZERO_STANDING
14 | PAN India Presence | chart/table | R212-R266 | 50/1/0/1/3 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer)
15 | Unique Positioning: Focused on Unorganised Micro-MSMEs | text | R267-R276 | 6/2/0/0/2 | 
16 | Our Customers are Micro Scale MSMEs… | text | R277-R281 | 4/1/0/0/0 | 
17 | Comprehensive Product Offerings | table | R282-R296 | 10/1/0/1/3 | 
18 | Board of Directors | text | R297-R305 | 1/8/0/0/0 | 
19 | Strong Management Team | chart/table | R306-R328 | 11/11/0/0/1 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer)
20 | Liquidity Profile | section divider (text) | none | 0 | NO_ROWS (divider; section named in R020)
21 | Diversified Lender Base with Reducing Cost of Borrowing | chart/table | R329-R359 | 25/1/0/2/3 | CHART_SCRAMBLED(3 rows, attribution not determinable; A3 must not infer)
22 | Liability Profile | chart/table | R360-R380 | 17/0/1/2/1 | 
23 | Asset Quality | section divider (text) | none | 0 | NO_ROWS (divider; section named in R020)
24 | Asset Quality Trends – Q2FY27 | table | R381-R395 | 15/0/0/0/0 | 
25 | Asset Quality Trends – H1FY27 | table | R396-R405 | 10/0/0/0/0 | 
26 | Collection Efficiency and PAR Trends – Overall | chart/table | R406-R434 | 25/0/0/2/2 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer)
27 | Collection Efficiency and PAR Trends - Key States | chart/table | R435-R509 | 72/1/0/0/2 | CHART_SCRAMBLED(25 rows, attribution not determinable; A3 must not infer)
28 | Summary of Provisions                   Stage 1  Stage 2  St | chart/table | R510-R561 | 47/0/0/3/2 | CHART_SCRAMBLED(18 rows, attribution not determinable; A3 must not infer)
29 | Robust Multi-Tiered Collection Capabilities | text | R562-R564 | 1/2/0/0/0 | 
30 | Key Efficiency Drivers | section divider (text) | none | 0 | NO_ROWS (divider; section named in R020)
31 | Efficiency Drivers – Technology | table | R565-R573 | 8/1/0/0/0 | 
32 | Efficiency Drivers – Mortgage Business | chart/table | R574-R589 | 11/0/2/1/2 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer)
33 | Efficiency Drivers – Repeat Business | text | R590-R595 | 5/0/1/0/0 | 
34 | Efficiency Drivers – Branch Network | chart/table | R596-R635 | 30/0/3/2/5 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer); ZERO_STANDING
35 | FY27 Guidance                                  FY27        Q | table | R636-R657 | 15/0/5/1/1 | 
36 | Three Year Vision : Growth | text | R658-R669 | 5/0/6/1/0 | 
37 | Financial Overview | section divider (text) | none | 0 | NO_ROWS (divider; section named in R020)
38 | Profit & Loss Summary | chart/table | R670-R737 | 64/0/0/1/3 | 
39 | Balance Sheet Summary                             30th Sept  | chart/table | R738-R778 | 36/1/0/1/3 | CHART_SCRAMBLED(28 rows, attribution not determinable; A3 must not infer)
40 | ROE Tree | chart/table | R779-R860 | 79/0/0/1/2 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer); ZERO_STANDING
41 | Shareholding Pattern                              More than  | chart/table | R861-R876 | 12/2/0/1/1 | CHART_SCRAMBLED(1 rows, attribution not determinable; A3 must not infer)
42 | CSR Activities | chart/table | R877-R903 | 23/2/0/2/0 | 
43 | Glossary | text | R904-R910 | 0/1/0/0/6 | 
44 | Contact Us                           Contact Information | text | R911-R913 | 0/3/0/0/0 | 

DROPPED_SLIDE: not assessable, prior ledger NOT AVAILABLE.

## 2. SLIDE NUMBERS
ROW_ID | category | A2 flags | cross-ref / note
R012 | NUMBER p1 | - | BSE scrip code
R024 | NUMBER p6 | - | disbursements QoQ growth Q2 FY27
R025 | NUMBER p6 | - | disbursements Q2 FY27
R026 | NUMBER p6 | - | disbursements H1 FY27
R029 | NUMBER p6 | - | AUM Q2 FY27
R030 | NUMBER p6 | - | AUM YoY growth
R031 | NUMBER p6 | - | AUM QoQ growth
R032 | NUMBER p6 | - | new borrowers added Q2 FY27
R033 | NUMBER p6 | - | active borrower base
R034 | NUMBER p6 | - | AUM per employee Q2 FY27
R035 | NUMBER p6 | - | AUM per employee Q2 FY26
R036 | NUMBER p6 | - | Opex ratio Q2 FY27
R038 | NUMBER p6 | - | GNPA Q2 FY27
R039 | NUMBER p6 | - | GNPA sequential improvement
R040 | NUMBER p6 | - | PAR X Q2 FY27
R041 | NUMBER p6 | - | PAR X QoQ improvement
R042 | NUMBER p6 | - | PAR X improvement vs Q2 FY26
R043 | NUMBER p6 | - | PAR X Q2 FY26
R044 | NUMBER p6 | - | credit cost Q2 FY27
R046 | NUMBER p6 | - | guided credit cost range
R047 | NUMBER p6 | - | Non-OD collection efficiency Q2 FY27
R048 | NUMBER p6 | - | Bucket 1 collection efficiency Q2 FY27
R049 | NUMBER p6 | - | Gross Total Income YoY Q2 FY27
R050 | NUMBER p6 | - | Gross Total Income QoQ Q2 FY27
R051 | NUMBER p6 | - | Gross Total Income Q2 FY27
R052 | NUMBER p6 | - | Net Interest Margin Q2 FY27
R053 | NUMBER p6 | - | PAT YoY Q2 FY27
R054 | NUMBER p6 | - | PAT QoQ Q2 FY27
R055 | NUMBER p6 | - | PAT Q2 FY27
R057 | NUMBER p6 | - | Gross Total Income YoY H1 FY27
R058 | NUMBER p6 | - | Gross Total Income H1 FY27
R059 | NUMBER p6 | - | NIM H1 FY27
R060 | NUMBER p6 | - | PPoP YoY H1 FY27
R061 | NUMBER p6 | - | PPoP H1 FY27
R062 | NUMBER p6 | - | PAT H1 FY27
R063 | NUMBER p6 | - | PAT H1 FY26
R064 | NUMBER p6 | - | PAT growth H1 FY27
R065 | NUMBER p6 | - | RoA H1 FY27
R066 | NUMBER p6 | - | RoE H1 FY27
R072 | NUMBER p7 | - | AUM Q2FY26 Rs Cr
R073 | NUMBER p7 | - | AUM Q1FY27 Rs Cr
R074 | NUMBER p7 | - | AUM Q2FY27 Rs Cr
R075 | NUMBER p7 | - | AUM YoY growth
R076 | NUMBER p7 | - | Disbursements Q2FY26 Rs Cr
R077 | NUMBER p7 | - | Disbursements Q1FY27 Rs Cr
R078 | NUMBER p7 | - | Disbursements Q2FY27 Rs Cr
R079 | NUMBER p7 | - | Disbursements YoY growth
R080 | NUMBER p7 | - | Gross Total Income Q2FY26 Rs Cr
R081 | NUMBER p7 | - | Gross Total Income Q1FY27 Rs Cr
R082 | NUMBER p7 | - | Gross Total Income Q2FY27 Rs Cr
R083 | NUMBER p7 | - | Gross Total Income YoY growth
R084 | NUMBER p7 | - | Net Interest Income Q2FY26 Rs Cr
R085 | NUMBER p7 | - | Net Interest Income Q1FY27 Rs Cr
R086 | NUMBER p7 | - | Net Interest Income Q2FY27 Rs Cr
R087 | NUMBER p7 | - | Net Interest Income YoY growth
R088 | NUMBER p7 | - | PPoP Q2FY26 Rs Cr
R089 | NUMBER p7 | - | PPoP Q1FY27 Rs Cr
R090 | NUMBER p7 | - | PPoP Q2FY27 Rs Cr
R091 | NUMBER p7 | - | PPoP YoY growth
R092 | NUMBER p7 | - | PAT Q2FY26 Rs Cr
R093 | NUMBER p7 | - | PAT Q1FY27 Rs Cr
R094 | NUMBER p7 | - | PAT Q2FY27 Rs Cr
R095 | NUMBER p7 | - | PAT YoY growth
R097 | NUMBER p8 | - | Average Yield Q2FY26 (chart order)
R098 | NUMBER p8 | - | Average Yield Q1FY27 (chart order)
R099 | NUMBER p8 | - | Average Yield Q2FY27 (chart order)
R100 | NUMBER p8 | - | NIM Q2FY26 (chart order)
R101 | NUMBER p8 | - | NIM Q1FY27 (chart order)
R102 | NUMBER p8 | - | NIM Q2FY27 (chart order)
R103 | NUMBER p8 | - | Cost to Income Q2FY26 (chart order)
R104 | NUMBER p8 | - | Cost to Income Q1FY27 (chart order)
R105 | NUMBER p8 | - | Cost to Income Q2FY27 (chart order)
R106 | NUMBER p8 | - | PAR X Q2FY26 (chart order)
R107 | NUMBER p8 | - | PAR X Q1FY27 (chart order)
R108 | NUMBER p8 | - | PAR X Q2FY27 (chart order)
R109 | NUMBER p8 | - | GNPA Q2FY26 (chart order)
R110 | NUMBER p8 | - | GNPA Q1FY27 (chart order)
R111 | NUMBER p8 | - | GNPA Q2FY27 (chart order)
R112 | NUMBER p8 | - | NNPA Q2FY26 (chart order)
R113 | NUMBER p8 | - | NNPA Q1FY27 (chart order)
R114 | NUMBER p8 | - | NNPA Q2FY27 (chart order)
R115 | NUMBER p8 | - | RoA (on assets) Q2FY26 (chart order)
R116 | NUMBER p8 | - | RoA (on assets) Q1FY27 (chart order)
R117 | NUMBER p8 | - | RoA (on assets) Q2FY27 (chart order)
R118 | NUMBER p8 | - | RoE Q2FY26 (chart order)
R119 | NUMBER p8 | - | RoE Q1FY27 (chart order)
R120 | NUMBER p8 | - | RoE Q2FY27 (chart order)
R121 | NUMBER p8 | - | Book Value Per Share, 30 Sep 2026
R122 | NUMBER p8 | - | Networth, 30 Sep 2026
R125 | NUMBER p8 | - | equity infusion Feb-26
R128 | NUMBER p9 | - | AUM H1FY27 Rs Cr
R129 | NUMBER p9 | - | AUM H1FY26 Rs Cr
R130 | NUMBER p9 | - | AUM YoY
R131 | NUMBER p9 | - | Disbursements H1FY27 Rs Cr
R132 | NUMBER p9 | - | Disbursements H1FY26 Rs Cr
R133 | NUMBER p9 | - | Disbursements YoY H1
R134 | NUMBER p9 | - | Gross Total Income H1FY27 Rs Cr
R135 | NUMBER p9 | - | Gross Total Income H1FY26 Rs Cr
R136 | NUMBER p9 | - | Gross Total Income YoY H1
R137 | NUMBER p9 | - | Net Interest Income H1FY27 Rs Cr
R138 | NUMBER p9 | - | Net Interest Income H1FY26 Rs Cr
R139 | NUMBER p9 | - | Net Interest Income YoY H1
R140 | NUMBER p9 | - | PPoP H1FY27 Rs Cr
R141 | NUMBER p9 | - | PPoP H1FY26 Rs Cr
R142 | NUMBER p9 | - | PPoP YoY H1
R143 | NUMBER p9 | - | PAT H1FY27 Rs Cr
R144 | NUMBER p9 | - | PAT H1FY26 Rs Cr
R145 | NUMBER p9 | - | PAT YoY H1
R148 | NUMBER p10 | - | Average Yield H1FY26 (chart order)
R149 | NUMBER p10 | - | Average Yield H1FY27 (chart order)
R150 | NUMBER p10 | - | NIM H1FY26 (chart order)
R151 | NUMBER p10 | - | NIM H1FY27 (chart order)
R152 | NUMBER p10 | - | Cost to Income H1FY26 (chart order)
R153 | NUMBER p10 | - | Cost to Income H1FY27 (chart order)
R154 | NUMBER p10 | - | PAR X H1FY26 (chart order)
R155 | NUMBER p10 | - | PAR X H1FY27 (chart order)
R156 | NUMBER p10 | - | GNPA H1FY26 (chart order)
R157 | NUMBER p10 | - | GNPA H1FY27 (chart order)
R158 | NUMBER p10 | - | NNPA H1FY26 (chart order)
R159 | NUMBER p10 | - | NNPA H1FY27 (chart order)
R160 | NUMBER p10 | - | RoA H1FY26 (chart order, layout attribution)
R161 | NUMBER p10 | - | RoA H1FY27 (chart order)
R162 | NUMBER p10 | - | RoE H1FY26 (chart order)
R163 | NUMBER p10 | - | RoE H1FY27 (chart order)
R169 | NUMBER p12 | - | AUM H1FY27
R170 | NUMBER p12 | - | Disbursements H1FY27
R171 | NUMBER p12 | - | Total Revenue H1FY27
R172 | NUMBER p12 | - | Branches across 18 states and 3 UTs
R173 | NUMBER p12 | - | Employees serving micro entrepreneurs
R174 | NUMBER p12 | - | Total equity
R175 | NUMBER p12 | - | unique clusters underwriting methodology
R176 | NUMBER p12 | - | active customers
R177 | NUMBER p12 | - | in-house origination model
R178 | NUMBER p12 | - | branches digital-first collections
R179 | NUMBER p12 | - | average ticket size
R183 | NUMBER p13 | - | states added FY2016
R184 | NUMBER p13 | - | states added FY2018
R185 | NUMBER p13 | - | states added FY2020
R186 | NUMBER p13 | - | states added FY2022
R187 | NUMBER p13 | - | states added FY2023
R188 | NUMBER p13 | ZERO_STANDING | states added FY2024 ZERO_STANDING
R189 | NUMBER p13 | ZERO_STANDING | states added FY2025 ZERO_STANDING
R190 | NUMBER p13 | ZERO_STANDING | states added FY2026 ZERO_STANDING
R191 | NUMBER p13 | - | total states FY2016
R192 | NUMBER p13 | - | total states FY2018
R193 | NUMBER p13 | - | total states FY2020
R194 | NUMBER p13 | - | total states FY2022
R195 | NUMBER p13 | - | total states FY2023
R196 | NUMBER p13 | - | total states FY2024
R197 | NUMBER p13 | - | total states FY2025
R198 | NUMBER p13 | - | total states FY2026
R199 | NUMBER p13 | - | branches (chart order, first)
R200 | NUMBER p13 | - | branches (chart order, second)
R201 | NUMBER p13 | - | branches (chart order, third)
R202 | NUMBER p13 | - | branches (chart order, fourth)
R203 | NUMBER p13 | - | branches (chart order, fifth)
R204 | NUMBER p13 | - | branches (chart order, sixth)
R205 | NUMBER p13 | - | AUM Rs Cr (chart order, first)
R206 | NUMBER p13 | - | AUM Rs Cr (chart order, second)
R207 | NUMBER p13 | - | AUM Rs Cr (chart order, third)
R208 | NUMBER p13 | - | AUM Rs Cr (chart order, fourth)
R209 | NUMBER p13 | - | AUM Rs Cr (chart order, fifth)
R212 | NUMBER p14 | - | AUM by Industry segment Mar-24 (chart order)
R213 | NUMBER p14 | - | AUM by Industry segment Mar-25 (chart order)
R214 | NUMBER p14 | - | AUM by Industry segment Mar-26 (chart order)
R215 | NUMBER p14 | - | AUM by Industry segment Sep-26 (chart order)
R216 | NUMBER p14 | - | Geographical AUM mix share (region label unresolved)
R217 | NUMBER p14 | - | Geographical AUM mix share
R218 | NUMBER p14 | - | Geographical AUM mix share
R219 | NUMBER p14 | - | Geographical AUM mix share
R220 | NUMBER p14 | - | Geographical AUM mix share
R221 | NUMBER p14 | - | Geographical AUM mix share
R222 | NUMBER p14 | - | state share PB (map)
R223 | NUMBER p14 | - | state share J&K (map)
R224 | NUMBER p14 | - | state share HR (map)
R225 | NUMBER p14 | - | state share CH (map)
R226 | NUMBER p14 | - | state share HP (map)
R227 | NUMBER p14 | - | state share DL (map)
R228 | NUMBER p14 | - | state share UK (map)
R229 | NUMBER p14 | - | state share RJ (map)
R230 | NUMBER p14 | - | state share UP (map)
R231 | NUMBER p14 | - | state share BR (map)
R232 | NUMBER p14 | - | state share GJ (map)
R233 | NUMBER p14 | - | state share MP (map)
R234 | NUMBER p14 | - | state share JH/WB (map)
R235 | NUMBER p14 | - | state share (map)
R236 | NUMBER p14 | - | state share (map)
R237 | NUMBER p14 | - | state share OR (map)
R238 | NUMBER p14 | - | state share MH (map)
R239 | NUMBER p14 | - | state share TL (map)
R240 | NUMBER p14 | - | state share KA (map)
R241 | NUMBER p14 | - | state share AP (map)
R242 | NUMBER p14 | - | state share TN (map)
R243 | NUMBER p14 | - | industry mix segment value (chart)
R244 | NUMBER p14 | - | industry mix segment value (chart)
R245 | NUMBER p14 | - | industry mix segment value (chart)
R246 | NUMBER p14 | - | industry mix segment value (chart)
R247 | NUMBER p14 | - | industry mix segment value (chart)
R248 | NUMBER p14 | - | industry mix segment value (chart)
R249 | NUMBER p14 | - | industry mix segment value (chart)
R250 | NUMBER p14 | - | industry mix segment value (chart)
R251 | NUMBER p14 | - | industry mix segment value (chart)
R252 | NUMBER p14 | - | industry mix segment value (chart)
R253 | NUMBER p14 | - | industry mix segment value (chart)
R254 | NUMBER p14 | - | industry mix segment value (chart)
R255 | NUMBER p14 | - | North region branches (layout)
R256 | NUMBER p14 | - | East region branches (layout)
R257 | NUMBER p14 | - | West region branches (layout)
R258 | NUMBER p14 | - | South branches
R259 | NUMBER p14 | - | Branches
R260 | NUMBER p14 | - | Active Customers
R261 | NUMBER p14 | - | No of Employees
R269 | NUMBER p15 | - | income, wage earners segment
R270 | NUMBER p15 | - | income, segment
R271 | NUMBER p15 | - | income, self-employed segment
R272 | NUMBER p15 | - | income, segment
R273 | NUMBER p15 | - | turnover, Unorganised Micro MSME
R274 | NUMBER p15 | - | turnover, Organised Micro MSME
R277 | NUMBER p16 | - | business clusters understood (over 70)
R278 | NUMBER p16 | - | average customer turnover
R279 | NUMBER p16 | - | permanent business setup minimum
R280 | NUMBER p16 | - | customers owned residence or place of business or both
R282 | NUMBER p17 | - | AUM split LAP
R283 | NUMBER p17 | - | AUM split Saral Property Loans
R284 | NUMBER p17 | - | AUM split Hypothecation Loans
R285 | NUMBER p17 | - | AUM Sep-26 Rs Cr
R286 | NUMBER p17 | - | ATS on disbursement LAP INR Lakhs
R287 | NUMBER p17 | - | ATS on disbursement Saral Property Loans INR Lakhs
R288 | NUMBER p17 | - | ATS on disbursement Hypothecation Loans INR Lakhs
R289 | NUMBER p17 | - | active loans LAP
R290 | NUMBER p17 | - | active loans Saral Property Loans
R291 | NUMBER p17 | - | active loans Hypothecation Loans
R305 | NUMBER p18 | - | Sanjay Sharma experience (over)
R317 | NUMBER p19 | - | tenure at Aye Finance
R318 | NUMBER p19 | - | tenure at Aye Finance
R319 | NUMBER p19 | - | tenure at Aye Finance
R320 | NUMBER p19 | - | tenure at Aye Finance
R321 | NUMBER p19 | - | tenure at Aye Finance
R322 | NUMBER p19 | - | tenure at Aye Finance
R323 | NUMBER p19 | - | tenure at Aye Finance
R324 | NUMBER p19 | - | tenure at Aye Finance
R325 | NUMBER p19 | - | tenure at Aye Finance
R326 | NUMBER p19 | - | tenure at Aye Finance
R327 | NUMBER p19 | - | tenure at Aye Finance
R329 | NUMBER p21 | - | Banks share of lender base
R330 | NUMBER p21 | - | Financial Institutions share of lender base
R331 | NUMBER p21 | - | Development Financial Institutions share
R333 | NUMBER p21 | - | retail borrowings within Financial Institutions
R334 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R335 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R336 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R337 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R338 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R339 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R340 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R341 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R342 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R343 | NUMBER p21 | - | CoB/Incremental CoB (chart order)
R345 | NUMBER p21 | - | debt raised Rs Cr (chart order)
R346 | NUMBER p21 | - | debt raised Rs Cr (chart order)
R347 | NUMBER p21 | - | debt raised Rs Cr (chart order)
R348 | NUMBER p21 | - | debt raised Rs Cr (chart order)
R349 | NUMBER p21 | - | debt raised Rs Cr (chart order)
R350 | NUMBER p21 | - | borrowing mix instrument type (chart)
R351 | NUMBER p21 | - | borrowing mix instrument type (chart)
R352 | NUMBER p21 | - | borrowing mix instrument type (chart)
R353 | NUMBER p21 | - | borrowing mix instrument type (chart)
R355 | NUMBER p21 | - | credit rating
R356 | NUMBER p21 | SCRAMBLED_ATTRIBUTION | credit rating (label scrambled; agency not shown)
R360 | NUMBER p22 | - | ALM cumulative (chart; two occurrences)
R361 | NUMBER p22 | - | ALM cumulative Rs Cr
R362 | NUMBER p22 | - | ALM cumulative Rs Cr
R363 | NUMBER p22 | - | ALM cumulative Rs Cr
R364 | NUMBER p22 | - | ALM cumulative Rs Cr
R365 | NUMBER p22 | - | ALM cumulative Rs Cr
R366 | NUMBER p22 | - | ALM cumulative Rs Cr
R367 | NUMBER p22 | - | ALM cumulative Rs Cr
R368 | NUMBER p22 | - | ALM cumulative Rs Cr
R369 | NUMBER p22 | - | Capital Adequacy Ratio (chart order)
R370 | NUMBER p22 | - | Capital Adequacy Ratio (chart order)
R371 | NUMBER p22 | - | Capital Adequacy Ratio (chart order)
R372 | NUMBER p22 | - | Capital Adequacy Ratio (chart order)
R373 | NUMBER p22 | - | Networth Rs Cr Mar-26
R374 | NUMBER p22 | - | Networth Rs Cr Sep-26
R375 | NUMBER p22 | - | Networth Rs Cr (chart order)
R376 | NUMBER p22 | - | Networth Rs Cr (chart order)
R381 | NUMBER p24 | - | PAR X Q2FY26
R382 | NUMBER p24 | - | PAR X Q1FY27
R383 | NUMBER p24 | - | PAR X Q2FY27
R384 | NUMBER p24 | - | PAR 30 Q2FY26 (chart order)
R385 | NUMBER p24 | - | PAR 30 Q1FY27 (chart order)
R386 | NUMBER p24 | - | PAR 30 Q2FY27 (chart order)
R387 | NUMBER p24 | - | Credit cost annualized Q2FY26
R388 | NUMBER p24 | - | Credit cost annualized Q1FY27
R389 | NUMBER p24 | - | Credit cost annualized Q2FY27
R390 | NUMBER p24 | - | Non-OD collection efficiency Q2FY26
R391 | NUMBER p24 | - | Non-OD collection efficiency Q1FY27
R392 | NUMBER p24 | - | Non-OD collection efficiency Q2FY27
R393 | NUMBER p24 | - | Bucket 1 collection efficiency Q2FY26
R394 | NUMBER p24 | - | Bucket 1 collection efficiency Q1FY27
R395 | NUMBER p24 | - | Bucket 1 collection efficiency Q2FY27
R396 | NUMBER p25 | - | PAR X H1FY26
R397 | NUMBER p25 | - | PAR X H1FY27
R398 | NUMBER p25 | - | PAR 30 H1FY26 (chart order)
R399 | NUMBER p25 | - | PAR 30 H1FY27 (chart order)
R400 | NUMBER p25 | - | Credit cost annualized H1FY26
R401 | NUMBER p25 | - | Credit cost annualized H1FY27
R402 | NUMBER p25 | - | Non-OD collection efficiency H1FY26
R403 | NUMBER p25 | - | Non-OD collection efficiency H1FY27
R404 | NUMBER p25 | - | Bucket 1 collection efficiency H1FY27 (chart order)
R405 | NUMBER p25 | - | Bucket 1 collection efficiency H1FY26 (chart order)
R406 | NUMBER p26 | - | Non-OD CE monthly (chart, Apr-Sep 26)
R407 | NUMBER p26 | - | Non-OD CE monthly (chart)
R408 | NUMBER p26 | - | Non-OD CE monthly (chart)
R409 | NUMBER p26 | - | Non-OD CE monthly (chart)
R410 | NUMBER p26 | - | Non-OD CE monthly (chart)
R411 | NUMBER p26 | - | Non-OD CE monthly (chart)
R412 | NUMBER p26 | - | Bucket 1 CE monthly (chart)
R413 | NUMBER p26 | - | Bucket 1 CE monthly (chart)
R414 | NUMBER p26 | - | Bucket 1 CE monthly (chart)
R415 | NUMBER p26 | - | Bucket 1 CE monthly (chart)
R416 | NUMBER p26 | - | Bucket 1 CE monthly (chart)
R417 | NUMBER p26 | - | Bucket 1 CE monthly (chart)
R418 | NUMBER p26 | - | PAR X monthly (chart)
R419 | NUMBER p26 | - | PAR X monthly (chart)
R420 | NUMBER p26 | - | PAR X monthly (chart)
R421 | NUMBER p26 | - | PAR X monthly (chart)
R422 | NUMBER p26 | - | PAR X monthly (chart)
R423 | NUMBER p26 | - | PAR X monthly (chart)
R424 | NUMBER p26 | - | PAR 30 monthly (chart)
R425 | NUMBER p26 | - | PAR 30 monthly (chart)
R426 | NUMBER p26 | - | PAR 30 monthly (chart)
R427 | NUMBER p26 | - | PAR 30 monthly (chart)
R428 | NUMBER p26 | - | PAR 30 monthly (chart)
R429 | NUMBER p26 | - | PAR 30 monthly (chart)
R431 | NUMBER p26 | - | portfolio originated post Jun-24
R437 | NUMBER p27 | - | Bihar Non-OD CE Apr-26
R438 | NUMBER p27 | - | Bihar Non-OD CE May-26
R439 | NUMBER p27 | - | Bihar Non-OD CE Jun-26
R440 | NUMBER p27 | - | Bihar Non-OD CE Jul-26
R441 | NUMBER p27 | - | Bihar Non-OD CE Aug-26
R442 | NUMBER p27 | - | Bihar Non-OD CE Sep-26
R443 | NUMBER p27 | - | Uttar Pradesh Non-OD CE Apr-26
R444 | NUMBER p27 | - | Uttar Pradesh Non-OD CE May-26
R445 | NUMBER p27 | - | Uttar Pradesh Non-OD CE Jun-26
R446 | NUMBER p27 | - | Uttar Pradesh Non-OD CE Jul-26
R447 | NUMBER p27 | - | Uttar Pradesh Non-OD CE Aug-26
R448 | NUMBER p27 | - | Uttar Pradesh Non-OD CE Sep-26
R449 | NUMBER p27 | - | Rajasthan Non-OD CE Apr-26
R450 | NUMBER p27 | - | Rajasthan Non-OD CE May-26
R451 | NUMBER p27 | - | Rajasthan Non-OD CE Jun-26
R452 | NUMBER p27 | - | Rajasthan Non-OD CE Jul-26
R453 | NUMBER p27 | - | Rajasthan Non-OD CE Aug-26
R454 | NUMBER p27 | - | Rajasthan Non-OD CE Sep-26
R455 | NUMBER p27 | - | Rest States Non-OD CE Apr-26
R456 | NUMBER p27 | - | Rest States Non-OD CE May-26
R457 | NUMBER p27 | - | Rest States Non-OD CE Jun-26
R458 | NUMBER p27 | - | Rest States Non-OD CE Jul-26
R459 | NUMBER p27 | - | Rest States Non-OD CE Aug-26
R460 | NUMBER p27 | - | Rest States Non-OD CE Sep-26
R461 | NUMBER p27 | - | Bihar Bucket 1 CE Apr-26
R462 | NUMBER p27 | - | Bihar Bucket 1 CE May-26
R463 | NUMBER p27 | - | Bihar Bucket 1 CE Jun-26
R464 | NUMBER p27 | - | Bihar Bucket 1 CE Jul-26
R465 | NUMBER p27 | - | Bihar Bucket 1 CE Aug-26
R466 | NUMBER p27 | - | Bihar Bucket 1 CE Sep-26
R467 | NUMBER p27 | - | Uttar Pradesh Bucket 1 CE Apr-26
R468 | NUMBER p27 | - | Uttar Pradesh Bucket 1 CE May-26
R469 | NUMBER p27 | - | Uttar Pradesh Bucket 1 CE Jun-26
R470 | NUMBER p27 | - | Uttar Pradesh Bucket 1 CE Jul-26
R471 | NUMBER p27 | - | Uttar Pradesh Bucket 1 CE Aug-26
R472 | NUMBER p27 | - | Uttar Pradesh Bucket 1 CE Sep-26
R473 | NUMBER p27 | - | Rajasthan Bucket 1 CE Apr-26
R474 | NUMBER p27 | - | Rajasthan Bucket 1 CE May-26
R475 | NUMBER p27 | - | Rajasthan Bucket 1 CE Jun-26
R476 | NUMBER p27 | - | Rajasthan Bucket 1 CE Jul-26
R477 | NUMBER p27 | - | Rajasthan Bucket 1 CE Aug-26
R478 | NUMBER p27 | - | Rajasthan Bucket 1 CE Sep-26
R479 | NUMBER p27 | - | Rest States Bucket 1 CE Apr-26
R480 | NUMBER p27 | - | Rest States Bucket 1 CE May-26
R481 | NUMBER p27 | - | Rest States Bucket 1 CE Jun-26
R482 | NUMBER p27 | - | Rest States Bucket 1 CE Jul-26
R483 | NUMBER p27 | - | Rest States Bucket 1 CE Aug-26
R484 | NUMBER p27 | - | Rest States Bucket 1 CE Sep-26
R485 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R486 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R487 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R488 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R489 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R490 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R491 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R492 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R493 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R494 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R495 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R496 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R497 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R498 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R499 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R500 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R501 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R502 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R503 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R504 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R505 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R506 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R507 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R508 | NUMBER p27 | SCRAMBLED_ATTRIBUTION | PAR X state-month (chart, attribution scrambled)
R513 | NUMBER p28 | - | Gross loans Stage 1, 30 Sep 2026 Rs Cr
R514 | NUMBER p28 | - | Gross loans Stage 2, 30 Sep 2026
R515 | NUMBER p28 | - | Gross loans Stage 3, 30 Sep 2026
R516 | NUMBER p28 | - | Gross loans total, 30 Sep 2026
R517 | NUMBER p28 | - | ECL provision Stage 1, 30 Sep 2026
R518 | NUMBER p28 | - | ECL provision Stage 2, 30 Sep 2026
R519 | NUMBER p28 | - | ECL provision Stage 3, 30 Sep 2026
R520 | NUMBER p28 | - | ECL provision total, 30 Sep 2026
R521 | NUMBER p28 | - | Net loans Stage 1, 30 Sep 2026
R522 | NUMBER p28 | - | Net loans Stage 2, 30 Sep 2026
R523 | NUMBER p28 | - | Net loans Stage 3, 30 Sep 2026
R524 | NUMBER p28 | - | Net loans total, 30 Sep 2026
R525 | NUMBER p28 | - | Provision % Stage 1, 30 Sep 2026
R526 | NUMBER p28 | - | Provision % Stage 2, 30 Sep 2026
R527 | NUMBER p28 | - | Provision % Stage 3, 30 Sep 2026
R528 | NUMBER p28 | - | Provision % total, 30 Sep 2026
R529 | NUMBER p28 | - | Gross loans Stage 1, 30 Jun 2026
R530 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R531 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R532 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R533 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R534 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R535 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R536 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | 30 Jun 2026 table cell (scrambled)
R537 | NUMBER p28 | - | Provision % Stage 2, 30 Jun 2026
R538 | NUMBER p28 | - | Provision % Stage 3, 30 Jun 2026
R539 | NUMBER p28 | - | Provision % total, 30 Jun 2026
R540 | NUMBER p28 | - | Net loans Stage 1, 30 Jun 2026
R541 | NUMBER p28 | - | Provision % Stage 1, 30 Jun 2026
R542 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell (scrambled)
R543 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell (scrambled)
R544 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell (scrambled)
R545 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell (scrambled)
R546 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell (scrambled)
R547 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell (scrambled)
R548 | NUMBER p28 | - | Gross loans Stage 1, 30 Sep 2025
R549 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell, 30 Sep 2025 (scrambled)
R550 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell, 30 Sep 2025 (scrambled)
R551 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell, 30 Sep 2025 (scrambled)
R552 | NUMBER p28 | - | ECL Stage 1, 30 Sep 2025
R553 | NUMBER p28 | - | Provision % Stage 2, 30 Sep 2025
R554 | NUMBER p28 | - | Provision % Stage 3, 30 Sep 2025
R555 | NUMBER p28 | - | Provision % total, 30 Sep 2025
R556 | NUMBER p28 | - | Net loans Stage 1, 30 Sep 2025
R557 | NUMBER p28 | SCRAMBLED_ATTRIBUTION | table cell, 30 Sep 2025 (scrambled)
R558 | NUMBER p28 | - | Provision % Stage 1, 30 Sep 2025
R559 | NUMBER p28 | - | PCR as of 30 Sep 2026
R564 | NUMBER p29 | - | branch infrastructure for field collections
R565 | NUMBER p31 | - | paperless loan origination
R566 | NUMBER p31 | - | inhouse underwriting
R567 | NUMBER p31 | - | underwriting with AI/ML scores
R568 | NUMBER p31 | - | underwriting with Cluster Methodology
R569 | NUMBER p31 | - | cashless disbursements
R570 | NUMBER p31 | - | customers activated on NACH
R571 | NUMBER p31 | - | collection through digital modes
R572 | NUMBER p31 | - | inhouse field collections
R574 | NUMBER p32 | - | dedicated staff in Primary ML Channel (FY24 to FY26)
R575 | NUMBER p32 | - | branches in Primary ML Channel
R576 | NUMBER p32 | - | Branch BAU branches (centralised underwriting)
R577 | NUMBER p32 | - | ML Disbursement Rs Cr (chart order)
R578 | NUMBER p32 | - | ML Disbursement Rs Cr (chart order)
R579 | NUMBER p32 | - | ML Disbursement Rs Cr (chart order)
R580 | NUMBER p32 | - | Branch coverage Primary Channel Q2FY26
R581 | NUMBER p32 | - | Branch coverage Primary Channel Q1FY27
R582 | NUMBER p32 | - | Branch coverage Primary Channel Q2FY27
R583 | NUMBER p32 | - | upsell staff deployed
R584 | NUMBER p32 | - | branches with upsell team
R590 | NUMBER p33 | - | tele-caller productivity per month H1FY27
R591 | NUMBER p33 | - | Repeat % in HL AUM Q2FY26
R592 | NUMBER p33 | - | Repeat % in HL AUM Q1FY27
R593 | NUMBER p33 | - | Repeat % in HL AUM Q2FY27
R594 | NUMBER p33 | - | Avg foreclosure rate H1FY27 annualized
R596 | NUMBER p34 | - | branches vintage 0-3 years
R597 | NUMBER p34 | - | branches vintage 4-6 years
R598 | NUMBER p34 | - | branches vintage 7-9 years
R599 | NUMBER p34 | - | branches vintage 10 years or greater
R600 | NUMBER p34 | - | avg AUM Rs Cr by vintage (layout attribution)
R601 | NUMBER p34 | - | avg AUM Rs Cr by vintage
R602 | NUMBER p34 | - | avg AUM Rs Cr by vintage
R603 | NUMBER p34 | - | potential capacity value (layout)
R604 | NUMBER p34 | - | assumed avg AUM Rs Cr at capacity
R605 | NUMBER p34 | - | potential capacity value (layout)
R606 | NUMBER p34 | - | potential capacity value (layout)
R607 | NUMBER p34 | - | potential incremental AUM Rs crore from existing branches over medium 
R608 | NUMBER p34 | - | 3-year AUM CAGR of 33 branches with 10+ year vintage
R609 | NUMBER p34 | - | AUM growth contribution (chart order)
R610 | NUMBER p34 | - | AUM growth contribution (chart order)
R611 | NUMBER p34 | - | AUM growth contribution (chart order)
R612 | NUMBER p34 | - | AUM growth contribution (chart order)
R613 | NUMBER p34 | - | contribution to AUM growth (chart)
R614 | NUMBER p34 | - | contribution to AUM growth (chart)
R615 | NUMBER p34 | - | contribution to AUM growth (chart)
R616 | NUMBER p34 | - | contribution to AUM growth (chart)
R617 | NUMBER p34 | - | contribution to AUM growth (chart)
R618 | NUMBER p34 | - | contribution to AUM growth (chart)
R619 | NUMBER p34 | - | contribution to AUM growth (chart)
R620 | NUMBER p34 | - | contribution to AUM growth (chart)
R621 | NUMBER p34 | - | contribution to AUM growth (chart)
R622 | NUMBER p34 | - | contribution to AUM growth (chart)
R623 | NUMBER p34 | - | contribution to AUM growth (chart)
R624 | NUMBER p34 | - | contribution to AUM growth (chart)
R627 | NUMBER p34 | ZERO_STANDING | new branches opened in H1FY27 ZERO_STANDING
R642 | NUMBER p35 | - | AUM growth Q2FY27
R643 | NUMBER p35 | - | AUM growth H1FY27
R644 | NUMBER p35 | - | NIM Q2FY27
R645 | NUMBER p35 | - | NIM H1FY27
R646 | NUMBER p35 | - | Opex cost Q2FY27
R647 | NUMBER p35 | - | Opex cost H1FY27
R648 | NUMBER p35 | - | Credit cost Q2FY27
R649 | NUMBER p35 | - | Credit cost H1FY27
R650 | NUMBER p35 | - | Return on Total Assets Q2FY27
R651 | NUMBER p35 | - | Return on Total Assets H1FY27
R652 | NUMBER p35 | - | FY27 AUM growth guidance
R653 | NUMBER p35 | - | FY27 NIM guidance
R654 | NUMBER p35 | - | FY27 Opex guidance
R655 | NUMBER p35 | - | FY27 credit cost guidance
R656 | NUMBER p35 | - | FY27 Return on Total Assets guidance
R664 | NUMBER p36 | - | normalized credit cost target
R665 | NUMBER p36 | - | RoA target
R666 | NUMBER p36 | - | RoE target
R667 | NUMBER p36 | - | AUM CAGR target
R668 | NUMBER p36 | - | Opex target
R670 | NUMBER p38 | - | Interest Income Q2FY27 Rs Cr
R671 | NUMBER p38 | - | Interest Income Q2FY26
R672 | NUMBER p38 | - | Interest Income YoY Q2
R673 | NUMBER p38 | - | Interest Income Q1FY27
R674 | NUMBER p38 | - | Interest Income QoQ
R675 | NUMBER p38 | - | Interest Income H1FY27
R676 | NUMBER p38 | - | Interest Income H1FY26
R677 | NUMBER p38 | - | Interest Income YoY H1
R678 | NUMBER p38 | - | Fee & Other Income Q2FY27
R679 | NUMBER p38 | - | Fee & Other Income Q2FY26 as printed
R680 | NUMBER p38 | - | Y-o-Y column as printed on Fee & Other Income row
R681 | NUMBER p38 | - | Fee & Other Income Q1FY27
R682 | NUMBER p38 | - | Q-o-Q column as printed on Fee & Other Income row
R683 | NUMBER p38 | - | Fee & Other Income H1FY27
R684 | NUMBER p38 | - | Fee & Other Income H1FY26 as printed
R685 | NUMBER p38 | - | Y-o-Y H1 column as printed on Fee & Other Income row
R686 | NUMBER p38 | - | Total Income Q2FY27
R687 | NUMBER p38 | - | Total Income Q2FY26
R688 | NUMBER p38 | - | Y-o-Y column as printed on Total Income row
R689 | NUMBER p38 | - | Total Income Q1FY27
R690 | NUMBER p38 | - | Q-o-Q column as printed on Total Income row
R691 | NUMBER p38 | - | Total Income H1FY27
R692 | NUMBER p38 | - | Total Income H1FY26
R693 | NUMBER p38 | - | Y-o-Y H1 column as printed on Total Income row
R694 | NUMBER p38 | - | Finance Cost Q2FY27
R695 | NUMBER p38 | - | Finance Cost Q2FY26
R696 | NUMBER p38 | - | Finance Cost Q1FY27
R697 | NUMBER p38 | - | Finance Cost H1FY27
R698 | NUMBER p38 | - | Finance Cost H1FY26
R699 | NUMBER p38 | - | Operating Expense Q2FY27
R700 | NUMBER p38 | - | Operating Expense Q2FY26
R701 | NUMBER p38 | - | Operating Expense Q1FY27
R702 | NUMBER p38 | - | Operating Expense H1FY27
R703 | NUMBER p38 | - | Operating Expense H1FY26
R704 | NUMBER p38 | - | PPoP Q2FY27
R705 | NUMBER p38 | - | PPoP Q2FY26
R706 | NUMBER p38 | - | PPoP Q1FY27
R707 | NUMBER p38 | - | PPoP H1FY27
R708 | NUMBER p38 | - | PPoP H1FY26
R709 | NUMBER p38 | - | Credit Cost Q2FY27
R710 | NUMBER p38 | - | Credit Cost Q2FY26
R711 | NUMBER p38 | - | Credit Cost Q1FY27
R712 | NUMBER p38 | - | Credit Cost H1FY27
R713 | NUMBER p38 | - | Credit Cost H1FY26
R714 | NUMBER p38 | - | Tax Q2FY27
R715 | NUMBER p38 | - | Tax Q2FY26
R716 | NUMBER p38 | - | Tax Q1FY27
R717 | NUMBER p38 | - | Tax H1FY27
R718 | NUMBER p38 | - | Tax H1FY26
R719 | NUMBER p38 | - | Profit after Tax Q2FY27
R720 | NUMBER p38 | - | Profit after Tax Q2FY26
R721 | NUMBER p38 | - | Profit after Tax Q1FY27
R722 | NUMBER p38 | - | Profit after Tax H1FY27
R723 | NUMBER p38 | - | Profit after Tax H1FY26
R724 | NUMBER p38 | - | Basic EPS Q2FY27 Rs
R725 | NUMBER p38 | - | Basic EPS Q2FY26
R726 | NUMBER p38 | - | Basic EPS Q1FY27
R727 | NUMBER p38 | - | Basic EPS H1FY27
R728 | NUMBER p38 | - | Basic EPS H1FY26
R729 | NUMBER p38 | - | Diluted EPS Q2FY27
R730 | NUMBER p38 | - | Diluted EPS Q2FY26
R731 | NUMBER p38 | - | Diluted EPS Q1FY27
R732 | NUMBER p38 | - | Diluted EPS H1FY27
R733 | NUMBER p38 | - | Diluted EPS H1FY26
R740 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R741 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R742 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled, Loans candidate)
R743 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R744 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R745 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R746 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R747 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R748 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R749 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R750 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R751 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R752 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R753 | NUMBER p39 | - | Total Assets 30 Sep 2026
R754 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R755 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R756 | NUMBER p39 | - | Total Assets 31 Mar 2026
R757 | NUMBER p39 | - | Total Assets 30 Sep 2025
R758 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled, Borrowings candidate)
R759 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R760 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R761 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R762 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R763 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R764 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R765 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R766 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R767 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R768 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R769 | NUMBER p39 | SCRAMBLED_ATTRIBUTION | balance sheet value (scrambled)
R770 | NUMBER p39 | - | Total Equity 30 Sep 2026
R771 | NUMBER p39 | - | Total Equity 31 Mar 2026
R772 | NUMBER p39 | - | Total Equity 30 Sep 2025
R773 | NUMBER p39 | - | Total Liabilities 30 Sep 2026
R774 | NUMBER p39 | - | Total Liabilities 31 Mar 2026
R775 | NUMBER p39 | - | Total Liabilities 30 Sep 2025
R779 | NUMBER p40 | - | Interest Income on ATA Q1FY27 (as printed)
R780 | NUMBER p40 | - | Interest Income on ATA Q2FY27
R781 | NUMBER p40 | - | Interest Income on ATA Q2FY26
R782 | NUMBER p40 | - | bps column (as printed)
R783 | NUMBER p40 | - | H1FY27 ratio (as printed)
R784 | NUMBER p40 | - | H1FY26 ratio (as printed)
R785 | NUMBER p40 | - | H1 YoY bps
R786 | NUMBER p40 | - | bps column
R787 | NUMBER p40 | - | ratio (as printed)
R788 | NUMBER p40 | - | bps column
R789 | NUMBER p40 | - | ratio (as printed)
R790 | NUMBER p40 | - | ratio (as printed)
R791 | NUMBER p40 | - | bps column
R792 | NUMBER p40 | - | ratio (as printed)
R793 | NUMBER p40 | - | bps column
R794 | NUMBER p40 | - | NIM H1FY27 (as printed)
R795 | NUMBER p40 | - | NIM H1FY26 (as printed)
R796 | NUMBER p40 | - | bps column
R797 | NUMBER p40 | - | Finance Cost on ATA Q2FY27
R798 | NUMBER p40 | - | Finance Cost on ATA Q2FY26
R799 | NUMBER p40 | - | Finance Cost on ATA YoY
R800 | NUMBER p40 | - | ratio (as printed)
R801 | NUMBER p40 | - | bps column
R802 | NUMBER p40 | - | ratio (as printed)
R803 | NUMBER p40 | - | ratio (as printed)
R804 | NUMBER p40 | - | bps column
R805 | NUMBER p40 | - | ratio (as printed)
R806 | NUMBER p40 | - | bps column
R807 | NUMBER p40 | - | Opex ratio H1FY27 (as printed)
R808 | NUMBER p40 | - | ratio H1FY26 (as printed)
R809 | NUMBER p40 | - | bps column as printed
R810 | NUMBER p40 | - | Net Interest Margin on ATA Q2FY27
R811 | NUMBER p40 | - | Net Interest Margin on ATA Q2FY26
R812 | NUMBER p40 | - | Net Interest Margin on ATA YoY
R813 | NUMBER p40 | - | ratio (as printed)
R814 | NUMBER p40 | - | bps column
R815 | NUMBER p40 | - | ratio H1FY27 (as printed)
R816 | NUMBER p40 | - | ratio H1FY26 (as printed)
R817 | NUMBER p40 | - | bps column
R818 | NUMBER p40 | - | ratio (as printed)
R819 | NUMBER p40 | - | bps column
R820 | NUMBER p40 | - | ratio H1FY27 (as printed)
R821 | NUMBER p40 | - | ratio H1FY26 (as printed)
R822 | NUMBER p40 | - | bps column
R823 | NUMBER p40 | - | Fee & Other Income on ATA Q2FY27
R824 | NUMBER p40 | - | ratio (as printed)
R825 | NUMBER p40 | - | bps column
R826 | NUMBER p40 | - | ratio (as printed)
R827 | NUMBER p40 | - | bps column
R828 | NUMBER p40 | - | ratio (as printed)
R829 | NUMBER p40 | - | ratio (as printed)
R830 | NUMBER p40 | - | bps column
R831 | NUMBER p40 | ZERO_STANDING | dash cells (ZERO_STANDING)
R832 | NUMBER p40 | - | Operating Expense on ATA Q2FY27
R833 | NUMBER p40 | - | Operating Expense on ATA Q2FY26
R834 | NUMBER p40 | - | Operating Expense on ATA YoY
R835 | NUMBER p40 | - | ratio as printed (unit unclear)
R836 | NUMBER p40 | - | bps column
R837 | NUMBER p40 | - | ratio as printed
R838 | NUMBER p40 | - | ratio as printed
R839 | NUMBER p40 | - | bps column
R840 | NUMBER p40 | - | ratio (as printed)
R841 | NUMBER p40 | - | ratio (as printed; RoE H1FY27 per page 6)
R842 | NUMBER p40 | - | ratio (as printed)
R843 | NUMBER p40 | - | Credit Cost on ATA Q2FY27
R844 | NUMBER p40 | - | Credit Cost on ATA Q2FY26
R845 | NUMBER p40 | - | Credit Cost on ATA YoY
R846 | NUMBER p40 | - | Profit after Tax on ATA Q2FY27
R847 | NUMBER p40 | - | Profit after Tax on ATA Q2FY26
R848 | NUMBER p40 | - | Profit after Tax on ATA YoY
R849 | NUMBER p40 | - | RoA (on AUM) Q2FY27
R850 | NUMBER p40 | - | RoA (on AUM) Q2FY26
R851 | NUMBER p40 | - | RoA (on AUM) YoY
R852 | NUMBER p40 | - | Leverage (x) Q2FY27
R853 | NUMBER p40 | - | Leverage (x) Q2FY26
R854 | NUMBER p40 | - | Return on Equity Q2FY27
R855 | NUMBER p40 | - | Return on Equity Q2FY26
R856 | NUMBER p40 | - | Return on Equity YoY
R857 | NUMBER p40 | - | Closing D/E
R861 | NUMBER p41 | - | shareholding category share (chart)
R862 | NUMBER p41 | - | shareholding category share
R863 | NUMBER p41 | - | shareholding category share
R864 | NUMBER p41 | - | shareholding category share
R865 | NUMBER p41 | - | shareholding category share
R866 | NUMBER p41 | - | shareholding category share
R867 | NUMBER p41 | - | holder percentage (layout)
R868 | NUMBER p41 | - | holder percentage (layout)
R869 | NUMBER p41 | - | holder percentage (layout)
R870 | NUMBER p41 | - | holder percentage (layout)
R871 | NUMBER p41 | - | holder percentage (layout)
R872 | NUMBER p41 | - | holder percentage (layout)
R879 | NUMBER p42 | - | grassroots micro-entrepreneurs
R880 | NUMBER p42 | - | livelihood programs
R881 | NUMBER p42 | - | increase in profit and customer acquisition
R882 | NUMBER p42 | - | women artisans earning regular income
R883 | NUMBER p42 | - | Women earn 40% higher wages
R884 | NUMBER p42 | - | enterprises established run by women
R885 | NUMBER p42 | - | additional donation from HUL
R886 | NUMBER p42 | - | overall donation from HUL exceeded
R888 | NUMBER p42 | - | Clusters
R889 | NUMBER p42 | - | States
R890 | NUMBER p42 | - | Districts
R891 | NUMBER p42 | - | Villages
R892 | NUMBER p42 | - | income generated by FAME women-focused programs
R893 | NUMBER p42 | - | cumulative impact
R894 | NUMBER p42 | - | Lives Touched
R895 | NUMBER p42 | - | Women Trained
R896 | NUMBER p42 | - | Livestock Treated
R897 | NUMBER p42 | - | Training Man-Hours
R898 | NUMBER p42 | - | milk collection centres
R899 | NUMBER p42 | - | dairy farmers
R900 | NUMBER p42 | - | milk deposited in the quarter
R901 | NUMBER p42 | - | Dairy aggregation shops
R902 | NUMBER p42 | - | dairy inputs sold at wholesale prices

## 3. FOOTNOTES, QUALIFIERS, FINE PRINT
ROW_ID | category | A2 flags | cross-ref / note
R013 | QUALIFIER p1 | - | presentation covers unaudited results
R014 | QUALIFIER p1 | - | enclosure note
R023 | QUALIFIER p6 | - | management context
R027 | QUALIFIER p6 | - | calibrated lending qualifier
R037 | QUALIFIER p6 | - | opex ratio qualifier
R056 | QUALIFIER p6 | - | PAT claim qualifier
R096 | QUALIFIER p7 | - | reclassification and rounding note
R123 | QUALIFIER p8 | - | marker # footnote
R124 | QUALIFIER p8 | - | asterisk footnote for RoE
R127 | QUALIFIER p8 | - | marker pairing
R146 | QUALIFIER p9 | - | reclassification and rounding note
R147 | QUALIFIER p10 | - | footnote marker
R164 | QUALIFIER p10 | - | asterisk footnote for RoE
R180 | QUALIFIER p12 | - | data date qualifier
R263 | QUALIFIER p14 | - | data date
R264 | QUALIFIER p14 | - | map note
R266 | QUALIFIER p14 | SCRAMBLED_ATTRIBUTION | extraction caveat
R275 | QUALIFIER p15 | - | tally marks note
R276 | QUALIFIER p15 | - | segment definitions
R293 | QUALIFIER p17 | - | collateral by product
R294 | QUALIFIER p17 | - | loan nature note
R295 | QUALIFIER p17 | - | data date
R328 | QUALIFIER p19 | SCRAMBLED_ATTRIBUTION | extraction caveat
R332 | QUALIFIER p21 | - | Financial Institutions asterisk
R358 | QUALIFIER p21 | SCRAMBLED_ATTRIBUTION | rating qualifier
R359 | QUALIFIER p21 | SCRAMBLED_ATTRIBUTION | extraction caveat
R379 | QUALIFIER p22 | - | ALM statement
R433 | QUALIFIER p26 | - | portfolio vintage claim
R434 | QUALIFIER p26 | SCRAMBLED_ATTRIBUTION | extraction caveat
R436 | QUALIFIER p27 | - | metric definition
R509 | QUALIFIER p27 | SCRAMBLED_ATTRIBUTION | extraction caveat
R560 | QUALIFIER p28 | - | double asterisk on net loans total 6,845
R561 | QUALIFIER p28 | SCRAMBLED_ATTRIBUTION | extraction caveat
R587 | QUALIFIER p32 | - | mortgage claim
R588 | QUALIFIER p32 | SCRAMBLED_ATTRIBUTION | extraction caveat
R628 | QUALIFIER p34 | - | branch opening statement
R629 | QUALIFIER p34 | - | asterisk footnote on Potential Capacity
R630 | QUALIFIER p34 | - | marker pairing
R634 | QUALIFIER p34 | - | company claim
R635 | QUALIFIER p34 | SCRAMBLED_ATTRIBUTION | extraction caveat
R657 | QUALIFIER p35 | - | asterisk footnote
R734 | QUALIFIER p38 | - | reclassification note
R735 | QUALIFIER p38 | - | rounding note
R736 | QUALIFIER p38 | - | layout anomaly flag
R776 | QUALIFIER p39 | - | reclassification note
R777 | QUALIFIER p39 | - | rounding note
R778 | QUALIFIER p39 | SCRAMBLED_ATTRIBUTION | extraction caveat
R859 | QUALIFIER p40 | - | reclassification and rounding note
R860 | QUALIFIER p40 | SCRAMBLED_ATTRIBUTION | extraction caveat
R876 | QUALIFIER p41 | SCRAMBLED_ATTRIBUTION | extraction caveat
R905 | QUALIFIER p43 | - | metric definition
R906 | QUALIFIER p43 | - | metric definition
R907 | QUALIFIER p43 | - | metric definition
R908 | QUALIFIER p43 | - | metric definition
R909 | QUALIFIER p43 | - | metric definition
R910 | QUALIFIER p43 | - | metric definition

## 4. FORWARD-LOOKING STATEMENTS
ROW_ID | category | A2 flags | cross-ref / note
R018 | FORWARD p3 | - | safe harbor FLS clause
R019 | FORWARD p3 | - | safe harbor no-update clause
R045 | FORWARD p6 | - | credit cost guided range
R068 | FORWARD p6 | - | H2 FY27 intent
R069 | FORWARD p6 | - | FY27 guidance commitment
R070 | FORWARD p6 | - | outlook statement
R210 | FORWARD p13 | - | IPO milestone
R380 | FORWARD p22 | - | forward statement
R585 | FORWARD p32 | - | OER improvement claim
R586 | FORWARD p32 | - | upsell program
R595 | FORWARD p33 | - | upsell opportunity
R631 | FORWARD p34 | - | potential capacity claim
R632 | FORWARD p34 | - | growth headroom claim
R633 | FORWARD p34 | - | growth claim
R637 | FORWARD p35 | - | FY27 guidance
R638 | FORWARD p35 | - | FY27 guidance
R639 | FORWARD p35 | - | FY27 guidance
R640 | FORWARD p35 | - | FY27 guidance
R641 | FORWARD p35 | - | FY27 guidance
R658 | FORWARD p36 | - | vision header
R659 | FORWARD p36 | - | 3-year vision
R660 | FORWARD p36 | - | 3-year vision
R661 | FORWARD p36 | - | 3-year vision
R662 | FORWARD p36 | - | 3-year vision
R663 | FORWARD p36 | - | strategic focus

## 5. DATES
ROW_ID | category | A2 flags | cross-ref / note
R009 | DATE p1 | - | letter date
R010 | DATE p1 | - | period of results
R011 | DATE p1 | - | digital signature timestamp
R016 | DATE p2 | - | presentation title period
R022 | DATE p6 | - | commentary period
R067 | DATE p6 | - | period
R071 | DATE p7 | - | slide period
R126 | DATE p8 | - | equity infusion date
R168 | DATE p12 | - | founding year
R181 | DATE p13 | - | journey timeline years
R182 | DATE p13 | - | certificate of registration year
R265 | DATE p14 | - | industry mix chart dates
R296 | DATE p17 | - | AUM split date
R344 | DATE p21 | - | CoB chart periods
R357 | DATE p21 | - | rating upgrade date
R377 | DATE p22 | - | chart dates
R378 | DATE p22 | - | ALM buckets
R430 | DATE p26 | - | monthly chart periods
R432 | DATE p26 | - | volatile over-lending period cutoff
R510 | DATE p28 | - | provisions table date
R511 | DATE p28 | - | provisions table date
R512 | DATE p28 | - | provisions table date
R589 | DATE p32 | - | ML chart periods
R625 | DATE p34 | - | chart periods
R626 | DATE p34 | - | contribution window
R636 | DATE p35 | - | guidance table columns
R669 | DATE p36 | - | vision horizon
R737 | DATE p38 | - | P&L column periods
R739 | DATE p39 | - | balance sheet dates
R858 | DATE p40 | - | ROE tree periods
R875 | DATE p41 | - | shareholding date
R887 | DATE p42 | - | HUL donation period
R903 | DATE p42 | - | CSR update period

## 6. ENTITIES (ENTITY_CHANGE not assessable, no prior list)
ROW_ID | category | A2 flags | cross-ref / note
R001 | ENTITY p1 | - | registrant
R002 | ENTITY p1 | - | company CIN
R003 | ENTITY p1 | - | exchanges addressed
R004 | ENTITY p1 | - | listing identifiers
R005 | ENTITY p1 | - | regulation cited
R006 | ENTITY p1 | - | regulator
R007 | ENTITY p1 | - | signatory
R008 | ENTITY p1 | - | company website
R015 | ENTITY-SUMMARY p1 | - | address block
R017 | ENTITY-SUMMARY p3 | - | safe harbor boilerplate
R020 | ENTITY-SUMMARY p4 | - | index
R021 | ENTITY p6 | - | commentary speaker
R028 | ENTITY p6 | - | drought-affected regions
R165 | ENTITY p12 | - | business descriptor
R166 | ENTITY p12 | - | regulator
R167 | ENTITY p12 | - | investor backers
R211 | ENTITY p13 | - | key investors
R262 | ENTITY p14 | - | chart legend
R267 | ENTITY p15 | - | segment taxonomy
R268 | ENTITY p15 | - | competitor classes
R281 | ENTITY-SUMMARY p16 | - | cluster roster
R292 | ENTITY p17 | - | product names
R297 | ENTITY p18 | - | director
R298 | ENTITY p18 | - | director
R299 | ENTITY p18 | - | director
R300 | ENTITY p18 | - | director
R301 | ENTITY p18 | - | director
R302 | ENTITY p18 | - | director
R303 | ENTITY p18 | - | director
R304 | ENTITY p18 | - | prior employers
R306 | ENTITY p19 | - | management
R307 | ENTITY p19 | - | management
R308 | ENTITY p19 | - | management
R309 | ENTITY p19 | - | management
R310 | ENTITY p19 | - | management
R311 | ENTITY p19 | - | management
R312 | ENTITY p19 | - | management
R313 | ENTITY p19 | - | management
R314 | ENTITY p19 | - | management
R315 | ENTITY p19 | - | management
R316 | ENTITY p19 | - | management
R354 | ENTITY p21 | - | borrowing instrument types
R435 | ENTITY p27 | - | key states
R562 | ENTITY p29 | - | collection structure
R563 | ENTITY p29 | - | models and systems
R573 | ENTITY-SUMMARY p31 | - | technology stack roster
R738 | ENTITY p39 | - | balance sheet captions
R873 | ENTITY p41 | - | shareholders
R874 | ENTITY p41 | - | categories
R877 | ENTITY p42 | - | CSR entity
R878 | ENTITY p42 | - | CSR partners
R904 | ENTITY-SUMMARY p43 | - | glossary
R911 | ENTITY p44 | - | contacts
R912 | ENTITY p44 | - | IR advisor
R913 | ENTITY-SUMMARY p44 | - | contact block

## 7. ZERO_STANDING INDEX
R188, R189, R190, R627, R831

## 8. MISSING_FROM_STRUCTURED
M01 | line 667 | page 28 | NUMBER | values 83 | 308 | 6,865 = 30-Jun-2026 gross loans Stage 2, Stage 3, Total (Summary of Provisions table; Sept-2026 column is 6,730 / 90 / 299 / 7,119) | MISSING_FROM_STRUCTURED, SCRAMBLED_ATTRIBUTION
M02 | line 807 | page 34 | NUMBER | value 0 = potential capacity for the 10+ year branch vintage (axis/label base of vintage capacity chart; companion values 560, 1,547, 2,301) | MISSING_FROM_STRUCTURED

## 8b. A1 LABEL CORRECTION (logged, A1 file not edited)
R076 | A1 label "Disbursements Q2FY26" value 1,219 | correct period is Q1FY27 (fulltext line 150, p7 shows 1,219 beside +10% QoQ marker) | per A3 presentation forensics
R077 | A1 label "Disbursements Q1FY27" value 1,275 | correct period is Q2FY26 | per A3 presentation forensics
Labels R076/R077 are swapped. Downstream must read R076 as Q1FY27 and R077 as Q2FY26.

## 9. RESTATED cross-refs (spot, same-metric repeats; not exhaustive)
Executive summary p6 numbers (R024-R053) restate p8 Key Highlights; A3 to pair by metric.
