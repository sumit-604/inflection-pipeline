# A2 ENUMERATION LEDGER — Route Mobile Limited (ROUTE), Q1 FY27, RESULTS FILING
Source: extract_results_route_q1fy27.txt (683 lines, 12 pages, source_filename: results_board_outcome_reg33.pdf)
Prior-quarter ledger: none available — entity-diff (ENTITY_CHANGE) and dropped-line checks cannot be run this cycle; flagged NO_PRIOR_LEDGER.

Zero-standing methodology note: a table row is flagged `ZERO_STANDING` if AT LEAST ONE disclosed column (any of the four periods, or any of the three sub-columns in the IPO-utilisation tables) is nil / dash / blank. This is the broadest defensible reading of "never drop a nil row" and was reconciled against a narrower "current-quarter-only" test during the sweep (see COUNT TEST note under zero_standing) — the broad test is what is reported below.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 22   sweep_count: 22   match: yes
  (18 main numbered notes ["N)" pattern, 9 consolidated C-section + 9 standalone
  B-section] + 4 unnumbered sub-lettered footnotes restricted to notes zones
  [consol 4(a) L450, consol 7a L465, consol 7b L468, standalone 4(a) L658].
  Excludes L339/L341 "a./b." sub-items, which are OCI table data rows, not
  footnotes — counted instead under line_items.)
category: line_items       grep_count: 94   sweep_count: 94   match: yes
  (raw regex pass over table zones returned 95; one false positive was the
  consolidated Table A column-header row L301, whose date strings
  "30.06.2026" etc. matched the decimal-number pattern — excluded on manual
  sweep. Reconciled total 94 = Consol Table A 39 + Segment Table B 21 +
  Standalone Table A 22 + IPO-utilisation-consol 5 + IPO-utilisation-standalone
  5 + forex table 1 + dividend-from-subsidiary table 1.)
category: zero_standing    grep_count: 14   sweep_count: 16   match: yes (post-resweep)
  (dash-token regex across table zones caught 14 rows directly; manual sweep
  added 2 rows where the cell is truly BLANK rather than a literal "-"
  character — Other Equity quarterly columns, Consol Table A L364 and
  Standalone Table A L619 — which a dash-only regex cannot catch. Re-swept
  and reconciled at 16; this is the corrected, final count.)
category: agenda_items      grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras     grep_count: 14   sweep_count: 14   match: yes
  (numbered paras: consol 6 [L135,142,150,162,183,205] + standalone 4
  [L505,510,517,545] = 10, grep exact match. Continuation/unnumbered
  paragraphs required a second, more lenient regex pass — first pass with
  `[A-Z][a-z]+ ` missed L191 "Further, of these subsidiaries..." because the
  capitalised word is followed by a comma, not a space; re-run with
  `[A-Z][a-z]+` found consol continuations at L159, L191, L202, L214 = 4;
  standalone has zero continuation paragraphs. 10 + 4 = 14, reconciled.)
category: entities          grep_count: 33   sweep_count: 33   match: yes
category: signature_blocks  grep_count: 8    sweep_count: 8    match: yes
category: annexures         grep_count: 2    sweep_count: 2    match: yes
  (Annexure 1 = the whole results + review-report package referenced at L40;
  Annexure I = subsidiary list inside the consolidated auditor's report,
  L243-284.)
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (all 4, not just item 1)

Board meeting: commenced 6:45 P.M. IST, concluded 8:45 P.M. IST (L87) — 2-hour meeting.

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | L32-42 | Unaudited Financial Results | Board approved Unaudited Standalone + Consolidated Financial Results for Q1 FY27 with Limited Review Reports, reviewed by Audit Committee then Board; enclosed as Annexure 1; extract to be published in newspapers | — |
| 2 | L44-49 | Fixation of Date of 22nd AGM | AGM: Wed, September 02, 2026, 3:30 P.M. IST, via VC/OAVM | — |
| 3 | L51-69 | Declaration of First Interim Dividend FY2026-27 | ₹4/- per equity share (FV ₹10/-); Record Date July 29, 2026; payment within 30 days of declaration (July 23, 2026); TDS per Income Tax Act 2025, documents due by July 29, 2026 | — |
| 3a | L54 | — inner table row: Series | Equity (EQ) | — |
| 3b | L55-57 | — inner table row: Record Date | July 29, 2026 (Reg 42 eligibility) | — |
| 3c | L58 | — inner table row: Purpose | Payment of First Interim Dividend FY2026-27 | — |
| 3d | L59 | — inner table row: Dividend Per Share | ₹4/- | — |
| 3e | L60-62 | — inner table row: Dividend Payment Date | Within 30 days from declaration date | — |
| 3f | L63-69 | — inner table row: TDS on Dividend | Per Finance Act 2020 / Income Tax Act 2025; docs due July 29, 2026 | — |
| 4 | L71-79 | Lapse of Stock Options | Board noted/took on record two separate lapse events | — |
| 4a | L75-76 | — sub-item: RML ESOP Plan 2017 | 1,250 options lapsed, 1 eligible employee, "pursuant to the lapse of such options" (reason terse/circular) | — |
| 4b | L78-79 | — sub-item: RML ESOP Plan 2021 | 22,000 options lapsed, eligible employees (plural), pursuant to cessation of employment | — |

