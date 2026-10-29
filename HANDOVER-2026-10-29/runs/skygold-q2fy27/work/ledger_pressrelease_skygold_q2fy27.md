# LEDGER pressrelease SKYGOLD q2fy27 (A2)
ids_in_structured: 180 | ids_referenced_in_ledger: 180 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: structured_rows   grep_count: 180 (grep -c "^R[0-9]")  sweep_count: 180 (R001-R180 contiguous)  match: yes
category: counts_by_type    A1 header: NUMBER 131|ENTITY 22|FORWARD 1|DATE 17|QUALIFIER 9 = 180; A2 tally by type column: same  match: yes
category: line_items (table rows)  grep_count: 11 (fulltext lines 80-100)  sweep_count: 11 (88 cells R038-R125 = 11 x 8)  match: yes
category: notes/footnotes  grep_count: 1 ("Note:" line 102)  sweep_count: 1 (R126)  match: yes
category: fulltext numeric sweep (independent): headline/quote/bullet numeric tokens outside table: lines 18-62 cover R001-R023 numbers; quote 6 (R129-R134); bullets 26 (R136-R161); no unmatched token found  match: yes
category: agenda_items / auditor_paras / entities_consolidation: n/a (press release)
gate_a2: pass
=== END COUNT TEST ===

## Ledger (ROW_ID | category | flags | note)
R001 | cover letter date | - | -
R002-R011 | exchange addressee/codes/addresses | - | -
R012-R013 | results period / unaudited qualifier | - | release says consolidated unaudited
R014-R015 | headline | RESTATED | = R025-R026; revenue 4,403.45 vs table 4,403.5 (R043) rounding
R016-R017 | periods | RESTATED | = R024
R018 | website | RESTATED | = R177
R019-R023 | signature block | - | signature timestamp 27-Oct 20:32 IST; no board-time in doc
R024-R037 | release header, basis, units | - | -
R038-R045 | line item Revenue (8 cells) | - | R038=R132=R136; R043=R129=R138
R046-R053 | line item EBITDA | - | R046=R133=R140; R051=R130=R142
R054-R061 | line item EBITDA margin | - | R054=R144; R059=R146
R062-R069 | line item Reported PBT | - | -
R070-R077 | line item Reported PBT % | - | -
R078-R085 | line item Reported PAT | - | R078=R134=R148; R083=R131=R150
R086-R093 | line item PAT margin | - | R086=R152; R091=R154
R094-R101 | line item Operational PBT | - | Op PBT 173.4 > reported 166.0
R102-R109 | line item Operational PBT % | - | -
R110-R117 | line item Operational PAT | - | Op PAT H1 234.5 vs reported 234.3
R118-R125 | line item Operational PAT % | - | -
R126 | note (Operational PAT/PBT definition) | - | non-operational income excluded; gap Q2 = 7.4 PBT
R127-R135 | MD quote | RESTATED | numbers duplicate table
R136-R155 | highlight bullets: revenue, EBITDA, margin, PAT, PAT margin | RESTATED | duplicates of table cells
R156-R159 | CFO bullet | FOOTNOTE_UNRESOLVED | prior CFO (100.9) labelled "H1 FY27" same as current, per R169; no CFO table in release
R160-R161 | Purvi acquisition numbers | - | Rs 9 crore for 100%
R162 | founding year | RESTATED | = R168
R163-R168 | periods/dates | - | R167 Oct 7 2026 board approval
R169-R170 | qualifiers (CFO label, guidance compare) | FOOTNOTE_UNRESOLVED | -
R171 | forward/prior guidance 20% CFO/EBITDA | - | only forward-type item; no new guidance
R172-R173 | Purvi entity, Board | ENTITY_CHANGE | new acquisition, closed; not in prior ledger (none available)
R174 | acquisition terms | - | -
R175-R180 | About, PR advisor, contacts | - | -

Zero/nil/dash standing items: none in doc (ZERO_STANDING count 0).
