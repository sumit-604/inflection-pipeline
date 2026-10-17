# A2 LEDGER: Cyient DLM Q2 FY27 press release (pressrelease)
ids_in_structured: 60 | ids_referenced_in_ledger: 60 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides(pages)   grep_count: 3   sweep_count: 3   match: yes
category: slide_numbers   grep_count: 24  sweep_count: 24  match: yes  (NUMBER rows R001-R024)
category: entities        grep_count: 16  sweep_count: 16  match: yes  (R025-R040)
category: forward_stmts   grep_count: 7   sweep_count: 7   match: yes  (R041-R047)
category: dates           grep_count: 8   sweep_count: 8   match: yes  (R048-R055)
category: qualifiers      grep_count: 5   sweep_count: 5   match: yes  (R056-R060)
category: notes/footnotes grep_count: 0   sweep_count: 0   match: yes  (A1 states no markers; fulltext grep for numbered/Note: lines returned none)
category: line_items      grep_count: 0   sweep_count: 0   match: yes  (no financial tables)
category: zero_standing   grep_count: 0   sweep_count: 0   match: yes
page split: p1=11 p2=28 p3=21 (sum 60)
gate_a2: pass
=== END COUNT TEST ===

## 1. Slides / pages
| ROW_ID | category | flags | note |
|---|---|---|---|
| page 1 (R020-R028, R039, R048, R060) | cover letter, text | - | exchange letter, signed |
| page 2 (R001-R015 etc.) | press release headline + results, text | - | |
| page 3 (R016-R019 etc.) | segments, outlook, boilerplate, contacts | - | |
Prior deck not available: no DROPPED_SLIDE test possible.

## 2. Numbers
| ROW_ID | category | flags | cross-ref / note |
|---|---|---|---|
| R001 | growth | RESTATED | = R004 |
| R002 | growth | RESTATED | = R008 |
| R003 | revenue | - | |
| R004 | growth | RESTATED | = R001 |
| R005 | growth | - | EBITDA growth 9.5% vs revenue 26.5% (R001): margin compression |
| R006 | profit | - | |
| R007 | margin | - | |
| R008 | growth | RESTATED | = R002 |
| R009 | profit | - | normalized basis, see R056 |
| R010 | margin | - | |
| R011 | profit | - | reported, includes R012 |
| R012 | one-off | - | earnout reversal gain, see R057 |
| R013 | order book | - | basis undefined, R058 |
| R014 | order book | - | |
| R015 | cash flow | FOOTNOTE_UNRESOLVED | FCF definition missing, R059 |
| R016 | order intake | - | |
| R017 | order intake | - | |
| R018 | order intake | - | |
| R019 | customers | - | |
| R020 | admin id | - | |
| R021 | signature timestamp | - | 17:18:23 IST; board meeting not applicable to press release |
| R022 | admin | - | |
| R023 | admin | - | |
| R024 | admin | - | |

## 3. Entities
| ROW_ID | category | flags | note |
|---|---|---|---|
| R025, R026 | exchange addressee | - | |
| R027 | regulation | - | |
| R028 | signatory | - | |
| R029 | quoted executive | - | MD and CEO quoted; CFO not quoted |
| R030 | company | - | |
| R031, R032 | segments (growth leaders) | - | |
| R033, R034 | segments (contributors) | - | |
| R035 | acquisition | - | integration complete |
| R036 | subsidiary | ENTITY_CHANGE | renamed (Cyient DLM Electronics Inc. to Altek Electronics); no prior list |
| R037 | capability | - | |
| R038, R039, R040 | contact / address / boilerplate groups | - | |

## 4. Forward-looking statements
| ROW_ID | flags | note |
|---|---|---|
| R041-R047 | - | R044 outlook has no figure; R041 and R044 both rest on order book |

## 5. Dates
| ROW_ID | flags | note |
|---|---|---|
| R048, R049 | RESTATED | letter and release date, both 15 Oct 2026 |
| R050, R051 | RESTATED | period, quarter label |
| R052, R053 | basis labels | |
| R054 | - | "for the year" unnamed FY |
| R055 | - | |

## 6. Qualifiers / disclaimers
| ROW_ID | flags | note |
|---|---|---|
| R056 | FOOTNOTE_UNRESOLVED | normalized PAT undefined |
| R057 | - | reported PAT includes one-off R012 |
| R058 | FOOTNOTE_UNRESOLVED | order book basis |
| R059 | FOOTNOTE_UNRESOLVED | FCF basis |
| R060 | - | digital signature |

## MISSING_FROM_STRUCTURED
None found.

## ACCOUNTABILITY
R001-R060 all referenced (24+16+7+8+5 = 60). Orphans: none.