### 1a. Ancillary letter disclosures (not board-approval agenda items, but disclosed in the same letter — enumerated per "never drop a nil row" spirit)

| Line | Item | Detail |
|------|------|--------|
| L82-85 | Insider Trading window opening | Trading window for Designated Persons opens Sunday, July 26, 2026 |
| L107-109 | Distribution / cc list (3 recipients) | (a) National Securities Depository Limited, (b) Central Depository Services (India) Limited, (c) KFin Technologies Limited |

---

## 2. DIGITAL SIGNATURE BLOCKS (8 total)

| # | Line | Signatory | Designation | Timestamp | Document | Flag |
|---|------|-----------|-------------|-----------|----------|------|
| 1 | L95-103 | Tejas Devendra Shah | Company Secretary & Compliance Officer, ICSI Membership A34829 | 2026.07.23 21:51:53 +05'30' | Board Outcome letter | After board conclusion (20:45 IST) — no timing flag |
| 2 | L222-229 | Rajni Mundra | Partner, Walker Chandiok & Co LLP, Membership 058644; UDIN 26058644FNAHFF9719 | 2026.07.23 21:36:36 +05'30' | Consolidated Auditor's Review Report | After board conclusion — no timing flag |
| 3 | L371-376 | Rajdipkumar Chandrakant Gupta | Managing Director | 2026.07.23 21:28:21 +05'30' | Consolidated Table A (Statement of Results) | After board conclusion — no timing flag |
| 4 | L419-424 | Rajdipkumar Chandrakant Gupta | Managing Director | 2026.07.23 21:28:34 +05'30' | Consolidated Table B (Segment Results) | After board conclusion — no timing flag |
| 5 | L477-484 | Rajdipkumar Chandrakant Gupta | Managing Director | 2026.07.23 21:28:50 +05'30' | Notes to Consolidated Results (C section) | After board conclusion — no timing flag |
| 6 | L558-565 | Rajni Mundra | Partner, Walker Chandiok & Co LLP, Membership 058644; UDIN 26058644RACSDN6612 | 2026.07.23 21:35:06 +05'30' | Standalone Auditor's Review Report | After board conclusion — no timing flag |
| 7 | L627-632 | Rajdipkumar Chandrakant Gupta | Managing Director | 2026.07.23 21:26:50 +05'30' | Standalone Table A (Statement of Results) | After board conclusion — no timing flag; earliest of the 5 Gupta signatures |
| 8 | L678-683 | Rajdipkumar Chandrakant Gupta | Managing Director | 2026.07.23 21:27:40 +05'30' | Notes to Standalone Results | After board conclusion — no timing flag |

Check performed: all 8 signature timestamps fall between 21:26:50 and 21:51:53 IST, all after the 20:45 IST board conclusion (L87). No SIGNATURE_BEFORE_CONCLUSION flag triggered. Sequence is internally consistent (standalone package signed first ~21:26-21:28, then consolidated ~21:28, then both auditor's review reports ~21:35-21:37, then the CS's Board Outcome letter last at 21:51).

---

## 3. AUDITOR'S REVIEW REPORT — CONSOLIDATED (Walker Chandiok & Co LLP) — 10 paragraph units

| # | Line | Type | First ~15 words / content | Flags |
|---|------|------|---------------------------|-------|
| 1 | L135-140 | Numbered para 1 (scope) | "We have reviewed the accompanying statement of unaudited consolidated financial results ('the Statement')..." — refers to Annexure 1 for subsidiary list | — |
| 2 | L142-148 | Numbered para 2 (management responsibility) | "This Statement, which is the responsibility of the Holding Company's management and approved by the Holding Company's Board..." — Ind AS 34, Reg 33 | — |
| 3 | L150-158 | Numbered para 3 (review standard) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." — "we do not express an audit opinion" | — |
| 3-cont | L159-160 | Unnumbered continuation of para 3 | "We also performed procedures in accordance with the circular issued by the SEBI under Regulation 33(8)..." | — |
| 4 | L162-168 | Numbered para 4 (conclusion) | "Based on our review conducted and procedures performed as stated in paragraph 3 above and upon consideration of the review reports of other auditors..." — unmodified conclusion, no material misstatement | Opinion type: unmodified/unqualified limited-review conclusion |
| 5 | L183-190 | Numbered para 5 (reliance — other auditors) | "We did not review the interim financial results of twenty-four subsidiaries included in the Statement..." — 24 subsidiaries, revenue ₹660.94 cr, PAT ₹24.19 cr, TCI ₹24.19 cr, reviewed by other auditors | Entities reviewed by other auditors: 24 |
| 5-cont-a | L191-200 | Unnumbered continuation of para 5 | "Further, of these subsidiaries, eleven subsidiaries, are located outside India..." — foreign GAAP results converted to Ind AS by management, WCC reviewed the conversion adjustments only | 11 of the 24 are foreign entities — flag FOREIGN_AUDIT_RELIANCE |
| 5-cont-b | L202-203 | Unnumbered continuation of para 5 | "Our conclusion is not modified in respect of these matters with respect to our reliance on the work done by and the reports of the other auditors." | — |
| 6 | L205-212 | Numbered para 6 (unreviewed entities) | "The Statement includes the interim financial results of seven subsidiaries, which have not been reviewed by their auditors..." — 7 subsidiaries, revenue ₹1.12 cr, PAT ₹0.02 cr, TCI ₹0.02 cr, management-furnished, "not material to the Group" | Unreviewed/unaudited entities: 7 — flag UNREVIEWED_SUBSIDIARY |
| 6-cont | L214-215 | Unnumbered continuation of para 6 | "Our conclusion is not modified in respect of this matter with respect to our reliance on the financial results certified by the Board of Directors." | — |

