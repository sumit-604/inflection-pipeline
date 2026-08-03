# A2 ENUMERATION LEDGER — INOX India (INOXINDIA) — Q1 FY27 — doctype: presentation (Q1 FY27 Result Press Release)

Source: `extract_presentation_inoxindia_q1fy27.txt` (source PDF: pressrelease_inoxindia_q1fy27.pdf, 4 pages, 182 extract lines)

NOTE ON DOCTYPE: the injected doctype label is "presentation," but the underlying
document is a 4-page results press release (regulatory covering letter + press
release body), not a slide deck. No slide numbers exist in the source. Enumeration
below uses page markers (`[page N]`) and extract line numbers as the anchor, per
the task instruction to enumerate every highlight bullet, segment mix claim, order
inflow/order book figure, consolidated highlights table row, forward statement,
CEO quote, and strategic development, plus the surrounding administrative content
(cover letter, digital signature, about-company, contact block) so that no
disclosure unit in the file is left off the ledger.

=== A2 COUNT TEST ===
category: cover_letter_items          grep_count: 11   sweep_count: 11   match: yes
category: highlight_bullets           grep_count: 5    sweep_count: 5    match: yes
category: narrative_statements        grep_count: 7    sweep_count: 7    match: yes
category: segment_mix_claims          grep_count: 4    sweep_count: 4    match: yes
category: divisional_development_claims grep_count: 13 sweep_count: 13   match: yes
category: strategic_development_bullets grep_count: 3  sweep_count: 3    match: yes
category: ceo_quote_items             grep_count: 6    sweep_count: 6    match: yes
category: consolidated_table_line_items grep_count: 3  sweep_count: 3    match: yes
category: zero_standing_line_items    grep_count: 0    sweep_count: 0    match: yes
category: forward_looking_statements  grep_count: 6*   sweep_count: 6    match: yes
category: about_company_statements    grep_count: 5    sweep_count: 5    match: yes
category: contact_block               grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===

