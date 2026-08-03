# A2 ENUMERATION LEDGER — SAMHI Hotels Limited (SAMHI), Q1 FY27
Source: `extract_pressrelease_samhi_q1fy27.txt` (doctype tag: presentation; actual sub-class: Regulation 30 covering letter + 4-page press release, prose narrative + KPI callouts + management quote, no slide deck, no OCR, unit convention Millions, x0.1 to Rs Crore)

This document is not a slide deck and not a concall transcript. It is treated
as a hybrid: a Reg 30 covering letter (1 agenda item, 1 signature block) plus
a press-release body (headline KPI callouts, a bulleted highlights list, two
financial tables, a management commentary quote, boilerplate/about section,
forward-looking-statement paragraph, and contact block). Every enumerable
unit below carries its source line number(s). No prior-quarter ledger was
supplied for this run, so no DROPPED_SLIDE / ENTITY_CHANGE diffing was
possible; this is noted as a gap, not assumed clean.

=== A2 COUNT TEST ===
category: pages                    grep_count: 4    sweep_count: 4    match: yes
category: notes (numbered footnotes) grep_count: 10  sweep_count: 10   match: yes
category: agenda_items (Reg 30 letter) grep_count: 1  sweep_count: 1   match: yes
category: headline_kpi_callouts    grep_count: 4    sweep_count: 4    match: yes
category: key_highlights_bullets   grep_count: 7    sweep_count: 7    match: yes
category: line_items (fin. highlights table) grep_count: 10 sweep_count: 10 match: yes
category: line_items (debt profile table)    grep_count: 6  sweep_count: 6  match: yes
category: mgmt_quote_paragraphs    grep_count: 7    sweep_count: 7    match: yes
category: mgmt_numbers (in quote)  grep_count: 11   sweep_count: 11   match: yes
category: forward_looking_statements grep_count: 1  sweep_count: 1    match: yes
category: about_samhi_facts        grep_count: 4    sweep_count: 4    match: yes
category: contact_blocks           grep_count: 2    sweep_count: 2    match: yes
category: signature_blocks         grep_count: 1    sweep_count: 1    match: yes
category: scrip_codes / CIN pairs  grep_count: 4    sweep_count: 4    match: yes
category: zero_standing (all-period dash rows) grep_count: 0 sweep_count: 0 match: yes
gate_a2: pass
=== END COUNT TEST ===

Note on zero_standing: Two table rows carry a dash in one or more periods
("Exceptional Items" line 118: dash in Q1FY27 and Q1FY26, but 1,075 in FY26;
"Profit/(Loss) from discontinued ops" line 119: dash in Q1FY27 only, (28) in
Q1FY26, (55) in FY26; "Net Debt: EBITDA (Adjusted for Growth Capital)" line
147: dash only in the Sep 30 2023 column). None of these three rows is dash/
nil/zero in EVERY period shown, so per the strict ZERO_STANDING rule (all
periods) none qualifies for that flag. They are enumerated below with a
PARTIAL_DASH note instead so A3/A4 do not lose the signal.

---

## 1. PAGES

| # | Page | Line (page marker) | Content summary | Flags |
|---|------|--------------------|------------------|-------|
| 1 | 1 | 27 | Reg 30 covering letter to BSE/NSE, signed by Sanjay Jain | |
| 2 | 2 | 76 | Press release headline, key highlights, consolidated financial highlights table + footnotes | |
| 3 | 3 | 136 | Debt profile table + footnotes; management commentary quote (Ashish Jakhanwala) | |
| 4 | 4 | 198 | About SAMHI, forward-looking statements, contact information | |

---

## 2. REGULATION 30 COVERING LETTER — AGENDA / BOARD ACTION (page 1)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Board approval of unaudited standalone and consolidated results, Q1 ended 30 June 2026, under Reg 33 SEBI LODR | 44-49 | Board meeting date: Monday, 03 August 2026. No board meeting start/end time disclosed anywhere in the document. | NOT_FOUND (meeting times) |

