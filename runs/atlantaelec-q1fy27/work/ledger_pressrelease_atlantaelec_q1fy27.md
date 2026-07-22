# A2 ENUMERATOR LEDGER — Atlanta Electricals Ltd, Q1FY27, doctype: presentation (Reg 30 press release / earnings release)

Source: `runs/atlantaelec-q1fy27/work/extract_pressrelease_atlantaelec_q1fy27.txt` (156 lines, 3 pages, 100% page coverage, no OCR pages flagged in header but garbled text observed on p.1 footer — see flags).

NOTE ON DOCTYPE MISMATCH: injected doctype label is "presentation" but the actual document is a 3-page Reg 30 cover letter + press release (Results Filing style content: transmittal letter, financial highlights table, narrative bullets, management quote, About boilerplate). There are no slides, no concall turns, no auditor report, no board agenda beyond the single transmittal. Enumeration below is organized by the document's actual structure and cross-mapped to the closest RESULTS FILING categories in the instructions (agenda item = the single transmittal action; line items = financial table cells; notes = the EBITDA footnote). Flag: `DOCTYPE_LABEL_MISMATCH`.

---

## TABLE 1 — Cover Letter / Reg 30 Transmittal (lines 16-35)

| # | Line(s) | Item | Content (first ~15 words / value) | Flags |
|---|---|---|---|---|
| 1.1 | 16 | Letterhead identifier | "Q2 ATLANTA" — garbled logo/header text | OCR_GARBLED |
| 1.2 | 17 | Letter date | "21st July, 2026" (renders as "21% July, 2026" in extract) | OCR_ARTIFACT |
| 1.3 | 18-24 | Addressee 1 | Listing Department, BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai 400001; Scrip Code: 544527 | — |
| 1.4 | 19-24 | Addressee 2 | Listing Department, National Stock Exchange of India Limited, Exchange Plaza C-1 Block G, BKC, Bandra (E), Mumbai 400051; Symbol: ATLANTAELE | — |
| 1.5 | 26 | Subject line | "Sub.: Press Release" | — |
| 1.6 | 27-28 | Reference | "Ref.: Regulation 30 of SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015" | — |
| 1.7 | 30 | Salutation | "Dear Sir/ Ma'am," | — |
| 1.8 | 32-33 | Body / sole agenda item | Enclosing press release of unaudited financial results for quarter ended 30th June 2026 | AGENDA_ITEM (only one — no AR approval, AGM, dividend, director appointment, auditor change, ESOP, or capital-raising resolution present; this is a simple Reg 30 transmittal, not a Board Outcome letter) |
| 1.9 | 35 | Closing statement | "This is for your information and record." | — |

Sub-total: 9 items. No board meeting start/end times disclosed (not a Board Outcome letter — flag `NO_MEETING_TIMES`).

---

## TABLE 2 — Key Consolidated Financial Highlights Table (lines 71-78)

Columns: Q1FY27 | Q1FY26 | YoY% | **Q4FY25** (label flag below). 5 rows x 4 periods = 20 cells, plus 1 footnote.

| # | Line | Row | Q1FY27 | Q1FY26 | YoY% | Q4FY25 | Flags |
|---|---|---|---|---|---|---|---|
| 2.1 | 73 | Revenue from Operations | 466.33 | 315.11 | 48.0% | 747.62 | PERIOD_LABEL_ANOMALY (col 4) |
| 2.2 | 74 | EBITDA* | 77.10 | 48.78 | 58.1% | 149.56 | PERIOD_LABEL_ANOMALY (col 4) |
| 2.3 | 75 | EBITDA % | 16.5% | 15.5% | +105 Bps | 20.0% | PERIOD_LABEL_ANOMALY (col 4) |
| 2.4 | 76 | PAT | 46.84 | 31.14 | 50.4% | 102.19 | PERIOD_LABEL_ANOMALY (col 4) |
| 2.5 | 77 | PAT % | 10.0% | 9.9% | +16 Bps | 13.7% | PERIOD_LABEL_ANOMALY (col 4) |
| 2.6 | 78 | Footnote | "*EBITDA excluding other income" | — | — | — | applies to row 2.2 |

**PERIOD_LABEL_ANOMALY**: the fourth column is headed "Q4FY25" (Jan-Mar 2025), not "Q4FY26" (Jan-Mar 2026, the immediately preceding/sequential quarter one would expect beside Q1FY27). Either the label is wrong (data is actually Q4FY26 mislabeled) or the company is genuinely benchmarking against a quarter over a year stale with no true QoQ column shown. No QoQ% is computed for the table at all (QoQ growth is asserted only in narrative text for order book, not for revenue/EBITDA/PAT). This is a materially reviewable label problem — flag for A3/A4.

