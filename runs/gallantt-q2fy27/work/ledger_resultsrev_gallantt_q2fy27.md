# A2 LEDGER - GALLANTT Q2 FY27 resultsrev (REVISED board outcome filed 21-Oct-2026)

ids_in_structured: 744 | ids_referenced_in_ledger: 744 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (rows)                    grep_count: 15   sweep_count: 15   match: yes   (7 new standalone: R338,R339,R341,R344,R345,R347,R350; 8 carried: R658,R659,R674,R675,R679,R680,R681,R684)
category: line_items new standalone       grep_count: 94   sweep_count: 94   match: yes   (P&L 24, BS 35, CF 35)
category: line_item_cells new standalone  grep_count: 284  sweep_count: 284  match: yes   (144 + 70 + 70)
category: line_items carried distinct     grep_count: 96   sweep_count: 96   match: yes   (296 cells: P&L 156, BS 70, CF 70; matches original ledger)
category: zero_standing_cells (all)       grep_count: 46   sweep_count: 46   match: yes   (19 new, 27 carried)
category: agenda_items                    grep_count: 1    sweep_count: 1    match: yes
category: auditor_rows carried            grep_count: 52   sweep_count: 52   match: yes
category: consolidated subsidiaries       grep_count: 1    sweep_count: 1    match: yes
category: structured ids vs header 744    grep_count: 744  sweep_count: 744  match: yes   (NUMBER 605, ENTITY 45, FORWARD 1, DATE 38, QUALIFIER 55)
gate_a2: pass
=== END COUNT TEST ===

DIFF VS ORIGINAL (19-Oct) LEDGER: NEW = page 1 date/timestamp (R009, R020) and standalone pp2-6 (R027-R358). CARRIED_UNCHANGED = R359-R743 plus R744 (new correction row, p12) (original R065-R449, +294). Original pp2-6 consolidated duplicates and their 8 SUPERSEDED rows are gone (replaced by 4 new superseded rows R033, R184, R261, R322).
FILING FLAGS: (1) STANDALONE_STATEMENT_ABSENT RESOLVED: standalone statements now present pp2-5; p12 standalone review report R693-R702 now has its statements; R744 corrects R697. (2) DATE_INCONSISTENCY RESOLVED: subject line 19-Oct-2026 (R009). (3) Filing posted 21-Oct, 2 days after meeting; signature 15:51 (R020). (4) STANDALONE_CONSOL_DIFF: H1FY27 PBT 24,798.82 vs 24,798.81; FY26 PAT 48,427.31 vs 48,426.70 (A1 footing section). (5) Standalone has no associate line. (6) DIVIDEND nil in 6m cash flow (R328) vs approved Rs 2 dividend (R350,R355). (7) Source item numbering skips 13 (R034). (8) Auditor sig UDIN differs standalone vs consolidated (carried). No ENTITY_CHANGE; no MISSING_FROM_STRUCTURED.

## Page 1 cover letter, agenda, signature (REVISED; re-anchored) (26)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R001 | p1:L24 |  | 
R002 | p1:L26 |  | 
R003 | p1:L28 |  | 
R004 | p1:L28 |  | 
R005 | p1:L30 |  | 
R006 | p1:L33 |  | 
R007 | p1:L34 |  | 
R008 | p1:L34 |  | 
R009 | p1:L38 | DATE_FIXED_VS_ORIGINAL | NEW: subject line now 19-Oct-2026 (original 03-Nov-2025); DATE_INCONSISTENCY of original resolved
R010 | p1:L39 | MEETING_TIMES 04:30 PM to 11:00 PM | 
R011 | p1:L41 |  | 
R012 | p1:L45 |  | sole agenda item: unaudited results with LRR
R013 | p1:L46 |  | 
R014 | p1:L49 |  | 
R015 | p1:L53 |  | 
R016 | p1:L56 |  | 
R017 | p1:L56 |  | only FORWARD row
R018 | p1:L60 |  | 
R019 | p1:L72 |  | 
R020 | p1:L75 | TIMESTAMP_CHANGED_VS_ORIGINAL | NEW: signature 21-Oct-2026 15:51:24; original 19-Oct 23:11:37; BSE posting 21-Oct 16:56, 2 days after meeting end 23:00 on 19-Oct
R021 | p1:L77 |  | 
R022 | p1:L83 |  | 
R023 | p1:L85 |  | 
R024 | p1:L86 |  | 
R025 | p1:L90 |  | 
R026 | p1:L91 |  | 

