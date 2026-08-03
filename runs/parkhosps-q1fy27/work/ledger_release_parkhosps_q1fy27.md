# LEDGER — Park Medi World Limited (PARKHOSPS), Q1 FY27, doctype: release (Reg 30 Media/Earnings Release)
Source: `extract_release_parkhosps_q1fy27.txt` (A1 extract; canonical doctype mapped to `presentation`; 4 PDF pages, 158 content lines, unit convention Millions, x0.1 to Cr).
Enumeration class applied per task instruction: presentation/narrative class — every page as a unit, every number in the summary table and narrative, every footnote/qualifier.

## CATEGORY MAP (how this doctype's content is mapped onto the standard A2 count fields)
- `slides` / `slide_numbers` -> the 4 physical pages of the release (page units).
- `line_items` -> every figure in the KEY CONSOLIDATED OPERATING & FINANCIAL SUMMARY table (cell-level).
- `zero_standing` -> zero/nil/dash-valued standing items check across the table and narrative (none found).
- `agenda_items` (repurposed for this doctype) -> every discrete numeric disclosure in the narrative outside the table: headline preview box, Q1 FY27 Highlights bullets, Growth Highlights bullets, "About Park Medi World" section.
- `mgmt_numbers` -> every number inside the Chairman/MD management quote.
- `notes` -> every footnote/qualifier: the cautionary forward-looking-statements paragraph, the "Unaudited" qualifier, approximation qualifiers (~, c.), the open-ended "150+" qualifier, the signature-block timezone qualifier.
- `entities` -> every distinct corporate/hospital/counterparty entity named.
- `turns`, `questions`, `auditor_paras` -> not applicable to this doctype (no transcript, no auditor report); set to 0.
- Signature block and pure administrative metadata (addresses, scrip codes, regulatory citation, IR contacts) are enumerated in their own supplementary table per Rule 7 (digital signature blocks) but are **not** folded into any gated count field; every row still carries a line number.

Convention note (documented so the grep/manual reconciliation is reproducible): quarter/FY period-labels that are self-referential to the reporting period itself (e.g. "Q1" in "Q1 FY'27", "27" in "FY'27", "26" in "FY'26" used as a bare period tag, not as a value) are treated the same way the table's own column headers were excluded from the table figure count — they are period identifiers, not disclosed values, and are excluded from the narrative/quote figure counts below. Every exclusion is called out explicitly at the line where it occurs.

=== A2 COUNT TEST ===
category: slides (pages)      grep_count: 4    sweep_count: 4    match: yes
category: slide_numbers       grep_count: 4    sweep_count: 4    match: yes
category: line_items       grep_count: 55   sweep_count: 55   match: yes
category: zero_standing    grep_count: 0    sweep_count: 0    match: yes
category: agenda_items     grep_count: 65   sweep_count: 65   match: yes
category: mgmt_numbers     grep_count: 8    sweep_count: 8    match: yes
category: notes            grep_count: 10   sweep_count: 10   match: yes
category: entities         grep_count: 12   sweep_count: 12   match: yes
category: turns            grep_count: 0    sweep_count: 0    match: yes (n/a — not a transcript doctype)
category: questions        grep_count: 0    sweep_count: 0    match: yes (n/a — not a transcript doctype)
category: auditor_paras    grep_count: 0    sweep_count: 0    match: yes (n/a — no auditor report in this doctype)
gate_a2: pass
=== END COUNT TEST ===

---

## TABLE 1 — PAGE / SECTION UNITS (4)

| # | Page marker line | PDF page content | Printed internal footer no. | Flags |
|---|---|---|---|---|
| 1 | 15 | Cover letter: Reg 30 disclosure to BSE/NSE, signed by Company Secretary (digital signature) | none (cover letter unpaginated) | — |
| 2 | 53 | Headline preview (YoY growth stats, bed-addition guidance), dateline, Q1 FY27 HIGHLIGHTS (5 bullets), Growth Highlights bullets 1-3 (Panchkula, Rudrapur, Umkal/Palam Vihar) | "1" (line 96) | — |
| 3 | 99 | Growth Highlights bullets 4-5 continued (Mehar, Agra/Febris/CY2026 total), KEY CONSOLIDATED OPERATING & FINANCIAL SUMMARY table, start of Chairman/MD quote, start of "About Park Medi World" | "2" (line 144) | — |
| 4 | 147 | End of "About Park Medi World", contact/IR details, Cautionary statement on forward-looking statements | none printed in extract (footer number absent) | PAGE_FOOTER_GAP — last page carries no printed page number in the extract though the doc is internally paginated 1-2 on pages 2-3 |

