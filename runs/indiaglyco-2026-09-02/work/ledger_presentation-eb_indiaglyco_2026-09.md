=== A2 COMPLETENESS LEDGER ===
company: India Glycols Limited (INDIAGLYCO) — Ennature Biopharma (EB)
quarter: 2026-09
doctype: presentation
source: A1 structured extraction, runs/indiaglyco-2026-09-02/extracted/indiaglyco-presentation-eb-2026-09-structured.md (R001-R152)
prior_quarter_ledger: none supplied — DROPPED_SLIDE comparison not performable this run

=== A2 COUNT TEST ===
category: pages(document)   grep_count: 15   sweep_count: 15   match: yes
category: numbers           grep_count: 52   sweep_count: 52   match: yes
category: entities          grep_count: 53   sweep_count: 53   match: yes
category: forward_statements grep_count: 26  sweep_count: 26   match: yes
category: dates             grep_count: 10   sweep_count: 10   match: yes
category: footnotes/qualifiers grep_count: 11 sweep_count: 11  match: yes
category: zero_standing     grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===

Method: grep_count = `grep -c "| NUMBER |"` etc. on the structured file per row-type
tag, cross-checked against header row_counts. sweep_count = manual page-by-page
walk assigning every R001-R152 ID to its page/slide (see Table 0 below), tallied
per category. Both methods independently produced identical totals; no fulltext
grep was needed to resolve any count (GATE A2 satisfied from structured file alone).

## TABLE 0: DOCUMENT/SLIDE INVENTORY (page-by-page, all 15 pages)

Page 1 is the SEBI Reg.30 intimation letter (cover wrapper) to BSE/NSE; pages
2-15 are the 14 deck slides of the Ennature Biopharma investor presentation.
Titles shown are the slide-subject text A1 captured as an ENTITY row; pages
with no captured subject row are marked NOT CAPTURED (not backfilled from
fulltext — out of scope per input discipline).

| Unit | Title (from captured slide-subject ENTITY row, else NOT CAPTURED) | Content type (A2 inferred) | IDs on this unit | A2 flags |
|---|---|---|---|---|
| p1 (cover letter, not a deck slide) | "Intimation under Reg.30 — Investor Presentation" | text (regulatory letter + digital signature block) | R001-R004, R053-R061, R132-R136 | — |
| Slide 1 (p2) | NOT CAPTURED (title page: "Ennature Biopharma") | text (title/cover) | R062, R063, R137 | — |
| Slide 2 (p3) | NOT CAPTURED (health & wellness demand stats) | text+data (stat blocks, 4 footnotes) | R005-R016, R142-R146 | — |
| Slide 3 (p4) | NOT CAPTURED (market size / target categories) | text+data | R017, R018, R064, R147 | — |
| Slide 4 (p5) | NOT CAPTURED (journey/demerger timeline) | diagram (timeline, 4 periods) | R065, R066, R106, R138-R141 | — |
| Slide 5 (p6) | NOT CAPTURED (3-segment overview) | text+data (segment mix %) | R019-R021, R067-R072 | — |
| Slide 6 (p7) | "Established API Franchise" (R073) | text+data (KPI blocks + strategy) | R022-R028, R073-R080, R107-R109, R148 | — |
| Slide 7 (p8) | "Diversified Biopolymer (Guar) Platform" (R081) | text+data (KPI blocks + strategy) | R029-R031, R081, R082, R110-R112, R149 | — |
| Slide 8 (p9) | "Scaling Branded Nutraceutical Ingredients" (R083) | text+data (KPI blocks + product roster + strategy) | R032-R036, R083-R090, R113-R116, R150 | — |
| Slide 9 (p10) | "Well Positioned to Capture the Shift Towards High Value Nutraceutical Ingredients" (R091) | text (moat pillars) | R091-R094, R117 | — |
| Slide 10 (p11) | "Creating Defensibility Through Intellectual Property and Clinical Evidence" (R095) | text+data (IP/clinical KPI blocks) | R037-R046, R095-R097 | — |
| Slide 11 (p12) | "Specialized Manufacturing Built on Global Quality Standards" (R098) | diagram+text (facility/process map + cert roster) | R047, R048, R098-R103, R151 | — |
| Slide 12 (p13) | NOT CAPTURED (Financial Highlights, FY26) | data (highlights table) | R049-R052, R152 | — |
| Slide 13 (p14) | "Business Outlook" (R104) | text (3-segment strategy bullets, dense) | R104, R118-R131 | note: 14 FORWARD rows on one slide, the single densest page in the deck |
| Slide 14 (p15) | NOT CAPTURED (closing tagline: "Translating Nature's Benefits with Science", R105) | text (closing/brand slide) | R105 | — |

