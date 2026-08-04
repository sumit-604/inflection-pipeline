# A2 ENUMERATOR LEDGER — MAPMYINDIA (C.E. Info Systems Ltd) — Q1 FY27 — Investor Presentation

Source: /home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/extract_presentation_mapmyindia_q1fy27.txt
17 pages / 17 formfeeds / 797 lines. Enumeration only — no interpretation.

Prior-quarter ledger: not supplied in injected inputs (`{{PRIOR_LEDGER_PATH}}` not provided). DROPPED_SLIDE
comparison cannot be run this cycle — flagged `PRIOR_LEDGER_UNAVAILABLE`, not a pass/fail finding.

```
=== A2 COUNT TEST ===
category: slides              grep_count: 17   sweep_count: 17   match: yes
category: line_items          grep_count: 30   sweep_count: 30   match: yes
category: zero_standing       grep_count: 3    sweep_count: 3    match: yes
category: notes               grep_count: 4    sweep_count: 4    match: yes
category: chart_data_labels   grep_count: 60   sweep_count: 60   match: yes
category: narrative_numbers   grep_count: 32   sweep_count: 32   match: yes
category: toc_items           grep_count: 7    sweep_count: 7    match: yes
category: governance_items    grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method notes (mechanical):
- `slides`: grep `^\[page [0-9]+\]` markers (line 17–736) = 17; manual sweep of formfeed_count in A1 header = 17.
- `line_items`: manual row count across the 6 structured tables in the deck (Consolidated Financial
  Highlights=7, Product-wise Map-led/IoT-led=5, Segmental Revenue Trend FY25=4, Segmental Revenue
  Trend FY26=4, Segmental Revenue Distribution/Mix Q1FY27=4, Top Non-Promoter Shareholders=6);
  grep cross-check via row-label anchors on each table's line range, same total.
- `chart_data_labels`: grep on each of the 5 `[CHART...]` lines (512, 557, 601, 645, 690), numeric
  tokens after stripping quarter/FY-period fragments (`Q1FY27`, `FY2026` etc., which are axis
  category labels, not data values) and, on line 690 only, stripping the restated non-promoter
  holder table (already counted once under `line_items`) — 15+10+14+14+7 = 60; manual re-read of
  each CHART annotation's "gridline/data/slice-value/growth-callout" sub-lists = 60, same total.
- `narrative_numbers`: grep on the identified prose/bullet lines (182,184,186 / 225,235 / 273,278,
  280,282,284,286,291 / 417,419,421,423 / 526 / 570 / 614) after stripping quarter-fragments =
  7+2+12+8+1+1+1 = 32; manual re-read of the same sentences, same total.
- `notes`: grep `-iE "note[ –:]|disclaimer"` on deck body (lines 17–777) hits lines 296, 688, 690
  (690 duplicates 688 — the "As on June 30, 2026" note restated inside the CHART annotation, not a
  4th distinct note), 696 → 3 grep-hit lines resolving to 4 distinct note/disclaimer units (line 296
  contains two numbered notes: EBITDA Margin formula and PAT Margin formula) = 4; manual sweep = 4.
- `toc_items`: manual count of non-blank list lines on the Table of Contents (page 3, lines 146–157,
  excluding the "Q1 FY2027" cover title and "Performance" section label) = 7; grep of the same line
  range for text lines with >2 words and no numeric content = 7.
- `governance_items`: manual sweep of forward-commitment / disclosure-policy statements outside the
  standard financial tables (Joint MD appointment, segmental-framework change, forward-looking
  disclaimer, Government-seasonality statement) = 4; grep `-iE "appoint|reporting framework|forward
  looking|seasonally weakest"` on deck body = 4 line hits, same total.

---

## TABLE 1 — SLIDES ENUMERATED (17/17)