Signature block: For Walker Chandiok & Co LLP, Chartered Accountants, Firm Reg. No. 001076N/N500013; Rajni Mundra, Partner, Membership No. 058644, UDIN 26058644FNAHFF9719; Place Mumbai; Date 23 July 2026 (L219-233 — see signature block table above for the digital-signature row).

No paragraph in the extract is explicitly headed "Emphasis of Matter" or "Other Matters" — paragraphs 5 and 6 function as reliance/unreviewed-entity disclosures but the extract carries no such literal heading text. NOT FOUND: explicit EoM/Other Matters caption (may exist as a bold/formatted heading in the source PDF not captured by this text extraction — extraction-limitation note, not a content gap). No Going Concern paragraph present.

Derived arithmetic (not in source text, flagged for A3/A4 cross-check, do not treat as an enumerated line): 33 total subsidiaries − 24 (reviewed by other auditors) − 7 (unreviewed) = 2 subsidiaries implied reviewed directly by Walker Chandiok & Co LLP. This subtraction is NOT stated anywhere in the filing.

---

## 4. AUDITOR'S REVIEW REPORT — STANDALONE (Walker Chandiok & Co LLP) — 4 paragraph units

| # | Line | Type | First ~15 words / content | Flags |
|---|------|------|----------------------------|-------|
| 1 | L505-508 | Numbered para 1 (scope) | "We have reviewed the accompanying statement of standalone unaudited financial results ('the Statement') of Route Mobile Limited..." | — |
| 2 | L510-515 | Numbered para 2 (management responsibility) | "The Statement, which is the responsibility of the Company's management and approved by the Company's Board of Directors..." | — |
| 3 | L517-524 | Numbered para 3 (review standard) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." — "we do not express an audit opinion" | No unnumbered continuation (unlike consol para 3, no SEBI-circular sentence here) |
| 4 | L545-550 | Numbered para 4 (conclusion) | "Based on our review conducted as above nothing has come to our attention that causes us to believe that the accompanying Statement..." — unmodified conclusion, no material misstatement | Opinion type: unmodified/unqualified limited-review conclusion |

Signature block: For Walker Chandiok & Co LLP, Chartered Accountants, Firm Reg. No. 001076N/N500013; Rajni Mundra, Partner, Membership No. 058644, UDIN 26058644RACSDN6612; Place Mumbai; Date 23 July 2026 (L555-568). No EoM, Other Matters, or Going Concern paragraphs present — standalone report is a plain 4-paragraph unmodified conclusion (single reviewed entity, no subsidiary-reliance language needed).

---

## 5. ANNEXURE I — LIST OF SUBSIDIARIES INCLUDED IN THE CONSOLIDATED STATEMENT (33 entities)

Cross-check against prior quarter: NOT POSSIBLE — no prior-quarter ledger supplied. Flag NO_PRIOR_LEDGER; ENTITY_CHANGE cannot be computed this cycle.