Slide count check: 1 cover letter + 14 deck slides = 15 pages = sweep_count above. Sum of IDs across all 15 units = 152 = ids_in_structured (verified by direct tally, matches grep totals below).

## TABLE 1: NUMBERS (R001-R052, 52 rows — "every number on every slide")

Every row below references its A1 ID only; verbatim value stays in the
structured file. No zero/nil/dash-valued line items were found anywhere in
this deck (this is a highlights-style presentation, not a full financial
statement with template line items) — zero_standing: 0, ZERO_STANDING flag
not applicable this doctype/run.

| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R001 | number | — | letter ref no., cover letter |
| R002 | number | — | BSE scrip code |
| R003 | number | — | regulation cited |
| R004 | number | — | prior letter ref no., cross-ref R134 (date of that letter) |
| R005 | number | — | demographic stat, slide 2 |
| R006 | number | — | demographic stat, slide 2, projected |
| R007 | number | — | demographic stat, slide 2 |
| R008 | number | — | demographic stat, slide 2, projected |
| R009 | number | — | NCD stat, slide 2, footnote R142 |
| R010 | number | — | activity stat, slide 2 |
| R011 | number | — | obesity stat worldwide, slide 2, footnote R143 |
| R012 | number | — | hypertension stat India, slide 2, footnote R144 (shares marker w/ R013) |
| R013 | number | — | obesity stat India, slide 2, footnote R144 |
| R014 | number | — | diabetes stat India, slide 2 |
| R015 | number | — | supplement usage stat US, slide 2, footnote R145 |
| R016 | number | — | supplement usage stat India, slide 2, footnote R145 |
| R017 | number | — | nutraceutical market size, slide 3, source R147 |
| R018 | number | — | botanical ingredients market size, slide 3, source R147 |
| R019 | number | — | API segment sales share, slide 5; RECONCILE: 67%+16%+17% = 100% (R019+R020+R021), internally consistent |
| R020 | number | — | Biopolymer segment sales share, slide 5 |
| R021 | number | — | Nutraceuticals segment sales share, slide 5 |
| R022 | number | — | API franchise build period, slide 6 |
| R023 | number | — | CEP approved count, slide 6 |
| R024 | number | — | CEP under-evaluation count, slide 6 |
| R025 | number | — | US-DMF filed count, slide 6 |
| R026 | number | — | API geographic reach, slide 6 |
| R027 | number | — | API active customers, slide 6 |
| R028 | number | — | API export revenue share FY26, slide 6, period note R148 |
| R029 | number | — | Biopolymer geographic reach, slide 7 |
| R030 | number | — | Biopolymer active customers, slide 7 |
| R031 | number | — | Biopolymer export revenue share FY26, slide 7, period note R149 |
| R032 | number | — | flagship branded ingredient count, slide 8 |
| R033 | number | — | planned branded ingredient additions, slide 8; cross-ref R128 (target "6-8 branded ingredients", slide 13) — feeds A4 arithmetic-consistency check (5 current + 2 planned = 7, within stated 6-8 target range) |
| R034 | number | — | Nutraceuticals geographic reach, slide 8 |
| R035 | number | — | Nutraceuticals active customers, slide 8 |
| R036 | number | — | Nutraceuticals export revenue share FY26, slide 8, period note R150 |
| R037 | number | — | patents filed, slide 10 |
| R038 | number | — | patents granted, slide 10; cross-check: R037 (9 filed) vs R038 (5 granted) vs R039 (4 under review) — 5+4=9, internally consistent |
| R039 | number | — | patents under review, slide 10 |
| R040 | number | — | US patents, slide 10 (subset of R037-R039, basis not specified — FOOTNOTE_UNRESOLVED: no note clarifies which filed/granted bucket the 2 US patents belong to) |
| R041 | number | — | total clinical trials, slide 10 |
| R042 | number | — | pre-clinical trials, slide 10 |
| R043 | number | — | publications, slide 10 |
| R044 | number | — | clinical trials, Aspargize, slide 10 |
| R045 | number | — | clinical trials, Maxicuma, slide 10; cross-check: R044+R045+R046 = 10+5+2 = 17, vs R041 total "20" clinical trials — 3 trial gap unexplained by named-product breakdown (materiality note for A3/A4: possible unnamed products or rounding in headline "20") |
| R046 | number | — | clinical trials, Gingeren, slide 10 |
| R047 | number | — | Dehradun capacity, slide 11 |
| R048 | number | — | Kashipur capacity, slide 11 |
| R049 | number | — | Revenue FY26, slide 12, period note R152 |
| R050 | number | — | Gross Margin FY26, slide 12, period note R152 |
| R051 | number | — | EBITDA FY26, slide 12, period note R152; cross-check: R051/R049 = 29/246 = 11.8%, vs stated R052 EBITDA Margin 11.9% — consistent within rounding |
| R052 | number | — | EBITDA Margin FY26, slide 12, period note R152 |

