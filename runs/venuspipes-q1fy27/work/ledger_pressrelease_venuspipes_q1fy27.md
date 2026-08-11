# A2 ENUMERATION LEDGER — Venus Pipes & Tubes (VENUSPIPES), Q1 FY27
Source: extract_pressrelease_venuspipes_q1fy27.txt (4-page press release, doctype=presentation, adapted enumeration)
Prior-quarter ledger: none available — no DROPPED_SLIDE / prior-period diff possible; noted as gap, not a mismatch.

```
=== A2 COUNT TEST ===
category: pages                          grep_count: 4    sweep_count: 4    match: yes
category: financial_table_numbers        grep_count: 21   sweep_count: 21   match: yes
category: highlight_numbers_outside_table grep_count: 8   sweep_count: 8    match: yes
category: mgmt_quote_claims              grep_count: 12   sweep_count: 12   match: yes  (raw naive sentence-split = 14; -2 for false splits at "Rs." abbreviation and the decimal point in "320.5"; adjusted grep = 12, ties to sweep)
category: operational_highlight_bullets  grep_count: 3    sweep_count: 3    match: yes  (grep on ✓ marker, lines 87/90/94)
category: about_and_self_description     grep_count: 11   sweep_count: 11   match: yes  (5 top-level sentences incl. page-2 self-description line 60-62; sentence 3 of About para decomposes into "two categories" claim + 5 named product categories = 6 rows; total 1+1+6+1+1+1(page2)=11)
category: footnotes_qualifiers           grep_count: 4    sweep_count: 4    match: yes
category: identifiers_procedural         grep_count: 13   sweep_count: 13   match: yes  (10 raw grep-matched lines; 3 lines carry multiple discrete items — line 19 addressees x2, line 26 identifiers x3, line 148 contacts x2 — item-level parse = 13, ties to sweep)
gate_a2: pass
=== END COUNT TEST ===
```

---

## TABLE A — PAGES (4)

| # | Line | Page | Heading/title | Content type | Summary |
|---|------|------|----------------|---------------|---------|
| A1 | 15 | 1 | (none — regulatory cover letter) | text | Intimation to BSE + NSE of attached Proposed Press Release; scrip/ISIN/symbol; digital signature block |
| A2 | 54 | 2 | "Venus Pipes & Tubes Limited" + headline "All time high revenue of INR 320.5 Crores" | text + table | Dateline, key financial highlights table, key operational highlights (3 bullets) |
| A3 | 97 | 3 | MD commentary + "About Venus Pipes & Tubes Ltd" | text | Arun Kothari (MD) quote (12 claims); company self-description paragraph |
| A4 | 143 | 4 | Contact information + Disclaimer | text | Company/IR contact details; forward-looking-statement disclaimer |

---

## TABLE B — FINANCIAL HIGHLIGHTS TABLE, EVERY NUMERIC CELL (21)

Header row (line 68): `Particulars (INR Cr) | Q1FY27 | Q1FY26 | YoY | Q4FY26 | YoY` — **flag `LABEL_INCONSISTENCY`**: the second "YoY" column header (comparing Q1FY27 to Q4FY26) is a sequential/QoQ comparison, not year-on-year; header mislabels it as "YoY" identically to the true YoY column. Carried forward for A3/A4.

| # | Line | Metric | Q1FY27 | Q1FY26 | YoY% | Q4FY26 | 2nd col (labeled YoY, actually QoQ) | Flags |
|---|------|--------|--------|--------|------|--------|--------------------------------------|-------|
| B1 | 70 | Revenue | 320.5 | — | — | — | — | |
| B2 | 70 | Revenue | — | 276.4 | — | — | — | |
| B3 | 70 | Revenue | — | — | 16.0% | — | — | |
| B4 | 70 | Revenue | — | — | — | 302.2 | — | |
| B5 | 70 | Revenue | — | — | — | — | 6.1% | LABEL_INCONSISTENCY (see header note) |
| B6 | 72 | EBITDA | 51.5 | — | — | — | — | |
| B7 | 72 | EBITDA | — | 44.9 | — | — | — | |
| B8 | 72 | EBITDA | — | — | 14.7% | — | — | |
| B9 | 72 | EBITDA | — | — | — | 49.4 | — | |
| B10 | 72 | EBITDA | — | — | — | — | 4.3% | LABEL_INCONSISTENCY |
| B11 | 74-76 | EBITDA Margin % | 16.1% | — | — | — | — | |
| B12 | 74-76 | EBITDA Margin % | — | 16.2% | — | — | — | |
| B13 | 74-76 | EBITDA Margin % | — | — | — | 16.3% | — | no YoY/QoQ bps delta shown for either comparator |
| B14 | 78 | PAT | 26.4 | — | — | — | — | |
| B15 | 78 | PAT | — | 24.8 | — | — | — | |
| B16 | 78 | PAT | — | — | 6.5% | — | — | |
| B17 | 78 | PAT | — | — | — | 25.4 | — | |
| B18 | 78 | PAT | — | — | — | — | 3.9% | LABEL_INCONSISTENCY |
| B19 | 80 | PAT Margin % | 8.2% | — | — | — | — | |
| B20 | 80 | PAT Margin % | — | 9.0% | — | — | — | |
| B21 | 80 | PAT Margin % | — | — | — | 8.4% | — | no bps delta shown |

