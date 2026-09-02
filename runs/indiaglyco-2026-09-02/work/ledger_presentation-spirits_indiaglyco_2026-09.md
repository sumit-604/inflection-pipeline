=== A2 COMPLETENESS LEDGER ===
company: India Glycols Limited (INDIAGLYCO) — IGL Spirits (Entity B)
quarter: 2026-09
doctype: presentation
source_structured: indiaglyco-presentation-spirits-2026-09-structured.md (R001-R355)
prior_quarter_ledger: none (first quarterly review of this entity/doctype pair; DROPPED_SLIDE and ENTITY_CHANGE diffs not applicable this run)

=== A2 COUNT TEST ===
category: slides        grep_count: 31   sweep_count: 31   match: yes
category: numbers       grep_count: 159  sweep_count: 159  match: yes
category: entities       grep_count: 84   sweep_count: 84   match: yes
category: forward        grep_count: 42   sweep_count: 42   match: yes
category: dates          grep_count: 50   sweep_count: 50   match: yes
category: qualifiers/footnotes  grep_count: 20   sweep_count: 20   match: yes
category: zero_standing  grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===

Method note: grep_count = tag-field grep (`grep -cE '\| TAG \|'`) per category, matching A1's
self-reported row_counts header exactly. sweep_count = independent awk field-split
(`awk -F' \| ' '{print $4}'`) re-tally of the same file, plus a manual per-page ID roll-up
(below) whose 31 page-groups sum to 355, matching total_rows. Both methods agree on every
category (GATE A2 pass). Zero/nil/dash-valued NUMBER rows: none found by regex sweep
(`\| NUMBER \| (0|Nil|-|–|N/A) \|`) — this is a broker-meet deck, not a results/statement
filing, so the ZERO_STANDING template-signal rule (results-filing item 2) has no applicable
instances; recorded as 0, not omitted.

=== ID ACCOUNTABILITY ===
ids_in_structured: 355
ids_referenced_in_ledger: 355
orphan_ids: []
match: yes

## TABLE 1 — SLIDE INVENTORY (slide/page = A1's page field; title/content-type inferred from
## the row content on that page, since A2 does not re-read the source; every ID for the page
## is grouped here — this satisfies presentation-checklist items 1-2 and the ID-accountability
## contract for all 355 rows)