## TABLE 2: ENTITIES (R053-R105, 53 rows)

| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R053 | entity | — | filing recipient, cover letter |
| R054 | entity | — | filing recipient, cover letter |
| R055 | entity | — | address block, cover letter (ENTITY-SUMMARY grouping per A1 materiality rule) |
| R056 | entity | — | self-reference symbol, cover letter |
| R057 | entity | — | regulator cited, cover letter |
| R058 | entity | — | hosting URL, cover letter |
| R059 | entity | — | signing company, cover letter |
| R060 | entity | — | digital signature cert block (ENTITY-SUMMARY grouping); cross-ref R136 (signature timestamp) |
| R061 | entity | — | signatory, cover letter; cross-ref R060, R136 |
| R062 | entity | — | subject entity, slide 1 |
| R063 | entity | — | confidentiality legend, slide 1 |
| R064 | entity | — | target health categories (ENTITY-SUMMARY), slide 3 |
| R065 | entity | — | demerger parent entity, slide 4 |
| R066 | entity | — | biopolymer portfolio added at demerger, slide 4 |
| R067 | entity | — | segment 1 name, slide 5 |
| R068 | entity | — | segment 2 name, slide 5 |
| R069 | entity | — | segment 3 name, slide 5 |
| R070 | entity | — | API product list (ENTITY-SUMMARY), slide 5; cross-ref R077-R080 (same 4 products named individually on slide 6) |
| R071 | entity | — | Biopolymer product list (ENTITY-SUMMARY), slide 5 |
| R072 | entity | — | Nutraceuticals product list (ENTITY-SUMMARY), slide 5 |
| R073 | entity | — | slide 6 subject/title |
| R074 | entity | — | certification type defined, slide 6 |
| R075 | entity | — | filing type defined, slide 6 |
| R076 | entity | — | quality certification, slide 6 |
| R077 | entity | — | API product, slide 6; cross-ref R070 |
| R078 | entity | — | API product, slide 6; cross-ref R070 |
| R079 | entity | — | API product, slide 6; cross-ref R070 |
| R080 | entity | — | API product, slide 6; cross-ref R070 |
| R081 | entity | — | slide 7 subject/title |
| R082 | entity | — | Biopolymer end markets (ENTITY-SUMMARY), slide 7 |
| R083 | entity | — | slide 8 subject/title |
| R084 | entity | — | regulatory approval cited, slide 8 |
| R085 | entity | — | certification cited, slide 8 |
| R086 | entity | — | branded product, slide 8; cross-ref R044, R116 (Aspargize trials/clinical mentions) |
| R087 | entity | — | branded product, slide 8; cross-ref R046 (Gingeren trials) |
| R088 | entity | — | branded product, slide 8; cross-ref R045 (Maxicuma trials) |
| R089 | entity | — | branded product, slide 8 (Xanthogreen — no trial-count row exists for this product; only Aspargize/Maxicuma/Gingeren get trial breakdowns in R044-R046) |
| R090 | entity | — | branded product, slide 8; cross-ref R116 (Berbisol clinical trials underway) |
| R091 | entity | — | slide 9 subject/title |
| R092 | entity | — | competitive moat pillars (ENTITY-SUMMARY), slide 9 |
| R093 | entity | — | quality certification (moat pillar), slide 9; cross-ref R076 |
| R094 | entity | — | quality certification (moat pillar), slide 9; cross-ref R084 |
| R095 | entity | — | slide 10 subject/title |
| R096 | entity | — | patented tech platform, slide 10 |
| R097 | entity | — | patented tech platform, slide 10 |
| R098 | entity | — | slide 11 subject/title |
| R099 | entity | — | facility location, slide 11; cross-ref R047 (Dehradun capacity) |
| R100 | entity | — | facility location, slide 11; cross-ref R048 (Kashipur capacity) |
| R101 | entity | — | SCFE facility descriptor, slide 11; footnote R151 |
| R102 | entity | — | process/facility capability labels (ENTITY-SUMMARY), slide 11 |
| R103 | entity | — | manufacturing certification roster (ENTITY-SUMMARY), slide 11 |
| R104 | entity | — | slide 13 subject/title |
| R105 | entity | — | closing tagline (ENTITY-SUMMARY), slide 14 |