\* forward_looking_statements grep methodology note: `grep -c` on individual
phrase strings undercounts by 2 because two of the six instances wrap across a
line break in the extract ("new opportunities" splits line 115/116; "revenue
visibility" splits line 97/98). A line-joined grep (`tr '\n' ' '` then search)
returns 6, matching the manual sweep exactly. Both methods, correctly applied,
converge on 6 — recorded above as the reconciled figure per GATE A2.

Grep commands used (illustrative, run against the extract file):
- `grep -coP "^\xef\x83\xbc"` → highlight bullet marker count (5)
- `grep -coP "\xef\x82\xb7"` → strategic-development bullet marker count (3)
- `grep -coE "^The Industrial Gases division|^The LNG Division|^During the quarter, the Cryo Scientific|^The Stainless-Steel Keg"` → segment paragraph starts (4)
- `grep -coE "^\s*(Total Revenue|EBITDA|PAT)\s+[0-9]"` → table line items (3)
- `sed -n '<range>p' | tr '\n' ' ' | grep -oE '[^.]+\.' | wc -l` → sentence counts for narrative / CEO quote / about-company blocks, manually adjusted for decimal-percentage false splits (e.g. "8.3%" incorrectly split by naive `.` boundary; corrected by re-reading full sentence)

---

## 1. Cover / Regulatory Filing Letter (page 1, lines 15-73)

| # | Line(s) | Item | Content (first ~15 words / key detail) | Flags |
|---|---------|------|------------------------------------------|-------|
| 1 | 22 | Date & internal reference | "IlL:SEC:SE:INTM:272 ... Date: 3rd August, 2026" | |
| 2 | 23-26, 29 | Addressee — BSE Limited | Corporate Relations Dept, New Trading Ring, Rotunda Bldg, Scrip Code (OCR-garbled, reads "Scr[D-Code-~046") | OCR_GARBLE |
| 3 | 24-29 | Addressee — NSE | The Manager Listing Dept, Exchange Plaza, BKC; Symbol: INOXINDIA | |
| 4 | 31 | Subject line | "Result Press Release for the Quarter ended on 30th June, 2026" | |
| 5 | 35-38 | Regulatory citation & enclosure statement | "Pursuant to Regulation 30 of the SEBI (LODR) Regulations, 2015, a copy of Press Release with respect to Unaudited Standalone and Consolidated Financial Results..." | STANDALONE_NOT_DISCLOSED (see note below) |
| 6 | 40 | Closing request | "You are requested to take the same on your record." | |
| 7 | 42-45 | Valediction | "Yours faithfully, For INOX India Limited" | |
| 8 | 46-59 | Digital signature certificate block | Digitally signed by PATEL JAYMEEN MOHANBHAI; DN string; serialNumber; postalCode 390012; Gujarat | |
| 9 | 46-59 | Signature timestamp | "Date: 2026.08.03 18:08:33 +05'30'" (same-day as press release date, no board meeting start/end time disclosed in this extract to cross-check against) | TIMESTAMP_NO_BOARD_TIME_REF |
| 10 | 63-66 | Signatory identity & enclosure note | "Jaymeen Patel, Company Secretary & Compliance..." / "Encl: As above" | |
| 11 | 71-72 | CIN & registered office footer | "CIN No.: L99999GJ1976PLC008945 ... 9th floor, KP Platina, Race Course, Vadodara - 390 007, Gujarat" (OCR-garbled digits) | OCR_GARBLE |

STANDALONE_NOT_DISCLOSED: the covering letter (row 5) states the enclosed
press release covers "Unaudited Standalone and Consolidated Financial
Results," but the press release body (Section 6 below) presents only the
Consolidated Q1 FY27 Financial Highlights table. No standalone figures
appear anywhere in the extract. Flagged for A3/A4 — either standalone
figures are omitted from this press release format (normal for this
company) or a page/table was dropped from the extraction; cannot be
resolved without a prior-quarter ledger (none supplied) or the full
results filing (separate doctype).

## 2. Highlights for Q1 FY27 — bullets (page 2, lines 84-89)

| # | Line | Bullet text | Figures | Flags |
|---|------|-------------|---------|-------|
| 1 | 85 | Revenue for Q1 FY27 grew 8.3% YoY to ₹382 Cr | 8.3%, ₹382 Cr | |
| 2 | 86 | EBITDA for first quarter rose 1.4% YoY to ₹90 Cr with EBITDA Margin of 23.5% | 1.4%, ₹90 Cr, 23.5% margin | |
| 3 | 87 | PAT for Q1 FY27 stood at ₹61 Cr with PAT Margin of 15.9% | ₹61 Cr, 15.9% margin | |
| 4 | 88 | Export Revenue stood at ₹222 Cr in Q1 FY27, contributing 58% to total revenues | ₹222 Cr, 58% | |
| 5 | 89 | Order Inflow at ₹532 Cr for the quarter, taking total order book to ₹1,686 Cr | ₹532 Cr, ₹1,686 Cr | |

## 3. Narrative / Body Paragraph — dateline paragraph (page 2, lines 91-98)

Restates and extends the highlight bullets; enumerated separately because it
carries figures/claims not in the bullets (export order book ₹1,140 Cr;
qualitative framing "positive market confidence," "revenue visibility").

| # | Line(s) | Sentence content (paraphrase) | Figures / claims | Flags |
|---|---------|-------------------------------|-------------------|-------|
| 1 | 91-92 | Dateline: INOX India released unaudited Q1 results as approved by Board of Directors | (no board meeting start/end time given) | |
| 2 | 93 | PAT ₹61 Cr for Q1 FY27 | ₹61 Cr | |
| 3 | 93 | Quarterly revenue ₹382 Cr, rising 8.3% YoY | ₹382 Cr, 8.3% | |
| 4 | 93-94 | EBITDA ₹90 Cr, up 1.4% | ₹90 Cr, 1.4% | |
| 5 | 94-95 | Exports 58% of revenue, export sales ₹222 Cr | 58%, ₹222 Cr | |
| 6 | 95-97 | Order inflows totaling ₹532 Cr, order book ₹1,686 Cr, "signifying positive market confidence and the potential of industrial and clean energy sectors" | ₹532 Cr, ₹1,686 Cr | forward-looking (cross-ref §9 row 1) |
| 7 | 97-98 | Export orders exceed ₹1,140 Cr, "providing strong revenue visibility for the coming quarters" | ₹1,140 Cr | forward-looking (cross-ref §9 row 2) |

## 4. Segment Mix Claims (revenue contribution by division)

| # | Line | Segment | % of quarter revenue | Flags |
|---|------|---------|----------------------|-------|
| 1 | 100 | Industrial Gases division | 53% | |
| 2 | 109 | LNG Division | 22% | |
| 3 | 117 | Cryo Scientific Division (CSD) | 20% | |
| 4 | 126 | Stainless-Steel Keg | not disclosed (no % given; narrative-only) | SEGMENT_MIX_INCOMPLETE |

SEGMENT_MIX_INCOMPLETE: three of four operating segments discussed in the
body carry an explicit revenue-contribution percentage (53% + 22% + 20% =
95% of revenue accounted for); the Stainless-Steel Keg segment paragraph
gives no percentage, leaving 5 points of quarterly revenue mix undisclosed
by name. A3/A4 should check whether Keg is folded into one of the other
three divisions for reporting purposes or is a genuinely separate ~5%
segment with no disclosed number.

## 5. Divisional Development / Order-Win Claims (qualitative, within segment paragraphs, pages 2-3, lines 100-129)

| # | Line(s) | Segment | Claim (paraphrase) | Flags |
|---|---------|---------|----------------------|-------|
| 1 | 100-103 | Industrial Gases | Major order from space exploration industry for large cryogenic storage tanks, plus order for six additional tanks from same customer | |
| 2 | 103-104 | Industrial Gases | Disposable cylinder business — healthy repeat orders from customers across global markets | |
| 3 | 104-106 | Industrial Gases | Entered semiconductor infrastructure space — initial orders for transportation tanks for semiconductor manufacturing facilities in Dholera | |
| 4 | 106-107 | Industrial Gases | Cryoseal liquid cylinder business gaining traction in India — dealer network expansion + manufacturing automation | |
| 5 | 109-111 | LNG | Decline in global LNG prices improved economic viability of LNG as transport fuel — renewed momentum in LNG fuelling infrastructure | |
| 6 | 111-112 | LNG | Secured multiple orders for LNG fuelling stations; strengthening leadership in LNG semi-trailer segment | |
| 7 | 112-114 | LNG | Installation activities commenced — first batch of large storage tanks delivered to mini-LNG terminal project site, The Bahamas | |
| 8 | 114-116 | LNG | Bahamas project initial success created new opportunities for satellite LNG stations | forward-looking (cross-ref §9 row 3) |
| 9 | 117-121 | CSD | Order from CERN for manufacture of specialized cryogenic modules for particle physics research facility | |
| 10 | 123-124 | CSD | Repeat order from ITER, France, strengthening position in advanced scientific cryogenic engineering | |
| 11 | 126-127 | Stainless-Steel Keg | Continued executing orders from leading global customers; expanding engagement with strategic brewery partners | |
| 12 | 127-128 | Stainless-Steel Keg | Approved customer base now includes Heineken, AB InBev, Molson Coors — over 40% of global beer market volumes | |
| 13 | 129 | Stainless-Steel Keg | Continued expanding portfolio of specialized non-standard keg variants | |

## 6. Strategic Developments — bulleted list (page 3, lines 131-140)

| # | Line(s) | Development | Flags |
|---|---------|-------------|-------|
| 1 | 132-134 | Strategic partnership with WAYOUT, Sweden, for manufacturing modular water micro-factories in India | |
| 2 | 135-137 | Received AS9100D aerospace quality certification — enables manufacture of aerospace components for onboard flight applications, "significantly expanding its addressable aerospace market" | forward-looking (cross-ref §9 row 4) |
| 3 | 138-140 | Partnered with ITM SLS Baroda University for a skill development center in semiconductor pipeline fabrication / orbital welding, supporting India's Semiconductor Mission | |

## 7. CEO Quote — Deepak Acharya, Chief Executive Officer (page 3, lines 142-154)

| # | Line(s) | Content | Figures / claims | Flags |
|---|---------|---------|-------------------|-------|
| 0 | 142 | Attribution: Deepak Acharya, Chief Executive Officer – INOX India Limited | | |
| 1 | 142-144 | "Highest-ever quarterly order inflow of approximately ₹532 crore, taking our current order book to a record ₹1,686 crore" | ₹532 cr (record framing), ₹1,686 cr (record framing) | cross-ref §8 |
| 2 | 144-146 | "Our export order book now exceeds ₹1,140 crore, reflecting... and providing strong revenue visibility for the coming quarters" | ₹1,140 cr | forward-looking (cross-ref §9 row 5) |
| 3 | 146-149 | "Stronger presence in high-growth segments through repeat orders from aerospace, entry into India's semiconductor ecosystem, prestigious orders from CERN and ITER, continued progress across LNG infrastructure" | (qualitative recap, no new figures) | |
| 4 | 149-151 | "Received the AS9100D aerospace quality certification... partnerships in semiconductor skill development and sustainable water solutions reinforce our focus on building new growth platforms" | (qualitative recap) | |
| 5 | 151-154 | "Backed by a record order book, diversified end markets, expanding global footprint and continued investments... we remain confident of delivering sustainable long-term growth and creating enduring value for our stakeholders" | | forward-looking (cross-ref §9 row 6) |

## 8. Consolidated Q1 FY27 Financial Highlights — table (page 3, lines 156-166)

Table caption (line 156): "Consolidated Q1 FY27 Financial Highlights (₹ crore)"
Column headers (line 159): Particulars | Q1 FY27 | Q1 FY26 | % Y-o-Y | FY26

| # | Line | Particulars | Q1 FY27 | Q1 FY26 | % Y-o-Y | FY26 | Flags |
|---|------|-------------|---------|---------|---------|------|-------|
| 1 | 161 | Total Revenue | 382 | 352 | 8.3% | 1,632 | |
| 2 | 163 | EBITDA | 90 | 88 | 1.4% | 388 | |
| 3 | 165 | PAT | 61 | 61 | 0% | 258 | flat YoY PAT (0%) — not a ZERO_STANDING item (values 61/61 are nonzero; growth rate happens to be flat) |

zero_standing count for this table: 0 (no line item is zero/nil/dash in
any disclosed period — only three line items shown; no balance-sheet or
cash-flow line items appear in this press release table).

No standalone table present in the extract — see STANDALONE_NOT_DISCLOSED
flag under Section 1, row 5.

## 9. Forward-Looking Statements (distinct phrases, cross-referenced to their source location)

| # | Line(s) | Location | Phrase | Flags |
|---|---------|----------|--------|-------|
| 1 | 96-97 | Narrative body (§3 row 6) | "signifying positive market confidence and the potential of industrial and clean energy sectors" | |
| 2 | 97-98 | Narrative body (§3 row 7) | "providing strong revenue visibility for the coming quarters" | |
| 3 | 115-116 | LNG divisional para (§5 row 8) | "has also created new opportunities for satellite LNG stations" | |
| 4 | 136-137 | Strategic developments (§6 row 2) | "significantly expanding its addressable aerospace market" | |
| 5 | 145-146 | CEO quote (§7 row 2) | "providing strong revenue visibility for the coming quarters" (repeat phrase, distinct location) | REPEAT_PHRASE (body + quote) |
| 6 | 151-154 | CEO quote (§7 row 5) | "we remain confident of delivering sustainable long-term growth and creating enduring value for our stakeholders" | |

## 10. About INOX India Ltd — boilerplate section (page 3-4, lines 168-179)

| # | Line(s) | Sentence content | Flags |
|---|---------|-------------------|-------|
| 1 | 168-171 | Company description: one of the largest manufacturers of Cryogenic Storage, Re-gas and Distribution Systems for LNG, Industrial Gases and Cryo-Scientific applications; operations in India, Brazil & Europe | |
| 2 | 171-172 | User base spread across 100+ countries; after-sales support network in 30+ countries | |
| 3 | 172-173 | "The company is leading India's efforts to use LNG for industrial and automotive use" | |
| 4 | 173-179 | Key strength: design engineering, manufacturing, supply and commissioning of Cryogenic turnkey packaged systems, vision to deliver higher value to consumers | |
| 5 | 178-179 | "For more information, please visit www.inoxcva.com" | |

## 11. Contact Information Block (page 4, lines 181-182)

| # | Line(s) | Content | Flags |
|---|---------|---------|-------|
| 1 | 181-182 | "For more information, contact: Puneet Gupta \| puneet.gupta@inoxcva.com" | |

## Page structure reference

| Page | Lines | Content type |
|------|-------|--------------|
| 1 | 15-73 | Regulatory covering letter to BSE/NSE + digital signature |
| 2 | 75-119 | Highlights bullets, narrative body para, Industrial Gases + LNG divisional paras, CSD para begins |
| 3 | 121-174 | CSD para continues, SS Keg para, Strategic Developments, CEO quote, Consolidated table, About section begins |
| 4 | 176-182 | About section continues, contact block |

---

## Flags summary (all rows)

- STANDALONE_NOT_DISCLOSED — cover letter cites standalone + consolidated results; only consolidated table appears in the body (Section 1 row 5 / Section 8 note)
- SEGMENT_MIX_INCOMPLETE — Stainless-Steel Keg segment has no disclosed revenue % contribution vs. 53%/22%/20% for the other three (Section 4 row 4)
- OCR_GARBLE — Scrip code and CIN numeral strings are OCR-corrupted in the extract (Section 1 rows 2, 11)
- TIMESTAMP_NO_BOARD_TIME_REF — digital signature timestamp (18:08:33) present but no board meeting start/end time is disclosed anywhere in this extract to cross-check same-day sequencing (Section 1 row 9)
- REPEAT_PHRASE — "providing strong revenue visibility for the coming quarters" appears verbatim in both the narrative body and the CEO quote (Section 9 rows 2 and 5)