No zero/nil/dash-valued standing line items appear in this table (see GAPS section — table is a 5-metric highlights extract, not a full financial statement, so `ZERO_STANDING` rule 3 does not apply; `zero_standing: 0`).

---

## TABLE C — FINANCIAL/OPERATIONAL NUMBERS OUTSIDE THE TABLE (8)

| # | Line | Location | Claim/number | Flags |
|---|------|----------|---------------|-------|
| C1 | 58 | Page 2 headline | "All time high revenue of INR 320.5 Crores" | RESTATEMENT of B1 (Revenue Q1FY27); cross-check target |
| C2 | 87-89 | Bullet 1 | Welded Pipes/Tubes revenue growth 21% YoY | NO_ABSOLUTE_VALUE — no Rs Cr figure for segment revenue, only % |
| C3 | 87-89 | Bullet 1 | Seamless Pipes/Tubes revenue growth 15% YoY | NO_ABSOLUTE_VALUE — same as C2 |
| C4 | 90-92 | Bullet 2 | Domestic growth 31% YoY | NO_ABSOLUTE_VALUE — no Rs Cr figure for domestic revenue |
| C5 | 90-92 | Bullet 2 | Exports "continued to remain around 30%" of revenue | APPROXIMATE — hedge word "around"; not a precise figure |
| C6 | 90-92 | Bullet 2 | Export revenue INR 94 Cr for the quarter | cross-check: 94/320.5 = 29.3%, consistent with "around 30%" in C5 |
| C7 | 102-103 | MD quote | "highest-ever quarterly revenue of Rs. 320.5 crores" | RESTATEMENT of B1/C1 |
| C8 | 102-103 | MD quote | "healthy growth of 16% year-on-year" | RESTATEMENT of B3 (16.0%), rounded to 16% in the quote |

No order-book number is disclosed anywhere in this press release (see GAPS).

---

## TABLE D — MANAGING DIRECTOR QUOTE, DISTINCT CLAIMS (12) — Arun Kothari, MD (attribution at line 99-100)

| # | Start line | Claim (paraphrase/first words) | Type | Flags |
|---|------------|----------------------------------|------|-------|
| D1 | 102 | "We have entered FY27 on a strong note, delivering our highest-ever quarterly revenue of Rs. 320.5 crores...16% year-on-year." | result claim + numeric restatement | RESTATEMENT (see C7/C8) |
| D2 | 104 | "This performance reflects sustained demand across our key domestic end markets, supported by our diversified presence...and strong customer relationships." | narrative/attribution claim | |
| D3 | 106 | "We continue to see healthy enquiry levels and remain well positioned to capitalize on emerging opportunities across our addressable markets." | forward-looking / soft guidance | hedge language ("well positioned") |
| D4 | 109 | "Our expansion into fittings and other value-added pipes and tubes has received an encouraging response from customers." | product-mix claim | qualitative, no number attached |
| D5 | 110 | "Over the medium term, we intend to steadily increase the contribution of these higher-value products to our overall revenue mix...differentiating Venus Pipes from its peers." | forward-commitment | no timeline or target % given |
| D6 | 113 | "In parallel, our forward integration into the spooling business is progressing as planned, with the capex execution on track." | forward-commitment | restates spooling project from bullet E3; no capex Rs figure given |
| D7 | 115 | "Looking ahead, demand continues to remain robust across both traditional industrial sectors and emerging applications." | forward-looking | |
| D8 | 116 | "New-age sectors such as data centers, clean energy and other segments are opening up new opportunities...strong visibility for the years ahead." | forward-looking, new-name-drop (data centers, clean energy) | first mention of these end-markets in this document |
| D9 | 120 | "On the export front, the geopolitical situation remains an area of watch." | hedge / risk phrase | |
| D10 | 120-121 | "In addition, freight rates continue to remain a factor that we are monitoring closely." | hedge / risk phrase | |
| D11 | 122 | "While these external factors may create near-term uncertainty, we remain focused on operational efficiency and maintaining close engagement with our customers." | hedge + commitment | |
| D12 | 124 | "Overall, we remain confident in the underlying demand environment and our ability to leverage...sustain our growth momentum and create long-term value for all stakeholders." | closing forward-looking claim | boilerplate-adjacent close |

