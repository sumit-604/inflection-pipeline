# A2 LEDGER: INDORAMA Capex Board Outcome, Q2 FY27 (Reg 30, 16-Oct-2026)
ids_in_structured: 47 | ids_referenced_in_ledger: 47 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 0   sweep_count: 0   match: yes (no numbered notes or footnotes)
category: line_items     grep_count: 0   sweep_count: 0   match: yes (no financial table)
category: agenda_items   grep_count: 1   sweep_count: 1   match: yes (capex approval only)
category: auditor_paras  grep_count: 0   sweep_count: 0   match: yes
category: entities       grep_count: 12  sweep_count: 12  match: yes (R018-R029)
category: signatures     grep_count: 1   sweep_count: 1   match: yes
category: all_ids        grep_count: 47  sweep_count: 47  match: yes
gate_a2: pass
=== END COUNT TEST ===

## Agenda items (Board Outcome)
A01 | capex approval, approx INR 200 Cr, Company + IVYPL, Butibori | R011,R022,R023,R027,R030,R031,R042,R044 | flags: SPLIT_NOT_STATED (Company vs IVYPL) | material
A01a timeline | R012,R032,R040,R043 | 12-18 months, estimated
A01b financing | R033,R034,R046 | term loan plus internal accrual, split not quantified: FUNDING_UNQUANTIFIED
Meeting start/end times: NOT STATED in filing (grep of fulltext line 38 shows only "held today"). Flag MEETING_TIMES_ABSENT.
No other agenda items (no results, dividend, AR, AGM, directors, auditor, ESOP, fundraising).

## Entities (R018-R029)
R018,R019,R020,R021,R022,R023,R024,R025,R026,R027,R028,R029 | no prior list (ND); ENTITY_CHANGE not testable. IVYPL (R023) is the only operating entity beyond filer.
Capex product lines R025,R026: speciality filament, speciality Fibre.

## Signature block
R028,R014,R039,R047,R013 | Ashok Yadav, CS, ACS 14223; signed 2026.10.16 14:51:58 +05'30'. No meeting end time to compare, so the timestamp-before-conclusion test is unresolved.

## Remaining rows (reference/boilerplate, grouped)
Reference/addressing: R001,R002,R003,R004,R005,R006,R007,R008,R020,R035 | letter ref and exchange details
Dates: R036,R037,R038,R041,R009,R010,R045 | letter date, meeting date, LODR basis
Address/CIN: R015,R016,R017,R029
Forward statements: R030-R034 (see A01)
Qualifiers: R042-R047 (see A01)
Coverage check: R001-R047 all placed above.
