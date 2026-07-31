# A2 ENUMERATION LEDGER — Ram Ratna Wires Ltd (RAMRAT) — Q1 FY27 — pressrelease

Source: `/home/user/inflection-pipeline/runs/ramrat-q1fy27/work/extract_pressrelease_ramrat_q1fy27.txt` (147 lines, 3 pages, 100% coverage, no OCR pages)

Doctype note: this is a prose investor press release / exchange cover letter, not one of the
three canonical doctypes (results filing / concall transcript / investor presentation).
Enumerated under PRESENTATION-CLASS semantics per task instructions: financial summary table,
quantified prose claims, MD-quote forward/qualitative phrases, and structural/narrative units.

```
=== A2 COUNT TEST ===
category: summary_table_line_items   grep_count: 5    sweep_count: 5    match: yes
category: quantified_claims          grep_count: 11   sweep_count: 11   match: yes
category: mgmt_forward_phrases       grep_count: 18   sweep_count: 18   match: yes
category: structural_narrative_units grep_count: 16   sweep_count: 16   match: yes
TOTAL                                grep_count: 50   sweep_count: 50   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used for the count test (all run against the extract file above):
- Summary table: `grep -n -E "^(Revenue from Operations|Operating EBITDA|EBITDA Margin|Profit After Tax|PAT Margin)"` → 5 matches (lines 80-84).
- Quantified claims: `grep -noE "Up 89%|Up 109%|Up 121%|₹ 1,853 Cr|₹ 90 Cr|₹ 35 Cr|\+89% YoY|\+109% YoY|\+121% YoY|rising to 26%|Founded in 1992"` → 11 matches.
- Forward phrases: 18 distinct single-line unique substrings (one per phrase, see Table 3), each verified to appear exactly once via `grep -n -F "<substring>"`.
- Structural units: 16 distinct unique heading/keyword substrings (see Table 4), each verified to appear exactly once via `grep -n -E "<substring>"`.
- Manual sweep: full-text read of all 147 lines, paragraph by paragraph, cross-checked against each grep list line-by-line. No additional items found; no grep hit lacked a manual counterpart.

---

## TABLE 1 — SUMMARY TABLE LINE ITEMS
"Key Financial Highlights" table, lines 79-84. Every line item enumerated with all period
values. No zero/nil/dash values present in this table (all five metrics populated for all
four periods shown); ZERO_STANDING flag not triggered anywhere in this document.

| # | Line | Line item | Q1 FY27 | Q1 FY26 | Y-o-Y | Q4 FY26 | FY26 | Flags |
|---|------|-----------|---------|---------|-------|---------|------|-------|
| 1 | 80 | Revenue from Operations (₹ Cr) | 1,853.3 | 982.5 | +88.6% | 1,752.9 | 5,176.6 | |
| 2 | 81 | Operating EBITDA (₹ Cr) | 89.6 | 42.9 | +109.0% | 93.2 | 263.6 | |
| 3 | 82 | EBITDA Margin (%) | 4.8% | 4.4% | (not stated in table row) | 5.3% | 5.1% | NOTE: no Y-o-Y bps/pp column value shown for this row despite column header present |
| 4 | 83 | Profit After Tax (₹ Cr) | 35.2 | 15.9 | +120.8% | 39.2 | 108.6 | |
| 5 | 84 | PAT Margin (%) | 1.9% | 1.6% | (not stated in table row) | 2.2% | 2.1% | NOTE: no Y-o-Y bps/pp column value shown for this row despite column header present |

Table header row (line 79): `Particulars (₹ Cr.)  Q1 FY27  Q1 FY26  Y-o-Y  Q4 FY26  FY26` — five period columns confirmed; margin rows (2 of 5) leave the Y-o-Y column blank in the source, a legitimate gap (delta of a ratio not stated) rather than a missing-value error, but noted for A3/A4 to check if bps change is derivable and whether its omission is itself a signal.

---

## TABLE 2 — QUANTIFIED CLAIMS (numbers/percentages stated in prose, outside the summary table)

| # | Line | Verbatim fragment | Claim | Flags |
|---|------|--------------------|-------|-------|
| 1 | 61 | "Revenue Up 89%" | Headline YoY revenue growth (subtitle) | |
| 2 | 61 | "EBITDA Up 109%" | Headline YoY EBITDA growth (subtitle) | |
| 3 | 61 | "PAT Up 121%" | Headline YoY PAT growth (subtitle) | |
| 4 | 73 | "₹ 1,853 Cr" | Revenue snapshot box value | |
| 5 | 73 | "₹ 90 Cr" | EBITDA snapshot box value (rounds 89.6 to 90) | ROUNDING vs Table 1 row 2 (89.6) |
| 6 | 73 | "₹ 35 Cr" | PAT snapshot box value (rounds 35.2 to 35) | ROUNDING vs Table 1 row 4 (35.2) |
| 7 | 74 | "+89% YoY" | Revenue growth restated under snapshot box | matches subtitle 89% vs table exact 88.6% — ROUNDING |
| 8 | 74 | "+109% YoY" | EBITDA growth restated under snapshot box | matches table exact 109.0% |
| 9 | 74 | "+121% YoY" | PAT growth restated under snapshot box | vs table exact 120.8% — ROUNDING |
| 10 | 94 | "contribution to revenue rising to 26%" | Copper Tubes segment now 26% of consolidated revenue | UNVERIFIABLE_STANDALONE — no segment table in this doc to cross-check; no prior-quarter % given for comparison ("rising to" implies a prior lower figure that is not stated) |
| 11 | 113 | "Founded in 1992" | Company incorporation/founding year | |

---

## TABLE 3 — MANAGEMENT-QUOTE FORWARD/QUALITATIVE PHRASES
MD quote: Shri Mahendrakumar Kabra, Managing Director, lines 88-104 (attribution at line 86).
Every forward-looking or qualitative (non-quantified) claim in the quote enumerated below in
reading order.

| # | Line | Verbatim phrase | Type | Flags |
|---|------|------------------|------|-------|
| 1 | 88 | "pleased to begin FY27 with a strong set of results" | Qualitative self-assessment | |
| 2 | 88-89 | "delivering healthy growth in revenue and profitability" | Qualitative summary claim | |
| 3 | 89 | "robust demand across key end-user industries" | Qualitative demand claim | UNQUANTIFIED — no named industries or split given |
| 4 | 89-90 | "disciplined execution" | Qualitative claim | UNQUANTIFIED |
| 5 | 90-91 | "continued investments in expanding our business portfolio and manufacturing capabilities" | Forward/ongoing-investment claim | UNQUANTIFIED — no capex figure attached |
| 6 | 93 | "continued momentum in our Copper Tubes business" | Forward/trend claim | ties to quantified claim #10 (Table 2) |
| 7 | 94 | "success of our diversification strategy" | Qualitative strategic claim | |
| 8 | 95 | "continue to invest in capacity expansion" | Forward-commitment phrase | UNQUANTIFIED — no capex amount, no capacity unit, no timeline |
| 9 | 95-96 | "strengthen our presence through our subsidiary and joint venture" | Forward phrase | subsidiary/JV not named in this document |
| 10 | 96 | "expanding our reach across high-growth end-use industries" | Forward phrase | UNQUANTIFIED |
| 11 | 96-97 | "building a more balanced and resilient business" | Forward/qualitative claim | |
| 12 | 99 | "remain focused on driving sustainable growth through operational excellence" | Forward-commitment phrase | boilerplate-adjacent, UNQUANTIFIED |
| 13 | 100 | "disciplined capital allocation" | Forward-commitment phrase | UNQUANTIFIED — no allocation framework or split given |
| 14 | 100 | "continued improvement in working capital efficiency" | Forward-commitment phrase | UNQUANTIFIED — no working-capital day/cycle metric given anywhere in doc to test against |
| 15 | 100-102 | "Supported by India's long-term investments in power infrastructure, manufacturing, electrification and energy-efficient cooling solutions" | Macro-tailwind claim | external, not company-specific |
| 16 | 102 | "well positioned to capitalize on the opportunities ahead" | Forward/qualitative claim | boilerplate |
| 17 | 102-103 | "further strengthen our market position" | Forward phrase | UNQUANTIFIED |
| 18 | 103-104 | "committed to creating sustainable value for all our stakeholders" | Closing qualitative commitment | boilerplate |

---

## TABLE 4 — STRUCTURAL / NARRATIVE UNITS

| # | Line(s) | Unit | Detail | Flags |
|---|---------|------|--------|-------|
| 1 | 18-24 | Covering letter addressee block | Dual addressee: BSE Limited (Corporate Relationship Dept.) and NSE; Script Code 522281, Symbol RAMRAT | |
| 2 | 27-29 | Subject line | "Press Release on the unaudited Financial Results of the Company under Regulation 30 of the SEBI (LODR) Regulations, 2015" — confirms results are UNAUDITED | |
| 3 | 31-40 | Letter body | Notes enclosure of press release for quarter ended 30-Jun-2026; states release also hosted at www.rrshramik.com | |
| 4 | 42 | Valediction | "Yours faithfully," / "For Ram Ratna Wires Limited" | |
| 5 | 44-53 | Digital signature block | Signatory: Saurabh Gupta; Designation: Company Secretary & Compliance Officer; M. No.: F13652; digitally signed timestamp 2026.07.31 16:57:10 +05'30' | Signature timestamp (31-Jul-2026, 16:57 IST) is same calendar day as the stated release date (line 63, "31st July 2026") — no board-meeting timing data present in this doctype to cross-check against (no board outcome letter in this extract), so no SIGNATURE_BEFORE_MEETING flag can be tested here; A3/A4 should cross-check against the board outcome intimation if/when available |
| 6 | 55 | Enclosure note | "Encl: As Above" | |
| 7 | 57-61 | Press release masthead + headline + subtitle | "Ram Ratna Wires Limited / Investor Release"; headline "Ram Ratna Wires Reports Strong Q1 FY27 Performance"; subtitle "Revenue Up 89%, EBITDA Up 109%, PAT Up 121% YoY" | |
| 8 | 63-64 | Dateline | "Mumbai, 31st July 2026" — announces results for quarter ended 30th June 2026; describes company as "India's leading manufacturer of winding wires & strips and copper tubes" | Self-description "leading manufacturer" is an unverified superlative claim, not sourced |
| 9 | 66-75 | Financial Performance Snapshot infographic | Three-box layout: Revenue from Operations / EBITDA / Profit After Tax, each with ₹ Cr value and %YoY, labeled "(Y-o-Y) (Consolidated)" | basis explicitly stated as Consolidated |
| 10 | 77-85 | "Key Financial Highlights" table (heading + full table) | Heading at line 77; table body enumerated row-by-row in Table 1 above | |
| 11 | 86 | MD quote attribution | "Commenting on the Results, Shri Mahendrakumar Kabra, MD said, -" | Only one management voice quoted in entire release; no CFO or other officer quoted |
| 12 | 88-104 | MD quote body (full block) | Three-paragraph quote; individual phrases enumerated in Table 3 | |
| 13 | 112-117 | "About Ram Ratna Wires Ltd" section | Founded 1992 (quantified claim #11); describes RR Shramik brand, product range (copper/aluminum winding wires, copper tubes/pipes); notes venture into BLDC motors, hub motors, HVLS fans, wind tower fabrication "through its subsidiary and JV companies" (unnamed) | subsidiary/JV named nowhere in this document |
| 14 | 119-123, 129 | Company contact block | Name: Mr. Saurabh Gupta; Email: investorrelations.rrwl@rrglobal.com; CIN: L31300MH1992PLC067802; Website: https://www.rrshramik.com | |
| 15 | 119-124, 130 | Investor Relations (external agent) contact block | MUFG Intime India Pvt. Ltd.; Names: Ms. Prachi Ambre / Mr. Irfan Raeen; Emails: Prachi.ambre@in.mpms.mufg.com / irfan.raeen@in.mpms.mufg.com; "Meeting Request" link; Website: https://in.mpms.mufg.com/ | two IR contacts named jointly, no indication of which to use for what |
| 16 | 132-142 | Safe Harbor section | Standard forward-looking-statement disclaimer; lists risk categories (industry downtrend, political/economic environment, tax laws, litigation, labour relations, FX, technology, investment/business income, cash flow projections, interest, other costs); states no obligation to update | boilerplate, standard SEBI-adjacent disclaimer language |

---

## CROSS-DOCUMENT NOTES FOR A3/A4 (enumeration-stage observations only, not interpretation)
- No prior-quarter ledger available for this ticker (first quarterly run) — no DROPPED_SLIDE /
  ENTITY_CHANGE / REPEAT_QUESTION style diff possible this cycle.
- This document contains no numbered notes, no board-agenda items, no auditor-report
  paragraphs, no consolidation-entity list, and no concall turns/participants/questions — none
  of the RESULTS FILING or CONCALL categories in the base instruction file apply to this
  doctype; only the four PRESENTATION-CLASS tables above are populated, per task routing.
- Three instances of headline-vs-table rounding are flagged inline in Table 2 (rows 5, 6, 7,
  9): snapshot-box and subtitle percentages/₹Cr figures round the table's one-decimal figures
  (e.g., 89.6 → "90", 120.8% → "121%"). Not an error, but a reconciliation point for A3.
  Combined tag: ROUNDING (4 occurrences).
- The 26% copper-tubes revenue-mix claim (Table 2 row 10 / Table 3 row 6) has no prior-period
  comparator in this document, despite the word "rising" implying one — flagged
  UNVERIFIABLE_STANDALONE for A3/A4 to check against the investor presentation or prior filings
  if available.
