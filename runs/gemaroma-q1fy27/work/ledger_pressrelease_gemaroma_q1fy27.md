# A2 ENUMERATOR LEDGER — GEMAROMA Q1FY27 — pressrelease doctype (routed as "presentation")

Source: extract_pressrelease_gemaroma_q1fy27.txt (5-page press release + Reg-30 cover letter,
238 extract lines, no slide-deck structure, no financial statement grid — only two summary
comparison tables). Per injected task instructions, and since this is the first-time coverage
of GEMAROMA (no prior ledger to diff against — recorded as `NOT_APPLICABLE`, not a mismatch),
this document is enumerated with the presentation branch adapted to prose: every page/section
as the unit, every financial figure/metric with its line number, every management quote
(attributed speaker), and every forward-looking/guidance statement with its line number, plus
the administrative/regulatory scaffolding (cover letter, signature, disclaimer, contacts,
boilerplate) and the earnings-call announcement block that the base anti-miss mandate requires
not be dropped. Zero/nil/dash-valued figures are enumerated with `ZERO_STANDING`, never dropped.

Atomic unit chosen per category: financial table rows are counted as one row per metric per
table (both YoY and QoQ comparator cells listed in full within the row, not split out).
Narrative figures/facts are counted as one row per discrete quantified fact. Management quote
paragraphs (blank-line-delimited) are counted separately from the forward-looking/guidance
statements they also contain — this is an intentional double-lens enumeration (utterance-unit
vs claim-unit), not a duplicate miss; noted explicitly so A3/A4 do not treat it as an error.

```
=== A2 COUNT TEST ===
category: pages_sections                grep_count: 5    sweep_count: 5    match: yes
category: financial_table_line_items    grep_count: 18   sweep_count: 18   match: yes
category: narrative_figures_facts       grep_count: 21   sweep_count: 21   match: yes
category: management_quote_paragraphs   grep_count: 5    sweep_count: 5    match: yes
category: forward_looking_guidance      grep_count: 13   sweep_count: 13   match: yes
category: regulatory_administrative     grep_count: 8    sweep_count: 8    match: yes
category: earnings_call_announcement    grep_count: 12   sweep_count: 12   match: yes
gate_a2: pass
total_disclosure_units: 82
=== END COUNT TEST ===
```

Grep commands used (all against extract_pressrelease_gemaroma_q1fy27.txt):
- pages_sections: `grep -c "\[page"` = 5
- financial_table_line_items: `grep -c -E "^\s*[0-9]+\s+(Revenue from Operations|Gross
  Profit|Gross Margin \(%\)|EBITDA\s+[0-9]|EBITDA Margin \(%\)|PAT\s+[0-9-]|PAT Margin
  \(%\)|EPS \(Rs\)|Cash PAT)"` = 18 (9 rows x 2 tables; anchored to avoid matching the two
  bullet-header false positives at lines 112 and 121 which reuse the label text in prose)
- narrative_figures_facts: `grep -o -E "9\.1 Cr|265 Cr|Established in 1997|nearly three
  decades|over 80 products|240 domestic|44 global|across 20 countries|three manufacturing
  facilities|16,171 MTPA|ISO 9001:2015|ISO 14001:2015|ISO 45001:2018|FSSC 22000|ISO
  22000:2018|ISO TS 22002-1:2009|Colgate-Palmolive|Dabur|Patanjali|SH Kelkar|Symrise" | wc -l`
  = 21
- management_quote_paragraphs: `grep -c -E "^\s*[0-9]+\s+("Q1FY27 witnessed|We are seeing
  continued progress|Innovation and R&D remain central|We continue to strengthen our
  international|We remain committed to disciplined execution)"` = 5 (blank-line-delimited
  paragraph starts within the attributed quote, lines 157-173; cross-checked against 4
  internal blank-line separators = 5 paragraphs)
- forward_looking_guidance: 13 single-line anchor phrases (chosen because several source
  sentences wrap across print-lines, which breaks whole-phrase grep; anchors picked from the
  unwrapped portion of each sentence) = 13, matching manual sweep of 13 distinct forward
  statements across pages 3 and 4