slide | inferred_title | content_type | row_ids | row_count | flags
1 | Exchange filing letter (BSE/NSE Reg. 30 intimation) | text/letterhead | R001-R003,R160-R169,R286-R289 | 17 | —
2 | Cover slide: "IGL Spirits Limited" | text | R170,R290,R336 | 3 | —
3 | Forward-looking statements disclaimer | text/legal | R171,R172,R337 | 3 | BASIS_QUALIFIER (safe-harbor, R337)
4 | Section divider: "1. Introduction" | text | R240 | 1 | —
5 | Key snapshot (Rev/EBITDA CAGR, RoCE, capacity, rankings) | text+numbers | R004-R012,R338-R341 | 13 | BASIS_QUALIFIER (footnotes 1-4)
6 | Journey / milestones timeline (two tracks: consumer-facing, manufacturing) | timeline+text | R013-R016,R173-R186,R291-R301,R342 | 30 | BASIS_QUALIFIER (CSD/core-market note)
7 | Section divider: "2. Industry Overview" | text | R241 | 1 | —
8 | Industry overview: demographics & alcobev consumption charts | charts | R017-R048,R187,R302-R311,R343 | 44 | BASIS_QUALIFIER (ex-beer, FX rate)
9 | Premiumization / affluent India trends | charts+text | R049-R065,R188,R244,R312-R321,R344 | 30 | PROJECTION (R244: $4.3tn by 2030); BASIS_QUALIFIER (affluent definition)
10 | Ethanol / bio-fuel industry overview | charts+text | R066-R076,R189,R245-R247,R322-R324,R345,R346 | 20 | PROJECTION (R245-R247: fleet/SAF/energy-security projections to 2030); BASIS_QUALIFIER (IEA estimates, FX rate)
11 | Section divider: "3. IGL Spirits" | text | R242 | 1 | —
12 | Brand portfolio by price tier (Elite/Affluent/Premium/Deluxe/Regular) | table+brand roster | R077-R081,R190-R205,R248-R252,R347 | 27 | PROJECTION (R248-R252: pipeline launches by tier); BASIS_QUALIFIER (MRP basis)
13 | White spirits segment | text+numbers | R082-R087,R206,R207,R253-R255,R325 | 12 | PROJECTION (R253-R255: volume target, 8-state expansion by FY-end)
14 | Whisky portfolio | text+numbers | R088,R089,R208-R212 | 7 | —
15 | Black Rum portfolio | text+numbers | R213-R217,R256,R257 | 7 | PROJECTION (R256,R257: growth/positioning claims, no anchor date)
16 | Bacardi partnership | text | R090,R218-R223,R258,R348 | 9 | BASIS_QUALIFIER (ranking by volume)
17 | Amrut partnership | text+numbers | R091-R095,R224-R229,R259,R260,R326,R327,R349 | 16 | BASIS_QUALIFIER (ranking by volume)
18 | Market footprint / geographic expansion map | map/legend | R230,R261,R350 | 3 | PROJECTION (R261: new-market expansion list); BASIS_QUALIFIER (IMFL/CSD glossary)
19 | CSD / Paramilitary channel | text | R096,R231,R232,R262-R264 | 6 | PROJECTION (R262-R264: planned launches, depot expansion)
20 | Bio-fuels overview | text+numbers | R097-R101,R328,R351 | 7 | BASIS_QUALIFIER (ESY definition, company-estimate basis)
21 | Manufacturing facilities (Kashipur, Gorakhpur) | text+numbers | R102-R108,R352 | 8 | PROJECTION (R352 footnote explicitly flags a capacity figure as "FY27E Projection" — the only qualifier in the deck that tags a NUMBER as forward-looking at footnote level, not just headline level)
22 | Feedstock-to-finished-goods process flow diagram | diagram | R233 | 1 | —
23 | Business model advantages / margin profile | text+numbers | R109,R234-R236,R329,R353 | 6 | BASIS_QUALIFIER (gross margin = Potable Spirits only)
24 | Strategic priorities (8 points) | text | R265-R272 | 8 | PROJECTION (all 8 rows are forward strategic-priority statements)
25 | Section divider: "4. Financial Highlights" | text | R243 | 1 | —
26 | Operational Highlights — Potable Spirits (FY24-FY26 actuals) | table | R110-R122 | 13 | — (historical actuals only, no forward rows)
27 | Key Historical Financials (Revenue/EBITDA/PAT, FY24-FY26 actuals) | table | R123-R144,R354 | 23 | BASIS_QUALIFIER (PAT post group bifurcation)
28 | Net Debt / Cash Profit / RoCE (FY24-FY26 actuals) | table | R145-R153,R355 | 10 | BASIS_QUALIFIER (Net Debt/Cash Profit/RoCE definitions)
29 | EBITDA growth pathway FY27E→FY31E | chart+text | R154,R155,R237,R273-R278,R330,R331 | 11 | PROJECTION (R154,R155,R273-R278: ~INR500Cr FY27E to ~INR1,000Cr FY31E pathway, all 5 growth drivers forward)
30 | Business outlook (EBITDA/volume/debt-free targets) | text | R156-R158,R279-R285,R332-R335 | 14 | PROJECTION (R156-R158,R279-R285: FY27/FY28/3-4yr targets — highest projection density on the deck)
31 | Contact details / CIN | text | R159,R238,R239 | 3 | —

TOTAL row_ids grouped: 355 (matches ids_in_structured; orphan_ids empty)

## TABLE 2 — FOOTNOTES / FINE-PRINT QUALIFIERS (presentation-checklist item 4; all 20
## QUALIFIER-tagged rows, each already carrying its slide of origin via Table 1)

