# A2 Enumeration Ledger — JNK India Limited (JNKINDIA), Q1 FY27, doctype: presentation (3-page Reg 30 press release)

Source: `runs/jnkindia-q1fy27/work/extract_pressrelease_jnkindia_q1fy27.txt`
Unit convention: **Rs. Crores** (document states "Particulars (Rs. Cr)" directly; no conversion applied).
Doc structure: page 1 = Reg 30 intimation letter to BSE/NSE + signature; page 2 = press release headline, results table, management quote; page 3 = "About JNK India", Safe Harbor Statement, contact block.

Note on method: because this is a 3-page narrative press release (not a slide deck), the INVESTOR-PRESENTATION "slide" unit is adapted to **claim/content block** = a paragraph-mode unit bounded by blank lines in the extract (mechanical, reproducible via blank-line splitting). Page boundaries are recorded separately per block.

---

## === A2 COUNT TEST ===

```
category: content_blocks (slide-equiv)  grep_count: 29   sweep_count: 29   match: yes
category: numbers (all pages, all tables) grep_count: 130  sweep_count: 130  match: yes
category: financial_table_line_items    grep_count: 5    sweep_count: 5    match: yes
category: footnotes_disclaimers         grep_count: 3    sweep_count: 3    match: yes
category: named_items (orders/customers/projects/entities/individuals/quotes) grep_count: 16 sweep_count: 16 match: yes
category: dropped_slides_vs_prior       grep_count: N/A  sweep_count: N/A  match: N/A (no prior-quarter ledger provided)
gate_a2: pass
```
## === END COUNT TEST ===

Grep commands used:
- content_blocks: paragraph-mode split on blank lines (`awk 'BEGIN{RS=""}...'`) over lines 14-167 (body, header excluded) → 29 records.
- numbers: `grep -noE '[0-9][0-9,]*\.?[0-9]*%?x?' <extract> | awk -F: '$1>13'` → 130 tokens across 39 lines.
- financial_table_line_items: 5 populated rows in the results table (lines 74-78).
- footnotes_disclaimers: `grep -n -iE "note|forward-looking|safe harbor|disclaimer|includes"` cross-checked manually → 3 (line 75 parenthetical, line 79 footnote, lines 136-144 Safe Harbor block).
- named_items: `grep -n -E "Mr\.|Chemdist|JNK Global|Advisors|Mundra|off-shore|metals|renewable|order book|bidding pipeline|Ashish Soni|Annie Varghese|Arvind Kamath"` → 16 matches mapping 1:1 to manual sweep rows.

---

## CATEGORY A — Content / Claim Blocks (slide-equivalent), all pages

