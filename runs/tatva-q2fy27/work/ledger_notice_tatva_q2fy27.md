=== A2 COUNT TEST ===
category: numbers      grep_count: 7  sweep_count: 7  match: yes
category: entities     grep_count: 8  sweep_count: 8  match: yes
category: forward      grep_count: 2  sweep_count: 2  match: yes
category: dates        grep_count: 7  sweep_count: 7  match: yes
category: qualifiers   grep_count: 4  sweep_count: 4  match: yes
category: total_ids    grep_count: 28 sweep_count: 28 match: yes
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 28 | ids_referenced_in_ledger: 28 | orphan_ids: [] | match: yes
Doctype note: one-page Reg 30 notice. No notes, line items, agenda items, auditor paras, turns or slides apply (0).
A1 anchor correction: R014 (TATVA symbol) is on fulltext line 26, not 27 (confirmed by grep; line 27 is the scrip code R003). Corrected here; A1 file not edited.

## Numbers
ROW_ID | category | A2 flags | cross-ref / materiality
R001 | number | RESTATED | letter date; same as R018
R002 | number | - | reference number
R003 | number | - | BSE scrip code, line 27
R004 | number | RESTATED | earlier intimation date; same as R019
R005 | number | RESTATED | call time; part of R020
R006 | number | - | CS membership number
R007 | number | RESTATED | signature timestamp; same as R024; 16:03 IST is ~57 min before the 17:00 call time (R005), so cancellation was same-day, short notice
## Entities
R008 | entity | - | issuer
R009 | entity | - | addressee
R010 | entity | - | addressee
R011 | entity | - | Reg 30 basis; see R026
R012 | entity | SAME_PERSON_R013 | signatory
R013 | entity | SAME_PERSON_R012 | digital signature name
R014 | entity | ANCHOR_CORRECTED | line 26 (A1 said 27)
R015 | entity | - | website; see R016
## Forward
R016 | forward | - | promised website publication; vague, no date or content named
R017 | forward | NO_NEW_DATE | call cancelled, no reschedule; see R025, R020
## Dates
R018 | date | RESTATED | = R001
R019 | date | RESTATED | = R004
R020 | date | - | cancelled call slot; contains R005
R021 | date | - | quarter-end period
R022 | date | - | half-year period; same date as R021
R023 | date | NON_DATE_FRAGMENT | year inside regulation name, not a disclosure date
R024 | date | RESTATED | = R007
## Qualifiers
R025 | qualifier | REASON_UNSPECIFIED | "unforeseen circumstances", no cause named; see R017
R026 | qualifier | - | boilerplate, with R011
R027 | qualifier | - | call was tied to results announcement
R028 | qualifier | - | signature note; with R013

```yaml
stage: A2-enumerator
company: "TATVA"
quarter: "Q2 FY27"
doctype: "presentation (notice)"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/tatva-q2fy27/work/ledger_notice_tatva_q2fy27.md"
counts:
  notes: 0
  line_items: 0
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 8
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [RESTATED, SAME_PERSON, ANCHOR_CORRECTED, NO_NEW_DATE, REASON_UNSPECIFIED, NON_DATE_FRAGMENT]
ids_in_structured: 28
ids_referenced: 28
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Call cancelled for unspecified reasons with no new date. Signature timestamp 16:03 IST is about an hour before the 17:00 call. R014 anchor corrected to line 26."
```