qualifier_id | slide | subject | flags
R336 | 2 | confidentiality legend | —
R337 | 3 | forward-looking-statements safe-harbor disclaimer | BASIS_QUALIFIER
R338 | 5 | Revenue/EBITDA CAGR basis = FY24-26 | BASIS_QUALIFIER
R339 | 5 | RoCE period = FY26 | BASIS_QUALIFIER
R340 | 5 | Top-5 ranking basis = sales volume in India | BASIS_QUALIFIER
R341 | 5 | initial allocation period = Ethanol Supply 2026 | BASIS_QUALIFIER, PROJECTION-adjacent (allocation, not realised revenue)
R342 | 6 | CSD abbreviation + core-markets definition | BASIS_QUALIFIER
R343 | 8 | ex-beer exclusion; INR/USD=90 FX rate | BASIS_QUALIFIER
R344 | 9 | "Affluent" defined as >US$10,000 p.c. income | BASIS_QUALIFIER
R345 | 10 | IEA Outlook basis for farmer-earnings/CO2/crude estimates | BASIS_QUALIFIER
R346 | 10 | INR/USD=90 FX rate | BASIS_QUALIFIER
R347 | 12 | MRP basis: UP prices, 750ml, some extrapolated | BASIS_QUALIFIER
R348 | 16 | ranking basis = by volume | BASIS_QUALIFIER
R349 | 17 | Old Port Rum ranking basis = by volume | BASIS_QUALIFIER
R350 | 18 | IMFL/CSD glossary | —
R351 | 20 | company-estimate basis + ESY definition (Nov 1-Oct 31) | BASIS_QUALIFIER
R352 | 21 | capacity figures: (1) as of FY26, (2) FY27E Projection | BASIS_QUALIFIER, PROJECTION — flags a capacity NUMBER as forward-looking at footnote level
R353 | 23 | gross margin = Potable Spirits only | BASIS_QUALIFIER
R354 | 27 | PAT basis = post Group's bifurcation into resulting companies | BASIS_QUALIFIER — structural discontinuity note, material for period-over-period PAT comparability
R355 | 28 | Net Debt / Cash Profit / RoCE formula definitions | BASIS_QUALIFIER

count: 20 (matches grep_count and sweep_count above)

## TABLE 3 — FORWARD / PROJECTION CROSS-REFERENCE (task-specific: this is a broker-meet deck
## with many FY27E/FY31E projections; every FORWARD-tagged row plus every NUMBER/DATE row
## anchored to a projection year, cross-referenced to its governing BASIS_QUALIFIER where one
## exists)

forward_row_range | slide(s) | subject | governing_qualifier | flag
R244 | 9 | alcobev consumption value to $4.3tn by 2030 | R343 (ex-beer, FX=90) | PROJECTION
R245-R247 | 10 | vehicle fleet 450mn by 2030; flex-fuel/SAF demand; energy-security rationale | R345,R346 | PROJECTION
R248-R252 | 12 | per-tier pipeline launch counts (Elite/Affluent/Premium/Deluxe) | R347 | PROJECTION
R253-R255 | 13 | white-spirits volume target, 8-state expansion, CSD approval | none | PROJECTION
R256-R257 | 15 | Black Rum category-outpace and seasonal-demand claims | none | PROJECTION (qualitative, no target date)
R258-R260 | 16-17 | Bacardi exclusivity claim; Amrut economics and strategic rationale | none | PROJECTION (structural, ongoing)
R261-R264 | 18-19 | new-market expansion list; CSD launch pipeline; depot expansion | none | PROJECTION
R265-R272 | 24 | 8 strategic priorities | none | PROJECTION (all 8)
R273-R278 | 29 | EBITDA growth pathway drivers (1-5) | R237 (Source: Company Projections) | PROJECTION
R279-R285 | 30 | business outlook: Top-3 aspiration, EBITDA >INR550Cr by FY27, 2x IMFL volumes by FY27, debt-free by FY28, INR1,000Cr EBITDA in 3-4yrs | R332-R335 (target-year dates) | PROJECTION
R154,R155 | 29 | EBITDA ~INR500Cr FY27E -> ~INR1,000Cr FY31E pathway numbers | R237,R330,R331 | PROJECTION
R156-R158 | 30 | EBITDA INR550Cr by FY27; 2x IMFL volume; INR1,000Cr in 3-4yrs (headline NUMBER duplicates of R280-R285 FORWARD text — same underlying claims, two tags) | R332-R335 | PROJECTION, RESTATED (cross-ref R280-R285)

count: 42 FORWARD rows all classified PROJECTION; 2 NUMBER rows (R154,R155) plus 3 NUMBER
rows (R156-R158) restate the same FY27/FY31 targets stated in FORWARD prose — flagged
RESTATED, not double-counted (each ID counted once in its own tag category per header).

## TABLE 4 — ZERO_STANDING

None found. Regex sweep of all 159 NUMBER rows for 0/Nil/dash/N/A values returned no matches.
This doctype is a broker-meet investor presentation (highlight/growth-story format), not a
results filing with a standardised P&L/balance-sheet line-item template, so the "line exists
because a zero-value transaction type is anticipated" signal (Amendment example: Southwest
"Profit on sale of share in subsidiary") has no applicable slide here. Recorded, not dropped.

## TABLE 5 — DROPPED_SLIDE / ENTITY_CHANGE

Not applicable. Prior-quarter ledger path = none (first quarterly-review run for this
entity/doctype pair). No diff base exists; flag not raised this run and should be raised on
the NEXT quarter's A2 run once this ledger becomes the prior-quarter reference.