| # | Line | Entity | Notes |
|---|------|--------|-------|
| 1 | L251 | 365Squared Limited | — |
| 2 | L252 | Call 2 Connect India Private Limited | — |
| 3 | L253 | Estratec S.A.S. | — |
| 4 | L254 | Elibom Colombia S.A.S. | — |
| 5 | L255 | M.R. Messaging FZE | — |
| 6 | L256 | Masiv Chile SpA | — |
| 7 | L257 | Masivian Peru S.A.C. | — |
| 8 | L258 | Masivian S.A.S. | — |
| 9 | L259 | Mobilelink Telecomunicaciones SpA | — |
| 10 | L260 | MR Messaging (Holding) Limited | — |
| 11 | L261 | MR Messaging Limited | — |
| 12 | L262 | MR Messaging South Africa (Proprietary) Limited | — |
| 13 | L263 | PT. Route Mobile Indonesia | — |
| 14 | L264 | Route Connect (Kenya) Limited | — |
| 15 | L265 | Route Connect Private Limited | — |
| 16 | L266 | Route Ledger Technologies Private Limited | — |
| 17 | L267 | Route Mobile (Bangladesh) Limited | — |
| 18 | L268 | Route Mobile (UK) Limited | — |
| 19 | L269 | Route Mobile Arabia Telecom | — |
| 20 | L270-271 | Route Mobile Communication services Co. | formerly known as Interteleco International for Modem Communication Services — RENAME on record (cannot confirm vs prior quarter, no baseline supplied) |
| 21 | L272 | Route Mobile Inc. | — |
| 22 | L273 | Route Mobile LLC | — |
| 23 | L274 | Route Mobile Lanka (Private) Limited | — |
| 24 | L275 | Route Mobile Limited (Ghana) | — |
| 25 | L276 | Route Mobile Malta Limited | — |
| 26 | L277 | Route Mobile Mexico S De RL De CV | — |
| 27 | L278 | Route Mobile Nepal Pvt. Ltd. | — |
| 28 | L279 | Route Mobile Pte. Ltd. | — |
| 29 | L280 | Route Mobile Uganda Limited | — |
| 30 | L281 | Routesms Solutions FZE | — |
| 31 | L282 | Routesms Solution Nigeria Ltd. | — |
| 32 | L283 | Send Clean Inc. | — |
| 33 | L284 | Send Clean Private Limited | formerly known as Cellent Technologies (India) Pvt. Ltd. — RENAME on record (cannot confirm vs prior quarter) |

Cross-reference to note C(1), L427: "...and its 33 subsidiaries..." — matches list count. Aggregate review-status breakdown given in auditor report (not entity-mapped in source): 24 reviewed by other auditors (11 of those foreign), 7 unreviewed/management-furnished, remainder (2, derived) reviewed directly by Walker Chandiok. NOT FOUND: per-entity mapping of which of the 33 named entities falls into which review-status bucket — the filing gives only aggregate counts.

---

## 6. FINANCIAL STATEMENTS — CONSOLIDATED, TABLE A: STATEMENT OF UNAUDITED CONSOLIDATED FINANCIAL RESULTS (39 line items, L298-370)