## Page 2 standalone P&L: titles, units, dates, qualifiers, signing (10)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R027 | p2:L160 | NEW_STANDALONE | 
R028 | p2:L164 | NEW_STANDALONE | 
R029 | p2:L190 | NEW_STANDALONE | 
R030 | p2:L190 | NEW_STANDALONE | 
R031 | p2:L190 | NEW_STANDALONE | 
R032 | p2:L190 | NEW_STANDALONE | 
R033 | p2:L190 | SUPERSEDED_ID | 
R034 | p2:L190 | ITEM_13_SKIPPED | 
R179 | p2:L215 | NEW_STANDALONE | 
R180 | p2:L215 | NEW_STANDALONE | 

## Page 2 standalone P&L line items (24 lines x 6 cols = 144 cells) (144)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R035 | p2:L191 | NEW_STANDALONE | Revenue from operationsRevenue from operations ; equal to consolidated per A1 cross-check
R036 | p2:L191 | NEW_STANDALONE | Revenue from operationsRevenue from operations ; equal to consolidated per A1 cross-check
R037 | p2:L191 | NEW_STANDALONE | Revenue from operationsRevenue from operations ; equal to consolidated per A1 cross-check
R038 | p2:L191 | NEW_STANDALONE | Revenue from operationsRevenue from operations ; equal to consolidated per A1 cross-check
R039 | p2:L191 | NEW_STANDALONE | Revenue from operationsRevenue from operations ; equal to consolidated per A1 cross-check
R040 | p2:L191 | NEW_STANDALONE | Revenue from operationsRevenue from operations ; equal to consolidated per A1 cross-check
R041 | p2:L192 | NEW_STANDALONE | Other incomeOther income ; equal to consolidated per A1 cross-check
R042 | p2:L192 | NEW_STANDALONE | Other incomeOther income ; equal to consolidated per A1 cross-check
R043 | p2:L192 | NEW_STANDALONE | Other incomeOther income ; equal to consolidated per A1 cross-check
R044 | p2:L192 | NEW_STANDALONE | Other incomeOther income ; equal to consolidated per A1 cross-check
R045 | p2:L192 | NEW_STANDALONE | Other incomeOther income ; equal to consolidated per A1 cross-check
R046 | p2:L192 | NEW_STANDALONE | Other incomeOther income ; equal to consolidated per A1 cross-check
R047 | p2:L193 | NEW_STANDALONE | Total incomeTotal income ; equal to consolidated per A1 cross-check
R048 | p2:L193 | NEW_STANDALONE | Total incomeTotal income ; equal to consolidated per A1 cross-check
R049 | p2:L193 | NEW_STANDALONE | Total incomeTotal income ; equal to consolidated per A1 cross-check
R050 | p2:L193 | NEW_STANDALONE | Total incomeTotal income ; equal to consolidated per A1 cross-check
R051 | p2:L193 | NEW_STANDALONE | Total incomeTotal income ; equal to consolidated per A1 cross-check
R052 | p2:L193 | NEW_STANDALONE | Total incomeTotal income ; equal to consolidated per A1 cross-check
R053 | p2:L194 | NEW_STANDALONE | Cost of RM
R054 | p2:L194 | NEW_STANDALONE | Cost of RM
R055 | p2:L194 | NEW_STANDALONE | Cost of RM
R056 | p2:L194 | NEW_STANDALONE | Cost of RM
R057 | p2:L194 | NEW_STANDALONE | Cost of RM
R058 | p2:L194 | NEW_STANDALONE | Cost of RM
R059 | p2:L195 | NEW_STANDALONE | Purchase stock in trade
R060 | p2:L195 | NEW_STANDALONE | Purchase stock in trade
R061 | p2:L195 | NEW_STANDALONE | Purchase stock in trade
R062 | p2:L195 | NEW_STANDALONE | Purchase stock in trade
R063 | p2:L195 | NEW_STANDALONE | Purchase stock in trade
R064 | p2:L195 | NEW_STANDALONE | Purchase stock in trade
R065 | p2:L196 | NEW_STANDALONE | Change in inventories
R066 | p2:L196 | NEW_STANDALONE | Change in inventories
R067 | p2:L196 | NEW_STANDALONE | Change in inventories
R068 | p2:L196 | NEW_STANDALONE | Change in inventories
R069 | p2:L196 | NEW_STANDALONE | Change in inventories
R070 | p2:L196 | NEW_STANDALONE | Change in inventories
R071 | p2:L197 | NEW_STANDALONE | Employee benefits
R072 | p2:L197 | NEW_STANDALONE | Employee benefits
R073 | p2:L197 | NEW_STANDALONE | Employee benefits
R074 | p2:L197 | NEW_STANDALONE | Employee benefits
R075 | p2:L197 | NEW_STANDALONE | Employee benefits
R076 | p2:L197 | NEW_STANDALONE | Employee benefits
R077 | p2:L198 | NEW_STANDALONE | Finance costs
R078 | p2:L198 | NEW_STANDALONE | Finance costs
R079 | p2:L198 | NEW_STANDALONE | Finance costs
R080 | p2:L198 | NEW_STANDALONE | Finance costs
R081 | p2:L198 | NEW_STANDALONE | Finance costs
R082 | p2:L198 | NEW_STANDALONE | Finance costs
R083 | p2:L199 | NEW_STANDALONE | Depreciation
R084 | p2:L199 | NEW_STANDALONE | Depreciation
R085 | p2:L199 | NEW_STANDALONE | Depreciation
R086 | p2:L199 | NEW_STANDALONE | Depreciation
R087 | p2:L199 | NEW_STANDALONE | Depreciation
R088 | p2:L199 | NEW_STANDALONE | Depreciation
R089 | p2:L200 | NEW_STANDALONE | Other expenses
R090 | p2:L200 | NEW_STANDALONE | Other expenses
R091 | p2:L200 | NEW_STANDALONE | Other expenses
R092 | p2:L200 | NEW_STANDALONE | Other expenses
R093 | p2:L200 | NEW_STANDALONE | Other expenses
R094 | p2:L200 | NEW_STANDALONE | Other expenses
R095 | p2:L201 | NEW_STANDALONE | Total expenses
R096 | p2:L201 | NEW_STANDALONE | Total expenses
R097 | p2:L201 | NEW_STANDALONE | Total expenses
R098 | p2:L201 | NEW_STANDALONE | Total expenses
R099 | p2:L201 | NEW_STANDALONE | Total expenses
R100 | p2:L201 | NEW_STANDALONE | Total expenses
R101 | p2:L202 | NEW_STANDALONE | PBEIT
R102 | p2:L202 | NEW_STANDALONE | PBEIT
R103 | p2:L202 | NEW_STANDALONE | PBEIT
R104 | p2:L202 | NEW_STANDALONE | PBEIT
R105 | p2:L202 | NEW_STANDALONE | PBEIT
R106 | p2:L202 | NEW_STANDALONE | PBEIT
R107 | p2:L203 | NEW_STANDALONE ZERO_STANDING | Exceptional items ; template signal, canonical standing line
R108 | p2:L203 | NEW_STANDALONE ZERO_STANDING | Exceptional items ; template signal, canonical standing line
R109 | p2:L203 | NEW_STANDALONE ZERO_STANDING | Exceptional items ; template signal, canonical standing line
R110 | p2:L203 | NEW_STANDALONE ZERO_STANDING | Exceptional items ; template signal, canonical standing line
R111 | p2:L203 | NEW_STANDALONE ZERO_STANDING | Exceptional items ; template signal, canonical standing line
R112 | p2:L203 | NEW_STANDALONE ZERO_STANDING | Exceptional items ; template signal, canonical standing line
R113 | p2:L204 | NEW_STANDALONE | PBT
R114 | p2:L204 | NEW_STANDALONE | PBT
R115 | p2:L204 | NEW_STANDALONE | PBT
R116 | p2:L204 | NEW_STANDALONE | PBT
R117 | p2:L204 | NEW_STANDALONE | PBT
R118 | p2:L204 | NEW_STANDALONE | PBT
R119 | p2:L205 | NEW_STANDALONE | Current tax
R120 | p2:L205 | NEW_STANDALONE | Current tax
R121 | p2:L205 | NEW_STANDALONE | Current tax
R122 | p2:L205 | NEW_STANDALONE | Current tax
R123 | p2:L205 | NEW_STANDALONE | Current tax
R124 | p2:L205 | NEW_STANDALONE | Current tax
R125 | p2:L206 | NEW_STANDALONE | Deferred tax
R126 | p2:L206 | NEW_STANDALONE | Deferred tax
R127 | p2:L206 | NEW_STANDALONE | Deferred tax
R128 | p2:L206 | NEW_STANDALONE | Deferred tax
R129 | p2:L206 | NEW_STANDALONE | Deferred tax
R130 | p2:L206 | NEW_STANDALONE | Deferred tax
R131 | p2:L207 | NEW_STANDALONE | Total tax
R132 | p2:L207 | NEW_STANDALONE | Total tax
R133 | p2:L207 | NEW_STANDALONE | Total tax
R134 | p2:L207 | NEW_STANDALONE | Total tax
R135 | p2:L207 | NEW_STANDALONE | Total tax
R136 | p2:L207 | NEW_STANDALONE | Total tax
R137 | p2:L208 | NEW_STANDALONE | PAT
R138 | p2:L208 | NEW_STANDALONE | PAT
R139 | p2:L208 | NEW_STANDALONE | PAT
R140 | p2:L208 | NEW_STANDALONE | PAT
R141 | p2:L208 | NEW_STANDALONE | PAT
R142 | p2:L208 | NEW_STANDALONE | PAT
R143 | p2:L209 | NEW_STANDALONE | OCI A
R144 | p2:L209 | NEW_STANDALONE | OCI A
R145 | p2:L209 | NEW_STANDALONE | OCI A
R146 | p2:L209 | NEW_STANDALONE | OCI A
R147 | p2:L209 | NEW_STANDALONE | OCI A
R148 | p2:L209 | NEW_STANDALONE | OCI A
R149 | p2:L210 | NEW_STANDALONE ZERO_STANDING | OCI B ; nil in all six columns
R150 | p2:L210 | NEW_STANDALONE ZERO_STANDING | OCI B ; nil in all six columns
R151 | p2:L210 | NEW_STANDALONE ZERO_STANDING | OCI B ; nil in all six columns
R152 | p2:L210 | NEW_STANDALONE ZERO_STANDING | OCI B ; nil in all six columns
R153 | p2:L210 | NEW_STANDALONE ZERO_STANDING | OCI B ; nil in all six columns
R154 | p2:L210 | NEW_STANDALONE ZERO_STANDING | OCI B ; nil in all six columns
R155 | p2:L211 | NEW_STANDALONE | Total OCI
R156 | p2:L211 | NEW_STANDALONE | Total OCI
R157 | p2:L211 | NEW_STANDALONE | Total OCI
R158 | p2:L211 | NEW_STANDALONE | Total OCI
R159 | p2:L211 | NEW_STANDALONE | Total OCI
R160 | p2:L211 | NEW_STANDALONE | Total OCI
R161 | p2:L212 | NEW_STANDALONE | TCI
R162 | p2:L212 | NEW_STANDALONE | TCI
R163 | p2:L212 | NEW_STANDALONE | TCI
R164 | p2:L212 | NEW_STANDALONE | TCI
R165 | p2:L212 | NEW_STANDALONE | TCI
R166 | p2:L212 | NEW_STANDALONE | TCI
R167 | p2:L213 | NEW_STANDALONE | Paid-up capital
R168 | p2:L213 | NEW_STANDALONE | Paid-up capital
R169 | p2:L213 | NEW_STANDALONE | Paid-up capital
R170 | p2:L213 | NEW_STANDALONE | Paid-up capital
R171 | p2:L213 | NEW_STANDALONE | Paid-up capital
R172 | p2:L213 | NEW_STANDALONE | Paid-up capital
R173 | p2:L214 | NEW_STANDALONE | EPS
R174 | p2:L214 | NEW_STANDALONE | EPS
R175 | p2:L214 | NEW_STANDALONE | EPS
R176 | p2:L214 | NEW_STANDALONE | EPS
R177 | p2:L214 | NEW_STANDALONE | EPS
R178 | p2:L214 | NEW_STANDALONE | EPS

