# A2 ENUMERATION LEDGER — Press Release (results-class), DSSL Q1 FY27

Source: `runs/dssl-q1fy27/work/extract_pressrelease_dssl_q1fy27.txt` (311 lines,
4 pages, 100% page coverage, no OCR pages flagged though ligature artifacts
`ﬁ`/`ﬂ`/`Ɵ` from the source PDF font are present throughout — see note under
Table 4/9/11 methodology).

Doctype note: this is a press release (management commentary + summary
tables), not a formal Reg 33 results filing. The RESULTS FILING enumeration
rules (notes / board agenda / annexures / auditor paragraphs / consolidation
entity list) are therefore N/A where the underlying disclosure unit does not
exist in this document; each N/A is recorded explicitly below rather than
silently omitted. Digital signature block (rule 7) IS present and is
enumerated.

=== A2 COUNT TEST ===
category: admin_identifiers      grep_count: 10  sweep_count: 10  match: yes
category: key_highlights_bullets grep_count: 7   sweep_count: 7   match: yes
category: key_highlights_kpis    grep_count: 16  sweep_count: 16  match: yes
category: segment_table_cells    grep_count: 24  sweep_count: 24  match: yes
category: pl_summary_cells       grep_count: 25  sweep_count: 25  match: yes
category: geo_table_cells        grep_count: 24  sweep_count: 24  match: yes
category: innovation_bullets     grep_count: 5   sweep_count: 5   match: yes
category: innovation_kpis        grep_count: 12  sweep_count: 12  match: yes
category: mgmt_quotes            grep_count: 2   sweep_count: 2   match: yes
category: quote_kpis             grep_count: 15  sweep_count: 15  match: yes
category: headline_duplicates    grep_count: 3   sweep_count: 3   match: yes
category: boilerplate_sections   grep_count: 5   sweep_count: 5   match: yes
category: notes                  grep_count: 0   sweep_count: 0   match: yes  (N/A — no numbered notes in a press release)
category: agenda_items           grep_count: 0   sweep_count: 0   match: yes  (N/A — no Board Outcome letter attached)
category: auditor_paras          grep_count: 0   sweep_count: 0   match: yes  (N/A — no auditor report attached)
category: entities                grep_count: 0   sweep_count: 0   match: yes  (N/A — no consolidation entity list disclosed in this document)
category: zero_standing          grep_count: 0   sweep_count: 0   match: yes  (all table cells populated; no nil/dash template line found)
gate_a2: pass
=== END COUNT TEST ===

