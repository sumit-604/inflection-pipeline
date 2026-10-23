# A2 LEDGER, TINNARUBR Q2 FY27 press release (presentation slot)
Source: extracted/tinnarubr-presentation-q2fy27-structured.md (R001-R138). Rows reference IDs; values live there.

=== A2 COUNT TEST ===
category: slides(pages)       grep_count: 3    sweep_count: 3    match: yes
category: slide_numbers       grep_count: 66   sweep_count: 66   match: yes   (R001-R066)
category: entities            grep_count: 29   sweep_count: 29   match: yes   (R067-R095)
category: forward             grep_count: 14   sweep_count: 14   match: yes   (R096-R109)
category: dates               grep_count: 18   sweep_count: 18   match: yes   (R110-R127)
category: qualifiers_footnotes grep_count: 11  sweep_count: 11   match: yes   (R128-R138)
category: line_items/notes/agenda/auditor: not applicable (press release; no tables, notes, agenda, audit report)
category: zero_standing       grep_count: 0    sweep_count: 0    match: yes
total_ids                     grep_count: 138  sweep_count: 138  match: yes
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 138 | ids_referenced_in_ledger: 138 | orphan_ids: [] | match: yes

## Slides (pages). Titles/content types not tagged in A1; page-level only.
| Page | Content type | ID span | Note |
| 1 | text, covering letter | R001-R005, R067-R073, R124-R127 | Reg 30 filing; signature R005/R127 |
| 2 | text, results narrative + KPI block | R006-R056, R074-R086, R096-R100, R109-R121, R128-R137 | KPI pairing positional |
| 3 | text, outlook / Vision 2029 / profile | R057-R066, R087-R095, R101-R108, R122-R123, R138 | no disclaimer |

## Slide numbers (every number)
| ROW_ID | category | flags | cross-ref / note |
| R001-R005 | identifiers, page 1 | | admin |
| R006 | headline | RESTATED | = R011 (H1 EBITDA 50%) |
| R007 | H1 revenue | | |
| R008 | H1 revenue YoY | POSITIONAL_PAIRING | |
| R009 | Q2 revenue | | |
| R010 | Q2 revenue YoY | RESTATED | = R023 |
| R011 | H1 EBITDA YoY | POSITIONAL_PAIRING, RESTATED | = R006 |
| R012 | Q2 EBITDA YoY | RESTATED | = R024 |
| R013 | H1 EBITDA | | |
| R014 | H1 PAT YoY | POSITIONAL_PAIRING | |
| R015 | Q2 EBITDA | | |
| R016 | Q2 PAT YoY | POSITIONAL_PAIRING, RESTATED | = R025 (explicit in text); only positional row with an independent text restatement |
| R017-R018 | H1 / Q2 PAT | | |
| R019-R022 | standalone H1 EBITDA, PAT, margins | LOWER_BOUND | R130 |
| R023-R027 | Q2 consolidated YoY and margins | RESTATED (R023-R025), LOWER_BOUND (R026-R027) | R131 |
| R028-R031 | segment YoY H1 | | R078-R081 |
| R032-R034 | debt 9%, 111, 121 | | R132 basis unstated |
| R035-R036 | interest coverage | | R114 |
| R037 | net D/E | | R133 definition unstated |
| R038-R039 | CARE ratings | | R075 |
| R040-R041 | MRP capacity | RESTATED | R096, R097 |
| R042-R045 | PCMB | | R077 |
| R046-R047 | capex done / planned | RESTATED | R047=R098 |
| R048-R049 | Andhra | RESTATED | R048=R099=R134 |
| R050-R053 | renewables | | |
| R054-R056 | Oman utilisation, margins | | R084 |
| R057-R061 | Vision 2029 | RESTATED | R103-R106; R060 same figure as R026 threshold (different scope) |
| R062-R063 | locations 8 to 10 | RESTATED | R107 |
| R064-R066 | plants, crushing capacity, recovery | | R136 |

## Entities
| ROW_ID | category | flags | note |
| R067-R073 | page 1 addressees, filer, signatory | | |
| R074 | reporting company | | |
| R075 | CARE Ratings | | rating upgrade stated; prior rating not given |
| R076-R077 | MRP, PCMB lines | | |
| R078-R081 | segments | | |
| R082-R083 | Andhra facility, recycling plans | | |
| R084 | Oman facility | | |
| R085 | Tinna Rubber Chile SpA | ENTITY_CHANGE | new wholly owned subsidiary, no prior list to diff |
| R086 | Chile | RESTATED | R093, R109 |
| R087-R095 | policy, plan, HQ, plants, South Africa, Saudi, Chile, products, customers | | R091 South Africa operation: not in consolidation detail |

## Forward-looking
| ROW_ID | category | flags | note |
| R096 | MRP commissioning Q3 FY27 | DATED_COMMITMENT | R115, R040 |
| R097 | 20,000 MTPA, world's largest | | R041 |
| R098 | capex Rs 100 Cr | | R047 |
| R099-R100 | Andhra plan | CEILING_NOT_COMMITMENT | R134, R048 |
| R101-R102 | policy / demand claims | | no source cited |
| R103-R107 | Vision 2029 targets | | R057-R063; R104 metric undefined (R135) |
| R108 | Saudi, Chile expansion | | undated |
| R109 | Chile purpose | | R085 |

## Dates
| R110-R123 | period/horizon dates | | H1FY27 etc. |
| R124-R127 | covering letter and signature dates | | R127 vs R005 time stamp; board meeting time absent from release |

## Qualifiers / footnotes
| R128-R136 | qualifiers | | R128 consolidated basis; R129 positional; R130-R131 lower bounds; R132-R133 undefined basis; R134 ceiling; R135 profitability undefined; R136 approximation |
| R137 | no footnote markers | FOOTNOTE_NONE | |
| R138 | no safe-harbour text | NO_DISCLAIMER | |

## Flags summary
ZERO_STANDING: none. DROPPED_SLIDE: not assessable (no prior). MISSING_FROM_STRUCTURED: none.
