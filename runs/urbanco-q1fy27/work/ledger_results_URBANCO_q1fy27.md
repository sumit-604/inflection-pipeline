# A2 ENUMERATION LEDGER — RESULTS FILING
Company: Urban Company Limited (URBANCO) | Quarter: Q1 FY27 (quarter ended June 30, 2026)
Source: results_URBANCO_q1fy27.pdf (11 pages) | A1 extract: extract_results_URBANCO_q1fy27.txt (582 lines)
Prior-quarter ledger: none available (first quarterly run for this ticker) — cross-quarter diffs (DROPPED_SLIDE-equivalent / entity-list diffs) deferred to A3/A4; noted where this run's own text supplies intra-filing evidence of change.

```
=== A2 COUNT TEST ===
category: notes           grep_count: 16   sweep_count: 16   match: yes
category: line_items      grep_count: 88   sweep_count: 88   match: yes
category: zero_standing   grep_count: 9    sweep_count: 9    match: yes
category: agenda_items    grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras   grep_count: 14   sweep_count: 14   match: yes
category: entities        grep_count: 10   sweep_count: 10   match: yes
category: signature_blocks grep_count: 3   sweep_count: 3    match: yes  (informational; no dedicated YAML field)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note: grep passes used `grep -n -E` on line-numbered ranges of the extract
(notes sections, statement tables, segment table, Annexure I, auditor report paragraphs).
Two adjustments were required to reconcile grep against manual sweep, both applied
consistently before the final count above:
1. Notes — both Notes sections open with an unnumbered first note (the numeral "1" is
   absent in the source/OCR; note 2 onward is numbered). Grep on `^[0-9]+[\. ]` alone
   yields 8 (consolidated) + 6 (standalone) = 14; manual sweep confirms 9 + 7 = 16
   (the implied "note 1" in each section, immediately following the "Notes to the ...
   Results" header). Final count = 16, methodology documented so re-runs reproduce it.
2. Zero-standing — a naive "two adjacent dash columns" grep (`\s-\s+-\s`) misses rows
   where the current-quarter (first data) column is a lone dash but a non-dash value
   sits in an adjacent column (e.g. Consolidated "Current tax": `- (0.21) - -`). Refined
   grep targets the first data token after the item description specifically. Reconciled
   count = 9. "Exceptional items" (consolidated line 260) is a related but distinct case:
   current-quarter value is non-zero (5.27); it was zero/dash in all three comparative
   periods shown. It is NOT counted in zero_standing (current-period value is non-nil)
   but is flagged `TEMPLATE_LINE_ACTIVATED` below since it is functionally the same
   "template line firing" pattern the ZERO_STANDING rule exists to surface.

---

## 1. NUMBERED NOTES

### 1A. Notes to the Consolidated Financial Results (page 6-7)
| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| 1 | 293 | "The statement of consolidated financial results of Urban Company Limited... have been reviewed and recommended by the Audit Committee" | Unnumbered in source (implied note 1) |
| 2 | 298 | "The Financial Results have been prepared in accordance with the recognition and measurement principles laid down..." | |
| 3 | 303 | "Information reported to the Chief Operating Decision Maker (CODM) for the purposes of cost allocation..." (segment note; full segment table at lines 324-353) | |
| 4 | 358 | "The figures for the quarter ended March 31, 2026, represent the difference between the audited annual..." | Standard balancing-figure disclosure |
| 5 | 361 | "The Financial Results for the quarter ended June 30, 2025, were neither subject to limited review nor audit..." | |
| 6 | 365 | "The Company's equity shares were listed on the National Stock Exchange of India limited (NSE) and BSE..." | Listing date Sept 17, 2025 |
| 7 | 367 | "During the quarter ended June 30, 2026, the 'ESOP Trust' has alloted 1,03,59,538 equity shares of ₹1/- each..." | |
| 8 | 370 | "During the quarter ended June 30, 2026, the Group has closed down its step-down subsidiary, 'Urban Company Arabia..." | ENTITY_CHANGE (cross-ref Annexure I entity 7, FCTR ₹5.27cr reclassified as exceptional item — cross-ref statement line 260) |
| 9 | 376 | "The financial results for the quarter and year ended June 30, 2026 are also being made available on the Stock Exchange..." | |

### 1B. Notes to the Standalone Financial Results (page 11)
| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| 1 | 544 | "The statement of standalone financial results of Urban Company Limited... have been reviewed and recommended by the Audit Committee" | Unnumbered in source (implied note 1) |
| 2 | 548 | "The Standalone Financial Results for the quarter ended June 30, 2025, were neither subject to limited review nor audit..." | |
| 3 | 552 | "The Standalone Financial Results have been prepared in accordance with the recognition and measurement principles laid down..." | |
| 4 | 557 | "The Company publishes these Standalone Financial Results along with the Consolidated Financial Results. In accordance with Ind AS 108..." | Confirms segment disclosure is consolidated-only (no standalone segment table — expected, not a gap) |
| 5 | 560 | "The Company's equity shares were listed on the National Stock Exchange of India limited (NSE) and BSE..." | Duplicate of consolidated note 6 |
| 6 | 562 | "During the quarter ended June 30, 2026, the 'ESOP Trust' has alloted 1,03,59,538 equity shares of ₹1/- each..." | Duplicate of consolidated note 7 |
| 7 | 565 | "The figures for the quarter ended March 31, 2026, represent the difference between the audited annual standalone..." | |

No asterisk/dagger/"Note:"-prefixed footnotes found outside the numbered sequences above. Two in-table qualifier footnotes captured instead as flags on their line items below: "(Face value on ₹1/- each)" (lines 282, 532) and "(not annualized except for yearly figures)" (lines 286, 537-538 area).

Notes total: 16 (9 consolidated + 7 standalone).

---

## 2. CONSOLIDATED STATEMENT OF FINANCIAL RESULTS — LINE ITEMS (page 5, lines 237-288)
Columns: Q1 FY27 (Jun 30, 2026, Unaudited) | Q4 FY26 (Mar 31, 2026, Audited) | Q1 FY26 (Jun 30, 2025, Unaudited) | FY26 (Mar 31, 2026, Audited)

| S.No/Line | Item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| 1 | Income (header) | 237 | — | — | — | — | |
| (a) | Revenue from operations | 238 | 528.34 | 425.56 | 367.27 | 1,555.54 | |
| (b) | Other income | 239 | 37.83 | 36.74 | 31.22 | 136.69 | |
| — | Total income (a+b) | 240 | 566.17 | 462.30 | 398.49 | 1,692.23 | subtotal |
| 2 | Expenses (header) | 242 | — | — | — | — | |
| a) | Purchases of stock-in-trade | 243 | 110.82 | 99.87 | 79.35 | 344.44 | |
| b) | Changes in inventories of stock-in-trade | 244 | (10.84) | (11.04) | (10.76) | (34.48) | |
| c) | Inventory loss on account of fire | 245 | - | - | 9.05 | 9.11 | ZERO_STANDING (current + prior quarter) |
| d) | Employee benefits expense | 246 | 151.15 | 129.31 | 99.22 | 456.48 | |
| e) | Finance costs | 247 | 3.11 | 3.28 | 2.68 | 12.00 | |
| f) | Depreciation and amortization expense | 248 | 15.79 | 13.57 | 9.50 | 45.21 | |
| g) | Listing expenses | 249 | - | - | 1.93 | 19.03 | ZERO_STANDING (current + prior quarter) |
| h) | Other expenses | 250 | 369.85 | 321.86 | 193.28 | 983.87 | |
| — | Total expenses (a+b+c+d+e+f+g+h) | 251 | 639.88 | 556.85 | 384.25 | 1,835.66 | subtotal |
| 3 | Profit/(loss) before share of net loss of JV, exceptional items and tax (1-2) | 253-254 | (73.71) | (94.55) | 14.24 | (143.43) | wraps to line 254 ("tax (1-2)") |
| 4 | Share of net loss of Joint Venture (equity method) | 256 | (4.77) | (5.31) | (8.60) | (31.17) | |
| 5 | Profit/(loss) before exceptional items and tax (3+4) | 258 | (78.48) | (99.86) | 5.64 | (174.60) | |
| 6 | Exceptional items (refer note 8) | 260 | 5.27 | - | - | - | TEMPLATE_LINE_ACTIVATED — zero/dash in all 3 comparative periods; ₹5.27cr FCTR reclassification this quarter per note 8, tied to Annexure I entity 7 liquidation |
| 7 | Profit/(loss) before tax (5-6) | 261 | (83.75) | (99.86) | 5.64 | (174.60) | |
| 8 | Tax expense/(credit) (header) | 263 | — | — | — | — | |
| a) | Current tax | 264 | - | (0.21) | - | - | ZERO_STANDING (current, prior-year comparative, and FY26 all zero; only the single Q4FY26 balancing quarter shows a value) |
| b) | Deferred tax | 265 | 8.37 | 61.51 | (1.30) | 60.21 | |
| — | Total tax expense/(credit) | 266 | 8.37 | 61.30 | (1.30) | 60.21 | subtotal |
| 9 | Profit/(loss) for the period/year (7-8) | 268 | (92.12) | (161.16) | 6.94 | (234.81) | |
| 10 | Other comprehensive income (header) | 270 | — | — | — | — | |
| (a) | Items that will not be reclassified to P&L (sub-header) | 271 | — | — | — | — | |
| — | -Remeasurement of defined benefit plans | 272 | 0.21 | (0.34) | 4.72 | 5.08 | |
| — | -Income tax effect of above | 273 | - | 1.19 | (1.19) | - | ZERO_STANDING (current quarter and FY26 zero) |
| (b) | Items that will be reclassified to P&L (sub-header) | 274 | — | — | — | — | |
| — | -Exchange difference on translation of foreign operations | 275 | 5.03 | 1.13 | 0.35 | 2.33 | |
| — | -Income tax on above | 276 | - | - | - | - | ZERO_STANDING (all four periods — canonical dormant template line) |
| — | Total other comprehensive income (a+b) | 277 | 5.24 | 1.98 | 3.88 | 7.41 | subtotal |
| 11 | Total comprehensive income/(loss) for the period/year (9+10) | 279 | (86.88) | (159.18) | 10.82 | (227.40) | |
| 12 | Paid-up equity share capital | 281-282 | 147.26 | 146.22 | 48.98 | 146.22 | footnote line 282: "(Face value on ₹1/- each)" |
| 13 | Other equity | 283 | (blank) | (blank) | (blank) | 1,997.37 | Quarter columns blank (not dash) — standard convention, balance-sheet item disclosed only at year-end; not flagged ZERO_STANDING (distinct from dash convention) |
| 14 | Earnings/(loss) per equity share (₹) (header) | 285-286 | — | — | — | — | footnote line 286: "(not annualized except for yearly figures)" |
| (a) | Basic (₹) | 287 | (0.60) | (1.08) | 0.05 | (1.57) | |
| (b) | Diluted (₹) | 288 | (0.60) | (1.08) | 0.05 | (1.57) | |

Consolidated statement line items: 38.

---

## 3. CONSOLIDATED SEGMENT REPORTING — LINE ITEMS (Note 3 detail table, page 6, lines 324-353)

| Item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| Revenue from external customers (header) | 333 | — | — | — | — | |
| India consumer services (excl. InstaHelp) - Total | 334 | 356.42 | 288.47 | 271.61 | 1,086.62 | |
| -Services | 335 | 290.23 | 219.03 | 222.21 | 864.57 | sub-line |
| -Products | 336 | 66.19 | 69.44 | 49.40 | 222.05 | sub-line |
| Native | 337 | 95.28 | 70.22 | 59.55 | 266.95 | |
| International business | 338 | 65.42 | 57.93 | 35.89 | 184.59 | |
| InstaHelp | 339 | 11.22 | 8.94 | 0.22 | 17.38 | |
| Grand Total | 340 | 528.34 | 425.56 | 367.27 | 1,555.54 | subtotal, ties to statement line 238 (a) |
| Segment Results (header) | 342 | — | — | — | — | |
| India consumer services (excl. InstaHelp) | 343 | 82.02 | 35.64 | 40.30 | 138.22 | |
| Native | 344 | (7.75) | (8.06) | (10.87) | (33.35) | |
| International business | 345 | 3.16 | 4.72 | (1.95) | 7.56 | |
| InstaHelp | 346 | (131.58) | (118.73) | (9.24) | (231.79) | OCR renders trailing bracket as apostrophe artifact |
| Consolidated segment results - Profit/(loss) | 347 | (54.15) | (86.43) | 18.24 | (119.36) | subtotal |
| Add: Other income | 349 | 37.83 | 36.74 | 31.22 | 136.69 | ties to statement line 239 |
| Less: Finance costs | 350 | (3.11) | (3.28) | (2.68) | (12.00) | ties to statement line 247 |
| Less: Share based payment expense | 351 | (38.49) | (28.01) | (23.04) | (103.55) | not a separate line on the face statement — only disclosed here in segment note |
| Less: Depreciation and amortisation | 352 | (15.79) | (13.57) | (9.50) | (45.21) | ties to statement line 248 |
| Profit/(loss) before share of JV, exceptional items and tax | 353 | (73.71) | (94.55) | 14.24 | (143.43) | ties to statement line 253 |

Segment reporting line items: 19.

---

## 4. STANDALONE STATEMENT OF FINANCIAL RESULTS — LINE ITEMS (page 10, lines 498-539)
Same column structure as Section 2.

| S.No/Line | Item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| 1 | Income (header) | 498 | — | — | — | — | |
| (a) | Revenue from operations | 499 | 375.54 | 281.72 | 268.55 | 1,081.22 | |
| (b) | Other income | 500 | 43.16 | 41.21 | 35.31 | 154.24 | |
| — | Total income (a+b) | 501 | 418.70 | 322.93 | 303.86 | 1,235.46 | subtotal |
| 2 | Expenses (header) | 503 | — | — | — | — | |
| a) | Purchases of stock-in-trade | 504 | 54.39 | 38.96 | 36.70 | 162.33 | |
| b) | Changes in inventories of stock-in-trade | 505 | (5.11) | (2.97) | (4.13) | (18.04) | |
| c) | Inventory loss on account of fire | 506 | - | - | 2.01 | 2.07 | ZERO_STANDING (current + prior quarter) |
| d) | Employee benefits expense | 507 | 131.02 | 106.92 | 86.91 | 393.61 | |
| e) | Finance costs | 508 | 3.01 | 3.21 | 2.67 | 11.78 | |
| f) | Depreciation and amortization expense | 509 | 15.09 | 13.07 | 8.73 | 42.91 | |
| g) | Listing expenses | 510 | - | - | 1.93 | 19.03 | ZERO_STANDING (current + prior quarter) |
| h) | Other expenses | 511 | 296.21 | 257.97 | 145.33 | 756.93 | |
| — | Total expenses (a+b+c+d+e+f+g+h) | 512 | 494.61 | 417.16 | 280.15 | 1,370.62 | subtotal |
| 3 | Profit/(loss) before tax (1-2) | 514 | (75.91) | (94.23) | 23.71 | (135.16) | source shows unbalanced parentheses on 3 of 4 figures (OCR artifact, e.g. "(94.23" / "(135.161" — not a sign/value error, closing paren dropped or digit-corrupted) |
| 4 | Tax expense/(credit) (header) | 516 | — | — | — | — | |
| a) | Current tax | 517 | - | - | - | - | ZERO_STANDING (all four periods — standalone entity shows no current tax in any period presented) |
| b) | Deferred tax | 518 | 8.37 | 61.51 | (1.30) | 60.21 | |
| — | Total tax expense/(credit) | 519 | 8.37 | 61.51 | (1.30) | 60.21 | subtotal |
| 5 | Profit/(loss) for the period/year (3-4) | 521 | (84.28) | (155.74) | 25.01 | (195.37) | same OCR paren artifact as line 514 |
| 6 | Other comprehensive income (header) | 523 | — | — | — | — | |
| — | Items that will not be reclassified to P&L (sub-header, unlettered — only one OCI category at standalone level) | 524 | — | — | — | — | No "items that will be reclassified" (translation FX) category at standalone level — expected, standalone has no foreign operations to translate |
| — | -Remeasurement of defined benefit plans | 525 | 0.21 | (0.13) | 4.72 | 5.22 | |
| — | -Income tax effect of above | 526 | - | 1.19 | (1.19) | - | ZERO_STANDING (current quarter and FY26 zero) |
| — | Total other comprehensive income | 527 | 0.21 | 1.06 | 3.53 | 5.22 | subtotal |
| 7 | Total comprehensive income/(loss) for the period/year (5+6) | 529 | (84.07) | (154.68) | 28.54 | (190.15) | same OCR paren artifact |
| 8 | Paid-up equity share capital | 531-532 | 147.26 | 146.22 | 48.98 | 146.22 | footnote line 532: "(Face value on ₹1/- each)" |
| 9 | Other equity | 534 | (blank) | (blank) | (blank) | 2,489.91 | Quarter columns blank — same convention as consolidated line 283; note value differs from consolidated Other equity (1,997.37) as expected (standalone vs consolidated equity base) |
| 10 | Earnings/(loss) per equity share (₹) (header) | 536-537 | — | — | — | — | footnote line 537: "(not annualized except for yearly figures)" |
| (a) | Basic (₹) | 538 | (0.55) | (1.04) | 0.17 | (1.31) | |
| (b) | Diluted (₹) | 539 | (0.55) | (1.04) | 0.17 | (1.31) | OCR renders opening paren as "<" |

Standalone statement line items: 31.

Line items total (Sections 2+3+4): 38 + 19 + 31 = 88.
Zero-standing total: 5 (consolidated statement) + 4 (standalone statement) = 9.

---

## 5. ANNEXURE I — LIST OF ENTITIES IN UNAUDITED CONSOLIDATED FINANCIAL RESULTS (page 4, lines 183-223)

| Sr. No | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| 1 | 189 | Urban Company Limited | Parent | |
| 2 | 192 | Handy Home Solutions Private Limited | Wholly owned subsidiary | |
| 3 | 195 | Urban Home Experts PTE LTD | Wholly owned subsidiary | |
| 4 | 198 | Urbanclap Technologies FZCO (DMCC) | Step down subsidiary | |
| 5 | 201 | Urban Company Technologies Onshore LLC | Step down subsidiary | |
| 6 | 204 | Urban Essentials General Trading L.L.C | Step down subsidiary | |
| 7 | 207-208 | Urban Company Arabia for Information Technology | Step down subsidiary | ENTITY_CHANGE — annotated "(liquidated as on 24 May 2026)"; formally dissolved during the quarter; cross-ref consolidated note 8 (line 370) and statement line 260 (exceptional item, FCTR reclassification of ₹5.27cr) |
| 8 | 211-212 | Company Waed Khadmat Al-Munzal For Marketing | Joint Venture of wholly owned subsidiary | This is the "joint venture" whose share of net loss is picked up at consolidated statement line 256 |
| 9 | 215 | Urban Company ESOP Trust | Entity controlled by the Parent | Standalone review report para 1 (line 416-417) states standalone Statement includes this trust's financial results |
| 10 | 218 | Partner Welfare Trust | Entity controlled by the Group | |

Entities total: 10.

AMBIGUOUS_ENTITY_REFERENCE flag: Consolidated review report para 8 (line 153) refers to "one trust which has not been reviewed" with Nil revenue/profit/OCI, without naming it. Two trusts appear in Annexure I (entity 9: Urban Company ESOP Trust; entity 10: Partner Welfare Trust). Standalone review report para 1 states the standalone Statement includes the ESOP Trust's results (implying it is in scope/reviewed there), which by elimination points to Partner Welfare Trust as the unreviewed entity — but the filing does not state this explicitly. Flagged for A3/A4 to resolve by name, not resolved here (enumeration only).

No prior-quarter entity list was supplied for this run; the ENTITY_CHANGE flag above is based entirely on this filing's own note 8 disclosure of the liquidation event, not a cross-quarter diff.

---

## 6. BOARD OUTCOME / REG 30-33 LETTER — AGENDA ITEMS (page 1, lines 14-65)

Board meeting: commenced 15:00 (3:00 p.m.), concluded 15:25 (3:25 p.m.) — line 40. Duration 25 minutes.

| # | Line | Agenda item | Flags |
|---|------|-------------|-------|
| 1 | 18-21 | Board "considered and approved the unaudited financial results (standalone and consolidated) for the quarter ended June 30, 2026" and "taken on record limited review report(s) issued by the statutory auditors... based on the recommendations of the Audit Committee" | Single bundled board action — results approval + review reports taken on record |

Sweep for other standard agenda categories (AR approval, AGM notice, record date, dividend, director appointments/resignations, auditor changes, scrutinizer appointment, ESOP grants, capital-raising enabling resolutions) — grep on those keywords across lines 14-65 returns no hits beyond the item above. No other agenda items are disclosed in this letter, consistent with the short 25-minute meeting window.

Agenda items total: 1.

Note: the letter's own "enclosed as Annexure - I" (line 37-38) refers to the enclosure bundle (financial results + limited review reports), a different document from "Annexure I" inside the consolidated Limited Review Report (Section 5 above, the entity list). Both are labelled "Annexure I" — a naming collision intrinsic to the filing, not an extraction error. Flagged for awareness, no action needed.

---

## 7. LIMITED REVIEW REPORT — CONSOLIDATED (pages 2-4, lines 92-176)

Auditor: B S R & Co. LLP, Chartered Accountants, Firm Registration No. 101248W/W-100022. Partner: Rakesh Dewan, Membership No. 092212. Place: Gurugram. Report date: 31 July 2026. UDIN: 26092212TUIKRA9037 (line 171).

| Para | Line | Type / content | First 15 words | Flags |
|---|------|------|-----------------|-------|
| 1 | 100-110 | Scope statement — entities reviewed | "We have reviewed the accompanying Statement of unaudited consolidated financial results of Urban..." | Scope includes Parent + subsidiaries + share of JV and trusts; prior-year comparative (Q1FY26) figures approved by Board but NOT reviewed |
| 2 | 111-116 | Management responsibility / Ind AS 34 basis | "This Statement, which is the responsibility of the Parent's management and approved by the Parent's..." | |
| 3 | 117-126 | Review standard (SRE 2410) / scope-of-review limitation | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | Explicit "we do not express an audit opinion" (line 124) |
| 4 | 127 | Cross-reference to Annexure I entity list | "The Statement includes the results of the entities mentioned in Annexure I to the Statement." | |
| 5 | 128-132 | Other-matter-type: Q4FY26 balancing-figure caveat, predecessor-auditor reliance for 9M FY26 | "Attention is drawn to the fact that the figures for the three months ended 31 March 2026..." | Emphasis-of-matter-like paragraph (not formally headed as such) |
| 6 | 133-138 | Conclusion (unmodified / negative-assurance) | "Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing..." | Standard SRE 2410 unmodified conclusion |
| 7 | 150-152 | Other-matter: predecessor auditor's FY26 audit opinion | "The consolidated financial results of the Group and its joint venture for the year ended 31 March 2026..." | Predecessor auditor's report dated 08 May 2026, unmodified opinion — auditor changeover context (predecessor vs B S R & Co. LLP as current reviewer) |
| 8 | 153-159 | Other-matter: unreviewed trust disclosure | "The Statement includes the unaudited financial results of one trust which has not been reviewed..." | AMBIGUOUS_ENTITY_REFERENCE (see Section 5) — trust unnamed; Nil revenue/PAT/TCI; management-represented as immaterial; "conclusion is not modified in respect of this matter" |
| — | 161-171 | Signature/attestation block | For B S R & Co. LLP / Rakesh Dewan, Partner / Membership No. 092212 / Gurugram / 31 July 2026 / UDIN: 26092212TUIKRA9037 | Not a numbered paragraph; date only (no HH:MM digital timestamp on auditor block, unlike company officer signatures in Section 9 |

Consolidated auditor paragraphs (numbered): 8.

---

## 8. LIMITED REVIEW REPORT — STANDALONE (pages 8-9, lines 405-480)

Same auditor, partner, firm registration, and report date as Section 7. UDIN: 26092212PVXRVQ3080 (line 475) — distinct UDIN from the consolidated report's UDIN (line 171), as required (one UDIN per report).

| Para | Line | Type / content | First 15 words | Flags |
|---|------|------|-----------------|-------|
| 1 | 413-420 | Scope statement — entity reviewed | "We have reviewed the accompanying Statement of unaudited standalone financial results of Urban..." | Scope statement explicitly states standalone Statement "in which are included financial results of Urban Company ESOP Trust" (line 416-417); prior-year comparative (Q1FY26) approved by Board but not reviewed |
| 2 | 421-427 | Management responsibility / Ind AS 34 basis | "This Statement, which is the responsibility of the Company's management and approved by its Board..." | |
| 3 | 428-435 | Review standard (SRE 2410) / scope-of-review limitation | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | "we do not express an audit opinion" (line 435) |
| 4 | 436-440 | Other-matter-type: Q4FY26 balancing-figure caveat | "Attention is drawn to the fact that the figures for the three months ended 31 March 2026..." | Identical substance to consolidated para 5 |
| 5 | 441-446 | Conclusion (unmodified / negative-assurance) | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." | Standard SRE 2410 unmodified conclusion |
| 6 | 462-463 | Other-matter: predecessor auditor's FY26 audit opinion | "The standalone financial results of the Company for the year ended 31 March 2026 were audited by..." | Predecessor auditor, report dated 08 May 2026, unmodified opinion |
| — | 465-475 | Signature/attestation block | For B S R & Co. LLP / Rakesh Dewan, Partner / Membership No. 092212 / Gurugram / 31 July 2026 / UDIN: 26092212PVXRVQ3080 | Not a numbered paragraph; no HH:MM timestamp |

Standalone auditor paragraphs (numbered): 6.

Note: standalone review report has no equivalent to consolidated para 8 (unreviewed trust) or para 4 (Annexure I entity-list cross-reference) — expected, since the standalone Statement scope is limited to the Company plus the one named trust (ESOP Trust), not a multi-entity consolidation.

Auditor paragraphs total (numbered, both reports): 8 + 6 = 14.

---

## 9. DIGITAL SIGNATURE BLOCKS (timestamp vs board meeting end 15:25)

| # | Line | Signatory | Designation | Document | Timestamp | Flags |
|---|------|-----------|-------------|----------|-----------|-------|
| 1 | 52-63 | Sonali Singh | Company Secretary and Compliance Officer (Membership No. A26585) | Reg 30/33 outcome letter (page 1) | 2026.07.31 15:47:12 +05'30' | 22 min after meeting concluded (15:25) — expected, this is the post-meeting disclosure letter itself |
| 2 | 384-394 | Abhiraj Singh Bhal | Chairperson, Managing Director and CEO (DIN: 07005253) | Consolidated financial results (page 7) | 2026.07.31 15:23:46 +05'30' | SIG_BEFORE_MEETING_END — signed 1 min 14 sec BEFORE the stated board meeting conclusion time of 15:25 |
| 3 | 572-582 | Abhiraj Singh Bhal | Chairperson, Managing Director and CEO (DIN: 07005253) | Standalone financial results (page 11) | 2026.07.31 15:22:53 +05'30' | SIG_BEFORE_MEETING_END — signed 2 min 7 sec BEFORE the stated board meeting conclusion time of 15:25 |

Signature blocks total: 3. Two of three carry SIG_BEFORE_MEETING_END.

---

## FLAGS SUMMARY
- ZERO_STANDING: 9 line items (5 consolidated statement, 4 standalone statement)
- TEMPLATE_LINE_ACTIVATED: 1 (Exceptional items, consolidated statement line 260 — zero/dash in all 3 comparative periods, non-zero this quarter)
- ENTITY_CHANGE: 1 (Annexure I entity 7, Urban Company Arabia for Information Technology, liquidated 24 May 2026)
- AMBIGUOUS_ENTITY_REFERENCE: 1 (unnamed unreviewed trust in consolidated review report para 8 — Section 5)
- SIG_BEFORE_MEETING_END: 2 (both Abhiraj Singh Bhal signatures on the consolidated and standalone results, timestamped before the stated 15:25 board meeting conclusion)

---
```yaml
stage: A2-enumerator
company: "URBANCO"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/urbanco-q1fy27/work/ledger_results_URBANCO_q1fy27.md"
counts:
  notes: 16
  line_items: 88
  zero_standing: 9
  agenda_items: 1
  auditor_paras: 14
  entities: 10
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, TEMPLATE_LINE_ACTIVATED, ENTITY_CHANGE, AMBIGUOUS_ENTITY_REFERENCE, SIG_BEFORE_MEETING_END]
gate_a2: pass
mismatch_note: ""
```
