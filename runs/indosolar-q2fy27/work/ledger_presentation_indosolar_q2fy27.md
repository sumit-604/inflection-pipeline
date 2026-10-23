# A2 LEDGER: INDOSOLAR Q2 FY27 (presentation doctype, 3-page press release dated 21-Oct-2026)
Source: extracted/indosolar-presentation-q2fy27-structured.md (R001-R084). Prior ledger: none (no DROPPED_SLIDE diff possible).

=== A2 COUNT TEST ===
category: slides (pages)    grep_count: 3    sweep_count: 3    match: yes
category: slide_numbers     grep_count: 41   sweep_count: 41   match: yes
category: entities          grep_count: 19   sweep_count: 19   match: yes (incl 2 ENTITY-SUMMARY)
category: forward           grep_count: 7    sweep_count: 7    match: yes
category: dates             grep_count: 10   sweep_count: 10   match: yes
category: qualifiers/footnotes grep_count: 7 sweep_count: 7    match: yes
category: zero_standing     grep_count: 0    sweep_count: 0    match: yes (no nil/dash rows in A1)
category: notes/agenda/auditor/turns/questions: not applicable to doctype
total IDs: grep 84, sweep 84 (41+19+7+10+7)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 84 | ids_referenced_in_ledger: 84 | orphan_ids: [] | match: yes

## 1. SLIDES (pages; content type)
PAGE | content type | IDs on page
1 | text (exchange letter, signature block) | R001, R042-R050, R059, R068-R071, R078, R083
2 | text + table (Q2/H1 financial table) + bullets | R002-R040, R051-R053, R061-R066, R072-R077, R079-R082
3 | text (plant profile, parent profile, IR contacts, disclaimer) | R041, R054-R058, R060, R067, R084
DROPPED_SLIDE: none assessable (no prior ledger).

## 2. NUMBERS (ROW_ID | category | flags | cross-ref / note)
R001 | number | RESTATED | = R042 (BSE scrip code)
R002 | number | RESTATED | headline revenue = R005 = R031
R003 | number | RESTATED | headline EBITDA = R011 = R033
R004 | number | RESTATED | headline PAT = R021 = R035
R005 | number/table | RESTATED | = R002, R031
R006 | number/table | RESTATED | = R032
R007 | number/table | - | YoY revenue Q2
R008 | number/table | - | H1 revenue
R009 | number/table | - | H1 FY26 revenue
R010 | number/table | - | YoY revenue H1
R011 | number/table | RESTATED | = R003, R033
R012 | number/table | RESTATED | = R034
R013 | number/table | - | YoY EBITDA Q2
R014 | number/table | - | H1 EBITDA
R015 | number/table | - | H1 FY26 EBITDA
R016 | number/table | - | YoY EBITDA H1
R017 | number/table | - | EBITDA margin Q2 FY27, no YoY cell (R082)
R018 | number/table | - | EBITDA margin Q2 FY26
R019 | number/table | - | EBITDA margin H1 FY27
R020 | number/table | - | EBITDA margin H1 FY26
R021 | number/table | RESTATED | = R004, R035
R022 | number/table | RESTATED | = R036
R023 | number/table | - | YoY PAT Q2
R024 | number/table | - | H1 PAT
R025 | number/table | - | H1 FY26 PAT
R026 | number/table | - | YoY PAT H1
R027 | number/table | - | PAT margin Q2 FY27, no YoY cell (R082)
R028 | number/table | - | PAT margin Q2 FY26
R029 | number/table | - | PAT margin H1 FY27
R030 | number/table | - | PAT margin H1 FY26
R031 | number/bullet | RESTATED | = R002, R005
R032 | number/bullet | RESTATED | = R006
R033 | number/bullet | RESTATED | = R003, R011
R034 | number/bullet | RESTATED | = R012
R035 | number/bullet | RESTATED | = R004, R021
R036 | number/bullet | RESTATED | = R022
R037 | number/volume | - | module production 148 MW vs R038 244 MW; material: only operating volume metric
R038 | number/volume | - | pair with R037
R039 | number/volume | - | module sold 98 MW vs R040 249 MW; sold < produced in Q2FY27 (148 vs 98), inventory/tolling question for A3
R040 | number/volume | - | pair with R039
R041 | number/capacity | - | 1.3 GW Noida capacity; = R054; no utilisation figure given (R037 is only proxy)

## 3. ENTITIES
R042 | entity | RESTATED | exchange addressee BSE; = R001
R043 | entity | - | NSE symbol WAAREEINDO
R044 | entity | - | ISIN
R045 | entity | - | SEBI LODR Reg 30
R046 | entity | - | filer
R047 | entity | - | signatory; = R083
R048 | entity | - | website
R049 | entity | - | CIN
R050 | entity | - | parent-group tag; relates R055
R051 | entity | - | CEO quoted
R052 | entity | RESTATED | Waaree Energies counterparty; = R065, R055; ENTITY_CHANGE candidate (pending amalgamation)
R053 | entity | - | tolling vs owned manufacturing mix (not a legal entity); = R061
R054 | entity | RESTATED | plant; = R041
R055 | entity | RESTATED | parent; = R050, R052
R056 | entity | - | IR contact
R057 | entity | - | IR contact
R058 | entity | - | IR email
R059 | entity-summary | - | address blocks group (page 1)
R060 | entity-summary | - | safe-harbour disclaimer group (page 3)

## 4. FORWARD-LOOKING
R061 | forward | RESTATED | tolling to owned transition; = R053; no volume or date quantified
R062 | forward | - | near-term challenges; no guidance number
R063 | forward | - | management intent
R064 | forward | - | management intent
R065 | forward | RESTATED | amalgamation; no date or terms (per A1); = R052
R066 | forward | - | synergy expectation, unquantified
R067 | forward | - | boilerplate FLS notice; = R060
No numeric guidance row exists in the document.

## 5. DATES
R068 | date | - | letter date 21-Oct-2026
R069 | date | - | results period 30-Sep-2026
R070 | date | - | not a true date (regulation year); kept for ID accounting
R071 | date | RESTATED | signature timestamp 20:40:15 IST; = R083; no board meeting times in document so timestamp-vs-meeting check not possible
R072 | date | - | press release date, Mumbai
R073 | date | - | period label
R074 | date | - | period label
R075 | date | - | period label
R076 | date | - | period label
R077 | date | - | period label (bullets)

## 6. QUALIFIERS / FOOTNOTES
R078 | qualifier | - | standalone, unaudited
R079 | qualifier | - | unit label Rs Crores
R080 | qualifier | - | A1 extraction repair of table; cells verified by A1
R081 | qualifier | FOOTNOTE_UNRESOLVED | 'Operating EBITDA' undefined; qualifies headline R003/R011
R082 | qualifier | - | blank YoY cells for margin rows (R017-R020, R027-R030)
R083 | qualifier | RESTATED | signature; = R071, R047
R084 | qualifier | - | not-a-recommendation restriction

## 7. ZERO_STANDING
None. A1 reports no zero, nil or dash values. Blank YoY margin cells (R082) are not zero rows.

## 8. MISSING_FROM_STRUCTURED
None. Fulltext grep for footnote markers returned nothing further.