---

## TABLE E — KEY OPERATIONAL HIGHLIGHTS, BULLET-LEVEL (3)

| # | Line | Bullet (first ~15 words) | Numbers embedded (cross-ref) | Flags |
|---|------|----------------------------|-------------------------------|-------|
| E1 | 87 | "Revenue from Welded Pipes / Tubes witnessed a growth of 21% and Seamless Pipes / Tubes witnessed growth of 15%..." | C2, C3 | |
| E2 | 90 | "Domestic growth stood robust at 31% with strong demand from end user industries, while exports continued to remain around 30%..." | C4, C5, C6 | |
| E3 | 94 | "Forward integration into Pipe spooling remains on track for commencement by December 2026" | none in Table C (timeline only) | forward-commitment date; cross-check target for next quarter's ledger |

---

## TABLE F — "ABOUT" SECTION + SELF-DESCRIPTION CLAIMS (11)

| # | Line | Claim | Flags |
|---|------|-------|-------|
| F0 | 60-62 | "one of the leading stainless-steel pipes / tubes manufacturers and exporters along with fittings in India" (page-2 dateline self-description) | unverified superlative ("leading") |
| F1 | 133-134 | "Venus Pipes & Tubes Limited is a manufacturer and exporter of stainless-steel pipes and tubes." | |
| F2 | 134-135 | "The company is into manufacturing of stainless steel tubes / pipes products along with fittings." | |
| F3 | 135-136 | "Company manufactures pipes / tubes in two broad categories — seamless tubes/pipes and welded tubes/pipes" | SOURCE_TYPO in extract: reads "in n two broad categories" (stray "n") |
| F4 | 136-137 | Product category 1 of 5: "stainless steel high precision & heat exchanger tubes" | part of "five categories of products" claim |
| F5 | 137 | Product category 2 of 5: "stainless steel hydraulic & instrumentation tubes" | |
| F6 | 138 | Product category 3 of 5: "stainless steel seamless pipes" | |
| F7 | 138 | Product category 4 of 5: "stainless steel welded pipes" | |
| F8 | 138-139 | Product category 5 of 5: "stainless-steel LSAW pipes" | |
| F9 | 139 | "The company sells products in both domestic and international markets." | |
| F10 | 140-141 | "Venus Pipes & Tubes exports its products to more than 30 countries including UK, US, Middle East and countries in the European Union, etc." | approximate ("more than"), no country-count breakdown |

---

## TABLE G — FOOTNOTES / QUALIFIERS / DISCLAIMERS (4)

| # | Line | Text | Flags |
|---|------|------|-------|
| G1 | 159-165 | Full DISCLAIMER paragraph: forward-looking statements subject to risks/uncertainties (economic environment, tax laws, inflation, litigation); company disclaims responsibility for action taken on such statements; no obligation to update | standard boilerplate; qualifies every forward-looking claim in Tables D/E |
| G2 | 28 | Subject line qualifier: "Unaudited Financial Results for the quarter ended June 30, 2026" | results are unaudited |
| G3 | 62-63 | Body qualifier: "announced its unaudited financial results for the first quarter ending June 30th, 2026" | restates G2 |
| G4 | 33-34 | "please find attached herewith a copy of the **Proposed** Press Release to be issued by the Company" | DRAFT_STATUS — cover letter describes the release as "Proposed," i.e. in-process at time of BSE/NSE filing |

---