Periods: Q1 FY27 (30.06.2026, Unaudited) | Q4 FY26 (31.03.2026, Refer note 3) | Q1 FY26 (30.06.2025, Unaudited) | FY26 (31.03.2026, Audited)

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | L304 | Revenue from operations | 1,151.51 | 1,130.90 | 1,050.83 | 4,408.21 | — |
| 2 | L305 | Other income | 11.06 | 27.85 | 10.97 | 54.09 | — |
| 3 | L306 | Total income | 1,162.57 | 1,158.75 | 1,061.80 | 4,462.30 | — |
| 4 | L309 | Purchase of messaging services | 911.07 | 866.99 | 825.76 | 3,400.90 | — |
| 5 | L310 | Employee benefits expense | 77.62 | 74.86 | 68.59 | 288.85 | — |
| 6 | L311 | Finance costs | 1.36 | 1.20 | 5.82 | 10.82 | — |
| 7 | L312 | Depreciation and amortisation expense | 23.71 | 23.61 | 22.48 | 91.61 | — |
| 8 | L313 | Other expenses | 57.34 | 52.82 | 62.58 | 181.21 | — |
| 9 | L314 | Total expenses | 1,071.10 | 1,019.48 | 985.23 | 3,973.39 | — |
| 10 | L317 | Profit before exceptional item and tax (1-2) | 91.47 | 139.27 | 76.57 | 488.91 | — |
| 11 | L319 | Exceptional item (Refer note 7 a and b) | - | - | - | (135.87) | ZERO_STANDING (nil all three quarters) |
| 12 | L321 | Profit before tax (3+4) | 91.47 | 139.27 | 76.57 | 353.04 | — |
| 13 | L324 | Current tax | 27.66 | 32.56 | 20.37 | 115.65 | — |
| 14 | L325 | Deferred tax benefit | (4.74) | (7.72) | (2.58) | (19.55) | — |
| 15 | L326 | [Tax expense subtotal, unlabeled] | 22.92 | 24.84 | 17.79 | 96.10 | — |
| 16 | L329 | Profit for the period/year (5-6) | 68.55 | 114.43 | 58.78 | 256.94 | — |
| 17 | L333 | Re-measurement of defined benefit plans | (0.43) | (0.16) | (0.93) | (0.97) | — |
| 18 | L334 | Income-tax effect on above | 0.11 | 0.04 | 0.23 | 0.24 | — |
| 19 | L335 | Sub total (i) | (0.32) | (0.12) | (0.70) | (0.73) | — |
| 20 | L339 | a. Effective portion of changes in fair value of cash flow hedge | (3.80) | - | - | - | ZERO_STANDING (nil in comparatives; new line item this quarter) |
| 21 | L340 | Income-tax effect of the above (hedge) | 0.95 | - | - | - | ZERO_STANDING (nil in comparatives) |
| 22 | L341 | b. Foreign currency translation reserve | 16.27 | 53.92 | 52.95 | 171.91 | — |
| 23 | L342 | Income-tax effect on above (FCTR) | - | - | - | - | ZERO_STANDING (nil ALL four periods) |
| 24 | L343 | Sub total (ii) | 13.42 | 53.92 | 52.95 | 171.91 | — |
| 25 | L345 | Total other comprehensive income (net of tax) | 13.10 | 53.80 | 52.25 | 171.18 | — |
| 26 | L347 | Total comprehensive income for the period/year (7+8) | 81.65 | 168.23 | 111.03 | 428.12 | — |
| 27 | L350 | Profit attributable to: Owners of the Parent | 62.61 | 109.32 | 53.21 | 239.02 | — |
| 28 | L351 | Profit attributable to: Non-controlling interest | 5.94 | 5.11 | 5.57 | 17.92 | — |
| 29 | L352 | [subtotal, unlabeled — repeats line 16] | 68.55 | 114.43 | 58.78 | 256.94 | — |
| 30 | L354 | OCI attributable to: Owners of the Parent | 12.90 | 52.20 | 51.50 | 166.94 | — |
| 31 | L355 | OCI attributable to: Non-controlling interest | 0.20 | 1.60 | 0.75 | 4.24 | — |
| 32 | L356 | [subtotal, unlabeled — repeats line 25] | 13.10 | 53.80 | 52.25 | 171.18 | — |
| 33 | L358 | TCI attributable to: Owners of the Parent | 75.51 | 161.52 | 104.71 | 405.96 | — |
| 34 | L359 | TCI attributable to: Non-controlling interest | 6.14 | 6.71 | 6.32 | 22.16 | — |
| 35 | L360 | [subtotal, unlabeled — repeats line 26] | 81.65 | 168.23 | 111.03 | 428.12 | — |
| 36 | L362 | Paid-up equity share capital (FV ₹10) | 63.00 | 63.00 | 63.00 | 63.00 | — |
| 37 | L364 | Other equity | (blank) | (blank) | (blank) | 2,706.59 | ZERO_STANDING (quarterly columns blank, only year-end disclosed — standard presentation for a balance-sheet item, still enumerated per rule) |
| 38 | L368 | Basic EPS (₹, not annualised) | 9.94 | 17.35 | 8.45 | 37.94 | — |
| 39 | L369 | Diluted EPS (₹, not annualised) | 9.94 | 17.35 | 8.45 | 37.94 | — |

Signature: Rajdipkumar Chandrakant Gupta, MD, digitally signed 2026.07.23 21:28:21 +05'30' (L371-376) — see signature block table.

---

## 7. FINANCIAL STATEMENTS — CONSOLIDATED, TABLE B: SEGMENT RESULTS (21 line items, L383-413)

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | L384 | Segment revenue - India | 236.21 | 263.29 | 219.47 | 934.39 | — |
| 2 | L385 | Segment revenue - Overseas | 1,063.28 | 1,028.66 | 992.73 | 4,129.31 | — |
| 3 | L386 | Segment revenue - Inter-segment revenue | (147.98) | (161.05) | (161.37) | (655.49) | — |
| 4 | L387 | Total revenue from operations | 1,151.51 | 1,130.90 | 1,050.83 | 4,408.21 | — |
| 5 | L390 | Segment results - India | (4.00) | 19.43 | 19.58 | 69.20 | — |
| 6 | L391 | Segment results - Overseas | 85.67 | 93.33 | 51.92 | 375.96 | — |
| 7 | L392 | Segment results - Inter-segment | 0.10 | (0.14) | (0.08) | 0.48 | — |
| 8 | L393-395 | Segment results before other income, finance costs, exceptional item and tax | 81.77 | 112.62 | 71.42 | 445.64 | — |
| 9 | L397 | Add: Other income | 11.06 | 27.85 | 10.97 | 54.09 | — |
| 10 | L398 | Less: Finance costs | 1.36 | 1.20 | 5.82 | 10.82 | — |
| 11 | L399 | Profit before exceptional item and tax | 91.47 | 139.27 | 76.57 | 488.91 | — |
| 12 | L400 | Less: Exceptional item | - | - | - | (135.87) | ZERO_STANDING (nil all three quarters) |
| 13 | L401 | Profit before tax | 91.47 | 139.27 | 76.57 | 353.04 | — |
| 14 | L404 | Segment assets - India | 1,679.63 | 1,642.30 | 1,583.39 | 1,642.30 | — |
| 15 | L405 | Segment assets - Overseas | 2,656.58 | 2,595.01 | 2,612.11 | 2,595.01 | — |
| 16 | L406 | Segment assets - Inter-segment assets | (651.41) | (681.08) | (901.47) | (681.08) | — |
| 17 | L407 | Total (segment assets) | 3,684.80 | 3,556.23 | 3,294.03 | 3,556.23 | — |
| 18 | L410 | Segment liabilities - India | 310.96 | 283.91 | 255.86 | 283.91 | — |
| 19 | L411 | Segment liabilities - Overseas | 1,095.79 | 1,103.52 | 1,337.79 | 1,103.52 | — |
| 20 | L412 | Segment liabilities - Inter-segment liabilities | (621.89) | (652.82) | (873.07) | (652.82) | — |
| 21 | L413 | Total (segment liabilities) | 784.86 | 734.61 | 720.58 | 734.61 | — |

