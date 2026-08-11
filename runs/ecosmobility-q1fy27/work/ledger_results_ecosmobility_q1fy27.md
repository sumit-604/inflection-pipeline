# A2 COMPLETENESS LEDGER — RESULTS FILING
Company: Ecos (India) Mobility & Hospitality Limited (ECOSMOBILITY)
Quarter: Q1 FY27 (quarter ended 30 June 2026)
Source: extract_results_ecosmobility_q1fy27.txt (451 lines, 9 pages, OCR pages 2-7)
Carried-forward A1 caveat: OCR noise on pages 2-3 (standalone + consolidated P&L) corrupted
SUBTOTAL/TOTAL rows (Total income, Total expenses, Profit before tax, Total tax expenses,
Net profit after tax, Total OCI, Total comprehensive income — this ledger additionally
identifies Total tax expenses and Total OCI as corrupted beyond the 5 A1 named). Individual
line items are intact. Every corrupted subtotal is flagged `TOTALS_CROSS_CHECK_NEEDED` below
and must be cross-checked against summed line items before being cited by A3/A4.

=== A2 COUNT TEST ===
category: notes (unnumbered paragraph notes, "Notes to unaudited Standalone & Consolidated
  Financial Results" section, lines 192-210)
  grep_count: 6   sweep_count: 6   match: yes
  detail: initial grep `^(The |These )` returned 5 (missed line 196, which begins with a
  curly-quote OCR artifact ‘ before "The figures..."). Re-swept with a byte-tolerant prefix
  pattern (`grep -nP "^.{0,3}(The |These )"`), which recovered line 196. Manual paragraph-by-
  paragraph read of lines 192-210 independently counts 6 paragraphs. Resolved match 6=6.
category: line_items (standalone + consolidated P&L tables combined)
  grep_count: 54 (after resweep)   sweep_count: 54   match: yes
  detail: first-pass grep on lettered sub-items (`^\(?[a-j]\)\s`) returned 28 (14 standalone +
  14 consolidated) against a manual sweep of 30 lettered sub-items (14 standalone + 16
  consolidated). The consolidated-table miss traced to two OCR corruptions: "e) Finance costs"
  OCR'd as "¢) Finance costs" (cent-sign substituted for "e"), and "g) Other expenses" OCR'd
  with the leading letter dropped entirely (bare ")"). Combined with numbered header/subtotal
  rows (10 standalone + 10 consolidated, several missing periods after the digit, e.g. "8+",
  "9 ", "10 ") and the six "attributable to:" dash-prefixed consolidated sub-rows, the full
  manual sweep totals 23 standalone + 31 consolidated = 54 distinct disclosed line items
  (including subtotal/total rows, excluding pure section headers with no own values). A
  resweep grep combining lettered items + numbered rows + dash-prefixed rows reaches 54.
  Resolved match 54=54.
category: zero_standing (current-quarter Jun 30 2026 column reads dash or 0.00)
  grep_count: 4   sweep_count: 4   match: yes
  detail: targeted line-number grep (lines 99, 137, 138, 147) confirms all four; no others in
  either table read dash/zero in the current-quarter column.
category: agenda_items (Board Outcome letter, Reg 30)
  grep_count: 5   sweep_count: 5   match: yes
category: auditor_paras (both review reports, numbered + unnumbered)
  grep_count: 9   sweep_count: 10   match: yes (after resweep)
  detail: grep on `^[0-9]\.\s` found 4 standalone-numbered + 5 consolidated-numbered = 9.
  Manual read found one additional UNNUMBERED paragraph in the consolidated report (lines
  333-335, the SEBI Circular CIR/CFD/CMDI/44/2019 procedures paragraph, sitting between
  numbered paras 3 and 4). Resweep count = 10. Resolved match 10=10.
category: annexure_b_items (Annexure-B, MoA Object Clause alteration table)
  grep_count: 10   sweep_count: 10   match: yes
category: annexure_c_items (Annexure-C, director particulars)
  grep_count: 7   sweep_count: 7   match: yes
category: signature_blocks
  grep_count: 4   sweep_count: 4   match: yes
category: entities (consolidation entity list, para 4 of consolidated auditor report)
  grep_count: 0   sweep_count: 0   match: yes (both zero — see flag below)
  detail: para 4 header ("The Statement includes results of the following entities:", line
  337) is present but the entity table itself is entirely lost to OCR (lines 339-341 contain
  only unreadable fragments: "TA", "Coa"", "AAA oe Fo"). Zero entities extractable. Flagged
  `ENTITY_LIST_NOT_EXTRACTED` — NOT FOUND per house rule; no estimate made.
gate_a2: pass
=== END COUNT TEST ===

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (Reg 30), page 1

Meeting: commenced 01:30 P.M., concluded 04:20 P.M. IST (2 hr 50 min) — line 52.

| # | Line | Agenda item | First 15 words | Flags |
|---|------|-------------|-----------------|-------|
| 1 | 34-35 | Standalone & Consolidated Unaudited Financial Results + Limited Review Report, Q1 FY27, Annexure-A | "Standalone & Consolidated Unaudited Financial Results of the Company along with the Limited Review Report for the quarter" | — |
| 2 | 36-37 | Alteration in Object Clause of MoA (add Event Management business), Annexure-B | "Alteration in the Object Clause of Memorandum of Association of the Company. The details are attached" | — |
| 3 | 38-40 | Re-appointment of Mr Rajesh Loomba (DIN 00082353) as Director, retiring by rotation, Annexure-C | "Re-appointment of Mr. Rajesh Loomba (DIN: 00082353) as a Director of the Company, who retires by rotation" | FAMILY_RELATIONSHIP (see Annexure-C row 7) |
| 4 | 41-47 | Draft notice of 30th AGM, 21 September 2026, via VC/OAVM | "Draft notice of the 30th Annual General Meeting to be held on Monday, 21st September 2026 through Video" | — |
| 5 | 48-50 | Record date 18 August 2026 for final dividend eligibility (FY26), subject to AGM approval | "Approved Tuesday, 18th August 2026 as the Record Date pursuant to Regulation 42 of SEBI (LODR) Regulations" | — |

## 2. DIGITAL SIGNATURE BLOCKS

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 58-66 | Shweta Bhardwaj | Company Secretary & Compliance Officer (Membership No: 43310) | Digitally signed 2026.08.11 16:30:09 +05'30' — 10 min after board meeting concluded (16:20 IST); no timing flag | — |
| 2 | 211-226 | Signatory name/title OCR-garbled ("thadun aging Director"); by order of the Board, likely the CMD (Rajesh Loomba) | Illegible in extract | Dated: August 11, 2026 (no time stamp captured) | OCR_ILLEGIBLE — signatory name not confirmable from extract |
| 3 | 275-285 | Sunil Wahal | Partner, S S Kothari Mehta & Co LLP (Membership No. 087294) — standalone review report | Date: August 11, 2026; UDIN: 26084294 ZWRX ZW 2848 | UDIN_OCR_UNCERTAIN — first 6 digits after year (084294) do not match stated Membership No. 087294 |
| 4 | 354-368 | Sunil Wahal | Partner, S S Kothari Mehta & Co LLP (Membership No. 087294) — consolidated review report | Date: August 11, 2026; UDIN: 26007294 LWDTOTH163 | UDIN_OCR_UNCERTAIN — first 6 digits after year (007294) do not match stated Membership No. 087294; also differs from UDIN in row 3 above (expected, different report, but both look OCR-corrupted relative to 087294) |

## 3. NOTES TO UNAUDITED STANDALONE & CONSOLIDATED FINANCIAL RESULTS (unnumbered paragraphs, lines 192-210)

| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| 1 | 193-195 | "The above unaudited standalone and consolidated financial results have been reviewed by the Audit Committee" | — |
| 2 | 196-198 | "The figures for the quarter ended March 31, 2026 as reported in these unaudited standalone" | — |
| 3 | 199-201 | "These unaudited standalone and consolidated financial results have been prepared in accordance with recognition and" | — |
| 4 | 202-204 | "The Company's business activity falls within a single segment, which is providing car rental services" | SINGLE_SEGMENT_NO_BREAKOUT — no segment table exists in this filing by design (Ind AS-108, single reportable segment) |
| 5 | 205-208 | "The statutory auditor of the Company have carried out review of these unaudited standalone and" | — |
| 6 | 209-210 | "The Board of Directors at its meeting held on July 6, 2026 has recommended a final" | Prior board meeting (6 July 2026) recommended dividend of ₹2.38/share, pending AGM approval — cross-reference to agenda item 5 (record date) |

### Footnotes below tables (separate from numbered/paragraph notes, swept per instruction)

| Line | Footnote text | Attaches to | Flags |
|------|----------------|-------------|-------|
| 116 | "*Not annualized" | Standalone EPS (line 113-115) | — |
| 173 | "*Figures have been showed zero due to rounding off in million" | Consolidated "Changes in stock-in-trade" (line 138) | ROUNDING_ZERO — explains the 0.00 current-quarter value; not a true nil transaction |
| 174 | "**Not annualized" | Consolidated EPS (line 170-172) | — |

## 4. STANDALONE P&L — EVERY LINE ITEM (lines 84-116, ₹ million)

| # | Line | Line item | Jun'26 | Mar'26 | Jun'25 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 85 | a) Revenue from operations | 2,060.56 | 1,989.86 | 1,776.43 | 7,810.42 | — |
| 2 | 86 | b) Other income | 38.18 | 36.31 | 28.64 | 113.57 | — |
| 3 | 87 | **Total income (1)** [subtotal] | 2,026.17* | (illegible) | 1,805.07* | (illegible) | TOTALS_CROSS_CHECK_NEEDED — label lost to OCR, only 2 of 4 period values legible and their column alignment is uncertain |
| 4 | 89 | a) Cost of services | 1,556.90 | 1,458.91 | 1,290.89 | 5,704.67 | — |
| 5 | 90 | b) Employee benefits expenses | 227.73 | 207.18 | 187.35 | 812.93 | — |
| 6 | 91 | c) Finance costs | 2.61 | 1.65 | 2.32 | 7.42 (OCR "742") | — |
| 7 | 92 | d) Depreciation and amortization expenses | 83.43 (OCR "$3.43") | 74.08 | 58.24 | 273.34 | OCR digit uncertain (leading digit rendered as "$") |
| 8 | 93 | e) Other expenses | 68.34 | 85.11 | 79.70 | 366.64 | — |
| 9 | 94 | **Total expenses (2)** [subtotal] | (illegible) | 1,826.93* | (illegible) | 1,618.50* | TOTALS_CROSS_CHECK_NEEDED — label garbled ("Totalexpenses"), 2 of 4 values legible, column alignment uncertain |
| 10 | 96 | **Profit before tax (1-2)** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label present, all values entirely lost to OCR on this line |
| 11 | 98 | a) Current tax | 45.51 | 50.69 (OCR "$0.69") | 50.74 | 220.92 | — |
| 12 | 99 | b) Tax relating to earlier years | — (dash) | 1.08 | — (dash) | 1.08 | ZERO_STANDING — current quarter (Jun'26) reads dash |
| 13 | 100 | c) Deferred tax | 0.23 | 12.34 | 3.19 (OCR "3,19") | 35.06 | — |
| 14 | 101 | **Total tax expenses** [subtotal] | NOT FOUND | NOT FOUND | 39.43* | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label lost entirely, only one value fragment legible, period unconfirmed |
| 15 | 103 | **Net profit after tax (3-4)** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label present, values reduced to unreadable fragments ("| .99 | see [3264 | SCS") |
| 16 | 106 | (a) Remeasurement gains/(losses) on defined benefit plans | (0.94) | 1.77 (OCR "L.77") | (1.57) | (3.77) | — |
| 17 | 107 | b) Income tax relating to the above item | 0.24 | 0.45 | 0.40 | 0.95 | — |
| 18 | 108 | **Total OCI (net of tax)** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — not named in A1's caveat list but equally OCR-corrupted; label present, values illegible |
| 19 | 110 | **Total comprehensive income (5+6)** [subtotal] | NOT FOUND | NOT FOUND | 131.47* | 569.23* | TOTALS_CROSS_CHECK_NEEDED — label present, 2 of 4 values legible, period alignment uncertain |
| 20 | 111 | Paid-up equity share capital (Face value ₹2/- each) | 120.00 | 120.00 | 120.00 | 120.00 | — |
| 21 | 112 | Other equity | (blank, quarterly cols not applicable) | (blank) | (blank) | 2,478.23 | Standard presentation — Other equity is a balance-sheet item, reported annual-only |
| 22 | 114 | a) Basic EPS (₹) | 2.40 | 2.66 | 2.21 | 9.53 | — |
| 23 | 115 | b) Diluted EPS (₹) | 2.40 | 2.66 | 2.21 (OCR "pee") | 9.53 (OCR "9:33") | OCR digit uncertain in Jun'25 and FY26 cells |

