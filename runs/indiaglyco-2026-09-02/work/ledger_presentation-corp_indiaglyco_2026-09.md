=== A2 COUNT TEST ===
category: slides         grep_count: 32   sweep_count: 32   match: yes
category: slide_numbers  grep_count: 146  sweep_count: 146  match: yes
category: entities       grep_count: 73   sweep_count: 73   match: yes
category: forward        grep_count: 26   sweep_count: 26   match: yes
category: dates          grep_count: 27   sweep_count: 27   match: yes
category: footnotes      grep_count: 19   sweep_count: 19   match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 291 | ids_referenced_in_ledger: 291 | orphan_ids: [] | match: yes

# NOTE ON GREP METHOD: grep_count for `slides` is grep -c '^\[page ' on A1 fulltext
# (page_count_pdfinfo: 32, page_coverage: 100%, fulltext used ONLY to confirm total slide
# count since the structured file's materiality rule groups/omits 5 section-divider slides
# with zero data rows: pages 4, 9, 13, 15, 30). grep_count for numbers/entities/forward/dates/
# footnotes is `grep -c '| TYPE |'` on the structured file; sweep_count is independent manual
# tally of R### IDs per TYPE section header. All match.

=== LEDGER: India Glycols Limited (INDIAGLYCO) | 2026-09 | presentation ===

## 1. SLIDE ENUMERATION (32 slides; item 1 + item 3 DROPPED_SLIDE check)

prior_quarter_deck: none provided -> DROPPED_SLIDE check NOT APPLICABLE this run (no baseline to diff)

slide | title | content_type | R-IDs on slide | A2 flags / note
---|---|---|---|---
1 | Regulatory filing letter (IGL/SE/2026-27/53) | text | R001,R002,R147,R148,R149,R150,R151,R152,R153,R246,R247,R248,R273 | 
2 | Four decades of sustainable chemistry (cover) | text/photo (end-market icon roster) | R154 | 
3 | Content (table of contents) | text | R155 | 
4 | Introduction (section divider) | text (divider, no data) | none | section divider, no A1 rows
5 | IGL Journey (four-decade timeline) | chart (timeline) | R003,R004,R005,R006,R156-R163,R249-R266 | 
6 | India Glycols Limited (capability/positioning) | text | R007-R013,R164,R220,R267,R274,R275 | 
7 | Key Financials | table | R014-R048,R221,R276 | BASIS_DIFFERENCE flag on EBITDA rows (see footnotes table R291 note)
8 | Advanced Multi-capability Manufacturing Platform | text | R049-R051,R165-R170 | 
9 | Structure of the Demerger (section divider) | text (divider, no data) | none | section divider, no A1 rows
10 | Overview of the Demerger | text | R171,R222-R229,R268,R269 | DATE_SEQUENCE_NOTE on R268/R229/R269
11 | Introduction to the Demerged Businesses | text/photo (brand taglines) | R172,R173 | 
12 | Demerged Structure (revenue split) | table | R052-R062,R174-R176,R230-R233,R277 | 
13 | India Glycols (Post Demerger) (section divider) | text (divider, no data) | none | section divider, no A1 rows
14 | India Glycols Limited - FY26 (segment revenue) | chart/table | R063-R069,R177 | 
15 | Industry (section divider) | text (divider, no data) | none | section divider, no A1 rows
16 | Sustainable Chemicals Entering a Structural Adoption Cycle | chart | R070-R081,R278,R279 | 
17 | India's Specialty Chemicals - Well Positioned | chart | R082-R098,R280,R281 | 
18 | Vision: 10X 10Y | chart/diagram (roadmap) | R099-R101,R234-R238,R270,R282 | 
19 | Pioneering & Scaling up Sustainable Chemistry | text | R102-R104,R178-R181,R283 | 
20 | Driving Growth with Positive Impact (6 pillars) | text | R239-R244 | 
21 | What we bring to the table: six foundations, forty years deep | text | R105-R108,R182-R188,R245,R271 | 
22 | Chemistry platforms - how we build | diagram | R109-R111,R189-R192 | 
23 | Application platforms - what our molecules do | diagram | R112,R113,R193-R195 | 
24 | One of India's Only Chemicals Plant with a Direct Rail Line to Port | chart/map (logistics) | R114-R117,R196-R199 | 
25 | Bio-Glycols \| Renewable Alternatives Serving Large Value Chains | table/chart | R118-R121,R200-R202,R284 | 
26 | Bio-Glycol Ethers \| Bio-based Solvents Serving Diversified Industrial Applications | table/chart | R122-R125,R203-R205,R285,R286 | 
27 | Performance Chemicals \| Application-led Chemistries For Specialty Needs | table/chart | R126-R129,R206-R210,R287,R288 | 
28 | Industrial Gases \| High-purity Solutions for Essential End-markets | table/chart | R130-R132,R211-R215 | 
29 | Clariant IGL Joint Venture \| Renewable Performance Chemicals Platform | table/chart | R133-R136,R216,R217,R272,R289,R290 | 
30 | Financial Highlights (section divider) | text (divider, no data) | none | section divider, no A1 rows
31 | Key Historical Financials | table | R137-R145,R291 | BASIS_DIFFERENCE flag on Adj.EBITDA rows
32 | Thank You (contact page) | text | R146,R218,R219 | 