Note L416: "(This space has been intentionally left blank)" — layout artifact, not a data row. Signature: Rajdipkumar Chandrakant Gupta, MD, digitally signed 2026.07.23 21:28:34 +05'30' (L419-424).

---

## 8. FINANCIAL STATEMENTS — STANDALONE, TABLE A: STATEMENT OF UNAUDITED STANDALONE FINANCIAL RESULTS (22 line items, L588-624)

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | L588 | Revenue from operations | 197.93 | 220.94 | 182.72 | 769.87 | — |
| 2 | L589 | Other income | 18.97 | 29.91 | 27.49 | 111.52 | — |
| 3 | L590 | Total income | 216.90 | 250.85 | 210.21 | 881.39 | — |
| 4 | L593 | Purchase of messaging services | 151.77 | 155.54 | 131.84 | 541.11 | — |
| 5 | L594 | Employee benefits expense | 24.30 | 19.94 | 22.95 | 88.97 | — |
| 6 | L595 | Finance costs | 0.39 | 0.28 | 0.37 | 1.44 | — |
| 7 | L596 | Depreciation and amortisation expense | 3.90 | 3.68 | 3.55 | 14.24 | — |
| 8 | L597 | Other expenses | 16.29 | 16.29 | 11.79 | 55.85 | — |
| 9 | L598 | Total expenses | 196.65 | 195.73 | 170.50 | 701.61 | — |
| 10 | L600 | Profit before tax (1-2) | 20.25 | 55.12 | 39.71 | 179.78 | — |
| 11 | L603 | Current tax | 4.79 | 14.49 | 9.35 | 45.58 | — |
| 12 | L604 | Deferred tax (benefit)/charge | (0.70) | (0.42) | (0.05) | (0.58) | — |
| 13 | L605 | [Tax expense subtotal, unlabeled] | 4.09 | 14.07 | 9.30 | 45.00 | — |
| 14 | L607 | Profit for the period/year (3-4) | 16.16 | 41.05 | 30.41 | 134.78 | — |
| 15 | L611 | Re-measurements of defined benefit plans | (0.43) | 0.10 | (0.93) | (0.76) | — |
| 16 | L612 | Income-tax effect of the above | 0.11 | (0.02) | 0.23 | 0.19 | — |
| 17 | L613 | Total OCI (net of tax) | (0.32) | 0.08 | (0.70) | (0.57) | — |
| 18 | L615 | Total comprehensive income (5+6) | 15.84 | 41.13 | 29.71 | 134.21 | — |
| 19 | L617 | Paid-up equity share capital (FV ₹10) | 63.00 | 63.00 | 63.00 | 63.00 | — |
| 20 | L619 | Other equity | (blank) | (blank) | (blank) | 1,262.17 | ZERO_STANDING (quarterly columns blank, only year-end disclosed) |
| 21 | L623 | Basic EPS (₹) | 2.56 | 6.52 | 4.83 | 21.39 | — |
| 22 | L624 | Diluted EPS (₹) | 2.56 | 6.52 | 4.83 | 21.39 | — |

Signature: Rajdipkumar Chandrakant Gupta, MD, digitally signed 2026.07.23 21:26:50 +05'30' (L627-632).

---

## 9. NOTES TO THE UNAUDITED CONSOLIDATED FINANCIAL RESULTS (C section, L426-473) — 9 main notes + 3 sub-items = 12 rows