Grep methodology note: table-cell counts were reconciled by `sed -n '<range>p'
| grep -c -v '^$'` (total non-blank lines in the table's line range) minus
`grep -c -E '^(<row labels>)$'` (row-label lines), verified against manual
line-by-line read. Bullet counts reconciled by `grep -c '^•'` within each
section's line range. KPI-within-narrative counts were reconciled with a
digit-token regex (`[0-9]+(\.[0-9]+)?%|₹[0-9]+(\.[0-9]+)?|[0-9]+,?[0-9]*\+?`,
with `Q[0-9]+`/`FY[0-9]+` period labels stripped first so quarter/FY tags are
not miscounted as KPI values) PLUS a ligature-normalized spelled-out-number
sweep (`ﬁ`→`fi` etc., then word-list match on one/two/…/ninth/first) run in
Python, because plain grep silently misses words rendered with PDF ligature
glyphs (e.g. "first" is encoded as `ﬁrst` in this extract and a naive
`\bfirst\b` grep misses it). Both passes were run and reconciled per category
before the counts above were locked.

---

## TABLE 1 — Cover Letter & Administrative Identifiers (10 rows)

| # | Line(s) | Item | Flags |
|---|---|---|---|
| A-1 | 18-19 | Registered office: New Municipal No. 1, Sri Subramanya Plaza (SS Plaza), 29th Main Road, BTM Layout, 1st stage, Ring Road, Bengaluru, Bengaluru Urban, Karnataka, PIN 560068 | — |
| A-2 | 20 | Tel 080-22244002; CIN L62099KA2024PLC184626 | — |
| A-3 | 22 | Letter date: July 27, 2026 | — |
| A-4 | 24-29 | BSE recipient: Listing Dept, BSE Ltd, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai-400001; Scrip Code 544413 | — |
| A-5 | 30-36 | NSE recipient: Listing Dept, NSE of India Ltd, Exchange Plaza, BKC, Bandra (East), Mumbai-400051; Symbol DIGITIDE | — |
| A-6 | 42-43 | Cover letter quotes the press release title verbatim: "Digitide returns to profitability in Q1 FY27; revenue rises 5.3% YoY to ₹775 crores" | DUPLICATE_MENTION (cross-ref Table 12 HD-1), ROUNDING_VARIANCE (₹775 vs ₹775.1 in Table 5/6) |
| A-7 | 56-58 | Signatory: Shailesha Barve, Company Secretary & Compliance Officer, Membership No. A50601 | — |
| A-8 | 62-67 | Digital signature block: "SHAILESHA BARVE / Digitally signed by SHAILESHA BARVE / Date: 2026.07.27 21:30:02 +05'30'" | DATA_GAP — no board meeting start/end time is disclosed anywhere in this document, so the signature timestamp (9:30 PM same day) cannot be benchmarked against a meeting-conclusion time per rule 7 |
| A-9 | 15, 69, 214, 271 | Page markers [page 1]-[page 4] (structural only, 4 occurrences) | — |
| A-10 | 20, 283 | Website www.digitide.com stated twice (letterhead + About section) | DUPLICATE_MENTION (minor) |

## TABLE 2 — Digital Signature Block
Folded into A-8 above per rule 7 (single signature block in this document; no separate board-outcome signatory to cross-check).

## TABLE 3 — Key Highlights: Bullet-level (7 rows)

| # | Line(s) | Bullet text (paraphrased) | Flags |
|---|---|---|---|
| B-1 | 81-82 | Revenue +5.3% YoY to ₹775.1 Cr, driven by disciplined focus on profitable growth | — |
| B-2 | 83-85 | Reported PAT turned positive at ₹2.9 Cr after two quarters, no exceptional items, "reflecting improved earnings quality" | — |
| B-3 | 86-88 | EBITDA ₹76.9 Cr declined QoQ, driven by lower revenues and minimum wage revisions across states | SELECTIVE_DISCLOSURE — bullet states direction ("declined") but omits the -12.5% QoQ magnitude that IS shown in Table 6, unlike B-1/B-4/B-5 which all state their % change explicitly |
| B-4 | 89-90 | T&D revenue +20.3% YoY to ₹237.4 Cr, contributing 31% of total revenue | — |
| B-5 | 91-92 | International revenue +10.2% YoY to ₹295.6 Cr, accounting for 38% of total revenue | — |
| B-6 | 93-94 | TCV bookings ₹205 Cr, supported by 26 key logo wins | — |
| B-7 | 95-96 | AI interactions reached 5.7 Mn incl. 2.5 Mn voice bots and 3.2 Mn chatbots | — |

## TABLE 4 — Key Highlights: Embedded KPI-level (16 rows)

| # | Line | KPI | Flags |
|---|---|---|---|
| KH-1 | 82 | 5.3% YoY revenue growth | DUPLICATE_MENTION (headline, both quotes, Table 6) |
| KH-2 | 82 | ₹775.1 Cr revenue | DUPLICATE_MENTION |
| KH-3 | 84 | ₹2.9 Cr Reported PAT | DUPLICATE_MENTION (matches Table 6) |
| KH-4 | 84 | "two quarters" — duration PAT was negative before turning positive | UNDEFINED_KPI (the two prior quarters are not named or shown; only Q4FY26 PAT (-5.0) is visible in this document) |
| KH-5 | 87 | ₹76.9 Cr EBITDA | DUPLICATE_MENTION, NON_GAAP_MEASURE (no reconciliation to Reported PAT or definition of EBITDA shown anywhere in this document) |
| KH-6 | 90 | 20.3% YoY T&D growth | DUPLICATE_MENTION |
| KH-7 | 90 | ₹237.4 Cr T&D revenue | DUPLICATE_MENTION |
| KH-8 | 90 | 31% of total revenue (T&D mix) | DUPLICATE_MENTION, ROUNDING_VARIANCE (Table 5 shows 30.6% for Q1FY27 T&D mix; 31% is a whole-number round-up) |
| KH-9 | 92 | 10.2% YoY International growth | DUPLICATE_MENTION |
| KH-10 | 92 | ₹295.6 Cr International revenue | DUPLICATE_MENTION |
| KH-11 | 92 | 38% of total revenue (International mix) | DUPLICATE_MENTION, ROUNDING_VARIANCE (Table 7 shows 38.1%) |
| KH-12 | 94 | ₹205 Cr TCV bookings | UNDEFINED_KPI (no TCV definition — contract duration, deal-type inclusion/exclusion criteria — given; no footnote), DUPLICATE_MENTION (also in CFO quote FQ-10) |
| KH-13 | 94 | 26 key logo wins | UNDEFINED_KPI ("key logo" threshold/deal-size undefined), DUPLICATE_MENTION (also CFO quote FQ-11) |
| KH-14 | 96 | 5.7 Mn AI interactions | UNDEFINED_KPI (no definition of what constitutes one "AI interaction") |
| KH-15 | 96 | 2.5 Mn voice bot interactions | UNDEFINED_KPI; internally consistent as a subtotal (2.5+3.2=5.7 ties to KH-14) |
| KH-16 | 96 | 3.2 Mn chatbot interactions | UNDEFINED_KPI; ties to KH-14 subtotal |

## TABLE 5 — Segment Performance Table: Cell-level (24 cells, 3 line items x 8 columns)

Columns per row: Q1FY26 value, Q1FY26 Mix, Q4FY26 value, Q4FY26 Mix, Q1FY27 value, Q1FY27 Mix, QoQ, YoY.

| Line item | Line | Q1FY26 | Mix | Line | Q4FY26 | Mix | Line | Q1FY27 | Mix | Line | QoQ | YoY | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BPM | 109-110 | 538.6 | 73.2% (111) | 112 | 550.8 | 68.9% (113) | 114 | 537.7 | 69.4% (115) | 116/117 | -2.4% | -0.2% | — |
| T&D | 118-119 | 197.2 | 26.8% (120) | 121 | 249.2 | 31.1% (122) | 123 | 237.4 | 30.6% (124) | 125/126 | -4.7% | 20.3% | DUPLICATE_MENTION vs KH-6/7/8, FQ-3/4/5 |
| Total | 127-128 | 735.8 | 100.0% (129) | 130 | 800.0 | 100.0% (131) | 132 | 775.1 | 100% (133) | 134/135 | -3.1% | 5.3% | DUPLICATE_MENTION vs Table 6 Revenue row and Table 7 Total row (same figures, three tables) |

(Individual cell rows, 24 total, expanded: BPM×8 = lines 110,111,112,113,114,115,116,117; T&D×8 = lines 119,120,121,122,123,124,125,126; Total×8 = lines 128,129,130,131,132,133,134,135.)

## TABLE 6 — Revenue / EBITDA / EBITDA% / Reported PAT / Reported PAT% Block: Cell-level (25 cells, 5 line items x 5 columns)

Columns: Q1FY26, Q4FY26, Q1FY27, QoQ, YoY (no Mix column in this block).

| Line item | Line | Q1FY26 | Q4FY26 | Q1FY27 | QoQ | YoY | Cell lines | Flags |
|---|---|---|---|---|---|---|---|---|
| Revenue | 148 | 735.8 | 800.0 | 775.1 | -3.1% | 5.3% | 149,150,151,152,153 | DUPLICATE_MENTION (Table 5 Total, Table 7 Total) |
| EBITDA | 154 | 82.6 | 87.9 | 76.9 | -12.5% | -6.9% | 155,156,157,158,159 | NON_GAAP_MEASURE; -12.5% QoQ not restated in narrative bullet B-3 (SELECTIVE_DISCLOSURE, see B-3) |
| EBITDA % | 160 | 11.2% | 11.0% | 9.9% | -107bps | -131bps | 161,162,163,164,165 | NON_GAAP_MEASURE |
| Reported PAT | 166 | 9.7 | -5.0 | 2.9 | "Turned Positive" | -69.7% | 167,168,169,170,171 | SUPPRESSED_METRIC — QoQ cell is a text label ("Turned Positive") instead of a numeric %, because Q4FY26 base was negative (-5.0); no absolute ₹ swing given anywhere in the narrative either |
| Reported PAT % | 172 | 1.3% | -0.6% | 0.4% | 100bps | -94bps | 173,174,175,176,177 | — |

(25 cell rows total: 5 line items x 5 columns, with the PAT-row QoQ cell being the non-numeric "Turned Positive" token — still counted as one enumerated cell per rule 2.)

## TABLE 7 — Geographical Performance Table (Domestic/International/Total): Cell-level (24 cells, 3 line items x 8 columns)

| Line item | Line | Q1FY26 | Mix | Q4FY26 | Mix | Q1FY27 | Mix | QoQ | YoY | Cell lines | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Domestic | 186 | 467.6 | 63.6% | 495.5 | 61.9% | 479.5 | 61.9% | -3.2% | 2.5% | 187-194 | — |
| International | 195 | 268.2 | 36.4% | 304.5 | 38.1% | 295.6 | 38.1% | -2.9% | 10.2% | 196-203 | DUPLICATE_MENTION vs KH-9/10/11, FQ-6/7/8 |
| Total | 204 | 735.8 | 100.0% | 800.0 | 100.0% | 775.1 | 100% | -3.1% | 5.3% | 205-212 | DUPLICATE_MENTION vs Table 5 Total, Table 6 Revenue row — identical figures across all 3 tables (internally consistent cross-check, not a red flag) |

(24 cell rows total: Domestic×8 = 187,188,189,190,191,192,193,194; International×8 = 196,197,198,199,200,201,202,203; Total×8 = 205,206,207,208,209,210,211,212.)

## TABLE 8 — Innovation, Partnership and People: Bullet-level (5 rows)

| # | Line(s) | Bullet text (paraphrased) | Flags |
|---|---|---|---|
| I-1 | 220-222 | New strategic roadmap: improving account economics, accelerating digital/international mix, disciplined value-accretive M&A | Qualitative only, no numbers |
| I-2 | 223-225 | First AI Innovation Lab established for a marquee customer; scalable engagement model now extended across client base; "12+ active discussions underway" | — |
| I-3 | 226-229 | Proprietary AI employees (Nikki, Neil, NINA, Q-Buddy) across HR/recruitment/onboarding/operations; lower attrition; 16,000+ hires in six months; NPS improved by 15% | — |
| I-4 | 230-233 | ARISE AI skills platform; 25-30% improvement in code generation productivity across six live projects | — |
| I-5 | 234-236 | Ranked Top 10 India's Best Workplaces in Health & Wellness 2026 (Great Place to Work); ICICI Prudential Tatva ranked Digitide its #1 partner for the ninth consecutive year | — |

## TABLE 9 — Innovation, Partnership and People: Embedded KPI-level (12 rows)

| # | Line | KPI | Flags |
|---|---|---|---|
| IN-1 | 224 | "first" AI Innovation Lab (ordinal claim) — note: rendered as ligature `ﬁrst` in source extract | UNDEFINED_KPI (no count of total labs; unverifiable claim) |
| IN-2 | 225 | "12+" active discussions | UNDEFINED_KPI (no definition of "active discussion," no conversion/close-rate context) |
| IN-3 | 228 | "16,000+" hires | UNDEFINED_KPI (gross vs net hires not specified; no attrition-adjusted headcount) |
| IN-4 | 228 | "six months" — period for the 16,000+ hires | UNDEFINED_KPI (start date of the six-month window not given) |
| IN-5 | 229 | "15%" NPS improvement | UNDEFINED_KPI (no baseline NPS value, no clarity on percentage points vs relative %, no methodology footnote) |
| IN-6 | 232 | "25%" — lower bound of code-gen productivity improvement range | UNDEFINED_KPI (no baseline productivity metric defined) |
| IN-7 | 232 | "30%" — upper bound of code-gen productivity improvement range | UNDEFINED_KPI |
| IN-8 | 232-233 | "six" live projects (denominator for the 25-30% claim) | UNDEFINED_KPI (six out of how many total client engagements not stated) |
| IN-9 | 235 | "Top 10" Best Workplaces in Health & Wellness 2026 | UNDEFINED_KPI (third-party award; scoring methodology not cited in this document) |
| IN-10 | 235 | "2026" award year | Factual/date, no flag |
| IN-11 | 236 | "#1" partner ranking (ICICI Prudential Tatva) | UNDEFINED_KPI (client's internal ranking methodology not disclosed) |
| IN-12 | 236 | "ninth consecutive year" — duration of the #1 ranking | UNDEFINED_KPI (no prior-year citation for independent verification) |

## TABLE 10 — Management Quotes: Quote-level (2 rows)

| # | Line(s) | Speaker | Role | Flags |
|---|---|---|---|
| Q-1 | 238-246 | Sameer Ahluwalia | Group Chief Executive Officer and Executive Director | Introduces new "four priorities" strategic framework (first appearance in this document) |
| Q-2 | 248-257 | Suraj Prasad | Group Chief Financial Officer | Restates 8 of the 16 Key Highlights KPIs at rounded precision (see Table 11) |

## TABLE 11 — Management Quotes: Embedded KPI-level (15 rows)

CEO quote (Q-1), 4 KPIs:

| # | Line | KPI | Flags |
|---|---|---|---|
| CQ-1 | 239 | 5.3% YoY revenue growth | DUPLICATE_MENTION |
| CQ-2 | 239 | ₹775 Cr revenue | DUPLICATE_MENTION, ROUNDING_VARIANCE (vs ₹775.1 Cr, Table 6) |
| CQ-3 | 242 | "over 300 clients" | UNDEFINED_KPI (vague "over," no exact count, no source, not corroborated elsewhere in the document) |
| CQ-4 | 242 | "four priorities" — Get Unified, Strengthen the Core, Go West/Go Digital, Go All Out | New disclosure, not previously named in Key Highlights or Innovation bullets |

CFO quote (Q-2), 11 KPIs:

| # | Line | KPI | Flags |
|---|---|---|---|
| FQ-1 | 249 | ₹775 Cr revenue | DUPLICATE_MENTION, ROUNDING_VARIANCE |
| FQ-2 | 249 | 5.3% YoY growth | DUPLICATE_MENTION |
| FQ-3 | 250 | 20.3% YoY T&D growth | DUPLICATE_MENTION |
| FQ-4 | 250 | ₹237 Cr T&D revenue | DUPLICATE_MENTION, ROUNDING_VARIANCE (vs ₹237.4 Cr, Table 5) |
| FQ-5 | 250 | 31% of revenue (T&D mix) | DUPLICATE_MENTION, ROUNDING_VARIANCE (vs 30.6%, Table 5) |
| FQ-6 | 251 | 10.2% YoY International growth | DUPLICATE_MENTION |
| FQ-7 | 251 | ₹296 Cr International revenue | DUPLICATE_MENTION, ROUNDING_VARIANCE (vs ₹295.6 Cr, Table 7) |
| FQ-8 | 251 | 38% of revenue (International mix) | DUPLICATE_MENTION, ROUNDING_VARIANCE (vs 38.1%, Table 7) |
| FQ-9 | 252 | "two quarters" PAT-positive duration | DUPLICATE_MENTION (same claim as KH-4), UNDEFINED_KPI |
| FQ-10 | 253 | ₹205 Cr TCV bookings | DUPLICATE_MENTION (same as KH-12), UNDEFINED_KPI |
| FQ-11 | 254 | 26 key logos added | DUPLICATE_MENTION (same as KH-13), UNDEFINED_KPI |

## TABLE 12 — Headline / Title Duplicate Mentions (3 rows)

| # | Line | Occurrence | Flags |
|---|---|---|---|
| HD-1 | 42-43 | Cover letter subject line quotes press release title verbatim: "...revenue rises 5.3% YoY to ₹775 crores" | DUPLICATE_MENTION |
| HD-2 | 74 | Press release headline: "Digitide returns to profitability in Q1 FY27; revenue rises 5.3% YoY to ₹775 Cr" | DUPLICATE_MENTION (same claim as HD-1) |
| HD-3 | 75 | Dateline parenthetical restates exchange codes "(BSE: 544413 \| NSE: DIGITIDE)" | DUPLICATE_MENTION (already disclosed A-4/A-5) |

## TABLE 13 — Boilerplate / Non-numeric Sections (5 rows)

| # | Line(s) | Section | Flags |
|---|---|---|---|
| BP-1 | 275-283 | "About Digitide Solutions Limited" company description | Qualitative only, no numeric KPIs |
| BP-2 | 287-291 | Investor/Analyst Contact — Rajesh Lachhani, Head of M&A and IR | Administrative |
| BP-3 | 293-295 | Apurva Pandey, Deputy Manager - M&A and IR | Administrative |
| BP-4 | 299-301 | Media Contact — Priya Philipose, AVP Marketing | Administrative |
| BP-5 | 305-311 | Disclaimer — standard forward-looking-statements safe-harbor language | Standard boilerplate, present as expected; no assurance/audit-status statement anywhere in the document — flag DATA_GAP: no limited-review/audit-status disclosure in this press release (unlike a Reg 33 filing) for A3 to check against the Reg 33 filing when reconciling |

---

## SUMMARY / DISCLOSURE UNITS NOT APPLICABLE TO THIS DOCTYPE (explicitly recorded, not silently dropped)

- Numbered notes: none present (0).
- Board Outcome letter agenda items (AR approval, AGM notice, record date, dividend, director appointments, auditor changes, scrutinizer, ESOP, capital-raising resolutions): not applicable — no Board Outcome letter is part of this extract.
- Annexures / director profiles: none present (0).
- Auditor report paragraphs (opinion type, EOM, Other Matters, Going Concern, UDIN, unaudited/management-furnished entities): not applicable — no auditor report attached to this press release.
- Consolidation entity list: not disclosed in this document, despite the CFO quote referring to "Consolidated revenue" — flag DATA_GAP for A3 to cross-check against the Reg 33 filing's entity list.
- Zero/nil/dash-valued standing line items: none found — every cell in all three tables (Segment, Revenue/EBITDA/PAT block, Geographical) carries a populated numeric or descriptive value across all three periods shown. `zero_standing: 0`.

## TOTAL ROW COUNT
10 + 7 + 16 + 24 + 25 + 24 + 5 + 12 + 2 + 15 + 3 + 5 = **148 enumerated disclosure units**.