No zero, nil, or dash-valued cells found in this table across all 20 cells (verified by direct read of lines 73-77). `zero_standing = 0` for this doctype's sole financial table.

---

## TABLE 3 — Headline Banner Claims (lines 63-65, above the dateline)

| # | Line | Claim | Flags |
|---|---|---|---|
| 3.1 | 63 | "48% Revenue Growth" | rounds table's 48.0% (2.1) |
| 3.2 | 63 | "58% EBITDA Growth" | rounds table's 58.1% (2.2) |
| 3.3 | 63 | "50% PAT Growth" | rounds table's 50.4% (2.4) |
| 3.4 | 64 | "105 bps EBITDA Margin Expansion YoY" | matches 2.3 |
| 3.5 | 65 | "Strong Order Backlog of ₹3,117 Crores" | ROUNDING_VARIANCE — body text (5.1) and Mgmt Commentary (6.5) both state ₹3,116.63 crore; headline rounds to ₹3,117 crore (+0.37cr rounding, immaterial but noted) |

---

## TABLE 4 — Performance Overview bullets, decomposed (lines 84-94; 3 raw bullets, 10 sub-claims)

| # | Line(s) | Claim | Flags |
|---|---|---|---|
| 4.1 | 84 | Revenue ₹466.33 crore, 48.0% YoY growth | restates 2.1 |
| 4.2 | 84-86 | Qualitative growth drivers: domestic order execution, higher capacity utilization, T&D + renewable energy demand | QUALITATIVE, unquantified |
| 4.3 | 88 | EBITDA +58.1% YoY to ₹77.10 crore | restates 2.2 |
| 4.4 | 88 | EBITDA margin +105 bps YoY to 16.5% | restates 2.3 |
| 4.5 | 88-89 | PAT +50.4% YoY to ₹46.84 crore | restates 2.4 |
| 4.6 | 89 | Qualitative driver: "improved operating leverage, better execution and a favourable product mix" | QUALITATIVE, unquantified |
| 4.7 | 91-93 | RRVPNL order ₹291.68 crore | first mention |
| 4.8 | 92 | Unit breakdown: 4 units, 160 MVA, 220/132 kV | — |
| 4.9 | 92-93 | Unit breakdown: 63 units, 50 MVA, 132/33 kV | — |
| 4.10 | 93 | Unit breakdown: 12 units, 31.5 MVA, 132/33 kV | — |

Sub-check: 4.8+4.9+4.10 units = 4+63+12 = 79 total transformer units; MVA sum = 4x160 + 63x50 + 12x31.5 = 640+3,150+378 = 4,168 MVA against a ₹291.68cr order (not separately verified against total order value — arithmetic-consistency task for A5).

---

## TABLE 5 — Key Business Updates bullets, decomposed (lines 97-118; 5 raw bullets, 18 sub-claims)

| # | Line(s) | Claim | Flags |
|---|---|---|---|
| 5.1 | 97 | Order book ₹3,116.63 crore as of 30th June 2026 | — |
| 5.2 | 97 | QoQ growth 25.0% | — |
| 5.3 | 97-98 | Q1 FY27 order inflow ₹972.42 crore | — |
| 5.4 | 98-100 | Qualitative: "healthy customer enquiries," "structural demand across power infrastructure sector" | QUALITATIVE, unquantified |
| 5.5 | 101-103 | Qualitative: business mix evolving toward higher-capacity transformers, moving up value chain | QUALITATIVE, unquantified |
| 5.6 | 103 | ">55% of order book comprises 220 kV transformers" | — |
| 5.7 | 103-104 | "400 kV transformers and reactors contribute nearly ₹275 crore" | approximate ("nearly") |
| 5.8 | 105-108 | RRVPNL order ₹291.68 crore | REPEAT_DISCLOSURE, dup of 4.7 |
| 5.9 | 105-108 | Unit breakdown: 4 units, 160 MVA, 220/132 kV | REPEAT_DISCLOSURE, dup of 4.8 |
| 5.10 | 105-108 | Unit breakdown: 63 units, 50 MVA, 132/33 kV | REPEAT_DISCLOSURE, dup of 4.9 |
| 5.11 | 105-108 | Unit breakdown: 12 units, 31.5 MVA, 132/33 kV | REPEAT_DISCLOSURE, dup of 4.10 |
| 5.12 | 109-110 | PGCIL approval for manufacturing up to 400 kV class transformers at Vadod facility | — |
| 5.13 | 110-111 | 400 kV transformer development at Vadod — status "remains on track" | STATUS_CLAIM, no date/timeline given |
| 5.14 | 111 | 765 kV transformer at Atlanta Trafo — status "remains on track" | STATUS_CLAIM, no date/timeline given |
| 5.15 | 111-112 | Qualitative: supports opportunities in transmission infra, renewable energy, BESS, data centres, export markets | QUALITATIVE, unquantified |
| 5.16 | 115 | "Manufacturing operations continued to scale up following the successful commissioning of new capacities in FY26" | STATUS_CLAIM, no capacity figure given |
| 5.17 | 116 | Inverter Duty Transformer (IDT) facility — commissioning in progress | STATUS_CLAIM, no completion date |
| 5.18 | 116-117 | Tank & Radiator backward integration — "progressing" | STATUS_CLAIM, no completion date |