Grep check: `grep -c '\[page ' extract_release_parkhosps_q1fy27.txt` = 4. Manual sweep = 4 pages (15, 53, 99, 147). Match.

---

## TABLE 2 — KEY CONSOLIDATED OPERATING & FINANCIAL SUMMARY (table figures, 55 cells / 11 metrics x 5 periods)
Unit: Rs Millions as stated ("INR mn"); x0.1 to reach Rs Crores per A1 header. Header row at line 109 (Particulars / Q1FY'27 / Q1FY'26 / YoY% / Q4FY'26 / QoQ%) excluded from the figure count — it is a column-label row, not a data row (same convention as excluding page-marker/section-heading numerals elsewhere in this ledger).

### Operating Figures

| Line | Metric | Q1 FY27 | Q1 FY26 | YoY% | Q4 FY26 | QoQ% | Flags |
|---|---|---|---|---|---|---|---|
| 111 | Total Bed Capacity | 3,960 | 3,000 | 32% | 3,610 | 10% | — |
| 112 | Occupancy (%) | 55.6% | 67.8% | -1,224 bps | 62.5% | -692 bps | — |
| 113 | Total Patients ('000s) | 249.8 | 213.9 | 17% | 213.5 | 17% | — |
| 114 | IPD patients ('000s) | 26.3 | 22.8 | 16% | 25.3 | 4% | — |
| 115 | OPD patients ('000s) | 223.4 | 191.2 | 17% | 188.2 | 19% | — |

Subheading at line 116 ("Financial Performance (INR mn)") — text only, no digits, not counted as a data row.

### Financial Performance (INR mn)

| Line | Metric | Q1 FY27 | Q1 FY26 | YoY% | Q4 FY26 | QoQ% | Flags |
|---|---|---|---|---|---|---|---|
| 117 | Revenue from Operations | 4,757 | 3,988 | 19% | 4,604 | 3% | — |
| 118 | EBITDA (ex-Other Income) | 1,261 | 1,049 | 20% | 1,274 | -1% | — |
| 119 | EBITDA Margin (%) | 26.5% | 26.3% | 20 bps | 27.7% | -116 bps | — |
| 120 | Net Profit | 886 | 655 | 35% | 768 | 15% | — |
| 121 | Net Profit Margin (%) | 18.6% | 16.4% | 220 bps | 16.7% | 195 bps | — |
| 122 | EPS (INR) | 2.05 | 1.70 | 20% | 1.78 | 15% | — |

**Zero/nil/dash check across all 55 cells: none found.** All 11 metrics carry populated non-zero values in all 5 columns for all periods shown; `zero_standing` = 0. (Full-document sweep for `nil`, bare `0`, `N/A`, `--` outside metadata found no matches — see Table 6 note.)

**Unit-consistency flag:** UNIT_INCONSISTENCY — the table and the Highlights bullets (Table 4) state figures in "INR mn"; the Growth Highlights bullets (Table 5) and "About" section state acquisition valuations and one facility's FY26 revenue in "INR crs" (e.g. line 83: "INR 177 crs"; line 88: "~INR 245 crs"; line 91: "INR 107 crs"). No mn-to-crs conversion is shown for these three figures inside the narrative itself; A3/A4 should reconcile against the x0.1 convention stated in the A1 header if cross-referencing them to the mn-denominated table.

Grep check (clean token extraction on lines 111-115, 117-122 with page-column headers and `'000s` unit labels stripped): 55 tokens. Manual sweep (5 columns x 11 metric rows): 55. Match.

---

## TABLE 3 — HEADLINE PREVIEW BOX (before "Q1 FY27 HIGHLIGHTS" heading; 9 figures)

| # | Line | Figure | Context (first words) | Flags |
|---|---|---|---|---|
| 1 | 57 | 19% | "...year-on-year growth of 19% in Revenue..." | RESTATED (matches Table 4 row 1 and Table 2 line 117 YoY%) |
| 2 | 57 | 20% | "...20% [in EBITDA]..." | RESTATED (matches Table 4 row 2 and Table 2 line 118 YoY%) |
| 3 | 58 | 35% | "...and 35% in Net Profit." | RESTATED (matches Table 4 row 3 and Table 2 line 120 YoY%) |
| 4 | 60 | 1,490 | "The Company expects to add 1,490 beds in calendar year 2026" | GUIDANCE; RESTATED at line 102 and line 132 (quote) |
| 5 | 60 | 2026 | "...calendar year 2026..." | GUIDANCE timeline; RESTATED |
| 6 | 60 | 46% | "...c.46% growth in bed capacity..." | GUIDANCE; APPROX (c.); RESTATED at line 102/103 and line 132 |
| 7 | 61 | 2025 | "...over 2025 capacity..." | reference-year for guidance base |
| 8 | 61 | 3,250 | "...2025 capacity of 3,250 beds..." | GUIDANCE base; RESTATED at line 103 |
| 9 | 61 | 12 | "...single largest addition ... in any 12-month period." | descriptor; RESTATED at line 104 |

Note: line 57 also contains the self-referential period tag "Q1 FY'27" (tokens "1" and "27") — excluded per the period-label convention stated above.

---

## TABLE 4 — Q1 FY27 HIGHLIGHTS BULLETS (financial; 5 bullets, 14 figures)

| Bullet | Line(s) | Figures (in order) | First 15 words | Flags |
|---|---|---|---|---|
| 1 — Revenue | 71 | 4,757; 19% | "Quarterly Revenue of INR 4,757 mn, growth of 19% YoY" | matches Table 2 line 117 |
| 2 — EBITDA | 72 | 1,261; 20%; 26.5%; 20 bps | "Quarterly EBITDA of INR 1,261 mn, growth of 20% YoY, with EBITDA margin of 26.5%..." | matches Table 2 line 118-119 |
| 3 — Net Profit | 73 | 886; 35%; 18.6%; 220 bps | "Quarterly Net Profit of INR 886 mn, growth of 35% YoY, with Net Profit margin..." | matches Table 2 line 120-121 |
| 4 — Debt | 75 | 256; 30; 2026 | "Negligible term bank debt of INR 256 mn as of 30th June 2026" | qualifier "Negligible" attached to 256; date = period-end, not new guidance |
| 5 — Liquidity | 76 | 2,998 | "Strong liquidity with INR 2,998 mn in Fixed Deposits." | qualifier "Strong" attached; balance-sheet figure not in the summary table |

Grep check (bullet markers): `grep -c '➢'` across lines 69-77 = 5. Manual sweep = 5. Match. Figure-token grep on lines 71,72,73,75,76 = 14. Manual sweep = 14. Match.

---

## TABLE 5 — GROWTH HIGHLIGHTS BULLETS (5 bullets, 31 figures)

| Bullet | Line(s) | Entity/subject | Figures (in order) | First 15 words | Flags |
|---|---|---|---|---|---|
| 1 — Panchkula | 81 | Panchkula greenfield hospital | 350; 10; 2026 | "Commissioned our largest-ever greenfield hospital in Panchkula (350 beds) on 10th April..." | historical/actual commissioning |
| 2 — Rudrapur | 82-84 | The Medicity Hospital (acquisition) | 25; 2026; 177; 2; 2026 | "On 25th May 2026, the Company signed a definitive agreement to acquire..." | valuation in INR crs (UNIT_INCONSISTENCY, see Table 2); SUBSEQUENT_EVENT — hospital "commissioned on 2nd August 2026," i.e. after the June 30, 2026 quarter-end and just one day before the Aug 3, 2026 release date |
| 3 — Umkal/Palam Vihar (Park Platinum) | 85-89 | Umkal Health Care Pvt Ltd / Park Hospital, Palam Vihar | 30; 2026; 225; 100; 86%; 245; 2026; 750 | "On 30th June 2026, our wholly owned subsidiary, Umkal Health Care Private Limited, approved..." | 86% and 245(crs) are APPROX (~) FY26 reference figures for context, not Q1FY27 results; 100-bed addition and 750-bed consolidated target are forward GUIDANCE; commissioning guidance = November 2026 |
| 4 — Mehar | 90-93 | Mehar Hospital, Zirakpur (acquisition) | 3; 2026; 107; 150 | "Today, on 3rd August 2026, the Company signed a definitive agreement to acquire 'Mehar Hospital'..." | SAME_DAY_DISCLOSURE — agreement dated the same day as the release itself (3rd August 2026); "150+" is OPEN_ENDED capacity qualifier; valuation in INR crs |
| 5 — Agra/Febris/CY2026 total | 100-104 | Agra facility; Febris hospital, Narela; company-wide CY2026 target | 360; 2026; 200; 1,490; 2026; 46%; 2026; 3,250; 2025; 12 | "Together with the already commissioned Agra facility with a capacity of 360 beds in February..." | 1,490 / 46% / 3,250 / 12-month are RESTATED from the headline preview (Table 3) and the quote (Table 7); "c.46%" is APPROX |

Note: line 87 contains the self-referential fiscal-year tag "FY'26" (token "26") — excluded per the period-label convention (it labels the reference year for the occupancy/revenue figures on line 88, not itself a new value).

Grep check (bullet markers): `grep -c '➢'` across lines 81-104 = 5. Manual sweep = 5. Match. Figure-token grep on lines 81-104 (period-label token at line 87 excluded) = 31. Manual sweep = 31. Match.

---

## TABLE 6 — MANAGEMENT QUOTE (Chairman & Managing Director, joint attribution)

| Line(s) | Speaker(s) / qualifier | Quote figures (in order) | First 15 words |
|---|---|---|---|
| 125-135 | Dr. Ajit Gupta, Chairman, and Dr. Ankit Gupta, Managing Director — joint quote, single attribution | 19%; 20%; 35%; 220; 18.6%; 1,490; 2026; 46% | "Q1 FY'27 has been a strong start to the year, with Revenue up 19%..." |

Qualifiers on this quote: all results figures (19%, 20%, 35%, 220bps, 18.6%) RESTATE Table 2/Table 4 figures verbatim; the forward figures (1,490 beds, 2026, c.46%) RESTATE Table 3/Table 5 guidance and are subject to the forward-looking-statements cautionary paragraph (Table 8, row 1). Line 126 contains the self-referential period tag "Q1 FY'27" (tokens "1" and "27") — excluded per convention.

Grep check (figure tokens across lines 125-135, period-label token at line 126 excluded): 8. Manual sweep: 8. Match.

---

## TABLE 7 — "ABOUT PARK MEDI WORLD LIMITED" SECTION (11 figures)

| # | Line | Figure | Context | Flags |
|---|---|---|---|---|
| 1 | 139 | 2 | "North India's 2nd largest hospital chain" | ranking claim, not a financial figure |
| 2 | 139 | 17 | "...currently operating 17 hospitals with a combined..." | current network size |
| 3 | 140 | 4,290 | "...capacity of 4,290 beds as on date." | current total capacity (as on release date, not quarter-end) |
| 4 | 140 | 5 | "The Group is in the process of integrating 5 additional hospitals..." | GUIDANCE (pipeline count) |
| 5 | 141 | 2 | "...at 2 existing units." | GUIDANCE (pipeline expansion count) |
| 6 | 141 | 1,450 | "...will add 1,450 beds to our network." | GUIDANCE (pipeline bed addition) |
| 7 | 148 | 4,740 | "Group's total capacity is expected to reach 4,740 beds by March 2027..." | GUIDANCE (capacity target) |
| 8 | 148 | 2027 | "...by March 2027..." | GUIDANCE timeline |
| 9 | 148 | 5,740 | "...and 5,740 beds by March 2028..." | GUIDANCE (capacity target) |
| 10 | 148 | 2028 | "...by March 2028..." | GUIDANCE timeline |
| 11 | 150 | 15 | "...established a strong presence across 15 key cities..." | current footprint |

Note: the 4,290-bed "as on date" figure (line 140) does not reconcile on its face to the 3,960-bed Q1FY27 closing figure in Table 2 (line 111) — the gap (330 beds) is consistent with the Panchkula (350 beds, commissioned in-quarter per Table 5 bullet 1) and subsequent Rudrapur/Mehar transactions disclosed after quarter-end; flagged for A3/A4 to reconcile, not resolved here (enumeration only).

Grep check (figure tokens across lines 139-141, 148, 150): 11. Manual sweep: 11. Match.

---

## TABLE 8 — FOOTNOTES / QUALIFIERS (10)

| # | Line(s) | Qualifier | Text / marker | Flags |
|---|---|---|---|---|
| 1 | 172-177 | Cautionary statement concerning forward-looking statements (full disclaimer paragraph) | "Certain statements in this document may be forward-looking statements..." | qualifies every GUIDANCE-flagged figure in Tables 3, 5, 6, 7 |
| 2 | 54 | "Unaudited" (heading) | "Park Group of Hospitals declares Q1 FY'27 Unaudited Results" | qualifies entire results set in Table 2 and Table 4 |
| 3 | 65-66 | "unaudited financial results" (dateline) | "...today announced its unaudited financial results for the quarter ended 30th June 2026." | duplicate of #2, separate occurrence |
| 4 | 88 | "~86%" approximation | "...had an occupancy of ~86% ..." | qualifies FY26 reference figure in Table 5 bullet 3 |
| 5 | 88 | "~INR 245 crs" approximation | "...delivered a revenue of ~INR 245 crs." | qualifies FY26 reference figure in Table 5 bullet 3; also UNIT_INCONSISTENCY (crs vs mn) |
| 6 | 60 | "c.46%" approximation | "...c.46% growth in bed capacity..." | qualifies Table 3 guidance figure |
| 7 | 102 | "c.46%" approximation | "...marking a capacity addition of c.46%..." | qualifies Table 5 bullet 5 guidance figure (restated) |
| 8 | 132 | "c.46%" approximation | "...a c.46% addition to capacity..." | qualifies Table 6 quote guidance figure (restated) |
| 9 | 92 | "150+" open-ended qualifier | "...with a capacity of 150+ beds..." | qualifies Table 5 bullet 4 figure — exact capacity not disclosed |
| 10 | 46 | "+05'30'" timezone qualifier | signature timestamp "2026.08.03 09:39:47 +05'30'" | qualifies the digital signature timestamp in Table 9 |

Grep check: qualifier-marker regex (`~[0-9]+%|~INR [0-9,]+ crs|c\.[0-9]+%|150\+|\+05'30'|[Uu]naudited`) = 9 occurrences (rows 2-10 above); manual sweep adds the cautionary-statement paragraph as its own unit (row 1) = 10 total either way (the grep for "Cautionary statement" / "forward-looking statements" independently confirms the paragraph's presence at lines 172-177). Match.

---

## TABLE 9 — SIGNATURE BLOCK & ADMINISTRATIVE METADATA (supplementary; not a gated count field, every row still carries a line number)

| # | Line(s) | Item | Detail | Flags |
|---|---|---|---|---|
| 1 | 42-48 | Digital signature block | Signatory: Abhishek Kapoor; Designation: Company Secretary & Compliance Officer; Timestamp: 2026.08.03 09:39:47 +05'30' | This is a Reg 30 cover letter signature, not a board-meeting-outcome signature — no board meeting start/end time is disclosed anywhere in this doctype (media release only), so the "signature before board meeting concluded" check (Rule 7) does not apply; noted as N/A rather than omitted |
| 2 | 16 | Release date | "August 03, 2026" | matches quote/dateline date (line 64, 90) |
| 3 | 18, 21-22 | Regulatory addressees | BSE Limited (Mumbai 400 001, Scrip Code 544645); National Stock Exchange of India Limited (Mumbai 400 051, SYMBOL: PARKHOSPS) | administrative, not a disclosure figure |
| 4 | 25-26 | Regulatory citation | "Regulation 30 of ... Listing Regulations, 2015" | administrative |
| 5 | 31-32 | Reporting period citation | "...quarter ended June 30, 2026." | matches detected_quarter in A1 header |
| 6 | 64-66 | Dateline / company description | "Gurugram, 3rd August 2026: Park Medi World Limited, North India's 2nd largest hospital chain..., (NSE: PARKHOSPS, BSE: 544645)..." | repeats scrip identifiers |
| 7 | 165-170 | IR / investor contact details | Park Medi World Limited (investor.relations@parkhospital.in); Adfactors Investor Relations (saloni.nagvekar@..., mansi.pasari@...) | administrative |

---

## TABLE 10 — DISTINCT NAMED ENTITIES (12)

| # | Entity | First line mentioned | Relationship / role | Flags |
|---|---|---|---|---|
| 1 | Park Medi World Limited | 40 | Issuer / reporting company | — |
| 2 | BSE Limited | 18 | Regulatory addressee (exchange) | — |
| 3 | National Stock Exchange of India Limited | 18 | Regulatory addressee (exchange) | — |
| 4 | Umkal Health Care Private Limited | 85 | Wholly owned subsidiary | operates Park Hospital, Palam Vihar |
| 5 | Park Hospital, Palam Vihar (Gurugram) | 86 | Existing flagship hospital (under Umkal Health Care) | subject of Park Platinum expansion |
| 6 | Park Platinum | 87 | New expansion brand name (100-bed addition at Palam Vihar) | — |
| 7 | The Medicity Hospital, Rudrapur | 82 | Acquisition target (definitive agreement signed) | valuation in INR crs; SUBSEQUENT_EVENT commissioning |
| 8 | Mehar Hospital, Zirakpur | 90 | Acquisition target (definitive agreement signed same day as release) | SAME_DAY_DISCLOSURE; valuation in INR crs |
| 9 | Panchkula (greenfield hospital) | 81 | Newly commissioned own-build facility | no distinct brand name given, referenced by location |
| 10 | Agra facility | 100 | Already-commissioned own facility (Feb 2026) | — |
| 11 | Febris multi-super-speciality hospital, Narela, Delhi | 101 | Upcoming own-build facility | not yet commissioned per narrative |
| 12 | Adfactors Investor Relations | 166 | External IR agency (contact point) | — |

Since no prior-quarter ledger was supplied for this run (prior-quarter ledger path: none), the `ENTITY_CHANGE` cross-check cannot be performed; this is noted rather than silently skipped.

Grep check: distinct-name pattern match across the document = 12 unique entity strings. Manual sweep = 12. Match.

---

## SUMMARY OF FLAGS RAISED (roll-up)

- UNIT_INCONSISTENCY — acquisition valuations and one FY26 reference figure stated in INR crs inside the narrative while the summary table and headline/highlights are in INR mn (lines 83, 88, 91).
- SUBSEQUENT_EVENT — Medicity Hospital, Rudrapur, disclosed as "commissioned on 2nd August 2026," i.e. after the June 30, 2026 quarter-end and one day before the August 3, 2026 release (line 84).
- SAME_DAY_DISCLOSURE — Mehar Hospital, Zirakpur, acquisition agreement dated "Today, on 3rd August 2026," the same date as the release itself (line 90).
- RESTATED — the 1,490-bed / c.46% / 3,250-bed CY2026 capacity-addition guidance is repeated verbatim three times (lines 60-61, 102-103, 132) and the 19%/20%/35% YoY headline growth trio is repeated across the preview box, highlights bullets, and quote.
- APPROX — approximation qualifiers "~86%", "~INR 245 crs" (line 88) and "c.46%" (lines 60, 102, 132, three occurrences).
- OPEN_ENDED — "150+ beds" capacity qualifier for Mehar Hospital (line 92), exact figure not disclosed.
- UNAUDITED — the entire results set is explicitly qualified as unaudited (lines 54, 65-66); caps any downstream verdict per pipeline NEVER-rule on unresolved evidence quality, propagate to A3/A4/A5.
- PAGE_FOOTER_GAP — the last extracted page carries no printed internal page number in the extract (page 4 / Table 1 row 4).
- Reconciliation note (not a flag, an observation for A3/A4): "About" section's "4,290 beds as on date" (line 140) does not tie out directly to the Q1FY27 closing 3,960-bed figure in the summary table (line 111); gap plausibly explained by post-quarter-end additions already disclosed in Growth Highlights, not resolved here.
- No `ZERO_STANDING`, `ENTITY_CHANGE`, `REPEAT_QUESTION`, `MGMT_ABSENCE`, or `DROPPED_SLIDE` flags apply: no zero/nil/dash line items exist in this release; no prior-quarter ledger was available for entity/slide-drop comparison; document is not a transcript (no questions/turns) and not a board-outcome letter (no agenda items).

---

```yaml
stage: A2-enumerator
company: "PARKHOSPS"
quarter: "Q1 FY27"
doctype: "release"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/ledger_release_parkhosps_q1fy27.md"
counts:
  notes: 10
  line_items: 55
  zero_standing: 0
  agenda_items: 65
  auditor_paras: 0
  entities: 12
  turns: 0
  questions: 0
  mgmt_numbers: 8
  slides: 4
  slide_numbers: 4
flags_raised: [UNIT_INCONSISTENCY, SUBSEQUENT_EVENT, SAME_DAY_DISCLOSURE, RESTATED, APPROX, OPEN_ENDED, UNAUDITED, PAGE_FOOTER_GAP]
gate_a2: pass
mismatch_note: ""
```