## 2. NUMBERS ON SLIDES (item 2; 146 rows, references A1 NUMBER table R001-R146)

ROW_ID | category | A2 flags | cross-ref / materiality note
---|---|---|---
R001 | numbers |  | 
R002 | numbers |  | 
R003 | numbers |  | 
R004 | numbers |  | 
R005 | numbers |  | 
R006 | numbers |  | 
R007 | numbers |  | 
R008 | numbers |  | 
R009 | numbers |  | 
R010 | numbers |  | 
R011 | numbers |  | 
R012 | numbers |  | 
R013 | numbers |  | 
R014 | numbers |  | duplicate statement of same fact at line 240 (~13% CAGR), single fact not RESTATED
R015 | numbers |  | duplicate statement of same fact at line 240 (~28% CAGR), single fact not RESTATED
R016 | numbers |  | 
R017 | numbers |  | 
R018 | numbers |  | 
R019 | numbers |  | 
R020 | numbers |  | 
R021 | numbers |  | 
R022 | numbers |  | 
R023 | numbers |  | 
R024 | numbers |  | 
R025 | numbers |  | 
R026 | numbers |  | 
R027 | numbers |  | 
R028 | numbers |  | 
R029 | numbers |  | 
R030 | numbers |  | 
R031 | numbers |  | 
R032 | numbers | BASIS_DIFFERENCE | India Glycols segment EBITDA FY24: page7 unadjusted 139 Cr (R032) vs page31 Adj.EBITDA 247 Cr (R140), cross-ref both bases
R033 | numbers |  | 
R034 | numbers |  | 
R035 | numbers | BASIS_DIFFERENCE | India Glycols segment EBITDA FY25: page7 unadjusted 130 Cr (R035) vs page31 Adj.EBITDA 312 Cr (R141), cross-ref both bases
R036 | numbers |  | 
R037 | numbers |  | 
R038 | numbers | BASIS_DIFFERENCE | India Glycols segment EBITDA FY26: page7 unadjusted 169 Cr (R038) vs page31 Adj.EBITDA 330 Cr (R142), cross-ref both bases; largest divergence
R039 | numbers |  | 
R040 | numbers |  | 
R041 | numbers |  | 
R042 | numbers |  | 
R043 | numbers | BASIS_DIFFERENCE | India Glycols EBITDA margin FY24: page7 8.8% (R043) vs page31 Adj. 15.6% (R143)
R044 | numbers | BASIS_DIFFERENCE | India Glycols EBITDA margin FY25: page7 10.1% (R044) vs page31 Adj. 24.2% (R144)
R045 | numbers | BASIS_DIFFERENCE | India Glycols EBITDA margin FY26: page7 14.5% (R045) vs page31 Adj. 28.4% (R145)
R046 | numbers |  | 
R047 | numbers |  | 
R048 | numbers |  | 
R049 | numbers |  | 
R050 | numbers |  | 
R051 | numbers |  | 
R052 | numbers |  | 
R053 | numbers |  | 
R054 | numbers |  | 
R055 | numbers |  | 
R056 | numbers |  | 
R057 | numbers |  | 
R058 | numbers |  | 
R059 | numbers |  | 
R060 | numbers |  | 
R061 | numbers |  | 
R062 | numbers |  | 
R063 | numbers |  | 
R064 | numbers |  | 
R065 | numbers |  | 
R066 | numbers |  | 
R067 | numbers |  | 
R068 | numbers |  | 
R069 | numbers |  | 
R070 | numbers |  | 
R071 | numbers |  | 
R072 | numbers |  | 
R073 | numbers |  | 
R074 | numbers |  | 
R075 | numbers |  | 
R076 | numbers |  | 
R077 | numbers |  | 
R078 | numbers |  | 
R079 | numbers |  | 
R080 | numbers |  | 
R081 | numbers |  | 
R082 | numbers |  | 
R083 | numbers |  | 
R084 | numbers |  | 
R085 | numbers |  | 
R086 | numbers |  | 
R087 | numbers |  | 
R088 | numbers |  | 
R089 | numbers |  | 
R090 | numbers |  | 
R091 | numbers |  | 
R092 | numbers |  | 
R093 | numbers |  | 
R094 | numbers |  | 
R095 | numbers |  | 
R096 | numbers |  | 
R097 | numbers |  | 
R098 | numbers |  | 
R099 | numbers |  | 
R100 | numbers |  | 
R101 | numbers |  | 
R102 | numbers |  | 
R103 | numbers |  | 
R104 | numbers |  | 
R105 | numbers |  | 
R106 | numbers |  | 
R107 | numbers |  | 
R108 | numbers |  | 
R109 | numbers |  | 
R110 | numbers |  | 
R111 | numbers |  | 
R112 | numbers |  | 
R113 | numbers |  | 
R114 | numbers |  | 
R115 | numbers |  | 
R116 | numbers |  | 
R117 | numbers |  | 
R118 | numbers |  | duplicate statement of same fact at line 809, single fact not RESTATED
R119 | numbers |  | 
R120 | numbers |  | 
R121 | numbers |  | 
R122 | numbers |  | 
R123 | numbers |  | 
R124 | numbers |  | 
R125 | numbers |  | 
R126 | numbers |  | 
R127 | numbers |  | 
R128 | numbers |  | 
R129 | numbers |  | 
R130 | numbers |  | 
R131 | numbers |  | 
R132 | numbers |  | 
R133 | numbers |  | 
R134 | numbers |  | 
R135 | numbers |  | 
R136 | numbers |  | 
R137 | numbers |  | 
R138 | numbers |  | 
R139 | numbers |  | 
R140 | numbers | BASIS_DIFFERENCE | India Glycols segment EBITDA FY24: page7 unadjusted 139 Cr (R032) vs page31 Adj.EBITDA 247 Cr (R140), cross-ref both bases
R141 | numbers | BASIS_DIFFERENCE | India Glycols segment EBITDA FY25: page7 unadjusted 130 Cr (R035) vs page31 Adj.EBITDA 312 Cr (R141), cross-ref both bases
R142 | numbers | BASIS_DIFFERENCE | India Glycols segment EBITDA FY26: page7 unadjusted 169 Cr (R038) vs page31 Adj.EBITDA 330 Cr (R142), cross-ref both bases; largest divergence
R143 | numbers | BASIS_DIFFERENCE | India Glycols EBITDA margin FY24: page7 8.8% (R043) vs page31 Adj. 15.6% (R143)
R144 | numbers | BASIS_DIFFERENCE | India Glycols EBITDA margin FY25: page7 10.1% (R044) vs page31 Adj. 24.2% (R144)
R145 | numbers | BASIS_DIFFERENCE | India Glycols EBITDA margin FY26: page7 14.5% (R045) vs page31 Adj. 28.4% (R145)
R146 | numbers |  | 