| # | Page | Lines | First words | Content type | Flags |
|---|------|-------|-------------|---------------|-------|
| 1 | 1 | 14-20 | "[page 1] JNK India Limited (Formerly known as..." | text (letterhead: co. name, CIN, address, tel, email, website) | |
| 2 | 1 | 22 | "Date: August 11, 2026" | text | |
| 3 | 1 | 24-30 | "To, ... To," (dual addressee block: BSE Limited / NSE, scrip code / security symbol) | text | |
| 4 | 1 | 33 | "Dear Sir/Madam," | text | |
| 5 | 1 | 35-36 | "Ref: Press Release – Intimation under Regulation 30 of SEBI..." | text | |
| 6 | 1 | 38-40 | "Pursuant to Regulation 30 of the Securities and Exchange Board..." | text (Reg 30 statement) | |
| 7 | 1 | 42 | "This is for your information and records." | text | |
| 8 | 1 | 44 | "Thanking you," | text | |
| 9 | 1 | 46 | "Yours faithfully," | text | |
| 10 | 1 | 48-52 | "For JNK India Limited [digital signature block]" | text/signature (Ashish Soni, digitally signed 2026.08.11 23:40:15 +05'30') | SIGNATURE_TIMESTAMP (see Category D note below table if applicable) |
| 11 | 1 | 54-55 | "Ashish Soni / Company Secretary and Compliance Officer" | text (signatory name + designation) | |
| 12 | 1→2 | 57-59 | "Encl: a/a" [page 2] "Q1FY27 Press Release" | text — merges two distinct items across a page break: (a) enclosure notation closing the Reg 30 letter (line 57), (b) page-2 running header "Q1FY27 Press Release" (line 59). No blank line separates them in the extract. | PAGE_SPAN |
| 13 | 2 | 63 | "JNK India Delivers Strong Start to FY27 with 3.1x Growth in EBITDA" | text (headline) | |
| 14 | 2 | 65-68 | "Thane, August 11, 2026: JNK India Limited, ("JNK" or the "Company")..." | text (dateline + intro para, incl. business description "combustion equipment company...fired heaters, reformers, cracking furnaces") | |
| 15 | 2 | 71 | "Consolidated Financial Performance for Q1FY27:" | text (section header) | |
| 16 | 2 | 73-79 | "Particulars (Rs. Cr) Q1FY27 Q1FY26 YoY FY26" | table + footnote — merges the 5-row results table (73-78) with its qualifying footnote (79); no blank line separates them | see Category C/D |
| 17 | 2 | 82 | "Mr. Arvind Kamath, Chairperson and Whole Time Director" | text (quote attribution) | |
| 18 | 2 | 84-89 | ""We started FY27 on a strong note, with total income growing by ~80.6%..."" | text (mgmt quote, para 1: results + margin discipline) | NUMBER_MISMATCH (see Category B, line 85) |
| 19 | 2 | 91-94 | "Our order book on June 30, 2026 is Rs 1,801 cr, and our growth visibility..." | text (mgmt quote, para 2: order book + bidding pipeline) | |
| 20 | 2 | 96-99 | "At the same time, we are taking further steps to diversify our business..." | text (mgmt quote, para 3: new verticals — off-shore, metals & minerals, renewable energy; JNK Chemdist green hydrogen project) | |
| 21 | 2 | 101-103 | "We believe this expansion will broaden our addressable market..." | text (mgmt quote, para 4) | |
| 22 | 2 | 105-107 | "Overall, we remain focused on executing our existing projects..." | text (mgmt quote, para 5, closing) | |
| 23 | 2→3 | 111-116 | "JNK India Limited [footer letterhead]" [page 3] "Q1FY27 Press Release" | text — merges page-2 footer letterhead repeat (111-114) with page-3 running header repeat (116) across a page break | PAGE_SPAN |
| 24 | 3 | 121-134 | "About JNK India Limited" | text (company description: capabilities, Mundra facility, JNK Global partnership, Chemdist Group JV, 51% equity, served industries) | |
| 25 | 3 | 136-144 | "Safe Harbor Statement" | text (forward-looking statements disclaimer) | FWD_LOOKING_CAVEAT |
| 26 | 3 | 147 | "For further information, please contact" | text | |
| 27 | 3 | 149 | "Company / Investor Relations Advisors" | text (contact table column headers) | |
| 28 | 3 | 151-158 | "JNK India Ltd. / Strategic Growth Advisors Pvt. Ltd." | text (contact details: CIN, names, emails, phone numbers, websites, both columns) | |
| 29 | 3 | 163-166 | "JNK India Limited [footer letterhead]" | text (final footer letterhead repeat) | |

Content type tally: 27 text blocks, 1 table+footnote block (16), 1 signature block (10, subset of text). No chart, photo, or OCR content present (doc is text-native, `ocr_pages: none` per A1 header).

---

## CATEGORY B — Every Number, Every Page (raw numeric-token sweep)

Convention: Rs. Crores unless otherwise marked (%, x-multiple, or identifier). Each row = one source line; token count in that line shown; all 130 tokens accounted for.