| # | Line | First ~15 words | Detail / flags |
|---|------|------------------|-----------------|
| 1 | L427-430 | "The unaudited consolidated financial results of Route Mobile Limited (the 'Holding Company') and its 33..." | Basis of preparation, Ind AS 34, Reg 33; confirms 33-subsidiary group count |
| 2 | L432-434 | "The unaudited consolidated financial results for the quarter ended 30 June 2026 has been reviewed by..." | Audit Committee review + Board approval, 23 July 2026; limited review by statutory auditors |
| 3 | L436-437 | "The figures for the quarter ended 31 March 2026 represents the balancing figures between audited figures..." | Q4FY26 column is a balancing/derived figure (audited FY less unaudited 9M), not independently reviewed |
| 4 | L439-449 | "The utilisation of the Holding Company's initial public offer (IPO) proceeds has been summarised below :" | IPO utilisation table — see Section 11 below for the 5 line items inside it |
| 4a | L450 | "IPO proceeds which remained unutilised as at 30 June 2026 have been temporarily invested in bank..." | Footnote to note 4 — unutilised IPO funds parked in bank deposits |
| 5 | L452-454 | "Funds amounting to ₹ 867.50 crores raised by the Holding Company pursuant to a Qualified Institutional..." | QIP proceeds (prior years) being utilised per objects; unutilised amount in FDs as at 30.06.2026 |
| 6 | L456-462 | "The Group has presented net foreign exchange gain under "Other income" and net foreign exchange loss..." | Forex gain/loss presentation note — see Section 11 for the 1-line table |
| 7 | L464 | "Exceptional items for the previous year ended 31 March 2026 pertain to:" | Header for two sub-items (7a, 7b), both relate to FY26 only, nil in all Q1FY27/Q4FY26/Q1FY26 quarter columns |
| 7a | L465-467 | "One of the subsidiaries in the Group wrote off a net advance of ₹107.96 crores paid under..." | Advance write-off, minimum-guaranteed-SMS-volume vendor dispute; settlement agreement dated 19 Feb 2026, all claims/counterclaims withdrawn |
| 7b | L468-469 | "Another subsidiary in the Group wrote off an advance of ₹27.91 crores paid to a vendor for..." | Second advance write-off, messaging-services procurement vendor, recoverability uncertainty |
| 8 | L470 | "The Board of Directors of the Holding Company have recommended a interim dividend @ 40% ( ₹..." | Interim dividend ₹4/share (40% of FV ₹10), approved 23 July 2026 — cross-refs Board Outcome agenda item 3 |
| 9 | L472-473 | "Figures of the previous periods/year have been re-grouped/re-classified, wherever considered necessary to make them..." | Standard re-grouping/reclassification note, "not material" |

---

## 10. NOTES TO THE UNAUDITED STANDALONE FINANCIAL RESULTS (L634-676) — 9 main notes + 1 sub-item = 10 rows

| # | Line | First ~15 words | Detail / flags |
|---|------|------------------|-----------------|
| 1 | L636-639 | "The unaudited standalone financial results of Route Mobile Limited (the 'Company') for the quarter ended 30..." | Basis of preparation, Ind AS 34, Reg 33 |
| 2 | L641-642 | "The unaudited standalone financial results for the quarter ended 30 June 2026 has been reviewed by..." | Audit Committee review + Board approval, 23 July 2026; limited review by statutory auditors |
| 3 | L644-645 | "The figures for the quarter ended 31 March 2026 represents the balancing figures between audited figures..." | Same balancing-figure caveat as consolidated note 3 |
| 4 | L647-657 | "The utilisation of the Company's initial public offer (IPO) proceeds has been summarised below:" | IPO utilisation table (standalone) — see Section 11, 5 line items |
| 4a | L658 | "IPO proceeds which remained unutilised as at 30 June 2026 have been temporarily invested in bank..." | Footnote to note 4 |
| 5 | L660-662 | "Funds amounting to ₹ 867.50 crores raised by the Company pursuant to a Qualified Institutional Placement..." | QIP utilisation note, same figure as consolidated note 5 |
| 6 | L663 | "In accordance with Ind AS 108, 'Operating Segments', the Company has opted to present segment information..." | Segment reporting deferred to consolidated results — explains absence of a standalone segment table |
| 7 | L665-669 | "Other income, inter alia , includes dividend declared by the subsidiary companies of Route Mobile Limited:" | Dividend-from-subsidiaries table — see Section 11, 1 line item, ZERO_STANDING for Q4FY26 |
| 8 | L672 | "The Board of Directors have recommended an interim dividend @ 40% (₹ 4 per share of..." | Same interim dividend recommendation as consolidated note 8 |
| 9 | L674-675 | "Figures of the previous periods have been re-grouped/re-classified, wherever considered necessary to make them..." | Standard re-grouping/reclassification note, "not material to these standalone financial results" |

---

## 11. INNER TABLES WITHIN NOTES (mini financial tables, all line items already counted in the line_items / zero_standing totals above)

### 11a. IPO utilisation — Consolidated (note 4, L439-449) — 5 line items

| # | Line | Objects of the issue | Planned per Prospectus | Utilised upto 30.06.2026 | Unutilised as on 30.06.2026 | Flags |
|---|------|----------------------|------------------------|---------------------------|------------------------------|-------|
| 1 | L444-445 | Repayment/pre-payment of certain borrowings | 36.50 | 36.50 | - | ZERO_STANDING (unutilised balance nil — fully applied) |
| 2 | L446 | Acquisitions and other strategic initiatives | 83.00 | 83.00 | - | ZERO_STANDING (unutilised balance nil — fully applied) |
| 3 | L447 | Purchase of office premises in Mumbai | 65.00 | - | 65.00 | ZERO_STANDING (zero utilised to date — object still pending, going on years since IPO) |
| 4 | L448 | General corporate purposes | 55.50 | 55.50 | - | ZERO_STANDING (unutilised balance nil — fully applied) |
| 5 | L449 | Net utilisation (total) | 240.00 | 175.00 | 65.00 | — |