## Page 3 standalone balance sheet: title, units, dates, stamps, trade payables qualifier (7)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R181 | p3:L315 | NEW_STANDALONE | 
R182 | p3:L315 | NEW_STANDALONE | 
R183 | p3:L315 | NEW_STANDALONE | 
R184 | p3:L315 | SUPERSEDED_ID | 
R185 | p3:L315 | NEW_STANDALONE | 
R186 | p3:L315 | NEW_STANDALONE | 
R245 | p3:L344 | NEW_STANDALONE | 

## Page 3 standalone balance sheet line items (35 lines x 2 cols = 70 cells) (70)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R187 | p3:L316 | NEW_STANDALONE | 
R188 | p3:L316 | NEW_STANDALONE | 
R189 | p3:L317 | NEW_STANDALONE | 
R190 | p3:L317 | NEW_STANDALONE | 
R191 | p3:L318 | NEW_STANDALONE | 
R192 | p3:L318 | NEW_STANDALONE | 
R193 | p3:L319 | NEW_STANDALONE | 
R194 | p3:L319 | NEW_STANDALONE | 
R195 | p3:L320 | NEW_STANDALONE | 
R196 | p3:L320 | NEW_STANDALONE | 
R197 | p3:L321 | NEW_STANDALONE | 
R198 | p3:L321 | NEW_STANDALONE | 
R199 | p3:L322 | NEW_STANDALONE | 
R200 | p3:L322 | NEW_STANDALONE | 
R201 | p3:L323 | NEW_STANDALONE | 
R202 | p3:L323 | NEW_STANDALONE | 
R203 | p3:L324 | NEW_STANDALONE | 
R204 | p3:L324 | NEW_STANDALONE | 
R205 | p3:L325 | NEW_STANDALONE | 
R206 | p3:L325 | NEW_STANDALONE | 
R207 | p3:L326 | NEW_STANDALONE | 
R208 | p3:L326 | NEW_STANDALONE | 
R209 | p3:L327 | NEW_STANDALONE | 
R210 | p3:L327 | NEW_STANDALONE | 
R211 | p3:L328 | NEW_STANDALONE | 
R212 | p3:L328 | NEW_STANDALONE | 
R213 | p3:L329 | NEW_STANDALONE | 
R214 | p3:L329 | NEW_STANDALONE | 
R215 | p3:L330 | NEW_STANDALONE | 
R216 | p3:L330 | NEW_STANDALONE | 
R217 | p3:L331 | NEW_STANDALONE | 
R218 | p3:L331 | NEW_STANDALONE | 
R219 | p3:L332 | NEW_STANDALONE | 
R220 | p3:L332 | NEW_STANDALONE | 
R221 | p3:L333 | NEW_STANDALONE | 
R222 | p3:L333 | NEW_STANDALONE | 
R223 | p3:L334 | NEW_STANDALONE | 
R224 | p3:L334 | NEW_STANDALONE | 
R225 | p3:L335 | NEW_STANDALONE | 
R226 | p3:L335 | NEW_STANDALONE | 
R227 | p3:L336 | NEW_STANDALONE | 
R228 | p3:L336 | NEW_STANDALONE | 
R229 | p3:L337 | NEW_STANDALONE | 
R230 | p3:L337 | NEW_STANDALONE | 
R231 | p3:L338 | NEW_STANDALONE | 
R232 | p3:L338 | NEW_STANDALONE | 
R233 | p3:L339 | NEW_STANDALONE | 
R234 | p3:L339 | NEW_STANDALONE | 
R235 | p3:L340 | NEW_STANDALONE | 
R236 | p3:L340 | NEW_STANDALONE | 
R237 | p3:L341 | NEW_STANDALONE | 
R238 | p3:L341 | NEW_STANDALONE | 
R239 | p3:L342 | NEW_STANDALONE | 
R240 | p3:L342 | NEW_STANDALONE | 
R241 | p3:L343 | NEW_STANDALONE | 
R242 | p3:L343 | NEW_STANDALONE | 
R243 | p3:L344 | NEW_STANDALONE | MSME payables 30Sep26 757.56 vs nil 31Mar26 (new MSME dues)
R244 | p3:L344 | NEW_STANDALONE ZERO_STANDING | MSME payables 30Sep26 757.56 vs nil 31Mar26 (new MSME dues)
R246 | p3:L345 | NEW_STANDALONE | 
R247 | p3:L345 | NEW_STANDALONE | 
R248 | p3:L346 | NEW_STANDALONE | 
R249 | p3:L346 | NEW_STANDALONE | 
R250 | p3:L347 | NEW_STANDALONE | 
R251 | p3:L347 | NEW_STANDALONE | 
R252 | p3:L348 | NEW_STANDALONE | current provisions nil at 31Mar26
R253 | p3:L348 | NEW_STANDALONE ZERO_STANDING | current provisions nil at 31Mar26
R254 | p3:L349 | NEW_STANDALONE | 
R255 | p3:L349 | NEW_STANDALONE | 
R256 | p3:L350 | NEW_STANDALONE | 
R257 | p3:L350 | NEW_STANDALONE | 

