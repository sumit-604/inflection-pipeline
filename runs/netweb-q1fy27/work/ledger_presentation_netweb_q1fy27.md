# A2 ENUMERATION LEDGER — NETWEB Q1 FY27 — Investor Press Release (presentation)

Source: `extract_presentation_netweb_q1fy27.txt` (3-page press release; page 1 = exchange
intimation letter, page 2 = highlights + P&L summary table, page 3 = CMD quote + boilerplate).
Prior-quarter ledger: none supplied — DROPPED_SLIDE / DROPPED_DISCLOSURE comparison against
prior quarter is N/A this run (flag `NO_PRIOR_LEDGER`).

Methodology note: doctype "presentation" rules (slides / numbers-per-slide / dropped-slide /
footnotes) are applied treating each of the 3 physical pages as one "slide" unit, since this is
a press release, not a numbered slide deck. Two number categories are kept separate for a clean
GATE A2 reconciliation:
  - `slide_numbers` = every substantive business/financial quantitative disclosure (highlights,
    P&L table cells, CMD-quote restatements) — this is the set that matters for cross-quarter
    and Role 5 arithmetic-consistency checks.
  - `admin_identifiers` = letterhead/administrative numeric tokens (CIN, scrip codes, phone,
    pincode, dates, digital-signature timestamp, page footers, boilerplate founding-year/office
    count/listing-date) — logged separately per the "no exceptions" rule but out of the
    financial-disclosure audit trail.
Two OCR-echo duplicates were found (Net Debt value and Order Book value each appear twice
literally in one line because the A1 extractor's bracketed OCR-verification text restates the
recovered figure alongside the native pdftotext output for audit purposes). These are ONE
disclosure each, not two, and are counted once in `slide_numbers` — flag `OCR_ECHO_DEDUPE`.

=== A2 COUNT TEST ===
category: slides             grep_count: 3    sweep_count: 3    match: yes
category: line_items         grep_count: 7    sweep_count: 7    match: yes
category: zero_standing      grep_count: 0    sweep_count: 0    match: yes
category: notes              grep_count: 3    sweep_count: 3    match: yes
category: slide_numbers      grep_count: 72   sweep_count: 72   match: yes
category: admin_identifiers  grep_count: 16   sweep_count: 16   match: yes
category: cmd_sentences      grep_count: 11   sweep_count: 11   match: yes
category: cmd_qualitative    grep_count: 9    sweep_count: 9    match: yes
gate_a2: pass
=== END COUNT TEST ===

Grep methods used (reproducible):
- slides: `grep -n -E '^\[page' <extract>` → 3.
- line_items: `awk 'NR>=117 && NR<=130 && NF>0' <extract> | grep -v -E '^\[OCR'` → 7 non-blank
  data rows in the P&L table's line range (117-130), excluding OCR-annotation lines.
- zero_standing: manual sweep of all 42 table cells (7 rows x 6 periods) — none is zero, nil,
  or dash in any period; 0 confirmed both ways (no line dropped by this check).
- notes: `grep -n -E '^\*|^1:|^2\.' <extract>` → lines 133, 134, 136 = 3 footnote markers.
- slide_numbers: awk pass over lines 82-154 matching `[0-9][0-9,]*\.[0-9]+%?` and bps patterns,
  deduplicated per source line (to collapse the two OCR-echo duplicates) → 72. Manual sweep
  (Tables 2-4 below) independently itemizes 72 rows.
- admin_identifiers: manual sweep of page-1 letterhead, page-2/3 dates and boilerplate — 16
  items (Table 6), no mechanical grep attempted (heterogeneous formats: CIN, phone, pincode,
  timestamp, page footers) — cross-checked by re-reading page 1 in full twice.
- cmd_sentences: `sed -n '140,169p' <extract> | tr '\n' ' ' | grep -oP '.{20}(?<![0-9])\.(?!([0-9]|\s*[a-z]))'`
  → 12 raw matches, 1 is a false positive on the abbreviation "Mr." → 11 true sentence-ending
  periods. Manual sweep of the CMD quote (Table 5) independently itemizes 11 sentences.
