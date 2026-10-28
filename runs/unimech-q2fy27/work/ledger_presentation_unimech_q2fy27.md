# A2 LEDGER: UNIMECH q2fy27 investor presentation
ids_in_structured: 670 | ids_referenced_in_ledger: 670 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides            grep_count: 26  sweep_count: 26  match: yes   (26 pdf pages; 23 with rows; pages 9, 17, 23 are section dividers with no rows)
category: slide_numbers (structured rows)  grep_count: 670  sweep_count: 670  match: yes   (NUMBER 509 | ENTITY 74 | FORWARD 41 | DATE 27 | QUALIFIER 19; type-grep equals A1 header)
category: line_items        grep_count: 81  sweep_count: 81  match: yes   (p8 20 lines x cols = 142 rows; p24 23 lines = 92 rows; p25 38 lines = 152 rows; render transcription line counts 20/23/38)
category: zero_standing     grep_count: 14  sweep_count: 14  match: yes   (plus 4 NA_STANDING, listed separately)
category: footnotes_qualifiers grep_count: 19 sweep_count: 19  match: yes
category: fulltext_number_sweep (independent, data slides 6,7,8,20,24,25 render transcription vs structured values, multiset compare) match: yes except 2 unrowed items below
  ID sequence R001-R670: no gaps, no duplicates.
orphan_ids: []
unrowed_items (fulltext number/label with no structured row): 2 (added below as MISSING_FROM_STRUCTURED); non-data ignored: p6 chart y-axis ticks 100.00-550.00 (lines 118-131), p25 list index labels 1-4, page-number footers.
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (page -> title, content type, ID range)
| page | title | type | IDs |
|---|---|---|---|
| 1 | Exchange forwarding letter | text | R001-R002, R510-R514, R584, R625-R629, R652 |
| 2 | Cover: Unimech Aerospace | text | R630 |
| 3 | Disclaimer | text | R515 |
| 4 | Section divider Quarter & Half | text | R631 |
| 5 | Message from the MD's desk | text | R003-R006, R516-R519, R585-R590, R632 |
| 6 | Q2 & H1 FY27* scoreboard | chart + text | R007-R040, R520-R524, R591-R593, R633-R635, R653-R655 |
| 7 | Order Book | chart + table | R041-R068, R525-R529, R594, R636-R638, R656-R659 |
| 8 | Consolidated P&L Q2/H1 | table | R069-R210, R530-R531, R639, R660-R662 |
| 9 | Business divider | divider | none (no data) |
| 10 | Aero Tooling / MRO | text | R211-R212, R532-R537 |
| 11 | Precision Components & Assemblies | text | R213-R214, R538-R542 |
| 12 | Initiatives Driving Long-Term Advantage | text | R215-R216, R543-R545, R595-R599, R663 |
| 13 | Hobel Bellows acquisition | text | R217-R221, R546-R548, R600-R602 |
| 14 | Kanoo-Unimech JV | text | R222-R228, R549-R551, R603-R604, R640, R664 |
| 15 | Competitive Edge | text + chart | R229-R235, R552-R553, R605-R611, R641-R642, R665-R666 |
| 16 | Key Growth Drivers | text | R554-R555, R612-R622 |
| 17 | Company divider | divider | none |
| 18 | Trusted Global Precision Mfg Platform | text | R236-R243, R556-R557, R643-R644 |
| 19 | Journey of Strategic Evolution | timeline | R244-R251, R558-R566, R623-R624, R645-R650 |
| 20 | Manufacturing Facilities | icon text | R252-R255, R567-R569, R667-R668 |
| 21 | Founder Led Management | text | R256-R260, R570-R576 |
| 22 | Independent Board | text | R261-R265, R577-R582 |
| 23 | Financial divider | divider | none |
| 24 | Historical Income Statement | table | R266-R357, R651, R669 |
| 25 | Historical Balance Sheet | table | R358-R509, R670 |
| 26 | Thank you / IR contacts | text | R583 |
DROPPED_SLIDE: not assessable (no prior-quarter ledger).

## 2. NUMBERS (R001-R509 grouped by slide; every ID referenced above in section 1)
| IDs | category | flags | note |
|---|---|---|---|
| R001-R006 | headline numbers p1/p5 | RESTATED | R003-R005 (H1 Rs 2,306 Mn, 85%, order book Rs 8,546 Mn) restate R019/R020, R041-R043 |
| R007-R040 | scoreboard p6 | RESTATED | R007 restates chart; R015-R040 repeat on p8 (R069+) and p24 |
| R041-R068 | order book + FAI funnel p7 | ZERO_STANDING R063; NA_STANDING R066 | R050 153% growth is on confirmed POs only (R658); R041 total ~855 Cr includes ~589 Cr LTA/award letters |
| R069-R210 | P&L line items p8 | NA_STANDING R167,R169,R172 | associate-entity row NA growth; Hobel wef 1 May 2026 (R531, R635) affects comparability |
| R211-R265 | operating stats p10-p22 | | |
| R252-R255 | facility stats p20 | | render-verified |
| R266-R357 | history P&L p24 | ZERO_STANDING R314 | ROCE/ROE/FAT rows included (R340-R357 range ratios) |
| R358-R509 | balance sheet p25 | ZERO_STANDING R374,R378,R382,R384,R385,R438,R439,R440,R446,R455,R458,R474 | goodwill nil in FY24-FY26, 3,219.9 in H1 FY27 (Hobel); investments current 3,385.8/4,684.1 to 1,808.5 |

## 3. ZERO_STANDING (14) and NA_STANDING (4)
ZERO_STANDING: R063, R314, R374, R378, R382, R384, R385, R438, R439, R440, R446, R455, R458, R474.
NA_STANDING: R066, R167, R169, R172.

## 4. ENTITIES (R510-R583, 74) | flags
R510-R583 all enumerated per slide in section 1. ENTITY_CHANGE: R531 and R543 (Hobel consolidated wef 1 May 2026, acquisition), R522/R544/R549-R551 (Kanoo-Unimech JV, associate line R530), R545/R566 (Dheya Engineering). No prior list to diff.

## 5. FORWARD (R584-R624, 41) and DATES (R625-R651, 27)
Forward statements: R584-R624, grouped by slide (section 1). Hedge/commitment content for A3. Dates: R625-R651.

## 6. FOOTNOTES / QUALIFIERS (R652-R670, 19)
R652-R670 each referenced. Unresolved-footnote check: asterisk markers R653, R661, R665, R667 each pair to a footnote (R655, R662, R666, R668): none FOOTNOTE_UNRESOLVED.

## 7. MISSING_FROM_STRUCTURED (2, minor)
| new ID | page | line | claim text | flag |
|---|---|---|---|---|
| M1 | page 7 | line 163 | Sep-26 (order book chart axis label, pair of R637) | MISSING_FROM_STRUCTURED |
| M2 | page 20 | line 560 | 3-axis to 5-axis CNC capability | MISSING_FROM_STRUCTURED |