The full RRVPNL order (₹291.68cr / 4+63+12 unit breakdown) appears twice verbatim in the same 3-page release (Performance Overview bullet 3, lines 91-94, and Key Business Updates bullet 3, lines 105-108) — flag `REPEAT_DISCLOSURE` on 5.8-5.11.

---

## TABLE 6a — Management Commentary: restated financial figures (lines 120-132)

Speaker: Mr. Niral Patel, Chairman and Managing Director. Quote runs lines 123-140, three paragraphs (blank-line-delimited: 123-126, 128-132, 134-140).

| # | Line | Claim | Flags |
|---|---|---|---|
| 6.1 | 124 | Revenue +48.0% YoY to ₹466.33 crore | restates 2.1 / 4.1 |
| 6.2 | 124 | EBITDA +58.1% to ₹77.10 crore | restates 2.2 / 4.3 |
| 6.3 | 125 | EBITDA margin 16.5% | restates 2.3 / 4.4 |
| 6.4 | 125 | PAT +50.4% YoY to ₹46.84 crore | restates 2.4 / 4.5 |
| 6.5 | 128 | Order book +25.0% sequentially to ₹3,116.63 crore | restates 5.1/5.2 |
| 6.6 | 129-132 | Qualitative: business-mix transformation, EHV strategy, "enhance the quality of our earnings over the long term" | QUALITATIVE, unquantified |

## TABLE 6b — Management Commentary: forward-looking statements (lines 134-140, paragraph 3)

| # | Line | Forward-looking statement | Flags |
|---|---|---|---|
| 6.7 | 134 | "we remain confident in the long-term opportunities emerging from India's expanding power infrastructure" | FLS, no timeframe/target |
| 6.8 | 135-136 | Demand drivers cited as structural: transmission network expansion, renewable energy integration, BESS, industrial electrification, data centre development | FLS, no quantification |
| 6.9 | 136-137 | "focused on increasing capacity utilisation across our manufacturing facilities" | FLS, no target % given |
| 6.10 | 137 | "expanding our export footprint" | FLS, no target/geography given |
| 6.11 | 137 | "commissioning our Inverter Duty Transformer facility" | FLS, restates 5.17, no date |
| 6.12 | 137-138 | "progressing our backward integration initiatives" | FLS, restates 5.18, no date |
| 6.13 | 138-139 | "advancing our capabilities in the EHV and UHV transformer segments, including the development of 400 kV and 765 kV transformers" | FLS, restates 5.13/5.14, no date |
| 6.14 | 139-140 | "These strategic initiatives will further strengthen our manufacturing capabilities and position us well for sustained long-term growth" | FLS, closing statement, no target/metric |

8 forward-looking phrases in a single management quote, none carrying a specific date, percentage target, or capex figure — flag `FLS_UNQUANTIFIED` (all 8).

---

## TABLE 7 — About Atlanta Electricals Limited (lines 142-146)

| # | Line(s) | Claim | Flags |
|---|---|---|---|
| 7.1 | 143-144 | Product range: power transformers from 5 MVA/11 kV up to 500 MVA/765 kV | — |
| 7.2 | 143-144 | Qualitative product list: auto transformers, inverter duty transformers, furnace transformers, generator transformers, special duty transformers | QUALITATIVE |
| 7.3 | 144-145 | "five facilities in Gujarat and Karnataka" | no facility-by-facility breakdown given |
| 7.4 | 145 | "over 30 years of experience" | — |
| 7.5 | 145-146 | "as of 31st March 2026, the Company has supplied over 4,800 transformers" | STALE_DATE — cumulative figure dated to FY26 fiscal year-end (31 Mar 2026), not to the Q1FY27 quarter-end (30 Jun 2026) this release otherwise reports as of |
| 7.6 | 146 | "...totalling more than 1,16,000 MVA across the country" | STALE_DATE, same as 7.5 |