Only one substantive agenda item is present in this letter (results approval).
There is no AR approval, AGM notice, record date, dividend, director
appointment, auditor change, scrutinizer, or ESOP item in this filing — this
is a single-purpose press-release covering letter, not a full Board Outcome
letter, so the absence of those items is expected for this doctype and is
not itself a flag.

### Recipients / scrip codes (letter header, page 1)

| # | Recipient | Line | Scrip code | Flags |
|---|-----------|------|------------|-------|
| 1 | BSE Limited, Corporate Relationship Dept., Mumbai | 32-38 | 543984 | |
| 2 | National Stock Exchange of India Limited, Bandra Kurla Complex, Mumbai | 33-38 | SAMHI | |

### Digital signature block (page 1)

| # | Signatory | Designation | Timestamp | Line | Flags |
|---|-----------|-------------|-----------|------|-------|
| 1 | Sanjay Jain | Senior Director – Corporate Affairs, Company Secretary and Compliance Officer | 2026.08.03 21:09:01 +05'30' | 61-68 | Cannot assess signature-before-board-meeting-concluded flag: no board meeting end time is disclosed in this letter (see item above), so timestamp cannot be cross-checked. |

---

## 3. HEADLINE KPI CALLOUT BOXES (page 2, top banner)

| # | KPI | Value | Line | Flags |
|---|-----|-------|------|-------|
| 1 | RevPAR growth (superscript note 1) | 9.6% | 85-86 | |
| 2 | Total Income | Rs 3,083 Mn | 85-86 | |
| 3 | Consolidated EBITDA | Rs 1,013 Mn | 85-86 | |
| 4 | PAT | Rs 249 Mn | 85-86 | |

Unit disclosure line: "All values in Rs mn, unless specified otherwise" — line 87.

---

## 4. KEY HIGHLIGHTS BULLETS (page 2)

| # | Bullet | Line | KPI type | Flags |
|---|--------|------|----------|-------|
| 1 | RevPAR at Rs. 5,219, up 9.6% YoY, despite geopolitical disruptions | 96 | RevPAR | |
| 2 | Occupancy stood at ~79.3% (up from ~74.2% Q1-FY26) | 98 | Occupancy | |
| 3 | Total Income for the quarter Rs. 3,083 Mn, up 10.8% YoY Comparable and +7.3% YoY Reported | 100 | Revenue | |
| 4 | EBITDA for the quarter Rs. 1,013 Mn, up 12.1% YoY Comparable, down 4.1% YoY Reported | 102 | EBITDA | |
| 5 | Effective Interest Rate is 7.8%, ~300bps lower since IPO | 104 | Interest rate | |
| 6 | Net Debt to EBITDA is at ~3.2x, ~2.4x on Operating Assets | 106 | Net debt / leverage | |
| 7 | PAT stood at Rs. 249 Mn, up by 29.6% YoY | 108 | PAT | |