| Line | Page | # tokens | Tokens | Context | Flags |
|------|------|----------|--------|---------|-------|
| 14 | 1 | 1 | 1 | "[page 1]" marker | non-content |
| 17 | 1 | 3 | 29268, 2010, 204223 | CIN: L29268MH2010PLC204223 | |
| 18 | 1 | 3 | 203, 206, 3 | Address: "203 to 206... Plot No. C-3" | |
| 19 | 1 | 4 | 400604, 91, 22, 68858000 | Address pin + Tel: 91-22-68858000 | |
| 22 | 1 | 2 | 11, 2026 | Date: August 11, 2026 | |
| 27 | 1 | 1 | 1 | "Phiroze Jeejeebhoy Towers" building no. context / Dalal Street ref | |
| 29 | 1 | 4 | 400, 001, 400, 051 | Mumbai pin codes (400001 BSE, 400051 NSE) | |
| 30 | 1 | 1 | 544167 | BSE scrip code | |
| 35 | 1 | 1 | 30 | "Regulation 30" | |
| 36 | 1 | 1 | 2015 | "Regulations, 2015" | |
| 38 | 1 | 1 | 30 | "Regulation 30" (body repeat) | |
| 39 | 1 | 1 | 2015 | "Regulations, 2015" (body repeat) | |
| 40 | 1 | 4 | 1, 27, 11, 2026 | "Q1FY27 Press Release dated August 11, 2026" | |
| 51 | 1 | 2 | 2026.08, 11 | Digital signature date stamp | |
| 52 | 1 | 5 | 23, 40, 15, 05, 30 | Digital signature time stamp "23:40:15 +05'30'" | |
| 58 | 1→2 | 1 | 2 | "[page 2]" marker | non-content |
| 59 | 2 | 2 | 1, 27 | "Q1FY27 Press Release" header | |
| 63 | 2 | 2 | 27, 3.1x | Headline: "...FY27 with 3.1x Growth in EBITDA" | |
| 65 | 2 | 3 | 11, 2026, 544167 | Dateline + "(BSE: 544167..." | |
| 68 | 2 | 2 | 30, 2026 | "quarter ended June 30, 2026" | |
| 71 | 2 | 2 | 1, 27 | "Q1FY27" in section header | |
| 73 | 2 | 5 | 1, 27, 1, 26, 26 | Table header row: Q1FY27 / Q1FY26 / FY26 | |
| 74 | 2 | 4 | 186.0, 103.0, 80.6%, 838.0 | Total Income row | |
| 75 | 2 | 4 | 21.9, 7.2, 3.1x, 111.3 | EBITDA (Includes Other Income) row | |
| 76 | 2 | 3 | 11.8%, 7.0%, 13.3% | EBITDA Margin row — **only 3 values, YoY column blank** | STRUCTURAL_BLANK |
| 77 | 2 | 4 | 9.6, 1.1, 8.5x, 64.8 | Profit After Tax row | |
| 78 | 2 | 3 | 5.2%, 1.1%, 7.7% | PAT Margin row — **only 3 values, YoY column blank** | STRUCTURAL_BLANK |
| 79 | 2 | 5 | 1, 27, 16.5, 1, 26 | Footnote: "Q1FY27...Rs 16.5 cr from JNK Chemdist...Q1FY26" | |
| 84 | 2 | 5 | 27, 80.6%, 186.0, 1, 27 | Quote: "...80.6% YoY to Rs. 186.0 cr in Q1FY27..." | |
| 85 | 2 | 7 | 10.30, 1, 26, 3.1x, 21.9, 8.5x, 9.6 | Quote: "...Rs. 10.30 cr in Q1FY26, EBITDA grew by 3.1x..." | **NUMBER_MISMATCH**: quote states Q1FY26 total income as "Rs. 10.30 cr"; results table (line 74) states Q1FY26 Total Income = Rs. 103.0 cr. Enumerated as found; discrepancy flagged for A3/A4 arithmetic-consistency review, not resolved here. |
| 87 | 2 | 3 | 11.8%, 1, 27 | Quote: "EBITDA margin of 11.8% in Q1FY27" | |
| 91 | 2 | 3 | 30, 2026, 1,801 | Quote: "order book on June 30, 2026 is Rs 1,801 cr" | |
| 92 | 2 | 1 | 6,000 | Quote: "bidding pipeline of Rs. ~6,000 cr" | |
| 112 | 2 | 3 | 29268, 2010, 204223 | Footer CIN repeat | |
| 113 | 2 | 4 | 203, 206, 3, 400604 | Footer address repeat | |
| 114 | 2 | 3 | 91, 22, 68858000 | Footer Tel repeat | |
| 115 | 2→3 | 1 | 3 | "[page 3]" marker | non-content |
| 116 | 3 | 2 | 1, 27 | "Q1FY27 Press Release" header repeat | |
| 125 | 3 | 1 | 20,000 | "fabrication facility in Mundra...20,000 square meters" | |
| 130 | 3 | 1 | 51% | "JNK India holding 51% equity share capital" | |
| 152 | 3 | 6 | 29268, 2010, 204223, 74140, 2010, 204285 | Two CINs (JNK India + Strategic Growth Advisors) | |
| 155 | 3 | 6 | 91, 96993, 82195, 91, 98214, 38864 | Two phone numbers (SGA advisors) | |
| 164 | 3 | 3 | 29268, 2010, 204223 | Footer CIN repeat (final) | |
| 165 | 3 | 4 | 203, 206, 3, 400604 | Footer address repeat (final) | |
| 166 | 3 | 3 | 91, 22, 68858000 | Footer Tel repeat (final) | |

Total tokens: **130** (matches grep count). Two structural-blank cells noted (lines 76, 78 — YoY column absent for both margin line items, consistent across both margin rows, single period shown so not comparable across periods; flagged rather than dropped). One cross-reference numeric discrepancy noted (line 85 vs line 74).