---

## TABLE 8 — Signature block / letterhead footer / contact details (lines 39-56, 150-156)

| # | Line(s) | Item | Flags |
|---|---|---|---|
| 8.1 | 39-42 | Valediction: "Thanking you, Yours faithfully, For Atlanta Electricals Limited" | — |
| 8.2 | 43-47 | Digital signature block: signatory "TEJALBEN SAUNAKKUMAR PANCHAL," signed 2026.07.21 13:12:07 +05'30' | timestamp is same-day as letter date (21 Jul 2026), consistent — no pre-meeting-conclusion anomaly detectable (this is a press-release transmittal, not a board-meeting-outcome letter, so no board conclusion time to check against) |
| 8.3 | 48-49 | Signatory name/designation: Tejal S. Panchal, Company Secretary & Compliance Officer | — |
| 8.4 | 54-56 | Letterhead footer (garbled OCR): "ATLANTA ELECTRICALS LIMITED," "ATLANTA ELECTRICALS PVT LTD" fragment, "CIN: 131110," www.aetrafo.com, phone 02692 235023, sales@aetrafo.com | OCR_GARBLED; CIN "131110" is not a valid CIN format (should be 21 alphanumeric chars, e.g. LNNNNNSSYYYYPLCNNNNNN) — flag `CIN_ANOMALY` (likely OCR truncation of the true CIN, not a genuine disclosure error, but must be verified against the source PDF, not silently corrected) |
| 8.5 | 150 | Header: "For Further Information, please contact:" | — |
| 8.6 | 152 | Company website: www.aetrafo.com | — |
| 8.7 | 152-153 | Media contact: Sayantani Banerjee, Adfactors PR, sayantani.banerjee@adfactorspr.com, +91 9830035203 | — |
| 8.8 | 154-156 | Investor contacts: Mohit Upadyay / Tejpal Singh, Adfactors PR, mohit.upadyay@adfactorspr.com / tejpal.singh@adfactorspr.com, +91 9324872783 / +91 9320006669 | — |

---

## NOT PRESENT IN THIS DOCUMENT (absence noted as data)

- No numbered notes section (grep for `^\s*[0-9]+\.\s` returns zero hits) — the only footnote is the single asterisk note at line 78.
- No Board Outcome agenda beyond the single press-release transmittal: no AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising enabling resolution. Flag `SINGLE_AGENDA_ITEM`.
- No auditor's report / limited review report attached or referenced in this extract (results are labelled "unaudited"; no auditor name, opinion type, or UDIN appears). Flag `NO_AUDITOR_REPORT_REFERENCED`.
- No entity/subsidiary consolidation list despite the results being labelled "consolidated financial results" — no subsidiary names, count, or relationship types disclosed anywhere in the release. Flag `NO_ENTITY_LIST`.
- No concall transcript content (no speaker turns, no Q&A) — this is a press release only.
- No slides (doctype label "presentation" does not match content — see note at top).
- No QoQ column for revenue/EBITDA/PAT/margins in the financial highlights table — QoQ is asserted only in narrative for order book (5.2) and order inflow context, never for the headline P&L lines.
- No standalone board meeting start/end time disclosed (not applicable to a simple Reg 30 press-release transmittal).

---

## === A2 COUNT TEST ===

Method note: grep patterns and independent manual line-by-line sweeps were run for every category below and cross-checked. Prose sections without a reliable single keyword (letter body, closing statement, letterhead logo) were verified via two independent manual passes over the same line ranges rather than grep, since no regex meaningfully isolates them from surrounding prose; this is noted per row.

