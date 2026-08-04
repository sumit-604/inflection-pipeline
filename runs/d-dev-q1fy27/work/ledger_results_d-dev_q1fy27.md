# A2 COMPLETENESS LEDGER — DEE Development Engineers Ltd (D-DEV / BSE 544198)
Doctype: results | Quarter: Q1 FY27 (quarter ended 30 June 2026)
Source: DOC1_board_outcome_full_results.pdf (17 pages, Rs. Lakhs, x0.01 to Cr)
A1 extract: /home/user/inflection-pipeline/runs/d-dev-q1fy27/work/extract_results_d-dev_q1fy27.txt
Prior-quarter ledger: not supplied — no diff performed; `ENTITY_CHANGE` / `DROPPED_SLIDE` style
carry-forward flags cannot be computed this run (flag as `NO_PRIOR_LEDGER`).

```
=== A2 COUNT TEST ===
category: board_agenda_items      grep_count: 11   sweep_count: 11   match: yes
category: notes_standalone        grep_count: 7    sweep_count: 7    match: yes
category: notes_consolidated      grep_count: 7*   sweep_count: 7    match: yes
category: annexures               grep_count: 8    sweep_count: 8    match: yes
category: segment_rows_standalone grep_count: 21   sweep_count: 21   match: yes
category: segment_rows_consol     grep_count: 27   sweep_count: 27   match: yes
category: line_items_standalone   grep_count: 28   sweep_count: 28   match: yes
category: line_items_consol       grep_count: 38   sweep_count: 38   match: yes
category: auditor_paras_standalone grep_count: 5   sweep_count: 5    match: yes
category: auditor_paras_consol    grep_count: 9    sweep_count: 9    match: yes
category: consolidation_entities  grep_count: 6    sweep_count: 6    match: yes
category: digital_signatures      grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```
*Consolidated-notes raw regex `^\s*[0-9]+ [A-Z]` on the notes block (lines 629-679) returns 8
hits; the 8th (line 671) is a table date-header row "30 June 2026  31 March 2026 ..." inside
Note 6's sub-table, not a numbered note. Excluded after manual verification (see Notes —
Consolidated table below). Reconciled sweep count = 7, matching standalone.

Grep bases used:
- board_agenda_items: `sed -n '15,160p' extract | grep -c -E "^[0-9]+\.[[:space:]]+[A-Z]"`
- notes_standalone: `sed -n '359,397p' extract | grep -c -E "^[0-9]+ [A-Z]"`
- notes_consolidated: `sed -n '629,679p' extract | grep -c -E "^\s*[0-9]+ [A-Z]"` (see note above)
- annexures: `grep -c -E "^\s*Annexure [A-Z]:" extract`
- segment_rows_standalone: `sed -n '333,357p' extract | grep -c -E "^\s*(a\)|b\)|c\)|Total|Revenue from operations|Operating profit|Less:|Add:|Profit before tax|Profit after tax)"`
- segment_rows_consol: same pattern + `d\)` on `sed -n '597,627p'`
- line_items_standalone / consol: `grep -c -E "[0-9]{1,3}(,[0-9]{3})*\.[0-9]{2}|[[:space:]]-[[:space:]]"` on the respective statement blocks (289-322 / 541-589)
- auditor_paras: `sed -n '<block>p' extract | grep -c -E "^\s*[0-9]+\.\s"` on standalone (196-275) and consolidated (419-526) report blocks
- consolidation_entities: manual count of numbered rows in the entity table, lines 450-460
- digital_signatures: `grep -c -i "digitally signed"` on full extract

---

## 1. BOARD OUTCOME — AGENDA ITEMS (cover letter, pages 1-3)