- regulatory_administrative: `grep -c -E "BSE Limited|Subject: Submission of Press
  Release|Pursuant to Regulation 30|Digitally signed by|Rounded off to nearest decimal|
  approved the incorporation of a Wholly Owned Subsidiary in Brazil|Update on Krystal
  Ingredients Pvt\. Ltd|Certain statements in this document that are not historical facts"` = 8
- earnings_call_announcement: `grep -o -E "Friday, 14th August 2026 \| 4:00 PM \(IST\)|Yash
  Parekh \(MD & CEO\)|Kaksha Parekh \(WTD, Chairperson & CFO\)|Shrenik Vora \(Non-executive
  Director\)|Aadit Shah|\+91 22 6280 1256|\+91 22 7115 8157|Hong Kong: 800964448|Singapore:
  8001012045|UK: 08081011573|USA: 18667462133|Diamond Pass Link" | wc -l` = 12

---

## 1. PAGES / SECTIONS (5)

| # | Line | Page | Section content | Flags |
|---|------|------|------------------|-------|
| P1 | 1 | Page 1 | Reg-30 cover letter to BSE & NSE, addressees, subject, regulatory citation, signatory | |
| P2 | 57 | Page 2 | Q1FY27 Press Release headline + Standalone Financial Highlights table + Consolidated Financial Highlights table | |
| P3 | 106 | Page 3 | Key Business Highlights (5 narrative bullets: Revenue, Gross/EBITDA Margin, PAT, Brazil expansion, Krystal Ingredients update) | |
| P4 | 151 | Page 4 | MD & CEO attributed quote (Mr. Yash Vipul Parekh) + Q1FY27 Earnings Call Details block | |
| P5 | 195 | Page 5 | "About Gem" company boilerplate + Contact Us + Disclaimer | |

## 2. FINANCIAL TABLE LINE ITEMS (18: 9 Standalone + 9 Consolidated)

### 2a. Standalone Financial Highlights (header line 70)

| # | Line | Metric | Q1FY27 | Q1FY26 | Y-o-Y % | Q4FY26 | Q-o-Q % | Flags |
|---|------|--------|--------|--------|---------|--------|---------|-------|
| S1 | 71 | Revenue from Operations (Rs Cr) | 83.0 | 76.4 | 8.6% | 112.2 | -26.1% | |
| S2 | 72 | Gross Profit (Rs Cr) | 14.7 | 19.1 | -23.2% | 26.2 | -44.0% | |
| S3 | 74 | Gross Margin (%) | 17.7% | 25.0% | -734 bps | 23.4% | -566 bps | |
| S4 | 75 | EBITDA (Rs Cr) | 8.5 | 10.5 | -19.0% | 15.1 | -43.4% | |
| S5 | 77 | EBITDA Margin (%) | 10.3% | 13.8% | -350 bps | 13.4% | -315 bps | |
| S6 | 78 | PAT (Rs Cr) | 7.3 | 6.5 | 11.0% | 11.9 | -39.0% | |
| S7 | 80 | PAT Margin (%) | 8.7% | 8.5% | 18 bps | 10.6% | -185 bps | |
| S8 | 82 | EPS (Rs) | 1.4 | 1.4 | (blank) | 2.3 | (blank) | `ZERO_STANDING` — YoY% and QoQ% growth cells are blank in the source table for this row while every other row in both tables carries a populated growth figure; no dash/nil marker printed, cell is simply empty |
| S9 | 83 | Cash PAT (Depreciation + PAT) (Rs Cr) | 8.9 | 8.0 | 11.1% | 13.3 | -33.3% | |

### 2b. Consolidated Financial Highlights (header line 87)

