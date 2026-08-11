# A2 ENUMERATION LEDGER — Credo Brands Marketing Ltd (CREDO) — Q1 FY27 — media-release (presentation doctype)

Source: `extract_mediarelease_credo_q1fy27.txt` (4 pages, 219 lines, unit convention: Crores x1, "in Rs. Crore" per source header). Prior-quarter ledger: none (first coverage) — no DROPPED_SLIDE / ENTITY_CHANGE diff possible this run.

```
=== A2 COUNT TEST ===
category: pages_sections              grep_count: 4    sweep_count: 4    match: yes
category: financial_table_line_items  grep_count: 6    sweep_count: 6    match: yes
category: operational_highlight_nums  grep_count: 15   sweep_count: 15   match: yes
category: management_quote_block      grep_count: 1    sweep_count: 1    match: yes
category: quote_numeric_claims        grep_count: 11   sweep_count: 11   match: yes
category: quote_forward_looking_para  grep_count: 4    sweep_count: 4    match: yes
category: narrative_bullets           grep_count: 10   sweep_count: 10   match: yes
category: digital_campaign_tiles      grep_count: 3    sweep_count: 3    match: yes
category: footnotes_fineprint         grep_count: 5    sweep_count: 5    match: yes
category: administrative_identifiers  grep_count: 19   sweep_count: 19   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used per category are given under each table below so the counts are reproducible.

---

## 1. Pages / Sections (per-page enumeration)

`grep -n "^\[page"` → 4 matches (lines 14, 54, 106, 161). Manual sweep confirms 4 pages, content typed below.

| # | Line | Page | Content type | Section headers present |
|---|------|------|--------------|--------------------------|
| 1 | 14 | Page 1 | text (covering letter) | Addressed to BSE/NSE, Scrip Code/Symbol, subject line, digital signature block |
| 2 | 54 | Page 2 | text + table | "KEY FINANCIAL HIGHLIGHTS" (P&L table), "KEY OPERATIONAL HIGHLIGHTS" (bullets), "KEY BUSINESS UPDATE" (2 numbered themes with checkmark sub-bullets) |
| 3 | 106 | Page 3 | photo tiles + text (mgmt quote) | "Recent Digital Campaigns" (3 tiles), management quote block (Kamal Khushlani, Chairman & MD) |
| 4 | 161 | Page 4 | text | "About Credo Brands Marketing Limited" (descriptive, no numbers), contact directory, "Safe Harbor" disclaimer |

No prior-quarter presentation ledger supplied → `DROPPED_SLIDE` check not applicable (flag N/A, first coverage).

---

## 2. Key Financial Highlights — Table Line Items

Grep: `grep -nE "^\s{2}(Total Revenue|Gross Profit|Gross Margin|EBITDA|EBITDA Margin|PAT)\s"` → 6 matches (lines 69–74). Manual sweep of table body (lines 68–74) confirms 6 line items, 0 rows zero/nil/dash in either period (no `ZERO_STANDING`).

| # | Line | Line item | Q1 FY27 | Q1 FY26 | YoY | Flags |
|---|------|-----------|---------|---------|-----|-------|
| 1 | 69 | Total Revenue | 125.3 | 119.9 | 5% | |
| 2 | 70 | Gross Profit | 77.2 | 73.8 | 5% | |
| 3 | 71 | Gross Margin | 61.6% | 61.6% | 10 bps | |
| 4 | 72 | EBITDA | 26.6 | 31.0 | (14%) | YOY_DECLINE |
| 5 | 73 | EBITDA Margin | 21.2% | 25.9% | (460 bps) | YOY_DECLINE |
| 6 | 74 | PAT | 2.3 | 6.3 | (63%) | YOY_DECLINE |

Note: header row itself (line 68, "Profit & Loss (in Rs. Crore) / Q1 FY27 / Q1 FY26 / YoY") is the table header, not a line item — excluded from the 6-count by design; both grep and sweep exclude it consistently.

---

## 3. Key Operational Highlights — Every Numeric Claim

Grep (percent tokens): `sed -n '76,83p' <file> | grep -oE '\(?-?[0-9]+(\.[0-9]+)?%\)?'` → 13. Grep (non-percent): `grep -oE '[0-9]+ (stores|days)'` → 2 (427 stores, 176 days). Total grep = 15. Manual sweep of lines 76–83 = 15.

| # | Line | Metric | Value | Flags |
|---|------|--------|-------|-------|
| 1 | 76 | Total EBOs as on 30 Jun 2026 | 427 stores | |
| 2 | 78 | Sales Mix — EBO | 61% | |
| 3 | 78 | Sales Mix — MBO | 17% | |
| 4 | 78 | Sales Mix — LFS | 5% | |
| 5 | 78 | Sales Mix — Online | 12% | |
| 6 | 78 | Sales Mix — Others | 5% | |
| 7 | 80 | Product Mix — Shirts | 47% | |
| 8 | 80 | Product Mix — T-shirts | 11% | |
| 9 | 80 | Product Mix — Bottomwear | 39% | |
| 10 | 80 | Product Mix — Outerwear | (1%) | NEGATIVE_VALUE |
| 11 | 80 | Product Mix — Others | 4% | |
| 12 | 81 | Working Capital Days (as on 30 Jun 2026) | 176 days | FOOTNOTE_QUALIFIED (TTM*, line 103) |
| 13 | 82 | RoCE (Q1 FY27) | 12.9% | FOOTNOTE_QUALIFIED (TTM*, line 103) |
| 14 | 82 | RoE (Q1 FY27) | 10.1% | FOOTNOTE_QUALIFIED (TTM*, line 103) |
| 15 | 83 | Marketing & Ad spend | 8.5% of revenue | |

Sales-mix row check: 61+17+5+12+5 = 100%. Product-mix row check: 47+11+39−1+4 = 100% (Outerwear stated as negative contribution). Both reconcile — recorded for A3/A4, not interpreted further here.

---

## 4. Management Quote — Block

Grep: `grep -ncE "Chairman & MD.*said|Commenting on the Result"` → 1 (line 122). Manual sweep of the document confirms exactly one attributed management quote (no other quoted speaker anywhere in the release).

| # | Line (start–end) | Speaker | Designation | Content |
|---|-------------------|---------|-------------|---------|
| 1 | 122–153 | Mr. Kamal Khushlani | Chairman & MD, Credo Brands Marketing Limited | Full quote spanning 6 paragraphs: (a) transformation-journey framing, lines 123–126; (b) revenue/gross-profit/margin, lines 128–129; (c) EBITDA/marketing spend/guidance/PAT, lines 131–137; (d) store network additions/closures, lines 139–142; (e) long-term transformation ambition, lines 144–148; (f) outlook, lines 150–153 |

---

## 5. Management Quote — Every Numeric Claim

Grep (₹ figures): `sed -n '122,153p' | grep -oE '₹[0-9]+(\.[0-9]+)?'` → 5. Grep (percent, incl. ranges): `grep -oE '[0-9]+(-[0-9]+)?%'` → 4. Grep (store-count phrases): `grep -oE '[0-9]+ (new stores|underperforming)'` → 2. Total grep = 11. Manual sweep = 11.

| # | Line | Claim | Value | Flags |
|---|------|-------|-------|-------|
| 1 | 128 | Q1 FY27 revenue | ₹125 crore | |
| 2 | 129 | Gross profit growth YoY | 5% | |
| 3 | 129 | Gross profit | ₹77 crore | |
| 4 | 129 | Gross margin | 62% | |
| 5 | 131 | EBITDA, Q1 FY27 | ₹27 crore | |
| 6 | 131 | EBITDA, Q1 FY26 (comparator) | ₹31 crore | |
| 7 | 132 | Marketing investment, % of revenue | 8.5% | |
| 8 | 133 | Full-year marketing spend guidance, FY27 | 8-10% | FORWARD_LOOKING |
| 9 | 137 | Profit After Tax, Q1 FY27 | ₹2.3 crore | |
| 10 | 139 | New stores opened | 5 stores | |
| 11 | 140 | Underperforming stores closed | 7 stores | |

Cross-check against Section 2 table: quote's ₹125cr / ₹77cr / 62% / ₹27cr / ₹2.3cr vs table's 125.3 / 77.2 / 61.6% / 26.6 / 2.3 — quote rounds to whole/near numbers where the table carries one decimal; EBITDA in the quote (₹27 crore) rounds up from the table's 26.6, and gross margin in the quote (62%) rounds up from the table's 61.6% — both are consistent rounding, flagged here only as a reconciliation note for A3/A4, not interpreted.

---

## 6. Management Quote — Forward-Looking / Commitment Phrases (paragraph-level)

Grep: keyword sweep `grep -niE "guidance|we see this as|continuing to build|we aim to|remains firmly on track|will continue|ambition remains|looking ahead|we believe|positions us well"` over lines 122–153 → hits at lines 133, 136, 141, 144, 146, 150, 152, grouping into 4 paragraph blocks (bounded by the blank lines at 130/138/143/149). Manual sweep = 4.

| # | Line (start–end) | Phrase (first ~15 words) | Flag |
|---|-------------------|---------------------------|------|
| 1 | 131–137 | "...in line with our full-year guidance of 8-10% through FY27. We see this as an important investment..." | FORWARD_LOOKING |
| 2 | 139–142 | "...we aim to improve output per store while enhancing the overall consumer experience and brand salience." | FORWARD_LOOKING |
| 3 | 144–148 | "Our long-term MUFTI 2.0 transformation remains firmly on track. We will continue to elevate our retail experience...Our ambition remains to build MUFTI into one of India's most loved..." | FORWARD_LOOKING |
| 4 | 150–153 | "Looking ahead, the global environment remains uncertain, with geopolitical tensions likely to keep consumers cautious...We believe MUFTI 2.0 positions us well to participate meaningfully..." | FORWARD_LOOKING, HEDGE (uncertain global environment / uneven demand visibility) |

Paragraphs 1 (123–126, transformation-journey framing) and 2 (128–129, revenue/GP/margin reporting) are retrospective/descriptive, not forward-commitment bearing — excluded from this table by design (they are captured in Sections 4–5).

---

## 7. Business Update — Narrative Bullets (page 2)

Grep: checkmark bullets `grep -n "✓"` → 8 (lines 87, 89, 90, 92, 95, 97, 98, 99). Numbered theme headers `grep -nE "^\s*[0-9]+\.\s"` → 2 (lines 86, 94). Total grep = 10. Manual sweep = 10.

| # | Line | Theme | Content (first 15 words) | Flag |
|---|------|-------|---------------------------|------|
| 1 | 86 | 1. MUFTI 2.0 TRANSFORMATION | "Reinventing the Store. Redefining the Brand Experience. Reigniting the Spark" | FORWARD_LOOKING |
| 2 | 87–88 | ✓ sub-bullet | "Continued progress on MUFTI's premiumisation journey through elevated stores, sharper merchandise, and stronger brand storytelling" | |
| 3 | 89 | ✓ sub-bullet | "Opened new-format premium stores in strategic locations with encouraging consumer response" | |
| 4 | 90–91 | ✓ sub-bullet | "Focused on improving retail productivity through selective store rationalisation and expansion into premium retail destinations" | FORWARD_LOOKING |
| 5 | 92–93 | ✓ sub-bullet | "Initiatives aimed at strengthening brand visibility, customer experience, and throughput per store over the medium to long term" | FORWARD_LOOKING |
| 6 | 94 | 2. STRENGTHENING DIGITAL & OMNICHANNEL CAPABILITIES | (header only) | |
| 7 | 95–96 | ✓ sub-bullet | "Continued investments in digital marketing through platforms such as Google and Meta to amplify MUFTI's evolving premium identity" | |
| 8 | 97 | ✓ sub-bullet | "Increased focus on content-led consumer engagement, digital storytelling, and performance marketing" | |
| 9 | 98 | ✓ sub-bullet | "Omnichannel strategy continues to connect online discovery with offline conversion and vice versa" | |
| 10 | 99–100 | ✓ sub-bullet | "Digital and brand-building investments aimed at strengthening long-term consumer engagement and sustainable future growth" | FORWARD_LOOKING |

No prior-quarter deck supplied, so no bullet present-last-quarter-but-absent-now check (`DROPPED_SLIDE`) is possible this run.

---

## 8. Recent Digital Campaigns — Tiles (page 3)

Grep: `grep -o "Click Here" <file> | wc -l` → 3 (all on line 117); campaign names co-located on line 116. Manual sweep = 3.

| # | Line | Campaign name | CTA |
|---|------|----------------|-----|
| 1 | 116 / 117 | PRATEIK X MUFTI | Click Here |
| 2 | 116 / 117 | FLOW LINEN | Click Here |
| 3 | 116 / 117 | HAVANA | Click Here |

No performance metrics, dates, or reach numbers disclosed for any campaign — pure name + link tiles.

---

## 9. Footnotes / Fine-Print Qualifiers on Headline Numbers

Grep: asterisk count `grep -o '\*' <file> | wc -l` → 4 (lines 81, 82×2, 103); plus `grep -n "Safe Harbor"` → 1 (line 207). Total grep = 5. Manual sweep = 5.

| # | Line | Qualifier | Qualifies | Flag |
|---|------|-----------|-----------|------|
| 1 | 81 | Asterisk marker on "Working Capital Days*" | Working Capital Days = 176 days (Section 3, row 12) | FOOTNOTE_QUALIFIED |
| 2 | 82 | Asterisk marker on "RoCE*" | RoCE = 12.9% (Section 3, row 13) | FOOTNOTE_QUALIFIED |
| 3 | 82 | Asterisk marker on "RoE*" | RoE = 10.1% (Section 3, row 14) | FOOTNOTE_QUALIFIED |
| 4 | 103 | Footnote definition: "*Trailing Twelve Months" | Defines the asterisk basis for rows 1–3 above | |
| 5 | 207–213 | "Safe Harbor" blanket disclaimer: forward-looking statements are estimates, subject to risks/uncertainties, not necessarily predictive, no obligation to update | Qualifies every forward-looking / guidance / ambition statement in Sections 5–7 (guidance 8-10%, all FORWARD_LOOKING-flagged rows) | HEDGE |

Note: EBITDA, EBITDA Margin and PAT YoY figures (Section 2, rows 4–6) carry no footnote qualifier despite the double-digit/steep declines — only Working Capital Days, RoCE and RoE (all TTM-basis operational metrics) are asterisked. Recorded as an observation for A3/A4, not interpreted here.

---

## 10. Administrative / Regulatory Identifiers & Contacts

Grep sub-totals: recipients `grep -oE "BSE Limited|National Stock Exchange of India Limited"` → 2 (line 19); scrip `grep -oE "Scrip Code|Scrip Symbol"` → 2 (line 24); CIN `grep -o "CIN:" | wc -l` → 2 (line 199); names `grep -oE "Mr\.|Ms\."` → 4 total in doc, minus 1 for Kamal Khushlani (line 122, already in Section 4) → 3 (line 201); emails `grep -oE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+"` → 3 (line 202); phones `grep -oE "\+91 [0-9]+ [0-9]+"` → 2 (line 203); websites `grep -oE "www\.[A-Za-z0-9.]+"` → 4 (lines 33, 204×3); signature block `grep -n "Digitally signed"` → 1 (line 41). Sum = 2+2+2+3+3+2+4+1 = 19. Manual sweep = 19.