## Page 4 standalone cash flow A/B: title, units, dates, superseded, signing (5)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R258 | p4:L443 | NEW_STANDALONE | 
R259 | p4:L443 | NEW_STANDALONE | 
R260 | p4:L443 | NEW_STANDALONE | 
R261 | p4:L443 | SUPERSEDED_ID | 
R262 | p4:L443 | NEW_STANDALONE | 

## Page 4 standalone cash flow line items (28 lines x 2 = 56 cells) (56)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R263 | p4:L444 | NEW_STANDALONE | 
R264 | p4:L444 | NEW_STANDALONE | 
R265 | p4:L445 | NEW_STANDALONE | 
R266 | p4:L445 | NEW_STANDALONE | 
R267 | p4:L446 | NEW_STANDALONE | 
R268 | p4:L446 | NEW_STANDALONE | 
R269 | p4:L447 | NEW_STANDALONE | nil FY26
R270 | p4:L447 | NEW_STANDALONE ZERO_STANDING | nil FY26
R271 | p4:L448 | NEW_STANDALONE | 
R272 | p4:L448 | NEW_STANDALONE | 
R273 | p4:L449 | NEW_STANDALONE | nil FY26
R274 | p4:L449 | NEW_STANDALONE ZERO_STANDING | nil FY26
R275 | p4:L450 | NEW_STANDALONE ZERO_STANDING | nil 6m vs 24.36 FY26
R276 | p4:L450 | NEW_STANDALONE | nil 6m vs 24.36 FY26
R277 | p4:L451 | NEW_STANDALONE | 
R278 | p4:L451 | NEW_STANDALONE | 
R279 | p4:L452 | NEW_STANDALONE | 
R280 | p4:L452 | NEW_STANDALONE | 
R281 | p4:L453 | NEW_STANDALONE | 
R282 | p4:L453 | NEW_STANDALONE | 
R283 | p4:L454 | NEW_STANDALONE | 
R284 | p4:L454 | NEW_STANDALONE | 
R285 | p4:L455 | NEW_STANDALONE | 
R286 | p4:L455 | NEW_STANDALONE | 
R287 | p4:L456 | NEW_STANDALONE | 
R288 | p4:L456 | NEW_STANDALONE | 
R289 | p4:L457 | NEW_STANDALONE | 
R290 | p4:L457 | NEW_STANDALONE | 
R291 | p4:L458 | NEW_STANDALONE | 
R292 | p4:L458 | NEW_STANDALONE | 
R293 | p4:L459 | NEW_STANDALONE | 
R294 | p4:L459 | NEW_STANDALONE | 
R295 | p4:L460 | NEW_STANDALONE | 
R296 | p4:L460 | NEW_STANDALONE | 
R297 | p4:L461 | NEW_STANDALONE | 
R298 | p4:L461 | NEW_STANDALONE | 
R299 | p4:L462 | NEW_STANDALONE | 
R300 | p4:L462 | NEW_STANDALONE | 
R301 | p4:L463 | NEW_STANDALONE | 
R302 | p4:L463 | NEW_STANDALONE | 
R303 | p4:L464 | NEW_STANDALONE | 
R304 | p4:L464 | NEW_STANDALONE | 
R305 | p4:L465 | NEW_STANDALONE | 
R306 | p4:L465 | NEW_STANDALONE | 
R307 | p4:L466 | NEW_STANDALONE ZERO_STANDING | nil 6m vs 11,030.50 FY26 (FY26 asset sale proceeds)
R308 | p4:L466 | NEW_STANDALONE | nil 6m vs 11,030.50 FY26 (FY26 asset sale proceeds)
R309 | p4:L467 | NEW_STANDALONE | 
R310 | p4:L467 | NEW_STANDALONE | 
R311 | p4:L468 | NEW_STANDALONE | 
R312 | p4:L468 | NEW_STANDALONE | 
R313 | p4:L469 | NEW_STANDALONE | 
R314 | p4:L469 | NEW_STANDALONE | 
R315 | p4:L470 | NEW_STANDALONE | 
R316 | p4:L470 | NEW_STANDALONE | 
R317 | p4:L471 | NEW_STANDALONE | 
R318 | p4:L471 | NEW_STANDALONE | 