| # | Page marker line | Title (as shown) | Content type | Flags |
|---|---|---|---|---|
| 1 | 17 | BSE/NSE Regulation 30 cover letter (Submission of Investor Presentation for Q1FY2027 Results) | text / regulatory cover letter | — |
| 2 | 83 | MapmyIndia / C.E. Info Systems Ltd — Investor Presentation — Q1FY2027 — August 2026 (deck cover/title) | text / title slide | — |
| 3 | 126 | Q1 FY2027 Performance — Table of Contents | text / list (7 entries, see Table 7) | — |
| 4 | 169 | Management Commentary (1/2) | text / narrative (quoted commentary begins) | — |
| 5 | 212 | Management Commentary (2/2) | text / narrative (quote continues, attributed to Rakesh Verma) | — |
| 6 | 255 | Consolidated Financial Highlights (Q1FY27) | table (7 line items) + bullet commentary | ZERO_STANDING x2 (see Table 2) |
| 7 | 298 | Our Business Description: Multi-Product, Multi-Industry, Multi-Use Case ... Company (1/2) | text / bulleted list, no figures | — |
| 8 | 341 | Our Business: ... (2/2) | text / bulleted list, no figures | — |
| 9 | 384 | Product-wise Highlights: Map-led and IoT-led | table (5 line items) + bullet commentary | ZERO_STANDING x1 (see Table 2) |
| 10 | 427 | Market-wise segmental revenue reporting transitioning to Automotive, Enterprise and Government (AEG) | text / explanatory (methodology change) | SEGMENT_FRAMEWORK_CHANGE |
| 11 | 470 | Annual and Quarterly revenue trends (Market-wise – New framework) | 3 tables (12 line items) + 1 combo bar/donut chart | — |
| 12 | 514 | Market-wise Revenue: Automotive | bullet text + bar chart | — |
| 13 | 559 | Market-wise Revenue: Enterprise | bullet text + bar chart | — |
| 14 | 603 | Market-wise Revenue: Government | bullet text + bar chart | — |
| 15 | 647 | Shareholding Pattern | table (6 named holders) + donut/pie chart(s) | — |
| 16 | 692 | Annexures — Disclaimer | text / full-page legal disclaimer | — |
| 17 | 736 | Thank You — Contact details | text / IR & Company Secretary contact info | — |

Slide count test: 17 slides enumerated, 17 page markers in extract, 17 = pdfinfo page_count and
formfeed_count from A1 header. Reconciled.

---

## TABLE 2 — FINANCIAL / SEGMENTAL / SHAREHOLDING LINE ITEMS (30/30)

### 2A. Consolidated Financial Highlights (Q1FY27) — Slide 6, table header line 271

| Line item | Line # | Q1FY27 | Q1FY26 | YoY Growth | FY26 | Flags |
|---|---|---|---|---|---|---|
| Total Income | 274 | 159.4 | 135.3 | 17.8% | 526.5 | — |
| Revenue from Operations | 276 | 139.7 | 121.6 | 14.9% | 474.1 | — |
| EBITDA | 279 | 56.1 | 55.9 | 0.4% | 175.5 | — |
| EBITDA Margin (%) [note 1] | 281 | 40.2% | 45.9% | (blank/dash) | 37% | ZERO_STANDING (YoY cell dash-valued) |
| PAT | 283 | 49.7 | 45.8 | 8.6% | 134.0 | — |
| PAT Margin (%) [note 2] | 285 | 31.2% | 33.9% | 17.8% | 25.5% | verbatim as extracted; YoY figure (17.8%) is identical to the Total Income YoY figure on this same table — carried as-is, not normalized/interpreted |
| Cash & cash equivalents (including financial instruments) | 288–289 | 745.3 | 676.9 | (blank/dash) | 685.0 | ZERO_STANDING (YoY cell dash-valued) |

### 2B. Product-wise Highlights: Map-led and IoT-led — Slide 9, table header lines 393–396

