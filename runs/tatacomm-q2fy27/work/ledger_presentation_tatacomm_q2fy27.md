# A2 LEDGER: TATACOMM presentation q2fy27
ids_in_structured: 74 | ids_referenced_in_ledger: 74 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides         grep_count: 9   sweep_count: 9   match: yes   (fulltext [page N] markers = 9 = pdfinfo page_count)
category: slide_numbers  grep_count: 33  sweep_count: 33  match: yes   (NUMBER rows R001-R033; header says 33)
category: entities       grep_count: 25  sweep_count: 25  match: yes   (R034-R058)
category: forward        grep_count: 3   sweep_count: 3   match: yes   (R059-R061)
category: dates          grep_count: 7   sweep_count: 7   match: yes   (R062-R068)
category: footnotes_qualifiers grep_count: 6 sweep_count: 6 match: yes (R069-R074)
category: zero_standing  grep_count: 0   sweep_count: 0   match: yes
category: dropped_slides grep_count: 0   sweep_count: 0   match: yes (prior deck ND; cannot test)
total_ids                grep_count: 74  sweep_count: 74  match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (page | title | type | IDs on slide)
Slide | title | content type | A2 flags | structured IDs
1 | Cover letter to exchanges (Attachment A) | text | none | R001-R010, R029-R031, R034-R039, R062-R065, R068, R073
2 | Q2FY27 title slide | text | none | R028, R066
3 | SAFE HARBOUR | text | none | R057, R069-R071, R074
4 | Customer reach and leadership team | text/org chart | none | R011-R015, R040-R052, R058
5 | PLAN ON PAGE | chart/diagram | none | R026, R027, R053, R059, R060
6 | DIGITAL PORFOLIO ON THE PATH TO BREAKEVEN (title typo verbatim) | chart | none | R016-R020, R061, R067, R072
7 | THE UNIFIED AI STACK | text/diagram | none | R032, R054
8 | CUSTOMER OUTCOMES DELIVERED | text/photo | none | R021-R025, R033, R055, R056
9 | Thank you / #togetherlimitless | text | NO_UNITS (no structured rows; closing slide) | none

## 2. SLIDE NUMBERS (ROW_ID | category | flags | note)
R001 | NUMBER | - | boilerplate/administrative or deck metric
R002 | NUMBER | - | boilerplate/administrative or deck metric
R003 | NUMBER | - | boilerplate/administrative or deck metric
R004 | NUMBER | - | boilerplate/administrative or deck metric
R005 | NUMBER | - | boilerplate/administrative or deck metric
R006 | NUMBER | - | BSE pincode; also appears in registered office line
R007 | NUMBER | - | boilerplate/administrative or deck metric
R008 | NUMBER | - | boilerplate/administrative or deck metric
R009 | NUMBER | - | boilerplate/administrative or deck metric
R010 | NUMBER | - | boilerplate/administrative or deck metric
R011 | NUMBER | - | 70% FS traffic share; no base period or source
R012 | NUMBER | - | restated with denominator R014/R015; 300/500 and 380/500
R013 | NUMBER | - | restated with denominator R014/R015; 300/500 and 380/500
R014 | NUMBER | - | denominator for R012/R013
R015 | NUMBER | - | denominator for R012/R013
R016 | NUMBER | RESTATED | pair with R017 (same bar); -3.6% Q2FY27
R017 | NUMBER | RESTATED | pair with R016
R018 | NUMBER | CHART_LABEL_UNPAIRED | Q1FY27 margin %; no rupee value in structured file for Q1FY27 bar (check p6 chart)
R019 | NUMBER | RESTATED | FY25 bar, % and INR pair; comparison base for breakeven path
R020 | NUMBER | RESTATED | FY25 bar, % and INR pair; comparison base for breakeven path
R021 | NUMBER | - | boilerplate/administrative or deck metric
R022 | NUMBER | - | boilerplate/administrative or deck metric
R023 | NUMBER | - | boilerplate/administrative or deck metric
R024 | NUMBER | - | boilerplate/administrative or deck metric
R025 | NUMBER | - | insurer single contract; qualitative count
R026 | NUMBER | COUNT_DISCREPANCY | WHAT? levers count 6; R060 names 5 levers (see note below)
R027 | NUMBER | - | boilerplate/administrative or deck metric
R028 | NUMBER | RESTATED | same as R066
R029 | NUMBER | RESTATED | same year as R068
R030 | NUMBER | - | boilerplate/administrative or deck metric
R031 | NUMBER | RESTATED | year inside CIN R009
R032 | NUMBER | - | boilerplate/administrative or deck metric
R033 | NUMBER | - | boilerplate/administrative or deck metric

## 3. ENTITIES (R034-R058)
R034 | ENTITY | - | 
R035 | ENTITY | - | 
R036 | ENTITY | - | 
R037 | ENTITY | - | 
R038 | ENTITY | - | 
R039 | ENTITY | - | 
R040 | ENTITY | - | cohort reference; tied to R012/R013
R041 | ENTITY | - | cohort reference; tied to R012/R013
R042 | ENTITY | - | 
R043 | ENTITY | - | 
R044 | ENTITY | - | 
R045 | ENTITY | - | 
R046 | ENTITY | - | 
R047 | ENTITY | - | 
R048 | ENTITY | - | 
R049 | ENTITY | - | 
R050 | ENTITY | - | 
R051 | ENTITY | - | 
R052 | ENTITY | - | MD and CEO; sole CEO row on leadership slide
R053 | ENTITY | - | 
R054 | ENTITY | - | 
R055 | ENTITY | ANONYMISED_CLIENT | unnamed customer; ANONYMISED_CLIENT
R056 | ENTITY | ANONYMISED_CLIENT | unnamed customer; ANONYMISED_CLIENT
R057 | ENTITY | - | risk-factor pointer to annual reports
R058 | ENTITY | - | org unit group; no consolidation list on this doctype (ENTITY_CHANGE not testable; prior ND)

## 4. FORWARD-LOOKING (R059-R061)
R059 | FORWARD | - | plan objective, no number or date
R060 | FORWARD | - | five levers named; R026 says 6; unquantified
R061 | FORWARD | - | breakeven path headline; no breakeven date given; ties to R016-R020

## 5. DATES (R062-R068)
R062 | DATE | - | letter date 15 Oct 2026
R063 | DATE | - | earlier letter 14 Oct 2026; relates to R003
R064 | DATE | - | call 15 Oct 2026 4:00 pm; ties R004
R065 | DATE | RESTATED | signature 14:14:50 (R010) on 2026.10.15; precedes 4 pm call
R066 | DATE | RESTATED | same as R028
R067 | DATE | - | periods Q2FY27, Q1FY27, FY25 for p6 bars
R068 | DATE | RESTATED | same as R029

## 6. FOOTNOTES / QUALIFIERS (R069-R074)
R069 | QUALIFIER | - | safe harbour risk statement
R070 | QUALIFIER | - | actuals may differ materially
R071 | QUALIFIER | - | no obligation to update
R072 | QUALIFIER | - | FY25 label defines R019/R020 bar; qualifies headline breakeven path R061
R073 | QUALIFIER | - | enclosure note
R074 | QUALIFIER | - | group summary for p3 lines 70-83 (groups R069-R071)

## 7. ZERO_STANDING: none (no nil/dash line items in deck)
## 8. DROPPED_SLIDE: not testable (prior ledger ND)
## 9. MISSING_FROM_STRUCTURED: none
