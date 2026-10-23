# A2 COMPLETENESS LEDGER — GHVINFRA Q1 FY27 (results, Reg 30 media release)

Source: /home/user/inflection-pipeline/runs/ghvinfra-q1fy27/work/extract_results_ghvinfra_q1fy27.txt
(182-line A1 extract; 3-page SEBI Reg 30 media release, NOT a full Reg 33
statement — no Board Outcome letter, no standalone/consolidated financial
statements, no auditor's report were extracted because none exist in this
filing type.)

Method note: grep counts below use content-marker patterns (bullet glyphs,
numbered-list prefixes, colon-labelled headers, distinctive paragraph-opening
phrases, or explicit line ranges for the tabular block) rather than blank-line
block detection alone, because several adjacent disclosure units in this PDF
extraction are not separated by blank lines (e.g., the P&L table at
lines 93-98 runs directly into the following paragraph at line 99 with no
blank line; the three headline bullets at lines 84-91 are separated only by
the bullet glyph, not blank lines). Both grep and manual sweep target the
same underlying content-marker definition, so counts are directly comparable.

Non-disclosure artifacts excluded from all counts below (extraction header,
page-break markers, repeated logo/letterhead lines): lines 1-13 (A1 header),
15, 70, 124 (page markers), 72-73, 126-127 (logo/tagline repeats on pages 2-3).