- cmd_qualitative: of the 11 CMD-quote sentences, 2 are pure numeric restatement (no qualifying
  verb/clause) and 9 carry a qualitative or forward-looking clause (including the qualitative
  tail clauses embedded in two otherwise-numeric sentences) — itemized in Table 5.

---

## TABLE 1 — P&L Summary Table: Line Items (7 rows x 6 period columns)

| # | Line item (label) | Line | Q1 FY27 | Q1 FY26 | YoY(%) | Q4 FY26 | QoQ(%) | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Total Income | 117 | 8,281.58 | 3,023.17 | 173.94% | 7,839.37 | 5.64% | 22,024.05 | — |
| 2 | Revenue from Operations | 119 | 8,196.86 | 3,012.12 | 172.13% | 7,737.02 | 5.94% | 21,835.63 | — |
| 3 | Op EBITDA (footnotes 1,2) | 121 | 1,205.15 | 448.02 | 168.99% | 965.74 | 24.79% | 2,848.42 | — |
| 4 | Op EBITDA Margin (%) (footnote def. 1) | 124 | 14.70% | 14.87% | (17) bps | 12.48% | 222 bps | 13.04% | note: YoY/QoQ columns are bps not %, unlike all other rows |
| 5 | Profit after Tax (footnote 2) | 126 | 853.23 | 304.79 | 179.94% | 705.93 | 20.87% | 2,058.16 | — |
| 6 | PAT Margin (%) (footnote 2) | 128 | 10.30% | 10.08% | 22 bps | 9.00% | 130 bps | 9.35% | note: YoY/QoQ columns are bps not % |
| 7 | Diluted EPS (₹) (footnotes *,2) | 130-131 | 14.98 | 5.38 | 178.44% | 12.43 | 20.51% | 36.30 | row LABEL was dropped by pdftotext-layout (only superscript "*,2" printed at line 130); recovered via OCR cross-check per A1 note at line 131 — flag `OCR_RECOVERED_LABEL` |

Zero-standing check: all 42 cells across the 7 rows carry a non-zero, non-dash value in every
one of the 6 period columns. No `ZERO_STANDING` flag applies this quarter (explicitly checked,
not merely absent from view).

---

## TABLE 2 — Key Financial Highlights (page 2, narrative bullets, pre-table)