| # | Line | Metric | Q1FY27 | Q1FY26 | Y-o-Y % | Q4FY26 | Q-o-Q % | Flags |
|---|------|--------|--------|--------|---------|--------|---------|-------|
| C1 | 88 | Revenue from Operations (Rs Cr) | 98.9 | 87.6 | 12.8% | 110.4 | -10.5% | |
| C2 | 90 | Gross Profit (Rs Cr) | 16.5 | 25.9 | -36.2% | 33.7 | -51.0% | |
| C3 | 91 | Gross Margin (%) | 16.7% | 29.5% | -1282 bps | 30.5% | -1384 bps | |
| C4 | 93 | EBITDA (Rs Cr) | 3.3 | 14.9 | -77.7% | 15.7 | -79.0% | |
| C5 | 95 | EBITDA Margin (%) | 3.3% | 17.0% | -1361 bps | 14.2% | -1089 bps | |
| C6 | 97 | PAT (Rs Cr) | -7.9 | 8.0 | -198.6% | 1.0 | -877.3% | consolidated PAT swung to a loss; standalone PAT (S6) stayed positive and grew 11.0% YoY in the same quarter — the standalone/consolidated divergence is itself a disclosure unit, flagged for A3/A4 |
| C7 | 99 | PAT Margin (%) | -8.0% | 9.1% | -1708 bps | 0.9% | -888 bps | |
| C8 | 101 | EPS (Rs) | -1.6 | 1.7 | (blank) | 0.2 | (blank) | `ZERO_STANDING` — same blank YoY%/QoQ% pattern as S8 |
| C9 | 102 | Cash PAT (Depreciation + PAT) (Rs Cr) | 1.3 | 9.8 | -87.2% | 10.0 | -87.5% | |

Table-level footnote: line 104, "Rounded off to nearest decimal" — qualifies every cell in
both tables above (S1-S9, C1-C9). Listed in full at Section 6, item R5.

## 3. NARRATIVE FINANCIAL / OPERATING FIGURES & COMPANY FACTS (21, outside the two summary tables)

| # | Line | Figure / fact | Context | Flags |
|---|------|-----|---------|-------|
| N1 | 128 | Rs. 9.1 Cr | Higher depreciation, Q1FY27, cited as a driver of the PAT decline | |
| N2 | 129 | ~Rs. 265 Cr | Total capex incurred for the Dahej facility (cumulative, approximate) | `APPROX_VALUE` |
| N3 | 200 | Established in 1997 | Company founding year | |
| N4 | 201 | Nearly three decades | Stated length of management team's industry experience | qualitative approximation, not a precise figure |
| N5 | 204 | Over 80 products | Product portfolio size | qualitative approximation ("over") |
| N6 | 207 | 240 domestic customers | Customer count, "over 240" | qualitative approximation |
| N7 | 207 | 44 global customers | Customer count | |
| N8 | 208 | 20 countries | Geographic customer spread | |
| N9 | 211 | Three manufacturing facilities | Facility count (Uttar Pradesh, Gujarat, Daman & Diu) | |
| N10 | 212 | 16,171 MTPA | Installed capacity | |
| N11 | 212 | ISO 9001:2015 | Certification held | |
| N12 | 212 | ISO 14001:2015 | Certification held | |
| N13 | 212 | ISO 45001:2018 | Certification held | |
| N14 | 213 | FSSC 22000 | Certification held | |
| N15 | 213 | ISO 22000:2018 | Certification held | |
| N16 | 213 | ISO TS 22002-1:2009 | Certification held | |
| N17 | 209 | Colgate-Palmolive | Named partner brand | |
| N18 | 209 | Dabur | Named partner brand | |
| N19 | 209 | Patanjali | Named partner brand | |
| N20 | 209 | SH Kelkar | Named partner brand | |
| N21 | 209 | Symrise | Named partner brand | "and others" (line 209) is an unquantified residual — not counted as a discrete fact |

## 4. MANAGEMENT QUOTE (attributed speaker: Mr. Yash Vipul Parekh, MD & CEO — attribution at line 155, quote body lines 157-173)

| # | Line | Paragraph (blank-line delimited) | First 15 words | Flags |
|---|------|-----------------------------------|-----------------|-------|
| Q1 | 157-159 | Para 1 | "Q1FY27 witnessed YoY growth in revenue from operations, while the business continued to operate in a..." | overlaps with FL1 below (double-lens, see header note) |
| Q2 | 161-162 | Para 2 | "We are seeing continued progress in customer engagement and product qualification. Our focus remains on..." | overlaps with FL10 |
| Q3 | 164-166 | Para 3 | "Innovation and R&D remain central to our long-term strategy, with continued focus on process innovation, product..." | overlaps with FL11 |
| Q4 | 168-169 | Para 4 | "We continue to strengthen our international presence, with the proposed Brazil subsidiary expected to enhance..." | overlaps with FL12; restates the Brazil expansion item first disclosed at N/A — see Section 6 item R6 |
| Q5 | 171-173 | Para 5 | "We remain committed to disciplined execution and sustainable value creation, with our focus now on progressively..." | overlaps with FL13 |

