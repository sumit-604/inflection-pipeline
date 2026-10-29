# A2 LEDGER: DYCL pressrelease q2fy27
Source: extracted/dycl-pressrelease-q2fy27-structured.md (Rs Crores x1). Page 2 table rows anchored to render-corrected block (fulltext lines 112-124).

ids_in_structured: 151 | ids_referenced_in_ledger: 151 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: numbers          grep_count: 107  sweep_count: 107  match: yes
category: entities         grep_count: 17   sweep_count: 17   match: yes
category: forward_stmts    grep_count: 5    sweep_count: 5    match: yes
category: dates            grep_count: 11   sweep_count: 11   match: yes
category: qualifiers       grep_count: 11   sweep_count: 11   match: yes
category: table_line_items grep_count: 10   sweep_count: 10   match: yes (P&L, each x6 periods = R013-R072)
category: borrowing_lines  grep_count: 8    sweep_count: 8    match: yes (each x3 dates = R076-R099)
category: notes/agenda/auditor/turns/questions/slides: N.A. (press release)
missing_from_structured: 3 (M1, M2, M3 below; added rows, structured grep unchanged)
gate_a2: pass
=== END COUNT TEST ===

## NUMBERS
ROW_ID | category | flags | note
R001-R006 | H1FY27 snapshot tiles (rev, OP, PAT, YoY) | RESTATED | tiles restate table R016, R022, R064; tile rounding per R143
R007-R012 | Q2FY27 snapshot tiles | RESTATED | restate R013, R019, R061
R013-R018 | P&L Operating Revenue x6 periods | - | 
R019-R024 | P&L Operating Profits x6 | - |
R025-R030 | P&L Operating Margins % x6 | - | Q2FY27 10.0% vs Q2FY26 11.0%
R031-R036 | P&L Finance Cost x6 | - | Q2FY27 4.2 vs 2.9 prior
R037-R042 | P&L Depreciation x6 | - |
R043-R048 | P&L Other Income x6 | - |
R049-R054 | P&L PBT x6 | - |
R055-R060 | P&L Income Tax x6 | - |
R061-R066 | P&L PAT x6 | - |
R067-R072 | P&L EPS x6 | - |
R073 | receivable days | - | defined by R146
R074 | export sales H1 | - | R147
R075 | order book | - | R148, no inclusion definition
R076-R078 | Term Loans x3 dates | - |
R079-R081 | Other Loans x3 | - |
R082-R084 | Working Capital Loans x3 | - | 64.4 to 32.3 QoQ
R085-R087 | Total On-balance sheet Debt x3 | - |
R088-R090 | LC Creditors off-balance x3 | - | R150
R091-R093 | Total Borrowing x3 | - |
R094-R096 | Cash & equivalents x3 | - |
R097-R099 | Net Debt x3 | - |
R100 | manufacturing plants | - | cross-ref R123
R101 | regional sales offices | - | R124
R102-R107 | identifiers (scrip, CIN, membership, postal, phone) | - | non-financial

## ENTITIES (no consolidation list in doc; no prior ledger, no ENTITY_CHANGE assessable)
R108-R114 | filing addressees, regulation, signatory, office | - |
R115-R116 | company, MD quote speaker | - |
R117 | new manufacturing facility | - | cross-ref R126, R127, R135
R118-R122 | products and customer segments | - |
R123-R124 | plant locations, offices | - |

## FORWARD STATEMENTS
R125 | MD growth expectation | - | 
R126 | new plant on stream | - | links R117
R127 | new plant contributes from second half | - | no quantification
R128 | export momentum | - |
R129 | disclaimer | - | pair R151

## DATES
R130-R140 | letter, release, periods, signature timestamp | - | R138 signature 13:02:41 IST on 27.10.2026; no board meeting times in doc

## QUALIFIERS
R141-R151 | unaudited, YoY basis, rounding, units, definitions, disclaimer | - | R145 is A1 note, not source text

## MISSING_FROM_STRUCTURED
ROW_ID | category | flags | claim text | line
M1 | forward/qualitative | MISSING_FROM_STRUCTURED | "Strong growth momentum from both government and private sector players" (key highlight, no figure) | fulltext line 127
M2 | qualitative MD statement | MISSING_FROM_STRUCTURED | "The business environment has improved despite crude price volatility and geo political disruptions." | fulltext line 108
M3 | QUALIFIER (MD execution-discipline claim, no figure) | MISSING_FROM_STRUCTURED | "We have always followed disciplined approach towards execution, expanding our market reach and strengthening our position as a trusted partner of evolving Indian power landscape" | fulltext lines 108-110 (sentence begins end of line 108, body on 109-110)

## Statement-only categories: N.A. (notes, agenda items, auditor paras, turns, questions, slides)