## 3. ENTITIES / PRODUCTS / PARTNERS NAMED (73 rows, references A1 ENTITY table R147-R219)

ROW_ID | category | A2 flags | cross-ref / materiality note
---|---|---|---
R147 | entities |  | 
R148 | entities |  | 
R149 | entities |  | 
R150 | entities |  | 
R151 | entities |  | 
R152 | entities |  | 
R153 | entities |  | 
R154 | entities |  | 
R155 | entities |  | 
R156 | entities |  | 
R157 | entities |  | 
R158 | entities |  | 
R159 | entities |  | 
R160 | entities |  | 
R161 | entities |  | 
R162 | entities |  | 
R163 | entities |  | 
R164 | entities |  | 
R165 | entities |  | 
R166 | entities |  | 
R167 | entities |  | 
R168 | entities |  | 
R169 | entities |  | 
R170 | entities |  | 
R171 | entities |  | 
R172 | entities |  | 
R173 | entities |  | 
R174 | entities |  | 
R175 | entities |  | 
R176 | entities |  | 
R177 | entities |  | 
R178 | entities |  | 
R179 | entities |  | 
R180 | entities |  | 
R181 | entities |  | 
R182 | entities |  | 
R183 | entities |  | 
R184 | entities |  | 
R185 | entities |  | 
R186 | entities |  | 
R187 | entities |  | 
R188 | entities |  | 
R189 | entities |  | 
R190 | entities |  | 
R191 | entities |  | 
R192 | entities |  | 
R193 | entities |  | 
R194 | entities |  | 
R195 | entities |  | 
R196 | entities |  | 
R197 | entities |  | 
R198 | entities |  | 
R199 | entities |  | 
R200 | entities |  | 
R201 | entities |  | 
R202 | entities |  | 
R203 | entities |  | 
R204 | entities |  | 
R205 | entities |  | 
R206 | entities |  | 
R207 | entities |  | 
R208 | entities |  | 
R209 | entities |  | 
R210 | entities |  | 
R211 | entities |  | 
R212 | entities |  | 
R213 | entities |  | 
R214 | entities |  | 
R215 | entities |  | 
R216 | entities |  | 
R217 | entities |  | 
R218 | entities |  | 
R219 | entities |  | 

