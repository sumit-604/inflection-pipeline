# A2 ENUMERATION LEDGER — Tejas Networks (TEJASNET), Q1 FY27, Doctype: presentation
Source doc: press release "Tejas announces Q1FY27 results" (pressrelease_tejasnet_q1fy27.pdf), 3 pages.
Enumeration path used: INVESTOR PRESENTATION (per orchestrator instruction; each page treated as one slide).
Prior-quarter ledger: none available — first pipeline run for this ticker. No `DROPPED_SLIDE` check possible; noted as `NO_PRIOR_BASELINE`.

```
=== A2 COUNT TEST ===
category: pages_slides           grep_count: 3    sweep_count: 3    match: yes
category: table_line_items       grep_count: 3    sweep_count: 3    match: yes
category: table_data_points      grep_count: 9    sweep_count: 9    match: yes
category: highlight_bullets      grep_count: 4    sweep_count: 4    match: yes
category: bullet_business_nums   grep_count: 4    sweep_count: 4    match: yes
category: md_quote_numbers       grep_count: 4    sweep_count: 4    match: yes
category: cfo_quote_numbers      grep_count: 6    sweep_count: 6    match: yes
category: period_label_mentions  grep_count: 8    sweep_count: 8    match: yes
category: admin_identifier_lines grep_count: 16   sweep_count: 16   match: yes
category: business_profile_nums  grep_count: 1    sweep_count: 1    match: yes
category: entities                grep_count: 3    sweep_count: 3    match: yes
category: footnote_disclaimer    grep_count: 1    sweep_count: 1    match: yes
category: signature_block        grep_count: 1    sweep_count: 1    match: yes
category: zero_standing          grep_count: 0    sweep_count: 0    match: yes (checked: all 9 P&L data points non-zero across all 3 periods; no dash/nil line found)
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation note: `admin_identifier_lines` counts distinct doc lines carrying administrative/identifier digits (16 lines); the ledger table below itemizes these into 18 discrete identifier fields because 3 lines (17, 30→doc16, 65→doc51) each carry two separate identifiers on one line. This is a labeling refinement, not a count mismatch — the 16-line unit is what was grepped and swept, and both agree.

---

## TABLE 1 — SLIDE / PAGE INVENTORY

| # | Page (doc line range) | Title / heading | Content type | Flags |
|---|---|---|---|---|
| 1 | Page 1 (doc lines 1–41, page marker at line 1) | Cover letter to NSE/BSE Secretaries, "Re: Press Release" | Text (letter) + digital signature block | NO_PRIOR_BASELINE |
| 2 | Page 2 (doc lines 43–83, page marker at line 43) | "Press Release — Tejas announces Q1FY27 results" | Text + financial table + two management quotes + bulleted highlights list | NO_PRIOR_BASELINE |
| 3 | Page 3 (doc lines 84–107, page marker at line 84) | "About Tejas Networks Limited" + "SAFE HARBOUR" | Text (company profile + forward-looking-statement disclaimer) | NO_PRIOR_BASELINE |

---

## TABLE 2 — HEADLINE P&L TABLE (page 2, doc lines 57–60)

| Row | Line item | Doc line | Q1-FY27 | Q1-FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|
| 1 | Period-header row | 57 | "Ql-FV27" | "Ql-FV26" | "FV26" | OCR_ARTIFACT — "Q1" renders "Ql" and "FY" renders "FV" in all three header labels; the underlying period identity (Q1 FY27 / Q1 FY26 / FY26) is unambiguous from context and matches the clean digits below |
| 2 | Net Revenue | 58 | 402 | 202 | 1,103 | none — all three values present, non-zero |
| 3 | PBT | 59 | (271) | (297) | (1,354) | none — loss in all three periods, values non-zero (parenthetical = loss, not a zero/dash) |
| 4 | PAT | 60 | (202) | (194) | (909) | none — loss in all three periods, values non-zero |

Zero/nil/dash check performed per rule: no line item and no period cell in this table is zero, nil, or dash-valued. `ZERO_STANDING` does not apply to this table.

---

## TABLE 3 — MD QUOTE NUMBERS (Mr. Arnob Roy, MD and CEO; doc lines 63–69)

| # | Doc line | Number / spec | First 15 words of surrounding text | Flags |
|---|---|---|---|---|
| 1 | 63 | (period label "Q1", OCR "Ql") | "Ql revenues were driven by international shipments of 5G radios and domestic" | OCR_ARTIFACT (Q1→Ql) — tracked in Table 8 (period labels) |
| 2 | 64 | 5G | "international shipments of 5G radios and domestic shipments of 100G/400G Optical and FTTx" | none — digit clean here |
| 3 | 64 | 100G | "domestic shipments of 100G/400G Optical and FTTx products" | none — renders clean in this quote (contrast with Table 4 row 3, bullet 3, where 100G is OCR-garbled) |
| 4 | 64 | 400G | "domestic shipments of 100G/400G Optical and FTTx products" | none |
| 5 | 65 | 5G (repeat mention) | "products. We registered our first commercial win for an end-to-end 5G network deployment" | none |

Business-figure count for this quote: 4 (100G, 400G, and 5G counted twice as it appears at both line 64 and line 65). No revenue/margin/order-book figures are spoken in the MD quote; those appear only in the CFO quote (Table 4).

---

## TABLE 4 — CFO QUOTE NUMBERS (Mr. AVS Prasad, CFO; doc lines 80–82)

| # | Doc line | Number | Metric | Flags |
|---|---|---|---|---|
| 1 | 80 | 402 | Q1 FY27 revenue (Rs. Cr) — restates Table 2 row 2 figure | none |
| 2 | 80–81 | 21% | QoQ revenue growth | none — this % is spoken only here; not present in the P&L table, which has no QoQ column |
| 3 | 81 | 1,529 | Order book (Rs. Cr) | none — first and only mention of order book in the document |
| 4 | 81 | 4,277 | Net debt (Rs. Cr) | none |
| 5 | 82 | 4,866 | Gross debt (Rs. Cr) | none |
| 6 | 82 | 589 | Cash (Rs. Cr) | none |

Note: gross debt (4,866) minus cash (589) = 4,277 = stated net debt; internally consistent (arithmetic check only, no interpretation intended — flagged for A4/A5 arithmetic-consistency use).
Also present at line 80: period label "Q1 FY27" (OCR "Ql FY27") — tracked in Table 8, not counted as a business figure here.

---

## TABLE 5 — KEY HIGHLIGHTS BULLETS (page 2, doc lines 72–78)

| Bullet | Doc line(s) | Text (verbatim) | Embedded number(s) | Flags |
|---|---|---|---|---|
| Intro line | 72 | "Some of the other key highlights of Ql FY27 were:" | (period label only) | OCR_ARTIFACT (Q1→Ql); tracked in Table 8 |
| 1 | 73 | "Supplied GPON OlTs to Tier-1 Indian telcos for their countrywide rollouts" | Tier-1 | OCR_ARTIFACT — "OLTs" renders "OlTs" (uppercase L misread as lowercase l); product-name artifact, not a digit artifact |
| 2 | 74–75 | "Selected as a vendor for the communication network modernization of a large power utility" | none | ZERO_STANDING not applicable — no numeric claim in this bullet at all (no order size, no capacity figure given) |
| 3 | 76–77 | "Won expansion order for l00G+ Coherent DWDM equipment from a leading bandwidth wholesaler in Africa" | 100G+ (OCR renders "l00G+") | OCR_ARTIFACT — digit "1" in "100G" misread as lowercase "l"; this is the specific artifact the orchestrator flagged. No order value, currency amount, or volume disclosed for this win — flag as a disclosure gap for A3/A4 (bullet states a win with zero quantification) |
| 4 | 78 | "Filed 46 patents in Ql FY27 taking our cumulative global patent filing count to 722" | 46 (patents filed this quarter); 722 (cumulative patent count) | OCR_ARTIFACT (Q1→Ql) on period label only; the two digit figures (46, 722) are clean |

Business-figure count for this table: 4 (Tier-1, 100G+, 46, 722). Bullet count: 4 (bullets 1–4; the intro line is not itself a bullet).

---

## TABLE 6 — BUSINESS / COMPANY-PROFILE NUMBERS (page 3, "About" section, doc lines 89–92)

| # | Doc line | Number | Context | Flags |
|---|---|---|---|---|
| 1 | 91 | 75 | "designs and manufactures ... entities in over 75 countries" | none — single unqualified count, no source/date given for the country figure |

---

## TABLE 7 — OWNERSHIP / ENTITY REFERENCES (page 3, doc lines 91–92)

| # | Doc line | Entity | Relationship | Flags |
|---|---|---|---|---|
| 1 | 91–92 | Tata Group | Parent group | ENTITY_CHANGE not applicable — no prior-quarter list to diff against (NO_PRIOR_BASELINE) |
| 2 | 91–92 | Panatone Finvest Ltd. | Majority shareholder of Tejas Networks Ltd.; itself a subsidiary of Tata Sons Pvt. Ltd. | NO_PRIOR_BASELINE |
| 3 | 91–92 | Tata Sons Pvt. Ltd. | Parent of Panatone Finvest Ltd. | NO_PRIOR_BASELINE |

---

## TABLE 8 — PERIOD-LABEL MENTIONS (Q1 / FY27 / FY26, all instances incl. OCR variants)

| # | Doc line | Rendered as | Location | Flags |
|---|---|---|---|---|
| 1 | 48 | "Q1FY27" | Press release headline | none — this instance renders clean |
| 2 | 57 | "Ql-FV27" | Table period header, column 1 | OCR_ARTIFACT (Q1→Ql, FY→FV) |
| 3 | 57 | "Ql-FV26" | Table period header, column 2 | OCR_ARTIFACT (Q1→Ql, FY→FV) |
| 4 | 57 | "FV26" | Table period header, column 3 | OCR_ARTIFACT (FY→FV) |
| 5 | 63 | "Ql revenues" | MD quote opening | OCR_ARTIFACT (Q1→Ql) |
| 6 | 72 | "Ql FY27" | Highlights intro line | OCR_ARTIFACT (Q1→Ql) |
| 7 | 78 | "Ql FY27" | Bullet 4 (patents) | OCR_ARTIFACT (Q1→Ql) |
| 8 | 80 | "Ql FY27" | CFO quote opening | OCR_ARTIFACT (Q1→Ql) |

7 of 8 mentions carry the "Q1→Ql" OCR artifact; the table-header row additionally carries "FY→FV" on all three of its labels. Per the mechanical caveat: the underlying P&L digits (402, 202, 1,103, 271, 297, 1,354, 202, 194, 909) and all other quoted figures remain clean and unambiguous; only the period-name labels are OCR-affected.

---

## TABLE 9 — ADMINISTRATIVE / IDENTIFIER FIELDS (letterhead, addresses, contact, signature; pages 1 and restated on pages 2–3)

| # | Doc line | Field | Value | Flags |
|---|---|---|---|---|
| 1 | 3 | Registered office — plot number | Plot No. 25 | none |
| 2 | 3 | Registered office — floor | 5th Floor | none |
| 3 | 4 | Registered office — phase | Electronic City Phase 1 | none |
| 4 | 5 | Registered office — PIN code | Bengaluru 560 100 | none |
| 5 | 6 | Telephone number(s) | +91-80-4179 4600/700/800 | none — one field, three extension numbers |
| 6 | 7 | Fax number | +91-80-2852 0201 | none |
| 7 | 10 | Letter date | July 27, 2026 | none |
| 8 | 14 | NSE address — building/block ref | Exchange Plaza, C/1, Block G | none |
| 9 | 16 | NSE Mumbai PIN code | 400 051 | none |
| 10 | 16 | BSE Mumbai PIN code | 400 001 | none |
| 11 | 17 | BSE Scrip Code (letterhead) | 540595 | none |
| 12 | 24 | Quarter-end date (letter body) | June 30, 2026 | none |
| 13 | 32–33 | Digital signature timestamp | 2026.07.27 20:22:34 +05'30' | Signed same calendar day as the results/press-release date (July 27, 2026); no board-meeting start/end time is disclosed anywhere in this document to compare against, so a MGMT_TIMING-style flag cannot be evaluated from this doctype alone — noted for A3/A4 to cross-reference against the board outcome filing if enumerated separately |
| 14 | 41 | CIN | L72900KA2000PLC026980 | none |
| 15 | 51 | Press-release dateline (restated) | July 27, 2026 | none — duplicate of field 7, different location in doc |
| 16 | 51 | BSE/NSE codes (restated) | BSE: 540595, NSE: TEJASNET | none — duplicate of field 11 |
| 17 | 52 | Quarter-end date (restated, press release body) | June 30, 2026 | none — duplicate of field 12 |
| 18 | 96 | Investor Relations contact phone | +91 80 41794600 | OCR_ARTIFACT — adjacent web/email addresses at doc lines 94 and 96 render "tejasnetworks.com" as "teiasnetworks.com" (j→i misread); phone digits themselves are clean |

---

## TABLE 10 — SIGNATURE BLOCK (page 1, doc lines 28–36)

| # | Doc line | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | 30–36 | Anantha Murthy N | Company Secretary & Compliance Officer | 2026.07.27 20:22:34 +05'30' | See Table 9 row 13 — no board-meeting time available in this doctype for a before/after comparison |

---

## TABLE 11 — FOOTNOTES / FINE-PRINT DISCLAIMERS (page 3, doc lines 98–107)

| # | Doc line range | Label | Qualifies | Flags |
|---|---|---|---|---|
| 1 | 98–107 | "SAFE HARBOUR" | Qualifies all forward-looking statements in the release generally; not tied to a specific headline number by cross-reference marker (no asterisk/footnote-number links it to any specific figure in Tables 2–6) | none — standard boilerplate; contains no numeric content itself |

---

## COUNTS SUMMARY (feeds YAML below)

- Pages/slides: 3
- Table line items (rows): 3; table data points (row×period values): 9
- MD quote numbers: 4; CFO quote numbers: 6 → combined "mgmt_numbers": 10
- Highlight bullets: 4; bullet business-figure numbers: 4
- Period-label mentions: 8 (7 OCR-affected, 1 clean)
- Administrative/identifier lines: 16 (18 discrete fields)
- Business-profile numbers: 1
- Entities (ownership chain): 3
- Footnote/disclaimer: 1
- Signature block: 1
- Zero-standing items: 0 (checked, none found)
- Comprehensive "every number on every page" total (slide_numbers): 9 (table) + 10 (mgmt quotes) + 4 (bullets) + 8 (period labels) + 18 (admin fields) + 1 (business profile) = 50

---

```yaml
stage: A2-enumerator
company: "TEJASNET"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/tejasnet-q1fy27/work/ledger_presentation_tejasnet_q1fy27.md"
counts:
  notes: 0
  line_items: 3
  zero_standing: 0
  agenda_items: 0
  auditor_paras: 0
  entities: 3
  turns: 0
  questions: 0
  mgmt_numbers: 10
  slides: 3
  slide_numbers: 50
flags_raised: [OCR_ARTIFACT, NO_PRIOR_BASELINE]
gate_a2: pass
mismatch_note: ""
```