| # | Item | Line | Subject (1st ~15 words) | Annexure | Flags |
|---|------|------|--------------------------|----------|-------|
| 1 | Item 1 | 34 | Approval of Unaudited Financial Results (Standalone & Consolidated) for Q1 FY27 with Limited Review Report | Annexure A | — |
| 2 | Item 2 | 41 | Reclassification and increase in Authorised Share Capital (Rs. 85 Cr to Rs. 95 Cr) and alteration of Capital Clause of MOA | Annexure B | — |
| 3 | Item 3 | 52 | Increase in Managerial Remuneration of Ms. Shikha Bansal, WTD, from Rs. 38.49 Lakhs to Rs. 1.38 Cr p.a. | — (no lettered annexure; detail in body) | — |
| 4 | Item 4 | 61 | Related Party Transaction — taking Office Premises on Rent, Ms. Shikha Bansal WTD, combined rent not exceeding Rs. 70,000/month, 11 months | Annexure C | — |
| 5 | Item 5 | 80 | Appointment of Ms. Ashvika Bansal, relative of a director, as CSR Head, Rs. 2,40,000/month | Annexure D | — |
| 6 | Item 6 | 88 | Approval for issuance/allotment of Equity Shares on conversion of Rs. 2,000 Cr loan facility (Bank of India-led consortium) pursuant to Sec 62(3) | Annexure E | — |
| 7 | Item 7 | 103 | Continuation of Directorship of Mr. Bhisham Kumar Gupta (DIN 09493608), Independent Director, beyond age 75 (to Jul 11, 2028) | Annexure F | — |
| 8 | Item 8 | 110 | Re-appointment of Ms. Shikha Bansal (DIN 02712175) as Whole-time Director, liable to retire by rotation | Annexure G | — |
| 9 | Item 9 | 115 | Re-appointment of Mrs. Shruti Aggarwal (DIN 08598962) as Whole-time Director, liable to retire by rotation | Annexure H | — |
| 10 | Item 10 | 122 | Convening of 37th AGM and related matters (Notice, Annual Report FY25-26, Book Closure, e-voting) | — | — |
| 11 | Item 11 | 130 | Re-constitution of Board Committees: (i) Stakeholders Relationship Committee, (ii) CSR Committee — full new composition given | Annexure I | — |

Sub-rows inside item 11 (committee compositions, not separately numbered agenda items, listed for
completeness):
- 11.i SRC members: Krishan Lalit Bansal (Chair), Shruti Aggarwal, Shilpi Barar, Ashwani Kumar Prabhakar, Bhisham Kumar Gupta — lines 133-137, 146
- 11.ii CSR Committee members: Shilpi Barar (Chair), Krishan Lalit Bansal, Shruti Aggarwal, Ashwani Kumar Prabhakar, Bhisham Kumar Gupta — lines 148-153

Board meeting timing: commenced 09:00 A.M., concluded 10:52 A.M. — line 159 (duration 1h52m for
an 11-item agenda including two capital/RPT resolutions and five appointment/re-appointment items).

Signatory (cover letter): Ranjan Kumar Sarangi, Company Secretary and Compliance Officer,
Membership No. F8604 — lines 171-173 (no digital timestamp on this letter itself, unlike the
auditor and CFO/CMD signature blocks below).

Count: 11 board agenda items (grep and sweep agree).

---

## 2. STANDALONE — INDEPENDENT AUDITOR'S LIMITED REVIEW REPORT (pages 4-5)

| Para | Line | Subject |
|------|------|---------|
| 1 | 204 | Scope statement — reviewed unaudited standalone financial results for quarter ended 30 June 2026 |
| 2 | 210 | Management responsibility for preparation per Ind AS 34; auditor responsibility to express a conclusion |
| 3 | 218 | Review conducted per SRE 2410; moderate assurance, not an audit opinion |
| 4 | 229 | Conclusion — nothing has come to attention indicating material misstatement (unmodified/clean conclusion) |
| 5 | 244 | **Emphasis of Matter** — refers to Note 6 (PSPCL/PSERC/APTEL tariff dispute, sub-judice, no adjustments made); conclusion not modified |

Auditor: S.R. Batliboi & Co LLP, LLP ID AAB-4294, ICAI Firm Reg No. 301003E/E300005 — line 240, 259.
Signatory: Rajeev Sawhney, Partner, Membership No. 096333 — lines 268-270.
UDIN: 26096333OSCLDJ9635 — line 271.
Digital signature timestamp: 2026.08.04 10:59:41 +05'30' — line 265. Board meeting concluded
10:52 A.M. (line 159); this standalone auditor signature is timestamped ~7 minutes AFTER board
conclusion — consistent sequencing, no flag.
Place/date: Gurugram, Haryana, August 04, 2026 — lines 273-274.