ENTITY_CHANGE not assessable this run (prior_quarter_ledger: none supplied).

## TABLE 3: FORWARD STATEMENTS (R106-R131, 26 rows)

| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R106 | forward | — | overall positioning statement, slide 4 |
| R107 | forward | — | API strategy 1, slide 6 |
| R108 | forward | — | API strategy 2, slide 6; cross-ref R118 (restated on outlook slide 13) |
| R109 | forward | — | API strategy 3, slide 6; cross-ref R120 (restated on outlook slide 13) |
| R110 | forward | — | Biopolymer strategy 1, slide 7; cross-ref R123 (restated on outlook slide 13) |
| R111 | forward | — | Biopolymer strategy 2, slide 7; cross-ref R124 (restated on outlook slide 13) |
| R112 | forward | — | Biopolymer strategy 3, slide 7; cross-ref R125 (restated on outlook slide 13) |
| R113 | forward | — | Nutraceuticals strategy 1, slide 8 |
| R114 | forward | — | Nutraceuticals strategy 2, slide 8 |
| R115 | forward | — | Nutraceuticals strategy 3, slide 8 |
| R116 | forward | — | ongoing trial (Berbisol), slide 8; cross-ref R090 |
| R117 | forward | — | Nutraceuticals outlook statement, slide 9 |
| R118 | forward | RESTATED | API outlook, slide 13; cross-ref R108 (same "1 new API/year" commitment repeated verbatim across slide 6 and slide 13) |
| R119 | forward | — | API outlook (share gain), slide 13 |
| R120 | forward | RESTATED | API outlook, slide 13; cross-ref R109 (regulated-market expansion repeated across slide 6 and slide 13) |
| R121 | forward | — | API outlook (NRT pharma presence), slide 13 |
| R122 | forward | — | Biopolymer outlook (higher-value mix), slide 13 |
| R123 | forward | RESTATED | Biopolymer outlook, slide 13; cross-ref R110 |
| R124 | forward | RESTATED | Biopolymer outlook, slide 13; cross-ref R111 |
| R125 | forward | RESTATED | Biopolymer outlook, slide 13; cross-ref R112 |
| R126 | forward | — | Nutraceuticals outlook (primary growth driver), slide 13 |
| R127 | forward | — | Nutraceuticals outlook (clinical validation), slide 13 |
| R128 | forward | — | Nutraceuticals outlook target, slide 13; cross-ref R032, R033 (5 current + 2 planned = 7, within stated 6-8 target) |
| R129 | forward | — | Nutraceuticals outlook (distribution expansion), slide 13 |
| R130 | forward | — | Nutraceuticals outlook (customer penetration), slide 13 |
| R131 | forward | — | overall strategic summary, slide 13, closing line of outlook slide |