## Page 5 standalone cash flow C: title, units, dates, superseded, signing (5)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R319 | p5:L520 | NEW_STANDALONE | 
R320 | p5:L520 | NEW_STANDALONE | 
R321 | p5:L520 | NEW_STANDALONE | 
R322 | p5:L520 | SUPERSEDED_ID | 
R323 | p5:L520 | NEW_STANDALONE | 

## Page 5 standalone cash flow line items (7 lines x 2 = 14 cells) (14)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R324 | p5:L521 | NEW_STANDALONE | 
R325 | p5:L521 | NEW_STANDALONE | 
R326 | p5:L522 | NEW_STANDALONE | 
R327 | p5:L522 | NEW_STANDALONE | 
R328 | p5:L523 | NEW_STANDALONE ZERO_STANDING | DIVIDEND_PAID nil in 6m though Rs 2/share approved at AGM 30-Sep-2026 (R350,R355); payment falls after period end or outside the statement window
R329 | p5:L523 | NEW_STANDALONE | DIVIDEND_PAID nil in 6m though Rs 2/share approved at AGM 30-Sep-2026 (R350,R355); payment falls after period end or outside the statement window
R330 | p5:L524 | NEW_STANDALONE | 
R331 | p5:L524 | NEW_STANDALONE | 
R332 | p5:L525 | NEW_STANDALONE | 
R333 | p5:L525 | NEW_STANDALONE | 
R334 | p5:L526 | NEW_STANDALONE | 
R335 | p5:L526 | NEW_STANDALONE | 
R336 | p5:L527 | NEW_STANDALONE | 
R337 | p5:L527 | NEW_STANDALONE | 