Count: 5 numbered paragraphs (para 5 = EOM). Entity list reviewed: standalone report covers only
the Company itself (no subsidiary entity table — that appears only in the consolidated report).
No Other Matters paragraph, no Going Concern paragraph, no qualification/disclaimer in the
standalone report (contrast with consolidated report, section 3 below).

---

## 3. STANDALONE — STATEMENT OF UNAUDITED FINANCIAL RESULTS (page 6, lines 285-322)

Columns: Quarter ended 30-06-2026 (Unaudited) | 31-03-2026 (Audited) | 30-06-2025 (Unaudited) |
Year Ended 31-03-2026 (Audited).

| Row | Line | Item | Flags |
|-----|------|------|-------|
| I | 289 | Revenue from operations | — |
| II | 290 | Other income | — |
| III | 291 | Total income | — |
| IV.a | 293 | Cost of material consumed | — |
| IV.b | 294 | Purchase of stock in trade | — |
| IV.c | 295 | Changes in inventories of finished goods, WIP and stock in trade | — |
| IV.d | 296 | Employee benefits expense | — |
| IV.e | 297 | Finance costs | — |
| IV.f | 298 | Depreciation and amortisation expense | — |
| IV.g | 299 | Consumption of stores and spare parts | — |
| IV.h | 300 | Other expenses | — |
| IV (total) | 301 | Total expense (a to h) | — |
| V | 302 | Profit before exceptional items and tax | — |
| VI | 304 | Exceptional items — Impact of Labour Codes (Refer note 5) | `ZERO_STANDING` (dash in 30-06-2026 and 30-06-2025 columns; nonzero in the two 31-03 columns) |
| VII | 305 | Profit before tax | — |
| VII.a | 306 | Current tax | — |
| VII.b | 307 | Adjustment of tax related to earlier years | `ZERO_STANDING` (dash in 3 of 4 periods, incl. current quarter) |
| VII.c | 308 | Deferred tax charge/(credit) | — |
| VIII | 309 | Total tax expense | — |
| IX | 310 | Profit for the period/year | — |
| X.a | 313 | Remeasurement of net defined benefit liability/asset, net | — |
| X.b | 314 | Income tax effect | — |
| X (total) | 315 | Total other comprehensive income, net of tax | — |
| XI | 316 | Total comprehensive income | — |
| XII | 317 | Paid up share capital (par value Rs. 10 each, fully paid) | — |
| XIII | 318 | Other equity | `ZERO_STANDING` (dash in all three quarter columns; value 81,780.51 only in year-ended column — standard for interim filings) |
| XIV.a | 320 | Earnings per equity share — Basic | — |
| XIV.b | 321 | Earnings per equity share — Diluted | — |

Footnote line 322: "**Not annualised except for the year end" — qualifies EPS rows, captured.

Count: 28 data-bearing line items; 3 flagged `ZERO_STANDING`.

---

## 4. STANDALONE — SEGMENT INFORMATION (page 7, lines 325-357)

Two reportable segments: Piping division, Power division (no Heavy fabrication segment at
standalone level — contrast with consolidated, section 8).

| Block | Row | Line | Item |
|-------|-----|------|------|
| Segment revenue | a | 334 | Piping division |
| Segment revenue | b | 335 | Power division |
| Segment revenue | Total | 336 | Total |
| Segment revenue | — | 337 | Revenue from operations (cross-check line, equals Total) |
| Segment results | a | 339 | Piping division |
| Segment results | b | 340 | Power division |
| Segment results | c | 341 | Unallocated |
| Segment results | — | 342 | Operating profit before interest and tax |
| Segment results | — | 343 | Less: Interest expense |
| Segment results | — | 344 | Add: Interest income |
| Segment results | — | 345 | Profit before tax |
| Segment results | — | 346 | Less: Tax expense |
| Segment results | — | 347 | Profit after tax |
| Segment assets | a | 349 | Piping division |
| Segment assets | b | 350 | Power division |
| Segment assets | c | 351 | Unallocated |
| Segment assets | Total | 352 | Total assets |
| Segment liabilities | a | 354 | Piping division |
| Segment liabilities | b | 355 | Power division |
| Segment liabilities | c | 356 | Unallocated |
| Segment liabilities | Total | 357 | Total liabilities |

Count: 21 segment rows (4 revenue + 9 results + 4 assets + 4 liabilities). No zero-standing rows
in this block — all segments carry values in all periods.