| Line item | Line # | Total Q1FY27 | Map-led Q1FY27 | Map-led Q1FY26 | IoT-led Q1FY27 | IoT-led Q1FY26 | Flags |
|---|---|---|---|---|---|---|---|
| Revenue from Operations | 399 | 139.7 | 98.7 | 98.2 | 41.1 | 23.4 | — |
| Sale of Hardware | 401 | 23.1 | 0 | 0 | 23.0 | 7.1 | ZERO_STANDING (Map-led column nil both periods — hardware sales structurally absent from the Map-led product line) |
| Sale of services | 404 | 116.6 | 98.7 | 98.2 | 18.0 | 16.3 | — |
| EBITDA | 406 | 56.1 | 50.7 | 53.8 | 5.4 | 2.0 | — |
| EBITDA Margin (%) | 408 | 40.2% | 51.4% | 54.8% | 13.1% | 8.7% | — |

### 2C. Segmental Revenue Trend — FY25 quarterly (Slide 11, table header line 480)

| Customer segment | Line # | Q1FY25 | Q2FY25 | Q3FY25 | Q4FY25 | Total FY25 | Flags |
|---|---|---|---|---|---|---|---|
| Automotive | 482 | 25.7 | 67.1 | 44.6 | 44.2 | 181.7 | — |
| Enterprise | 483 | 56.2 | 21.0 | 36.1 | 64.8 | 178.2 | — |
| Government | 485 | 19.6 | 15.5 | 33.8 | 34.5 | 103.4 | — |
| Grand Total | 486 | 101.5 | 103.7 | 114.5 | 143.5 | 463.3 | — |

### 2D. Segmental Revenue Trend — FY26 quarterly (Slide 11, table header line 489)

| Customer segment | Line # | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Total FY26 | Flags |
|---|---|---|---|---|---|---|---|
| Automotive | 490 | 45.7 | 46.9 | 47.9 | 49.2 | 189.8 | — |
| Enterprise | 492 | 60.6 | 22.9 | 29.2 | 61.7 | 174.4 | — |
| Government | 493 | 15.3 | 44.0 | 17.1 | 33.5 | 109.9 | — |
| Grand Total | 494 | 121.6 | 113.8 | 94.3 | 144.4 | 474.1 | — |

### 2E. Segmental Revenue Distribution/Mix Q1FY27 (Slide 11, table header line 501)

| Customer segment | Line # | Q1FY27 (Cr) | %age mix | Flags |
|---|---|---|---|---|
| Automotive | 503 | 58.8 | 42.1% | — |
| Enterprise | 504 | 64.2 | 46.0% | — |
| Government | 506 | 16.7 | 11.9% | — |
| Grand Total | 507 | 139.7 | 100% | — |

### 2F. Top Non-Promoter Shareholders (Slide 15, table header line 661)

| Holder | Line # | % Holding | Flags |
|---|---|---|---|
| Phonepe Private Limited | 665 | 13.7% | — |
| Tata Mutual Fund – Tata Small Cap Fund | 667 | 5.1% | — |
| Zenrin Co. Ltd | 670 | 3.4% | — |
| ICICI Prudential | 673 | 3.2% | — |
| Franklin India Opportunities Fund | 676 | 1.2% | — |
| Motilal Oswal Large Cap Fund | 679 | 0.5% | — |

Line-item total: 7 + 5 + 4 + 4 + 4 + 6 = 30. ZERO_STANDING flags: 3 (row 2A EBITDA Margin YoY dash,
row 2A Cash & cash equivalents YoY dash, row 2B Sale of Hardware Map-led both periods nil).

---

## TABLE 3 — CHART DATA LABELS (60/60), all flagged `[CHART...]` in A1 extract