Materiality note: slide 13 (Business Outlook) restates 5 of its 14 forward
statements (R118, R120, R123, R124, R125) nearly verbatim from the earlier
segment slides (R108-R112) — flagged RESTATED, not a new commitment, for A3/A4
to avoid double-counting forward-looking claims as fresh guidance.

## TABLE 4: DATES (R132-R141, 10 rows)

| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R132 | date | — | letter date, cover letter |
| R133 | date | — | regulation year cited, cover letter |
| R134 | date | — | prior letter date, cover letter; cross-ref R004 |
| R135 | date | — | investor meeting date, cover letter; same calendar date as R132 (letter issued same day as the meeting) |
| R136 | date | — | digital signature timestamp, cover letter; cross-ref R060, R061 — signature timestamp is same-day, post letter date, no MGMT_ABSENCE-style anomaly detected |
| R137 | date | — | presentation month/date, slide 1 |
| R138 | date | — | journey milestone period 1, slide 4 |
| R139 | date | — | journey milestone period 2, slide 4 |
| R140 | date | — | journey milestone period 3, slide 4 |
| R141 | date | — | journey milestone period 4 ("Current" = demerger stage), slide 4 |

## TABLE 5: FOOTNOTES / QUALIFIERS (R142-R152, 11 rows — "every footnote and fine-print disclaimer qualifying a headline number")

| ROW_ID | category | A2 flags | cross-ref / materiality note |
|---|---|---|---|
| R142 | footnote | — | defines NCD abbreviation qualifying R009, slide 2 |
| R143 | footnote | — | defines obesity threshold qualifying R011 (worldwide), slide 2 |
| R144 | footnote | — | defines obesity threshold qualifying R013 (India); shares footnote marker context with R012 (hypertension, unfootnoted number on same line range), slide 2 |
| R145 | footnote | — | defines supplement scope qualifying R015/R016, slide 2 |
| R146 | footnote | — | source attribution, slide 2, qualifies all of R005-R016 |
| R147 | footnote | — | source attribution, slide 3, qualifies R017-R018 |
| R148 | footnote | — | period-basis note qualifying R028 (API export mix, FY26), slide 6 |
| R149 | footnote | — | period-basis note qualifying R031 (Biopolymer export mix, FY26), slide 7 |
| R150 | footnote | — | period-basis note qualifying R036 (Nutraceuticals export mix, FY26), slide 8 |
| R151 | footnote | — | defines SCFE abbreviation qualifying R101, slide 11 |
| R152 | footnote | — | period-basis note qualifying R049-R052 (all four financial-highlight figures, FY26), slide 12 |

All 11 footnote markers/notes resolve to a matching pair in the structured
file (marker + note text both captured) — no FOOTNOTE_UNRESOLVED flag on the
footnote mechanism itself. (A separate, unrelated FOOTNOTE_UNRESOLVED note is
raised at R040 in Table 1: the "2 US patents" figure has no note clarifying
which bucket — filed/granted/under-review — it is a subset of; that is a gap
in a NUMBER's basis, not a broken footnote pair, so it is flagged there.)

=== ID ACCOUNTABILITY ===
ids_in_structured: 152
ids_referenced_in_ledger: 152
orphan_ids: []
match: yes

=== FLAG SUMMARY ===
RESTATED: R108/R118, R109/R120, R110/R123, R111/R124, R112/R125 (5 pairs, 10 IDs)
FOOTNOTE_UNRESOLVED: R040 (US-patent count has no basis note)
ZERO_STANDING: none present this doctype/run (0 line items)
ENTITY_CHANGE: not assessable (no prior-quarter ledger supplied)
DROPPED_SLIDE: not assessable (no prior-quarter ledger supplied)
MGMT_ABSENCE / REPEAT_QUESTION / turns / questions: not applicable — doctype
is presentation, not concall transcript

=== END A2 COMPLETENESS LEDGER ===