---

## 5. STANDALONE — NUMBERED NOTES (page 8, lines 360-397)

| Note | Line | Subject (first ~15 words) |
|------|------|----------------------------|
| 1 | 361 | Basis of preparation — Ind AS per Companies (Ind AS) Rules 2015, Section 133, Reg 33 SEBI LODR |
| 2 | 365 | Results reviewed by Audit Committee, approved by Board 04 Aug 2026; statutory auditors carried out limited review |
| 3 | 368 | CEO and CFO certificate under Reg 33 placed before the Board of Directors |
| 4 | 369 | Results will be made available on Company/BSE/NSE websites |
| 5 | 370 | Labour Codes (Code on Wages 2019 etc.) — Exceptional item table: past service cost charge, quarter/year figures | (contains the ZERO_STANDING table row cross-referenced in section 3 above) |
| 6 | 381 | PSPCL/PSERC/APTEL tariff dispute — 30-year PPA, 8 MW Abohar biomass plant, retrospective tariff revision, sub-judice, High Court stay | (this is the Emphasis of Matter note referenced by the standalone auditor report, section 2) |
| 7 | 395 | Q4 FY26 figures are balancing figures between full-year audited and 9M published figures |

Signature block: For and on behalf of the Board — Krishan Lalit Bansal, Chairman and Managing
Director, digitally signed 2026.08.04 10:49:58 +05'30' (line 401-407) — this signature timestamp
is BEFORE the board meeting's stated conclusion time of 10:52 A.M. (line 159). Flag `SIG_BEFORE_CONCLUSION`.
Place: Palwal, Haryana; Date: 04 August 2026 (line 406-407).

Count: 7 numbered notes.

---

## 6. CONSOLIDATED — INDEPENDENT AUDITOR'S LIMITED REVIEW REPORT (pages 9-10)

| Para | Line | Subject |
|------|------|---------|
| 1 | 426 | Scope statement — reviewed unaudited consolidated financial results (Holding Company + subsidiaries = "the Group") |
| 2 | 432 | Management responsibility for preparation per Ind AS 34; auditor responsibility to express conclusion |
| 3 | 439 | Review conducted per SRE 2410; also performed SEBI Master Circular Reg 33(8) procedures |
| 4 | 450 | Entity list — Statement includes results of 6 named entities (table below) |
| 5 | 462 | **Qualification basis** — Malwa Power Pvt Ltd (Rs. 5,082.67 lacs assets); PPA expired Apr 27, 2025; management has NOT carried out impairment assessment; auditor unable to determine impairment / consequential impact |
| 6 | 477 | Conclusion — "except for the possible effects of our observation in para 5 above," nothing else came to attention (this is a QUALIFIED conclusion, not clean) |
| 7 | 486 | **Emphasis of Matter** — refers to Note 4 (PSPCL/PSERC/APTEL tariff dispute), same substance as standalone Note 6; conclusion not modified by this EOM (but IS modified by para 5 qualification) |
| 8 | 495 | Reliance on other auditors — 5 subsidiaries reviewed by respective independent auditors; revenue Rs. 5,852.85 lacs, PAT Rs. 555.96 lacs, TCI Rs. 499.20 lacs |
| 9 | 500 | Other auditors' reports furnished by management; conclusion for those entities based solely on those reports, not modified w.r.t. reliance |

Auditor: S.R. Batliboi & Co LLP, same firm/registration as standalone (line 473, 511).
Signatory: Rajeev Sawhney, Partner, Membership No. 096333 (line 519-521).
UDIN: 26096333UVNOZW1843 — line 522 (distinct UDIN from standalone report, as expected for a
separate report).
Digital signature timestamp: 2026.08.04 11:01:33 +05'30' — line 517.
Place/date: Gurugram, Haryana, August 04, 2026 (line 524-525).

**Consolidation entity list** (para 4, lines 450-460):

| S.No. | Entity | Relationship | Line |
|-------|--------|--------------|------|
| 1 | DEE Development Engineers Limited | Holding Company | 454 |
| 2 | DEE Fabricom India Private Limited | Subsidiary Company | 455 |
| 3 | DEE Piping Systems (Thailand) Co. Limited | Subsidiary Company | 456 |
| 4 | Malwa Power Private Limited | Subsidiary Company | 457 |
| 5 | Molsieve Designs Limited | Subsidiary Company | 458 |
| 6 | Atul Krishan Bansal Foundation | Subsidiary Company | 459 |