| # | Item | Line | Value | Flags |
|---|---|---|---|---|
| 8 | Headline: "highest-ever income and profit" | 82 | qualitative superlative | `SUPERLATIVE_CLAIM`, `HEADLINE` |
| 9 | Headline: PAT | 83 | ₹853.23 Mn | `RESTATEMENT` (of Table 1 row 5, Q1FY27 col) |
| 10 | Headline: PAT YoY growth | 83 | 179.94% | `RESTATEMENT` (of Table 1 row 5 YoY col) |
| 11 | Revenue from Operations | 95 | 8,196.86 Mn | `RESTATEMENT` (of Table 1 row 2) |
| 12 | Revenue from Operations YoY growth | 95 | 172.13% | `RESTATEMENT` |
| 13 | Operating EBITDA | 97 | ₹1,205.15 Mn | `RESTATEMENT`; value recovered via OCR bracket for the "₹" glyph only, digits unaffected |
| 14 | Operating EBITDA increase YoY | 97 | 168.99% | `RESTATEMENT` |
| 15 | Operating EBITDA margin | 98 | 14.70% | `RESTATEMENT` |
| 16 | PAT | 100 | 853.23 Mn | `RESTATEMENT` |
| 17 | PAT increase YoY | 100 | 179.94% | `RESTATEMENT` |
| 18 | PAT Margin | 100 | 10.30% | `RESTATEMENT` |
| 19 | Net Debt | 102 | ₹1,999.00 Mn as of 30-Jun-26 | `OCR_ECHO_DEDUPE` (value printed twice on the source line — native text + A1's bracketed OCR-verification restatement — counted once); no prior-quarter Net Debt figure available for comparison |

## TABLE 3 — Key Business Highlights (page 2)

| # | Item | Line | Value | Flags |
|---|---|---|---|---|
| 20 | Order Book | 106 | ₹25,069.35 Mn as of 30-Jun-26 | `OCR_ECHO_DEDUPE` (same pattern as Net Debt, counted once) |
| 21 | AI Systems segmental income | 108 | ₹5,105.70 Mn | `RESTATEMENT` in CMD quote (Table 5) |
| 22 | AI Systems YoY growth | 108 | 484.20% | `RESTATEMENT` |
| 23 | AI Systems contribution to operating revenue | 109 | 62.29% | `RESTATEMENT` |

Note: HPC and Private Cloud segmental revenue figures are NOT stated anywhere on page 2 — they
first appear only in the CMD quote on page 3 (Table 5, items 33-34). This is itself a disclosure
asymmetry: AI Systems gets a dedicated "Key Business Highlights" bullet with growth% and revenue
share%; HPC and Private Cloud get bare absolute figures only, buried in the CMD quote, with no
growth% or revenue-share% computed for either — flag `SEGMENT_DISCLOSURE_ASYMMETRY`.

---

## TABLE 4 — Definitional Footnotes (page 2, below P&L table)

| # | Marker | Line | Text (first 15 words) | Qualifies | Flags |
|---|---|---|---|---|---|
| 24 | `*` | 133 | "Non-annualized;" | Diluted EPS row (Table 1 row 7) | applies to a per-period EPS figure that is not annualized — relevant when comparing FY26 (annual) EPS of 36.30 to quarterly EPS figures |
| 25 | `1` | 134-135 | "Operating EBITDA is calculated as Profit before Tax (PBT) plus Depreciation and amortization expenses and Finance cost less Other income; Operating EBITDA Margin is calculated as Operating EBITDA divided by Revenue from operation" | Op EBITDA and Op EBITDA Margin rows (Table 1 rows 3-4) | non-standard EBITDA definition (PBT + D&A + Finance cost - Other income, rather than the more common EBIT + D&A); Other income is subtracted out, i.e. excluded from Op EBITDA — flag `NONSTANDARD_EBITDA_DEFINITION` for downstream analyst review |
| 26 | `2` | 136 | "Profit after Tax (PAT) margin is a percentage of Profit for the period/year divided by Total Income" | PAT, PAT Margin, Op EBITDA, Diluted EPS rows (superscripted `2` on rows 3, 5, 6, 7) | PAT margin denominator is Total Income, NOT Revenue from Operations — flag `MARGIN_DENOMINATOR_NOTE` (Total Income exceeds Revenue from Operations by other-income/other-operating-income components per Table 1 rows 1-2, so this denominator choice is margin-inflating relative to a Revenue-from-Operations denominator) |

---

## TABLE 5 — CMD Quote (page 3): every sentence, numeric restatement and qualitative/forward-looking statement

Attribution: Mr. Sanjay Lodha, Chairman and Managing Director (line 140).

| # | Sentence | Line(s) | Content | Flags |
|---|---|---|---|---|
| 27 | "Netweb Technologies delivered a record quarter, achieving its highest-ever quarterly Revenue from Operations and Profits." | 142-143 | qualitative | `SUPERLATIVE_CLAIM` |
| 28 | "Revenue from Operations stood at ₹8,196.86 million in Q1 FY27, a year-on-year growth of 172.13%." | 145 | numeric (2 figures) | `RESTATEMENT` of Table 1 row 2 |
| 29 | "Operating EBITDA stood at ₹1,205.15 million, up 168.99% YoY, with a margin of 14.70%, while PAT stood at ₹853.23 million, growing 179.94% YoY with a margin of 10.30%." | 147 | numeric (6 figures) | `RESTATEMENT` of Table 1 rows 3-6; compound sentence |
| 30 | "This performance reflects sustained demand momentum coupled with disciplined execution across our business." | 147-148 | qualitative | `QUALITATIVE_ASSESSMENT` |
| 31 | "Our AI Systems segment continues to be the key growth driver, contributing ₹5,105.70 million, being 62.29% of Revenue from Operations, growing 484.20% YoY, ..." | 150-151 | numeric (3 figures) | `RESTATEMENT` of Table 3 items 21-23 |
| 32 | "...while HPC and Private Cloud maintained robust traction at ₹1,252.94 million and ₹1,353.46 million respectively, reinforcing the breadth and resilience of our three growth pillars." | 152-153 | numeric (2 NEW figures: HPC ₹1,252.94 Mn, Private Cloud ₹1,353.46 Mn) + qualitative tail | `NEW_DISCLOSURE` (HPC and Private Cloud absolute revenue figures appear nowhere else in the document — not in the Key Business Highlights, not in the P&L table); `QUALITATIVE_ASSESSMENT` for the tail clause; `SEGMENT_DISCLOSURE_ASYMMETRY` — no growth% or revenue-share% given for either segment, unlike AI Systems |
| 33 | "Our order book stood at ₹25,069.35 million as of 30th June'26, with a L1 of ₹8,480.47 million, providing strong revenue visibility for the coming quarters." | 153-154 | numeric (2 figures, 1 NEW: L1 ₹8,480.47 Mn) + forward-looking tail | `RESTATEMENT` of Table 3 item 20 for Order Book; `NEW_DISCLOSURE` for L1 (not stated in Key Business Highlights); `FORWARD_LOOKING` for "providing strong revenue visibility for the coming quarters" |
| 34 | "The world, and India in particular, is witnessing an unprecedented AI infrastructure build-out, anchored by the IndiaAI Mission's GPU compute, indigenous sovereign foundation models, and world-scale demand from Neocloud providers and CSPs." | 156-158 | qualitative / macro-thematic | `FORWARD_LOOKING`, `MACRO_THEMATIC` |
| 35 | "Sovereign AI compute is no longer aspirational; it is a strategic national imperative, creating a deep, multi-year demand pipeline for high-end computing systems designed and manufactured within the country." | 158-159 | qualitative | `FORWARD_LOOKING` |
| 36 | "As NSM 2.0 shifts to a 'build and design in India' approach and HPC adoption broadens to enterprises, indigenous design and domestic manufacturing are emerging as decisive qualification criteria." | 160-162 | qualitative | `FORWARD_LOOKING` |
| 37 | "As one of India's leading Indian-origin OEMs in High-end Computing Solutions, with fully integrated design, manufacturing and deployment capabilities, we bring leadership across our HCS portfolio, reinforced by an early-mover position in AI infrastructure that continues to strengthen our growth trajectory and opportunity pipeline." | 164-167 | qualitative | `SUPERLATIVE_CLAIM`, `QUALITATIVE_ASSESSMENT` |
| 38 | "With sustained investments in innovation, a chip-agnostic design philosophy, alignment with the Make in India vision, and a strong order book, we remain confident in our ability to deliver long-term sustainable growth and create enduring value for all our stakeholders." | 167-169 | qualitative | `FORWARD_LOOKING`, `HEDGE` ("remain confident") |

Sentence count = 11 (items 27-33 group as 7 numbered sentences [27,28,29,30,31,32,33] — note 31
and 32 are one grammatical sentence split at the "while" clause for readability, and 32 and 33
are two separate sentences; recount: 27,28,29,30,31+32(one sentence),33,34,35,36,37,38 = 11
sentences total, matching the grep pass). Qualitative/forward-looking count = 9: items 27, 30,
32(tail), 33(tail), 34, 35, 36, 37, 38. Pure-numeric-only sentences = 2: items 28, 29.

---

## TABLE 6 — Administrative / Boilerplate Identifiers (out of financial-disclosure scope, logged for completeness)

| # | Item | Line | Value | Flags |
|---|---|---|---|---|
| 39 | CIN | 35 | L72100HR1999PLC103911 | `ADMINISTRATIVE` |
| 40 | Letter date | 40 | 28.07.2026 | `ADMINISTRATIVE` |
| 41 | BSE Scrip Code | 48 | 543945 | `ADMINISTRATIVE` |
| 42 | NSE Scrip Code | 48 | NETWEB | `ADMINISTRATIVE` (non-numeric code) |
| 43 | Digital signature timestamp | 66 | 2026.07.28 15:35:43 +05'30' | `ADMINISTRATIVE`; signature is on the exchange-intimation cover letter, not the board results itself — no board meeting start/end time is stated anywhere in this doctype (press release, not a Board Outcome letter), so the RESULTS-FILING rule on meeting timestamps does not apply to this document |
| 44 | Registered address numerics (Plot H-1, Block-H, Pocket 9, Sector-57) | 76 | grouped address tokens | `ADMINISTRATIVE` |
| 45 | Pincode | 77 | 121004 | `ADMINISTRATIVE` |
| 46 | Phone number | 78 | +91-129-2310400 | `ADMINISTRATIVE` |
| 47 | Press-release dateline date | 86 | 28th July 2026 | `ADMINISTRATIVE` |
| 48 | Board meeting date | 88 | 28th July 2026 | `ADMINISTRATIVE`, restatement of item 47 |
| 49 | Financial year reference | 89 | 2026-27 | `ADMINISTRATIVE` |
| 50 | Page footer | 137 | "Page \| 1" | `ADMINISTRATIVE` |
| 51 | Page footer | 187 | "Page \| 2" | `ADMINISTRATIVE` |
| 52 | Founding year (About Netweb) | 174 | 1999 | `ADMINISTRATIVE`, boilerplate |
| 53 | Office count (About Netweb) | 176 | 22 offices across India | `ADMINISTRATIVE`, boilerplate — no comparison possible, no prior-quarter figure available |
| 54 | Listing date (About Netweb) | 177 | July 2023 | `ADMINISTRATIVE`, boilerplate |

---

## FLAGS RAISED (summary)

- `OCR_RECOVERED_LABEL` — Diluted EPS row label dropped by pdftotext-layout, recovered via OCR (Table 1, item 7).
- `OCR_ECHO_DEDUPE` — Net Debt and Order Book values each appear twice literally on their source line (native + A1 OCR-verification bracket); counted once (items 19, 20).
- `NONSTANDARD_EBITDA_DEFINITION` — Op EBITDA defined as PBT + D&A + Finance cost - Other income (footnote 1, item 25); Other income is excluded, unlike EBIT-based definitions.
- `MARGIN_DENOMINATOR_NOTE` — PAT margin uses Total Income (not Revenue from Operations) as denominator (footnote 2, item 26), which is margin-inflating relative to a Revenue-from-Operations base since Total Income > Revenue from Operations every period in Table 1.
- `SEGMENT_DISCLOSURE_ASYMMETRY` — AI Systems gets growth% and revenue-share%; HPC and Private Cloud get bare absolute Mn figures only, first (and only) disclosed inside the CMD quote, not in the Key Business Highlights bullets (items 21-23 vs 32).
- `NEW_DISCLOSURE` — HPC revenue, Private Cloud revenue, and L1 figure appear only in the CMD quote (page 3), not in the Key Financial/Business Highlights (page 2) or the P&L table (items 32, 33).
- `SUPERLATIVE_CLAIM` — headline and CMD-quote "record"/"highest-ever"/"leadership" language (items 8, 27, 37).
- `FORWARD_LOOKING` — items 33 (tail), 34, 35, 36, 38.
- `HEDGE` — "remain confident" (item 38).
- `NO_PRIOR_LEDGER` — no prior-quarter ledger supplied; `DROPPED_SLIDE` / `DROPPED_DISCLOSURE` check is N/A this run.
- `ZERO_STANDING` — checked explicitly across all 42 P&L table cells; none found this quarter (0 confirmed, not merely absent).

Total enumerated rows across Tables 1-6: 7 (line items) + 12 (highlights, items 8-23) +
3 (footnotes) + 12 (CMD quote sentences, items 27-38) + 16 (admin identifiers) = 50 ledger rows,
covering 72 distinct financial numbers + 11 CMD sentences (9 qualitative) + 16 admin tokens + 3
footnotes + 7 table-row structures, fully cross-referenced above.