## Page 5 cash flow notes (2 notes + standard) (3)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R338 | p5:L528 | NEW_STANDALONE | 
R339 | p5:L528 | NEW_STANDALONE | 
R340 | p5:L528 | NEW_STANDALONE | 

## Page 6 standalone notes 1-5, dividend, signature (18)
ROW_ID | page:line | A2 flags | cross-ref / materiality
R341 | p6:L533 | NEW_STANDALONE NOTE_NUMBERED | 
R342 | p6:L534 | NEW_STANDALONE | 
R343 | p6:L536 | NEW_STANDALONE | 
R344 | p6:L538 | NEW_STANDALONE NOTE_NUMBERED | 
R345 | p6:L542 | NEW_STANDALONE NOTE_NUMBERED | 
R346 | p6:L542 | NEW_STANDALONE | 
R347 | p6:L550 | NEW_STANDALONE NOTE_NUMBERED | 
R348 | p6:L550 | NEW_STANDALONE | 
R349 | p6:L553 | NEW_STANDALONE | unnumbered segment qualifier
R350 | p6:L557 | NEW_STANDALONE NOTE_NUMBERED | FY26 final dividend Rs 2/share; cross-ref cash flow R328/R329
R351 | p6:L557 | NEW_STANDALONE | 
R352 | p6:L557 | NEW_STANDALONE | 
R353 | p6:L557 | NEW_STANDALONE | 
R354 | p6:L558 | NEW_STANDALONE | 
R355 | p6:L559 | NEW_STANDALONE | 
R356 | p6:L570 | NEW_STANDALONE SIGNATURE_BLOCK | 
R357 | p6:L571 | NEW_STANDALONE SIGNATURE_BLOCK | signatory name partly illegible in text layer
R358 | p6:L572 | NEW_STANDALONE SIGNATURE_BLOCK | 

