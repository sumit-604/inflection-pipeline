# A2 ENUMERATION LEDGER — pacedigitk Q1FY27 — pressrelease

Source: `extract_pressrelease_pacedigitk_q1fy27.txt` (4 pages, 189 embedded content lines).
Line numbers below are the extract's own embedded line numbers (the number printed
immediately before each line's text in the source extract; verified equal to
real-file-line minus 14 throughout — no gaps).
Cross-checked against `extract_results_pacedigitk_q1fy27.txt` (unit: Millions,
Millions -> x0.1 Crores) where a results-filing counterpart could plausibly exist.

```
=== A2 COUNT TEST ===
category: disclosure_paragraphs   grep_count: 36   sweep_count: 36   match: yes
category: numbers                 grep_count: 56   sweep_count: 56   match: yes
category: forward_signals         grep_count: 7    sweep_count: 7    match: yes
category: mgmt_quote              grep_count: 1    sweep_count: 1    match: yes
category: safe_harbour            grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes (both mismatches caught by re-sweep before this table was
finalized, per GATE A2):
- `numbers`: a naive single-line grep for `[0-9]+ GWh` initially returned 55 —
  it missed the "10 GWh" target at line 158-159 because the PDF-extraction
  line wrap splits "...expand it to 10" (line 158) from "GWh." (line 159).
  A multiline-aware pass and manual sweep both confirm 56; the split instance
  is row `#56` in the numbers table below.
