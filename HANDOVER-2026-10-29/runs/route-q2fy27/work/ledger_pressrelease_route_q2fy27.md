# LEDGER: Route Mobile (ROUTE) Q2FY27 press release (investor-presentation discipline; 3 pages = 3 slide-equivalents)
Source: A1 structured R001-R074. Rows referenced by ID only; verbatim values live in the structured file.
Prior ledger (Q1FY27, older format): 3 slides, 33 numbers, 9 fwd-looking, 1 footnote. Slide-level DROPPED_SLIDE: none (3 of 3 present). Q2 fwd count 5 vs Q1 9: fewer forward statements (not a slide drop).

ids_in_structured: 74 | ids_referenced_in_ledger: 74 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: slides             grep_count: 3   sweep_count: 3   match: yes   (grep ^[page N])
category: slide_numbers      grep_count: 41  sweep_count: 41  match: yes   (grep "| NUMBER |"; p1 8, p2 26, p3 7)
category: notes_numbered     grep_count: 0   sweep_count: 0   match: yes   (grep "^\s*[0-9]+\.\s" on fulltext)
category: footnotes_qualif   grep_count: 4   sweep_count: 4   match: yes   (R071-R074; no asterisk/Note: lines)
category: fwd_statements     grep_count: 5   sweep_count: 5   match: yes
category: entities           grep_count: 14  sweep_count: 14  match: yes   (13 ENTITY + R054 ENTITY-SUMMARY; A1 header says 13)
category: dates              grep_count: 11  sweep_count: 11  match: yes
category: zero_standing      grep_count: 0   sweep_count: 0   match: yes   (no nil/dash rows)
gate_a2: pass
=== END COUNT TEST ===
```

## T1 Slides
| Slide | Page | Content | IDs on slide | Flags |
|---|---|---|---|---|
| 1 | p1 | text: Reg 30 cover letter, signature | R001-R003,R029,R033-R036,R042-R044,R053,R060,R069 | - |
| 2 | p2 | text: headline, YoY, QoQ, mgmt quotes, About RML | R004-R023,R030-R032,R038-R040,R045-R048,R055-R059,R061-R064,R066-R068,R070-R074 | - |
| 3 | p3 | text: About Proximus Global, contact | R024-R028,R037,R041,R049-R052,R054,R065 | - |

## T2 Numbers (R001-R041)
ROW_ID | category | flags | cross-ref / note
R001 | identifier | - | filing ref
R002 | identifier | RESTATED | = R037
R003 | identifier | - | CS membership
R004 | financial | RESTATED | = R006, R016 (revenue Q2FY27)
R005 | financial | RESTATED | = R012, R021 (PAT Q2FY27)
R006 | financial | RESTATED | = R004, R016
R007 | financial | - | Q2FY26 revenue base, YoY
R008 | financial | RESTATED | PBT pre-exceptional Q2FY27; = R010 (equal), R018
R009 | financial | - | Q2FY26 pre-exceptional PBT 137.87 vs R011 PBT 2.00: large Q2FY26 exceptional gap, not explained in release
R010 | financial | RESTATED | = R008, R018; PBT = pre-exceptional PBT, so no Q2FY27 exceptional item shown
R011 | financial | - | see R009
R012 | financial | RESTATED | = R005, R021
R013 | financial | - | Q2FY26 PAT loss; YoY swing from loss
R014 | financial | RESTATED | EPS basic = R015 (equal), R074
R015 | financial | RESTATED | = R014
R016 | financial | RESTATED | = R004, R006
R017 | financial | - | Q1FY27 revenue, QoQ base
R018 | financial | RESTATED | = R008, R010
R019 | financial | - | Q1FY27 PBT
R020 | financial | - | PBT margin; only margin disclosed; no EBITDA/GM/segment figures anywhere
R021 | financial | RESTATED | = R005, R012
R022 | financial | - | Q1FY27 PAT
R023 | date-as-number | RESTATED | = R064
R024 | boilerplate | RESTATED | = R065
R025 | boilerplate | - | Proximus Global stat
R026 | boilerplate | - | Proximus Global stat
R027 | boilerplate | - | Proximus Global stat
R028 | contact | RESTATED | within R054
R029 | date | RESTATED | = R060
R030 | date | RESTATED | = R061; dateline Oct 27 vs filing Oct 28
R031 | period label | RESTATED | = R068
R032 | period label | RESTATED | = R068
R033 | period label | RESTATED | = R068
R034 | regulatory | - | with R035, R053
R035 | regulatory | - | year of LODR
R036 | signature | RESTATED | = R069; timestamp 00:03:52 on Oct 28, after Oct 27 dateline (no board time in release to test)
R037 | identifier | RESTATED | = R002
R038 | period label | RESTATED | = R066
R039 | period label | RESTATED | = R067
R040 | period label | - | revenue-in-line-with-guidance claim; no guidance number given anywhere in release (materiality)
R041 | contact | RESTATED | within R054

## T3 Footnotes / qualifiers (no numbered notes)
R071 | qualifier | - | PBT pre-exceptional basis, see R009/R011
R072 | qualifier | - | PAT reported
R073 | qualifier | - | consolidated basis
R074 | qualifier | RESTATED | EPS basis; A1 confirms no footnotes in doc

## T4 Forward statements
R055 | fwd | - | Heltar portfolio expansion, qualitative
R056 | fwd | - | priorities; no numbers
R057 | fwd | - | "encouraging pipeline", unquantified; pairs R058
R058 | fwd | - | conversion intent, no timeline
R059 | fwd | - | strategy, no metrics

## T5 Entities / signatories / contacts
R042,R043 | addressee | - |
R044 | signatory | - | CS Tejas Shah
R045 | parent | - | Proximus Global
R046 | mgmt | - | Seckin Arikan, Chairman
R047 | mgmt | - | Tushar Agnihotri CEO
R048 | acquired | ENTITY_CHANGE | Heltar new vs Q1 consolidation; acquisition completion date year not stated (R064)
R049 | parent group | - |
R050,R051,R052 | peers | - | Telesign, BICS, Route Mobile
R053 | regulator | - |
R054 | contact | - | media contact (R028, R041)

## T6 Dates
R060 | filing | RESTATED | = R029
R061 | dateline | RESTATED | = R030
R062 | period end | - |
R063 | period end | RESTATED | = R062
R064 | Heltar completion | RESTATED | = R023; year missing
R065 | founding | RESTATED | = R024
R066 | comparison | RESTATED | = R038
R067 | comparison | RESTATED | = R039
R068 | current period | RESTATED | = R031
R069 | signature | RESTATED | = R036
R070 | "first-half performance" | - | ligature-dropped; H1 referenced but no H1 figures given (materiality)

## Missing from structured
none