Count: 9 numbered paragraphs (para 5 = qualification basis, para 7 = EOM, paras 8-9 = other-auditor
reliance). 6 consolidated entities. No prior-quarter entity list was supplied for this run, so
`ENTITY_CHANGE` cannot be tested — flagged `NO_PRIOR_LEDGER`.

Note: this is materially different report language from the standalone report — standalone report
(section 2) is a clean/unmodified conclusion with only an EOM; the consolidated report carries an
explicit qualification (para 5/6) on top of the EOM. This distinction is a first-class enumeration
fact, not an interpretation.

---

## 7. CONSOLIDATED — STATEMENT OF UNAUDITED FINANCIAL RESULTS (page 11, lines 535-589)

Columns identical structure to standalone (30-06-2026 Unaudited / 31-03-2026 Audited / 30-06-2025
Unaudited / FY26 Audited).

| Row | Line | Item | Flags |
|-----|------|------|-------|
| I | 541 | Revenue from operations | — |
| II | 542 | Other income | — |
| III | 543 | Total income | — |
| IV.a | 545 | Cost of material consumed | — |
| IV.b | 546 | Purchase of stock in trade | — |
| IV.c | 547 | Changes in inventories of finished goods, WIP and stock in trade | — |
| IV.d | 548 | Employee benefits expense | — |
| IV.e | 549 | Depreciation and amortisation expense | — |
| IV.f | 550 | Finance costs | — |
| IV.g | 551 | Consumption of stores and spare parts | — |
| IV.h | 552 | Other expenses | — |
| IV (total) | 553 | Total expense (a to h) | — |
| V | 554 | Profit before exceptional items and tax | — |
| VI | 556 | Exceptional items — Impact of Labour Codes (Refer note 6) | `ZERO_STANDING` (dash in 30-06-2026 and 30-06-2025 columns) |
| VII | 557 | Profit before tax | — |
| VII.a | 558 | Current tax | — |
| VII.b | 559 | Adjustment of tax related to earlier years | `ZERO_STANDING` (dash in 2 of 4 periods, incl. current quarter) |
| VII.c | 560 | Deferred tax charge/(credit) | — |
| VIII | 561 | Total tax expense | — |
| IX | 562 | Profit for the period/year | — |
| X.a | 565 | Remeasurement of net defined benefit liability/asset, net | — |
| X.b | 566 | Income tax effect | — |
| X.a (reclass.) | 568 | Exchange differences on translation of foreign operations | — |
| X (total) | 569 | Total other comprehensive income/(loss), net of tax | — |
| XI | 570 | Total comprehensive income | — |
| XII | 573 | Profit attributable to: Equity holders of the parent | — |
| XII | 574 | Profit attributable to: Non-controlling interest | — |
| XII | 575 | Profit attributable to: Total | — |
| XIII | 577 | OCI attributable to: Equity holders of the parent | — |
| XIII | 578 | OCI attributable to: Non-controlling interest | `ZERO_STANDING` (dash in ALL FOUR periods) |
| XIII | 579 | OCI attributable to: Total | — |
| XIV | 581 | TCI attributable to: Equity holders of the parent | — |
| XIV | 582 | TCI attributable to: Non-controlling interest | — |
| XIV | 583 | TCI attributable to: Total | — |
| XV | 584 | Paid up share capital (par value Rs. 10 each, fully paid) | — |
| XVI | 585 | Other equity | `ZERO_STANDING` (dash in all three quarter columns; value 82,112.20 only in year-ended column) |
| XVII.a | 587 | Earnings per equity share — Basic | — |
| XVII.b | 588 | Earnings per equity share — Diluted | — |

Footnote line 589: "**Not annualised except for the year end."

Count: 38 data-bearing line items; 4 flagged `ZERO_STANDING`. 10 more line items than standalone,
driven by the parent/NCI attribution splits (XII-XIV, three rows each) absent from the standalone
statement, and the additional reclassified-OCI exchange-translation row (X.a reclass, line 568).

---