| Chart | Slide | Line # | Labels enumerated | Flags |
|---|---|---|---|---|
| Segmental Revenue Distribution/Mix — quarterly + yearly trend (bar+donut combo) | 11 | 512 | Quarterly cluster: 26, 20, 15, 17, 46, 59, 61, 56, 64, 182, 190, 178, 174 (13 labels); Yearly cluster: 103, 110 (2 labels) = 15 labels | A1 flags this chart's OCR text-layer labels as partially intermixed/ambiguous between the quarterly and yearly series; authoritative source values are Tables 2C/2D/2E above, on the same slide |
| Automotive revenue bar chart | 12 | 557 | Gridlines: 65, 60, 55, 50, 45, 40, 35 (7); data label: 45.7 (Q1FY26); ambiguous label: 59; growth callout: 29% = 10 labels | one gridline value (59) flagged by A1 as possibly mislabeled by OCR, not confirmed as a genuine bar data label |
| Enterprise revenue bar chart | 13 | 601 | Gridlines: 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50 (11); data label: 60.6 (Q1FY26); ambiguous label: 64; growth callout: 6% = 14 labels | 64 flagged ambiguous (near-gridline placement) |
| Government revenue bar chart | 14 | 645 | Gridlines: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10 (11); data label: 15.3 (Q1FY26); ambiguous label: 17; growth callout: 11% = 14 labels | 17 flagged ambiguous (near-gridline placement) |
| Shareholding category mix donut/pie | 15 | 690 | Slice value labels: 15.1, 1.5, 18.1, 51.4, 1.1, 0.9, 11.9 = 7 labels (7 legend categories: Promoters, MF's/AIF's, Insurance Companies, Others, Corporate Bodies, FPI, Public — slice-to-category mapping not stated in source, not assigned here) | named non-promoter holder % values on this same chart annotation are the Table 2F values restated — not re-counted here to avoid double counting |

Chart data label total: 15 + 10 + 14 + 14 + 7 = 60.

---

## TABLE 4 — NARRATIVE / COMMENTARY NUMERIC DISCLOSURES (32/32)

Numbers stated in prose/bullet text on a slide, outside the structured tables of Table 2 and outside
the chart annotations of Table 3 (same headline figures often recur here in sentence form — each
recurrence is a separate disclosure instance per slide and is enumerated, not deduplicated against
Table 2/3).

| Slide | Line # | Value(s) | Context (first words) | Flags |
|---|---|---|---|---|
| 4 | 182 | 15%, ₹139.7 (cr) | "Revenue from Operations grew 15% year-on-year to ₹139.7" | — |
| 4 | 184 | ₹56.1 (cr), 40.2%, 8.6%, ₹49.7 (cr) | "EBITDA remained strong at ₹56.1 crore with EBITDA margin at 40.2%..." | — |
| 4 | 186 | 31.2% | "at 31.2%. Our performance reflects..." | — |
| 5 | 225 | 5+ (years) | "We have been using AI for the last 5+ years..." | non-precise magnitude, carried verbatim |
| 5 | 235 | 30+ (years) | "we have spent the last 30+ years continuously envisioning..." | non-precise magnitude, carried verbatim |
| 6 | 273 | 14.9%, ₹139.7 (Cr) | "operations grew by 14.9% YoY, reaching ₹139.7 Cr" | — |
| 6 | 278 | 40.2%, 8.6%, ₹49.7 (Cr) | "40.2%, PAT growth of 8.6% YoY to ₹49.7 Cr" | — |
| 6 | 280 | 31.2% | "PAT margin 31.2%." | — |
| 6 | 282 | 4 (Rs cr, part 1 of "Rs 4 ... cr write off") | "one-time Rs 4" | continues to line 284 |
| 6 | 284 | (continuation, no new digit — "cr write off" text only) | "cr write off for a specific government customer." | value already captured at line 282 |
| 6 | 286 | 745 (Cr), 685 (Cr) | "Cash & Cash equivalents grew to 745 Cr from 685" | — |
| 6 | 291 | 42%, 46%, 12% | "Government is 42%, 46%, 12% respectively, of the" | Automotive/Enterprise/Government revenue contribution mix |
| 9 | 417 | ₹98.7 (crore) | "Map-led business had stable revenue at ₹98.7 crore" | — |
| 9 | 419 | ~4%, 4 (Rs Cr) | "EBITDA margin was impacted by ~4% due to Rs 4Cr one-time write off" | — |
| 9 | 421 | 75%, ₹41.1 (crore) | "IoT-led business revenue grew 75% YoY to ₹41.1 crore" | — |
| 9 | 423 | 13.1%, 8.7%, 440 (bps) | "margin improved to 13.1% ... from 8.7% ... representing a 440 bps" | — |
| 12 | 526 | 29% | "Automotive business grew at 29% during Q1FY27 on a YoY basis" | duplicate value also appears as chart growth callout (Table 3, line 557) — both instances enumerated |
| 13 | 570 | 6% | "the Enterprise business grew at 6% on a YoY basis" | duplicate value also appears as chart growth callout (Table 3, line 601) |
| 14 | 614 | 11% | "the Government business grew at 11% on a YoY basis" | duplicate value also appears as chart growth callout (Table 3, line 645) |