- `forward_signals`: a naive single-line grep for "subsequent to the quarter"
  initially returned 2 of 3 occurrences — the first instance is split across
  the line-158... no, across lines 84/85 by the extract's embedded
  line-number prefix interrupting the mid-sentence wrap ("...Subsequent to
  the" / "85 quarter, the Company..."). A multiline-aware pass plus manual
  sweep both confirm 3 "subsequent to the quarter" instances (lines 84-85,
  113, 157), giving 7 total forward-signal statements after de-duplicating
  the overlapping "on track to" / "remain(s) on track" regex hits at the
  same two locations (lines 118 and 158-159).

---

## 1. DISCLOSURE PARAGRAPHS / SECTIONS (36)

Unit = blank-line-delimited block in the extract (mechanical, reproducible
via script), which in practice merges a section heading with its
immediately-following paragraph wherever the source has no blank line
between them (e.g. "Operational Highlights – Energy" + its first paragraph
are one block because the source runs them together).

| # | Line(s) | First ~12 words / content | Notes / flags |
|---|---------|---------------------------|----------------|
| 1 | 2-10 | "Pace Digitek Limited (Formerly Known as Pace Digitek Private Limited and Pace..." | Letterhead: regd. office, phone, email, website, CIN |
| 2 | 12 | "Ref No: PDL/2026-27/Q02_24" | Reference number line |
| 3 | 14 | "Date: August 05, 2026" | Letter date |
| 4 | 16-19 | "BSE Limited / National Stock Exchange of India Ltd" (addressee block, both exchanges, addresses) | |
| 5 | 21 | "Scrip Code – 544550 / Symbol – PACEDIGITK" | |
| 6 | 24-26 | "Dear Sir/Madam, Sub: Intimation of Press Release pursuant to Regulation 30 of SEBI..." | Salutation + subject line |
| 7 | 28-31 | "Pursuant to Regulation 30 read with Schedule III of the SEBI (Listing Obligations..." | Regulatory basis paragraph — intimates unaudited standalone+consolidated results, quarter ended June 30, 2026 |
| 8 | 33-34 | "The same has also been uploaded on the Company's website which may be viewed at..." | Website reference paragraph |
| 9 | 36 | "We hereby request you to take note of the same." | Closing request |
| 10 | 40 | "Thanking You," | Sign-off |
| 11 | 42-52 | "For PACE DIGITEK LIMITED [Formerly known as Pace Digitek Private Limited...]" | Digital signature block: Meghana M P, Company Secretary and Compliance Officer, Membership No. A42534. Timestamp: 2026.08.05 19:03:22 +05'30' (line 48-49) — same calendar date as letter date (line 14); no lead/lag flag warranted (no board-meeting timestamp given in this doctype to compare against) |
| 12 | 54-55 | "Add: Plot No. V-12, Industrial Estate, Kumbalgodu, Mysore Highway, Bangalore..." | Registered address repeat under signature |
| 13 | 58-61 | "Pace Digitek Limited Delivers a Strong Start to FY2027 with Robust Revenue Growth and Continued BESS Expansion" | Headline + 2 sub-headline stat lines (revenue, order book, PAT+YoY) |
| 14 | 63-65 | "Bengaluru, Wednesday, Aug 05, 2026: Pace Digitek Limited (NSE: PACEDIGITK | BSE: 544550), an..." | Dateline / lead paragraph |
| 15 | 67-69 | "During Q1 FY2027, the Company continued expanding its execution capabilities across Energy and..." | Overview paragraph (BESS, telecom infra, manufacturing integration, lifecycle services) |
| 16 | 71 | "Financial Performance:" | Section header |
| 17 | 73-78 | "Particulars (INR crore) Q1FY27 Q1FY26 Y-o-Y FY2026 FY2025 Y-o-Y" | Summary financial table: Revenue, EBITDA, EBITDA Margin, PAT, PAT Margin rows — see Table 2 for every cell |
| 18 | 81-86 | "Operational Highlights – Energy / During the quarter, the Company has successfully delivered 90 Battery..." | Header + Energy para 1: BESS containers delivered, executable Energy order book, BESS order visibility, `FORWARD_SIGNAL` (subsequent-quarter capacity event, see Table 3 #1) |
| 19 | 88-92 | "The Company continued to strengthen its manufacturing capabilities through localization initiatives, including..." | Energy para 2: localization, C&I prototype `FORWARD_SIGNAL` (Table 3 #2) |
| 20 | 94-96 | "The Company continued to expand its presence across the Manufacturing, EPC, and selective..." | Energy para 3: Manufacturing/EPC/BOO segment expansion |
| 21 | 98-99 | "Operational Highlights – Telecom & ICT / The executable Telecom & ICT order book stood at..." | Header + Telecom para 1: order book figure |
| 22 | 101-102 | "During Q1FY2027, the Company has received an Advance Work Order from Bharat Sanchar Nigam..." | Telecom para 2, part 1 — sentence is split by a page-break artifact (blank line + "[page 3]" marker between lines 102 and 105); continues as block #23 |
| 23 | 105-106 | "(O&M) of the middle-mile & last-mile network under the BharatNet programme in the Sikkim..." | Telecom para 2, part 2/continuation — BSNL Advance Work Order, Sikkim Telecom Circle, contract value ₹264 crore. Same sentence as block #22; extraction artifact, not a content gap |
| 24 | 108-109 | "The Company continued leveraging its telecom infrastructure execution capabilities and pan-India..." | Telecom para 3 |
| 25 | 111-115 | "Execution & Manufacturing Capabilities / During Q1 FY27, Pace Digitek continued to strengthen its EPC..." | Header + Execution para 1: `FORWARD_SIGNAL` (subsequent-quarter BESS line commissioning, Table 3 #3) |
| 26 | 117-119 | "The Company also continued investing in the phased expansion of its BESS manufacturing capacity..." | Execution para 2: `FORWARD_SIGNAL` (5→10 GWh ramp target + "remains on track", Table 3 #4) |
| 27 | 121-127 | "Other Strategic Developments / During the quarter, the Company continued to strengthen its BESS..." | Header + Strategic para 1: NEC XON Systems (South Africa) OEM partnership — 5 countries named (South Africa, Botswana, Mozambique, Namibia, Mauritius) |
| 28 | 129-135 | "Following the quarter-end, Pace Digitek further strengthened its long-term growth platform through key..." | Strategic para 2: `FORWARD_SIGNAL` (subsequent-to-quarter events, Table 3 #5) — MEGMEET Electrical India strategic cooperation agreement (AI data center power infrastructure) and Pace-Lineage Research Center (Pune, ACC/energy storage R&D) |
| 29 | 137 | "Financial Highlights:" | Section header |
| 30 | 139-143 | "Key Highlights for Q1 FY27 Financial Results • Revenue from Operations stood at ₹555.4..." | Header + 3 bullets restating Revenue, EBITDA (+margin), PAT (+margin) — all figures duplicate Table 2 rows already in the summary table |
| 31 | 145-148 | "Management Commentary / Mr. Maddisetty Venugopal Rao, Chairman & Managing Director, Pace Digitek Ltd said: 'We have commenced..." | Header + quote paragraph 1 — see Table 4 |
| 32 | 151-152 | "Our executable order book remains robust at ₹10,803.3 crore, providing strong revenue visibility..." | Quote paragraph 2 |
| 33 | 154-161 | "During the quarter, we operationalized our 2.5 GWh BESS manufacturing facility, strengthened our EPC..." | Quote paragraph 3 — contains 2 `FORWARD_SIGNAL` statements (Table 3 #6, #7): NEC XON OEM partnership reference, subsequent-quarter BESS line commissioning, "remain on track to expand it to 10 GWh" |
| 34 | 164 | "About Pace Digitek:" | Section header |
| 35 | 166-180 | "Pace Digitek Limited (BSE: 544550, NSE: PACEDIGITK) is an integrated infrastructure and energy..." | Company description + energy segment (BESS, subsidiary Lineage Power Private Limited) + Telecom & ICT segment description + media/IR contact block (Ajay Tambhale, Manasa KK — Pace Digitek IR; Khushbu Singhania, Tanishka Tanvi — Go India Advisors). No blank line separates these four sub-topics in the source, so they extract as one block |
| 36 | 184-189 | "Safe Harbour: Statements in this document relating to future status, events, or circumstances..." | Safe Harbour disclaimer — see Table 5 |

---

## 2. NUMBERS / FIGURES STATED (56)

Cross-check method: searched `extract_results_pacedigitk_q1fy27.txt` (consolidated
unaudited P&L, in Millions) for each figure after unit conversion (Millions x 0.1
= Crores). Revenue from Operations and Profit After Tax for Q1FY27 / Q1FY26 / FY2026
are literal line items there (lines 438, 458) and match exactly. EBITDA, all margin
percentages, FY2025 comparatives, order book, GWh capacity, and contract-value
figures have **no line item at all** in the results filing (EBITDA is a non-GAAP
figure not disclosed in the Ind AS statement; FY2025 is outside the results
filing's comparative columns entirely; order book/GWh/contract value are
operational KPIs never carried in a statutory P&L) — all flagged `CROSS_CHECK`
below even where independently re-derivable by arithmetic from filed lines.

| # | Line | Value | Metric / context | Flag |
|---|------|-------|-------------------|------|
| 1 | 60 | ₹555.4 crore | Q1FY27 Revenue from Operations (sub-headline) | verified vs results filing (line 438, 5,553.64mn) |
| 2 | 60 | ₹10,803.3 crore | Executable Order Book, total (sub-headline) | CROSS_CHECK — no results-filing line (operational KPI) |
| 3 | 61 | ₹62.5 crore | Q1FY27 PAT (sub-headline) | verified vs results filing (line 458, 625.05mn) |
| 4 | 61 | 14.3% | PAT YoY (sub-headline) | verified (internally consistent with verified base figures) |
| 5 | 74 | 555.4 | Revenue Q1FY27 (table) | verified |
| 6 | 74 | 367.1 | Revenue Q1FY26 (table) | verified vs results filing (line 438, 3,670.79mn) |
| 7 | 74 | 51.3% | Revenue YoY (table) | verified |
| 8 | 74 | 2,641.3 | Revenue FY2026 (table) | verified vs results filing (line 438, 26,412.70mn) |
| 9 | 74 | 2,438.8 | Revenue FY2025 (table) | CROSS_CHECK — FY2025 not in results-filing comparative columns |
| 10 | 74 | 8.3% | Revenue YoY FY26 vs FY25 (table) | CROSS_CHECK — FY25 baseline unverifiable |
| 11 | 75 | 86.1 | EBITDA Q1FY27 (table) | CROSS_CHECK — no EBITDA line item (re-derivable: PBT 816.29 + Dep 44.37 + Fin.cost 283.41 - Other income 283.41 = 860.66mn ≈ 86.1cr, matches) |
| 12 | 75 | 80.1 | EBITDA Q1FY26 (table) | CROSS_CHECK — no EBITDA line item |
| 13 | 75 | 7.5% | EBITDA YoY (table) | CROSS_CHECK |
| 14 | 75 | 455.2 | EBITDA FY2026 (table) | CROSS_CHECK |
| 15 | 75 | 481.7 | EBITDA FY2025 (table) | CROSS_CHECK — also FY25 not in filing |
| 16 | 75 | (5.5)% | EBITDA YoY FY26 vs FY25 (table) | CROSS_CHECK |
| 17 | 76 | 15.5% | EBITDA Margin Q1FY27 (table) | CROSS_CHECK — margin ratio not a filing line item |
| 18 | 76 | 21.8% | EBITDA Margin Q1FY26 (table) | CROSS_CHECK |
| 19 | 76 | 17.2% | EBITDA Margin FY2026 (table) | CROSS_CHECK |
| 20 | 76 | 19.8% | EBITDA Margin FY2025 (table) | CROSS_CHECK |
| 21 | 77 | 62.5 | PAT Q1FY27 (table) | verified |
| 22 | 77 | 54.7 | PAT Q1FY26 (table) | verified vs results filing (line 458, 546.98mn) |
| 23 | 77 | 14.3% | PAT YoY (table) | verified |
| 24 | 77 | 307.3 | PAT FY2026 (table) | verified vs results filing (line 458, 3,072.64mn) |
| 25 | 77 | 279.1 | PAT FY2025 (table) | CROSS_CHECK — FY25 not in results-filing comparative columns |
| 26 | 77 | 10.1% | PAT YoY FY26 vs FY25 (table) | CROSS_CHECK — FY25 baseline unverifiable |
| 27 | 78 | 11.3% | PAT Margin Q1FY27 (table) | CROSS_CHECK — margin ratio not a filing line item |
| 28 | 78 | 14.9% | PAT Margin Q1FY26 (table) | CROSS_CHECK |
| 29 | 78 | 11.6% | PAT Margin FY2026 (table) | CROSS_CHECK |
| 30 | 78 | 11.4% | PAT Margin FY2025 (table) | CROSS_CHECK |
| 31 | 82 | 90 | BESS containers delivered during the quarter | CROSS_CHECK — operational KPI, no filing line |
| 32 | 83 | ₹8,453 crore | Executable Energy order book, as of Aug 05, 2026 | CROSS_CHECK |
| 33 | 84 | 5 GWh | Overall BESS order visibility | CROSS_CHECK |
| 34 | 85-86 | 2.5 GWh | Additional BESS manufacturing platform, installed capacity (subsequent event) | CROSS_CHECK |
| 35 | 86 | 5 GWh | Total BESS manufacturing capacity post subsequent event | CROSS_CHECK |
| 36 | 99 | ₹2,350.3 crore | Executable Telecom & ICT order book, as of Aug 05, 2026 | CROSS_CHECK |
| 37 | 106 | ₹264 crore | BSNL Advance Work Order contract value (Sikkim Telecom Circle) | CROSS_CHECK |
| 38 | 114 | 2.5 GWh | Additional BESS manufacturing line commissioned, subsequent to quarter | CROSS_CHECK |
| 39 | 115 | 5 GWh | Total installed BESS manufacturing capacity (post subsequent event) | CROSS_CHECK |
| 40 | 118 | 5 GWh | Current phase base of capacity expansion plan | CROSS_CHECK |
| 41 | 118 | 10 GWh | Target phase of capacity expansion plan | CROSS_CHECK |
| 42 | 140 | ₹555.4 crore | Revenue (bullet, Key Highlights) | verified — duplicate of #5 |
| 43 | 140 | 51.3% | Revenue YoY (bullet) | verified — duplicate of #7 |
| 44 | 141 | ₹86.1 crore | EBITDA (bullet) | CROSS_CHECK — duplicate of #11 |
| 45 | 141 | 7.5% | EBITDA YoY (bullet) | CROSS_CHECK — duplicate of #13 |
| 46 | 141 | 15.5% | EBITDA margin (bullet) | CROSS_CHECK — duplicate of #17 |
| 47 | 142 | ₹62.5 crore | PAT (bullet) | verified — duplicate of #21 |
| 48 | 142 | 14.3% | PAT YoY (bullet) | verified — duplicate of #23 |
| 49 | 143 | 11.3% | PAT margin (bullet) | CROSS_CHECK — duplicate of #27 |
| 50 | 147 | ₹555.4 crore | Revenue (CMD quote) | verified — duplicate of #5 |
| 51 | 148 | 51.3% | Revenue YoY (CMD quote) | verified — duplicate of #7 |
| 52 | 151 | ₹10,803.3 crore | Order book (CMD quote) | CROSS_CHECK — duplicate of #2 |
| 53 | 154 | 2.5 GWh | BESS manufacturing facility operationalized during the quarter (CMD quote) | CROSS_CHECK |
| 54 | 157 | 2.5 GWh | Additional BESS manufacturing line, subsequent to quarter (CMD quote) | CROSS_CHECK — duplicate of #38 |
| 55 | 158 | 5 GWh | Total installed capacity (CMD quote) | CROSS_CHECK — duplicate of #39 |
| 56 | 158-159 | 10 GWh | Target capacity, "remain on track to expand it to 10 GWh" (CMD quote) — figure split by a mid-sentence PDF line wrap ("...10" on line 158, "GWh." on line 159) | CROSS_CHECK — duplicate of #41; catches the line-wrap-split figure re-swept for GATE A2 |

EBITDA Margin row (line 76) and the Y-o-Y column: no numeric value is printed for
the margin-delta Y-o-Y cell in either half of the table (blank, not a dash or
zero character) — this is a blank/omitted derived-ratio cell, not treated as a
`ZERO_STANDING` line item since it is not a standing balance-sheet/note line.

No `ZERO_STANDING` items identified — this doctype carries no formal financial-
statement notes or line items disclosed at nil/dash across all periods (that
enumeration belongs to the `results` doctype ledger, not this one).

---

## 3. FORWARD-LOOKING / COMMITMENT STATEMENTS (7) — all flagged `FORWARD_SIGNAL`

| # | Line(s) | Statement | Type |
|---|---------|-----------|------|
| 1 | 84-86 | "Subsequent to the quarter, the Company has also operationalized its additional BESS manufacturing platform with an installed capacity of 2.5 GWh, bringing its total BESS manufacturing capacity to 5 GWh." | Subsequent-to-quarter capacity event |
| 2 | 91-92 | "Pace Digitek also progressed the development of Commercial & Industrial (C&I) energy storage prototype solutions, which are currently under evaluation for commercial deployment." | Pipeline / future-commercialization statement |
| 3 | 113-115 | "Subsequent to the quarter, the Company commissioned an additional 2.5 GWh BESS manufacturing line, increasing its total installed BESS manufacturing capacity to 5 GWh, enhancing its ability to meet growing customer demand." | Subsequent-to-quarter capacity event |
| 4 | 117-119 | "The Company also continued investing in the phased expansion of its BESS manufacturing capacity from 5 GWh to 10 GWh and remains on track to commission its in-house container fabrication facility..." | Capacity ramp target + "remains on track" commitment |
| 5 | 129-135 | "Following the quarter-end, Pace Digitek further strengthened its long-term growth platform through key strategic initiatives." [MEGMEET Electrical India strategic cooperation agreement — AI data center power infrastructure; Pace-Lineage Research Center established in Pune] | Subsequent-to-quarter strategic events |
| 6 | 157-158 | "Subsequent to the quarter, we commissioned an additional 2.5 GWh BESS manufacturing line, taking our total installed capacity to 5 GWh" | Subsequent-to-quarter capacity event (CMD quote) |
| 7 | 158-159 | "...and remain on track to expand it to 10 GWh." | Capacity ramp target + "remain on track" commitment (CMD quote) |

Note: the same "5 GWh → 10 GWh, on/remain on track" commitment appears twice
(#4 in body copy, #7 in the CMD quote) — same underlying commitment, two
disclosure surfaces; both rows kept since each carries a distinct line number
and speaker context (unattributed body copy vs. CMD's own words).

---

## 4. MANAGEMENT COMMENTARY QUOTE (1)

| # | Line(s) | Speaker | Designation | Content summary |
|---|---------|---------|-------------|------------------|
| 1 | 146-161 | Mr. Maddisetty Venugopal Rao | Chairman & Managing Director, Pace Digitek Ltd | 3-paragraph quote: (i) 146-148 revenue growth 51.3% YoY driven by Telecom & ICT and Energy execution; (ii) 151-152 order book ₹10,803.3 crore, revenue visibility; (iii) 154-161 BESS facility operationalization, EPC/execution capability, NEC XON OEM partnership, subsequent BESS line commissioning to 5 GWh, "remain on track" to 10 GWh, closing on disciplined execution/stakeholder value |

---

## 5. SAFE HARBOUR DISCLAIMER (1)

| # | Line(s) | Content |
|---|---------|---------|
| 1 | 184-189 | "Safe Harbour:" header (184) + disclaimer paragraph (185-189): forward-looking statements re plans/objectives, R&D progress and results, potential project characteristics, project potential and target dates are based on estimates and anticipated effects of future events; subject to numerous risks and uncertainties; actual results may differ materially; no obligation to update forward-looking statements assumed |

---

## FLAG SUMMARY

- `CROSS_CHECK`: 39 of 56 numbers (rows #2, #9-#20, #25-#30, #31-#41, #44-#46, #49, #52-#56 in Table 2) — EBITDA family, all margin percentages, FY2025 comparatives, and all order-book/GWh/contract-value operational figures have no matching line item in `extract_results_pacedigitk_q1fy27.txt`. Revenue and PAT for Q1FY27/Q1FY26/FY2026 are independently verified against the results filing (unit-converted) and carry no flag.
- `FORWARD_SIGNAL`: 7 statements (Table 3), all subsequent-to-quarter events or explicit "on track" / "remains on track" capacity-ramp commitments.
- `ZERO_STANDING`: none applicable to this doctype.
- `ENTITY_CHANGE`, `MGMT_ABSENCE`, `REPEAT_QUESTION`, `DROPPED_SLIDE`: not applicable (no consolidation list, no Q&A, no prior-quarter deck in scope of this ledger).