## 8. CONSOLIDATED — SEGMENT INFORMATION (page 12, lines 592-627)

Four reportable segments at consolidated level: Piping division, Power division, Heavy
fabrication, Unallocated — one more segment (Heavy fabrication) than the standalone statement,
which reports only Piping and Power (section 4). This is a structural presence-matrix fact.

| Block | Row | Line | Item |
|-------|-----|------|------|
| Segment revenue | a | 598 | Piping division |
| Segment revenue | b | 599 | Power division |
| Segment revenue | c | 600 | Heavy fabrication |
| Segment revenue | d | 601 | Unallocated |
| Segment revenue | Total | 602 | Total |
| Segment revenue | — | 603 | Less: Inter segment revenue |
| Segment revenue | — | 604 | Revenue from operations (net of inter-segment) |
| Segment results | a | 606 | Piping division |
| Segment results | b | 607 | Power division |
| Segment results | c | 608 | Heavy fabrication |
| Segment results | d | 609 | Unallocated |
| Segment results | — | 610 | Operating profit before interest and tax |
| Segment results | — | 611 | Less: Interest expense |
| Segment results | — | 612 | Add: Interest income |
| Segment results | — | 613 | Profit before tax |
| Segment results | — | 614 | Less: Tax expense |
| Segment results | — | 615 | Profit after tax |
| Segment assets | a | 617 | Piping division |
| Segment assets | b | 618 | Power division |
| Segment assets | c | 619 | Heavy fabrication |
| Segment assets | d | 620 | Unallocated |
| Segment assets | Total | 621 | Total assets |
| Segment liabilities | a | 623 | Piping division |
| Segment liabilities | b | 624 | Power division |
| Segment liabilities | c | 625 | Heavy fabrication |
| Segment liabilities | d | 626 | Unallocated |
| Segment liabilities | Total | 627 | Total liabilities |

Count: 27 segment rows (7 revenue + 10 results + 5 assets + 5 liabilities). No zero-standing rows.

---

## 9. CONSOLIDATED — NUMBERED NOTES (page 13, lines 630-677)

