# A2 COMPLETENESS LEDGER — Presentation (Q1 FY27 Earnings Press Release)
Company: DEE Development Engineers Ltd (D-DEV / DEEDEV / BSE 544198)
Quarter: Q1 FY27 (quarter ended 30 June 2026)
Source: `runs/d-dev-q1fy27/work/extract_presentation_d-dev_q1fy27.txt` (DOC4_press_release.pdf, 4 pages, line_count 175)
Prior-quarter ledger: not supplied — DROPPED_SLIDE / prior-deck diff not applicable this run (flag: `NO_PRIOR_LEDGER`)

Unit boundary for this doctype = each page/section. Grep basis given per category; manual sweep performed independently line-by-line against the extract.

```
=== A2 COUNT TEST ===
category: sections_pages              grep_count: 4    sweep_count: 4    match: yes
category: headline_financial_metrics   grep_count: 6    sweep_count: 6    match: yes
category: strapline_highlights         grep_count: 6    sweep_count: 6    match: yes
category: operational_bullets          grep_count: 6    sweep_count: 6    match: yes
category: management_quote_claims      grep_count: 19   sweep_count: 19   match: yes
category: forward_looking_statements   grep_count: 9    sweep_count: 9    match: yes
category: footnotes_disclaimers        grep_count: 0    sweep_count: 0    match: yes
category: zero_standing_items          grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep basis used for each row:
- sections_pages: `grep -n "^\[page" <extract>` → 4 hits (lines 15, 56, 114, 154).
- headline_financial_metrics: manual delimit of the Financial Summary table body (lines 74–79), `sed -n '74,79p'` → 6 non-blank rows.
- strapline_highlights: manual delimit of the page-2 callout block above the dateline (lines 59–66) → 6 distinct claim lines (one spans two physical lines: 65–66).
- operational_bullets: `grep -cE "^    •" <extract>` → 6 hits (lines 82, 84, 87, 89, 91, 94).
- management_quote_claims: programmatic sentence split of the CMD quote block (lines 104–147) on sentence-terminating periods, with decimal-number periods (e.g. "₹3.50", "₹5.224") protected from false splits, and the mid-quote page-break artifact ("Page | 2" / "[page 3]" injected by the extractor between pages) discarded as noise, not a sentence → 19 sentences. Manual re-read of the same block confirms 19 distinct claims.
- forward_looking_statements: `grep -n -iE "expect|ahead|coming quarter|over time|ramp-up|ramp up|going forward|outlook"` → raw hits on lines 66, 90, 93, 109, 115, 120, 121, 129, 139, 140, 146 (11 lines); merged where two matched lines are one wrapped sentence (120–121, 139–140) → 9 distinct forward-looking statements. Manual sweep of the full document for future-tense/expectation language confirms 9.
- footnotes_disclaimers: `grep -n -E "\*|Note:|†|\^" <extract>` → 0 hits; manual sweep of all 4 pages confirms no footnote markers, asterisks, or fine-print disclaimers anywhere in the document.
- zero_standing_items: manual review of the Financial Summary table (only table in the document) — all 6 rows carry non-zero, non-dash values in both periods; no nil/dash standing line item present.

---

## Table 1 — Sections / Pages (unit = page)

| # | Page | Line range | Content summary | Flags |
|---|------|-----------|------------------|-------|
| 1 | Page 1 | 15–54 | Regulatory cover letter to BSE/NSE under Reg 30 SEBI LODR, transmitting the Press Release on unaudited Q1 FY27 results; digital signature block (Ranjan Kumar Sarangi, Company Secretary & Compliance Officer, Membership No. F8604; signed 2026.08.04 14:29:13 +05'30') | see Table 6 (signature block) |
| 2 | Page 2 | 56–113 | Press-release title, strapline/callout highlights, dateline, Financial Summary table, "Key Financial & Operational Highlights" bullet list, opening of CMD quote | — |
| 3 | Page 3 | 114–153 | Continuation and close of CMD quote (Mr. Krishan Lalit Bansal, Chairman & Managing Director) | — |
| 4 | Page 4 | 154–189 | "About DEE Development Engineers Limited" boilerplate description; company and Investor Relations (Adfactors PR) contact details; registered office / works address, CIN, GST registration | — |

## Table 2 — Headline Financial Metrics (Financial Summary table, page 2, lines 70–79)

Period columns present for every metric: **Q1 FY27**, **Q1 FY26**, **YoY%**. All three columns populated for all 6 rows — no metric has a missing period column.

| # | Line | Metric | Q1 FY27 | Q1 FY26 | YoY | Flags |
|---|------|--------|---------|---------|-----|-------|
| 1 | 74 | Revenue from Operations | 294.5 | 223.8 | 31.6% | — |
| 2 | 75 | Operating EBITDA | 49.7 | 35.9 | 38.7% | — |
| 3 | 76 | Operating EBITDA Margin | 16.9% | 16.0% | 86 bps | — |
| 4 | 77 | PAT | 16.1 | 13.1 | 22.4% | — |
| 5 | 78 | PAT Margin | 5.5% | 5.8% | (41) bps | — |
| 6 | 79 | Diluted EPS | 2.32 | 1.90 | 22.1 | `FORMAT_ANOMALY` — YoY column value "22.1" printed without a "%" suffix, unlike every other row's YoY value (all others carry "%" or "bps"); arithmetically consistent with 22.1% ((2.32−1.90)/1.90), so likely a source typo/missing glyph rather than a different unit — flagged for A3, not resolved here |

Cross-reference note (not a table row, observational only): the page-2 strapline (Table 3, row 2) rounds Revenue to "₹294 Cr" and Operating EBITDA to "₹50 Cr" against the table's precise 294.5 and 49.7 — ordinary rounding, not a discrepancy in the underlying figures.

## Table 3 — Page 2 Strapline / Callout Highlights (lines 57–66, above the dateline, distinct from the bulleted "Key Financial & Operational Highlights" list in Table 4)

| # | Line(s) | Claim | Flags |
|---|---------|-------|-------|
| 1 | 59 | "Dee Development Engineers delivers strong performance across all key parameters, aided by healthy execution" (banner line) | — |
| 2 | 60 | Q1 FY27 Revenue stood at ₹294 Cr, YoY growth of 31.6% | `REPEATED_CLAIM` (restates Table 2 row 1) |
| 3 | 61 | Q1 FY27 Operating EBITDA rose to ₹50 Cr, up 38.7% YoY | `REPEATED_CLAIM` (restates Table 2 row 2) |
| 4 | 62 | Q1 FY27 PAT grew to ₹16 Cr, up 22.4% YoY | `REPEATED_CLAIM` (restates Table 2 row 4) |
| 5 | 63 | Closing Order Book stands at ₹2,428 crore as on 30 June 2026 | — (YoY% for order book not given here; supplied only in Table 4 row 3) |
| 6 | 65–66 | Continued focus on deleveraging: ~₹225 cr debt reduction via preferential-issue proceeds to substantially lower finance costs "ahead" | `FWD_LOOKING` (also Table 5 row 1) |

## Table 4 — Operational Highlight Bullets ("Key Financial & Operational Highlights", page 2, lines 81–99)

| # | Line(s) | Bullet | Flags |
|---|---------|--------|-------|
| 1 | 82–83 | Revenue grew 31.6% YoY to ₹294 Cr, driven by Piping & Fittings segment execution momentum, supported by strong supplies to the Power sector | `REPEATED_CLAIM` (restates Table 3 row 2 with added segment/sector attribution) |
| 2 | 84–86 | Record Operating EBITDA of ₹50 Cr, up 38.7% YoY, margin 16.9%, supported by higher Power-sector execution in core business plus improved tariffs and biomass pellet operations in non-core business | `REPEATED_CLAIM` (restates Table 3 row 3 with added driver detail) |
| 3 | 87–88 | Closing Order Book ₹2,428 Cr as on 30 June 2026, up 92.5% YoY; additionally L1 position stood at ₹12 Cr | adds YoY% and L1 figure not present in Table 3 row 5 |
| 4 | 89–90 | Biomass pellet facility became operational midway through Q1 FY27, partially offsetting non-core business losses; full benefit expected from Q2 FY27 | `FWD_LOOKING` (also Table 5 row 2); `REPEATED_CLAIM` (restated in quote, Table 5 row 8 / Table 6 quote claims 15–16) |
| 5 | 91–93 | ~₹25 crore of revenue recognition deferred during the quarter due to temporary geopolitical disruption in the Middle East and customer-related issues; dispatches have since normalized, deferred revenue expected to be recognized in the coming quarter | `FWD_LOOKING` (also Table 5 row 3); `REPEATED_CLAIM` (near-verbatim restated in CMD quote claims 2–3, Table 6) |
| 6 | 94–99 | Board approved seeking shareholder approval under Section 62(3) Companies Act 2013 as an enabling provision aligned to existing working-capital sanction-letter terms; not a new borrowing/facility; conversion right exercisable by lenders only on an event of default | governance / enabling-resolution disclosure — distinct from Table 4's other financial-performance bullets; no prior-quarter comparison available to assess whether this is a new disclosure |

## Table 5 — Forward-Looking Statements (whole document, 9 distinct statements)

| # | Line(s) | Location | Statement | Cross-ref |
|---|---------|----------|-----------|-----------|
| 1 | 65–66 | Page 2 strapline | ~₹225 cr debt reduction to "substantially lower finance costs ahead" | Table 3 row 6 |
| 2 | 89–90 | Bullet 4 | Biomass pellet full benefit "expected from Q2 FY27" | Table 4 row 4 |
| 3 | 91–93 | Bullet 5 | Deferred ~₹25 cr revenue "expected to be recognized in the coming quarter" | Table 4 row 5 |
| 4 | 106–109 | CMD quote | Same deferred-revenue recognition expectation, restated in the quote | Table 6 claim 3; `REPEATED_CLAIM` of row 3 above |
| 5 | 115–118 | CMD quote | "Long-term outlook... remains encouraging," India capex cycle "reinforcing our confidence in the sector's growth prospects" | Table 6 claim 5–6 |
| 6 | 119–121 | CMD quote | Seamless pipe facility "is progressing through its ramp-up phase and is expected to contribute meaningfully as utilization improves... over time" | Table 6 claim 8 |
| 7 | 128–131 | CMD quote | Preferential-issue proceeds "expected to materially reduce leverage and finance costs, improve return ratios, and provide... greater financial flexibility" | Table 6 claim 12 |
| 8 | 138–140 | CMD quote | "We expect the pellet business to provide a meaningful contribution to revenue, profitability, and cash flows over the coming quarters" | Table 6 claim 16 |
| 9 | 145–147 | CMD quote | "We expect operating leverage, profitability, and cash flows to strengthen further, supporting a gradual reduction in debt" | Table 6 claim 19 |

## Table 6 — Management-Quote Claims (Mr. Krishan Lalit Bansal, CMD, lines 101–147; unit = distinct sentence/claim within the quote)

| # | Line(s) | Claim (paraphrase, source retains exact wording) | Flags |
|---|---------|----|-------|
| 1 | 104–106 | Delivered healthy operating and financial performance; growth in revenue, Operating EBITDA, and PAT, driven by strong core-business execution, particularly Power sector | — |
| 2 | 106–108 | ~₹25 crore revenue recognition deferred due to Middle East geopolitical disruption and customer-related issues, despite materials being fully manufactured, packed, and ready for dispatch | `REPEATED_CLAIM` (Table 4 row 5, Table 5 row 3) |
| 3 | 108–109 | Dispatches have since normalized; deferred revenue expected to be recognized in the coming quarter | `FWD_LOOKING` (Table 5 row 4); `REPEATED_CLAIM` |
| 4 | 109–111 | Performance reflects resilience of diversified business model, disciplined project execution, continued focus on operational efficiency and sustainable profitability | — |
| 5 | 115–117 | Long-term outlook for core business remains encouraging, supported by sustained investment across power, oil & gas, chemical, and process industries | `FWD_LOOKING` (Table 5 row 5) |
| 6 | 116–118 | India's ongoing capex cycle continues to create significant opportunities for specialized engineering/piping solutions, reinforcing confidence in sector growth prospects | `FWD_LOOKING` (Table 5 row 5) |
| 7 | 118–119 | Company continued to strengthen its manufacturing platform during the quarter | — |
| 8 | 119–121 | Seamless pipe manufacturing facility (commissioned March 2026, backward-integration strategy) is progressing through ramp-up phase, expected to contribute meaningfully as utilization improves, enhancing product integration, operating leverage, and margins over time | `FWD_LOOKING` (Table 5 row 6) |
| 9 | 121–124 | Anjar pipe fabrication facility (30,000 MT capacity added in FY26) continues to scale up steadily, strengthening manufacturing capabilities, execution capacity, ability to service larger/more complex projects | — |
| 10 | 126–128 | Majority of planned expansion capex now behind the company; focus shifted to improving capacity utilization, driving higher asset turns, expanding margins, generating stronger operating cash flows | — |
| 11 | 128–129 | Successful completion of ₹300 crore preferential issue during the quarter has further strengthened the balance sheet | — |
| 12 | 129–131 | Preferential-issue proceeds (earmarked for debt repayment) expected to materially reduce leverage and finance costs, improve return ratios, provide greater financial flexibility for future growth while maintaining disciplined capital structure | `FWD_LOOKING` (Table 5 row 7) |
| 13 | 133 | Non-core power generation business witnessed meaningful improvement during the quarter | — |
| 14 | 134–136 | Muktsar biomass power plant (6 MW) tariff revision: applicable tariff increased from ₹3.50/kWh to ₹5.224/kWh in FY26, with annual 5% escalation on the variable component, strengthening the business's earnings profile | — |
| 15 | 136–138 | 72,000 MTPA biomass pellet facility (estimated ₹80 crore revenue generation in FY27) commenced commercial operations approximately halfway through the quarter, resulting in only partial financial contribution in Q1 | `REPEATED_CLAIM` (Table 4 row 4) |
| 16 | 138–140 | As utilization ramps up, expect the pellet business to provide a meaningful contribution to revenue, profitability, and cash flows over the coming quarters, complementing renewable energy operations | `FWD_LOOKING` (Table 5 row 8); `REPEATED_CLAIM` |
| 17 | 142–143 | Continue to maintain a robust order book of ₹2,428 crore, providing strong revenue visibility across key end markets | `REPEATED_CLAIM` (Table 3 row 5, Table 4 row 3) |
| 18 | 143–145 | Remain confident in long-term growth trajectory, supported by healthy project pipeline, improving operating performance, enhanced manufacturing capabilities, and significantly stronger balance sheet post preferential issue | — |
| 19 | 145–147 | As utilization across expanded manufacturing footprint improves, expect operating leverage, profitability, and cash flows to strengthen further, supporting gradual debt reduction and continued stakeholder value creation | `FWD_LOOKING` (Table 5 row 9) |

## Table 7 — Signature Block / Administrative Content (page 1, lines 39–49; page 4, lines 154–189)

| # | Line(s) | Item | Detail | Flags |
|---|---------|------|--------|-------|
| 1 | 39–48 | Digital signature | Signatory: Ranjan Kumar Sarangi; Designation: Company Secretary and Compliance Officer; Membership No. F8604; Timestamp: 2026.08.04 14:29:13 +05'30' | No board-meeting timing given anywhere in this document to test against (results filing document, not this press release, would carry board meeting start/end times) — cannot assess timing flag from this doctype alone |
| 2 | 155–165 | Company boilerplate | "About DEE Development Engineers Limited" — business description, capacity claims, product/materials list (standard "about us" paragraph, not quarter-specific) | — |
| 3 | 168–175 | Contact details | Company contact: Mr. Brham Prakash Yadav, CFO; IR contact: Adfactors PR (Anand Venugopal / Ajinkya Salunke) | — |
| 4 | 180–184 | Corporate registration footer | Registered office, works address, phone/fax/email/web, CIN L74140HR1988PLC030225, GST Registration 06AACCD0207H1ZA | — |

---

## Reconciliation notes
- All six count-test categories reconcile exactly between grep and manual sweep; GATE A2 = PASS.
- No zero/nil/dash-valued standing line items exist in the sole financial table in this document (all 6 rows populated for both periods) — `ZERO_STANDING` flag not triggered this run.
- No prior-quarter presentation ledger was supplied, so `DROPPED_SLIDE` / page-level diff cannot be assessed; flagged as `NO_PRIOR_LEDGER` for A3/A4 awareness rather than left silent.
- Six distinct `REPEATED_CLAIM` instances identified where the same disclosure (revenue, EBITDA, order book, deferred revenue, biomass pellet ramp-up) is restated across the strapline, the bullet list, and the CMD quote — normal press-release structure, flagged only so A3/A4 do not double-count these as independent corroborating claims.
- One `FORMAT_ANOMALY` identified: Diluted EPS row's YoY column value ("22.1") lacks the "%" suffix present on every other row in the table.
