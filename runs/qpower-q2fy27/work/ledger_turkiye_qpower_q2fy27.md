# A2 LEDGER: QPOWER Q2 FY27 Turkiye PCS commencement (presentation/one-off letter)
ids_in_structured: 28 | ids_referenced_in_ledger: 28 | orphan_ids: [] | match: yes
missing_from_structured: 2 (M01, M02, added in loop iteration 1)

=== A2 COUNT TEST ===
category: slides         grep_count: 1   sweep_count: 1   match: yes
category: slide_numbers  grep_count: 14  sweep_count: 14  match: yes (NUMBER 7 + DATE 7)
category: entities       grep_count: 12  sweep_count: 12  match: yes (11 + 1 summary)
category: forward        grep_count: 2   sweep_count: 2   match: yes
category: footnotes      grep_count: 0   sweep_count: 0   match: yes
category: total_ids      grep_count: 28  sweep_count: 28  match: yes
category: missing_from_structured  grep_count: 2  sweep_count: 2  match: yes (L41-43, L45a vs fulltext)
gate_a2: pass
=== END COUNT TEST ===

## Slides
S1 | page 1 | text letter, no chart/table/photo | covers R001-R028

## Numbers (ROW_ID | category | flags | note)
R001 | number-identifier | - | BSE scrip code
R002 | number-identifier | RESTATED | address, see R019
R003 | number-identifier | RESTATED | address, see R019
R004 | number-identifier | RESTATED | address, see R019
R005 | number-regulatory | RESTATED | same as R025
R006 | number-regulatory | - | Reg 30 cited; also R027
R007 | number-identifier | - | CS membership no.

## Entities
R008-R010 | exchange/symbol | - | addressees
R011 | entity-subsidiary | - | Endoks owns PCS facility; check against known consol list in A3
R012 | entity-location | - | text damaged in extraction
R013 | entity-facility | - | new facility, material
R014 | entity-product | - | converters, inverters
R015 | entity-application | - | utility-scale BESS
R016 | entity-order-book | NO_FIGURES_DISCLOSED | order book referenced, no size
R017 | entity-company | - | signatory company
R018 | entity-person | - | signatory CS
R019 | entity-summary | RESTATED | groups R002-R004 addresses

## Forward statements
R020 | forward | FORWARD_NO_DATES_OR_VOLUMES | ramp-up unquantified
R021 | forward | FORWARD_NO_DATES_OR_VOLUMES | demand/capability claim

## Dates
R022 | date | RESTATED | letter date, also R027
R023 | date | - | commencement 16-Oct-2026 (day before letter)
R024 | date | - | signature timestamp 17-Oct 15:30 IST
R025 | date | RESTATED | = R005
R026 | not-a-date | A1_NONDATE_IN_DATE_TABLE | signature label
R027 | date | RESTATED | = R022
R028 | not-a-date | A1_NONDATE_IN_DATE_TABLE | quarter tag

## MISSING_FROM_STRUCTURED (fulltext line numbers; A1 file unchanged)
M01 | line 41-43 | MISSING_FROM_STRUCTURED | "This development represents an important step in the Group's expansion into power electronics and energy storage technologies, complementing its established portfolio of high-voltage equipment and power quality solutions." | strategic-positioning claim: new segment beyond established portfolio; qualitative, no figures
M02 | line 45 (first clause) | MISSING_FROM_STRUCTURED | "The new facility strengthens the Group's manufacturing and system integration capabilities," | capability claim; remainder of L45-47 is R021

## Footnotes / qualifiers
none (A1 QUALIFIER 0; fulltext grep confirms only an extraction-tool note)

## ZERO_STANDING
none (no financial tables)
