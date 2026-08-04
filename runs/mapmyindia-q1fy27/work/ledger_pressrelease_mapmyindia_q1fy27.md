# A2 ENUMERATOR LEDGER — MapmyIndia (MAPMYINDIA) Q1 FY27 — Press Release

Source: `extract_pressrelease_mapmyindia_q1fy27.txt` (6-page covering letter +
press release; unit convention Rs Cr; no OCR pages, 100% page coverage).
Doctype handled under presentation-class discipline per task injection:
financial highlights table rows, operational/business metrics, and
management quotes are the three mandated enumeration axes; a fourth
"structural/ancillary" sweep is added so no disclosure unit on the page is
dropped (covering letter, headers, boilerplate, disclaimer). All line
numbers are absolute lines in the extract file as read.

```
=== A2 COUNT TEST ===
category: line_items        grep_count: 7    sweep_count: 7    match: yes
category: operational_metrics grep_count: 29  sweep_count: 29   match: yes
category: quote_paragraphs  grep_count: 5    sweep_count: 5    match: yes
category: structural_units  grep_count: 21   sweep_count: 21   match: yes
not_applicable_categories: notes, agenda_items, auditor_paras, entities,
  turns, questions, slides — this doctype is a covering letter + press
  release, not a board-outcome filing, concall transcript, or slide deck;
  no rows of those types exist to enumerate.
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology per category, for reconciliation audit:
- line_items: `sed -n '102,111p' extract | grep -n -E "^\s+[A-Z]"` → 9 hits,
  minus 2 header/sub-header lines ("Particulars (Rs Cr)…", "FY27 FY26
  Growth") = 7 data rows.
- operational_metrics: `grep -oE "[0-9]+\.?[0-9]*%|Rs [0-9]+\.?[0-9]*"` on
  the headline block (7 hits) + `grep -oE "[0-9]+\.?[0-9]*%|₹[0-9]+\.?[0-9]*"`
  on the quote-para-1 block (7 hits) + targeted greps for dates (4),
  durations (2), scale claims (3), BSE/NSE identifiers (4 = 2 identifiers x
  2 occurrences), CIN + CMMI/ISO certification (2) = 29. Cross-checked
  against a full-document digit sweep (`grep -n -E "[0-9]"` on the entire
  body) that surfaced no unaccounted metric lines beyond postal codes,
  phone number and street-address digits, which are administrative, not
  business metrics, and are folded into structural unit S1/S6 instead.
- quote_paragraphs: topic-start phrase grep inside lines 115-183 (`said
  "We began`, `As our business evolves`, `This quarter also marks`, `When
  it comes to AI`, `It is important to re-emphasise`) → 5 hits, matching
  the 5 topical paragraphs identified by manual read.
- structural_units: grep of 21 block-opening anchor phrases (letter
  addressee block, subject line, body, signatory, enclosure, footer/CIN,
  headline, dateline, section headers, quote attribution line, business
  description, product-delivery bullet, industries-served bullet,
  revenue-model bullet, segment-reporting-change header, AEG detailed
  definitions, About MapmyIndia header, consumer-products paragraph,
  separator, contact block, FLS disclaimer) → 21 hits, matching manual
  sweep.

---

## TABLE 1 — FINANCIAL HIGHLIGHTS TABLE, LINE ITEMS (lines 99-111)

Header row: `Particulars (Rs Cr) | Q1 FY27 | Q1 FY26 | YoY Growth | FY26`
(lines 102-103).

| # | Line(s) | Line item | Q1 FY27 | Q1 FY26 | YoY Growth | FY26 | Flags |
|---|---------|-----------|---------|---------|------------|------|-------|
| 1 | 104 | Revenue from Operations | 139.7 | 121.6 | 14.9% | 474.1 | |
| 2 | 105 | Total Income | 159.4 | 135.3 | 17.8% | 526.5 | |
| 3 | 106 | EBITDA | 56.1 | 55.9 | 0.4% | 175.5 | |
| 4 | 107 | EBITDA Margin | 40.2% | 45.9% | (blank cell) | 37% | BLANK_CELL |
| 5 | 108 | PAT | 49.7 | 45.8 | 8.6% | 134 | |
| 6 | 109 | PAT Margin | 31.2% | 33.9% | (blank cell) | 25.5% | BLANK_CELL |
| 7 | 110-111 | Cash & Cash Equivalents including financial investments | 745.3 | 676.9 | (blank cell) | 685.0 | BLANK_CELL |

BLANK_CELL = the YoY Growth column is left empty in the source table for
this row (no dash or "NA" printed, simply blank whitespace between the two
adjacent columns) — a genuine disclosure gap, recorded verbatim, not
interpreted. No row in this table is ZERO_STANDING (no line item is
zero/nil/dash across all periods); zero_standing count = 0.

---

## TABLE 2 — OPERATIONAL / BUSINESS METRIC MENTIONS (29 rows, every
numeric or dated business fact stated in prose, INCLUDING restatements of
Table-1 figures in the headline and in the Chairman's quote — each
separate textual occurrence is its own row so downstream stages can check
cross-document consistency)

| # | Line(s) | Snippet (verbatim) | Value | Cross-ref | Flags |
|---|---------|---------------------|-------|-----------|-------|
| 1 | 88 | "Revenue up 14.9% YoY" | 14.9% | Table1 row1 (L104) | DUPLICATE_OF_TABLE |
| 2 | 88 | "to Rs 139.7 Cr" | 139.7 | Table1 row1 (L104) | DUPLICATE_OF_TABLE |
| 3 | 89 | "EBITDA at Rs 56.1 Cr" | 56.1 | Table1 row3 (L106) | DUPLICATE_OF_TABLE |
| 4 | 89 | "EBITDA margin at 40.2%" | 40.2% | Table1 row4 (L107) | DUPLICATE_OF_TABLE |
| 5 | 89 | "PAT up 8.6% to" | 8.6% | Table1 row5 (L108) | DUPLICATE_OF_TABLE |
| 6 | 91 | "Rs 49.7 Cr" | 49.7 | Table1 row5 (L108) | DUPLICATE_OF_TABLE |
| 7 | 91 | "PAT margin at 31.2%" | 31.2% | Table1 row6 (L109) | DUPLICATE_OF_TABLE |
| 8 | 23 | "August 04, 2026" (letter date) | 4 Aug 2026 | cross-ref row9 | |
| 9 | 94 | "New Delhi, India, 4th Aug 2026" (release dateline) | 4 Aug 2026 | cross-ref row8 | |
| 10 | 96-97 | "financial results for the First Quarter of FY2027 ended June 30th 2026" | 30 Jun 2026 | | |
| 11 | 117 | "Revenue from Operations grew 15% year-on-year" | 15% | Table1 row1 (L104 = 14.9%) | FIGURE_VARIANT |
| 12 | 117-118 | "to ₹139.7 crore" | 139.7 | Table1 row1 (L104) | DUPLICATE_OF_TABLE |
| 13 | 118 | "EBITDA remained strong at ₹56.1 crore" | 56.1 | Table1 row3 (L106) | DUPLICATE_OF_TABLE |
| 14 | 118 | "EBITDA margin at 40.2%" | 40.2% | Table1 row4 (L107) | DUPLICATE_OF_TABLE |
| 15 | 119 | "PAT increased 8.6% YoY" | 8.6% | Table1 row5 (L108) | DUPLICATE_OF_TABLE |
| 16 | 119 | "to ₹49.7 crore" | 49.7 | Table1 row5 (L108) | DUPLICATE_OF_TABLE |
| 17 | 119 | "PAT margin at 31.2%" | 31.2% | Table1 row6 (L109) | DUPLICATE_OF_TABLE |
| 18 | 137 | "appointment of Rohan Verma as Joint Managing Director… effective 1st July 2026" | 1 Jul 2026 | | |
| 19 | 160 | "We have been using AI for the last 5+ years" | 5+ years | | |
| 20 | 169 | "we have spent the last 30+ years continuously envisioning" | 30+ years | | |
| 21 | 30 | "BSE SCRIP Code: 543425" (cover letter) | 543425 | cross-ref row26 | |
| 22 | 30 | "NSE Symbol: MAPMYINDIA" (cover letter) | MAPMYINDIA | cross-ref row25 | |
| 23 | 306 | "served more than 2000 B2B and B2B2C customers since inception" | 2000+ | | |
| 24 | 308 | "pioneered digital mapping in India in 1995" | 1995 | | |
| 25 | 299 | "(NSE: MAPMYINDIA; BSE: 543425)" — NSE symbol | MAPMYINDIA | cross-ref row22 | |
| 26 | 299 | "(NSE: MAPMYINDIA; BSE: 543425)" — BSE code | 543425 | cross-ref row21 | |
| 27 | 322 | "integrated global maps for over 200 countries" | 200+ | | |
| 28 | 78 | "CIN: L74899DL 1995PLC065551" (footer) | CIN no. | | |
| 29 | 78 | "A CMMl-3 & ISO Certified Company" (footer, certification claim) | CMMI-3 + ISO | | |

Postal codes (Mumbai 400 001 / 400 051, line 16 orig), phone number
(+91-011-4600 9900, line 78) and street address digits (237, Okhla
Industrial Estate…, line 77) were swept and found to be administrative
identifiers, not business/operational metrics; they are folded into
structural units S1 and S6 in Table 4 rather than given their own metric
row, to keep this table's grep/sweep reconciliation clean.

---

## TABLE 3 — MANAGEMENT QUOTE (single quotation, lines 115-183, one
speaker; broken into topical paragraph sub-units for traceability since it
runs 69 lines and covers five distinct topics)

Attribution line: **113** — "Rakesh Verma, Chairman & Managing Director,
MapmyIndia, commenting on the Q1 FY27 results, said" — quote opens with a
curly open-quote at line 115, closes with a curly close-quote at line 183;
no other quotation marks interrupt it, confirmed by full-document
quotation-mark grep, so this is mechanically ONE quote from ONE speaker.

| # | Sub-unit | Line(s) | First ~15 words | Topic | Flags |
|---|----------|---------|------------------|-------|-------|
| QT1 | Full quote (parent unit) | 115-183 | "We began FY2027 with another quarter of profitable growth while continuing our evolution…" | Entire CMD statement | |
| QT1-P1 | Paragraph 1 | 115-122 | "We began FY2027 with another quarter of profitable growth while continuing our evolution…" | Q1 FY27 results recap (Revenue/EBITDA/PAT/margins) | |
| QT1-P2 | Paragraph 2 | 125-134 | "As our business evolves, to help investors and analysts understand our business better…" | Segmental revenue reporting change (A&M/C&E → Automotive/Enterprise/Government) | DUPLICATE_CONTENT (near-identical text restated outside the quote at lines 253-262, see S17 in Table 4) |
| QT1-P3 | Paragraph 3 | 135-138, 152-156 | "This quarter also marks an important milestone in our leadership journey with the appointment of Rohan Verma…" | Rohan Verma appointed Joint MD effective 1 Jul 2026, subject to shareholder approval | PAGE_SPAN (paragraph is split by the page-2/page-3 break at line 144; text is continuous, no content lost) |
| QT1-P4 | Paragraph 4 | 158-167 | "When it comes to AI, which is causing a paradigm shift and technological revolution…" | AI capability narrative, 5+ years of AI use, AI-native push | |
| QT1-P5 | Paragraph 5 | 169-183 | "It is important to re-emphasise that we have spent the last 30+ years continuously envisioning…" | 30+ year legacy, moat, flywheel framing | |

quote count (distinct speakers/quotations) = 1; paragraph sub-units = 5.

---

## TABLE 4 — STRUCTURAL / ANCILLARY DISCLOSURE UNITS (21 rows; covering
letter, headers, boilerplate, disclaimer — everything on the page that is
not a Table-1 row, Table-2 metric, or Table-3 quote paragraph)

| # | ID | Line(s) | Content | Flags |
|---|----|---------|---------|-------|
| 1 | S1 | 25-30 | Covering letter addressee block: BSE Limited (Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai 400 001, Scrip Code 543425) and National Stock Exchange of India Ltd (Exchange Plaza, BKC, Mumbai 400 051, Symbol MAPMYINDIA), both Listing Departments | |
| 2 | S2 | 34 | Subject line: "Submission of Press Release for Q1FY2027 Results" | |
| 3 | S3 | 36-44 | Letter body: salutation "Dear Sir / Madam", "Please find attached herewith Press Release for Q1FY2027 Results", "Kindly acknowledge the receipt of the same", closing "Thanking you. Yours faithfully, For C.E. Info Systems Limited" | |
| 4 | S4 | 52-53 | Signatory block: Saurabh Surendra Somani, Company Secretary & Compliance Officer | |
| 5 | S5 | 55-56 | Enclosure list: "Encl: Press Release" | |
| 6 | S6 | 75-78 | Company footer/registration block: C.E. INFO SYSTEMS LIMITED (previously C.E. Info Systems Pvt Ltd), registered address 237 Okhla Industrial Estate Phase-III New Delhi-110020, website/e-mail/phone contacts, CIN, CMMI-3 & ISO certification (numeric content of this block cross-referenced as Table-2 rows 28-29) | |
| 7 | S7 | 88-91 | Press release headline sentence (numeric content cross-referenced as Table-2 rows 1-7) | |
| 8 | S8 | 94-97 | Dateline + opening sentence: "New Delhi, India, 4th Aug 2026: C.E. Info Systems Ltd. ("MapmyIndia")… announced today its financial results for the First Quarter of FY2027 ended June 30th 2026" | |
| 9 | S9 | 99 | Section header: "Key Consolidated Financial Highlights for Q1 of FY2027:" | |
| 10 | S11 | 113 | Quote attribution line (see Table 3 QT1) | |
| 11 | S13 | 186-209 | "Our Business Description" header + Map-led / IoT-led product taxonomy (Maps, Navigation, Analytics & BI, GIS & Digital Twins, Workflow/Workforce Automation; IoT Hardware, SaaS for Mobility/Logistics/Industrial) | |
| 12 | S14 | 220-230 | "For every industry, we can deliver…" — off-the-shelf products, modular platforms, APIs/SDKs, end-to-end solutions (named: Mappls Auto NCASE, Mappls Pro, Mappls BFI, Mappls Gov, Mappls Defence, Mappls Oil & Gas), OEM & FDE/Systems Integration positioning | |
| 13 | S15 | 231-241 | "We serve multiple industries…" — Automotive / Enterprise / Government customer groupings, multiple-use-case framing | |
| 14 | S16 | 243-250 | "We earn revenue in the following manner" — Product Licensing & Subscriptions (MaaS/SaaS/PaaS), Device Sales & DaaS, Solutions/Services/SI delivery, per-vehicle/per-API/per-user/per-solution pricing | |
| 15 | S17 | 253-262 | "Market-wise segmental revenue reporting transitioning to AEG" section header + non-quoted restatement of the segment-reporting-change explanation | DUPLICATE_CONTENT (near-identical to QT1-P2, lines 125-134) |
| 16 | S18 | 264-294 | Detailed AEG segment definitions: Automotive (OEMs across 4W/2W/3W/large vehicles, ICE/EV, aftermarket), Enterprise (private sector ex-Automotive: new-age tech, e-comm/q-comm, consumer internet, mobility/logistics, manufacturing, BFSI, FMCG, retail, energy, telecom, healthcare, hospitality, real estate, SMEs), Government (Central/State/Local, Defence/Armed Forces/Police, National Mapping Agencies, Railways, PSUs) | |
| 17 | S19 | 295-331 | "About MapmyIndia (C.E. Info Systems Ltd) & Mappls" boilerplate: company description, MaaS/SaaS/PaaS positioning, moat narrative, map product description (2D/3D/4D/HD/RealView, 200+ countries) (numeric content cross-referenced as Table-2 rows 23-27) | |
| 18 | S20 | 348-355 | Consumer products description: Mappls App (free, web + downloadable) and Mappls Gadgets (vehicle trackers, dash cameras, navi-tainment systems) | |
| 19 | S21 | 357 | Section separator "***" | |
| 20 | S22 | 360-363 | Contact block: Media Contact (pr@mapmyindia.com), Investor Relations (investor.relations@mapmyindia.com) | |
| 21 | S23 | 365-374 | Forward-looking-statements disclaimer: standard FLS boilerplate, no obligation to update, lists risk factors (competition, growth, pricing environment, recruitment/retention, technology, wage inflation, law/regulatory policies) | |

---

## FLAG SUMMARY

- **BLANK_CELL** (3 instances, Table 1 rows 4, 6, 7 / lines 107, 109,
  110-111): the YoY Growth column is left blank for EBITDA Margin, PAT
  Margin, and Cash & Cash Equivalents — the source table shows a growth %
  for every value-type row but not for these three.
- **FIGURE_VARIANT** (1 instance, Table 2 row 11 / line 117): the
  Chairman's quote states revenue "grew 15% year-on-year" while the
  financial highlights table (line 104) and the headline (line 88) both
  state 14.9%. Recorded as a fact for A3/A5 arithmetic-consistency review;
  not interpreted here.
- **DUPLICATE_CONTENT** (1 pair, Table 3 QT1-P2 lines 125-134 and Table 4
  S17 lines 253-262): the segmental-revenue-reporting-change explanation
  is stated twice, once inside the Chairman's quote and once again as
  unquoted body text.
- **PAGE_SPAN** (1 instance, Table 3 QT1-P3 lines 135-138 + 152-156): the
  Rohan Verma appointment paragraph is split by the page-2/page-3 break;
  noted for completeness, no text is missing across the break (confirmed
  lines 139-151 are blank/page-break formatting only).

No ZERO_STANDING line items exist in Table 1 (all 7 rows carry real
values in every period column). No ENTITY_CHANGE, MGMT_ABSENCE,
REPEAT_QUESTION, or DROPPED_SLIDE applicable — this doctype has no
consolidation-entity list, no concall participants, no repeated analyst
questions, and no prior-quarter slide deck to diff against (this is a
press release, and no prior-quarter press-release ledger was supplied at
the injected PRIOR_LEDGER_PATH).