Narrative numeric value count (each distinct figure token, not each row): 7 (slide 4) + 2 (slide 5) +
12 (slide 6) + 8 (slide 9) + 1 (slide 12) + 1 (slide 13) + 1 (slide 14) = 32.

---

## TABLE 5 — NOTES & FOOTNOTES (4/4)

| # | Line # | Slide | Text (verbatim/paraphrase) | Flags |
|---|---|---|---|---|
| 1 | 296 | 6 | "Note – 1) EBITDA Margin = EBITDA / Revenue from Operations" | formula definition footnote, qualifies EBITDA Margin row in Table 2A |
| 2 | 296 | 6 | "2) PAT Margin = PAT / Total Income" | formula definition footnote, qualifies PAT Margin row in Table 2A (denominator is Total Income, not Revenue from Operations — mechanical fact only, not interpreted) |
| 3 | 688 | 15 | "Note: As on June 30, 2026" | dates the Shareholding Pattern table (Table 2F) and the shareholding chart (Table 3, line 690) as of quarter-end |
| 4 | 696 | 16 | "Disclaimer" — full-page legal disclaimer (lines 704–733): no-offer statement, confidentiality, not-a-prospectus statement, no-update obligation, forward-looking-statements hedge, third-party-data non-verification statement, no-recommendation statement | qualifies every forward-looking and externally-sourced figure in the deck; see Table 6 row 3 for the forward-looking-statement hedge specifically |

---

## TABLE 6 — FORWARD-LOOKING / GOVERNANCE DISCLOSURES (4/4)

| # | Slide | Line # | Disclosure | Flags |
|---|---|---|---|---|
| 1 | 4 | 202–209 | Appointment of Rohan Verma as Joint Managing Director, "subject to shareholder approval," effective 1st July 2026 | governance / leadership change, approval condition stated (not yet shareholder-ratified as of presentation date per source text) |
| 2 | 4, 10 | 191–197, 437–467 | Segmental revenue reporting framework change: market-wise reporting moves from previously-reported "A&M and C&E market segments" to new "Automotive, Enterprise, Government (AEG)" categories, effective this quarter | SEGMENT_FRAMEWORK_CHANGE — comparability break flagged mechanically; prior-period AEG figures are shown restated on slide 11 (Tables 2C/2D above) but the deck states this is a first-time presentation of the new framework |
| 3 | 16 | 722–727 | Standard forward-looking-statements hedge: statements based on "management's current expectations," "no obligation to update or revise," "You should not place undue reliance on forward looking statements" | boilerplate hedge language, qualifies all forward-looking content across the deck |
| 4 | 14 | 633 | "Q1 is seasonally weakest quarter for Government business" | qualitative seasonality statement attached to the Government segment revenue chart (Table 3, line 645) |

---

## TABLE 7 — TABLE OF CONTENTS CROSS-CHECK (7/7 entries, all matched to content slides)