```
=== A2 COUNT TEST ===
category: footnotes              grep_count: 1    sweep_count: 1    match: yes    (grep -n -E "^\*" ; row 2.6)
category: table_rows              grep_count: 5    sweep_count: 5    match: yes    (grep -n -E "^(Revenue from Operations|EBITDA\*|EBITDA %|PAT|PAT %)" ; rows 2.1-2.5)
category: table_cells             grep_count: 20   sweep_count: 20   match: yes    (per-row numeric-token grep, 4 tokens x 5 rows)
category: zero_standing_cells     grep_count: 0    sweep_count: 0    match: yes    (no zero/nil/dash cells found in the sole financial table)
category: headline_claims         grep_count: 5    sweep_count: 5    match: yes    (grep -oE numeric/%/bps/₹ tokens on lines 63-65 ; rows 3.1-3.5)
category: bullets_raw             grep_count: 8    sweep_count: 8    match: yes    (grep -c "•" ; 3 Performance Overview + 5 Key Business Updates)
category: bullets_decomposed      grep_count: n/a  sweep_count: 28   match: yes    (manual decomposition of the 8 raw bullets into discrete sub-claims, two independent passes both landing at 10 [Table 4] + 18 [Table 5] = 28)
category: mgmt_commentary_paras   grep_count: 3    sweep_count: 3    match: yes    (grep -n "^$" within lines 120-140 delimits 3 paragraph blocks: 123-126, 128-132, 134-140)
category: mgmt_restated_figures   grep_count: n/a  sweep_count: 6    match: yes    (two manual passes over para 1-2, lines 123-132; rows 6.1-6.6)
category: forward_looking_stmts   grep_count: n/a  sweep_count: 8    match: yes    (two manual passes over para 3, lines 134-140; rows 6.7-6.14)
category: about_section_claims    grep_count: 5    sweep_count: 5    match: yes    (custom grep -oE handling Indian comma-grouping on lines 142-146 ; rows 7.1,7.3,7.4,7.5,7.6; 7.2 excluded as qualitative)
category: cover_letter_items      grep_count: n/a  sweep_count: 9    match: yes    (two independent manual passes over lines 16-35 both landing at 9; structural-marker grep on Sub./Ref./Dear/BSE/NSE lines confirms 6 of the 9 boundaries directly, remaining 3 [logo, date, closing] have no keyword and were cross-read twice)
category: signature_footer_items  grep_count: n/a  sweep_count: 8    match: yes    (two independent manual passes over lines 39-56 and 150-156; structural-marker grep on TEJALBEN/CIN/www.aetrafo/For Further Information/Website/Media/Investors confirms 6 of 8 line anchors)
category: agenda_items            grep_count: n/a  sweep_count: 1    match: yes    (single transmittal action; confirmed by absence-sweep of AGM/dividend/director/auditor/ESOP/capital-raise keywords, zero hits for all)
gate_a2: pass
=== END COUNT TEST ===
```

Grand total ledger rows (Tables 1-8, all sub-claims, footnote, cells): 9 + 21 (20 cells + 1 footnote) + 5 + 10 + 18 + 6 + 8 + 6 + 8 = **91 discrete disclosure units** enumerated.

---

## FLAGS RAISED (summary)

- `DOCTYPE_LABEL_MISMATCH` — injected doctype "presentation" does not match actual content (Reg 30 letter + press release, no slides)
- `OCR_GARBLED` — letterhead line 16 ("Q2 ATLANTA"), footer lines 54-56
- `OCR_ARTIFACT` — line 17 date renders "21st" as "21%"
- `PERIOD_LABEL_ANOMALY` — financial highlights table's 4th column labelled "Q4FY25" instead of the expected sequential "Q4FY26"; no true QoQ comparison exists for revenue/EBITDA/PAT in the table (rows 2.1-2.5)
- `ROUNDING_VARIANCE` — headline order backlog ₹3,117cr (row 3.5) vs body/commentary ₹3,116.63cr (rows 5.1, 6.5)
- `REPEAT_DISCLOSURE` — RRVPNL ₹291.68cr order and full unit breakdown stated twice verbatim (rows 4.7-4.10 and 5.8-5.11)
- `QUALITATIVE` — unquantified narrative claims called out separately so they are not miscounted as numeric disclosures (rows 4.2, 4.6, 5.4, 5.5, 5.15, 6.6, 7.2)
- `STATUS_CLAIM` — forward-progress language ("on track," "progressing," "continues to scale up") with no date or completion metric (rows 5.13, 5.14, 5.16, 5.17, 5.18)
- `FLS_UNQUANTIFIED` — all 8 forward-looking statements in Management Commentary carry no date, target %, or capex figure (rows 6.7-6.14)
- `STALE_DATE` — About section cumulative supply figures (4,800+ transformers, 1,16,000+ MVA) dated "as of 31st March 2026" (FY26 year-end), not the Q1FY27 quarter-end of 30 June 2026 this release otherwise reports against (rows 7.5, 7.6)
- `CIN_ANOMALY` — footer CIN "131110" is not a valid CIN format; likely OCR truncation, needs source-PDF verification (row 8.4)
- `SINGLE_AGENDA_ITEM` — cover letter carries only the press-release transmittal; no other Board Outcome-style agenda items present
- `NO_AUDITOR_REPORT_REFERENCED` — results labelled unaudited; no auditor name/opinion/UDIN anywhere in extract
- `NO_ENTITY_LIST` — "consolidated" results with zero subsidiary/entity names disclosed
- `NO_MEETING_TIMES` — no board meeting start/end time (not applicable doctype)