## Pages 7-15 CARRIED_UNCHANGED (consolidated + auditor reports; revised id = original id + 294; revised line = original line + 101)
Per A1 DIFF VS ORIGINAL: no cell differs. Full detail lives in work/ledger_results_gallantt_q2fy27.md at the original IDs. Ranges below group every carried ID.
RANGE | page | rows | original IDs | what | flags
R359-R521 | p7 | 163 | R065-R227 | consolidated P&L (R359 superseded garbled row, 156 number cells, titles) | CARRIED_UNCHANGED; ZERO_STANDING cells carried
R522-R595 | p8 | 74 | R228-R301 | consolidated balance sheet | CARRIED_UNCHANGED
R596-R654 | p9 | 59 | R302-R360 | consolidated cash flow A/B | CARRIED_UNCHANGED
R655-R674 | p10 | 20 | R361-R380 | consolidated cash flow C, notes 1-2 (R658,R659,R674) | CARRIED_UNCHANGED
R675-R692 | p11 | 18 | R381-R398 | consolidated notes 1-5, signature | CARRIED_UNCHANGED
R693-R702 + R744 | p12 | 11 | R399-R408 | limited review report (standalone, p12) paras | CARRIED_UNCHANGED; R744 = A1 CORRECTION to R697 (standalone statements ARE on pp2-5, R027-R358), flag CORRECTION_ROW, R697 note superseded; STANDALONE_STATEMENT_ABSENT now RESOLVED (standalone statements pp2-5 present)
R703-R714 | p13 | 12 | R409-R420 | review report paras, auditor signature block, UDIN (standalone) | CARRIED_UNCHANGED; AUDITOR_CHANGE
R715-R724 | p14 | 10 | R421-R430 | consolidated review report | CARRIED_UNCHANGED
R725-R743 | p15 | 19 | R431-R449 | consolidated review report, subsidiary figures, signature, UDIN | CARRIED_UNCHANGED; ZERO_STANDING cells; UDIN_DIFFERS