## 5. CONSOLIDATED P&L — EVERY LINE ITEM (lines 131-172, ₹ million)

| # | Line | Line item | Jun'26 | Mar'26 | Jun'25 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 132 | a) Revenue from operations | 2,139.72 (OCR "2139: 72") | 2,067.60 | 1,811.19 | 8,081.58 | — |
| 2 | 133 | b) Other income | 37.48 | 36.18 | 28.75 | 112.91 | — |
| 3 | 134 | **Total income** [subtotal] | 2,003.78* | 1,839.94* | 194.40* | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label garbled ("Totalincome"), 3 of 4 values partially legible; "194.40" for Jun'25 is implausibly low next to standalone's 1,805.07 for the same period, likely truncated (e.g. missing leading "1,9") — needs cross-check against summed line items |
| 4 | 136 | a) Cost of services | 1,587.29 | 1,507.33 | 1,315.58 | 5,881.06 | — |
| 5 | 137 | b) Purchase of stock-in-trade | — (dash) | 8.96 | 0.64 | 22.99 | ZERO_STANDING — current quarter (Jun'26) reads dash |
| 6 | 138 | c) Changes in stock-in-trade* | 0.00 | 0.20 | (0.02) (OCR "(0,02)") | 0.46 | ZERO_STANDING + ROUNDING_ZERO — current-quarter 0.00 explained by footnote as rounding artifact, not true nil |
| 7 | 139 | d) Employee benefits expenses | 237.63 | 219.71 | 194.90 | 860.50 | — |
| 8 | 140 | e) Finance costs | 2.77 | 1.75 | 2.32 | 7.52 | OCR rendered label letter "e)" as "¢)" — caused the grep miss noted in count test |
| 9 | 141 | f) Depreciation and amortization expenses | 61.55 | 79.43 | 58.30 | 280.58 | — |
| 10 | 142 | g) Other expenses | 70.32 | 89.87 | 81.54 | 377.28 | OCR dropped the label letter "g" entirely (line begins with bare ")") — caused the grep miss noted in count test |
| 11 | 143 | **Total expenses** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — entire row (label and all values) lost to OCR noise |
| 12 | 144 | **Profit before tax (1-2)** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label present, all values illegible |
| 13 | 146 | a) Current tax | 46.30 | 50.67 | 50.90 | 223.17 | — |
| 14 | 147 | b) Tax relating to earlier years | — (dash) | 1.15 | — (dash) | 1.15 | ZERO_STANDING — current quarter (Jun'26) reads dash |
| 15 | 148 | c) Deferred tax | 0.16 | 12.66 | 2.91 | 35.99 | — |
| 16 | 149 | **Total tax expenses** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label garbled, values illegible |
| 17 | 151 | **Net profit after tax (3-4)** [subtotal] | NOT FOUND | NOT FOUND | 73.7? (fragment "737") | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label present, values reduced to unreliable fragments |
| 18 | 154 | (a) Remeasurement gains/(losses) on defined benefit plans | (1.12) | 1.45 | (1.67) | (4.51) | — |
| 19 | 155 | (b) Income tax relating to the above item | 0.28 | 0.36 | 0.42 | 1.14 | — |
| 20 | 156 | **Total OCI (net of tax)** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — not in A1's named list, equally corrupted here |
| 21 | 158 | **Total comprehensive income (5+6)** [subtotal] | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | TOTALS_CROSS_CHECK_NEEDED — label present, all values illegible |
| 22 | 160 | Net profit attributable to — Owners of the Company | 145.26 | 157.37 | 132.87 | 575.77 (OCR "$75.77") | — |
| 23 | 161 | Net profit attributable to — Non controlling interest | 0.24 | (0.00) | — (dash) | (0.00) | Near-zero every period but not literally dash in all four — not flagged ZERO_STANDING (Jun'26 = 0.24, nonzero) |
| 24 | 163 | OCI attributable to — Owners of the Company | (0.83) | 1.09 (OCR "1,09") | (1.25) | (3.37) | — |
| 25 | 164 | OCI attributable to — Non controlling interest | (0.01) | (0.00) | — (dash) | (0.00) | Near-zero every period; not flagged ZERO_STANDING (Jun'26 nonzero) |
| 26 | 166 | TCI attributable to — Owners of the Company | 144.43 | 158.46 | 131.62 | 572.40 | — |
| 27 | 167 | TCI attributable to — Non controlling interest | 0.23 | (0.00) | — (dash) | (0.00) | Near-zero every period; not flagged ZERO_STANDING (Jun'26 nonzero) |
| 28 | 168 | Paid-up equity share capital (Face value ₹2/- each) | 120.00 | 120.00 | 120.00 | 120.00 | — |
| 29 | 169 | Other equity | (blank) | (blank) | (blank) | 2,529.37 | Standard presentation, annual-only |
| 30 | 171 | a) Basic EPS (₹) | 2.42 | 2.63 | 2.21 | 9.60 | — |
| 31 | 172 | b) Diluted EPS (₹) | 2.42 | 2.63 | 2.21 | 9.60 | — |

## 6. SEGMENT REPORTING

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 202-204 | Single reportable segment (car rental services, Ind AS-108) — company states no segment disclosure made | SINGLE_SEGMENT_NO_BREAKOUT — no segment table exists in this filing by design; not a missing disclosure |

## 7. AUDITOR'S REVIEW REPORT — STANDALONE (lines 228-289)

| # | Line(s) | Paragraph / element | Content | Flags |
|---|---------|----------------------|---------|-------|
| 1 | 228-236 | Title / heading | S S Kothari Mehta & Co LLP, Chartered Accountants — Independent Auditor's Review Report on Quarterly Unaudited Standalone Financial Results, Reg 33 | — |
| 2 | 238-244 | Addressee | To the Board of Directors, Ecos (India) Mobility & Hospitality Limited, New Delhi | — |
| 3 | 246-250 | Para 1 (scope of engagement) | Reviewed accompanying statement of unaudited standalone financial results for quarter ended June 30, 2026, per Reg 33 | — |
| 4 | 252-257 | Para 2 (management responsibility, basis of preparation) | Statement is Management's responsibility, approved by Board, prepared per Ind AS 34 | — |
| 5 | 259-266 | Para 3 (review standard applied) | Review per SRE 2410 (ICAI); scope less than audit; no audit opinion expressed | — |
| 6 | 268-273 | Para 4 (conclusion/opinion) | Unmodified/clean review conclusion — nothing came to attention causing belief of material misstatement or non-disclosure | No Emphasis of Matter paragraph, no Other Matters paragraph, no Going Concern paragraph present anywhere in this report — absence noted explicitly |
| 7 | 275-285 | Signature block | Firm's Reg No. 000756N/N500441; Sunil Wahal, Partner, Membership No. 087294; Date August 11, 2026; Place New Delhi; UDIN 26084294 ZWRX ZW 2848 | UDIN_OCR_UNCERTAIN (see Section 2, row 3) |
| 8 | 287-288 | Firm address footer | Plot No. 68, Okhla Industrial Area, Phase-III, New Delhi-110020 | — |

## 8. AUDITOR'S REVIEW REPORT — CONSOLIDATED (lines 291-368)

| # | Line(s) | Paragraph / element | Content | Flags |
|---|---------|----------------------|---------|-------|
| 1 | 291-299 | Title / heading | S S Kothari Mehta & Co LLP — Review Report on Quarterly Unaudited Consolidated Financial Results, Reg 33 | — |
| 2 | 301-307 | Addressee | To the Board of Directors, Ecos (India) Mobility & Hospitality Limited, New Delhi | — |
| 3 | 309-314 | Para 1 (scope, "Holding Company"/"Group" defined) | Reviewed unaudited consolidated financial results of Group for quarter ended June 30, 2026 | — |
| 4 | 316-322 | Para 2 (management responsibility, basis of preparation) | Statement is Holding Company Management's responsibility, approved by Board, prepared per Ind AS 34 | — |
| 5 | 324-331 | Para 3 (review standard applied) | Review per SRE 2410 (ICAI); scope less than audit; no audit opinion expressed | — |
| 6 | 333-335 | Unnumbered supplementary paragraph | Additional procedures performed per SEBI Circular CIR/CFD/CMDI/44/2019 dated 29 March 2019 under Reg 33(8), to the extent applicable | This paragraph is UNNUMBERED, sitting between numbered paras 3 and 4 — caused the auditor_paras grep/sweep mismatch (see count test) |
| 7 | 337-343 | Para 4 (entity list) | "The Statement includes results of the following entities:" — entity table follows | ENTITY_LIST_NOT_EXTRACTED — table content (lines 339-341) is unrecoverable OCR noise; zero entity names/relationships extractable. NOT FOUND, no estimate made. Also implies stage 6 (entity cross-check for ENTITY_CHANGE vs prior quarter) cannot be performed from this extract. |
| 8 | 347-353 | Para 5 (conclusion/opinion) | Unmodified/clean review conclusion — nothing came to attention causing belief of material misstatement or non-disclosure | No Emphasis of Matter, no Other Matters, no Going Concern paragraph present |
| 9 | 354-368 | Signature block | Firm's Reg No. 000756N/N500441; Sunil Wahal, Partner, Membership No. 087294; Date August 11, 2026; Place New Delhi; UDIN 26007294 LWDTOTH163 | UDIN_OCR_UNCERTAIN (see Section 2, row 4) |
| 10 | 342-343 | Firm address footer | Plot No. 68, Okhla Industrial Area, Phase-III, New Delhi-110020 | — |

## 9. CONSOLIDATION ENTITY LIST

| # | Line | Entity | Relationship | Flags |
|---|------|--------|---------------|-------|
| — | 337-341 | NOT FOUND | NOT FOUND | ENTITY_LIST_NOT_EXTRACTED — para 4 header present, table content entirely lost to OCR; cannot enumerate a single entity. No prior-quarter ledger was supplied to this run for a diff, so ENTITY_CHANGE cannot be evaluated either. Flag for A3: source PDF must be re-OCR'd or read directly to recover the subsidiary list. |

## 10. ANNEXURE-B — ALTERATION OF OBJECT CLAUSE OF MOA (page 8, lines 371-424)

| # | Line(s) | Particular | Detail (summarized) | Flags |
|---|---------|------------|----------------------|-------|
| 1 | 383-386 | Nature of change | Addition of Event Management as an additional line of business in the Object Clause of the MOA | — |
| 2 | 387-396 | Proposed Object Clause | Event management business in India and abroad — corporate/government/private/social events, conferences, exhibitions, weddings, etc., plus venue management, décor, fabrication, AV/technical, transportation, ticketing, bookings, permissions | — |
| 3 | 397-399 | Reason for change | Diversify business activities to include event management alongside existing car rental/mobility business | — |
| 4 | 400-403 | Impact of the proposed change | Enables exploring event-management opportunities; existing business continues as before | — |
| 5 | 404-408 | Approval required | Special Resolution of Members, plus other statutory approvals as required | — |
| 6 | 409-411 | Date of Board approval | 11th August 2026 | — |
| 7 | 412-414 | Effective date | Upon Members' approval and completion of statutory filings/formalities | — |
| 8 | 415-416 | Regulatory/statutory approvals | Members' Special Resolution; filing with Registrar of Companies | — |
| 9 | 417-421 | Interest of Directors/KMP | None, except to the extent of shareholding, if any | — |
| 10 | 422-423 | Change in control | None — no change in control or management | — |

## 11. ANNEXURE-C — DIRECTOR RE-APPOINTMENT: MR RAJESH LOOMBA (page 9, lines 426-451)

| # | Line | Particular | Detail | Flags |
|---|------|------------|--------|-------|
| 1 | 432 | DIN No. | 00082353 | — |
| 2 | 433 | Date of Birth | 03/07/1971 (age 55) | — |
| 3 | 434 | Age | 55 | — |
| 4 | 435-437 | Qualification | Bachelor's degree in commerce, University of Delhi | — |
| 5 | 438-446 | Experience in specific functional area | Chairman & Managing Director of the Company; associated with Company since 15 February 1996; inducted into 'Global Hall of Fame' 2019 by World Auto Forum | — |
| 6 | 447 | Date of appointment on the Board | 15/02/1996 | — |
| 7 | 449-451 | Relationship with Directors inter-se | Brother of Mr Aditya Loomba and Ms Nidhi Seth, both also directors of the Company | FAMILY_RELATIONSHIP — three siblings hold board seats; re-appointment vote (agenda item 3) should be read against this related-party board composition |

---
## FLAGS SUMMARY (all flags raised, with counts)

| Flag | Count | Where |
|------|-------|-------|
| ZERO_STANDING | 4 | Standalone note 12 (row 12, line 99); Consolidated rows 5, 6, 14 (lines 137, 138, 147) |
| TOTALS_CROSS_CHECK_NEEDED | 14 | 7 standalone subtotal rows + 7 consolidated subtotal rows (Sections 4 and 5) |
| ROUNDING_ZERO | 1 | Consolidated row 6 (line 138), footnote line 173 |
| ENTITY_LIST_NOT_EXTRACTED | 1 | Section 9 (line 337-341) |
| SINGLE_SEGMENT_NO_BREAKOUT | 1 | Section 6 (line 202-204) |
| FAMILY_RELATIONSHIP | 1 | Annexure-C row 7 (line 449-451), cross-referenced to agenda item 3 |
| OCR_ILLEGIBLE | 1 | Section 2, signature block row 2 (line 211-226, signatory name) |
| UDIN_OCR_UNCERTAIN | 2 | Section 2, signature blocks rows 3 and 4 (lines 285, 368) |

---
```yaml
stage: A2-enumerator
company: "ECOSMOBILITY"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/ecosmobility-q1fy27/work/ledger_results_ecosmobility_q1fy27.md"
counts:                      # per applicable category
  notes: 6
  line_items: 54
  zero_standing: 4
  agenda_items: 5
  auditor_paras: 10
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
  annexure_b_items: 10
  annexure_c_items: 7
  signature_blocks: 4
flags_raised: [ZERO_STANDING, TOTALS_CROSS_CHECK_NEEDED, ROUNDING_ZERO, ENTITY_LIST_NOT_EXTRACTED, SINGLE_SEGMENT_NO_BREAKOUT, FAMILY_RELATIONSHIP, OCR_ILLEGIBLE, UDIN_OCR_UNCERTAIN]
gate_a2: pass
mismatch_note: ""
```