| # | TOC line # | TOC entry text | Matched slide(s) | Flags |
|---|---|---|---|---|
| 1 | 146 | Management Commentary | 4, 5 | — |
| 2 | 148 | Consolidated Financial Highlights (Q1FY27) | 6 | — |
| 3 | 150 | Business Description | 7, 8 | — |
| 4 | 151 | Segmental Highlights by Product: Map-led and IoT-led | 9 | — |
| 5 | 153 | Updated Market-wise Segmental Revenue Reporting Framework | 10, (11 continues the theme with trend data) | — |
| 6 | 155–156 | Segmental Revenue by Markets: AEG (Automotive, Enterprise and Government) | 12, 13, 14 (and 11's tables) | — |
| 7 | 157 | Shareholding Pattern | 15 | — |

Slides 1, 2 (cover letter/title) and 16, 17 (annexures/disclaimer, contact page) are standard
front/back matter not itemized in the TOC — consistent, not a gap.

---

## TABLE 8 — SUPPLEMENTARY: REGULATORY / CONTACT IDENTIFIERS (page 1 and page 17)

Not included in the GATE A2 count test above (these are static company/regulatory identifiers, not
quarterly performance disclosure units) but enumerated per the "every number on every slide" rule for
completeness.

| Slide | Line # | Identifier | Value |
|---|---|---|---|
| 1 | 26 | Letter date | August 04, 2026 |
| 1 | 32 | BSE registered address pincode | 400 001 |
| 1 | 32 | NSE registered address pincode | 400 051 |
| 1 | 33 | BSE Scrip Code | 543425 |
| 1 | 33 | NSE Symbol | MAPMYINDIA |
| 1 | 81 | Registered office pincode | New Delhi-110020 |
| 1 | 81 | Phone | +91-011-4600 9900 |
| 1 | 81 | CIN | L74899DL 1995PLC065551 |
| 1 | 81 | Quality certification | CMMI-3 (source text: "A CMMl-3 & ISO Certified Company") |
| 1 | 57 | Signatory | Saurabh Surendra Somani, Company Secretary & Compliance Officer |
| 17 | 750 | IR contact name | Sumit Pradhan |
| 17 | 754 | IR phone | +91 11 4600 9900 |
| 17 | 758 | CS contact name | Saurabh Surendra Somani |
| 17 | 763 | CS phone | +91 11 4600 9900 (duplicate of IR phone number) |
| 17 | 767–768 | Corporate office address / pincode | Plot No. 237, Okhla Industrial Estate, Phase-III, New Delhi 110 020 |

---

## DROPPED_SLIDE CHECK

Prior-quarter presentation ledger not supplied to this run (`{{PRIOR_LEDGER_PATH}}` blank in injected
inputs). No DROPPED_SLIDE comparison performed. Flagged `PRIOR_LEDGER_UNAVAILABLE` for A3/A4 to source
the Q4 FY26 presentation ledger if a slide-drop check is required downstream.

---

## FLAG SUMMARY

- ZERO_STANDING: 3 (Table 2A EBITDA Margin YoY dash, Table 2A Cash & cash equivalents YoY dash,
  Table 2B Sale of Hardware Map-led nil both periods)
- SEGMENT_FRAMEWORK_CHANGE: 1 (Table 6 #2 — A&M/C&E to AEG reporting transition)
- PRIOR_LEDGER_UNAVAILABLE: 1 (DROPPED_SLIDE check not run)

```yaml
stage: A2-enumerator
company: "MAPMYINDIA"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/ledger_presentation_mapmyindia_q1fy27.md"
counts:
  notes: 4
  line_items: 30
  zero_standing: 3
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 92
  slides: 17
  slide_numbers: 17
flags_raised: [ZERO_STANDING, SEGMENT_FRAMEWORK_CHANGE, PRIOR_LEDGER_UNAVAILABLE]
gate_a2: pass
mismatch_note: ""
```