Note: bullet 6 states Net Debt:EBITDA ~3.2x here (matches the debt-profile
table's Jun 30, 2026 column, line 146), whereas the management-quote
paragraph on page 3 (line 188) separately states "~3.0x." See §7 below —
flagged NUMBER_DISCREPANCY.

---

## 5. CONSOLIDATED FINANCIAL HIGHLIGHTS TABLE (page 2, lines 111-123)

Columns: Q1FY27 | Q1FY26 | YoY % | FY26

| # | Line item | Line | Q1FY27 | Q1FY26 | YoY% | FY26 | Flags |
|---|-----------|------|--------|--------|------|------|-------|
| 1 | Total Income | 114 | 3,083 | 2,873 | +7.3% | 12,790 | |
| 2 | Consolidated EBITDA* (superscript note 2) | 115 | 1,013 | 1,056 | -4.1% | 4,626 | |
| 3 | EBITDA Margin % | 116 | 32.9% | 36.8% | (blank) | 36.2% | |
| 4 | PBT (before exceptional items) | 117 | 327 | 259 | +26.4% | 1,650 | |
| 5 | Exceptional Items | 118 | - | - | (blank) | 1,075 | PARTIAL_DASH (dash both quarterly periods, populated only in FY26 column) |
| 6 | Profit/(Loss) from discontinued ops (superscript note 5) | 119 | - | (28) | (blank) | (55) | PARTIAL_DASH (dash in Q1FY27 only) |
| 7 | PBT | 120 | 327 | 231 | +41.8% | 2,671 | |
| 8 | PAT | 121 | 249 | 192 | +29.6% | 5,665 | |
| 9 | Attributable to SAMHI | 122 | 183 | 173 | (blank) | 5,030 | |
| 10 | Attributable to Minority Interest | 123 | 67 | 19 | (blank) | 636 | |

### Footnotes to this table (lines 124-129)

| # | Note | Line | First ~15 words |
|---|------|------|------------------|
| 1 | 124 | 124 | "Based on same-store, i.e, excludes the Trinity acquired in Oct'24, HIEX Greater Noida..." |
| 2 | 126 | 126 | "Comparable excludes one-time GIC-transaction related items in Q1FY26 and the GST input tax credit..." |
| 3 | 127 | 127 | "Includes the impact of: ~91mn of one-time other income in Q1FY26 on account of a subsidiary..." |
| 4 | 128 | 128 | "Includes the impact of: ~21mn of one-time GIC transaction expenses in Q1FY26, ~92mn of GST..." |
| 5 | 129 | 129 | "Profit/Loss from discontinued operations represents Caspia Delhi" |

Superscript markers observed in the table body (rendered oddly by
pdftotext as "!" "®" "?" in the highlights bullets and as bare "*" in the
table, e.g. line 115 "Consolidated EBITDA*" and line 148 "Interest Rate
7.8%*"): these are footnote-reference glyphs pointing back into the
numbered note lists above/below, not separate disclosure units in their
own right; no additional unnumbered footnote text was found trailing them.

---

## 6. DEBT PROFILE TABLE (page 3, lines 140-149)

Columns: Jun 30, 2026 | Mar 31, 2026 | Mar 31, 2025 | Sep 30, 2023

| # | Line item | Line | Jun 30 2026 | Mar 31 2026 | Mar 31 2025 | Sep 30 2023 | Flags |
|---|-----------|------|-------------|-------------|-------------|-------------|-------|
| 1 | Net Debt | 144 | 14,928 | 14,507 | 19,669 | 17,974 | |
| 2 | TTM EBITDA (superscript note 1) | 145 | 4,664 [OCR-garbled trailing "2"] | 4,721 [OCR-garbled trailing "2"] | 4,434 | 3,398 | Digit legibility flag: cell text renders "4,6642" / "4,7212" — likely a footnote-marker digit fused onto the number by text extraction, not a genuine 5-digit value; treat 4,664 / 4,721 as the numeric reading and the trailing digit as a footnote-reference artifact pending visual confirmation against the source PDF. |
| 3 | Net Debt: EBITDA | 146 | 3.2x | 3.1x | 2.4x | 5.3x | |
| 4 | Net Debt: EBITDA (Adjusted for Growth Capital) | 147 | 2.4x [rendered "240"] | 2.4x | 3.9x [rendered "3.9¢"] | - | PARTIAL_DASH (dash only in the Sep 30 2023 column); digit legibility flag on the Jun 30, 2026 cell ("240" likely "2.4x" with the "x" dropped/mis-rendered) |
| 5 | Interest Rate (superscript note 4) | 148 | 7.8%* | 7.9% | 9.2% | 10.8% | |
| 6 | Net Annualised Interest Run Rate (superscript note 5) | 149 | ~1,240 | ~1,270 | ~1,900 | ~2,400 | |

### Footnotes to this table (lines 150-154)

| # | Note | Line | First ~15 words |
|---|------|------|------------------|
| 1 | 150 | 150 | "Excluding ESOP & One-time Expenses" |
| 2 | 151 | 151 | "Excludes Caspia Delhi EBITDA on TTM basis" |
| 3 | 152 | 152 | "Capital allocated towards W(HITEC Hyd.), Westin Bglr., HRP Apartments, Sheraton Rooms & Apartments..." |
| 4 | 153 | 153 | "As on 30 June 2026. Please note that the interest rate includes the upfront fee which is amortized..." |
| 5 | 154 | 154 | "Does not include non-cash finance cost items such as interest on lease, EIR, etc. which are charged" |

---

## 7. MANAGEMENT COMMENTARY QUOTE (page 3, lines 158-190)

Speaker: Mr. Ashish Jakhanwala, MD & CEO, SAMHI Hotels Ltd. Single quote,
6 paragraphs, attribution line + 6 body paragraphs = 7 enumerable quote units.

| # | Unit | Line(s) | First ~10 words / content | Flags |
|---|------|---------|---------------------------|-------|
| 1 | Attribution line | 160 | "Commenting on the performance, Mr. Ashish Jakhanwala, MD & CEO, SAMHI Hotels Ltd." | |
| 2 | Quote para 1 | 163-167 | "I am pleased to report another quarter of resilient performance..." | |
| 3 | Quote para 2 | 169-171 | "The quarter witnessed some disruption to international travel..." | |
| 4 | Quote para 3 | 174-175 | "Our growth pipeline remains on track, with ongoing hotel additions..." | |
| 5 | Quote para 4 | 177-181 | "Our strategic partnership with RARE India extends our capabilities..." | |
| 6 | Quote para 5 | 183-185 | "Looking ahead, we are confident that our growth pipeline..." | |
| 7 | Quote para 6 | 188-190 | "Our balance sheet remains strong, with Net Debt to EBITDA..." | |

Only one management quote appears in the entire document (no additional
quotes from CFO, Chairman, or other officers).

### Numbers spoken/stated within the quote (mgmt_numbers), with paragraph and line

| # | Number | Context | Para | Line | Flags |
|---|--------|---------|------|------|-------|
| 1 | 9.6% | RevPAR growth YoY | 2 | 164 | |
| 2 | 10.8% | Total Income growth YoY, comparable basis | 2 | 164 | |
| 3 | Rs 3,083 million | Total Income value | 2 | 164 | |
| 4 | 12.1% | Consolidated EBITDA growth YoY, comparable basis | 2 | 165 | |
| 5 | Rs 1,013 million | Consolidated EBITDA value | 2 | 165 | |
| 6 | 36.0% | Operating EBITDA margin (excluding GST impact) | 2 | 166 | |
| 7 | 79.3% | Occupancy | 2 | 166 | |
| 8 | ~41% | Upscale inventory share, starting point | 4 | 175 | |
| 9 | ~60% | Upscale inventory share target by FY2030 | 4 | 175 | |
| 10 | ~40% | Target operating EBITDA margin | 6 | 185 | |
| 11 | ~3.0x | Net Debt to EBITDA, "comfortable" | 7 | 188 | NUMBER_DISCREPANCY — the debt profile table (line 146) and the page-2 highlights bullet (line 106) both state Net Debt:EBITDA at 3.2x as of Jun 30 2026; the CEO quote states "~3.0x." Both figures are explicitly disclosed in the same document; flagged for A3/A4 arithmetic-consistency review, not resolved here. |

---

## 8. ABOUT SAMHI / PORTFOLIO FACTS (page 4, lines 202-207)

| # | Fact | Line | Value | Flags |
|---|------|------|-------|-------|
| 1 | Hotel operator partnerships | 204-205 | Marriott, IHG, Hyatt (3 named operators) | |
| 2 | Portfolio size | 206 | 31 operating hotels | |
| 3 | Room/key count | 206 | 4,899 keys | |
| 4 | Geographic footprint | 206-207 | 13 cities, incl. NCR, Bengaluru, Hyderabad, Chennai, Pune | |

Single "ABOUT SAMHI HOTELS LTD." paragraph (lines 203-207) carries all four facts.

---

## 9. FORWARD-LOOKING STATEMENTS (page 4, lines 210-216)

| # | Unit | Line(s) | Content | Flags |
|---|------|---------|---------|-------|
| 1 | Section header | 210 | "FORWARD-LOOKING STATEMENTS" | |
| 2 | Disclaimer paragraph | 212-216 | Standard safe-harbor language: plans/objectives, R&D progress, project characteristics/target dates are forward-looking, subject to risks/uncertainties, actual results may differ materially, no obligation to update. | Single paragraph; boilerplate, no company assumes update obligation for FY26/FY2030 targets stated earlier in the CEO quote (upscale share ~60% by FY2030, ~40% EBITDA margin target) — those targets are therefore covered by this disclaimer even though it appears on a later page. |

---

## 10. CONTACT INFORMATION BLOCK (page 4, lines 218-228)

| # | Block | Line(s) | Entity | Contact person(s) | CIN | Flags |
|---|-------|---------|--------|--------------------|-----|-------|
| 1 | Company | 221-227 | SAMHI Hotels Limited | Mr. Gyana Das (Compliance@samhi.co.in) | L55101DL2010PLC211816 | |
| 2 | Investor Relations Advisors | 221-228 | Strategic Growth Advisors Pvt. Ltd. | Ms. Ami Parekh / Mr. Rahul Agarwal | U74140MH2010PTC204285 | |

---

## 11. TEXT-EXTRACTION / LETTERHEAD ARTIFACT OBSERVATIONS (mechanical, non-interpretive)

| # | Observation | Line(s) | Flags |
|---|-------------|---------|-------|
| 1 | Stylized company logo/tagline text renders as "IMART HOTEL INVESTMENTS—" (page 1) and "—SNART HOTEL INVESTMENTS——" (pages 2-4) instead of legible brand text, despite the A1 header certifying all 4 pages cleared the clean-text threshold with no OCR fallback needed. This is a font/kerning artifact on a stylized logo graphic, not a body-text OCR failure; it does not affect any numeric disclosure. | 28, 78, 138, 200 | TEXT_ARTIFACT (logo only, no numeric content affected) |
| 2 | Two table cells show a digit apparently fused with a footnote-marker glyph rather than a clean value ("4,6642", "4,7212" on line 145; "240" for what context indicates should read "2.4x" on line 147; "3.9¢" for "3.9x" also line 147). Flagged for visual confirmation against source PDF rather than silently corrected. | 145, 147 | TEXT_ARTIFACT — needs source-PDF visual check |

---

## SUMMARY COUNTS (feeds YAML below)

- pages: 4
- notes (numbered footnotes, both tables combined): 10
- agenda_items (Reg 30 letter): 1
- line_items (financial highlights table rows + debt profile table rows): 10 + 6 = 16
- zero_standing (strict all-period dash/nil/zero): 0 (three PARTIAL_DASH rows noted but do not meet the all-period bar)
- mgmt_quote_paragraphs (quote units, incl. attribution): 7
- mgmt_numbers (numeric statements inside the quote): 11
- headline_kpi_callouts: 4
- key_highlights_bullets: 7
- forward_looking_statements: 1
- about_samhi_facts: 4
- contact_blocks: 2
- signature_blocks: 1
- flags raised: NOT_FOUND (board meeting times), PARTIAL_DASH (x3), NUMBER_DISCREPANCY (x1), TEXT_ARTIFACT (x2)