| Note | Line | Subject (first ~15 words) |
|------|------|----------------------------|
| 1 | 631 | Basis of preparation — reviewed by Audit Committee, approved by Board 04 Aug 2026; Ind AS basis; Group = Holding Co + subsidiaries |
| 2 | 636 | CEO/CFO certificate under Reg 33 placed before Board |
| 3 | 637 | Results available on Company/BSE/NSE websites |
| 4 | 638 | PSPCL/PSERC/APTEL tariff dispute — 30-year PPA, 8 MW Abohar biomass plant, sub-judice, High Court stay (same dispute as standalone Note 6; this is the EOM note referenced by consolidated auditor para 7) |
| 5 | 652 | Malwa Power Private Limited (MPPL) — 6 MW biomass plant, PPA expired 27 April 2025, PSERC/APTEL tariff proceedings, assets Rs. 5,082.67 lakhs, impairment impact NOT assessed by management (this is the note underlying the consolidated auditor's qualification, para 5) |
| 6 | 666 | Labour Codes — Exceptional item table, Group-level past service cost charge, quarter/year figures | (contains ZERO_STANDING row cross-referenced in section 7) |
| 7 | 676 | Q4 FY26 figures are balancing figures between audited full-year and 9M published figures, subject to limited review |

Signature block: For and on behalf of the Board — Krishan Lalit Bansal, Chairman and Managing
Director, digitally signed 2026.08.04 10:50:53 +05'30' (lines 683-690) — also BEFORE the stated
board conclusion time of 10:52 A.M. Flag `SIG_BEFORE_CONCLUSION` (second instance; see standalone
Note section 5 for the first).
Place: Palwal, Haryana; Date: 04 August 2026 (line 689-690).

Count: 7 numbered notes.

---

## 10. STANDALONE vs CONSOLIDATED PRESENCE MATRIX

| Disclosure unit | Standalone | Consolidated | Notes on difference |
|---|---|---|---|
| Limited Review Report | Yes (pages 4-5, 5 paras) | Yes (pages 9-10, 9 paras) | Consolidated report is longer: adds entity list (para 4), a qualification on Malwa Power impairment (para 5-6), and other-auditor reliance (paras 8-9); standalone is unmodified/clean, consolidated is qualified |
| Statement of Results | Yes (28 line items) | Yes (38 line items) | Consolidated adds NCI attribution rows (XII-XIV) and a reclassified-OCI FX translation row absent from standalone |
| Segment Information | Yes (2 segments: Piping, Power; 21 rows) | Yes (4 segments: Piping, Power, Heavy fabrication, Unallocated; 27 rows) | Heavy fabrication segment exists only at consolidated level (subsidiary-level activity not present standalone); consolidated also shows an explicit inter-segment revenue elimination line absent from standalone |
| Numbered Notes | Yes (7 notes) | Yes (7 notes) | Numbering does not map 1:1 by subject: standalone Note 6 (PSPCL EOM) = consolidated Note 4; standalone Note 5 (Labour Codes) = consolidated Note 6; consolidated Note 5 (Malwa Power impairment) has NO standalone equivalent — Malwa Power is a subsidiary, consolidated-only disclosure |
| CEO/CFO certificate note | Yes (Note 3) | Yes (Note 2) | present both, different note numbers |
| Basis-of-preparation note | Yes (Note 1) | Yes (Note 1) | present both |
| Website-availability note | Yes (Note 4) | Yes (Note 3) | present both, different note numbers |
| Balancing-figures note (Q4 FY26) | Yes (Note 7) | Yes (Note 7) | present both, same number coincidentally |
| Malwa Power impairment note | No | Yes (Note 5) | consolidated-only; underlies the auditor's qualification |
| UDIN | 26096333OSCLDJ9635 | 26096333UVNOZW1843 | distinct, both present |
| Digital signature (auditor) | 10:59:41 | 11:01:33 | both after board conclusion (10:52 A.M.) |
| Digital signature (CMD) | 10:49:58 | 10:50:53 | both BEFORE board conclusion (10:52 A.M.) — flagged `SIG_BEFORE_CONCLUSION` both instances |

---

## 11. ANNEXURES B THROUGH I (pages 14-17)

| Annexure | Line | Subject | Table rows enumerated |
|----------|------|---------|------------------------|
| B | 697 | Reclassification and Increase in Authorised Share Capital and alteration of Capital Clause of MOA | 6 rows: (1) Type of capital, (2) Existing Authorised Share Capital, (3) Proposed Increased Authorised Share Capital, (4) Reason for increase, (5) Manner of alteration of MOA, (6) Mode of approval — lines 702-723 |
| C | 727 | Related Party Transaction for taking Office Premises on Rent | 9 rows: (1) Name of Related Party, (2) Relationship, (3) Nature of Transaction, (4) Purpose of Transaction, (5) Tenure of Agreement, (6) Monthly Rent/Total Value, (7) Arm's Length Basis, (8) Audit Committee Approval, (9) Materiality — lines 730-739 |
| D | 741 | Appointment of Ms. Ashvika Bansal as CSR Head | 8 rows: (1) Name, (2) Designation, (3) Reason for change, (4) Date of Appointment & term, (5) Brief Profile, (6) Disclosure of relationships, (7) Remuneration, (8) Other Directorships — lines 744-780 |
| E | 783 | Approval for issuance/allotment of Equity Shares on conversion of loan facility (Sec 62(3)) | 9 rows: (1) Name of Lender, (2) Amount of Loan, (3) Type of issuance, (4) Names of investors, (5) Trigger for Conversion, (6) Type of Security, (7) Conversion Price, (8) Number of Shares, (9) Approval Required — lines 787-804 |
| F | 816 | Continuation of Directorship of Mr. Bhisham Kumar Gupta beyond age 75 | 12 rows: (1) Name, (2) DIN, (3) Category, (4) Reason for change, (5) Date of Birth, (6) Current Term, (7) Date of attaining age 75, (8) Period of Continuation approved, (9) Brief Profile, (10) Disclosure of relationships, (11) Directorship in other listed entities, (12) BSE Circular information — lines 820-847 |
| G | 849 | Re-appointment of Ms. Shikha Bansal (DIN 02712175) as Whole-time Director | 8 rows: (1) Name, (2) DIN, (3) Category, (4) Reason for change, (5) Date & Time, (6) Brief Profile, (7) Disclosure of relationships, (8) BSE Circular information — lines 853-874 |
| H | 884 | Re-appointment of Mrs. Shruti Aggarwal (DIN 08598962) as Whole-time Director | 8 rows: (1) Name, (2) DIN, (3) Category, (4) Reason for change, (5) Date & Term, (6) Brief Profile, (7) Disclosure of relationships, (8) BSE Circular information — lines 888-909 |
| I | 911 | Re-constitution of Committees of the Board | 6 rows: (1) Reason for change, (2) Date of re-constitution, (3) Details of Committees re-constituted, (4) New Composition (SRC — 5 members, CSR — 5 members), (5) Brief Profile of new inductees, (6) Relationship with other Directors — lines 914-939 |

Note: "Annexure A" (the results + Limited Review Report, referenced at line 39) is not a separate
governance-disclosure annexure — it IS the standalone/consolidated statement + review report
enumerated in sections 2-9 above; it is not double-counted in the B-I governance-annexure count.

Director/appointee profile detail captured per operating rule 4 (name, DIN where applicable, role,
term dates, background, relationships):

| Name | DIN | Role | Term / dates | Relationship disclosed |
|------|-----|------|---------------|--------------------------|
| Ms. Ashvika Bansal | n/a (not a director) | CSR Head | Appointed 04.08.2026, appointment letter | Relative of a Director (Annexure D row 6, line 776) |
| Mr. Bhisham Kumar Gupta | 09493608 | Independent Director | Current term Jul 12 2023 - Jul 11 2028; continuation approved Jun 05 2027 - Jul 11 2028 | Not related to any other Director (Annexure F row 10, line 841) |
| Ms. Shikha Bansal | 02712175 | Whole-time Director, retire by rotation | 5 years, 01.11.2025 - 31.10.2030 | Part of Promoter Group (Annexure G row 7, line 870); also RPT counterparty in Item 4/Annexure C |
| Mrs. Shruti Aggarwal | 08598962 | Whole-time Director, retire by rotation | 5 years, 14.04.2025 - 13.04.2030 | Part of Promoter Group (Annexure H row 7, line 905) |

Count: 8 annexures (B-I).

---

## 12. CROSS-REFERENCE / CONSISTENCY OBSERVATIONS (enumerated, not interpreted)

- Standalone Note 6 and consolidated Note 4 describe the identical PSPCL/PSERC/APTEL dispute in
  near-identical language (lines 381-393 vs 638-649); both are referenced by their respective
  auditor report's Emphasis of Matter paragraph (standalone para 5, line 244; consolidated para 7,
  line 486).
