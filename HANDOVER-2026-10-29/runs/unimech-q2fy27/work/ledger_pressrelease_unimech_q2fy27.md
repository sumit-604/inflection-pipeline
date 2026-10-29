=== A2 COUNT TEST ===
ids_in_structured: 123 | ids_referenced_in_ledger: 123 | orphan_ids: [] | match: yes
category: slides(pages)      grep_count: 3    sweep_count: 3    match: yes
category: slide_numbers      grep_count: 68   sweep_count: 68   match: yes  (R001-R068; table values 32 = 4 rows x 8 cols, R015-R046)
category: entities           grep_count: 19   sweep_count: 19   match: yes  (+3 ENTITY-SUMMARY R088-R090)
category: forward            grep_count: 11   sweep_count: 11   match: yes
category: dates              grep_count: 13   sweep_count: 13   match: yes
category: footnotes_qualifiers grep_count: 9  sweep_count: 9    match: yes
category: zero_standing      grep_count: 0    sweep_count: 0    match: yes
fulltext sweep: numeric tokens in fulltext lines 18-145 all traced to a row or a grouped row; unrowed: see MISSING list (minor, none material)
gate_a2: pass
=== END COUNT TEST ===

## Slides (pages; no prior deck, no DROPPED_SLIDE test possible)
P1 | PDF p1 | text | cover letter to BSE/NSE | rows R001-R007, R069-R073, R102-R104, R105, R116
P2 | PDF p2 | text + table | press release (page 1 of release) | rows R008-R064, R074-R080, R091-R100, R106-R113, R115, R117-R121
P3 | PDF p3 | text | about, contacts, safe-harbor | rows R065-R068, R081-R090, R101, R114, R122-R123

## Slide numbers (ROW | category | flags | note)
R001-R007 | cover-letter ids/dates | RESTATED(R001=R102, R003=R103, R004=R104) | admin
R008-R014 | headline numbers | RESTATED(R008=R025, R009=R023, R010=R033, R011=R041, R012=R039, R013=R063, R014 base absent) | headline rounded; "8-times" prior-year order book base not given
R015-R022 | table Total Revenue | RESTATED(R015 vs R023 different metric) | Total vs Operations gap present
R023-R030 | table Revenue from Operations | RESTATED(R025=R048=R008 pct; R028=R050=R061) |
R031-R038 | table EBITDA | RESTATED(R033=R053; R036=R055) |
R039-R046 | table PAT | RESTATED(R039=R057; R044=R059) |
R047-R060 | bullet restatements of table | RESTATED | R054 40% margin: basis not stated (R119)
R051 | ~96% of FY26 revenue | QUALIFIER ref R118 | FY26 base not stated
R061-R063 | CMD quote numbers | RESTATED(R061=R028, R062=R030, R063=R013) |
R064 | 20-month pipeline | RESTATED(R113) |
R065-R068 | about-company numbers | | R068 cert names

## Entities
R069-R087 | ENTITY | none; no prior list so no ENTITY_CHANGE test | R076, R078 OEMs/customers UNNAMED (MGMT_ABSENCE of names); R080 Saudi JV: no detail
R088-R090 | ENTITY-SUMMARY | grouped blocks (certs, contact block, safe-harbor risks)

## Forward-looking
R091-R101 | FORWARD | R094 H2 semiconductor step-up UNQUANTIFIED; R096 "compounding multi-year" UNQUANTIFIED; R097/R098 no dates, capex or size | R101 boilerplate

## Dates
R102-R114 | DATE | RESTATED(R102/R103/R106; R105/R107; R114=R065; R113=R064) | R111/R112 timing vague

## Footnotes / qualifiers
R115-R123 | QUALIFIER | R115/R116 unaudited; FOOTNOTE_UNRESOLVED: R118, R119, R120, R121 (definitions absent) | R122-R123 disclaimer

## ZERO_STANDING: none (no nil/dash rows in table)

## MISSING_FROM_STRUCTURED (fulltext sweep; none material)
M01 | line 123 | second website form "www.unimechaerospace.com" (R073 covers https form) | trivial
M02 | lines 104, 147 | page-footer numerals "1", "2" | trivial
M03 | lines 128,133,138 | individual phone numbers/emails | grouped under R089, treated accounted
M04 | lines 80-81 | claims "high-margin order mix", "strong operating leverage" (qualitative, no number) | not numbers; noted for A3 if wanted
M05 | lines 116-117 | capability list (build-to-print/spec, machining, etc.) | descriptive; R083/R084 partial