No other attributed management quote appears anywhere else in the document. `MGMT_ABSENCE` is
not applicable here (this is a press release, not a concall transcript with a roll call).

## 5. FORWARD-LOOKING / GUIDANCE STATEMENTS (13)

| # | Line | Statement | Flags |
|---|------|-----------|-------|
| FL1 | 117-119 | Revenue contribution from newer product verticals "expected to build progressively as customer approvals and qualifications are completed and volumes ramp up" | |
| FL2 | 123-125 | "the Company expects a stronger product mix and operating leverage to support a gradual improvement in margins" | |
| FL3 | 129-130 | "the Company expects operating leverage to support profitability going forward" | |
| FL4 | 139-141 | Krystal Ingredients Cooling Agents: "business is expected to make a revenue contribution from Q3FY27 as customer qualifications are completed and commercial supplies scale up" | |
| FL5 | 142-144 | Krystal Ingredients Safranal: "Revenue contribution is expected to commence towards the end of Q2FY27, with a more meaningful contribution from Q3FY27" | |
| FL6 | 145-146 | Krystal Ingredients Phenol Derivatives: "Trial production is expected to commence towards the end of Q2FY27" | |
| FL7 | 146-147 | Krystal Ingredients Phenol Derivatives: "Commercial production is targeted during Q3FY27, subject to completion of the required approvals and quality processes" | |
| FL8 | 147-148 | Krystal Ingredients Phenol Derivatives: "meaningful revenue contribution expected from Q4FY27" | three sequential timeline commitments (FL6/FL7/FL8) for a single product line, each a separate, falsifiable date-bound claim |
| FL9 | 157-159 | MD quote: focus "shifting towards utilizing and monetising the expanded manufacturing platform at Dahej and scaling the newer product categories through Krystal Ingredients" | =Q1 |
| FL10 | 161-162 | MD quote: "Our focus remains on converting these opportunities into recurring commercial business as they scale" | =Q2 |
| FL11 | 164-166 | MD quote: R&D/innovation strategic focus statement, "central to our long-term strategy" | =Q3 |
| FL12 | 168-169 | MD quote: "the proposed Brazil subsidiary expected to enhance our distribution reach in Latin America" | =Q4; Brazil subsidiary is board-approved but not yet incorporated (see R6) — this is guidance on an outcome not yet realized |
| FL13 | 171-173 | MD quote: closing commitment — "progressively scaling Krystal Ingredients' Dahej facility, strengthening our product capabilities and expanding our presence across global markets" | =Q5 |

The safe-harbor disclaimer (lines 232-237, Section 6 item R8) qualifies all 13 statements above
but is itself administrative boilerplate, not a guidance statement — listed separately.

## 6. REGULATORY / ADMINISTRATIVE / CORPORATE-ACTION ITEMS (8)

| # | Line | Item | Flags |
|---|------|------|-------|
| R1 | 12-19 | Letter recipients: BSE Limited (Listing/Compliance Dept, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai) and National Stock Exchange of India Limited (Listing/Compliance Dept, Exchange Plaza, BKC, Bandra East); BSE Code 544491, NSE Symbol GEMAROMA | |
| R2 | 23-24 | Subject line: "Submission of Press Release in respect of Unaudited (Standalone & Consolidated) Financial Results for the quarter ended June 30, 2026" | |
| R3 | 26-28 | Regulatory citation: Regulation 30 and Para A of Part A of Schedule III read with Regulation 46 of the SEBI (LODR) Regulations, 2015 | |
| R4 | 38-46 | Signatory block: Akshita Deepak Gohil, Company Secretary & Compliance Officer, "For Gem Aromatics Limited," digitally signed 2026.08.13 18:58:30 +05'30' | No board-meeting start/end time is disclosed anywhere in this document, so the "signature before board meeting concluded" check cannot be run against this artifact (`NOT_APPLICABLE` — not a Board Outcome letter) |
| R5 | 104 | Table footnote: "Rounded off to nearest decimal" — qualifies all 18 financial table line items (Section 2) | |
| R6 | 133-135 | Corporate action: Company "has approved the incorporation of a Wholly Owned Subsidiary in Brazil" to distribute essential oils, aromatic chemicals and specialty chemicals in Latin America | `NEW_ENTITY_ANNOUNCED` — board-approved but not yet incorporated as of this release; no prior-quarter ledger exists to run a formal `ENTITY_CHANGE` diff (`NOT_APPLICABLE`, first-time coverage), but flagged for A3/A4 to track at next quarter's filing |
| R7 | 137 | Entity reference: Krystal Ingredients Pvt. Ltd., described as an existing Wholly Owned Subsidiary | |
| R8 | 230-237 | Disclaimer: standard forward-looking-statements safe-harbor paragraph | qualifies FL1-FL13 (Section 5) and Q1-Q5 (Section 4) |