---

## CATEGORY C — Financial Table Line Items (results table, lines 73-78)

| # | Line | Line item | Q1FY27 | Q1FY26 | YoY | FY26 | Flags |
|---|------|-----------|--------|--------|-----|------|-------|
| 1 | 74 | Total Income | 186.0 | 103.0 | 80.6% | 838.0 | NUMBER_MISMATCH cross-ref (quote line 85 states 10.30 for Q1FY26) |
| 2 | 75 | EBITDA (Includes Other Income) | 21.9 | 7.2 | 3.1x | 111.3 | parenthetical qualifier "Includes Other Income" — see Category D |
| 3 | 76 | EBITDA Margin | 11.8% | 7.0% | (blank) | 13.3% | STRUCTURAL_BLANK — no YoY value shown |
| 4 | 77 | Profit After Tax | 9.6 | 1.1 | 8.5x | 64.8 | |
| 5 | 78 | Profit After Tax Margin | 5.2% | 1.1% | (blank) | 7.7% | STRUCTURAL_BLANK — no YoY value shown |

Zero/nil/dash check: all 5 line items carry populated values in Q1FY27, Q1FY26, and FY26 columns (this is a 5-line summary table, not a full statement — no line item registers zero, nil, or dash across all periods). **ZERO_STANDING count: 0.** Checked and confirmed, not assumed.

---

## CATEGORY D — Footnotes / Disclaimers / Forward-Looking Caveats Qualifying Headline Numbers

| # | Line(s) | Text (first 15 words) | Qualifies | Flags |
|---|---------|------------------------|-----------|-------|
| 1 | 75 | "(Includes Other Income)" — parenthetical directly in the EBITDA line-item label | EBITDA figures (21.9 / 7.2 / 3.1x / 111.3) — signals EBITDA is not a pure operating-EBITDA figure | HEADLINE_QUALIFIER |
| 2 | 79 | "Q1FY27 Total Income includes Revenue of Rs 16.5 cr from JNK Chemdist Limited which was not part of it in Q1FY26" | Total Income YoY growth (80.6%) — flags that part of the growth is inorganic/consolidation-driven (new entity in scope), not like-for-like | COMPARABILITY_CAVEAT |
| 3 | 136-144 | "Statements in this document relating to future status, events, or circumstances, including but not limited to statements about plans and objectives..." (Safe Harbor Statement, full paragraph) | All forward-looking statements in the release — order book/bidding pipeline visibility claims (lines 91-92), new-vertical diversification plans (lines 96-103), growth outlook language throughout the Chairperson's quote | FWD_LOOKING_CAVEAT |

---

## CATEGORY E — Named Orders / Customers / Projects / Entities / Individuals / Quotes

| # | Line(s) | Item | Type | Detail | Flags |
|---|---------|------|------|--------|-------|
| 1 | 82, 84-107 | Mr. Arvind Kamath | Management quote | Chairperson and Whole Time Director; sole quoted executive in the release | |
| 2 | 79 | JNK Chemdist Limited | Named entity (subsidiary/consolidation addition) | Contributed Rs 16.5 cr revenue in Q1FY27, "not part of it in Q1FY26" | ENTITY_CHANGE (newly consolidated vs. prior-year comparative; no prior ledger to cross-check first appearance date) |
| 3 | 96-99 | Green hydrogen project (executed by JNK Chemdist) | Named project (generic reference, no counterparty/customer named) | "actively pursuing more opportunities in related categories" | |
| 4 | 91 | Order book: Rs 1,801 cr | Aggregate disclosure, not a named order | As of June 30, 2026 | |
| 5 | 92 | Bidding pipeline: Rs ~6,000 cr | Aggregate disclosure, not a named order | "across domestic and international markets" | approximate figure ("~"), not exact |
| 6 | 97 | Off-shore (new vertical) | Named business vertical, no specific project/customer | "entering the off-shore...opportunities" | |
| 7 | 97 | Metals & minerals (new vertical) | Named business vertical | | |
| 8 | 97-98 | Renewable energy (expanded focus) | Named business vertical | "focusing more on renewable energy" | |
| 9 | 127-128 | JNK Global (South Korea) | Named strategic partner entity | "leading manufacturer...of industrial combustion equipment" | |
| 10 | 128-130 | Chemdist Group (founders) | Named JV partner entity | JV to develop green hydrogen, sustainable fuels, chemicals, carbon capture; JNK India holds 51% equity share capital | possible naming overlap with row 2 (JNK Chemdist Limited) — same underlying JV referenced two ways ("JNK Chemdist Limited" vs. "joint venture with founders of Chemdist Group"); flagged for A3/A4 to confirm same entity |
| 11 | 125-127 | Mundra, Gujarat fabrication facility | Named facility/asset | ~20,000 sq meters, multi-product SEZ unit, near deep-draft port | |
| 12 | 48-55 | Ashish Soni | Named individual (non-quote) | Company Secretary and Compliance Officer; digital signatory of the Reg 30 letter | |
| 13 | 153 | Annie Varghese | Named individual (non-quote) | Investor Relations, JNK India | |
| 14 | 151, 153 | Strategic Growth Advisors Pvt. Ltd. | Named entity (IR advisory firm) | CIN: U74140MH2010PTC204285 | |
| 15 | 153 | Mandar Chavan | Named individual (non-quote) | IR Advisor, Strategic Growth Advisors | |
| 16 | 153 | Rahul Agarwal | Named individual (non-quote) | IR Advisor, Strategic Growth Advisors | |