## MISSING_FROM_STRUCTURED
none found.

## ENTITY_CHANGE
none (perimeter carried unchanged: Suryalaxmi Technologies Pvt Ltd).

```yaml
stage: A2-enumerator
company: "GALLANTT"
quarter: "q2fy27"
doctype: "resultsrev"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/gallantt-q2fy27/work/ledger_resultsrev_gallantt_q2fy27.md"
counts:
  notes: 15
  line_items: 190
  zero_standing: 46
  agenda_items: 1
  auditor_paras: 52
  entities: 1
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, NEW_STANDALONE, CARRIED_UNCHANGED, DATE_FIXED_VS_ORIGINAL, TIMESTAMP_CHANGED_VS_ORIGINAL, SUPERSEDED_ID, STANDALONE_STATEMENT_ABSENT_RESOLVED, AUDITOR_CHANGE, UDIN_DIFFERS, STANDALONE_CONSOL_DIFF, DIVIDEND_PAID_NIL_POST_AGM]
ids_in_structured: 744
ids_referenced: 744
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Revised 21-Oct filing: new content is page 1 (subject date fixed to 19-Oct-2026, signature 21-Oct 15:51) and standalone pp2-6 (R027-R358: 94 distinct lines, 284 cells, 19 ZERO_STANDING, 7 notes). R359-R743 carried unchanged (original id + 294). Original flags STANDALONE_STATEMENT_ABSENT and DATE_INCONSISTENCY are resolved. Standalone H1FY27 cash flow shows dividend paid nil although Rs 2/share was approved at the 30-Sep-2026 AGM (R350,R355,R328), so payment falls after period end; A3 should test against Q3. Standalone FY26 PAT 48,427.31 vs consolidated 48,426.70 (0.61 lakh gap), no associate line in standalone. Counts: line_items 94 new + 96 carried; cells 284 + 296."
```