=== A2 COUNT TEST ===
category: line_items (headline P&L table rows)             grep_count: 5   sweep_count: 5   match: yes
category: narrative_financial_metrics (metrics in prose, absent from table)  grep_count: 2   sweep_count: 2   match: yes
category: headline_bullets                                 grep_count: 3   sweep_count: 3   match: yes
category: narrative_paragraphs (body, non-tabular, non-list)  grep_count: 12  sweep_count: 12  match: yes
category: director_appointments (annexure-equivalent)      grep_count: 3   sweep_count: 3   match: yes
category: business_verticals (About section)               grep_count: 6   sweep_count: 6   match: yes
category: letter_metadata (Reg 30 cover-letter elements)   grep_count: 11  sweep_count: 11  match: yes
category: signature_block (digital signature, split by extraction blank line)  grep_count: 2   sweep_count: 2   match: yes
category: absence_flags (standard results-filing units confirmed absent)  grep_count: 15  sweep_count: 15  match: yes
category: zero_standing (table line items with a nil/dash value in either period)  grep_count: 0   sweep_count: 0   match: yes
category: notes (numbered notes to financial statements)   grep_count: 0   sweep_count: 0   match: yes  [see ABSENCE #3]
category: agenda_items (Board Outcome letter agenda)       grep_count: 0   sweep_count: 0   match: yes  [see ABSENCE #8]
category: auditor_paras                                    grep_count: 0   sweep_count: 0   match: yes  [see ABSENCE #7]
category: entities (consolidation entity list)             grep_count: 0   sweep_count: 0   match: yes  [see ABSENCE #13]
gate_a2: pass
total positive-count rows enumerated: 59
=== END COUNT TEST ===

---

## TABLE A — Cover-Letter / Reg 30 Filing Metadata (11 rows)

| # | Line(s) | Item | Content (first ~15 words) | Flags |
|---|---|---|---|---|
| A1 | 17-20 | Letterhead / company identity block | "GHV INFRA PROJECTS LIMITED... (Formerly known as Sindu Valley Technologies Limited)" | NAME_CHANGE — prior corporate identity, worth tracking for entity-continuity checks |
| A2 | 25 | Letter date | "Date: August 11, 2026" | DATE_DISCREPANCY vs. media-release dateline (line 99, "10th August 2026") — one day earlier |
| A3 | 27-31 | Addressee | "To, Department of Corporate Services, BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai – 400001" | — |
| A4 | 33-34 | Scrip identifiers | "SCRIP ID: GHVINFRA / SCRIP CODE: 505504" | — |
| A5 | 36-37 | Subject line / regulation cited | "Subject: Intimation of Media Release under Regulation 30 of the SEBI (LODR) Regulations, 2015" | — |
| A6 | 39 | Salutation | "Dear Sir/Madam," | — |
| A7 | 41-44 | Reg 30 compliance statement | "Pursuant to the Regulations 30 of the Securities and Exchange Board of India... please find enclosed a copy of Media release" | — |
| A8 | 46 | Closing instruction to exchange | "You are requested to kindly take the same on record." | — |
| A9 | 48-49 | Valediction | "Thanking you, Yours faithfully" | — |
| A10 | 61 | Enclosure line | "Encl: Media Release" | — |
| A11 | 66-68 | Registered office / contact / CIN | "Registered Office: A-511, 5th Floor, Kanakia Wall Street... CIN No.: L43900MH1976PLC457495" | — |

## TABLE B — Digital Signature Block (2 rows)

| # | Line(s) | Item | Content | Flags |
|---|---|---|---|---|
| B1 | 51-56 | Signing entity + digital signature stamp | "For GHV Infra Projects Limited (Formally known as Sindu Valley Technologies Limited); Digitally signed by Daksh Tulsibhai Mewada, Date: 2026.08.11 16:11:40 +05'30'" | Signed same calendar date as the letter (Aug 11) but one day after the media-release dateline (Aug 10) — see DATE_DISCREPANCY at A2 |
| B2 | 58-59 | Signatory name / designation | "Daksh Tulsibhai Mewada, Company Secretary & Compliance Officer" | No board-meeting start/end time exists in this filing to cross-check the signature timestamp against (see ABSENCE #9) |

## TABLE C — Headline P&L Table Line Items (5 rows, lines 93-98)

| # | Line | Particular | Q1FY27 | Q1FY26 | YoY% | Flags |
|---|---|---|---|---|---|---|
| C1 | 94 | Revenue from operations | 218.59 | 80.46 | 171.67% | Non-zero both periods |
| C2 | 95 | EBITDA | 28.05 | 8.35 | 235.93% | Non-zero both periods |
| C3 | 96 | EBITDA% | 12.83% | 10.38% | +245 bps | Non-zero both periods |
| C4 | 97 | PAT | 11.25 | 4.72 | 138.35% | Non-zero both periods |
| C5 | 98 | PAT% | 5.15% | 5.86% | -71 bps | Non-zero both periods |

No zero, nil, or dash-valued line items appear in the table in either period
— `zero_standing` count is genuinely 0, not a dropped row (checked both
columns of all 5 rows).

## TABLE D — Narrative-Only Financial Metrics, Absent From the Headline Table (2 rows)

| # | Line(s) | Metric | Content | Flags |
|---|---|---|---|---|
| D1 | 86-87, 110-111 | PBT | "PBT increases 145.73% YoY to Rs. 15.53 crore" (bullet, 86-87); "PBT also witnessed a robust 145.73% YoY increase to Rs. 15.53 crore from Rs. 6.32 crore" (narrative, 110-111) | TABLE_OMISSION — PBT is disclosed twice in prose with full YoY comparative but is not a row in the headline P&L table alongside Revenue/EBITDA/PAT |
| D2 | 112 | Diluted EPS | "Diluted EPS stood at Rs. 1.48 in Q1FY27." | TABLE_OMISSION, INCOMPLETE_COMPARATIVE — no Q1FY26 comparator or YoY% given for EPS, unlike every other headline metric |

## TABLE E — Headline Bullets (3 rows, lines 84-91)

| # | Line(s) | Content | Flags |
|---|---|---|---|
| E1 | 84-85 | "Revenue from Operations rises 171.67% YoY to Rs. 218.59 crore; PAT surges 138.35% YoY to Rs. 11.25 crore" | — |
| E2 | 86-87 | "EBITDA grows 235.93% YoY to Rs. 28.05 crore; PBT increases 145.73% YoY to Rs. 15.53 crore" | — |
| E3 | 88-91 | "Appoints Shri Manoj Aggarwal {Former MD of GIDC and GMDC}, Shri Dhanraj O. Tawade {Former NHAI Member (Technical)} and Shri Swarup Dasgupta (Former Executive Director-Bank of India) as Additional Independent Directors" | Malformed bracket punctuation in source ("{Former...)}") — transcription artifact, not a content flag |

## TABLE F — Narrative Body Paragraphs (12 rows)

| # | Line(s) | Opens with | Flags |
|---|---|---|---|
| F1 | 78 | "Media Release" (section label) | — |
| F2 | 80-82 | "GHV Infra Projects Reports Strong Q1FY27 Performance; EBITDA Records 235.93% YoY Growth" + sub-headline "Revenue from Operations increases 171.67% YoY, driven by strong execution momentum" | — |
| F3 | 99-106 | "Mumbai, 10th August 2026: GHV Infra Projects Limited (BSE: 505504)... reported strong business momentum during the quarter ended June 30, 2026" | Explicitly states "On a standalone basis" (line 101) — confirms results are standalone-only; see ABSENCE #1 |
| F4 | 108-112 | "The strong business momentum was further reflected in the Company's operating performance, with EBITDA more than tripling..." | Contains PBT and Diluted EPS figures — see TABLE D |
| F5 | 114-122 | "Mr. Ajay Hans, Managing Director, GHV Infra Projects Limited, said, 'The beginning of FY27 reflects the strength of our evolving business platform...'" | Management quote — MD only; no CFO or other management commentary present |
| F6 | 131-132 | "In a recent strategic development, GHV Infra Projects Limited strengthened its Board with the appointment of three eminent professionals..." | "recent" — no specific appointment/board-resolution date given; see ABSENCE #12 |
| F7 | 147-151 | "The appointments bring extensive expertise across public administration, infrastructure development, highways and transportation, banking, finance and corporate governance..." | — |
| F8 | 153-154 | "GHV Infra Projects Limited has been honoured with the 'Emerging Contractor of the Year' award at the RAHSTA Awards 2026." | Award mention, no further detail (awarding body, date of ceremony) given |
| F9 | 156-160 | "Going ahead, GHV Infra Projects Limited remains focused on strengthening its execution capabilities, expanding its presence across key infrastructure segments..." | Forward-looking / outlook language, qualitative only, no quantitative guidance |
| F10 | 162 | "About GHV Infra Projects Limited:" (section header) | — |
| F11 | 164-165 | "GHV Infra Projects Limited is a growing EPC turnkey construction company delivering complex, high-value projects across below verticals:" | — |
| F12 | 179-182 | "With an execution-driven approach, structured project management systems and Engineering expertise, GHV Infra is focused on delivering projects with quality, safety, precision and efficiency." | — |

## TABLE G — Director Appointments (annexure-equivalent, 3 rows, lines 134-145)

| # | Line(s) | Name | Role | Background (first ~15 words) | Flags |
|---|---|---|---|---|---|
| G1 | 134-137 | Shri Manoj Aggarwal | Additional Independent Director | "Retired IAS officer and Former Managing Director of GIDC and GMDC, with over 45 years of experience..." | No DIN given (ABSENCE #11); no term/effective date given (ABSENCE #12) |
| G2 | 138-141 | Shri Dhanraj O. Tawade | Additional Independent Director | "Former Member (Technical), National Highways Authority of India (NHAI), brings around 37 years of rich experience..." | Same as G1 |
| G3 | 142-145 | Shri Swarup Dasgupta | Additional Independent Director | "Former Executive Director of Bank of India, brings over four decades of distinguished experience in banking... currently serves as Advisor – Corporate Credit at Punjab & Sind Bank" | Same as G1; current outside role (Punjab & Sind Bank advisor) is a potential related-party/independence consideration for A3/A4, not adjudicated here |

## TABLE H — Business Verticals, "About" Section (6 rows, lines 167-177)

| # | Line(s) | Vertical | Content | Flags |
|---|---|---|---|---|
| H1 | 167 | Infrastructure | "EPC execution of roads, water and railway projects." | — |
| H2 | 168-169 | Industrial | "EPC execution and LSTK of Steel plant units, Refinery units and other manufacturing process plants." | — |
| H3 | 170-171 | Building | "EPC execution of residential, commercial, institutional buildings, factory buildings, Integrated townships along with required infrastructure etc." | — |
| H4 | 172-173 | Coastal Infrastructure | "EPC execution for jetties, berths, Ro-Ro, cruise infrastructure, marine connectivity through coastal roads and rail links." | — |
| H5 | 174-175 | Energy | "EPC execution of renewable and conventional energy infrastructure, including solar, wind and thermal power projects." | — |
| H6 | 176-177 | Data Centres | "Turnkey EPC execution of data centre including civil, MEP, utility integration, specialised infrastructure etc." | No revenue/order-book split is given across these six verticals — see ABSENCE #6 (segment reporting) |

## TABLE I — ABSENCE LEDGER: Standard Results-Filing Disclosure Units Not Present (15 rows)

Every item below was verified absent by keyword grep across the full 182-line
extract (0 hits, or hits confirmed as unrelated false positives — see grep
log: "Consolidated" 0, "Cash Flow" 0, "Balance Sheet" 0, "Limited Review" 0,
"Auditor" 0, "AGM" 0, "Record Date" 0, "Dividend" 0, "ESOP" 0, "Scrutinizer" 0,
"Statutory Auditor" 0, "Order Book" 0, "Quarter ended March" 0; "Segment" 3
hits all qualitative narrative usage, not a reporting table; "DIN" 9 hits all
substring false positives within other words, e.g. "building", "expanding").

| # | Absent unit | Note |
|---|---|---|
| I1 | Consolidated financial results | Only standalone basis reported (line 101 states so explicitly) |
| I2 | Full standalone P&L beyond the 5 headline metrics | No Other income, Total income, Total expenses, Finance costs, Depreciation & amortisation, Exceptional items, Tax expense, OCI, Total Comprehensive Income, EPS basic, paid-up equity capital, or Reserves in the table |
| I3 | Notes to financial results (numbered notes / accounting policy notes) | None present; only content resembling a numbered list is the director-appointment list (Table G), which is not a financial note |
| I4 | Cash Flow Statement | Absent |
| I5 | Balance Sheet / Statement of Assets and Liabilities | Absent |
| I6 | Segment-wise revenue / results / capital-employed table | Only qualitative vertical descriptions (Table H); no figures allocated by segment |
| I7 | Auditor's Limited Review Report (opinion type, EOM, Other Matters, Going Concern, UDIN, entities reviewed) | Absent — this is a media release, not the Reg 33 statement it summarizes |
| I8 | Board Outcome letter / meeting agenda items (AR approval, AGM notice, record date, dividend declaration, auditor appointment/change, scrutinizer appointment, ESOP grants, capital-raising enabling resolutions) | Absent — no Board Outcome letter was extracted; only a Reg 30 media-release intimation |
| I9 | Board meeting start/end time | Absent — cannot cross-check digital signature timestamp (line 53-56) against meeting conclusion time per standard practice |
| I10 | Sequential / QoQ comparison (vs. Q4FY26) | Only YoY (vs. Q1FY26) comparison given throughout |
| I11 | DIN (Director Identification Number) for the 3 newly appointed Additional Independent Directors | Absent for all three (Table G) |
| I12 | Effective date / board-resolution date of the three director appointments | Only "recent strategic development" (line 131) given, no specific date |
| I13 | Consolidation / subsidiary entity list with relationship type | Absent — no subsidiaries, associates, or JVs named anywhere in the extract despite the standalone-basis statement |
| I14 | Order book / backlog quantitative figures | Only qualitative "project pipeline" language (line 118-119); no number given |
| I15 | Diluted EPS prior-year (Q1FY26) comparator and YoY% | EPS given only as a single Q1FY27 figure (line 112), unlike every other headline metric which carries both periods and a YoY% |

---

## SUMMARY OF FLAGS RAISED

- NAME_CHANGE — company formerly Sindu Valley Technologies Limited (A1)
- DATE_DISCREPANCY — media-release dateline (10-Aug-2026, line 99) precedes
  the BSE intimation letter date and digital-signature date (11-Aug-2026,
  lines 25, 53-56) by one day (A2, B1)
- TABLE_OMISSION — PBT and Diluted EPS disclosed in prose but excluded from
  the headline P&L table (D1, D2)
- INCOMPLETE_COMPARATIVE — Diluted EPS has no prior-period comparator or
  YoY% (D2, I15)
- Multiple ABSENCE flags (I1-I15) — this filing is structurally a Reg 30
  media release, not a Reg 33 financial-results statement or Board Outcome
  letter; the entire standard results-filing disclosure architecture
  (consolidated results, notes, cash flow, balance sheet, segment reporting,
  auditor's report, Board Outcome agenda items) is absent by document type,
  not by omission within a filing that should contain them — A3/A4 should
  treat these as a completeness ceiling on this doctype, not as company-level
  red flags, unless the underlying Reg 33 statement (not provided to this
  pipeline run) is separately checked and found to also omit them.