no ENTITY_CHANGE flags possible this run: prior_quarter_deck = none, no baseline entity list to diff against

## 4. FORWARD-LOOKING / STRATEGIC STATEMENTS (26 rows, references A1 FORWARD table R220-R245)

ROW_ID | category | A2 flags | cross-ref / materiality note
---|---|---|---
R220 | forward_statements |  | 
R221 | forward_statements |  | 
R222 | forward_statements |  | 
R223 | forward_statements |  | 
R224 | forward_statements |  | 
R225 | forward_statements |  | 
R226 | forward_statements |  | demerger perimeter allocation: IGL retains Bio Specialty Materials/Sustainable & Performance Chemicals/Gases; IGL Spirits gets Potable Spirits & Biofuels; Ennature gets Nutraceuticals/APIs/Biopolymers
R227 | forward_statements |  | 
R228 | forward_statements |  | 
R229 | forward_statements | DATE_SEQUENCE_NOTE | timeline commitment cross-ref R268 (effective date), R269 (conclusion date)
R230 | forward_statements |  | 
R231 | forward_statements |  | 
R232 | forward_statements |  | 
R233 | forward_statements |  | 
R234 | forward_statements |  | 
R235 | forward_statements |  | 
R236 | forward_statements |  | 
R237 | forward_statements |  | 
R238 | forward_statements |  | 
R239 | forward_statements |  | 
R240 | forward_statements |  | 
R241 | forward_statements |  | 
R242 | forward_statements |  | 
R243 | forward_statements |  | 
R244 | forward_statements |  | 
R245 | forward_statements |  | 

## 5. DATES (27 rows, references A1 DATE table R246-R272)

ROW_ID | category | A2 flags | cross-ref / materiality note
---|---|---|---
R246 | dates |  | 
R247 | dates |  | 
R248 | dates |  | 
R249 | dates |  | 
R250 | dates |  | 
R251 | dates |  | 
R252 | dates |  | 
R253 | dates |  | 
R254 | dates |  | 
R255 | dates |  | 
R256 | dates |  | 
R257 | dates |  | 
R258 | dates |  | 
R259 | dates |  | 
R260 | dates |  | 
R261 | dates |  | 
R262 | dates |  | 
R263 | dates |  | 
R264 | dates |  | 
R265 | dates |  | 
R266 | dates |  | 
R267 | dates |  | 
R268 | dates | DATE_SEQUENCE_NOTE | demerger effective date 1-Sep-2026 precedes filing/meeting date 2-Sep-2026 (R246/R248); cross-ref R269, R229 (expected conclusion 24-Oct-2026)
R269 | dates | DATE_SEQUENCE_NOTE | expected conclusion 24-Oct-2026 is after effective date 1-Sep-2026 (R268); sequence internally consistent but 'effective' precedes 'concluded' worth A3 scrutiny
R270 | dates |  | 
R271 | dates |  | 
R272 | dates |  | 

## 6. FOOTNOTES / FINE-PRINT DISCLAIMERS QUALIFYING HEADLINE NUMBERS (item 4; 19 rows, references A1 QUALIFIER table R273-R291)

ROW_ID | category | A2 flags | cross-ref / materiality note
---|---|---|---
R273 | footnotes |  | 
R274 | footnotes |  | 
R275 | footnotes |  | 
R276 | footnotes |  | 
R277 | footnotes |  | 
R278 | footnotes |  | 
R279 | footnotes |  | 
R280 | footnotes |  | 
R281 | footnotes |  | 
R282 | footnotes |  | 
R283 | footnotes |  | 
R284 | footnotes |  | 
R285 | footnotes |  | 
R286 | footnotes |  | 
R287 | footnotes |  | 
R288 | footnotes |  | 
R289 | footnotes |  | 
R290 | footnotes |  | 
R291 | footnotes | FOOTNOTE_UNRESOLVED | Adj. EBITDA add-back footnote applies to page31 only; page7 EBITDA carries no equivalent footnote though same underlying entity (see BASIS_DIFFERENCE rows R032/R035/R038/R043/R044/R045 and their R140/R141/R142/R143/R144/R145 pairs)

## 7. ZERO_STANDING SWEEP

Independent sweep of all 146 NUMBER rows for zero/nil/dash-valued standing line items: NONE FOUND.
This is a marketing/investor deck, not a financial-statement filing; it carries no standing
line-item template (e.g. no P&L schedule with contra/nil rows). zero_standing count: 0.

## 8. MISSING_FROM_STRUCTURED

None. Independent sweep of the structured file (all 291 rows) plus the fulltext page-count
check (32 pages, 100% coverage per A1 header) found no disclosure unit A1's structured file
lacks. The 5 section-divider slides (pages 4, 9, 13, 15, 30) carry title text only, already
visible in R155's table-of-contents ENTITY-SUMMARY row; not a new missing unit.
