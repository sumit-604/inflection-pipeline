# A2 ENUMERATION LEDGER — ANUP Q1 FY27 — Press Release (doctype tagged: presentation)

Source: `extract_pressrelease_anup_q1fy27.txt` (A1 extract). Document is a 3-page
PDF: page 1 = SEBI Reg. 30 covering letter to BSE/NSE; pages 2-3 = the Q1 FY27
press release narrative. There is no slide deck in this filing, so the
INVESTOR PRESENTATION enumeration branch is adapted per orchestrator
instruction: "slide" = page; every bullet/paragraph is enumerated as its own
claim unit; every number stated is enumerated; every forward-looking/outlook
statement is enumerated separately with its line cite; every footnote/
disclaimer is enumerated. Prior-quarter ledger: **none available** — the
DROPPED_SLIDE / cross-quarter diff check could not be run (noted as a
limitation below, not a gate failure).

```
=== A2 COUNT TEST ===
category: total_disclosure_blocks (awk blank-line paragraph blocks, whole doc)   grep_count: 28   sweep_count: 28   match: yes
category: cover_letter_blocks (page 1 letter, paragraph-block level)             grep_count: 12   sweep_count: 12   match: yes
category: signature_blocks                                                       grep_count: 1    sweep_count: 1    match: yes
category: section_headers (press release body)                                   grep_count: 5    sweep_count: 5    match: yes
category: bulleted_claims (press release body, "•" marker)                       grep_count: 20   sweep_count: 20   match: yes
category: narrative_paragraphs (non-bullet, non-header body prose)               grep_count: 6    sweep_count: 6    match: yes
category: forward_looking_outlook_statements                                     grep_count: 13   sweep_count: 13   match: yes
category: numbers_financial_business (₹, %, spelled counts)                      grep_count: 14   sweep_count: 14   match: yes
category: numbers_administrative_identifiers (line-based)                        grep_count: 23   sweep_count: 23   match: yes
category: letterhead_footer_blocks (CIN repeat)                                  grep_count: 2    sweep_count: 2    match: yes
category: ir_cs_contacts ("Email:" tokens)                                       grep_count: 3    sweep_count: 3    match: yes
category: footnotes_disclaimers                                                  grep_count: 1    sweep_count: 1    match: yes
category: addressees (regulatory recipients)                                     grep_count: 2    sweep_count: 2    match: yes
category: zero_standing_line_items (no financial table present)                  grep_count: 0    sweep_count: 0    match: yes (N/A)
category: consolidation_entities (none listed in this document)                  grep_count: 0    sweep_count: 0    match: yes (N/A)
category: auditor_paragraphs (not applicable, no auditor report in doc)          grep_count: 0    sweep_count: 0    match: yes (N/A)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology notes: bullets counted via `grep -c "•"`; section headers via
keyword grep on the 5 known headers; financial numbers via `₹` count (10),
`%` count in body (2, excludes header metadata's unrelated "page_coverage:
100%"), and spelled-count "two"/"Two" (2); administrative numbers counted at
one-row-per-matched-content-line granularity (23 lines; two of those lines —
canonical 96 and 150 — each carry 3 numeric sub-values: fax + 2 tel numbers,
documented inline in the row rather than gated as separate rows); paragraph
blocks via an awk blank-line-delimited pass across the whole extract (28
total: 12 in the cover letter, 16 in the press release body incl. disclaimer
and footer repeat); forward-looking/outlook statements via the mechanical
union of (a) all 8 bullets structurally inside the "Outlook for FY27" section
and (b) 5 keyword-flagged statements outside that section, cross-checked
against an independent manual read of the full body.

---

## 1. Cover Letter Disclosure Items (page 1, lines 2-43)

| # | Line(s) | Item | Detail | Flags |
|---|---------|------|--------|-------|
| 1 | 2 | Letter date | 06th August, 2026 | |
| 2 | 4-11 | Addressee 1 | BSE Limited, Dept. of Corporate Services, P.J. Towers, Dalal Street, Mumbai 400 001; Security Code 542460 | |
| 2b | 4-11 | Addressee 2 | National Stock Exchange of India Ltd, Listing Department, Exchange Plaza, BKC, Bandra (E), Mumbai 400 051; Symbol ANUP | |
| 2c | 11 | Security ID | Security ID: ANUP (BSE) / Symbol: ANUP (NSE) — same identifier both exchanges | |
| 3 | 13 | Salutation | "Dear Sir/Madam," | |
| 4 | 15 | Subject line | "Press Release - Unaudited Financial Results for the quarter ended on 30th June, 2026" | |
| 5 | 17-18 | Regulatory reference | Regulation 30 of SEBI (LODR) Regulations, 2015 | |
| 6 | 20-23 | Body statement | Pursuant to Reg. 30, enclosing press release on Unaudited Standalone and Consolidated Financial Results, quarter ended 30 June 2026 | |
| 7 | 25-26 | Availability statement | Press release also to be posted at https://www.anupengg.com/quarterly-report/ | |
| 8 | 28 | Closing request | "You are requested to take the above on your records." | |
| 9 | 30 | Closing salutation | "Thanking you," | |
| 10 | 32-34 | Valediction block | "Yours faithfully, For, The Anup Engineering Limited" + "Digitally signed by Desai" tag | |
| 11 | 36-41 | Signature block detail | Desai Lay / Lay Desai, Company Secretary, Membership No. A57117 (see Table 2 for full signature-timestamp check) | |
| 12 | 43 | Enclosure note | "Encl.: As Above" | |

Block count = 12 (matches COUNT TEST `cover_letter_blocks`; rows 2/2b/2c are
sub-facts inside the single addressee block and are not separately gated).

## 2. Signature Block

| # | Line(s) | Signatory | Designation | Signed date | Signed time | Flags |
|---|---------|-----------|-------------|-------------|--------------|-------|
| 1 | 34-41 | Desai Lay / Lay Desai | Company Secretary (Membership No. A57117) | 2026.08.06 | 12:53:53 +05'30' | No board-meeting conclusion time is stated anywhere in this document (it is a press-release covering letter, not a full Outcome-of-Board-Meeting intimation), so the "signed before meeting concluded" check from the RESULTS FILING branch is **not applicable / cannot be tested** against this document alone. |

## 3. Press Release — Section Headers (5)

| # | Line | Header text |
|---|------|-------------|
| 1 | 49 | "Highlights for Q1 FY27 (Comparison on a YoY basis):" |
| 2 | 67 | "Consolidated Financial Highlights:" |
| 3 | 84 | "Outlook for FY27" |
| 4 | 121 | "About Anup Engineering:" |
| 5 | 135 | "Disclaimer:" |

## 4. Press Release — Bulleted Claims (20)

### 4a. Highlights for Q1 FY27 (4 bullets, lines 50-54)

| # | Line(s) | First ~15 words | Numbers present | Flags |
|---|---------|------------------|------------------|-------|
| 1 | 50 | "Revenue of ₹125 Cr achieved in line with planned Q1 execution, while gross margin remains intact." | ₹125 Cr | |
| 2 | 51 | "Highest pending orderbook visibility (including LOI) of ₹985 Cr." | ₹985 Cr | |
| 3 | 52-53 | "Strategic growth initiatives gained momentum with orders secured for new proprietary & licensed products..." | none | |
| 4 | 54 | "FY27 focus remains on stabilization and consolidation of the business." | none | FORWARD_LOOKING; REPEATED_CLAIM (see #10, #13 below) |

### 4b. Consolidated Financial Highlights (8 bullets, lines 68-82)

| # | Line(s) | First ~15 words | Numbers present | Flags |
|---|---------|------------------|------------------|-------|
| 5 | 68 | "Consolidated revenue for Q1 FY27 stood at ₹125 Cr; EBITDA for the quarter was ₹9.2 Cr." | ₹125 Cr, ₹9.2 Cr | |
| 6 | 69-71 | "Performance during the quarter reflects a planned lower execution due to low order booking during last year..." | none | |
| 7 | 72-73 | "EBITDA margins were impacted entirely on account of lower revenue leading to under-absorption of fixed costs." | none | |
| 8 | 74 | "Highest ever order booking during the quarter of ~₹315 Cr and ~₹540 Cr YTD." | ~₹315 Cr, ~₹540 Cr | |
| 9 | 75-77 | "Booked order of more than ₹150 Cr for Thermal Power plants, entering elite group of manufacturers..." | ₹150 Cr | FORWARD_LOOKING (embedded clause "expected to see significant growth in near future") |
| 10 | 78-79 | "Bagged order of two proprietary license products in line with strategic intent to move in to niche segment." | "two" (spelled count) | |
| 11 | 80 | "Started execution of Two large Air-Cool Heat Exchanger for a marquee customer in Germany." | "Two" (spelled count) | Entity cited: unnamed customer, Germany |
| 12 | 81-82 | "The Company remains committed to protecting margins and maintaining healthy cash flows despite cost pressures..." | none | FORWARD_LOOKING |

### 4c. Outlook for FY27 (8 bullets, lines 85-113, spans pages 2-3)

| # | Line(s) | First ~15 words | Numbers present | Flags |
|---|---------|------------------|------------------|-------|
| 13 | 85-88 | "FY27 is expected to be a year of stabilization, strengthening of fundamentals, consolidation and risk management..." | none | FORWARD_LOOKING; REPEATED_CLAIM (see #4, #15) |
| 14 | 89 | "Healthy pending orderbook (including LOI) of ₹985 Cr (of which ~₹240 Cr booked for FY28)" | ₹985 Cr, ~₹240 Cr | FORWARD_LOOKING (FY28 forward booking clause) |
| 15 | 100-101 | "Orderbook between Domestic (61%) and Exports (39%), suggesting pick up in domestic demand." | 61%, 39% | FORWARD_LOOKING (soft/interpretive — "suggesting pick up") |
| 16 | 102 | "Encouraging Order inquiry pipeline of ₹1,100 Cr." | ₹1,100 Cr | FORWARD_LOOKING (soft — pipeline visibility, not an explicit projection) |
| 17 | 103-105 | "Foray into the Nuclear, Thermal energy and clean energy storage segment, positions the company well..." | none | FORWARD_LOOKING |
| 18 | 106-108 | "The company wishes to strategically grow the technical services business to boost growth and enhance profitability..." | none | FORWARD_LOOKING |
| 19 | 109-111 | "Considering the current global volatile business scenarios due to wars & geopolitics, the focus of the company this year will be more on Stabilization..." | none | FORWARD_LOOKING; REPEATED_CLAIM (see #4, #13) |
| 20 | 112-113 | "Continuous endeavor to add new critical and proprietary products to create more niche space." | none | FORWARD_LOOKING |

## 5. Press Release — Narrative Paragraphs / Statements (non-bullet, non-header body prose) (6)

| # | Line(s) | Content | Numbers | Flags |
|---|---------|---------|---------|-------|
| 1 | 47 | Headline claim: "Q1 FY27 performance reflects planned execution strategy, very strong order booking" | none | |
| 2 | 56-60 | Dateline + company description: Ahmedabad, 06 Aug 2026 dateline; company description (static process equipment; Oil & Gas, Petrochemicals, LNG/LPG, Hydrogen, Nuclear, Aerospace, Energy Storage); announces results for quarter ended 30 June 2026 | date 30 June 2026 | No named CMD/MD/promoter is quoted anywhere in this paragraph or elsewhere in the document (see MGMT_ABSENCE flag) |
| 3 | 62-65 | "The result reflects a planned operating performance during the quarter, which also includes debottlenecking our operations which got disrupted due to geopolitical uncertainties and supply chain under a lot of strain. This was a step in the right direction..." | none | FORWARD_LOOKING (closing clause "to ensure smooth operations during rest of the year") |
| 4 | 115-119 | "Looking ahead, management remains optimistic about the medium-term outlook, supported by expanded capacities, a fully operational Kheda facility, and diversified capabilities..." | none | FORWARD_LOOKING; entity cited: Kheda facility |
| 5 | 123-125 | "About Anup Engineering" boilerplate: company caters to Oil & Gas, Petrochemicals, LNG, Hydrogen, Fertilizers, Chemicals/Pharmaceuticals, Power, Water, Paper & Pulp, Aerospace; product range: Heat Exchangers, Reactors, Pressure Vessels, Columns & Towers, Silos and Tanks, Industrial Centrifuges & Formed Components | none | |
| 6 | 127 | "For further information, please visit: www.anupengg.com." | none | |

## 6. Forward-Looking / Outlook Statements (13, cross-referenced from Tables 4-5, cited independently per task instruction)

| # | Line(s) | Statement (abridged) | Source table ref | Notes |
|---|---------|-----------------------|-------------------|-------|
| 1 | 54 | "FY27 focus remains on stabilization and consolidation of the business." | 4a-#4 | REPEATED_CLAIM group |
| 2 | 62-65 | "...step in the right direction to ensure smooth operations during rest of the year." | 5-#3 | |
| 3 | 75-77 | "...which is expected to see significant growth in near future." (Thermal sector) | 4b-#9 | embedded clause |
| 4 | 81-82 | "The Company remains committed to protecting margins and maintaining healthy cash flows despite cost pressures..." | 4b-#12 | |
| 5 | 85-88 | "FY27 is expected to be a year of stabilization, strengthening of fundamentals, consolidation and risk management..." | 4c-#13 | REPEATED_CLAIM group |
| 6 | 89 | "...of which ~₹240 Cr booked for FY28" | 4c-#14 | forward booking figure |
| 7 | 100-101 | "...suggesting pick up in domestic demand." | 4c-#15 | soft/interpretive |
| 8 | 102 | "Encouraging Order inquiry pipeline of ₹1,100 Cr." | 4c-#16 | soft — pipeline visibility |
| 9 | 103-105 | "...positions the company well to enhance capabilities, diversify revenue base and strengthen its long-term outlook." | 4c-#17 | |
| 10 | 106-108 | "The company wishes to strategically grow the technical services business to boost growth and enhance profitability..." | 4c-#18 | |
| 11 | 109-111 | "...the focus of the company this year will be more on Stabilization of current operations, better Execution, Consolidation and Risk mitigation." | 4c-#19 | REPEATED_CLAIM group |
| 12 | 112-113 | "Continuous endeavor to add new critical and proprietary products to create more niche space." | 4c-#20 | |
| 13 | 115-119 | "Looking ahead, management remains optimistic about the medium-term outlook... well positioned to achieve its annual objectives and drive sustainable long-term value creation." | 5-#4 | |

REPEATED_CLAIM: items #1, #5, #11 restate the same "stabilization /
consolidation / risk management" framing near-verbatim three times within one
document (lines 54, 85-88, 109-111).

## 7. Every Number Stated — Business/Financial (14)

| # | Line | Value | Context | Flags |
|---|------|-------|---------|-------|
| 1 | 50 | ₹125 Cr | Revenue, Q1 FY27 | |
| 2 | 51 | ₹985 Cr | Pending orderbook incl. LOI (first citation) | |
| 3 | 68 | ₹125 Cr | Consolidated revenue, Q1 FY27 (repeat citation) | |
| 4 | 68 | ₹9.2 Cr | EBITDA, Q1 FY27 | |
| 5 | 74 | ~₹315 Cr | Order booking, Q1 FY27 (highest ever) | |
| 6 | 74 | ~₹540 Cr | Order booking, YTD | |
| 7 | 75 | ₹150 Cr (more than) | Thermal Power plant order booked | |
| 8 | 78 | "two" | Proprietary license products bagged | |
| 9 | 80 | "Two" | Large Air-Cool Heat Exchangers, execution started (Germany customer) | |
| 10 | 89 | ₹985 Cr | Pending orderbook incl. LOI (repeat citation) | |
| 11 | 89 | ~₹240 Cr | Of which booked for FY28 | |
| 12 | 100 | 61% | Orderbook — Domestic share | |
| 13 | 101 | 39% | Orderbook — Exports share | |
| 14 | 102 | ₹1,100 Cr | Order inquiry pipeline | |

## 8. Every Number Stated — Administrative / Identifier (23 matched lines; 2 lines carry 3 sub-values each)

| # | Line(s) | Value(s) | Context |
|---|---------|----------|---------|
| 1 | 2 | 06th August, 2026 | Letter date |
| 2 | 8 | Mumbai - 400 001 | BSE address PIN |
| 3 | 9 | Mumbai - 400 051 | NSE address PIN |
| 4 | 10 | 542460 | BSE Security Code |
| 5 | 15 | 30th June, 2026 | Quarter end date (Sub line) |
| 6 | 17-18 | Regulation 30, 2015 | SEBI LODR reference (Ref. line, 1st citation) |
| 7 | 20-21 | Regulations 30, 2015 | SEBI LODR reference (Pursuant clause, 2nd citation) |
| 8 | 22-23 | 30th June, 2026 | Quarter end date (Pursuant clause, repeat) |
| 9 | 37 | 2026.08.06 | Signature date |
| 10 | 38 | 12:53:53 +05'30' | Signature time |
| 11 | 41 | A57117 | Company Secretary membership number |
| 12 | 56 | August 06, 2026 | Press-release dateline date (repeat of letter date) |
| 13 | 60 | 30 June 2026 | Quarter end date (dateline paragraph, 3rd citation) |
| 14 | 94 | 66 KV | Registered office address descriptor (electrical sub-station), page 2 footer |
| 15 | 95 | L29306GJ2017PLC099085 | CIN, page 2 footer (1st citation) |
| 16 | 96 | +91 79 2287 0642 (fax); +91 79 2287 2823 and 2287 0622 (tel) | Page 2 footer contact numbers — 3 sub-values on one line |
| 17 | 130 | +91 79402 58900 | Lay Desai (CS) phone |
| 18 | 148 | 66 KV | Registered office address descriptor, page 3 footer (repeat) |
| 19 | 149 | L29306GJ2017PLC099085 | CIN, page 3 footer (2nd citation) |
| 20 | 150 | +91 79 2287 0642 (fax); +91 79 2287 2823 and 2287 0622 (tel) | Page 3 footer contact numbers — 3 sub-values on one line, repeat |

(Rows 6, 7 and 16, 20 each bundle multiple raw digit-tokens into one cited
disclosure fact per the table above; the line-count basis used for GATE A2 —
23 — counts each of the 20 rows above by its matched line(s), with rows 16
and 20 each contributing 3 raw numeric tokens, reconciling to the 24 discrete
values enumerated across all rows.)

## 9. Letterhead / Boilerplate Footer Blocks (2 — identical content, repeated)

| # | Line(s) | Content |
|---|---------|---------|
| 1 | 94-97 | THE ANUP ENGINEERING LIMITED; CIN L29306GJ2017PLC099085; address (Behind 66 KV Elec. Sub Station, Odhav Road, Ahmedabad-382 415, Gujarat); fax/tel/email — page 2 footer |
| 2 | 148-151 | Identical footer block repeated at end of page 3 |

## 10. IR / CS Contacts (3)

| # | Line(s) | Name | Designation | Email | Phone |
|---|---------|------|-------------|-------|-------|
| 1 | 129-130 | Lay Desai | Company Secretary | cs@anupengg.com | +91 79402 58900 |
| 2 | 129-130 | Himanshu Suthar | Sr. Manager - Investor Relations | himanshu.suthar@arvind.in | not stated |
| 3 | 132-133 | Satya Prakash Mishra (Mr.) | Group Head - Investor Relations | satyaprakash.mishra@arvind.in | not stated |

## 11. Footnotes & Disclaimers (1)

| # | Line(s) | Content |
|---|---------|---------|
| 1 | 135-143 | Standard forward-looking-statements disclaimer: statements herein may be statements of future expectations based on management's current view/assumptions, subject to known/unknown risks; no liability for any loss from use of the document; document does not constitute an offer or invitation to purchase/subscribe for shares nor forms the basis of any contract or commitment. |

## 12. Zero/Nil/Dash Standing Line Items — N/A

This document is a narrative press release with no tabular financial
statement (no P&L, balance sheet, or segment table with line items). There is
therefore no line-items table in which a ZERO_STANDING check applies.
zero_standing = 0, N/A (not a gap — the document type structurally does not
carry this).

## 13. Consolidation Entity List — N/A

No list of consolidated entities/subsidiaries/JVs is presented in this
document; only the standalone parent "The Anup Engineering Limited (ANUP)" is
named. entities = 0, N/A. No ENTITY_CHANGE check possible or applicable.

## 14. Prior-Quarter Comparison / DROPPED_SLIDE Check — could not be run

Prior-quarter ledger path supplied to this run: "none available." No
cross-quarter diff of sections/bullets/numbers present-vs-dropped could be
performed. This is a data-availability limitation for this run, not a
mismatch inside the current document, and is surfaced as a flag below for
A3/A4 awareness (a genuine dropped-disclosure signal cannot be tested this
quarter).

---

## Flags summary

- **MGMT_ABSENCE** — no named CMD/Managing Director/promoter quote is
  attributed anywhere in this press release (checked via keyword sweep for
  "Managing Director," "Chairman," "said," "commented" — zero hits). The
  entire narrative is issued in the company's voice with only CS/IR contact
  names at the foot; unusual for a results press release, which typically
  carries at least one attributed leadership quote.
- **REPEATED_CLAIM** — the "stabilization / consolidation / risk management"
  framing is restated near-verbatim three times: lines 54, 85-88, 109-111.
- **PRIOR_QUARTER_UNAVAILABLE** — no prior-quarter ledger was supplied; the
  DROPPED_SLIDE / cross-quarter silence-signal check could not be run this
  quarter (see section 14).

No ZERO_STANDING, ENTITY_CHANGE, MGMT_ABSENCE-on-transcript,
REPEAT_QUESTION, or auditor-paragraph flags apply — none of those categories
are structurally present in this document (narrative press release, no
tables, no transcript, no auditor report).

```yaml
stage: A2-enumerator
company: "ANUP"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/anup-q1fy27/work/ledger_pressrelease_anup_q1fy27.md"
counts:                      # per applicable category
  notes: 1
  line_items: 0
  zero_standing: 0
  agenda_items: 12
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 14
  slides: 3
  slide_numbers: 3
flags_raised: [MGMT_ABSENCE, REPEATED_CLAIM, PRIOR_QUARTER_UNAVAILABLE]
gate_a2: pass                # pass | fail
mismatch_note: ""            # non-empty only if gate_a2 fail
```