## 7. EARNINGS CALL ANNOUNCEMENT DETAILS (12)

| # | Line | Detail | Flags |
|---|------|--------|-------|
| E1 | 179 | Call date/time: Friday, 14th August 2026, 4:00 PM (IST) | call is scheduled for the day after this press release's signature date (13 Aug 2026) — normal sequencing, no flag |
| E2 | 182 | Participant: Yash Parekh (MD & CEO) | |
| E3 | 182 | Participant: Kaksha Parekh (WTD, Chairperson & CFO) | |
| E4 | 183 | Participant: Shrenik Vora (Non-executive Director) | |
| E5 | 183 | Participant: Aadit Shah (CEO's Office) | |
| E6 | 188 | Primary dial-in number 1: +91 22 6280 1256 | |
| E7 | 188 | Primary dial-in number 2: +91 22 7115 8157 | |
| E8 | 191 | International toll free — Hong Kong: 800964448 | |
| E9 | 191 | International toll free — Singapore: 8001012045 | |
| E10 | 191 | International toll free — UK: 08081011573 | |
| E11 | 191 | International toll free — USA: 18667462133 | |
| E12 | 193 | "Diamond Pass Link" heading present with no URL/link text captured in the extract | `MISSING_VALUE` — either the link is a hyperlink not captured by text extraction, or no link was embedded in the source document; cannot distinguish from this extract alone |

---

## 8. ZERO / NIL / DASH-VALUED STANDING LINE ITEMS

Both financial tables (Standalone, Consolidated) show 9 of 9 metric rows populated with real
values in every period column except the EPS row's YoY%/QoQ% growth cells, which are blank
(S8, C8 — see Section 2). These are the only `ZERO_STANDING`-flagged items in this document;
count = 2. No table row in either table is entirely zero, nil, or dash across all periods.

---

## FLAGS RAISED (summary, deduplicated)

- `ZERO_STANDING` — 2 instances (S8, C8: EPS rows, blank YoY%/QoQ% growth cells)
- `APPROX_VALUE` — 1 instance (N2: ~Rs. 265 Cr Dahej capex)
- `NEW_ENTITY_ANNOUNCED` — 1 instance (R6: Brazil WOS, board-approved not yet incorporated)
- `MISSING_VALUE` — 1 instance (E12: Diamond Pass Link with no URL text)
- `NOT_APPLICABLE` — prior-quarter ledger not supplied (first-time GEMAROMA coverage), so
  `ENTITY_CHANGE` / `DROPPED_SLIDE` diff checks cannot be run this cycle; board-meeting-time
  cross-check not applicable (this is a press release, not a Board Outcome letter)
- Standalone/consolidated PAT divergence noted at C6 (standalone PAT +11.0% YoY vs consolidated
  PAT swinging to a Rs -7.9 Cr loss in the same quarter) — surfaced as a disclosure unit for
  A3/A4, not resolved or interpreted here per the enumerate-don't-interpret mandate

## GATE A2: PASS

All seven reconciliation categories (pages/sections, financial table line items, narrative
figures/facts, management quote paragraphs, forward-looking/guidance statements, regulatory/
administrative items, earnings call announcement details) matched grep count to manual sweep
count 1:1. Two anchor sets required correction during the sweep before they matched: (1) the
financial-table-line-items grep initially over-matched two bullet-header false positives
(lines 112, 121) that reuse table-row label text in prose — fixed by anchoring to the
line-number-prefixed table-row format; (2) several forward-looking-statement phrases wrap
across printed lines and were invisible to whole-phrase grep — fixed by re-anchoring on the
unwrapped portion of each sentence. No unresolved mismatch remains. Total disclosure units
enumerated across all categories: 82.