- Malwa Power impairment: appears in consolidated auditor para 5 (line 462, "unable to determine
  whether any impairment is required"), consolidated Note 5 (line 652, "management is unable to
  assess the consequential impact"), and NOT in the standalone report or standalone notes at all
  (standalone financials exclude the subsidiary). Cross-referenced asset figure Rs. 5,082.67 lakhs
  appears identically at line 462 (auditor report) and line 662/665 (Note 5).
- Both digital-signature CMD blocks (standalone line 401-407, consolidated line 683-690) predate
  the stated board conclusion time of 10:52 A.M. (line 159) by 2-3 minutes (10:49:58 and 10:50:53
  respectively) while both auditor signatures postdate it (10:59:41 and 11:01:33). Flagged
  `SIG_BEFORE_CONCLUSION` for both CMD signature instances — enumerated as a fact for A3/A4, not
  interpreted here.
```

---

## FINAL COUNTS SUMMARY

- Board agenda items: 11 (lines 34-130, cover letter pages 1-3)
- Standalone numbered notes: 7 (lines 361-395)
- Consolidated numbered notes: 7 (lines 631-676)
- Annexures (B-I, governance disclosures): 8 (lines 697-939)
- Standalone segment rows: 21 (lines 334-357)
- Consolidated segment rows: 27 (lines 598-627)
- Standalone statement line items: 28 (3 flagged ZERO_STANDING)
- Consolidated statement line items: 38 (4 flagged ZERO_STANDING)
- Standalone auditor report paragraphs: 5 (para 5 = EOM)
- Consolidated auditor report paragraphs: 9 (para 5-6 = qualification, para 7 = EOM, para 8-9 = other-auditor reliance)
- Consolidation entities: 6
- Digital signature blocks: 4 (2 auditor, 2 CMD)