## TABLE H — IDENTIFIERS / PROCEDURAL ITEMS (13)

| # | Line | Item | Flags |
|---|------|------|-------|
| H1 | 17 | Letter date: August 10, 2026 | |
| H2 | 19-24 | Addressee 1: Department of Corporate Services, BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai 400001 | |
| H3 | 19-24 | Addressee 2: Listing Department, National Stock Exchange of India Ltd, Exchange Plaza, Plot No. C/1, G Block, Bandra Kurla Complex, Bandra (East), Mumbai 400051 | |
| H4 | 26 | Scrip Code: 543528 | |
| H5 | 26 | ISIN: INE0JA001018 | |
| H6 | 26 | Symbol: VENUSPIPES | |
| H7 | 43-47 | Digital signature block: Pavan Kumar Jain, digitally signed, timestamp 2026.08.10 14:02:00 +05'30' | timestamp same calendar date as letter (H1); no board-meeting time in this doc to cross-check against (this is a press release, not a Board Outcome letter) — comparison N/A |
| H8 | 50-52 | CS Pavan Kumar Jain, Company Secretary and Compliance Officer, Membership No. A66752 | |
| H9 | 60 | Dateline: "Dhaneti, Gujarat: 10th August, 2026" | consistent with H1 |
| H10 | 99-100 | Attribution: Arun Kothari, Managing Director, Venus Pipes & Tubes Ltd | source of Table D quote |
| H11 | 132 | About-section restated identifiers: website (venuspipes.com), BSE: 543528, NSE: VENUSPIPES | consistent with H4/H6 |
| H12 | 148-150 | Company contact: Venus Pipes & Tubes Ltd., e-mail cs@venuspipes.com | |
| H13 | 148-154 | IR contact: Strategic Growth Advisors — Mr. Sagar Shroff / Mr. Ayush Haria, phones +91 98205 19303 / +91 98204 62966, e-mails sagar.shroff@sgapl.net / ayush.haria@sgapl.net | |

---

## GAPS / ABSENCE OBSERVATIONS (not line-numbered ledger rows — nothing to grep, flagged for A3/A4 attention)

1. **MISSING_BASIS** — the financial highlights table (lines 66-80) never states whether Revenue/EBITDA/PAT are Standalone or Consolidated. Table header only says "Particulars (INR Cr)" (line 68). No such label appears anywhere in the 4-page release.
2. **NOT_DISCLOSED (order book)** — no order-book / order-backlog figure appears anywhere in the release, despite this being a standard highlight for this sector.
3. **NOT_DISCLOSED (capex quantum)** — spooling forward-integration capex is referenced qualitatively twice (E3 "on track," D6 "capex execution on track") but no Rs Cr capex figure or capacity-addition number is ever given.
4. **LIMITED_SCOPE_DOCUMENT** — this is a 4-page highlights press release, not full financial statements: no balance sheet, cash flow, debt, capacity-utilization, or segment-wise absolute revenue (Cr) figures are present at all. Confirmed by page-by-page sweep (Tables A-H above cover 100% of the document's 151 content lines).
5. **No prior-quarter ledger available** (prior_ledger_path = none) — `DROPPED_SLIDE` / entity-list / prior-period diff checks could not be run this cycle.

---

## SUMMARY COUNT

| Category | Count |
|---|---|
| Pages (A) | 4 |
| Financial table numbers (B) | 21 |
| Highlight numbers outside table (C) | 8 |
| MD quote claims (D) | 12 |
| Operational highlight bullets (E) | 3 |
| About/self-description claims (F) | 11 |
| Footnotes/qualifiers (G) | 4 |
| Identifiers/procedural (H) | 13 |
| **Total disclosure units enumerated** | **76** |
| Zero-standing items | 0 (N/A — no full financial statement in this doctype) |

```yaml
stage: A2-enumerator
company: "VENUSPIPES"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/venuspipes-q1fy27/work/ledger_pressrelease_venuspipes_q1fy27.md"
counts:
  notes: 4
  line_items: 21
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 8
  slides: 4
  slide_numbers: 76
flags_raised: [LABEL_INCONSISTENCY, NO_ABSOLUTE_VALUE, APPROXIMATE, RESTATEMENT, DRAFT_STATUS, SOURCE_TYPO, MISSING_BASIS, NOT_DISCLOSED]
gate_a2: pass
mismatch_note: ""
```