---

## CATEGORY F — Slides Present in Prior Quarter's Deck but Absent Now (DROPPED_SLIDE check)

**N/A — no prior-quarter ledger path was provided** (task input: "Prior-quarter ledger path: none"). Cannot assess `DROPPED_SLIDE` for this run. This gap should be closed by A3/A4 if a Q4FY26 or Q1FY26 press-release ledger becomes available, since the doc itself flags a comparability change (JNK Chemdist Limited entering the consolidation scope, Category D row 2 / Category E row 2) that a prior-deck diff would corroborate.

---

## Flags Raised (summary)

- `NUMBER_MISMATCH` — line 85 quote states Q1FY26 Total Income as "Rs. 10.30 cr"; table (line 74) states Rs. 103.0 cr for the same metric/period. Same order-of-magnitude digits, different decimal placement — enumerated as-is, not resolved.
- `STRUCTURAL_BLANK` — EBITDA Margin (line 76) and PAT Margin (line 78) rows carry no YoY column value (blank, not dash/NM), unlike all other rows in the table.
- `HEADLINE_QUALIFIER` — EBITDA line item is labelled "(Includes Other Income)," qualifying the 21.9 / 3.1x headline figures.
- `COMPARABILITY_CAVEAT` — Total Income YoY growth includes Rs 16.5 cr from JNK Chemdist Limited, not present in the Q1FY26 comparative.
- `FWD_LOOKING_CAVEAT` — Safe Harbor Statement covers all forward-looking language in the release, notably order book/bidding pipeline visibility claims and new-vertical diversification plans.
- `ENTITY_CHANGE` — JNK Chemdist Limited newly contributing revenue in Q1FY27 vs. Q1FY26; cannot fully evidence first-appearance quarter without a prior-quarter ledger.
- `PAGE_SPAN` — two content blocks (12, 23) straddle a page break with no blank-line separation in the extract, each merging two distinct disclosure items.
- Prior-quarter deck unavailable → `DROPPED_SLIDE` category not assessable this run (see Category F).

Zero-standing check performed and confirmed **zero** ZERO_STANDING rows (Category C) — not assumed, actively verified against the table.

---

```yaml
stage: A2-enumerator
company: "JNKINDIA"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/jnkindia-q1fy27/work/ledger_pressrelease_jnkindia_q1fy27.md"
counts:
  slides: 29                 # claim/content blocks (paragraph units, 3 pages)
  slide_numbers: 3           # distinct pages
  numbers: 130                # every numeric token, all pages, incl. table
  line_items: 5               # financial table rows
  zero_standing: 0
  notes: 3                    # footnotes / disclaimers / forward-looking caveats
  named_items: 16             # named orders/customers/projects/entities/individuals/quotes
  entities: 4                 # named organizations among named_items (JNK Chemdist, JNK Global, Chemdist Group, Strategic Growth Advisors)
  agenda_items: 0              # not applicable (not a Board Outcome letter)
  auditor_paras: 0             # not applicable (no auditor report in this doc)
  turns: 0                     # not applicable (not a transcript)
  questions: 0                 # not applicable (not a transcript)
  mgmt_numbers: 0               # not applicable (numbers already captured under 'numbers'; no separate concall turn structure)
flags_raised: [NUMBER_MISMATCH, STRUCTURAL_BLANK, HEADLINE_QUALIFIER, COMPARABILITY_CAVEAT, FWD_LOOKING_CAVEAT, ENTITY_CHANGE, PAGE_SPAN]
gate_a2: pass
mismatch_note: ""
```
