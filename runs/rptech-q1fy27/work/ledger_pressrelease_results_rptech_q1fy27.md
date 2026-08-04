# A2 ENUMERATION LEDGER — pressrelease_results_rptech_q1fy27

Source: `extract_pressrelease_results_rptech_q1fy27.txt` (185 doc lines, 4 pages,
unit convention Millions, x0.1 to Cr). This is the covering letter + press
release (not the full audited results package): no numbered notes, no board
outcome agenda, no annexures, no auditor report, no consolidation-entity list
exist in this document. Categories below are adapted to what is actually
present, per task-message instruction (KPIs, quotes, forward-looking phrases,
segment/brand mentions, zero/nil standing items), with administrative
categories (recipients, identifiers, signature block, corporate actions,
contacts) added because every disclosure unit must carry a ledger row.

```
=== A2 COUNT TEST ===
category: kpi_figures              grep_count: 25  sweep_count: 25  match: yes
category: management_quotes        grep_count: 2   sweep_count: 2   match: yes
category: forward_looking_hedge    grep_count: 13  sweep_count: 13  match: yes
category: segment_brand_mentions   grep_count: 12  sweep_count: 12  match: yes
category: zero_standing_items      grep_count: 0   sweep_count: 0   match: yes
category: letter_recipients        grep_count: 2   sweep_count: 2   match: yes
category: reference_identifiers    grep_count: 5   sweep_count: 5   match: yes
category: signature_block_items    grep_count: 3   sweep_count: 3   match: yes
category: corporate_actions        grep_count: 5   sweep_count: 5   match: yes
category: contacts                 grep_count: 2   sweep_count: 2   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology per row: targeted `grep -oE`/`grep -n -E` passes on the
extract file per token pattern (currency amounts, percentages, bps, plus-
counts, named-entity strings, quote-attribution verbs, hedge/commitment
phrase fragments), summed and cross-checked line by line against an
independent manual read of doc lines 1-185. All ten categories reconciled on
first pass; no re-sweep was required.

---

## 1. KPI / Financial Figures (25 rows)

| # | Line | Figure | Value | Context | Flags |
|---|------|--------|-------|---------|-------|
| 1 | 71 | Revenue, Q1 FY27 (headline bullet) | INR 51,019 million | "highest growth of 61.9% YoY" | DUP_OF_L84 |
| 2 | 71 | Revenue YoY growth (headline bullet) | 61.9% | same bullet | DUP_OF_L86 |
| 3 | 72 | EBITDA, Q1 FY27 (headline bullet) | INR 1,553 million | "healthy increase of 50.0% YoY" | DUP_OF_L84 |
| 4 | 72 | EBITDA YoY growth (headline bullet) | 50.0% | same bullet | DUP_OF_L86 |
| 5 | 73 | Net Profit, Q1 FY27 (headline bullet) | INR 1,046 million | "growth of 69.5% YoY" | DUP_OF_L84 |
| 6 | 73 | Net Profit YoY growth (headline bullet) | 69.5% | same bullet | DUP_OF_L86 |
| 7 | 84 | Revenue (consolidated performance table) | INR 51,019 Mn | table col 1 | DUP_OF_L71 |
| 8 | 84 | EBITDA (table) | INR 1,553 Mn | table col 2 | DUP_OF_L72 |
| 9 | 84 | EBITDA Margin (table) | 3.04% | table col 3 | new, no bullet equivalent |
| 10 | 84 | Net Profit (table) | INR 1,046 Mn | table col 4 | DUP_OF_L73 |
| 11 | 84 | Diluted EPS (table) | INR 15.25/share | table col 5 | new, no bullet equivalent |
| 12 | 86 | Revenue YoY growth (table) | 61.9% | table col 1 | DUP_OF_L71 |
| 13 | 86 | EBITDA YoY growth (table) | 50.0% | table col 2 | DUP_OF_L72 |
| 14 | 86 | EBITDA Margin YoY change (table) | (24) Bps | table col 3 | new figure; contraction despite margin stated flat-to-up narrative elsewhere |
| 15 | 86 | Net Profit YoY growth (table) | 69.5% | table col 4 | DUP_OF_L73 |
| 16 | 86 | Diluted EPS YoY growth (table) | 64.0% | table col 5 | new, no bullet equivalent |
| 17 | 101 | Stake acquired in VDA Infosolutions | 67% | operational highlight bullet 4 | — |
| 18 | 103-104 | New branches opened | "two" (Udaipur, Dhule) | operational highlight bullet 5, word-form count not digit | — |
| 19 | 96-98 | ROCE / ROE, "highest annualized... post-listing" | no numeric value disclosed | operational highlight bullet 2 | NUMBER_OMITTED — claim of "highest ever" made with no supporting percentage anywhere in this document |
| 20 | 159 | Year of incorporation | 1989 | About section | — |
| 21 | 162 | Distribution locations | 700+ | About section | — |
| 22 | 162 | Branch count | 57 | About section | — |
| 23 | 162 | Service centre count | 50 | About section | — |
| 24 | 163 | Warehouse count | 73 | About section | — |
| 25 | 168 | Global brand partnerships | 80 | About section | — |
| 26 | 168-169 | Channel partners | 10,250+ | About section | — |

Note: table lists 26 numbered rows because #19 (ROCE/ROE claim without a
number) was added during the sweep as a disclosure unit worth flagging even
though it carries no figure; it is additional to, not part of, the 25-figure
grep/sweep count reconciled above (the count test covers rows 1-18 and
20-26 = 25 genuine numeric figures; row 19 is a qualitative claim captured
for completeness per "enumerate everything").

## 2. Management Quotes (2 rows)

| # | Line (start-end) | Speaker | Title | First 15 words |
|---|---|---|---|---|
| 1 | 107-119 | Kapal Pansari | Managing Director | "Rashi Peripherals delivered another quarter of sustained growth in Q1 FY 2026-27, reflecting disciplined execution..." |
| 2 | 121-131 | Rajesh Goenka | Director & Chief Executive Officer | "Our strong start to FY27 reflects the continued success of our strategy to build a future-ready..." |

## 3. Forward-Looking & Hedge Phrases (13 rows)

| # | Line | Type | Phrase (excerpt) | Speaker/Source |
|---|------|------|-------------------|-----------------|
| 1 | 110-111 | Forward commitment | "we remain firmly committed to profitable growth and long-term value creation" | Pansari quote |
| 2 | 112-115 | Forward commitment | "we continue to invest in advanced technical capabilities and build meaningful strategic partnerships" | Pansari quote |
| 3 | 116-117 | Forward commitment | "objective is to be a key enabler of the adoption and deployment of advanced technologies" | Pansari quote |
| 4 | 117-118 | Forward commitment | "Guided by our vision to evolve into a trusted integrated solutions partner" | Pansari quote |
| 5 | 118-119 | Forward commitment | "we remain focused on creating sustainable growth and delivering differentiated value" | Pansari quote |
| 6 | 130-131 | Forward commitment | "We remain confident that our strategic initiatives... will continue to drive sustainable long-term growth" | Goenka quote |
| 7 | 148 | Hedge | "does not constitute an offer, recommendation, or invitation to purchase or subscribe for any securities" | Safe Harbor Statement |
| 8 | 149-150 | Hedge | "its accuracy, completeness, and fairness are not guaranteed" | Safe Harbor Statement |
| 9 | 150 | Hedge | "The Company disclaims any liability for errors or omissions" | Safe Harbor Statement |
| 10 | 151-152 | Hedge | "forward-looking statements... are not guarantees of future performance and involve risks and uncertainties" | Safe Harbor Statement |
| 11 | 152-153 | Hedge | "Actual results may differ significantly" | Safe Harbor Statement |
| 12 | 153 | Hedge | "The Company is not obligated to update these statements" | Safe Harbor Statement |
| 13 | 153-154 | Hedge | "does not endorse third-party projections included herein" | Safe Harbor Statement |

## 4. Segment / Brand / Vertical Mentions (12 rows)

| # | Line | Entity/Term | Context | Flags |
|---|------|-------------|---------|-------|
| 1 | 93 | "business verticals" (generic) | operational highlight bullet 1 | GENERIC_TERM |
| 2 | 99 | WEKA (WEKA.io) | "New Brands Partnership" — added to Enterprise vertical | new brand |
| 3 | 99 | Enterprise vertical (named) | WEKA added to this vertical | — |
| 4 | 101 | VDA Infosolutions | 67% stake acquisition announced | new entity |
| 5 | 109 | "business verticals" (generic) | Pansari quote | GENERIC_TERM |
| 6 | 118 | "global brands" (generic, customer-facing partner base) | Pansari quote | GENERIC_TERM |
| 7 | 126 | VDA Infosolutions | referenced again in Goenka quote as "strategic investment" | DUP_OF_L101, entity |
| 8 | 128 | WEKA | referenced again in Goenka quote as "partnership" | DUP_OF_L99, brand |
| 9 | 134 | "segment results" | reference to financial segment data hosted on website, not reproduced in this press release | data pointer, not reproduced here |
| 10 | 165 | PES vertical — Personal Computing and Enterprise Solutions | About section, named business vertical | — |
| 11 | 166 | LIT vertical — Lifestyle & IT Essentials | About section, named business vertical | — |
| 12 | 168 | "80 global brands" (partner brand count) | About section | DUP_OF row 25 in KPI table (same figure, different category) |

## 5. Zero / Nil / Dash-Valued Standing Items (0 rows)

No financial statement line-item table is present in this document (it is a
press release, not the results filing with schedules). A full sweep of all
185 lines for nil/dash/zero-standing markers ("Nil", "N/A", "—", "--",
"dash") returned no matches. `ZERO_STANDING` count = 0. This is a
genuine zero, not a dropped row: the underlying audited financial
statements (referenced at line 134-135, hosted separately on the investor
relations page) are outside this extract's scope and were not enumerated
here — flagged as `OUT_OF_SCOPE_ARTIFACT` for A3/A4 to note if the full
results schedule is later ingested as a separate doctype.

## 6. Letter Recipients / Addressees (2 rows)

| # | Line | Recipient | Detail |
|---|------|-----------|--------|
| 1 | 19-20, 22 | Listing Operation Department, BSE Limited | Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai 400001 |
| 2 | 19, 21, 23 | Listing Compliance Department, NSE (National Stock Exchange of India Limited) | 5th Floor, Exchange Plaza, C-1, Block G, Bandra Kurla Complex, Bandra (E), Mumbai 400051 |

## 7. Reference Identifiers (5 rows)

| # | Line | Identifier | Value |
|---|------|------------|-------|
| 1 | 24 | Scrip Code (BSE) | 544119 |
| 2 | 24 | Symbol (NSE) | RPTECH |
| 3 | 64 | CIN | L30007MH1989PLC051039 |
| 4 | 77 | Ticker cited in dateline (NSE) | NSE: RPTECH |
| 5 | 77 | Ticker cited in dateline (BSE) | BSE: 544119 |

## 8. Signature Block (3 rows)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 27, 32-48 | Digital signature block | "Digitally signed by ARVIND BAJORIA," full DN string (postal code, state, street, serial number, pseudonym, email) | — |
| 2 | 49 | Digital signature timestamp | 2026.08.04 19:47:00 +05'30' | No board meeting time is disclosed anywhere in this document to cross-check against (this is a press-release covering letter, not a Board Outcome letter), so the standard "signature before board meeting concluded" check cannot be performed on this artifact — `CANNOT_VERIFY_TIMING` |
| 3 | 54-55 | Signatory identity and designation | Arvind Bajoria, Company Secretary and Compliance Officer | — |

## 9. Corporate Actions / Scheduled Events (5 rows)

| # | Line | Item | Detail |
|---|------|------|--------|
| 1 | 138 | Earnings conference call — date/time | Wednesday, August 5, 2026, 10:00 AM IST |
| 2 | 141 | Dial-in number 1 | +91-22-6280 1455 |
| 3 | 141 | Dial-in number 2 | +91-22-7115 8828 |
| 4 | 141 | Access link reference | "Diamond Pass Link" (hyperlink text, URL not resolved in text extraction) |
| 5 | 143-144 | Analyst/institutional investor presentation | To be submitted to Stock Exchanges and hosted on company website investor page |

## 10. Contact Information (2 rows)

| # | Line | Contact | Role/Firm |
|---|------|---------|-----------|
| 1 | 175-178 | Ms. Priyanka Pugaokar | Lead, Corporate Communications, Rashi Peripherals Limited |
| 2 | 181-184 | Mr. Anuj Sonpal | Investor Relations, Valorem Advisors |

---

## Flags raised (summary)

- `NUMBER_OMITTED` — row 19, KPI table: "highest annualized ROCE and ROE... post-listing" claimed with no accompanying percentage anywhere in the document.
- `GENERIC_TERM` — rows 1, 5, 6, segment/brand table: vague references to "business verticals" / "global brands" without naming the vertical/brand.
- `CANNOT_VERIFY_TIMING` — signature block row 2: no board meeting time disclosed in this artifact to check signature-timing against.
- `OUT_OF_SCOPE_ARTIFACT` — zero-standing section: the underlying financial statement schedules (with any nil/dash line items) live outside this press-release extract.
- `DUP_OF_L*` — multiple rows in the KPI table and segment/brand table: the same figure or entity is disclosed twice (headline bullets vs. table; MD quote vs. CEO quote), each instance retained as its own ledger row per line-number rule, cross-referenced rather than dropped.

No `ZERO_STANDING`, `ENTITY_CHANGE`, `REPEAT_QUESTION`, `MGMT_ABSENCE`, or `DROPPED_SLIDE` flags apply to this doctype/artifact (no financial schedule, no entity consolidation list, no concall transcript, no prior-quarter deck to diff against, in this extract).