| # | Line | Item | Value |
|---|------|------|-------|
| 1 | 19 | Regulatory addressee | BSE Limited |
| 2 | 19 | Regulatory addressee | National Stock Exchange of India Limited |
| 3 | 24 | Scrip Code | 544058 |
| 4 | 24 | Scrip Symbol | MUFTI |
| 5 | 41–48 | Digital signature block | Sanjay Kumar Mutha, Company Secretary and Compliance Officer, digitally signed 2026.08.11 18:22:36 +05'30' |
| 6 | 199 | Company CIN | L18101MH1999PLC119669 |
| 7 | 199 | IR firm (Strategic Growth Advisors Pvt. Ltd.) CIN | U74140MH2010PTC204285 |
| 8 | 201 | Company contact | Mr. Rasik Mittal, CFO |
| 9 | 201 | IR contact | Mr. Deven Dhruva |
| 10 | 201 | IR contact | Ms. Prachi Chhugani |
| 11 | 202 | Company email | investorrelations@mufti.in |
| 12 | 202 | IR email | deven.dhruva@sgapl.net |
| 13 | 202 | IR email | prachi.chhugani@sgapl.net |
| 14 | 203 | IR phone | +91 98333 73300 |
| 15 | 203 | IR phone | +91 89492 92029 |
| 16 | 204 | Company website | www.muftijeans.in |
| 17 | 204 | Company website | www.credobrands.in |
| 18 | 204 | IR website | www.sgapl.net |
| 19 | 33 | Company website (referenced in covering letter body) | www.credobrands.in |

No board-meeting timestamps are disclosed in this document (media release, not a board outcome letter) — signature timestamp (18:22:36 IST, 11 Aug 2026) cannot be checked against a meeting-conclusion time; recorded, no flag raised (data not available to test, not a positive finding).

---

## Summary Row Count

4 (pages) + 6 (financial table) + 15 (operational numbers) + 1 (quote block) + 11 (quote numbers) + 4 (quote forward-looking) + 10 (narrative bullets) + 3 (campaign tiles) + 5 (footnotes) + 19 (administrative) = **78 ledger rows**, all carrying a line number, zero silently dropped items (financial table has no zero/nil/dash line items this quarter — none to flag `ZERO_STANDING`).

```yaml
stage: A2-enumerator
company: "CREDO"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/credo-q1fy27/work/ledger_mediarelease_credo_q1fy27.md"
counts:
  notes: 5
  line_items: 6
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 11
  slides: 4
  slide_numbers: 44
flags_raised: [FORWARD_LOOKING, HEDGE, FOOTNOTE_QUALIFIED, YOY_DECLINE, NEGATIVE_VALUE]
gate_a2: pass
mismatch_note: ""
```
