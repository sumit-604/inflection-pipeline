# A2 LEDGER: QPOWER EGM outcome 19-Oct-2026 (Q2 FY27), doctype presentation/egm
ID ACCOUNTABILITY: ids_in_structured: 68 | ids_referenced_in_ledger: 68 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: structured_ids   grep_count: 68  sweep_count: 68 (24+24+5+12+3)  match: yes
category: number_rows      grep_count: 24  sweep_count: 24  match: yes
category: entity_rows      grep_count: 24  sweep_count: 24  match: yes
category: forward_rows     grep_count: 5   sweep_count: 5   match: yes
category: date_rows        grep_count: 12  sweep_count: 12  match: yes
category: qualifier_rows   grep_count: 3   sweep_count: 3   match: yes
category: agenda_items     grep_count: 3 (resolutions, fulltext 136-144)  sweep_count: 3  match: yes
category: notes (unnumbered, A1 foot) grep_count: 2  sweep_count: 2  match: yes
category: line_items / auditor_paras / consolidation entities / turns / slides: n/a (0)
anchor_check (fulltext, 170 lines): 3 wrong anchors, 4 imprecise (below)
gate_a2: pass
=== END COUNT TEST ===

## ANCHOR CORRECTIONS (A1 line numbers vs fulltext; ID kept, line fixed here)
| ROW | A1 line | fulltext line | note |
| R025 | 25-27 | 20 (BSE addressee) | A1 range wrong |
| R045 | 140 | 151-153 (website list) | A1 line wrong |
| R046 | 133 | 113-118 (statute refs) | A1 line wrong |
| R062 | 117 | 113-118 | imprecise |
| R021 | 135-143 | 136-144 | imprecise |
| R047 | 141-143 | 142-144 | imprecise |
| R028 | 46 | 45-46 | imprecise |
| R065 | 31 | none (task-derived period label, not in document) | not a document unit |

## 1 NUMBERS (R001-R024)
| ROW | category | flags | note |
| R001-R002 | identifiers | | |
| R003, R005, R006, R063 | meeting time | RESTATED (3,5,6,63) | start 4.00pm; end 4.40pm = 40 min meeting |
| R007, R024, R064 | e-voting 15 min post-meeting | RESTATED | |
| R008 | members attended (35) | | low attendance |
| R009, R010 | directors present 8; attendees 7 | | table layout broken (stray "Independent Director" fulltext line 67; designations misaligned lines 59-78) |
| R011, R050 | QIP up to 700 crore | RESTATED | |
| R012, R013, R014, R051 | bridge loan 175 cr, 9%, "11 years" | RESTATED | promoter related party; tenor wording "interest for 11 years" |
| R015-R018 | statutory refs | | |
| R019, R020, R058, R059 | e-voting window | RESTATED | |
| R021 | 3 resolutions | | see agenda |
| R022, R052, R061 | results within 48h | RESTATED | no voting results in document |
| R004, R023 | CS membership no.; PIN | | |

## 2 AGENDA ITEMS (3) 
| item | ROW | flags | note |
| Res 1: preferential issue to Winwin selling shareholders (share swap) | R021, R048, R041 | FOOTNOTE_UNRESOLVED | type Special/Special/Ordinary mapping ambiguous (fulltext 136-139) |
| Res 2: QIP | R021, R011, R050 | FOOTNOTE_UNRESOLVED | same |
| Res 3: RPT with Promoters/Promoter Group | R021, R047, R012-R014, R051 | FOOTNOTE_UNRESOLVED | RPT includes promoter bridge loan by inference of A1 only |
Voting results: NOT IN DOCUMENT (flag NO_VOTING_RESULTS).

## 3 ENTITIES (R025-R048, 24)
| R025-R027 filer/exchanges | | |
| R028, R029 CS, Sangli | | name spelling variants Suryavanshi/Suryanshi |
| R030-R037 directors (8) | | R030 CMD; R031 Joint MD (p4) but designation blank in p2 table; R032 Joint MD; R033-R034 WTD; R035-R037 ID. MGMT_ABSENCE: none, CMD present |
| R038-R040 attendees | | CFO Rajesh Jayaraman (spelled Jeyaraman line 98) |
| R041 Winwin Speciality Insulators | ENTITY_CHANGE (proposed acquisition target) | |
| R042, R043, R044, R045, R046, R047, R048 | | R047 promoter group counterparty; R048 allottees |

## 4 FORWARD (R049-R053) | 5 DATE (R054-R065) | 6 QUALIFIER (R066-R068)
| R049-R053 | FORWARD | acquisition, QIP use of proceeds, bridge loan, results declaration, "expected benefits" (no detail in doc) |
| R054-R065 | DATE | R056/R060 signature 19:34 after 16:40 conclusion, no sequencing flag; R065 not document text |
| R066-R068 | QUALIFIER | |

## 7 MISSING_FROM_STRUCTURED
| M1 | fulltext 90 | MISSING_FROM_STRUCTURED | "requisite quorum was present"; no quorum count stated |
| M2 | fulltext 33 | MISSING_FROM_STRUCTURED | filed under Regulation 30 SEBI LODR |
| M3 | fulltext 145-147 | MISSING_FROM_STRUCTURED | shareholder Q&A held; queries answered by Mr Bharanidharan Pandyan, Joint MD; no questions recorded |
| M4 | fulltext 150-152 | MISSING_FROM_STRUCTURED | registered office Plot No L-61, MIDC, Kupwad Block, Sangli; company website www.qualitypower.com |
| M5 | fulltext 95-98 | MISSING_FROM_STRUCTURED | Chairman briefed on "promoter financing arrangements" (plural); only partly in R051 |