### 11b. IPO utilisation — Standalone (note 4, L647-657) — 5 line items, identical figures to 11a

| # | Line | Objects of the issue | Planned per Prospectus | Utilised upto 30.06.2026 | Unutilised as on 30.06.2026 | Flags |
|---|------|----------------------|------------------------|---------------------------|------------------------------|-------|
| 1 | L652-653 | Repayment/pre-payment of certain borrowings | 36.50 | 36.50 | - | ZERO_STANDING |
| 2 | L654 | Acquisitions and other strategic initiatives | 83.00 | 83.00 | - | ZERO_STANDING |
| 3 | L655 | Purchase of office premises in Mumbai | 65.00 | - | 65.00 | ZERO_STANDING |
| 4 | L656 | General corporate purposes | 55.50 | 55.50 | - | ZERO_STANDING |
| 5 | L657 | Net utilisation (total) | 240.00 | 175.00 | 65.00 | — |

### 11c. Net foreign exchange gain/(loss) — Consolidated (note 6, L456-462) — 1 line item

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | L462 | Net foreign exchange (gain)/loss | (0.61) | (18.15) | 24.73 | (14.76) | — (no dash in any period, not zero-standing) |

### 11d. Dividend declared by subsidiary companies — Standalone (note 7, L665-669) — 1 line item

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | L669 | Dividend declared by subsidiary companies | 4.22 | - | 2.46 | 2.46 | ZERO_STANDING (nil in Q4FY26 quarter — no subsidiary dividend declared that quarter) |

---

## 12. ZERO_STANDING SUMMARY (16 rows, cross-referenced to their source tables above)

| # | Table | Line | Particulars | Nil column(s) |
|---|-------|------|-------------|----------------|
| 1 | Consol A | L319 | Exceptional item | Q1FY27, Q4FY26, Q1FY26 |
| 2 | Consol A | L339 | a. Effective portion of cash flow hedge | Q4FY26, Q1FY26, FY26 |
| 3 | Consol A | L340 | Income-tax effect of the above (hedge) | Q4FY26, Q1FY26, FY26 |
| 4 | Consol A | L342 | Income-tax effect on above (FCTR) | ALL 4 periods |
| 5 | Consol A | L364 | Other equity | Q1FY27, Q4FY26, Q1FY26 (blank) |
| 6 | Segment B | L400 | Less: Exceptional item | Q1FY27, Q4FY26, Q1FY26 |
| 7 | Standalone A | L619 | Other equity | Q1FY27, Q4FY26, Q1FY26 (blank) |
| 8 | IPO util - Consol | L444-445 | Repayment/pre-payment of borrowings | Unutilised column |
| 9 | IPO util - Consol | L446 | Acquisitions and other strategic initiatives | Unutilised column |
| 10 | IPO util - Consol | L447 | Purchase of office premises in Mumbai | Utilised-upto column |
| 11 | IPO util - Consol | L448 | General corporate purposes | Unutilised column |
| 12 | IPO util - Standalone | L652-653 | Repayment/pre-payment of borrowings | Unutilised column |
| 13 | IPO util - Standalone | L654 | Acquisitions and other strategic initiatives | Unutilised column |
| 14 | IPO util - Standalone | L655 | Purchase of office premises in Mumbai | Utilised-upto column |
| 15 | IPO util - Standalone | L656 | General corporate purposes | Unutilised column |
| 16 | Dividend from subsidiary - Standalone | L669 | Dividend declared by subsidiary companies | Q4FY26 column |

---

## FLAGS RAISED (summary)

- `ZERO_STANDING` x16 — see Section 12.
- `FOREIGN_AUDIT_RELIANCE` — 11 of the 24 unreviewed-by-holding-auditor subsidiaries are located outside India, reviewed under local review standards, converted to Ind AS by management (consol auditor report para 5-cont, L191-200).
- `UNREVIEWED_SUBSIDIARY` — 7 subsidiaries' interim results not reviewed by any auditor, furnished by management, deemed "not material to the Group" (consol auditor report para 6, L205-212).
- `NO_PRIOR_LEDGER` — no prior-quarter ledger supplied; ENTITY_CHANGE and DROPPED_SLIDE/line diffs could not be run this cycle. Two entities in Annexure I carry "formerly known as" renames on their face (L270-271 Route Mobile Communication services Co.; L284 Send Clean Private Limited) — these are pre-existing renames disclosed in-filing, not confirmed as new-this-quarter without a baseline.
- No `SIGNATURE_BEFORE_CONCLUSION` flag — all 8 digital signatures postdate the 20:45 IST board conclusion.
- No `MGMT_ABSENCE` / `REPEAT_QUESTION` — not applicable to a results-filing doctype.

---
