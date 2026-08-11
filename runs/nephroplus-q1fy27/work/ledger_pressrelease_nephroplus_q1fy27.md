# A2 COMPLETENESS LEDGER — Press Release Companion, NephroPlus (Nephrocare Health Services Ltd), Q1FY27

Source: `runs/nephroplus-q1fy27/work/extract_pressrelease_nephroplus_q1fy27.txt`
Doctype: results (press-release companion to Reg 33 filing — apply results-branch table enumeration; narrative branch improvised per task injection since this is not a standard results filing with numbered notes / Board Outcome / auditor report / consolidation list)
Unit convention: Rs Crores (x1, already in crores per header)
Line numbers cited below are the embedded A1 extraction line numbers (the digit immediately following each `Read`/`grep` row index in the source file), not raw file offsets.

```
=== A2 COUNT TEST ===
category: cover_letter_items         grep_count: 7   sweep_count: 7   match: yes
category: line_items (fin. tables)   grep_count: 8   sweep_count: 8   match: yes
category: zero_standing              grep_count: 0   sweep_count: 0   match: yes
category: notes (table footnotes)    grep_count: 3   sweep_count: 3   match: yes
category: numbered_notes             grep_count: 0   sweep_count: 0   match: yes (not present in press-release-class document)
category: narrative_quantified_metrics grep_count: 19 sweep_count: 19 match: yes
category: management_quotes          grep_count: 3   sweep_count: 3   match: yes
category: digital_signature_blocks   grep_count: 1   sweep_count: 1   match: yes
category: contact_blocks             grep_count: 2   sweep_count: 2   match: yes
category: safe_harbour_paragraph     grep_count: 1   sweep_count: 1   match: yes
category: agenda_items (Board Outcome) grep_count: 0 sweep_count: 0   match: yes (not present in press-release-class document)
category: auditor_paras              grep_count: 0   sweep_count: 0   match: yes (not present in press-release-class document)
category: entities (consolidation list) grep_count: 0 sweep_count: 0  match: yes (not present in press-release-class document; About-paragraph geography list captured as narrative metric M18/M28 instead, not a formal consolidation entity list)
category: annexures/director_profiles grep_count: 0  sweep_count: 0   match: yes (not present in press-release-class document)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on the narrative_quantified_metrics reconciliation: grep pass used a curated list of 19 unique anchor substrings (one per discrete quantified claim identified by manual sweep), run with `grep -o -E` so that multiple claims sharing one physical (wrapped) source line each register as a separate match. All 19 anchors matched exactly once each, with no unmatched claims left over on manual re-check of lines 67-134. First attempt at a looser keyword-alternation grep (row-based, not claim-based) returned 16 line-hits and would have under-counted a QoQ EBITDA-margin claim that wraps onto its own line (L79) — re-swept and corrected before emitting, per GATE A2.

---

## 1. COVER LETTER / TRANSMITTAL ITEMS (page 1) — 7 rows

| # | Line | Item | Value / Text | Flags |
|---|------|------|---------------|-------|
| T1 | L2 | Filing reference number | "Ref: NEPHROPLUS/SE/71" | |
| T2 | L3 | Letter date | August 11, 2026 | |
| T3 | L9 | Scrip Code (BSE) | 544647 | |
| T4 | L9 | Scrip Symbol (NSE) | NEPHROPLUS | |
| T5 | L12 | Subject line | "Press Release on Q1FY27 Financial Results" | |
| T6 | L13-14, L18 | Regulatory basis (stated twice, same fact) | Regulation 30 of SEBI (LODR) Regulations, 2015 | |
| T7 | L18-20 | Purpose/scope statement | "Unaudited Standalone and Consolidated financial results of the Company for the quarter ended June 30, 2026" | **STANDALONE_NOT_IN_EXTRACT** — letter claims both Standalone and Consolidated results are enclosed, but no standalone financial highlights table appears anywhere in the 4-page extract; only the "Consolidated Performance: Q1FY27" table (L45-56) is present |

## 2. FINANCIAL HIGHLIGHTS TABLE — Consolidated Performance: Q1FY27 (page 2, Rs Cr) — 5 rows

| # | Line | Particular | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Flags |
|---|------|-----------|--------|--------|-----|--------|-----|-------|
| L1 | L47 | Revenue | 281.8 | 227.8 | 23.7% | 265.6 | 6.1% | |
| L2 | L48 | Adj. EBITDA* | 65.1 | 49.8 | 30.7% | 55.4 | 17.5% | |
| L3 | L49 | Adj. EBITDA Margin* | 23.1% | 21.9% | (blank — no bps figure shown) | 20.9% | (blank — no bps figure shown) | **MARGIN_DELTA_OMITTED** — table's YoY/QoQ columns are blank for both margin rows even though the narrative bullets (L78-80) separately state the YoY (+120bps) and QoQ (+220bps) point changes; the table itself does not carry them |
| L4 | L51 | Adj. PAT# | 36.8 | 26.0 | 41.7% | 35.1 | 4.7% | |
| L5 | L52 | Adj. PAT Margin# | 13.1% | 11.4% | (blank) | 13.2% | (blank) | **MARGIN_DELTA_OMITTED** (same as L3) |

No line item in this table is zero, nil, or dash-valued across all periods; `zero_standing` = 0 for this table.

## 3. FINANCIAL HIGHLIGHTS TABLE — Operational Highlights: Q1FY27 (page 2, non-Rs metrics) — 3 rows

| # | Line | Particular | Q1FY27 | Q1FY26 | YoY | Q4FY26 | QoQ | Flags |
|---|------|-----------|--------|--------|-----|--------|-----|-------|
| L6 | L62 | Treatments | 10,31,084 | 9,09,860 | 13.3% | 9,96,074 | 3.5% | |
| L7 | L63 | RPT (Revenue Per Treatment) | 2,733 | 2,503 | 9.2% | 2,667 | 5.2% | |
| L8 | L64 | Guests | 38,262 | 33,868 | 13.0% | 36,981 | 3.5% | |

No line item in this table is zero, nil, or dash-valued across all periods; `zero_standing` = 0 for this table.

## 4. TABLE FOOTNOTES (asterisk/hash markers below the financial tables) — 3 rows

| # | Line | Marker | Text | Flags |
|---|------|--------|------|-------|
| N1 | L53 | * | "EBITDA adjusted for ESOP expenses of Rs. 1.3 crores in Q1FY27, Rs. 2.3 crores in Q1FY26, Rs. 1.7 crores in Q4FY26" | |
| N2 | L54-56 | # | "PAT adjusted for share of loss from JV of 3.6 crores, ESOP expenses of Rs. 1.3 crores in Q1 FY27, ESOP expenses of Rs. 2.3 crores in Q1 FY26 and share of loss from JV of 3.1 crores, ESOP expenses of Rs. 1.7 crores in Q4 FY26" | |
| N3 | L83 | * | "EBITDA adjusted for Saudi expenses and ESOP expenses" | **INCONSISTENT_DEFINITION** — this second "*" footnote (in the bullet-highlights section) defines the Adj. EBITDA adjustment as covering "Saudi expenses and ESOP expenses," while N1 (the table footnote, same asterisk marker, same metric) defines it only as ESOP expenses with no mention of Saudi expenses. Two differing definitions share the same marker in the same document; not reconciled anywhere in the extract. |

Numbered notes (financial-statement style, e.g. "1. ... 2. ...") — **0 found**; not present in press-release-class document (confirmed via `grep -n -E "^\s*[0-9]+\.\s"`, no matches).

## 5. NARRATIVE QUANTIFIED OPERATIONAL METRICS/CLAIMS (bullets + quote sub-metrics + About-paragraph) — 19 rows

| # | Line | Source | Claim | Flags |
|---|------|--------|-------|-------|
| M1 | L70 | Bullets | Q1FY27 revenue of ₹281.8 crore, +23.7% YoY | |
| M2 | L72-73 | Bullets | Treatments up 13.3% YoY to 10.31 lakh (Q1FY26: 9.10 lakh) | |
| M3 | L73 | Bullets | Guests up 13.0% YoY to 38,262 | |
| M4 | L73-74 | Bullets | Revenue per treatment +9.2% YoY to ₹2,733 (Q1FY26: ₹2,503) | |
| M5 | L76 | Bullets | Adjusted EBITDA of ₹65.1 crore, +30.7% YoY | |
| M6 | L78-79 | Bullets | Adjusted EBITDA margin expanded 120 bps YoY to 23.1% (Q1FY26: 21.9%) | |
| M7 | L79-80 | Bullets | Adjusted EBITDA margin improved 220 bps sequentially over Q4FY26 (20.9%) | |
| M8 | L82 | Bullets | Adjusted PAT grew 41.7% YoY to ₹36.8 crore (Q1FY26: ₹26.0 crore) | |
| M9 | L88 | Chairman & MD quote | Only 21% of India's dialysis services market is served by pure-play dialysis networks today | |
| M10 | L89 | Chairman & MD quote | "16 years ago, this number was zero" (historical pure-play penetration claim, unaudited/unsourced) | |
| M14 | L102 | Group CEO quote | Revenue grew 23.7% YoY to ₹282 crore | **ROUNDING_VARIANCE** vs table's ₹281.8 crore (L47) / bullet's ₹281.8 crore (L70) |
| M15 | L102-103 | Group CEO quote | EBITDA grew 30.7% YoY to ₹65 crore | **ROUNDING_VARIANCE** vs table's/bullet's ₹65.1 crore (L48, L76) |
| M16 | L103 | Group CEO quote | Guest volumes grew 13% YoY to 38,262 | minor rounding (13% vs table's/bullet's 13.0%, L64/L73) — not flagged, immaterial |
| M17 | L103-104 | Group CEO quote | "Crossed 10,30,000 treatments" in the quarter | **ROUNDING_VARIANCE** vs table's precise 10,31,084 (L62) / bullet's "10.31 lakh" (L72) |
| M18 | L104 | Group CEO quote | Network reached 550 operating clinics across 5 countries | new metric, not stated in either financial table |
| M19 | L104-105 | Group CEO quote | "Significant 50-clinic milestone" reached in the Philippines | new metric |
| M25 | L124-125 | CFO quote | Restates: Revenue +23.7% YoY, Adjusted EBITDA +30.7%, Adjusted PAT +41.7% ("each line outpacing the one above it") | **REPEAT_METRIC** — third restatement of the same three growth rates already given in M1/M5/M8 and M14/M15 (CEO quote); no new figures |
| M27 | L131 | About paragraph | "Owning and operating 550 dialysis centres" | **REPEAT_METRIC** — duplicate of M18's "550 operating clinics" (Group CEO quote); consistent, not a discrepancy |
| M28 | L132-133 | About paragraph | Footprint named across 5 countries: India, Nepal, the Philippines, Uzbekistan, Saudi Arabia | consistent with M18's "5 countries"; first place the 5 countries are individually named |

Note: the three verbatim management quotes (Section 6 below) also carry qualitative/forward-looking content without standalone numeric values (e.g., strategic rationale for international expansion, the NIDA training-academy launch, the NephroPlus Dialysis Index launch, margin-discipline commentary). That qualitative content is preserved in full in the verbatim quote capture in Section 6 and is not separately itemized here, consistent with the task scope of "every quantified operational metric."

## 6. MANAGEMENT COMMENTARY QUOTES (verbatim) — 3 rows

| # | Line | Speaker | Quote (verbatim) |
|---|------|---------|-------------------|
| Q1 | L86-98 | Mr. Vikram Vuppala, Chairman & MD | "Dialysis services across the World are mostly delivered by Pure play dialysis networks. In India, today, only 21% of the dialysis services market is served by Pure play dialysis networks. 16 years ago, this number was zero. As the dialysis industry is shifting from Unorganized to Organized, NephroPlus, as the market leader in India stands to gain disproportionately due to its focus on clinical quality, service excellence and patient centricity. As we all know, the dialysis market is growing fast due to the ever-increasing burden of Diabetes and Hypertension and this additional lever of shift from Unorganized to Organized will help NephroPlus expand across India including the Tier 2/Tier 3 cities and beyond. As we continue to scale up in existing countries, we are also exploring entry into new countries via strategic acquisitions or long-term partnerships with payors. We will continue to invest in identifying and understanding new geographies where we believe we can make massive impact on dialysis patients' lives while creating shareholder value in the long term." |
| Q2 | L100-116 | Mr. Rohit Singh, Group Chief Executive Officer | "Q1 FY27 was a quarter of strong financial performance and continued strategic expansion for NephroPlus. Revenue grew 23.7% year-on-year to ₹282 crore, and EBITDA grew 30.7% YoY to ₹65 crore. Guest volumes grew 13% YoY to 38,262, as we crossed 10,30,000 treatments in the first quarter of this financial year. Our network reached 550 operating clinics across 5 countries, with a significant 50-clinic milestone in the Philippines. NephroPlus continues to demonstrate that it is a dialysis platform made in India for the world. This past quarter, we launched the NephroPlus International Dialysis Academy (NIDA), an in-house training program based in India and the Philippines, to build a robust pipeline of renal nurses qualified to work anywhere in the world. This will enable us to efficiently staff our international dialysis clinics where hiring renal nurses is a huge challenge. Also, we have undertaken initiatives to increase fistula creation and reduce cross-infections, and have launched the NephroPlus Dialysis Index, a composite health score designed to monitor clinical outcomes at the patient level, which can be aggregated at the Clinic, Cluster, Zone, and Country levels over the next few quarters. Overall, we remain confident in our ability to grow profitably and efficiently while delivering superior clinical quality across every market we serve." |
| Q3 | L118-128 | Mr. Prashant Goenka, Chief Financial Officer | "Q1 FY27 reflects the strength of our India platform — operating profitably at some of the lowest price points globally, a solid reflection of the underlying efficiency of our model. This efficiency, combined with high barriers to entry in dialysis care, gives us the confidence to scale into the higher price-point international markets, while preserving margin discipline rather than chasing growth at any cost. Revenue grew 23.7% year-on-year, while Adjusted EBITDA grew faster at 30.7% and Adjusted PAT faster still at 41.7% — each line outpacing the one above it, a clear signature of operating leverage as platform strength converts scale into higher profitability and returns. Capital continues to be deployed with discipline, keeping us on track for durable, long-term value creation" |

## 7. DIGITAL SIGNATURE BLOCK — 1 row

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| S1 | L25-35 | Kishore Kathri | Company Secretary and Head Legal (Membership No. F9895) | Digitally signed 2026.08.11 18:20:28 +05'30' | Letter date (L3, "August 11, 2026") and signature date (2026.08.11) are the same calendar day; no board meeting start/end time is stated anywhere in this document (press release, not a Board Outcome letter), so a pre-meeting-conclusion signature timing check is not possible from this extract |

## 8. CONTACT / INVESTOR-RELATIONS BLOCKS (page 4) — 2 rows

| # | Line | Block | Detail |
|---|------|-------|--------|
| C1 | L139-144 | Company IR contact | Nephrocare Health Services Limited; Mr. Rohit Aidasani; investor.relations@nephroplus.com |
| C2 | L145-151 | External IR agency | Strategic Growth Advisors; Mr. Sagar Shroff / Mr. Ayush Haria; +91 98205 19303 / +91 98204 62966; sagar.shroff@sgapl.net / ayush.haria@sgapl.net |

## 9. SAFE HARBOUR / FORWARD-LOOKING STATEMENT DISCLAIMER — 1 row

| # | Line | Text |
|---|------|------|
| SH1 | L154-163 | "Statements in this document relating to future status, events, or circumstances, including but not limited to statements about plans and objectives, the progress and results of research and development, potential project characteristics, project potential and target dates for project related issues are forward-looking statements based on estimates and the anticipated effects of future events on current and developing circumstances. Such statements are subject to numerous risks and uncertainties and are not necessarily predictive of future results. Actual results may differ materially from those anticipated in the forward-looking statements. The company assumes no obligation to update forward-looking statements to reflect actual results changed assumptions or other factors." |

## 10. CATEGORIES NOT PRESENT IN THIS DOCUMENT

| Category | Count | Note |
|---|---|---|
| Board Outcome agenda items (AR approval, AGM notice, record date, dividend, director appointments, auditor changes, scrutinizer, ESOP grants, capital-raising resolutions) | 0 | not present in press-release-class document; this is a press release, not the Board Outcome letter |
| Board meeting start/end times | 0 | not present in press-release-class document |
| Annexures / director profile tables (name, DIN, role, term dates, background, relationships) | 0 | not present in press-release-class document |
| Auditor report paragraphs (opinion type, EOM, Other Matters, Going Concern, entity list, UDIN) | 0 | not present in press-release-class document |
| Formal consolidation entity list with relationship type | 0 | not present in press-release-class document; About-paragraph geography footprint (India, Nepal, Philippines, Uzbekistan, Saudi Arabia) is a narrative operating-footprint claim, not a formal subsidiary/JV/associate consolidation list with relationship type, and is captured instead as narrative metrics M18/M28 |

## TOTAL LEDGER ROWS

7 (cover letter) + 8 (financial table line items) + 3 (footnotes) + 19 (narrative quantified metrics) + 3 (management quotes) + 1 (digital signature) + 2 (contact blocks) + 1 (safe harbour) = **44 rows**

## FLAGS SUMMARY

- `STANDALONE_NOT_IN_EXTRACT` (T7) — cover letter claims standalone + consolidated results enclosed; only consolidated table present in extract
- `MARGIN_DELTA_OMITTED` (L3, L5) — table YoY/QoQ columns blank for both margin line items despite bps deltas being stated in the narrative bullets
- `INCONSISTENT_DEFINITION` (N3 vs N1) — two "*" footnotes with different Adj. EBITDA adjustment definitions (Saudi + ESOP vs ESOP-only)
- `ROUNDING_VARIANCE` (M14, M15, M17) — Group CEO quote restates revenue/EBITDA/treatments using rounded figures that differ from the precise table values
- `REPEAT_METRIC` (M25, M27) — same growth-rate triplet and clinic count restated across multiple narrative sources without new information
